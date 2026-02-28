# Github MCP Server Esimerkki

## Kuvaus

Tämä oli demo, joka luotiin AI Agents Hackathonia varten, jota isännöi Microsoft Reactor.

Työkaluja käytetään suosittelemaan hackathon-projekteja käyttäjän Github-repojen perusteella.
Tämä tehdään seuraavasti:

1. **Github Agent** - Käyttää Github MCP -palvelinta hakemaan repositoriot ja tietoja niistä.
2. **Hackathon Agent** - Ottaa Github Agentin tiedot ja kehittelee luovia hackathon-projektiehdotuksia perustuen projekteihin, käyttäjän käyttämiin kieliin ja AI Agents -hackathonin projektiratoihin.
3. **Events Agent** - Hackathon-agenetin ehdotuksen perusteella Events Agent suosittelee asiaankuuluvia tapahtumia AI Agent Hackathon -sarjasta.
## Koodin suorittaminen 

### Ympäristömuuttujat

Tämä demo käyttää Microsoft Agent Frameworkia, Azure OpenAI Servicea, Github MCP Serveriä ja Azure AI Searchia.

Varmista, että sinulla on asianmukaiset ympäristömuuttujat asetettuna näiden työkalujen käyttöä varten:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit-palvelimen suorittaminen

Tämän demon MCP-palvelimeen yhdistämiseksi käytetään Chainlit:iä keskustelukäyttöliittymänä. 

Palvelimen käynnistämiseksi käytä seuraavaa komentoa terminaalissasi:

```bash
chainlit run app.py -w
```

Tämän pitäisi käynnistää Chainlit-palvelimesi osoitteessa `localhost:8000` sekä täyttää Azure AI Search -indeksisi `event-descriptions.md`-sisällöllä. 

## Yhdistäminen MCP-palvelimeen

Yhdistääksesi Github MCP Serveriin, valitse "pistoke"-ikoni "Kirjoita viestisi tähän.." -chat-ruudun alapuolelta:

![MCP-yhteys](../../../../../translated_images/fi/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Sieltä voit klikata "Yhdistä MCP" lisätäksesi komennon yhdistääksesi Github MCP Serveriin:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

After connecting, you should see a (1) next to the plug icon to confirm that its connected. If not, try restarting the chainlit server with `chainlit run app.py -w`.

## Demon käyttö 

Aloittaaksesi agenttien työnkulun, jossa suositellaan hackathon-projekteja, voit kirjoittaa viestin kuten: 

"Suosittele hackathon-projekteja Github-käyttäjälle koreyspace"

Router Agent analysoi pyyntösi ja päättää, mikä agenttien yhdistelmä (GitHub, Hackathon ja Events) sopii parhaiten käsittelemään kyselyäsi. Agentit toimivat yhdessä tarjotakseen kattavia suosituksia perustuen GitHub-repositorion analyysiin, projektien ideointiin ja asiaankuuluviin teknologiatapahtumiin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty tekoälykäännöspalvelulla Co-op Translator (https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää auktoritatiivisena lähteenä. Kriittisten tietojen osalta suosittelemme ammattimaista ihmiskääntäjän tekemää käännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->