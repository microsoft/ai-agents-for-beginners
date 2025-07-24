<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T09:01:56+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "sk"
}
-->
# Lekcia 11: Integrácia Model Context Protocol (MCP)

## Úvod do Model Context Protocol (MCP)

Model Context Protocol (MCP) je moderný rámec navrhnutý na štandardizáciu interakcií medzi AI modelmi a klientskými aplikáciami. MCP slúži ako most medzi AI modelmi a aplikáciami, ktoré ich využívajú, poskytujúc konzistentné rozhranie bez ohľadu na implementáciu modelu.

Kľúčové aspekty MCP:

- **Štandardizovaná komunikácia**: MCP vytvára spoločný jazyk pre aplikácie na komunikáciu s AI modelmi
- **Vylepšené spravovanie kontextu**: Umožňuje efektívne odovzdávanie kontextových informácií AI modelom
- **Kompatibilita naprieč platformami**: Funguje v rôznych programovacích jazykoch vrátane C#, Java, JavaScript, Python a TypeScript
- **Jednoduchá integrácia**: Umožňuje vývojárom ľahko integrovať rôzne AI modely do svojich aplikácií

MCP je obzvlášť cenný pri vývoji AI agentov, pretože umožňuje agentom interagovať s rôznymi systémami a zdrojmi dát prostredníctvom jednotného protokolu, čím sa stávajú flexibilnejšími a výkonnejšími.

## Ciele učenia
- Pochopiť, čo je MCP a jeho úlohu vo vývoji AI agentov
- Nastaviť a nakonfigurovať MCP server pre integráciu s GitHubom
- Vytvoriť systém s viacerými agentmi pomocou nástrojov MCP
- Implementovať RAG (Retrieval Augmented Generation) s Azure Cognitive Search

## Predpoklady
- Python 3.8+
- Node.js 14+
- Azure predplatné
- GitHub účet
- Základné porozumenie Semantic Kernel

## Pokyny na nastavenie

1. **Nastavenie prostredia**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurácia služieb Azure**
   - Vytvorte zdroj Azure Cognitive Search
   - Nastavte službu Azure OpenAI
   - Nakonfigurujte environmentálne premenné v súbore `.env`

3. **Nastavenie MCP servera**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Štruktúra projektu

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

## Hlavné komponenty

### 1. Systém s viacerými agentmi
- GitHub Agent: Analýza repozitárov
- Hackathon Agent: Odporúčania projektov
- Events Agent: Návrhy technologických podujatí

### 2. Integrácia s Azure
- Cognitive Search na indexovanie podujatí
- Azure OpenAI na inteligenciu agentov
- Implementácia vzoru RAG

### 3. Nástroje MCP
- Analýza GitHub repozitárov
- Inšpekcia kódu
- Extrakcia metadát

## Prehľad kódu

Ukážka demonštruje:
1. Integráciu MCP servera
2. Orchestráciu viacerých agentov
3. Integráciu Azure Cognitive Search
4. Implementáciu vzoru RAG

Kľúčové funkcie:
- Analýza GitHub repozitárov v reálnom čase
- Inteligentné odporúčania projektov
- Zhodovanie podujatí pomocou Azure Search
- Streamovanie odpovedí s Chainlit

## Spustenie ukážky

Pre podrobné pokyny na nastavenie a viac informácií si pozrite [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Spustite MCP server:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Spustite aplikáciu:
   ```bash
   chainlit run app.py -w
   ```

3. Otestujte integráciu:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Riešenie problémov

Bežné problémy a riešenia:
1. Problémy s pripojením MCP
   - Overte, či server beží
   - Skontrolujte dostupnosť portu
   - Potvrďte GitHub tokeny

2. Problémy s Azure Search
   - Overte reťazce pripojenia
   - Skontrolujte existenciu indexu
   - Overte nahrávanie dokumentov

## Ďalšie kroky
- Preskúmajte ďalšie nástroje MCP
- Implementujte vlastných agentov
- Vylepšite schopnosti RAG
- Pridajte viac zdrojov podujatí
- **Pokročilé**: Pozrite si [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) pre príklady komunikácie medzi agentmi

## Zdroje
- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentácia](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumentácia Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Príručky Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.