[![Agentic RAG](../../../translated_images/pcm/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Click di pikin pikshua wey dey up make you see video for dis lesson)_

# Agentic RAG

Dis lesson go give full overview about Agentic Retrieval-Augmented Generation (Agentic RAG), weh be new AI way weh big language models (LLMs) dey plan their next move by themself dem dey find info from outside sources. E no be like static retrieval-then-read wey dey normal; Agentic RAG dey do many calls go LLM, come dey put tool or function calls and dey organize the output. Di system dey check wetin e find, dey improve queries, dey use another tools if e need, come continue dis process till e find better answer.

## Introduction

Dis lesson go cover

- **Understand Agentic RAG:**  Learn about di new style for AI weh big language models (LLMs) dey plan dem next steps on their own while dem dey get info from outside data sources.
- **Grasp Iterative Maker-Checker Style:** Understand di loop weh dey involve many calls to di LLM, put tool or function calls plus organized outputs, wey dey help improve correctness and solve wrong queries.
- **Explore Practical Applications:** See places wey Agentic RAG dey work well, like for correctness-first environments, complex database work, and long workflows.

## Learning Goals

After you finish this lesson, you go sabi how to/ understand:

- **Understanding Agentic RAG:** Learn about di new AI style weh big language models (LLMs) dey plan their next steps on their own while dem dey collect info from outside sources.
- **Iterative Maker-Checker Style:** Understand di loop idea weh involve many calls to di LLM, put tool or function calls and structured outputs, wey dey improve correctness and handle wrong queries.
- **Owning the Reasoning Process:** Understand how di system fit be in control of how e reason through things, e fit decide how e go solve wahala without following tori wey dem plan before.
- **Workflow:** Understand how di agentic model dey decide by itself to find market trend reports, identify competitor data, join internal sales info, put findings together, and check di plan.
- **Iterative Loops, Tool Integration, and Memory:** Learn how di system dey depend on loop interaction, dey keep state and memory across steps to stop repeat Wahala and make correct decisions.
- **Handling Failure Modes and Self-Correction:** Check how di system dey correct itself well, including iterating, re-querying, using diagnostic tools, and support from human oversight.
- **Boundaries of Agency:** Understand di limits of Agentic RAG, including domain-specific freedom, infrastructure dependence, and respecting safety guardrails.
- **Practical Use Cases and Value:** Identify places wey Agentic RAG dey shine, like correctness-first settings, complex database work, and extended workflows.
- **Governance, Transparency, and Trust:** Learn why governance and transparency dey important, including clear reasoning, bias control, and human supervision.

## Wetin be Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) na new AI style weh big language models (LLMs) dey plan their next moves on their own while dem dey gather info from outside sources. E no be like static retrieval-then-read pattern; Agentic RAG dey do many calls to LLM, mix am with tool or function calls plus structured outputs. Di system dey check result, improve queries, call more tools if e need, and continue till e find better solution. Dis iterative “maker-checker” style dey improve correctness, fit handle wrong queries, and make sure result good well well.

Di system dey fully control how e reason, e dey rewrite query wey fail, pick better retrieval ways, and join many tools—like vector search for Azure AI Search, SQL databases, or custom APIs—before e give final answer. The better thing for agentic system be say e fit control e own reasoning. Normal RAG dem dey follow pre-planned path, but agentic system dey decide steps by itself based on quality of info e find.

## Define Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) na new AI way where LLMs no just dey pull info from outside data sources but dem dey plan their next move by themselves. E no be like static retrieval-then-read or one fine script prompt, Agentic RAG dey do loop with many calls to LLM, mix am with tool/function calls plus structured output. Every time, di system dey check di result, decide if e go improve the queries, call more tools if e need, and continue till e get better solution.

Dis iterative “maker-checker” approach na to make results correct, fix bad queries wey go structured databases (like NL2SQL), and make sure result balance and high-quality. No be only rely on fine prompt chains, di system dey control how e reason. E fit rewrite bad queries, choose different retrieval way, and join many tools like vector search for Azure AI Search, SQL databases, or custom APIs before e finalize answer. Dis one mean say no need complex orchestrations; just simple loop of “LLM call → tool use → LLM call → …” go fit get strong and grounded output.

![Agentic RAG Core Loop](../../../translated_images/pcm/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Owning the Reasoning Process

Wetin make system “agentic” na say e fit control how e reason. Normal RAG models dey depend on humans to plan path for model: chain-of-thought wey show wetin to get and when to do am.
But when system really be agentic, e go decide by itself how to solve problem. E no dey follow script; e dey find steps based on info quality wey e find.
For example, if dem ask am to create product launch plan, e no go just depend on prompt wey talk all the research and decision workflow. Instead, di agentic model go decide alone to:

1. Find current market trend reports using Bing Web Grounding
2. Identify relevant competitor data with Azure AI Search.
3.	Join historical internal sales data with Azure SQL Database.
4. Put all findings together into better plan through Azure OpenAI Service.
5.	Check di plan for any gap or wahala, if e find any, e go do another round of data searching.
All these steps — refining queries, choosing sources, try till e happy with answer — na model itself dey decide, no human script.

## Iterative Loops, Tool Integration, and Memory

![Tool Integration Architecture](../../../translated_images/pcm/tool-integration.0f569710b5c17c10.webp)

Agentic system dey use looped interaction pattern:

- **Initial Call:** User goal (user prompt) na im dem give LLM.
- **Tool Invocation:** If model find say info never complete or instructions dey unclea, e go choose tool or retrieval way—like vector database query (e.g. Azure AI Search Hybrid search over private data) or structured SQL call—to get more info.
- **Assessment & Refinement:** After e check data wey return, model go decide if info enough. If no, e go improve query, try another tool, or change plan.
- **Repeat Until Satisfied:** Dis cycle go continue till model sure say e get enough clear info to give final well-reasoned answer.
- **Memory & State:** Because system keep state and memory across steps, e fit remember previous tries and result, no dey enter same loop again, come dey make better decisions as e move.

Overtime, dis one dey give sense say model dey understand better, e fit handle complex multi-step tasks without human to dey always interfere or change prompt.

## Handling Failure Modes and Self-Correction

Agentic RAG own autonomy get strong self-correcting systems too. When e jam dead ends—like finding wrong doc or bad queries—we fit:

- **Iterate and Re-Query:** Instead of dey give low-quality answers, model go try new search ways, rewrite database queries, or check other data sets.
- **Use Diagnostic Tools:** System fit call extra functions wey help debug how e take reason or check if data correct. Tools like Azure AI Tracing dey important to allow good observability and monitoring.
- **Fallback on Human Oversight:** For important or repeated wahala, model fit show say e no sure and beg human help. When human give feedback, model fit learn and improve for future.

Dis iterative and dynamic style dey help model improve steady steady, e no be one-time system; e dey learn from mistakes during one session.

![Self Correction Mechanism](../../../translated_images/pcm/self-correction.da87f3783b7f174b.webp)

## Boundaries of Agency

Despite say e autonomous inside task, Agentic RAG no be Artificial General Intelligence. Di “agentic” powers na limited to tools, data sources, and policies wey human developers give am. E no fit create hin own tools or waka outside domain boundaries wey dem set. Instead, e good at managing resources wey e get inside.
Main differences from advanced AI dem be:

1. **Domain-Specific Autonomy:** Agentic RAG systems dey work to achieve user-set goals inside one known domain, dem dey use ways like query rewriting or tool choice to improve results.
2. **Infrastructure-Dependent:** System powers dey depend on tools and data dem wey developers join. E no fit cross those limits without human help.
3. **Respect for Guardrails:** Ethical rules, compliance, and business policies still very important. Agent freedom always dey controlled by safety and oversight mechanisms (hope so?).

## Practical Use Cases and Value

Agentic RAG dey shine for places wey need repeated editing and accuracy:

1. **Correctness-First Environments:** For compliance checking, regulatory work, or legal research, agentic model fit dey check facts many times, check plenty sources, and rewrite queries till e get fully vetted answer.
2. **Complex Database Interactions:** For structured data wey queries fit fail or need updates, system fit improve queries by itself using Azure SQL or Microsoft Fabric OneLake, sure say final data na wetin user want.
3. **Extended Workflows:** Long sessions fit evolve as new info show. Agentic RAG fit continue add new data, change strategies as e learn more about problem.

## Governance, Transparency, and Trust

As systems become more autonomous inside reasoning, governance and transparency dey important:

- **Explainable Reasoning:** Model fit show audit trail of queries wey e do, sources wey e use, and reasoning steps wey e take to decide. Tools like Azure AI Content Safety and Azure AI Tracing / GenAIOps fit help keep transparency and reduce risk.
- **Bias Control and Balanced Retrieval:** Developers fit adjust retrieval ways to make sure balanced, representative sources dey considered, and dem fit regularly check output for bias using custom models for advanced data science orgs using Azure Machine Learning.
- **Human Oversight and Compliance:** For sensitive work, human review still necessary. Agentic RAG no go replace human judgement for big decisions—e go help make better vetted options.

Get tools wey fit provide clear record of actions dey very important. Without am, e go hard to debug multi-step process. See example from Literal AI (company wey dey behind Chainlit) for Agent run:

![AgentRunExample](../../../translated_images/pcm/AgentRunExample.471a94bc40cbdc0c.webp)

## Conclusion

Agentic RAG na natural way AI systems dey evolve for how dem handle complex, data-heavy tasks. By using looped interaction, picking tools by itself, and improving queries till complete correct result, system dey move past static prompt following to become better, context-aware decision maker. Even though e still limited by human-set infrastructure and ethics, these agentic powers fit give richer, more dynamic and useful AI experience for both companies and end-users.

### You get more questions about Agentic RAG?

Join [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) make you link up with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implement Retrieval Augmented Generation (RAG) with Azure OpenAI Service: Learn how to use your own data with the Azure OpenAI Service. This Microsoft Learn module provides a comprehensive guide on implementing RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluation of generative AI applications with Microsoft Foundry: This article covers the evaluation and comparison of models on publicly available datasets, including Agentic AI applications and RAG architectures</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">What is Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: A Complete Guide to Agent-Based Retrieval Augmented Generation – News from generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: turbocharge your RAG wit query reformulation and self-query! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Adding Agentic Layers to RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Di Future of Knowledge Assistants: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">How to Build Agentic RAG Systems</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Using Microsoft Foundry Agent Service to scale your AI agents</a>

### Academic Papers

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterative Refinement wit Self-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Language Agents wit Verbal Reinforcement Learning</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Large Language Models Fit Self-Correct wit Tool-Interactive Critiquing</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: One Survey on Agentic RAG</a>

## Smoke-Test Dis Agent (Optional)

After you don learn to deploy agents for [Lesson 16](../16-deploying-scalable-agents/README.md), you fit smoke-test dis lesson `TravelRAGAgent` — check say im answers dey grounded for the knowledge base — wit [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). See [`tests/README.md`](../tests/README.md) for how you go run am.

## Previous Lesson

[Tool Use Design Pattern](../04-tool-use/README.md)

## Next Lesson

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->