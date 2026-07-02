# Bruk av Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentic Protocols](../../../translated_images/no/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikk på bildet ovenfor for å se video av denne leksjonen)_

Etter hvert som bruken av AI-agenter øker, øker også behovet for protokoller som sikrer standardisering, sikkerhet og støtter åpen innovasjon. I denne leksjonen vil vi dekke 3 protokoller som søker å møte dette behovet - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduksjon

I denne leksjonen vil vi dekke:

• Hvordan **MCP** lar AI-agenter få tilgang til eksterne verktøy og data for å fullføre brukeroppgaver.

• Hvordan **A2A** muliggjør kommunikasjon og samarbeid mellom forskjellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige språkgrensesnitt til et hvilket som helst nettsted, noe som gjør det mulig for AI-agenter å oppdage og samhandle med innholdet.

## Læringsmål

• **Identifisere** hovedformålet og fordelene med MCP, A2A, og NLWeb i konteksten av AI-agenter.

• **Forklare** hvordan hver protokoll legger til rette for kommunikasjon og samhandling mellom LLM-er, verktøy og andre agenter.

• **Gjenkjenne** de distinkte rollene hver protokoll spiller i å bygge komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åpen standard som tilbyr en standardisert måte for applikasjoner å gi kontekst og verktøy til LLM-er. Dette muliggjør en "universell adapter" til forskjellige datakilder og verktøy som AI-agenter kan koble seg til på en konsekvent måte.

La oss se på komponentene i MCP, fordelene sammenlignet med direkte API-bruk, og et eksempel på hvordan AI-agenter kan bruke en MCP-server.

### MCP Kjernekomponenter

MCP opererer med en **klient-server-arkitektur** og de kjernekomponentene er:

• **Verter** er LLM-applikasjoner (for eksempel en kodeeditor som VSCode) som starter forbindelsene til en MCP-server.

• **Klienter** er komponenter innen vertapplikasjonen som opprettholder én-til-én-forbindelser med servere.

• **Servere** er lette programmer som eksponerer spesifikke funksjonaliteter.

Inkludert i protokollen er tre kjerneprimitivelementer som er funksjonene til en MCP-server:

• **Verktøy**: Dette er diskrete handlinger eller funksjoner en AI-agent kan kalle for å utføre en handling. For eksempel kan en værtjeneste eksponere et "hent vær" verktøy, eller en e-handelsserver kan eksponere et "kjøp produkt"-verktøy. MCP-servere annonserer hvert verktøynavn, beskrivelse og input/output-skjema i sin funksjonsliste.

• **Ressurser**: Dette er skrivebeskyttede dataelementer eller dokumenter som en MCP-server kan tilby, og klienter kan hente dem ved behov. Eksempler inkluderer filinnhold, databaseposter eller loggfiler. Ressurser kan være tekst (som kode eller JSON) eller binære (som bilder eller PDF-er).

• **Forespørsler**: Dette er forhåndsdefinerte maler som gir foreslåtte forespørsler, og muliggjør mer komplekse arbeidsflyter.

### Fordeler med MCP

MCP tilbyr betydelige fordeler for AI-agenter:

• **Dynamisk verktøyoppdagelse**: Agenter kan dynamisk motta en liste over tilgjengelige verktøy fra en server, sammen med beskrivelser av hva de gjør. Dette står i kontrast til tradisjonelle API-er, som ofte krever statisk koding for integrasjoner, noe som betyr at enhver API-endring krever kodeoppdateringer. MCP tilbyr en "integrer en gang"-tilnærming, som fører til større tilpasningsevne.

• **Interoperabilitet på tvers av LLM-er**: MCP fungerer på tvers av forskjellige LLM-er, og gir fleksibilitet til å bytte kjerne-modeller for å evaluere bedre ytelse.

• **Standardisert sikkerhet**: MCP inkluderer en standard autentiseringsmetode, som forbedrer skalerbarheten når man legger til tilgang til flere MCP-servere. Dette er enklere enn å håndtere ulike nøkler og autentiseringstyper for ulike tradisjonelle API-er.

### MCP Eksempel

![MCP Diagram](../../../translated_images/no/mcp-diagram.e4ca1cbd551444a1.webp)

Tenk deg at en bruker ønsker å bestille en flyreise ved hjelp av en AI-assistent drevet av MCP.

1. **Forbindelse**: AI-assistenten (MCP-klienten) kobler seg til en MCP-server levert av et flyselskap.

2. **Verktøyoppdagelse**: Klienten spør flyselskapets MCP-server: "Hvilke verktøy har dere tilgjengelig?" Serveren svarer med verktøy som "søk flyreiser" og "bestill flyreise".

3. **Verktøysanrop**: Du ber AI-assistenten: "Vennligst søk etter en flyreise fra Portland til Honolulu." AI-assistenten, ved bruk av sin LLM, identifiserer at den må kalle "søk flyreiser"-verktøyet og sender relevante parametere (avreisested, destinasjon) til MCP-serveren.

