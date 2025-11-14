<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-10-11T11:29:29+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "et"
}
-->
# Github MCP Server Näide

## Kirjeldus

See demo loodi AI Agentide Hackathoni jaoks, mida korraldas Microsoft Reactor.

Tööriist on mõeldud hackathoni projektide soovitamiseks kasutaja Githubi reposide põhjal. See toimub järgmiselt:

1. **Github Agent** - Kasutab Github MCP Serverit, et hankida reposid ja nende kohta teavet.
2. **Hackathoni Agent** - Võtab Github Agenti andmed ja loob loovaid hackathoni projektide ideid, lähtudes kasutaja projektidest, kasutatud programmeerimiskeeltest ja AI Agentide hackathoni projektiradadest.
3. **Sündmuste Agent** - Hackathoni agendi soovituste põhjal soovitab sündmuste agent asjakohaseid sündmusi AI Agentide Hackathoni sarjast.

## Koodi käivitamine

### Keskkonnamuutujad

See demo kasutab Azure Open AI teenust, Semantic Kernelit, Github MCP Serverit ja Azure AI Searchi.

Veendu, et sul on õiged keskkonnamuutujad seadistatud nende tööriistade kasutamiseks:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Chainlit Serveri käivitamine

MCP serveriga ühenduse loomiseks kasutab see demo Chainlit'i vestlusliidest.

Serveri käivitamiseks kasuta oma terminalis järgmist käsku:

```bash
chainlit run app.py -w
```


See peaks käivitama sinu Chainlit serveri aadressil `localhost:8000` ning täitma sinu Azure AI Search indeksi `event-descriptions.md` sisuga.

## MCP Serveriga ühenduse loomine

Github MCP Serveriga ühenduse loomiseks vali "pistiku" ikoon, mis asub "Sisesta oma sõnum siia.." vestluskasti all:

![MCP Ühendus](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.et.png)

Sealt saad klõpsata "Connect an MCP", et lisada käsk Github MCP Serveriga ühenduse loomiseks:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


Asenda "[YOUR PERSONAL ACCESS TOKEN]" oma tegeliku isikliku juurdepääsulubade tokeniga.

Pärast ühenduse loomist peaks pistiku ikooni kõrval ilmuma (1), mis kinnitab, et ühendus on loodud. Kui ei, proovi Chainlit serverit uuesti käivitada käsuga `chainlit run app.py -w`.

## Demo kasutamine

Agentide töövoo käivitamiseks hackathoni projektide soovitamiseks võid sisestada sõnumi nagu:

"Soovita hackathoni projekte Githubi kasutajale koreyspace"

Router Agent analüüsib sinu päringut ja määrab, milline agentide kombinatsioon (GitHub, Hackathon ja Events) sobib kõige paremini sinu päringu käsitlemiseks. Agendid töötavad koos, et pakkuda põhjalikke soovitusi, mis põhinevad Githubi reposide analüüsil, projektide ideedel ja asjakohastel tehnoloogiasündmustel.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.