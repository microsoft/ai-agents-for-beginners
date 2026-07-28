[![Agentic RAG](../../../translated_images/sv/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

# Agentic RAG

Den här lektionen ger en omfattande översikt över Agentic Retrieval-Augmented Generation (Agentic RAG), ett framväxande AI-paradigm där stora språkmodeller (LLMs) självständigt planerar sina nästa steg medan de hämtar information från externa källor. Till skillnad från statiska mönster med hämtning-och-läs, innebär Agentic RAG iterativa anrop till LLM, växlat med verktygs- eller funktionsanrop och strukturerade utgångar. Systemet utvärderar resultat, förfinar frågor, anropar ytterligare verktyg vid behov och fortsätter denna cykel tills en tillfredsställande lösning nås.

## Introduktion

Den här lektionen kommer att täcka

- **Förstå Agentic RAG:** Lär dig om det framväxande paradigmet inom AI där stora språkmodeller (LLMs) självständigt planerar sina nästa steg samtidigt som de hämtar information från externa datakällor.
- **Begrip Iterativ Maker-Checker-stil:** Förstå loopen av iterativa anrop till LLM, med inslag av verktygs- eller funktionsanrop och strukturerade utdata, utformade för att förbättra korrekthet och hantera felaktiga frågor.
- **Utforska praktiska tillämpningar:** Identifiera scenarion där Agentic RAG verkligen utmärker sig, såsom miljöer med fokus på korrekthet, komplexa databasintegrationer och förlängda arbetsflöden.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna/förstå:

- **Förstå Agentic RAG:** Lär dig om det framväxande paradigmet inom AI där stora språkmodeller (LLMs) självständigt planerar sina nästa steg samtidigt som de hämtar information från externa datakällor.
- **Iterativ Maker-Checker-stil:** Begrip konceptet med en loop av iterativa anrop till LLM, med inslag av verktygs- eller funktionsanrop och strukturerade utdata, utformade för att förbättra korrekthet och hantera felaktiga frågor.
- **Egen äganderätt över resonemangsprocessen:** Förstå systemets förmåga att äga sitt resonemangsprocess, fatta beslut om hur problem ska närmas utan att förlita sig på fördefinierade vägar.
- **Arbetsflöde:** Förstå hur en agentmodell självständigt beslutar att hämta marknadstrendrapporter, identifiera konkurrentdata, korrelera interna försäljningsmått, syntetisera fynd och utvärdera strategi.
- **Iterativa loopar, verktygsintegration och minne:** Lär dig om systemets beroende av ett loopat interaktionsmönster, med bevarande av tillstånd och minne över steg för att undvika repetitiva slingor och fatta informerade beslut.
- **Hantera felättestillstånd och självkorrektion:** Utforska systemets robusta självkorrektionsmekanismer, inklusive iteration och omfrågning, användande av diagnostiska verktyg och fallback till mänsklig övervakning.
- **Agentgränser:** Förstå begränsningarna för Agentic RAG, med fokus på domänspecifik autonomi, infrastrukturbundenhet och respekt för skyddsbarriärer.
- **Praktiska användningsfall och värde:** Identifiera scenarion där Agentic RAG utmärker sig, såsom miljöer med fokus på korrekthet, komplexa databasintegrationer och förlängda arbetsflöden.
- **Styrning, transparens och förtroende:** Lär dig vikten av styrning och transparens, inklusive förklarbart resonemang, bias-kontroll och mänsklig övervakning.

## Vad är Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) är ett framväxande AI-paradigm där stora språkmodeller (LLMs) självständigt planerar sina nästa steg samtidigt som de hämtar information från externa källor. Till skillnad från statiska mönster med hämtning-och-läs, innebär Agentic RAG iterativa anrop till LLM, växlat med verktygs- eller funktionsanrop och strukturerade utgångar. Systemet utvärderar resultat, förfinar frågor, anropar ytterligare verktyg vid behov och fortsätter denna cykel tills en tillfredsställande lösning nås. Denna iterativa “maker-checker”-stil förbättrar korrekthet, hanterar felaktiga frågor och säkerställer högkvalitativa resultat.

Systemet äger aktivt sitt resonemangsprocess, skriver om misslyckade frågor, väljer olika hämtmetoder och integrerar flera verktyg – såsom vektorsökning i Azure AI Search, SQL-databaser eller anpassade API:er – innan det slutgiltiga svaret fastställs. Det som särskiljer ett agentiskt system är dess förmåga att äga sitt resonemangsprocess. Traditionella RAG-implementeringar förlitar sig på fördefinierade vägar, men ett agentiskt system bestämmer självständigt stegens ordning baserat på kvaliteten på informationen det hittar.

## Definition av Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) är ett framväxande paradigm inom AI-utveckling där LLM inte bara hämtar information från externa datakällor utan även självständigt planerar sina nästa steg. Till skillnad från statiska mönster med hämtning-och-läs eller noggrant skriptade promptsekvenser, involverar Agentic RAG en loop av iterativa anrop till LLM, växlat med verktygs- eller funktionsanrop och strukturerade utdata. Vid varje steg utvärderar systemet de resultat det fått, beslutar om det ska förfina sina frågor, anropar ytterligare verktyg vid behov och fortsätter denna cykel tills det uppnår en tillfredsställande lösning.

Denna iterativa “maker-checker”-driftsstil är utformad för att förbättra korrekthet, hantera felaktiga frågor till strukturerade databaser (t.ex. NL2SQL) och säkerställa balanserade, högkvalitativa resultat. Istället för att enbart förlita sig på noggrant konstruerade promptkedjor, äger systemet aktivt sitt resonemangsprocess. Det kan skriva om frågor som misslyckas, välja olika hämtmetoder och integrera flera verktyg – såsom vektorsökning i Azure AI Search, SQL-databaser eller anpassade API:er – innan det slutgiltiga svaret fastställs. Detta eliminerar behovet av alltför komplexa orkestrationsramverk. Istället kan en relativt enkel loop av ”LLM-anrop → verktygsanvändning → LLM-anrop → …” ge sofistikerade och välgrundade utdata.

![Agentic RAG Core Loop](../../../translated_images/sv/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Äga resonemangsprocessen

Den avgörande egenskapen som gör ett system “agentiskt” är dess förmåga att äga sitt resonemangsprocess. Traditionella RAG-implementeringar bygger ofta på att människor fördefinierar en väg för modellen: en tankekedja som beskriver vad som ska hämtas och när.
Men när ett system verkligen är agentiskt, bestämmer det internt hur problem ska närmas. Det följer inte bara ett skript; det bestämmer självständigt sekvensen av steg baserat på kvaliteten på den information det hittar.
Till exempel, om det blir ombett att skapa en produktlanseringsstrategi, förlitar det sig inte enbart på en prompt som beskriver hela forsknings- och beslutsgången. Istället bestämmer den agentiska modellen självständigt att:

1. Hämta aktuella marknadstrendrapporter med hjälp av Bing Web Grounding
2. Identifiera relevant konkurrentdata med Azure AI Search.
3. Korrelera historiska interna försäljningsmått med Azure SQL Database.
4. Syntetisera fynden till en sammanhängande strategi orkestrerad via Azure OpenAI Service.
5. Utvärdera strategin för luckor eller inkonsekvenser, och om nödvändigt initiera en ny hämtning.
Alla dessa steg — att förfina frågor, välja källor, iterera tills man är “nöjd” med svaret — beslutas av modellen, inte förhands-skriptade av en människa.

## Iterativa loopar, verktygsintegration och minne

![Tool Integration Architecture](../../../translated_images/sv/tool-integration.0f569710b5c17c10.webp)

Ett agentiskt system förlitar sig på ett loopat interaktionsmönster:

- **Initierande anrop:** Användarens mål (dvs. användarprompt) presenteras för LLM.
- **Verktygsanrop:** Om modellen identifierar saknad information eller tvetydiga instruktioner, väljer den ett verktyg eller en hämtmetod — som en vektordatabasfråga (t.ex. Azure AI Search Hybrid-sökning över privata data) eller en strukturerad SQL-anrop — för att samla mer kontext.
- **Bedömning & Förfining:** Efter att ha granskat den returnerade datan beslutar modellen om informationen räcker. Om inte, förfinar den frågan, testar ett annat verktyg eller justerar sitt tillvägagångssätt.
- **Upprepa tills nöjd:** Denna cykel fortsätter tills modellen bedömer att den har tillräcklig klarhet och bevis för att leverera ett slutgiltigt, välmotiverat svar.
- **Minne & Tillstånd:** Eftersom systemet bibehåller tillstånd och minne över stegen, kan det minnas tidigare försök och deras utfall, undvika repetitiva loopar och fatta mer informerade beslut under processen.

Över tid skapar detta en känsla av en utvecklande förståelse, vilket gör det möjligt för modellen att navigera komplexa, flerstegsuppgifter utan att en människa ständigt behöver ingripa eller omformulera prompten.

## Hantering av felättestillstånd och självkorrektion

Agentic RAG:s autonomi innefattar också robusta självkorrektionsmekanismer. När systemet når återvändsgränder — till exempel att hämta irrelevanta dokument eller stöta på felaktiga frågor — kan det:

- **Iterera och omfråga:** Istället för att returnera lågkvalitativa svar försöker modellen nya sökstrategier, skriver om databasfrågor eller tittar på alternativa datamängder.
- **Använda diagnostiska verktyg:** Systemet kan anropa ytterligare funktioner som hjälper det att felsöka sina resonemangs-steg eller bekräfta korrektheten i hämtad data. Verktyg som Azure AI Tracing blir viktiga för att möjliggöra robust observerbarhet och övervakning.
- **Fallback till mänsklig övervakning:** Vid scenarier med hög risk eller återkommande misslyckanden kan modellen markera osäkerhet och begära mänsklig vägledning. När människan ger korrigerande feedback kan modellen inkorporera denna lärdom framgent.

Detta iterativa och dynamiska tillvägagångssätt gör att modellen kan förbättras kontinuerligt, vilket säkerställer att det inte bara är ett engångssystem utan ett som lär sig av sina misstag under en session.

![Self Correction Mechanism](../../../translated_images/sv/self-correction.da87f3783b7f174b.webp)

## Agentgränser

Trots sin autonomi inom en uppgift är Agentic RAG inte analogt med artificiell generell intelligens. Dess “agentiska” förmågor är begränsade till verktygen, datakällorna och policys som tillhandahålls av mänskliga utvecklare. Det kan inte uppfinna egna verktyg eller gå utanför de domängränser som satts upp. I stället utmärker det sig i att dynamiskt orkestrera de resurser som finns till hands.
Viktiga skillnader från mer avancerade AI-former inkluderar:

1. **Domänspecifik autonomi:** Agentic RAG-system är fokuserade på att uppnå användardefinierade mål inom en känd domän, och använder strategier som omskrivning av frågor eller val av verktyg för att förbättra resultat.
2. **Infrastrukturbunden:** Systemets kapaciteter är beroende av de verktyg och data som integrerats av utvecklare. Det kan inte överskrida dessa gränser utan mänskligt ingripande.
3. **Respekt för skyddsbarriärer:** Etiska riktlinjer, efterlevnadsregler och företagsregler är fortsatt mycket viktiga. Agentens frihet är alltid begränsad av säkerhetsåtgärder och övervakningsmekanismer (förhoppningsvis?).

## Praktiska användningsfall och värde

Agentic RAG utmärker sig i scenarion som kräver iterativ förfining och precision:

1. **Miljöer med fokus på korrekthet:** Vid efterlevnadskontroller, regulatorisk analys eller juridisk forskning kan den agentiska modellen upprepade gånger verifiera fakta, konsultera flera källor och skriva om frågor tills den producerar ett noga granskat svar.
2. **Komplexa databasintegrationer:** Vid hantering av strukturerad data där frågor ofta kan misslyckas eller behöva justeras kan systemet självständigt förfina sina frågor med Azure SQL eller Microsoft Fabric OneLake, vilket säkerställer att slutlig hämtning stämmer överens med användarens avsikt.
3. **Förlängda arbetsflöden:** Längre sessioner kan utvecklas efterhand som ny information dyker upp. Agentic RAG kan kontinuerligt införliva nya data och justera strategier när den lär sig mer om problemområdet.

## Styrning, transparens och förtroende

Eftersom dessa system blir mer autonoma i sitt resonemang är styrning och transparens avgörande:

- **Förklarbart resonemang:** Modellen kan ge en spårbar audit-logg över de frågor den ställt, de källor den konsulterat och de resonemangssteg den tagit för att nå sin slutsats. Verktyg som Azure AI Content Safety och Azure AI Tracing / GenAIOps kan hjälpa till att upprätthålla transparens och minska risker.
- **Bias-kontroll och balanserad hämtning:** Utvecklare kan justera sökstrategier för att säkerställa att balanserade, representativa datakällor beaktas, och regelbundet granska utdata för att upptäcka bias eller snedvridna mönster med hjälp av anpassade modeller för avancerade data science-organisationer som använder Azure Machine Learning.
- **Mänsklig övervakning och efterlevnad:** Vid känsliga uppgifter förblir mänsklig granskning essentiell. Agentic RAG ersätter inte mänskligt omdöme i kritiska beslut — det förstärker det genom att leverera noggrant granskade alternativ.

Att ha verktyg som ger en tydlig redovisning över åtgärder är avgörande. Utan dem kan det vara mycket svårt att felsöka en flerstegsprocess. Se följande exempel från Literal AI (företaget bakom Chainlit) för en Agentkörning:

![AgentRunExample](../../../translated_images/sv/AgentRunExample.471a94bc40cbdc0c.webp)

## Slutsats

Agentic RAG representerar en naturlig utveckling i hur AI-system hanterar komplexa, dataintensiva uppgifter. Genom att anta ett loopat interaktionsmönster, självständigt välja verktyg och förfina frågor tills ett högkvalitativt resultat uppnås rör sig systemet bortom statiskt promptföljande till en mer adaptiv, kontextmedveten beslutsfattare. Trots att den fortfarande är bunden av mänskligt definierade infrastrukturer och etiska riktlinjer, möjliggör dessa agentiska förmågor rikare, mer dynamiska och i slutändan mer användbara AI-interaktioner för både företag och slutanvändare.

### Fler frågor om Agentic RAG?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra elever, delta i office hours och få svar på dina frågor om AI-agenter.

## Ytterligare resurser

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementera Retrieval Augmented Generation (RAG) med Azure OpenAI Service: Lär dig hur du använder dina egna data med Azure OpenAI Service. Den här Microsoft Learn-modulen erbjuder en omfattande guide för att implementera RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Utvärdering av generativa AI-applikationer med Microsoft Foundry: Denna artikel täcker utvärdering och jämförelse av modeller på offentligt tillgängliga dataset, inklusive Agentic AI-applikationer och RAG-arkitekturer</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Vad är Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: En komplett guide till agentbaserad Retrieval Augmented Generation – Nyheter från generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: turbo-ladda din RAG med frågeomformulering och självfråga! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Lägga till Agentiska lager till RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Framtiden för kunskapassistenter: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Hur man bygger agentiska RAG-system</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Använda Microsoft Foundry Agent Service för att skala dina AI-agenter</a>

### Akademiska artiklar

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativ förbättring med självfeedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Språkagenter med verbal förstärkningsinlärning</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Stora språkmodeller kan självkorrigera med verktygsinteraktiv kritik</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: En översikt om agentisk RAG</a>

## Röktesta denna agent (valfritt)

Efter att du lärt dig att distribuera agenter i [Lektion 16](../16-deploying-scalable-agents/README.md), kan du röktesta denna lektions `TravelRAGAgent` — för att kontrollera att dess svar förblir förankrade i kunskapsbasen — med [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Se [`tests/README.md`](../tests/README.md) för hur man kör det.

## Föregående lektion

[Designmönster för verktygsanvändning](../04-tool-use/README.md)

## Nästa lektion

[Bygga pålitliga AI-agenter](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->