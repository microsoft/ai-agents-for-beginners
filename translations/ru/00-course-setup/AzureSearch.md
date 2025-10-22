<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:33:17+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ru"
}
-->
# Руководство по настройке Azure AI Search

Это руководство поможет вам настроить Azure AI Search через портал Azure. Следуйте приведённым ниже шагам, чтобы создать и сконфигурировать службу Azure AI Search.

## Требования

Перед началом убедитесь, что у вас есть:

- Подписка Azure. Если у вас нет подписки, вы можете создать бесплатный аккаунт на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Шаг 1: Создание службы Azure AI Search

1. Войдите в [портал Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. В левой панели навигации нажмите **Создать ресурс**.
3. В строке поиска введите "Azure AI Search" и выберите **Azure AI Search** из списка результатов.
4. Нажмите кнопку **Создать**.
5. На вкладке **Основные** заполните следующие поля:
   - **Подписка**: выберите вашу подписку Azure.
   - **Группа ресурсов**: создайте новую группу ресурсов или выберите существующую.
   - **Имя ресурса**: введите уникальное имя для вашей службы поиска.
   - **Регион**: выберите регион, ближайший к вашим пользователям.
   - **Тарифный план**: выберите подходящий тариф. Для тестирования можно начать с бесплатного тарифа.
6. Нажмите **Проверить + создать**.
7. Проверьте настройки и нажмите **Создать** для создания службы поиска.

## Шаг 2: Начало работы с Azure AI Search

1. После завершения развертывания перейдите к вашей службе поиска в портале Azure.
2. На странице обзора службы поиска нажмите кнопку **Быстрый старт**.
3. Следуйте инструкциям в руководстве Быстрого старта, чтобы создать индекс, загрузить данные и выполнить поисковый запрос.

### Создание индекса

1. В руководстве Быстрого старта нажмите **Создать индекс**.
2. Определите схему индекса, указав поля и их атрибуты (например, тип данных, возможность поиска, фильтрации).
3. Нажмите **Создать** для создания индекса.

### Загрузка данных

1. В руководстве Быстрого старта нажмите **Загрузить данные**.
2. Выберите источник данных (например, Azure Blob Storage, Azure SQL Database) и укажите необходимые параметры подключения.
3. Сопоставьте поля источника данных с полями индекса.
4. Нажмите **Отправить** для загрузки данных в индекс.

### Выполнение поискового запроса

1. В руководстве Быстрого старта нажмите **Обозреватель поиска**.
2. Введите поисковый запрос в строку поиска, чтобы проверить работу поиска.
3. Просмотрите результаты и при необходимости скорректируйте схему индекса или данные.

## Шаг 3: Использование инструментов Azure AI Search

Azure AI Search интегрируется с различными инструментами для расширения возможностей поиска. Вы можете использовать Azure CLI, Python SDK и другие инструменты для продвинутой настройки и управления.

### Использование Azure CLI

1. Установите Azure CLI, следуя инструкциям на странице [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Войдите в Azure CLI с помощью команды:
   ```bash
   az login
   ```
3. Создайте новую службу поиска с помощью Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Создайте индекс с помощью Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Использование Python SDK

1. Установите клиентскую библиотеку Azure Cognitive Search для Python:
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

Для более подробной информации обратитесь к следующей документации:

- [Создание службы Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Начало работы с Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Инструменты Azure AI Search](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Заключение

Вы успешно настроили Azure AI Search через портал Azure и интегрированные инструменты. Теперь вы можете изучать более продвинутые функции и возможности Azure AI Search для улучшения ваших поисковых решений.

Для дополнительной помощи посетите [документацию Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.