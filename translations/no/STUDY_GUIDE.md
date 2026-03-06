# AI-agenter for nybegynnere - Studieveiledning og kurssammendrag

This guide provides a summary of the "AI Agents for Beginners" course and explains key concepts, frameworks, and design patterns for building AI Agents.

## 1. Introduksjon til AI-agenter

**Hva er AI-agenter?**
AI-agenter er systemer som utvider kapasitetene til Large Language Models (LLMs) ved å gi dem tilgang til **verktøy**, **kunnskap**, og **minne**. I motsetning til en standard LLM-chatbot som bare genererer tekst basert på treningsdata, kan en AI-agent:
- **Oppfatte** miljøet sitt (via sensorer eller inndata).
- **Resonere** om hvordan man løser et problem.
- **Handle** for å endre miljøet (via aktuatorer eller verktøyutførelse).

**Nøkkelkomponenter i en agent:**
- **Miljø**: Rommet der agenten opererer (f.eks. et bookingsystem).
- **Sensorer**: Mekanismer for å samle informasjon (f.eks. å lese et API).
- **Aktuatorer**: Mekanismer for å utføre handlinger (f.eks. sende en e-post).
- **Hjerne (LLM)**: Resonneringsmotoren som planlegger og bestemmer hvilke handlinger som skal utføres.

## 2. Agent-rammeverk

Kurset bruker **Microsoft Agent Framework (MAF)** sammen med **Azure AI Foundry Agent Service V2** for å bygge agenter:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Enhetlig Python/C# SDK for agenter, verktøy og arbeidsflyter | Å bygge agenter med verktøy, fleragent-arbeidsflyter og produksjonsmønstre. |
| **Azure AI Foundry Agent Service** | Administrert kjøring i skyen | Sikker, skalerbar distribusjon med innebygd tilstandshåndtering, observabilitet og tillit. |

## 3. Agentiske designmønstre

Designmønstre hjelper med å strukturere hvordan agenter opererer for å løse problemer pålitelig.

### **Tool Use Pattern** (Leksjon 4)
Dette mønsteret gjør det mulig for agenter å interagere med omverdenen.
- **Konsept**: Agenten får et "skjema" (en liste over tilgjengelige funksjoner og deres parametere). LLM bestemmer *hvilket* verktøy som skal kalles og med *hvilke* argumenter basert på brukerens forespørsel.
- **Flyt**: Brukerforespørsel -> LLM -> **Verktøyvalg** -> **Verktøykjøring** -> LLM (med verktøyutdata) -> Endelig svar.
- **Bruksområder**: Hente sanntidsdata (vær, aksjepriser), utføre beregninger, kjøre kode.

### **Planleggingsmønster** (Leksjon 7)
Dette mønsteret gjør det mulig for agenter å løse komplekse, flertrinnsoppgaver.
- **Konsept**: Agenten bryter ned et overordnet mål i en sekvens av mindre deloppgaver.
- **Tilnærminger**:
  - **Oppgavedekomponering**: Dele opp "Planlegg en reise" i "Bestill fly", "Bestill hotell", "Lei bil".
  - **Iterativ planlegging**: Revurdere planen basert på resultatet fra tidligere steg (f.eks. hvis flyet er fullt, velg en annen dato).
- **Implementasjon**: Involverer ofte en "Planner"-agent som genererer en strukturert plan (f.eks. JSON) som deretter utføres av andre agenter.

## 4. Designprinsipper

Når du designer agenter, vurder tre dimensjoner:
- **Space**: Agenter bør koble mennesker og kunnskap, være tilgjengelige, men ikke påtrengende.
- **Time**: Agenter bør lære av *fortiden*, gi relevante påminnelser i *nået*, og tilpasse seg for *fremtiden*.
- **Core**: Omfavn usikkerhet, men etabler tillit gjennom åpenhet og brukerkontroll.

## 5. Sammendrag av nøkkellærdommer

- **Leksjon 1**: Agenter er systemer, ikke bare modeller. De oppfatter, resonnerer og handler.
- **Leksjon 2**: Microsoft Agent Framework abstraherer kompleksiteten knyttet til verktøyskall og tilstandshåndtering.
- **Leksjon 3**: Design med åpenhet og brukerkontroll i tankene.
- **Leksjon 4**: Verktøy er agentens "hender". Definisjon av skjema er avgjørende for at LLM skal forstå hvordan de skal brukes.
- **Leksjon 7**: Planlegging er agentens "utførende funksjon", som gjør det mulig å takle komplekse arbeidsflyter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->