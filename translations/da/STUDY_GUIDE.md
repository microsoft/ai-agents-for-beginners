# AI-Agenter for Begyndere - Studievejledning

Brug denne vejledning som en praktisk ledsager, mens du gennemgår kurset. Den er
ikke ment som erstatning for lektionerne. Den hjælper dig med at beslutte, hvor du skal starte,
hvad du skal kigge efter i hver lektion, og hvordan du forbinder ideerne til en lille fungerende agent-
demo.

Hvis det er første gang, du er her, så start enkelt:

1. Læs [Kursusopsætning](./00-course-setup/README.md).
2. Gennemfør lektionerne 01-06 i rækkefølge.
3. Hav en lille demo-idé i tankerne, mens du lærer.
4. Efter hver lektion, spørg: "Hvad kan min agent nu, som den ikke kunne
   før?"

## En Simpel Demo at Have i Tankerne

En god måde at lære agenter på er at følge én demo-idé gennem kurset.

Eksempeldemo: **en kursushjælper-agent**.

Brugeren spørger:

> "Jeg vil lære, hvordan agenter bruger værktøjer. Find de rigtige lektioner, opsummer hvad
> jeg skal læse først, og giv mig en kort øvelse."

En almindelig chatbot kan svare ud fra, hvad den allerede ved. En agent kan mere:

1. **Læs eller søg i kursusfiler** for at finde de rette lektioner.
2. **Brug værktøjer** til at hente lektion-links, eksempler eller støttemateriale.
3. **Planlæg** en kort læringsvej i stedet for at give ét langt svar.
4. **Brug kontekst** fra den aktuelle samtale for at holde fokus på elevens
   mål.
5. **Husk nyttige præferencer** hvis applikationen understøtter hukommelse.
6. **Vis spor, kildehenvisninger eller logs** så brugeren kan forstå, hvad der skete.
7. **Anvend sikkerhedsforanstaltninger** før risikable handlinger eller brug af følsomme data.

Når du studerer hver lektion, vend tilbage til denne demo og spørg: hvilken ny funktionalitet
ville denne lektion tilføje?

## Hvad Du Bygger Op Mod

Ved kursets slutning bør du kunne forklare og bygge agentsystemer,
der kombinerer disse dele:

| Del | Almindeligt sprog | I demoen |
|------|------------------------|-------------|
| Model | Den ræsonnerende motor, der fortolker brugerens anmodning | Forstår at eleven ønsker lektioner om værktøjsbrug |
| Værktøjer | Funktioner, API'er, filer, browsere eller tjenester, agenten kan bruge | Søger i repo eller henter lektionens indhold |
| Viden | Dokumenter eller data brugt til at grundfæste svaret | Kursus README-filer og lektionmateriale |
| Kontekst | Information medtaget i næste modelkald | Brugerens mål og værktøjsresultaterne |
| Hukommelse | Information gemt til senere brug | Eleven foretrækker hands-on Python-eksempler |
| Planlægning | At bryde et større mål ned i mindre trin | Find lektioner, opsummer dem, foreslå øvelser |
| Orkestrering | Fordeling af opgaver på tværs af værktøjer, trin eller agenter | En planlægger kalder et søgeværktøj, derefter en opsummerer |
| Tillid | Sikkerhed, evaluering og overvågning | Logger værktøjskald og spørger før højt-impact handlinger |

## Modeller og Udbydere

Kursuskodeeksemplerne bruger **Microsoft Agent Framework (MAF)** og retter sig mod **Azure OpenAI Responses API** — den anbefalede API fremover, som kombinerer chat-svar, værktøjskald, multimodal input og tilstandsfyldte samtaler i ét API-flade. Du forbinder enten gennem et **Microsoft Foundry** projekt (med `FoundryChatClient`) eller direkte til Azure OpenAI (med `OpenAIChatClient`).

Mens du arbejder dig igennem lektionerne, har du nogle udbydermuligheder:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — den primære vej brugt på tværs af lektionerne. Log ind med `az login` for nøglefri Entra ID-godkendelse.
- **Foundry Local** — kør modeller helt lokalt gennem en OpenAI-kompatibel API (ingen sky, ingen API-nøgler). Ideelt til offline eller omkostningsfri eksperimenter. Se [Kursusopsætning](./00-course-setup/README.md).
- **MiniMax** — en OpenAI-kompatibel udbyder med store-kontekst modeller, brugbar som erstatning.

> **Note:** GitHub Models er udfaset (ophører juli 2026) og understøtter ikke Responses API’en. Eksemplerne er opdateret til at bruge Azure OpenAI / Microsoft Foundry i stedet.

