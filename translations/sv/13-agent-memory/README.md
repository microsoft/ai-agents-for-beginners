# Minne för AI-agenter 
[![Agent Memory](../../../translated_images/sv/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

När man diskuterar de unika fördelarna med att skapa AI-agenter diskuteras huvudsakligen två saker: möjligheten att anropa verktyg för att slutföra uppgifter och förmågan att förbättras över tid. Minne ligger i grunden för att skapa en självförbättrande agent som kan skapa bättre upplevelser för våra användare.

I denna lektion kommer vi att titta på vad minne är för AI-agenter och hur vi kan hantera det och använda det till fördel för våra applikationer.

## Introduktion

Denna lektion kommer att täcka:

• **Förståelse av AI-agenters minne**: Vad minne är och varför det är avgörande för agenter.

• **Implementera och lagra minne**: Praktiska metoder för att lägga till minneskapaciteter i dina AI-agenter, med fokus på korttids- och långtidsminne.

• **Göra AI-agenter självförbättrande**: Hur minne gör det möjligt för agenter att lära av tidigare interaktioner och förbättras över tid.

## Tillgängliga implementationer

Denna lektion inkluderar två omfattande anteckningsbokshandledningar:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerar minne med Mem0 och Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerar strukturerat minne med Cognee, bygger automatiskt en kunskapsgraf stödd av embeddings, visualiserar grafen och intelligent hämtning

## Lärandemål

Efter att ha slutfört denna lektion kommer du att veta hur du:

• **Skilja mellan olika typer av AI-agentminne**, inklusive arbetsminne, korttids- och långtidsminne, samt specialiserade former som persona- och episodiskt minne.

• **Implementera och hantera korttids- och långtidsminne för AI-agenter** med Microsoft Agent Framework, utnyttja verktyg som Mem0, Cognee, Whiteboard memory och integrera med Azure AI Search.

• **Förstå principerna bakom självförbättrande AI-agenter** och hur robusta minneshanteringssystem bidrar till kontinuerligt lärande och anpassning.

## Förstå AI-agenters minne

I grunden hänvisar **minne för AI-agenter till de mekanismer som gör det möjligt för dem att behålla och återkalla information**. Denna information kan vara specifika detaljer om en konversation, användarpreferenser, tidigare handlingar eller till och med inlärda mönster.

Utan minne är AI-applikationer ofta stateless, vilket innebär att varje interaktion börjar från början. Detta leder till en upprepad och frustrerande användarupplevelse där agenten "glömmer" tidigare kontext eller preferenser.

### Varför är minne viktigt?

En agents intelligens är djupt kopplad till dess förmåga att minnas och använda tidigare information. Minne gör att agenter kan vara:

• **Reflekterande**: Lära av tidigare handlingar och resultat.

• **Interaktiva**: Behålla kontext i en pågående konversation.

• **Proaktiva och reaktiva**: Förutse behov eller svara lämpligt baserat på historisk data.

• **Autonoma**: Fungere mer självständigt genom att dra nytta av lagrad kunskap.

Målet med att implementera minne är att göra agenter mer **pålitliga och kapabla**.

### Typer av minne

#### Arbetsminne

Tänk på detta som en skisslapp en agent använder under en enda, pågående uppgift eller tankeprocess. Det håller omedelbar information som behövs för att beräkna nästa steg.

För AI-agenter fångar arbetsminnet ofta den mest relevanta informationen från en konversation, även om hela chattloggen är lång eller trunkerad. Det fokuserar på att extrahera nyckelelement som krav, förslag, beslut och åtgärder.

**Exempel på arbetsminne**

I en resebokningsagent kan arbetsminnet fånga användarens aktuella begäran, som "Jag vill boka en resa till Paris". Detta specifika krav hålls i agentens omedelbara kontext för att styra den aktuella interaktionen.

#### Korttidsminne

Denna typ av minne behåller information under en enskild konversation eller session. Det är kontexten för den nuvarande chatten, vilket gör att agenten kan hänvisa tillbaka till tidigare turer i dialogen.

**Exempel på korttidsminne**

Om en användare frågar, "Hur mycket skulle ett flyg till Paris kosta?" och sedan följer upp med "Vad sägs om boende där?", säkerställer korttidsminnet att agenten vet att "där" avser "Paris" inom samma konversation.

#### Långtidsminne

Detta är information som kvarstår över flera konversationer eller sessioner. Det möjliggör att agenter kommer ihåg användarpreferenser, historiska interaktioner eller generell kunskap över längre perioder. Detta är viktigt för personalisering.

**Exempel på långtidsminne**

Ett långtidsminne kan lagra att "Ben gillar skidåkning och utomhusaktiviteter, gillar kaffe med bergsutsikt, och vill undvika avancerade skidbackar på grund av en tidigare skada". Denna information, inlärd från tidigare interaktioner, påverkar rekommendationer i framtida reseplaneringssessioner och gör dem mycket personliga.

#### Personaminne

Denna specialiserade minnestyp hjälper en agent att utveckla en konsekvent "personlighet" eller "persona". Det gör att agenten kan komma ihåg detaljer om sig själv eller sin avsedda roll, vilket gör interaktionerna mer flytande och fokuserade.

**Exempel på personaminne**
Om reseagenten är utformad för att vara en "expert på skidplanering" kan personaminnet förstärka denna roll och påverka dess svar så att de stämmer överens med en experts ton och kunskap.

#### Arbetsflödes-/episodiskt minne

Detta minne lagrar sekvensen av steg en agent tar under en komplex uppgift, inklusive framgångar och misslyckanden. Det är som att minnas specifika "episoder" eller tidigare erfarenheter för att lära av dem.

**Exempel på episodiskt minne**

Om agenten försökte boka ett specifikt flyg men misslyckades på grund av otillgänglighet, kan episodiskt minne registrera detta misslyckande och låta agenten försöka alternativa flyg eller informera användaren om problemet på ett mer informerat sätt vid ett senare försök.

#### Entitetsminne

Detta innebär att extrahera och komma ihåg specifika entiteter (som personer, platser eller saker) och händelser från konversationer. Det gör att agenten kan bygga en strukturerad förståelse av viktiga element som diskuterats.

**Exempel på entitetsminne**

Från en konversation om en tidigare resa kan agenten extrahera "Paris", "Eiffeltornet" och "middag på Le Chat Noir restaurang" som entiteter. Vid en framtida interaktion kan agenten komma ihåg "Le Chat Noir" och erbjuda sig att boka ett nytt bord där.

#### Strukturerad RAG (Retrieval Augmented Generation)

Medan RAG är en bredare teknik, framhävs "Strukturerad RAG" som en kraftfull minnesteknik. Den extraherar tät, strukturerad information från olika källor (konversationer, e-post, bilder) och använder den för att förbättra precision, recall och hastighet i svar. Till skillnad från klassisk RAG som enbart förlitar sig på semantisk likhet, arbetar Strukturerad RAG med informationens inneboende struktur.

**Exempel på Strukturerad RAG**

Istället för att bara matcha nyckelord kan Strukturerad RAG analysera flygdetails (destination, datum, tid, flygbolag) från ett e-postmeddelande och lagra dem på ett strukturerat sätt. Detta möjliggör precisa frågor som "Vilket flyg bokade jag till Paris på tisdag?"

## Implementera och lagra minne

Att implementera minne för AI-agenter innebär en systematisk process för **minneshantering**, som inkluderar att generera, lagra, hämta, integrera, uppdatera och till och med "glömma" (eller radera) information. Hämtning är ett särskilt avgörande aspekt.

### Specialiserade minnesverktyg

#### Mem0

Ett sätt att lagra och hantera agentminne är att använda specialiserade verktyg som Mem0. Mem0 fungerar som ett persistents minneslager och tillåter agenter att återkalla relevanta interaktioner, lagra användarpreferenser och faktuell kontext samt lära av framgångar och misslyckanden över tid. Idén här är att stateless-agenter blir stateful.

Det fungerar genom en **tvåstegs minnespipeline: extraktion och uppdatering**. Först skickas meddelanden som läggs till i en agents tråd till Mem0-tjänsten, som använder en Large Language Model (LLM) för att sammanfatta konversationshistorik och extrahera nya minnen. Därefter avgör en LLM-driven uppdateringsfas om man ska lägga till, modifiera eller ta bort dessa minnen, och lagrar dem i en hybrid datalagring som kan inkludera vektor-, graf- och nyckel-/värde-databaser. Detta system stöder också olika minnestyper och kan integrera grafminne för att hantera relationer mellan entiteter.

#### Cognee

Ett annat kraftfullt tillvägagångssätt är att använda **Cognee**, ett öppen källkod semantic memory för AI-agenter som transformerar strukturerad och ostrukturerad data till sökbara kunskapsgrafer stödda av embeddings. Cognee erbjuder en **dual-store architecture** som kombinerar vektorsökningslikhet med grafrelationer, vilket gör att agenter kan förstå inte bara vilken information som är lik, utan hur koncept relaterar till varandra.

Det utmärker sig i **hybrid retrieval** som blandar vektorsimilaritet, grafstruktur och LLM-resonemang - från råa chunk-uppslag till grafmedveten fråge-svar. Systemet upprätthåller ett **levande minne** som utvecklas och växer samtidigt som det förblir sökbart som en sammanhängande graf, vilket stöder både korttids sessionskontext och långtids bestående minne.

Cognee-anteckningsboksexemplet ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) visar hur man bygger detta enhetliga minneslager, med praktiska exempel på hur man tar in olika datakällor, visualiserar kunskapsgrafen och frågar med olika sökstrategier anpassade till specifika agentbehov.

### Att lagra minne med RAG

Utöver specialiserade minnesverktyg som mem0 , kan du utnyttja robusta söktjänster som **Azure AI Search som en backend för att lagra och hämta minnen**, särskilt för strukturerad RAG.

Detta gör att du kan förankra agentens svar i din egen data, vilket säkerställer mer relevanta och korrekta svar. Azure AI Search kan användas för att lagra användarspecifika reseminnen, produktkataloger eller annan domänspecifik kunskap.

Azure AI Search stödjer funktioner som **Strukturerad RAG**, vilken excellerar i att extrahera och hämta tät, strukturerad information från stora dataset som konversationshistorik, e-post eller till och med bilder. Detta ger "övermänsklig precision och recall" jämfört med traditionella textchunktning och embedding-approacher.

## Få AI-agenter att självförbättra sig

Ett vanligt mönster för självförbättrande agenter involverar att introducera en **"kunskapsagent"**. Denna separata agent observerar huvudsamtalet mellan användaren och primäragenten. Dess roll är att:

1. **Identifiera värdefull information**: Avgöra om någon del av konversationen är värd att spara som allmän kunskap eller en specifik användarpreferens.

2. **Extrahera och sammanfatta**: Destillera det väsentliga lärandet eller preferensen från konversationen.

3. **Lagra i en kunskapsbas**: Spara denna extraherade information, ofta i en vektordatabas, så att den kan hämtas senare.

4. **Förstärka framtida förfrågningar**: När användaren initierar en ny förfrågan hämtar kunskapsagenten relevant lagrad information och bifogar den till användarens prompt, vilket ger viktig kontext till primäragenten (liknande RAG).

### Optimeringar för minne

• **Latenshantering**: För att undvika att sakta ner användarinteraktioner kan en billigare, snabbare modell användas initialt för att snabbt kontrollera om information är värd att lagra eller hämta, och endast anropa den mer komplexa extraktions-/hämtningsprocessen när det är nödvändigt.

• **Underhåll av kunskapsbasen**: För en växande kunskapsbas kan mindre frekvent använd information flyttas till "cold storage" för att hantera kostnader.

## Fler frågor om agentminne?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra elever, delta i office hours och få dina frågor om AI-agenter besvarade.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungliga språk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell, mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->