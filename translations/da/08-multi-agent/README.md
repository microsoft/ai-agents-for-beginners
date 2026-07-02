[![Multi-Agent Design](../../../translated_images/da/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik på billedet ovenfor for at se video af denne lektion)_

# Multi-agent designmønstre

Så snart du begynder at arbejde på et projekt, der involverer flere agenter, skal du overveje multi-agent designmønsteret. Det er dog ikke altid umiddelbart klart, hvornår man skal skifte til multi-agenter, og hvad fordelene er.

## Introduktion

I denne lektion søger vi at besvare følgende spørgsmål:

- Hvilke scenarier er multi-agenter anvendelige til?
- Hvad er fordelene ved at bruge multi-agenter frem for bare en enkelt agent, der udfører flere opgaver?
- Hvad er byggestenene til at implementere multi-agent designmønsteret?
- Hvordan får vi synlighed i, hvordan de flere agenter interagerer med hinanden?

## Læringsmål

Efter denne lektion bør du kunne:

- Identificere scenarier hvor multi-agenter er anvendelige
- Genkende fordelene ved at bruge multi-agenter frem for en enkelt agent.
- Forstå byggestenene til at implementere multi-agent designmønsteret.

Hvad er det større billede?

*Multi-agenter er et designmønster, som gør det muligt for flere agenter at arbejde sammen om at nå et fælles mål*.

Dette mønster er bredt anvendt i forskellige felter, herunder robotteknologi, autonome systemer og distribueret databehandling.

## Scenarier hvor multi-agenter er anvendelige

Så hvilke scenarier er et godt anvendelsestilfælde for at bruge multi-agenter? Svaret er, at der er mange scenarier, hvor anvendelsen af flere agenter er fordelagtigt især i følgende tilfælde:

- **Stort arbejdspres**: Store arbejdsmængder kan opdeles i mindre opgaver og tildeles forskellige agenter, hvilket muliggør parallel behandling og hurtigere færdiggørelse. Et eksempel på dette er i tilfælde af en stor databehandlingsopgave.
- **Komplekse opgaver**: Komplekse opgaver, som store arbejdsmængder, kan opdeles i mindre underopgaver og tildeles forskellige agenter, der hver specialiserer sig i et bestemt aspekt af opgaven. Et godt eksempel er i tilfælde af autonome køretøjer, hvor forskellige agenter håndterer navigation, forhindringsdetektion og kommunikation med andre køretøjer.
- **Forskellig ekspertise**: Forskellige agenter kan have divers ekspertise, hvilket gør dem i stand til at håndtere forskellige aspekter af en opgave mere effektivt end en enkelt agent. Et godt eksempel på dette er inden for sundhedspleje, hvor agenter kan håndtere diagnostik, behandlingsplaner og patientovervågning.

## Fordele ved at bruge multi-agenter frem for en enkelt agent

Et enkelt agentsystem kan fungere godt til simple opgaver, men til mere komplekse opgaver kan brugen af flere agenter give flere fordele:

- **Specialisering**: Hver agent kan specialisere sig i en specifik opgave. Mangel på specialisering i en enkelt agent betyder, at du har en agent, som kan alt, men som kan blive forvirret over, hvad den skal gøre, når den står over for en kompleks opgave. Den kan for eksempel ende med at udføre en opgave, som den ikke er bedst egnet til.
- **Skalerbarhed**: Det er nemmere at skalere systemer ved at tilføje flere agenter end ved at overbelaste en enkelt agent.
- **Fejltolerance**: Hvis en agent fejler, kan de andre fortsætte med at fungere, hvilket sikrer systemets pålidelighed.

Lad os tage et eksempel: Lad os booke en rejse for en bruger. Et enkelt agentsystem skulle håndtere alle aspekter af rejsebookingsprocessen, fra at finde fly til at booke hoteller og lejebiler. For at opnå dette med en enkelt agent, skulle agenten have værktøjer til at håndtere alle disse opgaver. Dette kunne føre til et komplekst og monolitisk system, som er svært at vedligeholde og skalere. Et multi-agent system kunne derimod have forskellige agenter specialiseret i at finde fly, booke hoteller og lejebiler. Det ville gøre systemet mere modulært, lettere at vedligeholde og skalerbart.

Sammenlign dette med et rejsebureau drevet som en familieejet butik versus et rejsebureau drevet som en franchise. Familiebutikken ville have en enkelt agent, der håndterede alle aspekter af rejsebookingsprocessen, mens franchisen ville have forskellige agenter, der håndterer forskellige aspekter af rejsebookingsprocessen.

## Byggesten til implementering af multi-agent designmønsteret

Før du kan implementere multi-agent designmønsteret, skal du forstå byggestenene, der udgør mønsteret.

Lad os gøre det mere konkret ved igen at kigge på eksemplet med booking af en rejse for en bruger. I dette tilfælde vil byggestenene omfatte:

- **Agentkommunikation**: Agenter til at finde fly, booke hoteller og lejebiler skal kommunikere og dele information om brugerens præferencer og begrænsninger. Du skal beslutte protokoller og metoder til denne kommunikation. Konkrement betyder det, at agenten, der finder fly, skal kommunikere med agenten, der booker hoteller, for at sikre, at hotellet er booket til samme datoer som flyet. Det betyder, at agenterne skal dele information om brugerens rejsedatoer, hvilket betyder, at du skal beslutte *hvilke agenter der deler info og hvordan de deler info*.
- **Koordinationsmekanismer**: Agenter skal koordinere deres handlinger for at sikre, at brugerens præferencer og begrænsninger overholdes. En brugerpræference kunne være, at de ønsker et hotel tæt på lufthavnen, mens en begrænsning kunne være, at lejebiler kun er tilgængelige i lufthavnen. Det betyder, at agenten, der booker hoteller, skal koordinere med agenten, der booker lejebiler, for at sikre, at brugerens præferencer og begrænsninger opfyldes. Det betyder, at du skal beslutte *hvordan agenterne koordinerer deres handlinger*.
- **Agentarkitektur**: Agenter skal have den interne struktur til at træffe beslutninger og lære af deres interaktioner med brugeren. Det betyder, at agenten, der finder fly, skal have den interne struktur til at træffe beslutninger om, hvilke fly der skal anbefales til brugeren. Det betyder, at du skal beslutte *hvordan agenterne træffer beslutninger og lærer af deres interaktioner med brugeren*. Eksempler på, hvordan en agent lærer og forbedrer sig, kunne være, at agenten til at finde fly bruger en maskinlæringsmodel til at anbefale fly til brugeren baseret på deres tidligere præferencer.
- **Synlighed i multi-agent interaktioner**: Du skal have synlighed i, hvordan de flere agenter interagerer med hinanden. Det betyder, at du skal have værktøjer og teknikker til at spore agentaktiviteter og -interaktioner. Dette kan være i form af logging- og overvågningsværktøjer, visualiseringsværktøjer og præstationsmålinger.
- **Multi-agent mønstre**: Der findes forskellige mønstre til implementering af multi-agent systemer, såsom centraliserede, decentrale og hybride arkitekturer. Du skal vælge det mønster, der bedst passer til dit brugsscenarie.
- **Menneske i loopet**: I de fleste tilfælde vil du have et menneske i loopet, og du skal instruere agenterne om, hvornår de skal bede om menneskelig indgriben. Dette kan være i form af en bruger, der beder om et specifikt hotel eller fly, som agenterne ikke har anbefalet, eller at bede om bekræftelse før booking af et fly eller hotel.

## Synlighed i multi-agent interaktioner

Det er vigtigt, at du har synlighed i, hvordan de flere agenter interagerer med hinanden. Denne synlighed er essentiel for fejlretning, optimering og sikring af systemets samlede effektivitet. For at opnå dette skal du have værktøjer og teknikker til at spore agentaktiviteter og -interaktioner. Dette kan være i form af logging- og overvågningsværktøjer, visualiseringsværktøjer og præstationsmålinger.

For eksempel, i tilfælde af booking af en rejse for en bruger, kunne du have et dashboard, der viser status for hver agent, brugerens præferencer og begrænsninger samt interaktionerne mellem agenterne. Dette dashboard kunne vise brugerens rejsedatoer, de fly, der anbefales af flyagenten, de hoteller, der anbefales af hotelagenten, og de lejebiler, der anbefales af lejebilagenten. Det ville give dig et klart overblik over, hvordan agenterne interagerer med hinanden, og om brugerens præferencer og begrænsninger bliver opfyldt.

Lad os se nærmere på hver af disse aspekter.

- **Logging- og overvågningsværktøjer**: Du vil have logging for hver handling, en agent udfører. En logpost kunne gemme information om agenten, der udførte handlingen, den udførte handling, tidspunktet for handlingen og resultatet af handlingen. Disse oplysninger kan derefter bruges til fejlretning, optimering og mere.

- **Visualiseringsværktøjer**: Visualiseringsværktøjer kan hjælpe dig med at se interaktionerne mellem agenter på en mere intuitiv måde. For eksempel kunne du have en graf, der viser informationsflowet mellem agenter. Dette kan hjælpe dig med at identificere flaskehalse, ineffektiviteter og andre problemer i systemet.

- **Præstationsmålinger**: Præstationsmålinger kan hjælpe dig med at spore effektiviteten af multi-agent systemet. For eksempel kunne du følge den tid, det tager at fuldføre en opgave, antallet af opgaver udført pr. tidsenhed og nøjagtigheden af anbefalingerne fra agenterne. Disse oplysninger kan hjælpe dig med at identificere forbedringsområder og optimere systemet.

## Multi-agent mønstre

Lad os dykke ned i nogle konkrete mønstre, vi kan bruge til at skabe multi-agent applikationer. Her er nogle interessante mønstre værd at overveje:

### Gruppchat

Dette mønster er nyttigt, når du ønsker at oprette en gruppechat-applikation, hvor flere agenter kan kommunikere med hinanden. Typiske anvendelsestilfælde for dette mønster inkluderer teamsamarbejde, kundesupport og sociale netværk.

I dette mønster repræsenterer hver agent en bruger i gruppechatten, og beskeder udveksles mellem agenter ved hjælp af en messaging-protokol. Agenterne kan sende beskeder til gruppechatten, modtage beskeder fra gruppechatten og svare på beskeder fra andre agenter.

Dette mønster kan implementeres ved hjælp af en centraliseret arkitektur, hvor alle beskeder rutes gennem en central server, eller en decentraliseret arkitektur, hvor beskeder udveksles direkte.

![Group chat](../../../translated_images/da/multi-agent-group-chat.ec10f4cde556babd.webp)

### Overdragelse

Dette mønster er nyttigt, når du ønsker at oprette en applikation, hvor flere agenter kan overdrage opgaver til hinanden.

Typiske anvendelsestilfælde for dette mønster inkluderer kundesupport, opgavestyring og workflow-automatisering.

I dette mønster repræsenterer hver agent en opgave eller et trin i en arbejdsgang, og agenter kan overdrage opgaver til andre agenter baseret på foruddefinerede regler.

![Hand off](../../../translated_images/da/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Samarbejdende filtrering

Dette mønster er nyttigt, når du ønsker at skabe en applikation, hvor flere agenter kan samarbejde om at lave anbefalinger til brugere.

Hvorfor du vil have flere agenter til at samarbejde er fordi hver agent kan have forskellig ekspertise og kan bidrage til anbefalingsprocessen på forskellige måder.

Lad os tage et eksempel, hvor en bruger ønsker en anbefaling om den bedste aktie at købe på børsen.

- **Brancheekspert**: En agent kunne være ekspert i en specifik branche.
- **Teknisk analyse**: En anden agent kunne være ekspert i teknisk analyse.
- **Fundamental analyse**: og en anden agent kunne være ekspert i fundamental analyse. Ved at samarbejde kan disse agenter give en mere omfattende anbefaling til brugeren.

![Recommendation](../../../translated_images/da/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Refusionsproces

Overvej et scenarie, hvor en kunde forsøger at få refusion for et produkt, der kan være ganske mange agenter involveret i denne proces, men lad os opdele det mellem agenter specielle for denne proces og generelle agenter, der kan bruges i andre processer.

**Agenter specifikke for refusionsprocessen**:

Følgende er nogle agenter, der kunne være involveret i refusionsprocessen:

- **Kundeagent**: Denne agent repræsenterer kunden og er ansvarlig for at igangsætte refusionsprocessen.
- **Sælgeragent**: Denne agent repræsenterer sælgeren og er ansvarlig for at behandle refusionen.
- **Betalingsagent**: Denne agent repræsenterer betalingsprocessen og er ansvarlig for at refundere kundens betaling.
- **Løsningsagent**: Denne agent repræsenterer løsningsprocessen og er ansvarlig for at løse eventuelle problemer, der opstår under refusionsprocessen.
- **Overholdelsesagent**: Denne agent repræsenterer overholdelsesprocessen og sikrer, at refusionsprocessen overholder regler og politikker.

**Generelle agenter**:

Disse agenter kan bruges af andre dele af din virksomhed.

- **Forsendelsesagent**: Denne agent repræsenterer forsendelsesprocessen og er ansvarlig for at sende produktet tilbage til sælgeren. Denne agent kan bruges både til refusionsprocessen og til generel forsendelse af et produkt via et køb for eksempel.
- **Feedback-agent**: Denne agent repræsenterer feedbackprocessen og er ansvarlig for at indsamle feedback fra kunden. Feedback kan ske når som helst og ikke kun under refusionsprocessen.
- **Eskaleringsagent**: Denne agent repræsenterer eskaleringsprocessen og er ansvarlig for at eskalere problemer til et højere supportniveau. Du kan bruge denne type agent til enhver proces, hvor du har brug for at eskalere et problem.
- **Notifikationsagent**: Denne agent repræsenterer notifikationsprocessen og er ansvarlig for at sende notifikationer til kunden på forskellige stadier af refusionsprocessen.
- **Analyseragent**: Denne agent repræsenterer analyseprocessen og er ansvarlig for at analysere data relateret til refusionsprocessen.
- **Revisionsagent**: Denne agent repræsenterer revisionsprocessen og sikrer, at refusionsprocessen udføres korrekt.
- **Rapporteringsagent**: Denne agent repræsenterer rapporteringsprocessen og er ansvarlig for at generere rapporter om refusionsprocessen.
- **Vidensagent**: Denne agent repræsenterer vidensprocessen og er ansvarlig for at opretholde en vidensbase med information relateret til refusionsprocessen. Denne agent kunne have viden både om refusioner og andre dele af din virksomhed.
- **Sikkerhedsagent**: Denne agent repræsenterer sikkerhedsprocessen og sikrer sikkerheden i refusionsprocessen.
- **Kvalitetsagent**: Denne agent repræsenterer kvalitetsprocessen og sikrer kvaliteten af refusionsprocessen.

Der er ganske mange agenter nævnt tidligere både for den specifikke refusionsproces, men også for de generelle agenter, der kan bruges i andre dele af din virksomhed. Forhåbentlig giver det dig en idé om, hvordan du kan beslutte, hvilke agenter du skal bruge i dit multi-agent system.

## Opgave

Design et multi-agent system til en kundesupportproces. Identificer de involverede agenter i processen, deres roller og ansvar, og hvordan de interagerer med hinanden. Overvej både agenter specifikke for kundesupportprocessen og generelle agenter, der kan bruges i andre dele af din virksomhed.
> Tænk dig om, før du læser den følgende løsning, du kan have brug for flere agenter, end du tror.

> TIP: Tænk over de forskellige faser i kundesupportprocessen, og overvej også agenter, der er nødvendige for ethvert system.

## Løsning

[Løsning](./solution/solution.md)

## Vidensprøver

Spørgsmål: Hvornår bør du overveje at bruge multi-agenter?

- [ ] A1: Når du har en lille arbejdsbyrde og en simpel opgave.
- [ ] A2: Når du har en stor arbejdsbyrde
- [ ] A3: Når du har en simpel opgave.

[Løsningsquiz](./solution/solution-quiz.md)

## Resume

I denne lektion har vi set på multi-agent designmønsteret, inklusive de scenarier, hvor multi-agenter er anvendelige, fordelene ved at bruge multi-agenter frem for en enkelt agent, byggeklodserne til implementering af multi-agent designmønsteret, og hvordan man får indsigt i, hvordan de flere agenter interagerer med hinanden.

### Har du flere spørgsmål om Multi-Agent Designmønsteret?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre elever, deltage i åbent hus og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework dokumentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentiske designmønstre</a>


## Forrige lektion

[Planlægningsdesign](../07-planning-design/README.md)

## Næste lektion

[Metakognition i AI-agenter](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->