[![Intro to AI Agents](../../../translated_images/sv/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klicka på bilden ovan för att se videon för denna lektion)_

# Introduktion till AI-agenter och användningsfall för agenter

Välkommen till kursen **AI Agents for Beginners**! Den här kursen ger dig grundläggande kunskaper – och verklig fungerande kod – för att börja bygga AI-agenter från grunden.

Kom och säg hej i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — det är fullt av elever och AI-byggare som gärna svarar på frågor.

Innan vi börjar bygga, låt oss säkerställa att vi faktiskt förstår vad en AI-agent *är* och när det är meningsfullt att använda en.

---

## Introduktion

Den här lektionen täcker:

- Vad AI-agenter är, och de olika typer som finns
- Vilka typer av uppgifter AI-agenter är bäst lämpade för
- De grundläggande byggstenarna du använder när du designar en agentisk lösning

## Lärandemål

I slutet av denna lektion ska du kunna:

- Förklara vad en AI-agent är och hur den skiljer sig från en vanlig AI-lösning
- Veta när man ska använda en AI-agent (och när man inte ska)
- Skissa på en grundläggande agentisk lösningsdesign för ett verkligt problem

---

## Definition av AI-agenter och typer av AI-agenter

### Vad är AI-agenter?

Här är ett enkelt sätt att tänka på det:

> **AI-agenter är system som låter stora språkmodeller (LLM) faktiskt *göra saker* – genom att ge dem verktyg och kunskap för att agera på världen, inte bara svara på prompts.**

Låt oss bryta ner det lite:

- **System** — En AI-agent är inte bara en sak. Det är en samling delar som arbetar tillsammans. I grunden har varje agent tre delar:
  - **Miljö** — Den plats/utrymme agenten arbetar i. För en resebokningsagent är detta bokningsplattformen själv.
  - **Sensorer** — Hur agenten läser det aktuella tillståndet i sin miljö. Vår reseagent kan kolla hotell tillgänglighet eller flygpriser.
  - **Aktuatorer** — Hur agenten agerar. Resagenten kanske bokar ett rum, skickar en bekräftelse eller avbokar en reservation.

![What Are AI Agents?](../../../translated_images/sv/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Stora språkmodeller** — Agenter fanns redan innan LLM, men det är LLM som gör moderna agenter så kraftfulla. De kan förstå naturligt språk, resonera kring kontext och omvandla en vag användarförfrågan till en konkret handlingsplan.

- **Utför handlingar** — Utan ett agentsystem genererar en LLM bara text. Inom ett agentsystem kan LLM faktiskt *utföra* steg – söka i en databas, anropa ett API, skicka ett meddelande.

- **Tillgång till verktyg** — Vilka verktyg agenten kan använda beror på (1) miljön den körs i och (2) vad utvecklaren valt att koppla in. En reseagent kan kanske söka flyg men inte redigera kundregister – det handlar om vad du kopplar upp.

- **Minne + Kunskap** — Agenter kan ha korttidsminne (nuvarande konversation) och långtidsminne (en kunddatabas, tidigare interaktioner). Resagenten kan "komma ihåg" att du föredrar gångplats.

---

### Olika typer av AI-agenter

Alla agenter är inte byggda på samma sätt. Här är en översikt över huvudtyperna, med resebokningsagenten som exempel:

| **Agenttyp** | **Vad den gör** | **Exempel: reseagent** |
|---|---|---|
| **Enkla reflexagenter** | Följda hårdkodade regler – inget minne, ingen planering. | Ser ett klagomails → vidarebefordrar det till kundservice. Det är allt. |
| **Modellbaserade reflexagenter** | Behåller en intern världmodell och uppdaterar den när saker förändras. | Följer historiska flygpriser och markerar rutter som plötsligt blivit dyra. |
| **Målbaserade agenter** | Har ett mål i sikte och räknar ut hur det nås steg för steg. | Boka en full resa (flyg, bil, hotell) från din nuvarande plats till destinationen. |
| **Nyttobaserade agenter** | Hittar inte bara *en* lösning – hittar *den bästa* genom att väga för- och nackdelar. | Väger kostnad mot bekvämlighet för att hitta resan som passar dina preferenser bäst. |
| **Lärande agenter** | Blir bättre över tid genom att lära från återkoppling. | Justerar framtida bokningsrekommendationer baserat på enkätsvar efter resan. |
| **Hierarkiska agenter** | En högre nivå-agent delar upp arbete i deluppgifter och delegerar till lägre nivå-agenter. | En "avboka resa"-begäran delas upp i: avboka flyg, avboka hotell, avboka hyrbil – varje hanteras av en subagent. |
| **Multi-Agent System (MAS)** | Flera oberoende agenter som arbetar tillsammans (eller tävlar). | Samarbetande: separata agenter hanterar hotell, flyg och underhållning. Konkurrerande: flera agenter tävlar om att fylla hotellrum till bästa pris. |

---

## När ska man använda AI-agenter

Bara för att du *kan* använda en AI-agent betyder det inte att du alltid *ska*. Här är situationerna där agenter verkligen glänser:

![When to use AI Agents?](../../../translated_images/sv/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Öppna problem** — När stegen för att lösa ett problem inte kan förprogrammeras. Du behöver att LLM löser vägen dynamiskt.
- **Flera steg i processen** — Uppgifter som kräver verktygsanvändning över flera steg, inte bara en enkel uppslagning eller generering.
- **Förbättring över tid** — När du vill att systemet ska bli smartare baserat på användaråterkoppling eller miljösignaler.

Vi går djupare in på när (och när *inte*) man ska använda AI-agenter i lektionen **Building Trustworthy AI Agents** senare i kursen.

---

## Grunderna i agentiska lösningar

### Agentutveckling

Det första du gör när du bygger en agent är att definiera *vad den kan göra* – dess verktyg, åtgärder och beteenden.

I denna kurs använder vi **Azure AI Agent Service** som vår huvudplattform. Den stödjer:

- Öppna modeller som OpenAI, Mistral och Llama
- Licensierade data från leverantörer som Tripadvisor
- Standardiserade OpenAPI 3.0-verktygsdefinitioner

### Agentiska mönster

Du kommunicerar med LLM via prompts. Med agenter kan du inte alltid handgöra varje prompt manuellt – agenten måste kunna agera över många steg. Där kommer **agentiska mönster** in. De är återanvändbara strategier för promptning och orkestrering av LLM på ett mer skalbart och pålitligt sätt.

Denna kurs är uppbyggd kring de vanligaste och mest användbara agentiska mönstren.

### Agentiska ramverk

Agentiska ramverk ger utvecklare färdiga mallar, verktyg och infrastruktur för att bygga agenter. De gör det lättare att:

- Koppla upp verktyg och funktioner
- Observera vad agenten gör (och debugga när något går fel)
- Samarbeta över flera agenter

I denna kurs fokuserar vi på **Microsoft Agent Framework (MAF)** för att bygga produktionsklara agenter.

---

## Kodexempel

Redo att se det i praktiken? Här är kodexemplen för denna lektion:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Frågor?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att koppla upp dig med andra elever, delta i kontorstider och få svar på dina AI-agentfrågor från communityn.

---

## Föregående lektion

[Course Setup](../00-course-setup/README.md)

## Nästa lektion

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell manuell översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->