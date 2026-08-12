---
name: local-ai-agents
license: MIT
---
# Kohalike tehisintellekti agentide loomine Foundry Locali ja Qweni abil

> Kaaslane oskuste jaoks [Õppetund 17 – Kohalike tehisintellekti agentide loomine](../../../17-creating-local-ai-agents/README.md).
> Kasuta seda, et aidata õppijal ehitada agent, kes arutleb, kutsub tööriistu ja otsib
> dokumentatsiooni täielikult omaenda masinal — pilveta ennustamist. Tugevda iga
> soovitus õppetunni sisu ja käivitatava märkmikuga.

## Käivitajad

Aktiveeri see oskus, kui õppija soovib:
- Käivitada agent **täielikult seadmes** privaatsuse, kulu või võrguühenduseta tööks.
- Teenindada mudelit lokaalselt **Foundry Localiga** ja ühenduda OpenAI-ühilduva lõpp-punkti kaudu.
- Kasutada **Qweni funktsioonikutsumise** mudelit usaldusväärsete kohalike tööriistakutsete jaoks.
- Lisada **kohalik RAG** (Chroma) või **kohalik MCP server**.
- Kujundada **hübriidne** lokaalse/pilve marsruutimise strateegia.

## Põhimudel

SLM vahetab laiuse privaatsuse, kulu ja võrguühenduseta töö vastu. Võitja
strateegia: **lase SLM-il orkestreerida ja tööriistadel teha raske töö.** Mudel
ei pea *teadma* koodibaasi — ta peab teadma, millal kutsuda `read_file` ja `search_docs`.
See mängib SLMi tugevust (piiratud otsused nagu tööriista valik) ja hoiab eemal tema nõrkusest (lai teadmine, pikk mitmeastmeline arutlus).



## Miks just need osad

- **Foundry Local** eksponeerib **OpenAI-ühilduvat HTTP lõpp-punkti**, nii et pilveagentide kood kandub üle vaid `base_url` muutmisega (ja kasutades kohalikku kohahoidja API võtit). See valib ka masina jaoks parima ülesehituse (CPU/GPU/NPU).
- **Qwen** mudelid on koolitatud funktsioonikutsumiseks ja esitavad järjepidevalt korrektsed tööriistakutsed — see muudab kohalikust *vestlus* mudelist lokaalse *agendi*.
- **Chroma** töötab protsessis ja salvestab vektoreid kettale, nii et kogu RAG torujuhtme (embedding → salvestamine → taasesitamine → arutlus) saab hoida lokaalsena.
- **MCP** on transpordikiht, mitte pilveteenus: MCP server saab töötada lokaalselt üle `stdio`.

## Seadistuse põhitõed

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # kohalik kohatäide
```

~8 GB RAM on realistlik miinimum; GPU/NPU aitab kuid ei ole vajalik.

## Peamised mustrid, mida korduda

Suuna õppija märkmikule
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Kitsaskohastatud tööriistad**: iga failitööriist lahendab rajad ja keelab kõike, mis jääb väljapoole üht projekti juurkausta — isegi kohapeal töötab tööriist kasutaja õigustes.
- **Tööriistakutseloop**: registreeri tööriistad OpenAI tööriistade skeemiga, käivita taotletud tööriistad kohapeal, sööta tulemused tagasi, korda kuni lõpliku vastuseni.
- **Kohalik RAG**: lisa dokumendid Chroma kollektsiooni; `search_docs` tagastab top-k osad.
- **Kohalik MCP**: ühenda kohalikku serverisse üle `stdio`; piira see projekti kaustaga ja valideeri väljundid.

## Hübriidmarsruutimine (lokaalne kui üks mudelitest)

| Situatsioon | Kus see töötab |
|-----------|---------------|
| Tundlikud andmed / võrguühenduseta | Kohalik SLM |
| Lihtne, piiratud ülesanne | Kohalik SLM (odav, kiire) |
| Raske mitmeastmeline arutlus tundmatutel andmetel | Pilvemudel |
| Pilvekatkestus | Kohalik SLM (sujuv degradeerumine) |

See peegeldab mudelimarsruutimise mõtet Õppetunnist 16, kus töölauaarvuti on üks marsruutidest. Eelista lahendusi, mis langevad tagasi kohalikule, nii et agent degradeerub kvaliteedis, mitte ei vea läbi.



## Assistentide ohutusmeetmed

- Hoia iga faili/tööriista tegevus piiratud kitsaskohastatud projekti kaustaga.
- Ära saada koodi ega andmeid pilve, kui õppija eesmärk on privaatsus/võrguühenduseta — hoia kogu torujuhe kohalik.
- Sea realistlikud ootused SLM kvaliteedile; toetu tööriistadele ja RAGile, mitte mudeli meelde jäetud teadmistele.
- Pane tähele, et Õppetund 17-l puudub **Foundry Responses** lõpp-punkt, seega pilvemudeli suitsutesti tegevus ei kehti — valideeri, käivitades märkmiku kohalikult.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->