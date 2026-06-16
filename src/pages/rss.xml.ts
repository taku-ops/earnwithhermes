import rss, { pagesGlobToRssItems } from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context: any) {
  const useCases = await getCollection('useCases', ({ data }) => !data.draft);
  const articles = await getCollection('articles', ({ data }) => !data.draft);

  const items = [
    ...useCases.map((uc) => ({
      title: uc.data.title,
      pubDate: uc.data.date,
      description: uc.data.description,
      link: `/use-cases/${uc.id}/`,
      categories: uc.data.tags || [],
    })),
    ...articles.map((a) => ({
      title: a.data.title,
      pubDate: a.data.date,
      description: a.data.description,
      link: `/learn/${a.id}/`,
      categories: a.data.tags || [],
    })),
  ];

  // Sort by date, newest first
  items.sort((a, b) => b.pubDate.getTime() - a.pubDate.getTime());

  return rss({
    title: 'Earn With Hermes',
    description: 'Blueprints, tutorials, and real stories of people generating autonomous income with Hermes Agent.',
    site: context.site || 'https://earnwithhermes.com',
    items: items.map((item) => ({
      title: item.title,
      pubDate: item.pubDate,
      description: item.description,
      link: item.link,
      categories: item.categories,
    })),
    customData: `<language>en-us</language>`,
    stylesheet: false,
  });
}
