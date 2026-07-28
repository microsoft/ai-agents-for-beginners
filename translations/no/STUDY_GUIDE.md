# AI-agenter for nybegynnere - Studieguide

Bruk denne guiden som en praktisk følgesvenn mens du går gjennom kurset. Den er
ikke ment å erstatte leksjonene. Den hjelper deg med å bestemme hvor du skal starte, hva du skal
se etter i hver leksjon, og hvordan du kan koble ideene sammen til en liten fungerende agent-
demo.

Hvis dette er din første gang her, start enkelt:

1. Les [Course Setup](./00-course-setup/README.md).
2. Fullfør leksjonene 01-06 i rekkefølge.
3. Ha én liten demoidé i tankene mens du lærer.
4. Etter hver leksjon, spør: "Hva kan agenten min gjøre nå som den ikke kunne gjøre
   før?"

## En enkel demo å ha i tankene

En god måte å lære om agenter på er å følge én demoidé gjennom kurset.

Eksempeldemo: **en assistentagent for kurset**.

Brukeren spør:

> "Jeg vil lære hvordan agenter bruker verktøy. Finn de riktige leksjonene, oppsummer hva
> jeg bør lese først, og gi meg en kort oppgave til praksis."

En vanlig chatbot kan svare ut fra det den allerede vet. En agent kan gjøre mer:

1. **Les eller søk i kursfiler** for å finne de riktige leksjonene.
2. **Bruk verktøy** for å hente leksjonslenker, eksempler eller støttemateriale.
3. **Planlegg** en kort læringssti i stedet for å gi ett langt svar.
4. **Bruk kontekst** fra den nåværende samtalen for å holde fokus på elevens
   mål.
5. **Husk nyttige preferanser** hvis applikasjonen støtter minne.
6. **Vis spor, referanser eller logger** slik at brukeren kan forstå hva som skjedde.
7. **Bruk sikkerhetsbarrierer** før du tar risikable handlinger eller bruker sensitiv data.

Når du studerer hver leksjon, kom tilbake til denne demoen og spør: hvilken ny evne
vil denne leksjonen legge til?

## Hva du bygger mot

Innen slutten av kurset bør du kunne forklare og bygge agentsystemer
som kombinerer disse delene:

| Del | Enkelt forklart | I demoen |
|------|------------------------|-------------|
| Modell | Resonneringsmotoren som tolker brukerens forespørsel | Forstår at læreren ønsker leksjoner om verktøybruk |
| Verktøy | Funksjoner, APIer, filer, nettlesere eller tjenester agenten kan bruke | Søker i depotet eller henter leksjonsinnhold |
| Kunnskap | Dokumenter eller data som underbygger svaret | Kurs-README-filer og leksjonsmateriale |
| Kontekst | Informasjon som inkluderes i neste modellkall | Brukerens mål og resultatene fra verktøyene |
| Minne | Informasjon lagret for senere bruk | Læreren foretrekker praktiske Python-eksempler |
| Planlegging | Å dele opp et større mål i mindre steg | Finne leksjoner, oppsummere dem, foreslå øving |
| Orkestrering | Ruting av arbeid over verktøy, steg eller agenter | En planlegger kaller et søkeverktøy, så en oppsummerer |
| Tillit | Sikkerhet, evaluering og observasjon | Logger verktøysamtaler og spør før handlinger med stor påvirkning |

## Modeller og tilbydere

Kodeeksemplene i kurset bruker **Microsoft Agent Framework (MAF)** og retter seg mot **Azure OpenAI Responses API** — den anbefalte API-en fremover, som kombinerer chat-svar, verktøysamtaler, multimodal input og tilstandsbevarende samtaler i ett API-grensesnitt. Du kobler enten gjennom et **Microsoft Foundry**-prosjekt (med `FoundryChatClient`) eller direkte til Azure OpenAI (med `OpenAIChatClient`).

Mens du jobber deg gjennom leksjonene, har du noen tilbydere å velge mellom:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — hovedveien brukt i leksjonene. Logg inn med `az login` for nøkkelfri Entra ID-autentisering.
- **Foundry Local** — kjør modeller helt på enheten gjennom et OpenAI-kompatibelt API (ingen skytjenester, ingen API-nøkler). Ideelt for offline eller kostnadsfrie eksperimenter. Se [Course Setup](./00-course-setup/README.md).
- **MiniMax** — en OpenAI-kompatibel tilbyder med modeller for stor kontekst, kan brukes som en drop-in-alternativ.

> **Merk:** GitHub Models er utfaset (pensjoneres i juli 2026) og støtter ikke Responses API. Eksemplene er oppdatert til å bruke Azure OpenAI / Microsoft Foundry i stedet.

## Velg din læringssti

Du kan ta hele kurset i rekkefølge, eller hoppe til en sti basert på hva du ønsker
å bygge.

