# Bruke Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentic Protocols](../../../translated_images/no/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikk på bildet ovenfor for å se video av denne leksjonen)_

Etter hvert som bruken av AI-agenter øker, øker også behovet for protokoller som sikrer standardisering, sikkerhet og støtter åpen innovasjon. I denne leksjonen vil vi dekke 3 protokoller som søker å møte dette behovet - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduksjon

I denne leksjonen vil vi dekke:

• Hvordan **MCP** gjør det mulig for AI-agenter å få tilgang til eksterne verktøy og data for å fullføre brukeroppgaver.

• Hvordan **A2A** muliggjør kommunikasjon og samarbeid mellom forskjellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige språkgrensesnitt til enhver nettside som gjør at AI-agenter kan oppdage og samhandle med innholdet.

## Læringsmål

• **Identifisere** hovedformålet og fordelene med MCP, A2A og NLWeb i konteksten av AI-agenter.

• **Forklare** hvordan hver protokoll legger til rette for kommunikasjon og interaksjon mellom LLM-er, verktøy og andre agenter.

• **Gjenkjenne** de distinkte rollene hver protokoll spiller i byggingen av komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åpen standard som tilbyr en standardisert måte for applikasjoner å gi kontekst og verktøy til LLM-er. Dette muliggjør en "universell adapter" til ulike datakilder og verktøy som AI-agenter kan koble seg til på en konsistent måte.

La oss se på komponentene i MCP, fordelene sammenlignet med direkte API-bruk, og et eksempel på hvordan AI-agenter kan bruke en MCP-server.

### MCPs kjernekomponenter

MCP opererer med en **klient-tjener-arkitektur** og kjernekomponentene er:

• **Vertsprogrammer (Hosts)** er LLM-applikasjoner (for eksempel en kodeeditor som VSCode) som initierer forbindelsene til en MCP-server.

• **Klienter (Clients)** er komponenter innen vertsprogrammet som opprettholder en-til-en-forbindelser med servere.

• **Servere (Servers)** er lette programmer som eksponerer spesifikke kapasiteter.

Inkludert i protokollen er tre kjerneelementer som er kapabilitetene til en MCP-server:

• **Verktøy (Tools)**: Dette er diskrete handlinger eller funksjoner en AI-agent kan kalle for å utføre en handling. For eksempel kan en værmeldingstjeneste eksponere et "hent vær" verktøy, eller en e-handelsserver kan eksponere et "kjøp produkt" verktøy. MCP-servere annonserer hvert verktøys navn, beskrivelse og input/output-skjema i kapabilitetslisten.

• **Ressurser (Resources)**: Dette er skrivebeskyttede dataelementer eller dokumenter som en MCP-server kan tilby, og klienter kan hente dem på forespørsel. Eksempler inkluderer filinnhold, databaseposter eller loggfiler. Ressurser kan være tekst (som kode eller JSON) eller binære data (som bilder eller PDF-er).

• **Forespørsler (Prompts)**: Dette er forhåndsdefinerte maler som tilbyr foreslåtte forespørsler, noe som muliggjør mer komplekse arbeidsflyter.

### Fordeler med MCP

MCP tilbyr betydelige fordeler for AI-agenter:

• **Dynamisk oppdagelse av verktøy**: Agenter kan dynamisk motta en liste over tilgjengelige verktøy fra en server sammen med beskrivelser av hva de gjør. Dette står i kontrast til tradisjonelle API-er som ofte krever statisk koding for integrasjoner, noe som betyr at enhver API-endring krever kodeoppdateringer. MCP tilbyr en "integrere én gang"-tilnærming, noe som gir større tilpasningsevne.

• **Interoperabilitet på tvers av LLM-er**: MCP fungerer på tvers av forskjellige LLM-er, og gir fleksibilitet til å bytte kjernemodeller for å evaluere bedre ytelse.

• **Standardisert sikkerhet**: MCP inkluderer en standard autentiseringsmetode, noe som forbedrer skalerbarheten når man legger til tilgang til flere MCP-servere. Dette er enklere enn å håndtere forskjellige nøkler og autentiseringstyper for ulike tradisjonelle API-er.

### MCP-eksempel

![MCP Diagram](../../../translated_images/no/mcp-diagram.e4ca1cbd551444a1.webp)

Tenk deg at en bruker ønsker å bestille en flyreise ved hjelp av en AI-assistent drevet av MCP.

1. **Forbindelse**: AI-assistenten (MCP-klienten) kobler seg til en MCP-server levert av et flyselskap.

2. **Oppdagelse av verktøy**: Klienten spør flyselskapets MCP-server: "Hvilke verktøy har dere tilgjengelig?" Serveren svarer med verktøy som "søk etter fly" og "bestill fly".

