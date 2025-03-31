<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "932a1f463f0fcf97090b93b5d0255dff",
  "translation_date": "2025-03-28T09:10:31+00:00",
  "source_file": "00-course-setup\\AzureSearch.md",
  "language_code": "pl"
}
-->
# Przewodnik konfiguracji Azure AI Search

Ten przewodnik pomoże Ci skonfigurować Azure AI Search za pomocą portalu Azure. Postępuj zgodnie z poniższymi krokami, aby utworzyć i skonfigurować usługę Azure AI Search.

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że masz:

- Subskrypcję Azure. Jeśli nie posiadasz subskrypcji Azure, możesz utworzyć darmowe konto na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Krok 1: Utwórz usługę Azure AI Search

1. Zaloguj się do [portalu Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. W lewym panelu nawigacyjnym kliknij **Utwórz zasób**.
3. W polu wyszukiwania wpisz „Azure Cognitive Search” i wybierz **Azure Cognitive Search** z listy wyników.
4. Kliknij przycisk **Utwórz**.
5. W zakładce **Podstawowe** podaj następujące informacje:
   - **Subskrypcja**: Wybierz swoją subskrypcję Azure.
   - **Grupa zasobów**: Utwórz nową grupę zasobów lub wybierz istniejącą.
   - **Nazwa zasobu**: Wprowadź unikalną nazwę dla swojej usługi wyszukiwania.
   - **Region**: Wybierz region najbliższy Twoim użytkownikom.
   - **Poziom cenowy**: Wybierz poziom cenowy odpowiadający Twoim wymaganiom. Możesz zacząć od darmowego poziomu do testów.
6. Kliknij **Przejrzyj + utwórz**.
7. Sprawdź ustawienia i kliknij **Utwórz**, aby utworzyć usługę wyszukiwania.

## Krok 2: Rozpocznij pracę z Azure AI Search

1. Po zakończeniu wdrażania przejdź do swojej usługi wyszukiwania w portalu Azure.
2. Na stronie przeglądu usługi wyszukiwania kliknij przycisk **Szybki start**.
3. Postępuj zgodnie z instrukcjami w przewodniku szybkiego startu, aby utworzyć indeks, przesłać dane i wykonać zapytanie wyszukiwania.

### Utwórz indeks

1. W przewodniku szybkiego startu kliknij **Utwórz indeks**.
2. Zdefiniuj schemat indeksu, określając pola i ich atrybuty (np. typ danych, możliwość wyszukiwania, filtrowania).
3. Kliknij **Utwórz**, aby utworzyć indeks.

### Prześlij dane

1. W przewodniku szybkiego startu kliknij **Prześlij dane**.
2. Wybierz źródło danych (np. Azure Blob Storage, Azure SQL Database) i podaj wymagane szczegóły połączenia.
3. Mapuj pola źródła danych na pola indeksu.
4. Kliknij **Prześlij**, aby przesłać dane do indeksu.

### Wykonaj zapytanie wyszukiwania

1. W przewodniku szybkiego startu kliknij **Eksplorator wyszukiwania**.
2. Wpisz zapytanie wyszukiwania w polu wyszukiwania, aby przetestować funkcjonalność wyszukiwania.
3. Przejrzyj wyniki wyszukiwania i w razie potrzeby dostosuj schemat indeksu lub dane.

## Krok 3: Korzystaj z narzędzi Azure AI Search

Azure AI Search integruje się z różnymi narzędziami, aby ulepszyć możliwości wyszukiwania. Możesz używać Azure CLI, Python SDK i innych narzędzi do zaawansowanych konfiguracji i operacji.

### Korzystanie z Azure CLI

1. Zainstaluj Azure CLI, postępując zgodnie z instrukcjami na stronie [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Zaloguj się do Azure CLI, używając polecenia:
   ```bash
   az login
   ```
3. Utwórz nową usługę wyszukiwania za pomocą Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Utwórz indeks za pomocą Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Korzystanie z Python SDK

1. Zainstaluj bibliotekę klienta Azure Cognitive Search dla Pythona:
   ```bash
   pip install azure-search-documents
   ```
2. Użyj poniższego kodu w Pythonie, aby utworzyć indeks i przesłać dokumenty:
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

Szczegółowe informacje znajdziesz w poniższej dokumentacji:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Podsumowanie

Pomyślnie skonfigurowałeś Azure AI Search za pomocą portalu Azure i zintegrowanych narzędzi. Możesz teraz eksplorować bardziej zaawansowane funkcje i możliwości Azure AI Search, aby ulepszyć swoje rozwiązania wyszukiwania.

Aby uzyskać dodatkową pomoc, odwiedź [dokumentację Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.