| Hvis målet ditt er å... | Start med | Så studer |
|-----------------------|------------|------------|
| Forstå hva agenter er | 01, 02, 03 | 04, 05, 06 |
| Bygge en agent som bruker verktøy | 04 | 05, 07, 14 |
| Bygge en RAG-basert agent | 05 | 04, 06, 12 |
| Designe arbeidsflyter med flere steg | 07 | 08, 09, 14 |
| Forstå multi-agent systemer | 08 | 07, 09, 11 |
| Forberede agenter for produksjon | 06, 10 | 12, 13, 16, 18 |
| Distribuere og skalere agenter på Foundry | 10, 16 | 06, 13, 18 |
| Bygge lokale / offline-første agenter | 17 | 04, 05, 11 |
| Utforske protokoller og nettleserautomatisering | 11, 15 | 10, 18 |

Tips: hvis du er ny til agenter, ikke hopp over leksjonene 01-06. De gir deg
vokabularet du trenger for resten av kurset.

## Leksjon-for-leksjon guide

| Leksjon | Hva du lærer | Prøv dette etter leksjonen |
|--------|----------------|---------------------------|
| [01 - Intro til AI-agenter](./01-intro-to-ai-agents/README.md) | Hva som gjør en agent annerledes enn en vanlig chatbot. | Forklar demoideen din som en agent, ikke bare en chatteapp. |
| [02 - Agentiske rammeverk](./02-explore-agentic-frameworks/README.md) | Hvordan rammeverk hjelper med modeller, verktøy, tilstand og arbeidsflyter. | Identifiser hvilke deler av demoen din et rammeverk ville håndtere. |
| [03 - Agentiske designmønstre](./03-agentic-design-patterns/README.md) | Vanlige mønstre for å designe agentoppførsel. | Skissér brukerreisen før du skriver kode. |
| [04 - Bruk av verktøy](./04-tool-use/README.md) | Hvordan agenter kaller verktøy for å hente data eller utføre handlinger. | Definer ett verktøy agentdemoen din ville trengt. |
| [05 - Agentisk RAG](./05-agentic-rag/README.md) | Hvordan innhenting fundamenterer agentsvar i dokumenter eller data. | Bestem hvilken kunnskapskilde demoen din bør søke i. |

| [06 - Pålitelige agenter](./06-building-trustworthy-agents/README.md) | Hvordan legge til sikkerhetsmekanismer, tilsyn og tryggere oppførsel. | Legg til en regel for når agenten skal spørre brukeren først. |
| [07 - Planleggingsdesign](./07-planning-design/README.md) | Hvordan agenter deler opp større mål i mindre steg. | Skriv en tre-trinns plan for demoforespørselen din. |
| [08 - Design for flere agenter](./08-multi-agent/README.md) | Når man bør fordele arbeid på tvers av spesialiserte agenter. | Bestem om demoen din trenger én agent eller flere. |
| [09 - Metakognisjon](./09-metacognition/README.md) | Hvordan agenter kan gjennomgå og forbedre egen output. | Legg til en siste egenkontroll før agenten svarer. |
| [10 - AI-agenter i produksjon](./10-ai-agents-production/README.md) | Hva som endrer seg når en agent går fra demo til produksjon. | List opp hva du ville overvåket: kvalitet, kostnad, ventetid, feil. |
| [11 - Agentiske protokoller](./11-agentic-protocols/README.md) | Hvordan protokoller kobler agenter til verktøy og andre agenter. | Identifiser hvor en standardprotokoll kan forenkle integrasjonen. |
| [12 - Kontekst-engineering](./12-context-engineering/README.md) | Hvordan velge, trimme, isolere og håndtere kontekst. | Bestem hva som hører hjemme i prompten og hva som bør holdes utenfor. |
| [13 - Agentminne](./13-agent-memory/README.md) | Hvordan agenter kan lagre nyttig informasjon på tvers av interaksjoner. | Velg ett sikkert preferansepunkt demoen din kan huske. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Rammeverksspesifikke byggeklosser for agenter og arbeidsflyter, pluss hosting av LangChain/LangGraph-agenter på Microsoft Foundry. | Kartlegg demoens steg til rammeverkskonsepter. |
| [15 - Agenter for databruk](./15-browser-use/README.md) | Hvordan agenter kan interagere med nettleser- eller UI-flater, inkludert virkelige eksempler som Microsoft Project Opal. | Velg én nettleseroppgave som fortsatt bør kreve brukergodkjenning. |
| [16 - Distribuering av skalerbare agenter](./16-deploying-scalable-agents/README.md) | Hvordan ta en agent fra prototype til en skalerbar, observerbar produksjonsdistribuering på Microsoft Foundry (hostede agenter, modellruting, caching, evalueringsporter, røyktester). | List produksjonsutfordringer demoen din fortsatt trenger: hosting, ruting, kostnad, evaluering. |
| [17 - Lage lokale AI-agenter](./17-creating-local-ai-agents/README.md) | Hvordan bygge lokal-første agenter som kjører helt på din maskin med Foundry Local og Qwen (lokale verktøy, lokal RAG, lokal MCP). | Bestem hvilke deler av demoen som bør forbli private og kjøre lokalt. |
| [18 - Sikring av AI-agenter](./18-securing-ai-agents/README.md) | Hvordan gjøre agenthandlinger mer reviderbare og manipulasjonssikre. | Bestem hvilke handlinger i demoen som bør logges eller kvitteres. |

