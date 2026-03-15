[![可信賴的 AI 代理](../../../translated_images/zh-HK/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(按上方圖片以觀看本課影片)_

# 建立可信賴的 AI 代理

## 簡介

本課將涵蓋：

- 如何建立及部署安全且有效的 AI 代理
- 開發 AI 代理 時的重要安全考量。
- 在開發 AI 代理 時如何維護資料及用戶私隱。

## 學習目標

完成本課後，你將會知道如何：

- 識別並減輕建立 AI 代理 時的風險。
- 實施安全措施以確保資料和存取得到妥善管理。
- 建立能維持資料私隱並提供優質用戶體驗的 AI 代理。

## 安全

我們先來看看如何構建安全的具代理性的應用程式。安全意指 AI 代理按設計運作。作為具代理性應用的開發者，我們有方法及工具以最大化安全性：

### 建立系統訊息框架

如果你曾使用大型語言模型 (LLMs) 建立 AI 應用程式，你就會了解設計一個健全的系統提示或系統訊息的重要性。這些提示建立了 LLM 與使用者及資料互動的元規則、指示與指引。

對於 AI 代理，系統提示更為重要，因為 AI 代理需要高度具體的指示來完成我們為其設計的任務。

為了建立可擴展的系統提示，我們可以使用系統訊息框架來為應用程式中建立一個或多個代理：

![建立系統訊息框架](../../../translated_images/zh-HK/system-message-framework.3a97368c92d11d68.webp)

#### 步驟 1：建立一個元系統訊息 

元提示將會被 LLM 用來產生我們為代理所建立的系統提示。我們將它設計成模板，以便在需要時有效率地建立多個代理。

以下是一個我們會提供給 LLM 的元系統訊息範例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 步驟 2：建立一個基本提示

下一步是建立一個基本提示來描述 AI 代理。你應包括代理的角色、代理將完成的任務，以及代理的其他職責。

以下是一個範例：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 步驟 3：向 LLM 提供基本系統訊息

現在我們可以透過將元系統訊息作為系統訊息，並結合我們的基本系統訊息，來優化此系統訊息。

這會產生一個更適合指導我們 AI 代理的系統訊息：

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

#### 步驟 4：反覆修正與改進

此系統訊息框架的價值在於能更容易地擴展為多個代理建立系統訊息，並隨時間改進你的系統訊息。很少會有一個系統訊息在第一次就能符合你完整的使用情境。能夠透過更改基本系統訊息並將其執行於系統上來做小幅調整與改進，將讓你能比較與評估結果。

## 了解威脅

要建立值得信賴的 AI 代理，了解並減輕針對 AI 代理 的風險與威脅非常重要。以下將介紹其中一些對 AI 代理 的不同威脅，以及你如何更好地計劃與準備應對它們。

![了解威脅](../../../translated_images/zh-HK/understanding-threats.89edeada8a97fc0f.webp)

### 任務與指示

**描述：** 攻擊者嘗試透過提示或操控輸入來改變 AI 代理的指示或目標。

**緩解措施**：執行驗證檢查和輸入篩選，以在 AI 代理處理前偵測可能危險的提示。由於這些攻擊通常需要與代理頻繁互動，限制對話回合數是另一種防止此類攻擊的方法。

### 存取關鍵系統

**描述**：如果 AI 代理可以存取儲存敏感資料的系統與服務，攻擊者可能會破壞代理與這些服務之間的通訊。這些攻擊可以是直接攻擊，也可以是透過代理間接獲取關於這些系統的資訊的嘗試。

**緩解措施**：AI 代理應只在必要時存取系統，以防止此類攻擊。代理與系統之間的通訊也應當是安全的。實施驗證與存取控制是保護這些資訊的另一種方式。

### 資源與服務過載

**描述：** AI 代理可以存取不同的工具和服務以完成任務。攻擊者可能利用此能力透過 AI 代理發送大量請求來攻擊這些服務，可能導致系統故障或高昂的費用。

**緩解措施：** 實施政策以限制 AI 代理對服務發出的請求次數。限制對話回合數和向 AI 代理發出的請求數也是防止此類攻擊的方法。

### 知識庫中毒

**描述：** 此類攻擊不是直接針對 AI 代理，而是針對 AI 代理會使用的知識庫和其他服務。這可能包括破壞 AI 代理用來完成任務的資料或資訊，導致對使用者產生有偏或非預期的回應。

**緩解措施：** 定期驗證 AI 代理在其工作流程中將使用的資料。確保對這些資料的存取是安全的，並僅由受信任的人員變更，以避免此類攻擊。

### 連鎖錯誤

**描述：** AI 代理會存取各種工具與服務以完成任務。由攻擊者引起的錯誤可能導致 AI 代理所連接的其他系統失效，使攻擊蔓延更廣且更難排查。

**緩解措施：** 避免這種情況的一個方法是讓 AI 代理在受限環境中運行，例如在 Docker container 中執行任務，以防止直接對系統的攻擊。當某些系統回應錯誤時，建立後備機制和重試邏輯是防止更大系統故障的另一種方式。

## 人類介入

另一個建立值得信賴的 AI 代理 系統的有效方法是採用人類介入（Human-in-the-loop）。這會建立一個流程，讓使用者能在執行期間向代理提供回饋。使用者實際上在多代理系統中扮演代理的角色，透過提供批准或終止正在執行的流程來參與。

![人類介入](../../../translated_images/zh-HK/human-in-the-loop.5f0068a678f62f4f.webp)

以下是一段使用 Microsoft Agent Framework 的程式碼片段，示範這個概念如何實作：

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 建立需人類介入批准的供應者
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# 建立帶有人類批准步驟的代理
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# 使用者可以審閱及批准回應
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 結論

建立值得信賴的 AI 代理 需要謹慎的設計、健全的安全措施與持續的迭代。透過實作結構化的元提示系統、了解潛在威脅並採取緩解策略，開發人員可以建立既安全又有效的 AI 代理。此外，納入人類介入的方式可確保 AI 代理與使用者需求保持一致，同時將風險降至最低。隨著 AI 持續發展，對安全、私隱與倫理議題採取主動態度將是培養 AI 驅動系統信任與可靠性的關鍵。

### 想了解更多有關建立值得信賴的 AI 代理 的問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者會面、參加辦公時間並獲得你的 AI 代理 問題的解答。

## 額外資源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">負責任的 AI 概覽</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式 AI 模型與 AI 應用的評估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全系統訊息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">風險評估範本</a>

## 上一堂課

[具代理性的 RAG](../05-agentic-rag/README.md)

## 下一堂課

[規劃設計模式](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務 Co‑op Translator（https://github.com/Azure/co-op-translator）進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原文應視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而導致的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->