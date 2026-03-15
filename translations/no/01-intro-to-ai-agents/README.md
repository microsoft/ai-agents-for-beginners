[![Intro to AI Agents](../../../translated_images/no/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikk på bildet ovenfor for å se video av denne leksjonen)_


# Introduksjon til AI-agenter og bruksområder for agenter

Velkommen til kurset "AI Agents for Beginners"! Dette kurset gir grunnleggende kunnskap og praktiske eksempler for å bygge AI-agenter.

Bli med i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> for å møte andre lærende og AI-agentutviklere og stille spørsmål du har om dette kurset.

For å starte dette kurset begynner vi med å få en bedre forståelse av hva AI-agenter er og hvordan vi kan bruke dem i applikasjonene og arbeidsflytene vi bygger.

## Introduksjon

Denne leksjonen dekker:

- Hva er AI-agenter og hvilke forskjellige typer agenter finnes?
- Hvilke bruksområder passer best for AI-agenter og hvordan kan de hjelpe oss?
- Hva er noen av de grunnleggende byggeklossene ved utforming av agentbaserte løsninger?

## Læringsmål
Etter å ha fullført denne leksjonen skal du kunne:

- Forstå AI-agentkonsepter og hvordan de skiller seg fra andre AI-løsninger.
- Bruke AI-agenter på en mest mulig effektiv måte.
- Utforme agentbaserte løsninger produktivt for både brukere og kunder.

## Definere AI-agenter og typer AI-agenter

### Hva er AI-agenter?

AI-agenter er **systemer** som gjør det mulig for **store språkmodeller (LLMs)** å **utføre handlinger** ved å utvide deres evner ved å gi LLM-er **tilgang til verktøy** og **kunnskap**.

La oss dele denne definisjonen opp i mindre deler:

- **System** – Det er viktig å tenke på agenter ikke bare som en enkelt komponent, men som et system av mange komponenter. På det grunnleggende nivået er komponentene i en AI-agent:
  - **Miljø** – Det definerte området hvor AI-agenten opererer. For eksempel, hvis vi hadde en reisebestillingsagent, kan miljøet være reisebestillingssystemet som AI-agenten bruker for å utføre oppgaver.
  - **Sensorer** – Miljøer har informasjon og gir tilbakemeldinger. AI-agenter bruker sensorer for å samle og tolke denne informasjonen om gjeldende tilstand i miljøet. I eksempelagenten for reisebestilling kan bestillingssystemet gi informasjon som hotelltilgjengelighet eller flypriser.
  - **Aktuatorer** – Når AI-agenten mottar gjeldende tilstand i miljøet, bestemmer agenten hva slags handling som skal utføres for å endre miljøet i oppgaven. For reisebestillingsagenten kan det være å booke et tilgjengelig rom for brukeren.

![What Are AI Agents?](../../../translated_images/no/what-are-ai-agents.1ec8c4d548af601a.webp)

**Store språkmodeller** – Begrepet agenter eksisterte før opprettelsen av LLM-er. Fordelen med å bygge AI-agenter med LLM-er er deres evne til å tolke menneskelig språk og data. Denne evnen gjør at LLM-er kan tolke miljøinformasjon og definere en plan for å endre miljøet.

**Utføre handlinger** – Utenfor AI-agent-systemer er LLM-er begrenset til situasjoner hvor handlingen er å generere innhold eller informasjon basert på brukerens forespørsel. Inne i AI-agent-systemer kan LLM-er utføre oppgaver ved å tolke brukerens forespørsel og bruke verktøy som er tilgjengelige i deres miljø.

**Tilgang til verktøy** – Hvilke verktøy LLM-en har tilgang til defineres av 1) miljøet den opererer i og 2) utvikleren av AI-agenten. For vårt eksempel med Reiseagenten er agentens verktøy begrenset av operasjonene som er tilgjengelige i bestillingssystemet, og/eller utvikleren kan begrense agentens tilgang til verktøy til flyvninger.

**Minne+Kunnskap** – Minne kan være korttidsminne i konteksten mellom samtalen mellom brukeren og agenten. På lang sikt, utover informasjonen levert av miljøet, kan AI-agenter også hente kunnskap fra andre systemer, tjenester, verktøy og til og med andre agenter. I eksempel med Reiseagenten kan denne kunnskapen være informasjon om brukerens reisepreferanser lagret i en kundedatabase.

### De forskjellige typene agenter

Nå som vi har en generell definisjon av AI-agenter, la oss se på noen spesifikke agenttyper og hvordan de ville bli brukt i en reisebestillings-AI-agent.

