[![可信賴的 AI 代理](../../../translated_images/zh-HK/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(點擊上方圖片觀看本課影片)_

# 建立可信賴的 AI 代理

## 簡介

本課程將涵蓋：

- 如何建立及部署安全且有效的 AI 代理
- 開發 AI 代理時的重要安全考量
- 開發 AI 代理時如何維護資料與用戶隱私

## 學習目標

完成本課程後，您將了解如何：

- 識別並減輕建立 AI 代理時的風險
- 實施安全措施，確保資料與存取被妥善管理
- 創造維護資料隱私並提供優質用戶體驗的 AI 代理

## 安全性

讓我們先來看看如何打造安全的代理應用程式。安全性意味著 AI 代理能如設計般運作。作為代理應用程式的建造者，我們有方法與工具可以最大化安全性：

### 建立系統訊息框架

如果你曾使用大型語言模型（LLM）建立 AI 應用，會知道設計穩固的系統提示或系統訊息的重要性。這些提示建立了元規則、指令以及 LLM 和使用者及資料互動的指導方針。

對於 AI 代理來說，系統提示更為重要，因為 AI 代理需要高度具體的指示來完成我們為其設計的任務。

為了創建可擴充的系統提示，我們可以使用系統訊息框架來為我們的應用程式建立一個或多個代理：

![建立系統訊息框架](../../../translated_images/zh-HK/system-message-framework.3a97368c92d11d68.webp)

#### 第一步：建立元系統訊息

元提示將由 LLM 用於生成我們創建代理的系統提示。我們將其設計為模板以便在需要時有效率地創建多個代理。

這是一個會給 LLM 的元系統訊息範例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 第二步：建立基本提示

下一步是建立描述 AI 代理的基本提示。你應該包含代理的角色、代理將完成的任務，以及代理的其他責任。

這是一個範例：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 第三步：將基本系統訊息提供給 LLM

現在我們可以透過提供元系統訊息作為系統訊息，以及我們的基本系統訊息，來優化此系統訊息。

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

#### 第四步：反覆調整和改進

此系統訊息框架的價值在於能更輕鬆地擴充多個代理的系統訊息創建，並隨時間改進系統訊息。通常你不會一開始就擁有完美符合完整用例的系統訊息。能夠透過改變基本系統訊息並執行系統來做小幅調整和改進，讓你能比較並評估結果。

## 了解威脅

要建立可信賴的 AI 代理，理解並減輕對你的 AI 代理的風險與威脅很重要。我們來看看幾種針對 AI 代理的不同威脅，以及如何更好地規劃與準備。

![了解威脅](../../../translated_images/zh-HK/understanding-threats.89edeada8a97fc0f.webp)

### 任務與指令

**描述：** 攻擊者試圖透過提示或者操縱輸入來改變 AI 代理的指令或目標。

<strong>緩解</strong>：執行驗證檢查與輸入過濾，偵測可能危險的提示，在被 AI 代理處理前阻擋。由於這些攻擊通常需要頻繁與代理互動，限制對話回合數也是防止此類攻擊的方法之一。

### 存取關鍵系統

**描述：** 如果 AI 代理能存取儲存敏感資料的系統與服務，攻擊者可能會破壞代理與這些服務間的通訊。這些攻擊可以是直接攻擊，或是經由代理嘗試間接取得系統資訊。

<strong>緩解</strong>：AI 代理應依需求限定存取系統，避免此類攻擊。代理與系統間的通訊應安全。實施身份驗證和存取控制也是保護此資訊的方法。

### 資源與服務過載

**描述：** AI 代理可存取不同工具和服務完成任務。攻擊者可利用此能力，透過 AI 代理發送大量請求攻擊這些服務，可能導致系統故障或高額成本。

**緩解：** 實施政策限制 AI 代理向服務發送請求數量。限制對 AI 代理的對話回合與請求次數也是防範此類攻擊之道。

### 知識庫中毒

**描述：** 此類攻擊不是直接針對 AI 代理，而是針對 AI 代理使用的知識庫及其他服務。這可能涉及損害 AI 代理完成任務會用到的資料或資訊，導致偏頗或非預期的回應用戶。

**緩解：** 定期驗證 AI 代理在工作流程中使用的資料。確保資料存取安全，僅被信任的人員修改，避免此類攻擊。

### 鏈狀錯誤

**描述：** AI 代理存取各種工具和服務完成任務。攻擊者引發的錯誤可導致 AI 代理連接的其他系統故障，造成攻擊擴大且更難診斷。

<strong>緩解</strong>：避免此情況的一種方法是讓 AI 代理在有限環境中運作，如於 Docker 容器中執行任務，阻止直接系統攻擊。建立備援機制及錯誤重試邏輯，當某些系統回傳錯誤時，也能防止更大系統故障。

## 人類在迴路中

建立可信賴的 AI 代理系統另一有效方式是採用人類在迴路中模式。此流程允許用戶在運行中對代理提供回饋。用戶本質上成為多代理系統中的代理，並能對執行過程發出批准或終止指令。

![人類在迴路中](../../../translated_images/zh-HK/human-in-the-loop.5f0068a678f62f4f.webp)

以下是使用 Microsoft Agent Framework 來示範如何實作這概念的程式碼片段：

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# 建立含有人類審批環節的供應商
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 建立具有人類審批步驟的代理程式
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# 使用者可審查及批准回應
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 結論

建立可信賴的 AI 代理需要謹慎設計、堅固的安全措施與持續迭代。透過實施結構化的元提示系統、了解潛在威脅並運用緩解策略，開發者能創建安全且有效的 AI 代理。此外，納入人類在迴路中的方法確保 AI 代理依用戶需求調整，同時降低風險。隨著 AI 持續發展，保持積極的安全、隱私及倫理考量，將是促進 AI 系統信任和可靠性的關鍵。

## 程式碼範例

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb)：元提示系統訊息框架的逐步示範。
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb)：可信賴代理的事前批准門檻、風險分層及稽核日誌。

### 對建立可信賴的 AI 代理有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加開放時間並獲得你的 AI 代理問題解答。

## 其他資源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">責任 AI 總覽</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式 AI 模型及 AI 應用評估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全系統訊息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">風險評估範本</a>

## 上一課

[Agentic RAG](../05-agentic-rag/README.md)

## 下一課

[規劃設計模式](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->