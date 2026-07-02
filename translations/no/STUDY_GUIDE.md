# AI-agenter for nybegynnere - Studieveiledning

Bruk denne veiledningen som en praktisk ledsager mens du går gjennom kurset. Den er
ikke ment å erstatte leksjonene. Den hjelper deg med å bestemme hvor du skal begynne, hva du skal
se etter i hver leksjon, og hvordan du kan knytte ideene sammen til en liten fungerende agent-
demo.

Hvis dette er første gang du er her, start enkelt:

1. Les [Oppsett av kurs](./00-course-setup/README.md).
2. Fullfør leksjonene 01-06 i rekkefølge.
3. Ha en liten demoidé i tankene mens du lærer.
4. Etter hver leksjon, spør: "Hva kan agenten min gjøre nå som den ikke kunne gjøre
   før?"

## En enkel demo å ha i tankene

En god måte å lære om agenter på er å følge én demoidé gjennom kurset.

Eksempeldemo: **en kursassistent-agent**.

Brukeren spør:

> "Jeg vil lære hvordan agenter bruker verktøy. Finn de riktige leksjonene, oppsummer hva
> jeg bør lese først, og gi meg en kort øvelse."

En vanlig chatbot kan svare ut fra det den allerede vet. En agent kan gjøre mer:

1. **Lese eller søke i kursfiler** for å finne de riktige leksjonene.
2. **Bruke verktøy** for å hente leksjonslenker, eksempler eller støttemateriell.
3. **Planlegge** en kort læringssti i stedet for å gi ett langt svar.
4. **Bruke kontekst** fra den nåværende samtalen for å holde fokus på elevens
   mål.
5. **Huske nyttige preferanser** hvis applikasjonen støtter minne.
6. **Vise spor, henvisninger eller logger** slik at brukeren kan forstå hva som skjedde.
7. **Bruke retningslinjer** før den tar risikofylte handlinger eller bruker sensitive data.

Mens du studerer hver leksjon, kom tilbake til denne demoen og spør: hvilken ny funksjon
vil denne leksjonen legge til?

## Hva du bygger mot

Ved slutten av kurset skal du kunne forklare og bygge agentsystemer
som kombinerer disse delene:

| Del | Enkel forklaring | I demoen |
|------|------------------|----------|
| Modell | Resonnementsmotoren som tolker brukerens forespørsel | Forstår at eleven vil ha leksjoner om verktøybruk |
| Verktøy | Funksjoner, API-er, filer, nettlesere eller tjenester agenten kan bruke | Søker i repoet eller henter leksjonsinnhold |
| Kunnskap | Dokumenter eller data som grunnlegger svaret | Kurs-README-filer og leksjonsmateriale |
| Kontekst | Informasjon inkludert i neste modellkall | Brukerens mål og verktøyresultater |
| Minne | Informasjon lagret for senere bruk | Eleven foretrekker praktiske Python-eksempler |
| Planlegging | Bryter et større mål ned i mindre steg | Finne leksjoner, oppsummere dem, foreslå øvelse |
| Orkestrering | Rutet arbeid på tvers av verktøy, steg eller agenter | En planlegger kaller et søkeverktøy, så en oppsummerer |
| Tillit | Sikkerhet, evaluering og observasjon | Logger verktøy-kall og spør før viktige handlinger |

## Velg din læringsvei

Du kan ta hele kurset i rekkefølge, eller hoppe til en vei basert på hva du vil
bygge.

| Hvis målet ditt er å... | Start med | Så studer |
|------------------------|-----------|-----------|
| Forstå hva agenter er | 01, 02, 03 | 04, 05, 06 |
| Bygge en agent som bruker verktøy | 04 | 05, 07, 14 |
| Bygge en RAG-basert agent | 05 | 04, 06, 12 |
| Designe flertrinns arbeidsflyter | 07 | 08, 09, 14 |
| Forstå fleragent-systemer | 08 | 07, 09, 11 |
| Forberede agenter for produksjon | 06, 10 | 12, 13, 18 |
| Utforske protokoller og nettleserautomatisering | 11, 15 | 10, 18 |

