# Azure AI Keresés Beállítási Útmutató

Ez az útmutató segít az Azure AI Keresés beállításában az Azure portál használatával. Kövesse az alábbi lépéseket az Azure AI Keresési szolgáltatás létrehozásához és konfigurálásához.

## Előfeltételek

Mielőtt elkezdené, győződjön meg arról, hogy rendelkezik a következőkkel:

- Egy Azure előfizetés. Ha nincs Azure előfizetése, létrehozhat egy ingyenes fiókot az [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) oldalon.

## 1. lépés: Hozzon létre egy Azure Tárolási Fiókot

1. Kövesse ezt az útmutatót, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), hogy létrehozzon egy új Azure Tárolási Fiókot.
   **MEGJEGYZÉS**: Győződjön meg arról, hogy a Tárolási Fiók típusa Standard General Purpose V2 legyen.

## 2. lépés: Hozzon létre egy Azure AI Keresési Szolgáltatást

1. Jelentkezzen be az [Azure portálra](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. A bal oldali navigációs panelen kattintson a **Create a resource** lehetőségre.
3. A keresőmezőbe írja be, hogy "Azure AI Search", majd válassza ki az eredmények közül az **Azure AI Search** szolgáltatást.
4. Kattintson a **Create** gombra.
5. Az **Alapadatok** lapon adja meg a következő adatokat:
   - **Előfizetés**: Válassza ki Azure előfizetését.
   - **Erőforráscsoport**: Hozzon létre új erőforráscsoportot vagy válasszon ki egy meglévőt.
   - **Erőforrás neve**: Adjon meg egy egyedi nevet a keresési szolgáltatásnak.
   - **Régió**: Válassza ki a felhasználóihoz legközelebbi régiót.
   - **Árazási szint**: Válasszon az igényeinek megfelelő árazási szintet. Teszteléshez kezdhet az ingyenes (Free) szinttel.
6. Kattintson a **Review + create** gombra.
7. Tekintse át a beállításokat, majd kattintson a **Create** gombra a keresési szolgáltatás létrehozásához.

## 3. lépés: Kezdje el használni az Azure AI Keresést

1. A telepítés befejezése után navigáljon a keresési szolgáltatásához az Azure portálon.
2. A keresési szolgáltatás áttekintő paneljén másolja ki az URL-t. Ez valahogy így fog kinézni: `https://<service-name>.search.windows.net`.
3. **(Ajánlott)** Engedélyezze a kulcs nélküli hozzáférést Microsoft Entra ID (RBAC) használatával az alábbi 4. lépés szerint — kulcs nem szükséges. Az ebben az útmutatóban szereplő példák indexeket hoznak létre/frissítenek és dokumentumokat töltenek fel, amelyekhez szükség van a **Search Service Contributor** és a **Search Index Data Contributor** szerepkörökre (vagy kulcsalapú hitelesítés esetén a **primary admin key** — nem a query key). Csak ha az RBAC nem használható, nyissa meg a **Settings > Keys** panelt és másolja ki a **primary admin key** kulcsot.
4. Kövesse a [Gyors kezdési útmutató](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) lépéseit az index létrehozásához, adatok feltöltéséhez és keresés végrehajtásához.

## 4. lépés: Használja az Azure AI Keresési Eszközöket

Az Azure AI Keresés különböző eszközökkel integrálódik, hogy bővítse keresési képességeit. Használhatja az Azure CLI-t, Python SDK-t, .NET SDK-t és más eszközöket fejlettebb konfigurációkhoz és műveletekhez.

### Azure CLI használata

1. Telepítse az Azure CLI-t a [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) útmutató szerint.
2. Jelentkezzen be az Azure CLI-be a következő paranccsal:

   ```bash
   az login
   ```
3. **(Ajánlott) Engedélyezze a kulcs nélküli hozzáférést Microsoft Entra ID (RBAC) használatával:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show nem tartalmaz "endpoint" mezőt; építsd fel az URL-t a szolgáltatás neve alapján.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC engedélyezésével az alábbi Python és .NET SDK példák a `DefaultAzureCredential`-t használják, amely a helyi fejlesztés során az `az login` munkamenetét használja — nincs szükség admin kulcsra. Lásd: [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternatíva) Kulcs alapú hitelesítés** — csak ha nem használható RBAC, tárolja az admin kulcsot is:

#### Tárolja az Azure AI Keresési példány végpontját és API kulcsát környezeti változókban.

    ```bash
    # zsh/bash
    # az az search service show parancs nem ad vissza "endpoint" mezőt; az URL-t az erőforrás névből kell összeállítani.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az az search service show parancs nem ad vissza "endpoint" mezőt; az URL-t az erőforrás névből kell összeállítani.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK használata

1. Telepítse az Azure Cognitive Search klienskönyvtárat és az Azure Identity-t Pythonhoz:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Használja a következő Python kódot egy index létrehozásához és dokumentumok feltöltéséhez:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Kulcs nélküli (ajánlott): az az `az login` azonosítóját használja az Entra ID RBAC-on keresztül.
    # Szükséges a "Search Service Contributor" és a "Search Index Data Contributor" szerepkörök.
    credential = DefaultAzureCredential()
    # Tartaléklépés (kulcs alapú hitelesítés):
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

1. Futtassa a következő parancsot egy index létrehozásához és dokumentumok feltöltéséhez:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Az alábbi .NET példa a `DefaultAzureCredential`-t használja, amely az `az login` által biztosított Azure CLI bejelentkezést használhatja helyi fejlesztés során.

2. Íme az `AzureSearch.cs` .NET kódja:

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

Részletesebb információért olvassa el a következő dokumentációt:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Összefoglalás

Sikeresen beállította az Azure AI Keresést az Azure portál használatával és integrált eszközökkel. Most már felfedezheti az Azure AI Keresés fejlettebb funkcióit és képességeit a keresési megoldásai továbbfejlesztéséhez.

További segítségért látogasson el az [Azure Cognitive Search dokumentáció](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) oldalra.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->