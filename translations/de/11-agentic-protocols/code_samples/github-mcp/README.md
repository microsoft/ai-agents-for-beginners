# Github MCP Server Beispiel

## Beschreibung

Dies war eine Demo, die für den AI Agents Hackathon erstellt wurde, der vom Microsoft Reactor veranstaltet wurde.

Das Tool wird verwendet, um Hackathon-Projekte basierend auf den Github-Repositories eines Benutzers zu empfehlen.
Dies geschieht durch:

1. **Github Agent** - Verwendet den Github MCP Server, um Repositories und Informationen über diese Repositories abzurufen.
2. **Hackathon Agent** - Nimmt die Daten des Github Agent und entwickelt kreative Hackathon-Projektideen basierend auf den Projekten, den vom Benutzer verwendeten Sprachen und den Projekttracks des AI Agents Hackathons.
3. **Events Agent** - Basierend auf den Vorschlägen des Hackathon-Agenten empfiehlt der Events Agent relevante Veranstaltungen aus der AI Agent Hackathon-Serie.
## Ausführen des Codes 

### Umgebungsvariablen

Diese Demo verwendet Microsoft Agent Framework, Azure OpenAI Service, den Github MCP Server und Azure AI Search.

Stellen Sie sicher, dass Sie die entsprechenden Umgebungsvariablen gesetzt haben, um diese Tools zu verwenden:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Starten des Chainlit-Servers

Um eine Verbindung zum MCP-Server herzustellen, verwendet diese Demo Chainlit als Chat-Oberfläche. 

Um den Server zu starten, verwenden Sie im Terminal den folgenden Befehl:

```bash
chainlit run app.py -w
```

Dadurch sollte Ihr Chainlit-Server auf `localhost:8000` gestartet werden und gleichzeitig Ihr Azure AI Search Index mit dem Inhalt der Datei `event-descriptions.md` gefüllt werden. 

## Verbindung zum MCP-Server

Um eine Verbindung zum Github MCP Server herzustellen, wählen Sie das "Stecker"-Symbol unter dem Chatfeld "Geben Sie hier Ihre Nachricht ein.." aus:

![MCP verbinden](../../../../../translated_images/de/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Dort können Sie auf "Mit einem MCP verbinden" klicken, um den Befehl hinzuzufügen, der die Verbindung zum Github MCP Server herstellt:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Ersetzen Sie "[YOUR PERSONAL ACCESS TOKEN]" durch Ihr tatsächliches Zugriffstoken. 

Nach dem Verbinden sollten Sie eine (1) neben dem Stecker-Symbol sehen, um zu bestätigen, dass die Verbindung hergestellt ist. Falls nicht, versuchen Sie, den Chainlit-Server mit `chainlit run app.py -w` neu zu starten.

## Verwendung der Demo 

Um den Agenten-Workflow zu starten, der Hackathon-Projekte empfiehlt, können Sie eine Nachricht wie die folgende eingeben: 

"Empfehle Hackathon-Projekte für den Github-Benutzer koreyspace"

Der Router-Agent analysiert Ihre Anfrage und ermittelt, welche Kombination von Agenten (GitHub, Hackathon und Events) am besten geeignet ist, Ihre Anfrage zu bearbeiten. Die Agenten arbeiten zusammen, um umfassende Empfehlungen auf der Grundlage der Analyse der GitHub-Repositories, der Projektideen und relevanter Tech-Veranstaltungen zu liefern.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst Co-op Translator (https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Die Originalfassung in der jeweiligen Ausgangssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen, übernehmen wir keine Haftung.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->