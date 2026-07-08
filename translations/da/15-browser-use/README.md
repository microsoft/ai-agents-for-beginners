# Bygning af Computerbrugereagenter (CUA)

Computerbrugereagenter kan interagere med websites på samme måde som et menneske: ved at åbne en browser, inspicere siden og tage den næste bedste handling ud fra, hvad de ser. I denne lektion bygger du en browserautomatiseringsagent, der søger på Airbnb, udtrækker strukturerede data om annoncer og identificerer det billigste ophold i Stockholm.

Lektionen kombinerer Browser-Use til AI-drevet navigation, Playwright og Chrome DevTools Protocol (CDP) til browserkontrol, Azure OpenAI til synsaktiveret ræsonnering og Pydantic til struktureret udtrækning.

## Introduktion

Denne lektion vil dække:

- Forstå hvornår computerbrugereagenter er et bedre valg end kun API-automatisering
- Kombinere Browser-Use med Playwright og CDP for pålidelig håndtering af browserens livscyklus
- Bruge Azure OpenAI vision og struktureret Pydantic-output til at udtrække annonceringsdata fra dynamiske websider
- Beslutte hvornår man bruger agent-først, aktør-først eller en hybrid browserautomatiseringsarbejdsgang

## Læringsmål

Efter at have gennemført denne lektion vil du vide, hvordan du:

- Konfigurerer Browser-Use med Azure OpenAI og Playwright
- Bygger en browserautomatiseringsarbejdsgang, der navigerer på et rigtigt website og håndterer dynamiske UI-elementer
- Udtrækker typede resultater fra synligt sideindhold og omdanner dem til videre forretningslogik
- Vælger mellem agent- og aktørmønstre baseret på hvor forudsigelig browseropgaven er

## Kodeeksempel

Denne lektion inkluderer én notebook-tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Starter en Chrome-session via CDP, søger på Airbnb efter annoncer i Stockholm, udtrækker priser med Browser-Use vision og returnerer det billigste tilbud som strukturerede data.

## Forudsætninger

- Python 3.12+
- Azure OpenAI-implementering konfigureret i dit miljø
- Chrome eller Chromium installeret lokalt
- Playwright-afhængigheder installeret
- Grundlæggende kendskab til asynkron Python

## Opsætning

