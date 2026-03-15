# AI-agenter i produksjon: Observabilitet og evaluering

[![AI Agents in Production](../../../translated_images/no/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Etter hvert som AI-agenter går fra eksperimentelle prototyper til reelle applikasjoner, blir evnen til å forstå atferden deres, overvåke ytelsen og systematisk evaluere resultatene deres viktig.

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du kan/forstå:
- Grunnleggende begreper om agentobservabilitet og evaluering
- Teknikker for å forbedre ytelsen, kostnader og effektivitet til agenter
- Hva og hvordan du systematisk evaluerer AI-agentene dine
- Hvordan kontrollere kostnader når du setter AI-agenter i produksjon
- Hvordan instrumentere agenter bygget med Microsoft Agent Framework

Målet er å utruste deg med kunnskapen som trengs for å gjøre dine «svarte bokser»-agenter om til transparente, håndterbare og pålitelige systemer.

_**Merk:** Det er viktig å distribuere AI-agenter som er trygge og pålitelige. Sjekk også ut leksjonen [Bygge pålitelige AI-agenter](./06-building-trustworthy-agents/README.md)._

## Spor og segmenter

Observabilitetsverktøy som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerer vanligvis agentkjøringer som spor og segmenter.

- **Spor (Trace)** representerer en fullstendig agentoppgave fra start til slutt (som å håndtere en brukerforespørsel).
- **Segmenter (Spans)** er individuelle trinn innen sporet (som å kalle en språkmodell eller hente data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uten observabilitet kan en AI-agent føles som en «svart boks» – dens interne tilstand og resonnering er ugjennomsiktig, noe som gjør det vanskelig å diagnostisere problemer eller optimalisere ytelsen. Med observabilitet blir agenter «glassbokser» som tilbyr åpenhet som er avgjørende for å bygge tillit og sikre at de opererer som forventet.

## Hvorfor observabilitet er viktig i produksjonsmiljøer

Overgangen av AI-agenter til produksjonsmiljøer introduserer et nytt sett utfordringer og krav. Observabilitet er ikke lenger noe «koselig å ha», men en kritisk egenskap:

*   **Feilsøking og årsaksanalyse**: Når en agent feiler eller produserer uventet output, gir observabilitetsverktøy spor som trengs for å finne feilens kilde. Dette er spesielt viktig i komplekse agenter som kan involvere flere LLM-kall, verktøyinteraksjoner og betinget logikk.
*   **Forsinkelse og kostnadsstyring**: AI-agenter er ofte avhengige av LLM-er og andre eksterne API-er som blir fakturert per token eller per kall. Observabilitet tillater nøyaktig sporing av disse kallene, slik at operasjoner som er for langsomme eller dyre kan identifiseres. Dette gjør at team kan optimalisere prompts, velge mer effektive modeller eller redesigne arbeidsflyter for å håndtere driftskostnader og sikre god brukeropplevelse.
*   **Tillit, sikkerhet og etterlevelse**: I mange applikasjoner er det viktig å sikre at agenter opptrer trygt og etisk. Observabilitet gir en revisjonsspor av agentens handlinger og avgjørelser. Dette kan brukes for å oppdage og begrense problemer som prompt-injeksjon, generering av skadelig innhold eller feilbehandling av personlig identifiserbar informasjon (PII). For eksempel kan du gjennomgå spor for å forstå hvorfor en agent ga et bestemt svar eller brukte et spesifikt verktøy.
*   **Kontinuerlig forbedringssløyfer**: Observabilitetsdata er grunnlaget for en iterativ utviklingsprosess. Ved å overvåke hvordan agenter presterer i den virkelige verden, kan team identifisere forbedringsområder, samle data for finjustering av modeller og validere effekten av endringer. Dette skaper en tilbakemeldingssløyfe hvor produksjonssinnsikt fra online evaluering informerer offline-eksperimentering og raffinering, som fører til stadig bedre agentytelse.

## Nøkkelmetrikker å følge med på

For å overvåke og forstå agentatferd bør en rekke metrikker og signaler følges med på. Selv om spesifikke metrikker kan variere basert på agentens formål, er noen universelt viktige.

Her er noen av de vanligste metrikkene som observabilitetsverktøy overvåker:

**Forsinkelse:** Hvor raskt svarer agenten? Lange ventetider påvirker brukeropplevelsen negativt. Du bør måle forsinkelse for oppgaver og individuelle trinn ved å spore agentkjøringer. For eksempel kan en agent som bruker 20 sekunder på alle modellkall akselereres ved å bruke en raskere modell eller kjøre modellkall parallelt.

**Kostnader:** Hva koster hver agentkjøring? AI-agenter er avhengige av LLM-kall som faktureres per token eller eksterne API-er. Hyppig verktøybruk eller flere prompts kan raskt øke kostnadene. Hvis en agent for eksempel kaller en LLM fem ganger for en marginal kvalitetsforbedring, må du vurdere om kostnaden er berettiget eller om du kan redusere antall kall eller bruke en billigere modell. Realtidsovervåkning kan også hjelpe med å oppdage uventede topper (f.eks. feil som forårsaker overdrevne API-løkker).

**Forespørselsfeil:** Hvor mange forespørsler feilet agenten på? Dette kan inkludere API-feil eller mislykkede verktøykall. For å gjøre agenten mer robust i produksjon, kan du sette opp fallback-mekanismer eller retry-logikk. F.eks. hvis LLM-leverandør A er nede, kan du bytte til LLM-leverandør B som backup.

**Brukertilbakemeldinger:** Å implementere direkte brukerevalueringer gir verdifulle innsikter. Dette kan inkludere eksplisitte vurderinger (👍tommel opp/👎tommel ned, ⭐1-5 stjerner) eller tekstlige kommentarer. Konsistent negativ tilbakemelding bør varsle deg, da dette er et tegn på at agenten ikke fungerer som forventet.

**Implisitt brukertilbakemelding:** Brukeratferd gir indirekte tilbakemelding selv uten eksplisitte vurderinger. Dette kan inkludere umiddelbar omformulering av spørsmål, gjentatte forespørsler eller bruk av en retry-knapp. Hvis du f.eks. ser at brukere gjentatte ganger stiller samme spørsmål, er det et tegn på at agenten ikke fungerer som forventet.

**Nøyaktighet:** Hvor ofte produserer agenten korrekte eller ønskede resultater? Definisjonene av nøyaktighet varierer (f.eks. korrekt problemløsning, informasjonsnøyaktighet, brukertilfredshet). Første steg er å definere hva suksess ser ut som for din agent. Du kan spore nøyaktighet via automatiske sjekker, evalueringspoeng eller fullføringsmerker for oppgaver. For eksempel å merke spor som «lyktes» eller «feilet».

**Automatiserte evalueringsmetrikker:** Du kan også sette opp automatiserte evalueringer. For eksempel kan du bruke en LLM til å score agentens output, f.eks. om den er hjelpsom, nøyaktig eller ikke. Det finnes også flere open source-biblioteker som hjelper deg med scoring av ulike aspekter ved agenten. F.eks. [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://llm-guard.com/) for å oppdage skadelig språkbruk eller prompt-injeksjon.

I praksis gir en kombinasjon av disse metrikkene best dekning av en AI-agent sin helsetilstand. I kapittelets [eksempelnotatbok](./code_samples/10-expense_claim-demo.ipynb) skal vi vise deg hvordan disse metrikene ser ut i virkelige eksempler, men først lærer vi hvordan en typisk evalueringsarbeidsflyt ser ut.

## Instrumenter agenten din

For å samle inn sporingsdata må du instrumentere koden din. Målet er å instrumentere agentkoden for å sende ut spor og metrikker som kan fanges, behandles og visualiseres av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har vokst frem som en industristandard for LLM-observabilitet. Det tilbyr et sett av API-er, SDK-er og verktøy for generering, innsamling og eksport av telemetridata.

Det finnes mange instrumenteringsbiblioteker som pakker inn eksisterende agentrammeverk og gjør det enkelt å eksportere OpenTelemetry-segmenter til observabilitetsverktøy. Microsoft Agent Framework integrerer naturlig med OpenTelemetry. Nedenfor er et eksempel på instrumentering av en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentutførelse spores automatisk
    pass
```

[Eksempelnotatboken](./code_samples/10-expense_claim-demo.ipynb) i dette kapittelet viser hvordan du instrumenterer din MAF-agent.

**Manuell opprettelse av segmenter:** Selv om instrumenteringsbiblioteker gir et godt grunnlag, finnes det ofte tilfeller hvor mer detaljert eller tilpasset informasjon trengs. Du kan manuelt opprette segmenter for å legge til egendefinert applikasjonslogikk. Viktigere er at de kan berike automatisk eller manuelt opprettede segmenter med egendefinerte attributter (også kalt tagger eller metadata). Disse attributtene kan inkludere virksomhetsspesifikke data, mellomregninger eller annen kontekst som kan være nyttig for feilsøking eller analyse, som `user_id`, `session_id` eller `model_version`.

Eksempel på å opprette spor og segmenter manuelt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentevaluering

Observabilitet gir oss metrikker, men evaluering er prosessen med å analysere disse dataene (og utføre tester) for å bestemme hvor godt en AI-agent presterer og hvordan den kan forbedres. Med andre ord: Når du har disse sporene og metrikkene, hvordan bruker du dem til å vurdere agenten og ta beslutninger?

Regelmessig evaluering er viktig fordi AI-agenter ofte er ikke-deterministiske og kan utvikle seg (gjennom oppdateringer eller endret modellatferd) – uten evaluering ville du ikke visst om din «smarte agent» faktisk gjør jobben sin godt eller om den har forverret seg.

Det finnes to kategorier evalueringer for AI-agenter: **online-evaluering** og **offline-evaluering**. Begge er verdifulle og utfyller hverandre. Vi begynner vanligvis med offline-evaluering, siden dette er det minste nødvendige steget før distribusjon av en agent.

### Offline-evaluering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette innebærer å evaluere agenten i et kontrollert miljø, vanligvis ved hjelp av testdatasett, ikke sanntids brukerforespørsler. Du bruker kuraterte datasett hvor du vet hva forventet resultat eller korrekt atferd er, og kjører deretter agenten på disse.

For eksempel, hvis du har bygget en agent for matematiske tekstoppgaver, kan du ha et [testdatasett](https://huggingface.co/datasets/gsm8k) med 100 oppgaver med kjente svar. Offline-evaluering gjøres ofte i utviklingsfasen (og kan inngå i CI/CD-pipelines) for å sjekke forbedringer eller forhindre regresjon. Fordelen er at det er **reproduserbart og du kan få klare nøyaktighetsmetrikker siden du har sannheten**. Du kan også simulere brukerforespørsler og måle agentens svar mot ideelle svar eller bruke automatiserte metrikker som beskrevet over.

Den viktigste utfordringen med offline-evaluering er å sikre at testdatasettet er omfattende og forblir relevant – agenten kan prestere godt på et fast testsett, men møte svært forskjellige forespørsler i produksjon. Derfor bør du holde testsett oppdatert med nye kanttilfeller og eksempler som gjenspeiler virkelige scenarier. En blanding av små «røyktester» og større evalueringssett er nyttig: små sett for raske sjekker og større for bredere ytelsesmetrikker.

### Online-evaluering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering av agenten i et levende, reelt miljø, altså under faktisk bruk i produksjon. Online-evaluering innebærer å overvåke agentens ytelse på reelle brukerinteraksjoner og kontinuerlig analysere resultater.

For eksempel kan du spore suksessrater, brukertilfredshetsscore eller andre metrikker på live trafikk. Fordelen med online-evaluering er at den **fanger opp ting du kanskje ikke kan forutse i et laboratorium** – du kan observere modellforandringer over tid (hvis agentens effektivitet forverres når inputmønstrene endres) og oppdage uventede spørsmål eller situasjoner som ikke var i testdataene. Det gir et ekte bilde av hvordan agenten oppfører seg i virkeligheten.

Online-evaluering involverer ofte innsamling av implisitt og eksplisitt brukertilbakemelding, som diskutert, og eventuelt kjøring av shadow-tester eller A/B-tester (der en ny versjon av agenten kjører parallelt for å sammenligne med den gamle). Utfordringen er at det kan være vanskelig å få pålitelige etiketter eller score for sanntidsinteraksjoner – du må kanskje stole på brukertilbakemeldinger eller nedstrømsmetrikker (som om brukeren klikket resultatet).

### Kombinere de to

Online- og offline-evalueringer utelukker ikke hverandre; de er meget utfyllende. Innsikter fra online-overvåkning (f.eks. nye typer brukerforespørsler hvor agenten presterer dårlig) kan brukes til å utvide og forbedre offline-testdatasett. Omvendt kan agenter som gjør det bra i offline-tester, deretter distribueres med større selvtillit og overvåkes online.

Mange team følger faktisk en sløyfe:

_evaluer offline -> distribuer -> overvåk online -> samle inn nye feiltilfeller -> legg til i offline-datasett -> forbedre agent -> gjenta_.

## Vanlige problemer

Når du setter AI-agenter i produksjon, kan du møte ulike utfordringer. Her er noen vanlige problemer og mulige løsninger:

| **Problem**    | **Mulig løsning**   |
| ------------- | ------------------ |
| AI-agent utfører ikke oppgaver konsekvent | - Forbedre prompten som gis til AI-agenten; vær tydelig på mål.<br>- Identifiser om oppgavene kan deles opp i deloppgaver som håndteres av flere agenter. |
| AI-agent havner i uendelige løkker | - Sørg for tydelige avslutningsbetingelser slik at agenten vet når den skal stoppe prosessen.<br>- For komplekse oppgaver som krever resonnering og planlegging, bruk en større modell spesialisert for slike oppgaver. |
| Verktøyskall fra AI-agenten fungerer ikke godt | - Test og valider verktøyets output utenfor agentsystemet.<br>- Forbedre definerte parametere, prompts og navnsetting av verktøy.  |
| Multi-agent system opptrer inkonsistent | - Forbedre prompts gitt til hver enkelt agent for å sikre at de er spesifikke og distinkte.<br>- Bygg et hierarkisk system med en "ruting"- eller kontrollagent som avgjør hvilken agent som er riktig. |

Mange av disse problemene kan identifiseres mer effektivt med observabilitet på plass. Sporene og metrikkene vi diskuterte tidligere hjelper til med å peke nøyaktig hvor i agentarbeidsflyten problemer oppstår, noe som gjør feilsøking og optimalisering mye mer effektiv.

## Kostnadsstyring
Her er noen strategier for å håndtere kostnadene ved å sette AI-agenter i produksjon:

**Bruke mindre modeller:** Små språkmodeller (SLM) kan prestere godt på visse agentrelaterte bruksområder og vil redusere kostnadene betydelig. Som nevnt tidligere er det beste å bygge et evalueringssystem for å bestemme og sammenligne ytelse mot større modeller for å forstå hvor godt en SLM vil prestere på ditt brukstilfelle. Vurder å bruke SLM-er for enklere oppgaver som intensjonsklassifisering eller parameteruttrekk, samtidig som større modeller reserveres for komplekse resonnementer.

**Bruke en routermodell:** En lignende strategi er å bruke en variasjon av modeller og størrelser. Du kan bruke en LLM/SLM eller serverløs funksjon for å rute forespørsler basert på kompleksitet til best egnede modeller. Dette vil også bidra til å redusere kostnader samtidig som ytelsen sikres på riktige oppgaver. For eksempel, rute enkle forespørsler til mindre, raskere modeller, og kun bruke kostbare store modeller for komplekse resonnementoppgaver.

**Mellomlagring av svar:** Å identifisere vanlige forespørsler og oppgaver og gi svarene før de går gjennom ditt agentiske system er en god måte å redusere volumet av lignende forespørsler på. Du kan til og med implementere et flyt for å identifisere hvor lik en forespørsel er til dine mellomlagrede forespørsler ved å bruke mer grunnleggende AI-modeller. Denne strategien kan betydelig redusere kostnader for ofte stilte spørsmål eller vanlige arbeidsflyter.

## La oss se hvordan dette fungerer i praksis

I [eksempelnottboken for denne delen](./code_samples/10-expense_claim-demo.ipynb) skal vi se eksempler på hvordan vi kan bruke observasjonsverktøy for å overvåke og evaluere agenten vår.


### Har du flere spørsmål om AI-agenter i produksjon?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre som lærer, delta på kontortid og få svar på dine spørsmål om AI-agenter.

## Forrige leksjon

[Metakognisjon Designmønster](../09-metacognition/README.md)

## Neste leksjon

[Agentiske Protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feilfortolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->