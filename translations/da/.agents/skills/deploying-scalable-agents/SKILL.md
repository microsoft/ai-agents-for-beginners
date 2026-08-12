---
name: deploying-scalable-agents
license: MIT
---
# Udrulning af skalerbare agenter med Microsoft Foundry

> Følgesvendskompetence til [Lektion 16 – Udrulning af skalerbare agenter](../../../16-deploying-scalable-agents/README.md).
> Brug den til at hjælpe en lærende med at flytte en agent fra prototype til en skalerbar, observerbar
> produktionsudrulning. Underbyg hver anbefaling med lektionens indhold og
> den kørende notesbog; opfind ikke Foundry-API'er.

## Triggere

Aktivér denne færdighed, når en lærende ønsker at:
- Udrulle en agent til Microsoft Foundry som en **hostet agent** og gøre den versionsstyret/observerbar.
- Vælge mellem **klient-hostet, hostet agent og agent-workflow** udrulningsmønstre.
- Tilføje **modelruting**, **respons-caching** eller **begrænset samtidighed** for at styre latenstid og omkostninger.
- Tilføje en **evalueringsport** så en dårlig agentversion ikke kan udgives.
- Tilføje et **menneske-i-loop-godkendelsestrin** for højrisikohandlinger.
- Instrumentere en agent med **OpenTelemetry** tracing til produktionsobserverbarhed.
- **Røgt-test** en udrullet agent som en hurtig port efter udrulning.

## Kerne-mindre model

En produktionsagent er mest det operationelle skelet *omkring* modellen (~80%),
ikke selve modellen. Kortlæg hver anbefaling til en af disse bekymringer:

| Bekymring | Prototype → Produktion |
|---------|------------------------|
| Hosting | notesbog → versionsstyret hostet tjeneste |
| Identitet | din `az login` → administreret identitet + scoped RBAC |
| Status | in-memory → eksternt tråd-/hukommelseslager |
| Fejl | traceback → genforsøg, backoffs, alarmer |
| Omkostning | "et par cent" → sporet, rutet, cached, budgetteret |
| Kvalitet | øjekast → automatiseret evalueringsport |
| Tillid | du godkender → politik + menneske-i-loop |

## Udrulningsmønstre (vælg et, eller kombinér)

1. **Klient-hostet** — ræsonneringssløjfen kører i din proces. Maks kontrol; du ejer skalering/status.
2. **Hostet agent (Foundry Agent Service)** — Foundry hoster sløjfen, gemmer tråde, håndhæver RBAC/indholdssikkerhed, viser agenten i portalen. Mindre kontrol, langt mindre operationsflade.
3. **Agent-workflow** — flere agenter/værktøjer sammensat til en graf med forgreninger, godkendelsesnoder og holdbare checkpoints.

## Livscyklus (sløjfen der leverer en agent)

`opret → versioner → evaluer (port) → udrul hostet → observer online → indsamle fejl → gentag`.
**Offline evaluering er en port, ikke en eftertanke** — en version udgives ikke
medmindre den klarer tærsklen. Online observerbarhed fodrer rigtige fejl tilbage
til den offline testsæt.

## Skalerings- og omkostningshåndtag (i prioriteret rækkefølge)

1. **Vælg modelstørrelse korrekt** — brug den mindste model der passerer evalueringsporten.
2. **Ruter efter kompleksitet** — lille/hurtig model til simple forespørgsler, stor model til ægte ræsonnering (DIY klassifikator eller Foundry Model Router).
3. **Cache** — betjen næsten-duplikat-forespørgsler uden modelopkald.
4. **Stateless design + begrænset samtidighed** — eksternaliser status; genforsøg med udskydelse.

## Nøglemønstre der skal genskabes

Peg den lærende hen imod disse fra notesbogen
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Forespørgselsbehandler**: cache → rute efter kompleksitet → trace span → kør → cache.
- **Evalueringsport**: score et offline testsæt; returnér `pass_rate >= threshold` og udrul kun hvis sandt.
- **Menneskelig godkendelse**: `@tool(approval_mode="always_require")` til handlinger som store refunderinger.
- **Tracing**: indpak hver forespørgsel i `tracer.start_as_current_span(...)` og sæt attributter som `routed.model`, `customer.id`.

## Røg-test af en udrullet agent

Efter udrulning, bekræft at endpoint rent faktisk svarer (en grøn udrulning kan stadig være
stille). Brug [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
handlen via [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
med kataloget i [`tests/`](../../../tests/README.md). Køreren POST'er hver
prompt til `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
og tjekker svarets tekst. Identiteten har brug for rollen **Azure AI User** på
Foundry projektomfang; token-auditoriet skal være `https://ai.azure.com/`.

Læg portene lagvis: **røgtest** (tilgængelig/svarende, ved hver udrulning) → **offline
evaluering** (god nok til udrulning, før forfremmelse) → **online evaluering** (hvordan
går det "derude", kontinuerligt).

## Enterprise-kontroller

- **RBAC**: giv hver hostet agent en administreret identitet med mindst privilegium.
- **MCP i produktion**: behandl hver MCP-server som en ikke-pålidelig grænse — fastlås version, afgræns identitet, valider output, rate-limiting, udsæt aldrig hemmeligheder.

## Vogtere for assistenten

- Foretræk det kanoniske `FoundryChatClient(...)` + `provider.as_agent(...)` mønster brugt gennem kurset.
- Lov ikke levende-Azure resultater, du ikke har verificeret; anbefal røgt-test workflowen for at bekræfte en udrulning.
- Hold evaluering og omkostningsråd bundet sammen: evaluering sætter kvalitetsgulvet, routing/caching holder omkostningerne tæt ved det gulv.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->