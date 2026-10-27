# AI-agenter i produktion: Observerbarhed og evaluering

[![AI Agents in Production](../../../translated_images/da/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Når AI-agenter går fra eksperimentelle prototyper til virkelige anvendelser, bliver evnen til at forstå deres adfærd, overvåge deres ydeevne og systematisk evaluere deres output vigtig.

## Læringsmål

Efter at have gennemført denne lektion, vil du vide hvordan/forstå:
- Kernekoncepter for agent-observerbarhed og evaluering
- Teknikker til forbedring af agenters ydeevne, omkostninger og effektivitet
- Hvad og hvordan du systematisk evaluerer dine AI-agenter
- Hvordan du kontrollerer omkostninger ved udrulning af AI-agenter i produktion
- Hvordan man instrumenterer agenter bygget med Microsoft Agent Framework

Målet er at give dig den viden, der skal til for at omdanne dine "black box"-agenter til gennemsigtige, håndterbare og pålidelige systemer.

_**Bemærk:** Det er vigtigt at udrulle AI-agenter, der er sikre og pålidelige. Se også lektionen [Bygning af pålidelige AI-agenter](../06-building-trustworthy-agents/README.md)._

## Traces og Spans

Observerbarhedsværktøjer som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) repræsenterer normalt agentkørsler som traces og spans.

- **Trace** repræsenterer en komplet agentopgave fra start til slut (som at håndtere en brugerforespørgsel).
- **Spans** er individuelle trin inden for trace (som at kalde et sprogsmodel eller hente data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uden observerbarhed kan en AI-agent føles som en "black box" - dens interne tilstand og ræsonnement er uklart, hvilket gør det svært at diagnosticere problemer eller optimere ydeevne. Med observerbarhed bliver agenter til "glasbokse," der tilbyder gennemsigtighed, som er afgørende for at opbygge tillid og sikre, at de fungerer som forventet.

## Hvorfor observerbarhed er vigtig i produktionsmiljøer

Overgangen af AI-agenter til produktionsmiljøer introducerer en ny række udfordringer og krav. Observerbarhed er ikke længere et "nice-to-have" men en kritisk evne:

*   **Debugging og rodårsagsanalyser**: Når en agent fejler eller producerer uventet output, giver observerbarhedsværktøjer traces, der er nødvendige for at finde fejlkilden. Dette er især vigtigt i komplekse agenter, der kan involvere flere LLM-kald, værktøjsinteraktioner og betinget logik.
*   **Latens og omkostningsstyring**: AI-agenter bruger ofte LLM'er og andre eksterne API'er, der faktureres pr. token eller pr. kald. Observerbarhed gør det muligt præcist at spore disse kald, hvilket hjælper med at identificere operationer, der er unødigt langsomme eller dyre. Dette gør det muligt for teams at optimere prompts, vælge mere effektive modeller eller redesigne arbejdsgange for at håndtere driftsomkostninger og sikre en god brugeroplevelse.
*   **Tillid, sikkerhed og compliance**: I mange anvendelser er det vigtigt at sikre, at agenter opfører sig sikkert og etisk korrekt. Observerbarhed giver et revisionsspor af agentens handlinger og beslutninger. Dette kan bruges til at opdage og afbøde problemer som prompt-injektion, generering af skadeligt indhold eller ukorrekt håndtering af personhenførbare oplysninger (PII). For eksempel kan du gennemgå traces for at forstå, hvorfor en agent gav et bestemt svar eller brugte et specifikt værktøj.
*   **Kontinuerlige forbedringssløjfer**: Observerbarhedsdata danner grundlaget for en iterativ udviklingsproces. Ved at overvåge, hvordan agenter præsterer i den virkelige verden, kan teams identificere forbedringsområder, indsamle data til finjustering af modeller og validere effekten af ændringer. Dette skaber en feedbacksløjfe, hvor produktionsindsigter fra online-evaluering informerer offline-eksperimenter og -forbedringer, hvilket fører til gradvist bedre agentpræstationer.

## Nøglemetrikker at spore

For at overvåge og forstå agentadfærd bør en række metrikker og signaler spores. Selvom specifikke metrikker kan variere baseret på agentens formål, er nogle universelt vigtige.

Her er nogle af de mest almindelige metrikker, som observerbarhedsværktøjer monitorerer:

**Latens:** Hvor hurtigt svarer agenten? Lange ventetider påvirker brugeroplevelsen negativt. Du bør måle latens for opgaver og individuelle trin ved at spore agentkørsler. For eksempel kan en agent, der tager 20 sekunder for alle modelkald, accelereres ved at bruge en hurtigere model eller ved at køre modelkald parallelt.

**Omkostninger:** Hvad er udgiften pr. agentkørsel? AI-agenter er afhængige af LLM-kald, der faktureres pr. token eller eksterne API'er. Hyppig værktøjsbrug eller flere prompts kan hurtigt øge omkostningerne. For eksempel, hvis en agent kalder en LLM fem gange for en marginal kvalitetforbedring, skal du vurdere, om omkostningen er berettiget, eller om du kan reducere antallet af kald eller bruge en billigere model. Realtidsovervågning kan også hjælpe med at identificere uventede spidsbelastninger (fx fejl som forårsager overdrevne API-løkker).

**Forespørgselsfejl:** Hvor mange forespørgsler fejlede agenten i? Dette kan inkludere API-fejl eller mislykkede værktøjskald. For at gøre din agent mere robust mod disse fejl i produktion kan du opsætte fallback-mekanismer eller genforsøg. Fx hvis LLM-udbyder A er nede, skifter du til LLM-udbyder B som backup.

**Brugerfeedback:** Implementering af direkte bruger-evalueringer giver værdifuld indsigt. Dette kan inkludere eksplicitte vurderinger (👍tommel-op/👎ned, ⭐1-5 stjerner) eller skriftlige kommentarer. Konsistent negativ feedback bør advare dig, da det er et tegn på, at agenten ikke fungerer som forventet.

**Implicit brugerfeedback:** Brugeradfærd giver indirekte feedback selv uden eksplicitte vurderinger. Dette kan inkludere øjeblikkelig omformulering af spørgsmål, gentagne forespørgsler eller klik på en retry-knap. Fx hvis du ser, at brugere gentagne gange stiller det samme spørgsmål, er det et tegn på, at agenten ikke fungerer som forventet.

**Nøjagtighed:** Hvor ofte producerer agenten korrekte eller ønskelige output? Definitionerne af nøjagtighed varierer (fx korrekt løsning af problemløsning, præcision ved informationshentning, brugertilfredshed). Det første skridt er at definere, hvad succes ser ud for din agent. Du kan spore nøjagtighed via automatiserede tjek, evalueringsscorer eller opgavefuldførelseslabels. For eksempel at markere traces som "success" eller "failed".

**Automatiserede evalueringsmetrikker:** Du kan også opsætte automatiserede evalueringsrutiner. For eksempel kan du bruge en LLM til at score agentens output, fx om det er hjælpsomt, nøjagtigt eller ej. Der findes også flere open source-biblioteker, som hjælper dig med at vurdere forskellige aspekter af agenten. Fx [RAGAS](https://docs.ragas.io/) til RAG-agenter eller [LLM Guard](https://github.com/protectai/llm-guard) til at opdage skadeligt sprogbrug eller prompt-injektion.

I praksis giver en kombination af disse metrikker den bedste dækning af AI-agentens helbredstilstand. I dette kapitels [eksempelnote bog](./code_samples/10-expense_claim-demo.ipynb) viser vi dig, hvordan disse metrikker ser ud i virkelige eksempler, men først lærer vi, hvordan en typisk evalueringsarbejdsgang ser ud.

## Instrumenter din agent

For at indsamle tracedata skal du instrumentere din kode. Målet er at instrumentere agentkoden til at udsende traces og metrikker, som kan opfanges, behandles og visualiseres af en observerbarhedsplatform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) er blevet en industristandard for LLM-observerbarhed. Det tilbyder et sæt API'er, SDK'er og værktøjer til generering, indsamling og eksport af telemetridata.

Der findes mange instrumenteringsbiblioteker, som pakker eksisterende agentrammer ind og gør det nemt at eksportere OpenTelemetry-spans til et observerbarhedsværktøj. Microsoft Agent Framework integrerer nativeret med OpenTelemetry. Nedenfor er et eksempel på instrumentering af en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

Eksempelnote bogen [eksempelnote bog](./code_samples/10-expense_claim-demo.ipynb) i dette kapitel demonstrerer, hvordan du instrumenterer din MAF-agent.

**Manuel Span-oprettelse:** Selvom instrumenteringsbiblioteker giver en god basislinje, er der ofte tilfælde, hvor mere detaljeret eller tilpasset information er nødvendig. Du kan manuelt oprette spans for at tilføje brugerdefineret applikationslogik. Endnu vigtigere er, at de kan berige automatisk eller manuelt oprettede spans med brugerdefinerede attributter (også kendt som tags eller metadata). Disse attributter kan inkludere forretningsspecifikke data, mellemregninger eller enhver kontekst, der kan være nyttig til debugging eller analyse, såsom `user_id`, `session_id` eller `model_version`.

Eksempel på manuel oprettelse af traces og spans med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent-evaluering

Observerbarhed giver os metrikker, men evaluering er processen med at analysere disse data (og udføre tests) for at vurdere, hvor godt en AI-agent præsterer, og hvordan den kan forbedres. Med andre ord, når du har disse traces og metrikker, hvordan bruger du dem så til at bedømme agenten og træffe beslutninger?

Regelmæssig evaluering er vigtig, fordi AI-agenter ofte er ikke-deterministiske og kan udvikle sig (gennem opdateringer eller ændret modeladfærd) – uden evaluering ville du ikke vide, om din "smarte agent" faktisk udfører sit job godt, eller om den er regressiv.

Der findes to kategorier af evalueringer for AI-agenter: **online evaluering** og **offline evaluering**. Begge er værdifulde, og de supplerer hinanden. Vi begynder normalt med offline evaluering, da det er det minimale nødvendige trin, før man implementerer en agent.

### Offline evaluering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette involverer evaluering af agenten i et kontrolleret miljø, typisk med testdatasæt, ikke levende brugerforespørgsler. Du bruger kuraterede datasæt, hvor du kender det forventede output eller korrekt adfærd, og kører derefter agenten på disse.

For eksempel, hvis du har bygget en matematikordproblem-agent, kan du have et [testdatasæt](https://huggingface.co/datasets/openai/gsm8k) med 100 problemer med kendte svar. Offline evaluering udføres ofte under udvikling (og kan være en del af CI/CD pipelines) for at tjekke forbedringer eller beskytte mod regressionsfejl. Fordelen er, at det er **gentageligt, og du kan få klare nøjagtighedsmetrikker, fordi du har sandheden**. Du kan også simulere brugerforespørgsler og måle agentens svar mod ideelle svar eller bruge automatiserede metrikker som beskrevet ovenfor.

Den væsentlige udfordring ved offline evaluering er at sikre, at dit testdatasæt er omfattende og forbliver relevant – agenten kan klare sig godt på et fast testset, men møde meget forskellige forespørgsler i produktion. Derfor bør du holde testdatasæt opdateret med nye kanttilfælde og eksempler, der afspejler virkelige scenarier. En blanding af små "smoke-test" cases og større evalueringssæt er nyttig: små sæt til hurtige tjek og større til bredere præstationsmetrikker.

### Online evaluering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering af agenten i et live, virkeligt miljø, altså under faktisk brug i produktion. Online evaluering involverer overvågning af agentens ydeevne på rigtige brugerinteraktioner og kontinuerlig analyse af resultater.

For eksempel kan du spore succesrater, brugertilfredsheds-score eller andre metrikker på live trafik. Fordelen ved online evaluering er, at det **fanger ting, du måske ikke forudså i laboratorieindstillinger** – du kan observere modeldrift over tid (hvis agentens effektivitet forringes, efterhånden som inputmønstre ændrer sig) og opdage uventede forespørgsler eller situationer, som ikke var i dit testdatasæt. Det giver et ægte billede af, hvordan agenten opfører sig i felten.

Online evaluering involverer ofte indsamling af implicit og eksplicit brugerfeedback, som drøftet, og eventuelt kørsel af shadow tests eller A/B tests (hvor en ny version af agenten kører parallelt for at sammenligne med den gamle). Udfordringen er, at det kan være vanskeligt at få pålidelige labels eller scores for live-interaktioner – du må måske stole på brugerfeedback eller downstream-metrikker (fx om brugeren klikkede på resultatet).

### Kombinere de to

Online og offline evaluering er ikke gensidigt udelukkende; de supplerer hinanden meget. Indsigter fra online overvågning (fx nye typer brugerforespørgsler, hvor agenten præsterer dårligt) kan bruges til at udvide og forbedre offline testdatasæt. Omvendt kan agenter, der klarer sig godt i offline tests, efterfølgende implementeres med større tillid og overvåges online.

Faktisk anvender mange teams en sløjfe:

_evaluer offline -> deployer -> overvåg online -> indsamle nye fejltilfælde -> tilføj til offline datasæt -> forfin agent -> gentag_.

## Almindelige problemer

Når du udruller AI-agenter i produktion, kan du støde på forskellige udfordringer. Her er nogle almindelige problemer og deres mulige løsninger:

| **Problem**    | **Mulig løsning**   |
| ------------- | ------------------ |
| AI-agenten udfører ikke opgaver konsekvent | - Forfin prompten til AI-agenten; vær klar i dine mål.<br>- Identificer, hvor opdeling af opgaver i delopgaver og håndtering ved flere agenter kan hjælpe. |
| AI-agenten kører i kontinuerlige løkker | - Sørg for klare afslutningsbetingelser, så agenten ved, hvornår processen skal stoppes.<br>- For komplekse opgaver, der kræver ræsonnement og planlægning, brug en større model, der er specialiseret til ræsonneringsopgaver. |
| AI-agentens værktøjskald fungerer ikke godt | - Test og valider værktøjets output uden for agentsystemet.<br>- Forfin de definerede parametre, prompts og navngivning af værktøjer. |
| Multi-agent system præsterer ikke konsekvent | - Forfin prompts til hver enkelt agent for at sikre, at de er specifikke og adskiller sig fra hinanden.<br>- Byg et hierarkisk system med en "routing" eller controller-agent, der bestemmer, hvilken agent der er den korrekte. |

Mange af disse problemer kan identificeres mere effektivt med observerbarhed på plads. De traces og metrikker, vi diskuterede tidligere, hjælper med at præcisere, præcis hvor i agentens arbejdsgang problemer opstår, hvilket gør debugging og optimering langt mere effektivt.

## Omkostningsstyring

Her er nogle strategier til at styre omkostningerne ved udrulning af AI-agenter i produktion:

**Brug af mindre modeller:** Små sprogmodeller (SLM'er) kan klare sig godt i visse agentiske anvendelsessituationer og vil reducere omkostningerne betydeligt. Som nævnt tidligere er det bedste måde at forstå, hvor godt en SLM vil klare sig i din brugssag, at opbygge et evalueringssystem til at bestemme og sammenligne ydeevnen mod større modeller. Overvej at bruge SLM'er til enklere opgaver som hensigtsklassifikation eller parameterudtrækning, mens større modeller reserveres til kompleks ræsonnering.

**Brug af en routermodel:** En lignende strategi er at anvende en mangfoldighed af modeller og størrelser. Du kan bruge en LLM/SLM eller serverløs funktion til at dirigere forespørgsler baseret på kompleksitet til de bedst egnede modeller. Dette vil også hjælpe med at reducere omkostninger samtidig med at sikre ydeevne på de rette opgaver. For eksempel, diriger simple forespørgsler til mindre, hurtigere modeller, og brug kun dyre store modeller til komplekse ræsonneringsopgaver.

**Caching af svar:** Identificering af almindelige forespørgsler og opgaver og fremlæggelse af svarene, før de går gennem dit agentiske system, er en god måde at reducere mængden af lignende forespørgsler. Du kan endda implementere en proces til at identificere, hvor ens en forespørgsel er i forhold til dine cachede forespørgsler ved hjælp af mere grundlæggende AI-modeller. Denne strategi kan markant reducere omkostningerne for ofte stillede spørgsmål eller almindelige arbejdsgange.

## Lad os se, hvordan det virker i praksis

I [eksempelnottet i denne sektion](./code_samples/10-expense_claim-demo.ipynb) vil vi se eksempler på, hvordan vi kan bruge observeringsværktøjer til at overvåge og evaluere vores agent.


### Har du flere spørgsmål om AI-agenter i produktion?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i åbne kontortimer og få svar på dine spørgsmål om AI-agenter.

## Forrige lektion

[Metakognitionsdesignmønster](../09-metacognition/README.md)

## Næste lektion

[Agentiske protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->