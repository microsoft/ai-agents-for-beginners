[![Introductie tot AI-agenten](../../../translated_images/nl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_


# Introductie tot AI-agenten en toepassingsgevallen voor agenten

Welkom bij de cursus "AI Agents for Beginners"! Deze cursus biedt fundamentele kennis en praktische voorbeelden voor het bouwen van AI-agenten.

Sluit je aan bij de <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord-community</a> om andere leerlingen en AI-agentbouwers te ontmoeten en eventuele vragen over deze cursus te stellen.

Om deze cursus te beginnen, starten we met een beter begrip van wat AI-agenten zijn en hoe we ze kunnen gebruiken in de toepassingen en workflows die we bouwen.

## Introductie

Deze les behandelt:

- Wat zijn AI-agenten en wat zijn de verschillende types agenten?
- Voor welke toepassingsgevallen zijn AI-agenten het meest geschikt en hoe kunnen ze ons helpen?
- Wat zijn enkele van de basisbouwstenen bij het ontwerpen van agentachtige oplossingen?

## Leerdoelen
Na het voltooien van deze les zou je in staat moeten zijn om:

- AI-agentconcepten te begrijpen en hoe ze verschillen van andere AI-oplossingen.
- AI-agenten zo efficiënt mogelijk toe te passen.
- Agentachtige oplossingen productief te ontwerpen voor zowel gebruikers als klanten.

## Het definiëren van AI-agenten en types AI-agenten

### Wat zijn AI-agenten?

AI-agenten zijn **systemen** die **Grote taalmodellen (LLMs)** in staat stellen om **acties uit te voeren** door hun mogelijkheden uit te breiden door LLMs **toegang te geven tot hulpmiddelen** en **kennis**.

Laten we deze definitie in kleinere onderdelen opsplitsen:

- **Systeem** - Het is belangrijk om agenten niet te zien als slechts één component, maar als een systeem van vele componenten. Op het basale niveau zijn de componenten van een AI-agent:
  - **Omgeving** - De gedefinieerde ruimte waarbinnen de AI-agent opereert. Bijvoorbeeld, als we een reisboekings-AI-agent zouden hebben, kan de omgeving het reisboekingensysteem zijn dat de AI-agent gebruikt om taken te voltooien.
  - **Sensoren** - Omgevingen hebben informatie en geven feedback. AI-agenten gebruiken sensoren om deze informatie over de huidige toestand van de omgeving te verzamelen en te interpreteren. In het voorbeeld van de reisboekingsagent kan het reisboekingensysteem informatie geven zoals hotelbeschikbaarheid of vluchtprijzen.
  - **Actuatoren** - Zodra de AI-agent de huidige toestand van de omgeving heeft ontvangen, bepaalt de agent voor de huidige taak welke actie moet worden uitgevoerd om de omgeving te veranderen. Voor de reisboekingsagent kan dit bijvoorbeeld het boeken van een beschikbare kamer voor de gebruiker zijn.

![Wat zijn AI-agenten?](../../../translated_images/nl/what-are-ai-agents.1ec8c4d548af601a.webp)

**Grote taalmodellen** - Het concept van agenten bestond al vóór de creatie van LLMs. Het voordeel van het bouwen van AI-agenten met LLMs is hun vermogen om menselijke taal en gegevens te interpreteren. Dit vermogen stelt LLMs in staat om omgevingsinformatie te interpreteren en een plan te definiëren om de omgeving te veranderen.

**Acties uitvoeren** - Buiten AI-agentensystemen zijn LLMs beperkt tot situaties waarin de actie het genereren van inhoud of informatie is op basis van de prompt van een gebruiker. Binnen AI-agentensystemen kunnen LLMs taken voltooien door het verzoek van de gebruiker te interpreteren en hulpmiddelen te gebruiken die beschikbaar zijn in hun omgeving.

**Toegang tot hulpmiddelen** - Tot welke hulpmiddelen het LLM toegang heeft, wordt bepaald door 1) de omgeving waarin het opereert en 2) de ontwikkelaar van de AI-agent. Voor ons reisagentvoorbeeld worden de hulpmiddelen van de agent beperkt door de bewerkingen die beschikbaar zijn in het boekingssysteem, en/of kan de ontwikkelaar de toegang van de agent tot hulpmiddelen beperken tot bijvoorbeeld alleen vluchten.

**Geheugen + Kennis** - Geheugen kan kortetermijn zijn in de context van het gesprek tussen de gebruiker en de agent. Op de lange termijn, buiten de informatie die door de omgeving wordt verstrekt, kunnen AI-agenten ook kennis ophalen uit andere systemen, services, hulpmiddelen en zelfs andere agenten. In het reisagentvoorbeeld kan deze kennis informatie zijn over de reisvoorkeuren van de gebruiker die zich in een klantenbestand bevindt.

### De verschillende types agenten

Nu we een algemene definitie van AI-agenten hebben, laten we enkele specifieke agenttypes bekijken en hoe ze zouden worden toegepast op een reisboekings-AI-agent.

