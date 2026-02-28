# 生產環境中的 AI 代理：可觀察性與評估

[![生產環境中的 AI 代理](../../../translated_images/zh-TW/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

隨著 AI 代理從實驗性原型走向真實世界應用，了解其行為、監控其效能以及系統性地評估其輸出變得越來越重要。

## 學習目標

完成本課程後，您將了解/會做：
- 代理可觀察性與評估的核心概念
- 改善代理效能、成本與有效性的技術
- 以系統化方式評估您的 AI 代理的項目與方法
- 在將 AI 代理部署到生產環境時如何控制成本
- 如何對使用 Microsoft Agent Framework 建構的代理進行儀表化

目標是讓您具備將「黑盒」代理轉變為透明、可管理且可靠系統的知識。

_**注意：** 部署安全且值得信賴的 AI 代理非常重要。也請參閱 [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md) 課程。_

## 跟蹤與跨度

像 [Langfuse](https://langfuse.com/) 或 [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) 這類可觀察性工具通常將代理執行表示為 traces 和 spans。

- **Trace** 代表從開始到結束的一個完整代理任務（例如處理一個使用者查詢）。
- **Spans** 是 trace 中的單一步驟（例如呼叫語言模型或檢索資料）。

![Langfuse 中的追蹤樹狀圖](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

沒有可觀察性時，AI 代理會感覺像個「黑盒」——其內部狀態與推理不透明，會使診斷問題或優化效能變得困難。有了可觀察性，代理就變成「玻璃盒」，提供的透明度對建立信任並確保它們按預期運作至關重要。

## 為什麼在生產環境中可觀察性很重要

將 AI 代理轉入生產環境會帶來一組新的挑戰與需求。可觀察性不再是「可有可無」，而是一項關鍵能力：

*   **除錯與根因分析**：當代理失敗或產生意外輸出時，可觀察性工具提供定位錯誤來源所需的 trace。這在可能涉及多次 LLM 呼叫、工具互動與條件邏輯的複雜代理中尤其重要。
*   **延遲與成本管理**：AI 代理通常依賴按 token 或按次計費的 LLM 與其他外部 API。可觀察性允許精確追蹤這些呼叫，有助於識別過慢或過於昂貴的操作。這使團隊能優化提示、選擇更有效率的模型或重新設計工作流程，以管理營運成本並確保良好的使用者體驗。
*   **信任、安全與合規**：在許多應用中，確保代理安全且合乎倫理行為非常重要。可觀察性提供代理行為與決策的稽核軌跡。這可用於偵測與緩解像提示注入、產生有害內容或錯誤處理個人識別資訊（PII）等問題。例如，您可以檢視 trace 以了解代理為何給出某個回應或使用特定工具。
*   **持續改進循環**：可觀察性資料是反覆開發流程的基礎。透過監控代理在真實世界中的表現，團隊可以找出改進空間、收集用於微調模型的資料，並驗證變更的影響。這建立了一個回饋循環：來自線上評估的生產洞察會用來指導離線實驗與改良，最終帶來越來越好的代理效能。

## 要追蹤的關鍵指標

為了監控與理解代理行為，應追蹤一系列的指標與訊號。具體指標會依代理的用途而異，但一些指標是普遍重要的。

以下是可觀察性工具常監控的一些指標：

**延遲（Latency）：** 代理回應的速度如何？長時間等待會負面影響使用者體驗。您應透過追蹤代理執行來測量任務與單一步驟的延遲。例如，一個在所有模型呼叫上花了 20 秒的代理，可以透過使用更快的模型或平行執行模型呼叫來加速。

**成本（Costs）：** 每次代理執行的花費是多少？AI 代理依賴按 token 或外部 API 計費的 LLM。頻繁使用工具或多次提示會迅速增加成本。例如，如果代理為了非常有限的品質提升而呼叫 LLM 五次，您必須評估成本是否合理，或是否可以減少呼叫次數或使用更便宜的模型。即時監控也能幫助識別意外尖峰（例如程式錯誤導致過度的 API 迴圈）。

**請求錯誤（Request Errors）：** 代理失敗了多少請求？這可能包括 API 錯誤或工具呼叫失敗。為了讓代理在生產環境中更具韌性，您可以設置備援或重試機制。例如當 LLM 供應商 A 無法使用時，切換到 LLM 供應商 B 作為備援。

**使用者回饋（User Feedback）：** 實作直接的使用者評價可提供有價值的見解。這可包括明確的評分（👍按讚/👎踩、⭐1-5 顆星）或文字評論。持續的負面回饋應發出警示，表示代理未如預期運作。

**隱含使用者回饋（Implicit User Feedback）：** 即使沒有明確評分，使用者行為也會提供間接回饋。這可包含立即重新措辭問題、重複查詢或點擊重試按鈕。例如，如果您發現使用者反覆詢問相同問題，這表示代理沒有達到預期。

**準確性（Accuracy）：** 代理產出正確或理想結果的頻率如何？準確性的定義會因情境而異（例如解題正確性、資訊檢索準確性、使用者滿意度）。第一步是定義代理的成功樣貌。您可以透過自動檢查、評分或任務完成標籤來追蹤準確性。例如，將 trace 標記為「成功」或「失敗」。

**自動化評估指標（Automated Evaluation Metrics）：** 您也可以設置自動化評估。例如，使用 LLM 為代理的輸出打分（例如是否有幫助、準確或不是）。也有幾個開源函式庫可以幫助您評分代理的不同面向，例如用於 RAG 代理的 [RAGAS](https://docs.ragas.io/) 或用來偵測有害語言或提示注入的 [LLM Guard](https://llm-guard.com/)。

在實務上，這些指標的組合能提供對 AI 代理健康狀態的最佳覆蓋。於本章的範例筆記本（./code_samples/10-expense_claim-demo.ipynb），我們將示範這些指標在真實範例中的樣貌，但在此之前，我們先學習典型的評估工作流程。

## 對您的代理進行儀表化

為了收集追蹤資料，您需要對程式碼進行儀表化。目標是使代理程式碼發出可被可觀察性平台捕獲、處理與視覺化的 trace 與指標。

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) 已成為 LLM 可觀察性的業界標準。它提供一套用於產生、收集與匯出遙測資料的 API、SDK 與工具。

有很多儀表化函式庫可以包裹現有的代理框架，並便於將 OpenTelemetry spans 匯出到可觀察性工具。Microsoft Agent Framework 與 OpenTelemetry 原生整合。以下為對 MAF 代理進行儀表化的範例：

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # 代理執行會自動被追蹤
    pass
```

本章的 [範例筆記本](./code_samples/10-expense_claim-demo.ipynb) 將示範如何對您的 MAF 代理進行儀表化。

**手動建立 Span：** 儘管儀表化函式庫提供良好的基線，但常有需要更詳細或自訂資訊的情況。您可以手動建立 spans 來加入自訂應用程式邏輯。更重要的是，您可以為自動或手動建立的 spans 增加自訂屬性（也稱為標籤或 metadata）。這些屬性可以包含業務特定的資料、中間計算或任何對除錯或分析有用的上下文，例如 `user_id`、`session_id` 或 `model_version`。

以下示例示範如何使用 [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) 手動建立 traces 與 spans：

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## 代理評估

可觀察性為我們提供指標，但評估則是分析那些資料（並執行測試）以判定 AI 代理的表現及可改進之處。換句話說，一旦您有了 trace 與指標，如何使用它們來評判代理並做出決策？

定期評估很重要，因為 AI 代理常具有非決定性，且會隨著更新或模型行為漂移而演變——若沒有評估，您無法知道您的「智慧代理」是否真的在做好它的工作，或是否已經退化。

對 AI 代理而言，有兩類評估：**線上評估（online evaluation）**與**離線評估（offline evaluation）**。兩者都有價值，且彼此互補。我們通常從離線評估開始，因為這是部署任何代理前的最基本必要步驟。

### 離線評估

![Langfuse 中的資料集項目](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

這包括在受控環境中評估代理，通常使用測試資料集，而非即時的使用者查詢。您會使用已策劃的資料集，知道預期輸出或正確行為，然後在這些資料上執行代理。

例如，如果您建立了一個數學文字題代理，您可能有一個包含已知答案的 100 題 [測試資料集](https://huggingface.co/datasets/gsm8k)。離線評估通常在開發期間進行（也可以作為 CI/CD 管線的一部分）以檢查改進或防止回歸。其好處是它是可**重複**的，且因為您有基準真值，能取得明確的準確性指標。您也可以模擬使用者查詢並將代理的回應與理想答案比對，或使用上面提到的自動化指標。

離線評估的主要挑戰是確保測試資料集完整且保持相關——代理可能在固定測試集上表現良好，但在生產環境遇到完全不同的查詢。因此，您應保持測試集隨著新的邊緣案例與反映真實情境的範例而更新。混合使用小型的「冒煙測試」案例與較大的評估集是有用的：小集合用於快速檢查，較大集合則用於更廣泛的效能衡量。

### 線上評估

![可觀察性指標總覽](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

這是指在真實、實際使用的生產環境中評估代理，也就是在實際使用過程中進行評估。線上評估包括在真實使用者互動上持續監控代理的表現並分析結果。

例如，您可能會追蹤成功率、使用者滿意度分數或其他在實際流量上的指標。線上評估的優勢在於它能**捕捉實驗室環境中無法預期的情況**——您可以觀察到隨時間的模型漂移（如果代理的效能隨輸入模式改變而下降）並捕捉到未納入測試資料的意外查詢或情境。它提供代理在真實世界中行為的真實畫面。

線上評估通常包含收集隱含與明示的使用者回饋（如前所述），並可能執行 shadow test 或 A/B 測試（讓新版本的代理與舊版本並行運行以進行比較）。挑戰在於對即時互動取得可靠標籤或分數可能很困難——您可能需要依賴使用者回饋或下游指標（例如使用者是否點擊結果）。

### 結合兩者

線上與離線評估並非互相排斥；兩者高度互補。來自線上監控的洞察（例如代理在某些新型使用者查詢上表現不佳）可以用來擴充與改進離線測試資料集。相反地，在離線測試中表現良好的代理，可以更有信心地部署並在線上監控。

事實上，許多團隊採用一個循環：

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_。

## 常見問題

當您將 AI 代理部署到生產環境時，可能會遇到各種挑戰。以下是一些常見問題及其可能的解決方法：

| **問題**    | **可能的解決方案**   |
| ------------- | ------------------ |
| AI 代理無法穩定執行任務 | - 精練給 AI 代理的提示，明確目標。<br>- 找出將任務拆分為子任務並由多個代理處理是否有幫助。 |
| AI 代理陷入無限迴圈  | - 確保您有明確的終止條件，讓代理知道何時停止流程。<br>- 對於需要推理與規劃的複雜任務，使用更擅長推理任務的大模型。 |
| AI 代理的工具呼叫表現不佳   | - 在代理系統之外測試並驗證工具的輸出。<br>- 精練工具的參數、提示與命名。  |
| 多代理系統無法穩定運作 | - 精練給每個代理的提示，確保它們是具體且彼此區別的。<br>- 使用「路由」或控制器代理建立分層系統，以決定哪個代理是正確的選擇。 |

許多這類問題在有可觀察性時能更有效率地被識別。我們先前討論的 trace 與指標能精確指出代理工作流程中問題發生的位置，讓除錯與優化效率大幅提升。

## 成本管理
Here are some strategies to manage the costs of deploying AI agents to production:

**Using Smaller Models:** 小型語言模型 (SLMs) 在某些代理式使用情境中表現良好，且能顯著降低成本。如前所述，建立一個評估系統來判定並比較與較大型模型的效能，是了解 SLM 在您使用情境中表現如何的最佳方式。考慮在較簡單的任務（例如意圖分類或參數擷取）使用 SLM，而在需要複雜推理時保留較大型模型。

**Using a Router Model:** 類似的策略是使用多樣化的模型與大小。您可以使用 LLM/SLM 或無伺服器函式來根據複雜度將請求路由到最合適的模型。這也有助於在確保正確任務的效能同時降低成本。例如，將簡單查詢路由到較小且較快的模型，僅在需要複雜推理時才使用昂貴的大型模型。

**Caching Responses:** 識別常見請求和任務，並在它們進入您的代理式系統之前先行提供回應，是減少類似請求量的好方法。您甚至可以實作一個流程，使用較基礎的 AI 模型來判斷一個請求與您快取的請求相似的程度。對於常見問題或常見工作流程，這個策略能大幅降低成本。

## Lets see how this works in practice

In the [example notebook of this section](./code_samples/10-expense_claim-demo.ipynb), we’ll see examples of how we can use observability tools to monitor and evaluate our agent.


### Got More Questions about AI Agents in Production?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Previous Lesson

[Metacognition Design Pattern](../09-metacognition/README.md)

## Next Lesson

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。以原始語言撰寫的原文應被視為具權威性的版本。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或誤釋不負任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->