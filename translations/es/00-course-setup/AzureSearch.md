# Guía de Configuración de Azure AI Search

Esta guía le ayudará a configurar Azure AI Search usando el portal de Azure. Siga los pasos a continuación para crear y configurar su servicio de Azure AI Search.

## Requisitos Previos

Antes de comenzar, asegúrese de tener lo siguiente:

- Una suscripción de Azure. Si no tiene una suscripción de Azure, puede crear una cuenta gratuita en [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Paso 1: Crear una Cuenta de Almacenamiento de Azure

1. Siga esta instrucción, [Crear una cuenta de almacenamiento de Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), para crear una nueva Cuenta de Almacenamiento de Azure.
   **NOTA**: Asegúrese de que el tipo de Cuenta de Almacenamiento sea Standard General Purpose V2.

## Paso 2: Crear un Servicio de Azure AI Search

1. Inicie sesión en el [portal de Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. En el panel de navegación de la izquierda, haga clic en **Crear un recurso**.
3. En el cuadro de búsqueda, escriba "Azure AI Search" y seleccione **Azure AI Search** de la lista de resultados.
4. Haga clic en el botón **Crear**.
5. En la pestaña **Básicos**, proporcione la siguiente información:
   - **Suscripción**: Seleccione su suscripción de Azure.
   - **Grupo de recursos**: Cree un nuevo grupo de recursos o seleccione uno existente.
   - **Nombre del recurso**: Ingrese un nombre único para su servicio de búsqueda.
   - **Región**: Seleccione la región más cercana a sus usuarios.
   - **Nivel de precios**: Elija un nivel de precios que se ajuste a sus necesidades. Puede comenzar con el nivel gratuito para pruebas.
6. Haga clic en **Revisar y crear**.
7. Revise la configuración y haga clic en **Crear** para crear el servicio de búsqueda.

## Paso 3: Comenzar con Azure AI Search

1. Una vez que se complete la implementación, navegue a su servicio de búsqueda en el portal de Azure.
2. En el panel de resumen del servicio de búsqueda, copie la URL. Debe verse como `https://<nombre-del-servicio>.search.windows.net`.
3. **(Recomendado)** Active el acceso sin clave con Microsoft Entra ID (RBAC) como se muestra en el Paso 4 a continuación; no se necesita clave. Los ejemplos en esta guía crean/actualizan índices y cargan documentos, lo que requiere los roles de **Contribuyente del Servicio de Búsqueda** y **Contribuyente de Datos de Índices de Búsqueda** (o, para autenticación basada en clave, la **clave admin primaria** — no la clave de consulta). Solo si no puede usar RBAC, abra el panel **Configuración > Claves** y copie la **clave admin primaria**.
4. Siga los pasos en la página de la [Guía rápida](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) para crear un índice, cargar datos y realizar una búsqueda.

## Paso 4: Usar las Herramientas de Azure AI Search

Azure AI Search se integra con varias herramientas para mejorar sus capacidades de búsqueda. Puede usar Azure CLI, Python SDK, .NET SDK y otras herramientas para configuraciones y operaciones avanzadas.

### Usando Azure CLI

1. Instale Azure CLI siguiendo las instrucciones en [Instalar Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Inicie sesión en Azure CLI usando el comando:

   ```bash
   az login
   ```
3. **(Recomendado) Active el acceso sin clave con Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show no tiene el campo "endpoint"; construya la URL a partir del nombre del servicio.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Con RBAC activado, los ejemplos de Python y .NET SDK abajo se autentican con `DefaultAzureCredential`, que usa su sesión `az login` durante el desarrollo local — no se necesita clave admin. Consulte [Conectar con Azure AI Search usando roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternativa) Autenticación basada en clave** — solo si no puede usar RBAC, almacene también la clave admin:

#### Almacene tanto el endpoint como la clave API para la instancia de Azure AI Search en variables de entorno.

    ```bash
    # zsh/bash
    # az search service show no tiene el campo "endpoint"; construya la URL desde el nombre del servicio.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<nombre-del-servicio>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <grupo-de-recursos> --service-name <nombre-del-servicio> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show no tiene el campo "endpoint"; construya la URL desde el nombre del servicio.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<nombre-del-servicio>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <grupo-de-recursos> --service-name <nombre-del-servicio> --query "primaryKey" -o tsv)
    ```

### Usando Python SDK

1. Instale la biblioteca cliente de Azure Cognitive Search y Azure Identity para Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Use el siguiente código Python para crear un índice y cargar documentos:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Sin claves (recomendado): usa tu identidad `az login` a través de Entra ID RBAC.
    # Requiere los roles "Colaborador de Servicio de Búsqueda" y "Colaborador de Datos de Índice de Búsqueda".
    credential = DefaultAzureCredential()
    # Alternativa (autenticación basada en clave):
    # from azure.core.credentials import AzureKeyCredential
    # credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

1. Ejecute el siguiente comando para crear un índice y cargar documentos:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    El ejemplo de .NET a continuación usa `DefaultAzureCredential`, que puede usar su inicio de sesión de Azure CLI desde `az login` durante el desarrollo local.

2. Aquí está el código .NET de `AzureSearch.cs`:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:package Azure.Identity@1.21.0
    #:property PublishAot=false

    using Azure;
    using Azure.Identity;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var indexName = "sample-index";

    // Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    // Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    var credential = new DefaultAzureCredential();
    // Fallback (key-based auth): the `using Azure;` directive above already imports
    // AzureKeyCredential; replace the credential line above with:
    // var credential = new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!);
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

Para información más detallada, consulte la siguiente documentación:

- [Crear un servicio de Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Comenzar con Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Herramientas de Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusión

Ha configurado Azure AI Search con éxito usando el portal de Azure y las herramientas integradas. Ahora puede explorar funciones y capacidades más avanzadas de Azure AI Search para mejorar sus soluciones de búsqueda.

Para obtener más ayuda, visite la [documentación de Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->