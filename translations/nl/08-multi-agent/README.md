[![Multi-agent ontwerp](../../../translated_images/nl/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Multi-agent ontwerp patronen

Zodra je begint te werken aan een project waarbij meerdere agenten betrokken zijn, moet je rekening houden met het multi-agent ontwerp patroon. Het is echter misschien niet direct duidelijk wanneer je overschakelt op multi-agenten en wat de voordelen zijn.

## Introductie

In deze les proberen we de volgende vragen te beantwoorden:

- Wat zijn de scenario's waarin multi-agenten toepasbaar zijn?
- Wat zijn de voordelen van het gebruik van multi-agenten ten opzichte van één enkele agent die meerdere taken uitvoert?
- Wat zijn de bouwstenen voor het implementeren van het multi-agent ontwerp patroon?
- Hoe krijgen we inzicht in hoe de meerdere agenten met elkaar interacteren?

## Leerdoelen

Na deze les zou je in staat moeten zijn om:

- Scenario's te identificeren waarin multi-agenten toepasbaar zijn
- De voordelen van het gebruik van multi-agenten ten opzichte van een enkele agent te herkennen.
- De bouwstenen te begrijpen voor het implementeren van het multi-agent ontwerp patroon.

Wat is het grotere geheel?

*Multi-agenten zijn een ontwerp patroon dat het mogelijk maakt dat meerdere agenten samenwerken om een gemeenschappelijk doel te bereiken*.

Dit patroon wordt veel gebruikt in diverse vakgebieden, waaronder robotica, autonome systemen en gedistribueerd rekenen.

## Scenario's waarin multi-agenten toepasbaar zijn

Dus welke scenario's zijn goede toepassingen voor het gebruik van multi-agenten? Het antwoord is dat er veel scenario's zijn waarin het inzetten van meerdere agenten voordelig is, vooral in de volgende gevallen:

- **Grote werklasten**: Grote werklasten kunnen worden opgesplitst in kleinere taken en toegewezen aan verschillende agenten, wat parallelle verwerking en snellere voltooiing mogelijk maakt. Een voorbeeld hiervan is bij een grote data verwerkingstaak.
- **Complexe taken**: Complexe taken, net als grote werklasten, kunnen worden onderverdeeld in kleinere subtaken en toegewezen aan verschillende agenten, elk gespecialiseerd in een specifiek aspect van de taak. Een goed voorbeeld hiervan is bij autonome voertuigen waar verschillende agenten navigatie, obstakeldetectie en communicatie met andere voertuigen beheren.
- **Diverse expertise**: Verschillende agenten kunnen diverse expertise hebben, waardoor ze verschillende aspecten van een taak effectiever kunnen afhandelen dan een enkele agent. Een goed voorbeeld hiervan is in de gezondheidszorg waar agenten diagnostiek, behandelplannen en patiëntmonitoring kunnen beheren.

## Voordelen van het gebruik van multi-agenten ten opzichte van een enkele agent

Een enkel agentsysteem kan goed werken voor eenvoudige taken, maar voor complexere taken biedt het gebruik van meerdere agenten verschillende voordelen:

- **Specialisatie**: Elke agent kan gespecialiseerd zijn in een specifieke taak. Het ontbreken van specialisatie in een enkele agent betekent dat je een agent hebt die alles kan doen, maar mogelijk in de war raakt bij een complexe taak. Het kan bijvoorbeeld een taak uitvoeren waarvoor het niet het beste geschikt is.
- **Schaalbaarheid**: Het is gemakkelijker om systemen op te schalen door meer agenten toe te voegen in plaats van één enkele agent te overladen.
- **Fouttolerantie**: Als één agent faalt, kunnen anderen blijven functioneren, wat zorgt voor betrouwbaarheid van het systeem.

Laten we een voorbeeld nemen: een reis boeken voor een gebruiker. Een enkel agentsysteem zou alle aspecten van het boekingsproces moeten afhandelen, van het vinden van vluchten tot het boeken van hotels en huurauto's. Om dit met een enkele agent te bereiken, zou de agent tools moeten hebben om al deze taken te verwerken. Dit kan leiden tot een complex en monolithisch systeem dat moeilijk te onderhouden en op te schalen is. Een multi-agent systeem kan daarentegen verschillende agenten hebben die gespecialiseerd zijn in het vinden van vluchten, het boeken van hotels en huurauto's. Dit maakt het systeem modularer, gemakkelijker te onderhouden en schaalbaar.

Vergelijk dit met een reisbureau beheerd als een familiebedrijf versus een reisbureau beheerd als een franchise. Het familiebedrijf zou een enkele agent hebben die alle aspecten van het boekingsproces beheert, terwijl de franchise verschillende agenten zou hebben die verschillende aspecten van het boekingsproces beheren.

## Bouwstenen van het implementeren van het multi-agent ontwerp patroon

Voordat je het multi-agent ontwerp patroon kunt implementeren, moet je de bouwstenen begrijpen die het patroon vormen.

Laten we dit concreter maken door opnieuw te kijken naar het voorbeeld van een reis boeken voor een gebruiker. In dit geval omvatten de bouwstenen:

- **Agentcommunicatie**: Agenten voor het vinden van vluchten, boeken van hotels en huurauto's moeten communiceren en informatie delen over de voorkeuren en beperkingen van de gebruiker. Je moet beslissen over de protocollen en methoden voor deze communicatie. Wat dit concreet betekent is dat de agent voor het vinden van vluchten moet communiceren met de agent voor het boeken van hotels om ervoor te zorgen dat het hotel voor dezelfde data als de vlucht wordt geboekt. Dat betekent dat de agenten informatie moeten delen over de reisdata van de gebruiker, wat inhoudt dat je moet bepalen *welke agenten informatie delen en hoe ze die informatie delen*.
- **Coördinatiemechanismen**: Agenten moeten hun acties coördineren om te zorgen dat de voorkeuren en beperkingen van de gebruiker worden voldaan. Een voorkeur van de gebruiker kan zijn dat ze een hotel dichtbij de luchthaven willen, terwijl een beperking kan zijn dat huurauto's alleen op de luchthaven beschikbaar zijn. Dit betekent dat de agent voor het boeken van hotels moet coördineren met de agent voor het boeken van huurauto's om ervoor te zorgen dat de voorkeuren en beperkingen van de gebruiker worden voldaan. Dit betekent dat je moet bepalen *hoe de agenten hun acties coördineren*.
- **Agentarchitectuur**: Agenten moeten de interne structuur hebben om beslissingen te nemen en te leren van hun interacties met de gebruiker. Dit betekent dat de agent voor het vinden van vluchten de interne structuur moet hebben om beslissingen te nemen over welke vluchten aan de gebruiker worden aanbevolen. Dit betekent dat je moet bepalen *hoe de agenten beslissingen nemen en leren van hun interacties met de gebruiker*. Voorbeelden van hoe een agent leert en verbetert kunnen zijn dat de agent voor het vinden van vluchten een machine learning model zou kunnen gebruiken om vluchten aan te bevelen op basis van eerdere voorkeuren van de gebruiker.
- **Inzicht in multi-agent interacties**: Je moet inzicht hebben in hoe de meerdere agenten met elkaar interacteren. Dit betekent dat je tools en technieken moet hebben voor het volgen van agentactiviteiten en interacties. Dit kan in de vorm zijn van logging- en monitoringshulpmiddelen, visualisatiehulpmiddelen en prestatiestatistieken.
- **Multi-agent patronen**: Er zijn verschillende patronen voor het implementeren van multi-agent systemen, zoals gecentraliseerde, gedecentraliseerde en hybride architecturen. Je moet beslissen welk patroon het beste past bij jouw gebruikssituatie.
- **Mens in de lus**: In de meeste gevallen zal er een mens in de lus zijn en je moet de agenten instrueren wanneer ze menselijke tussenkomst moeten vragen. Dit kan in de vorm zijn van een gebruiker die vraagt om een specifiek hotel of vlucht die de agenten niet hebben aanbevolen, of om bevestiging voordat een vlucht of hotel wordt geboekt.

## Inzicht in multi-agent interacties

Het is belangrijk dat je inzicht hebt in hoe de meerdere agenten met elkaar interacteren. Dit inzicht is essentieel voor het debuggen, optimaliseren en waarborgen van de effectiviteit van het systeem. Om dit te bereiken, moet je tools en technieken hebben om agentactiviteiten en interacties te volgen. Dit kan in de vorm zijn van logging- en monitoringshulpmiddelen, visualisatiehulpmiddelen en prestatiestatistieken.

Bijvoorbeeld, in het geval van het boeken van een reis voor een gebruiker, zou je een dashboard kunnen hebben dat de status toont van elke agent, de voorkeuren en beperkingen van de gebruiker, en de interacties tussen agenten. Dit dashboard zou de reisdata van de gebruiker kunnen tonen, de vluchten aanbevolen door de vluchtagent, de hotels aanbevolen door de hotelagent, en de huurauto’s aanbevolen door de huurauto-agent. Dit zou je een duidelijk beeld geven van hoe de agenten met elkaar interacteren en of de voorkeuren en beperkingen van de gebruiker worden nageleefd.

Laten we elk van deze aspecten wat gedetailleerder bekijken.

- **Logging- en monitoringshulpmiddelen**: Je wilt logging voor elke actie die een agent onderneemt. Een logvermelding kan informatie opslaan over de agent die de actie uitvoerde, de uitgevoerde actie, het tijdstip waarop de actie werd uitgevoerd en het resultaat van de actie. Deze informatie kan dan worden gebruikt voor debuggen, optimaliseren en meer.

- **Visualisatiehulpmiddelen**: Visualisatiehulpmiddelen kunnen je helpen om de interacties tussen agenten op een meer intuïtieve manier te zien. Bijvoorbeeld, je zou een grafiek kunnen hebben die de informatiestroom tussen agenten toont. Dit kan je helpen om knelpunten, inefficiënties en andere problemen in het systeem te herkennen.

- **Prestatiestatistieken**: Prestatiestatistieken kunnen je helpen bij het volgen van de effectiviteit van het multi-agent systeem. Bijvoorbeeld, je zou de tijd kunnen volgen die nodig is om een taak te voltooien, het aantal voltooide taken per tijdseenheid en de nauwkeurigheid van de aanbevelingen door de agenten. Deze informatie kan je helpen gebieden voor verbetering te identificeren en het systeem te optimaliseren.

## Multi-agent patronen

Laten we enkele concrete patronen bekijken die we kunnen gebruiken om multi-agent apps te creëren. Hier zijn enkele interessante patronen om te overwegen:

### Groepschat

Dit patroon is nuttig wanneer je een groepschatapplicatie wilt maken waarbij meerdere agenten met elkaar kunnen communiceren. Typische gebruikssituaties voor dit patroon zijn team samenwerking, klantenondersteuning en sociale netwerken.

In dit patroon vertegenwoordigt elke agent een gebruiker in de groepschat, en worden berichten uitgewisseld tussen agenten via een berichtenprotocol. De agenten kunnen berichten naar de groepschat sturen, berichten ontvangen van de groepschat, en reageren op berichten van andere agenten.

Dit patroon kan worden geïmplementeerd met een gecentraliseerde architectuur waarbij alle berichten via een centrale server worden geleid, of een gedecentraliseerde architectuur waarbij berichten direct worden uitgewisseld.

![Groepschat](../../../translated_images/nl/multi-agent-group-chat.ec10f4cde556babd.webp)

### Overdracht

Dit patroon is nuttig wanneer je een applicatie wilt maken waarbij meerdere agenten taken aan elkaar kunnen overdragen.

Typische gebruikssituaties voor dit patroon zijn klantenondersteuning, taakbeheer en workflowautomatisering.

In dit patroon vertegenwoordigt elke agent een taak of een stap in een workflow, en kunnen agenten taken aan andere agenten overdragen op basis van vooraf bepaalde regels.

![Overdracht](../../../translated_images/nl/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Samenwerkende filtering

Dit patroon is nuttig wanneer je een applicatie wilt maken waarbij meerdere agenten samenwerken om aanbevelingen aan gebruikers te doen.

De reden waarom je meerdere agenten wilt laten samenwerken is omdat elke agent verschillende expertise kan hebben en op verschillende manieren kan bijdragen aan het aanbevelingsproces.

Laten we een voorbeeld nemen waarbij een gebruiker een aanbeveling wil over de beste aandelen om te kopen op de aandelenmarkt.

- **Industrie-expert**: Een agent kan een expert zijn in een specifieke industrie.
- **Technische analyse**: Een andere agent kan een expert zijn in technische analyse.
- **Fundamentele analyse**: en een andere agent kan een expert zijn in fundamentele analyse. Door samen te werken kunnen deze agenten een meer uitgebreide aanbeveling aan de gebruiker doen.

![Aanbeveling](../../../translated_images/nl/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Teruggaveproces

Beschouw een scenario waarin een klant probeert een terugbetaling voor een product te krijgen. Er kunnen behoorlijk wat agenten betrokken zijn bij dit proces, maar laten we het verdelen tussen agenten die specifiek zijn voor dit proces en algemene agenten die in andere processen kunnen worden gebruikt.

**Agenten specifiek voor het teruggaveproces**:

Hier zijn enkele agenten die betrokken kunnen zijn bij het teruggaveproces:

- **Klantagent**: Deze agent vertegenwoordigt de klant en is verantwoordelijk voor het starten van het teruggaveproces.
- **Verkoperagent**: Deze agent vertegenwoordigt de verkoper en is verantwoordelijk voor het verwerken van de terugbetaling.
- **Betaalagent**: Deze agent vertegenwoordigt het betaalproces en is verantwoordelijk voor het terugbetalen van de betaling aan de klant.
- **Oplossingsagent**: Deze agent vertegenwoordigt het oplossingsproces en is verantwoordelijk voor het oplossen van eventuele problemen die tijdens het teruggaveproces ontstaan.
- **Compliance-agent**: Deze agent vertegenwoordigt het compliance-proces en is verantwoordelijk voor het waarborgen dat het teruggaveproces voldoet aan regelgeving en beleid.

**Algemene agenten**:

Deze agenten kunnen door andere onderdelen van je bedrijf worden gebruikt.

- **Verzendagent**: Deze agent vertegenwoordigt het verzendproces en is verantwoordelijk voor het terugsturen van het product naar de verkoper. Deze agent kan zowel worden gebruikt voor het teruggaveproces als voor algemene verzending van een product via een aankoop bijvoorbeeld.
- **Feedback-agent**: Deze agent vertegenwoordigt het feedbackproces en is verantwoordelijk voor het verzamelen van feedback van de klant. Feedback kan op elk moment worden verzameld en niet alleen tijdens het teruggaveproces.
- **Escalatie-agent**: Deze agent vertegenwoordigt het escalatieproces en is verantwoordelijk voor het escaleren van problemen naar een hoger niveau van ondersteuning. Je kunt dit type agent voor elk proces gebruiken waarbij je een probleem moet escaleren.
- **Notificatie-agent**: Deze agent vertegenwoordigt het notificatieproces en is verantwoordelijk voor het versturen van meldingen aan de klant tijdens verschillende fasen van het teruggaveproces.
- **Analyse-agent**: Deze agent vertegenwoordigt het analyseproces en is verantwoordelijk voor het analyseren van gegevens met betrekking tot het teruggaveproces.
- **Audit-agent**: Deze agent vertegenwoordigt het audit-proces en is verantwoordelijk voor het auditen van het teruggaveproces om ervoor te zorgen dat het correct wordt uitgevoerd.
- **Rapportage-agent**: Deze agent vertegenwoordigt het rapportageproces en is verantwoordelijk voor het genereren van rapporten over het teruggaveproces.
- **Kennisagent**: Deze agent vertegenwoordigt het kennisproces en is verantwoordelijk voor het onderhouden van een kennisbank met informatie gerelateerd aan het teruggaveproces. Deze agent kan kennis hebben over terugbetalingen en andere delen van je bedrijf.
- **Beveiligingsagent**: Deze agent vertegenwoordigt het beveiligingsproces en is verantwoordelijk voor het waarborgen van de beveiliging van het teruggaveproces.
- **Kwaliteitsagent**: Deze agent vertegenwoordigt het kwaliteitsproces en is verantwoordelijk voor het waarborgen van de kwaliteit van het teruggaveproces.

Er zijn behoorlijk wat agenten genoemd, zowel voor het specifieke teruggaveproces als voor de algemene agenten die in andere delen van je bedrijf kunnen worden gebruikt. Hopelijk geeft dit je een idee hoe je kunt beslissen welke agenten je in je multi-agent systeem kunt gebruiken.

## Opdracht

Ontwerp een multi-agent systeem voor een klantenondersteuningsproces. Identificeer de agenten die betrokken zijn bij het proces, hun rollen en verantwoordelijkheden, en hoe zij met elkaar interacteren. Overweeg zowel agenten die specifiek zijn voor het klantenondersteuningsproces als algemene agenten die in andere delen van je bedrijf kunnen worden gebruikt.


> Denk er even over na voordat je de volgende oplossing leest, je hebt misschien meer agenten nodig dan je denkt.

> TIP: Denk na over de verschillende fasen van het klantenserviceproces en overweeg ook de agenten die nodig zijn voor elk systeem.

## Oplossing

[Oplossing](./solution/solution.md)

## Kenniscontroles

### Vraag 1

Welke situatie is het meest geschikt voor een multi-agentensysteem?

- [ ] A1: Een supportbot beantwoordt veelvoorkomende vragen met één kennisbank en een kleine set tools.
- [ ] A2: Een restitutie-workflow heeft aparte rollen voor fraude, betaling en compliance, elk met eigen tools, en hun resultaten moeten worden gecoördineerd.
- [ ] A3: Dezelfde eenvoudige classificatieaanvraag komt duizenden keren per uur binnen.

### Vraag 2

Wanneer is één enkele agent meestal de betere keuze?

- [ ] A1: De taak kan worden uitgevoerd met één set instructies en tools, zonder overdracht naar specialisten.
- [ ] A2: De agent heeft toegang tot meer dan één tool.
- [ ] A3: De workflow vereist aparte rollen met verschillende toestemmingen en onafhankelijke audit-trails.

[Oplossing quiz](./solution/solution-quiz.md)

## Samenvatting

In deze les hebben we gekeken naar het multi-agent ontwerpprincipe, inclusief de scenario’s waarbij multi-agenten toepasbaar zijn, de voordelen van het gebruik van multi-agenten boven een enkele agent, de bouwstenen voor het implementeren van het multi-agent ontwerpprincipe, en hoe inzicht te krijgen in hoe de verschillende agenten met elkaar samenwerken.

### Meer vragen over het Multi-Agent Ontwerpprincipe?

Sluit je aan bij de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, deel te nemen aan office hours en je vragen over AI Agenten beantwoord te krijgen.

## Aanvullende bronnen

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework documentatie</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentische ontwerpprincipes</a>


## Vorige les

[Planning Design](../07-planning-design/README.md)

## Volgende les

[Metacognitie in AI Agenten](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->