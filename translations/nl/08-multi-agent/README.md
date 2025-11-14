<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T17:24:26+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "nl"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.nl.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Multi-agent ontwerp patronen

Zodra je begint te werken aan een project met meerdere agents, moet je rekening houden met het multi-agent ontwerp patroon. Het is echter niet altijd meteen duidelijk wanneer je moet overstappen naar multi-agents en wat de voordelen zijn.

## Introductie

In deze les proberen we de volgende vragen te beantwoorden:

- Wat zijn de scenario's waarin multi-agents toepasbaar zijn?
- Wat zijn de voordelen van het gebruik van multi-agents in plaats van één enkele agent die meerdere taken uitvoert?
- Wat zijn de bouwstenen voor het implementeren van het multi-agent ontwerp patroon?
- Hoe krijgen we inzicht in hoe de verschillende agents met elkaar interageren?

## Leerdoelen

Na deze les zou je in staat moeten zijn om:

- Scenario's te identificeren waarin multi-agents toepasbaar zijn.
- De voordelen van het gebruik van multi-agents boven een enkele agent te herkennen.
- De bouwstenen van het implementeren van het multi-agent ontwerp patroon te begrijpen.

Wat is het grotere geheel?

*Multi-agents zijn een ontwerp patroon waarmee meerdere agents kunnen samenwerken om een gemeenschappelijk doel te bereiken.*

Dit patroon wordt veel gebruikt in verschillende gebieden, waaronder robotica, autonome systemen en gedistribueerde computing.

## Scenario's waarin Multi-Agents toepasbaar zijn

Dus, wat zijn goede gebruiksscenario's voor het gebruik van multi-agents? Het antwoord is dat er veel scenario's zijn waarin het inzetten van meerdere agents voordelig is, vooral in de volgende gevallen:

- **Grote werklast**: Grote werklasten kunnen worden opgedeeld in kleinere taken en toegewezen aan verschillende agents, waardoor parallelle verwerking en snellere voltooiing mogelijk zijn. Een voorbeeld hiervan is een grote dataverwerkingstaak.
- **Complexe taken**: Complexe taken, net als grote werklasten, kunnen worden opgesplitst in kleinere subtaken en toegewezen aan verschillende agents, die elk gespecialiseerd zijn in een specifiek aspect van de taak. Een goed voorbeeld hiervan is bij autonome voertuigen, waar verschillende agents navigatie, obstakeldetectie en communicatie met andere voertuigen beheren.
- **Diverse expertise**: Verschillende agents kunnen diverse expertise hebben, waardoor ze verschillende aspecten van een taak effectiever kunnen aanpakken dan een enkele agent. Een goed voorbeeld hiervan is in de gezondheidszorg, waar agents diagnostiek, behandelplannen en patiëntmonitoring kunnen beheren.

## Voordelen van het gebruik van Multi-Agents boven een enkele agent

Een systeem met één agent kan goed werken voor eenvoudige taken, maar voor meer complexe taken kan het gebruik van meerdere agents verschillende voordelen bieden:

- **Specialisatie**: Elke agent kan gespecialiseerd zijn in een specifieke taak. Gebrek aan specialisatie in een enkele agent betekent dat je een agent hebt die alles kan doen, maar die in de war kan raken bij complexe taken. Het kan bijvoorbeeld een taak uitvoeren waarvoor het niet het meest geschikt is.
- **Schaalbaarheid**: Het is gemakkelijker om systemen te schalen door meer agents toe te voegen dan door een enkele agent te overbelasten.
- **Fouttolerantie**: Als één agent faalt, kunnen anderen blijven functioneren, wat zorgt voor systeem betrouwbaarheid.

Laten we een voorbeeld nemen: stel dat we een reis voor een gebruiker willen boeken. Een systeem met één agent zou alle aspecten van het reisboekingsproces moeten afhandelen, van het vinden van vluchten tot het boeken van hotels en huurauto's. Om dit te bereiken met één agent, zou de agent tools nodig hebben om al deze taken te beheren. Dit kan leiden tot een complex en monolithisch systeem dat moeilijk te onderhouden en te schalen is. Een multi-agent systeem daarentegen kan verschillende agents hebben die gespecialiseerd zijn in het vinden van vluchten, het boeken van hotels en huurauto's. Dit zou het systeem meer modulair, gemakkelijker te onderhouden en schaalbaar maken.

Vergelijk dit met een reisbureau dat wordt gerund als een familiebedrijf versus een reisbureau dat wordt gerund als een franchise. Het familiebedrijf zou een enkele agent hebben die alle aspecten van het reisboekingsproces afhandelt, terwijl de franchise verschillende agents zou hebben die verschillende aspecten van het reisboekingsproces afhandelen.

