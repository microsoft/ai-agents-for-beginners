<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:01:26+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "sv"
}
-->
# Användning av Agentiska Protokoll (MCP, A2A och NLWeb)

[![Agentiska Protokoll](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.sv.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Klicka på bilden ovan för att se videon till denna lektion)_

När användningen av AI-agenter ökar, växer också behovet av protokoll som säkerställer standardisering, säkerhet och stöd för öppen innovation. I denna lektion kommer vi att gå igenom tre protokoll som syftar till att möta detta behov - Model Context Protocol (MCP), Agent to Agent (A2A) och Natural Language Web (NLWeb).

## Introduktion

I denna lektion kommer vi att gå igenom:

• Hur **MCP** gör det möjligt för AI-agenter att få tillgång till externa verktyg och data för att utföra användaruppgifter.

• Hur **A2A** möjliggör kommunikation och samarbete mellan olika AI-agenter.

• Hur **NLWeb** tillför naturliga språkgränssnitt till vilken webbplats som helst, vilket gör det möjligt för AI-agenter att upptäcka och interagera med innehållet.

## Lärandemål

• **Identifiera** huvudsyftet och fördelarna med MCP, A2A och NLWeb i kontexten av AI-agenter.

• **Förklara** hur varje protokoll underlättar kommunikation och interaktion mellan LLM:er, verktyg och andra agenter.

• **Känna igen** de olika roller som varje protokoll spelar i att bygga komplexa agentiska system.

## Model Context Protocol

**Model Context Protocol (MCP)** är en öppen standard som tillhandahåller ett standardiserat sätt för applikationer att ge kontext och verktyg till LLM:er. Detta möjliggör en "universell adapter" till olika datakällor och verktyg som AI-agenter kan ansluta till på ett konsekvent sätt.

Låt oss titta på MCP:s komponenter, fördelarna jämfört med direkt API-användning och ett exempel på hur AI-agenter kan använda en MCP-server.

### MCP Kärnkomponenter

MCP använder en **klient-server-arkitektur** och kärnkomponenterna är:

• **Hosts** är LLM-applikationer (till exempel en kodredigerare som VSCode) som initierar anslutningar till en MCP-server.

• **Clients** är komponenter inom host-applikationen som upprätthåller en-till-en-anslutningar med servrar.

• **Servers** är lättviktiga program som exponerar specifika funktioner.

Protokollet inkluderar tre kärnprimitiver som är MCP-serverns kapabiliteter:

• **Tools**: Dessa är separata åtgärder eller funktioner som en AI-agent kan kalla för att utföra en uppgift. Till exempel kan en vädertjänst exponera ett "hämta väder"-verktyg, eller en e-handelsserver kan exponera ett "köp produkt"-verktyg. MCP-servrar annonserar varje verktygs namn, beskrivning och in-/utdata-schema i sin kapabilitetslista.

• **Resources**: Dessa är skrivskyddade dataobjekt eller dokument som en MCP-server kan tillhandahålla, och klienter kan hämta dem vid behov. Exempel inkluderar filinnehåll, databasposter eller loggfiler. Resurser kan vara text (som kod eller JSON) eller binära (som bilder eller PDF:er).

• **Prompts**: Dessa är fördefinierade mallar som ger föreslagna prompts, vilket möjliggör mer komplexa arbetsflöden.

### Fördelar med MCP

MCP erbjuder betydande fördelar för AI-agenter:

• **Dynamisk Verktygsupptäckt**: Agenter kan dynamiskt ta emot en lista över tillgängliga verktyg från en server tillsammans med beskrivningar av vad de gör. Detta skiljer sig från traditionella API:er, som ofta kräver statisk kodning för integrationer, vilket innebär att varje API-ändring kräver koduppdateringar. MCP erbjuder ett "integrera en gång"-tillvägagångssätt, vilket leder till större anpassningsförmåga.

• **Interoperabilitet mellan LLM:er**: MCP fungerar över olika LLM:er, vilket ger flexibilitet att byta kärnmodeller för att utvärdera bättre prestanda.

• **Standardiserad Säkerhet**: MCP inkluderar en standardautentiseringsmetod, vilket förbättrar skalbarheten när fler MCP-servrar läggs till. Detta är enklare än att hantera olika nycklar och autentiseringstyper för olika traditionella API:er.

### MCP Exempel

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.sv.png)

Föreställ dig att en användare vill boka en flygresa med hjälp av en AI-assistent som drivs av MCP.

1. **Anslutning**: AI-assistenten (MCP-klienten) ansluter till en MCP-server som tillhandahålls av ett flygbolag.

2. **Verktygsupptäckt**: Klienten frågar flygbolagets MCP-server, "Vilka verktyg har ni tillgängliga?" Servern svarar med verktyg som "sök flyg" och "boka flyg".

