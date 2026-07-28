# AI-agenter för nybörjare - Studiematerial

Använd denna guide som en praktisk följeslagare medan du går igenom kursen. Den är
inte avsedd att ersätta lektionerna. Den hjälper dig att bestämma var du ska börja,
vad du ska leta efter i varje lektion och hur du kopplar samman idéerna till en liten fungerande agent-
demo.

Om detta är din första gång här, börja enkelt:

1. Läs [Kursuppsättning](./00-course-setup/README.md).
2. Genomför Lektion 01-06 i ordning.
3. Ha en liten demoidé i åtanke medan du lär dig.
4. Efter varje lektion, fråga: "Vad kan min agent göra nu som den inte kunde
   göra tidigare?"

## En enkel demo att ha i åtanke

Ett bra sätt att lära sig agenter är att följa en demoidé genom hela kursen.

Exempel på demo: **en kursassistent-agent**.

Användaren frågar:

> "Jag vill lära mig hur agenter använder verktyg. Hitta rätt lektioner, sammanfatta vad
> jag bör läsa först, och ge mig en kort övningsuppgift."

En vanlig chatbot kan svara utifrån det den redan kan. En agent kan göra mer:

1. **Läsa eller söka i kursfiler** för att hitta rätt lektioner.
2. **Använda verktyg** för att hämta lektionlänkar, exempel eller stödmaterial.
3. **Planera** en kort inlärningsväg istället för att ge ett långt svar.
4. **Använda kontext** från den aktuella konversationen för att hålla fokus på lärarens
   mål.
5. **Komma ihåg användbara preferenser** om applikationen stödjer minne.
6. **Visa spår, referenser eller loggar** så att användaren kan förstå vad som hänt.
7. **Tillämpa skyddsåtgärder** innan riskfyllda handlingar eller användning av känslig data sker.

När du studerar varje lektion, återvänd till denna demo och fråga: vilken ny funktion
skulle denna lektion lägga till?

## Vad du bygger mot

I slutet av kursen bör du kunna förklara och bygga agentsystem
som kombinerar dessa delar:

| Del | Vad det betyder på vardagsspråk | I demo |
|------|----------------------------|-------------|
| Modell | Den resonemangsmotor som tolkar användarens förfrågan | Förstår att eleven vill ha lektioner om verktygsanvändning |
| Verktyg | Funktioner, API:er, filer, webbläsare eller tjänster agenten kan använda | Söker i repo eller hämtar lektionsinnehåll |
| Kunskap | Dokument eller data som används för att förankra svaret | Kursens README-filer och lektionsmaterial |
| Kontext | Information som inkluderas i nästa modellanrop | Användarens mål och verktygsresultat |
| Minne | Information som sparas för senare användning | Eleven föredrar praktiska Python-exempel |
| Planering | Bryter ner ett större mål till mindre steg | Hitta lektioner, sammanfatta dem, föreslå övningar |
| Orkestrering | Dirigerar arbete över verktyg, steg eller agenter | En planerare anropar ett sökverktyg, sedan en sammanfattare |
| Tillit | Säkerhet, utvärdering och observerbarhet | Loggar verktygsanrop och frågar innan högriskåtgärder |

## Modeller och leverantörer

Kodexemplen i kursen använder **Microsoft Agent Framework (MAF)** och riktar sig mot **Azure OpenAI Responses API** — den rekommenderade API:n framöver, som kombinerar chatt-kompletteringar, verktygsanrop, multimodala input och tillståndsbaserade konversationer i en enda API-yta. Du kopplar antingen via ett **Microsoft Foundry**-projekt (`FoundryChatClient`) eller direkt till Azure OpenAI (`OpenAIChatClient`).

När du arbetar med lektionerna har du några leverantörsalternativ:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — huvudvägen som används i lektionsserien. Logga in med `az login` för nyckellös Entra ID-autentisering.
- **Foundry Local** — kör modeller helt på enheten genom en OpenAI-kompatibel API (ingen moln, inga API-nycklar). Perfekt för offline- eller kostnadsfri experimentering. Se [Kursuppsättning](./00-course-setup/README.md).
- **MiniMax** — en OpenAI-kompatibel leverantör med stora kontextmodeller, användbar som en drop-in-alternativ.

> **Notera:** GitHub Models är föråldrat (avslutas juli 2026) och stöder inte Responses API. Exemplen har uppdaterats till att använda Azure OpenAI / Microsoft Foundry istället.

## Välj din inlärningsväg

Du kan ta hela kursen i ordning eller hoppa till en väg baserat på vad du vill
bygga.

