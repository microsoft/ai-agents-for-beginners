# Bruke Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentiske Protokoller](../../../translated_images/no/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikk på bildet over for å se video av denne leksjonen)_

Etter hvert som bruken av AI-agenter øker, øker også behovet for protokoller som sikrer standardisering, sikkerhet og støtter åpen innovasjon. I denne leksjonen vil vi dekke 3 protokoller som søker å møte dette behovet - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduksjon

I denne leksjonen vil vi dekke:

• Hvordan **MCP** gjør det mulig for AI-agenter å få tilgang til eksterne verktøy og data for å utføre brukeroppgaver.

• Hvordan **A2A** muliggjør kommunikasjon og samarbeid mellom forskjellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige språkgrensesnitt til enhver nettside, slik at AI-agenter kan oppdage og samhandle med innholdet.

## Læringsmål

• **Identifiser** kjerneformålet og fordelene med MCP, A2A og NLWeb i sammenheng med AI-agenter.

• **Forklar** hvordan hver protokoll legger til rette for kommunikasjon og interaksjon mellom LLM-er, verktøy og andre agenter.

• **Gjenkjenn** de distinkte rollene hver protokoll spiller i å bygge komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åpen standard som gir en standardisert måte for applikasjoner å gi kontekst og verktøy til LLM-er. Dette muliggjør en "universal adapter" til forskjellige datakilder og verktøy som AI-agenter kan koble til på en konsistent måte.

La oss se på komponentene i MCP, fordelene sammenlignet med direkte API-bruk, og et eksempel på hvordan AI-agenter kan bruke en MCP-server.

### MCP Kjernekomponenter

MCP opererer på en **klient-server-arkitektur** og kjernekomponentene er:

• **Hosts** er LLM-applikasjoner (for eksempel en kodeeditor som VSCode) som starter tilkoblinger til en MCP-server.

• **Klienter** er komponenter innenfor host-applikasjonen som opprettholder en-til-en-tilkoblinger med servere.

• **Servere** er lette programmer som eksponerer spesifikke kapasiteter.

Inkludert i protokollen er tre kjerneprimitiver som er kapabilitetene til en MCP-server:

• **Verktøy**: Dette er diskrete handlinger eller funksjoner en AI-agent kan kalle for å utføre en handling. For eksempel kan en værtjeneste tilby et «hent vær» verktøy, eller en e-handelsserver kan tilby et «kjøp produkt» verktøy. MCP-servere annonserer hvert verktøynavn, beskrivelse og inndata/utdataskjema i sin kapabilitetsliste.

• **Ressurser**: Dette er skrivebeskyttet dataelementer eller dokumenter som en MCP-server kan tilby, og klienter kan hente dem på forespørsel. Eksempler inkluderer filinnhold, databaseregistre eller loggfiler. Ressurser kan være tekst (som kode eller JSON) eller binære (som bilder eller PDF-er).

• **Prompts**: Dette er forhåndsdefinerte maler som gir foreslåtte prompts, noe som tillater mer komplekse arbeidsflyter.

### Fordeler med MCP

MCP tilbyr betydelige fordeler for AI-agenter:

• **Dynamisk Verktøysoppdagelse**: Agenter kan dynamisk motta en liste over tilgjengelige verktøy fra en server sammen med beskrivelser av hva de gjør. Dette står i kontrast til tradisjonelle API-er, som ofte krever statisk koding for integrasjoner, noe som betyr at enhver API-endring krever kodeoppdateringer. MCP tilbyr en «integrer én gang»-tilnærming, som gir større tilpasningsevne.

• **Interoperabilitet på tvers av LLM-er**: MCP fungerer på tvers av forskjellige LLM-er, og gir fleksibilitet til å bytte kjerne-modeller for evaluering for bedre ytelse.

• **Standardisert Sikkerhet**: MCP inkluderer en standard autentiseringsmetode, noe som forbedrer skalerbarheten når man legger til tilgang til flere MCP-servere. Dette er enklere enn å håndtere forskjellige nøkler og autentiseringstyper for ulike tradisjonelle API-er.

### MCP Eksempel

![MCP Diagram](../../../translated_images/no/mcp-diagram.e4ca1cbd551444a1.webp)

Tenk deg at en bruker ønsker å bestille en flyreise ved hjelp av en AI-assistent drevet av MCP.

1. **Tilkobling**: AI-assistenten (MCP-klienten) kobler seg til en MCP-server levert av et flyselskap.

2. **Verktøysoppdagelse**: Klienten spør flyselskapets MCP-server, "Hvilke verktøy har du tilgjengelig?" Serveren svarer med verktøy som "søk flyreiser" og "bestill flyreiser".

3. **Verktøykall**: Du ber så AI-assistenten: "Vennligst søk etter en flyreise fra Portland til Honolulu." AI-assistenten, ved bruk av sin LLM, identifiserer at den må kalle på "søk flyreiser" verktøyet og sender relevante parametere (avreise, destinasjon) til MCP-serveren.

