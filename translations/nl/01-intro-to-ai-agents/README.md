[![Introductie tot AI-Agenten](../../../translated_images/nl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Introductie tot AI-Agenten en Gebruikscasussen van Agenten

Welkom bij de cursus **AI-Agenten voor Beginners**! Deze cursus geeft je de basiskennis — en echte werkende code — om AI-Agenten vanaf nul te bouwen.

Kom hallo zeggen in de <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — deze zit vol met leerders en AI-bouwers die graag vragen beantwoorden.

Voordat we aan de slag gaan met bouwen, laten we eerst zeker weten dat we begrijpen wat een AI-Agent *is* en wanneer het zinvol is er een te gebruiken.

---

## Introductie

Deze les behandelt:

- Wat AI-Agenten zijn, en de verschillende typen die bestaan
- Voor welke soorten taken AI-Agenten het meest geschikt zijn
- De kernbouwstenen die je gebruikt bij het ontwerpen van een Agent-oplossing

## Leerdoelen

Aan het einde van deze les moet je in staat zijn:

- Uit te leggen wat een AI-Agent is en hoe het verschilt van een gewone AI-oplossing
- Te weten wanneer je een AI-Agent moet inzetten (en wanneer niet)
- Een basisontwerp te schetsen voor een Agent-oplossing voor een probleem uit de praktijk

---

## Definiëren van AI-Agenten en Typen AI-Agenten

### Wat zijn AI-Agenten?

Hier is een eenvoudige manier om erover na te denken:

> **AI-Agenten zijn systemen die Large Language Models (LLM's) echt *laten handelen* — door ze tools en kennis te geven om op de wereld in te grijpen, niet alleen om op prompts te reageren.**

Laten we dat wat verder uitleggen:

- **Systeem** — Een AI-Agent is niet zomaar één ding. Het is een verzameling onderdelen die samenwerken. In de kern heeft elke agent drie onderdelen:
  - **Omgeving** — De ruimte waarin de agent werkt. Voor een reisboekingsagent zou dat het boekingsplatform zelf zijn.
  - **Sensoren** — Hoe de agent de huidige staat van zijn omgeving leest. Onze reisagent kan bijvoorbeeld hotelbeschikbaarheid of vluchtprijzen checken.
  - **Actuatoren** — Hoe de agent actie onderneemt. De reisagent kan een kamer boeken, een bevestiging sturen, of een reservering annuleren.

![Wat Zijn AI-Agenten?](../../../translated_images/nl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agenten bestonden al vóór LLM's, maar LLM's maken moderne agenten zo krachtig. Zij kunnen natuurlijke taal begrijpen, context doorgronden en een vage gebruikersvraag omzetten in een concreet actieplan.

- **Acties Uitvoeren** — Zonder een agentsysteem genereert een LLM alleen tekst. Binnen een agentsysteem kan de LLM daadwerkelijk *stappen uitvoeren* — een database doorzoeken, een API aanroepen, een bericht sturen.

- **Toegang tot Tools** — Welke tools de agent kan gebruiken, hangt af van (1) de omgeving waarin hij draait en (2) wat de ontwikkelaar hem geeft. Een reisagent kan bijvoorbeeld vluchtzoekopdrachten uitvoeren maar geen klantgegevens bewerken — het hangt allemaal af van wat je aansluit.

- **Geheugen + Kennis** — Agenten kunnen kortetermijngeheugen hebben (het huidige gesprek) en langetermijngeheugen (een klantenbestand, eerdere interacties). De reisagent kan zich "herinneren" dat je bij voorkeur een raamstoel kiest.

---

### De Verschillende Typen AI-Agenten

Niet alle agenten zijn op dezelfde manier gebouwd. Hier is een overzicht van de belangrijkste typen, met een reisboekingsagent als voorbeeld:

| **Agentyype** | **Wat het doet** | **Reisagentvoorbeeld** |
|---|---|---|
| **Eenvoudige Reflexagenten** | Volgen vaste regels — geen geheugen, geen planning. | Ziet een klachtmail → stuurt deze door naar klantenservice. Dat is alles. |
| **Modelgebaseerde Reflexagenten** | Houdt een intern model van de wereld bij en werkt dit bij als dingen veranderen. | Houdt historische vluchtprijzen bij en markeert routes die plotseling duur zijn. |
| **Doelgebaseerde Agenten** | Heeft een doel voor ogen en bedenkt stap voor stap hoe dat te bereiken. | Boekt een volledige reis (vluchten, auto, hotel) vanaf jouw huidige locatie om je naar de bestemming te brengen. |
| **Nutgebaseerde Agenten** | Zoekt niet zomaar een *oplossing*, maar de *beste* door afwegingen te maken. | Weegt kosten tegen gemak af om de reis te vinden die het beste bij je voorkeuren past. |
| **Leerende Agenten** | Worden beter in de tijd door te leren van feedback. | Past toekomstige boekingsaanbevelingen aan op basis van enquêteresultaten na de reis. |
| **Hiërarchische Agenten** | Een topniveau-agent verdeelt taken in subtaken en delegeert aan lagere niveau agenten. | Een "annuleer reis"-verzoek wordt opgesplitst in: vlucht annuleren, hotel annuleren, auto annuleren — elk afgehandeld door een sub-agent. |
| **Multi-Agent Systemen (MAS)** | Meerdere onafhankelijke agenten werken samen (of concurreren). | Samenwerkend: verschillende agenten verzorgen hotels, vluchten en entertainment. Concurrerend: meerdere agenten concurreren om hotelkamers tegen de beste prijs te vullen. |

---

## Wanneer AI-Agenten gebruiken

Alleen omdat je een AI-Agent *kunt* gebruiken, betekent niet dat je dat altijd *moet* doen. Hier zijn situaties waarin agenten echt uitblinken:

![Wanneer AI-Agenten gebruiken?](../../../translated_images/nl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Open Einde Problemen** — Wanneer de stappen om een probleem op te lossen niet vooraf geprogrammeerd kunnen worden. De LLM moet het pad dynamisch uitzoeken.
- **Meerdere Stappen Processen** — Taken die gereedschappen over meerdere beurten vereisen, niet slechts één enkele opzoeking of generatie.
- **Verbetering in de Tijd** — Wanneer je wilt dat het systeem slimmer wordt op basis van gebruikersfeedback of signalen uit de omgeving.

We gaan later in de cursus dieper in op wanneer (en wanneer juist *niet*) AI-Agenten te gebruiken in de les **Betrouwbare AI-Agenten Bouwen**.

---

## Basisprincipes van Agentoplossingen

### Agentontwikkeling

Het eerste wat je doet bij het bouwen van een agent is definiëren *wat hij kan* — de tools, acties en gedragingen.

In deze cursus gebruiken we de **Azure AI Agent Service** als ons platform. Deze ondersteunt:

- Open modellen zoals OpenAI, Mistral en Llama
- Gelicentieerde data van aanbieders zoals Tripadvisor
- Gestandaardiseerde OpenAPI 3.0 tooldefinities

### Agentpatronen

Je communiceert met LLM's via prompts. Bij agenten kun je niet altijd elke prompt handmatig samenstellen — de agent moet over meerdere stappen actie ondernemen. Daar komen **Agentpatronen** om de hoek kijken. Dat zijn herbruikbare strategieën om LLM's op een schaalbare en betrouwbare manier aan te sturen en te coördineren.

Deze cursus is opgebouwd rond de meest voorkomende en nuttige agentpatronen.

### Agentframeworks

Agentframeworks bieden ontwikkelaars kant-en-klare sjablonen, tools en infrastructuur om agenten te bouwen. Ze maken het makkelijker om:

- Tools en mogelijkheden aan te sluiten
- Te observeren wat de agent doet (en te debuggen als het misgaat)
- Samen te werken tussen meerdere agenten

In deze cursus richten we ons op het **Microsoft Agent Framework (MAF)** voor het bouwen van productieklare agenten.

---

## Codevoorbeelden

Klaar om het in actie te zien? Hier zijn de codevoorbeelden voor deze les:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Vragen?

Sluit je aan bij de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om in contact te komen met andere leerders, bij spreekuren te zijn, en je AI-Agent vragen te laten beantwoorden door de community.

---

## Vorige Les

[Cursus Setup](../00-course-setup/README.md)

## Volgende Les

[Agentframeworks Verkennen](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Terwijl we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->