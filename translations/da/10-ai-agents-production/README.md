# AI-agenter i produktion: Observabilitet & evaluering

[![AI Agents in Production](../../../translated_images/da/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Når AI-agenter bevæger sig fra eksperimentelle prototyper til virkelige anvendelser, bliver evnen til at forstå deres adfærd, overvåge deres ydeevne og systematisk evaluere deres output vigtig.

## Læringsmål

Efter at have gennemført denne lektion vil du vide, hvordan du/forstå:
- Kernebegreber for agent-observabilitet og evaluering
- Teknikker til at forbedre agenters ydeevne, omkostninger og effektivitet
- Hvad og hvordan du systematisk evaluerer dine AI-agenter
- Hvordan du kontrollerer omkostninger ved udrulning af AI-agenter i produktion
- Hvordan du instrumenterer agenter bygget med Microsoft Agent Framework

Målet er at udstyre dig med viden til at omdanne dine "black box"-agenter til transparente, håndterbare og pålidelige systemer.

_**Bemærk:** Det er vigtigt at udrulle AI-agenter, der er sikre og pålidelige. Se også lektionen [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Traces og Spans

Observabilitetsværktøjer som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) repræsenterer normalt agentkørsler som traces og spans.

- **Trace** repræsenterer en komplet agent-opgave fra start til slut (f.eks. håndtering af en brugerforespørgsel).
- **Spans** er individuelle trin inden for trace'en (f.eks. kald til et sprogmodel eller hentning af data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uden observabilitet kan en AI-agent føles som en "black box" - dens interne tilstand og ræsonnement er uigennemsigtigt, hvilket gør det svært at diagnosticere problemer eller optimere ydeevnen. Med observabilitet bliver agenter til "glasbokse," der tilbyder gennemsigtighed, som er afgørende for at opbygge tillid og sikre, at de fungerer som tiltænkt.

## Hvorfor observabilitet er vigtigt i produktionsmiljøer

Overgangen af AI-agenter til produktionsmiljøer introducerer en ny række udfordringer og krav. Observabilitet er ikke længere "nice-to-have" men en kritisk kapabilitet:

*   **Debugging og rodårsagsanalyser**: Når en agent fejler eller producerer et uventet resultat, giver observabilitetsværktøjer de traces, der er nødvendige for at lokalisere fejlkilden. Dette er især vigtigt i komplekse agenter, der kan involvere flere LLM-kald, værktøjsinteraktioner og betinget logik.
*   **Latency og omkostningsstyring**: AI-agenter er ofte afhængige af LLM’er og andre eksterne API’er, der faktureres pr. token eller kald. Observabilitet tillader præcis sporing af disse kald, hvilket hjælper med at identificere operationer, der er unødigt langsomme eller dyre. Dette gør det muligt for teams at optimere prompts, vælge mere effektive modeller eller redesigne arbejdsprocesser for at håndtere driftsomkostninger og sikre en god brugeroplevelse.
*   **Tillid, sikkerhed og overholdelse**: I mange anvendelser er det vigtigt at sikre, at agenter opfører sig sikkert og etisk. Observabilitet giver et revisionsspor af agenthandlinger og beslutninger. Dette kan bruges til at opdage og mindske problemer som prompt-injektion, generering af skadeligt indhold eller forkert håndtering af personligt identificerbare oplysninger (PII). For eksempel kan du gennemgå traces for at forstå, hvorfor en agent gav et bestemt svar eller brugte et specifikt værktøj.
*   **Kontinuerlige forbedringsloops**: Observabilitetsdata er fundamentet for en iterativ udviklingsproces. Ved at overvåge, hvordan agenter præsterer i virkeligheden, kan teams identificere forbedringsområder, indsamle data til finjustering af modeller og validere effekten af ændringer. Dette skaber en feedback-loop, hvor produktionsindsigter fra online evaluering informerer offline eksperimenter og forbedringer, hvilket fører til gradvist bedre agentpræstation.

## Centrale metrics at følge

For at overvåge og forstå agentadfærd bør en række metrics og signaler følges. Selvom de specifikke metrics kan variere afhængigt af agentens formål, er nogle universelt vigtige.

Her er nogle af de mest almindelige metrics, som observabilitetsværktøjer overvåger:

**Latency:** Hvor hurtigt svarer agenten? Lange ventetider påvirker brugeroplevelsen negativt. Du bør måle latency for opgaver og individuelle trin ved at spore agentkørsler. F.eks. kunne en agent, der bruger 20 sekunder på alle modelkald, accelereres ved at bruge en hurtigere model eller ved at køre modelkald parallelt.

**Omkostninger:** Hvad er udgiften pr. agentkørsel? AI-agenter afhænger af LLM-kald, der faktureres pr. token eller eksterne API’er. Hyppig brug af værktøjer eller flere prompts kan hurtigt øge omkostningerne. F.eks. hvis en agent kalder en LLM fem gange for en marginal kvalitetsforbedring, skal du vurdere, om omkostningen er berettiget, eller om du kan reducere antallet af kald eller bruge en billigere model. Real-time overvågning kan også hjælpe med at identificere uventede spidsbelastninger (fx fejl, der forårsager overdrevne API-løkker).

**Request Errors:** Hvor mange forespørgsler fejlede agenten? Dette kan inkludere API-fejl eller mislykkede værktøjskald. For at gøre din agent mere robust mod disse i produktion kan du opsætte fallback-mekanismer eller gentagelser. Fx hvis LLM-udbyder A er nede, skifter du til LLM-udbyder B som backup.

**Brugerfeedback:** Implementering af direkte brugerevalueringer giver værdifuld indsigt. Dette kan inkludere eksplicitte vurderinger (👍thumbs-up/👎down, ⭐1-5 stjerner) eller tekstkommentarer. Konsistent negativ feedback bør advare dig, da det er et tegn på, at agenten ikke fungerer som forventet.

**Implicit brugerfeedback:** Brugeradfærd giver indirekte feedback selv uden eksplicitte vurderinger. Dette kan inkludere øjeblikkelig omformulering af spørgsmål, gentagne forespørgsler eller klik på en gentag-knap. Fx hvis du ser, at brugere gentagne gange stiller det samme spørgsmål, er det et tegn på, at agenten ikke fungerer som forventet.

**Nøjagtighed:** Hvor ofte producerer agenten korrekte eller ønskværdige output? Definitionerne af nøjagtighed varierer (fx korrekt problemløsning, korrekt informationshentning, brugertilfredshed). Det første skridt er at definere, hvad succes ser ud for din agent. Du kan spore nøjagtighed via automatiserede kontrolpunkter, evalueringsscore eller task completion labels. F.eks. markering af traces som "succeeded" eller "failed".

**Automatiserede evalueringsmetrics:** Du kan også opsætte automatiserede evalueringsprocesser. For eksempel kan du bruge en LLM til at bedømme agentens output, eksempelvis om det er hjælpsomt, præcist eller ej. Der findes også flere open source biblioteker, der hjælper med at score forskellige aspekter af agenten. Fx [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://llm-guard.com/) til at opdage skadelig sprogbrug eller prompt-injektion.

I praksis giver en kombination af disse metrics den bedste dækning af en AI-agents helbred. I dette kapitels [eksempel-notebook](./code_samples/10-expense_claim-demo.ipynb) vil vi vise dig, hvordan disse metrics ser ud i virkelige eksempler, men først vil vi lære, hvordan en typisk evalueringsworkflow ser ud.

## Instrumentér din agent

For at indsamle trace-data skal du instrumentere din kode. Målet er at instrumentere agentkoden til at udsende traces og metrics, som kan indfanges, processeres og visualiseres af en observabilitetsplatform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) er blevet en industristandard for LLM-observabilitet. Det tilbyder et sæt API’er, SDK’er og værktøjer til generering, indsamling og eksport af telemetridata.

Der findes mange instrumenteringsbiblioteker, der pakker eksisterende agent-rammer ind og gør det nemt at eksportere OpenTelemetry spans til et observabilitetsværktøj. Microsoft Agent Framework integrerer nativt med OpenTelemetry. Nedenfor er et eksempel på instrumentering af en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentudførelse spores automatisk
    pass
```

[Eksempel-notebook](./code_samples/10-expense_claim-demo.ipynb) i dette kapitel vil demonstrere, hvordan du instrumenterer din MAF-agent.

**Manuel span-oprettelse:** Mens instrumenteringsbiblioteker giver et godt udgangspunkt, er der ofte tilfælde, hvor mere detaljeret eller tilpasset information er nødvendig. Du kan manuelt oprette spans for at tilføje tilpasset applikationslogik. Endnu vigtigere kan de berige automatisk eller manuelt oprettede spans med tilpassede attributter (også kaldet tags eller metadata). Disse attributter kan inkludere forretningsspecifikke data, mellemregninger eller enhver kontekst, der kan være nyttig til fejlfinding eller analyse, såsom `user_id`, `session_id` eller `model_version`.

Eksempel på manuelle traces og spans med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent evaluering

Observabilitet giver os metrics, men evaluering er processen med at analysere disse data (og udføre tests) for at afgøre, hvor godt en AI-agent præsterer, og hvordan den kan forbedres. Med andre ord, når du har disse traces og metrics, hvordan bruger du dem til at vurdere agenten og træffe beslutninger?

Regelmæssig evaluering er vigtig, fordi AI-agenter ofte er ikke-deterministiske og kan udvikle sig (gennem opdateringer eller afdrift i modeladfærd) – uden evaluering ville du ikke vide, om din "smarte agent" faktisk klarer sit job godt eller om den er regresset.

Der findes to kategorier evalueringer for AI-agenter: **online evaluering** og **offline evaluering**. Begge er værdifulde, og de supplerer hinanden. Vi starter som regel med offline evaluering, da dette er det minimum nødvendige trin før udrulning af en agent.

### Offline evaluering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette involverer evaluering af agenten i et kontrolleret miljø, typisk ved hjælp af testdatasæt og ikke live brugerforespørgsler. Du bruger kuraterede datasæt, hvor du kender det forventede output eller korrekt adfærd, og kører så din agent på disse.

For eksempel, hvis du har bygget en agent til matematiske tekstopgaver, kan du have et [testdatasæt](https://huggingface.co/datasets/gsm8k) på 100 opgaver med kendte svar. Offline evaluering udføres ofte under udvikling (og kan være en del af CI/CD pipelines) for at tjekke forbedringer eller forhindre regress. Fordelen er, at det er **gentageligt, og du kan få klare nøjagtigheds-metric, da du har ground truth**. Du kan også simulere brugerforespørgsler og måle agentens svar mod ideelle svar eller bruge automatiserede metrics som beskrevet ovenfor.

Den vigtigste udfordring ved offline evaluering er at sikre, at dit testdatasæt er omfattende og forbliver relevant – agenten kan klare sig godt på et fast testdatasæt, men støde på meget forskellige forespørgsler i produktion. Derfor bør du holde testdatasæt opdaterede med nye kanttilfælde og eksempler, der afspejler virkelige scenarier. En blanding af små ”smoke test”-cases og større evalueringssæt er nyttig: små sæt til hurtige check og større til bredere præstationsmålinger.

### Online evaluering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering af agenten i et live, virkeligt miljø, altså under faktisk brug i produktion. Online evaluering involverer overvågning af agentens ydeevne på rigtige brugerinteraktioner og løbende analyse af resultater.

For eksempel kan du spore succesrater, brugertilfredsheds-score eller andre metrics på live trafik. Fordelen ved online evaluering er, at den **fanger ting, du måske ikke forventer i et laboratoriemiljø** – du kan observere model-afdrift over tid (hvis agentens effektivitet falder, mens inputmønstre ændres) og opdage uventede forespørgsler eller situationer, der ikke var i dit testdatasæt. Det giver et sandt billede af, hvordan agenten opfører sig i virkeligheden.

Online evaluering involverer ofte indsamling af implicit og eksplicit brugerfeedback, som diskuteret, og muligvis kørsel af shadow tests eller A/B tests (hvor en ny version af agenten kører parallelt for at sammenligne med den gamle). Udfordringen er, at det kan være svært at få pålidelige labels eller scores for live interaktioner – du kan være afhængig af brugerfeedback eller efterfølgende metrics (fx om brugeren klikkede på resultatet).

### Kombinere de to

Online og offline evaluering er ikke gensidigt udelukkende; de er stærkt komplementære. Indsigter fra online overvågning (fx nye typer brugerforespørgsler, hvor agenten præsterer dårligt) kan bruges til at udvide og forbedre offline testdatasæt. Omvendt kan agenter, der klarer sig godt i offline tests, derefter mere trygt udrulles og overvåges online.

Faktisk anvender mange teams en loop:

_evaluer offline -> udrul -> overvåg online -> indsamle nye fejltilfælde -> tilføj til offline datasæt -> forfin agent -> gentag_.

## Almindelige problemer

Når du ruller AI-agenter ud i produktion, kan du møde forskellige udfordringer. Her er nogle almindelige problemer og deres potentielle løsninger:

| **Problem**    | **Potentielle løsninger**   |
| ------------- | ------------------ |
| AI-agenten udfører ikke opgaver konsekvent | - Finjuster prompten givet til AI-agenten; vær klar om mål.<br>- Identificer hvor opgaver kan opdeles i delopgaver og håndteres af flere agenter. |
| AI-agent kører i kontinuerlige loops | - Sørg for klare afslutningsbetingelser, så agenten ved, hvornår processen skal stoppe.<br>- For komplekse opgaver med ræsonnering og planlægning, brug en større model, der er specialiseret til dette. |
| AI-agentens værktøjskald fungerer ikke godt | - Test og valider værktøjets output uden for agentsystemet.<br>- Finjuster definerede parametre, prompts og navngivning af værktøjer. |
| Multi-agent system præsterer ikke konsekvent | - Finjuster prompts givet til hver agent for at sikre, at de er specifikke og forskellige.<br>- Byg et hierarkisk system med en "routing" eller controller agent, der bestemmer hvilken agent, der er korrekt. |

Mange af disse problemer kan identificeres mere effektivt med observabilitet på plads. De traces og metrics, vi diskuterede tidligere, hjælper med præcist at lokalisere, hvor i agentens workflow problemer opstår, hvilket gør debugging og optimering meget mere effektiv.

## Styring af omkostninger


Her er nogle strategier til at håndtere omkostningerne ved at sætte AI-agenter i produktion:

**Brug af mindre modeller:** Små sprogmodeller (SLM'er) kan klare sig godt i visse agentbaserede brugstilfælde og vil reducere omkostningerne betydeligt. Som nævnt tidligere er det bedste at bygge et evalueringssystem til at bestemme og sammenligne ydeevnen i forhold til større modeller for at forstå, hvor godt en SLM vil klare sig i dit brugstilfælde. Overvej at bruge SLM'er til enklere opgaver som intentionsklassificering eller parameterudtrækning, mens du reserverer større modeller til kompleks ræsonnering.

**Brug af en router-model:** En lignende strategi er at bruge en mangfoldighed af modeller og størrelser. Du kan bruge en LLM/SLM eller en serverløs funktion til at rute forespørgsler baseret på kompleksitet til de bedst egnede modeller. Dette vil også hjælpe med at reducere omkostninger samtidig med, at ydeevnen sikres på de rigtige opgaver. For eksempel kan du rute simple forespørgsler til mindre, hurtigere modeller og kun bruge dyre store modeller til komplekse ræsonneringsopgaver.

**Caching af svar:** At identificere almindelige forespørgsler og opgaver og give svarene, før de går igennem dit agentbaserede system, er en god måde at reducere mængden af lignende forespørgsler på. Du kan endda implementere en flow til at identificere, hvor ens en forespørgsel er i forhold til dine cachede forespørgsler ved hjælp af mere simple AI-modeller. Denne strategi kan betydeligt reducere omkostningerne for ofte stillede spørgsmål eller almindelige arbejdsgange.

## Lad os se, hvordan dette fungerer i praksis

I [eksempelnotsbogen for dette afsnit](./code_samples/10-expense_claim-demo.ipynb) vil vi se eksempler på, hvordan vi kan bruge overvågningsværktøjer til at monitorere og evaluere vores agent.


### Har du flere spørgsmål om AI-agenter i produktion?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Forrige lektion

[Metakognition Designmønster](../09-metacognition/README.md)

## Næste lektion

[Agentbaserede protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->