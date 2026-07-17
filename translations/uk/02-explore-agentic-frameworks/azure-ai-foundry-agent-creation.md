# Розробка сервісу агента Microsoft Foundry

У цьому завданні ви використовуєте інструменти сервісу агента Microsoft Foundry у [порталі Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst), щоб створити агента для бронювання рейсів. Агент зможе взаємодіяти з користувачами та надавати інформацію про рейси.

## Передумови

Щоб виконати це завдання, вам потрібно:
1. Обліковий запис Azure з активною підпискою. [Створіть обліковий запис безкоштовно](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Потрібні дозволи для створення хабу Microsoft Foundry або його наявність.
    - Якщо ваша роль Учасник або Власник, ви можете виконати кроки цього посібника.

## Створення хабу Microsoft Foundry

> **Примітка:** Раніше Microsoft Foundry мала назву Azure AI Studio.

1. Дотримуйтесь інструкцій із допису в блозі [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) щодо створення хабу Microsoft Foundry.
2. Після створення проєкту закрийте всі підказки та перегляньте сторінку проєкту в порталі Microsoft Foundry, яка має виглядати приблизно так:

    ![Microsoft Foundry Project](../../../translated_images/uk/azure-ai-foundry.88d0c35298348c2f.webp)

## Розгортання моделі

1. У панелі зліва для вашого проєкту в розділі **Мої активи** виберіть сторінку **Моделі + кінцеві точки**.
2. На сторінці **Моделі + кінцеві точки** на вкладці **Розгортання моделей** у меню **+ Розгорнути модель** виберіть **Розгорнути базову модель**.
3. Знайдіть модель `gpt-4.1-mini` у списку, виберіть її та підтвердіть.

    > **Примітка**: Зменшення TPM допомагає уникнути надмірного використання квоти, доступної у підписці, яку ви використовуєте.

    ![Model Deployed](../../../translated_images/uk/model-deployment.3749c53fb81e18fd.webp)

## Створення агента

Тепер, коли модель розгорнута, ви можете створити агента. Агент — це модель розмовного штучного інтелекту, яка використовується для взаємодії з користувачами.

1. У панелі зліва для вашого проєкту в розділі **Створити й налаштувати** виберіть сторінку **Агенти**.
2. Натисніть **+ Створити агента** для створення нового агента. У діалоговому вікні **Налаштування агента**:
    - Введіть ім’я агента, наприклад `FlightAgent`.
    - Переконайтеся, що вибрано розгортання моделі `gpt-4.1-mini`, створене раніше.
    - Встановіть **Інструкції** відповідно до запиту, якому має слідувати агент. Ось приклад:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> Для детальнішого запиту ви можете переглянути [цей репозиторій](https://github.com/ShivamGoyal03/RoamMind) для отримання додаткової інформації.
    
> Крім того, ви можете додати **Базу знань** та **Дії**, щоб розширити можливості агента надавати більше інформації та виконувати автоматизовані завдання на основі запитів користувачів. У цьому завданні ці кроки можна пропустити.
    
![Agent Setup](../../../translated_images/uk/agent-setup.9bbb8755bf5df672.webp)

3. Щоб створити нового багатокомпонентного агента, просто натисніть **Новий агент**. Новостворений агент відобразиться на сторінці агентів.


## Тестування агента

Після створення агента ви можете протестувати його, щоб побачити, як він відповідає на запити користувачів у середовищі Microsoft Foundry portal playground.

1. У верхній частині панелі **Налаштування** для вашого агента виберіть **Спробувати у середовищі playground**.
2. У панелі **Playground** ви можете спілкуватися з агентом, вводячи запити у вікні чату. Наприклад, ви можете попросити агента знайти рейси з Сіетла до Нью-Йорка на 28 число.

    > **Примітка**: Агент може не надавати точних відповідей, оскільки в цьому завданні не використовується актуальна інформація в реальному часі. Мета – перевірити здатність агента розуміти та відповідати на запити користувачів на основі наданих інструкцій.

    ![Agent Playground](../../../translated_images/uk/agent-playground.dc146586de715010.webp)

3. Після тестування агента ви можете додатково налаштувати його, додавши більше намірів, навчальних даних і дій для розширення його можливостей.

## Видалення ресурсів

Коли ви закінчите тестування агента, ви можете видалити його, щоб уникнути додаткових витрат.
1. Відкрийте [Azure portal](https://portal.azure.com) та перегляньте вміст групи ресурсів, де розгорнуті ресурси хабу, які використовувалися в цьому завданні.
2. На панелі інструментів виберіть **Видалити групу ресурсів**.
3. Введіть ім’я групи ресурсів і підтвердіть видалення.

## Ресурси

- [Документація Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Портал Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Початок роботи з Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Основи агентів ШІ на Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->