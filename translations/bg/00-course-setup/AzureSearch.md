<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:40:08+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "bg"
}
-->
# Ръководство за настройка на Azure AI Search

Това ръководство ще ви помогне да настроите Azure AI Search чрез Azure портала. Следвайте стъпките по-долу, за да създадете и конфигурирате вашата услуга Azure AI Search.

## Предварителни изисквания

Преди да започнете, уверете се, че разполагате със следното:

- Абонамент за Azure. Ако нямате абонамент, можете да създадете безплатен акаунт на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Стъпка 1: Създаване на услуга Azure AI Search

1. Влезте в [Azure портала](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. В лявото навигационно меню кликнете върху **Create a resource**.
3. В полето за търсене въведете "Azure AI Search" и изберете **Azure AI Search** от списъка с резултати.
4. Натиснете бутона **Create**.
5. В раздела **Basics** попълнете следната информация:
   - **Subscription**: Изберете вашия Azure абонамент.
   - **Resource group**: Създайте нова ресурсна група или изберете съществуваща.
   - **Resource name**: Въведете уникално име за вашата търсачна услуга.
   - **Region**: Изберете региона, най-близък до вашите потребители.
   - **Pricing tier**: Изберете ценови план, който отговаря на вашите нужди. Можете да започнете с безплатния план за тестове.
6. Кликнете върху **Review + create**.
7. Прегледайте настройките и натиснете **Create**, за да създадете търсачната услуга.

## Стъпка 2: Започнете работа с Azure AI Search

1. След като разгръщането приключи, отидете на вашата търсачна услуга в Azure портала.
2. В страницата с общ преглед на услугата кликнете върху бутона **Quickstart**.
3. Следвайте стъпките в ръководството Quickstart, за да създадете индекс, качите данни и извършите търсене.

### Създаване на индекс

1. В ръководството Quickstart кликнете върху **Create an index**.
2. Определете схемата на индекса, като посочите полетата и техните атрибути (например тип данни, дали са търсими, филтруеми).
3. Натиснете **Create**, за да създадете индекса.

### Качване на данни

1. В ръководството Quickstart кликнете върху **Upload data**.
2. Изберете източник на данни (например Azure Blob Storage, Azure SQL Database) и въведете необходимите данни за връзка.
3. Свържете полетата от източника на данни с полетата на индекса.
4. Натиснете **Submit**, за да качите данните в индекса.

### Извършване на търсене

1. В ръководството Quickstart кликнете върху **Search explorer**.
2. Въведете заявка за търсене в полето, за да тествате функционалността.
3. Прегледайте резултатите и при необходимост коригирайте схемата на индекса или данните.

## Стъпка 3: Използване на инструментите на Azure AI Search

Azure AI Search се интегрира с различни инструменти, които разширяват възможностите за търсене. Можете да използвате Azure CLI, Python SDK и други инструменти за по-сложни конфигурации и операции.

### Използване на Azure CLI

1. Инсталирайте Azure CLI, като следвате инструкциите на [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Влезте в Azure CLI с командата:
   ```bash
   az login
   ```
3. Създайте нова търсачна услуга чрез Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Създайте индекс чрез Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Използване на Python SDK

1. Инсталирайте библиотеката Azure Cognitive Search за Python:
   ```bash
   pip install azure-search-documents
   ```
2. Използвайте следния Python код, за да създадете индекс и да качите документи:
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

За по-подробна информация, вижте следната документация:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Заключение

Успешно настроихте Azure AI Search чрез Azure портала и интегрираните инструменти. Сега можете да разгледате по-напреднали функции и възможности на Azure AI Search, за да подобрите вашите търсачни решения.

За допълнителна помощ посетете [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.