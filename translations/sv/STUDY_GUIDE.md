# AI-agenter för nybörjare - Studieguide

Använd denna guide som en praktisk följeslagare medan du går igenom kursen. Den är
inte avsedd att ersätta lektionerna. Den hjälper dig att avgöra var du ska börja, vad du ska
leta efter i varje lektion och hur du kopplar samman idéerna till en liten fungerande agent-
demo.

Om det är första gången du är här, börja enkelt:

1. Läs [Kursinställning](./00-course-setup/README.md).
2. Genomför lektionerna 01-06 i ordning.
3. Ha en liten demoidé i åtanke medan du lär dig.
4. Efter varje lektion, fråga: "Vad kan min agent göra nu som den inte kunde göra
   tidigare?"

## En enkel demo att ha i åtanke

Ett bra sätt att lära sig agenter är att följa en demoidé genom kursen.

Exempeldemo: **en kursassistentagent**.

Användaren frågar:

> "Jag vill lära mig hur agenter använder verktyg. Hitta rätt lektioner, sammanfatta vad
> jag bör läsa först och ge mig en kort övningsuppgift."

En vanlig chattbot kan svara utifrån vad den redan vet. En agent kan göra mer:

1. **Läsa eller söka i kursfiler** för att hitta rätt lektioner.
2. **Använda verktyg** för att hämta lektionlänkar, exempel eller stödmaterial.
3. **Planera** en kort lärväg istället för att ge ett långt svar.
4. **Använda kontext** från den aktuella konversationen för att fokusera på lärarens
   mål.
5. **Komma ihåg användbara preferenser** om applikationen stödjer minne.
6. **Visa spår, citat eller loggar** så att användaren kan förstå vad som hände.
7. **Tillämpa skyddsåtgärder** innan riskabla handlingar utförs eller känsliga data används.

När du studerar varje lektion, återkom till denna demo och fråga: vilken ny
förmåga skulle denna lektion tillföra?

## Vad du bygger mot

I slutet av kursen ska du kunna förklara och bygga agentsystem som kombinerar dessa delar:

| Del | Betydelse på vardagsspråk | I demon |
|------|--------------------------|---------|
| Modell | Resoneringsmotorn som tolkar användarens begäran | Förstår att läraren vill ha lektioner om verktygsanvändning |
| Verktyg | Funktioner, API:er, filer, webbläsare eller tjänster agenten kan använda | Söker i repo eller hämtar lektionsinnehåll |
| Kunskap | Dokument eller data som grundar svaret | Kursens README-filer och lektionsmaterial |
| Kontext | Information som skickas med nästa modellanrop | Användarens mål och verktygets resultat |
| Minne | Sparad information för senare användning | Läraren föredrar praktiska Python-exempel |
| Planering | Att bryta ner ett större mål i mindre steg | Hitta lektioner, sammanfatta dem, föreslå övning |
| Orkestrering | Styra arbete mellan verktyg, steg eller agenter | En planerare anropar en sökfunktion, sedan en sammanfattare |
| Förtroende | Säkerhet, trygghet, utvärdering och observabilitet | Loggar verktygsanrop och frågar innan åtgärder med stor påverkan |

## Modeller och leverantörer

Kodexemplen i kursen använder **Microsoft Agent Framework (MAF)** och riktar sig mot **Azure OpenAI Responses API** — det rekommenderade API:t framöver, som kombinerar chattkomplettering, verktygsanrop, multimodala indata och tillståndsbaserade konversationer i en och samma API-yta. Du kopplar antingen via ett **Microsoft Foundry**-projekt (med `FoundryChatClient`) eller direkt till Azure OpenAI (med `OpenAIChatClient`).

När du arbetar dig genom lektionerna har du några leverantörsalternativ:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — huvudsaklig väg som används genom lektionerna. Logga in med `az login` för nyckellös Entra ID-autentisering.
- **Foundry Local** — kör modeller helt lokalt via en OpenAI-kompatibel API (ingen moln, inga API-nycklar). Perfekt för offline- eller kostnadsfri experimentering. Se [Kursinställning](./00-course-setup/README.md).
- **MiniMax** — en OpenAI-kompatibel leverantör med modeller för stora kontexter, användbar som drop-in-alternativ.

> **Observera:** GitHub Models är föråldrat (utgår juli 2026) och stöder inte Responses API. Exemplen har uppdaterats för att använda Azure OpenAI / Microsoft Foundry istället.

## Välj din lärväg

