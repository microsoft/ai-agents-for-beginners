[![Доверени AI агенти](../../../translated_images/bg/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

# Създаване на доверени AI агенти

## Въведение

Този урок ще обхване:

- Как да изградим и внедрим безопасни и ефективни AI агенти
- Важни съображения за сигурност при разработването на AI агенти.
- Как да поддържаме поверителност на данните и на потребителите при разработване на AI агенти.

## Учебни цели

След приключване на този урок, ще знаете как да:

- Идентифицирате и намалявате рисковете при създаването на AI агенти.
- Прилагате мерки за сигурност, за да осигурите правилното управление на данните и достъпа.
- Създавате AI агенти, които поддържат поверителност на данните и осигуряват качествено потребителско изживяване.

## Безопасност

Нека първо разгледаме изграждането на безопасни агентни приложения. Безопасността означава, че AI агентът изпълнява задачите си според предназначението. Като създатели на агентни приложения, разполагаме с методи и инструменти за максимизиране на безопасността:

### Изграждане на рамка за системни съобщения

Ако някога сте изграждали AI приложение с помощта на големи езикови модели (LLMs), знаете колко е важно да се проектира здрава системна подсказка или системно съобщение. Тези подсказки установяват мета правилата, инструкциите и насоките за това как LLM ще взаимодейства с потребителя и данните.

За AI агенти, системната подсказка е още по-важна, тъй като AI агентите се нуждаят от много конкретни инструкции, за да изпълнят задачите, които сме проектирали за тях.

За да създадем мащабируеми системни подсказки, можем да използваме рамка за системни съобщения за изграждането на един или повече агенти в нашето приложение:

![Изграждане на рамка за системни съобщения](../../../translated_images/bg/system-message-framework.3a97368c92d11d68.webp)

#### Стъпка 1: Създайте мета системно съобщение

Мета подсказката ще бъде използвана от LLM за генериране на системни подсказки за агенти, които създаваме. Проектираме я като шаблон, за да можем ефективно да създаваме множество агенти при необходимост.

Ето пример за мета системно съобщение, което бихме дали на LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Стъпка 2: Създайте основна подсказка

Следващата стъпка е да създадете основна подсказка, която описва AI агента. Трябва да включите ролята на агента, задачите, които агентът ще изпълнява, и всякакви други отговорности на агента.

Ето пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Стъпка 3: Представяне на основното системно съобщение на LLM

Сега можем да оптимизираме това системно съобщение, като предоставим мета системното съобщение като системно съобщение и нашето основно системно съобщение.

Това ще произведе системно съобщение, което е по-добре проектирано да насочва нашите AI агенти:

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

#### Стъпка 4: Повтаряйте и усъвършенствайте

Ценността на тази рамка за системни съобщения е възможността по-лесно да се мащабира създаването на системни съобщения за множество агенти, както и да се подобряват системните съобщения с времето. Рядко ще имате системно съобщение, което работи перфектно от първия път за вашия пълен случай на употреба. Възможността да правите малки корекции и подобрения чрез промяна на основното системно съобщение и пускане през системата ще ви позволи да сравнявате и оценявате резултатите.

## Разбиране на заплахите

За да изградите доверени AI агенти, е важно да разберете и намалите рисковете и заплахите, свързани с вашия AI агент. Нека разгледаме само някои от различните заплахи за AI агенти и как можете по-добре да планирате и се подготвите за тях.

![Разбиране на заплахите](../../../translated_images/bg/understanding-threats.89edeada8a97fc0f.webp)

### Задача и инструкция

**Описание:** Злонамерени лица се опитват да променят инструкциите или целите на AI агента чрез подсказки или манипулиране на входни данни.

**Намаляване:** Изпълнявайте проверки за валидност и филтри на входните данни, за да откривате потенциално опасни подсказки преди те да бъдат обработени от AI агента. Тъй като тези атаки обикновено изискват честа интеракция с агента, ограничаването на броя ходове в разговора е друг начин за предотвратяване на тези видове атаки.

### Достъп до критични системи

**Описание:** Ако AI агентът има достъп до системи и услуги, които съхраняват чувствителни данни, злонамерените лица могат да компрометират комуникацията между агента и тези услуги. Това могат да бъдат директни атаки или косвени опити да се получи информация за тези системи чрез агента.

**Намаляване:** AI агентите трябва да имат достъп до системите само при необходимост, за да се предотвратят тези видове атаки. Комуникацията между агента и системата също трябва да бъде защитена. Прилагането на автентикация и контрол на достъпа е друг начин за защита на тази информация.

### Претоварване на ресурси и услуги

**Описание:** AI агентите могат да използват различни инструменти и услуги за изпълнение на задачи. Злонамерените лица могат да използват тази възможност, за да атакуват тези услуги чрез изпращане на голям брой заявки чрез AI агента, което може да доведе до повреди на системата или високи разходи.

**Намаляване:** Прилагайте политики за ограничаване на броя заявки, които AI агент може да направи към услуга. Ограничаването на броя ходове в разговора и заявките към вашия AI агент е друг начин да се предотвратят тези видове атаки.

### Отравяне на базата с познания

**Описание:** Този вид атака не е насочена директно към AI агента, а към базата с познания и други услуги, които AI агентът ще използва. Това може да включва корумпиране на данните или информацията, които AI агентът използва за изпълнение на задача, което води до пристрастни или нежелани отговори към потребителя.

**Намаляване:** Редовно проверявайте данните, които AI агентът ще използва в своите работни процеси. Осигурете, че достъпът до тези данни е защитен и те могат да бъдат променяни само от доверени лица, за да се избегне този вид атака.

### Вериги от грешки

**Описание:** AI агентите използват различни инструменти и услуги за изпълнение на задачи. Грешки, причинени от злонамерени лица, могат да доведат до повреди на други системи, свързани с AI агента, което прави атаката по-разпространена и по-трудна за диагностициране.

**Намаляване:** Един от методите за избягване е AI агентът да работи в ограничена среда, например като изпълнява задачи в Docker контейнер, за да се предотвратят директни атаки върху системата. Създаването на резервни механизми и логика за повторен опит, когато някои системи отговарят с грешка, е друг начин за предотвратяване на по-големи повреди на системата.

## Човек в цикъла

Друг ефективен начин за изграждане на доверени AI агент системи е използването на човек в цикъла. Това създава поток, при който потребителите могат да предоставят обратна връзка на агентите по време на работа. Потребителите в същност действат като агенти в мултиагентна система, като одобряват или прекратяват текущия процес.

![Човек в цикъла](../../../translated_images/bg/human-in-the-loop.5f0068a678f62f4f.webp)

Ето кодов откъс, който използва Microsoft Agent Framework, за да покаже как е реализирана тази концепция:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Създайте доставчика с одобрение от човек в цикъла
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Създайте агента с етап на одобрение от човек
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Потребителят може да прегледа и одобри отговора
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Заключение

Създаването на доверени AI агенти изисква внимателно проектиране, здрави мерки за сигурност и непрекъснато усъвършенстване. Чрез прилагане на структурирани мета подсказки, разбиране на потенциалните заплахи и използване на стратегии за смекчаване, разработчиците могат да създадат AI агенти, които са безопасни и ефективни. Освен това включването на подход с човек в цикъла гарантира, че AI агентите остават съобразени с нуждите на потребителите, като същевременно минимизират рисковете. Докато AI продължава да се развива, поддържането на проактивна позиция по отношение на сигурността, поверителността и етичните аспекти ще бъде ключово за изграждането на доверие и надеждност в AI-системите.

### Имате още въпроси относно създаването на доверени AI агенти?

Присъединете се към [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), за да се срещнете с други обучаващи се, да посетите работни часове и да получите отговори на въпросите си за AI агенти.

## Допълнителни ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Преглед на отговорното използване на AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка на генеративни AI модели и AI приложения</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системни съобщения за безопасност</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон за оценка на риска</a>

## Предишен урок

[Agentic RAG](../05-agentic-rag/README.md)

## Следващ урок

[Проектиране на шаблон за планиране](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческия сервис [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, възникнали в резултат на използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->