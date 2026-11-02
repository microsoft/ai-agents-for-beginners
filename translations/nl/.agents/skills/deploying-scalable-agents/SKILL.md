---
name: deploying-scalable-agents
license: MIT
---
# Schaalbare Agenten Uitrollen met Microsoft Foundry

> Bijbehorende vaardigheid voor [Les 16 – Schaalbare Agenten Uitrollen](../../../16-deploying-scalable-agents/README.md).
> Gebruik deze om een leerling te helpen een agent van prototype naar een schaalbare, observeerbare
> productie-implementatie te verplaatsen. Baseer elke aanbeveling op de lesinhoud en
> het uitvoerbare notitieboek; verzin geen Foundry API's.

## Triggers

Activeer deze vaardigheid wanneer een leerling wil:
- Een agent uitrollen naar Microsoft Foundry als een **gehoste agent** en deze versieerbaar/observeerbaar maken.
- Kiezen tussen **client-hosted, hosted-agent, en agent-workflow** uitrolpatronen.
- **Model routing**, **response caching** of **begrensde gelijktijdigheid** toevoegen om latentie en kosten te beheersen.
- Een **evaluatiepoort** toevoegen zodat een slechte agentversie niet wordt uitgerold.
- Een goedkeuringsstap met **mens-in-de-lus** toevoegen voor risicovolle acties.
- Een agent instrumenteren met **OpenTelemetry** tracing voor productieobserveerbaarheid.
- Een uitgerolde agent **rooktest** doen als een snelle poort na uitrol.

## Kernmodel

Een productie-agent is vooral het operationele skelet *rond* het model (~80%),
niet het model zelf. Koppel elke aanbeveling aan een van deze aandachtspunten:

| Zorgpunt | Prototype → Productie |
|---------|---------------------|
| Hosting | notitieboek → versieerbare gehoste dienst |
| Identiteit | jouw `az login` → beheerde identiteit + gescopeerde RBAC |
| Status | in-memory → extern draad-/geheugenopslag |
| Fout | traceback → retries, fallbacks, alerts |
| Kosten | "een paar cent" → gevolgd, gerouteerd, gecached, begroot |
| Kwaliteit | visuele inspectie → geautomatiseerde evaluatiepoort |
| Vertrouwen | jij keurt goed → beleid + mens-in-de-lus |

## Uitrolpatronen (kies een of combineer)

1. **Client-hosted** — de redeneerlus draait in jouw proces. Maximale controle; jij beheert schaal en status.
2. **Hosted agent (Foundry Agent Service)** — Foundry host de lus, slaat threads op, handhaaft RBAC/contentbeveiliging, toont de agent in het portaal. Minder controle, veel minder operationeel oppervlak.
3. **Agent workflow** — meerdere agenten/tools samengevoegd in een grafiek met vertakkingen, goedkeuringsknopen en duurzame checkpoints.

## Levenscyclus (de lus die een agent implementeert)

`create → versie → evalueren (poort) → gehost uitrollen → online observeren → fouten verzamelen → herhalen`.
**Offline evaluatie is een poort, geen bijzaak** — een versie wordt niet uitgerold
tenzij deze de drempel passeert. Online observeerbaarheid voedt echte fouten terug
in de offline testset.

## Schaal- en kostknoppen (in prioriteitsvolgorde)

1. **Model juist dimensioneren** — gebruik het kleinste model dat de evaluatiepoort haalt.
2. **Routeren op complexiteit** — klein/snel model voor eenvoudige verzoeken, groot model voor echt redeneren (eigen classifier of Foundry Model Router).
3. **Cache** — serveer bijna-duplicate verzoeken zonder modelaanroep.
4. **Stateless ontwerp + begrensde gelijktijdigheid** — externaliseer status; retry met backoff.

## Belangrijke patronen om na te bootsen

Verwijs de leerling naar deze uit het notitieboek
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Request handler**: cache → routeren op complexiteit → trace span → uitvoeren → cache.
- **Evaluatiepoort**: scoor een offline testset; retourneer `pass_rate >= threshold` en rol alleen uit als waar.
- **Menselijke goedkeuring**: `@tool(approval_mode="always_require")` voor acties zoals grote terugbetalingen.
- **Tracing**: wikkel elke aanvraag in `tracer.start_as_current_span(...)` en zet attributen zoals `routed.model`, `customer.id`.

## Rooktesten van een uitgerolde agent

Controleer na uitrol of de endpoint daadwerkelijk reageert (een groene uitrol kan nog steeds
stil zijn). Gebruik de [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
actie via [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
met de catalogus in [`tests/`](../../../tests/README.md). De runner POST elke
prompt naar `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
en controleert op de antwoordtekst. De identiteit heeft de **Azure AI User** rol nodig op
Foundry project scope; het token audience moet `https://ai.azure.com/` zijn.

Leg de poorten op elkaar: **rooktest** (bereikbaar/reagerend, elke uitrol) → **offline
evaluatie** (goed genoeg om uit te rollen, vóór promotie) → **online evaluatie** (hoe
doet het in de praktijk, continu).

## Bedrijfseisen

- **RBAC**: geef elke gehoste agent een beheerde identiteit met minimaal benodigde rechten.
- **MCP in productie**: behandel elke MCP server als een niet-vertrouwde grens — pin de versie, scope de identiteit, valideer outputs, rate-limit, en leg nooit geheimen bloot.

## Beveiligingsmaatregelen voor de assistent

- Geef de voorkeur aan het canonieke `FoundryChatClient(...)` + `provider.as_agent(...)` patroon dat in de hele cursus wordt gebruikt.
- Beloft geen live-Azure resultaten die je niet hebt geverifieerd; raad aan de rooktest-workflow te gebruiken om een uitrol te bevestigen.
- Houd evaluatie en kostenadvies aan elkaar gekoppeld: evaluatie stelt de kwaliteitsvloer vast, routing/caching houden de kosten dichtbij die vloer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->