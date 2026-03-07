[![Introduktion till AI‑agenter](../../../translated_images/sv/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klicka på bilden ovan för att se videon för denna lektion)_


# Introduktion till AI‑agenter och användningsfall för agenter

Välkommen till kursen "AI‑agenter för nybörjare"! Denna kurs ger grundläggande kunskap och praktiska exempel för att bygga AI‑agenter.

Gå med i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord-community</a> för att träffa andra deltagare och AI‑agentbyggare och ställa frågor om denna kurs.

För att starta denna kurs börjar vi med att få en bättre förståelse för vad AI‑agenter är och hur vi kan använda dem i de applikationer och arbetsflöden vi bygger.

## Introduktion

Denna lektion täcker:

- Vad är AI‑agenter och vilka är de olika typerna av agenter?
- Vilka användningsfall passar bäst för AI‑agenter och hur kan de hjälpa oss?
- Vilka är några av de grundläggande byggstenarna när man utformar agentiska lösningar?

## Lärandemål
Efter att ha slutfört denna lektion bör du kunna:

- Förstå koncepten kring AI‑agenter och hur de skiljer sig från andra AI‑lösningar.
- Använda AI‑agenter på ett effektivt sätt.
- Designa agentiska lösningar produktivt för både användare och kunder.

## Definition av AI‑agenter och typer av AI‑agenter

### Vad är AI‑agenter?

AI‑agenter är **system** som gör det möjligt för **stora språkmodeller (LLMs)** att **utföra åtgärder** genom att utöka sina kapaciteter genom att ge LLMs **åtkomst till verktyg** och **kunskap**.

Låt oss bryta ned denna definition i mindre delar:

- **System** - Det är viktigt att tänka på agenter inte bara som en enskild komponent utan som ett system av många komponenter. På grundläggande nivå är komponenterna i en AI‑agent:
  - **Miljö** - Det definierade utrymmet där AI‑agenten verkar. Till exempel, om vi hade en reseboknings‑AI‑agent, kan miljön vara resebokningssystemet som AI‑agenten använder för att slutföra uppgifter.
  - **Sensorer** - Miljöer har information och ger återkoppling. AI‑agenter använder sensorer för att samla in och tolka denna information om miljöns nuvarande tillstånd. I exemplet med resebokningsagenten kan resebokningssystemet ge information såsom tillgänglighet för hotell eller flygpriser.
  - **Aktuatorer** - När AI‑agenten får information om miljöns nuvarande tillstånd bestämmer agenten för den aktuella uppgiften vilken åtgärd som ska utföras för att förändra miljön. För resebokningsagenten kan det vara att boka ett tillgängligt rum åt användaren.

![Vad är AI‑agenter?](../../../translated_images/sv/what-are-ai-agents.1ec8c4d548af601a.webp)

**Stora språkmodeller** - Begreppet agenter fanns innan skapandet av LLMs. Fördelen med att bygga AI‑agenter med LLMs är deras förmåga att tolka mänskligt språk och data. Denna förmåga gör det möjligt för LLMs att tolka miljöinformation och definiera en plan för att förändra miljön.

**Utföra åtgärder** - Utanför AI‑agentsystem är LLMs begränsade till situationer där åtgärden är att generera innehåll eller information baserat på en användares uppmaning. Inom AI‑agentsystem kan LLMs utföra uppgifter genom att tolka användarens begäran och använda verktyg som finns tillgängliga i deras miljö.

**Tillgång till verktyg** - Vilka verktyg LLM har tillgång till definieras av 1) miljön den verkar i och 2) utvecklaren av AI‑agenten. I vårt exempel med reseagenten är agentens verktyg begränsade av de operationer som finns i bokningssystemet, och/eller kan utvecklaren begränsa agentens verktygstillgång till flyg.

**Minne+Kunskap** - Minne kan vara kortsiktigt i kontexten av konversationen mellan användaren och agenten. Långsiktigt, utöver den information som tillhandahålls av miljön, kan AI‑agenter också hämta kunskap från andra system, tjänster, verktyg och till och med andra agenter. I reseagentsexemplet kan denna kunskap vara information om användarens resepreferenser som finns i en kunddatabas.

### De olika typerna av agenter

Nu när vi har en allmän definition av AI‑agenter, låt oss titta på några specifika agenttyper och hur de skulle tillämpas på en reseboknings‑AI‑agent.

