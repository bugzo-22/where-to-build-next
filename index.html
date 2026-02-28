<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Felicis Portfolio — Where to Build Next</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>✦</text></svg>">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,500;0,9..144,700;1,9..144,400&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  :root{--bg:#06060b;--card:#0c0c14;--card-hover:#10101c;--border:#1a1a2e;--text:#e2e8f0;--text-muted:#64748b;--text-dim:#475569;--accent:#818cf8;--accent2:#a78bfa;--green:#34d399;--surface:#111118}
  body{background:var(--bg);color:var(--text);font-family:'DM Sans',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
  #root{min-height:100vh}
  @keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
  @keyframes fadeIn{from{opacity:0}to{opacity:1}}
  .fade-up{animation:fadeUp .5s ease both}
  .fade-in{animation:fadeIn .4s ease both}
</style>
</head>
<body>
<div id="root"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.9/babel.min.js"></script>
<script type="text/babel">
const { useState, useCallback, useEffect, useRef } = React;

const COMPANIES = [
  {
    id: "ricursive", name: "Ricursive Intelligence", color: "#00C9A7", emoji: "🔄",
    oneliner: "AI-designed semiconductors — compressing chip design from years to weeks",
    fund: "FV 10", stage: "Series A", valuation: "$4B", raised: "$335M",
    location: "San Francisco",
    careers: "https://jobs.ashbyhq.com/Ricursive%20Intelligence/",
    founders: "Dr. Anna Goldie (CEO) & Dr. Azalia Mirhoseini (CTO) — co-created AlphaChip at Google Brain/DeepMind, deployed across 4 generations of TPUs. Previously worked on Claude (Anthropic) and Gemini (DeepMind). Co-created Mixture-of-Experts (MoE) architectures used in ChatGPT and Gemini. Azalia also directs Stanford's Scaling Intelligence Lab.",
    product: "Full-stack AI platform for semiconductor design. Compresses chip design cycles from 2-3 years. Their AI generates 'alien' designs — curved, donut-shaped placements humans would never attempt — that outperform human layouts on wire length, power, and timing.",
    thesis: "Chips are the fuel for AI scaling laws. Faster chip design → better compute → better AI → even faster chip design. They're enabling a shift from 'fabless' to 'designless' — any company can create custom silicon without massive in-house design teams.",
    numbers: "$335M total. $35M seed (Sequoia), $300M Series A (Lightspeed) at $4B valuation — 2 months apart. Investors: DST Global, NVentures (NVIDIA), Felicis. Fewer than 10 employees at Series A.",
    category: "ai"
  },
  {
    id: "periodic", name: "Periodic Labs", color: "#4ADE80", emoji: "⚗️",
    oneliner: "AI scientists paired with autonomous labs — discovering new materials at superhuman speed",
    fund: "FV 9", stage: "Seed", valuation: "$1.5B", raised: "$300M",
    location: "San Francisco",
    careers: "https://jobs.ashbyhq.com/periodic-labs",
    founders: "Liam Fedus: Ex-VP of Research at OpenAI. Created ChatGPT, led post-training team. Published first trillion-parameter neural network paper. Ekin Dogus Cubuk: Ex-Head of Chemistry & Materials at DeepMind. Led GNoME paper discovering 2.2M new crystal structures (Nature).",
    product: "AI scientists paired with autonomous physical laboratories. AI agents propose hypotheses, robots run experiments, AI analyzes results, then iterates. Each experiment generates proprietary data (including failures) competitors can't access. Initial focus: superconductors, semiconductor thermal issues.",
    thesis: "AI has exhausted internet data. The next frontier is generating NEW knowledge through physical experimentation. 'Intelligence is necessary but not sufficient. New knowledge is created when ideas are found to be consistent with reality.' The next great dataset comes from the lab bench, not the web.",
    numbers: "$300M seed — possibly the largest seed in startup history. Led by a16z, with NVIDIA, Accel, Felicis. $1.5B pre-money. Angels: Jeff Bezos, Eric Schmidt, Jeff Dean.",
    category: "ai"
  },
  {
    id: "datology", name: "DatologyAI", color: "#A78BFA", emoji: "🧬",
    oneliner: "Automated data curation for AI training — because models are what they eat",
    fund: "FV 9", stage: "Series A", valuation: "", raised: "$57.6M",
    location: "San Francisco",
    careers: "https://jobs.ashbyhq.com/DatologyAI",
    founders: "Ari Morcos (CEO): PhD neuroscience Harvard, 2 years DeepMind, 5 years Meta FAIR as Senior Staff Scientist. Matthew Leavitt (CSO): Ex-MosaicML and MetaAI, PhD neuroscience McGill. Bogdan Gaza (CTO): 10+ years infrastructure at Amazon and Twitter.",
    product: "Automated data curation at petabyte scale. Identifies the most valuable training data, removes redundant/harmful points, suggests augmentation strategies, and optimizes training batches. Modality-agnostic — works on text, images, and more. Replaces months of manual data engineering.",
    thesis: "Even the best architectures underperform on bad data. Angel investors include Jeff Dean, Yann LeCun, and Geoffrey Hinton — the holy trinity of deep learning backing a data curation company. Named WEF Technology Pioneer.",
    numbers: "$57.6M total. $11.65M seed (Amplify Partners). $46M Series A led by Felicis, with M12 (Microsoft), Amazon Alexa Fund. Founded September 2023.",
    category: "ai"
  },
  {
    id: "simular", name: "Simular", color: "#60A5FA", emoji: "🖥️",
    oneliner: "Desktop AI agents that physically control any computer — not just the browser",
    fund: "FV 10", stage: "Series A", valuation: "", raised: "$27M",
    location: "San Francisco",
    careers: "https://jobs.ashbyhq.com/simular",
    founders: "Ang Li (CEO): Ex-Google DeepMind continuous learning scientist. PhD University of Maryland. Previously at Baidu Apollo, Facebook AI. Jiachen Yang: Ex-DeepMind reinforcement learning specialist. PhD Georgia Tech. Met at DeepMind working on Google products including Waymo.",
    product: "Controls the ENTIRE desktop — not just the browser. Physically moves the mouse, clicks buttons, and types across any application. 'Neuro-symbolic' approach + proprietary Simulang abstraction layer converts successful AI workflows into deterministic code, solving the hallucination problem.",
    thesis: "Targets 'API-deficient industries' — insurance, healthcare, finance — where repetitive computer work can't be automated because there are no APIs. Selected for Microsoft's Windows 365 for Agents program. Agent S framework: 69.9% on OSWorld benchmark (human: 72%).",
    numbers: "$27M total. $21.5M Series A led by Felicis, $5M seed. NVIDIA doubled down from seed. Early customers: car dealerships, HOAs, insurance.",
    category: "ai"
  },
  {
    id: "skild", name: "Skild AI", color: "#F472B6", emoji: "🤖",
    oneliner: "One universal brain for all robots — foundation models for the physical world",
    fund: "FV 9", stage: "Series C", valuation: "$14B+", raised: "$1.81B",
    location: "Pittsburgh",
    careers: "https://job-boards.greenhouse.io/skildai-careers/",
    founders: "Deepak Pathak (CEO): IIT Kanpur gold medalist, PhD UC Berkeley, CMU Robotics professor. Pioneer of 'curiosity-driven learning' (4K+ citations). Abhinav Gupta (President): CMU Robotics professor since 2009, founding member of Meta FAIR. 75K+ citations.",
    product: "A universal foundation model for robotics — one 'brain' that controls any robot for any task. Unlike vertical robots, Skild Brain works across quadrupeds, humanoids, robotic arms, and mobile manipulators. Trained on massive human video data and physics simulations.",
    thesis: "By 2030, global talent shortage could reach 85.2M people costing $8.5T. Skild's universal brain could bring robots to every industry. Building the 'Excel of robotics' — one platform for all robotic hardware.",
    numbers: "$1.81B across 4 rounds. $1.4B Series C (Jan 2026) at $14B+ led by SoftBank. Investors: NVIDIA, Samsung, LG, Sequoia, Felicis. ~34 employees. Pittsburgh-based.",
    category: "ai"
  },
  {
    id: "poolside", name: "Poolside", color: "#38BDF8", emoji: "🏊",
    oneliner: "AI code generation through reinforcement learning — models that learn by coding themselves",
    fund: "FV 9", stage: "Series B", valuation: "$3B", raised: "$626M+",
    location: "Paris",
    careers: "https://jobs.ashbyhq.com/poolside",
    founders: "Jason Warner (CEO): Former CTO of GitHub, incubated Copilot and Code Search. Previously led engineering at Heroku and Canonical. Eiso Kant (CTO): Founded source{d} — the world's first company applying AI to source code.",
    product: "RLCEF (Reinforcement Learning from Code Execution Feedback): Models learn by coding across 500K+ codebases, not just reading code. They explore solutions, learn from successes and failures. No data or code ever leaves the customer's security boundary.",
    thesis: "Software development will be the first capability where AI surpasses human intelligence. Vision: turn millions of developers into billions. Projects that took 10 engineers six months done in hours of compute.",
    numbers: "$626M+ total. $126M seed led by Felicis. $500M Series B led by Bain Capital at $3B. AWS partnership (Bedrock). 10,000 NVIDIA GPUs. 80% team Europe-based. ~62 employees.",
    category: "ai"
  },
  {
    id: "lmarena", name: "LMArena", color: "#FBBF24", emoji: "⚔️",
    oneliner: "The definitive AI leaderboard — where OpenAI, Google, and Anthropic secretly test models",
    fund: "FV 9", stage: "Series A", valuation: "$1.7B", raised: "$250M",
    location: "Berkeley",
    careers: "https://jobs.ashbyhq.com/lmarena",
    founders: "Anastasios Angelopoulos (CEO): UC Berkeley researcher, statistician. Wei-Lin Chiang (CTO): UC Berkeley researcher. Ion Stoica: Berkeley CS professor, co-founder of Databricks, faculty advisor. Core team from Berkeley, Stanford, UCSD, CMU.",
    product: "Users submit a prompt → two anonymous AI models respond → users vote. Aggregated across millions of votes using Elo ratings — live leaderboards across text, code, image, video, and search. 5M+ monthly active users across 150 countries.",
    thesis: "OpenAI, Google, Anthropic, xAI all test models here secretly before launch. DeepSeek tested R1 months before debut. OpenAI tested GPT-5 as 'summit'. Once it's the de-facto benchmark layer, the product naturally expands.",
    numbers: "$250M total. $100M seed at $600M. $150M Series A at $1.7B — unicorn in 7 months. ARR exceeded $30M within 4 months of commercial launch. 400+ models evaluated.",
    category: "ai"
  },
  {
    id: "standard_kernel", name: "Standard Kernel", color: "#D946EF", emoji: "🧠",
    oneliner: "AI that writes GPU kernels beating NVIDIA's own libraries — unlocking the AI hardware bottleneck",
    fund: "FV 9", stage: "Seed", valuation: "", raised: "Undisclosed",
    location: "Mountain View",
    careers: "https://docs.google.com/forms/d/e/1FAIpQLSc7_F7F6LLh_yX7k2_v874P72t4KXgqX6Mda5fOQyLFOTa8Kg/viewform",
    founders: "Anne Ouyang (CEO): Ex-NVIDIA premier kernel team. Author of KernelBench, the first benchmark for AI kernel generation. PhD student in Stanford's Scaling Intelligence Lab. Christopher Rinard: Ex-MosaicML, Stanford CS PhD. They met as TAs for MIT's Performance Engineering course.",
    product: "AI platform that auto-generates optimized GPU kernels. Works in pure CUDA C and PTX assembly (not Triton). H100 BF16 matmul at 102-105% of cuBLAS. H100 BF16 attention at 104% of FlashAttention3. 20% speedup on Llama 3 FFN through auto-discovered fusion.",
    thesis: "Kernel engineers command seven-figure salaries. Kernels unlock gains across the ENTIRE AI stack: models, deployment, cloud costs, hardware adoption. General Catalyst: 'a foundational key to unlock the future of AI infrastructure.'",
    numbers: "Raised from General Catalyst (lead) and Felicis. Founded April 2025. KernelBench benchmark and 'Surprisingly Fast AI-Generated Kernels' paper.",
    category: "ai"
  },
  {
    id: "mercor", name: "Mercor", color: "#F59E0B", emoji: "🎯",
    oneliner: "AI-powered expert matching for AI training — the youngest self-made billionaire founders in history",
    fund: "FV 9", stage: "Series C", valuation: "$10B", raised: "$482M+",
    location: "San Francisco",
    careers: "https://jobs.ashbyhq.com/mercor",
    founders: "Brendan Foody (CEO), Adarsh Hiremath (CTO), Surya Midha (COO) — three Bay Area high school friends (Bellarmine debate team), all dropped out of college (Harvard, Georgetown) to build Mercor. Thiel Fellows. Became the youngest self-made billionaires at age 22.",
    product: "AI-driven platform connecting domain experts (scientists, doctors, lawyers, engineers) with AI labs for model training. AI interviews and evaluates 468K+ applicants, matching them with specialized training opportunities. Manages 30K+ contractors paid $1.5M+ per day collectively.",
    thesis: "After Meta's $14.3B stake in Scale AI caused major labs (OpenAI, Google) to cut ties, Mercor captured enormous demand. On track to hit $500M ARR faster than Anysphere (Cursor). 'If AI automates 90% of the economy, humans become the bottleneck for the remaining 10% — that's 10x leverage.'",
    numbers: "$350M Series C led by Felicis at $10B (5x in 8 months). Prior: $100M Series B at $2B, $32M Series A. Investors: Benchmark, General Catalyst, Robinhood Ventures. Angels: Peter Thiel, Jack Dorsey, Adam D'Angelo. $75M+ ARR and profitable.",
    category: "ai"
  },
  {
    id: "motherduck", name: "MotherDuck", color: "#FBBF24", emoji: "🦆",
    oneliner: "Serverless cloud analytics built on DuckDB — making 'Big Data' dead for 95% of workloads",
    fund: "FV 9", stage: "Series B", valuation: "$400M", raised: "$100M",
    location: "Seattle",
    careers: "https://jobs.ashbyhq.com/MotherDuck",
    founders: "Jordan Tigani (CEO): Founding engineer at Google BigQuery. Previously CPO at SingleStore. Coined 'Big Data is Dead' — the thesis that modern laptops are faster than cloud data warehouses for most workloads. Co-founders include Ryan Boyd (ex-Google DevRel) and Tino Tereshko (VP of Produck 🦆).",
    product: "Serverless cloud analytics platform built on DuckDB, the open-source embedded database. Hybrid engine combines local (laptop) and cloud execution — queries start in 30ms. Users store, share, and query data with the speed of local computing and the collaboration of the cloud. No distributed systems overhead for the 95% of workloads that aren't petabyte-scale.",
    thesis: "DuckDB is the fastest-growing database in the world (40% monthly DB-Engines growth). MotherDuck has an exclusive partnership with DuckDB Labs to build the commercial cloud layer. The 'scale-up' approach beats traditional distributed warehouses on cost and speed for most real-world data sizes. Team recruited from Snowflake, Databricks, AWS, Meta, Elastic.",
    numbers: "$100M total. $52.5M Series B led by Felicis at $400M valuation. Prior: $35M Series A (a16z), $12.5M seed (Redpoint). Investors: Altimeter, Madrona, Amplify, Zero Prime. Viviana Faga (Felicis GP) on board. 2,000+ users at launch, growing fast.",
    category: "devtools"
  },
  {
    id: "deepjudge", name: "DeepJudge", color: "#6366F1", emoji: "⚖️",
    oneliner: "AI-powered legal search that turns law firms' hidden knowledge into competitive advantage",
    fund: "FV 9", stage: "Series A", valuation: "$300M", raised: "$51.9M",
    location: "Zurich, Switzerland",
    careers: "https://jobs.ashbyhq.com/deepjudge",
    founders: "Paulina Grnarova (CEO), Kevin Roth, and Yannic Kilcher — all ex-Google researchers with PhDs in AI from ETH Zurich. Leadership team includes senior alumni from Thomson Reuters, Casetext, and Kira Systems. Deeply technical founders who built a proprietary retrieval engine purpose-built for law.",
    product: "Enterprise search platform that connects a firm's document management, email, intranet, and client portals to retrieval-augmented AI agents. Custom neural networks deliver precise, context-aware search without moving sensitive data outside secure boundaries. Turns millions of precedents into actionable insight in real time. 80-90% active usage across customers.",
    thesis: "Generic RAG engines collapse on messy, permission-walled legal data. DeepJudge built secure precision retrieval purpose-built for law. Named #1 Legal AI tool globally by SKILLS.law. Recognized as likely category leader within 1-3 years by Legal Technology Hub. Freshfields (global elite firm) selected DeepJudge as core AI strategy.",
    numbers: "$51.9M total. $41.2M Series A led by Felicis at $300M valuation, with Coatue. Prior: $10.7M seed (Coatue). 500%+ YoY revenue growth. Customers: Freshfields, Holland & Knight, Cozen O'Connor, ArentFox Schiff, Gunderson Dettmer. 3rd in Top 100 Swiss Startups. Expanding US and UK.",
    category: "ai"
  },
  {
    id: "crusoe", name: "Crusoe", color: "#F59E0B", emoji: "⚡",
    oneliner: "Turning stranded energy into AI compute — building one of the world's largest AI data center campuses",
    fund: "FV 9", stage: "Late", valuation: "$10B", raised: "$2.64B",
    location: "Denver / Abilene, TX",
    careers: "https://jobs.ashbyhq.com/Crusoe",
    founders: "Chase Lochmiller (CEO): MIT math/physics, Stanford CS/AI, ex-Jump Trading. Summited Everest in 2018 and saw gas flares from oil fields lighting up the night. Cully Cavness (President/COO): Oil & gas family background. They pair tech + energy DNA.",
    product: "Vertically integrated AI infrastructure: find stranded/renewable energy → build hyperscale data centers → offer Crusoe Cloud (GPU IaaS). Digital Flare Mitigation turns waste gas into electricity for AI. In-house modular data center manufacturing.",
    thesis: "Building the Stargate campus in Abilene, TX: 1.2 gigawatts — one of the world's most powerful AI factories. Part of the $500B Stargate initiative with OpenAI/Oracle/SoftBank. 45GW pipeline across North America and Europe.",
    numbers: "$2.64B raised across 13 rounds at $10B valuation. Investors: Founders Fund, NVIDIA, Fidelity, Mubadala, Bain Capital. ~$276M revenue 2024, projecting near $1B for 2025.",
    category: "energy"
  },
  {
    id: "radiant", name: "Radiant Nuclear", color: "#FB923C", emoji: "☢️",
    oneliner: "Portable nuclear microreactors deployable anywhere AI needs power",
    fund: "FV 8", stage: "Growth", valuation: "", raised: "$300M+",
    location: "Los Angeles",
    careers: "https://job-boards.greenhouse.io/radiant",
    founders: "Doug Bernauer (CEO): Aerospace and defense engineering background. Vision: nuclear energy should be deployable like industrial equipment — manufactured in a factory, shipped to site, operational quickly.",
    product: "The Kaleidos portable microreactor. Factory-manufactured and transportable. Powers remote military bases, data centers, mining operations, disaster relief. First reactor (Kaleidos Demonstration Unit) on track at Idaho National Lab's DOME facility.",
    thesis: "AI's power demands grow exponentially. Data centers need 24/7 clean baseload that renewables alone can't provide. Radiant deploys directly at data center sites. Deal for 20 Kaleidos with Equinix (major data center operator) plus US Air Force contract.",
    numbers: "$300M+ raised. Investors: Founders Fund, Draper Associates, ARK Venture Fund, Chevron Technology Ventures. US Air Force/DIU contract. Equinix deal for 20 microreactors. Targeting first reactor 2028.",
    category: "energy"
  },
  {
    id: "exowatt", name: "Exowatt", color: "#F97316", emoji: "☀️",
    oneliner: "Solar thermal + long-duration storage — 24/7 clean energy purpose-built for data centers",
    fund: "FV 9", stage: "Early", valuation: "", raised: "Undisclosed",
    location: "Miami",
    careers: "https://jobs.lever.co/exowatt",
    founders: "Energy and deep-tech entrepreneurs combining solar thermal engineering, energy storage, and data center infrastructure expertise. Based in Miami, FL.",
    product: "Modular clean energy using concentrated solar thermal paired with proprietary thermal storage. Unlike solar panels (only work when sun shines), thermal storage enables 24/7 power delivery — critical for data centers that can't tolerate intermittency.",
    thesis: "Every major AI company is desperate for power. Grid connections take years. Exowatt deploys faster and cheaper than traditional power infrastructure. Data center power market could reach hundreds of billions.",
    numbers: "Backed by Andreessen Horowitz and Sam Altman. Felicis investor. Targeting the massive data center power market.",
    category: "energy"
  },
  {
    id: "armada", name: "Armada", color: "#0EA5E9", emoji: "🛰️",
    oneliner: "Satellite-connected edge computing for oil rigs, military bases, and disaster zones",
    fund: "FV 9", stage: "Growth", valuation: "", raised: "$200M+",
    location: "Palo Alto",
    careers: "https://job-boards.greenhouse.io/armada/",
    founders: "Dan Wright (CEO) and Jon Runyan (COO), with Pradeep Nair (founding CTO). Board includes Trae Stephens (Founders Fund, Anduril co-founder).",
    product: "Ruggedized, satellite-connected modular data centers: Beacon (briefcase-sized), Cruiser (20' container), Triton (40' container), Leviathan (two 45' containers). All with Armada Edge Platform + Starlink connectivity. Deployed in 43 countries.",
    thesis: "75% of enterprise data originates at the edge with virtually zero processing. Dual-use: equally suited for oil rigs or military frontlines. US Navy testing for autonomous drone data processing. Microsoft partnership for Azure Marketplace.",
    numbers: "$200M+ raised. Investors: Founders Fund, Lux Capital, M12 (Microsoft), Shield Capital, Felicis. Partners: Starlink, Microsoft, Halliburton, Skydio. 43 countries. ~60 employees.",
    category: "energy"
  },
  {
    id: "entire", name: "Entire", color: "#14B8A6", emoji: "🌐",
    oneliner: "The developer platform for the AI agent era — from the man who built GitHub",
    fund: "FV 10", stage: "Seed", valuation: "$300M", raised: "$60M",
    location: "Seattle",
    careers: null,
    founders: "Thomas Dohmke (CEO): Former CEO of GitHub for 4 years (2021-2025). Oversaw Copilot's rise to 20M+ users. Previously founded HockeyApp (acquired by Microsoft 2015). Left GitHub on great terms with Satya Nadella to build the next defining developer platform.",
    product: "Three-layer open-source platform: 1) Git-compatible database for AI-produced code. 2) Universal semantic reasoning layer for multi-agent collaboration. 3) AI-native UI for agent-to-human review. First product Checkpoints: CLI that auto-captures prompts, reasoning, and decisions behind every agent's code. Works with Claude Code, Gemini CLI, Codex.",
    thesis: "'Soon developers won't look at code anymore — agents will write way more than humans can review.' Entire isn't training models — it's the management layer tracking what agents did and why. Open-source, agent-agnostic. The largest-ever seed round for a dev tool startup.",
    numbers: "$60M seed at $300M valuation led by Felicis. Investors: Madrona, M12 (Microsoft VC), Basis Set. Angels: Jerry Yang, Garry Tan (YC CEO), Olivier Pomel (Datadog CEO), Gergely Orosz. Launched Feb 2026.",
    category: "devtools"
  },
  {
    id: "n8n", name: "n8n", color: "#EF4444", emoji: "🔗",
    oneliner: "AI-powered workflow automation — 145K GitHub stars, the 'Excel of AI'",
    fund: "FV 7", stage: "Series C", valuation: "$2.5B", raised: "$240M",
    location: "Berlin",
    careers: "https://jobs.ashbyhq.com/n8n",
    founders: "Jan Oberhauser: Solo founder. Former VFX artist who worked on Maleficent and other films. Self-taught programmer. Built n8n from scratch in Berlin 2019. His creative background shaped the visual node-based approach.",
    product: "AI-powered workflow automation with visual node-based editor. 'Connect everything to anything' — 500+ integrations, any LLM, MCP protocol. Self-hosted or cloud. 'Fair-code' licensing. 75-80% of customer workflows now use AI.",
    thesis: "145K+ GitHub stars (Top 50 globally). 700K+ active developers. AI pivot was perfectly timed — they had automation infrastructure already built; AI orchestration was the natural evolution. Customers: Volkswagen, Vodafone, Delivery Hero, KPMG, Twitch, United Nations.",
    numbers: "$240M total. $180M Series C led by Accel at $2.5B (7x jump in 7 months). Investors: NVentures (NVIDIA), Sequoia, Felicis, Highland Europe. ARR above $40M with 10x YoY usage growth.",
    category: "devtools"
  },
  {
    id: "chalk", name: "Chalk AI", color: "#818CF8", emoji: "📐",
    oneliner: "Real-time data platform for AI inference — 5ms latency at 100K+ queries per second",
    fund: "FV 9", stage: "Series A", valuation: "$500M", raised: "$60M",
    location: "San Francisco",
    careers: "https://job-boards.greenhouse.io/chalkinc/",
    founders: "Marc Freed-Finnegan (CEO): Launched Google Wallet, founded Index (acquired by Stripe → became Stripe Terminal). Elliot Marx: Built ML infrastructure at Affirm, co-founded Haven Money (acquired by Credit Karma). Andrew Moreland: Ex-Palantir. All met at Stanford.",
    product: "Real-time data platform for AI inference. Teams declare features in Python → Chalk compiles them into parallel Rust pipelines delivering data in <5ms at 100K+ QPS. Same code for training and serving, eliminating skew. 'The Databricks of the AI era.'",
    thesis: "Every AI model needs fresh data at inference — fraud detection, identity verification, lending decisions, content moderation. Chalk fills this critical gap. Customers: MoneyLion, Socure, Doppel, Ramp, Melio.",
    numbers: "$60M total. $50M Series A led by Felicis at $500M valuation. Aydin Senkut on board. ~30 employees. Named Challenger in Gartner AI development platforms analysis.",
    category: "devtools"
  },
  {
    id: "supabase", name: "Supabase", color: "#3ECF8E", emoji: "🗄️",
    oneliner: "The open-source Firebase alternative — 2M+ developers, 65K+ GitHub stars",
    fund: "Focus", stage: "Series C", valuation: "", raised: "$116M+",
    location: "Singapore (remote)",
    careers: "https://jobs.ashbyhq.com/supabase/",
    founders: "Paul Copplestone (CEO): Australian developer/entrepreneur with strong open-source conviction. Ant Wilson (CTO): Deep database and infrastructure expertise. Fully remote team based in Singapore.",
    product: "Open-source Firebase alternative built on PostgreSQL. Database, authentication, instant APIs, edge functions, real-time subscriptions, storage, and vector embeddings for AI. Build full-stack apps in hours. No vendor lock-in.",
    thesis: "2M+ developers (up from 100K when Felicis invested). AI features (vector embeddings, pgvector) position them as the default database for AI apps. Developers love it: familiar PostgreSQL, powerful, zero vendor lock-in.",
    numbers: "$116M+ raised. Series C led by Felicis. YC S20. 2M+ developers. 65K+ GitHub stars. Remote-first, one of the fastest developer adoption curves in modern infrastructure.",
    category: "devtools"
  },
  {
    id: "runway", name: "Runway AI", color: "#EC4899", emoji: "🎬",
    oneliner: "The world's first AI video generation tool — used on Academy Award-winning films",
    fund: "Focus", stage: "Late", valuation: "", raised: "$200M+",
    location: "Brooklyn, NY",
    careers: "https://job-boards.greenhouse.io/runwayml/",
    founders: "Cristóbal Valenzuela (CEO): Chilean artist/economist who studied media arts at NYU Tisch. Co-created ml5.js. TIME100 AI Most Influential People (2023). 'Think of AI as a new type of camera.' Anastasis Germanidis and Alejandro Matamala — met at Tisch ~2016.",
    product: "Gen-3/Gen-4+ models for text-to-video, image-to-video, and video editing. Used by editors on 'Everything Everywhere All at Once' (Best Picture Oscar). Full-stack: foundational models to consumer creative tools. Building 'world models' that simulate reality.",
    thesis: "Used by The Late Show, ad agencies, architecture firms (KPF), and indie filmmakers. Annual AI Film Festival. Vision: every piece of media will eventually be AI-generated or AI-assisted.",
    numbers: "$200M+ raised. Investors: Google, NVIDIA, Salesforce, Felicis. Founded 2018. Academy Award-winning content made with their tools.",
    category: "devtools"
  },
  {
    id: "semgrep", name: "Semgrep", color: "#10B981", emoji: "🛡️",
    oneliner: "Code security that developers actually love — scanning 100M+ lines monthly",
    fund: "Focus", stage: "Growth", valuation: "", raised: "Multi-round",
    location: "San Francisco",
    careers: "https://jobs.ashbyhq.com/semgrep/",
    founders: "Isaac Evans (CEO): Built the company from academic research into a commercial powerhouse. Security research and developer tooling background. Realized shifting security 'left' required tools developers actually enjoy.",
    product: "Code security platform: 500+ built-in rules across 30+ languages. AI-powered Semgrep Assistant understands code context, reduces false positives, auto-triages. Rules look like the code they match — any developer can write security checks. Open-source core + enterprise.",
    thesis: "AI-generated code is flooding codebases — but AI makes mistakes. As every company ships more code faster with AI, the attack surface grows exponentially. Semgrep is the safety net. Scaled from thousands to 100M+ lines scanned monthly.",
    numbers: "100M+ lines scanned monthly. Major enterprise customers in tech, finance, healthcare. Multiple funding rounds including Felicis. San Francisco-based.",
    category: "security"
  },
  {
    id: "vannevar", name: "Vannevar Labs", color: "#6366F1", emoji: "🎯",
    oneliner: "AI-powered intelligence for national security — profitable and mission-critical",
    fund: "Focus", stage: "Growth", valuation: "$500M–$1B", raised: "Undisclosed",
    location: "San Francisco / NYC",
    careers: "https://job-boards.greenhouse.io/vannevarlabs",
    founders: "Brett Granberg (CEO) and Nini Moorhead. Named after Vannevar Bush, WWII science advisor who wrote 'As We May Think' (1945). They bring Silicon Valley engineering to defense's hardest problems.",
    product: "AI-powered intelligence and decision support for national security. Processes vast data — satellite imagery, signals intelligence, open-source data — surfacing actionable insights for military and intelligence operators. 'Google for defense analysts' with classified-level security.",
    thesis: "Geopolitical tensions rising. Military operations generate more data than humans can process. Felicis team 'flew across the country to have barbecue and discuss defense problems.' AI + defense is a market growing as governments realize AI is an operational necessity.",
    numbers: "Valued $500M–$1B. Profitable. Multiple government contracts. Active hiring for Forward Deployed Engineers. NYC satellite office.",
    category: "security"
  },
  {
    id: "corridor", name: "Corridor", color: "#8B5CF6", emoji: "🔒",
    oneliner: "Application security for AI-written code — led by a top hacker and Facebook's former CISO",
    fund: "FV 10", stage: "Early", valuation: "", raised: "Undisclosed",
    location: "San Francisco",
    careers: "https://jobs.ashbyhq.com/corridor/",
    founders: "Jack Cable (CEO): Hacker-turned-builder, career breaking real systems and securing critical infrastructure. Ashwin Ramaswami (CTO): Built security infrastructure across government, open source, and cloud. Ran for Georgia State Senate in 2024. Alex Stamos (Head of Product): Former CISO of Facebook.",
    product: "AI-native application security for modern development. Tools that understand AI-generated code patterns and catch vulnerabilities legacy scanners miss. Built for teams shipping with copilots and agents where code volume outpaces traditional review.",
    thesis: "Exceptional founding team: a top hacker (Cable), a security infra builder who ran for office (Ramaswami), and Facebook's former CISO (Stamos). Engineering from Applied Intuition, CMU, Vanta, Google, Stanford.",
    numbers: "Early-stage, Felicis Fund 10. Hiring across engineering (backend, frontend, infra, security, AI/ML) and Founding Technical Recruiter. Moving fast.",
    category: "security"
  },
  {
    id: "artemis", name: "Artemis", color: "#06B6D4", emoji: "🛡️",
    oneliner: "AI-native threat detection — what if your SIEM had AI-powered intuition?",
    fund: "FV 10", stage: "Early", valuation: "", raised: "Undisclosed",
    location: "New York",
    careers: "https://jobs.ashbyhq.com/artemis",
    founders: "Shachar Hirshberg: Ex-Palo Alto Networks, AWS, Demisto (acquired by PANW). Harvard Business School. Built cybersecurity products used by tens of thousands. Dan Shiebler: Ex-Abnormal Security (AI email security) and Twitter. Deep ML/AI expertise.",
    product: "AI-native cybersecurity platform using advanced ML for threat detection that traditional tools miss. Combines deep domain expertise from Palo Alto Networks and Abnormal Security with modern AI for next-gen detection and response.",
    thesis: "AI-generated code flooding codebases, AI agents in production, AI-powered attacks growing more sophisticated. Legacy security tools built for the pre-AI world can't keep pace. Founders have deep domain expertise from building security products at massive scale.",
    numbers: "Founded 2025, New York. Backed by Felicis and Lockstep (cybersecurity-focused VC). Actively hiring Senior Software Engineers. Early stage, building fast.",
    category: "security"
  },
  {
    id: "runlayer", name: "Runlayer", color: "#E11D48", emoji: "🏗️",
    oneliner: "Enterprise MCP security — signed 8 unicorns in 4 months, with the MCP co-creator as advisor",
    fund: "FV 10", stage: "Seed", valuation: "", raised: "$11M",
    location: "New York",
    careers: "https://jobs.ashbyhq.com/anysource",
    founders: "Andrew Berman (CEO): Serial entrepreneur — Nanit, Vowel (→ Zapier), became Director of AI at Zapier. Tal Peretz: Israeli Air Force ML, built Zapier MCP in 2 days — became fastest-growing product. Vitor Balocco: Staff AI Engineer at Zapier, MCP security expert.",
    product: "Command-and-control plane for enterprise MCP. Private registry of vetted servers, one-click installs, custom threat detection (tool poisoning, shadowing, command injection), fine-grained permissions, PII/token masking, observability. SOC2 Type II + HIPAA certified.",
    thesis: "MCP is now the standard (OpenAI, Microsoft, AWS, Google, Anthropic) but 10% of MCP servers are malicious. David Soria Parra (MCP co-creator at Anthropic) is Runlayer's angel investor. Travis McPeak (Head of Security at Cursor) is advisor.",
    numbers: "$11M seed led by Keith Rabois (Khosla) and Felicis. 8 unicorn/public customers in 4 months: Gusto, dbt Labs, Instacart, Opendoor, Lemonade.",
    category: "security"
  },
  {
    id: "sphere", name: "Sphere", color: "#7C3AED", emoji: "🌍",
    oneliner: "AI-native cross-border tax compliance — making global selling as easy as local",
    fund: "FV 8", stage: "Series A", valuation: "", raised: "$21M",
    location: "San Francisco",
    careers: "https://jobs.ashbyhq.com/sphere",
    founders: "Nicholas Rudder (Founder). Built direct integrations with 100+ global tax authorities over 18 months in stealth. Vision: 'Make selling globally as easy as selling locally.'",
    product: "End-to-end automated cross-border tax compliance: registration, calculation, filing, and remittance across 100+ jurisdictions. Proprietary TRAM (Tax Review and Assessment Model) codifies global tax law. Deploys in under 24 hours. One of only 3 tax vendors globally with native Stripe Billing/Checkout integration.",
    thesis: "a16z partner Marc Andrusko: 'Just as Deel redefined global payroll, Sphere is transforming revenue-based compliance.' Expanding beyond indirect tax into input tax, withholding, e-invoicing, and tariffs.",
    numbers: "$21M Series A led by Andreessen Horowitz, with YC and Felicis. Customers: Lovable, Replit, Windsurf, Deel, ElevenLabs, HeyGen. 30%+ monthly revenue growth since Dec 2024 launch.",
    category: "other"
  },
  {
    id: "unsiloed", name: "Unsiloed AI", color: "#F43F5E", emoji: "📄",
    oneliner: "Turn any document into structured AI-ready data — beating LlamaIndex and Gemini on benchmarks",
    fund: "FV 10", stage: "Seed", valuation: "", raised: "Pre-seed",
    location: "San Francisco",
    careers: "https://jobs.gem.com/unsiloed-ai",
    founders: "Aman Mishra (CEO): IIT Kharagpur. Built ultra low-latency trading systems at a hedge fund. Founding Engineer (#1) at a stealth startup building AI copilots for Goldman Sachs and Charles Schwab. Adnan Abbas (CTO): MIT + IIT Kharagpur. Built multimodal models at Fortune 10, autonomous nav at Mercedes-Benz.",
    product: "APIs turning complex unstructured data (PDFs, PPTs, DOCX, tables, charts, images) into structured Markdown/JSON for LLMs. Proprietary vision-language models — not just OCR. Outperforms LlamaIndex, Gemini, Mistral, and Unstructured.io on benchmarks. One API call replaces months of work.",
    thesis: "80%+ of enterprise data is multimodal and unstructured. Every AI agent and RAG pipeline needs reliable data ingestion. Already processing millions of pages weekly for Fortune 150 banks and NASDAQ companies.",
    numbers: "YC F25. ~7 employees. $550K revenue by Nov 2025. Processing millions of pages weekly. Customers: Fortune 150 banks, NASDAQ companies, 10+ YC startups.",
    category: "devtools"
  },
  {
    id: "phonic", name: "Phonic", color: "#F472B6", emoji: "🎙️",
    oneliner: "End-to-end voice AI platform — in-house models with 300ms latency for lifelike agent conversations",
    fund: "FV 10", stage: "Seed", valuation: "", raised: "$4M",
    location: "San Francisco",
    careers: "https://job-boards.greenhouse.io/phonic",
    founders: "Moin Nadeem (CEO): MEng + BS MIT. Previously at MosaicML (acquired by Databricks for $1.3B). Co-founded MIT's machine learning club. Nikhil Murthy (CTO): MEng + BS MIT. Deep expertise in audio foundation models and voice systems. They've known each other 7+ years and built Phonic's models entirely in-house.",
    product: "First end-to-end speech-to-speech platform for building conversational voice agents. Trains all models in-house — voice generation, recognition, and interaction unified in one system. Intelligent decision system replaces rigid decision trees, dynamically adapting to edge cases. 300ms end-to-end latency. Deploy via cloud API or on-premises.",
    thesis: "Voice AI is at a tipping point but reliability has been the blocker. Most companies stitch together disconnected ASR, LLM, and TTS layers. Phonic owns the full stack, enabling deeper integration of reliability into the models themselves. Working with insurance and healthcare companies where voice interactions are high-trust and high-stakes.",
    numbers: "$4M seed led by Lux Capital. Angels: Amjad Masad (Replit founder), Clem Delangue (Hugging Face founder), Qasar Younis (Applied Intuition founder), Erik Bernhardsson (Modal founder). Founded 2024, San Francisco.",
    category: "ai"
  },
];

const AIRTABLE_FORM = "https://airtable.com/appwB7m3bxjfGmDuB/pagN6zOVSylyRTBwh/form";

const getInterestUrl = (companyName) => {
  return `${AIRTABLE_FORM}?prefill_Primary+Company=${encodeURIComponent(companyName)}`;
};

const CATEGORIES = {
  all: { label: "All Companies", icon: "✦" },
  ai: { label: "AI / ML & Models", icon: "🔬" },
  energy: { label: "Energy & Infrastructure", icon: "⚡" },
  devtools: { label: "Developer Tools", icon: "🛠️" },
  security: { label: "Security & Defense", icon: "🔒" },
  other: { label: "Fintech & Other", icon: "📊" },
};

function CompanyCard({ company, onClick }) {
  return (
    <div onClick={onClick} className="fade-up" style={{
      background: "var(--card)", border: "1px solid var(--border)", borderRadius: 16,
      padding: "22px 24px", cursor: "pointer", transition: "all .25s ease",
      borderLeft: `3px solid ${company.color}`,
      position: "relative", overflow: "hidden",
    }}
    onMouseOver={e => { e.currentTarget.style.background = "var(--card-hover)"; e.currentTarget.style.borderColor = company.color + "44"; e.currentTarget.style.transform = "translateY(-2px)"; }}
    onMouseOut={e => { e.currentTarget.style.background = "var(--card)"; e.currentTarget.style.borderColor = "var(--border)"; e.currentTarget.style.transform = "translateY(0)"; }}
    >
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 10 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <span style={{ fontSize: 22 }}>{company.emoji}</span>
          <div>
            <div style={{ fontSize: 16, fontWeight: 600, color: "#f1f5f9", letterSpacing: "-0.01em" }}>{company.name}</div>
            <div style={{ display: "flex", gap: 6, marginTop: 4, flexWrap: "wrap" }}>
              <span style={{ fontSize: 10, padding: "2px 7px", borderRadius: 4, background: company.color + "18", color: company.color, fontWeight: 600, letterSpacing: "0.03em" }}>{company.stage}</span>
              {company.valuation && <span style={{ fontSize: 10, padding: "2px 7px", borderRadius: 4, background: "#1e293b", color: "#94a3b8", fontWeight: 500 }}>{company.valuation}</span>}
              <span style={{ fontSize: 10, padding: "2px 7px", borderRadius: 4, background: "#1e293b", color: "#94a3b8", fontWeight: 500 }}>📍 {company.location}</span>
            </div>
          </div>
        </div>
      </div>
      <p style={{ fontSize: 13.5, color: "#94a3b8", lineHeight: 1.6, margin: 0 }}>{company.oneliner}</p>
      {company.careers && (
        <div style={{ marginTop: 12 }}>
          <span style={{ fontSize: 11, color: "var(--green)", fontWeight: 500 }}>🟢 Hiring — View open roles →</span>
        </div>
      )}
    </div>
  );
}

function CompanyDetail({ company, onBack }) {
  const sections = [
    { title: "What They're Building", content: company.product, icon: "⚙️" },
    { title: "Founding Team", content: company.founders, icon: "👥" },
    { title: "Why This Matters", content: company.thesis, icon: "💡" },
    { title: "Key Numbers", content: company.numbers, icon: "📈" },
  ];

  return (
    <div className="fade-in" style={{ fontFamily: "'DM Sans', system-ui, sans-serif", background: "var(--bg)", minHeight: "100vh", color: "var(--text)", padding: "20px 16px" }}>
      <div style={{ maxWidth: 720, margin: "0 auto" }}>
        <button onClick={onBack} style={{ background: "none", border: "none", color: "var(--text-muted)", cursor: "pointer", fontSize: 13, fontFamily: "inherit", marginBottom: 20, padding: "6px 0" }}>← Back to all companies</button>

        <div style={{ borderLeft: `3px solid ${company.color}`, paddingLeft: 20, marginBottom: 28 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 6 }}>
            <span style={{ fontSize: 28 }}>{company.emoji}</span>
            <h1 style={{ fontSize: 26, fontWeight: 700, color: "#f8fafc", fontFamily: "'Fraunces', serif", letterSpacing: "-0.02em" }}>{company.name}</h1>
          </div>
          <p style={{ fontSize: 15, color: "#94a3b8", lineHeight: 1.65, maxWidth: 560, marginBottom: 14 }}>{company.oneliner}</p>
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 16 }}>
            <span style={{ fontSize: 11, padding: "4px 10px", borderRadius: 6, background: company.color + "18", color: company.color, fontWeight: 600 }}>{company.stage}</span>
            {company.valuation && <span style={{ fontSize: 11, padding: "4px 10px", borderRadius: 6, background: "#1e293b", color: "#cbd5e1", fontWeight: 500 }}>{company.valuation}</span>}
            {company.raised && <span style={{ fontSize: 11, padding: "4px 10px", borderRadius: 6, background: "#1e293b", color: "#cbd5e1", fontWeight: 500 }}>Raised: {company.raised}</span>}
            <span style={{ fontSize: 11, padding: "4px 10px", borderRadius: 6, background: "#1e293b", color: "#cbd5e1", fontWeight: 500 }}>📍 {company.location}</span>
          </div>

          {company.careers && (
            <a href={company.careers} target="_blank" rel="noopener noreferrer" style={{
              display: "inline-flex", alignItems: "center", gap: 8, padding: "12px 24px",
              background: company.color, color: "#000", fontWeight: 600, fontSize: 14,
              borderRadius: 10, textDecoration: "none", transition: "all .2s",
              boxShadow: `0 0 20px ${company.color}33`, marginRight: 10
            }}
            onMouseOver={e => e.currentTarget.style.transform = "translateY(-1px)"}
            onMouseOut={e => e.currentTarget.style.transform = "translateY(0)"}
            >
              View Open Roles →
            </a>
          )}
          <a href={getInterestUrl(company.name)} target="_blank" rel="noopener noreferrer" style={{
            display: "inline-flex", alignItems: "center", gap: 8, padding: "12px 24px",
            background: "transparent", color: company.color, fontWeight: 600, fontSize: 14,
            borderRadius: 10, textDecoration: "none", transition: "all .2s",
            border: `1.5px solid ${company.color}66`
          }}
          onMouseOver={e => { e.currentTarget.style.background = company.color + "18"; e.currentTarget.style.transform = "translateY(-1px)"; }}
          onMouseOut={e => { e.currentTarget.style.background = "transparent"; e.currentTarget.style.transform = "translateY(0)"; }}
          >
            ✋ I'm Interested
          </a>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          {sections.map((s, i) => (
            <div key={i} className="fade-up" style={{
              background: "var(--card)", border: "1px solid var(--border)", borderRadius: 14,
              padding: "20px 22px", animationDelay: `${i * 0.08}s`
            }}>
              <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 10 }}>
                <span style={{ fontSize: 15 }}>{s.icon}</span>
                <h3 style={{ fontSize: 13, fontWeight: 600, color: company.color, textTransform: "uppercase", letterSpacing: "0.06em" }}>{s.title}</h3>
              </div>
              <p style={{ fontSize: 14, lineHeight: 1.75, color: "#cbd5e1", whiteSpace: "pre-line" }}>{s.content}</p>
            </div>
          ))}
        </div>

        <div style={{ textAlign: "center", marginTop: 32, marginBottom: 40, padding: "28px 20px", background: "var(--card)", border: `1px solid ${company.color}33`, borderRadius: 16 }}>
            <p style={{ fontSize: 14, color: "#94a3b8", marginBottom: 14 }}>Interested in {company.name}?</p>
            <div style={{ display: "flex", gap: 10, justifyContent: "center", flexWrap: "wrap" }}>
              {company.careers && (
                <a href={company.careers} target="_blank" rel="noopener noreferrer" style={{
                  display: "inline-flex", alignItems: "center", gap: 8, padding: "14px 32px",
                  background: company.color, color: "#000", fontWeight: 700, fontSize: 15,
                  borderRadius: 12, textDecoration: "none",
                  boxShadow: `0 0 30px ${company.color}44`
                }}>
                  View Open Roles →
                </a>
              )}
              <a href={getInterestUrl(company.name)} target="_blank" rel="noopener noreferrer" style={{
                display: "inline-flex", alignItems: "center", gap: 8, padding: "14px 32px",
                background: "transparent", color: company.color, fontWeight: 700, fontSize: 15,
                borderRadius: 12, textDecoration: "none",
                border: `1.5px solid ${company.color}66`
              }}>
                ✋ Tell Felicis I'm Interested
              </a>
            </div>
          </div>
      </div>
    </div>
  );
}

