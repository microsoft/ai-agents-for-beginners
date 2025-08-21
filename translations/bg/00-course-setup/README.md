<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76945069b52a49cd0432ae3e0b0ba22e",
  "translation_date": "2025-07-12T07:57:20+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "bg"
}
-->
# Настройка на курса

## Въведение

Този урок ще обхване как да стартирате примерите с код от този курс.

## Клониране или форкване на това хранилище

За да започнете, моля, клонирайте или направете форк на GitHub хранилището. Това ще създаде ваша собствена версия на материалите от курса, за да можете да стартирате, тествате и променяте кода!

Това може да се направи, като кликнете върху линка към

Вече трябва да имате ваша собствена форкната версия на курса на следния линк:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.bg.png)

## Стартиране на кода

Този курс предлага серия от Jupyter Notebooks, които можете да стартирате, за да получите практически опит в изграждането на AI агенти.

Примерите с код използват следното:

**Изисква GitHub акаунт - Безплатно**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Обозначено като (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Обозначено като (autogen.ipynb)

**Изисква Azure абонамент**:
3) Azure AI Foundry + Azure AI Agent Service. Обозначено като (azureaiagent.ipynb)

Препоръчваме ви да изпробвате и трите типа примери, за да видите кой работи най-добре за вас.

Който и вариант да изберете, той ще определи кои стъпки за настройка трябва да следвате по-долу:

## Изисквания

- Python 3.12+
  - **NOTE**: Ако нямате инсталиран Python 3.12, уверете се, че го инсталирате. След това създайте виртуална среда с python3.12, за да се гарантира, че правилните версии се инсталират от файла requirements.txt.
- GitHub акаунт - за достъп до GitHub Models Marketplace
- Azure абонамент - за достъп до Azure AI Foundry
- Azure AI Foundry акаунт - за достъп до Azure AI Agent Service

В кореновата директория на това хранилище сме включили файл `requirements.txt`, който съдържа всички необходими Python пакети за стартиране на примерите с код.

Можете да ги инсталирате, като изпълните следната команда в терминала в кореновата директория на хранилището:

```bash
pip install -r requirements.txt
```
Препоръчваме създаването на Python виртуална среда, за да избегнете конфликти и проблеми.

## Настройка на VSCode
Уверете се, че използвате правилната версия на Python в VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка за примери с GitHub модели

### Стъпка 1: Получаване на вашия GitHub Personal Access Token (PAT)

Този курс използва GitHub Models Marketplace, предоставяйки безплатен достъп до големи езикови модели (LLMs), които ще използвате за изграждане на AI агенти.

За да използвате GitHub моделите, трябва да създадете [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Това може да се направи, като отидете на вашия GitHub акаунт.

в GitHub акаунт.

1. Изберете опцията `Fine-grained tokens` от лявата страна на екрана.

    След това изберете `Generate new token`.

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.bg.png)

Ще бъдете подканени да въведете име за вашия токен, да изберете дата на изтичане (Препоръчително: 30 дни) и да изберете обхватите на токена (Public Repositories).

Също така е необходимо да редактирате разрешенията на този токен: Permissions -> Models -> Позволява достъп до GitHub Models

Копирайте новия токен, който току-що създадохте. Сега ще го добавите към вашия `.env` файл, включен в този курс.

### Стъпка 2: Създаване на вашия `.env` файл

За да създадете вашия `.env` файл, изпълнете следната команда в терминала.

```bash
cp .env.example .env
```

Това ще копира примерния файл и ще създаде `.env` във вашата директория, където ще попълните стойностите за променливите на средата.

С копирания токен отворете `.env` файла в любимия си текстов редактор и го поставете в полето `GITHUB_TOKEN`.

Вече трябва да можете да стартирате примерите с код от този курс.

## Настройка за примери с Azure AI Foundry и Azure AI Agent Service

### Стъпка 1: Получаване на вашия Azure Project Endpoint

Следвайте стъпките за създаване на хъб и проект в Azure AI Foundry, описани тук: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

След като създадете вашия проект, ще трябва да получите низ за връзка към вашия проект.

Това може да се направи, като отидете на страницата **Overview** на вашия проект в Azure AI Foundry портала.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.bg.png)

### Стъпка 2: Създаване на вашия `.env` файл

За да създадете вашия `.env` файл, изпълнете следната команда в терминала.

```bash
cp .env.example .env
```

Това ще копира примерния файл и ще създаде `.env` във вашата директория, където ще попълните стойностите за променливите на средата.

С копирания токен отворете `.env` файла в любимия си текстов редактор и го поставете в полето `PROJECT_ENDPOINT`.

### Стъпка 3: Вход в Azure

Като най-добра практика за сигурност ще използваме [автентикация без ключове](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst), за да се удостоверим в Azure OpenAI с Microsoft Entra ID.

След това отворете терминал и изпълнете `az login --use-device-code`, за да влезете във вашия Azure акаунт.

След като влезете, изберете вашия абонамент в терминала.

## Допълнителни променливи на средата - Azure Search и Azure OpenAI

За урока Agentic RAG - Урок 5 - има примери, които използват Azure Search и Azure OpenAI.

Ако искате да стартирате тези примери, ще трябва да добавите следните променливи на средата към вашия `.env` файл:

### Страница Overview (Проект)

- `AZURE_SUBSCRIPTION_ID` - Проверете **Project details** на страницата **Overview** на вашия проект.

- `AZURE_AI_PROJECT_NAME` - Вижте горната част на страницата **Overview** за вашия проект.

- `AZURE_OPENAI_SERVICE` - Намерете това в таба **Included capabilities** за **Azure OpenAI Service** на страницата **Overview**.

### Център за управление

- `AZURE_OPENAI_RESOURCE_GROUP` - Отидете на **Project properties** на страницата **Overview** на **Management Center**.

- `GLOBAL_LLM_SERVICE` - Под **Connected resources**, намерете името на връзката **Azure AI Services**. Ако не е изброено, проверете **Azure portal** под вашата ресурсна група за името на ресурса AI Services.

### Страница Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Изберете вашия модел за вграждане (например `text-embedding-ada-002`) и отбележете **Deployment name** от детайлите на модела.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Изберете вашия чат модел (например `gpt-4o-mini`) и отбележете **Deployment name** от детайлите на модела.

### Azure портал

- `AZURE_OPENAI_ENDPOINT` - Потърсете **Azure AI services**, кликнете върху него, след това отидете на **Resource Management**, **Keys and Endpoint**, превъртете надолу до "Azure OpenAI endpoints" и копирайте този, който е за "Language APIs".

- `AZURE_OPENAI_API_KEY` - От същия екран копирайте KEY 1 или KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Намерете вашия **Azure AI Search** ресурс, кликнете върху него и вижте **Overview**.

- `AZURE_SEARCH_API_KEY` - След това отидете на **Settings** и след това **Keys**, за да копирате основния или вторичния администраторски ключ.

### Външна уеб страница

- `AZURE_OPENAI_API_VERSION` - Посетете страницата [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) под **Latest GA API release**.

### Настройка на автентикация без ключове

Вместо да кодирате вашите идентификационни данни, ще използваме връзка без ключове с Azure OpenAI. За целта ще импортираме `DefaultAzureCredential` и по-късно ще извикаме функцията `DefaultAzureCredential`, за да получим идентификационните данни.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Нуждаете се от помощ?

Ако имате проблеми със стартирането на тази настройка, присъединете се към нашия

или

.

## Следващ урок

Вече сте готови да стартирате кода за този курс. Приятно учене за света на AI агентите!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия първичен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.