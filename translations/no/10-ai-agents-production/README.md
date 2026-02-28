# AI-agenter i produksjon: Observabilitet og evaluering

[![AI Agents in Production](../../../translated_images/no/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Etter hvert som AI-agenter går fra eksperimentelle prototyper til virkelige applikasjoner, blir evnen til å forstå deres oppførsel, overvåke ytelsen og systematisk evaluere resultatene viktig.

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du kan/forstå:
- Kjernbegreper for agentobservabilitet og evaluering
- Teknikker for å forbedre ytelsen, kostnadene og effektiviteten til agenter
- Hva og hvordan du systematisk evaluerer AI-agentene dine
- Hvordan kontrollere kostnader ved utrulling av AI-agenter i produksjon
- Hvordan instrumentere agenter bygget med Microsoft Agent Framework

Målet er å gi deg kunnskapen til å transformere dine "black box"-agenter til transparente, håndterbare og pålitelige systemer.

_**Merk:** Det er viktig å distribuere AI-agenter som er trygge og pålitelige. Sjekk også ut leksjonen [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Spor og spenner

Observabilitetsverktøy som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerer vanligvis agentkjøringer som spor (traces) og spenner (spans).

- **Trace** representerer en komplett agentoppgave fra start til slutt (som å håndtere en brukerforespørsel).
- **Spans** er individuelle steg innenfor sporet (som å kalle et språkmodell eller hente data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Uten observabilitet kan en AI-agent føles som en "black box" – dens interne tilstand og resonnering er ugjennomsiktige, noe som gjør det vanskelig å diagnostisere problemer eller optimalisere ytelsen. Med observabilitet blir agenter "glasskasser" som tilbyr gjennomsiktighet som er avgjørende for å bygge tillit og sikre at de fungerer som forventet.

## Hvorfor observabilitet er viktig i produksjonsmiljøer

Overgangen av AI-agenter til produksjonsmiljøer introduserer et nytt sett med utfordringer og krav. Observabilitet er ikke lenger et "hyggelig å ha", men en kritisk evne:

*   **Feilsøking og årsaksanalyse**: Når en agent mislykkes eller produserer et uventet resultat, gir observabilitetsverktøy spor som trengs for å lokalisere kilden til feilen. Dette er spesielt viktig i komplekse agenter som kan involvere flere LLM-kall, verktøysinteraksjoner og betinget logikk.
*   **Latens- og kostnadsstyring**: AI-agenter er ofte avhengige av LLM-er og andre eksterne API-er som faktureres per token eller per kall. Observabilitet tillater presis sporing av disse kallene, noe som hjelper med å identifisere operasjoner som er for langsomme eller dyre. Dette gjør det mulig for team å optimalisere prompts, velge mer effektive modeller eller redesigne arbeidsflyter for å håndtere driftskostnader og sikre god brukeropplevelse.
*   **Tillitt, sikkerhet og etterlevelse**: I mange applikasjoner er det viktig å sikre at agenter oppfører seg trygt og etisk. Observabilitet gir en revisjonsspor av agenthandlinger og beslutninger. Dette kan brukes til å oppdage og dempe problemer som promptinjeksjon, generering av skadelig innhold eller feilbehandling av personlig identifiserbar informasjon (PII). For eksempel kan du gjennomgå spor for å forstå hvorfor en agent ga et bestemt svar eller brukte et spesifikt verktøy.
*   **Kontinuerlige forbedringssløyfer**: Observabilitetsdata er grunnlaget for en iterativ utviklingsprosess. Ved å overvåke hvordan agenter presterer i virkeligheten, kan team identifisere forbedringsområder, samle data for finjustering av modeller og validere effekten av endringer. Dette skaper en tilbakemeldingssløyfe hvor produksjonsinnsikt fra online evaluering informerer offline eksperimentering og forbedring, som fører til stadig bedre agentytelse.

## Viktige mål å spore

For å overvåke og forstå agentatferd bør en rekke metrikker og signaler spores. Selv om de spesifikke metrikker kan variere basert på agentens formål, er noen universelt viktige.

Her er noen av de vanligste metrikker som observabilitetsverktøy overvåker:

**Latens:** Hvor raskt svarer agenten? Lange ventetider påvirker brukeropplevelsen negativt. Du bør måle latens for oppgaver og individuelle steg ved å spore agentkjøringer. For eksempel kan en agent som bruker 20 sekunder på alle modellkall akselereres ved å bruke en raskere modell eller kjøre modellkall parallelt.

**Kostnader:** Hva er kostnaden per agentkjøring? AI-agenter er avhengige av LLM-kall fakturert per token eller eksterne API-er. Hyppig bruk av verktøy eller flere prompts kan raskt øke kostnadene. For eksempel, hvis en agent kaller en LLM fem ganger for marginal kvalitetsforbedring, må du vurdere om kostnaden er rettferdiggjort, eller om du kan redusere antall kall eller bruke en billigere modell. Sanntidsovervåkning kan også hjelpe med å oppdage uventede topper (f.eks. feil som forårsaker overdrevne API-løkker).

**Forespørselsfeil:** Hvor mange forespørsler mislyktes agenten med? Dette kan inkludere API-feil eller mislykkede verktøykall. For å gjøre agenten mer robust mot disse i produksjon kan du sette opp fallback-mekanismer eller forsøk på nytt. F.eks. hvis LLM-leverandør A er nede, bytter du til LLM-leverandør B som backup.

**Brukertilbakemelding:** Implementering av direkte brukervurderinger gir verdifulle innsikter. Dette kan inkludere eksplisitte vurderinger (👍tommel opp/👎ned, ⭐1-5 stjerner) eller tekstlige kommentarer. Konsistent negativ tilbakemelding bør varsle deg da dette er et tegn på at agenten ikke fungerer som forventet.

**Implicit brukertilbakemelding:** Brukeratferd gir indirekte tilbakemelding selv uten eksplisitte vurderinger. Dette kan inkludere umiddelbar omskriving av spørsmål, gjentatte forespørsler eller klikk på en prøv på nytt-knapp. F.eks. hvis du ser at brukere gjentatte ganger stiller det samme spørsmålet, er dette et tegn på at agenten ikke fungerer som forventet.

**Nøyaktighet:** Hvor ofte produserer agenten korrekte eller ønskede resultater? Definisjoner av nøyaktighet varierer (f.eks. korrekt problemløsning, informasjonshentingsnøyaktighet, brukertilfredshet). Første steg er å definere hva suksess ser ut som for din agent. Du kan spore nøyaktighet via automatiserte sjekker, evalueringspoeng eller oppgavemerking. For eksempel, merke spor som "lyktes" eller "feilet".

**Automatiserte evalueringsmetrikker:** Du kan også sette opp automatiserte vurderinger. For eksempel kan du bruke en LLM til å score agentens output, f.eks. om den er hjelpsom, korrekt eller ikke. Det finnes også flere åpen kildekode-biblioteker som hjelper deg å score forskjellige aspekter av agenten, f.eks. [RAGAS](https://docs.ragas.io/) for RAG-agenter eller [LLM Guard](https://llm-guard.com/) for å oppdage skadelig språk eller promptinjeksjon.

I praksis gir en kombinasjon av disse metrikker best oversikt over en AI-agents helse. I dette kapitlets [eksempel-notatbok](./code_samples/10-expense_claim-demo.ipynb) vil vi vise hvordan disse metrikker ser ut i ekte eksempler, men først skal vi lære hvordan en typisk evalueringsarbeidsflyt ser ut.

## Instrumenter agenten din

For å samle inn sporingsdata må du instrumentere koden din. Målet er å instrumentere agentkoden slik at den avgir spor og metrikker som kan fanges opp, behandles og visualiseres av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har blitt en industristandard for LLM-observabilitet. Det gir et sett API-er, SDK-er og verktøy for å generere, samle og eksportere telemetridata.

Det finnes mange instrumenteringsbiblioteker som pakker inn eksisterende agentrammeverk og gjør det enkelt å eksportere OpenTelemetry-spann (spans) til et observabilitetsverktøy. Microsoft Agent Framework integrerer OpenTelemetry nativen. Nedenfor er et eksempel på å instrumentere en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentutførelse spores automatisk
    pass
```

[Eksempel-notatboken](./code_samples/10-expense_claim-demo.ipynb) i dette kapitlet vil demonstrere hvordan du instrumenterer din MAF-agent.

**Manuell span-opprettelse:** Selv om instrumenteringsbiblioteker gir et godt grunnlag, finnes det ofte tilfeller der mer detaljert eller tilpasset informasjon trengs. Du kan manuelt opprette spenner for å legge til egendefinert applikasjonslogikk. Viktigere er at de kan berike automatisk eller manuelt opprettede spenner med egendefinerte attributter (også kalt tagger eller metadata). Disse attributtene kan inkludere forretningsspesifikke data, mellomregninger eller kontekst som kan være nyttig for feilsøking eller analyse, som `user_id`, `session_id`, eller `model_version`.

Eksempel på å manuelt lage spor og spenner med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent-evaluering

Observabilitet gir oss metrikker, men evaluering er prosessen med å analysere disse dataene (og utføre tester) for å avgjøre hvor godt en AI-agent presterer og hvordan den kan forbedres. Med andre ord, når du har fått de sporene og metrikker, hvordan bruker du dem til å bedømme agenten og ta beslutninger?

Regelmessig evaluering er viktig fordi AI-agenter ofte er ikke-deterministiske og kan utvikle seg (gjennom oppdateringer eller modelladferdsdrift) – uten evaluering ville du ikke vite om din “smarte agent” faktisk gjør jobben sin godt eller om den har regressert.

Det finnes to kategorier av evalueringer for AI-agenter: **online evaluering** og **offline evaluering**. Begge er verdifulle og utfyller hverandre. Vi begynner vanligvis med offline evaluering, da dette er det minste nødvendige steget før utrulling av en agent.

### Offline evaluering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dette innebærer å evaluere agenten i et kontrollert miljø, typisk ved bruk av testdatasett, ikke levende brukerforespørsler. Du bruker kuraterte datasett der du vet hva forventet output eller korrekt oppførsel er, og kjører deretter agenten på disse.

For eksempel, hvis du bygde en agent for matte-tekstopgaver, kan du ha et [testdatasett](https://huggingface.co/datasets/gsm8k) med 100 problemer med kjente svar. Offline evaluering gjøres ofte under utvikling (og kan være en del av CI/CD-pipelines) for å sjekke forbedringer eller beskytte mot regresjoner. Fordelen er at det er **repeterbart, og du kan få klare nøyaktighetsmetrikker siden du har korrekt svar**. Du kan også simulere brukerforespørsler og måle agentens svar mot ideelle svar eller bruke automatiske metrikker som nevnt ovenfor.

Den største utfordringen med offline evaluering er å sikre at testdatasettet ditt er omfattende og forblir relevant – agenten kan prestere bra på et fast testsett, men møte svært forskjellige forespørsler i produksjon. Derfor bør du holde testsettene oppdatert med nye ytterpunkter og eksempler som gjenspeiler virkelige scenarier. En blanding av små “smoke test”-tilfeller og større evalueringssett er nyttig: små sett for raske sjekker og større sett for bredere ytelsesmåling.

### Online evaluering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dette refererer til evaluering av agenten i et levende, virkelig miljø, altså under faktisk bruk i produksjon. Online evaluering innebærer å overvåke agentens ytelse på ekte brukerinteraksjoner og kontinuerlig analysere resultater.

For eksempel kan du spore suksessrater, brukertilfredshetscore eller andre metrikker på levende trafikk. Fordelen med online evaluering er at det **fanger opp ting du kanskje ikke forventer i et laboratoriemiljø** – du kan observere modellforandring over tid (hvis agentens effektivitet svekkes når inndataprofiler endres) og avdekke uventede forespørsler eller situasjoner som ikke var i testdataene dine. Det gir et ekte bilde av hvordan agenten oppfører seg i praksis.

Online evaluering inkluderer ofte innsamling av implisitt og eksplisitt brukertilbakemelding, som diskutert, og muligens kjøring av skyggedata-tester eller A/B-tester (der en ny versjon av agenten kjører parallelt for å sammenligne med den gamle). Utfordringen er at det kan være vanskelig å få pålitelige merkelapper eller scorer for levende interaksjoner – du kan være avhengig av brukertilbakemelding eller nedstrømsmetrikker (som om brukeren klikket på resultatet).

### Kombinasjon av begge

Online og offline evaluering er ikke gjensidig utelukkende; de utfyller hverandre godt. Innsikter fra online overvåking (f.eks. nye typer brukerforespørsler hvor agenten presterer dårlig) kan brukes til å utvide og forbedre offline testdatasett. Omvendt kan agenter som presterer godt i offline-tester deployeres med større tillit og overvåkes online.

Faktisk adopterer mange team en sløyfe:

_evaluer offline -> distribuer -> overvåk online -> samle nye feiltilfeller -> legg til i offline datasett -> finjuster agent -> gjenta_.

## Vanlige problemer

Når du distribuerer AI-agenter i produksjon, kan du støte på ulike utfordringer. Her er noen vanlige problemer og mulige løsninger:

| **Problem**    | **Mulig løsning**   |
| ------------- | ------------------ |
| AI-agent utfører ikke oppgaver konsekvent | - Finpuss prompten som gis til AI-agenten; vær tydelig på målsetninger.<br>- Identifiser om det hjelper å dele oppgavene i deloppgaver og la flere agenter håndtere disse. |
| AI-agent havner i kontinuerlige løkker  | - Sørg for klare avslutningsbetingelser slik at agenten vet når den skal stoppe prosessen.<br>- For komplekse oppgaver som krever resonnering og planlegging, bruk en større modell spesialisert på resonneringsoppgaver. |
| AI-agentens verktøysanrop fungerer ikke bra   | - Test og valider verktøyets output utenfor agentsystemet.<br>- Finpuss definerte parametere, prompts og navngivning av verktøy.  |
| Multi-agent system utfører ikke konsekvent | - Finpuss prompts som gis til hver agent for å sikre at de er spesifikke og distinkte fra hverandre.<br>- Bygg et hierarkisk system med en "routing"- eller kontrollagent for å avgjøre hvilken agent som er rett. |

Mange av disse problemene kan identifiseres mer effektivt med observabilitet på plass. Sporene og metrikker vi diskuterte tidligere hjelper med å lokalisere nøyaktig hvor i agentens arbeidsflyt problemer oppstår, noe som gjør feilsøking og optimalisering mye mer effektiv.

## Kostnadsstyring
Her er noen strategier for å håndtere kostnadene ved å sette AI-agenter i produksjon:

**Bruke Mindre Modeller:** Små språkmodeller (SLMs) kan prestere godt på visse agentiske brukstilfeller og vil redusere kostnadene betydelig. Som nevnt tidligere, er det beste å bygge et evalueringssystem for å bestemme og sammenligne ytelsen mot større modeller for å forstå hvor godt en SLM vil fungere på ditt brukstilfelle. Vurder å bruke SLM-er for enklere oppgaver som intensjonsklassifisering eller parameterutvinning, samtidig som du reserverer større modeller for kompleks resonnement.

**Bruke en Routermodell:** En lignende strategi er å bruke en variasjon av modeller og størrelser. Du kan bruke en LLM/SLM eller en serverløs funksjon for å rute forespørsler basert på kompleksitet til de best egnede modellene. Dette vil også bidra til å redusere kostnader samtidig som ytelsen sikres på riktige oppgaver. For eksempel, send enkle forespørsler til mindre, raskere modeller, og bruk kun dyre store modeller for komplekse resonnementoppgaver.

**Bufring av Respons:** Å identifisere vanlige forespørsler og oppgaver og gi responsene før de går gjennom ditt agentiske system er en god måte å redusere mengden av lignende forespørsler på. Du kan til og med implementere en flyt for å identifisere hvor lik en forespørsel er i forhold til dine bufrede forespørsler ved å bruke mer grunnleggende AI-modeller. Denne strategien kan betydelig redusere kostnadene for ofte stilte spørsmål eller vanlige arbeidsflyter.

## La oss se hvordan dette fungerer i praksis

I [eksempeln notebook fra denne seksjonen](./code_samples/10-expense_claim-demo.ipynb) vil vi se eksempler på hvordan vi kan bruke observasjonsverktøy for å overvåke og evaluere vår agent.


### Har du flere spørsmål om AI-agenter i produksjon?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortid og få svar på dine spørsmål om AI-agenter.

## Forrige leksjon

[Metakognisjon Designmønster](../09-metacognition/README.md)

## Neste leksjon

[Agentiske protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved bruk av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på det opprinnelige språket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->