"""Migrate Hugo markdown content to Astro content collections."""
import os
import re

hugo_uc_dir = os.path.expanduser('~/earnwithhermes/content/use-cases')
astro_uc_dir = os.path.expanduser('~/earnwithhermes-astro/src/content/useCases')
os.makedirs(astro_uc_dir, exist_ok=True)

CATEGORY_MAP = {
    'agency-ai-ops': 'Agency & Consulting',
    'chief-of-staff': 'Agency & Consulting',
    'client-work-automated': 'Agency & Consulting',
    'supabase-crm': 'Agency & Consulting',
    'weather-trading-bot': 'Trading & Markets',
    'polymarket-trading': 'Trading & Markets',
    'crosschain-trading': 'Trading & Markets',
    'token-cost-cut': 'Cost Savings',
    'mac-mini-agent': 'Cost Savings',
    'vps-vs-openclaw': 'Cost Savings',
    'hetzner-vps': 'Cost Savings',
    'smart-routing': 'Cost Savings',
    'tiktok-factory': 'Content Monetization',
    'marketing-studio': 'Content Monetization',
    'x-roast-poster': 'Content Monetization',
    'content-ops-pipeline': 'Content Monetization',
    'roofing-leadgen': 'Building Products',
    'printing-factory': 'Building Products',
}

META = {
    'agency-ai-ops': {'author': '@IBuzovskyi', 'storySource': 'X/Twitter', 'income': '$2,485/mo'},
    'chief-of-staff': {'author': '@ogiberstein', 'storySource': 'Discord'},
    'client-work-automated': {'author': '@NathanWilbanks_', 'storySource': 'X/Twitter', 'income': '$100K+'},
    'supabase-crm': {'author': 'Derek Cheung', 'storySource': 'YouTube'},
    'weather-trading-bot': {'author': '@DeRonin_', 'storySource': 'X/Twitter', 'income': '+116%'},
    'polymarket-trading': {'author': '@adiix_official', 'storySource': 'X/Twitter'},
    'crosschain-trading': {'author': 'Gideon Ng', 'storySource': 'Blog'},
    'token-cost-cut': {'author': 'Greg Isenberg', 'storySource': 'Podcast', 'income': '90% less'},
    'mac-mini-agent': {'author': '@witcheer', 'storySource': 'X/Twitter', 'income': '$21/mo'},
    'vps-vs-openclaw': {'author': 'Alex P.', 'storySource': 'Blog', 'income': '<$20/mo'},
    'hetzner-vps': {'author': 'Théo Vigneres', 'storySource': 'YouTube', 'income': '$10/mo'},
    'smart-routing': {'author': 'u/hackrepair', 'storySource': 'Reddit'},
    'tiktok-factory': {'author': '@cyrilXBT', 'storySource': 'X/Twitter'},
    'marketing-studio': {'author': '@codewithimanshu', 'storySource': 'X/Twitter'},
    'x-roast-poster': {'author': '@yodaaa', 'storySource': 'Discord'},
    'content-ops-pipeline': {'author': '@mvanhorn', 'storySource': 'X/Twitter'},
    'roofing-leadgen': {'author': '@cyberfarmacist', 'storySource': 'Discord'},
    'printing-factory': {'author': '@Xwm1234', 'storySource': 'GitHub'},
}

def adapt_uc(content: str, slug: str) -> str:
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        return content
    yaml_str, body = match.group(1), match.group(2)
    fields = {}
    for line in yaml_str.split('\n'):
        m = re.match(r'^(\w+):\s*(.*)', line)
        if m:
            fields[m.group(1).strip()] = m.group(2).strip()
    category = CATEGORY_MAP.get(slug, 'use-cases')
    meta = META.get(slug, {})
    new = '---\n'
    new += f'title: "{fields.get("title", slug)}"\n'
    new += f'date: {fields.get("date", "2026-01-01")}\n'
    new += 'draft: false\n'
    new += f'description: "{fields.get("description", "")}"\n'
    new += f'tags: {fields.get("tags", "[]")}\n'
    new += f'categories: ["{category}"]\n'
    if meta.get('author'): new += f'author: "{meta["author"]}"\n'
    if meta.get('storySource'): new += f'storySource: "{meta["storySource"]}"\n'
    if meta.get('income'): new += f'income: "{meta["income"]}"\n'
    new += '---\n' + body
    return new

count = 0
for fname in sorted(os.listdir(hugo_uc_dir)):
    if not fname.endswith('.md') or fname == '_index.md':
        continue
    slug = fname.replace('.md', '')
    with open(os.path.join(hugo_uc_dir, fname)) as f:
        adapted = adapt_uc(f.read(), slug)
    with open(os.path.join(astro_uc_dir, fname), 'w') as f:
        f.write(adapted)
    count += 1
    print(f'  ✓ {fname}')

# Migrate articles
hugo_art_dir = os.path.expanduser('~/earnwithhermes/content/articles')
astro_art_dir = os.path.expanduser('~/earnwithhermes-astro/src/content/articles')
os.makedirs(astro_art_dir, exist_ok=True)

for fname in sorted(os.listdir(hugo_art_dir)):
    if not fname.endswith('.md') or fname == '_index.md':
        continue
    with open(os.path.join(hugo_art_dir, fname)) as f:
        content = f.read()
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        yaml_str, body = match.group(1), match.group(2)
        fields = {}
        for line in yaml_str.split('\n'):
            m = re.match(r'^(\w+):\s*(.*)', line)
            if m:
                fields[m.group(1).strip()] = m.group(2).strip()
        new = '---\n'
        new += f'title: "{fields.get("title", fname)}"\n'
        new += f'date: {fields.get("date", "2026-01-01")}\n'
        new += 'draft: false\n'
        new += f'description: "{fields.get("description", "")}"\n'
        new += f'tags: {fields.get("tags", "[]")}\n'
        new += f'categories: {fields.get("categories", "[tutorials]")}\n'
        if 'canonicalURL' in fields:
            new += f'canonicalURL: {fields["canonicalURL"]}\n'
        new += '---\n' + body
        content = new
    with open(os.path.join(astro_art_dir, fname), 'w') as f:
        f.write(content)
    print(f'  ✓ articles/{fname}')

print(f'\nDone! Migrated {count} use cases + articles')
