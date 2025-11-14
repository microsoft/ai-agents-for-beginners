<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T21:27:42+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "sk"
}
-->
# Návod na integráciu MCP servera

## Predpoklady
- Nainštalovaný Node.js (verzia 14 alebo vyššia)
- Správca balíkov npm
- Prostredie Python s potrebnými závislosťami

## Kroky nastavenia

1. **Nainštalujte balík MCP servera**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Spustite MCP server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Server by sa mal spustiť a zobraziť URL adresu pripojenia.

3. **Overte pripojenie**
   - V rozhraní Chainlit vyhľadajte ikonu zástrčky (🔌)
   - Vedľa ikony zástrčky by sa malo zobraziť číslo (1), čo znamená úspešné pripojenie
   - Konzola by mala zobraziť: "GitHub plugin setup completed successfully" (spolu s ďalšími stavovými riadkami)

## Riešenie problémov

### Bežné problémy

1. **Konflikt portov**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Riešenie: Zmeňte port pomocou:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problémy s autentifikáciou**
   - Uistite sa, že GitHub prihlasovacie údaje sú správne nakonfigurované
   - Skontrolujte, či sú v súbore .env uvedené potrebné tokeny
   - Overte prístup k GitHub API

3. **Zlyhanie pripojenia**
   - Skontrolujte, či server beží na očakávanom porte
   - Skontrolujte nastavenia firewallu
   - Overte, či prostredie Python obsahuje potrebné balíky

## Overenie pripojenia

Váš MCP server je správne pripojený, keď:
1. Konzola zobrazuje "GitHub plugin setup completed successfully"
2. Logy pripojenia zobrazujú "✓ MCP Connection Status: Active"
3. GitHub príkazy fungujú v chatovom rozhraní

## Premenné prostredia

Vyžadované v súbore .env:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testovanie pripojenia

Pošlite túto testovaciu správu v chate:
```
Show me the repositories for username: [GitHub Username]
```  
Úspešná odpoveď zobrazí informácie o repozitári.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.