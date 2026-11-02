# Vodnik za nastavitev Azure AI Search

Ta vodnik vam bo pomagal nastaviti Azure AI Search z uporabo Azure portala. Sledite spodnjim korakom za ustvarjanje in konfiguracijo vaše storitve Azure AI Search.

## Predpogoji

Preden začnete, zagotovite, da imate naslednje:

- Azure naročnino. Če še nimate Azure naročnine, lahko ustvarite brezplačen račun na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## 1. korak: Ustvarite Azure račun za shranjevanje

1. Sledite temu navodilu, [Ustvarjanje Azure računa za shranjevanje](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), za ustvarjanje novega Azure računa za shranjevanje.
   **OPOMBA**: Prepričajte se, da je tip računa za shranjevanje Standard General Purpose V2.

## 2. korak: Ustvarite storitev Azure AI Search

1. Prijavite se v [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V levem navigacijskem oknu kliknite **Ustvari vir**.
3. V iskalno polje vnesite "Azure AI Search" in izberite **Azure AI Search** s seznama rezultatov.
4. Kliknite gumb **Ustvari**.
5. V zavihku **Osnove** vnesite naslednje informacije:
   - **Naročnina**: Izberite svojo Azure naročnino.
   - **Skupina virov**: Ustvarite novo skupino virov ali izberite obstoječo.
   - **Ime vira**: Vnesite edinstveno ime za vašo iskalno storitev.
   - **Regija**: Izberite regijo, najbližjo vašim uporabnikom.
   - **Cenovni razred**: Izberite cenovni razred, ki ustreza vaši uporabi. Za testiranje lahko začnete z brezplačnim razredom.
6. Kliknite **Pregled + ustvari**.
7. Preglejte nastavitve in kliknite **Ustvari** za ustvarjanje iskalne storitve.

## 3. korak: Zaženite Azure AI Search

1. Ko je namestitev končana, pojdite v vašo iskalno storitev v Azure portalu.
2. V pregledu iskalne storitve kopirajte URL. Moral bi izgledati kot `https://<service-name>.search.windows.net`.
3. **(Priporočeno)** Omogočite dostop brez ključa z Microsoft Entra ID (RBAC), kot je prikazano v 4. koraku spodaj — ni potreben ključ. Primeri v tem vodniku ustvarjajo/posodabljajo indekse in nalagajo dokumente, za kar so potrebne vloge **Search Service Contributor** in **Search Index Data Contributor** (ali za preverjanje pristnosti na osnovi ključa je potreben **primarni administratorski ključ** — ne ključ poizvedbe). Če RBAC ne morete uporabiti, odprite **Nastavitve > Ključi** in kopirajte **primarni administratorski ključ**.
4. Sledite korakom na strani [Vodnik za začetek](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) za ustvarjanje indeksa, nalaganje podatkov in izvedbo iskanja.

## 4. korak: Uporaba orodij Azure AI Search

Azure AI Search se integrira z različnimi orodji za izboljšanje vaših iskalnih zmogljivosti. Lahko uporabljate Azure CLI, Python SDK, .NET SDK in druga orodja za napredne nastavitve in operacije.

### Uporaba Azure CLI

1. Namestite Azure CLI s sledenjem navodilom na [Namestitev Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prijavite se v Azure CLI z ukazom:

   ```bash
   az login
   ```
3. **(Priporočeno) Omogočite dostop brez ključa z Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Z omogočenim RBAC, primeri Python in .NET SDK spodaj preverjajo pristnost z `DefaultAzureCredential`, ki med lokalnim razvojem uporablja vašo `az login` sejo — ni potreben administratorski ključ. Oglejte si [Povezava z Azure AI Search z uporabo vlog](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Varnostna rešitev) Preverjanje pristnosti na osnovi ključa** — le če ne morete uporabiti RBAC, shranite tudi administratorski ključ:

#### Shranite tako končno točko kot API ključ za Azure AI Search primer kot okoljski spremenljivki.

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

### Uporaba Python SDK

1. Namestite knjižnico Azure Cognitive Search klient in Azure Identity za Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Uporabite naslednjo kodo v Pythonu za ustvarjanje indeksa in nalaganje dokumentov:

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

### Uporaba .NET SDK

1. Zaženite naslednji ukaz za ustvarjanje indeksa in nalaganje dokumentov:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Primer .NET spodaj uporablja `DefaultAzureCredential`, ki lahko med lokalnim razvojem uporablja vašo prijavo v Azure CLI iz `az login`.

2. Tukaj je .NET koda za `AzureSearch.cs`:

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

- [Ustvarjanje storitve Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Začetek z Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Orodja Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Zaključek

Uspešno ste nastavili Azure AI Search z uporabo Azure portala in integriranih orodij. Zdaj lahko raziščete bolj napredne funkcije in zmogljivosti Azure AI Search za izboljšanje vaših iskalnih rešitev.

Za nadaljnjo pomoč obiščite [Dokumentacijo Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->