[![多智能体设计](../../../translated_images/zh-CN/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(点击上方图片查看本课视频)_
# AI 代理中的元认知

## 介绍

欢迎来到关于 AI 代理中元认知的课程！本章节针对对 AI 代理如何思考自身思维过程好奇的初学者设计。完成本课后，您将理解关键概念，并配备实际示例，用于在 AI 代理设计中应用元认知。

## 学习目标

完成本课后，您将能够：

1. 理解代理定义中推理循环的含义。
2. 使用规划和评估技术帮助自我纠错的代理。
3. 创建能够操作代码以完成任务的代理。

## 元认知介绍

元认知指的是涉及思考自身思维的高级认知过程。对于 AI 代理来说，这意味着能够基于自我意识和过去经验评估并调整其行为。元认知，即“关于思考的思考”，是代理 AI 系统开发中的重要概念。它涉及 AI 系统意识到自身内部过程，能够监控、调节并相应地适应其行为。就像我们在观察环境或分析问题时所做的那样。这种自我意识有助于 AI 系统做出更好决策，识别错误，并随着时间提升性能 —— 再次关联到图灵测试以及 AI 是否会接管的争论。

在代理 AI 系统的背景下，元认知可以帮助解决多个挑战，例如：
- 透明性：确保 AI 系统能解释其推理和决策过程。
- 推理能力：增强 AI 系统综合信息和做出合理决策的能力。
- 适应性：使 AI 系统能够适应新环境和变化的条件。
- 感知：提高 AI 系统识别和解读环境数据的准确性。

### 什么是元认知？

元认知，即“关于思考的思考”，是一种更高级的认知过程，涉及对自身认知过程的自我意识和自我调节。在 AI 领域，元认知使代理能够评估并调整其策略和行为，从而提升问题解决和决策能力。通过理解元认知，您可以设计不仅更智能而且更适应和高效的 AI 代理。真正的元认知，您会看到 AI 明确地推理其自身推理过程。

示例： “我优先考虑价格更便宜的航班，因为……我可能错过了直飞，所以让我再检查一下。”。
跟踪它为何选择某条路径。
- 注意到它犯了错误，因为过度依赖上次用户偏好，因此它不仅调整最终建议，还修改决策策略。
- 诊断模式，例如“每次看到用户提‘太拥挤’时，我不仅应该去除某些景点，还要反思如果我总按受欢迎程度排序‘顶级景点’，那我的挑选方法就是有缺陷的。”

### 元认知在 AI 代理中的重要性

元认知在 AI 代理设计中起着关键作用，主要原因有：

![元认知重要性](../../../translated_images/zh-CN/importance-of-metacognition.b381afe9aae352f7.webp)

- 自我反思：代理可以评估自身表现并识别改进空间。
- 适应能力：代理可以根据过去经验和变化环境调整策略。
- 错误修正：代理可自主检测并修正错误，提升结果准确性。
- 资源管理：代理通过规划和评估优化时间和计算能力等资源的使用。

## AI 代理的组成部分

在深入元认知过程之前，了解 AI 代理的基本组成部分至关重要。AI 代理通常包括：

- 角色设定：代理的个性及特点，定义其与用户互动的方式。
- 工具：代理可执行的功能和能力。
- 技能：代理拥有的知识和专长。

这些组成部分协同工作，构成可以执行特定任务的“专业单元”。

<strong>示例</strong>：
设想一个旅游代理服务，不仅规划您的假期，还能基于实时数据及过往客户旅程经验调整路径。

### 示例：旅游代理服务中的元认知

想象您正在设计一个由 AI 驱动的旅游代理服务。该代理“旅游代理”帮助用户规划假期。为了融入元认知，旅游代理需要基于自我意识和过往经验评估并调整行为。元认知可能发挥作用的方式如下：

#### 当前任务

当前任务是帮助用户规划一次巴黎之旅。

#### 完成任务的步骤

1. <strong>收集用户偏好</strong>：询问用户的旅行日期、预算、兴趣（如博物馆、美食、购物）及具体需求。
2. <strong>检索信息</strong>：搜索符合用户偏好的航班、住宿、景点和餐馆。
3. <strong>生成推荐</strong>：提供个性化行程，包括航班详情、酒店预订和建议活动。
4. <strong>基于反馈调整</strong>：向用户征求推荐反馈，并据此作出调整。

#### 所需资源

- 访问航班和酒店预订数据库。
- 巴黎景点和餐馆信息。
- 来自先前互动的用户反馈数据。

#### 经验与自我反思

旅游代理利用元认知评估表现并从过往经验中学习。例如：

1. <strong>分析用户反馈</strong>：旅游代理审视用户反馈，确定哪些推荐受欢迎，哪些不被认可，进而调整未来建议。
2. <strong>适应性</strong>：若用户曾表示不喜欢拥挤场所，旅游代理未来将避免在高峰时段推荐热门景点。
3. <strong>错误修正</strong>：若旅游代理曾建议预订已满的酒店，则学会在推荐前更加严格确认可用性。

#### 实际开发者示例

以下是结合元认知的旅游代理简化代码示例：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # 根据偏好搜索航班、酒店和景点
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
        # 分析反馈并调整未来推荐
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# 示例用法
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

#### 元认知的重要性

- <strong>自我反思</strong>：代理可以分析表现并识别改进空间。
- <strong>适应性</strong>：代理能根据反馈及环境变化调整策略。
- <strong>错误修正</strong>：代理能自主检测并纠正错误。
- <strong>资源管理</strong>：代理能优化时间和计算资源的使用。

通过引入元认知，旅游代理能提供更个性化且精准的旅行推荐，提升整体用户体验。

---

## 2. 代理中的规划

规划是 AI 代理行为的关键组成部分。它涉及制定实现目标所需的步骤，考虑当前状态、资源和可能的障碍。

### 规划要素

- <strong>当前任务</strong>：明确任务定义。
- <strong>完成任务的步骤</strong>：将任务拆分为可管理的步骤。
- <strong>所需资源</strong>：确定必要资源。
- <strong>经验</strong>：利用过去经验指导规划。

<strong>示例</strong>：
以下是旅游代理为有效协助用户制定旅行计划需要采取的步骤：

### 旅游代理的步骤

1. <strong>收集用户偏好</strong>
   - 询问用户旅行日期、预算、兴趣及具体需求。
   - 示例：“您计划何时出行？”“您的预算范围是多少？”“您假期喜欢什么活动？”

2. <strong>检索信息</strong>
   - 根据用户偏好搜索相关旅游选项。
   - <strong>航班</strong>：寻找预算内且符合偏好的可用航班。
   - <strong>住宿</strong>：找到符合用户地点、价格及设施偏好的酒店或租赁房。
   - <strong>景点和餐馆</strong>：识别符合用户兴趣的热门景点、活动和餐饮选项。

3. <strong>生成推荐</strong>
   - 将检索到的信息整合成个性化行程。
   - 提供航班选项、酒店预订及建议活动，并确保推荐符合用户偏好。

4. <strong>向用户展示行程</strong>
   - 将拟议行程分享给用户审阅。
   - 示例：“这是为您规划的巴黎旅行建议行程，包括航班详情、酒店预订及推荐活动和餐馆，您怎么看？”

5. <strong>收集反馈</strong>
   - 征询用户对行程的反馈。
   - 示例：“您喜欢这些航班吗？”“酒店合适吗？”“有哪些活动想添加或删除？”

6. <strong>根据反馈调整</strong>
   - 基于用户反馈修改行程。
   - 对航班、住宿及活动建议进行适当调整，以更符合用户偏好。

7. <strong>最终确认</strong>
   - 向用户展示更新后的行程以供最终确认。
   - 示例：“根据您的反馈我已做出调整，这是更新后的行程，您觉得如何？”

8. <strong>预订并确认</strong>
   - 用户确认后，进行航班、住宿及预定活动的预订。
   - 向用户发送确认信息。

9. <strong>持续支持</strong>
   - 在旅程前后保持支持，协助用户的变更和额外需求。
   - 示例：“如果旅行期间需要任何帮助，请随时联系我！”

### 示例互动

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

# 在预订请求中的示例用法
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

## 3. 纠正性 RAG 系统

首先，让我们理解 RAG 工具和预先上下文加载的区别

![RAG 与上下文加载比较](../../../translated_images/zh-CN/rag-vs-context.9eae588520c00921.webp)

### 检索增强生成（RAG）

RAG 结合了检索系统和生成模型。当提出查询时，检索系统从外部来源获取相关文档或数据，利用这些检索信息增强生成模型的输入，这帮助模型生成更准确且符合上下文的回复。

在 RAG 系统中，代理从知识库检索相关信息，并利用其生成适当的回应或行动。

### 纠正性 RAG 方法

纠正性 RAG 方法专注于使用 RAG 技术校正错误，提升 AI 代理的准确度。其包含：

1. <strong>提示技术</strong>：使用特定提示引导代理检索相关信息。
2. <strong>工具</strong>：实现算法和机制，使代理评估检索信息的相关性并生成准确回复。
3. <strong>评估</strong>：持续评估代理表现，并作出调整以提升准确率与效率。

#### 示例：搜索代理中的纠正性 RAG

设想一个从网络检索信息以回答用户查询的搜索代理。纠正性 RAG 方法可能包括：

1. <strong>提示技术</strong>：基于用户输入制定搜索查询。
2. <strong>工具</strong>：利用自然语言处理和机器学习算法对搜索结果进行排序和过滤。
3. <strong>评估</strong>：分析用户反馈，识别并纠正检索信息中的不准确之处。

### 旅游代理中的纠正性 RAG

纠正性 RAG （检索增强生成）增强 AI 检索和生成信息的能力，同时纠正任何不准确之处。让我们看看旅游代理如何利用纠正性 RAG 方法提供更准确且相关的旅行推荐。

包括以下内容：

- **提示技术：** 使用特定提示引导代理检索相关信息。
- **工具：** 实现算法和机制，使代理评估检索信息相关性并生成准确响应。
- **评估：** 持续评估代理表现并作出调整以提升准确率与效率。

#### 在旅游代理中实施纠正性 RAG 的步骤

1. <strong>初始用户互动</strong>
   - 旅游代理收集用户初始偏好，如目的地、旅行日期、预算和兴趣。
   - 示例：

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. <strong>信息检索</strong>
   - 旅游代理根据用户偏好检索航班、住宿、景点和餐馆信息。
   - 示例：

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. <strong>生成初始推荐</strong>
   - 旅游代理利用检索信息生成个性化行程。
   - 示例：

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. <strong>收集用户反馈</strong>
   - 旅游代理向用户征求对初始推荐的反馈。
   - 示例：

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **纠正性 RAG 过程**
   - <strong>提示技术</strong>：旅游代理根据用户反馈制定新的搜索查询。
     - 示例：

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - <strong>工具</strong>：旅游代理使用算法对新搜索结果进行排序和过滤，重点突出根据用户反馈的相关性。
     - 示例：

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - <strong>评估</strong>：旅游代理不断评估推荐的相关性和准确性，通过分析用户反馈做出必要调整。
     - 示例：

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### 实际示例

以下是一个简单的 Python 代码示例，整合了旅游代理中的纠正性 RAG 方法：

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

# 示例用法
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

### 预先上下文加载


预先加载上下文是指在处理查询之前，将相关的上下文或背景信息加载到模型中。这意味着模型从一开始就可以访问这些信息，从而帮助它生成更有见地的回答，而无需在处理过程中检索额外数据。

下面是一个简化的示例，展示了在 Python 中旅行代理应用如何进行预先加载上下文：

```python
class TravelAgent:
    def __init__(self):
        # 预加载热门目的地及其信息
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # 从预加载的上下文中获取目的地信息
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# 使用示例
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### 说明

1. **初始化（`__init__` 方法）**：`TravelAgent` 类预加载了一个包含热门目的地信息的字典，如巴黎、东京、纽约和悉尼。该字典包括每个目的地的国家、货币、语言和主要景点等详细信息。

2. **检索信息（`get_destination_info` 方法）**：当用户查询某个特定目的地时，`get_destination_info` 方法会从预加载的上下文字典中获取相关信息。

通过预先加载上下文，旅行代理应用可以快速响应用户查询，而无需实时从外部来源检索信息。这使应用更加高效和响应迅速。

### 在迭代前以目标启动计划

以目标启动计划意味着一开始就有一个明确的目标或预期结果。通过事先定义这个目标，模型可以在整个迭代过程中将其作为指导原则。这有助于确保每次迭代都朝着实现预期结果的方向推进，从而使过程更高效、更有针对性。

下面是一个例子，展示了如何在 Python 中为旅行代理在迭代前以目标启动旅行计划：

### 场景

旅行代理希望为客户规划一个定制的假期。目标是基于客户的偏好和预算创建一个能够最大化客户满意度的旅行行程。

### 步骤

1. 定义客户的偏好和预算。
2. 根据这些偏好启动初步计划。
3. 通过迭代优化计划，以提高客户满意度。

#### Python 代码

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

# 示例用法
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

#### 代码说明

1. **初始化（`__init__` 方法）**：`TravelAgent` 类初始化时传入潜在目的地列表，每个目的地有名称、费用和活动类型等属性。

2. **启动计划（`bootstrap_plan` 方法）**：该方法根据客户偏好和预算创建初步旅行计划。遍历目的地列表，如果目的地符合客户偏好且预算允许，则加入计划。

3. **匹配偏好（`match_preferences` 方法）**：检查某目的地是否符合客户偏好。

4. **迭代计划（`iterate_plan` 方法）**：该方法通过尝试用更符合客户偏好和预算约束的替代目的地替换计划中的每个目的地，来优化初步计划。

5. **计算费用（`calculate_cost` 方法）**：计算当前计划的总费用，包括可能的新目的地。

#### 示例用法

- <strong>初步计划</strong>：旅行代理根据客户对观光的偏好和 2000 美元的预算创建初步计划。
- <strong>优化计划</strong>：旅行代理迭代优化该计划，以更好地满足客户偏好和预算。

通过以明确目标（例如最大化客户满意度）启动计划并通过迭代优化，旅行代理可以为客户创建定制且优化的旅行行程。这种方法确保旅行计划从一开始就符合客户的偏好和预算，并能随着每次迭代不断改进。

### 利用大型语言模型进行重排和评分

大型语言模型（LLM）可以用于重排和评分，通过评估检索到的文档或生成回答的相关性和质量。其工作原理如下：

**检索：** 初步检索步骤根据查询获取候选文档或回答集合。

**重排：** LLM 评估这些候选项，并根据相关性和质量进行重排。此步骤确保最相关且高质量的信息优先呈现。

**评分：** LLM 给每个候选项赋分，反映其相关性和质量。这有助于选择最佳回答或文档。

通过利用 LLM 进行重排和评分，系统可以提供更准确、更符合上下文的信息，提高整体用户体验。

以下示例展示了旅行代理如何在 Python 中利用大型语言模型（LLM）基于用户偏好对旅行目的地进行重排和评分：

#### 场景 - 基于偏好的旅行

旅行代理希望根据客户偏好推荐最佳旅行目的地。LLM 帮助对目的地进行重排和评分，确保呈现最相关选项。

#### 步骤：

1. 收集用户偏好。
2. 检索潜在旅行目的地列表。
3. 使用 LLM 根据用户偏好对目的地进行重排和评分。

下面展示如何将之前的示例更新为使用 Azure OpenAI 服务：

#### 要求

1. 需要拥有 Azure 订阅。
2. 创建 Azure OpenAI 资源并获取 API 密钥。

#### 示例 Python 代码

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # 为 Azure OpenAI 生成提示
        prompt = self.generate_prompt(preferences)
        
        # 定义请求的头信息和负载
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # 调用 Azure OpenAI API 获取重新排序和评分的目的地
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # 提取并返回推荐结果
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

# 示例用法
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

#### 代码说明 - 偏好订购者

1. <strong>初始化</strong>：`TravelAgent` 类初始化时传入潜在旅行目的地列表，每个目的地有名称和描述等属性。

2. **获取推荐 (`get_recommendations` 方法)**：该方法基于用户偏好生成 Azure OpenAI 服务的提示词，并向 Azure OpenAI API 发起 HTTP POST 请求，获取重排和评分后的目的地列表。

3. **生成提示词 (`generate_prompt` 方法)**：该方法构造 Azure OpenAI 所需的提示词，包含用户偏好和目的地列表，引导模型根据给定偏好对目的地进行重排和评分。

4. **API 调用**：利用 `requests` 库向 Azure OpenAI API 端点发起 HTTP POST 请求，响应包含重排和评分后的目的地数据。

5. <strong>示例用法</strong>：旅行代理收集用户偏好（例如对观光和多元文化的兴趣），使用 Azure OpenAI 服务获取重排和评分后的旅行推荐。

请确保将 `your_azure_openai_api_key` 替换为您的真实 Azure OpenAI API 密钥，`https://your-endpoint.com/...` 替换为您 Azure OpenAI 部署的实际端点 URL。

通过利用 LLM 进行重排和评分，旅行代理能够为客户提供更个性化和相关的旅行推荐，提升整体体验。

### RAG：提示技术 与 工具

检索增强生成（RAG）既可以是一种提示技术，也可以是开发 AI 代理的一个工具。理解两者之间的区别，有助于更有效地在项目中利用 RAG。

#### 作为提示技术的 RAG

**它是什么？**

- 作为提示技术，RAG 涉及设计特定查询或提示，引导从大规模语料库或数据库检索相关信息。然后利用这些信息生成回答或执行操作。

**工作原理：**

1. <strong>设计提示</strong>：根据任务或用户输入创建结构化提示或查询。
2. <strong>检索信息</strong>：利用提示，从已有知识库或数据集中检索相关数据。
3. <strong>生成回答</strong>：结合检索到的信息和生成式 AI 模型，产出全面且连贯的回答。

<strong>旅行代理示例</strong>：

- 用户输入：“我想参观巴黎的博物馆。”
- 提示：“查找巴黎的顶级博物馆。”
- 检索信息：关于卢浮宫博物馆、奥赛博物馆等的详细信息。
- 生成回答：“以下是巴黎的一些顶级博物馆：卢浮宫博物馆、奥赛博物馆和蓬皮杜艺术中心。”

#### 作为工具的 RAG

**它是什么？**

- 作为工具，RAG 是一个集成系统，自动化检索和生成流程，使开发者无需为每个查询手工编写提示，即可轻松实现复杂 AI 功能。

**工作原理：**

1. <strong>集成</strong>：将 RAG 嵌入 AI 代理架构，自动处理检索和生成任务。
2. <strong>自动化</strong>：工具管理整个流程，从接收用户输入到生成最终回答，无需每步显式提示。
3. <strong>效率提升</strong>：通过简化检索和生成过程，提升代理性能，实现更快更精准的响应。

<strong>旅行代理示例</strong>：

- 用户输入：“我想参观巴黎的博物馆。”
- RAG 工具：自动检索关于博物馆的信息并生成回答。
- 生成回答：“以下是巴黎的一些顶级博物馆：卢浮宫博物馆、奥赛博物馆和蓬皮杜艺术中心。”

### 对比

| 方面                   | 提示技术                                         | 工具                                                |
|------------------------|-------------------------------------------------|-----------------------------------------------------|
| **手动 vs 自动**       | 每个查询手动设计提示                             | 检索和生成全过程自动化                               |
| <strong>控制力</strong>             | 对检索流程有更大控制                             | 简化并自动化检索和生成                               |
| <strong>灵活性</strong>             | 可基于特定需求定制提示                           | 更适合大规模部署                                     |
| <strong>复杂度</strong>             | 需设计和调整提示                                 | 易于集成到 AI 代理架构中                             |

### 实践示例

**提示技术示例：**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**工具示例：**

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

### 评估相关性

评估相关性是 AI 代理性能的重要方面。它确保代理检索和生成的信息对用户是恰当、准确且有用的。下面探讨评估相关性的方式，包括实际例子和技术。

#### 评估相关性的关键概念

1. <strong>上下文意识</strong>：
   - 代理必须理解用户查询的上下文，才能检索并生成相关信息。
   - 例如：用户询问“巴黎最好的餐厅”，代理应考虑用户对菜系类型和预算的偏好。

2. <strong>准确性</strong>：
   - 代理提供的信息应为事实正确且最新的。
   - 例如：推荐当前营业且评价良好的餐厅，而非过时或已关闭的选项。

3. <strong>用户意图</strong>：
   - 代理应推断用户查询背后的意图，提供最相关信息。
   - 例如：用户查询“经济型酒店”，代理应优先推荐价格实惠的选项。

4. <strong>反馈循环</strong>：
   - 持续收集和分析用户反馈，帮助代理优化相关性评估过程。
   - 例如：根据用户对之前推荐的评分和反馈，改进后续回答。

#### 评估相关性的实用技术

1. <strong>相关性评分</strong>：
   - 根据检索项与用户查询及偏好的匹配程度，为每项赋予相关性评分。
   - 例如：

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

2. <strong>过滤与排序</strong>：
   - 过滤掉无关项，并根据相关性评分对剩余项排序。
   - 例如：

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # 返回前10个相关项目
     ```

3. **自然语言处理（NLP）**：
   - 利用 NLP 技术理解用户查询，检索相关信息。
   - 例如：

     ```python
     def process_query(query):
         # 使用自然语言处理从用户的查询中提取关键信息
         processed_query = nlp(query)
         return processed_query
     ```

4. <strong>用户反馈整合</strong>：
   - 收集对提供推荐的用户反馈，并用于调整未来的相关性评估。
   - 例如：

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### 示例：旅行代理中的相关性评估

下面是旅行代理如何评估旅行推荐相关性的实际示例：

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
        return ranked_items[:10]  # 返回前10个相关项目

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

# 示例用法
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

### 带有意图的搜索

带有意图的搜索涉及理解和解析用户查询背后的真实目的或目标，以检索和生成最相关且有用的信息。这种方法超越了简单的关键词匹配，更关注把握用户的实际需求和上下文。

#### 带有意图搜索的关键概念

1. <strong>理解用户意图</strong>：
   - 用户意图可分为三类：信息性、导航性和交易性。
     - <strong>信息性意图</strong>：用户寻求某个主题的信息（如“巴黎有哪些最好博物馆？”）。
     - <strong>导航性意图</strong>：用户想访问特定网站或页面（如“卢浮宫博物馆官网”）。
     - <strong>交易性意图</strong>：用户希望完成交易，如预订机票或购买商品（如“预订飞往巴黎的机票”）。

2. <strong>上下文意识</strong>：
   - 分析用户查询的上下文，有助于准确识别用户意图。这包括考虑之前交互、用户偏好和当前查询的具体细节。

3. **自然语言处理（NLP）**：
   - 利用 NLP 技术理解和解析用户的自然语言查询，包括实体识别、情感分析和查询解析等任务。

4. <strong>个性化</strong>：
   - 基于用户历史、偏好和反馈对搜索结果进行个性化，提高检索信息的相关性。

#### 实用示例：旅行代理中的带有意图搜索

以旅行代理为例，看看如何实现带有意图的搜索。

1. <strong>收集用户偏好</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. <strong>理解用户意图</strong>

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. <strong>上下文意识</strong>


   ```python
   def analyze_context(query, user_history):
       # 将当前查询与用户历史结合以理解上下文
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. <strong>搜索和个性化结果</strong>

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
       # 信息意图的示例搜索逻辑
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # 导航意图的示例搜索逻辑
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # 交易意图的示例搜索逻辑
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # 个性化示例逻辑
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # 返回前10个个性化结果
   ```

5. <strong>示例用法</strong>

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

## 4. 将代码生成作为工具

代码生成代理使用 AI 模型编写和执行代码，以解决复杂问题和自动化任务。

### 代码生成代理

代码生成代理使用生成式 AI 模型来编写和执行代码。这些代理可以通过生成和运行各种编程语言的代码来解决复杂问题、自动化任务并提供有价值的洞见。

#### 实际应用

1. <strong>自动代码生成</strong>：为特定任务生成代码段，如数据分析、网页爬取或机器学习。
2. **将 SQL 用作 RAG**：使用 SQL 查询从数据库检索和操作数据。
3. <strong>问题解决</strong>：创建并执行代码以解决具体问题，如优化算法或分析数据。

#### 示例：用于数据分析的代码生成代理

假设你正在设计一个代码生成代理。它的工作流程可能如下：

1. <strong>任务</strong>：分析数据集以识别趋势和模式。
2. <strong>步骤</strong>：
   - 将数据集加载到数据分析工具中。
   - 生成 SQL 查询以过滤和聚合数据。
   - 执行查询并获取结果。
   - 使用结果生成可视化和洞见。
3. <strong>所需资源</strong>：访问数据集、数据分析工具和 SQL 能力。
4. <strong>经验</strong>：利用过去的分析结果提高未来分析的准确性和相关性。

### 示例：用于旅行代理的代码生成代理

在此示例中，我们将设计一个代码生成代理 Travel Agent，帮助用户通过生成和执行代码来规划旅行。该代理可以处理获取旅行选项、筛选结果和使用生成式 AI 编制行程等任务。

#### 代码生成代理概览

1. <strong>收集用户偏好</strong>：收集用户输入，如目的地、旅行日期、预算和兴趣。
2. <strong>生成代码以获取数据</strong>：生成代码片段检索航班、酒店和景点信息。
3. <strong>执行生成的代码</strong>：运行生成的代码以获取实时信息。
4. <strong>生成行程</strong>：将获取的数据编制成个性化旅行计划。
5. <strong>根据反馈调整</strong>：接收用户反馈，必要时重新生成代码以优化结果。

#### 逐步实现

1. <strong>收集用户偏好</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. <strong>生成代码以获取数据</strong>

   ```python
   def generate_code_to_fetch_data(preferences):
       # 示例：生成根据用户偏好搜索航班的代码
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # 示例：生成搜索酒店的代码
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. <strong>执行生成的代码</strong>

   ```python
   def execute_code(code):
       # 使用 exec 执行生成的代码
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

5. <strong>根据反馈调整</strong>

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # 根据用户反馈调整偏好设置
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # 使用更新后的偏好设置重新生成并执行代码
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### 利用环境感知与推理

基于表格的模式确实可以通过利用环境感知与推理来增强查询生成过程。

下面是一个示例说明如何实现：

1. <strong>理解模式</strong>：系统将理解表格的模式，并使用这些信息为查询生成提供基础。
2. <strong>基于反馈调整</strong>：系统将根据反馈调整用户偏好，并推理哪些模式字段需要更新。
3. <strong>生成并执行查询</strong>：系统将生成并执行查询，根据新偏好获取更新的航班和酒店数据。

这是一个结合上述概念的更新 Python 代码示例：

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # 根据用户反馈调整偏好设置
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # 基于模式推理以调整其他相关偏好
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # 根据模式和反馈自定义逻辑以调整偏好
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # 生成代码以根据更新的偏好获取航班数据
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # 生成代码以根据更新的偏好获取酒店数据
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # 模拟执行代码并返回模拟数据
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # 根据航班、酒店和景点生成行程
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# 示例模式
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# 使用示例
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# 使用更新的偏好重新生成并执行代码
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### 说明 - 基于反馈的预订

1. <strong>模式感知</strong>：`schema` 字典定义了基于反馈如何调整偏好，包括 `favorites` 和 `avoid` 等字段及其对应调整。
2. **调整偏好（`adjust_based_on_feedback` 方法）**：此方法根据用户反馈和模式调整偏好。
3. **基于环境的调整（`adjust_based_on_environment` 方法）**：该方法根据模式和反馈定制调整。
4. <strong>生成并执行查询</strong>：系统生成代码以基于调整后的偏好获取更新的航班和酒店数据，并模拟执行这些查询。
5. <strong>生成行程</strong>：系统基于新的航班、酒店和景点数据创建更新后的行程。

通过使系统具备环境感知能力并基于模式进行推理，它能生成更准确、更相关的查询，从而提供更好的旅行推荐和更个性化的用户体验。

### 使用 SQL 作为检索增强生成（RAG）技术

SQL（结构化查询语言）是与数据库交互的强大工具。在作为检索增强生成（RAG）方法一部分时，SQL 能从数据库中检索相关数据以支持并生成 AI 代理的响应或动作。让我们探讨如何在旅行代理中将 SQL 用作 RAG 技术。

#### 关键概念

1. <strong>数据库交互</strong>：
   - 使用 SQL 查询数据库，检索相关信息并操作数据。
   - 例如：从旅行数据库获取航班详情、酒店信息和景点数据。

2. **与 RAG 集成**：
   - 根据用户输入和偏好生成 SQL 查询。
   - 利用检索到的数据生成个性化推荐或操作。

3. <strong>动态查询生成</strong>：
   - AI 代理根据上下文和用户需求生成动态 SQL 查询。
   - 例如：定制 SQL 查询以根据预算、日期和兴趣筛选结果。

#### 应用场景

- <strong>自动代码生成</strong>：为特定任务生成代码片段。
- **将 SQL 用作 RAG**：利用 SQL 查询操作数据。
- <strong>问题解决</strong>：创建并执行代码解决问题。

<strong>示例</strong>：
一个数据分析代理：

1. <strong>任务</strong>：分析数据集找出趋势。
2. <strong>步骤</strong>：
   - 加载数据集。
   - 生成 SQL 查询过滤数据。
   - 执行查询并获取结果。
   - 生成可视化和洞见。
3. <strong>资源</strong>：数据访问权限，SQL 能力。
4. <strong>经验</strong>：利用过去结果提升未来分析效果。

#### 实际示例：在旅行代理中使用 SQL

1. <strong>收集用户偏好</strong>

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **生成 SQL 查询**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **执行 SQL 查询**

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

4. <strong>生成推荐</strong>

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

#### 示例 SQL 查询

1. <strong>航班查询</strong>

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. <strong>酒店查询</strong>

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. <strong>景点查询</strong>

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

通过利用 SQL 作为检索增强生成（RAG）技术的一部分，像旅行代理这样的 AI 代理可以动态检索并使用相关数据，从而提供准确且个性化的推荐。

### 元认知示例

为了演示元认知的实现，创建一个简单的代理，其<strong>在解决问题时反思自身的决策过程</strong>。在此示例中，我们构建一个系统，代理试图优化酒店选择，但当犯错或做出次优选择时，会评估自身推理并调整策略。

我们将通过一个基本示例模拟该过程，代理基于价格和质量组合选择酒店，但会“反思”其决策并据此调整。

#### 这展示了元认知的方式：

1. <strong>初始决策</strong>：代理将选择最便宜的酒店，未考虑质量影响。
2. <strong>反思和评估</strong>：初次选择后，代理根据用户反馈检查酒店是否是“差”选择。如果发现质量过低，它会反思其推理。
3. <strong>调整策略</strong>：代理根据反思调整策略，从“最便宜”调整为“最高质量”，从而改善未来迭代的决策过程。

示例代码如下：

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # 存储之前选择的酒店
        self.corrected_choices = []  # 存储修正后的选择
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
        # 假设我们有一些用户反馈，告诉我们上次的选择是否合适
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # 如果之前的选择不满意，则调整策略
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

# 模拟一个酒店列表（价格和质量）
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# 创建一个代理
agent = HotelRecommendationAgent()

# 第一步：代理使用“最便宜”策略推荐一家酒店
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# 第二步：代理对选择进行反思，必要时调整策略
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# 第三步：代理再次推荐，这次使用调整后的策略
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### 代理的元认知能力

关键在于代理能够：
- 评估其之前的选择和决策过程。
- 基于该反思调整策略，即元认知的实际应用。

这是一种简单形式的元认知，系统能基于内部反馈调整推理过程。

### 结论

元认知是一个强大的工具，可显著提升 AI 代理的能力。通过引入元认知过程，你可以设计出更加智能、适应性强且高效的代理。利用附加资源进一步探索 AI 代理中令人着迷的元认知世界。

### 关于元认知设计模式还有更多问题吗？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 与其他学习者交流，参加办公时间并获得 AI 代理相关问题的解答。

## 上一课

[多代理设计模式](../08-multi-agent/README.md)

## 下一课

[AI 代理的生产环境应用](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->