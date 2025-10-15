<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:36:31+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ru"
}
-->
# Настройка курса

## Введение

В этом уроке мы рассмотрим, как запускать примеры кода из данного курса.

## Присоединяйтесь к другим участникам и получайте помощь

Прежде чем клонировать репозиторий, присоединитесь к [каналу Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord), чтобы получить помощь с настройкой, задать вопросы о курсе или связаться с другими участниками.

## Клонируйте или форкните этот репозиторий

Для начала клонируйте или форкните репозиторий GitHub. Это создаст вашу собственную версию материалов курса, чтобы вы могли запускать, тестировать и изменять код!

Это можно сделать, перейдя по ссылке <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкнуть репозиторий</a>.

Теперь у вас должна быть собственная форкнутая версия этого курса по следующей ссылке:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.ru.png)

### Поверхностное клонирование (рекомендуется для воркшопов / Codespaces)

  >Полный репозиторий может быть большим (~3 ГБ) при загрузке всей истории и всех файлов. Если вы участвуете только в воркшопе или вам нужны только несколько папок с уроками, поверхностное клонирование (или выборочное клонирование) позволяет избежать большей части загрузки, сокращая историю и/или пропуская блобы.

#### Быстрое поверхностное клонирование — минимальная история, все файлы

Замените `<your-username>` в командах ниже на URL вашего форка (или URL оригинального репозитория, если вы предпочитаете).

Чтобы клонировать только последнюю историю коммитов (небольшая загрузка):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Чтобы клонировать определенную ветку:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частичное (выборочное) клонирование — минимальные блобы + только выбранные папки

Для этого используется частичное клонирование и выборочная загрузка (требуется Git версии 2.25+ и рекомендуется современный Git с поддержкой частичного клонирования):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдите в папку репозитория:

Для bash:

```bash
cd ai-agents-for-beginners
```

Для Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

