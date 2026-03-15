# AI Agents wey dey Production: Observability & Evaluation

[![AI Agents wey dey Production](../../../translated_images/pcm/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

As AI agents dey move from experimental prototypes go real-world applications, e dey important to sabi how dem dey behave, monitor how dem dey perform, and evaluate wetin dem produce in systematic way.

## Wetin you go learn

After you finish this lesson, you go sabi/understand:
- Di main koncepts about how to observe and evaluate agents
- Ways to improve performance, costs, and effectiveness of agents
- Wetin and how to evaluate your AI agents systematically
- How to control costs when you dey deploy AI agents for production
- How to instrument agents wey dem build with Microsoft Agent Framework

Di goal na to give you knowledge wey go help turn your "black box" agents to transparent, manageable, and dependable systems.

_**Note:** E important make you deploy AI Agents wey safe and trustworthy. Check out the [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md) lesson too._

## Traces and Spans

Observability tools like [Langfuse](https://langfuse.com/) or [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) dey usually represent agent runs as traces and spans.

- **Trace** dey represent complete agent task from start to finish (like handling user query).
- **Spans** na individual steps inside the trace (like to call language model or fetch data).

![Trace tree for Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Without observability, AI agent fit feel like "black box" — internal state and reasoning no clear, e go hard to diagnose wahala or optimize performance. With observability, agents go turn "glass boxes," wey dey give transparency wey dey important to build trust and make sure dem dey operate as e suppose.

## Why Observability Matters in Production Environments

When you move AI agents go production, new challenges and requirements go show. Observability no be "nice-to-have" again; e become critical:

*   **Debugging and Root-Cause Analysis**: When agent fail or e bring unexpected output, observability tools go give traces wey fit pinpoint di source of di error. Dis one dey especially important for complex agents wey fit involve many LLM calls, tool interactions, and conditional logic.
*   **Latency and Cost Management**: AI agents dey depend on LLMs and other external APIs wey dey bill per token or per call. Observability fit track these calls sharply, help find operations wey slow or too costly. Dis one fit make team optimize prompts, choose more efficient models, or redesign workflow to manage operational costs and give better user experience.
*   **Trust, Safety, and Compliance**: For many apps, e important to make sure agents dey behave safely and ethically. Observability dey give audit trail of agent actions and decisions. You fit use am detect and reduce issues like prompt injection, harmful content, or mishandling of personally identifiable information (PII). For example, you fit review traces to sabi why agent give particular response or why e use specific tool.
*   **Continuous Improvement Loops**: Observability data na foundation for iterative development. By monitoring how agents dey perform for real world, teams fit identify areas to improve, gather data for fine-tuning models, and validate effect of changes. Dis one create feedback loop where production insights from online evaluation dey inform offline experiments and refinement, lead to better agent performance over time.

## Key Metrics to Track

To monitor and understand agent behaviour, you suppose track plenty metrics and signals. Di exact metrics fit change based on wetin agent dey do, but some metrics universal.

Here be some common metrics wey observability tools dey monitor:

**Latency:** How fast agent dey respond? Long wait time dey spoil user experience. You suppose measure latency for tasks and individual steps by tracing agent runs. For example, if agent dey take 20 seconds for all model calls, you fit speed am up by using faster model or by running model calls parallel.

**Costs:** How much e dey cost per agent run? AI agents dey use LLM calls wey dem dey bill per token or external APIs. Frequent tool usage or many prompts fit quickly raise cost. For example, if agent dey call LLM five times for small quality gain, you need check if cost worth am or if you fit reduce calls or use cheaper model. Real-time monitoring fit also help find unexpected spikes (e.g., bugs wey dey cause excessive API loops).

**Request Errors:** How many requests the agent fail? This fit include API errors or failed tool calls. To make agent more robust for production, you fit set up fallbacks or retries. E.g., if LLM provider A down, you go switch to LLM provider B as backup.

**User Feedback:** Direct user evaluations dey give valuable insights. This fit be explicit ratings (👍thumbs-up/👎down, ⭐1-5 stars) or written comments. Consistent negative feedback supposed alert you say agent no dey work as e suppose.

**Implicit User Feedback:** User behavior dey give indirect feedback even without explicit ratings. This fit include quick rephrasing of question, repeated queries, or clicking retry. E.g., if users dey ask same question again and again, na sign say agent no dey work as expected.

**Accuracy:** How often agent produce correct or desirable outputs? Definitions of accuracy fit vary (e.g., problem-solving correctness, information retrieval accuracy, user satisfaction). Di first step na to define wetin success mean for your agent. You fit track accuracy with automated checks, evaluation scores, or task completion labels. For example, mark traces as "succeeded" or "failed".

**Automated Evaluation Metrics:** You fit set up automated evals. For example, use an LLM to score agent output — if e helpful, accurate, or no. Plenty open-source libraries fit help score different aspects of agent. E.g. [RAGAS](https://docs.ragas.io/) for RAG agents or [LLM Guard](https://llm-guard.com/) to detect harmful language or prompt injection.

For real practice, combination of these metrics de give the best view of AI agent health. For this chapter's [example notebook](./code_samples/10-expense_claim-demo.ipynb), we go show how these metrics dey look for real examples but first, we go learn how typical evaluation workflow dey.

## Instrument your Agent

To gather tracing data, you must instrument your code. Di goal na to instrument agent code to emit traces and metrics wey observability platform fit capture, process, and visualize.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) don become industry standard for LLM observability. E provide APIs, SDKs, and tools for generating, collecting, and exporting telemetry data.

Plenty instrumentation libraries dey wey wrap existing agent frameworks and make am easy to export OpenTelemetry spans to observability tool. Microsoft Agent Framework integrate with OpenTelemetry natively. Below na example on instrumenting a MAF agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Di agent wey dey run, na automatic dem dey trace am.
    pass
```

Di [example notebook](./code_samples/10-expense_claim-demo.ipynb) for this chapter go show how to instrument your MAF agent.

**Manual Span Creation:** Even though instrumentation libraries dey give good baseline, sometimes you need more detailed or custom information. You fit manually create spans to add custom application logic. More importantly, you fit enrich automatically or manually created spans with custom attributes (also known as tags or metadata). These attributes fit include business-specific data, intermediate computations, or any context wey fit help debugging or analysis, like `user_id`, `session_id`, or `model_version`.

Example on creating traces and spans manually with the [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent Evaluation

Observability go give us metrics, but evaluation na di process of analyzing that data (and running tests) to determine how well AI agent dey perform and how e fit improve. In other words, when you get traces and metrics, how you go use dem to judge agent and make decisions?

Regular evaluation important because AI agents dey non-deterministic and fit change (through updates or model drift) – without evaluation you no go sabi if your “smart agent” really dey do im work well or if e don regress.

Two categories of evaluation dey for AI agents: **online evaluation** and **offline evaluation**. Both get value and dem dey complement each other. We dey normally start with offline evaluation, because na minimum step before you deploy any agent.

### Offline Evaluation

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dis one involve evaluating agent for controlled setting, normally using test datasets, not live user queries. You dey use curated datasets wey get known expected outputs or correct behavior, then run your agent on top of them.

For example, if you build math word-problem agent, you fit get [test dataset](https://huggingface.co/datasets/gsm8k) of 100 problems wey get known answers. Offline evaluation dey done during development (and fit be part of CI/CD) to check improvements or guard against regressions. Benefit na say e **repeatable and you fit get clear accuracy metrics because you get ground truth**. You fit also simulate user queries and compare agent responses with ideal answers or use automated metrics as we mention above.

Main challenge of offline eval na to make sure your test dataset comprehensive and stay relevant – agent fit perform well on fixed test set but meet different queries for production. So you suppose update test sets with new edge cases and real-world examples. Mix of small “smoke test” cases and larger evaluation sets dey useful: small sets for quick checks and large sets for broader metrics.

### Online Evaluation 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dis one na to evaluate agent for live, real-world environment, i.e. during actual usage in production. Online evaluation dey monitor agent performance on real user interactions and dey analyze outcomes continuously.

For example, you fit track success rates, user satisfaction scores, or other metrics on live traffic. Advantage of online evaluation na say e **capture things wey you no fit anticipate for lab** – you fit see model drift over time (if agent effectiveness dey reduce as input patterns change) and catch unexpected queries or situations wey no dey your test data. E dey give true picture of how agent dey behave for real use.

Online evaluation dey often collect implicit and explicit user feedback, and fit run shadow tests or A/B tests (where new version of agent run parallel to compare with old). Challenge be say e hard to get reliable labels or scores for live interactions – you fit rely on user feedback or downstream metrics (like whether user click the result).

### Combining the two

Online and offline evaluations no dey oppose — dem complement each other. Insights from online monitoring (e.g., new types of queries wey agent perform badly on) fit help improve offline test datasets. On the other hand, agents wey pass offline tests fit deploy for production with more confidence and then monitor online.

Plenty teams use loop:

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_.

## Common Issues

As you deploy AI agents to production, you fit meet different challenges. Here be common issues and possible solutions:

| **Wahala**    | **Wetin fit solve am**   |
| ------------- | ------------------ |
| AI Agent no dey perform tasks consistently | - Refine di prompt wey you dey give the AI Agent; make objectives clear.<br>- Find where dividing the tasks into subtasks and handle dem with multiple agents fit help. |
| AI Agent dey run into continuous loops  | - Make sure termination terms and conditions clear so Agent go sabi when to stop process.<br>- For complex tasks wey need reasoning and planning, use larger model wey specialize for reasoning. |
| AI Agent tool calls no dey perform well   | - Test and validate tool output outside of the agent system.<br>- Refine parameters, prompts, and naming of tools.  |
| Multi-Agent system no dey perform consistently | - Refine prompts wey you give each agent to make dem specific and different from one another.<br>- Build hierarchical system using routing or controller agent to decide which agent correct. |

Plenty of these issues you fit identify better if observability dey place. Traces and metrics wey we talk about go help pinpoint where for agent workflow di problems dey, make debugging and optimization faster.

## Managing Costs
Here are some strategies to manage the costs of deploying AI agents to production:

**Using Smaller Models:** Small Language Models (SLMs) fit perform well for some agentic use-cases and dem go reduce cost plenty. Like we mention before, to build evaluation system wey go check and compare performance with larger models na the best way to sabi how SLM go perform for your use case. Try use SLMs for simpler tasks like intent classification or parameter extraction, and leave larger models for complex reasoning.

**Using a Router Model:** Another strategy na to use different models and sizes. You fit use an LLM/SLM or serverless function to route requests based on how complex dem be to the models wey best fit. This one go help reduce cost and still make sure performance dey for the correct tasks. For example, send simple queries go smaller, faster models, and only use expensive large models for complex reasoning tasks.

**Caching Responses:** To identify common requests and tasks and give di responses before dem even enter your agentic system na good way to reduce di number of similar requests. You fit even build flow wey go check how similar one request be to your cached requests using more basic AI models. Dis strategy fit reduce cost well for frequently asked questions or normal workflows.

## Make we see how dis dey work for practice

In the [example notebook for this section](./code_samples/10-expense_claim-demo.ipynb), we go see examples of how we fit use observability tools to monitor and evaluate our agent.


### You get more questions about AI agents for production?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours and get your AI agents questions answered.

## Previous Lesson

[Metacognition Design Pattern](../09-metacognition/README.md)

## Next Lesson

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate by AI translation service wey dem dey call Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make sure say e correct, abeg note say automated translation fit get mistakes or wrong parts. The original document for im own language na di authoritative source. For important matter, we recommend make professional human translator do di translation. We no go responsible for any misunderstanding or wrong interpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->