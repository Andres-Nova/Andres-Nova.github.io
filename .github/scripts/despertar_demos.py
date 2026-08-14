"""
Despierta los demos de Streamlit Cloud que hayan entrado en modo reposo.
Usa Playwright (navegador Chromium headless) para establecer una conexión
WebSocket real — la única forma que Streamlit Cloud reconoce como actividad.

Ejecutado automáticamente por GitHub Actions cada 6 horas.
"""

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

TIMEOUT_NAVEGACION = 60_000   # 60 s para que cargue la página inicial
TIMEOUT_BOTON      =  8_000   # 8 s para detectar si aparece el botón de reposo
TIMEOUT_DESPERTAR  = 90_000   # 90 s para que el app arranque después de clicar


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
            # Esperar a que desaparezca la pantalla de reposo y cargue la app
            page.wait_for_function(
                "() => !document.body.innerText.includes('gone to sleep')",
                timeout=TIMEOUT_DESPERTAR,
            )
            print(f"  ✅ {nombre} despertada y activa")
        except PlaywrightTimeout:
            print(f"  ⚠️  {nombre}: clicado pero tardó demasiado en responder")
        except Exception as e:
            print(f"  ❌ {nombre}: error al despertar — {e}")
    else:
        print(f"  ✅ {nombre} ya estaba activa")


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
