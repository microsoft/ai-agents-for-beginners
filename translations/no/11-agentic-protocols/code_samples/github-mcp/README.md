<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T16:09:21+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "no"
}
-->
# Github MCP Server Eksempel

## Beskrivelse

Dette er en demo laget for AI Agents Hackathon arrangert gjennom Microsoft Reactor.

Verktøyet brukes til å anbefale hackathon-prosjekter basert på en brukers Github-repos. Dette gjøres ved:

1. **Github Agent** - Bruker Github MCP Server for å hente repos og informasjon om disse reposene.
2. **Hackathon Agent** - Tar data fra Github Agent og kommer opp med kreative hackathon-prosjektideer basert på prosjektene, språkene som brukes av brukeren, og prosjektsporene for AI Agents hackathon.
3. **Events Agent** - Basert på forslagene fra Hackathon Agent, vil Events Agent anbefale relevante arrangementer fra AI Agent Hackathon-serien.

## Kjøre koden 

### Miljøvariabler

Denne demoen bruker Azure Open AI Service, Semantic Kernel, Github MCP Server og Azure AI Search.

Sørg for at du har de riktige miljøvariablene satt opp for å bruke disse verktøyene:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Kjøre Chainlit Server

For å koble til MCP-serveren bruker denne demoen Chainlit som en chat-grensesnitt.

For å starte serveren, bruk følgende kommando i terminalen:

```bash
chainlit run app.py -w
```

Dette bør starte Chainlit-serveren din på `localhost:8000` og fylle Azure AI Search Index med innholdet fra `event-descriptions.md`.

## Koble til MCP Server

For å koble til Github MCP Server, velg "plug"-ikonet under "Type your message here.." chat-boksen:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.no.png)

Derfra kan du klikke på "Connect an MCP" for å legge til kommandoen for å koble til Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Erstatt "[YOUR PERSONAL ACCESS TOKEN]" med din faktiske Personal Access Token.

Etter tilkobling, bør du se en (1) ved siden av plug-ikonet som bekrefter at det er koblet til. Hvis ikke, prøv å starte Chainlit-serveren på nytt med `chainlit run app.py -w`.

## Bruke demoen 

For å starte agentarbeidsflyten med å anbefale hackathon-prosjekter, kan du skrive en melding som:

"Anbefal hackathon-prosjekter for Github-brukeren koreyspace"

Router Agent vil analysere forespørselen din og avgjøre hvilken kombinasjon av agenter (GitHub, Hackathon og Events) som er best egnet til å håndtere forespørselen din. Agentene samarbeider for å gi omfattende anbefalinger basert på analyse av Github-repositorier, prosjektideer og relevante teknologiske arrangementer.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.