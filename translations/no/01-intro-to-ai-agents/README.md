[![Intro to AI Agents](../../../translated_images/no/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikk på bildet over for å se videoen til denne leksjonen)_

# Introduksjon til AI-agenter og bruksområder for agenter

Velkommen til kurset **AI Agents for Beginners**! Dette kurset gir deg grunnleggende kunnskap — og ekte fungerende kode — for å begynne å bygge AI-agenter fra bunnen av.

Kom og si hei i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — det er fullt av lærende og AI-byggere som gjerne svarer på spørsmål.

Før vi hopper til bygging, la oss først sørge for at vi faktisk forstår hva en AI-agent *er* og når det gir mening å bruke en.

---

## Introduksjon

Denne leksjonen dekker:

- Hva AI-agenter er, og de forskjellige typene som finnes
- Hvilke slags oppgaver AI-agenter passer best til
- Kjernebyggeklossene du vil bruke når du designer en agent-løsning

## Læringsmål

Når du er ferdig med denne leksjonen, bør du kunne:

- Forklare hva en AI-agent er og hvordan den skiller seg fra en vanlig AI-løsning
- Vite når du bør bruke en AI-agent (og når du ikke bør)
- Lage en enkel skisse for design av en agent-løsning for et ekte problem

---

## Definere AI-agenter og typer AI-agenter

### Hva er AI-agenter?

Her er en enkel måte å tenke på det:

> **AI-agenter er systemer som lar store språkmodeller (LLMs) faktisk *gjøre ting* — ved å gi dem verktøy og kunnskap til å handle i verden, ikke bare svare på forespørsler.**

La oss forklare litt nærmere:

- **System** — En AI-agent er ikke bare én ting. Det er en samling deler som jobber sammen. I kjernen har hver agent tre deler:
  - **Miljø** — Området agenten jobber i. For en reisebestillingsagent ville dette være selve bestillingsplattformen.
  - **Sensorer** — Hvordan agenten leser den nåværende tilstanden i miljøet. Reiseagenten kan sjekke hotelltilgjengelighet eller flypriser.
  - **Aktuatorer** — Hvordan agenten tar handling. Reiseagenten kan bestille et rom, sende en bekreftelse eller kansellere en reservasjon.

![Hva er AI-agenter?](../../../translated_images/no/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Store språkmodeller** — Agenter eksisterte før LLM-er, men LLM-er er det som gjør moderne agenter så kraftige. De kan forstå naturlig språk, resonnere over kontekst og gjøre en vag brukerforespørsel om til en konkret handlingsplan.

- **Utføre handlinger** — Uten et agent-system genererer LLM-en bare tekst. Inne i et agent-system kan LLM-en faktisk *utføre* trinn — søke i en database, kalle en API, sende en melding.

- **Tilgang til verktøy** — Hvilke verktøy agenten kan bruke avhenger av (1) miljøet den kjører i og (2) hva utvikleren har gitt den. En reiseagent kan søke etter fly men ikke redigere kundedata — det handler om hva du kobler opp.

- **Minne + kunnskap** — Agenter kan ha korttidsminne (den nåværende samtalen) og langtidsminne (en kundedatabase, tidligere interaksjoner). Reiseagenten kan "huske" at du foretrekker vindusseter.

---

### De forskjellige typene AI-agenter

Ikke alle agenter bygges likt. Her er en oversikt over hovedtypene, med en reisebestillingsagent som eksempel:

| **Agenttype** | **Hva den gjør** | **Reiseagent-eksempel** |
|---|---|---|
| **Enkle refleksagenter** | Følger fastkodede regler — intet minne, ingen planlegging. | Ser en klage-email → videresender til kundeservice. Basta. |
| **Modellbaserte refleksagenter** | Har en intern modell av verden og oppdaterer den når ting endrer seg. | Fører oversikt over historiske flypriser og varsler om ruter som plutselig blir dyre. |
| **Målbaserte agenter** | Har et mål i tankene og finner ut hvordan det kan nås steg for steg. | Bestiller en komplett tur (fly, bil, hotell) fra din nåværende posisjon til destinasjonen din. |
| **Nyttebaserte agenter** | Finner ikke bare *en* løsning — finner den *beste* ved å veie fordeler og ulemper. | Veier kostnad mot bekvemmelighet for å finne turen som scorer høyest i henhold til dine ønsker. |
| **Lærende agenter** | Blir bedre over tid ved å lære fra tilbakemeldinger. | Justerer fremtidige booking-anbefalinger basert på undersøkelsesresultater etter turen. |
| **Hierarkiske agenter** | En agent på høyt nivå deler opp arbeidet i deloppgaver og delegerer til agenter på lavere nivå. | En "avbestill tur"-forespørsel deles opp i: avbestill fly, avbestill hotell, avbestill leiebil — hver håndteres av en delagent. |
| **Multi-Agent Systemer (MAS)** | Flere uavhengige agenter som jobber sammen (eller konkurrerer). | Samarbeid: separate agenter tar seg av hoteller, fly og underholdning. Konkurranse: flere agenter konkurrerer om å fylle hotellrom til beste pris. |

---

## Når bruke AI-agenter

Bare fordi du *kan* bruke en AI-agent, betyr ikke at du alltid *bør*. Her er situasjonene hvor agenter virkelig utmerker seg:

![Når bruke AI-agenter?](../../../translated_images/no/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Åpne problemer** — Når stegene for å løse et problem ikke kan forhåndsprogrammeres. Du trenger at LLM-en finner veien dynamisk.
- **Flertrinnsprosesser** — Oppgaver som krever bruk av verktøy over flere steg, ikke bare et enkelt søk eller generering.
- **Forbedring over tid** — Når du ønsker at systemet skal bli smartere basert på brukertilbakemeldinger eller miljøsignaler.

Vi går mer i dybden på når (og når *ikke*) man burde bruke AI-agenter i leksjonen **Bygge pålitelige AI-agenter** senere i kurset.

---

## Grunnleggende om agent-løsninger

### Agentutvikling

Det første du gjør når du bygger en agent, er å definere *hva den kan gjøre* — dens verktøy, handlinger og oppførsel.

I dette kurset bruker vi **Microsoft Foundry Agent Service** som vår hovedplattform. Den støtter:

- Modeller fra tilbydere som OpenAI, Mistral og Meta (Llama)
- Lisensierte data fra tilbydere som Tripadvisor
- Standardiserte OpenAPI 3.0 verktøydefinisjoner

### Agent-mønstre

Du kommuniserer med LLM-er via prompts. Med agenter kan du ikke alltid lage hver prompt manuelt — agenten må ta handling over mange steg. Der kommer **Agent-mønstre** inn. De er gjenbrukbare strategier for prompting og orkestrering av LLM-er på en mer skalerbar, pålitelig måte.

Dette kurset er strukturert rundt de vanligste og mest nyttige agent-mønstrene.

### Agent-rammeverk

Agent-rammeverk gir utviklere ferdige maler, verktøy og infrastruktur for å bygge agenter. De gjør det lettere å:

- Koble opp verktøy og funksjoner
- Observere hva agenten gjør (og feilsøke når noe går galt)
- Samarbeide på tvers av flere agenter

I dette kurset fokuserer vi på **Microsoft Agent Framework (MAF)** for å bygge produksjonsklare agenter.

---

## Kodeeksempler

Klar til å se det i aksjon? Her er kodeeksemplene for denne leksjonen:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Har du spørsmål?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å komme i kontakt med andre lærende, delta på kontortid og få AI-agent-spørsmålene dine besvart av fellesskapet.


---

## Rask testing av denne agenten (valgfritt)

Når du lærer å distribuere agenter i [Leksjon 16](../16-deploying-scalable-agents/README.md), kan du legge til en rask helsesjekk etter distribusjon for denne leksjonens `TravelAgent` med den ferdige katalogen [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Se [`tests/README.md`](../tests/README.md) for hvordan du kjører den.

---

## Forrige leksjon

[Oppsett av kurset](../00-course-setup/README.md)

## Neste leksjon

[Utforske agent-rammeverk](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->