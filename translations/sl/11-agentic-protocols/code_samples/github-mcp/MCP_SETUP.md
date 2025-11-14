<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-30T00:24:24+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "sl"
}
-->
# Vodnik za integracijo MCP strežnika

## Predpogoji
- Nameščen Node.js (različica 14 ali novejša)
- Upravitelj paketov npm
- Python okolje z zahtevanimi odvisnostmi

## Koraki za nastavitev

1. **Namestite MCP strežniški paket**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Zaženite MCP strežnik**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Strežnik bi se moral zagnati in prikazati povezovalni URL.

3. **Preverite povezavo**
   - Poiščite ikono vtiča (🔌) v vašem Chainlit vmesniku
   - Številka (1) bi se morala pojaviti poleg ikone vtiča, kar označuje uspešno povezavo
   - Konzola bi morala prikazati: "GitHub plugin setup completed successfully" (skupaj z dodatnimi vrsticami stanja)

## Odpravljanje težav

### Pogoste težave

1. **Konflikt vrat**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Rešitev: Spremenite vrata z uporabo:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Težave z avtentikacijo**
   - Prepričajte se, da so GitHub poverilnice pravilno nastavljene
   - Preverite, da datoteka .env vsebuje zahtevane žetone
   - Preverite dostop do GitHub API-ja

3. **Povezava ni uspela**
   - Preverite, ali strežnik deluje na pričakovanih vratih
   - Preverite nastavitve požarnega zidu
   - Preverite, ali Python okolje vsebuje zahtevane pakete

## Preverjanje povezave

Vaš MCP strežnik je pravilno povezan, ko:
1. Konzola prikazuje "GitHub plugin setup completed successfully"
2. Dnevniki povezave prikazujejo "✓ MCP Connection Status: Active"
3. GitHub ukazi delujejo v klepetalnem vmesniku

## Okoljske spremenljivke

Zahtevane v vaši datoteki .env:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testiranje povezave

Pošljite to testno sporočilo v klepet:
```
Show me the repositories for username: [GitHub Username]
```
Uspešen odgovor bo prikazal informacije o repozitoriju.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.