3. **Verktøysutløsning**: Du ber så AI-assistenten: "Vennligst søk etter en flyreise fra Portland til Honolulu." AI-assistenten, ved bruk av sin LLM, identifiserer at den må kalle verktøyet "søk etter fly" og sender de relevante parametrene (avreisested, destinasjon) til MCP-serveren.

4. **Utførelse og respons**: MCP-serveren, som fungerer som en wrapper, foretar selve kallet til flyselskapets interne bookings-API. Den mottar deretter flyinformasjonen (f.eks. JSON-data) og sender den tilbake til AI-assistenten.

5. **Videre interaksjon**: AI-assistenten presenterer flyalternativene. Når du velger en flyreise, kan assistenten kalle verktøyet "bestill fly" på samme MCP-server for å fullføre bookingen.

## Agent-til-Agent Protokoll (A2A)

Mens MCP fokuserer på å koble LLM-er til verktøy, tar **Agent-til-Agent (A2A) protokollen** det et steg videre ved å muliggjøre kommunikasjon og samarbeid mellom forskjellige AI-agenter.  A2A kobler AI-agenter på tvers av ulike organisasjoner, miljøer og teknologistakker for å fullføre en delt oppgave.

Vi vil undersøke komponentene og fordelene med A2A, sammen med et eksempel på hvordan det kan anvendes i vår reiseapplikasjon.

### A2As kjernekomponenter

A2A fokuserer på å muliggjøre kommunikasjon mellom agenter og la dem samarbeide om å fullføre en underoppgave for brukeren. Hver komponent i protokollen bidrar til dette:

#### Agentkort

På samme måte som en MCP-server deler en liste over verktøy, har et Agentkort:
- Navnet på agenten.
- En **beskrivelse av de generelle oppgavene** den fullfører.
- En **liste over spesifikke ferdigheter** med beskrivelser for å hjelpe andre agenter (eller til og med menneskelige brukere) å forstå når og hvorfor de vil kalle på den agenten.
- Den **nåværende Endepunkt-URL-en** til agenten.
- **Versjonen** og **kapabilitetene** til agenten som for eksempel strømming av svar og push-varsler.

#### Agentutfører

Agentutføreren er ansvarlig for **å overføre konteksten fra brukersamtalen til den eksterne agenten**, den eksterne agenten trenger dette for å forstå oppgaven som skal utføres. I en A2A-server bruker en agent sin egen Store Språkmodell (LLM) for å tolke innkommende forespørsler og utføre oppgaver ved hjelp av egne interne verktøy.

#### Artefakt

Når en ekstern agent har fullført den forespurte oppgaven, blir arbeidsproduktet opprettet som et artefakt. Et artefakt **inneholder resultatet av agentens arbeid**, en **beskrivelse av hva som ble utført**, og **tekstkonteksten** som sendes gjennom protokollen. Etter at artefaktet er sendt, lukkes forbindelsen med den eksterne agenten til den trengs igjen.

#### Hendelseskø

Denne komponenten brukes til **håndtering av oppdateringer og overføring av meldinger**. Det er spesielt viktig i produksjon for agentiske systemer for å forhindre at forbindelsen mellom agenter lukkes før en oppgave er fullført, spesielt når oppgavefullføring kan ta lang tid.

### Fordeler med A2A

• **Forbedret samarbeid**: Det gjør det mulig for agenter fra forskjellige leverandører og plattformer å interagere, dele kontekst og arbeide sammen, noe som legger til rette for sømløs automatisering på tvers av tradisjonelt isolerte systemer.

• **Fleksibel modellvalg**: Hver A2A-agent kan bestemme hvilken LLM den bruker for å betjene sine forespørsler, noe som muliggjør optimaliserte eller finjusterte modeller per agent, i motsetning til enkel LLM-tilkobling i noen MCP-scenarier.

• **Innebygd autentisering**: Autentisering er integrert direkte i A2A-protokollen, noe som gir en robust sikkerhetsramme for agentinteraksjoner.

### A2A-eksempel

![A2A Diagram](../../../translated_images/no/A2A-Diagram.8666928d648acc26.webp)

La oss utvide vårt reisebestillingsscenario, men denne gangen bruke A2A.

1. **Brukerforespørsel til Multi-Agent**: En bruker interagerer med en "Reiseagent" A2A-klient/agent, kanskje ved å si, "Vennligst bestill en komplett tur til Honolulu for neste uke, inkludert fly, hotell og leiebil".

2. **Orkestrering av Reiseagenten**: Reiseagenten mottar denne komplekse forespørselen. Den bruker sin LLM for å resonnere om oppgaven og avgjør at den må samhandle med andre spesialiserte agenter.

3. **Inter-agent kommunikasjon**: Reiseagenten bruker deretter A2A-protokollen for å koble til nedstrøms agenter, for eksempel en "Flyselskapagent," en "Hotellagent," og en "Leiebilagent" som er opprettet av forskjellige selskaper.