Tips: hvis du er ny til agenter, ikke hopp over leksjonene 01-06. De gir deg
ordforrådet du trenger for resten av kurset.

## Leksjon-for-leksjon-veiledning

| Leksjon | Hva du lærer | Prøv dette etter leksjonen |
|---------|--------------|----------------------------|
| [01 - Intro til AI-agenter](./01-intro-to-ai-agents/README.md) | Hva som gjør en agent annerledes enn en vanlig chatbot. | Forklar demoideen din som en agent, ikke bare en chatteapp. |
| [02 - Agentiske rammeverk](./02-explore-agentic-frameworks/README.md) | Hvordan rammeverk hjelper med modeller, verktøy, tilstand og arbeidsflyter. | Identifiser hvilke deler av demoen rammeverket ville håndtert. |
| [03 - Agentiske designmønstre](./03-agentic-design-patterns/README.md) | Vanlige mønstre for å designe agentatferd. | Skisser brukerreisen før du skriver kode. |
| [04 - Verktøybruk](./04-tool-use/README.md) | Hvordan agenter kaller verktøy for å hente data eller utføre handling. | Definer ett verktøy agenten i demoen din trenger. |
| [05 - Agentisk RAG](./05-agentic-rag/README.md) | Hvordan henting forankrer agentsvar i dokumenter eller data. | Bestem hvilken kunnskapskilde demoen skal søke i. |
| [06 - Pålitelige agenter](./06-building-trustworthy-agents/README.md) | Hvordan legge til retningslinjer, tilsyn og tryggere oppførsel. | Legg til en regel for når agenten skal spørre brukeren først. |
| [07 - Planleggingsdesign](./07-planning-design/README.md) | Hvordan agenter bryter større mål ned i mindre steg. | Skriv en tre-stegs plan for demoforespørselen din. |
| [08 - Fleragent-design](./08-multi-agent/README.md) | Når man skal splitte arbeidet på flere spesialiserte agenter. | Bestem om demoen din trenger én agent eller flere. |
| [09 - Metakognisjon](./09-metacognition/README.md) | Hvordan agenter kan gjennomgå og forbedre egen output. | Legg til en siste selv-sjekk før agenten svarer. |
| [10 - AI-agenter i produksjon](./10-ai-agents-production/README.md) | Hva som endres når en agent går fra demo til produksjon. | List opp hva du vil overvåke: kvalitet, kostnad, ventetid, feil. |
| [11 - Agentiske protokoller](./11-agentic-protocols/README.md) | Hvordan protokoller kobler agenter til verktøy og andre agenter. | Identifiser hvor en standardprotokoll kan forenkle integrasjon. |
| [12 - Konsteksteknikk](./12-context-engineering/README.md) | Hvordan velge, trimme, isolere og håndtere kontekst. | Bestem hva som hører hjemme i prompten og hva som bør holdes utenfor. |
| [13 - Agentminne](./13-agent-memory/README.md) | Hvordan agenter kan lagre nyttig informasjon på tvers av interaksjoner. | Velg én trygg preferanse demoen kan huske. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Rammeverksspesifikke byggeklosser for agenter og arbeidsflyter. | Koble demoens steg til rammeverkskonsepter. |
| [15 - Datamaskinbruksagenter](./15-browser-use/README.md) | Hvordan agenter kan interagere med nettleser- eller UI-flater. | Velg én nettleseroppgave som fortsatt bør kreve brukerbekreftelse. |
| [18 - Sikring av AI-agenter](./18-securing-ai-agents/README.md) | Hvordan gjøre agenthandlinger mer reviderbare og manipulasjonssikre. | Bestem hvilke handlinger i demoen som bør logges eller kvitteres. |

Leksjonene 16 og 17 er listet i hoved-README som kommer snart. Legg dem til i
studieplanen din når innholdet er tilgjengelig.

## Viktige ideer på nybegynnervennlig språk

### Verktøy

Et verktøy er noe agenten kan kalle for å gjøre arbeid utenfor modellen. Et godt verktøy
har et klart navn, en smal oppgave, typede input, forutsigbar output, og en trygg måte
å feile på.

