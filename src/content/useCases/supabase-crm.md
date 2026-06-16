---
title: "24/7 Supabase CRM for Less Than ChatGPT Plus"
date: 2026-03-15
draft: false
description: "A full CRM assistant powered by Hermes Agent and Supabase — with real data management, persistent memory, and autonomous skill creation — all for under $20/month."
tags: ["crm", "supabase", "database", "cost-savings", "autonomous", "skill-creation"]
categories: ["Agency & Consulting"]
author: "Derek Cheung"
storySource: "YouTube"
---

Derek Cheung built a Hermes Agent connected to Supabase that manages real customer data, autonomously proposed and built a new skill from its own reflection, and costs less than a single ChatGPT Plus subscription.

> *"Less than a single ChatGPT Plus subscription for a 24/7 assistant with real data management. After several interactions, Hermes autonomously proposed a new 'Supabase MCP scripts' skill — created from its own reflection."*
>
> — **Derek Cheung** on [YouTube](https://www.youtube.com/watch?v=W_ZgH0WPayo) (2026)

---

### Architecture

This setup connects Hermes to a real database (Supabase, a Firebase-like backend-as-a-service), giving it:

- **Persistent customer records.** Hermes can create, read, update, and delete CRM entries.
- **Real data management.** Not mock data, not a spreadsheet, but a proper relational database.
- **Autonomous operation.** Running 24/7 without human intervention.
- **Self-improvement.** The agent autonomously identified a gap in its capabilities and built a new skill to fill it.

### Skill Creation

After several interactions, Hermes noticed a pattern: it kept reaching for the same database operations. It proposed, unprompted, a new "Supabase MCP scripts" skill to make those operations more efficient. It then built that skill itself.

### Cost Comparison

| Service | Monthly Cost | 24/7 Operation | Real Data | Self-Improving |
|---------|-------------|----------------|-----------|----------------|
| Hermes + Supabase | **< $20/mo** | Yes | Yes | Yes |
| ChatGPT Plus | $20/mo | No | No | No |
| Enterprise CRM | $50-200/mo | No | Yes | No |

---

### Setup Steps

1. **Set up Hermes.** Deploy on a VPS or home server.
2. **Create a Supabase account.** The free tier is generous enough for small CRMs.
3. **Design your database schema.** Tables for contacts, deals, interactions, etc.
4. **Write MCP (Model Context Protocol) scripts.** Give Hermes the ability to query and mutate data.
5. **Add your customer data.** Import existing records or start fresh.
6. **Define workflows.** Lead capture, follow-up reminders, deal stage tracking.
7. **Let it improve.** Hermes will naturally identify gaps and propose new skills.
