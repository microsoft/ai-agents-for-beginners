# AI Agents voor Beginners - Studiegids

Gebruik deze gids als een praktische metgezel terwijl je door de cursus gaat. Het is
niet bedoeld om de lessen te vervangen. Het helpt je beslissen waar te beginnen, wat te
zoeken in elke les, en hoe de ideeën te verbinden tot een kleine werkende agent
demo.

Als dit je eerste keer hier is, begin dan eenvoudig:

1. Lees de [Course Setup](./00-course-setup/README.md).
2. Maak de lessen 01-06 in volgorde af.
3. Houd één klein demo-idee in gedachten terwijl je leert.
4. Vraag na elke les: "Wat kan mijn agent nu doen dat hij voorheen niet kon?"


## Een eenvoudige demo om in gedachten te houden

Een goede manier om agenten te leren is één demo-idee door de hele cursus te volgen.

Voorbeeld demo: **een cursus-helper agent**.

De gebruiker vraagt:

> "Ik wil leren hoe agenten tools gebruiken. Vind de juiste lessen, vat samen wat
> ik eerst moet lezen, en geef me een korte oefentaak."

Een gewone chatbot kan antwoorden op basis van wat hij al weet. Een agent kan meer:

1. **Lees of doorzoek cursusbestanden** om de juiste lessen te vinden.
2. **Gebruik tools** om leslinks, voorbeelden of ondersteunend materiaal op te halen.
3. **Plan** een kort leertraject in plaats van één lang antwoord te geven.
4. **Gebruik context** uit het huidige gesprek om gefocust te blijven op het doel van de leerling.
5. **Onthoud nuttige voorkeuren** als de applicatie geheugen ondersteunt.
6. **Toon sporen, citaties of logs** zodat de gebruiker kan begrijpen wat er is gebeurd.
7. **Pas guardrails toe** voordat je risicovolle acties onderneemt of gevoelige gegevens gebruikt.


zou deze les toevoegen?


## Waar je naartoe werkt

Aan het einde van de cursus zou je agent-systemen moeten kunnen uitleggen en bouwen
die deze onderdelen combineren:

| Onderdeel | Betekenis in gewone taal | In de demo |
|------|------------------------|-------------|
| Model | De redeneermotor die het verzoek van de gebruiker interpreteert | Begrijpt dat de leerling lessen wil over toolgebruik |
| Tools | Functies, API's, bestanden, browsers of diensten die de agent kan gebruiken | Doorzoekt de repo of haalt lesmateriaal op |
| Kennis | Documenten of data gebruikt om het antwoord te onderbouwen | Cursus README-bestanden en lesmateriaal |
| Context | Informatie opgenomen in de volgende model-aanroep | Het doel van de gebruiker en de toolresultaten |
| Geheugen | Informatie opgeslagen voor later gebruik | De leerling geeft de voorkeur aan hands-on Python voorbeelden |
| Planning | Een groter doel opsplitsen in kleinere stappen | Vind lessen, vat ze samen, stel oefening voor |
| Orkestratie | Werk verdelen over tools, stappen of agenten | Een planner roept eerst een zoektool aan, daarna een samenvatter |
| Vertrouwen | Veiligheid, beveiliging, evaluatie en observeerbaarheid | Logt tool-aanroepen en vraagt voordat hij ingrijpende handelingen uitvoert |

## Modellen en Providers

De codevoorbeelden van de cursus gebruiken het **Microsoft Agent Framework (MAF)** en richten zich op de **Azure OpenAI Responses API** — de aanbevolen API voor de toekomst, die chats, tool-aanroepen, multimodale input en stateful gesprekken in één enkele API combineert. Je maakt verbinding via een **Microsoft Foundry** project (met `FoundryChatClient`) of direct met Azure OpenAI (met `OpenAIChatClient`).

