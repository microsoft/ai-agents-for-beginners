<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T16:15:13+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "sv"
}
-->
# MCP Server Integrationsguide

## Förutsättningar
- Node.js installerat (version 14 eller högre)
- npm-pakethanterare
- Python-miljö med nödvändiga beroenden

## Installationssteg

1. **Installera MCP Server-paketet**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Starta MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Servern bör starta och visa en anslutnings-URL.

3. **Verifiera anslutning**
   - Leta efter plug-ikonen (🔌) i ditt Chainlit-gränssnitt  
   - En siffra (1) bör visas bredvid plug-ikonen som indikerar en lyckad anslutning  
   - Konsolen bör visa: "GitHub plugin setup completed successfully" (tillsammans med ytterligare statusrader)

## Felsökning

### Vanliga problem

1. **Portkonflikt**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Lösning: Ändra porten med:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Autentiseringsproblem**
   - Kontrollera att GitHub-uppgifterna är korrekt konfigurerade  
   - Kontrollera att .env-filen innehåller nödvändiga tokens  
   - Verifiera åtkomst till GitHub API  

3. **Anslutning misslyckades**
   - Bekräfta att servern körs på förväntad port  
   - Kontrollera brandväggsinställningar  
   - Verifiera att Python-miljön har nödvändiga paket  

## Verifiering av anslutning

Din MCP-server är korrekt ansluten när:  
1. Konsolen visar "GitHub plugin setup completed successfully"  
2. Anslutningsloggar visar "✓ MCP Connection Status: Active"  
3. GitHub-kommandon fungerar i chattgränssnittet  

## Miljövariabler

Krävs i din .env-fil:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testa anslutning

Skicka detta testmeddelande i chatten:  
```
Show me the repositories for username: [GitHub Username]
```  
Ett lyckat svar kommer att visa information om repository.  

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.