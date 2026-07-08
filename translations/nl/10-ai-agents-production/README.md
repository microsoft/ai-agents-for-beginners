# AI-agents in productie: observeerbaarheid & evaluatie

[![AI Agents in Production](../../../translated_images/nl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Naarmate AI-agents verschuiven van experimentele prototypes naar toepassingen in de echte wereld, wordt het belangrijk om hun gedrag te begrijpen, hun prestaties te monitoren en hun output systematisch te evalueren.

## Leerdoelen

Na het voltooien van deze les weet je hoe je/begrijp je:
- Kernconcepten van observeerbaarheid en evaluatie van agents
- Technieken om de prestaties, kosten en effectiviteit van agents te verbeteren
- Wat en hoe je je AI-agents systematisch kunt evalueren
- Hoe je kosten kunt beheersen bij het inzetten van AI-agents in productie
- Hoe je agents gebouwd met Microsoft Agent Framework kunt instrumenteren

Het doel is om je de kennis te geven om je "black box" agents om te vormen tot transparante, beheersbare en betrouwbare systemen.

_**Opmerking:** Het is belangrijk om AI Agents te implementeren die veilig en betrouwbaar zijn. Bekijk ook de les [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Traces en Spans

Observeerbaarheidstools zoals [Langfuse](https://langfuse.com/) of [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representeren agent runs meestal als traces en spans.

- **Trace** vertegenwoordigt een volledige agent taak van begin tot eind (zoals het verwerken van een gebruikersvraag).
- **Spans** zijn individuele stappen binnen de trace (zoals het aanroepen van een taalmodel of het ophalen van data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Zonder observeerbaarheid kan een AI-agent aanvoelen als een "black box" - de interne staat en redenering zijn ondoorzichtig, waardoor het moeilijk is problemen te diagnosticeren of prestaties te optimaliseren. Met observeerbaarheid worden agents "glass boxes," die transparantie bieden die cruciaal is om vertrouwen op te bouwen en ervoor te zorgen dat ze werken zoals bedoeld. 

## Waarom observeerbaarheid belangrijk is in productieomgevingen

Het overbrengen van AI-agents naar productieomgevingen brengt nieuwe uitdagingen en eisen met zich mee. Observeerbaarheid is geen "nice-to-have" meer, maar een essentiële capaciteit:

*   **Debuggen en oorzaak-analyse**: Wanneer een agent faalt of een onverwachte output produceert, bieden observeerbaarheidstools de traces die nodig zijn om de bron van de fout te achterhalen. Dit is vooral belangrijk bij complexe agents die meerdere LLM-aanroepen, toolinteracties en conditionele logica kunnen omvatten.
*   **Latency en kostenbeheer**: AI-agents vertrouwen vaak op LLM's en andere externe API's die per token of per aanroep worden gefactureerd. Observeerbaarheid maakt nauwkeurige tracking van deze oproepen mogelijk, waardoor operaties die te traag of te duur zijn kunnen worden geïdentificeerd. Dit stelt teams in staat prompts te optimaliseren, efficiëntere modellen te kiezen of workflows te herontwerpen om operationele kosten te beheersen en een goede gebruikerservaring te garanderen.
*   **Vertrouwen, veiligheid en naleving**: In veel toepassingen is het belangrijk om ervoor te zorgen dat agents zich veilig en ethisch gedragen. Observeerbaarheid biedt een audit-trail van agentacties en beslissingen. Dit kan worden gebruikt om problemen zoals promptinjectie, het genereren van schadelijke inhoud of het verkeerd omgaan met persoonlijk identificeerbare informatie (PII) te detecteren en te verminderen. Bijvoorbeeld kun je traces bekijken om te begrijpen waarom een agent een bepaalde reactie gaf of een specifiek hulpmiddel gebruikte.
*   **Continue verbeteringscycli**: Observeerbaarheidsdata vormt de basis van een iteratief ontwikkelingsproces. Door te monitoren hoe agents presteren in de echte wereld, kunnen teams verbeterpunten identificeren, data verzamelen voor het fine-tunen van modellen en de impact van wijzigingen valideren. Dit creëert een feedbackloop waarin inzichten uit online evaluatie offline experimenten en verfijning informeren, wat leidt tot steeds betere agentprestaties.

## Belangrijke metrics om te volgen

Om agentgedrag te monitoren en te begrijpen, moeten diverse metrics en signalen worden gevolgd. Hoewel de specifieke metrics kunnen variëren afhankelijk van het doel van de agent, zijn sommige universeel belangrijk.

Hier zijn enkele van de meest voorkomende metrics die observeerbaarheidstools monitoren:

**Latency:** Hoe snel reageert de agent? Lange wachttijden hebben een negatieve impact op de gebruikerservaring. Je moet de latency meten voor taken en individuele stappen door agent runs te traceren. Bijvoorbeeld, een agent die 20 seconden nodig heeft voor alle modelaanroepen kan versneld worden door een sneller model te gebruiken of door modelaanroepen parallel uit te voeren.

**Kosten:** Wat zijn de kosten per agent run? AI-agents vertrouwen op LLM-aanroepen die per token worden gefactureerd of externe API's. Frequente toolgebruik of meerdere prompts kunnen de kosten snel verhogen. Bijvoorbeeld, als een agent een LLM vijf keer aanroept voor een marginale kwaliteitsverbetering, moet je beoordelen of de kosten gerechtvaardigd zijn of dat je het aantal aanroepen kunt verminderen of een goedkoper model kunt gebruiken. Real-time monitoring kan ook helpen onverwachte pieken te identificeren (bijvoorbeeld bugs die excessieve API-lussen veroorzaken).

**Request Errors:** Hoeveel verzoeken zijn mislukt? Dit kan API-fouten of mislukte toolaanroepen omvatten. Om je agent robuuster te maken tegen deze in productie, kun je fallback-mechanismen of retries instellen. Bijvoorbeeld als LLM-provider A down is, schakel je over naar LLM-provider B als back-up.

**Gebruikersfeedback:** Directe gebruikersbeoordelingen bieden waardevolle inzichten. Dit kan expliciete beoordelingen zijn (👍duim omhoog/👎omlaag, ⭐1-5 sterren) of tekstuele opmerkingen. Consistente negatieve feedback moet je waarschuwen, want dit is een teken dat de agent niet werkt zoals verwacht.

**Impliciete gebruikersfeedback:** Gebruikersgedrag levert indirecte feedback, zelfs zonder expliciete beoordelingen. Dit kan directe herformulering van vragen omvatten, herhaalde zoekopdrachten of het klikken op een retry-knop. Bijvoorbeeld, als je ziet dat gebruikers herhaaldelijk dezelfde vraag stellen, is dit een teken dat de agent niet werkt zoals verwacht.

**Nauwkeurigheid:** Hoe vaak produceert de agent correcte of wenselijke outputs? Definities van nauwkeurigheid variëren (bijv. correctheid van probleemoplossing, informatieve nauwkeurigheid, gebruikerstevredenheid). De eerste stap is definiëren wat succes voor jouw agent betekent. Je kunt nauwkeurigheid volgen via geautomatiseerde controles, evaluatiescores of taakvoltooiingslabels. Bijvoorbeeld traces markeren als "geslaagd" of "mislukt".

**Geautomatiseerde evaluatiemetrics:** Je kunt ook geautomatiseerde evaluaties opzetten. Bijvoorbeeld een LLM gebruiken om de output van de agent te scoren (bijv. nuttig, nauwkeurig of niet). Er zijn ook verschillende open source bibliotheken die helpen verschillende aspecten van de agent te scoren, zoals [RAGAS](https://docs.ragas.io/) voor RAG-agents of [LLM Guard](https://llm-guard.com/) om schadelijke taal of promptinjectie te detecteren.

In de praktijk biedt een combinatie van deze metrics de beste dekking van de gezondheid van een AI-agent. In dit hoofdstuk [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) laten we zien hoe deze metrics eruit zien in echte voorbeelden, maar eerst leren we hoe een typische evaluatieworkflow eruitziet.

## Instrumenteer je agent

Om tracingdata te verzamelen, moet je je code instrumenteren. Het doel is om de agentcode te instrumenteren zodat deze traces en metrics uitstoot die kunnen worden vastgelegd, verwerkt en gevisualiseerd door een observeerbaarheidsplatform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) is uitgegroeid tot een industriestandaard voor LLM observeerbaarheid. Het biedt een set API's, SDK's en tools voor het genereren, verzamelen en exporteren van telemetriedata.

Er zijn veel instrumentatielibraries die bestaande agentframeworks wrappen en het gemakkelijk maken OpenTelemetry spans naar een observeerbaarheidstool te exporteren. Microsoft Agent Framework integreert native met OpenTelemetry. Hieronder een voorbeeld van het instrumenteren van een MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentuitvoering wordt automatisch gevolgd
    pass
```

De [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) in dit hoofdstuk demonstreert hoe je je MAF-agent kunt instrumenteren.

**Handmatige spancreatie:** Terwijl instrumentatielibraries een goede basis bieden, zijn er vaak gevallen waar gedetailleerdere of aangepaste informatie nodig is. Je kunt handmatig spans creëren om aangepaste applicatielogica toe te voegen. Belangrijker nog kunnen ze automatisch of handmatig gecreëerde spans verrijken met aangepaste attributen (ook bekend als tags of metadata). Deze attributen kunnen bedrijfspecifieke data, tussenliggende berekeningen of elke context omvatten die nuttig kan zijn voor debugging of analyse, zoals `user_id`, `session_id` of `model_version`.

Voorbeeld van het handmatig aanmaken van traces en spans met de [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent evaluatie

Observeerbaarheid geeft ons metrics, maar evaluatie is het proces van het analyseren van die data (en uitvoeren van tests) om te bepalen hoe goed een AI-agent presteert en hoe deze kan worden verbeterd. Met andere woorden, zodra je die traces en metrics hebt, hoe gebruik je die dan om de agent te beoordelen en beslissingen te nemen?

Regelmatige evaluatie is belangrijk omdat AI-agents vaak niet-deterministisch zijn en kunnen evolueren (door updates of drift in modelgedrag) – zonder evaluatie zou je niet weten of je “slimme agent” zijn werk goed doet of juist achteruitgaat.

Er zijn twee categorieën evaluaties voor AI-agents: **online evaluatie** en **offline evaluatie**. Beide zijn waardevol en vullen elkaar aan. We beginnen meestal met offline evaluatie, omdat dit de minimale noodzakelijke stap is vóór het uitrollen van een agent.

### Offline evaluatie

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dit omvat het evalueren van de agent in een gecontroleerde omgeving, meestal met testdatasets, niet met live gebruikersvragen. Je gebruikt samengestelde datasets waarvan je de verwachte output of correct gedrag weet, en laat je agent die doorlopen.

Bijvoorbeeld, als je een agent hebt gebouwd voor wiskundige tekstproblemen, zou je een [testdataset](https://huggingface.co/datasets/gsm8k) kunnen hebben van 100 problemen met bekende antwoorden. Offline evaluatie wordt vaak gedaan tijdens de ontwikkeling (en kan deel uitmaken van CI/CD-pijplijnen) om verbeteringen te controleren of regressies te voorkomen. Het voordeel is dat het **herhaalbaar is en je duidelijke nauwkeurigheidsmetrics krijgt omdat je de grondwaarheid hebt**. Je kunt ook gebruikersvragen simuleren en de antwoorden van de agent meten tegen ideale antwoorden of gebruik maken van geautomatiseerde metrics zoals hierboven beschreven.

De belangrijkste uitdaging bij offline evaluatie is ervoor te zorgen dat je testdataset volledig is en relevant blijft – de agent kan goed presteren op een vaste testset, maar heel andere vragen tegenkomen in productie. Daarom moet je testsets bijwerken met nieuwe edgecases en voorbeelden die de echte werksituaties weerspiegelen. Een mix van kleine “smoke test” cases en grotere evaluatiesets is nuttig: kleine sets voor snelle controles en grotere voor bredere prestatietracking.

### Online evaluatie

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dit verwijst naar het evalueren van de agent in een live, real-life omgeving, dat wil zeggen tijdens daadwerkelijk gebruik in productie. Online evaluatie omvat het monitoren van de prestaties van de agent op echte gebruikersinteracties en het continu analyseren van resultaten.

Bijvoorbeeld, je kunt succespercentages, gebruikersbeoordelingsscores of andere metrics volgen op live verkeer. Het voordeel van online evaluatie is dat het **aspecten vastlegt die je mogelijk niet verwacht in een labsetting** – je kunt modeldrift over tijd waarnemen (als de effectiviteit van de agent afneemt terwijl invoerpatronen veranderen) en onverwachte vragen of situaties ontdekken die niet in je testdata zaten. Het geeft een waarheidsgetrouw beeld van hoe de agent zich in de praktijk gedraagt.

Online evaluatie omvat vaak het verzamelen van impliciete en expliciete gebruikersfeedback, zoals besproken, en kan ook het uitvoeren van shadow tests of A/B-tests omvatten (waarbij een nieuwe versie van de agent parallel draait om te vergelijken met de oude). De uitdaging is dat het lastig kan zijn betrouwbare labels of scores te krijgen voor live interacties – je kunt afhankelijk zijn van gebruikersfeedback of downstream metrics (zoals of de gebruiker op het resultaat klikte).

### De combinatie van beide

Online en offline evaluaties sluiten elkaar niet uit; ze vullen elkaar juist goed aan. Inzichten uit online monitoring (bijvoorbeeld soorten gebruikersvragen waarop de agent slecht presteert) kunnen worden gebruikt om offline testdatasets aan te vullen en te verbeteren. Omgekeerd kunnen agents die goed presteren in offline tests met meer vertrouwen online worden uitgerold en gemonitord.

Veel teams hanteren een cyclus:

_offline evalueren -> uitrollen -> online monitoren -> nieuwe faalcases verzamelen -> toevoegen aan offline dataset -> agent verfijnen -> herhalen_.

## Veelvoorkomende problemen

Bij het inzetten van AI-agents in productie kun je verschillende uitdagingen tegenkomen. Hier zijn enkele veelvoorkomende problemen en mogelijke oplossingen:

| **Probleem**    | **Mogelijke oplossing**   |
| ------------- | ------------------ |
| AI-agent voert taken niet consistent uit | - Verfijn de prompt die aan de AI-Agent wordt gegeven; wees duidelijk over de doelstellingen.<br>- Identificeer waar het opdelen van taken in subtaken en afhandelen door meerdere agents kan helpen. |
| AI-agent komt in continue loops terecht | - Zorg dat je duidelijke stopvoorwaarden hebt zodat de Agent weet wanneer het proces moet stoppen.<br>- Voor complexe taken die redeneren en plannen vereisen, gebruik een groter model dat gespecialiseerd is in redeneertaken. |
| AI-agent toolaanroepen presteren niet goed | - Test en valideer de output van de tool buiten het agentsysteem.<br>- Verfijn de gedefinieerde parameters, prompts en benoeming van tools.  |
| Multi-agent systeem presteert niet consistent | - Verfijn prompts aan elke agent zodat ze specifiek en verschillend van elkaar zijn.<br>- Bouw een hiërarchisch systeem met een "routerende" of controller-agent die bepaalt welke agent de juiste is. |

Veel van deze problemen kunnen effectiever worden geïdentificeerd met observeerbaarheid. De eerder besproken traces en metrics helpen precies te bepalen waar in de agent workflow problemen optreden, waardoor debuggen en optimaliseren veel efficiënter wordt.

## Kosten beheren


Hier zijn enkele strategieën om de kosten van het inzetten van AI-agenten in productie te beheren:

**Gebruik van Kleinere Modellen:** Kleine taalmodellen (SLM's) kunnen goed presteren bij bepaalde agent-gerichte use-cases en zullen de kosten aanzienlijk verlagen. Zoals eerder vermeld, is het bouwen van een evaluatiesysteem om de prestaties te bepalen en te vergelijken met grotere modellen de beste manier om te begrijpen hoe goed een SLM zal presteren voor jouw use case. Overweeg om SLM's te gebruiken voor eenvoudigere taken zoals intentieclassificatie of parameterextractie, terwijl je grotere modellen reserveert voor complexe redenering.

**Gebruik van een Routermodel:** Een vergelijkbare strategie is het gebruik van een diversiteit aan modellen en maten. Je kunt een LLM/SLM of serverloze functie gebruiken om verzoeken op basis van complexiteit naar de best passende modellen te routeren. Dit helpt ook om kosten te besparen en zorgt ervoor dat de prestaties passend zijn voor de juiste taken. Bijvoorbeeld, leid eenvoudige vragen naar kleinere, snellere modellen en gebruik dure grote modellen alleen voor complexe redeneertaken.

**Caching van Antwoorden:** Het identificeren van veelvoorkomende verzoeken en taken en het vooraf leveren van de antwoorden voordat ze door je agent-systeem gaan, is een goede manier om het volume van soortgelijke verzoeken te verminderen. Je kunt zelfs een flow implementeren om te bepalen hoe vergelijkbaar een verzoek is met je opgeslagen (gecachede) verzoeken met behulp van meer basale AI-modellen. Deze strategie kan de kosten aanzienlijk verlagen voor veelgestelde vragen of gebruikelijke workflows.

## Laten we kijken hoe dit in de praktijk werkt

In de [voorbeeldnotebook van deze sectie](./code_samples/10-expense_claim-demo.ipynb) zien we voorbeelden van hoe we observatietools kunnen gebruiken om onze agent te monitoren en evalueren.


### Meer Vragen over AI-Agenten in Productie?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, deel te nemen aan office hours en je vragen over AI-Agenten beantwoord te krijgen.

## Vorige Les

[Metacognition Design Pattern](../09-metacognition/README.md)

## Volgende Les

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->