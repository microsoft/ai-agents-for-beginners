[![Agentic RAG](../../../translated_images/zh-MO/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(點擊上方圖片觀看本課程視頻)_

# Agentic RAG

本課程全面介紹了Agentic檢索增強生成（Agentic RAG），這是一種新興的人工智能範式，其中大型語言模型（LLM）能自主規劃下一步行動，同時從外部來源拉取資訊。與靜態的先檢索再閱讀模式不同，Agentic RAG涉及對LLM的迭代調用，穿插工具或函數調用以及結構化輸出。系統會評估結果、優化查詢、在需要時調用額外工具，並持續此循環直到獲得滿意解決方案。

## 介紹

本課程將涵蓋

- **了解Agentic RAG：** 學習這種新興AI範式，其中大型語言模型（LLM）能自主規劃下一步行動，並從外部數據源提取資訊。
- **掌握迭代製造-檢查風格：** 理解迭代調用LLM的循環，穿插工具或函數調用及結構化輸出，旨在提升正確性並處理格式錯誤的查詢。
- **探索實際應用：** 確認Agentic RAG表現優異的場景，如以正確性優先的環境、複雜數據庫交互及長週期工作流程。

## 學習目標

完成本課程後，你將知道如何／理解：

- **理解Agentic RAG：** 了解這種新興AI模式，其中大型語言模型（LLM）能自主計劃下一步行動，並從外部數據源提取資訊。
- **迭代製造-檢查風格：** 掌握透過迭代調用LLM，並搭配工具或函數調用與結構化輸出的循環，以提升正確性和處理格式錯誤查詢的概念。
- **掌控推理過程：** 理解系統自主掌控推理過程的能力，能自主決定如何處理問題，而非依賴預設路徑。
- **工作流程：** 了解agentic模型如何獨立決定檢索市場趨勢報告、識別競爭對手數據、關聯內部銷售指標、綜合結論並評估策略。
- **迭代循環、工具整合與記憶：** 了解系統依賴於循環互動模式，於多步驟中維持狀態與記憶，避免重複循環並作出明智決策。
- **處理失敗模式與自我修正：** 探索系統強健的自我修正機制，包括迭代與重新查詢、使用診斷工具，以及依賴人工監督的備援機制。
- **代理範疇界限：** 了解Agentic RAG的限制，專注於領域特定自主性、基礎設施依賴及守護措施的尊重。
- **實際使用案例與價值：** 確認Agentic RAG在需要迭代精煉與精確性的場景中表現優異，如以正確性為先的環境、複雜資料庫交互與長工作流程。
- **治理、透明度與信任：** 了解治理與透明度的重要性，包括可解釋推理、偏差控制與人工監督。

## 什麼是Agentic RAG？

Agentic檢索增強生成（Agentic RAG）是一種新興的人工智能範式，其中大型語言模型（LLM）能自主規劃下一步行動，同時從外部來源拉取資訊。與靜態的先檢索再閱讀模式不同，Agentic RAG涉及對LLM的迭代調用，穿插工具或函數調用以及結構化輸出。系統會評估結果、優化查詢、在需要時調用額外工具，並持續此循環直到獲得滿意解決方案。這種迭代的「製造-檢查」風格能提升正確性，處理格式錯誤的查詢，並確保高品質結果。

系統積極掌控推理過程，重寫失敗查詢、選擇不同檢索方法、整合多種工具——例如Azure AI Search的向量搜索、SQL資料庫或自訂API——然後才最終給出答案。Agentic系統的區別特點是能完全掌控其推理過程。傳統RAG實現依賴預先定義的路徑，而agentic系統則會根據所獲信息的質量自主決定步驟順序。

## 定義Agentic檢索增強生成（Agentic RAG）

Agentic檢索增強生成（Agentic RAG）是AI開發中的一種新興範式，其中大型語言模型（LLM）不僅從外部數據源提取資訊，還能自主規劃下一步行動。它不同於靜態的檢索再讀取模式或精心編排的提示序列，Agentic RAG包含一個對LLM的迭代調用循環，穿插工具或函數調用及結構化輸出。在每個環節，系統評估已獲得的結果，決定是否優化查詢、調用更多工具，並持續迴圈直到達到滿意的解決方案。

這種迭代的「製造-檢查」操作風格旨在提升正確性、處理針對結構化數據庫（如NL2SQL）的格式錯誤查詢，並確保結果的平衡與高質量。系統不僅依靠精心設計的提示鏈，而是主動掌控推理過程。它能重寫失敗的查詢、選擇不同的檢索方法、整合多項工具——例如Azure AI Search的向量搜索、SQL資料庫或自訂API——在最終給出答案前，移除了過度複雜的編排框架。相反，透過一個相對簡單的「LLM調用→工具使用→LLM調用→…」循環過程，即可產出複雜且有據可依的輸出。

![Agentic RAG Core Loop](../../../translated_images/zh-MO/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## 掌控推理過程

系統「agentic」的獨特品質就在於其掌控推理過程的能力。傳統RAG實作往往依賴人工事先定義模型的路徑：列出需要檢索的內容及時間的思考鏈。
但真正的agentic系統會在內部決定如何處理問題。它不只是執行腳本，而是根據所獲資訊的質量自主決定步驟順序。
例如，若被要求制定產品上市策略，它不會僅依賴提示中明確列出的整個研究與決策流程，而是agentic模型自主決定：

1. 使用Bing Web Grounding檢索當前市場趨勢報告
2. 利用Azure AI Search識別相關競爭對手數據
3. 使用Azure SQL Database關聯歷史內部銷售指標
4. 通過Azure OpenAI Service綜合發現，製定連貫策略
5. 評估策略中存在的漏洞或不一致，如有必要進行新一輪檢索
所有這些步驟——優化查詢、選擇來源、持續迭代直到「滿意」答案——均由模型自主決定，而非人工預寫腳本。

## 迭代循環、工具整合與記憶

![Tool Integration Architecture](../../../translated_images/zh-MO/tool-integration.0f569710b5c17c10.webp)

Agentic系統依賴循環互動模式：

- **初始調用：** 將用戶目標（即用戶提示）提供給LLM。
- **工具調用：** 若模型發現資訊不足或指令含糊，會選擇工具或檢索方法——如向量資料庫查詢（例如Azure AI Search對私有數據的混合搜索）或結構化SQL調用——以收集更多上下文。
- **評估與優化：** 在審查回傳數據後，模型決定資訊是否充足。若不足，會優化查詢、嘗試其他工具或調整策略。
- **反覆至滿意：** 此循環持續進行，直到模型判定已獲足夠清晰度和證據，可給出最終且推理完善的回應。
- **記憶與狀態：** 由於系統在多步驟中維持狀態和記憶，它能回想先前嘗試與結果，避免重複循環並作出更明智決策。

時間推移中，這形塑出一種不斷演進的理解力，使模型能駕馭複雜多步任務，而不需人為持續介入或重塑提示。

## 處理失敗模式與自我修正

Agentic RAG的自主性還包含強健的自我修正機制。當系統遇到死胡同，如檢索出無關文件或遇到格式錯誤的查詢時，它能：

- **迭代與重新查詢：** 模型不會返回低價值的回應，而是嘗試新的搜索策略，重寫資料庫查詢，或查看替代資料集。
- **使用診斷工具：** 系統可能調用額外功能，協助調試推理步驟或確認檢索數據的正確性。Azure AI Tracing等工具對增強可觀察性和監控至關重要。
- **依賴人工監督：** 對高風險或多次失敗的情況，模型可能標記不確定性並請求人工指導。當人類提供修正反饋後，模型可在後續中吸收該經驗。

此迭代且動態的方法讓模型持續提升，確保它不僅是一次性的系統，而是在該會話中從錯誤中學習。

![Self Correction Mechanism](../../../translated_images/zh-MO/self-correction.da87f3783b7f174b.webp)

## 代理範疇界限

儘管在任務中具自主性，Agentic RAG並不等同於人工通用智能。其「agentic」能力僅限於由人工開發人員提供的工具、數據源和政策。它無法自創工具或跨越已設置的領域邊界，而是專長於動態協調現有資源。
與更高級AI形式的主要區別包括：

1. **領域專屬自主性：** Agentic RAG系統聚焦於在已知範疇內達成用戶定義目標，採用如查詢重寫或工具選擇等策略改善結果。
2. **基礎設施依賴性：** 系統能力依賴開發人員整合的工具和數據，無人工介入無法突破這些邊界。
3. **尊重守護措施：** 倫理指南、合規規範與業務政策極其重要。agent的自由度始終受到安全措施與監督機制的限制（希望如此？）

## 實際使用案例與價值

Agentic RAG在需要迭代精煉與準確性的場景中表現出色：

1. **以正確性為先的環境：** 在合規檢查、法規分析或法律研究中，agentic模型能反覆驗證事實、諮詢多重來源並重寫查詢，直到產出徹底審核的答案。
2. **複雜數據庫交互：** 面對結構化數據且查詢常失敗或需要調整時，系統能自主使用Azure SQL或Microsoft Fabric OneLake優化查詢，確保最終檢索結果符合用戶意圖。
3. **長工作流程：** 長時間執行的會話隨著新資訊出現而演變。Agentic RAG能持續融合新數據，隨著對問題域的加深理解調整策略。

## 治理、透明度與信任

隨著這些系統在推理上的自主性提升，治理與透明度變得關鍵：

- **可解釋推理：** 模型能提供查詢記錄、諮詢過的來源和推理步驟的審計軌跡。Azure AI Content Safety與Azure AI Tracing / GenAIOps等工具有助於維持透明度並降低風險。
- **偏差控制與平衡檢索：** 開發者可以調整檢索策略，確保考慮平衡且具代表性的數據來源，並定期使用自訂模型在Azure Machine Learning環境中審核輸出，偵測偏差或失衡模式。
- **人工監督與合規：** 對於敏感任務，人工審查依然必不可少。Agentic RAG不取代人在高風險決策中的判斷，而是透過提供更徹底審核的選項來輔助。

有能提供行為清晰記錄的工具至關重要。缺少這些，調試多步流程將非常困難。以下為Literal AI（Chainlit背後公司）提供的代理運行範例：

![AgentRunExample](../../../translated_images/zh-MO/AgentRunExample.471a94bc40cbdc0c.webp)

## 結論

Agentic RAG代表了AI系統處理複雜、數據密集任務的自然演進。透過採用循環互動模式、自主選擇工具並持續優化查詢直到達成高品質結果，系統超越了靜態依提示執行，成為更具適應性、情境感知的決策者。雖仍受限於人為定義的基礎設施與道德指引，這些agentic能力讓企業和終端用戶獲得更豐富、更動態、也更實用的AI互動體驗。

### 對Agentic RAG有更多問題嗎？

加入[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學員交流，參加辦公時間，並解答您的AI代理問題。

## 額外資源

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">使用Azure OpenAI服務實作檢索增強生成（RAG）：學習如何與Azure OpenAI服務一起使用您自己的數據。本Microsoft Learn模組提供實作RAG的全面指南</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">使用Microsoft Foundry評估生成式AI應用：本文涵蓋公開資料集上模型的評估與比較，包括Agentic AI應用和RAG架構</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">什麼是Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG：基於代理的檢索增強生成完整指南 – generation RAG新聞</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG：透過查詢重構和自我查詢加速你的 RAG！Hugging Face 開源 AI 食譜</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">向 RAG 添加代理層</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">知識助理的未來：Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">如何建立代理式 RAG 系統</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">使用 Microsoft Foundry 代理服務擴展你的 AI 代理</a>

### 學術論文

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 自我精煉：帶有自我反饋的迭代精煉</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 反思：帶有語言強化學習的語言代理</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC：大型語言模型可通過工具互動批評自我糾正</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 代理檢索增強生成：代理式 RAG 調查</a>

## 簡易測試此代理（可選）

在你學會如何在 [Lesson 16](../16-deploying-scalable-agents/README.md) 中部署代理後，可以使用 [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) 對本課的 `TravelRAGAgent` 進行簡易測試，檢查其回答是否依據知識庫。請參閱 [`tests/README.md`](../tests/README.md) 瞭解如何運行測試。

## 上一課

[工具使用設計模式](../04-tool-use/README.md)

## 下一課

[建立可信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->