<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:40:49+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "fi"
}
-->
# Azure AI Search - Asennusopas

Tämä opas auttaa sinua ottamaan Azure AI Searchin käyttöön Azure-portaalissa. Seuraa alla olevia ohjeita luodaksesi ja määrittääksesi Azure AI Search -palvelun.

## Esivaatimukset

Ennen kuin aloitat, varmista, että sinulla on seuraavat:

- Azure-tilaus. Jos sinulla ei ole Azure-tilausta, voit luoda ilmaisen tilin osoitteessa [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Vaihe 1: Luo Azure Storage -tili

1. Seuraa näitä ohjeita, [Luo Azure Storage -tili](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), luodaksesi uuden Azure Storage -tilin.
   **NOTE**: Varmista, että Storage Account -tyyppi on Standard General Purpose V2.

## Vaihe 2: Luo Azure AI Search -palvelu

1. Kirjaudu sisään [Azure-portaaliin](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Vasemmanpuoleisessa navigointipaneelissa napsauta **Luo resurssi**.
3. Hakukenttään kirjoita "Azure AI Search" ja valitse **Azure AI Search** hakutuloksista.
4. Napsauta **Luo**-painiketta.
5. **Perustiedot**-välilehdellä anna seuraavat tiedot:
   - **Tilaus**: Valitse Azure-tilauksesi.
   - **Resurssiryhmä**: Luo uusi resurssiryhmä tai valitse olemassa oleva.
   - **Resurssin nimi**: Anna hakupalvelulle yksilöllinen nimi.
   - **Alue**: Valitse käyttäjiäsi lähin alue.
   - **Hinnoittelutaso**: Valitse tarpeisiisi sopiva hinnoittelutaso. Voit aloittaa ilmaisella tasolla testikäyttöä varten.
6. Napsauta **Tarkista + luo**.
7. Tarkista asetukset ja napsauta **Luo** luodaksesi hakupalvelun.

## Vaihe 3: Aloita Azure AI Searchin käyttö

1. Kun käyttöönotto on valmis, siirry hakupalveluusi Azure-portaalissa.
2. Hakupalvelun yleiskatsauspaneelissa kopioi URL-osoite. Sen pitäisi näyttää tältä: `https://<service-name>.search.windows.net`.
3. Asetukset > Avaimet -paneelissa kopioi kyselyavain.
4. Seuraa [Pikaopas](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) -sivun ohjeita luodaksesi indeksin, ladataksesi dataa ja suorittaaksesi hakukyselyn.

## Vaihe 4: Käytä Azure AI Search -työkaluja

Azure AI Search integroituu useisiin työkaluihin hakutoimintojen parantamiseksi. Voit käyttää Azure CLI:tä, Python SDK:ta, .NET SDK:ta ja muita työkaluja edistyneisiin määrityksiin ja toimintoihin.

### Azure CLI:n käyttö

1. Asenna Azure CLI seuraamalla ohjeita [Asenna Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Kirjaudu Azure CLI:hin komennolla:

   ```bash
   az login
   ```

3. Tallenna sekä Azure AI Search -instanssin päätepiste että API-avain ympäristömuuttujiin.

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

### Python SDK:n käyttö

1. Asenna Azure Cognitive Search -asiakasohjelmakirjasto Pythonille:

   ```bash
   pip install azure-search-documents
   ```

2. Käytä seuraavaa Python-koodia luodaksesi indeksin ja ladataksesi dokumentteja:

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

### .NET SDK:n käyttö

1. Suorita seuraava komento luodaksesi indeksin ja ladataksesi dokumentteja:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Tässä on .NET-koodi `AzureSearch.cs`:

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

Lisätietoja löydät seuraavista dokumenteista:

- [Luo Azure Cognitive Search -palvelu](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Aloita Azure Cognitive Searchin käyttö](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search -työkalut](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Yhteenveto

Olet onnistuneesti ottanut Azure AI Searchin käyttöön Azure-portaalissa ja integroinut työkalut. Voit nyt tutkia Azure AI Searchin edistyneitä ominaisuuksia ja toimintoja parantaaksesi hakuratkaisujasi.

Lisäapua varten käy [Azure Cognitive Search -dokumentaatiossa](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.