# AI Agenter i Produksjon: Observabilitet & Evaluering

[![AI Agents in Production](../../../translated_images/no/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Etter hvert som AI-agenter går fra eksperimentelle prototyper til virkelige applikasjoner, blir evnen til å forstå deres oppførsel, overvåke ytelsen og systematisk evaluere deres resultater viktig.

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan/forstå:
- Kjernebegreper om agentobservabilitet og evaluering
- Teknikkene for å forbedre ytelse, kostnader og effektivitet for agenter
- Hva og hvordan du systematisk evaluerer dine AI-agenter
- Hvordan kontrollere kostnader ved utrulling av AI-agenter i produksjon
- Hvordan instrumentere agenter bygget med Microsoft Agent Framework

Målet er å utstyre deg med kunnskapen til å forvandle dine "svarte bokser" agenter til gjennomsiktige, håndterbare og pålitelige systemer.

_**Merk:** Det er viktig å distribuere AI-agenter som er trygge og pålitelige. Ta også en titt på [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md) leksjonen._

## Spor og Spenn

Observabilitetsverktøy som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerer vanligvis agentkjøringer som spor og spenn.

- **Spor (Trace)** representerer en fullstendig agentoppgave fra start til slutt (som å håndtere en brukerforespørsel).
- **Spenn (Spans)** er individuelle steg innen sporet (som å kalle et språkmodell eller hente data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uten observabilitet kan en AI-agent føles som en "svart boks" – dens interne tilstand og resonnement er uklare, noe som gjør det vanskelig å diagnostisere problemer eller optimalisere ytelsen. Med observabilitet blir agenter "glassbokser", som gir transparens som er avgjørende for å bygge tillit og sikre at de fungerer som tiltenkt.

## Hvorfor observabilitet er viktig i produksjonsmiljøer

Overføringen av AI-agenter til produksjonsmiljøer introduserer et nytt sett utfordringer og krav. Observabilitet er ikke lenger et "hyggelig å ha", men en kritisk kapasitet:

*   **Feilsøking og Rotårsaksanalyse**: Når en agent feiler eller gir et uventet resultat, gir observabilitetsverktøyene sporene som trengs for å finne kilden til feilen. Dette er spesielt viktig i komplekse agenter som kan involvere flere LLM-kall, verktøyinteraksjoner og betinget logikk.
*   **Latens og Kostnadsstyring**: AI-agenter er ofte avhengige av LLM-er og andre eksterne API-er som faktureres per token eller per kall. Observabilitet tillater presis sporing av disse kallene, noe som hjelper å identifisere operasjoner som er unødvendig langsomme eller dyre. Dette gjør team i stand til å optimalisere prompts, velge mer effektive modeller eller redesigne arbeidsflyter for å styre driftskostnader og sikre en god brukeropplevelse.
*   **Tillitt, Sikkerhet og Overholdelse**: I mange applikasjoner er det viktig å sikre at agenter oppfører seg trygt og etisk. Observabilitet gir en revisjonsspor av agenthandlinger og avgjørelser. Dette kan brukes til å oppdage og begrense problemer som prompt-injeksjon, generering av skadelig innhold, eller feilbehandling av personlig identifiserbar informasjon (PII). For eksempel kan du gjennomgå spor for å forstå hvorfor en agent ga et bestemt svar eller brukte et spesifikt verktøy.
*   **Kontinuerlige Forbedringssløyfer**: Observabilitetsdata er grunnlaget for en iterativ utviklingsprosess. Ved å overvåke hvordan agenter presterer i den virkelige verden, kan team identifisere forbedringsområder, samle data for finjustering av modeller, og validere effekten av endringer. Dette skaper en tilbakemeldingssløyfe hvor produksjonsinnsikter fra online evaluering informerer offline eksperimentering og forbedring, noe som leder til stadig bedre agentytelse.

## Viktige metrikker å spore

For å overvåke og forstå agentens oppførsel bør en rekke metrikker og signaler følges. Mens spesifikke metrikker kan variere basert på agentens formål, er noen universelt viktige.

Her er noen av de vanligste metrikker som observabilitetsverktøy overvåker:

**Latens:** Hvor raskt svarer agenten? Lange ventetider påvirker brukeropplevelsen negativt. Du bør måle latens for oppgaver og individuelle steg ved å spore agentkjøringer. For eksempel, en agent som bruker 20 sekunder på alle modellkall kan akselereres ved å bruke en raskere modell eller kjøre modellkall parallelt.

**Kostnader:** Hva koster en agentkjøring? AI-agenter er avhengige av LLM-kall fakturert per token eller eksterne API-er. Hyppig verktøybruk eller flere prompts kan raskt øke kostnadene. For eksempel, hvis en agent kaller en LLM fem ganger for marginal forbedring av kvalitet, må du vurdere om kostnaden er berettiget eller om du kan redusere antall kall eller bruke en billigere modell. Sanntidsovervåking kan også hjelpe med å identifisere uventede topper (f.eks. feil som forårsaker overdreven API-løkker).

**Forespørselsfeil:** Hvor mange forespørsler mislyktes agenten i? Dette kan inkludere API-feil eller mislykkede verktøykall. For å gjøre agenten mer robust mot disse i produksjon kan du da sette opp fallback-løsninger eller nye forsøk. F.eks. hvis LLM-leverandør A er nede, bytter du til LLM-leverandør B som backup.

**Brukerfeedback:** Implementering av direkte brukervurderinger gir verdifulle innsikter. Dette kan inkludere eksplisitte vurderinger (👍 tommel opp/👎 tommel ned, ⭐1-5 stjerner) eller tekstlige kommentarer. Konsistent negativ feedback bør varsle deg, da dette er et tegn på at agenten ikke fungerer som forventet.

**Implicit brukerfeedback:** Brukeratferd gir indirekte tilbakemeldinger selv uten eksplisitte vurderinger. Dette kan inkludere umiddelbar omformulering av spørsmål, gjentatte spørringer eller klikk på en prøv igjen-knapp. F.eks. hvis du ser at brukere gjentatte ganger spør samme spørsmål, er dette et tegn på at agenten ikke fungerer som forventet.

**Nøyaktighet:** Hvor ofte produserer agenten korrekte eller ønskelige resultater? Definisjoner av nøyaktighet varierer (eks. korrekt problemløsning, informasjonssøkets nøyaktighet, brukertilfredshet). Det første skrittet er å definere hva suksess er for din agent. Du kan spore nøyaktighet via automatiserte sjekker, evalueringspoengsummer eller oppgavefullføringsetiketter. For eksempel å merke spor som "lyktes" eller "feilet".

**Automatiserte evalueringsmetrikker:** Du kan også sette opp automatiserte evalueringer. For eksempel kan du bruke en LLM for å skåre agentens output om den er hjelpsom, nøyaktig eller ikke. Det finnes også flere open source-biblioteker som hjelper deg med å skåre ulike aspekter av agenten. F.eks. [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://llm-guard.com/) for å oppdage skadelig språk eller prompt-injeksjon. 

I praksis gir en kombinasjon av disse metrikker best dekning av en AI-agents helse. I dette kapitlets [eksempelnotatbok](./code_samples/10-expense_claim-demo.ipynb) vil vi vise hvordan disse metrikker ser ut i virkelige eksempler, men først skal vi lære hvordan en typisk evalueringsarbeidsflyt ser ut.

## Instrumenter agenten din

For å samle sporingsdata må du instrumentere koden din. Målet er å instrumentere agentkoden til å sende ut spor og metrikker som kan fanges, bearbeides og visualiseres av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har blitt en industristandard for LLM-observabilitet. Den tilbyr API-er, SDK-er og verktøy for å generere, samle inn og eksportere telemetridata. 

Det finnes mange instrumenteringsbiblioteker som omslutter eksisterende agentrammeverk og gjør det enkelt å eksportere OpenTelemetry-spenn til et observabilitetsverktøy. Microsoft Agent Framework integrerer naturlig med OpenTelemetry. Nedenfor er et eksempel på å instrumentere en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentutførelse spores automatisk
    pass
```

[Eksempelnotatboken](./code_samples/10-expense_claim-demo.ipynb) i dette kapittelet vil demonstrere hvordan du instrumenterer din MAF-agent.

**Manuell oppretting av spenn:** Mens instrumenteringsbiblioteker gir en god basis, er det ofte tilfeller hvor mer detaljert eller tilpasset informasjon er nødvendig. Du kan manuelt lage spenn for å legge til tilpasset applikasjonslogikk. Viktigere er at du kan berike automatisk eller manuelt opprettede spenn med egendefinerte attributter (også kjent som tagger eller metadata). Disse attributtene kan inkludere forretningsspesifikke data, mellomregninger eller kontekst som kan være nyttig for feilsøking eller analyse, slik som `user_id`, `session_id` eller `model_version`.

Eksempel på å manuelt opprette spor og spenn med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent Evaluering

Observabilitet gir oss metrikker, men evaluering er prosessen med å analysere disse dataene (og utføre tester) for å avgjøre hvor godt en AI-agent presterer og hvordan den kan forbedres. Med andre ord, når du har de sporene og metrikker, hvordan bruker du dem til å vurdere agenten og ta beslutninger? 

Regelmessig evaluering er viktig fordi AI-agenter ofte er ikke-deterministiske og kan utvikle seg (gjennom oppdateringer eller modells drift) – uten evaluering ville du ikke vite om din "smarte agent" faktisk gjør jobben sin godt eller om den har regressert.

Det finnes to kategorier evalueringer for AI-agenter: **online evaluering** og **offline evaluering**. Begge er verdifulle og utfyller hverandre. Vi begynner vanligvis med offline evaluering, da dette er minimum nødvendig steg før utrulling av en agent.

### Offline evaluering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette innebærer å evaluere agenten i et kontrollert miljø, vanligvis ved å bruke testdatasett, ikke live brukerforespørsler. Du bruker kuraterte datasett hvor du vet hva forventet resultat eller korrekt oppførsel er, og deretter kjører agenten på disse. 

For eksempel, hvis du har bygget en agent for matteordoppgaver, kan du ha et [testdatasett](https://huggingface.co/datasets/gsm8k) med 100 problemer med kjente svar. Offline evaluering gjøres ofte under utvikling (og kan være en del av CI/CD-pipelines) for å sjekke forbedringer eller unngå regresjoner. Fordelen er at det er **gjentakbart, og du kan få klare nøyaktighetsmetrikker siden du har sannheten**. Du kan også simulere brukerforespørsler og måle agentens svar mot ideelle svar eller bruke automatiserte metrikker som beskrevet ovenfor.

Den viktigste utfordringen med offline evaluering er å sikre at testdatasettet ditt er omfattende og forblir relevant – agenten kan prestere godt på et fast testsett, men møte helt andre forespørsler i produksjon. Derfor bør du holde testsett oppdatert med nye kanttilfeller og eksempler som reflekterer virkelige scenarier. En blanding av små "røyk-test" saker og større evalueringssett er nyttig: små sett for raske sjekker og større for bredere ytelsesmetrikker.

### Online evaluering 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering av agenten i et live, virkelighetsbasert miljø, altså under faktisk bruk i produksjon. Online evaluering innebærer å overvåke agentens ytelse på virkelige brukerinteraksjoner og kontinuerlig analysere resultater.

Du kan for eksempel spore suksessrater, brukertilfredshets-score eller andre metrikker på live trafikk. Fordelen med online evaluering er at det **fanger opp ting du kanskje ikke kan forutse i et laboratoriemiljø** – du kan observere modellavvik over tid (hvis agentens effekt forverres når inputmønstre endres) og oppdage uventede spørsmål eller situasjoner som ikke var i testdataene. Det gir et sant bilde av hvordan agenten oppfører seg i naturen.

Online evaluering innebærer ofte innsamling av implisitt og eksplisitt brukerfeedback, som diskutert, og muligens kjøring av skyggetester eller A/B-tester (hvor en ny versjon av agenten kjører parallelt for sammenligning med den gamle). Utfordringen er at det kan være vanskelig å få pålitelige etiketter eller score for live-interaksjoner – du kan måtte stole på brukerfeedback eller nedstrøms metrikker (som om brukeren klikket på resultatet).

### Kombinere de to

Online og offline evalueringer er ikke gjensidig ekskluderende; de utfyller hverandre godt. Innsikter fra online overvåking (f.eks. nye typer brukerforespørsler der agenten presterer dårlig) kan brukes til å forbedre og utvide offline testdatasett. Omvendt kan agenter som presterer godt i offline tester trygt distribueres og overvåkes online.

Mange team adopterer faktisk en sløyfe:

_evaluer offline -> distribuer -> overvåk online -> samle nye feiltilfeller -> legg til i offline datasett -> forbedre agent -> gjenta_.

## Vanlige problemer

Når du distribuerer AI-agenter i produksjon, kan du møte ulike utfordringer. Her er noen vanlige problemer og deres potensielle løsninger:

| **Problem**    | **Potensiell løsning**   |
| ------------- | ------------------ |
| AI-agenten utfører ikke oppgaver konsekvent | - Forbedre prompten gitt til AI-agenten; vær tydelig på mål.<br>- Identifiser hvor oppgaver kan deles inn i deloppgaver og håndteres av flere agenter. |
| AI-agenten havner i kontinuerlige løkker  | - Sørg for klare avslutningsvilkår slik at agenten vet når prosessen skal stoppe.<br>- For komplekse oppgaver som krever resonnement og planlegging, bruk en større modell som er spesialisert for slike oppgaver. |
| AI-agentens verktøykall fungerer ikke bra   | - Test og valider verktøyets output utenfor agentsystemet.<br>- Forbedre definerte parametere, prompts og navn på verktøy.  |
| Multi-agent system presterer inkonsistent | - Forbedre prompts gitt til hver agent slik at de er spesifikke og tydelig adskilte.<br>- Bygg et hierarkisk system ved å bruke en "ruting"- eller kontrollagent for å avgjøre hvilken agent som er riktig. |

Mange av disse problemene kan identifiseres mer effektivt med observabilitet på plass. Sporene og metrikker vi diskuterte tidligere hjelper med å fastslå akkurat hvor i agentens arbeidsflyt problemer oppstår, noe som gjør feilsøking og optimalisering mye mer effektivt.

## Kostnadsstyring


Her er noen strategier for å håndtere kostnadene ved å implementere AI-agenter i produksjon:

**Bruke Mindre Modeller:** Små språklige modeller (SLM) kan fungere godt for visse agentbaserte bruksområder og vil redusere kostnadene betydelig. Som nevnt tidligere, er det beste å bygge et evalueringssystem for å fastslå og sammenligne ytelsen kontra større modeller for å forstå hvor godt en SLM vil prestere i ditt bruksområde. Vurder å bruke SLM-er for enklere oppgaver som intensjonsklassifisering eller parameteruttrekk, mens du reserverer større modeller for kompleks resonnement.

**Bruke en Ruter-modell:** En lignende strategi er å bruke en variasjon av modeller og størrelser. Du kan bruke en LLM/SLM eller serverløs funksjon til å rute forespørsler basert på kompleksitet til de best egnede modellene. Dette vil også hjelpe med å redusere kostnader samtidig som ytelsen på de riktige oppgavene sikres. For eksempel, rute enkle forespørsler til mindre, raskere modeller, og bare bruke dyre store modeller til komplekse resonnementoppgaver.

**Caching av Svar:** Å identifisere vanlige forespørsler og oppgaver og gi svar før de går gjennom ditt agentbaserte system er en god måte å redusere mengden av lignende forespørsler. Du kan til og med implementere en flyt for å identifisere hvor lik en forespørsel er til dine hurtigbufrede svar ved å bruke enklere AI-modeller. Denne strategien kan betydelig redusere kostnader for ofte stilte spørsmål eller vanlige arbeidsflyter.

## La oss se hvordan dette fungerer i praksis

I [eksempel-notatboken i denne seksjonen](./code_samples/10-expense_claim-demo.ipynb) skal vi se eksempler på hvordan vi kan bruke observasjonsverktøy for å overvåke og evaluere agenten vår.


### Har du flere spørsmål om AI-agenter i produksjon?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på dine spørsmål om AI-agenter.

## Forrige leksjon

[Metakognisjonsdesignmønster](../09-metacognition/README.md)

## Neste leksjon

[Agentiske Protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->