3. **Verktygsanrop**: Du ber AI-assistenten, "Sök efter ett flyg från Portland till Honolulu." AI-assistenten, med hjälp av sin LLM, identifierar att den behöver kalla "sök flyg"-verktyget och skickar relevanta parametrar (ursprung, destination) till MCP-servern.

4. **Utförande och Svar**: MCP-servern, som fungerar som en wrapper, gör det faktiska anropet till flygbolagets interna boknings-API. Den tar emot flyginformationen (t.ex. JSON-data) och skickar tillbaka den till AI-assistenten.

5. **Vidare Interaktion**: AI-assistenten presenterar flygalternativen. När du väljer ett flyg kan assistenten kalla "boka flyg"-verktyget på samma MCP-server och slutföra bokningen.

## Agent-to-Agent Protocol (A2A)

Medan MCP fokuserar på att ansluta LLM:er till verktyg, tar **Agent-to-Agent (A2A) protokollet** det ett steg längre genom att möjliggöra kommunikation och samarbete mellan olika AI-agenter. A2A ansluter AI-agenter över olika organisationer, miljöer och tekniska stackar för att slutföra en gemensam uppgift.

Vi kommer att undersöka komponenterna och fördelarna med A2A, tillsammans med ett exempel på hur det kan tillämpas i vår reseapplikation.

### A2A Kärnkomponenter

A2A fokuserar på att möjliggöra kommunikation mellan agenter och få dem att arbeta tillsammans för att slutföra en deluppgift åt användaren. Varje komponent i protokollet bidrar till detta:

#### Agentkort

Precis som en MCP-server delar en lista över verktyg, har ett agentkort:
- Agentens namn.
- En **beskrivning av de allmänna uppgifter** den utför.
- En **lista över specifika färdigheter** med beskrivningar för att hjälpa andra agenter (eller till och med mänskliga användare) att förstå när och varför de skulle vilja kalla den agenten.
- Agentens **aktuella Endpoint-URL**.
- Agentens **version** och **kapabiliteter**, såsom strömmande svar och push-notiser.

#### Agentutförare

Agentutföraren ansvarar för att **skicka användarchattens kontext till den fjärragenten**, som behöver detta för att förstå uppgiften som ska utföras. I en A2A-server använder en agent sin egen Large Language Model (LLM) för att tolka inkommande förfrågningar och utföra uppgifter med sina egna interna verktyg.

#### Artefakt

När en fjärragent har slutfört den begärda uppgiften skapas dess arbetsprodukt som en artefakt. En artefakt **innehåller resultatet av agentens arbete**, en **beskrivning av vad som slutfördes**, och den **textkontext** som skickas genom protokollet. Efter att artefakten har skickats stängs anslutningen med den fjärragenten tills den behövs igen.

#### Händelsekö

Denna komponent används för att **hantera uppdateringar och skicka meddelanden**. Den är särskilt viktig i produktion för agentiska system för att förhindra att anslutningen mellan agenter stängs innan en uppgift är slutförd, särskilt när uppgiftens slutförandetid kan ta längre tid.

### Fördelar med A2A

• **Förbättrat Samarbete**: Det möjliggör att agenter från olika leverantörer och plattformar interagerar, delar kontext och arbetar tillsammans, vilket underlättar sömlös automatisering över traditionellt fristående system.

• **Flexibilitet i Modellval**: Varje A2A-agent kan bestämma vilken LLM den använder för att hantera sina förfrågningar, vilket möjliggör optimerade eller finjusterade modeller per agent, till skillnad från en enda LLM-anslutning i vissa MCP-scenarier.

• **Inbyggd Autentisering**: Autentisering är direkt integrerad i A2A-protokollet, vilket ger en robust säkerhetsram för interaktioner mellan agenter.

### A2A Exempel

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.sv.png)

Låt oss utveckla vårt resebokningsscenario, men denna gång med A2A.

1. **Användarförfrågan till Multi-Agent**: En användare interagerar med en "Reseagent" A2A-klient/agent, kanske genom att säga, "Boka en hel resa till Honolulu nästa vecka, inklusive flyg, hotell och hyrbil."

2. **Orkestrering av Reseagenten**: Reseagenten tar emot denna komplexa förfrågan. Den använder sin LLM för att resonera kring uppgiften och avgöra att den behöver interagera med andra specialiserade agenter.

3. **Inter-Agent Kommunikation**: Reseagenten använder A2A-protokollet för att ansluta till nedströmsagenter, såsom en "Flygagent," en "Hotellagent," och en "Biluthyrningsagent" som skapats av olika företag.

