# Zgodovina sprememb

Vse pomembne spremembe v tečaju **AI Agentov za začetnike** so dokumentirane v tej datoteki.

## [Nepublikirano] — 2026-07-06

Ta izdaja premakne tečaj na **Azure OpenAI Responses API**, standardizira poimenovanje izdelkov na **Microsoft Foundry** in **Microsoft Agent Framework (MAF)**, upokoji GitHub Models, posodobi različice SDK in doda novo vsebino o lokalnih modelih ter gostovanju drugih ogrodij na Foundry.

### Dodano

- **Sposobnost migracije** — Namestil [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (iz [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) pod `.agents/skills/`, vključno z njegovimi sklici in skripto za skeniranje.
- **Foundry Local (zagon modelov na napravi)** — Nova razdelek "Alternativni ponudnik: Foundry Local" v [00-course-setup/README.md](./00-course-setup/README.md) pokriva namestitev (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` in povezovanje `FoundryLocalManager` z Microsoft Agent Framework preko `OpenAIChatClient`.
- **Gostovanje agentov LangChain / LangGraph na Microsoft Foundry** — Nov razdelek v [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ter zažig vzorčni primer [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) z uporabo `langchain-azure-ai[hosting]` in `ResponsesHostServer` (protokol `/responses`), temelječ na [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nov razdelek "Primer iz resničnega sveta: Microsoft Project Opal" v [15-browser-use/README.md](./15-browser-use/README.md), ki Opal umešča kot agent za poslovno uporabo računalnika in ga povezuje s koncepti tečaja (človek v zanki, zaupanje/varnost, načrtovanje, veščine).
- **Druga vaja 02 Python vzorec** — Dodan [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (glej "Spremembe" — migriran iz nekdanjega Semantic Kernel zvezka) in vključen v README lekcije.
- Dodan razdelek **Modeli in ponudniki** v [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Spremenjeno

- **Chat Completions → Responses API (Python).** Vzorci, ki so klicali model neposredno, so bili migrirani s Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), z uporabo odjemalca `OpenAI` proti stabilnemu končnemu točki Azure OpenAI `/openai/v1/` (brez `api_version`). Vplivani vzorci vključujejo:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — celoten potek klica funkcije (orodna shema preoblikovana v Responses format, rezultati orodja vrnjeni kot `function_call_output`, `max_output_tokens` itd.).
- **GitHub Models → Azure OpenAI.** GitHub Models je opuščen (upokojitev **julij 2026**) in ne podpira Responses API. Vse poti kode GitHub Models so bile pretvorjene na Azure OpenAI / Microsoft Foundry prek Python in .NET vzorcev:
  - Python: zvezki delovnega toka Lekcije 08 (`01`–`03`), Lekcija 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + spremljajoča `.md` dokumentacija, in zvezki/`.md` Lekcije 08 za dotNET (`01`–`03`) zdaj uporabljajo `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` z `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Nekdanji `02-semantic-kernel.ipynb` je bil prepisan za uporabo Microsoft Agent Framework z Azure OpenAI (Responses API) in preimenovan v `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizacija na `FoundryChatClient` + `as_agent`.** README in koda zvezkov, ki je sklicevala `AzureAIProjectAgentProvider`, so bile standardizirane na kanonski vzorec, ki ga uporablja Lekcija 01 in lastni vzorci ogrodja: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` z `provider.as_agent(...)`. Posodobljeno v README-ih in zvezkih Lekcij 02–14 (npr. spomin Lekcije 13, vsi zvezki Lekcije 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Poimenovanje izdelkov.** Preimenovano v celotni angleški vsebini:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Nespremenjeno: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" in imena okolijskih spremenljivk.)
- **Odvisnosti** ([requirements.txt](../../requirements.txt)):
  - Zagozdil `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Zagozdil `openai>=1.108.1` (minimalno za Responses API).
  - Odstranil `azure-ai-inference` (je bil uporabljen samo v migriranih vzorcih GitHub Models).
- **Okoljska konfiguracija** ([.env.example](../../.env.example)): odstranjene spremenljivke GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); dodane `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` in izbirni `AZURE_OPENAI_API_KEY`; ime posodobljeno na Microsoft Foundry.
- **Dokumentacija** — Posodobljeno [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) in [STUDY_GUIDE.md](./STUDY_GUIDE.md) za zgoraj navedeno (nastavitev okoljskih spremenljivk, preveritveni delček, navodila za ponudnike, poimenovanje).

### Odstranjeno

- Koraki za uvajanje GitHub Models in okoljske spremenljivke iz nastavitev dokumentacije (nadomeščeno z Azure OpenAI / Microsoft Foundry).

### Varnost / zasebnost (čiščenje javnih delitev)

- Počistili izhode izvajanja Jupyter zvezkov, ki so razkrivali pravi **ID Azure naročnine**, imena skupin virov / virov in ID povezave Bing, poleg **lokalnih poti do datotek in uporabniških imen** razvijalcev, v:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Preverjeno, da v sledeni angleški vsebini ni ostalo nobenih ključev API, tokenov, ID-jev naročnin ali osebnih poti (sklici na `GITHUB_TOKEN`, ki ostajajo, so token GitHub Actions v potekih dela in GitHub MCP strežniški PAT v nastavitvi Lekcije 11 — oba zakonita in nista povezana z GitHub Models).

### Opombe in znane omejitve

- **Niso zagnani/prevajani.** To so izobraževalni vzorci, posodobljeni za pravilnost API-ja in poimenovanja; niso bili zagnani proti živim Azure virom, .NET vzorci pa niso bili prevedeni v tem okolju. Preverite nasprotno svoje lastno Microsoft Foundry / Azure OpenAI okolje.
- **Model za uvajanje mora podpirati Responses API.** Uporabite uvajanje, kot sta `gpt-4o-mini`, `gpt-4.1` ali model `gpt-5.x`. Starejši modeli podpirajo osnovno funkcionalnost Responses, a ne vseh funkcij.
- **Različica agent-framework.** Vzorci ciljajo na zadnjo različico MAF (`>=1.10.0`). Kanonski klic za ustvarjanje agenta je `client.as_agent(...)`; API-ji so bili preverjeni glede na uradne objavljene dokumentacije in nameščen prevod. Če zaklenete drugo različico, potrdite razpoložljivost metode (`as_agent` proti `create_agent`).
- **Zvezek delovnega toka Lekcije 08, 04** namerno ohranja `AzureAIAgentClient` (iz `agent-framework-azure-ai`), ker uporablja Microsoft Foundry Agent Service gostovana orodja (Bing iskanje, interpretator kode); je že na osnovi Responses.
- **Privzeto .NET uvajanje.** Dva dotNET vzorca delovnega toka Lekcije 08 sta prej trdo kodirala `gpt-4o`; zdaj privzeto uporabljata `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Če vzorec uporablja multimodalni/vidni vhod, nastavite `AZURE_OPENAI_DEPLOYMENT` na ustrezen model.
- **Foundry Local** izpostavlja OpenAI-kompatibilni konec za **Chat Completions** in je namenjen lokalnemu razvoju; za celoten nabor funkcij Responses API uporabite Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->