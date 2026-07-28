# Bruke agentprotokoller (MCP, A2A og NLWeb)

[![Agentic Protocols](../../../translated_images/no/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikk på bildet over for å se video av denne leksjonen)_

Etter hvert som bruken av AI-agenter øker, øker også behovet for protokoller som sikrer standardisering, sikkerhet og støtter åpen innovasjon. I denne leksjonen vil vi dekke 3 protokoller som tar sikte på å møte dette behovet - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduksjon

I denne leksjonen vil vi dekke:

• Hvordan **MCP** lar AI-agenter få tilgang til eksterne verktøy og data for å utføre brukeroppgaver.

• Hvordan **A2A** muliggjør kommunikasjon og samarbeid mellom forskjellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige språkgrensesnitt til enhver nettside, slik at AI-agenter kan oppdage og interagere med innholdet.

## Læringsmål

• **Identifisere** kjerneformålet og fordelene med MCP, A2A og NLWeb i konteksten av AI-agenter.

• **Forklare** hvordan hver protokoll legger til rette for kommunikasjon og interaksjon mellom LLM-er, verktøy og andre agenter.

• **Gjenkjenne** de distinkte rollene hver protokoll spiller i bygging av komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åpen standard som gir en standardisert måte for applikasjoner å gi kontekst og verktøy til LLM-er. Dette muliggjør en "universell adapter" til forskjellige datakilder og verktøy som AI-agenter kan koble seg til på en konsekvent måte.

La oss se på komponentene i MCP, fordelene sammenlignet med direkte API-bruk og et eksempel på hvordan AI-agenter kan bruke en MCP-server.

### MCPs kjernekomponenter

MCP opererer på en **klient-server-arkitektur**, og kjernekomponentene er:

• **Hosts** er LLM-applikasjoner (for eksempel en kodeeditor som VSCode) som starter tilkoblingene til en MCP-server.

• **Clients** er komponenter innenfor host-applikasjonen som opprettholder en-til-en-tilkoblinger med servere.

• **Servers** er lettvektsprogrammer som eksponerer spesifikke funksjoner.

Inkludert i protokollen er tre kjerneelementer som er funksjonene til en MCP-server:

• **Verktøy**: Disse er diskrete handlinger eller funksjoner en AI-agent kan kalle for å utføre en handling. For eksempel kan en værtjeneste eksponere et "hent vær"-verktøy, eller en e-handelsserver kan tilby et "kjøp produkt"-verktøy. MCP-servere annonserer hvert verktøys navn, beskrivelse og input/output-skjema i sine funksjonsoppføringer.

• **Ressurser**: Dette er lese-only dataelementer eller dokumenter som en MCP-server kan tilby, og klienter kan hente dem ved behov. Eksempler inkluderer filinnhold, databaseregistre eller loggfiler. Ressursene kan være tekst (som kode eller JSON) eller binære (som bilder eller PDF-er).

• **Prompter**: Dette er forhåndsdefinerte maler som gir foreslåtte prompter, som gjør det mulig med mer komplekse arbeidsflyter.

### Fordeler med MCP

MCP tilbyr betydelige fordeler for AI-agenter:

• **Dynamisk verktøyoppdagelse**: Agenter kan dynamisk motta en liste over tilgjengelige verktøy fra en server sammen med beskrivelser av hva de gjør. Dette står i kontrast til tradisjonelle API-er som ofte krever statisk koding for integrasjoner, noe som betyr at enhver endring i API krever kodeoppdateringer. MCP tilbyr en "integrer én gang"-tilnærming som fører til større tilpasningsdyktighet.

• **Interoperabilitet på tvers av LLM-er**: MCP fungerer på tvers av forskjellige LLM-er, og gir fleksibilitet til å bytte kjernemodeller for å vurdere bedre ytelse.

• **Standardisert sikkerhet**: MCP inkluderer en standard autentiseringsmetode, noe som forbedrer skalerbarheten når man legger til tilgang til flere MCP-servere. Dette er enklere enn å håndtere forskjellige nøkler og autentiseringstyper for ulike tradisjonelle API-er.

### MCP-eksempel

![MCP Diagram](../../../translated_images/no/mcp-diagram.e4ca1cbd551444a1.webp)

Tenk deg at en bruker ønsker å bestille en flyreise ved hjelp av en AI-assistent som drives av MCP.

1. **Tilkobling**: AI-assistenten (MCP-klienten) kobler seg til en MCP-server levert av et flyselskap.

2. **Verktøyoppdagelse**: Klienten spør flyselskapets MCP-server: "Hvilke verktøy har dere tilgjengelig?" Serveren svarer med verktøy som "søk flyreiser" og "bestill flyreiser".

3. **Verktøypåkalling**: Du ber deretter AI-assistenten: "Vennligst søk etter en flyreise fra Portland til Honolulu." AI-assistenten, ved hjelp av sin LLM, identifiserer at den må kalle på "søk flyreiser"-verktøyet og sender de relevante parametrene (avreisested, destinasjon) til MCP-serveren.

4. **Utførelse og svar**: MCP-serveren, som fungerer som en omslagspakke, gjør det faktiske kallet til flyselskapets interne bestillings-API. Den mottar deretter flyinformasjonen (f.eks. JSON-data) og sender den tilbake til AI-assistenten.

5. **Videre interaksjon**: AI-assistenten presenterer flyvalgene. Når du har valgt en flyreise, kan assistenten påkalle "bestill flyreise"-verktøyet på samme MCP-server og fullføre bestillingen.

## Agent-til-Agent Protokoll (A2A)

Mens MCP fokuserer på å koble LLM-er til verktøy, tar **Agent-til-Agent (A2A)-protokollen** det et steg videre ved å muliggjøre kommunikasjon og samarbeid mellom forskjellige AI-agenter. A2A kobler AI-agenter på tvers av forskjellige organisasjoner, miljøer og teknologistakker for å utføre en delt oppgave.

Vi skal se på komponentene og fordelene ved A2A, sammen med et eksempel på hvordan det kan anvendes i vår reiseapplikasjon.

### A2As kjernekomponenter

A2A fokuserer på å muliggjøre kommunikasjon mellom agenter og få dem til å arbeide sammen for å fullføre en deloppgave for brukeren. Hver komponent i protokollen bidrar til dette:

#### Agentkort

På samme måte som en MCP-server deler en liste over verktøy, har et Agentkort:
- Navnet til agenten.
- En **beskrivelse av de generelle oppgavene** den utfører.
- En **liste over spesifikke ferdigheter** med beskrivelser som hjelper andre agenter (eller til og med menneskelige brukere) å forstå når og hvorfor de vil kalle på den agenten.
- Den **nåværende Endepunkt-URL-en** til agenten
- Agentens **versjon** og **funksjoner** som strømming av svar og push-varsler.

#### Agentutfører

Agentutføreren er ansvarlig for å **overføre konteksten av brukerchatten til den eksterne agenten**; den eksterne agenten trenger dette for å forstå oppgaven som skal fullføres. I en A2A-server bruker en agent sin egen store språkmodell (LLM) for å analysere innkommende forespørsler og utføre oppgaver ved hjelp av sine egne interne verktøy.

#### Artefakt

Når en ekstern agent har fullført den forespurte oppgaven, blir produktet av arbeidet opprettet som et artefakt. Et artefakt **inneholder resultatet av agentens arbeid**, en **beskrivelse av hva som ble fullført**, og **tekstkonteksten** som sendes gjennom protokollen. Etter at artefakten er sendt, lukkes forbindelsen med den eksterne agenten til den trengs igjen.

#### Hendelseskø

Denne komponenten brukes for **håndtering av oppdateringer og overføring av meldinger**. Den er spesielt viktig i produksjon for agentiske systemer for å forhindre at forbindelsen mellom agenter lukkes før en oppgave er fullført, spesielt når oppgavefullføringstider kan ta lengre tid.

### Fordeler med A2A

• **Forbedret samarbeid**: Den gjør det mulig for agenter fra forskjellige leverandører og plattformer å samhandle, dele kontekst og samarbeide, og legger til rette for sømløs automatisering på tvers av tradisjonelt atskilte systemer.

• **Fleksibilitet i modellvalg**: Hver A2A-agent kan bestemme hvilken LLM den bruker for å betjene sine forespørsler, noe som tillater optimaliserte eller finjusterte modeller per agent, i motsetning til en enkelt LLM-tilkobling i enkelte MCP-scenarier.

• **Innebygd autentisering**: Autentisering er integrert direkte i A2A-protokollen, og gir en robust sikkerhetsramme for agentinteraksjoner.

### A2A-eksempel

![A2A Diagram](../../../translated_images/no/A2A-Diagram.8666928d648acc26.webp)

La oss utvide vårt scenarios for reisebestilling, men denne gangen bruker vi A2A.

1. **Brukerforespørsel til multi-agent**: En bruker interagerer med en "Reiseagent" A2A-klient/agent, kanskje ved å si: "Vennligst bestill en hel tur til Honolulu for neste uke, inkludert fly, hotell og leiebil".

2. **Orkestrering av Reiseagenten**: Reiseagenten mottar denne komplekse forespørselen. Den bruker sin LLM til å resonnere om oppgaven og avgjøre at den må samhandle med andre spesialiserte agenter.

3. **Inter-agent kommunikasjon**: Reiseagenten bruker deretter A2A-protokollen til å koble seg til underordnede agenter, som en "Flyselskap Agent", en "Hotell Agent" og en "Leiebil Agent" som er opprettet av forskjellige selskaper.

4. **Delegert oppgaveutførelse**: Reiseagenten sender spesifikke oppgaver til disse spesialiserte agentene (f.eks. "Finn flyreiser til Honolulu", "Bestill hotell", "Lei bil"). Hver av disse spesialiserte agentene, som kjører sine egne LLM-er og bruker sine egne verktøy (som selv kan være MCP-servere), utfører sin spesifikke del av bestillingen.

5. **Konsolidert svar**: Når alle underordnede agenter har fullført sine oppgaver, samler Reiseagenten resultatene (flydetaljer, hotellbekreftelse, leiebilbestilling) og sender et omfattende, chat-lignende svar tilbake til brukeren.

## Natural Language Web (NLWeb)

Nettsider har lenge vært hovedmetoden for brukere å få tilgang til informasjon og data på internett.

La oss se på de forskjellige komponentene i NLWeb, fordelene med NLWeb og et eksempel på hvordan vår NLWeb fungerer ved å se på vår reiseapplikasjon.

### Komponenter i NLWeb

- **NLWeb-applikasjon (kjerne servicemotor)**: Systemet som behandler naturlige språkspørsmål. Det kobler sammen de ulike delene av plattformen for å lage svar. Du kan tenke på det som **motoren som driver naturlige språkfunksjoner** på en nettside.

- **NLWeb-protokoll**: Dette er et **grunnleggende sett med regler for naturlig språkinteraksjon** med en nettside. Den sender tilbake svar i JSON-format (ofte med Schema.org). Formålet er å lage et enkelt grunnlag for "AI-nettet", på samme måte som HTML gjorde det mulig å dele dokumenter på nett.

- **MCP-server (Model Context Protocol Endepunkt)**: Hver NLWeb-oppsett fungerer også som en **MCP-server**. Dette betyr at den kan **dele verktøy (som en "ask"-metode) og data** med andre AI-systemer. I praksis gjør dette nettsidens innhold og evner brukbare for AI-agenter, og lar siden bli en del av det bredere "agentøkosystemet".

- **Embeddingsmodeller**: Disse modellene brukes til å **konvertere nettsideinnhold til numeriske representasjoner kalt vektorer** (embeddings). Disse vektorene fanger betydning på en måte som datamaskiner kan sammenligne og søke i. De lagres i en spesiell database, og brukere kan velge hvilken embeddingsmodell de ønsker å bruke.

- **Vektordatabase (gjenfinningsmekanisme)**: Denne databasen **lagrer embeddings av nettsideinnholdet**. Når noen stiller et spørsmål, sjekker NLWeb vektordatabasen for raskt å finne den mest relevante informasjonen. Den gir en rask liste over mulige svar rangert etter likhet. NLWeb fungerer med forskjellige vektorlager-systemer som Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb som eksempel

![NLWeb](../../../translated_images/no/nlweb-diagram.c1e2390b310e5fe4.webp)

Tenk på vår nettside for reisebestilling igjen, men denne gangen drevet av NLWeb.

1. **Datainnsamling**: Reise-nettstedets eksisterende produktkataloger (f.eks. flyoppføringer, hotellbeskrivelser, turpakker) formateres med Schema.org eller lastes inn via RSS-feeder. NLWebs verktøy inntar disse strukturerte dataene, lager embeddings og lagrer dem i en lokal eller ekstern vektordatabase.

2. **Spørsmål i naturlig språk (menneske)**: En bruker besøker nettsiden og, i stedet for å navigere i menyer, skriver inn i et chattegrensesnitt: "Finn et barnevennlig hotell i Honolulu med basseng for neste uke".

3. **NLWeb-behandling**: NLWeb-applikasjonen mottar denne forespørselen. Den sender forespørselen til en LLM for forståelse og søker samtidig i sin vektordatabase etter relevante hotelloppføringer.

4. **Nøyaktige resultater**: LLM-en hjelper til med å tolke søkeresultatene fra databasen, identifisere de beste treffene basert på kriteriene "barnevennlig," "basseng," og "Honolulu," og formaterer deretter et svar på naturlig språk. Viktig er at svaret refererer til faktiske hoteller fra nettsidens katalog, og unngår oppdiktet informasjon.

5. **AI-agentinteraksjon**: Fordi NLWeb fungerer som en MCP-server, kan en ekstern AI-reiseagent også koble seg til denne nettsidens NLWeb-instans. AI-agenten kan da bruke `ask` MCP-metoden for å spørre nettsiden direkte: `ask("Er det noen veganske restauranter i Honolulu-området anbefalt av hotellet?")`. NLWeb-instansen vil behandle dette, med bruk av sin database over restaurantinformasjon (hvis lastet inn), og returnere et strukturert JSON-svar.

### Flere spørsmål om MCP/A2A/NLWeb?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortimer og få svar på dine spørsmål om AI-agenter.

## Ressurser

- [MCP for nybegynnere](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentasjon](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Forrige leksjon

[AI-agenter i produksjon](../10-ai-agents-production/README.md)

## Neste leksjon

[Kontekstengineering for AI-agenter](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->