# Розробка сервісу Microsoft Foundry Agent

У цьому завданні ви використовуєте інструменти сервісу Microsoft Foundry Agent у [порталі Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst), щоб створити агента для бронювання рейсів. Агент зможе взаємодіяти з користувачами та надавати інформацію про рейси.

## Необхідні умови

Для виконання цього завдання вам потрібні такі речі:
1. Обліковий запис Azure з активною підпискою. [Створіть обліковий запис безкоштовно](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Вам потрібні права на створення центру Microsoft Foundry або його має створити хтось інший для вас.
    - Якщо ваша роль — Contributor або Owner, ви можете скористатися кроками цього посібника.

## Створення центру Microsoft Foundry

> **Примітка:** Раніше Microsoft Foundry називався Azure AI Studio.

1. Дотримуйтесь цих вказівок із [статті Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) для створення центру Microsoft Foundry.
2. Коли ваш проєкт буде створено, закрийте всі відображувані підказки та перегляньте сторінку проєкту в порталі Microsoft Foundry, яка має виглядати приблизно так:

    ![Microsoft Foundry Project](../../../translated_images/uk/azure-ai-foundry.88d0c35298348c2f.webp)

## Розгортання моделі

1. У панелі зліва для вашого проєкту в розділі **My assets** виберіть сторінку **Models + endpoints**.
2. На сторінці **Models + endpoints** на вкладці **Model deployments** у меню **+ Deploy model** оберіть **Deploy base model**.
3. Знайдіть у списку модель `gpt-5-mini`, виберіть її та підтвердіть.

    > **Примітка**: Зменшення TPM допомагає уникнути надмірного використання квоти у вашій підписці.

    ![Model Deployed](../../../translated_images/uk/model-deployment.3749c53fb81e18fd.webp)

## Створення агента

Тепер, коли ви розгорнули модель, можете створити агента. Агент — це розмовна модель ШІ, яка може взаємодіяти з користувачами.

1. У панелі зліва для вашого проєкту, у розділі **Build & Customize** виберіть сторінку **Agents**.
2. Натисніть **+ Create agent** для створення нового агента. У діалоговому вікні **Agent Setup**:
    - Введіть ім’я для агента, наприклад `FlightAgent`.
    - Переконайтеся, що вибрано розгортання моделі `gpt-5-mini`, яке ви створили раніше.
    - Встановіть **Інструкції** згідно з підказкою, якої агент має дотримуватися. Ось приклад:
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
> Для детальнішої підказки можна ознайомитися з [цим репозиторієм](https://github.com/ShivamGoyal03/RoamMind).
    
> Крім того, ви можете додати **Knowledge Base** та **Actions**, щоб розширити можливості агента для надання додаткової інформації та виконання автоматичних завдань за запитами користувачів. У цьому завданні ці кроки можна пропустити.
    
![Agent Setup](../../../translated_images/uk/agent-setup.9bbb8755bf5df672.webp)

3. Щоб створити нового мульти-ШІ агента, просто натисніть **New Agent**. Новостворений агент відобразиться на сторінці Agents.


## Тестування агента

Після створення агента ви можете перевірити, як він відповідає на запити користувачів у середовищі порталу Microsoft Foundry.

1. У верхній частині панелі **Setup** для вашого агента виберіть **Try in playground**.
2. У панелі **Playground** ви можете взаємодіяти з агентом, вводячи запити в чаті. Наприклад, попросіть агента знайти рейси з Сіетла до Нью-Йорка на 28 число.

    > **Примітка**: Агент може не надавати точних відповідей, оскільки в цьому завданні не використовується реальних даних у режимі реального часу. Мета — протестувати здатність агента розуміти і відповідати на запити користувачів відповідно до заданих інструкцій.

    ![Agent Playground](../../../translated_images/uk/agent-playground.dc146586de715010.webp)

3. Після тестування агента ви можете додатково налаштувати його, додавши більше інтенцій, навчальні дані та дії для розширення його можливостей.

## Видалення ресурсів

Коли ви закінчите тестування агента, видаліть його, щоб уникнути додаткових витрат.
1. Відкрийте [Azure портал](https://portal.azure.com) і перегляньте вміст групи ресурсів, де розгорнули ресурси центру, які використовували в цьому завданні.
2. На панелі інструментів виберіть **Delete resource group**.
3. Введіть назву групи ресурсів і підтвердіть її видалення.

## Ресурси

- [Документація Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Портал Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Початок роботи з Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Основи AI агентів на Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->