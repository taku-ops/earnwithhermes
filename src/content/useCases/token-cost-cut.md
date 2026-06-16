---
title: "90% Token Spend Cut — $130 to $10 per 5 Days"
date: 2026-04-01
draft: false
description: "How switching to Hermes Agent on a cheap Android phone via Termux slashed token costs by 90%, from $130 to just $10 per 5 days, while gaining on-device sensors and SMS capabilities."
tags: ["cost-savings", "android", "termux", "openrouter", "token-optimization", "podcast"]
categories: ["Cost Savings"]
author: "Greg Isenberg"
storySource: "Podcast"
income: "90% less"
---

When Greg Isenberg and Imran Muthuvappa shared how they cut their AI agent costs by 90%, the numbers were straightforward. Hermes Agent on a cheap Android phone via Termux, paired with OpenRouter's model routing. It went from roughly $130 per 5 days to roughly $10 per 5 days. A 10x reduction that makes round-the-clock agent operation possible without a big budget.

> *"Switching to Hermes with OpenRouter cut my token spend ~90% — from ~$130 per 5 days to ~$10 per 5 days. Hermes runs on a cheap Android phone via Termux + Termux API — unlocks SMS, sensors, and on-device social posting. Customization is a trap; output is the skill."*
>
> — **Greg Isenberg & Imran Muthuvappa** on [Startup Ideas Podcast](https://podcasts.apple.com/dk/podcast/hermes-agent-clearly-explained-and-how-to-use-it/id1593424985?i=1000762440356) (2026)

---

### Cost Breakdown

| Before (ChatGPT/Claude Direct) | After (Hermes on Android) |
|-------------------------------|---------------------------|
| $130 per 5 days | **$10 per 5 days** |
| No persistent memory | Full memory system |
| Web-only access | SMS + sensors + social |
| Single model | **Smart routing (any model)** |
| No automation | Cron + skills ecosystem |

### What the Phone Adds

Running Hermes on a cheap Android phone via Termux is not just about cost. The phone itself gives capabilities a cloud server cannot:

- Send and receive SMS messages directly
- On-device camera, microphone, GPS, accelerometer
- Native app integration for social posting
- Phones are built to run 24/7
- Built-in battery backup
- A $50-100 Android phone is plenty

### Customization is a Trap

One takeaway from this story: "Customization is a trap; output is the skill." It is easy to spend time tweaking prompts, adjusting parameters, and perfecting the setup. The real value comes from what the agent produces, not how you configured it.

### Using Termux + Termux API

[Termux](https://termux.dev/) turns Android into a Linux terminal. The Termux API exposes phone capabilities:

```bash
# Send an SMS
termux-sms-send -n "+123****7890" "Hello from Hermes!"

# Get GPS location
termux-location -p

# Take a photo
termux-camera-photo output.jpg

# Make a notification
termux-notification --title "Trade Alert" --content "BTC above $100K"
```

These API calls become Hermes skills, giving the agent real-world sensing and action capabilities.

---

### Setup

1. Get a cheap Android phone running Android 8+, $50-100
2. Install Termux from F-Droid (not Play Store, it is outdated there)
3. Install Termux:API for SMS, sensors, and camera access
4. Install Hermes with standard pip install in Termux
5. Configure OpenRouter with smart routing and cheap models for routine tasks
6. Set up cron jobs to run Hermes on a schedule
7. Create SMS and sensor skills to unlock phone capabilities
8. Monitor costs in the OpenRouter dashboard

Plug the phone in 24/7 in a corner of your home. You now have a $10/month AI agent running indefinitely.
