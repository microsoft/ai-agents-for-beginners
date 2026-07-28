[![Intro to AI Agents](../../../translated_images/nl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik op de afbeelding hierboven om de video voor deze les te bekijken)_

# Introductie tot AI Agents en Gebruikscases voor Agents

Welkom bij de **AI Agents voor Beginners** cursus! Deze cursus geeft je de basiskennis — en echte werkende code — om AI Agents vanaf nul te bouwen.

Kom even hallo zeggen in de <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — een plek vol studenten en AI-bouwers die graag vragen beantwoorden.

Voordat we aan het bouwen slaan, laten we eerst zeker weten dat we echt begrijpen wat een AI Agent *is* en wanneer het zinvol is er een te gebruiken.

---

## Introductie

Deze les behandelt:

- Wat AI Agents zijn, en de verschillende types die bestaan
- Voor welke taken AI Agents het beste geschikt zijn
- De kernbouwstenen die je gebruikt bij het ontwerpen van een Agent-oplossing

## Leerdoelen

Aan het einde van deze les zou je in staat moeten zijn om:

- Uitleggen wat een AI Agent is en hoe het verschilt van een gewone AI-oplossing
- Weten wanneer je een AI Agent moet inzetten (en wanneer niet)
- Een basaal ontwerp te schetsen voor een Agent-oplossing voor een probleem uit de praktijk

---

## Definiëren van AI Agents en Types AI Agents

### Wat zijn AI Agents?

Hier is een eenvoudige manier om erover na te denken:

> **AI Agents zijn systemen die Large Language Models (LLM's) daadwerkelijk *dingen laten doen* — door ze tools en kennis te geven om op de wereld te reageren, niet alleen te reageren op prompts.**

Laten we dat even nader bekijken:

- **Systeem** — Een AI Agent is niet slechts één ding. Het is een collectie van onderdelen die samenwerken. Elke agent heeft in de kern drie onderdelen:
  - **Omgeving** — De ruimte waarbinnen de agent werkt. Voor een reisboekingsagent is dit het boekingsplatform zelf.
  - **Sensoren** — Hoe de agent de huidige staat van zijn omgeving leest. Onze reisagent controleert bijvoorbeeld hotelbeschikbaarheid of vliegtarieven.
  - **Actuatoren** — Hoe de agent actie onderneemt. De reisagent kan een kamer boeken, een bevestiging sturen of een reservering annuleren.

![Wat Zijn AI Agents?](../../../translated_images/nl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agents bestonden al vóór LLM's, maar LLM's maken moderne agents zo krachtig. Ze kunnen natuurlijke taal begrijpen, redeneren over context, en een vage gebruikersvraag omzetten in een concreet actieplan.

- **Acties Uitvoeren** — Zonder een agent-systeem genereert een LLM alleen tekst. Binnen een agent-systeem kan de LLM daadwerkelijk stappen *uitvoeren* — zoals zoeken in een database, een API aanroepen, een bericht sturen.

- **Toegang tot Tools** — Welke tools de agent kan gebruiken hangt af van (1) de omgeving waarin het draait en (2) wat de ontwikkelaar ervoor heeft aangebracht. Een reisagent kan wel vluchten zoeken maar geen klantgegevens aanpassen — het draait om wat je verbindt.

- **Geheugen + Kennis** — Agents kunnen kortetermijngeheugen hebben (het huidige gesprek) en langetermijngeheugen (een klantenbestand, eerdere interacties). De reisagent "herinnert" zich misschien dat je raamplaatsen prefereert.

---

### De Verschillende Types AI Agents

Niet alle agents zijn op dezelfde manier gebouwd. Hier is een overzicht van de belangrijkste types, met een reisboekingsagent als lopend voorbeeld:

| **Type Agent** | **Wat Het Doet** | **Voorbeeld Reisagent** |
|---|---|---|
| **Eenvoudige Reflex Agents** | Volgt harde, vaste regels — geen geheugen, geen planning. | Ziet een klacht per e-mail → stuurt deze door naar klantenservice. Dat is alles. |
| **Model-Based Reflex Agents** | Houdt een intern model van de wereld bij en werkt dit bij als dingen veranderen. | Volgt historische vliegtarieven en markeert routes die plotseling duur zijn. |
| **Goal-Based Agents** | Heeft een doel voor ogen en bedenkt stap voor stap hoe dat te bereiken. | Boekt een volledige reis (vluchten, auto, hotel) van je huidige locatie naar je bestemming. |
| **Utility-Based Agents** | Vindt niet zomaar *een* oplossing — zoekt de *beste* door voor- en nadelen af te wegen. | Balanceert kosten versus gemak om de trip te vinden die het beste bij je voorkeuren past. |
| **Learning Agents** | Wordt beter door feedback te leren. | Past toekomstige boekingsaanbevelingen aan op basis van enquêteresultaten na trips. |
| **Hiërarchische Agents** | Een agent op hoog niveau deelt het werk op in subtaken en delegeert aan lagere agents. | Een verzoek 'reis annuleren' wordt opgesplitst in: vlucht annuleren, hotel annuleren, autohuur annuleren — elk uitgevoerd door een sub-agent. |
| **Multi-Agent Systemen (MAS)** | Meerdere onafhankelijke agents die samenwerken (of concurreren). | Samenwerkend: aparte agents voor hotels, vluchten en entertainment. Concurrerend: meerdere agents wedijveren om hotelkamers tegen de beste prijs te vullen. |

---

## Wanneer AI Agents Gebruiken

Alleen omdat je een AI Agent *kunt* gebruiken, betekent niet dat je dat altijd *moet*. Hier zijn situaties waarin agents echt uitblinken:

![Wanneer AI Agents gebruiken?](../../../translated_images/nl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Open-eindproblemen** — Wanneer de stappen om een probleem op te lossen niet vooraf geprogrammeerd kunnen worden. Je hebt de LLM nodig om het pad dynamisch uit te vinden.
- **Meerstapsprocessen** — Taken die het gebruik van tools over meerdere momenten vereisen, niet slechts één enkele opvraging of generatie.
- **Verbetering in de Tijd** — Wanneer je wilt dat het systeem slimmer wordt op basis van feedback van gebruikers of signalen uit de omgeving.

We gaan dieper in op wanneer (en wanneer *niet*) AI Agents te gebruiken in de les **Betrouwbare AI Agents Bouwen** later in de cursus.

---

## Basisprincipes van Agent-oplossingen

### Agentontwikkeling

Het eerste wat je doet bij het bouwen van een agent is definiëren *wat het kan doen* — zijn tools, acties en gedrag.

In deze cursus gebruiken we de **Microsoft Foundry Agent Service** als ons hoofdplatform. Het ondersteunt:

- Modellen van aanbieders als OpenAI, Mistral en Meta (Llama)
- Gelicentieerde data van aanbieders als Tripadvisor
- Gestandaardiseerde OpenAPI 3.0 tooldefinities

### Agentpatronen

Je communiceert met LLM's via prompts. Met agents kun je niet altijd elke prompt handmatig maken — de agent moet acties over meerdere stappen uitvoeren. Daarvoor bestaan **Agentpatronen**. Het zijn herbruikbare strategieën voor het prompten en aansturen van LLM's op een schaalbare, betrouwbare manier.

Deze cursus is opgezet rondom de meest voorkomende en nuttige agentpatronen.

### Agentframeworks

Agentframeworks bieden ontwikkelaars kant-en-klare sjablonen, tools en infrastructuur voor het bouwen van agents. Ze maken het makkelijker om:

- Tools en mogelijkheden aan te sluiten
- Te observeren wat de agent doet (en te debuggen als het misgaat)
- Samen te werken tussen meerdere agents

In deze cursus richten we ons op het **Microsoft Agent Framework (MAF)** voor het bouwen van productieklare agents.

---

## Code Voorbeelden

Klaar om het in actie te zien? Hier zijn de codevoorbeelden voor deze les:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Vragen?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om in contact te komen met andere studenten, kantooruren bij te wonen, en antwoorden te krijgen op je AI Agent vragen van de community.


---

## Agent Testen (Optioneel)

Zodra je geleerd hebt hoe agents te implementeren in [Les 16](../16-deploying-scalable-agents/README.md), kun je een snelle post-deploy gezondheidscontrole voor de `TravelAgent` van deze les toevoegen met de kant-en-klare catalogus [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Zie [`tests/README.md`](../tests/README.md) voor hoe je dit kunt uitvoeren.

---

## Vorige Les

[Cursus Setup](../00-course-setup/README.md)

## Volgende Les

[Agentframeworks Verkennen](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->