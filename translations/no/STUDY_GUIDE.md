# AI-agenter for nybegynnere - Studieveiledning

Bruk denne veiledningen som en praktisk følgesvenn mens du går gjennom kurset. Den er
ikke ment å erstatte leksjonene. Den hjelper deg med å bestemme hvor du skal starte, hva du skal
se etter i hver leksjon, og hvordan du kan koble ideene sammen til en liten fungerende agent-
demo.

Hvis dette er første gangen du er her, start enkelt:

1. Les [Course Setup](./00-course-setup/README.md).
2. Fullfør leksjonene 01-06 i rekkefølge.
3. Ha én liten demoidé i tankene mens du lærer.
4. Etter hver leksjon, spør: "Hva kan agenten min gjøre nå som den ikke kunne
   gjøre før?"

## En enkel demo å ha i tankene

En god måte å lære om agenter på er å følge én demoidé gjennom hele kurset.

Eksempel-demo: **en kursassistent-agent**.

Brukeren spør:

> "Jeg vil lære hvordan agenter bruker verktøy. Finn de riktige leksjonene, oppsummer hva
> jeg bør lese først, og gi meg en kort øvelse."

En vanlig chatbot kan svare ut fra det den allerede vet. En agent kan gjøre mer:

1. **Les eller søk i kursfiler** for å finne de riktige leksjonene.
2. **Bruk verktøy** for å hente leksjonslenker, eksempler eller støttemateriell.
3. **Planlegg** en kort læringssti i stedet for å gi ett langt svar.
4. **Bruk kontekst** fra den pågående samtalen for å holde fokus på elevens
   mål.
5. **Husk nyttige preferanser** hvis applikasjonen støtter minne.
6. **Vis spor, henvisninger eller logger** slik at brukeren kan forstå hva som skjedde.
7. **Bruk sikringsmekanismer** før du tar risikable handlinger eller bruker sensitive data.

Når du studerer hver leksjon, kom tilbake til denne demoen og spør: hvilken ny
evne ville denne leksjonen lagt til?

## Hva du bygger mot

Innen slutten av kurset bør du kunne forklare og bygge agentsystemer
som kombinerer disse delene:

| Del | Enkel forklaring | I demoen |
|------|------------------------|-------------|
| Modell | Resonneringsmotoren som tolker brukerens forespørsel | Forstår at læreren vil ha leksjoner om bruk av verktøy |
| Verktøy | Funksjoner, API-er, filer, nettlesere eller tjenester agenten kan bruke | Søker i repoet eller henter leksjonsinnhold |
| Kunnskap | Dokumenter eller data brukt for å grunnfeste svaret | Kurs-README-filer og leksjonsmateriell |
| Kontekst | Informasjon inkludert i neste modellkall | Brukerens mål og resultater fra verktøy |
| Minne | Informasjon lagret for senere bruk | Læreren foretrekker praktiske Python-eksempler |
| Planlegging | Bryte et større mål ned i mindre steg | Finn leksjoner, oppsummer dem, foreslå praksis |
| Orkestrering | Rutearbeid over verktøy, trinn eller agenter | En planlegger kaller et søkeverktøy, deretter en oppsummerer |
| Tillit | Sikkerhet, evaluering og observabilitet | Logger verktøykall og spør før handlinger med stor påvirkning |

## Modeller og leverandører

Kurskodeeksemplene bruker **Microsoft Agent Framework (MAF)** og retter seg mot **Azure OpenAI Responses API** — den anbefalte API-en fremover, som kombinerer chattfullføringer, verktøyskall, multimodal input og tilstandsfulle samtaler i ett API-område. Du kobler til enten gjennom et **Microsoft Foundry**-prosjekt (med `FoundryChatClient`) eller direkte til Azure OpenAI (med `OpenAIChatClient`).

Når du jobber deg gjennom leksjonene, har du noen leverandøralternativer:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — hovedveien brukt gjennom leksjonene. Logg inn med `az login` for nøkkelfri Entra ID-autentisering.
- **Foundry Local** — kjør modeller fullstendig lokalt gjennom en OpenAI-kompatibel API (ingen sky, ingen API-nøkler). Ideelt for offline eller kostnadsfri eksperimentering. Se [Course Setup](./00-course-setup/README.md).
- **MiniMax** — en OpenAI-kompatibel leverandør med store kontekstmodeller, brukbar som en drop-in-alternativ.

> **Merk:** GitHub Models er utfaset (legges ned i juli 2026) og støtter ikke Responses API. Eksemplene er oppdatert til å bruke Azure OpenAI / Microsoft Foundry i stedet.

## Velg din læringsvei

