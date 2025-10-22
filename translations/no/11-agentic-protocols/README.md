<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:06:29+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "no"
}
-->
# Bruk av Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentiske Protokoller](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.no.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikk på bildet over for å se videoen til denne leksjonen)_

Etter hvert som bruken av AI-agenter øker, vokser også behovet for protokoller som sikrer standardisering, sikkerhet og støtter åpen innovasjon. I denne leksjonen skal vi dekke tre protokoller som tar sikte på å møte dette behovet - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduksjon

I denne leksjonen skal vi dekke:

• Hvordan **MCP** lar AI-agenter få tilgang til eksterne verktøy og data for å utføre brukeroppgaver.

• Hvordan **A2A** muliggjør kommunikasjon og samarbeid mellom ulike AI-agenter.

• Hvordan **NLWeb** bringer naturlige språkgrensesnitt til enhver nettside, slik at AI-agenter kan oppdage og interagere med innholdet.

## Læringsmål

• **Identifisere** hovedformålet og fordelene med MCP, A2A og NLWeb i konteksten av AI-agenter.

• **Forklare** hvordan hver protokoll legger til rette for kommunikasjon og interaksjon mellom LLM-er, verktøy og andre agenter.

• **Gjenkjenne** de ulike rollene hver protokoll spiller i byggingen av komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åpen standard som gir en standardisert måte for applikasjoner å tilby kontekst og verktøy til LLM-er. Dette muliggjør en "universell adapter" til ulike datakilder og verktøy som AI-agenter kan koble seg til på en konsistent måte.

La oss se på komponentene i MCP, fordelene sammenlignet med direkte API-bruk, og et eksempel på hvordan AI-agenter kan bruke en MCP-server.

### MCP Kjernekomponenter

MCP opererer på en **klient-server-arkitektur**, og kjernekomponentene er:

• **Vertsapplikasjoner** er LLM-applikasjoner (for eksempel en kodeeditor som VSCode) som starter tilkoblinger til en MCP-server.

• **Klienter** er komponenter innenfor vertsapplikasjonen som opprettholder én-til-én-tilkoblinger med servere.

• **Servere** er lette programmer som tilbyr spesifikke funksjoner.

Protokollen inkluderer tre kjerneprimitiver som representerer MCP-serverens funksjoner:

• **Verktøy**: Dette er diskrete handlinger eller funksjoner en AI-agent kan bruke for å utføre en oppgave. For eksempel kan en vær-tjeneste tilby et "hent vær"-verktøy, eller en e-handelsserver kan tilby et "kjøp produkt"-verktøy. MCP-servere annonserer hvert verktøys navn, beskrivelse og input/output-skjema i sin funksjonsliste.

• **Ressurser**: Dette er skrivebeskyttede dataelementer eller dokumenter som en MCP-server kan tilby, og klienter kan hente dem ved behov. Eksempler inkluderer filinnhold, databaseposter eller loggfiler. Ressurser kan være tekst (som kode eller JSON) eller binære (som bilder eller PDF-er).

• **Prompter**: Dette er forhåndsdefinerte maler som gir foreslåtte prompter, og muliggjør mer komplekse arbeidsflyter.

### Fordeler med MCP

MCP gir betydelige fordeler for AI-agenter:

• **Dynamisk verktøyoppdagelse**: Agenter kan dynamisk motta en liste over tilgjengelige verktøy fra en server sammen med beskrivelser av hva de gjør. Dette står i kontrast til tradisjonelle API-er, som ofte krever statisk koding for integrasjoner, noe som betyr at enhver API-endring krever kodeoppdateringer. MCP tilbyr en "integrer én gang"-tilnærming, som gir større fleksibilitet.

• **Interoperabilitet på tvers av LLM-er**: MCP fungerer på tvers av ulike LLM-er, og gir fleksibilitet til å bytte kjerne-modeller for å evaluere bedre ytelse.

• **Standardisert sikkerhet**: MCP inkluderer en standard autentiseringsmetode, som forbedrer skalerbarheten når man legger til tilgang til flere MCP-servere. Dette er enklere enn å administrere ulike nøkler og autentiseringstyper for forskjellige tradisjonelle API-er.

### MCP Eksempel

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.no.png)

Tenk deg at en bruker ønsker å bestille en flyreise ved hjelp av en AI-assistent drevet av MCP.

1. **Tilkobling**: AI-assistenten (MCP-klienten) kobler seg til en MCP-server levert av et flyselskap.

2. **Verktøyoppdagelse**: Klienten spør flyselskapets MCP-server, "Hvilke verktøy har dere tilgjengelig?" Serveren svarer med verktøy som "søk flyreiser" og "bestill flyreiser".

