# Github MCP Server Example

## Description

Dette var en demo oprettet til AI Agents Hackathonet afholdt gennem Microsoft Reactor.

Værktøjet bruges til at anbefale hackathonprojekter baseret på en brugers Github-repos.
Dette gøres ved:

1. **Github Agent** - Ved at bruge Github MCP Serveren til at hente repositories og information om disse repositories.
2. **Hackathon Agent** - Tager data fra Github Agenten og finder på kreative hackathon-projektidéer baseret på projekterne, de sprog brugeren benytter, og projektsporene for AI Agents hackathonet.
3. **Events Agent** - Baseret på Hackathon Agentens forslag anbefaler Events Agent relevante events fra AI Agent Hackathon-serien.
## Running the code 

### Environment Variables

Denne demo bruger Microsoft Agent Framework, Azure OpenAI Service, Github MCP Serveren og Azure AI Search.

Sørg for, at du har de korrekte miljøvariabler sat for at bruge disse værktøjer:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

For at oprette forbindelse til MCP-serveren bruger denne demo Chainlit som en chatgrænseflade. 

For at køre serveren skal du bruge følgende kommando i din terminal:

```bash
chainlit run app.py -w
```

Dette burde starte din Chainlit-server på `localhost:8000` samt udfylde din Azure AI Search Index med indholdet fra `event-descriptions.md`. 

## Connecting to the MCP Server

For at oprette forbindelse til Github MCP Serveren skal du vælge "stik"-ikonet under chatboksen "Type your message here..":

![MCP-forbindelse](../../../../../translated_images/da/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Derfra kan du klikke på "Connect an MCP" for at tilføje kommandoen til at forbinde til Github MCP Serveren:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Erstat "[YOUR PERSONAL ACCESS TOKEN]" med dit faktiske Personal Access Token. 

Efter tilslutning bør du se et (1) ved siden af stik-ikonet for at bekræfte, at det er forbundet. Hvis ikke, så prøv at genstarte chainlit-serveren med `chainlit run app.py -w`.

## Using the Demo 

For at starte agentworkflowet med at anbefale hackathonprojekter kan du skrive en besked som for eksempel: 

"Anbefal hackathonprojekter for Github-brugeren koreyspace"

Router Agenten vil analysere din forespørgsel og afgøre, hvilken kombination af agenter (GitHub, Hackathon og Events) der er bedst egnet til at håndtere din forespørgsel. Agentene arbejder sammen for at give omfattende anbefalinger baseret på analyse af GitHub-repositories, idéudvikling til projekter og relevante teknologiske events.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten Co-op Translator (https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales en professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->