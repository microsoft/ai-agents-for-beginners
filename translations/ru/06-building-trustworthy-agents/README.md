[![Доверенные ИИ-Агенты](../../../translated_images/ru/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Создание доверенных ИИ-агентов

## Введение

В этом уроке будут рассмотрены:

- Как создавать и развертывать безопасных и эффективных ИИ-агентов
- Важные аспекты безопасности при разработке ИИ-агентов.
- Как обеспечивать конфиденциальность данных и пользователей при разработке ИИ-агентов.

## Цели обучения

После прохождения этого урока вы узнаете, как:

- Опознавать и снижать риски при создании ИИ-агентов.
- Внедрять меры безопасности для правильного управления данными и доступом.
- Создавать ИИ-агентов, которые сохраняют конфиденциальность данных и обеспечивают качественный пользовательский опыт.

## Безопасность

Для начала рассмотрим создание безопасных агентных приложений. Безопасность означает, что ИИ-агент работает так, как задумано. В качестве разработчиков агентных приложений у нас есть методы и инструменты для максимизации безопасности:

### Создание системы сообщений

Если вы когда-либо создавали ИИ-приложение с использованием больших языковых моделей (LLM), вы знаете важность проектирования надежного системного запроса или системного сообщения. Эти запросы устанавливают мета-правила, инструкции и руководства для взаимодействия LLM с пользователем и данными.

Для ИИ-агентов системный запрос еще важнее, поскольку агенты ИИ нуждаются в очень конкретных инструкциях для выполнения задач, которые мы для них разработали.

Для создания масштабируемых системных запросов мы можем использовать структуру системных сообщений для построения одного или нескольких агентов в нашем приложении:

![Создание системы сообщений](../../../translated_images/ru/system-message-framework.3a97368c92d11d68.webp)

#### Шаг 1: Создайте мета-системное сообщение

Мета-запрос будет использоваться LLM для генерации системных запросов для создаваемых нами агентов. Мы проектируем его как шаблон, чтобы эффективно создавать несколько агентов при необходимости.

Вот пример мета-системного сообщения, которое мы дадим LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Шаг 2: Создайте базовый запрос

Следующий шаг — создать базовый запрос для описания ИИ-агента. Включите роль агента, задачи, которые агент выполнит, а также любые другие обязанности агента.

Вот пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Шаг 3: Передайте базовое системное сообщение LLM

Теперь мы можем оптимизировать это системное сообщение, предоставив мета-системное сообщение в качестве системного сообщения и наше базовое системное сообщение.

Это создаст системное сообщение, лучше предназначенное для управления нашими ИИ-агентами:

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

Ценность этой системы сообщений заключается в возможности легко масштабировать создание системных сообщений для нескольких агентов, а также совершенствовать ваши системные сообщения со временем. Редко бывает так, что системное сообщение срабатывает идеально с первого раза для вашего полного варианта использования. Возможность вносить небольшие изменения и улучшения, изменяя базовое системное сообщение и запускаю его через систему, позволит вам сравнивать и оценивать результаты.

## Понимание угроз

Чтобы создавать доверенных ИИ-агентов, важно понимать и снижать риски и угрозы для вашего ИИ-агента. Рассмотрим некоторые из различных угроз ИИ-агентам и способы их планирования и подготовки.

![Понимание угроз](../../../translated_images/ru/understanding-threats.89edeada8a97fc0f.webp)

### Задача и инструкция

**Описание:** Злоумышленники пытаются изменить инструкции или цели ИИ-агента через запросы или манипулирование входными данными.

**Смягчение:** Выполняйте проверки валидации и фильтры входных данных, чтобы обнаружить потенциально опасные запросы до их обработки ИИ-агентом. Поскольку эти атаки обычно требуют частого взаимодействия с Агентом, ограничение количества раундов в разговоре — еще один способ предотвратить такие атаки.

### Доступ к критическим системам

**Описание:** Если ИИ-агент имеет доступ к системам и сервисам, которые хранят чувствительные данные, злоумышленники могут скомпрометировать связь между агентом и этими сервисами. Это могут быть прямые атаки или косвенные попытки получить информацию о системах через агента.

**Смягчение:** ИИ-агенты должны иметь доступ к системам только по необходимости, чтобы предотвратить такие атаки. Связь между агентом и системой также должна быть защищена. Внедрение аутентификации и контроля доступа — еще один способ защиты информации.

### Перегрузка ресурсов и сервисов

**Описание:** ИИ-агенты могут использовать различные инструменты и сервисы для выполнения задач. Злоумышленники могут использовать это, чтобы атаковать сервисы, отправляя высокий объем запросов через ИИ-агента, что может привести к сбоям системы или высоким затратам.

**Смягчение:** Внедрите политики ограничения количества запросов, которые ИИ-агент может отправлять сервису. Ограничение количества раундов разговоров и запросов к вашему ИИ-агенту — еще один способ предотвратить такие атаки.

### Отравление базы знаний

**Описание:** Этот тип атаки не направлен непосредственно на ИИ-агента, а на базу знаний и другие сервисы, которые использует ИИ-агент. Это может включать повреждение данных или информации, которую агент будет использовать для выполнения задачи, что приведет к предвзятым или нежелательным ответам пользователю.

**Смягчение:** Регулярно проверяйте данные, которые ИИ-агент будет использовать в своих рабочих процессах. Обеспечьте безопасный доступ к этим данным и возможность изменений только для доверенных лиц, чтобы избежать такого рода атак.

### Каскадные ошибки

**Описание:** ИИ-агенты используют различные инструменты и сервисы для выполнения задач. Ошибки, вызванные злоумышленниками, могут привести к сбоям в других системах, к которым подключен ИИ-агент, что делает атаку более масштабной и сложной для устранения.

**Смягчение:** Один из способов избежать этого — заставить ИИ-агента работать в ограниченной среде, например, выполнять задачи в Docker-контейнере, чтобы предотвратить прямые атаки на систему. Создание механизмов резервного копирования и логики повторных попыток при ошибках в ответах систем — еще один способ предотвратить более масштабные сбои.

## Человек в цикле

Еще один эффективный способ создать доверенные системы ИИ-агентов — использование человека в цикле. Это создает поток, в котором пользователи могут предоставлять обратную связь агентам во время работы. Пользователи фактически выступают агентами в мультиагентной системе и могут одобрять или завершать выполняющийся процесс.

![Человек в цикле](../../../translated_images/ru/human-in-the-loop.5f0068a678f62f4f.webp)

Вот фрагмент кода с использованием Microsoft Agent Framework, демонстрирующий реализацию этой концепции:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Создайте провайдера с утверждением человеком в процессе
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Создайте агента с этапом одобрения человеком
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

Создание доверенных ИИ-агентов требует тщательного проектирования, надежных мер безопасности и постоянной итерации. Внедряя структурированные системы мета-промптов, понимая потенциальные угрозы и применяя стратегии смягчения, разработчики могут создавать ИИ-агентов, которые одновременно безопасны и эффективны. Кроме того, включение подхода «человек в цикле» обеспечивает сохранение соответствия ИИ-агентов потребностям пользователей при минимизации рисков. По мере развития ИИ ключевым фактором для укрепления доверия и надежности в системах на базе ИИ будет проактивный подход к безопасности, конфиденциальности и этическим аспектам.

## Примеры кода

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Пошаговая демонстрация системы мета-промптов для системных сообщений.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Ворота предварительного одобрения действий, ранжирование рисков и ведение аудита для доверенных агентов.

### Остались вопросы по созданию доверенных ИИ-агентов?

Присоединяйтесь к [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), чтобы познакомиться с другими учениками, посещать часы консультаций и получать ответы на вопросы по ИИ-агентам.

## Дополнительные ресурсы

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Обзор ответственного использования ИИ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка моделей генеративного ИИ и приложений ИИ</a>
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