For kursassistent-demoen kan et verktøy være:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG og kunnskap

RAG hjelper agenten med å svare ut fra kildemateriale istedenfor å gjette. I dette
kurset kan kildematerialet være leksjons-README-filer, kodeeksempler eller eksterne
ressurser lenket fra leksjonene.

Bruk RAG når svaret bør være basert på dokumenter, data eller nåværende
prosjektfiler.

### Planlegging

Planlegging er nyttig når forespørselen har mer enn ett steg. Hold planer korte og
synlige nok til at en utvikler eller bruker kan inspisere dem.

For demoen kan en plan være:

1. Finn leksjoner relatert til verktøybruk.
2. Oppsummer de mest relevante leksjonene.
3. Anbefal en øvelse.

### Kontekst

Kontekst er hva modellen ser akkurat nå. For lite kontekst kan gjøre at agenten
går glipp av viktige detaljer. For mye kontekst kan gjøre agenten tregere, dyrere,
eller lettere å forvirre.

God konsteksteknikk betyr å velge riktig informasjon til neste modellkall.

### Minne

Minne er informasjon lagret for senere bruk. Ikke lagre alt. Lagre informasjon
bare når den er nyttig, trygg, og lett å oppdatere eller slette.

For eksempel kan det være nyttig å huske "eleven foretrekker Python-eksempler".
Å huske sensitive personopplysninger er vanligvis ikke lurt.

### Evaluering og observasjon

Evaluering spør: gjorde agenten det riktige?

Observasjon spør: kan vi se hvordan det skjedde?

For produksjonsagenter, følg med på modellkall, verktøykall, hentet kontekst,
ventetid, kostnad, feil, og brukertilbakemeldinger.

### Tillit og sikkerhet

Pålitelige agenter trenger mer enn en hjelpsom prompt. Bruk minst-mulig-privilegium-verktøy,
menneskelig godkjenning for handlinger med stor effekt, datautskjæring der det trengs, og logger eller
kvitteringer for handlinger som må kunne revideres.

## En 15-minutters gjennomgangsrutine

Bruk denne rutinen etter hver leksjon:

1. **Oppsummer leksjonen med én setning.**
2. **Navngi den nye agentfunksjonen.** For eksempel: verktøybruk, henting,
   planlegging, minne, observasjon, eller sikkerhet.
3. **Legg den til kursassistent-demoen.** Hva endrer seg i demoen nå?
4. **Finn risikoen.** Hva kan gå galt hvis denne funksjonen misbrukes?
5. **Skriv ett testspørsmål.** Hvordan vil du sjekke at agenten oppfører seg riktig?

## Rask selvkontroll

Før du går videre, prøv å svare på disse spørsmålene:

1. Hva kan en agent gjøre som en vanlig chatbot ikke kan gjøre alene?
2. Hvilket verktøy trenger agenten din først, og hvorfor?
3. Hvilken kunnskapskilde bør grunnlegge agentens svar?
4. Hvilken kontekst bør inkluderes i neste modellkall?
5. Hva bør agenten huske, og hva bør unngås å lagre?
6. Når bør agenten be om menneskelig godkjenning?
7. Hvilke logger, spor eller kvitteringer vil hjelpe deg å feilsøke eller revidere agenten senere?

## Forslått avsluttende øvelse

På slutten av kurset, bygg en liten agent som hjelper en elev å navigere i dette
arkivet.

Minimum versjon:

- Motta et tema fra brukeren.
- Finn de mest relevante leksjonene.
- Oppsummer hva man bør lese først.
- Foreslå én praktisk oppgave.
- Vis hvilke leksjonsfiler eller lenker som ble brukt.

Utvidet versjon:

- Husk elevens foretrukne programmeringsspråk.
- Bruk en enkel plan før du svarer.
- Legg til et selv-sjekk-steg før det endelige svaret.
- Loggfør verktøykall og hentede kilder.
- Be om bekreftelse før nettleser- eller UI-automatiseringsoppgaver.

Dette gir deg en liten, men realistisk måte å øve på verktøy, RAG, planlegging,
kontekst, minne, observasjon og tillit i ett prosjekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->