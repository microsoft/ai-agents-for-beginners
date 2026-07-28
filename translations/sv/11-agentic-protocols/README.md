# Använda Agentiska Protokoll (MCP, A2A och NLWeb)

[![Agentic Protocols](../../../translated_images/sv/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

I takt med att användningen av AI-agenter ökar ökar också behovet av protokoll som säkerställer standardisering, säkerhet och stödjer öppen innovation. I denna lektion kommer vi att behandla 3 protokoll som syftar till att möta detta behov - Model Context Protocol (MCP), Agent to Agent (A2A) och Natural Language Web (NLWeb).

## Introduktion

I denna lektion kommer vi att gå igenom:

• Hur **MCP** tillåter AI-agenter att få åtkomst till externa verktyg och data för att slutföra användaruppgifter.

• Hur **A2A** möjliggör kommunikation och samarbete mellan olika AI-agenter.

• Hur **NLWeb** för med sig naturliga språkgränssnitt till vilken webbplats som helst och gör att AI-agenter kan upptäcka och interagera med innehållet.

## Lärandemål

• **Identifiera** det centrala syftet och fördelarna med MCP, A2A och NLWeb i kontexten av AI-agenter.

• **Förklara** hur varje protokoll underlättar kommunikation och interaktion mellan LLM:er, verktyg och andra agenter.

• **Känna igen** de särskilda roller som varje protokoll spelar i att bygga komplexa agentiska system.

## Model Context Protocol

**Model Context Protocol (MCP)** är en öppen standard som tillhandahåller ett standardiserat sätt för applikationer att ge kontext och verktyg till LLM:er. Detta möjliggör en "universal adapter" till olika datakällor och verktyg som AI-agenter kan ansluta till på ett konsekvent sätt.

Låt oss titta på komponenterna i MCP, fördelarna jämfört med direkt API-användning, och ett exempel på hur AI-agenter kan använda en MCP-server.

### MCP Kärnkomponenter

MCP bygger på en **klient-serverarkitektur** och kärnkomponenterna är:

• **Hosts** är LLM-applikationer (till exempel en kodredigerare som VSCode) som startar kopplingarna till en MCP-server.

• **Clients** är komponenter inom host-applikationen som upprätthåller en-till-en-anslutningar med servrar.

• **Servers** är lätta program som exponerar specifika kapabiliteter.

Inkluderat i protokollet finns tre kärnprimitiver som är kapabiliteterna hos en MCP-server:

• **Verktyg**: Detta är diskreta åtgärder eller funktioner som en AI-agent kan kalla för att utföra en handling. Till exempel kan en vädertjänst exponera ett "hämta väder"-verktyg, eller en e-handelsserver kan exponera ett "köp produkt"-verktyg. MCP-servrar annonserar varje verktygs namn, beskrivning och in-/utmatningsschema i sin kapabilitetslista.

• **Resurser**: Detta är skrivskyddade dataobjekt eller dokument som en MCP-server kan tillhandahålla och klienter kan hämta dem på begäran. Exempel inkluderar filinnehåll, databaspunkter eller loggfiler. Resurser kan vara text (som kod eller JSON) eller binära (som bilder eller PDF:er).

• **Prompter**: Dessa är fördefinierade mallar som erbjuder föreslagna prompter, vilket möjliggör mer komplexa arbetsflöden.

### Fördelar med MCP

MCP erbjuder betydande fördelar för AI-agenter:

• **Dynamisk verktygsupptäckt**: Agenter kan dynamiskt få en lista över tillgängliga verktyg från en server tillsammans med beskrivningar av vad de gör. Detta står i kontrast till traditionella API:er som ofta kräver statisk kodning för integrationer, vilket innebär att varje API-ändring kräver koduppdateringar. MCP erbjuder en "integrera en gång"-metod, vilket leder till större anpassningsbarhet.

• **Interoperabilitet över LLM:er**: MCP fungerar över olika LLM:er och ger flexibilitet att byta ut kärnmodeller för att utvärdera bättre prestanda.

• **Standardiserad säkerhet**: MCP inkluderar en standardiserad autentiseringsmetod, vilket förbättrar skalbarheten när man lägger till åtkomst till ytterligare MCP-servrar. Detta är enklare än att hantera olika nycklar och autentiseringstyper för olika traditionella API:er.

### MCP Exempel

![MCP Diagram](../../../translated_images/sv/mcp-diagram.e4ca1cbd551444a1.webp)

Föreställ dig att en användare vill boka en flygresa med hjälp av en AI-assistent som drivs av MCP.

1. **Anslutning**: AI-assistenten (MCP-klienten) ansluter till en MCP-server som tillhandahålls av ett flygbolag.

2. **Verktygsupptäckt**: Klienten frågar flygbolagets MCP-server: "Vilka verktyg har ni tillgängliga?" Servern svarar med verktyg som "sök flyg" och "boka flyg".

3. **Verktygsanrop**: Du ber sedan AI-assistenten: "Vänligen sök efter en flygning från Portland till Honolulu." AI-assistenten, med hjälp av sin LLM, identifierar att den behöver kalla på "search flights"-verktyget och skickar relevanta parametrar (ursprung, destination) till MCP-servern.

4. **Utförande och Svar**: MCP-servern, som agerar som ett omslag, gör det faktiska anropet till flygbolagets interna boknings-API. Den tar emot flyginformationen (t.ex. JSON-data) och skickar tillbaka den till AI-assistenten.

5. **Vidare Interaktion**: AI-assistenten presenterar flygalternativen. När du väljer en flygning kan assistenten anropa "bokningsverktyget" på samma MCP-server och slutföra bokningen.

## Agent-till-Agent Protokoll (A2A)

Medan MCP fokuserar på att koppla LLM:er till verktyg, tar **Agent-till-Agent (A2A) protokollet** det ett steg längre genom att möjliggöra kommunikation och samarbete mellan olika AI-agenter. A2A kopplar AI-agenter från olika organisationer, miljöer och teknologiska stackar för att slutföra en gemensam uppgift.

Vi kommer att undersöka komponenterna och fördelarna med A2A, samt ett exempel på hur det kan tillämpas i vår reseapplikation.

### A2A Kärnkomponenter

A2A fokuserar på att möjliggöra kommunikation mellan agenter och låta dem samarbeta för att slutföra en deluppgift åt användaren. Varje komponent i protokollet bidrar till detta:

#### Agentkort

På samma sätt som en MCP-server delar en lista av verktyg, har ett Agentkort:
- Namnet på agenten.
- En **beskrivning av de allmänna uppgifter** den utför.
- En **lista över specifika färdigheter** med beskrivningar för att hjälpa andra agenter (eller till och med mänskliga användare) att förstå när och varför de skulle vilja anropa den agenten.
- **Den nuvarande slutanvändar-URL:**en för agenten.
- **Versionen** och **kapabiliteter** för agenten såsom strömmande svar och push-notiser.

#### Agentutförare

Agentutföraren ansvarar för **att vidarebefordra användarchattens kontext till den fjärrstyrda agenten**, den fjärrstyrda agenten behöver detta för att förstå uppgiften som ska utföras. I en A2A-server använder en agent sin egen Large Language Model (LLM) för att tolka inkommande förfrågningar och utföra uppgifter med sina egna interna verktyg.

#### Artefakt

När en fjärragent har slutfört den begärda uppgiften skapas dess arbetsprodukt som en artefakt. En artefakt **innehåller resultatet av agentens arbete**, en **beskrivning av vad som slutförts**, och den **textuella kontexten** som skickas via protokollet. Efter att artefakten skickats stängs anslutningen med den fjärrstyrda agenten tills den behövs igen.

#### Händelsekö

Denna komponent används för **att hantera uppdateringar och vidarebefordra meddelanden**. Den är särskilt viktig i produktion för agentiska system för att förhindra att anslutningen mellan agenter stängs innan en uppgift är slutförd, särskilt när uppgiftens slutförandetid kan vara längre.

### Fördelar med A2A

• **Förbättrat samarbete**: Det gör det möjligt för agenter från olika leverantörer och plattformar att interagera, dela kontext och samarbeta, vilket underlättar sömlös automatisering över traditionellt oanslutna system.

• **Modellvalsfrihet**: Varje A2A-agent kan bestämma vilken LLM den använder för att hantera sina förfrågningar, vilket tillåter optimerade eller finjusterade modeller per agent, till skillnad från en enda LLM-anslutning i vissa MCP-scenarier.

• **Inbyggd autentisering**: Autentisering är integrerad direkt i A2A-protokollet och tillhandahåller ett robust säkerhetsramverk för agentinteraktioner.

### A2A Exempel

![A2A Diagram](../../../translated_images/sv/A2A-Diagram.8666928d648acc26.webp)

Låt oss utveckla vårt resebokningsscenario, men denna gång med A2A.

1. **Användarförfrågan till Multi-Agent**: En användare interagerar med en "Reseagent"-A2A-klient/agent, kanske genom att säga: "Vänligen boka en hel resa till Honolulu nästa vecka, inklusive flyg, hotell och hyrbil".

2. **Orkestrering av Reseagenten**: Reseagenten får denna komplexa förfrågan. Den använder sin LLM för att resonera kring uppgiften och avgöra att den behöver interagera med andra specialiserade agenter.

3. **Interagentkommunikation**: Reseagenten använder sedan A2A-protokollet för att koppla till nedströmsagenter, såsom en "Flygbolagsagent", en "Hotellagent" och en "Hyrbilsagent" som skapas av olika företag.

4. **Delegation av Uppgiftsutförande**: Reseagenten skickar specifika uppgifter till dessa specialiserade agenter (t.ex. "Hitta flyg till Honolulu", "Boka hotell", "Hyr bil"). Var och en av dessa specialiserade agenter, som kör egna LLM:er och använder sina egna verktyg (vilka kan vara MCP-servrar själva), utför sin specifika del av bokningen.

5. **Sammanställd Respons**: När alla nedströmsagenter har slutfört sina uppgifter samlar Reseagenten ihop resultaten (flyguppgifter, hotellbekräftelse, hyrbilsbokning) och skickar ett omfattande, chattliknande svar tillbaka till användaren.

## Natural Language Web (NLWeb)

Webbplatser har länge varit det primära sättet för användare att få tillgång till information och data över internet.

Låt oss titta på de olika komponenterna i NLWeb, fördelarna med NLWeb och ett exempel på hur vårt NLWeb fungerar genom att titta på vår reseapplikation.

### Komponenter i NLWeb

- **NLWeb-applikation (Kärntjänstkod)**: Systemet som bearbetar frågor på naturligt språk. Det kopplar samman de olika delarna av plattformen för att skapa svar. Du kan tänka på det som **motorn som driver webbplatsens naturliga språkfunktioner**.

- **NLWeb-protokoll**: En **grundläggande uppsättning regler för naturlig språkinteraktion** med en webbplats. Det skickar tillbaka svar i JSON-format (ofta med Schema.org). Syftet är att skapa en enkel grund för ”AI-webben”, på samma sätt som HTML gjorde det möjligt att dela dokument online.

- **MCP-server (Model Context Protocol Endpoint)**: Varje NLWeb-upplägg fungerar också som en **MCP-server**. Det betyder att den kan **dela verktyg (som en ”ask”-metod) och data** med andra AI-system. I praktiken gör detta webbplatsens innehåll och kapabiliteter användbara för AI-agenter, vilket gör att sidan blir en del av det bredare ”agentekosystemet.”

- **Embeddingmodeller**: Dessa modeller används för att **omvandla webbplatsinnehåll till numeriska representationer kallade vektorer** (embeddingar). Dessa vektorer fångar mening på ett sätt som datorer kan jämföra och söka i. De lagras i en särskild databas, och användare kan välja vilken embeddingmodell de vill använda.

- **Vektordatabas (Sökmekanism)**: Denna databas **lagrar embeddingar av webbplatsinnehållet**. När någon ställer en fråga söker NLWeb i vektordatabasen för att snabbt hitta mest relevant information. Den ger en snabb lista över möjliga svar, rankade efter likhet. NLWeb fungerar med olika vektorlager som Qdrant, Snowflake, Milvus, Azure AI Search och Elasticsearch.

### NLWeb genom Exempel

![NLWeb](../../../translated_images/sv/nlweb-diagram.c1e2390b310e5fe4.webp)

Tänk på vår resebokningswebbplats igen, men denna gång drivs den av NLWeb.

1. **Dataingestering**: Resesajtens befintliga produktkataloger (t.ex. flyglistor, hotellbeskrivningar, paketresor) formateras med Schema.org eller laddas via RSS-flöden. NLWeb:s verktyg hämtar denna strukturerade data, skapar embeddingar och lagrar dem i en lokal eller fjärrstyrd vektordatabas.

2. **Fråga på naturligt språk (mänskligt)**: En användare besöker webbplatsen och skriver istället för att navigera i menyer in i en chattgränssnitt: ”Hitta ett familjevänligt hotell i Honolulu med pool nästa vecka”.

3. **NLWeb-bearbetning**: NLWeb-applikationen tar emot denna fråga. Den skickar frågan till en LLM för förståelse och söker samtidigt i sin vektordatabas efter relevanta hotelllistor.

4. **Exakta resultat**: LLM hjälper till att tolka sökresultaten från databasen, identifiera bästa matchningar baserat på kriterierna ”familjevänligt,” ”pool” och ”Honolulu,” och formaterar sedan ett svar på naturligt språk. Viktigt är att svaret hänvisar till faktiska hotell från webbplatsens katalog och undviker påhittad information.

5. **AI-Agentinteraktion**: Eftersom NLWeb fungerar som en MCP-server kan en extern AI-resagent också koppla till denna webbplats NLWeb-instans. AI-agenten kan då använda MCP-metoden `ask` för att fråga webbplatsen direkt: `ask("Finns det några veganska restauranger i Honolulu-området som rekommenderas av hotellet?")`. NLWeb-instansen skulle bearbeta detta, utnyttja sin databas med restauranginformation (om laddad), och returnera ett strukturerat JSON-svar.

### Fler frågor om MCP/A2A/NLWeb?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra elever, delta i kontorstid och få svar på dina frågor om AI-agenter.

## Resurser

- [MCP för Nybörjare](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Föregående Lektion

[AI Agents in Production](../10-ai-agents-production/README.md)

## Nästa Lektion

[Context Engineering for AI Agents](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->