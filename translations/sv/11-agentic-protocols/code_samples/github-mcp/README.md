# Github MCP Server Exempel

## Beskrivning

Detta var en demo skapad för AI Agents Hackathon som arrangerades genom Microsoft Reactor.

Verktyget används för att rekommendera hackathon-projekt baserat på en användares Github-repos.
Detta görs genom:

1. **Github Agent** - Använder Github MCP Server för att hämta repos och information om dessa repos.
2. **Hackathon Agent** - Tar datan från Github Agent och kommer på kreativa hackathon-projektidéer baserat på projekten, de språk användaren använder och projektspåren för AI Agents hackathon.
3. **Events Agent** - Baserat på förslagen från hackathon-agenten kommer events-agenten rekommendera relevanta evenemang från AI Agent Hackathon-serien.
## Köra koden 

### Miljövariabler

Denna demo använder Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server och Azure AI Search.

Se till att du har rätt miljövariabler inställda för att använda dessa verktyg:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Köra Chainlit-servern

För att ansluta till MCP-servern använder denna demo Chainlit som ett chattgränssnitt. 

För att köra servern, använd följande kommando i din terminal:

```bash
chainlit run app.py -w
```

Detta bör starta din Chainlit-server på `localhost:8000` samt fylla din Azure AI Search-index med innehållet i `event-descriptions.md`. 

## Ansluta till MCP-servern

För att ansluta till Github MCP Server, välj "plug"-ikonen under chattrutan "Type your message here..":

![MCP-anslutning](../../../../../translated_images/sv/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Därifrån kan du klicka på "Connect an MCP" för att lägga till kommandot som ansluter till Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Ersätt "[YOUR PERSONAL ACCESS TOKEN]" med din verkliga Personal Access Token. 

Efter anslutning bör du se en (1) bredvid plug-ikonen för att bekräfta att den är ansluten. Om inte, prova att starta om chainlit-servern med `chainlit run app.py -w`.

## Använda demon 

För att starta agentarbetsflödet för att rekommendera hackathon-projekt kan du skriva ett meddelande som: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent kommer analysera din förfrågan och avgöra vilken kombination av agenter (GitHub, Hackathon och Events) som är bäst lämpad att hantera din fråga. Agenternas samarbete ger omfattande rekommendationer baserade på analys av GitHub-repositorier, projektidéer och relevanta teknikevenemang.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller felaktigheter. Den ursprungliga versionen av dokumentet på dess ursprungsspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas en professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår genom användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->