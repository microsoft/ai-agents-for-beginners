# Context Engineering voor AI-agenten

[![Context Engineering](../../../translated_images/nl/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Het begrijpen van de complexiteit van de toepassing waarvoor je een AI-agent bouwt, is belangrijk om er een betrouwbare te maken. We moeten AI-agenten bouwen die effectief informatie beheren om complexe behoeften aan te pakken, verder dan alleen promptengineering.

In deze les bekijken we wat context engineering is en welke rol het speelt bij het bouwen van AI-agenten.

## Inleiding

Deze les behandelt:

• **Wat context engineering is** en waarom het anders is dan promptengineering.

• **Strategieën voor effectieve context engineering**, inclusief hoe je informatie schrijft, selecteert, comprimeert en isoleert.

• **Veelvoorkomende contextfouten** die je AI-agent kunnen tegenwerken en hoe je ze kunt oplossen.

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

• **Context engineering definieert** en het onderscheidt van promptengineering.

• **De belangrijkste componenten van context** in toepassingen met Large Language Models (LLM) identificeert.

• **Strategieën toepast voor het schrijven, selecteren, comprimeren en isoleren van context** om de prestaties van agenten te verbeteren.

• **Veelvoorkomende contextfouten herkent**, zoals vergiftiging, afleiding, verwarring en botsingen, en mitigatietechnieken implementeert.

## Wat is Context Engineering?

Voor AI-agenten is context hetgeen de planning aandrijft om bepaalde acties te ondernemen. Context engineering is de praktijk om ervoor te zorgen dat de AI-agent de juiste informatie heeft om de volgende stap van de taak te voltooien. Het contextvenster is beperkt in grootte, dus als bouwer van agenten moeten we systemen en processen maken om het toevoegen, verwijderen en condenseren van informatie in het contextvenster te beheren.

### Prompt Engineering vs Context Engineering

Prompt engineering richt zich op een enkele set statische instructies om de AI-agenten effectief met regels te sturen. Context engineering gaat over het beheren van een dynamische set informatie, inclusief de initiële prompt, om ervoor te zorgen dat de AI-agent in de loop van de tijd heeft wat hij nodig heeft. Het kernidee van context engineering is dit proces herhaalbaar en betrouwbaar te maken.

### Soorten Context

[![Soorten Context](../../../translated_images/nl/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Het is belangrijk te onthouden dat context niet slechts één ding is. De informatie die de AI-agent nodig heeft, kan uit verschillende bronnen komen en het is aan ons om ervoor te zorgen dat de agent toegang heeft tot deze bronnen:

De soorten context die een AI-agent mogelijk moet beheren zijn:

• **Instructies:** Dit zijn de "regels" voor de agent – prompts, systeemberichten, few-shot voorbeelden (laten zien hoe de AI iets moet doen) en beschrijvingen van tools die het kan gebruiken. Hier combineert het focusgebied van promptengineering zich met context engineering.

• **Kennis:** Dit omvat feiten, informatie opgehaald uit databases, of langetermijnherinneringen die de agent heeft verzameld. Dit omvat ook het integreren van een Retrieval Augmented Generation (RAG) systeem als een agent toegang nodig heeft tot verschillende kennisopslagplaatsen en databases.

• **Tools:** Dit zijn definities van externe functies, API's en MCP-servers die de agent kan aanroepen, samen met de feedback (resultaten) die het krijgt bij het gebruik ervan.

• **Gespreksgeschiedenis:** De lopende dialoog met een gebruiker. Naarmate de tijd verstrijkt, worden deze gesprekken langer en complexer, wat betekent dat ze ruimte innemen in het contextvenster.

• **Gebruikersvoorkeuren:** Informatie die in de loop van de tijd is geleerd over de voorkeuren en afkeuren van een gebruiker. Deze kunnen worden opgeslagen en opgevraagd worden bij het nemen van belangrijke beslissingen om de gebruiker te helpen.

## Strategieën voor Effectieve Context Engineering

### Planningsstrategieën

[![Best Practices Context Engineering](../../../translated_images/nl/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Goede context engineering begint met goede planning. Hier is een benadering die je helpt na te denken over hoe je het concept van context engineering kunt toepassen:

1. **Definieer duidelijke resultaten** - De resultaten van de taken die AI-agenten moeten uitvoeren, moeten duidelijk worden gedefinieerd. Beantwoord de vraag: "Hoe ziet de wereld eruit wanneer de AI-agent klaar is met zijn taak?" Met andere woorden, welke verandering, informatie of reactie moet de gebruiker hebben na interactie met de AI-agent.
2. **Breng de context in kaart** - Zodra je de resultaten van de AI-agent hebt gedefinieerd, moet je de vraag beantwoorden: "Welke informatie heeft de AI-agent nodig om deze taak te voltooien?". Zo kun je beginnen met het in kaart brengen van waar die informatie te vinden is.
3. **Creëer contextpijplijnen** - Nu je weet waar de informatie is, moet je beantwoorden: "Hoe krijgt de agent deze informatie?". Dit kan op verschillende manieren, waaronder RAG, het gebruik van MCP-servers en andere tools.

### Praktische Strategieën

Planning is belangrijk, maar zodra de informatie begint binnen te komen in het contextvenster van onze agent, moeten we praktische strategieën hebben om dit te beheren:

#### Context beheren

Hoewel sommige informatie automatisch aan het contextvenster wordt toegevoegd, gaat context engineering over het actief beheren van deze informatie, wat met een paar strategieën kan worden gedaan:

 1. **Agent Scratchpad**  
 Dit stelt een AI-agent in staat aantekeningen te maken van relevante informatie over de huidige taken en gebruikersinteracties tijdens een sessie. Dit moet buiten het contextvenster bestaan, bijvoorbeeld in een bestand of runtime-object dat de agent later tijdens deze sessie kan ophalen indien nodig.

 2. **Herinneringen**  
 Scratchpads zijn goed voor het beheren van informatie buiten het contextvenster van een enkele sessie. Herinneringen stellen agenten in staat relevante informatie over meerdere sessies op te slaan en op te halen. Dit kan samenvattingen, gebruikersvoorkeuren en feedback voor toekomstige verbeteringen omvatten.

 3. **Context comprimeren**  
  Zodra het contextvenster groeit en het limiet nadert, kunnen technieken zoals samenvatten en inkorten worden gebruikt. Dit houdt in dat alleen de meest relevante informatie wordt bewaard of oudere berichten worden verwijderd.
  
 4. **Multi-Agent-systemen**  
  Het ontwikkelen van multi-agent-systemen is een vorm van context engineering omdat elke agent zijn eigen contextvenster heeft. Hoe die context wordt gedeeld en doorgegeven aan andere agenten is iets om uit te denken bij het bouwen van deze systemen.
  
 5. **Sandbox-omgevingen**  
  Als een agent code moet uitvoeren of grote hoeveelheden informatie in een document moet verwerken, kan dit veel tokens kosten om de resultaten te verwerken. In plaats van dit allemaal in het contextvenster op te slaan, kan de agent een sandbox-omgeving gebruiken die deze code kan uitvoeren en alleen de resultaten en andere relevante informatie kan lezen.
  
 6. **Runtime-statusobjecten**  
   Dit wordt gedaan door containers van informatie te maken om situaties te beheren wanneer de agent toegang nodig heeft tot bepaalde informatie. Voor een complexe taak kan dit een agent in staat stellen de resultaten van elk subtakketap stap voor stap op te slaan, zodat de context alleen verbonden blijft met die specifieke subtaak.

#### Context inspecteren

Nadat je een van deze strategieën hebt toegepast, is het de moeite waard om te controleren wat de volgende modelaanroep daadwerkelijk ontving. Een nuttige debugvraag is:

> Heeft de agent te veel context geladen, de verkeerde context, of context gemist die hij nodig had?

Je hoeft geen ruwe prompts, tool-uitvoer of geheugeninhoud te loggen om die vraag te beantwoorden. In productie geef je de voorkeur aan kleine contextinspectie-records die aantallen, id's, hashes en beleidslabels vastleggen:

- **Selectie:** Houd bij hoeveel kandidaatstukken, tools of herinneringen werden overwogen, hoeveel werden geselecteerd, en welke regel of score ervoor zorgde dat de anderen werden gefilterd.
- **Compressie:** Leg de bronbereik of trace-id vast, de samenvatting-id, een geschatte tokentelling voor en na compressie, en of de ruwe inhoud werd uitgesloten van de volgende aanroep.
- **Isolatie:** Noteer welke subtaak in een aparte agent, sessie of sandbox draaide, welke begrensde samenvatting werd teruggegeven, en of grote tool-uitvoer buiten de context van de hoofdagent bleef.
- **Geheugen en RAG:** Sla id's van opgevraagde documenten, geheugen-id's, scores, geselecteerde id's en redactiestatus op in plaats van de volledige opgehaalde tekst.
- **Veiligheid en privacy:** Geef de voorkeur aan hashes, id's, tokenbuckets en beleidslabels boven gevoelige prompttekst, toolargumenten, toolresultaten of gebruikersgeheugeninhoud.

Het doel is niet om meer context te bewaren. Het is om genoeg bewijs achter te laten zodat een ontwikkelaar kan zien welke contextstrategie is uitgevoerd en of dit de volgende modelaanroep op de bedoelde wijze heeft veranderd.

### Voorbeeld van Context Engineering

Stel dat we een AI-agent willen die **"Boek een reis voor mij naar Parijs."**

• Een eenvoudige agent die alleen promptengineering gebruikt, zou misschien gewoon reageren: **"Oké, wanneer wil je naar Parijs gaan?"** Hij verwerkte alleen je directe vraag op het moment dat de gebruiker die stelde.

• Een agent die de context engineering-strategieën toepast die we bespraken, zou veel meer doen. Voordat hij zelfs reageert, kan zijn systeem bijvoorbeeld:

  ◦ **Je agenda checken** voor beschikbare data (real-time gegevens ophalen).

 ◦ **Eerdere reisvoorkeuren ophalen** (uit het langetermijngeheugen) zoals je favoriete luchtvaartmaatschappij, budget, of of je directe vluchten prefereert.

 ◦ **Beschikbare tools identificeren** voor het boeken van vluchten en hotels.

- Een voorbeeldantwoord kan zijn: "Hey [Jouw Naam]! Ik zie dat je de eerste week van oktober vrij bent. Zal ik zoeken naar directe vluchten naar Parijs met [Voorkeursluchtvaartmaatschappij] binnen je gebruikelijke budget van [Budget]?" Dit rijkere, contextbewuste antwoord toont de kracht van context engineering aan.

## Veelvoorkomende Contextfouten

### Context Vergiftiging

**Wat het is:** Wanneer een hallucinatie (valse informatie gegenereerd door het LLM) of een fout in de context komt en herhaaldelijk wordt genoemd, waardoor de agent onmogelijke doelen nastreeft of onzinstrategieën ontwikkelt.

**Wat te doen:** Implementeer **contextvalidatie** en **quarantaine**. Valideer informatie voordat deze wordt toegevoegd aan het langetermijngeheugen. Als mogelijke vergiftiging wordt gedetecteerd, start dan nieuwe contextthreads om te voorkomen dat de slechte informatie zich verspreidt.

**Voorbeeld Reisboeking:** Je agent hallucinereert een **directe vlucht van een kleine lokale luchthaven naar een verre internationale stad** die eigenlijk geen internationale vluchten aanbiedt. Dit niet-bestaande vluchtgegeven wordt opgeslagen in de context. Later, wanneer je de agent vraagt om te boeken, blijft hij proberen tickets te vinden voor deze onmogelijke route, wat leidt tot herhaalde fouten.

**Oplossing:** Implementeer een stap die **de vluchtbestaan en routes valideert met een real-time API** _voordat_ het vluchtdetail aan de werkcontext van de agent wordt toegevoegd. Als de validatie faalt, wordt de foutieve informatie "geïnterneerd" en niet verder gebruikt.

### Context Afleiding

**Wat het is:** Wanneer de context zo groot wordt dat het model te veel op de opgebouwde geschiedenis focust in plaats van op wat het tijdens training leerde, wat leidt tot repetitieve of niet-helpende acties. Modellen kunnen fouten beginnen te maken nog voordat het contextvenster vol is.

**Wat te doen:** Gebruik **contextsummarizatie**. Periode komprimeren zich opeenhopende informatie in kortere samenvattingen, waarbij belangrijke details worden bewaard en overbodige geschiedenis wordt verwijderd. Dit helpt om de focus te "resetten".

**Voorbeeld Reisboeking:** Je hebt al lang gesproken over verschillende droomreisbestemmingen, inclusief een gedetailleerd verslag van je rugzakreis van twee jaar geleden. Als je uiteindelijk vraagt om een **"goedkope vlucht voor volgende maand te vinden,"** raakt de agent verstrikt in de oude, irrelevante details en blijft hij vragen over je rugzakuitrusting of oude reisschema's, en negeert hij je actuele verzoek.

**Oplossing:** Na een bepaald aantal interacties of als de context te groot wordt, moet de agent **de meest recente en relevante gedeelten van het gesprek samenvatten** – gericht op je actuele reisdata en bestemming – en die gecondenseerde samenvatting voor de volgende LLM-aanroep gebruiken, terwijl minder relevante historische chat wordt weggegooid.

### Context Verwarring

**Wat het is:** Wanneer onnodige context, vaak in de vorm van te veel beschikbare tools, ervoor zorgt dat het model slechte reacties genereert of irrelevante tools aanroept. Kleinere modellen zijn hier bijzonder vatbaar voor.

**Wat te doen:** Implementeer **tool loadout management** met behulp van RAG-technieken. Bewaar toolbeschrijvingen in een vectordatabase en selecteer _alleen_ de meest relevante tools voor elke specifieke taak. Onderzoek toont aan dat het beperken van toolselecties tot minder dan 30 effectief is.

**Voorbeeld Reisboeking:** Je agent heeft toegang tot tientallen tools: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, enzovoort. Je vraagt, **"Wat is de beste manier om in Parijs rond te reizen?"** Door het grote aantal tools raakt de agent in de war en probeert hij `book_flight` _binnen_ Parijs aan te roepen, of `rent_car` terwijl jij liever openbaar vervoer gebruikt, omdat toolbeschrijvingen mogelijk overlappen of hij simpelweg niet kan bepalen welke de beste is.

**Oplossing:** Gebruik **RAG over toolbeschrijvingen**. Wanneer je vraagt over het rondreizen in Parijs, haalt het systeem dynamisch _alleen_ de meest relevante tools op zoals `rent_car` of `public_transport_info` op basis van je query, en presenteert een gerichte "loadout" van tools aan het LLM.

### Context Botsing

**Wat het is:** Wanneer conflicterende informatie binnen de context bestaat, wat leidt tot inconsistente redenering of slechte eindantwoorden. Dit gebeurt vaak wanneer informatie in fases aankomt en vroege, onjuiste aannames in de context blijven staan.

**Wat te doen:** Gebruik **context pruning** en **offloading**. Pruning betekent het verwijderen van verouderde of conflicterende informatie zodra er nieuwe details binnenkomen. Offloading geeft het model een aparte "scratchpad"-werkruimte om informatie te verwerken zonder het hoofdcontext te vervuilen.


**Voorbeeld van reisboeking:** Je vertelt aanvankelijk aan je agent, **"Ik wil economy class vliegen."** Later in het gesprek verander je van gedachten en zeg je, **"Eigenlijk, voor deze reis, laten we business class nemen."** Als beide instructies in de context blijven, kan de agent tegenstrijdige zoekresultaten krijgen of in de war raken over welke voorkeur voorrang moet krijgen.

**Oplossing:** Implementeer **context pruning**. Wanneer een nieuwe instructie een oude tegenspreekt, wordt de oudere instructie verwijderd of expliciet overschreven in de context. Alternatief kan de agent een **scratchpad** gebruiken om tegenstrijdige voorkeuren te verzoenen voordat hij beslist, zodat alleen de uiteindelijke, consistente instructie zijn acties stuurt.

## Nog meer vragen over Context Engineering?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere lerenden te ontmoeten, deel te nemen aan spreekuren en je vragen over AI Agents beantwoord te krijgen.
## Vorige les

[Agentic Protocols](../11-agentic-protocols/README.md)

## Volgende les

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->