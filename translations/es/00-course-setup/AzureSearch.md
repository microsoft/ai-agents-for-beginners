# Guía de Configuración de Azure AI Search

Esta guía le ayudará a configurar Azure AI Search utilizando el portal de Azure. Siga los pasos a continuación para crear y configurar su servicio Azure AI Search.

## Requisitos Previos

Antes de comenzar, asegúrese de tener lo siguiente:

- Una suscripción de Azure. Si no tiene una suscripción de Azure, puede crear una cuenta gratuita en [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Paso 1: Crear una Cuenta de Almacenamiento de Azure

1. Siga esta instrucción, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), para crear una nueva Cuenta de Almacenamiento de Azure.
   **NOTA**: Asegúrese de que el tipo de Cuenta de Almacenamiento sea Standard General Purpose V2.

## Paso 2: Crear un Servicio Azure AI Search

1. Inicie sesión en el [portal de Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. En el panel de navegación izquierdo, haga clic en **Crear un recurso**.
3. En el cuadro de búsqueda, escriba "Azure AI Search" y seleccione **Azure AI Search** de la lista de resultados.
4. Haga clic en el botón **Crear**.
5. En la pestaña **Básicos**, proporcione la siguiente información:
   - **Suscripción**: Seleccione su suscripción de Azure.
   - **Grupo de recursos**: Cree un nuevo grupo de recursos o seleccione uno existente.
   - **Nombre del recurso**: Ingrese un nombre único para su servicio de búsqueda.
   - **Región**: Seleccione la región más cercana a sus usuarios.
   - **Nivel de precios**: Elija un nivel de precios que se adapte a sus necesidades. Puede comenzar con el nivel Gratis para pruebas.
6. Haga clic en **Revisar + crear**.
7. Revise la configuración y haga clic en **Crear** para crear el servicio de búsqueda.

## Paso 3: Comenzar con Azure AI Search

1. Una vez que la implementación esté completa, navegue a su servicio de búsqueda en el portal de Azure.
2. En el panel de resumen del servicio de búsqueda, copie la URL. Debe tener un formato como `https://<service-name>.search.windows.net`.
3. **(Recomendado)** Habilite el acceso sin clave con Microsoft Entra ID (RBAC) como se muestra en el Paso 4 a continuación — no se necesita clave. Los ejemplos en esta guía crean/actualizan índices y suben documentos, lo que requiere los roles de **Search Service Contributor** y **Search Index Data Contributor** (o, para autenticación basada en clave, la **clave principal de administrador** — no la clave de consulta). Solo si no puede usar RBAC, abra el panel **Configuración > Claves** y copie la **clave principal de administrador**.
4. Siga los pasos en la página de [Guía de inicio rápido](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) para crear un índice, cargar datos y realizar una búsqueda.

## Paso 4: Usar las Herramientas de Azure AI Search

Azure AI Search se integra con diversas herramientas para mejorar sus capacidades de búsqueda. Puede utilizar Azure CLI, SDK para Python, SDK para .NET y otras herramientas para configuraciones y operaciones avanzadas.

### Uso de Azure CLI

1. Instale Azure CLI siguiendo las instrucciones en [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Inicie sesión en Azure CLI usando el comando:

   ```bash
   az login
   ```
3. **(Recomendado) Habilite el acceso sin clave con Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show no tiene un campo "endpoint"; construya la URL a partir del nombre del servicio.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Con RBAC habilitado, los ejemplos de SDK para Python y .NET a continuación autentican con `DefaultAzureCredential`, que usa su sesión de `az login` durante el desarrollo local — no se necesita clave de administrador. Vea [Conectarse a Azure AI Search usando roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternativa) Autenticación basada en clave** — solo si no puede usar RBAC, almacene también la clave de administrador:

#### Almacene tanto el punto de conexión como la clave API de la instancia de Azure AI Search en variables de entorno.

    ```bash
    # zsh/bash
    # az search service show no tiene campo "endpoint"; construya la URL a partir del nombre del servicio.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show no tiene campo "endpoint"; construya la URL a partir del nombre del servicio.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Uso del SDK para Python

1. Instale la biblioteca cliente Azure Cognitive Search y Azure Identity para Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Use el siguiente código Python para crear un índice y subir documentos:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Sin clave (recomendado): utiliza tu identidad de `az login` a través del control de acceso basado en roles (RBAC) de Entra ID.
    # Requiere los roles "Colaborador de servicio de búsqueda" y "Colaborador de datos de índice de búsqueda".
    credential = DefaultAzureCredential()
    # Reserva (autenticación basada en clave):
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

### Uso del SDK para .NET

1. Ejecute el siguiente comando para crear un índice y subir documentos:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    El ejemplo para .NET a continuación utiliza `DefaultAzureCredential`, que puede usar su inicio de sesión de Azure CLI con `az login` durante el desarrollo local.

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

Para obtener información más detallada, consulte la siguiente documentación:

- [Crear un servicio Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Comenzar con Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Herramientas Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusión

Ha configurado exitosamente Azure AI Search utilizando el portal de Azure y las herramientas integradas. Ahora puede explorar funciones y capacidades más avanzadas de Azure AI Search para mejorar sus soluciones de búsqueda.

Para obtener más ayuda, visite la [documentación de Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->