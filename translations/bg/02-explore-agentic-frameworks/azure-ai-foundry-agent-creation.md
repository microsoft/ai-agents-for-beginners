# Разработка на Microsoft Foundry Agent Service  

В това упражнение използвате инструментите на Microsoft Foundry Agent Service в [Microsoft Foundry портала](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst), за да създадете агент за резервация на полети. Агентът ще може да взаимодейства с потребителите и да предоставя информация за полети.  

## Предварителни изисквания  

За да завършите това упражнение, ви трябват следните неща:  
1. Акаунт в Azure с активен абонамент. [Създайте акаунт безплатно](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).  
2. Трябва да имате разрешения за създаване на Microsoft Foundry hub или някой да създаде такъв вместо вас.  
    - Ако вашата роля е Contributor или Owner, можете да следвате стъпките в това ръководство.  

## Създаване на Microsoft Foundry hub  

> **Забележка:** Microsoft Foundry преди беше известна като Azure AI Studio.  

1. Следвайте насоките от публикацията в блога на [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) за създаване на Microsoft Foundry hub.  
2. Когато проектът ви е създаден, затворете всички показани съвети и прегледайте страницата на проекта в портала на Microsoft Foundry, която трябва да изглежда подобно на следната снимка:  

    ![Microsoft Foundry Project](../../../translated_images/bg/azure-ai-foundry.88d0c35298348c2f.webp)  

## Разгръщане на модел  

1. В панела вляво за проекта си, в секцията **My assets**, изберете страницата **Models + endpoints**.  
2. В страницата **Models + endpoints**, в раздела **Model deployments**, от менюто **+ Deploy model** изберете **Deploy base model**.  
3. Потърсете модела `gpt-4.1-mini` в списъка, след това го изберете и потвърдете.  

    > **Забележка**: Намаляването на TPM помага да се избегне прекомерното използване на квотата, налична в абонамента, който използвате.  

    ![Model Deployed](../../../translated_images/bg/model-deployment.3749c53fb81e18fd.webp)  

## Създаване на агент  

След като сте разположили модел, можете да създадете агент. Агентът е разговорен AI модел, който може да се използва за взаимодействие с потребителите.  

1. В панела вляво за проекта си, в секцията **Build & Customize**, изберете страницата **Agents**.  
2. Кликнете **+ Create agent**, за да създадете нов агент. В диалоговия прозорец **Agent Setup**:  
    - Въведете име за агента, например `FlightAgent`.  
    - Уверете се, че е избрано разгръщането на модела `gpt-4.1-mini`, което сте създали по-рано.  
    - Задайте **Instructions** според подсказката, която искате агентът да следва. Ето един пример:  
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
> За подробна подсказка можете да разгледате [този репозиторий](https://github.com/ShivamGoyal03/RoamMind) за повече информация.  
    
> Освен това, може да добавите **Knowledge Base** и **Actions**, за да подобрите възможностите на агента да предоставя повече информация и да изпълнява автоматизирани задачи според исканията на потребителя. За това упражнение можете да пропуснете тези стъпки.  
    
![Agent Setup](../../../translated_images/bg/agent-setup.9bbb8755bf5df672.webp)  

3. За да създадете нов мулти-AI агент, просто кликнете **New Agent**. Новосъздаденият агент ще се покаже на страницата Agents.  


## Тествайте агента  

След като създадете агента, можете да го тествате, за да видите как отговаря на въпроси от потребителите в playground-а на Microsoft Foundry портала.  

1. В горната част на панела **Setup** за агента си изберете **Try in playground**.  
2. В панела **Playground** можете да взаимодействате с агента, като въвеждате запитвания в чат прозореца. Например, можете да помолите агента да търси полети от Сиатъл до Ню Йорк на 28-ми.  

    > **Забележка**: Агентът може да не предоставя точни отговори, тъй като в това упражнение не се използват актуални данни в реално време. Целта е да се тества способността на агента да разбира и отговаря на запитванията на потребителите според предоставените инструкции.  

    ![Agent Playground](../../../translated_images/bg/agent-playground.dc146586de715010.webp)  

3. След тестване на агента можете да го персонализирате допълнително, като добавите повече намерения, тренировъчни данни и действия, за да подобрите възможностите му.  

## Почистване на ресурси  

Когато приключите с тестването на агента, можете да го изтриете, за да избегнете допълнителни разходи.  
1. Отворете [Azure портала](https://portal.azure.com) и прегледайте съдържанието на ресурсната група, в която сте разположили ресурсите на hub-a, използвани в това упражнение.  
2. В лентата с инструменти изберете **Delete resource group**.  
3. Въведете името на ресурсната група и потвърдете, че искате да я изтриете.  

## Ресурси  

- [Документация за Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)  
- [Microsoft Foundry портал](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)  
- [Започване с Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)  
- [Основи на AI агентите в Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)  
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->