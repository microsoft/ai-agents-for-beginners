# AI-agenter for begyndere - Studievejledning

Brug denne vejledning som en praktisk ledsager, mens du bevæger dig gennem kurset. Den er
ikke ment som erstatning for lektionerne. Den hjælper dig med at beslutte, hvor du skal starte, hvad du skal
kigge efter i hver lektion, og hvordan du forbinder ideerne til en lille fungerende agent-
demo.

Hvis dette er din første gang her, start simpelt:

1. Læs [Course Setup](./00-course-setup/README.md).
2. Gennemfør lektionerne 01-06 i rækkefølge.
3. Hav én lille demoidé i tankerne, mens du lærer.
4. Efter hver lektion, spørg: "Hvad kan min agent gøre nu, som den ikke kunne
   før?"

## En simpel demo at holde i tankerne

En god måde at lære agenter på er at følge én demoidé gennem kurset.

Eksempel på demo: **en kursusassistent-agent**.

Brugeren spørger:

> "Jeg vil lære, hvordan agenter bruger værktøjer. Find de rigtige lektioner, opsummer hvad
> jeg først bør læse, og giv mig en kort øvelse."

En almindelig chatbot kan svare ud fra, hvad den allerede ved. En agent kan gøre mere:

1. **Læs eller søg i kursusfiler** for at finde de rigtige lektioner.
2. **Brug værktøjer** til at hente lektionlinks, eksempler eller støttemateriale.
3. **Planlæg** en kort læringssti i stedet for at give et langt svar.
4. **Brug kontekst** fra den aktuelle samtale for at holde fokus på
   elevens mål.
5. **Husk nyttige præferencer**, hvis applikationen understøtter hukommelse.
6. **Vis spor, citater eller logfiler**, så brugeren kan forstå, hvad der skete.
7. **Anvend sikkerhedsforanstaltninger** før risikable handlinger eller brug af følsomme data.

Mens du studerer hver lektion, vend tilbage til denne demo og spørg: hvilken ny kapabilitet
ville denne lektion tilføre?

## Hvad du bygger hen imod

Ved kursets afslutning bør du kunne forklare og bygge agentsystemer
, der kombinerer disse dele:

| Del | Almindeligt sprog | I demoen |
|------|------------------------|-------------|
| Model | Den ræsonnerende motor, der fortolker brugerens anmodning | Forstår, at eleven ønsker lektioner om brug af værktøjer |
| Værktøjer | Funktioner, API'er, filer, browsere eller services agenten kan bruge | Søger i repositoriet eller henter lektionens indhold |
| Viden | Dokumenter eller data brugt til at understøtte svaret | Kursusets README-filer og lektionmaterialer |
| Kontekst | Information inkluderet i næste modelkald | Brugerens mål og resultater fra værktøjer |
| Hukommelse | Information gemt til senere brug | Eleven foretrækker praktiske Python-eksempler |
| Planlægning | Opdeling af et større mål i mindre trin | Find lektioner, opsummér dem, foreslå øvelse |
| Orkestrering | Fordeling af arbejde på værktøjer, trin eller agenter | En planlægger kalder et søgeværktøj, derefter en opsummeringsfunktion |
| Tillid | Sikkerhed, evaluering og observerbarhed | Logger værktøjskald og spørger før handlinger med stor indvirkning |

## Modeller og udbydere

Kursusets kodeeksempler bruger **Microsoft Agent Framework (MAF)** og retter sig mod **Azure OpenAI Responses API** — den anbefalede API fremover, som kombinerer chat-completions, kald af værktøjer, multimodal input og tilstandsholdende samtaler i et enkelt API-flade. Du forbinder enten via et **Microsoft Foundry** projekt (med `FoundryChatClient`) eller direkte til Azure OpenAI (med `OpenAIChatClient`).

Når du arbejder dig gennem lektionerne, har du flere udbydermuligheder:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — hovedvejen brugt i lektionerne. Log ind med `az login` for nøglefri Entra ID-autentificering.
- **Foundry Local** — kør modeller fuldt på enheden via en OpenAI-kompatibel API (ingen cloud, ingen API-nøgler). Ideel til offline eller gratis eksperimenter. Se [Course Setup](./00-course-setup/README.md).
- **MiniMax** — en OpenAI-kompatibel udbyder med store kontekstmodeller, brugbar som en drop-in erstatning.

> **Bemærk:** GitHub Models er udfaset (udgår juli 2026) og understøtter ikke Responses API. Eksemplerne er opdateret til at bruge Azure OpenAI / Microsoft Foundry i stedet.

## Vælg din læringssti

Du kan følge hele kurset i rækkefølge eller springe til en sti baseret på, hvad du vil
bygge.

