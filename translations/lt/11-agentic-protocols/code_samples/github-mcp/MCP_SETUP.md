<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-30T15:00:29+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "lt"
}
-->
# MCP Server Integracijos Gidas

## Reikalavimai
- Įdiegta Node.js (14 ar naujesnė versija)
- npm paketų tvarkyklė
- Python aplinka su reikalingomis priklausomybėmis

## Nustatymo Žingsniai

1. **Įdiekite MCP Server Paketą**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Paleiskite MCP Serverį**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Serveris turėtų paleisti ir parodyti prisijungimo URL.

3. **Patikrinkite Prisijungimą**  
   - Ieškokite kištuko piktogramos (🔌) savo Chainlit sąsajoje  
   - Šalia kištuko piktogramos turėtų pasirodyti skaičius (1), nurodantis sėkmingą prisijungimą  
   - Konsolėje turėtų būti rodoma: „GitHub plugin setup completed successfully“ (kartu su papildomomis būsenos eilutėmis)

## Trikčių Šalinimas

### Dažnos Problemų Priežastys

1. **Porto Konfliktas**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Sprendimas: Pakeiskite portą naudodami:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Autentifikacijos Problemų**  
   - Įsitikinkite, kad GitHub prisijungimo duomenys yra tinkamai sukonfigūruoti  
   - Patikrinkite, ar .env faile yra reikalingi tokenai  
   - Patikrinkite GitHub API prieigą

3. **Nepavyko Prisijungti**  
   - Patikrinkite, ar serveris veikia numatytame porte  
   - Patikrinkite ugniasienės nustatymus  
   - Įsitikinkite, kad Python aplinka turi reikalingus paketus

## Prisijungimo Patikrinimas

Jūsų MCP serveris tinkamai prijungtas, kai:  
1. Konsolėje rodoma „GitHub plugin setup completed successfully“  
2. Prisijungimo žurnaluose rodoma „✓ MCP Connection Status: Active“  
3. GitHub komandos veikia pokalbių sąsajoje

## Aplinkos Kintamieji

Reikalingi jūsų .env faile:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Prisijungimo Testavimas

Išsiųskite šį testinį pranešimą pokalbyje:  
```
Show me the repositories for username: [GitHub Username]
```  
Sėkmingas atsakymas parodys saugyklos informaciją.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.