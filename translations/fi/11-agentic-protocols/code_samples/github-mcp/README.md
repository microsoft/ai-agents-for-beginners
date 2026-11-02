# Github MCP Server Esimerkki

## Kuvaus

Tämä oli demo, joka luotiin AI Agents Hackathonia varten, joka järjestettiin Microsoft Reactorin kautta.

Työkaluja käytetään suosittelemään hackathon-projekteja käyttäjän Github-repositorioden perusteella.
Tämä tehdään seuraavasti:

1. **Github Agent** - Käyttämällä Github MCP Serveriä hakemaan repoja ja tietoja näistä repoista.
2. **Hackathon Agent** - Ottaa Github Agentin tiedot ja kehittää luovia hackathon-projektideoita perustuen projekteihin, käyttäjän käyttämiin ohjelmointikieliin ja AI Agents -hackathonin projektiratoihin.
3. **Events Agent** - Hackathon-agentin ehdotuksen perusteella Events Agent suosittelee asiaankuuluvia tapahtumia AI Agent Hackathon -sarjasta.
## Koodin ajaminen 

### Ympäristömuuttujat

Tämä demo käyttää Microsoft Agent Frameworkia, Azure OpenAI Serviceä, Github MCP Serveriä ja Azure AI Searchia.

Varmista, että sinulla on asianmukaiset ympäristömuuttujat asetettu näiden työkalujen käyttöä varten:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit-palvelimen ajaminen

Yhdistääksesi MCP-palvelimeen, tämä demo käyttää Chainlitia chat-käyttöliittymänä. 

Palvelimen käynnistämiseksi käytä seuraavaa komentoa terminaalissasi:

```bash
chainlit run app.py -w
```

Tämän pitäisi käynnistää Chainlit-palvelimesi osoitteessa `localhost:8000` sekä täyttää Azure AI Search -indeksisi `event-descriptions.md`-sisällöllä. 

## Yhdistäminen MCP-palvelimeen

Yhdistääksesi Github MCP Serveriin valitse "plug" -ikoni "Type your message here.." -tekstikentän alapuolelta:

![MCP-yhteys](../../../../../translated_images/fi/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Siitä voit klikata "Connect an MCP" lisätäksesi komennon yhdistääksesi Github MCP Serveriin:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

Kun yhteys on muodostettu, sinun pitäisi nähdä (1) pistokkeen vieressä vahvistuksena siitä, että se on yhdistetty. Jos ei, yritä käynnistää chainlit-palvelin uudelleen komennolla `chainlit run app.py -w`.

## Demon käyttäminen 

Aloittaaksesi agenttityönkulun, jossa suositellaan hackathon-projekteja, voit kirjoittaa viestin kuten: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent analysoi pyyntösi ja päättää, mikä agenttien yhdistelmä (GitHub, Hackathon, ja Events) sopii parhaiten käsittelemään kyselyäsi. Agentit toimivat yhdessä tarjotakseen kattavia suosituksia GitHub-repositorion analyysin, projektien ideoinnin ja asiaankuuluvien alan tapahtumien perusteella.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty tekoälykäännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automatisoiduissa käännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää määräävänä lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai tulkintavirheistä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->