Tijdens het volgen van de lessen heb je een paar provider-opties:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — de hoofdroute die in de lessen wordt gebruikt. Meld je aan met `az login` voor keyless Entra ID authenticatie.
- **Foundry Local** — draai modellen volledig op het apparaat via een OpenAI-compatibele API (geen cloud, geen API-sleutels). Ideaal voor offline of kosteloze experimenten. Zie [Course Setup](./00-course-setup/README.md).
- **MiniMax** — een OpenAI-compatibele provider met grote-contextmodellen, te gebruiken als een drop-in alternatief.

> **Opmerking:** GitHub Models is verouderd (wordt uitgefaseerd in juli 2026) en ondersteunt de Responses API niet. De voorbeelden zijn bijgewerkt om Azure OpenAI / Microsoft Foundry te gebruiken.

## Kies je leerpad

Je kunt de volledige cursus in volgorde doen, of naar een pad springen op basis van wat je wilt
bouwen.

| Als je doel is om... | Begin met | Bestudeer daarna |
|-----------------------|------------|------------|
| Begrijpen wat agenten zijn | 01, 02, 03 | 04, 05, 06 |
| Een agent bouwen die tools gebruikt | 04 | 05, 07, 14 |
| Een RAG-gebaseerde agent bouwen | 05 | 04, 06, 12 |
| Meerstaps-workflows ontwerpen | 07 | 08, 09, 14 |
| Meervoudige agent-systemen begrijpen | 08 | 07, 09, 11 |
| Agenten voorbereiden voor productie | 06, 10 | 12, 13, 16, 18 |
| Agenten implementeren en schalen op Foundry | 10, 16 | 06, 13, 18 |
| Lokale / offline-eerst agenten bouwen | 17 | 04, 05, 11 |
| Protocollen en browserautomatisering verkennen | 11, 15 | 10, 18 |

Tip: als je nieuw bent met agenten, sla dan lessen 01-06 niet over. Ze geven je de
woordenschat die je nodig zult hebben voor de rest van de cursus.

## Les-voor-les gids

| Les | Wat je leert | Probeer dit na de les |
|--------|----------------|---------------------------|
| [01 - Introductie tot AI Agents](./01-intro-to-ai-agents/README.md) | Wat een agent anders maakt dan een basis chatbot. | Leg je demo-idee uit als een agent, niet alleen een chatapp. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | Hoe frameworks helpen met modellen, tools, staat, en workflows. | Identificeer welke delen van je demo een framework zou beheren. |
| [03 - Agentic Ontwerppatronen](./03-agentic-design-patterns/README.md) | Veelvoorkomende patronen voor het ontwerpen van agentgedrag. | Schets de gebruikersreis voordat je code schrijft. |
| [04 - Toolgebruik](./04-tool-use/README.md) | Hoe agenten tools aanroepen om data te krijgen of actie te ondernemen. | Definieer één tool die jouw demo-agent nodig zou hebben. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Hoe retrieval agentantwoorden bij documenten of data verankert. | Bepaal welke kennisbron jouw demo zou moeten doorzoeken. |

