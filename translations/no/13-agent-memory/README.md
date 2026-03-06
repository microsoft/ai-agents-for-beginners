# Minne for AI-agenter  
[![Agent Memory](../../../translated_images/no/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Når man diskuterer de unike fordelene ved å lage AI-agenter, snakkes det hovedsakelig om to ting: evnen til å kalle verktøy for å utføre oppgaver og evnen til å forbedre seg over tid. Minne er grunnlaget for å lage selvforbedrende agenter som kan skape bedre opplevelser for brukerne våre.

I denne leksjonen skal vi se på hva minne er for AI-agenter og hvordan vi kan håndtere det og bruke det til fordel for applikasjonene våre.

## Introduksjon

Denne leksjonen vil dekke:

• **Forstå AI-agentminne**: Hva minne er og hvorfor det er essensielt for agenter.

• **Implementering og lagring av minne**: Praktiske metoder for å legge til minnefunksjonalitet i AI-agentene dine, med fokus på korttids- og langtidsminne.

• **Å gjøre AI-agenter selvforbedrende**: Hvordan minne gjør at agenter kan lære av tidligere interaksjoner og forbedre seg over tid.

## Tilgjengelige implementasjoner

Denne leksjonen inkluderer to omfattende notatbøker:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerer minne ved hjelp av Mem0 og Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerer strukturert minne ved bruk av Cognee, automatisk bygging av kunnskapsgraf støttet av embeddings, visualisering av graf og intelligent henting

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

• **Skille mellom ulike typer AI-agentminne**, inkludert arbeidsminne, korttidsminne og langtidsminne, samt spesialiserte former som persona- og episodisk minne.

• **Implementere og håndtere korttids- og langtidsminne for AI-agenter** ved hjelp av Microsoft Agent Framework, med verktøy som Mem0, Cognee, Whiteboard-minne, og integrering med Azure AI Search.

• **Forstå prinsippene bak selvforbedrende AI-agenter** og hvordan robuste minnehåndteringssystemer bidrar til kontinuerlig læring og tilpasning.

## Forstå AI-agentminne

I kjernen refererer **minne for AI-agenter til mekanismene som gjør at de kan beholde og hente frem informasjon**. Denne informasjonen kan være spesifikke detaljer om en samtale, brukerpreferanser, tidligere handlinger eller til og med lærte mønstre.

Uten minne er AI-applikasjoner ofte statsløse, noe som betyr at hver interaksjon starter på nytt. Dette fører til en repeterende og frustrerende brukeropplevelse hvor agenten "glemmer" tidligere kontekst eller preferanser.

### Hvorfor er minne viktig?

En agents intelligens er dypt knyttet til dens evne til å hente frem og bruke tidligere informasjon. Minne gjør at agenter kan være:

• **Reflekterende**: Lære av tidligere handlinger og utfall.

• **Interaktive**: Opprettholde kontekst over en pågående samtale.

• **Proaktive og reaktive**: Forutse behov eller svare passende basert på historiske data.

• **Autonome**: Operere mer selvstendig ved å trekke på lagret kunnskap.

Målet med å implementere minne er å gjøre agenter mer **pålitelige og dyktige**.

### Typer minne

#### Arbeidsminne

Tenk på dette som et skissepapir agenten bruker under en enkelt, pågående oppgave eller tankeprosess. Det holder umiddelbar informasjon som trengs for å beregne neste steg.

For AI-agenter fanger arbeidsminnet ofte den mest relevante informasjonen fra en samtale, selv om hele samtalehistorien er lang eller forkortet. Det fokuserer på å trekke ut nøkkelelementer som krav, forslag, beslutninger og handlinger.

**Arbeidsminne-eksempel**

I en reisebestillingsagent kan arbeidsminnet fange brukerens nåværende forespørsel, som "Jeg vil bestille en tur til Paris". Dette spesifikke kravet holdes i agentens umiddelbare kontekst for å styre den nåværende interaksjonen.

#### Korttidsminne

Denne typen minne beholder informasjon i løpet av en enkelt samtale eller økt. Det er konteksten i den nåværende chatten, som lar agenten referere tilbake til tidligere turer i dialogen.

**Korttidsminne-eksempel**

Hvis en bruker spør, "Hvor mye koster en flyreise til Paris?" og deretter følger opp med "Hva med overnatting der?", sikrer korttidsminne at agenten vet at "der" refererer til "Paris" i samme samtale.

#### Langtidsminne

Dette er informasjon som vedvarer over flere samtaler eller økter. Det gjør at agenter kan huske brukerpreferanser, historiske interaksjoner eller generell kunnskap over lengre tid. Dette er viktig for personalisering.

**Langtidsminne-eksempel**

Langtidsminnet kan lagre at "Ben liker ski og utendørsaktiviteter, liker kaffe med utsikt til fjellet, og vil unngå avanserte skibakker på grunn av en tidligere skade". Denne informasjonen, lært fra tidligere interaksjoner, påvirker anbefalinger i fremtidige reiseplanleggingsøkter og gjør dem svært personlige.

#### Persona-minne

Denne spesialiserte minnetypen hjelper en agent med å utvikle en konsistent "personlighet" eller "persona". Det lar agenten huske detaljer om seg selv eller sin tiltenkte rolle, noe som gjør interaksjoner mer flytende og fokusert.

**Persona-minne-eksempel**  
Hvis reiseagenten er designet for å være en "ekspert på ski", kan persona-minnet forsterke denne rollen og påvirke svarene for å stemme overens med en eksperts tone og kunnskap.

#### Workflow/Episodisk minne

Dette minnet lagrer rekkefølgen av steg en agent tar under en kompleks oppgave, inkludert suksesser og feil. Det er som å huske spesifikke "episoder" eller tidligere erfaringer for å lære av dem.

**Episodisk minne-eksempel**

Hvis agenten forsøkte å bestille en spesifikk flyreise, men det mislyktes på grunn av utilgjengelighet, kan episodisk minne registrere denne feilen, slik at agenten kan prøve alternative flyvninger eller informere brukeren om problemet på en mer informert måte ved et senere forsøk.

#### Entitetsminne

Dette innebærer å trekke ut og huske spesifikke enheter (som personer, steder eller ting) og hendelser fra samtaler. Det lar agenten bygge en strukturert forståelse av nøkkel-elementer som er diskutert.

**Entitetsminne-eksempel**

Fra en samtale om en tidligere tur kan agenten trekke ut "Paris," "Eiffeltårnet," og "middag på restauranten Le Chat Noir" som enheter. I en fremtidig interaksjon kan agenten huske "Le Chat Noir" og tilby å gjøre en ny reservasjon der.

#### Strukturert RAG (Retrieval Augmented Generation)

Mens RAG er en bredere teknikk, fremheves "Strukturert RAG" som en kraftfull minneteknologi. Den trekker ut tett, strukturert informasjon fra ulike kilder (samtaler, e-poster, bilder) og bruker det for å forbedre presisjon, gjenfinning og hastighet i svar. I motsetning til klassisk RAG som bare baserer seg på semantisk likhet, jobber Strukturert RAG med den iboende strukturen i informasjonen.

**Strukturert RAG-eksempel**

I stedet for bare å matche nøkkelord, kan Strukturert RAG analysere flydetaljer (destinasjon, dato, tid, flyselskap) fra en e-post og lagre dem på en strukturert måte. Dette gjør det mulig med presise spørsmål som "Hvilket fly bestilte jeg til Paris på tirsdag?"

## Implementering og lagring av minne

Å implementere minne for AI-agenter innebærer en systematisk prosess av **minnehåndtering**, som inkluderer generering, lagring, henting, integrasjon, oppdatering og til og med "glemming" (eller sletting) av informasjon. Henting er et spesielt kritisk aspekt.

### Spesialiserte minneverktøy

#### Mem0

En måte å lagre og håndtere agentminne på er å bruke spesialiserte verktøy som Mem0. Mem0 fungerer som et persistent minnelag, som gjør at agenter kan hente frem relevante interaksjoner, lagre brukerpreferanser og faktabasert kontekst, og lære av suksesser og feil over tid. Tanken her er at statsløse agenter blir til tilstandsbaserte.

Det fungerer gjennom en **to-faset minneprosess: ekstraksjon og oppdatering**. Først sendes meldinger lagt til en agents tråd til Mem0-tjenesten, som bruker en stor språkmodell (LLM) til å oppsummere samtalehistorikken og trekke ut nye minner. Deretter avgjør en LLM-drevet oppdateringsfase om minnene skal legges til, endres eller slettes, og lagrer dem i en hybrid datalagring som kan inkludere vektor-, graf- og nøkkel-verdi-databaser. Systemet støtter også ulike minnetyper og kan inkludere grafminne for å håndtere relasjoner mellom entiteter.

#### Cognee

En annen kraftfull tilnærming er å bruke **Cognee**, et åpen kildekode semantisk minnesystem for AI-agenter som omdanner strukturert og ustrukturert data til søkbare kunnskapsgrafer støttet av embeddings. Cognee tilbyr en **dual-store-arkitektur** som kombinerer vektorlignende søk med grafrelasjoner, og lar agenter forstå ikke bare hva informasjon ligner på, men hvordan konsepter relaterer til hverandre.

Det utmerker seg i **hybrid gjenfinning** som blander vektorlignende søk, grafstruktur og LLM-resonnement – fra rå oppslag av fragmenter til grafbevisst spørsmålsbesvarelse. Systemet opprettholder et **levende minne** som utvikler seg og vokser mens det forblir søkbart som én sammenkoblet graf, og støtter både korttids kontekst i en økt og langtids vedvarende minne.

Cognee-notatbok-tutorialen ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrerer bygging av dette sammenslåtte minnelaget, med praktiske eksempler på å innta ulike datakilder, visualisere kunnskapsgrafen og søke med ulike søkestrategier tilpasset spesifikke agentbehov.

### Lagring av minne med RAG

Utover spesialiserte minneverktøy som mem0, kan du utnytte robuste søketjenester som **Azure AI Search som backend for lagring og henting av minner**, spesielt for strukturert RAG.

Dette gjør at du kan forankre agentens svar med dine egne data, og sikre mer relevante og presise svar. Azure AI Search kan brukes til å lagre brukerspesifikke reiseminnene, produktkataloger eller annen domene-spesifikk kunnskap.

Azure AI Search støtter funksjonaliteter som **Strukturert RAG**, som utmerker seg i å trekke ut og hente tett, strukturert informasjon fra store datasett som samtalehistorier, e-poster eller til og med bilder. Dette gir "supermenneskelig presisjon og gjenfinning" sammenlignet med tradisjonell tekstfragmentering og embedding-tilnærminger.

## Gjøre AI-agenter selvforbedrende

Et vanlig mønster for selvforbedrende agenter involverer å introdusere en **"kunnskapsagent"**. Denne separate agenten observerer hovedsamtalen mellom brukeren og hovedagenten. Dens rolle er å:

1. **Identifisere verdifull informasjon**: Bestemme om noen deler av samtalen er verdt å lagre som generell kunnskap eller en spesifikk brukerpreferanse.

2. **Ekstrahere og oppsummere**: Destillere essensiell læring eller preferanse fra samtalen.

3. **Lagre i en kunnskapsbase**: Vedvarende lagre denne uttrukne informasjonen, ofte i en vektordatabse, slik at den kan hentes senere.

4. **Berike fremtidige spørringer**: Når brukeren starter en ny forespørsel, henter kunnskapsagenten relevant lagret informasjon og legger det til brukerens prompt, og gir avgjørende kontekst til hovedagenten (likt RAG).

### Optimaliseringer for minne

• **Latency-håndtering**: For å unngå å forsinke brukerinteraksjoner kan en billigere, raskere modell brukes først for raskt å sjekke om informasjon er verdt å lagre eller hente, og kun kalle den mer komplekse ekstraksjons-/hentefasen når nødvendig.

• **Vedlikehold av kunnskapsbase**: For en voksende kunnskapsbase kan mindre ofte brukt informasjon flyttes til "kald lagring" for kostnadskontroll.

## Har du flere spørsmål om agentminne?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre som lærer, delta på kontortid og få svar på spørsmål om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi jobber for nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->