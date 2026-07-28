# Tala ng Pagbabago

Ang lahat ng mga kapansin-pansing pagbabago sa kursong **AI Agents for Beginners** ay naitala sa file na ito.

## [Inilabas] — 2026-07-14

Ang paglabas na ito ay inilipat ang kurso mula sa dalawang bagong-deprecated na mga modelo, inilipat ang mga natitirang Lesson notebooks sa matatag na Microsoft Agent Framework API, at pinatunayan ang mga Python notebooks laban sa buhay na deployment ng Microsoft Foundry.

### Binago

- **Inilipat mula sa deprecated na mga modelo (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Parehong `gpt-4.1` at `gpt-4.1-mini` ay ngayon deprecated na (nakapaskil na petsa ng pagreretiro **14 Oktubre 2026**). Pinalitan ang bawat reference sa kurso (docs, `.env.example`, Python/.NET notebooks at mga halimbawa) gamit ang hindi deprecated na `gpt-5-mini`. Ang halimbawa ng model-routing ng Lesson 16 ay nagtataglay ng maliit/malaki na pagkakaiba gamit ang `gpt-5-nano` (maliit) at `gpt-5-mini` (malaki). Ang mga na-vendor na third-party na files ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), kasaysayan ng GitHub Models text, at mga tala ng kakayahan ng `azure-openai-to-responses` skill ay sinadyang iniwan nang hindi nabago.
- **Inilipat ang Lesson 14 handoff notebook sa matatag na API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) ay ngayon gumagamit ng `agent_framework.orchestrations.HandoffBuilder` na may `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming na batay sa `event.type`, at `FoundryChatClient` (pinalitan ang tinanggal na pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` na mga simbolo).
- **Inilipat ang Lesson 14 human-in-the-loop notebook sa matatag na API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) ay ngayon nagpapahinto gamit ang `ctx.request_info(...)` + `@response_handler` (pinalitan ang tinanggal na `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), binubuo gamit ang `WorkflowBuilder(start_executor=..., output_executors=[...])`, nagmamaneho ng istrakturang output gamit ang `default_options={"response_format": ...}`, at gumagamit ng scripted answer para tumakbo nang walang nanny (walang blocking `input()`).
- **Environment configuration** ([.env.example](../../.env.example)): inilipat ang mga pangalan ng model deployment sa `gpt-5-mini`; idinagdag ang `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Lesson 16 routing) at ang dating nawawalang `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Lesson 15 browser-use).
- **Dependencies** ([requirements.txt](../../requirements.txt)): pinirmi ang `agent-framework`, `agent-framework-foundry`, at `agent-framework-openai` sa `~=1.10.0` para sa isang self-consistent, validated na set (1.11.0 ay naglalabas ng experimental na breaking changes sa mga surface na ginagamit ng mga lesson na ito).

### Mga Tala at Kilalang Limitasyon

- **Pinatunayan laban sa buhay na Microsoft Foundry.** Ang mga Python notebooks ay naipatupad ng headlessly gamit ang `nbconvert` laban sa isang Microsoft Foundry project gamit ang `gpt-5-mini` (at `gpt-5-nano` para sa Lesson 16 routing). Mag-deploy ng katumbas na hindi deprecated na mga modelo sa iyong sariling proyekto; binabasa ng mga notebook ang deployment name mula sa `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Kailangan pa rin ng karagdagang mga resources para sa ilang lessons.** Kinakailangan ng Lesson 05 ang Azure AI Search; ang Lesson 08 Bing-grounding workflow (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) ay nangangailangan ng koneksyon sa Bing at ng Microsoft Foundry Agent Service na mga hosting tools; kinakailangan ng Lesson 13 (Cognee) at Lesson 17 (Foundry Local) ang kanilang sariling mga runtime.

## [Inilabas] — 2026-07-13

Ang paglabas na ito ay nagdadagdag ng dalawang bagong lessons na kumukumpleto sa deployment arc — pagpapalaki ng mga agent sa Microsoft Foundry at pagpapaliit sa isang workstation lamang — plus isang smoke-test pipeline, bagong-bagong navigation ng kurso, mga bagong kasanayan para sa mag-aaral, at na-update na branding.

### Idinagdag

