[![Multi-agent ontwerp](../../../translated_images/nl/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Multi-agent ontwerp patronen

Zodra je begint met werken aan een project dat meerdere agenten omvat, moet je rekening houden met het multi-agent ontwerp patroon. Het is echter misschien niet meteen duidelijk wanneer je moet overschakelen naar multi-agenten en wat de voordelen zijn.

## Introductie

In deze les proberen we de volgende vragen te beantwoorden:

- Voor welke scenario's zijn multi-agenten toepasbaar?
- Wat zijn de voordelen van het gebruik van multi-agenten ten opzichte van slechts één enkele agent die meerdere taken uitvoert?
- Wat zijn de bouwstenen voor het implementeren van het multi-agent ontwerp patroon?
- Hoe krijgen we zicht op hoe de meerdere agenten met elkaar interacteren?

## Leerdoelen

Na deze les zou je in staat moeten zijn om:

- Scenario's te identificeren waar multi-agenten toepasbaar zijn
- De voordelen te herkennen van het gebruik van multi-agenten ten opzichte van een enkele agent.
- De bouwstenen van het implementeren van het multi-agent ontwerp patroon te begrijpen.

Wat is het grotere plaatje?

*Multi-agenten zijn een ontwerp patroon dat meerdere agenten in staat stelt samen te werken om een gemeenschappelijk doel te bereiken*.

Dit patroon wordt veel gebruikt in diverse velden, waaronder robotica, autonome systemen en gedistribueerde computing.

## Scenario's waar Multi-Agenten Toepasbaar Zijn

Dus welke scenario's zijn een goede use case voor het gebruik van multi-agenten? Het antwoord is dat er veel scenario's zijn waarin het inzetten van meerdere agenten voordelig is, vooral in de volgende gevallen:

- **Grote werklasten**: Grote werklasten kunnen worden verdeeld in kleinere taken en toegewezen aan verschillende agenten, wat parallelle verwerking en snellere voltooiing mogelijk maakt. Een voorbeeld hiervan is een grote dataverwerkingstaak.
- **Complexe taken**: Complexe taken, net als grote werklasten, kunnen worden opgesplitst in kleinere subtaken en toegewezen aan verschillende agenten, elk gespecialiseerd in een specifiek aspect van de taak. Een goed voorbeeld hiervan is bij autonome voertuigen waar verschillende agenten navigatie, obstakeldetectie en communicatie met andere voertuigen beheren.
- **Diverse expertise**: Verschillende agenten kunnen diverse expertise hebben, waardoor ze verschillende aspecten van een taak effectiever kunnen behandelen dan één enkele agent. Voor dit geval is een goed voorbeeld de gezondheidszorg waar agenten diagnoses, behandelplannen en patiëntmonitoring kunnen beheren.

## Voordelen van het Gebruiken van Multi-Agenten ten Opzichte van een Enkele Agent

Een enkel agent systeem kan goed werken voor eenvoudige taken, maar voor complexere taken kan het gebruik van meerdere agenten verschillende voordelen bieden:

- **Specialisatie**: Elke agent kan zijn gespecialiseerd in een specifieke taak. Een gebrek aan specialisatie in een enkele agent betekent dat je een agent hebt die alles kan doen, maar mogelijk verward raakt over wat te doen bij een complexe taak. Het kan bijvoorbeeld eindigen met het uitvoeren van een taak waarvoor het niet het best geschikt is.
- **Schaalbaarheid**: Het is makkelijker om systemen te schalen door meer agenten toe te voegen dan door één enkele agent te overladen.
- **Fouttolerantie**: Als één agent faalt, kunnen anderen blijven functioneren, wat de betrouwbaarheid van het systeem waarborgt.

Laten we een voorbeeld nemen: we boeken een reis voor een gebruiker. Een enkel agent systeem zou alle aspecten van het boekingsproces van een reis moeten afhandelen, van het vinden van vluchten tot het boeken van hotels en huurauto's. Om dit met één enkele agent te bereiken, zou de agent over tools moeten beschikken om al deze taken te beheren. Dit kan leiden tot een complex en monolithisch systeem dat moeilijk te onderhouden en te schalen is. Een multi-agent systeem kan daarentegen verschillende agenten hebben die gespecialiseerd zijn in het vinden van vluchten, het boeken van hotels en huurauto's. Dit maakt het systeem modulair, makkelijker te onderhouden en schaalbaar.

Vergelijk dit met een reisbureau dat als een buurtwinkel wordt gerund versus een reisbureau dat als franchise wordt gerund. De buurtwinkel zou één enkele agent hebben die alle aspecten van het boekingsproces afhandelt, terwijl de franchise verschillende agenten heeft die verschillende aspecten van het boekingsproces afhandelen.

## Bouwstenen van het Implementeren van het Multi-Agent Ontwerp Patroon

Voordat je het multi-agent ontwerp patroon kunt implementeren, moet je de bouwstenen begrijpen die het patroon vormen.

Laten we dit concreter maken door weer te kijken naar het voorbeeld van het boeken van een reis voor een gebruiker. In dit geval zouden de bouwstenen het volgende omvatten:

- **Agent Communicatie**: Agenten voor het vinden van vluchten, het boeken van hotels en huurauto's moeten communiceren en informatie delen over de voorkeuren en beperkingen van de gebruiker. Je moet beslissen over de protocollen en methodes voor deze communicatie. Wat dit concreet betekent is dat de agent voor het vinden van vluchten communiceert met de agent voor het boeken van hotels om er zeker van te zijn dat het hotel geboekt wordt voor dezelfde data als de vlucht. Dat betekent dat de agenten informatie over de reisdata van de gebruiker moeten delen, wat betekent dat je moet beslissen *welke agenten informatie delen en hoe ze die informatie delen*.
- **Coördinatiemechanismen**: Agenten moeten hun acties coördineren om te zorgen dat de voorkeuren en beperkingen van de gebruiker worden gerespecteerd. Een gebruikersvoorkeur kan zijn dat ze een hotel dicht bij de luchthaven willen, terwijl een beperking kan zijn dat huurauto's alleen bij de luchthaven beschikbaar zijn. Dit betekent dat de agent voor het boeken van hotels moet coördineren met de agent voor het boeken van huurauto's om te zorgen dat de voorkeuren en beperkingen van de gebruiker worden nageleefd. Dit betekent dat je moet beslissen *hoe de agenten hun acties coördineren*.
- **Agent Architectuur**: Agenten moeten een interne structuur hebben om beslissingen te nemen en te leren van hun interacties met de gebruiker. Dit betekent dat de agent voor het vinden van vluchten een interne structuur moet hebben om beslissingen te nemen over welke vluchten aan de gebruiker worden aanbevolen. Dit betekent dat je moet beslissen *hoe de agenten beslissingen nemen en leren van hun interacties met de gebruiker*. Voorbeelden van hoe een agent leert en verbetert kunnen zijn dat de agent voor het vinden van vluchten een machine learning model gebruikt om vluchten aan te bevelen op basis van eerder getoonde voorkeuren.
- **Zichtbaarheid in Multi-Agent Interacties**: Je moet zicht hebben op hoe de meerder agenten met elkaar interacteren. Dit betekent dat je tools en technieken moet gebruiken voor het volgen van agent activiteiten en interacties. Dit kan in de vorm van loggen en monitoring tools, visualisatie tools en prestatie-indicatoren zijn.
- **Multi-agent Patronen**: Er zijn verschillende patronen voor het implementeren van multi-agent systemen, zoals gecentraliseerde, gedecentraliseerde en hybride architecturen. Je moet het patroon kiezen dat het beste past bij jouw gebruikssituatie.
- **Mens in de lus**: In de meeste gevallen zal er een mens in de lus zijn en moet je de agenten instrueren wanneer ze om menselijke interventie moeten vragen. Dit kan in de vorm van een gebruiker die vraagt om een specifiek hotel of vlucht die de agenten niet hebben aanbevolen, of om bevestiging voordat een vlucht of hotel geboekt wordt.

## Zichtbaarheid in Multi-Agent Interacties

Het is belangrijk dat je zicht hebt op hoe de meerdere agenten met elkaar interacteren. Deze zichtbaarheid is essentieel voor het debuggen, optimaliseren en waarborgen van de effectiviteit van het gehele systeem. Om dit te bereiken, moet je tools en technieken hebben om agent activiteiten en interacties te volgen. Dit kan in de vorm van logging- en monitoringtools, visualisatie tools en prestatie-indicatoren.

Bijvoorbeeld, in het geval van het boeken van een reis voor een gebruiker, kun je een dashboard hebben dat de status van elke agent toont, de voorkeuren en beperkingen van de gebruiker en de interacties tussen agenten. Dit dashboard kan de reisdata van de gebruiker tonen, de vluchten die door de vluchtagent zijn aanbevolen, de hotels die door de hotelagent zijn aanbevolen en de huurauto's die door de huurauto-agent zijn aanbevolen. Dit geeft je een duidelijk beeld van hoe de agenten met elkaar interacteren en of de voorkeuren en beperkingen van de gebruiker worden nageleefd.

Laten we elk van deze aspecten wat gedetailleerder bekijken.

- **Logging- en Monitoring Tools**: Je wilt voor elke actie die een agent neemt logging hebben. Een logvermelding kan informatie opslaan over welke agent de actie heeft uitgevoerd, welke actie, het tijdstip van uitvoeren en het resultaat van de actie. Deze informatie kan vervolgens worden gebruikt voor debugging, optimalisatie en meer.

- **Visualisatie Tools**: Visualisatie tools kunnen je helpen de interacties tussen agenten op een intuïtievere manier te zien. Zo kun je bijvoorbeeld een grafiek hebben die de informatiestroom tussen agenten toont. Dit kan je helpen knelpunten, inefficiënties en andere problemen in het systeem te identificeren.

- **Prestatie-Indicatoren**: Prestatie-indicatoren kunnen je helpen de effectiviteit van het multi-agent systeem te volgen. Je kunt bijvoorbeeld de tijd volgen die nodig is om een taak te voltooien, het aantal voltooide taken per tijdseenheid en de nauwkeurigheid van de aanbevelingen die door de agenten worden gedaan. Deze informatie kan je helpen verbeterpunten te identificeren en het systeem te optimaliseren.

## Multi-Agent Patronen

Laten we enkele concrete patronen bekijken die we kunnen gebruiken om multi-agent apps te maken. Hier zijn een paar interessante patronen die het overwegen waard zijn:

### Groepschat

Dit patroon is nuttig wanneer je een groepschat applicatie wilt maken waar meerdere agenten met elkaar kunnen communiceren. Typische gebruikssituaties voor dit patroon zijn team samenwerking, klantenondersteuning en sociale netwerken.

In dit patroon vertegenwoordigt elke agent een gebruiker in de groepschat en worden berichten tussen agenten uitgewisseld via een messaging protocol. De agenten kunnen berichten naar de groepschat sturen, berichten van de groepschat ontvangen en reageren op berichten van andere agenten.

Dit patroon kan worden geïmplementeerd met een gecentraliseerde architectuur waarbij alle berichten via een centrale server lopen, of een gedecentraliseerde architectuur waar berichten direct worden uitgewisseld.

![Groepschat](../../../translated_images/nl/multi-agent-group-chat.ec10f4cde556babd.webp)

### Overdracht

Dit patroon is nuttig wanneer je een applicatie wilt maken waarin meerdere agenten taken aan elkaar kunnen overdragen.

Typische gebruikssituaties voor dit patroon zijn klantenondersteuning, taakbeheer en workflow automatisering.

In dit patroon vertegenwoordigt elke agent een taak of een stap in een workflow, en kunnen agenten taken overdragen aan andere agenten op basis van vooraf gedefinieerde regels.

![Overdracht](../../../translated_images/nl/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Collaboratieve filtering

Dit patroon is nuttig wanneer je een applicatie wilt maken waarin meerdere agenten samenwerken om aanbevelingen aan gebruikers te doen.

Waarom je meerdere agenten samen wilt laten werken, is omdat elke agent andere expertise kan hebben en kan bijdragen aan het aanbevelingsproces op verschillende manieren.

Laten we een voorbeeld nemen waarin een gebruiker een aanbeveling wil voor het beste aandeel om te kopen op de aandelenmarkt.

- **Industrie-expert**: Eén agent kan expert zijn in een specifieke industrie.
- **Technische analyse**: Een andere agent kan expert zijn in technische analyse.
- **Fundamentele analyse**: en weer een andere agent kan expert zijn in fundamentele analyse. Door samen te werken, kunnen deze agenten een meer uitgebreide aanbeveling aan de gebruiker geven.

![Aanbeveling](../../../translated_images/nl/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Terugbetalingsproces

Overweeg een scenario waarbij een klant probeert een terugbetaling te krijgen voor een product, er kunnen nogal wat agenten betrokken zijn bij dit proces maar laten we het verdelen tussen agenten specifiek voor dit proces en algemene agenten die voor andere processen gebruikt kunnen worden.

**Agenten specifiek voor het terugbetalingsproces**:

Hier volgen enkele agenten die betrokken kunnen zijn bij het terugbetalingsproces:

- **Klantagent**: Deze agent vertegenwoordigt de klant en is verantwoordelijk voor het initiëren van het terugbetalingsproces.
- **Verkoperagent**: Deze agent vertegenwoordigt de verkoper en is verantwoordelijk voor het verwerken van de terugbetaling.
- **Betaalagent**: Deze agent vertegenwoordigt het betaalproces en is verantwoordelijk voor het terugbetalen van de betaling aan de klant.
- **Oplossingsagent**: Deze agent vertegenwoordigt het oplossingsproces en is verantwoordelijk voor het oplossen van problemen die zich voordoen tijdens het terugbetalingsproces.
- **Compliance agent**: Deze agent vertegenwoordigt het compliance proces en is verantwoordelijk voor het waarborgen dat het terugbetalingsproces voldoet aan regelgeving en beleid.

**Algemene agenten**:

Deze agenten kunnen door andere delen van je bedrijf worden gebruikt.

- **Verzendagent**: Deze agent vertegenwoordigt het verzendproces en is verantwoordelijk voor het terugsturen van het product naar de verkoper. Deze agent kan zowel voor het terugbetalingsproces als voor algemene verzending van een product via een aankoop worden gebruikt.
- **Feedback agent**: Deze agent vertegenwoordigt het feedbackproces en is verantwoordelijk voor het verzamelen van feedback van de klant. Feedback kan op elk moment worden gevraagd en niet alleen tijdens het terugbetalingsproces.
- **Escalatie agent**: Deze agent vertegenwoordigt het escalatieproces en is verantwoordelijk voor het escaleren van problemen naar een hoger serviceniveau. Je kunt dit type agent gebruiken voor elk proces waarbij je een probleem moet escaleren.
- **Notificatie agent**: Deze agent vertegenwoordigt het notificatieproces en is verantwoordelijk voor het verzenden van meldingen aan de klant op verschillende stadia van het terugbetalingsproces.
- **Analytics agent**: Deze agent vertegenwoordigt het analyseproces en is verantwoordelijk voor het analyseren van data gerelateerd aan het terugbetalingsproces.
- **Audit agent**: Deze agent vertegenwoordigt het audit proces en is verantwoordelijk voor het controleren van het terugbetalingsproces om te zorgen dat het correct wordt uitgevoerd.
- **Rapportage agent**: Deze agent vertegenwoordigt het rapportageproces en is verantwoordelijk voor het genereren van rapporten over het terugbetalingsproces.
- **Kennis agent**: Deze agent vertegenwoordigt het kennisproces en is verantwoordelijk voor het onderhouden van een kennisbank met informatie gerelateerd aan het terugbetalingsproces. Deze agent kan deskundig zijn zowel in terugbetalingen als andere delen van je bedrijf.
- **Beveiligingsagent**: Deze agent vertegenwoordigt het beveiligingsproces en is verantwoordelijk voor het waarborgen van de beveiliging van het terugbetalingsproces.
- **Kwaliteitsagent**: Deze agent vertegenwoordigt het kwaliteitsproces en is verantwoordelijk voor het garanderen van de kwaliteit van het terugbetalingsproces.

Er zijn behoorlijk wat agenten hierboven genoemd zowel voor het specifieke terugbetalingsproces als ook voor de algemene agenten die in andere delen van je bedrijf kunnen worden gebruikt. Hopelijk geeft dit je een idee over hoe je kunt beslissen welke agenten je gebruikt in je multi-agent systeem.

## Opdracht

Ontwerp een multi-agent systeem voor een klantenondersteuningsproces. Identificeer de agenten die bij het proces betrokken zijn, hun rollen en verantwoordelijkheden, en hoe ze met elkaar interacteren. Overweeg zowel agenten specifiek voor het klantenondersteuningsproces als algemene agenten die in andere delen van je bedrijf kunnen worden gebruikt.
> Denk goed na voordat je de volgende oplossing leest, je hebt mogelijk meer agenten nodig dan je denkt.

> TIP: Denk aan de verschillende fasen van het klantenondersteuningsproces en overweeg ook agenten die nodig zijn voor elk systeem.

## Oplossing

[Oplossing](./solution/solution.md)

## Kenniscontroles

Vraag: Wanneer moet je overwegen om multi-agenten te gebruiken?

- [ ] A1: Wanneer je een kleine werklast en een eenvoudige taak hebt.
- [ ] A2: Wanneer je een grote werklast hebt.
- [ ] A3: Wanneer je een eenvoudige taak hebt.

[Oplossing quiz](./solution/solution-quiz.md)

## Samenvatting

In deze les hebben we gekeken naar het multi-agent ontwerp patroon, inclusief de scenario's waarin multi-agenten toepasbaar zijn, de voordelen van het gebruik van multi-agenten ten opzichte van één enkele agent, de bouwstenen voor het implementeren van het multi-agent ontwerp patroon, en hoe je zicht krijgt op hoe de meerdere agenten met elkaar samenwerken.

### Meer vragen over het Multi-Agent Ontwerp Patroon?

Word lid van de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, kantooruren bij te wonen en je vragen over AI-agenten beantwoord te krijgen.

## Aanvullende bronnen

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework documentatie</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentic ontwerp patronen</a>

## Vorige les

[Planning Ontwerp](../07-planning-design/README.md)

## Volgende les

[Metacognitie in AI-agenten](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vrijwaring**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, kan het zijn dat geautomatiseerde vertalingen fouten of onjuistheden bevatten. Het oorspronkelijke document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties voortvloeiend uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->