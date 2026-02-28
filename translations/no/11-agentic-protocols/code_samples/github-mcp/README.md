# Github MCP Server Eksempel

## Beskrivelse

Dette var en demo laget for AI Agents Hackathon arrangert gjennom Microsoft Reactor.

Verktøyet brukes til å anbefale hackathon-prosjekter basert på en brukers Github-repositorier.
Dette gjøres ved:

1. **Github Agent** - Bruke Github MCP Server for å hente repos og informasjon om disse repositoriene.
2. **Hackathon Agent** - Tar dataene fra Github Agent og kommer opp med kreative hackathon-prosjektideer basert på prosjektene, språkene som brukes av brukeren og prosjektsporene for AI Agents hackathon.
3. **Events Agent** - Basert på hackathon-agentens forslag, vil events-agenten anbefale relevante arrangementer fra AI Agent Hackathon-serien.
## Kjører koden

### Miljøvariabler

Denne demoen bruker Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server og Azure AI Search.

Sørg for at du har riktige miljøvariabler satt for å bruke disse verktøyene:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Kjøre Chainlit Server

For å koble til MCP-serveren bruker denne demoen Chainlit som chattegrensesnitt.

For å starte serveren, bruk følgende kommando i terminalen din:

```bash
chainlit run app.py -w
```

Dette skal starte Chainlit-serveren din på `localhost:8000` samt fylle Azure AI Search-indeksen din med `event-descriptions.md`-innholdet.

## Kobler til MCP Server

For å koble til Github MCP Server, velg "plug"-ikonet under chatteboksen "Type your message here..":

![MCP Connect](../../../../../translated_images/no/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Derfra kan du klikke på "Connect an MCP" for å legge til kommandoen for å koble til Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Erstatt "[YOUR PERSONAL ACCESS TOKEN]" med din faktiske Personal Access Token.

Etter tilkobling bør du se en (1) ved siden av plug-ikonet for å bekrefte at det er koblet til. Hvis ikke, prøv å starte chainlit-serveren på nytt med `chainlit run app.py -w`.

## Bruke Demoen

For å starte agentens arbeidsflyt for å anbefale hackathon-prosjekter, kan du skrive en melding som:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent vil analysere forespørselen din og avgjøre hvilken kombinasjon av agenter (GitHub, Hackathon og Events) som er best egnet til å håndtere forespørselen din. Agentene jobber sammen for å gi omfattende anbefalinger basert på analyse av GitHub-repositorier, prosjektideer og relevante teknologiske arrangementer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets originalspråk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->