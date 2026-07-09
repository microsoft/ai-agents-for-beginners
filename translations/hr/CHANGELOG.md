# Dnevnici promjena

Sve značajne promjene za tečaj **AI agenti za početnike** dokumentirane su u ovoj datoteci.

## [Nije objavljeno] — 2026-07-06

Ovo izdanje migrira tečaj na **Azure OpenAI Responses API**, standardizira nazive proizvoda na **Microsoft Foundry** i **Microsoft Agent Framework (MAF)**, povlači GitHub modele, ažurira verzije SDK-a te dodaje novi sadržaj o lokalnim modelima i hostanju drugih okvira na Foundryju.

### Dodano

- **Vještina migracije** — Instalirana [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (iz [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) u `.agents/skills/`, uključujući njene reference i skriptu za skeniranje.
- **Foundry Local (pokretanje modela na uređaju)** — Nova sekcija "Alternative Provider: Foundry Local" u [00-course-setup/README.md](./00-course-setup/README.md) koja pokriva instalaciju (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` i povezivanje `FoundryLocalManager` s Microsoft Agent Frameworkom putem `OpenAIChatClient`.
- **Hostanje LangChain / LangGraph agenata na Microsoft Foundry** — Nova sekcija u [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus izvršni primjer [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) koristeći `langchain-azure-ai[hosting]` i `ResponsesHostServer` (protokol `/responses`), temeljeno na [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nova sekcija "Primjer iz stvarnog svijeta: Microsoft Project Opal" u [15-browser-use/README.md](./15-browser-use/README.md) koja okvirno prikazuje Opal kao enterprise agenta za korištenje računala i mapira ga na pojmove iz tečaja (čovjek u petlji, povjerenje/sigurnost, planiranje, Vještine).
- **Drugi Python primjer za lekciju 02** — Dodan [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (vidi "Izmijenjeno" — migriran iz bivše Semantic Kernel bilježnice) i povezan u README lekcije.
- Dodana sekcija **Modeli i davatelji** u [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Izmijenjeno

- **Chat Completions → Responses API (Python).** Primjeri koji su izravno pozivali model migrirani su s Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), koristeći `OpenAI` klijenta prema stabilnoj Azure OpenAI `/openai/v1/` krajnjoj točki (bez `api_version`). Obuhvaćeni primjeri uključuju:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — cjelokupna demonstracija poziva funkcije (šema alata spustila se na Responses format, rezultati alata vraćaju se kao `function_call_output`, `max_output_tokens`, i sl.).
- **GitHub modeli → Azure OpenAI.** GitHub modeli su zastarjeli (ukidaju se **srpanj 2026**) i ne podržavaju Responses API. Svi kodni putovi za GitHub modele konvertirani su na Azure OpenAI / Microsoft Foundry u Python i .NET primjerima:
  - Python: bilježnice tijeka rada lekcije 08 (`01`–`03`), lekcija 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + prateći `.md` dokumenti, i lekcija 08 dotNET bilježnice tijeka rada/`.md` (`01`–`03`) sada koriste `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` s `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Bivša bilježnica `02-semantic-kernel.ipynb` preuređena je za korištenje Microsoft Agent Frameworka s Azure OpenAI (Responses API) i preimenovana u `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizacija na `FoundryChatClient` + `as_agent`.** README i bilježnički kod koji je referencirao `AzureAIProjectAgentProvider` standardiziran je na kanonski obrazac korišten u lekciji 01 i vlastitim uzorcima okvira: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` s `provider.as_agent(...)`. Ažurirano u README-ima i bilježnicama lekcija 02–14 (npr. memorija lekcije 13, sve bilježnice lekcije 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Nazivi proizvoda.** Preimenovano kroz cijeli sadržaj na engleskom:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Neizmijenjeno: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", i nazivi varijabli okruženja.)
- **Ovisnosti** ([requirements.txt](../../requirements.txt)):
  - Zaključane verzije `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Zaključana verzija `openai>=1.108.1` (minimalno za Responses API).
  - Uklonjen `azure-ai-inference` (koristio se samo u migriranim GitHub Model primjerima).
- **Konfiguracija okruženja** ([.env.example](../../.env.example)): uklonjene varijable za GitHub modele (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); dodani `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` i opcionalni `AZURE_OPENAI_API_KEY`; ažurirani nazivi na Microsoft Foundry.
- **Dokumentacija** — ažurirani [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), i [STUDY_GUIDE.md](./STUDY_GUIDE.md) za gore navedeno (podešavanje varijabli okruženja, isječak za provjeru, upute za davatelja, nazivi).


### Uklonjeno

- Koraci uvođenja GitHub Modela i varijable okoline iz dokumenata za postavljanje (zamijenjeni Azure OpenAI / Microsoft Foundry).

### Sigurnost / Privatnost (čišćenje za javno dijeljenje)

- Očišćeni izlazi izvršavanja Jupyter bilježnica koji su curili stvarni **Azure pretplatnički ID**, imena grupi resursa / resursa i Bing ID veze, plus developerske **lokalne putanje datoteka i korisnička imena**, u:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Provjereno da nema preostalih API ključeva, tokena, ID pretplate ili osobnih putanja u praćenim sadržajima na engleskom jeziku (ostaci `GITHUB_TOKEN` koji ostaju su GitHub Actions token u workflowima i GitHub MCP server PAT u postavljanju Lekcije 11 — oba legitimni i nevezani za GitHub Models).

### Napomene i poznata ograničenja

- **Nije izvršeno/kompilirano.** Ovo su edukativni primjeri ažurirani za ispravnost API-ja/imenovanja; nisu pokretani prema živim Azure resursima, a .NET primjeri nisu kompilirani u ovom okruženju. Provjerite na vašoj vlastitoj Microsoft Foundry / Azure OpenAI implementaciji.
- **Implementacija modela mora podržavati Responses API.** Koristite implementaciju poput `gpt-4o-mini`, `gpt-4.1` ili model `gpt-5.x`. Stariji modeli podržavaju osnovnu funkcionalnost Responses, ali ne sve značajke.
- **Verzija agent-frameworka.** Primjeri se odnose na najnoviji MAF (`>=1.10.0`). Kanonski poziv za kreiranje agenta je `client.as_agent(...)`; API-jevi su provjereni prema objavljenoj dokumentaciji frameworka i instaliranoj verziji. Ako koristite drugu verziju, potvrdite dostupnost metoda (`as_agent` nasuprot `create_agent`).
- **Bilježnica tijeka rada Lekcija 08 broj 04** namjerno zadržava `AzureAIAgentClient` (iz `agent-framework-azure-ai`) jer koristi alate Microsoft Foundry Agent Service hostirane (Bing povezivanje, tumač koda); već se bazira na Responses.
- **.NET zadana implementacija.** Dva primjera tijeka rada Lesson 08 dotNET ranije su tvrdo kodirali `gpt-4o`; sada su zadani na `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Ako primjer zahtijeva multimodalni/vidni unos, postavite `AZURE_OPENAI_DEPLOYMENT` na odgovarajući model.
- **Foundry Local** izlaže OpenAI-kompatibilnu **Chat Completions** endpoint i namijenjen je za lokalni razvoj; za puni skup značajki Responses API, koristite Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->