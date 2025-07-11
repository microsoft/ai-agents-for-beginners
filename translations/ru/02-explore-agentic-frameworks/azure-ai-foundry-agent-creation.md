<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7e92870dc0843e13d4dabc620c09d2d9",
  "translation_date": "2025-07-11T14:28:14+00:00",
  "source_file": "02-explore-agentic-frameworks/azure-ai-foundry-agent-creation.md",
  "language_code": "ru"
}
-->
# Разработка сервиса Azure AI Agent

В этом упражнении вы используете инструменты сервиса Azure AI Agent в [портале Azure AI Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) для создания агента по бронированию авиабилетов. Агент сможет взаимодействовать с пользователями и предоставлять информацию о рейсах.

## Предварительные требования

Для выполнения этого упражнения вам потребуется следующее:
1. Учетная запись Azure с активной подпиской. [Создайте учетную запись бесплатно](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Вам нужны разрешения для создания хаба Azure AI Foundry или чтобы его создали для вас.
    - Если ваша роль - Contributor или Owner, вы можете следовать шагам в этом руководстве.

## Создание хаба Azure AI Foundry

> **Примечание:** Ранее Azure AI Foundry был известен как Azure AI Studio.

1. Следуйте этим рекомендациям из [блога Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) для создания хаба Azure AI Foundry.
2. Когда ваш проект будет создан, закройте все отображаемые советы и просмотрите страницу проекта в портале Azure AI Foundry, которая должна выглядеть примерно так:

    ![Проект Azure AI Foundry](../../../02-explore-agentic-frameworks/images/azure-ai-foundry.png)

## Развертывание модели

1. В левой панели вашего проекта в разделе **Мои активы** выберите страницу **Модели + конечные точки**.
2. На странице **Модели + конечные точки**, на вкладке **Развертывания моделей**, в меню **+ Развернуть модель**, выберите **Развернуть базовую модель**.
3. Найдите модель `gpt-4o-mini` в списке, затем выберите и подтвердите её.

    > **Примечание**: Снижение TPM помогает избежать чрезмерного использования квоты, доступной в вашей подписке.

    ![Модель развернута](../../../02-explore-agentic-frameworks/images/model-deployment.png)

## Создание агента

Теперь, когда вы развернули модель, вы можете создать агента. Агент - это модель разговорного ИИ, которая может использоваться для взаимодействия с пользователями.

1. В левой панели вашего проекта в разделе **Создание и настройка** выберите страницу **Агенты**.
2. Нажмите **+ Создать агента**, чтобы создать нового агента. В диалоговом окне **Настройка агента**:
    - Введите имя для агента, например, `FlightAgent`.
    - Убедитесь, что выбрано развертывание модели `gpt-4o-mini`, которое вы создали ранее.
    - Установите **Инструкции** в соответствии с подсказкой, которую вы хотите, чтобы агент следовал. Вот пример:
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
> Для подробной подсказки вы можете ознакомиться с [этим репозиторием](https://github.com/ShivamGoyal03/RoamMind) для получения дополнительной информации.
    
> Кроме того, вы можете добавить **Базу знаний** и **Действия**, чтобы расширить возможности агента по предоставлению дополнительной информации и выполнению автоматизированных задач на основе запросов пользователей. Для этого упражнения вы можете пропустить эти шаги.
    
![Настройка агента](../../../02-explore-agentic-frameworks/images/agent-setup.png)

3. Чтобы создать нового мульти-ИИ агента, просто нажмите **Новый агент**. Новый агент будет отображен на странице Агенты.

## Тестирование агента

После создания агента вы можете протестировать его, чтобы увидеть, как он отвечает на запросы пользователей в игровом поле портала Azure AI Foundry.

1. В верхней части панели **Настройка** для вашего агента выберите **Попробовать в игровом поле**.
2. В панели **Игровое поле** вы можете взаимодействовать с агентом, вводя запросы в окне чата. Например, вы можете попросить агента найти рейсы из Сиэтла в Нью-Йорк на 28-е число.

    > **Примечание**: Агент может не предоставлять точные ответы, так как в этом упражнении не используются данные в реальном времени. Цель - протестировать способность агента понимать и отвечать на запросы пользователей на основе предоставленных инструкций.

    ![Игровое поле агента](../../../02-explore-agentic-frameworks/images/agent-playground.png)

3. После тестирования агента вы можете дополнительно настроить его, добавив больше намерений, обучающих данных и действий для расширения его возможностей.

## Очистка ресурсов

Когда вы закончите тестирование агента, вы можете удалить его, чтобы избежать дополнительных затрат.
1. Откройте [портал Azure](https://portal.azure.com) и просмотрите содержимое группы ресурсов, где вы развернули ресурсы хаба, использованные в этом упражнении.
2. На панели инструментов выберите **Удалить группу ресурсов**.
3. Введите имя группы ресурсов и подтвердите, что хотите её удалить.

## Ресурсы

- [Документация Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Портал Azure AI Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Начало работы с Azure AI Studio](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Основы агентов ИИ на Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.