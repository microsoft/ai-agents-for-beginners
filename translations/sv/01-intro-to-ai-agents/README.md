[![Intro to AI Agents](../../../translated_images/sv/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klicka på bilden ovan för att se videon för denna lektion)_

# Introduktion till AI-agenter och användningsområden för agenter

Välkommen till kursen **AI Agents for Beginners**! Denna kurs ger dig grundläggande kunskaper — och fungerande kod — för att börja bygga AI-agenter från grunden.

Kom och säg hej i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — den är full av lärande och AI-byggherrar som gärna svarar på frågor.

Innan vi börjar bygga, låt oss först se till att vi faktiskt förstår vad en AI-agent *är* och när det är vettigt att använda en.

---

## Introduktion

Den här lektionen täcker:

- Vad AI-agenter är, och de olika typer som finns
- Vilka typer av uppgifter AI-agenter är bäst lämpade för
- De grundläggande byggstenarna du använder när du designar en agentlösning

## Lärandemål

I slutet av denna lektion ska du kunna:

- Förklara vad en AI-agent är och hur den skiljer sig från en vanlig AI-lösning
- Veta när du ska använda en AI-agent (och när du inte ska)
- Skissa på en grundläggande agentlösningsdesign för ett verkligt problem

---

## Definiera AI-agenter och typer av AI-agenter

### Vad är AI-agenter?

Här är ett enkelt sätt att tänka på det:

> **AI-agenter är system som låter stora språkmodeller (LLMs) faktiskt *göra saker* — genom att ge dem verktyg och kunskap att agera i världen, inte bara svara på prompts.**

Låt oss bryta ner det lite:

- **System** — En AI-agent är inte bara en sak. Det är en samling delar som arbetar tillsammans. I grunden har varje agent tre delar:
  - **Miljö** — Den plats där agenten arbetar. För en resebokningsagent skulle detta vara bokningsplattformen själv.
  - **Sensorer** — Hur agenten läser det aktuella tillståndet i sin miljö. Vår reseagent kan t.ex. kontrollera tillgänglighet på hotell eller flygpriser.
  - **Aktuatorer** — Hur agenten agerar. Reseagenten kan boka ett rum, skicka en bekräftelse eller avboka en reservation.

![What Are AI Agents?](../../../translated_images/sv/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Stora språkmodeller** — Agenternas existens fanns innan LLMs, men LLMs är vad som gör moderna agenter så kraftfulla. De kan förstå naturligt språk, resonera kring kontext och förvandla en vag användarförfrågan till en konkret handlingsplan.

- **Utföra handlingar** — Utan ett agentsystem genererar en LLM bara text. Inuti ett agentsystem kan LLM faktiskt *utföra* steg — söka i en databas, anropa ett API, skicka ett meddelande.

- **Tillgång till verktyg** — Vilka verktyg agenten kan använda beror på (1) miljön den körs i och (2) vad utvecklaren valt att ge den. En reseagent kan exempelvis söka flyg men inte redigera kundregister — allt handlar om vad du kopplar ihop.

- **Minne + Kunskap** — Agenter kan ha korttidsminne (den pågående konversationen) och långtidsminne (en kunddatabas, tidigare interaktioner). Reseagenten kan "komma ihåg" att du föredrar fönsterplatser.

---

### De olika typerna av AI-agenter

Alla agenter är inte byggda på samma sätt. Här är en sammanställning av huvudtyperna, med resebokningsagenten som exempel genomgående:

| **Agenttyp** | **Vad den gör** | **Exempel med reseagent** |
|---|---|---|
| **Enkla reflexagenter** | Följer hårdkodade regler — inget minne, ingen planering. | Ser ett klagomail → vidarebefordrar det till kundtjänst. Det är allt. |
| **Modellbaserade reflexagenter** | Har en intern modell av världen och uppdaterar den när saker ändras. | Följer historiska flygpriser och flaggar rutter som plötsligt blivit dyrare. |
| **Målinriktade agenter** | Har ett mål i åtanke och klurar ut hur det ska nås steg för steg. | Bokar en hel resa (flyg, bil, hotell) från din nuvarande plats för att ta dig till destinationen. |
| **Nytta-baserade agenter** | Hittar inte bara *en* lösning — hittar *den bästa* genom att väga för- och nackdelar. | Väger kostnad mot bekvämlighet för att hitta resan som bäst passar dina preferenser. |
| **Lärande agenter** | Blir bättre med tiden genom att lära sig från feedback. | Justerar framtida bokningsrekommendationer baserat på enkätresultat efter resan. |
| **Hierarkiska agenter** | En övergripande agent delar upp arbete i deluppgifter och delegerar till underagenter. | En förfrågan om "avbokning av resa" delas upp i: avboka flyg, avboka hotell, avboka hyrbil — varje hanteras av en underagent. |
| **Multi-Agent System (MAS)** | Flera oberoende agenter som arbetar tillsammans (eller konkurrerar). | Samarbete: separata agenter hanterar hotell, flyg och nöjen. Konkurrens: flera agenter tävlar om att fylla hotellrum till bästa pris. |

---

## När ska man använda AI-agenter

Bara för att du *kan* använda en AI-agent betyder det inte att du alltid *ska*. Här är situationerna där agenter verkligen lyser:

![When to use AI Agents?](../../../translated_images/sv/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Öppna problem** — När stegen för att lösa ett problem inte kan förprogrammeras. Du behöver att LLM dynamiskt hittar vägen.
- **Flera steg i processen** — Uppgifter som kräver verktyg under flera omgångar, inte bara en uppslagning eller generering.
- **Förbättring över tid** — När du vill att systemet ska bli smartare baserat på användarfeedback eller miljösignaler.

Vi går djupare in på när (och när *inte*) man ska använda AI-agenter i lektionen **Bygga pålitliga AI-agenter** senare i kursen.

---

## Grundläggande om agentlösningar

### Agentutveckling

Det första du gör när du bygger en agent är att definiera *vad den kan göra* — dess verktyg, handlingar och beteenden.

I denna kurs använder vi **Azure AI Agent Service** som vår huvudsakliga plattform. Den stöder:

- Modeller från leverantörer som OpenAI, Mistral, och Meta (Llama)
- Licensierad data från leverantörer som Tripadvisor
- Standardiserade OpenAPI 3.0-verktygsdefinitioner

### Agentmönster

Du kommunicerar med LLM via prompts. Med agenter kan du inte alltid skapa varje prompt manuellt — agenten behöver agera över många steg. Där kommer **agentmönster** in. De är återanvändbara strategier för prompting och orkestrering av LLM på ett mer skalbart och pålitligt sätt.

Denna kurs är uppbyggd kring de vanligaste och mest användbara agentmönstren.

### Agentramverk

Agentramverk ger utvecklare färdiga mallar, verktyg och infrastruktur för att bygga agenter. De gör det enklare att:

- Koppla ihop verktyg och kapabiliteter
- Observera vad agenten gör (och felsöka när det går fel)
- Samarbeta mellan flera agenter

I denna kurs fokuserar vi på **Microsoft Agent Framework (MAF)** för att bygga produktionsklara agenter.

---

## Kodexempel

Redo att se det i praktiken? Här är kodexemplen för denna lektion:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Frågor?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att koppla ihop med andra lärande, delta i kontorstid och få dina frågor om AI-agenter besvarade av communityn.

---

## Föregående lektion

[Course Setup](../00-course-setup/README.md)

## Nästa lektion

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->