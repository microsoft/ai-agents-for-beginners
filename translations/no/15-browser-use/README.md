# Bygge databruksagenter (CUA)

Databruksagenter kan samhandle med nettsteder på samme måte som et menneske ville gjort: ved å åpne en nettleser, inspisere siden og ta den neste beste handlingen basert på det de ser. I denne leksjonen skal du bygge en nettleserautomatiseringsagent som søker på Airbnb, trekker ut strukturert listeinformasjon, og identifiserer det billigste oppholdet i Stockholm.

Leksjonen kombinerer Browser-Use for AI-drevet navigasjon, Playwright og Chrome DevTools Protocol (CDP) for nettleserkontroll, Azure OpenAI for synsaktivert resonnement, og Pydantic for strukturert utvinning.

## Introduksjon

Denne leksjonen vil dekke:

- Forstå når databruksagenter er bedre egnet enn kun API-automatisering
- Kombinere Browser-Use med Playwright og CDP for pålitelig styring av nettleserens livssyklus
- Bruke Azure OpenAI visjon og strukturert Pydantic-utdata for å trekke ut listeinformasjon fra dynamiske nettsider
- Å avgjøre når man skal bruke en agent-først, aktør-først eller hybrid nettleserautomatiseringsarbeidsflyt

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du:

- Konfigurerer Browser-Use med Azure OpenAI og Playwright
- Bygger en nettleserautomatiseringsarbeidsflyt som navigerer et ekte nettsted og håndterer dynamiske brukergrensesnittselementer
- Trekker ut typede resultater fra synlig sidinnhold og omdanner dem til videre forretningslogikk
- Velger mellom agent- og aktørmønstre basert på hvor forutsigbar nettleseroppgaven er

## Kodeeksempel

Denne leksjonen inkluderer én notatbokveiledning:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Starter en Chrome-økt over CDP, søker Airbnb etter Stockholm-lister, trekker ut priser med Browser-Use visjon, og returnerer det billigste alternativet som strukturert data.

## Forutsetninger

- Python 3.12+
- Azure OpenAI-distribusjon konfigurert i ditt miljø
- Chrome eller Chromium installert lokalt
- Playwright-avhengigheter installert
- Grunnleggende kjennskap til async Python

## Installering

