<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T21:27:20+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "hu"
}
-->
# MCP Server Integrációs Útmutató

## Előfeltételek
- Telepített Node.js (14-es vagy újabb verzió)
- npm csomagkezelő
- Python környezet a szükséges függőségekkel

## Beállítási lépések

1. **MCP Server csomag telepítése**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **MCP Server indítása**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   A szervernek el kell indulnia, és meg kell jelenítenie egy csatlakozási URL-t.

3. **Kapcsolat ellenőrzése**  
   - Keresd a dugó ikont (🔌) a Chainlit felületén  
   - Egy szám (1) kell, hogy megjelenjen a dugó ikon mellett, jelezve a sikeres kapcsolatot  
   - A konzolnak ezt kell mutatnia: "GitHub plugin setup completed successfully" (további állapotsorokkal együtt)

## Hibakeresés

### Gyakori problémák

1. **Portütközés**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Megoldás: Módosítsd a portot az alábbi paranccsal:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Hitelesítési problémák**  
   - Győződj meg róla, hogy a GitHub hitelesítő adatok megfelelően vannak konfigurálva  
   - Ellenőrizd, hogy a .env fájl tartalmazza a szükséges tokeneket  
   - Ellenőrizd a GitHub API hozzáférést  

3. **Kapcsolat sikertelen**  
   - Ellenőrizd, hogy a szerver a várt porton fut-e  
   - Nézd meg a tűzfal beállításait  
   - Győződj meg róla, hogy a Python környezet tartalmazza a szükséges csomagokat  

## Kapcsolat ellenőrzése

Az MCP szerver megfelelően csatlakozott, ha:  
1. A konzol ezt mutatja: "GitHub plugin setup completed successfully"  
2. A kapcsolatnaplók ezt mutatják: "✓ MCP Connection Status: Active"  
3. A GitHub parancsok működnek a csevegési felületen  

## Környezeti változók

Szükséges a .env fájlban:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Kapcsolat tesztelése

Küldd el ezt a tesztüzenetet a csevegésben:  
```
Show me the repositories for username: [GitHub Username]
```  
Egy sikeres válasz a repozitórium információit fogja megjeleníteni.  

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.