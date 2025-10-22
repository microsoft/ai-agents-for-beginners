<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:33:07+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "de"
}
-->
# Azure AI Search Einrichtungsanleitung

Diese Anleitung hilft Ihnen dabei, Azure AI Search über das Azure-Portal einzurichten. Folgen Sie den untenstehenden Schritten, um Ihren Azure AI Search-Dienst zu erstellen und zu konfigurieren.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- Ein Azure-Abonnement. Falls Sie noch kein Azure-Abonnement besitzen, können Sie ein kostenloses Konto unter [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) erstellen.

## Schritt 1: Erstellen eines Azure AI Search-Dienstes

1. Melden Sie sich im [Azure-Portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) an.
2. Klicken Sie im linken Navigationsbereich auf **Create a resource**.
3. Geben Sie im Suchfeld „Azure AI Search“ ein und wählen Sie **Azure AI Search** aus der Ergebnisliste aus.
4. Klicken Sie auf die Schaltfläche **Create**.
5. Geben Sie im Tab **Basics** folgende Informationen ein:
   - **Subscription**: Wählen Sie Ihr Azure-Abonnement aus.
   - **Resource group**: Erstellen Sie eine neue Ressourcengruppe oder wählen Sie eine vorhandene aus.
   - **Resource name**: Geben Sie einen eindeutigen Namen für Ihren Suchdienst ein.
   - **Region**: Wählen Sie die Region aus, die Ihren Nutzern am nächsten liegt.
   - **Pricing tier**: Wählen Sie einen Tarif, der Ihren Anforderungen entspricht. Für Tests können Sie mit dem Free-Tarif beginnen.
6. Klicken Sie auf **Review + create**.
7. Überprüfen Sie die Einstellungen und klicken Sie auf **Create**, um den Suchdienst zu erstellen.

## Schritt 2: Erste Schritte mit Azure AI Search

1. Nach Abschluss der Bereitstellung navigieren Sie im Azure-Portal zu Ihrem Suchdienst.
2. Klicken Sie auf der Übersichtsseite des Suchdienstes auf die Schaltfläche **Quickstart**.
3. Folgen Sie den Schritten im Quickstart-Leitfaden, um einen Index zu erstellen, Daten hochzuladen und eine Suchanfrage durchzuführen.

### Einen Index erstellen

1. Klicken Sie im Quickstart-Leitfaden auf **Create an index**.
2. Definieren Sie das Indexschema, indem Sie die Felder und deren Eigenschaften (z. B. Datentyp, durchsuchbar, filterbar) festlegen.
3. Klicken Sie auf **Create**, um den Index zu erstellen.

### Daten hochladen

1. Klicken Sie im Quickstart-Leitfaden auf **Upload data**.
2. Wählen Sie eine Datenquelle (z. B. Azure Blob Storage, Azure SQL Database) aus und geben Sie die erforderlichen Verbindungsdetails ein.
3. Ordnen Sie die Felder der Datenquelle den Indexfeldern zu.
4. Klicken Sie auf **Submit**, um die Daten in den Index hochzuladen.

### Eine Suchanfrage durchführen

1. Klicken Sie im Quickstart-Leitfaden auf **Search explorer**.
2. Geben Sie eine Suchanfrage in das Suchfeld ein, um die Suchfunktion zu testen.
3. Überprüfen Sie die Suchergebnisse und passen Sie bei Bedarf das Indexschema oder die Daten an.

## Schritt 3: Azure AI Search Tools verwenden

Azure AI Search lässt sich mit verschiedenen Tools integrieren, um Ihre Suchfunktionen zu erweitern. Sie können Azure CLI, Python SDK und weitere Tools für erweiterte Konfigurationen und Operationen nutzen.

### Verwendung der Azure CLI

1. Installieren Sie die Azure CLI, indem Sie den Anweisungen unter [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) folgen.
2. Melden Sie sich mit folgendem Befehl bei der Azure CLI an:
   ```bash
   az login
   ```
3. Erstellen Sie einen neuen Suchdienst mit der Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Erstellen Sie einen Index mit der Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Verwendung des Python SDK

1. Installieren Sie die Azure Cognitive Search Clientbibliothek für Python:
   ```bash
   pip install azure-search-documents
   ```
2. Verwenden Sie den folgenden Python-Code, um einen Index zu erstellen und Dokumente hochzuladen:
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

Für detailliertere Informationen konsultieren Sie bitte die folgenden Dokumentationen:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Fazit

Sie haben Azure AI Search erfolgreich über das Azure-Portal und die integrierten Tools eingerichtet. Nun können Sie weitere erweiterte Funktionen und Möglichkeiten von Azure AI Search erkunden, um Ihre Suchlösungen zu optimieren.

Für weitere Unterstützung besuchen Sie die [Azure Cognitive Search Dokumentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.