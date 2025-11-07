<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:22:42+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "es"
}
-->
# Guía de configuración de Azure AI Search

Esta guía te ayudará a configurar Azure AI Search utilizando el portal de Azure. Sigue los pasos a continuación para crear y configurar tu servicio de Azure AI Search.

## Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente:

- Una suscripción de Azure. Si no tienes una suscripción de Azure, puedes crear una cuenta gratuita en [Cuenta gratuita de Azure](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Paso 1: Crear una cuenta de almacenamiento de Azure

1. Sigue estas instrucciones, [Crear una cuenta de almacenamiento de Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), para crear una nueva cuenta de almacenamiento de Azure.  
   **NOTE**: Asegúrate de que el tipo de cuenta de almacenamiento sea Standard General Purpose V2.

## Paso 2: Crear un servicio de Azure AI Search

1. Inicia sesión en el [portal de Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. En el panel de navegación izquierdo, haz clic en **Crear un recurso**.
3. En el cuadro de búsqueda, escribe "Azure AI Search" y selecciona **Azure AI Search** de la lista de resultados.
4. Haz clic en el botón **Crear**.
5. En la pestaña **Básicos**, proporciona la siguiente información:
   - **Suscripción**: Selecciona tu suscripción de Azure.
   - **Grupo de recursos**: Crea un nuevo grupo de recursos o selecciona uno existente.
   - **Nombre del recurso**: Ingresa un nombre único para tu servicio de búsqueda.
   - **Región**: Selecciona la región más cercana a tus usuarios.
   - **Nivel de precios**: Elige un nivel de precios que se ajuste a tus necesidades. Puedes comenzar con el nivel gratuito para pruebas.
6. Haz clic en **Revisar + crear**.
7. Revisa la configuración y haz clic en **Crear** para crear el servicio de búsqueda.

## Paso 3: Comenzar con Azure AI Search

1. Una vez que se complete la implementación, navega a tu servicio de búsqueda en el portal de Azure.
2. En el panel de vista general del servicio de búsqueda, copia la URL. Debería verse como `https://<service-name>.search.windows.net`.
3. En Configuración > Claves, copia la clave de consulta.
4. Sigue los pasos en la página [Guía de inicio rápido](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) para crear un índice, cargar datos y realizar una consulta de búsqueda.

## Paso 4: Usar herramientas de Azure AI Search

Azure AI Search se integra con varias herramientas para mejorar tus capacidades de búsqueda. Puedes usar Azure CLI, Python SDK, .NET SDK y otras herramientas para configuraciones y operaciones avanzadas.

### Usando Azure CLI

1. Instala Azure CLI siguiendo las instrucciones en [Instalar Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Inicia sesión en Azure CLI usando el comando:

   ```bash
   az login
   ```

3. Almacena tanto el endpoint como la clave API de la instancia de Azure AI Search en variables de entorno.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Usando Python SDK

1. Instala la biblioteca cliente de Azure Cognitive Search para Python:

   ```bash
   pip install azure-search-documents
   ```

2. Usa el siguiente código en Python para crear un índice y cargar documentos:

    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = "sample-index"

    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(service_endpoint, credential)

    fields = [
        SimpleField(name="id", type=edm.String, key=True),
        SimpleField(name="content", type=edm.String, searchable=True),
    ]

    index = SearchIndex(name=index_name, fields=fields)

    index_client.create_index(index)

    search_client = SearchClient(service_endpoint, index_name, credential)

    documents = [
        {"id": "1", "content": "Hello world"},
        {"id": "2", "content": "Azure Cognitive Search"}
    ]

    search_client.upload_documents(documents)
    ```

### Usando .NET SDK

1. Ejecuta el siguiente comando para crear un índice y cargar documentos:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Aquí está el código .NET de `AzureSearch.cs`:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:property PublishAot=false

    using Azure;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var apiKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!;
    var indexName = "sample-index";

    var credential = new AzureKeyCredential(apiKey);
    var indexClient = new SearchIndexClient(serviceEndpoint, credential);

    var fields = new List<SearchField>()
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    };

    var index = new SearchIndex(name: indexName, fields: fields);

    var response = await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{response.Value.Name}' ready.");

    var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

    var documents = new[]
    {
        new { id = "1", content = "Hello world" },
        new { id = "2", content = "Azure Cognitive Search" }
    };

    var result = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {result.Value.Results.Count} documents to index '{response.Value.Name}'.");
    ```

Para obtener información más detallada, consulta la siguiente documentación:

- [Crear un servicio de Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Comenzar con Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Herramientas de Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusión

Has configurado exitosamente Azure AI Search utilizando el portal de Azure e integrado herramientas. Ahora puedes explorar características y capacidades más avanzadas de Azure AI Search para mejorar tus soluciones de búsqueda.

Para obtener más ayuda, visita la [documentación de Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.