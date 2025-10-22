<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T15:38:10+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "da"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.da.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Multi-agent designmønstre

Så snart du begynder at arbejde på et projekt, der involverer flere agenter, skal du overveje multi-agent designmønsteret. Det er dog ikke altid umiddelbart klart, hvornår man skal skifte til multi-agenter, og hvilke fordele det giver.

## Introduktion

I denne lektion vil vi forsøge at besvare følgende spørgsmål:

- Hvilke scenarier er relevante for multi-agenter?
- Hvad er fordelene ved at bruge multi-agenter frem for én enkelt agent, der udfører flere opgaver?
- Hvad er byggestenene for at implementere multi-agent designmønsteret?
- Hvordan kan vi få indsigt i, hvordan de forskellige agenter interagerer med hinanden?

## Læringsmål

Efter denne lektion bør du kunne:

- Identificere scenarier, hvor multi-agenter er relevante.
- Genkende fordelene ved at bruge multi-agenter frem for en enkelt agent.
- Forstå byggestenene for at implementere multi-agent designmønsteret.

Hvad er det større perspektiv?

*Multi-agenter er et designmønster, der gør det muligt for flere agenter at arbejde sammen for at opnå et fælles mål.*

Dette mønster anvendes bredt inden for forskellige områder, herunder robotteknologi, autonome systemer og distribueret databehandling.

## Scenarier, hvor multi-agenter er relevante

Hvilke scenarier er gode eksempler på brugen af multi-agenter? Svaret er, at der er mange scenarier, hvor det er fordelagtigt at anvende flere agenter, især i følgende tilfælde:

- **Store arbejdsbyrder**: Store arbejdsbyrder kan opdeles i mindre opgaver og tildeles forskellige agenter, hvilket muliggør parallel behandling og hurtigere færdiggørelse. Et eksempel på dette er en stor databehandlingsopgave.
- **Komplekse opgaver**: Komplekse opgaver kan, ligesom store arbejdsbyrder, opdeles i mindre delopgaver og tildeles forskellige agenter, der hver især specialiserer sig i en bestemt del af opgaven. Et godt eksempel er autonome køretøjer, hvor forskellige agenter håndterer navigation, forhindringsdetektion og kommunikation med andre køretøjer.
- **Forskellig ekspertise**: Forskellige agenter kan have forskellig ekspertise, hvilket gør dem i stand til at håndtere forskellige aspekter af en opgave mere effektivt end en enkelt agent. Et godt eksempel er sundhedssektoren, hvor agenter kan håndtere diagnostik, behandlingsplaner og patientovervågning.

## Fordele ved at bruge multi-agenter frem for en enkelt agent

Et system med en enkelt agent kan fungere godt til simple opgaver, men til mere komplekse opgaver kan brugen af flere agenter give flere fordele:

- **Specialisering**: Hver agent kan specialisere sig i en bestemt opgave. Manglende specialisering i en enkelt agent betyder, at du har en agent, der kan alt, men som kan blive forvirret, når den står over for en kompleks opgave. Den kan for eksempel ende med at udføre en opgave, som den ikke er bedst egnet til.
- **Skalerbarhed**: Det er lettere at skalere systemer ved at tilføje flere agenter frem for at overbelaste en enkelt agent.
- **Fejltolerance**: Hvis én agent fejler, kan andre fortsætte med at fungere, hvilket sikrer systemets pålidelighed.

Lad os tage et eksempel: Lad os booke en rejse for en bruger. Et system med en enkelt agent skulle håndtere alle aspekter af rejsebookingsprocessen, fra at finde fly til at booke hoteller og lejebiler. For at opnå dette med en enkelt agent skulle agenten have værktøjer til at håndtere alle disse opgaver. Dette kunne føre til et komplekst og monolitisk system, der er svært at vedligeholde og skalere. Et multi-agent system kunne derimod have forskellige agenter, der er specialiseret i at finde fly, booke hoteller og lejebiler. Dette ville gøre systemet mere modulært, lettere at vedligeholde og skalerbart.

Sammenlign dette med et rejsebureau drevet som en lille familievirksomhed versus et rejsebureau drevet som en franchise. Familievirksomheden ville have en enkelt agent, der håndterer alle aspekter af rejsebookingsprocessen, mens franchisen ville have forskellige agenter, der håndterer forskellige aspekter af processen.

