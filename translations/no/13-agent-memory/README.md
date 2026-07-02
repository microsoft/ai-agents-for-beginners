# Minne for AI-agenter  
[![Agent Memory](../../../translated_images/no/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Når man diskuterer de unike fordelene ved å lage AI-agenter, er det hovedsakelig to ting som diskuteres: evnen til å bruke verktøy for å fullføre oppgaver og evnen til å forbedre seg over tid. Minne er grunnlaget for å skape en selvforbedrende agent som kan skape bedre opplevelser for brukerne våre.

I denne leksjonen skal vi se på hva minne er for AI-agenter og hvordan vi kan administrere det og bruke det til fordel for applikasjonene våre.

## Introduksjon

Denne leksjonen vil dekke:

• **Forstå AI-agentminne**: Hva minne er og hvorfor det er viktig for agenter.

• **Implementere og lagre minne**: Praktiske metoder for å legge til minnekapasiteter til AI-agenter, med fokus på korttids- og langtidsminne.

• **Gjøre AI-agenter selvforbedrende**: Hvordan minne gjør det mulig for agenter å lære fra tidligere interaksjoner og forbedre seg over tid.

## Tilgjengelige implementeringer

Denne leksjonen inkluderer to omfattende notatbøker:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerer minne ved bruk av Mem0 og Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerer strukturert minne med Cognee, som automatisk bygger kunnskapsgraf støttet av embeddings, visualiserer grafen, og intelligent gjenfinning

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

• **Skille mellom ulike typer AI-agentminne**, inkludert arbeidsminne, korttidsminne og langtidsminne, samt spesialiserte former som persona- og episodisk minne.

• **Implementere og administrere korttids- og langtidsminne for AI-agenter** ved bruk av Microsoft Agent Framework, og utnytte verktøy som Mem0, Cognee, Whiteboard memory, og integrere med Azure AI Search.

• **Forstå prinsippene bak selvforbedrende AI-agenter** og hvordan robuste minnehåndteringssystemer bidrar til kontinuerlig læring og tilpasning.

## Forstå AI-agentminne

I kjernen refererer **minne for AI-agenter til mekanismene som tillater dem å beholde og hente informasjon**. Denne informasjonen kan være spesifikke detaljer om en samtale, brukerpreferanser, tidligere handlinger eller til og med lærte mønstre.

Uten minne er AI-applikasjoner ofte statsløse, noe som betyr at hver interaksjon starter fra bunnen av. Dette fører til en repetitiv og frustrerende brukeropplevelse hvor agenten "glemmer" tidligere kontekst eller preferanser.

### Hvorfor er minne viktig?

En agents intelligens er dypt knyttet til dens evne til å hente og bruke tidligere informasjon. Minne gjør det mulig for agenter å være:

• **Reflekterende**: Lære av tidligere handlinger og utfall.

• **Interaktive**: Opprettholde kontekst gjennom en pågående samtale.

• **Proaktive og reaktive**: Forutse behov eller svare passende basert på historiske data.

• **Autonome**: Operere mer uavhengig ved å trekke på lagret kunnskap.

Målet med å implementere minne er å gjøre agenter mer **pålitelige og kapable**.

### Typer minne

#### Arbeidsminne

Tenk på dette som et notatark en agent bruker under en enkelt, pågående oppgave eller tankeprosess. Det holder umiddelbar informasjon som trengs for å beregne neste steg.

For AI-agenter fanger arbeidsminnet ofte den mest relevante informasjonen fra en samtale, selv om hele chatthistorikken er lang eller avkortet. Det fokuserer på å trekke ut nøkkel-elementer som krav, forslag, beslutninger og handlinger.

**Eksempel på arbeidsminne**

I en reisebestillingsagent kan arbeidsminnet fange brukerens nåværende forespørsel, som for eksempel "Jeg vil bestille en tur til Paris". Dette spesifikke kravet holdes i agentens umiddelbare kontekst for å veilede den pågående interaksjonen.

#### Korttidsminne

Denne typen minne beholder informasjon i løpet av én enkelt samtale eller økt. Det er konteksten for den nåværende chatten, som lar agenten referere tilbake til tidligere deler av dialogen.

I [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK-eksempler tilsvarer dette `AgentSession`, opprettet med `agent.create_session()`. Økten er rammeverkets innebygde korttidsminne: det holder samtalekontekst tilgjengelig mens samme økt gjenbrukes, men denne konteksten lagres ikke når økten avsluttes eller applikasjonen startes på nytt. Bruk langtidsminne for fakta og preferanser som må overleve på tvers av økter, vanligvis via en database, vektorindeks eller annen vedvarende lagring.

**Eksempel på korttidsminne**

Hvis en bruker spør, "Hvor mye koster en flybillett til Paris?" og følger opp med "Hva med overnatting der?", sørger korttidsminnet for at agenten vet at "der" refererer til "Paris" innenfor samme samtale.

#### Langtidsminne

Dette er informasjon som vedvarer over flere samtaler eller økter. Det tillater agenter å huske brukerpreferanser, historiske interaksjoner eller generell kunnskap over lengre tid. Dette er viktig for personalisering.

**Eksempel på langtidsminne**

Langtidsminnet kan lagre at "Ben liker ski og utendørsaktiviteter, foretrekker kaffe med fjordutsikt, og ønsker å unngå avanserte skibakker på grunn av en tidligere skade". Denne informasjonen, lært fra tidligere interaksjoner, påvirker anbefalinger i fremtidige reiseplanleggingsøkter, noe som gjør dem høyst personlig tilpasset.

#### Persona-minne

Denne spesialiserte minnetypen hjelper en agent å utvikle en konsistent "personlighet" eller "persona". Det lar agenten huske detaljer om seg selv eller sin tiltenkte rolle, noe som gjør interaksjoner mer flytende og målrettet.

**Eksempel på persona-minne**

Hvis reiseagenten er designet som en "ekspert på ski-planlegging," kan persona-minnet forsterke denne rollen, og påvirke svarene slik at de samsvarer med en eksperts tone og kunnskap.

#### Arbeidsflyt-/episodisk minne

Dette minnet lagrer sekvensen av steg en agent tar under en kompleks oppgave, inkludert suksesser og feil. Det er som å huske spesifikke "episoder" eller tidligere erfaringer for å lære av dem.

**Eksempel på episodisk minne**

Hvis agenten forsøkte å bestille en spesifikk flybillett, men det mislyktes på grunn av utilgjengelighet, kan episodisk minne registrere denne feilen. Det tillater agenten å prøve alternative flyvninger eller informere brukeren om problemet på en bedre opplyst måte ved neste forsøk.

#### Entitetsminne

Dette innebærer å trekke ut og huske spesifikke enheter (som personer, steder eller ting) og hendelser fra samtaler. Det lar agenten bygge en strukturert forståelse av sentrale elementer som diskuteres.

**Eksempel på entitetsminne**

Fra en samtale om en tidligere tur kan agenten trekke ut "Paris," "Eiffeltårnet," og "middag på Le Chat Noir-restaurant" som enheter. I en fremtidig interaksjon kan agenten huske "Le Chat Noir" og tilby å gjøre en ny reservasjon der.

#### Strukturert RAG (Retrieval Augmented Generation)

Mens RAG er en bredere teknikk, fremheves "Strukturert RAG" som en kraftig minneteknologi. Den trekker ut tett, strukturert informasjon fra ulike kilder (samtaler, e-poster, bilder) og bruker dette for å forbedre presisjon, tilbakekalling og hastighet i svarene. I motsetning til klassisk RAG som baserer seg kun på semantisk likhet, jobber Strukturert RAG med den iboende strukturen i informasjonen.

**Eksempel på strukturert RAG**

I stedet for bare å matche nøkkelord kan Strukturert RAG analysere flydetaljer (destinasjon, dato, tid, flyselskap) fra en e-post og lagre dem på en strukturert måte. Dette muliggjør presise spørringer som "Hvilket fly booket jeg til Paris på tirsdag?"

## Implementere og lagre minne

Implementering av minne for AI-agenter innebærer en systematisk prosess for **minnehåndtering**, som inkluderer generering, lagring, gjenfinning, integrering, oppdatering og til og med "glemming" (eller sletting) av informasjon. Gjenfinning er et spesielt viktig aspekt.

### Spesialiserte minneverktøy

#### Mem0

En måte å lagre og administrere agentminne på, er ved bruk av spesialiserte verktøy som Mem0. Mem0 fungerer som et vedvarende minnelag, som gjør det mulig for agenter å hente relevante interaksjoner, lagre brukerpreferanser og faktakontekst, og lære av suksesser og feil over tid. Ideen er at statsløse agenter blir til tilstandsbevarende.

Det fungerer gjennom en **to-fase minneprosess: utvinning og oppdatering**. Først sendes meldinger lagt til en agents tråd til Mem0-tjenesten, som bruker en stor språkmodell (LLM) til å oppsummere samtalehistorikk og trekke ut nye minner. Deretter avgjør en LLM-basert oppdateringsfase om minnene skal legges til, endres eller slettes, og lagrer dem i en hybrid databutikk som kan inkludere vektor-, graf- og nøkkel-verdi-databaser. Systemet støtter også ulike minnetyper og kan inkludere grafminne for å administrere relasjoner mellom enheter.

#### Cognee

En annen kraftfull tilnærming er bruk av **Cognee**, et åpen kildekode-semantisk minne for AI-agenter som forvandler strukturert og ustrukturert data til søkbare kunnskapsgrafer støttet av embeddings. Cognee tilbyr en **to-lagers arkitektur** som kombinerer vektorsøk etter likhet med grafrelasjoner, og gjør det mulig for agenter å forstå ikke bare hva informasjon er lik, men hvordan konsepter relaterer til hverandre.

Den utmerker seg i **hybrid gjenfinning** som blander vektorsimilartet, grafstruktur og LLM-resonnering — fra rå oppslag av tekstbiter til grafbevisst spørsmål-og-svar. Systemet opprettholder et **levende minne** som utvikler seg og vokser mens det forblir søkbart som én sammenkoblet graf, støttende både korttids øktkontekst og langtids vedvarende minne.

Cognee-notatboken ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrerer bygging av dette enhetlige minnelaget, med praktiske eksempler på å hente inn ulike datakilder, visualisere kunnskapsgrafen og søke med forskjellige søkstrategier tilpasset spesifikke agentbehov.

### Lagring av minne med RAG

Utover spesialiserte minneverktøy som Mem0, kan du utnytte robuste søketjenester som **Azure AI Search som backend for lagring og gjenfinning av minner**, spesielt for strukturert RAG.

Dette gjør det mulig å forankre agentens svar med dine egne data, og sikrer mer relevante og nøyaktige svar. Azure AI Search kan brukes for å lagre bruker-spesifikke reiseminner, produktkataloger, eller annen domene-spesifikk kunnskap.

Azure AI Search støtter funksjoner som **Strukturert RAG**, som utmerker seg i å trekke ut og hente tett, strukturert informasjon fra store datasett som samtalehistorikker, e-poster, eller til og med bilder. Dette gir "supermenneskelig presisjon og tilbakekalling" sammenlignet med tradisjonelle tekstbiter og embedding-tilnærminger.

## Gjøre AI-agenter selvforbedrende

Et vanlig mønster for selvforbedrende agenter innebærer å introdusere en **"kunnskapsagent"**. Denne separate agenten observerer hovedsamtalen mellom brukeren og den primære agenten. Dens rolle er å:

1. **Identifisere verdifull informasjon**: Bestemme om noen deler av samtalen er verdt å lagre som generell kunnskap eller en spesifikk brukerpreferanse.

2. **Utvinn og oppsummer**: Destillere det essensielle læringspunktet eller preferansen fra samtalen.

3. **Lagre i en kunnskapsbase**: Persistere denne utvunnede informasjonen, ofte i en vektordatabse, slik at den kan hentes senere.

4. **Berike fremtidige spørringer**: Når brukeren starter en ny forespørsel, henter kunnskapsagenten relevant lagret informasjon og legger den til i brukerens prompt, og gir viktig kontekst til den primære agenten (lignende RAG).

### Optimaliseringer for minne

• **Latensstyring**: For å unngå å bremse brukerinteraksjoner, kan en billigere, raskere modell brukes innledningsvis for å raskt sjekke om informasjon er verdt å lagre eller hente, og bare kalle den mer komplekse utvinnings-/gjenfinningsprosessen når nødvendig.

• **Vedlikehold av kunnskapsbase**: For en voksende kunnskapsbase kan sjeldnere brukt informasjon flyttes til "kaldlagring" for å håndtere kostnader.

## Har du flere spørsmål om agentminne?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortid og få svar på dine spørsmål om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->