# Hukommelse for AI-agenter 
[![Agent Memory](../../../translated_images/da/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Når man diskuterer de unikke fordele ved at skabe AI-agenter, er det især to ting, der drøftes: evnen til at kalde værktøjer for at udføre opgaver og evnen til at forbedre sig over tid. Hukommelse er fundamentet for at skabe selvforbedrende agenter, der kan skabe bedre oplevelser for vores brugere.

I denne lektion vil vi se på, hvad hukommelse er for AI-agenter, og hvordan vi kan administrere og bruge den til gavn for vores applikationer.

## Introduktion

Denne lektion vil dække:

• **Forståelse af AI-agenters hukommelse**: Hvad hukommelse er, og hvorfor det er vigtigt for agenter.

• **Implementering og lagring af hukommelse**: Praktiske metoder til at tilføje hukommelsesfunktioner til dine AI-agenter med fokus på korttids- og langtidshukommelse.

• **Gøre AI-agenter selvforbedrende**: Hvordan hukommelse gør det muligt for agenter at lære af tidligere interaktioner og forbedre sig over tid.

## Tilgængelige implementeringer

Denne lektion inkluderer to omfattende notebook tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerer hukommelse ved hjælp af Mem0 og Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerer struktureret hukommelse ved hjælp af Cognee, der automatisk opbygger en vidensgraf understøttet af embeddings, visualiserer grafen og intelligent hentning

## Læringsmål

Efter at have gennemført denne lektion vil du vide, hvordan man:

• **Skelner mellem forskellige typer AI-agenthukommelse**, herunder arbejdshukommelse, korttidshukommelse og langtidshukommelse samt specialiserede former som persona- og episodisk hukommelse.

• **Implementerer og administrerer korttids- og langtidshukommelse for AI-agenter** ved brug af Microsoft Agent Framework, samtidig med at man udnytter værktøjer som Mem0, Cognee, Whiteboard-hukommelse og integration med Azure AI Search.

• **Forstår principperne bag selvforbedrende AI-agenter** og hvordan robuste hukommelsesstyringssystemer bidrager til kontinuerlig læring og tilpasning.

## Forståelse af AI-agenters hukommelse

I sin kerne refererer **hukommelse for AI-agenter til mekanismerne, der gør det muligt for dem at bevare og genkalde information**. Denne information kan være specifikke detaljer om en samtale, brugerpræferencer, tidligere handlinger eller endda lærte mønstre.

Uden hukommelse er AI-applikationer ofte tilstandsløse, hvilket betyder, at hver interaktion starter forfra. Dette fører til en gentagende og frustrerende brugeroplevelse, hvor agenten "glemmer" tidligere kontekst eller præferencer.

### Hvorfor er hukommelse vigtigt?

En agents intelligens er dybt knyttet til dens evne til at genkalde og bruge tidligere information. Hukommelse gør det muligt for agenter at være:

• **Reflekterende**: Lære af tidligere handlinger og resultater.

• **Interaktive**: Opretholde kontekst over en igangværende samtale.

• **Proaktive og Reaktive**: Forudse behov eller reagere passende baseret på historiske data.

• **Autonome**: Operere mere selvstændigt ved at trække på lagret viden.

Målet med at implementere hukommelse er at gøre agenter mere **pålidelige og kompetente**.

### Typer af hukommelse

#### Arbejdshukommelse

Tænk på dette som et stykke kladdepapir, som en agent bruger under en enkelt, igangværende opgave eller tankeproces. Det indeholder umiddelbar information, der er nødvendig for at beregne næste trin.

For AI-agenter fanger arbejdshukommelsen ofte den mest relevante information fra en samtale, selv hvis hele chat historikken er lang eller forkortet. Den fokuserer på at udtrække nøgleelementer som krav, forslag, beslutninger og handlinger.

**Eksempel på arbejdshukommelse**

I en rejsebookingsagent kunne arbejdshukommelsen fange brugerens aktuelle forespørgsel, såsom "Jeg vil gerne booke en tur til Paris". Dette specifikke krav opbevares i agentens umiddelbare kontekst for at vejlede den aktuelle interaktion.

#### Korttidshukommelse

Denne type hukommelse bevarer information i løbet af en enkelt samtale eller session. Det er konteksten i den aktuelle chat, der gør det muligt for agenten at referere tilbage til tidligere dialogtrin.

I [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK eksempler svarer dette til `AgentSession`, oprettet med `agent.create_session()`. Sessionen er frameworkets indbyggede korttidshukommelse: den holder samtalekonteksten tilgængelig, mens samme session genbruges, men den kontekst gemmes ikke, når sessionen slutter eller applikationen genstartes. Brug langtidshukommelse til fakta og præferencer, der skal bevares på tværs af sessioner, typisk gennem en database, vektorindeks eller en anden persistent lagring.

**Eksempel på korttidshukommelse**

Hvis en bruger spørger, "Hvor meget ville en flybillet til Paris koste?" og derefter følger op med "Hvad med overnatning der?", sikrer korttidshukommelsen, at agenten ved, at "der" refererer til "Paris" inden for samme samtale.

#### Langtidshukommelse

Dette er information, der bevares på tværs af flere samtaler eller sessioner. Det gør det muligt for agenter at huske brugerpræferencer, historiske interaktioner eller generel viden over længere perioder. Dette er vigtigt for personalisering.

**Eksempel på langtidshukommelse**

En langtidshukommelse kunne gemme, at "Ben nyder skiløb og udendørsaktiviteter, kan lide kaffe med bjergudsigt og ønsker at undgå avancerede pister på grund af en tidligere skade". Denne information, lært fra tidligere interaktioner, påvirker anbefalinger i fremtidige rejseplanlægningssessioner og gør dem meget personlige.

#### Persona-hukommelse

Denne specialiserede hukommelsestype hjælper en agent med at udvikle en konsekvent "personlighed" eller "persona". Den gør det muligt for agenten at huske detaljer om sig selv eller sin tiltænkte rolle, hvilket gør interaktioner mere flydende og fokuserede.

**Eksempel på persona-hukommelse**
Hvis rejseagenten er designet til at være en "ekspert i skilægningsplanlægning", kunne persona-hukommelsen forstærke denne rolle og påvirke dens svar til at matche en eksperts tone og viden.

#### Workflow-/episodisk hukommelse

Denne hukommelse gemmer rækkefølgen af trin, en agent tager under en kompleks opgave, inklusive succeser og fejl. Det svarer til at huske specifikke "episoder" eller tidligere oplevelser for at lære af dem.

**Eksempel på episodisk hukommelse**

Hvis agenten forsøgte at booke en bestemt flyvning, men det mislykkedes på grund af utilgængelighed, kunne episodisk hukommelse registrere denne fiasko, hvilket giver agenten mulighed for at prøve alternative flyvninger eller informere brugeren om problemet på en mere oplyst måde ved et senere forsøg.

#### Entitetshukommelse

Dette indebærer at udtrække og huske specifikke entiteter (som personer, steder eller ting) og begivenheder fra samtaler. Det gør det muligt for agenten at opbygge en struktureret forståelse af nøgleelementer, der er diskuteret.

**Eksempel på entitetshukommelse**

Fra en samtale om en tidligere rejse kunne agenten udtrække "Paris," "Eiffeltårnet" og "middag på Le Chat Noir-restaurant" som entiteter. Ved en fremtidig interaktion kunne agenten huske "Le Chat Noir" og tilbyde at lave en ny reservation der.

#### Struktureret RAG (Retrieval Augmented Generation)

Mens RAG er en bredere teknik, fremhæves "Struktureret RAG" som en kraftfuld hukommelsesteknologi. Den udtrækker tæt, struktureret information fra forskellige kilder (samtaler, e-mails, billeder) og bruger det til at forbedre præcision, genfinding og hastighed i svar. I modsætning til klassisk RAG, der kun bygger på semantisk lighed, arbejder Struktureret RAG med den iboende struktur i informationen.

**Eksempel på Struktureret RAG**

I stedet for blot at matche nøgleord kunne Struktureret RAG f.eks. parse flydetaljer (destination, dato, tid, flyselskab) fra en e-mail og gemme dem struktureret. Det tillader præcise forespørgsler som "Hvilken flyvning bookede jeg til Paris tirsdag?"

## Implementering og lagring af hukommelse

Implementering af hukommelse for AI-agenter involverer en systematisk proces for **hukommelsesstyring**, som inkluderer generering, lagring, hentning, integration, opdatering og endda "glemsel" (eller sletning) af information. Hentning er et særligt vigtigt aspekt.

### Specialiserede hukommelsesværktøjer

#### Mem0

En måde at lagre og administrere agenthukommelse på er ved at bruge specialiserede værktøjer som Mem0. Mem0 fungerer som et persistent hukommelseslag, der tillader agenter at genkalde relevante interaktioner, lagre brugerpræferencer og faktuel kontekst og lære af succeser og fejl over tid. Ideen her er, at tilstandsløse agenter bliver til tilstandsbevidste.

Det fungerer gennem en **to-faset hukommelsespipeline: ekstraktion og opdatering**. Først sendes beskeder tilføjet til en agents tråd til Mem0-tjenesten, som bruger en stor sprogmodel (LLM) til at opsummere samtalehistorik og udtrække nye minder. Derefter afgør en LLM-drevet opdateringsfase, om disse minder skal tilføjes, ændres eller slettes, og de lagres i en hybrid datalager, der kan inkludere vektor-, graf- og nøgleværdi-databaser. Systemet understøtter også forskellige hukommelsestyper og kan indarbejde grafhukommelse til styring af relationer mellem entiteter.

#### Cognee

En anden kraftfuld tilgang er at bruge **Cognee**, en open source semantisk hukommelse for AI-agenter, der omdanner strukturerede og ustrukturerede data til forespørgselsvenlige vidensgrafer understøttet af embeddings. Cognee tilbyder en **dual-store arkitektur**, der kombinerer vektorligningsøgning med grafrelationer, hvilket gør det muligt for agenter at forstå ikke blot hvad information der er lignende, men også hvordan begreber relaterer til hinanden.

Det udmærker sig ved **hybrid hentning**, der blander vektorlignings-, grafstruktur- og LLM-begrundelse - fra rå chunk-opslag til graf-bevidst spørgsmålssvar. Systemet opretholder **levende hukommelse**, som udvikler sig og vokser, mens det forbliver forespørgbart som én sammenkoblet graf, der understøtter både korttids sessionskontekst og langtidsholdbar persistent hukommelse.

Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrerer opbygning af dette forenede hukommelseslag med praktiske eksempler på indtagelse af forskellige datakilder, visualisering af vidensgraf og forespørgsler med forskellige søgestrategier skræddersyet til specifikke agentbehov.

### Lagring af hukommelse med RAG

Udover specialiserede hukommelsesværktøjer som Mem0 kan du udnytte robuste søgetjenester som **Azure AI Search som backend til lagring og hentning af minder**, især for struktureret RAG.

Dette gør det muligt at forankre agentens svar i dine egne data, hvilket sikrer mere relevante og nøjagtige svar. Azure AI Search kan bruges til at lagre brugerspecifikke rejseminder, produktkataloger eller anden domænespecifik viden.

Azure AI Search understøtter funktioner som **Struktureret RAG**, der udmærker sig i at udtrække og hente tæt, struktureret information fra store datasæt som samtalehistorik, e-mails eller endda billeder. Det giver "supermenneskelig præcision og genfinding" sammenlignet med traditionelle tekstchunking- og embedding-tilgange.

## Gøre AI-agenter selvforbedrende

Et almindeligt mønster for selvforbedrende agenter involverer at introducere en **"vidensagent"**. Denne separate agent observerer hovedsamtalen mellem brugeren og den primære agent. Dens rolle er at:

1. **Identificere værdifuld information**: Bestemme, om nogen del af samtalen er værd at gemme som generel viden eller en specifik brugerpræference.

2. **Udtrække og opsummere**: Destillere den væsentlige læring eller præference fra samtalen.

3. **Lagre i en vidensbase**: Gemme denne udtrukne information, ofte i en vektordatabse, så den kan hentes senere.

4. **Forstærke fremtidige forespørgsler**: Når brugeren initierer en ny forespørgsel, henter vidensagenten relevant gemt information og tilføjer den til brugerens prompt, hvilket giver afgørende kontekst til den primære agent (ligesom RAG).

### Optimeringer for hukommelse

• **Latensstyring**: For at undgå at sænke brugerinteraktioner kan en billigere og hurtigere model først bruges til hurtigt at tjekke, om information er værd at gemme eller hente, og først kalde den mere komplekse ekstraktions-/hentningsproces når nødvendigt.

• **Vedligeholdelse af vidensbase**: For en voksende vidensbase kan mindre brugt information flyttes til "kold lagring" for at styre omkostninger.

## Har du flere spørgsmål om agenthukommelse?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.
## Forrige lektion

[Context Engineering for AI Agents](../12-context-engineering/README.md)

## Næste lektion

[Exploring Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->