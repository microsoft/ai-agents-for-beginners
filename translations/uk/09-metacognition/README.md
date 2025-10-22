<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T23:38:17+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "uk"
}
-->
[![Дизайн багатозадачних агентів](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.uk.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_
# Метакогніція в AI-агентах

## Вступ

Ласкаво просимо до уроку про метакогніцію в AI-агентах! Цей розділ створений для початківців, які цікавляться тим, як AI-агенти можуть аналізувати власні процеси мислення. До кінця цього уроку ви зрозумієте ключові концепції та отримаєте практичні приклади застосування метакогніції в дизайні AI-агентів.

## Цілі навчання

Після завершення цього уроку ви зможете:

1. Зрозуміти наслідки циклів роздумів у визначенні агентів.
2. Використовувати техніки планування та оцінки для допомоги агентам у самокорекції.
3. Створювати власних агентів, здатних маніпулювати кодом для виконання завдань.

## Вступ до метакогніції

Метакогніція стосується вищих когнітивних процесів, які включають роздуми про власне мислення. Для AI-агентів це означає здатність оцінювати та коригувати свої дії на основі самосвідомості та минулого досвіду. Метакогніція, або "мислення про мислення", є важливою концепцією у розвитку агентних AI-систем. Вона передбачає, що AI-системи усвідомлюють власні внутрішні процеси та можуть контролювати, регулювати й адаптувати свою поведінку відповідно. Це схоже на те, як ми оцінюємо ситуацію або аналізуємо проблему. Така самосвідомість може допомогти AI-системам приймати кращі рішення, виявляти помилки та покращувати свою продуктивність з часом — знову повертаючись до тесту Тьюрінга та дебатів про те, чи AI може захопити світ.

У контексті агентних AI-систем метакогніція може допомогти вирішити кілька викликів, таких як:
- Прозорість: Забезпечення того, щоб AI-системи могли пояснити свої роздуми та рішення.
- Розуміння: Покращення здатності AI-систем синтезувати інформацію та приймати обґрунтовані рішення.
- Адаптація: Дозволяє AI-системам пристосовуватися до нових середовищ і змінних умов.
- Сприйняття: Підвищення точності AI-систем у розпізнаванні та інтерпретації даних із навколишнього середовища.

### Що таке метакогніція?

Метакогніція, або "мислення про мислення", — це вищий когнітивний процес, який включає самосвідомість і саморегуляцію власних когнітивних процесів. У сфері AI метакогніція надає агентам можливість оцінювати та адаптувати свої стратегії й дії, що призводить до покращення здатності вирішувати проблеми та приймати рішення. Розуміння метакогніції дозволяє створювати AI-агентів, які є не лише більш розумними, але й більш адаптивними та ефективними. У справжній метакогніції AI явно розмірковує про власні роздуми.

Приклад: «Я пріоритизував дешевші рейси, тому що… Можливо, я пропустив прямі рейси, тож перевірю ще раз».
Відстеження того, як або чому було обрано певний маршрут.
- Відзначення, що були зроблені помилки через надмірну залежність від уподобань користувача з минулого разу, тому змінюється стратегія прийняття рішень, а не лише кінцева рекомендація.
- Діагностика шаблонів, наприклад: «Коли я бачу, що користувач згадує "занадто людно", я маю не лише виключати певні атракції, але й переглянути свій метод вибору "топових атракцій", якщо я завжди ранжую за популярністю».

### Важливість метакогніції в AI-агентах

Метакогніція відіграє ключову роль у дизайні AI-агентів з кількох причин:

![Важливість метакогніції](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.uk.png)

- Саморефлексія: Агенти можуть оцінювати власну продуктивність і визначати області для покращення.
- Адаптивність: Агенти можуть змінювати свої стратегії на основі минулого досвіду та змінних умов.
- Корекція помилок: Агенти можуть автономно виявляти та виправляти помилки, що призводить до більш точних результатів.
- Управління ресурсами: Агенти можуть оптимізувати використання ресурсів, таких як час і обчислювальна потужність, плануючи та оцінюючи свої дії.

## Компоненти AI-агента

Перед тим як заглиблюватися в метакогнітивні процеси, важливо зрозуміти основні компоненти AI-агента. AI-агент зазвичай складається з:

- Персона: Особистість і характеристики агента, які визначають, як він взаємодіє з користувачами.
- Інструменти: Можливості та функції, які агент може виконувати.
- Навички: Знання та експертиза, якими володіє агент.

Ці компоненти працюють разом, створюючи "одиницю експертизи", яка може виконувати конкретні завдання.

**Приклад**:
Розглянемо туристичного агента, який не лише планує вашу відпустку, але й коригує свій маршрут на основі даних у реальному часі та минулого досвіду клієнтів.

### Приклад: Метакогніція в сервісі туристичного агента

Уявіть, що ви створюєте сервіс туристичного агента на основі AI. Цей агент, "Туристичний агент", допомагає користувачам планувати їхні відпустки. Щоб включити метакогніцію, Туристичний агент має оцінювати та коригувати свої дії на основі самосвідомості та минулого досвіду. Ось як метакогніція може відігравати роль:

#### Поточне завдання

Поточне завдання — допомогти користувачеві спланувати поїздку до Парижа.

#### Кроки для виконання завдання

1. **Збір уподобань користувача**: Запитати у користувача про його дати подорожі, бюджет, інтереси (наприклад, музеї, кухня, шопінг) та будь-які конкретні вимоги.
2. **Пошук інформації**: Знайти варіанти рейсів, проживання, атракцій та ресторанів, які відповідають уподобанням користувача.
3. **Генерація рекомендацій**: Надати персоналізований маршрут із деталями рейсів, бронюванням готелів та запропонованими активностями.
4. **Корекція на основі відгуків**: Запитати у користувача відгук про рекомендації та внести необхідні корективи.

#### Необхідні ресурси

- Доступ до баз даних бронювання рейсів і готелів.
- Інформація про паризькі атракції та ресторани.
- Дані відгуків користувачів із попередніх взаємодій.

#### Досвід і саморефлексія

Туристичний агент використовує метакогніцію для оцінки своєї продуктивності та навчання на основі минулого досвіду. Наприклад:

1. **Аналіз відгуків користувачів**: Туристичний агент переглядає відгуки користувачів, щоб визначити, які рекомендації були добре сприйняті, а які — ні. Він коригує свої майбутні пропозиції відповідно.
2. **Адаптивність**: Якщо користувач раніше згадував про нелюбов до людних місць, Туристичний агент уникатиме рекомендацій популярних туристичних місць у години пік у майбутньому.
3. **Корекція помилок**: Якщо Туристичний агент допустив помилку в минулому бронюванні, наприклад, запропонував готель, який був повністю заброньований, він навчиться ретельніше перевіряти доступність перед тим, як робити рекомендації.

#### Практичний приклад для розробників

Ось спрощений приклад того, як код Туристичного агента може виглядати з урахуванням метакогніції:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
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
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
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

#### Чому метакогніція важлива

- **Саморефлексія**: Агенти можуть аналізувати свою продуктивність і визначати області для покращення.
- **Адаптивність**: Агенти можуть змінювати стратегії на основі відгуків і змінних умов.
- **Корекція помилок**: Агенти можуть автономно виявляти та виправляти помилки.
- **Управління ресурсами**: Агенти можуть оптимізувати використання ресурсів, таких як час і обчислювальна потужність.

Інтегруючи метакогніцію, Туристичний агент може надавати більш персоналізовані та точні рекомендації для подорожей, покращуючи загальний досвід користувача.

---

## 2. Планування в агентах

Планування є критичним компонентом поведінки AI-агента. Воно включає визначення кроків, необхідних для досягнення мети, враховуючи поточний стан, ресурси та можливі перешкоди.

### Елементи планування

- **Поточне завдання**: Чітко визначити завдання.
- **Кроки для виконання завдання**: Розбити завдання на керовані етапи.
- **Необхідні ресурси**: Визначити необхідні ресурси.
- **Досвід**: Використовувати минулий досвід для інформування планування.

**Приклад**:
Ось кроки, які Туристичний агент має виконати, щоб ефективно допомогти користувачеві спланувати його подорож:

### Кроки для Туристичного агента

1. **Збір уподобань користувача**
   - Запитати у користувача деталі про його дати подорожі, бюджет, інтереси та будь-які конкретні вимоги.
   - Приклади: "Коли ви плануєте подорож?" "Який ваш бюджет?" "Які активності вам подобаються у відпустці?"

2. **Пошук інформації**
   - Знайти відповідні варіанти подорожі на основі уподобань користувача.
   - **Рейси**: Шукати доступні рейси в межах бюджету користувача та бажаних дат подорожі.
   - **Проживання**: Знайти готелі або орендовані приміщення, які відповідають уподобанням користувача щодо місця розташування, ціни та зручностей.
   - **Атракції та ресторани**: Визначити популярні атракції, активності та варіанти харчування, які відповідають інтересам користувача.

3. **Генерація рекомендацій**
   - Скомпілювати отриману інформацію в персоналізований маршрут.
   - Надати деталі, такі як варіанти рейсів, бронювання готелів та запропоновані активності, переконавшись, що рекомендації відповідають уподобанням користувача.

4. **Представлення маршруту користувачеві**
   - Поділитися запропонованим маршрутом із користувачем для його перегляду.
   - Приклад: "Ось запропонований маршрут для вашої подорожі до Парижа. Він включає деталі рейсів, бронювання готелів та список рекомендованих активностей і ресторанів. Дайте знати, що ви думаєте!"

5. **Збір відгуків**
   - Запитати у користувача відгук про запропонований маршрут.
   - Приклади: "Вам подобаються варіанти рейсів?" "Готель відповідає вашим потребам?" "Чи є активності, які ви хотіли б додати або видалити?"

6. **Корекція на основі відгуків**
   - Модифікувати маршрут на основі відгуків користувача.
   - Внести необхідні зміни до рекомендацій щодо рейсів, проживання та активностей, щоб краще відповідати уподобанням користувача.

7. **Фінальне підтвердження**
   - Представити оновлений маршрут користувачеві для фінального підтвердження.
   - Приклад: "Я вніс корективи на основі ваших відгуків. Ось оновлений маршрут. Чи все виглядає добре для вас?"

8. **Бронювання та підтвердження**
   - Після схвалення маршруту користувачем, перейти до бронювання рейсів, проживання та будь-яких запланованих активностей.
   - Надіслати деталі підтвердження користувачеві.

9. **Надання постійної підтримки**
   - Залишатися доступним для допомоги користувачеві з будь-якими змінами або додатковими запитами до та під час його подорожі.
   - Приклад: "Якщо вам потрібна будь-яка додаткова допомога під час вашої подорожі, не соромтеся звертатися до мене в будь-який час!"

### Приклад взаємодії

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

# Example usage within a booing request
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

## 3. Коригувальна система RAG

Спочатку давайте зрозуміємо різницю між інструментом RAG та попереднім завантаженням контексту.

![RAG vs Завантаження контексту](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.uk.png)

### Генерація з доповненням пошуку (RAG)

RAG поєднує систему пошуку з генеративною моделлю. Коли робиться запит, система пошуку отримує відповідні документи або дані з зовнішнього джерела, і ця отримана інформація використовується для доповнення введення до генеративної моделі. Це допомагає моделі генерувати більш точні та контекстуально релевантні відповіді.

У системі RAG агент отримує відповідну інформацію з бази знань і використовує її для генерації відповідних відповідей або дій.

### Коригувальний підхід RAG

Коригувальний підхід RAG зосереджується на використанні технік RAG для виправлення помилок і покращення точності AI-агентів. Це включає:

1. **Техніка підказок**: Використання конкретних підказок для направлення агента у пошуку відповідної інформації.
2. **Інструмент**: Реалізація алгоритмів і механізмів, які дозволяють агенту оцінювати релевантність отриманої інформації та генерувати точні відповіді.
3. **Оцінка**: Постійна оцінка продуктивності агента та внесення коректив для покращення його точності та ефективності.

#### Приклад: Коригувальний RAG у пошуковому агенті

Розглянемо пошукового агента, який отримує інформацію з вебу для відповіді на запити користувачів. Коригувальний підхід RAG може включати:

1. **Техніка підказок**: Формулювання пошукових запитів на основі введення користувача.
2. **Інструмент**: Використання алгоритмів обробки природної мови та машинного навчання для ранжування та фільтрації результатів пошуку.
3. **Оцінка**: Аналіз відгуків користувачів для виявлення та виправлення неточностей у отриманій інформації.

### Коригувальний RAG у Туристичному агенті

Коригувальний RAG (Генерація з доповненням пошуку) покращує здатність AI отримувати та генерувати інформацію, одночасно виправляючи будь-які неточності. Давайте подивимося, як Туристичний агент може використовувати коригувальний підхід RAG для надання більш точних і релевантних рекомендацій для подорожей.

Це включає:

- **Техніка підказок:** Використання конкретних підказок для направлення агента у пошуку відповідної інформації.
- **Інструмент:** Реалізація алгоритмів і механізмів, які дозволяють агенту оцін
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

# Example usage
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

### Попереднє завантаження контексту

Попереднє завантаження контексту передбачає завантаження відповідної інформації або фону в модель перед обробкою запиту. Це означає, що модель має доступ до цієї інформації з самого початку, що допомагає їй генерувати більш обґрунтовані відповіді без необхідності отримувати додаткові дані під час процесу.

Ось спрощений приклад того, як може виглядати попереднє завантаження контексту для додатку туристичного агента на Python:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Пояснення

1. **Ініціалізація (метод `__init__`)**: Клас `TravelAgent` попередньо завантажує словник, що містить інформацію про популярні напрямки, такі як Париж, Токіо, Нью-Йорк і Сідней. Цей словник включає деталі, як-от країна, валюта, мова та основні визначні місця для кожного напрямку.

2. **Отримання інформації (метод `get_destination_info`)**: Коли користувач запитує про конкретний напрямок, метод `get_destination_info` отримує відповідну інформацію зі словника попередньо завантаженого контексту.

Завдяки попередньому завантаженню контексту додаток туристичного агента може швидко відповідати на запити користувачів без необхідності отримувати цю інформацію з зовнішнього джерела в реальному часі. Це робить додаток більш ефективним і швидким.

### Ініціалізація плану з метою перед ітерацією

Ініціалізація плану з метою передбачає початок роботи з чітко визначеною ціллю або бажаним результатом. Визначивши цю мету заздалегідь, модель може використовувати її як орієнтир протягом усього ітеративного процесу. Це допомагає забезпечити, що кожна ітерація наближає до досягнення бажаного результату, роблячи процес більш ефективним і цілеспрямованим.

Ось приклад того, як можна ініціалізувати план подорожі з метою перед ітерацією для туристичного агента на Python:

### Сценарій

Туристичний агент хоче скласти індивідуальний відпочинок для клієнта. Мета — створити маршрут подорожі, який максимально задовольнить клієнта, враховуючи його вподобання та бюджет.

### Кроки

1. Визначити вподобання клієнта та бюджет.
2. Ініціалізувати початковий план на основі цих вподобань.
3. Ітерувати, щоб уточнити план, оптимізуючи його для задоволення клієнта.

#### Код на Python

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

# Example usage
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

#### Пояснення коду

1. **Ініціалізація (метод `__init__`)**: Клас `TravelAgent` ініціалізується списком потенційних напрямків, кожен з яких має атрибути, як-от назва, вартість і тип активності.

2. **Ініціалізація плану (метод `bootstrap_plan`)**: Цей метод створює початковий план подорожі на основі вподобань клієнта та бюджету. Він перебирає список напрямків і додає їх до плану, якщо вони відповідають вподобанням клієнта та вписуються в бюджет.

3. **Відповідність вподобанням (метод `match_preferences`)**: Цей метод перевіряє, чи відповідає напрямок вподобанням клієнта.

4. **Ітерація плану (метод `iterate_plan`)**: Цей метод уточнює початковий план, намагаючись замінити кожен напрямок у плані на кращий варіант, враховуючи вподобання клієнта та бюджетні обмеження.

5. **Розрахунок вартості (метод `calculate_cost`)**: Цей метод розраховує загальну вартість поточного плану, включаючи потенційний новий напрямок.

#### Приклад використання

- **Початковий план**: Туристичний агент створює початковий план на основі вподобань клієнта щодо огляду визначних місць і бюджету в $2000.
- **Уточнений план**: Туристичний агент ітерує план, оптимізуючи його відповідно до вподобань і бюджету клієнта.

Ініціалізуючи план з чіткою метою (наприклад, максимізація задоволення клієнта) та ітеруючи для його уточнення, туристичний агент може створити індивідуальний і оптимізований маршрут подорожі для клієнта. Такий підхід забезпечує відповідність плану вподобанням і бюджету клієнта з самого початку та покращує його з кожною ітерацією.

### Використання LLM для повторного ранжування та оцінювання

Великі мовні моделі (LLM) можуть використовуватися для повторного ранжування та оцінювання, аналізуючи релевантність і якість отриманих документів або згенерованих відповідей. Ось як це працює:

**Отримання**: На першому етапі отримується набір кандидатів (документів або відповідей) на основі запиту.

**Повторне ранжування**: LLM оцінює цих кандидатів і повторно ранжує їх на основі релевантності та якості. Це забезпечує, що найрелевантніша та найякісніша інформація подається першою.

**Оцінювання**: LLM присвоює кожному кандидату оцінку, яка відображає їхню релевантність і якість. Це допомагає вибрати найкращу відповідь або документ для користувача.

Використовуючи LLM для повторного ранжування та оцінювання, система може надавати більш точну та контекстуально релевантну інформацію, покращуючи загальний досвід користувача.

Ось приклад того, як туристичний агент може використовувати велику мовну модель (LLM) для повторного ранжування та оцінювання напрямків подорожей на основі вподобань користувача на Python:

#### Сценарій — Подорож на основі вподобань

Туристичний агент хоче рекомендувати найкращі напрямки подорожей клієнту на основі його вподобань. LLM допоможе повторно ранжувати та оцінити напрямки, щоб забезпечити подання найрелевантніших варіантів.

#### Кроки:

1. Зібрати вподобання користувача.
2. Отримати список потенційних напрямків подорожей.
3. Використати LLM для повторного ранжування та оцінювання напрямків на основі вподобань користувача.

Ось як можна оновити попередній приклад для використання Azure OpenAI Services:

#### Вимоги

1. Вам потрібна підписка на Azure.
2. Створіть ресурс Azure OpenAI та отримайте свій API-ключ.

#### Приклад коду на Python

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
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

# Example usage
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

#### Пояснення коду — Рекомендації на основі вподобань

1. **Ініціалізація**: Клас `TravelAgent` ініціалізується списком потенційних напрямків подорожей, кожен з яких має атрибути, як-от назва та опис.

2. **Отримання рекомендацій (метод `get_recommendations`)**: Цей метод генерує підказку для сервісу Azure OpenAI на основі вподобань користувача та надсилає HTTP POST-запит до API Azure OpenAI, щоб отримати повторно ранжовані та оцінені напрямки.

3. **Генерація підказки (метод `generate_prompt`)**: Цей метод створює підказку для Azure OpenAI, включаючи вподобання користувача та список напрямків. Підказка спрямовує модель на повторне ранжування та оцінювання напрямків на основі наданих вподобань.

4. **Виклик API**: Бібліотека `requests` використовується для надсилання HTTP POST-запиту до кінцевої точки API Azure OpenAI. Відповідь містить повторно ранжовані та оцінені напрямки.

5. **Приклад використання**: Туристичний агент збирає вподобання користувача (наприклад, інтерес до огляду визначних місць і різноманітної культури) та використовує сервіс Azure OpenAI для отримання повторно ранжованих і оцінених рекомендацій щодо напрямків подорожей.

Не забудьте замінити `your_azure_openai_api_key` на ваш фактичний API-ключ Azure OpenAI і `https://your-endpoint.com/...` на фактичну URL-адресу кінцевої точки вашого розгортання Azure OpenAI.

Використовуючи LLM для повторного ранжування та оцінювання, туристичний агент може надавати більш персоналізовані та релевантні рекомендації щодо подорожей клієнтам, покращуючи їхній загальний досвід.
#### Практичний приклад: Пошук з наміром у Travel Agent

Розглянемо Travel Agent як приклад, щоб побачити, як можна реалізувати пошук з наміром.

1. **Збір уподобань користувача**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Розуміння намірів користувача**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Контекстна обізнаність**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Пошук і персоналізація результатів**

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
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **Приклад використання**

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

## 4. Генерація коду як інструмент

Агенти, що генерують код, використовують AI-моделі для написання та виконання коду, вирішення складних задач і автоматизації процесів.

### Агенти, що генерують код

Агенти, що генерують код, застосовують генеративні AI-моделі для написання та виконання коду. Ці агенти можуть вирішувати складні задачі, автоматизувати процеси та надавати цінні інсайти, генеруючи та виконуючи код різними мовами програмування.

#### Практичні застосування

1. **Автоматична генерація коду**: Генерація фрагментів коду для конкретних задач, таких як аналіз даних, веб-скрапінг або машинне навчання.
2. **SQL як RAG**: Використання SQL-запитів для отримання та обробки даних із баз даних.
3. **Розв'язання задач**: Створення та виконання коду для вирішення конкретних проблем, таких як оптимізація алгоритмів або аналіз даних.

#### Приклад: Агент, що генерує код для аналізу даних

Уявіть, що ви створюєте агента, який генерує код. Ось як це може працювати:

1. **Задача**: Аналіз набору даних для виявлення трендів і закономірностей.
2. **Кроки**:
   - Завантаження набору даних у інструмент для аналізу.
   - Генерація SQL-запитів для фільтрації та агрегування даних.
   - Виконання запитів і отримання результатів.
   - Використання результатів для створення візуалізацій та інсайтів.
3. **Необхідні ресурси**: Доступ до набору даних, інструменти для аналізу даних і можливості SQL.
4. **Досвід**: Використання попередніх результатів аналізу для покращення точності та релевантності майбутніх аналізів.

### Приклад: Агент, що генерує код для Travel Agent

У цьому прикладі ми створимо агента, Travel Agent, який допомагає користувачам планувати подорожі, генеруючи та виконуючи код. Цей агент може виконувати такі задачі, як пошук варіантів подорожі, фільтрація результатів і складання маршруту за допомогою генеративного AI.

#### Огляд агента, що генерує код

1. **Збір уподобань користувача**: Збирає дані користувача, такі як місце призначення, дати подорожі, бюджет і інтереси.
2. **Генерація коду для отримання даних**: Генерує фрагменти коду для отримання даних про рейси, готелі та атракції.
3. **Виконання згенерованого коду**: Виконує згенерований код для отримання актуальної інформації.
4. **Генерація маршруту**: Компонує отримані дані в персоналізований план подорожі.
5. **Коригування на основі зворотного зв’язку**: Отримує зворотний зв’язок від користувача і, за необхідності, регенерує код для уточнення результатів.

#### Покрокова реалізація

1. **Збір уподобань користувача**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Генерація коду для отримання даних**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Виконання згенерованого коду**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
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

4. **Генерація маршруту**

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

5. **Коригування на основі зворотного зв’язку**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Використання обізнаності про середовище та логіки

Використання схеми таблиці може покращити процес генерації запитів, застосовуючи обізнаність про середовище та логіку.

Ось приклад, як це можна реалізувати:

1. **Розуміння схеми**: Система розуміє схему таблиці та використовує цю інформацію для генерації запитів.
2. **Коригування на основі зворотного зв’язку**: Система коригує уподобання користувача на основі зворотного зв’язку та визначає, які поля в схемі потрібно оновити.
3. **Генерація та виконання запитів**: Система генерує та виконує запити для отримання оновлених даних про рейси та готелі на основі нових уподобань.

Ось оновлений приклад коду на Python, який включає ці концепції:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Пояснення - Бронювання на основі зворотного зв’язку

1. **Обізнаність про схему**: Словник `schema` визначає, як уподобання повинні коригуватися на основі зворотного зв’язку. Він включає поля, такі як `favorites` і `avoid`, з відповідними коригуваннями.
2. **Коригування уподобань (метод `adjust_based_on_feedback`)**: Цей метод коригує уподобання на основі зворотного зв’язку користувача та схеми.
3. **Коригування на основі середовища (метод `adjust_based_on_environment`)**: Цей метод налаштовує коригування на основі схеми та зворотного зв’язку.
4. **Генерація та виконання запитів**: Система генерує код для отримання оновлених даних про рейси та готелі на основі скоригованих уподобань і симулює виконання цих запитів.
5. **Генерація маршруту**: Система створює оновлений маршрут на основі нових даних про рейси, готелі та атракції.

Завдяки обізнаності про середовище та логіці на основі схеми система може генерувати більш точні та релевантні запити, що призводить до кращих рекомендацій для подорожей і більш персоналізованого досвіду користувача.

### Використання SQL як техніки Retrieval-Augmented Generation (RAG)

SQL (Structured Query Language) — це потужний інструмент для взаємодії з базами даних. Використовуючи SQL як частину підходу Retrieval-Augmented Generation (RAG), можна отримувати релевантні дані з баз даних для інформування та генерації відповідей або дій у AI-агентах. Давайте розглянемо, як SQL може бути використаний як техніка RAG у контексті Travel Agent.

#### Основні концепції

1. **Взаємодія з базою даних**:
   - SQL використовується для запитів до баз даних, отримання релевантної інформації та обробки даних.
   - Приклад: Отримання деталей рейсів, інформації про готелі та атракції з бази даних подорожей.

2. **Інтеграція з RAG**:
   - SQL-запити генеруються на основі введених даних і уподобань користувача.
   - Отримані дані використовуються для генерації персоналізованих рекомендацій або дій.

3. **Динамічна генерація запитів**:
   - AI-агент генерує динамічні SQL-запити на основі контексту та потреб користувача.
   - Приклад: Налаштування SQL-запитів для фільтрації результатів за бюджетом, датами та інтересами.

#### Застосування

- **Автоматична генерація коду**: Генерація фрагментів коду для конкретних задач.
- **SQL як RAG**: Використання SQL-запитів для обробки даних.
- **Розв'язання задач**: Створення та виконання коду для вирішення проблем.

**Приклад**:
Агент для аналізу даних:

1. **Задача**: Аналіз набору даних для виявлення трендів.
2. **Кроки**:
   - Завантаження набору даних.
   - Генерація SQL-запитів для фільтрації даних.
   - Виконання запитів і отримання результатів.
   - Генерація візуалізацій та інсайтів.
3. **Ресурси**: Доступ до набору даних, можливості SQL.
4. **Досвід**: Використання попередніх результатів для покращення майбутніх аналізів.

#### Практичний приклад: Використання SQL у Travel Agent

1. **Збір уподобань користувача**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Генерація SQL-запитів**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Виконання SQL-запитів**

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

4. **Генерація рекомендацій**

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

#### Приклад SQL-запитів

1. **Запит рейсів**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Запит готелів**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Запит атракцій**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Використовуючи SQL як частину техніки Retrieval-Augmented Generation (RAG), AI-агенти, такі як Travel Agent, можуть динамічно отримувати та використовувати релевантні дані для надання точних і персоналізованих рекомендацій.

### Приклад метакогніції

Щоб продемонструвати реалізацію метакогніції, створимо простого агента, який *аналізує свій процес прийняття рішень* під час вирішення задачі. У цьому прикладі ми побудуємо систему, де агент намагається оптимізувати вибір готелю, але потім оцінює своє власне мислення і коригує стратегію, якщо робить помилки або субоптимальні вибори.

Ми симулюємо це за допомогою базового прикладу, де агент обирає готелі на основі комбінації ціни та якості, але "рефлексує" над своїми рішеннями і коригує їх.

#### Як це ілюструє метакогніцію:

1. **Початкове рішення**: Агент обирає найдешевший готель, не враховуючи вплив якості.
2. **Рефлексія та оцінка**: Після початкового вибору агент перевіряє, чи був готель "поганим" вибором, використовуючи зворотний зв’язок користувача. Якщо якість готелю була занадто низькою, агент рефлексує над своїм мисленням.
3. **Коригування стратегії**: Агент коригує свою стратегію, переходячи від "найдешевшого" до "найякіснішого", покращуючи процес прийняття рішень у майбутніх ітераціях.

Ось приклад:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

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
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
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

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Метакогнітивні здібності агента

Основна ідея полягає в здатності агента:
- Оцінювати свої попередні вибори та процес прийняття рішень.
- Коригувати свою стратегію на основі рефлексії, тобто метакогніція в дії.

Це проста форма метакогніції, де система здатна коригувати свій процес мислення на основі внутрішнього зворотного зв’язку.

### Висновок

Метакогніція — це потужний інструмент, який може значно покращити можливості AI-агентів. Інтегруючи метакогнітивні процеси, ви можете створювати агентів, які є більш розумними, адаптивними та ефективними. Використовуйте додаткові ресурси, щоб глибше дослідити захоплюючий світ метакогніції в AI-агентах.

### Є питання щодо шаблону дизайну метакогніції?

Приєднуйтесь до [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), щоб зустрітися з іншими учасниками, відвідати години консультацій і отримати відповіді на ваші запитання щодо AI-агентів.

## Попередній урок

[Шаблон дизайну мультиагентів](../08-multi-agent/README.md)

## Наступний урок

[AI-агенти у виробництві](../10-ai-agents-production/README.md)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.