## Vælg Din Læringsvej

Du kan tage hele kurset i rækkefølge eller springe til en vej baseret på, hvad du vil
bygge.

| Hvis dit mål er at... | Start med | Studer derefter |
|-----------------------|------------|------------|
| Forstå hvad agenter er | 01, 02, 03 | 04, 05, 06 |
| Byg en agent, der bruger værktøjer | 04 | 05, 07, 14 |
| Byg en RAG-baseret agent | 05 | 04, 06, 12 |
| Design multi-trins arbejdsgange | 07 | 08, 09, 14 |
| Forstå multi-agent systemer | 08 | 07, 09, 11 |
| Forbered agenter til produktion | 06, 10 | 12, 13, 18 |
| Udforsk protokoller og browserautomatisering | 11, 15 | 10, 18 |

Tip: Hvis du er ny med agenter, så spring ikke lektionerne 01-06 over. De giver dig
ordforrådet, du skal bruge til resten af kurset.

## Lektion-for-Lektion Vejledning

| Lektion | Hvad du lærer | Prøv dette efter lektionen |
|--------|----------------|---------------------------|
| [01 - Intro til AI-Agenter](./01-intro-to-ai-agents/README.md) | Hvad der gør en agent forskellig fra en basic chatbot. | Forklar din demo-idé som en agent, ikke bare en chat-app. |
| [02 - Agentiske Frameworks](./02-explore-agentic-frameworks/README.md) | Hvordan frameworks hjælper med modeller, værktøjer, tilstand og arbejdsgange. | Identificer hvilke dele af din demo et framework ville styre. |
| [03 - Agentiske Designmønstre](./03-agentic-design-patterns/README.md) | Almindelige mønstre til design af agentadfærd. | Skitsér brugerrejsen før du skriver kode. |
| [04 - Værktøjsbrug](./04-tool-use/README.md) | Hvordan agenter kalder værktøjer for at hente data eller handle. | Definér ét værktøj din demo-agent ville have brug for. |
| [05 - Agentisk RAG](./05-agentic-rag/README.md) | Hvordan retrieval grundfæster agentens svar i dokumenter eller data. | Beslut hvilken videnskilde din demo skal søge i. |
| [06 - Pålidelige Agenter](./06-building-trustworthy-agents/README.md) | Hvordan man tilføjer sikkerhedsforanstaltninger, tilsyn og mere sikker adfærd. | Tilføj én regel for, hvornår agenten først skal spørge brugeren. |
| [07 - Planlægningsdesign](./07-planning-design/README.md) | Hvordan agenter bryder større mål ned i mindre trin. | Skriv en plan i tre trin for din demo-anmodning. |
| [08 - Multi-Agent Design](./08-multi-agent/README.md) | Hvornår man opdeler arbejde mellem specialiserede agenter. | Beslut om din demo har brug for én agent eller flere. |
| [09 - Metakognition](./09-metacognition/README.md) | Hvordan agenter kan gennemgå og forbedre deres eget output. | Tilføj et slut-selvcheck før agenten svarer. |
| [10 - AI-Agenter i Produktion](./10-ai-agents-production/README.md) | Hvad der ændrer sig, når en agent går fra demo til produktion. | List det du ville overvåge: kvalitet, omkostning, latenstid, fejl. |
| [11 - Agentiske Protokoller](./11-agentic-protocols/README.md) | Hvordan protokoller forbinder agenter til værktøjer og andre agenter. | Identificer hvor en standardprotokol kunne forenkle integration. |
| [12 - Kontekst Engineering](./12-context-engineering/README.md) | Hvordan man vælger, trimmer, isolerer og styrer kontekst. | Beslut hvad der høre til i prompten, og hvad der skal holdes ude. |
| [13 - Agent Hukommelse](./13-agent-memory/README.md) | Hvordan agenter kan gemme nyttig information på tværs af interaktioner. | Vælg én sikker præference din demo kunne huske. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Framework-specifikke byggesten for agenter og arbejdsgange, plus hosting af LangChain/LangGraph agenter på Microsoft Foundry. | Kortlæg dine demo-trin til framework-koncepter. |
| [15 - Computerbrug Agenter](./15-browser-use/README.md) | Hvordan agenter kan interagere med browser- eller UI-flader, inklusiv virkelige eksempler som Microsoft Project Opal. | Vælg én browser-opgave der stadig bør kræve brugerbekræftelse. |
| [18 - Sikring af AI-Agenter](./18-securing-ai-agents/README.md) | Hvordan man gør agenthandlinger mere reviderbare og manipulationssikre. | Beslut hvilke handlinger i din demo der skal logges eller kvitteres. |