Du kan ta hele kurset i rekkefølge, eller hoppe til en vei basert på hva du ønsker
å bygge.

| Hvis målet ditt er å... | Start med | Studer deretter |
|-----------------------|------------|------------|
| Forstå hva agenter er | 01, 02, 03 | 04, 05, 06 |
| Bygge en agent som bruker verktøy | 04 | 05, 07, 14 |
| Bygge en RAG-basert agent | 05 | 04, 06, 12 |
| Designe flertrinnede arbeidsflyter | 07 | 08, 09, 14 |
| Forstå fleragent-systemer | 08 | 07, 09, 11 |
| Forberede agenter for produksjon | 06, 10 | 12, 13, 18 |
| Utforske protokoller og nettleserautomatisering | 11, 15 | 10, 18 |

Tips: hvis du er ny med agenter, ikke hopp over leksjonene 01-06. De gir deg
vokabularet du trenger for resten av kurset.

## Leksjon-for-leksjon-veiledning

| Leksjon | Hva du lærer | Prøv dette etter leksjonen |
|--------|----------------|---------------------------|
| [01 - Intro til AI-agenter](./01-intro-to-ai-agents/README.md) | Hva som gjør en agent forskjellig fra en grunnleggende chatbot. | Forklar demoideen din som en agent, ikke bare en chatteapp. |
| [02 - Agentiske rammeverk](./02-explore-agentic-frameworks/README.md) | Hvordan rammeverk hjelper med modeller, verktøy, tilstand og arbeidsflyter. | Identifiser hvilke deler av demoen en rammeverk ville håndtert. |
| [03 - Agentiske designmønstre](./03-agentic-design-patterns/README.md) | Vanlige mønstre for design av agentadferd. | Skisser brukerreisen før du skriver kode. |
| [04 - Verktøybruk](./04-tool-use/README.md) | Hvordan agenter kaller verktøy for å hente data eller utføre handlinger. | Definer ett verktøy demoagenten din ville trengt. |
| [05 - Agentisk RAG](./05-agentic-rag/README.md) | Hvordan oppslag forankrer agentens svar i dokumenter eller data. | Bestem hvilken kunnskapskilde demoen din skal søke i. |
| [06 - Pålitelige agenter](./06-building-trustworthy-agents/README.md) | Hvordan legge til sikringsmekanismer, tilsyn og tryggere adferd. | Legg til én regel for når agenten skal spørre brukeren først. |
| [07 - Planleggingsdesign](./07-planning-design/README.md) | Hvordan agenter bryter større mål ned i mindre steg. | Skriv en tre-trinns plan for demoforespørselen din. |

| [08 - Multi-agent design](./08-multi-agent/README.md) | Når man bør dele arbeidet mellom spesialiserte agenter. | Bestem om demoen din trenger én agent eller flere. |
| [09 - Metakognisjon](./09-metacognition/README.md) | Hvordan agenter kan gjennomgå og forbedre sin egen produksjon. | Legg til en siste selvkontroll før agenten svarer. |
| [10 - AI-agenter i produksjon](./10-ai-agents-production/README.md) | Hva som endres når en agent går fra demo til produksjon. | List opp hva du ville overvåket: kvalitet, kostnad, ventetid, feil. |
| [11 - Agentiske protokoller](./11-agentic-protocols/README.md) | Hvordan protokoller kobler agenter til verktøy og andre agenter. | Identifiser hvor en standard protokoll kan gjøre integrasjonen enklere. |
| [12 - Kontekstengineering](./12-context-engineering/README.md) | Hvordan velge, trimme, isolere og håndtere kontekst. | Bestem hva som hører hjemme i prompten og hva som bør holdes ute. |
| [13 - Agentminne](./13-agent-memory/README.md) | Hvordan agenter kan lagre nyttig informasjon på tvers av interaksjoner. | Velg en trygg preferanse demoen din kunne huske. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Rammeverksspesifikke byggesteiner for agenter og arbeidsflyter, pluss hosting av LangChain/LangGraph-agenter på Microsoft Foundry. | Kartlegg demostegene dine til rammeverkskonsepter. |
| [15 - Datamaskinbrukagenter](./15-browser-use/README.md) | Hvordan agenter kan samhandle med nettleser- eller UI-flater, inkludert virkelige eksempler som Microsoft Project Opal. | Velg én nettleseroppgave som fortsatt bør kreve brukerbekreftelse. |
| [18 - Sikring av AI-agenter](./18-securing-ai-agents/README.md) | Hvordan gjøre agenters handlinger mer reviderbare og manipulasjonsbestandige. | Bestem hvilke handlinger i demoen din som skal logges eller kvitteres. |

