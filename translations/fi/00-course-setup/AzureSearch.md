# Azure AI Searchin asennusopas

Tämä opas auttaa sinua ottamaan Azure AI Searchin käyttöön Azure-portaalin avulla. Noudata alla olevia ohjeita luodaksesi ja määrittääksesi Azure AI Search -palvelusi.

## Ennen aloittamista

Varmista ennen aloittamista, että sinulla on seuraavat asiat:

- Azure-tilaus. Jos sinulla ei ole Azure-tilausta, voit luoda ilmaisen tilin osoitteessa [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Vaihe 1: Luo Azure Storage -tili

1. Noudata tätä ohjetta, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), luodaksesi uuden Azure Storage -tilin.
   **HUOM**: Varmista, että Storage Accountin tyypiksi on valittu Standard General Purpose V2.

## Vaihe 2: Luo Azure AI Search -palvelu

1. Kirjaudu sisään [Azure-portaaliin](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Vasemmanpuoleisessa navigaatiopaneelissa napsauta **Luo resurssi**.
3. Hakukenttään kirjoita "Azure AI Search" ja valitse **Azure AI Search** tulosluettelosta.
4. Napsauta **Luo**-painiketta.
5. **Perustiedot**-välilehdellä anna seuraavat tiedot:
   - **Tilaus**: Valitse Azure-tilauksesi.
   - **Resurssiryhmä**: Luo uusi resurssiryhmä tai valitse olemassa oleva.
   - **Resurssin nimi**: Anna hakupalvelullesi ainutlaatuinen nimi.
   - **Alue**: Valitse alue, joka on käyttäjiäsi lähinnä.
   - **Hinnoittelutasot**: Valitse hinnoittelutaso, joka sopii tarpeisiisi. Voit aloittaa ilmaisella tasolla testauksessa.
6. Napsauta **Tarkista + luo**.
7. Tarkista asetukset ja napsauta **Luo** luodaksesi hakupalvelun.

## Vaihe 3: Aloita Azure AI Searchin käyttö

1. Kun käyttöönotto on valmis, siirry hakupalveluusi Azure-portaalissa.
2. Kopioi hakupalvelun yleiskatsauspaneelista URL-osoite. Sen pitäisi näyttää tältä: `https://<service-name>.search.windows.net`.
3. **(Suositeltavaa)** Ota käyttöön avaimeton käyttö Microsoft Entra ID:n (RBAC) kanssa alla kohdassa Vaihe 4 — avainta ei tarvita. Tässä oppaassa olevat esimerkit luovat/päivittävät indeksejä ja lataavat asiakirjoja, jotka vaativat roolit **Search Service Contributor** ja **Search Index Data Contributor** (tai avaintunnistuksessa **pääkäyttäjän avain** — ei kyselyavainta). Vain jos et voi käyttää RBACia, avaa **Asetukset > Avaimet** -paneeli ja kopioi **pääkäyttäjän avain**.
4. Noudata ohjeita [Pika-aloitusoppaassa](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) indeksin luomiseksi, datan lataamiseksi ja haun suorittamiseksi.

## Vaihe 4: Käytä Azure AI Search -työkaluja

Azure AI Search integroituu useiden työkalujen kanssa parantaakseen hakutoimintojasi. Voit käyttää Azure CLI:tä, Python SDK:ta, .NET SDK:ta ja muita työkaluja edistyneisiin määrityksiin ja toimintoihin.

### Azure CLI:n käyttö

1. Asenna Azure CLI noudattamalla ohjeita kohdassa [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Kirjaudu sisään Azure CLI:hin komennolla:

   ```bash
   az login
   ```
3. **(Suositeltavaa) Ota käyttöön avaimeton käyttö Microsoft Entra ID:n (RBAC) kanssa:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBACin ollessa käytössä alla olevat Python- ja .NET SDK -esimerkit todentavat käyttämällä `DefaultAzureCredential`, joka hyödyntää `az login`-istuntoasi paikallisessa kehityksessä — ei tarvitse admin-avainta. Katso [Yhdistä Azure AI Searchiin rooleilla](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Varavaihtoehto) Avaintunnistus** — vain jos et voi käyttää RBACia, tallenna myös admin-avain:

#### Tallenna sekä päätepiste että API-avain Azure AI Search -instanssin ympäristömuuttujiin.

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

### Python SDK:n käyttö

1. Asenna Azure Cognitive Search -asiakasohjelmakirjasto ja Azure Identity Pythonille:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Käytä seuraavaa Python-koodia indeksin luomiseksi ja asiakirjojen lataamiseksi:

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

### .NET SDK:n käyttö

1. Suorita seuraava komento indeksin luomiseksi ja asiakirjojen lataamiseksi:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Alla oleva .NET-esimerkki käyttää `DefaultAzureCredential`, joka voi käyttää Azure CLI -kirjautumistasi `az login` paikallisessa kehityksessä.

2. Tässä on `AzureSearch.cs` .NET-koodi:

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

Yksityiskohtaisempaa tietoa saat seuraavasta dokumentaatiosta:

- [Luo Azure Cognitive Search -palvelu](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Aloita Azure Cognitive Searchin käyttö](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search -työkalut](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Yhteenveto

Olet onnistuneesti ottanut Azure AI Searchin käyttöön Azure-portaalin ja integroitujen työkalujen avulla. Voit nyt tutkia Azure AI Searchin kehittyneempiä ominaisuuksia ja mahdollisuuksia parantaaksesi hakuratkaisujasi.

Lisäavun saamiseksi käy [Azure Cognitive Search -dokumentaatiossa](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->