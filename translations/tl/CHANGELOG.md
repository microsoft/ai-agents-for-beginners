# Tala ng mga Pagbabago

Lahat ng mahalagang pagbabago sa kurso na **AI Agents para sa mga Baguhan** ay naitala sa file na ito.

## [Hindi pa Nailalabas] — 2026-07-06

Inililipat ng bersyong ito ang kurso sa **Azure OpenAI Responses API**, pinapantay ang mga pangalan ng produkto sa **Microsoft Foundry** at ang **Microsoft Agent Framework (MAF)**, tinatanggal ang GitHub Models, ina-update ang mga bersyon ng SDK, at nagdaragdag ng bagong nilalaman tungkol sa mga lokal na modelo at pag-host ng iba pang framework sa Foundry.

### Idinagdag

- **Kasanayan sa paglilipat** — In-install ang [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (mula sa [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sa ilalim ng `.agents/skills/`, kasama ang mga reperensya nito at scanner script.
- **Foundry Local (patakbuhin ang mga modelo sa aparato)** — Bagong seksyon na "Alternative Provider: Foundry Local" sa [00-course-setup/README.md](./00-course-setup/README.md) na sumasaklaw sa pag-install (`winget` / `brew`), `foundry model run`, ang `foundry-local-sdk`, at pagsasama ng `FoundryLocalManager` sa Microsoft Agent Framework sa pamamagitan ng `OpenAIChatClient`.
- **Pagho-host ng LangChain / LangGraph agents sa Microsoft Foundry** — Bagong seksyon sa [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) at isang tumatakbong halimbawa na [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) gamit ang `langchain-azure-ai[hosting]` at `ResponsesHostServer` (ang `/responses` na protocol), batay sa [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Bagong seksyon na "Real-World Example: Microsoft Project Opal" sa [15-browser-use/README.md](./15-browser-use/README.md) na inilalarawan ang Opal bilang isang enterprise computer-use agent at iniugnay ito sa mga konsepto ng kurso (human-in-the-loop, trust/security, planning, Skills).
- **Ikalawang Lesson 02 Python sample** — Idinagdag ang [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (tingnan ang "Binago" — inilipat mula sa dating Semantic Kernel notebook) at nilink ito sa lesson README.
- Seksiyon ng **Models and Providers** na idinagdag sa [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Binago

- **Chat Completions → Responses API (Python).** Ang mga sample na direktang tumawag sa modelo ay inilipat mula sa Chat Completions patungong Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), gamit ang `OpenAI` client laban sa matatag na Azure OpenAI `/openai/v1/` endpoint (walang `api_version`). Kasama sa mga apektadong sample ang:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — ang buong walkthrough ng function-calling (tool schema na nilapad sa format ng Responses, mga resulta ng tool na ibinalik bilang `function_call_output`, `max_output_tokens`, atbp.).
- **GitHub Models → Azure OpenAI.** Itinakwil na ang GitHub Models (magwawakas sa **Hulyo 2026**) at hindi sinusuportahan ang Responses API. Lahat ng mga code path ng GitHub Models ay kinonvert sa Azure OpenAI / Microsoft Foundry sa mga Python at .NET na sample:
  - Python: Mga workflow notebook ng Lesson 08 (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + mga kaakibat na `.md` docs, at ang mga Lesson 08 dotNET workflow notebooks/`.md` (`01`–`03`) ay ngayon gumagamit ng `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` gamit ang `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Ang dating `02-semantic-kernel.ipynb` ay isinalin upang gamitin ang Microsoft Agent Framework na may Azure OpenAI (Responses API) at pinalitan ang pangalan sa `02-python-agent-framework-azure-openai.ipynb`.
- **Pinantay sa `FoundryChatClient` + `as_agent`.** Ang README at notebook code na nag-reference sa `AzureAIProjectAgentProvider` ay pinantay sa kanonikong pattern na ginamit ng Lesson 01 at sariling mga sample ng framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` na may `provider.as_agent(...)`. Na-update ito sa Lesson 02–14 READMEs at notebooks (hal., memorya sa Lesson 13, lahat ng Lesson 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Pangalan ng produkto.** Pinalitan ang pangalan sa buong English na nilalaman:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Hindi nagbago: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", at mga pangalan ng environment-variable.)
- **Mga dependency** ([requirements.txt](../../requirements.txt)):
  - Naka-pin ang `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Naka-pin ang `openai>=1.108.1` (minimum para sa Responses API).
  - Tinanggal ang `azure-ai-inference` (ginamit lang sa mga migrated na GitHub Models sample).
- **Pag-configure ng environment** ([.env.example](../../.env.example)): tinanggal ang mga variable ng GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); idinagdag ang `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, at opsyonal na `AZURE_OPENAI_API_KEY`; in-update ang pangalang sa Microsoft Foundry.
- **Mga dokumento** — In-update ang [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), at [STUDY_GUIDE.md](./STUDY_GUIDE.md) para sa mga nabanggit sa itaas (pagsesetup ng env vars, snippet sa beripikasyon, gabay sa provider, pangalan).

### Tinanggal

- Mga hakbang sa pag-onboard ng GitHub Models at mga environment variable mula sa mga setup na dokumento (pinalitan ng Azure OpenAI / Microsoft Foundry).

### Seguridad / Privacy (paglilinis para sa pampublikong pagbabahagi)

- Nilinis ang mga resulta ng pagpapatupad ng Jupyter notebook na naglalabas ng totoong **Azure subscription ID**, mga pangalan ng resource-group / resource, at Bing connection ID, pati na rin ang developer **local file paths at mga username**, sa:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Sinuri na walang API keys, tokens, subscription IDs, o personal paths ang nananatili sa nasubaybayang English na nilalaman (ang mga reperensya sa `GITHUB_TOKEN` na nandoon ay ang GitHub Actions token sa mga workflow at ang GitHub MCP server PAT sa Lesson 11 setup — parehong lehitimo at walang kinalaman sa GitHub Models).

### Mga Tala at Kilalang Limitasyon

- **Hindi pinatakbo/na-compile.** Ito ay mga sample na pang-edukasyon na na-update para sa tama na API/pangalan; hindi ito pinatakbo laban sa live na Azure resources, at ang mga sample ng .NET ay hindi na-compile sa kapaligirang ito. Siguraduhing i-validate laban sa iyong sariling Microsoft Foundry / Azure OpenAI deployment.
- **Dapat suportahan ng deployment ng modelo ang Responses API.** Gumamit ng deployment tulad ng `gpt-4o-mini`, `gpt-4.1`, o isang `gpt-5.x` na modelo. Ang mga mas lumang modelo ay sumusuporta sa pangunahing functionality ng Responses ngunit hindi lahat ng mga tampok.
- **Bersyon ng agent-framework.** Ang mga sample ay nakatuon sa pinakabagong MAF (`>=1.10.0`). Ang kanonikong pagtawag sa paggawa ng agent ay `client.as_agent(...)`; na-validate ang mga API laban sa inilathalang dokumento ng framework at isang naka-install na build. Kung pipili ka ng ibang bersyon, siguraduhing kumpirmahin ang availability ng paraan (`as_agent` laban sa `create_agent`).
- **Lesson 08 workflow notebook 04** ay sinadyang pinananatili ang `AzureAIAgentClient` (mula sa `agent-framework-azure-ai`) dahil ginagamit nito ang mga tools na naka-host sa Microsoft Foundry Agent Service (Bing grounding, code interpreter); ito ay batay na sa Responses.
- **Default deployment sa .NET.** Dalawang Lesson 08 dotNET workflow sample na dati ay hard-coded ang `gpt-4o`; ngayon ay default na sa `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Kung umaasa ang sample sa multimodal/vision input, itakda ang `AZURE_OPENAI_DEPLOYMENT` sa angkop na modelo.
- **Foundry Local** ay naglalantad ng OpenAI-compatible na **Chat Completions** endpoint at nilalayong gamitin para sa lokal na pagde-develop; gamitin ang Azure OpenAI / Microsoft Foundry para sa buong feature set ng Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->