## Byggestenene for at implementere multi-agent designmønsteret

Før du kan implementere multi-agent designmønsteret, skal du forstå de byggesten, der udgør mønsteret.

Lad os gøre dette mere konkret ved igen at se på eksemplet med at booke en rejse for en bruger. I dette tilfælde ville byggestenene omfatte:

- **Agentkommunikation**: Agenter til at finde fly, booke hoteller og lejebiler skal kommunikere og dele information om brugerens præferencer og begrænsninger. Du skal beslutte dig for protokoller og metoder til denne kommunikation. Konkret betyder det, at agenten til at finde fly skal kommunikere med agenten til at booke hoteller for at sikre, at hotellet er booket til de samme datoer som flyet. Det betyder, at agenterne skal dele information om brugerens rejsedatoer, hvilket betyder, at du skal beslutte *hvilke agenter der deler information, og hvordan de deler information*.
- **Koordineringsmekanismer**: Agenter skal koordinere deres handlinger for at sikre, at brugerens præferencer og begrænsninger opfyldes. En brugerpræference kunne være, at de ønsker et hotel tæt på lufthavnen, mens en begrænsning kunne være, at lejebiler kun er tilgængelige i lufthavnen. Dette betyder, at agenten til at booke hoteller skal koordinere med agenten til at booke lejebiler for at sikre, at brugerens præferencer og begrænsninger opfyldes. Dette betyder, at du skal beslutte *hvordan agenterne koordinerer deres handlinger*.
- **Agentarkitektur**: Agenter skal have en intern struktur til at træffe beslutninger og lære af deres interaktioner med brugeren. Dette betyder, at agenten til at finde fly skal have en intern struktur til at træffe beslutninger om, hvilke fly der skal anbefales til brugeren. Dette betyder, at du skal beslutte *hvordan agenterne træffer beslutninger og lærer af deres interaktioner med brugeren*. Eksempler på, hvordan en agent lærer og forbedrer sig, kunne være, at agenten til at finde fly kunne bruge en maskinlæringsmodel til at anbefale fly til brugeren baseret på deres tidligere præferencer.
- **Synlighed i multi-agent interaktioner**: Du skal have synlighed i, hvordan de forskellige agenter interagerer med hinanden. Dette betyder, at du skal have værktøjer og teknikker til at spore agentaktiviteter og interaktioner. Dette kunne være i form af lognings- og overvågningsværktøjer, visualiseringsværktøjer og præstationsmålinger.
- **Multi-agent mønstre**: Der findes forskellige mønstre til at implementere multi-agent systemer, såsom centraliserede, decentraliserede og hybride arkitekturer. Du skal beslutte dig for det mønster, der passer bedst til din brugssag.
- **Menneske i loopet**: I de fleste tilfælde vil du have et menneske i loopet, og du skal instruere agenterne om, hvornår de skal bede om menneskelig indgriben. Dette kunne være i form af en bruger, der beder om et specifikt hotel eller fly, som agenterne ikke har anbefalet, eller beder om bekræftelse, før de booker et fly eller hotel.

## Synlighed i multi-agent interaktioner

Det er vigtigt, at du har synlighed i, hvordan de forskellige agenter interagerer med hinanden. Denne synlighed er afgørende for fejlfinding, optimering og sikring af systemets samlede effektivitet. For at opnå dette skal du have værktøjer og teknikker til at spore agentaktiviteter og interaktioner. Dette kunne være i form af lognings- og overvågningsværktøjer, visualiseringsværktøjer og præstationsmålinger.

For eksempel, i tilfældet med at booke en rejse for en bruger, kunne du have et dashboard, der viser status for hver agent, brugerens præferencer og begrænsninger samt interaktionerne mellem agenterne. Dette dashboard kunne vise brugerens rejsedatoer, de fly, der anbefales af flyagenten, de hoteller, der anbefales af hotelagenten, og de lejebiler, der anbefales af lejebilagenten. Dette ville give dig et klart overblik over, hvordan agenterne interagerer med hinanden, og om brugerens præferencer og begrænsninger bliver opfyldt.

Lad os se nærmere på hver af disse aspekter.

