<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76945069b52a49cd0432ae3e0b0ba22e",
  "translation_date": "2025-07-12T07:57:55+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sr"
}
-->
у вашем GitHub налогу.

Изаберите опцију `Fine-grained tokens` са леве стране екрана.

    Затим изаберите `Generate new token`.

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.sr.png)

Бићете упитани да унесете име за ваш токен, изаберете датум истека (Препоручено: 30 дана) и изаберете опсеге за ваш токен (Јавни репозиторијуми).

Такође је неопходно изменити дозволе овог токена: Permissions -> Models -> Дозволи приступ GitHub моделима

Копирајте нови токен који сте управо креирали. Сада ћете га додати у ваш `.env` фајл који је укључен у овај курс.

### Корак 2: Креирајте своју `.env` датотеку

Да бисте креирали `.env` датотеку, покрените следећу команду у вашем терминалу.

```bash
cp .env.example .env
```

Ово ће копирати пример фајла и креирати `.env` у вашем директоријуму где ћете унети вредности за променљиве окружења.

Са копираним токеном, отворите `.env` датотеку у вашем омиљеном текст едитору и налепите ваш токен у поље `GITHUB_TOKEN`.

Сада би требало да можете да покренете примере кода из овог курса.

## Подешавање за примере који користе Azure AI Foundry и Azure AI Agent Service

### Корак 1: Преузмите свој Azure Project Endpoint

Пратите кораке за креирање хаба и пројекта у Azure AI Foundry који се налазе овде: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Када креирате свој пројекат, потребно је да преузмете стринг за повезивање вашег пројекта.

Ово можете урадити тако што ћете отићи на страницу **Overview** вашег пројекта у Azure AI Foundry порталу.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sr.png)

### Корак 2: Креирајте своју `.env` датотеку

Да бисте креирали `.env` датотеку, покрените следећу команду у вашем терминалу.

```bash
cp .env.example .env
```

Ово ће копирати пример фајла и креирати `.env` у вашем директоријуму где ћете унети вредности за променљиве окружења.

Са копираним токеном, отворите `.env` датотеку у вашем омиљеном текст едитору и налепите ваш токен у поље `PROJECT_ENDPOINT`.

### Корак 3: Пријавите се на Azure

Као најбољу праксу за безбедност, користићемо [аутентификацију без кључа](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) за аутентификацију на Azure OpenAI са Microsoft Entra ID.

Затим, отворите терминал и покрените `az login --use-device-code` да се пријавите на ваш Azure налог.

Када се пријавите, изаберите своју претплату у терминалу.

## Додатне променљиве окружења - Azure Search и Azure OpenAI 

За лекцију Agentic RAG - Лекција 5 - постоје примери који користе Azure Search и Azure OpenAI.

Ако желите да покренете ове примере, потребно је да додате следеће променљиве окружења у вашу `.env` датотеку:

### Страница прегледа (Пројекат)

- `AZURE_SUBSCRIPTION_ID` - Проверите **Project details** на страници **Overview** вашег пројекта.

- `AZURE_AI_PROJECT_NAME` - Погледајте врх странице **Overview** вашег пројекта.

- `AZURE_OPENAI_SERVICE` - Пронађите ово на картици **Included capabilities** за **Azure OpenAI Service** на страници **Overview**.

### Центар за управљање

- `AZURE_OPENAI_RESOURCE_GROUP` - Идите на **Project properties** на страници **Overview** у **Management Center**.

- `GLOBAL_LLM_SERVICE` - Под **Connected resources**, пронађите име везе за **Azure AI Services**. Ако није наведено, проверите у **Azure порталу** унутар ваше групе ресурса за име ресурса AI Services.

### Страница модела + крајњих тачака

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Изаберите свој модел за уграђивање (нпр. `text-embedding-ada-002`) и забележите **Deployment name** из детаља модела.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Изаберите свој модел за ћаскање (нпр. `gpt-4o-mini`) и забележите **Deployment name** из детаља модела.

### Azure портал

- `AZURE_OPENAI_ENDPOINT` - Потражите **Azure AI services**, кликните на њега, затим идите на **Resource Management**, **Keys and Endpoint**, скролујте до "Azure OpenAI endpoints" и копирајте онај који пише "Language APIs".

- `AZURE_OPENAI_API_KEY` - Са истог екрана, копирајте KEY 1 или KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Пронађите ваш **Azure AI Search** ресурс, кликните на њега и погледајте **Overview**.

- `AZURE_SEARCH_API_KEY` - Затим идите на **Settings** и затим **Keys** да копирате примарни или секундарни администраторски кључ.

### Спољна веб страница

- `AZURE_OPENAI_API_VERSION` - Посетите страницу [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) под **Latest GA API release**.

### Подешавање аутентификације без кључа

Уместо да уносите ваше акредитиве директно у код, користићемо keyless конекцију са Azure OpenAI. За то ћемо импортовати `DefaultAzureCredential` и касније позвати функцију `DefaultAzureCredential` да добијемо акредитиве.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Заглављени негде?

Ако имате било каквих проблема са покретањем овог подешавања, придружите се нашем

или

.

## Следећа лекција

Сада сте спремни да покренете код за овај курс. Срећно у учењу више о свету AI агената!

[Увод у AI агенте и њихове случајеве употребе](../01-intro-to-ai-agents/README.md)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.