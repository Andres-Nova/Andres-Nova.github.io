// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://andres-nova.github.io',
  base: '/nexus-ops',
  outDir: '../nexus-ops',
  trailingSlash: 'always',
});
