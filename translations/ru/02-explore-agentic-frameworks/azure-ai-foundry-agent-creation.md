# Разработка сервиса агента Microsoft Foundry

В этом упражнении вы используете инструменты Microsoft Foundry Agent Service в [портале Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) для создания агента для бронирования авиабилетов. Агент сможет взаимодействовать с пользователями и предоставлять информацию о рейсах.

## Требования

Чтобы выполнить это упражнение, необходимо следующее:
1. Учетная запись Azure с активной подпиской. [Создайте учетную запись бесплатно](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Необходимы права для создания Microsoft Foundry hub или уже созданный для вас hub.
    - Если ваша роль — Contributor или Owner, вы можете следовать шагам в этом руководстве.

## Создание Microsoft Foundry hub

> **Примечание:** Microsoft Foundry ранее назывался Azure AI Studio.

1. Следуйте этим инструкциям из [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) блог-поста для создания Microsoft Foundry hub.
2. После создания проекта закройте все появившиеся подсказки и ознакомьтесь со страницей проекта в портале Microsoft Foundry, которая должна выглядеть примерно так, как на изображении ниже:

    ![Microsoft Foundry Project](../../../translated_images/ru/azure-ai-foundry.88d0c35298348c2f.webp)

## Развертывание модели

1. В панели слева вашего проекта в разделе **My assets** выберите страницу **Models + endpoints**.
2. На странице **Models + endpoints**, во вкладке **Model deployments**, в меню **+ Deploy model** выберите **Deploy base model**.
3. Найдите модель `gpt-5-mini` в списке, затем выберите и подтвердите её.

    > **Примечание**: Уменьшение TPM помогает избежать чрезмерного использования квоты, доступной в вашей подписке.

    ![Model Deployed](../../../translated_images/ru/model-deployment.3749c53fb81e18fd.webp)

## Создание агента

Теперь, когда вы развернули модель, вы можете создать агента. Агент — это модель разговорного ИИ, которая может использоваться для взаимодействия с пользователями.

1. В панели слева вашего проекта в разделе **Build & Customize** выберите страницу **Agents**.
2. Нажмите **+ Create agent**, чтобы создать нового агента. В диалоговом окне **Agent Setup**:
    - Введите имя агента, например `FlightAgent`.
    - Убедитесь, что выбрана модель `gpt-5-mini`, развернутая ранее.
    - Установите **Instructions** согласно инструкции, которой должен следовать агент. Вот пример:
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
> Для подробного промпта вы можете ознакомиться с [этим репозиторием](https://github.com/ShivamGoyal03/RoamMind) для получения дополнительной информации.
    
> Кроме того, вы можете добавить **Knowledge Base** и **Actions** для расширения возможностей агента по предоставлению дополнительной информации и выполнению автоматизированных задач на основе запросов пользователей. Для этого упражнения можно пропустить эти шаги.
    
![Agent Setup](../../../translated_images/ru/agent-setup.9bbb8755bf5df672.webp)

3. Чтобы создать нового мульти-ИИ агента, просто нажмите **New Agent**. Новый агент появится на странице Agents.


## Тестирование агента

После создания агента вы можете протестировать его, чтобы увидеть, как он отвечает на запросы пользователей в игровом поле портала Microsoft Foundry.

1. В верхней части панели **Setup** вашего агента выберите **Try in playground**.
2. В панели **Playground** вы можете взаимодействовать с агентом, вводя запросы в окне чата. Например, вы можете попросить агента найти рейсы из Сиэтла в Нью-Йорк на 28-е число.

    > **Примечание**: Агент может не давать точные ответы, поскольку в данном упражнении не используется актуальная информация в реальном времени. Цель — проверить способность агента понимать и отвечать на запросы пользователей на основе заданных инструкций.

    ![Agent Playground](../../../translated_images/ru/agent-playground.dc146586de715010.webp)

3. После тестирования агента вы можете дополнительно настроить его, добавляя больше интентов, обучающих данных и действий для расширения его возможностей.

## Очистка ресурсов

После завершения тестирования агента вы можете удалить его, чтобы избежать дополнительных расходов.
1. Откройте [Azure портал](https://portal.azure.com) и просмотрите содержимое группы ресурсов, в которую вы развернули hub и другие ресурсы, используемые в этом упражнении.
2. На панели инструментов выберите **Delete resource group**.
3. Введите имя группы ресурсов и подтвердите удаление.

## Ресурсы

- [Документация Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Портал Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Начало работы с Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Основы агентов ИИ на Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->