- **Lognings- og overvågningsværktøjer**: Du vil gerne have logning for hver handling, der udføres af en agent. En logindgang kunne gemme information om den agent, der udførte handlingen, handlingen, der blev udført, tidspunktet for handlingen og resultatet af handlingen. Disse oplysninger kan derefter bruges til fejlfinding, optimering og mere.

- **Visualiseringsværktøjer**: Visualiseringsværktøjer kan hjælpe dig med at se interaktionerne mellem agenter på en mere intuitiv måde. For eksempel kunne du have en graf, der viser informationsflowet mellem agenter. Dette kunne hjælpe dig med at identificere flaskehalse, ineffektivitet og andre problemer i systemet.

- **Præstationsmålinger**: Præstationsmålinger kan hjælpe dig med at spore effektiviteten af multi-agent systemet. For eksempel kunne du spore den tid, det tager at fuldføre en opgave, antallet af opgaver, der fuldføres pr. tidsenhed, og nøjagtigheden af de anbefalinger, der gives af agenterne. Disse oplysninger kan hjælpe dig med at identificere forbedringsområder og optimere systemet.

## Multi-agent mønstre

Lad os dykke ned i nogle konkrete mønstre, vi kan bruge til at skabe multi-agent applikationer. Her er nogle interessante mønstre, der er værd at overveje:

### Gruppechat

Dette mønster er nyttigt, når du vil skabe en gruppechat-applikation, hvor flere agenter kan kommunikere med hinanden. Typiske brugssager for dette mønster inkluderer team-samarbejde, kundesupport og sociale netværk.

I dette mønster repræsenterer hver agent en bruger i gruppechatten, og beskeder udveksles mellem agenter ved hjælp af en beskedprotokol. Agenterne kan sende beskeder til gruppechatten, modtage beskeder fra gruppechatten og svare på beskeder fra andre agenter.

Dette mønster kan implementeres ved hjælp af en centraliseret arkitektur, hvor alle beskeder dirigeres gennem en central server, eller en decentraliseret arkitektur, hvor beskeder udveksles direkte.

![Gruppechat](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.da.png)

### Overdragelse

Dette mønster er nyttigt, når du vil skabe en applikation, hvor flere agenter kan overdrage opgaver til hinanden.

Typiske brugssager for dette mønster inkluderer kundesupport, opgavestyring og workflow-automatisering.

I dette mønster repræsenterer hver agent en opgave eller et trin i et workflow, og agenter kan overdrage opgaver til andre agenter baseret på foruddefinerede regler.

![Overdragelse](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.da.png)

### Samarbejdende filtrering

Dette mønster er nyttigt, når du vil skabe en applikation, hvor flere agenter kan samarbejde om at give anbefalinger til brugere.

Hvorfor du ville have flere agenter til at samarbejde, er fordi hver agent kan have forskellig ekspertise og kan bidrage til anbefalingsprocessen på forskellige måder.

Lad os tage et eksempel, hvor en bruger ønsker en anbefaling om den bedste aktie at købe på aktiemarkedet.

- **Industrianalyse**: En agent kunne være ekspert i en specifik industri.
- **Teknisk analyse**: En anden agent kunne være ekspert i teknisk analyse.
- **Fundamental analyse**: Og en tredje agent kunne være ekspert i fundamental analyse. Ved at samarbejde kan disse agenter give en mere omfattende anbefaling til brugeren.

![Anbefaling](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.da.png)

## Scenario: Refunderingsproces

Overvej et scenarie, hvor en kunde forsøger at få en refundering for et produkt. Der kan være en del agenter involveret i denne proces, men lad os opdele det mellem agenter, der er specifikke for denne proces, og generelle agenter, der kan bruges i andre processer.

**Agenter specifikke for refunderingsprocessen**:

Følgende er nogle agenter, der kunne være involveret i refunderingsprocessen:

- **Kundeagent**: Denne agent repræsenterer kunden og er ansvarlig for at starte refunderingsprocessen.
- **Sælgeragent**: Denne agent repræsenterer sælgeren og er ansvarlig for at behandle refunderingen.
- **Betalingsagent**: Denne agent repræsenterer betalingsprocessen og er ansvarlig for at refundere kundens betaling.
- **Løsningsagent**: Denne agent repræsenterer løsningsprocessen og er ansvarlig for at løse eventuelle problemer, der opstår under refunderingsprocessen.
- **Compliance-agent**: Denne agent repræsenterer compliance-processen og er ansvarlig for at sikre, at refunderingsprocessen overholder regler og politikker.

