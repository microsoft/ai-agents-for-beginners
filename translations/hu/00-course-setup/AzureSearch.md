<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:46:08+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "hu"
}
-->
# Azure AI Search Beállítási Útmutató

Ez az útmutató segít az Azure AI Search beállításában az Azure portál használatával. Kövesse az alábbi lépéseket az Azure AI Search szolgáltatás létrehozásához és konfigurálásához.

## Előfeltételek

Mielőtt elkezdené, győződjön meg arról, hogy rendelkezik az alábbiakkal:

- Egy Azure előfizetés. Ha még nincs Azure előfizetése, létrehozhat egy ingyenes fiókot itt: [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## 1. lépés: Hozzon létre egy Azure Storage fiókot

1. Kövesse ezt az útmutatót: [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), hogy létrehozzon egy új Azure Storage fiókot.
   **NOTE**: Győződjön meg arról, hogy a Storage fiók típusa Standard General Purpose V2.

## 2. lépés: Hozzon létre egy Azure AI Search szolgáltatást

1. Jelentkezzen be az [Azure portálra](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. A bal oldali navigációs panelen kattintson a **Create a resource** lehetőségre.
3. A keresőmezőbe írja be az "Azure AI Search" kifejezést, és válassza ki az **Azure AI Search** lehetőséget a találatok listájából.
4. Kattintson a **Create** gombra.
5. A **Basics** fülön adja meg a következő információkat:
   - **Subscription**: Válassza ki az Azure előfizetését.
   - **Resource group**: Hozzon létre egy új erőforráscsoportot, vagy válasszon egy meglévőt.
   - **Resource name**: Adjon meg egy egyedi nevet a keresési szolgáltatásának.
   - **Region**: Válassza ki a felhasználóihoz legközelebbi régiót.
   - **Pricing tier**: Válasszon egy árkategóriát, amely megfelel az igényeinek. Teszteléshez kezdheti az ingyenes csomaggal.
6. Kattintson a **Review + create** gombra.
7. Ellenőrizze a beállításokat, majd kattintson a **Create** gombra a keresési szolgáltatás létrehozásához.

## 3. lépés: Kezdje el az Azure AI Search használatát

1. Miután a telepítés befejeződött, navigáljon a keresési szolgáltatásához az Azure portálon.
2. A keresési szolgáltatás áttekintő paneljén másolja ki az URL-t. Ennek így kell kinéznie: `https://<service-name>.search.windows.net`.
3. A Beállítások > Kulcsok panelen másolja ki a lekérdezési kulcsot.
4. Kövesse a [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) oldalon található lépéseket egy index létrehozásához, adatok feltöltéséhez és keresési lekérdezés végrehajtásához.

## 4. lépés: Használja az Azure AI Search eszközöket

Az Azure AI Search különböző eszközökkel integrálható, hogy javítsa keresési képességeit. Használhatja az Azure CLI-t, a Python SDK-t, a .NET SDK-t és más eszközöket fejlettebb konfigurációkhoz és műveletekhez.

### Azure CLI használata

1. Telepítse az Azure CLI-t az alábbi útmutató követésével: [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Jelentkezzen be az Azure CLI-be az alábbi parancs használatával:

   ```bash
   az login
   ```

3. Tárolja az Azure AI Search példány végpontját és API kulcsát környezeti változókban.

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

### Python SDK használata

1. Telepítse az Azure Cognitive Search klienskönyvtárat Pythonhoz:

   ```bash
   pip install azure-search-documents
   ```

2. Használja az alábbi Python kódot egy index létrehozásához és dokumentumok feltöltéséhez:

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

### .NET SDK használata

1. Futtassa az alábbi parancsot egy index létrehozásához és dokumentumok feltöltéséhez:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Íme a `AzureSearch.cs` .NET kódja:

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

További részletes információért tekintse meg az alábbi dokumentációkat:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Összegzés

Sikeresen beállította az Azure AI Search szolgáltatást az Azure portálon és integrált eszközökkel. Most már felfedezheti az Azure AI Search fejlettebb funkcióit és képességeit, hogy továbbfejlessze keresési megoldásait.

További segítségért látogasson el az [Azure Cognitive Search dokumentáció](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) oldalára.

---

**Felelősségi nyilatkozat**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.