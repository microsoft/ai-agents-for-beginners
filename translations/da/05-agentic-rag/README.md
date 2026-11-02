[![Agentic RAG](../../../translated_images/da/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Agentic RAG

Denne lektion giver en omfattende gennemgang af Agentic Retrieval-Augmented Generation (Agentic RAG), et fremvoksende AI-paradigme, hvor store sprogmodeller (LLM'er) autonomt planlægger deres næste skridt, mens de henter information fra eksterne kilder. I modsætning til statiske retrieval-then-read mønstre involverer Agentic RAG iterative kald til LLM'en, krydret med værktøjs- eller funktionskald og strukturerede output. Systemet evaluerer resultater, forfiner forespørgsler, aktiverer yderligere værktøjer efter behov og fortsætter denne cyklus, indtil en tilfredsstillende løsning er opnået.

## Introduktion

Denne lektion vil dække

- **Forstå Agentic RAG:** Lær om det fremvoksende paradigme i AI, hvor store sprogmodeller (LLM'er) autonomt planlægger deres næste skridt, mens de henter information fra eksterne datakilder.
- **Forstå iterativ Maker-Checker stil:** Forstå løkken med iterative kald til LLM'en, krydret med værktøjs- eller funktionskald og strukturerede output, designet til at forbedre korrekthed og håndtere fejlformulerede forespørgsler.
- **Udforsk praktiske anvendelser:** Identificer scenarier, hvor Agentic RAG skinner, såsom korrekthed-først miljøer, komplekse databaseinteraktioner og udvidede workflows.

## Læringsmål

Efter at have gennemført denne lektion vil du vide hvordan og forstå:

- **Forståelse af Agentic RAG:** Lær om det fremvoksende paradigme i AI, hvor store sprogmodeller (LLM'er) autonomt planlægger deres næste skridt, mens de henter information fra eksterne datakilder.
- **Iterativ Maker-Checker stil:** Forstå konceptet med en løkke af iterative kald til LLM'en, krydret med værktøjs- eller funktionskald og strukturerede output, designet til at forbedre korrekthed og håndtere fejlformulerede forespørgsler.
- **Selvstændighed i ræsonneringsprocessen:** Forstå systemets evne til at eje sin ræsonneringsproces, træffe beslutninger om hvordan man griber problemer an uden at være afhængig af foruddefinerede veje.
- **Workflow:** Forstå hvordan en agentmodel uafhængigt beslutter at hente markedsrapportmateriale, identificere konkurrentdata, korrelere interne salgstal, syntetisere fundene og evaluere strategien.
- **Iterative løkker, værktøjsintegration og hukommelse:** Lær om systemets afhængighed af et loopet interaktionsmønster, der opretholder tilstand og hukommelse på tværs af trin for at undgå gentagne løkker og træffe informerede beslutninger.
- **Håndtering af fejlsituationer og selvkorrektion:** Udforsk systemets robuste selvkorrektionsmekanismer, inklusive iterative og gentagne forespørgsler, brug af diagnostiske værktøjer og tilbagefald på menneskelig overvågning.
- **Agentgrænser:** Forstå begrænsningerne af Agentic RAG, med fokus på domæne-specifik autonomi, afhængighed af infrastruktur og respekt for sikkerhedsforanstaltninger.
- **Praktiske anvendelsestilfælde og værdi:** Identificer scenarier, hvor Agentic RAG skiller sig ud, som i korrekthed-først miljøer, komplekse databaseinteraktioner og udvidede workflows.
- **Styring, gennemsigtighed og tillid:** Lær om vigtigheden af styring og gennemsigtighed, inklusive forklarlig ræsonnering, bias-kontrol og menneskelig overvågning.

## Hvad er Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) er et fremvoksende AI-paradigme, hvor store sprogmodeller (LLM'er) autonomt planlægger deres næste skridt, mens de henter information fra eksterne kilder. I modsætning til statiske retrieval-then-read mønstre involverer Agentic RAG iterative kald til LLM'en, krydret med værktøjs- eller funktionskald og strukturerede output. Systemet evaluerer resultater, forfiner forespørgsler, aktiverer yderligere værktøjer efter behov og fortsætter denne cyklus, indtil en tilfredsstillende løsning er opnået. Denne iterative "maker-checker" stil forbedrer korrekthed, håndterer fejlformulerede forespørgsler og sikrer resultater af høj kvalitet.

Systemet ejer aktivt sin ræsonneringsproces, omskriver fejlede forespørgsler, vælger forskellige hentemetoder og integrerer flere værktøjer – såsom vektorsøgning i Azure AI Search, SQL-databaser eller brugerdefinerede API'er – før det færdiggør sit svar. Den afgørende egenskab ved et agentisk system er dets evne til selvstændigt at eje sin ræsonneringsproces. Traditionelle RAG-implementeringer er afhængige af foruddefinerede veje, men et agentisk system bestemmer autonomt rækkefølgen af trin baseret på kvaliteten af den fundne information.

## Definition af Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) er et fremvoksende paradigme inden for AI-udvikling, hvor LLM'er ikke kun henter information fra eksterne datakilder, men også autonomt planlægger deres næste skridt. I modsætning til statiske retrieval-then-read mønstre eller omhyggeligt udformede prompt-sekvenser involverer Agentic RAG en løkke af iterative kald til LLM'en, krydret med værktøjs- eller funktionskald og strukturerede output. Ved hvert trin evaluerer systemet de opnåede resultater, beslutter, om det skal forfine sine forespørgsler, aktiverer yderligere værktøjer efter behov og fortsætter denne cyklus, indtil det opnår en tilfredsstillende løsning.

Denne iterative “maker-checker” driftsstil er designet til at forbedre korrekthed, håndtere fejlformulerede forespørgsler til strukturerede databaser (fx NL2SQL) og sikre afbalancerede, resultater af høj kvalitet. I stedet for kun at stole på omhyggeligt designede promptkæder ejer systemet aktivt sin ræsonneringsproces. Det kan omskrive forespørgsler, der fejler, vælge forskellige hentemetoder og integrere flere værktøjer – såsom vektorsøgning i Azure AI Search, SQL-databaser eller brugerdefinerede API'er – før det færdiggør sit svar. Dette fjerner behovet for alt for komplekse orkestreringsrammer. I stedet kan en forholdsvis enkel løkke af “LLM-kald → værktøjsbrug → LLM-kald → …” skabe sofistikerede og godt funderede output.

![Agentic RAG Core Loop](../../../translated_images/da/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Eje ræsonneringsprocessen

Den afgørende egenskab, der gør et system “agentisk”, er dets evne til at eje sin ræsonneringsproces. Traditionelle RAG-implementeringer er ofte afhængige af, at mennesker foruddefinerer en sti for modellen: en tænke-kæde, der skitserer, hvad der skal hentes og hvornår.
Men når et system er virkelig agentisk, beslutter det internt, hvordan det skal gribe problemet an. Det udfører ikke bare et script; det bestemmer autonomt rækkefølgen af trin baseret på kvaliteten af den information, det finder.
For eksempel, hvis det bliver bedt om at skabe en produktlanceringsstrategi, stoler det ikke kun på en prompt, der beskriver hele forsknings- og beslutningsworkflowet. I stedet beslutter den agentiske model selvstændigt at:

1. Hente aktuelle markedsrapportmaterialer via Bing Web Grounding
2. Identificere relevante konkurrentdata via Azure AI Search.
3. Koble historiske interne salgstal sammen via Azure SQL Database.
4. Syntetisere fundene til en sammenhængende strategi orkestreret via Azure OpenAI Service.
5. Evaluere strategien for mangler eller uoverensstemmelser, og starte endnu en runde med hentning om nødvendigt.
Alle disse trin – forfine forespørgsler, vælge kilder, iterere indtil “tilfreds” med svaret – besluttes af modellen, ikke forudskrevet af et menneske.

## Iterative løkker, værktøjsintegration og hukommelse

![Tool Integration Architecture](../../../translated_images/da/tool-integration.0f569710b5c17c10.webp)

Et agentisk system er afhængigt af et loopet interaktionsmønster:

- **Indledende kald:** Brugerens mål (dvs. brugerprompten) præsenteres for LLM'en.
- **Værktøjsindkaldelse:** Hvis modellen identificerer manglende information eller tvetydige instruktioner, vælger den et værktøj eller en hentemetode – som en vektor-databaseforespørgsel (fx Azure AI Search Hybrid søgning over private data) eller et struktureret SQL-kald – for at samle mere kontekst.
- **Vurdering & forfining:** Efter at have gennemgået de returnerede data beslutter modellen, om informationen er tilstrækkelig. Hvis ikke, forfiner den forespørgslen, prøver et andet værktøj eller justerer sin tilgang.
- **Gentag indtil tilfreds:** Denne cyklus fortsætter, indtil modellen vurderer, at den har tilstrækkelig klarhed og belæg for at levere et endeligt, velovervejet svar.
- **Hukommelse & tilstand:** Fordi systemet opretholder tilstand og hukommelse på tværs af trin, kan det huske tidligere forsøg og deres udfald, undgå gentagne løkker og træffe mere informerede beslutninger, mens det skrider frem.

Over tid skaber dette en følelse af udviklende forståelse, som gør det muligt for modellen at navigere komplekse, flertrinsopgaver uden konstant menneskelig indgriben eller omskrivning af prompten.

## Håndtering af fejlsituationer og selvkorrektion

Agentic RAG's autonomi involverer også robuste selvkorrektionsmekanismer. Når systemet rammer blindgyder – såsom at hente irrelevante dokumenter eller støde på fejlformulerede forespørgsler – kan det:

- **Iterere og genforespørge:** I stedet for at returnere lavværdi-svar, prøver modellen nye søgestrategier, omskriver databaseforespørgsler eller ser på alternative datasæt.
- **Brug af diagnostiske værktøjer:** Systemet kan aktivere yderligere funktioner designet til at hjælpe det med at fejlfinde dets ræsonneringstrin eller bekræfte korrektheden af hentede data. Værktøjer som Azure AI Tracing vil være vigtige for at muliggøre robust observerbarhed og overvågning.
- **Tilbagefald på menneskelig overvågning:** For højt prioriterede eller gentagne fejlsituationer kan modellen markere usikkerhed og anmode om menneskelig vejledning. Når mennesket leverer korrigerende feedback, kan modellen inkorporere denne læring fremadrettet.

Denne iterative og dynamiske tilgang gør det muligt for modellen at forbedre sig kontinuerligt, hvilket sikrer, at det ikke blot er et one-shot system, men et der lærer af sine fejltrin under en given session.

![Self Correction Mechanism](../../../translated_images/da/self-correction.da87f3783b7f174b.webp)

## Agentgrænser

På trods af autonomien inden for en opgave er Agentic RAG ikke analog til Artificial General Intelligence. Dets “agentiske” evner er begrænset til de værktøjer, datakilder og politikker, som menneskelige udviklere stiller til rådighed. Det kan ikke opfinde sine egne værktøjer eller træde uden for de domænegrænser, der er sat. I stedet excellerer det i dynamisk orkestrering af de ressourcer, der er til rådighed.
Vigtige forskelle fra mere avancerede AI-former inkluderer:

1. **Domænespecifik autonomi:** Agentic RAG-systemer er fokuseret på at opnå brugerdefinerede mål inden for et kendt domæne ved at anvende strategier som forespørgselsomskrivelse eller værktøjsvalg for at forbedre resultater.
2. **Infrastrukturafhængighed:** Systemets kapaciteter afhænger af de værktøjer og data, som udviklerne integrerer. Det kan ikke overskride disse grænser uden menneskelig indgriben.
3. **Respekt for sikkerhedsforanstaltninger:** Etiske retningslinjer, overholdelsesregler og forretningspolitikker forbliver meget vigtige. Agentens frihed er altid begrænset af sikkerhedsforanstaltninger og overvågningsmekanismer (forhåbentlig?).

## Praktiske anvendelsestilfælde og værdi

Agentic RAG skiller sig ud i scenarier, der kræver iterativ forfining og præcision:

1. **Korrekthed-først miljøer:** Ved compliance-tjek, regulatorisk analyse eller juridisk research kan den agentiske model gentagne gange verificere fakta, konsultere flere kilder og omskrive forespørgsler, indtil den leverer et grundigt gennemgået svar.
2. **Komplekse databaseinteraktioner:** Når man arbejder med strukturerede data, hvor forespørgsler ofte kan fejle eller kræve justering, kan systemet autonomt forfine sine forespørgsler vha. Azure SQL eller Microsoft Fabric OneLake, så den endelige hentning stemmer overens med brugerens hensigt.
3. **Udvidede workflows:** Længerevarende sessioner kan udvikle sig, efterhånden som ny information dukker op. Agentic RAG kan løbende inkorporere nye data og justere strategier, efterhånden som det lærer mere om problemfeltet.

## Styring, gennemsigtighed og tillid

Efterhånden som disse systemer bliver mere autonome i deres ræsonnering, er styring og gennemsigtighed afgørende:

- **Forklarlig ræsonnering:** Modellen kan levere en revisionsspor af de forespørgsler, den har lavet, de kilder den har konsulteret, og ræsonneringstrinene den har taget for at nå sin konklusion. Værktøjer som Azure AI Content Safety og Azure AI Tracing / GenAIOps kan hjælpe med at opretholde gennemsigtighed og mindske risici.
- **Bias kontrol og balanceret hentning:** Udviklere kan justere hentningsstrategier for at sikre, at afbalancerede og repræsentative datakilder overvejes, og regelmæssigt revidere output for at opdage bias eller skæve mønstre ved hjælp af brugerdefinerede modeller til avancerede data science-organisationer, der bruger Azure Machine Learning.
- **Menneskelig overvågning og compliance:** For følsomme opgaver er menneskelig gennemgang stadig essentiel. Agentic RAG erstatter ikke menneskelig dømmekraft i high-stakes beslutninger – det supplerer den ved at levere mere grundigt gennemgåede muligheder.

At have værktøjer, der leverer en klar oversigt over handlinger, er afgørende. Uden dem kan det være meget vanskeligt at fejlfinde en flertrinsproces. Se følgende eksempel fra Literal AI (selskabet bag Chainlit) for et Agent-run:

![AgentRunExample](../../../translated_images/da/AgentRunExample.471a94bc40cbdc0c.webp)

## Konklusion

Agentic RAG repræsenterer en naturlig udvikling i, hvordan AI-systemer håndterer komplekse, dataintensive opgaver. Ved at anvende et loopet interaktionsmønster, autonomt vælge værktøjer og forfine forespørgsler, indtil et resultat af høj kvalitet opnås, bevæger systemet sig ud over statisk prompt-udførelse til en mere adaptiv, kontekstbevidst beslutningstager. Mens det stadig er begrænset af menneskeskabte infrastrukturer og etiske retningslinjer, muliggør disse agentiske evner rigere, mere dynamiske og i sidste ende mere nyttige AI-interaktioner for både virksomheder og slutbrugere.

### Har du flere spørgsmål om Agentic RAG?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre elever, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementer Retrieval Augmented Generation (RAG) med Azure OpenAI Service: Lær hvordan du bruger dine egne data med Azure OpenAI Service. Denne Microsoft Learn modul tilbyder en omfattende guide til implementering af RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering af generative AI-applikationer med Microsoft Foundry: Denne artikel dækker evalueringen og sammenligningen af modeller på offentligt tilgængelige datasæt, inklusive Agentic AI-applikationer og RAG-arkitekturer</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Hvad er Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: En komplet guide til agentbaseret Retrieval Augmented Generation – Nyheder fra generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: forøg kraften i din RAG med forespørgselsomformulering og selv-forespørgsel! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Tilføjelse af Agentiske Lag til RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Fremtiden for Vidensassistenter: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Hvordan man Bygger Agentiske RAG-Systemer</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Brug af Microsoft Foundry Agent Service til at skalere dine AI-agenter</a>

### Akademiske Artikler

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativ Forfining med Selvfeedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Sprogagenter med Verbal Forstærkningslæring</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Store Sprogsmodeller Kan Selv-Korrigere med Værktøj-Interaktiv Kritisk Gennemgang</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentisk Retrieval-Augmented Generation: En Undersøgelse af Agentisk RAG</a>

## Røgtestning af Denne Agent (Valgfrit)

Efter du har lært at implementere agenter i [Lesson 16](../16-deploying-scalable-agents/README.md), kan du røgteste denne lektions `TravelRAGAgent` — for at kontrollere at dens svar forbliver funderet i vidensbasen — med [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Se [`tests/README.md`](../tests/README.md) for hvordan du kører den.

## Forrige Lektion

[Mønster for Værktøjsbrug](../04-tool-use/README.md)

## Næste Lektion

[Bygning af Pålidelige AI-agenter](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->