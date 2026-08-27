# Przewodnik po konfiguracji Azure AI Search

Ten przewodnik pomoże Ci skonfigurować Azure AI Search za pomocą portalu Azure. Postępuj zgodnie z poniższymi krokami, aby utworzyć i skonfigurować usługę Azure AI Search.

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że masz następujące elementy:

- Subskrypcję Azure. Jeśli nie masz subskrypcji Azure, możesz utworzyć darmowe konto na stronie [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Krok 1: Utwórz konto magazynu Azure

1. Postępuj zgodnie z instrukcją [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), aby utworzyć nowe konto magazynu Azure.
   **UWAGA**: Upewnij się, że typ konta magazynu to Standard General Purpose V2.

## Krok 2: Utwórz usługę Azure AI Search

1. Zaloguj się do [portalu Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. W lewym panelu nawigacyjnym kliknij **Utwórz zasób**.
3. W polu wyszukiwania wpisz "Azure AI Search" i wybierz **Azure AI Search** z listy wyników.
4. Kliknij przycisk **Utwórz**.
5. W zakładce **Podstawowe** podaj następujące informacje:
   - **Subskrypcja**: Wybierz swoją subskrypcję Azure.
   - **Grupa zasobów**: Utwórz nową grupę zasobów lub wybierz istniejącą.
   - **Nazwa zasobu**: Wprowadź unikalną nazwę dla usługi wyszukiwania.
   - **Region**: Wybierz region najbliższy Twoim użytkownikom.
   - **Poziom cenowy**: Wybierz poziom cenowy odpowiadający Twoim wymaganiom. Możesz zacząć od warstwy darmowej do testów.
6. Kliknij **Przegląd + utwórz**.
7. Sprawdź ustawienia i kliknij **Utwórz**, aby utworzyć usługę wyszukiwania.

## Krok 3: Rozpocznij pracę z Azure AI Search

1. Po zakończeniu wdrażania przejdź do swojej usługi wyszukiwania w portalu Azure.
2. W panelu przeglądu usługi wyszukiwania skopiuj adres URL. Powinien wyglądać jak `https://<service-name>.search.windows.net`.
3. **(Zalecane)** Włącz dostęp bezkluczowy za pomocą Microsoft Entra ID (RBAC), jak pokazano w kroku 4 poniżej — bez potrzeby użycia klucza. Przykłady w tym przewodniku tworzą/aktualizują indeksy i przesyłają dokumenty, które wymagają ról **Search Service Contributor** oraz **Search Index Data Contributor** (lub, przy uwierzytelnianiu kluczowym, **głównego klucza administratora** — nie klucza zapytania). Jeśli nie możesz użyć RBAC, otwórz panel **Ustawienia > Klucze** i skopiuj **główny klucz administratora**.
4. Postępuj zgodnie z krokami na stronie [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), aby utworzyć indeks, przesłać dane i wykonać wyszukiwanie.

## Krok 4: Używaj narzędzi Azure AI Search

Azure AI Search integruje się z różnymi narzędziami, które zwiększają możliwości wyszukiwania. Możesz korzystać z Azure CLI, Python SDK, .NET SDK oraz innych narzędzi do zaawansowanych konfiguracji i operacji.

### Używanie Azure CLI

1. Zainstaluj Azure CLI, postępując zgodnie z instrukcjami na stronie [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Zaloguj się do Azure CLI przy pomocy polecenia:

   ```bash
   az login
   ```
3. **(Zalecane) Włącz dostęp bezkluczowy za pomocą Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show nie ma pola "endpoint"; zbuduj URL z nazwy usługi.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Po włączeniu RBAC, przykłady dla Python i .NET SDK poniżej uwierzytelniają się za pomocą `DefaultAzureCredential`, które wykorzystuje Twoją sesję `az login` podczas lokalnego rozwoju — nie jest potrzebny klucz administratora. Zobacz [Połącz się z Azure AI Search za pomocą ról](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternatywa) Uwierzytelnianie na podstawie klucza** — tylko jeśli nie możesz użyć RBAC, zapisz również klucz administratora:

#### Zapisz zarówno punkt końcowy, jak i klucz API instancji Azure AI Search do zmiennych środowiskowych.

    ```bash
    # zsh/bash
    # az search service show nie ma pola "endpoint"; zbuduj URL z nazwy usługi.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show nie ma pola "endpoint"; zbuduj URL z nazwy usługi.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Używanie Python SDK

1. Zainstaluj bibliotekę klienta Azure Cognitive Search oraz Azure Identity dla Pythona:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Użyj poniższego kodu Pythona, aby utworzyć indeks i przesłać dokumenty:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Bez klucza (zalecane): korzysta z twojej tożsamości `az login` za pośrednictwem Entra ID RBAC.
    # Wymaga ról "Search Service Contributor" i "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Użycie awaryjne (uwierzytelnianie oparte na kluczu):
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

### Używanie .NET SDK

1. Uruchom poniższe polecenie, aby utworzyć indeks i przesłać dokumenty:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Poniższy przykład .NET używa `DefaultAzureCredential`, które może korzystać z Twojego logowania Azure CLI za pomocą `az login` podczas lokalnego rozwoju.

2. Oto kod .NET pliku `AzureSearch.cs`:

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

Więcej szczegółowych informacji znajdziesz w następującej dokumentacji:

- [Utwórz usługę Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Rozpocznij pracę z Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Narzędzia Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Podsumowanie

Pomyślnie skonfigurowałeś Azure AI Search za pomocą portalu Azure i zintegrowanych narzędzi. Teraz możesz odkrywać bardziej zaawansowane funkcje i możliwości Azure AI Search, aby wzbogacić swoje rozwiązania wyszukiwania.

W celu uzyskania dalszej pomocy odwiedź [dokumentację Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->