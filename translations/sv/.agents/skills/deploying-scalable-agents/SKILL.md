---
name: deploying-scalable-agents
license: MIT
---
# Distribuera Skalbara Agenter med Microsoft Foundry

> Följeslagarfärdighet för [Lektion 16 – Distribuera Skalbara Agenter](../../../16-deploying-scalable-agents/README.md).
> Använd den för att hjälpa en lärande att flytta en agent från prototyp till en skalbar, observerbar
> produktionsdistribution. Grundlägg varje rekommendation i lektionsinnehållet och
> den körbara notebooken; uppfinna inte Foundry-API:er.

## Triggers

Aktivera denna färdighet när en lärande vill:
- Distribuera en agent till Microsoft Foundry som en **hostad agent** och göra den versionshanterad/observerbar.
- Välja mellan **klienthostad, hostad agent och agentarbetsflöde** distributionsmönster.
- Lägg till **modellroutning**, **svarscachning** eller **begränsad samtidighet** för att kontrollera latens och kostnad.
- Lägg till en **utvärderingsgrind** så att en dålig agentversion inte kan levereras.
- Lägg till ett **människa-i-loopen-godkännande** steg för riskfyllda åtgärder.
- Instrumentera en agent med **OpenTelemetry** spårning för produktionsobserverbarhet.
- **Rök-test** en distribuerad agent som en snabb post-distributionsgrind.

## Kärnmental modell

En produktionsagent är mestadels den operativa skelettet *runt* modellen (~80%),
inte modellen själv. Karta varje rekommendation till en av dessa aspekter:

| Aspekt | Prototyp → Produktion |
|---------|------------------------|
| Hostning | notebook → versionshanterad hostad tjänst |
| Identitet | din `az login` → hanterad identitet + scopes RBAC |
| Tillstånd | i minne → extern tråd/minneslagring |
| Fel | traceback → omförsök, fallback, varningar |
| Kostnad | "några cent" → spårad, routad, cachad, budgeterad |
| Kvalitet | ögonbedömning → automatiserad utvärderingsgrind |
| Tillit | du godkänner → policy + människa-i-loopen |

## Distributionsmönster (välj ett, eller kombinera)

1. **Klienthostad** — resonemangsloopen körs i din process. Max kontroll; du äger skalning/tillstånd.
2. **Hostad agent (Foundry Agent Service)** — Foundry hostar loopen, lagrar trådar, genomdriver RBAC/innehållssäkerhet, visar agenten i portalen. Mindre kontroll, mycket mindre operativ yta.
3. **Agentarbetsflöde** — flera agenter/verktyg sammansatta i en graf med förgreningar, godkännandenoder och hållbara checkpoints.

## Livscykel (loopen som levererar en agent)

`skapa → versionera → utvärdera (grind) → distribuera hostad → observera online → samla fel → upprepa`.
**Offlineutvärdering är en grind, inte en eftertanke** — en version levereras inte
om den inte klarar tröskeln. Onlineobserverbarhet matar verkliga fel tillbaka
in i offline testuppsättningen.

## Skalnings- och kostnadsreglage (i prioriteringsordning)

1. **Rättstorlek modellen** — använd den minsta modellen som klarar utvärderingsgrinden.
2. **Routa efter komplexitet** — liten/snabb modell för enkla förfrågningar, stor modell för verklig resonemang (Gör själv-klassificerare eller Foundry Model Router).
3. **Cache** — servera nästan dubblettförfrågningar utan ett modellanrop.
4. **Stateless design + begränsad samtidighet** — externalisera tillstånd; försök igen med backoff.

## Nyckelmönster att reproducera

Peka den lärande på dessa från notebooken
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Förfrågningshanterare**: cache → routa efter komplexitet → spårningsspan → kör → cache.
- **Utvärderingsgrind**: poängsätt en offline testuppsättning; returnera `pass_rate >= threshold` och distribuera endast om sant.
- **Mänskligt godkännande**: `@tool(approval_mode="always_require")` för åtgärder som stora återbetalningar.
- **Spårning**: wrappa varje förfrågan i `tracer.start_as_current_span(...)` och sätt attribut som `routed.model`, `customer.id`.

## Rök-test av en distribuerad agent

Efter distribution, verifiera att slutpunkten faktiskt svarar (en grön distribution kan fortfarande vara
tyst). Använd [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
åtgärden via [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
med katalogen i [`tests/`](../../../tests/README.md). Köraren gör POST på varje
prompt till `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
och kontrollerar svarstexten. Identiteten behöver rollen **Azure AI User** på
Foundry-projektomfånget; tokenpubliken måste vara `https://ai.azure.com/`.

Stapla grindarna: **rök-test** (nåbar/svarande, varje distribution) → **offline
utvärdering** (tillräckligt bra för att levereras, före promotion) → **online utvärdering** (hur
går det i det vilda, kontinuerligt).

## Företagskontroller

- **RBAC**: ge varje hostad agent en hanterad identitet med minsta privilegium.
- **MCP i produktion**: behandla varje MCP-server som en otrorisk gräns — fäst versionen, scopa dess identitet, validera utdata, hastighetsbegränsa, exponera aldrig hemligheter.

## Skydd för assistenten

- Föredra det kanoniska `FoundryChatClient(...)` + `provider.as_agent(...)` mönstret som används genom kursen.
- Lovar inte live-Azure-resultat du inte verifierat; rekommendera rök-testarbetsflödet för att bekräfta en distribution.
- Håll utvärdering och kostnadsråd kopplade: utvärdering sätter kvalitetsgolvet, routing/cachning håller kostnader nära det golvet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->