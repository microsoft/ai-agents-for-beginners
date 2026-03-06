[![Introduktion til AI-agenter](../../../translated_images/da/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik på billedet ovenfor for at se video af denne lektion)_


# Introduktion til AI-agenter og agent-brugstilfælde

Velkommen til kurset "AI Agents for Beginners"! Dette kursus giver grundlæggende viden og anvendte eksempler til at bygge AI-agenter.

Deltag i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> for at møde andre kursister og AI-agentbyggere og stille de spørgsmål, du har om dette kursus.

For at starte dette kursus begynder vi med at få en bedre forståelse af, hvad AI-agenter er, og hvordan vi kan bruge dem i de applikationer og arbejdsgange, vi bygger.

## Introduktion

Denne lektion dækker:

- Hvad er AI-agenter, og hvilke forskellige typer agenter findes der?
- Hvilke brugstilfælde er bedst for AI-agenter, og hvordan kan de hjælpe os?
- Hvad er nogle af de grundlæggende byggesten ved design af agentiske løsninger?

## Læringsmål
Efter at have gennemført denne lektion bør du være i stand til at:

- Forstå koncepter omkring AI-agenter og hvordan de adskiller sig fra andre AI-løsninger.
- Anvende AI-agenter mest effektivt.
- Designe agentiske løsninger produktivt for både brugere og kunder.

## Definition af AI-agenter og typer af AI-agenter

### Hvad er AI-agenter?

AI-agenter er **systemer**, der gør det muligt for **Store sprogmodeller(LLMs)** at **udføre handlinger** ved at udvide deres kapaciteter ved at give LLMs **adgang til værktøjer** og **viden**.

Lad os bryde denne definition ned i mindre dele:

- **System** - Det er vigtigt at tænke på agenter ikke blot som en enkelt komponent, men som et system af mange komponenter. På det basale niveau er komponenterne i en AI-agent:
  - **Environment** - Det definerede rum hvor AI-agenten opererer. For eksempel, hvis vi havde en rejsebookings-AI-agent, kunne miljøet være rejsebookingsystemet, som AI-agenten bruger til at fuldføre opgaver.
  - **Sensors** - Miljøer har information og giver feedback. AI-agenter bruger sensorer til at indsamle og fortolke denne information om den aktuelle tilstand i miljøet. I eksemplet med rejsebookingsagenten kan rejsebookingsystemet give oplysninger såsom hoteltilgængelighed eller flypriser.
  - **Actuators** - Når AI-agenten modtager den aktuelle tilstand af miljøet, bestemmer agenten for den aktuelle opgave, hvilken handling der skal udføres for at ændre miljøet. For rejsebookingsagenten kan det være at booke et ledigt værelse for brugeren.

![Hvad er AI-agenter?](../../../translated_images/da/what-are-ai-agents.1ec8c4d548af601a.webp)

**Store sprogmodeller** - Konceptet med agenter eksisterede før skabelsen af LLMs. Fordelen ved at bygge AI-agenter med LLMs er deres evne til at fortolke menneskesprog og data. Denne evne gør det muligt for LLMs at fortolke miljøinformation og definere en plan for at ændre miljøet.

**Udøve handlinger** - Uden for AI-agent-systemer er LLMs begrænset til situationer, hvor handlingen er at generere indhold eller information baseret på en brugers prompt. Inde i AI-agent-systemer kan LLMs udføre opgaver ved at fortolke brugerens forespørgsel og bruge værktøjer, der er tilgængelige i deres miljø.

**Adgang til værktøjer** - Hvilke værktøjer LLM'en har adgang til defineres af 1) det miljø, den opererer i, og 2) udvikleren af AI-agenten. I vores rejseagenteksempel er agentens værktøjer begrænset af de operationer, der er tilgængelige i bookingsystemet, og/eller udvikleren kan begrænse agentens værktøjsadgang til fly.

**Hukommelse+Viden** - Hukommelse kan være kortvarig i konteksten af samtalen mellem brugeren og agenten. På længere sigt, ud over den information der leveres af miljøet, kan AI-agenter også hente viden fra andre systemer, tjenester, værktøjer og endda andre agenter. I rejseagenteksemplet kunne denne viden være information om brugerens rejsepræferencer placeret i en kundedatabase.

### De forskellige typer agenter

Nu hvor vi har en generel definition af AI-agenter, lad os se på nogle specifikke agenttyper, og hvordan de ville blive anvendt i en rejsebookings-AI-agent.

| **Agenttype**                | **Beskrivelse**                                                                                                                       | **Eksempel**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enkle refleksagenter**      | Udfører øjeblikkelige handlinger baseret på foruddefinerede regler.                                                                    | Rejseagent fortolker konteksten af en mail og videresender rejseklager til kundeservice.                                                                                                                                        |
| **Modelbaserede refleksagenter** | Udfører handlinger baseret på en model af verden og ændringer i den model.                                                            | Rejseagent prioriterer ruter med betydelige prisændringer baseret på adgang til historiske prisdata.                                                                                                                           |
| **Målorienterede agenter**         | Opretter planer for at opnå specifikke mål ved at fortolke målet og bestemme handlinger for at nå det.                                  | Rejseagent booker en rejse ved at bestemme nødvendige rejsearrangementer (bil, offentlig transport, fly) fra den aktuelle placering til destinationen.                                                                                |
| **Nyttebaserede agenter**      | Overvejer præferencer og vægter kompromiser numerisk for at bestemme, hvordan mål opnås.                                               | Rejseagent maksimerer nytte ved at afveje bekvemmelighed vs. pris ved booking af rejse.                                                                                                                                          |
| **Lærende agenter**           | Forbedrer sig over tid ved at reagere på feedback og justere handlinger derefter.                                                        | Rejseagent forbedres ved at bruge kundefeedback fra efterrejsen-undersøgelser til at foretage justeringer til fremtidige bookinger.                                                                                                               |
| **Hierarkiske agenter**       | Indeholder flere agenter i et lagdelt system, hvor højere niveau agenter nedbryder opgaver i underopgaver for lavere niveau agenter. | Rejseagent annullerer en rejse ved at opdele opgaven i underopgaver (for eksempel annullering af specifikke bookinger) og lade lavere niveau agenter fuldføre dem og rapportere tilbage til højere niveau agenten.                                     |
| **Multi-agent-systemer (MAS)** | Agenter fuldfører opgaver uafhængigt, enten samarbejdende eller konkurrerende.                                                           | Samarbejdende: Flere agenter booker specifikke rejsetjenester såsom hoteller, fly og underholdning. Konkurrerende: Flere agenter styrer og konkurrerer om en delt hotelbookingskalender for at booke kunder ind på hotellet. |

## Hvornår bruge AI-agenter

I den tidligere sektion brugte vi rejseagenteksemplet til at forklare, hvordan de forskellige agenttyper kan bruges i forskellige scenarier inden for rejsebooking. Vi vil fortsætte med at bruge denne applikation igennem kurset.

Lad os se på de typer af brugstilfælde, som AI-agenter er bedst egnede til:

![Hvornår skal man bruge AI-agenter?](../../../translated_images/da/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Åbne problemer** - tillader LLM'en at bestemme de nødvendige trin for at fuldføre en opgave, fordi det ikke altid kan hardkodes ind i en arbejdsgang.
- **Flertrinsprocesser** - opgaver, der kræver et niveau af kompleksitet, hvor AI-agenten skal bruge værktøjer eller information over flere omgange i stedet for enkelt-gangs hentning.  
- **Forbedring over tid** - opgaver hvor agenten kan forbedre sig over tid ved at modtage feedback fra enten sit miljø eller brugere for at levere bedre nytte.

Vi dækker flere overvejelser ved brug af AI-agenter i lektionen Building Trustworthy AI Agents.

## Grundlæggende om agentiske løsninger

### Udvikling af agenter

Det første skridt i designet af et AI-agent-system er at definere værktøjer, handlinger og adfærd. I dette kursus fokuserer vi på at bruge **Azure AI Agent Service** til at definere vores agenter. Den tilbyder funktioner som:

- Valg af åbne modeller såsom OpenAI, Mistral og Llama
- Brug af licenserede data gennem leverandører såsom Tripadvisor
- Brug af standardiserede OpenAPI 3.0-værktøjer

### Agentiske mønstre

Kommunikation med LLMs sker gennem prompts. Givet AI-agenters semi-autonome natur er det ikke altid muligt eller nødvendigt manuelt at gen-prømme LLM'en efter en ændring i miljøet. Vi bruger **agentiske mønstre**, der tillader os at prikke LLM'en over flere trin på en mere skalerbar måde.

Dette kursus er opdelt i nogle af de aktuelle populære agentiske mønstre.

### Agentiske rammeværk

Agentiske rammeværk giver udviklere mulighed for at implementere agentiske mønstre gennem kode. Disse rammeværk tilbyder skabeloner, plugins og værktøjer til bedre agent-samarbejde. Disse fordele giver muligheder for bedre observerbarhed og fejlsøgning af AI-agent-systemer.

I dette kursus vil vi udforske Microsoft Agent Framework (MAF) til at bygge produktionsklare AI-agenter.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Har du flere spørgsmål om AI-agenter?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre kursister, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Forrige lektion

[Kursusopsætning](../00-course-setup/README.md)

## Næste lektion

[Udforskning af agentiske rammeværk](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, som måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->