<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T18:40:23+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "nl"
}
-->
# MCP Server Integratiegids

## Vereisten
- Node.js geïnstalleerd (versie 14 of hoger)
- npm pakketbeheerder
- Python-omgeving met vereiste afhankelijkheden

## Installatiestappen

1. **Installeer MCP Server-pakket**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Start MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   De server zou moeten starten en een verbindings-URL weergeven.

3. **Controleer verbinding**
   - Zoek naar het stekkericoon (🔌) in je Chainlit-interface
   - Er zou een nummer (1) naast het stekkericoon moeten verschijnen, wat aangeeft dat de verbinding succesvol is
   - De console zou moeten tonen: "GitHub plugin setup completed successfully" (samen met aanvullende statusregels)

## Problemen oplossen

### Veelvoorkomende problemen

1. **Poortconflict**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Oplossing: Wijzig de poort met:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Authenticatieproblemen**
   - Zorg ervoor dat GitHub-credentials correct zijn geconfigureerd
   - Controleer of het .env-bestand de vereiste tokens bevat
   - Verifieer toegang tot de GitHub API

3. **Verbinding mislukt**
   - Controleer of de server draait op de verwachte poort
   - Controleer firewall-instellingen
   - Verifieer dat de Python-omgeving de vereiste pakketten bevat

## Verificatie van verbinding

Je MCP-server is correct verbonden wanneer:
1. De console toont "GitHub plugin setup completed successfully"
2. Verbindingslogboeken tonen "✓ MCP Connection Status: Active"
3. GitHub-commando's werken in de chatinterface

## Omgevingsvariabelen

Vereist in je .env-bestand:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Verbinding testen

Stuur dit testbericht in de chat:
```
Show me the repositories for username: [GitHub Username]
```
Een succesvolle reactie toont informatie over de repository.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.