| [06 - Vertrouwde Agenten](./06-building-trustworthy-agents/README.md) | Hoe je vangrails, toezicht en veiliger gedrag toevoegt. | Voeg een regel toe over wanneer de agent eerst de gebruiker moet vragen. |
| [07 - Ontwerp van Planning](./07-planning-design/README.md) | Hoe agenten grotere doelen opdelen in kleinere stappen. | Schrijf een plan in drie stappen voor je demo-aanvraag. |
| [08 - Ontwerp van Multi-Agenten](./08-multi-agent/README.md) | Wanneer werk verdeeld wordt over gespecialiseerde agenten. | Bepaal of je demo één agent of meerdere nodig heeft. |
| [09 - Metacognitie](./09-metacognition/README.md) | Hoe agenten hun eigen output kunnen herzien en verbeteren. | Voeg een laatste zelfcontrole toe voordat de agent reageert. |
| [10 - AI Agents in Productie](./10-ai-agents-production/README.md) | Wat er verandert als een agent van demo naar productie gaat. | Maak een lijst van wat je zou monitoren: kwaliteit, kosten, latency, fouten. |
| [11 - Agentische Protocollen](./11-agentic-protocols/README.md) | Hoe protocollen agenten verbinden met tools en andere agenten. | Identificeer waar een standaardprotocol integratie kan vereenvoudigen. |
| [12 - Context Engineering](./12-context-engineering/README.md) | Hoe context geselecteerd, bijgesneden, geïsoleerd en beheerd wordt. | Bepaal wat in de prompt hoort en wat buiten moet blijven. |
| [13 - Agent Memory](./13-agent-memory/README.md) | Hoe agenten nuttige informatie over interacties heen kunnen opslaan. | Kies één veilige voorkeur die je demo zou kunnen onthouden. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Framework-specifieke bouwstenen voor agenten en workflows, plus het hosten van LangChain/LangGraph-agenten op Microsoft Foundry. | Breng de demo-stappen in kaart naar frameworkconcepten. |
| [15 - Computer Gebruik Agenten](./15-browser-use/README.md) | Hoe agenten kunnen interacteren met browser- of UI-interfaces, inclusief realistische voorbeelden zoals Microsoft Project Opal. | Kies één browsertaak die nog steeds gebruikersbevestiging vereist. |
| [16 - Schaalbare Agenten Implementeren](./16-deploying-scalable-agents/README.md) | Hoe een agent van prototype naar een schaalbare, observeerbare productie-implementatie op Microsoft Foundry gaat (gehoste agenten, modelroutering, caching, evaluatiepoorten, rooktesten). | Noem de productiezorgen die je demo nog heeft: hosting, routering, kosten, evaluatie. |
| [17 - Lokale AI Agenten Maken](./17-creating-local-ai-agents/README.md) | Hoe lokaal- eerst agenten te bouwen die volledig op je machine draaien met Foundry Local en Qwen (lokale tools, lokale RAG, lokale MCP). | Bepaal welke delen van je demo privé moeten blijven en lokaal moeten draaien. |
| [18 - AI Agenten Beveiligen](./18-securing-ai-agents/README.md) | Hoe agentacties auditabeler en manipulatieweerbaar gemaakt worden. | Bepaal welke acties in je demo gelogd of geregistreerd moeten worden. |

## Gevalideerde Geïmplementeerde Agenten met Rooktesten

Wanneer je een agent implementeert (Les 16), is een **rooktest** de goedkoopste eerste
controle of de implementatie daadwerkelijk antwoordt. Deze repo bevat kant-en-klare
catalogi onder [tests/](./tests/README.md) voor de implementeerbare agenten in de lessen
01, 04, 05 en 16, aangesloten op de
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Actie. Voer ze uit via het **Actions** tabblad na het implementeren van de lesagent.
Rooktesten zijn een eerste poort — offline en online evaluatie (lessen 10 en 16)
vertellen je hoe *goed* de agent is.

## Belangrijke Ideeën in Beginnersvriendelijke Termen

### Tools

Een tool is iets dat de agent kan aanroepen om werk buiten het model te doen. Een goede tool
heeft een duidelijke naam, een specifieke taak, getypte inputs, voorspelbare output en een veilige manier
om te falen.

Voor de cursushelper demo kan een tool zijn:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG en Kennis

RAG helpt de agent te antwoorden vanuit bronmateriaal in plaats van te raden. In deze
cursus kan dat bronmateriaal les-README’s, codevoorbeelden of externe
bronnen zijn die uit de lessen gelinkt worden.

Gebruik RAG wanneer het antwoord gebaseerd moet zijn op documenten, data of actuele
projectbestanden.

### Planning

