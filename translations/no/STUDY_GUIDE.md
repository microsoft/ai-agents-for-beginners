# AI-agenter for nybegynnere - Studieguide og kurssammendrag

Denne guiden gir en oppsummering av kurset "AI Agents for Beginners" og forklarer nøkkelkonsepter, rammeverk og designmønstre for å bygge AI-agenter.

## 1. Introduksjon til AI-agenter

**Hva er AI-agenter?**
AI-agenter er systemer som utvider kapasitetene til store språkmodeller (LLMer) ved å gi dem tilgang til **verktøy**, **kunnskap**, og **hukommelse**. I motsetning til en standard LLM-chatbot som bare genererer tekst basert på treningsdata, kan en AI-agent:
- **Oppfatte** sine omgivelser (via sensorer eller inndata).
- **Resonnere** om hvordan man løser et problem.
- **Handle** for å endre omgivelsene (via aktuatorer eller verktøyutførelse).

**Nøkkelkomponenter i en agent:**
- **Miljø**: Rommet hvor agenten opererer (f.eks. et bookingsystem).
- **Sensorer**: Mekanismer for å samle informasjon (f.eks. lese en API).
- **Aktuatorer**: Mekanismer for å utføre handlinger (f.eks. sende en e-post).
- **Hjerne (LLM)**: Resonneringsmotoren som planlegger og bestemmer hvilke handlinger som skal tas.

## 2. Agentiske rammeverk

Kurset bruker **Microsoft Agent Framework (MAF)** med **Azure AI Foundry Agent Service V2** for å bygge agenter:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Enhetlig Python/C#-SDK for agenter, verktøy og arbeidsflyter | Bygge agenter med verktøy, fleragent-arbeidsflyter og produksjonsmønstre. |
| **Azure AI Foundry Agent Service** | Administrert skykjøring | Sikker, skalerbar distribusjon med innebygd tilstandshåndtering, observerbarhet og tillit. |

## 3. Agentiske designmønstre

Designmønstre hjelper med å strukturere hvordan agenter opererer for å løse problemer pålitelig.

### **Mønster for verktøybruk** (Leksjon 4)
Dette mønsteret lar agenter samhandle med omverdenen.
- **Konsept**: Agenten får et "skjema" (en liste over tilgjengelige funksjoner og deres parametere). LLM-en avgjør *hvilket* verktøy som skal kalles og med *hvilke* argumenter basert på brukerens forespørsel.
- **Flyt**: Brukerforespørsel -> LLM -> **Verktøyvalg** -> **Verktøyutførelse** -> LLM (med verktøyets utdata) -> Endelig svar.
- **Bruksområder**: Hente sanntidsdata (vær, aksjepriser), utføre beregninger, kjøre kode.

### **Planleggingsmønster** (Leksjon 7)
Dette mønsteret gjør det mulig for agenter å løse komplekse, trinnvise oppgaver.
- **Konsept**: Agenten bryter ned et overordnet mål i en sekvens av mindre deloppgaver.
- **Tilnærminger**:
  - **Oppgavedekomponering**: Dele "Planlegg en tur" inn i "Bestill fly", "Bestill hotell", "Lei bil".
  - **Iterativ planlegging**: Revurdere planen basert på resultatet av tidligere steg (f.eks. hvis flyet er fullt, velg en annen dato).
- **Implementering**: Involverer ofte en "Planner"-agent som genererer en strukturert plan (f.eks. JSON) som deretter utføres av andre agenter.

## 4. Designprinsipper

Når du designer agenter, vurder tre dimensjoner:
- **Område**: Agenter bør knytte mennesker og kunnskap sammen, være tilgjengelige men lite påtrengende.
- **Tid**: Agenter bør lære fra *Fortiden*, gi relevante dytt i *Nået*, og tilpasse seg for *Fremtiden*.
- **Kjerne**: Omfavn usikkerhet, men etabler tillit gjennom åpenhet og brukerkontroll.

## 5. Oppsummering av viktige leksjoner

- **Leksjon 1**: Agenter er systemer, ikke bare modeller. De oppfatter, resonnerer og handler.
- **Leksjon 2**: Microsoft Agent Framework abstraherer kompleksiteten ved verktøysanrop og tilstandshåndtering.
- **Leksjon 3**: Design med åpenhet og brukerkontroll i tankene.
- **Leksjon 4**: Verktøy er agentens "hender". Definisjon av skjema er avgjørende for at LLM-en skal forstå hvordan de brukes.
- **Leksjon 7**: Planlegging er agentens "utførende funksjon", som gjør det mulig å ta tak i komplekse arbeidsflyter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Den opprinnelige versjonen på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales en profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->