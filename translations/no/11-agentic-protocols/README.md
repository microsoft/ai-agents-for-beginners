# Bruke Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentic Protocols](../../../translated_images/no/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikk på bildet over for å se video av denne leksjonen)_

Etter hvert som bruken av AI-agenter vokser, øker også behovet for protokoller som sikrer standardisering, sikkerhet og støtter åpen innovasjon. I denne leksjonen vil vi dekke 3 protokoller som søker å møte dette behovet - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduksjon

I denne leksjonen vil vi dekke:

• Hvordan **MCP** lar AI-agenter få tilgang til eksterne verktøy og data for å fullføre brukeres oppgaver.

• Hvordan **A2A** muliggjør kommunikasjon og samarbeid mellom forskjellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige språkgrensesnitt til ethvert nettsted og gjør det mulig for AI-agenter å oppdage og samhandle med innholdet.

## Læringsmål

• **Identifisere** hovedformålet og fordelene med MCP, A2A og NLWeb i konteksten av AI-agenter.

• **Forklare** hvordan hver protokoll muliggjør kommunikasjon og interaksjon mellom LLMs, verktøy og andre agenter.

• **Gjenkjenne** de distinkte rollene hver protokoll spiller i bygging av komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åpen standard som gir en standardisert måte for applikasjoner å tilby kontekst og verktøy til LLMs. Dette muliggjør en "universal adapter" til forskjellige datakilder og verktøy som AI-agenter kan koble seg til på en konsistent måte.

La oss se på komponentene i MCP, fordelene sammenlignet med direkte API-bruk, og et eksempel på hvordan AI-agenter kan bruke en MCP-server.

### MCP-kjernekomponenter

MCP opererer på en **klient-server-arkitektur** og kjernekomponentene er:

• **Verter** er LLM-applikasjoner (for eksempel en kodeeditor som VSCode) som starter forbindelsene til en MCP-server.

• **Klienter** er komponenter innen vertsapplikasjonen som opprettholder en-til-en forbindelser med servere.

• **Servere** er lette programmer som eksponerer spesifikke kapasiteter.

Inkludert i protokollen er tre kjerneprimitiver som er kapabilitetene til en MCP-server:

• **Verktøy**: Dette er diskrete handlinger eller funksjoner en AI-agent kan kalle for å utføre en handling. For eksempel kan en værtjeneste eksponere et verktøy kalt "hent vær", eller en e-handelsserver kan eksponere et verktøy kalt "kjøp produkt". MCP-servere annonserer hvert verktøys navn, beskrivelse, og input/output-skjema i sine kapabilitetslister.

• **Ressurser**: Dette er lesbare dataelementer eller dokumenter som en MCP-server kan tilby, og klienter kan hente dem på forespørsel. Eksempler inkluderer filinnhold, databaseoppføringer eller loggfiler. Ressurser kan være tekst (som kode eller JSON) eller binær (som bilder eller PDFer).

• **Prompter**: Dette er forhåndsdefinerte maler som gir foreslåtte prompter, og tillater mer komplekse arbeidsflyter.

### Fordeler med MCP

MCP tilbyr betydelige fordeler for AI-agenter:

• **Dynamisk verktøyoppdagelse**: Agenter kan dynamisk motta en liste over tilgjengelige verktøy fra en server sammen med beskrivelser av hva de gjør. Dette står i kontrast til tradisjonelle API-er, som ofte krever statisk koding for integrasjoner, noe som betyr at enhver API-endring krever kodeoppdateringer. MCP tilbyr en "integrer én gang"-tilnærming, noe som gir større tilpasningsevne.

• **Interoperabilitet på tvers av LLMs**: MCP fungerer på tvers av forskjellige LLMs, og gir fleksibilitet til å bytte hovedmodeller for å evaluere bedre ytelse.

• **Standardisert sikkerhet**: MCP inkluderer en standard autentiseringsmetode, som forbedrer skalerbarhet ved å legge til tilgang til flere MCP-servere. Dette er enklere enn å håndtere forskjellige nøkler og autentiseringstyper for ulike tradisjonelle API-er.

### MCP-eksempel

![MCP Diagram](../../../translated_images/no/mcp-diagram.e4ca1cbd551444a1.webp)

Tenk deg at en bruker ønsker å bestille en flyreise ved hjelp av en AI-assistent drevet av MCP.

1. **Tilkobling**: AI-assistenten (MCP-klienten) kobler til en MCP-server levert av et flyselskap.

2. **Verktøyoppdagelse**: Klienten spør flyselskapets MCP-server: "Hvilke verktøy har dere tilgjengelig?" Serveren svarer med verktøy som "søk fly" og "bestill fly".

3. **Verktøykalling**: Du ber AI-assistenten: "Vennligst søk etter en flyreise fra Portland til Honolulu." AI-assistenten, ved hjelp av sin LLM, identifiserer at den må kalle "søk fly"-verktøyet og sender relevante parametere (avreisested, destinasjon) til MCP-serveren.

