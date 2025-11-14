<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T21:27:32+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "cs"
}
-->
# Příručka pro integraci MCP serveru

## Předpoklady
- Nainstalovaný Node.js (verze 14 nebo vyšší)
- Správce balíčků npm
- Python prostředí s požadovanými závislostmi

## Kroky nastavení

1. **Nainstalujte balíček MCP serveru**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Spusťte MCP server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Server by se měl spustit a zobrazit URL pro připojení.

3. **Ověřte připojení**
   - V rozhraní Chainlit vyhledejte ikonu zástrčky (🔌)
   - Vedle ikony zástrčky by se mělo objevit číslo (1), což značí úspěšné připojení
   - Konzole by měla zobrazit: "GitHub plugin setup completed successfully" (spolu s dalšími stavovými řádky)

## Řešení problémů

### Běžné problémy

1. **Konflikt portů**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Řešení: Změňte port pomocí:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problémy s autentizací**
   - Ujistěte se, že GitHub přihlašovací údaje jsou správně nakonfigurovány
   - Zkontrolujte, zda soubor .env obsahuje požadované tokeny
   - Ověřte přístup k GitHub API

3. **Selhání připojení**
   - Ověřte, že server běží na očekávaném portu
   - Zkontrolujte nastavení firewallu
   - Ověřte, že Python prostředí obsahuje požadované balíčky

## Ověření připojení

Váš MCP server je správně připojen, pokud:
1. Konzole zobrazí "GitHub plugin setup completed successfully"
2. Logy připojení zobrazí "✓ MCP Connection Status: Active"
3. GitHub příkazy fungují v chatovacím rozhraní

## Proměnné prostředí

Požadované v souboru .env:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testování připojení

Pošlete tuto testovací zprávu v chatu:  
```
Show me the repositories for username: [GitHub Username]
```  
Úspěšná odpověď zobrazí informace o repozitáři.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.