function App() {
  const [selected, setSelected] = useState(null);
  const [filter, setFilter] = useState("all");
  const [search, setSearch] = useState("");

  const filtered = COMPANIES.filter(c => {
    const matchCat = filter === "all" || c.category === filter;
    const matchSearch = !search || c.name.toLowerCase().includes(search.toLowerCase()) || c.oneliner.toLowerCase().includes(search.toLowerCase()) || c.founders.toLowerCase().includes(search.toLowerCase());
    return matchCat && matchSearch;
  });

  if (selected) {
    return <CompanyDetail company={selected} onBack={() => setSelected(null)} />;
  }

  return (
    <div style={{ fontFamily: "'DM Sans', system-ui, sans-serif", background: "var(--bg)", minHeight: "100vh", color: "var(--text)", padding: "32px 16px 60px" }}>
      <div style={{ maxWidth: 900, margin: "0 auto" }}>
        {/* Header */}
        <div style={{ textAlign: "center", marginBottom: 36 }}>
          <div style={{ fontSize: 10, letterSpacing: 4, color: "var(--text-muted)", textTransform: "uppercase", marginBottom: 8, fontWeight: 500 }}>Felicis Ventures Portfolio</div>
          <h1 style={{ fontFamily: "'Fraunces', serif", fontSize: 34, fontWeight: 700, color: "#f8fafc", letterSpacing: "-0.03em", lineHeight: 1.2, marginBottom: 10 }}>
            Where to Build Next
          </h1>
          <p style={{ color: "var(--text-muted)", fontSize: 14, maxWidth: 480, margin: "0 auto", lineHeight: 1.6 }}>
            {COMPANIES.length} companies shaping the future of AI, energy, developer tools, and security. Find your next role.
          </p>
          <a href={AIRTABLE_FORM} target="_blank" rel="noopener noreferrer" style={{
            display: "inline-flex", alignItems: "center", gap: 6, marginTop: 14, padding: "10px 22px",
            background: "var(--accent)" + "18", color: "var(--accent)", fontWeight: 600, fontSize: 13,
            borderRadius: 8, textDecoration: "none", border: "1px solid var(--accent)" + "44",
            transition: "all .2s"
          }}>
            ✋ Express interest in a company
          </a>
        </div>

        {/* Search */}
        <div style={{ marginBottom: 16 }}>
          <input
            type="text" value={search} onChange={e => setSearch(e.target.value)}
            placeholder="Search companies, founders, technologies..."
            style={{
              width: "100%", padding: "13px 18px", background: "var(--surface)", border: "1px solid var(--border)",
              borderRadius: 12, color: "var(--text)", fontSize: 14, fontFamily: "inherit", outline: "none",
              transition: "border .2s"
            }}
            onFocus={e => e.target.style.borderColor = "var(--accent)"}
            onBlur={e => e.target.style.borderColor = "var(--border)"}
          />
        </div>

        {/* Category Filters */}
        <div style={{ display: "flex", gap: 6, marginBottom: 28, flexWrap: "wrap" }}>
          {Object.entries(CATEGORIES).map(([key, { label, icon }]) => (
            <button key={key} onClick={() => setFilter(key)} style={{
              padding: "8px 14px", borderRadius: 8, border: "1px solid",
              borderColor: filter === key ? "var(--accent)" : "var(--border)",
              background: filter === key ? "var(--accent)" + "18" : "transparent",
              color: filter === key ? "var(--accent)" : "var(--text-muted)",
              fontSize: 12, fontWeight: 500, cursor: "pointer", fontFamily: "inherit",
              transition: "all .2s", whiteSpace: "nowrap"
            }}>
              {icon} {label}
            </button>
          ))}
        </div>

        {/* Stats Bar */}
        <div style={{ display: "flex", gap: 16, marginBottom: 24, flexWrap: "wrap" }}>
          {[
            { n: filtered.length, l: "companies" },
            { n: filtered.filter(c => c.careers).length, l: "hiring now" },
            { n: filtered.filter(c => c.stage === "Early" || c.stage === "Seed").length, l: "early stage" },
          ].map((s, i) => (
            <div key={i} style={{ fontSize: 12, color: "var(--text-muted)" }}>
              <span style={{ color: "#f1f5f9", fontWeight: 700, fontSize: 16 }}>{s.n}</span> {s.l}
            </div>
          ))}
        </div>

        {/* Company Grid */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(min(340px, 100%), 1fr))", gap: 12 }}>
          {filtered.map((c, i) => (
            <div key={c.id} style={{ animationDelay: `${i * 0.04}s` }}>
              <CompanyCard company={c} onClick={() => setSelected(c)} />
            </div>
          ))}
        </div>

        {filtered.length === 0 && (
          <div style={{ textAlign: "center", padding: 60, color: "var(--text-muted)" }}>
            <div style={{ fontSize: 32, marginBottom: 10 }}>🔍</div>
            <p>No companies match your search.</p>
          </div>
        )}

        {/* Footer */}
        <div style={{ textAlign: "center", marginTop: 48, paddingTop: 24, borderTop: "1px solid var(--border)" }}>
          <p style={{ fontSize: 12, color: "var(--text-dim)" }}>
            Felicis Ventures · Portfolio Talent Network
          </p>
        </div>
      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
</script>
</body>
</html>
