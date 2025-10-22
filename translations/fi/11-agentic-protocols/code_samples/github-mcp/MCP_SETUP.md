<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T18:40:14+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "fi"
}
-->
# MCP Serverin integrointiohje

## Esivaatimukset
- Node.js asennettuna (versio 14 tai uudempi)
- npm-pakettienhallinta
- Python-ympäristö tarvittavilla riippuvuuksilla

## Asennusvaiheet

1. **Asenna MCP Server -paketti**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Käynnistä MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Palvelimen pitäisi käynnistyä ja näyttää yhteys-URL.

3. **Vahvista yhteys**
   - Etsi pistokkeen kuvake (🔌) Chainlit-käyttöliittymästä
   - Pistokkeen kuvakkeen vieressä pitäisi näkyä numero (1), joka osoittaa onnistuneen yhteyden
   - Konsolissa pitäisi näkyä: "GitHub plugin setup completed successfully" (sekä muita tilarivejä)

## Vianmääritys

### Yleiset ongelmat

1. **Porttikonflikti**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Ratkaisu: Vaihda portti käyttämällä:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Todennusongelmat**
   - Varmista, että GitHub-tunnukset on määritetty oikein
   - Tarkista, että .env-tiedostossa on tarvittavat tokenit
   - Vahvista GitHub API -pääsy

3. **Yhteys epäonnistui**
   - Varmista, että palvelin toimii odotetulla portilla
   - Tarkista palomuuriasetukset
   - Vahvista, että Python-ympäristössä on tarvittavat paketit

## Yhteyden vahvistaminen

MCP-palvelimesi on yhdistetty oikein, kun:
1. Konsolissa näkyy "GitHub plugin setup completed successfully"
2. Yhteyslokeissa näkyy "✓ MCP Connection Status: Active"
3. GitHub-komennot toimivat chat-käyttöliittymässä

## Ympäristömuuttujat

Tarvitaan .env-tiedostossa:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Yhteyden testaaminen

Lähetä tämä testiviesti chatissa:
```
Show me the repositories for username: [GitHub Username]
```  
Onnistunut vastaus näyttää tietoja repositoriosta.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.