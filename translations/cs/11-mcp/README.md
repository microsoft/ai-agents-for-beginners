<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:40:10+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "cs"
}
-->
# Lekce 11: Integrace Model Context Protocol (MCP)

## Úvod do Model Context Protocol (MCP)

Model Context Protocol (MCP) je moderní rámec navržený pro standardizaci interakcí mezi AI modely a klientskými aplikacemi. MCP slouží jako most mezi AI modely a aplikacemi, které je využívají, a poskytuje konzistentní rozhraní bez ohledu na implementaci modelu.

Klíčové aspekty MCP:

- **Standardizovaná komunikace**: MCP zavádí společný jazyk pro komunikaci aplikací s AI modely
- **Vylepšená správa kontextu**: Umožňuje efektivní předávání kontextových informací AI modelům
- **Kompatibilita napříč platformami**: Funguje v různých programovacích jazycích, včetně C#, Java, JavaScript, Python a TypeScript
- **Snadná integrace**: Umožňuje vývojářům jednoduše integrovat různé AI modely do svých aplikací

MCP je obzvláště užitečný při vývoji AI agentů, protože umožňuje agentům komunikovat s různými systémy a zdroji dat prostřednictvím jednotného protokolu, což činí agenty flexibilnějšími a výkonnějšími.

## Cíle výuky
- Pochopit, co je MCP a jakou roli hraje při vývoji AI agentů
- Nastavit a nakonfigurovat MCP server pro integraci s GitHubem
- Vytvořit systém s více agenty pomocí nástrojů MCP
- Implementovat RAG (Retrieval Augmented Generation) s Azure Cognitive Search

## Požadavky
- Python 3.8+
- Node.js 14+
- Předplatné Azure
- Účet na GitHubu
- Základní znalost Semantic Kernel

## Pokyny k nastavení

1. **Nastavení prostředí**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurace služeb Azure**
   - Vytvořte prostředek Azure Cognitive Search
   - Nastavte službu Azure OpenAI
   - Nakonfigurujte proměnné prostředí v souboru `.env`

3. **Nastavení MCP serveru**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struktura projektu

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

## Hlavní komponenty

### 1. Systém s více agenty
- GitHub Agent: Analýza repozitářů
- Hackathon Agent: Doporučení projektů
- Events Agent: Návrhy technologických událostí

### 2. Integrace s Azure
- Cognitive Search pro indexování událostí
- Azure OpenAI pro inteligenci agentů
- Implementace vzoru RAG

### 3. Nástroje MCP
- Analýza GitHub repozitářů
- Kontrola kódu
- Extrakce metadat

## Prohlídka kódu

Ukázka demonstruje:
1. Integraci MCP serveru
2. Orchestrace více agentů
3. Integraci Azure Cognitive Search
4. Implementaci vzoru RAG

Klíčové funkce:
- Analýza GitHub repozitářů v reálném čase
- Inteligentní doporučení projektů
- Přiřazování událostí pomocí Azure Search
- Streamování odpovědí s Chainlit

## Spuštění ukázky

Podrobné pokyny k nastavení a další informace naleznete v [README příkladu MCP serveru na GitHubu](./code_samples/github-mcp/README.md).

1. Spusťte MCP server:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Spusťte aplikaci:  
   ```bash
   chainlit run app.py -w
   ```

3. Otestujte integraci:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Řešení problémů

Běžné problémy a jejich řešení:
1. Problémy s připojením k MCP
   - Ověřte, že server běží
   - Zkontrolujte dostupnost portu
   - Ověřte GitHub tokeny

2. Problémy s Azure Search
   - Ověřte připojovací řetězce
   - Zkontrolujte existenci indexu
   - Ověřte nahrání dokumentů

## Další kroky
- Prozkoumejte další nástroje MCP
- Implementujte vlastní agenty
- Vylepšete schopnosti RAG
- Přidejte více zdrojů událostí
- **Pokročilé**: Podívejte se na [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) pro příklady komunikace mezi agenty

## Zdroje
- [MCP pro začátečníky](https://aka.ms/mcp-for-beginners)  
- [Dokumentace MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumentace Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Průvodce Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.