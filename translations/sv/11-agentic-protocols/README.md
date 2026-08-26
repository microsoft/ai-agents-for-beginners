# Använda Agentic Protocols (MCP, A2A och NLWeb)

[![Agentic Protocols](../../../translated_images/sv/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

I takt med att användningen av AI-agenter ökar, så ökar också behovet av protokoll som säkerställer standardisering, säkerhet och stödjer öppen innovation. I denna lektion kommer vi att gå igenom 3 protokoll som syftar till att möta detta behov - Model Context Protocol (MCP), Agent to Agent (A2A) och Natural Language Web (NLWeb).

## Introduktion

I denna lektion kommer vi att täcka:

• Hur **MCP** tillåter AI-agenter att använda externa verktyg och data för att slutföra användaruppgifter.

• Hur **A2A** möjliggör kommunikation och samarbete mellan olika AI-agenter.

• Hur **NLWeb** ger naturliga språkgränssnitt till vilken webbplats som helst, vilket möjliggör för AI-agenter att hitta och interagera med innehållet.

## Läromål

• **Identifiera** huvudsyftet och fördelarna med MCP, A2A och NLWeb i kontexten av AI-agenter.

• **Förklara** hur varje protokoll underlättar kommunikation och interaktion mellan LLMs, verktyg och andra agenter.

• **Känna igen** de olika roller som varje protokoll spelar i att bygga komplexa agentiska system.

## Model Context Protocol

**Model Context Protocol (MCP)** är en öppen standard som tillhandahåller ett standardiserat sätt för applikationer att ge kontext och verktyg till LLMs. Detta möjliggör en "universell adapter" till olika datakällor och verktyg som AI-agenter kan ansluta till på ett konsekvent sätt.

Låt oss titta på komponenterna i MCP, fördelarna jämfört med direkt API-användning, och ett exempel på hur AI-agenter kan använda en MCP-server.

### MCPs kärnkomponenter

MCP bygger på en **klient-server-arkitektur** och kärnkomponenterna är:

• **Hosts** är LLM-applikationer (till exempel en kodredigerare som VSCode) som startar anslutningarna till en MCP-server.

• **Clients** är komponenter inom host-applikationen som bibehåller en-till-en-anslutningar med servrar.

• **Servers** är lätta program som exponerar specifika funktioner.

Inkluderat i protokollet finns tre kärnprimitiv som är kapaciteterna hos en MCP-server:

• **Verktyg**: Det här är diskreta handlingar eller funktioner som en AI-agent kan anropa för att utföra en handling. Till exempel kan en vädertjänst exponera ett "hämta väder"-verktyg, eller en e-handelsserver kan exponera ett "köp produkt"-verktyg. MCP-servrar annonserar varje verktygs namn, beskrivning och input/output-schema i deras kapabilitetslista.

• **Resurser**: Detta är dataobjekt eller dokument med endast läsrättigheter som en MCP-server kan tillhandahålla, och klienter kan hämta dem vid behov. Exempel inkluderar filinnehåll, databaspunkter eller loggfiler. Resurser kan vara text (som kod eller JSON) eller binära (som bilder eller PDF-filer).

• **Prompter**: Det här är fördefinierade mallar som ger föreslagna anrop, vilket möjliggör mer komplexa arbetsflöden.

### Fördelar med MCP

MCP erbjuder betydande fördelar för AI-agenter:

• **Dynamisk verktygsupptäckt**: Agenter kan dynamiskt erhålla en lista på tillgängliga verktyg från en server tillsammans med beskrivningar av vad de gör. Detta står i kontrast till traditionella API:er, som ofta kräver statisk kodning för integrationer, vilket betyder att varje API-ändring kräver koduppdateringar. MCP erbjuder en "integrera en gång"-metod, vilket leder till större anpassningsbarhet.

• **Interoperabilitet mellan LLMs**: MCP fungerar över olika LLMs, vilket ger flexibilitet att byta kärnmodeller för att undersöka bättre prestanda.

• **Standardiserad säkerhet**: MCP inkluderar en standardiserad autentiseringsmetod, vilket förbättrar skalbarheten när man lägger till tillgång till ytterligare MCP-servrar. Detta är enklare än att hantera olika nycklar och autentiseringstyper för flera traditionella API:er.

### MCP-exempel

![MCP Diagram](../../../translated_images/sv/mcp-diagram.e4ca1cbd551444a1.webp)

Föreställ dig att en användare vill boka en flygresa med hjälp av en AI-assistent som drivs av MCP.

1. **Anslutning**: AI-assistenten (MCP-klienten) ansluter till en MCP-server som tillhandahålls av ett flygbolag.

2. **Verktygsupptäckt**: Klienten frågar flygbolagets MCP-server: "Vilka verktyg har ni tillgängliga?" Servern svarar med verktyg som "sök flyg" och "boka flyg".

3. **Verktygsanrop**: Du ber sedan AI-assistenten: "Sök efter en flygresa från Portland till Honolulu." AI-assistenten, med hjälp av sin LLM, identifierar att den behöver anropa verktyget "sök flyg" och skickar relevanta parametrar (ursprung, destination) till MCP-servern.

4. **Utförande och svar**: MCP-servern, som fungerar som ett omslag, gör det faktiska anropet till flygbolagets interna boknings-API. Den tar emot flyginformationen (t.ex. JSON-data) och skickar den tillbaka till AI-assistenten.

5. **Vidare interaktion**: AI-assistenten visar flygalternativen. När du har valt en flygning kan assistenten anropa verktyget "boka flyg" på samma MCP-server och slutföra bokningen.

## Agent-till-Agent-protokoll (A2A)

Medan MCP fokuserar på att koppla LLMs till verktyg, tar **Agent-to-Agent (A2A) protokollet** det ett steg längre genom att möjliggöra kommunikation och samarbete mellan olika AI-agenter. A2A kopplar AI-agenter över olika organisationer, miljöer och tekniska stackar för att slutföra en gemensam uppgift.

Vi kommer att undersöka komponenterna och fördelarna med A2A, tillsammans med ett exempel på hur det kan tillämpas i vår reseapplikation.

### A2A kärnkomponenter

A2A fokuserar på att möjliggöra kommunikation mellan agenter och att de arbetar tillsammans för att slutföra deluppgifter åt användaren. Varje komponent i protokollet bidrar till detta:

#### Agentkort

På liknande sätt som en MCP-server delar en lista på verktyg, har ett Agentkort:
- Agentens namn.
- En **beskrivning av de generella uppgifterna** den utför.
- En **lista över specifika färdigheter** med beskrivningar för att hjälpa andra agenter (eller till och med mänskliga användare) att förstå när och varför de vill anropa den agenten.
- Agentens **nuvarande endpoint-URL**.
- Agentens **version** och **funktioner** som t.ex. streaming-svar och push-notiser.

#### Agentutförare

Agentutföraren ansvarar för att **skicka användarens chattkontext till den fjärranslutna agenten**, vilken behöver detta för att förstå uppgiften som ska utföras. I en A2A-server använder en agent sin egen Large Language Model (LLM) för att tolka inkommande förfrågningar och utföra uppgifter med sina egna interna verktyg.

#### Artefakt

När en fjärragent har slutfört den begärda uppgiften skapas dess arbetsprodukt som en artefakt. En artefakt **innehåller resultatet av agentens arbete**, en **beskrivning av vad som slutförts**, och den **textkontext** som skickas genom protokollet. Efter att artefakten har skickats stängs anslutningen till den fjärranslutna agenten tills den behövs igen.

#### Evenemangskö

Denna komponent används för **hantering av uppdateringar och överföring av meddelanden**. Den är särskilt viktig i produktion för agentiska system för att förhindra att anslutningen mellan agenter stängs innan en uppgift är slutförd, särskilt när uppgiftens slutförandetid kan vara längre.

### Fördelar med A2A

• **Förbättrat samarbete**: Det möjliggör för agenter från olika leverantörer och plattformar att interagera, dela kontext och arbeta tillsammans, vilket underlättar sömlös automatisering över traditionellt separerade system.

• **Flexibilitet i modellval**: Varje A2A-agent kan bestämma vilken LLM den använder för att hantera sina förfrågningar, vilket tillåter optimerade eller finjusterade modeller per agent, till skillnad från en enda LLM-anslutning i vissa MCP-scenarier.

• **Inbyggd autentisering**: Autentisering är direkt integrerad i A2A-protokollet, vilket ger en robust säkerhetsram för agentinteraktioner.

### A2A-exempel

![A2A Diagram](../../../translated_images/sv/A2A-Diagram.8666928d648acc26.webp)

Låt oss utveckla vår scen för resebokning, men denna gång med A2A.

1. **Användarförfrågan till multi-agent**: En användare interagerar med en "Reseagent" A2A-klient/agent, kanske genom att säga: "Boka en komplett resa till Honolulu nästa vecka, inklusive flyg, hotell och hyrbil".

2. **Orkestrering av reseagenten**: Reseagenten tar emot denna komplexa förfrågan. Den använder sin LLM för att resonera om uppgiften och avgör att den behöver interagera med andra specialiserade agenter.

3. **Kommunikation mellan agenter**: Reseagenten använder sedan A2A-protokollet för att ansluta till underordnade agenter, såsom en "Flygbolagsagent", en "Hotelagent" och en "Hyrbilsagent" som skapas av olika företag.

4. **Delegation av uppgifter**: Reseagenten skickar specifika uppgifter till dessa specialiserade agenter (t.ex. "Hitta flyg till Honolulu", "Boka hotell", "Hyra bil"). Var och en av dessa specialiserade agenter, som kör sina egna LLMs och använder sina egna verktyg (vilka kan vara MCP-servrar själva), utför sin del av bokningen.

5. **Konsoliderat svar**: När alla underordnade agenter har slutfört sina uppgifter sammanställer reseagenten resultaten (flygdetaljer, hotellbekräftelse, hyrbilsbokning) och skickar ett omfattande, chattformat svar tillbaka till användaren.

## Natural Language Web (NLWeb)

Webbplatser har länge varit det primära sättet för användare att få tillgång till information och data över internet.

Låt oss titta på de olika komponenterna i NLWeb, fördelarna med NLWeb och ett exempel på hur vår NLWeb fungerar genom att titta på vår reseapplikation.

### Komponenter i NLWeb

- **NLWeb-applikation (Kärntjänstkod)**: Systemet som bearbetar frågor på naturligt språk. Det kopplar samman olika delar av plattformen för att skapa svar. Du kan tänka på det som **motorn som driver de naturliga språkfunktionerna** på en webbplats.

- **NLWeb Protokoll**: Detta är en **grundläggande uppsättning regler för naturlig språkinteraktion** med en webbplats. Det skickar tillbaka svar i JSON-format (ofta med Schema.org). Syftet är att skapa en enkel grund för "AI-webben", på samma sätt som HTML gjorde det möjligt att dela dokument online.

- **MCP-server (Model Context Protocol Endpoint)**: Varje NLWeb-installation fungerar också som en **MCP-server**. Det betyder att den kan **dela verktyg (som en "ask"-metod) och data** med andra AI-system. I praktiken gör detta webbplatsens innehåll och funktioner användbara för AI-agenter, vilket låter sidan bli en del av det bredare "agentekosystemet."

- **Embedding-modeller**: Dessa modeller används för att **omvandla webbplatsinnehåll till numeriska representationer kallade vektorer (embeddings)**. Dessa vektorer fångar betydelse på ett sätt som datorer kan jämföra och söka i. De lagras i en speciell databas, och användare kan välja vilken embedding-modell de vill använda.

- **Vektordatabas (Hämtmekanism)**: Denna databas **lagrar embeddingar av webbplatsens innehåll**. När någon ställer en fråga söker NLWeb i vektordatabasen för att snabbt hitta den mest relevanta informationen. Det ger en snabb lista över möjliga svar, rankade efter likhet. NLWeb fungerar med olika lagringssystem som Qdrant, Snowflake, Milvus, Azure AI Search och Elasticsearch.

### NLWeb med exempel

![NLWeb](../../../translated_images/sv/nlweb-diagram.c1e2390b310e5fe4.webp)

Tänk på vår resebokningswebbplats igen, men denna gång drivs den av NLWeb.

1. **Datainmatning**: Resesajtens befintliga produktkataloger (t.ex. flyglistor, hotellsbeskrivningar, paketresor) formateras med Schema.org eller laddas via RSS-flöden. NLWebs verktyg tar in denna strukturerade data, skapar embeddingar och lagrar dem i en lokal eller fjärrbaserad vektordatabas.

2. **Naturlig språkfråga (människa)**: En användare besöker webbplatsen och istället för att navigera i menyer skriver hen i ett chattgränssnitt: "Hitta ett familjevänligt hotell i Honolulu med pool för nästa vecka".

3. **NLWeb-bearbetning**: NLWeb-applikationen tar emot denna fråga. Den skickar frågan till en LLM för förståelse och söker samtidigt i sin vektordatabas efter relevanta hotelllistor.

4. **Exakta resultat**: LLM hjälper till att tolka sökresultaten från databasen, identifiera de bästa matchningarna baserat på kriterierna "familjevänligt", "pool" och "Honolulu", och formaterar sedan ett svar i naturligt språk. Viktigt är att svaret refererar till faktiska hotell från webbplatsens katalog, vilket undviker påhittad information.

5. **Interaktion med AI-agent**: Eftersom NLWeb fungerar som en MCP-server kan en extern AI-reseagent också ansluta till denna webbplats NLWeb-instans. AI-agenten kan då använda `ask`-MCP-metoden för att direkt fråga webbplatsen: `ask("Finns det några veganska restauranger i Honoluluområdet som rekommenderas av hotellet?")`. NLWeb-instansen skulle bearbeta detta, utnyttja sin databas med restauranginformation (om den är inläst), och returnera ett strukturerat JSON-svar.

### Har du fler frågor om MCP/A2A/NLWeb?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra lärande, delta i kontorstider och få svar på dina AI-agentfrågor.

## Resurser

- [MCP för nybörjare](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Föregående Lektion

[AI-agenter i produktion](../10-ai-agents-production/README.md)

## Nästa Lektion

[Kontextengineering för AI-agenter](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->