3. **Verktøybruk**: Du ber AI-assistenten, "Vennligst søk etter en flyreise fra Portland til Honolulu." AI-assistenten, ved hjelp av sin LLM, identifiserer at den må bruke "søk flyreiser"-verktøyet og sender de relevante parameterne (opprinnelse, destinasjon) til MCP-serveren.

4. **Utførelse og respons**: MCP-serveren, som fungerer som en innpakning, gjør det faktiske kallet til flyselskapets interne booking-API. Den mottar deretter flyinformasjonen (f.eks. JSON-data) og sender den tilbake til AI-assistenten.

5. **Videre interaksjon**: AI-assistenten presenterer flyalternativene. Når du velger en flyreise, kan assistenten bruke "bestill flyreise"-verktøyet på samme MCP-server for å fullføre bestillingen.

## Agent-til-Agent Protokoll (A2A)

Mens MCP fokuserer på å koble LLM-er til verktøy, tar **Agent-til-Agent (A2A) protokollen** det et steg videre ved å muliggjøre kommunikasjon og samarbeid mellom ulike AI-agenter. A2A kobler AI-agenter på tvers av ulike organisasjoner, miljøer og teknologiske plattformer for å fullføre en delt oppgave.

Vi skal undersøke komponentene og fordelene med A2A, sammen med et eksempel på hvordan det kan brukes i vår reiseapplikasjon.

### A2A Kjernekomponenter

A2A fokuserer på å muliggjøre kommunikasjon mellom agenter og få dem til å samarbeide om å fullføre en deloppgave for brukeren. Hver komponent i protokollen bidrar til dette:

#### Agentkort

På samme måte som en MCP-server deler en liste over verktøy, har et agentkort:
- Navnet på agenten.
- En **beskrivelse av de generelle oppgavene** den utfører.
- En **liste over spesifikke ferdigheter** med beskrivelser for å hjelpe andre agenter (eller til og med menneskelige brukere) med å forstå når og hvorfor de vil bruke denne agenten.
- Den **nåværende Endpoint-URL-en** til agenten.
- **Versjonen** og **funksjonene** til agenten, som streaming-responser og push-varsler.

#### Agentutfører

Agentutføreren er ansvarlig for **å sende konteksten til brukerens chat til den eksterne agenten**, slik at den eksterne agenten kan forstå oppgaven som må fullføres. I en A2A-server bruker en agent sin egen Large Language Model (LLM) for å analysere innkommende forespørsler og utføre oppgaver ved hjelp av sine egne interne verktøy.

#### Artefakt

Når en ekstern agent har fullført den forespurte oppgaven, opprettes arbeidsproduktet som en artefakt. En artefakt **inneholder resultatet av agentens arbeid**, en **beskrivelse av hva som ble fullført**, og **tekstkonteksten** som sendes gjennom protokollen. Etter at artefakten er sendt, lukkes tilkoblingen med den eksterne agenten til den trengs igjen.

#### Hendelseskø

Denne komponenten brukes til **å håndtere oppdateringer og sende meldinger**. Den er spesielt viktig i produksjon for agentiske systemer for å forhindre at tilkoblingen mellom agenter lukkes før en oppgave er fullført, spesielt når oppgaveløsning kan ta lengre tid.

### Fordeler med A2A

• **Forbedret samarbeid**: Den muliggjør interaksjon mellom agenter fra ulike leverandører og plattformer, deler kontekst og samarbeider, og legger til rette for sømløs automatisering på tvers av tradisjonelt adskilte systemer.

• **Fleksibilitet i modellvalg**: Hver A2A-agent kan bestemme hvilken LLM den bruker for å håndtere forespørslene sine, noe som gir mulighet for optimaliserte eller finjusterte modeller per agent, i motsetning til en enkelt LLM-tilkobling i noen MCP-scenarier.

• **Innebygd autentisering**: Autentisering er integrert direkte i A2A-protokollen, og gir et robust sikkerhetsrammeverk for agentinteraksjoner.

### A2A Eksempel

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.no.png)

La oss utvide vårt reisebestillingsscenario, men denne gangen ved bruk av A2A.

1. **Brukerforespørsel til multi-agent**: En bruker interagerer med en "Reiseagent" A2A-klient/agent, kanskje ved å si: "Vennligst bestill en hel tur til Honolulu for neste uke, inkludert fly, hotell og leiebil."

2. **Orkestrering av Reiseagent**: Reiseagenten mottar denne komplekse forespørselen. Den bruker sin LLM til å resonnere om oppgaven og avgjøre at den må interagere med andre spesialiserte agenter.

3. **Inter-agent kommunikasjon**: Reiseagenten bruker deretter A2A-protokollen for å koble seg til underliggende agenter, som en "Flyselskap-agent," en "Hotell-agent," og en "Bilutleie-agent" som er opprettet av ulike selskaper.

