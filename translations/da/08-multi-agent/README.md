[![Multi-agent design](../../../translated_images/da/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik på billedet ovenfor for at se video af denne lektion)_

# Multi-agent designmønstre

Så snart du begynder at arbejde på et projekt, der involverer flere agenter, bliver du nødt til at overveje multi-agent designmønsteret. Det kan dog ikke være umiddelbart klart, hvornår man skal skifte til multi-agenter, og hvad fordelene er.

## Introduktion

I denne lektion forsøger vi at besvare følgende spørgsmål:

- Hvilke scenarier er multi-agenter anvendelige til?
- Hvad er fordelene ved at bruge multi-agenter i forhold til kun én enkelt agent, der udfører flere opgaver?
- Hvad er byggestenene til implementering af multi-agent designmønsteret?
- Hvordan får vi indsigt i, hvordan de flere agenter interagerer med hinanden?

## Læringsmål

Efter denne lektion bør du være i stand til at:

- Identificere scenarier, hvor multi-agenter er anvendelige
- Genkende fordelene ved at bruge multi-agenter frem for en enkelt agent
- Forstå byggestenene til implementering af multi-agent designmønsteret

Hvad er det større billede?

*Multi-agenter er et designmønster, der tillader flere agenter at arbejde sammen for at opnå et fælles mål*.

Dette mønster er bredt anvendt inden for forskellige områder, herunder robotteknologi, autonome systemer og distribueret databehandling.

## Scenarier hvor multi-agenter er anvendelige

Hvilke scenarier er gode anvendelsestilfælde for brug af multi-agenter? Svaret er, at der er mange scenarier, hvor det er gavnligt at ansætte flere agenter, især i følgende tilfælde:

- **Store arbejdsbyrder**: Store arbejdsbyrder kan opdeles i mindre opgaver og tildeles forskellige agenter, hvilket tillader parallel behandling og hurtigere afslutning. Et eksempel på dette er i tilfælde af en stor databehandlingsopgave.
- **Komplekse opgaver**: Komplekse opgaver, ligesom store arbejdsbyrder, kan opdeles i mindre underopgaver og tildeles forskellige agenter, som hver specialiserer sig i en bestemt del af opgaven. Et godt eksempel er i tilfælde af autonome køretøjer, hvor forskellige agenter styrer navigation, forhindringsdetektion og kommunikation med andre køretøjer.
- **Forskellig ekspertise**: Forskellige agenter kan have forskellig ekspertise, hvilket tillader dem at håndtere forskellige aspekter af en opgave mere effektivt end en enkelt agent. I dette tilfælde er et godt eksempel sundhedssektoren, hvor agenter kan håndtere diagnostik, behandlingsplaner og patientovervågning.

## Fordele ved at bruge multi-agenter i forhold til en enkelt agent

Et enkelt agentsystem kan fungere godt til simple opgaver, men til mere komplekse opgaver kan brug af flere agenter give flere fordele:

- **Specialisering**: Hver agent kan specialisere sig i en bestemt opgave. Manglende specialisering i en enkelt agent betyder, at agenten kan gøre alt, men måske bliver forvirret over, hvad der skal gøres, når den står over for en kompleks opgave. Den kan for eksempel ende med at udføre en opgave, som den ikke er bedst egnet til.
- **Skalerbarhed**: Det er nemmere at skalere systemer ved at tilføje flere agenter i stedet for at overbelaste en enkelt agent.
- **Fejltolerance**: Hvis en agent fejler, kan andre fortsætte med at fungere, hvilket sikrer systemets pålidelighed.

Lad os tage et eksempel: Lad os booke en rejse for en bruger. Et enkelt agentsystem skulle håndtere alle aspekter af rejsebookingprocessen, fra at finde fly til at booke hoteller og lejebiler. For at opnå dette med en enkelt agent skulle agenten have værktøjer til at håndtere alle disse opgaver. Dette kunne føre til et komplekst og monolitisk system, som er svært at vedligeholde og skalerbart. Et multi-agent system kunne derimod have forskellige agenter specialiseret i at finde fly, booke hoteller og lejebiler. Dette ville gøre systemet mere modulært, lettere at vedligeholde og skalerbart.

Sammenlign dette med et rejsebureau drevet som en lille lokal butik versus et rejsebureau drevet som en franchise. Den lille butik ville have en enkelt agent, der håndterer alle aspekter af rejsebookingprocessen, mens franchisen ville have forskellige agenter, der håndterer forskellige aspekter af rejsebookingprocessen.

## Byggesten til implementering af multi-agent designmønsteret

Før du kan implementere multi-agent designmønsteret, skal du forstå byggestenene, der udgør mønsteret.

Lad os gøre dette mere konkret ved igen at se på eksemplet med booking af en rejse for en bruger. I dette tilfælde ville byggestenene inkludere:

- **Agentkommunikation**: Agenter til at finde fly, booke hoteller og lejebiler skal kommunikere og dele information om brugerens præferencer og begrænsninger. Du skal beslutte protokollerne og metoderne for denne kommunikation. Hvad dette konkret betyder, er, at agenten til at finde fly skal kommunikere med agenten til booking af hoteller for at sikre, at hotellet er booket til de samme datoer som flyet. Det betyder, at agenterne skal dele oplysninger om brugerens rejsedatoer, hvilket betyder, at du skal beslutte *hvilke agenter der deler information og hvordan de deler information*.
- **Koordineringsmekanismer**: Agenterne skal koordinere deres handlinger for at sikre, at brugerens præferencer og begrænsninger opfyldes. En brugerpræference kan være, at de ønsker et hotel tæt på lufthavnen, mens en begrænsning kan være, at lejebiler kun er tilgængelige i lufthavnen. Det betyder, at agenten, der booker hotel, skal koordinere med agenten, der booker lejebiler, for at sikre, at brugerens præferencer og begrænsninger opfyldes. Det betyder, at du skal beslutte *hvordan agenterne koordinerer deres handlinger*.
- **Agentarkitektur**: Agenterne skal have en intern struktur for at træffe beslutninger og lære af deres interaktioner med brugeren. Det betyder, at agenten til at finde fly skal have en intern struktur for at træffe beslutninger om, hvilke fly der skal anbefales til brugeren. Det betyder, at du skal beslutte *hvordan agenterne træffer beslutninger og lærer af deres interaktioner med brugeren*. Eksempler på hvordan en agent lærer og forbedrer sig kunne være, at agenten til at finde fly kunne bruge en maskinlæringsmodel til at anbefale fly til brugeren baseret på deres tidligere præferencer.
- **Indsigt i multi-agent interaktioner**: Du skal have indsigt i, hvordan de flere agenter interagerer med hinanden. Det betyder, at du skal have værktøjer og teknikker til at spore agentaktiviteter og interaktioner. Dette kunne være i form af lognings- og overvågningsværktøjer, visualiseringsværktøjer og præstationsmålinger.
- **Multi-agent mønstre**: Der findes forskellige mønstre til implementering af multi-agent systemer, såsom centraliserede, decentraliserede og hybride arkitekturer. Du skal vælge det mønster, der passer bedst til dit brugstilfælde.
- **Menneske i løkken**: I de fleste tilfælde vil du have et menneske i løkken, og du skal instruere agenterne om, hvornår de skal bede om menneskelig indgriben. Dette kan være i form af en bruger, der spørger efter et specifikt hotel eller fly, som agenterne ikke har anbefalet, eller beder om bekræftelse, før de booker et fly eller hotel.

## Indsigt i multi-agent interaktioner

Det er vigtigt, at du har indsigt i, hvordan de flere agenter interagerer med hinanden. Denne indsigt er essentiel for at kunne fejlfinde, optimere og sikre systemets samlede effektivitet. For at opnå dette skal du have værktøjer og teknikker til at spore agentaktiviteter og interaktioner. Dette kan være i form af lognings- og overvågningsværktøjer, visualiseringsværktøjer og præstationsmålinger.

For eksempel, i tilfælde af booking en rejse for en bruger, kunne du have et dashboard, som viser status for hver agent, brugerens præferencer og begrænsninger, samt interaktionerne mellem agenterne. Dette dashboard kunne vise brugerens rejsedatoer, de fly, der anbefales af flyagenten, de hoteller, der anbefales af hotelagenten, og de lejebiler, der anbefales af lejebilagenten. Dette ville give dig et klart billede af, hvordan agenterne interagerer, og om brugerens præferencer og begrænsninger bliver opfyldt.

Lad os se nærmere på hver af disse aspekter.

- **Lognings- og overvågningsværktøjer**: Du ønsker at have logning for hver handling, en agent udfører. En logpost kunne gemme information om agenten, der tog handlingen, den udførte handling, tidspunktet for handlingen og resultatet af handlingen. Disse informationer kan derefter bruges til fejlretning, optimering og mere.
- **Visualiseringsværktøjer**: Visualiseringsværktøjer kan hjælpe dig med at se interaktionerne mellem agenter på en mere intuitiv måde. For eksempel kunne du have en graf, der viser informationsflowet mellem agenter. Dette kan hjælpe dig med at identificere flaskehalse, ineffektiviteter og andre problemer i systemet.
- **Præstationsmålinger**: Præstationsmålinger kan hjælpe dig med at spore effektiviteten af multi-agent systemet. For eksempel kunne du spore den tid, det tager at fuldføre en opgave, antallet af opgaver fuldført per tidsenhed og nøjagtigheden af de anbefalinger, agenterne laver. Disse informationer kan hjælpe dig med at identificere forbedringsområder og optimere systemet.

## Multi-agent mønstre

Lad os dykke ned i nogle konkrete mønstre, vi kan bruge til at skabe multi-agent apps. Her er nogle interessante mønstre værd at overveje:

### Gruppearbejde (Group chat)

Dette mønster er nyttigt, når du ønsker at skabe en gruppechat-applikation, hvor flere agenter kan kommunikere med hinanden. Typiske anvendelsestilfælde for dette mønster inkluderer teamsamarbejde, kundesupport og sociale netværk.

I dette mønster repræsenterer hver agent en bruger i gruppechatten, og beskeder udveksles mellem agenter ved hjælp af en messaging-protokol. Agenterne kan sende beskeder til gruppechatten, modtage beskeder fra gruppechatten og svare på beskeder fra andre agenter.

Dette mønster kan implementeres ved hjælp af en centraliseret arkitektur, hvor alle beskeder rutes gennem en central server, eller en decentraliseret arkitektur, hvor beskeder udveksles direkte.

![Group chat](../../../translated_images/da/multi-agent-group-chat.ec10f4cde556babd.webp)

### Overlevering (Hand-off)

Dette mønster er nyttigt, når du vil lave en applikation, hvor flere agenter kan overlevere opgaver til hinanden.

Typiske anvendelsestilfælde for dette mønster inkluderer kundesupport, opgavestyring og workflow-automatisering.

I dette mønster repræsenterer hver agent en opgave eller et trin i en arbejdsproces, og agenter kan overlevere opgaver til andre agenter baseret på foruddefinerede regler.

![Hand off](../../../translated_images/da/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Samarbejdende filtrering (Collaborative filtering)

Dette mønster er nyttigt, når du ønsker at lave en applikation, hvor flere agenter kan samarbejde om at lave anbefalinger til brugere.

Grunden til at have flere agenter til at samarbejde er, at hver agent kan have forskellig ekspertise og kan bidrage til anbefalingsprocessen på forskellige måder.

Lad os tage et eksempel, hvor en bruger ønsker en anbefaling af den bedste aktie at købe på aktiemarkedet.

- **Brancheekspert**: Én agent kunne være ekspert i en bestemt branche.
- **Teknisk analyse**: En anden agent kunne være ekspert i teknisk analyse.
- **Fundamental analyse**: Og en tredje agent kunne være ekspert i fundamental analyse. Ved at samarbejde kan disse agenter give en mere omfattende anbefaling til brugeren.

![Recommendation](../../../translated_images/da/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Refusionsproces

Overvej et scenarie, hvor en kunde forsøger at få refusion for et produkt, der kan være en del agenter involveret i denne proces, men lad os opdele det mellem agenter specifikke for denne proces og generelle agenter, der kan bruges i andre processer.

**Agenter specifikke for refusionsprocessen**:

Følgende er nogle agenter, der kunne være involveret i refusionsprocessen:

- **Kundeagent**: Denne agent repræsenterer kunden og er ansvarlig for at starte refusionsprocessen.
- **Sælgeragent**: Denne agent repræsenterer sælgeren og er ansvarlig for at behandle refusionen.
- **Betalingsagent**: Denne agent repræsenterer betalingsprocessen og er ansvarlig for at refundere kundens betaling.
- **Resolutionagent**: Denne agent repræsenterer løsningsprocessen og er ansvarlig for at løse eventuelle problemer, der opstår under refusionsprocessen.
- **Complianceagent**: Denne agent repræsenterer compliance-processen og er ansvarlig for at sikre, at refusionsprocessen overholder regler og politikker.

**Generelle agenter**:

Disse agenter kan bruges af andre dele af din virksomhed.

- **Forsendelsesagent**: Denne agent repræsenterer forsendelsesprocessen og er ansvarlig for at sende produktet tilbage til sælgeren. Denne agent kan bruges både til refusionsprocessen og til generel forsendelse af et produkt ved et køb for eksempel.
- **Feedbackagent**: Denne agent repræsenterer feedbackprocessen og er ansvarlig for at indsamle feedback fra kunden. Feedback kan gives når som helst og ikke kun under refusionsprocessen.
- **Eskaleringsagent**: Denne agent repræsenterer eskaleringsprocessen og er ansvarlig for at eskalere problemer til et højere supportniveau. Du kan bruge denne type agent til enhver proces, hvor du skal eskalere et problem.
- **Notifikationsagent**: Denne agent repræsenterer notifikationsprocessen og er ansvarlig for at sende beskeder til kunden på forskellige stadier i refusionsprocessen.
- **Analyseagent**: Denne agent repræsenterer analyseprocessen og er ansvarlig for at analysere data relateret til refusionsprocessen.
- **Revisionagent**: Denne agent repræsenterer revisionsprocessen og er ansvarlig for at revidere refusionsprocessen for at sikre, at den udføres korrekt.
- **Rapporteringsagent**: Denne agent repræsenterer rapporteringsprocessen og er ansvarlig for at generere rapporter om refusionsprocessen.
- **Vidensagent**: Denne agent repræsenterer vidensprocessen og er ansvarlig for at vedligeholde en vidensbase med information relateret til refusionsprocessen. Denne agent kunne have viden både om refusioner og andre dele af din virksomhed.
- **Sikkerhedsagent**: Denne agent repræsenterer sikkerhedsprocessen og er ansvarlig for at sikre sikkerheden i refusionsprocessen.
- **Kvalitetsagent**: Denne agent repræsenterer kvalitetsprocessen og er ansvarlig for at sikre kvaliteten af refusionsprocessen.

Der er ganske mange agenter listet ovenfor, både til den specifikke refusionsproces, men også til de generelle agenter, der kan bruges i andre dele af din virksomhed. Forhåbentlig giver dette dig en idé om, hvordan du kan beslutte, hvilke agenter du vil bruge i dit multi-agent system.

## Opgave

Design et multi-agent system til en kundesupportproces. Identificer de agenter, der er involveret i processen, deres roller og ansvar, og hvordan de interagerer med hinanden. Overvej både agenter specifikke for kundesupportprocessen og generelle agenter, der kan bruges i andre dele af din virksomhed.
> Tænk lidt over det, inden du læser den følgende løsning; du kan få brug for flere agenter, end du tror.

> TIP: Overvej de forskellige faser i kundesupportprocessen, og tænk også på agenter, der er nødvendige for ethvert system.

## Løsning

[Løsning](./solution/solution.md)

## Vidensprøver

Spørgsmål: Hvornår bør du overveje at bruge multi-agenter?

- [ ] A1: Når du har en lille arbejdsbyrde og en simpel opgave.
- [ ] A2: Når du har en stor arbejdsbyrde
- [ ] A3: Når du har en simpel opgave.

[Løsning quiz](./solution/solution-quiz.md)

## Resumé

I denne lektion har vi set på multi-agent designmønsteret, herunder scenarier hvor multi-agenter er anvendelige, fordelene ved at bruge multi-agenter frem for en enkelt agent, byggestenene i implementeringen af multi-agent designmønsteret, og hvordan man får indsigt i, hvordan de flere agenter interagerer med hinanden.

### Har du flere spørgsmål om Multi-Agent Designmønsteret?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre deltagere, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework dokumentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentiske designmønstre</a>


## Forrige lektion

[Planlæg design](../07-planning-design/README.md)

## Næste lektion

[Metakognition i AI-agenter](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog skal betragtes som den autoritative kilde. For væsentlige oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->