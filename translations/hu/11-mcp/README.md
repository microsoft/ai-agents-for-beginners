<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:38:59+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "hu"
}
-->
# 11. Lecke: Model Context Protocol (MCP) Integráció

## Bevezetés a Model Context Protocol (MCP) keretrendszerbe

A Model Context Protocol (MCP) egy korszerű keretrendszer, amely az AI modellek és kliensalkalmazások közötti interakciók szabványosítására lett kifejlesztve. Az MCP hidat képez az AI modellek és az azokat használó alkalmazások között, egységes interfészt biztosítva a modell implementációjától függetlenül.

Az MCP főbb jellemzői:

- **Szabványosított kommunikáció**: Az MCP egy közös nyelvet hoz létre az alkalmazások és az AI modellek közötti kommunikációhoz
- **Fejlett kontextuskezelés**: Hatékonyan teszi lehetővé a kontextuális információk továbbítását az AI modellek számára
- **Platformfüggetlen kompatibilitás**: Számos programozási nyelven működik, beleértve a C#, Java, JavaScript, Python és TypeScript nyelveket
- **Zökkenőmentes integráció**: Lehetővé teszi a fejlesztők számára, hogy könnyedén integrálják az AI modelleket az alkalmazásaikba

Az MCP különösen hasznos az AI ügynökök fejlesztésében, mivel lehetővé teszi, hogy az ügynökök különböző rendszerekkel és adatforrásokkal egységes protokollon keresztül kommunikáljanak, így rugalmasabbá és erőteljesebbé válnak.

## Tanulási célok
- Megérteni, mi az MCP, és milyen szerepet játszik az AI ügynökök fejlesztésében
- MCP szerver beállítása és konfigurálása GitHub integrációhoz
- Több ügynökből álló rendszer építése MCP eszközökkel
- RAG (Retrieval Augmented Generation) megvalósítása Azure Cognitive Search segítségével

## Előfeltételek
- Python 3.8+
- Node.js 14+
- Azure előfizetés
- GitHub fiók
- Alapvető ismeretek a Semantic Kernelről

## Telepítési útmutató

1. **Környezet beállítása**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure szolgáltatások konfigurálása**
   - Hozz létre egy Azure Cognitive Search erőforrást
   - Állítsd be az Azure OpenAI szolgáltatást
   - Konfiguráld a környezeti változókat a `.env` fájlban

3. **MCP szerver beállítása**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Projektstruktúra

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

## Főbb komponensek

### 1. Több ügynökből álló rendszer
- GitHub ügynök: Repozitórium elemzése
- Hackathon ügynök: Projektajánlások
- Események ügynök: Technológiai események ajánlása

### 2. Azure integráció
- Cognitive Search eseményindexeléshez
- Azure OpenAI az ügynökök intelligenciájához
- RAG minta megvalósítása

### 3. MCP eszközök
- GitHub repozitórium elemzése
- Kódelemzés
- Metaadatok kinyerése

## Kódbemutató

A példa bemutatja:
1. MCP szerver integrációját
2. Több ügynök összehangolását
3. Azure Cognitive Search integrációját
4. RAG minta megvalósítását

Főbb funkciók:
- Valós idejű GitHub repozitórium elemzés
- Intelligens projektajánlások
- Események párosítása Azure Search segítségével
- Streaming válaszok Chainlit használatával

## A minta futtatása

Részletes telepítési útmutatóért és további információkért lásd a [Github MCP Server Example README](./code_samples/github-mcp/README.md) fájlt.

1. Indítsd el az MCP szervert:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Indítsd el az alkalmazást:  
   ```bash
   chainlit run app.py -w
   ```

3. Teszteld az integrációt:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Hibakeresés

Gyakori problémák és megoldások:
1. MCP kapcsolódási problémák
   - Ellenőrizd, hogy a szerver fut-e
   - Ellenőrizd a port elérhetőségét
   - Győződj meg a GitHub tokenek helyességéről

2. Azure Search problémák
   - Ellenőrizd a kapcsolat stringeket
   - Győződj meg az index létezéséről
   - Ellenőrizd a dokumentumfeltöltést

## Következő lépések
- Fedezd fel az MCP további eszközeit
- Valósíts meg egyedi ügynököket
- Fejleszd tovább a RAG képességeket
- Adj hozzá több eseményforrást
- **Haladó**: Nézd meg a [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) példákat ügynök-ügynök kommunikációra

## Források
- [MCP kezdőknek](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentáció](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search dokumentáció](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel útmutatók](https://learn.microsoft.com/semantic-kernel/)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.