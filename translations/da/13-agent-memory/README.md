# Hukommelse for AI-agenter 
[![Agenthukommelse](../../../translated_images/da/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

When discussing the unique benefits of creating AI Agents, two things are mainly discussed: the ability to call tools to complete tasks and the ability to improve over time. Memory is at the foundation of creating self-improving agent that can create better experiences for our users.

In this lesson, we will look at what memory is for AI Agents and how we can manage it and use it for the benefit of our applications.

## Introduktion

This lesson will cover:

• **Forståelse af AI-agenters hukommelse**: Hvad hukommelse er, og hvorfor det er væsentligt for agenter.

• **Implementering og lagring af hukommelse**: Praktiske metoder til at tilføje hukommelsesfunktioner til dine AI-agenter, med fokus på kort- og langtidshukommelse.

• **Gøre AI-agenter selvforbedrende**: Hvordan hukommelse gør det muligt for agenter at lære af tidligere interaktioner og forbedre sig over tid.

## Tilgængelige implementeringer

This lesson includes two comprehensive notebook tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerer hukommelse ved hjælp af Mem0 og Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerer struktureret hukommelse ved hjælp af Cognee, bygger automatisk en viden-graf understøttet af embeddings, visualiserer grafen og intelligent hentning

## Læringsmål

After completing this lesson, you will know how to:

• **Differentiate between various types of AI agent memory**, including working, short-term, and long-term memory, as well as specialized forms like persona and episodic memory.
- Differentiere mellem forskellige typer af AI-agenthukommelse, herunder arbejdshukommelse, korttids- og langtidshukommelse, samt specialiserede former som persona- og episodisk hukommelse.

• **Implement and manage short-term and long-term memory for AI agents** using Microsoft Agent Framework, leveraging tools like Mem0, Cognee, Whiteboard memory, and integrating with Azure AI Search.
- Implementere og administrere kort- og langtidshukommelse for AI-agenter ved hjælp af Microsoft Agent Framework, med værktøjer som Mem0, Cognee, Whiteboard memory og integration med Azure AI Search.

• **Understand the principles behind self-improving AI agents** and how robust memory management systems contribute to continuous learning and adaptation.
- Forstå principperne bag selvforbedrende AI-agenter og hvordan robuste hukommelsesstyringssystemer bidrager til kontinuerlig læring og tilpasning.

## Forståelse af AI-agenters hukommelse

At sin kerne refererer **hukommelse for AI-agenter til de mekanismer, der giver dem mulighed for at bevare og genkalde information**. Denne information kan være specifikke detaljer om en samtale, brugerpræferencer, tidligere handlinger eller endda lærte mønstre.

Uden hukommelse er AI-applikationer ofte tilstandsløse, hvilket betyder, at hver interaktion starter fra bunden. Dette fører til en gentagende og frustrerende brugeroplevelse, hvor agenten "glemmer" tidligere kontekst eller præferencer.

### Hvorfor er hukommelse vigtig?

En agents intelligens er dybt knyttet til dens evne til at genkalde og udnytte tidligere information. Hukommelse gør det muligt for agenter at være:

• **Reflekterende**: Lære af tidligere handlinger og resultater.

• **Interaktive**: Opretholde kontekst i en igangværende samtale.

• **Proaktive og reaktive**: Forudse behov eller reagere passende baseret på historiske data.

• **Autonome**: Operere mere uafhængigt ved at trække på lagret viden.

Målet med at implementere hukommelse er at gøre agenter mere **pålidelige og kompetente**.

### Typer af hukommelse

#### Arbejdshukommelse

Tænk på dette som en skitseblok, en agent bruger under en enkelt, igangværende opgave eller tankeproces. Den holder den umiddelbare information, der er nødvendig for at beregne næste skridt.

For AI-agenter fanger arbejdshukommelsen ofte de mest relevante oplysninger fra en samtale, selvom den fulde chat-historik er lang eller trunkeret. Den fokuserer på at udtrække nøgleelementer som krav, forslag, beslutninger og handlinger.

**Eksempel på arbejdshukommelse**

I en rejsebookingsagent kunne arbejdshukommelsen fange brugerens aktuelle anmodning, såsom "Jeg vil booke en rejse til Paris". Dette specifikke krav holdes i agentens umiddelbare kontekst for at guide den aktuelle interaktion.

#### Korttids-hukommelse

Denne type hukommelse bevarer information i løbet af én samtale eller session. Det er konteksten i den aktuelle chat, som gør det muligt for agenten at referere tilbage til tidligere runder i dialogen.

**Eksempel på korttids-hukommelse**

Hvis en bruger spørger, "Hvor meget vil en flyrejse til Paris koste?" og derefter følger op med "Hvad med indkvartering der?", sikrer korttids-hukommelsen, at agenten ved, at "der" refererer til "Paris" inden for samme samtale.

#### Langtidshukommelse

Dette er information, der bevares på tværs af flere samtaler eller sessioner. Det tillader agenter at huske brugerpræferencer, historiske interaktioner eller generel viden over længere perioder. Dette er vigtigt for personalisering.

**Eksempel på langtidshukommelse**

En langtidshukommelse kunne gemme, at "Ben nyder skiløb og udendørsaktiviteter, kan lide kaffe med bjergudsigt, og ønsker at undgå avancerede ski-løjper på grund af en tidligere skade". Disse oplysninger, lært fra tidligere interaktioner, påvirker anbefalinger i fremtidige rejseplanlægningssessioner og gør dem meget mere personlige.

#### Persona-hukommelse

Denne specialiserede hukommelsestype hjælper en agent med at udvikle en konsekvent "personlighed" eller "persona". Den gør det muligt for agenten at huske detaljer om sig selv eller sin tiltenkte rolle, hvilket gør interaktionerne mere flydende og fokuserede.

**Eksempel på persona-hukommelse**
Hvis rejseagenten er designet til at være en "ekspert i skiplanlægning", kan persona-hukommelsen forstærke denne rolle og påvirke dens svar til at være i tråd med en eksperts tone og viden.

#### Workflow/episodisk hukommelse

Denne hukommelse gemmer rækkefølgen af trin, en agent tager under en kompleks opgave, inklusive succeser og fejl. Det er som at huske specifikke "episoder" eller tidligere erfaringer for at lære af dem.

**Eksempel på episodisk hukommelse**

Hvis agenten forsøgte at booke en bestemt flyvning, men det mislykkedes på grund af manglende tilgængelighed, kunne episodisk hukommelse registrere denne fejl, så agenten kan prøve alternative flyvninger eller informere brugeren om problemet på en mere oplyst måde ved et efterfølgende forsøg.

#### Entitets-hukommelse

Dette involverer udtrækning og hukommelse af specifikke entiteter (som personer, steder eller ting) og begivenheder fra samtaler. Det gør det muligt for agenten at opbygge en struktureret forståelse af nøgleelementer, der drøftes.

**Eksempel på entitets-hukommelse**

Fra en samtale om en tidligere tur kunne agenten udtrække "Paris," "Eiffeltårnet," og "middag på Le Chat Noir-restaurant" som entiteter. Ved en fremtidig interaktion kunne agenten genkalde "Le Chat Noir" og tilbyde at lave en ny reservation der.

#### Struktureret RAG (Retrieval Augmented Generation)

Mens RAG er en bredere teknik, fremhæves "Struktureret RAG" som en kraftfuld hukommelsesteknologi. Den udtrækker tæt, struktureret information fra forskellige kilder (samtaler, e-mails, billeder) og bruger det til at forbedre præcision, recall og hastighed i svar. I modsætning til klassisk RAG, der udelukkende er baseret på semantisk lighed, arbejder Struktureret RAG med informationens iboende struktur.

**Eksempel på struktureret RAG**

I stedet for kun at matche nøgleord, kunne Struktureret RAG parse flyoplysninger (destination, dato, tid, flyselskab) fra en e-mail og gemme dem på en struktureret måde. Dette muliggør præcise forespørgsler som "Hvilket fly bookede jeg til Paris på tirsdag?"

## Implementering og lagring af hukommelse

Implementering af hukommelse for AI-agenter involverer en systematisk proces af **hukommelsesstyring**, som omfatter generering, lagring, hentning, integration, opdatering og endda "glemning" (eller sletning) af information. Hentning er et særligt vigtigt aspekt.

### Specialiserede hukommelsesværktøjer

#### Mem0

En måde at gemme og administrere agent-hukommelse på er ved at bruge specialiserede værktøjer som Mem0. Mem0 fungerer som et vedvarende hukommelseslag, der gør det muligt for agenter at genkalde relevante interaktioner, gemme brugerpræferencer og faktuel kontekst samt lære af succeser og fejl over tid. Idéen her er, at tilstandsløse agenter bliver til tilstandsfulde agenter.

Det fungerer gennem en **to-trins hukommelsespipeline: ekstraktion og opdatering**. Først sendes beskeder, der er tilføjet til en agents tråd, til Mem0-tjenesten, som bruger en Large Language Model (LLM) til at opsummere samtalehistorik og udtrække nye minder. Efterfølgende bestemmer en LLM-drevet opdateringsfase, om disse minder skal tilføjes, ændres eller slettes, og gemmer dem i en hybrid datalager, der kan inkludere vektor-, graf- og nøgle-værdi-databaser. Dette system understøtter også forskellige hukommelsestyper og kan inkorporere grafhukommelse til at administrere relationer mellem entiteter.

#### Cognee

En anden kraftfuld tilgang er at bruge **Cognee**, en open-source semantisk hukommelse for AI-agenter, der omdanner strukturerede og ustrukturerede data til spørgbare vidensgrafer understøttet af embeddings. Cognee tilbyder en **dual-store architecture** der kombinerer vektorbaseret similarity-søgning med grafrelationer, hvilket gør det muligt for agenter ikke kun at forstå, hvilke informationer der er lignende, men også hvordan begreber relaterer til hinanden.

Det excellerer i **hybrid hentning**, der blander vektorsimilaritet, grafstruktur og LLM-resonnering - fra rå chunk-opslag til graf-bevidst spørgesvar. Systemet opretholder **levende hukommelse**, der udvikler sig og vokser, samtidig med at den forbliver spørgelig som én sammenkoblet graf, hvilket understøtter både kortsigtet sessionskontekst og langvarig vedvarende hukommelse.

The Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrates building this unified memory layer, with practical examples of ingesting diverse data sources, visualizing the knowledge graph, and querying with different search strategies tailored to specific agent needs.

### Lagre hukommelse med RAG

Beyond specialized memory tools like mem0 , you can leverage robust search services like **Azure AI Search as a backend for storing and retrieving memories**, especially for structured RAG.

This allows you to ground your agent's responses with your own data, ensuring more relevant and accurate answers. Azure AI Search can be used to store user-specific travel memories, product catalogs, or any other domain-specific knowledge.

Azure AI Search supports capabilities like **Structured RAG**, which excels at extracting and retrieving dense, structured information from large datasets like conversation histories, emails, or even images. This provides "superhuman precision and recall" compared to traditional text chunking and embedding approaches.

## Gøre AI-agenter selvforbedrende

A common pattern for self-improving agents involves introducing a **"knowledge agent"**. This separate agent observes the main conversation between the user and the primary agent. Its role is to:

1. **Identify valuable information**: Determine if any part of the conversation is worth saving as general knowledge or a specific user preference.

2. **Extract and summarize**: Distill the essential learning or preference from the conversation.

3. **Store in a knowledge base**: Persist this extracted information, often in a vector database, so it can be retrieved later.

4. **Augment future queries**: When the user initiates a new query, the knowledge agent retrieves relevant stored information and appends it to the user's prompt, providing crucial context to the primary agent (similar to RAG).

### Optimeringer for hukommelse

• **Latency Management**: To avoid slowing down user interactions, a cheaper, faster model can be used initially to quickly check if information is valuable to store or retrieve, only invoking the more complex extraction/retrieval process when necessary.

• **Knowledge Base Maintenance**: For a growing knowledge base, less frequently used information can be moved to "cold storage" to manage costs.

## Har du flere spørgsmål om agenthukommelse?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på originalsproget bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales en professionel, menneskelig oversættelse. Vi er ikke ansvarlige for misforståelser eller fejltolkninger som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->