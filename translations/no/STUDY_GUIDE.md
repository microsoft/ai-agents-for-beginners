# AI-agenter for nybegynnere - Studieveiledning og kurssammendrag

Denne veiledningen gir en oppsummering av kurset "AI-agenter for nybegynnere" og forklarer viktige konsepter, rammeverk og designmønstre for å bygge AI-agenter.

## 1. Introduksjon til AI-agenter

**Hva er AI-agenter?**  
AI-agenter er systemer som utvider mulighetene til store språkmodeller (LLMs) ved å gi dem tilgang til **verktøy**, **kunnskap** og **minne**. I motsetning til en standard LLM-chatbot som bare genererer tekst basert på treningsdata, kan en AI-agent:  
- **Oppfatte** sitt miljø (via sensorer eller inndata).  
- **Resonnere** om hvordan man løser et problem.  
- **Handle** for å endre miljøet (via aktuatorer eller verktøykjøring).

**Nøkkelkomponenter for en agent:**  
- **Miljø**: Rommet der agenten opererer (f.eks. et bookingsystem).  
- **Sensorer**: Mekanismer for å samle informasjon (f.eks. lese en API).  
- **Aktuatorer**: Mekanismer for å utføre handlinger (f.eks. sende en e-post).  
- **Hjerne (LLM)**: Resonneringsmotoren som planlegger og bestemmer hvilke handlinger som skal tas.

## 2. Agentiske rammeverk

Kurset dekker tre hovedrammeverk for å bygge agenter:

| Rammeverk | Fokus | Best for |
|-----------|-------|----------|
| **Semantic Kernel** | Produksjonsklart SDK for .NET/Python | Bedriftsapplikasjoner, integrering av AI med eksisterende kode. |
| **AutoGen** | Samarbeid mellom flere agenter | Komplekse scenarier som krever at flere spesialiserte agenter kommuniserer med hverandre. |
| **Azure AI Agent Service** | Administrert skytjeneste | Sikker, skalerbar utrulling med innebygd tilstandsadministrasjon. |

## 3. Agentiske designmønstre

Designmønstre hjelper til med å strukturere hvordan agenter opererer for å løse problemer pålitelig.

### **Verktøybruksmønster** (Leksjon 4)  
Dette mønsteret gjør det mulig for agenter å samhandle med omverdenen.  
- **Konsept**: Agenten får en "skjema" (en liste over tilgjengelige funksjoner og deres parametere). LLM-en avgjør *hvilket* verktøy som skal kalles og med *hvilke* argumenter basert på brukerens forespørsel.  
- **Flyt**: Brukerforespørsel -> LLM -> **Verktøysvalg** -> **Verktøyutførelse** -> LLM (med verktøyutgang) -> Endelig svar.  
- **Bruksområder**: Hente sanntidsdata (vær, aksjepriser), utføre beregninger, kjøre kode.

### **Planleggingsmønster** (Leksjon 7)  
Dette mønsteret gjør det mulig for agenter å løse komplekse oppgaver i flere steg.  
- **Konsept**: Agenten bryter ned et overordnet mål i en sekvens av mindre deloppgaver.  
- **Tilnærminger**:  
  - **Oppgavedekomponering**: Dele opp "Planlegg en reise" i "Bestill fly", "Bestill hotell", "Lei bil".  
  - **Iterativ planlegging**: Reviderer planen basert på resultatet av tidligere steg (f.eks. hvis flyet er fullt, velg en annen dato).  
- **Implementering**: Involverer ofte en "planlegger"-agent som genererer en strukturert plan (f.eks. JSON) som deretter utføres av andre agenter.

## 4. Designprinsipper

Når du designer agenter, vurder tre dimensjoner:  
- **Rom**: Agenter bør forbinde mennesker og kunnskap, være tilgjengelige men diskrete.  
- **Tid**: Agenter bør lære fra *fortiden*, gi relevante påminnelser i *nået* og tilpasse seg for *fremtiden*.  
- **Kjerne**: Omfavn usikkerhet, men bygg tillit gjennom åpenhet og brukerkontroll.

## 5. Oppsummering av viktige leksjoner

- **Leksjon 1**: Agenter er systemer, ikke bare modeller. De oppfatter, resonerer og handler.  
- **Leksjon 2**: Rammeverk som Semantic Kernel og AutoGen abstraherer kompleksiteten ved verktøysanrop og tilstandsadministrasjon.  
- **Leksjon 3**: Design med åpenhet og brukerkontroll i fokus.  
- **Leksjon 4**: Verktøy er agentens "hender". Skjemadefinisjon er avgjørende for at LLM-en skal forstå hvordan de brukes.  
- **Leksjon 7**: Planlegging er agentens "utførende funksjon" som gjør det mulig å håndtere komplekse arbeidsflyter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på sitt morsmål skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi kan ikke holdes ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->