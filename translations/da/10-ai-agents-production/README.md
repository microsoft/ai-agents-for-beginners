# AI-agenter i produktion: Observabilitet & evaluering

[![AI Agents in Production](../../../translated_images/da/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Efterhånden som AI-agenter bevæger sig fra eksperimentelle prototyper til virkelige anvendelser, bliver evnen til at forstå deres adfærd, overvåge deres ydeevne og systematisk evaluere deres output vigtig.

## Læringsmål

Efter at have gennemført denne lektion vil du vide, hvordan du/forstår:
- Grundlæggende begreber inden for agentobservabilitet og evaluering
- Teknikker til at forbedre agenternes ydeevne, omkostninger og effektivitet
- Hvad og hvordan du systematisk evaluerer dine AI-agenter
- Hvordan du kontrollerer omkostninger, når du implementerer AI-agenter i produktion
- Hvordan du instrumenterer agenter bygget med Microsoft Agent Framework

Målet er at udstyre dig med viden til at transformere dine "black box"-agenter til gennemsigtige, håndterbare og pålidelige systemer.

_**Bemærk:** Det er vigtigt at implementere AI-agenter, der er sikre og troværdige. Se også lektionen [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Traces og Spans

Observabilitetsværktøjer som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) repræsenterer normalt agentkørsler som traces og spans.

- **Trace** repræsenterer en komplet agentopgave fra start til slut (som håndtering af en brugerhenvendelse).
- **Spans** er enkelte trin inden for tracen (som kald til et sprogmodel eller datahentning).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uden observabilitet kan en AI-agent føles som en "black box" – dens interne tilstand og ræsonnement er uigennemsigtige, hvilket gør det vanskeligt at diagnosticere problemer eller optimere ydeevne. Med observabilitet bliver agenter til "glasbokse," der tilbyder gennemsigtighed, hvilket er afgørende for at opbygge tillid og sikre, at de fungerer som tiltænkt.

## Hvorfor observabilitet er vigtigt i produktionsmiljøer

Overgangen af AI-agenter til produktionsmiljøer introducerer en ny række udfordringer og krav. Observabilitet er ikke længere “rart at have”, men en kritisk funktion:

*   **Fejlfinding og årsagsanalyse**: Når en agent fejler eller producerer et uventet output, giver observabilitetsværktøjer de traces, der er nødvendige for at identificere årsagen til fejlen. Dette er især vigtigt i komplekse agenter, der kan involvere flere LLM-kald, værktøjsinteraktioner og betinget logik.
*   **Latency og omkostningsstyring**: AI-agenter er ofte afhængige af LLM’er og andre eksterne API’er, som faktureres per token eller per kald. Observabilitet tillader præcis sporing af disse kald, hvilket hjælper med at identificere operationer, der er særligt langsomme eller dyre. Det gør det muligt for teams at optimere prompts, vælge mere effektive modeller eller omdesigne arbejdsgange for at styre driftsomkostninger og sikre en god brugeroplevelse.
*   **Tillid, sikkerhed og compliance**: I mange anvendelser er det vigtigt at sikre, at agenter opfører sig sikkert og etisk forsvarligt. Observabilitet giver en revisionsspor over agentens handlinger og beslutninger. Dette kan bruges til at registrere og afbøde problemer som promptinjektion, generering af skadeligt indhold eller mishandling af personligt identificerbare oplysninger (PII). For eksempel kan du gennemgå traces for at forstå, hvorfor en agent gav et bestemt svar eller brugte et bestemt værktøj.
*   **Kontinuerlige forbedringssløjfer**: Observabilitetsdata er fundamentet for en iterativ udviklingsproces. Ved at overvåge, hvordan agenter præsterer i den virkelige verden, kan teams identificere forbedringsområder, indsamle data til finjustering af modeller og validere effekten af ændringer. Dette skaber en feedback-sløjfe, hvor produktionsindsigter fra online evaluering informerer offline eksperimenter og forfining, hvilket fører til gradvist bedre agentpræstation.

## Vigtige metrics at spore

For at overvåge og forstå agentens adfærd bør en række metrics og signaler følges. Mens de specifikke metrics kan variere baseret på agentens formål, er nogle universelt vigtige.

Her er nogle af de mest almindelige metrics, som observabilitetsværktøjer overvåger:

**Latency:** Hvor hurtigt svarer agenten? Lange ventetider påvirker brugeroplevelsen negativt. Du bør måle latency for opgaver og enkelte trin ved at trace agentkørsler. For eksempel kunne en agent, der tager 20 sekunder om alle modelkald, accelereres ved at bruge en hurtigere model eller ved at køre modelkald parallelt.

**Omkostninger:** Hvad er omkostningen per agentkørsel? AI-agenter er afhængige af LLM-kald, der faktureres per token eller eksterne API’er. Hyppig brug af værktøjer eller flere prompts kan hurtigt øge omkostningerne. For eksempel, hvis en agent kalder en LLM fem gange for en marginal kvalitetsforbedring, skal du vurdere, om omkostningen er berettiget, eller om du kunne reducere antallet af kald eller bruge en billigere model. Realtidsovervågning kan også hjælpe med at identificere uventede spidser (f.eks. fejl, der forårsager overdrevne API-løkker).

**Fejl i forespørgsler:** Hvor mange forespørgsler fejlede agenten i? Dette kan omfatte API-fejl eller fejlede værktøjskald. For at gøre din agent mere robust mod disse i produktion kan du opsætte fallback-mekanismer eller genforsøg. Fx hvis LLM-udbyder A er nede, kan du skifte til LLM-udbyder B som backup.

**Brugerfeedback:** Implementering af direkte brugervurderinger giver værdifulde indsigter. Dette kan inkludere eksplicitte vurderinger (👍thumbs-up/👎down, ⭐1-5 stjerner) eller tekstkommentarer. Konsistent negativ feedback bør advare dig, da det er et tegn på, at agenten ikke fungerer som forventet.

**Implicit brugerfeedback:** Brugeradfærd giver indirekte feedback, selv uden eksplicitte vurderinger. Dette kan inkludere øjeblikkelig omformulering af spørgsmål, gentagne forespørgsler eller klik på en gentagelsesknap. F.eks. hvis du ser, at brugere gentagne gange stiller det samme spørgsmål, er det et tegn på, at agenten ikke fungerer som forventet.

**Nøjagtighed:** Hvor ofte producerer agenten korrekte eller ønskede output? Definitionen af nøjagtighed varierer (f.eks. korrekt problemløsning, informationsgenfindelsesnøjagtighed, brugertilfredshed). Det første skridt er at definere, hvordan succes ser ud for din agent. Du kan spore nøjagtighed via automatiserede checks, evalueringsscorer eller opgavelabels. F.eks. ved at markere traces som "succeeded" eller "failed".

**Automatiserede evalueringsmetrics:** Du kan også opsætte automatiserede evalueringer. For eksempel kan du bruge en LLM til at score agentens output, fx om det er hjælpsomt, nøjagtigt eller ej. Der findes også flere open source-biblioteker, der hjælper med at vurdere forskellige aspekter af agenten. Fx [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://llm-guard.com/) til at opdage skadeligt sprog eller promptinjektion.

I praksis giver en kombination af disse metrics den bedste dækning af en AI-agents sundhed. I dette kapitels [eksempel-notebook](./code_samples/10-expense_claim-demo.ipynb) viser vi, hvordan disse metrics ser ud i virkelige eksempler, men først lærer vi, hvordan en typisk evalueringsworkflow ser ud.

## Instrumenter din agent

For at indsamle trace-data skal du instrumentere din kode. Målet er at instrumentere agentkoden, så den udsender traces og metrics, som kan indfanges, processeres og visualiseres af en observabilitetsplatform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) er blevet en industristandard for LLM-observabilitet. Det tilbyder et sæt API’er, SDK’er og værktøjer til at generere, indsamle og eksportere telemetridata.

Der findes mange instrumenteringsbiblioteker, som omslutter eksisterende agent-frameworks og gør det nemt at eksportere OpenTelemetry-spans til et observabilitetsværktøj. Microsoft Agent Framework integrerer indbygget med OpenTelemetry. Nedenfor er et eksempel på at instrumentere en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentudførelse spores automatisk
    pass
```

[Example notebook](./code_samples/10-expense_claim-demo.ipynb) i dette kapitel demonstrerer, hvordan du instrumenterer din MAF-agent.

**Manuel span-oprettelse:** Mens instrumenteringsbiblioteker giver et godt udgangspunkt, er der ofte behov for mere detaljeret eller tilpasset information. Du kan manuelt oprette spans for at tilføje brugerdefineret applikationslogik. Endnu vigtigere, kan de berige automatisk eller manuelt oprettede spans med brugerdefinerede attributter (også kendt som tags eller metadata). Disse attributter kan inkludere forretningsspecifikke data, mellemliggende beregninger eller enhver kontekst, der måtte være nyttig til fejlfinding eller analyse, såsom `user_id`, `session_id` eller `model_version`.

Eksempel på at oprette traces og spans manuelt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentevaluering

Observabilitet giver os metrics, men evaluering er processen med at analysere disse data (og udføre tests) for at afgøre, hvor godt en AI-agent præsterer og hvordan den kan forbedres. Med andre ord, når du har disse traces og metrics, hvordan bruger du dem til at vurdere agenten og træffe beslutninger?

Regelmæssig evaluering er vigtig, fordi AI-agenter ofte er ikke-deterministiske og kan udvikle sig (gennem opdateringer eller ændringer i modeladfærd) – uden evaluering ville du ikke vide, om din “smarte agent” rent faktisk udfører sit arbejde godt eller er gået tilbage.

Der findes to kategorier af evalueringer for AI-agenter: **online evaluering** og **offline evaluering**. Begge er værdifulde og supplerer hinanden. Vi begynder som regel med offline evaluering, da det er det mindst nødvendige skridt før implementering af en agent.

### Offline evaluering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette involverer evaluering af agenten i en kontrolleret setting, typisk ved brug af testdatasæt, ikke levende brugerhenvendelser. Du bruger kuraterede datasæt, hvor du ved, hvad det forventede output eller korrekte adfærd er, og kører så din agent på disse.

For eksempel, hvis du byggede en agent til matematiske tekstopgaver, kunne du have et [testdatasæt](https://huggingface.co/datasets/gsm8k) med 100 opgaver med kendte svar. Offline evaluering foretages ofte under udvikling (og kan være en del af CI/CD-pipelines) for at tjekke forbedringer eller forhindre tilbagegang. Fordelen er, at det er **gentageligt, og du kan få klare nøjagtighedsmetrics, fordi du har sandheden til rådighed**. Du kan også simulere brugerhenvendelser og måle agentens svar mod ideelle svar eller bruge automatiserede metrics som beskrevet ovenfor.

Den største udfordring med offline evaluering er at sikre, at dit testdatasæt er omfattende og forbliver relevant – agenten kan klare sig godt på et fast testdatasæt, men støde på meget anderledes forespørgsler i produktion. Derfor bør du holde testdatasæt opdaterede med nye kanttilfælde og eksempler, der afspejler virkelige scenarier. En blanding af små “smoke test”-cases og større evalueringssæt er nyttig: små sæt til hurtige checks og større sæt til bredere præstationsmålinger.

### Online evaluering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering af agenten i et levende, virkeligt miljø, altså under faktisk brug i produktion. Online evaluering indebærer overvågning af agentens ydeevne på rigtige brugerinteraktioner og løbende analyse af resultater.

For eksempel kan du spore succesrater, brugertilfredshedsscorer eller andre metrics på live trafik. Fordelen ved online evaluering er, at det **fanger ting, du måske ikke havde forudset i et laboratoriemiljø** – du kan observere modelafvigelse over tid (hvis agentens effektivitet falder, efterhånden som inputmønstre skifter) og opdage uventede forespørgsler eller situationer, der ikke var i dit testdata. Det giver et ægte billede af, hvordan agenten opfører sig i felten.

Online evaluering involverer ofte indsamling af implicit og eksplicit brugerfeedback, som diskuteret, og eventuelt kørsel af shadow tests eller A/B-tests (hvor en ny version af agenten kører parallelt for at sammenligne med den gamle). Udfordringen er, at det kan være svært at få pålidelige labels eller scores for live-interaktioner – du er muligvis afhængig af brugerfeedback eller downstream metrics (f.eks. om brugeren klikker på resultatet).

### Kombinere de to

Online og offline evalueringer er ikke gensidigt udelukkende; de supplerer hinanden kraftigt. Indsigter fra online overvågning (f.eks. nye typer brugerforespørgsler, hvor agenten klarer sig dårligt) kan bruges til at udvide og forbedre offline testdatasæt. Omvendt kan agenter, der klarer sig godt i offline tests, derefter implementeres med større tillid og overvåges online.

Mange teams følger faktisk en cyklus:

_evaluer offline -> implementer -> overvåg online -> indsamle nye fejltilfælde -> tilføj til offline datasæt -> forfine agent -> gentag_.

## Almindelige problemer

Når du implementerer AI-agenter i produktion, kan du støde på forskellige udfordringer. Her er nogle almindelige problemer og deres mulige løsninger:

| **Problem**    | **Mulig løsning**   |
| ------------- | ------------------ |
| AI-agenten udfører ikke opgaver konsekvent | - Forfin prompten givet til AI-agenten; vær klar omkring målene.<br>- Identificer, om opgaver kan opdeles i delopgaver håndteret af flere agenter. |
| AI-agenten kører i kontinuerlige loops  | - Sørg for klare betingelser for afslutning, så agenten ved, hvornår processen skal stoppe.<br>- Til komplekse opgaver, der kræver ræsonnement og planlægning, brug en større model, der er specialiseret til sådanne opgaver. |
| AI-agentens værktøjskald fungerer ikke godt   | - Test og valider værktøjets output uden for agentsystemet.<br>- Forfin de definerede parametre, prompts og navngivning af værktøjer.  |
| Multi-agent systemet fungerer ikke konsekvent | - Forfin prompts til hver agent, så de er specifikke og forskellige fra hinanden.<br>- Byg et hierarkisk system med en "routing" eller controller agent, der bestemmer, hvilken agent der er den korrekte. |

Mange af disse problemer kan identificeres mere effektivt med observabilitet på plads. De traces og metrics, vi tidligere har diskuteret, hjælper med præcist at lokalisere, hvor i agentworkflowen problemer opstår, hvilket gør fejlfinding og optimering meget mere effektivt.

## Omkostningsstyring
Her er nogle strategier til at håndtere omkostningerne ved at implementere AI-agenter i produktion:

**Brug af mindre modeller:** Små sprogmodeller (SLM'er) kan klare sig godt på visse agentiske anvendelsestilfælde og vil reducere omkostningerne betydeligt. Som nævnt tidligere er opbygning af et evalueringssystem til at bestemme og sammenligne ydeevne i forhold til større modeller den bedste måde at forstå, hvor godt en SLM klarer sig i dit anvendelsestilfælde. Overvej at bruge SLM'er til enklere opgaver som intentionsklassificering eller parameterudtrækning, mens større modeller reserveres til kompleks ræsonnering.

**Brug af en router-model:** En lignende strategi er at bruge en mangfoldighed af modeller og størrelser. Du kan bruge en LLM/SLM eller en serverløs funktion til at rute forespørgsler baseret på kompleksitet til de bedst egnede modeller. Dette vil også hjælpe med at reducere omkostningerne og samtidig sikre ydeevne på de rette opgaver. For eksempel rutes simple forespørgsler til mindre, hurtigere modeller, og dyre store modeller bruges kun til komplekse ræsonneringsopgaver.

**Caching af svar:** Identifikation af almindelige forespørgsler og opgaver samt levering af svarene, før de går gennem dit agentiske system, er en god måde at reducere mængden af lignende forespørgsler på. Du kan endda implementere en flow til at identificere, hvor lignende en forespørgsel er i forhold til dine cachede forespørgsler ved hjælp af mere basale AI-modeller. Denne strategi kan markant reducere omkostninger for hyppigt stillede spørgsmål eller almindelige arbejdsgange.

## Lad os se, hvordan dette fungerer i praksis

I [eksempelnoteaturen i denne sektion](./code_samples/10-expense_claim-demo.ipynb) vil vi se eksempler på, hvordan vi kan bruge observabilitetsværktøjer til at overvåge og evaluere vores agent.

### Har du flere spørgsmål om AI-agenter i produktion?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få besvaret dine spørgsmål om AI-agenter.

## Forrige lektion

[Metakognitionsdesignmønster](../09-metacognition/README.md)

## Næste lektion

[Agentiske protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->