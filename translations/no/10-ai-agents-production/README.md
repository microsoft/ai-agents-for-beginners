# AI-agenter i produksjon: Observabilitet og evaluering

[![AI Agents in Production](../../../translated_images/no/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Etter hvert som AI-agenter går fra eksperimentelle prototyper til virkelige applikasjoner, blir evnen til å forstå deres oppførsel, overvåke deres ytelse og systematisk evaluere deres resultater viktig.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du vite hvordan du kan/forstå:
- Kjernebegreper innen agentobservabilitet og evaluering
- Metoder for å forbedre ytelsen, kostnadene og effektiviteten til agenter
- Hva og hvordan du systematisk evaluerer dine AI-agenter
- Hvordan kontrollere kostnader ved utrulling av AI-agenter i produksjon
- Hvordan instrumentere agenter bygget med Microsoft Agent Framework

Målet er å gi deg kunnskapen til å gjøre dine "black box"-agenter til transparente, håndterbare og pålitelige systemer.

_**Merk:** Det er viktig å distribuere AI-agenter som er sikre og pålitelige. Sjekk også ut [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md) leksjonen._

## Traces og Spans

Observabilitetsverktøy som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerer vanligvis agentkjøringer som traces og spans.

- **Trace** representerer en komplett agentoppgave fra start til slutt (f.eks. håndtering av en brukerforespørsel).
- **Spans** er individuelle steg innen trace (f.eks. å kalle et språkmodell eller hente data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uten observabilitet kan en AI-agent føles som en "black box" – dens interne tilstand og resonnement er utydelig, noe som gjør det vanskelig å diagnostisere problemer eller optimalisere ytelsen. Med observabilitet blir agentene til "glassbokser", og gir en åpenhet som er avgjørende for å bygge tillit og sikre at de fungerer som tiltenkt.

## Hvorfor observabilitet er viktig i produksjonsmiljøer

Overgangen av AI-agenter til produksjonsmiljøer introduserer et nytt sett med utfordringer og krav. Observabilitet er ikke lenger et "hyggelig å ha", men en kritisk evne:

*   **Feilsøking og årsaksanalyse:** Når en agent feiler eller gir uventet output, gir observabilitetsverktøy trace-data som trengs for å spore kilden til feilen. Dette er spesielt viktig i komplekse agenter som kan involvere flere LLM-kall, verktøyinteraksjoner og betinget logikk.
*   **Latens og kostnadshåndtering:** AI-agenter er ofte avhengige av LLM-er og andre eksterne API-er som belastes per token eller per kall. Observabilitet tillater presis sporing av disse kallene, og hjelper til med å identifisere operasjoner som er unødvendig langsomme eller dyre. Dette gjør det mulig for team å optimalisere forespørsler, velge mer effektive modeller eller redesigne arbeidsflyter for å håndtere operasjonelle kostnader og sikre en god brukeropplevelse.
*   **Tillitt, sikkerhet og etterlevelse:** I mange applikasjoner er det viktig å sikre at agenter oppfører seg trygt og etisk. Observabilitet gir en revisjonsspor av agentenes handlinger og beslutninger. Dette kan brukes til å oppdage og motvirke problemer som promptinjeksjon, generering av skadelig innhold eller feilbehandling av personlig identifiserbar informasjon (PII). For eksempel kan du gjennomgå traces for å forstå hvorfor en agent ga et bestemt svar eller brukte et spesifikt verktøy.
*   **Kontinuerlige forbedringssløyfer:** Observabilitetsdata er grunnlaget for en iterativ utviklingsprosess. Ved å overvåke hvordan agenter presterer i den virkelige verden, kan team identifisere forbedringsområder, samle data for finjustering av modeller, og validere effekten av endringer. Dette skaper en feedbacksløyfe der produksjonsinnsikt fra online evaluering informerer offline eksperimentering og forbedring, som fører til gradvis bedre agentytelse.

## Nøkkelmetrikker å spore

For å overvåke og forstå agentens oppførsel bør et bredt spekter av metrikker og signaler spores. Selv om de spesifikke metrikene kan variere basert på agentens formål, er noen universelt viktige.

Her er noen av de vanligste metrikker som observabilitetsverktøy overvåker:

**Latens:** Hvor raskt svarer agenten? Lange ventetider påvirker brukeropplevelsen negativt. Du bør måle latens for oppgaver og individuelle steg ved å spore agentkjøringer. For eksempel kan en agent som bruker 20 sekunder på alle modellkall akselereres ved å bruke en raskere modell eller kjøre kall parallelt.

**Kostnader:** Hva koster en agentkjøring? AI-agenter benytter LLM-kall som belastes per token eller eksterne API-er. Hyppig bruk av verktøy eller mange forespørsler kan raskt øke kostnadene. For eksempel, hvis en agent kaller en LLM fem ganger for marginal kvalitetforbedring, må du vurdere om kostnaden er berettiget eller om du kan redusere antall kall eller bruke en rimeligere modell. Sanntidsovervåking kan også hjelpe til å identifisere uventede topper (f.eks. feil som forårsaker overdrevne API-løkker).

**Forespørselsfeil:** Hvor mange forespørsler feilet agenten på? Dette kan inkludere API-feil eller mislykkede verktøyskall. For å gjøre agenten mer robust i produksjon, kan du deretter sette opp fallbacks eller retry-mekanismer. F.eks. hvis LLM-leverandør A er nede, bytter du til LLM-leverandør B som backup.

**Brukerfeedback:** Implementering av direkte brukerevalueringer gir verdifull innsikt. Dette kan inkludere eksplisitte vurderinger (👍tommel opp/👎tommel ned, ⭐1-5 stjerner) eller tekstkommentarer. Konsistent negativ tilbakemelding bør varsle deg, da dette er et tegn på at agenten ikke fungerer som forventet.

**Implisitt brukerfeedback:** Brukeratferd gir indirekte tilbakemeldinger selv uten eksplisitte vurderinger. Dette kan inkludere umiddelbar omformulering av spørsmål, gjentatte forespørsler eller klikk på retry-knapp. F.eks. hvis du ser at brukere gjentatte ganger stiller det samme spørsmålet, er dette et tegn på at agenten ikke fungerer som forventet.

**Nøyaktighet:** Hvor ofte gir agenten korrekte eller ønskede resultater? Definisjoner av nøyaktighet varierer (f.eks. problemløsning, informasjonsgjenfinning, brukertilfredshet). Det første steget er å definere hva suksess er for din agent. Du kan spore nøyaktighet via automatiserte kontroller, evalueringspoeng eller oppgavefullføringsetiketter. For eksempel å merke traces som "lyktes" eller "feilet".

**Automatiserte evalueringsmetrikker:** Du kan også sette opp automatiserte evalueringer. For eksempel kan du bruke en LLM for å score agentens output, f.eks. om den er hjelpsom, nøyaktig eller ikke. Det finnes også flere open source-biblioteker som hjelper deg med å score forskjellige aspekter av agenten, f.eks. [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://llm-guard.com/) for å oppdage skadelig språk eller promptinjeksjon.

I praksis gir en kombinasjon av disse metrikker best dekning av helsen til en AI-agent. I dette kapitlets [eksempelnlettebok](./code_samples/10-expense_claim-demo.ipynb) vil vi vise hvordan disse metrikker ser ut i virkelige eksempler, men først skal vi lære hvordan en typisk evalueringsflyt ser ut.

## Instrumenter din Agent

For å samle sporingsdata må du instrumentere koden din. Målet er å instrumentere agentkoden slik at den sender ut traces og metrikker som kan fanges opp, behandles og visualiseres av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har etablert seg som en industristandard for observabilitet av LLM-er. Den tilbyr sett med API-er, SDK-er og verktøy for å generere, samle inn og eksportere telemetridata.

Det finnes mange instrumenteringsbiblioteker som pakker inn eksisterende agent-rammeverk og gjør det enkelt å eksportere OpenTelemetry spans til et observabilitetsverktøy. Microsoft Agent Framework integrerer nativt med OpenTelemetry. Nedenfor er et eksempel på instrumentering av en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentutførelse spores automatisk
    pass
```

[Eksempelnletteboken](./code_samples/10-expense_claim-demo.ipynb) i dette kapitlet vil demonstrere hvordan du instrumenterer din MAF-agent.

**Manuell Opprettelse av Span:** Selv om instrumenteringsbiblioteker gir et godt grunnlag, er det ofte tilfeller hvor mer detaljert eller tilpasset informasjon er nødvendig. Du kan manuelt opprette spans for å legge til egendefinert applikasjonslogikk. Viktigst er at disse kan berike automatisk eller manuelt opprettede spans med egendefinerte attributter (også kalt tagger eller metadata). Disse attributtene kan inkludere forretningsspesifikke data, mellomliggende beregninger eller kontekst som kan være nyttig for feilsøking eller analyse, som `user_id`, `session_id` eller `model_version`.

Eksempel på å lage traces og spans manuelt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent Evaluering

Observabilitet gir oss metrikker, men evaluering er prosessen med å analysere disse dataene (og utføre tester) for å avgjøre hvordan en AI-agent presterer og hvordan den kan forbedres. Med andre ord, når du har traces og metrikker, hvordan bruker du dem til å vurdere agenten og ta beslutninger?

Regelmessig evaluering er viktig fordi AI-agenter ofte er ikke-deterministiske og kan utvikle seg (gjennom oppdateringer eller endrende modellatferd) – uten evaluering ville du ikke vite om din “smarte agent” faktisk gjør jobben sin bra eller om den har regressert.

Det finnes to kategorier av evalueringer for AI-agenter: **online evaluering** og **offline evaluering**. Begge er verdifulle, og de utfyller hverandre. Vi starter vanligvis med offline evaluering, da dette er det minste nødvendige steget før utrulling av en agent.

### Offline Evaluering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette innebærer evaluering av agenten i et kontrollert miljø, vanligvis med testdatasett, ikke levende brukerforespørsler. Du bruker kuraterte datasett hvor du vet hva forventet output eller korrekt oppførsel er, og kjører agenten på disse.

For eksempel, hvis du har bygget en addresseagent for matematiske tekstoppgaver, kan du ha et [testdatasett](https://huggingface.co/datasets/gsm8k) med 100 problemer med kjente svar. Offline evaluering gjøres ofte under utvikling (og kan være del av CI/CD-pipelines) for å sjekke forbedringer eller forhindre regresjoner. Fordelen er at det er **reproduserbart og du får klare nøyaktighetsmetrikker siden du har grunnsannheten**. Du kan også simulere brukerhenvendelser og måle agentens svar mot ideelle svar eller bruke automatiserte metrikker som beskrevet tidligere.

Den største utfordringen med offline evaluering er å sikre at testdatasettet er omfattende og forblir relevant – agenten kan prestere godt på et fast testsett, men møte svært forskjellige forespørsler i produksjon. Derfor bør du holde testsett oppdatert med nye kanttilfeller og eksempler som speiler virkelige scenarier. En blanding av små “røyk-tester” og større evalueringssett er nyttig: små for raske sjekker og store for bredere ytelsesmetrikker.

### Online Evaluering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering av agenten i et live, reelt miljø, altså under faktisk bruk i produksjon. Online evaluering innebærer å overvåke agentens ytelse på ekte brukerinteraksjoner og kontinuerlig analysere resultater.

For eksempel kan du spore suksessrate, brukertilfredshetsscore eller andre metrikker på live trafikk. Fordelen med online evaluering er at det **fanger opp ting du kanskje ikke forutså i et lab-miljø** – du kan observere modell-drift over tid (hvis agentens effektivitet avtar når inndataendringer skjer) og fange uventede forespørsler eller situasjoner som ikke var i testdataene dine. Den gir et ekte bilde av hvordan agenten oppfører seg i praksis.

Online evaluering involverer ofte innsamling av implisitt og eksplisitt brukerfeedback, som diskutert, og muligens kjøring av shadow-tester eller A/B-tester (hvor en ny agentversjon kjører parallelt for å sammenligne med den gamle). Utfordringen er at det kan være vanskelig å få pålitelige etiketter eller poeng for live-interaksjoner – du kan måtte stole på brukerfeedback eller nedstrøms metrikker (f.eks. om brukeren klikket på resultatet).

### Kombinere de to

Online og offline evalueringer utelukker ikke hverandre; de utfyller hverandre mye. Innsikt fra online overvåking (f.eks. nye typer brukerforespørsler hvor agenten presterer dårlig) kan brukes til å forbedre offline testsett. Tilsvarende kan agenter som presterer godt på offline tester trygt distribueres og overvåkes online.

Mange team følger faktisk denne sløyfen:

_evaluer offline -> distribuer -> overvåk online -> samle nye feiltilfeller -> legg til i offline datasett -> forbedre agent -> gjenta_.

## Vanlige Problemer

Når du distribuerer AI-agenter i produksjon, kan du møte ulike utfordringer. Her er noen vanlige problemer og mulige løsninger:

| **Problem**    | **Potensiell løsning**   |
| ------------- | ------------------ |
| AI-agent som ikke utfører oppgaver konsekvent | - Forbedre prompten gitt til AI-agenten; vær tydelig på mål.<br>- Identifiser hvor oppgaven kan deles opp i deloppgaver og håndteres av flere agenter. |
| AI-agent som kjører i kontinuerlige løkker  | - Sørg for klare avslutningsbetingelser slik at agenten vet når prosessen skal stoppe.<br>- For komplekse oppgaver som krever resonnement og planlegging, bruk en større modell som er spesialisert på dette. |
| AI-agentens verktøyskall fungerer dårlig   | - Test og valider verktøyets output utenfor agentsystemet.<br>- Forbedre definerte parametere, prompts og navngivning av verktøyene.  |
| Multi-agent system som ikke fungerer konsekvent | - Forbedre promptene gitt til hver agent for å sikre at de er spesifikke og forskjellige fra hverandre.<br>- Bygg et hierarkisk system ved å bruke en "routing" eller kontrollagent til å avgjøre hvilken agent som er riktig. |

Mange av disse problemene kan identifiseres mer effektivt med observabilitet på plass. Trace- og metrikdataene vi har diskutert tidligere hjelper deg med å finne nøyaktig hvor i agentens arbeidsflyt problemene oppstår, noe som gjør feilsøking og optimalisering mye mer effektivt.

## Kostnadshåndtering
Her er noen strategier for å håndtere kostnadene ved å distribuere AI-agenter i produksjon:

**Bruke Mindre Modeller:** Små språkmodeller (SLMs) kan fungere godt på visse agentbaserte brukstilfeller og vil redusere kostnadene betydelig. Som nevnt tidligere, er det beste å bygge et evalueringssystem for å bestemme og sammenligne ytelse mot større modeller for å forstå hvor godt en SLM vil prestere på ditt brukstilfelle. Vurder å bruke SLMs for enklere oppgaver som intensjonsklassifisering eller parameteruttrekk, mens du reserverer større modeller for kompleks resonnement.

**Bruke en Router Modell:** En lignende strategi er å bruke en variasjon av modeller og størrelser. Du kan bruke en LLM/SLM eller serverløs funksjon for å rute forespørsler basert på kompleksitet til de mest passende modellene. Dette vil også bidra til å redusere kostnader samtidig som det sikrer ytelse på riktige oppgaver. For eksempel, rute enkle spørsmål til mindre, raskere modeller, og bare bruke dyre store modeller for komplekse resonnementoppgaver.

**Cache Respons:** Å identifisere vanlige forespørsler og oppgaver og levere svarene før de går gjennom agentbasert system er en god måte å redusere volumet av lignende forespørsler. Du kan til og med implementere en flyt for å identifisere hvor lik en forespørsel er med dine bufrede forespørsler ved hjelp av mer grunnleggende AI-modeller. Denne strategien kan betydelig redusere kostnader for ofte stilte spørsmål eller vanlige arbeidsflyter.

## La oss se hvordan dette fungerer i praksis

I [eksempelnotatboken for denne seksjonen](./code_samples/10-expense_claim-demo.ipynb) vil vi se eksempler på hvordan vi kan bruke observasjonsverktøy for å overvåke og evaluere agenten vår.

### Har du flere spørsmål om AI-agenter i produksjon?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortimer og få svar på dine AI-agentspørsmål.

## Forrige leksjon

[Metakognisjon Designmønster](../09-metacognition/README.md)

## Neste leksjon

[Agentiske Protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->