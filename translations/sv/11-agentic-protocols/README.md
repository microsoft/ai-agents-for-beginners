# Användning av agentprotokoll (MCP, A2A och NLWeb)

[![Agentprotokoll](../../../translated_images/sv/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

När användningen av AI-agenter ökar, ökar också behovet av protokoll som säkerställer standardisering, säkerhet och stödjer öppen innovation. I denna lektion kommer vi att gå igenom 3 protokoll som syftar till att möta detta behov - Model Context Protocol (MCP), Agent to Agent (A2A) och Natural Language Web (NLWeb).

## Introduktion

I denna lektion kommer vi att täcka:

• Hur **MCP** tillåter AI-agenter att få åtkomst till externa verktyg och data för att slutföra användarens uppgifter.

• Hur **A2A** möjliggör kommunikation och samarbete mellan olika AI-agenter.

• Hur **NLWeb** förser vilken webbplats som helst med naturliga språkgränssnitt så att AI-agenter kan upptäcka och interagera med innehållet.

## Lärandemål

• **Identifiera** huvudsyftet och fördelarna med MCP, A2A och NLWeb i samband med AI-agenter.

• **Förklara** hur varje protokoll underlättar kommunikation och interaktion mellan LLM:er, verktyg och andra agenter.

• **Känna igen** de olika roller varje protokoll spelar vid uppbyggnaden av komplexa agentiska system.

## Model Context Protocol

The **Model Context Protocol (MCP)** är en öppen standard som tillhandahåller ett standardiserat sätt för applikationer att ge kontext och verktyg till LLM:er. Detta möjliggör en "universell adapter" till olika datakällor och verktyg som AI-agenter kan ansluta till på ett konsekvent sätt.

Låt oss titta på komponenterna i MCP, fördelarna jämfört med direkt API-användning, och ett exempel på hur AI-agenter kan använda en MCP-server.

### MCP:s kärnkomponenter

MCP fungerar på en **klient-server-arkitektur** och kärnkomponenterna är:

• **Hosts** är LLM-applikationer (till exempel en kodredigerare som VSCode) som initierar anslutningarna till en MCP-server.

• **Clients** är komponenter inom värdapplikationen som upprätthåller en en-till-en-anslutning med servrar.

• **Servers** är lättviktiga program som exponerar specifika kapabiliteter.

Inkluderat i protokollet finns tre grundläggande primitiva enheter som är kapabiliteterna hos en MCP-server:

• **Tools**: Dessa är diskreta åtgärder eller funktioner som en AI-agent kan anropa för att utföra en handling. Till exempel kan en vädertjänst exponera ett "get weather"-verktyg, eller en e-handelsserver kan exponera ett "purchase product"-verktyg. MCP-servrar annonserar varje verktygs namn, beskrivning och input/output-schema i sin kapabilitetslista.

• **Resources**: Dessa är skrivskyddade dataobjekt eller dokument som en MCP-server kan tillhandahålla, och klienter kan hämta dem vid behov. Exempel inkluderar filinnehåll, databasposter eller loggfiler. Resurser kan vara text (som kod eller JSON) eller binära (som bilder eller PDF-filer).

• **Prompts**: Dessa är fördefinierade mallar som ger föreslagna uppmaningar och möjliggör mer komplexa arbetsflöden.

### Fördelar med MCP

MCP erbjuder betydande fördelar för AI-agenter:

• **Dynamisk upptäckt av verktyg**: Agenter kan dynamiskt ta emot en lista över tillgängliga verktyg från en server tillsammans med beskrivningar av vad de gör. Detta står i kontrast till traditionella API:er, som ofta kräver statisk kodning för integrationer, vilket innebär att varje API-ändring kräver koduppdateringar. MCP erbjuder ett "integrera en gång"-sätt, vilket leder till större anpassningsbarhet.

• **Interoperabilitet över LLM:er**: MCP fungerar över olika LLM:er, vilket ger flexibilitet att byta kärnmodeller för att utvärdera bättre prestanda.

• **Standardiserad säkerhet**: MCP inkluderar en standardiserad autentiseringsmetod, vilket förbättrar skalbarheten när man lägger till åtkomst till ytterligare MCP-servrar. Detta är enklare än att hantera olika nycklar och autentiseringstyper för olika traditionella API:er.

### MCP-exempel

![MCP-diagram](../../../translated_images/sv/mcp-diagram.e4ca1cbd551444a1.webp)

Föreställ dig att en användare vill boka en flygresa med hjälp av en AI-assistent som drivs av MCP.

1. **Anslutning**: AI-assistenten (MCP-klienten) ansluter till en MCP-server som tillhandahålls av ett flygbolag.

2. **Verktygsupptäckt**: Klienten frågar flygbolagets MCP-server, "Vilka verktyg har ni tillgängliga?" Servern svarar med verktyg som "search flights" och "book flights".

3. **Verktygsanrop**: Du ber sedan AI-assistenten, "Sök efter en flygning från Portland till Honolulu." AI-assistenten, med hjälp av sin LLM, identifierar att den behöver anropa verktyget "search flights" och skickar relevanta parametrar (avreseort, destination) till MCP-servern.

4. **Utförande och svar**: MCP-servern, som agerar som en wrapper, gör det faktiska anropet till flygbolagets interna boknings-API. Den tar emot flyginformationen (t.ex. JSON-data) och skickar den tillbaka till AI-assistenten.

5. **Ytterligare interaktion**: AI-assistenten presenterar flygalternativen. När du väljer en flygning kan assistenten anropa verktyget "book flight" på samma MCP-server och slutföra bokningen.

## Agent-to-Agent Protocol (A2A)

Medan MCP fokuserar på att koppla LLM:er till verktyg, tar **Agent-to-Agent (A2A)-protokollet** det ett steg längre genom att möjliggöra kommunikation och samarbete mellan olika AI-agenter. A2A kopplar samman AI-agenter över olika organisationer, miljöer och teknologistackar för att slutföra en gemensam uppgift.

Vi kommer att undersöka komponenterna och fördelarna med A2A, tillsammans med ett exempel på hur det kan tillämpas i vår reseapplikation.

### A2A:s kärnkomponenter

A2A fokuserar på att möjliggöra kommunikation mellan agenter och att låta dem arbeta tillsammans för att slutföra en deluppgift åt användaren. Varje komponent i protokollet bidrar till detta:

#### Agentkort

Liknande hur en MCP-server delar en lista med verktyg, har ett Agentkort:
- Agentens namn.
- En **beskrivning av de generella uppgifter** den utför.
- En **lista över specifika färdigheter** med beskrivningar för att hjälpa andra agenter (eller till och med mänskliga användare) förstå när och varför de vill anropa den agenten.
- Den **nuvarande Endpoint URL** för agenten
- **versionen** och **kapabiliteterna** hos agenten såsom sändning av strömmande svar och push-notifikationer.

#### Agentutförare

Agentutföraren ansvarar för att **skicka kontexten från användarchatten till den fjärrstyrda agenten**, den fjärrstyrda agenten behöver detta för att förstå uppgiften som ska utföras. I en A2A-server använder en agent sin egen Large Language Model (LLM) för att tolka inkommande förfrågningar och utföra uppgifter med sina egna interna verktyg.

#### Artefakt

När en fjärragent har slutfört den begärda uppgiften skapas dess arbetsprodukt som en artefakt. En artefakt **innehåller resultatet av agentens arbete**, en **beskrivning av vad som slutfördes**, och den **textkontext** som skickas genom protokollet. Efter att artefakten har skickats stängs anslutningen till den fjärrstyrda agenten tills den behövs igen.

#### Händelsekö

Denna komponent används för **hantering av uppdateringar och vidarebefordran av meddelanden**. Den är särskilt viktig i produktion för agentiska system för att förhindra att anslutningen mellan agenter stängs innan en uppgift är slutförd, särskilt när uppgiftens slutförandetid kan vara längre.

### Fördelar med A2A

• **Förbättrat samarbete**: Det gör det möjligt för agenter från olika leverantörer och plattformar att interagera, dela kontext och arbeta tillsammans, vilket underlättar sömlös automatisering över traditionellt åtskilda system.

• **Flexibilitet i modellval**: Varje A2A-agent kan välja vilken LLM den använder för att hantera sina förfrågningar, vilket möjliggör optimerade eller finjusterade modeller per agent, till skillnad från en enda LLM-anslutning i vissa MCP-scenarier.

• **Inbyggd autentisering**: Autentisering är integrerad direkt i A2A-protokollet och tillhandahåller ett robust säkerhetsramverk för agentinteraktioner.

### A2A-exempel

![A2A-diagram](../../../translated_images/sv/A2A-Diagram.8666928d648acc26.webp)

Låt oss utöka vårt scenario för resebokning, men denna gång med A2A.

1. **Användarens förfrågan till multi-agent**: En användare interagerar med en "Travel Agent" A2A-klient/agent, kanske genom att säga, "Boka en hel resa till Honolulu nästa vecka, inklusive flyg, hotell och hyrbil".

2. **Orkestrering av Travel Agent**: Travel Agent tar emot denna komplexa förfrågan. Den använder sin LLM för att resonera kring uppgiften och avgöra att den behöver interagera med andra specialiserade agenter.

3. **Inter-agentkommunikation**: Travel Agent använder sedan A2A-protokollet för att ansluta till downstream-agenter, såsom en "Airline Agent", en "Hotel Agent" och en "Car Rental Agent" som skapats av olika företag.

4. **Delegerad utförande av uppgifter**: Travel Agent skickar specifika uppgifter till dessa specialiserade agenter (t.ex. "Hitta flyg till Honolulu", "Boka ett hotell", "Hyra en bil"). Var och en av dessa specialiserade agenter, som kör sina egna LLM:er och använder sina egna verktyg (vilka i sig kan vara MCP-servrar), utför sin specifika del av bokningen.

5. **Konsoliderat svar**: När alla nedströmsagenter slutfört sina uppgifter sammanställer Travel Agent resultaten (flyguppgifter, hotellbekräftelse, hyrbilsbokning) och skickar ett omfattande, chattliknande svar tillbaka till användaren.

## Natural Language Web (NLWeb)

Webbplatser har länge varit det primära sättet för användare att få tillgång till information och data över internet.

Låt oss titta på de olika komponenterna i NLWeb, fördelarna med NLWeb och ett exempel på hur vår NLWeb fungerar genom att titta på vår reseapplikation.

### Komponenter i NLWeb

- **NLWeb-applikation (kärntjänstkod)**: Systemet som bearbetar frågor i naturligt språk. Det kopplar ihop plattformens olika delar för att skapa svar. Du kan tänka på det som **motorn som driver webbplatsens funktioner för naturligt språk**.

- **NLWeb-protokollet**: Detta är en **grundläggande uppsättning regler för interaktion i naturligt språk** med en webbplats. Det skickar tillbaka svar i JSON-format (ofta med Schema.org). Dess syfte är att skapa en enkel grund för ”AI-webben”, på samma sätt som HTML gjorde det möjligt att dela dokument online.

- **MCP-server (Model Context Protocol Endpoint)**: Varje NLWeb-uppsättning fungerar också som en **MCP-server**. Detta betyder att den kan **dela verktyg (som en "ask"-metod) och data** med andra AI-system. I praktiken gör detta webbplatsens innehåll och funktioner användbara för AI-agenter, vilket tillåter att sidan blir en del av det bredare ”agent-ekosystemet.”

- **Inbäddningsmodeller**: Dessa modeller används för att **omvandla webbplatsens innehåll till numeriska representationer kallade vektorer** (embeddings). Dessa vektorer fångar betydelse på ett sätt som datorer kan jämföra och söka i. De lagras i en särskild databas, och användare kan välja vilken inbäddningsmodell de vill använda.

- **Vektordatabas (sökmekanism)**: Denna databas **lagrar inbäddningarna av webbplatsinnehållet**. När någon ställer en fråga kontrollerar NLWeb vektordatabasen för att snabbt hitta den mest relevanta informationen. Den ger en snabb lista över möjliga svar, rankade efter likhet. NLWeb fungerar med olika vektorlagringssystem såsom Qdrant, Snowflake, Milvus, Azure AI Search och Elasticsearch.

### NLWeb-exempel

![NLWeb](../../../translated_images/sv/nlweb-diagram.c1e2390b310e5fe4.webp)

Tänk igen på vår webbplats för resebokning, men den här gången drivs den av NLWeb.

1. **Dataingestion**: Webbplatsens befintliga produktkataloger (t.ex. flyglistor, hotellsbeskrivningar, paketresor) formateras med Schema.org eller laddas via RSS-flöden. NLWebs verktyg importerar dessa strukturerade data, skapar inbäddningar och lagrar dem i en lokal eller fjärrliggande vektordatabas.

2. **Fråga i naturligt språk (mänsklig)**: En användare besöker webbplatsen och, istället för att navigera via menyer, skriver i ett chattgränssnitt: "Hitta ett familjevänligt hotell i Honolulu med pool för nästa vecka".

3. **NLWeb-bearbetning**: NLWeb-applikationen tar emot frågan. Den skickar frågan till en LLM för förståelse och söker samtidigt i sin vektordatabas efter relevanta hotelllistningar.

4. **Exakta resultat**: LLM:en hjälper till att tolka sökresultaten från databasen, identifiera de bästa matchningarna baserat på kriterierna "familjevänligt", "pool" och "Honolulu", och formaterar därefter ett svar i naturligt språk. Avgörande är att svaret hänvisar till faktiska hotell från webbplatsens katalog, vilket undviker påhittad information.

5. **Interaktion med AI-agent**: Eftersom NLWeb fungerar som en MCP-server kan en extern AI-reseagent också ansluta till webbplatsens NLWeb-instans. AI-agenten kan då använda MCP-metoden `ask` för att fråga webbplatsen direkt: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. NLWeb-instansen skulle bearbeta detta, utnyttja sin databas med information om restauranger (om den är inladdad) och returnera ett strukturerat JSON-svar.

### Fler frågor om MCP/A2A/NLWeb?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra lärande, delta i mottagningstider och få dina frågor om AI-agenter besvarade.

## Resurser

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För information av kritisk betydelse rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->