# Bygge datamaskinbruksagenter (CUA)

Datamaskinbruksagenter kan samhandle med nettsteder på samme måte som en person ville gjort: ved å åpne en nettleser, inspisere siden, og utføre neste beste handling basert på det de ser. I denne leksjonen skal du bygge en nettleserautomatiseringsagent som søker på Airbnb, henter ut strukturert oppføringsdata, og identifiserer det billigste oppholdet i Stockholm.

Leksjonen kombinerer Browser-Use for AI-drevet navigasjon, Playwright og Chrome DevTools-protokoll (CDP) for nettleserkontroll, Azure OpenAI for synsbasert resonnering, og Pydantic for strukturert uttrekk.

## Introduksjon

Denne leksjonen vil dekke:

- Å forstå når datamaskinbruksagenter er et bedre valg enn kun API-automatisering
- Å kombinere Browser-Use med Playwright og CDP for pålitelig håndtering av nettleserens livssyklus
- Å bruke Azure OpenAI syn og strukturert Pydantic-utdata for å hente oppføringsdata fra dynamiske nettsider
- Å avgjøre når du skal bruke en agent-først, aktør-først eller hybrid nettleserautomatiseringsflyt

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du:

- Konfigurerer Browser-Use med Azure OpenAI og Playwright
- Bygger en nettleserautomatiseringsflyt som navigerer på et ekte nettsted og håndterer dynamiske brukergrensesnittselementer
- Henter ut typede resultater fra synlig sideinnhold og konverterer dem til videre forretningslogikk
- Velger mellom agent- og aktørmønstre basert på hvor forutsigbar nettleseroppgaven er

## Eksempelkode

Denne leksjonen inkluderer ett notatbok-veiledning:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Starter en Chrome-økt over CDP, søker Airbnb etter oppføringer i Stockholm, henter priser med Browser-Use syn, og returnerer det billigste alternativet som strukturert data.

## Forutsetninger

- Python 3.12+
- Azure OpenAI-distribusjon konfigurert i miljøet ditt
- Chrome eller Chromium installert lokalt
- Playwright-avhengigheter installert
- Grunnleggende kjennskap til asynkron Python

## Oppsett

