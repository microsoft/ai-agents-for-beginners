---
name: local-ai-agents
license: MIT
---
# Lage lokale AI-agenter med Foundry Local og Qwen

> Følgesvennferdighet for [Leksjon 17 – Lage lokale AI-agenter](../../../17-creating-local-ai-agents/README.md).
> Bruk den til å hjelpe en lærer å bygge en agent som resonerer, kaller verktøy og søker
> i dokumentasjon helt på egen maskin — ingen skybasert inferens. Begrunn alle
> anbefalinger i leksjonsinnholdet og den kjørbare notatboken.

## Triggere

Aktiver denne ferdigheten når en lærer ønsker å:
- Kjøre en agent **helt på enheten** for personvern, kostnad eller offline grunner.
- Tjene en modell lokalt med **Foundry Local** og koble til via OpenAI-kompatibelt endepunkt.
- Bruke en **Qwen-funksjonskall**-modell for å drive pålitelige lokale verktøysanrop.
- Legge til **lokal RAG** (Chroma) eller en **lokal MCP-server**.
- Designe en **hybrid** lokal/sky rutingsstrategi.

## Kjerne mental modell

En SLM bytter bredde mot personvern, kostnad og offline-operasjon. Den vinnende
strategien: **la SLM orkestrere og la verktøyene gjøre det tunge arbeidet.** Modellen
trenger ikke å *kjenne* kodebasen — den må vite når den skal kalle
`read_file` og `search_docs`. Det spiller på en SLMs styrke (avgrensede beslutninger
som verktøyvalg) og bort fra dens svakhet (bred kunnskap, lang multi-hopp
resonnering).

## Hvorfor disse spesifikke komponentene

- **Foundry Local** eksponerer et **OpenAI-kompatibelt HTTP-endepunkt**, så sky-agentkode overføres ved å endre bare `base_url` (og bruke en lokal plassholder API-nøkkel). Den velger også automatisk beste bygg (CPU/GPU/NPU) for maskinen.
- **Qwen**-modeller er trent for funksjonskall og sender godt formede verktøysanrop konsekvent — dette er hva som gjør en lokal *chat*-modell til en lokal *agent*.
- **Chroma** kjører i-prosess og lagrer vektorer på disk, så hele RAG-pipelinen (embed → lagre → hente → resonner) forblir lokal.
- **MCP** er et transportlag, ikke en skytjeneste: en MCP-server kan kjøre lokalt over `stdio`.

## Nødvendig oppsett

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # lokal plassholder
```

~8 GB RAM er et realistisk minimum; en GPU/NPU hjelper, men er ikke nødvendig.

## Viktige mønstre å gjenskape

Peker læreren til notatboken
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Sandkasseverktøy**: hvert filverktøy løser stier og avviser alt utenfor en enkelt prosjektrot — selv lokalt kjører et verktøy med brukerens tillatelser.
- **Verktøysanropsløkke**: registrer verktøy med OpenAI verktøyskjema, kjør etterspurte verktøy lokalt, mat tilbake resultater, gjenta til endelig svar.
- **Lokal RAG**: oppdater dokumenter i en Chroma-samling; `search_docs` returnerer topp-k biter.
- **Lokal MCP**: koble til en lokal server over `stdio`; avgrens den til en prosjektdirektorium og valider resultatene.

## Hybrid ruting (lokalt som en av modellene)

| Situasjon | Hvor det kjører |
|-----------|---------------|
| Sensitive data / offline | Lokal SLM |
| Enkelt, avgrenset oppgave | Lokal SLM (billig, rask) |
| Vanskelig multi-hopp resonnering på ikke-sensitive data | Sky-modell |
| Sky-nedetid | Lokal SLM (grasiøs degradering) |

Dette speiler modell-rutingsideen fra Leksjon 16, med arbeidsstasjonen som en
av rutene. Foretrekk design som faller tilbake til lokalt slik at agenten degraderer i
kvalitet fremfor å feile fullstendig.

## Vernerekkverk for assistenten

- Hold alle fil-/verktøyoperasjoner begrenset til en sandkasse prosjektmappe.
- Ikke send kode eller data til skyen når lærerens uttalte mål er personvern/offline — hold hele pipelinen lokal.
- Sett realistiske forventninger til SLM-kvalitet; støtt deg på verktøy og RAG fremfor modellens memoriserte kunnskap.
- Merk at Leksjon 17 **ikke** har Foundry Responses-endepunkt, så sky-røyk-testaksjonen gjelder ikke — valider ved å kjøre notatboken lokalt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->