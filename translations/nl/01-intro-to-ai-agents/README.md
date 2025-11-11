<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cdd28bc00816d2773bb2b5968d782abc",
  "translation_date": "2025-11-11T11:24:45+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "nl"
}
-->
[![Intro to AI Agents](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.nl.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Introductie tot AI Agents en Toepassingsmogelijkheden

Welkom bij de cursus "AI Agents voor Beginners"! Deze cursus biedt fundamentele kennis en praktische voorbeelden voor het bouwen van AI Agents.

Word lid van de <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> om andere cursisten en AI Agent-bouwers te ontmoeten en stel al je vragen over deze cursus.

Om deze cursus te starten, beginnen we met een beter begrip van wat AI Agents zijn en hoe we ze kunnen gebruiken in de applicaties en workflows die we bouwen.

## Introductie

Deze les behandelt:

- Wat zijn AI Agents en wat zijn de verschillende soorten agents?
- Welke toepassingen zijn het meest geschikt voor AI Agents en hoe kunnen ze ons helpen?
- Wat zijn enkele van de basisbouwstenen bij het ontwerpen van Agent-oplossingen?

## Leerdoelen
Na het voltooien van deze les zou je in staat moeten zijn om:

- Begrip te hebben van AI Agent-concepten en hoe ze verschillen van andere AI-oplossingen.
- AI Agents efficiënt toe te passen.
- Agent-oplossingen productief te ontwerpen voor zowel gebruikers als klanten.

## Definitie van AI Agents en Soorten AI Agents

### Wat zijn AI Agents?

AI Agents zijn **systemen** die **Large Language Models (LLMs)** in staat stellen **acties uit te voeren** door hun mogelijkheden uit te breiden met **toegang tot tools** en **kennis**.

Laten we deze definitie in kleinere delen opsplitsen:

- **Systeem** - Het is belangrijk om agents niet te zien als slechts één enkel onderdeel, maar als een systeem van vele componenten. Op het basale niveau bestaan de componenten van een AI Agent uit:
  - **Omgeving** - De gedefinieerde ruimte waarin de AI Agent opereert. Bijvoorbeeld, als we een reisboekings-AI Agent hadden, zou de omgeving het reisboekingssysteem kunnen zijn dat de AI Agent gebruikt om taken uit te voeren.
  - **Sensoren** - Omgevingen bevatten informatie en geven feedback. AI Agents gebruiken sensoren om deze informatie over de huidige staat van de omgeving te verzamelen en te interpreteren. In het voorbeeld van de reisboekingsagent kan het reisboekingssysteem informatie geven zoals hotelbeschikbaarheid of vluchtprijzen.
  - **Actuatoren** - Zodra de AI Agent de huidige staat van de omgeving ontvangt, bepaalt de agent welke actie moet worden uitgevoerd om de omgeving te veranderen. Voor de reisboekingsagent kan dit bijvoorbeeld het boeken van een beschikbare kamer voor de gebruiker zijn.

![Wat zijn AI Agents?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.nl.png)

**Large Language Models** - Het concept van agents bestond al vóór de creatie van LLMs. Het voordeel van het bouwen van AI Agents met LLMs is hun vermogen om menselijke taal en data te interpreteren. Dit vermogen stelt LLMs in staat om omgevingsinformatie te interpreteren en een plan te definiëren om de omgeving te veranderen.

**Acties Uitvoeren** - Buiten AI Agent-systemen zijn LLMs beperkt tot situaties waarin de actie het genereren van inhoud of informatie is op basis van een gebruikersprompt. Binnen AI Agent-systemen kunnen LLMs taken uitvoeren door de gebruikersvraag te interpreteren en gebruik te maken van tools die beschikbaar zijn in hun omgeving.

**Toegang tot Tools** - Welke tools de LLM tot zijn beschikking heeft, wordt bepaald door 1) de omgeving waarin het opereert en 2) de ontwikkelaar van de AI Agent. In ons reisagentvoorbeeld zijn de tools van de agent beperkt tot de functies die beschikbaar zijn in het boekingssysteem, en/of de ontwikkelaar kan de toegang van de agent tot tools zoals vluchten beperken.

**Geheugen + Kennis** - Geheugen kan kortetermijn zijn in de context van het gesprek tussen de gebruiker en de agent. Op de lange termijn, buiten de informatie die door de omgeving wordt verstrekt, kunnen AI Agents ook kennis ophalen uit andere systemen, diensten, tools en zelfs andere agents. In het reisagentvoorbeeld kan deze kennis informatie zijn over de reisvoorkeuren van de gebruiker die in een klantendatabase zijn opgeslagen.

### De verschillende soorten agents

Nu we een algemene definitie van AI Agents hebben, laten we eens kijken naar enkele specifieke soorten agents en hoe ze zouden worden toegepast op een reisboekings-AI Agent.