4. **Utførelse og Svar**: MCP-serveren, som fungerer som en wrapper, utfører det faktiske anropet til flyselskapets interne bestillings-API. Deretter mottar den flyinformasjonen (f.eks. JSON-data) og sender den tilbake til AI-assistenten.

5. **Videre Samhandling**: AI-assistenten presenterer flyalternativene. Når du velger en flyreise, kan assistenten kalle "bestill flyreise"-verktøyet på samme MCP-server og fullføre bestillingen.

## Agent-til-Agent Protokoll (A2A)

Mens MCP fokuserer på å koble LLM-er til verktøy, tar **Agent-til-Agent (A2A) protokollen** det et steg videre ved å muliggjøre kommunikasjon og samarbeid mellom forskjellige AI-agenter. A2A kobler AI-agenter på tvers av ulike organisasjoner, miljøer og teknologistakker for å fullføre en delt oppgave.

Vi skal undersøke komponentene og fordelene ved A2A, sammen med et eksempel på hvordan det kan brukes i vår reiseapplikasjon.

### A2A Kjernekomponenter

A2A fokuserer på å gjøre det mulig for agenter å kommunisere og samarbeide for å fullføre en deloppgave for brukeren. Hver komponent i protokollen bidrar til dette:

#### Agentkort

På samme måte som en MCP-server deler en liste over verktøy, har et Agentkort:
- Navnet på agenten.
- En **beskrivelse av de generelle oppgavene** den utfører.
- En **liste over spesifikke ferdigheter** med beskrivelser for å hjelpe andre agenter (eller til og med menneskelige brukere) å forstå når og hvorfor de vil kalle den agenten.
- Den **nåværende Endepunkt-URL-en** til agenten.
- Agentens **versjon** og **funksjoner** som for eksempel streaming av svar og push-varslinger.

#### Agent Execute

Agent Execute har ansvar for **å sende konteksten fra brukerchatten til den eksterne agenten**, den eksterne agenten trenger dette for å forstå oppgaven som skal fullføres. I en A2A-server bruker en agent sin egen Large Language Model (LLM) for å tolke innkommende forespørsler og utføre oppgaver ved hjelp av sine interne verktøy.

#### Artefakt

Når en ekstern agent har fullført den forespurte oppgaven, blir produktet av arbeidet opprettet som et artefakt. Et artefakt **inneholder resultatet av agentens arbeid**, en **beskrivelse av hva som ble fullført**, og **tekstkonteksten** som sendes gjennom protokollen. Etter at artefaktet er sendt, lukkes forbindelsen til den eksterne agenten inntil den trengs igjen.

#### Hendelseskø

Denne komponenten brukes til **å håndtere oppdateringer og sende meldinger**. Den er spesielt viktig i produksjon for agentiske systemer for å forhindre at forbindelsen mellom agenter lukkes før en oppgave er fullført, spesielt når oppgavens fullføringstid kan være lang.

### Fordeler med A2A

• **Forbedret Samarbeid**: Den gjør det mulig for agenter fra forskjellige leverandører og plattformer å samhandle, dele kontekst og jobbe sammen, noe som muliggjør sømløs automatisering på tvers av tradisjonelt frakoblede systemer.

• **Fleksibilitet i Modellvalg**: Hver A2A-agent kan bestemme hvilken LLM den bruker for å betjene forespørslene sine, noe som tillater optimaliserte eller finjusterte modeller per agent, i motsetning til en enkelt LLM-tilkobling i noen MCP-scenarier.

• **Innebygd Autentisering**: Autentisering er integrert direkte i A2A-protokollen, som gir en robust sikkerhetsramme for agentinteraksjoner.

### A2A Eksempel

![A2A Diagram](../../../translated_images/no/A2A-Diagram.8666928d648acc26.webp)

La oss utvide vårt reisebestillingsscenario, men denne gangen med A2A.

1. **Brukerforespørsel til Multi-Agent**: En bruker interagerer med en "Reiseagent" A2A-klient/agent, kanskje ved å si: "Vennligst bestill en hel tur til Honolulu neste uke, inkludert fly, hotell og leiebil".

2. **Orkestrering av Reiseagent**: Reiseagenten mottar denne komplekse forespørselen. Den bruker sin LLM for å resonnere rundt oppgaven og avgjøre at den må samhandle med andre spesialiserte agenter.

3. **Kommunikasjon Mellom Agenter**: Reiseagenten bruker deretter A2A-protokollen for å koble seg til nedstrøms agenter, som en "Flyselskap Agent", en "Hotell Agent" og en "Leiebil Agent" som er opprettet av forskjellige selskaper.

