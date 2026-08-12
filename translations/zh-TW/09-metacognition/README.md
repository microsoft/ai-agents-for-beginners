[![多智能體設計](../../../translated_images/zh-TW/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(點擊上方圖片觀看本課程影片)_
# AI 智能代理中的後設認知

## 介紹

歡迎來到關於 AI 智能代理中後設認知的課程！本章節專為對 AI 代理如何思考自身思考過程感到好奇的初學者設計。課程結束時，您將理解關鍵概念，並能運用實例設計具備後設認知的 AI 代理。

## 學習目標

完成本課程後，您將能夠：

1. 理解智能代理定義中推理迴圈的含義。
2. 運用規劃與評估技巧協助自我修正的代理。
3. 創建能操作程式碼以完成任務的智能代理。

## 後設認知介紹

後設認知指的是關於自身思維進行思考的高階認知過程。對 AI 代理而言，這意味著能根據自我覺察與過去經驗評估並調整行動。後設認知，即「思考關於思考」，是開發具代理性 AI 系統的重要概念。它涉及 AI 系統認知自身內部過程，能監控、調節並適應行為。就像我們在閱讀環境或解決問題時所做的自我覺察。這種自我覺察幫助 AI 系統做出更佳決策、識別錯誤，並隨時間提升表現——再次聯繫到圖靈測試及 AI 是否會接管的辯論。

在具代理性 AI 系統中，後設認知可以幫助解決多種挑戰，包括：
- 透明度：確保 AI 系統能說明其推理與決策過程。
- 推理：提升 AI 系統綜合資訊並做出合理決策的能力。
- 適應性：允許 AI 系統調整以應對新環境與變化條件。
- 感知：提升 AI 系統正確識別與解讀環境資料的能力。

### 什麼是後設認知？

後設認知，或稱「思考關於思考」，是一種高階認知過程，包含自我覺察與自我調節的認知技能。在 AI 領域，後設認知使代理評估並調整策略與行動，增進解決問題和決策能力。透過了解後設認知，您能設計出不僅更智能，且更具適應性與效率的 AI 代理。真正的後設認知會使 AI 明確地推理自身的推理過程。

範例：「我優先考慮較便宜的航班，因為…我可能錯過了直飛航班，讓我重新檢查一下。」。
記錄它如何或為何選擇特定路線。
- 注意到它犯錯是因過度依賴上次用戶偏好，因此它調整的是決策策略，而非僅最終推薦。
- 診斷模式，如「每當看到用戶提到‘太擁擠’，我不僅應避免某些景點，也應反思我依人氣排序‘熱門景點’的錯誤方法。」

### 後設認知在 AI 代理中的重要性

後設認知在 AI 代理設計中扮演關鍵角色，原因包括：

![後設認知的重要性](../../../translated_images/zh-TW/importance-of-metacognition.b381afe9aae352f7.webp)

- 自我反思：代理可評估自身表現，辨識改進空間。
- 適應能力：代理根據過去經驗及環境變化調整策略。
- 修正錯誤：代理能自主偵測並修正錯誤，提升結果準確度。
- 資源管理：代理能透過規劃與評估優化時間與計算資源使用。

## AI 代理的組成部分

在深入後設認知過程前，理解 AI 代理的基本組成十分重要。AI 代理通常包含：

- 個性設定：代理的個性與特徵，決定其如何與用戶互動。
- 工具：代理可執行的能力與功能。
- 技能：代理擁有的知識與專長。

這些組件協同合作，形成可執行特定任務的「專業單元」。

<strong>範例</strong>：
想像一個旅行代理，它不僅規劃假期，還能根據即時數據和過往用戶旅程經驗調整行程。

### 旅行代理服務中的後設認知範例

假設您正在設計一個 AI 驅動的旅行代理服務。這個代理「旅行代理」協助用戶規劃假期。為了融入後設認知，「旅行代理」需基於自我覺察與過往經驗評估並調整行動。後設認知可能的作用方式如下：

#### 當前任務

目前任務是幫助用戶計劃前往巴黎的旅行。

#### 完成任務的步驟

1. <strong>收集用戶偏好</strong>：詢問用戶旅遊日期、預算、興趣（如博物館、美食、購物）及特殊需求。
2. <strong>檢索資訊</strong>：搜尋航班選項、住宿、景點及餐廳，以符合用戶偏好。
3. <strong>產生推薦</strong>：提供包含航班細節、酒店訂房與建議活動的個人化行程。
4. <strong>根據回饋調整</strong>：向用戶詢問推薦意見並做必要調整。

#### 所需資源

- 存取航班和酒店預訂資料庫。
- 巴黎景點和餐廳資訊。
- 過去互動中的用戶回饋資料。

#### 經驗與自我反思

旅行代理利用後設認知評估表現並從過往經驗學習。例如：

1. <strong>分析用戶回饋</strong>：旅行代理回顧用戶回饋，判斷哪些建議受歡迎，哪些不然，並相應調整未來建議。
2. <strong>適應能力</strong>：若用戶曾提及不喜歡擁擠場所，旅行代理未來將避免在熱門時段推薦熱門景點。
3. <strong>錯誤修正</strong>：若過去訂房出錯（例如建議訂已滿房的酒店），代理學會更嚴謹檢查可用性再做推薦。

#### 實作範例

以下是一段簡化的旅行代理融合後設認知的程式碼範例：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # 根據偏好搜尋航班、飯店和景點
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # 分析回饋並調整未來的推薦
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# 使用範例
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### 後設認知的重要性

- <strong>自我反思</strong>：代理能分析表現，發現改進點。
- <strong>適應力</strong>：代理能根據回饋和環境變化調整策略。
- <strong>錯誤修正</strong>：代理能自動偵錯並修正錯誤。
- <strong>資源管理</strong>：代理能優化時間與計算資源使用。

結合後設認知後，旅行代理能提供更個人化且準確的旅遊建議，提升整體用戶體驗。

---

## 2. 代理中的規劃

規劃是 AI 代理行為中的關鍵部分，涉及列出達成目標所需的步驟，考量當前狀態、資源及可能障礙。

### 規劃要素

- <strong>當前任務</strong>：明確定義任務。
- <strong>完成任務的步驟</strong>：將任務拆解成可管理步驟。
- <strong>所需資源</strong>：辨識必需資源。
- <strong>經驗</strong>：運用過去經驗輔助規劃。

<strong>範例</strong>：
以下是旅行代理需採取的步驟，以有效協助用戶規劃行程：

### 旅行代理的步驟

1. <strong>收集用戶偏好</strong>
   - 詢問用戶有關旅遊日期、預算、興趣及特殊需求的詳細資訊。
   - 範例：「你計劃何時旅遊？」「你的預算範圍是多少？」「假期喜歡進行哪些活動？」

2. <strong>檢索資訊</strong>
   - 根據用戶偏好搜尋相關旅遊選項。
   - <strong>航班</strong>：尋找符合預算和旅行日期的可用航班。
   - <strong>住宿</strong>：找出符合位置、價格及設施需求的酒店或出租物業。
   - <strong>景點與餐廳</strong>：辨識符合用戶興趣的熱門景點、活動與用餐選項。

3. <strong>產生推薦</strong>
   - 將檢索信息編入個人化行程。
   - 提供航班細節、酒店訂房及建議活動，確保推薦符合用戶偏好。

4. <strong>向用戶展示行程</strong>
   - 與用戶分享建議行程供其審閱。
   - 範例：「這是給您的巴黎旅行建議行程，包括航班細節、酒店預訂，以及推薦的活動和餐廳。請告訴我您的想法！」

5. <strong>收集回饋</strong>
   - 詢問用戶對建議行程的意見。
   - 範例：「您喜歡這些航班選項嗎？」「酒店是否符合您的需求？」「有無想新增或刪除的活動？」

6. <strong>根據回饋調整</strong>
   - 根據用戶意見修改行程。
   - 調整航班、住宿與活動建議以更符合用戶偏好。

7. <strong>最終確認</strong>
   - 向用戶展示更新過的行程以便最終確認。
   - 範例：「我已根據您的回饋調整行程，這是更新版本，您看起來都滿意嗎？」

8. <strong>預訂並確認</strong>
   - 用戶確認行程後，進行航班、住宿和預定活動的訂票。
   - 並將確認細節發送給用戶。

9. <strong>提供持續支援</strong>
   - 旅途中及前後，隨時協助用戶變更或額外需求。
   - 範例：「行程期間如有需要，隨時聯絡我協助！」

### 互動範例

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# 在啟動請求中的範例用法
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. 修正性 RAG 系統

首先，我們要理解 RAG 工具與預先載入上下文的差異。

![RAG 與上下文載入比較](../../../translated_images/zh-TW/rag-vs-context.9eae588520c00921.webp)

### 檢索增強生成 (RAG)

RAG 結合了檢索系統與生成模型。當有查詢時，檢索系統會從外部來源取得相關文件或資料，利用這些資訊增強生成模型的輸入，幫助模型產生更準確且符合上下文的回答。

在 RAG 系統中，代理會從知識庫檢索相關資訊，再用以生成適切回應或行動。

### 修正性 RAG 方法

修正性 RAG 強調利用 RAG 技術來修正錯誤並提升 AI 代理的準確度。其包含：

1. <strong>提示技術</strong>：使用特定提示引導代理檢索相關資料。
2. <strong>工具</strong>：實作算法與機制，使代理評估檢索資料的相關性並生成正確回答。
3. <strong>評估</strong>：持續評估代理表現，進行調整以提升準確率和效率。

#### 範例：搜尋代理中的修正性 RAG

以一個從網絡檢索資料回答用戶問題的搜尋代理為例。修正性 RAG 可能包括：

1. <strong>提示技術</strong>：根據用戶輸入形成搜尋查詢。
2. <strong>工具</strong>：利用自然語言處理和機器學習算法對搜尋結果進行排序和過濾。
3. <strong>評估</strong>：分析用戶回饋，識別並修正檢索資訊中的不準確之處。

### 旅行代理中的修正性 RAG

修正性 RAG（檢索增強生成）提升 AI 在檢索和生成資訊的能力，同時糾正任何不準確資訊。來看看旅行代理如何利用修正性 RAG 方法提供更準確且相關的旅遊建議。

此方法包括：

- **提示技術：** 使用特定提示引導代理檢索相關資訊。
- **工具：** 實施算法和機制，使代理評估檢索資訊的相關性並生成準確回應。
- **評估：** 持續評估代理表現，做出調整以提升準確和效率。

#### 旅行代理中實施修正性 RAG 的步驟

1. <strong>初始用戶互動</strong>
   - 旅行代理收集用戶的初始偏好，例如目的地、旅遊日期、預算和興趣。
   - 範例：

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. <strong>資訊檢索</strong>
   - 旅行代理根據用戶偏好檢索航班、住宿、景點和餐廳資訊。
   - 範例：

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. <strong>生成初步推薦</strong>
   - 旅行代理利用檢索到的資訊生成個人化行程。
   - 範例：

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. <strong>收集用戶反饋</strong>
   - 旅行代理詢問用戶對初步推薦的意見。
   - 範例：

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **修正性 RAG 流程**
   - <strong>提示技術</strong>：旅行代理根據用戶反饋製作新的搜尋查詢。
     - 範例：

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - <strong>工具</strong>：旅行代理使用算法排序與過濾新搜尋結果，強調根據用戶回饋的相關性。
     - 範例：

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - <strong>評估</strong>：旅行代理持續分析用戶回饋，評估建議的相關性和準確度，並做必要調整。
     - 範例：

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### 實作範例

下方為一段簡化的 Python 程式碼範例，展示如何在旅行代理中融合修正性 RAG 方法：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# 使用範例
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### 預先載入上下文


預先載入上下文是指在處理查詢之前，將相關的上下文或背景資訊載入模型。這代表模型從一開始就能取得這些資訊，進而幫助它生成更有依據的回應，而無需在過程中額外檢索資料。

以下是預先載入上下文在 Python 旅行代理應用中的簡化範例：

```python
class TravelAgent:
    def __init__(self):
        # 預先加載熱門目的地及其資訊
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # 從預先加載的上下文中擷取目的地資訊
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# 使用範例
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### 說明

1. **初始化（`__init__` 方法）**：`TravelAgent` 類別預先載入一個字典，包含巴黎、東京、紐約和悉尼等熱門旅遊地點的資訊。此字典包括每個地點的國家、貨幣、語言和主要景點等詳細資料。

2. **擷取資訊（`get_destination_info` 方法）**：當使用者查詢特定旅遊地點時，`get_destination_info` 方法會從預先載入的上下文字典中取得相關資訊。

通過預先載入上下文，旅行代理應用能迅速回應用戶查詢，不必在實時中從外部來源檢索資料，使應用更有效率且反應更快速。

### 在迭代前以目標啟動計劃

以目標啟動計劃意味著在開始時就設定明確的目標或預期結果。透過事先定義此目標，模型能以此作為指導原則，貫穿整個迭代過程。這有助於確保每次迭代都朝向實現預期成果，讓流程更有效率且有焦點。

以下是如何在 Python 旅行代理中，先以目標啟動旅遊計劃，再進行迭代的範例：

### 場景

旅行代理想為客戶規劃量身訂做的假期，目標是根據客戶的偏好和預算，創建最大化客戶滿意度的旅遊行程。

### 步驟

1. 定義客戶的偏好和預算。
2. 根據這些偏好啟動初步計劃。
3. 透過迭代優化計劃，以提升客戶滿意度。

#### Python 代碼

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# 範例用法
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### 程式碼說明

1. **初始化（`__init__` 方法）**：`TravelAgent` 類別藉由潛在旅遊地點列表初始化，每個地點具有名稱、費用和活動類型等屬性。

2. **啟動計劃 (`bootstrap_plan` 方法)**：此方法根據客戶偏好和預算建立初始旅遊計劃。它會遍歷地點列表，若符合偏好且預算可負擔，就納入計劃中。

3. **比對偏好 (`match_preferences` 方法)**：此方法判斷某個地點是否符合客戶的偏好。

4. **迭代計劃 (`iterate_plan` 方法)**：此方法透過嘗試用更符合客戶偏好和預算的地點替代原計劃中的地點，優化計劃內容。

5. **計算費用 (`calculate_cost` 方法)**：此方法計算包含新增地點的目前計劃總花費。

#### 範例使用情境

- <strong>初始計劃</strong>：旅行代理依客戶對觀光的偏好和 2000 美元預算建立初始旅遊計劃。
- <strong>優化後計劃</strong>：代理透過迭代計劃，依據客戶偏好和預算進行優化。

透過以清晰目標（例如最大化客戶滿意度）啟動計劃以及反覆迭代，旅行代理能為客戶打造客製化且最佳化的旅遊行程。此方法確保旅遊計劃從一開始就符合客戶偏好和預算，且隨著每次迭代逐步精進。

### 利用大型語言模型（LLM）進行重新排名和評分

大型語言模型（LLM）可以用於重新排名和評分，藉由評估檢索到的文件或生成的回應的相關性和品質。運作流程如下：

<strong>檢索</strong>：初步檢索根據查詢獲取一組候選文件或回應。

<strong>重新排名</strong>：LLM 評估這些候選項目，依據其相關性和品質重新排列順序。此步驟確保最相關且高品質的資訊優先呈現。

<strong>評分</strong>：LLM 為每個候選項目分配分數，反映其相關性和品質，有助於挑選最佳回應或文件給用戶。

透過利用 LLM 做重新排名和評分，系統能提供更準確且具上下文相關性的資訊，提升整體使用者體驗。

以下展示旅行代理如何用大型語言模型（LLM）根據用戶偏好重新排名並評分旅遊目的地的 Python 範例：

#### 場景 - 根據偏好旅遊

旅行代理想根據客戶偏好推薦最佳旅遊目的地，LLM 協助重新排名並評分，確保呈現最相關的選項。

#### 步驟：

1. 收集用戶偏好。
2. 擷取潛在旅遊目的地清單。
3. 使用 LLM 依用戶偏好重新排名並評分目的地。

以下展示如何更新先前範例，改用 Azure OpenAI 服務：

#### 需求

1. 需要有 Azure 訂閱。
2. 建立 Azure OpenAI 資源並取得 API 金鑰。

#### 範例 Python 程式碼

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # 產生 Azure OpenAI 的提示
        prompt = self.generate_prompt(preferences)
        
        # 定義請求的標頭和載荷
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # 呼叫 Azure OpenAI API 以獲取重新排序和評分的目的地
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # 擷取並返回建議結果
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# 使用範例
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### 程式碼說明 - 偏好預訂器

1. <strong>初始化</strong>：`TravelAgent` 類別以旅遊目的地清單初始化，每個地點皆包含名稱和描述等屬性。

2. **獲取推薦（`get_recommendations` 方法）**：此方法根據用戶偏好生成提示字串，並向 Azure OpenAI API 發出 HTTP POST 請求，獲取經重新排名與評分的目的地。

3. **生成提示（`generate_prompt` 方法）**：此方法為 Azure OpenAI 構建提示，包含用戶偏好和目的地清單，指導模型根據提供的偏好重新排序並評分目的地。

4. **API 呼叫**：使用 `requests` 函式庫向 Azure OpenAI API 端點發送 HTTP POST 請求，取得重新排名和評分結果。

5. <strong>使用範例</strong>：旅行代理收集用戶偏好（例如對觀光和多元文化的興趣），利用 Azure OpenAI 服務取得重新排序並評分的旅遊推薦。

請確保將 `your_azure_openai_api_key` 換成您實際的 Azure OpenAI API 金鑰，並將 `https://your-endpoint.com/...` 換成實際的 Azure OpenAI 部署端點 URL。

利用 LLM 進行重新排名與評分，旅行代理能提供更個人化且貼切的旅遊推薦，提升整體客戶體驗。

### RAG：提示技術與工具的比較

檢索增強生成（RAG）既可視為提示技術，也可作為工具用於 AI 代理開發。了解兩者差異有助於更有效利用 RAG。

#### RAG 作為提示技術

**是什麼？**

- 作為提示技術，RAG 包含設計特定查詢或提示，以引導從大量資料或數據庫檢索相關資訊，再用以生成回應或行動。

**運作方式：**

1. <strong>設計提示</strong>：根據任務或用戶輸入，創建結構良好的提示或查詢。
2. <strong>檢索信息</strong>：利用提示從現有知識庫或數據集中搜尋相關資料。
3. <strong>生成回應</strong>：結合檢索的資訊與生成式 AI 模型，產生完整且連貫的回應。

**旅行代理案例：**

- 使用者輸入：「我想去巴黎的博物館。」
- 提示：「找巴黎的熱門博物館。」
- 檢索資訊：羅浮宮、奧賽博物館等詳細資料。
- 生成回應：「以下是巴黎的熱門博物館：羅浮宮、奧賽博物館和龐畢度中心。」

#### RAG 作為工具

**是什麼？**

- 作為工具，RAG 是一套集成系統，自動化檢索與生成流程，方便開發者在不需為每個查詢手動設計提示的情況下，實作複雜 AI 功能。

**運作方式：**

1. <strong>整合</strong>：將 RAG 嵌入 AI 代理架構，自動處理檢索和生成任務。
2. <strong>自動化</strong>：工具管理整個流程，從接收用戶輸入至生成最終回應，無需每步驟明確提示。
3. <strong>效率</strong>：藉由簡化檢索與生成流程，提升代理效率與回應速度。

**旅行代理案例：**

- 使用者輸入：「我想去巴黎的博物館。」
- RAG 工具：自動檢索博物館資訊並生成回應。
- 生成回應：「以下是巴黎的熱門博物館：羅浮宮、奧賽博物館和龐畢度中心。」

### 比較

| 方面                   | 提示技術                                                      | 工具                                                    |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **手動 vs 自動**       | 手動為每個查詢設計提示。                                     | 自動化處理檢索與生成流程。                             |
| <strong>控制度</strong>             | 提供對檢索流程更高控制度。                                   | 簡化並自動化檢索與生成流程。                           |
| <strong>彈性</strong>               | 可根據特定需求自訂提示。                                     | 適合大規模實作，更有效率。                             |
| <strong>複雜度</strong>             | 需要設計及調整提示。                                         | 更容易整合於 AI 代理架構中。                           |

### 實作範例

**提示技術範例：**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**工具範例：**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### 評估相關性

評估相關性是 AI 代理性能中極為重要的環節。它確保代理檢索和生成的資訊是恰當、正確且對用戶有用。我們來探討如何評估 AI 代理的相關性，包括實務範例與技術。

#### 評估相關性的關鍵概念

1. <strong>上下文意識</strong>：
   - 代理必須理解用戶查詢的上下文，方能檢索和生成相關資訊。
   - 範例：用戶查詢「巴黎最佳餐廳」，代理應考慮用戶的口味及預算偏好。

2. <strong>準確性</strong>：
   - 代理提供的資訊應基於事實，且保持最新。
   - 範例：推薦目前營業且評價良好的餐廳，而非過時或已關閉的選項。

3. <strong>用戶意圖</strong>：
   - 代理應推斷用戶查詢背後的意圖，以提供最相關資訊。
   - 範例：若用戶查詢「平價飯店」，代理應優先推薦經濟實惠的選項。

4. <strong>反饋迴圈</strong>：
   - 持續收集並分析用戶反饋，有助代理改善相關性評估流程。
   - 範例：結合用戶評分與先前推薦的反饋，優化未來回應。

#### 評估相關性的實務技術

1. <strong>相關性評分</strong>：
   - 根據檢索項目與用戶查詢及偏好的匹配程度，賦予相關性分數。
   - 範例：

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. <strong>過濾與排序</strong>：
   - 過濾掉不相關項目，根據相關性分數對剩餘項目排序。
   - 範例：

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # 回傳前 10 個相關項目
     ```

3. **自然語言處理（NLP）**：
   - 利用 NLP 技術理解用戶查詢，檢索相關資訊。
   - 範例：

     ```python
     def process_query(query):
         # 使用自然語言處理從使用者的查詢中提取關鍵資訊
         processed_query = nlp(query)
         return processed_query
     ```

4. <strong>整合用戶反饋</strong>：
   - 收集用戶對推薦的反饋，並用以調整未來的相關性評估。
   - 範例：

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### 範例：旅遊代理評估相關性

以下為旅遊代理如何評估旅遊推薦相關性的實務範例：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # 回傳前10個相關項目

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# 範例用法
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### 帶有意圖的搜尋

帶有意圖的搜尋是指理解並解釋用戶查詢背後的目的或目標，檢索並生成最相關且有用的資訊。此方法超越純關鍵字匹配，著重於把握用戶真實需求和上下文。

#### 帶意圖搜尋的關鍵概念

1. <strong>理解用戶意圖</strong>：
   - 用戶意圖可分為三類：資訊型、導航型和交易型。
     - <strong>資訊型意圖</strong>：用戶尋求關於主題的資訊（例如：「巴黎有哪些最佳博物館？」）。
     - <strong>導航型意圖</strong>：用戶想前往特定網站或頁面（例如：「羅浮宮官方網站」）。
     - <strong>交易型意圖</strong>：用戶希望執行交易，如訂票或購買（例如：「訂巴黎的機票」）。

2. <strong>上下文意識</strong>：
   - 分析用戶查詢的上下文，準確判斷意圖，包括考量先前互動、偏好和查詢細節。

3. **自然語言處理（NLP）**：
   - 使用 NLP 技術理解並解釋用戶的自然語言查詢，包括實體識別、情緒分析與查詢解析等任務。

4. <strong>個人化</strong>：
   - 根據用戶歷史、偏好與反饋，個人化搜尋結果，提升資訊相關性。

#### 實務範例：旅遊代理中的帶意圖搜尋

以下以旅遊代理為例，展示如何實作帶意圖的搜尋。

1. <strong>收集用戶偏好</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. <strong>理解用戶意圖</strong>

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. <strong>上下文意識</strong>


   ```python
   def analyze_context(query, user_history):
       # 將當前查詢與用戶歷史結合以理解上下文
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. <strong>搜尋與個人化結果</strong>

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # 資訊意圖的範例搜尋邏輯
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # 導航意圖的範例搜尋邏輯
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # 交易意圖的範例搜尋邏輯
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # 個人化範例邏輯
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # 回傳前 10 名個人化結果
   ```

5. <strong>範例用法</strong>

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. 作為工具的程式碼生成

程式碼生成代理使用 AI 模型撰寫並執行程式碼，解決複雜問題並自動化任務。

### 程式碼生成代理

程式碼生成代理使用生成式 AI 模型撰寫並執行程式碼。這些代理可以透過生成並執行多種程式語言的程式碼來解決複雜問題、自動化任務並提供有價值的見解。

#### 實際應用

1. <strong>自動程式碼生成</strong>：為特定任務生成程式碼片段，如資料分析、網路爬蟲或機器學習。
2. **將 SQL 作為 RAG 使用**：使用 SQL 查詢來檢索及操作資料庫中的資料。
3. <strong>問題解決</strong>：撰寫並執行程式碼以解決具體問題，如演算法優化或資料分析。

#### 範例：用於資料分析的程式碼生成代理

假設你正在設計一個程式碼生成代理。以下是它可能的運作方式：

1. <strong>任務</strong>：分析資料集以識別趨勢和模式。
2. <strong>步驟</strong>：
   - 將資料集載入資料分析工具。
   - 生成 SQL 查詢來篩選和聚合資料。
   - 執行查詢並取得結果。
   - 使用結果生成視覺化圖表與見解。
3. <strong>所需資源</strong>：資料集存取權限、資料分析工具和 SQL 能力。
4. <strong>經驗</strong>：利用過去分析結果來提升未來分析的準確性與相關性。

### 範例：用於旅遊代理的程式碼生成代理

在此範例中，我們將設計一個程式碼生成代理「旅遊代理」，透過生成並執行程式碼幫助使用者規劃旅程。此代理能處理例如擷取旅遊選項、篩選結果及組合行程等任務，利用生成式 AI 技術實現。

#### 程式碼生成代理概述

1. <strong>蒐集使用者偏好</strong>：收集使用者輸入的目的地、旅遊日期、預算和興趣等資訊。
2. <strong>生成擷取資料的程式碼</strong>：產生程式碼片段以取得有關航班、飯店和景點的資料。
3. <strong>執行生成的程式碼</strong>：執行生成的程式碼以擷取即時資訊。
4. <strong>生成行程</strong>：將取得的資料編輯成個人化的旅遊計畫。
5. <strong>根據回饋進行調整</strong>：接收使用者回饋，必要時重新生成程式碼以優化結果。

#### 逐步實作

1. <strong>蒐集使用者偏好</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. <strong>生成擷取資料的程式碼</strong>

   ```python
   def generate_code_to_fetch_data(preferences):
       # 範例：產生根據使用者偏好搜尋航班的程式碼
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # 範例：產生搜尋飯店的程式碼
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. <strong>執行生成程式碼</strong>

   ```python
   def execute_code(code):
       # 使用 exec 執行產生的程式碼
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. <strong>生成行程</strong>

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. <strong>根據回饋進行調整</strong>

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # 根據用戶反饋調整偏好設定
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # 使用更新的偏好設定重新生成並執行程式碼
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### 利用環境感知與推理

根據資料表的架構確實能增強查詢生成流程，通過利用環境感知與推理。

以下是一個示例說明如何實現：

1. <strong>理解架構</strong>：系統會理解資料表的架構，並用此資訊作為查詢生成的基礎。
2. <strong>根據回饋進行調整</strong>：系統會根據使用者回饋調整偏好，並推理哪些欄位需更新。
3. <strong>生成並執行查詢</strong>：根據新的偏好，系統會產生並執行查詢以擷取更新的航班和飯店資料。

以下是一段更新的 Python 程式碼範例，結合上述概念：

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # 根據用戶反饋調整偏好設定
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # 根據架構進行推理以調整其他相關偏好設定
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # 根據架構和反饋自訂邏輯以調整偏好設定
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # 產生程式碼以根據更新的偏好設定抓取航班資料
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # 產生程式碼以根據更新的偏好設定抓取飯店資料
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # 模擬執行程式碼並返回模擬資料
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # 根據航班、飯店和景點產生行程
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# 範例架構
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# 使用範例
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# 重新產生並執行帶有更新偏好設定的程式碼
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### 解釋 - 根據回饋進行預訂

1. <strong>架構感知</strong>：`schema` 字典定義了如何根據回饋調整偏好，其中包含欄位如 `favorites` 和 `avoid`，及其相應的調整方式。
2. **調整偏好 (`adjust_based_on_feedback` 方法)**：此方法根據使用者回饋與架構調整偏好。
3. **基於環境的調整 (`adjust_based_on_environment` 方法)**：此方法根據架構與回饋自定義調整方式。
4. <strong>生成並執行查詢</strong>：系統會根據調整後的偏好生成程式碼以擷取更新的航班和飯店資料，並模擬這些查詢的執行。
5. <strong>生成行程</strong>：系統根據新的航班、飯店及景點資料創建更新後的行程。

將系統設計為環境知曉並基於架構推理，可以產生更準確且具相關性的查詢，帶來更佳的旅遊推薦和個人化使用者體驗。

### 使用 SQL 作為檢索擴充生成 (Retrieval-Augmented Generation, RAG) 技術

SQL（結構化查詢語言）是與資料庫互動的強大工具。當作為檢索擴充生成（RAG）方法的一部分使用時，SQL 可用來從資料庫檢索相關資料，以協助 AI 代理生成回應或執行操作。讓我們探討如何在旅遊代理情境下使用 SQL 作為 RAG 技術。

#### 主要概念

1. <strong>資料庫互動</strong>：
   - SQL 用於查詢資料庫，檢索相關資訊以及操作資料。
   - 範例：從旅遊資料庫取得航班詳情、飯店資訊及景點資料。

2. **與 RAG 結合**：
   - 根據使用者輸入和偏好生成 SQL 查詢。
   - 檢索的資料用以生成個人化推薦或行動。

3. <strong>動態查詢生成</strong>：
   - AI 代理根據情境與使用者需求產生動態 SQL 查詢。
   - 範例：根據預算、日期和興趣客製化 SQL 查詢以過濾結果。

#### 應用

- <strong>自動程式碼生成</strong>：為特定任務生成程式碼片段。
- **將 SQL 作為 RAG**：使用 SQL 查詢操作資料。
- <strong>問題解決</strong>：撰寫並執行程式碼解決問題。

<strong>範例</strong>：
一個資料分析代理：

1. <strong>任務</strong>：分析資料集以發掘趨勢。
2. <strong>步驟</strong>：
   - 載入資料集。
   - 生成 SQL 查詢以篩選資料。
   - 執行查詢並取得結果。
   - 生成視覺化和見解。
3. <strong>資源</strong>：資料集存取權限以及 SQL 能力。
4. <strong>經驗</strong>：利用過去結果提升未來分析。

#### 實際範例：旅遊代理中使用 SQL

1. <strong>蒐集使用者偏好</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **生成 SQL 查詢**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **執行 SQL 查詢**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. <strong>生成推薦</strong>

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### 範例 SQL 查詢

1. <strong>航班查詢</strong>

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. <strong>飯店查詢</strong>

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. <strong>景點查詢</strong>

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

利用 SQL 作為檢索擴充生成（RAG）技術的一部分，像旅遊代理這類 AI 代理可以動態檢索並運用相關資料，提供精確且個人化的推薦。

### 元認知範例

為了示範元認知的實作，讓我們創建一個簡單代理，它在解決問題時會<em>反思自己的決策過程</em>。在這個範例中，我們將建構一個系統，代理嘗試優化飯店選擇，並在做出錯誤或次優決策時評估自己的推理並調整策略。

我們將透過一個基於價格和品質綜合評比來選飯店的基本範例進行模擬，代理會「反思」自身決策並相應調整。

#### 此例說明元認知方式：

1. <strong>初始決策</strong>：代理選擇最便宜的飯店，未考慮品質影響。
2. <strong>反思與評估</strong>：在初次選擇後，代理利用使用者回饋檢查飯店是否為「不佳」選擇。若發現飯店品質過低，則反思自己的推理。
3. <strong>調整策略</strong>：代理根據反思調整策略，從「最便宜」改為「最高品質」，從而改善未來決策流程。

範例代碼如下：

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # 儲存先前選擇的飯店
        self.corrected_choices = []  # 儲存修正後的選擇
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # 可用的策略

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # 假設我們有一些用戶反饋，告訴我們上一次的選擇是否良好
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # 如果先前的選擇不令人滿意，調整策略
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# 模擬一個飯店清單（價格和品質）
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# 建立一個代理人
agent = HotelRecommendationAgent()

# 第一步：代理人使用「最便宜」策略推薦飯店
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# 第二步：代理人反思選擇，必要時調整策略
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# 第三步：代理人再次推薦，這次使用調整後的策略
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### 代理元認知能力

這裡的關鍵在於代理能夠：
- 評估先前選擇與決策過程。
- 根據反思調整策略，即元認知實踐。

這是一種簡單的元認知形式，使系統能夠根據內部回饋調整推理過程。

### 結論

元認知是一項強大的工具，能顯著提升 AI 代理的能力。透過納入元認知流程，可以設計出更聰明、具適應性且效率更高的代理。請利用附加資源深入探索 AI 代理中的元認知妙趣。

### 對元認知設計模式有更多問題嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者交流、參加辦公時段並獲得你的 AI 代理相關問題解答。

## 上一課

[多代理設計模式](../08-multi-agent/README.md)

## 下一課

[AI 代理生產環境應用](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->