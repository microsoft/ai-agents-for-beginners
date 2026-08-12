# Opbygning af Computer Use Agents (CUA)

Computer use agents kan interagere med hjemmesider på samme måde som en person: ved at åbne en browser, inspicere siden og tage den næste bedste handling baseret på, hvad de ser. I denne lektion bygger du en browserautomationsagent, der søger på Airbnb, udtrækker strukturerede listeoplysninger og identificerer det billigste ophold i Stockholm.

Lektionen kombinerer Browser-Use til AI-drevet navigation, Playwright og Chrome DevTools Protocol (CDP) til browserkontrol, Azure OpenAI til visionsbaseret ræsonnering og Pydantic til struktureret udtrækning.

## Introduktion

Denne lektion vil dække:

- Forstå, hvornår computer use agents er et bedre valg end udelukkende API-automation
- Kombinere Browser-Use med Playwright og CDP til pålidelig håndtering af browserens livscyklus
- Bruge Azure OpenAI vision og struktureret Pydantic-output til at udtrække listeoplysninger fra dynamiske websider
- Beslutte, hvornår man skal bruge et agent-først, actor-først eller hybrid browserautomationsworkflow

## Læringsmål

Efter at have gennemført denne lektion, vil du vide, hvordan man:

- Konfigurerer Browser-Use med Azure OpenAI og Playwright
- Opbygger et browserautomationsworkflow, der navigerer på et ægte website og håndterer dynamiske UI-elementer
- Udtrækker typede resultater fra synligt sideindhold og omsætter dem til forretningslogik
- Vælger mellem agent- og actor-mønstre baseret på, hvor forudsigeligt browseropgaven er

## Kodeeksempel

Denne lektion inkluderer en notebook-tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Starter en Chrome-session over CDP, søger Airbnb efter lister i Stockholm, udtrækker priser med Browser-Use vision og returnerer det billigste valg som strukturerede data.

## Forudsætninger

- Python 3.12+
- Azure OpenAI-udrulning konfigureret i dit miljø
- Chrome eller Chromium installeret lokalt
- Playwright-afhængigheder installeret
- Grundlæggende fortrolighed med async Python

## Opsætning

