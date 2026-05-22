[![Intro to AI Agents](../../../translated_images/nl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik op de afbeelding hierboven om de video voor deze les te bekijken)_

# Introductie tot AI Agents en gebruikssituaties voor Agents

Welkom bij de cursus **AI Agents voor Beginners**! Deze cursus geeft je de basiskennis — en werkende code — om AI Agents vanaf nul te bouwen.

Zeg hoi in de <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — deze zit vol met leerlingen en AI-bouwers die graag vragen beantwoorden.

Voordat we beginnen met bouwen, laten we eerst begrijpen wat een AI Agent *is* en wanneer het zinvol is er een te gebruiken.

---

## Introductie

Deze les behandelt:

- Wat AI Agents zijn, en de verschillende typen die bestaan
- Voor welke soorten taken AI Agents het beste geschikt zijn
- De kernbouwstenen die je zult gebruiken bij het ontwerpen van een agent-gebaseerde oplossing

## Leerdoelen

Aan het einde van deze les kun je:

- Uitleggen wat een AI Agent is en hoe deze verschilt van een reguliere AI-oplossing
- Weten wanneer je een AI Agent moet inzetten (en wanneer niet)
- Een basisontwerp schetsen van een agent-gebaseerde oplossing voor een probleem uit de praktijk

---

## Definiëren van AI Agents en typen AI Agents

### Wat zijn AI Agents?

Hier is een eenvoudige manier om erover na te denken:

> **AI Agents zijn systemen die Large Language Models (LLM's) daadwerkelijk *dingen laten doen* — door hen gereedschappen en kennis te geven om op de wereld te handelen, en niet alleen te reageren op prompts.**

Laten we dat wat nader bekijken:

- **Systeem** — Een AI Agent is niet zomaar één ding. Het is een verzameling onderdelen die samenwerken. In de kern heeft elke agent drie onderdelen:
  - **Omgeving** — De ruimte waarin de agent werkt. Voor een reisboekingsagent is dit het boekingsplatform zelf.
  - **Sensoren** — Hoe de agent de huidige staat van zijn omgeving leest. Onze reisagent controleert bijvoorbeeld hotelbeschikbaarheid of vluchtprijzen.
  - **Actuatoren** — Hoe de agent actie onderneemt. De reisagent boekt misschien een kamer, stuurt een bevestiging of annuleert een reservering.

![What Are AI Agents?](../../../translated_images/nl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agents bestonden al voor LLM's, maar LLM's maken moderne agents zo krachtig. Ze begrijpen natuurlijke taal, redeneren over context, en zetten een vage gebruikersvraag om in een concreet actieplan.

- **Acties uitvoeren** — Zonder een agentsysteem genereert een LLM alleen tekst. Binnen een agentsysteem kan de LLM daadwerkelijk *stappen uitvoeren* — een database doorzoeken, een API aanroepen, een bericht versturen.

- **Toegang tot gereedschappen** — Welke gereedschappen de agent kan gebruiken hangt af van (1) de omgeving waarin hij draait en (2) wat de ontwikkelaar hem heeft gegeven. Een reisagent kan vluchten zoeken maar misschien geen klantgegevens wijzigen — het hangt ervan af wat je koppelt.

- **Geheugen + Kennis** — Agents kunnen een kortetermijngeheugen hebben (het huidige gesprek) en langetermijngeheugen (een klantenbestand, eerdere interacties). De reisagent "herinnert" zich bijvoorbeeld dat je de voorkeur geeft aan een stoel bij het raam.

---

### De verschillende typen AI Agents

Niet alle agents zijn hetzelfde gebouwd. Hier is een indeling van de belangrijkste types, met een reisboekingsagent als voorbeeld:

| **Type Agent** | **Wat het doet** | **Voorbeeld Reisagent** |
|---|---|---|
| **Eenvoudige reflexagents** | Volgen harde regels — geen geheugen, geen planning. | Ziet een klacht-email → stuurt door naar klantenservice. Dat is het. |
| **Modelgebaseerde reflexagents** | Houdt een intern model van de wereld bij en werkt dit bij als dingen veranderen. | Houdt historische vluchtprijzen bij en markeert routes die plots duur zijn. |
| **Doelgerichte agents** | Heeft een doel en bedenkt stap voor stap hoe dat te bereiken. | Boekt een hele reis (vluchten, auto, hotel) vanaf je huidige locatie naar je bestemming. |
| **Nut-gebaseerde agents** | Zoekt niet zomaar *een* oplossing — maar de *beste* door afwegingen te maken. | Weegt kosten tegen gemak om de reis te vinden die het beste aansluit op je voorkeuren. |
| **Leeragents** | Wordt beter in de loop van de tijd door te leren van feedback. | Past toekomstige boekingsaanbevelingen aan op basis van enquêteresultaten na de reis. |
| **Hiërarchische agents** | Een agent op hoog niveau verdeelt het werk in deelopdrachten en geeft die door aan lagere agents. | Een verzoek "reis annuleren" wordt opgesplitst in: vlucht annuleren, hotel annuleren, autohuur annuleren — elk afgehandeld door een deelagent. |
| **Multi-agent Systemen (MAS)** | Meerdere onafhankelijke agents werken samen (of concurreren). | Samenwerkend: aparte agents regelen hotels, vluchten en entertainment. Competitief: meerdere agents concurreren om hotelkamers tegen de beste prijs te vullen. |

---

## Wanneer AI Agents gebruiken

Alleen omdat je een AI Agent *kan* gebruiken, betekent dat niet altijd dat je dat ook *moet* doen. Dit zijn de situaties waarin agents echt uitblinken:

![When to use AI Agents?](../../../translated_images/nl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Open-eind problemen** — Wanneer de stappen om een probleem op te lossen niet vooraf geprogrammeerd kunnen worden. Je hebt de LLM nodig om het pad dynamisch uit te zoeken.
- **Meer-staps processen** — Taken die vereisen dat je tools meerdere keren achter elkaar gebruikt, niet slechts één enkele opvraging of generatie.
- **Verbetering in de tijd** — Wanneer je wilt dat het systeem slimmer wordt op basis van gebruikersfeedback of omgevingssignalen.

We gaan dieper in op wanneer (en wanneer *niet*) AI Agents te gebruiken in de les **Betrouwbare AI Agents bouwen**, later in de cursus.

---

## Basisprincipes van agent-gebaseerde oplossingen

### Agentontwikkeling

Het eerste wat je doet bij het bouwen van een agent is definiëren *wat deze kan doen* — zijn gereedschappen, acties en gedrag.

In deze cursus gebruiken we de **Azure AI Agent Service** als ons hoofdplatform. Deze ondersteunt:

- Modellen van aanbieders zoals OpenAI, Mistral en Meta (Llama)
- Gelicentieerde data van aanbieders zoals Tripadvisor
- Gestandaardiseerde OpenAPI 3.0 tooldefinities

### Agent-gebaseerde patronen

Je communiceert met LLM's via prompts. Bij agents kun je niet altijd elke prompt handmatig maken — de agent moet acties kunnen ondernemen over meerdere stappen. Daarom zijn er **agent-gebaseerde patronen**. Dit zijn herbruikbare strategieën om LLM's op een schaalbaardere en betrouwbaardere manier aan te sturen en te orkestreren.

Deze cursus is opgebouwd rond de meest voorkomende en nuttige agent-gebaseerde patronen.

### Agent-Frameworks

Agent-Frameworks bieden ontwikkelaars kant-en-klare sjablonen, gereedschappen en infrastructuur om agents te bouwen. Ze maken het eenvoudiger om:

- Gereedschappen en functies te koppelen
- Te observeren wat de agent doet (en te debuggen als iets misgaat)
- Samen te werken tussen meerdere agents

In deze cursus richten we ons op het **Microsoft Agent Framework (MAF)** voor het bouwen van productieklare agents.

---

## Code Voorbeelden

Klaar om het in actie te zien? Hier zijn de codevoorbeelden voor deze les:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Vragen?

Doe mee met de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om in contact te komen met andere leerlingen, aanwezig te zijn bij spreekuren, en je AI Agent-vragen door de community beantwoord te krijgen.

---

## Vorige les

[Cursus Setup](../00-course-setup/README.md)

## Volgende les

[Agent Frameworks verkennen](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->