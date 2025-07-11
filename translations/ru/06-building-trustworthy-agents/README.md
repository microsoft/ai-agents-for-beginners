<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f57852cac3a86c4a5ef47f793cc12178",
  "translation_date": "2025-07-11T14:39:04+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "ru"
}
-->
[![Доверенные AI-агенты](../../../06-building-trustworthy-agents/images/lesson-6-thumbnail.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Создание Доверенных AI-агентов

## Введение

Этот урок охватывает:

- Как создавать и развертывать безопасных и эффективных AI-агентов
- Важные соображения по безопасности при разработке AI-агентов
- Как поддерживать конфиденциальность данных и пользователей при разработке AI-агентов

## Цели обучения

После завершения этого урока вы узнаете, как:

- Определять и снижать риски при создании AI-агентов
- Реализовывать меры безопасности для надлежащего управления данными и доступом
- Создавать AI-агентов, которые сохраняют конфиденциальность данных и обеспечивают качественный пользовательский опыт

## Безопасность

Давайте сначала рассмотрим создание безопасных агентных приложений. Безопасность означает, что AI-агент выполняет свои функции так, как задумано. Как разработчики агентных приложений, мы имеем методы и инструменты для максимизации безопасности:

### Создание фреймворка системных сообщений

Если вы когда-либо создавали AI-приложение с использованием больших языковых моделей (LLM), вы знаете, насколько важно разрабатывать надежный системный запрос или системное сообщение. Эти запросы устанавливают метаправила, инструкции и руководства для взаимодействия LLM с пользователем и данными.

Для AI-агентов системный запрос еще более важен, так как AI-агенты нуждаются в очень конкретных инструкциях для выполнения задач, которые мы для них разработали.

Чтобы создать масштабируемые системные запросы, мы можем использовать фреймворк системных сообщений для создания одного или нескольких агентов в нашем приложении:

![Создание фреймворка системных сообщений](../../../06-building-trustworthy-agents/images/system-message-framework.png)

#### Шаг 1: Создание мета-системного сообщения

Мета-запрос будет использоваться LLM для генерации системных запросов для агентов, которых мы создаем. Мы разрабатываем его как шаблон, чтобы при необходимости можно было эффективно создавать несколько агентов.

Вот пример мета-системного сообщения, которое мы бы дали LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Шаг 2: Создание базового запроса

Следующий шаг — создать базовый запрос для описания AI-агента. Вы должны включить роль агента, задачи, которые агент будет выполнять, и любые другие обязанности агента.

Вот пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Шаг 3: Предоставление базового системного сообщения LLM

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

Ценность этого фреймворка системных сообщений заключается в возможности масштабировать создание системных сообщений для нескольких агентов, а также улучшать ваши системные сообщения со временем. Редко бывает, что системное сообщение работает с первого раза для вашего полного случая использования. Возможность вносить небольшие изменения и улучшения, изменяя базовое системное сообщение и пропуская его через систему, позволит вам сравнивать и оценивать результаты.

## Понимание угроз

Чтобы создать доверенных AI-агентов, важно понимать и снижать риски и угрозы для вашего AI-агента. Давайте рассмотрим некоторые из различных угроз для AI-агентов и как вы можете лучше планировать и готовиться к ним.

![Понимание угроз](../../../06-building-trustworthy-agents/images/understanding-threats.png)

### Задача и инструкция

**Описание:** Злоумышленники пытаются изменить инструкции или цели AI-агента с помощью запросов или манипуляции входными данными.

**Снижение риска**: Выполняйте проверки валидации и фильтры входных данных, чтобы обнаруживать потенциально опасные запросы до их обработки AI-агентом. Поскольку эти атаки обычно требуют частого взаимодействия с агентом, ограничение количества ходов в разговоре — еще один способ предотвратить такие атаки.

### Доступ к критическим системам

**Описание**: Если AI-агент имеет доступ к системам и сервисам, которые хранят конфиденциальные данные, злоумышленники могут скомпрометировать связь между агентом и этими сервисами. Это могут быть прямые атаки или косвенные попытки получить информацию об этих системах через агента.

**Снижение риска**: AI-агенты должны иметь доступ к системам только по мере необходимости, чтобы предотвратить такие атаки. Связь между агентом и системой также должна быть безопасной. Реализация аутентификации и контроля доступа — еще один способ защитить эту информацию.

### Перегрузка ресурсов и сервисов

**Описание:** AI-агенты могут получать доступ к различным инструментам и сервисам для выполнения задач. Злоумышленники могут использовать эту возможность для атаки на эти сервисы, отправляя большое количество запросов через AI-агента, что может привести к сбоям в системе или высоким затратам.

**Снижение риска:** Реализуйте политики, чтобы ограничить количество запросов, которые AI-агент может сделать к сервису. Ограничение количества ходов в разговоре и запросов к вашему AI-агенту — еще один способ предотвратить такие атаки.

### Отравление базы знаний

**Описание:** Этот тип атаки не направлен непосредственно на AI-агента, а нацелен на базу знаний и другие сервисы, которые будет использовать AI-агент. Это может включать в себя порчу данных или информации, которую AI-агент будет использовать для выполнения задачи, что приведет к предвзятым или непреднамеренным ответам пользователю.

**Снижение риска:** Проводите регулярную проверку данных, которые AI-агент будет использовать в своих рабочих процессах. Убедитесь, что доступ к этим данным безопасен и изменяется только доверенными лицами, чтобы избежать такого типа атаки.

### Каскадные ошибки

**Описание:** AI-агенты получают доступ к различным инструментам и сервисам для выполнения задач. Ошибки, вызванные злоумышленниками, могут привести к сбоям других систем, к которым подключен AI-агент, что делает атаку более распространенной и сложной для устранения.

**Снижение риска**: Один из способов избежать этого — позволить AI-агенту работать в ограниченной среде, например, выполнять задачи в контейнере Docker, чтобы предотвратить прямые атаки на систему. Создание механизмов резервного копирования и логики повторных попыток, когда определенные системы отвечают с ошибкой, — еще один способ предотвратить более крупные сбои в системе.

## Человек в цикле

Еще один эффективный способ создания доверенных систем AI-агентов — использование человека в цикле. Это создает поток, в котором пользователи могут предоставлять обратную связь агентам во время выполнения. Пользователи фактически выступают в роли агентов в многоагентной системе, предоставляя одобрение или завершение выполняемого процесса.

![Человек в цикле](../../../06-building-trustworthy-agents/images/human-in-the-loop.png)

Вот фрагмент кода с использованием AutoGen, чтобы показать, как реализована эта концепция:

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

Создание доверенных AI-агентов требует тщательного проектирования, надежных мер безопасности и постоянной итерации. Реализуя структурированные системы мета-запросов, понимая потенциальные угрозы и применяя стратегии снижения рисков, разработчики могут создавать AI-агентов, которые безопасны и эффективны. Кроме того, внедрение подхода с человеком в цикле гарантирует, что AI-агенты остаются в соответствии с потребностями пользователей, минимизируя риски. По мере того как AI продолжает развиваться, поддержание проактивной позиции в отношении безопасности, конфиденциальности и этических соображений будет ключом к укреплению доверия и надежности в системах, управляемых AI.

## Дополнительные ресурсы

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Обзор ответственного использования AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка генеративных AI-моделей и AI-приложений</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Сообщения системы безопасности</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон оценки рисков</a>

## Предыдущий урок

[Агентный RAG](../05-agentic-rag/README.md)

## Следующий урок

[Планирование шаблона проектирования](../07-planning-design/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.