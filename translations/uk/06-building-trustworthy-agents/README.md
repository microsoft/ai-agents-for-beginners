[![Довірені AI агенти](../../../translated_images/uk/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Клацніть на зображенні вище, щоб переглянути відео цього уроку)_

# Створення довірених AI агентів

## Вступ

У цьому уроці розглянемо:

- Як створювати та розгортати безпечних і ефективних AI агентів
- Важливі аспекти безпеки при розробці AI агентів.
- Як підтримувати конфіденційність даних та користувачів при розробці AI агентів.

## Цілі навчання

Після завершення цього уроку ви знатимете, як:

- Виявляти та зменшувати ризики при створенні AI агентів.
- Впроваджувати заходи безпеки для належного управління даними та доступом.
- Створювати AI агентів, які підтримують конфіденційність даних та забезпечують якісний користувацький досвід.

## Безпека

Спершу розглянемо створення безпечних агентних додатків. Безпека означає, що AI агент працює так, як задумано. Як розробники агентних додатків, ми маємо методи та інструменти для максимізації безпеки:

### Створення системи повідомлень (System Message Framework)

Якщо ви коли-небудь створювали AI-додаток із використанням великих мовних моделей (LLM), ви знаєте, наскільки важливо розробити надійний системний запит або системне повідомлення. Ці запити встановлюють метаправила, інструкції та керівні принципи того, як LLM взаємодіятиме з користувачем і даними.

Для AI агентів системний запит ще важливіший, оскільки їм потрібні дуже конкретні інструкції для виконання задач, які ми для них розробили.

Щоб створювати масштабовані системні запити, можна використати фреймворк системних повідомлень для побудови одного або кількох агентів у додатку:

![Створення системи повідомлень](../../../translated_images/uk/system-message-framework.3a97368c92d11d68.webp)

#### Крок 1: Створити мета-системне повідомлення 

Мета-запит використовує LLM для генерації системних запитів для створюваних агентів. Ми проектуємо його як шаблон, щоб ефективно створювати кілька агентів за потреби.

Ось приклад мета-системного повідомлення, яке ми дадемо LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Крок 2: Створити базовий запит

Наступний крок — створити базовий запит для опису AI агента. Варто включити роль агента, задачі, які він виконує, та інші його обов’язки.

Ось приклад:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Крок 3: Надати базове системне повідомлення LLM

Тепер ми можемо оптимізувати це системне повідомлення, передавши як системне повідомлення мета-системне повідомлення та наше базове системне повідомлення.

Це створить системне повідомлення, краще призначене для керівництва нашими AI агентами:

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

#### Крок 4: Ітерації та покращення

Цінність цього фреймворку системних повідомлень полягає у тому, що він полегшує масштабування створення системних повідомлень для кількох агентів, а також покращення ваших системних повідомлень з часом. Рідко буває, що системне повідомлення спрацьовує з першого разу для вашого повного випадку використання. Можливість робити невеликі коригування, змінюючи базове системне повідомлення та пропускаючи його через систему, дає змогу порівнювати й оцінювати результати.

## Розуміння загроз

Щоб створювати довірені AI агенти, важливо розуміти та зменшувати ризики й загрози для вашого AI агента. Розглянемо лише деякі загрози для AI агентів і як краще їх планувати та підготуватися.

![Розуміння загроз](../../../translated_images/uk/understanding-threats.89edeada8a97fc0f.webp)

### Задачі та інструкції

**Опис:** Зловмисники намагаються змінити інструкції або цілі AI агента через запити або маніпулювання вхідними даними.

**Пом'якшення**: Виконуйте перевірки валідації та фільтри вхідних даних, щоб виявляти потенційно небезпечні запити до їх обробки AI агентом. Оскільки такі атаки зазвичай вимагають частої взаємодії з агентом, обмеження кількості ходів у розмові — ще один спосіб запобігти таким атакам.

### Доступ до критичних систем

**Опис:** Якщо AI агент має доступ до систем і сервісів, які зберігають конфіденційні дані, зловмисники можуть зламати зв’язок між агентом та цими сервісами. Це можуть бути прямі атаки або непрямі спроби отримати інформацію про ці системи через агента.

**Пом'якшення:** AI агенти повинні мати доступ до систем лише за потребою, щоб запобігти таким атакам. Зв’язок між агентом і системою також має бути захищеним. Запровадження автентифікації та контролю доступу — ще один спосіб захисту цієї інформації.

### Перевантаження ресурсів та сервісів

**Опис:** AI агенти можуть отримувати доступ до різних інструментів і сервісів для виконання задач. Зловмисники можуть використати цю здатність для атак на ці сервіси, відправляючи через AI агента велику кількість запитів, що може призвести до збоїв систем або значних витрат.

**Пом'якшення:** Впровадьте політики, що обмежують кількість запитів, які AI агент може робити до сервісу. Обмеження кількості ходів у розмові та запитів до вашого AI агента — ще один спосіб запобігти таким атакам.

### Отруєння бази знань

**Опис:** Цей тип атаки не спрямований безпосередньо на AI агента, а на базу знань та інші сервіси, які AI агент використовує. Це може включати корупцію даних або інформації, яку агент застосовує для виконання задач, що призведе до упереджених або ненавмисних відповідей користувачу.

**Пом'якшення:** Регулярно перевіряйте дані, які AI агент використовує у своїх робочих процесах. Забезпечуйте, щоб доступ до цих даних був захищений і змінювався лише довіреними особами, щоб уникнути такого типу атаки.

### Каскадні помилки

**Опис:** AI агенти звертаються до різних інструментів і сервісів для виконання задач. Помилки, спричинені зловмисниками, можуть призвести до збоїв інших систем, з якими агент пов’язаний, що робить атаку більш масштабною та складнішою для усунення.

**Пом'якшення:** Один із способів уникнути цього — щоб AI агент працював у обмеженому середовищі, наприклад, виконуючи задачі в контейнері Docker, щоб запобігти прямим атакам на систему. Створення механізмів відкату та логіки повтору при помилках певних систем — ще один спосіб запобігти масштабним збоям.

## Людина в циклі (Human-in-the-Loop)

Ще одним ефективним способом створення довірених AI агентів є використання концепції Людина в циклі. Це створює процес, у якому користувачі можуть надавати зворотній зв’язок агентам під час виконання. Користувачі фактично виступають агентами в багатозадачній системі, надаючи дозвіл або припиняючи процес.

![Людина в циклі](../../../translated_images/uk/human-in-the-loop.5f0068a678f62f4f.webp)

Ось фрагмент коду з використанням Microsoft Agent Framework, що ілюструє, як реалізується цей концепт:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Створити провайдера з затвердженням за участю людини
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Створити агента з кроком затвердження людиною
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Користувач може переглянути та затвердити відповідь
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Висновок

Створення довірених AI агентів вимагає ретельного проєктування, надійних заходів безпеки та постійної ітерації. Впроваджуючи структуровані системи мета-промптів, розуміючи потенційні загрози й застосовуючи стратегії пом'якшення, розробники можуть створювати AI агентів, які є безпечними та ефективними. Крім того, інтеграція підходу Людина в циклі забезпечує відповідність AI агентів потребам користувачів і мінімізує ризики. Оскільки AI продовжує розвиватися, підтримка проактивної позиції щодо безпеки, конфіденційності та етичних аспектів буде ключовою для формування довіри та надійності систем на базі AI.

## Приклади коду

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Покрокова демонстрація системи мета-промптів у system-message framework.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Схеми попереднього затвердження дій, рейтинги ризиків та журналювання аудиту для довірених агентів.

### Маєте більше запитань про створення довірених AI агентів?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб зустріти інших учнів, відвідувати години консультацій та отримати відповіді на ваші питання про AI агентів.

## Додаткові ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Огляд відповідального використання AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оцінка моделей генеративного AI та додатків AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Повідомлення системи безпеки</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон оцінки ризиків</a>

## Попередній урок

[Agentic RAG](../05-agentic-rag/README.md)

## Наступний урок

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->