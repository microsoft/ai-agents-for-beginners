# AI-agenter i produktion: Observabilitet & evaluering

[![AI-agenter i produktion](../../../translated_images/da/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Efterhånden som AI-agenter bevæger sig fra eksperimentelle prototyper til virkelige applikationer, bliver evnen til at forstå deres adfærd, overvåge deres ydeevne og systematisk evaluere deres output vigtig.

## Læringsmål

Efter at have gennemført denne lektion vil du vide hvordan/forstå:
- Kernebegreber inden for agent-observabilitet og evaluering
- Teknikker til at forbedre agenters ydeevne, omkostninger og effektivitet
- Hvad og hvordan du systematisk evaluerer dine AI-agenter
- Hvordan du kontrollerer omkostninger ved at udrulle AI-agenter i produktion
- Hvordan du instrumenterer agenter bygget med Microsoft Agent Framework

Målet er at give dig viden til at forvandle dine "black box"-agenter til gennemsigtige, håndterbare og pålidelige systemer.

_**Bemærk:** Det er vigtigt at udrulle AI-agenter, der er sikre og troværdige. Tjek også lektionen [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Observabilitetsværktøjer såsom [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) repræsenterer typisk agentkørsler som traces og spans.

- **Trace** repræsenterer en komplet agentopgave fra start til slut (som at håndtere en brugerforespørgsel).
- **Spans** er individuelle trin inden for trace'et (som at kalde en sprogmodel eller hente data).

![Trace-træ i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uden observabilitet kan en AI-agent føles som en "black box" - dens interne tilstand og ræsonnement er uigennemsigtige, hvilket gør det svært at diagnosticere problemer eller optimere ydeevnen. Med observabilitet bliver agenter til "glasbokse", der tilbyder gennemsigtighed, hvilket er afgørende for at opbygge tillid og sikre, at de fungerer som tiltænkt. 

## Hvorfor observabilitet er vigtig i produktionsmiljøer

At overføre AI-agenter til produktionsmiljøer introducerer et nyt sæt udfordringer og krav. Observabilitet er ikke længere noget "rart at have", men en kritisk kapabilitet:

*   **Fejlfinding og årsagsanalyse**: Når en agent fejler eller producerer et uventet output, giver observabilitetsværktøjer de traces, der er nødvendige for at fastslå fejlkilden. Dette er især vigtigt i komplekse agenter, der kan involvere flere LLM-kald, værktøjsinteraktioner og betinget logik.
*   **Latency og omkostningsstyring**: AI-agenter er ofte afhængige af LLM'er og andre eksterne API'er, der faktureres per token eller per kald. Observabilitet tillader præcis sporing af disse kald, hvilket hjælper med at identificere operationer, der er urimeligt langsomme eller dyre. Dette gør det muligt for teams at optimere prompts, vælge mere effektive modeller eller redesigne arbejdsflow for at styre driftsomkostninger og sikre en god brugeroplevelse.
*   **Troværdighed, sikkerhed og compliance**: I mange anvendelser er det vigtigt at sikre, at agenter opfører sig sikkert og etisk. Observabilitet giver et revisionsspor af agentens handlinger og beslutninger. Dette kan bruges til at opdage og afbøde problemer som prompt-injektion, generering af skadeligt indhold eller forkert håndtering af personligt identificerbare oplysninger (PII). For eksempel kan du gennemgå traces for at forstå, hvorfor en agent gav et bestemt svar eller brugte et bestemt værktøj.
*   **Kontinuerlige forbedringssløjfer**: Observabilitetsdata er fundamentet for en iterativ udviklingsproces. Ved at overvåge, hvordan agenter præsterer i den virkelige verden, kan teams identificere forbedringsområder, indsamle data til finjustering af modeller og validere effekten af ændringer. Dette skaber en feedbacksløjfe, hvor produktionsindsigter fra online-evaluering informerer offline-eksperimenter og forfining, hvilket fører til gradvist bedre agentperformance.

## Vigtige metrikker at spore

For at overvåge og forstå agentadfærd bør en række metrikker og signaler spores. Selvom de specifikke metrikker kan variere afhængigt af agentens formål, er nogle universelt vigtige.

Her er nogle af de mest almindelige metrikker, som observabilitetsværktøjer overvåger:

**Latency:** Hvor hurtigt svarer agenten? Lange ventetider påvirker brugeroplevelsen negativt. Du bør måle latenstid for opgaver og individuelle trin ved at trace agentkørsler. For eksempel kan en agent, der bruger 20 sekunder på alle modelkald, accelereres ved at bruge en hurtigere model eller ved at køre modelkald parallelt.

**Costs:** Hvad er udgiften per agentkørsel? AI-agenter er afhængige af LLM-kald, der faktureres per token, eller eksterne API'er. Hyppig brug af værktøjer eller flere prompts kan hurtigt øge omkostningerne. For eksempel, hvis en agent kalder en LLM fem gange for en marginal kvalitetsforbedring, skal du vurdere, om omkostningen er berettiget, eller om du kan reducere antallet af kald eller bruge en billigere model. Realtidsmonitorering kan også hjælpe med at identificere uventede spidser (fx bugs, der forårsager overdrevne API-løkker).

**Request Errors:** Hvor mange forespørgsler fejlede agenten på? Dette kan inkludere API-fejl eller fejlede værktøjskald. For at gøre din agent mere robust i produktion kan du sætte fallback-mekanismer eller retries op. Fx hvis LLM-udbyder A er nede, kan du skifte til LLM-udbyder B som backup.

**User Feedback:** Implementering af direkte brugerevalueringer giver værdifuld indsigt. Dette kan inkludere eksplicitte vurderinger (👍thumbs-up/👎down, ⭐1-5 stjerner) eller tekstuelle kommentarer. Konsistent negativ feedback bør advare dig, da det er et tegn på, at agenten ikke fungerer som forventet. 

**Implicit User Feedback:** Brugeradfærd giver indirekte feedback selv uden eksplicitte vurderinger. Dette kan inkludere øjeblikkelig omformulering af spørgsmål, gentagne forespørgsler eller klik på en retry-knap. Fx hvis du ser, at brugere gentagne gange stiller det samme spørgsmål, er det et tegn på, at agenten ikke fungerer som forventet.

**Accuracy:** Hvor ofte producerer agenten korrekte eller ønskelige output? Definitionen af nøjagtighed varierer (fx korrekt løsning af problemer, informations-hentningens nøjagtighed, brugertilfredshed). Det første skridt er at definere, hvordan succes ser ud for din agent. Du kan spore nøjagtighed via automatiserede checks, evalueringsscorer eller opgavefuldførelsesetiketter. For eksempel ved at markere traces som "succeeded" eller "failed". 

**Automated Evaluation Metrics:** Du kan også opsætte automatiserede evalueringer. For eksempel kan du bruge en LLM til at score agentens output, fx om det er nyttigt, nøjagtigt eller ej. Der findes også flere open source-biblioteker, der hjælper med at score forskellige aspekter af agenten. Fx [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://llm-guard.com/) til at detektere skadeligt sprog eller prompt-injektion. 

I praksis giver en kombination af disse metrikker den bedste dækning af en AI-agents sundhed. I dette kapitels [eksempel-notebook](./code_samples/10-expense_claim-demo.ipynb) viser vi, hvordan disse metrikker ser ud i virkelige eksempler, men først lærer vi, hvordan en typisk evalueringsworkflow ser ud.

## Instrumentér din agent

For at indsamle tracing-data skal du instrumentere din kode. Målet er at instrumentere agentkoden til at udsende traces og metrikker, som kan indfanges, behandles og visualiseres af en observabilitetsplatform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) er blevet en industristandard for LLM-observabilitet. Det tilbyder et sæt APIs, SDK'er og værktøjer til at generere, indsamle og eksportere telemetridata. 

Der findes mange instrumenteringsbiblioteker, der omslutter eksisterende agentframeworks og gør det nemt at eksportere OpenTelemetry-spans til et observabilitetsværktøj. Microsoft Agent Framework integrerer med OpenTelemetry naturligt. Nedenfor er et eksempel på at instrumentere en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentens udførelse spores automatisk
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Manuel span-oprettelse:** Mens instrumenteringsbiblioteker giver et godt udgangspunkt, er der ofte tilfælde, hvor mere detaljeret eller tilpasset information er nødvendig. Du kan manuelt oprette spans for at tilføje brugerdefineret applikationslogik. Endnu vigtigere kan de berige automatisk eller manuelt oprettede spans med brugerdefinerede attributter (også kendt som tags eller metadata). Disse attributter kan inkludere forretningsspecifikke data, mellemregninger eller enhver kontekst, der kan være nyttig til fejlfinding eller analyse, såsom `user_id`, `session_id`, eller `model_version`.

Eksempel på at oprette traces og spans manuelt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent-evaluering

Observabilitet giver os metrikker, men evaluering er processen med at analysere disse data (og udføre tests) for at bestemme, hvor godt en AI-agent præsterer, og hvordan den kan forbedres. Med andre ord, når du har de traces og metrikker, hvordan bruger du dem så til at vurdere agenten og træffe beslutninger? 

Regelmæssig evaluering er vigtig, fordi AI-agenter ofte er ikke-deterministiske og kan udvikle sig (gennem opdateringer eller driftningsadfærd) – uden evaluering ville du ikke vide, om din "smarte agent" faktisk udfører sit arbejde godt eller om den er regresset.

Der er to kategorier af evalueringer for AI-agenter: **online-evaluering** og **offline-evaluering**. Begge er værdifulde, og de supplerer hinanden. Vi begynder normalt med offline-evaluering, da dette er det minimale nødvendige skridt inden udrulning af en agent.

### Offline-evaluering

![Datasæt-elementer i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette indebærer at evaluere agenten i et kontrolleret miljø, typisk ved brug af testdatasæt, ikke live brugerforespørgsler. Du bruger kuraterede datasæt, hvor du kender det forventede output eller korrekt opførsel, og kører derefter din agent på disse. 

For eksempel, hvis du har bygget en agent til matematik-opgaver, kan du have et [testdatasæt](https://huggingface.co/datasets/gsm8k) på 100 problemer med kendte svar. Offline-evaluering udføres ofte under udvikling (og kan være en del af CI/CD-pipelines) for at tjekke forbedringer eller beskytte imod regressioner. Fordelen er, at det er **gentageligt, og du kan få klare nøjagtighedsmetrikker, da du har ground truth**. Du kan også simulere brugerforespørgsler og måle agentens svar mod ideelle svar eller bruge automatiserede metrikker som beskrevet ovenfor. 

Den centrale udfordring med offline-eval er at sikre, at dit testdatasæt er dækkende og forbliver relevant – agenten kan klare sig godt på et fast testsæt, men møde meget forskellige forespørgsler i produktion. Derfor bør du holde testsæt opdaterede med nye edge cases og eksempler, der afspejler virkelige scenarier. En blanding af små "smoke test"-cases og større evalueringssæt er nyttig: små sæt til hurtige checks og større sæt til bredere performancemålinger.

### Online-evaluering 

![Oversigt over observabilitetsmetrikker](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette henviser til at evaluere agenten i et live, virkeligt miljø, dvs. under faktisk brug i produktion. Online-evaluering involverer overvågning af agentens ydeevne på rigtige brugerinteraktioner og kontinuerlig analyse af resultater. 

For eksempel kan du spore succesrater, brugertilfredshedsscorer eller andre metrikker på live-trafik. Fordelen ved online-evaluering er, at det **fanger ting, du måske ikke forudser i et laboratoriemiljø** – du kan observere modeldrift over tid (hvis agentens effektivitet forringes, efterhånden som inputmønstre ændrer sig) og fange uventede forespørgsler eller situationer, der ikke var i dit testdata. Det giver et ægte billede af, hvordan agenten opfører sig i felten. 

Online-evaluering involverer ofte indsamling af implicit og eksplicit brugerfeedback, som diskuteret, og eventuelt kørsel af shadow-tests eller A/B-tests (hvor en ny version af agenten kører parallelt for at sammenligne med den gamle). Udfordringen er, at det kan være svært at få pålidelige labels eller scores for live-interaktioner – du kan være afhængig af brugerfeedback eller downstream-metrikker (fx om brugeren klikkede på resultatet). 

### Kombination af de to

Online- og offline-evaluering er ikke gensidigt udelukkende; de supplerer hinanden stærkt. Indsigter fra online-overvågning (fx nye typer brugerforespørgsler, hvor agenten klarer sig dårligt) kan bruges til at udvide og forbedre offline-testsæt. Omvendt kan agenter, der klarer sig godt i offline-test, derefter blive mere trygt udrullet og overvåget online. 

Faktisk adopterer mange teams en sløjfe: 

_evaluer offline -> implementér -> overvåg online -> indsamle nye fejltilfælde -> tilføj til offline-datasæt -> forfin agent -> gentag_.

## Almindelige problemer

Når du udruller AI-agenter i produktion, kan du støde på forskellige udfordringer. Her er nogle almindelige problemer og deres potentielle løsninger:

| **Problem**    | **Potentiel løsning**   |
| ------------- | ------------------ |
| AI-agenten udfører ikke opgaver konsekvent | - Forfin prompten, der gives til AI-agenten; vær klar omkring målene.<br>- Identificer, hvor opdeling af opgaver i delopgaver og håndtering af dem af flere agenter kan hjælpe. |
| AI-agenten havner i kontinuerlige løkker  | - Sørg for, at du har klare termineringsbetingelser, så agenten ved, hvornår den skal stoppe processen.<br>- For komplekse opgaver, der kræver ræsonnement og planlægning, brug en større model, der er specialiseret i ræsonnement. |
| AI-agentens værktøjskald fungerer ikke godt   | - Test og valider værktøjets output uden for agentsystemet.<br>- Forfin de definerede parametre, prompts og navngivning af værktøjer.  |
| Fleragent-systemet fungerer ikke konsekvent | - Forfin prompts givet til hver agent for at sikre, at de er specifikke og adskilte fra hinanden.<br>- Byg et hierarkisk system ved hjælp af en "routing" eller controller-agent for at afgøre, hvilken agent der er den korrekte. |

Mange af disse problemer kan identificeres mere effektivt med observabilitet på plads. De traces og metrikker, vi diskuterede tidligere, hjælper med nøjagtigt at pege på, hvor i agent-workflowet problemer opstår, hvilket gør fejlfinding og optimering meget mere effektiv.

## Håndtering af omkostninger
Her er nogle strategier til at håndtere omkostningerne ved at implementere AI-agenter i produktion:

**Brug af mindre modeller:** Små sprogmodeller (SLMs) kan præstere godt i visse agentbaserede anvendelsestilfælde og vil reducere omkostningerne væsentligt. Som nævnt tidligere er det bedste at bygge et evalueringssystem til at bestemme og sammenligne ydeevnen i forhold til større modeller for at forstå, hvor godt en SLM vil klare sig i dit anvendelsestilfælde. Overvej at bruge SLMs til enklere opgaver som intentionklassificering eller parameterudtrækning, mens du reserverer større modeller til kompleks ræsonnering.

**Brug af en routingmodel:** En lignende strategi er at bruge en mangfoldighed af modeller og størrelser. Du kan bruge en LLM/SLM eller en serverløs funktion til at dirigere forespørgsler baseret på kompleksitet til de bedst egnede modeller. Dette vil også hjælpe med at reducere omkostninger samtidig med at sikre ydeevne på de rette opgaver. For eksempel, rout enkle forespørgsler til mindre, hurtigere modeller, og brug kun dyre, store modeller til komplekse ræsonneringsopgaver.

**Caching svar:** At identificere almindelige forespørgsler og opgaver og levere svarene, før de går gennem dit agentbaserede system, er en god måde at reducere mængden af lignende forespørgsler på. Du kan endda implementere et flow til at identificere, hvor ens en forespørgsel er i forhold til dine cachede forespørgsler ved hjælp af mere basale AI-modeller. Denne strategi kan betydeligt reducere omkostningerne for ofte stillede spørgsmål eller almindelige arbejdsgange.

## Lad os se, hvordan dette fungerer i praksis

I [example notebook of this section](./code_samples/10-expense_claim-demo.ipynb) vil vi se eksempler på, hvordan vi kan bruge værktøjer til overvågning og evaluering af vores agent.

### Har du flere spørgsmål om AI-agenter i produktion?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Forrige lektion

[Designmønster for metakognition](../09-metacognition/README.md)

## Næste lektion

[Agentiske protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten Co-op Translator (https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, skal du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales en professionel, menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->