<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T11:58:03+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "de"
}
-->
# Lektion 11: Integration des Model Context Protocol (MCP)

## Einführung in das Model Context Protocol (MCP)

Das Model Context Protocol (MCP) ist ein hochmodernes Framework, das entwickelt wurde, um die Interaktionen zwischen KI-Modellen und Client-Anwendungen zu standardisieren. MCP fungiert als Brücke zwischen KI-Modellen und den Anwendungen, die sie nutzen, und bietet eine einheitliche Schnittstelle, unabhängig von der zugrunde liegenden Modellimplementierung.

Wesentliche Aspekte von MCP:

- **Standardisierte Kommunikation**: MCP schafft eine gemeinsame Sprache, mit der Anwendungen mit KI-Modellen kommunizieren können.
- **Verbessertes Kontextmanagement**: Ermöglicht die effiziente Übergabe von Kontextinformationen an KI-Modelle.
- **Plattformübergreifende Kompatibilität**: Funktioniert mit verschiedenen Programmiersprachen wie C#, Java, JavaScript, Python und TypeScript.
- **Nahtlose Integration**: Erleichtert Entwicklern die Integration verschiedener KI-Modelle in ihre Anwendungen.

MCP ist besonders wertvoll bei der Entwicklung von KI-Agenten, da es Agenten ermöglicht, über ein einheitliches Protokoll mit verschiedenen Systemen und Datenquellen zu interagieren. Dadurch werden die Agenten flexibler und leistungsfähiger.

## Lernziele
- Verstehen, was MCP ist und welche Rolle es bei der Entwicklung von KI-Agenten spielt
- Einrichten und Konfigurieren eines MCP-Servers für die GitHub-Integration
- Aufbau eines Multi-Agenten-Systems mit MCP-Tools
- Implementierung von RAG (Retrieval Augmented Generation) mit Azure Cognitive Search

## Voraussetzungen
- Python 3.8+
- Node.js 14+
- Azure-Abonnement
- GitHub-Konto
- Grundlegendes Verständnis des Semantic Kernel

## Einrichtungsanweisungen

1. **Umgebung einrichten**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure-Dienste konfigurieren**
   - Erstellen einer Azure Cognitive Search-Ressource
   - Einrichten des Azure OpenAI-Dienstes
   - Konfigurieren der Umgebungsvariablen in `.env`

3. **MCP-Server einrichten**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Projektstruktur

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Kernkomponenten

### 1. Multi-Agenten-System
- GitHub-Agent: Analyse von Repositories
- Hackathon-Agent: Projektvorschläge
- Event-Agent: Vorschläge für Technologie-Events

### 2. Azure-Integration
- Cognitive Search für die Indexierung von Events
- Azure OpenAI für die Intelligenz der Agenten
- Implementierung des RAG-Musters

### 3. MCP-Tools
- Analyse von GitHub-Repositories
- Code-Inspektion
- Metadatenextraktion

## Code-Durchlauf

Das Beispiel zeigt:
1. Integration des MCP-Servers
2. Orchestrierung von Multi-Agenten
3. Integration von Azure Cognitive Search
4. Implementierung des RAG-Musters

Wichtige Funktionen:
- Echtzeit-Analyse von GitHub-Repositories
- Intelligente Projektvorschläge
- Event-Matching mit Azure Search
- Streaming-Antworten mit Chainlit

## Ausführen des Beispiels

Für detaillierte Einrichtungsanweisungen und weitere Informationen siehe die [GitHub MCP Server Example README](./code_samples/github-mcp/README.md).

1. Starten Sie den MCP-Server:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Starten Sie die Anwendung:  
   ```bash
   chainlit run app.py -w
   ```

3. Testen Sie die Integration:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Fehlerbehebung

Häufige Probleme und Lösungen:
1. MCP-Verbindungsprobleme
   - Überprüfen, ob der Server läuft
   - Verfügbarkeit des Ports prüfen
   - GitHub-Tokens überprüfen

2. Probleme mit Azure Search
   - Verbindungszeichenfolgen validieren
   - Existenz des Indexes prüfen
   - Hochladen von Dokumenten überprüfen

## Nächste Schritte
- Weitere MCP-Tools erkunden
- Eigene Agenten implementieren
- RAG-Funktionen erweitern
- Weitere Event-Quellen hinzufügen
- **Fortgeschritten**: Schauen Sie sich [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) für Beispiele zur Kommunikation zwischen Agenten an

## Ressourcen
- [MCP für Einsteiger](https://aka.ms/mcp-for-beginners)  
- [MCP-Dokumentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search-Dokumentation](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel-Anleitungen](https://learn.microsoft.com/semantic-kernel/)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.