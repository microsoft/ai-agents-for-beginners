[![Intro til AI-agenter](../../../translated_images/da/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Introduktion til AI-agenter og agentbrugssager

Velkommen til kurset **AI-agenter for begyndere**! Dette kursus giver dig den grundlæggende viden — og fungerende kode — til at begynde at bygge AI-agenter fra bunden.

Kom og sig hej i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord-fællesskabet</a> — det er fyldt med lærende og AI-byggere, der gerne svarer på spørgsmål.

Inden vi kaster os ud i at bygge, lad os sikre, at vi faktisk forstår, hvad en AI-agent *er*, og hvornår det giver mening at bruge en.

---

## Introduktion

Denne lektion dækker:

- Hvad AI-agenter er, og de forskellige typer der findes
- Hvilke slags opgaver AI-agenter egner sig bedst til
- De grundlæggende byggesten, du bruger, når du designer en agentbaseret løsning

## Læringsmål

Når du er færdig med denne lektion, bør du kunne:

- Forklare, hvad en AI-agent er, og hvordan den er forskellig fra en almindelig AI-løsning
- Vide, hvornår det giver mening at bruge en AI-agent (og hvornår ikke)
- Skitsere et grundlæggende agentbaseret løsningsdesign for et virkelighedsproblem

---

## Definition af AI-agenter og typer af AI-agenter

### Hvad er AI-agenter?

Her er en simpel måde at tænke på det:

> **AI-agenter er systemer, der lader store sprogmodeller (LLMs) *faktisk gøre ting* — ved at give dem værktøjer og viden til at handle på verden, ikke bare svare på forespørgsler.**

Lad os uddybe det lidt:

- **System** — En AI-agent er ikke bare én ting. Det er en samling dele, der arbejder sammen. I sin kerne har hver agent tre dele:
  - **Miljø** — Det rum agenten arbejder i. For en rejsebooking-agent ville det være bookingsystemet selv.
  - **Sensorer** — Hvordan agenten læser den aktuelle tilstand i sit miljø. Vores rejseagent kunne tjekke hoteltilgængelighed eller flypriser.
  - **Aktuatorer** — Hvordan agenten handler. Rejseagenten kunne booke et værelse, sende en bekræftelse eller annullere en reservation.

![Hvad er AI-agenter?](../../../translated_images/da/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Store sprogmodeller** — Agenter fandtes før LLM’er, men LLM’er er det, der gør moderne agenter så kraftfulde. De kan forstå naturligt sprog, ræsonnere om kontekst og omsætte en uklar brugerforespørgsel til en konkret handlingsplan.

- **Udfør handlinger** — Uden et agentsystem genererer en LLM bare tekst. Inde i et agentsystem kan LLM faktisk *udføre* trin — søge i en database, kalde en API, sende en besked.

- **Adgang til værktøjer** — Hvilke værktøjer agenten kan bruge, afhænger af (1) det miljø, den kører i, og (2) hvad udvikleren har valgt at give den. En rejseagent kan måske søge efter fly, men ikke redigere kundeoplysninger — det handler om, hvad du forbinder.

- **Hukommelse + viden** — Agenter kan have korttidshukommelse (den aktuelle samtale) og langtidshukommelse (en kundedatabase, tidligere interaktioner). Rejseagenten kan "huske", at du foretrækker sæder ved vinduet.

---

### De forskellige typer AI-agenter

Ikke alle agenter er bygget ens. Her er en oversigt over de vigtigste typer med en rejsebooking-agent som eksempel:

| **Agenttype** | **Hvad den gør** | **Rejseagenteksempel** |
|---|---|---|
| **Simple refleksagenter** | Følger hårdkodede regler — ingen hukommelse, ingen planlægning. | Ser en klage-mail → videresender den til kundeservice. Det er det. |
| **Model-baserede refleksagenter** | Holder en intern model af verden og opdaterer den løbende. | Sporer historiske flypriser og markerer ruter, der pludselig bliver dyre. |
| **Målorienterede agenter** | Har et mål og finder ud af, hvordan det nås trin for trin. | Booker en hel rejse (fly, bil, hotel) fra din nuværende lokation for at få dig til destinationen. |
| **Nyttebaserede agenter** | Finder ikke bare *en* løsning — finder den *bedste* ved at veje fordele og ulemper. | Afvejer omkostninger mod bekvemmelighed for at finde den rejse, der scorer højest på dine præferencer. |
| **Lærende agenter** | Bliver bedre over tid ved at lære af feedback. | Justerer fremtidige bookinganbefalinger baseret på spørgeskemasvar efter rejsen. |
| **Hierarkiske agenter** | En overordnet agent opdeler arbejdet i delopgaver og delegerer til lavere-niveau agenter. | En "annuller tur"-anmodning opdeles i: annuller fly, annuller hotel, annuller billeje — hver håndteres af en under-agent. |
| **Multi-agent systemer (MAS)** | Flere uafhængige agenter arbejder sammen (eller konkurrerer). | Samarbejdende: separate agenter håndterer hoteller, fly og underholdning. Konkurrerende: flere agenter konkurrerer om at finde hotelværelser til den bedste pris. |

---

## Hvornår skal man bruge AI-agenter

Bare fordi du *kan* bruge en AI-agent, betyder det ikke, at du altid *skal*. Her er situationerne, hvor agenter virkelig kommer til deres ret:

![Hvornår skal man bruge AI-agenter?](../../../translated_images/da/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Åbne problemstillinger** — Når trinnene til at løse et problem ikke kan programmeres på forhånd. Du har brug for, at LLM’en selv finder vej dynamisk.
- **Flertrinsprocesser** — Opgaver der kræver brug af værktøjer over flere trin, ikke bare et enkelt opslag eller generering.
- **Forbedring over tid** — Når du ønsker systemet skal blive klogere baseret på brugerfeedback eller miljøsignaler.

Vi vil dykke dybere ned i, hvornår (og hvornår *ikke*) man skal bruge AI-agenter i lektionen **At bygge pålidelige AI-agenter** senere i kurset.

---

## Grundlæggende for agentbaserede løsninger

### Agentudvikling

Det første, du gør, når du bygger en agent, er at definere *hvad den kan gøre* — dens værktøjer, handlinger og adfærd.

I dette kursus bruger vi **Azure AI Agent Service** som vores primære platform. Den understøtter:

- Åbne modeller som OpenAI, Mistral og Llama
- Licenserede data fra udbydere som Tripadvisor
- Standardiserede OpenAPI 3.0-værktøjsdefinitioner

### Agentmønstre

Du kommunikerer med LLM’er gennem prompts. Med agenter kan du ikke altid håndbygge hver prompt manuelt — agenten skal kunne handle på tværs af mange trin. Her kommer **agentmønstre** ind i billedet. Det er genanvendelige strategier til at promptstyre og orkestrere LLM’er på en mere skalerbar, pålidelig måde.

Dette kursus er struktureret om de mest almindelige og nyttige agentmønstre.

### Agentframeworks

Agentframeworks giver udviklere færdige skabeloner, værktøjer og infrastruktur til at bygge agenter. De gør det lettere at:

- Forbinde værktøjer og funktioner
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

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at komme i kontakt med andre lærende, deltage i office hours, og få svar på dine AI-agent-spørgsmål fra fællesskabet.

---

## Forrige lektion

[Opsætning af kursus](../00-course-setup/README.md)

## Næste lektion

[Udforskning af agentframeworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, skal du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->