| **Type Agent**                | **Beschrijving**                                                                                                                       | **Voorbeeld**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Eenvoudige Reflex Agents**  | Voeren directe acties uit op basis van vooraf gedefinieerde regels.                                                                     | Reisagent interpreteert de context van de e-mail en stuurt reisgerelateerde klachten door naar de klantenservice.                                                                                                               |
| **Modelgebaseerde Reflex Agents** | Voeren acties uit op basis van een model van de wereld en veranderingen in dat model.                                                  | Reisagent geeft prioriteit aan routes met significante prijswijzigingen op basis van toegang tot historische prijsgegevens.                                                                                                     |
| **Doelgerichte Agents**       | Maken plannen om specifieke doelen te bereiken door het doel te interpreteren en acties te bepalen om het te bereiken.                 | Reisagent boekt een reis door noodzakelijke reisarrangementen (auto, openbaar vervoer, vluchten) van de huidige locatie naar de bestemming te bepalen.                                                                          |
| **Nutgerichte Agents**        | Overwegen voorkeuren en wegen afwegingen numeriek af om te bepalen hoe doelen te bereiken.                                              | Reisagent maximaliseert nut door gemak versus kosten af te wegen bij het boeken van reizen.                                                                                                                                     |
| **Lerende Agents**            | Verbeteren in de loop van de tijd door te reageren op feedback en acties dienovereenkomstig aan te passen.                                                                   | Reisagent verbetert door gebruik te maken van klantfeedback uit post-reis enquêtes om aanpassingen te maken voor toekomstige boekingen.                                                                                        |
| **Hiërarchische Agents**      | Bevatten meerdere agents in een gelaagd systeem, waarbij hogere agents taken opdelen in subtaken voor lagere agents om te voltooien.    | Reisagent annuleert een reis door de taak op te splitsen in subtaken (bijvoorbeeld specifieke boekingen annuleren) en lagere agents deze te laten uitvoeren, die vervolgens rapporteren aan de hogere agent.                      |
| **Multi-Agent Systemen (MAS)** | Agents voltooien taken onafhankelijk, hetzij coöperatief of competitief.                                                               | Coöperatief: Meerdere agents boeken specifieke reisservices zoals hotels, vluchten en entertainment. Competitief: Meerdere agents beheren en concurreren over een gedeelde hotelboekingskalender om klanten in het hotel te boeken. |

## Wanneer AI Agents te gebruiken

In de eerdere sectie hebben we de reisagent-toepassing gebruikt om uit te leggen hoe de verschillende soorten agents kunnen worden gebruikt in verschillende scenario's van reisboekingen. We zullen deze toepassing gedurende de cursus blijven gebruiken.

Laten we eens kijken naar de soorten toepassingen waarvoor AI Agents het meest geschikt zijn:

![Wanneer AI Agents te gebruiken?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.nl.png)

- **Open-eindige problemen** - waarbij de LLM de benodigde stappen bepaalt om een taak te voltooien, omdat dit niet altijd hardcoded kan worden in een workflow.
- **Meerstapsprocessen** - taken die een bepaalde mate van complexiteit vereisen waarbij de AI Agent tools of informatie over meerdere stappen moet gebruiken in plaats van eenmalige gegevensopvraging.  
- **Verbetering in de tijd** - taken waarbij de agent in de loop van de tijd kan verbeteren door feedback te ontvangen van zijn omgeving of gebruikers om betere resultaten te leveren.

We behandelen meer overwegingen voor het gebruik van AI Agents in de les over het bouwen van betrouwbare AI Agents.

## Basisprincipes van Agent-oplossingen

### Ontwikkeling van Agents

De eerste stap bij het ontwerpen van een AI Agent-systeem is het definiëren van de tools, acties en gedragingen. In deze cursus richten we ons op het gebruik van de **Azure AI Agent Service** om onze Agents te definiëren. Het biedt functies zoals:

- Selectie van Open Models zoals OpenAI, Mistral en Llama
- Gebruik van gelicentieerde gegevens via providers zoals Tripadvisor
- Gebruik van gestandaardiseerde OpenAPI 3.0-tools

### Agentic Patterns

Communicatie met LLMs gebeurt via prompts. Gezien de semi-autonome aard van AI Agents is het niet altijd mogelijk of nodig om de LLM handmatig opnieuw te prompten na een verandering in de omgeving. We gebruiken **Agentic Patterns** die ons in staat stellen de LLM over meerdere stappen op een meer schaalbare manier te prompten.

Deze cursus is verdeeld in enkele van de huidige populaire Agentic Patterns.

### Agentic Frameworks

Agentic Frameworks stellen ontwikkelaars in staat om agentic patterns via code te implementeren. Deze frameworks bieden sjablonen, plugins en tools voor betere samenwerking tussen AI Agents. Deze voordelen bieden mogelijkheden voor betere observatie en probleemoplossing van AI Agent-systemen.

In deze cursus zullen we het onderzoeksgerichte AutoGen-framework en het productieklare Agent-framework van Semantic Kernel verkennen.

## Voorbeeldcodes

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Meer vragen over AI Agents?

Word lid van de [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) om andere cursisten te ontmoeten, spreekuren bij te wonen en je vragen over AI Agents beantwoord te krijgen.

## Vorige Les

[Course Setup](../00-course-setup/README.md)

## Volgende Les

[Verkennen van Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->