4. **Delegert oppgaveutførelse**: Reiseagenten sender spesifikke oppgaver til disse spesialiserte agentene (f.eks. "Finn flyreiser til Honolulu," "Bestill et hotell," "Lei en bil"). Hver av disse spesialiserte agentene, som kjører sine egne LLM-er og bruker sine egne verktøy (som kan være MCP-servere selv), utfører sin spesifikke del av bookingen.

5. **Konsolidert svar**: Når alle nedstrømsagentene fullfører sine oppgaver, kompilere Reiseagenten resultatene (flydetaljer, hotellbekreftelse, leiebilbestilling) og sender et omfattende, chat-stil svar tilbake til brukeren.

## Natural Language Web (NLWeb)

Nettsider har lenge vært den primære måten for brukere å få tilgang til informasjon og data på internett.

La oss se på de ulike komponentene i NLWeb, fordelene med NLWeb og et eksempel på hvordan vår NLWeb virker ved å se på vår reiseapplikasjon.

### Komponenter i NLWeb

- **NLWeb-applikasjon (Kjernesoftware)**: Systemet som behandler naturlige språkspørsmål. Det kobler de ulike delene av plattformen sammen for å skape svar. Du kan tenke på det som **motoren som driver naturlige språkfunksjoner** på en nettside.

- **NLWeb-protokoll**: Dette er et **grunnleggende sett med regler for naturlig språklig interaksjon** med en nettside. Den sender svar tilbake i JSON-format (ofte ved bruk av Schema.org). Formålet er å skape et enkelt fundament for “AI-nettet,” på samme måte som HTML gjorde det mulig å dele dokumenter på nettet.

- **MCP-server (Model Context Protocol endepunkt)**: Hver NLWeb-oppsett fungerer også som en **MCP-server**. Det betyr at den kan **dele verktøy (som en “ask” metode) og data** med andre AI-systemer. I praksis gjør dette nettsidens innhold og muligheter tilgjengelig for AI-agenter, slik at siden blir en del av det bredere “agent-økosystemet.”

- **Embeddingsmodeller**: Disse modellene brukes til å **omdanne nettsideinnhold til numeriske representasjoner kalt vektorer** (embeddings). Disse vektorene fanger mening på en måte datamaskiner kan sammenligne og søke i. De lagres i en spesiell database, og brukere kan velge hvilken embedding-modell de ønsker å bruke.

- **Vektordatabaser (Hentemekanisme)**: Denne databasen **lagrer vektorene til nettsideinnholdet**. Når noen stiller et spørsmål, sjekker NLWeb vektordatabasen for raskt å finne den mest relevante informasjonen. Det gir en rask liste over mulige svar, rangert etter likhet. NLWeb fungerer med forskjellige vektorlagringssystemer som Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb ved eksempel

![NLWeb](../../../translated_images/no/nlweb-diagram.c1e2390b310e5fe4.webp)

Tenk på vår reisebestillingsside igjen, men denne gangen drevet av NLWeb.

1. **Dataimport**: Den eksisterende produktkatalogen på reisesiden (f.eks. flylister, hotellbeskrivelser, turopplegg) formateres ved hjelp av Schema.org eller lastes inn via RSS-feeder. NLWebs verktøy importerer disse strukturerte dataene, lager embeddings og lagrer dem i en lokal eller ekstern vektordatabasedatabase.

2. **Naturlig-språk-spørring (Menneske)**: En bruker besøker nettsiden og i stedet for å navigere i menyer skriver i et chattegrensesnitt: "Finn meg et familievennlig hotell i Honolulu med basseng for neste uke."

3. **NLWeb-behandling**: NLWeb-applikasjonen mottar denne forespørselen. Den sender forespørselen til en LLM for forståelse og søker samtidig i sin vektordatabasen etter relevante hotelltilbud.

4. **Nøyaktige resultater**: LLM-en hjelper med å tolke søkeresultatene fra databasen, identifisere de beste treffene basert på kriteriene "familievennlig," "basseng," og "Honolulu," og formaterer deretter et naturlig språk-svar. Viktigst av alt, svaret refererer til faktiske hoteller fra nettsidens katalog og unngår oppdiktet informasjon.

5. **AI-agent-interaksjon**: Fordi NLWeb fungerer som en MCP-server, kan en ekstern AI-reiseagent også koble seg til denne nettsidens NLWeb-instans. AI-agenten kan da bruke MCP-metoden `ask` for å spørre nettsiden direkte: `ask("Er det noen veganvennlige restauranter i Honolulu-området anbefalt av hotellet?")`. NLWeb-instansen vil behandle dette, bruke sin database med restaurantinformasjon (hvis lastet inn), og returnere et strukturert JSON-svar.

### Har du flere spørsmål om MCP/A2A/NLWeb?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre elever, delta på kontortimer og få besvart dine spørsmål om AI-agenter.

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