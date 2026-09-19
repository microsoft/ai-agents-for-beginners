# Vodnik za nastavitev Azure AI Search

Ta vodnik vam bo pomagal nastaviti Azure AI Search z uporabo Azure portala. Sledite spodnjim korakom za ustvarjanje in konfiguracijo vaše Azure AI Search storitve.

## Zahteve

Pred začetkom poskrbite, da imate naslednje:

- Azure naročnino. Če nimate Azure naročnine, lahko ustvarite brezplačen račun na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Korak 1: Ustvarite Azure Storage račun

1. Sledite tem navodilom, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), da ustvarite nov Azure Storage račun.
   **OPOMBA**: Prepričajte se, da je vrsta Storage računa Standard General Purpose V2.

## Korak 2: Ustvarite Azure AI Search storitev

1. Prijavite se v [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V levem navigacijskem meniju kliknite **Create a resource**.
3. V iskalno polje vpišite "Azure AI Search" in izberite **Azure AI Search** s seznama rezultatov.
4. Kliknite gumb **Create**.
5. Na zavihku **Basics** izpolnite naslednje podatke:
   - **Subscription**: Izberite svojo Azure naročnino.
   - **Resource group**: Ustvarite novo ali izberite obstoječo skupino virov.
   - **Resource name**: Vnesite edinstveno ime za vašo iskalno storitev.
   - **Region**: Izberite regijo, ki je najbližja vašim uporabnikom.
   - **Pricing tier**: Izberite cenovni nivo, ki ustreza vašim potrebam. Za testiranje lahko začnete s Free nivojem.
6. Kliknite **Review + create**.
7. Preverite nastavitve in kliknite **Create** za ustvarjanje iskalne storitve.

## Korak 3: Začnite z uporabo Azure AI Search

1. Ko je namestitev končana, pojdite na svojo iskalno storitev v Azure portalu.
2. Na pregledu iskalne storitve kopirajte URL. Izgledati mora približno tako: `https://<service-name>.search.windows.net`.
3. **(Priporočeno)** Omogočite dostop brez ključa z Microsoft Entra ID (RBAC), kot je prikazano v koraku 4 spodaj — brez potrebe po ključu. Primeri v tem vodniku ustvarjajo/posodabljajo indekse in nalagajo dokumente, kar zahteva vloge **Search Service Contributor** in **Search Index Data Contributor** (ali, pri avtentikaciji s ključem, **primarni administrativni ključ** — ne ključ za poizvedbe). Če RBAC ne morete uporabiti, odprite **Settings > Keys** in kopirajte **primarni administrativni ključ**.
4. Sledite korakom iz [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) strani za ustvarjanje indeksa, nalaganje podatkov in izvajanje iskanja.

## Korak 4: Uporaba orodij Azure AI Search

Azure AI Search se integrira z različnimi orodji za izboljšanje vaših iskalnih zmogljivosti. Lahko uporabljate Azure CLI, Python SDK, .NET SDK in druga orodja za napredne nastavitve in operacije.

### Uporaba Azure CLI

1. Namestite Azure CLI tako, da sledite navodilom na [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prijavite se v Azure CLI z ukazom:

   ```bash
   az login
   ```
3. **(Priporočeno) Omogočite dostop brez ključa z Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # ukaz az search service show nima polja "endpoint"; URL sestavite iz imena storitve.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Z omogočenim RBAC, Python in .NET SDK primeri spodaj preverijo pristnost z `DefaultAzureCredential`, ki uporablja vaš `az login` sejo med lokalnim razvojem — ni potreben administratorski ključ. Več si oglejte v [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Rezervna možnost) Avtentikacija s ključem** — le če RBAC ne morete uporabiti, shranite tudi administratorski ključ:

#### Shranite tako endpoint kot API ključ Azure AI Search instance v okoljske spremenljivke.

    ```bash
    # zsh/bash
    # az search service show nima polja "endpoint"; sestavite URL iz imena storitve.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show nima polja "endpoint"; sestavite URL iz imena storitve.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Uporaba Python SDK

1. Namestite knjižnico Azure Cognitive Search klient in Azure Identity za Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Uporabite spodnjo Python kodo za ustvarjanje indeksa in nalaganje dokumentov:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Brez ključa (priporočeno): uporablja vašo identiteto `az login` preko Entra ID RBAC.
    # Zahteva vlogi "Search Service Contributor" in "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Nadomestni način (avtentikacija na podlagi ključa):
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

### Uporaba .NET SDK

1. Zaženite spodnji ukaz za ustvarjanje indeksa in nalaganje dokumentov:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Primer .NET spodaj uporablja `DefaultAzureCredential`, ki lahko uporabi vašo prijavo v Azure CLI z `az login` med lokalnim razvojem.

2. Tukaj je .NET koda datoteke `AzureSearch.cs`:

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

Za bolj podrobne informacije si oglejte naslednjo dokumentacijo:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Zaključek

Uspešno ste nastavili Azure AI Search z uporabo Azure portala in vgrajenih orodij. Zdaj lahko raziskujete bolj napredne funkcije in zmogljivosti Azure AI Search za izboljšanje vaših iskalnih rešitev.

Za dodatno pomoč obiščite [Azure Cognitive Search dokumentacijo](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->