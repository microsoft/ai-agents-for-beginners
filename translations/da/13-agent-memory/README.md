# Hukommelse for AI-agenter
[![Agent Memory](../../../translated_images/da/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Når man diskuterer de unikke fordele ved at skabe AI-agenter, er der to ting, der primært diskuteres: evnen til at kalde værktøjer for at fuldføre opgaver og evnen til at forbedre sig over tid. Hukommelse er grundlaget for at skabe en selvforbedrende agent, der kan skabe bedre oplevelser for vores brugere.

I denne lektion vil vi se på, hvad hukommelse er for AI-agenter, og hvordan vi kan håndtere den og bruge den til fordel for vores applikationer.

## Introduktion

Denne lektion dækker:

• **Forståelse af AI-agenthukommelse**: Hvad hukommelse er, og hvorfor det er essentielt for agenter.

• **Implementering og lagring af hukommelse**: Praktiske metoder til at tilføje hukommelsesfunktioner til dine AI-agenter med fokus på korttids- og langtidshukommelse.

• **Gøre AI-agenter selvforbedrende**: Hvordan hukommelse gør det muligt for agenter at lære af tidligere interaktioner og forbedre sig over tid.

## Tilgængelige implementeringer

Denne lektion inkluderer to omfattende notebook-tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerer hukommelse ved hjælp af Mem0 og Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerer struktureret hukommelse ved hjælp af Cognee, der automatisk bygger en viden-graf bakket op af embeddings, visualiserer grafen og intelligent genfinding

## Læringsmål

Efter denne lektion vil du kunne:

• **Skelne mellem forskellige typer af AI-agenthukommelse**, inklusive arbejdshukommelse, korttids- og langtidshukommelse samt specialiserede former som persona- og episodisk hukommelse.

• **Implementere og administrere korttids- og langtidshukommelse for AI-agenter** ved hjælp af Microsoft Agent Framework, med værktøjer som Mem0, Cognee, Whiteboard memory, og integration med Azure AI Search.

• **Forstå principperne bag selvforbedrende AI-agenter** og hvordan robuste hukommelsesstyringssystemer bidrager til kontinuerlig læring og tilpasning.

## Forståelse af AI-agenthukommelse

Grundlæggende refererer **hukommelse for AI-agenter til de mekanismer, der gør det muligt for dem at bevare og genkalde information**. Denne information kan være specifikke detaljer om en samtale, brugerpræferencer, tidligere handlinger eller endda lærte mønstre.

Uden hukommelse er AI-applikationer ofte tilstandsløse, hvilket betyder, at hver interaktion starter forfra. Det fører til en gentagende og frustrerende brugeroplevelse, hvor agenten "glemmer" tidligere kontekst eller præferencer.

### Hvorfor er hukommelse vigtig?

En agents intelligens er dybt knyttet til dens evne til at genkalde og anvende tidligere information. Hukommelse gør det muligt for agenter at være:

• **Reflekterende**: Lære af tidligere handlinger og resultater.

• **Interaktive**: Opretholde kontekst over en igangværende samtale.

• **Proaktive og reaktive**: Forudse behov eller reagere passende baseret på historiske data.

• **Autonome**: Operere mere uafhængigt ved at trække på lagret viden.

Målet med at implementere hukommelse er at gøre agenter mere **pålidelige og kapable**.

### Typer af hukommelse

#### Arbejdshukommelse

Tænk på dette som et stykke skitsepapir, en agent bruger under en enkelt, igangværende opgave eller tankeproces. Det indeholder øjeblikkelig information, der er nødvendig for at beregne det næste skridt.

For AI-agenter fanger arbejdshukommelse ofte den mest relevante information fra en samtale, selv hvis hele chat-historikken er lang eller forkortet. Den fokuserer på at udtrække nøgleelementer som krav, forslag, beslutninger og handlinger.

**Eksempel på arbejdshukommelse**

I en rejsebookingsagent kan arbejdshukommelsen fange brugerens nuværende anmodning, som "Jeg vil gerne booke en tur til Paris". Dette specifikke krav holdes i agentens umiddelbare kontekst for at styre den aktuelle interaktion.

#### Korttids-hukommelse

Denne type hukommelse bevarer information i løbet af en enkelt samtale eller session. Det er konteksten for den nuværende chat, som gør det muligt for agenten at referere tilbage til tidligere dialogtrin.

I [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK-eksempler svarer dette til `AgentSession`, oprettet med `agent.create_session()`. Sessionen er frameworkets indbyggede korttids-hukommelse: den holder samtalekonteksten tilgængelig, mens den samme session genbruges, men denne kontekst gemmes ikke, når sessionen afsluttes eller applikationen genstartes. Brug langtidshukommelse til fakta og præferencer, der skal overleve på tværs af sessioner, typisk gennem en database, vektorindeks eller en anden permanent lagring.

**Eksempel på korttids-hukommelse**

Hvis en bruger spørger, "Hvor meget koster en flybillet til Paris?" og derefter følger op med, "Hvad med overnatning der?", sikrer korttids-hukommelsen, at agenten ved, at "der" refererer til "Paris" inden for samme samtale.

#### Langtidshukommelse

Dette er information, der bevares på tværs af flere samtaler eller sessioner. Det gør det muligt for agenter at huske brugerpræferencer, historiske interaktioner eller generel viden over længere perioder. Dette er vigtigt for personalisering.

**Eksempel på langtidshukommelse**

En langtidshukommelse kunne gemme, at "Ben nyder skiløb og udendørsaktiviteter, kan lide kaffe med udsigt til bjergene, og ønsker at undgå avancerede skiløjper på grund af en tidligere skade". Denne information, lært fra tidligere interaktioner, påvirker anbefalinger i fremtidige rejseplanlægningssessioner og gør dem meget personlige.

#### Persona-hukommelse

Denne specialiserede hukommelsestype hjælper en agent med at udvikle en konsekvent "personlighed" eller "persona". Det gør det muligt for agenten at huske detaljer om sig selv eller sin tilsigtede rolle, hvilket gør interaktioner mere flydende og fokuserede.

**Eksempel på persona-hukommelse**
Hvis rejseagenten er designet til at være en "ekspert i skiplanlægning", kan persona-hukommelsen forstærke denne rolle og påvirke dens svar til at være i overensstemmelse med en eksperts tone og viden.

#### Workflow/Episodisk hukommelse

Denne hukommelse gemmer rækkefølgen af trin, en agent tager under en kompleks opgave, inklusive succeser og fejl. Det svarer til at huske specifikke "episoder" eller tidligere erfaringer for at lære af dem.

**Eksempel på episodisk hukommelse**

Hvis agenten forsøgte at booke en bestemt flyvning, men det mislykkedes på grund af utilgængelighed, kunne den episodiske hukommelse registrere denne fejl, så agenten kan prøve alternative flyvninger eller informere brugeren om problemet på en mere informeret måde ved et efterfølgende forsøg.

#### Entitetshukommelse

Dette indebærer at udtrække og huske specifikke enheder (som personer, steder eller ting) og begivenheder fra samtaler. Det gør det muligt for agenten at opbygge en struktureret forståelse af nøgleelementer, der er diskuteret.

**Eksempel på entitetshukommelse**

Fra en samtale om en tidligere tur kunne agenten udtrække "Paris", "Eiffeltårnet" og "middag på Le Chat Noir restaurant" som enheder. I en fremtidig interaktion kunne agenten huske "Le Chat Noir" og tilbyde at lave en ny reservation dér.

#### Struktureret RAG (Retrieval Augmented Generation)

Mens RAG er en bredere teknik, fremhæves "Struktureret RAG" som en kraftfuld hukommelsesteknologi. Den udtrækker tæt, struktureret information fra forskellige kilder (samtaler, e-mails, billeder) og bruger den til at øge præcision, tilbagekaldelse og hastighed i svarene. I modsætning til klassisk RAG, der kun baserer sig på semantisk lighed, arbejder Struktureret RAG med den iboende struktur i informationen.

**Eksempel på Struktureret RAG**

I stedet for blot at matche søgeord kunne Struktureret RAG udtrække flyoplysninger (destination, dato, tid, flyselskab) fra en e-mail og gemme dem på en struktureret måde. Det muliggør præcise forespørgsler som "Hvilken flyvning bookede jeg til Paris på tirsdag?"

## Implementering og lagring af hukommelse

Implementering af hukommelse for AI-agenter involverer en systematisk proces af **hukommelsesstyring**, som inkluderer generering, lagring, hentning, integration, opdatering og endda "glemsel" (eller sletning) af information. Hentning er et særligt vigtigt aspekt.

### Specialiserede hukommelsesværktøjer

#### Mem0

En måde at lagre og administrere agenthukommelse på er ved at bruge specialiserede værktøjer som Mem0. Mem0 fungerer som et vedvarende hukommelseslag, der gør det muligt for agenter at genkalde relevante interaktioner, lagre brugerpræferencer og faktuel kontekst samt lære af succeser og fejl over tid. Ideen er, at statsløse agenter bliver til tilstandsfyldte.

Det fungerer gennem en **to-fase hukommelses-pipeline: udtrækning og opdatering**. Først sendes meddelelser, der tilføjes til en agents tråd, til Mem0-tjenesten, som bruger en stor sprogmodel (LLM) til at opsummere samtalehistorik og udtrække nye minder. Herefter afgør en LLM-drevet opdateringsfase, om disse minder skal tilføjes, ændres eller slettes, og lagrer dem i en hybriddatastore, der kan inkludere vektor-, graf- og nøgle-værdi-databaser. Systemet understøtter også forskellige hukommelsestyper og kan inkorporere grafhukommelse til håndtering af relationer mellem enheder.

#### Cognee

En anden kraftfuld tilgang er at bruge **Cognee**, en open-source semantisk hukommelse for AI-agenter, der omdanner strukturerede og ustrukturerede data til forespørgselsbare vidensgrafer bakket op af embeddings. Cognee tilbyder en **dual-store arkitektur**, der kombinerer vektorsøgningssimilaritet med grafrelationer, hvilket gør det muligt for agenter at forstå ikke kun, hvad information ligner, men hvordan begreber relaterer til hinanden.

Det excellerer i **hybrid hentning**, der blander vektorsimilaritet, grafstruktur og LLM-resonering - fra rå chunk-opslag til graf-bevidst spørgesvar. Systemet opretholder en **levende hukommelse**, der udvikler sig og vokser, samtidig med at den forbliver forespørgselbar som en sammenhængende graf, der understøtter både korttids sessionkontekst og langtidshukommelse.

Cognee-notebook-tutorialen ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrerer opbygning af dette enheds-hukommelseslag med praktiske eksempler på at indtage forskellige datakilder, visualisere vidensgrafen og forespørge med forskellige søgestrategier, tilpasset specifikke agentbehov.

### Lagring af hukommelse med RAG

Udover specialiserede hukommelsesværktøjer som Mem0 kan du bruge robuste søgetjenester som **Azure AI Search som backend til lagring og hentning af minder**, især for struktureret RAG.

Dette gør det muligt at forankre din agents svar i dine egne data og sikre mere relevante og præcise svar. Azure AI Search kan bruges til at lagre bruger-specifikke rejseminder, produktkataloger eller anden domænespecifik viden.

Azure AI Search understøtter funktioner som **Struktureret RAG**, der excellerer i at udtrække og hente tæt, struktureret information fra store datasæt som samtalehistorikker, e-mails eller endda billeder. Dette giver "supermenneskelig præcision og tilbagekaldelse" sammenlignet med traditionelle tekstchunking- og embedding-tilgange.

## Gøre AI-agenter selvforbedrende

Et almindeligt mønster for selvforbedrende agenter involverer introduktionen af en **"vidensagent"**. Denne separate agent observerer hovedsamtalen mellem brugeren og den primære agent. Dens rolle er at:

1. **Identificere værdifuld information**: Bestemme om nogen del af samtalen er værd at gemme som generel viden eller en specifik brugerpræference.

2. **Udtrække og opsummere**: Destillere den essentielle læring eller præference fra samtalen.

3. **Gem i en vidensbase**: Bevare denne udtrukne information, ofte i en vektordatabase, så den kan hentes senere.

4. **Forstærke fremtidige forespørgsler**: Når brugeren igangsætter en ny forespørgsel, henter vidensagenten relevant lagret information og føjer den til brugerens prompt, hvilket giver vigtig kontekst til den primære agent (ligesom RAG).

### Optimeringer for hukommelse

• **Latency-styring**: For at undgå at forsinke brugerinteraktioner kan en billigere og hurtigere model bruges først til hurtigt at tjekke, om information er værd at lagre eller hente, og kun påkalde den mere komplekse udtræknings-/hentningsproces, når nødvendigt.

• **Vedligeholdelse af vidensbase**: For en voksende vidensbase kan sjældnere brugt information flyttes til "kold lagring" for at styre omkostninger.

## Har du flere spørgsmål om agenthukommelse?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at mødes med andre elever, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->