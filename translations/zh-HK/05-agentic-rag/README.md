[![Agentic RAG](../../../translated_images/zh-HK/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(點擊上方圖片觀看本課程影片)_

# Agentic RAG

本課程全面介紹 Agentic Retrieval-Augmented Generation（Agentic RAG），這是一種新興的 AI 範式，其中大型語言模型（LLM）可自主規劃下一步行動，同時從外部來源提取資料。不同於靜態的檢索後閱讀模式，Agentic RAG 涉及對 LLM 的反覆呼叫，交替進行工具或函數調用以及結構化輸出。系統會評估結果，優化查詢，如有需要則調用更多工具，並持續此循環直到達成令人滿意的解決方案。

## 介紹

本課程將涵蓋

- **了解 Agentic RAG：** 學習 AI 新興範式，其中大型語言模型（LLM）自主規劃下一步行動，同時從外部資料來源提取資訊。
- **掌握反覆的製作者-核查者模式：** 理解反覆呼叫 LLM 的迴圈，穿插工具或函數呼叫及結構化輸出，旨在提升正確性及處理格式錯誤的查詢。
- **探索實用應用：** 辨識 Agentic RAG 突出的場景，例如重視正確性的環境、複雜的資料庫互動及延伸工作流程。

## 學習目標

完成本課程後，你將會知道如何／理解：

- **理解 Agentic RAG：** 了解 AI 新興範式，其中大型語言模型（LLM）自主計劃下一步，同時提取外部資料。
- **反覆的製作者-核查者模式：** 掌握反覆呼叫 LLM 的迴圈概念，穿插工具或函數呼叫及結構化輸出，以提升正確性及處理格式錯誤的查詢。
- **掌控推理流程：** 理解系統擁有自身推理能力，能自行決定如何處理問題，無需依賴預定路徑。
- **工作流程：** 了解代理模型獨立決定檢索市場趨勢報告、識別競爭者資料、關聯內部銷售指標、綜合分析結果並評估策略的過程。
- **反覆迴圈、工具整合及記憶：** 瞭解此系統依賴反覆互動模式，跨步驟維持狀態和記憶，避免重複輪迴並做出明智決策。
- **處理失效模式與自我校正：** 探索系統強大自我校正機制，包括迭代及重新查詢、使用診斷工具以及求助人類監督。
- **代理範圍邊界：** 理解 Agentic RAG 的限制，聚焦於特定領域自主性、基礎架構依賴及遵守安全規範。
- **實際用例及價值：** 辨識 Agentic RAG 表現出色的場景，如注重正確性的環境、複雜的資料庫交互和延伸工作流程。
- **治理、透明度與信任：** 瞭解治理和透明度的重要性，包括可解釋的推理、偏見控制及人類監管。

## 什麼是 Agentic RAG？

Agentic Retrieval-Augmented Generation（Agentic RAG）是一種新興的 AI 範式，大型語言模型（LLM）自主規劃下一步行動，同時從外部來源提取資訊。不同於靜態的檢索後閱讀模式，Agentic RAG 涉及對 LLM 的反覆呼叫，穿插工具或函數調用及結構化輸出。系統評估結果，優化查詢，必要時調用更多工具，並持續此循環直至達成滿意解決方案。此反覆的「製作者-核查者」式操作提升正確性，處理格式錯誤查詢，確保高品質結果。

系統積極掌控其推理過程，重寫失敗查詢，選擇不同檢索方式，並整合多種工具，例如 Azure AI Search 向量搜尋、SQL 資料庫或自訂 API，最終敲定答案。Agentic 系統的獨特之處在於其掌控推理流程的能力。傳統 RAG 實作依賴預定義路徑，但 Agentic 系統根據資訊品質自主決定步驟順序。

## 定義 Agentic Retrieval-Augmented Generation（Agentic RAG）

Agentic Retrieval-Augmented Generation（Agentic RAG）是 AI 發展中的新範式，LLM 不僅從外部資料來源提取資訊，還自主規劃下一步行動。不同於靜態檢索後閱讀模式或精心編寫的提示序列，Agentic RAG 涉及反覆呼叫 LLM 的迴圈，穿插工具或函數呼叫及結構化輸出。每個回合系統評估結果，決定是否優化查詢，必要時調用更多工具，繼續迴圈直至取得滿意解決方案。

這種反覆的「製作者-核查者」操作模式旨在提升正確性，處理格式錯誤的結構化資料庫查詢（例如 NL2SQL），確保成果的均衡與高品質。系統積極掌握推理流程，可重寫失敗的查詢、選擇不同檢索方式、整合多種工具，如 Azure AI Search 向量搜尋、SQL 資料庫或自訂 API，最終決定答案。此舉免除了過於複雜的編排框架，取而代之的是一個相對簡單的「LLM 呼叫 → 工具使用 → LLM 呼叫 → …」迴圈，卻能產出成熟且有根據的結果。

![Agentic RAG 核心迴圈](../../../translated_images/zh-HK/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## 掌控推理流程

系統成為「Agentic」的關鍵特質是能夠掌控自身推理流程。傳統 RAG 實作常依賴人類預先定義模型的路徑：一串思考鏈條，指示何時及如何檢索資訊。
但當系統真正具備代理性，它會內部決定如何處理問題。它不只是執行腳本，而是根據所得資訊的品質自主決定步驟順序。
例如，當被要求制定產品上市策略時，它不會只依賴一個描繪完整研究及決策流程的提示，而是代理模型會獨立決定：

1. 使用 Bing 網絡資料檢索取得最新市場趨勢報告
2. 利用 Azure AI Search 辨識相關競爭者資料
3. 使用 Azure SQL 資料庫比對歷史內部銷售數據
4. 透過 Azure OpenAI Service 綜合分析結論成為完整策略
5. 評估策略中有無缺口或不一致，必要時提示再度檢索
這些步驟──優化查詢、選擇來源、反覆試探直至「滿意」答案──均由模型決定，非人類預寫腳本。

## 反覆迴圈、工具整合及記憶

![工具整合架構](../../../translated_images/zh-HK/tool-integration.0f569710b5c17c10.webp)

代理系統依賴以下迴圈互動模式：

- **初始呼叫：** 將用戶目標（即用戶提示）傳遞給 LLM。
- **工具調用：** 若模型識別缺少資訊或指令模糊，會選擇工具或檢索方法，如向量資料庫查詢（例如 Azure AI Search 混合私有資料檢索）或結構化的 SQL 呼叫，以收集更多上下文資訊。
- **評估與優化：** 透過檢查回傳數據，模型判斷資料是否足夠，如不夠會優化查詢、更換工具或調整策略。
- **反覆至滿意：** 循環進行直到模型確認已有足夠資料與證據以產出最終合理的回應。
- **記憶與狀態：** 系統在多步驟間維持狀態與記憶，能回憶之前的嘗試與結果，避免重複輪迴，並做出更知情的決策。

久而久之，這形成一種不斷演進的理解，讓模型能駕馭複雜的多步任務，無需人類持續干預或調整提示。

## 處理失敗模式與自我校正

Agentic RAG 的自主性也包含強大自我校正機制。當系統遇到死胡同，例如檢索到無關文件或格式錯誤查詢時，它可以：

- **反覆與重新查詢：** 不返回低價值回答，而是嘗試新的檢索策略，重寫資料庫查詢，或查看替代資料集。
- **使用診斷工具：** 系統可調用設計用以調試推理步驟或確認檢索資料正確性的附加函數。像 Azure AI Tracing 的工具將有助於強化可觀察性與監控。
- **依賴人工監督：** 對高風險或屢次失敗狀況，模型可標示不確定性並尋求人類指導。人類給予的校正反饋將被模型納入學習，於後續應用。

這種反覆且動態的方式允許模型持續進步，確保不只是一次性的系統，而是在特定會話中從錯誤中學習。

![自我校正機制](../../../translated_images/zh-HK/self-correction.da87f3783b7f174b.webp)

## 代理範圍邊界

儘管 Agentic RAG 於任務中具有自主性，它並不等同於通用人工智慧。其「代理」能力限於人類開發者提供的工具、資料來源與政策。它無法自行發明工具或突破設定的領域界限，而是在現有資源中靈活調度。
與更先進 AI 形式的關鍵差異包括：

1. **領域專屬自主性：** Agentic RAG 系統專注於實現用戶定義目標於特定領域，利用查詢重寫或工具選擇等策略提升成果。
2. **依賴基礎架構：** 系統能力取決於開發者整合的工具和資料，無法無人介入超越這些限制。
3. **尊重安全規範：** 倫理指導、合規規則與商務政策非常重要，代理的自由度永遠受限於安全措施和監管機制（希望如此？）。

## 實際用例及價值

Agentic RAG 在需反覆優化與精確度的場景中表現突出：

1. **重視正確性的環境：** 在合規檢查、法規分析或法律研究中，代理模型可反覆驗證事實，諮詢多來源，並反覆重寫查詢，直到產生徹底審核的答覆。
2. **複雜資料庫互動：** 處理結構化資料時，查詢經常失敗或需調整，系統能自主優化 Azure SQL 或 Microsoft Fabric OneLake 的查詢，確保最終檢索符合使用者意圖。
3. **延長工作流程：** 較長會話會隨新資訊浮現而演變。Agentic RAG 能持續整合新資料，隨著對問題領域理解加深而調整策略。

## 治理、透明度與信任

隨著系統推理自主性提升，治理和透明度顯得尤為重要：

- **可解釋推理：** 模型可提供其發出查詢、諮詢來源及推理步驟的審計軌跡。工具如 Azure AI 內容安全和 Azure AI Tracing / GenAIOps 有助維持透明度並降低風險。
- **偏見控制與均衡檢索：** 開發者可調整檢索策略，確保考慮均衡且具代表性的資料來源，並定期審核輸出以檢測偏見或失衡模式，採用 Azure Machine Learning 為先進資料科學組織定製模型。
- **人類監督與合規：** 對於敏感任務，人類審查仍不可或缺。Agentic RAG 不取代人類在高風險決策中的判斷，而是提供更完整審核的選項作為輔助。

有明確記錄行動的工具至關重要，缺乏時多步過程除錯非常困難。參見 Literal AI（Chainlit 背後公司）提供的 Agent 運行示例：

![AgentRunExample](../../../translated_images/zh-HK/AgentRunExample.471a94bc40cbdc0c.webp)

## 結論

Agentic RAG 代表 AI 系統處理複雜資料密集任務的自然進化。透過採用反覆互動模式、自主選擇工具及優化查詢直到達成高品質結果，系統超越靜態提示執行，成為更具適應性、情境感知的決策者。雖仍受限於人類定義的基礎架構與倫理規範，這些代理能力使企業和終端用戶享有更豐富、更動態且更實用的 AI 互動體驗。

### 對 Agentic RAG 有更多問題？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加線上諮詢，解答你的 AI 代理人問題。

## 額外資源

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">使用 Azure OpenAI Service 實作 Retrieval Augmented Generation (RAG)：學習如何搭配 Azure OpenAI Service 使用自有資料。此 Microsoft Learn 模組提供實作 RAG 的全方位指南</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">使用 Microsoft Foundry 評估生成式 AI 應用：本文涵蓋在公開資料集上模型的評估與比較，包括 Agentic AI 應用及 RAG 架構</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">什麼是 Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG：基於代理的檢索增強生成完整指南 – Generation RAG 新聞</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG：用查詢重構和自我查詢為你的 RAG 提速！Hugging Face 開源 AI 食譜書</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">為 RAG 添加 Agentic 層</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">知識助理的未來：Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">如何構建 Agentic RAG 系統</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">使用 Microsoft Foundry Agent 服務擴展你的 AI 代理</a>

### 學術論文

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 自我優化：帶有自我反饋的迭代優化</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 反思：帶有語言強化學習的語言代理</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC：大型語言模型能通過交互式工具批評自我修正</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic 檢索增強生成：Agentic RAG 調查</a>

## 簡單測試此代理（可選）

在你學會在 [Lesson 16](../16-deploying-scalable-agents/README.md) 部署代理後，你可以用 [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) 對本課的 `TravelRAGAgent` 進行簡單測試 — 確認它的答案保持基於知識庫。具體執行方法請參見 [`tests/README.md`](../tests/README.md)。

## 前一課

[工具使用設計模式](../04-tool-use/README.md)

## 下一課

[構建可信 AI 代理](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->