Installer pakkene som brukes i notatboken:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Sett Azure OpenAI-miljøvariablene som brukes av notatboken:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valgfritt: standard er den nyeste API-versjonen hvis utelatt
AZURE_OPENAI_API_VERSION=...
```

## Arkitekturoversikt

Notatboken demonstrerer en hybrid nettleserautomatiseringsflyt:

1. Chrome startes med CDP aktivert slik at både Playwright og Browser-Use kan dele samme nettleserøkt.
2. En Browser-Use-agent håndterer åpne navigasjonsoppgaver som å åpne Airbnb, lukke popup-vinduer og søke etter Stockholm.
3. Den aktive siden inspiseres med et strukturert Pydantic-skjema for å hente oppføringstitler, nattlige priser, vurderinger og URL-er.
4. Python-logikken sammenligner de hentede oppføringene og markerer det billigste resultatet.

Denne tilnærmingen beholder den fleksible, synsbaserte resonneringen som Browser-Use er god på, samtidig som du får deterministisk nettleserkontroll når du trenger det.

## Nøkkelpunkter og beste praksis

### Når du skal bruke Agent vs Aktør

| Scenario | Bruk Agent | Bruk Aktør |
|----------|------------|-----------|
| Dynamiske oppsett | Ja, AI kan tilpasse seg sideendringer | Nei, skjøre selektorer kan bryte |
| Kjente strukturer | Nei, en agent er langsommere enn direkte kontroll | Ja, rask og presis |
| Finne elementer | Ja, naturlig språk fungerer godt | Nei, eksakte selektorer er påkrevd |
| Tidskontroll | Nei, mindre forutsigbart | Ja, full kontroll over venting og gjentakelser |
| Komplekse arbeidsflyter | Ja, håndterer uventede UI-tilstander | Nei, krever eksplisitt forgrening |

### Beste praksis for Browser-Use

1. Start med en agent for utforsking og dynamisk navigasjon.
2. Bytt til direkte sidekontroll når samhandlingen blir forutsigbar.
3. Bruk strukturerte utdata-modeller slik at hentet data valideres og er type-sikker.
4. Legg til forsinkelser strategisk etter handlinger som utløser synlige UI-endringer.
5. Ta skjermbilder under iterasjon slik at feil blir lettere å feilsøke.
6. Forvent at nettsteder endres og design fallback-strategier for popup-vinduer og layoutskift.
7. Bland agent- og aktørmønstre for å få både fleksibilitet og presisjon.

### Reelle bruksområder

- Reisebestilling og prisovervåking
- Prisammenligning og tilgjengelighetssjekker for e-handel
- Strukturert uttrekk fra dynamiske nettsteder
- Synsbevisst UI-testing og verifisering
- Nettstedsovervåking og varsling
- Intelligent utfylling av skjemaer over flertrinnsprosesser

## Reelt eksempel: Microsoft Project Opal

Agenten du bygger i denne leksjonen er en liten, lokal versjon av en **datamaskinbruksagent (CUA)** — et program som styrer en nettleser slik en person ville. Microsoft bringer denne ideen til bedrift med **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, en funksjon i Microsoft 365 Copilot.

Med Project Opal beskriver du en oppgave, og agenten jobber på dine vegne ved å bruke **datamaskinbruk på en sikker Windows 365 Cloud PC**, opererende over organisasjonens nettleserbaserte applikasjoner, nettsider og data. Den fungerer **asynkront i bakgrunnen**, og du kan styre arbeidet eller ta kontroll når som helst. Eksempel jobber inkluderer:

- Håndtering av forespørsler om medlemskap i sikkerhetsgrupper
- Samling og validering av revisjonsbevis for samsvarsgranskinger
- Sortering av IT-hendelser (oppdatere saksstatus, tildele eiere, lukke duplikater)
- Sammenstilling av Excel-data til et finansielt avslutningsdokument

Opal er en nyttig referanse for hvordan en **produksjonsklar, pålitelig** datamaskinbruksagent ser ut — og det forsterker konsepter fra tidligere leksjoner:

| Konsept i dette kurset | Hvordan Project Opal anvender det |
|-----------------------|---------------------------------|
| **Human-in-the-loop** (Leksjon 06) | Opal pauser for påloggingsdetaljer, sensitiv data eller tvetydige instruksjoner, og taster aldri inn passord eller sender skjemaer uten eksplisitt bekreftelse. Du kan *ta kontroll* og *gi fra deg kontroll* midt i oppgaven. |
| **Pålitelige og sikre agenter** (Leksjon 06 & 18) | Kjører i isolert Windows 365 Cloud PC, er som standard kun nettleserbasert (annen datamaskintilgang blokkert, håndhevet via Intune), bruker *din* identitet så den kun får tilgang til hva du er autorisert for, og logger alle handlinger for revisjonssporing. |
| **Planlegging og metakognisjon** (Leksjon 07 & 09) | Opal genererer en plan for jobben først, deretter overvåker den egen resonnering ved hvert steg og pauser hvis den oppdager mistenkelig aktivitet. |
| **Gjenbrukbare ferdigheter/verktøy** (Leksjon 04) | **Skills** lar deg skrive instruksjoner for repeterbare jobber (importert fra en `.md`-fil eller forfattet med Opal) og gjenbruke dem på tvers av samtaler. |

> **Tilgjengelighet:** Project Opal er for øyeblikket tilgjengelig for brukere i [Frontier tidlig tilgangsprogram](https://adoption.microsoft.com/copilot/frontier-program/) med Microsoft 365 Copilot-abonnement, og administratoren din må fullføre oppsett. Fordi det er en eksperimentell Frontier-funksjon, kan kapasiteten endres over tid.

## Ytterligere ressurser

- [Kom i gang med Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrasjonsmal](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktørparametere og innholdshenting](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursoppsett](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->