Du kan ta hela kursen i ordning eller hoppa till en väg baserat på vad du vill
bygga.

| Om ditt mål är att... | Börja med | Studera sedan |
|----------------------|-----------|---------------|
| Förstå vad agenter är | 01, 02, 03 | 04, 05, 06 |
| Bygga en agent som använder verktyg | 04 | 05, 07, 14 |
| Bygga en RAG-baserad agent | 05 | 04, 06, 12 |
| Designa flerstegsarbetsflöden | 07 | 08, 09, 14 |
| Förstå multi-agent system | 08 | 07, 09, 11 |
| Förbereda agenter för produktion | 06, 10 | 12, 13, 18 |
| Utforska protokoll och webbläsarautomatisering | 11, 15 | 10, 18 |

Tips: om du är ny inom agenter, hoppa inte över lektionerna 01-06. De ger dig det
ordförråd du behöver för resten av kursen.

## Lektion för lektion-guide

| Lektion | Vad du lär dig | Prova detta efter lektionen |
|---------|----------------|-----------------------------|
| [01 - Intro till AI-agenter](./01-intro-to-ai-agents/README.md) | Vad som skiljer en agent från en vanlig chattbot. | Förklara din demoidé som en agent, inte bara som en chattapp. |
| [02 - Agentiska ramverk](./02-explore-agentic-frameworks/README.md) | Hur ramverk hjälper med modeller, verktyg, tillstånd och arbetsflöden. | Identifiera vilka delar av din demo ett ramverk skulle hantera. |
| [03 - Agentiska designmönster](./03-agentic-design-patterns/README.md) | Vanliga mönster för att designa agentbeteende. | Skissa användarresan innan du skriver kod. |
| [04 - Verktygsanvändning](./04-tool-use/README.md) | Hur agenter anropar verktyg för att hämta data eller utföra åtgärder. | Definiera ett verktyg som din demoagent skulle behöva. |
| [05 - Agentisk RAG](./05-agentic-rag/README.md) | Hur återvinning förankrar agentens svar i dokument eller data. | Bestäm vilken kunskapskälla din demo ska söka i. |
| [06 - Pålitliga agenter](./06-building-trustworthy-agents/README.md) | Hur man lägger till skydd, övervakning och säkrare beteende. | Lägg till en regel för när agenten bör fråga användaren först. |
| [07 - Planeringsdesign](./07-planning-design/README.md) | Hur agenter bryter ner större mål i mindre steg. | Skriv en trestegsplan för din demoförfrågan. |
| [08 - Multi-agent design](./08-multi-agent/README.md) | När man ska dela upp arbete mellan specialiserade agenter. | Bestäm om din demo behöver en eller flera agenter. |
| [09 - Metakognition](./09-metacognition/README.md) | Hur agenter kan granska och förbättra sin egen output. | Lägg till en slutlig självkontroll innan agenten svarar. |
| [10 - AI-agenter i produktion](./10-ai-agents-production/README.md) | Vad som förändras när en agent går från demo till produktion. | Lista vad du skulle övervaka: kvalitet, kostnad, svarstid, fel. |
| [11 - Agentiska protokoll](./11-agentic-protocols/README.md) | Hur protokoll kopplar agenter till verktyg och andra agenter. | Identifiera var ett standardprotokoll kan förenkla integration. |
| [12 - Kontextteknik](./12-context-engineering/README.md) | Hur man väljer, trimmar, isolerar och hanterar kontext. | Bestäm vad som ska ingå i prompten och vad som ska exkluderas. |
| [13 - Agentminne](./13-agent-memory/README.md) | Hur agenter kan spara användbar information över interaktioner. | Välj en säker preferens som din demo kan komma ihåg. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Ramverksspecifika byggstenar för agenter och arbetsflöden, plus värdskap för LangChain/LangGraph-agenter i Microsoft Foundry. | Karta dina demosteg till ramverkskoncept. |
| [15 - Datoranvändningsagenter](./15-browser-use/README.md) | Hur agenter kan interagera med webbläsare eller UI-yta, inklusive verkliga exempel som Microsoft Project Opal. | Välj en webbläsaruppgift som fortfarande ska kräva användarbekräftelse. |
| [18 - Säkerställ AI-agenter](./18-securing-ai-agents/README.md) | Hur man gör agenters handlingar mer granskningsbara och manipulationssäkra. | Bestäm vilka åtgärder i din demo som bör loggas eller få kvittens. |

