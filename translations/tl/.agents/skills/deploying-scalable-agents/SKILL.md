---
name: deploying-scalable-agents
license: MIT
description: 'Dalhin ang isang gumaganang prototype ng agent sa isang scalable, observable
  na production deployment sa Microsoft Foundry. Saklaw nito ang mga deployment pattern
  (client-hosted, hosted agents, agent workflows), ang lifecycle ng agent, model routing,
  response caching, evaluation gates, human-in-the-loop approval, observability gamit
  ang OpenTelemetry, cost optimisation, at smoke-testing ng mga deployed na agent
  gamit ang AI Smoke Test action. Batay sa Lesson 16 ng AI Agents for Beginners. GAMITIN
  PARA SA: pag-deploy ng agent sa production, pag-scale ng agent, Microsoft Foundry
  hosted agent, Foundry Agent Service, model routing, response caching, evaluation
  gate, release gate, human approval workflow, agent observability, agent tracing,
  agent cost optimisation, smoke test ng hosted agent, production customer support
  agent. HUWAG GAMITIN PARA SA: pagbuo ng iyong unang agent (simulan sa Lesson 01),
  pagpapatakbo ng mga agent nang lokal sa device (gamitin ang local-ai-agents / Lesson
  17), Azure infrastructure provisioning na hindi kaugnay sa mga agent, mga deployment
  target na hindi sa Foundry.'
---
# Pag-deploy ng Scalable Agents gamit ang Microsoft Foundry

> Kasamang kakayahan para sa [Lesson 16 – Deploying Scalable Agents](../../../16-deploying-scalable-agents/README.md).
> Gamitin ito upang tulungan ang isang nag-aaral na mailipat ang isang agent mula prototype patungo sa scalable, maa-obserbahang
> production deployment. Ibatay ang bawat rekomendasyon sa nilalaman ng aralin at
> ang runnable notebook; huwag mag-imbento ng Foundry APIs.

## Mga Trigger

I-activate ang kakayahang ito kapag nais ng nag-aaral na:
- I-deploy ang isang agent sa Microsoft Foundry bilang **hosted agent** at gawing may bersyon/na-o-obserbahan.
- Piliin sa pagitan ng **client-hosted, hosted-agent, at agent-workflow** na deployment patterns.
- Magdagdag ng **model routing**, **response caching**, o **bounded concurrency** upang kontrolin ang latency at gastos.
- Magdagdag ng **evaluation gate** upang hindi maipadala ang isang masamang bersyon ng agent.
- Maglagay ng hakbang ng **human-in-the-loop approval** para sa mga aksyon na may mataas na panganib.
- Instrumentuhan ang isang agent ng **OpenTelemetry** tracing para sa production observability.
- **Smoke-test** ang isang na-deploy na agent bilang mabilis na gate pagkatapos i-deploy.

## Pangunahing mental model

Ang production agent ay karamihang operational skeleton *sa paligid* ng modelo (~80%),
hindi ang mismong modelo. Iugnay ang bawat rekomendasyon sa isa sa mga concern na ito:

| Concern | Prototype → Production |
|---------|------------------------|
| Hosting | notebook → versioned hosted service |
| Identity | iyong `az login` → managed identity + scoped RBAC |
| State | in-memory → externalised thread/memory store |
| Failure | traceback → retries, fallbacks, alerts |
| Cost | "ilang sentimo" → sinubaybayan, nai-route, na-cache, nabadyet |
| Quality | eyeballing → automated evaluation gate |
| Trust | ikaw ang pumapahintulot → policy + human-in-the-loop |

## Mga deployment pattern (pumili ng isa, o pagsamahin)

1. **Client-hosted** — tumatakbo ang reasoning loop sa iyong proseso. Pinakamataas na kontrol; ikaw ang may-ari ng scaling/state.
2. **Hosted agent (Foundry Agent Service)** — ang Foundry ang nagho-host ng loop, nag-iimbak ng mga thread, nagpapatupad ng RBAC/content safety, ipinapakita ang agent sa portal. Mas kaunting kontrol, mas kaunting operational surface.
3. **Agent workflow** — maraming agents/tools na pinagsama sa isang graph na may branching, approval nodes, at durable checkpoints.

## Lifecycle (ang loop na nagpapadala ng agent)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Ang offline evaluation ay isang gate, hindi lamang panghuli** — hindi maipapadala ang isang bersyon
maliban kung ito ay pumasa sa threshold. Ang online observability ay nagbibigay ng totoong pagkabigo pabalik
sa offline test set.

## Mga scaling at cost lever (sa priority na pagkakasunod)

1. **Tamang laki ng modelo** — gamitin ang pinakamaliit na modelo na pumapasa sa evaluation gate.
2. **Route ayon sa complexity** — maliit/mabilis na modelo para sa mga simpleng kahilingan, malaking modelo para sa totoong pag-iisip (DIY classifier o Foundry Model Router).
3. **Cache** — paglingkuran ang mga halos magkakahiwang kahilingan nang walang model call.
4. **Stateless design + bounded concurrency** — gawing external ang estado; ulitin na may backoff.

## Mga pangunahing pattern na dapat tularan

Ituro sa nag-aaral ang mga ito mula sa notebook
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Request handler**: cache → route ayon complexity → trace span → patakbuhin → cache.
- **Evaluation gate**: iskor ang offline test set; ibalik ang `pass_rate >= threshold` at mag-deploy lamang kung totoo.
- **Human approval**: `@tool(approval_mode="always_require")` para sa mga aksyon tulad ng malalaking refund.
- **Tracing**: balutin ang bawat kahilingan sa `tracer.start_as_current_span(...)` at itakda ang attributes tulad ng `routed.model`, `customer.id`.

## Pagsusuri ng smoke test para sa na-deploy na agent

Pagkatapos i-deploy, tiyaking sasagot talaga ang endpoint (ang berdeng deploy ay maaaring
maging tahimik pa rin). Gamitin ang [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
action sa pamamagitan ng [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
na may katalogo sa [`tests/`](../../../tests/README.md). Ang runner ay ipinapadala ang bawat
prompt sa `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
at nagsusuri sa text ng reply. Kailangang mayroong **Azure AI User** role ang identity sa
saklaw ng Foundry project; ang token audience ay dapat `https://ai.azure.com/`.

I-layer ang mga gate: **smoke test** (maaabot/sumasagot, sa bawat deploy) → **offline
evaluation** (sapat na maganda para ipadala, bago i-promote) → **online evaluation** (paano
ang takbo nito sa aktwal, patuloy).

## Mga kontrol ng enterprise

- **RBAC**: bigyan ang bawat hosted agent ng managed identity na may pinakamababang pribilehiyo.
- **MCP sa production**: ituring ang bawat MCP server bilang hindi pinagkakatiwalaang hangganan — i-pin ang bersyon, tukuyin ang identity nito, i-validate ang mga output, limitahan ang rate, huwag kailanman mag-expose ng mga lihim.

## Mga pananggalang para sa assistant

- Mas paboran ang canonical na `FoundryChatClient(...)` + `provider.as_agent(...)` pattern na ginagamit sa buong kurso.
- Huwag mangako ng live-Azure na resulta na hindi mo pa naverify; irekomenda ang smoke-test workflow upang kumpirmahin ang deployment.
- Panatilihing magkasama ang payo sa evaluation at cost: ang evaluation ang nagtatakda ng kalidad na minimum, habang ang routing/caching ang nagkokontrol ng gastos malapit sa limitasyong iyon.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->