| Om ditt mål är att... | Börja med | Studera sedan |
|-----------------------|------------|------------|
| Förstå vad agenter är | 01, 02, 03 | 04, 05, 06 |
| Bygga en agent som använder verktyg | 04 | 05, 07, 14 |
| Bygga en RAG-baserad agent | 05 | 04, 06, 12 |
| Designa flerstegsarbetsflöden | 07 | 08, 09, 14 |
| Förstå multiagent-system | 08 | 07, 09, 11 |
| Förbereda agenter för produktion | 06, 10 | 12, 13, 16, 18 |
| Distribuera och skala agenter på Foundry | 10, 16 | 06, 13, 18 |
| Bygga lokala / offline-först agenter | 17 | 04, 05, 11 |
| Utforska protokoll och webbläsarautomatisering | 11, 15 | 10, 18 |

Tips: om du är ny på agenter, hoppa inte över Lektion 01-06. De ger dig
vokabulären du behöver för resten av kursen.

## Lektion-för-lektion-guide

| Lektion | Vad du lär dig | Prova detta efter lektionen |
|--------|----------------|---------------------------|
| [01 - Introduktion till AI-agenter](./01-intro-to-ai-agents/README.md) | Vad som gör en agent annorlunda än en vanlig chatbot. | Förklara din demoidé som en agent, inte bara en chatt-app. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | Hur ramverk hjälper till med modeller, verktyg, tillstånd och arbetsflöden. | Identifiera vilka delar av din demo ett ramverk skulle hantera. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Vanliga mönster för att designa agentbeteende. | Skissa användarresan innan du skriver kod. |
| [04 - Verktygsanvändning](./04-tool-use/README.md) | Hur agenter anropar verktyg för att hämta data eller agera. | Definiera ett verktyg din demoeagent skulle behöva. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Hur återhämtning förankrar agentsvar i dokument eller data. | Bestäm vilken kunskapskälla din demo bör söka i. |
| [06 - Pålitliga agenter](./06-building-trustworthy-agents/README.md) | Hur man lägger till skydd, övervakning och säkrare beteende. | Lägg till en regel för när agenten ska fråga användaren först. |
| [07 - Planeringsdesign](./07-planning-design/README.md) | Hur agenter delar upp större mål i mindre steg. | Skriv en trestegsplan för din demoförfrågan. |
| [08 - Multi-agentdesign](./08-multi-agent/README.md) | När man ska dela arbete över specialiserade agenter. | Bestäm om din demo behöver en eller flera agenter. |
| [09 - Metakognition](./09-metacognition/README.md) | Hur agenter kan granska och förbättra sin egen output. | Lägg till en slutlig självgranskning innan agenten svarar. |
| [10 - AI-agenter i produktion](./10-ai-agents-production/README.md) | Vad som förändras när en agent går från demo till produktion. | Lista vad du skulle övervaka: kvalitet, kostnad, fördröjning, fel. |
| [11 - Agentic Protocols](./11-agentic-protocols/README.md) | Hur protokoll kopplar agenter till verktyg och andra agenter. | Identifiera var ett standardprotokoll kan förenkla integrationen. |
| [12 - Kontextengineering](./12-context-engineering/README.md) | Hur man väljer, trimmar, isolerar och hanterar kontext. | Bestäm vad som ska ingå i prompten och vad som ska lämnas utanför. |
| [13 - Agentminne](./13-agent-memory/README.md) | Hur agenter kan spara användbar information mellan interaktioner. | Välj en säker preferens som din demo kan komma ihåg. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Ramverksspecifika byggstenar för agenter och arbetsflöden, plus att vara värd för LangChain/LangGraph-agenter på Microsoft Foundry. | Mappa dina demosteg till ramverksbegrepp. |
| [15 - Agenter för datorskärmanvändning](./15-browser-use/README.md) | Hur agenter kan interagera med webbläsare eller UI-ytor, inklusive verkliga exempel som Microsoft Project Opal. | Välj en webbläsaruppgift som fortfarande bör kräva användarbekräftelse. |
| [16 - Distribuera skalbara agenter](./16-deploying-scalable-agents/README.md) | Hur man tar en agent från prototyp till en skalbar, observerbar produktionsdistribution på Microsoft Foundry (hostade agenter, modellroutning, caching, utvärderingsgrindar, röktester). | Lista produktionsaspekter din demo fortfarande behöver: hosting, routning, kostnad, utvärdering. |
| [17 - Skapa lokala AI-agenter](./17-creating-local-ai-agents/README.md) | Hur man bygger lokal-först agenter som körs helt på din maskin med Foundry Local och Qwen (lokala verktyg, lokal RAG, lokal MCP). | Bestäm vilka delar av din demo som ska vara privata och köras lokalt. |
| [18 - Säkerställa AI-agenter](./18-securing-ai-agents/README.md) | Hur man gör agenthandlingar mer granskbara och manipuleringssäkra. | Bestäm vilka handlingar i din demo som ska loggas eller kvitteras. |

