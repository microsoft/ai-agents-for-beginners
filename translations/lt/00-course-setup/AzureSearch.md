# Azure AI Search įdiegimo vadovas

Šis vadovas padės jums įdiegti Azure AI Search naudojant Azure portalą. Sekite žemiau pateiktus veiksmus, kad sukurtumėte ir sukonfigūruotumėte savo Azure AI Search paslaugą.

## Prieš pradedant

Prieš pradėdami įsitikinkite, kad turite šiuos dalykus:

- Azure prenumeratą. Jei neturite Azure prenumeratos, galite sukurti nemokamą paskyrą adresu [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## 1 veiksmas: Sukurkite Azure saugyklos paskyrą

1. Sekite šią instrukciją, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), kad sukurtumėte naują Azure saugyklos paskyrą.
   **PASTABA**: Įsitikinkite, kad saugyklos paskyros tipas yra Standard General Purpose V2.

## 2 veiksmas: Sukurkite Azure AI Search paslaugą

1. Prisijunkite prie [Azure portalo](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Kairėje naršymo srityje spustelėkite **Create a resource**.
3. Paieškos laukelyje įveskite „Azure AI Search“ ir iš rezultatų sąrašo pasirinkite **Azure AI Search**.
4. Spustelėkite mygtuką **Create**.
5. Skiltyje **Basics** pateikite šią informaciją:
   - **Subscription**: Pasirinkite savo Azure prenumeratą.
   - **Resource group**: Sukurkite naują arba pasirinkite esamą resursų grupę.
   - **Resource name**: Įveskite unikalias paieškos paslaugos pavadinimą.
   - **Region**: Pasirinkite regioną, artimiausią jūsų vartotojams.
   - **Pricing tier**: Pasirinkite kainų lygį, atitinkantį jūsų poreikius. Testavimui galite pradėti nuo nemokamo rinkinio.
6. Spustelėkite **Review + create**.
7. Peržiūrėkite nustatymus ir spustelėkite **Create**, kad sukurtumėte paieškos paslaugą.

## 3 veiksmas: Pradėkite naudotis Azure AI Search

1. Baigus diegimą, eikite į savo paieškos paslaugą Azure portale.
2. Paieškos paslaugos apžvalgos srityje nukopijuokite URL. Jis turėtų atrodyti kaip `https://<service-name>.search.windows.net`.
3. **(Rekomenduojama)** Įgalinkite prieigą be rakto su Microsoft Entra ID (RBAC), kaip parodyta 4 žingsnyje žemiau — rakto nereikia. Šio vadovo pavyzdžiai kuria / atnaujina indeksus ir įkelia dokumentus, kurie reikalauja **Search Service Contributor** ir **Search Index Data Contributor** vaidmenų (arba, naudojant autentifikavimą su raktu, **pagrindinio administratoriaus rakto** — ne užklausos rakto). Tik jei negalite naudoti RBAC, atidarykite **Settings > Keys** puslapį ir nukopijuokite **pagrindinį administratoriaus raktą**.
4. Sekite žingsnius [Quickstart vadove](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), kad sukurtumėte indeksą, įkeltumėte duomenis ir atliktumėte paiešką.

## 4 veiksmas: Naudokite Azure AI Search įrankius

Azure AI Search integruojasi su įvairiais įrankiais, kad pagerintų jūsų paieškos galimybes. Galite naudoti Azure CLI, Python SDK, .NET SDK ir kitus įrankius pažangioms konfigūracijoms ir operacijoms.

### Naudojant Azure CLI

1. Įdiekite Azure CLI sekdami instrukcijas adresu [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prisijunkite prie Azure CLI naudodami komandą:

   ```bash
   az login
   ```
3. **(Rekomenduojama) Įgalinkite prieigą be rakto su Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show neturi "endpoint" lauko; sukurkite URL iš paslaugos pavadinimo.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Naudojant įjungtą RBAC, žemiau pateikti Python ir .NET SDK pavyzdžiai autentifikuojasi su `DefaultAzureCredential`, kuris vietinio vystymo metu naudoja jūsų `az login` sesiją — administratoriaus rakto nereikia. Žr. [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternatyva) Autentifikacija su raktu** — tik jei negalite naudoti RBAC, taip pat saugokite administratoriaus raktą:

#### Išsaugokite tiek endpoint, tiek API raktą Azure AI Search instancijos kintamuosiuose aplinkoje.

    ```bash
    # zsh/bash
    # az search service show neturi „endpoint“ lauko; sukurkite URL iš paslaugos vardo.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show neturi „endpoint“ lauko; sukurkite URL iš paslaugos vardo.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Naudojant Python SDK

1. Įdiekite Azure Cognitive Search klientų biblioteką ir Azure Identity Python kalbai:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Naudokite šį Python kodą, kad sukurtumėte indeksą ir įkeltumėte dokumentus:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Be rakto (rekomenduojama): naudoja jūsų `az login` tapatybę per Entra ID RBAC.
    # Reikalauja „Search Service Contributor“ ir „Search Index Data Contributor“ vaidmenų.
    credential = DefaultAzureCredential()
    # Atsarginis variantas (autentifikacija pagal raktą):
    # iš azure.core.credentials importuoti AzureKeyCredential
    # kredencialas = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

### Naudojant .NET SDK

1. Paleiskite šią komandą, kad sukurtumėte indeksą ir įkeltumėte dokumentus:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Žemiau pateiktas .NET pavyzdys naudoja `DefaultAzureCredential`, kuris gali naudoti jūsų Azure CLI prisijungimą iš `az login` vietinio vystymo metu.

2. Štai .NET failo `AzureSearch.cs` kodas:

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

Daugiau išsamių informacijos rasite šioje dokumentacijoje:

- [Sukurkite Azure Cognitive Search paslaugą](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Pradėkite naudotis Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search įrankiai](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Išvada

Jūs sėkmingai įdiegėte Azure AI Search naudodami Azure portalą ir integruotus įrankius. Dabar galite tyrinėti pažangesnes Azure AI Search funkcijas ir galimybes, kad pagerintumėte savo paieškos sprendimus.

Dėl papildomos pagalbos apsilankykite [Azure Cognitive Search dokumentacijoje](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->