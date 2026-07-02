# AI-agenter for begyndere - Studiemateriale

Brug denne guide som en praktisk ledsager, mens du bevæger dig igennem kurset. Den
er ikke ment som en erstatning for lektionerne. Den hjælper dig med at beslutte, hvor du skal starte,
hvad du skal kigge efter i hver lektion, og hvordan du forbinder ideerne til en lille fungerende agent-demo.

Hvis det er første gang, du er her, så start simpelt:

1. Læs [Course Setup](./00-course-setup/README.md).
2. Gennemfør lektionerne 01-06 i rækkefølge.
3. Hav en lille demo-idé i tankerne, mens du lærer.
4. Efter hver lektion, spørg: "Hvad kan min agent gøre nu, som den ikke kunne gøre
   før?"

## En simpel demo at have i tankerne

En god måde at lære agenter på er at følge én demo-idé gennem hele kurset.

Eksempeldemo: **en kursushjælper-agent**.

Brugeren spørger:

> "Jeg vil lære, hvordan agenter bruger værktøjer. Find de rigtige lektioner, opsummer hvad
> jeg skal læse først, og giv mig en kort praktisk opgave."

En almindelig chatbot kan svare ud fra det, den allerede ved. En agent kan gøre mere:

1. **Læs eller søg i kursusfiler** for at finde de rigtige lektioner.
2. **Brug værktøjer** til at hente lektioners links, eksempler eller støttemateriale.
3. **Planlæg** en kort læringsvej i stedet for at give ét langt svar.
4. **Brug kontekst** fra den aktuelle samtale for at holde fokus på elevens
   mål.
5. **Husk nyttige præferencer** hvis applikationen understøtter hukommelse.
6. **Vis spor, kildehenvisninger eller logs** så brugeren kan forstå, hvad der skete.
7. **Anvend sikkerhedsforanstaltninger** før risikable handlinger eller brug af følsomme data.

Mens du studerer hver lektion, vend tilbage til denne demo og spørg:
hvilken ny evne vil lektionen tilføje?

## Hvad du bygger hen imod

Ved kursets afslutning bør du kunne forklare og bygge agentsystemer
der kombinerer disse dele:

| Del | Almindeligt sprogligt betyder | I demoen |
|------|-------------------------------|----------|
| Model | Den ræsonnerende motor, der fortolker brugerens anmodning | Forstår at læreren vil have lektioner om værktøjsbrug |
| Værktøjer | Funktioner, API’er, filer, browsere eller tjenester agenten kan bruge | Søger i repository eller henter lektioners indhold |
| Viden | Dokumenter eller data brugt til at forankre svaret | Kursus-README-filer og lektionsmateriale |
| Kontekst | Information inkluderet i næste modelkald | Brugerens mål og værktøjsresultater |
| Hukommelse | Information gemt til senere brug | Læreren foretrækker praktiske Python-eksempler |
| Planlægning | Opdeling af et større mål i mindre trin | Find lektioner, opsummer dem, foreslå øvelse |
| Orkestrering | Fordeling af arbejde over værktøjer, trin eller agenter | En planner kalder et søgeværktøj, så en opsummerer |
| Tillid | Sikkerhed, tryghed, evaluering og overvågning | Logger værktøjskald og spørger før handlinger med stor effekt |

## Vælg din læringsvej

Du kan tage hele kurset i rækkefølge eller springe til en vej baseret på, hvad du ønsker
at bygge.

| Hvis dit mål er at... | Start med | Så studér |
|----------------------|-----------|-----------|
| Forstå hvad agenter er | 01, 02, 03 | 04, 05, 06 |
| Bygge en agent der bruger værktøjer | 04 | 05, 07, 14 |
| Bygge en RAG-baseret agent | 05 | 04, 06, 12 |
| Designe workflows med flere trin | 07 | 08, 09, 14 |
| Forstå multi-agent-systemer | 08 | 07, 09, 11 |
| Forberede agenter til produktion | 06, 10 | 12, 13, 18 |
| Udforske protokoller og browserautomatisering | 11, 15 | 10, 18 |

