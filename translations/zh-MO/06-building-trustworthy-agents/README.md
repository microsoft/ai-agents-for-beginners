[![Trustworthy AI Agents](../../../translated_images/zh-MO/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(點擊上方圖片觀看本課視頻)_

# 建立可信賴的 AI 代理

## 簡介

本課將涵蓋：

- 如何構建和部署安全且有效的 AI 代理
- 開發 AI 代理時的重要安全考慮
- 開發 AI 代理時如何維護資料和使用者隱私

## 學習目標

完成本課後，你將會知道如何：

- 識別並減緩建立 AI 代理時的風險
- 實施安全措施，確保資料和存取權限得到適當管理
- 創建維護資料隱私並提供優質使用者體驗的 AI 代理

## 安全性

讓我們先了解如何打造安全的代理應用。安全性意味著 AI 代理的表現符合設計。作為代理應用的開發者，我們有方法和工具來最大化安全性：

### 建立系統訊息架構

如果你曾用大型語言模型（LLMs）建構 AI 應用，會知道設計堅固系統提示或系統訊息的重要性。這些提示設定了後設規則、指示和指引，決定 LLM 如何與使用者和資料互動。

對 AI 代理而言，系統提示更加重要，因為 AI 代理需要非常具體的指示來完成我們為其設計的任務。

為了建立可擴展的系統提示，我們可以使用系統訊息架構來打造應用中一個或多個代理：

![Building a System Message Framework](../../../translated_images/zh-MO/system-message-framework.3a97368c92d11d68.webp)

#### 步驟 1：創建後設系統訊息

後設提示將由 LLM 使用來生成我們創建代理的系統提示。我們將它設計成範本，以便有效率地創建多個代理（如有需要）。

以下是一個會給 LLM 的後設系統訊息範例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 步驟 2：創建基本提示

下一步是創建一個基本提示來描述 AI 代理。你應該包含代理的角色、代理將完成的任務，以及代理的其他責任。

以下是一個範例：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 步驟 3：向 LLM 提供基本系統訊息

現在，我們可以優化這個系統訊息，方法是將後設系統訊息作為系統訊息，並加上我們的基本系統訊息。

這將產生更適合引導我們 AI 代理的系統訊息：

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

#### 步驟 4：迭代與改進

此系統訊息架構的價值在於能輕鬆擴展多個代理的系統訊息創建，並隨時間改善系統訊息。幾乎不會有系統訊息在第一次就能完全符合你的使用案例。能夠用小幅度調整和改進基本系統訊息並透過系統運行，將讓你可以比較和評估結果。

## 理解威脅

要建立可信賴的 AI 代理，了解並減輕對 AI 代理的風險與威脅非常重要。讓我們來看看部分不同的 AI 代理威脅，以及你如何更好規劃與準備。

![Understanding Threats](../../../translated_images/zh-MO/understanding-threats.89edeada8a97fc0f.webp)

### 任務和指令

**描述：** 攻擊者試圖通過提示或操控輸入來改變 AI 代理的指令或目標。

<strong>緩解方法</strong>：執行驗證檢查和輸入過濾，偵測潛在危險的提示，並在其被 AI 代理處理前阻止。由於這種攻擊通常需要頻繁與代理互動，限制對話回合數也是防止此類攻擊的方法之一。

### 存取關鍵系統

**描述：** 如果 AI 代理能存取存有敏感資料的系統和服務，攻擊者可能入侵代理與這些服務間的通訊。可能是直接攻擊，也可能是透過代理嘗試獲取有關這些系統的資訊。

**緩解方法：** 應限制 AI 代理對系統的存取權限，只能按需取得，以防止此類攻擊。代理與系統間的通訊也應保持安全。實施身份驗證和存取控制也是保護這些資訊的方式。

### 資源和服務過載

**描述：** AI 代理可存取不同工具和服務完成任務。攻擊者可利用此能力，透過 AI 代理發送大量請求攻擊這些服務，可能導致系統失效或高額成本。

**緩解方法：** 實施政策限制 AI 代理向服務發送請求的數量。限制對話回合數和向 AI 代理發出請求數量也是防止這類攻擊的方式之一。

### 知識庫中毒

**描述：** 此類攻擊不直接針對 AI 代理，而是針對代理使用的知識庫及其他服務。可能透過破壞代理資料或資訊，造成代理對使用者產生偏頗或非預期回應。

**緩解方法：** 定期驗證 AI 代理工作流程中所使用的資料。確保資料存取安全，僅由信任的個人變更，以避免此類攻擊。

### 連鎖錯誤

**描述：** AI 代理存取多種工具和服務完成任務。攻擊者造成的錯誤可能導致代理連結的其他系統出現故障，造成攻擊擴散且難以排查。

<strong>緩解方法</strong>：一種方法是讓 AI 代理在受限環境運作，例如在 Docker 容器中執行任務，避免直接系統攻擊。建立錯誤回退機制和重試邏輯，當某些系統回傳錯誤時，防止更大規模系統故障。

## 人類在迴路中

另一種建立可信賴 AI 代理系統的有效方式是使用「人類在迴路中」。這建立一個流程，使用者能在代理運作時提供回饋。使用者本質上作為多代理系統中的代理，對運行中的程序給予批准或終止。

![Human in The Loop](../../../translated_images/zh-MO/human-in-the-loop.5f0068a678f62f4f.webp)

以下為示範使用 Microsoft Agent Framework 實作此概念的程式碼片段：

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 建立帶有人工審批的提供者
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# 建立帶有人工作審批步驟的代理
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# 使用者可以審核並批准回應
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 結論

建立可信賴的 AI 代理需要謹慎設計、強健的安全措施和持續迭代。透過實施結構化的後設提示系統、理解潛在威脅並採用緩解策略，開發者能創造既安全又有效的 AI 代理。此外，採用人類在迴路中方法確保 AI 代理與使用者需求保持一致，同時降低風險。隨著 AI 持續發展，保持對安全、隱私和倫理的積極態度，將是促進 AI 驅動系統可信賴與可靠的關鍵。

## 程式碼範例

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb)：後設提示系統訊息架構的逐步示範。
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb)：可信賴代理的事前批准門檻、風險分級和稽核紀錄。

### 對建立可信賴 AI 代理有更多疑問？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流，參加諮詢時間，並獲得 AI 代理相關疑問的解答。

## 額外資源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">負責任 AI 概述</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式 AI 模型與 AI 應用的評估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全系統訊息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">風險評估範本</a>

## 上一課

[Agentic RAG](../05-agentic-rag/README.md)

## 下一課

[規劃設計範式](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->