| Hvis dit mål er at... | Start med | Derefter studer |
|-----------------------|------------|------------|
| Forstå, hvad agenter er | 01, 02, 03 | 04, 05, 06 |
| Bygge en agent, der bruger værktøjer | 04 | 05, 07, 14 |
| Bygge en RAG-baseret agent | 05 | 04, 06, 12 |
| Designe workflow med flere trin | 07 | 08, 09, 14 |
| Forstå multi-agent-systemer | 08 | 07, 09, 11 |
| Forberede agenter til produktion | 06, 10 | 12, 13, 16, 18 |
| Udrulle og skalere agenter på Foundry | 10, 16 | 06, 13, 18 |
| Bygge lokale / offline-første agenter | 17 | 04, 05, 11 |
| Udforske protokoller og browserautomatisering | 11, 15 | 10, 18 |

Tip: hvis du er ny med agenter, spring ikke Lektion 01-06 over. De giver dig det
ordforråd, du får brug for resten af kurset.

## Lektion-for-lektion guide

| Lektion | Hvad du lærer | Prøv dette efter lektionen |
|--------|----------------|---------------------------|
| [01 - Introduktion til AI-agenter](./01-intro-to-ai-agents/README.md) | Hvad gør en agent anderledes end en almindelig chatbot. | Forklar din demoidé som en agent, ikke bare en chat-app. |
| [02 - Agentiske frameworks](./02-explore-agentic-frameworks/README.md) | Hvordan frameworks hjælper med modeller, værktøjer, tilstand og workflows. | Identificer hvilke dele af din demo et framework ville styre. |
| [03 - Agentiske designmønstre](./03-agentic-design-patterns/README.md) | Almindelige mønstre til design af agent-adfærd. | Skitser brugerens rejse inden du skriver kode. |
| [04 - Brug af værktøjer](./04-tool-use/README.md) | Hvordan agenter kalder værktøjer for at hente data eller tage handling. | Definer ét værktøj, din demo-agent ville have brug for. |
| [05 - Agentisk RAG](./05-agentic-rag/README.md) | Hvordan retrieval etablerer agentens svar i dokumenter eller data. | Beslut, hvilken videnskilde din demo skal søge i. |
| [06 - Tillidsværdige agenter](./06-building-trustworthy-agents/README.md) | Hvordan man tilføjer sikkerhedsforanstaltninger, tilsyn og sikrere adfærd. | Tilføj en regel for, hvornår agenten først skal spørge brugeren. |
| [07 - Planlægningsdesign](./07-planning-design/README.md) | Hvordan agenter opdeler større mål i mindre trin. | Skriv en tre-trins plan for din demo-anmodning. |
| [08 - Multi-agent design](./08-multi-agent/README.md) | Hvornår man fordeler arbejde på specialiserede agenter. | Beslut om din demo har brug for én agent eller flere. |
| [09 - Metakognition](./09-metacognition/README.md) | Hvordan agenter kan gennemgå og forbedre deres output. | Tilføj en slutlig selvkontrol inden agenten svarer. |
| [10 - AI-agenter i produktion](./10-ai-agents-production/README.md) | Hvad der ændres, når en agent går fra demo til produktion. | List hvad du ville overvåge: kvalitet, omkostning, latenstid, fejl. |
| [11 - Agentiske protokoller](./11-agentic-protocols/README.md) | Hvordan protokoller forbinder agenter til værktøjer og andre agenter. | Identificer hvor en standardprotokol kunne forenkle integrationen. |
| [12 - Kontext engineering](./12-context-engineering/README.md) | Hvordan man vælger, skærer ned, isolerer og håndterer kontekst. | Beslut, hvad der hører til i prompten og hvad der skal holdes ude. |
| [13 - Agent-hukommelse](./13-agent-memory/README.md) | Hvordan agenter kan gemme nyttig information på tværs af interaktioner. | Vælg én sikker præference, din demo kunne huske. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Framework-specifikke byggesten til agenter og workflows, plus hosting af LangChain/LangGraph agenter på Microsoft Foundry. | Map dine demo-trin til framework-koncepter. |
| [15 - Computerbrugs-agenter](./15-browser-use/README.md) | Hvordan agenter kan interagere med browser- eller UI-flader, inkl. virkelige eksempler som Microsoft Project Opal. | Vælg én browseropgave, som stadig skal kræve brugerbekræftelse. |
| [16 - Udrulning af skalerbare agenter](./16-deploying-scalable-agents/README.md) | Hvordan man tager en agent fra prototype til en skalerbar, observerbar produktionsudrulning på Microsoft Foundry (hostede agenter, modelrouting, caching, evalueringsporte, røgtjek). | List de produktionsbekymringer din demo stadig har brug for: hosting, routing, omkostning, evaluering. |
| [17 - Oprettelse af lokale AI-agenter](./17-creating-local-ai-agents/README.md) | Hvordan man bygger lokale-første agenter, der kører fuldt ud på din computer med Foundry Local og Qwen (lokale værktøjer, lokal RAG, lokal MCP). | Beslut hvilke dele af din demo der skal forblive private og køre lokalt. |
| [18 - Sikring af AI-agenter](./18-securing-ai-agents/README.md) | Hvordan man gør agenthandlinger mere reviderbare og manipulationssikre. | Beslut, hvilke handlinger i din demo der skal logges eller have kvittering. |

