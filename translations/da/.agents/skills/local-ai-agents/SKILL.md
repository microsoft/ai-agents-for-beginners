---
name: local-ai-agents
license: MIT
---
# Oprettelse af lokale AI-agenter med Foundry Local og Qwen

> Følgesvendfærdighed til [Lektion 17 – Oprettelse af lokale AI-agenter](../../../17-creating-local-ai-agents/README.md).
> Brug den til at hjælpe en lærende med at opbygge en agent, der ræsonnerer, kalder værktøjer og søger
> i dokumentationen helt på deres egen maskine — ingen cloud inferens. Forankr enhver
> anbefaling i lektionsindholdet og den kørbare notesbog.

## Udløsere

Aktivér denne færdighed, når en lærende ønsker at:
- Køre en agent **fuldt ud på enheden** af hensyn til privatliv, omkostninger eller offline-grunde.
- Servere en model lokalt med **Foundry Local** og forbinde via den OpenAI-kompatible endpoint.
- Bruge en **Qwen funktion-kalds** model til at styre pålidelige lokale værktøjskald.
- Tilføje **lokal RAG** (Chroma) eller en **lokal MCP-server**.
- Designe en **hybrid** lokal/cloud routingstrategi.

## Kerne mental model

En SLM bytter bredde for privatliv, omkostninger og offline-drift. Den vindende
strategi: **lad SLM’en orkestrere og lad værktøjerne tage det tunge løft.** Modellen
behøver ikke at *kende* kodebasen — den skal vide, hvornår den skal kalde
`read_file` og `search_docs`. Det spiller på en SLM’s styrke (begrænsede beslutninger
som valg af værktøj) og væk fra dens svaghed (bred viden, lang multi-hop
ræsonnering).

## Hvorfor netop disse komponenter

- **Foundry Local** eksponerer en **OpenAI-kompatibel HTTP-endpoint**, så cloud-agent kode overføres ved blot at ændre `base_url` (og bruge en lokal placeholder API-nøgle). Den vælger også automatisk det bedste build (CPU/GPU/NPU) til maskinen.
- **Qwen** modeller er trænet til funktionskald og udsender konsekvent velstrukturerede værktøjskald — det er det, der forvandler en lokal *chat* model til en lokal *agent*.
- **Chroma** kører in-process og lagrer vektorer på disk, så hele RAG-pipelinen (embed → store → retrieve → reason) forbliver lokal.
- **MCP** er et transportlag, ikke en cloud-tjeneste: en MCP-server kan køre lokalt over `stdio`.

## Opsætningsnødvendigheder

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

~8 GB RAM er et realistisk minimum; en GPU/NPU hjælper, men er ikke påkrævet.

## Nøglemønstre at gengive

Peg den lærende mod notesbogen
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Sandkasse-værktøjer**: hvert filværktøj løser stier og afviser alt uden for en enkelt projektrod — selv lokalt kører et værktøj med brugerens tilladelser.
- **Værktøjskald-loop**: registrer værktøjer med OpenAI’s værktøjsskema, udfør forespurgte værktøjer lokalt, fød resultaterne tilbage, gentag indtil endeligt svar.
- **Lokal RAG**: indsæt dokumenter i en Chroma-kollektion; `search_docs` returnerer top-k uddrag.
- **Lokal MCP**: forbind til en lokal server over `stdio`; afgræns den til en projektmappe og valider dens output.

## Hybrid routing (lokal som en af modellerne)

| Situation | Hvor den kører |
|-----------|---------------|
| Følsomme data / offline | Lokal SLM |
| Simpel, afgrænset opgave | Lokal SLM (billig, hurtig) |
| Svær multi-hop ræsonnering på ikke-følsomme data | Cloud model |
| Cloud nedbrud | Lokal SLM (graceful nedtrapning) |

Dette spejler model-routing idéen fra Lektion 16, med arbejdsstationen som en
af ruterne. Foretræk designs, der falder tilbage på lokalt, så agenten degraderer i
kvalitet i stedet for at fejle helt.

## Sikkerhedsrækkefølger for assistenten

- Hold enhver fil-/værktøjsoperation afgrænset til en sandkasse-projektmappe.
- Send ikke kode eller data til skyen, når den lærendes udtrykte mål er privatliv/offline — hold hele pipeline lokal.
- Sæt realistiske forventninger til SLM-kvalitet; læn dig på værktøjer og RAG frem for modellens memoriserede viden.
- Bemærk at Lektion 17 **ikke har noget** Foundry Responses endpoint, så cloud smoke-test handlinger gælder ikke — valider ved at køre notesbogen lokalt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->