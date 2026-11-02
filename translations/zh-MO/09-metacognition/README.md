[![多智能體設計](../../../translated_images/zh-MO/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(點擊上方圖片觀看本課程影片)_
# AI 代理中的元認知

## 簡介

歡迎來到 AI 代理中元認知的課程！本章節專為好奇 AI 代理如何反思自身思考過程的新手設計。課程結束時，您將理解關鍵概念，並獲得實用範例，以應用元認知於 AI 代理設計中。

## 學習目標

完成本課後，您將能夠：

1. 理解代理定義中推理迴圈的影響。
2. 運用規劃與評估技術幫助自我校正的代理。
3. 創建能操作程式碼完成任務的自有代理。

## 元認知簡介

元認知是指涉及對自身思考進行思考的高階認知過程。對 AI 代理來說，這意味著能根據自我覺察和過去經驗評估並調整行動。元認知，或稱「對思考的思考」，是開發代理式 AI 系統的重要概念。它涉及 AI 系統覺察自身內部過程，並能監控、調節及調整其行為。就像我們在解讀環境或面對問題時做的那樣。這種自我覺察可協助 AI 系統做出更佳決策、識別錯誤並隨時間提升效能——這又與圖靈測試及 AI 是否會取代人類的爭論相關。

在代理式 AI 系統中，元認知可協助解決多個挑戰，例如：
- 透明度：確保 AI 系統能解釋其推理與決策。
- 推理能力：增強 AI 系統綜合資訊並做出合理決策的能力。
- 適應性：允許 AI 系統調整以適應新環境及變動條件。
- 感知力：提升 AI 系統辨識並解讀環境資料的準確度。

### 什麼是元認知？

元認知，或稱「對思考的思考」，是一種高階認知過程，包含自我覺察與自我調節認知過程。在 AI 領域，元認知使代理能評估並調整其策略與行動，促進問題解決與決策能力提升。了解元認知後，您可以設計出不僅更聰明且更具適應性及效率的 AI 代理。在真正的元認知中，您將見到 AI 明確地對自己的推理進行推理。

範例：「我優先考慮較便宜的航班，因為… 可能會錯過直航航班，讓我再檢查一遍。」。
跟蹤它為何或如何選擇某條路線。
- 注意到它犯錯是因過度依賴上次用戶偏好，因此不只修改最終建議，還調整其決策策略。
- 診斷模式，如：「每當我看到用戶提到『太擠』，我不僅要刪除某些景點，還要反思如果我總是根據人氣排名選擇『熱門景點』，那麼我的方法本身就是錯的。」

### 元認知在 AI 代理中的重要性

元認知在 AI 代理設計中扮演關鍵角色，原因包括：

![元認知的重要性](../../../translated_images/zh-MO/importance-of-metacognition.b381afe9aae352f7.webp)

- 自我反思：代理能評估自身表現並找出改進空間。
- 適應能力：代理能根據過去經驗及變化環境調整策略。
- 錯誤修正：代理可自主偵測並修正錯誤，提高準確度。
- 資源管理：代理能透過規劃與評估行動，優化資源利用，如時間與計算能量。

## AI 代理的組成部分

在探討元認知過程前，了解 AI 代理的基本組成部分至關重要。AI 代理通常包含：

- 角色特性：代理的個性與特質，定義其與用戶互動的方式。
- 工具：代理所具備的能力與功能。
- 技能：代理擁有的知識與專長。

這些組件合作建立「專業單元」，可執行特定任務。

<strong>範例</strong>：
想像一個旅行代理，不僅規劃假期，還能根據實時資料與過往客戶旅程經驗調整其規劃路線。

### 範例：旅行代理服務中的元認知

想像您正在設計一個由 AI 驅動的旅行代理服務。該代理「旅行代理」協助用戶規劃假期。為融入元認知，旅行代理需要根據自我覺察和過往經驗評估並調整其行動。元認知在此的角色如下：

#### 目前任務

目前任務是幫助用戶規劃巴黎之行。

#### 完成任務的步驟

1. <strong>收集用戶偏好</strong>：詢問用戶的旅行日期、預算、興趣（博物館、美食、購物等）及任何特定需求。
2. <strong>資料檢索</strong>：搜尋符合用戶偏好的航班選項、住宿、景點及餐廳。
3. <strong>生成建議</strong>：提供包含航班細節、飯店預訂和建議活動的個人化行程。
4. <strong>根據回饋調整</strong>：請用戶對建議提供回饋，並做必要調整。

#### 所需資源

- 訪問航班和飯店訂房資料庫。
- 巴黎景點及餐廳資訊。
- 來自先前互動的用戶回饋數據。

#### 經驗與自我反思

旅行代理利用元認知評估其表現並從過往經驗中學習。例如：

1. <strong>分析用戶回饋</strong>：旅行代理檢視用戶回饋，判斷哪些建議受歡迎，哪些不受歡迎，並相應調整未來建議。
2. <strong>適應能力</strong>：若用戶曾提及不喜歡人多的地方，旅行代理未來會避免在高峰時段推薦熱門景點。
3. <strong>錯誤修正</strong>：如果旅行代理之前出錯，例如建議已滿房的飯店，它會學會在建議前更嚴格檢查可用性。

#### 開發者實務範例

以下為融入元認知的旅行代理簡化程式碼範例：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # 根據偏好搜尋航班、酒店及景點
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
        # 分析反饋並調整未來推薦
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

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
travel_agent.adjust_based_on_feedback(feedback)
```

#### 為何元認知重要

- <strong>自我反思</strong>：代理能分析自身表現並找出改進方向。
- <strong>適應能力</strong>：代理依據回饋與環境變化調整策略。
- <strong>錯誤修正</strong>：代理能自主偵測並修正錯誤。
- <strong>資源管理</strong>：代理能優化如時間和計算資源的使用。

融入元認知後，旅行代理能提供更個人化且準確的旅行建議，提升整體用戶體驗。

---

## 2. 代理中的規劃

規劃是 AI 代理行為的重要組件。它涉及列出達成目標所需步驟，考慮當前狀態、可用資源和可能障礙。

### 規劃要素

- <strong>當前任務</strong>：明確定義任務。
- <strong>完成任務步驟</strong>：將任務拆解為可管理步驟。
- <strong>所需資源</strong>：確認必要資源。
- <strong>經驗</strong>：利用過往經驗輔助規劃。

<strong>範例</strong>：
旅行代理需執行以下步驟以有效協助用戶規劃旅程：

### 旅行代理步驟

1. <strong>收集用戶偏好</strong>
   - 詢問用戶旅行日期、預算、興趣及任何特定需求。
   - 範例：「您打算何時出行？」「預算範圍是多少？」「假期喜歡哪些活動？」

2. <strong>資訊檢索</strong>
   - 根據用戶偏好搜尋相關旅遊選項。
   - <strong>航班</strong>：尋找符合用戶預算與旅行日期的航班。
   - <strong>住宿</strong>：尋找符合地點、價格與設施偏好的飯店或出租房。
   - <strong>景點與餐廳</strong>：辨識符合用戶興趣的熱門景點、活動和餐飲選項。

3. <strong>生成建議</strong>
   - 將檢索的資訊彙整成個人化行程。
   - 提供諸如航班選擇、飯店預訂及建議活動，確保建議符合用戶偏好。

4. <strong>呈現行程給用戶</strong>
   - 與用戶分享建議行程以供審閱。
   - 範例：「這是為您規劃的巴黎旅程建議行程，包括航班細節、飯店預訂及推薦活動和餐廳。請告訴我您的想法！」

5. <strong>收集回饋</strong>
   - 詢問用戶對建議行程的回饋。
   - 範例：「您喜歡這些航班選擇嗎？」「飯店是否符合您的需求？」「是否有想新增或刪除的活動？」

6. <strong>根據回饋調整</strong>
   - 根據用戶回饋修改行程。
   - 調整航班、住宿及活動建議，讓行程更符合用戶偏好。

7. <strong>最終確認</strong>
   - 將更新後的行程呈現給用戶做最後確認。
   - 範例：「我已根據您的回饋做出調整。這是更新後的行程，請問一切是否符合您的期待？」

8. <strong>預訂及確認</strong>
   - 用戶批准後，進行航班、住宿及預先安排活動的預訂。
   - 將確認資料發送給用戶。

9. <strong>持續支援</strong>
   - 在旅程前及期間，隨時為用戶提供變更或額外需求的協助。
   - 範例：「若您旅途中需要進一步協助，隨時聯絡我！」

### 範例互動

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

# 在負面評價請求中的使用範例
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

## 3. 校正型 RAG 系統

首先讓我們了解 RAG 工具與先發上下文載入的差異

![RAG 與上下文載入比較](../../../translated_images/zh-MO/rag-vs-context.9eae588520c00921.webp)

### 檢索增強生成 (RAG)

RAG 結合檢索系統與生成模型。當有查詢時，檢索系統會從外部資源調取相關文件或數據，並用這些檢索到的資訊增強生成模型的輸入，幫助模型產生更準確且符合上下文的回應。

在 RAG 系統中，代理會從知識庫檢索相關資訊，並用以生成合適的回應或行動。

### 校正型 RAG 方法

校正型 RAG 方法專注於使用 RAG 技術修正錯誤並提升 AI 代理的準確性。此方法包含：

1. <strong>提示技術</strong>：利用特定提示引導代理檢索相關資訊。
2. <strong>工具</strong>：實作算法與機制，使代理能評估檢索資訊的相關性並生成精準回應。
3. <strong>評估</strong>：持續評估代理表現並作調整，以提升準確度與效率。

#### 範例：搜尋代理的校正型 RAG

以一個從網路檢索資訊回答用戶查詢的搜尋代理為例。校正型 RAG 方法可能涉及：

1. <strong>提示技術</strong>：根據用戶輸入形成搜尋查詢。
2. <strong>工具</strong>：使用自然語言處理與機器學習算法對搜尋結果進行排序和過濾。
3. <strong>評估</strong>：透過分析用戶回饋識別並修正檢索資訊的不準確。

### 旅行代理中的校正型 RAG

校正型 RAG（檢索增強生成）強化 AI 在檢索與生成資訊時糾正錯誤的能力。讓我們看看旅行代理如何利用校正型 RAG 方法，提供更準確和相關的旅行建議。

這包括：

- **提示技術：** 使用特定提示引導代理檢索相關資訊。
- **工具：** 實作算法與機制，使代理評估檢索資訊的相關性並生成精準回應。
- **評估：** 持續評估代理表現並作調整，以提升準確度與效率。

#### 在旅行代理中實施校正型 RAG 的步驟

1. <strong>初步用戶互動</strong>
   - 旅行代理從用戶收集初始偏好，如目的地、旅行日期、預算及興趣。
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
   - 旅行代理基於用戶偏好檢索航班、住宿、景點和餐廳資訊。
   - 範例：

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. <strong>生成初步建議</strong>
   - 旅行代理利用檢索到的資訊生成個人化行程。
   - 範例：

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. <strong>收集用戶回饋</strong>
   - 旅行代理請用戶對初步建議提供回饋。
   - 範例：

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **校正型 RAG 過程**
   - <strong>提示技術</strong>：旅行代理根據用戶回饋形成新的搜尋查詢。
     - 範例：

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - <strong>工具</strong>：旅行代理運用算法對新搜尋結果進行排序與過濾，強調根據用戶回饋的相關性。
     - 範例：

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - <strong>評估</strong>：旅行代理持續評估建議的相關性與準確性，分析用戶回饋並做必要調整。
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

#### 實務範例

以下為融入校正型 RAG 方法的簡化 Python 代碼示例，用於旅行代理：

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

# 使用示例
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

### 先發上下文載入


預先載入上下文涉及在處理查詢之前，將相關的上下文或背景資訊載入模型。這意味著模型從一開始就能訪問這些資訊，這有助於它產生更有見地的回應，而不需要在過程中額外檢索資料。

這裡是一個關於旅行代理應用程式在 Python 中如何進行預先載入上下文的簡化範例：

```python
class TravelAgent:
    def __init__(self):
        # 預先載入熱門目的地及其資訊
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # 從預先載入的上下文中提取目的地資訊
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

1. **初始化（`__init__` 方法）**：`TravelAgent` 類別預先載入了一個字典，包含了巴黎、東京、紐約和悉尼等熱門目的地的資訊。該字典包括每個目的地的國家、貨幣、語言和主要景點等細節。

2. **取得資訊（`get_destination_info` 方法）**：當使用者查詢特定的目的地時，`get_destination_info` 方法會從預先載入的上下文字典中擷取相關資訊。

透過預先載入上下文，旅行代理應用程式能快速回應使用者查詢，而無需在實時從外部來源檢索訊息。這讓應用程式更高效且回應迅速。

### 在迭代前以目標引導規劃

以目標引導規劃涉及從明確的目標或預期結果開始。透過預先定義此目標，模型能在整個迭代過程中將其作為指導原則。這有助於確保每次迭代都更接近達成預期結果，使流程更有效率且專注。

這裡是一個示例，說明如何在 Python 中為旅行代理以目標引導旅行計劃，再進行迭代：

### 情境

一位旅行代理想為客戶規劃一個定制化假期。目標是建立一個最大化客戶滿意度的旅遊行程，根據其偏好和預算制定。

### 步驟

1. 定義客戶的偏好和預算。
2. 依據這些偏好啟動初步計劃。
3. 透過迭代精煉計劃，優化客戶滿意度。

#### Python 程式碼

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

1. **初始化（`__init__` 方法）**：`TravelAgent` 類別以一個潛在目的地清單初始化，每個目的地具有名稱、費用及活動類型等屬性。

2. **啟動計劃（`bootstrap_plan` 方法）**：根據客戶的偏好和預算，此方法創建初步旅行計劃。它迭代清單中的目的地，若符合客戶偏好且預算範圍內，將其加入計劃。

3. **匹配偏好（`match_preferences` 方法）**：此方法檢查某目的地是否符合客戶偏好。

4. **迭代計劃（`iterate_plan` 方法）**：此方法透過嘗試以更佳匹配替換計劃中的每個目的地，考量客戶偏好與預算限制，來優化初步計劃。

5. **計算費用（`calculate_cost` 方法）**：此方法計算目前計劃總費用，包含可能加入的新目的地。

#### 範例使用

- <strong>初始計劃</strong>：旅行代理根據客戶對觀光的偏好及 2000 美元預算制訂初步計劃。
- <strong>精煉計劃</strong>：旅行代理透過迭代優化計劃，符合客戶偏好與預算。

透過以明確目標（如最大化客戶滿意度）啟動計劃，並通過迭代精煉，旅行代理可為客戶創造定制且優化的旅遊行程。此方法能確保旅遊計劃一開始就與客戶偏好和預算一致，且隨著每次迭代得以改善。

### 利用大型語言模型（LLM）進行重排和評分

大型語言模型（LLM）可用於重排和評分，透過評估檢索到的文件或生成的回應的相關性和品質。其運作方式如下：

**檢索：** 初始檢索步驟根據查詢擷取一組候選文件或回應。

**重排：** LLM 評估這些候選項，並根據其相關性和品質重新排序。此步驟確保最相關且高品質的資訊優先呈現。

**評分：** LLM 對每個候選項給予分數，反映其相關性和品質，有助於選出最佳回應或文件。

透過利用 LLM 進行重排和評分，系統能提供更精確和符合語境的資訊，提升整體用戶體驗。

這裡是一個旅行代理如何使用大型語言模型（LLM）根據用戶偏好重排和評分旅行目的地的 Python 範例：

#### 情境 — 根據偏好選擇旅行目的地

旅行代理想根據客戶偏好推薦最佳旅行目的地。LLM 將協助重排並評分這些目的地，確保呈現最相關的選項。

#### 步驟：

1. 收集用戶偏好。
2. 擷取一份潛在旅行目的地清單。
3. 利用 LLM 根據用戶偏好重排並評分目的地。

以下示範如何將前述範例更新為使用 Azure OpenAI 服務：

#### 需求

1. 你需要有 Azure 訂閱。
2. 創建 Azure OpenAI 資源並取得你的 API 金鑰。

#### Python 範例程式碼

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # 生成 Azure OpenAI 的提示
        prompt = self.generate_prompt(preferences)
        
        # 定義請求的標頭和負載
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # 調用 Azure OpenAI API 以獲取重新排序及評分的目的地
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # 提取並返回建議
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

# 使用例子
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

#### 程式碼說明 — 偏好訂製者

1. <strong>初始化</strong>：`TravelAgent` 類別以潛在旅行目的地清單初始化，每個目的地具有名稱和描述等屬性。

2. **取得推薦（`get_recommendations` 方法）**：此方法根據用戶偏好產生給 Azure OpenAI 服務的提示（prompt），並藉由 HTTP POST 請求呼叫 Azure OpenAI API，取得重排與評分的目的地結果。

3. **產生提示（`generate_prompt` 方法）**：此方法構建 Azure OpenAI 的提示內容，包括用戶偏好與目的地清單。此提示引導模型根據提供的偏好重排和評分目的地。

4. **API 呼叫**：使用 `requests` 函式庫發送 HTTP POST 請求到 Azure OpenAI API 端點。回應涵蓋重排與評分後的目的地結果。

5. <strong>範例使用</strong>：旅行代理收集用戶偏好（例如對觀光和多元文化感興趣），並使用 Azure OpenAI 服務獲得重排與評分的旅行目的地推薦。

請務必將 `your_azure_openai_api_key` 替換成你實際的 Azure OpenAI API 金鑰，並將 `https://your-endpoint.com/...` 替換成你 Azure OpenAI 部署的實際端點 URL。

透過利用 LLM 進行重排和評分，旅行代理能夠為客戶提供更個人化且相關的旅行推薦，增強整體體驗。

### RAG：提示技術 vs 工具

檢索增強生成（RAG）既可以是一種提示技術，也可以是一種工具，應用於 AI 代理的開發。理解兩者的區別有助於你更有效地在專案中利用 RAG。

#### RAG 作為提示技術

**什麼是它？**

- 作為提示技術，RAG 涉及制定具體查詢或提示，以引導從大型語料庫或資料庫中檢索相關資訊。該資訊隨後用來生成回應或執行行動。

**其運作方式：**

1. <strong>制定提示</strong>：根據手頭任務或使用者輸入創建結構良好的提示或查詢。
2. <strong>檢索資訊</strong>：利用提示從現有知識庫或資料集中搜尋相關資料。
3. <strong>生成回應</strong>：將檢索到的資訊與生成式 AI 模型結合，以產生完整且連貫的回應。

**旅行代理範例：**

- 使用者輸入：「我想參觀巴黎的博物館。」
- 提示：「找出巴黎頂級博物館。」
- 檢索資訊：羅浮宮博物館、奧賽美術館等細節。
- 生成回應：「這裡有一些巴黎的頂級博物館：羅浮宮博物館、奧賽美術館與蓬皮杜藝術中心。」

#### RAG 作為工具

**什麼是它？**

- 作為工具，RAG 是一套整合系統，自動化檢索與生成流程，讓開發者無需為每個查詢手動撰寫提示即可實現複雜 AI 功能。

**其運作方式：**

1. <strong>整合</strong>：將 RAG 嵌入 AI 代理架構，自動處理檢索與生成任務。
2. <strong>自動化</strong>：工具管理整個流程，從接收使用者輸入到生成最終回應，無需為每步驟設定明確提示。
3. <strong>效率</strong>：透過精簡檢索與生成流程，提升代理效能，使回應更快且更準確。

**旅行代理範例：**

- 使用者輸入：「我想參觀巴黎的博物館。」
- RAG 工具：自動檢索博物館資訊並生成回應。
- 生成回應：「這裡有一些巴黎的頂級博物館：羅浮宮博物館、奧賽美術館與蓬皮杜藝術中心。」

### 比較

| 方面                  | 提示技術                                        | 工具                                                  |
|-----------------------|------------------------------------------------|-------------------------------------------------------|
| **手動 vs 自動**       | 為每個查詢手動制定提示。                       | 自動化檢索與生成過程。                               |
| <strong>控制度</strong>             | 對檢索過程提供更多控制。                       | 精簡並自動化檢索與生成。                             |
| <strong>彈性</strong>               | 可根據具體需求定制提示。                       | 適合大規模實施，更高效。                             |
| <strong>複雜度</strong>             | 需撰寫並調整提示。                             | 易於整合入 AI 代理架構。                             |

### 實務範例

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

評估相關性是 AI 代理效能的重要面向。它確保代理檢索和生成的資訊是適當、準確且對使用者有用。讓我們探索如何評估 AI 代理的相關性，包括實務範例與技巧。

#### 評估相關性的關鍵概念

1. <strong>上下文感知</strong>：
   - 代理必須了解使用者查詢的上下文，以檢索與生成相關資訊。
   - 範例：如果使用者詢問「巴黎有哪些最佳餐廳」，代理應考慮使用者的偏好，如料理種類與預算。

2. <strong>準確性</strong>：
   - 代理提供的資訊應該是事實正確且最新的。
   - 範例：推薦目前營業且評價良好的餐廳，而非過時或已關閉選項。

3. <strong>用戶意圖</strong>：
   - 代理應該推斷使用者查詢背後的意圖，以提供最相關的資訊。
   - 範例：使用者查詢「經濟型飯店」，代理應優先推薦負擔得起的選項。

4. <strong>回饋迴路</strong>：
   - 持續收集並分析用戶回饋，有助於代理改進其相關性評估流程。
   - 範例：納入用戶對先前推薦的評分與回饋，以優化未來回應。

#### 評估相關性的實務技巧

1. <strong>相關性打分</strong>：
   - 根據檢索項目與使用者查詢及偏好的契合度，給予相關性分數。
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

2. <strong>篩選與排序</strong>：
   - 過濾掉不相關項目，並根據相關性分數排序剩餘項目。
   - 範例：

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # 返回前10個相關項目
     ```

3. **自然語言處理（NLP）**：
   - 使用 NLP 技術理解使用者查詢並檢索相關資訊。
   - 範例：

     ```python
     def process_query(query):
         # 使用NLP從用戶的查詢中提取關鍵資訊
         processed_query = nlp(query)
         return processed_query
     ```

4. <strong>用戶回饋整合</strong>：
   - 收集對提供推薦的用戶回饋，並用於調整未來的相關性評估。
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

#### 範例：旅行代理評估相關性

以下是旅行代理如何評估旅行推薦相關性的實務範例：

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
        return ranked_items[:10]  # 返回前十個相關項目

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
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### 目標搜尋

目標搜尋涉及理解並詮釋使用者查詢背後的目的或目標，以檢索並生成最相關且有用的資訊。這種方法不僅是匹配關鍵詞，而是重點把握使用者的實際需求和上下文。

#### 目標搜尋中的關鍵概念

1. <strong>理解使用者意圖</strong>：
   - 使用者意圖可分為資訊型、導航型和交易型三大類。
     - <strong>資訊型意圖</strong>：使用者尋找某主題的資訊（例如：「巴黎最佳博物館有哪些？」）。
     - <strong>導航型意圖</strong>：使用者想前往特定網站或頁面（例如：「羅浮宮博物館官方網站」）。
     - <strong>交易型意圖</strong>：使用者欲進行交易，如訂機票或購物（例如：「訂一張飛往巴黎的機票」）。

2. <strong>上下文感知</strong>：
   - 分析使用者查詢的上下文有助準確識別其意圖，包括考慮過往互動、用戶偏好及當前查詢的具體細節。

3. **自然語言處理（NLP）**：
   - 採用 NLP 技術理解及詮釋使用者的自然語言查詢，涵蓋實體識別、情感分析與查詢解析等任務。

4. <strong>個人化</strong>：
   - 根據使用者歷史、偏好與回饋個人化搜尋結果，提升檢索資訊的相關性。

#### 實務範例：在旅行代理中實施目標搜尋

以旅行代理為例，看看如何實現目標搜尋。

1. <strong>收集使用者偏好</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. <strong>理解使用者意圖</strong>

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. <strong>上下文感知</strong>


   ```python
   def analyze_context(query, user_history):
       # 結合當前查詢與用戶歷史以理解語境
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. <strong>搜索並個人化結果</strong>

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
       # 範例個人化邏輯
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # 回傳前 10 個個人化結果
   ```

5. <strong>範例使用</strong>

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

## 4. 作為工具的碼生成

代碼生成代理使用 AI 模型來撰寫和執行代碼，以解決複雜問題及自動化任務。

### 代碼生成代理

代碼生成代理使用生成式 AI 模型來撰寫和執行代碼。這些代理能夠解決複雜問題、自動化任務，並通過生成和運行各種程式語言的代碼提供有價值的見解。

#### 實際應用

1. <strong>自動代碼生成</strong>：為特定任務生成代碼片段，例如數據分析、網絡爬蟲或機器學習。
2. **以 SQL 作為 RAG**：使用 SQL 查詢從資料庫檢索和操作數據。
3. <strong>問題解決</strong>：創建並執行代碼以解決特定問題，例如優化演算法或分析數據。

#### 範例：用於數據分析的代碼生成代理

假設你正在設計一個代碼生成代理。它的工作方式如下：

1. <strong>任務</strong>：分析數據集以識別趨勢和模式。
2. <strong>步驟</strong>：
   - 將數據集載入數據分析工具。
   - 生成 SQL 查詢來篩選和彙總數據。
   - 執行查詢並檢索結果。
   - 使用結果生成視覺化和見解。
3. <strong>所需資源</strong>：訪問數據集、數據分析工具和 SQL 功能。
4. <strong>經驗</strong>：使用過去的分析結果提升未來分析的準確性和相關性。

### 範例：用於旅行代理的代碼生成代理

在此範例中，我們將設計一個名為 Travel Agent 的代碼生成代理，幫助用戶通過生成和執行代碼來規劃旅行。此代理可處理如獲取旅行選項、篩選結果及利用生成式 AI 編制行程等任務。

#### 代碼生成代理概述

1. <strong>收集用戶偏好</strong>：收集用戶輸入的目的地、旅行日期、預算和興趣。
2. <strong>生成代碼以獲取數據</strong>：生成代碼片段以檢索航班、酒店和景點的信息。
3. <strong>執行生成代碼</strong>：運行生成的代碼以獲取即時資訊。
4. <strong>生成行程</strong>：將獲取的資料彙編為個性化旅行計劃。
5. <strong>根據反饋調整</strong>：接收用戶反饋並在必要時重新生成代碼以優化結果。

#### 分步實施

1. <strong>收集用戶偏好</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. <strong>生成代碼以獲取數據</strong>

   ```python
   def generate_code_to_fetch_data(preferences):
       # 示例：產生代碼以根據用戶偏好搜索航班
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # 示例：產生代碼以搜索酒店
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. <strong>執行生成代碼</strong>

   ```python
   def execute_code(code):
       # 使用 exec 執行生成的代碼
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

5. <strong>根據反饋調整</strong>

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

根據資料表的結構確實可以透過利用環境感知與推理來增強查詢生成過程。

以下是一個示範如何做到這點的例子：

1. <strong>理解結構</strong>：系統會了解資料表的結構，並利用該資訊來定位查詢生成。
2. <strong>根據反饋調整</strong>：系統會根據反饋調整用戶偏好，並推理出結構中哪些欄位需要更新。
3. <strong>生成與執行查詢</strong>：系統會根據新偏好生成並執行查詢，以獲取更新的航班和酒店資料。

下方是一個結合這些概念的更新 Python 代碼範例：

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # 根據用戶反饋調整偏好設定
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # 根據架構推理以調整其他相關偏好
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # 基於架構和反饋自訂邏輯以調整偏好
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # 生成根據更新偏好取得航班資料的程式碼
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # 生成根據更新偏好取得酒店資料的程式碼
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # 模擬執行程式碼並返回模擬資料
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # 根據航班、酒店和景點生成行程
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# 範例架構
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# 範例用法
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# 重新生成並執行包含更新偏好的程式碼
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### 解說 - 依據反饋進行預訂

1. <strong>結構感知</strong>：`schema` 字典定義了如何根據反饋調整偏好，其中包括 `favorites` 和 `avoid` 等欄位及相應的調整。
2. **調整偏好（`adjust_based_on_feedback` 方法）**：此方法根據用戶反饋和結構調整偏好。
3. **基於環境的調整（`adjust_based_on_environment` 方法）**：該方法根據結構和反饋定制調整內容。
4. <strong>生成並執行查詢</strong>：系統生成代碼以根據調整後的偏好獲取更新的航班和酒店資料，並模擬執行這些查詢。
5. <strong>生成行程</strong>：系統根據新的航班、酒店和景點資料製作更新的行程。

透過使系統具有環境感知並基於結構推理，它能生成更準確且相關的查詢，從而提供更佳的旅行推薦和更個人化的用戶體驗。

### 將 SQL 作為檢索增強生成（RAG）技術

SQL（結構化查詢語言）是一個強大的資料庫互動工具。當作為檢索增強生成（RAG）方法一部分使用時，SQL 能從資料庫檢索相關數據，用以指導並生成 AI 代理的回答或行動。讓我們探討如何在 Travel Agent 中以 RAG 技術使用 SQL。

#### 主要概念

1. <strong>資料庫互動</strong>：
   - SQL 用於查詢資料庫、檢索相關資訊及操作數據。
   - 例如：從旅遊資料庫獲取航班詳情、酒店資訊和景點資料。

2. **與 RAG 整合**：
   - 根據用戶輸入和偏好生成 SQL 查詢。
   - 取得的數據用於生成人性化推薦或行動建議。

3. <strong>動態查詢生成</strong>：
   - AI 代理根據上下文和用戶需求生成動態 SQL 查詢。
   - 例如：自訂 SQL 查詢以基於預算、日期和興趣過濾結果。

#### 應用範例

- <strong>自動代碼生成</strong>：生成特定任務的代碼片段。
- **以 SQL 作為 RAG**：使用 SQL 查詢來操作數據。
- <strong>問題解決</strong>：創建並執行代碼以解決問題。

<strong>範例</strong>：
一個數據分析代理：

1. <strong>任務</strong>：分析數據集找出趨勢。
2. <strong>步驟</strong>：
   - 載入數據集。
   - 生成 SQL 查詢來篩選數據。
   - 執行查詢並檢索結果。
   - 生成視覺化圖表和見解。
3. <strong>資源</strong>：數據集存取、SQL 功能。
4. <strong>經驗</strong>：利用過去結果提升未來分析。

#### 實務範例：在 Travel Agent 中使用 SQL

1. <strong>收集用戶偏好</strong>

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

2. <strong>酒店查詢</strong>

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. <strong>景點查詢</strong>

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

透過將 SQL 作為檢索增強生成（RAG）技術的一部分，像 Travel Agent 這類 AI 代理可以動態取得和利用相關數據，提供精確且個人化的推薦。

### 元認知範例

為了展示元認知的實作，我們來創建一個簡單代理，它在解決問題的同時<em>反思其決策過程</em>。在本例中，代理試圖優化酒店選擇，但在發現錯誤或次優決策時，會評估自身推理並調整策略。

我們將用一個基本例子來模擬，代理基於價格和品質的組合選擇酒店，且會「反思」其決策，並作相應調整。

#### 這如何展示元認知：

1. <strong>初始決策</strong>：代理會挑選最便宜的酒店，未理解品質對決策的影響。
2. <strong>反思與評估</strong>：初次選擇後，代理會利用用戶反饋檢查該酒店是否為「不佳」選擇，若發現品質太低，便反思自己的推理。
3. <strong>調整策略</strong>：代理基於反思調整策略，從「最便宜」轉變為「最高品質」，從而在未來迭代中改善決策過程。

以下是一個示例：

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # 儲存之前選擇的酒店
        self.corrected_choices = []  # 儲存更正後的選擇
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
        # 假設我們有一些用戶反饋，告訴我們最後的選擇是否好
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # 若之前的選擇不理想，調整策略
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

# 模擬一組酒店列表（價格與質量）
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# 創建一個代理人
agent = HotelRecommendationAgent()

# 第一步：代理人使用「最便宜」策略推薦酒店
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# 第二步：代理人反思選擇，如有需要調整策略
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# 第三步：代理人再次推薦，這次使用調整後的策略
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### 代理的元認知能力

關鍵在於代理能夠：
- 評估其先前的選擇與決策過程。
- 根據反思調整策略，即元認知的實際應用。

這是一種簡單的元認知形式，系統能根據內部反饋調整其推理過程。

### 結論

元認知是一個強大的工具，可顯著提升 AI 代理的能力。透過納入元認知過程，你可以設計更智能、適應性更強且效率更高的代理。請使用額外資源進一步探索 AI 代理中元認知的精彩世界。

### 對元認知設計模式有更多疑問？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者互動，參加辦公時間並獲得 AI 代理相關問題的解答。

## 上一課

[多代理設計模式](../08-multi-agent/README.md)

## 下一課

[AI 代理在生產環境](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->