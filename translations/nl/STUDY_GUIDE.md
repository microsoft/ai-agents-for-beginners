# AI-agenten voor beginners - studiegids

Gebruik deze gids als een praktische begeleider terwijl je door de cursus gaat. Het is
niet bedoeld om de lessen te vervangen. Het helpt je te beslissen waar te beginnen, wat te
zoeken in elke les, en hoe de ideeën te verbinden tot een kleine werkende agent
demo.

Als dit je eerste keer hier is, begin dan eenvoudig:

1. Lees de [Course Setup](./00-course-setup/README.md).
2. Voltooi lessen 01-06 op volgorde.
3. Houd één klein demo-idee in gedachten terwijl je leert.
4. Vraag na elke les: "Wat kan mijn agent nu wat hij eerder niet kon?"


## Een eenvoudige demo om in gedachten te houden

Een goede manier om agenten te leren is één demo-idee door de cursus heen te volgen.

Voorbeelddemo: **een cursushelper-agent**.

De gebruiker vraagt:

> "Ik wil leren hoe agenten tools gebruiken. Vind de juiste lessen, vat samen wat
> ik eerst zou moeten lezen, en geef me een korte oefentaak."

Een reguliere chatbot kan antwoorden vanuit wat hij al weet. Een agent kan meer:

1. **Lees of doorzoek cursusbestanden** om de juiste lessen te vinden.
2. **Gebruik tools** om leskoppelingen, voorbeelden of ondersteunend materiaal op te halen.
3. **Plan** een kort leertraject in plaats van één lang antwoord te geven.
4. **Gebruik context** uit het huidige gesprek om gefocust te blijven op het doel van de leerling.
5. **Onthoud nuttige voorkeuren** als de applicatie geheugen ondersteunt.
6. **Laat sporen, citaties of logs zien** zodat de gebruiker kan begrijpen wat er gebeurde.
7. **Pas beveiligingsmaatregelen toe** voordat je risicovolle acties uitvoert of gevoelige data gebruikt.


mogelijkheid zou deze les toevoegen?


## Waar je naartoe werkt

Aan het einde van de cursus moet je in staat zijn agent systemen uit te leggen en te bouwen
die deze onderdelen combineren:

| Onderdeel | Betekenis in gewone taal | In de demo |
|------|------------------------|-------------|
| Model | De redeneermotor die de vraag van de gebruiker interpreteert | Begrijpt dat de leerling lessen wil over toolgebruik |
| Tools | Functies, API's, bestanden, browsers of diensten die de agent kan gebruiken | Doorzoekt de repo of haalt lesinhoud op |
| Kennis | Documenten of data die het antwoord onderbouwen | Cursus README-bestanden en lesmateriaal |
| Context | Informatie die is inbegrepen in de volgende modelaanroep | Het doel van de gebruiker en de toolresultaten |
| Geheugen | Informatie die voor later gebruik opgeslagen is | De leerling geeft de voorkeur aan hands-on Pythonvoorbeelden |
| Planning | Een groter doel opsplitsen in kleinere stappen | Zoek lessen, vat samen, stel oefening voor |
| Orkestratie | Werk routen over tools, stappen of agenten | Een planner roept een zoektool op, daarna een samenvatter |
| Vertrouwen | Veiligheid, beveiliging, evaluatie en observeerbaarheid | Logt toolaanroepen en vraagt vooraf bij impactvolle acties |

## Modellen en Providers

De cursus-codevoorbeelden gebruiken het **Microsoft Agent Framework (MAF)** en richten zich op de **Azure OpenAI Responses API** — de aanbevolen API voortaan, die chatcompletions, toolaanroepen, multimodale input, en stateful gesprekken combineert in een enkele API-omgeving. Je verbindt via een **Microsoft Foundry** project (met `FoundryChatClient`) of rechtstreeks met Azure OpenAI (met `OpenAIChatClient`).

Terwijl je door de lessen werkt, heb je een paar provideropties:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — het primaire pad gebruikt in de lessen. Meld je aan met `az login` voor sleutelvrije Entra ID-authenticatie.
- **Foundry Local** — draai modellen volledig lokaal via een OpenAI-compatibele API (geen cloud, geen API-sleutels). Ideaal voor offline of kosteloze experimenten. Zie [Course Setup](./00-course-setup/README.md).
- **MiniMax** — een OpenAI-compatibele provider met large-context modellen, bruikbaar als drop-in alternatief.

> **Let op:** GitHub Models is verouderd (wordt stopgezet juli 2026) en ondersteunt de Responses API niet. De voorbeelden zijn bijgewerkt om Azure OpenAI / Microsoft Foundry te gebruiken.

## Kies je leerroute

