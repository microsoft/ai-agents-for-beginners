# Github MCP serveri näide

## Kirjeldus

See oli demoversioon, mis loodi AI agentide hackathoni jaoks, mida korraldas Microsoft Reactor.

See tööriist on mõeldud kasutajate Githubi hoidlate põhjal hackathoni projektide soovitamiseks.
See toimub järgmiselt:

1. **Github Agent** - Kasutab Github MCP serverit hoidlate ja nende hoidlate kohta info toomiseks.
2. **Hackathoni Agent** - Võtab andmed Github Agendilt ja tuleb välja loominguliste hackathoni projektide ideedega, mis põhinevad kasutaja projektidel, keeltest, mida kasutaja kasutab, ning AI agentide hackathoni projektiradadel.
3. **Sündmuste Agent** - Põhinedes hackathoni agendi soovitusel soovitab sündmuste agent selliseid relevantseid sündmusi AI agentide hackathoni sarjast.
## Koodi käivitamine

### Keskkonnamuutujad

See demo kasutab Microsoft Agent Frameworki, Azure OpenAI teenust, Github MCP serverit ja Azure AI otsingut.

Veendu, et sul on õiged keskkonnamuutujad seadistatud nende tööriistade kasutamiseks:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit serveri käivitamine

MCP serveriga ühenduse loomiseks kasutab see demo Chainlit chat-liidest.

Serveri käivitamiseks kasuta oma terminalis järgmist käsku:

```bash
chainlit run app.py -w
```

See peaks käivitama sinu Chainlit serveri aadressil `localhost:8000` ning täitma sinu Azure AI otsingumoodi sisuga `event-descriptions.md`.

## Ühenduse loomine MCP serveriga

Github MCP serveriga ühenduse loomiseks vali "pistik" ikoon "Type your message here.." vestluskasti all:

![MCP Connect](../../../../../translated_images/et/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Sealt saad klõpsata "Connect an MCP" nupule, et lisada käsk Github MCP serveriga ühenduse loomiseks:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Asenda "[YOUR PERSONAL ACCESS TOKEN]" oma tegeliku isikliku ligipääsu tokeniga.

Pärast ühenduse loomist peaks pistiku ikooni kõrvale ilmuma (1), mis kinnitab ühendust. Kui ei ilmu, proovi chainliti server uuesti käivitada käsuga `chainlit run app.py -w`.

## Demo kasutamine

Agentide töövoo käivitamiseks, mis soovitab hackathoni projekte, võid saata sõnumi nagu:

"Soovita hackathoni projekte Github kasutajale koreyspace"

Router Agent analüüsib sinu päringut ja otsustab, milline agentide kombinatsioon (GitHub, Hackathoni ja Sündmuste agent) on sobivaim sinu päringu käsitlemiseks. Agendid töötavad koos, et pakkuda põhjalikke soovitusi, mis põhinevad GitHubi hoidlate analüüsil, projektide ideedel ja asjakohastel tehnoloogiasündmustel.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Sõnumiklausel**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks lugeda usaldusväärseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta käesoleva tõlke kasutamisest tingitud arusaamatuste ega valesti tõlgendamise eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->