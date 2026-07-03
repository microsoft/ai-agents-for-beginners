[![Надеждни AI агенти](../../../translated_images/bg/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Кликнете върху изображението по-горе, за да гледате видео на този урок)_

# Създаване на надеждни AI агенти

## Въведение

Този урок ще разгледа:

- Как да изградим и внедрим безопасни и ефективни AI агенти
- Важни съображения за сигурност при разработването на AI агенти.
- Как да поддържаме поверителността на данните и потребителите при разработването на AI агенти.

## Учебни цели

След завършване на този урок ще можете да:

- Идентифицирате и смекчавате рисковете при създаването на AI агенти.
- Прилагате мерки за сигурност, за да гарантирате правилното управление на данните и достъпа.
- Създавате AI агенти, които поддържат поверителността на данните и осигуряват качествен потребителски опит.

## Безопасност

Нека първо разгледаме създаването на безопасни агентни приложения. Безопасността означава, че AI агентът изпълнява както е проектиран. Като създатели на агентни приложения, разполагаме с методи и инструменти за максимизиране на безопасността:

### Изграждане на рамка за системно съобщение

Ако някога сте изграждали AI приложение с големи езикови модели (LLMs), знаете колко е важно да се проектира стабилен системен промпт или системно съобщение. Тези промпти установяват мета правилата, инструкциите и насоките за това как LLM ще взаимодейства с потребителя и данните.

За AI агенти системният промпт е още по-важен, тъй като AI агентите ще имат нужда от много специфични инструкции, за да изпълнят задачите, които сме ги проектирали да изпълняват.

За да създадем мащабируеми системни промпти, можем да използваме рамка за системно съобщение за изграждане на един или повече агенти в нашето приложение:

![Изграждане на рамка за системно съобщение](../../../translated_images/bg/system-message-framework.3a97368c92d11d68.webp)

#### Стъпка 1: Създаване на мета системно съобщение

Мета промптът ще бъде използван от LLM за генериране на системните промпти за агентите, които създаваме. Проектираме го като шаблон, за да можем ефективно да създаваме множество агенти, ако е необходимо.

Ето пример за мета системно съобщение, което бихме дали на LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Стъпка 2: Създаване на основен промпт

Следващата стъпка е да се създаде основен промпт, описващ AI агента. Трябва да включите ролята на агента, задачите, които агентът ще изпълнява, както и други отговорности, които има агентът.

Ето пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Стъпка 3: Предоставяне на основно системно съобщение на LLM

Сега можем да оптимизираме това системно съобщение, като предоставим мета системното съобщение като системно съобщение заедно с нашето основно системно съобщение.

Това ще създаде системно съобщение, което е по-добре проектирано за насочване на нашите AI агенти:

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

#### Стъпка 4: Повтаряне и подобряване

Ползата от тази рамка за системни съобщения е способността да се мащабира създаването на системни съобщения от множество агенти по-лесно, както и да се подобряват системните съобщения с течение на времето. Рядко се случва първото системно съобщение да е напълно подходящо за вашия цялостен случай на употреба. Възможността да правите малки корекции и подобрения, като променяте основното системно съобщение и го подлагате на системата, ви позволява да сравнявате и оценявате резултатите.

## Разбиране на заплахите

За да изградите надеждни AI агенти, е важно да разберете и смекчите рисковете и заплахите за вашия AI агент. Нека разгледаме някои от различните заплахи към AI агентите и как може по-добре да планирате и подготвите за тях.

![Разбиране на заплахите](../../../translated_images/bg/understanding-threats.89edeada8a97fc0f.webp)

### Задачи и инструкции

**Описание:** Атакуващи се опитват да променят инструкциите или целите на AI агента чрез промптиране или манипулиране на входните данни.

**Смекчаване**: Извършвайте проверки за валидност и филтриране на входните данни, за да откриете потенциално опасни промпти преди те да бъдат обработени от AI агента. Тъй като тези атаки обикновено изискват чест интеракционен контакт с агента, ограничаването на броя разговорни ходове е друг начин да се предотвратят тези типове атаки.

### Достъп до критични системи

**Описание:** Ако AI агент има достъп до системи и услуги, които съхраняват чувствителни данни, атакуващите могат да компрометират комуникацията между агента и тези услуги. Това могат да бъдат директни атаки или индиректни опити за получаване на информация за тези системи чрез агента.

**Смекчаване:** AI агентите трябва да имат достъп до системи само на база необходимост, за да се предотвратят тези типове атаки. Комуникацията между агента и системата също трябва да бъде защитена. Прилагането на автентикация и контрол на достъпа е друг начин да защитите тази информация.

### Претоварване на ресурси и услуги

**Описание:** AI агентите имат достъп до различни инструменти и услуги за изпълнение на задачи. Атакуващите могат да използват тази възможност да атакуват тези услуги чрез изпращане на голям обем заявки през AI агента, което може да доведе до повреди на системата или високи разходи.

**Смекчаване:** Внедрете политики за ограничаване на броя на заявките, които един AI агент може да направи към услуга. Ограничаването на броя на ходовете в разговора и заявките към вашия AI агент е друг начин да се предотвратят тези типове атаки.

### Отравяне на база знания

**Описание:** Този тип атака не е насочена директно към AI агента, а към базата знания и други услуги, които AI агентът ще използва. Това може да включва корумпиране на данните или информацията, която AI агентът ще използва при изпълнение на задача, водещо до пристрастни или нежелани отговори към потребителя.

**Смекчаване:** Извършвайте редовна проверка на данните, с които AI агентът работи в своите работни процеси. Осигурете, че достъпът до тези данни е защитен и може да се променя само от доверени лица, за да избегнете този тип атака.

### Каскадни грешки

**Описание:** AI агентите използват различни инструменти и услуги за изпълнение на задачи. Грешки, причинени от атакуващи, могат да доведат до повреди на други свързани системи, което прави атаката по-разпространена и по-трудна за диагностициране.

**Смекчаване:** Един от методите за избягване на това е AI агентът да работи в ограничена среда, като например изпълняване на задачи в Docker контейнер, за да се предотвратят директни системни атаки. Създаването на резервни механизми и логика за повторен опит при системни грешки е друг начин за предотвратяване на по-големи системни повреди.

## Човек в цикъла

Друг ефективен начин за създаване на надеждни системи с AI агенти е използването на човек в цикъла. Това създава поток, при който потребителите могат да подават обратна връзка към агентите по време на работа. Потребителите всъщност действа като агенти в мултиагентна система, предоставяйки одобрение или прекъсване на текущия процес.

![Човек в цикъла](../../../translated_images/bg/human-in-the-loop.5f0068a678f62f4f.webp)

Ето примерен код, използващ Microsoft Agent Framework, който показва как този концепт се прилага:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Създайте доставчика с одобрение от човек в цикъла
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Създайте агента с етап за одобрение от човек
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Потребителят може да преглежда и одобрява отговора
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Заключение

Създаването на надеждни AI агенти изисква внимателен дизайн, стабилни мерки за сигурност и непрекъснато усъвършенстване. Чрез прилагане на структуриран мета промптинг, разбиране на потенциалните заплахи и използване на стратегии за смекчаване, разработчиците могат да създадат AI агенти, които са и безопасни, и ефективни. Освен това, интегрирането на подход с човек в цикъла гарантира, че AI агентите остават съобразени с нуждите на потребителя и минимизират рисковете. С напредъка на AI, поддържането на проактивна позиция по отношение на сигурността, поверителността и етичните аспекти ще бъде ключово за изграждане на доверие и надеждност в системите, базирани на AI.

## Примери с код

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Демонстрация стъпка по стъпка на системата за мета промпти.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Одобрителни врати преди действие, класиране на рискове и водене на одитен журнал за надеждни агенти.

### Имате ли още въпроси относно създаването на надеждни AI агенти?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнете с други изучаващи, да посетите офис часове и да получите отговори на вашите въпроси за AI агенти.

## Допълнителни ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Преглед на отговорното използване на AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка на модели за генеративен AI и AI приложения</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системни съобщения за безопасност</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон за оценка на рискове</a>

## Предишен урок

[Agentic RAG](../05-agentic-rag/README.md)

## Следващ урок

[Дизайнерски шаблон за планиране](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->