<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:47:30+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sk"
}
-->
# Príručka na nastavenie Azure AI Search

Táto príručka vám pomôže nastaviť Azure AI Search pomocou portálu Azure. Postupujte podľa krokov nižšie na vytvorenie a konfiguráciu vašej služby Azure AI Search.

## Predpoklady

Pred začiatkom sa uistite, že máte nasledovné:

- Predplatné Azure. Ak nemáte predplatné Azure, môžete si vytvoriť bezplatný účet na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Krok 1: Vytvorenie účtu Azure Storage

1. Postupujte podľa pokynov na stránke [Vytvorenie účtu Azure Storage](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), aby ste vytvorili nový účet Azure Storage.
   **NOTE**: Uistite sa, že typ účtu Storage je Standard General Purpose V2.

## Krok 2: Vytvorenie služby Azure AI Search

1. Prihláste sa do [portálu Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V navigačnom paneli na ľavej strane kliknite na **Vytvoriť zdroj**.
3. Do vyhľadávacieho poľa zadajte "Azure AI Search" a vyberte **Azure AI Search** zo zoznamu výsledkov.
4. Kliknite na tlačidlo **Vytvoriť**.
5. Na karte **Základy** zadajte nasledujúce informácie:
   - **Predplatné**: Vyberte svoje predplatné Azure.
   - **Skupina zdrojov**: Vytvorte novú skupinu zdrojov alebo vyberte existujúcu.
   - **Názov zdroja**: Zadajte jedinečný názov pre vašu službu vyhľadávania.
   - **Región**: Vyberte región najbližší vašim používateľom.
   - **Úroveň cien**: Vyberte úroveň cien, ktorá vyhovuje vašim požiadavkám. Na testovanie môžete začať s bezplatnou úrovňou.
6. Kliknite na **Skontrolovať + vytvoriť**.
7. Skontrolujte nastavenia a kliknite na **Vytvoriť**, aby ste vytvorili službu vyhľadávania.

## Krok 3: Začnite s Azure AI Search

1. Po dokončení nasadenia prejdite na svoju službu vyhľadávania v portáli Azure.
2. Na prehľadovom paneli služby vyhľadávania skopírujte URL adresu. Mala by vyzerať ako `https://<service-name>.search.windows.net`.
3. Na karte Nastavenia > Kľúče skopírujte kľúč pre dotazy.
4. Postupujte podľa krokov na stránke [Rýchly štart](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), aby ste vytvorili index, nahrali údaje a vykonali dotaz na vyhľadávanie.

## Krok 4: Použitie nástrojov Azure AI Search

Azure AI Search sa integruje s rôznymi nástrojmi na zlepšenie vašich možností vyhľadávania. Môžete použiť Azure CLI, Python SDK, .NET SDK a ďalšie nástroje na pokročilé konfigurácie a operácie.

### Použitie Azure CLI

1. Nainštalujte Azure CLI podľa pokynov na stránke [Inštalácia Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prihláste sa do Azure CLI pomocou príkazu:

   ```bash
   az login
   ```

3. Uložte endpoint a API kľúč pre inštanciu Azure AI Search do environmentálnych premenných.

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

### Použitie Python SDK

1. Nainštalujte knižnicu klienta Azure Cognitive Search pre Python:

   ```bash
   pip install azure-search-documents
   ```

2. Použite nasledujúci Python kód na vytvorenie indexu a nahranie dokumentov:

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

### Použitie .NET SDK

1. Spustite nasledujúci príkaz na vytvorenie indexu a nahranie dokumentov:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Tu je .NET kód `AzureSearch.cs`:

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

Pre podrobnejšie informácie si pozrite nasledujúcu dokumentáciu:

- [Vytvorenie služby Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Začnite s Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Nástroje Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Záver

Úspešne ste nastavili Azure AI Search pomocou portálu Azure a integrovaných nástrojov. Teraz môžete preskúmať pokročilé funkcie a možnosti Azure AI Search na zlepšenie vašich riešení vyhľadávania.

Pre ďalšiu pomoc navštívte [dokumentáciu Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.