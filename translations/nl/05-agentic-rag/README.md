[![Agentic RAG](../../../translated_images/nl/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Agentic RAG

Deze les geeft een uitgebreid overzicht van Agentic Retrieval-Augmented Generation (Agentic RAG), een opkomend AI-paradigma waarbij grote taalmodellen (LLM's) autonoom hun volgende stappen plannen terwijl ze informatie uit externe bronnen halen. In tegenstelling tot statische retrieval-en-then-lees patronen omvat Agentic RAG iteratieve oproepen naar de LLM, afgewisseld met tools- of functieverzoeken en gestructureerde outputs. Het systeem evalueert resultaten, verfijnt queries, roept indien nodig extra tools aan en zet deze cyclus voort tot een bevredigende oplossing is bereikt.

## Introductie

In deze les behandelen we

- **Begrijp Agentic RAG:** Leer over het opkomende paradigma in AI waarbij grote taalmodellen (LLM's) autonoom hun volgende stappen plannen terwijl ze informatie uit externe databronnen halen.
- **Begrijp Iteratieve Maker-Checker Stijl:** Begrijp de lus van iteratieve oproepen naar de LLM, afgewisseld met tool- of functieverzoeken en gestructureerde outputs, ontworpen om correctheid te verbeteren en verkeerd gevormde queries af te handelen.
- **Ontdek Praktische Toepassingen:** Identificeer scenario's waarin Agentic RAG uitblinkt, zoals omgevingen die correctheid prioriteren, complexe database-interacties en uitgebreide workflows.

## Leerdoelen

Na het voltooien van deze les weet je hoe/begrijp je:

- **Begrijpen van Agentic RAG:** Leer over het opkomende paradigma in AI waarbij grote taalmodellen (LLM's) autonoom hun volgende stappen plannen terwijl ze informatie uit externe databronnen halen.
- **Iteratieve Maker-Checker Stijl:** Begrijp het concept van een lus van iteratieve oproepen naar de LLM, afgewisseld met tool- of functieverzoeken en gestructureerde outputs, ontworpen om correctheid te verbeteren en verkeerd gevormde queries af te handelen.
- **Eigenaar zijn van het Redeneringsproces:** Begrijp het vermogen van het systeem om eigenaar te zijn van zijn redeneringsproces, waarbij het beslissingen neemt over hoe het problemen aanpakt zonder te vertrouwen op vooraf gedefinieerde paden.
- **Workflow:** Begrijp hoe een agentisch model zelfstandig beslist om markttrendrapporten op te halen, concurrentgegevens te identificeren, interne verkoopstatistieken te correleren, bevindingen te synthetiseren en de strategie te evalueren.
- **Iteratieve Lussen, Tool-Integratie en Geheugen:** Leer over het vertrouwen van het systeem op een gelust interactiepatroon, waarbij status en geheugen worden onderhouden over stappen heen om herhalende lussen te vermijden en geïnformeerde beslissingen te nemen.
- **Omgaan met Foutmodi en Zelfcorrectie:** Ontdek de robuuste zelfcorrectiemechanismen van het systeem, inclusief itereren en opnieuw query'en, het gebruik van diagnostische tools en terugvallen op menselijke supervisie.
- **Beperkingen van Agentie:** Begrijp de beperkingen van Agentic RAG, met focus op domeinspecifieke autonomie, afhankelijkheid van infrastructuur en respect voor veiligheidsmaatregelen.
- **Praktische Gebruikssituaties en Waarde:** Identificeer scenario's waarin Agentic RAG uitblinkt, zoals omgevingen die correctheid prioriteren, complexe database-interacties en uitgebreide workflows.
- **Bestuur, Transparantie en Vertrouwen:** Leer over het belang van bestuur en transparantie, inclusief verklaarbare redenering, beheersing van vooroordelen en menselijke supervisie.

## Wat is Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) is een opkomend AI-paradigma waarbij grote taalmodellen (LLM's) autonoom hun volgende stappen plannen terwijl ze informatie uit externe bronnen halen. In tegenstelling tot statische retrieval-en-then-lees patronen omvat Agentic RAG iteratieve oproepen naar de LLM, afgewisseld met tool- of functieverzoeken en gestructureerde outputs. Het systeem evalueert resultaten, verfijnt queries, roept indien nodig extra tools aan en zet deze cyclus voort tot een bevredigende oplossing is bereikt. Deze iteratieve “maker-checker” stijl verbetert de correctheid, handelt verkeerd gevormde queries af en zorgt voor resultaten van hoge kwaliteit.

Het systeem beheert actief zijn redeneringsproces, herschrijft mislukte queries, kiest verschillende methoden voor informatieophaling en integreert meerdere tools—zoals vectorzoekopdrachten in Azure AI Search, SQL-databases, of aangepaste API's—voordat het zijn antwoord finaliseert. Het onderscheidende kenmerk van een agentisch systeem is het vermogen om eigenaar te zijn van zijn redeneringsproces. Traditionele RAG-implementaties vertrouwen op vooraf gedefinieerde paden, maar een agentisch systeem bepaalt autonoom de volgorde van stappen op basis van de kwaliteit van de gevonden informatie.

## Definitie van Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) is een opkomend paradigma in AI-ontwikkeling waarbij LLM's niet alleen informatie uit externe databronnen halen maar ook autonoom hun volgende stappen plannen. In tegenstelling tot statische retrieval-en-then-lees patronen of zorgvuldig gescripte promptsequenties, omvat Agentic RAG een lus van iteratieve oproepen naar de LLM, afgewisseld met tool- of functieverzoeken en gestructureerde outputs. Bij elke stap evalueert het systeem de verkregen resultaten, besluit het of het zijn queries moet verfijnen, roept het indien nodig extra tools aan en zet deze cyclus voort tot een bevredigende oplossing wordt bereikt.

Deze iteratieve “maker-checker” stijl van werken is ontworpen om correctheid te verbeteren, verkeerd gevormde queries naar gestructureerde databases aan te pakken (bijv. NL2SQL) en gebalanceerde, hoogwaardige resultaten te verzekeren. In plaats van alleen te vertrouwen op zorgvuldig ontworpen promptketens, beheert het systeem actief zijn redeneringsproces. Het kan queries herschrijven die mislukken, verschillende informatieophaaldmethoden kiezen en meerdere tools integreren—zoals vectorzoekopdrachten in Azure AI Search, SQL-databases of aangepaste API's—voordat het zijn antwoord finaliseert. Dit elimineert de noodzaak voor overdreven complexe orkestratiekaders. In plaats daarvan kan een relatief eenvoudige lus van “LLM-aanroep → tool-gebruik → LLM-aanroep → …” geavanceerde en goed onderbouwde outputs opleveren.

![Agentic RAG Core Loop](../../../translated_images/nl/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Eigenaar zijn van het Redeneringsproces

De onderscheidende eigenschap die een systeem “agentisch” maakt, is het vermogen om eigenaar te zijn van zijn redeneringsproces. Traditionele RAG-implementaties zijn vaak afhankelijk van mensen die een pad voor het model vooraf definiëren: een denkbeeldige keten die aangeeft wat wanneer moet worden opgehaald.
Maar wanneer een systeem echt agentisch is, beslist het intern hoe het het probleem benadert. Het voert niet alleen een script uit; het bepaalt autonoom de volgorde van stappen op basis van de kwaliteit van de gevonden informatie.
Bijvoorbeeld, als het wordt gevraagd een productlanceringsstrategie te creëren, vertrouwt het niet alleen op een prompt die de hele onderzoeks- en besluitvormingsworkflow uitwerkt. In plaats daarvan beslist het agentische model zelfstandig om:

1. Huidige markttrendrapporten op te halen met behulp van Bing Web Grounding
2. Relevante gegevens van concurrenten te identificeren met Azure AI Search.
3. Historische interne verkoopstatistieken te correleren met Azure SQL Database.
4. De bevindingen te synthetiseren tot een samenhangende strategie, georkestreerd via Azure OpenAI Service.
5. De strategie te evalueren op hiaten of inconsistenties, en indien nodig een nieuwe ronde van informatieophaling in te zetten.
Al deze stappen—queries verfijnen, bronnen kiezen, itereren tot het “tevreden” is met het antwoord—worden door het model beslist, niet vooraf door een mens gescript.

## Iteratieve Lussen, Tool-Integratie en Geheugen

![Tool Integration Architecture](../../../translated_images/nl/tool-integration.0f569710b5c17c10.webp)

Een agentisch systeem vertrouwt op een gelust interactiepatroon:

- **Initiële Aanroep:** Het doel van de gebruiker (ook wel gebruikersprompt genoemd) wordt gepresenteerd aan de LLM.
- **Tool-aanroep:** Als het model ontbrekende informatie of vage instructies constateert, selecteert het een tool of informatieophaalmethode—zoals een vector-database-query (bijv. Azure AI Search Hybrid-zoekopdracht over privégegevens) of een gestructureerde SQL-aanroep—om meer context te verzamelen.
- **Beoordeling & Verfijning:** Na het bekijken van de teruggegeven gegevens, beslist het model of de informatie voldoende is. Zo niet, dan verfijnt het de query, probeert een andere tool of past zijn aanpak aan.
- **Herhaal tot Tevredenheid:** Deze cyclus gaat door totdat het model bepaalt dat het genoeg duidelijkheid en bewijs heeft om een definitief, weloverwogen antwoord te geven.
- **Geheugen & Status:** Omdat het systeem status en geheugen over stappen heen behoudt, kan het eerdere pogingen en hun uitkomsten herinneren, waardoor herhaalde lussen worden vermeden en beter geïnformeerde beslissingen worden genomen terwijl het verder werkt.

In de loop der tijd creëert dit een gevoel van evoluerend begrip, waardoor het model complexe, meervoudige stap-taken kan navigeren zonder dat een mens constant hoeft in te grijpen of de prompt opnieuw hoeft vorm te geven.

## Omgaan met Foutmodi en Zelfcorrectie

De autonomie van Agentic RAG omvat ook robuuste zelfcorrectiemechanismen. Wanneer het systeem vastloopt—bijvoorbeeld door het ophalen van irrelevante documenten of het tegenkomen van verkeerd gevormde queries—kan het:

- **Itereren en Opnieuw Query’en:** In plaats van lage-waarde antwoorden te geven, probeert het model nieuwe zoekstrategieën, herschrijft database-queries of bekijkt alternatieve datasets.
- **Diagnostische Tools gebruiken:** Het systeem kan extra functies aanroepen die helpen bij het debuggen van redeneringsstappen of het bevestigen van de correctheid van opgehaalde gegevens. Tools zoals Azure AI Tracing zijn belangrijk om robuuste observeerbaarheid en monitoring mogelijk te maken.
- **Terugvallen op Menselijke Supervisie:** Bij scenario's met hoge inzet of herhaald falen kan het model onzekerheid aangeven en om menselijke begeleiding vragen. Zodra de mens corrigerende feedback geeft, kan het model die les in de toekomst toepassen.

Deze iteratieve en dynamische aanpak stelt het model in staat continu te verbeteren, waardoor het niet slechts een eenmalig systeem is, maar een dat leert van zijn misstappen tijdens een sessie.

![Self Correction Mechanism](../../../translated_images/nl/self-correction.da87f3783b7f174b.webp)

## Grenzen van Agentie

Ondanks zijn autonomie binnen een taak is Agentic RAG niet analoog aan Kunstmatige Algemene Intelligentie. Zijn “agentische” capaciteiten zijn beperkt tot de tools, databronnen en beleidsregels die door menselijke ontwikkelaars worden geleverd. Het kan zijn eigen tools niet uitvinden of buiten de domeingrenzen stappen die zijn gesteld. In plaats daarvan blinkt het uit in het dynamisch orkestreren van de beschikbare resources.
Belangrijke verschillen ten opzichte van meer geavanceerde AI-vormen zijn:

1. **Domeinspecifieke Autonomie:** Agentic RAG-systemen zijn gericht op het bereiken van door gebruikers gedefinieerde doelen binnen een bekend domein, waarbij strategieën zoals het herschrijven van queries of het kiezen van tools worden gebruikt om resultaten te verbeteren.
2. **Afhankelijk van Infrastructuur:** De capaciteiten van het systeem hangen af van de tools en gegevens die door ontwikkelaars zijn geïntegreerd. Het kan deze grenzen niet overschrijden zonder menselijke tussenkomst.
3. **Respect voor Veiligheidsmaatregelen:** Ethische richtlijnen, nalevingsregels en bedrijfsbeleid blijven erg belangrijk. De vrijheid van de agent wordt altijd beperkt door veiligheidsmaatregelen en toezichtmechanismen (hopelijk?).

## Praktische Gebruikssituaties en Waarde

Agentic RAG blinkt uit in scenario's die iteratieve verfijning en precisie vereisen:

1. **Omgevingen die Correctheid Prioriteren:** In compliance-controles, regelgeving-analyse of juridisch onderzoek kan het agentische model feiten herhaaldelijk verifiëren, meerdere bronnen raadplegen en queries herschrijven totdat het een grondig getoetst antwoord levert.
2. **Complexe Database-Interactie:** Bij het omgaan met gestructureerde gegevens waarbij queries vaak kunnen falen of aanpassing nodig hebben, kan het systeem zelfstandig zijn queries verfijnen met Azure SQL of Microsoft Fabric OneLake, om te verzekeren dat de uiteindelijke zoekopdracht overeenkomt met de intentie van de gebruiker.
3. **Uitgebreide Workflows:** Langdurige sessies kunnen evolueren naarmate nieuwe informatie beschikbaar komt. Agentic RAG kan continu nieuwe data verwerken en strategieën aanpassen naarmate het meer leert over het probleemgebied.

## Bestuur, Transparantie en Vertrouwen

Naarmate deze systemen autonomer worden in hun redenering, zijn bestuur en transparantie cruciaal:

- **Verklaarbare Redenering:** Het model kan een audittrail leveren van de queries die het heeft gesteld, de bronnen die het heeft geraadpleegd en de redeneringsstappen die het heeft genomen om tot zijn conclusie te komen. Tools zoals Azure AI Content Safety en Azure AI Tracing / GenAIOps helpen transparantie te waarborgen en risico's te verminderen.
- **Beheersing van Vooroordelen en Gebalanceerde Informatieophaling:** Ontwikkelaars kunnen zoekstrategieën afstemmen om gebalanceerde, representatieve databronnen mee te nemen, en outputs regelmatig auditen om vooroordelen of scheve patronen te detecteren met behulp van aangepaste modellen voor geavanceerde datawetenschapsorganisaties die Azure Machine Learning gebruiken.
- **Menselijk Toezicht en Naleving:** Voor gevoelige taken blijft menselijke review essentieel. Agentic RAG vervangt niet de menselijke beoordeling in situaties met hoge inzet, het ondersteunt die door meer grondig getoetste opties te leveren.

Het hebben van tools die een duidelijk overzicht geven van acties is essentieel. Zonder deze tools kan het debuggen van een meerstapsproces erg moeilijk zijn. Zie het volgende voorbeeld van Literal AI (bedrijf achter Chainlit) voor een Agent-run:

![AgentRunExample](../../../translated_images/nl/AgentRunExample.471a94bc40cbdc0c.webp)

## Conclusie

Agentic RAG vertegenwoordigt een natuurlijke evolutie in de manier waarop AI-systemen complexe, data-intensieve taken afhandelen. Door het aannemen van een gelust interactiepatroon, zelfstandig tools te selecteren en queries te verfijnen totdat een hoogwaardige uitkomst bereikt is, beweegt het systeem verder dan statisch promptvolgen naar een meer adaptieve, contextbewuste besluitvormer. Hoewel het nog steeds gebonden is aan door mensen gedefinieerde infrastructuren en ethische richtlijnen, maken deze agentische capaciteiten rijkere, dynamischere en uiteindelijk nuttigere AI-interacties mogelijk voor zowel bedrijven als eindgebruikers.

### Meer vragen over Agentic RAG?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere lerenden te ontmoeten, office hours bij te wonen en antwoord te krijgen op je vragen over AI Agents.

## Aanvullende Bronnen

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementeer Retrieval Augmented Generation (RAG) met Azure OpenAI Service: Leer hoe je je eigen data gebruikt met Azure OpenAI Service. Deze Microsoft Learn-module biedt een uitgebreide gids voor het implementeren van RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluatie van generatieve AI-toepassingen met Microsoft Foundry: Dit artikel behandelt de evaluatie en vergelijking van modellen op publiek beschikbare datasets, inclusief Agentic AI-toepassingen en RAG-architecturen</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Wat is Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Een Complete Gids voor Agent-Based Retrieval Augmented Generation – Nieuws van generatie RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: versnel je RAG met query-herschikking en zelfquery! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agentlaag toevoegen aan RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">De toekomst van kennisassistenten: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Hoe bouw je agentic RAG-systemen</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Microsoft Foundry Agent Service gebruiken om je AI-agents te schalen</a>

### Academische Artikelen

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratieve verfijning met zelffeedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Talagenten met verbale versterkingsleer</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Grote taalmodellen kunnen zichzelf corrigeren met tool-geïntegreerde kritiek</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Een overzicht van Agentic RAG</a>

## Deze Agent Testen (optioneel)

Nadat je hebt geleerd hoe je agents inzet in [Les 16](../16-deploying-scalable-agents/README.md), kun je deze les's `TravelRAGAgent` testen — controleren of de antwoorden blijven gebaseerd op de kennisbank — met [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Zie [`tests/README.md`](../tests/README.md) voor hoe je het uitvoert.

## Vorige Les

[Tool Use Design Pattern](../04-tool-use/README.md)

## Volgende Les

[Betrouwbare AI-agents bouwen](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->