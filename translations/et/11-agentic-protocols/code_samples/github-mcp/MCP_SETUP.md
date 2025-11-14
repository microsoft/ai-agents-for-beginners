<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-10-11T11:27:14+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "et"
}
-->
# MCP Serveri integreerimise juhend

## Eeltingimused
- Paigaldatud Node.js (versioon 14 või uuem)
- npm paketihaldur
- Python keskkond vajalike sõltuvustega

## Seadistamise sammud

1. **Paigalda MCP Serveri pakett**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Käivita MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Server peaks käivituma ja kuvama ühenduse URL-i.

3. **Kontrolli ühendust**
   - Otsi pistiku ikooni (🔌) oma Chainlit liideses
   - Pistiku ikooni kõrval peaks ilmuma number (1), mis näitab edukat ühendust
   - Konsoolis peaks olema näha: "GitHub plugin setup completed successfully" (koos täiendavate olekureaga)

## Tõrkeotsing

### Levinud probleemid

1. **Pordi konflikt**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Lahendus: Muuda porti, kasutades:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Autentimise probleemid**
   - Veendu, et GitHubi mandaadid on õigesti seadistatud
   - Kontrolli, et .env fail sisaldab vajalikke tunnuseid
   - Veendu, et GitHubi API-le on juurdepääs

3. **Ühendus ebaõnnestus**
   - Kontrolli, kas server töötab eeldataval pordil
   - Kontrolli tulemüüri seadeid
   - Veendu, et Python keskkonnas on vajalikud paketid olemas

## Ühenduse kontrollimine

Teie MCP server on korralikult ühendatud, kui:
1. Konsoolis kuvatakse "GitHub plugin setup completed successfully"
2. Ühenduse logides kuvatakse "✓ MCP Connection Status: Active"
3. GitHubi käsud töötavad vestlusliideses

## Keskkonnamuutujad

Vajalikud teie .env failis:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Ühenduse testimine

Saada see testisõnum vestluses:
```
Show me the repositories for username: [GitHub Username]
```
Edukas vastus kuvab repositooriumi informatsiooni.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.