# Sprievodca nastavením Azure AI Search

Tento sprievodca vám pomôže nastaviť Azure AI Search pomocou Azure portálu. Postupujte podľa krokov nižšie na vytvorenie a konfiguráciu vašej služby Azure AI Search.

## Predpoklady

Pred začatím sa uistite, že máte nasledovné:

- Predplatné Azure. Ak nemáte predplatné Azure, môžete si vytvoriť bezplatný účet na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Krok 1: Vytvorenie Azure Storage účtu

1. Postupujte podľa tohto návodu, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), na vytvorenie nového Azure Storage účtu.
   **POZNÁMKA**: Uistite sa, že typ Storage účtu je Standard General Purpose V2.

## Krok 2: Vytvorenie služby Azure AI Search

1. Prihláste sa do [Azure portálu](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V ľavom navigačnom paneli kliknite na **Vytvoriť zdroj**.
3. Do vyhľadávacieho poľa zadajte "Azure AI Search" a vyberte **Azure AI Search** zo zoznamu výsledkov.
4. Kliknite na tlačidlo **Vytvoriť**.
5. V karte **Základy** zadajte nasledujúce informácie:
   - **Predplatné**: Vyberte svoje Azure predplatné.
   - **Skupina zdrojov**: Vytvorte novú skupinu zdrojov alebo vyberte existujúcu.
   - **Názov zdroja**: Zadajte jedinečný názov pre vašu vyhľadávaciu službu.
   - **Región**: Vyberte región najbližší vašim používateľom.
   - **Cenová vrstva**: Vyberte cenovú vrstvu, ktorá vyhovuje vašim požiadavkám. Na testovanie môžete začať s bezplatnou vrstvou.
6. Kliknite na **Skontrolovať + vytvoriť**.
7. Skontrolujte nastavenia a kliknite na **Vytvoriť** na vytvorenie vyhľadávacej služby.

## Krok 3: Začnite s Azure AI Search

1. Po dokončení nasadenia prejdite na vašu vyhľadávaciu službu v Azure portáli.
2. V prehľade vyhľadávacej služby skopírujte URL. Malo by vyzerať ako `https://<service-name>.search.windows.net`.
3. **(Odporúčané)** Povoliť prístup bez kľúča pomocou Microsoft Entra ID (RBAC) ako je uvedené v kroku 4 nižšie — kľúč nie je potrebný. Vzory v tomto návode vytvárajú/aktualizujú indexy a nahrávajú dokumenty, čo vyžaduje roly **Search Service Contributor** a **Search Index Data Contributor** (alebo pri autentifikácii založenej na kľúči, **primárny administrátorský kľúč** — nie dotazovací kľúč). Ak nemôžete použiť RBAC, otvorte panel **Nastavenia > Kľúče** a skopírujte **primárny administrátorský kľúč**.
4. Postupujte podľa krokov na stránke [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) na vytvorenie indexu, nahranie údajov a vykonanie vyhľadávania.

## Krok 4: Použitie nástrojov Azure AI Search

Azure AI Search sa integruje s rôznymi nástrojmi, ktoré vylepšujú vaše vyhľadávacie možnosti. Môžete používať Azure CLI, Python SDK, .NET SDK a ďalšie nástroje na pokročilé konfigurácie a operácie.

### Používanie Azure CLI

1. Nainštalujte Azure CLI podľa pokynov na [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prihláste sa do Azure CLI pomocou príkazu:

   ```bash
   az login
   ```
3. **(Odporúčané) Povoliť prístup bez kľúča pomocou Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    S povoleným RBAC sa Python a .NET SDK príklady nižšie autentifikujú cez `DefaultAzureCredential`, ktorý využíva vašu reláciu `az login` počas lokálneho vývoja — administrátorský kľúč nie je potrebný. Viac na [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Náhradné riešenie) Autentifikácia na základe kľúča** — iba ak nemôžete použiť RBAC, uložte aj administrátorský kľúč:

#### Uložte koncový bod a API kľúč pre Azure AI Search inštanciu do premenných prostredia.

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

### Použitie Python SDK

1. Nainštalujte knižnicu Azure Cognitive Search client a Azure Identity pre Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Použite nasledujúci Python kód na vytvorenie indexu a nahranie dokumentov:

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

### Použitie .NET SDK

1. Spustite nasledujúci príkaz na vytvorenie indexu a nahranie dokumentov:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Príklad .NET nižšie používa `DefaultAzureCredential`, ktorý môže použiť vaše prihlásenie cez Azure CLI z `az login` počas lokálneho vývoja.

2. Tu je .NET kód pre `AzureSearch.cs`:

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

Pre podrobnejšie informácie si pozrite nasledujúcu dokumentáciu:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Záver

Úspešne ste nastavili Azure AI Search pomocou Azure portálu a integrovaných nástrojov. Teraz môžete preskúmať pokročilejšie funkcie a možnosti Azure AI Search na vylepšenie vašich vyhľadávacích riešení.

Pre ďalšiu pomoc navštívte [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->