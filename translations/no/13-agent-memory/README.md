# Minne for AI-agenter  
[![Agent Memory](../../../translated_images/no/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Når vi diskuterer de unike fordelene ved å lage AI-agenter, er to ting hovedsakelig i fokus: evnen til å kalle verktøy for å utføre oppgaver og evnen til å forbedre seg over tid. Minne er grunnlaget for å skape selvforbedrende agenter som kan skape bedre opplevelser for brukerne våre.

I denne leksjonen skal vi se på hva minne er for AI-agenter og hvordan vi kan håndtere det og bruke det til fordel for våre applikasjoner.

## Introduksjon

Denne leksjonen vil dekke:

• **Forståelse av AI-agentminne**: Hva minne er og hvorfor det er viktig for agenter.

• **Implementering og lagring av minne**: Praktiske metoder for å legge til minnefunksjoner i AI-agentene dine, med fokus på korttids- og langtidsminne.

• **Gjøre AI-agenter selvforbedrende**: Hvordan minne muliggjør at agenter lærer fra tidligere interaksjoner og forbedrer seg over tid.

## Tilgjengelige implementasjoner

Denne leksjonen inkluderer to omfattende notatbøker:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerer minne ved bruk av Mem0 og Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerer strukturert minne ved bruk av Cognee, bygger automatisk kunnskapsgraf støttet av embeddings, visualiserer grafen og intelligent gjenfinning

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

• **Skille mellom ulike typer AI-agentminne**, inkludert arbeidsminne, korttidsminne og langtidsminne, samt spesialiserte former som persona- og episodisk minne.

• **Implementere og administrere korttids- og langtidsminne for AI-agenter** ved bruk av Microsoft Agent Framework, med verktøy som Mem0, Cognee, Whiteboard-minne, og integrasjon med Azure AI Search.

• **Forstå prinsippene bak selvforbedrende AI-agenter** og hvordan robuste minnestyringssystemer bidrar til kontinuerlig læring og tilpasning.

## Forståelse av AI-agentminne

I sin kjerne refererer **minne for AI-agenter til mekanismer som lar dem beholde og hente informasjon**. Denne informasjonen kan være spesifikke detaljer om en samtale, brukerpreferanser, tidligere handlinger eller til og med lærte mønstre.

Uten minne er AI-applikasjoner ofte tilstandsløse, noe som betyr at hver interaksjon starter fra bunnen av. Dette fører til en repeterende og frustrerende brukeropplevelse hvor agenten "glemmer" tidligere kontekst eller preferanser.

### Hvorfor er minne viktig?

En agents intelligens er dypt knyttet til dens evne til å huske og bruke tidligere informasjon. Minne lar agenter være:

• **Reflekterende**: Lære av tidligere handlinger og resultater.

• **Interaktive**: Opprettholde kontekst gjennom en pågående samtale.

• **Proaktive og reaktive**: Forutse behov eller respondere passende basert på historiske data.

• **Autonome**: Operere mer selvstendig ved å bruke lagret kunnskap.

Målet med å implementere minne er å gjøre agenter mer **pålitelige og kapable**.

### Typer minne

#### Arbeidsminne

Tenk på dette som et notatark en agent bruker under en enkelt, pågående oppgave eller tankerekke. Det holder umiddelbar informasjon som trengs for å utføre neste steg.

For AI-agenter fanger arbeidsminne ofte den mest relevante informasjonen fra en samtale, selv om hele chatthistorikken er lang eller forkortet. Det fokuserer på å hente ut nøkkeldetaljer som krav, forslag, beslutninger og handlinger.

**Eksempel på arbeidsminne**

I en reisebestillingsagent kan arbeidsminnet fange brukerens nåværende forespørsel, som "Jeg ønsker å bestille en tur til Paris". Dette spesifikke kravet holdes i agentens umiddelbare kontekst for å styre den pågående interaksjonen.

#### Korttidsminne

Denne typen minne beholder informasjon for varigheten av en enkelt samtale eller økt. Det er konteksten i den nåværende chatten, som gjør at agenten kan referere tilbake til tidligere turer i dialogen.

I [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK-eksempler tilsvarer dette `AgentSession`, opprettet med `agent.create_session()`. Økten er rammeverkets innebygde korttidsminne: den holder samtalekontekst tilgjengelig så lenge samme økt gjenbrukes, men den konteksten lagres ikke når økten avsluttes eller applikasjonen starter på nytt. Bruk langtidsminne for fakta og preferanser som må bevares på tvers av økter, typisk gjennom en database, vektorindeks eller annen persisterende lagring.

**Eksempel på korttidsminne**

Hvis en bruker spør, "Hvor mye koster en flybillett til Paris?" og følger opp med "Hva med overnatting der?", sørger korttidsminnet for at agenten vet at "der" refererer til "Paris" i samme samtale.

#### Langtidsminne

Dette er informasjon som vedvarer over flere samtaler eller økter. Det lar agenter huske brukerpreferanser, historiske interaksjoner eller generell kunnskap over lengre tid. Dette er viktig for personalisering.

**Eksempel på langtidsminne**

Et langtidsminne kan lagre at "Ben liker ski og utendørsaktiviteter, foretrekker kaffe med fjellutsikt, og vil unngå avanserte skibakker på grunn av en tidligere skade." Denne informasjonen, lært fra tidligere interaksjoner, påvirker anbefalinger i fremtidige reiseplanleggingsøkter, og gjør dem svært personlige.

#### Persona-minne

Denne spesialiserte minnetypen hjelper en agent med å utvikle en konsistent "personlighet" eller "persona". Det gjør at agenten kan huske detaljer om seg selv eller sin tiltenkte rolle, noe som gjør interaksjoner mer flytende og målrettede.

**Eksempel på persona-minne**

Hvis reiseagenten er designet som en "ekspert på skiplanlegging", kan persona-minnet forsterke denne rollen og påvirke svarene slik at de stemmer overens med en eksperts tone og kunnskap.

#### Workflow/Episodisk minne

Dette minnet lagrer rekkefølgen av trinn en agent tar under en kompleks oppgave, inkludert suksesser og feil. Det er som å huske spesifikke "episoder" eller tidligere erfaringer for å lære av dem.

**Eksempel på episodisk minne**

Hvis agenten prøvde å bestille en bestemt flyvning, men det mislyktes på grunn av mangel på tilgjengelighet, kan episodisk minne ta opp denne feilen, slik at agenten kan prøve alternative flyvninger eller informere brukeren bedre ved en ny forsøk.

#### Entitetsminne

Dette innebærer å hente ut og huske spesifikke entiteter (som personer, steder eller ting) og hendelser fra samtaler. Det lar agenten bygge en strukturert forståelse av viktige elementer som diskuteres.

**Eksempel på entitetsminne**

Fra en samtale om en tidligere tur kan agenten hente ut "Paris", "Eiffeltårnet" og "middag på Le Chat Noir-restaurant" som entiteter. Ved en senere interaksjon kan agenten huske "Le Chat Noir" og tilby å gjøre en ny reservasjon der.

#### Strukturert RAG (Retrieval Augmented Generation)

Mens RAG er en bredere teknikk, fremheves "Strukturert RAG" som en kraftfull minneteknologi. Den henter ut tett, strukturert informasjon fra forskjellige kilder (samtaler, e-poster, bilder) og bruker dette for å forbedre presisjon, gjenfinning og hastighet i svar. I motsetning til klassisk RAG som bare baserer seg på semantisk likhet, arbeider Strukturert RAG med den iboende strukturen i informasjonen.

**Eksempel på strukturert RAG**

I stedet for bare å matche nøkkelord, kan Strukturert RAG analysere flydetaljer (destinasjon, dato, tid, flyselskap) fra en e-post og lagre dem på en strukturert måte. Dette tillater presise spørsmål som "Hvilken flyvning bestilte jeg til Paris på tirsdag?"

## Implementering og lagring av minne

Å implementere minne for AI-agenter innebærer en systematisk prosess for **minnestyring**, som inkluderer generering, lagring, gjenfinning, integrering, oppdatering og til og med "glemming" (eller sletting) av informasjon. Gjenfinning er et spesielt viktig aspekt.

### Spesialiserte minneverktøy

#### Mem0

En måte å lagre og administrere agentminne på er å bruke spesialiserte verktøy som Mem0. Mem0 fungerer som et persistent minnelag, som lar agenter hente relevante interaksjoner, lagre brukerpreferanser og faktuell kontekst, og lære av suksesser og feil over tid. Tanken her er at tilstandsløse agenter blir til tilstandsbevarende.

Det fungerer gjennom en **to-fase minneprosess: utvinning og oppdatering**. Først sendes meldinger lagt til i en agents tråd til Mem0-tjenesten, som bruker en stor språkmodell (LLM) for å oppsummere samtalehistorikk og trekke ut nye minner. Deretter avgjør en LLM-drevet oppdateringsfase om disse minnene skal legges til, endres eller slettes, og lagrer dem i en hybrid database som kan inkludere vektor-, graf- og nøkkel-verdi-databaser. Systemet støtter også forskjellige minnetyper og kan inkludere grafminne for å håndtere relasjoner mellom entiteter.

#### Cognee

En annen kraftfull tilnærming er å bruke **Cognee**, et åpen kildekode semantisk minne for AI-agenter som omdanner strukturert og ustrukturert data til søkbare kunnskapsgrafer støttet av embeddings. Cognee tilbyr en **dual-store arkitektur** som kombinerer vektorlignende søk med grafrelasjoner, noe som gjør at agenter kan forstå ikke bare hvilken informasjon som er lik, men også hvordan konsepter henger sammen.

Det utmerker seg i **hybrid gjenfinning** som blander vektorlignende søk, grafstruktur og LLM-resonnering – fra rå chunk-lokalisering til grafbevisst spørsmålssvar. Systemet opprettholder et **levende minne** som utvikler seg og vokser mens det forblir søkbart som en sammenhengende graf, og støtter både korttids øktsammenheng og langtids vedvarende minne.

Cognee-notatbokopplæringen ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrerer bygging av dette sammenslåtte minnelaget, med praktiske eksempler på innlesing av ulike datakilder, visualisering av kunnskapsgrafen og spørring med forskjellige søkestrategier tilpasset agentenes spesifikke behov.

### Lagring av minne med RAG

Utover spesialiserte minneverktøy som Mem0, kan du bruke robuste søketjenester som **Azure AI Search som backend for lagring og gjenfinning av minner**, spesielt for strukturert RAG.

Dette lar deg forankre agentens svar med dine egne data, og sikrer mer relevante og presise svar. Azure AI Search kan brukes til å lagre bruker-spesifikke reise-minner, produktkataloger eller annen domenespesifikk kunnskap.

Azure AI Search støtter funksjoner som **Strukturert RAG**, som utmerker seg i å hente ut og gjenfinne tett, strukturert informasjon fra store datasett som samtalehistorikk, e-post eller til og med bilder. Dette gir "overmenneskelig presisjon og gjenfinning" sammenlignet med tradisjonelle tilnærminger basert på tekstchunking og embedding.

## Gjøre AI-agenter selvforbedrende

Et vanlig mønster for selvforbedrende agenter innebærer å introdusere en **"kunnskapsagent"**. Denne separate agenten observerer hovedsamtalen mellom brukeren og den primære agenten. Dens rolle er å:

1. **Identifisere verdifull informasjon**: Bestemme om deler av samtalen er verdt å lagre som generell kunnskap eller spesifikke brukerpreferanser.

2. **Uttrekk og oppsummering**: Destillere læring eller preferanse fra samtalen.

3. **Lagre i en kunnskapsbase**: Persistere denne uttrukne informasjonen, ofte i en vektordatabases, slik at den kan hentes frem senere.

4. **Berike fremtidige spørringer**: Når brukeren starter en ny spørring henter kunnskapsagenten relevant lagret informasjon og legger det til brukerens prompt, og gir avgjørende kontekst til hovedagenten (likt RAG).

### Optimaliseringer for minne

• **Latensstyring**: For å unngå at brukerinteraksjoner forsinkes, kan en rimeligere, raskere modell brukes først for raskt å sjekke om informasjon er verdt å lagre eller hente, og bare kalle den mer komplekse utvinnings-/gjenfinningsprosessen når det trengs.

• **Vedlikehold av kunnskapsbase**: For en voksende kunnskapsbase kan mindre brukt informasjon flyttes til "kaldlagring" for å redusere kostnader.

## Har du flere spørsmål om agentminne?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på spørsmål om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->