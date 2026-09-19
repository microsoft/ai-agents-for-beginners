# Använda Agentiska Protokoll (MCP, A2A och NLWeb)

[![Agentiska Protokoll](../../../translated_images/sv/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

I takt med att användningen av AI-agenter växer, ökar även behovet av protokoll som säkerställer standardisering, säkerhet och stödjer öppen innovation. I denna lektion kommer vi att täcka 3 protokoll som syftar till att möta detta behov - Model Context Protocol (MCP), Agent to Agent (A2A) och Natural Language Web (NLWeb).

## Introduktion

I denna lektion kommer vi att gå igenom:

• Hur **MCP** tillåter AI-agenter att få tillgång till externa verktyg och data för att slutföra användaruppgifter.

• Hur **A2A** möjliggör kommunikation och samarbete mellan olika AI-agenter.

• Hur **NLWeb** introducerar naturliga språkgränssnitt till vilken webbplats som helst, vilket gör det möjligt för AI-agenter att upptäcka och interagera med innehållet.

## Lärandemål

• **Identifiera** huvudsyftet och fördelarna med MCP, A2A och NLWeb i kontexten av AI-agenter.

• **Förklara** hur varje protokoll underlättar kommunikation och interaktion mellan LLMs, verktyg och andra agenter.

• **Känna igen** de olika roller som varje protokoll spelar i att bygga komplexa agentiska system.

## Model Context Protocol

**Model Context Protocol (MCP)** är en öppen standard som tillhandahåller ett standardiserat sätt för applikationer att ge kontext och verktyg till LLMs. Detta möjliggör en "universell adapter" till olika datakällor och verktyg som AI-agenter kan ansluta till på ett konsekvent sätt.

Låt oss titta på komponenterna i MCP, fördelarna jämfört med direkt API-användning och ett exempel på hur AI-agenter kan använda en MCP-server.

### MCP Kärnkomponenter

MCP fungerar på en **klient-server-arkitektur** och kärnkomponenterna är:

• **Hosts** är LLM-applikationer (till exempel en kodredigerare som VSCode) som initierar anslutningarna till en MCP-server.

• **Klienter** är komponenter inom host-applikationen som upprätthåller en-till-en-anslutningar med servrar.

• **Servrar** är lättviktsprogram som exponerar specifika kapabiliteter.

I protokollet ingår tre kärn-primitiver som är kapabiliteterna hos en MCP-server:

• **Verktyg**: Dessa är diskreta åtgärder eller funktioner som en AI-agent kan anropa för att utföra en handling. Till exempel kan en vädertjänst exponera ett "get weather"-verktyg, eller en e-handelsserver kan exponera ett "purchase product"-verktyg. MCP-servrar annonserar varje verktygs namn, beskrivning och input/output-schema i sin kapabilitetslista.

• **Resurser**: Dessa är skrivskyddade dataobjekt eller dokument som en MCP-server kan tillhandahålla och som klienter kan hämta vid behov. Exempel inkluderar filinnehåll, databasposter eller loggfiler. Resurser kan vara text (som kod eller JSON) eller binära (som bilder eller PDF-filer).

• **Prompter**: Dessa är fördefinierade mallar som ger föreslagna prompter, vilket möjliggör mer komplexa arbetsflöden.

### Fördelar med MCP

MCP erbjuder betydande fördelar för AI-agenter:

• **Dynamisk verktygsupptäckt**: Agenter kan dynamiskt få en lista över tillgängliga verktyg från en server tillsammans med beskrivningar av vad de gör. Detta står i kontrast till traditionella API:er som ofta kräver statisk kodning för integrationer, vilket innebär att varje API-ändring kräver koduppdateringar. MCP erbjuder ett "integrera en gång"-tillvägagångssätt, vilket leder till större anpassningsbarhet.

• **Interoperabilitet över LLMs**: MCP fungerar över olika LLMs och ger flexibilitet att byta kärnmodeller för bättre prestanda.

• **Standardiserad säkerhet**: MCP inkluderar en standardiserad autentiseringsmetod, vilket förbättrar skalbarheten när man lägger till tillgång till ytterligare MCP-servrar. Detta är enklare än att hantera olika nycklar och autentiseringstyper för olika traditionella API:er.

### MCP Exempel

![MCP Diagram](../../../translated_images/sv/mcp-diagram.e4ca1cbd551444a1.webp)

Föreställ dig att en användare vill boka en flygresa med en AI-assistent som drivs av MCP.

1. **Anslutning**: AI-assistenten (MCP-klienten) ansluter till en MCP-server som tillhandahålls av ett flygbolag.

2. **Verktygsupptäckt**: Klienten frågar flygbolagets MCP-server: "Vilka verktyg har ni tillgängliga?" Servern svarar med verktyg som "sök flyg" och "boka flyg".

3. **Verktygsanrop**: Du ber sedan AI-assistenten, "Vänligen sök efter en flygresa från Portland till Honolulu." AI-assistenten, med sin LLM, identifierar att den behöver anropa "sök flyg"-verktyget och skickar relevanta parametrar (ursprung, destination) till MCP-servern.

4. **Utförande och svar**: MCP-servern, som fungerar som ett omslag, gör det faktiska anropet till flygbolagets interna boknings-API. Den tar emot flyginformationen (t.ex. JSON-data) och skickar tillbaka den till AI-assistenten.

5. **Vidare interaktion**: AI-assistenten presenterar flygalternativen. När du väljer en flygresa kan assistenten anropa "boka flyg"-verktyget på samma MCP-server och slutföra bokningen.

## Agent-till-Agent Protokoll (A2A)

Medan MCP fokuserar på att koppla LLMs till verktyg, tar **Agent-till-Agent (A2A) protokollet** det ett steg längre genom att möjliggöra kommunikation och samarbete mellan olika AI-agenter. A2A kopplar samman AI-agenter över olika organisationer, miljöer och teknikstackar för att slutföra gemensamma uppgifter.

Vi kommer att undersöka komponenterna och fördelarna med A2A, tillsammans med ett exempel på hur det kan tillämpas i vår reseapplikation.

### A2A Kärnkomponenter

A2A fokuserar på att möjliggöra kommunikation mellan agenter och att få dem att samarbeta för att slutföra en användaruppgift. Varje komponent i protokollet bidrar till detta:

#### Agentkort

Liknande hur en MCP-server delar en lista över verktyg, innehåller ett Agentkort:
- Agentens namn.
- En **beskrivning av de allmänna uppgifter** den utför.
- En **lista över specifika färdigheter** med beskrivningar för att hjälpa andra agenter (eller även mänskliga användare) förstå när och varför de skulle vilja anropa den agenten.
- Agentens **nuvarande Endpoint-URL**
- Agentens **version** och **kapabiliteter** såsom streaming-responser och push-notiser.

#### Agentexekverare

Agentexekveraren ansvarar för att **skicka med kontexten från användarchatten till den fjärranslutna agenten**; den fjärranslutna agenten behöver detta för att förstå uppgiften som ska slutföras. I en A2A-server använder en agent sin egen Large Language Model (LLM) för att tolka inkommande förfrågningar och utföra uppgifter med sina egna interna verktyg.

#### Artefakt

När en fjärragent har slutfört den begärda uppgiften skapas dess arbetsprodukt som en artefakt. En artefakt **innehåller resultatet av agentens arbete**, en **beskrivning av vad som slutförts** och den **textkontext** som förmedlas genom protokollet. Efter att artefakten skickats avslutas anslutningen med fjärragenten tills den behövs igen.

#### Händelsekö

Denna komponent används för **hantering av uppdateringar och meddelandeöverföring**. Den är särskilt viktig i produktionsmiljö för agentiska system för att förhindra att anslutningen mellan agenter stängs innan en uppgift är slutförd, särskilt när uppgiftens slutförandetid kan vara längre.

### Fördelar med A2A

• **Förbättrat samarbete**: Den möjliggör att agenter från olika leverantörer och plattformar kan interagera, dela kontext och arbeta tillsammans, vilket underlättar sömlös automatisering över traditionellt frånkopplade system.

• **Flexibilitet i modellval**: Varje A2A-agent kan välja vilken LLM den använder för att betjäna sina förfrågningar, vilket tillåter optimerade eller finjusterade modeller per agent, till skillnad från en enda LLM-anslutning i vissa MCP-scenarier.

• **Inbyggd autentisering**: Autentisering är integrerad direkt i A2A-protokollet, vilket tillhandahåller en robust säkerhetsram för agentinteraktioner.

### A2A Exempel

![A2A Diagram](../../../translated_images/sv/A2A-Diagram.8666928d648acc26.webp)

Låt oss utveckla vårt resebokningsscenario, men den här gången med A2A.

1. **Användarförfrågan till multi-agent**: En användare interagerar med en "Reseagent"-A2A klient/agent, kanske genom att säga, "Vänligen boka en hel resa till Honolulu nästa vecka, inklusive flyg, hotell och hyrbil".

2. **Orkestrering av Resagenten**: Resagenten tar emot denna komplexa förfrågan. Den använder sin LLM för att resonera kring uppgiften och avgöra att den behöver interagera med andra specialiserade agenter.

3. **Inter-agentkommunikation**: Resagenten använder sedan A2A-protokollet för att ansluta till downstream-agenter, såsom en "Flygbolagsagent", en "Hotellagent" och en "Biluthyrningsagent" som skapas av olika företag.

4. **Delegation av uppgiftsutförande**: Resagenten skickar specifika uppgifter till dessa specialiserade agenter (t.ex. "Hitta flyg till Honolulu", "Boka ett hotell", "Hyr en bil"). Varje av dessa specialiserade agenter, som kör sina egna LLMs och använder sina egna verktyg (som kan vara MCP-servrar själva), utför sin specifika del av bokningen.

5. **Konsoliderat svar**: När alla downstream-agenter slutfört sina uppgifter sammanställer Resagenten resultaten (flygdetails, hotellbekräftelse, biluthyrningsbokning) och skickar ett omfattande, chattlikt svar tillbaka till användaren.

## Natural Language Web (NLWeb)

Webbplatser har länge varit det primära sättet för användare att få tillgång till information och data över internet.

Låt oss titta på de olika komponenterna i NLWeb, fördelarna med NLWeb och ett exempel på hur vår NLWeb fungerar genom att titta på vår reseapplikation.

### Komponenter i NLWeb

- **NLWeb Applikation (Kärntjänstkod)**: Systemet som bearbetar frågor på naturligt språk. Det kopplar samman olika delar av plattformen för att skapa svar. Du kan tänka på det som **motorn som driver naturliga språkfunktioner** på en webbplats.

- **NLWeb Protokoll**: Detta är en **grundläggande uppsättning regler för naturlig språk-interaktion** med en webbplats. Det skickar tillbaka svar i JSON-format (ofta med Schema.org). Dess syfte är att skapa en enkel grund för "AI-webben", på samma sätt som HTML gjorde det möjligt att dela dokument online.

- **MCP Server (Model Context Protocol Endpoint)**: Varje NLWeb-installation fungerar också som en **MCP-server**. Det innebär att den kan **dela verktyg (som en "ask"-metod) och data** med andra AI-system. I praktiken gör detta webbplatsens innehåll och förmågor användbara för AI-agenter, vilket gör att sidan blir en del av det bredare "agentekosystemet".

- **Inbäddningsmodeller**: Dessa modeller används för att **konvertera webbplatsinnehåll till numeriska representationer kallade vektorer** (inbäddningar). Dessa vektorer fångar mening på ett sätt som datorer kan jämföra och söka i. De lagras i en speciell databas, och användare kan välja vilken inbäddningsmodell de vill använda.

- **Vektordatabas (återvinningsmekanism)**: Denna databas **lagrar inbäddningarna av webbplatsens innehåll**. När någon ställer en fråga söker NLWeb i vektordatabasen för att snabbt hitta den mest relevanta informationen. Den ger en snabb lista med möjliga svar, rangordnade efter likhet. NLWeb fungerar med olika vektorlagringssystem som Qdrant, Snowflake, Milvus, Azure AI Search och Elasticsearch.

### NLWeb genom exempel

![NLWeb](../../../translated_images/sv/nlweb-diagram.c1e2390b310e5fe4.webp)

Tänk på vår resebokningswebbplats igen, men denna gång är den driven av NLWeb.

1. **Dataingestering**: Reswebbplatsens befintliga produktkataloger (t.ex. flyglistor, hotellbeskrivningar, paketresor) formateras med Schema.org eller laddas via RSS-flöden. NLWeb:s verktyg tar in denna strukturerade data, skapar inbäddningar och lagrar dem i en lokal eller fjärransluten vektordatabas.

2. **Fråga på naturligt språk (mänsklig)**: En användare besöker webbplatsen och istället för att navigera i menyer skriver in i ett chattgränssnitt: "Hitta ett familjevänligt hotell i Honolulu med pool nästa vecka".

3. **NLWeb Bearbetning**: NLWeb-applikationen tar emot denna fråga. Den skickar frågan till en LLM för förståelse och söker samtidigt i sin vektordatabas efter relevanta hotellistor.

4. **Exakta resultat**: LLM hjälper till att tolka sökresultaten från databasen, identifiera de bästa matchningarna baserat på kriterierna "familjevänligt," "pool," och "Honolulu" och formaterar sedan ett svar på naturligt språk. Viktigt är att svaret refererar till faktiska hotell från webbplatsens katalog, och undviker påhittad information.

5. **AI Agent-interaktion**: Eftersom NLWeb fungerar som en MCP-server kan en extern AI reseagent också ansluta till denna webbplats NLWeb-instans. AI-agenten kan då använda `ask`-MCP-metoden för att direkt fråga webbplatsen: `ask("Finns det några veganvänliga restauranger i Honolulu-området rekommenderade av hotellet?")`. NLWeb-instansen bearbetar detta, utnyttjar sin databas med restauranginformation (om den är inläst) och returnerar ett strukturerat JSON-svar.

### Fler frågor om MCP/A2A/NLWeb?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra studerande, delta i kontorstid och få svar på dina frågor om AI-agenter.

## Resurser

- [MCP för nybörjare](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Föregående lektion

[AI-agenter i produktion](../10-ai-agents-production/README.md)

## Nästa lektion

[Kontextteknik för AI-agenter](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->