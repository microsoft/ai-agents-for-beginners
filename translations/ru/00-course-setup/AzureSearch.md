<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-11T14:38:28+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ru"
}
-->
# Руководство по настройке Azure AI Search

Это руководство поможет вам настроить Azure AI Search с использованием портала Azure. Следуйте приведенным ниже шагам, чтобы создать и настроить ваш сервис Azure AI Search.

## Предварительные требования

Прежде чем начать, убедитесь, что у вас есть следующее:

- Подписка на Azure. Если у вас нет подписки на Azure, вы можете создать бесплатную учетную запись на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Шаг 1: Создание сервиса Azure AI Search

1. Войдите в [портал Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. В левой панели навигации нажмите на **Создать ресурс**.
3. В строке поиска введите "Azure AI Search" и выберите **Azure AI Search** из списка результатов.
4. Нажмите кнопку **Создать**.
5. На вкладке **Основы** укажите следующую информацию:
   - **Подписка**: Выберите вашу подписку на Azure.
   - **Группа ресурсов**: Создайте новую группу ресурсов или выберите существующую.
   - **Имя ресурса**: Введите уникальное имя для вашего поискового сервиса.
   - **Регион**: Выберите регион, ближайший к вашим пользователям.
   - **Уровень цен**: Выберите уровень цен, который соответствует вашим требованиям. Вы можете начать с бесплатного уровня для тестирования.
6. Нажмите **Проверить и создать**.
7. Проверьте настройки и нажмите **Создать**, чтобы создать поисковый сервис.

## Шаг 2: Начало работы с Azure AI Search

1. После завершения развертывания перейдите к вашему поисковому сервису на портале Azure.
2. На странице обзора поискового сервиса нажмите кнопку **Быстрый старт**.
3. Следуйте шагам в руководстве по быстрому старту, чтобы создать индекс, загрузить данные и выполнить поисковый запрос.

### Создание индекса

1. В руководстве по быстрому старту нажмите на **Создать индекс**.
2. Определите схему индекса, указав поля и их атрибуты (например, тип данных, возможность поиска, возможность фильтрации).
3. Нажмите **Создать**, чтобы создать индекс.

### Загрузка данных

1. В руководстве по быстрому старту нажмите на **Загрузить данные**.
2. Выберите источник данных (например, Azure Blob Storage, Azure SQL Database) и укажите необходимые данные для подключения.
3. Сопоставьте поля источника данных с полями индекса.
4. Нажмите **Отправить**, чтобы загрузить данные в индекс.

### Выполнение поискового запроса

1. В руководстве по быстрому старту нажмите на **Исследователь поиска**.
2. Введите поисковый запрос в строку поиска, чтобы протестировать функциональность поиска.
3. Просмотрите результаты поиска и при необходимости скорректируйте схему индекса или данные.

## Шаг 3: Использование инструментов Azure AI Search

Azure AI Search интегрируется с различными инструментами для расширения ваших возможностей поиска. Вы можете использовать Azure CLI, Python SDK и другие инструменты для продвинутых конфигураций и операций.

### Использование Azure CLI

1. Установите Azure CLI, следуя инструкциям на [Установка Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Войдите в Azure CLI, используя команду:
   ```bash
   az login
   ```
3. Создайте новый поисковый сервис с помощью Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Создайте индекс с помощью Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Использование Python SDK

1. Установите библиотеку клиента Azure Cognitive Search для Python:
   ```bash
   pip install azure-search-documents
   ```
2. Используйте следующий код на Python для создания индекса и загрузки документов:
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

Для получения более подробной информации обратитесь к следующей документации:

- [Создание сервиса Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Начало работы с Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Инструменты Azure AI Search](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Заключение

Вы успешно настроили Azure AI Search с использованием портала Azure и интегрированных инструментов. Теперь вы можете исследовать более продвинутые функции и возможности Azure AI Search для улучшения ваших поисковых решений.

Для получения дополнительной помощи посетите [документацию по Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.