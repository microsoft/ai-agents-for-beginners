[![Intro to AI Agents](../../../translated_images/da/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Introduktion til AI Agenter og Agentbrugssager

Velkommen til **AI Agents for Beginners** kurset! Dette kursus giver dig den grundlæggende viden — og ægte fungerende kode — til at begynde at bygge AI Agenter fra bunden.

Kom og sig hej i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — det er fyldt med elever og AI-byggere, der er glade for at svare på spørgsmål.

Før vi går i gang med at bygge, lad os sikre, at vi faktisk forstår, hvad en AI Agent *er*, og hvornår det giver mening at bruge en.

---

## Introduktion

Denne lektion dækker:

- Hvad AI Agenter er, og de forskellige typer der findes
- Hvilke slags opgaver AI Agenter er bedst egnet til
- De centrale byggeklodser, du vil bruge, når du designer en agent-løsning

## Læringsmål

Ved slutningen af denne lektion skal du kunne:

- Forklare, hvad en AI Agent er, og hvordan den adskiller sig fra en almindelig AI-løsning
- Vide, hvornår du skal vælge en AI Agent (og hvornår ikke)
- Skitsere et grundlæggende agent-design for et virkeligt problem

---

## Definition af AI Agenter og Typer af AI Agenter

### Hvad er AI Agenter?

Her er en simpel måde at tænke på det:

> **AI Agenter er systemer, der lader Store Sprogmodeller (LLMs) faktisk *gøre ting* — ved at give dem værktøjer og viden til at handle på verden, ikke bare svare på anmodninger.**

Lad os pakke det lidt ud:

- **System** — En AI Agent er ikke bare én ting. Det er en samling af dele, der arbejder sammen. I sin kerne har hver agent tre dele:
  - **Miljø** — Det rum agenten arbejder i. For en rejsebookingsagent ville dette være selve bookingplatformen.
  - **Sensorer** — Hvordan agenten læser den aktuelle tilstand i sit miljø. Vores rejseagent kunne tjekke hoteltilgængelighed eller flypriser.
  - **Aktuatorer** — Hvordan agenten handler. Rejseagenten kunne booke et værelse, sende en bekræftelse eller annullere en reservation.

![What Are AI Agents?](../../../translated_images/da/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Store Sprogmodeller** — Agenter eksisterede før LLMs, men LLMs er det, der gør moderne agenter så kraftfulde. De kan forstå naturligt sprog, ræsonnere om kontekst og omdanne en vag brugerforespørgsel til en konkret handlingsplan.

- **Udføre Handlinger** — Uden et agentsystem genererer en LLM bare tekst. Inden for et agentsystem kan LLM faktisk *udføre* trin — søge i en database, kalde et API, sende en besked.

- **Adgang til Værktøjer** — Hvilke værktøjer agenten kan bruge afhænger af (1) det miljø, den kører i, og (2) hvad udvikleren har valgt at give den. En rejseagent kan måske søge efter flyrejser, men ikke redigere kundedata — det handler om, hvad du forbinder.

- **Hukommelse + Viden** — Agenter kan have korttidshukommelse (den aktuelle samtale) og langtidshukommelse (en kundedatabase, tidligere interaktioner). Rejseagenten kan "huske", at du foretrækker vinduessæder.

---

### De Forskellige Typer af AI Agenter

Ikke alle agenter er bygget på samme måde. Her er en oversigt over hovedtyperne, med en rejsebookingsagent som eksempel:

| **Agenttype** | **Hvad Den Gør** | **Rejseagent Eksempel** |
|---|---|---|
| **Simple Refleksagenter** | Følger hårdkodede regler — ingen hukommelse, ingen planlægning. | Ser en klageemail → videresender den til kundeservice. Det er det. |
| **Modelbaserede Refleksagenter** | Har en intern model af verden og opdaterer den, når ting ændrer sig. | Følger historiske flypriser og markerer ruter, der pludselig er dyre. |
| **Målorienterede Agenter** | Har et mål for øje og finder ud af, hvordan det nås trin for trin. | Booker en hel rejse (fly, bil, hotel) med udgangspunkt i din nuværende lokation for at få dig til destinationen. |
| **Nyttebaserede Agenter** | Finder ikke bare *en* løsning — finder den *bedste* ved at veje fordele og ulemper. | Balancerer pris mod bekvemmelighed for at finde den rejse, der scorer højest for dine præferencer. |
| **Lærende Agenter** | Bliver bedre over tid ved at lære fra feedback. | Justerer fremtidige bookingforslag baseret på efter-rejse undersøgelsesresultater. |
| **Hierarkiske Agenter** | En agent på højere niveau opdeler arbejdet i delopgaver og delegerer til lavere niveau agenter. | En "annuller rejse" anmodning opdeles i: annuller fly, annuller hotel, annuller biludlejning — hver håndteres af en underagent. |
| **Multi-Agent Systemer (MAS)** | Flere uafhængige agenter arbejder sammen (eller konkurrerer). | Samarbejdende: separate agenter håndterer hoteller, fly og underholdning. Konkurrerende: flere agenter konkurrerer om at fylde hotelværelser til bedste pris. |

---

## Hvornår Man Skal Bruge AI Agenter

Bare fordi du *kan* bruge en AI Agent, betyder det ikke, at du altid *skal*. Her er situationerne, hvor agenter virkelig skinner:

![Hvornår man bruger AI Agenter?](../../../translated_images/da/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Åbne Problemer** — Når trinnene til at løse et problem ikke kan forprogrammeres. Du har brug for, at LLM dynamisk finder vejen.
- **Flere Trin Processer** — Opgaver, der kræver brug af værktøjer over flere omgange, ikke bare et enkelt opslag eller generering.
- **Forbedring Over Tid** — Når du vil have systemet til at blive klogere baseret på brugerfeedback eller miljømæssige signaler.

Vi vil gå mere i dybden om, hvornår (og hvornår *ikke*) man skal bruge AI Agenter i **Building Trustworthy AI Agents** lektionen senere i kurset.

---

## Grundlæggende Agentløsninger

### Agentudvikling

Det første du gør, når du bygger en agent, er at definere *hvad den kan gøre* — dens værktøjer, handlinger og adfærd.

I dette kursus bruger vi **Microsoft Foundry Agent Service** som vores hovedplatform. Den understøtter:

- Modeller fra udbydere som OpenAI, Mistral og Meta (Llama)
- Licenserede data fra udbydere som Tripadvisor
- Standardiserede OpenAPI 3.0 værktøjsdefinitioner

### Agentiske Mønstre

Du kommunikerer med LLMs gennem prompts. Med agenter kan du ikke altid håndskrive hver prompt manuelt — agenten skal udføre handlinger over mange trin. Det er her **Agentiske Mønstre** kommer ind. Det er genanvendelige strategier til at prompt og orkestrere LLMs på en mere skalerbar, pålidelig måde.

Dette kursus er struktureret omkring de mest almindelige og nyttige agentiske mønstre.

### Agentiske Frameworks

Agentiske Frameworks giver udviklere færdiglavede skabeloner, værktøjer og infrastruktur til at bygge agenter. De gør det nemmere at:

- Forbinde værktøjer og kapaciteter
- Observere hvad agenten gør (og fejlfinde når noget går galt)
- Samarbejde mellem flere agenter

I dette kursus fokuserer vi på **Microsoft Agent Framework (MAF)** til at bygge produktionsklare agenter.

---

## Kodeeksempler

Klar til at se det i aktion? Her er kodeeksemplerne til denne lektion:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Har du spørgsmål?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at forbinde med andre elever, deltage i kontortimer og få svar på dine AI Agent spørgsmål fra fællesskabet.


---

## Røgs-test af denne Agent (Valgfrit)

Når du lærer at deployere agenter i [Lesson 16](../16-deploying-scalable-agents/README.md), kan du tilføje en hurtig post-deploy sundhedskontrol for denne lektions `TravelAgent` med den færdiglavede katalog [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Se [`tests/README.md`](../tests/README.md) for hvordan du kører den.

---

## Forrige Lektion

[Course Setup](../00-course-setup/README.md)

## Næste Lektion

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->