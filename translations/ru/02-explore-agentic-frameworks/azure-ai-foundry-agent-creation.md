# Разработка сервиса агента Microsoft Foundry

В этом упражнении вы используете инструменты сервиса агента Microsoft Foundry в [портале Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) для создания агента для бронирования билетов на авиарейсы. Агент сможет взаимодействовать с пользователями и предоставлять информацию о рейсах.

## Предварительные требования

Для выполнения этого упражнения вам потребуется следующее:
1. Учетная запись Azure с активной подпиской. [Создайте бесплатную учетную запись](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. У вас должны быть права для создания хаба Microsoft Foundry или доступ к уже созданному хабу.
    - Если ваша роль Contributor или Owner, вы можете следовать шагам в этом руководстве.

## Создание хаба Microsoft Foundry

> **Примечание:** Ранее Microsoft Foundry назывался Azure AI Studio.

1. Следуйте этим рекомендациям из [блога Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) для создания хаба Microsoft Foundry.
2. После создания проекта закройте все отображаемые советы и ознакомьтесь со страницей проекта в портале Microsoft Foundry, которая должна выглядеть примерно так, как на изображении ниже:

    ![Microsoft Foundry Project](../../../translated_images/ru/azure-ai-foundry.88d0c35298348c2f.webp)

## Развертывание модели

1. В панели слева для вашего проекта в разделе **Мои ресурсы** выберите страницу **Модели + конечные точки**.
2. На странице **Модели + конечные точки**, на вкладке **Развертывания модели**, в меню **+ Развернуть модель** выберите **Развернуть базовую модель**.
3. В списке найдите модель `gpt-4.1-mini`, затем выберите и подтвердите её.

    > **Примечание**: Снижение TPM помогает избежать чрезмерного использования доступной квоты в вашей подписке.

    ![Model Deployed](../../../translated_images/ru/model-deployment.3749c53fb81e18fd.webp)

## Создание агента

Теперь, когда модель развернута, вы можете создать агента. Агент — это модель разговорного искусственного интеллекта, которая может использоваться для взаимодействия с пользователями.

1. В панели слева для вашего проекта в разделе **Создание и настройка** выберите страницу **Агенты**.
2. Нажмите **+ Создать агента** для создания нового агента. В диалоговом окне **Настройка агента**:
    - Введите имя агента, например `FlightAgent`.
    - Убедитесь, что выбрано развертывание модели `gpt-4.1-mini`, созданное ранее.
    - Настройте **Инструкции** согласно подсказке, которой вы хотите, чтобы агент следовал. Вот пример:
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
    
> Кроме того, вы можете добавить **Базу знаний** и **Действия** для расширения возможностей агента по предоставлению информации и выполнению автоматизированных задач на основе запросов пользователей. Для этого упражнения эти шаги можно пропустить.
    
![Agent Setup](../../../translated_images/ru/agent-setup.9bbb8755bf5df672.webp)

3. Чтобы создать нового мульти-AI агента, просто нажмите **Новый агент**. Новый агент отобразится на странице Агенты.


## Тестирование агента

После создания агента вы можете протестировать его, чтобы увидеть, как он отвечает на запросы пользователей в песочнице портала Microsoft Foundry.

1. Вверху панели **Настройка** для вашего агента выберите **Попробовать в песочнице**.
2. В панели **Песочница** вы можете взаимодействовать с агентом, вводя запросы в окно чата. Например, вы можете попросить агента найти рейсы из Сиэтла в Нью-Йорк на 28 число.

    > **Примечание**: Агент может не предоставлять точные ответы, так как в этом упражнении не используются данные в реальном времени. Цель — проверить способность агента понимать и отвечать на запросы пользователей на основе заданных инструкций.

    ![Agent Playground](../../../translated_images/ru/agent-playground.dc146586de715010.webp)

3. После тестирования агента вы можете дополнительно настраивать его, добавляя больше намерений, тренировочных данных и действий для расширения функционала.

## Очистка ресурсов

После завершения тестирования агента его можно удалить, чтобы избежать дополнительных затрат.
1. Откройте [портал Azure](https://portal.azure.com) и перейдите к группе ресурсов, в которую были развернуты ресурсы хаба для этого упражнения.
2. В панели инструментов выберите **Удалить группу ресурсов**.
3. Введите имя группы ресурсов и подтвердите удаление.

## Ресурсы

- [Документация Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Портал Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Первоначальное знакомство с Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Основы агентов ИИ на Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->