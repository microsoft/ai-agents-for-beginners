[![Доверенные AI агенты](../../../translated_images/ru/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Создание доверенных AI агентов

## Введение

В этом уроке мы рассмотрим:

- Как создавать и запускать безопасных и эффективных AI агентов
- Важные аспекты безопасности при разработке AI агентов.
- Как сохранять данные и конфиденциальность пользователей при разработке AI агентов.

## Цели обучения

После прохождения этого урока вы будете уметь:

- Определять и снижать риски при создании AI агентов.
- Внедрять меры безопасности для обеспечения правильного управления данными и доступом.
- Создавать AI агентов, которые поддерживают конфиденциальность данных и обеспечивают качественный пользовательский опыт.

## Безопасность

Сначала рассмотрим создание безопасных агентных приложений. Безопасность означает, что AI агент работает так, как задумано. Как создатели агентных приложений, у нас есть методы и инструменты для максимизации безопасности:

### Создание системы сообщений

Если вы когда-либо создавали AI-приложение с использованием больших языковых моделей (LLM), вы знаете, как важно спроектировать надежный системный запрос или системное сообщение. Эти запросы устанавливают мета-правила, инструкции и руководства о том, как LLM будет взаимодействовать с пользователем и данными.

Для AI агентов системный запрос еще важнее, поскольку агентам нужны очень конкретные инструкции для выполнения тех задач, которые мы для них предусмотрели.

Чтобы создавать масштабируемые системные запросы, мы можем использовать систему сообщений для создания одного или нескольких агентов в нашем приложении:

![Создание системы сообщений](../../../translated_images/ru/system-message-framework.3a97368c92d11d68.webp)

#### Шаг 1: Создайте мета-системное сообщение

Мета-запрос будет использоваться LLM для генерации системных сообщений для создаваемых агентов. Мы проектируем его как шаблон, чтобы эффективно создавать несколько агентов при необходимости.

Пример мета-системного сообщения, которое мы передаём LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Шаг 2: Создайте базовый запрос

Следующий шаг — создать базовый запрос, описывающий AI агента. Следует указать роль агента, задачи, которые он будет выполнять, и любые другие его обязанности.

Пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Шаг 3: Предоставьте базовое системное сообщение LLM

Теперь мы можем оптимизировать это системное сообщение, передавая мета-системное сообщение в качестве системного сообщения вместе с нашим базовым системным сообщением.

Это создаст системное сообщение, лучше подходящее для управления нашими AI агентами:

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

#### Шаг 4: Итерации и улучшения

Ценность этой системы сообщений заключается в том, чтобы облегчить масштабное создание системных сообщений для нескольких агентов, а также улучшать системные сообщения со временем. Редко когда системное сообщение работает идеально с первого раза для полного сценария использования. Возможность делать небольшие изменения и улучшения, меняя базовое системное сообщение и пропуская его через систему, позволит вам сравнивать и оценивать результаты.

## Понимание угроз

Для создания доверенных AI агентов важно понимать и снижать риски и угрозы для вашего AI агента. Рассмотрим некоторые из различных угроз AI агентам и как вы можете лучше планировать и подготавливаться к ним.

![Понимание угроз](../../../translated_images/ru/understanding-threats.89edeada8a97fc0f.webp)

### Задача и инструкции

**Описание:** Злоумышленники пытаются изменить инструкции или цели AI агента путем подсказок или манипуляций с входными данными.

**Меры защиты:** Выполняйте проверки валидности и фильтрацию ввода, чтобы обнаруживать потенциально опасные подсказки до их обработки AI агентом. Поскольку такие атаки обычно требуют частого взаимодействия с агентом, ограничение количества ходов в разговоре — ещё один способ предотвратить эти атаки.

### Доступ к критическим системам

**Описание:** Если AI агент имеет доступ к системам и сервисам, хранящим конфиденциальные данные, злоумышленники могут скомпрометировать связь между агентом и этими сервисами. Это могут быть прямые атаки или косвенные попытки получить информацию об этих системах через агента.

**Меры защиты:** AI агенты должны иметь доступ к системам только по необходимости, чтобы предотвратить такие атаки. Связь между агентом и системой также должна быть защищена. Внедрение аутентификации и контроля доступа — ещё один способ защиты этой информации.

### Перегрузка ресурсов и сервисов

**Описание:** AI агенты могут использовать разные инструменты и сервисы для выполнения задач. Злоумышленники могут использовать эту возможность для атак на эти сервисы, отправляя большое количество запросов через AI агента, что может привести к сбоям системы или высоким затратам.

**Меры защиты:** Внедрите политики ограничения количества запросов, которые агент может сделать к сервису. Ограничение количества ходов разговора и запросов к AI агенту — ещё один способ защититься от таких атак.

### Отравление базы знаний

**Описание:** Этот вид атаки нацелен не непосредственно на AI агента, а на базу знаний и другие сервисы, которые агент использует. Это может привести к искажению данных или информации, которыми AI агент пользуется для выполнения задачи, что вызовет предвзятые или нежелательные ответы пользователю.

**Меры защиты:** Регулярно проверяйте данные, которые использует AI агент в своих рабочих процессах. Обеспечьте, чтобы доступ к этим данным был защищен и их изменяли только доверенные лица, чтобы избежать такого рода атак.

### Каскадные ошибки

**Описание:** AI агенты обращаются к разным инструментам и сервисам для выполнения задач. Ошибки, вызванные злоумышленниками, могут привести к сбоям других связанных систем, расширяя масштабы атаки и усложняя её устранение.

**Меры защиты:** Один из способов избежать этого — запускать AI агента в ограниченной среде, например, выполнять задачи в контейнере Docker, чтобы предотвратить прямые атаки на систему. Создание механизмов резервного копирования и повторных попыток при ошибках определённых систем — ещё один способ защитить систему.

## Человек в цикле

Ещё один эффективный способ создать доверенную систему AI агентов — использовать концепцию «Человек в цикле». Это создаёт поток, в котором пользователи могут оставлять обратную связь агентам во время их работы. Пользователи фактически выступают агентами в мультиагентной системе, одобряя или останавливая выполняющийся процесс.

![Человек в цикле](../../../translated_images/ru/human-in-the-loop.5f0068a678f62f4f.webp)

Вот фрагмент кода с использованием Microsoft Agent Framework, показывающий, как реализована эта концепция:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Создайте поставщика с утверждением с участием человека
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Создайте агента с шагом утверждения человеком
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Пользователь может проверить и одобрить ответ
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Заключение

Создание доверенных AI агентов требует тщательного проектирования, надежных мер безопасности и постоянной итерации. Реализуя структурированные мета-системы запросов, понимая потенциальные угрозы и применяя стратегии их снижения, разработчики могут создавать безопасных и эффективных AI агентов. Кроме того, внедрение подхода «человек в цикле» обеспечивает соответствие AI агентов потребностям пользователей при минимизации рисков. По мере развития AI, активное внимание к безопасности, конфиденциальности и этическим аспектам будет ключом к укреплению доверия и надежности систем на базе AI.

## Примеры кода

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Пошаговая демонстрация системы мета-запросов и системы сообщений.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Предварительное одобрение действий, уровни риска и ведение аудиторских журналов для доверенных агентов.

### Есть еще вопросы о создании доверенных AI агентов?

Присоединяйтесь к [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), чтобы общаться с другими учащимися, посещать офисные часы и получать ответы на вопросы по AI агентам.

## Дополнительные ресурсы

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Обзор ответственного использования AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка генеративных моделей AI и AI приложений</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системные сообщения безопасности</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон оценки рисков</a>

## Предыдущий урок

[Agentic RAG](../05-agentic-rag/README.md)

## Следующий урок

[Шаблон проектирования планирования](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->