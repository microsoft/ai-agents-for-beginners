# Minne för AI-agenter  
[![Agent Memory](../../../translated_images/sv/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

När man diskuterar de unika fördelarna med att skapa AI-agenter är det främst två saker som tas upp: möjligheten att anropa verktyg för att slutföra uppgifter och möjligheten att förbättras över tid. Minne är grunden för att skapa självförbättrande agenter som kan skapa bättre upplevelser för våra användare.

I denna lektion kommer vi att titta på vad minne är för AI-agenter och hur vi kan hantera det och använda det till fördel för våra applikationer.

## Introduktion

Denna lektion kommer att täcka:

• **Förstå AI-agentminne**: Vad minne är och varför det är viktigt för agenter.

• **Implementera och lagra minne**: Praktiska metoder för att lägga till minnesförmågor till dina AI-agenter med fokus på korttids- och långtidsminne.

• **Göra AI-agenter självförbättrande**: Hur minne möjliggör för agenter att lära sig från tidigare interaktioner och förbättras med tiden.

## Tillgängliga implementationer

Denna lektion innehåller två omfattande notebook-tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementerar minne med Mem0 och Azure AI Search med Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementerar strukturerat minne med Cognee, bygger automatiskt en kunskapsgraf stödd av embeddings, visualiserar grafen och intelligent återvinning

## Inlärningsmål

Efter att ha slutfört denna lektion kommer du att veta hur man:

• **Skiljer mellan olika typer av AI-agentminne**, inklusive arbetsminne, korttidsminne och långtidsminne samt specialiserade former som persona- och episodiskt minne.

• **Implementerar och hanterar korttids- och långtidsminne för AI-agenter** med Microsoft Agent Framework, med verktyg som Mem0, Cognee, Whiteboard-minne och integration med Azure AI Search.

• **Förstår principerna bakom självförbättrande AI-agenter** och hur robusta minneshanteringssystem bidrar till kontinuerligt lärande och anpassning.

## Förstå AI-agentminne

I grunden syftar **minne för AI-agenter på de mekanismer som gör att de kan behålla och återkalla information**. Denna information kan vara specifika detaljer om en konversation, användarpreferenser, tidigare handlingar eller till och med inlärda mönster.

Utan minne är AI-applikationer ofta statslösa, vilket innebär att varje interaktion startar från grunden. Detta leder till en repetitiv och frustrerande användarupplevelse där agenten "glömmer" tidigare sammanhang eller preferenser.

### Varför är minne viktigt?

En agents intelligens är djupt kopplad till dess förmåga att återkalla och använda tidigare information. Minne gör det möjligt för agenter att vara:

• **Reflekterande**: Lära sig från tidigare handlingar och resultat.

• **Interaktiva**: Bibehålla sammanhang under en pågående konversation.

• **Proaktiva och Reaktiva**: Förutse behov eller reagera lämpligt baserat på historiska data.

• **Autonoma**: Fungerar mer självständigt genom att dra nytta av lagrad kunskap.

Målet med att implementera minne är att göra agenter mer **pålitliga och kapabla**.

### Minnestyper

#### Arbetsminne

Tänk på detta som en skissblockslapp som en agent använder under en enda pågående uppgift eller tankeprocess. Det innehåller omedelbar information som behövs för att räkna ut nästa steg.

För AI-agenter fångar arbetsminnet ofta den mest relevanta informationen från en konversation, även om hela chattloggen är lång eller trunkerad. Det fokuserar på att extrahera nyckelelement som krav, förslag, beslut och åtgärder.

**Exempel på Arbetsminne**

I en resebokningsagent kan arbetsminnet fånga användarens aktuella önskemål, till exempel "Jag vill boka en resa till Paris". Detta specifika krav hålls i agentens omedelbara kontext för att styra den aktuella interaktionen.

#### Korttidsminne

Denna typ av minne behåller information under en enskild konversation eller session. Det är kontexten för den aktuella chatten och tillåter agenten att referera tillbaka till tidigare dialogtur.

I [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK-exempel motsvarar detta `AgentSession`, skapat med `agent.create_session()`. Sessionen är ramverkets inbyggda korttidsminne: det håller konversationskontext tillgänglig så länge samma session återanvänds, men den kontexten sparas inte när sessionen avslutas eller applikationen startas om. Använd långtidsminne för fakta och preferenser som måste bevaras över sessioner, vanligtvis via en databas, vektorindex eller annan beständig lagring.

**Exempel på Korttidsminne**

Om en användare frågar, "Hur mycket kostar en flygning till Paris?" och sedan följer upp med "Hur är det med boende där?", säkerställer korttidsminnet att agenten förstår att "där" syftar på "Paris" inom samma konversation.

#### Långtidsminne

Detta är information som består över flera konversationer eller sessioner. Det gör att agenter kan minnas användarpreferenser, historiska interaktioner eller generell kunskap över längre perioder. Detta är viktigt för personalisering.

**Exempel på Långtidsminne**

Ett långtidsminne kan lagra att "Ben gillar skidåkning och utomhusaktiviteter, föredrar kaffe med utsikt över berg och vill undvika avancerade skidbackar på grund av en tidigare skada". Denna information, inlärd från tidigare interaktioner, påverkar rekommendationer i framtida reseplaneringssessioner, vilket gör dem mycket personliga.

#### Persona-minne

Denna specialiserade minnestyp hjälper en agent att utveckla en konsekvent "personlighet" eller "persona". Det tillåter agenten att komma ihåg detaljer om sig själv eller sin avsedda roll, vilket gör interaktionerna mer flytande och fokuserade.

**Exempel på Persona-minne**

Om reseagenten är designad för att vara en "expert på skidplanering" kan persona-minnet förstärka denna roll och påverka dess svar för att stämma överens med en experts ton och kunskap.

#### Workflow/Episodiskt minne

Detta minne lagrar ordningen av steg som en agent tar under en komplex uppgift, inklusive framgångar och misslyckanden. Det är som att minnas specifika "avsnitt" eller tidigare erfarenheter för att lära sig av dem.

**Exempel på Episodiskt minne**

Om agenten försökte boka en viss flygning men det misslyckades på grund av otillgänglighet, kan episodiskt minne registrera detta misslyckande. Detta tillåter agenten att försöka alternativa flyg eller informera användaren om problemet på ett mer insiktsfullt sätt vid ett senare försök.

#### Entitetsminne

Detta innebär att extrahera och komma ihåg specifika entiteter (som personer, platser eller saker) och händelser från konversationer. Det låter agenten bygga en strukturerad förståelse av nyckelelement som diskuterats.

**Exempel på Entitetsminne**

Från en konversation om en tidigare resa kan agenten extrahera "Paris," "Eiffeltornet" och "middag på Le Chat Noir restaurang" som entiteter. Vid en senare interaktion kan agenten minnas "Le Chat Noir" och erbjuda att boka ett nytt bord där.

#### Strukturerad RAG (Retrieval Augmented Generation)

Medan RAG är en bredare teknik, lyfts "Strukturerad RAG" fram som en kraftfull minnesteknologi. Den extraherar tät, strukturerad information från olika källor (konversationer, e-post, bilder) och använder den för att förbättra precision, recall och svarshastighet. Till skillnad från klassisk RAG som endast bygger på semantisk likhet, arbetar Strukturerad RAG med den inneboende strukturen i informationen.

**Exempel på Strukturerad RAG**

Istället för att bara matcha nyckelord kan Strukturerad RAG analysera flygdetaljer (destination, datum, tid, flygbolag) från ett mejl och lagra dem på ett strukturerat sätt. Detta möjliggör precisa frågor som "Vilket flyg bokade jag till Paris på tisdag?"

## Implementera och lagra minne

Att implementera minne för AI-agenter innebär en systematisk process för **minneshantering**, som inkluderar att generera, lagra, hämta, integrera, uppdatera och till och med "glömma" (eller radera) information. Återvinning är en särskilt avgörande aspekt.

### Specialiserade minnesverktyg

#### Mem0

Ett sätt att lagra och hantera agentminne är genom specialiserade verktyg som Mem0. Mem0 fungerar som ett beständigt minneslager som gör det möjligt för agenter att återkalla relevanta interaktioner, lagra användarpreferenser och faktuell kontext samt lära av framgångar och misslyckanden över tid. Idén är att statslösa agenter blir tillståndsbevarande.

Det fungerar genom en **tvåfasig minnespipeline: extraktion och uppdatering**. Först skickas meddelanden som läggs till en agents tråd till Mem0-tjänsten, som använder en Large Language Model (LLM) för att sammanfatta konversationshistorik och extrahera nya minnen. Därefter avgör en LLM-driven uppdateringsfas om dessa minnen ska läggas till, ändras eller tas bort, och lagrar dem i en hybrid databas som kan inkludera vektor-, graf- och nyckel-värde databaser. Systemet stöder även olika minnestyper och kan inkorporera grafminne för att hantera relationer mellan entiteter.

#### Cognee

En annan kraftfull metod är att använda **Cognee**, ett öppen källkod-semantiskt minne för AI-agenter som omvandlar strukturerad och ostrukturerad data till frågebara kunskapsgrafer stödda av embeddings. Cognee erbjuder en **dubbel lagringsarkitektur** som kombinerar vektorsökning med grafrelationer, vilket ger agenter möjlighet att förstå inte bara vad som är likt, utan också hur koncept relaterar till varandra.

Det excellerar i **hybridåtervinning** som blandar vektorsimiläritet, grafstruktur och LLM-resonemang – från råtlookup av chunkar till grafmedveten frågeställning. Systemet upprätthåller ett **levande minne** som utvecklas och växer samtidigt som det förblir frågbart som en sammanlänkad graf, med stöd för både korttids-sessioner och långsiktigt bestående minne.

Cognee-notebooktutorian ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) visar hur man bygger detta enade minneslager, med praktiska exempel på ingestion av olika datakällor, visualisering av kunskapsgrafen och frågor med olika sökstrategier anpassade efter specifika agentbehov.

### Lagra minne med RAG

Utöver specialiserade minnesverktyg som mem0 kan du använda robusta söktjänster som **Azure AI Search som backend för lagring och hämtning av minnen**, särskilt för strukturerad RAG.

Detta gör att du kan grunda agentens svar i dina egna data, vilket säkerställer mer relevanta och korrekta svar. Azure AI Search kan användas för att lagra användarspecifika reseminnen, produktkataloger eller annan domänspecifik kunskap.

Azure AI Search stöder funktioner som **Strukturerad RAG**, vilket excellerar i att extrahera och återvinna tät, strukturerad information från stora datamängder såsom konversationshistorik, mejl eller till och med bilder. Detta ger "övermänsklig precision och recall" jämfört med traditionell textchunking och embeddings.

## Göra AI-agenter självförbättrande

Ett vanligt mönster för självförbättrande agenter involverar att införa en **"kunskapsagent"**. Denna separata agent observerar huvudsamtalet mellan användaren och den primära agenten. Dess roll är att:

1. **Identifiera värdefull information**: Avgöra om någon del av konversationen är värd att spara som allmän kunskap eller specifik användarpreferens.

2. **Extrahera och sammanfatta**: Destillera det väsentliga lärandet eller preferensen från konversationen.

3. **Lagra i en kunskapsbas**: Spara denna extraherade information, ofta i en vektordatabas, så att den kan hämtas senare.

4. **Förstärka framtida frågor**: När användaren initierar en ny fråga hämtar kunskapsagenten relevant sparad information och lägger till den i användarens prompt, vilket ger avgörande kontext till huvudagenten (liknande RAG).

### Optimeringar för minne

• **Latenshantering**: För att undvika att bromsa användarinteraktioner kan en billigare, snabbare modell användas initialt för att snabbt kontrollera om information är värd att lagra eller hämta, och endast aktivera den mer komplexa extraktions-/återvinningsprocessen vid behov.

• **Underhåll av kunskapsbas**: För en växande kunskapsbas kan mindre frekvent använd information flyttas till "kall lagring" för kostnadseffektivitet.

## Har du fler frågor om agentminne?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra elever, delta i kontorstid och få svar på dina frågor om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->