## Bouwstenen voor het implementeren van het Multi-Agent Ontwerp Patroon

Voordat je het multi-agent ontwerp patroon kunt implementeren, moet je de bouwstenen begrijpen die het patroon vormen.

Laten we dit concreet maken door opnieuw te kijken naar het voorbeeld van het boeken van een reis voor een gebruiker. In dit geval zouden de bouwstenen zijn:

- **Agentcommunicatie**: Agents voor het vinden van vluchten, het boeken van hotels en huurauto's moeten communiceren en informatie delen over de voorkeuren en beperkingen van de gebruiker. Je moet beslissen over de protocollen en methoden voor deze communicatie. Concreet betekent dit dat de agent voor het vinden van vluchten moet communiceren met de agent voor het boeken van hotels om ervoor te zorgen dat het hotel wordt geboekt voor dezelfde data als de vlucht. Dat betekent dat de agents informatie moeten delen over de reisdata van de gebruiker, wat betekent dat je moet beslissen *welke agents informatie delen en hoe ze informatie delen*.
- **Coördinatiemechanismen**: Agents moeten hun acties coördineren om ervoor te zorgen dat de voorkeuren en beperkingen van de gebruiker worden nageleefd. Een gebruikersvoorkeur kan zijn dat ze een hotel dicht bij de luchthaven willen, terwijl een beperking kan zijn dat huurauto's alleen beschikbaar zijn op de luchthaven. Dit betekent dat de agent voor het boeken van hotels moet coördineren met de agent voor het boeken van huurauto's om ervoor te zorgen dat de voorkeuren en beperkingen van de gebruiker worden nageleefd. Dit betekent dat je moet beslissen *hoe de agents hun acties coördineren*.
- **Agentarchitectuur**: Agents moeten een interne structuur hebben om beslissingen te nemen en te leren van hun interacties met de gebruiker. Dit betekent dat de agent voor het vinden van vluchten een interne structuur moet hebben om beslissingen te nemen over welke vluchten aan de gebruiker worden aanbevolen. Dit betekent dat je moet beslissen *hoe de agents beslissingen nemen en leren van hun interacties met de gebruiker*. Voorbeelden van hoe een agent leert en verbetert, kunnen zijn dat de agent voor het vinden van vluchten een machine learning-model gebruikt om vluchten aan de gebruiker aan te bevelen op basis van hun eerdere voorkeuren.
- **Inzicht in Multi-Agent Interacties**: Je moet inzicht hebben in hoe de verschillende agents met elkaar interageren. Dit betekent dat je tools en technieken nodig hebt om agentactiviteiten en interacties te volgen. Dit kan in de vorm zijn van log- en monitoringtools, visualisatietools en prestatiestatistieken.
- **Multi-Agent Patronen**: Er zijn verschillende patronen voor het implementeren van multi-agent systemen, zoals gecentraliseerde, gedecentraliseerde en hybride architecturen. Je moet beslissen welk patroon het beste past bij jouw gebruikssituatie.
- **Mens in de lus**: In de meeste gevallen zal er een mens in de lus zijn en moet je de agents instrueren wanneer ze om menselijke tussenkomst moeten vragen. Dit kan in de vorm zijn van een gebruiker die vraagt om een specifiek hotel of vlucht die de agents niet hebben aanbevolen, of om bevestiging vraagt voordat een vlucht of hotel wordt geboekt.

## Inzicht in Multi-Agent Interacties

Het is belangrijk dat je inzicht hebt in hoe de verschillende agents met elkaar interageren. Dit inzicht is essentieel voor debugging, optimalisatie en het waarborgen van de effectiviteit van het algehele systeem. Om dit te bereiken, heb je tools en technieken nodig om agentactiviteiten en interacties te volgen. Dit kan in de vorm zijn van log- en monitoringtools, visualisatietools en prestatiestatistieken.

Bijvoorbeeld, in het geval van het boeken van een reis voor een gebruiker, zou je een dashboard kunnen hebben dat de status van elke agent, de voorkeuren en beperkingen van de gebruiker, en de interacties tussen agents toont. Dit dashboard zou de reisdata van de gebruiker, de vluchten aanbevolen door de vluchtagent, de hotels aanbevolen door de hotelagent, en de huurauto's aanbevolen door de huurautoagent kunnen tonen. Dit zou je een duidelijk beeld geven van hoe de agents met elkaar interageren en of de voorkeuren en beperkingen van de gebruiker worden nageleefd.

Laten we elk van deze aspecten meer in detail bekijken.

