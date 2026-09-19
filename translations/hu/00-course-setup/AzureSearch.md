# Azure AI Search telepítési útmutató

Ez az útmutató segít az Azure AI Search beállításában az Azure portál használatával. Kövesse az alábbi lépéseket az Azure AI Search szolgáltatás létrehozásához és konfigurálásához.

## Előfeltételek

Mielőtt elkezdené, győződjön meg arról, hogy rendelkezik a következőkkel:

- Egy Azure-előfizetés. Ha még nincs Azure-előfizetése, ingyenes fiókot hozhat létre a [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) oldalon.

## 1. lépés: Azure Storage-fiók létrehozása

1. Kövesse ezt az útmutatót, a [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) oldalt az új Azure Storage-fiók létrehozásához.
   **MEGJEGYZÉS**: Győződjön meg róla, hogy a Storage Account típusa Standard General Purpose V2 legyen.

## 2. lépés: Azure AI Search szolgáltatás létrehozása

1. Jelentkezzen be az [Azure portálra](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. A bal oldali navigációs sávban kattintson a **Create a resource** elemre.
3. A keresőmezőbe írja be, hogy "Azure AI Search", majd válassza ki az **Azure AI Search** elemet az eredmények listájából.
4. Kattintson a **Create** gombra.
5. A **Basics** fülön adja meg a következő információkat:
   - **Subscription**: Válassza ki Azure-előfizetését.
   - **Resource group**: Hozzon létre egy új erőforráscsoportot, vagy válasszon ki egy meglévőt.
   - **Resource name**: Adjon meg egy egyedi nevet keresési szolgáltatásának.
   - **Region**: Válassza ki a felhasználóihoz legközelebbi régiót.
   - **Pricing tier**: Válasszon az igényeinek megfelelő árképzési szintet. Teszteléshez választhatja az ingyenes ("Free") szintet.
6. Kattintson a **Review + create** gombra.
7. Tekintse át a beállításokat, majd kattintson a **Create** gombra a keresési szolgáltatás létrehozásához.

## 3. lépés: Az Azure AI Search használatának megkezdése

1. A telepítés befejezése után lépjen a keresési szolgáltatásához az Azure portálon.
2. A keresési szolgáltatás áttekintő paneljén másolja ki az URL-címet. Ez valahogy így fog kinézni: `https://<service-name>.search.windows.net`.
3. **(Ajánlott)** Engedélyezze a kulcs nélküli hozzáférést Microsoft Entra ID (RBAC) használatával az alábbi 4. lépés szerint — nincs szükség kulcsra. Ez az útmutató példái indexek létrehozását/frissítését és dokumentumok feltöltését végzik, melyekhez szükséges a **Search Service Contributor** és **Search Index Data Contributor** szerepkör (vagy kulcs alapú hitelesítés esetén az **alap admin kulcs** — nem a lekérdezési kulcs). Csak ha nem tud RBAC-ot használni, nyissa meg a **Settings > Keys** panelt, és másolja ki az **alap admin kulcsot**.
4. Kövesse a [Gyors bemutató](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) oldal lépéseit index létrehozásához, adatok feltöltéséhez és kereséshez.

## 4. lépés: Az Azure AI Search eszközök használata

Az Azure AI Search különböző eszközökkel integrálódik, hogy továbbfejlessze keresési képességeit. Használhatja az Azure CLI-t, Python SDK-t, .NET SDK-t és más eszközöket az összetettebb konfigurációkhoz és műveletekhez.

### Azure CLI használata

1. Telepítse az Azure CLI-t a [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) útmutató szerint.
2. Jelentkezzen be az Azure CLI-be az alábbi parancs használatával:

   ```bash
   az login
   ```
3. **(Ajánlott) Engedélyezze a kulcs nélküli hozzáférést Microsoft Entra ID (RBAC) használatával:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # Az kereső szolgáltatás megjelenítés nem tartalmaz "endpoint" mezőt; az URL-t a szolgáltatás nevéből kell összeállítani.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Az RBAC engedélyezése esetén az alábbi Python és .NET SDK példák `DefaultAzureCredential`-lel hitelesítenek, amely helyi fejlesztés során az `az login` munkamenetet használja — nincs szükség admin kulcsra. Lásd: [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Visszaesésként) Kulcs alapú hitelesítés** — csak ha nem tud RBAC-ot használni, tárolja az admin kulcsot is:

#### Tárolja az Azure AI Search végpont és API kulcsát környezeti változóként.

    ```bash
    # zsh/bash
    # az az search service show parancsnak nincs "endpoint" mezője; az URL-t a szolgáltatás neve alapján kell felépíteni.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az az search service show parancsnak nincs "endpoint" mezője; az URL-t a szolgáltatás neve alapján kell felépíteni.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK használata

1. Telepítse az Azure Cognitive Search klienskönyvtárat és az Azure Identity könyvtárat Pythonhoz:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. A következő Python kód segítségével hozzon létre egy indexet és töltsön fel dokumentumokat:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Kulcs nélküli (ajánlott): az `az login` azonosítóját használja az Entra ID RBAC-on keresztül.
    # Szükség van a "Search Service Contributor" és a "Search Index Data Contributor" szerepkörökre.
    credential = DefaultAzureCredential()
    # Visszaesés (kulcs alapú hitelesítés):
    # az azure.core.credentials importálja az AzureKeyCredential-t
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

1. Futtassa a következő parancsot az index létrehozásához és dokumentumok feltöltéséhez:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Az alábbi .NET példa `DefaultAzureCredential`-t használ, amely helyi fejlesztés során az `az login` Azure CLI-be való bejelentkezését tudja használni.

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

Részletesebb információért tekintse meg az alábbi dokumentációkat:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Összegzés

Sikeresen beállította az Azure AI Search szolgáltatást az Azure portál és integrált eszközök segítségével. Most már felfedezheti az Azure AI Search fejlettebb funkcióit és képességeit, hogy továbbfejlessze keresési megoldásait.

További segítségért látogasson el az [Azure Cognitive Search dokumentáció](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) oldalra.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->