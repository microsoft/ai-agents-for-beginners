# Popis promjena

Sve značajne promjene u tečaju **AI agenti za početnike** dokumentirane su u ovoj datoteci.

## [Objavljeno] — 2026-07-13

Ovo izdanje dodaje dvije nove lekcije koje dovršavaju luk implementacije — skaliranje agenata do Microsoft Foundry i spuštanje do jedne radne stanice — plus pipeline za brzi test, osvježenu navigaciju tečajem, nove vještine za učenike i ažurirani brending.

### Dodano

- **Lekcija 16 — Implementacija skalabilnih agenata s Microsoft Foundry.** Nova lekcija [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) i izvršni notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) koji gradi produkcijskog agenta za korisničku podršku (alata, RAG, memorija, usmjeravanje modela, keširanje odgovora, odobrenje čovjeka, vrata za evaluaciju i OpenTelemetry praćenje), s dijagramima za razvoj/implementaciju/izvršavanje u Mermaidu, provjerom znanja, zadatkom i izazovom.
- **Lekcija 17 — Kreiranje lokalnih AI agenata s Foundry Local i Qwen.** Nova lekcija [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) i notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) koji gradi potpuno uređajnog inženjerskog asistenta (pozivanje Qwen funkcija preko Foundry Local, alatne datoteke u sandboxu, lokalni RAG s Chromom, opcionalni lokalni MCP), s dijagramima samo lokalno / lokalni RAG / pozivanje alata, provjerom znanja, zadatkom i izazovom.
- **Pipeline za brzi test.** Novi workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus katalog po lekcijama pod [tests/](./tests/README.md) za implementirane agente u Lekcijama 01, 04, 05 i 16, s README indeksom koji mapira svaki katalog na njegovu lekciju i ime hostiranog agenta. Lekcija 16 dobiva sekciju "Validacija raspoređenog agenta s brzim testovima"; lekcije 01/04/05 dobivaju opcionalnu oznaku za brzi test.
- **Vještine učenika.** Nove vještine agenata pod `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (paket lekcija 16 i 17), i [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kako validirati uzorke notebooka protiv aktivnog Microsoft Foundry / Azure OpenAI postava).
- **Pokretač validacije notebooka.** Novi [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) koji izvršava svaki Python notebook bez glave koristeći `nbconvert` i ispisuje matricu PROŠAO/NIJE PROŠAO (plus `results.json`). Automatski pronalazi root repozitorija i Python, isključuje notebokove koji nisu iz tečaja (`.venv`, `site-packages`, `translations`, resurse predložaka vještina) i `.NET` notebookove prema zadanim postavkama, podržava `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` i `-Python`.
- **Navigacija tečajem.** Dodane poveznice Prethodna/Sljedeća lekcija za lekcije 11–15 (prije su nedostajale) tako da cijeli tečaj sada povezuje 00 → 18 u oba smjera.
- **Nove sličice.** Miniature lekcija za lekcije 16 i 17, plus osvježena društvena slika repozitorija [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (sad promovira dvije nove lekcije i URL `aka.ms/ai-agents-beginners`).
- **Ovisnosti** ([requirements.txt](../../requirements.txt)): dodani `foundry-local-sdk` i `chromadb` za Lekciju 17.

### Promijenjeno

- **Glavna tablica lekcija u [README.md](./README.md)**: Lekcije 16 i 17 sada vode do svog sadržaja (prije "Uskoro"); slika repozitorija je ažurirana na `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: dodane lekcije 16 i 17 u vodič po lekcijama i putovima učenja, te sekcija "Validacija raspoređenih agenata s brzim testovima".
- **[AGENTS.md](./AGENTS.md)**: ažuriran broj/opis lekcija (00–18), dodana sekcija za validaciju brzim testiranjem te primjeri imenovanja uzoraka za lekcije 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Prethodna lekcija" sada pokazuje na lekciju 17 (prije lekcija 15), zatvarajući lanac.
- **Standardizirani referenzi modela na modelima koji nisu zastarjeli.** Zamijenjene su sve reference `gpt-4o` / `gpt-4o-mini` kroz cijeli tečaj (dokumentacija, `.env.example`, Python/.NET notebookovi i primjeri) sa `gpt-4.1-mini` — `gpt-4o` (sve verzije) se povlači 2026. Lekcija 16 primjer usmjeravanja modela koristi kontrast malo/veliko koristeći `gpt-4.1-mini` (malo) i `gpt-4.1` (veliko). Python notebookovi sada biraju model iz varijabli okoline (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`), umjesto tvrdog koda imena modela.

### Napomene i poznata ograničenja

- **Nisu izvršeni protiv aktivnog Azurea.** Novi notebookovi lekcija su edukativni primjeri; pokrenite i validirajte ih u svojoj Microsoft Foundry / Foundry Local postavci. Workflow za brzi test zahtijeva da implementirate agenta iz lekcije i konfigurirate Azure OIDC tajne (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) s ulogom **Azure AI User** na opsegu Foundry projekta.
- **Lekcija 17 je samo lokalna.** Nema Foundry Responses endpoint, stoga akcija za brzi test nije primjenjiva; validirajte ju pokretanjem notebooka na svojoj radnoj stanici.

## [Objavljeno] — 2026-07-06

Ovo izdanje migrira tečaj na **Azure OpenAI Responses API**, standardizira nazive proizvoda na **Microsoft Foundry** i **Microsoft Agent Framework (MAF)**, ukida GitHub modele, ažurira verzije SDK-a i dodaje novi sadržaj o lokalnim modelima i hostanju drugih frameworka na Foundryu.

### Dodano

- **Vještina migracije** — Instalirana Agent vještina [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (iz [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) pod `.agents/skills/`, uključujući reference i skriptu za skeniranje.
- **Foundry Local (pokretanje modela na uređaju)** — Nova sekcija "Alternativni pružatelj: Foundry Local" u [00-course-setup/README.md](./00-course-setup/README.md) koja pokriva instalaciju (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` i povezivanje `FoundryLocalManager` s Microsoft Agent Frameworkom preko `OpenAIChatClient`.
- **Hostanje LangChain / LangGraph agenata na Microsoft Foundry** — Nova sekcija u [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus izvršni primjer [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) koristeći `langchain-azure-ai[hosting]` i `ResponsesHostServer` (protokol `/responses`), temeljeno na [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nova sekcija "Primjer iz stvarnog svijeta: Microsoft Project Opal" u [15-browser-use/README.md](./15-browser-use/README.md) koji postavlja Opal kao enterprise agenta za korištenje računala i povezuje ga s konceptima tečaja (čovjek-u-cjeloj, povjerenje/sigurnost, planiranje, vještine).
- **Drugi Python primjer iz Lekcije 02** — Dodano [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (vidi "Promijenjeno" — migrirano iz starog Semantic Kernel notebooka) i povezano u README lekcije.
- Dodana sekcija Modeli i pružatelji u [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Promijenjeno

- **Chat Completions → Responses API (Python).** Primjeri koji su pozivali model direktno migrirani su s Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), koristeći `OpenAI` klijenta prema stabilnom Azure OpenAI `/openai/v1/` endpointu (bez `api_version`). Uključeni primjeri:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — kompletan walkthrough funkcije pozivanja (shema alata izravnana u Responses format, rezultati alata vraćeni kao `function_call_output`, `max_output_tokens` itd.).
- **GitHub modeli → Azure OpenAI.** GitHub modeli su zastarjeli (ukidaju se **srpanj 2026**) i ne podržavaju Responses API. Svi kodni putevi GitHub modela su konvertirani u Azure OpenAI / Microsoft Foundry za Python i .NET primjere:
  - Python: workflow notebookovi Lekcije 08 (`01`–`03`), Lekcija 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + prateća `.md` dokumentacija, te workflow notebookovi i `.md` Lekcije 08 (`01`–`03`) sada koriste `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` s `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Stari notebook `02-semantic-kernel.ipynb` prepravljan je da koristi Microsoft Agent Framework s Azure OpenAI (Responses API) i preimenovan u `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizacija na `FoundryChatClient` + `as_agent`.** README i kod notebooka koji su referencirali `AzureAIProjectAgentProvider` standardizirani su na kanonski uzorak korišten Lekcijom 01 i vlastitim primjerima frameworka: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` s `provider.as_agent(...)`. Ažurirano kroz README-e i notebooke Lekcija 02–14 (npr., memorija Lekcije 13, svi notebookovi Lekcije 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Nazivi proizvoda.** Preimenovano kroz cijeli engleski sadržaj:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Neizmijenjeno: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" i nazivi varijabli okoline.)
- **Ovisnosti** ([requirements.txt](../../requirements.txt)):
  - Fiksirani `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fiksirani `openai>=1.108.1` (minimalno za Responses API).
  - Uklonjen `azure-ai-inference` (koristio se samo u migriranim GitHub Models primjerima).
- **Konfiguracija okoline** ([.env.example](../../.env.example)): uklonjene varijable za GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); dodani `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` i opcionalni `AZURE_OPENAI_API_KEY`; ažurirani nazivi na Microsoft Foundry.
- **Dokumentacija** — Ažurirani [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) i [STUDY_GUIDE.md](./STUDY_GUIDE.md) za gore navedeno (postavke varijabli okoline, provjerne skripte, upute za pružatelje, nazivi).

### Uklonjeno

- Koraci uvođenja GitHub modela i varijable okoline iz dokumentacije postavljanja (zastarjeli u korist Azure OpenAI / Microsoft Foundry).

### Sigurnost / Privatnost (čišćenje javnog dijeljenja)

- Očišćeni izlazi izvršavanja Jupyter notebookova koji su otkrivali stvarni **ID pretplate na Azure**, nazive grupa resursa / resursa, i ID veze za Bing, plus lokalne putove datoteka i korisnička imena razvojnog programera, u:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Provjereno da nema preostalih API ključeva, tokena, ID-eva pretplate ili osobnih putanja u praćenom engleskom sadržaju (preostale reference na `GITHUB_TOKEN` su GitHub Actions tokeni u workflow-ima i GitHub MCP server PAT u postavkama lekcije 11 — oba legitimna i nevezana za GitHub modele).

### Napomene i poznata ograničenja

- **Nije izvršeno/kompilirano.** Ovo su edukativni primjeri ažurirani za ispravnost API-ja/imenovanja; nisu pokretani nad stvarnim Azure resursima, a .NET primjeri nisu kompilirani u ovom okruženju. Provjerite na vlastitoj implementaciji Microsoft Foundry / Azure OpenAI.
- **Implementacija modela mora podržavati Responses API.** Koristite implementaciju poput `gpt-4.1-mini`, `gpt-4.1` ili `gpt-5.x` modela. Stariji modeli podržavaju osnovne funkcije Responses, ali ne i sve značajke.
- **Verzija agent-frameworka.** Primjeri ciljaju najnoviji MAF (`>=1.10.0`). Kanonski poziv za stvaranje agenata je `client.as_agent(...)`; API-jevi su provjereni prema objavljenoj dokumentaciji frameworka i instaliranoj verziji. Ako koristite drugu verziju, provjerite dostupnost metode (`as_agent` vs `create_agent`).
- **Radni bilježnik radnog toka lekcije 08, datoteka 04** namjerno zadržava `AzureAIAgentClient` (iz `agent-framework-azure-ai`) jer koristi Microsoft Foundry Agent Service alate (Bing pouzdanje, interpretator koda); već je baziran na Responses.
- **.NET zadana implementacija.** Dva .NET primjera iz lekcije 08 su ranije imali hard-coded određeni model; sada su po defaultu `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ako primjer koristi multimodalni/vidni input, postavite `AZURE_OPENAI_DEPLOYMENT` na odgovarajući model.
- **Foundry Local** izlaže OpenAI-kompatibilni endpoint za **Chat Completions** i namijenjen je lokalnom razvoju; za potpune mogućnosti Responses API-ja koristite Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->