4. **Delegerad Uppgiftsutförande**: Reseagenten skickar specifika uppgifter till dessa specialiserade agenter (t.ex. "Hitta flyg till Honolulu," "Boka ett hotell," "Hyra en bil"). Var och en av dessa specialiserade agenter, som kör sina egna LLM:er och använder sina egna verktyg (som kan vara MCP-servrar själva), utför sin specifika del av bokningen.

5. **Sammanställd Svar**: När alla nedströmsagenter slutför sina uppgifter sammanställer reseagenten resultaten (flygdetaljer, hotellbekräftelse, biluthyrningsbokning) och skickar ett omfattande, chattformat svar tillbaka till användaren.

## Natural Language Web (NLWeb)

Webbplatser har länge varit det primära sättet för användare att få tillgång till information och data över internet.

Låt oss titta på de olika komponenterna i NLWeb, fördelarna med NLWeb och ett exempel på hur vår NLWeb fungerar genom att titta på vår reseapplikation.

### Komponenter i NLWeb

- **NLWeb-applikation (Kärnkod för tjänsten)**: Systemet som bearbetar frågor i naturligt språk. Det ansluter de olika delarna av plattformen för att skapa svar. Du kan tänka på det som **motorn som driver de naturliga språkfunktionerna** på en webbplats.

- **NLWeb-protokoll**: Detta är en **grundläggande uppsättning regler för interaktion med naturligt språk** på en webbplats. Det skickar tillbaka svar i JSON-format (ofta med Schema.org). Syftet är att skapa en enkel grund för "AI-webben," på samma sätt som HTML gjorde det möjligt att dela dokument online.

- **MCP-server (Model Context Protocol Endpoint)**: Varje NLWeb-installation fungerar också som en **MCP-server**. Detta innebär att den kan **dela verktyg (som en "fråga"-metod) och data** med andra AI-system. I praktiken gör detta webbplatsens innehåll och funktioner användbara för AI-agenter, vilket gör att webbplatsen blir en del av det bredare "agentekosystemet."

- **Inbäddningsmodeller**: Dessa modeller används för att **konvertera webbplatsinnehåll till numeriska representationer kallade vektorer** (inbäddningar). Dessa vektorer fångar mening på ett sätt som datorer kan jämföra och söka. De lagras i en speciell databas, och användare kan välja vilken inbäddningsmodell de vill använda.

- **Vektordatabas (Återhämtningsmekanism)**: Denna databas **lagrar inbäddningarna av webbplatsens innehåll**. När någon ställer en fråga kontrollerar NLWeb vektordatabasen för att snabbt hitta den mest relevanta informationen. Den ger en snabb lista över möjliga svar, rankade efter likhet. NLWeb fungerar med olika vektorlageringssystem såsom Qdrant, Snowflake, Milvus, Azure AI Search och Elasticsearch.

### NLWeb Exempel

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.sv.png)

Tänk på vår resebokningswebbplats igen, men denna gång drivs den av NLWeb.

1. **Dataingestion**: Resewebbplatsens befintliga produktkataloger (t.ex. flyglistor, hotellbeskrivningar, resepaket) formateras med Schema.org eller laddas via RSS-flöden. NLWeb:s verktyg tar in denna strukturerade data, skapar inbäddningar och lagrar dem i en lokal eller fjärransluten vektordatabas.

2. **Naturlig Språkfråga (Människa)**: En användare besöker webbplatsen och, istället för att navigera i menyer, skriver i ett chattgränssnitt: "Hitta ett familjevänligt hotell i Honolulu med pool för nästa vecka."

3. **NLWeb Bearbetning**: NLWeb-applikationen tar emot denna fråga. Den skickar frågan till en LLM för förståelse och söker samtidigt i sin vektordatabas efter relevanta hotelllistor.

4. **Exakta Resultat**: LLM hjälper till att tolka sökresultaten från databasen, identifiera de bästa matchningarna baserat på kriterierna "familjevänligt," "pool," och "Honolulu," och formaterar sedan ett svar i naturligt språk. Viktigt är att svaret hänvisar till faktiska hotell från webbplatsens katalog, och undviker påhittad information.

5. **AI-agent Interaktion**: Eftersom NLWeb fungerar som en MCP-server kan en extern AI-reseagent också ansluta till denna webbplats NLWeb-instans. AI-agenten kan då använda `ask` MCP-metoden för att direkt fråga webbplatsen: `ask("Finns det några veganska restauranger i Honolulu-området som rekommenderas av hotellet?")`. NLWeb-instansen skulle bearbeta detta, utnyttja sin databas med restauranginformation (om laddad), och returnera ett strukturerat JSON-svar.

### Har du fler frågor om MCP/A2A/NLWeb?

Gå med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra elever, delta i öppet hus och få svar på dina frågor om AI-agenter.

## Resurser

- [MCP för Nybörjare](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.