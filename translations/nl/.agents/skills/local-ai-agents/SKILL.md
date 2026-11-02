---
name: local-ai-agents
license: MIT
---
# Lokale AI-agents maken met Foundry Local en Qwen

> Bijbehorende vaardigheid voor [Les 17 – Lokale AI-agents maken](../../../17-creating-local-ai-agents/README.md).
> Gebruik het om een lerende te helpen een agent te bouwen die redeneert, tools aanroept en
> documentatie doorzoekt volledig op hun eigen machine — geen cloud-inferentie. Baseer elke
> aanbeveling op de lesinhoud en het uitvoerbare notitieboek.

## Triggers

Activeer deze vaardigheid wanneer een lerende wil:
- Een agent **volledig on-device** draaien om privacy-, kosten- of offline-redenen.
- Een model lokaal aanbieden met **Foundry Local** en verbinding maken via de OpenAI-compatibele endpoint.
- Een **Qwen function-calling** model gebruiken om betrouwbare lokale tool-aanroepen te sturen.
- **Lokale RAG** (Chroma) of een **lokale MCP-server** toevoegen.
- Een **hybride** lokaal/cloud routeringsstrategie ontwerpen.

## Kern mentale model

Een SLM ruilt breedte in voor privacy, kosten en offline werking. De winnende
strategie: **laat de SLM orkestreren en laat tools het zware werk doen.** Het
model hoeft de codebasis niet te *kennen* — het hoeft alleen te weten wanneer het
`read_file` en `search_docs` moet aanroepen. Dat speelt in op de kracht van een SLM (begrensde beslissingen
zoals tool-selectie) en maakt gebruik van zijn zwakte (brede kennis, lange multi-hop
redenering).

## Waarom juist deze onderdelen

- **Foundry Local** biedt een **OpenAI-compatibele HTTP-endpoint** aan, zodat cloud agentcode overgezet kan worden door alleen `base_url` te wijzigen (en een lokale tijdelijke API-sleutel te gebruiken). Het selecteert ook automatisch de beste build (CPU/GPU/NPU) voor de machine.
- **Qwen** modellen zijn getraind voor function calling en genereren consequent goed gevormde tool-aanroepen — dit verandert een lokaal *chat* model in een lokale *agent*.
- **Chroma** draait in-process en slaat vectoren op schijf op, zodat de hele RAG-pijplijn (embed → opslaan → ophalen → redeneren) lokaal blijft.
- **MCP** is een transport, geen cloudservice: een MCP-server kan lokaal draaien via `stdio`.

## Belangrijke setup-essenties

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

~8 GB RAM is een realistisch minimum; een GPU/NPU helpt maar is niet verplicht.

## Belangrijke patronen om te reproduceren

Verwijs de lerende naar het notitieboek
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Sandboxed tools**: elke bestandstool lost paden op en weigert alles buiten één project-root — zelfs lokaal draait een tool met de permissies van de gebruiker.
- **Tool-aanroep lus**: registreer tools met het OpenAI tool-schema, voer de gevraagde tools lokaal uit, voed de resultaten terug, herhaal tot een definitief antwoord.
- **Lokale RAG**: pas documenten toe in een Chroma-collectie; `search_docs` retourneert top-k fragmenten.
- **Lokale MCP**: verbind met een lokale server via `stdio`; scopeer het naar een projectdirectory en valideer de outputs.

## Hybride routering (lokaal als één van de modellen)

| Situatie | Waar het draait |
|-----------|---------------|
| Gevoelige data / offline | Lokale SLM |
| Eenvoudige, begrensde taak | Lokale SLM (goedkoop, snel) |
| Moeilijke multi-hop redenering op niet-gevoelige data | Cloud model |
| Cloud uitval | Lokale SLM (gracieuze degradatie) |

Dit weerspiegelt het modelrouteringsidee uit Les 16, met de werkplek als één
van de routes. Geef voorkeur aan ontwerpen die terugvallen op lokaal zodat de agent degradeert in
kwaliteit in plaats van volledig faalt.

## Veilgheden voor de assistent

- Houd elke bestand/tool operatie beperkt tot een sandboxed projectdirectory.
- Stuur geen code of data naar de cloud wanneer het opgegeven doel van de lerende privacy/offline is — hou de hele pijplijn lokaal.
- Stel realistische verwachtingen voor SLM-kwaliteit; leun op tools en RAG in plaats van op de gememoriseerde kennis van het model.
- Let op dat Les 17 **geen** Foundry Responses-endpoint heeft, dus de cloud smoke-test actie niet van toepassing is — valideer door het notitieboek lokaal uit te voeren.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->