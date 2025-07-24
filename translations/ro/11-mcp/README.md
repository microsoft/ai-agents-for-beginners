<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T09:04:13+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ro"
}
-->
# Lecția 11: Integrarea Protocolului de Context al Modelului (MCP)

## Introducere în Protocolul de Context al Modelului (MCP)

Protocolul de Context al Modelului (MCP) este un cadru de ultimă generație conceput pentru a standardiza interacțiunile dintre modelele AI și aplicațiile client. MCP servește ca o punte între modelele AI și aplicațiile care le utilizează, oferind o interfață consistentă, indiferent de implementarea modelului de bază.

Aspecte cheie ale MCP:

- **Comunicare Standardizată**: MCP stabilește un limbaj comun pentru aplicații în vederea comunicării cu modelele AI
- **Gestionarea Contextului Îmbunătățită**: Permite transmiterea eficientă a informațiilor contextuale către modelele AI
- **Compatibilitate Cross-platform**: Funcționează pe diverse limbaje de programare, inclusiv C#, Java, JavaScript, Python și TypeScript
- **Integrare Simplă**: Permite dezvoltatorilor să integreze cu ușurință diferite modele AI în aplicațiile lor

MCP este deosebit de valoros în dezvoltarea agenților AI, deoarece le permite să interacționeze cu diverse sisteme și surse de date printr-un protocol unificat, făcând agenții mai flexibili și mai puternici.

## Obiective de Învățare
- Înțelegerea MCP și rolul său în dezvoltarea agenților AI
- Configurarea și configurarea unui server MCP pentru integrarea cu GitHub
- Construirea unui sistem multi-agent folosind instrumentele MCP
- Implementarea RAG (Generare Augmentată prin Recuperare) cu Azure Cognitive Search

## Cerințe Prealabile
- Python 3.8+
- Node.js 14+
- Abonament Azure
- Cont GitHub
- Înțelegere de bază a Semantic Kernel

## Instrucțiuni de Configurare

1. **Configurarea Mediului**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configurarea Serviciilor Azure**
   - Creați o resursă Azure Cognitive Search
   - Configurați serviciul Azure OpenAI
   - Configurați variabilele de mediu în `.env`

3. **Configurarea Serverului MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Structura Proiectului

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

## Componente Principale

### 1. Sistem Multi-Agent
- Agent GitHub: Analiza depozitelor
- Agent Hackathon: Recomandări de proiecte
- Agent Evenimente: Sugestii pentru evenimente tehnologice

### 2. Integrarea Azure
- Cognitive Search pentru indexarea evenimentelor
- Azure OpenAI pentru inteligența agenților
- Implementarea modelului RAG

### 3. Instrumente MCP
- Analiza depozitelor GitHub
- Inspecția codului
- Extracția de metadate

## Prezentare Generală a Codului

Exemplul demonstrează:
1. Integrarea serverului MCP
2. Orchestrarea multi-agent
3. Integrarea Azure Cognitive Search
4. Implementarea modelului RAG

Funcționalități cheie:
- Analiza depozitelor GitHub în timp real
- Recomandări inteligente de proiecte
- Potrivirea evenimentelor folosind Azure Search
- Răspunsuri în flux cu Chainlit

## Rularea Exemplului

Pentru instrucțiuni detaliate de configurare și mai multe informații, consultați [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Porniți serverul MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Lansați aplicația:
   ```bash
   chainlit run app.py -w
   ```

3. Testați integrarea:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Depanare

Probleme comune și soluții:
1. Probleme de Conexiune MCP
   - Verificați dacă serverul este pornit
   - Verificați disponibilitatea portului
   - Confirmați tokenurile GitHub

2. Probleme Azure Search
   - Validați șirurile de conexiune
   - Verificați existența indexului
   - Confirmați încărcarea documentelor

## Pași Următori
- Explorați instrumente suplimentare MCP
- Implementați agenți personalizați
- Îmbunătățiți capacitățile RAG
- Adăugați mai multe surse de evenimente
- **Avansat**: Consultați [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) pentru exemple de comunicare între agenți

## Resurse
- [MCP pentru Începători](https://aka.ms/mcp-for-beginners)  
- [Documentația MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Documentația Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Ghiduri Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.