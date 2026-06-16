---
title: "Competitor Analysis Swarm: Ported From Codex to Hermes"
date: 2026-06-10
draft: false
description: "How @zedosplasticos ported a working competitor-analysis swarm from Codex to Hermes — analyzing businesses and their competitors to find gaps and SEO/positioning strategies."
tags: ["competitor-analysis", "swarm", "business-intelligence", "seo", "positioning", "codex", "automation"]
categories: ["Agency & Consulting"]
author: "@zedosplasticos008"
storySource: "Discord"
---

## The Swarm That Finds Market Gaps

Building a swarm that analyzes businesses, their competitors, and produces practical strategy recommendations is no small feat. @zedosplasticos did it on Codex, then ported the entire thing to Hermes, finding the transition smoother than expected.

> *"I was building a swarm (that actually works) on codex to analyse business and their competitors. To find gaps and build a strategy to outrank them. After a couple a hours, pushing the swarm to hermes and convert it to hermes env. It made a really good job."*
>
> — **@zedosplasticos008** on Discord

---

### What the Swarm Does

1. Analyze a target business — products, pricing, positioning, SEO
2. Identify top 3-5 competitors
3. Find gaps in competitor strategies
4. Build an actionable outrank/outposition strategy

### Why Hermes Was the Right Home

| Factor | Codex | Hermes |
|--------|-------|--------|
| Persistent memory | Sessions are isolated | Cross-session context |
| Tool ecosystem | Limited | 40+ built-in tools |
| Cron/scheduling | Manual runs | Automated recurring jobs |
| Skill persistence | Not native | SKILL.md self-improvement |

---

## Setup

1. **Define the analysis scope** — What industries, what data sources
2. **Build the research subagents** — One per competitor, run in parallel
3. **Create the gap analysis skill** — Compare positioning, SEO, messaging
4. **Add strategy generation** — Hermes drafts the outrank plan
5. **Schedule recurring runs** — Weekly or monthly competitor monitoring
