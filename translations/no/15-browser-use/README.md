# Bygge datamaskinbrukagenter (CUA)

Datamaskinbrukagenter kan samhandle med nettsteder på samme måte som et menneske: ved å åpne en nettleser, inspisere siden og ta det beste neste steget basert på det de ser. I denne leksjonen skal du bygge en nettleserautomatiseringsagent som søker på Airbnb, henter ut strukturerte listeopplysninger, og identifiserer det billigste oppholdet i Stockholm.

Leksjonen kombinerer Browser-Use for AI-drevet navigasjon, Playwright og Chrome DevTools-protokollen (CDP) for nettleserkontroll, Azure OpenAI for visjonsaktivert resonnering, og Pydantic for strukturert utvinning.

## Introduksjon

Denne leksjonen vil dekke:

- Forstå når datamaskinbrukagenter passer bedre enn kun API-automatisering
- Kombinere Browser-Use med Playwright og CDP for pålitelig håndtering av nettleserens livssyklus
- Bruke Azure OpenAI-visjon og strukturert Pydantic-utdata for å hente ut listeopplysninger fra dynamiske nettsider
- Bestemme når man skal bruke en agent-først, aktør-først, eller hybrid arbeidsflyt for nettleserautomatisering

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

- Konfigurere Browser-Use med Azure OpenAI og Playwright
- Bygge en nettleserautomatiseringsarbeidsflyt som navigerer på et reelt nettsted og håndterer dynamiske UI-elementer
- Hente ut typede resultater fra synlig sideinnhold og gjøre dem om til videre forretningslogikk
- Velge mellom agent- og aktørmønstre basert på hvor forutsigbar nettleseroppgaven er

## Kodeeksempel

Denne leksjonen inkluderer en notatbokveiledning:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Starter en Chrome-økt over CDP, søker Airbnb etter Stockholm-lister, henter priser med Browser-Use-visjon, og returnerer det billigste alternativet som strukturerte data.

## Forutsetninger

- Python 3.12+
- Azure OpenAI-distribusjon konfigurert i ditt miljø
- Chrome eller Chromium installert lokalt
- Playwright-avhengigheter installert
- Grunnleggende kjennskap til async Python

## Oppsett

