[![Multi-agent design](../../../translated_images/da/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

# Multi-agent designmønstre

Så snart du begynder at arbejde på et projekt, der involverer flere agenter, skal du overveje multi-agent designmønsteret. Det er dog ikke altid umiddelbart klart, hvornår man skal skifte til multi-agenter, og hvad fordelene er.

## Introduktion

I denne lektion vil vi besvare følgende spørgsmål:

- Hvilke scenarier er multi-agenter anvendelige i?
- Hvad er fordelene ved at bruge multi-agenter fremfor blot en enkelt agent, der udfører flere opgaver?
- Hvad er byggestenene for implementering af multi-agent designmønsteret?
- Hvordan får vi synlighed i, hvordan de flere agenter interagerer med hinanden?

## Læringsmål

Efter denne lektion bør du kunne:

- Identificere scenarier hvor multi-agenter er anvendelige
- Genkende fordelene ved at bruge multi-agenter fremfor en enkelt agent.
- Forstå byggestenene for implementering af multi-agent designmønsteret.

Hvad er det store billede?

*Multi-agenter er et designmønster, der tillader flere agenter at arbejde sammen for at nå et fælles mål*.

Dette mønster anvendes bredt inden for forskellige felter, herunder robotik, autonome systemer og distribueret databehandling.

## Scenarier hvor multi-agenter er anvendelige

Hvilke scenarier egner sig så godt til brug af multi-agenter? Svaret er, at der er mange scenarier, hvor anvendelse af flere agenter er fordelagtigt især i følgende tilfælde:

- **Store arbejdsbyrder**: Store arbejdsbyrder kan opdeles i mindre opgaver og tildeles forskellige agenter, hvilket muliggør parallel behandling og hurtigere afslutning. Et eksempel på dette er ved en stor databehandlingsopgave.
- **Komplekse opgaver**: Komplekse opgaver, ligesom store arbejdsbyrder, kan brydes ned i mindre delopgaver og tildeles forskellige agenter, som hver specialiserer sig i en bestemt del af opgaven. Et godt eksempel på dette er autonome køretøjer, hvor forskellige agenter håndterer navigation, forhindringsregistrering og kommunikation med andre køretøjer.
- **Forskellig ekspertise**: Forskellige agenter kan have forskellig ekspertise, hvilket gør, at de kan håndtere forskellige aspekter af en opgave mere effektivt end en enkelt agent. Et godt eksempel på dette er inden for sundhedssektoren, hvor agenter kan håndtere diagnostik, behandlingsplaner og patientovervågning.

## Fordele ved at bruge multi-agenter fremfor en enkelt agent

Et enkelt agentsystem kan fungere godt for simple opgaver, men ved mere komplekse opgaver kan brugen af flere agenter give flere fordele:

- **Specialisering**: Hver agent kan specialisere sig i en bestemt opgave. Manglende specialisering i en enkelt agent betyder, at du har en agent, som kan gøre alt, men som kan blive forvirret over, hvad den skal gøre, når den står over for en kompleks opgave. Den kan for eksempel ende med at udføre en opgave, den ikke er bedst egnet til.
- **Skalerbarhed**: Det er nemmere at skalere systemer ved at tilføje flere agenter fremfor at overbelaste en enkelt agent.
- **Fejltolerance**: Hvis en agent fejler, kan de andre fortsætte med at fungere, hvilket sikrer systemets pålidelighed.

Lad os tage et eksempel, lad os booke en rejse for en bruger. Et enkelt agentsystem skulle håndtere alle aspekter af rejsebookingsprocessen, fra at finde fly til at booke hoteller og lejebiler. For at opnå dette med en enkelt agent, skulle agenten have værktøjer til at håndtere alle disse opgaver. Det kunne føre til et komplekst og monolitisk system, der er svært at vedligeholde og skalere. Et multi-agent system kunne derimod have forskellige agenter specialiseret i at finde fly, booke hoteller og lejebiler. Dette ville gøre systemet mere modulært, lettere at vedligeholde og skalerbart.

Sammenlign dette med et rejsebureau drevet som en familiebutik versus et rejsebureau drevet som en franchise. Familiebutikken ville have en enkelt agent, der håndterer alle aspekter af rejsebookingsprocessen, mens franchisen ville have forskellige agenter, der håndterer forskellige aspekter af rejsebookingsprocessen.

## Byggesten for implementering af multi-agent designmønsteret

Før du kan implementere multi-agent designmønsteret, skal du forstå byggestenene, der udgør mønsteret.

Lad os gøre dette mere konkret ved igen at kigge på eksemplet med at booke en rejse for en bruger. I dette tilfælde vil byggestenene omfatte:

- **Agentkommunikation**: Agenter til at finde fly, booke hoteller og lejebiler skal kommunikere og dele oplysninger om brugerens præferencer og begrænsninger. Du skal beslutte protokoller og metoder for denne kommunikation. Konkrete eksempler er, at agenten for fly skal kommunikere med agenten for hotelbooking for at sikre, at hotellet bookes for samme datoer som flyet. Det betyder, at agenterne skal dele oplysninger om brugerens rejsedatoer, hvilket betyder, at du skal beslutte *hvilke agenter der deler info og hvordan de deler info*.
- **Koordinationsmekanismer**: Agenter skal koordinere deres handlinger for at sikre, at brugerens præferencer og begrænsninger opfyldes. En brugerpræference kunne være, at de ønsker et hotel tæt på lufthavnen, mens en begrænsning kunne være, at lejebiler kun er tilgængelige i lufthavnen. Det betyder, at agenten for hotelbooking skal koordinere med agenten for booking af lejebiler for at sikre, at brugerens præferencer og begrænsninger opfyldes. Dette betyder, at du skal beslutte *hvordan agenterne koordinerer deres handlinger*.
- **Agentarkitektur**: Agenter skal have den interne struktur til at træffe beslutninger og lære af deres interaktioner med brugeren. Det betyder, at agenten for fly skal have den interne struktur til at træffe beslutninger om, hvilke fly der skal anbefales til brugeren. Dette betyder, at du skal beslutte *hvordan agenterne træffer beslutninger og lærer af deres interaktioner med brugeren*. Eksempler på, hvordan en agent lærer og forbedres, kunne være, at agenten for fly kunne bruge en maskinlæringsmodel til at anbefale fly til brugeren baseret på tidligere præferencer.
- **Synlighed i multi-agent interaktioner**: Du skal have synlighed i, hvordan de flere agenter interagerer med hinanden. Det betyder, at du skal have værktøjer og teknikker til at følge agentaktiviteter og interaktioner. Dette kan være i form af log- og overvågningsværktøjer, visualiseringsværktøjer og performancemål.
- **Multi-agent mønstre**: Der er forskellige mønstre til implementering af multi-agent systemer, såsom centraliserede, decentraliserede og hybride arkitekturer. Du skal vælge det mønster, der bedst passer til dit anvendelsestilfælde.
- **Menneske i løkken**: I de fleste tilfælde vil der være et menneske i løkken, og du skal instruere agenterne, hvornår de skal bede om menneskelig indgriben. Dette kan f.eks. være i form af, at en bruger anmoder om et specifikt hotel eller fly, som agenterne ikke har anbefalet, eller at brugeren skal bekræfte, før en fly- eller hotelbooking gennemføres.

## Synlighed i multi-agent interaktioner

Det er vigtigt, at du har synlighed i, hvordan de flere agenter interagerer med hinanden. Denne synlighed er essentiel for fejlfinding, optimering og sikring af systemets samlede effektivitet. For at opnå dette skal du have værktøjer og teknikker til at følge agentaktiviteter og interaktioner. Dette kan være i form af log- og overvågningsværktøjer, visualiseringsværktøjer og performancemål.

For eksempel, i tilfælde af at booke en rejse for en bruger, kunne du have et dashboard, der viser status for hver agent, brugerens præferencer og begrænsninger, samt interaktionerne mellem agenterne. Dette dashboard kunne vise brugerens rejsedatoer, de fly, som flyagenten anbefaler, de hoteller, som hotelagenten anbefaler, og lejebilerne, som lejebilagenten anbefaler. Dette ville give dig et klart overblik over, hvordan agenterne interagerer med hinanden, og om brugerens præferencer og begrænsninger bliver opfyldt.

Lad os se nærmere på hver af disse aspekter.

- **Lognings- og overvågningsværktøjer**: Du vil have logning for hver handling, en agent foretager. En logpost kan gemme information om den agent, der udførte handlingen, den udførte handling, tidspunktet for handlingen og resultatet af handlingen. Denne information kan så bruges til fejlfinding, optimering og mere.

- **Visualiseringsværktøjer**: Visualiseringsværktøjer kan hjælpe dig med at se interaktionerne mellem agenter på en mere intuitiv måde. For eksempel kunne du have en graf, der viser informationsstrømmen mellem agenter. Dette kan hjælpe dig med at identificere flaskehalse, ineffektiviteter og andre problemer i systemet.

- **Performancemål**: Performancemål kan hjælpe dig med at følge effektiviteten af multi-agent systemet. For eksempel kunne du følge den tid, det tager at fuldføre en opgave, antallet af opgaver fuldført pr. tidsenhed og nøjagtigheden af anbefalingerne fra agenterne. Denne information kan hjælpe dig med at identificere forbedringsområder og optimere systemet.

## Multi-agent mønstre

Lad os dykke ned i nogle konkrete mønstre, vi kan bruge til at skabe multi-agent apps. Her er nogle interessante mønstre, der er værd at overveje:

### Gruppchat

Dette mønster er nyttigt, når du ønsker at skabe en gruppechat-applikation, hvor flere agenter kan kommunikere med hinanden. Typiske brugstilfælde for dette mønster inkluderer teamsamarbejde, kundesupport og sociale netværk.

I dette mønster repræsenterer hver agent en bruger i gruppechatten, og meddelelser udveksles mellem agenter ved hjælp af en messaging-protokol. Agenterne kan sende beskeder til gruppechatten, modtage beskeder fra gruppechatten og svare på beskeder fra andre agenter.

Dette mønster kan implementeres ved hjælp af en centraliseret arkitektur, hvor alle beskeder rutes gennem en central server, eller en decentraliseret arkitektur, hvor beskeder udveksles direkte.

![Gruppchat](../../../translated_images/da/multi-agent-group-chat.ec10f4cde556babd.webp)

### Overdragelse

Dette mønster er nyttigt, når du ønsker at skabe en applikation, hvor flere agenter kan overdrage opgaver til hinanden.

Typiske brugstilfælde for dette mønster inkluderer kundesupport, opgavestyring og workflow-automatisering.

I dette mønster repræsenterer hver agent en opgave eller et trin i en arbejdsgang, og agenter kan overdrage opgaver til andre agenter baseret på foruddefinerede regler.

![Overdragelse](../../../translated_images/da/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Samarbejdende filtrering

Dette mønster er nyttigt, når du ønsker at skabe en applikation, hvor flere agenter kan samarbejde om at lave anbefalinger til brugere.

Årsagen til at have flere agenter, der samarbejder, er, at hver agent kan have forskellig ekspertise og kan bidrage til anbefalingsprocessen på forskellige måder.

Lad os tage et eksempel, hvor en bruger ønsker en anbefaling om den bedste aktie at købe på aktiemarkedet.

- **Branchens ekspert**: En agent kunne være ekspert i en specifik branche.
- **Teknisk analyse**: En anden agent kunne være ekspert i teknisk analyse.
- **Fundamental analyse**: og en tredje agent kunne være ekspert i fundamental analyse. Ved at samarbejde kan disse agenter give en mere omfattende anbefaling til brugeren.

![Anbefaling](../../../translated_images/da/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenarie: Refusionsproces

Overvej et scenarie, hvor en kunde forsøger at få en refusion for et produkt, der kan være ret mange agenter involveret i denne proces, men lad os opdele det mellem agenter specifikke for denne proces og generelle agenter, der kan bruges i andre processer.

**Agenter specifikke for refusionsprocessen**:

Følgende er nogle agenter, der kunne være involveret i refusionsprocessen:

- **Kundeagent**: Denne agent repræsenterer kunden og er ansvarlig for at indlede refusionsprocessen.
- **Sælgeragent**: Denne agent repræsenterer sælgeren og er ansvarlig for at behandle refusionen.
- **Betalingsagent**: Denne agent repræsenterer betalingsprocessen og er ansvarlig for at tilbagebetale kundens betaling.
- **Løsningsagent**: Denne agent repræsenterer løsningsprocessen og er ansvarlig for at løse eventuelle problemer, der opstår under refusionsprocessen.
- **Compliance-agent**: Denne agent repræsenterer compliance-processen og er ansvarlig for at sikre, at refusionsprocessen overholder regler og politikker.

**Generelle agenter**:

Disse agenter kan bruges af andre dele af din virksomhed.

- **Forsendelsesagent**: Denne agent repræsenterer forsendelsesprocessen og er ansvarlig for at sende produktet tilbage til sælgeren. Denne agent kan bruges både til refusionsprocessen og til generel forsendelse af et produkt ved f.eks. et køb.
- **Feedback-agent**: Denne agent repræsenterer feedbackprocessen og er ansvarlig for at indsamle feedback fra kunden. Feedback kan ske på ethvert tidspunkt og ikke kun under refusionsprocessen.
- **Eskaleringsagent**: Denne agent repræsenterer eskaleringsprocessen og er ansvarlig for at eskalere problemer til et højere supportniveau. Du kan bruge denne type agent til enhver proces, hvor du har brug for at eskalere et problem.
- **Notifikationsagent**: Denne agent repræsenterer notifikationsprocessen og er ansvarlig for at sende notifikationer til kunden på forskellige stadier af refusionsprocessen.
- **Analyseagent**: Denne agent repræsenterer analyseprocessen og er ansvarlig for at analysere data relateret til refusionsprocessen.
- **Revisionsagent**: Denne agent repræsenterer revisionsprocessen og er ansvarlig for at revidere refusionsprocessen for at sikre, at den bliver udført korrekt.
- **Rapporteringsagent**: Denne agent repræsenterer rapporteringsprocessen og er ansvarlig for at generere rapporter om refusionsprocessen.
- **Vidensagent**: Denne agent repræsenterer vidensprocessen og er ansvarlig for at vedligeholde en vidensbase med information relateret til refusionsprocessen. Denne agent kunne være vidende både om refusioner og andre dele af din virksomhed.
- **Sikkerhedsagent**: Denne agent repræsenterer sikkerhedsprocessen og er ansvarlig for at sikre sikkerheden i refusionsprocessen.
- **Kvalitetsagent**: Denne agent repræsenterer kvalitetsprocessen og er ansvarlig for at sikre kvaliteten af refusionsprocessen.

Der er ret mange agenter listet tidligere både for den specifikke refusionsproces men også for de generelle agenter, der kan bruges i andre dele af din virksomhed. Forhåbentlig giver dette dig en idé om, hvordan du kan beslutte, hvilke agenter du skal bruge i dit multi-agent system.

## Opgave

Design et multi-agent system for en kundesupportproces. Identificer de agenter, der er involveret i processen, deres roller og ansvar, og hvordan de interagerer med hinanden. Overvej både agenter specifikke for kundesupportprocessen og generelle agenter, der kan bruges i andre dele af din virksomhed.


> Tænk dig godt om, før du læser den følgende løsning, du kan få brug for flere agenter, end du tror.

> TIP: Overvej de forskellige faser i kundesupportprocessen, og tænk også på de agenter, der er nødvendige for ethvert system.

## Løsning

[Løsning](./solution/solution.md)

## Videnstjek

### Spørgsmål 1

Hvilket scenarie er den bedste pasform til et multi-agent system?

- [ ] A1: En support-bot besvarer almindelige spørgsmål ved hjælp af én vidensbase og et lille sæt værktøjer.
- [ ] A2: En refusionsworkflow kræver separate roller til svindel, betaling og overholdelse, hver med deres egne værktøjer, og deres resultater skal koordineres.
- [ ] A3: Den samme simple klassificeringsanmodning modtages tusindvis af gange i timen.

### Spørgsmål 2

Hvornår er en enkelt agent normalt det bedste valg?

- [ ] A1: Opgaven kan håndteres med ét sæt instruktioner og værktøjer uden specialistoverdragelser.
- [ ] A2: Agenten har adgang til mere end ét værktøj.
- [ ] A3: Workflowet kræver separate roller med forskellige tilladelser og uafhængige revisionsspor.

[Løsning quiz](./solution/solution-quiz.md)

## Resumé

I denne lektion har vi set på multi-agent designmønsteret, herunder de scenarier, hvor multi-agenter er anvendelige, fordelene ved at bruge multi-agenter frem for en enkelt agent, byggestenene til implementering af multi-agent designmønsteret, og hvordan man får indsigt i, hvordan de mange agenter interagerer med hinanden.

### Har du flere spørgsmål om Multi-Agent Designmønsteret?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at mødes med andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework-dokumentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentiske designmønstre</a>


## Forrige lektion

[Planlægning og design](../07-planning-design/README.md)

## Næste lektion

[Metakognition i AI-agenter](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->