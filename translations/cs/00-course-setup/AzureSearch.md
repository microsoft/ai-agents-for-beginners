<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:46:50+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "cs"
}
-->
# Průvodce nastavením Azure AI Search

Tento průvodce vám pomůže nastavit Azure AI Search pomocí portálu Azure. Postupujte podle níže uvedených kroků pro vytvoření a konfiguraci služby Azure AI Search.

## Předpoklady

Než začnete, ujistěte se, že máte následující:

- Předplatné Azure. Pokud nemáte předplatné Azure, můžete si vytvořit bezplatný účet na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Krok 1: Vytvoření účtu Azure Storage

1. Postupujte podle pokynů na stránce [Vytvoření účtu Azure Storage](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) pro vytvoření nového účtu Azure Storage.
   **NOTE**: Ujistěte se, že typ účtu Storage je Standard General Purpose V2.

## Krok 2: Vytvoření služby Azure AI Search

1. Přihlaste se do [portálu Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V levém navigačním panelu klikněte na **Vytvořit prostředek**.
3. Do vyhledávacího pole zadejte "Azure AI Search" a vyberte **Azure AI Search** ze seznamu výsledků.
4. Klikněte na tlačítko **Vytvořit**.
5. Na kartě **Základy** zadejte následující informace:
   - **Předplatné**: Vyberte své předplatné Azure.
   - **Skupina prostředků**: Vytvořte novou skupinu prostředků nebo vyberte existující.
   - **Název prostředku**: Zadejte jedinečný název pro svou službu vyhledávání.
   - **Region**: Vyberte region nejbližší vašim uživatelům.
   - **Úroveň cen**: Vyberte úroveň cen, která vyhovuje vašim požadavkům. Pro testování můžete začít s bezplatnou úrovní.
6. Klikněte na **Zkontrolovat a vytvořit**.
7. Zkontrolujte nastavení a klikněte na **Vytvořit** pro vytvoření služby vyhledávání.

## Krok 3: Začínáme s Azure AI Search

1. Jakmile je nasazení dokončeno, přejděte na svou službu vyhledávání v portálu Azure.
2. Na přehledovém panelu služby vyhledávání zkopírujte URL. Mělo by vypadat jako `https://<service-name>.search.windows.net`.
3. Na panelu Nastavení > Klíče zkopírujte klíč pro dotazy.
4. Postupujte podle kroků na stránce [Průvodce rychlým startem](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) pro vytvoření indexu, nahrání dat a provedení dotazu vyhledávání.

## Krok 4: Použití nástrojů Azure AI Search

Azure AI Search se integruje s různými nástroji pro zlepšení vašich možností vyhledávání. Můžete použít Azure CLI, Python SDK, .NET SDK a další nástroje pro pokročilé konfigurace a operace.

### Použití Azure CLI

1. Nainstalujte Azure CLI podle pokynů na stránce [Instalace Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Přihlaste se do Azure CLI pomocí příkazu:

   ```bash
   az login
   ```

3. Uložte endpoint a API klíč pro instanci Azure AI Search do proměnných prostředí.

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

### Použití Python SDK

1. Nainstalujte klientskou knihovnu Azure Cognitive Search pro Python:

   ```bash
   pip install azure-search-documents
   ```

2. Použijte následující Python kód pro vytvoření indexu a nahrání dokumentů:

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

### Použití .NET SDK

1. Spusťte následující příkaz pro vytvoření indexu a nahrání dokumentů:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Zde je .NET kód `AzureSearch.cs`:

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

Pro podrobnější informace se podívejte na následující dokumentaci:

- [Vytvoření služby Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Začínáme s Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Nástroje Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Závěr

Úspěšně jste nastavili Azure AI Search pomocí portálu Azure a integrovaných nástrojů. Nyní můžete prozkoumat pokročilejší funkce a možnosti Azure AI Search pro zlepšení vašich řešení vyhledávání.

Pro další pomoc navštivte [dokumentaci Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.