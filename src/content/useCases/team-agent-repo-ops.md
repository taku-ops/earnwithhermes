---
title: "One Team Agent: Repos, Onchain Debug, Protocol Docs"
date: 2026-06-10
draft: true
description: "How @megabyte0x integrated Hermes with SourceDev for repo indexing, Tenderly MCP for onchain debugging, and LLM-Wiki for protocol documentation — a team-wide agent that knows the entire stack."
tags: ["team-agent", "repo-indexing", "onchain", "blockchain", "documentation", "web3", "tenderly"]
categories: ["Building Products"]
author: "@megabyte0x"
storySource: "Discord"
---

## The Team Agent That Knows Everything

Imagine a single agent that can search your internal repos, debug a failing blockchain transaction, and answer questions about your protocol documentation — all through the same chat interface. @megabyte0x built exactly that, integrating three powerful tools into one Hermes agent accessible to the entire team.

> *"It's integrated with SourceDev to index repos (self hosted), Tenderly MCP to debug onchain transactions, LLM-Wiki ingest of Litepaper of our protocol and other docs. Hopefully team will find it useful and will integrate more infra tools over time to help the team."*
>
> — **@megabyte0x** on Discord

---

### The Integration Stack

| Tool | Purpose | How Hermes Uses It |
|------|---------|-------------------|
| SourceDev | Repo indexing | Search code, find patterns, read commits |
| Tenderly MCP | Onchain debugging | Trace failing transactions, diagnose contract issues |
| LLM-Wiki | Protocol docs | Answer team questions about the protocol |

### Why This Works for Teams

- **Single interface** — No more switching between GitHub, Etherscan, and Notion
- **Institutional memory** — Every answer and action persists
- **Autonomous debugging** — Hermes can trace and diagnose without human step-by-step
- **Scalable** — Add more tool integrations over time

---

## How You Can Do This Too

1. **Set up SourceDev** or similar self-hosted code search
2. **Connect your repositories** — Git repos Hermes can search
3. **Wire Tenderly MCP** — For onchain debugging (if applicable)
4. **Ingest documentation** — LLM-Wiki or similar doc ingestion
5. **Make it team-accessible** — Share the Hermes session or gateway
6. **Add more tools** — CI/CD status, deployment logs, monitoring