| **Agenttyp**                  | **Beskrivning**                                                                                                                      | **Exempel**                                                                                                                                                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enkla reflexagenter**       | Utför omedelbara åtgärder baserat på fördefinierade regler.                                                                           | Reseagent tolkar kontexten i ett e‑postmeddelande och vidarebefordrar reseklagomål till kundservice.                                                                                                                           |
| **Modellbaserade reflexagenter** | Utför åtgärder baserat på en modell av världen och förändringar i den modellen.                                                      | Reseagent prioriterar rutter med betydande prisförändringar baserat på tillgång till historiska prisdata.                                                                                                                     |
| **Målbaserade agenter**       | Skapar planer för att uppnå specifika mål genom att tolka målet och avgöra vilka åtgärder som krävs för att nå det.                   | Reseagent bokar en resa genom att avgöra nödvändiga researrangemang (bil, kollektivtrafik, flyg) från nuvarande plats till destinationen.                                                                                          |
| **Nytta‑baserade agenter**    | Tar hänsyn till preferenser och väger avvägningar numeriskt för att avgöra hur man uppnår mål.                                        | Reseagent maximerar nyttan genom att väga bekvämlighet mot kostnad vid bokning av resor.                                                                                                                                    |
| **Lärande agenter**           | Förbättras över tid genom att reagera på återkoppling och justera åtgärder i enlighet därmed.                                         | Reseagent förbättras genom att använda kundfeedback från efterresorundersökningar för att göra justeringar i framtida bokningar.                                                                                               |
| **Hierarkiska agenter**       | Innehåller flera agenter i ett nivådelat system, där högre nivåer delar upp uppgifter i deluppgifter för lägre nivåer att slutföra.  | Reseagent avbokar en resa genom att dela upp uppgiften i deluppgifter (till exempel avboka specifika bokningar) och låta lägre nivåsagenter slutföra dem, rapportera tillbaka till den högre nivån.                                |
| **Fleragentsystem (MAS)**     | Agenter utför uppgifter oberoende, antingen samarbetande eller konkurrerande.                                                        | Samarbetande: Flera agenter bokar specifika resetjänster såsom hotell, flyg och underhållning. Konkurrerande: Flera agenter hanterar och konkurrerar om en gemensam hotellbokningskalender för att boka kunder på hotellet. |

## När man ska använda AI‑agenter

I det tidigare avsnittet använde vi användningsfallet Reseagent för att förklara hur de olika typerna av agenter kan användas i olika scenarier för resebokning. Vi kommer att fortsätta använda denna applikation genom hela kursen.

Låt oss titta på vilka typer av användningsfall som AI‑agenter passar bäst för:

![När ska man använda AI‑agenter?](../../../translated_images/sv/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Öppna problem** - tillåter LLM att avgöra vilka steg som behövs för att slutföra en uppgift eftersom det inte alltid går att hårdkoda i ett arbetsflöde.
- **Flerstegsprocesser** - uppgifter som kräver en nivå av komplexitet där AI‑agenten behöver använda verktyg eller information över flera vändor istället för engångshämtning.  
- **Förbättring över tid** - uppgifter där agenten kan förbättras över tid genom att få återkoppling från antingen sin miljö eller användare för att ge bättre nytta.

Vi tar upp fler överväganden kring användning av AI‑agenter i lektionen Bygga pålitliga AI‑agenter.

## Grundläggande om agentiska lösningar

### Agentutveckling

Det första steget i att utforma ett AI‑agentsystem är att definiera verktyg, åtgärder och beteenden. I denna kurs fokuserar vi på att använda **Azure AI Agent Service** för att definiera våra agenter. Den erbjuder funktioner som:

- Val av öppna modeller såsom OpenAI, Mistral och Llama
- Användning av licensierade data genom leverantörer som Tripadvisor
- Användning av standardiserade OpenAPI 3.0‑verktyg

### Agentiska mönster

Kommunikation med LLM sker via prompts. Med tanke på AI‑agenters semiautonoma natur är det inte alltid möjligt eller nödvändigt att manuellt omprompta LLM efter en förändring i miljön. Vi använder **agentiska mönster** som gör att vi kan prompta LLM över flera steg på ett mer skalbart sätt.

Denna kurs är indelad i några av de för närvarande populära agentiska mönstren.

### Agentiska ramverk

Agentiska ramverk tillåter utvecklare att implementera agentiska mönster genom kod. Dessa ramverk erbjuder mallar, plugins och verktyg för bättre samarbete mellan AI‑agenter. Dessa fördelar ger möjligheter till bättre observabilitet och felsökning av AI‑agentsystem.

I denna kurs kommer vi att utforska Microsoft Agent Framework (MAF) för att bygga produktionsklara AI‑agenter.

## Kodexempel

- Python: [Agentramverk](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agentramverk](./code_samples/01-dotnet-agent-framework.md)

## Fler frågor om AI‑agenter?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra deltagare, delta i kontorstider och få dina frågor om AI‑agenter besvarade.

## Föregående lektion

[Kursuppsättning](../00-course-setup/README.md)

## Nästa lektion

[Utforska agentiska ramverk](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfriskrivning:
Detta dokument har översatts med hjälp av AI-översättningstjänsten Co-op Translator (https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på originalspråket bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell, mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->