Lektioner 16 och 17 listas i huvudsakliga README som kommer snart. Lägg till dem i din
studieplan när lektionsmaterial är tillgängligt.

## Nyckelidéer på nybörjarvänligt språk

### Verktyg

Ett verktyg är något agenten kan anropa för att utföra arbete utanför modellen. Ett bra verktyg
har ett tydligt namn, ett snävt uppdrag, typade indata, förutsägbar output och ett säkert sätt att
misslyckas på.

För kursassistent-demon kan ett verktyg vara:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG och kunskap

RAG hjälper agenten att svara från källmaterial istället för att gissa. I denna
kurs kan källmaterialet vara lektionsREADME-filer, kodexempel eller externa
resurser länkade från lektionerna.

Använd RAG när svaret ska förankras i dokument, data eller aktuella
projektfiler.

### Planering

Planering är användbart när begäran har mer än ett steg. Håll planer korta och
tillräckligt tydliga för att en utvecklare eller användare ska kunna granska dem.

För demon kan en plan vara:

1. Hitta lektioner relaterade till verktygsanvändning.
2. Sammanfatta de mest relevanta lektionerna.
3. Rekommendera en övningsuppgift.

### Kontext

Kontext är vad modellen ser just nu. För lite kontext kan få agenten
att missa viktiga detaljer. För mycket kontext kan göra agenten långsammare, dyrare
eller lättare att förvirra.

Bra kontextteknik betyder att välja rätt information för nästa modellanrop.

### Minne

Minne är information som sparas för senare bruk. Spara inte allt. Spara bara information
när den är användbar, säker och lätt att uppdatera eller radera.

Till exempel kan det vara användbart att komma ihåg "läraren föredrar Python-exempel."
Att komma ihåg känsliga persondata är vanligtvis inte bra.

### Utvärdering och observabilitet

Utvärdering frågar: gjorde agenten rätt sak?

Observabilitet frågar: kan vi se hur det gick till?

För produktionsagenter, håll koll på modellanrop, verktygsanrop, hämtad kontext,
svarstid, kostnad, fel och användarfeedback.

### Förtroende och säkerhet

Pålitliga agenter behöver mer än bara en hjälpsam prompt. Använd verktyg med minsta möjliga åtkomst,
mänskligt godkännande för åtgärder med stor påverkan, dataredigering där det behövs och loggar eller
kvittenser för åtgärder som måste granskas.

## En 15-minuters repetitionsrutin

Använd denna rutin efter varje lektion:

1. **Sammanfatta lektionen i en mening.**
2. **Nämn den nya agentförmågan.** Till exempel: verktygsanvändning, hämtning,
   planering, minne, observabilitet eller säkerhet.
3. **Lägg till det i kursassistentdemon.** Vad ändras i demon nu?
4. **Hitta risken.** Vad kan gå fel om denna förmåga missbrukas?
5. **Skriv en testfråga.** Hur skulle du kontrollera att agenten beter sig väl?

## Snabb självkontroll

Innan du går vidare, försök svara på dessa frågor:

1. Vad kan en agent göra som en vanlig chattbot inte kan göra på egen hand?
2. Vilket verktyg skulle din agent behöva först, och varför?
3. Vilken kunskapskälla ska förankra agentens svar?
4. Vilken kontext bör ingå i nästa modellanrop?
5. Vad bör agenten komma ihåg, och vad bör undvikas att spara?
6. När bör agenten be om mänskligt godkännande?
7. Vilka loggar, spår eller kvittenser skulle hjälpa dig att felsöka eller granska agenten senare?

## Föreslagen kapstone-övning

I slutet av kursen, bygg en liten agent som hjälper en lärande att navigera i detta
repo.

Minimiversion:

- Acceptera ett ämne från användaren.
- Hitta de mest relevanta lektionerna.
- Sammanfatta vad som ska läsas först.
- Föreslå en praktisk övningsuppgift.
- Visa vilka lektionsfiler eller länkar som användes.

Utökad version:

- Kom ihåg den lärandes föredragna programspråk.
- Använd en enkel plan innan svar.
- Lägg till ett självkontrollsteg innan slutgiltigt svar.
- Logga verktygsanrop och hämtade källor.
- Be om bekräftelse innan webbläsar- eller UI-automatiseringsuppgifter startas.

Det ger dig ett litet men realistiskt sätt att öva verktyg, RAG, planering,
kontext, minne, observabilitet och förtroende i ett och samma projekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->