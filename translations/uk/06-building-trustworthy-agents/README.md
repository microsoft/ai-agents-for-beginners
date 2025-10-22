<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T23:41:52+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "uk"
}
-->
[![Довірені AI-агенти](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.uk.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Створення довірених AI-агентів

## Вступ

Цей урок охоплює:

- Як створювати та розгортати безпечних і ефективних AI-агентів.
- Важливі аспекти безпеки при розробці AI-агентів.
- Як забезпечити конфіденційність даних і користувачів під час розробки AI-агентів.

## Цілі навчання

Після завершення цього уроку ви знатимете, як:

- Визначати та зменшувати ризики при створенні AI-агентів.
- Реалізовувати заходи безпеки для належного управління даними та доступом.
- Створювати AI-агентів, які зберігають конфіденційність даних і забезпечують якісний користувацький досвід.

## Безпека

Спочатку розглянемо створення безпечних агентних додатків. Безпека означає, що AI-агент виконує свої функції відповідно до задуму. Як розробники агентних додатків, ми маємо методи та інструменти для максимізації безпеки:

### Створення фреймворку системних повідомлень

Якщо ви коли-небудь створювали AI-додаток із використанням великих мовних моделей (LLMs), ви знаєте, наскільки важливо розробити надійний системний запит або системне повідомлення. Ці запити встановлюють мета-правила, інструкції та керівні принципи для взаємодії LLM із користувачем і даними.

Для AI-агентів системний запит ще важливіший, оскільки вони потребують дуже конкретних інструкцій для виконання завдань, які ми для них розробили.

Щоб створювати масштабовані системні запити, ми можемо використовувати фреймворк системних повідомлень для створення одного або кількох агентів у нашому додатку:

![Створення фреймворку системних повідомлень](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.uk.png)

#### Крок 1: Створіть мета-системне повідомлення

Мета-запит буде використовуватися LLM для генерації системних запитів для агентів, яких ми створюємо. Ми розробляємо його як шаблон, щоб ефективно створювати кілька агентів за потреби.

Ось приклад мета-системного повідомлення, яке ми можемо надати LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Крок 2: Створіть базовий запит

Наступний крок — створити базовий запит для опису AI-агента. Ви повинні включити роль агента, завдання, які він виконуватиме, та інші його обов’язки.

Ось приклад:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Крок 3: Надання базового системного повідомлення LLM

Тепер ми можемо оптимізувати це системне повідомлення, надавши мета-системне повідомлення як системне повідомлення разом із нашим базовим системним повідомленням.

Це створить системне повідомлення, яке краще підходить для керування нашими AI-агентами:

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

#### Крок 4: Ітерація та вдосконалення

Цінність цього фреймворку системних повідомлень полягає в тому, щоб спростити створення системних повідомлень для кількох агентів, а також покращувати їх із часом. Рідко буває, що системне повідомлення працює ідеально з першого разу для всього випадку використання. Можливість вносити невеликі зміни та вдосконалення, змінюючи базове системне повідомлення та пропускаючи його через систему, дозволяє порівнювати та оцінювати результати.

## Розуміння загроз

Щоб створювати довірені AI-агенти, важливо розуміти та зменшувати ризики й загрози для вашого AI-агента. Розгляньмо деякі з можливих загроз для AI-агентів і способи їх уникнення.

![Розуміння загроз](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.uk.png)

### Завдання та інструкції

**Опис:** Зловмисники намагаються змінити інструкції або цілі AI-агента через запити або маніпуляцію вхідними даними.

**Запобігання:** Виконуйте перевірки та фільтрацію вхідних даних, щоб виявляти потенційно небезпечні запити до їх обробки AI-агентом. Оскільки ці атаки зазвичай вимагають частих взаємодій із агентом, обмеження кількості кроків у розмові є ще одним способом запобігання таким атакам.

### Доступ до критичних систем

**Опис:** Якщо AI-агент має доступ до систем і сервісів, які зберігають конфіденційні дані, зловмисники можуть скомпрометувати зв’язок між агентом і цими сервісами. Це можуть бути прямі атаки або непрямі спроби отримати інформацію про ці системи через агента.

**Запобігання:** AI-агенти повинні мати доступ до систем лише за необхідності, щоб запобігти таким атакам. Зв’язок між агентом і системою також має бути захищеним. Реалізація автентифікації та контролю доступу є ще одним способом захисту цієї інформації.

### Перевантаження ресурсів і сервісів

**Опис:** AI-агенти можуть отримувати доступ до різних інструментів і сервісів для виконання завдань. Зловмисники можуть використовувати цю можливість для атак на ці сервіси, надсилаючи велику кількість запитів через AI-агента, що може призвести до збоїв у системі або високих витрат.

**Запобігання:** Реалізуйте політики для обмеження кількості запитів, які AI-агент може надсилати до сервісу. Обмеження кількості кроків у розмові та запитів до вашого AI-агента є ще одним способом запобігання таким атакам.

### Отруєння бази знань

**Опис:** Цей тип атаки не спрямований безпосередньо на AI-агента, а на базу знань та інші сервіси, які використовує AI-агент. Це може включати пошкодження даних або інформації, яку AI-агент використовуватиме для виконання завдання, що призводить до упереджених або небажаних відповідей користувачеві.

**Запобігання:** Регулярно перевіряйте дані, які AI-агент використовуватиме у своїх робочих процесах. Переконайтеся, що доступ до цих даних є захищеним і змінюється лише довіреними особами, щоб уникнути такого типу атак.

### Каскадні помилки

**Опис:** AI-агенти отримують доступ до різних інструментів і сервісів для виконання завдань. Помилки, спричинені зловмисниками, можуть призвести до збоїв інших систем, до яких підключений AI-агент, що робить атаку більш масштабною та складною для усунення.

**Запобігання:** Один із методів уникнення цього — дозволити AI-агенту працювати в обмеженому середовищі, наприклад, виконувати завдання в контейнері Docker, щоб запобігти прямим атакам на систему. Створення механізмів резервування та логіки повторних спроб у разі, якщо певні системи відповідають помилкою, є ще одним способом запобігання масштабним збоям системи.

## Людина в процесі

Ще один ефективний спосіб створення довірених систем AI-агентів — це використання підходу "людина в процесі". Це створює потік, у якому користувачі можуть надавати зворотний зв’язок агентам під час їх роботи. Користувачі фактично виступають як агенти в багатокомпонентній системі, надаючи схвалення або припиняючи виконання процесу.

![Людина в процесі](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.uk.png)

Ось приклад коду з використанням AutoGen, який демонструє, як реалізується ця концепція:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Висновок

Створення довірених AI-агентів вимагає ретельного дизайну, надійних заходів безпеки та постійної ітерації. Реалізуючи структуровані системи мета-запитів, розуміючи потенційні загрози та застосовуючи стратегії їх запобігання, розробники можуть створювати AI-агентів, які є безпечними та ефективними. Крім того, впровадження підходу "людина в процесі" забезпечує відповідність AI-агентів потребам користувачів, мінімізуючи ризики. У міру розвитку AI підтримка проактивного підходу до безпеки, конфіденційності та етичних міркувань буде ключем до зміцнення довіри та надійності в системах, керованих AI.

### Маєте додаткові запитання щодо створення довірених AI-агентів?

Приєднуйтесь до [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), щоб поспілкуватися з іншими учнями, відвідати години консультацій і отримати відповіді на ваші запитання щодо AI-агентів.

## Додаткові ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Огляд відповідального використання AI</a>  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оцінка генеративних AI-моделей і AI-додатків</a>  
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системні повідомлення для безпеки</a>  
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон оцінки ризиків</a>  

## Попередній урок

[Agentic RAG](../05-agentic-rag/README.md)

## Наступний урок

[Планування: шаблон дизайну](../07-planning-design/README.md)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.