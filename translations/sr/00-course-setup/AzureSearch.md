<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:40:20+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sr"
}
-->
# Azure AI Search Водич за подешавање

Овај водич ће вам помоћи да подесите Azure AI Search користећи Azure портал. Пратите кораке испод да бисте креирали и конфигурисали ваш Azure AI Search сервис.

## Захтеви

Пре него што почнете, уверите се да имате следеће:

- Azure претплату. Ако немате Azure претплату, можете направити бесплатан налог на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Корак 1: Креирање Azure AI Search сервиса

1. Пријавите се на [Azure портал](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. У левом навигационом менију кликните на **Create a resource**.
3. У пољу за претрагу укуцајте "Azure AI Search" и изаберите **Azure AI Search** са листе резултата.
4. Кликните на дугме **Create**.
5. У картици **Basics** унесите следеће информације:
   - **Subscription**: Изаберите вашу Azure претплату.
   - **Resource group**: Креирајте нову ресурсну групу или изаберите постојећу.
   - **Resource name**: Унесите јединствено име за ваш search сервис.
   - **Region**: Изаберите регион најближи вашим корисницима.
   - **Pricing tier**: Изаберите ниво цена који одговара вашим потребама. За тестирање можете почети са Free нивоом.
6. Кликните на **Review + create**.
7. Прегледајте подешавања и кликните на **Create** да бисте креирали search сервис.

## Корак 2: Почетак рада са Azure AI Search

1. Када се имплементација заврши, идите на ваш search сервис у Azure порталу.
2. На страници прегледа search сервиса кликните на дугме **Quickstart**.
3. Пратите кораке у Quickstart водичу да бисте креирали индекс, отпремили податке и извршили претрагу.

### Креирање индекса

1. У Quickstart водичу кликните на **Create an index**.
2. Дефинишите шему индекса тако што ћете одредити поља и њихове атрибуте (нпр. тип података, да ли је претраживо, филтрирано).
3. Кликните на **Create** да бисте креирали индекс.

### Отпремање података

1. У Quickstart водичу кликните на **Upload data**.
2. Изаберите извор података (нпр. Azure Blob Storage, Azure SQL Database) и унесите потребне детаље за повезивање.
3. Мапирајте поља извора података на поља индекса.
4. Кликните на **Submit** да бисте отпремили податке у индекс.

### Извршавање претраге

1. У Quickstart водичу кликните на **Search explorer**.
2. Унесите упит за претрагу у поље за претрагу да бисте тестирали функционалност претраге.
3. Прегледајте резултате претраге и по потреби прилагодите шему индекса или податке.

## Корак 3: Коришћење Azure AI Search алата

Azure AI Search се интегрише са разним алатима како би побољшао ваше могућности претраге. Можете користити Azure CLI, Python SDK и друге алате за напредне конфигурације и операције.

### Коришћење Azure CLI

1. Инсталирајте Azure CLI пратећи упутства на [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Пријавите се у Azure CLI користећи команду:
   ```bash
   az login
   ```
3. Креирајте нови search сервис користећи Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Креирајте индекс користећи Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Коришћење Python SDK

1. Инсталирајте Azure Cognitive Search клијентску библиотеку за Python:
   ```bash
   pip install azure-search-documents
   ```
2. Користите следећи Python код за креирање индекса и отпремање докумената:
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

За детаљније информације, погледајте следећу документацију:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Закључак

Успешно сте подесили Azure AI Search користећи Azure портал и интегрисане алате. Сада можете истраживати напредније функције и могућности Azure AI Search како бисте унапредили ваша решења за претрагу.

За додатну помоћ посетите [Azure Cognitive Search документацију](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.