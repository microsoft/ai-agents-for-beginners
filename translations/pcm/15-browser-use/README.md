# Building Computer Use Agents (CUA)

Computer use agents fit interact wit websites like persin dem: by opening browser, checking di page, an dey take di next best action from wetin dem see. For dis lesson, you go build browser automation agent wey go search Airbnb, extract structured listing data, an sabi di cheapest place to stay for Stockholm.

Di lesson join Browser-Use for AI-driven navigation, Playwright an Chrome DevTools Protocol (CDP) for browser control, Azure OpenAI for vision-enabled reasoning, an Pydantic for structured extraction.

## Introduction

Dis lesson go cover:

- Understanding wen computer use agents better pass API-only automation
- Combining Browser-Use wit Playwright an CDP for correct browser lifecycle management
- Using Azure OpenAI vision an structured Pydantic output to extract listing data from dynamic web pages
- Deciding wen to use agent-first, actor-first, or hybrid browser automation workflow

## Learning Goals

After you finish dis lesson, you go sabi how to:

- Configure Browser-Use wit Azure OpenAI an Playwright
- Build browser automation workflow wey go navigate real website and handle dynamic UI elements
- Extract typed results from visible page content an turn dem into downstream business logic
- Choose between agent an actor patterns based on how predictable di browser task be

## Code Sample

Dis lesson get one notebook tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Launch Chrome session over CDP, search Airbnb for Stockholm listings, extract prices wit Browser-Use vision, an return di cheapest option as structured data.

## Prerequisites

- Python 3.12+
- Azure OpenAI deployment configured for your environment
- Chrome or Chromium installed for your computer
- Playwright dependencies installed
- Basic knowledge of async Python

## Setup

