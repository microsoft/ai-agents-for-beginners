<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-30T00:24:15+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "hr"
}
-->
# Vodič za integraciju MCP servera

## Preduvjeti
- Instaliran Node.js (verzija 14 ili novija)
- npm upravitelj paketa
- Python okruženje s potrebnim ovisnostima

## Koraci za postavljanje

1. **Instalirajte MCP Server paket**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Pokrenite MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Server bi trebao započeti i prikazati URL za povezivanje.

3. **Provjerite vezu**
   - Potražite ikonu utikača (🔌) u Chainlit sučelju
   - Broj (1) trebao bi se pojaviti pored ikone utikača, što označava uspješnu vezu
   - Konzola bi trebala prikazati: "GitHub plugin setup completed successfully" (zajedno s dodatnim statusnim linijama)

## Rješavanje problema

### Uobičajeni problemi

1. **Sukob porta**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Rješenje: Promijenite port koristeći:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problemi s autentifikacijom**
   - Provjerite jesu li GitHub vjerodajnice ispravno konfigurirane
   - Provjerite da .env datoteka sadrži potrebne tokene
   - Potvrdite pristup GitHub API-ju

3. **Veza nije uspjela**
   - Potvrdite da server radi na očekivanom portu
   - Provjerite postavke vatrozida
   - Provjerite da Python okruženje ima potrebne pakete

## Provjera veze

Vaš MCP server je ispravno povezan kada:
1. Konzola prikazuje "GitHub plugin setup completed successfully"
2. Dnevnici veze prikazuju "✓ MCP Connection Status: Active"
3. GitHub naredbe rade u chat sučelju

## Varijable okruženja

Potrebno u vašoj .env datoteci:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testiranje veze

Pošaljite ovu testnu poruku u chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Uspješan odgovor prikazat će informacije o repozitoriju.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.