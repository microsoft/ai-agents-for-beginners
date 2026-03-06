[![Надежные агенты ИИ](../../../translated_images/ru/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Нажмите на изображение выше, чтобы просмотреть видео этого урока)_

# Создание надежных агентов ИИ

## Введение

В этом уроке будут рассмотрены:

- Как создавать и развёртывать безопасных и эффективных агентов ИИ
- Важные соображения по безопасности при разработке агентов ИИ
- Как обеспечивать конфиденциальность данных и пользователей при разработке агентов ИИ

## Цели обучения

После завершения этого урока вы узнаете, как:

- Определять и снижать риски при создании агентов ИИ
- Реализовывать меры безопасности для надлежащего управления данными и доступом
- Создавать агентов ИИ, которые сохраняют конфиденциальность данных и обеспечивают качественный пользовательский опыт

## Безопасность

Сначала рассмотрим создание безопасных агентных приложений. Безопасность означает, что агент ИИ работает в соответствии с задумкой. Как создатели агентных приложений, мы располагаем методами и инструментами для максимизации безопасности:

### Создание фреймворка системных сообщений

Если вы когда-либо создавали ИИ-приложение с использованием больших языковых моделей (LLM), вы знаете, насколько важно разработать надёжный системный промпт или системное сообщение. Эти промпты устанавливают метаправила, инструкции и рекомендации о том, как LLM будет взаимодействовать с пользователем и данными.

Для агентов ИИ системный промпт ещё более важен, так как агентам ИИ потребуются очень конкретные инструкции для выполнения задач, которые мы для них разработали.

Чтобы создавать масштабируемые системные промпты, мы можем использовать фреймворк системных сообщений для построения одного или нескольких агентов в нашем приложении:

![Создание фреймворка системных сообщений](../../../translated_images/ru/system-message-framework.3a97368c92d11d68.webp)

#### Шаг 1: Создать мета-системное сообщение

Мета-промпт будет использоваться LLM для генерации системных промптов для создаваемых нами агентов. Мы разрабатываем его как шаблон, чтобы эффективно создавать несколько агентов при необходимости.

Вот пример мета-системного сообщения, который мы бы передали LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Шаг 2: Создать базовый промпт

Следующий шаг — создать базовый промпт для описания агента ИИ. Вам следует включить роль агента, задачи, которые агент будет выполнять, и любые другие обязанности агента.

Вот пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Шаг 3: Передать базовое системное сообщение LLM

Теперь мы можем оптимизировать это системное сообщение, предоставив мета-системное сообщение как системное сообщение и наше базовое системное сообщение.

Это создаст системное сообщение, которое лучше подходит для управления нашими агентами ИИ:

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

Ценность этого фреймворка системных сообщений заключается в возможности масштабировать создание системных сообщений для нескольких агентов, а также в улучшении ваших системных сообщений со временем. Редко бывает так, что системное сообщение с первого раза работает для всего вашего сценария использования. Возможность вносить небольшие изменения и улучшения, изменяя базовое системное сообщение и прогоняя его через систему, позволит вам сравнивать и оценивать результаты.

## Понимание угроз

Чтобы создавать надежных агентов ИИ, важно понимать и снижать риски и угрозы для вашего агента ИИ. Рассмотрим некоторые из различных угроз для агентов ИИ и как лучше планировать и готовиться к ним.

![Понимание угроз](../../../translated_images/ru/understanding-threats.89edeada8a97fc0f.webp)

### Задача и инструкция

**Описание:** Злоумышленники пытаются изменить инструкции или цели агента ИИ с помощью подсказок или манипуляции входными данными.

**Меры смягчения**: Выполняйте проверки валидации и фильтры входных данных, чтобы обнаруживать потенциально опасные подсказки до их обработки агентом ИИ. Поскольку эти атаки обычно требуют частого взаимодействия с агентом, ограничение количества ходов в разговоре — ещё один способ предотвратить такого рода атаки.

### Доступ к критическим системам

**Описание**: Если агент ИИ имеет доступ к системам и сервисам, хранящим конфиденциальные данные, злоумышленники могут скомпрометировать связь между агентом и этими сервисами. Это могут быть прямые атаки или косвенные попытки получить информацию об этих системах через агента.

**Меры смягчения**: Агентам ИИ следует предоставлять доступ к системам только при необходимости, чтобы предотвратить такого рода атаки. Также связь между агентом и системой должна быть защищена. Реализация аутентификации и контроля доступа — ещё один способ защитить эту информацию.

### Перегрузка ресурсов и сервисов

**Описание:** Агенты ИИ могут обращаться к различным инструментам и службам для выполнения задач. Злоумышленники могут использовать эту возможность для атак на эти сервисы, отправляя большой объём запросов через агента ИИ, что может привести к сбоям в системе или высоким расходам.

**Меры смягчения:** Внедряйте политики, ограничивающие число запросов, которые агент ИИ может отправлять в сервис. Ограничение числа ходов в беседе и запросов к вашему агенту ИИ — ещё один способ предотвратить такого рода атаки.

### Заражение базы знаний

**Описание:** Этот тип атаки не направлен непосредственно на агента ИИ, а на базу знаний и другие сервисы, которые агент ИИ будет использовать. Это может включать порчу данных или информации, которую агент ИИ использует для выполнения задачи, что приведёт к предвзятым или непреднамеренным ответам пользователю.

**Меры смягчения:** Проводите регулярную проверку данных, которые агент ИИ будет использовать в своих рабочих процессах. Убедитесь, что доступ к этим данным защищён и ими могут изменять только доверенные лица, чтобы избежать такого типа атак.

### Каскадные ошибки

**Описание:** Агенты ИИ обращаются к различным инструментам и сервисам для выполнения задач. Ошибки, вызванные злоумышленниками, могут привести к сбоям в других системах, к которым подключён агент ИИ, что сделает атаку более распространённой и трудной для устранения.

**Меры смягчения**: Один из способов избежать этого — запускать агента ИИ в ограниченном окружении, например выполнять задачи в контейнере Docker, чтобы предотвратить прямые системные атаки. Создание механизмов резервного копирования и логики повторных попыток при получении ошибок от некоторых систем — ещё один способ предотвратить более масштабные сбои.

## Человек в цикле

Ещё один эффективный способ создания надёжных систем агентов ИИ — использование подхода «человек в цикле». Это создаёт поток, где пользователи могут предоставлять обратную связь агентам во время выполнения. Пользователи фактически выступают в роли агентов в многопользовательской системе, одобряя или прекращая выполняемый процесс.

![Человек в цикле](../../../translated_images/ru/human-in-the-loop.5f0068a678f62f4f.webp)

Вот фрагмент кода с использованием Microsoft Agent Framework, показывающий, как реализуется эта концепция:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Создать провайдера с участием человека для утверждения
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Создать агента с этапом одобрения с участием человека
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Пользователь может просмотреть и одобрить ответ
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Заключение

Создание надёжных агентов ИИ требует тщательного проектирования, надёжных мер безопасности и непрерывной итерации. Внедряя структурированные системы мета-промптинга, понимая потенциальные угрозы и применяя стратегии смягчения, разработчики могут создавать агентов ИИ, которые одновременно безопасны и эффективны. Кроме того, включение подхода «человек в цикле» обеспечивает соответствие агентов ИИ потребностям пользователей при минимизации рисков. По мере развития ИИ поддержание проактивной позиции по вопросам безопасности, конфиденциальности и этики будет ключом к формированию доверия и надёжности в системах на основе ИИ.

### Есть ещё вопросы по созданию надежных агентов ИИ?

Присоединяйтесь к [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), чтобы познакомиться с другими учащимися, посетить часы консультаций и получить ответы на вопросы по вашим агентам ИИ.

## Дополнительные ресурсы

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Обзор ответственного использования ИИ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка генеративных моделей ИИ и ИИ-приложений</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системные сообщения безопасности</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон оценки рисков</a>

## Предыдущий урок

[Agentic RAG](../05-agentic-rag/README.md)

## Следующий урок

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Отказ от ответственности:
Этот документ был переведен с помощью сервиса машинного перевода Co-op Translator (https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Исходный документ на его оригинальном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или неверные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->