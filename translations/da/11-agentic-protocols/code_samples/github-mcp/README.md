<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T16:09:09+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "da"
}
-->
# Github MCP Server Eksempel

## Beskrivelse

Dette er en demo, der blev skabt til AI Agents Hackathon, arrangeret af Microsoft Reactor.

Værktøjet bruges til at anbefale hackathon-projekter baseret på en brugers Github-repos. Dette gøres ved hjælp af:

1. **Github Agent** - Bruger Github MCP Server til at hente repos og information om disse repos.
2. **Hackathon Agent** - Tager data fra Github Agent og udarbejder kreative hackathon-projektidéer baseret på projekterne, de anvendte programmeringssprog og projektsporene for AI Agents Hackathon.
3. **Events Agent** - Baseret på Hackathon Agents forslag vil Events Agent anbefale relevante events fra AI Agent Hackathon-serien.

## Kørsel af koden

### Miljøvariabler

Denne demo bruger Azure Open AI Service, Semantic Kernel, Github MCP Server og Azure AI Search.

Sørg for, at du har de korrekte miljøvariabler sat op for at bruge disse værktøjer:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Kørsel af Chainlit Server

For at forbinde til MCP-serveren bruger denne demo Chainlit som en chatgrænseflade.

For at køre serveren skal du bruge følgende kommando i din terminal:

```bash
chainlit run app.py -w
```

Dette bør starte din Chainlit-server på `localhost:8000` og samtidig udfylde din Azure AI Search Index med indholdet fra `event-descriptions.md`.

## Forbindelse til MCP Server

For at forbinde til Github MCP Server skal du vælge "stik"-ikonet under chatboksen "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.da.png)

Herfra kan du klikke på "Connect an MCP" for at tilføje kommandoen til at forbinde til Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Erstat "[YOUR PERSONAL ACCESS TOKEN]" med din faktiske personlige adgangstoken.

Efter tilslutning bør du se et (1) ved siden af stik-ikonet for at bekræfte, at forbindelsen er oprettet. Hvis ikke, prøv at genstarte Chainlit-serveren med `chainlit run app.py -w`.

## Brug af demoen

For at starte agentarbejdsgangen med at anbefale hackathon-projekter kan du skrive en besked som:

"Anbefal hackathon-projekter til Github-brugeren koreyspace"

Router Agent vil analysere din forespørgsel og afgøre, hvilken kombination af agenter (GitHub, Hackathon og Events) der bedst kan håndtere din forespørgsel. Agenterne arbejder sammen for at levere omfattende anbefalinger baseret på analyse af Github-repositories, projektidéer og relevante teknologibegivenheder.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.