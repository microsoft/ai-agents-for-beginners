<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:23:24+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "de"
}
-->
# Azure AI Search Einrichtungsanleitung

Diese Anleitung hilft Ihnen, Azure AI Search über das Azure-Portal einzurichten. Folgen Sie den untenstehenden Schritten, um Ihren Azure AI Search-Dienst zu erstellen und zu konfigurieren.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- Ein Azure-Abonnement. Falls Sie noch kein Azure-Abonnement haben, können Sie ein kostenloses Konto unter [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) erstellen.

## Schritt 1: Erstellen eines Azure Storage-Kontos

1. Folgen Sie dieser Anleitung, [Erstellen eines Azure Storage-Kontos](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), um ein neues Azure Storage-Konto zu erstellen.
   **NOTE**: Stellen Sie sicher, dass der Typ des Storage-Kontos "Standard General Purpose V2" ist.

## Schritt 2: Erstellen eines Azure AI Search-Dienstes

1. Melden Sie sich im [Azure-Portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) an.
2. Klicken Sie im Navigationsbereich auf der linken Seite auf **Ressource erstellen**.
3. Geben Sie im Suchfeld "Azure AI Search" ein und wählen Sie **Azure AI Search** aus der Ergebnisliste aus.
4. Klicken Sie auf die Schaltfläche **Erstellen**.
5. Geben Sie im Tab **Grundlagen** die folgenden Informationen ein:
   - **Abonnement**: Wählen Sie Ihr Azure-Abonnement aus.
   - **Ressourcengruppe**: Erstellen Sie eine neue Ressourcengruppe oder wählen Sie eine bestehende aus.
   - **Ressourcenname**: Geben Sie einen eindeutigen Namen für Ihren Suchdienst ein.
   - **Region**: Wählen Sie die Region, die Ihren Nutzern am nächsten ist.
   - **Preisstufe**: Wählen Sie eine Preisstufe, die Ihren Anforderungen entspricht. Sie können mit der kostenlosen Stufe für Tests beginnen.
6. Klicken Sie auf **Überprüfen + Erstellen**.
7. Überprüfen Sie die Einstellungen und klicken Sie auf **Erstellen**, um den Suchdienst zu erstellen.

## Schritt 3: Erste Schritte mit Azure AI Search

1. Sobald die Bereitstellung abgeschlossen ist, navigieren Sie zu Ihrem Suchdienst im Azure-Portal.
2. Kopieren Sie im Übersichtsbereich des Suchdienstes die URL. Sie sollte wie folgt aussehen: `https://<service-name>.search.windows.net`.
3. Kopieren Sie im Bereich Einstellungen > Schlüssel den Abfrageschlüssel.
4. Folgen Sie den Schritten auf der Seite [Schnellstart-Anleitung](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), um einen Index zu erstellen, Daten hochzuladen und eine Suchabfrage durchzuführen.

## Schritt 4: Verwendung von Azure AI Search-Tools

Azure AI Search integriert sich mit verschiedenen Tools, um Ihre Suchfunktionen zu verbessern. Sie können Azure CLI, Python SDK, .NET SDK und andere Tools für erweiterte Konfigurationen und Operationen verwenden.

### Verwendung von Azure CLI

1. Installieren Sie die Azure CLI, indem Sie den Anweisungen unter [Azure CLI installieren](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) folgen.
2. Melden Sie sich mit folgendem Befehl bei der Azure CLI an:

   ```bash
   az login
   ```

3. Speichern Sie sowohl den Endpunkt als auch den API-Schlüssel für die Azure AI Search-Instanz in Umgebungsvariablen.

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

### Verwendung des Python SDK

1. Installieren Sie die Azure Cognitive Search-Clientbibliothek für Python:

   ```bash
   pip install azure-search-documents
   ```

2. Verwenden Sie den folgenden Python-Code, um einen Index zu erstellen und Dokumente hochzuladen:

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

### Verwendung des .NET SDK

1. Führen Sie den folgenden Befehl aus, um einen Index zu erstellen und Dokumente hochzuladen:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Hier ist der .NET-Code von `AzureSearch.cs`:

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

Für detailliertere Informationen lesen Sie die folgende Dokumentation:

- [Erstellen eines Azure Cognitive Search-Dienstes](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Erste Schritte mit Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search-Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Fazit

Sie haben Azure AI Search erfolgreich über das Azure-Portal eingerichtet und Tools integriert. Sie können nun weitere erweiterte Funktionen und Möglichkeiten von Azure AI Search erkunden, um Ihre Suchlösungen zu verbessern.

Für weitere Unterstützung besuchen Sie die [Azure Cognitive Search-Dokumentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.