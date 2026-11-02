# Развој Microsoft Foundry Agent сервиса

У овој вежби користите алате Microsoft Foundry Agent сервиса у [Microsoft Foundry порталу](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) да бисте направили агента за резервацију летова. Агент ће моћи да комуницира са корисницима и пружа информације о летовима.

## Предуслови

Да бисте завршили ову вежбу, потребно је следеће:
1. Azure налог са активном претплатом. [Направите налог бесплатно](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Потребне су вам дозволе за креирање Microsoft Foundry чворишта или неко треба да га направи за вас.
    - Ако сте у улози Contributor или Owner, можете пратити кораке у овом упутству.

## Креирање Microsoft Foundry чворишта

> **Напомена:** Microsoft Foundry је раније био познат као Azure AI Studio.

1. Пратите смернице из [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) блог поста за креирање Microsoft Foundry чворишта.
2. Када пројекат буде креиран, затворите све савете који се појаве и прегледајте страницу пројекта у Microsoft Foundry порталу, која би требало да изгледа слично као следећа слика:

    ![Microsoft Foundry Project](../../../translated_images/sr/azure-ai-foundry.88d0c35298348c2f.webp)

## Распоређивање модела

1. У панелу са леве стране за ваш пројекат, у одељку **My assets**, изаберите страницу **Models + endpoints**.
2. На страници **Models + endpoints**, на картици **Model deployments**, у менију **+ Deploy model**, изаберите **Deploy base model**.
3. Претражите модел `gpt-5-mini` на листи, затим га изаберите и потврдите.

    > **Напомена**: Смањење TPM помаже да се избегне прекомерна употреба квоте доступне у претплати коју користите.

    ![Model Deployed](../../../translated_images/sr/model-deployment.3749c53fb81e18fd.webp)

## Креирање агента

Сада када сте распоредили модел, можете креирати агента. Агент је конверзациони AI модел који се користи за интеракцију са корисницима.

1. У панелу са леве стране за ваш пројекат, у одељку **Build & Customize**, изаберите страницу **Agents**.
2. Кликните **+ Create agent** да бисте креирали новог агента. У дијалогу **Agent Setup**:
    - Унесите име агента, као што је `FlightAgent`.
    - Уверите се да је изабрано распоређивање модела `gpt-5-mini` које сте раније креирали.
    - Поставите **Instructions** према упутствима која желите да агент прати. Ево једног примера:
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
> За детаљан упит можете проверити [овaj репозиторијум](https://github.com/ShivamGoyal03/RoamMind) за више информација.
    
> Поред тога, можете додати **Knowledge Base** и **Actions** да бисте унапредили могућности агента да пружи више информација и обавља аутоматизоване задатке на основу корисничких захтева. За ову вежбу, ове кораке можете прескочити.
    
![Agent Setup](../../../translated_images/sr/agent-setup.9bbb8755bf5df672.webp)

3. За креирање новог multi-AI агента, једноставно кликните **New Agent**. Новокреирани агент ће се затим приказати на страници Agents.


## Тестирање агента

Након креирања агента можете га тестирати да видите како одговара на корисничке упите у Microsoft Foundry порталу у режиму игре.

1. На врху панела **Setup** за вашег агента изаберите **Try in playground**.
2. У панелу **Playground** можете комуницирати са агентом тако што ћете у писаној форми у прозору за ћаскање постављати питања. На пример, можете затражити од агента да тражи летове од Сијетла до Њујорка 28. у месецу.

    > **Напомена**: Агент можда неће пружати тачне одговоре, јер се у овој вежби не користе подаци у реалном времену. Намена је да се тестирате способност агента да разуме и одговара на корисничке упите у складу са датим упутствима.

    ![Agent Playground](../../../translated_images/sr/agent-playground.dc146586de715010.webp)

3. Након тестирања агента, можете га додатно прилагодити додавањем више интента, података за обуку и акција како бисте унапредили његове могућности.

## Чишћење ресурса

Када завршите са тестирањем агента, можете га избрисати да бисте избегли додатне трошкове.
1. Отворите [Azure портал](https://portal.azure.com) и прегледајте садржај ресурса групе у којој сте распоредили чвориште коришћено у овој вежби.
2. На траци са алаткама изаберите **Delete resource group**.
3. Унесите име ресурса групе и потврдите да желите да је избришете.

## Ресурси

- [Microsoft Foundry документација](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry портал](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Започињање рада са Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Основе AI агената на Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->