<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:36:07+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "pl"
}
-->
# Przewodnik konfiguracji Azure AI Search

Ten przewodnik pomoże Ci skonfigurować Azure AI Search za pomocą portalu Azure. Postępuj zgodnie z poniższymi krokami, aby utworzyć i skonfigurować usługę Azure AI Search.

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że masz:

- Subskrypcję Azure. Jeśli nie masz subskrypcji Azure, możesz utworzyć darmowe konto na stronie [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Krok 1: Utwórz konto magazynu Azure

1. Postępuj zgodnie z instrukcją [Tworzenie konta magazynu Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), aby utworzyć nowe konto magazynu Azure.  
   **NOTE**: Upewnij się, że typ konta magazynu to Standard General Purpose V2.

## Krok 2: Utwórz usługę Azure AI Search

1. Zaloguj się do [portalu Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. W lewym panelu nawigacyjnym kliknij **Utwórz zasób**.
3. W polu wyszukiwania wpisz "Azure AI Search" i wybierz **Azure AI Search** z listy wyników.
4. Kliknij przycisk **Utwórz**.
5. W zakładce **Podstawowe** podaj następujące informacje:
   - **Subskrypcja**: Wybierz swoją subskrypcję Azure.
   - **Grupa zasobów**: Utwórz nową grupę zasobów lub wybierz istniejącą.
   - **Nazwa zasobu**: Wprowadź unikalną nazwę dla swojej usługi wyszukiwania.
   - **Region**: Wybierz region najbliższy Twoim użytkownikom.
   - **Poziom cenowy**: Wybierz poziom cenowy odpowiadający Twoim wymaganiom. Możesz zacząć od darmowego poziomu do testów.
6. Kliknij **Przejrzyj + utwórz**.
7. Przejrzyj ustawienia i kliknij **Utwórz**, aby utworzyć usługę wyszukiwania.

## Krok 3: Rozpocznij pracę z Azure AI Search

1. Po zakończeniu wdrożenia przejdź do swojej usługi wyszukiwania w portalu Azure.
2. W panelu przeglądu usługi wyszukiwania skopiuj URL. Powinien wyglądać tak: `https://<service-name>.search.windows.net`.
3. W zakładce Ustawienia > Klucze skopiuj klucz zapytania.
4. Postępuj zgodnie z krokami na stronie [Przewodnik szybkiego startu](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), aby utworzyć indeks, przesłać dane i wykonać zapytanie wyszukiwania.

## Krok 4: Korzystaj z narzędzi Azure AI Search

Azure AI Search integruje się z różnymi narzędziami, aby zwiększyć możliwości wyszukiwania. Możesz używać Azure CLI, Python SDK, .NET SDK i innych narzędzi do zaawansowanej konfiguracji i operacji.

### Korzystanie z Azure CLI

1. Zainstaluj Azure CLI, postępując zgodnie z instrukcjami na stronie [Instalacja Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Zaloguj się do Azure CLI za pomocą polecenia:

   ```bash
   az login
   ```

3. Zapisz zarówno punkt końcowy, jak i klucz API dla instancji Azure AI Search w zmiennych środowiskowych.

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

### Korzystanie z Python SDK

1. Zainstaluj bibliotekę klienta Azure Cognitive Search dla Pythona:

   ```bash
   pip install azure-search-documents
   ```

2. Użyj poniższego kodu Python, aby utworzyć indeks i przesłać dokumenty:

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

### Korzystanie z .NET SDK

1. Uruchom poniższe polecenie, aby utworzyć indeks i przesłać dokumenty:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Oto kod .NET dla `AzureSearch.cs`:

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

Więcej szczegółowych informacji znajdziesz w poniższej dokumentacji:

- [Tworzenie usługi Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Rozpocznij pracę z Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Narzędzia Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Podsumowanie

Pomyślnie skonfigurowałeś Azure AI Search za pomocą portalu Azure i zintegrowanych narzędzi. Teraz możesz eksplorować bardziej zaawansowane funkcje i możliwości Azure AI Search, aby ulepszyć swoje rozwiązania wyszukiwania.

Aby uzyskać dalszą pomoc, odwiedź [dokumentację Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.