[![值得信賴的 AI 代理](../../../translated_images/zh-HK/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(點擊上方圖片觀看本課程影片)_

# 建立值得信賴的 AI 代理

## 介紹

本課程將涵蓋：

- 如何構建和部署安全且有效的 AI 代理
- 開發 AI 代理時的重要安全考量
- 在開發 AI 代理時如何維護數據和用戶隱私

## 學習目標

完成本課程後，您將能夠：

- 識別並減輕創建 AI 代理時的風險
- 實施安全措施以確保數據和訪問權限得以妥善管理
- 創建能維護數據隱私並提供優質用戶體驗的 AI 代理

## 安全性

首先來看看如何建立安全的代理應用程式。安全性意味著 AI 代理按設計執行。作為代理應用程式的構建者，我們有方法和工具可最大化安全性：

### 建立系統訊息框架

如果您曾經使用大型語言模型（LLM）開發 AI 應用，您會明白設計強健系統提示或系統訊息的重要性。這些提示建立了元規則、指令和指南，指示 LLM 如何與用戶和數據互動。

對 AI 代理而言，系統提示更為重要，因為 AI 代理需要高度具體的指令來完成我們設計的任務。

為了創建可擴展的系統提示，我們可以使用系統訊息框架來在應用中打造一個或多個代理：

![建立系統訊息框架](../../../translated_images/zh-HK/system-message-framework.3a97368c92d11d68.webp)

#### 第一步：建立元系統訊息

元提示將由 LLM 用於生成我們創建的代理的系統提示。我們將其設計為範本，以便必要時能高效創建多個代理。

以下是我們會給予 LLM 的元系統訊息範例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 第二步：建立基本提示

接下來建立基本提示來描述 AI 代理。您應該包括代理的角色、代理將完成的任務以及代理的其他責任。

以下是範例：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 第三步：向 LLM 提供基本系統訊息

現在我們可以通過提供元系統訊息作為系統訊息以及我們的基本系統訊息來優化此系統訊息。

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

#### 第四步：迭代與改進

此系統訊息框架的價值在於能更輕鬆地擴展多個代理的系統訊息創建，並隨時間改善您的系統訊息。很少有系統訊息能首次就完全符合您的用例。能透過變更基本系統訊息並重新執行系統來進行小幅調整和改進，讓您可以比較並評估結果。

## 理解威脅

要建立值得信賴的 AI 代理，理解並減輕對 AI 代理的風險與威脅非常重要。以下只介紹部分對 AI 代理的不同威脅，以及您如何更好地規劃和準備。

![理解威脅](../../../translated_images/zh-HK/understanding-threats.89edeada8a97fc0f.webp)

### 任務與指令

**說明：** 攻擊者試圖通過提示或操控輸入來更改 AI 代理的指令或目標。

**緩解做法：** 執行驗證檢查和輸入過濾，以在處理前偵測可能危險的提示。由於此類攻擊常需要頻繁與代理互動，限制對話輪數是防止此類攻擊的另一種方式。

### 存取關鍵系統

**說明：** 如果 AI 代理能存取儲存敏感數據的系統與服務，攻擊者可能會破壞代理與這些服務間的通訊。這可包含直接攻擊或通過代理間接獲取系統資訊的嘗試。

**緩解做法：** AI 代理應只在必要時存取系統，以防止此類攻擊。代理與系統的通訊也應安全。實施身份驗證和存取控制是保護此資訊的另一方式。

### 資源與服務過載

**說明：** AI 代理可存取不同工具和服務來完成任務。攻擊者可能利用此能力通過 AI 代理向這些服務發送大量請求，導致系統故障或高額費用。

**緩解做法：** 實施政策限制 AI 代理對服務的請求數量。限制對 AI 代理的對話輪數和請求次數也是預防此類攻擊的方式。

### 知識庫污染

**說明：** 此攻擊不直接針對 AI 代理，而是針對 AI 代理將使用的知識庫及其他服務。可能涉及破壞 AI 代理用於完成任務的資料或資訊，導致對用戶產生偏頗或非預期的回應。

**緩解做法：** 經常驗證 AI 代理在工作流程中使用的資料。確保該資料存取安全，僅由受信任人員變更，以避免此類攻擊。

### 連鎖錯誤

**說明：** AI 代理存取各種工具和服務完成任務。攻擊者引起的錯誤可能導致 AI 代理連接的其他系統失效，令攻擊範圍更廣且更難排查。

**緩解做法：** 一種做法是讓 AI 代理在受限環境中運作，例如在 Docker 容器中執行任務，以防止直接系統攻擊。當某些系統回應錯誤時，設計後備機制和重試邏輯也是防止更大系統故障的方式。

## 人類介入循環

另一種有效建立值得信賴 AI 代理系統的方法是使用人類介入循環（Human-in-the-loop）。此流程允許用戶在執行過程中向代理提供反饋。用戶本質上在多代理系統中充當代理，可以批准或終止運行中的程序。

![人類介入循環](../../../translated_images/zh-HK/human-in-the-loop.5f0068a678f62f4f.webp)

以下是一段使用 Microsoft Agent Framework 展示此概念實作的程式碼片段：

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 建立一個具有人類審核流程的提供者
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# 建立一個包含人類審核步驟的代理
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# 使用者可以審查並批准回應
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 結論

建立值得信賴的 AI 代理需要謹慎設計、強健的安全措施及持續迭代。透過實施結構化元提示系統、理解潛在威脅並應用緩解策略，開發者能打造既安全又有效的 AI 代理。此外，結合人類介入循環方法能確保 AI 代理持續符合用戶需求，同時降低風險。隨著 AI 持續演進，維持對安全、隱私和倫理考量的前瞻性態度，將是培養 AI 驅動系統信任與可靠性的關鍵。

## 程式碼範例

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb)：元提示系統訊息框架逐步示範。
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb)：預先動作批准門檻、風險分級與可信賴代理的審計日誌。

### 對建立值得信賴的 AI 代理有更多問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流，參加辦公時間並獲得 AI 代理相關問題的解答。

## 其他資源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">負責任 AI 概覽</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式 AI 模型及 AI 應用評估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全性系統訊息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">風險評估範本</a>

## 前一課程

[代理式 RAG](../05-agentic-rag/README.md)

## 下一課程

[規劃設計模式](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->