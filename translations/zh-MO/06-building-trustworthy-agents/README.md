[![可靠的 AI 代理](../../../translated_images/zh-MO/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(點擊上方圖片觀看本課程影片)_

# 建立可靠的 AI 代理

## 介紹

本課程將涵蓋：

- 如何建立和部署安全且有效的 AI 代理
- 發展 AI 代理時的重要安全考量
- 發展 AI 代理時如何維護資料和使用者隱私

## 學習目標

完成本課程後，您將了解如何：

- 識別與減輕創建 AI 代理時的風險
- 實施安全措施以確保資料和存取權限的適當管理
- 創建能維護資料隱私並提供優質使用者體驗的 AI 代理

## 安全性

首先讓我們看看如何建立安全的代理應用程式。安全性意味著 AI 代理能按設計正常運作。作為代理應用程式的開發者，我們有方法和工具能最大化安全性：

### 建立系統訊息架構

如果您曾經使用大型語言模型（LLM）建立 AI 應用程式，您會知道設計強健的系統提示或系統訊息的重要性。這些提示設定了元規則、指令和指導原則，決定 LLM 如何與使用者和資料互動。

對於 AI 代理來說，系統提示更為重要，因為 AI 代理需要非常具體的指令來完成我們為其設計的任務。

為了創建可擴展的系統提示，我們可以使用系統訊息架構來建構應用程式中一個或多個代理：

![建立系統訊息架構](../../../translated_images/zh-MO/system-message-framework.3a97368c92d11d68.webp)

#### 第一步：建立元系統訊息

元提示將由 LLM 使用，以產生我們創建的代理的系統提示。我們將其設計為模板，以便在需要時高效地創建多個代理。

以下是一個我們會給 LLM 的元系統訊息範例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 第二步：建立基本提示

下一步是建立描述 AI 代理的基本提示。您應該包含代理的角色、代理將完成的任務，以及其他任何代理的責任。

這是一個範例：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 第三步：向 LLM 提供基本系統訊息

現在，我們可以透過提供元系統訊息作為系統訊息以及我們的基本系統訊息來優化這個系統訊息。

這將產生一個更適合指導我們 AI 代理的系統訊息：

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

#### 第四步：迭代與改進

這個系統訊息架構的價值在於可以更輕鬆地擴展從多個代理創建系統訊息，並且隨著時間改進您的系統訊息。您很少會在第一次就擁有適用於完整使用案例的系統訊息。能夠透過更改基本系統訊息並透過系統運行來進行微調和改進，將允許您比較和評估結果。

## 了解威脅

為了建立可信賴的 AI 代理，了解並減輕 AI 代理面臨的風險和威脅很重要。讓我們來看一些對 AI 代理的不同威脅，以及如何更好地規劃和準備。

![了解威脅](../../../translated_images/zh-MO/understanding-threats.89edeada8a97fc0f.webp)

### 任務與指令

**描述：** 攻擊者嘗試通過提示或操作輸入來改變 AI 代理的指令或目標。

**緩解措施：** 執行驗證檢查和輸入過濾，以在 AI 代理處理前偵測潛在危險的提示。由於這類攻擊通常需要頻繁與代理互動，限制對話輪數也是防止此類攻擊的方法之一。

### 訪問關鍵系統

**描述：** 如果 AI 代理能訪問存有敏感資料的系統和服務，攻擊者可能會破壞代理與這些服務間的通訊。這些攻擊可以是直接攻擊，也可能是透過代理間接嘗試取得這些系統的資訊。

**緩解措施：** AI 代理應只在必要時才能訪問這些系統，以防止此類攻擊。代理與系統間的通訊也應保持安全。實施身份驗證和存取控制是保護這些資訊的另一方法。

### 資源與服務過載

**描述：** AI 代理能存取不同的工具和服務來完成任務。攻擊者可能利用此能力通過 AI 代理發送大量請求，攻擊這些服務，導致系統故障或高昂成本。

**緩解措施：** 實施政策限制 AI 代理對服務發出的請求數量。限制對 AI 代理的對話輪數和請求數量也是防止這類攻擊的方法。

### 知識庫中毒

**描述：** 此類攻擊不直接針對 AI 代理，而是針對 AI 代理所使用的知識庫和其他服務。這可能涉及污染 AI 代理用來完成任務的資料或資訊，導致對使用者出現偏頗或非預期的回應。

**緩解措施：** 定期驗證 AI 代理在工作流程中使用的資料。確保只有可信任的人才能變更這些資料，避免此類攻擊。

### 鏈式錯誤

**描述：** AI 代理存取各種工具和服務完成任務。攻擊者引發的錯誤可能導致與 AI 代理連接的其他系統失效，使攻擊擴散且難以排查。

**緩解措施：** 一種避免方法是讓 AI 代理在限制的環境中運作，例如在 Docker 容器中執行任務，以防止直接系統攻擊。當某些系統回傳錯誤時，建立回退機制和重試邏輯也是防止較大系統故障的方式。

## 人類在迴路中

另一種有效構建可信 AI 代理系統的方法是採用人類在迴路中。這會創建一個流程，讓使用者在運行過程中能向代理提供反饋。使用者本質上在多代理系統中扮演代理角色，並通過提供批准或終止運行流程。

![人類在迴路中](../../../translated_images/zh-MO/human-in-the-loop.5f0068a678f62f4f.webp)

這裡有一段使用 Microsoft Agent Framework 的程式碼示例，展示如何實現這個概念：

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 建立具有人類審核環節的提供者
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# 建立具有人類審批步驟的代理
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# 用戶可以檢視並批准回應
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 結論

建立可靠的 AI 代理需要謹慎的設計、堅實的安全措施和持續的迭代。透過實施結構化的元提示系統、了解潛在威脅以及應用緩解策略，開發人員能創造既安全又有效的 AI 代理。此外，結合人類在迴路中的方法確保 AI 代理能持續符合使用者需求，同時將風險降至最低。隨著 AI 持續發展，維持對安全、隱私和倫理考量的主動態度將是促進 AI 驅動系統信任與可靠性的關鍵。

### 想了解更多關於建立可靠 AI 代理的問題？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者會面，參加辦公時間，獲取 AI 代理相關問題的解答。

## 額外資源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">負責任的 AI 概述</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式 AI 模型及 AI 應用評估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全系統訊息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">風險評估範本</a>

## 上一課

[代理 RAG](../05-agentic-rag/README.md)

## 下一課

[規劃設計模式](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由人工智能翻譯服務【Co-op Translator】(https://github.com/Azure/co-op-translator) 翻譯而成。儘管我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為具有權威性的來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->