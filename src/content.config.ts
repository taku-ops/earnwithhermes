import { defineCollection, z } from 'astro:content'
import { glob } from 'astro/loaders'

const useCases = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: './src/content/useCases' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
    description: z.string(),
    tags: z.array(z.string()).default([]),
    categories: z.array(z.string()).default([]),
    storySource: z.string().optional(),
    author: z.string().optional(),
    income: z.string().optional(),
    roi: z.string().optional(),
  }),
})

const articles = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: './src/content/articles' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
    description: z.string(),
    tags: z.array(z.string()).default([]),
    categories: z.array(z.string()).default([]),
    canonicalURL: z.string().optional(),
  }),
})

export const collections = { useCases, articles }
