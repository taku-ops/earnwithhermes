---
title: "ZeroID: Fix Sub-Agent Scope Delegation and Context Costs"
date: 2026-06-10
draft: true
description: "How @justin_albrethsen built ZeroID — an agent identity layer using RFC 8693 token exchange — to fix the cost and scope delegation problems that make sub-agents expensive."
tags: ["cost-optimization", "sub-agents", "zero-id", "context-window", "scope-delegation", "architecture"]
categories: ["Cost Savings"]
author: "@justin_albrethsen"
storySource: "Discord"
---

## The Hidden Cost of Sub-Agents

Sub-agents are Hermes's superpower — but they come with a hidden cost: context windows filling up with delegation instructions, permissions, and scope definitions. @justin_albrethsen identified this problem and built ZeroID, an agent identity layer that eliminates the overhead.

> *"One of the problems I run into with Hermes is high cost when context windows fill up. One method to fix this is heavy use of sub-agents, but permissions/scope delegation to the sub-agent is often problematic. ZeroID is an agent identity layer that uses RFC 8693 token exchange to handle scope delegation."*
>
> — **@justin_albrethsen** on Discord

---

### The Problem

| Issue | Cost Impact |
|-------|-------------|
| Full scope definition per sub-agent call | Wastes 500-2000 tokens per delegation |
| Permission checking each time | Context gets polluted with rules |
| No identity persistence | Sub-agent restarts from scratch |

### How ZeroID Fixes It

ZeroID uses the OAuth-style RFC 8693 token exchange pattern: a sub-agent receives a compact token that encodes its identity, scope, and permissions. The parent doesn't need to re-explain everything — the token says it all.

---

## How You Can Do This Too

1. **Audit your sub-agent costs** — How many tokens are delegation overhead?
2. **Understand RFC 8693** — Token exchange for scoped access
3. **Build a permission schema** — What can each sub-agent role do?
4. **Implement token exchange** — Compact identity tokens per sub-agent
5. **Measure savings** — Track context token reduction per delegation
