<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:55:23+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "bg"
}
-->
# Настройка на курса

## Въведение

Този урок ще обхване как да стартирате примерите с код от този курс.

## Присъединете се към други обучаващи се и получете помощ

Преди да започнете да клонирате вашето хранилище, присъединете се към [AI Agents For Beginners Discord канала](https://aka.ms/ai-agents/discord), за да получите помощ с настройката, да зададете въпроси относно курса или да се свържете с други обучаващи се.

## Клониране или форкване на това хранилище

За да започнете, моля, клонирайте или форкнете GitHub хранилището. Това ще създаде ваша собствена версия на материалите от курса, за да можете да стартирате, тествате и променяте кода!

Това може да се направи, като кликнете върху линка за <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкване на хранилището</a>.

Сега трябва да имате ваша собствена форкната версия на този курс на следния линк:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.bg.png)

### Повърхностно клониране (препоръчително за работилници / Codespaces)

  >Пълното хранилище може да бъде голямо (~3 GB), когато изтеглите цялата история и всички файлове. Ако само посещавате работилницата или ви трябват само няколко папки с уроци, повърхностното клониране (или частично клониране) избягва повечето от тези изтегляния, като съкращава историята и/или пропуска ненужни файлове.

#### Бързо повърхностно клониране — минимална история, всички файлове

Заменете `<your-username>` в командите по-долу с вашия URL за форк (или URL на оригиналното хранилище, ако предпочитате).

За да клонирате само последната история на комитите (малко изтегляне):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

За да клонирате конкретен клон:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частично (селектирано) клониране — минимални файлове + само избрани папки

Това използва частично клониране и селективно изтегляне (изисква Git 2.25+ и се препоръчва модерна версия на Git с поддръжка за частично клониране):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Влезте в папката на хранилището:

За bash:

```bash
cd ai-agents-for-beginners
```

За Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

