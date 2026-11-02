# Github MCP serveri näide

## Kirjeldus

See oli demo, mis loodi Microsoft Reactori kaudu korraldatud AI Agentide hackathoni jaoks.

Seda tööriista kasutatakse kasutaja Githubi hoidlate põhjal hackathoni projektide soovitamiseks. Seda tehakse järgmiselt:

1. **Github Agent** – Kasutab Github MCP Serverit hoidlate ja nende hoidlate kohta käiva teabe hankimiseks.
2. **Hackathoni agent** – Võtab Githubi agendilt saadud andmed ja tuleb välja loominguliste hackathoni projektide ideedega, mis põhinevad kasutaja projektidel, kasutatavatel keeltes ning AI Agentide hackathoni projektiradadel.
3. **Sündmuste agent** – Põhinedes hackathoni agendi soovitusel soovitab vastavaid üritusi AI Agentide hackathoni sarjast.

## Koodi käivitamine

### Keskkonnamuutujad

See demo kasutab Microsoft Agent Frameworki, Azure OpenAI teenust, Github MCP Serverit ja Azure AI Searchi.

Veenduge, et teil on õiged keskkonnamuutujad seadistatud nende tööriistade kasutamiseks:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Chainlit serveri käivitamine

MCP serveriga ühenduse loomiseks kasutab see demo Chainlit’it vestlusliidesena.

Serveri käivitamiseks kasutage oma terminalis järgmist käsku:

```bash
chainlit run app.py -w
```


See peaks käivitama teie Chainlit serveri aadressil `localhost:8000` ning täitma teie Azure AI Searchi indeksit `event-descriptions.md` sisuga.

## Ühenduse loomine MCP serveriga

Github MCP Serveriga ühenduse loomiseks valige "pistikupesa" ikoon "Type your message here.." vestlusakna all:

![MCP Connect](../../../../../translated_images/et/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Sealt saate klõpsata "Connect an MCP" nuppu, et lisada käsk Github MCP Serveriga ühenduse loomiseks:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


Asendage "[YOUR PERSONAL ACCESS TOKEN]" oma tegeliku isikliku juurdepääsutokniga.

Pärast ühenduse loomist peaks pistikupesa ikooni kõrvale ilmuma (1), mis kinnitab, et ühendus on loodud. Kui ei, proovige Chainlit server uuesti käivitada käsuga `chainlit run app.py -w`.

## Demo kasutamine

Hackathoni projektide soovitamise agentide töövoo alustamiseks võite kirjutada sõnumi näiteks:

"Soovita hackathoni projekte Github kasutajale koreyspace"

Router Agent analüüsib teie päringut ning otsustab, milline agentide kombinatsioon (GitHub, Hackathon ja Events) sobib teie päringuga tegelemiseks kõige paremini. Agentide koostöö võimaldab pakkuda põhjalikke soovitusi, mis põhinevad GitHubi hoidlate analüüsil, projektide ideede genereerimisel ja asjakohastel tehnikasündmustel.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud tehisintellektil põhineva tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame täpsust, palun pange tähele, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega kaasnevate arusaamatuste või valesti tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->