4. **Utførelse og svar**: MCP-serveren, som fungerer som en wrapper, foretar selve anropet til flyselskapets interne bestillings-API. Den mottar deretter flyinformasjonen (f.eks. JSON-data) og sender den tilbake til AI-assistenten.

5. **Videre interaksjon**: AI-assistenten presenterer flyalternativene. Når du velger en flyreise, kan assistenten kalle "bestill fly"-verktøyet på samme MCP-server og fullføre bestillingen.

## Agent-til-Agent Protokoll (A2A)

Mens MCP fokuserer på å koble LLMs til verktøy, tar **Agent-til-Agent (A2A) protokollen** det et steg videre ved å muliggjøre kommunikasjon og samarbeid mellom forskjellige AI-agenter. A2A kobler AI-agenter på tvers av organisasjoner, miljøer og teknologistakker for å fullføre en felles oppgave.

Vi skal undersøke komponentene og fordelene med A2A, sammen med et eksempel på hvordan det kan brukes i vår reiseapplikasjon.

### A2A kjernekomponenter

A2A fokuserer på å muliggjøre kommunikasjon mellom agenter og få dem til å samarbeide for å fullføre en underoppgave for brukeren. Hver komponent av protokollen bidrar til dette:

#### Agentkort

På samme måte som en MCP-server deler en liste over verktøy, har et Agentkort:
- Navnet på agenten.
- En **beskrivelse av de generelle oppgavene** den fullfører.
- En **liste over spesifikke ferdigheter** med beskrivelser for å hjelpe andre agenter (eller til og med menneskelige brukere) å forstå når og hvorfor de vil ringe til den agenten.
- Den **gjeldende endepunkt-URL-en** til agenten
- **Versjonen** og **kapasiteter** til agenten, som streaming-responser og push-varsler.

#### Agentutfører

Agentutføreren er ansvarlig for **å sende konteksten av brukerchatten til den eksterne agenten**, den eksterne agenten trenger dette for å forstå oppgaven som skal fullføres. I en A2A-server bruker en agent sin egen store språkmodell (LLM) for å tolke innkommende forespørsler og utføre oppgaver ved hjelp av sine interne verktøy.

#### Artefakt

Når en ekstern agent har fullført den forespurte oppgaven, opprettes produktet av arbeidet som et artefakt. Et artefakt **inneholder resultatet av agentens arbeid**, en **beskrivelse av hva som ble fullført**, og **tekstkonteksten** som sendes gjennom protokollen. Etter at artefakten er sendt, lukkes forbindelsen med den eksterne agenten til den trengs igjen.

#### Hendelseskø

Denne komponenten brukes for **å håndtere oppdateringer og sende meldinger**. Den er spesielt viktig i produksjon for agentiske systemer for å forhindre at forbindelsen mellom agenter lukkes før en oppgave er fullført, spesielt når oppgavens fullføring kan ta lengre tid.

### Fordeler med A2A

• **Forbedret samarbeid**: Den gjør det mulig for agenter fra forskjellige leverandører og plattformer å samhandle, dele kontekst og samarbeide, noe som muliggjør sømløs automatisering på tvers av tradisjonelt frakoblede systemer.

• **Fleksibel modellvalg**: Hver A2A-agent kan bestemme hvilken LLM den bruker for å betjene sine forespørsler, noe som tillater optimaliserte eller finjusterte modeller per agent, i motsetning til en enkelt LLM-tilkobling i noen MCP-scenarier.

• **Innbygget autentisering**: Autentisering er integrert direkte i A2A-protokollen, og gir et robust sikkerhetsrammeverk for agentinteraksjoner.

### A2A-eksempel

![A2A Diagram](../../../translated_images/no/A2A-Diagram.8666928d648acc26.webp)

La oss utvide vårt reisebestillingsscenario, men denne gangen bruker vi A2A.

1. **Brukerforespørsel til Multi-Agent**: En bruker interagerer med en "Reiseagent" A2A-klient/agent, kanskje ved å si, "Vennligst bestill en hel tur til Honolulu neste uke, inkludert fly, hotell og leiebil".

2. **Orkestrering av Reiseagent**: Reiseagenten mottar denne komplekse forespørselen. Den bruker sin LLM til å resonnere rundt oppgaven og avgjør at den må interagere med andre spesialiserte agenter.

3. **Kommunikasjon mellom agenter**: Reiseagenten bruker deretter A2A-protokollen for å koble til nedstrøms agenter, som en "Flyselskapagent," en "Hotellagent" og en "Leiebilagent" som er opprettet av forskjellige selskaper.

