<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T15:33:42+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "da"
}
-->
[![Intro til AI-agenter](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.da.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Introduktion til AI-agenter og deres anvendelsesmuligheder

Velkommen til kurset "AI-agenter for begyndere"! Dette kursus giver grundlæggende viden og praktiske eksempler på, hvordan man bygger AI-agenter.

Deltag i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre kursusdeltagere og AI-agentudviklere og stille spørgsmål om kurset.

For at starte kurset begynder vi med at få en bedre forståelse af, hvad AI-agenter er, og hvordan vi kan bruge dem i de applikationer og arbejdsgange, vi udvikler.

## Introduktion

Denne lektion dækker:

- Hvad er AI-agenter, og hvilke forskellige typer agenter findes der?
- Hvilke anvendelsesmuligheder er bedst for AI-agenter, og hvordan kan de hjælpe os?
- Hvad er nogle af de grundlæggende byggesten, når man designer agentbaserede løsninger?

## Læringsmål
Efter at have gennemført denne lektion, bør du kunne:

- Forstå AI-agentbegreber og hvordan de adskiller sig fra andre AI-løsninger.
- Anvende AI-agenter mest effektivt.
- Produktivt designe agentbaserede løsninger til både brugere og kunder.

## Definition af AI-agenter og typer af AI-agenter

### Hvad er AI-agenter?

AI-agenter er **systemer**, der gør det muligt for **Large Language Models (LLMs)** at **udføre handlinger** ved at udvide deres kapaciteter gennem adgang til **værktøjer** og **viden**.

Lad os opdele denne definition i mindre dele:

- **System** - Det er vigtigt at tænke på agenter som et system af mange komponenter, ikke blot en enkelt komponent. På det grundlæggende niveau består en AI-agent af:
  - **Miljø** - Det definerede område, hvor AI-agenten opererer. For eksempel, hvis vi havde en rejsebooking-agent, kunne miljøet være det bookingsystem, som agenten bruger til at udføre opgaver.
  - **Sensorer** - Miljøer indeholder information og giver feedback. AI-agenter bruger sensorer til at indsamle og fortolke denne information om miljøets aktuelle tilstand. I eksemplet med rejsebooking-agenten kan bookingsystemet give information som hoteltilgængelighed eller flypriser.
  - **Aktuatorer** - Når AI-agenten modtager miljøets aktuelle tilstand, bestemmer den, hvilken handling der skal udføres for at ændre miljøet. For rejsebooking-agenten kan det være at booke et ledigt værelse til brugeren.

![Hvad er AI-agenter?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.da.png)

**Large Language Models** - Konceptet med agenter eksisterede før oprettelsen af LLM'er. Fordelen ved at bygge AI-agenter med LLM'er er deres evne til at fortolke menneskesprog og data. Denne evne gør det muligt for LLM'er at fortolke miljøinformation og definere en plan for at ændre miljøet.

**Udføre handlinger** - Uden for AI-agent-systemer er LLM'ers handlinger begrænset til at generere indhold eller information baseret på en brugers prompt. Inden for AI-agent-systemer kan LLM'er udføre opgaver ved at fortolke brugerens anmodning og bruge værktøjer, der er tilgængelige i deres miljø.

**Adgang til værktøjer** - Hvilke værktøjer LLM'en har adgang til, defineres af 1) det miljø, den opererer i, og 2) udvikleren af AI-agenten. For vores rejseagenteksempel er agentens værktøjer begrænset af de operationer, der er tilgængelige i bookingsystemet, og/eller udvikleren kan begrænse agentens værktøjsadgang til fly.

**Hukommelse+Viden** - Hukommelse kan være kortsigtet i konteksten af samtalen mellem brugeren og agenten. Langsigtet, uden for den information, der leveres af miljøet, kan AI-agenter også hente viden fra andre systemer, tjenester, værktøjer og endda andre agenter. I rejseagenteksemplet kunne denne viden være information om brugerens rejsepræferencer, der er gemt i en kundedatabase.

### De forskellige typer agenter

Nu hvor vi har en generel definition af AI-agenter, lad os se på nogle specifikke agenttyper og hvordan de kunne anvendes i en rejsebooking-agent.

| **Agenttype**                 | **Beskrivelse**                                                                                                                       | **Eksempel**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Udfører øjeblikkelige handlinger baseret på foruddefinerede regler.                                                                    | Rejseagenten fortolker konteksten af en e-mail og videresender rejseklager til kundeservice.                                                                                                                                   |
| **Model-Based Reflex Agents** | Udfører handlinger baseret på en model af verden og ændringer i denne model.                                                          | Rejseagenten prioriterer ruter med betydelige prisændringer baseret på adgang til historiske prisdata.                                                                                                                        |
| **Goal-Based Agents**         | Skaber planer for at opnå specifikke mål ved at fortolke målet og bestemme handlinger for at nå det.                                   | Rejseagenten booker en rejse ved at bestemme nødvendige rejsearrangementer (bil, offentlig transport, fly) fra den nuværende placering til destinationen.                                                                       |
| **Utility-Based Agents**      | Overvejer præferencer og afvejer kompromiser numerisk for at bestemme, hvordan mål opnås.                                             | Rejseagenten maksimerer nytte ved at afveje bekvemmelighed mod omkostninger, når rejser bookes.                                                                                                                                |
| **Learning Agents**           | Forbedrer sig over tid ved at reagere på feedback og justere handlinger derefter.                                                     | Rejseagenten forbedrer sig ved at bruge kundefeedback fra efter-rejse-undersøgelser til at foretage justeringer i fremtidige bookinger.                                                                                         |
| **Hierarchical Agents**       | Indeholder flere agenter i et hierarkisk system, hvor højere niveau-agenter opdeler opgaver i delopgaver, som lavere niveau-agenter udfører. | Rejseagenten annullerer en rejse ved at opdele opgaven i delopgaver (f.eks. annullering af specifikke bookinger) og lade lavere niveau-agenter udføre dem, mens de rapporterer tilbage til højere niveau-agenten.                  |
| **Multi-Agent Systems (MAS)** | Agenter udfører opgaver uafhængigt, enten samarbejdende eller konkurrerende.                                                          | Samarbejdende: Flere agenter booker specifikke rejsetjenester som hoteller, fly og underholdning. Konkurrerende: Flere agenter administrerer og konkurrerer om en delt hotelbookingkalender for at booke kunder ind på hotellet. |

## Hvornår skal man bruge AI-agenter?

I det tidligere afsnit brugte vi rejseagentens anvendelsestilfælde til at forklare, hvordan de forskellige typer agenter kan bruges i forskellige scenarier for rejsebooking. Vi vil fortsætte med at bruge denne applikation gennem hele kurset.

Lad os se på de typer anvendelsestilfælde, hvor AI-agenter er bedst egnet:

![Hvornår skal man bruge AI-agenter?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.da.png)

- **Åbne problemstillinger** - hvor LLM'en selv kan bestemme de nødvendige trin for at fuldføre en opgave, fordi det ikke altid kan hardcodes i en arbejdsgang.
- **Flertrinsprocesser** - opgaver, der kræver en vis kompleksitet, hvor AI-agenten skal bruge værktøjer eller information over flere trin i stedet for enkeltstående forespørgsler.
- **Forbedring over tid** - opgaver, hvor agenten kan forbedre sig over tid ved at modtage feedback fra enten sit miljø eller brugere for at levere bedre nytte.

Vi dækker flere overvejelser om brugen af AI-agenter i lektionen om at bygge pålidelige AI-agenter.

## Grundlæggende om agentbaserede løsninger

### Agentudvikling

Det første skridt i designet af et AI-agent-system er at definere værktøjer, handlinger og adfærd. I dette kursus fokuserer vi på at bruge **Azure AI Agent Service** til at definere vores agenter. Det tilbyder funktioner som:

- Valg af åbne modeller som OpenAI, Mistral og Llama
- Brug af licenserede data gennem udbydere som Tripadvisor
- Brug af standardiserede OpenAPI 3.0-værktøjer

### Agentbaserede mønstre

Kommunikation med LLM'er sker gennem prompts. Givet den semi-autonome natur af AI-agenter er det ikke altid muligt eller nødvendigt manuelt at gentage prompts til LLM'en efter en ændring i miljøet. Vi bruger **agentbaserede mønstre**, der gør det muligt at prompt LLM'en over flere trin på en mere skalerbar måde.

Dette kursus er opdelt i nogle af de nuværende populære agentbaserede mønstre.

### Agentbaserede rammeværk

Agentbaserede rammeværk giver udviklere mulighed for at implementere agentbaserede mønstre gennem kode. Disse rammeværk tilbyder skabeloner, plugins og værktøjer til bedre samarbejde mellem AI-agenter. Disse fordele giver bedre muligheder for at observere og fejlfinde AI-agent-systemer.

I dette kursus vil vi udforske det forskningsdrevne AutoGen-rammeværk og det produktionsklare Agent-rammeværk fra Semantic Kernel.

### Har du flere spørgsmål om AI-agenter?

Deltag i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre kursusdeltagere, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Forrige lektion

[Kursusopsætning](../00-course-setup/README.md)

## Næste lektion

[Udforskning af agentbaserede rammeværk](../02-explore-agentic-frameworks/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.