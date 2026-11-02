# AI-agenter i produksjon: Observabilitet og evaluering

[![AI Agents in Production](../../../translated_images/no/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Når AI-agenter går fra eksperimentelle prototyper til virkelige applikasjoner, blir evnen til å forstå deres oppførsel, overvåke deres ytelse og systematisk evaluere deres resultater viktig.

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan/forstå:
- Kjernkonsepter for agentobservabilitet og evaluering
- Teknikker for å forbedre ytelse, kostnader og effektivitet av agenter
- Hva og hvordan du systematisk evaluerer dine AI-agenter
- Hvordan kontrollere kostnader ved utrulling av AI-agenter i produksjon
- Hvordan instrumentere agenter bygget med Microsoft Agent Framework

Målet er å utstyre deg med kunnskapen for å forvandle dine "svartbokser" til transparente, håndterbare og pålitelige systemer.

_**Merk:** Det er viktig å distribuere AI-agenter som er trygge og pålitelige. Se også leksjonen [Bygge pålitelige AI-agenter](../06-building-trustworthy-agents/README.md)._

## Spor og Spans

Observabilitetsverktøy som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerer vanligvis agentkjøringer som spor og spans.

- **Spor** representerer en komplett agentoppgave fra start til slutt (som å behandle en brukerforespørsel).
- **Spans** er individuelle steg innenfor sporet (som å kalle et språkmodell eller hente data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uten observabilitet kan en AI-agent føles som en "svart boks" – dens interne tilstand og resonnement er ugjennomsiktige, noe som gjør det vanskelig å diagnostisere problemer eller optimalisere ytelsen. Med observabilitet blir agenter "glassbokser", som tilbyr åpenhet som er avgjørende for å bygge tillit og sikre at de opererer som tiltenkt.

## Hvorfor observabilitet er viktig i produksjonsmiljøer

Overgangen av AI-agenter til produksjonsmiljøer introduserer et nytt sett med utfordringer og krav. Observabilitet er ikke lenger en "nice-to-have" men en kritisk evne:

*   **Feilsøking og rotårsaksanalyse**: Når en agent feiler eller produserer et uventet output, gir observabilitetsverktøy sporene som trengs for å finne kilden til feilen. Dette er spesielt viktig i komplekse agenter som kan involvere flere LLM-kall, verktøyinteraksjoner og betinget logikk.
*   **Latens og kostnadsstyring**: AI-agenter benytter ofte LLM-er og andre eksterne API-er som faktureres per token eller kall. Observabilitet gir presis sporing av disse kallene, og hjelper med å identifisere operasjoner som er unødvendig trege eller dyre. Dette gjør det mulig for team å optimalisere prompt, velge mer effektive modeller eller redesigne arbeidsflyter for å kontrollere driftskostnader og sikre god brukeropplevelse.
*   **Tillit, sikkerhet og samsvar**: I mange applikasjoner er det viktig å sikre at agenter oppfører seg trygt og etisk. Observabilitet gir et revisjonsspor av agenthandlinger og beslutninger. Dette kan brukes til å oppdage og avhjelpe problemer som promptinjeksjon, generering av skadelig innhold eller feilbehandling av personlig identifiserbar informasjon (PII). For eksempel kan du gjennomgå spor for å forstå hvorfor en agent ga et bestemt svar eller brukte et spesifikt verktøy.
*   **Kontinuerlige forbedringssløyfer**: Observabilitetsdata er grunnlaget for en iterativ utviklingsprosess. Ved å overvåke hvordan agenter presterer i virkeligheten, kan team identifisere forbedringsområder, samle data for finjustering av modeller og validere effekten av endringer. Dette skaper en tilbakemeldingssløyfe hvor produksjonsinnsikter fra online evaluering informerer offline eksperimentering og forbedring, noe som fører til stadig bedre agentytelse.

## Nøkkelmetrikker å følge med på

For å overvåke og forstå agentoppførsel bør et utvalg metrikker og signaler følges. Mens spesifikke metrikker kan variere basert på agentens formål, er noen universelt viktige.

Her er noen av de vanligste metrikker som observabilitetsverktøy overvåker:

**Latens:** Hvor raskt svarer agenten? Lange ventetider påvirker brukeropplevelsen negativt. Du bør måle latens for oppgaver og individuelle steg ved å spore agentkjøringer. For eksempel kan en agent som bruker 20 sekunder på alle modellkall akselereres ved å bruke en raskere modell eller kjøre modellkall parallelt.

**Kostnader:** Hva koster en agentkjøring? AI-agenter baserer seg på LLM-kall som faktureres per token eller eksterne API-er. Hyppig bruk av verktøy eller flere prompt kan raskt øke kostnadene. For eksempel, hvis en agent kaller en LLM fem ganger for en marginal kvalitetsforbedring, må du vurdere om kostnaden er rettferdiggjort eller om du kan redusere antallet kall eller bruke en rimeligere modell. Sanntidsovervåking kan også hjelpe med å identifisere uventede topper (f.eks. feil som forårsaker overdrevne API-sykluser).

**Forespørselsfeil:** Hvor mange forespørsler feilet agenten på? Dette kan inkludere API-feil eller mislykkede verktøykall. For å gjøre agenten mer robust mot disse i produksjon, kan du sette opp fallback-løsninger eller gjenforsøk. Fx hvis LLM-leverandør A er nede, kan du bytte til leverandør B som backup.

**Brukertilbakemelding:** Implementering av direkte brukerevalueringer gir verdifull innsikt. Dette kan inkludere eksplisitte vurderinger (👍tommel opp/👎tommel ned, ⭐1-5 stjerner) eller tekstlige kommentarer. Konsistent negativ feedback bør varsle deg da dette er et tegn på at agenten ikke fungerer som forventet.

**Implicit brukertilbakemelding:** Brukeratferd gir indirekte feedback selv uten eksplisitte vurderinger. Dette kan inkludere umiddelbar omformulering av spørsmål, gjentatte forespørsler eller klikk på en prøv på nytt-knapp. F.eks. hvis du ser at brukere gjentatte ganger stiller det samme spørsmålet, er dette et tegn på at agenten ikke fungerer som forventet.

**Nøyaktighet:** Hvor ofte produserer agenten korrekte eller ønskelige resultater? Definisjoner av nøyaktighet varierer (f.eks. korrekt løsning av problemer, nøyaktighet i informasjonsinnhenting, brukertilfredshet). Det første trinnet er å definere hva suksess betyr for din agent. Du kan spore nøyaktighet via automatiske kontroller, evalueringspoeng eller oppgavefullføringsetiketter. For eksempel å merke spor som "lyktes" eller "mislyktes".

**Automatiserte evalueringsmetrikker:** Du kan også sette opp automatiserte evalueringer. For eksempel kan du bruke en LLM til å gi poeng på agentens output, f.eks. om det er nyttig, nøyaktig eller ikke. Det finnes også flere åpne kilde-biblioteker som hjelper deg å score ulike aspekter av agenten. F.eks. [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://github.com/protectai/llm-guard) for å oppdage skadelig språkbruk eller promptinjeksjon.

I praksis gir en kombinasjon av disse metrikker best dekning av en AI-agents helsetilstand. I dette kapitlets [eksempelnote](./code_samples/10-expense_claim-demo.ipynb) vil vi vise deg hvordan disse metrikker ser ut i virkelige eksempler, men først lærer vi hvordan en typisk evalueringsarbeidsflyt ser ut.

## Instrumenter agenten din

For å samle sporeddata må du instrumentere koden. Målet er å instrumentere agentkoden for å sende ut spor og metrikker som kan fanges, behandles og visualiseres av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har etablert seg som en industristandard for LLM-observabilitet. Det tilbyr en sett API-er, SDK-er og verktøy for generering, innsamling og eksport av telemetridata.

Det finnes mange instrumentasjonsbiblioteker som pakker inn eksisterende agentrammeverk og gjør det enkelt å eksportere OpenTelemetry-spans til et observabilitetsverktøy. Microsoft Agent Framework integrerer OpenTelemetry nativer. Nedenfor er et eksempel på å instrumentere en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

[Eksempelnote](./code_samples/10-expense_claim-demo.ipynb) i dette kapitlet vil demonstrere hvordan du instrumenterer MAF-agenten din.

**Manuell span-opprettelse:** Selv om instrumentasjonsbiblioteker gir et godt grunnlag, er det ofte tilfeller hvor mer detaljert eller tilpasset informasjon trengs. Du kan manuelt opprette spans for å legge til egendefinert applikasjonslogikk. Viktigere er at de kan berike automatisk eller manuelt opprettede spans med egendefinerte attributter (også kalt tags eller metadata). Disse attributtene kan inkludere forretningsspesifikke data, mellomregninger, eller enhver kontekst som kan være nyttig for feilsøking eller analyse, som `user_id`, `session_id`, eller `model_version`.

Eksempel på manuell opprettelse av spor og spans med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent-evaluering

Observabilitet gir oss metrikker, men evaluering er prosessen med å analysere disse dataene (og utføre tester) for å avgjøre hvor godt en AI-agent presterer og hvordan den kan forbedres. Med andre ord, når du har disse spor og metrikker, hvordan bruker du dem til å vurdere agenten og ta beslutninger?

Reglemessig evaluering er viktig fordi AI-agenter ofte er ikke-deterministiske og kan utvikle seg (gjennom oppdateringer eller atferdsendringer i modellen) – uten evaluering vil du ikke vite om din “smarte agent” faktisk gjør jobben sin godt eller om den har regress.

Det finnes to kategorier evalueringsmetoder for AI-agenter: **online evaluering** og **offline evaluering**. Begge er verdifulle og utfyller hverandre. Vi begynner vanligvis med offline evaluering, da dette er det minste nødvendige trinnet før utrulling av en agent.

### Offline evaluering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette innebærer å evaluere agenten i et kontrollert miljø, vanligvis med testdatasett, ikke live brukerforespørsler. Du bruker kuraterte datasett hvor du vet hva forventet output eller korrekt oppførsel er, og så kjører du agenten på disse.

For eksempel, hvis du har bygget en agent for matteoppgaver, kan du ha et [testdatasett](https://huggingface.co/datasets/openai/gsm8k) med 100 problemer med kjente svar. Offline evaluering gjøres ofte under utvikling (og kan inngå i CI/CD-pipeliner) for å sjekke forbedringer eller forhindre regresjon. Fordelen er at det er **reproduserbart og du kan få klare nøyaktighetsmetrikker siden du har et grunnsannhet**. Du kan også simulere brukerforespørsler og måle agentens svar mot ideelle svar eller bruke automatiserte metrikker som beskrevet ovenfor.

Hovedutfordringen med offline evaluering er å sikre at testdatasettet ditt er omfattende og forblir relevant – agenten kan prestere godt på et fast testsett, men møte svært forskjellige forespørsler i produksjon. Derfor bør du holde testsettene oppdatert med nye kanttilfeller og eksempler som reflekterer virkelige scenarioer. En blanding av små “smøretester” og større evalueringssett er nyttig: små sett for raske kontroller og større for bredere ytelsesmålinger.

### Online evaluering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering av agenten i et levende, virkelighetsnært miljø, altså under faktisk bruk i produksjon. Online evaluering involverer overvåking av agentens ytelse på ekte brukerinteraksjoner og kontinuerlig analyse av resultater.

For eksempel kan du spore suksessrater, brukertilfredshetsvurderinger eller andre metrikker på live trafikk. Fordelen med online evaluering er at den **fanger opp ting du kanskje ikke kan forutsi i et laboratorium** – du kan observere modellendring over tid (hvis agentens effektivitet avtar ettersom inndataendringer skjer) og fange opp uventede forespørsler eller situasjoner som ikke fantes i testdataene. Dette gir et ekte bilde av hvordan agenten oppfører seg i felt.

Online evaluering innebærer ofte innsamling av både implisitt og eksplisitt brukertilbakemelding, som diskutert, og muligens kjøring av skyggtester eller A/B tester (hvor en ny versjon av agenten kjører parallelt for sammenligning med den gamle). Utfordringen er at det kan være vanskelig å få pålitelige etiketter eller poeng for live interaksjoner – du kan måtte stole på brukertilbakemeldinger eller downstream-metrikker (som om brukeren klikket på resultatet).

### Kombinere de to

Online og offline evaluering er ikke gjensidig utelukkende; de utfyller hverandre godt. Innsikter fra online overvåking (f.eks. nye typer brukerforespørsler hvor agenten presterer dårlig) kan brukes til å supplere og forbedre offline testdatasett. Omvendt kan agenter som presterer godt i offline tester, med større trygghet distribueres og overvåkes online.

Faktisk adopterer mange team en sløyfe:

_evaluer offline -> distribuer -> overvåk online -> saml nye feilstilfeller -> legg til i offline datasett -> forbedre agent -> gjenta_.

## Vanlige problemer

Når du ruller ut AI-agenter i produksjon, kan du møte ulike utfordringer. Her er noen vanlige problemer og mulige løsninger:

| **Problem**    | **Potensiell løsning**   |
| ------------- | ------------------ |
| AI-agenten utfører ikke oppgaver konsekvent | - Forbedre prompten som gis til AI-agenten; vær tydelig på mål.<br>- Identifiser hvor oppgavene kan deles i deloppgaver og håndteres av flere agenter. |
| AI-agenten havner i kontinuerlige løkker | - Sørg for klare avslutningsvilkår slik at agenten vet når prosessen skal stoppe.<br>- For komplekse oppgaver som krever resonnement og planlegging, bruk en større modell som er spesialisert på slike oppgaver. |
| Agentens verktøykall fungerer ikke godt | - Test og valider verktøyets output utenfor agentsystemet.<br>- Forbedre definerte parametere, prompt og navn på verktøy. |
| Multi-agent system fungerer ikke konsekvent | - Forbedre promptene gitt til hver agent slik at de er spesifikke og distinkte.<br>- Bygg et hierarkisk system med en "rute-" eller kontrollagent som bestemmer hvilken agent som er riktig. |

Mange av disse problemene kan oppdages mer effektivt med observabilitet på plass. Sporene og metrikker vi diskuterte tidligere hjelper til med å finne nøyaktig hvor i agentens arbeidsflyt problemer oppstår, noe som gjør feilsøking og optimalisering mye mer effektivt.

## Kostnadsstyring

Her er noen strategier for å styre kostnadene ved utrulling av AI-agenter i produksjon:

**Bruke mindre modeller:** Små språkmodeller (SLM-er) kan prestere godt på visse agentiske brukstilfeller og vil redusere kostnadene betydelig. Som nevnt tidligere, er det beste å bygge et evalueringssystem for å bestemme og sammenligne ytelse mot større modeller, for å forstå hvor godt en SLM vil prestere for ditt brukstilfelle. Vurder å bruke SLM-er for enklere oppgaver som intensjonsklassifisering eller parameteruttrekk, mens du reserverer større modeller for kompleks resonnering.

**Bruke en ruter-modell:** En lignende strategi er å bruke en variasjon av modeller og størrelser. Du kan bruke en LLM/SLM eller serverløs funksjon til å rute forespørsler basert på kompleksitet til best egnede modeller. Dette vil også bidra til å redusere kostnader samtidig som ytelsen sikres på riktige oppgaver. For eksempel, rute enkle spørringer til mindre, raskere modeller, og kun bruke dyre store modeller for komplekse resonneringsoppgaver.

**Bufring av svar:** Identifisering av vanlige forespørsler og oppgaver og å levere svarene før de går gjennom ditt agentiske system er en god måte å redusere volumet av lignende forespørsler på. Du kan til og med implementere en flyt for å vurdere hvor lik en forespørsel er til dine bufrede forespørsler ved å bruke mer grunnleggende AI-modeller. Denne strategien kan redusere kostnader betydelig for ofte stilte spørsmål eller vanlige arbeidsflyter.

## La oss se hvordan dette fungerer i praksis

I [eksempelnottboken for denne seksjonen](./code_samples/10-expense_claim-demo.ipynb) vil vi se eksempler på hvordan vi kan bruke observasjonsverktøy for å overvåke og evaluere agenten vår.


### Har du flere spørsmål om AI-agenter i produksjon?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på spørsmålene dine om AI-agenter.

## Forrige leksjon

[Metakognisjonsdesignmønster](../09-metacognition/README.md)

## Neste leksjon

[Agentiske protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->