<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T18:33:07+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "fi"
}
-->
# Github MCP Server Esimerkki

## Kuvaus

Tämä on demo, joka luotiin AI Agents Hackathon -tapahtumaa varten, järjestetty Microsoft Reactorin kautta.

Työkalu suosittelee hackathon-projekteja käyttäjän Github-repositorioiden perusteella. Tämä tapahtuu seuraavasti:

1. **Github Agent** - Käyttää Github MCP Serveriä hakeakseen repositorioita ja tietoa niistä.
2. **Hackathon Agent** - Käyttää Github Agentin dataa ja kehittää luovia hackathon-projekti-ideoita käyttäjän projekteihin, käytettyihin ohjelmointikieliin ja AI Agents Hackathonin projektiraitoihin perustuen.
3. **Events Agent** - Hackathon Agentin ehdotusten perusteella Events Agent suosittelee relevantteja tapahtumia AI Agents Hackathon -sarjasta.

## Koodin suorittaminen 

### Ympäristömuuttujat

Tämä demo käyttää Azure Open AI Servicea, Semantic Kernelia, Github MCP Serveriä ja Azure AI Searchia.

Varmista, että sinulla on oikeat ympäristömuuttujat asetettuna näiden työkalujen käyttöä varten:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Serverin käynnistäminen

Yhdistääksesi MCP-serveriin, tämä demo käyttää Chainlitia chat-käyttöliittymänä.

Käynnistääksesi serverin, käytä seuraavaa komentoa terminaalissasi:

```bash
chainlit run app.py -w
```

Tämän pitäisi käynnistää Chainlit-serverisi osoitteessa `localhost:8000` sekä täyttää Azure AI Search -indeksisi `event-descriptions.md` -sisällöllä.

## Yhdistäminen MCP Serveriin

Yhdistääksesi Github MCP Serveriin, valitse "pistoke"-ikoni "Type your message here.." -chat-laatikon alapuolelta:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.fi.png)

Tämän jälkeen voit klikata "Connect an MCP" lisätäksesi komennon, joka yhdistää Github MCP Serveriin:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Korvaa "[YOUR PERSONAL ACCESS TOKEN]" omalla henkilökohtaisella pääsytunnuksellasi.

Yhdistämisen jälkeen pistoke-ikonin vieressä pitäisi näkyä (1) vahvistuksena siitä, että yhteys on muodostettu. Jos ei, kokeile käynnistää Chainlit-serveri uudelleen komennolla `chainlit run app.py -w`.

## Demon käyttäminen 

Aloittaaksesi agenttityöskentelyn hackathon-projektien suosittelemiseksi, voit kirjoittaa viestin, kuten:

"Suosittele hackathon-projekteja Github-käyttäjälle koreyspace"

Router Agent analysoi pyyntösi ja määrittää, mikä yhdistelmä agenteista (GitHub, Hackathon ja Events) sopii parhaiten kyselysi käsittelyyn. Agentit työskentelevät yhdessä tarjotakseen kattavia suosituksia Github-repositorioiden analyysin, projektien ideoinnin ja relevanttien teknologiatapahtumien perusteella.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.