Installer de pakker, der bruges i notebooken:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Sæt de Azure OpenAI-miljøvariabler, som notebooken bruger:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valgfrit: standardindstillingen er den nyeste API-version, når den udelades
AZURE_OPENAI_API_VERSION=...
```

## Arkitekturoversigt

Notebooken demonstrerer en hybrid browserautomatiseringsarbejdsgang:

1. Chrome starter med CDP aktiveret, så både Playwright og Browser-Use kan dele den samme browsersession.
2. En Browser-Use agent håndterer åbne navigationopgaver såsom at åbne Airbnb, afvise pop-ups og søge efter Stockholm.
3. Den aktive side inspiceres med et struktureret Pydantic-skema for at udtrække annoncentitler, nattelige priser, bedømmelser og URL'er.
4. Python-logik sammenligner de udtrukne annoncer og fremhæver det billigste resultat.

Denne tilgang bevarer den fleksible, synsbaserede ræsonnering, som Browser-Use er god til, samtidig med at du får deterministisk browserkontrol, når du har brug for det.

## Vigtige pointer og bedste praksis

### Hvornår man skal bruge Agent vs Aktør

| Scenario | Brug Agent | Brug Aktør |
|----------|-------------|-----------|
| Dynamiske layouts | Ja, AI kan tilpasse sig sideændringer | Nej, skøre selektorer kan bryde |
| Kendt struktur | Nej, en agent er langsommere end direkte kontrol | Ja, hurtigt og præcist |
| Find elementer | Ja, naturligt sprog virker godt | Nej, eksakte selektorer er påkrævet |
| Timing kontrol | Nej, mindre forudsigeligt | Ja, fuld kontrol over ventetid og genforsøg |
| Komplekse arbejdsgange | Ja, håndterer uventede UI-tilstande | Nej, kræver eksplicit branching |

### Browser-Use bedste praksis

1. Start med en agent til udforskning og dynamisk navigation.
2. Skift til direkte sidekontrol, når interaktionen bliver forudsigelig.
3. Brug strukturerede outputmodeller, så udtrukne data er validerede og typesikre.
4. Tilføj strategiske forsinkelser efter handlinger, der udløser synlige UI-ændringer.
5. Tag screenshots under iteration for lettere at kunne debugge fejl.
6. Forvent at websites ændrer sig og design fallback-strategier til pop-ups og layoutskift.
7. Bland agent- og aktørmønstre for at få både fleksibilitet og præcision.

### Virkelige anvendelser

- Rejsebooking og prisovervågning
- Prissammenligning og tilgængelighedskontrol inden for e-handel
- Struktureret udtrækning fra dynamiske websites
- Synsbevidst UI-test og verifikation
- Websiteovervågning og alarm
- Intelligent udfyldning af formularer på tværs af flertrinsprocesser

## Virkeligt eksempel: Microsoft Project Opal

Den agent, du bygger i denne lektion, er en lille, lokal version af en **computerbrugereagent (CUA)** — et program, der styrer en browser, som et menneske. Microsoft bringer denne idé til virksomheder med **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, en funktion i Microsoft 365 Copilot.

Med Project Opal beskriver du en opgave, og agenten arbejder på dine vegne ved hjælp af **computerbrug på en sikker Windows 365 Cloud PC**, der opererer på tværs af din organisations browserbaserede applikationer, sider og data. Den arbejder **asynkront i baggrunden**, og du kan styre opgaven eller tage kontrol når som helst. Eksempeljob inkluderer:

- Håndtering af anmodninger om medlemskab i sikkerhedsgrupper
- Indsamling og validering af revisionsbeviser til compliance-gennemgange
- Triagering af IT-hændelser (opdatering af ticketstatus, tildeling af ejere, lukning af dubletter)
- Sammenstilling af Excel-data i et finansielt afslutningsdokument

Opal er en nyttig reference for, hvordan en **produktionsmoden, troværdig** computerbrugereagent ser ud — og den underbygger koncepter fra tidligere lektioner:

| Koncept i dette kursus | Hvordan Project Opal anvender det |
|------------------------|-------------------------------|
| **Mennesket-i-lopen** (Lektion 06) | Opal stopper op for loginoplysninger, følsomme data eller tvetydige instruktioner, og indtaster aldrig adgangskoder eller sender formularer uden eksplicit bekræftelse. Du kan *tage kontrol* og *aflevere kontrol* midt i opgaven. |
| **Troværdige & sikre agenter** (Lektioner 06 & 18) | Kører i en isoleret Windows 365 Cloud PC, er som standard browser-only (andet computeradgang blokeret via Intune), bruger *din* identitet, så den kun får adgang til autoriserede ressourcer, og logger hver handling for revisionsspor. |
| **Planlægning & metakognition** (Lektioner 07 & 09) | Opal genererer først en plan for jobbet, overvåger derefter sin egen ræsonnering ved hvert trin og stopper, hvis den opdager mistænkelig aktivitet. |
| **Genanvendelige kapabiliteter / værktøjer** (Lektion 04) | **Skills** giver dig mulighed for at skrive instruktioner til gentagelige opgaver (importeret fra en `.md`-fil eller oprettet med Opal) og genbruge dem på tværs af samtaler. |

> **Tilgængelighed:** Project Opal er i øjeblikket tilgængeligt for brugere i [Frontier tidlig adgangsprogrammet](https://adoption.microsoft.com/copilot/frontier-program/) med et Microsoft 365 Copilot-abonnement, og din administrator skal have fuldført opsætningen. Da det er en eksperimentel Frontier-funktion, kan kapabiliteter ændre sig over tid.

## Yderligere ressourcer

- [Kom godt i gang med Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrationsskabelon](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktørparametre og indholdstræk](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursusopsætning](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->