Je kunt de volledige cursus in volgorde volgen, of springen naar een pad gebaseerd op wat je wilt
bouwen.

| Als jouw doel is om... | Begin met | Bestudeer daarna |
|-----------------------|------------|-------------|
| Te begrijpen wat agenten zijn | 01, 02, 03 | 04, 05, 06 |
| Een agent te bouwen die tools gebruikt | 04 | 05, 07, 14 |
| Een RAG-gebaseerde agent te bouwen | 05 | 04, 06, 12 |
| Meerstaps workflows te ontwerpen | 07 | 08, 09, 14 |
| Multi-agent systemen te begrijpen | 08 | 07, 09, 11 |
| Agenten voor productie voor te bereiden | 06, 10 | 12, 13, 18 |
| Protocollen en browserautomatisering te verkennen | 11, 15 | 10, 18 |

Tip: als je nieuw bent met agenten, sla dan geen lessen 01-06 over. Ze geven je de
woordenschat die je nodig hebt voor de rest van de cursus.

## Les-voor-les gids

| Les | Wat je leert | Probeer dit na de les |
|--------|----------------|---------------------------|
| [01 - Intro tot AI-agenten](./01-intro-to-ai-agents/README.md) | Wat een agent anders maakt dan een basis-chatbot. | Leg je demo-idee uit als een agent, niet alleen een chat-app. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | Hoe frameworks helpen met modellen, tools, status en workflows. | Bepaal welke delen van je demo een framework zou beheren. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Veelvoorkomende patronen voor het ontwerpen van agentgedrag. | Schets de gebruikersreis voordat je code schrijft. |
| [04 - Toolgebruik](./04-tool-use/README.md) | Hoe agenten tools aanroepen om data te krijgen of actie te ondernemen. | Definieer één tool die jouw demo-agent nodig zou hebben. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Hoe retrieval agent-antwoorden onderbouwt met documenten of data. | Bepaal welke kennisbron jouw demo moet doorzoeken. |
| [06 - Vertrouwenswaardige agenten](./06-building-trustworthy-agents/README.md) | Hoe je beveiligingsmaatregelen, toezicht en veiliger gedrag toevoegt. | Voeg één regel toe wanneer de agent eerst de gebruiker moet vragen. |
| [07 - Planning ontwerp](./07-planning-design/README.md) | Hoe agenten grotere doelen opsplitsen in kleinere stappen. | Schrijf een plan van drie stappen voor je demo-verzoek. |

| [08 - Multi-Agent Design](./08-multi-agent/README.md) | Wanneer werk te verdelen over gespecialiseerde agenten. | Bepaal of je demo één agent of meerdere nodig heeft. |
| [09 - Metacognition](./09-metacognition/README.md) | Hoe agenten hun eigen output kunnen beoordelen en verbeteren. | Voeg een laatste zelfcontrole toe voordat de agent reageert. |
| [10 - AI Agents in Production](./10-ai-agents-production/README.md) | Wat verandert als een agent van demo naar productie gaat. | Maak een lijst van wat je zou monitoren: kwaliteit, kosten, latency, fouten. |
| [11 - Agentic Protocols](./11-agentic-protocols/README.md) | Hoe protocollen agenten verbinden met tools en andere agenten. | Bepaal waar een standaardprotocol integratie zou kunnen vereenvoudigen. |
| [12 - Context Engineering](./12-context-engineering/README.md) | Hoe context te selecteren, bij te snijden, isoleren en beheren. | Bepaal wat in de prompt hoort en wat moet worden weggelaten. |
| [13 - Agent Memory](./13-agent-memory/README.md) | Hoe agenten nuttige informatie over interacties heen kunnen opslaan. | Kies één veilige voorkeur die je demo zou kunnen onthouden. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Framework-specifieke bouwstenen voor agenten en workflows, plus hosting van LangChain/LangGraph agenten op Microsoft Foundry. | Koppel de demo stappen aan frameworkconcepten. |
| [15 - Computer Use Agents](./15-browser-use/README.md) | Hoe agenten kunnen interageren met browser- of UI-interfaces, inclusief praktijkvoorbeelden zoals Microsoft Project Opal. | Kies één browsertask die nog steeds gebruikersbevestiging nodig heeft. |
| [18 - Securing AI Agents](./18-securing-ai-agents/README.md) | Hoe agent-acties auditabel en vermoedecht te maken. | Bepaal welke acties in je demo gelogd of bevestigd moeten worden. |

Lessons 16 en 17 worden in de hoofd-README vermeld als binnenkort beschikbaar. Voeg ze toe aan je
studieplan zodra de lesinhoud beschikbaar is.

## Belangrijke Ideeën in Beginnersvriendelijke Termen

