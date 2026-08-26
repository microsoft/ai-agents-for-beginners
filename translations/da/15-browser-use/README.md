# Bygning af Computer Use Agents (CUA)

Computer use agents kan interagere med websites på samme måde som en person: ved at åbne en browser, inspicere siden og tage den næste bedste handling ud fra, hvad de ser. I denne lektion bygger du en browserautomatiseringsagent, der søger på Airbnb, udtrækker strukturerede liste-data og identificerer den billigste overnatning i Stockholm.

Lektionen kombinerer Browser-Use til AI-drevet navigation, Playwright og Chrome DevTools Protocol (CDP) til browserkontrol, Azure OpenAI til synsaktiveret ræsonnering og Pydantic til struktureret udtrækning.

## Introduktion

Denne lektion vil dække:

- Forstå, hvornår computer use agents er bedre end kun API-automatisering
- Kombinere Browser-Use med Playwright og CDP til pålidelig browser livscyklusstyring
- Brug af Azure OpenAI vision og struktureret Pydantic output til at udtrække liste-data fra dynamiske websider
- Beslutte hvornår man bruger agent-først, aktør-først eller hybrid browserautomatiseringsworkflow

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Konfigurere Browser-Use med Azure OpenAI og Playwright
- Bygge et browserautomatiseringsworkflow, der navigerer på en rigtig hjemmeside og håndterer dynamiske UI-elementer
- Udtrække typeregistrerede resultater fra synligt sideindhold og omsætte dem til efterfølgende forretningslogik
- Vælge mellem agent- og aktørmønstre baseret på, hvor forudsigelig browseropgaven er

## Kodeeksempel

Denne lektion inkluderer én notebook tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Starter en Chrome-session via CDP, søger Airbnb for Stockholm-lister, udtrækker priser med Browser-Use vision og returnerer den billigste mulighed som strukturerede data.

## Forudsætninger

- Python 3.12+
- Azure OpenAI-udrulning konfigureret i dit miljø
- Chrome eller Chromium installeret lokalt
- Playwright-afhængigheder installeret
- Grundlæggende kendskab til async Python

## Opsætning

