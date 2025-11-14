<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:53:39+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "lt"
}
-->
# Azure AI Search nustatymo vadovas

Šis vadovas padės jums nustatyti Azure AI Search naudojant Azure portalą. Sekite žemiau pateiktus veiksmus, kad sukurtumėte ir sukonfigūruotumėte savo Azure AI Search paslaugą.

## Būtinos sąlygos

Prieš pradėdami, įsitikinkite, kad turite:

- Azure prenumeratą. Jei neturite Azure prenumeratos, galite sukurti nemokamą paskyrą adresu [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## 1 žingsnis: Sukurkite Azure saugyklos paskyrą

1. Sekite šias instrukcijas, [Sukurti Azure saugyklos paskyrą](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), kad sukurtumėte naują Azure saugyklos paskyrą.  
   **PASTABA**: Įsitikinkite, kad saugyklos paskyros tipas yra Standard General Purpose V2.

## 2 žingsnis: Sukurkite Azure AI Search paslaugą

1. Prisijunkite prie [Azure portalo](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Kairėje navigacijos juostoje spustelėkite **Create a resource**.
3. Paieškos laukelyje įveskite „Azure AI Search“ ir pasirinkite **Azure AI Search** iš rezultatų sąrašo.
4. Spustelėkite mygtuką **Create**.
5. Skiltyje **Basics** pateikite šią informaciją:
   - **Subscription**: Pasirinkite savo Azure prenumeratą.
   - **Resource group**: Sukurkite naują išteklių grupę arba pasirinkite esamą.
   - **Resource name**: Įveskite unikalų pavadinimą savo paieškos paslaugai.
   - **Region**: Pasirinkite regioną, artimiausią jūsų vartotojams.
   - **Pricing tier**: Pasirinkite kainų planą, kuris atitinka jūsų poreikius. Pradžiai galite pasirinkti nemokamą planą.
6. Spustelėkite **Review + create**.
7. Peržiūrėkite nustatymus ir spustelėkite **Create**, kad sukurtumėte paieškos paslaugą.

## 3 žingsnis: Pradėkite naudotis Azure AI Search

1. Kai diegimas bus baigtas, eikite į savo paieškos paslaugą Azure portale.
2. Paieškos paslaugos apžvalgos skydelyje nukopijuokite URL. Jis turėtų atrodyti taip: `https://<service-name>.search.windows.net`.
3. Skiltyje Settings > Keys nukopijuokite užklausos raktą.
4. Sekite veiksmus [Greitojo starto vadove](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), kad sukurtumėte indeksą, įkeltumėte duomenis ir atliktumėte paieškos užklausą.

## 4 žingsnis: Naudokite Azure AI Search įrankius

Azure AI Search integruojasi su įvairiais įrankiais, kad pagerintų jūsų paieškos galimybes. Galite naudoti Azure CLI, Python SDK, .NET SDK ir kitus įrankius pažangesniems konfigūravimams ir operacijoms.

### Naudojant Azure CLI

1. Įdiekite Azure CLI, sekdami instrukcijas [Įdiegti Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prisijunkite prie Azure CLI naudodami komandą:

   ```bash
   az login
   ```

3. Išsaugokite tiek galutinį tašką, tiek API raktą Azure AI Search instancijai aplinkos kintamuosiuose.

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

### Naudojant Python SDK

1. Įdiekite Azure Cognitive Search klientų biblioteką Python:

   ```bash
   pip install azure-search-documents
   ```

2. Naudokite šį Python kodą, kad sukurtumėte indeksą ir įkeltumėte dokumentus:

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

### Naudojant .NET SDK

1. Paleiskite šią komandą, kad sukurtumėte indeksą ir įkeltumėte dokumentus:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Štai .NET kodas `AzureSearch.cs`:

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

Daugiau informacijos rasite šiuose dokumentuose:

- [Sukurti Azure Cognitive Search paslaugą](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Pradėti naudotis Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search įrankiai](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Išvada

Jūs sėkmingai nustatėte Azure AI Search naudodami Azure portalą ir integruotus įrankius. Dabar galite tyrinėti pažangesnes Azure AI Search funkcijas ir galimybes, kad pagerintumėte savo paieškos sprendimus.

Dėl papildomos pagalbos apsilankykite [Azure Cognitive Search dokumentacijoje](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.