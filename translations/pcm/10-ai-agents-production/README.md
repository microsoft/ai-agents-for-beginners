# AI Agents for Production: Observability & Evaluation

[![AI Agents for Production](../../../translated_images/pcm/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

As AI agents dey waka from experimental prototypes go real-world applications, the ability to sabi their behavior, dey monitor how dem dey perform, plus dey systematically evaluate their outputs, na important tin.

## Learning Goals

After you finish dis lesson, you go sabi how to/understand:
- Core concepts of agent observability and evaluation
- Techniques to improve the performance, costs, and effectiveness of agents
- Wetin and how to evaluate your AI agents systematically
- How to control costs when you dey deploy AI agents to production
- How to instrument agents wey dem build with Microsoft Agent Framework

The goal be to equip you with the knowledge to change your "black box" agents to transparent, manageable, and dependable systems.

_**Note:** E important say you deploy AI Agents wey safe and trustworthy. Check the [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md) lesson too._

## Traces and Spans

Observability tools like [Langfuse](https://langfuse.com/) or [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) dey usually represent agent runs as traces and spans.

- **Trace** represent complete agent work from beginning to end (like handling user query).
- **Spans** na the individual steps inside the trace (like calling language model or fetching data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Without observability, AI agent fit feel like "black box" - inside part and reasoning dey opaque, e dey hard to diagnose wahala or optimize performance. With observability, agents turn "glass boxes," wey dey give clear transparency wey vital for building trust and sure dem dey work as e suppose. 

## Why Observability Matter for Production Environments

When AI agents enter production environments, e bring new challenges and needs. Observability no be "nice-to-have" again but na critical skill:

*   **Debugging and Root-Cause Analysis**: When agent fail or produce unexpected output, observability tools dey provide traces wey fit pinpoint where error start. Dis important wella for complex agents wey fit dey call multiple LLMs, tools, and conditional logic.
*   **Latency and Cost Management**: AI agents dey rely on LLMs and other APIs wey dem dey charge per token or call. Observability dey allow make you track calls well well, so you fit know which operations dey slow or costly. E help teams optimize prompts, select better models, or reshape workflows to manage cost and give better user experience.
*   **Trust, Safety, and Compliance**: For many apps, e important say agents dey behave safe and ethical. Observability give audit trail for actions and decisions. E fit help detect and stop troubles like prompt injection, harmful content, or mishandling PII. For example, you fit check traces to know why agent give certain response or use particular tool.
*   **Continuous Improvement Loops**: Observability data na the base for iterative development. As you dey monitor how agents dey perform for real life, teams fit identify areas for betterment, collect data for fine-tuning models, and check the effects of changes. E create feedback loop wey production insights from online evaluation dey inform offline experimentation and refinement, wey lead to better agent performance step by step.

## Key Metrics to Track

To monitor and understand agent behavior, you need dey track plenty metrics and signals. Even though metrics fit change by agent purpose, some metrics dey universally important.

Here na some common metrics wey observability tools dey monitor:

**Latency:** How fast agent dey respond? Long wait time dey spoil user experience. You suppose measure latency for tasks and individual steps by tracing agent runs. For example, if agent take 20 seconds for all model calls, e fit faster if you use faster model or run calls in parallel.

**Costs:** How much e dey cost per agent run? AI agents use LLM calls wey dem dey charge per token or API calls. If tools dey use plenty or multiple prompts dey happen, e fit quickly increase cost. For example, if agent dey call LLM five times for small quality improvement, you gas check if e worth the cost or if you fit reduce number of calls or use cheaper model. Real-time monitoring fit also show unexpected cost spikes (like bugs wey dey cause excessive API calls).

**Request Errors:** How many requests agent fail? This fit include API errors or tool calls wey no work. To make agent strong for production, you fit set fallbacks or retries. E.g. if LLM provider A down, switch to LLM provider B as backup.

**User Feedback:** Putting direct user evaluations dey give valuable insights. This fit include explicit ratings (👍thumbs-up/👎down, ⭐1-5 stars) or text comments. Consistent bad feedback suppose alert you as e mean say agent no dey work as e suppose. 

**Implicit User Feedback:** User behavior dey give indirect feedback even without explicit ratings. For example, immediate question rephrasing, repeated queries, or clicking retry button. E.g. if you notice users dey ask same questions again, e mean say agent no dey work as expected.

**Accuracy:** How often agent dey give correct or wanted outputs? Accuracy definitions fit differ (e.g., correctness for problem solving, info retrieval accuracy, or user satisfaction). First step na to define wetin success mean for your agent. You fit track accuracy with automated checks, evaluation scores, or task completion labels. For example, tag traces as "succeeded" or "failed". 

**Automated Evaluation Metrics:** You fit also set automated evals. For example, use LLM to score agent output like if e helpful, accurate, or no. Plenty open source libraries dey help score different agent aspects. E.g. [RAGAS](https://docs.ragas.io/) for RAG agents or [LLM Guard](https://llm-guard.com/) to spot harmful language or prompt injection. 

For practice, combination of these metrics dey give best view of AI agent health. For this chapter’s [example notebook](./code_samples/10-expense_claim-demo.ipynb), we go show how these metrics dey look with real examples but first, we go learn typical evaluation workflow.

## Instrument your Agent

To collect trace data, you need instrument your code. The aim na to instrument agent code to send traces and metrics wey observability platform fit capture, process, and show.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) don become industry standard for LLM observability. E provide sets of APIs, SDKs, and tools for generating, collecting, and exporting telemetry data. 

Plenty instrumentation libraries dey wey fit wrap existing agent frameworks and e easy to export OpenTelemetry spans to observability tools. Microsoft Agent Framework get native OpenTelemetry integration. Below na example to instrument MAF agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent ejecushon dey trace amotomatikaly
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) for this chapter go show how to instrument your MAF agent.

**Manual Span Creation:** Even though instrumentation libraries provide good base, sometimes you go need more detailed or custom info. You fit manually create spans to add custom application logic. More important, you fit add custom attributes (tags or metadata) to automatically or manually created spans. These attributes fit be business-specific data, intermediate calculations, or any context wey dey useful for debugging or analysis, like `user_id`, `session_id`, or `model_version`.

Example of how to create traces and spans manually wit [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent Evaluation

Observability dey give us metrics, but evaluation na the process where you analyze dat data (and do tests) to know how well AI agent dey perform and how e fit improve. In other words, when you get traces and metrics, how you go use am judge agent and make decisions? 

Regular evaluation dey important because AI agents fit no dey deterministic and dem fit change (by updates or drifting model behavior) – if no evaluation, you no go sabi if your “smart agent” really dey do e work well or e dey regress.

Two types evaluation dey for AI agents: **online evaluation** and **offline evaluation**. Both dey important and dem dey complement each other. Normally we start with offline evaluation coz na the minimum step wey you need before you deploy agent.

### Offline Evaluation

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

This one na evaluation wey you do for controlled place, usually with test datasets, no be with live user queries. You dey use curated datasets wey you sabi expected output or correct behavior, then you run your agent on top.

For example, if you build math word problem agent, you fit get [test dataset](https://huggingface.co/datasets/gsm8k) of 100 problems with known answers. Offline evaluation fit happen for development and fit dey part of CI/CD pipelines to check if things improve or if regression no show. The good thing be say e **repeatable and you fit get clear accuracy metrics since you get ground truth**. You fit simulate user queries and compare agent response with best answers or use automated metrics as we talk before. 

The big challenge for offline eval na to make sure your test dataset dey complete and up to date – agent fit do well for fixed test set but e fit meet very different queries inside production. So you suppose dey update test sets with new edge cases and examples wey reflect real-world scenarios. A combination of small “smoke test” cases and larger evaluation sets dey useful: small sets for quick checks and bigger ones for broad performance metrics.

### Online Evaluation 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

This one mean evaluate agent for live real-world environment, i.e. during actual production use. Online evaluation mean monitoring agent performance on real user interactions and continuously analyze results. 

For example, you fit track success rates, user satisfaction, or other metrics on live traffic. Advantage of online evaluation be say e **capture tinz you no fit predict for lab setting** – you fit observe model drift over time (if agent effectiveness drop as input pattern shift) and catch unexpected queries or situations wey no dey your test data. E show true behavior of agent inside real world. 

Online evaluation dey include collecting implicit and explicit user feedback, and fit run shadow tests or A/B tests (where new version of agent run alongside old one to compare). Challenge be say e fit hard to get reliable labels or scores for live interactions – you go rely on user feedback or downstream metrics (like whether user click the result). 

### Combining the two

Online and offline evaluations no dey separate; dem dey work well together. Insights from online monitoring (e.g., new kind user queries where agent no perform well) fit help improve offline test datasets. On the other side, agents wey perform well offline fit confidently deploy and monitor online. 

Many teams dey use loop like this: 

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_.

## Common Issues

When you deploy AI agents for production, you fit see different kind challenges. Here be some common wahalas and how you fit solve am:

| **Issue**    | **Potential Solution**   |
| ------------- | ------------------ |
| AI Agent no dey do tasks steady | - Sharpen the prompt wey you dey give AI Agent; make objectives clear.<br>- See if you fit divide tasks into subtasks wey multiple agents fit handle. |
| AI Agent dey run continuous loops  | - Make sure clear termination terms and conditions dey so Agent sabi when to stop.<br>- For complex tasks wey need reasoning and planning, use bigger model wey specialize for reasoning. |
| AI Agent tool calls no dey perform well   | - Test and validate tool output outside agent system.<br>- Sharpen parameters, prompts, and naming of tools.  |
| Multi-Agent system no dey perform steady | - Sharpen prompts for each agent to make dem specific and different.<br>- Build hierarchical system wey use "routing" or controller agent to choose correct agent. |

Most of these wahala you fit identify well if observability dey. The traces and metrics wey we talk before dey help show exact place wey wahala dey for agent workflow, e make debugging and optimization easy.

## Managing Costs


Dis na some strategies to manage di costs of deploying AI agents to production:

**Using Smaller Models:** Small Language Models (SLMs) fit perform well for some agentic use-cases and e go reduce costs well well. Like we talk before, to build evaluation system wey go fit determine and compare performance against bigger models na di best way to sabi how well SLM go perform for your use case. Try use SLMs for simple tasks like intent classification or parameter extraction, and keep bigger models for wahala wey heavy like complex reasoning.

**Using a Router Model:** Another way be say use different models and sizes. You fit use LLM/SLM or serverless function to route requests base on how complex e be to di best fit models. This one also go help reduce costs and still make sure say performance dey correct for the right tasks. For example, send simple queries go smaller, faster models, and only use expensive big models for where reasoning heavy.

**Caching Responses:** To sabi common requests and tasks and give di responses before dem enter your agentic system na beta way to reduce many requests wey resemble each other. You fit even run flow wey go track how close request be to your cached requests by using simple AI models. This strategy fit reduce costs well for questions wey people ask often or common workflows.

## Make we see how dis one dey work for practice

For di [example notebook of this section](./code_samples/10-expense_claim-demo.ipynb), we go see how we fit use observability tools take monitor and evaluate our agent.


### You Get More Questions about AI Agents for Production?

Join di [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and get answers to your AI Agents questions.

## Previous Lesson

[Metacognition Design Pattern](../09-metacognition/README.md)

## Next Lesson

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->