4. **Utførelse og Respons**: MCP-serveren, som fungerer som et omslag, foretar det faktiske kallet til flyselskapets interne bestillings-API. Den mottar deretter flyinformasjonen (f.eks. JSON-data) og sender den tilbake til AI-assistenten.

5. **Videre Interaksjon**: AI-assistenten presenterer flyalternativene. Når du velger en flyreise, kan assistenten innkalle "bestill flyreise" verktøyet på samme MCP-server, og fullføre bestillingen.

## Agent-til-Agent Protokoll (A2A)

Mens MCP fokuserer på å koble LLM-er til verktøy, tar **Agent-til-Agent (A2A) protokollen** det et steg videre ved å muliggjøre kommunikasjon og samarbeid mellom forskjellige AI-agenter. A2A kobler AI-agenter på tvers av organisasjoner, miljøer og teknologistakker for å utføre en felles oppgave.

Vi vil undersøke komponentene og fordelene med A2A, sammen med et eksempel på hvordan det kan brukes i vår reiseapplikasjon.

### A2A Kjernekomponenter

A2A fokuserer på å muliggjøre kommunikasjon mellom agenter og la dem jobbe sammen for å fullføre en brukerens deloppgave. Hver komponent i protokollen bidrar til dette:

#### Agentkort

På samme måte som en MCP-server deler en liste over verktøy, har et Agentkort:
- Navnet på agenten.
- En **beskrivelse av generelle oppgaver** den utfører.
- En **liste over spesifikke ferdigheter** med beskrivelser for å hjelpe andre agenter (eller til og med menneskelige brukere) å forstå når og hvorfor de ønsker å kalle den agenten.
- Den **nåværende Endepunkt-URLen** til agenten
- Agentens **versjon** og **kapasiteter** som strømmede responser og push-varsler.

#### Agent Utfører

Agent Utføreren er ansvarlig for å **sende konteksten fra brukersamtalen til den eksterne agenten**, den eksterne agenten trenger dette for å forstå oppgaven som må utføres. I en A2A-server bruker agenten sin egen Large Language Model (LLM) for å tolke innkommende forespørsler og utføre oppgaver ved hjelp av egne interne verktøy.

#### Artefakt

Når en ekstern agent har fullført den forespurte oppgaven, opprettes resultatet som et artefakt. Et artefakt **inneholder resultatet av agentens arbeid**, en **beskrivelse av hva som ble fullført**, og **tekstkonteksten** som sendes gjennom protokollen. Etter at artefaktet er sendt, lukkes forbindelsen til den eksterne agenten inntil den trengs igjen.

#### Hendelseskø

Denne komponenten brukes til **å håndtere oppdateringer og sende meldinger**. Den er spesielt viktig i produksjon for agentiske systemer for å forhindre at forbindelsen mellom agenter lukkes før en oppgave er fullført, spesielt når oppgavefullføringstiden kan ta lengre tid.

### Fordeler med A2A

• **Forbedret Samarbeid**: Den gjør det mulig for agenter fra forskjellige leverandører og plattformer å interagere, dele kontekst og jobbe sammen, og muliggjør sømløs automatisering på tvers av tradisjonelt adskilte systemer.

• **Fleksibilitet i Modellvalg**: Hver A2A-agent kan selv bestemme hvilken LLM den bruker til å betjene sine forespørsler, noe som tillater optimaliserte eller finjusterte modeller per agent, i motsetning til en enkelt LLM-tilkobling i noen MCP-scenarier.

• **Innebygd Autentisering**: Autentisering er integrert direkte i A2A protokollen, noe som gir et robust sikkerhetsrammeverk for agentinteraksjoner.

### A2A Eksempel

![A2A Diagram](../../../translated_images/no/A2A-Diagram.8666928d648acc26.webp)

La oss utvide vårt scenario for reisebestilling, men denne gangen med A2A.

1. **Brukerforespørsel til Multi-Agent**: En bruker interagerer med en "Travel Agent" A2A klient/agent, kanskje ved å si: "Vennligst bestill en hel reise til Honolulu neste uke, inkludert fly, hotell og leiebil".

2. **Orkestrering av Reiseagent**: Reiseagenten mottar denne komplekse forespørselen. Den bruker sin LLM til å resonere rundt oppgaven og avgjør at den må samhandle med andre spesialiserte agenter.

3. **Kommunikasjon Mellom Agenter**: Reiseagenten bruker deretter A2A protokollen til å koble til underordnede agenter, for eksempel en "Flyselskap Agent", en "Hotell Agent" og en "Bilutleie Agent" som er opprettet av forskjellige selskaper.

