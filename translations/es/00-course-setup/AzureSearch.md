# Guía de configuración de Azure AI Search

Esta guía te ayudará a configurar Azure AI Search utilizando el portal de Azure. Sigue los pasos a continuación para crear y configurar tu servicio Azure AI Search.

## Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente:

- Una suscripción de Azure. Si no tienes una suscripción de Azure, puedes crear una cuenta gratuita en [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Paso 1: Crear una cuenta de almacenamiento de Azure

1. Sigue esta instrucción, [Crear una cuenta de almacenamiento de Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), para crear una nueva cuenta de almacenamiento de Azure.
   **NOTA**: Asegúrate de que el tipo de cuenta de almacenamiento sea Standard General Purpose V2.

## Paso 2: Crear un servicio Azure AI Search

1. Inicia sesión en el [portal de Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. En el panel de navegación izquierdo, haz clic en **Crear un recurso**.
3. En el cuadro de búsqueda, escribe "Azure AI Search" y selecciona **Azure AI Search** de la lista de resultados.
4. Haz clic en el botón **Crear**.
5. En la pestaña **Básicos**, proporciona la siguiente información:
   - **Suscripción**: Selecciona tu suscripción de Azure.
   - **Grupo de recursos**: Crea un nuevo grupo de recursos o selecciona uno existente.
   - **Nombre del recurso**: Ingresa un nombre único para tu servicio de búsqueda.
   - **Región**: Selecciona la región más cercana a tus usuarios.
   - **Nivel de precios**: Elige un nivel de precios que se adapte a tus necesidades. Puedes comenzar con el nivel Gratis para pruebas.
6. Haz clic en **Revisar y crear**.
7. Revisa la configuración y haz clic en **Crear** para crear el servicio de búsqueda.

## Paso 3: Comenzar con Azure AI Search

1. Una vez que se complete la implementación, navega hasta tu servicio de búsqueda en el portal de Azure.
2. En el panel de descripción general del servicio de búsqueda, copia la URL. Debería ser algo parecido a `https://<service-name>.search.windows.net`.
3. **(Recomendado)** Habilita el acceso sin clave con Microsoft Entra ID (RBAC) como se muestra en el Paso 4 a continuación — no es necesaria ninguna clave. Los ejemplos en esta guía crean/actualizan índices y suben documentos, lo que requiere los roles **Colaborador de servicio de búsqueda** y **Colaborador de datos de índice de búsqueda** (o, para autenticación basada en clave, la **clave de administrador primaria** — no la clave de consultas). Solo si no puedes usar RBAC, abre el panel **Configuración > Claves** y copia la **clave de administrador primaria**.
4. Sigue los pasos en la página de [Guía rápida](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) para crear un índice, subir datos y realizar una búsqueda.

## Paso 4: Usar herramientas de Azure AI Search

Azure AI Search se integra con diversas herramientas para mejorar tus capacidades de búsqueda. Puedes usar Azure CLI, Python SDK, .NET SDK y otras herramientas para configuraciones y operaciones avanzadas.

### Uso de Azure CLI

1. Instala Azure CLI siguiendo las instrucciones en [Instalar Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Inicia sesión en Azure CLI usando el comando:

   ```bash
   az login
   ```
3. **(Recomendado) Habilita el acceso sin clave con Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show no tiene un campo "endpoint"; construya la URL a partir del nombre del servicio.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Con RBAC habilitado, los ejemplos de Python y .NET SDK abajo se autentican con `DefaultAzureCredential`, que usa tu sesión `az login` durante el desarrollo local — no se necesita clave de administrador. Consulta [Conectar con Azure AI Search usando roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternativa) Autenticación basada en clave** — solo si no puedes usar RBAC, guarda la clave de administrador también:

#### Almacena tanto el punto de conexión como la clave API para la instancia de Azure AI Search en variables de entorno.

   * **zsh / bash**
     ```bash
     # az search service show no tiene un campo "endpoint"; construya la URL a partir del nombre del servicio.
     export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
     export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

   * **PowerShell**
     ```powershell
     # az search service show no tiene un campo "endpoint"; construya la URL a partir del nombre del servicio.
     $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
     $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

### Uso del SDK de Python

1. Instala la biblioteca cliente de Azure Cognitive Search y Azure Identity para Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Usa el siguiente código en Python para crear un índice y subir documentos:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Sin clave (recomendado): utiliza tu identidad `az login` a través de RBAC de Entra ID.
    # Requiere los roles "Search Service Contributor" y "Search Index Data Contributor".
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

### Uso del SDK de .NET

1. Ejecuta el siguiente comando para crear un índice y subir documentos:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    El ejemplo de .NET abajo usa `DefaultAzureCredential`, que puede utilizar tu inicio de sesión de Azure CLI desde `az login` durante el desarrollo local.

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

Para información más detallada, consulta la siguiente documentación:

- [Crear un servicio Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Comenzar con Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Herramientas de Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusión

Has configurado exitosamente Azure AI Search utilizando el portal de Azure y las herramientas integradas. Ahora puedes explorar características y capacidades más avanzadas de Azure AI Search para mejorar tus soluciones de búsqueda.

Para obtener más ayuda, visita la [documentación de Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->