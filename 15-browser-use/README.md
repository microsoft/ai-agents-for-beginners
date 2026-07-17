# Building Computer Use Agents (CUA)

Computer use agents can interact with websites the same way a person would: by opening a browser, inspecting the page, and taking the next best action from what they see. In this lesson, you'll build a browser automation agent that searches Airbnb, extracts structured listing data, and identifies the cheapest stay in Stockholm.

The lesson combines Browser-Use for AI-driven navigation, Playwright and Chrome DevTools Protocol (CDP) for browser control, Azure OpenAI for vision-enabled reasoning, and Pydantic for structured extraction.

## Introduction

This lesson will cover:

- Understanding when computer use agents are a better fit than API-only automation
- Combining Browser-Use with Playwright and CDP for reliable browser lifecycle management
- Using Azure OpenAI vision and structured Pydantic output to extract listing data from dynamic web pages
- Deciding when to use an agent-first, actor-first, or hybrid browser automation workflow

## Learning Goals

After completing this lesson, you will know how to:

- Configure Browser-Use with Azure OpenAI and Playwright
- Build a browser automation workflow that navigates a real website and handles dynamic UI elements
- Extract typed results from visible page content and turn them into downstream business logic
- Choose between agent and actor patterns based on how predictable the browser task is

## Code Sample

This lesson includes one notebook tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Launches a Chrome session over CDP, searches Airbnb for Stockholm listings, extracts prices with Browser-Use vision, and returns the cheapest option as structured data.

## Prerequisites

- Python 3.12+
- Azure OpenAI deployment configured in your environment
- Chrome or Chromium installed locally
- Playwright dependencies installed
- Basic familiarity with async Python

## Setup

Install the packages used in the notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Set the Azure OpenAI environment variables used by the notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Optional: defaults to the latest API version when omitted
AZURE_OPENAI_API_VERSION=...
```

## Architecture Overview

The notebook demonstrates a hybrid browser automation workflow:

1. Chrome starts with CDP enabled so both Playwright and Browser-Use can share the same browser session.
2. A Browser-Use agent handles open-ended navigation tasks such as opening Airbnb, dismissing pop-ups, and searching for Stockholm.
3. The active page is inspected with a structured Pydantic schema to extract listing titles, nightly prices, ratings, and URLs.
4. Python logic compares the extracted listings and highlights the cheapest result.

This approach keeps the flexible, vision-based reasoning that Browser-Use is good at while still giving you deterministic browser control when you need it.

## Key Takeaways and Best Practices

### When to Use Agent vs Actor

| Scenario | Use Agent | Use Actor |
|----------|-----------|-----------|
| Dynamic layouts | Yes, AI can adapt to page changes | No, brittle selectors can break |
| Known structure | No, an agent is slower than direct control | Yes, fast and precise |
| Finding elements | Yes, natural language works well | No, exact selectors are required |
| Timing control | No, less predictable | Yes, full control over waits and retries |
| Complex workflows | Yes, handles unexpected UI states | No, requires explicit branching |

### Browser-Use Best Practices

1. Start with an agent for exploration and dynamic navigation.
2. Switch to direct page control when the interaction becomes predictable.
3. Use structured output models so extracted data is validated and type-safe.
4. Add delays strategically after actions that trigger visible UI changes.
5. Capture screenshots while iterating so failures are easier to debug.
6. Expect websites to change and design fallback strategies for pop-ups and layout shifts.
7. Blend agent and actor patterns to get both flexibility and precision.

### Safety Guardrails for Browser Agents

Browser agents operate on live websites, so they need tighter boundaries than a script that only calls a known API. Before moving from a notebook demo to a real workflow, define the controls around what the agent can see, click, and submit.

1. **Scope the browsing environment.** Run the agent in a dedicated browser profile or sandbox, and limit it to the domains required for the task.
2. **Separate observation from action.** Let the agent search, read, and extract data first; require an explicit approval step before it submits forms, sends messages, books travel, makes purchases, deletes records, or changes account settings.
3. **Keep secrets out of prompts and traces.** Do not place passwords, payment details, session cookies, or raw personal data in the model context. Let the user take over for authentication and redact sensitive fields from logs.
4. **Treat page content as untrusted input.** A website can contain instructions that are meant for the agent, not the user. The agent should ignore page text that asks it to change its goal, reveal data, disable safeguards, or visit unrelated sites.
5. **Use deterministic checks around risky steps.** Verify the current URL, page title, selected item, price, recipient, and action summary with code before asking the user to approve the final step.
6. **Set budgets and stop conditions.** Bound the number of actions, retries, tabs, and minutes the agent can use. Stop when the page state is ambiguous instead of continuing to click.
7. **Record useful evidence, not everything.** Keep action summaries, timestamps, URLs, selected element descriptions, and screenshot references so failures can be reviewed without storing unnecessary sensitive page content.

In the Airbnb sample, the safe default is to search listings and extract prices. Signing in, contacting a host, or completing a booking should be a separate user-approved action.

### Real-World Applications

- Travel booking and price monitoring
- E-commerce price comparison and availability checks
- Structured extraction from dynamic websites
- Vision-aware UI testing and verification
- Website monitoring and alerting
- Intelligent form filling across multi-step flows

## Real-World Example: Microsoft Project Opal

The agent you build in this lesson is a small, local version of a **computer use agent (CUA)** — a program that drives a browser the way a person would. Microsoft is bringing this same idea to the enterprise with **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, a capability in Microsoft 365 Copilot.

With Project Opal, you describe a task and the agent works on your behalf using **computer use on a secure Windows 365 Cloud PC**, operating across your organization's browser-based applications, sites, and data. It works **asynchronously in the background**, and you can guide the work or take control at any time. Example jobs include:

- Managing security group membership requests
- Collecting and validating audit evidence for compliance reviews
- Triaging IT incidents (updating ticket status, assigning owners, closing duplicates)
- Compiling Excel data into a financial close deck

Opal is a useful reference for what a **production-grade, trustworthy** computer use agent looks like — and it reinforces concepts from earlier lessons:

| Concept in this course | How Project Opal applies it |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lesson 06) | Opal pauses for login credentials, sensitive data, or ambiguous instructions, and never enters passwords or submits forms without explicit confirmation. You can *Take Control* and *Return Control* mid-task. |
| **Trustworthy & secure agents** (Lessons 06 & 18) | Runs in an isolated Windows 365 Cloud PC, is browser-only by default (other computer access blocked, enforced via Intune), uses *your* identity so it only accesses what you're authorized for, and logs every action for auditability. |
| **Planning & metacognition** (Lessons 07 & 09) | Opal generates a plan for the job first, then supervises its own reasoning at each step and pauses if it detects suspicious activity. |
| **Reusable capabilities / tools** (Lesson 04) | **Skills** let you write instructions for repeatable jobs (imported from a `.md` file or authored with Opal) and reuse them across conversations. |

> **Availability:** Project Opal is currently available to users in the [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) with a Microsoft 365 Copilot subscription, and your administrator must complete setup. Because it's an experimental Frontier feature, capabilities may change over time.

## Additional Resources

- [Get started with Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integration template](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actor parameters and content extraction](https://docs.browser-use.com/customize/actor/all-parameters)
- [Course Setup](../00-course-setup/README.md)

## Previous Lesson

[Exploring Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Next Lesson

[Deploying Scalable Agents](../16-deploying-scalable-agents/README.md)
