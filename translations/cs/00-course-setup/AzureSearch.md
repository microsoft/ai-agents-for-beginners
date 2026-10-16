# Průvodce nastavením Azure AI Search

Tento průvodce vám pomůže nastavit Azure AI Search pomocí Azure portálu. Postupujte podle níže uvedených kroků pro vytvoření a konfiguraci služby Azure AI Search.

## Požadavky

Než začnete, ujistěte se, že máte následující:

- Předplatné Azure. Pokud nemáte předplatné Azure, můžete si vytvořit bezplatný účet na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Krok 1: Vytvoření Azure Storage účtu

1. Postupujte podle tohoto návodu, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), abyste vytvořili nový Azure Storage účet.
   **POZNÁMKA**: Ujistěte se, že typ Storage účtu je Standard General Purpose V2.

## Krok 2: Vytvoření služby Azure AI Search

1. Přihlaste se do [Azure portálu](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V levém navigačním panelu klikněte na **Create a resource**.
3. Do vyhledávacího pole zadejte „Azure AI Search“ a vyberte **Azure AI Search** ze seznamu výsledků.
4. Klikněte na tlačítko **Create**.
5. V záložce **Basics** zadejte následující informace:
   - **Subscription**: Vyberte své Azure předplatné.
   - **Resource group**: Vytvořte novou nebo vyberte existující skupinu prostředků.
   - **Resource name**: Zadejte jedinečný název vaší služby vyhledávání.
   - **Region**: Vyberte oblast, která je nejblíže vašim uživatelům.
   - **Pricing tier**: Zvolte cenovou úroveň, která vyhovuje vašim požadavkům. Pro testování můžete začít s bezplatnou úrovní.
6. Klikněte na **Review + create**.
7. Zkontrolujte nastavení a klikněte na **Create** pro vytvoření služby vyhledávání.

## Krok 3: Začínáme s Azure AI Search

1. Po dokončení nasazení přejděte ke své službě vyhledávání v Azure portálu.
2. V přehledovém panelu služby vyhledávání zkopírujte URL. Mělo by vypadat jako `https://<service-name>.search.windows.net`.
3. **(Doporučeno)** Povolení přístupu bez klíče pomocí Microsoft Entra ID (RBAC) podle kroku 4 níže — není potřeba klíč. Vzory v tomto průvodci vytvářejí/aktualizují indexy a nahrávají dokumenty, což vyžaduje role **Search Service Contributor** a **Search Index Data Contributor** (nebo při autentifikaci na základě klíče **primární administrátorský klíč** — nikoliv dotazovací klíč). Pouze pokud nemůžete použít RBAC, otevřete panel **Settings > Keys** a zkopírujte **primární administrátorský klíč**.
4. Postupujte podle kroků na stránce [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) pro vytvoření indexu, nahrání dat a provedení vyhledávání.

## Krok 4: Používání Azure AI Search nástrojů

Azure AI Search se integruje s různými nástroji pro zlepšení vašich vyhledávacích schopností. Můžete používat Azure CLI, Python SDK, .NET SDK a další nástroje pro pokročilé konfigurace a operace.

### Použití Azure CLI

1. Nainstalujte Azure CLI podle instrukcí na [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Přihlaste se do Azure CLI pomocí příkazu:

   ```bash
   az login
   ```
3. **(Doporučeno) Povolení přístupu bez klíče pomocí Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # služba az search show nemá pole "endpoint"; vytvořte URL z názvu služby.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Pokud je RBAC povoleno, Python a .NET SDK příklady níže autentifikují s `DefaultAzureCredential`, který používá vaši `az login` relaci během lokálního vývoje — není potřeba administrátorský klíč. Viz [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Záložní možnost) Autentifikace na základě klíče** — pouze pokud nelze použít RBAC, uložte také administrátorský klíč:

#### Uložte jak endpoint, tak API klíč instance Azure AI Search do proměnných prostředí.

    ```bash
    # zsh/bash
    # az search service show nemá pole "endpoint"; URL sestavte z názvu služby.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show nemá pole "endpoint"; URL sestavte z názvu služby.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Použití Python SDK

1. Nainstalujte knihovnu Azure Cognitive Search client a Azure Identity pro Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Použijte následující Python kód k vytvoření indexu a nahrání dokumentů:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Bez klíče (doporučeno): používá vaši identitu `az login` přes Entra ID RBAC.
    # Vyžaduje role "Přispěvatel služby vyhledávání" a "Přispěvatel dat indexu vyhledávání".
    credential = DefaultAzureCredential()
    # Náhradní možnost (ověření založené na klíči):
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

### Použití .NET SDK

1. Spusťte následující příkaz pro vytvoření indexu a nahrání dokumentů:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Následující .NET příklad používá `DefaultAzureCredential`, který může používat vaše přihlášení Azure CLI z `az login` během lokálního vývoje.

2. Zde je kód .NET souboru `AzureSearch.cs`:

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

Pro podrobnější informace naleznete v následující dokumentaci:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Závěr

Úspěšně jste nastavili Azure AI Search pomocí Azure portálu a integrovaných nástrojů. Nyní můžete prozkoumat pokročilejší funkce a možnosti Azure AI Search pro zlepšení vašich vyhledávacích řešení.

Pro další pomoc navštivte [dokumentaci Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->