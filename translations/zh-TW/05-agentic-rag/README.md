[![Agentic RAG](../../../translated_images/zh-TW/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(點擊上方圖片觀看本課程影片)_

# Agentic RAG

本課程提供關於自主檢索增強生成（Agentic Retrieval-Augmented Generation，Agentic RAG）的一個全面概述，這是一種新興的 AI 範式，其中大型語言模型（LLMs）能夠自主規劃下一步行動，同時從外部資源中提取資訊。與靜態的檢索－閱讀模式不同，Agentic RAG 涉及對 LLM 的迭代呼叫，並穿插工具或函式呼叫及結構化輸出。系統會評估結果、細化查詢、如有需要調用更多工具，並持續這個循環直到達成滿意的解決方案。

## 介紹

本課程將涵蓋

- **了解 Agentic RAG：** 認識 AI 新興範式，讓大型語言模型（LLMs）自主規劃下一步，同時從外部數據源提取資訊。
- **掌握迭代式製造‐檢查者風格：** 理解對 LLM 反覆迭代呼叫的流程，穿插工具或函式呼叫與結構化輸出，以提升正確性及處理格式錯誤的查詢。
- **探索實務應用場景：** 識別 Agentic RAG 發揮優勢的場景，例如優先正確性環境、複雜資料庫互動及延伸工作流程。

## 學習目標

完成本課程後，你將能夠/了解：

- **理解 Agentic RAG：** 認識 AI 新興範式，讓大型語言模型（LLMs）自主規劃下一步，同時從外部數據源提取資訊。
- **迭代式製造‐檢查者風格：** 掌握對 LLM 反覆迭代呼叫的概念，穿插工具或函式呼叫與結構化輸出，提升正確性並處理格式錯誤的查詢。
- **掌握推理過程自主權：** 理解系統擁有自身推理過程的能力，自主決定如何解決問題，而非依賴預定路徑。
- **工作流程：** 理解自主模型如何獨立決定提取市場趨勢報告、識別競爭對手資料、關聯內部銷售指標、綜合分析結果並評估策略。
- **迭代循環、工具整合與記憶：** 了解系統依靠反覆互動模式，跨步驟維持狀態和記憶，避免重複循環並做出明確決策。
- **處理失敗模式與自我修正：** 探討系統完善的自我修正機制，包括迭代重查、使用診斷工具以及倚賴人工監督。
- **自主邊界：** 了解 Agentic RAG 的限制，著重於領域特定自主權、基礎架構依賴與監控規範。
- **實務應用與價值：** 確認 Agentic RAG 發揮優勢的場合，如優先正確性環境、複雜資料庫互動及擴展工作流程。
- **治理、透明性與信任：** 瞭解治理與透明性的重要性，包括可解釋的推理、偏差控制與人工監督。

## 什麼是 Agentic RAG？

自主檢索增強生成（Agentic RAG）是一種新興的 AI 範式，大型語言模型（LLMs）能夠自主規劃下一步，同時從外部資源拉取資訊。不同於靜態的檢索－閱讀模式，Agentic RAG 包含對 LLM 的迭代呼叫，穿插工具或函式呼叫及結構化輸出。系統會評估結果、細化查詢，必要時調用附加工具，並持續此循環直到獲得令人滿意的解決方案。這種迭代的「製造－檢查者」風格提升正確性，處理格式錯誤的查詢，並確保高品質結果。

系統積極掌握自身推理過程，重寫失敗的查詢，選擇不同的檢索方法，並整合多種工具——例如 Azure AI Search 的向量搜索、SQL 資料庫或自訂 API——最終完成答案。代理系統的獨特之處在於其掌握推理過程的能力。傳統 RAG 實作依賴預先定義的路徑，而代理系統則基於所獲資訊的品質自主決定步驟順序。

## 定義 Agentic 檢索增強生成（Agentic RAG）

自主檢索增強生成（Agentic RAG）是 AI 發展中一種新興範式，LLMs 不僅從外部數據源提取資訊，還能自主規劃下一步行動。不同於靜態檢索－閱讀模式或精心設計的提示序列，Agentic RAG 涉及對 LLM 的反覆迭代呼叫，穿插工具或函式呼叫與結構化輸出。系統每一步都評估已取得的結果，決定是否細化查詢，必要時呼叫額外工具，並持續此循環直到達成滿意解決方案。

此種迭代的「製造－檢查者」操作風格旨在提升正確性、處理結構化資料庫（如 NL2SQL）的格式錯誤查詢，並確保均衡且高品質的結果。系統積極掌握自身推理過程，不僅依賴精心設計的提示鏈。它能重寫失敗的查詢、選擇不同檢索方式並整合多個工具——包含 Azure AI Search 向量搜索、SQL 資料庫或客製化 API——最終完成答案。如此便不需過於複雜的協調框架，而是透過「LLM 呼叫 → 使用工具 → LLM 呼叫 → …」的相對簡單循環，產生複雜且有根據的輸出。

![Agentic RAG Core Loop](../../../translated_images/zh-TW/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## 掌握推理過程

使系統成為「自主」的關鍵特質，是它能掌握自身的推理過程。傳統 RAG 多依賴人類預先定義模型的路徑：一個概述欲檢索內容與時間的思考鏈。
但當系統真正具備自主性時，它會在內部決定如何解決問題。它不只是執行腳本，而是根據所取得的資訊質量自主決定步驟順序。
例如，當被要求建立產品上市策略時，它不會只依賴完整指示整個研究與決策流程的提示。相反地，代理模型會獨立決定：

1. 使用 Bing Web Grounding 檢索當前市場趨勢報告
2. 使用 Azure AI Search 識別相關競爭對手資料
3. 使用 Azure SQL Database 關聯歷史內部銷售指標
4. 通過 Azure OpenAI 服務協調整理成一致性的策略
5. 評估策略中的缺口或不一致處，必要時進行新一輪檢索
以上所有步驟——細化查詢、選擇來源、反覆進行直到對答案「滿意」——皆由模型自主決定，非人為預先編寫腳本。

## 迭代循環、工具整合與記憶

![Tool Integration Architecture](../../../translated_images/zh-TW/tool-integration.0f569710b5c17c10.webp)

代理系統依賴一種迴圈互動模式：

- **初始呼叫：** 使用者目標（又稱使用者提示）呈現給 LLM。
- **調用工具：** 若模型發現資訊不足或指令模糊，會選擇工具或檢索方法，如向量資料庫查詢（如對私有資料運行 Azure AI Search 混合搜尋）或結構化 SQL 呼叫，以獲取更多上下文。
- **評估與細化：** 閱讀回傳資料後，模型判定資訊是否足夠。如不足，則細化查詢、嘗試不同工具或調整策略。
- **反覆直到滿意：** 此循環將持續，直到模型認為已有足夠明確與充分證據，給出最終合理的回應。
- **記憶與狀態：** 因為系統跨步驟保持狀態與記憶，能回憶先前嘗試與結果，避免重複循環並做出更明確決策。

隨著時間推移，這創造一種演進性理解，使模型能掌握複雜多步任務，無需人類持續介入或重塑提示。

## 處理錯誤模式與自我修正

Agentic RAG 的自主性同時具備強大的自我修正機制。當系統遇到瓶頸——例如檢索到無關文件或遭遇格式錯誤查詢時——它能：

- **反覆迭代與重新查詢：** 模型嘗試新的搜尋策略，重寫資料庫查詢，或檢視替代資料集合，而非回傳低品質結果。
- **使用診斷工具：** 系統可呼叫額外功能幫助除錯推理流程或確認回傳資料正確性。工具如 Azure AI Tracing 對實現強健的可觀察性與監控非常重要。
- **倚賴人工監督：** 針對高風險或反覆失敗情況，模型可能標記不確定性並請求人類指導。當人類給予糾正意見後，模型可在後續運行中汲取經驗。

此種迭代且動態的方法讓模型持續進步，確保它不只是一次性系統，而是在該次會話中從錯誤中學習。

![Self Correction Mechanism](../../../translated_images/zh-TW/self-correction.da87f3783b7f174b.webp)

## 自主性的邊界

儘管具任務自主性，Agentic RAG 並非通用人工智慧。其「自主」能力限制於人類開發者提供的工具、資料來源與政策。它無法自行創造工具或跨越已設定的領域邊界。它擅長的是動態協調現有資源。
與更先進 AI 型態的主要差異包括：

1. **領域專屬自主權：** Agentic RAG 系統聚焦於實現使用者定義目標的已知領域，採用查詢重寫或工具選擇策略以改進成果。
2. **依賴基礎架構：** 系統能力依賴開發者整合的工具與資料，無人為介入無法跨越此限。
3. <strong>尊重監管規範：</strong>倫理準則、合規規定與商業政策依然極為重要。代理系統的自由始終受安全措施與監督機制約束（希望如此）。

## 實務應用案例與價值

Agentic RAG 在需反覆細化與精確的場景中表現突出：

1. **優先正確性環境：** 在合規檢查、法規分析或法律研究中，代理模型可多次核實事實、查詢多方資料並不停重寫查詢以產生深度審核的答案。
2. **複雜資料庫互動：** 處理結構化資料時，查詢經常失敗或需調整，系統能自主修正 Azure SQL 或 Microsoft Fabric OneLake 的查詢，確保最終檢索符合使用者意圖。
3. **延伸工作流程：** 較長運行期間，隨著新資訊出現，Agentic RAG 繼續整合新數據，且在學習更多問題領域後調整策略。

## 治理、透明性與信任

隨著系統推理更具自主性，治理與透明性變得至關重要：

- **可解釋推理：** 模型能提供查詢歷程、參考來源及推理過程的審計軌跡。工具如 Azure AI Content Safety 及 Azure AI Tracing / GenAIOps 有助維護透明度及風險控管。
- **偏差控制與均衡檢索：** 開發者可調整檢索策略確保參考均衡且具代表性的數據源，並使用針對進階數據科學組織的 Azure Machine Learning 客製化模型定期稽核輸出，檢測偏差或偏頗模式。
- **人工監督與合規：** 對敏感任務，人工審查仍不可或缺。Agentic RAG 不替代高風險決策中的人類判斷，而是透過提供更充分審核的選項輔助判斷。

擁有能提供清楚執行紀錄的工具至關重要。否則調試多步驟流程非常困難。以下為 Literal AI（Chainlit 背後公司）提供的代理運行範例：

![AgentRunExample](../../../translated_images/zh-TW/AgentRunExample.471a94bc40cbdc0c.webp)

## 結論

Agentic RAG 代表 AI 系統處理複雜且大量資料任務的自然進化。透過採用迭代互動模式、自主選擇工具與細化查詢直至達成高品質結果，系統從靜態提示跟隨者轉變為更具適應性與情境感知的決策者。雖然仍受限於人類定義的基礎架構與倫理準則，但這些代理能力讓企業與最終用戶能夠享有更豐富、更動態且最終更實用的 AI 互動體驗。

### 對 Agentic RAG 有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加辦公時間並解決你的 AI Agents 問題。

## 其他資源

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">使用 Azure OpenAI 服務實作檢索增強生成 (RAG)：了解如何使用自己的資料與 Azure OpenAI 服務。本 Microsoft Learn 模組提供實作 RAG 的全面指南</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Microsoft Foundry 的生成式 AI 應用評估：本文涵蓋在公開數據集上評估和比較模型，包括自主 AI 應用和 RAG 架構</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">什麼是 Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG：基於代理的檢索增強生成完整指南 – generation RAG 新聞</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG：使用查詢重組和自我查詢加速您的 RAG！Hugging Face 開源 AI 食譜</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">為 RAG 添加 Agentic 層</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">知識助理的未來：Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">如何構建 Agentic RAG 系統</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">使用 Microsoft Foundry Agent Service 擴展您的 AI 代理</a>

### 學術論文

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine：帶有自我反饋的迭代精煉</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion：具有語言強化學習的語言代理</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC：大型語言模型可以通過工具交互批評自我修正</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic 檢索增強生成：Agentic RAG 調查報告</a>

## 簡易測試此代理（可選）

在您學會在 [Lesson 16](../16-deploying-scalable-agents/README.md) 部署代理後，您可以用 [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) 對本課的 `TravelRAGAgent` 進行簡易測試——檢查它的回答是否基於知識庫。如何執行測試請參閱 [`tests/README.md`](../tests/README.md)。

## 前一課

[工具使用設計模式](../04-tool-use/README.md)

## 下一課

[構建值得信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->