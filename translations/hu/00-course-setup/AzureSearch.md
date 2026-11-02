# Azure AI Search Telepítési Útmutató

Ez az útmutató segít az Azure AI Search beállításában az Azure portál használatával. Kövesse az alábbi lépéseket az Azure AI Search szolgáltatás létrehozásához és konfigurálásához.

## Előfeltételek

Mielőtt elkezdené, győződjön meg arról, hogy a következőkkel rendelkezik:

- Egy Azure-előfizetés. Ha nincs Azure-előfizetése, ingyenes fiókot hozhat létre a [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) oldalon.

## 1. lépés: Hozzon létre egy Azure Storage fiókot

1. Kövesse ezt az utasítást, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), hogy létrehozzon egy új Azure Storage fiókot.
   **MEGJEGYZÉS**: Győződjön meg róla, hogy a Storage Account típusa Standard General Purpose V2 legyen.

## 2. lépés: Hozzon létre egy Azure AI Search szolgáltatást

1. Jelentkezzen be az [Azure portálra](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. A bal oldali navigációs panelen kattintson a **Create a resource** lehetőségre.
3. A keresőmezőbe írja be, hogy "Azure AI Search", majd válassza ki az **Azure AI Search** elemet az eredmények közül.
4. Kattintson a **Create** gombra.
5. Az **Alapok** fülön adja meg a következő információkat:
   - **Subscription**: Válassza ki az Azure-előfizetését.
   - **Resource group**: Hozzon létre egy új erőforráscsoportot, vagy válasszon ki egy meglévőt.
   - **Resource name**: Adjon meg egy egyedi nevet a keresési szolgáltatásnak.
   - **Region**: Válassza ki a felhasználóihoz legközelebbi régiót.
   - **Pricing tier**: Válasszon egy díjszabási szintet, amely megfelel az igényeinek. Teszteléshez használhatja az ingyenes szintet.
6. Kattintson a **Review + create** gombra.
7. Ellenőrizze a beállításokat, majd kattintson a **Create** gombra a keresési szolgáltatás létrehozásához.

## 3. lépés: Kezdje el használni az Azure AI Search-t

1. A telepítés befejezése után navigáljon a keresési szolgáltatásához az Azure portálon.
2. A keresési szolgáltatás áttekintő paneljén másolja ki az URL-t. Ez így néz ki: `https://<service-name>.search.windows.net`.
3. **(Ajánlott)** Engedélyezze a kulcs nélküli hozzáférést Microsoft Entra ID-vel (RBAC), az alábbi 4. lépés szerint — kulcs nem szükséges. Az útmutatóban található példák indexeket hoznak létre/frissítenek és dokumentumokat töltenek fel, amelyekhez szükséges a **Search Service Contributor** és **Search Index Data Contributor** szerepkörök (vagy kulcs alapú hitelesítés esetén a **primary admin key** — nem a lekérdezési kulcs). Csak ha nem tudja használni az RBAC-ot, nyissa meg a **Settings > Keys** panelt és másolja ki a **primary admin key**-t.
4. Kövesse a [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) lépéseit egy index létrehozásához, adatok feltöltéséhez és keresés végrehajtásához.

## 4. lépés: Használja az Azure AI Search eszközöket

Az Azure AI Search különböző eszközökkel integrálódik, hogy növelje a keresési képességeit. Használhatja az Azure CLI-t, a Python SDK-t, a .NET SDK-t és más eszközöket fejlettebb konfigurációk és műveletek elvégzéséhez.

### Azure CLI használata

1. Telepítse az Azure CLI-t az utasítások szerint a [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) oldalon.
2. Jelentkezzen be az Azure CLI-be a következő paranccsal:

   ```bash
   az login
   ```
3. **(Ajánlott) Engedélyezze a kulcs nélküli hozzáférést Microsoft Entra ID-vel (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Az RBAC engedélyezésével az alábbi Python és .NET SDK minták `DefaultAzureCredential`-t használnak hitelesítésre, amely a helyi fejlesztés során az `az login` munkamenetet használja — adminisztrátori kulcs nem szükséges. Lásd: [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Tartalék) Kulcs alapú hitelesítés** — csak ha nem tudja használni az RBAC-ot, akkor tárolja a felügyelői kulcsot is:

#### Tárolja az Azure AI Search végpontját és API-kulcsát környezeti változóként.

   * **zsh / bash**
     ```bash
     # az search service show has no "endpoint" field; build the URL from the service name.
     export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
     export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

   * **PowerShell**
     ```powershell
     # az search service show has no "endpoint" field; build the URL from the service name.
     $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
     $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

### Python SDK használata

1. Telepítse az Azure Cognitive Search klienskönyvtárat és az Azure Identity-t Pythonhoz:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Használja az alábbi Python kódot index létrehozására és dokumentumok feltöltésére:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    # Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    credential = DefaultAzureCredential()
    # Fallback (key-based auth):
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

### .NET SDK használata

1. Futtassa az alábbi parancsot index létrehozására és dokumentumok feltöltésére:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Az alábbi .NET minta az `DefaultAzureCredential`-at használja, amely képes használni az Azure CLI bejelentkezését `az login` alatt helyi fejlesztéskor.

2. Itt található az `AzureSearch.cs` .NET kódja:

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

Részletesebb információkért tekintse meg az alábbi dokumentációkat:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Összegzés

Sikeresen beállította az Azure AI Search szolgáltatást az Azure portál használatával és integrált eszközökkel. Most már felfedezheti az Azure AI Search fejlettebb funkcióit és képességeit, hogy fokozza keresési megoldásait.

További segítségért látogasson el az [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) oldalra.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->