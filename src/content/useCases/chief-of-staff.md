---
title: "Hermes as Chief of Staff — Multi-Project Agent OS"
date: 2026-04-10
draft: false
description: "Running a full project operating system on Hermes — one Chief of Staff agent with per-project sub-profiles, cross-project memory, nightly backups, and daily WhatsApp reporting."
tags: ["chief-of-staff", "project-management", "multi-project", "profiles", "vps", "backup", "whatsapp"]
categories: ["Agency & Consulting"]
author: "@ogiberstein"
storySource: "Discord"
---

## An Agent Operating System for Your Projects

When Hermes becomes an **operating system for your work** instead of a single assistant, one "Chief of Staff" agent coordinates a fleet of project-specific sub-agents, each with their own memory and context.

> *"My 'main agent' is my 'Chief of Staff' who has his own memory cross-project/workflow. Every 'project' (1 project = 1 Slack channel) has its own agent sub-profile with its own memory. The whole system runs on a VPS, with backup routing if the main model fails, and gets backed up every night to Github. Daily reporting is sent to WhatsApp."*
>
> — **@ogiberstein** on Discord

---

### Architecture: The Agent OS

```
┌─────────────────────────────────────────┐
│          CHIEF OF STAFF AGENT           │
│   (Cross-project memory, coordination)  │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐│
│  │ Project  │ │ Project  │ │ Project  ││
│  │ Agent A  │ │ Agent B  │ │ Agent C  ││
│  │ (memory) │ │ (memory) │ │ (memory) ││
│  └──────────┘ └──────────┘ └──────────┘│
│                                         │
│  ┌─────────────────────────────────┐    │
│  │      Infrastructure Layer       │    │
│  │  VPS + Nightly GitHub Backup    │    │
│  │  + Fallback Model Routing       │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### The Components

**1. Chief of Staff Agent:** The "main" agent with cross-project memory. It knows what's happening across all projects, can spot dependencies, and coordinates handoffs.

**2. Project Sub-Agents:** Each project (mapped to a Slack channel) gets its own Hermes profile with dedicated memory. This means Project A's context doesn't leak into Project B, but the Chief of Staff can pull information from both.

**3. Slack Integration:** Projects are managed in Slack channels, making collaboration with human team members seamless.

**4. Backup Routing:** If the primary model fails (API outage, rate limit, etc.), the system automatically falls back to a secondary model. No downtime.

**5. Nightly GitHub Backups:** The entire agent state — profiles, memory, skills, cron jobs — is backed up to GitHub every night. Full recovery from any disaster.

**6. WhatsApp Daily Reporting:** Every morning, a concise summary of what happened across all projects is delivered directly to the user's phone.

The setup runs 24/7, keeps cross-project context, and scales to any number of projects.

---

## Setup

1. **Set up Hermes on a VPS** — You need persistent uptime
2. **Create your Chief of Staff profile** — Give it a SOUL.md focused on coordination and high-level awareness
3. **Create sub-profiles per project** — Each with narrowed context and domain-specific skills
4. **Connect Slack channels** — One channel per project, with the agent in each
5. **Set up backup routing** — Configure OpenRouter with fallback models
6. **Add cron-based GitHub backups** — `git add && git commit && git push` nightly
7. **Configure WhatsApp reporting** — Use the Hermes WhatsApp integration for daily summaries

Start with 2-3 projects, get the rhythm right, then expand. The agent OS grows with you.