Tip: hvis du er ny til agenter, så spring ikke lektionerne 01-06 over.
De giver dig den terminologi, du får brug for resten af kurset.

## Lektion-for-lektion guide

| Lektion | Hvad du lærer | Prøv dette efter lektionen |
|---------|---------------|----------------------------|
| [01 - Intro til AI-agenter](./01-intro-to-ai-agents/README.md) | Hvad gør en agent anderledes end en almindelig chatbot. | Forklar din demo-idé som en agent, ikke bare en chat-app. |
| [02 - Agentiske frameworks](./02-explore-agentic-frameworks/README.md) | Hvordan frameworks hjælper med modeller, værktøjer, tilstand og workflows. | Identificer hvilke dele af din demo en framework ville håndtere. |
| [03 - Agentiske designmønstre](./03-agentic-design-patterns/README.md) | Almindelige mønstre til at designe agentadfærd. | Skitsér brugerrejsen før kodning. |
| [04 - Brug af værktøjer](./04-tool-use/README.md) | Hvordan agenter kalder værktøjer for at hente data eller udføre handling. | Definer ét værktøj din demo-agent ville have brug for. |
| [05 - Agentisk RAG](./05-agentic-rag/README.md) | Hvordan retrieval forankrer agent-svar i dokumenter eller data. | Beslut hvilken videnskilde din demo skal søge i. |
| [06 - Pålidelige agenter](./06-building-trustworthy-agents/README.md) | Hvordan man tilføjer sikkerhedsforanstaltninger, overvågning og sikrere adfærd. | Tilføj én regel for, hvornår agenten først skal spørge brugeren. |
| [07 - Planlægningsdesign](./07-planning-design/README.md) | Hvordan agenter opdeler større mål i mindre trin. | Skriv en tre-trins plan for din demo-anmodning. |
| [08 - Design af multi-agent](./08-multi-agent/README.md) | Hvornår arbejde bør splittes over specialiserede agenter. | Beslut om din demo behøver én agent eller flere. |
| [09 - Metakognition](./09-metacognition/README.md) | Hvordan agenter kan gennemgå og forbedre deres eget output. | Tilføj en sidste selvtjek, før agenten svarer. |
| [10 - AI-agenter i produktion](./10-ai-agents-production/README.md) | Hvad der ændres, når en agent går fra demo til produktion. | Lav en liste over, hvad du vil overvåge: kvalitet, omkostning, latenstid, fejl. |
| [11 - Agentiske protokoller](./11-agentic-protocols/README.md) | Hvordan protokoller forbinder agenter til værktøjer og andre agenter. | Identificer hvor en standardprotokol kan forenkle integration. |
| [12 - Kontekst-engineering](./12-context-engineering/README.md) | Hvordan man vælger, trimmer, isolerer og styrer kontekst. | Beslut hvad der hører til i prompten, og hvad der skal udelades. |
| [13 - Agenthukommelse](./13-agent-memory/README.md) | Hvordan agenter kan gemme nyttige informationer på tværs af interaktioner. | Vælg én sikker præference din demo kan huske. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Framework-specifikke byggeblokke til agenter og workflows. | Mapper dine demo-trin til framework-koncepter. |
| [15 - Agenter til computerbrug](./15-browser-use/README.md) | Hvordan agenter kan interagere med browser- eller UI-flader. | Vælg én browseropgave, som stadig skal kræve brugerbekræftelse. |
| [18 - Sikring af AI-agenter](./18-securing-ai-agents/README.md) | Hvordan agenthandlinger bliver mere reviderbare og manipulationssikre. | Beslut hvilke handlinger i din demo, der skal logges eller kvitteres. |

Lektionerne 16 og 17 er nævnt i hoved-README som "kommer snart". Tilføj dem til din
studieplan, når lektionsindholdet er tilgængeligt.

## Vigtige idéer i begyndervenligt sprog

### Værktøjer

Et værktøj er noget, agenten kan kalde for at udføre arbejde uden for modellen. Et godt værktøj
har et klart navn, en snæver opgave, typed input, forudsigeligt output og en sikker måde at fejle på.

