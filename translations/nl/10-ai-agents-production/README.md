# AI-agents in productie: Observeerbaarheid & Evaluatie

[![AI-agents in productie](../../../translated_images/nl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Naarmate AI-agents verschuiven van experimentele prototypes naar toepassingen in de echte wereld, wordt het vermogen om hun gedrag te begrijpen, hun prestaties te monitoren en hun outputs systematisch te evalueren belangrijk.

## Leerdoelen

Na het voltooien van deze les weet je hoe/begrijp je:
- Kernconcepten van agent-observeerbaarheid en evaluatie
- Technieken om de prestaties, kosten en effectiviteit van agents te verbeteren
- Wat en hoe je je AI-agents systematisch moet evalueren
- Hoe je kosten kunt beheersen bij het inzetten van AI-agents in productie
- Hoe je agents bouwt met Microsoft Agent Framework kunt instrumenteren

Het doel is je uit te rusten met de kennis om je "zwarte doos" agents om te vormen tot transparante, beheersbare en betrouwbare systemen.

_**Opmerking:** Het is belangrijk om AI-agents te implementeren die veilig en betrouwbaar zijn. Bekijk ook de les [Vertrouwenswaardige AI-agents bouwen](./06-building-trustworthy-agents/README.md)._

## Traces en Spans

Observeerbaarheidstools zoals [Langfuse](https://langfuse.com/) of [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) geven agentruns meestal weer als traces en spans.

- **Trace** vertegenwoordigt een volledige agenttaak van begin tot eind (zoals het afhandelen van een gebruikersvraag).
- **Spans** zijn afzonderlijke stappen binnen de trace (zoals het aanroepen van een language model of het ophalen van gegevens).

![Traceboom in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Zonder observeerbaarheid kan een AI-agent aanvoelen als een "zwarte doos" — de interne staat en redenering zijn ondoorzichtig, waardoor het moeilijk is om problemen te diagnosticeren of prestaties te optimaliseren. Met observeerbaarheid worden agents "glazen dozen" die transparantie bieden die essentieel is voor het opbouwen van vertrouwen en ervoor zorgen dat ze werken zoals bedoeld. 

## Waarom observeerbaarheid belangrijk is in productieomgevingen

Het overbrengen van AI-agents naar productieomgevingen introduceert een nieuwe reeks uitdagingen en vereisten. Observeerbaarheid is niet langer een "nice-to-have" maar een kritische capaciteit:

*   **Foutopsporing en oorzaakanalyse**: Wanneer een agent faalt of een onverwachte output produceert, bieden observeerbaarheidstools de traces die nodig zijn om de bron van de fout te lokaliseren. Dit is vooral belangrijk in complexe agents die meerdere LLM-aanroepen, toolinteracties en conditionele logica kunnen bevatten.
*   **Latentie- en kostenbeheer**: AI-agents vertrouwen vaak op LLMs en andere externe API's die per token of per oproep in rekening worden gebracht. Observeerbaarheid maakt nauwkeurige tracking van deze oproepen mogelijk, waardoor je operaties kunt identificeren die buitensporig langzaam of duur zijn. Dit stelt teams in staat prompts te optimaliseren, efficiëntere modellen te selecteren of workflows te herontwerpen om operationele kosten te beheersen en een goede gebruikerservaring te garanderen.
*   **Vertrouwen, veiligheid en naleving**: In veel toepassingen is het belangrijk om ervoor te zorgen dat agents zich veilig en ethisch gedragen. Observeerbaarheid levert een audittrail van agentacties en -beslissingen. Dit kan worden gebruikt om problemen zoals promptinjectie, het genereren van schadelijke inhoud of het onjuist behandelen van persoonlijk identificeerbare informatie (PII) te detecteren en te mitigeren. Bijvoorbeeld, je kunt traces bekijken om te begrijpen waarom een agent een bepaalde reactie gaf of een specifieke tool gebruikte.
*   **Continue verbeteringslussen**: Observeerbaarheidsdata vormt de basis van een iteratief ontwikkelproces. Door te monitoren hoe agents in de echte wereld presteren, kunnen teams verbeterpunten identificeren, data verzamelen voor het fijnregelen van modellen en de impact van wijzigingen valideren. Dit creëert een feedbackloop waarbij productie-inzichten uit online evaluatie offline experimenten en verfijningen informeren, wat leidt tot steeds betere agentprestaties.

## Belangrijke statistieken om te volgen

Om het gedrag van agents te monitoren en te begrijpen, moeten verschillende statistieken en signalen worden gevolgd. Hoewel de specifieke metrics kunnen variëren afhankelijk van het doel van de agent, zijn sommige universeel belangrijk.

Hier zijn enkele van de meest voorkomende statistieken die observeerbaarheidstools monitoren:

**Latentie:** Hoe snel reageert de agent? Lange wachttijden beïnvloeden de gebruikerservaring negatief. Je zou latentie voor taken en individuele stappen moeten meten door agentruns te tracen. Bijvoorbeeld, een agent die 20 seconden nodig heeft voor alle modelaanroepen kan worden versneld door een sneller model te gebruiken of door modelaanroepen parallel uit te voeren.

**Kosten:** Wat zijn de kosten per agentrun? AI-agents vertrouwen op LLM-aanroepen die per token worden gefactureerd of op externe API's. Frequent gebruik van tools of meerdere prompts kan de kosten snel opvoeren. Bijvoorbeeld, als een agent een LLM vijf keer aanroept voor een marginale kwaliteitsverbetering, moet je beoordelen of de kosten gerechtvaardigd zijn of dat je het aantal oproepen kunt verminderen of een goedkoper model kunt gebruiken. Realtime monitoring kan ook onverwachte pieken identificeren (bijv. bugs die tot buitensporige API-lussen leiden).

**Requestfouten:** Hoeveel verzoeken is de agent niet gelukt? Dit kan API-fouten of mislukte toolaanroepen omvatten. Om je agent robuuster te maken tegen deze fouten in productie, kun je dan fallback‑strategieën of retries instellen. Bijv. als LLM-provider A down is, schakel je over naar LLM-provider B als backup.

**Gebruikersfeedback:** Het implementeren van directe gebruikersbeoordelingen levert waardevolle inzichten op. Dit kan expliciete beoordelingen omvatten (👍thumbs-up/👎down, ⭐1-5 sterren) of tekstuele opmerkingen. Aanhoudend negatieve feedback moet een waarschuwing zijn omdat dit aangeeft dat de agent niet werkt zoals verwacht. 

**Impliciete gebruikersfeedback:** Gebruikersgedrag geeft indirecte feedback, zelfs zonder expliciete beoordelingen. Dit kan onmiddellijke herformulering van vragen omvatten, herhaalde queries of het klikken op een retry-knop. Bijv. als je ziet dat gebruikers herhaaldelijk dezelfde vraag stellen, is dit een teken dat de agent niet naar verwachting presteert.

**Nauwkeurigheid:** Hoe vaak produceert de agent correcte of gewenste outputs? Definities van nauwkeurigheid variëren (bijv. correctheid bij probleemoplossing, nauwkeurigheid van informatie-ophaling, gebruikersvoldoening). De eerste stap is definiëren hoe succes eruitziet voor je agent. Je kunt nauwkeurigheid volgen via geautomatiseerde checks, evaluatiescores of taakvoltooiingslabels. Bijvoorbeeld door traces te markeren als "geslaagd" of "mislukt". 

**Geautomatiseerde evaluatiemaatstaven:** Je kunt ook geautomatiseerde evaluaties opzetten. Bijvoorbeeld kun je een LLM gebruiken om de output van de agent te scoren, bijv. of deze behulpzaam of accuraat is. Er zijn ook verschillende open source bibliotheken die je helpen verschillende aspecten van de agent te scoren. Bijv. [RAGAS](https://docs.ragas.io/) voor RAG-agents of [LLM Guard](https://llm-guard.com/) om schadelijke taal of promptinjectie te detecteren. 

In de praktijk geeft een combinatie van deze statistieken de beste dekking van de gezondheid van een AI-agent. In het [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) van dit hoofdstuk laten we zien hoe deze statistieken eruitzien in echte voorbeelden, maar eerst leren we hoe een typische evaluatieworkflow eruitziet.

## Instrumenteer je agent

Om tracingdata te verzamelen, moet je je code instrumenteren. Het doel is om de agentcode te instrumenteren zodat deze traces en metrics kan uitsturen die door een observeerbaarheidsplatform kunnen worden vastgelegd, verwerkt en gevisualiseerd.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) is uitgegroeid tot een industrienorm voor LLM-observeerbaarheid. Het biedt een set API's, SDK's en tools voor het genereren, verzamelen en exporteren van telemetriedata. 

Er zijn veel instrumentisatiebibliotheken die bestaande agentframeworks omhullen en het eenvoudig maken om OpenTelemetry-spans naar een observeerbaarheidstool te exporteren. Microsoft Agent Framework integreert native met OpenTelemetry. Hieronder staat een voorbeeld van het instrumenteren van een MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # De uitvoering van de agent wordt automatisch gevolgd
    pass
```

Het [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) in dit hoofdstuk zal demonstreren hoe je je MAF-agent kunt instrumenteren.

**Handmatige spancreatie:** Hoewel instrumentatielibraries een goede basis bieden, zijn er vaak gevallen waar meer gedetailleerde of aangepaste informatie nodig is. Je kunt handmatig spans aanmaken om aangepaste applicatielogica toe te voegen. Wat nog belangrijker is, is dat je automatisch of handmatig aangemaakte spans kunt verrijken met aangepaste attributen (ook wel tags of metadata genoemd). Deze attributen kunnen bedrijfsspecifieke gegevens, tussenresultaten of context bevatten die nuttig kan zijn voor debugging of analyse, zoals `user_id`, `session_id` of `model_version`.

Voorbeeld van het handmatig creëren van traces en spans met de [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluatie van agenten

Observeerbaarheid geeft ons metrics, maar evaluatie is het proces van het analyseren van die data (en het uitvoeren van tests) om te bepalen hoe goed een AI-agent presteert en hoe deze kan worden verbeterd. Met andere woorden, zodra je die traces en metrics hebt, hoe gebruik je ze om de agent te beoordelen en beslissingen te nemen? 

Regelmatige evaluatie is belangrijk omdat AI-agents vaak niet-deterministisch zijn en kunnen evolueren (door updates of drift in modelgedrag) – zonder evaluatie zou je niet weten of je "slimme agent" daadwerkelijk zijn werk goed doet of dat hij achteruit is gegaan.

Er zijn twee categorieën evaluaties voor AI-agents: **online evaluatie** en **offline evaluatie**. Beide zijn waardevol en vullen elkaar aan. We beginnen meestal met offline-evaluatie, omdat dit de minimale noodzakelijke stap is voordat je een agent inzet.

### Offline-evaluatie

![Datasetitems in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dit houdt in dat je de agent in een gecontroleerde omgeving evalueert, doorgaans met behulp van testdatasets, niet met live gebruikersqueries. Je gebruikt samengestelde datasets waarvan je weet wat de verwachte output of het correcte gedrag is, en draait vervolgens je agent daarop. 

Bijvoorbeeld, als je een agent hebt gebouwd voor wiskundewoordproblemen, kun je een [testdataset](https://huggingface.co/datasets/gsm8k) van 100 problemen met bekende antwoorden hebben. Offline-evaluatie wordt vaak gedaan tijdens ontwikkeling (en kan deel uitmaken van CI/CD-pijplijnen) om verbeteringen te controleren of regressies te voorkomen. Het voordeel is dat het **herhaalbaar is en je duidelijke nauwkeurigheidsstatistieken kunt krijgen omdat je ground truth hebt**. Je kunt ook gebruikersqueries simuleren en de reacties van de agent meten aan de hand van ideale antwoorden of geautomatiseerde metrics zoals hierboven beschreven. 

De belangrijkste uitdaging bij offline-evaluatie is ervoor te zorgen dat je testdataset uitgebreid en relevant blijft – de agent kan goed presteren op een vaste testset maar heel andere queries tegenkomen in productie. Daarom moet je testsets up-to-date houden met nieuwe edgecases en voorbeelden die de echte wereld weerspiegelen​. Een mix van kleine "smoke test"-gevallen en grotere evaluatiesets is nuttig: kleine sets voor snelle controles en grotere voor bredere prestatieresultaten​.

### Online-evaluatie 

![Overzicht van observeerbaarheidsstatistieken](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dit verwijst naar het evalueren van de agent in een live, real-world omgeving, d.w.z. tijdens daadwerkelijk gebruik in productie. Online-evaluatie omvat het monitoren van de prestaties van de agent op echte gebruikersinteracties en het continu analyseren van uitkomsten. 

Bijvoorbeeld, je kunt succespercentages, gebruikersvoldoening-scores of andere metrics op live verkeer bijhouden. Het voordeel van online-evaluatie is dat het **zaken vastlegt die je mogelijk niet in een labsetting verwacht** – je kunt modeldrift in de loop van de tijd waarnemen (als de effectiviteit van de agent afneemt naarmate inputpatronen verschuiven) en onverwachte queries of situaties opvangen die niet in je testdata stonden​. Het geeft een waarheidsgetrouw beeld van hoe de agent zich in het veld gedraagt. 

Online-evaluatie omvat vaak het verzamelen van impliciete en expliciete gebruikersfeedback, zoals eerder besproken, en mogelijk het uitvoeren van shadow-tests of A/B-tests (waarbij een nieuwe versie van de agent parallel draait om te vergelijken met de oude). De uitdaging is dat het lastig kan zijn om betrouwbare labels of scores voor live-interacties te verkrijgen – je kunt afhankelijk zijn van gebruikersfeedback of downstream-metrics (zoals of de gebruiker op het resultaat klikte). 

### Beide combineren

Online- en offline-evaluaties sluiten elkaar niet uit; ze vullen elkaar juist goed aan. Inzichten uit online monitoring (bijv. nieuwe types gebruikersqueries waarbij de agent slecht presteert) kunnen worden gebruikt om offline testdatasets aan te vullen en te verbeteren. Omgekeerd kunnen agents die goed presteren in offline tests met meer vertrouwen worden ingezet en online gemonitord.

In feite hanteren veel teams de volgende lus: 

_evalueer offline -> uitrollen -> monitoren online -> nieuwe faalgevallen verzamelen -> toevoegen aan offline-dataset -> agent verfijnen -> herhalen_.

## Veelvoorkomende problemen

Als je AI-agents in productie inzet, kun je verschillende uitdagingen tegenkomen. Hier zijn enkele veelvoorkomende problemen en hun mogelijke oplossingen:

| **Probleem**    | **Potentiële oplossing**   |
| ------------- | ------------------ |
| AI-agent voert taken niet consequent uit | - Verfijn de prompt die aan de AI-agent wordt gegeven; wees duidelijk over de doelstellingen.<br>- Bepaal waar het opdelen van taken in subtaken en het laten afhandelen door meerdere agenten kan helpen. |
| AI-agent komt in voortdurende lussen terecht  | - Zorg dat je duidelijke beëindigingsvoorwaarden hebt zodat de agent weet wanneer het proces moet stoppen.<br>- Voor complexe taken die redeneren en plannen vereisen, gebruik een groter model dat gespecialiseerd is in redeneertaken. |
| Tool-aanroepen van de AI-agent presteren niet goed   | - Test en valideer de output van de tool buiten het agentsysteem om.<br>- Verfijn de gedefinieerde parameters, prompts en de naamgeving van tools.  |
| Multi-agent systeem presteert niet consistent | - Verfijn de prompts die aan elke agent worden gegeven zodat ze specifiek en verschillend van elkaar zijn.<br>- Bouw een hiërarchisch systeem met een "routing" of controller-agent om te bepalen welke agent de juiste is. |

Veel van deze problemen kunnen effectiever worden geïdentificeerd met observeerbaarheid geïmplementeerd. De traces en metrics die we eerder bespraken helpen precies te identificeren waar in de agentworkflow problemen optreden, waardoor debuggen en optimaliseren veel efficiënter wordt.

## Kosten beheren
Hier zijn enkele strategieën om de kosten van het inzetten van AI-agenten in productie te beheersen:

**Gebruik van kleinere modellen:** Kleine taalmodellen (SLMs) kunnen in bepaalde agentachtige gebruikssituaties goed presteren en de kosten aanzienlijk verlagen. Zoals eerder genoemd, is het opzetten van een evaluatiesysteem om de prestaties te bepalen en te vergelijken met grotere modellen de beste manier om te begrijpen hoe goed een SLM zal presteren in jouw gebruikssituatie. Overweeg SLMs te gebruiken voor eenvoudigere taken zoals intentieclassificatie of parameterextractie, terwijl je grotere modellen reserveert voor complexe redeneertaken.

**Gebruik van een routermodel:** Een vergelijkbare strategie is het gebruik van een diversiteit aan modellen en groottes. Je kunt een LLM/SLM of serverless functie gebruiken om verzoeken op basis van complexiteit te routeren naar de best passende modellen. Dit helpt ook om kosten te verlagen terwijl het prestaties op de juiste taken waarborgt. Bijvoorbeeld: routeer eenvoudige vragen naar kleinere, snellere modellen en gebruik dure grote modellen alleen voor complexe redeneertaken.

**Antwoorden cachen:** Het identificeren van veelvoorkomende verzoeken en taken en het vooraf leveren van de antwoorden voordat ze via je agent-systeem gaan, is een goede manier om het aantal vergelijkbare verzoeken te verminderen. Je kunt zelfs een proces implementeren om te bepalen hoe vergelijkbaar een verzoek is met je gecachte verzoeken, met behulp van meer eenvoudige AI-modellen. Deze strategie kan de kosten aanzienlijk verlagen voor veelgestelde vragen of gangbare werkstromen.

## Laten we kijken hoe dit in de praktijk werkt

In het [voorbeeldnotebook van deze sectie](./code_samples/10-expense_claim-demo.ipynb) zullen we voorbeelden zien van hoe we observability-tools kunnen gebruiken om onze agent te monitoren en te evalueren.

### Nog vragen over AI-agenten in productie?

Sluit je aan bij de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, deel te nemen aan spreekuren en je vragen over AI-agenten beantwoord te krijgen.

## Vorige les

[Ontwerppatroon voor metacognitie](../09-metacognition/README.md)

## Volgende les

[Agentische protocollen](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dit document is vertaald met behulp van de AI-vertalingsdienst Co-op Translator (https://github.com/Azure/co-op-translator). Hoewel we naar nauwkeurigheid streven, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor belangrijke informatie raden wij een professionele menselijke vertaling aan. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->