- **Lesson 16 — Pag-deploy ng Scalable Agents gamit ang Microsoft Foundry.** Bagong lesson [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) at runnable notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) na bumubuo ng isang production customer-support agent (tools, RAG, memorya, model routing, caching ng tugon, pag-apruba ng tao, isang evaluation gate, at OpenTelemetry tracing), kasama ang development/deployment/runtime na Mermaid diagrams, knowledge check, assignment, at challenge.
- **Lesson 17 — Paglikha ng Lokal na AI Agents gamit ang Foundry Local at Qwen.** Bagong lesson [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) at notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) na bumubuo ng ganap na on-device engineering assistant (Qwen function calling via Foundry Local, sandboxed file tools, local RAG gamit ang Chroma, opsyonal na local MCP), may mga diagram para lamang sa local / local-RAG / tool-calling, knowledge check, assignment, at challenge.
- **Smoke-test pipeline.** Bagong [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) pati na rin ang mga per-lesson catalogs sa ilalim ng [tests/](./tests/README.md) para sa mga deployable agents sa Lessons 01, 04, 05, at 16, kasama ang index README na nagmamapa sa bawat catalog sa lesson at hosted-agent na pangalan. Nakakuha ang Lesson 16 ng seksyon na "Validating a Deployed Agent with Smoke Tests"; nakuha ng Lessons 01/04/05 ang opsyonal na pointer para sa smoke-test.
- **Mga kasanayan para sa mag-aaral.** Bagong Agent Skills sa ilalim ng `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (na naglalaman ng mga gabay ng Lesson 16 at 17), at [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kung paano patunayan ang mga notebook samples laban sa buhay na Microsoft Foundry / Azure OpenAI setup).
- **Notebook validation runner.** Bagong [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) na nagpapatakbo ng bawat Python notebook headlessly gamit ang `nbconvert` at nagpi-print ng PASS/FAIL na matrix (kasama ang `results.json`). Awtomatikong dinedetect ang repo root at Python, hindi isinama ang mga hindi pang-kurso na notebooks (`.venv`, `site-packages`, `translations`, skill template assets) at mga `.NET` notebooks bilang default, at sumusuporta sa `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, at `-Python`.
- **Navigation ng kurso.** Idinagdag ang mga Prev/Next lesson links sa Lessons 11–15 (na dating wala) kaya ang buong kurso ay nag-uugnay mula 00 → 18 sa parehong direksyon.
- **Bagong mga thumbnail.** Mga lesson thumbnail para sa Lessons 16 at 17, kasama ang na-refresh na repository social image [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (na nag-aanunsyo ngayon ng dalawang bagong lessons at ng `aka.ms/ai-agents-beginners` URL).
- **Dependencies** ([requirements.txt](../../requirements.txt)): idinagdag ang `foundry-local-sdk` at `chromadb` para sa Lesson 17.

### Binago

- **Pangunahing [README.md](./README.md)** lesson table: Ang Lessons 16 at 17 ay ngayon naka-link sa kanilang nilalaman (na dati ay "Darating Na"); ang repository image ay pinalitan sa `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: Idinagdag ang Lessons 16 at 17 sa gabay ng lesson-bilang-lesson at mga learning paths, pati na rin ang seksyong "Validating Deployed Agents with Smoke Tests".
- **[AGENTS.md](./AGENTS.md)**: in-update ang bilang ng lesson/deskripsyon (00–18), idinagdag ang seksyon para sa smoke-testing validation, at idinagdag ang mga halimbawa ng pagnenaming ng Lesson 16/17 sample.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: Ang "Previous Lesson" ay ngayon tumuturo sa Lesson 17 (dating Lesson 15), pinagsasara ang chain.
- **Nakapag-standarisang mga reference sa modelo para sa mga hindi deprecated na modelo.** Pinalitan lahat ng `gpt-4o` / `gpt-4o-mini` references sa buong kurso (docs, `.env.example`, Python/.NET notebooks at mga halimbawa) gamit ang `gpt-4.1-mini` — ang `gpt-4o` (lahat ng bersyon) ay magreretiro sa 2026. Ang halimbawa ng model-routing ng Lesson 16 ay nagtataglay ng maliit/malaki na pagkakaiba gamit ang `gpt-4.1-mini` (maliit) at `gpt-4.1` (malaki). Ang mga Python notebooks ay ngayon pumipili ng modelo mula sa mga environment variables (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) sa halip na naka-hardcode ang pangalan ng modelo.

### Mga Tala at Kilalang Limitasyon

- **Hindi pinatakbo laban sa buhay na Azure.** Ang mga bagong lesson notebooks ay mga educational samples; patakbuhin at patunayan ito laban sa sarili mong Microsoft Foundry / Foundry Local setup. Ang smoke-test workflow ay nangangailangan na i-deploy mo ang lesson agent at i-configure ang Azure OIDC secrets (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) na may **Azure AI User** role sa Foundry project scope.
- **Ang Lesson 17 ay para lamang sa local.** Wala itong Foundry Responses endpoint, kaya ang smoke-test action ay hindi naangkop; patunayan ito sa pamamagitan ng pagpapatakbo ng notebook sa iyong workstation.

## [Inilabas] — 2026-07-06

Ang paglabas na ito ay inilipat ang kurso sa **Azure OpenAI Responses API**, nag-standardize ng product naming sa **Microsoft Foundry** at ang **Microsoft Agent Framework (MAF)**, nagretiro ng GitHub Models, nag-update ng mga bersyon ng SDK, at nagdagdag ng bagong nilalaman tungkol sa mga local na modelo at pagho-host ng ibang mga framework sa Foundry.

### Idinagdag

- **Migration skill** — In-install ang [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (mula sa [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sa ilalim ng `.agents/skills/`, kasama ang mga reference at scanner script nito.
- **Foundry Local (patakbuhin ang mga modelo on-device)** — Bagong seksyong "Alternative Provider: Foundry Local" sa [00-course-setup/README.md](./00-course-setup/README.md) na sumasaklaw sa pag-install (`winget` / `brew`), `foundry model run`, ang `foundry-local-sdk`, at pag-wiring ng `FoundryLocalManager` sa Microsoft Agent Framework gamit ang `OpenAIChatClient`.
- **Pagho-host ng LangChain / LangGraph agents sa Microsoft Foundry** — Bagong seksyon sa [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) at runnable sample [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) gamit ang `langchain-azure-ai[hosting]` at `ResponsesHostServer` (ang `/responses` protocol), batay sa [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Bagong seksyong "Real-World Example: Microsoft Project Opal" sa [15-browser-use/README.md](./15-browser-use/README.md) na inilalarawan si Opal bilang isang enterprise computer-use agent at inilalapat ito sa mga konsepto ng kurso (human-in-the-loop, trust/security, planning, Skills).
- **Ikalawang Lesson 02 Python sample** — Idinagdag ang [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (tingnan ang "Changed" — inilipat mula sa dating Semantic Kernel notebook) at naka-link ito sa lesson README.
- **Mga Seksyon para sa Models at Providers** na idinagdag sa [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Binago

- **Chat Completions → Responses API (Python).** Ang mga sample na tumawag sa modelo ng direkta ay inilipat mula sa Chat Completions sa Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), gamit ang `OpenAI` client laban sa matatag na Azure OpenAI `/openai/v1/` endpoint (walang `api_version`). Kasama sa mga naapektuhang sample ang:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — ang buong walkthrough ng function-calling (tool schema na inayos sa Responses format, ang mga resulta ng tool ay ibinalik bilang `function_call_output`, `max_output_tokens`, atbp.).

- **GitHub Models → Azure OpenAI.** Ang GitHub Models ay hindi na gagamitin (magtatapos sa **Hulyo 2026**) at hindi sumusuporta sa Responses API. Lahat ng mga code path ng GitHub Models ay na-convert sa Azure OpenAI / Microsoft Foundry sa mga halimbawa ng Python at .NET:
  - Python: Lesson 08 workflow notebooks (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + kasamang `.md` na mga dokumento, at ang Lesson 08 dotNET workflow notebooks/`.md` (`01`–`03`) ay gumagamit na ngayon ng `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` gamit ang `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Ang dating `02-semantic-kernel.ipynb` ay muling isinulat upang gamitin ang Microsoft Agent Framework kasama ang Azure OpenAI (Responses API) at pinalitan ang pangalan sa `02-python-agent-framework-azure-openai.ipynb`.
- **Standardized on `FoundryChatClient` + `as_agent`.** Ang README at mga code ng notebook na tumutukoy sa `AzureAIProjectAgentProvider` ay na-standardize sa canonical na pattern na ginamit sa Lesson 01 at sa sariling mga halimbawa ng framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` gamit ang `provider.as_agent(...)`. Na-update ito sa buong Lesson 02–14 READMEs at mga notebook (hal., Lesson 13 memory, lahat ng Lesson 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Product naming.** Pinangalanan muli sa buong nilalamang Ingles:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Hindi nabago: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", at mga pangalan ng environment variable.)
- **Dependencies** ([requirements.txt](../../requirements.txt)):
  - Nakapirming `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Nakapirming `openai>=1.108.1` (minimum para sa Responses API).
  - Tinanggal ang `azure-ai-inference` (ginamit lang sa mga na-migrate na halimbawa ng GitHub Models).
- **Environment configuration** ([.env.example](../../.env.example)): tinanggal ang mga variable ng GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); idinagdag ang `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, at opsyonal na `AZURE_OPENAI_API_KEY`; in-update ang pangalan sa Microsoft Foundry.
- **Docs** — Na-update ang [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), at [STUDY_GUIDE.md](./STUDY_GUIDE.md) para sa mga nabanggit (pagsasaayos ng env vars, snippet para sa beripikasyon, gabay sa provider, pangalan).

### Tinanggal

- Mga hakbang sa onboarding ng GitHub Models at mga environment variable mula sa setup na dokumento (pinalitan na ng Azure OpenAI / Microsoft Foundry).

### Seguridad / Privacy (paglilinis para sa pampublikong pagbabahagi)

- Nilinis ang mga output ng Jupyter notebook execution na naglalabas ng totoong **Azure subscription ID**, mga pangalan ng resource-group / resource, at Bing connection ID, pati na rin ang mga developer **local file paths at mga username**, sa:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Nasiguro na walang mga API key, token, subscription ID, o mga personal na path na natitira sa nasubaybayang nilalamang Ingles (ang mga natitirang reference sa `GITHUB_TOKEN` ay para sa GitHub Actions token sa mga workflow at ang GitHub MCP server PAT sa Lesson 11 setup — kapwa lehitimo at hindi konektado sa GitHub Models).

### Mga Tala at kilalang limitasyon

- **Hindi naipatupad/nakompayl.** Ito ay mga sample para sa edukasyon na na-update para sa tamang API/pangalan; hindi ito pinatakbo laban sa mga live na Azure resources, at ang mga .NET sample ay hindi na-kompayl sa kapaligirang ito. Suriin sa iyong sariling Microsoft Foundry / Azure OpenAI deployment.
- **Ang deployment ng modelo ay dapat sumuporta sa Responses API.** Gumamit ng deployment tulad ng `gpt-4.1-mini`, `gpt-4.1`, o isang `gpt-5.x` na modelo. Suportado ng mga lumang modelo ang pangunahing functionality ng Responses pero hindi lahat ng feature.
- **Bersyon ng agent-framework.** Nilalayon ng mga sample ang pinakabagong MAF (`>=1.10.0`). Ang canonical na tawag sa paglikha ng ahente ay `client.as_agent(...)`; na-validate ang mga API laban sa mga publikadong dokumento ng framework at isang naka-install na build. Kung gagamit ng ibang bersyon, tiyakin ang availability ng metodo (`as_agent` kumpara sa `create_agent`).
- **Lesson 08 workflow notebook 04** ay sinasadya pa ring gumagamit ng `AzureAIAgentClient` (mula sa `agent-framework-azure-ai`) dahil gumagamit ito ng mga tool na naka-host sa Microsoft Foundry Agent Service (Bing grounding, code interpreter); ito ay batay na sa Responses.
- **.NET default na deployment.** Dalawang halimbawa ng Lesson 08 dotNET workflow ay dati hard-coded sa isang espesipikong modelo; ngayon ay default nang `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Kung ang sample ay umaasa sa multimodal/vision input, itakda ang `AZURE_OPENAI_DEPLOYMENT` sa angkop na modelo.
- **Foundry Local** ay nagpapakita ng OpenAI-compatible na endpoint ng **Chat Completions** at nilalayon para sa lokal na pag-develop; gamitin ang Azure OpenAI / Microsoft Foundry para sa buong set ng feature ng Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->