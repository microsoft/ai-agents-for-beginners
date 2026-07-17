# Di build Computer Use Agents (CUA)

Computer use agents fit interact wit websites like how pesin go do am: opening browser, check di page, den take di next best action based on wetin dem see. For dis lesson, you go build browser automation agent wey dey search Airbnb, carry out structured listing data, and find di cheapest place to stay for Stockholm.

Di lesson join Browser-Use for AI-driven navigation, Playwright and Chrome DevTools Protocol (CDP) for browser control, Azure OpenAI for vision-enabled reasoning, plus Pydantic for structured extraction.

## Introduction

Dis lesson go cover:

- Understanding when computer use agents better pass API-only automation
- Combining Browser-Use wit Playwright and CDP for reliable browser lifecycle management
- Using Azure OpenAI vision and structured Pydantic output to extract listing data from dynamic web pages
- Deciding when to use agent-first, actor-first, or hybrid browser automation workflow

## Learning Goals

After you finish dis lesson, you go sabi how to:

- Configure Browser-Use wit Azure OpenAI and Playwright
- Build browser automation workflow wey navigate real website and handle dynamic UI elements
- Extract typed results from visible page content and turn dem to downstream business logic
- Choose between agent and actor patterns based on how predictable di browser work be

## Code Sample

Dis lesson get one notebook tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): E launch Chrome session over CDP, search Airbnb for Stockholm listings, extract prices wit Browser-Use vision, and return di cheapest option as structured data.

## Prerequisites

- Python 3.12+
- Azure OpenAI deployment wey you don set for your environment
- Chrome or Chromium wey you don install for your local machine
- Playwright dependencies wey you don install
- Basic understanding of async Python

## Setup

Install di packages wey di notebook dey use:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Set the Azure OpenAI environment variables wey di notebook dey use:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Optional: e go use di latest API version if you no put anything
AZURE_OPENAI_API_VERSION=...
```

## Architecture Overview

Di notebook dey show one hybrid browser automation workflow:

1. Chrome begin wit CDP enabled so Playwright and Browser-Use fit share di same browser session.
2. Browser-Use agent dey handle open-ended navigation tasks like opening Airbnb, close pop-ups, and search for Stockholm.
3. Di active page dey inspected wit structured Pydantic schema to extract listing titles, nightly prices, ratings, and URLs.
4. Python logic dey compare di extracted listings and highlight di cheapest result.

Dis method dey keep di flexible, vision-based reasoning wey Browser-Use sabi well, plus e still give you deterministic browser control when you need am.

## Key Takeaways and Best Practices

### When to Use Agent vs Actor

| Scenario | Use Agent | Use Actor |
|----------|-----------|-----------|
| Dynamic layouts | Yes, AI fit adapt to page changes | No, brittle selectors fit break |
| Known structure | No, agent slow pass direct control | Yes, fast and precise |
| Finding elements | Yes, natural language dey work well | No, exact selectors dey required |
| Timing control | No, less predictable | Yes, full control over waits and retries |
| Complex workflows | Yes, fit handle unexpected UI states | No, e need explicit branching |

### Browser-Use Best Practices

1. Start wit agent for exploration and dynamic navigation.
2. Switch go direct page control if di interaction don dey predictable.
3. Use structured output models so extracted data go dey validated and type-safe.
4. Put delays for actions wey dey cause visible UI changes.
5. Capture screenshots while you dey iterate so e go dey easy to debug failures.
6. Expect say websites go dey change and design fallback strategies for pop-ups and layout shifts.
7. Mix agent and actor patterns to get both flexibility and precision.

### Safety Guardrails for Browser Agents

Browser agents dey work for live websites, so dem need tighter boundaries pass script wey dey call known API only. Before you move from notebook demo go real workflow, define di controls about wetin di agent fit see, click, and submit.

1. **Scope di browsing environment.** Make agent run inside dedicated browser profile or sandbox, and limit am to di domains wey task require.
2. **Separate observation from action.** Make agent search, read, and extract data first; require explicit approval bifo e fit submit forms, send messages, book travel, buy tins, delete records, or change account settings.
3. **Keep secrets out of prompts and traces.** No put passwords, payment details, session cookies, or raw personal data for model context. Make user handle authentication and hide sensitive fields from logs.
4. **Treat page content as untrusted input.** Website fit get instructions wey dem mean for agent, no be for user. Agent suppose ignore page text wey tell am to change goal, reveal data, disable safeguards, or visit sites wey no relate.
5. **Use deterministic checks around risky steps.** Verify current URL, page title, selected item, price, recipient, and action summary wit code before you ask user to approve final step.
6. **Set budgets and stop conditions.** Limit number of actions, retries, tabs, and minutes wey di agent fit use. Stop if page state no clear and no continue to click.
7. **Record useful evidence, no everything.** Keep action summaries, timestamps, URLs, selected element descriptions, and screenshots so e go easy to review failures without storing unnecessary sensitive page content.

For di Airbnb sample, di safe default na to search listings and extract prices. To sign in, contact host, or complete booking suppose be separate user-approved action.

### Real-World Applications

- Travel booking and price monitoring
- E-commerce price comparison and availability checks
- Structured extraction from dynamic websites
- Vision-aware UI testing and verification
- Website monitoring and alerting
- Intelligent form filling across multi-step flows

## Real-World Example: Microsoft Project Opal

Di agent wey you build for dis lesson na small, local version of **computer use agent (CUA)** — na program wey dey drive browser like pesin. Microsoft dey bring dis same idea enter enterprise wit **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, na feature for Microsoft 365 Copilot.

Wit Project Opal, you go talk task, and di agent go work on your behalf using **computer use for secure Windows 365 Cloud PC**, e go work across your organization's browser-based apps, sites, and data. E dey work **asynchronously for background**, and you fit guide di work or take control anytime. Example jobs na:

- Managing security group membership requests
- Collecting and validating audit evidence for compliance reviews
- Triaging IT incidents (update ticket status, assign owners, close duplicates)
- Compiling Excel data into financial close deck

Opal na correct example for **production-grade, trustworthy** computer use agent — and e dey reinforce concepts from earlier lessons:

| Concept for dis course | How Project Opal dey apply am |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lesson 06) | Opal go pause for login credentials, sensitive data, or ambiguous instructions, and e no go ever enter passwords or submit forms without clear confirmation. You fit *Take Control* and *Return Control* during task. |
| **Trustworthy & secure agents** (Lessons 06 & 18) | E dey run inside isolated Windows 365 Cloud PC, e browser-only by default (other computer access blocked, enforced by Intune), e dey use *your* identity so e go only access wetin you get permission for, and e go log every action for auditability. |
| **Planning & metacognition** (Lessons 07 & 09) | Opal first go generate plan for job, then e go supervise e own reasoning at each step and pause if e see suspicious activity. |
| **Reusable capabilities / tools** (Lesson 04) | **Skills** dey let you write instructions for repeatable jobs (import from `.md` file or write with Opal) and reuse dem across conversations. |

> **Availability:** Project Opal dey available now for users wey dey [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) wit Microsoft 365 Copilot subscription, and your administrator must complete setup. Because na experimental Frontier feature, capabilities fit change over time.

## Additional Resources

- [Get started wit Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integration template](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actor parameters and content extraction](https://docs.browser-use.com/customize/actor/all-parameters)
- [Course Setup](../00-course-setup/README.md)

## Previous Lesson

[Exploring Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Next Lesson

[Deploying Scalable Agents](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->