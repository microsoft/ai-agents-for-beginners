<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:34:34+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "no"
}
-->
# Leksjon 11: Integrering av Model Context Protocol (MCP)

## Introduksjon til Model Context Protocol (MCP)

Model Context Protocol (MCP) er et banebrytende rammeverk designet for å standardisere interaksjoner mellom AI-modeller og klientapplikasjoner. MCP fungerer som en bro mellom AI-modeller og applikasjonene som bruker dem, og gir et konsistent grensesnitt uavhengig av den underliggende modellimplementasjonen.

Hovedaspekter ved MCP:

- **Standardisert kommunikasjon**: MCP etablerer et felles språk for applikasjoner som kommuniserer med AI-modeller
- **Forbedret konteksthåndtering**: Muliggjør effektiv overføring av kontekstuell informasjon til AI-modeller
- **Plattformuavhengig kompatibilitet**: Fungerer på tvers av ulike programmeringsspråk, inkludert C#, Java, JavaScript, Python og TypeScript
- **Sømløs integrering**: Gjør det enkelt for utviklere å integrere ulike AI-modeller i applikasjonene sine

MCP er spesielt verdifull i utviklingen av AI-agenter, da det lar agenter samhandle med ulike systemer og datakilder gjennom en enhetlig protokoll, noe som gjør agentene mer fleksible og kraftige.

## Læringsmål
- Forstå hva MCP er og dens rolle i utviklingen av AI-agenter
- Sette opp og konfigurere en MCP-server for integrasjon med GitHub
- Bygge et multi-agent-system ved hjelp av MCP-verktøy
- Implementere RAG (Retrieval Augmented Generation) med Azure Cognitive Search

## Forutsetninger
- Python 3.8+
- Node.js 14+
- Azure-abonnement
- GitHub-konto
- Grunnleggende forståelse av Semantic Kernel

## Oppsettsinstruksjoner

1. **Miljøoppsett**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurer Azure-tjenester**
   - Opprett en Azure Cognitive Search-ressurs
   - Sett opp Azure OpenAI-tjenesten
   - Konfigurer miljøvariabler i `.env`

3. **MCP-serveroppsett**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Prosjektstruktur

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

## Kjernekomponenter

### 1. Multi-agent-system
- GitHub-agent: Analyse av repositorier
- Hackathon-agent: Prosjektanbefalinger
- Event-agent: Forslag til teknologiske arrangementer

### 2. Azure-integrasjon
- Cognitive Search for indeksering av arrangementer
- Azure OpenAI for agentintelligens
- Implementering av RAG-mønster

### 3. MCP-verktøy
- Analyse av GitHub-repositorier
- Kodeinspeksjon
- Metadatauttrekk

## Gjennomgang av kode

Eksemplet demonstrerer:
1. Integrering av MCP-server
2. Orkestrering av multi-agenter
3. Integrasjon med Azure Cognitive Search
4. Implementering av RAG-mønster

Nøkkelfunksjoner:
- Sanntidsanalyse av GitHub-repositorier
- Intelligente prosjektanbefalinger
- Matching av arrangementer ved hjelp av Azure Search
- Strømming av svar med Chainlit

## Kjøre eksemplet

For detaljerte oppsettsinstruksjoner og mer informasjon, se [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Start MCP-serveren:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Start applikasjonen:
   ```bash
   chainlit run app.py -w
   ```

3. Test integrasjonen:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Feilsøking

Vanlige problemer og løsninger:
1. MCP-tilkoblingsproblemer
   - Bekreft at serveren kjører
   - Sjekk porttilgjengelighet
   - Bekreft GitHub-tokens

2. Problemer med Azure Search
   - Valider tilkoblingsstrenger
   - Sjekk om indeksen eksisterer
   - Bekreft opplasting av dokumenter

## Neste steg
- Utforsk flere MCP-verktøy
- Implementer tilpassede agenter
- Forbedre RAG-funksjonalitet
- Legg til flere datakilder for arrangementer
- **Avansert**: Sjekk ut [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) for eksempler på kommunikasjon mellom agenter

## Ressurser
- [MCP for nybegynnere](https://aka.ms/mcp-for-beginners)  
- [MCP-dokumentasjon](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search-dokumentasjon](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel-guider](https://learn.microsoft.com/semantic-kernel/)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.