### Tools

Een tool is iets dat de agent kan aanroepen om werk buiten het model te doen. Een goede tool
heeft een duidelijke naam, een smal takenpakket, getypte invoer, voorspelbare uitvoer en een veilige manier
om te falen.

Voor de cursushelper-demo kan een tool zijn:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG en Kennis

RAG helpt de agent antwoorden te geven vanuit bronmateriaal in plaats van te gokken. In deze
cursus kan dat bronmateriaal bestaan uit les-README's, codevoorbeelden of externe
bronnen die vanuit de lessen gelinkt zijn.

Gebruik RAG wanneer het antwoord gegrond moet zijn op documenten, data of actuele
projectbestanden.

### Planning

Planning is nuttig wanneer de aanvraag uit meer dan één stap bestaat. Houd plannen kort en
zichtbaar genoeg zodat een ontwikkelaar of gebruiker ze kan inspecteren.

Voor de demo kan een plan zijn:

1. Zoek lessen gerelateerd aan toolgebruik.
2. Vat de meest relevante lessen samen.
3. Raad één praktische oefentaak aan.

### Context

Context is wat het model op dit moment ziet. Te weinig context kan ervoor zorgen dat de agent
belangrijke details mist. Te veel context kan de agent traag, duur,
of makkelijker in de war maken.

Goede context-engineering betekent het juiste informatie kiezen voor de volgende model
oproep.

### Geheugen

Geheugen is informatie die voor later wordt opgeslagen. Sla niet alles op. Sla informatie
alleen op als deze nuttig, veilig en gemakkelijk bij te werken of te verwijderen is.

Bijvoorbeeld kan het onthouden van "de leerling geeft de voorkeur aan Python-voorbeelden" nuttig zijn.
Het onthouden van gevoelige persoonlijke gegevens is dat meestal niet.

### Evaluatie en Observeerbaarheid

Evaluatie vraagt: deed de agent het juiste?

Observeerbaarheid vraagt: kunnen we zien hoe het is gegaan?

Voor productie-agenten, houd bij modeloproepen, tooloproepen, opgehaalde context,
latency, kosten, fouten en gebruikersfeedback.

### Vertrouwen en Beveiliging

Betrouwbare agenten hebben meer nodig dan een behulpzame prompt. Gebruik tools met minimale bevoegdheden,
menselijke goedkeuring voor acties met grote impact, gegevensredactie waar nodig, en logs of
bewijzen voor acties die geaudit moeten worden.

## Een 15-Minuten Review Routine

Gebruik deze routine na elke les:

1. **Vat de les samen in één zin.**
2. **Noem de nieuwe agent-capaciteit.** Bijvoorbeeld: toolgebruik, retrieval,
   planning, geheugen, observeerbaarheid of beveiliging.
3. **Voeg het toe aan de cursushelper-demo.** Wat verandert er nu in de demo?
4. **Vind het risico.** Wat kan er misgaan als deze capaciteit verkeerd gebruikt wordt?
5. **Schrijf één toetsvraag.** Hoe zou je controleren dat de agent zich goed gedraagt?

## Snelle Zelfcontrole

Probeer voordat je verder gaat deze vragen te beantwoorden:

1. Wat kan een agent wat een gewone chatbot niet zelf kan?
2. Welke tool zou je agent als eerste nodig hebben, en waarom?
3. Welke kennisbron moet het antwoord van de agent onderbouwen?
4. Welke context moet worden meegenomen in de volgende modeloproep?
5. Wat moet de agent onthouden, en wat moet het vermijden op te slaan?
6. Wanneer moet de agent om menselijke goedkeuring vragen?
7. Welke logs, sporen of ontvangstbewijzen helpen je later bij het debuggen of auditen van de agent?

## Voorgestelde Capstone Oefening

Bouw aan het eind van de cursus een kleine agent die een leerling helpt door deze
repository te navigeren.

Minimale versie:

- Accepteer een onderwerp van de gebruiker.
- Vind de meest relevante lessen.
- Vat samen wat eerst gelezen moet worden.
- Stel één praktische oefentaak voor.
- Toon welke lesbestanden of links zijn gebruikt.

Uitgebreide versie:

- Onthoud de voorkeursprogrammeertaal van de leerling.
- Gebruik een eenvoudig plan voordat je antwoordt.
- Voeg een zelfcontrole-stap toe voor het eindantwoord.
- Log tool-aanroepen en opgehaalde bronnen.
- Vraag om bevestiging voordat je browser- of UI-automatiseringstaken opstart.

Dit geeft je een kleine maar realistische manier om tools, RAG, planning,
context, geheugen, observeerbaarheid en vertrouwen in één project te oefenen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->