4. **Delegert Oppgaveutførelse**: Reiseagenten sender spesifikke oppgaver til disse spesialiserte agentene (f.eks. "Finn flyreiser til Honolulu," "Bestill hotell," "Lei bil"). Hver av disse spesialiserte agentene, som kjører sine egne LLM-er og bruker sine egne verktøy (som selv kan være MCP-servere), utfører sin del av bestillingen.

5. **Konsolidert Svar**: Når alle nedstrømsagentene har fullført sine oppgaver, samler Reiseagenten resultatene (flydetaljer, hotellbekreftelse, leiebilbestilling) og sender et omfattende, chattelignende svar tilbake til brukeren.

## Natural Language Web (NLWeb)

Nettsteder har lenge vært den primære måten for brukere å få tilgang til informasjon og data på internett.

La oss se på de ulike komponentene i NLWeb, fordelene med NLWeb og et eksempel på hvordan vår NLWeb fungerer ved å se på vår reiseapplikasjon.

### Komponenter i NLWeb

- **NLWeb-applikasjon (Kjernekode for tjenesten)**: Systemet som behandler spørsmål på naturlig språk. Den kobler de forskjellige delene av plattformen for å skape svar. Du kan tenke på det som **motoren som driver de naturlige språkfunksjonene** på et nettsted.

- **NLWeb Protokoll**: Dette er et **grunnleggende sett med regler for naturlig språkinteraksjon** med et nettsted. Det sender tilbake svar i JSON-format (ofte ved bruk av Schema.org). Hensikten er å skape et enkelt fundament for "AI Web," på samme måte som HTML gjorde det mulig å dele dokumenter på nettet.

- **MCP Server (Model Context Protocol Endepunkt)**: Hver NLWeb-oppsett fungerer også som en **MCP-server**. Det betyr at den kan **dele verktøy (som en "ask"-metode) og data** med andre AI-systemer. I praksis gjør dette nettsidens innhold og kapasiteter tilgjengelig for AI-agenter, slik at siden kan bli en del av det bredere "agentøkosystemet."

- **Embedding-modeller**: Disse modellene brukes til å **konvertere nettsideinnhold til numeriske representasjoner kalt vektorer** (embeddings). Disse vektorene fanger mening på en måte som datamaskiner kan sammenligne og søke i. De lagres i en spesiell database, og brukere kan velge hvilken embedding-modell de ønsker å bruke.

- **Vektordatabasen (Hentingsmekanisme)**: Denne databasen **lagrer embeddingene av nettsideinnholdet**. Når noen stiller et spørsmål, sjekker NLWeb vektordatabasen for å raskt finne den mest relevante informasjonen. Den gir en rask liste over mulige svar, rangert etter likhet. NLWeb fungerer med forskjellige vektorlagringssystemer som Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb ved Eksempel

![NLWeb](../../../translated_images/no/nlweb-diagram.c1e2390b310e5fe4.webp)

Tenk igjen på vårt reisebestillingsnettsted, men denne gangen er det drevet av NLWeb.

1. **Data Inntak**: Reise-nettstedets eksisterende produktkataloger (f.eks. flyliste, hotellbeskrivelser, turistpakker) blir formatert ved hjelp av Schema.org eller lastet inn via RSS-feeder. NLWebs verktøy inntar disse strukturerte dataene, lager embeddings og lagrer dem i en lokal eller ekstern vektordatabasen.

2. **Spørsmål på Naturlig Språk (Menneskelig)**: En bruker besøker nettstedet og, i stedet for å navigere i menyer, skriver i en chatgrensesnitt: "Finn et familievennlig hotell i Honolulu med basseng for neste uke".

3. **NLWeb Behandling**: NLWeb-applikasjonen mottar dette spørsmålet. Den sender forespørselen til en LLM for forståelse og søker samtidig i vektordatabasen etter relevante hotellister.

4. **Nøyaktige Resultater**: LLM-en hjelper med å tolke søkeresultatene fra databasen, identifisere de beste treffene basert på kriteriene "familievennlig," "basseng," og "Honolulu," og formaterer deretter et svar i naturlig språk. Det er avgjørende at svaret viser til faktiske hoteller fra nettstedets katalog, og unngår fabrikkert informasjon.

5. **AI-Agent Samhandling**: Fordi NLWeb fungerer som en MCP-server, kunne en ekstern AI-reiseagent også koble seg til denne nettsteds NLWeb-instansen. AI-agenten kan da bruke `ask` MCP-metoden for å spørre nettstedet direkte: `ask("Er det noen veganske restauranter i Honolulu-området som hotellet anbefaler?")`. NLWeb-instansen vil prosessere dette, utnytte databasen med restaurantinformasjon (om lastet inn), og returnere et strukturert JSON-svar.

### Har du flere spørsmål om MCP/A2A/NLWeb?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta i kontortid og få svar på dine spørsmål om AI-agenter.

## Ressurser

- [MCP for nybegynnere](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentasjon](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->