---
name: deploying-scalable-agents
license: MIT
---
# Distribuering av skalerbare agenter med Microsoft Foundry

> Kompaniansferdighet for [Leksjon 16 – Distribuering av skalerbare agenter](../../../16-deploying-scalable-agents/README.md).
> Bruk den for å hjelpe en elev med å flytte en agent fra prototype til en skalerbar, observerbar
> produksjonsdistribuering. Grunnfest alle anbefalinger i leksjonsinnholdet og
> den kjørbare notatboken; oppfinn ikke Foundry-APIer.

## Utløsere

Aktiver denne ferdigheten når en elev ønsker å:
- Distribuere en agent til Microsoft Foundry som en **hostet agent** og gjøre den versjonert/observerbar.
- Velge mellom **klient-hostet, hostet-agent, og agent-arbeidsflyt** distribusjonsmønstre.
- Legge til **modellruting**, **respons-caching**, eller **begrenset samtidighet** for å kontrollere ventetid og kostnad.
- Legge til en **evalueringsport** slik at en dårlig agentversjon ikke kan distribueres.
- Legge til et **menneske-i-sløyfen godkjenningssteg** for handlinger med høy risiko.
- Instrumentere en agent med **OpenTelemetry** tracing for produksjonsovervåkbarhet.
- **Røyktest** en distribuert agent som en rask port etter distribusjon.

## Kjernemodell

En produksjonsagent er stort sett det operative rammeverket *rundt* modellen (~80%),
ikke modellen selv. Kartlegg hver anbefaling til en av disse bekymringene:

| Bekymring | Prototype → Produksjon |
|---------|------------------------|
| Hosting | notatbok → versjonert hostet tjeneste |
| Identitet | din `az login` → administrert identitet + avgrenset RBAC |
| Tilstand | i minnet → ekstern tråd/minnelager |
| Feil | feilsporing → retry, fallback, varsler |
| Kostnad | "noen cent" → sporet, rutet, cachet, budsjettert |
| Kvalitet | vurdering med øye → automatisert evalueringsport |
| Tillit | du godkjenner → policy + menneske-i-sløyfen |

## Distribusjonsmønstre (velg ett, eller kombiner)

1. **Klient-hostet** — resonnementsløkken kjører i din prosess. Maks kontroll; du eier skalering/tilstand.
2. **Hostet agent (Foundry Agent Service)** — Foundry hoster løkken, lagrer tråder, håndhever RBAC/innholdssikkerhet, viser agenten i portalen. Mindre kontroll, betydelig mindre operativ overflate.
3. **Agent-arbeidsflyt** — flere agenter/verktøy komponert inn i en graf med forgreninger, godkjenningsnoder og varige sjekkpunkter.

## Livssyklus (løkken som distribuerer en agent)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Offline evaluering er en port, ikke en ettertanke** — en versjon distribueres ikke
med mindre den passerer terskelen. Online observerbarhet mater virkelige feil
tilbake inn i offline testsettet.

## Skalerings- og kostnadsutløser (i prioritert rekkefølge)

1. **Riktig dimensjonering av modellen** — bruk den minste modellen som passerer evalueringsporten.
2. **Ruting etter kompleksitet** — liten/rask modell for enkle forespørsler, stor modell for ekte resonnement (DIY-klassifiserer eller Foundry Model Router).
3. **Cache** — besvar nesten-dupliserte forespørsler uten modellkall.
4. **Stateless design + begrenset samtidighet** — eksterngjør tilstand; forsøk på nytt med tilbakefall.

## Viktige mønstre å gjenskape

Pek læreren til disse fra notatboken
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Forespørselsbehandler**: cache → ruting etter kompleksitet → trace span → kjør → cache.
- **Evalueringsport**: score et offline testsett; returner `pass_rate >= threshold` og distribuer kun hvis sant.
- **Menneskelig godkjenning**: `@tool(approval_mode="always_require")` for handlinger som store refusjoner.
- **Tracing**: pakk hver forespørsel i `tracer.start_as_current_span(...)` og sett attributter som `routed.model`, `customer.id`.

## Røyktesting av en distribuert agent

Etter distribusjon, verifiser at endepunktet faktisk svarer (en grønn distribusjon kan fortsatt være
taus). Bruk [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
handlingen via [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
med katalogen i [`tests/`](../../../tests/README.md). Runneren poster hver
prompt til `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
og sjekker svareteksten. Identiteten trenger **Azure AI User**-rollen på
Foundry prosjektomfang; token-mottaker må være `https://ai.azure.com/`.

Legg lag på lag: **røyktest** (tilgjengelig/svarer, hver distribusjon) → **offline
evaluering** (god nok til distribusjon, før promotering) → **online evaluering** (hvordan
går det ute i felt, kontinuerlig).

## Enterprise-kontroller

- **RBAC**: gi hver hostede agent en administrert identitet med minst privilegium.
- **MCP i produksjon**: behandle hver MCP-server som en upålitelig grense — frys versjonen, avgrens identiteten, valider utdata, rate-begrens, aldri eksponer hemmeligheter.

## Sikringsmekanismer for assistenten

- Foretrekk det kanoniske `FoundryChatClient(...)` + `provider.as_agent(...)`-mønsteret brukt i hele kurset.
- Ikke lov liv-Azure-resultater du ikke har verifisert; anbefal røyktest-prosedyren for å bekrefte en distribusjon.
- Hold evaluering og kostnadsråd bundet sammen: evalueringen setter kvalitetsgulvet, ruting/caching holder kostnaden nær det gulvet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->