4. **Delegert oppgaveutførelse**: Reiseagenten sender spesifikke oppgaver til disse spesialiserte agentene (f.eks. "Finn fly til Honolulu," "Bestill hotell," "Leie bil"). Hver av disse spesialiserte agentene, som kjører sine egne LLMs og bruker sine egne verktøy (som kan være MCP-servere), utfører sin spesifikke del av bestillingen.

5. **Konsolidert respons**: Når alle nedstrøms agentene er ferdige med sine oppgaver, samler Reiseagenten resultatene (flydetaljer, hotellbekreftelse, leiebilbestilling) og sender et omfattende, chat-lignende svar tilbake til brukeren.

## Natural Language Web (NLWeb)

Nettsteder har lenge vært hovedmåten for brukere å få tilgang til informasjon og data på internett.

La oss se på de ulike komponentene i NLWeb, fordelene med NLWeb og et eksempel på hvordan vårt NLWeb fungerer ved å se på vår reiseapplikasjon.

### Komponenter i NLWeb

- **NLWeb-applikasjon (kjerne tjenestekode)**: Systemet som behandler spørsmål på naturlig språk. Det kobler sammen de ulike delene av plattformen for å skape svar. Du kan tenke på det som **motoren som driver de naturlige språkfunksjonene** til en nettside.

- **NLWeb-protokoll**: Dette er et **grunnleggende sett med regler for naturlig språksinteraksjon** med et nettsted. Den sender tilbake svar i JSON-format (ofte ved bruk av Schema.org). Hensikten er å skape et enkelt fundament for “AI-nettet,” på samme måte som HTML gjorde det mulig å dele dokumenter online.

- **MCP-server (Model Context Protocol-endepunkt)**: Hver NLWeb-oppsett fungerer også som en **MCP-server**. Det betyr at den kan **dele verktøy (som en “ask”-metode) og data** med andre AI-systemer. I praksis gjør dette nettstedets innhold og evner brukbare for AI-agenter, slik at siden blir en del av det bredere "agent-økosystemet".

- **Innebyggingsmodeller**: Disse modellene brukes til å **konvertere nettstedets innhold til numeriske representasjoner kalt vektorer** (innebygginger). Disse vektorene fanger mening på en måte som datamaskiner kan sammenligne og søke i. De lagres i en spesiell database, og brukere kan velge hvilken innebyggingsmodell de vil bruke.

- **Vektordatabase (oppslagsmekanisme)**: Denne databasen **lagrer innebyggingene av nettstedets innhold**. Når noen stiller et spørsmål, sjekker NLWeb vektordatabasen for raskt å finne den mest relevante informasjonen. Den gir en rask liste med mulige svar, rangert etter likhet. NLWeb fungerer med forskjellige vektorlager systemer som Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb ved eksempel

![NLWeb](../../../translated_images/no/nlweb-diagram.c1e2390b310e5fe4.webp)

Tenk igjen på vårt reisebestillingsnettsted, men denne gangen er det drevet av NLWeb.

1. **Dataopptak**: Reise-nettstedets eksisterende produktkataloger (f.eks. flyoppføringer, hotellbeskrivelser, turpakker) formateres ved bruk av Schema.org eller lastes inn via RSS-feeder. NLWebs verktøy behandler disse strukturerte dataene, lager innebygginger og lagrer dem i en lokal eller fjern vektordatabase.

2. **Naturlig språkspørring (menneske)**: En bruker besøker nettstedet og, i stedet for å navigere i menyer, skriver inn i et chattergrensesnitt: "Finn meg et familievennlig hotell i Honolulu med basseng for neste uke".

3. **NLWeb-behandling**: NLWeb-applikasjonen mottar denne forespørselen. Den sender spørringen til en LLM for forståelse og søker samtidig i sin vektordatabase etter relevante hotelloppføringer.

4. **Nøyaktige resultater**: LLM hjelper til med å tolke søkeresultatene fra databasen, identifisere de beste treffene basert på kriteriene "familievennlig," "basseng," og "Honolulu," og formaterer så et svar på naturlig språk. Viktigst er at svaret refererer til faktiske hoteller fra nettstedets katalog, og unngår oppdiktet informasjon.

5. **AI-agentinteraksjon**: Fordi NLWeb fungerer som en MCP-server, kan en ekstern AI-reiseagent også koble seg til dette nettstedets NLWeb-instans. AI-agenten kan så bruke MCP-metoden `ask` for å spørre nettstedet direkte: `ask("Finnes det noen veganvennlige restauranter i Honolulu-området anbefalt av hotellet?")`. NLWeb-instansen vil behandle dette, bruke sin database over restaurantinformasjon (om den er lastet inn), og returnere et strukturert JSON-svar.

### Har du flere spørsmål om MCP/A2A/NLWeb?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortimer og få svar på dine spørsmål om AI-agenter.

## Ressurser

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Forrige Leksjon

[AI-agenter i produksjon](../10-ai-agents-production/README.md)

## Neste Leksjon

[Context Engineering for AI Agents](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->