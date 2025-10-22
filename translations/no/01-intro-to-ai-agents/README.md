<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T15:45:46+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "no"
}
-->
[![Introduksjon til AI-agenter](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.no.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikk på bildet over for å se videoen til denne leksjonen)_

# Introduksjon til AI-agenter og bruksområder

Velkommen til kurset "AI-agenter for nybegynnere"! Dette kurset gir grunnleggende kunnskap og praktiske eksempler på hvordan man bygger AI-agenter.

Bli med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærere og AI-agentbyggere, og still spørsmål du måtte ha om dette kurset.

For å starte kurset, begynner vi med å få en bedre forståelse av hva AI-agenter er og hvordan vi kan bruke dem i applikasjonene og arbeidsflytene vi bygger.

## Introduksjon

Denne leksjonen dekker:

- Hva er AI-agenter, og hvilke typer agenter finnes?
- Hvilke bruksområder passer best for AI-agenter, og hvordan kan de hjelpe oss?
- Hva er noen av de grunnleggende byggeklossene når man designer agentbaserte løsninger?

## Læringsmål

Etter å ha fullført denne leksjonen, skal du kunne:

- Forstå konseptene bak AI-agenter og hvordan de skiller seg fra andre AI-løsninger.
- Bruke AI-agenter på en mest mulig effektiv måte.
- Produktivt designe agentbaserte løsninger for både brukere og kunder.

## Definere AI-agenter og typer AI-agenter

### Hva er AI-agenter?

AI-agenter er **systemer** som gjør det mulig for **store språkmodeller (LLMs)** å **utføre handlinger** ved å utvide deres evner gjennom tilgang til **verktøy** og **kunnskap**.

La oss bryte ned denne definisjonen i mindre deler:

- **System** - Det er viktig å tenke på agenter som et system av mange komponenter, ikke bare én enkelt komponent. På et grunnleggende nivå består komponentene i en AI-agent av:
  - **Miljø** - Det definerte rommet hvor AI-agenten opererer. For eksempel, hvis vi hadde en AI-agent for reisebestilling, kunne miljøet være reisebestillingssystemet som agenten bruker for å fullføre oppgaver.
  - **Sensorer** - Miljøer har informasjon og gir tilbakemeldinger. AI-agenter bruker sensorer for å samle inn og tolke denne informasjonen om miljøets nåværende tilstand. I eksempelet med reisebestillingsagenten kan systemet gi informasjon som hotelltilgjengelighet eller flypriser.
  - **Aktuatorer** - Når AI-agenten mottar informasjon om miljøets nåværende tilstand, bestemmer den hvilke handlinger som skal utføres for å endre miljøet. For reisebestillingsagenten kan dette være å bestille et tilgjengelig rom for brukeren.

![Hva er AI-agenter?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.no.png)

**Store språkmodeller** - Konseptet med agenter eksisterte før opprettelsen av LLM-er. Fordelen med å bygge AI-agenter med LLM-er er deres evne til å tolke menneskelig språk og data. Denne evnen gjør det mulig for LLM-er å tolke miljøinformasjon og definere en plan for å endre miljøet.

**Utføre handlinger** - Utenfor AI-agent-systemer er LLM-er begrenset til situasjoner der handlingen er å generere innhold eller informasjon basert på en brukers forespørsel. Innenfor AI-agent-systemer kan LLM-er utføre oppgaver ved å tolke brukerens forespørsel og bruke verktøy som er tilgjengelige i deres miljø.

**Tilgang til verktøy** - Hvilke verktøy LLM-en har tilgang til, bestemmes av 1) miljøet den opererer i og 2) utvikleren av AI-agenten. For vårt reiseagenteksempel er agentens verktøy begrenset av operasjonene som er tilgjengelige i bestillingssystemet, og/eller utvikleren kan begrense agentens tilgang til kun flyreiser.

**Minne + kunnskap** - Minne kan være kortsiktig i konteksten av samtalen mellom brukeren og agenten. Langsiktig, utenfor informasjonen som gis av miljøet, kan AI-agenter også hente kunnskap fra andre systemer, tjenester, verktøy og til og med andre agenter. I reiseagenteksempelet kan denne kunnskapen være informasjon om brukerens reisepreferanser som finnes i en kundedatabase.

### De ulike typene agenter

Nå som vi har en generell definisjon av AI-agenter, la oss se på noen spesifikke agenttyper og hvordan de kan brukes i en AI-agent for reisebestilling.