For kursushjælper-demoen kunne et værktøj være:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG og viden

RAG hjælper agenten med at svare ud fra kildemateriale i stedet for at gætte. I dette
kursus kan kildematerialet være lektions-README’er, kodeeksempler eller eksterne
ressourcer linket fra lektionerne.

Brug RAG når svaret skal forankres i dokumenter, data eller aktuelle
projektfiler.

### Planlægning

Planlægning er nyttigt, når anmodningen har flere trin. Hold planer korte og
synlige nok til, at en udvikler eller bruger kan inspicere dem.

For demoen kunne en plan være:

1. Find lektioner relateret til værktøjsbrug.
2. Opsummer de mest relevante lektioner.
3. Anbefal én praktisk opgave.

### Kontekst

Kontekst er hvad modellen ser lige nu. For lidt kontekst kan få agenten til
at overse vigtige detaljer. For meget kontekst kan gøre agenten langsommere, dyrere
eller nemmere at forvirre.

God kontekst-engineering betyder at vælge den rette information til næste modelkald.

### Hukommelse

Hukommelse er information gemt til senere. Gem ikke alt. Gem kun information,
når det er nyttigt, sikkert og let at opdatere eller slette.

For eksempel kan det være nyttigt at huske "læreren foretrækker Python-eksempler".
At huske følsomme persondata er normalt ikke.

### Evaluering og overvågning

Evaluering spørger: gjorde agenten det rigtige?

Overvågning spørger: kan vi se, hvordan det skete?

For produktionsagenter, hold styr på modelkald, værktøjskald, hentet kontekst,
latenstid, omkostning, fejl og brugerfeedback.

### Tillid og sikkerhed

Pålidelige agenter har brug for mere end en hjælpsom prompt. Brug mindst-moglige-rettigheder-værktøjer,
menneskelig godkendelse for høj-effekt handlinger, data-redigering hvor nødvendigt,
og logs eller kvitteringer for handlinger der skal revideres.

## En 15-minutters anmeldelsesrutine

Brug denne rutine efter hver lektion:

1. **Opsummer lektionen i én sætning.**
2. **Navngiv den nye agent-evne.** For eksempel: værktøjsbrug, retrieval,
   planlægning, hukommelse, overvågning eller sikkerhed.
3. **Tilføj den til kursushjælper-demoen.** Hvad ændres i demoen nu?
4. **Find risikoen.** Hvad kan gå galt, hvis evnen misbruges?
5. **Skriv ét testspørgsmål.** Hvordan vil du tjekke, at agenten opfører sig godt?

## Hurtig selvtest

Før du går videre, prøv at besvare disse spørgsmål:

1. Hvad kan en agent gøre, som en almindelig chatbot ikke kan gøre selv?
2. Hvilket værktøj vil din agent have brug for først, og hvorfor?
3. Hvilken videnskilde skal forankre agentens svar?
4. Hvilken kontekst bør inkluderes i næste modelkald?
5. Hvad skal agenten huske, og hvad bør undgås at gemme?
6. Hvornår skal agenten bede om menneskelig godkendelse?
7. Hvilke logs, spor eller kvitteringer vil hjælpe dig med at fejlfinde eller revidere agenten senere?

## Foreslået afsluttende øvelse

Ved kursets afslutning, byg en lille agent, der hjælper en lærende med at navigere
i dette repository.

Minimum version:

- Accepter et emne fra brugeren.
- Find de mest relevante lektioner.
- Opsummer hvad der skal læses først.
- Foreslå én praktisk øvelse.
- Vis hvilke lektionsfiler eller links der blev brugt.

Udvidet version:

- Husk lærerens foretrukne programmeringssprog.
- Brug en simpel plan før svar.
- Tilføj et selvtjek-trin før det endelige svar.
- Log værktøjskald og hentede kilder.
- Spørg om bekræftelse før åbning af browser- eller UI-automatiseringsopgaver.

Dette giver dig en lille men realistisk måde at øve værktøjer, RAG, planlægning,
kontekst, hukommelse, overvågning og tillid i ét projekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->