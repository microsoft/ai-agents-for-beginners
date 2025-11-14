<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2c9703548140bafa2d6a77406552542",
  "translation_date": "2025-10-03T14:46:37+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "no"
}
-->
# Hukommelse for AI-agenter
[![Agent Memory](../../../translated_images/lesson-13-thumbnail.959e3bc52d210c64a614a3bece6b170a2c472138dc0a14c7fbde07306ef95ae7.no.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Når vi diskuterer de unike fordelene ved å lage AI-agenter, er det to ting som ofte nevnes: evnen til å bruke verktøy for å utføre oppgaver og evnen til å forbedre seg over tid. Hukommelse er grunnlaget for å skape selvforbedrende agenter som kan gi bedre opplevelser for brukerne våre.

I denne leksjonen skal vi se på hva hukommelse er for AI-agenter, hvordan vi kan administrere den, og hvordan vi kan bruke den til fordel for applikasjonene våre.

## Introduksjon

Denne leksjonen dekker:

• **Forstå AI-agentens hukommelse**: Hva hukommelse er og hvorfor det er viktig for agenter.

• **Implementere og lagre hukommelse**: Praktiske metoder for å legge til hukommelsesfunksjoner i AI-agenter, med fokus på kortsiktig og langsiktig hukommelse.

• **Gjøre AI-agenter selvforbedrende**: Hvordan hukommelse gjør det mulig for agenter å lære av tidligere interaksjoner og forbedre seg over tid.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

• **Skille mellom ulike typer AI-agentens hukommelse**, inkludert arbeids-, kortsiktig og langsiktig hukommelse, samt spesialiserte former som persona- og episodisk hukommelse.

• **Implementere og administrere kortsiktig og langsiktig hukommelse for AI-agenter** ved hjelp av Semantic Kernel-rammeverket, verktøy som Mem0 og Whiteboard-hukommelse, og integrering med Azure AI Search.

• **Forstå prinsippene bak selvforbedrende AI-agenter** og hvordan robuste hukommelsessystemer bidrar til kontinuerlig læring og tilpasning.

## Forstå AI-agentens hukommelse

I sin kjerne refererer **hukommelse for AI-agenter til mekanismer som lar dem beholde og hente frem informasjon**. Denne informasjonen kan være spesifikke detaljer om en samtale, brukerpreferanser, tidligere handlinger eller til og med lærte mønstre.

Uten hukommelse er AI-applikasjoner ofte tilstandsløse, noe som betyr at hver interaksjon starter fra scratch. Dette fører til en repetitiv og frustrerende brukeropplevelse der agenten "glemmer" tidligere kontekst eller preferanser.

### Hvorfor er hukommelse viktig?

En agents intelligens er nært knyttet til dens evne til å huske og bruke tidligere informasjon. Hukommelse gjør det mulig for agenter å være:

• **Reflekterende**: Lære av tidligere handlinger og resultater.

• **Interaktive**: Opprettholde kontekst gjennom en pågående samtale.

• **Proaktive og reaktive**: Forutse behov eller reagere hensiktsmessig basert på historiske data.

• **Autonome**: Operere mer selvstendig ved å trekke på lagret kunnskap.

Målet med å implementere hukommelse er å gjøre agenter mer **pålitelige og kapable**.

### Typer hukommelse

#### Arbeidshukommelse

Tenk på dette som et stykke kladdepapir en agent bruker under en enkelt, pågående oppgave eller tankeprosess. Det holder umiddelbar informasjon som trengs for å beregne neste steg.

For AI-agenter fanger arbeidshukommelse ofte den mest relevante informasjonen fra en samtale, selv om hele samtalehistorikken er lang eller avkortet. Den fokuserer på å trekke ut nøkkelpunkter som krav, forslag, beslutninger og handlinger.

**Eksempel på arbeidshukommelse**

I en reisebestillingsagent kan arbeidshukommelsen fange brukerens nåværende forespørsel, som "Jeg vil bestille en tur til Paris". Dette spesifikke kravet holdes i agentens umiddelbare kontekst for å styre den nåværende interaksjonen.

#### Korttidsminne

Denne typen hukommelse beholder informasjon for varigheten av en enkelt samtale eller økt. Det er konteksten for den nåværende chatten, som lar agenten referere til tidligere vendinger i dialogen.

**Eksempel på korttidsminne**

Hvis en bruker spør: "Hvor mye koster en flyreise til Paris?" og deretter følger opp med "Hva med overnatting der?", sørger korttidsminnet for at agenten vet at "der" refererer til "Paris" i den samme samtalen.

#### Langtidsminne

Dette er informasjon som vedvarer på tvers av flere samtaler eller økter. Det lar agenter huske brukerpreferanser, historiske interaksjoner eller generell kunnskap over lengre tid. Dette er viktig for personalisering.

**Eksempel på langtidsminne**

Et langtidsminne kan lagre at "Ben liker ski og utendørsaktiviteter, foretrekker kaffe med fjellutsikt, og vil unngå avanserte skibakker på grunn av en tidligere skade". Denne informasjonen, lært fra tidligere interaksjoner, påvirker anbefalinger i fremtidige reiseplanleggingsøkter, og gjør dem svært personlige.

#### Persona-hukommelse

Denne spesialiserte hukommelsestypen hjelper en agent med å utvikle en konsistent "personlighet" eller "persona". Det lar agenten huske detaljer om seg selv eller sin tiltenkte rolle, og gjør interaksjoner mer flytende og fokuserte.

**Eksempel på persona-hukommelse**

Hvis reiseagenten er designet for å være en "ekspert på skiplanlegging", kan persona-hukommelsen forsterke denne rollen, og påvirke svarene til å samsvare med en eksperts tone og kunnskap.

#### Arbeidsflyt-/episodisk hukommelse

Denne hukommelsen lagrer sekvensen av trinn en agent tar under en kompleks oppgave, inkludert suksesser og feil. Det er som å huske spesifikke "episoder" eller tidligere erfaringer for å lære av dem.

**Eksempel på episodisk hukommelse**

Hvis agenten forsøkte å bestille en spesifikk flyreise, men det mislyktes på grunn av utilgjengelighet, kan episodisk hukommelse registrere denne feilen, slik at agenten kan prøve alternative flyreiser eller informere brukeren om problemet på en mer informert måte ved et senere forsøk.

#### Enhetshukommelse

Dette innebærer å trekke ut og huske spesifikke enheter (som personer, steder eller ting) og hendelser fra samtaler. Det lar agenten bygge en strukturert forståelse av nøkkelpunktene som diskuteres.

**Eksempel på enhetshukommelse**

Fra en samtale om en tidligere tur kan agenten trekke ut "Paris", "Eiffeltårnet" og "middag på Le Chat Noir restaurant" som enheter. I en fremtidig interaksjon kan agenten huske "Le Chat Noir" og tilby å gjøre en ny reservasjon der.

#### Strukturert RAG (Retrieval Augmented Generation)

Mens RAG er en bredere teknikk, fremheves "strukturert RAG" som en kraftig hukommelsesteknologi. Den trekker ut tett, strukturert informasjon fra ulike kilder (samtaler, e-poster, bilder) og bruker den til å forbedre presisjon, gjenkalling og hastighet i svarene. I motsetning til klassisk RAG som kun baserer seg på semantisk likhet, arbeider strukturert RAG med den iboende strukturen i informasjonen.

**Eksempel på strukturert RAG**

I stedet for bare å matche nøkkelord, kan strukturert RAG analysere flydetaljer (destinasjon, dato, tid, flyselskap) fra en e-post og lagre dem på en strukturert måte. Dette muliggjør presise forespørsler som "Hvilket fly bestilte jeg til Paris på tirsdag?"

## Implementere og lagre hukommelse

Å implementere hukommelse for AI-agenter innebærer en systematisk prosess med **hukommelsesadministrasjon**, som inkluderer generering, lagring, henting, integrering, oppdatering og til og med "glemming" (eller sletting) av informasjon. Henting er en spesielt viktig del.

### Spesialiserte hukommelsesverktøy

En måte å lagre og administrere agentens hukommelse på er ved å bruke spesialiserte verktøy som Mem0. Mem0 fungerer som et vedvarende hukommelseslag, som lar agenter huske relevante interaksjoner, lagre brukerpreferanser og faktuell kontekst, og lære av suksesser og feil over tid. Ideen her er at tilstandsløse agenter blir til tilstandsfulle.

Det fungerer gjennom en **to-fase hukommelsesprosess: utvinning og oppdatering**. Først sendes meldinger lagt til en agents tråd til Mem0-tjenesten, som bruker en Large Language Model (LLM) for å oppsummere samtalehistorikk og trekke ut nye minner. Deretter bestemmer en LLM-drevet oppdateringsfase om disse minnene skal legges til, endres eller slettes, og lagrer dem i en hybrid datalagring som kan inkludere vektor-, graf- og nøkkel-verdi-databaser. Dette systemet støtter også ulike hukommelsestyper og kan inkludere grafhukommelse for å administrere relasjoner mellom enheter.

### Lagring av hukommelse med RAG

Utover spesialiserte hukommelsesverktøy som Mem0, kan du bruke robuste søketjenester som **Azure AI Search som backend for lagring og henting av minner**, spesielt for strukturert RAG.

Dette lar deg forankre agentens svar med dine egne data, og sikrer mer relevante og nøyaktige svar. Azure AI Search kan brukes til å lagre bruker-spesifikke reise-minner, produktkataloger eller annen domenespesifikk kunnskap.

Azure AI Search støtter funksjoner som **strukturert RAG**, som utmerker seg ved å trekke ut og hente tett, strukturert informasjon fra store datasett som samtalehistorikk, e-poster eller til og med bilder. Dette gir "supermenneskelig presisjon og gjenkalling" sammenlignet med tradisjonelle tekstchunking- og embedding-tilnærminger.

## Gjøre AI-agenter selvforbedrende

Et vanlig mønster for selvforbedrende agenter innebærer å introdusere en **"kunnskapsagent"**. Denne separate agenten observerer hovedsamtalen mellom brukeren og den primære agenten. Dens rolle er å:

1. **Identifisere verdifull informasjon**: Bestemme om noen del av samtalen er verdt å lagre som generell kunnskap eller en spesifikk brukerpreferanse.

2. **Trekk ut og oppsummer**: Destillere den essensielle læringen eller preferansen fra samtalen.

3. **Lagre i en kunnskapsbase**: Bevare denne uttrukne informasjonen, ofte i en vektordatabase, slik at den kan hentes frem senere.

4. **Forsterke fremtidige forespørsler**: Når brukeren starter en ny forespørsel, henter kunnskapsagenten relevant lagret informasjon og legger den til brukerens prompt, og gir viktig kontekst til den primære agenten (ligner på RAG).

### Optimaliseringer for hukommelse

• **Latenshåndtering**: For å unngå å bremse brukerinteraksjoner, kan en billigere, raskere modell brukes først for raskt å sjekke om informasjon er verdt å lagre eller hente, og kun aktivere den mer komplekse utvinnings-/hentingsprosessen når det er nødvendig.

• **Vedlikehold av kunnskapsbase**: For en voksende kunnskapsbase kan mindre brukt informasjon flyttes til "kald lagring" for å redusere kostnader.

## Har du flere spørsmål om agentens hukommelse?

Bli med på [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortimer og få svar på spørsmålene dine om AI-agenter.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.