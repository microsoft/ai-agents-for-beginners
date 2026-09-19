# Azure AI Search Einrichtungshandbuch

Dieser Leitfaden hilft Ihnen bei der Einrichtung von Azure AI Search über das Azure-Portal. Folgen Sie den untenstehenden Schritten, um Ihren Azure AI Search-Dienst zu erstellen und zu konfigurieren.

## Voraussetzungen

Stellen Sie vor Beginn sicher, dass Sie Folgendes haben:

- Ein Azure-Abonnement. Wenn Sie kein Azure-Abonnement haben, können Sie ein kostenloses Konto unter [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) erstellen.

## Schritt 1: Erstellen eines Azure Storage-Kontos

1. Befolgen Sie diese Anleitung, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), um ein neues Azure Storage-Konto zu erstellen.
   **HINWEIS**: Stellen Sie sicher, dass der Typ des Storage-Kontos "Standard General Purpose V2" ist.

## Schritt 2: Erstellen eines Azure AI Search-Dienstes

1. Melden Sie sich im [Azure-Portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) an.
2. Klicken Sie im linken Navigationsbereich auf **Ressource erstellen**.
3. Geben Sie im Suchfeld „Azure AI Search“ ein und wählen Sie **Azure AI Search** aus der Ergebnisliste aus.
4. Klicken Sie auf die Schaltfläche **Erstellen**.
5. Geben Sie im Tab **Grundlagen** die folgenden Informationen ein:
   - **Abonnement**: Wählen Sie Ihr Azure-Abonnement aus.
   - **Resource Group**: Erstellen Sie eine neue Ressourcengruppe oder wählen Sie eine vorhandene aus.
   - **Ressourcename**: Geben Sie einen eindeutigen Namen für Ihren Suchdienst ein.
   - **Region**: Wählen Sie die Region, die Ihren Benutzern am nächsten ist.
   - **Preisstufe**: Wählen Sie eine Preisstufe, die Ihren Anforderungen entspricht. Für Tests können Sie mit der kostenlosen Stufe beginnen.
6. Klicken Sie auf **Überprüfen + erstellen**.
7. Überprüfen Sie die Einstellungen und klicken Sie auf **Erstellen**, um den Suchdienst zu erstellen.

## Schritt 3: Einstieg in Azure AI Search

1. Sobald die Bereitstellung abgeschlossen ist, navigieren Sie zu Ihrem Suchdienst im Azure-Portal.
2. Kopieren Sie im Übersichtsbereich des Suchdienstes die URL. Diese sollte wie `https://<service-name>.search.windows.net` aussehen.
3. **(Empfohlen)** Aktivieren Sie den schlüssellosen Zugriff mit Microsoft Entra ID (RBAC), wie in Schritt 4 unten gezeigt — kein Schlüssel erforderlich. Die Beispiele in diesem Handbuch erstellen/aktualisieren Indizes und laden Dokumente hoch, wofür die Rollen **Search Service Contributor** und **Search Index Data Contributor** erforderlich sind (oder für die schlüsselbasierte Authentifizierung der **primäre Administrationsschlüssel** — nicht der Abfrageschlüssel). Nur wenn Sie RBAC nicht verwenden können, öffnen Sie das Menü **Einstellungen > Schlüssel** und kopieren Sie den **primären Administrationsschlüssel**.
4. Folgen Sie den Schritten in der [Schnellstartanleitung](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), um einen Index zu erstellen, Daten hochzuladen und eine Suche durchzuführen.

## Schritt 4: Verwendung von Azure AI Search Tools

Azure AI Search integriert verschiedene Tools, um Ihre Suchfunktionen zu erweitern. Sie können die Azure CLI, das Python SDK, das .NET SDK und andere Tools für erweiterte Konfigurationen und Operationen verwenden.

### Verwendung der Azure CLI

1. Installieren Sie die Azure CLI, indem Sie den Anweisungen unter [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) folgen.
2. Melden Sie sich mit dem Befehl bei der Azure CLI an:

   ```bash
   az login
   ```
3. **(Empfohlen) Aktivieren Sie den schlüssellosen Zugriff mit Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show hat kein "endpoint"-Feld; die URL wird aus dem Dienstnamen erstellt.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Mit aktiviertem RBAC authentifizieren sich die unten stehenden Python- und .NET-SDK-Beispiele über `DefaultAzureCredential`, der während der lokalen Entwicklung Ihre `az login`-Sitzung verwendet — kein Administrationsschlüssel erforderlich. Weitere Informationen finden Sie unter [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternativ) Schlüsselbasierte Authentifizierung** — nur wenn Sie RBAC nicht verwenden können, speichern Sie auch den Administrationsschlüssel:

#### Speichern Sie sowohl Endpoint als auch API-Schlüssel der Azure AI Search-Instanz in Umgebungsvariablen.

    ```bash
    # zsh/bash
    # az search service show hat kein "endpoint"-Feld; bauen Sie die URL aus dem Servicenamen zusammen.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show hat kein "endpoint"-Feld; bauen Sie die URL aus dem Servicenamen zusammen.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Verwendung des Python SDK

1. Installieren Sie die Clientbibliothek Azure Cognitive Search und Azure Identity für Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Verwenden Sie den folgenden Python-Code, um einen Index zu erstellen und Dokumente hochzuladen:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (empfohlen): verwendet Ihre `az login` Identität über Entra ID RBAC.
    # Erfordert die Rollen "Search Service Contributor" und "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Fallback (schlüsselbasierte Authentifizierung):
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

### Verwendung des .NET SDK

1. Führen Sie den folgenden Befehl aus, um einen Index zu erstellen und Dokumente hochzuladen:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Das .NET-Beispiel unten verwendet `DefaultAzureCredential`, das Ihr Azure CLI-Anmeldeverfahren von `az login` während der lokalen Entwicklung nutzen kann.

2. Hier ist der .NET-Code von `AzureSearch.cs`:

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

Für detailliertere Informationen lesen Sie bitte die folgende Dokumentation:

- [Erstellen eines Azure Cognitive Search-Dienstes](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Erste Schritte mit Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Fazit

Sie haben Azure AI Search erfolgreich über das Azure-Portal eingerichtet und in Tools integriert. Nun können Sie weitere fortgeschrittene Funktionen und Möglichkeiten von Azure AI Search erkunden, um Ihre Suchlösungen zu verbessern.

Für weitere Unterstützung besuchen Sie die [Azure Cognitive Search-Dokumentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->