[![多智能體設計](../../../translated_images/zh-HK/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(點擊上方圖片觀看本課程影片)_
# AI 智能體中的後設認知

## 簡介

歡迎來到 AI 智能體後設認知的課程！本章節專為好奇 AI 智能體如何思考自我思維過程的初學者設計。完成本課程後，您將了解關鍵概念，並掌握應用後設認知於 AI 智能體設計的實用範例。

## 學習目標

完成本課程後，您將能夠：

1. 理解推理迴圈在智能體定義中的影響。
2. 利用規劃與評估技術協助自我修正的智能體。
3. 創建能操控程式碼以完成任務的智能體。

## 後設認知介紹

後設認知指的是涉及思考自我思維的高階認知過程。對於 AI 智能體來說，這意味著能根據自我意識與過往經驗評估並調整其行動。後設認知，或稱「對思考的思考」，是智能體 AI 系統發展中的重要概念。它包含 AI 系統認識自身內部過程，且能監控、調節及適應其行為。就像我們在觀察環境或分析問題時所做的那樣。這種自我意識能幫助 AI 系統做出更佳決策、識別錯誤，並持續提升運作表現——再次聯想到圖靈測試及 AI 是否將掌控世界的爭論。

在智能體 AI 系統的範疇中，後設認知可幫助解決數項挑戰，例如：
- 透明度：確保 AI 系統能解釋其推理與決策。
- 推理能力：提升 AI 系統綜合資訊並做出合理決策的能力。
- 適應能力：使 AI 系統能調整以適應新環境與變化條件。
- 感知能力：改善 AI 系統對環境資料的準確識別及解讀。

### 什麼是後設認知？

後設認知，或稱「對思考的思考」，係一種高階認知過程，包含自我覺察與自我調節自身的認知過程。在 AI 範疇中，後設認知使智能體能評估及調整其策略與行動，促進問題解決及決策能力的提升。理解後設認知後，您可以設計出不僅更聰明且更具適應性與效率的 AI 智能體。真正的後設認知會讓 AI 明確推理其自身的推理過程。

範例：「我優先選擇較便宜的航班，因為……可能會錯過直飛航班，讓我重新檢查一下。」。
追蹤它選擇特定路徑的原因或方式。
- 注意它因過度依賴上次的用戶偏好而犯錯，故不只修改最終建議，也改變決策策略。
- 診斷模式，例如：「當我看到用戶提到‘太擁擠’時，我不只是移除某些景點，也應反思 若只依人氣排序‘熱門景點’的方法是有缺陷的。」

### 後設認知在 AI 智能體中的重要性

後設認知在 AI 智能體設計上扮演關鍵角色，原因包括：

![後設認知的重要性](../../../translated_images/zh-HK/importance-of-metacognition.b381afe9aae352f7.webp)

- 自我反思：智能體可評估自身表現並識別需改進之處。
- 適應性：智能體能根據過去經驗和環境變化調整策略。
- 錯誤修正：智能體可自主偵測與修正錯誤，提高結果準確度。
- 資源管理：智能體透過規劃與評估行動，優化時間及計算資源的使用。

## AI 智能體的組件

在深入後設認知過程前，理解 AI 智能體的基本組件至關重要。AI 智能體通常包含：

- 角色特性：智能體的個性能及特徵，決定其與用戶互動方式。
- 工具：智能體可執行的功能與能力。
- 技能：智能體擁有的知識和專業能力。

這些組成部分攜手合作，形成能執行特定任務的「專業單元」。

<strong>範例</strong>：
想想看旅行代理智能體，它不僅規劃您的假期，且能依據即時數據及客戶過往旅程經驗調整行程。

### 範例：旅行代理服務中的後設認知

假設您設計一個由 AI 驅動的旅行代理服務。這個智能體「Travel Agent」協助用戶規劃假期。為融合後設認知，Travel Agent 需要基於自我覺察及過去經驗，評估並調整其行動。後設認知可具體體現於：

#### 當前任務

目前任務是協助用戶規劃巴黎之旅。

#### 完成任務的步驟

1. <strong>收集用戶偏好</strong>：詢問用戶旅行日期、預算、興趣（如博物館、美食、購物）及任何特殊需求。
2. <strong>檢索資訊</strong>：尋找符合用戶偏好的航班、住宿、景點及餐廳資訊。
3. <strong>生成建議</strong>：提供包含航班詳情、飯店預訂和推薦活動的個人化行程。
4. <strong>根據反饋調整</strong>：詢問用戶對建議的意見，並進行必要調整。

#### 需要的資源

- 存取航班及飯店預訂資料庫。
- 巴黎景點與餐廳資訊。
- 來自先前互動的用戶反饋數據。

#### 經驗與自我反思

Travel Agent 利用後設認知來評估其績效，並從過往經驗中學習。例如：

1. <strong>分析用戶反饋</strong>：Travel Agent 評估用戶回饋，判斷哪些建議受歡迎，哪些不佳，並相應調整未來建議。
2. <strong>適應性</strong>：若用戶先前表明不喜擁擠場所，Travel Agent 未來會避免在高峰時間推薦熱門景點。
3. <strong>錯誤修正</strong>：若 Travel Agent 過去建議了已額滿的飯店，會學習更嚴謹地查核可用性再做推薦。

#### 實務開發者範例

以下為 Travel Agent 代碼融合後設認知的簡化範例：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # 根據偏好搜尋航班、酒店和景點
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

#### 為何後設認知重要

- <strong>自我反思</strong>：智能體能分析其表現，找出需改進之處。
- <strong>適應性</strong>：智能體可依反饋與變化條件調整策略。
- <strong>錯誤修正</strong>：智能體能自主偵測並修正錯誤。
- <strong>資源管理</strong>：智能體能優化資源運用，如時間和計算能力。

融入後設認知後，Travel Agent 能提供更個人化且準確的旅遊建議，提高整體用戶體驗。

---

## 2. 智能體中的規劃

規劃是 AI 智能體行為的重要組成，涵蓋訂定達成目標所需步驟，並考量現狀、資源及潛在障礙。

### 規劃要素

- <strong>當前任務</strong>：明確定義任務。
- <strong>完成任務步驟</strong>：將任務劃分為易管理的步驟。
- <strong>所需資源</strong>：識別必要資源。
- <strong>經驗</strong>：利用過去經驗指導規劃。

<strong>範例</strong>：
以下為 Travel Agent 助用戶有效規劃旅程需執行的步驟：

### Travel Agent 步驟

1. <strong>收集用戶偏好</strong>
   - 詢問用戶旅行日期、預算、興趣及任何特別需求。
   - 範例：「您計劃何時出行？」、「您的預算範圍是多少？」、「您喜歡假期中參與哪些活動？」

2. <strong>檢索資訊</strong>
   - 根據用戶偏好搜尋相關旅遊選項。
   - <strong>航班</strong>：尋找預算內且在用戶偏好日期的可用航班。
   - <strong>住宿</strong>：找到符合用戶地點、價格及設施偏好的飯店或租賃物件。
   - <strong>景點與餐廳</strong>：找出與用戶興趣相符的熱門景點、活動和餐飲選項。

3. <strong>生成建議</strong>
   - 將檢索到的資訊彙整成個人化行程。
   - 提供航班選擇、飯店預訂和建議活動細節，確保建議貼合用戶偏好。

4. <strong>向用戶呈現行程</strong>
   - 與用戶分享建議行程讓其審閱。
   - 範例：「這是為您規劃的巴黎行程，包含航班資訊、飯店預訂及推薦活動與餐廳清單。請告訴我您的想法！」

5. <strong>收集反饋</strong>
   - 詢問用戶對建議行程的看法。
   - 範例：「您喜歡這些航班選擇嗎？」「這間飯店符合您的需求嗎？」「您想加減哪些活動？」

6. <strong>根據反饋調整</strong>
   - 根據用戶反饋修改行程。
   - 對航班、住宿及活動建議做必要調整，更吻合用戶偏好。

7. <strong>最終確認</strong>
   - 向用戶呈現更新後行程，請其最終確認。
   - 範例：「我已根據您的意見調整行程。這是更新版，您覺得還好嗎？」

8. <strong>預訂與確認</strong>
   - 用戶確認行程後，進行航班、住宿及預定活動。
   - 將確認詳情發送給用戶。

9. <strong>持續支援</strong>
   - 在用戶旅程前及期間，隨時提供協助及處理額外需求。
   - 範例：「旅途中若需任何協助，隨時聯絡我！」

### 互動示範

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

# 在預訂請求中的範例用法
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

## 3. 糾正型 RAG 系統

首先，我們來理解 RAG 工具與預先載入上下文的區別。

![RAG 與上下文加載比較](../../../translated_images/zh-HK/rag-vs-context.9eae588520c00921.webp)

### 檢索增強生成（RAG）

RAG 結合了檢索系統與生成模型。當提出查詢時，檢索系統從外部資源檢索相關文件或資料，再將檢索到的資訊用於增強輸入給生成模型，有助模型產生更準確且具語境相關的回應。

在 RAG 系統中，智能體從知識庫檢索相關資訊，並用以生成適當回應或行動。

### 糾正型 RAG 方法

糾正型 RAG 的重點在於運用 RAG 技術來糾正錯誤與提升 AI 智能體精準度。這包括：

1. <strong>提示技術</strong>：利用特定提示引導智能體檢索相關資訊。
2. <strong>工具</strong>：實作演算法與機制，讓智能體評估檢索資訊的相關度並產生精確回應。
3. <strong>評估</strong>：持續評估智能體表現，並進行調整以提升準確率與效率。

#### 範例：搜尋智能體中的糾正型 RAG

想像一個從網路檢索資訊回應使用者查詢的搜尋智能體。糾正型 RAG 方法可能包含：

1. <strong>提示技術</strong>：根據用戶輸入構建搜尋查詢。
2. <strong>工具</strong>：使用自然語言處理及機器學習演算法對搜尋結果進行排名與篩選。
3. <strong>評估</strong>：分析用戶反饋，識別並糾正檢索資訊的不準確處。

### 旅行代理中的糾正型 RAG

糾正型 RAG（檢索增強生成）增強 AI 在檢索與生成資訊時糾正錯誤的能力。讓我們看看 Travel Agent 如何使用此方法來提供更準確且相關的旅行建議。

這包括：

- **提示技術：** 利用特定提示引導智能體檢索相關資訊。
- **工具：** 實作演算法與機制，讓智能體評估檢索結果相關度並產生精確回應。
- **評估：** 持續評估智能體表現並作調整，提升準確率與效率。

#### 在旅行代理中實作糾正型 RAG 的步驟

1. <strong>初步用戶互動</strong>
   - Travel Agent 收集用戶的初步偏好，如目的地、旅行日期、預算及興趣。
   - 範例：

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. <strong>檢索資訊</strong>
   - Travel Agent 根據用戶偏好檢索航班、住宿、景點與餐廳資訊。
   - 範例：

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. <strong>生成初步建議</strong>
   - Travel Agent 利用檢索到的資訊生成個人化行程。
   - 範例：

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. <strong>收集用戶反饋</strong>
   - Travel Agent 向用戶詢問對初步建議的意見。
   - 範例：

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **糾正型 RAG 過程**
   - <strong>提示技術</strong>：Travel Agent 根據用戶反饋制定新的搜尋查詢。
     - 範例：

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - <strong>工具</strong>：Travel Agent 使用演算法對新的搜尋結果進行排名與篩選，強調基於用戶反饋的相關性。
     - 範例：

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - <strong>評估</strong>：Travel Agent 持續分析用戶反饋，評估建議的相關性與精確度，並作必要調整。
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

以下為將糾正型 RAG 方法整合至 Travel Agent 的簡化 Python 代碼範例：

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


預先載入上下文是指在處理查詢前將相關的上下文或背景資訊載入模型。這意味著模型從一開始就可以訪問這些資訊，有助於它生成更具參考性的回答，而無需在過程中檢索額外資料。

下面是一個簡化的範例，展示在 Python 裡旅行代理應用如何執行預先載入上下文：

```python
class TravelAgent:
    def __init__(self):
        # 預先載入熱門目的地及其資料
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # 從預載內容中擷取目的地資料
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# 範例用法
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### 解釋

1. **初始化（`__init__` 方法）**：`TravelAgent` 類別預先載入一個包含熱門目的地資訊的字典，如巴黎、東京、紐約和雪梨。該字典包含每個目的地的國家、貨幣、語言和主要景點等細節。

2. **擷取資訊（`get_destination_info` 方法）**：當用戶查詢特定目的地時，`get_destination_info` 方法從預先載入的上下文字典中提取相關資訊。

透過預先載入上下文，旅行代理應用可以快速回應用戶查詢，無需實時從外部來源檢索資料。這使應用更有效率且更具回應性。

### 在迭代前先用目標啟動計畫

用目標啟動計畫是指以明確的目標或期望結果為起點。透過事先定義此目標，模型可以將其作為整個迭代過程的指導原則，有助於確保每次迭代表現更接近期望結果，使過程更有效率且聚焦。

以下是如何在 Python 中為旅行代理在迭代前用目標啟動旅行計畫的範例：

### 場景

一位旅行代理想為客戶規劃訂製假期。目標是根據客戶偏好和預算制定最大化滿意度的行程。

### 步驟

1. 定義客戶偏好和預算。
2. 根據這些偏好啟動初始計畫。
3. 迭代精煉計畫，以優化客戶滿意度。

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

# 使用範例
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

1. **初始化（`__init__` 方法）**：`TravelAgent` 類別初始化時帶有一組潛在目的地列表，每個目的地有名稱、成本和活動類型等屬性。

2. **啟動計畫（`bootstrap_plan` 方法）**：根據客戶偏好和預算創建初始旅行計畫。它會遍歷目的地列表，若符合偏好並在預算內，則將其加入計畫。

3. **匹配偏好（`match_preferences` 方法）**：檢查目的地是否符合客戶偏好。

4. **迭代計畫（`iterate_plan` 方法）**：透過嘗試用更符合偏好的目的地替換計畫中的地點，精煉初始計畫，同時考慮預算限制。

5. **計算成本（`calculate_cost` 方法）**：計算目前計畫總費用，包括可能的新目的地。

#### 範例用法

- <strong>初始計畫</strong>：旅行代理基於客戶的觀光偏好和 2000 美元預算制定初始行程。
- <strong>精煉計畫</strong>：旅行代理透過迭代精煉計畫，優化符合客戶偏好與預算。

透過以明確目標（例如最大化客戶滿意度）啟動計畫，並經過迭代精煉，旅行代理能為客戶制定訂製且最佳化的旅行行程。這確保從一開始行程就符合客戶偏好和預算，並隨著迭代不斷改善。

### 利用大型語言模型（LLM）進行重新排序和評分

大型語言模型（LLM）可以用於重新排序和評分，評估檢索到的文件或生成的回答的相關性和品質。其運作過程如下：

<strong>檢索</strong>：初步檢索根據查詢獲取候選文件或回答集合。

<strong>重新排序</strong>：LLM 評估這些候選項並按相關性及品質重新排序，確保最相關且高品質的資訊優先呈現。

<strong>評分</strong>：LLM 為每個候選項指派分數，反映其相關性和品質，有助於挑選最佳回答或文件。

透過利用 LLM 進行重新排序和評分，系統能提供更準確且符合上下文的資訊，提升整體用戶體驗。

以下是一個範例，展示旅行代理如何在 Python 中依用戶偏好利用大型語言模型（LLM）對旅遊目的地進行重新排序和評分：

#### 場景 - 根據偏好旅遊

旅行代理想根據客戶偏好推薦最佳旅遊目的地。LLM 將幫助重新排序並評分目的地，確保展示最相關選項。

#### 步驟：

1. 收集用戶偏好。
2. 檢索潛在旅遊目的地列表。
3. 使用 LLM 根據用戶偏好對目的地重新排序並評分。

以下示範如何更新前述範例以使用 Azure OpenAI 服務：

#### 需求

1. 需擁有 Azure 訂閱。
2. 創建 Azure OpenAI 資源並取得 API 金鑰。

#### Python 範例程式碼

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # 為 Azure OpenAI 產生提示
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
        
        # 調用 Azure OpenAI API 以取得重新排序及評分的目的地
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # 擷取並回傳推薦結果
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

#### 程式碼說明 - 偏好預訂

1. <strong>初始化</strong>：`TravelAgent` 類別初始化時帶有潛在旅遊目的地列表，每個目的地有名稱和描述等屬性。

2. **取得推薦結果（`get_recommendations` 方法）**：此方法根據用戶偏好生成 Azure OpenAI 服務的提示，並發出 HTTP POST 請求調用 Azure OpenAI API，取得重新排序和評分後的目的地。

3. **生成提示（`generate_prompt` 方法）**：建立給 Azure OpenAI 的提示，包含用戶偏好和目的地列表。該提示指導模型依偏好重新排序及評分目的地。

4. **API 呼叫**：使用 `requests` 庫向 Azure OpenAI API 端點發出 HTTP POST 請求。回應包含重新排序和評分後的目的地。

5. <strong>範例用法</strong>：旅行代理收集用戶偏好（例如喜愛觀光與多元文化），並使用 Azure OpenAI 服務取得重新排序和評分的旅行目的地推薦。

請確保將 `your_azure_openai_api_key` 替換為您的實際 Azure OpenAI API 金鑰，並將 `https://your-endpoint.com/...` 替換為 Azure OpenAI 部署的實際端點 URL。

透過利用 LLM 進行重新排序和評分，旅行代理可提供更個人化且相關的旅行推薦，提升客戶整體體驗。

### RAG：提示技巧 vs 工具

檢索增強生成（RAG）既可視為提示技巧，也可作為開發 AI 代理的工具。理解兩者差異，有助於更有效地利用 RAG。

#### 作為提示技巧的 RAG

**它是什麼？**

- 作為提示技巧，RAG 涉及設計特定查詢或提示，以引導從大型語料庫或資料庫檢索相關資訊，再用該資訊生成回答或動作。

**如何運作：**

1. <strong>設計提示</strong>：根據任務或用戶輸入製作結構良好的提示或查詢。
2. <strong>檢索資訊</strong>：用提示從預先存在的知識庫或資料集搜尋相關資料。
3. <strong>生成回答</strong>：結合檢索到的資訊與生成式 AI 模型，產出完整且連貫的回答。

<strong>旅行代理中的例子</strong>：

- 用戶輸入：「我想參觀巴黎的博物館。」
- 提示：「找出巴黎的頂級博物館。」
- 檢索資訊：有關羅浮宮博物館、奧賽美術館等細節。
- 生成回答：「這裡有一些巴黎的頂級博物館：羅浮宮博物館、奧賽美術館和龐畢度中心。」

#### 作為工具的 RAG

**它是什麼？**

- 作為工具，RAG 是一個整合系統，自動化處理檢索和生成流程，讓開發者無需為每個查詢手動製作提示即可實現複雜 AI 功能。

**如何運作：**

1. <strong>整合</strong>：將 RAG 嵌入 AI 代理架構，自動處理檢索和生成任務。
2. <strong>自動化</strong>：工具管理整個流程，從接收用戶輸入到產生最終回應，無需針對每步設計明確提示。
3. <strong>效率</strong>：透過簡化檢索及生成過程，提高代理效能，使回應更快且更精確。

<strong>旅行代理中的例子</strong>：

- 用戶輸入：「我想參觀巴黎的博物館。」
- RAG 工具：自動檢索有關博物館的資訊，並生成回應。
- 生成回答：「這裡有一些巴黎的頂級博物館：羅浮宮博物館、奧賽美術館和龐畢度中心。」

### 比較

| 方面                  | 提示技巧                                                   | 工具                                                  |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **手動 vs 自動**        | 為每個查詢手動設計提示。                                   | 自動化處理檢索和生成。                                   |
| <strong>控制</strong>                | 對檢索過程控制度較高。                                     | 簡化並自動化檢索及生成。                                |
| <strong>彈性</strong>                | 可根據特定需求客製提示。                                  | 適合大規模應用，效率較高。                               |
| <strong>複雜度</strong>              | 需設計並微調提示。                                         | 容易整合到 AI 代理架構中。                               |

### 實務範例

**提示技巧範例：**

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

評估相關性是 AI 代理表現的關鍵面向，確保代理檢索和生成的資訊適合、精確且對用戶有用。讓我們探討如何評估 AI 代理的相關性，包括實務範例和技術。

#### 評估相關性的關鍵概念

1. <strong>上下文感知</strong>：
   - 代理必須理解用戶查詢的上下文，才能檢索和生成相關資訊。
   - 範例：用戶查詢「巴黎最佳餐廳」，代理應考慮用戶偏好，如菜系和預算。

2. <strong>準確性</strong>：
   - 代理提供的資訊應具事實正確性且為最新。
   - 範例：推薦現在營業且評價良好的餐廳，而非過時或已關閉選項。

3. <strong>用戶意圖</strong>：
   - 代理應推測用戶查詢的真正意圖，提供最相關資訊。
   - 範例：用戶查「經濟型旅館」，代理應優先推薦價格合理選項。

4. <strong>反饋回路</strong>：
   - 持續收集和分析用戶反饋，有助於代理改進相關性評估流程。
   - 範例：結合用戶對過往推薦的評價和意見，提升未來回應品質。

#### 評估相關性的實務技術

1. <strong>相關性得分</strong>：
   - 根據檢索項是否符合用戶查詢和偏好，為其分配相關性得分。
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
   - 過濾掉不相關項目，根據得分排序剩餘項目。
   - 範例：

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # 返回最相關的前10個項目
     ```

3. **自然語言處理（NLP）**：
   - 利用 NLP 技術理解用戶查詢並檢索相關資訊。
   - 範例：

     ```python
     def process_query(query):
         # 使用自然語言處理從用戶查詢中提取關鍵資訊
         processed_query = nlp(query)
         return processed_query
     ```

4. <strong>用戶反饋整合</strong>：
   - 收集用戶對推薦的回饋，並利用這些訊息調整未來的相關性評估。
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

#### 範例：旅行代理評估推薦相關性

這裡有一個實務範例展示旅行代理如何評估旅行推薦的相關性：

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
        return ranked_items[:10]  # 返回前10個相關項目

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

### 有意圖的搜尋

有意圖的搜尋包含理解與詮釋用戶查詢背後的目的或目標，以檢索和生成最相關且有用的資訊。此方法超越純粹匹配關鍵字，著重掌握用戶的真實需求與上下文。

#### 有意圖搜尋的關鍵概念

1. <strong>理解用戶意圖</strong>：
   - 用戶意圖大致可分為三類：資訊型、導向型與交易型。
     - <strong>資訊型意圖</strong>：用戶尋求主題相關資訊（如：「巴黎有哪些最佳博物館？」）。
     - <strong>導向型意圖</strong>：用戶想導航至特定網站或頁面（如：「羅浮宮博物館官方網站」）。
     - <strong>交易型意圖</strong>：用戶欲執行交易，如訂機票或購買（如：「訂一張飛巴黎的機票」）。

2. <strong>上下文感知</strong>：
   - 分析用戶查詢的上下文有助準確識別其意圖，包含先前互動、用戶偏好及當前查詢細節。

3. **自然語言處理（NLP）**：
   - 運用 NLP 技術理解並詮釋用戶提出的自然語言查詢，涵蓋實體識別、情感分析及查詢解析等任務。

4. <strong>個人化</strong>：
   - 基於用戶歷史、偏好和反饋個人化搜尋結果，提升檢索資訊的相關性。

#### 實務範例：旅行代理中的有意圖搜尋

以旅行代理為例，展示如何實現有意圖搜尋。

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

3. <strong>上下文感知</strong>


   ```python
   def analyze_context(query, user_history):
       # 將當前查詢與用戶歷史結合以理解上下文
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. <strong>搜尋及個人化結果</strong>

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
       # 用於資訊性意圖的搜尋示例邏輯
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # 用於導航性意圖的搜尋示例邏輯
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # 用於交易性意圖的搜尋示例邏輯
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # 個人化示例邏輯
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # 回傳前10個個人化結果
   ```

5. <strong>使用範例</strong>

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

## 4. 將生成代碼作為工具

生成代碼的代理人使用 AI 模型來編寫和執行代碼，解決複雜問題並自動化任務。

### 生成代碼代理人

生成代碼的代理人使用生成式 AI 模型來編寫和執行代碼。這些代理人能夠通過用多種程式語言生成並執行代碼，來解決複雜問題、自動化任務並提供有價值的見解。

#### 實際應用

1. <strong>自動代碼生成</strong>：為特定任務生成代碼片段，例如數據分析、網頁爬蟲或機器學習。
2. **RAG 中的 SQL**：使用 SQL 查詢從資料庫檢索和操作數據。
3. <strong>問題解決</strong>：創建並執行代碼解決特定問題，例如優化算法或分析數據。

#### 範例：用於數據分析的代碼生成代理人

想像你正在設計一個代碼生成代理人。以下是它的可能運作方式：

1. <strong>任務</strong>：分析數據集以識別趨勢和模式。
2. <strong>步驟</strong>：
   - 將數據集載入數據分析工具。
   - 生成 SQL 查詢以過濾和匯總數據。
   - 執行查詢並檢索結果。
   - 使用結果生成視覺化和洞見。
3. <strong>必需資源</strong>：可訪問數據集、數據分析工具和 SQL 功能。
4. <strong>經驗</strong>：利用過去分析結果提升未來分析的準確性與相關性。

### 範例：用於旅行代理人的代碼生成代理人

在此範例中，我們將設計一個代碼生成代理人，Travel Agent，協助用戶規劃旅行，透過生成和執行代碼來完成任務。此代理人可以處理擷取旅遊選項、篩選結果和編制行程等工作，運用生成式 AI 技術。

#### 代碼生成代理人概述

1. <strong>收集用戶偏好</strong>：收集用戶輸入，例如目的地、旅行日期、預算和興趣。
2. <strong>產生獲取數據的代碼</strong>：生成代碼片段以檢索關於航班、酒店和景點的數據。
3. <strong>執行生成的代碼</strong>：執行生成的代碼以獲取實時資訊。
4. <strong>生成行程</strong>：將獲取的數據編制成個人化旅行計劃。
5. <strong>根據反饋進行調整</strong>：接收用戶反饋，必要時重新生成代碼以優化結果。

#### 實作步驟詳解

1. <strong>收集用戶偏好</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. <strong>產生獲取數據的代碼</strong>

   ```python
   def generate_code_to_fetch_data(preferences):
       # 例子：生成代碼以根據用戶喜好搜尋航班
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # 例子：生成代碼以搜尋酒店
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. <strong>執行生成的代碼</strong>

   ```python
   def execute_code(code):
       # 使用 exec 執行已生成的代碼
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

5. <strong>根據反饋進行調整</strong>

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
   
   # 重新生成並執行帶有更新偏好的代碼
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### 利用環境感知與推理

根據資料表結構確實可以透過運用環境感知與推理來提升查詢生成過程。

以下是如何實作的範例：

1. <strong>理解架構</strong>：系統會理解資料表的架構，並利用此資訊作為查詢生成的基礎。
2. <strong>根據反饋調整</strong>：系統會根據反饋調整用戶偏好，並推理哪些架構欄位需要更新。
3. <strong>生成並執行查詢</strong>：系統會生成並執行查詢，以根據新偏好抓取更新的航班和酒店資料。

以下是融入這些概念的更新版 Python 程式碼範例：

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # 根據用戶反饋調整偏好設定
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # 根據結構推理調整其他相關偏好設定
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # 根據結構和反饋自訂邏輯調整偏好設定
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # 生成代碼以根據更新的偏好設定獲取航班數據
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # 生成代碼以根據更新的偏好設定獲取酒店數據
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # 模擬執行代碼並返回模擬數據
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # 根據航班、酒店和景點生成行程安排
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# 範例結構
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# 使用範例
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# 使用更新的偏好設定重新生成並執行代碼
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### 解說 — 基於反饋的預訂調整

1. <strong>架構意識</strong>：`schema` 字典定義了如何基於反饋調整偏好，包括 `favorites` 和 `avoid` 欄位及其對應調整。
2. **調整偏好（`adjust_based_on_feedback` 方法）**：此方法根據用戶反饋及架構調整偏好設定。
3. **基於環境的調整（`adjust_based_on_environment` 方法）**：此方法根據架構和反饋自訂調整策略。
4. <strong>生成並執行查詢</strong>：系統根據調整後的偏好生成代碼抓取更新的航班和酒店資料，並模擬執行這些查詢。
5. <strong>生成行程</strong>：系統根據更新的航班、酒店及景點資料產生最新行程。

透過使系統具備環境感知並基於架構推理，可生成更準確且相關的查詢，進而提供更佳的旅行建議和更個人化的用戶體驗。

### 將 SQL 作為檢索強化生成（RAG）技術使用

SQL（結構化查詢語言）是與資料庫互動的強大工具。在檢索強化生成（RAG）方法中，SQL 可從資料庫中檢索相關數據，用於AI代理的響應生成或行動決策。讓我們探討 SQL 如何用作 Travel Agent 的 RAG 技術。

#### 關鍵概念

1. <strong>資料庫互動</strong>：
   - 使用 SQL 查詢資料庫、取得相關資訊和操作數據。
   - 範例：從旅遊資料庫擷取航班詳情、酒店資訊及景點資料。

2. **與 RAG 結合**：
   - 根據用戶輸入和偏好生成 SQL 查詢。
   - 使用檢索到的數據生成個人化建議或行動。

3. <strong>動態查詢生成</strong>：
   - AI 代理根據情境和需求動態生成 SQL 查詢。
   - 範例：根據預算、日期和興趣自訂 SQL 查詢篩選結果。

#### 應用案例

- <strong>自動代碼生成</strong>：為特定任務生成代碼片段。
- **RAG 中的 SQL**：使用 SQL 查詢操作數據。
- <strong>問題解決</strong>：創建並執行代碼解決問題。

<strong>例子</strong>：
一個數據分析代理人：

1. <strong>任務</strong>：分析數據集尋找趨勢。
2. <strong>步驟</strong>：
   - 載入數據集。
   - 生成 SQL 查詢篩選數據。
   - 執行查詢並取得結果。
   - 生成視覺化及洞見。
3. <strong>資源</strong>：可訪問數據集和 SQL 功能。
4. <strong>經驗</strong>：使用過往結果改善未來分析。

#### 實務範例：Travel Agent 中使用 SQL

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

利用 SQL 作為檢索強化生成（RAG）技術的一部分，像 Travel Agent 這樣的 AI 代理能動態檢索並使用相關資料，提供準確且個人化的建議。

### 元認知範例

為了展示元認知的實作，我們來建立一個簡單代理，它在解決問題的同時會<em>反思其決策過程</em>。本例中，我們將構建一個系統，代理嘗試優化酒店選擇，但若其推理失誤或選擇次優，則會評估自身推理並調整策略。

我們將透過一個基本範例模擬此狀況，代理根據價格與品質的綜合評估選擇酒店，但會「反思」其決策並做出相應調整。

#### 此範例如何說明元認知：

1. <strong>初步決策</strong>：代理選擇價格最低的酒店，未考慮品質影響。
2. <strong>反思與評估</strong>：初選後，代理透過用戶反饋檢查酒店是否為不良選擇。如發現品質過低，則反思其推理。
3. <strong>調整策略</strong>：代理基於反思調整策略，從「最低價」切換至「最高品質」，提升未來決策的品質。

範例如下：

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # 儲存之前選擇的酒店
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
        # 假設我們有一些用戶反饋，告訴我們最後的選擇是否好
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # 如果之前的選擇不理想，調整策略
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

# 模擬一個酒店列表（價格和質素）
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# 建立一個代理人
agent = HotelRecommendationAgent()

# 第一步：代理人使用「最平」策略推薦酒店
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# 第二步：代理人反思選擇並在必要時調整策略
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# 第三步：代理人再次推薦，這次使用調整後的策略
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### 代理的元認知能力

關鍵在於代理能夠：
- 評估先前的選擇及決策過程。
- 根據反思調整策略，展現元認知的實作。

這是元認知的一種簡易形式，系統能基於內部反饋調整推理程序。

### 結論

元認知是能顯著提升 AI 代理能力的強大工具。透過融合元認知過程，您可以設計出更智能、適應力強且有效率的代理。可使用附加資源進一步探索 AI 代理中元認知的精彩世界。

### 對元認知設計模式有更多疑問？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加辦公時間並獲得 AI 代理相關問題的解答。

## 前一課程

[多代理設計模式](../08-multi-agent/README.md)

## 下一課程

[生產環境中的 AI 代理](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->