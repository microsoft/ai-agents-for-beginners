<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:30:18+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "sv"
}
-->
# Lektion 11: Integration av Model Context Protocol (MCP)

## Introduktion till Model Context Protocol (MCP)

Model Context Protocol (MCP) är ett banbrytande ramverk som är utformat för att standardisera interaktioner mellan AI-modeller och klientapplikationer. MCP fungerar som en bro mellan AI-modeller och de applikationer som använder dem, och tillhandahåller ett konsekvent gränssnitt oavsett den underliggande modellimplementeringen.

Viktiga aspekter av MCP:

- **Standardiserad kommunikation**: MCP etablerar ett gemensamt språk för applikationer att kommunicera med AI-modeller
- **Förbättrad hantering av kontext**: Möjliggör effektiv överföring av kontextuell information till AI-modeller
- **Plattformsoberoende kompatibilitet**: Fungerar med olika programmeringsspråk, inklusive C#, Java, JavaScript, Python och TypeScript
- **Smidig integration**: Gör det enkelt för utvecklare att integrera olika AI-modeller i sina applikationer

MCP är särskilt värdefullt vid utveckling av AI-agenter eftersom det gör det möjligt för agenter att interagera med olika system och datakällor via ett enhetligt protokoll, vilket gör agenterna mer flexibla och kraftfulla.

## Lärandemål
- Förstå vad MCP är och dess roll i utvecklingen av AI-agenter
- Installera och konfigurera en MCP-server för GitHub-integration
- Bygga ett system med flera agenter med hjälp av MCP-verktyg
- Implementera RAG (Retrieval Augmented Generation) med Azure Cognitive Search

## Förkunskaper
- Python 3.8+
- Node.js 14+
- Azure-abonnemang
- GitHub-konto
- Grundläggande förståelse för Semantic Kernel

## Installationsinstruktioner

1. **Miljöinställning**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurera Azure-tjänster**
   - Skapa en Azure Cognitive Search-resurs
   - Ställ in Azure OpenAI-tjänsten
   - Konfigurera miljövariabler i `.env`

3. **Installera MCP-server**
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

## Kärnkomponenter

### 1. System med flera agenter
- GitHub-agent: Analys av repository
- Hackathon-agent: Projektrekommendationer
- Event-agent: Förslag på teknikevenemang

### 2. Azure-integration
- Cognitive Search för indexering av evenemang
- Azure OpenAI för agentintelligens
- Implementering av RAG-mönster

### 3. MCP-verktyg
- Analys av GitHub-repository
- Kodinspektion
- Metadataextraktion

## Genomgång av kod

Exemplet demonstrerar:
1. Integration av MCP-server
2. Orkestrering av flera agenter
3. Integration med Azure Cognitive Search
4. Implementering av RAG-mönster

Nyckelfunktioner:
- Realtidsanalys av GitHub-repository
- Intelligenta projektrekommendationer
- Matchning av evenemang med Azure Search
- Strömmande svar med Chainlit

## Köra exemplet

För detaljerade installationsinstruktioner och mer information, se [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Starta MCP-servern:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Starta applikationen:
   ```bash
   chainlit run app.py -w
   ```

3. Testa integrationen:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Felsökning

Vanliga problem och lösningar:
1. Problem med MCP-anslutning
   - Kontrollera att servern körs
   - Kontrollera porttillgänglighet
   - Bekräfta GitHub-tokens

2. Problem med Azure Search
   - Validera anslutningssträngar
   - Kontrollera att indexet finns
   - Bekräfta uppladdning av dokument

## Nästa steg
- Utforska ytterligare MCP-verktyg
- Implementera anpassade agenter
- Förbättra RAG-funktioner
- Lägg till fler källor för evenemang
- **Avancerat**: Kolla in [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) för exempel på kommunikation mellan agenter

## Resurser
- [MCP för nybörjare](https://aka.ms/mcp-for-beginners)  
- [MCP-dokumentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search-dokumentation](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel-guider](https://learn.microsoft.com/semantic-kernel/)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.