4. **Delegert oppgaveutførelse**: Reiseagenten sender spesifikke oppgaver til disse spesialiserte agentene (f.eks. "Finn flyreiser til Honolulu," "Bestill et hotell," "Lei en bil"). Hver av disse spesialiserte agentene, som kjører sine egne LLM-er og bruker sine egne verktøy (som kan være MCP-servere selv), utfører sin spesifikke del av bestillingen.

5. **Samlet respons**: Når alle underliggende agenter fullfører sine oppgaver, samler Reiseagenten resultatene (flydetaljer, hotellbekreftelse, bilutleie-bestilling) og sender en omfattende, chat-stil respons tilbake til brukeren.

## Natural Language Web (NLWeb)

Nettsider har lenge vært den primære måten for brukere å få tilgang til informasjon og data på internett.

La oss se på de ulike komponentene i NLWeb, fordelene med NLWeb og et eksempel på hvordan NLWeb fungerer ved å se på vår reiseapplikasjon.

### Komponenter i NLWeb

- **NLWeb-applikasjon (Kjernetjenestekode)**: Systemet som behandler naturlige språkspørsmål. Det kobler sammen de ulike delene av plattformen for å lage svar. Du kan tenke på det som **motoren som driver de naturlige språkfunksjonene** på en nettside.

- **NLWeb-protokoll**: Dette er et **grunnleggende sett med regler for naturlig språkinteraksjon** med en nettside. Den sender tilbake svar i JSON-format (ofte ved bruk av Schema.org). Formålet er å skape et enkelt grunnlag for "AI-nettet," på samme måte som HTML gjorde det mulig å dele dokumenter online.

- **MCP-server (Model Context Protocol Endpoint)**: Hver NLWeb-oppsett fungerer også som en **MCP-server**. Dette betyr at den kan **dele verktøy (som en "spør"-metode) og data** med andre AI-systemer. I praksis gjør dette nettstedets innhold og funksjoner brukbare for AI-agenter, slik at nettstedet blir en del av det bredere "agent-økosystemet."

- **Embedding-modeller**: Disse modellene brukes til å **konvertere nettstedets innhold til numeriske representasjoner kalt vektorer** (embeddings). Disse vektorene fanger mening på en måte som datamaskiner kan sammenligne og søke. De lagres i en spesiell database, og brukere kan velge hvilken embedding-modell de vil bruke.

- **Vektordatabase (Hentemekanisme)**: Denne databasen **lagrer embeddingene av nettstedets innhold**. Når noen stiller et spørsmål, sjekker NLWeb vektordatabasen for raskt å finne den mest relevante informasjonen. Den gir en rask liste over mulige svar, rangert etter likhet. NLWeb fungerer med ulike vektorlagringssystemer som Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb Eksempel

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.no.png)

Tenk deg vår reisebestillingsnettside igjen, men denne gangen drevet av NLWeb.

1. **Dataregistrering**: Reisewebsiden sitt eksisterende produktkatalog (f.eks. flylister, hotellbeskrivelser, turpakker) formateres ved bruk av Schema.org eller lastes inn via RSS-feeder. NLWebs verktøy registrerer disse strukturerte dataene, lager embeddings og lagrer dem i en lokal eller ekstern vektordatabase.

2. **Naturlig språkspørsmål (Menneske)**: En bruker besøker nettsiden og, i stedet for å navigere i menyer, skriver inn i et chat-grensesnitt: "Finn et familievennlig hotell i Honolulu med basseng for neste uke."

3. **NLWeb-behandling**: NLWeb-applikasjonen mottar dette spørsmålet. Den sender spørsmålet til en LLM for forståelse og søker samtidig i sin vektordatabase etter relevante hotelloppføringer.

4. **Presise resultater**: LLM hjelper til med å tolke søkeresultatene fra databasen, identifisere de beste treffene basert på "familievennlig," "basseng," og "Honolulu"-kriterier, og deretter formatere et naturlig språkrespons. Viktigst av alt refererer responsen til faktiske hoteller fra nettstedets katalog, og unngår oppdiktet informasjon.

5. **AI-agentinteraksjon**: Fordi NLWeb fungerer som en MCP-server, kan en ekstern AI-reiseagent også koble seg til nettstedets NLWeb-instans. AI-agenten kan deretter bruke `ask` MCP-metoden for å spørre nettstedet direkte: `ask("Er det noen veganvennlige restauranter i Honolulu-området anbefalt av hotellet?")`. NLWeb-instansen vil behandle dette, utnytte sin database med restaurantinformasjon (hvis lastet), og returnere en strukturert JSON-respons.

### Har du flere spørsmål om MCP/A2A/NLWeb?

Bli med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortimer og få svar på dine spørsmål om AI-agenter.

## Ressurser

- [MCP for nybegynnere](https://aka.ms/mcp-for-beginners)  
- [MCP-dokumentasjon](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.