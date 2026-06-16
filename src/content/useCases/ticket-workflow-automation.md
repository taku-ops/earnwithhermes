---
title: "Hermes Triage: Auto-Managing Tickets in Your PM Software"
date: 2026-06-10
draft: false
description: "How @dalekc72 wired Hermes and Claude Code to Plane.so — tickets come in, Hermes triages and assigns, and documents the outcome in Obsidian. Paperclip that gets stuff done."
tags: ["ticket-management", "project-management", "plane-dot-so", "automation", "claude-code", "obsidian", "ops"]
categories: ["Building Products"]
author: "@dalekc72"
storySource: "Discord"
---

@dalekc72 wired Hermes and Claude Code directly into Plane.so. Tickets come in, get triaged, assigned, worked, and documented, all autonomously.

> *"Super excited that Hermes and Claude Code are now working tickets in my PM software, Plane.so. Tickets come in and Hermes triages and assigns and starts working the tickets. Basically Paperclip that gets sh*t done. They then document in the ticket and if needed create documentation for Obsidian."*
>
> — **@dalekc72** on Discord

---

### The Ticket Pipeline

```
Ticket created
    |
Hermes reads: title, description, labels, priority
    |
Hermes triages: category, assignee, urgency
    |
Claude Code executes: if coding task, work the ticket
    |
Documentation: updates ticket, creates Obsidian notes if needed
    |
Done: ticket resolved, team notified
```

### Design

- **Zero human triage.** Hermes reads and categorizes instantly.
- **Claude Code integration.** Code-level tickets get worked automatically.
- **Obsidian documentation.** Knowledge persists beyond the ticket.
- **Plane.so native.** No custom middleware needed.

---

### Setup Steps

1. **Set up Plane.so** (or any PM tool with API).
2. **Wire webhooks.** Ticket creation triggers Hermes.
3. **Build the triage skill.** Categorize by type, urgency, assignee.
4. **Connect Claude Code.** For tickets that need code changes.
5. **Add Obsidian connector.** Auto-create documentation when patterns repeat.
6. **Set up daily digest.** Cron job to report what was resolved.