Planning is nuttig wanneer het verzoek meer dan één stap bevat. Houd plannen kort en
zichtbaar genoeg voor een ontwikkelaar of gebruiker om te inspecteren.

Voor de demo kan een plan zijn:

1. Vind lessen die verband houden met het gebruik van tools.
2. Vat de meest relevante lessen samen.
3. Raad één oefentaak aan.

### Context

Context is wat het model nu ziet. Te weinig context kan ervoor zorgen dat de agent
belangrijke details mist. Te veel context kan de agent trager, duurder
of gemakkelijker in de war maken.

Goede contextengineering betekent de juiste informatie kiezen voor de volgende model-
oproep.

### Geheugen

Geheugen is opgeslagen informatie voor later. Bewaar niet alles. Sla informatie alleen op
wanneer het nuttig, veilig en gemakkelijk bij te werken of te verwijderen is.

Bijvoorbeeld, onthouden dat "de leerling de voorkeur geeft aan Python-voorbeelden" kan nuttig zijn.
Het onthouden van gevoelige persoonlijke data meestal niet.

### Evaluatie en Observeerbaarheid

Evaluatie vraagt: heeft de agent het juiste gedaan?

Observeerbaarheid vraagt: kunnen we zien hoe het gebeurde?

Voor productieagenten, houd bij: modelaanroepen, toolaanroepen, opgehaalde context,
latency, kosten, fouten en gebruikersfeedback.

### Vertrouwen en Beveiliging

Vertrouwde agenten hebben meer nodig dan een behulpzame prompt. Gebruik least-privilege tools,
menselijke goedkeuring voor acties met grote impact, dataredactie waar nodig, en logs of
ontvangstbewijzen voor acties die geaudit moeten worden.

## Een 15-Minuten Review Routine

Gebruik deze routine na elke les:

1. **Vat de les samen in één zin.**
2. **Noem de nieuwe agentcapaciteit.** Bijvoorbeeld: gebruik van tools, retrieval,
   planning, geheugen, observeerbaarheid of beveiliging.
3. **Voeg het toe aan de cursushelper-demo.** Wat verandert er nu in de demo?
4. **Vind het risico.** Wat kan er misgaan als deze capaciteit verkeerd wordt gebruikt?
5. **Schrijf één toetsvraag.** Hoe zou je controleren of de agent zich goed gedraagt?

## Snelle Zelfcontrole

Voordat je verder gaat, probeer deze vragen te beantwoorden:

1. Wat kan een agent doen dat een gewone chatbot niet zelf kan?
2. Welke tool zou je agent eerst nodig hebben, en waarom?
3. Welke kennisbron moet het antwoord van de agent onderbouwen?
4. Welke context moet worden meegenomen in de volgende modeloproep?

5. Wat moet de agent onthouden en wat moet hij vermijden op te slaan?
6. Wanneer moet de agent om goedkeuring van een mens vragen?
7. Welke logs, sporen of ontvangstbewijzen zouden je later helpen om de agent te debuggen of te controleren?


## Voorgestelde Capstone Oefening

Aan het einde van de cursus bouw je een kleine agent die een leerling helpt navigeren in deze
repository.

Minimale versie:

- Accepteer een onderwerp van de gebruiker.
- Vind de meest relevante lessen.
- Vat samen wat je eerst moet lezen.
- Stel één hands-on oefentaak voor.
- Toon welke lesbestanden of links gebruikt zijn.

Uitgebreide versie:

- Onthoud de voorkeurstaal van de leerling.
- Gebruik een eenvoudig plan voordat je antwoordt.
- Voeg een zelfcontrole-stap toe vóór het definitieve antwoord.
- Log tool-aanroepen en opgehaalde bronnen.
- Vraag om bevestiging voordat je een browser of UI-automatiseringstaken opent.

Dit geeft je een kleine maar realistische manier om te oefenen met tools, RAG, planning,
context, geheugen, observeerbaarheid en vertrouwen in één project.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->