**Generelle agenter**:

Disse agenter kan bruges af andre dele af din virksomhed.

- **Forsendelsesagent**: Denne agent repræsenterer forsendelsesprocessen og er ansvarlig for at sende produktet tilbage til sælgeren. Denne agent kan bruges både til refunderingsprocessen og til generel forsendelse af et produkt, for eksempel ved et køb.
- **Feedback-agent**: Denne agent repræsenterer feedback-processen og er ansvarlig for at indsamle feedback fra kunden. Feedback kan gives når som helst og ikke kun under refunderingsprocessen.
- **Eskaleringsagent**: Denne agent repræsenterer eskaleringsprocessen og er ansvarlig for at eskalere problemer til et højere supportniveau. Du kan bruge denne type agent til enhver proces, hvor du har brug for at eskalere et problem.
- **Notifikationsagent**: Denne agent repræsenterer notifikationsprocessen og er ansvarlig for at sende notifikationer til kunden på forskellige stadier af refunderingsprocessen.
- **Analyseringsagent**: Denne agent repræsenterer analyseprocessen og er ansvarlig for at analysere data relateret til refunderingsprocessen.
- **Revisionsagent**: Denne agent repræsenterer revisionsprocessen og er ansvarlig for at revidere refunderingsprocessen for at sikre, at den udføres korrekt.
- **Rapporteringsagent**: Denne agent repræsenterer rapporteringsprocessen og er ansvarlig for at generere rapporter om refunderingsprocessen.
- **Vidensagent**: Denne agent repræsenterer vidensprocessen og er ansvarlig for at vedligeholde en vidensbase med information relateret til refunderingsprocessen. Denne agent kan være vidende både om refunderinger og andre dele af din virksomhed.
- **Sikkerhedsagent**: Denne agent repræsenterer sikkerhedsprocessen og er ansvarlig for at sikre sikkerheden i refunderingsprocessen.
- **Kvalitetsagent**: Denne agent repræsenterer kvalitetsprocessen og er ansvarlig for at sikre kvaliteten af refunderingsprocessen.

Der er en del agenter nævnt ovenfor, både for den specifikke refunderingsproces og for de generelle agenter, der kan bruges i andre dele af din virksomhed. Forhåbentlig giver dette dig en idé om, hvordan du kan beslutte, hvilke agenter du vil bruge i dit multi-agent system.

## Opgave
Design et multi-agent system til en kundesupportproces. Identificer de agenter, der er involveret i processen, deres roller og ansvar, og hvordan de interagerer med hinanden. Overvej både agenter, der er specifikke for kundesupportprocessen, og generelle agenter, der kan bruges i andre dele af din virksomhed.

> Tænk over det, før du læser den følgende løsning – du har måske brug for flere agenter, end du tror.

> TIP: Tænk på de forskellige stadier i kundesupportprocessen og overvej også agenter, der er nødvendige for ethvert system.

## Løsning

[Løsning](./solution/solution.md)

## Vidensspørgsmål

Spørgsmål: Hvornår bør du overveje at bruge multi-agenter?

- [ ] A1: Når du har en lille arbejdsbyrde og en simpel opgave.
- [ ] A2: Når du har en stor arbejdsbyrde.
- [ ] A3: Når du har en simpel opgave.

[Løsningsquiz](./solution/solution-quiz.md)

## Resumé

I denne lektion har vi kigget på multi-agent designmønsteret, herunder de scenarier, hvor multi-agenter er relevante, fordelene ved at bruge multi-agenter frem for en enkelt agent, byggestenene til at implementere multi-agent designmønsteret, og hvordan man får indsigt i, hvordan de forskellige agenter interagerer med hinanden.

### Har du flere spørgsmål om Multi-Agent Designmønsteret?

Deltag i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortid og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- ## Forrige lektion

[Planlægningsdesign](../07-planning-design/README.md)

## Næste lektion

[Metakognition i AI-agenter](../09-metacognition/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.