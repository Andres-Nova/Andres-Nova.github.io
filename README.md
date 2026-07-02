# Andres Nova — Portfolio Personal

Sitio de portafolio personal construido en HTML/CSS/JS vanilla, listo para GitHub Pages.

## Despliegue en GitHub Pages

1. Crear un repositorio en GitHub con el nombre `Underwork1.github.io`
2. Subir los archivos: `index.html` + carpeta `assets/`
3. Ir a **Settings → Pages → Source: Deploy from a branch → main → / (root)**
4. En 1-2 minutos el sitio estará en: **https://Underwork1.github.io**

## Reemplazar el CV

Renombrar tu CV a `CV_Andres_Nova.pdf` y subirlo a la carpeta `assets/`.

## Agregar o quitar proyectos

Abrir `index.html` y buscar `PROJECTS_CONFIG` al inicio del bloque `<script>`.
Cambiar `visible: false` a `visible: true` (o viceversa) en cualquier proyecto.

## Personalización rápida

- **Colores:** buscar `:root` en el `<style>` — todas las variables de color están ahí.
- **Textos:** buscar la sección correspondiente en el HTML.
- **Proyectos nuevos:** agregar un objeto al array `PROJECTS_CONFIG` siguiendo la misma estructura.

## Placeholders pendientes

Buscar `REEMPLAZAR` en el código para encontrar todos los valores a completar:

| Placeholder | Descripción |
|---|---|
| URL Streamlit urban-mobility | URL de tu app desplegada en Streamlit |
| URL repo RAG | Nombre del repo RAG en GitHub |
| og:image | Subir una imagen preview a assets/og-preview.png |
