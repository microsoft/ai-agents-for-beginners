<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5cc6836626047aa055e8960c8484a7d0",
  "translation_date": "2025-08-29T16:06:30+00:00",
  "source_file": "11-agentic-protocols/code_samples/mcp-agents/README.md",
  "language_code": "sv"
}
-->
# Bygga kommunikationssystem mellan agenter med MCP

> Kortfattat - Kan du bygga Agent2Agent-kommunikation med MCP? Ja!

MCP har utvecklats avsevärt bortom sitt ursprungliga mål att "tillhandahålla kontext till LLMs". Med de senaste förbättringarna, inklusive [återupptagbara strömmar](https://modelcontextprotocol.io/docs/concepts/transports#resumability-and-redelivery), [elicitering](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), [sampling](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling) och notifieringar ([framsteg](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress) och [resurser](https://modelcontextprotocol.io/specification/2025-06-18/schema#resourceupdatednotification)), erbjuder MCP nu en robust grund för att bygga komplexa kommunikationssystem mellan agenter.

## Missuppfattningen om Agent/Verktyg

När fler utvecklare utforskar verktyg med agentliknande beteenden (körs under längre perioder, kan kräva ytterligare input under exekvering, etc.), är en vanlig missuppfattning att MCP är olämpligt, främst eftersom tidiga exempel på dess verktygsprimitive fokuserade på enkla begär-svar-mönster.

Denna uppfattning är föråldrad. MCP-specifikationen har förbättrats avsevärt under de senaste månaderna med funktioner som fyller gapet för att bygga långvariga agentliknande beteenden:

- **Streaming & Partiella Resultat**: Realtidsuppdateringar under exekvering
- **Återupptagbarhet**: Klienter kan återansluta och fortsätta efter avbrott
- **Hållbarhet**: Resultat överlever serveromstarter (t.ex. via resurslänkar)
- **Fleromgångsinteraktioner**: Interaktiv input under exekvering via elicitering och sampling

Dessa funktioner kan kombineras för att möjliggöra komplexa agentliknande och multi-agent-applikationer, alla implementerade på MCP-protokollet.

Som referens kommer vi att hänvisa till en agent som ett "verktyg" som är tillgängligt på en MCP-server. Detta innebär att det finns en värdapplikation som implementerar en MCP-klient som etablerar en session med MCP-servern och kan anropa agenten.

## Vad gör ett MCP-verktyg "agentliknande"?

Innan vi dyker in i implementeringen, låt oss fastställa vilka infrastrukturella kapaciteter som behövs för att stödja långvariga agenter.

> Vi definierar en agent som en enhet som kan arbeta autonomt under längre perioder, kapabel att hantera komplexa uppgifter som kan kräva flera interaktioner eller justeringar baserade på realtidsfeedback.

### 1. Streaming & Partiella Resultat

Traditionella begär-svar-mönster fungerar inte för långvariga uppgifter. Agenter behöver tillhandahålla:

- Realtidsuppdateringar om framsteg
- Intermediära resultat

**MCP-stöd**: Resursuppdateringsnotifieringar möjliggör streaming av partiella resultat, även om detta kräver noggrann design för att undvika konflikter med JSON-RPC:s 1:1 begär/svar-modell.

| Funktion                  | Användningsfall                                                                                                                                                                       | MCP-stöd                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Realtidsuppdateringar om framsteg | Användaren begär en kodbasmigreringsuppgift. Agenten streamar framsteg: "10% - Analyserar beroenden... 25% - Konverterar TypeScript-filer... 50% - Uppdaterar importer..."          | ✅ Framstegsnotifieringar                                                                  |
| Partiella resultat        | Uppgiften "Generera en bok" streamar partiella resultat, t.ex. 1) Berättelsens struktur, 2) Kapitellista, 3) Varje kapitel när det är klart. Värden kan inspektera, avbryta eller omdirigera vid varje steg. | ✅ Notifieringar kan "utökas" för att inkludera partiella resultat, se förslag på PR 383, 776 |

### 2. Återupptagbarhet

Agenter måste hantera nätverksavbrott smidigt:

- Återanslutning efter (klient)avbrott
- Fortsättning från där de slutade (meddelandeåterleverans)

