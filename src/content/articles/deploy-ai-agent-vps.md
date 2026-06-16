---
title: "How to Deploy Hermes Agent on a Budget VPS (Beginner's Guide)"
date: 2026-05-09T00:00:00Z
draft: false
description: "Want to deploy your own Hermes Agent on a VPS with Telegram integration? This step-by-step guide walks you through it - no server experience needed."
tags: ["tutorial", "hermes-agent", "vps", "digitalocean", "telegram", "self-hosting", "beginner tutorial", "AI agent deployment", "cloud server", "DevOps"]
categories: ["tutorials"]
canonicalURL: "https://earnwithhermes.com/learn/deploy-ai-agent-vps/"
---

## Before You Start: What You'll Need

This guide is built for **absolute beginners** - no server experience required. Here's what you need before we begin:

- **A computer** (Mac, Windows, or Linux)
- **A phone or computer with Telegram** (free, takes 2 minutes to install)
- **A VPS provider account** (the guide covers how to set one up)
- **15 minutes of focused time**

> **Total cost to deploy:** roughly $6/month for the server, plus small AI usage fees depending on how much you use your agent (typically a few dollars per month).

---

## What Is Hermes Agent?

[Hermes Agent](https://hermes-agent.nousresearch.com) is an open-source AI agent that can browse the web, run code, write files, search your notes, and use tools - all autonomously. Think of it as a capable assistant you can give tasks to and it works through them on its own.

It runs in your terminal or as a Telegram bot, connects to any major AI model (OpenRouter, DeepSeek, Anthropic, etc.), and is designed to be self-hosted. That means you own it - open source, no per-seat subscription, no vendor lock-in, and full control over how it's set up and configured.

## What Is a VPS and Why Do You Need One?

A **VPS** (Virtual Private Server) is just a computer that lives in a data center and stays on 24/7. Think of it as your laptop, but someone else pays the electricity bill, it never goes to sleep, and you access it over the internet.

Three reasons to put your AI agent on a VPS instead of your laptop:

1. **Persistence** - your agent runs 24/7. You log out, it stays put.
2. **Phone-native** - talk to your agent from Telegram on your phone. No terminal needed.
3. **Elastic** - one agent today, ten next week. A VPS doesn't care.

A budget VPS gives you room to run multiple agents, a database, or a web dashboard without upgrading.

## Step 1: Get a Cloud Server (VPS)

### What Is DigitalOcean?

DigitalOcean is a cloud hosting company. They rent you small virtual servers called **Droplets** starting at a few dollars per month.

**[👉 Sign up for DigitalOcean here](https://m.do.co/c/940ca4b955e8).**

Once you're signed in:

1. Click **Create → Droplets** (big green button)
2. Under **Choose Region**, pick a data center close to you (e.g., New York if you're on the US East Coast)
3. Under **Choose an image**, select **Ubuntu 24.04 LTS** - LTS stands for Long Term Support, meaning it gets security updates for years without needing a major upgrade
4. Under **Choose size**, pick the **$6/month** plan (called "Basic" with 1 GB RAM / 1 CPU - enough for Hermes Agent plus room to grow)
5. Under **Add SSH Key** - keep reading, the next section explains this
6. Click **Create Droplet**

> **Pro tip:** Skip all the add-ons (backups, monitoring, etc.) for now. You can add them later. The base plan is plenty for an AI agent.

### About SSH Keys (What They Are and How to Create One)

When you create your server, you need a way to prove you're the owner. That's what an **SSH key** does - it's like a digital key that unlocks your server.

**On Mac or Linux:** Open your **Terminal** app. Type:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Hit **Enter** three times (accept the defaults). Then show your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the output (it starts with `ssh-ed25519`). Paste this into the DigitalOcean "Add SSH Key" section.

**On Windows:** Use [PuTTYgen](https://www.puttygen.com/) or install [Git Bash](https://git-scm.com/downloads) and follow the Mac instructions above.

> **Don't have an SSH key yet?** No worries - most people don't on their first try. The commands above create one. If you get stuck, DigitalOcean has [a visual guide here](https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/).

### Connect to Your Server

Once your Droplet is created, DigitalOcean gives you an **IP address** (looks like `192.0.2.123`). Copy it.

Open your **Terminal** (Mac/Linux) or **Command Prompt / PowerShell** (Windows) and type:

```bash
ssh root@YOUR_DROPLET_IP
```

Replace `YOUR_DROPLET_IP` with the actual IP DigitalOcean gave you. So if your IP is `192.0.2.123`, you'd type:

```bash
ssh root@192.0.2.123
```

If it asks "Are you sure you want to continue connecting?" - type **yes** and hit Enter.

You should see a welcome message. **That's it** - you're inside your server. The rest of the commands in this guide get typed in this same terminal window.

> **⚠️ Common problem:** If you get "Permission denied" or "Connection refused":
> - Make sure you added your SSH key when creating the Droplet (Step 1.5)
> - Wait 30 seconds and try again - the server takes a moment to boot
> - Double-check you copied the IP address correctly

## Step 2: Install the AI Agent Software

Now that you're connected to your server, you need to install Hermes Agent - the AI agent software. Copy and paste this command:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

**What this does:** It downloads the installation script from the Hermes Agent team and runs it. The installer detects that you're on Linux, downloads everything needed, and sets up the `hermes` command.

After it finishes, run this to reload your terminal:

```bash
source ~/.bashrc
```

Then verify it worked:

```bash
hermes --version
```

You should see something like `v0.x.x`. If you see a version number, the installation succeeded.

The whole thing takes about 30 seconds. You now have one of the most powerful open-source AI agents on your server, waiting for instructions.

> **⚠️ Common problem:** If `hermes --version` says "command not found":
> - Make sure you ran `source ~/.bashrc` after the install
> - Try logging out (`exit`) and SSH back in again

## Step 3: Choose and Configure an AI Model

Hermes Agent needs an **AI model** to do its thinking - this is the brain that decides which tools to use and how to answer you.

### Where to Get an API Key

An **API key** is like a password that links your agent to the AI provider's servers. You'll need one before you can configure your agent.

| Provider | Best For | Sign Up | Typical Monthly Cost |
|----------|----------|---------|---------------------|
| **[OpenRouter](https://openrouter.ai)** | Beginners - one key, 100+ models | Sign up, add $5 credit | $1-5 for light use |
| **[DeepSeek](https://platform.deepseek.com)** | Cheapest option, good for agents | Sign up, add credit | <$1 for light use |
| **[Anthropic](https://console.anthropic.com)** | Strong reasoning capabilities | Sign up, use free trial | Generous free credit included |

> **💡 Tip:** Start with **OpenRouter**. Put in $5 and you'll have months of use. You can switch providers anytime.
>
> **⚠️ Important:** API keys are usually shown **only once** when you create them. Copy your key immediately and store it somewhere safe - like a password manager or a text file on your computer. If you lose it, you'll need to generate a new one from the provider's dashboard.

### Configure the AI Provider

```bash
hermes setup model
```

The setup wizard will walk you through:

1. **Pick a provider** - I recommend **OpenRouter** to start. One account gives you access to every major AI model, and you only pay for what you use.
2. **Enter your API key** - paste the key you saved from the step above
3. **Select a default model** - pick a fast, cheap model like `deepseek-v4-flash`

### How Much Does AI Usage Cost?

There's no fixed monthly fee - you pay based on **how much you use your agent** and **which model** you choose. A quick chat costs fractions of a cent. Heavy daily use with a powerful model might run $5-10/month. The $5 credit on OpenRouter will last most beginners months.

### Test Your Agent

Once configured, test it:

```bash
hermes
```

You're now talking to an autonomous AI agent running on a cloud server - accessible from anywhere in the world. Type "Hello, what can you do?" and watch it respond.

Type `/exit` to quit the conversation (but don't worry - your agent stays installed on the server).

## Step 4: Connect Your Agent to Telegram

This is where it gets fun. Your agent lives on the server, but you talk to it from your phone - like texting an assistant.

### Create a Telegram Bot

1. Open Telegram on your phone or computer
2. Search for **@BotFather** (it's Telegram's official bot-creation tool, verified with a blue checkmark)
3. Send the message `/newbot`
4. BotFather will ask for a **name** - this is what shows in your chat (e.g., "My AI Assistant")
5. Then it asks for a **username** - must end in "bot" (e.g., `my_ai_helper_bot`)
6. BotFather replies with a **bot token** - this looks like a long string of letters and numbers

> **What is a bot token?** Think of it as a password for your bot. It lets Hermes Agent post messages in your Telegram chat as if it's the bot. **Never share this token with anyone.**

### Link the Bot to Your Agent

Back in your server terminal, run:

```bash
hermes gateway setup
```

When it asks for your **bot token**, paste the one BotFather gave you. That's it.

Now open Telegram and find your bot (search the username you chose). Send `/start`. Your agent responds instantly - from the VPS, not from your laptop.

**Test the magic:** Log out of your server (type `exit`). Wait 30 seconds. Send your bot another message from Telegram. It still works.

> **That's the whole point.** Your agent stays online even when you're not at your computer.

## Step 5: Run Your First Real Task

You have an always-on AI agent in your pocket. Try asking it to do something genuinely useful:

> "Search Hacker News for the latest AI agent tools. Summarize the top 3 and save them to a markdown file."

Your agent will:
┃ 1. Browse the web and search Hacker News
┃ 2. Read several articles
┃ 3. Write a summary markdown file on the server
┃ 4. Send you a formatted reply on Telegram with what it found

All while you make coffee, drive, or sleep. Your agent doesn't need your attention to work.

## Frequently Asked Questions

**How much does this cost per month?**
The server costs $6/month. AI model usage is separate (typically $0.50-5/month for personal use depending on how much you talk to it). Total: roughly $6-11/month.

**Can I use a different VPS provider?**
Yes. The same steps work on [Linode](https://linode.com), [Hetzner](https://hetzner.com) (as cheap as $4/month), or [Vultr](https://vultr.com). Just get a Ubuntu 24.04 server with SSH access.

**Do I need to know how to code?**
No. Every command in this guide is copy-paste. You don't need to write a single line of code.

**What if I break something?**
You can destroy your Droplet and start over in 2 minutes. Everything is disposable until you put production data on it. Just delete the Droplet and create a new one.

**Can I run multiple agents on one VPS?**
It depends on your workload. A single agent doing occasional tasks uses very little resources. If you're running several agents that constantly browse the web, write files, and run code, you may want to upgrade to a larger plan. Start with one agent and scale up when you need to.

**Do I need to keep my laptop running?**
No. Your agent lives on the VPS, not your laptop. You can shut down your computer and your agent keeps working.

## What This Unlocks

An always-on AI agent changes what's possible:

- **Daily monitoring** - your agent checks feeds every morning, summarizes what's new, and delivers the highlights to your phone
- **Persistent projects** - research, writing, and data collection that doesn't reset when you close your laptop
- **Multiple agents** - one for lead generation, one for market research, one for content creation - all running in parallel
- **Income potential** - automated content curation, agent-powered services, and eventually paid agent products you can sell

**Start here.** [Sign up for DigitalOcean](https://m.do.co/c/940ca4b955e8), install Hermes Agent, and connect it to Telegram. Spend less than 30 minutes following this guide, and you'll have your own always-on AI agent ready to start building with.

---

*This tutorial uses affiliate links. If you sign up for DigitalOcean through my link, I earn credit at no extra cost to you.*
