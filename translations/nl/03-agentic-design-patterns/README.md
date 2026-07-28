[![Hoe ontwerp je goede AI-agents](../../../translated_images/nl/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_
# Principes voor AI Agentisch Ontwerp

## Introductie

Er zijn veel manieren om na te denken over het bouwen van AI Agentische Systemen. Aangezien ambiguïteit een kenmerk is en geen fout in Generative AI ontwerp, is het soms moeilijk voor ingenieurs om te bepalen waar ze moeten beginnen. We hebben een reeks mensgerichte UX Ontwerpprincipes opgesteld om ontwikkelaars in staat te stellen klantgerichte agentische systemen te bouwen om aan hun zakelijke behoeften te voldoen. Deze ontwerpprincipes zijn geen voorschrijvende architectuur, maar eerder een startpunt voor teams die agent-ervaringen definiëren en ontwikkelen.

Over het algemeen zouden agents moeten:

- Menselijke capaciteiten uitbreiden en opschalen (brainstormen, probleemoplossing, automatisering, enz.)
- Kennisleemten opvullen (brengt me op de hoogte van kennisdomeinen, vertaling, enz.)
- Samenwerking faciliteren en ondersteunen op de manieren waarop wij als individuen het liefst samenwerken met anderen
- Ons betere versies van onszelf maken (bijv. life coach/taskmaster, ons helpen emotionele regulatie en mindfulness vaardigheden te leren, veerkracht opbouwen, enz.)

## Deze les behandelt

- Wat de Agentische Ontwerpprincipes zijn
- Welke richtlijnen gevolgd moeten worden bij het implementeren van deze ontwerpprincipes
- Voorbeelden van het gebruik van de ontwerpprincipes

## Leerdoelen

Na het voltooien van deze les zul je in staat zijn om:

1. Uit te leggen wat de Agentische Ontwerpprincipes zijn
2. De richtlijnen voor het gebruik van de Agentische Ontwerpprincipes uit te leggen
3. Te begrijpen hoe je een agent bouwt met gebruik van de Agentische Ontwerpprincipes

## De Agentische Ontwerpprincipes

![Agentische Ontwerpprincipes](../../../translated_images/nl/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Ruimte)

Dit is de omgeving waarin de agent opereert. Deze principes bepalen hoe we agents ontwerpen voor het deelnemen aan fysieke en digitale werelden.

- **Verbinding maken, niet samenvoegen** – help mensen verbinden met andere mensen, gebeurtenissen en bruikbare kennis om samenwerking en verbinding mogelijk te maken.
- Agents helpen gebeurtenissen, kennis en mensen verbinden.
- Agents brengen mensen dichter bij elkaar. Ze zijn niet ontworpen om mensen te vervangen of te kleineren.
- **Gemakkelijk toegankelijk maar af en toe onzichtbaar** – de agent werkt grotendeels op de achtergrond en ondersteunt ons alleen wanneer dit relevant en gepast is.
  - Agent is gemakkelijk vindbaar en toegankelijk voor geautoriseerde gebruikers op elk apparaat of platform.
  - Agent ondersteunt multimodale invoer en uitvoer (geluid, spraak, tekst, enz.).
  - Agent kan naadloos schakelen tussen voorgrond en achtergrond; tussen proactief en reactief, afhankelijk van zijn waarneming van gebruikersbehoeften.
  - Agent kan in onzichtbare vorm werken, maar het achtergrondproces en de samenwerking met andere Agents zijn transparant en bestuurbaar voor de gebruiker.

### Agent (Tijd)

Dit is hoe de agent zich in de tijd gedraagt. Deze principes bepalen hoe we agents ontwerpen die interactie hebben met verleden, heden en toekomst.

- **Verleden**: Reflecteren op de geschiedenis inclusief zowel toestand als context.
  - Agent levert relevantere resultaten op basis van analyse van uitgebreidere historische gegevens, verder dan alleen het evenement, mensen of toestanden.
  - Agent creëert verbindingen vanuit gebeurtenissen uit het verleden en reflecteert actief op geheugen om in te spelen op actuele situaties.
- **Nu**: Aansporen meer dan alleen melden.
  - Agent belichaamt een uitgebreide benadering van interactie met mensen. Wanneer een gebeurtenis plaatsvindt, gaat de Agent verder dan statische notificatie of andere statische formaliteit. Agent kan flows vereenvoudigen of dynamisch signalen genereren om de aandacht van de gebruiker op het juiste moment te richten.
  - Agent levert informatie op basis van de context van de omgeving, sociale en culturele veranderingen en afgestemd op de intentie van de gebruiker.
  - Agent interactie kan geleidelijk zijn, evoluerend/groeiend in complexiteit om gebruikers op lange termijn te versterken.
- **Toekomst**: Aanpassen en evolueren.
  - Agent past zich aan diverse apparaten, platforms en modaliteiten aan.
  - Agent past zich aan gebruikersgedrag, toegankelijkheidsbehoeften aan en is vrij aanpasbaar.
  - Agent wordt gevormd door en evolueert via continue gebruikersinteractie.

### Agent (Kern)

Dit zijn de belangrijkste elementen in de kern van het ontwerp van een agent.

- **Omarm onzekerheid maar vestig vertrouwen**.
  - Een zeker niveau van onzekerheid bij de Agent wordt verwacht. Onzekerheid is een belangrijk onderdeel van agent ontwerp.
  - Vertrouwen en transparantie zijn fundamentele lagen van agent ontwerp.
  - Mensen hebben controle over wanneer de Agent aan/uit is en de status van de Agent is te allen tijde duidelijk zichtbaar.

## De richtlijnen om deze principes te implementeren

Wanneer je de eerdere ontwerpprincipes toepast, gebruik dan de volgende richtlijnen:

1. **Transparantie**: Informeer de gebruiker dat AI betrokken is, hoe het werkt (inclusief eerdere acties), en hoe feedback te geven en het systeem aan te passen.
2. **Controle**: Stel de gebruiker in staat om aan te passen, voorkeuren te specificeren en te personaliseren, en controle te hebben over het systeem en zijn eigenschappen (inclusief de mogelijkheid om te vergeten).
3. **Consistentie**: Streef naar consistente, multimodale ervaringen op apparaten en eindpunten. Gebruik waar mogelijk vertrouwde UI/UX-elementen (bijv. microfoonpictogram voor spraakinteractie) en verminder de cognitieve belasting van de klant zoveel mogelijk (bijv. streef naar beknopte antwoorden, visuele hulpmiddelen en ‘Meer informatie’-inhoud).

## Hoe ontwerp je een Reisagent met behulp van deze Principes en Richtlijnen

Stel dat je een Reisagent ontwerpt, zo kun je denken aan het gebruik van de Ontwerpprincipes en Richtlijnen:

1. **Transparantie** – Laat de gebruiker weten dat de Reisagent een AI-gestuurde Agent is. Geef enkele basisinstructies over hoe te beginnen (bijv. een “Hallo” bericht, voorbeeld prompts). Documenteer dit duidelijk op de productpagina. Toon de lijst met prompts die een gebruiker in het verleden heeft gevraagd. Maak duidelijk hoe feedback gegeven kan worden (duim omhoog en omlaag, Feedback verzenden knop, enz.). Maak duidelijk of de Agent gebruiks- of onderwerpbeperkingen heeft.
2. **Controle** – Zorg dat het duidelijk is hoe de gebruiker de Agent kan aanpassen nadat deze is gemaakt met zaken als de Systeem Prompt. Stel de gebruiker in staat te kiezen hoe uitgebreid de Agent is, de schrijfstijl en eventuele kanttekeningen over waar de Agent niet over mag praten. Laat de gebruiker alle gekoppelde bestanden of gegevens, prompts en eerdere gesprekken bekijken en verwijderen.
3. **Consistentie** – Zorg dat de iconen voor Deel Prompt, voeg een bestand of foto toe en tag iemand of iets standaard en herkenbaar zijn. Gebruik het paperclip-icoon om bestandsupload/-deling met de Agent aan te geven, en een afbeelding-icoon om grafische uploads aan te geven.

## Voorbeeldcodes

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Meer vragen over AI Agentische Ontwerppatronen?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, kantooruren bij te wonen en je AI Agents vragen beantwoord te krijgen.

## Aanvullende bronnen

- <a href="https://openai.com" target="_blank">Praktijken voor het Besturen van Agentische AI Systemen | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Het HAX Toolkit Project - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Responsible AI Toolbox</a>

## Vorige les

[Verkenning van Agentische Frameworks](../02-explore-agentic-frameworks/README.md)

## Volgende les

[Designpatroon voor gebruik van tools](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->