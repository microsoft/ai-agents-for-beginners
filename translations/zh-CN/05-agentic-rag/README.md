[![Agentic RAG](../../../translated_images/zh-CN/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(点击上方图片观看本课视频)_

# Agentic RAG

本课全面介绍了Agentic Retrieval-Augmented Generation（Agentic RAG），这是一种新兴的AI范式，大型语言模型(LLM)在提取外部信息的同时，能够自主规划下一步操作。不同于静态的先检索后阅读模式，Agentic RAG涉及对LLM的迭代调用，穿插工具或函数调用及结构化输出。系统评估结果、优化查询、根据需要调用更多工具，并循环直到获得满意的解决方案。

## 介绍

本课内容包括

- **理解Agentic RAG:** 了解这一AI新范式，LLM能自主规划下一步操作并从外部数据源检索信息。
- **掌握迭代的Maker-Checker风格:** 理解迭代调用LLM的循环，穿插工具或函数调用及结构化输出，以提高正确性并处理格式错误的查询。
- **探索实际应用:** 识别Agentic RAG适用的场景，如重视正确性的环境、复杂数据库交互和扩展的工作流。

## 学习目标

完成本课后，您将能够/了解：

- **理解Agentic RAG:** 掌握这一AI新兴范式，LLM自主规划下一步操作并从外部数据源获取信息。
- **迭代Maker-Checker风格:** 理解迭代调用LLM的循环，穿插工具或函数调用及结构化输出，以提升正确性并处理格式错误查询。
- **掌控推理过程:** 理解系统自主掌控推理流程，如何决定解决问题的方式而无需预定义路径。
- **工作流:** 理解Agentic模型如何自主决定提取市场趋势报告、识别竞争对手数据、关联内部销售指标、整合发现并评估策略。
- **迭代循环、工具集成与记忆:** 了解系统基于循环交互模式，跨步骤保持状态与记忆，避免重复循环并作出明智决策。
- **故障处理与自我纠正:** 探索系统强大的自我纠错机制，包括迭代重试、使用诊断工具以及依赖人工监督。
- **自主边界:** 了解Agentic RAG的局限性，关注领域特定的自主性、基础设施依赖及规范约束。
- **实际使用场景与价值:** 识别Agentic RAG发挥优势的场景，如重视准确性的环境、复杂数据库交互和延展工作流。
- **治理、透明度与信任:** 了解治理和透明度的重要性，包括可解释推理、偏差控制及人工监督。

## 什么是Agentic RAG？

Agentic Retrieval-Augmented Generation（Agentic RAG）是一种新兴的AI范式，LLM在检索外部信息的同时自主规划下一步操作。与静态的先检索后阅读模式不同，Agentic RAG涉及对LLM的迭代调用，穿插工具或函数调用和结构化输出。系统评估所获结果，优化查询，按需调用更多工具，循环执行直到获得满意方案。这种迭代的“maker-checker”风格提升了正确性，能处理格式错误的查询，确保高质量结果。

系统主动掌控其推理过程，重写失败的查询、选择不同检索方法、集成多种工具——如Azure AI Search的向量检索、SQL数据库或自定义API——然后才给出最终答案。Agentic系统的显著特点是能自主掌控推理流程。传统RAG只能依赖预定义路径，Agentic系统则根据所获信息的质量自主确定操作步骤序列。

## 定义Agentic Retrieval-Augmented Generation（Agentic RAG）

Agentic Retrieval-Augmented Generation（Agentic RAG）是AI开发中的新兴范式，LLM不仅能够从外部数据源提取信息，还能自主规划下一步操作。不同于静态的先检索后阅读模式或精心编排的提示序列，Agentic RAG涉及迭代调用LLM的循环，穿插工具或函数调用和结构化输出。每一步系统都会评估结果，决定是否优化查询、调用额外工具，并循环直到满足条件。

这种迭代的“maker-checker”操作模式旨在提高正确性，处理向结构化数据库（如NL2SQL）提出的错误格式查询，并保证平衡且高质量的结果。系统不单靠精心设计的提示链，而是主动掌控推理流程，能重写失败的查询、选择不同的检索方法、整合多种工具——如Azure AI Search向量检索、SQL数据库或自定义API—最终给出结果。这样无需复杂的编排框架，只需“LLM调用→工具使用→LLM调用→…”的循环即可产出复杂且稳健的输出。

![Agentic RAG Core Loop](../../../translated_images/zh-CN/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## 掌控推理过程

系统被称为“Agentic”的关键特质是它自主掌控推理过程。传统RAG实现通常依赖于人类预定义模型的路径：一个指明何时检索什么内容的思维链。
但当系统真正具备Agentic特质时，它则内部决定如何解决问题。它不仅仅执行脚本，而是基于所获信息质量自主确定步骤顺序。
举例来说，若被要求制定产品发布策略，Agentic模型不会仅依赖明确规定整个研究和决策流程的提示，而是自主决定：

1. 使用Bing Web Grounding检索当前市场趋势报告
2. 通过Azure AI Search识别相关竞争对手数据
3. 运用Azure SQL数据库关联历史内部销售指标
4. 通过Azure OpenAI服务将发现整合为连贯策略
5. 评估策略中存在的遗漏或不一致，必要时再次检索
以上所有步骤——优化查询、选择信息来源、迭代直至“满意”答案——均由模型自主决定，而非人工预设。

## 迭代循环、工具集成与记忆

![Tool Integration Architecture](../../../translated_images/zh-CN/tool-integration.0f569710b5c17c10.webp)

Agentic系统依赖于循环交互模式：

- **初始调用:** 用户目标（即用户提示）被传递给LLM。
- **工具调用:** 若模型发现信息缺失或指令模糊，选择相关工具或检索方式—如向量数据库查询（例如Azure AI Search对私有数据的混合搜索）或结构化SQL调用—以获取更多上下文。
- **评估与优化:** 评审返回数据后，模型判定信息是否充分。若不充分，则优化查询、尝试不同工具或调整策略。
- **循环至满意:** 持续循环，直到模型判定已具有足够清晰度和证据来提供最终、合理的答复。
- **记忆与状态:** 由于系统跨步骤保持状态和记忆，能回溯此前尝试及结果，避免重复循环并随着进展做出更明智的决策。

随着时间推移，模型形成不断发展的理解，能够应对复杂的多步任务，无需人工持续干预或调整提示。

## 处理失败模式与自我纠正

Agentic RAG的自主性还体现在其强大的自我纠错机制上。当系统遭遇死胡同——比如检索到无关文档或遇到格式错误的查询时——它可以：

- **迭代重试:** 模型不返回低价值响应，而是尝试新搜索策略、重写数据库查询或查看替代数据集。
- **使用诊断工具:** 系统可调用额外函数帮助调试推理步骤或确认检索数据正确性。Azure AI Tracing等工具对于实现健壮的可观测性与监控至关重要。
- **依赖人工监督:** 在高风险或反复失败场景中，模型可能标记不确定性并请求人工指导。一旦获得人工纠正反馈，模型能将经验纳入后续推理。

这种迭代且动态的方法使模型持续改进，确保它不仅是一次性系统，而是能在单次会话中从错误中学习。

![Self Correction Mechanism](../../../translated_images/zh-CN/self-correction.da87f3783b7f174b.webp)

## 自主性的边界

尽管在任务内具备自主性，Agentic RAG并非人工通用智能。其“自主”能力受限于人类开发者提供的工具、数据源和政策。它无法自创工具或突破设定的领域边界，而是在动态编排现有资源方面表现出色。
关键区别于更先进AI形式的地方包括：

1. **领域特定的自主性:** Agentic RAG专注于在已知领域内实现用户定义目标，采用如查询重写或工具选择等策略改善结果。
2. **依赖基础设施:** 系统能力取决于开发者集成的工具和数据，无法在无人干预下超越这些边界。
3. **遵守规章:** 道德准则、合规规则及业务政策极为重要。代理的自由始终受安全措施和监督机制约束（希望如此）。

## 实际使用场景与价值

Agentic RAG在需要迭代优化和精准度的场景中表现出色：

1. **重视正确性的环境:** 在合规检查、法规分析或法律研究中，Agentic模型能反复验证事实，咨询多源信息，重写查询，直到产出彻底审核的答案。
2. **复杂数据库交互:** 在处理结构化数据时，查询常失败或需调整，系统能自主优化查询（利用Azure SQL或Microsoft Fabric OneLake），确保最终检索符合用户意图。
3. **延伸工作流:** 长时间运行的会话会随着新信息涌现而发展。Agentic RAG能持续整合新数据，随着对问题领域认识的加深调整策略。

## 治理、透明度与信任

随着系统推理自主性增强，治理和透明度显得尤为关键：

- **可解释推理:** 模型能提供查询轨迹、参考来源及达成结论的推理步骤记录。Azure AI内容安全、Azure AI追踪/GenAIOps等工具有助维护透明度与风险缓解。
- **偏见控制与平衡检索:** 开发者可调优检索策略，确保涉及平衡且具代表性的数据源，定期通过定制模型审计输出，检测偏差或倾斜模式，尤其是使用Azure机器学习支持的高级数据科学组织。
- **人工监督与合规:** 对于敏感任务，人工审查仍不可缺。Agentic RAG不能替代高风险决策中的人工判断，而是通过提供更为彻底审核的选项予以增强。

拥有可清晰记录操作的工具非常重要。缺乏时，对多步骤过程的调试会十分困难。下面是Literal AI（Chainlit背后公司）给出的Agent运行示例：

![AgentRunExample](../../../translated_images/zh-CN/AgentRunExample.471a94bc40cbdc0c.webp)

## 结论

Agentic RAG代表了AI系统处理复杂、数据密集型任务的自然演进。通过采用循环交互模式，自主选择工具，优化查询，直至获得高质量结果，系统超越了静态遵循提示的模式，成为更具适应性和上下文感知的决策者。虽然仍受限于人类定义的基础设施和伦理准则，这些Agentic能力使企业和终端用户能够实现更丰富、更动态且更有用的AI交互。

### 对Agentic RAG还有更多疑问？

加入[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，与其他学习者交流，参加答疑时间，获得您关于AI代理的问题解答。

## 额外资源

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">使用Azure OpenAI服务实现检索增强生成（RAG）：学习如何用您自己的数据配合Azure OpenAI服务。本Microsoft Learn模块提供了全面的RAG实现指南</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">利用Microsoft Foundry评估生成式AI应用：本文涵盖模型在公开数据集上的评估与比较，包括Agentic AI应用和RAG架构</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">什么是Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG：基于代理的检索增强生成完整指南 – Generation RAG新闻</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">智能RAG：通过查询重新构造和自我查询，为您的RAG加速！Hugging Face开源AI手册</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">为RAG添加智能层</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">知识助理的未来：Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">如何构建智能RAG系统</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">使用Microsoft Foundry Agent服务扩展您的AI代理</a>

### 学术论文

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine：带有自我反馈的迭代精炼</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion：具有语言强化学习的语言代理</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC：大语言模型通过工具交互式批评进行自我纠正</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 智能检索增强生成：智能RAG综述</a>

## 快速测试该代理（可选）

在学习了如何在[第16课](../16-deploying-scalable-agents/README.md)中部署代理之后，您可以通过[`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json)对本课的`TravelRAGAgent`进行快速测试——检查其回答是否基于知识库。有关如何运行测试，请参见[`tests/README.md`](../tests/README.md)。

## 上一课

[工具使用设计模式](../04-tool-use/README.md)

## 下一课

[构建可信赖的AI代理](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->