| **Agenttype**                | **Beskrivelse**                                                                                                                       | **Eksempel**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enkle refleksagenter**      | Utfører umiddelbare handlinger basert på forhåndsdefinerte regler.                                                                   | Reiseagenten tolker e-postens kontekst og videresender reiseklager til kundeservice.                                                                                                                                          |
| **Modellbaserte refleksagenter** | Utfører handlinger basert på en modell av verden og endringer i den modellen.                                                          | Reiseagenten prioriterer ruter med betydelige prisendringer basert på tilgang til historiske prisdata.                                                                                                                     |
| **Målbaserte agenter**         | Lager planer for å oppnå spesifikke mål ved å tolke målet og bestemme handlinger for å nå det.                                        | Reiseagent bokser en reise ved å bestemme nødvendige reisearrangementer (bil, kollektivtransport, fly) fra nåværende sted til destinasjon.                                                                                  |
| **Nyttebaserte agenter**       | Vurderer preferanser og veier avveininger numerisk for å bestemme hvordan man oppnår mål.                                             | Reiseagenten maksimerer nytte ved å avveie bekvemmelighet mot kostnad ved bestilling av reise.                                                                                                                               |
| **Lærende agenter**            | Forbedrer seg over tid ved å respondere på tilbakemeldinger og justere handlinger deretter.                                           | Reiseagenten forbedres ved å bruke kundetilbakemeldinger fra undersøkelser etter reise for å gjøre justeringer i fremtidige bestillinger.                                                                                     |
| **Hierarkiske agenter**        | Har flere agenter i et lagdelt system, der agenter på høyere nivå deler oppgaver i underoppgaver for agenter på lavere nivå til å fullføre. | Reiseagenten kansellerer en tur ved å dele oppgaven i underoppgaver (for eksempel kansellere spesifikke bestillinger) og gi lavnivåagenter i oppdrag å fullføre dem og rapportere tilbake til høyere nivå agent.                |
| **Multi-agent systemer (MAS)** | Agenter utfører oppgaver uavhengig, enten samarbeidsvillig eller konkurrerende.                                                        | Samarbeid: Flere agenter bestiller spesifikke reisetjenester som hoteller, fly og underholdning. Konkurranse: Flere agenter styrer og konkurrerer om en delt hotellbestillingskalender for å booke kunder inn på hotellet.  |

## Når bruke AI-agenter

I forrige avsnitt brukte vi Reiseagent-case for å forklare hvordan de forskjellige agenttypene kan brukes i ulike scenarioer for reisebestilling. Vi vil fortsette å bruke denne applikasjonen gjennom kurset.

La oss se på typer bruksområder hvor AI-agenter passer best:

![When to use AI Agents?](../../../translated_images/no/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Åpne problemer** – tillater LLM å bestemme nødvendige steg for å fullføre en oppgave fordi det ikke alltid kan hardkodes i en arbeidsflyt.
- **Flere-trinns prosesser** – oppgaver som krever et nivå av kompleksitet der AI-agenten må bruke verktøy eller informasjon over flere runder i stedet for enkelthenting.
- **Forbedring over tid** – oppgaver hvor agenten kan forbedre seg over tid ved å motta tilbakemeldinger enten fra sitt miljø eller brukere for å gi bedre nytteverdi.

Vi dekker flere betraktninger om bruk av AI-agenter i leksjonen Bygge pålitelige AI-agenter.

## Grunnleggende om agentiske løsninger

### Agentutvikling

Det første steget i å designe et AI-agent-system er å definere verktøy, handlinger og atferd. I dette kurset fokuserer vi på å bruke **Azure AI Agent Service** for å definere våre agenter. Den tilbyr funksjoner som:

- Valg av åpne modeller som OpenAI, Mistral og Llama
- Bruk av lisensierte data gjennom leverandører som Tripadvisor
- Bruk av standardiserte OpenAPI 3.0-verktøy

### Agentiske mønstre

Kommunikasjon med LLM skjer gjennom prompts. Gitt den semi-autonome naturen til AI-agenter, er det ikke alltid mulig eller nødvendig å manuelt reprompt LLM etter en endring i miljøet. Vi bruker **agentiske mønstre** som lar oss prompt LLM over flere steg på en mer skalerbar måte.

Dette kurset er delt inn i noen av dagens populære agentiske mønstre.

### Agentiske rammeverk

Agentiske rammeverk gir utviklere mulighet til å implementere agentiske mønstre gjennom kode. Disse rammeverkene tilbyr maler, plugins og verktøy for bedre samarbeid mellom AI-agenter. Disse fordelene gir mulighet for bedre observasjon og feilsøking av AI-agent-systemer.

I dette kurset skal vi utforske Microsoft Agent Framework (MAF) for å bygge produksjonsklare AI-agenter.

## Eksempel-kode

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Har du flere spørsmål om AI-agenter?

Bli med på [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontoretimer og få svar på spørsmål om AI-agenter.

## Forrige leksjon

[Course Setup](../00-course-setup/README.md)

## Neste leksjon

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->