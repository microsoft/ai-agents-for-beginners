<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-30T13:05:34+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "en"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.en.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Click the image above to view video of this lesson)_

# Agentic RAG

This lesson provides a detailed overview of Agentic Retrieval-Augmented Generation (Agentic RAG), a new AI approach where large language models (LLMs) independently plan their next steps while gathering information from external sources. Unlike static retrieval-then-read methods, Agentic RAG involves repeated interactions with the LLM, alternating with tool or function calls and structured outputs. The system evaluates results, refines queries, uses additional tools if necessary, and continues this process until a satisfactory solution is reached.

## Introduction

This lesson will cover:

- **Understanding Agentic RAG:** Learn about the new AI paradigm where large language models (LLMs) independently plan their next steps while pulling information from external data sources.
- **Iterative Maker-Checker Style:** Understand the process of repeated interactions with the LLM, alternating with tool or function calls and structured outputs, aimed at improving accuracy and handling problematic queries.
- **Practical Applications:** Discover scenarios where Agentic RAG excels, such as environments prioritizing accuracy, complex database tasks, and extended workflows.

## Learning Goals

After completing this lesson, you will be able to:

- **Understand Agentic RAG:** Learn about the new AI paradigm where large language models (LLMs) independently plan their next steps while pulling information from external data sources.
- **Iterative Maker-Checker Style:** Understand the concept of repeated interactions with the LLM, alternating with tool or function calls and structured outputs, aimed at improving accuracy and handling problematic queries.
- **Own the Reasoning Process:** Grasp how the system takes charge of its reasoning process, deciding how to approach problems without relying on pre-defined paths.
- **Workflow:** Learn how an agentic model independently retrieves market trend reports, identifies competitor data, correlates internal sales metrics, synthesizes findings, and evaluates strategies.
- **Iterative Loops, Tool Integration, and Memory:** Understand the system’s reliance on repeated interactions, maintaining state and memory across steps to avoid redundancy and make informed decisions.
- **Handling Failure Modes and Self-Correction:** Explore the system’s ability to self-correct, including iterating and re-querying, using diagnostic tools, and relying on human oversight when necessary.
- **Boundaries of Agency:** Recognize the limitations of Agentic RAG, focusing on domain-specific autonomy, infrastructure dependence, and adherence to guardrails.
- **Practical Use Cases and Value:** Identify scenarios where Agentic RAG excels, such as environments prioritizing accuracy, complex database tasks, and extended workflows.
- **Governance, Transparency, and Trust:** Learn about the importance of governance and transparency, including explainable reasoning, bias control, and human oversight.

## What is Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) is a new AI approach where large language models (LLMs) independently plan their next steps while gathering information from external sources. Unlike static retrieval-then-read methods, Agentic RAG involves repeated interactions with the LLM, alternating with tool or function calls and structured outputs. The system evaluates results, refines queries, uses additional tools if necessary, and continues this process until a satisfactory solution is reached. This iterative “maker-checker” style improves accuracy, handles problematic queries, and ensures high-quality results.

The system actively takes charge of its reasoning process, rewriting failed queries, choosing different retrieval methods, and integrating multiple tools—such as vector search in Azure AI Search, SQL databases, or custom APIs—before finalizing its answer. What sets an agentic system apart is its ability to own its reasoning process. Traditional RAG implementations rely on pre-defined paths, but an agentic system autonomously determines the sequence of steps based on the quality of the information it finds.

## Defining Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) is a new AI approach where LLMs not only gather information from external data sources but also independently plan their next steps. Unlike static retrieval-then-read methods or carefully scripted prompt sequences, Agentic RAG involves repeated interactions with the LLM, alternating with tool or function calls and structured outputs. At each step, the system evaluates the results it has obtained, decides whether to refine its queries, uses additional tools if necessary, and continues this process until it achieves a satisfactory solution.