Installer pakkene som brukes i notatboken:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Sett Azure OpenAI miljøvariablene som notatboken bruker:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valgfritt: standard er siste API-versjon når den utelates
AZURE_OPENAI_API_VERSION=...
```

## Arkitekturoversikt

Notatboken demonstrerer en hybrid nettleserautomatiseringsarbeidsflyt:

1. Chrome starter med CDP aktivert slik at både Playwright og Browser-Use kan dele samme nettleserøkt.
2. En Browser-Use-agent håndterer åpne navigasjonsoppgaver som å åpne Airbnb, avvise popup-vinduer, og søke etter Stockholm.
3. Den aktive siden inspiseres med et strukturert Pydantic-skjema for å trekke ut listeoverskrifter, nattpriser, vurderinger og URL-er.
4. Python-logikk sammenligner de uttrukne listene og fremhever det billigste resultatet.

Denne tilnærmingen beholder den fleksible, synsbaserte resonnementsevnen som Browser-Use er god på, samtidig som den gir deg deterministisk nettleserkontroll når du trenger det.

## Viktige punkter og beste praksis

### Når bruke Agent vs Aktør

| Scenario | Bruke Agent | Bruke Aktør |
|----------|-------------|-------------|
| Dynamiske oppsett | Ja, AI kan tilpasse seg sideendringer | Nei, skjøre selektorer kan feile |
| Kjent struktur | Nei, en agent er tregere enn direkte kontroll | Ja, raskt og presist |
| Finne elementer | Ja, naturlig språk fungerer godt | Nei, eksakte selektorer kreves |
| Tidstyring | Nei, mindre forutsigbart | Ja, full kontroll over venting og forsøk |
| Komplekse arbeidsflyter | Ja, håndterer uventede UI-tilstander | Nei, krever eksplisitt forgrening |

### Beste praksis for Browser-Use

1. Start med en agent for utforskning og dynamisk navigasjon.
2. Bytt til direkte sidestyring når interaksjonen blir forutsigbar.
3. Bruk strukturerte utdata-modeller slik at uttrukket data valideres og er type-sikker.
4. Legg til forsinkelser strategisk etter handlinger som utløser synlige UI-endringer.
5. Ta skjermbilder under iterasjoner slik at feil blir enklere å feilsøke.
6. Forvent at nettsteder endres og design nødstrategier for popup-vinduer og layoutforskyvninger.
7. Kombiner agent- og aktørmønstre for å få både fleksibilitet og presisjon.

### Sikkerhetsgrenser for nettleseragenter

Nettleseragenter opererer på levende nettsteder, så de trenger strengere begrensninger enn et skript som bare kaller en kjent API. Før du går fra en notatbokdemo til en ekte arbeidsflyt, definer kontrollene rundt hva agenten kan se, klikke på og sende inn.

1. **Begrens nettlesermiljøet.** Kjør agenten i en dedikert nettleserprofil eller sandkasse, og begrens den til domenene som kreves for oppgaven.
2. **Skill observasjon fra handling.** La agenten søke, lese og trekke ut data først; krev et eksplisitt godkjenningssteg før den sender inn skjemaer, sender meldinger, bestiller reiser, gjør kjøp, sletter oppføringer eller endrer kontoopplysninger.
3. **Hold hemmeligheter ute av prompt og logger.** Plasser ikke passord, betalingsdetaljer, sesjonskaker eller rå personopplysninger i modellkonteksten. La brukeren ta over for autentisering og rediger sensitive felt i logger.
4. **Behandle sidens innhold som ikke-pålitelig input.** Et nettsted kan inneholde instruksjoner ment for agenten, ikke brukeren. Agenten skal ignorere sidetekst som ber den endre mål, avsløre data, deaktivere sikkerhetsmekanismer eller besøke irrelevante nettsteder.
5. **Bruk deterministiske sjekker rundt risikofylte steg.** Verifiser gjeldende URL, sidetittel, valgt element, pris, mottaker og handlingsoppsummering med kode før du ber brukeren godkjenne det siste steget.
6. **Sett budsjetter og stoppbetingelser.** Begrens antall handlinger, forsøk, faner og minutter agenten kan bruke. Stopp når sidetilstanden er tvetydig i stedet for å fortsette å klikke.
7. **Registrer nyttig bevis, ikke alt.** Behold handlingsoppsummeringer, tidsstempler, URL-er, beskrivelser av valgte elementer og referanser til skjermbilder slik at feil kan gjennomgås uten å lagre unødvendig sensitivt sidinnhold.

I Airbnb-eksemplet er standarden å søke listinger og trekke ut priser. Innlogging, kontakt med vert eller fullføring av bestilling bør være en separat bruker-godkjent handling.

### Virkelige bruksområder

- Reisebestilling og prisovervåkning
- Pris sammenligning og tilgjengelighetssjekker for e-handel
- Strukturert utvinning fra dynamiske nettsteder
- Synsbevisst UI-testing og verifisering
- Nettstedsmonitorering og varsling
- Intelligent utfylling av skjemaer gjennom flertrinnsprosesser

## Virkelig eksempel: Microsoft Project Opal

Agenten du bygger i denne leksjonen er en liten, lokal versjon av en **databruksagent (CUA)** — et program som styrer en nettleser slik en person ville gjort. Microsoft bringer denne ideen til bedrifter med **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, en funksjon i Microsoft 365 Copilot.

Med Project Opal beskriver du en oppgave, og agenten arbeider på dine vegne ved å bruke **databruk på en sikker Windows 365 Cloud PC**, som opererer på tvers av organisasjonens nettleserbaserte applikasjoner, nettsider og data. Den jobber **asynkront i bakgrunnen**, og du kan styre arbeidet eller ta kontroll når som helst. Eksempeloppgaver inkluderer:

- Håndtere forespørsler om medlemskap i sikkerhetsgrupper
- Samle og validere revisjonsbevis for etterlevelsesgjennomganger
- Sortere IT-hendelser (oppdatere status, tildele eiere, lukke duplikater)
- Sammenslå Excel-data til en økonomisk rapport

Opal er en nyttig referanse for hvordan en **produksjonsklar, pålitelig** databruksagent ser ut — og forsterker konsepter fra tidligere leksjoner:

| Konsept i dette kurset | Hvordan Project Opal bruker det |
|------------------------|-------------------------------|
| **Menneske-i-løkken** (Leksjon 06) | Opal stopper opp for innloggingsinformasjon, sensitiv data eller tvetydige instruksjoner, og sender aldri inn passord eller skjemaer uten eksplisitt bekreftelse. Du kan *ta kontroll* og *gi fra deg kontroll* midt i en oppgave. |
| **Pålitelige og sikre agenter** (Leksjon 06 & 18) | Kjører i en isolert Windows 365 Cloud PC, er som standard nettleserbare (annen datatilgang er blokkert, håndhevet via Intune), bruker *din* identitet slik at den kun får tilgang til det du er autorisert for, og logger alle handlinger for revisjon. |
| **Planlegging og metakognisjon** (Leksjon 07 & 09) | Opal genererer først en plan for oppgaven, deretter overvåker den sitt eget resonnement på hvert steg og stopper opp hvis den oppdager mistenkelig aktivitet. |
| **Gjenbrukbare ferdigheter/verktøy** (Leksjon 04) | **Ferdigheter** lar deg skrive instruksjoner for gjentakbare oppgaver (importert fra en `.md`-fil eller opprettet med Opal) og bruke dem på tvers av samtaler. |

> **Tilgjengelighet:** Project Opal er for øyeblikket tilgjengelig for brukere i [Frontier tidlig tilgangsprogram](https://adoption.microsoft.com/copilot/frontier-program/) med et Microsoft 365 Copilot-abonnement, og administratoren må fullføre oppsettet. Siden det er en eksperimentell Frontier-funksjon, kan funksjonaliteten endres over tid.

## Ytterligere ressurser

- [Kom i gang med Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrasjonsmal](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktørparametere og innholdsutvinning](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursoppsett](../00-course-setup/README.md)

## Forrige leksjon

[Utforske Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Neste leksjon

[Distribuere skalerbare agenter](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->