Installer de pakker, der bruges i notebooken:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Sæt de Azure OpenAI-miljøvariable, som notebooken bruger:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valgfrit: standardindstilles til den nyeste API-version, når det udelades
AZURE_OPENAI_API_VERSION=...
```

## Arkitekturoversigt

Notebooken demonstrerer et hybrid browserautomationsworkflow:

1. Chrome starter med CDP aktiveret, så både Playwright og Browser-Use kan dele den samme browsersession.
2. En Browser-Use agent håndterer åbne navigationopgaver såsom at åbne Airbnb, afvise pop-ups og søge efter Stockholm.
3. Den aktive side inspiceres med et struktureret Pydantic-skema for at udtrække listeoverskrifter, natlige priser, bedømmelser og URL'er.
4. Python-logik sammenligner de udtrukne lister og fremhæver det billigste resultat.

Denne tilgang bevarer den fleksible, visionsbaserede ræsonnering, som Browser-Use er god til, samtidig med at du får deterministisk browserkontrol, når det er nødvendigt.

## Vigtige pointer og bedste praksis

### Hvornår man skal bruge Agent vs Actor

| Scenario | Brug Agent | Brug Actor |
|----------|------------|-----------|
| Dynamiske layouts | Ja, AI kan tilpasse sig sideændringer | Nej, skrøbelige selektorer kan bryde |
| Kendt struktur | Nej, en agent er langsommere end direkte kontrol | Ja, hurtig og præcis |
| Find elementer | Ja, naturligt sprog fungerer godt | Nej, præcise selektorer kræves |
| Timing kontrol | Nej, mindre forudsigeligt | Ja, fuld kontrol over ventetider og forsøg |
| Komplekse workflows | Ja, håndterer uventede UI-tilstande | Nej, kræver eksplicit forgrening |

### Browser-Use bedste praksis

1. Start med en agent til udforskning og dynamisk navigation.
2. Skift til direkte sidekontrol, når interaktionen bliver forudsigelig.
3. Brug strukturerede output-modeller, så udtrukne data valideres og er typesikre.
4. Tilføj forsinkelser strategisk efter handlinger, der udløser synlige UI-ændringer.
5. Tag screenshots under iteration, så fejl er lettere at fejlfinde.
6. Forvent at hjemmesider ændrer sig, og design fallback-strategier til pop-ups og layoutskift.
7. Bland agent- og actor-mønstre for at opnå både fleksibilitet og præcision.

### Sikkerhedsgitre for Browser Agents

Browser-agenter opererer på levende hjemmesider, så de kræver strammere grænser end et script, der kun kalder en kendt API. Inden du går fra en notebook-demo til et ægte workflow, skal du definere kontrolmekanismerne omkring, hvad agenten kan se, klikke på og indsende.

1. **Afgræns browsingmiljøet.** Kør agenten i en dedikeret browserprofil eller sandbox, og begræns den til de nødvendige domæner for opgaven.
2. **Adskil observation fra handling.** Lad agenten først søge, læse og udtrække data; kræv et eksplicit godkendelsestrin, før den indsender formularer, sender beskeder, booker rejser, foretager køb, sletter poster eller ændrer kontoinstillinger.
3. **Hold hemmeligheder ude af prompts og logs.** Placer ikke adgangskoder, betalingsoplysninger, sessionscookies eller rå persondata i modelkonteksten. Lad brugeren overtage til autentifikation og rediger følsomme felter ud af logfiler.
4. **Behandl sideindhold som utroværdig input.** En hjemmeside kan indeholde instruktioner, der er beregnet for agenten, ikke brugeren. Agenten skal ignorere sidetekst, der beder den om at ændre sit mål, afsløre data, deaktivere sikkerhedsforanstaltninger eller besøge irrelevante sider.
5. **Brug deterministiske kontroller omkring risikable trin.** Verificer den aktuelle URL, sidetitel, valgte element, pris, modtager og handlingsresumé med kode, før du beder brugeren godkende det endelige trin.
6. **Sæt budgetter og stopbetingelser.** Begræns antal handlinger, forsøg, faner og minutter agenten må bruge. Stop, når sidetilstanden er tvetydig i stedet for at fortsætte med at klikke.
7. **Optag nyttige beviser, ikke alt.** Gem handlingsresuméer, tidsstempler, URLs, beskrivelser af valgte elementer og screenshots-referencer, så fejl kan gennemgås uden at gemme unødvendigt følsomt sideindhold.

I Airbnb-eksemplet er standarden at søge lister og udtrække priser sikkert. At logge ind, kontakte en vært eller gennemføre en booking bør være en separat brugergodkendt handling.

### Anvendelser i den virkelige verden

- Rejsebooking og prisovervågning
- E-handel pris-sammenligning og tilgængelighedskontrol
- Struktureret udtrækning fra dynamiske hjemmesider
- Vision-aware UI-testning og verifikation
- Hjemmesideovervågning og alarmering
- Intelligent formularudfyldning på tværs af flertrinsflows

## Eksempel fra den virkelige verden: Microsoft Project Opal

Agenten, du bygger i denne lektion, er en lille, lokal version af en **computer use agent (CUA)** — et program, der styrer en browser på samme måde som en person. Microsoft bringer denne idé til erhvervslivet med **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, en funktion i Microsoft 365 Copilot.

Med Project Opal beskriver du en opgave, og agenten arbejder på dine vegne ved hjælp af **computer use på en sikker Windows 365 Cloud PC**, der opererer på tværs af din organisations browser-baserede applikationer, sider og data. Den arbejder **asynkront i baggrunden**, og du kan styre arbejdet eller overtage kontrollen når som helst. Eksempler på jobs omfatter:

- Håndtering af anmodninger om sikkerhedsgruppe-medlemskab
- Indsamling og validering af revisionsbeviser til compliance-gennemgange
- Triagere IT-incidenter (opdatere ticketsstatus, tildele ejere, lukke dubletter)
- Sammenstille Excel-data til en finansiel afslutningspræsentation

Opal er en nyttig reference for, hvordan en **produktionsklar, pålidelig** computer use agent ser ud — og den understøtter begreber fra tidligere lektioner:

| Begreb i dette kursus | Hvordan Project Opal anvender det |
|---------------------|----------------------------------|
| **Human-in-the-loop** (Lektion 06) | Opal stopper op for login-oplysninger, følsomme data eller uklare instruktioner og indtaster aldrig adgangskoder eller indsender formularer uden eksplicit bekræftelse. Du kan *Overtage Kontrollen* og *Aflevere Kontrollen* midt i en opgave. |
| **Pålidelige & sikre agenter** (Lektioner 06 & 18) | Kører i en isoleret Windows 365 Cloud PC, er som standard browser-only (andet computeradgang blokeret, håndhævet via Intune), bruger *din* identitet, så den kun får adgang til det, du er autoriseret til, og logger alle handlinger til revisions- og sporbarhed. |
| **Planlægning & metakognition** (Lektioner 07 & 09) | Opal genererer først en plan for jobbet, overvåger sin egen ræsonnering ved hvert trin og stopper op, hvis den opdager mistænkelig aktivitet. |
| **Genanvendelige kapaciteter / værktøjer** (Lektion 04) | **Skills** giver dig mulighed for at skrive instruktioner til gentagelige jobs (importeret fra en `.md` fil eller forfattet med Opal) og genbruge dem på tværs af samtaler. |

> **Tilgængelighed:** Project Opal er i øjeblikket tilgængelig for brugere i [Frontier early access-programmet](https://adoption.microsoft.com/copilot/frontier-program/) med et Microsoft 365 Copilot-abonnement, og din administrator skal have gennemført opsætningen. Da det er en eksperimentel Frontier-funktion, kan funktionaliteter ændre sig over tid.

## Yderligere ressourcer

- [Kom godt i gang med Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrationsskabelon](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actor-parametre og indholdsudtrækning](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursusopsætning](../00-course-setup/README.md)

## Forrige lektion

[Udforskning af Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Næste lektion

[Udrulning af skalerbare agenter](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->