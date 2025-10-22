<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:41:15+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "uk"
}
-->
# Посібник із налаштування Azure AI Search

Цей посібник допоможе вам налаштувати Azure AI Search за допомогою порталу Azure. Виконайте наведені нижче кроки, щоб створити та налаштувати службу Azure AI Search.

## Вимоги

Перед початком переконайтеся, що у вас є:

- Підписка Azure. Якщо у вас немає підписки Azure, ви можете створити безкоштовний обліковий запис на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Крок 1: Створення служби Azure AI Search

1. Увійдіть у [Azure портал](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. У лівій навігаційній панелі натисніть **Create a resource**.
3. У полі пошуку введіть "Azure AI Search" і виберіть **Azure AI Search** зі списку результатів.
4. Натисніть кнопку **Create**.
5. На вкладці **Basics** заповніть наступну інформацію:
   - **Subscription**: Виберіть вашу підписку Azure.
   - **Resource group**: Створіть нову групу ресурсів або виберіть існуючу.
   - **Resource name**: Введіть унікальне ім’я для вашої служби пошуку.
   - **Region**: Виберіть регіон, найближчий до ваших користувачів.
   - **Pricing tier**: Оберіть тарифний план, який відповідає вашим потребам. Для тестування можна почати з безкоштовного тарифу.
6. Натисніть **Review + create**.
7. Перевірте налаштування та натисніть **Create** для створення служби пошуку.

## Крок 2: Початок роботи з Azure AI Search

1. Після завершення розгортання перейдіть до вашої служби пошуку в порталі Azure.
2. На сторінці огляду служби пошуку натисніть кнопку **Quickstart**.
3. Виконуйте кроки в посібнику Quickstart, щоб створити індекс, завантажити дані та виконати пошуковий запит.

### Створення індексу

1. У посібнику Quickstart натисніть **Create an index**.
2. Визначте схему індексу, вказавши поля та їхні атрибути (наприклад, тип даних, можливість пошуку, фільтрації).
3. Натисніть **Create** для створення індексу.

### Завантаження даних

1. У посібнику Quickstart натисніть **Upload data**.
2. Виберіть джерело даних (наприклад, Azure Blob Storage, Azure SQL Database) і надайте необхідні дані для підключення.
3. Відобразіть поля джерела даних на поля індексу.
4. Натисніть **Submit** для завантаження даних до індексу.

### Виконання пошукового запиту

1. У посібнику Quickstart натисніть **Search explorer**.
2. Введіть пошуковий запит у поле пошуку, щоб перевірити функціональність пошуку.
3. Перегляньте результати пошуку та за потреби відкоригуйте схему індексу або дані.

## Крок 3: Використання інструментів Azure AI Search

Azure AI Search інтегрується з різними інструментами для розширення можливостей пошуку. Ви можете використовувати Azure CLI, Python SDK та інші інструменти для просунутих налаштувань і операцій.

### Використання Azure CLI

1. Встановіть Azure CLI, дотримуючись інструкцій на сторінці [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Увійдіть в Azure CLI за допомогою команди:
   ```bash
   az login
   ```
3. Створіть нову службу пошуку за допомогою Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Створіть індекс за допомогою Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Використання Python SDK

1. Встановіть бібліотеку клієнта Azure Cognitive Search для Python:
   ```bash
   pip install azure-search-documents
   ```
2. Використайте наступний код на Python для створення індексу та завантаження документів:
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

Для детальнішої інформації звертайтеся до наступної документації:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Висновок

Ви успішно налаштували Azure AI Search за допомогою порталу Azure та інтегрованих інструментів. Тепер ви можете досліджувати більш просунуті функції та можливості Azure AI Search для покращення ваших пошукових рішень.

Для додаткової допомоги відвідайте [документацію Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.