This iterative “maker-checker” style of operation is designed to improve accuracy, handle problematic queries to structured databases (e.g., NL2SQL), and ensure balanced, high-quality results. Instead of relying solely on carefully engineered prompt chains, the system actively takes charge of its reasoning process. It can rewrite queries that fail, choose different retrieval methods, and integrate multiple tools—such as vector search in Azure AI Search, SQL databases, or custom APIs—before finalizing its answer. This eliminates the need for overly complex orchestration frameworks. Instead, a relatively simple loop of “LLM call → tool use → LLM call → …” can produce sophisticated and well-grounded outputs.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.en.png)

## Owning the Reasoning Process

What makes a system “agentic” is its ability to take charge of its reasoning process. Traditional RAG implementations often depend on humans pre-defining a path for the model: a chain-of-thought that outlines what to retrieve and when.  
But when a system is truly agentic, it internally decides how to approach the problem. It’s not just following a script; it’s independently determining the sequence of steps based on the quality of the information it finds.  
For example, if it’s asked to create a product launch strategy, it doesn’t rely solely on a prompt that spells out the entire research and decision-making workflow. Instead, the agentic model independently decides to:

1. Retrieve current market trend reports using Bing Web Grounding.
2. Identify relevant competitor data using Azure AI Search.
3. Correlate historical internal sales metrics using Azure SQL Database.
4. Synthesize the findings into a cohesive strategy orchestrated via Azure OpenAI Service.
5. Evaluate the strategy for gaps or inconsistencies, prompting another round of retrieval if necessary.

All of these steps—refining queries, choosing sources, iterating until “happy” with the answer—are decided by the model, not pre-scripted by a human.

## Iterative Loops, Tool Integration, and Memory

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.en.png)

An agentic system relies on repeated interactions:

- **Initial Call:** The user’s goal (i.e., user prompt) is presented to the LLM.
- **Tool Invocation:** If the model identifies missing information or ambiguous instructions, it selects a tool or retrieval method—like a vector database query (e.g., Azure AI Search Hybrid search over private data) or a structured SQL call—to gather more context.
- **Assessment & Refinement:** After reviewing the returned data, the model decides whether the information suffices. If not, it refines the query, tries a different tool, or adjusts its approach.
- **Repeat Until Satisfied:** This cycle continues until the model determines that it has enough clarity and evidence to deliver a final, well-reasoned response.
- **Memory & State:** Because the system maintains state and memory across steps, it can recall previous attempts and their outcomes, avoiding redundancy and making more informed decisions as it proceeds.

Over time, this creates a sense of evolving understanding, enabling the model to navigate complex, multi-step tasks without requiring a human to constantly intervene or reshape the prompt.

## Handling Failure Modes and Self-Correction

Agentic RAG’s autonomy also includes robust self-correction mechanisms. When the system encounters obstacles—such as retrieving irrelevant documents or dealing with problematic queries—it can:

- **Iterate and Re-Query:** Instead of returning low-value responses, the model tries new search strategies, rewrites database queries, or explores alternative data sets.
- **Use Diagnostic Tools:** The system may use additional functions to debug its reasoning steps or confirm the accuracy of retrieved data. Tools like Azure AI Tracing are important for enabling robust observability and monitoring.
- **Fallback on Human Oversight:** For high-stakes or repeatedly failing scenarios, the model might flag uncertainty and request human guidance. Once the human provides corrective feedback, the model can incorporate that lesson going forward.

This iterative and dynamic approach allows the model to continuously improve, ensuring it’s not just a one-shot system but one that learns from its mistakes during a given session.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.en.png)

## Boundaries of Agency

Despite its autonomy within a task, Agentic RAG is not equivalent to Artificial General Intelligence. Its “agentic” capabilities are limited to the tools, data sources, and policies provided by human developers. It can’t create its own tools or step outside the domain boundaries that have been set. Instead, it excels at dynamically orchestrating the resources at hand.  
Key differences from more advanced AI forms include:

1. **Domain-Specific Autonomy:** Agentic RAG systems focus on achieving user-defined goals within a known domain, using strategies like query rewriting or tool selection to improve outcomes.
2. **Infrastructure-Dependent:** The system’s capabilities depend on the tools and data integrated by developers. It can’t exceed these boundaries without human intervention.
3. **Respect for Guardrails:** Ethical guidelines, compliance rules, and business policies remain critical. The agent’s freedom is always constrained by safety measures and oversight mechanisms.

## Practical Use Cases and Value

Agentic RAG excels in scenarios requiring iterative refinement and precision:

1. **Correctness-First Environments:** In compliance checks, regulatory analysis, or legal research, the agentic model can repeatedly verify facts, consult multiple sources, and rewrite queries until it produces a thoroughly vetted answer.
2. **Complex Database Interactions:** When working with structured data where queries often fail or need adjustment, the system can autonomously refine its queries using Azure SQL or Microsoft Fabric OneLake, ensuring the final retrieval aligns with the user’s intent.
3. **Extended Workflows:** Longer-running sessions may evolve as new information emerges. Agentic RAG can continuously incorporate new data, adapting its strategies as it learns more about the problem.

## Governance, Transparency, and Trust

As these systems become more autonomous in their reasoning, governance and transparency are essential:

- **Explainable Reasoning:** The model can provide a record of the queries it made, the sources it consulted, and the reasoning steps it took to reach its conclusion. Tools like Azure AI Content Safety and Azure AI Tracing / GenAIOps can help maintain transparency and mitigate risks.
- **Bias Control and Balanced Retrieval:** Developers can adjust retrieval strategies to ensure balanced, representative data sources are considered, and regularly audit outputs to detect bias or skewed patterns using custom models for advanced data science organizations with Azure Machine Learning.
- **Human Oversight and Compliance:** For sensitive tasks, human review remains crucial. Agentic RAG doesn’t replace human judgment in high-stakes decisions—it enhances it by delivering more thoroughly vetted options.

Having tools that provide a clear record of actions is essential. Without them, debugging a multi-step process can be very challenging. See the following example from Literal AI (the company behind Chainlit) for an Agent run:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.en.png)

## Conclusion

Agentic RAG represents a natural progression in how AI systems handle complex, data-intensive tasks. By adopting repeated interactions, autonomously selecting tools, and refining queries until achieving a high-quality result, the system moves beyond static prompt-following into a more adaptive, context-aware decision-maker. While still limited by human-defined infrastructures and ethical guidelines, these agentic capabilities enable richer, more dynamic, and ultimately more useful AI interactions for both businesses and end-users.

### Got More Questions about Agentic RAG?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI Agents questions answered.

## Additional Resources

-
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implement Retrieval Augmented Generation (RAG) with Azure OpenAI Service: Learn how to use your own data with the Azure OpenAI Service. This Microsoft Learn module provides a comprehensive guide on implementing RAG  
- [Evaluation of generative AI applications with Azure AI Foundry: This article covers the evaluation and comparison of models on publicly available datasets, including Agentic AI applications and RAG architectures](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)  
- [What is Agentic RAG | Weaviate](https://weaviate.io/blog/what-is-agentic-rag)  
- [Agentic RAG: A Complete Guide to Agent-Based Retrieval Augmented Generation – News from generation RAG](https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/)  
- [Agentic RAG: turbocharge your RAG with query reformulation and self-query! Hugging Face Open-Source AI Cookbook](https://huggingface.co/learn/cookbook/agent_rag)  
- [Adding Agentic Layers to RAG](https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U)  
- [The Future of Knowledge Assistants: Jerry Liu](https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s)  
- [How to Build Agentic RAG Systems](https://www.youtube.com/watch?v=AOSjiXP1jmQ)  
- [Using Azure AI Foundry Agent Service to scale your AI agents](https://ignite.microsoft.com/sessions/BRK102?source=sessions)  

### Academic Papers  

- [2303.17651 Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)  
- [2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)  
- [2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)  
- [2501.09136 Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG](https://arxiv.org/abs/2501.09136)  

## Previous Lesson  

[Tool Use Design Pattern](../04-tool-use/README.md)  

## Next Lesson  

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)  

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.