[![值得信賴的 AI 代理](../../../translated_images/zh-MO/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(點擊上方圖片觀看本課程影片)_

# 建立值得信賴的 AI 代理

## 簡介

本課程將涵蓋：

- 如何建立及部署安全且有效的 AI 代理
- 開發 AI 代理時的重要安全考量
- 開發 AI 代理時如何維護數據和使用者隱私

## 學習目標

完成本課程後，您將能夠：

- 在建立 AI 代理時識別並減輕風險
- 實施安全措施，確保數據和存取權限妥善管理
- 創建維護數據隱私且提供優質使用者體驗的 AI 代理

## 安全性

首先讓我們看看如何建立安全的代理應用程式。安全性意味著 AI 代理如預期般運作。作為代理應用的開發者，我們擁有方法和工具來最大化安全性：

### 建立系統訊息架構

如果您曾使用大型語言模型（LLMs）建立 AI 應用，您應該知道設計堅固系統提示或系統訊息的重要性。這些提示建立了 LLM 如何與使用者及數據互動的元規則、指令和指南。

對於 AI 代理而言，系統提示更為重要，因為 AI 代理需要非常具體的指令來完成我們設計的任務。

為了創建可擴展的系統提示，我們可以使用系統訊息架構來構建應用中一個或多個代理：

![建立系統訊息架構](../../../translated_images/zh-MO/system-message-framework.3a97368c92d11d68.webp)

#### 步驟 1：建立元系統訊息

元提示將由 LLM 用來產生我們所創建代理的系統提示。我們設計它作為一個範本，使得若有需要時可以有效率地創建多個代理。

這裡是一個我們會給 LLM 的元系統訊息範例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 步驟 2：建立基本提示

下一步是建立描述 AI 代理的基本提示。您應包含代理的角色、代理會完成的任務，以及代理的任何其他職責。

這是一個範例：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 步驟 3：向 LLM 提供基本系統訊息

現在我們可以透過提供元系統訊息作為系統訊息以及我們的基本系統訊息來優化此系統訊息。

這將產生更適合指引我們 AI 代理的系統訊息：

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### 步驟 4：反覆改進

此系統訊息架構的價值在於能夠更容易擴展多個代理系統訊息的創建，並隨時間改進您的系統訊息。您通常不會首次就擁有適合完整使用場景的系統訊息。能藉由修改基本系統訊息並透過系統執行，進行小幅調整和改進，從而比較及評估結果，是非常重要的。

## 了解威脅

為了建立值得信賴的 AI 代理，理解並減輕對 AI 代理的風險和威脅至關重要。讓我們來看幾種不同的 AI 代理威脅，以及您如何更好地規劃和準備應對它們。

![了解威脅](../../../translated_images/zh-MO/understanding-threats.89edeada8a97fc0f.webp)

### 任務與指令

**描述：** 攻擊者透過提示或操縱輸入嘗試更改 AI 代理的指令或目標。

**緩解措施：** 執行驗證檢查及輸入過濾，於 AI 代理處理之前偵測潛在危險的提示。由於這類攻擊通常需要頻繁與代理互動，限制對話輪數也是防止此類攻擊的方法之一。

### 存取關鍵系統

**描述：** 若 AI 代理可訪問儲存敏感資料的系統與服務，攻擊者可能會破壞代理與這些服務間的通訊。這可能是直接攻擊或透過代理間接試圖獲取這些系統資訊。

**緩解措施：** AI 代理應僅在必要時存取系統，以防這類攻擊。代理與系統間的通訊也應保障安全。實施驗證及存取控制是保護資訊的另一方法。

### 資源與服務超載

**描述：** AI 代理可訪問不同工具和服務完成任務。攻擊者可能利用此能力透過 AI 代理發送大量請求攻擊這些服務，導致系統故障或高額成本。

**緩解措施：** 制定政策限制 AI 代理對服務的請求數量。限制與 AI 代理對話輪數及請求數也是防止此類攻擊的方法。

### 知識庫污染

**描述：** 此類攻擊不直接針對 AI 代理，而是攻擊 AI 代理使用的知識庫及其它服務。可能涉及污染代理用來完成任務的資料，導致對使用者產生偏頗或非預期回應。

**緩解措施：** 定期驗證 AI 代理在其工作流程中使用的資料。確保該資料存取安全且僅由可信人員更改，以避免此類攻擊。

### 鏈式錯誤

**描述：** AI 代理訪問多種工具與服務完成任務。攻擊者引起的錯誤可導致連接系統故障，使攻擊擴散且更難排查。

**緩解措施：** 一種方法是使 AI 代理在受限制的環境中執行，例如在 Docker 容器內執行任務，避免直接系統攻擊。當特定系統回傳錯誤時，建立備援機制與重試邏輯是防止更大系統故障的另一方式。

## 人機協同

建立值得信賴 AI 代理系統的另一有效方法是使用人機協同。此方法讓使用者能在代理運行時提供回饋。使用者基本上在多代理系統中扮演代理角色，透過批准或終止運行程序來參與。

![人機協同](../../../translated_images/zh-MO/human-in-the-loop.5f0068a678f62f4f.webp)

這裡示範使用 Microsoft Agent Framework 實現此概念的程式碼片段：

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# 建立具有人類審批流程的供應者
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 建立帶有人工審批步驟的代理
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# 使用者可以審閱並批准回應
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 結論

建立值得信賴的 AI 代理需要細緻設計、強健的安全措施與持續迭代。透過實施結構化元提示系統、理解潛在威脅及採取緩解策略，開發者能創建既安全又有效的 AI 代理。此外，結合人機協同方法確保 AI 代理始終符合使用者需求並減少風險。隨著 AI 持續發展，積極維持安全、隱私及倫理考量將是促進 AI 驅動系統信任與可靠性的關鍵。

## 程式碼範例

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb)：元提示系統訊息架構的逐步示範。
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb)：可信代理的前置批准閘、風險分層與稽核紀錄。

### 對建立值得信賴 AI 代理有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加諮詢時間並獲得 AI 代理相關問題解答。

## 額外資源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">負責任的 AI 概述</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式 AI 模型及 AI 應用評估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全性系統訊息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">風險評估範本</a>

## 上一課

[Agentic RAG](../05-agentic-rag/README.md)

## 下一課

[計劃設計模式](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->