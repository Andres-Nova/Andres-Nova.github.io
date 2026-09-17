# nexus-ops-src

Fuente Astro del sitio Nexus Ops (landing + blog). El build de este proyecto genera el
sitio estático que se sirve en `https://andres-nova.github.io/nexus-ops/`.

## Instalar

```sh
npm install
```

## Desarrollo

```sh
npm run dev
```

Levanta el servidor de desarrollo de Astro en `http://localhost:4321/nexus-ops/`
(respeta el `base: '/nexus-ops'` de `astro.config.mjs`).

## Build

```sh
npm run build
```

Compila el sitio y lo escribe en `../nexus-ops/` (un directorio HERMANO de este, fuera
de `nexus-ops-src/`), que es la carpeta que realmente se commitea y se publica en
GitHub Pages. `outDir: '../nexus-ops'` en `astro.config.mjs` hace este redireccionamiento.

El script `postbuild` borra automáticamente `../nexus-ops/astro/` (un `content.d.ts` que
Astro regenera en cada build y que no forma parte del sitio servible).

Después de un build, revisá con `git status --short ../nexus-ops` que no queden archivos
inesperados, y commiteá el resultado junto con los cambios de `src/`:

```sh
git add nexus-ops-src/ nexus-ops/
git commit -m "..."
```

## Previsualizar el build respetando el base path

`astro preview` NO respeta el `base` de la misma forma que GitHub Pages, así que para
verificar el sitio tal cual queda publicado hay que servir la carpeta PADRE (la que
contiene tanto `nexus-ops-src/` como `nexus-ops/`) y visitar `/nexus-ops/`:

```sh
cd ..              # la carpeta que contiene nexus-ops-src/ y nexus-ops/
npx serve . -l 5098
```

Y abrir `http://localhost:5098/nexus-ops/`, `http://localhost:5098/nexus-ops/blog/`, etc.

## Estructura

```
src/
├── layouts/       BaseLayout (landing + blog) y BlogLayout (post individual)
├── components/    secciones de la landing (Nav, Hero, Servicios, Calculadora...)
├── content/blog/  posts en Markdown (content collection tipada, ver content/config.ts)
└── pages/         index.astro (landing), blog/index.astro, blog/[...slug].astro
```

## Reproducibilidad del build

Un clon limpio de este repo + `npm ci` + `npm run build` debe producir exactamente lo
que está commiteado en `../nexus-ops/` (`git status` limpio sobre esa carpeta). Si algún
día un build deja algo distinto, es una regresión a corregir antes de commitear el
resultado.
