---
name: local-ai-agents
license: MIT
description: 'Bumuo ng mga local-first AI agents na tumatakbo nang buong-buo sa isang
  developer workstation gamit ang Microsoft Foundry Local at Qwen function-calling
  models. Saklaw nito ang Small Language Models (SLMs), ang OpenAI-compatible na lokal
  na endpoint, sandboxed local tools, lokal na RAG gamit ang Chroma, lokal na MCP
  servers, hybrid cloud/local routing, at ang privacy/cost/offline trade-offs. Batay
  sa Lesson 17 ng AI Agents for Beginners. GAMITIN PARA SA: pagpapatakbo ng agent
  nang lokal, offline agent, on-device agent, Foundry Local, Qwen function calling,
  local tool calling, lokal na RAG, Chroma vector database, lokal na MCP server, privacy-preserving
  agent, hybrid local at cloud agent, small language model agent, engineering assistant
  sa aking makina. HUWAG GAMITIN PARA SA: pag-deploy ng mga agents sa cloud nang malakihan
  (gamitin ang deploying-scalable-agents / Lesson 16), paggawa ng iyong unang agent
  concept (Lesson 01), Foundry (cloud) hosted agents, GPU cluster / server-side inference
  provisioning.'
---
# Paglikha ng Lokal na AI Agents gamit ang Foundry Local at Qwen

> Kasama sa kasanayan para sa [Lesson 17 – Paglikha ng Lokal na AI Agents](../../../17-creating-local-ai-agents/README.md).
> Gamitin ito upang tulungan ang isang nag-aaral na bumuo ng isang ahente na nagrerason, tumatawag ng mga tool, at naghahanap ng
> dokumentasyon nang buong mag-isa sa kanilang sariling makina — walang cloud inference. Ibatay ang bawat
> rekomendasyon sa nilalaman ng leksyon at ang tumatakbong notebook.

## Mga Trigger

Isaaktibo ang kasanayang ito kapag nais ng nag-aaral na:
- Patakbuhin ang isang ahente **nangang buong-on-device** para sa privacy, gastos, o offline na dahilan.
- Maglingkod ng isang modelo nang lokal gamit ang **Foundry Local** at kumonekta sa pamamagitan ng compatible endpoint ng OpenAI.
- Gumamit ng **Qwen function-calling** na modelo upang magpatakbo ng maaasahang lokal na pagtawag sa mga tool.
- Magdagdag ng **local RAG** (Chroma) o isang **local MCP server**.
- Magdisenyo ng isang **hybrid** na lokal/cloud routing strategy.

## Pangunahing mental na modelo

Ang isang SLM ay nagtutuko ng lawak para sa privacy, gastos, at offline na operasyon. Ang panalong
estratehiya: **hayaan ang SLM ang mag-orchestrate at hayaan ang mga tool ang gumawa ng mabibigat na gawain.** Ang
modelo ay hindi kailangang *maalam* sa codebase — kailangan lang nitong malaman kung kailan tatawagin
`read_file` at `search_docs`. Ito ay nakatuon sa lakas ng SLM (mga limitadong desisyon
tulad ng pagpili ng tool) at inilalayo sa kahinaan nito (malawak na kaalaman, mahaba at multi-hop
na pangangatwiran).

## Bakit ang mga partikular na bahagi na ito

- Ang **Foundry Local** ay naglalantad ng isang **OpenAI-compatible HTTP endpoint**, kaya ang code ng cloud agent ay naililipat lamang sa pamamagitan ng pagpapalit ng `base_url` (at paggamit ng lokal na placeholder na API key). Awtomatikong pinipili rin nito ang pinakamahusay na build (CPU/GPU/NPU) para sa makina.
- Ang mga modelo ng **Qwen** ay sinanay para sa function calling at naglalabas ng maayos na porma ng mga pagtawag sa tool nang pare-pareho — ito ang nagpapalit ng isang lokal na *chat* na modelo sa isang lokal na *agent*.
- Ang **Chroma** ay tumatakbo sa proseso at nag-iimbak ng mga vectors sa disk, kaya ang buong RAG pipeline (embed → store → retrieve → reason) ay nananatiling lokal.
- Ang **MCP** ay isang transport, hindi isang cloud service: ang MCP server ay maaaring tumakbo nang lokal sa `stdio`.

## Mga kailangan para sa setup

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # lokal na placeholder
```

~8 GB RAM ang isang realistiko at minimum; nakakatulong ang GPU/NPU pero hindi kinakailangan.

## Mga susi na pattern na dapat kopyahin

Ituro ang nag-aaral sa notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Sandboxed tools**: bawat file tool ay nagtutukoy ng mga path at tinatanggihan ang anuman sa labas ng isang solong ugat na proyekto — kahit lokal, ang tool ay tumatakbo gamit ang mga pahintulot ng user.
- **Tool-calling loop**: irehistro ang mga tool gamit ang OpenAI tools schema, patakbuhin ang hinihiling na mga tool nang lokal, ibalik ang mga resulta, ulitin hanggang sa makakuha ng pinal na sagot.
- **Local RAG**: mag-upsert ng mga docs sa isang Chroma collection; `search_docs` ay nagbabalik ng mga nangungunang top-k chunks.
- **Local MCP**: kumonekta sa isang lokal na server gamit ang `stdio`; itakda ito sa isang proyekto na direktoryo at patunayan ang mga output nito.

## Hybrid na routing (lokal bilang isa sa mga modelo)

| Sitwasyon | Saan ito tumatakbo |
|-----------|---------------|
| Sensitibong datos / offline | Lokal na SLM |
| Simple, limitadong gawain | Lokal na SLM (murang, mabilis) |
| Mahirap na multi-hop na pangangatwiran sa hindi sensitibong data | Cloud model |
| Cloud outage | Lokal na SLM (maayos na pagbaba ng kalidad) |

Ito ay sumasalamin sa ideya ng model-routing mula sa Lesson 16, gamit ang workstation bilang isa
sa mga ruta. Piliin ang mga disenyo na bumabalik sa lokal para ang ahente ay bumaba sa
kalidad sa halip na tuluyang mabigo.

## Mga guardrail para sa katulong

- Panatilihin ang bawat operasyon sa file/tool na saklaw lamang ng isang sandboxed na direktoryo ng proyekto.
- Huwag magpadala ng code o datos sa cloud kapag ang layunin ng nag-aaral ay privacy/offline — panatilihin ang buong pipeline nang lokal.
- Magtakda ng realistiko na mga inaasahan para sa kalidad ng SLM; umasa sa mga tool at RAG sa halip na ang naalala ng modelo na kaalaman.
- Tandaan na ang Lesson 17 ay **walang** Foundry Responses endpoint, kaya ang cloud smoke-test action ay hindi nalalapat — patunayan ito sa pamamagitan ng pagpapatakbo ng notebook nang lokal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->