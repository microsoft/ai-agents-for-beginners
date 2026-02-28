# Github MCP Server Exempel

## Beskrivning

Detta var en demo skapad för AI Agents Hackathon som hölls via Microsoft Reactor.

Verktyget används för att rekommendera hackathonprojekt baserat på en användares Github repos.
Detta görs genom:

1. **Github Agent** - Använder Github MCP Server för att hämta repos och information om dessa repos.
2. **Hackathon Agent** - Tar datan från Github Agent och kommer på kreativa hackathonprojektidéer baserat på projekten, de språk användaren använder och projektspåren för AI Agents hackathon.
3. **Events Agent** - Baserat på Hackathon Agentens förslag kommer Events Agent att rekommendera relevanta evenemang från AI Agent Hackathon-serien.
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

För att starta servern, använd följande kommando i din terminal:

```bash
chainlit run app.py -w
```

Detta bör starta din Chainlit-server på `localhost:8000` samt fylla din Azure AI Search-index med innehållet i `event-descriptions.md`. 

## Ansluta till MCP-servern

För att ansluta till Github MCP Server, välj "plug" ikonen under chattrutan "Type your message here.." :

![MCP Anslut](../../../../../translated_images/sv/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Därifrån kan du klicka på "Connect an MCP" för att lägga till kommandot för att ansluta till Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Ersätt "[YOUR PERSONAL ACCESS TOKEN]" med din faktiska Personal Access Token. 

Efter anslutning bör du se en (1) bredvid plug-ikonen för att bekräfta att den är ansluten. Om inte, försök starta om chainlit-servern med `chainlit run app.py -w`.

## Använda demon 

För att starta agentarbetsflödet för att rekommendera hackathonprojekt kan du skriva ett meddelande som: 

"Rekommendera hackathonprojekt för Github-användaren koreyspace"

Router Agent kommer att analysera din förfrågan och avgöra vilken kombination av agenter (GitHub, Hackathon, och Events) som passar bäst för att hantera din fråga. Agenterna arbetar tillsammans för att ge omfattande rekommendationer baserade på analys av GitHub-repositorier, projektidéer och relevanta tech-evenemang.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfriskrivning:
Detta dokument har översatts med hjälp av AI-översättningstjänsten Co-op Translator (https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Originaldokumentet på dess ursprungsspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->