<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:14:42+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "no"
}
-->
# Minne for AI-agenter

Når man diskuterer de unike fordelene ved å lage AI-agenter, er det to ting som ofte nevnes: evnen til å bruke verktøy for å utføre oppgaver og evnen til å forbedre seg over tid. Minne er grunnlaget for å skape selvforbedrende agenter som kan gi bedre opplevelser for brukerne våre.

I denne leksjonen skal vi se på hva minne er for AI-agenter, hvordan vi kan administrere det, og hvordan vi kan bruke det til fordel for applikasjonene våre.

## Introduksjon

Denne leksjonen dekker:

• **Forståelse av AI-agentminne**: Hva minne er og hvorfor det er essensielt for agenter.

• **Implementering og lagring av minne**: Praktiske metoder for å legge til minnefunksjoner i AI-agenter, med fokus på korttids- og langtidsminne.

• **Gjøre AI-agenter selvforbedrende**: Hvordan minne gjør det mulig for agenter å lære av tidligere interaksjoner og forbedre seg over tid.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

• **Skille mellom ulike typer AI-agentminne**, inkludert arbeidsminne, korttidsminne og langtidsminne, samt spesialiserte former som personaminne og episodisk minne.

• **Implementere og administrere korttids- og langtidsminne for AI-agenter** ved hjelp av Semantic Kernel-rammeverket, verktøy som Mem0 og Whiteboard-minne, og integrering med Azure AI Search.

• **Forstå prinsippene bak selvforbedrende AI-agenter** og hvordan robuste minnehåndteringssystemer bidrar til kontinuerlig læring og tilpasning.

## Forståelse av AI-agentminne

I sin kjerne refererer **minne for AI-agenter til mekanismer som lar dem beholde og hente frem informasjon**. Denne informasjonen kan være spesifikke detaljer om en samtale, brukerpreferanser, tidligere handlinger eller til og med lærte mønstre.

Uten minne er AI-applikasjoner ofte tilstandsløse, noe som betyr at hver interaksjon starter fra bunnen av. Dette fører til en repetitiv og frustrerende brukeropplevelse der agenten "glemmer" tidligere kontekst eller preferanser.

### Hvorfor er minne viktig?

Agentens intelligens er nært knyttet til dens evne til å huske og bruke tidligere informasjon. Minne gjør det mulig for agenter å være:

• **Reflekterende**: Lære av tidligere handlinger og resultater.

• **Interaktive**: Opprettholde kontekst gjennom en pågående samtale.

• **Proaktive og reaktive**: Forutse behov eller reagere hensiktsmessig basert på historiske data.

• **Autonome**: Operere mer selvstendig ved å trekke på lagret kunnskap.

Målet med å implementere minne er å gjøre agenter mer **pålitelige og kapable**.

### Typer av minne

#### Arbeidsminne

Tenk på dette som et stykke kladdepapir en agent bruker under en enkelt, pågående oppgave eller tankeprosess. Det holder umiddelbar informasjon som trengs for å beregne neste steg.

For AI-agenter fanger arbeidsminne ofte opp den mest relevante informasjonen fra en samtale, selv om hele samtalehistorikken er lang eller avkortet. Det fokuserer på å trekke ut nøkkelpunkter som krav, forslag, beslutninger og handlinger.

**Eksempel på arbeidsminne**

I en reisebestillingsagent kan arbeidsminne fange opp brukerens nåværende forespørsel, som "Jeg vil bestille en tur til Paris". Dette spesifikke kravet holdes i agentens umiddelbare kontekst for å styre den nåværende interaksjonen.

#### Korttidsminne

Denne typen minne beholder informasjon for varigheten av en enkelt samtale eller økt. Det er konteksten for den nåværende chatten, som lar agenten referere tilbake til tidligere vendinger i dialogen.

**Eksempel på korttidsminne**

Hvis en bruker spør: "Hvor mye koster en flyreise til Paris?" og deretter følger opp med "Hva med overnatting der?", sørger korttidsminnet for at agenten vet at "der" refererer til "Paris" innenfor den samme samtalen.

#### Langtidsminne

Dette er informasjon som vedvarer på tvers av flere samtaler eller økter. Det lar agenter huske brukerpreferanser, historiske interaksjoner eller generell kunnskap over lengre tid. Dette er viktig for personalisering.

**Eksempel på langtidsminne**

Et langtidsminne kan lagre at "Ben liker ski og utendørsaktiviteter, foretrekker kaffe med fjellutsikt, og ønsker å unngå avanserte skibakker på grunn av en tidligere skade". Denne informasjonen, lært fra tidligere interaksjoner, påvirker anbefalinger i fremtidige reiseplanleggingsøkter, og gjør dem svært personlige.

#### Personaminne

Denne spesialiserte typen minne hjelper en agent med å utvikle en konsistent "personlighet" eller "rolle". Det lar agenten huske detaljer om seg selv eller sin tiltenkte rolle, noe som gjør interaksjoner mer flytende og fokuserte.

**Eksempel på personaminne**

Hvis reiseagenten er designet for å være en "ekspert på skiplanlegging", kan personaminne forsterke denne rollen, og påvirke svarene slik at de samsvarer med tonen og kunnskapen til en ekspert.

#### Arbeidsflyt-/episodisk minne

Dette minnet lagrer sekvensen av trinn en agent tar under en kompleks oppgave, inkludert suksesser og feil. Det er som å huske spesifikke "episoder" eller tidligere erfaringer for å lære av dem.

