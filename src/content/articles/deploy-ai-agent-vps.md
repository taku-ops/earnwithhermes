---
title: "How to Deploy Hermes Agent on a Budget VPS (Beginner's Guide)"
date: 2026-05-09T00:00:00Z
draft: false
description: "Want to deploy your own Hermes Agent on a VPS with Telegram integration? This step-by-step guide walks you through it - no server experience needed."
tags: ["tutorial", "hermes-agent", "vps", "digitalocean", "telegram", "self-hosting", "beginner tutorial", "AI agent deployment", "cloud server", "DevOps"]
categories: ["tutorials"]
canonicalURL: "https://earnwithhermes.com/learn/deploy-ai-agent-vps/"
---

## Before You Start

This guide is for **absolute beginners**. No server experience needed. Here's what you need:

- **A computer** (Mac, Windows, or Linux)
- **Telegram** on your phone or computer (free, takes 2 minutes)
- **A VPS provider account** (the guide covers this)
- **15 minutes**

> **Total cost to deploy:** roughly $6/month for the server, plus small AI usage fees depending on use (typically a few dollars per month).

---

## What Is Hermes Agent?

[Hermes Agent](https://hermes-agent.nousresearch.com) is an open-source AI agent that can browse the web, run code, write files, search your notes, and use tools on its own. You give it tasks and it works through them.

It runs in your terminal or as a Telegram bot, connects to any major AI model (OpenRouter, DeepSeek, Anthropic, etc.), and is designed to be self-hosted. Open source, no per-seat subscription, no vendor lock-in, full control over the setup.

## What Is a VPS and Why Do You Need One?

A **VPS** (Virtual Private Server) is a computer that lives in a data center and stays on 24/7. It never goes to sleep, and you access it over the internet.

Three reasons to put your AI agent on a VPS instead of your laptop:

1. **Persistence** - your agent runs 24/7 even when you log out.
2. **Phone-native** - talk to it from Telegram on your phone. No terminal needed.
3. **Elastic** - one agent today, ten next week. A VPS doesn't care.

A budget VPS gives you room to run multiple agents, a database, or a web dashboard without upgrading.

## Step 1: Get a Cloud Server (VPS)

### What Is DigitalOcean?

DigitalOcean rents small virtual servers called **Droplets** starting at a few dollars per month.

**[👉 Sign up for DigitalOcean here](https://m.do.co/c/940ca4b955e8).**

Once you're signed in:

1. Click **Create → Droplets** (big green button)
2. Under **Choose Region**, pick a data center close to you
3. Under **Choose an image**, select **Ubuntu 24.04 LTS** (Long Term Support - security updates for years)
4. Under **Choose size**, pick the **$6/month** plan (1 GB RAM / 1 CPU - enough for Hermes Agent plus room to grow)
5. Under **Add SSH Key** - keep reading, the next section explains this
6. Click **Create Droplet**

> **Pro tip:** Skip the add-ons (backups, monitoring, etc.) for now. You can add them later. The base plan is plenty.

### About SSH Keys

When you create your server, you need a way to prove you're the owner. An **SSH key** is like a digital key that unlocks your server.

**On Mac or Linux:** Open **Terminal** and type:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Hit **Enter** three times. Then show your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the output (starts with `ssh-ed25519`). Paste this into the DigitalOcean "Add SSH Key" section.

**On Windows:** Use [PuTTYgen](https://www.puttygen.com/) or install [Git Bash](https://git-scm.com/downloads) and follow the Mac instructions above.

> **No SSH key yet?** No worries. Most people don't on their first try. The commands above create one. If you get stuck, DigitalOcean has [a visual guide here](https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/).

### Connect to Your Server

Once your Droplet is created, DigitalOcean gives you an **IP address** (looks like `192.0.2.123`). Copy it.

Open **Terminal** (Mac/Linux) or **Command Prompt / PowerShell** (Windows) and type:

```bash
ssh root@YOUR_DROPLET_IP
```

Replace `YOUR_DROPLET_IP` with the actual IP. So if your IP is `192.0.2.123`:

```bash
ssh root@192.0.2.123
```

If it asks "Are you sure you want to continue connecting?" type **yes** and hit Enter.

You should see a welcome message. You're inside your server. The rest of the commands in this guide go in this same terminal window.

> **⚠️ Common problem:** If you get "Permission denied" or "Connection refused":
> - Make sure you added your SSH key when creating the Droplet
> - Wait 30 seconds and try again - the server takes a moment to boot
> - Double-check you copied the IP address correctly

## Step 2: Install the AI Agent Software

Now that you're connected to your server, install Hermes Agent:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

**What this does:** Downloads the installation script and runs it. The installer detects Linux, downloads everything needed, and sets up the `hermes` command.

After it finishes, reload your terminal:

```bash
source ~/.bashrc
```

Then verify:

```bash
hermes --version
```

You should see something like `v0.x.x`. If you see a version number, the installation worked. The whole thing takes about 30 seconds.

> **⚠️ Common problem:** If `hermes --version` says "command not found":
> - Make sure you ran `source ~/.bashrc` after the install
> - Try logging out (`exit`) and SSH back in

## Step 3: Choose and Configure an AI Model

Hermes Agent needs an **AI model** to do its thinking. The model decides which tools to use and how to answer you.

### Where to Get an API Key

An **API key** is like a password that links your agent to the AI provider's servers.

| Provider | Best For | Sign Up | Typical Monthly Cost |
|----------|----------|---------|---------------------|
| **[OpenRouter](https://openrouter.ai)** | Beginners - one key, 100+ models | Sign up, add $5 credit | $1-5 for light use |
| **[DeepSeek](https://platform.deepseek.com)** | Cheapest option, good for agents | Sign up, add credit | <$1 for light use |
| **[Anthropic](https://console.anthropic.com)** | Strong reasoning | Sign up, use free trial | Generous free credit included |

> **Tip:** Start with **OpenRouter**. Put in $5 and you'll have months of use. You can switch providers anytime.

> **Important:** API keys are usually shown **only once** when you create them. Copy it immediately and store it somewhere safe. If you lose it, you'll need to generate a new one.

### Configure the AI Provider

```bash
hermes setup model
```

The setup wizard walks you through:

1. **Pick a provider** - I recommend **OpenRouter** to start
2. **Enter your API key** - paste the key from the step above
3. **Select a default model** - pick a fast, cheap model like `deepseek-v4-flash`

### How Much Does AI Usage Cost?

There's no fixed monthly fee. You pay based on **how much you use your agent** and **which model** you choose. A quick chat costs fractions of a cent. Heavy daily use with a powerful model might run $5-10/month. The $5 OpenRouter credit will last most beginners months.

### Test Your Agent

Once configured:

```bash
hermes
```

You're now talking to an autonomous AI agent running on a cloud server, accessible from anywhere. Type "Hello, what can you do?" and watch it respond.

Type `/exit` to quit (your agent stays installed on the server).

## Step 4: Connect Your Agent to Telegram

Your agent lives on the server, but you talk to it from your phone. It's like texting an assistant.

### Create a Telegram Bot

1. Open Telegram
2. Search for **@BotFather** (Telegram's official bot-creation tool, verified with a blue checkmark)
3. Send `/newbot`
4. BotFather asks for a **name** - what shows in your chat (e.g., "My AI Assistant")
5. Then a **username** - must end in "bot" (e.g., `my_ai_helper_bot`)
6. BotFather replies with a **bot token** - a long string of letters and numbers

> **What is a bot token?** It's a password for your bot. It lets Hermes Agent post messages in your Telegram chat. **Never share this token.**

### Link the Bot to Your Agent

Back in your server terminal:

```bash
hermes gateway setup
```

When it asks for your **bot token**, paste the one BotFather gave you. That's it.

Now open Telegram and find your bot. Send `/start`. Your agent responds instantly from the VPS, not from your laptop.

**Test it:** Log out of your server (type `exit`). Wait 30 seconds. Send your bot another message from Telegram. It still works.

> Your agent stays online even when you're not at your computer.

## Step 5: Run Your First Real Task

You have an always-on AI agent in your pocket. Try asking it:

> "Search Hacker News for the latest AI agent tools. Summarize the top 3 and save them to a markdown file."

Your agent will:
┃ 1. Browse the web and search Hacker News
┃ 2. Read several articles
┃ 3. Write a summary markdown file on the server
┃ 4. Send you a formatted reply on Telegram with what it found

All while you do something else. Your agent doesn't need your attention to work.

## Frequently Asked Questions

**How much does this cost per month?**
The server costs $6/month. AI model usage is separate (typically $0.50-5/month for personal use). Total: roughly $6-11/month.

**Can I use a different VPS provider?**
Yes. The same steps work on [Linode](https://linode.com), [Hetzner](https://hetzner.com) (as cheap as $4/month), or [Vultr](https://vultr.com). Get a Ubuntu 24.04 server with SSH access.

**Do I need to know how to code?**
No. Every command here is copy-paste.

**What if I break something?**
You can destroy your Droplet and start over in 2 minutes. Everything is disposable until you put production data on it.

**Can I run multiple agents on one VPS?**
It depends on your workload. A single agent doing occasional tasks uses very little. If you run several agents constantly browsing, writing files, and running code, you may want to upgrade. Start with one and scale up when needed.

**Do I need to keep my laptop running?**
No. Your agent lives on the VPS. Shut down your computer and it keeps working.

## What This Unlocks

An always-on AI agent changes what's possible:

- **Daily monitoring** - your agent checks feeds every morning and delivers highlights to your phone
- **Persistent projects** - research, writing, data collection that doesn't reset when you close your laptop
- **Multiple agents** - one for lead generation, one for market research, and one for content creation, all running in parallel
- **Income potential** - automated content curation, agent-powered services, and eventually paid agent products

**Start here.** [Sign up for DigitalOcean](https://m.do.co/c/940ca4b955e8), install Hermes Agent, connect it to Telegram. Spend less than 30 minutes on this guide, and you'll have your own always-on AI agent.

---

*This tutorial uses affiliate links. If you sign up for DigitalOcean through my link, I earn credit at no extra cost to you.*
