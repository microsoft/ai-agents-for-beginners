[![Intro til AI-agenter](../../../translated_images/da/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Introduktion til AI-agenter og anvendelsestilfælde for agenter

Velkommen til **AI-agenter for begyndere**-kurset! Dette kursus giver dig den grundlæggende viden — og ægte fungerende kode — til at begynde at bygge AI-agenter fra bunden.

Kom og sig hej i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord fællesskabet</a> — det er fyldt med lærende og AI-byggere, som gerne vil besvare spørgsmål.

Før vi går i gang med at bygge, lad os sikre os, at vi rent faktisk forstår, hvad en AI-agent *er* og hvornår det giver mening at bruge en.

---

## Introduktion

Denne lektion dækker:

- Hvad AI-agenter er, og de forskellige typer, der findes
- Hvilke slags opgaver AI-agenter er bedst egnet til
- De kernebyggesten, du vil bruge, når du designer en agent-baseret løsning

## Læringsmål

Når du er færdig med denne lektion, bør du kunne:

- Forklare hvad en AI-agent er, og hvordan den adskiller sig fra en almindelig AI-løsning
- Vide, hvornår du skal vælge en AI-agent (og hvornår ikke)
- Skitsere et grundlæggende agent-baseret løsningsdesign til et virkeligt problem

---

## Definition af AI-agenter og typer af AI-agenter

### Hvad er AI-agenter?

Her er en simpel måde at tænke på det:

> **AI-agenter er systemer, der lader store sprogmodeller (LLM'er) faktisk *gøre ting* — ved at give dem værktøjer og viden til at handle i verden, ikke bare svare på prompts.**

Lad os udfolde det lidt:

- **System** — En AI-agent er ikke bare én ting. Det er en samling af dele, der arbejder sammen. I sin kerne har hver agent tre dele:
  - **Miljø** — Det rum agenten arbejder i. For en rejsebestillingsagent vil det være bookingplatformen selv.
  - **Sensorer** — Hvordan agenten læser den aktuelle tilstand i sit miljø. Vores rejseagent kan tjekke hoteltilgængelighed eller flypriser.
  - **Aktuatorer** — Hvordan agenten tager handling. Rejseagenten kan booke et værelse, sende en bekræftelse eller annullere en reservation.

![Hvad er AI-agenter?](../../../translated_images/da/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Store sprogmodeller** — Agenter eksisterede før LLM'er, men LLM'er gør moderne agenter så kraftfulde. De kan forstå naturligt sprog, ræsonnere om kontekst og omsætte en vag brugerforespørgsel til en konkret handlingsplan.

- **Udføre handlinger** — Uden et agent-system genererer en LLM bare tekst. Inden for et agent-system kan LLM’en faktisk *udføre* trin — søge i en database, kalde en API, sende en besked.

- **Adgang til værktøjer** — Hvilke værktøjer agenten kan bruge afhænger af (1) det miljø, den kører i, og (2) hvad udvikleren har valgt at give den. En rejseagent kan søge efter fly, men ikke redigere kundedata — det handler om, hvad du kobler til.

- **Hukommelse + viden** — Agenter kan have korttidshukommelse (den aktuelle samtale) og langtidshukommelse (en kundedatabase, tidligere interaktioner). Rejseagenten kan "huske", at du foretrækker vinduessæder.

---

### De forskellige typer AI-agenter

Ikke alle agenter bygges ens. Her er en oversigt over hovedtyperne, med en rejsebestillingsagent som gennemgående eksempel:

| **Agenttype** | **Hvad den gør** | **Eksempel på rejseagent** |
|---|---|---|
| **Simple reflex-agenter** | Følger hårdkodede regler — ingen hukommelse, ingen planlægning. | Ser en klage-email → videresender den til kundeservice. Det er det. |
| **Model-baserede reflex-agenter** | Holder en intern model af verden og opdaterer den, når ting ændrer sig. | Sporer historiske flypriser og markerer ruter, der pludselig er dyre. |
| **Mål-baserede agenter** | Har et mål i tankerne og finder ud af, hvordan man når det trin for trin. | Booker en hel tur (fly, bil, hotel) fra din nuværende placering for at komme til dit rejsemål. |
| **Nyttemaksimerende agenter** | Finder ikke bare *en* løsning — finder den *bedste* ved at afveje fordele og ulemper. | Afvejer pris mod bekvemmelighed for at finde turen, der scorer højest for dine præferencer. |
| **Lærende agenter** | Bliver bedre over tid ved at lære af feedback. | Justerer fremtidige bookingforslag baseret på spørgeskemasvar efter turen. |
| **Hierarkiske agenter** | En højniveau-agent opdeler arbejdet i delopgaver og delegerer til underordnede agenter. | En "annuller tur"-forespørgsel deles op i: annuller fly, annuller hotel, annuller biludlejning — hver håndteres af en under-agent. |
| **Multi-agent systemer (MAS)** | Flere uafhængige agenter arbejder sammen (eller konkurrerer). | Samarbejdende: separate agenter håndterer hoteller, fly og underholdning. Konkurrerende: flere agenter konkurrerer om at fylde hotelværelser til bedste pris. |

---

## Hvornår man skal bruge AI-agenter

Bare fordi du *kan* bruge en AI-agent, betyder det ikke, at du altid *skal*. Her er situationerne, hvor agenter virkelig skinner:

![Hvornår skal man bruge AI-agenter?](../../../translated_images/da/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Åbne problemer** — Når trinnene til at løse et problem ikke kan forprogrammeres. Du har brug for, at LLM’en finder vejen dynamisk.
- **Flere trin-processer** — Opgaver der kræver brug af værktøjer over flere omgange, ikke bare et enkelt opslag eller tekstgenerering.
- **Forbedring over tid** — Når du ønsker, at systemet bliver klogere baseret på brugerfeedback eller signaler fra omgivelserne.

Vi dykker dybere ned i, hvornår (og hvornår *ikke*) man skal bruge AI-agenter i lektionen **Byg troværdige AI-agenter** senere i kurset.

---

## Grundlæggende om agent-baserede løsninger

### Agentudvikling

Det første, du gør, når du bygger en agent, er at definere *hvad den kan gøre* — dens værktøjer, handlinger og adfærd.

I dette kursus bruger vi **Azure AI Agent Service** som vores hovedplatform. Den understøtter:

- Modeller fra udbydere som OpenAI, Mistral og Meta (Llama)
- Licenserede data fra udbydere som Tripadvisor
- Standardiserede OpenAPI 3.0 værktøjsdefinitioner

### Agentiske mønstre

Du kommunikerer med LLM'er via prompts. Med agenter kan du ikke altid håndbygge hver prompt manuelt — agenten skal tage handling over mange trin. Det er her, **Agentiske mønstre** kommer ind. Det er genanvendelige strategier til at prompt og orkestrere LLM'er på en mere skalerbar, pålidelig måde.

Dette kursus er struktureret omkring de mest almindelige og nyttige agentiske mønstre.

### Agentiske frameworks

Agentiske frameworks giver udviklere færdige skabeloner, værktøjer og infrastruktur til at bygge agenter. De gør det lettere at:

- Kobler værktøjer og kapaciteter sammen
- Observere, hvad agenten gør (og fejlfinde, når noget går galt)
- Samarbejde på tværs af flere agenter

I dette kursus fokuserer vi på **Microsoft Agent Framework (MAF)** til at bygge produktionsklare agenter.

---

## Kodeeksempler

Klar til at se det i praksis? Her er kodeeksemplerne til denne lektion:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Har du spørgsmål?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at tale med andre lærende, deltage i office hours og få svar på dine AI-agent-spørgsmål fra fællesskabet.

---

## Forrige lektion

[Opsætning af kursus](../00-course-setup/README.md)

## Næste lektion

[Udforsk agentiske frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->