Installer de pakker, der bruges i notebooken:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Sæt de Azure OpenAI miljøvariabler, der bruges af notebooken:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valgfrit: standard til den nyeste API-version, hvis den udelades
AZURE_OPENAI_API_VERSION=...
```

## Arkitektur Oversigt

Notebooken demonstrerer et hybrid browserautomatiseringsworkflow:

1. Chrome starter med CDP aktiveret, så både Playwright og Browser-Use kan dele samme browsersession.
2. En Browser-Use agent håndterer åbne navigationopgaver såsom at åbne Airbnb, afvise pop-ups og søge efter Stockholm.
3. Den aktive side inspiceres med et struktureret Pydantic-skema for at udtrække listeoverskrifter, pris pr. nat, bedømmelser og URL'er.
4. Python-logik sammenligner de udtrukne lister og fremhæver den billigste mulighed.

Denne tilgang bevarer den fleksible, visionsbaserede ræsonnering, som Browser-Use er god til, samtidig med at du får deterministisk browserkontrol, når du har brug for det.

## Vigtigste pointer og bedste praksis

### Hvornår skal man bruge agent vs aktør

| Scenario | Brug Agent | Brug Aktør |
|----------|-----------|-----------|
| Dynamiske layouts | Ja, AI kan tilpasse sig sideskift | Nej, skrøbelige selektorer kan bryde |
| Kendt struktur | Nej, en agent er langsommere end direkte kontrol | Ja, hurtigt og præcist |
| Find elementer | Ja, naturligt sprog fungerer godt | Nej, nøjagtige selektorer er nødvendige |
| Timing kontrol | Nej, mindre forudsigelig | Ja, fuld kontrol over ventetider og forsøg |
| Komplekse workflows | Ja, håndterer uventede UI-tilstande | Nej, kræver eksplicit forgrening |

### Browser-Use bedste praksis

1. Start med en agent til udforskning og dynamisk navigation.
2. Skift til direkte sidekontrol, når interaktionen bliver forudsigelig.
3. Brug strukturerede outputmodeller, så udtrukne data er validerede og typerigtige.
4. Tilføj forsinkelser strategisk efter handlinger, der udløser synlige UI-ændringer.
5. Tag skærmbilleder under iteration, så fejl er lettere at fejlfinde.
6. Forvent at websites ændrer sig og design nødfaldsstrategier for pop-ups og layoutskift.
7. Bland agent- og aktørmønstre for både fleksibilitet og præcision.

### Sikkerhedsforanstaltninger for browser-agenter

Browser-agenter opererer på live websites, så de behøver strammere grænser end et script, der kun kalder en kendt API. Før du går fra notebook-demo til et reelt workflow, definér kontrollerne omkring, hvad agenten kan se, klikke på og indsende.

1. **Afgræns browser-miljøet.** Kør agenten i en dedikeret browserprofil eller sandbox, og begræns den til de domæner, der er nødvendige for opgaven.
2. **Adskil observation fra handling.** Lad agenten søge, læse og udtrække data først; kræv et eksplicit godkendelsestrin, før den indsende formularer, sender beskeder, booker rejser, foretager køb, sletter optegnelser eller ændrer kontoinstillinger.
3. **Hold hemmeligheder ude af prompts og sporingslogs.** Placer ikke adgangskoder, betalingsoplysninger, sessionscookies eller rå persondata i modelkonteksten. Lad brugeren overtage for autentificering og rediger følsomme felter fra logs.
4. **Behandl sideindhold som utroværdigt input.** Et website kan indeholde instrukser beregnet for agenten, ikke brugeren. Agenten bør ignorere sidetekst, der beder den om at ændre sit mål, afsløre data, deaktivere sikkerhedsforanstaltninger eller besøge irrelevante sider.
5. **Brug deterministiske checks omkring risikable trin.** Verificér den aktuelle URL, sidens titel, valgte element, pris, modtager og handlingsoversigt med kode, før du beder brugeren om at godkende det afsluttende trin.
6. **Sæt budgetter og stop-betingelser.** Begræns antal handlinger, genforsøg, faner og minutter, agenten kan bruge. Stop, når sidens tilstand er tvetydig, i stedet for at fortsætte med klik.
7. **Optag nyttige beviser, ikke alt.** Gem handlingsoversigter, tidsstempler, URL'er, beskrivelser af valgte elementer og skærmbilledereferencer, så fejl kan gennemgås uden at gemme unødvendigt følsomt sideindhold.

I Airbnb-eksemplet er den sikre standard at søge i lister og udtrække priser. At logge ind, kontakte en vært eller fuldføre en booking bør være en separat bruger-godkendt handling.

### Anvendelser i virkeligheden

- Rejsebooking og prisovervågning
- Prissammenligning og tilgængelighedstjek i e-handel
- Struktureret udtræk fra dynamiske websites
- Vision-aware UI-testning og verifikation
- Website-overvågning og alarmering
- Intelligent formularudfyldning på tværs af flertrinsflows

## Virkeligt eksempel: Microsoft Project Opal

Den agent, du bygger i denne lektion, er en lille, lokal version af en **computer use agent (CUA)** — et program, der styrer en browser på samme måde som en person ville. Microsoft bringer denne idé til virksomhedsbrug med **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, en funktion i Microsoft 365 Copilot.

Med Project Opal beskriver du en opgave, og agenten arbejder på dine vegne ved hjælp af **computer use på en sikker Windows 365 Cloud PC**, der opererer på tværs af din organisations browserbaserede apps, sites og data. Den arbejder **asynkront i baggrunden**, og du kan til enhver tid guide arbejdet eller overtage kontrollen. Eksempler på opgaver inkluderer:

- Håndtering af anmodninger om medlemskab i sikkerhedsgrupper
- Indsamling og validering af revisionsbeviser til compliance-gennemgange
- Triagering af IT-hændelser (opdatering af billetstatus, tildeling af ejere, lukning af dubletter)
- Sammenstilling af Excel-data til en finansiel afslutningspræsentation

Opal er en nyttig reference til, hvordan en **produktionsklar, troværdig** computer use agent ser ud — og forstærker koncepter fra tidligere lektioner:

| Koncept i dette kursus | Hvordan Project Opal anvender det |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lektion 06) | Opal pauser for loginoplysninger, følsomme data eller tvetydige instruktioner, og indtaster aldrig adgangskoder eller indsender formularer uden eksplicit bekræftelse. Du kan *Overtage Kontrollen* og *Returnere Kontrollen* midt i opgaven. |
| **Troværdige & sikre agenter** (Lektioner 06 & 18) | Kører i en isoleret Windows 365 Cloud PC, er kun browser-baseret som standard (andet computeradgang blokeret via Intune), bruger *din* identitet, så den kun får adgang til det, du er autoriseret til, og logger hver handling til revision. |
| **Planlægning & metakognition** (Lektioner 07 & 09) | Opal genererer først en plan for opgaven, overvåger derefter sin egen ræsonnering i hvert trin og pauser, hvis den opdager mistænkelig aktivitet. |
| **Genanvendelige færdigheder / værktøjer** (Lektion 04) | **Skills** lader dig skrive instruktioner til gentagelige opgaver (importeret fra en `.md` fil eller oprettet med Opal) og genbruge dem på tværs af samtaler. |

> **Tilgængelighed:** Project Opal er aktuelt tilgængeligt for brugere i [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) med et Microsoft 365 Copilot abonnement, og din administrator skal have færdiggjort opsætningen. Da det er en eksperimentel Frontier-funktion, kan kapaciteter ændre sig over tid.

## Videnstjek

Test din forståelse før du går videre til næste lektion.

**1. Hvornår er en browserbaseret computer use agent bedre end et rent API-workflow?**

<details>
<summary>Svar</summary>

Brug en browseragent, når opgaven afhænger af, hvad der er synligt i en web-UI, siden ikke eksponerer den nødvendige API, eller siden ændrer sig ofte nok til, at fast API eller selektorlogik ville være skrøbelig. Hvis en stabil API findes til den samme opgave, foretræk API'en, fordi den normalt er hurtigere, lettere at teste og sikrere.
</details>

**2. I et hybridworkflow, hvilke dele skal agenten håndtere, og hvilke dele skal direkte Playwright-kode håndtere?**

<details>
<summary>Svar</summary>

Lad agenten håndtere åbne navigation- og dynamiske UI-tilstande, såsom at finde den rigtige side eller afvise uventede pop-ups. Skift til direkte Playwright-kontrol, når sidestrukturen er kendt, og handlingen kræver præcision, genforsøg, ventetider eller deterministisk validering.
</details>

**3. Airbnb-eksemplet finder en liste, som brugeren måske vil booke. Hvad skal ske, før workflowet logger ind, kontakter en vært eller fuldfører en booking?**

<details>
<summary>Svar</summary>

Workflowet bør pause og bede om eksplicit bruger-godkendelse. Før det beder om dette, skal det vise en klar oversigt over den valgte liste, den aktuelle URL, pris, datoer og tilsigtet handling. Søgning og prisudtræk kan være autonomt; kontoadgang, beskeder, køb og bookinger bør være bruger-godkendt.
</details>

**4. En webside fortæller agenten at ignorere sine oprindelige instruktioner, besøge en anden side og afsløre gemte legitimationsoplysninger. Hvordan bør agenten behandle den tekst?**

<details>
<summary>Svar</summary>

Behandl det som utroværdigt sideindhold, ikke som en udvikler- eller bruger-instruktion. Agenten bør blive inden for det tilladte domæne og opgavens scope, nægte at afsløre hemmeligheder og undgå at følge sidetekst, der ændrer mål, deaktiverer sikkerhedsforanstaltninger eller sender den til irrelevante sider.
</details>

**5. Hvilke beviser er nyttige at gemme, når en browseragent kører, og hvad bør undgås?**

<details>
<summary>Svar</summary>

Gem handlingsoversigter, tidsstempler, URL'er, beskrivelser af valgte elementer, valideringsresultater og skærmbilledereferencer, så kørslen kan gennemgås. Undgå at gemme adgangskoder, betalingsoplysninger, sessionscookies, rå persondata eller hele sideindhold, medmindre der er en specifik opbevarings- og privatårsag.
</details>

## Yderligere ressourcer

- [Kom godt i gang med Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integration template](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktørparametre og indholdsudtrækning](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursusopsætning](../00-course-setup/README.md)

## Forrige lektion

[Udforskning af Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Næste lektion

[Implementering af skalerbare agenter](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->