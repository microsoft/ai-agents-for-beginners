[![Достоверни AI агенти](../../../translated_images/bg/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

# Създаване на достоверни AI агенти

## Въведение

Този урок ще обхване:

- Как да създадем и внедрим безопасни и ефективни AI агенти
- Важни съображения относно сигурността при разработване на AI агенти.
- Как да запазим поверителността на данните и потребителите при разработване на AI агенти.

## Цели на обучението

След завършване на този урок ще можете да:

- Идентифицирате и намалявате рисковете при създаване на AI агенти.
- Прилагате мерки за сигурност, за да осигурите правилно управление на достъпа и данните.
- Създавате AI агенти, които защитават поверителността на данните и предоставят качествен потребителски опит.

## Безопасност

Нека първо разгледаме изграждането на безопасни агентни приложения. Безопасността означава, че AI агентът действа според замисъла. Като създатели на агентни приложения, разполагаме с методи и инструменти за максимизиране на безопасността:

### Създаване на рамка за системни съобщения

Ако сте строили AI приложение с помощта на големи езикови модели (LLMs), знаете колко е важно да се създаде здрав система подканващ текст или системно съобщение. Тези подканвания установяват мета правилата, инструкциите и насоките за това как LLM ще взаимодейства с потребителя и с данните.

За AI агенти системният подканващ текст е дори по-важен, тъй като те ще се нуждаят от много специфични инструкции, за да изпълнят задачите, които сме им задали.

За да създадем мащабируеми системни подканвания, можем да използваме рамка за системни съобщения за изграждане на един или повече агенти в нашето приложение:

![Създаване на рамка за системни съобщения](../../../translated_images/bg/system-message-framework.3a97368c92d11d68.webp)

#### Стъпка 1: Създайте Мета системно съобщение

Мета подканата ще се използва от LLM, за да генерира системните подканвания за агентите, които създаваме. Проектираме я като шаблон, така че да можем ефективно да създаваме множество агенти, ако е необходимо.

Ето пример за мета системно съобщение, което бихме дали на LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Стъпка 2: Създайте основна подканваща фраза

Следващата стъпка е да създадем основна подканваща фраза, която описва AI агента. Трябва да включите ролята на агента, задачите, които ще изпълни, и всякакви други отговорности на агента.

Ето пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Стъпка 3: Предоставете Основното Системно Съобщение на LLM

Сега можем да оптимизираме това системно съобщение, като предоставим мета системното съобщение като системно съобщение и нашето основно системно съобщение.

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

#### Стъпка 4: Итерация и Подобрение

Стойността на тази рамка за системни съобщения е в това, че позволява по-лесно мащабиране при създаване на системни съобщения за множество агенти, както и подобряване на вашите системни съобщения с течение на времето. Рядко ще имате системно съобщение, което функционира перфектно от първия път за вашия цялостен случай. Възможността да правите малки настройки и подобрения чрез промяна на основното системно съобщение и изпълнението му през системата ще ви позволи да сравнявате и оценявате резултатите.

## Разбиране на заплахите

За да създадете достоверни AI агенти, е важно да разберете и намалите рисковете и заплахите за вашия AI агент. Нека разгледаме само някои от различните заплахи за AI агентите и как можете да планирате и подготвите по-добре за тях.

![Разбиране на заплахите](../../../translated_images/bg/understanding-threats.89edeada8a97fc0f.webp)

### Задача и инструкция

**Описание:** Нападатели се опитват да променят инструкциите или целите на AI агента чрез подканване или манипулиране на входни данни.

**Намаляване на риска**: Изпълнете проверки за валидност и филтриране на входните данни, за да откривате потенциално опасни подканвания преди те да бъдат обработени от AI агента. Тъй като тези атаки обикновено изискват честа интеракция с агента, ограничаването на броя на ходовете в разговора е още един начин да се предотвратят тези типове атаки.

### Достъп до критични системи

**Описание:** Ако AI агентът има достъп до системи и услуги, които съхраняват чувствителни данни, нападателите могат да компрометират комуникацията между агента и тези услуги. Това могат да бъдат директни атаки или непреки опити да се получи информация за тези системи чрез агента.

**Намаляване на риска:** AI агентите трябва да имат достъп до системи само при необходимост, за да се предотвратят тези типове атаки. Комуникацията между агента и системата също трябва да бъде сигурна. Прилагането на автентикация и контрол на достъпа е друг начин за защита на тази информация.

### Претоварване на ресурси и услуги

**Описание:** AI агентите могат да използват различни инструменти и услуги за изпълнение на задачи. Нападатели могат да използват тази способност, за да атакуват тези услуги, като изпращат голям обем заявки през AI агента, което може да доведе до повреди в системата или високи разходи.

**Намаляване на риска:** Въведете политики за ограничаване на броя на заявките, които AI агент може да изпрати към услуга. Ограничаването на броя на ходовете в разговора и заявките към AI агента е друг начин да се предотвратят тези типове атаки.

### Отравяне на базата знания

**Описание:** Този вид атака не е насочен директно към AI агента, а към базата знания и други услуги, които AI агентът ще използва. Това може да включва повреда на данните или информацията, която AI агентът използва за изпълнение на задача, водейки до пристрастни или нежелани отговори към потребителя.

**Намаляване на риска:** Извършвайте редовна проверка на данните, които AI агентът използва в своите работни потоци. Осигурете сигурен достъп до тези данни, който може да бъде променян само от доверени лица, за да избегнете този вид атака.

### Каскадни грешки

**Описание:** AI агентите осъществяват достъп до различни инструменти и услуги за изпълнение на задачи. Грешки, предизвикани от нападатели, могат да доведат до повреди в други системи, свързани с AI агента, което прави атаката по-широкообхватна и по-трудна за отстраняване.

**Намаляване на риска:** Един от методите за избягване на това е AI агентът да оперира в ограничена среда, например изпълняване на задачи в Docker контейнер, за да се предотвратят директни атаки върху системата. Създаването на резервни механизми и логика за повторение при системи, отговарящи с грешка, е друг начин за предотвратяване на по-големи системни повреди.

## Човек в цикъла (Human-in-the-Loop)

Друг ефективен начин за изграждане на достоверни AI агентни системи е използването на Човек в цикъла. Това създава процес, при който потребителите могат да дават обратна връзка на агентите по време на изпълнение. Потребителите по същество действат като агенти в мултиагентна система чрез предоставяне на одобрение или прекратяване на процеса.

![Човек в Цикъла](../../../translated_images/bg/human-in-the-loop.5f0068a678f62f4f.webp)

Ето примерен код, използващ Microsoft Agent Framework, за да покаже как се прилага тази концепция:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Създайте доставчика с одобрение от човек в цикъла
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Създайте агента с стъпка за одобрение от човек
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

Създаването на достоверни AI агенти изисква внимателен дизайн, здравословни мерки за сигурност и непрекъснати итерации. Чрез прилагането на структурирани мета подканващи системи, разбиране на потенциалните заплахи и използване на стратегии за намаляване на риска, разработчиците могат да създадат AI агенти, които са както безопасни, така и ефективни. Допълнително, интегрирането на подход с човек в цикъла гарантира, че AI агентите остават съобразени с нуждите на потребителите, като същевременно минимизират рисковете. С развитието на AI е ключово да се поддържа проактивна позиция относно сигурността, поверителността и етичните съображения за насърчаване на доверие и надеждност в AI-базирани системи.

## Примери с код

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Демонстрация стъпка по стъпка на рамката за системни съобщения с мета подканваща система.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Предварителни одобрения на действия, оценяване на рискови нива и водене на журнал за достоверни агенти.

### Имаме ли още въпроси за създаването на достоверни AI агенти?

Присъединете се към [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), за да се срещнете с други обучаващи се, да участвате в офис часове и да получите отговори на въпросите си за AI агенти.

## Допълнителни ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Обзор на отговорното използване на AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка на генеративни AI модели и AI приложения</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Съобщения за система за безопасност</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон за оценка на риска</a>

## Предходен урок

[Agentic RAG](../05-agentic-rag/README.md)

## Следващ урок

[Планов дизайн модел](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->