[![Intro til AI-agenter](../../../translated_images/no/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikk på bildet over for å se videoen til denne leksjonen)_

# Introduksjon til AI-agenter og bruksområder for agenter

Velkommen til **AI Agents for Beginners**-kurset! Dette kurset gir deg grunnleggende kunnskap — og fungerende kode — for å begynne å bygge AI-agenter fra bunnen av.

Kom og si hei i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord-fellesskapet</a> — det er fullt av lærende og AI-bygger som gjerne svarer på spørsmål.

Før vi hopper inn i byggingen, la oss først sørge for at vi faktisk forstår hva en AI-agent *er* og når det gir mening å bruke en.

---

## Introduksjon

Denne leksjonen dekker:

- Hva AI-agenter er, og de forskjellige typene som finnes
- Hvilke oppgaver AI-agenter egner seg best for
- De grunnleggende byggesteinene du bruker når du designer en agentløsning

## Læringsmål

Ved slutten av denne leksjonen bør du kunne:

- Forklare hva en AI-agent er og hvordan den skiller seg fra en vanlig AI-løsning
- Vite når du bør bruke en AI-agent (og når ikke)
- Skissere en grunnleggende agentløsning for et virkelighetsbasert problem

---

## Definere AI-agenter og typer AI-agenter

### Hva er AI-agenter?

Her er en enkel måte å tenke på det:

> **AI-agenter er systemer som lar store språkmodeller (LLMs) faktisk *gjøre ting* — ved å gi dem verktøy og kunnskap til å handle i verden, ikke bare svare på spørsmål.**

La oss bryte det ned litt:

- **System** — En AI-agent er ikke bare én ting. Det er en samling deler som jobber sammen. I kjernen har hver agent tre deler:
  - **Miljø** — Området agenten arbeider i. For en reisebestillingsagent vil dette være selve bestillingsplattformen.
  - **Sensorer** — Hvordan agenten leser den nåværende tilstanden i miljøet sitt. Vår reiseagent kan sjekke hotelltilgjengelighet eller flypriser.
  - **Aktuatorer** — Hvordan agenten utfører handlinger. Reiseagenten kan bestille et rom, sende en bekreftelse eller avbestille en reservasjon.

![Hva er AI-agenter?](../../../translated_images/no/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Store språkmodeller** — Agenter fantes før LLM-er, men det er LLM-ene som gjør moderne agenter så kraftige. De kan forstå naturlig språk, resonnere rundt kontekst, og omskape en vag brukerforespørsel til en konkret handlingsplan.

- **Utføre handlinger** — Uten et agentsystem genererer LLM bare tekst. Inne i et agentsystem kan LLM faktisk *utføre* steg — søke i en database, kalle et API, sende en melding.

- **Tilgang til verktøy** — Hvilke verktøy agenten kan bruke avhenger av (1) miljøet den kjører i, og (2) hva utvikleren har valgt å gi den. En reiseagent kan kanskje søke flyreiser, men ikke redigere kunderegistre — det handler om hva du kobler opp.

- **Minne + Kunnskap** — Agenter kan ha korttidsminne (den pågående samtalen) og langtidsminne (en kundedatabase, tidligere interaksjoner). Reiseagenten kan for eksempel "huske" at du foretrekker vindusplasser.

---

### De forskjellige typene AI-agenter

Ikke alle agenter bygges på samme måte. Her er en oversikt over de viktigste typene, med reisebestillingsagenten som eksempel:

| **Agenttype** | **Hva den gjør** | **Eksempel: Reiseagent** |
|---|---|---|
| **Enkel refleksagent** | Følger faste regler — uten minne, uten planlegging. | Ser en klage-epost → videresender den til kundeservice. That's it. |
| **Modellbasert refleksagent** | Holder en intern modell av verden og oppdaterer den når ting endres. | Holder oversikt over historiske flypriser og varsler om ruter som plutselig er dyre. |
| **Målbasert agent** | Har et mål i sikte og finner ut hvordan det nås steg for steg. | Bestiller en hel reise (fly, bil, hotell) fra din nåværende posisjon til målet. |
| **Nyttebasert agent** | Finnes ikke bare *en* løsning — finner den *beste* ved å veie fordeler og ulemper. | Veier kostnad opp mot bekvemmelighet for å finne reisen som scorer høyest på dine preferanser. |
| **Lærende agent** | Blir bedre over tid ved å lære av tilbakemeldinger. | Justerer fremtidige bookingforslag basert på evalueringer etter reisen. |
| **Hierarkisk agent** | En overordnet agent deler opp oppgaver i underoppgaver og delegerer til lavere agenter. | En "avbestill reise"-forespørsel deles i: avbestill fly, avbestill hotell, avbestill bilutleie — håndtert av under-agenter. |
| **Multi-agent-systemer (MAS)** | Flere uavhengige agenter jobber sammen (eller konkurrerer). | Samarbeid: ulike agenter håndterer hotell, fly og underholdning. Konkurranse: flere agenter konkurrerer om å fylle hotellrom til beste pris. |

---

## Når bruke AI-agenter

Bare fordi du *kan* bruke en AI-agent, betyr ikke det at du alltid *bør*. Her er situasjonene hvor agenter virkelig utmerker seg:

![Når bruke AI-agenter?](../../../translated_images/no/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Åpne problemer** — Når stegene for å løse et problem ikke kan forhåndsprogrammeres. Du trenger at LLM dynamisk finner veien.
- **Flere steg i prosesser** — Oppgaver som krever bruk av verktøy i flere omganger, ikke bare ett enkelt oppslag eller generering.
- **Forbedring over tid** — Når du ønsker at systemet skal bli smartere basert på brukerfeedback eller signaler fra miljøet.

Vi går mer i dybden på når (og når *ikke*) du bør bruke AI-agenter i leksjonen **Bygg pålitelige AI-agenter** senere i kurset.

---

## Grunnleggende om agentløsninger

### Agentutvikling

Det første du gjør når du bygger en agent er å definere *hva den kan gjøre* — hvilke verktøy, handlinger og adferd den har.

I dette kurset bruker vi **Azure AI Agent Service** som hovedplattform. Den støtter:

- Modeller fra leverandører som OpenAI, Mistral og Meta (Llama)
- Lisensierte data fra leverandører som Tripadvisor
- Standardiserte OpenAPI 3.0 verktøydefinisjoner

### Agentmønstre

Du kommuniserer med LLM-er via prompts. Med agenter kan du ikke alltid håndskrive hver prompt manuelt — agenten må kunne handle over flere steg. Derfor har vi **agentmønstre**. De er gjenbrukbare strategier for å promptlyse og orkestrere LLM-er på en mer skalerbar og pålitelig måte.

Dette kurset er strukturert rundt de mest vanlige og nyttige agentmønstrene.

### Agentrammeverk

Agentrammeverk gir utviklere ferdige maler, verktøy og infrastruktur for å bygge agenter. De gjør det enklere å:

- Koble opp verktøy og funksjonalitet
- Observere hva agenten gjør (og feilsøke ved problemer)
- Samarbeide på tvers av flere agenter

I dette kurset fokuserer vi på **Microsoft Agent Framework (MAF)** for å bygge produksjonsklare agenter.

---

## Kodeeksempler

Klar til å se det i praksis? Her er kodeeksemplene for denne leksjonen:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Har du spørsmål?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å koble med andre lærende, delta på kontortid, og få svar på spørsmål om AI-agenter fra fellesskapet.

---

## Forrige leksjon

[Kurset settes opp](../00-course-setup/README.md)

## Neste leksjon

[Utforske agentrammeverk](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->