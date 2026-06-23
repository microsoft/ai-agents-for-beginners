[![Довірені AI агенти](../../../translated_images/uk/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Створення довірених AI агентів

## Вступ

У цьому уроці буде розглянуто:

- Як створювати та розгортати безпечних і ефективних AI агентів
- Важливі питання безпеки при розробці AI агентів.
- Як підтримувати конфіденційність даних та користувачів при розробці AI агентів.

## Цілі навчання

Після завершення цього уроку ви знатимете, як:

- Виявляти та зменшувати ризики при створенні AI агентів.
- Впроваджувати заходи безпеки для належного керування даними та доступом.
- Створювати AI агентів, які підтримують конфіденційність даних і забезпечують якісний користувацький досвід.

## Безпека

Спочатку розглянемо створення безпечних агентних застосунків. Безпека означає, що AI агент працює відповідно до призначення. Як творці агентних застосунків, ми маємо методи та інструменти для максимізації безпеки:

### Створення системного повідомлення

Якщо ви коли-небудь створювали AI застосунок з використанням Великих Мовних Моделей (LLM), ви знаєте важливість розробки надійного системного підказки або системного повідомлення. Ці підказки встановлюють метаправила, інструкції та вказівки щодо того, як LLM буде взаємодіяти з користувачем та даними.

Для AI агентів системний підказка ще важливіший, оскільки AI агентам потрібні дуже конкретні інструкції для виконання поставлених нами завдань.

Для створення масштабованих системних повідомлень ми можемо використовувати каркас системних повідомлень для побудови одного або кількох агентів у нашому застосунку:

![Побудова системного повідомлення](../../../translated_images/uk/system-message-framework.3a97368c92d11d68.webp)

#### Крок 1: Створення мета системного повідомлення

Мета-підказка буде використовуватися LLM для генерації системних повідомлень для агентів, яких ми створюємо. Ми проектуємо її як шаблон, щоб ефективно створювати кількох агентів у разі потреби.

Ось приклад мета системного повідомлення, яке ми дамо LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Крок 2: Створити базовий підказ

Наступний крок – створити базовий підказ для опису AI агента. Ви повинні включити роль агента, завдання, які він буде виконувати, та будь-які інші обов’язки агента.

Ось приклад:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Крок 3: Надати базове системне повідомлення LLM

Тепер ми можемо оптимізувати це системне повідомлення, надаючи мета системне повідомлення як системне повідомлення та наше базове системне повідомлення.

Це створить системне повідомлення, краще спроектоване для керування нашими AI агентами:

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

#### Крок 4: Ітерація та поліпшення

Цінність цієї системи повідомлень полягає в тому, що можна масштабувати створення системних повідомлень для кількох агентів й удосконалювати їх з часом. Рідко буває, що системне повідомлення працює з першої спроби для вашого повного випадку використання. Можливість робити невеликі коригування та покращення, змінюючи базове системне повідомлення та пропускаючи його через систему, дозволить порівнювати та оцінювати результати.

## Розуміння загроз

Щоб створити довірених AI агентів, важливо розуміти та зменшувати ризики та загрози вашому AI агенту. Розглянемо лише деякі з різних загроз AI агентам і як краще планувати і готуватися до них.

![Розуміння загроз](../../../translated_images/uk/understanding-threats.89edeada8a97fc0f.webp)

### Завдання та інструкції

**Опис:** Зловмисники намагаються змінити інструкції або цілі AI агента через підказки або маніпуляції вхідними даними.

**Пом’якшення**: Виконуйте перевірки валідації та фільтри вхідних даних для виявлення потенційно небезпечних підказок до того, як їх обробить AI агент. Оскільки ці атаки зазвичай вимагають частої взаємодії з агентом, обмеження кількості ходів у розмові — інший спосіб запобігти такого роду атакам.

### Доступ до критичних систем

**Опис:** Якщо AI агент має доступ до систем і служб, що зберігають конфіденційні дані, зловмисники можуть скомпрометувати комунікацію між агентом і цими службами. Це можуть бути прямі атаки або непрямі спроби отримати інформацію про ці системи через агента.

**Пом’якшення:** AI агенти повинні мати доступ до систем лише за необхідності, щоб запобігти такого роду атакам. Комунікація між агентом і системою також має бути захищеною. Впровадження аутентифікації та контролю доступу є іншим способом захисту цієї інформації.

### Перевантаження ресурсів та служби

**Опис:** AI агенти можуть отримувати доступ до різних інструментів і служб для виконання завдань. Зловмисники можуть скористатися цією здатністю для атак на ці служби, надсилаючи великий обсяг запитів через AI агента, що може призвести до відмов систем або високих витрат.

**Пом’якшення:** Впровадьте політики для обмеження кількості запитів, які AI агент може робити до служби. Обмеження кількості ходів розмови та запитів до вашого AI агента — ще один спосіб запобігти такого роду атакам.

### Отруєння бази знань

**Опис:** Цей тип атаки не спрямований безпосередньо на AI агент, а на базу знань та інші служби, які AI агент використовуватиме. Це може включати пошкодження даних або інформації, яку AI агент використовуватиме для виконання завдань, що призведе до упереджених або небажаних відповідей користувачу.

**Пом’якшення:** Регулярно перевіряйте дані, які AI агент використовуватиме у своїх робочих процесах. Переконайтеся, що доступ до цих даних захищений і їх змінюють лише довірені особи, щоб уникнути такого роду атак.

### Каскадні помилки

**Опис:** AI агенти отримують доступ до різних інструментів і служб для виконання завдань. Помилки, спричинені зловмисниками, можуть призвести до відмов інших систем, до яких підключений AI агент, що робить атаку більш масштабною і складнішою для усунення.

**Пом’якшення**: Один зі способів уникнути цього — працювати AI агенту в обмеженому середовищі, наприклад, виконуючи завдання в Docker контейнері, щоб запобігти прямим атакам на систему. Створення резервних механізмів та логіки повторних спроб при появі помилки певних систем – ще один спосіб уникнути великих збоїв.

## Людина в циклі

Ще один ефективний спосіб створення довірених систем AI агентів — використання Людини в циклі. Це створює потік, де користувачі можуть надавати зворотний зв’язок агентам під час виконання. Користувачі фактично виступають як агенти в мультіагентній системі, надаючи схвалення або припинення роботи процесу.

![Людина в циклі](../../../translated_images/uk/human-in-the-loop.5f0068a678f62f4f.webp)

Ось фрагмент коду з використанням Microsoft Agent Framework, який показує, як реалізується ця концепція:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Створіть провайдера з погодженням за участю людини
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Створіть агента з кроком погодження людиною
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Користувач може переглянути та схвалити відповідь
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Висновок

Створення довірених AI агентів вимагає ретельного проектування, надійних заходів безпеки та безперервної ітерації. Впроваджуючи структуровані системи мета-підказок, розуміючи потенційні загрози та застосовуючи стратегії пом’якшення, розробники можуть створювати AI агентів, які є безпечними та ефективними. Крім того, включення підходу «Людина в циклі» гарантує, що AI агенти залишаються узгодженими з потребами користувачів, мінімізуючи ризики. Оскільки AI продовжує розвиватися, підтримка проактивного підходу до безпеки, конфіденційності та етичних аспектів буде ключовою для формування довіри та надійності у системах на основі AI.

## Приклади коду

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Крок за кроком демонстрація системи мета-підказок.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Ворота переддії, ранжування ризиків та журнал аудиту для довірених агентів.

### Маєте більше питань про створення довірених AI агентів?

Приєднуйтесь до [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), щоб зустрітися з іншими навчаючимися, відвідати години консультацій і отримати відповіді на свої питання про AI агенти.

## Додаткові ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Огляд відповідального використання AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оцінка генеративних AI моделей та застосунків AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системні повідомлення безпеки</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон оцінки ризиків</a>

## Попередній урок

[Agentic RAG](../05-agentic-rag/README.md)

## Наступний урок

[Патерн проектування планування](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->