| **Agent Type**                | **Description**                                                                                                                       | **Example**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Eenvoudige reflexagenten**      | Voeren onmiddellijke acties uit op basis van vooraf gedefinieerde regels.                                                                                  | Reisagent interpreteert de context van de e-mail en stuurt reisklachten door naar de klantenservice.                                                                                                                          |
| **Modelgebaseerde reflexagenten** | Voeren acties uit op basis van een model van de wereld en veranderingen in dat model.                                                              | Reisagent geeft prioriteit aan routes met significante prijswijzigingen op basis van toegang tot historische prijsgegevens.                                                                                                             |
| **Doelgerichte agenten**         | Maken plannen om specifieke doelen te bereiken door het doel te interpreteren en acties te bepalen om het te bereiken.                                  | Reisagent boekt een reis door de benodigde reisarrangementen te bepalen (auto, openbaar vervoer, vluchten) van de huidige locatie naar de bestemming.                                                                                |
| **Nut-gebaseerde agenten**      | Houden rekening met voorkeuren en wegen afwegingen numeriek om te bepalen hoe doelen te bereiken.                                               | Reisagent maximaliseert nut door gebruiksgemak versus kosten af te wegen bij het boeken van reizen.                                                                                                                                          |
| **Leeragenten**           | Verbeteren in de loop van de tijd door te reageren op feedback en acties dienovereenkomstig aan te passen.                                                        | Reisagent verbetert door klantfeedback van enquêtes na de reis te gebruiken om aanpassingen te maken voor toekomstige boekingen.                                                                                                               |
| **Hiërarchische agenten**       | Bestaan uit meerdere agenten in een gelaagd systeem, waarbij agenten op hoger niveau taken opdelen in subtaken die lagere agenten voltooien. | Reisagent annuleert een reis door de taak op te delen in subtaken (bijvoorbeeld het annuleren van specifieke boekingen) en lagere agenten deze subtaken te laten voltooien en terugrapporteren aan de agent op hoger niveau.                                     |
| **Multi-agentensystemen (MAS)** | Agenten voltooien taken onafhankelijk, hetzij coöperatief hetzij competitief.                                                           | Coöperatief: Meerdere agenten boeken specifieke reisdiensten zoals hotels, vluchten en entertainment. Competitief: Meerdere agenten beheren en concurreren over een gedeelde hotelboekingskalender om klanten in het hotel te boeken. |

## Wanneer AI-agenten gebruiken

In het eerdere gedeelte hebben we het reisagent-gebruiksscenario gebruikt om uit te leggen hoe de verschillende types agenten kunnen worden gebruikt in verschillende scenario's van reisboekingen. We zullen deze toepassing blijven gebruiken in de hele cursus.

Laten we kijken naar de soorten toepassingsgevallen waarvoor AI-agenten het meest geschikt zijn:

![Wanneer AI-agenten gebruiken?](../../../translated_images/nl/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Open-eindproblemen** - het LLM toestaan om de benodigde stappen te bepalen om een taak te voltooien omdat dit niet altijd in een workflow kan worden vastgelegd.
- **Meerstapsprocessen** - taken die een niveau van complexiteit vereisen waarbij de AI-agent hulpmiddelen of informatie over meerdere beurten moet gebruiken in plaats van eenmalige ophalen.  
- **Verbetering in de loop van de tijd** - taken waarbij de agent in de loop van de tijd kan verbeteren door feedback te ontvangen van zijn omgeving of gebruikers om een betere bruikbaarheid te bieden.

We behandelen meer overwegingen bij het gebruik van AI-agenten in de les Vertrouwbare AI-agenten bouwen.

## Basisprincipes van agentachtige oplossingen

### Agentontwikkeling

De eerste stap bij het ontwerpen van een AI-agentensysteem is het definiëren van de hulpmiddelen, acties en gedragingen. In deze cursus richten we ons op het gebruik van de **Azure AI Agent Service** om onze agenten te definiëren. Het biedt functies zoals:

- Selectie van Open modellen zoals OpenAI, Mistral en Llama
- Gebruik van gelicentieerde gegevens via providers zoals Tripadvisor
- Gebruik van gestandaardiseerde OpenAPI 3.0-hulpmiddelen

### Agentachtige patronen

Communicatie met LLMs verloopt via prompts. Gezien de semi-autonome aard van AI-agenten is het niet altijd mogelijk of nodig om het LLM handmatig opnieuw te prompten na een verandering in de omgeving. We gebruiken **agentachtige patronen** die ons in staat stellen het LLM over meerdere stappen op een meer schaalbare manier te prompten.

Deze cursus is verdeeld in enkele van de momenteel populaire agentachtige patronen.

### Agentachtige frameworks

Agentachtige frameworks stellen ontwikkelaars in staat agentachtige patronen via code te implementeren. Deze frameworks bieden sjablonen, plugins en hulpmiddelen voor betere samenwerking tussen agenten. Deze voordelen bieden mogelijkheden voor betere observeerbaarheid en probleemoplossing van AI-agentensystemen.

In deze cursus zullen we het Microsoft Agent Framework (MAF) verkennen voor het bouwen van productieklare AI-agenten.

## Voorbeeldcodes

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Nog meer vragen over AI-agenten?

Sluit je aan bij de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, deel te nemen aan spreekuren en je vragen over AI-agenten beantwoord te krijgen.

## Vorige les

[Course Setup](../00-course-setup/README.md)

## Volgende les

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we naar nauwkeurigheid streven, houd er rekening mee dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->