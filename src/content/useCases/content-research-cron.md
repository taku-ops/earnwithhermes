---
title: "Weekly Cron: Auto-Research the Top 3 AI Tools for Your Next Video"
date: 2026-06-10
draft: false
description: "A YouTube creator set up a Monday morning cron that researches trending AI tools, picks the top 3 for tutorials, and writes itself a new skill — entirely autonomous."
tags: ["youtube", "content-research", "cron", "video-creation", "ai-tools", "trend-discovery", "automation"]
categories: ["Content Monetization"]
author: "Metrics Media"
storySource: "YouTube"
---

## The Self-Improving Research Pipeline

Metrics Media wanted a system that finds trending AI tools before the competition, ranks the top 3 for tutorial videos, and keeps getting better at it. The solution: a weekly cron job that not only does the research — it writes a SKILL.md so the approach improves over time.

> *"Research the top trending AI tools right now and come back with the top three that would make for an interesting tutorial video. Create a new skill based on your approach and call it YouTube-video-research. Can you set up a weekly job that runs every Monday at 9:00 AM using that skill?"*
>
> — **Metrics Media** on [YouTube](https://www.youtube.com/watch?v=CwPUOVUdApE)

---

| Problem | Solution |
|---------|----------|
| Wasting hours researching trends | Hermes does it Monday morning |
| Not knowing what's hot before competitors | Automated trend scanning |
| Reinventing the research process each week | Skill persists and improves |
| Forgetting to check sources | Cron runs without fail |

### The Self-Improvement Loop

1. Hermes researches trending AI tools from multiple sources
2. Ranks top 3 based on tutorial potential
3. Creates or updates a SKILL.md with the methodology
4. Next Monday: the skill is better than the last run

---

## Setup

1. **Define your niche** — AI tools, SaaS, marketing, whatever you cover
2. **List research sources** — Product Hunt, GitHub trending, HN, Reddit, Twitter
3. **Create the research skill** — Prompt Hermes to write the SKILL.md
4. **Set up the cron** — `0 9 * * 1` (every Monday at 9am)
5. **Wire delivery** — Output to email, Discord, or your content calendar
6. **Review and shoot** — Monday morning, you have your topics ready