## Validere distribuerte agenter med røyktester

Når du distribuerer en agent (Leksjon 16), er en **røyktest** den billigste første
sjekken for at distribusjonen faktisk svarer. Dette depotet leverer kjøreklare
kataloger under [tests/](./tests/README.md) for de deployerbare agentene i Leksjonene
01, 04, 05, og 16, koblet til

[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Handling. Kjør dem fra **Actions**-fanen etter å ha distribuert leksonens agent.
Røyktester er en første port — offline- og online-evaluering (Leksjoner 10 og 16)
forteller deg hvor *god* agenten er.

## Nøkkelideer på nybegynnervennlig språk

### Verktøy

Et verktøy er noe agenten kan kalle for å gjøre arbeid utenfor modellen. Et godt verktøy
har et klart navn, et smalt oppdrag, typede inndata, forutsigbart utdata og en trygg måte
å feile på.

For kursassistentdemoen kan et verktøy være:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG og kunnskap

RAG hjelper agenten med å svare ut fra kildemateriale i stedet for å gjette. I dette
kurset kan det kildematerialet være leksjons-README-filer, kodeeksempler eller eksterne
ressurser lenket fra leksjonene.

Bruk RAG når svaret bør være forankret i dokumenter, data eller gjeldende
prosjektfiler.

### Planlegging

Planlegging er nyttig når forespørselen har mer enn ett steg. Hold planer korte og
synlige nok til at en utvikler eller bruker kan inspisere dem.

For demoen kan en plan være:

1. Finn leksjoner relatert til bruk av verktøy.
2. Oppsummer de mest relevante leksjonene.
3. Anbefal en øvingsoppgave.

### Kontekst

Kontekst er det modellen ser akkurat nå. For lite kontekst kan gjøre at agenten
mister viktige detaljer. For mye kontekst kan gjøre agenten tregere, dyrere,
eller lettere forvirret.

God kontekstdesign betyr å velge riktig informasjon for neste modellkall.


### Minne

Minne er informasjon lagret for senere. Ikke lagre alt. Lagre informasjon
bare når det er nyttig, trygt og enkelt å oppdatere eller slette.

For eksempel kan det være nyttig å huske at "brukeren foretrekker Python-eksempler".
Å huske sensitiv personlig informasjon er vanligvis ikke lurt.

### Evaluering og observerbarhet

Evaluering spør: gjorde agenten det rette?

Observerbarhet spør: kan vi se hvordan det skjedde?

For produksjonsagenter, følg med på modellkall, verktøykall, hentet kontekst,
latens, kostnad, feil og brukerfeedback.

### Tillit og sikkerhet

Pålitelige agenter trenger mer enn en hjelpsom prompt. Bruk minst mulig privilegerte verktøy,
menneskelig godkjenning for handlinger med stor innvirkning, dataredigering der det trengs, og logger eller
kvitteringer for handlinger som må revideres.

## En 15-minutters gjennomgangsrutine

Bruk denne rutinen etter hver leksjon:

1. **Oppsummer leksjonen i én setning.**
2. **Navngi den nye agentkapasiteten.** For eksempel: verktøybruk, henting,
   planlegging, minne, observerbarhet eller sikkerhet.
3. **Legg den til kursassistentdemoen.** Hva endrer seg i demoen nå?
4. **Finn risikoen.** Hva kan gå galt hvis denne kapasiteten misbrukes?
5. **Skriv ett testspørsmål.** Hvordan ville du sjekke at agenten oppfører seg bra?

## Rask egenkontroll

Før du går videre, prøv å svare på disse spørsmålene:

1. Hva kan en agent gjøre som en vanlig chatbot ikke kan gjøre alene?
2. Hvilket verktøy trenger agenten din først, og hvorfor?
3. Hvilken kunnskapskilde bør forankre agentens svar?
4. Hvilken kontekst bør inkluderes i neste modellkall?

5. Hva bør agenten huske, og hva bør den unngå å lagre?
6. Når bør agenten be om godkjenning fra et menneske?
7. Hvilke logger, spor eller kvitteringer vil hjelpe deg med å feilsøke eller revidere agenten senere?


## Foreslått avsluttende oppgave

På slutten av kurset, lag en liten agent som hjelper en lærende med å navigere i dette
depotet.

Minimum versjon:

- Ta imot et emne fra brukeren.
- Finn de mest relevante leksjonene.
- Oppsummer hva som skal leses først.
- Foreslå én praktisk oppgave.
- Vis hvilke leksjonsfiler eller lenker som ble brukt.

Utvidet versjon:

- Husk brukerens foretrukne programmeringsspråk.
- Bruk en enkel plan før du svarer.
- Legg til et selvkontrollsteg før det endelige svaret.
- Loggfør verktøysanrop og hentede kilder.
- Be om bekreftelse før du åpner nettleser eller UI-automatiseringsoppgaver.

Dette gir deg en liten, men realistisk måte å øve på verktøy, RAG, planlegging,
kontekst, hukommelse, overvåking og tillit i ett prosjekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->