- **Log- en Monitoringtools**: Je wilt logging uitvoeren voor elke actie die door een agent wordt ondernomen. Een logvermelding kan informatie opslaan over de agent die de actie heeft ondernomen, de actie die is ondernomen, het tijdstip waarop de actie is ondernomen en het resultaat van de actie. Deze informatie kan vervolgens worden gebruikt voor debugging, optimalisatie en meer.

- **Visualisatietools**: Visualisatietools kunnen je helpen de interacties tussen agents op een meer intuïtieve manier te zien. Bijvoorbeeld, je zou een grafiek kunnen hebben die de informatiestroom tussen agents toont. Dit kan je helpen knelpunten, inefficiënties en andere problemen in het systeem te identificeren.

- **Prestatiestatistieken**: Prestatiestatistieken kunnen je helpen de effectiviteit van het multi-agent systeem te volgen. Bijvoorbeeld, je zou de tijd kunnen volgen die nodig is om een taak te voltooien, het aantal taken dat per tijdseenheid wordt voltooid, en de nauwkeurigheid van de aanbevelingen die door de agents worden gedaan. Deze informatie kan je helpen gebieden voor verbetering te identificeren en het systeem te optimaliseren.

## Multi-Agent Patronen

Laten we enkele concrete patronen bekijken die we kunnen gebruiken om multi-agent apps te maken. Hier zijn enkele interessante patronen die het overwegen waard zijn:

### Groepschat

Dit patroon is nuttig wanneer je een groepschat applicatie wilt maken waarin meerdere agents met elkaar kunnen communiceren. Typische gebruiksscenario's voor dit patroon zijn team samenwerking, klantenondersteuning en sociale netwerken.

In dit patroon vertegenwoordigt elke agent een gebruiker in de groepschat, en berichten worden uitgewisseld tussen agents met behulp van een berichtenprotocol. De agents kunnen berichten naar de groepschat sturen, berichten van de groepschat ontvangen en reageren op berichten van andere agents.

Dit patroon kan worden geïmplementeerd met behulp van een gecentraliseerde architectuur waarbij alle berichten via een centrale server worden gerouteerd, of een gedecentraliseerde architectuur waarbij berichten rechtstreeks worden uitgewisseld.

![Groepschat](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.nl.png)

### Overdracht

Dit patroon is nuttig wanneer je een applicatie wilt maken waarin meerdere agents taken aan elkaar kunnen overdragen.

Typische gebruiksscenario's voor dit patroon zijn klantenondersteuning, taakbeheer en workflow automatisering.

In dit patroon vertegenwoordigt elke agent een taak of een stap in een workflow, en agents kunnen taken aan andere agents overdragen op basis van vooraf gedefinieerde regels.

![Overdracht](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.nl.png)

### Collaboratief filteren

Dit patroon is nuttig wanneer je een applicatie wilt maken waarin meerdere agents kunnen samenwerken om aanbevelingen aan gebruikers te doen.

Waarom je zou willen dat meerdere agents samenwerken, is omdat elke agent verschillende expertise kan hebben en op verschillende manieren kan bijdragen aan het aanbevelingsproces.

Laten we een voorbeeld nemen waarin een gebruiker een aanbeveling wil over de beste aandelen om te kopen op de aandelenmarkt.

- **Industrie-expert**: Eén agent kan een expert zijn in een specifieke industrie.
- **Technische analyse**: Een andere agent kan een expert zijn in technische analyse.
- **Fundamentele analyse**: En een andere agent kan een expert zijn in fundamentele analyse. Door samen te werken, kunnen deze agents een meer uitgebreide aanbeveling aan de gebruiker geven.

![Aanbeveling](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.nl.png)

## Scenario: Terugbetalingsproces

Overweeg een scenario waarin een klant probeert een terugbetaling te krijgen voor een product. Er kunnen behoorlijk wat agents betrokken zijn bij dit proces, maar laten we het verdelen tussen agents die specifiek zijn voor dit proces en algemene agents die in andere processen kunnen worden gebruikt.

**Agents specifiek voor het terugbetalingsproces**:

De volgende agents kunnen betrokken zijn bij het terugbetalingsproces:

- **Klantagent**: Deze agent vertegenwoordigt de klant en is verantwoordelijk voor het starten van het terugbetalingsproces.
- **Verkoperagent**: Deze agent vertegenwoordigt de verkoper en is verantwoordelijk voor het verwerken van de terugbetaling.
- **Betalingsagent**: Deze agent vertegenwoordigt het betalingsproces en is verantwoordelijk voor het terugbetalen van de betaling van de klant.
- **Resolutieagent**: Deze agent vertegenwoordigt het resolutieproces en is verantwoordelijk voor het oplossen van eventuele problemen die zich voordoen tijdens het terugbetalingsproces.
- **Complianceagent**: Deze agent vertegenwoordigt het complianceproces en is verantwoordelijk voor het waarborgen dat het terugbetalingsproces voldoet aan regelgeving en beleid.

