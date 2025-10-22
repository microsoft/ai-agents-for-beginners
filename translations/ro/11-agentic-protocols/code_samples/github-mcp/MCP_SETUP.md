<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T21:27:51+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "ro"
}
-->
# Ghid de Integrare MCP Server

## Cerințe preliminare
- Node.js instalat (versiunea 14 sau mai recentă)
- Manager de pachete npm
- Mediu Python cu dependențele necesare

## Pași de configurare

1. **Instalează pachetul MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Pornește MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Serverul ar trebui să pornească și să afișeze un URL de conexiune.

3. **Verifică conexiunea**
   - Caută pictograma de priză (🔌) în interfața Chainlit
   - Ar trebui să apară un număr (1) lângă pictograma de priză, indicând o conexiune reușită
   - Consola ar trebui să afișeze: "Configurarea pluginului GitHub a fost finalizată cu succes" (împreună cu alte linii de stare suplimentare)

## Depanare

### Probleme frecvente

1. **Conflict de port**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Soluție: Schimbă portul folosind:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Probleme de autentificare**
   - Asigură-te că acreditările GitHub sunt configurate corect
   - Verifică dacă fișierul .env conține tokenurile necesare
   - Confirmă accesul la API-ul GitHub

3. **Conexiune eșuată**
   - Confirmă că serverul rulează pe portul așteptat
   - Verifică setările firewall-ului
   - Asigură-te că mediul Python are pachetele necesare

## Verificarea conexiunii

Serverul MCP este conectat corect atunci când:
1. Consola afișează "Configurarea pluginului GitHub a fost finalizată cu succes"
2. Jurnalele de conexiune afișează "✓ MCP Connection Status: Active"
3. Comenzile GitHub funcționează în interfața de chat

## Variabile de mediu

Necesar în fișierul .env:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testarea conexiunii

Trimite acest mesaj de test în chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Un răspuns reușit va afișa informații despre repository.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.