Install di packages wey di notebook dey use:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Set Azure OpenAI environment variables wey di notebook dey use:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Optional: e dey use di latest API version if you no put anything
AZURE_OPENAI_API_VERSION=...
```

## Architecture Overview

Di notebook show one hybrid browser automation workflow:

1. Chrome start wit CDP enabled so both Playwright an Browser-Use fit share di same browser session.
2. One Browser-Use agent handle open-ended navigation tasks like opening Airbnb, dismiss pop-ups, an search for Stockholm.
3. Di active page get structured Pydantic schema wey dey extract listing titles, nightly prices, ratings, an URLs.
4. Python logic dey compare di extracted listings an highlight di cheapest result.

Dis approach keep di flexible, vision-based reasoning wey Browser-Use good for, and e still dey give you deterministic browser control wen you need am.

## Key Takeaways and Best Practices

### When to Use Agent vs Actor

| Scenario | Use Agent | Use Actor |
|----------|-----------|-----------|
| Dynamic layouts | Yes, AI fit adapt to page changes | No, brittle selectors fit break |
| Known structure | No, agent dey slower than direct control | Yes, fast an precise |
| Finding elements | Yes, natural language work well | No, exact selectors na wetin e need |
| Timing control | No, e no dey predictable | Yes, full control over waits an retries |
| Complex workflows | Yes, fit handle unexpected UI states | No, e need explicit branching |

### Browser-Use Best Practices

1. Start wit agent for exploration an dynamic navigation.
2. Switch to direct page control wen interaction dey predictable.
3. Use structured output models so extracted data go validate an make sense.
4. Add delays wey dey strategic after actions wey trigger visible UI changes.
5. Dey capture screenshots while you dey iterate so failure go dey easier to debug.
6. Expect say websites go change an design fallback strategies for pop-ups an layout shifts.
7. Mix agent an actor patterns to get both flexibility an precision.

### Safety Guardrails for Browser Agents

Browser agents dey work on live websites, so dem need tight boundaries pass script wey dey only call known API. Before you move from notebook demo go real workflow, define di controls around wetin di agent fit see, click, an submit.

1. **Scope the browsing environment.** Run di agent for dedicated browser profile or sandbox, and limit am to di domains wey di task need.
2. **Separate observation from action.** Make di agent search, read, an extract data first; make e require explicit approval before e submit forms, send messages, book travel, make purchases, delete records, or change account settings.
3. **Keep secrets out of prompts and traces.** No put passwords, payment details, session cookies, or raw personal data inside di model context. Make di user take over for authentication an redact sensitive fields from logs.
4. **Treat page content as untrusted input.** One website fit get instructions wey dem mean for di agent, no di user. Di agent suppose ignore page text wey tell am to change e goal, show data, disable safeguards, or visit unrelated sites.
5. **Use deterministic checks around risky steps.** Check di current URL, page title, selected item, price, recipient, an action summary wit code before you ask di user to approve di final step.
6. **Set budgets and stop conditions.** Limit di number of actions, retries, tabs, an minutes di agent fit use. Stop wen page state no clear instead of continuing to click.
7. **Record useful evidence, not everything.** Keep action summaries, timestamps, URLs, selected element descriptions, an screenshot references so failure fit review without storing unnecessary sensitive page content.

For di Airbnb sample, di safe default na to search listings an extract prices. Signing in, contacting host, or complete booking suppose be separate user-approved action.

### Real-World Applications

- Travel booking an price monitoring
- E-commerce price comparison an availability checks
- Structured extraction from dynamic websites
- Vision-aware UI testing an verification
- Website monitoring an alerting
- Intelligent form filling across multi-step flows

## Real-World Example: Microsoft Project Opal

Di agent wey you build for dis lesson na small, local version of **computer use agent (CUA)** — program wey dey drive browser like persin. Microsoft dey bring dis same idea go enterprise wit **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, capability wey dey Microsoft 365 Copilot.

Wit Project Opal, you go describe di task an di agent go work for your behalf using **computer use on secure Windows 365 Cloud PC**, and e dey operate across your organization browser-based apps, sites, an data. E dey **asynchronously for background**, an you fit guide di work or take control anytime. Example jobs na:

- Managing security group membership requests
- Collecting an validating audit evidence for compliance reviews
- Triaging IT incidents (updating ticket status, assigning owners, closing duplicates)
- Compiling Excel data into financial close deck

Opal na better example for how **production-grade, trustworthy** computer use agent suppose be — an e improve concepts from earlier lessons:

| Concept for dis course | How Project Opal use am |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lesson 06) | Opal dey pause for login credentials, sensitive data, or instructions wey poku, and e no dey enter passwords or submit forms without clear confirmation. You fit *Take Control* or *Return Control* in di middle of task. |
| **Trustworthy & secure agents** (Lessons 06 & 18) | E dey run for isolated Windows 365 Cloud PC, browser-only by default (other computer access block via Intune), e dey use *your* identity so e access only wetin you authorized, an e dey log every action for auditability. |
| **Planning & metacognition** (Lessons 07 & 09) | Opal dey generate plan for job first, then e dey supervise e own reasoning every step an e go pause if e notice suspicious activity. |
| **Reusable capabilities / tools** (Lesson 04) | **Skills** dey allow you write instructions for repeatable jobs (import from `.md` file or author wit Opal) an reuse dem across conversations. |

> **Availability:** Project Opal dey available to users for [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) wit Microsoft 365 Copilot subscription, and your admin must complete setup. Because na experimental Frontier feature, capabilities fit change over time.

## Knowledge Check

Test your understanding before you move go di next lesson.

**1. Wen be browser-based computer use agent better pass API-only workflow?**

<details>
<summary>Answer</summary>

Use browser agent wen di task depend on wetin dey visible for web UI, di site no get di API wey e need, or di page dey change frequently so fixed API or selector logic go break. If stable API dey for same task, better use API because e faster, easier to test, an easier to secure.
</details>

**2. For hybrid workflow, which parts make agent handle an which parts make direct Playwright code handle?**

<details>
<summary>Answer</summary>

Make agent handle open-ended navigation an dynamic UI states, like finding correct page or dismiss unexpected pop-ups. Switch to direct Playwright control wen page structure dey known an action need precision, retries, waits, or deterministic validation.
</details>

**3. Di Airbnb sample find listing wey user fit want book. Wetin suppose happen before workflow sign in, contact host, or complete booking?**

<details>
<summary>Answer</summary>

Workflow suppose pause an ask for explicit user approval. Before e ask, e suppose show clear summary of selected listing, current URL, price, dates, an intended action. Searching an extracting prices fit be autonomous; account access, messages, purchases, an bookings suppose be user-approved.
</details>

**4. One web page tell di agent to ignore e original instructions, visit another site, an reveal saved credentials. How agent suppose treat that text?**

<details>
<summary>Answer</summary>

Treat am like untrusted page content, no like developer or user instruction. Agent suppose stay inside allowed domain an task scope, refuse to reveal secrets, an no follow page text wey make am change goal, disable safeguards, or send am to unrelated sites.
</details>

**5. Wetin evidence make sense to keep wen browser agent dey run, an wetin suppose avoid?**

<details>
<summary>Answer</summary>

Keep action summaries, timestamps, URLs, selected element descriptions, validation results, an screenshot references so run fit review. Avoid storing passwords, payment details, session cookies, raw personal data, or full page content unless specific retention an privacy reason dey.
</details>

## Additional Resources

- [Get started with Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
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