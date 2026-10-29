---
name: local-ai-agents
description: Build local-first AI agents that run entirely on a developer workstation with Microsoft Foundry Local and Qwen function-calling models. Covers sandboxed local tools, local RAG with Chroma, local MCP servers, hybrid cloud/local routing, and privacy, cost, and offline trade-offs.
license: MIT
---
# Paikallisten tekoälyagenttien luominen Foundry Localin ja Qwenin avulla

> Seuraava taito tukee [Oppitunti 17 – Paikallisten tekoälyagenttien luominen](../../../17-creating-local-ai-agents/README.md).
> Käytä sitä auttamaan oppijaa rakentamaan agentti, joka päättää, kutsuu työkaluja ja etsii
> dokumentaatiota kokonaan omalla koneellaan — ilman pilvipalvelimen tulkintaa. Perusta kaikki
> suositukset oppitunnin sisältöön ja ajettavaan muistikirjaan.

## Laukaisimet

Aktivoi tämä taito, kun oppija haluaa:
- Suorittaa agentin **täysin laitteella** yksityisyyden, kustannusten tai offline-tilan vuoksi.
- Palvella mallia paikallisesti **Foundry Localilla** ja yhdistää OpenAI-yhteensopivan päätepisteen kautta.
- Käyttää **Qwen-funktiokutsumallia** luotettavien paikallisten työkalukutsujen ajamiseen.
- Lisätä **paikallinen RAG** (Chroma) tai **paikallinen MCP-palvelin**.
- Suunnitella **hybridimallinen** paikallinen/pilvierottelu.

## Keskeinen ajatusmalli

SLM (pieni kielimalli) uhraa laajuuden yksityisyydelle, kustannuksille ja offline-toiminnalle. Voittava
strategia: **anna SLM:n orkestroida ja anna työkalujen hoitaa raskas työ.** Mallin ei tarvitse 
*tuntea* koodipohjaa — sen täytyy tietää, milloin kutsua
`read_file` ja `search_docs`. Tämä hyödyntää SLM:n vahvuuksia (rajatut päätökset kuten työkalun valinta)
ja välttää sen heikkouksia (laaja tieto, monivaiheinen päättely).


## Miksi juuri nämä osat

- **Foundry Local** tarjoaa **OpenAI-yhteensopivan HTTP-päätepisteen**, joten pilviagentin koodi siirtyy muuttamalla vain `base_url` (ja käyttämällä paikallista paikkamerkki-API-avainta). Se myös valitsee automaattisesti parhaan rakennelman (CPU/GPU/NPU) koneelle.
- **Qwen**-mallit on koulutettu funktiokutsuihin ja ne tuottavat johdonmukaisesti hyvin muodostettuja työkalukutsuja — tämä muuttaa paikallisen *keskustelu*mallin paikalliseksi *agentiksi*.
- **Chroma** toimii prosessissa ja tallentaa vektorit levylle, joten koko RAG-putki (upotus → tallennus → haku → päättely) pysyy paikallisena.
- **MCP** on siirtotekniikka, ei pilvipalvelu: MCP-palvelin voi toimia paikallisesti `stdio` yli.

## Asennusvaatimukset

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # local placeholder
```

Noin 8 GB RAM on realistinen vähimmäisvaatimus; GPU/NPU auttaa, mutta ei ole pakollinen.

## Tärkeimmät mallit jäljittelyyn

Opasta oppijaa käyttämään muistikirjaa
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Säilötyt työkalut**: jokainen tiedostotyökalu ratkaisee polut ja hylkää kaiken yhden projektin juurihakemiston ulkopuolelta — jopa paikallisesti työkalu toimii käyttäjän oikeuksilla.
- **Työkalukutsusilmukka**: rekisteröi työkalut OpenAI-työkalu-kaavion kanssa, suorita pyydetyt työkalut paikallisesti, palautetaan tulokset, toista kunnes saadaan lopullinen vastaus.
- **Paikallinen RAG**: päivitä dokumentit Chroman kokoelmaan; `search_docs` palauttaa top-k-palasia.
- **Paikallinen MCP**: yhdistä paikalliseen palvelimeen `stdio` kautta; rajaa projektiin ja validoi sen tulokset.

## Hybridirakenteet (paikallinen yhtenä malleista)

| Tilanne | Missä se ajetaan |
|-----------|---------------|
| Herkkä data / offline | Paikallinen SLM |
| Yksinkertainen, rajattu tehtävä | Paikallinen SLM (halpa, nopea) |
| Vaikea monivaiheinen päättely epäherkässä datassa | Pilvimalli |
| Pilvipalvelun häiriö | Paikallinen SLM (pehmeä degradatio) |

Tämä heijastaa mallin ohjauksen ideaa Oppitunnista 16, jolloin työasema on yksi
reiteistä. Suosi malleja, jotka tarvittaessa tukeutuvat paikalliseen, jotta agentti heikkenee
laadultaan sen sijaan, että epäonnistuisi kokonaan.

## Avustajan turvaverkot

- Pidä jokainen tiedosto-/työkaluoperaatio rajattuna säilöttyyn projektihakemistoon.
- Älä lähetä koodia tai dataa pilveen, kun oppijan tavoite on yksityisyys/offline — pidä koko putki paikallisena.
- Aseta realistiset odotukset SLM:n laadulle; luota työkaluihin ja RAGiin mieluummin kuin mallin muistiin.
- Huomioi, että Oppitunnilla 17 ei ole Foundry Responses -päätepistettä, joten pilven toiminnan savutesti ei päde — vahvista suorittamalla muistikirja paikallisesti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->