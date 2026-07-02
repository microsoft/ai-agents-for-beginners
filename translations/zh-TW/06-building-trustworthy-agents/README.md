[![值得信賴的 AI 代理人](../../../translated_images/zh-TW/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(點擊上方圖片觀看本課程影片)_

# 建立值得信賴的 AI 代理人

## 介紹

本課程將涵蓋：

- 如何建立並部署安全且有效的 AI 代理人
- 開發 AI 代理人時的重要安全考量
- 開發 AI 代理人時如何維護資料與用戶隱私

## 學習目標

完成本課程後，您將能夠：

- 辨識並降低建立 AI 代理人時的風險
- 實施安全措施，確保資料與存取權的妥善管理
- 創造能維護資料隱私且提供優質用戶體驗的 AI 代理人

## 安全性

讓我們先來看看如何建立安全的代理人式應用程式。安全性代表 AI 代理人如預期般運作。作為代理人式應用的開發者，我們擁有方法和工具以最大化安全性：

### 建立系統訊息框架

若您曾使用大型語言模型 (LLM) 建置 AI 應用，您就知道設計健全系統提示或系統訊息的重要性。這些提示會建立元規則、指示與指導方針，決定 LLM 如何與用戶及資料互動。

對 AI 代理人來說，系統提示更加重要，因為 AI 代理人需要高度特定的指示來完成我們為其設計的任務。

為了建立可擴展的系統提示，我們可以使用系統訊息框架來建置應用中的一個或多個代理人：

![建立系統訊息框架](../../../translated_images/zh-TW/system-message-framework.3a97368c92d11d68.webp)

#### 步驟 1：建立元系統訊息

元提示將由 LLM 用來產生我們創建代理人的系統提示。我們將它設計為範本，以便若需要時高效率地建立多個代理人。

以下是我們提供給 LLM 的元系統訊息範例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 步驟 2：建立基本提示

下一步是建立用以描述 AI 代理人的基本提示。您應包含代理人的角色、代理人將完成的任務，以及代理人的其他職責。

以下是範例：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 步驟 3：向 LLM 提供基本系統訊息

現在，我們可以藉由同時提供元系統訊息與基本系統訊息來優化此系統訊息。

這將產生更適合指導 AI 代理人的系統訊息：

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

#### 步驟 4：反覆修改與改進

此系統訊息框架的價值在於能夠更輕鬆地擴展多個代理人的系統訊息創建，並隨著時間改進您的系統訊息。很少會在第一次就為完整使用案例獲得完美的系統訊息。能夠透過改變基本系統訊息並經系統運行來做小幅調整和改進，將讓您能比較並評估結果。

## 了解威脅

為建立值得信賴的 AI 代理人，重要的是了解並降低 AI 代理人的風險與威脅。以下只介紹一些不同的 AI 代理人威脅，以及您如何更好地規劃與準備它們。

![了解威脅](../../../translated_images/zh-TW/understanding-threats.89edeada8a97fc0f.webp)

### 任務與指令

**描述：** 攻擊者嘗試透過提示或操控輸入改變 AI 代理人的指令或目標。

<strong>緩解措施</strong>：執行驗證檢查與輸入過濾器，在 AI 代理人處理前偵測潛在危險提示。由於此類攻擊通常需要頻繁與代理人互動，限制對話回合數也是防止此類攻擊的方式之一。

### 存取關鍵系統

**描述：** 若 AI 代理人可存取存有敏感資料的系統及服務，攻擊者可能破壞代理人與這些服務間的通訊。這些可成為直接攻擊，或透過代理人間接取得系統資訊的嘗試。

<strong>緩解措施</strong>：AI 代理人應有限度地根據需求存取系統，以防此類攻擊。代理人與系統間的通訊也應安全，實施認證與存取控制是保護資料的另一方法。

### 資源與服務過載

**描述：** AI 代理人可存取不同工具與服務來執行任務。攻擊者可能利用此功能，透過 AI 代理人發送大量請求以攻擊這些服務，導致系統故障或高昂費用。

**緩解措施：** 制定政策限制 AI 代理人對服務的請求數量。限制對 AI 代理人的對話回合數和請求數量也是防止此類攻擊的方式。

### 知識庫中毒

**描述：** 此類攻擊並非直接針對 AI 代理人，而是攻擊 AI 代理人將使用的知識庫與其他服務。可能會損壞 AI 代理人用以完成任務的資料或資訊，導致對用戶產生偏頗或非預期的回應。

**緩解措施：** 定期驗證 AI 代理人工作流程中使用的資料。確保該資料的存取安全，並僅由受信任者修改，以避免此類攻擊。

### 鏈式錯誤

**描述：** AI 代理人存取多個工具與服務以完成任務。攻擊者造成的錯誤可能導致 AI 代理人連接的其他系統故障，使攻擊更為擴散和難以排除故障。

<strong>緩解措施</strong>：一種避免方法是讓 AI 代理人在有限環境運作，例如在 Docker 容器中執行任務，防止直接系統攻擊。建立當特定系統回應錯誤時的回退機制與重試邏輯也是防止大規模系統故障的方式。

## 人類介入循環

另一種建立值得信賴 AI 代理人系統的有效方法是引入人類介入循環 (Human-in-the-loop)。此流程讓用戶能在運行時向代理人提供回饋。用戶實質上擔任多代理人系統中的代理人，提供核准或終止運行流程的決策。

![人類介入循環](../../../translated_images/zh-TW/human-in-the-loop.5f0068a678f62f4f.webp)

以下為使用 Microsoft Agent Framework 的程式碼片段，說明此概念如何實現：

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 建立具有人工審核的提供者
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# 建立具有人工審核步驟的代理人
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# 使用者可以審查並核准回應
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 結論

建立值得信賴的 AI 代理人需要謹慎設計、強健的安全措施與持續迭代。透過實作結構化的元提示系統、理解潛在威脅以及應用緩解策略，開發者能打造既安全又有效的 AI 代理人。此外，導入人類介入循環確保 AI 代理人持續符合用戶需求，同時降低風險。隨著 AI 持續演進，積極維護安全、隱私與倫理考量將是建立 AI 系統信任與可靠性的關鍵。

## 程式碼範例

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb)：元提示系統訊息框架的逐步示範。
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb)：具備預先行動審核門檻、風險分層及稽核日誌的值得信賴代理人範例。

### 有更多關於建立值得信賴 AI 代理人的問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流、參加辦公時間並獲得 AI 代理人相關問題的解答。

## 其他資源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">負責任的 AI 概述</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式 AI 模型與 AI 應用的評估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全性系統訊息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">風險評估範本</a>

## 上一課

[代理式 RAG](../05-agentic-rag/README.md)

## 下一課

[規劃設計範式](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->