Leksjonene 16 og 17 er listet opp i hoved-README som kommer snart. Legg dem til i din
studieplan når leksjonsinnholdet er tilgjengelig.

## Viktige ideer på nybegynnervennlig språk

### Verktøy

Et verktøy er noe agenten kan kalle for å gjøre arbeid utenfor modellen. Et godt verktøy
har et klart navn, et smalt arbeidsområde, typede innganger, forutsigbar utdata og en sikker måte
å feile på.

For kursassistent-demoen kan et verktøy være:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG og kunnskap

RAG hjelper agenten med å svare ut fra kildemateriale i stedet for å gjette. I dette
kurset kan det kildematerialet være leksjons-README-filer, kodeeksempler eller eksterne
ressurser lenket fra leksjonene.

Bruk RAG når svaret bør være forankret i dokumenter, data eller nåværende
prosjektfiler.

### Planlegging

Planlegging er nyttig når forespørselen har mer enn ett steg. Hold planer korte og
synlige nok for en utvikler eller bruker å inspisere.

For demoen kan en plan være:

1. Finn leksjoner relatert til verktøybruk.
2. Oppsummer de mest relevante leksjonene.
3. Anbefal én praksisoppgave.

### Kontekst

Kontekst er det modellen ser akkurat nå. For lite kontekst kan gjøre at agenten
overser viktige detaljer. For mye kontekst kan gjøre agenten tregere, dyrere,
eller lettere å forvirre.

God kontekstengineering betyr å velge riktig informasjon for neste modell

samtale.

### Minne

Minne er informasjon som lagres for senere bruk. Ikke lagre alt. Lagre informasjon
bare når den er nyttig, sikker, og enkel å oppdatere eller slette.

For eksempel kan det være nyttig å huske "at læreren foretrekker Python-eksempler".
Å huske sensitiv personlig informasjon er som regel ikke det.

### Evaluering og Observabilitet

Evaluering spør: gjorde agenten det rette?

Observabilitet spør: kan vi se hvordan det skjedde?

For produksjonsagenter, hold oversikt over modellanrop, verktøyanrop, hentet kontekst,
forsinkelse, kostnad, feil, og brukerfeedback.

### Tillit og Sikkerhet

Pålitelige agenter trenger mer enn et hjelpsomt prompt. Bruk minst privilegerte verktøy,
menneskelig godkjenning for handlinger med stor innvirkning, dataredigering der nødvendig,
og logger eller kvitteringer for handlinger som må kunne revideres.

## En 15-minutters Gjennomgangsrutine

Bruk denne rutinen etter hver leksjon:

1. **Oppsummer leksjonen i én setning.**
2. **Nevn den nye agentkapasiteten.** For eksempel: verktøybruk, henting,
   planlegging, minne, observabilitet, eller sikkerhet.
3. **Legg den til i kursassistentdemoen.** Hva endres i demoen nå?
4. **Finn risikoen.** Hva kan gå galt hvis denne kapasiteten misbrukes?
5. **Skriv ett testspørsmål.** Hvordan ville du sjekke at agenten oppfører seg riktig?

## Rask Egenkontroll

Før du går videre, prøv å svare på disse spørsmålene:

1. Hva kan en agent gjøre som en vanlig chatbot ikke kan gjøre alene?
2. Hvilket verktøy vil agenten din trenge først, og hvorfor?
3. Hvilken kunnskapskilde bør begrunne agentens svar?
4. Hvilken kontekst bør inkluderes i neste modellanrop?
5. Hva bør agenten huske, og hva bør unngås å lagre?
6. Når bør agenten be om menneskelig godkjenning?
7. Hvilke logger, spor, eller kvitteringer vil hjelpe deg med feilfinning eller revisjon senere?

## Foreslått Avsluttende Oppgave

På slutten av kurset, bygg en liten agent som hjelper en elev med å navigere i dette
depotet.

Minimum versjon:

- Ta imot et tema fra brukeren.
- Finn de mest relevante leksjonene.
- Oppsummer hva som bør leses først.
- Foreslå en praktisk oppgave.
- Vis hvilke leksjonsfiler eller lenker som ble brukt.

Utvidet versjon:

- Husk elevens foretrukne programmeringsspråk.
- Bruk en enkel plan før svar.
- Legg til et egenkontrollsteg før det endelige svaret.
- Logg verktøyanrop og hentede kilder.
- Be om bekreftelse før åpning av nettleser eller UI-automatisering.

Dette gir deg en liten, men realistisk måte å øve på verktøy, RAG, planlegging,
kontekst, minne, observabilitet, og tillit i ett prosjekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->