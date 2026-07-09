# How to Build Computer Use Agents (CUA)

Computer use agents fit dey interact with websites just like person: e go open browser, check page well well, then do the next beta thing based on wetin e see. For dis lesson, you go build browser automation agent wey go search Airbnb, pull structured listing data, and find the cheapest place to stay for Stockholm.

Dis lesson combine Browser-Use for AI-driven navigation, Playwright and Chrome DevTools Protocol (CDP) to control browser, Azure OpenAI wey get vision for better reasoning, plus Pydantic for structured data extraction.

## Introduction

Dis lesson go cover:

- When computer use agents better pass API-only automation
- How to combine Browser-Use with Playwright and CDP for solid browser lifecycle management
- How to use Azure OpenAI vision plus structured Pydantic output to extract listing data from dynamic web pages
- When to choose agent-first, actor-first, or hybrid browser automation workflow

## Learning Goals

After you finish dis lesson, you go sabi how to:

- Set up Browser-Use with Azure OpenAI and Playwright
- Build browser automation wey go navigate real website plus handle dynamic UI elements
- Extract typed results from wetin dey visible for page and turn am to downstream business logic
- Decide when to use agent vs actor pattern based on how predictable di browser task be

## Code Sample

Dis lesson get one notebook tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): E dey launch Chrome session over CDP, e dey search Airbnb for Stockholm listings, e dey extract prices with Browser-Use vision, and e return the cheapest option as structured data.

## Prerequisites

- Python 3.12+
- Azure OpenAI deployment wey you don configure for your environment
- Chrome or Chromium wey you don install for your machine
- Playwright dependencies wey you don install
- Basic knowledge of async Python

## Setup

Install di packages wey dis notebook go use:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Set di Azure OpenAI environment variables wey dis notebook go use:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Optional: e go use di latest API version if you no put anything
AZURE_OPENAI_API_VERSION=...
```

## Architecture Overview

Dis notebook dey show hybrid browser automation workflow:

1. Chrome go start with CDP enabled so Playwright and Browser-Use fit share the same browser session.
2. Browser-Use agent go handle open-ended navigation tasks like opening Airbnb, dismissing pop-ups, and searching Stockholm.
3. E go inspect di active page with structured Pydantic schema to extract listing titles, nightly prices, ratings, and URLs.
4. Python logic go compare di extracted listings and highlight di cheapest one.

Dis method dey keep di flexible, vision-based reasoning wey Browser-Use dey good at, plus e still dey give you deterministic browser control wen you need am.

## Key Takeaways and Best Practices

### When to Use Agent vs Actor

| Scenario | Use Agent | Use Actor |
|----------|-----------|-----------|
| Dynamic layouts | Yes, AI fit adapt as page dey change | No, brittle selectors fit break |
| Known structure | No, agent go slow pass direct control | Yes, e fast and precise |
| Finding elements | Yes, natural language dey work well | No, you need exact selectors |
| Timing control | No, e less predictable | Yes, you get full control over waits and retries |
| Complex workflows | Yes, e fit handle unexpected UI states | No, e need explicit branching |

### Browser-Use Best Practices

1. Start with agent for exploration and dynamic navigation.
2. Switch to direct page control wen the interaction don become predictable.
3. Use structured output models make sure extracted data valid and type-safe.
4. Add delays well for actions wey dey trigger visible UI changes.
5. Capture screenshots as you dey iterate to make debugging easy.
6. Expect websites to change and design fallback plans for pop-ups and layout shifts.
7. Mix agent and actor patterns to get both flexibility and precision.

### Real-World Applications

- Travel booking and price monitoring
- E-commerce price comparison and availability checks
- Structured extraction from dynamic websites
- Vision-aware UI testing and verification
- Website monitoring and alerting
- Intelligent form filling across multi-step flows

## Real-World Example: Microsoft Project Opal

The agent wey you go build for dis lesson na small, local version of **computer use agent (CUA)** — na program wey dey run browser like person. Microsoft don bring dis same idea enter enterprise with **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, wey be capability for Microsoft 365 Copilot.

With Project Opal, you go just describe di task, agent go work on your behalf using **computer use on secure Windows 365 Cloud PC**, e dey operate for your organization browser-based apps, sites, and data. E dey work **asynchronously for background**, and you fit guide work or take control anytime. Example jobs include:

- Managing security group membership requests
- Collecting and validating audit evidence for compliance reviews
- Triaging IT incidents (updating ticket status, assigning owners, closing duplicates)
- Compiling Excel data into financial close deck

Opal na better example of **production-grade, trustworthy** computer use agent — and e also dey reinforce concepts from earlier lessons:

| Concept for dis course | How Project Opal take apply am |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lesson 06) | Opal dey pause for login details, sensitive data, or ambiguous instructions, and e no dey enter passwords or submit forms without clear confirmation. You fit *Take Control* and *Return Control* anytime during task. |
| **Trustworthy & secure agents** (Lessons 06 & 18) | E dey run inside isolated Windows 365 Cloud PC, e dey browser-only by default (other computer access blocked, enforced with Intune), e dey use *your* identity to access only wetin you authorized, and e go log every action for audit. |
| **Planning & metacognition** (Lessons 07 & 09) | Opal go first generate plan for di job, then e go supervise e own reasoning for every step and pause if e find anything suspicious. |
| **Reusable capabilities / tools** (Lesson 04) | **Skills** dey let you write instructions for repeatable jobs (wey you fit import from `.md` file or create with Opal) and use dem again for different conversations. |

> **Availability:** Project Opal dey currently available for users wey dey [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) with Microsoft 365 Copilot subscription, and your admin must do setup. Because na experimental Frontier feature, capabilities fit change over time.

## Additional Resources

- [Get started with Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integration template](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actor parameters and content extraction](https://docs.browser-use.com/customize/actor/all-parameters)
- [Course Setup](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->