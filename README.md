# Where to Build Next

A curated portfolio showcase of 28 high-growth startups across AI/ML, energy infrastructure, developer tools, security, and fintech. Built to connect talented people with exceptional companies through a searchable, filterable directory with detailed company profiles and direct career links.

## What This Is

**Where to Build Next** is a single-page web application that serves as a talent-facing portfolio directory. Each company listing includes:

- Company overview and one-liner description
- Funding stage and valuation
- Capital raised and investor details
- Founder backgrounds and leadership
- Product deep-dives and investment thesis
- Direct links to open roles and career pages
- One-click interest submission via Airtable

## Featured Categories

| Category | Companies | Examples |
|----------|-----------|----------|
| AI / ML & Models | 11 | Mercor, Skild AI, Poolside, LMArena |
| Developer Tools | 7 | Supabase, n8n, Runway AI, Chalk AI |
| Energy & Infrastructure | 4 | Crusoe, Radiant Nuclear, Exowatt |
| Security & Defense | 5 | Semgrep, Vannevar Labs, Corridor |
| Fintech & Other | 1 | Sphere |

## Features

- **Search** &mdash; Full-text search across company names, descriptions, and founder info
- **Category Filters** &mdash; Filter by sector (AI/ML, Energy, Dev Tools, Security, Fintech)
- **Live Stats** &mdash; Real-time counts of matching companies, hiring status, and stage breakdown
- **Company Detail Pages** &mdash; Expandable profiles with founder bios, product details, financials, and thesis
- **Career Links** &mdash; Direct links to each company's job board (Ashby, Greenhouse, etc.)
- **Interest Forms** &mdash; Pre-filled Airtable forms to express interest in specific companies

## Tech Stack

- **React 18.2** and **ReactDOM** via CDN
- **Babel Standalone 7.23** for runtime JSX transpilation
- **Google Fonts** (DM Sans + Fraunces)
- **CSS Custom Properties** for dark-theme design system
- **Airtable** for interest form submissions

No build tools, no bundler, no package manager. The entire application is a single self-contained `index.html` file.

## Getting Started

No setup required. Just open the file in your browser:

```bash
open index.html
```

### Deploy

This is a static site with no build step. Deploy `index.html` to any static hosting provider:

- **GitHub Pages** &mdash; Push to a `gh-pages` branch or enable Pages on `main`
- **Vercel** &mdash; `vercel` from the project root
- **Netlify** &mdash; Drag and drop `index.html` in the Netlify dashboard
- **Cloudflare Pages** &mdash; Connect the repo, no build command needed

## Project Structure

```
where-to-build-next/
├── README.md        # This file
└── index.html       # Entire application (~620 lines)
```

The `index.html` file contains:

| Section | Description |
|---------|-------------|
| CDN imports | React, ReactDOM, Babel, Google Fonts |
| `COMPANIES` array | All 28 company data objects |
| CSS styles | Full dark-theme design system with animations |
| React components | `CompanyCard`, `CompanyDetail`, `App` |
| Render call | `ReactDOM.createRoot` entry point |

## Design

Dark theme with a purple accent palette:

- **Background**: Near-black (`#06060b`)
- **Cards**: Dark surface (`#0c0c14`) with subtle borders
- **Accent**: Indigo/purple (`#818cf8`, `#a78bfa`)
- **Typography**: DM Sans for UI, Fraunces for display headings
- **Animations**: Fade-up entrance animations and hover glow effects

## Adding or Updating Companies

Edit the `COMPANIES` array in `index.html`. Each company object follows this structure:

```javascript
{
  id: 29,
  name: "Company Name",
  color: "#hex",
  emoji: "🚀",
  oneliner: "What the company does in one sentence.",
  stage: "Series A",
  valuation: "$500M",
  raised: "$50M",
  location: "San Francisco, CA",
  careers: "https://jobs.company.com",
  founders: "Founder background and experience.",
  product: "Detailed product description.",
  thesis: "Why this company matters.",
  numbers: "Key metrics, investors, and financials.",
  category: "ai"  // ai | energy | devtools | security | fintech
}
```

## License

All rights reserved.
