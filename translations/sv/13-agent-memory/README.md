# Minne för AI-agenter
[![Agentminne](../../../translated_images/sv/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

När man diskuterar de unika fördelarna med att skapa AI-agenter diskuteras främst två saker: förmågan att anropa verktyg för att utföra uppgifter och förmågan att förbättras över tid. Minne är grunden för att skapa självförbättrande agenter som kan skapa bättre upplevelser för våra användare.

I denna lektion kommer vi att titta på vad minne är för AI-agenter och hur vi kan hantera det och använda det till fördel för våra applikationer.

## Introduktion

Denna lektion kommer att täcka:

• **Förstå AI-agentminne**: Vad minne är och varför det är viktigt för agenter.

• **Implementering och lagring av minne**: Praktiska metoder för att lägga till minneskapacitet till dina AI-agenter, med fokus på korttids- och långtidsminne.

• **Göra AI-agenter självförbättrande**: Hur minne gör det möjligt för agenter att lära sig från tidigare interaktioner och förbättras över tid.

## Tillgängliga implementationer

Denna lektion inkluderar två omfattande notebook-tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerar minne med Mem0 och Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerar strukturerat minne med Cognee, som automatiskt bygger kunskapsgraf baserad på embeddings, visualiserar grafen och smart hämtning

## Lärandemål

Efter att ha avslutat denna lektion kommer du att kunna:

• **Skilja mellan olika typer av AI-agentminne**, inklusive arbetsminne, korttidsminne och långtidsminne samt specialiserade former som persona- och episodiskt minne.

• **Implementera och hantera korttids- och långtidsminne för AI-agenter** med Microsoft Agent Framework, utnyttja verktyg som Mem0, Cognee, Whiteboard-minne och integrera med Azure AI Search.

• **Förstå principerna bakom självförbättrande AI-agenter** och hur robusta minneshanteringssystem bidrar till kontinuerligt lärande och anpassning.

## Förstå AI-agentminne

I grunden avser **minne för AI-agenter de mekanismer som tillåter dem att behålla och återkalla information**. Denna information kan vara specifika detaljer om en konversation, användarpreferenser, tidigare handlingar eller till och med inlärda mönster.

Utan minne är AI-applikationer ofta tillståndslösa, vilket betyder att varje interaktion börjar från början. Detta leder till en repetitiv och frustrerande användarupplevelse där agenten "glömmer" tidigare kontext eller preferenser.

### Varför är minne viktigt?

En agents intelligens är djupt kopplad till dess förmåga att återkalla och använda tidigare information. Minne gör att agenter kan vara:

• **Reflekterande**: Lära sig av tidigare handlingar och resultat.

• **Interaktiva**: Bibehålla kontext under en pågående konversation.

• **Proaktiva och reaktiva**: Förutse behov eller reagera lämpligt baserat på historiska data.

• **Autonoma**: Arbeta mer självständigt genom att använda lagrad kunskap.

Målet med att implementera minne är att göra agenter mer **påliteliga och kapabla**.

### Minnestyper

#### Arbetsminne

Tänk på detta som ett kladdpapper som en agent använder under en enskild pågående uppgift eller tankeprocess. Det håller omedelbar information som behövs för att beräkna nästa steg.

För AI-agenter fångar arbetsminnet ofta den mest relevanta informationen från en konversation, även om hela chathistoriken är lång eller trunkerad. Det fokuserar på att extrahera nyckelelement som krav, förslag, beslut och åtgärder.

**Exempel på arbetsminne**

I en resebokningsagent kan arbetsminnet fånga användarens aktuella begäran, som "Jag vill boka en resa till Paris". Detta specifika krav hålls i agentens omedelbara kontext för att vägleda den pågående interaktionen.

#### Korttidsminne

Denna typ av minne behåller information under hela en konversation eller session. Det är kontexten för den aktuella chatten, vilket tillåter agenten att hänvisa tillbaka till tidigare turer i dialogen.

I [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK-exemplen motsvarar detta `AgentSession`, skapad med `agent.create_session()`. Sessionen är ramverkets inbyggda korttidsminne: det håller kontexten från konversationen tillgänglig medan samma session återanvänds, men kontexten sparas inte när sessionen slutar eller applikationen startas om. Använd långtidsminne för fakta och preferenser som behöver överleva över sessioner, vanligtvis via en databas, vektorindex eller annan permanent lagring.

**Exempel på korttidsminne**

Om en användare frågar, "Hur mycket skulle en flygning till Paris kosta?" och sedan följer upp med "Hur är det med boende där?", säkerställer korttidsminne att agenten vet att "där" refererar till "Paris" inom samma konversation.

#### Långtidsminne

Detta är information som kvarstår över flera konversationer eller sessioner. Det tillåter agenter att minnas användarpreferenser, historiska interaktioner eller allmän kunskap över längre perioder. Detta är viktigt för personalisering.

**Exempel på långtidsminne**

Ett långtidsminne kan spara att "Ben tycker om skidåkning och utomhusaktiviteter, gillar kaffe med utsikt över bergen och vill undvika avancerade skidbackar på grund av en tidigare skada". Denna information, inlärd från tidigare interaktioner, påverkar rekommendationer i framtida reseplaneringssessioner och gör dem mycket personliga.

#### Personaminne

Denna specialiserade minnestyp hjälper en agent att utveckla en konsekvent "personlighet" eller "persona". Den tillåter agenten att minnas detaljer om sig själv eller sin avsedda roll, vilket gör interaktionerna mer flytande och fokuserade.

**Exempel på personaminne**
Om reseagenten är utformad som en "expert på skidplanering" kan personaminnet förstärka denna roll och påverka dess svar att anpassas till en experts ton och kunskap.

#### Arbetsflödes-/episodiskt minne

Detta minne lagrar sekvensen steg som en agent tar under en komplex uppgift, inklusive framgångar och misslyckanden. Det är som att minnas specifika "avsnitt" eller tidigare erfarenheter för att lära av dem.

**Exempel på episodiskt minne**

Om agenten försökte boka en specifik flygning men misslyckades på grund av otillgänglighet, kan episodiskt minne registrera detta misslyckande, vilket tillåter agenten att försöka alternativa flyg eller informera användaren mer informerat vid ett senare försök.

#### Entitetsminne

Detta innebär att extrahera och minnas specifika entiteter (som personer, platser eller saker) och händelser från konversationer. Det tillåter agenten att bygga en strukturerad förståelse av viktiga element som diskuterats.

**Exempel på entitetsminne**

Från en konversation om en tidigare resa kan agenten extrahera "Paris," "Eiffeltornet," och "middag på Le Chat Noir restaurang" som entiteter. Vid en framtida interaktion kan agenten minnas "Le Chat Noir" och erbjuda att göra en ny reservation där.

#### Strukturerad RAG (Retrieval Augmented Generation)

Medan RAG är en bredare teknik, framhävs "Strukturerad RAG" som en kraftfull minnesteknologi. Den extraherar tät, strukturerad information från olika källor (konversationer, e-post, bilder) och använder den för att förbättra precision, återkallelse och hastighet i svar. Till skillnad från klassisk RAG som endast förlitar sig på semantisk likhet, arbetar Strukturerad RAG med den inneboende strukturen i informationen.

**Exempel på strukturerad RAG**

Istället för att bara matcha nyckelord kan Strukturerad RAG tolka flyguppgifter (destination, datum, tid, flygbolag) från ett mejl och lagra dem på ett strukturerat sätt. Detta tillåter exakta frågor som "Vilket flyg bokade jag till Paris på tisdag?"

## Implementering och lagring av minne

Att implementera minne för AI-agenter innebär en systematisk process av **minneshantering**, som inkluderar generering, lagring, hämtning, integrering, uppdatering och även "att glömma" (eller ta bort) information. Hämtning är en särskilt viktig aspekt.

### Specialiserade minnesverktyg

#### Mem0

Ett sätt att lagra och hantera agentminne är att använda specialiserade verktyg som Mem0. Mem0 fungerar som ett beständigt minneslager, vilket tillåter agenter att återkalla relevanta interaktioner, lagra användarpreferenser och faktuell kontext samt lära sig från framgångar och misslyckanden över tid. Idén är att statslösa agenter blir tillståndsbaserade.

Det fungerar genom en **tvåfasig minnespipeline: extraktion och uppdatering**. Först skickas meddelanden som läggs till i en agents tråd till Mem0-tjänsten, som använder en stor språkmodell (LLM) för att sammanfatta konversationshistorik och extrahera nya minnen. Därefter avgör en LLM-driven uppdateringsfas om minnena ska läggas till, ändras eller tas bort, och lagrar dem i en hybrid databas som kan inkludera vektor-, graf- och nyckel-värde-databaser. Systemet stöder även olika minnestyper och kan inkludera grafminne för att hantera relationer mellan entiteter.

#### Cognee

En annan kraftfull metod är att använda **Cognee**, ett open source semantiskt minne för AI-agenter som omvandlar strukturerad och ostrukturerad data till frågebara kunskapsgrafer understödda av embeddings. Cognee tillhandahåller en **dubbel lagringsarkitektur** som kombinerar vektorlikhetssökning med grafrelationer, vilket gör att agenter kan förstå inte bara vad information är lik, utan hur begrepp relaterar till varandra.

Det utmärker sig i **hybrid hämtning** som blandar vektorlikhet, grafstruktur och LLM-resonemang - från rå sökning i delar till grafmedveten frågeställning. Systemet upprätthåller ett **levande minne** som utvecklas och växer samtidigt som det förblir frågebart som en sammanlänkad graf, och stöder både korttids kontext för sessioner och långtidsbeständigt minne.

Cognee notebook-tutorialen ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) visar byggandet av detta enade minneslager, med praktiska exempel på hur man matar in data från olika källor, visualiserar kunskapsgrafen och frågar med olika sökstrategier anpassade till specifika agentbehov.

### Lagra minne med RAG

Utöver specialiserade minnesverktyg som Mem0 kan du utnyttja robusta söktjänster som **Azure AI Search som backend för lagring och hämtning av minnen**, särskilt för strukturerad RAG.

Detta låter dig grunda agentens svar med dina egna data, vilket säkerställer mer relevanta och korrekta svar. Azure AI Search kan användas för att lagra användarspecifika resminnen, produktkataloger eller annan domänspecifik kunskap.

Azure AI Search stöder kapaciteter som **Strukturerad RAG**, som utmärker sig i att extrahera och hämta tät, strukturerad information från stora datamängder som konversationshistorik, e-post eller till och med bilder. Detta ger "supermänsklig precision och återkallelse" jämfört med traditionella textdelnings- och embeddingsmetoder.

## Göra AI-agenter självförbättrande

Ett vanligt mönster för självförbättrande agenter innebär att införa en **"kunskapsagent"**. Denna separata agent observerar huvudkonversationen mellan användaren och den primära agenten. Dess roll är att:

1. **Identifiera värdefull information**: Avgöra om någon del av konversationen är värd att spara som generell kunskap eller specifik användarpreferens.

2. **Extrahera och sammanfatta**: Destillera den väsentliga lärdomen eller preferensen från konversationen.

3. **Lagra i en kunskapsbas**: Spara denna extraherade information, ofta i en vektordatabas, så att den kan hämtas senare.

4. **Utöka framtida frågor**: När användaren initierar en ny fråga hämtar kunskapsagenten relevant lagrad information och bifogar den till användarens prompt, vilket ger kritisk kontext till huvudagenten (liknande RAG).

### Optimeringar för minne

• **Latenshantering**: För att undvika att sakta ner användarinteraktioner kan en billigare, snabbare modell användas initialt för att snabbt kontrollera om information är värd att lagra eller hämta, och endast anropa den mer komplexa extraktions-/hämtprocessen vid behov.

• **Underhåll av kunskapsbasen**: För en växande kunskapsbas kan mindre ofta använd information flyttas till "kall förvaring" för att hantera kostnader.

## Har du fler frågor om agentminne?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att möta andra lärande, delta i kontorstider och få dina frågor om AI-agenter besvarade.
## Föregående lektion

[Context Engineering for AI Agents](../12-context-engineering/README.md)

## Nästa lektion

[Utforska Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->