# AI-agenter i produktion: Observabilitet & evaluering

[![AI-agenter i produktion](../../../translated_images/da/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Efterhånden som AI-agenter bevæger sig fra eksperimentelle prototyper til virkelige anvendelser, bliver evnen til at forstå deres adfærd, overvåge deres ydeevne og systematisk evaluere deres output vigtig.

## Læringsmål

Efter at have gennemført denne lektion vil du vide hvordan/forstå:
- Grundlæggende koncepter inden for agent-observabilitet og evaluering
- Teknikker til forbedring af agenters ydeevne, omkostninger og effektivitet
- Hvad og hvordan du systematisk evaluerer dine AI-agenter
- Hvordan du styrer omkostninger ved udrulning af AI-agenter i produktion
- Hvordan du instrumenterer agenter bygget med Microsoft Agent Framework

Målet er at udstyre dig med den viden, der skal til for at omdanne dine "black box"-agenter til gennemskuelige, håndterbare og pålidelige systemer.

_**Bemærk:** Det er vigtigt at udrulle AI-agenter, der er sikre og troværdige. Se også lektionen [Opbygning af troværdige AI-agenter](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Observabilitetsværktøjer såsom [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) repræsenterer normalt agentkørsler som traces og spans.

- **Trace** repræsenterer en komplet agentopgave fra start til slut (som f.eks. håndtering af en brugerforespørgsel).
- **Spans** er individuelle trin inden for trace (som f.eks. kald til et sprogmodel-API eller hentning af data).

![Trace-træ i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uden observabilitet kan en AI-agent føles som en "black box" - dens interne tilstand og ræsonnement er uigennemsigtige, hvilket gør det svært at diagnosticere problemer eller optimere ydeevnen. Med observabilitet bliver agenterne til "glass boxes", der tilbyder gennemsigtighed, hvilket er afgørende for at opbygge tillid og sikre, at de fungerer som forventet. 

## Hvorfor observabilitet er vigtigt i produktionsmiljøer

Overgangen af AI-agenter til produktionsmiljøer introducerer et nyt sæt udfordringer og krav. Observabilitet er ikke længere et "nice-to-have", men en kritisk kapabilitet:

*   **Debugging og root-cause-analyse**: Når en agent fejler eller producerer et uventet output, leverer observabilitetsværktøjer de traces, der er nødvendige for at identificere årsagen til fejlen. Dette er især vigtigt i komplekse agenter, der kan involvere flere LLM-kald, værktøjsinteraktioner og betinget logik.
*   **Latens- og omkostningsstyring**: AI-agenter er ofte afhængige af LLM'er og andre eksterne API'er, der faktureres per token eller per kald. Observabilitet muliggør præcis sporing af disse kald og hjælper med at identificere operationer, der er unødigt langsomme eller dyre. Dette gør det muligt for teams at optimere prompts, vælge mere effektive modeller eller redesigne arbejdsflows for at styre driftsomkostninger og sikre en god brugeroplevelse.
*   **Tillid, sikkerhed og compliance**: I mange anvendelser er det vigtigt at sikre, at agenter opfører sig sikkert og etisk. Observabilitet giver et revisionsspor af agenthandlinger og beslutninger. Dette kan bruges til at opdage og afbøde problemer som prompt-injektion, generering af skadeligt indhold eller forkert håndtering af personligt identificerbare oplysninger (PII). For eksempel kan du gennemgå traces for at forstå, hvorfor en agent gav et bestemt svar eller brugte et specifikt værktøj.
*   **Kontinuerlige forbedringssløjfer**: Observabilitetsdata er fundamentet for en iterativ udviklingsproces. Ved at overvåge, hvordan agenter præsterer i den virkelige verden, kan teams identificere forbedringsområder, indsamle data til finjustering af modeller og validere effekten af ændringer. Dette skaber en feedbacksløjfe, hvor produktionsindsigter fra online-evaluering informerer offline-eksperimenter og forfinelser, hvilket fører til gradvist bedre agentpræstation.

## Nøglemetrikker at tracke

For at overvåge og forstå agentadfærd bør en række metrikker og signaler spores. Selvom de specifikke metrikker kan variere baseret på agentens formål, er nogle universelt vigtige.

Her er nogle af de mest almindelige metrikker, som observabilitetsværktøjer overvåger:

**Latens:** Hvor hurtigt reagerer agenten? Lange ventetider påvirker brugeroplevelsen negativt. Du bør måle latens for opgaver og individuelle trin ved at trace agentkørsler. For eksempel kan en agent, der bruger 20 sekunder på alle modelkald, accelereres ved at bruge en hurtigere model eller ved at køre modelkald parallelt.

**Omkostninger:** Hvad koster en agentkørsel? AI-agenter er afhængige af LLM-kald, der faktureres per token, eller eksterne API'er. Hyppig brug af værktøjer eller multiple prompts kan hurtigt øge omkostningerne. For eksempel, hvis en agent kalder en LLM fem gange for marginal forbedring af kvaliteten, skal du vurdere, om omkostningen er berettiget, eller om du kunne reducere antallet af kald eller bruge en billigere model. Realtidsovervågning kan også hjælpe med at identificere uventede spidser (f.eks. fejl, der forårsager overdrevne API-løkker).

**Request-fejl:** Hvor mange forespørgsler fejlede agenten i? Dette kan inkludere API-fejl eller mislykkede værktøjsopkald. For at gøre din agent mere robust over for disse i produktion kan du opsætte fallback-mekanismer eller retries. F.eks. hvis LLM-udbyder A er nede, kan du skifte til LLM-udbyder B som backup.

**Brugerfeedback:** Implementering af direkte brugerevalueringer giver værdifuld indsigt. Dette kan inkludere eksplicitte ratings (👍thumbs-up/👎down, ⭐1-5 stjerner) eller tekstkommentarer. Konsistent negativ feedback bør alarmere dig, da det er et tegn på, at agenten ikke fungerer som forventet. 

**Implicit brugerfeedback:** Brugeradfærd giver indirekte feedback selv uden eksplicitte ratings. Dette kan inkludere øjeblikkelig omformulering af spørgsmål, gentagne forespørgsler eller klik på en retry-knap. F.eks. hvis du ser, at brugere gentagne gange stiller det samme spørgsmål, er det et tegn på, at agenten ikke fungerer som forventet.

**Nøjagtighed:** Hvor ofte producerer agenten korrekte eller ønskværdige outputs? Definitionen af nøjagtighed varierer (f.eks. korrekt problemløsning, nøjagtighed af informationssøgning, brugertilfredshed). Det første skridt er at definere, hvad succes ser ud som for din agent. Du kan spore nøjagtighed via automatiserede checks, evalueringsscore eller opgaveafslutningsmærkater. For eksempel at markere traces som "succeeded" eller "failed". 

**Automatiserede evalueringsmetrikker:** Du kan også opsætte automatiserede evalueringer. For eksempel kan du bruge en LLM til at score agentens output, fx om det er hjælpsomt eller korrekt. Der findes også flere open source-biblioteker, der hjælper med at score forskellige aspekter af agenten, f.eks. [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://llm-guard.com/) til at opdage skadeligt sprog eller prompt-injektion. 

I praksis giver en kombination af disse metrikker den bedste dækning af en AI-agents helbred. I dette kapitels [eksempel-notebook](./code_samples/10-expense_claim-demo.ipynb) vil vi vise, hvordan disse metrikker ser ud i virkelige eksempler, men først lærer vi, hvordan en typisk evalueringsworkflow ser ud.

## Instrumenter din agent

For at indsamle tracing-data skal du instrumentere din kode. Målet er at instrumentere agentkoden til at udsende traces og metrikker, som kan indfanges, behandles og visualiseres af en observabilitetsplatform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) er blevet en industristandard for LLM-observabilitet. Det giver et sæt API'er, SDK'er og værktøjer til at generere, indsamle og eksportere telemetridata. 

Der findes mange instrumenteringsbiblioteker, der pakker eksisterende agent-rammeværk ind og gør det nemt at eksportere OpenTelemetry-spans til et observabilitetsværktøj. Microsoft Agent Framework integrerer med OpenTelemetry indbygget. Nedenfor er et eksempel på instrumentering af en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentens udførelse spores automatisk
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Manuel span-oprettelse:** Mens instrumenteringsbiblioteker giver en god baseline, er der ofte tilfælde, hvor mere detaljeret eller tilpasset information er nødvendig. Du kan manuelt oprette spans for at tilføje brugerdefineret applikationslogik. Endnu vigtigere kan de berige automatisk eller manuelt oprettede spans med brugerdefinerede attributter (også kendt som tags eller metadata). Disse attributter kan inkludere forretningsspecifikke data, mellemliggende beregninger eller enhver kontekst, der kan være nyttig til debugging eller analyse, såsom `user_id`, `session_id` eller `model_version`.

Eksempel på at oprette traces og spans manuelt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent-evaluering

Observabilitet giver os metrikker, men evaluering er processen med at analysere disse data (og udføre tests) for at afgøre, hvor godt en AI-agent præsterer, og hvordan den kan forbedres. Med andre ord, når du har de traces og metrikker, hvordan bruger du dem til at bedømme agenten og træffe beslutninger?

Regelmæssig evaluering er vigtig, fordi AI-agenter ofte er ikke-deterministiske og kan udvikle sig (gennem opdateringer eller drifting af modeladfærd) – uden evaluering ville du ikke vide, om din "smarte agent" faktisk udfører sit job godt, eller om den er gået tilbage i ydeevne.

Der er to kategorier af evalueringer for AI-agenter: **online-evaluering** og **offline-evaluering**. Begge er værdifulde og komplementerer hinanden. Vi starter normalt med offline-evaluering, da dette er det minimale nødvendige trin, inden man deployerer en agent.

### Offline-evaluering

![Datasætposter i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette involverer evaluering af agenten i et kontrolleret miljø, typisk ved brug af testdatasets, ikke live brugerspørgsmål. Du bruger kuraterede datasæt, hvor du ved, hvad det forventede output eller korrekt adfærd er, og derefter kører din agent på disse.

For eksempel, hvis du har bygget en agent til matematikordopgaver, kan du have et [testdatasæt](https://huggingface.co/datasets/gsm8k) på 100 opgaver med kendte svar. Offline-evaluering udføres ofte under udvikling (og kan være en del af CI/CD-pipelines) for at kontrollere forbedringer eller forhindre regressionsfejl. Fordelen er, at det er **gentageligt, og du kan få klare nøjagtighedsmetrikker, da du har ground truth**. Du kan også simulere brugerforespørgsler og måle agentens svar imod ideelle svar eller bruge automatiserede metrikker som beskrevet ovenfor.

Den centrale udfordring ved offline-eval er at sikre, at dit testdatasæt er omfattende og forbliver relevant – agenten kan klare sig godt på et fast testset, men støde på meget forskellige forespørgsler i produktion. Derfor bør du holde testset opdateret med nye edge cases og eksempler, der afspejler virkelige scenarier. En blanding af små "smoke test"-cases og større evalueringssæt er nyttig: små sæt til hurtige checks og større sæt til bredere præstationsmålinger.

### Online-evaluering

![Oversigt over observabilitetsmålinger](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering af agenten i et live, virkeligt miljø, dvs. under faktisk brug i produktion. Online-evaluering involverer overvågning af agentens ydeevne på rigtige brugerinteraktioner og løbende analyse af resultater.

For eksempel kan du spore succesrater, brugertilfredsheds-score eller andre metrikker på live-trafik. Fordelen ved online-evaluering er, at den **fanger ting, du måske ikke forudser i et laboratorium** – du kan observere model-drift over tid (hvis agentens effektivitet nedbrydes, efterhånden som input-mønstre ændrer sig) og fange uventede forespørgsler eller situationer, der ikke var i dit testdata. Det giver et sandt billede af, hvordan agenten opfører sig "i det fri".

Online-evaluering involverer ofte indsamling af implicit og eksplicit brugerfeedback, som diskuteret, og eventuelt kørsel af shadow-tests eller A/B-tests (hvor en ny version af agenten kører parallelt for at sammenligne med den gamle). Udfordringen er, at det kan være svært at få pålidelige labels eller scores for live-interaktioner – du kan være nødt til at stole på brugerfeedback eller downstream-metrics (f.eks. om brugeren klikkede på resultatet).

### Kombination af de to

Online- og offline-evaluering er ikke gensidigt udelukkende; de supplerer hinanden kraftigt. Indsigter fra online-overvågning (f.eks. nye typer brugerspørgsmål, hvor agenten klarer sig dårligt) kan bruges til at udvide og forbedre offline-testdatasæt. Omvendt kan agenter, der klarer sig godt i offline-tests, derefter deployeres med større tillid og overvåges online.

Faktisk adopterer mange teams en løkke:

_evaluer offline -> deployer -> overvåg online -> indsamle nye fejlcases -> tilføj til offline-datasæt -> forfin agent -> gentag_.

## Almindelige problemer

Når du udruller AI-agenter i produktion, kan du støde på forskellige udfordringer. Her er nogle almindelige problemer og deres mulige løsninger:

| **Problem**    | **Potentiel løsning**   |
| ------------- | ------------------ |
| AI-agenten udfører ikke opgaver konsekvent | - Forfin prompten givet til AI-agenten; vær klar i målsætninger.<br>- Identificer hvor opdelingen af opgaver i delopgaver og håndtering af dem af flere agenter kan hjælpe. |
| AI-agenten kører ind i kontinuerlige løkker  | - Sørg for, at du har klare termineringsbetingelser, så agenten ved, hvornår den skal stoppe processen.<br>- For komplekse opgaver, der kræver ræsonnement og planlægning, brug en større model, der er specialiseret i ræsonnement. |
| AI-agentens værktøjskald fungerer ikke godt   | - Test og valider værktøjets output uden for agentsystemet.<br>- Forfin de definerede parametre, prompts og navngivning af værktøjer.  |
| Multi-agent systemet fungerer ikke konsekvent | - Forfin prompts givet til hver agent for at sikre, at de er specifikke og forskellige fra hinanden.<br>- Byg et hierarkisk system ved hjælp af en "routing" eller controller-agent til at bestemme, hvilken agent der er den korrekte. |

Mange af disse problemer kan identificeres mere effektivt med observabilitet på plads. De traces og metrikker, vi diskuterede tidligere, hjælper med præcist at påpege, hvor i agent-workflowet problemer opstår, hvilket gør debugging og optimering meget mere effektivt.

## Håndtering af omkostninger
Her er nogle strategier til at håndtere omkostningerne ved at sætte AI-agenter i produktion:

**Using Smaller Models:** Small Language Models (SLMs) kan præstere godt i visse agentiske anvendelsestilfælde og vil reducere omkostningerne betydeligt. Som nævnt tidligere er det bedste middel til at forstå, hvor godt en SLM vil klare sig i dit brugstilfælde, at opbygge et evalueringssystem til at fastslå og sammenligne ydeevnen i forhold til større modeller. Overvej at bruge SLMs til enklere opgaver som intentionklassificering eller parameterudtrækning, mens du reserverer større modeller til kompleks ræsonnering.

**Using a Router Model:** En lignende strategi er at anvende modeller i forskellige størrelser. Du kan bruge en LLM/SLM eller en serverløs funktion til at rute forespørgsler baseret på kompleksitet til de bedst egnede modeller. Dette hjælper også med at reducere omkostningerne samtidig med, at det sikrer ydeevne på de rette opgaver. For eksempel kan du rute simple forespørgsler til mindre, hurtigere modeller og kun bruge dyre, store modeller til komplekse ræsonneringsopgaver.

**Caching Responses:** At identificere almindelige forespørgsler og opgaver og levere svarene, før de kommer igennem dit agentiske system, er en god måde at reducere mængden af lignende forespørgsler på. Du kan endda implementere et flow til at identificere, hvor lignende en forespørgsel er i forhold til dine cachede forespørgsler ved hjælp af mere simple AI-modeller. Denne strategi kan reducere omkostningerne betydeligt for ofte stillede spørgsmål eller almindelige arbejdsgange.

## Lad os se, hvordan dette fungerer i praksis

I [eksempelnotebooket i denne sektion](./code_samples/10-expense_claim-demo.ipynb) vil vi se eksempler på, hvordan vi kan bruge observabilitetsværktøjer til at overvåge og evaluere vores agent.


### Har du flere spørgsmål om AI-agenter i produktion?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre deltagere, deltage i kontortimer og få besvaret dine spørgsmål om AI-agenter.

## Forrige lektion

[Metakognition Designmønster](../09-metacognition/README.md)

## Næste lektion

[Agentiske protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget bør betragtes som den autoritative kilde. Til kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->