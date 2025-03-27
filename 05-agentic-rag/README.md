[![Agentic RAG](./images/lesson-5-thumbnail.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Click the image above to view video of this lesson)_

# Agentic RAG

This lesson provides a comprehensive overview of Agentic Retrieval-Augmented Generation (Agentic RAG), an emerging AI paradigm where large language models (LLMs) autonomously plan their next steps while pulling information from external sources. Unlike static retrieval-then-read patterns, Agentic RAG involves iterative calls to the LLM, interspersed with tool or function calls and structured outputs. The system evaluates results, refines queries, invokes additional tools if needed, and continues this cycle until a satisfactory solution is achieved.

## Introduction

This lesson will cover

- **Understand Agentic RAG:**  Learn about the emerging paradigm in AI where large language models (LLMs) autonomously plan their next steps while pulling information from external data sources.
- **Grasp Iterative Maker-Checker Style:** Comprehend the loop of iterative calls to the LLM, interspersed with tool or function calls and structured outputs, designed to improve correctness and handle malformed queries.
- **Explore Practical Applications:** Identify scenarios where Agentic RAG shines, such as correctness-first environments, complex database interactions, and extended workflows.

## Learning Goals

After completing this lesson, you will know how to/understand:

- **Understanding Agentic RAG:** Learn about the emerging paradigm in AI where large language models (LLMs) autonomously plan their next steps while pulling information from external data sources.
- **Iterative Maker-Checker Style:** Grasp the concept of a loop of iterative calls to the LLM, interspersed with tool or function calls and structured outputs, designed to improve correctness and handle malformed queries.
- **Owning the Reasoning Process:** Comprehend the system's ability to own its reasoning process, making decisions on how to approach problems without relying on pre-defined paths.
- **Workflow:** Understand how an agentic model independently decides to retrieve market trend reports, identify competitor data, correlate internal sales metrics, synthesize findings, and evaluate the strategy.
- **Iterative Loops, Tool Integration, and Memory:** Learn about the system's reliance on a looped interaction pattern, maintaining state and memory across steps to avoid repetitive loops and make informed decisions.
- **Handling Failure Modes and Self-Correction:** Explore the system's robust self-correction mechanisms, including iterating and re-querying, using diagnostic tools, and falling back on human oversight.
- **Boundaries of Agency:** Understand the limitations of Agentic RAG, focusing on domain-specific autonomy, infrastructure dependence, and respect for guardrails.
- **Practical Use Cases and Value:** Identify scenarios where Agentic RAG shines, such as correctness-first environments, complex database interactions, and extended workflows.
- **Governance, Transparency, and Trust:** Learn about the importance of governance and transparency, including explainable reasoning, bias control, and human oversight.

## What is Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) is an emerging AI paradigm where large language models (LLMs) autonomously plan their next steps while pulling information from external sources. Unlike static retrieval-then-read patterns, Agentic RAG involves iterative calls to the LLM, interspersed with tool or function calls and structured outputs. The system evaluates results, refines queries, invokes additional tools if needed, and continues this cycle until a satisfactory solution is achieved. This iterative “maker-checker” style improves correctness, handles malformed queries, and ensures high-quality results.

The system actively owns its reasoning process, rewriting failed queries, choosing different retrieval methods, and integrating multiple tools—such as vector search in Azure AI Search, SQL databases, or custom APIs—before finalizing its answer. The distinguishing quality of an agentic system is its ability to own its reasoning process. Traditional RAG implementations rely on pre-defined paths, but an agentic system autonomously determines the sequence of steps based on the quality of the information it finds.

## Defining Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) is an emerging paradigm in AI development where LLMs not only pull information from external data sources but also autonomously plan their next steps. Unlike static retrieval-then-read patterns or carefully scripted prompt sequences, Agentic RAG involves a loop of iterative calls to the LLM, interspersed with tool or function calls and structured outputs. At every turn, the system evaluates the results it has obtained, decides whether to refine its queries, invokes additional tools if needed, and continues this cycle until it achieves a satisfactory solution.

This iterative “maker-checker” style of operation is designed to improve correctness, handle malformed queries to structured databases (e.g. NL2SQL), and ensure balanced, high-quality results. Rather than relying solely on carefully engineered prompt chains, the system actively owns its reasoning process. It can rewrite queries that fail, choose different retrieval methods, and integrate multiple tools—such as vector search in Azure AI Search, SQL databases, or custom APIs—before finalizing its answer. This removes the need for overly complex orchestration frameworks. Instead, a relatively simple loop of “LLM call → tool use → LLM call → …” can yield sophisticated and well-grounded outputs.

![Agentic RAG Core Loop](./images/agentic-rag-core-loop.png)

## Owning the Reasoning Process

The distinguishing quality that makes a system “agentic” is its ability to own its reasoning process. Traditional RAG implementations often depend on humans pre-defining a path for the model: a chain-of-thought that outlines what to retrieve and when.
But when a system is truly agentic, it internally decides how to approach the problem. It’s not just executing a script; it’s autonomously determining the sequence of steps based on the quality of the information it finds.
For example, if it’s asked to create a product launch strategy, it doesn’t rely solely on a prompt that spells out the entire research and decision-making workflow. Instead, the agentic model independently decides to:

1. Retrieve current market trend reports using Bing Web Grounding
2. Identify relevant competitor data using Azure AI Search.
3.	Correlate historical internal sales metrics using Azure SQL Database.
4. Synthesize the findings into a cohesive strategy orchestrated via Azure OpenAI Service.
5.	Evaluate the strategy for gaps or inconsistencies, prompting another round of retrieval if necessary.
All of these steps—refining queries, choosing sources, iterating until “happy” with the answer—are decided by the model, not pre-scripted by a human.

## Iterative Loops, Tool Integration, and Memory

![Tool Integration Architecture](./images/tool-integration.png)

An agentic system relies on a looped interaction pattern:

- **Initial Call:** The user’s goal (aka. user prompt) is presented to the LLM.
- **Tool Invocation:** If the model identifies missing information or ambiguous instructions, it selects a tool or retrieval method—like a vector database query (e.g. Azure AI Search Hybrid search over private data) or a structured SQL call—to gather more context.
- **Assessment & Refinement:** After reviewing the returned data, the model decides whether the information suffices. If not, it refines the query, tries a different tool, or adjusts its approach.
- **Repeat Until Satisfied:** This cycle continues until the model determines that it has enough clarity and evidence to deliver a final, well-reasoned response.
- **Memory & State:** Because the system maintains state and memory across steps, it can recall previous attempts and their outcomes, avoiding repetitive loops and making more informed decisions as it proceeds.

Over time, this creates a sense of evolving understanding, enabling the model to navigate complex, multi-step tasks without requiring a human to constantly intervene or reshape the prompt.

## Handling Failure Modes and Self-Correction

Agentic RAG’s autonomy also involves robust self-correction mechanisms. When the system hits dead ends—such as retrieving irrelevant documents or encountering malformed queries—it can:

- **Iterate and Re-Query:** Instead of returning low-value responses, the model attempts new search strategies, rewrites database queries, or looks at alternative data sets.
- **Use Diagnostic Tools:** The system may invoke additional functions designed to help it debug its reasoning steps or confirm the correctness of retrieved data. Tools like Azure AI Tracing will be important to enable robust observability and monitoring.
- **Fallback on Human Oversight:** For high-stakes or repeatedly failing scenarios, the model might flag uncertainty and request human guidance. Once the human provides corrective feedback, the model can incorporate that lesson going forward.

This iterative and dynamic approach allows the model to improve continuously, ensuring that it’s not just a one-shot system but one that learns from its missteps during a given session.

![Self Correction Mechanism](./images/self-correction.png)

## Boundaries of Agency

Despite its autonomy within a task, Agentic RAG is not analogous to Artificial General Intelligence. Its “agentic” capabilities are confined to the tools, data sources, and policies provided by human developers. It can’t invent its own tools or step outside the domain boundaries that have been set. Rather, it excels at dynamically orchestrating the resources at hand.
Key differences from more advanced AI forms include:

1. **Domain-Specific Autonomy:** Agentic RAG systems are focused on achieving user-defined goals within a known domain, employing strategies like query rewriting or tool selection to improve outcomes.
2. **Infrastructure-Dependent:** The system’s capabilities hinge on the tools and data integrated by developers. It can’t surpass these boundaries without human intervention.
3. **Respect for Guardrails:** Ethical guidelines, compliance rules, and business policies remain very important. The agent’s freedom is always constrained by safety measures and oversight mechanisms (hopefully?)

## Practical Use Cases and Value

Agentic RAG shines in scenarios requiring iterative refinement and precision:

1. **Correctness-First Environments:** In compliance checks, regulatory analysis, or legal research, the agentic model can repeatedly verify facts, consult multiple sources, and rewrite queries until it produces a thoroughly vetted answer.
2. **Complex Database Interactions:** When dealing with structured data where queries might often fail or need adjustment, the system can autonomously refine its queries using Azure SQL or Microsoft Fabric OneLake, ensuring the final retrieval aligns with the user’s intent.
3. **Extended Workflows:** Longer-running sessions might evolve as new information surfaces. Agentic RAG can continuously incorporate new data, shifting strategies as it learns more about the problem space.

## Governance, Transparency, and Trust

As these systems become more autonomous in their reasoning, governance and transparency are crucial:

- **Explainable Reasoning:** The model can provide an audit trail of the queries it made, the sources it consulted, and the reasoning steps it took to reach its conclusion. Tools like Azure AI Content Safety and Azure AI Tracing / GenAIOps can help maintain transparency and mitigate risks.
- **Bias Control and Balanced Retrieval:** Developers can tune retrieval strategies to ensure balanced, representative data sources are considered, and regularly audit outputs to detect bias or skewed patterns using custom models for advanced data science organizations using Azure Machine Learning.
- **Human Oversight and Compliance:** For sensitive tasks, human review remains essential. Agentic RAG doesn’t replace human judgment in high-stakes decisions—it augments it by delivering more thoroughly vetted options.

Having tools that provide a clear record of actions is essential. Without them, debugging a multi-step process can be very difficult. See the following example from Literal AI (company behind Chainlit) for an Agent run:

![AgentRunExample](./images/AgentRunExample.png)

![AgentRunExample2](./images/AgentRunExample2.png)

## Conclusion

Agentic RAG represents a natural evolution in how AI systems handle complex, data-intensive tasks. By adopting a looped interaction pattern, autonomously selecting tools, and refining queries until achieving a high-quality result, the system moves beyond static prompt-following into a more adaptive, context-aware decision-maker. While still bounded by human-defined infrastructures and ethical guidelines, these agentic capabilities enable richer, more dynamic, and ultimately more useful AI interactions for both enterprises and end-users.

## Additional Resources

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implement Retrieval Augmented Generation (RAG) with Azure OpenAI Service: Learn how to use your own data with the Azure OpenAI Service. This Microsoft Learn module provides a comprehensive guide on implementing RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluation of generative AI applications with Azure AI Foundry: This article covers the evaluation and comparison of models on publicly available datasets, including Agentic AI applications and RAG architectures</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">What is Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: A Complete Guide to Agent-Based Retrieval Augmented Generation – News from generation RAG</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: turbocharge your RAG with query reformulation and self-query! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Adding Agentic Layers to RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">The Future of Knowledge Assistants: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">How to Build Agentic RAG Systems</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Using Azure AI Foundry Agent Service to scale your AI agents</a>

### Academic Papers

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterative Refinement with Self-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG</a>

## Previous Lesson

[Tool Use Design Pattern](../04-tool-use/README.md)

## Next Lesson

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)