## Validering af udrullede agenter med røgtjek

Når du udruller en agent (Lektion 16), er en **røgtjek** den billigste første
kontrol for at sikre, at udrulningen rent faktisk svarer. Dette repo leverer klar-til-kørsel
kataloger under [tests/](./tests/README.md) for de udrulbare agenter i Lektionerne
01, 04, 05, og 16, koblet til
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action. Kør dem fra fanen **Actions**, efter at lektions-agenten er udrullet.
Røgtjek er en første port — offline og online evaluering (Lektionerne 10 og 16)
fortæller dig, hvor *god* agenten er.

## Nøgleideer i nybegyndervenlige termer

### Værktøjer

Et værktøj er noget, agenten kan kalde for at udføre arbejde uden for modellen. Et godt værktøj
har et klart navn, en snæver opgave, typede input, forudsigeligt output, og en sikker måde
at fejle på.

For kursusassistent-demoen kunne et værktøj være:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG og viden

RAG hjælper agenten med at svare ud fra kildemateriale i stedet for at gætte. I dette
kursus kunne denne kilde være lektionernes README'er, kodeeksempler eller eksterne
ressourcer linket fra lektionerne.

Brug RAG, når svaret bør være forankret i dokumenter, data eller aktuelle
projektfiler.

### Planlægning

Planlægning er nyttigt, når anmodningen har mere end ét trin. Hold planer korte og
synlige nok til, at en udvikler eller bruger kan inspicere dem.

For demoen kunne en plan være:

1. Find lektioner relateret til brug af værktøjer.
2. Opsummér de mest relevante lektioner.
3. Anbefal én øvelsesopgave.

### Kontekst

Kontekst er, hvad modellen ser lige nu. For lidt kontekst kan få agenten
til at overse vigtige detaljer. For meget kontekst kan gøre agenten langsommere, dyrere,
eller lettere at forvirre.

God kontekst-engineering betyder at vælge den rigtige information til det næste model-
kald.

### Hukommelse

Hukommelse er information gemt til senere brug. Gem ikke alt. Gem information
kun når den er nyttig, sikker, og nem at opdatere eller slette.

For eksempel kan det være nyttigt at huske "eleven foretrækker Python-eksempler".
At huske følsomme persondata er normalt ikke det.

### Evaluering og observerbarhed

Evaluering stiller spørgsmålet: gjorde agenten det rigtige?

Observerbarhed stiller spørgsmålet: kan vi se, hvordan det skete?

For produktionsagenter, hold styr på modelkald, værktøjskald, hentet kontekst,
latenstid, omkostninger, fejl og brugerfeedback.

### Tillid og sikkerhed

Tillidsværdige agenter kræver mere end en hjælpsom prompt. Brug mindst-privilegieværktøjer,
menneskelig godkendelse for handlinger med stor indvirkning, data-redigering hvor nødvendigt, og logfiler eller
kvitteringer for handlinger, der skal kunne revideres.

## En 15-minutters gennemgangsrutine

Brug denne rutine efter hver lektion:

1. **Opsummér lektionen i én sætning.**
2. **Navngiv den nye agent-kapabilitet.** For eksempel: brug af værktøj, retrieval,
   planlægning, hukommelse, observerbarhed eller sikkerhed.
3. **Tilføj den til kursusassistent-demoen.** Hvad ændres i demoen nu?
4. **Find risikoen.** Hvad kunne gå galt, hvis denne kapabilitet misbruges?
5. **Skriv ét testspørgsmål.** Hvordan ville du kontrollere, at agenten opfører sig godt?

## Hurtig selvkontrol

Før du går videre, prøv at besvare disse spørgsmål:

1. Hvad kan en agent gøre, som en almindelig chatbot ikke kan gøre alene?
2. Hvilket værktøj ville din agent have brug for først, og hvorfor?
3. Hvilken videnskilde bør forankre agentens svar?
4. Hvilken kontekst bør inkluderes i det næste modelkald?
5. Hvad bør agenten huske, og hvad bør den undgå at gemme?
6. Hvornår bør agenten bede om menneskelig godkendelse?
7. Hvilke logfiler, spor eller kvitteringer ville hjælpe dig med at fejlfinde eller revidere agenten senere?


## Foreslået afsluttende opgave

I slutningen af kurset, byg en lille agent, der hjælper en elev med at navigere i dette
repository.

Minimum version:

- Accepter et emne fra brugeren.
- Find de mest relevante lektioner.
- Opsummer, hvad man skal læse først.
- Foreslå en praktisk opgave.
- Vis hvilke lektionsfiler eller links der blev brugt.

Udvidet version:

- Husk elevens foretrukne programmeringssprog.
- Brug en simpel plan før svar.
- Tilføj en selvkontrol før det endelige svar.
- Log værktøjskald og hentede kilder.
- Spørg om bekræftelse før åbning af browser eller UI-automatiseringsopgaver.

Dette giver dig en lille men realistisk måde at øve værktøjer, RAG, planlægning,
kontekst, hukommelse, observerbarhed og tillid i ét projekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->