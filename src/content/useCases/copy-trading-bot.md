---
title: "Copy-Trading Bot: Rebuilt With Hermes Agent and Claude Code"
date: 2026-06-03
draft: false
description: "Gencay rebuilt his copy-trading bot to run on a Mac Mini with Hermes Agent — finding profitable Hyperliquid traders, tracking positions every 5 minutes, and reporting via Telegram. No GitHub Actions, no external scheduler."
tags: ["trading", "copy-trading", "hyperliquid", "mac-mini", "cron", "telegram", "claude-code"]
categories: ["Trading & Markets"]
author: "Gencay"
storySource: "Substack"
---

## From GitHub Actions to Always-On Trading

Gencay had a working copy-trading bot built with Claude Code, but it ran on GitHub Actions and had a problem: GitHub silently skipped roughly 80% of frequent jobs when its servers were busy. The bot needed an external scheduler and a Slack webhook just to stay alive. Changing it meant editing code, pushing a commit, and waiting for the action to run.

He rebuilt it on a Mac Mini with Hermes Agent. The cron lives inside the agent now — no external scheduler needed.

> *"The difference is that I can change the bot by talking to it."*
>
> — **Gencay** on [LearnAIWithMe Substack](https://www.learnwithmeai.com/p/claude-code-copy-trading-bot) (June 3, 2026)

---

### Three Decoupled Jobs

| Job | Frequency | What It Does |
|-----|-----------|--------------|
| **Job A** | Once daily | Pulls Hyperliquid leaderboard, filters and ranks traders by execution quality, writes shortlist to JSON |
| **Job B** | Every 5 minutes | Reads shortlist, fetches open positions, compares with last snapshot — new positions trigger BUY, closed positions trigger SELL |
| **Job C** | Every 30 minutes | Reads state, calculates 24h PnL and activity, sends a pulse to Telegram |

### Why Hermes Fixed the Old Problems

The old GitHub Actions setup was fragile. Jobs got dropped, changes required a full git commit cycle, and the bot needed two external services just to stay on schedule.

Hermes handles cron natively. Tell it "run every 5 minutes" and it does. No silent skips, no external scheduler, no webhooks.

Telegram became both the reporting channel and the command interface. Send a sentence to change the bot's behavior — no code commit needed.

### The Setup

1. Run Hermes on an always-on machine (Mac Mini, Hetzner, or AWS)
2. Create a new agent in Hermes, point it at a dedicated Telegram channel
3. Claude Code writes the trading script, a Hermes skill places it directly
4. Tell Hermes the schedule in plain language — it sets its own cron

The author recommends Hetzner or AWS if you don't have a spare machine.

---

## Do This Yourself

1. Get an always-on machine — Mac Mini, Hetzner VPS, or AWS instance
2. Install Hermes Agent and connect it to a Telegram channel
3. Write your trading script — or adapt an existing one
4. Define your jobs in plain language to Hermes's cron
5. Start with a paper portfolio, verify the strategy, then go live
