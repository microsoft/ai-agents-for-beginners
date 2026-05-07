[![Intro til AI-agenter](../../../translated_images/no/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikk på bildet over for å se videoen for denne leksjonen)_

# Introduksjon til AI-agenter og bruksområder for agenter

Velkommen til kurset **AI-agenter for nybegynnere**! Dette kurset gir deg grunnleggende kunnskap — og fungerende kode — for å begynne å bygge AI-agenter fra bunnen av.

Kom innom og si hei i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — det er fullt av elever og AI-byggere som gjerne svarer på spørsmål.

Før vi hopper i gang med byggingen, la oss sørge for at vi faktisk forstår hva en AI-agent *er* og når det gir mening å bruke en.

---

## Introduksjon

Denne leksjonen dekker:

- Hva AI-agenter er, og de forskjellige typene som finnes
- Hvilke typer oppgaver AI-agenter er best egnet for
- De grunnleggende byggeklossene du vil bruke når du designer en agentløsning

## Læringsmål

Når du er ferdig med denne leksjonen, skal du kunne:

- Forklare hva en AI-agent er og hvordan den skiller seg fra en vanlig AI-løsning
- Vite når du skal velge en AI-agent (og når du ikke skal)
- Skissere et grunnleggende design for en agentløsning på et reelt problem

---

## Definere AI-agenter og typer AI-agenter

### Hva er AI-agenter?

Her er en enkel måte å tenke på det:

> **AI-agenter er systemer som lar store språkmodeller (LLMs) faktisk *gjøre ting* — ved å gi dem verktøy og kunnskap til å handle på verden, ikke bare svare på forespørsler.**

La oss bryte det litt ned:

- **System** — En AI-agent er ikke bare én ting. Det er en samling deler som jobber sammen. Kjernen i enhver agent består av tre deler:
  - **Miljø** — Rommet agenten jobber i. For en reisebestillingsagent vil dette være bestillingsplattformen selv.
  - **Sensorer** — Hvordan agenten leser den nåværende tilstanden i miljøet sitt. Reiseagenten kan sjekke hotelltilgjengelighet eller flypriser.
  - **Aktuatorer** — Hvordan agenten tar handling. Reiseagenten kan bestille et rom, sende en bekreftelse eller kansellere en reservasjon.

![Hva er AI-agenter?](../../../translated_images/no/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Store språkmodeller** — Agenter fantes før LLM-er, men LLM-er gjør moderne agenter så kraftige. De kan forstå naturlig språk, tenke over kontekst og gjøre en vag brukerforespørsel om til en konkret handlingsplan.

- **Utføre handlinger** — Uten et agentsystem genererer en LLM bare tekst. Inne i et agentsystem kan LLM faktisk *utføre* steg — søke i en database, kalle en API, sende en melding.

- **Tilgang til verktøy** — Hvilke verktøy agenten kan bruke avhenger av (1) miljøet den kjører i og (2) hva utvikleren har gitt den. En reiseagent kan søke etter fly men ikke redigere kundedata — det handler om hva du kobler på.

- **Minne + kunnskap** — Agenter kan ha korttidsminne (den nåværende samtalen) og langtidsminne (en kundedatabase, tidligere interaksjoner). Reiseagenten kan «huske» at du foretrekker seter ved vinduet.

---

### De forskjellige typene AI-agenter

Ikke alle agenter er bygget likt. Her er en oversikt over hovedtypene, med en reisebestillingsagent som eksempel:

| **Agenttype** | **Hva den gjør** | **Eksempel med reiseagent** |
|---|---|---|
| **Enkle refleksagenter** | Følger forhåndsdefinerte regler — ingen hukommelse, ingen planlegging. | Ser en klagemail → videresender den til kundeservice. Det er det. |
| **Modellbaserte refleksagenter** | Har en intern modell av verden og oppdaterer den når ting endres. | Sporer historiske flypriser og markerer ruter som plutselig blir dyre. |
| **Målbaserte agenter** | Har et mål i tankene og finner ut hvordan det nås steg for steg. | Bestiller en komplett reise (fly, bil, hotell) fra ditt nåværende sted til destinasjonen. |
| **Nyttebaserte agenter** | Finner ikke bare *en* løsning — finner *den beste* ved å veie fordeler og ulemper. | Balanserer kostnad versus bekvemmelighet for å finne turen som passer dine preferanser best. |
| **Lærende agenter** | Blir bedre over tid ved å lære av tilbakemeldinger. | Justerer fremtidige bestillingsforslag basert på spørreundersøkelser etter reisen. |
| **Hierarkiske agenter** | En overordnet agent deler opp arbeid i deloppgaver og delegerer til agenter på lavere nivå. | En forespørsel om å «kansellere reise» deles opp i: kansellere fly, kansellere hotell, kansellere leiebil — hver håndtert av en underagent. |
| **Multi-agent-systemer (MAS)** | Flere uavhengige agenter som jobber sammen (eller konkurrerer). | Samarbeid: forskjellige agenter håndterer hotell, fly og underholdning. Konkurranse: flere agenter konkurrerer om å fylle hotellrom til beste pris. |

---

## Når å bruke AI-agenter

Bare fordi du *kan* bruke en AI-agent betyr ikke at du alltid *skal*. Her er situasjonene der agenter virkelig utmerker seg:

![Når bruke AI-agenter?](../../../translated_images/no/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Åpne problemer** — Når trinnene for å løse et problem ikke kan forhåndsprogrammeres. Du trenger at LLM finner veien dynamisk.
- **Flere trinns prosesser** — Oppgaver som krever bruk av verktøy over flere steg, ikke bare et enkelt oppslag eller generering.
- **Forbedring over tid** — Når du vil at systemet skal bli smartere basert på brukerfeedback eller miljøsignaler.

Vi går dypere inn på når (og når ikke) man skal bruke AI-agenter i leksjonen **Bygge pålitelige AI-agenter** senere i kurset.

---

## Grunnleggende om agentløsninger

### Agentutvikling

Det første du gjør når du bygger en agent er å definere *hva den kan gjøre* — verktøyene, handlingene og oppførselen.

I dette kurset bruker vi **Azure AI Agent Service** som hovedplattform. Den støtter:

- Åpne modeller som OpenAI, Mistral og Llama
- Lisensiert data fra leverandører som Tripadvisor
- Standardiserte OpenAPI 3.0-definisjoner for verktøy

### Agentmønstre

Du kommuniserer med LLM-er gjennom prompt. Med agenter kan du ikke alltid håndlage hver prompt manuelt — agenten må kunne ta handling over mange steg. Det er her **agentmønstre** kommer inn. De er gjenbrukbare strategier for å prompt og orkestrere LLM-er på en mer skalerbar og pålitelig måte.

Dette kurset er strukturert rundt de mest vanlige og nyttige agentmønstrene.

### Agentrammeverk

Agentrammeverk gir utviklere ferdige maler, verktøy og infrastruktur for å bygge agenter. De gjør det enklere å:

- Koble til verktøy og funksjoner
- Observere hva agenten gjør (og feilsøke ved feil)
- Samarbeide på tvers av flere agenter

I dette kurset fokuserer vi på **Microsoft Agent Framework (MAF)** for å bygge produksjonsklare agenter.

---

## Kodeeksempler

Klar til å se det i praksis? Her er kodeeksemplene for denne leksjonen:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Har du spørsmål?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å knytte kontakt med andre elever, delta på kontortimer og få svar på dine spørsmål om AI-agenter fra fellesskapet.

---

## Forrige leksjon

[Oppsett av kurs](../00-course-setup/README.md)

## Neste leksjon

[Utforske agentrammeverk](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettingstjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi strekker oss etter nøyaktighet, vennligst vær klar over at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->