Lektionerne 16 og 17 står i hoved-README’en som kommer snart. Tilføj dem til din
studieplan, når lektionindhold bliver tilgængeligt.

## Centrale Ideer i Begyndervenlige Termer

### Værktøjer

Et værktøj er noget, agenten kan kalde for at udføre arbejde uden for modellen. Et godt værktøj
har et tydeligt navn, en snæver opgave, typede inputs, forudsigeligt output, og en sikker måde
at fejle på.

For kursushjælp-demoen kunne et værktøj være:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG og Viden

RAG hjælper agenten med at svare ud fra kildemateriale i stedet for at gætte. I dette
kursus kunne det materiale være lektionernes README-filer, kodeeksempler eller eksterne
ressourcer, der er linket fra lektionerne.

Brug RAG, når svaret skal forankres i dokumenter, data eller aktuelle
projektfiler.

### Planlægning

Planlægning er nyttig, når anmodningen har mere end ét trin. Hold planer korte og
synlige nok til at en udvikler eller bruger kan gennemgå dem.

For demoen kunne en plan være:

1. Find lektioner relateret til værktøjsbrug.
2. Opsummer de mest relevante lektioner.
3. Anbefal én øvelse.

### Kontekst

Kontekst er, hvad modellen ser lige nu. For lidt kontekst kan få agenten til
at overse vigtige detaljer. For meget kontekst kan gøre agenten langsommere, dyrere,
eller lettere forvirret.

God kontekst engineering betyder at vælge den rette information til næste model-
kald.

### Hukommelse

Hukommelse er information gemt til senere. Gem ikke alt. Gem kun information,
når det er nyttigt, sikkert, og nemt at opdatere eller slette.

For eksempel kan det være brugbart at huske "eleven foretrækker Python-eksempler".
At huske følsomme persondata er det som regel ikke.

### Evaluering og Overvågning

Evaluering spørger: gjorde agenten det rigtige?

Overvågning spørger: kan vi se, hvordan det skete?

For produktionsagenter, hold styr på modelkald, værktøjskald, hentet kontekst,
latenstid, omkostninger, fejl og brugertilbagemeldinger.

### Tillid og Sikkerhed

Pålidelige agenter har brug for mere end en hjælpsom prompt. Brug mindst-privilegium værktøjer,
menneskelig godkendelse ved høj-impact handlinger, dataredigering hvor nødvendigt,
og logfiler eller kvitteringer for handlinger, der skal kunne revideres.

## En 15-Minutters Gennemgangsrutine

Brug denne rutine efter hver lektion:

1. **Opsummer lektionen i én sætning.**
2. **Navngiv den nye agentfunktion.** For eksempel: værktøjsbrug, retrieval,
   planlægning, hukommelse, overvågning eller sikkerhed.
3. **Tilføj den til kursushjælper-demonstrationen.** Hvad ændrer sig i demoen nu?
4. **Find risikoen.** Hvad kunne gå galt, hvis denne funktionalitet misbruges?
5. **Skriv et testspørgsmål.** Hvordan ville du tjekke, at agenten opfører sig godt?

## Hurtig Selvevaluering

Før du går videre, prøv at besvare disse spørgsmål:

1. Hvad kan en agent gøre, som en almindelig chatbot ikke kan gøre alene?
2. Hvilket værktøj ville din agent have brug for først, og hvorfor?
3. Hvilken videnskilde skal grundfæste agentens svar?
4. Hvilken kontekst skal inkluderes i næste modelkald?
5. Hvad skal agenten huske, og hvad skal den undgå at gemme?
6. Hvornår skal agenten bede om menneskelig godkendelse?
7. Hvilke logs, spor eller kvitteringer ville hjælpe dig med at fejlfinde eller revidere agenten senere?

## Foreslået Afsluttende Øvelse

Ved kursets slutning, byg en lille agent, der hjælper en elev med at navigere i dette
repository.

Minimum version:

- Accepter et emne fra brugeren.
- Find de mest relevante lektioner.
- Opsummer hvad der skal læses først.
- Foreslå én praktisk øvelse.
- Vis hvilke lektionfiler eller links, der blev brugt.

Udvidet version:

- Husk elevens foretrukne programmeringssprog.
- Brug en simpel plan før svar.
- Tilføj et selvcheck trin før det endelige svar.
- Log værktøjskald og hentede kilder.
- Spørg om bekræftelse før åbning af browser- eller UI-automatiseringsopgaver.

Dette giver dig en lille, men realistisk måde at øve værktøjer, RAG, planlægning,
kontekst, hukommelse, overvågning og tillid i ét projekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->