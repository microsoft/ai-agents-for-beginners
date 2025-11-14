<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T12:26:13+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "ru"
}
-->
[![Доверенные AI-агенты](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.ru.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Создание доверенных AI-агентов

## Введение

В этом уроке мы рассмотрим:

- Как создавать и внедрять безопасных и эффективных AI-агентов.
- Важные аспекты безопасности при разработке AI-агентов.
- Как обеспечить конфиденциальность данных и пользователей при разработке AI-агентов.

## Цели обучения

После завершения этого урока вы сможете:

- Определять и снижать риски при создании AI-агентов.
- Реализовывать меры безопасности для правильного управления данными и доступом.
- Создавать AI-агентов, которые сохраняют конфиденциальность данных и обеспечивают качественный пользовательский опыт.

## Безопасность

Сначала давайте рассмотрим создание безопасных агентных приложений. Безопасность означает, что AI-агент выполняет задачи в соответствии с заданным дизайном. У разработчиков агентных приложений есть методы и инструменты для максимизации безопасности:

### Создание структуры системных сообщений

Если вы когда-либо создавали AI-приложение с использованием больших языковых моделей (LLMs), вы знаете, насколько важно разработать надежный системный запрос или системное сообщение. Эти запросы устанавливают метаправила, инструкции и рекомендации для взаимодействия LLM с пользователем и данными.

Для AI-агентов системный запрос еще более важен, так как AI-агенты нуждаются в четких инструкциях для выполнения задач, которые мы для них разработали.

Чтобы создавать масштабируемые системные запросы, мы можем использовать структуру системных сообщений для создания одного или нескольких агентов в нашем приложении:

![Создание структуры системных сообщений](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.ru.png)

#### Шаг 1: Создайте мета-системное сообщение

Мета-запрос будет использоваться LLM для генерации системных запросов для агентов, которых мы создаем. Мы разрабатываем его как шаблон, чтобы эффективно создавать нескольких агентов, если это необходимо.

Вот пример мета-системного сообщения, которое мы можем предоставить LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Шаг 2: Создайте базовый запрос

Следующий шаг — создать базовый запрос для описания AI-агента. В нем следует указать роль агента, задачи, которые он будет выполнять, и любые другие его обязанности.

Вот пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Шаг 3: Предоставьте базовое системное сообщение LLM

Теперь мы можем оптимизировать это системное сообщение, предоставив мета-системное сообщение в качестве системного сообщения и наше базовое системное сообщение.

Это создаст системное сообщение, которое лучше подходит для управления нашими AI-агентами:

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

#### Шаг 4: Итерация и улучшение

Ценность этой структуры системных сообщений заключается в возможности масштабировать создание системных сообщений для нескольких агентов, а также улучшать их со временем. Редко бывает, что системное сообщение идеально подходит для полного сценария использования с первого раза. Возможность вносить небольшие изменения и улучшения, изменяя базовое системное сообщение и пропуская его через систему, позволит вам сравнивать и оценивать результаты.

## Понимание угроз

Чтобы создавать доверенных AI-агентов, важно понимать и снижать риски и угрозы для вашего AI-агента. Давайте рассмотрим некоторые из различных угроз для AI-агентов и способы их предотвращения.

![Понимание угроз](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.ru.png)

### Задачи и инструкции

**Описание:** Злоумышленники пытаются изменить инструкции или цели AI-агента через запросы или манипуляцию входными данными.

**Меры противодействия:** Выполняйте проверки и фильтрацию входных данных, чтобы обнаружить потенциально опасные запросы до их обработки AI-агентом. Поскольку такие атаки обычно требуют частого взаимодействия с агентом, ограничение количества ходов в разговоре — еще один способ предотвратить подобные атаки.

### Доступ к критическим системам

**Описание:** Если AI-агент имеет доступ к системам и сервисам, хранящим конфиденциальные данные, злоумышленники могут скомпрометировать связь между агентом и этими сервисами. Это могут быть прямые атаки или косвенные попытки получить информацию о системах через агента.

**Меры противодействия:** AI-агенты должны иметь доступ к системам только в случае необходимости, чтобы предотвратить такие атаки. Связь между агентом и системой должна быть защищена. Реализация аутентификации и контроля доступа — еще один способ защитить эту информацию.

### Перегрузка ресурсов и сервисов

**Описание:** AI-агенты могут использовать различные инструменты и сервисы для выполнения задач. Злоумышленники могут использовать эту возможность для атак на сервисы, отправляя большое количество запросов через AI-агента, что может привести к сбоям системы или высоким затратам.

**Меры противодействия:** Реализуйте политики, ограничивающие количество запросов, которые AI-агент может отправить в сервис. Ограничение количества ходов в разговоре и запросов к вашему AI-агенту — еще один способ предотвратить такие атаки.

### Отравление базы знаний

**Описание:** Этот тип атаки не направлен непосредственно на AI-агента, а на базу знаний и другие сервисы, которые AI-агент будет использовать. Это может включать повреждение данных или информации, которые AI-агент будет использовать для выполнения задачи, что приведет к предвзятым или нежелательным ответам пользователю.

**Меры противодействия:** Проводите регулярную проверку данных, которые AI-агент будет использовать в своих рабочих процессах. Убедитесь, что доступ к этим данным защищен и изменения вносятся только доверенными лицами, чтобы избежать такого рода атак.

### Каскадные ошибки

**Описание:** AI-агенты используют различные инструменты и сервисы для выполнения задач. Ошибки, вызванные злоумышленниками, могут привести к сбоям других систем, с которыми связан AI-агент, что делает атаку более масштабной и сложной для устранения.

**Меры противодействия:** Один из способов избежать этого — заставить AI-агента работать в ограниченной среде, например, выполнять задачи в контейнере Docker, чтобы предотвратить прямые атаки на систему. Создание механизмов резервного копирования и логики повторных попыток при получении ошибок от определенных систем — еще один способ предотвратить более крупные сбои системы.

## Человек в процессе

Еще один эффективный способ создания доверенных систем AI-агентов — использование подхода "человек в процессе". Это создает поток, в котором пользователи могут предоставлять обратную связь агентам во время выполнения задач. Пользователи фактически выступают в роли агентов в многоагентной системе, предоставляя одобрение или прекращая выполнение процесса.

![Человек в процессе](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.ru.png)

Вот пример кода с использованием AutoGen, демонстрирующий, как реализуется эта концепция:

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

## Заключение

Создание доверенных AI-агентов требует тщательного проектирования, надежных мер безопасности и постоянной итерации. Реализуя структурированные системы мета-запросов, понимая потенциальные угрозы и применяя стратегии их предотвращения, разработчики могут создавать AI-агентов, которые одновременно безопасны и эффективны. Кроме того, внедрение подхода "человек в процессе" гарантирует, что AI-агенты остаются согласованными с потребностями пользователей, минимизируя риски. По мере развития AI поддержание активной позиции в вопросах безопасности, конфиденциальности и этических аспектов будет ключом к укреплению доверия и надежности в системах, управляемых AI.

### Остались вопросы о создании доверенных AI-агентов?

Присоединяйтесь к [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), чтобы встретиться с другими учащимися, посетить офисные часы и получить ответы на свои вопросы о AI-агентах.

## Дополнительные ресурсы

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Обзор ответственного использования AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка генеративных AI-моделей и AI-приложений</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системные сообщения для обеспечения безопасности</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон оценки рисков</a>

## Предыдущий урок

[Agentic RAG](../05-agentic-rag/README.md)

## Следующий урок

[Паттерн проектирования планирования](../07-planning-design/README.md)

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.