4. **Delegert Oppgaveutførelse**: Reiseagenten sender spesifikke oppgaver til disse spesialiserte agentene (f.eks. "Finn fly til Honolulu", "Bestill et hotell", "Lei en bil"). Hver av disse spesialiserte agentene, som kjører sine egne LLM-er og bruker sine egne verktøy (som kan være MCP-servere selv), utfører sin del av bestillingen.

5. **Konsolidert Respons**: Når alle underordnede agenter fullfører sine oppgaver, samler Reiseagenten resultatene (flydetaljer, hotellbekreftelse, leiebilbestilling) og sender en omfattende, chat-lignende respons tilbake til brukeren.

## Natural Language Web (NLWeb)

Nettsteder har lenge vært den primære måten for brukere å få tilgang til informasjon og data på internett.

La oss se på de forskjellige komponentene i NLWeb, fordelene med NLWeb og et eksempel på hvordan vårt NLWeb fungerer ved å se på vår reiseapplikasjon.

### Komponenter i NLWeb

- **NLWeb-applikasjon (Kjerne Tjenestekode)**: Systemet som behandler spørsmål på naturlig språk. Det kobler de ulike delene av plattformen for å skape svar. Du kan tenke på det som **motoren som driver naturlige språkfunksjoner** på en nettside.

- **NLWeb-protokollen**: Dette er et **grunnleggende sett med regler for naturlig språkinteraksjon** med en nettside. Den sender tilbake svar i JSON-format (ofte ved bruk av Schema.org). Hensikten er å skape et enkelt fundament for “AI-nettet,” på samme måte som HTML gjorde det mulig å dele dokumenter på nettet.

- **MCP Server (Model Context Protocol Endepunkt)**: Hvert NLWeb-oppsett fungerer også som en **MCP-server**. Det betyr at den kan **dele verktøy (som en "spør" metode) og data** med andre AI-systemer. I praksis gjør dette nettsidens innhold og evner brukbare for AI-agenter, slik at nettstedet blir en del av det bredere "agentøkosystemet."

- **Inbedding-modeller**: Disse modellene brukes til å **konvertere nettsideinnhold til numeriske representasjoner kalt vektorer (embeddings)**. Disse vektorene fanger betydning på en måte som datamaskiner kan sammenligne og søke i. De lagres i en spesiell database, og brukere kan velge hvilken inbedding-modell de ønsker å bruke.

- **Vektordatabasesystem (Søkemekanisme)**: Denne databasen **lagrer inbeddingene av nettsideinnholdet**. Når noen stiller et spørsmål, sjekker NLWeb vektordatabasen for å raskt finne mest relevant informasjon. Den gir en rask liste over mulige svar, rangert etter likhet. NLWeb fungerer med forskjellige vektorlagringssystemer som Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb ved Eksempel

![NLWeb](../../../translated_images/no/nlweb-diagram.c1e2390b310e5fe4.webp)

Tenk på vårt reisebestillingsnettsted igjen, men denne gangen drevet av NLWeb.

1. **Datainntak**: Nettstedets eksisterende produktkataloger (f.eks. flylister, hotellbeskrivelser, rundturspakker) er formatert ved bruk av Schema.org eller lastet inn via RSS-feeds. NLWebs verktøy inntar denne strukturerte dataen, lager inbeddings, og lagrer den i en lokal eller ekstern vektordatabasedatabase.

2. **Spørsmål på Naturlig Språk (Menneske)**: En bruker besøker nettsiden og i stedet for å navigere menyer, skriver i et chat-grensesnitt: "Finn et familievennlig hotell i Honolulu med basseng for neste uke".

3. **NLWeb Behandling**: NLWeb-applikasjonen mottar denne forespørselen. Den sender spørsmålet til en LLM for forståelse og søker samtidig i sin vektordatabasen etter relevante hotelloppføringer.

4. **Nøyaktige Resultater**: LLM-en hjelper til med å tolke søkeresultatene fra databasen, identifisere de beste treff basert på kriteriene "familievennlig", "basseng" og "Honolulu", og formaterer deretter et naturlig språk-svar. Viktigst er at svaret refererer til faktiske hoteller fra nettstedets katalog, og unngår oppdiktet informasjon.

5. **AI Agent Interaksjon**: Fordi NLWeb fungerer som en MCP-server, kan en ekstern AI-reiseagent også koble seg til denne nettsidens NLWeb-instans. AI-agenten kan da bruke `ask` MCP-metoden til å spørre nettsiden direkte: `ask("Er det noen veganske restauranter i Honolulu-området anbefalt av hotellet?")`. NLWeb-instansen vil behandle dette, og utnytte sin database med restaurantinformasjon (hvis lastet inn), og returnere et strukturert JSON-svar.

### Har Du Flere Spørsmål om MCP/A2A/NLWeb?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortid og få svar på dine AI-agenter-relaterte spørsmål.

## Ressurser

- [MCP for Nybegynnere](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentasjon](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved bruk av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi etterstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For viktig informasjon anbefales profesjonell menneskelig oversettelse. Vi tar ikke ansvar for misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->