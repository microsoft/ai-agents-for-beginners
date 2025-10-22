<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-30T14:59:35+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "de"
}
-->
# MCP Server-Integrationsleitfaden

## Voraussetzungen
- Installiertes Node.js (Version 14 oder höher)
- npm-Paketmanager
- Python-Umgebung mit den erforderlichen Abhängigkeiten

## Einrichtungsschritte

1. **MCP Server-Paket installieren**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **MCP Server starten**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Der Server sollte starten und eine Verbindungs-URL anzeigen.

3. **Verbindung überprüfen**  
   - Suchen Sie nach dem Stecker-Symbol (🔌) in Ihrer Chainlit-Oberfläche  
   - Eine Zahl (1) sollte neben dem Stecker-Symbol erscheinen, was auf eine erfolgreiche Verbindung hinweist  
   - Die Konsole sollte anzeigen: "GitHub plugin setup completed successfully" (zusammen mit zusätzlichen Statusmeldungen)

## Fehlerbehebung

### Häufige Probleme

1. **Port-Konflikt**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Lösung: Ändern Sie den Port mit:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Authentifizierungsprobleme**  
   - Stellen Sie sicher, dass die GitHub-Zugangsdaten korrekt konfiguriert sind  
   - Überprüfen Sie, ob die .env-Datei die erforderlichen Tokens enthält  
   - Vergewissern Sie sich, dass der Zugriff auf die GitHub-API funktioniert

3. **Verbindung fehlgeschlagen**  
   - Überprüfen Sie, ob der Server auf dem erwarteten Port läuft  
   - Prüfen Sie die Firewall-Einstellungen  
   - Stellen Sie sicher, dass die Python-Umgebung die erforderlichen Pakete enthält

## Verbindungsüberprüfung

Ihr MCP-Server ist ordnungsgemäß verbunden, wenn:  
1. Die Konsole "GitHub plugin setup completed successfully" anzeigt  
2. Die Verbindungsprotokolle "✓ MCP Connection Status: Active" anzeigen  
3. GitHub-Befehle in der Chat-Oberfläche funktionieren

## Umgebungsvariablen

Erforderlich in Ihrer .env-Datei:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Verbindung testen

Senden Sie diese Testnachricht im Chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Eine erfolgreiche Antwort zeigt Informationen zum Repository an.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.