**Eksempel på episodisk minne**

Hvis agenten forsøkte å bestille en spesifikk flyreise, men det mislyktes på grunn av utilgjengelighet, kan episodisk minne registrere denne feilen, slik at agenten kan prøve alternative flyreiser eller informere brukeren om problemet på en mer informert måte ved et senere forsøk.

#### Enhetsminne

Dette innebærer å trekke ut og huske spesifikke enheter (som personer, steder eller ting) og hendelser fra samtaler. Det lar agenten bygge en strukturert forståelse av nøkkelpunkter som diskuteres.

**Eksempel på enhetsminne**

Fra en samtale om en tidligere tur kan agenten trekke ut "Paris", "Eiffeltårnet" og "middag på Le Chat Noir restaurant" som enheter. I en fremtidig interaksjon kan agenten huske "Le Chat Noir" og tilby å gjøre en ny reservasjon der.

#### Strukturert RAG (Retrieval Augmented Generation)

Mens RAG er en bredere teknikk, fremheves "strukturert RAG" som en kraftig minneteknologi. Den trekker ut tett, strukturert informasjon fra ulike kilder (samtaler, e-poster, bilder) og bruker det for å forbedre presisjon, gjenkalling og hastighet i svarene. I motsetning til klassisk RAG som kun baserer seg på semantisk likhet, arbeider strukturert RAG med den iboende strukturen i informasjonen.

**Eksempel på strukturert RAG**

I stedet for bare å matche nøkkelord, kan strukturert RAG analysere flydetaljer (destinasjon, dato, tid, flyselskap) fra en e-post og lagre dem på en strukturert måte. Dette muliggjør presise forespørsler som "Hvilket fly bestilte jeg til Paris på tirsdag?"

## Implementering og lagring av minne

Implementering av minne for AI-agenter innebærer en systematisk prosess med **minnehåndtering**, som inkluderer generering, lagring, henting, integrering, oppdatering og til og med "glemming" (eller sletting) av informasjon. Henting er en spesielt viktig del.

### Spesialiserte minneverktøy

En måte å lagre og administrere agentminne på er ved å bruke spesialiserte verktøy som Mem0. Mem0 fungerer som et vedvarende minnelag, som lar agenter huske relevante interaksjoner, lagre brukerpreferanser og faktakontekst, og lære av suksesser og feil over tid. Ideen her er at tilstandsløse agenter blir til tilstandsfulle.

Det fungerer gjennom en **to-fase minnepipeline: ekstraksjon og oppdatering**. Først sendes meldinger lagt til en agents tråd til Mem0-tjenesten, som bruker en Large Language Model (LLM) for å oppsummere samtalehistorikk og trekke ut nye minner. Deretter bestemmer en LLM-drevet oppdateringsfase om disse minnene skal legges til, endres eller slettes, og lagrer dem i en hybrid datalagring som kan inkludere vektor-, graf- og nøkkel-verdi-databaser. Dette systemet støtter også ulike minnetyper og kan inkludere grafminne for å administrere relasjoner mellom enheter.

### Lagring av minne med RAG

Utover spesialiserte minneverktøy som Mem0, kan du bruke robuste søketjenester som **Azure AI Search som backend for lagring og henting av minner**, spesielt for strukturert RAG.

Dette lar deg forankre agentens svar med dine egne data, og sikrer mer relevante og nøyaktige svar. Azure AI Search kan brukes til å lagre bruker-spesifikke reiseopplevelser, produktkataloger eller annen domenespesifikk kunnskap.

Azure AI Search støtter funksjoner som **strukturert RAG**, som utmerker seg ved å trekke ut og hente tett, strukturert informasjon fra store datasett som samtalehistorikk, e-poster eller til og med bilder. Dette gir "supermenneskelig presisjon og gjenkalling" sammenlignet med tradisjonelle tekstchunking- og embedding-tilnærminger.

## Gjøre AI-agenter selvforbedrende

Et vanlig mønster for selvforbedrende agenter innebærer å introdusere en **"kunnskapsagent"**. Denne separate agenten observerer hovedsamtalen mellom brukeren og den primære agenten. Dens rolle er å:

1. **Identifisere verdifull informasjon**: Bestemme om noen del av samtalen er verdt å lagre som generell kunnskap eller en spesifikk brukerpreferanse.

2. **Ekstrahere og oppsummere**: Destillere essensiell læring eller preferanse fra samtalen.

3. **Lagre i en kunnskapsbase**: Bevare denne ekstraherte informasjonen, ofte i en vektordatabase, slik at den kan hentes frem senere.

4. **Forsterke fremtidige forespørsler**: Når brukeren starter en ny forespørsel, henter kunnskapsagenten relevant lagret informasjon og legger det til brukerens prompt, og gir viktig kontekst til den primære agenten (ligner på RAG).

### Optimaliseringer for minne

• **Latenshåndtering**: For å unngå å bremse brukerinteraksjoner, kan en billigere, raskere modell brukes først for raskt å sjekke om informasjon er verdt å lagre eller hente, og kun aktivere den mer komplekse ekstraksjons-/hentingsprosessen når det er nødvendig.

• **Vedlikehold av kunnskapsbase**: For en voksende kunnskapsbase kan mindre brukt informasjon flyttes til "kald lagring" for å redusere kostnader.

## Har du flere spørsmål om kontekstteknikk?

Bli med på [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortimer og få svar på spørsmålene dine om AI-agenter.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.