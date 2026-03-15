# AI 代理在生產環境：可觀察性與評估

[![AI Agents in Production](../../../translated_images/zh-MO/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

隨著 AI 代理從實驗原型移向真實世界的應用，理解其行為、監測其效能、以及系統性地評估其輸出變得很重要。

## 學習目標

完成本課後，您將會知道/理解：
- 代理可觀察性與評估的核心概念
- 提升代理效能、成本與效果的技術
- 系統性地評估 AI 代理的內容與方法
- 在將 AI 代理部署到生產環境時如何控制成本
- 如何為使用 Microsoft Agent Framework 所建立的代理加入量測

目標是讓您具備把「黑盒」代理轉變為透明、可管理且值得信賴系統的知識。

_**注意：** 部署安全且值得信賴的 AI 代理非常重要。也請參考 [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md) 課程。_

## 追蹤與跨度

觀察工具例如 [Langfuse](https://langfuse.com/) 或 [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) 通常會把代理運行表示為追蹤（traces）和跨度（spans）。

- **Trace（追蹤）** 代表從開始到結束的一個完整代理任務（例如處理一個使用者查詢）。
- **Spans（跨度）** 是追蹤內的個別步驟（例如呼叫語言模型或檢索資料）。

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

沒有可觀察性時，AI 代理會像一個「黑盒」——其內部狀態與推理是不透明的，導致難以診斷問題或優化效能。有了可觀察性，代理會變成「玻璃盒」，提供建立信任與確保其如預期運作所需的透明度。

## 為何在生產環境中可觀察性很重要

將 AI 代理移到生產環境會帶來一系列新的挑戰與需求。可觀察性不再是「可有可無」，而是一項關鍵能力：

*   **除錯與根本原因分析**：當代理失敗或產生意外輸出時，可觀察性工具提供所需的追蹤來釐清錯誤來源。在可能涉及多次 LLM 呼叫、工具互動與條件邏輯的複雜代理中，這尤其重要。
*   **延遲與成本管理**：AI 代理常依賴按 token 或按呼叫計費的 LLM 與其他外部 API。可觀察性可以精確追蹤這些呼叫，有助於找出過慢或過於昂貴的操作。這能讓團隊優化 prompts、選擇更有效率的模型或重新設計工作流程，以管理營運成本並確保良好的使用者體驗。
*   **信任、安全與合規**：在許多應用中，確保代理行為安全且符合道德非常重要。可觀察性提供代理行動與決策的審計痕跡。這可用來偵測並緩解像是 prompt 注入、產生有害內容或不當處理個人可識別資訊（PII）等問題。例如，您可以檢視追蹤以了解代理為何提供某個回應或使用特定工具。
*   **持續改進迴圈**：可觀察性資料是反覆式開發流程的基礎。透過監控代理在真實世界中的表現，團隊可以找出改進的方向、收集微調模型的資料，並驗證更動的影響。這會建立一個反饋迴圈，將來自線上評估的生產洞見用於離線實驗與改良，逐步提升代理效能。

## 需要追蹤的關鍵指標

為了監控並理解代理行為，應該追蹤一系列指標與訊號。雖然具體指標會根據代理的目的有所不同，但有些是普遍重要的。

以下是可觀察性工具通常會監控的一些常見指標：

**Latency（延遲）：** 代理回應的速度如何？過長的等待時間會負面影響使用者體驗。您應透過追蹤代理運行來測量任務與各個步驟的延遲。例如，一個代理所有模型呼叫合計需 20 秒，可能可透過使用較快的模型或並行處理模型呼叫來加速。

**Costs（成本）：** 每次代理執行的花費為何？AI 代理依賴按 token 計費的 LLM 呼叫或外部 API。頻繁使用工具或多次 prompt 會快速提高成本。例如，如果代理為了微幅品質提升呼叫 LLM 五次，就必須評估成本是否合理，或者是否能減少呼叫次數或使用更便宜的模型。即時監控也能幫助識別意外的尖峰（例如程式錯誤導致過度 API 迴圈）。

**Request Errors（請求錯誤）：** 代理失敗的請求有多少？這可能包括 API 錯誤或工具呼叫失敗。為了讓代理在生產環境中更穩健，您可以設置後備或重試機制。例如如果 LLM 提供者 A 故障，您可以切換到 LLM 提供者 B 作為備援。

**User Feedback（使用者回饋）：** 實作直接的使用者評估能提供有價值的洞見。這可以包括明確評分（👍thumbs-up/👎down、⭐1-5 星）或文字評論。持續性的負面回饋應該提醒您，這可能表示代理未如預期運作。

**Implicit User Feedback（隱含使用者回饋）：** 使用者行為即使沒有明確評分也會提供間接回饋。這可能包括立即重述問題、重複查詢或點擊重試按鈕。例如，如果您看到使用者反覆詢問同一問題，這就是代理未如預期工作的徵兆。

**Accuracy（準確性）：** 代理產生正確或期望輸出的頻率如何？準確性的定義會有所不同（例如問題解決的正確性、資訊檢索的準確性、使用者滿意度）。第一步是為您的代理定義成功的樣貌。您可以透過自動檢查、評分或任務完成標籤來追蹤準確性。例如，將追蹤標示為「succeeded」或「failed」。

**Automated Evaluation Metrics（自動化評估指標）：** 您也可以設定自動化評估。例如，使用 LLM 為代理的輸出打分（例如是否有幫助、是否準確等）。也有若干開源函式庫可以協助評分代理的不同面向，例如用於 RAG 代理的 [RAGAS](https://docs.ragas.io/) 或用於偵測有害語言或 prompt 注入的 [LLM Guard](https://llm-guard.com/)。

在實務上，這些指標的組合能提供對 AI 代理健康狀態的最佳覆蓋。在本章的 [example notebook](./code_samples/10-expense_claim-demo.ipynb) 範例中，我們會示範這些指標在真實範例中的樣貌，但首先我們會學習典型的評估工作流程。

## 為您的代理加入量測

要收集追蹤資料，您需要為程式加入量測。目標是為代理程式碼加入量測以發出可被觀察平台捕捉、處理與視覺化的追蹤與指標。

**OpenTelemetry (OTel)：** [OpenTelemetry](https://opentelemetry.io/) 已成為 LLM 可觀察性的產業標準。它提供一套 API、SDK 與工具來產生、收集與匯出遙測資料。

有許多封裝現有代理框架並讓匯出 OpenTelemetry spans 到觀察工具變得簡單的量測庫。Microsoft Agent Framework 原生整合 OpenTelemetry。以下示範如何為 MAF 代理加入量測：

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # 代理的執行會自動被追蹤
    pass
```

本章的 [example notebook](./code_samples/10-expense_claim-demo.ipynb) 將示範如何為您的 MAF 代理加入量測。

**手動建立 Span：** 雖然量測庫提供了良好的基線，但常常會有需要更詳細或自訂資訊的情況。您可以手動建立 spans 來加入自訂的應用程式邏輯。更重要的是，您可以為自動或手動建立的 spans 增加自訂屬性（也稱為標籤或 metadata）。這些屬性可以包含商業特定的資料、中間運算結果或任何對除錯或分析有用的上下文，例如 `user_id`、`session_id` 或 `model_version`。

以下示範如何使用 [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) 手動建立追蹤與跨度：

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## 代理評估

可觀察性提供我們指標，但評估是分析這些資料（與執行測試）以判斷 AI 代理表現良好與否並找出改善方式的過程。換句話說，一旦擁有那些追蹤與指標，您要如何使用它們來評斷代理並做出決策？

定期評估很重要，因為 AI 代理通常具有非決定性，且會隨著更新或模型行為漂移而演變——沒有評估，您不會知道您的「智慧代理」是否真的在做好其工作，或是否出現了退步。

AI 代理的評估主要分為兩類：**線上評估（online evaluation）** 與 **離線評估（offline evaluation）**。兩者都很有價值，互為補充。我們通常從離線評估開始，因為這是在部署任何代理前的最低必要步驟。

### 離線評估

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

這涉及在受控環境下評估代理，通常使用測試資料集，而非即時使用者查詢。您使用已策劃的資料集，在那裡您知道期望的輸出或正確行為，然後在這些資料上執行代理。

例如，如果您建立了一個數學文字題代理，您可能有一個包含 100 題且答案已知的 [test dataset](https://huggingface.co/datasets/gsm8k)。離線評估常在開發期間進行（並可作為 CI/CD 管線的一部分），用以檢查改進或防止回歸。其好處是 **可重複，且由於有真實答案可以得到明確的準確性指標**。您也可能模擬使用者查詢，並將代理回應與理想答案比較，或使用前述的自動化指標來衡量。

離線評估的主要挑戰是確保您的測試資料集具有全面性並保持相關性——代理可能在固定的測試集上表現良好，但在生產中遇到截然不同的查詢。因此，您應該持續更新測試集，加入反映真實場景的新邊緣案例與範例。小型的「冒煙測試」案例與較大的評估集混合使用很有用：小集合用於快速檢查，較大集合用於更廣泛的性能指標。

### 線上評估

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

這指的是在實際、真實環境中（即生產中實際使用時）對代理進行評估。線上評估涉及監控代理在真實使用者互動中的表現並持續分析結果。

例如，您可能會追蹤成功率、使用者滿意度分數或其他對線上流量的指標。線上評估的優點是它 **能捕捉您在實驗室設定中可能無法預見的情況**——您可以觀察模型隨時間漂移（如果隨著輸入模式變動代理效能下降）並發現未納入測試資料中的意外查詢或情境。它提供代理在真實世界中行為的真實畫面。

線上評估通常涉及收集隱含與明確的使用者回饋（如前述），並可能執行 shadow 測試或 A/B 測試（讓新版本代理與舊版本並行運行以進行比較）。挑戰在於要為線上互動取得可靠的標籤或分數可能很棘手——您可能需依賴使用者回饋或下游指標（例如使用者是否點擊結果）。

### 結合兩者

線上與離線評估並不互斥；它們高度互補。線上監控的洞見（例如代理在某些新型態使用者查詢上的低效表現）可以用來增強與改進離線測試資料集。反過來，離線測試表現良好的代理可以更有信心地部署並在上線後監控。

事實上，許多團隊採用一個循環流程：

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_。

## 常見問題

當您將 AI 代理部署到生產環境時，可能會遇到各種挑戰。以下是一些常見問題及其潛在解決方案：

| **Issue**    | **Potential Solution**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - 精煉給 AI 代理的 prompt；明確目標。<br>- 確認是否能將任務拆成子任務並由多個代理處理以改善情況。 |
| AI Agent running into continuous loops  | - 確保您有明確的終止條件與規則，讓代理知道何時停止流程。<br>- 對於需要推理與規劃的複雜任務，使用較擅長推理任務的較大型模型。 |
| AI Agent tool calls are not performing well   | - 在代理系統外測試並驗證工具的輸出。<br>- 精煉工具的參數定義、prompts 與命名。  |
| Multi-Agent system not performing consistently | - 精煉給每個代理的 prompts，確保它們明確且彼此不同。<br>- 使用「路由」或控制器代理建立階層式系統，以決定哪個代理最適合處理某個任務。 |

許多這類問題在有可觀察性時能更有效地被識別。我們先前討論的追蹤與指標有助於精確指出代理工作流程中問題出現的位置，讓除錯與優化更有效率。

## 成本管理
以下是一些管理將 AI 代理部署到生產環境成本的策略：

**使用較小的模型：** Small Language Models (SLMs) 在某些代理使用情境中表現良好，並能顯著降低成本。如前所述，建立一個評估系統以判定並比較與較大模型的效能，是了解 SLM 在您的使用情境中表現的最佳方式。考慮在較簡單的任務（例如意圖分類或參數抽取）中使用 SLM，而將較大型模型保留給複雜推理。

**使用路由模型：** 類似的策略是使用多樣化的模型與規模。您可以使用 LLM/SLM 或無伺服器函數，根據請求的複雜度將請求路由到最合適的模型。這不僅有助於降低成本，同時也能確保在合適的任務上達到效能。例如，將簡單查詢路由到較小、較快的模型，只有在需要複雜推理時才使用昂貴的大型模型。

**快取回應：** 識別常見請求與任務，並在它們經由您的代理系統之前提供回應，是減少相似請求量的好方法。您甚至可以實作一個流程，使用較基礎的 AI 模型來判定一個請求與您快取的請求之相似程度。對於常見問題或常見工作流程，這個策略可大幅降低成本。

## 讓我們看看這在實務上如何運作

在[本節的範例筆記本](./code_samples/10-expense_claim-demo.ipynb)中，我們會看到一些範例，展示如何使用可觀察性工具來監控和評估我們的代理。


### 對在生產環境中的 AI 代理還有更多問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者見面、參加諮詢時段並獲得您關於 AI 代理的問題解答。

## 上一課

[後設認知設計模式](../09-metacognition/README.md)

## 下一課

[代理協議](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件之翻譯係使用 AI 翻譯服務 Co-op Translator（https://github.com/Azure/co-op-translator）所產出。雖然我們力求準確，但自動翻譯可能含有錯誤或不準確之處。原始語言版本應視為具權威性的版本。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->