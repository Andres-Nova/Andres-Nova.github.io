// nexus-ops-src/src/content/config.ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    badge: z.string(),
    readingTime: z.string(),
    keywords: z.string().optional(),
  }),
});

export const collections = { blog };