**MCP-stöd**: MCP StreamableHTTP-transport stöder idag sessionsåterupptagning och meddelandeåterleverans med sessions-ID och senaste händelse-ID. Här är det viktigt att servern implementerar en EventStore som möjliggör händelseuppspelning vid klientåteranslutning.  
Observera att det finns ett communityförslag (PR #975) som utforskar transportoberoende återupptagbara strömmar.

| Funktion      | Användningsfall                                                                                                                                                   | MCP-stöd                                                                |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Återupptagbarhet | Klienten kopplas bort under en långvarig uppgift. Vid återanslutning återupptas sessionen med missade händelser uppspelade, fortsätter sömlöst från där den slutade. | ✅ StreamableHTTP-transport med sessions-ID, händelseuppspelning och EventStore |

### 3. Hållbarhet

Långvariga agenter behöver persistent tillstånd:

- Resultat överlever serveromstarter
- Status kan hämtas utanför sessionen
- Framstegsspårning över sessioner

**MCP-stöd**: MCP stöder nu en resurslänk som returtyp för verktygsanrop. Idag är ett möjligt mönster att designa ett verktyg som skapar en resurs och omedelbart returnerar en resurslänk. Verktyget kan fortsätta att hantera uppgiften i bakgrunden och uppdatera resursen. Klienten kan i sin tur välja att polla resursens status för att få partiella eller fullständiga resultat (baserat på vilka resursuppdateringar servern tillhandahåller) eller prenumerera på resursen för uppdateringsnotifieringar.

En begränsning här är att polling av resurser eller prenumeration på uppdateringar kan konsumera resurser med konsekvenser i stor skala. Det finns ett öppet communityförslag (inklusive #992) som utforskar möjligheten att inkludera webhooks eller triggers som servern kan använda för att notifiera klienten/värdapplikationen om uppdateringar.

| Funktion    | Användningsfall                                                                                                                                        | MCP-stöd                                                        |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Hållbarhet  | Servern kraschar under en datamigreringsuppgift. Resultat och framsteg överlever omstart, klienten kan kontrollera status och fortsätta från persistent resurs. | ✅ Resurslänkar med persistent lagring och statusnotifieringar |

### 4. Fleromgångsinteraktioner

Agenter behöver ofta ytterligare input under exekvering:

- Mänsklig förtydligande eller godkännande
- AI-assistans för komplexa beslut
- Dynamisk parameterjustering

**MCP-stöd**: Fullt stöd via sampling (för AI-input) och elicitering (för mänsklig input).

| Funktion                 | Användningsfall                                                                                                                                     | MCP-stöd                                           |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Fleromgångsinteraktioner | Resebokningsagenten begär prisbekräftelse från användaren och ber sedan AI att sammanfatta reseinformationen innan bokningen slutförs.              | ✅ Elicitering för mänsklig input, sampling för AI-input |

## Implementering av långvariga agenter på MCP - Kodöversikt

Som en del av denna artikel tillhandahåller vi ett [kodarkiv](https://github.com/victordibia/ai-tutorials/tree/main/MCP%20Agents) som innehåller en komplett implementering av långvariga agenter med MCP Python SDK och StreamableHTTP-transport för sessionsåterupptagning och meddelandeåterleverans. Implementeringen demonstrerar hur MCP-funktioner kan kombineras för att möjliggöra sofistikerade agentliknande beteenden.

Specifikt implementerar vi en server med två primära agentverktyg:

- **Reseagent** - Simulerar en resebokningstjänst med prisbekräftelse via elicitering
- **Forskningsagent** - Utför forskningsuppgifter med AI-assisterade sammanfattningar via sampling

Båda agenterna demonstrerar realtidsuppdateringar, interaktiva bekräftelser och fullständiga sessionsåterupptagningsmöjligheter.

## Utvidgning till multi-agent-kommunikation på MCP

Implementeringen ovan kan utvidgas till multi-agent-system genom att förbättra värdapplikationens intelligens och omfattning:

- **Intelligent uppgiftsnedbrytning**: Värden analyserar komplexa användarförfrågningar och bryter ner dem i deluppgifter för olika specialiserade agenter
- **Multi-server-koordinering**: Värden upprätthåller anslutningar till flera MCP-servrar, var och en exponerar olika agentkapaciteter
- **Uppgiftstillståndshantering**: Värden spårar framsteg över flera samtidiga agentuppgifter, hanterar beroenden och sekvensering
- **Resiliens & omförsök**: Värden hanterar fel, implementerar omförsökslogik och omdirigerar uppgifter när agenter blir otillgängliga
- **Resultatsyntes**: Värden kombinerar utdata från flera agenter till sammanhängande slutresultat

Värden utvecklas från en enkel klient till en intelligent orkestrator som koordinerar distribuerade agentkapaciteter samtidigt som MCP-protokollets grund bibehålls.

## Slutsats

MCP:s förbättrade kapaciteter - resursnotifieringar, elicitering/sampling, återupptagbara strömmar och persistenta resurser - möjliggör komplexa interaktioner mellan agenter samtidigt som protokollets enkelhet bibehålls.

## Kom igång

Redo att bygga ditt eget Agent2Agent-system? Följ dessa steg:

### 1. Kör demon

### 2. Testa återupptagningsmöjligheter

### 3. Utforska och utvidga

Detta demonstrerar hur MCP möjliggör intelligenta agentbeteenden samtidigt som verktygsbaserad enkelhet bibehålls.

Sammanfattningsvis utvecklas MCP-protokollspecifikationen snabbt; läsaren uppmuntras att granska den officiella dokumentationswebbplatsen för de senaste uppdateringarna - https://modelcontextprotocol.io/introduction

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.