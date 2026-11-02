[![Доверени AI агенти](../../../translated_images/bg/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

# Създаване на доверени AI агенти

## Въведение

Този урок ще покрие:

- Как да създадем и внедрим безопасни и ефективни AI агенти
- Важни съображения за сигурността при разработка на AI агенти.
- Как да поддържаме поверителност на данните и потребителите при разработка на AI агенти.

## Учебни цели

След завършване на този урок, ще знаете как да:

- Идентифицирате и намалявате рисковете при създаване на AI агенти.
- Изпълнявате мерки за сигурност, за да гарантирате правилно управление на данните и достъпа.
- Създавате AI агенти, които поддържат поверителност на данните и осигуряват качествен потребителски опит.

## Безопасност

Нека първо разгледаме създаването на безопасни агенционни приложения. Безопасността означава, че AI агентът функционира според предназначението си. Като създатели на агенционни приложения, разполагаме с методи и инструменти за максимизиране на безопасността:

### Създаване на рамка за системно съобщение

Ако някога сте създавали AI приложение, използвайки големи езикови модели (LLMs), знаете колко е важно да се проектира здравословен системен промпт или системно съобщение. Тези промпти определят мета правилата, инструкциите и насоките за това как LLM ще взаимодейства с потребителя и с данните.

При AI агенти системният промпт е още по-важен, тъй като AI агентите ще се нуждаят от много конкретни инструкции, за да изпълнят задачите, които сме проектирали за тях.

За да създадем мащабируеми системни промпти, можем да използваме рамка за системно съобщение за изграждане на един или повече агенти в нашето приложение:

![Създаване на рамка за системно съобщение](../../../translated_images/bg/system-message-framework.3a97368c92d11d68.webp)

#### Стъпка 1: Създайте мета системно съобщение

Мета промптът ще се използва от LLM, за да генерира системните промпти за агентите, които създаваме. Проектираме го като шаблон, за да можем ефективно да създаваме множество агенти, ако е необходимо.

Ето пример за мета системно съобщение, което бихме дали на LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Стъпка 2: Създайте основен промпт

Следващата стъпка е да създадете основен промпт, който описва AI агента. Трябва да включите ролята на агента, задачите, които агентът ще изпълнява, и всички други отговорности на агента.

Ето пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Стъпка 3: Предоставяне на основно системно съобщение на LLM

Сега можем да оптимизираме това системно съобщение като предоставим мета системното съобщение като системно съобщение и нашето основно системно съобщение.

Това ще произведе системно съобщение, което е по-добре проектирано за насочване на нашите AI агенти:

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

#### Стъпка 4: Итерация и подобрение

Ценността на тази рамка за системни съобщения е възможността за мащабиране на създаването на системни съобщения за множество агенти по-лесно, както и подобряване на вашите системни съобщения с течение на времето. Рядко ще имате системно съобщение, което работи от първия път за вашия цялостен случай на употреба. Възможността за малки корекции и подобрения чрез промяна на основното системно съобщение и изпълнението му през системата ще ви позволи да сравнявате и оценявате резултатите.

## Разбиране на заплахите

За да създадем доверени AI агенти, е важно да разберем и намалим рисковете и заплахите за вашия AI агент. Нека разгледаме само някои от различните заплахи към AI агенти и как да планирате и подготвите по-добре за тях.

![Разбиране на заплахите](../../../translated_images/bg/understanding-threats.89edeada8a97fc0f.webp)

### Задача и инструкция

**Описание:** Нападатели се опитват да променят инструкциите или целите на AI агента чрез промптиране или манипулиране на входните данни.

**Намаляване на риска**: Изпълнявайте валидационни проверки и филтри за входните данни, за да откриете потенциално опасни промпти преди те да бъдат обработени от AI агента. Тъй като тези атаки обикновено изискват честа интеракция с агента, ограничаването на броя ходове в разговора е друг начин за предотвратяване на този тип атаки.

### Достъп до критични системи

**Описание:** Ако AI агентът има достъп до системи и услуги, които съхраняват чувствителни данни, нападатели могат да компрометират комуникацията между агента и тези услуги. Това може да са директни атаки или непреки опити за получаване на информация за тези системи чрез агента.

**Намаляване на риска:** AI агентите трябва да имат достъп до системите само когато е необходимо, за да се предотвратят тези типове атаки. Комуникацията между агента и системата също трябва да бъде сигурна. Прилагането на автентикация и контрол на достъпа е друг начин за защита на тази информация.

### Претоварване на ресурси и услуги

**Описание:** AI агентите могат да имат достъп до различни инструменти и услуги за изпълнение на задачи. Нападатели могат да използват тази възможност за атака на тези услуги чрез изпращане на голям обем заявки чрез AI агента, което може да доведе до системни сривове или високи разходи.

**Намаляване на риска:** Прилагайте политики за ограничаване на броя на заявките, които AI агент може да прави към дадена услуга. Ограничаването на броя ходове в разговора и заявките към вашия AI агент е друг начин за предотвратяване на този тип атаки.

### Отравяне на базата от знания

**Описание:** Този тип атака не е насочен директно към AI агента, а към базата от знания и други услуги, които AI агентът ще използва. Това може да включва коруптиране на данните или информацията, които AI агентът използва за изпълнение на дадена задача, водещо до пристрастни или нежелани отговори към потребителя.

**Намаляване на риска:** Извършвайте редовна проверка на данните, които AI агентът ще използва в своите работни потоци. Осигурете сигурен достъп до тези данни и те да се променят само от доверени лица, за да се избегне този тип атака.

### Каскадни грешки

**Описание:** AI агентите имат достъп до различни инструменти и услуги за изпълнение на задачи. Грешки, причинени от нападатели, могат да доведат до повреди в други системи, към които AI агентът е свързан, което прави атаката по-широко разпространена и трудно проследима.

**Намаляване на риска:** Един метод за избягване на това е AI агентът да работи в ограничена среда, като изпълнява задачи в Docker контейнер, за да се предотвратят директни атаки върху системата. Създаването на резервни механизми и логика за повторно изпълнение, когато определени системи отговарят с грешка, е друг начин за предотвратяване на по-големи системни повреди.

## Човек в цикъла

Друг ефективен начин за създаване на доверени AI агентски системи е използването на човек в цикъла. Това създава поток, в който потребителите могат да предоставят обратна връзка на агентите по време на изпълнение. Потребителите по същество действат като агенти в мултиагентска система и чрез одобрение или прекратяване на изпълнявания процес.

![Човек в цикъла](../../../translated_images/bg/human-in-the-loop.5f0068a678f62f4f.webp)

Ето откъс от код, използващ Microsoft Agent Framework, който показва как се реализира тази концепция:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Създайте доставчика с одобрение от човек в цикъла
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Създайте агента с етап за одобрение от човек
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

Създаването на доверени AI агенти изисква внимателно проектиране, здрави мерки за сигурност и непрекъснато усъвършенстване. Като прилагате структурирани мета-промпт системи, разбирате потенциалните заплахи и прилагате стратегии за намаляване, разработчиците могат да създадат AI агенти, които са както безопасни, така и ефективни. Освен това включването на подход човек в цикъла гарантира, че AI агентите остават съобразени с нуждите на потребителите, като същевременно минимизират рисковете. В ерата на непрекъснатото развитие на AI, поддържането на проактивна позиция по отношение на сигурността, поверителността и етичните съображения ще бъде ключово за насърчаването на доверие и надеждност в AI-базирани системи.

## Примери с код

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Демонстрация стъпка по стъпка на рамката за мета промпт системно съобщение.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Портали за предварително одобрение на действия, категоризация на рисковете и регистриране на одити за доверени агенти.

### Имате още въпроси относно създаването на доверени AI агенти?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнете с други обучаващи се, да посещавате офис часове и да получите отговори на вашите въпроси за AI агенти.

## Допълнителни ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Преглед на отговорното използване на AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка на генеративни AI модели и AI приложения</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системни съобщения за безопасност</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон за оценка на риска</a>

## Предишен урок

[Agentic RAG](../05-agentic-rag/README.md)

## Следващ урок

[Патерн за планиране и дизайн](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->