**Algemene agents**:

Deze agents kunnen worden gebruikt door andere delen van je bedrijf.

- **Verzendagent**: Deze agent vertegenwoordigt het verzendproces en is verantwoordelijk voor het terugsturen van het product naar de verkoper. Deze agent kan zowel worden gebruikt voor het terugbetalingsproces als voor algemene verzending van een product, bijvoorbeeld bij een aankoop.
- **Feedbackagent**: Deze agent vertegenwoordigt het feedbackproces en is verantwoordelijk voor het verzamelen van feedback van de klant. Feedback kan op elk moment worden verzameld en niet alleen tijdens het terugbetalingsproces.
- **Escalatieagent**: Deze agent vertegenwoordigt het escalatieproces en is verantwoordelijk voor het escaleren van problemen naar een hoger niveau van ondersteuning. Je kunt dit type agent gebruiken voor elk proces waarin je een probleem moet escaleren.
- **Notificatieagent**: Deze agent vertegenwoordigt het notificatieproces en is verantwoordelijk voor het verzenden van notificaties naar de klant in verschillende stadia van het terugbetalingsproces.
- **Analyticsagent**: Deze agent vertegenwoordigt het analyticsproces en is verantwoordelijk voor het analyseren van gegevens met betrekking tot het terugbetalingsproces.
- **Auditagent**: Deze agent vertegenwoordigt het auditproces en is verantwoordelijk voor het auditen van het terugbetalingsproces om ervoor te zorgen dat het correct wordt uitgevoerd.
- **Rapportageagent**: Deze agent vertegenwoordigt het rapportageproces en is verantwoordelijk voor het genereren van rapporten over het terugbetalingsproces.
- **Kennisagent**: Deze agent vertegenwoordigt het kennisproces en is verantwoordelijk voor het onderhouden van een kennisbank met informatie met betrekking tot het terugbetalingsproces. Deze agent kan zowel kennis hebben over terugbetalingen als andere delen van je bedrijf.
- **Beveiligingsagent**: Deze agent vertegenwoordigt het beveiligingsproces en is verantwoordelijk voor het waarborgen van de beveiliging van het terugbetalingsproces.
- **Kwaliteitsagent**: Deze agent vertegenwoordigt het kwaliteitsproces en is verantwoordelijk voor het waarborgen van de kwaliteit van het terugbetalingsproces.

Er zijn behoorlijk wat agents genoemd, zowel voor het specifieke terugbetalingsproces als voor de algemene agents die in andere delen van je bedrijf kunnen worden gebruikt. Hopelijk geeft dit je een idee van hoe je kunt beslissen welke agents je wilt gebruiken in je multi-agent systeem.

## Opdracht
## Ontwerp een multi-agent systeem voor een klantenondersteuningsproces. Identificeer de betrokken agents in het proces, hun rollen en verantwoordelijkheden, en hoe ze met elkaar samenwerken. Overweeg zowel agents die specifiek zijn voor het klantenondersteuningsproces als algemene agents die in andere delen van je bedrijf kunnen worden gebruikt.

> Denk goed na voordat je de onderstaande oplossing leest, je hebt misschien meer agents nodig dan je denkt.

> TIP: Denk aan de verschillende fasen van het klantenondersteuningsproces en overweeg ook agents die nodig zijn voor elk systeem.

## Oplossing

[Oplossing](./solution/solution.md)

## Kennisvragen

Vraag: Wanneer moet je overwegen om multi-agents te gebruiken?

- [ ] A1: Wanneer je een kleine werklast en een eenvoudige taak hebt.
- [ ] A2: Wanneer je een grote werklast hebt.
- [ ] A3: Wanneer je een eenvoudige taak hebt.

[Oplossing quiz](./solution/solution-quiz.md)

## Samenvatting

In deze les hebben we gekeken naar het multi-agent ontwerpmodel, inclusief de scenario's waarin multi-agents toepasbaar zijn, de voordelen van het gebruik van multi-agents ten opzichte van een enkele agent, de bouwstenen voor het implementeren van het multi-agent ontwerpmodel, en hoe je inzicht kunt krijgen in hoe de verschillende agents met elkaar samenwerken.

### Meer vragen over het Multi-Agent Ontwerpmodel?

Word lid van de [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, spreekuren bij te wonen en je vragen over AI Agents beantwoord te krijgen.

## Aanvullende bronnen

## Vorige Les

[Planning Ontwerp](../07-planning-design/README.md)

## Volgende Les

[Metacognitie in AI Agents](../09-metacognition/README.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.