Затем укажите, какие папки вам нужны (пример ниже показывает две папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

После клонирования и проверки файлов, если вам нужны только файлы и вы хотите освободить место (без истории git), удалите метаданные репозитория (💀необратимо — вы потеряете все функции Git: коммиты, загрузки, отправки или доступ к истории).

Для Linux/macOS:

```bash
rm -rf .git
```

Для Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### Использование GitHub Codespaces (рекомендуется для избежания больших локальных загрузок)

- Создайте новый Codespace для этого репозитория через [интерфейс GitHub](https://github.com/codespaces).  

- В терминале нового Codespace выполните одну из команд поверхностного/выборочного клонирования, чтобы загрузить только нужные папки уроков в рабочую область Codespace.
- Опционально: после клонирования внутри Codespaces удалите .git, чтобы освободить дополнительное место (см. команды удаления выше).
- Примечание: если вы предпочитаете открыть репозиторий напрямую в Codespaces (без дополнительного клонирования), учтите, что Codespaces создаст среду devcontainer и может загрузить больше, чем вам нужно. Клонирование поверхностной копии внутри нового Codespace дает больше контроля над использованием дискового пространства.

#### Советы

- Всегда заменяйте URL клонирования на ваш форк, если вы хотите редактировать/коммитить.
- Если позже вам понадобится больше истории или файлов, вы можете их загрузить или настроить выборочную загрузку для включения дополнительных папок.

## Запуск кода

Этот курс предлагает серию Jupyter Notebooks, которые вы можете использовать для практического изучения создания AI-агентов.

Примеры кода используют:

**Требуется аккаунт GitHub - бесплатно**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Обозначено как (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Обозначено как (autogen.ipynb)

**Требуется подписка Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Обозначено как (azureaiagent.ipynb)

Мы рекомендуем попробовать все три типа примеров, чтобы понять, какой из них лучше всего подходит для вас.

Какой бы вариант вы ни выбрали, он определит, какие шаги настройки вам нужно будет выполнить ниже:

## Требования

- Python 3.12+
  - **NOTE**: Если у вас не установлен Python 3.12, убедитесь, что вы его установили. Затем создайте виртуальную среду (venv) с использованием python3.12, чтобы гарантировать установку правильных версий из файла requirements.txt.
  
    >Пример

    Создайте директорию виртуальной среды Python:

    ``` bash
    python3 -m venv venv
    ```

    Затем активируйте виртуальную среду для:

    macOS и Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- Аккаунт GitHub - для доступа к GitHub Models Marketplace
- Подписка Azure - для доступа к Azure AI Foundry
- Аккаунт Azure AI Foundry - для доступа к Azure AI Agent Service

Мы включили файл `requirements.txt` в корневую папку этого репозитория, который содержит все необходимые пакеты Python для запуска примеров кода.

Вы можете установить их, выполнив следующую команду в терминале в корневой папке репозитория:

```bash
pip install -r requirements.txt
```

Мы рекомендуем создать виртуальную среду Python, чтобы избежать конфликтов и проблем.

## Настройка VSCode
Убедитесь, что вы используете правильную версию Python в VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка для примеров с использованием GitHub Models 

### Шаг 1: Получите персональный токен доступа (PAT) GitHub

Этот курс использует GitHub Models Marketplace, предоставляя бесплатный доступ к большим языковым моделям (LLM), которые вы будете использовать для создания AI-агентов.

Чтобы использовать GitHub Models, вам нужно создать [персональный токен доступа GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Это можно сделать, перейдя в <a href="https://github.com/settings/personal-access-tokens" target="_blank">настройки персональных токенов доступа</a> в вашем аккаунте GitHub.

Пожалуйста, следуйте [принципу минимальных привилегий](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) при создании токена. Это означает, что вы должны предоставить токену только те разрешения, которые необходимы для выполнения примеров кода в этом курсе.

1. Выберите опцию `Fine-grained tokens` на левой стороне экрана, перейдя в **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.ru.png)

    Затем выберите `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.ru.png)

2. Введите описательное имя для вашего токена, которое отражает его назначение, чтобы его было легко идентифицировать позже.

    🔐 Рекомендация по сроку действия токена

    Рекомендуемый срок действия: 30 дней.
    Для большей безопасности можно выбрать более короткий период — например, 7 дней 🛡️.
    Это отличный способ установить личную цель и завершить курс, пока ваша мотивация на высоте 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.ru.png)

3. Ограничьте область действия токена вашим форком этого репозитория.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.ru.png)

4. Ограничьте разрешения токена: в разделе **Permissions** нажмите вкладку **Account**, затем кнопку "+ Add permissions". Появится выпадающее меню. Найдите **Models** и поставьте галочку.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.ru.png)

5. Проверьте необходимые разрешения перед созданием токена. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.ru.png)

6. Перед созданием токена убедитесь, что вы готовы сохранить его в безопасном месте, например, в хранилище паролей, так как он больше не будет отображаться после создания. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.ru.png)

Скопируйте ваш новый токен, который вы только что создали. Теперь добавьте его в файл `.env`, включенный в этот курс.

### Шаг 2: Создайте файл `.env`

Чтобы создать файл `.env`, выполните следующую команду в терминале.

```bash
cp .env.example .env
```

Это скопирует пример файла и создаст `.env` в вашей директории, где вы заполните значения для переменных окружения.

Скопировав ваш токен, откройте файл `.env` в вашем любимом текстовом редакторе и вставьте ваш токен в поле `GITHUB_TOKEN`.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.ru.png)

Теперь вы сможете запускать примеры кода из этого курса.

## Настройка для примеров с использованием Azure AI Foundry и Azure AI Agent Service

### Шаг 1: Получите конечную точку вашего проекта Azure

Следуйте инструкциям по созданию хаба и проекта в Azure AI Foundry, которые можно найти здесь: [Обзор ресурсов хаба](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources).

После создания проекта вам нужно будет получить строку подключения для вашего проекта.

Это можно сделать, перейдя на страницу **Overview** вашего проекта в портале Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.ru.png)

### Шаг 2: Создайте файл `.env`

Чтобы создать файл `.env`, выполните следующую команду в терминале.

```bash
cp .env.example .env
```

Это скопирует пример файла и создаст `.env` в вашей директории, где вы заполните значения для переменных окружения.

Скопировав ваш токен, откройте файл `.env` в вашем любимом текстовом редакторе и вставьте ваш токен в поле `PROJECT_ENDPOINT`.

### Шаг 3: Войдите в Azure

В целях безопасности мы будем использовать [аутентификацию без ключа](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) для аутентификации в Azure OpenAI с помощью Microsoft Entra ID. 

Далее откройте терминал и выполните команду `az login --use-device-code`, чтобы войти в ваш аккаунт Azure.

После входа в систему выберите вашу подписку в терминале.

## Дополнительные переменные окружения - Azure Search и Azure OpenAI 

Для урока Agentic RAG - Урок 5 - есть примеры, которые используют Azure Search и Azure OpenAI.

Если вы хотите запустить эти примеры, вам нужно будет добавить следующие переменные окружения в ваш файл `.env`:

### Страница обзора (Project)

- `AZURE_SUBSCRIPTION_ID` - Проверьте **Project details** на странице **Overview** вашего проекта.

- `AZURE_AI_PROJECT_NAME` - Посмотрите в верхней части страницы **Overview** вашего проекта.

- `AZURE_OPENAI_SERVICE` - Найдите это на вкладке **Included capabilities** для **Azure OpenAI Service** на странице **Overview**.

### Центр управления

- `AZURE_OPENAI_RESOURCE_GROUP` - Перейдите в **Project properties** на странице **Overview** в **Management Center**.

- `GLOBAL_LLM_SERVICE` - В разделе **Connected resources** найдите имя подключения **Azure AI Services**. Если не указано, проверьте **Azure portal** в вашей группе ресурсов для имени ресурса AI Services.

### Страница моделей + конечных точек

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Выберите вашу модель встраивания (например, `text-embedding-ada-002`) и запишите **Deployment name** из деталей модели.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Выберите вашу модель чата (например, `gpt-4o-mini`) и запишите **Deployment name** из деталей модели.

### Портал Azure

- `AZURE_OPENAI_ENDPOINT` - Найдите **Azure AI services**, нажмите на него, затем перейдите в **Resource Management**, **Keys and Endpoint**, прокрутите вниз до "Azure OpenAI endpoints" и скопируйте тот, который называется "Language APIs".

- `AZURE_OPENAI_API_KEY` - На том же экране скопируйте KEY 1 или KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Найдите ваш ресурс **Azure AI Search**, нажмите на него и посмотрите **Overview**.

- `AZURE_SEARCH_API_KEY` - Затем перейдите в **Settings**, затем **Keys**, чтобы скопировать основной или вторичный административный ключ.

### Внешняя веб-страница

- `AZURE_OPENAI_API_VERSION` - Посетите страницу [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) в разделе **Latest GA API release**.

### Настройка аутентификации без ключа

Вместо жесткого кодирования ваших учетных данных мы будем использовать подключение без ключа с Azure OpenAI. Для этого мы импортируем `DefaultAzureCredential`, а затем вызовем функцию `DefaultAzureCredential`, чтобы получить учетные данные.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Застряли где-то?
Если у вас возникли проблемы с запуском этой настройки, присоединяйтесь к нашему <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord-сообществу Azure AI</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">создайте запрос</a>.

## Следующий урок

Теперь вы готовы запустить код для этого курса. Приятного изучения мира AI-агентов!

[Введение в AI-агентов и примеры их использования](../01-intro-to-ai-agents/README.md)

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.