# AGENTS.md

Static landing page for [earnwithhermes.com](https://earnwithhermes.com) — a simple promotional site for "AI Agents That Make Money."

## Quick start

```bash
git clone https://github.com/taku-ops/earnwithhermes.git
cd earnwithhermes-landing
```

No build step needed. Just open `index.html` in a browser, or serve it:

```bash
python3 -m http.server 8000
```

Or deploy to any static host (Netlify, Vercel, GitHub Pages, etc.).

## Project structure

```
earnwithhermes-landing/
├── index.html     # Single-page landing (inline CSS, no JS framework)
└── CNAME          # Custom domain: earnwithhermes.com
```

## Deployment

The site is a single static HTML file with inline styles. Deploy by pushing to the `main` branch — points to `earnwithhermes.com` via CNAME.

## Conventions

- Single HTML file, no framework, no build step
- Inline CSS, no external stylesheets
- No JavaScript

## Dependencies

None. Just a browser.
