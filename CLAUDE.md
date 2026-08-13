# portafolio — Contexto para Claude

## Qué es este proyecto

Portafolio personal de Andres Nova publicado en GitHub Pages. Presencia profesional como Data Architect & AI Engineer.

**Ruta:** `/home/andres/Documentos/Codigo/Proyectos/portafolio/`
**Repo:** https://github.com/Andres-Nova/Andres-Nova.github.io (público)
**URL publicada:** https://andres-nova.github.io ✅ **ACTIVA**
**Git remoto:** HTTPS (no SSH) — `git -C /home/andres/Documentos/Codigo/Proyectos/portafolio push`

---

## Estado actual

- i18n bilingüe ES/EN completo ✅
- 6 proyectos configurados (4 visibles, 2 ocultos)
- GitHub Pages: **ACTIVO** ✅ — desplegado desde `main` / `(root)`
- og-preview.png generada (1200×630px) en `assets/` ✅
- Sección Certificaciones completa con CV verificado ✅
- About actualizado con métricas reales ✅
- Hero badge Apache Airflow añadido ✅
- Experience con fechas y títulos reales ✅
- Dashboard Riesgo Crediticio: demo LIVE + imagen preview ✅
- Siniestralidad Vial Bogotá: demo LIVE + imagen preview del mapa ✅

---

## Pendientes en orden de prioridad

1. **Subir CV real**
   ```bash
   cp /ruta/CV_Andres_Nova.pdf /home/andres/Documentos/Codigo/Proyectos/portafolio/assets/CV_Andres_Nova.pdf
   git -C /home/andres/Documentos/Codigo/Proyectos/portafolio add assets/CV_Andres_Nova.pdf
   git -C /home/andres/Documentos/Codigo/Proyectos/portafolio commit -m "feat: agregar CV Andres Nova"
   git -C /home/andres/Documentos/Codigo/Proyectos/portafolio push
   ```

2. **Hacer visibles proyectos ocultos** cuando estén listos:
   - `sentiment-nlp`: `visible: false` → `true`
   - `ollama-manager`: ídem

3. **Verificar nombre repo** `sentiment-nlp`: confirmar si GitHub lo tiene como `sentiment-nlp-co` o `sentimiento-nlp-co`

---

## Stack

- Single-file `index.html` — todo CSS en `<style>`, todo JS en `<script>` al final del body
- CDN: Google Fonts (Inter 400/500/600/700) + Font Awesome 6.5.0
- GitHub Pages desde `main` / root — username: `Andres-Nova`, repo: `Andres-Nova.github.io`
- Sin frameworks JS ni build step

---

## i18n bilingüe

- Toggle ES/EN en navbar, default español, persistencia `localStorage`
- `TRANSLATIONS = { es: {...}, en: {...} }` — 52+ claves cubriendo todo el sitio
- Atributos `data-i18n` en cada elemento traducible
- `setLanguage(lang)` actualiza DOM, placeholders, re-renderiza proyectos, reinicia typewriter

---

## Proyectos configurados (PROJECTS_CONFIG)

Orden en la grilla (de arriba a abajo, izquierda a derecha):

| pos | id | visible | featured | image | repo | demo |
|-----|-----|---------|----------|-------|------|------|
| 1 | banking-risk | ✅ | ⭐ Destacado | `assets/banking-risk-preview.jpg` | `Andres-Nova/credit-risk-colombia` | https://credit-risk-colombia.streamlit.app/ ✅ LIVE |
| 2 | urban-mobility | ✅ | — | `assets/bogota-traffic-preview.jpg` | `Andres-Nova/bogota-traffic-safety` | https://bogota-traffic-safety.streamlit.app/ ✅ LIVE |
| 3 | rag-system | ✅ | — | — | `Andres-Nova/academic-rag` (privado) | — |
| 4 | whatsapp-bot | ✅ | — | — | `Andres-Nova/whatsapp-llm-bot` | — |
| — | sentiment-nlp | ❌ oculto | — | — | `Andres-Nova/sentiment-nlp-co` (privado) | — |
| — | ollama-manager | ❌ oculto | — | — | `Andres-Nova/ollama-manager` | — |

### Imágenes preview
- `assets/banking-risk-preview.jpg` — screenshot del dashboard (KPIs 149k / 6.7% / AUC 0.86 / KS 0.57)
- `assets/bogota-traffic-preview.jpg` — mapa Bogotá 1200×660px con 20k puntos de siniestros
- Efecto hover zoom CSS en `.card-preview img { transform: scale(1.04) }`

---

## Convenciones

- Commits descriptivos en español
- Sin Co-Authored-By ni metadatos de IA
- `git -C /ruta/portafolio push` — el repo es independiente del repo padre de Codigo/
- Archivos excluidos: `.claude/`, `docs/superpowers/`, `PROMPT~1.MD`