| **Agenttype**                 | **Beskrivelse**                                                                                                                       | **Eksempel**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enkle refleksagenter**      | Utfører umiddelbare handlinger basert på forhåndsdefinerte regler.                                                                     | Reiseagenten tolker konteksten i en e-post og videresender klager til kundeservice.                                                                                                     |
| **Modellbaserte refleksagenter** | Utfører handlinger basert på en modell av verden og endringer i denne modellen.                                                       | Reiseagenten prioriterer ruter med betydelige prisendringer basert på tilgang til historiske prisdata.                                                                                   |
| **Målbaserte agenter**         | Lager planer for å oppnå spesifikke mål ved å tolke målet og bestemme handlinger for å nå det.                                         | Reiseagenten bestiller en reise ved å finne nødvendige reiseordninger (bil, offentlig transport, fly) fra nåværende sted til destinasjonen.                                              |
| **Nyttebaserte agenter**       | Vurderer preferanser og veier opp avveininger numerisk for å bestemme hvordan mål skal oppnås.                                         | Reiseagenten maksimerer nytte ved å veie bekvemmelighet mot kostnad når den bestiller reiser.                                                                                           |
| **Lærende agenter**            | Forbedrer seg over tid ved å svare på tilbakemeldinger og justere handlinger deretter.                                                | Reiseagenten forbedrer seg ved å bruke kundetilbakemeldinger fra undersøkelser etter reisen for å gjøre justeringer i fremtidige bestillinger.                                          |
| **Hierarkiske agenter**        | Har flere agenter i et hierarkisk system, hvor høyere nivå-agenter deler oppgaver i deloppgaver som lavere nivå-agenter fullfører.    | Reiseagenten kansellerer en reise ved å dele oppgaven i deloppgaver (for eksempel å kansellere spesifikke bestillinger) og la lavere nivå-agenter fullføre dem, og rapportere tilbake til høyere nivå-agenten.                   |
| **Multi-agent-systemer (MAS)** | Agenter fullfører oppgaver uavhengig, enten samarbeidsvillig eller konkurrerende.                                                     | Samarbeid: Flere agenter bestiller spesifikke reisetjenester som hoteller, fly og underholdning. Konkurranse: Flere agenter administrerer og konkurrerer om en delt hotellbestillingskalender for å booke kunder inn på hotellet. |

## Når skal man bruke AI-agenter?

I den tidligere delen brukte vi reiseagent-brukstilfellet for å forklare hvordan de forskjellige typene agenter kan brukes i ulike scenarier for reisebestilling. Vi vil fortsette å bruke denne applikasjonen gjennom hele kurset.

La oss se på hvilke typer brukstilfeller AI-agenter egner seg best for:

![Når skal man bruke AI-agenter?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.no.png)

- **Åpne problemer** - lar LLM-en bestemme nødvendige steg for å fullføre en oppgave fordi det ikke alltid kan hardkodes i en arbeidsflyt.
- **Flertrinnsprosesser** - oppgaver som krever et visst nivå av kompleksitet der AI-agenten må bruke verktøy eller informasjon over flere steg i stedet for enkeltstående forespørsler.
- **Forbedring over tid** - oppgaver der agenten kan forbedre seg over tid ved å motta tilbakemeldinger fra enten miljøet eller brukerne for å gi bedre nytte.

Vi dekker flere vurderinger rundt bruk av AI-agenter i leksjonen om å bygge pålitelige AI-agenter.

## Grunnleggende om agentbaserte løsninger

### Agentutvikling

Det første steget i å designe et AI-agent-system er å definere verktøyene, handlingene og oppførselen. I dette kurset fokuserer vi på å bruke **Azure AI Agent Service** for å definere våre agenter. Den tilbyr funksjoner som:

- Valg av åpne modeller som OpenAI, Mistral og Llama
- Bruk av lisensierte data gjennom leverandører som Tripadvisor
- Bruk av standardiserte OpenAPI 3.0-verktøy

### Agentiske mønstre

Kommunikasjon med LLM-er skjer gjennom forespørsler. Gitt den semi-autonome naturen til AI-agenter, er det ikke alltid mulig eller nødvendig å manuelt sende nye forespørsler til LLM-en etter en endring i miljøet. Vi bruker **agentiske mønstre** som lar oss sende forespørsler til LLM-en over flere steg på en mer skalerbar måte.

Dette kurset er delt inn i noen av de nåværende populære agentiske mønstrene.

### Agentiske rammeverk

Agentiske rammeverk lar utviklere implementere agentiske mønstre gjennom kode. Disse rammeverkene tilbyr maler, plugins og verktøy for bedre samarbeid mellom AI-agenter. Disse fordelene gir bedre muligheter for observasjon og feilsøking av AI-agent-systemer.

I dette kurset vil vi utforske det forskningsdrevne AutoGen-rammeverket og det produksjonsklare Agent-rammeverket fra Semantic Kernel.

### Har du flere spørsmål om AI-agenter?

Bli med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærere, delta på kontortimer og få svar på spørsmål om AI-agenter.

## Forrige leksjon

[Kursoppsett](../00-course-setup/README.md)

## Neste leksjon

[Utforske agentiske rammeverk](../02-explore-agentic-frameworks/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.