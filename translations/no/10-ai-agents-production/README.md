# AI-agenter i produksjon: Observerbarhet & evaluering

[![AI Agents in Production](../../../translated_images/no/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Når AI-agenter går fra å være eksperimentelle prototyper til virkelige applikasjoner, blir evnen til å forstå oppførselen deres, overvåke ytelsen og systematisk evaluere resultatene deres viktig.

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan/forstå:
- Kjernebegreper for agentobserverbarhet og evaluering
- Teknikker for å forbedre ytelsen, kostnadene og effektiviteten til agenter
- Hva og hvordan du systematisk evaluerer AI-agentene dine
- Hvordan kontrollere kostnader ved utrulling av AI-agenter i produksjon
- Hvordan instrumentere agenter bygget med Microsoft Agent Framework

Målet er å utstyre deg med kunnskapen for å forvandle dine "svarte bokser" til transparente, håndterbare og pålitelige systemer.

_**Merk:** Det er viktig å distribuere AI-agenter som er trygge og pålitelige. Sjekk også ut leksjonen [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Spor og Spenn

Observerbarhetsverktøy som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerer vanligvis agentkjøringer som spor og spenn.

- **Spor** representerer en fullstendig agentoppgave fra start til slutt (som å håndtere en brukerforespørsel).
- **Spenn** er individuelle steg innenfor sporet (som å kalle et språkmodell eller hente data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uten observerbarhet kan en AI-agent føles som en "svart boks" – dens interne tilstand og resonnering er uklar, noe som gjør det vanskelig å diagnostisere problemer eller optimalisere ytelsen. Med observerbarhet blir agenter "glassbokser", som tilbyr gjennomsiktighet som er avgjørende for å bygge tillit og sikre at de opererer som forventet.

## Hvorfor observerbarhet er viktig i produksjonsmiljøer

Overgangen til produksjonsmiljøer for AI-agenter introduserer nye utfordringer og krav. Observerbarhet er ikke lenger en "hyggelig å ha"-funksjon, men en kritisk kapasitet:

*   **Feilsøking og rotårsaksanalyse**: Når en agent feiler eller produserer et uventet resultat, gir observerbarhetsverktøyene de nødvendige sporene for å identifisere feilens kilde. Dette er spesielt viktig i komplekse agenter som kan involvere flere LLM-kall, verktøyinteraksjoner og betinget logikk.
*   **Forsinkelse og kostnadsstyring**: AI-agenter er ofte avhengige av LLM-er og andre eksterne API-er som faktureres per token eller per kall. Observerbarhet gir presis sporing av disse kallene, og hjelper til med å identifisere operasjoner som er unødig trege eller dyre. Dette gjør det mulig for team å optimalisere spørsmål, velge mer effektive modeller eller redesigne arbeidsflyter for å håndtere driftskostnader og sikre en god brukeropplevelse.
*   **Tillit, sikkerhet og etterlevelse**: I mange applikasjoner er det viktig å sikre at agenter oppfører seg trygt og etisk. Observerbarhet gir en revisjonsspor av agentens handlinger og beslutninger. Dette kan brukes til å oppdage og motvirke problemer som prompt-injeksjon, generering av skadelig innhold eller feilbehandling av personlig identifiserbar informasjon (PII). For eksempel kan du gjennomgå spor for å forstå hvorfor en agent ga et bestemt svar eller brukte et spesifikt verktøy.
*   **Kontinuerlige forbedringssløyfer**: Observerbarhetsdata er grunnlaget for en iterativ utviklingsprosess. Ved å overvåke hvordan agenter presterer i praksis, kan team identifisere forbedringsområder, samle data for finjustering av modeller og validere effekten av endringer. Dette skaper en tilbakemeldingssløyfe hvor produksjonsinnsikter fra online evaluering informerer offline eksperimentering og forbedring, noe som leder til gradvis bedre ytelse for agentene.

## Nøkkelmetrikker å følge med på

For å overvåke og forstå agentens oppførsel bør et bredt spekter av metrikker og signaler spores. Selv om de spesifikke metrikker kan variere basert på agentens formål, er noen universelt viktige.

Her er noen av de vanligste metrikker som observerbarhetsverktøy overvåker:

**Forsinkelse (Latency):** Hvor raskt svarer agenten? Lange ventetider påvirker brukeropplevelsen negativt. Du bør måle forsinkelse for oppgaver og individuelle steg ved å spore agentkjøringer. For eksempel kan en agent som bruker 20 sekunder på alle modellkall akselereres ved å bruke en raskere modell eller ved å kjøre modellkall parallelt.

**Kostnader:** Hva er kostnaden per agentkjøring? AI-agenter er avhengige av LLM-kall som faktureres per token eller eksterne API-er. Hyppig bruk av verktøy eller flere spørsmål kan raskt øke kostnadene. Hvis en agent for eksempel kaller en LLM fem ganger for en marginal kvalitetsforbedring, må du vurdere om kostnaden er berettiget, eller om du kan redusere antall kall eller bruke en billigere modell. Sanntidsovervåking kan også hjelpe med å identifisere uventede spisser (f.eks. feil som forårsaker overdrevne API-løkker).

**Forespørselsfeil:** Hvor mange forespørsler feilet agenten på? Dette kan inkludere API-feil eller mislykkede verktøykall. For å gjøre agenten mer robust mot disse i produksjon, kan du sette opp fallback-mekanismer eller forsøk på nytt. F.eks. hvis LLM-leverandør A er nede, bytter du til LLM-leverandør B som reserve.

**Brukertilbakemelding:** Implementering av direkte brukervurderinger gir verdifulle innsikter. Dette kan inkludere eksplisitte rangeringer (👍tommel opp/👎ned, ⭐1-5 stjerner) eller tekstkommentarer. Konsistent negativ tilbakemelding bør varsle deg, da dette er et tegn på at agenten ikke fungerer som forventet.

**Implisitt brukertilbakemelding:** Brukeratferd gir indirekte tilbakemeldinger selv uten eksplisitte rangeringer. Dette kan være umiddelbar omformulering av spørsmål, gjentatte forespørsler eller å klikke på en prøv igjen-knapp. F.eks. om du ser at brukere gjentatte ganger stiller samme spørsmål, er dette et tegn på at agenten ikke fungerer som forventet.

**Nøyaktighet:** Hvor ofte produserer agenten korrekte eller ønskelige resultater? Nøyaktighetsdefinisjoner varierer (f.eks. korrekthet i problemløsing, nøyaktighet i informasjonsinnhenting, brukertilfredshet). Første steg er å definere hva suksess ser ut som for agenten din. Du kan spore nøyaktighet via automatiske sjekker, evalueringspoeng eller oppgavefullføringsmerker. For eksempel å merke spor som "lyktes" eller "feilet".

**Automatiserte evalueringsmetrikker:** Du kan også sette opp automatiske evalueringsrutiner. For eksempel kan du bruke en LLM til å score agentens output, f.eks. om det er hjelpsomt, nøyaktig eller ikke. Det finnes også flere open source-biblioteker som hjelper med å score ulike aspekter av agenten. F.eks. [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://llm-guard.com/) for å oppdage skadelig språk eller prompt-injeksjon.

I praksis gir en kombinasjon av disse metrikker best dekning av en AI-agent sin helsetilstand. I dette kapitlets [eksempelnotatbok](./code_samples/10-expense_claim-demo.ipynb) vil vi vise deg hvordan disse metrikker ser ut i virkelige eksempler, men først skal vi lære hvordan en typisk evalueringsarbeidsflyt ser ut.

## Instrumenter agenten din

For å samle inn sporingsdata må du instrumentere koden. Målet er å instrumentere agentkoden slik at den avgir spor og metrikker som kan fanges opp, behandles og visualiseres av en observerbarhetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har blitt en industristandard for LLM-observerbarhet. Det gir et sett med API-er, SDK-er og verktøy for å generere, samle inn og eksportere telemetridata.

Det finnes mange instrumenteringsbiblioteker som pakker inn eksisterende agent-rammeverk og gjør det enkelt å eksportere OpenTelemetry-spenn til et observerbarhetsverktøy. Microsoft Agent Framework integreres med OpenTelemetry innfødt. Nedenfor er et eksempel på instrumentering av en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentutførelse spores automatisk
    pass
```

[Eksempelnotatboken](./code_samples/10-expense_claim-demo.ipynb) i dette kapitlet vil demonstrere hvordan du instrumenterer din MAF-agent.

**Manuell opprettelse av spenn:** Selv om instrumenteringsbiblioteker gir et godt grunnlag, finnes det ofte tilfeller hvor mer detaljerte eller tilpassede opplysninger trengs. Du kan manuelt opprette spenn for å legge til egendefinert applikasjonslogikk. Viktigst er at de kan berike automatisk eller manuelt opprettede spenn med egendefinerte attributter (også kjent som tags eller metadata). Disse attributtene kan inkludere forretningsspesifikke data, mellomliggende beregninger eller hvilken som helst kontekst som kan være nyttig ved feilsøking eller analyse, som `user_id`, `session_id` eller `model_version`.

Eksempel på å manuelt opprette spor og spenn med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentevaluering

Observerbarhet gir oss metrikker, men evaluering er prosessen med å analysere disse dataene (og utføre tester) for å avgjøre hvor godt en AI-agent presterer og hvordan den kan forbedres. Med andre ord, når du har de sporene og metrikker, hvordan bruker du dem til å bedømme agenten og ta beslutninger?

Regelmessig evaluering er viktig fordi AI-agenter ofte er ikke-deterministiske og kan utvikle seg (gjennom oppdateringer eller endringer i modellens oppførsel) – uten evaluering ville du ikke vite om din "smarte agent" faktisk gjør jobben sin godt eller om den har forverret seg.

Det finnes to kategorier evaluering for AI-agenter: **online evaluering** og **offline evaluering**. Begge er verdifulle, og de utfyller hverandre. Vi starter vanligvis med offline evaluering, da dette er minimum nødvendig steg før deployering av noen agent.

### Offline evaluering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette innebærer å evaluere agenten i et kontrollert miljø, vanligvis ved å bruke testdatasett, ikke levende brukerforespørsler. Du bruker kuraterte datasett hvor du vet hva forventet output eller korrekt oppførsel er, for deretter å kjøre agenten på disse.

For eksempel, om du har bygget en agent for matematiske tekstoppgaver, kan du ha et [testdatasett](https://huggingface.co/datasets/gsm8k) med 100 problemer med kjente svar. Offline evaluering gjøres ofte under utvikling (og kan være del av CI/CD-pipelines) for å sjekke forbedringer eller forhindre regresjoner. Fordelen er at det er **reproduserbart og du får klare nøyaktighetsmetrikker fordi du har jord-sannheten**. Du kan også simulere brukerforespørsler og måle agentens svar mot ideelle svar eller bruke automatiserte metrikker som beskrevet ovenfor.

Den viktigste utfordringen med offline evaluering er å sørge for at testdatasettet ditt er omfattende og forblir relevant – agenten kan prestere godt på et fast testssett, men møte svært forskjellige forespørsler i produksjon. Derfor bør du holde testsett oppdatert med nye grensesnittstilfeller og eksempler som reflekterer virkelige scenarier. En blanding av små "røyktester" og større evalueringssett er nyttig: små sett for raske kontroller og større for bredere ytelsesmetrikker.

### Online evaluering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering av agenten i et live, virkelighetsnært miljø, altså under faktisk bruk i produksjon. Online evaluering innebærer å overvåke agentens ytelse på ekte brukerinteraksjoner og kontinuerlig analysere resultater.

For eksempel kan du spore suksessrater, brukertilfredshetspoeng eller andre metrikker på live trafikk. Fordelen med online evaluering er at den **fanger opp ting du kanskje ikke forventer i et laboratoriemiljø** – du kan observere modellforskyvning over tid (hvis agentens effektivitet svekkes etter hvert som inndatastrukturer skifter) og oppdage uventede forespørsler eller situasjoner som ikke var i testdataene dine. Det gir et ekte bilde av hvordan agenten oppfører seg ute i felt.

Online evaluering innebærer ofte å samle både implisitt og eksplisitt brukertilbakemelding, som diskutert, og eventuelt kjøre skyggespill eller A/B-tester (der en ny versjon av agenten kjører parallelt for å sammenligne med den gamle). Utfordringen er at det kan være vanskelig å få pålitelige merkelapper eller score for live interaksjoner – du kan måtte stole på brukertilbakemelding eller nedstrøms metrikker (som om brukeren klikket på resultatet).

### Kombinere de to

Online og offline evaluering er ikke gjensidig utelukkende; de utfyller hverandre godt. Innsikter fra online overvåking (f.eks. nye typer brukerforespørsler der agenten presterer dårlig) kan brukes til å utvide og forbedre offline testdatasett. Omvendt kan agenter som presterer godt på offline tester trygt deployeres og overvåkes online.

Faktisk adopterer mange team en sløyfe:

_evaluer offline -> deployer -> overvåk online -> samle nye feilstilfeller -> legg til i offline-datasett -> forbedre agent -> gjenta_.

## Vanlige problemer

Når du deployerer AI-agenter til produksjon, kan du møte ulike utfordringer. Her er noen vanlige problemer og potensielle løsninger:

| **Problem**    | **Potensiell løsning**   |
| ------------- | ------------------ |
| AI-agent presterer ikke oppgavene konsekvent | - Forbedre prompten gitt til AI-agenten; vær tydelig på mål.<br>- Identifiser om oppgavene kan deles opp i deloppgaver håndtert av flere agenter. |
| AI-agent går inn i kontinuerlige løkker | - Sørg for klare avslutningsbetingelser slik at agenten vet når prosessen skal stoppes.<br>- For komplekse oppgaver som krever resonnering og planlegging, bruk en større modell spesialisert for slike oppgaver. |
| AI-agentens verktøykall fungerer ikke som forventet | - Test og valider verktøyets output utenfor agentsystemet.<br>- Forbedre definerte parametere, prompt og navn på verktøyene. |
| Multi-agent system presterer inkonsekvent | - Forbedre promptene gitt til hver agent for å sikre at de er spesifikke og ulike.<br>- Bygg et hierarkisk system med en "ruting" eller kontrollagent som bestemmer hvilken agent som er riktig. |

Mange av disse problemene kan identifiseres mer effektivt med observerbarhet på plass. Sporene og metrikker vi diskuterte tidligere hjelper til med å nøyaktig identifisere hvor i agentens arbeidsflyt problemene oppstår, noe som gjør feilsøking og optimalisering mye mer effektivt.

## Kostnadsstyring


Her er noen strategier for å håndtere kostnadene ved å distribuere AI-agenter i produksjon:

**Bruke Mindre Modeller:** Små språkmodeller (SLMs) kan fungere godt på visse agentiske bruksområder og vil redusere kostnadene betydelig. Som nevnt tidligere er det beste måten å bygge et evalueringssystem for å bestemme og sammenligne ytelse mot større modeller, for å forstå hvor godt en SLM vil fungere på ditt brukstilfelle. Vurder å bruke SLM-er for enklere oppgaver som intensjonsklassifisering eller parameterutvinning, samtidig som større modeller reserveres for kompleks resonnering.

**Bruke en Router-modell:** En lignende strategi er å bruke en variasjon av modeller og størrelser. Du kan bruke en LLM/SLM eller serverløs funksjon for å rute forespørsler basert på kompleksitet til de best egnede modellene. Dette vil også bidra til å redusere kostnader samtidig som det sikrer ytelse på riktige oppgaver. For eksempel, ruter du enkle forespørsler til mindre, raskere modeller, og bruker bare dyre store modeller for komplekse resonneringsoppgaver.

**Cache-responser:** Å identifisere vanlige forespørsler og oppgaver og tilby svarene før de går gjennom ditt agentiske system, er en god måte å redusere volumet av lignende forespørsler på. Du kan til og med implementere en flyt for å identifisere hvor lik en forespørsel er med dine cachede forespørsler ved hjelp av mer grunnleggende AI-modeller. Denne strategien kan betydelig redusere kostnader for ofte stilte spørsmål eller vanlige arbeidsflyter.

## La oss se hvordan dette fungerer i praksis

I [eksempel-notatboken for denne delen](./code_samples/10-expense_claim-demo.ipynb), vil vi se eksempler på hvordan vi kan bruke observasjonsverktøy for å overvåke og evaluere agenten vår.


### Har du flere spørsmål om AI-agenter i produksjon?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på dine spørsmål om AI-agenter.

## Forrige leksjon

[Metakognisjon Designmønster](../09-metacognition/README.md)

## Neste leksjon

[Agentiske protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->