# Azure AI Search -asetusten opas

Tämä opas auttaa sinua määrittämään Azure AI Searchin Azure-portaalin avulla. Noudata alla olevia ohjeita luodaksesi ja määrittääksesi Azure AI Search -palvelusi.

## Vaatimukset

Ennen aloittamista varmista, että sinulla on seuraavat:

- Azure-tilaus. Jos sinulla ei ole Azure-tilausta, voit luoda ilmaisen tilin osoitteessa [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Vaihe 1: Luo Azure Storage -tili

1. Noudata tätä ohjetta, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), luodaksesi uuden Azure Storage -tilin.
   **HUOM**: Varmista, että Storage-tilin tyypiksi on valittu Standard General Purpose V2.

## Vaihe 2: Luo Azure AI Search -palvelu

1. Kirjaudu sisään [Azure-portaaliin](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Valitse vasemmassa navigointipaneelissa **Create a resource**.
3. Kirjoita hakukenttään "Azure AI Search" ja valitse hakutuloksista **Azure AI Search**.
4. Napsauta **Create**-painiketta.
5. Täytä **Basics**-välilehdellä seuraavat tiedot:
   - **Subscription**: Valitse Azure-tilauksesi.
   - **Resource group**: Luo uusi resurssiryhmä tai valitse olemassa oleva.
   - **Resource name**: Anna hakupalvelullesi ainutlaatuinen nimi.
   - **Region**: Valitse käyttäjiäsi lähinnä oleva alue.
   - **Pricing tier**: Valitse hintataso tarpeittesi mukaan. Voit aloittaa testaamalla Free-tasolla.
6. Napsauta **Review + create**.
7. Tarkista asetukset ja napsauta **Create** luodaksesi hakupalvelun.

## Vaihe 3: Aloita Azure AI Searchin käyttö

1. Kun käyttöönotto on valmis, siirry hakupalveluusi Azure-portaalissa.
2. Kopioi hakupalvelun yleisnäkymästä URL-osoite. Sen pitäisi olla muodossa `https://<service-name>.search.windows.net`.
3. **(Suositeltu)** Ota käyttöön avainvapaa pääsy Microsoft Entra ID:llä (RBAC) alla olevan Vaiheen 4 mukaisesti — avainta ei tarvita. Tämän oppaan esimerkit luovat/päivittävät indeksejä ja lataavat dokumentteja, mikä edellyttää **Search Service Contributor** ja **Search Index Data Contributor** -rooleja (tai avainpohjaisessa todentamisessa **primary admin key** — ei query key). Käytä RBAC:ia aina kun mahdollista, ja jos et voi, avaa **Settings > Keys** -paneeli ja kopioi **primary admin key**.
4. Noudata [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) -sivun ohjeita luodaksesi indeksin, ladataksesi dataa ja suorittaaksesi haun.

## Vaihe 4: Käytä Azure AI Search -työkaluja

Azure AI Search integroituu erilaisiin työkaluihin hakutoimintojen tehostamiseksi. Voit käyttää Azure CLI:tä, Python SDK:ta, .NET SDK:ta ja muita työkaluja kehittyneeseen määritykseen ja toimintoihin.

### Azure CLI:n käyttö

1. Asenna Azure CLI seuraamalla ohjeita osoitteessa [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Kirjaudu sisään Azure CLI:hin komennolla:

   ```bash
   az login
   ```
3. **(Suositeltu) Ota avainvapaa pääsy käyttöön Microsoft Entra ID:llä (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show -komennolla ei ole "endpoint"-kenttää; luo URL palvelun nimestä.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Kun RBAC on käytössä, alla olevat Python- ja .NET SDK -esimerkit tunnistautuvat `DefaultAzureCredential`-luokan avulla, joka käyttää `az login` -istuntoasi paikallisessa kehityksessä — ylläpitäjän avainta ei tarvita. Katso lisää [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Varavaihtoehto) Avainpohjainen tunnistus** — vain jos et voi käyttää RBAC:ia, tallenna myös ylläpitäjän avain:

#### Tallenna sekä päätepiste että API-avain ympäristömuuttujiin Azure AI Search -instanssille.

    ```bash
    # zsh/bash
    # az search service show -komennossa ei ole "endpoint"-kenttää; rakenna URL palvelun nimestä.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show -komennossa ei ole "endpoint"-kenttää; rakenna URL palvelun nimestä.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK:n käyttö

1. Asenna Azure Cognitive Search -asiakas- ja Azure Identity -kirjastot Pythonille:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Käytä seuraavaa Python-koodia luodaksesi indeksin ja ladataksesi dokumentteja:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Avaineton (suositeltu): käyttää `az login` -henkilöllisyyttäsi Entra ID RBAC:n kautta.
    # Vaatii "Search Service Contributor" ja "Search Index Data Contributor" -roolit.
    credential = DefaultAzureCredential()
    # Varavaihtoehto (avaimeen perustuva todennus):
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

### .NET SDK:n käyttö

1. Suorita seuraava komento luodaksesi indeksin ja ladataksesi dokumentteja:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Alla oleva .NET-esimerkki käyttää `DefaultAzureCredential`-luokkaa, joka voi käyttää Azure CLI:n `az login` -kirjautumistasi paikallisessa kehityksessä.

2. Tässä on .NET-koodi tiedostosta `AzureSearch.cs`:

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

Lisätietoja löydät seuraavista dokumenteista:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Yhteenveto

Olet onnistuneesti määrittänyt Azure AI Searchin Azure-portaalin ja integroit työkalut. Voit nyt tutustua Azure AI Searchin kehittyneempiin ominaisuuksiin ja toimintoihin ratkaistaksesi hakutarpeitasi paremmin.

Lisäavun saamiseksi vieraile osoitteessa [Azure Cognitive Search dokumentaatio](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->