Installer pakkene brukt i notatboken:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Sett Azure OpenAI miljøvariablene brukt av notatboken:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valgfritt: som standard brukes den nyeste API-versjonen når den utelates
AZURE_OPENAI_API_VERSION=...
```

## Arkitekturoversikt

Notatboken demonstrerer en hybrid arbeidsflyt for nettleserautomatisering:

1. Chrome starter med CDP aktivert slik at både Playwright og Browser-Use kan dele samme nettleserøkt.
2. En Browser-Use-agent håndterer åpent avsluttede navigasjonsoppgaver som å åpne Airbnb, avvise popup-vinduer og søke etter Stockholm.
3. Den aktive siden inspiseres med et strukturert Pydantic-skjema for å hente ut listeoverskrifter, nattpriser, vurderinger og URL-er.
4. Python-logikk sammenligner de hentede listene og markerer det billigste resultatet.

Denne tilnærmingen beholder den fleksible, visjonsbaserte resonneringen som Browser-Use er god på, samtidig som du får deterministisk nettleserkontroll når du trenger det.

## Viktige læringspunkter og beste praksis

### Når bruke Agent vs Aktør

| Scenario | Bruk Agent | Bruk Aktør |
|----------|------------|------------|
| Dynamiske oppsett | Ja, AI kan tilpasse seg sideendringer | Nei, sprø selektorer kan brytes |
| Kjent struktur | Nei, en agent er tregere enn direkte kontroll | Ja, rask og presis |
| Finne elementer | Ja, naturlig språk fungerer godt | Nei, nøyaktige selektorer kreves |
| Tidskontroll | Nei, mindre forutsigbar | Ja, full kontroll over ventetider og forsøk |
| Komplekse arbeidsflyter | Ja, håndterer uventede UI-tilstander | Nei, krever eksplisitt forgreining |

### Browser-Use beste praksis

1. Start med en agent for utforskning og dynamisk navigasjon.
2. Gå over til direkte sidekontroll når interaksjonen blir forutsigbar.
3. Bruk strukturerte utdata-modeller slik at utvunnet data valideres og er typetrygg.
4. Legg til forsinkelser strategisk etter handlinger som utløser synlige UI-endringer.
5. Ta skjermbilder under iterasjoner slik at feil blir enklere å feilsøke.
6. Forvent at nettsteder endrer seg og utform tilbakefallstrategier for popup-er og layoutskift.
7. Kombiner agent- og aktørmønstre for å få både fleksibilitet og presisjon.

### Sikkerhetsvern for nettleseragenter

Nettleseragenter opererer på levende nettsteder, så de trenger strengere grenser enn et skript som kun kaller et kjent API. Før du går fra en notatbokdemo til en ekte arbeidsflyt, definer kontrollene rundt hva agenten kan se, klikke på og sende inn.

1. **Avgrens nettlesermiljøet.** Kjør agenten i en dedikert nettleserprofil eller sandkasse, og begrens den til domener som kreves for oppgaven.
2. **Skill observasjon fra handling.** La agenten søke, lese og hente ut data først; krev et eksplisitt godkjenningssteg før den sender inn skjemaer, sender meldinger, bestiller reiser, foretar kjøp, sletter poster eller endrer kontoinnstillinger.
3. **Hold hemmeligheter ute av prompt og logger.** Plasser ikke passord, betalingsinformasjon, sesjonscookies eller rå persondata i modellkonteksten. La brukeren ta over for autentisering og sensurer sensitive felt fra logger.
4. **Behandle sideinnhold som ikke-pålitelig input.** Et nettsted kan inneholde instruksjoner ment for agenten, ikke brukeren. Agenten bør ignorere sidetekst som ber den endre mål, avsløre data, deaktivere sikkerhetsmekanismer eller besøke irrelevante nettsteder.
5. **Bruk deterministiske sjekker rundt risikable steg.** Verifiser gjeldende URL, sidetittel, valgt element, pris, mottaker og handlingsoppsummering med kode før brukeren blir bedt om å godkjenne siste steg.
6. **Sett budsjetter og stoppbetingelser.** Begrens antall handlinger, forsøk, faner og minutter agenten kan bruke. Stopp når sidetilstanden er uklar i stedet for å fortsette å klikke.
7. **Registrer nyttige bevis, ikke alt.** Behold handlingsoppsummeringer, tidsstempler, URL-er, beskrivelser av valgte elementer og skjermbildereferanser slik at feil kan gjennomgås uten å lagre unødvendig sensitivt sideinnhold.

I Airbnb-eksemplet er det sikre standard å søke i lister og hente ut priser. Innlogging, kontakt med vert eller fullføring av booking bør være en separat brukergodkjent handling.

### Virkelige Bruksområder

- Reisebestilling og prisovervåking
- E-handel prisjämförelse og tilgjengelighetssjekker
- Strukturert utvinning fra dynamiske nettsteder
- Visjonsbevisst UI-testing og verifisering
- Nettstedsmonitorering og varsling
- Intelligent utfylling av skjemaer gjennom flertrinns prosesser

## Virkelig eksempel: Microsoft Project Opal

Agenten du bygger i denne leksjonen er en liten, lokal utgave av en **datamaskinbrukagent (CUA)** — et program som styrer en nettleser slik et menneske ville gjort. Microsoft bringer denne samme ideen til bedrifter med **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, en funksjon i Microsoft 365 Copilot.

Med Project Opal beskriver du en oppgave, og agenten jobber på dine vegne ved å bruke **datamaskinbruk på en sikker Windows 365 Cloud PC**, som opererer på tvers av organisasjonens nettleserbaserte apper, nettsteder og data. Den jobber **asynkront i bakgrunnen**, og du kan styre arbeidet eller ta kontroll når som helst. Eksempeloppgaver inkluderer:

- Håndtering av forespørsler om medlemskap i sikkerhetsgrupper
- Samle og validere revisjonsbevis for samsvarsrevisjoner
- Klassifisere IT-hendelser (oppdatere sakstatus, tildele eiere, lukke duplikater)
- Kompilere Excel-data til en økonomisk avslutningspresentasjon

Opal er en nyttig referanse for hvordan en **produksjonsklar, pålitelig** datamaskinbrukagent ser ut — og forsterker konsepter fra tidligere leksjoner:

| Konsept i dette kurset | Hvordan Project Opal anvender det |
|-----------------------|------------------------------|
| **Menneske-i-sløyfen** (Leksjon 06) | Opal pauser for innloggingsinformasjon, sensitive data eller uklare instruksjoner, og skriver aldri inn passord eller sender inn skjemaer uten eksplisitt bekreftelse. Du kan *ta kontroll* og *gi tilbake kontroll* midt i oppgaven. |
| **Pålitelige og sikre agenter** (Leksjon 06 & 18) | Kjører i isolert Windows 365 Cloud PC, er som standard kun nettleserbasert (annen datamaskintilgang blokkert, håndhevet via Intune), bruker *din* identitet så den kun får tilgang til det du er autorisert for, og logger alle handlinger for revisjon. |
| **Planlegging og metakognisjon** (Leksjon 07 & 09) | Opal lager først en plan for jobben, overvåker så sin egen resonnering på hvert steg, og pauser hvis den oppdager mistenkelig aktivitet. |
| **Gjenbrukbare evner/verktøy** (Leksjon 04) | **Ferdigheter** lar deg skrive instruksjoner for repeterbare jobber (importert fra en `.md`-fil eller laget i Opal) og gjenbruke dem i samtaler. |

> **Tilgjengelighet:** Project Opal er for øyeblikket tilgjengelig for brukere i [Frontier tidlig tilgangsprogram](https://adoption.microsoft.com/copilot/frontier-program/) med Microsoft 365 Copilot-abonnement, og administrator må fullføre oppsett. Siden det er en eksperimentell Frontier-funksjon, kan funksjonene endres over tid.

## Kunnskapssjekk

Test din forståelse før du går videre til neste leksjon.

**1. Når er en nettleserbasert datamaskinbrukagent bedre enn en arbeidsflyt som kun bruker API?**

<details>
<summary>Svar</summary>

Bruk en nettleseragent når oppgaven avhenger av hva som er synlig i en web-UI, siden ikke eksponerer nødvendig API, eller siden endres hyppig nok til at fast API- eller selektorkode ville bli sprø. Hvis et stabilt API finnes for samme oppgave, foretrekk API fordi det vanligvis er raskere, lettere å teste og sikrere.
</details>

**2. I en hybrid arbeidsflyt, hvilke deler bør agenten håndtere og hvilke deler bør håndteres av direkte Playwright-kode?**

<details>
<summary>Svar</summary>

La agenten håndtere åpne navigasjonsoppgaver og dynamiske UI-tilstander, som å finne riktig side eller avvise uventede popup-vinduer. Bytt til direkte Playwright-kontroll når sidestrukturen er kjent og handlingen trenger presisjon, forsøk, venting eller deterministisk validering.
</details>

**3. Airbnb-eksemplet finner en annonse brukeren kanskje vil bestille. Hva bør skje før arbeidsflyten logger inn, kontakter en vert eller fullfører en bestilling?**

<details>
<summary>Svar</summary>

Arbeidsflyten bør pause og be om eksplisitt brukergodkjenning. Før den spør, bør den vise en klar oppsummering av valgt annonse, nåværende URL, pris, datoer og tiltenkt handling. Søking og prishenting kan være autonomt; kontotilgang, meldinger, kjøp og bestillinger bør være brukergodkjent.
</details>

**4. En nettside instruerer agenten til å ignorere sine opprinnelige instruksjoner, besøke et annet nettsted og avsløre lagrede legitimasjoner. Hvordan bør agenten behandle denne teksten?**

<details>
<summary>Svar</summary>

Behandle den som upålitelig sideinnhold, ikke som instruksjon fra utvikler eller bruker. Agenten bør holde seg innenfor tillatt domene og oppgaveomfang, nekte å avsløre hemmeligheter og unngå å følge sidetekst som endrer mål, deaktiverer sikkerhetstiltak eller sender den til irrelevante nettsteder.
</details>

**5. Hvilket bevis er nyttig å beholde når en nettleseragent kjører, og hva bør unngås?**

<details>
<summary>Svar</summary>

Behold handlingsoppsummeringer, tidsstempler, URL-er, beskrivelser av valgte elementer, valideringsresultater og skjermbildereferanser slik at gjennomgang kan utføres. Unngå lagring av passord, betalingsdetaljer, sesjonscookies, rå persondata eller fullstendig sideinnhold med mindre det finnes en spesifikk grunn for lagring og personvern.
</details>

## Ytterligere ressurser

- [Kom i gang med Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrasjon-mal](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktørparametere og innholdsutvinning](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kuroppsett](../00-course-setup/README.md)

## Forrige leksjon

[Utforske Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Neste leksjon

[Distribuere skalerbare agenter](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->