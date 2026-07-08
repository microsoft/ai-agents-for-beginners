[![Agentic RAG](../../../translated_images/da/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

# Agentic RAG

Denne lektion giver en omfattende oversigt over Agentic Retrieval-Augmented Generation (Agentic RAG), et nyt AI-paradigme hvor store sprogmodeller (LLM'er) selvstændigt planlægger deres næste skridt samtidig med at de henter information fra eksterne kilder. I modsætning til statiske hent-og-læs mønstre involverer Agentic RAG iterative kald til LLM'en, afbrudt af værktøjs- eller funktionskald og strukturerede output. Systemet evaluerer resultater, forfiner forespørgsler, kalder yderligere værktøjer om nødvendigt og fortsætter denne cyklus, indtil en tilfredsstillende løsning opnås.

## Introduktion

Denne lektion vil dække

- **Forstå Agentic RAG:** Lær om det nye paradigme inden for AI, hvor store sprogmodeller (LLM'er) selvstændigt planlægger deres næste skridt, mens de henter information fra eksterne datakilder.
- **Forstå Iterativ Maker-Checker Stil:** Forstå løkken med iterative kald til LLM, afbrudt af værktøjs- eller funktionskald og strukturerede output, designet til at forbedre korrekthed og håndtere fejlagtige forespørgsler.
- **Udforsk Praktiske Anvendelser:** Identificer scenarier hvor Agentic RAG udmærker sig, såsom korrekte-først miljøer, komplekse databaseinteraktioner og udvidede arbejdsgange.

## Læringsmål

Efter at have afsluttet denne lektion vil du vide, hvordan du/forstå:

- **Forståelse af Agentic RAG:** Lær om det nye paradigme inden for AI, hvor store sprogmodeller (LLM'er) selvstændigt planlægger deres næste skridt, mens de henter information fra eksterne datakilder.
- **Iterativ Maker-Checker Stil:** Forstå konceptet med en løkke af iterative kald til LLM, afbrudt af værktøjs- eller funktionskald og strukturerede output, designet til at forbedre korrekthed og håndtere fejlagtige forespørgsler.
- **At eje ræsonnementsprocessen:** Forstå systemets evne til at have kontrol over sin ræsonnementsproces og træffe beslutninger om, hvordan problemer skal gribes an uden at stole på foruddefinerede veje.
- **Arbejdsgang:** Forstå, hvordan en agentmodel selvstændigt beslutter at hente markedsrapportér, identificere konkurrentdata, korrelere interne salgsmetrikker, syntetisere fund og evaluere strategien.
- **Iterative løkker, værktøjsintegration og hukommelse:** Lær om systemets afhængighed af et loopet interaktionsmønster, der opretholder tilstand og hukommelse på tværs af trin for at undgå gentagne løkker og træffe informerede beslutninger.
- **Håndtering af fejltilstande og selvkorrektion:** Udforsk systemets robuste selvkorrektionsmekanismer, inklusive iteration og genforespørgsel, brug af diagnostiske værktøjer og tilbagetrækning til menneskelig overvågning.
- **Agentgrænser:** Forstå begrænsningerne for Agentic RAG med fokus på domænespecifik autonomi, infrastrukturafhængighed og respekt for sikkerhedsforanstaltninger.
- **Praktiske brugssager og værdi:** Identificer scenarier hvor Agentic RAG udmærker sig, såsom korrekthed-først miljøer, komplekse databaseinteraktioner og udvidede arbejdsgange.
- **Governance, transparens og tillid:** Lær om vigtigheden af governance og transparens, inklusive forklarbar ræsonnering, bias-kontrol og menneskelig overvågning.

## Hvad er Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) er et nyt AI-paradigme, hvor store sprogmodeller (LLM'er) selvstændigt planlægger deres næste skridt, mens de henter information fra eksterne kilder. I modsætning til statiske hent-og-læs mønstre involverer Agentic RAG iterative kald til LLM, afbrudt af værktøjs- eller funktionskald og strukturerede output. Systemet evaluerer resultater, forfiner forespørgsler, kalder yderligere værktøjer om nødvendigt, og fortsætter denne cyklus indtil en tilfredsstillende løsning opnås. Denne iterative ”maker-checker” stil forbedrer korrekthed, håndterer fejlagtige forespørgsler og sikrer resultater af høj kvalitet.

Systemet ejer aktivt sin ræsonnementsproces, omskriver mislykkede forespørgsler, vælger forskellige hentemetoder og integrerer flere værktøjer – såsom vektorsøgning i Azure AI Search, SQL-databaser eller tilpassede API'er – før det færdiggør sit svar. Den særlige kvalitet ved et agentbaseret system er dets evne til at eje sin ræsonnementsproces. Traditionelle RAG-implementeringer stole på foruddefinerede veje, men et agentisk system bestemmer selvstændigt rækkefølgen af trin baseret på kvaliteten af den information, det finder.

## Definition af Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) er et nyt paradigme inden for AI-udvikling, hvor LLM'er ikke bare henter information fra eksterne datakilder, men også selvstændigt planlægger deres næste skridt. I modsætning til statiske hent-og-læs mønstre eller omhyggeligt scriptsatte promptsekvenser involverer Agentic RAG en løkke af iterative kald til LLM, afbrudt af værktøjs- eller funktionskald og strukturerede output. Ved hvert skridt evaluerer systemet de opnåede resultater, beslutter om det skal forfine sine forespørgsler, kalder ekstra værktøjer ved behov og fortsætter denne cyklus, indtil det når en tilfredsstillende løsning.

Denne iterative ”maker-checker” driftsform er designet til at forbedre korrektheden, håndtere fejlbehæftede forespørgsler til strukturerede databaser (f.eks. NL2SQL) og sikre balancerede, resultater af høj kvalitet. I stedet for kun at stole på omhyggeligt konstruerede promptkæder ejer systemet aktivt sin ræsonnementsproces. Det kan omskrive fejlede forespørgsler, vælge forskellige hentemetoder og integrere flere værktøjer – såsom vektorsøgning i Azure AI Search, SQL-databaser eller tilpassede API'er – før det færdiggør sit svar. Dette fjerner behovet for alt for komplekse orkestreringsrammer. I stedet kan en relativt simpel løkke af ”LLM-kald → værktøjsbrug → LLM-kald → …” resultere i sofistikerede og veldokumenterede output.

![Agentic RAG Core Loop](../../../translated_images/da/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## At eje ræsonnementsprocessen

Den særlige kvalitet, der gør et system ”agentisk”, er dets evne til at eje sin ræsonnementsproces. Traditionelle RAG-implementeringer er ofte afhængige af, at mennesker foruddefinerer en sti for modellen: en chain-of-thought, der skitserer, hvad der skal hentes og hvornår.
Men når et system virkelig er agentisk, beslutter det internt, hvordan det skal gribe problemet an. Det udfører ikke bare et script; det fastlægger selvstændigt rækkefølgen af trin baseret på kvaliteten af den information, det finder.
For eksempel, hvis det bliver bedt om at skabe en produktlanceringsstrategi, er det ikke kun afhængigt af en prompt, der beskriver hele undersøgelses- og beslutningsprocessen. I stedet beslutter det agentiske model selvstændigt at:

1. Hente aktuelle markedsrapportér ved hjælp af Bing Web Grounding
2. Identificere relevant konkurrentdata ved hjælp af Azure AI Search.
3. Korrelere historiske interne salgsmetrikker ved hjælp af Azure SQL Database.
4. Syntetisere fundene til en sammenhængende strategi orkestreret via Azure OpenAI Service.
5. Evaluere strategien for mangler eller inkonsistenser og om nødvendigt igangsætte endnu en runde af hentninger.
Alle disse trin – forfining af forespørgsler, valg af kilder, iteration indtil ”tilfreds” med svaret – besluttes af modellen og ikke forudskrevet af et menneske.

## Iterative løkker, værktøjsintegration og hukommelse

![Tool Integration Architecture](../../../translated_images/da/tool-integration.0f569710b5c17c10.webp)

Et agentisk system er afhængigt af et loopet interaktionsmønster:

- **Initialt kald:** Brugerens mål (dvs. brugerprompten) præsenteres for LLM'en.
- **Værktøjskald:** Hvis modellen identificerer manglende information eller tvetydige instruktioner, vælger den et værktøj eller en hentemetode – som en forespørgsel til en vektordatabase (f.eks. Azure AI Search Hybrid-søgning over private data) eller et struktureret SQL-kald – for at indsamle mere kontekst.
- **Vurdering & forfining:** Efter at have gennemgået de returnerede data beslutter modellen, om informationen er tilstrækkelig. Hvis ikke, forfiner den forespørgslen, prøver et andet værktøj eller tilpasser sin tilgang.
- **Gentag indtil tilfreds:** Denne cyklus fortsætter, indtil modellen vurderer, at den har tilstrækkelig klarhed og evidens til at give et endeligt, velovervejet svar.
- **Hukommelse & tilstand:** Fordi systemet opretholder tilstand og hukommelse på tværs af trin, kan det huske tidligere forsøg og deres resultater, undgå gentagne løkker og træffe mere informerede beslutninger efterhånden som processen skrider frem.

Over tid skaber dette en følelse af udviklende forståelse, hvilket muliggør at modellen kan navigere komplekse, flertrinsopgaver uden at kræve konstant menneskelig indgriben eller omskrivning af prompten.

## Håndtering af fejltilstande og selvkorrektion

Agentic RAG's autonomi omfatter også robuste selvkorrektionsmekanismer. Når systemet støder på blindgyder – såsom at hente irrelevante dokumenter eller møde fejlagtige forespørgsler – kan det:

- **Iterere og genforespørge:** I stedet for at returnere lavværdige svar forsøger modellen nye søgestrategier, omskriver databaseforespørgsler eller undersøger alternative datasæt.
- **Brug af diagnostiske værktøjer:** Systemet kan kalde ekstra funktioner designet til at hjælpe med at debugge ræsonnementstrin eller bekræfte korrektheden af hentede data. Værktøjer som Azure AI Tracing vil være vigtige for at muliggøre robust observabilitet og overvågning.
- **Tilbagetrækning til menneskelig overvågning:** For kritiske eller gentagne fejlscenarier kan modellen markere usikkerhed og anmode om menneskelig vejledning. Når mennesket giver korrigerende feedback, kan modellen inkorporere denne læring fremadrettet.

Denne iterative og dynamiske tilgang tillader modellen at forbedre sig kontinuerligt, hvilket sikrer at den ikke blot er et engangssystem, men et der lærer af sine fejltrin under en given session.

![Self Correction Mechanism](../../../translated_images/da/self-correction.da87f3783b7f174b.webp)

## Agentgrænser

Selvom Agentic RAG har autonomi inden for en opgave, er det ikke analogt med Kunstig Generel Intelligens. Dets ”agentiske” evner er begrænset til de værktøjer, datakilder og politikker, der er leveret af menneskelige udviklere. Det kan ikke opfinde sine egne værktøjer eller træde uden for de domænegrænser, der er sat. I stedet udmærker det sig i dynamisk at orkestrere de tilgængelige ressourcer.
Vigtige forskelle i forhold til mere avancerede AI-former inkluderer:

1. **Domænespecifik autonomi:** Agentic RAG-systemer fokuserer på at opnå brugerdefinerede mål inden for et kendt domæne og anvender strategier som forespørgselsomskrivning eller værktøjsvalg for at forbedre resultater.
2. **Infrastrukturafhængighed:** Systemets kapaciteter afhænger af de værktøjer og data, som udviklere integrerer. Det kan ikke overskride disse grænser uden menneskelig indgriben.
3. **Respekt for sikkerhedsforanstaltninger:** Etiske retningslinjer, overholdelsesregler og forretningspolitikker forbliver yderst vigtige. Agentens frihed er altid begrænset af sikkerhedsforanstaltninger og overvågningsmekanismer (forhåbentlig).

## Praktiske brugssager og værdi

Agentic RAG excellerer i scenarier, der kræver iterativ forfining og præcision:

1. **Korrektion-først miljøer:** I compliance-tjek, reguleringsanalyse eller juridisk forskning kan den agentiske model gentagne gange verificere fakta, konsultere flere kilder og omskrive forespørgsler, indtil den producerer et grundigt kontrolleret svar.
2. **Komplekse databaseinteraktioner:** Når man arbejder med strukturerede data, hvor forespørgsler ofte kan fejle eller kræve tilpasning, kan systemet selvstændigt forfine sine forespørgsler ved hjælp af Azure SQL eller Microsoft Fabric OneLake og sikre, at den endelige hentning stemmer overens med brugerens intention.
3. **Udvidede arbejdsgange:** Længerevarende sessioner kan udvikle sig, efterhånden som ny information dukker op. Agentic RAG kan løbende inkorporere nye data og ændre strategier, efterhånden som den lærer mere om problemområdet.

## Governance, transparens og tillid

Efterhånden som disse systemer bliver mere autonome i deres ræsonnement, er governance og transparens afgørende:

- **Forklarbar ræsonnering:** Modellen kan levere en revisionssti over de forespørgsler, den foretager, de kilder den konsulterer, og ræsonnementstrinene den tager for at nå sin konklusion. Værktøjer som Azure AI Content Safety og Azure AI Tracing / GenAIOps kan hjælpe med at opretholde transparens og mindske risici.
- **Bias-kontrol og balanceret hentning:** Udviklere kan justere hentningsstrategier for at sikre, at balancerede, repræsentative datakilder overvejes, og regelmæssigt revidere output for at opdage bias eller forskubbede mønstre ved hjælp af tilpassede modeller for avancerede data science organisationer ved brug af Azure Machine Learning.
- **Menneskelig overvågning og overholdelse:** For følsomme opgaver forbliver menneskelig gennemgang essentiel. Agentic RAG erstatter ikke menneskelig dømmekraft i beslutninger med høje indsats – det supplerer den ved at levere mere grundigt kontrollerede muligheder.

At have værktøjer, der giver en klar oversigt over handlinger, er essentielt. Uden dem kan debugging af en flertrinsproces være meget vanskelig. Se følgende eksempel fra Literal AI (firmaet bag Chainlit) for en Agent-kørsel:

![AgentRunExample](../../../translated_images/da/AgentRunExample.471a94bc40cbdc0c.webp)

## Konklusion

Agentic RAG repræsenterer en naturlig udvikling i måden, AI-systemer håndterer komplekse, dataintensive opgaver på. Ved at anvende et loopet interaktionsmønster, selvstændigt vælge værktøjer og forfine forespørgsler indtil et resultat af høj kvalitet opnås, bevæger systemet sig ud over statisk promptfølgning til en mere adaptiv og kontekstbevidst beslutningstager. Selvom det stadig er begrænset af menneskeskabte infrastrukturer og etiske retningslinjer, giver disse agentiske evner rigere, mere dynamiske og i sidste ende mere brugbare AI-interaktioner for både virksomheder og slutbrugere.

### Har du flere spørgsmål om Agentic RAG?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementer Retrieval Augmented Generation (RAG) med Azure OpenAI Service: Lær hvordan du bruger dine egne data med Azure OpenAI Service. Denne Microsoft Learn modul giver en omfattende guide til implementering af RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering af generative AI-applikationer med Microsoft Foundry: Denne artikel dækker evaluering og sammenligning af modeller på offentligt tilgængelige datasæt, inklusiv Agentic AI-applikationer og RAG-arkitekturer</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Hvad er Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: En komplet guide til agentbaseret Retrieval Augmented Generation – Nyheder fra generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: turbocharge din RAG med forespørgselsomformulering og selv-forespørgsel! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Tilføjelse af Agentiske Lag til RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Kommende videnassistenter: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Sådan bygger du agentiske RAG-systemer</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Brug af Microsoft Foundry Agent Service til at skalere dine AI-agenter</a>

### Akademiske artikler

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativ forfining med selv-feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Sprogagenter med verbal forstærkningslæring</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Store sprogmodeller kan selvkorrigere med værktøjs-interaktiv kritik</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: En undersøgelse af Agentic RAG</a>

## Forrige lektion

[Tool Use Design Pattern](../04-tool-use/README.md)

## Næste lektion

[Byg tillidsværdige AI-agenter](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->