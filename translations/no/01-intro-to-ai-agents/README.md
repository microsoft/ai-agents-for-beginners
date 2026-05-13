[![Intro to AI Agents](../../../translated_images/no/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikk på bildet ovenfor for å se videoen til denne leksjonen)_

# Introduksjon til AI-agenter og bruksområder for agenter

Velkommen til kurset **AI Agents for Beginners**! Dette kurset gir deg grunnleggende kunnskap — og ekte fungerende kode — for å begynne å bygge AI-agenter fra bunnen av.

Kom og si hei i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — det er fullt av lærende og AI-byggere som gjerne svarer på spørsmål.

Før vi hopper i gang med byggingen, la oss sørge for at vi faktisk forstår hva en AI-agent *er* og når det gir mening å bruke en.

---

## Introduksjon

Denne leksjonen dekker:

- Hva AI-agenter er, og de forskjellige typene som finnes
- Hvilke slags oppgaver AI-agenter egner seg best for
- Kjernen av byggesteiner du vil bruke når du designer en agentbasert løsning

## Læringsmål

Innen slutten av denne leksjonen bør du kunne:

- Forklare hva en AI-agent er og hvordan den skiller seg fra en vanlig AI-løsning
- Vite når du bør bruke en AI-agent (og når du ikke bør)
- Skissere et enkelt agentbasert løsningsdesign for et problem fra den virkelige verden

---

## Definere AI-agenter og typer AI-agenter

### Hva er AI-agenter?

Her er en enkel måte å tenke på det:

> **AI-agenter er systemer som lar store språkmodeller (LLMer) faktisk *gjøre ting* — ved å gi dem verktøy og kunnskap til å handle i verden, ikke bare svare på spørsmål.**

La oss belyse det litt:

- **System** — En AI-agent er ikke bare én ting. Det er en samling deler som jobber sammen. Kjernen i enhver agent består av tre deler:
  - **Miljø** — Området agenten opererer i. For en reisebestillingsagent ville dette være bookingsystemet.
  - **Sensorer** — Hvordan agenten leser den nåværende tilstanden i miljøet. Reiseagenten kan sjekke hotelltilgjengelighet eller flypriser.
  - **Aktuatorer** — Hvordan agenten utfører handling. Reiseagenten kan bestille et rom, sende en bekreftelse eller avbryte en reservasjon.

![Hva er AI-agenter?](../../../translated_images/no/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Store språkmodeller** — Agenter fantes før LLM-er, men det er LLM-ene som gjør moderne agenter så kraftfulle. De kan forstå naturlig språk, resonnere over kontekst og gjøre en uklar brukerforespørsel om til en konkret handlingsplan.

- **Utføre handlinger** — Uten et agentsystem genererer en LLM bare tekst. Inne i et agentsystem kan LLM faktisk *utføre* steg — søke i en database, kontakte en API, sende en melding.

- **Tilgang til verktøy** — Hvilke verktøy agenten kan bruke avhenger av (1) miljøet den kjører i og (2) hva utvikleren har valgt å gi den. En reiseagent kan for eksempel søke etter fly men ikke redigere kundedata — alt handler om hva du kobler til.

- **Minne + kunnskap** — Agenter kan ha korttidsminne (den nåværende samtalen) og langtidsminne (en kundedatabase, tidligere interaksjoner). Reiseagenten kan "huske" at du foretrekker vindusseter.

---

### De forskjellige typene AI-agenter

Ikke alle agenter er bygget på samme måte. Her er en oversikt over hovedtypene, med en reisebestillingsagent som løpende eksempel:

| **Agenttype** | **Hva den gjør** | **Eksempel med reiseagent** |
|---|---|---|
| **Enkle refleksagenter** | Følger forhåndsdefinerte regler — ingen minner, ingen planlegging. | Ser en klage-epost → videresender den til kundeservice. Det er alt. |
| **Modellbaserte refleksagenter** | Har en intern modell av verden som oppdateres når ting endrer seg. | Følger historiske flypriser og varsler om ruter som plutselig blir dyre. |
| **Målbaserte agenter** | Har et mål og finner ut hvordan det skal nås steg for steg. | Bestiller en hel reise (fly, bil, hotell) fra nåværende sted til destinasjonen din. |
| **Nyttebaserte agenter** | Finner ikke bare *en* løsning — finner den *beste* ved å veie fordeler og ulemper. | Balansere kostnad vs. bekvemmelighet for å finne reisen som passer best for dine preferanser. |
| **Lærende agenter** | Blir bedre over tid ved å lære av tilbakemeldinger. | Justerer fremtidige bookinganbefalinger basert på spørreundersøkelser etter turen. |
| **Hierarkiske agenter** | En overordnet agent deler oppgavene i deloppgaver og delegerer til underordnede agenter. | En «avbestill tur»-forespørsel deles opp i: avbestill fly, avbestill hotell, avbestill leiebil — hver håndtert av en sub-agent. |
| **Multi-agent systemer (MAS)** | Flere uavhengige agenter som jobber sammen (eller konkurrerer). | Samarbeid: separate agenter håndterer hotell, fly og underholdning. Konkurranse: flere agenter konkurrerer om å fylle hotellrom til best pris. |

---

## Når bør man bruke AI-agenter

Bare fordi du *kan* bruke en AI-agent, betyr det ikke at du alltid *bør*. Her er situasjonene hvor agenter virkelig skinner:

![Når bør man bruke AI-agenter?](../../../translated_images/no/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Åpne problemer** — Når stegene for å løse et problem ikke kan forhåndsprogrammeres. Du trenger at LLM-en finner veien dynamisk.
- **Prosesser med flere steg** — Oppgaver som krever verktøy brukt over flere omganger, ikke bare ett enkelt oppslag eller generering.
- **Forbedring over tid** — Når du vil at systemet skal bli smartere basert på brukerfeedback eller miljøsignaler.

Vi går mer i dybden på når (og når *ikke*) man skal bruke AI-agenter i leksjonen **Building Trustworthy AI Agents** senere i kurset.

---

## Grunnleggende om agentbaserte løsninger

### Agentutvikling

Det første du gjør når du bygger en agent, er å definere *hva den kan gjøre* — hvilke verktøy, handlinger og atferd den har.

I dette kurset bruker vi **Azure AI Agent Service** som hovedplattform. Den støtter:

- Modeller fra leverandører som OpenAI, Mistral og Meta (Llama)
- Lisensiert data fra leverandører som Tripadvisor
- Standardiserte OpenAPI 3.0-verktøydefinisjoner

### Agentmønstre

Du kommuniserer med LLM-er via prompts. Med agenter kan du ikke alltid lage hver prompt manuelt — agenten må kunne utføre handlinger over mange steg. Her kommer **agentmønstre** inn i bildet. De er gjenbrukbare strategier for prompting og orkestrering av LLM-er på en mer skalerbar, pålitelig måte.

Dette kurset er strukturert rundt de mest vanlige og nyttige agentmønstrene.

### Agentrammeverk

Agentrammeverk gir utviklere ferdige maler, verktøy og infrastruktur for å bygge agenter. De gjør det enklere å:

- Koble opp verktøy og funksjonalitet
- Observere hva agenten gjør (og feilsøke når noe går galt)
- Samarbeide på tvers av flere agenter

I dette kurset fokuserer vi på **Microsoft Agent Framework (MAF)** for å bygge produksjonsklare agenter.

---

## Kodeeksempler

Klar til å se det i praksis? Her er kodeeksemplene til denne leksjonen:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Spørsmål?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å kontakte andre lærende, delta på kontortid og få besvart spørsmål om AI-agenter av fellesskapet.

---

## Forrige leksjon

[Course Setup](../00-course-setup/README.md)

## Neste leksjon

[Utforske agentrammeverk](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->