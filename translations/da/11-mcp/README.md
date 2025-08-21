<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:27:28+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "da"
}
-->
# Lektion 11: Integration af Model Context Protocol (MCP)

## Introduktion til Model Context Protocol (MCP)

Model Context Protocol (MCP) er en avanceret ramme designet til at standardisere interaktioner mellem AI-modeller og klientapplikationer. MCP fungerer som en bro mellem AI-modeller og de applikationer, der bruger dem, og tilbyder en ensartet grænseflade uanset den underliggende modelimplementering.

Nøgleaspekter ved MCP:

- **Standardiseret Kommunikation**: MCP etablerer et fælles sprog for applikationer til at kommunikere med AI-modeller
- **Forbedret Kontekststyring**: Muliggør effektiv overførsel af kontekstuel information til AI-modeller
- **Platformuafhængig Kompatibilitet**: Fungerer på tværs af forskellige programmeringssprog, herunder C#, Java, JavaScript, Python og TypeScript
- **Problemfri Integration**: Gør det nemt for udviklere at integrere forskellige AI-modeller i deres applikationer

MCP er særligt værdifuld i udviklingen af AI-agenter, da det giver agenter mulighed for at interagere med forskellige systemer og datakilder via en samlet protokol, hvilket gør agenterne mere fleksible og kraftfulde.

## Læringsmål
- Forstå, hvad MCP er, og dens rolle i udviklingen af AI-agenter
- Opsætte og konfigurere en MCP-server til GitHub-integration
- Bygge et multi-agent system ved hjælp af MCP-værktøjer
- Implementere RAG (Retrieval Augmented Generation) med Azure Cognitive Search

## Forudsætninger
- Python 3.8+
- Node.js 14+
- Azure-abonnement
- GitHub-konto
- Grundlæggende forståelse af Semantic Kernel

## Opsætningsinstruktioner

1. **Opsætning af Miljø**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurer Azure-tjenester**
   - Opret en Azure Cognitive Search-ressource
   - Opsæt Azure OpenAI-tjeneste
   - Konfigurer miljøvariabler i `.env`

3. **Opsætning af MCP-server**
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

## Centrale Komponenter

### 1. Multi-Agent System
- GitHub Agent: Analyse af repositories
- Hackathon Agent: Projektanbefalinger
- Events Agent: Forslag til teknologiske begivenheder

### 2. Azure Integration
- Cognitive Search til indeksering af begivenheder
- Azure OpenAI til agentintelligens
- Implementering af RAG-mønster

### 3. MCP-værktøjer
- Analyse af GitHub repositories
- Inspektion af kode
- Udtrækning af metadata

## Gennemgang af Kode

Eksemplet demonstrerer:
1. Integration af MCP-server
2. Orkestrering af multi-agent system
3. Integration med Azure Cognitive Search
4. Implementering af RAG-mønster

Nøglefunktioner:
- Analyse af GitHub repositories i realtid
- Intelligente projektanbefalinger
- Matchning af begivenheder ved hjælp af Azure Search
- Streaming af svar med Chainlit

## Kørsel af Eksemplet

For detaljerede opsætningsinstruktioner og mere information, se [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Start MCP-serveren:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Start applikationen:
   ```bash
   chainlit run app.py -w
   ```

3. Test integrationen:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Fejlfinding

Almindelige problemer og løsninger:
1. MCP-forbindelsesproblemer
   - Bekræft, at serveren kører
   - Tjek porttilgængelighed
   - Bekræft GitHub-tokens

2. Problemer med Azure Search
   - Valider forbindelsesstrenge
   - Tjek, om indekset eksisterer
   - Bekræft dokumentupload

## Næste Skridt
- Udforsk yderligere MCP-værktøjer
- Implementer brugerdefinerede agenter
- Forbedr RAG-funktionalitet
- Tilføj flere begivenhedskilder
- **Avanceret**: Se [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) for eksempler på agent-til-agent kommunikation

## Ressourcer
- [MCP for Begyndere](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.