След това посочете кои папки искате (примерът по-долу показва две папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

След като клонирате и проверите файловете, ако ви трябват само файловете и искате да освободите място (без история на Git), моля, изтрийте метаданните на хранилището (💀необратимо — ще загубите всички функции на Git: няма комити, изтегляния, качвания или достъп до историята).

За Linux/macOS:

```bash
rm -rf .git
```

За Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### Използване на GitHub Codespaces (препоръчително за избягване на големи локални изтегляния)

- Създайте нов Codespace за това хранилище чрез [GitHub UI](https://github.com/codespaces).  

- В терминала на новосъздадения Codespace изпълнете една от командите за повърхностно/частично клониране по-горе, за да добавите само папките с уроци, които ви трябват, в работното пространство на Codespace.
- По избор: след клониране в Codespaces, премахнете .git, за да освободите допълнително пространство (вижте командите за премахване по-горе).
- Забележка: Ако предпочитате да отворите хранилището директно в Codespaces (без допълнително клониране), имайте предвид, че Codespaces ще създаде среда за разработка и може все още да предостави повече, отколкото ви е необходимо. Клонирането на повърхностно копие в нов Codespace ви дава повече контрол върху използването на дисковото пространство.

#### Съвети

- Винаги заменяйте URL за клониране с вашия форк, ако искате да редактирате/комитирате.
- Ако по-късно ви е необходима повече история или файлове, можете да ги изтеглите или да коригирате селективното изтегляне, за да включите допълнителни папки.

## Стартиране на кода

Този курс предлага серия от Jupyter Notebooks, които можете да стартирате, за да получите практически опит в изграждането на AI агенти.

Примерите с код използват:

**Изисква GitHub акаунт - Безплатно**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Обозначен като (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Обозначен като (autogen.ipynb)

**Изисква абонамент за Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Обозначен като (azureaiagent.ipynb)

Препоръчваме ви да изпробвате и трите типа примери, за да видите кой работи най-добре за вас.

Който и вариант да изберете, той ще определи кои стъпки за настройка трябва да следвате по-долу:

## Изисквания

- Python 3.12+
  - **NOTE**: Ако нямате инсталиран Python3.12, уверете се, че сте го инсталирали. След това създайте вашата виртуална среда (venv) с python3.12, за да гарантирате, че правилните версии са инсталирани от файла requirements.txt.
  
    >Пример

    Създайте директория за Python venv:

    ``` bash
    python3 -m venv venv
    ```

    След това активирайте venv средата за:

    macOS и Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- GitHub акаунт - За достъп до GitHub Models Marketplace
- Абонамент за Azure - За достъп до Azure AI Foundry
- Azure AI Foundry акаунт - За достъп до Azure AI Agent Service

В корена на това хранилище сме включили файл `requirements.txt`, който съдържа всички необходими Python пакети за стартиране на примерите с код.

Можете да ги инсталирате, като изпълните следната команда в терминала в корена на хранилището:

```bash
pip install -r requirements.txt
```
Препоръчваме да създадете виртуална среда за Python, за да избегнете конфликти и проблеми.

## Настройка на VSCode
Уверете се, че използвате правилната версия на Python в VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка за примери с използване на GitHub модели 

### Стъпка 1: Получете вашия GitHub Personal Access Token (PAT)

Този курс използва GitHub Models Marketplace, предоставяйки безплатен достъп до модели за големи езикови модели (LLMs), които ще използвате за изграждане на AI агенти.

За да използвате GitHub моделите, ще трябва да създадете [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Това може да се направи, като отидете на <a href="https://github.com/settings/personal-access-tokens" target="_blank">настройките за лични токени за достъп</a> във вашия GitHub акаунт.

Моля, следвайте [Принципа на минималните привилегии](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely), когато създавате вашия токен. Това означава, че трябва да дадете на токена само разрешенията, които са му необходими, за да стартира примерите с код в този курс.

1. Изберете опцията `Fine-grained tokens` от лявата страна на екрана, като преминете към **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.bg.png)

    След това изберете `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.bg.png)

2. Въведете описателно име за вашия токен, което отразява неговата цел, за да бъде лесно разпознаваем по-късно.


    🔐 Препоръка за продължителност на токена

    Препоръчителна продължителност: 30 дни
    За по-сигурна позиция можете да изберете по-кратък период — например 7 дни 🛡️
    Това е чудесен начин да си поставите лична цел и да завършите курса, докато мотивацията ви е висока 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.bg.png)

3. Ограничете обхвата на токена до вашия форк на това хранилище.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.bg.png)

4. Ограничете разрешенията на токена: Под **Permissions**, кликнете върху таба **Account** и натиснете бутона "+ Add permissions". Ще се появи падащо меню. Моля, потърсете **Models** и отметнете полето за него.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.bg.png)

5. Проверете необходимите разрешения преди да генерирате токена. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.bg.png)

6. Преди да генерирате токена, уверете се, че сте готови да го съхраните на сигурно място, като например в сейф за пароли, тъй като той няма да бъде показан отново след създаването му. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.bg.png)

Копирайте новия токен, който току-що сте създали. Сега ще го добавите към вашия `.env` файл, включен в този курс.


### Стъпка 2: Създайте вашия `.env` файл

За да създадете вашия `.env` файл, изпълнете следната команда в терминала.

```bash
cp .env.example .env
```

Това ще копира примерния файл и ще създаде `.env` във вашата директория, където ще попълните стойностите за променливите на средата.

С копирания токен, отворете файла `.env` в любимия си текстов редактор и го поставете в полето `GITHUB_TOKEN`.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.bg.png)


Сега трябва да можете да стартирате примерите с код от този курс.

## Настройка за примери с използване на Azure AI Foundry и Azure AI Agent Service

### Стъпка 1: Получете вашия Azure Project Endpoint


Следвайте стъпките за създаване на хъб и проект в Azure AI Foundry, описани тук: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


След като създадете вашия проект, ще трябва да получите връзката за вашия проект.

Това може да се направи, като отидете на страницата **Overview** на вашия проект в портала на Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.bg.png)

### Стъпка 2: Създайте вашия `.env` файл

За да създадете вашия `.env` файл, изпълнете следната команда в терминала.

```bash
cp .env.example .env
```

Това ще копира примерния файл и ще създаде `.env` във вашата директория, където ще попълните стойностите за променливите на средата.

С копирания токен, отворете файла `.env` в любимия си текстов редактор и го поставете в полето `PROJECT_ENDPOINT`.

### Стъпка 3: Влезте в Azure

Като най-добра практика за сигурност, ще използваме [автентикация без ключове](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst), за да се удостоверим в Azure OpenAI с Microsoft Entra ID. 

След това отворете терминал и изпълнете `az login --use-device-code`, за да влезете във вашия Azure акаунт.

След като влезете, изберете вашия абонамент в терминала.


## Допълнителни променливи на средата - Azure Search и Azure OpenAI 

За урока Agentic RAG - Урок 5 - има примери, които използват Azure Search и Azure OpenAI.

Ако искате да стартирате тези примери, ще трябва да добавите следните променливи на средата към вашия `.env` файл:

### Страница Overview (Проект)

- `AZURE_SUBSCRIPTION_ID` - Проверете **Project details** на страницата **Overview** на вашия проект.

- `AZURE_AI_PROJECT_NAME` - Погледнете горната част на страницата **Overview** за вашия проект.

- `AZURE_OPENAI_SERVICE` - Намерете това в таба **Included capabilities** за **Azure OpenAI Service** на страницата **Overview**.

### Център за управление

- `AZURE_OPENAI_RESOURCE_GROUP` - Отидете на **Project properties** на страницата **Overview** на **Management Center**.

- `GLOBAL_LLM_SERVICE` - Под **Connected resources**, намерете името на връзката **Azure AI Services**. Ако не е посочено, проверете **Azure portal** под вашата ресурсна група за името на ресурса AI Services.

### Страница Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Изберете вашия модел за вграждане (например `text-embedding-ada-002`) и отбележете **Deployment name** от детайлите на модела.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Изберете вашия чат модел (например `gpt-4o-mini`) и отбележете **Deployment name** от детайлите на модела.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Потърсете **Azure AI services**, кликнете върху него, след това отидете на **Resource Management**, **Keys and Endpoint**, превъртете надолу до "Azure OpenAI endpoints" и копирайте този, който казва "Language APIs".

- `AZURE_OPENAI_API_KEY` - От същия екран, копирайте KEY 1 или KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Намерете вашия ресурс **Azure AI Search**, кликнете върху него и вижте **Overview**.

- `AZURE_SEARCH_API_KEY` - След това отидете на **Settings** и след това **Keys**, за да копирате основния или вторичния администраторски ключ.

### Външна уеб страница

- `AZURE_OPENAI_API_VERSION` - Посетете страницата [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) под **Latest GA API release**.

### Настройка на автентикация без ключове

Вместо да кодирате вашите идентификационни данни, ще използваме връзка без ключове с Azure OpenAI. За целта ще импортираме `DefaultAzureCredential` и по-късно ще извикаме функцията `DefaultAzureCredential`, за да получим идентификационните данни.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Затруднения?
Ако имате някакви проблеми с изпълнението на тази настройка, присъединете се към нашия <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord на общността Azure AI</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">създайте проблем</a>.

## Следващ урок

Вече сте готови да стартирате кода за този курс. Приятно учене за света на AI агентите!

[Въведение в AI агентите и техните приложения](../01-intro-to-ai-agents/README.md)

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.