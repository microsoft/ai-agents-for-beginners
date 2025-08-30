<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T10:28:24+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "de"
}
-->
# Github MCP Server Beispiel

## Beschreibung

Dies ist eine Demo, die für den AI Agents Hackathon erstellt wurde, der über den Microsoft Reactor veranstaltet wurde.

Das Tool wird verwendet, um Hackathon-Projekte basierend auf den Github-Repos eines Benutzers zu empfehlen. Dies geschieht durch:

1. **Github Agent** - Verwendet den Github MCP Server, um Repos und Informationen über diese Repos abzurufen.
2. **Hackathon Agent** - Nutzt die Daten des Github Agents, um kreative Hackathon-Projektideen basierend auf den Projekten, den vom Benutzer verwendeten Programmiersprachen und den Projekttracks des AI Agents Hackathon zu entwickeln.
3. **Events Agent** - Basierend auf den Vorschlägen des Hackathon Agents empfiehlt der Events Agent relevante Veranstaltungen aus der AI Agent Hackathon-Serie.

## Code ausführen

### Umgebungsvariablen

Diese Demo verwendet Azure Open AI Service, Semantic Kernel, den Github MCP Server und Azure AI Search.

Stellen Sie sicher, dass Sie die richtigen Umgebungsvariablen gesetzt haben, um diese Tools zu nutzen:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Den Chainlit Server starten

Um eine Verbindung zum MCP Server herzustellen, verwendet diese Demo Chainlit als Chat-Schnittstelle.

Um den Server zu starten, verwenden Sie den folgenden Befehl in Ihrem Terminal:

```bash
chainlit run app.py -w
```

Dies sollte Ihren Chainlit Server auf `localhost:8000` starten und Ihren Azure AI Search Index mit dem Inhalt von `event-descriptions.md` füllen.

## Verbindung zum MCP Server herstellen

Um eine Verbindung zum Github MCP Server herzustellen, klicken Sie auf das "Stecker"-Symbol unterhalb des Chat-Feldes "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.de.png)

Von dort aus können Sie auf "Connect an MCP" klicken, um den Befehl hinzuzufügen, der die Verbindung zum Github MCP Server herstellt:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Ersetzen Sie "[YOUR PERSONAL ACCESS TOKEN]" durch Ihren tatsächlichen Personal Access Token.

Nach der Verbindung sollte ein (1) neben dem Stecker-Symbol erscheinen, um zu bestätigen, dass die Verbindung hergestellt wurde. Falls nicht, versuchen Sie, den Chainlit Server mit `chainlit run app.py -w` neu zu starten.

## Die Demo verwenden

Um den Agenten-Workflow zur Empfehlung von Hackathon-Projekten zu starten, können Sie eine Nachricht wie diese eingeben:

"Empfehle Hackathon-Projekte für den Github-Benutzer koreyspace"

Der Router Agent analysiert Ihre Anfrage und bestimmt, welche Kombination von Agenten (GitHub, Hackathon und Events) am besten geeignet ist, Ihre Anfrage zu bearbeiten. Die Agenten arbeiten zusammen, um umfassende Empfehlungen basierend auf der Analyse von Github-Repositories, der Entwicklung von Projektideen und relevanten Technologieveranstaltungen bereitzustellen.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.