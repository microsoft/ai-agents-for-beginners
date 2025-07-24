<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:38:47+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "nl"
}
-->
# Les 11: Integratie van Model Context Protocol (MCP)

## Introductie tot Model Context Protocol (MCP)

Het Model Context Protocol (MCP) is een geavanceerd framework dat is ontworpen om interacties tussen AI-modellen en clientapplicaties te standaardiseren. MCP fungeert als een brug tussen AI-modellen en de applicaties die deze gebruiken, en biedt een consistente interface, ongeacht de onderliggende modelimplementatie.

Belangrijke aspecten van MCP:

- **Gestandaardiseerde Communicatie**: MCP stelt een gemeenschappelijke taal vast voor applicaties om met AI-modellen te communiceren
- **Verbeterd Contextbeheer**: Maakt efficiënte overdracht van contextuele informatie naar AI-modellen mogelijk
- **Platformonafhankelijke Compatibiliteit**: Werkt met verschillende programmeertalen, waaronder C#, Java, JavaScript, Python en TypeScript
- **Naadloze Integratie**: Stelt ontwikkelaars in staat om eenvoudig verschillende AI-modellen in hun applicaties te integreren

MCP is vooral waardevol bij de ontwikkeling van AI-agenten, omdat het agenten in staat stelt om via een uniform protocol met verschillende systemen en gegevensbronnen te communiceren, waardoor ze flexibeler en krachtiger worden.

## Leerdoelen
- Begrijpen wat MCP is en de rol ervan in de ontwikkeling van AI-agenten
- Een MCP-server opzetten en configureren voor GitHub-integratie
- Een multi-agent systeem bouwen met MCP-tools
- RAG (Retrieval Augmented Generation) implementeren met Azure Cognitive Search

## Vereisten
- Python 3.8+
- Node.js 14+
- Azure-abonnement
- GitHub-account
- Basiskennis van Semantic Kernel

## Installatie-instructies

1. **Omgevingsinstellingen**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure-diensten configureren**
   - Maak een Azure Cognitive Search-resource aan
   - Stel de Azure OpenAI-service in
   - Configureer omgevingsvariabelen in `.env`

3. **MCP-server instellen**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Projectstructuur

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

## Kerncomponenten

### 1. Multi-Agent Systeem
- GitHub Agent: Analyse van repositories
- Hackathon Agent: Aanbevelingen voor projecten
- Events Agent: Suggesties voor technische evenementen

### 2. Azure-integratie
- Cognitive Search voor het indexeren van evenementen
- Azure OpenAI voor de intelligentie van agenten
- Implementatie van het RAG-patroon

### 3. MCP-tools
- Analyse van GitHub-repositories
- Code-inspectie
- Metadata-extractie

## Code-uitleg

De voorbeeldcode demonstreert:
1. Integratie van de MCP-server
2. Orkestratie van meerdere agenten
3. Integratie met Azure Cognitive Search
4. Implementatie van het RAG-patroon

Belangrijke functies:
- Realtime analyse van GitHub-repositories
- Intelligente projectaanbevelingen
- Evenementenmatching met Azure Search
- Streamingreacties met Chainlit

## Het Voorbeeld Uitvoeren

Voor gedetailleerde installatie-instructies en meer informatie, raadpleeg de [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Start de MCP-server:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Start de applicatie:
   ```bash
   chainlit run app.py -w
   ```

3. Test de integratie:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Problemen Oplossen

Veelvoorkomende problemen en oplossingen:
1. MCP-verbindingproblemen
   - Controleer of de server actief is
   - Controleer de beschikbaarheid van de poort
   - Bevestig GitHub-tokens

2. Problemen met Azure Search
   - Controleer verbindingsstrings
   - Controleer of de index bestaat
   - Verifieer het uploaden van documenten

## Volgende Stappen
- Verken aanvullende MCP-tools
- Implementeer aangepaste agenten
- Verbeter RAG-mogelijkheden
- Voeg meer gegevensbronnen voor evenementen toe
- **Geavanceerd**: Bekijk [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) voor voorbeelden van communicatie tussen agenten

## Bronnen
- [MCP voor Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentatie](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Gidsen](https://learn.microsoft.com/semantic-kernel/)

**Disclaimer (Vrijwaring)**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.