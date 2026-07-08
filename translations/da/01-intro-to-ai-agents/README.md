[![Intro til AI-agenter](../../../translated_images/da/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Introduktion til AI-agenter og agentbrugssager

Velkommen til **AI Agents for Beginners**-kurset! Dette kursus giver dig den grundlæggende viden – og rigtig fungerende kode – til at begynde at bygge AI-agenter fra bunden.

Kom og sig hej i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord-fællesskabet</a> — det er fyldt med studerende og AI-udviklere, som gerne vil svare på spørgsmål.

Før vi går i gang med at bygge, lad os sikre os, at vi faktisk forstår, hvad en AI-agent *er*, og hvornår det giver mening at bruge en.

---

## Introduktion

Denne lektion dækker:

- Hvad AI-agenter er, og de forskellige typer, der findes
- Hvilke slags opgaver AI-agenter er bedst egnet til
- De grundlæggende byggeklodser, du vil bruge, når du designer en agentbaseret løsning

## Læringsmål

Når du er færdig med denne lektion, skal du kunne:

- Forklare hvad en AI-agent er, og hvordan den adskiller sig fra en almindelig AI-løsning
- Vide, hvornår du skal vælge en AI-agent (og hvornår ikke)
- Skitsere et grundlæggende agentbaseret løsningsdesign til et virkeligt problem

---

## Definition af AI-agenter og typer af AI-agenter

### Hvad er AI-agenter?

Her er en enkel måde at tænke på det:

> **AI-agenter er systemer, der lader store sprogmodeller (LLM’er) faktisk *gøre ting* — ved at give dem værktøjer og viden til at handle på verden, ikke bare svare på prompts.**

Lad os pakke det lidt ud:

- **System** — En AI-agent er ikke bare én ting. Det er en samling af dele, der arbejder sammen. I sin kerne har hver agent tre dele:
  - **Miljø** — Det rum, agenten arbejder i. For en rejsebookingsagent ville det være bookingplatformen selv.
  - **Sensorer** — Hvordan agenten læser den nuværende tilstand i sit miljø. Vores rejseagent kunne tjekke hoteltilgængelighed eller flypriser.
  - **Aktuatorer** — Hvordan agenten handler. Rejseagenten kunne booke et værelse, sende en bekræftelse eller annullere en reservation.

![Hvad er AI-agenter?](../../../translated_images/da/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Store sprogmodeller** — Agenter fandtes før LLM’er, men LLM’er er det, der gør moderne agenter så stærke. De kan forstå naturligt sprog, ræsonnere omkring kontekst og omsætte en vag brugerforespørgsel til en konkret handlingsplan.

- **Udføre handlinger** — Uden et agentsystem genererer en LLM bare tekst. Inden for et agentsystem kan LLM’en faktisk *udføre* trin — søge i en database, kalde et API, sende en besked.

- **Adgang til værktøjer** — Hvilke værktøjer agenten kan bruge afhænger af (1) det miljø, den kører i, og (2) hvad udvikleren har valgt at give den. En rejseagent kan måske finde fly, men ikke redigere kundedata — det handler om, hvad du forbinder.

- **Hukommelse + viden** — Agenter kan have korttidshukommelse (den aktuelle samtale) og langtidshukommelse (en kundedatabase, tidligere interaktioner). Rejseagenten kunne "huske", at du foretrækker sæder ved vinduet.

---

### De forskellige typer AI-agenter

Ikke alle agenter er bygget ens. Her er en oversigt over hovedtyperne, med en rejsebookingsagent som løbende eksempel:

| **Agenttype** | **Hvad den gør** | **Eksempel med rejseagent** |
|---|---|---|
| **Enkle refleksagenter** | Følger hårdkodede regler — ingen hukommelse, ingen planlægning. | Ser en klageemail → videresender den til kundeservice. Det er alt. |
| **Model-baserede refleksagenter** | Har en intern model af verden og opdaterer den, efterhånden som ting ændrer sig. | Holder øje med historiske flypriser og flagger ruter, der pludseligt bliver dyre. |
| **Målorienterede agenter** | Har et mål i tankerne og finder ud af at opnå det trin for trin. | Booker en hel rejse (fly, bil, hotel) med udgangspunkt i din nuværende placering for at få dig til dit mål. |
| **Nytteorienterede agenter** | Finder ikke bare *en* løsning — men den *bedste* ved at veje fordele og ulemper. | Balancerer pris mod bekvemmelighed for at finde den rejse, der bedst opfylder dine præferencer. |
| **Lærende agenter** | Bliver bedre over tid ved at lære af feedback. | Justerer fremtidige bookingforslag baseret på spørgeskemasvar efter rejsen. |
| **Hierarkiske agenter** | En agent på højt niveau opdeler opgaver i delopgaver og delegerer til lavere niveau agenter. | En "annuller rejse"-anmodning deles op i: annuller fly, annuller hotel, annuller billeje — hver håndteres af en underagent. |
| **Multi-agent systemer (MAS)** | Flere uafhængige agenter, der arbejder sammen (eller konkurrerer). | Kooperativ: separate agenter tager sig af hoteller, fly og underholdning. Konkurrerende: flere agenter konkurrerer om at få fyldt hotelværelser til den bedste pris. |

---

## Hvornår man skal bruge AI-agenter

Bare fordi du *kan* bruge en AI-agent, betyder det ikke, at du altid *skal*. Her er situationerne, hvor agenter virkelig er effektive:

![Hvornår man skal bruge AI-agenter?](../../../translated_images/da/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Åbne problemer** — Når trinnene til at løse et problem ikke kan forprogrammeres. Du har brug for, at LLM’en finder vejen dynamisk.
- **Flertrinsprocesser** — Opgaver, der kræver at bruge værktøjer over flere trin, ikke bare opslag eller generering af enkelt tekst.
- **Forbedring over tid** — Når du vil have systemet til at blive smartere baseret på brugerfeedback eller signaler fra miljøet.

Vi går dybere ind i, hvornår (og hvornår *ikke*) man skal bruge AI-agenter i lektionen **Building Trustworthy AI Agents** senere i kurset.

---

## Grundlæggende om agentbaserede løsninger

### Agentudvikling

Det første, du gør, når du bygger en agent, er at definere *hvad den kan gøre* — dens værktøjer, handlinger og adfærd.

På dette kursus bruger vi **Microsoft Foundry Agent Service** som vores hovedplatform. Den understøtter:

- Modeller fra udbydere som OpenAI, Mistral og Meta (Llama)
- Licenserede data fra udbydere som Tripadvisor
- Standardiserede OpenAPI 3.0 værktøjsdefinitioner

### Agentmønstre

Du kommunikerer med LLM’er via prompts. Med agenter kan du ikke altid håndfremstille hver prompt manuelt — agenten skal kunne handle over mange trin. Det er her, **agentmønstre** kommer ind. De er genanvendelige strategier til at promptstyre og orkestrere LLM’er på en mere skalerbar, pålidelig måde.

Dette kursus er struktureret omkring de mest almindelige og nyttige agentmønstre.

### Agentframeworks

Agentframeworks giver udviklere færdige skabeloner, værktøjer og infrastruktur til at bygge agenter. De gør det nemmere at:

- Tilkoble værktøjer og funktioner
- Observere, hvad agenten laver (og fejlfinde, når noget går galt)
- Samarbejde på tværs af flere agenter

På dette kursus fokuserer vi på **Microsoft Agent Framework (MAF)** til at bygge produktionsklare agenter.

---

## Eksempelkode

Klar til at se det i aktion? Her er eksempler på kode til denne lektion:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Har du spørgsmål?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at komme i kontakt med andre studerende, deltage i åbne kontortimer og få svar på dine AI-agentspørgsmål fra fællesskabet.


---

## Forrige lektion

[Opsætning af kursus](../00-course-setup/README.md)

## Næste lektion

[Udforskning af agentframeworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->