## Validera distribuerade agenter med röktester

När du distribuerar en agent (Lektion 16) är ett **röktest** den billigaste första
kontrollen för att se att distributionen faktiskt svarar. Detta repo levereras med färdiga
kataloger under [tests/](./tests/README.md) för de distribuerbara agenterna i Lektionerna
01, 04, 05 och 16, kopplade till
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action. Kör dem från fliken **Actions** efter att ha distribuerat agenten från lektionen.
Röktester är en första grind — offline och online utvärdering (Lektion 10 och 16)
berättar hur *bra* agenten är.

## Nyckelidéer på nybörjarvänligt språk

### Verktyg

Ett verktyg är något agenten kan anropa för att göra arbete utanför modellen. Ett bra verktyg
har ett tydligt namn, en smal uppgift, typade indata, förutsägbar output och ett säkert sätt
att misslyckas.

För kursassistent-demo kan ett verktyg vara:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG och kunskap

RAG hjälper agenten att svara från källmaterial istället för att gissa. I denna
kurs kan detta källmaterial vara lektions-README-filer, kodexempel eller externa
resurser länkade från lektionerna.

Använd RAG när svaret bör förankras i dokument, data eller aktuella
projektfiler.

### Planering

Planering är användbart när förfrågan har mer än ett steg. Håll planerna korta och
synliga nog för att en utvecklare eller användare ska kunna granska dem.

För demo kan en plan vara:

1. Hitta lektioner relaterade till verktygsanvändning.
2. Sammanfatta de mest relevanta lektionerna.
3. Rekommendera en övningsuppgift.

### Kontext

Kontext är vad modellen ser just nu. För lite kontext kan göra att agenten
missar viktiga detaljer. För mycket kontext kan göra agenten långsammare, dyrare,
eller lättare att förvirras.

Bra kontextengineering innebär att välja rätt information för nästa modellanrop.




endast när det är användbart, säkert och lätt att uppdatera eller radera.


Till exempel kan det vara användbart att komma ihåg "eleven föredrar Python-exempel".
Att minnas känslig personlig data är oftast inte bra.

### Utvärdering och observerbarhet

Utvärdering frågar: gjorde agenten rätt sak?

Observerbarhet frågar: kan vi se hur det hände?

För produktionsagenter, spåra modellanrop, verktygsanrop, hämtad kontext,
latens, kostnad, fel och användarfeedback.

### Tillit och säkerhet

Pålitliga agenter behöver mer än en hjälpsam prompt. Använd verktyg med lägsta privilegier,
mänskligt godkännande för åtgärder med stor påverkan, dataredigering där det behövs, samt loggar eller
kvitton för åtgärder som måste granskas.

## En 15-minuters genomgångsrutin

Använd denna rutin efter varje lektion:

1. **Sammanfatta lektionen med en mening.**
2. **Namnge den nya agentförmågan.** Till exempel: verktygsanvändning, återvinning,
   planering, minne, observerbarhet eller säkerhet.
3. **Lägg till den i kursassistent-demo.** Vad ändras i demot nu?
4. **Hitta risken.** Vad kan gå fel om denna förmåga missbrukas?
5. **Skriv en testfråga.** Hur skulle du kontrollera att agenten beter sig väl?

## Snabb självkontroll

Innan du går vidare, försök besvara dessa frågor:

1. Vad kan en agent göra som en vanlig chatbot inte kan göra själv?
2. Vilket verktyg skulle din agent behöva först, och varför?
3. Vilken kunskapskälla bör förankra agentens svar?
4. Vilken kontext bör inkluderas i nästa modellanrop?
5. Vad bör agenten minnas och vad bör den undvika att lagra?
6. När ska agenten fråga om mänskligt godkännande?
7. Vilka loggar, spår eller kvitton skulle hjälpa dig att felsöka eller granska agenten senare?


## Föreslagen Avslutningsövning

I slutet av kursen, bygg en liten agent som hjälper en lärande att navigera detta
arkiv.

Minimumversion:

- Ta emot ett ämne från användaren.
- Hitta de mest relevanta lektionerna.
- Sammanfatta vad man ska läsa först.
- Föreslå en praktisk övningsuppgift.
- Visa vilka lektionsfiler eller länkar som användes.

Utökad version:

- Kom ihåg den lärandes föredragna programmeringsspråk.
- Använd en enkel plan innan svaret ges.
- Lägg till ett självkontrollsteg innan slutligt svar.
- Logga verktygsanrop och hämtade källor.
- Be om bekräftelse innan webbläsare eller UI-automatiseringsuppgifter öppnas.

Detta ger dig ett litet men realistiskt sätt att öva verktyg, RAG, planering,
kontext, minne, observerbarhet och förtroende i ett projekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->