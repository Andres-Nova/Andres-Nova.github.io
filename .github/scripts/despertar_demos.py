"""
Despierta los demos de Streamlit Cloud que hayan entrado en modo reposo.
Usa Playwright (navegador Chromium headless) para establecer una conexión
WebSocket real — la única forma que Streamlit Cloud reconoce como actividad.

Después de despertar, mantiene el navegador en la página durante 60 segundos
para que Streamlit registre la sesión como activa y reinicie su contador.

Ejecutado automáticamente por GitHub Actions cada 3 horas.
"""

import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

APPS = [
    ("credit-risk-colombia", "https://credit-risk-colombia.streamlit.app"),
    ("bogota-traffic-safety", "https://bogota-traffic-safety.streamlit.app"),
    ("academic-rag",          "https://academic-rag.streamlit.app"),
    ("sentiment-nlp-co",      "https://sentiment-nlp-co.streamlit.app"),
]

# Textos posibles del botón de despertar (Streamlit los muestra en inglés)
TEXTOS_DESPERTAR = [
    "Yes, get this app back up!",
    "Yes, get this app back up",
    "Wake it up",
]

# Selector que confirma que la app Streamlit cargó completamente
SELECTOR_APP_CARGADA = "[data-testid='stAppViewContainer'], [data-testid='stApp'], .main"

TIMEOUT_NAVEGACION  = 60_000   # 60 s para que cargue la página inicial
TIMEOUT_BOTON       =  8_000   # 8 s para detectar si aparece el botón de reposo
TIMEOUT_DESPERTAR   = 120_000  # 120 s para que el app arranque después de clicar
TIMEOUT_CARGA_APP   = 60_000   # 60 s para confirmar que la app cargó de verdad
TIEMPO_SESION_ACTIVA = 60_000  # 60 s manteniendo conexión activa (reinicia contador)


def despertar_app(page, nombre: str, url: str) -> None:
    print(f"\n🔄 Verificando {nombre} ...")
    try:
        page.goto(url, timeout=TIMEOUT_NAVEGACION, wait_until="domcontentloaded")
    except PlaywrightTimeout:
        print(f"  ⚠️  {nombre}: tiempo de carga agotado (puede estar iniciando)")
        return
    except Exception as e:
        print(f"  ❌ {nombre}: error al navegar — {e}")
        return

    # Buscar botón de despertar
    boton = None
    for texto in TEXTOS_DESPERTAR:
        candidato = page.get_by_text(texto, exact=False)
        try:
            candidato.wait_for(state="visible", timeout=TIMEOUT_BOTON)
            boton = candidato
            break
        except PlaywrightTimeout:
            continue

    if boton:
        print(f"  💤 {nombre} en reposo — clicando para despertar ...")
        try:
            boton.click()
            # Esperar a que desaparezca la pantalla de reposo
            page.wait_for_function(
                "() => !document.body.innerText.includes('gone to sleep')",
                timeout=TIMEOUT_DESPERTAR,
            )
            # Esperar a que el componente principal de Streamlit aparezca
            try:
                page.wait_for_selector(SELECTOR_APP_CARGADA, timeout=TIMEOUT_CARGA_APP)
                print(f"  🚀 {nombre} cargada — manteniendo sesión {TIEMPO_SESION_ACTIVA // 1000}s ...")
            except PlaywrightTimeout:
                print(f"  ⚠️  {nombre}: app iniciada pero selector no encontrado — esperando igualmente ...")

            # Mantener la conexión WebSocket activa para que Streamlit
            # registre la sesión y reinicie el contador de inactividad.
            page.wait_for_timeout(TIEMPO_SESION_ACTIVA)
            print(f"  ✅ {nombre} activa y sesión registrada")
        except PlaywrightTimeout:
            print(f"  ⚠️  {nombre}: clicado pero tardó demasiado en responder")
        except Exception as e:
            print(f"  ❌ {nombre}: error al despertar — {e}")
    else:
        print(f"  ✅ {nombre} ya estaba activa — manteniendo sesión {TIEMPO_SESION_ACTIVA // 1000}s ...")
        # También mantenemos la sesión cuando el app ya estaba activa
        page.wait_for_timeout(TIEMPO_SESION_ACTIVA)
        print(f"  ✅ {nombre} sesión renovada")


def main():
    print("=" * 55)
    print("  Verificando estado de los 4 demos de Streamlit")
    print("=" * 55)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for nombre, url in APPS:
            page = browser.new_page()
            despertar_app(page, nombre, url)
            page.close()
        browser.close()

    print("\n✔  Revisión completa")


if __name__ == "__main__":
    main()
