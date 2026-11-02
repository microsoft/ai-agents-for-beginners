[![Intro till AI-agenter](../../../translated_images/sv/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klicka på bilden ovan för att titta på videon för denna lektion)_

# Introduktion till AI-agenter och agentanvändningsfall

Välkommen till kursen **AI Agents for Beginners**! Denna kurs ger dig grundläggande kunskap — och riktig fungerande kod — för att börja bygga AI-agenter från grunden.

Kom och säg hej i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — det är fullt av elever och AI-byggare som gärna svarar på frågor.

Innan vi börjar bygga, låt oss försäkra oss om att vi faktiskt förstår vad en AI-agent *är* och när det är meningsfullt att använda en.

---

## Introduktion

Denna lektion behandlar:

- Vad AI-agenter är och de olika typer som finns
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

> **AI-agenter är system som låter stora språkmodeller (LLMs) faktiskt *göra saker* — genom att ge dem verktyg och kunskap för att agera i världen, inte bara svara på frågor.**

Låt oss bryta ner det lite:

- **System** — En AI-agent är inte bara en sak. Det är en samling delar som arbetar tillsammans. I kärnan har varje agent tre delar:
  - **Miljö** — Den plats agenten arbetar i. För en resebokningsagent skulle detta vara bokningsplattformen själv.
  - **Sensorer** — Hur agenten läser av det aktuella tillståndet i sin miljö. Vår reseagent kan kolla hotell tillgänglighet eller flygpriser.
  - **Aktuatorer** — Hur agenten agerar. Resagenten kan boka ett rum, skicka en bekräftelse eller avboka en reservation.

![Vad är AI-agenter?](../../../translated_images/sv/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Stora språkmodeller** — Agenter fanns innan LLMs, men LLMs är det som gör moderna agenter så kraftfulla. De kan förstå naturligt språk, resonera om kontext, och omvandla en vag användarförfrågan till en konkret handlingsplan.

- **Utföra åtgärder** — Utan ett agentsystem genererar en LLM bara text. Inom ett agentsystem kan LLM verkligen *utföra* steg — söka i databas, anropa API, skicka ett meddelande.

- **Tillgång till verktyg** — Vilka verktyg agenten kan använda beror på (1) miljön den körs i och (2) vad utvecklaren valt att ge den. En reseagent kan söka flyg men inte redigera kundregister — det handlar om vad du kopplar in.

- **Minne + Kunskap** — Agenter kan ha korttidsminne (det aktuella samtalet) och långtidsminne (en kunddatabas, tidigare interaktioner). Resagenten kan "komma ihåg" att du föredrar fönsterplatser.

---

### De olika typerna av AI-agenter

Inte alla agenter är byggda likadant. Här är en sammanställning av de huvudsakliga typerna, med en resebokningsagent som exempel:

| **Agenttyp** | **Vad den gör** | **Exempel med reseagent** |
|---|---|---|
| **Simple Reflex Agents** | Följer hårdkodade regler — inget minne, ingen planering. | Ser ett klagomail → vidarebefordrar det till kundtjänst. Det är allt. |
| **Model-Based Reflex Agents** | Har en intern modell av världen och uppdaterar den när saker förändras. | Spårar historiska flygpriser och flaggar rutter som plötsligt blivit dyra. |
| **Goal-Based Agents** | Har ett mål i sikte och räknar ut hur det nås steg för steg. | Bokar en komplett resa (flyg, bil, hotell) från din nuvarande plats till destinationen. |
| **Utility-Based Agents** | Hittar inte bara *en* lösning — hittar *den bästa* genom att väga för- och nackdelar. | Väger kostnad mot bekvämlighet för att hitta resan som bäst matchar dina preferenser. |
| **Learning Agents** | Blir bättre med tiden genom att lära av feedback. | Justerar framtida bokningsförslag baserat på enkätsvar efter resan. |
| **Hierarchical Agents** | En agent på hög nivå delar upp arbetet i deluppgifter och delegerar till underordnade agenter. | En begäran om "avboka resa" delas upp i: avboka flyg, avboka hotell, avboka hyrbil — var och en hanteras av en underagent. |
| **Multi-Agent Systems (MAS)** | Flera oberoende agenter som arbetar tillsammans (eller konkurrerar). | Samarbetande: separata agenter hanterar hotell, flyg och underhållning. Konkurrerande: flera agenter tävlar om att fylla hotellrum till bäst pris. |

---

## När ska man använda AI-agenter

Bara för att du *kan* använda en AI-agent betyder det inte att du alltid *ska*. Här är situationer där agenter verkligen utmärker sig:

![När ska du använda AI-agenter?](../../../translated_images/sv/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Öppna problem** — När stegen för att lösa ett problem inte kan förprogrammeras. Du behöver att LLM dynamiskt listar ut vägen.
- **Flera steg-processer** — Uppgifter som kräver att använda verktyg över flera steg, inte bara en enkel sökning eller generering.
- **Förbättring över tid** — När du vill att systemet ska bli smartare baserat på användarfeedback eller miljösignaler.

Vi går djupare in på när (och när *inte*) man ska använda AI-agenter i lektionen **Bygga pålitliga AI-agenter** senare i kursen.

---

## Grunderna i agentlösningar

### Agentutveckling

Det första du gör när du bygger en agent är att definiera *vad den kan göra* — dess verktyg, handlingar och beteenden.

I denna kurs använder vi **Microsoft Foundry Agent Service** som huvudplattform. Den stödjer:

- Modeller från leverantörer som OpenAI, Mistral och Meta (Llama)
- Licensierad data från leverantörer som Tripadvisor
- Standardiserade OpenAPI 3.0-verktygsdefinitioner

### Agentiska mönster

Du kommunicerar med LLMs via prompts. Med agenter kan du inte alltid skapa varje prompt manuellt — agenten behöver agera över många steg. Där kommer **agentiska mönster** in. Det är återanvändbara strategier för att prompta och orkestrera LLMs på ett mer skalbart och pålitligt sätt.

Denna kurs är strukturerad runt de vanligaste och mest användbara agentiska mönstren.

### Agentiska ramverk

Agentiska ramverk ger utvecklare färdiga mallar, verktyg och infrastruktur för att bygga agenter. De gör det enklare att:

- Koppla upp verktyg och funktioner
- Observera vad agenten gör (och felsöka när det går fel)
- Samarbeta över flera agenter

I denna kurs fokuserar vi på **Microsoft Agent Framework (MAF)** för att bygga agentklara för produktion.

---

## Kodexempel

Redo att se det i aktion? Här är kodexemplen för denna lektion:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Har du frågor?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att koppla upp dig med andra elever, delta i kontorstid, och få dina AI-agentfrågor besvarade av communityn.


---

## Snabbtest av denna agent (frivilligt)

När du lärt dig att distribuera agenter i [Lektion 16](../16-deploying-scalable-agents/README.md), kan du lägga till en snabb efter-distribution hälsokontroll för denna lektions `TravelAgent` med den färdiga katalogen [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Se [`tests/README.md`](../tests/README.md) för hur du kör den.

---

## Föregående lektion

[Kursinställning](../00-course-setup/README.md)

## Nästa lektion

[Utforska agentiska ramverk](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->