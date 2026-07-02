# Hukommelse til AI-agenter 
[![Agent Memory](../../../translated_images/da/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Når man diskuterer de unikke fordele ved at skabe AI-agenter, er der især to ting, der bliver talt om: evnen til at kalde værktøjer til at udføre opgaver og evnen til at forbedre sig over tid. Hukommelse er fundamentet for at skabe en selvforbedrende agent, der kan skabe bedre oplevelser for vores brugere.

I denne lektion vil vi se på, hvad hukommelse er for AI-agenter, og hvordan vi kan håndtere den og bruge den til fordel for vores applikationer.

## Introduktion

Denne lektion vil dække:

• **Forståelse af AI-agentens hukommelse**: Hvad hukommelse er, og hvorfor det er vigtigt for agenter.

• **Implementering og lagring af hukommelse**: Praktiske metoder til at tilføje hukommelsesfunktionalitet til dine AI-agenter med fokus på kort- og langtids hukommelse.

• **Gøre AI-agenter selvforbedrende**: Hvordan hukommelse gør det muligt for agenter at lære af tidligere interaktioner og forbedre sig over tid.

## Tilgængelige implementeringer

Denne lektion inkluderer to omfattende notebook-tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerer hukommelse ved hjælp af Mem0 og Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerer struktureret hukommelse ved hjælp af Cognee, som automatisk bygger vidensgraf understøttet af embeddings, visualiserer grafen og udfører intelligent opslag

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

• **Skelne mellem forskellige typer AI-agenters hukommelse**, herunder arbejdshukommelse, korttids- og langtids hukommelse samt specialiserede former som persona- og episodisk hukommelse.

• **Implementere og håndtere korttids- og langtids hukommelse for AI-agenter** ved hjælp af Microsoft Agent Framework, udnytte værktøjer som Mem0, Cognee, Whiteboard hukommelse og integrere med Azure AI Search.

• **Forstå principperne bag selvforbedrende AI-agenter** og hvordan robuste hukommelseshåndteringssystemer bidrager til kontinuerlig læring og tilpasning.

## Forståelse af AI-agenters hukommelse

I sin kerne henviser **hukommelse for AI-agenter til mekanismer, der gør det muligt for dem at bevare og tilbagekalde information**. Denne information kan være specifikke detaljer om en samtale, brugerpræferencer, tidligere handlinger eller endda lærte mønstre.

Uden hukommelse er AI-applikationer ofte statsløse, hvilket betyder at hver interaktion starter forfra. Dette fører til en gentagende og frustrerende brugeroplevelse, hvor agenten "glemmer" tidligere kontekst eller præferencer.

### Hvorfor er hukommelse vigtigt?

En agents intelligens er dybt forbundet med dens evne til at huske og anvende tidligere information. Hukommelse gør det muligt for agenter at være:

• **Reflekterende**: Lære fra tidligere handlinger og resultater.

• **Interaktive**: Opretholde kontekst gennem en igangværende samtale.

• **Proaktive og reaktive**: Forudse behov eller reagere hensigtsmæssigt baseret på historiske data.

• **Autonome**: Operere mere uafhængigt ved at trække på lagret viden.

Målet med at implementere hukommelse er at gøre agenter mere **pålidelige og kompetente**.

### Typer af hukommelse

#### Arbejdshukommelse

Tænk på dette som et stykke kladdepapir en agent bruger under en enkelt, igangværende opgave eller tankeproces. Den holder øjeblikkelig information, der er nødvendig for at beregne næste skridt.

For AI-agenter indfanger arbejdshukommelsen ofte de mest relevante oplysninger fra en samtale, selvom hele chat-historikken er lang eller afkortet. Den fokuserer på at udtrække nøgleelementer som krav, forslag, beslutninger og handlinger.

**Eksempel på arbejdshukommelse**

I en rejsebookingsagent kan arbejdshukommelsen fange brugerens aktuelle anmodning, som f.eks. "Jeg vil gerne booke en tur til Paris". Dette specifikke krav holdes i agentens umiddelbare kontekst for at styre den aktuelle interaktion.

#### Korttids hukommelse

Denne type hukommelse bevarer information i løbet af en enkelt samtale eller session. Det er konteksten for den nuværende chat, som gør det muligt for agenten at referere tilbage til tidligere udvekslinger i dialogen.

I [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK-eksempler svarer dette til `AgentSession`, oprettet med `agent.create_session()`. Sessionen er frameworkets indbyggede korttids hukommelse: den holder samtalekontext tilgængelig, mens samme session genbruges, men denne kontekst bevares ikke, når sessionen afsluttes eller applikationen genstartes. Brug langtids hukommelse til fakta og præferencer, som skal overleve på tværs af sessioner, typisk via en database, vektorindeks eller anden persistent lagring.

**Eksempel på korttids hukommelse**

Hvis en bruger spørger: "Hvor meget koster en flybillet til Paris?" og derefter følger op med "Hvad med indkvartering der?", sikrer korttids hukommelsen, at agenten ved, at "der" refererer til "Paris" inden for samme samtale.

#### Langtids hukommelse

Dette er information, der består på tværs af flere samtaler eller sessioner. Det gør det muligt for agenter at huske brugerpræferencer, historiske interaktioner eller generel viden over længere perioder. Dette er vigtigt for personalisering.

**Eksempel på langtids hukommelse**

En langtids hukommelse kunne gemme, at "Ben nyder skiløb og udendørs aktiviteter, kan lide kaffe med udsigt til bjerge, og ønsker at undgå avancerede skibakker på grund af en tidligere skade". Disse oplysninger, lært fra tidligere interaktioner, påvirker anbefalinger i fremtidige rejseplanlægningssessioner og gør dem meget personlige.

#### Persona-hukommelse

Denne specialiserede hukommelsestype hjælper en agent med at udvikle en konsistent "personlighed" eller "persona". Det gør det muligt for agenten at huske detaljer om sig selv eller sin tiltænkte rolle, hvilket gør interaktionerne mere flydende og fokuserede.

**Eksempel på persona-hukommelse**

Hvis rejseagenten er designet til at være en "ekspert inden for skiløb", kan persona-hukommelsen forstærke denne rolle og påvirke dens svar i tråd med en eksperts tone og viden.

#### Workflow/Episodisk hukommelse

Denne hukommelse lagrer rækkefølgen af trin, en agent tager under en kompleks opgave, inklusiv succeser og fejl. Det svarer til at huske specifikke "episoder" eller tidligere erfaringer for at lære af dem.

**Eksempel på episodisk hukommelse**

Hvis agenten forsøgte at booke en specifik flyvning, men det mislykkedes på grund af manglende tilgængelighed, kunne den episodiske hukommelse registrere denne fejl og dermed give agenten mulighed for at prøve alternative flyvninger eller informere brugeren om problemet på en mere velinformeret måde ved næste forsøg.

#### Entitetshukommelse

Dette indebærer udtrækning og lagring af specifikke entiteter (såsom personer, steder eller ting) og begivenheder fra samtaler. Det giver agenten mulighed for at opbygge en struktureret forståelse af nøgleelementer, der diskuteres.

**Eksempel på entitetshukommelse**

Fra en samtale om en tidligere rejse kan agenten udtrække "Paris", "Eiffeltårnet" og "middag på Le Chat Noir restaurant" som entiteter. Ved en fremtidig interaktion kunne agenten huske "Le Chat Noir" og tilbyde at lave en ny reservation der.

#### Struktureret RAG (Retrieval Augmented Generation)

Mens RAG er en bredere teknik, fremhæves "Struktureret RAG" som en kraftfuld hukommelsesteknologi. Den udtrækker tæt, struktureret information fra forskellige kilder (samtaler, e-mails, billeder) og bruger det til at forbedre præcision, recall og hastighed i svar. Modsat klassisk RAG, som udelukkende er baseret på semantisk lighed, arbejder Struktureret RAG med den iboende struktur i informationen.

**Eksempel på struktureret RAG**

I stedet for blot at matche nøgleord kan Struktureret RAG analysere flydetaljer (destination, dato, tid, flyselskab) fra en e-mail og lagre dem struktureret. Det muliggør præcise forespørgsler som "Hvilken flyvning bookede jeg til Paris på tirsdag?"

## Implementering og lagring af hukommelse

Implementering af hukommelse for AI-agenter involverer en systematisk proces af **hukommelseshåndtering**, som inkluderer generering, lagring, hentning, integration, opdatering og endda "glemsel" (eller sletning) af information. Hentning er et særligt vigtigt aspekt.

### Specialiserede hukommelsesværktøjer

#### Mem0

En måde at lagre og håndtere agenthukommelse på er at bruge specialiserede værktøjer som Mem0. Mem0 fungerer som et vedvarende hukommelseslag, der gør det muligt for agenter at huske relevante interaktioner, gemme brugerpræferencer og faktuel kontekst samt lære af succeser og fejl over tid. Ideen er her, at statsløse agenter bliver til tilstandsfyldte agenter.

Det fungerer gennem en **to-faset hukommelsespipeline: udtrækning og opdatering**. Først sendes beskeder, som tilføjes agentens tråd, til Mem0-tjenesten, der bruger en stor sprogmodel (LLM) til at opsummere samtalehistorikken og udtrække nye minder. Derefter bestemmer en opdateringsfase, drevet af LLM, om disse minder skal tilføjes, ændres eller slettes, og de lagres i en hybrid datalager, der kan inkludere vektor-, graf- og nøgle-værdi-databaser. Systemet understøtter også forskellige typer hukommelse og kan inkorporere grafhukommelse til håndtering af relationer mellem entiteter.

#### Cognee

En anden stærk tilgang er brug af **Cognee**, en open source semantisk hukommelse til AI-agenter, som omdanner strukturerede og ustrukturerede data til forespørgselsbare vidensgrafer understøttet af embeddings. Cognee tilbyder en **dobbeltdatabaseret arkitektur** der kombinerer vektorsøgning med grafrelationer, så agenter kan forstå ikke blot hvad informationer er ens, men hvordan begreber relaterer til hinanden.

Det excellerer i **hybrid hentning**, der blander vektorlighedhed, grafstruktur og LLM-reasoning – fra rå opslag i datastykker til graf-bevidst spørgsmål-svar. Systemet opretholder en **levende hukommelse**, der udvikler sig og vokser, mens den forbliver forespørgselsbar som én sammenhængende graf, hvilket understøtter både korttids session kontekst og langtids persistent hukommelse.

Cognee notebook-guiden ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrerer opbygning af dette samlede hukommelseslag med praktiske eksempler på indtastning af forskelligartede datakilder, visualisering af vidensgrafen og forespørgsler med forskellige søgestrategier tilpasset specifikke agentbehov.

### Lagring af hukommelse med RAG

Ud over specialiserede hukommelsesværktøjer som Mem0 kan du udnytte robuste søgetjenester som **Azure AI Search som en backend til lagring og hentning af minder**, især til struktureret RAG.

Dette gør det muligt for dig at forankre din agents svar i dine egne data, hvilket sikrer mere relevante og præcise svar. Azure AI Search kan bruges til at lagre bruger-specifikke rejsehukommelser, produktkataloger eller anden domænespecifik viden.

Azure AI Search understøtter funktioner som **Struktureret RAG**, der excellerer i at udtrække og hente tæt, struktureret information fra store datasæt som samtalehistorikker, e-mails eller endda billeder. Det giver "supermenneskelig præcision og recall" sammenlignet med traditionelle tekst-chunking og embedding-metoder.

## Gøre AI-agenter selvforbedrende

Et almindeligt mønster for selvforbedrende agenter involverer introduktion af en **"vidensagent"**. Denne separate agent observerer hovedsamtalen mellem brugeren og den primære agent. Dens rolle er at:

1. **Identificere værdifuld information**: Bestemme om nogen del af samtalen er værd at gemme som generel viden eller en specifik brugerpræference.

2. **Udtrække og opsummere**: Destillere det væsentlige læringspunkt eller præference fra samtalen.

3. **Lagre i en vidensdatabase**: Gemme denne udtrukne information, ofte i en vektordatabase, så den kan hentes senere.

4. **Berige fremtidige forespørgsler**: Når brugeren starter en ny forespørgsel, henter vidensagenten relevant lagret information og tilføjer den til brugerens prompt, hvilket giver afgørende kontekst til den primære agent (på lignende måde som RAG).

### Optimeringer for hukommelse

• **Latency-håndtering**: For at undgå at nedsætte brugerinteraktioner kan en billigere, hurtigere model bruges først til hurtigt at tjekke, om information er værd at gemme eller hente, og kun derefter aktivere den mere komplekse udtræknings-/hentningsproces, hvis nødvendigt.

• **Vedligeholdelse af vidensbase**: For en voksende vidensbase kan mindre brugte informationer flyttes til "kold lagring" for at styre omkostninger.

## Har du flere spørgsmål om agenthukommelse?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i office hours og få svar på dine AI Agent-spørgsmål.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->