# Mga Agent Smoke Test

Ang folder na ito ay naglalaman ng **smoke-test na mga katalogo** para sa mga agent na binuo mo sa kurso.
Ang smoke test ay isang mura at mabilis na pagsusuri na ang isang **deployed na Microsoft Foundry hosted
agent** ay naaabot, tumutugon, at sumusunod sa mga pinaka-basic na inaasahan ng prompt nito.
Ito ay unang hadlang — hindi kapalit ng buong evaluation
pipeline na iyong matututuhan sa [Lesson 10](../10-ai-agents-production/README.md) at
[Lesson 16](../16-deploying-scalable-agents/README.md).

Ang mga katalogo ay ginagamit ng [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action sa pamamagitan ng [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
workflow.

## Paano Patakbuhin

1. **I-deploy ang agent ng aralin** sa Microsoft Foundry bilang hosted agent (tingnan
   Lesson 16 para sa deployment workflow). Tandaan ang **pangalan ng agent** at ang iyong
   **Foundry project endpoint**.
2. Idagdag ang mga sumusunod na repository secrets (Settings → Secrets and variables → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Kailangang mayroong **Azure AI User** role
   ang federated identity sa **Foundry project scope**.
3. Mula sa **Actions** tab, patakbuhin ang **Smoke-test hosted agents** at piliin ang
   `tests_file` para sa aralin, pagkatapos ay ilagay ang tumutugmang `agent_name` at
   `project_endpoint`.

## Katalogo → aralin → pangalan ng agent

| Katalogo | Aralin | I-deploy na agent bilang |
|---------|--------|-------------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro to AI Agents](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Tool Use](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Deploying Scalable Agents](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Aling mga aralin ang may smoke tests?

Ang smoke tests ay nalalapat sa mga aralin kung saan ikaw ay **nagde-deploy ng agent** na ang mga tugon sa teksto ay maaaring
masuri laban sa kilalang nilalaman. Ang mga aralin na konseptwal, tumatakbo lamang lokal,
o gumagawa ng hindi tiyak na malikhaing output ay sinasadyang hindi isinama:

- **Lesson 17 (Creating Local AI Agents)** ay tumatakbo nang buong-buo sa iyong workstation gamit ang
  Foundry Local at **hindi** nag-eexpose ng Foundry Responses endpoint, kaya hindi ito
  naaangkop sa aksyon na ito. Suriin ito sa pamamagitan ng pagpapatakbo ng notebook nang lokal.
- Ang mga aralin tungkol sa design-pattern at teorya (02, 03, 06, 07, 09, 12) ay hindi nagpapadala ng kahit isang
  deployable na agent para sa smoke-test.

## Iskema ng Katalogo (mabilisang sanggunian)

Bawat katalogo ay isang JSON na dokumento na may top-level na `tests` array. Bawat entry ay nagpo-post
ng isang prompt at nagsasagawa ng pagpapatunay sa sagot:

| Field | Kahulugan |
|-------|----------|
| `id` | Natatanging identifier ng hakbang na nakalimbag sa log. |
| `description` | Layuning nababasa ng tao. |
| `prompt` | Ang mensaheng ipinadala sa agent. |
| `assertions.status` | Inaasahang HTTP status (default 200). |
| `assertions.contains_any` | Pumasa kung ang tugon ay naglalaman ng alinman sa mga substring na ito. |
| `assertions.contains_all` | Pumasa kung ang tugon ay naglalaman ng bawat substring. |
| `assertions.contains_none` | Pumasa kung ang tugon ay walang anuman sa mga substring na ito. |
| `save_response_id_as` | Itago ang reply id para sa isang susunod na multi-turn na hakbang. |
| `use_previous_response_id` | Ipadala ang pag-ikot na ito bilang nakadugtong sa naka-save na reply id. |

Ang mga assertions ay case-insensitive na pagsusuri ng substring. Tingnan ang
[action documentation](https://github.com/marketplace/actions/ai-smoke-test) para sa
buong iskema, kabilang ang Foundry-managed na mga conversation resource.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->