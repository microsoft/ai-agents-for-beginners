# Változási napló

Az **AI Agents for Beginners** tanfolyam minden jelentős változása ebben a fájlban dokumentált.

## [Kiadva] — 2026-07-14

Ez a kiadás eltávolítja a tanfolyamot két nemrégiben elavult modellel, áthelyezi a maradék Lecke jegyzetfüzeteket a stabil Microsoft Agent Framework API-ra, és éles Microsoft Foundry telepítés ellen validálja a Python jegyzetfüzeteket.

### Megváltozott

- **Átállás elavult modellekről (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Mindkét `gpt-4.1` és `gpt-4.1-mini` mostantól elavult (megjelent visszavonási dátum **2026. október 14.**). A tanfolyamban minden hivatkozás (dokumentumok, `.env.example`, Python/.NET jegyzetfüzetek és példák) lecserélve nem elavult `gpt-5-mini` modellre. A Lecke 16 modell-irányítási példája megtartja a kis/nagy kontrasztot a `gpt-5-nano` (kis) és `gpt-5-mini` (nagy) modellekkel. A harmadik féltől származó fájlok ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), a GitHub Models történeti szöveg és az `azure-openai-to-responses` képességjegyzetek szándékosan változatlanok maradtak.
- **A Lecke 14 átadás jegyzetfüzet migrálva a stabil API-ra.** A [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) most a `agent_framework.orchestrations.HandoffBuilder`-t használja `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` alapú streamelést, és `FoundryChatClient`-et (helyettesítve a megszüntetett pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` jeleket).
- **Lecke 14 emberi közreműködéses jegyzetfüzet migrálva a stabil API-ra.** A [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) most szüneteltet a `ctx.request_info(...)` + `@response_handler` használatával (helyettesítve a megszüntetett `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), épít `WorkflowBuilder(start_executor=..., output_executors=[...])` segítségével, strukturált kimenetet terel a `default_options={"response_format": ...}`-en keresztül, és szkriptelt választ használ, így a jegyzetfüzet felügyelet nélkül fut (nincs blokkoló `input()`).
- **Környezeti konfiguráció** ([.env.example](../../.env.example)): átállt a modell telepítési nevekre `gpt-5-mini`-re; hozzáadva `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Lecke 16 irányítás) és a korábban hiányzó `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Lecke 15 böngésző használat).
- **Függőségek** ([requirements.txt](../../requirements.txt)): az `agent-framework`, `agent-framework-foundry` és `agent-framework-openai` rögzítve lett `~=1.10.0` verzióra egy önkonzisztens, validált készlethez (az 1.11.0 kísérleti törő változtatásokat hoz azon felületeken, amiket ezek a leckék használnak).

### Megjegyzések és ismert korlátozások

- **Éles Microsoft Foundry ellen validálva.** A Python jegyzetfüzetek fej nélküli futtatásra kerültek `nbconvert` segítségével egy Microsoft Foundry projekten `gpt-5-mini` (és Lecke 16 irányításhoz `gpt-5-nano`) modellel. Telepítsen ekvivalens nem elavult modelleket a saját projektjébe; a jegyzetfüzetek a telepítés nevét az `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` változókból olvassák.
- **Néhány leckéhez továbbra is extra erőforrások szükségesek.** A Lecke 05 Azure AI Search-t igényel; a Lecke 08 Bing-alapú munkafolyamat (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) Bing kapcsolatot és a Microsoft Foundry Agent Service által hosztolt eszközöket igényel; a Lecke 13 (Cognee) és Lecke 17 (Foundry Local) saját futtató környezetet igényel.

## [Kiadva] — 2026-07-13

Ez a kiadás két új leckét ad hozzá, amik befejezik a telepítési ívet — az ágensek skálázását Microsoft Foundry-ra és egyetlen munkaállomásra, továbbá egy gyors-teszt futtató pipeline-t, frissített tanfolyam navigációt, új tanulói készségeket és megújult arculatot.

### Hozzáadva

- **Lecke 16 — Skálázható ágensek telepítése Microsoft Foundry-val.** Új lecke [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) és futtatható jegyzetfüzet [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) egy éles ügyféltámogató ügynök építésére (eszközök, RAG, memória, modell-irányítás, válasz gyorsítótárazás, emberi jóváhagyás, értékelési kapu, és OpenTelemetry követés), fejlesztési/telepítési/futtatási Mermaid diagramokkal, tudásellenőrzéssel, feladattal és kihívással.
- **Lecke 17 — Helyi AI ágensek létrehozása Foundry Local és Qwen segítségével.** Új lecke [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) és jegyzetfüzet [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) teljesen eszközön futó mérnöki asszisztens építésére (Qwen funkcióhívás Foundry Local-on keresztül, homokozós fájl eszközök, helyi RAG Chromával, opcionális helyi MCP), helyi-only / helyi-RAG / eszközhívó diagramokkal, tudásellenőrzéssel, feladattal és kihívással.
- **Gyors-teszt pipeline.** Új [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) és leckénkénti katalógusok a [tests/](./tests/README.md) mappában a telepíthető ágensekhez a Leckék 01, 04, 05 és 16 alatt, egy index README-vel, amely a katalógusokat leképezi a leckére és a hosztolt ügynök nevére. A Lecke 16 kap egy "Telepített Ügynök Érvényesítése Gyors-Tesztekkel" részt; a Leckék 01/04/05 opcionális gyors-teszt mutatót kapnak.
- **Tanulói készségek.** Új Ágensek Készségek a `.agents/skills/` alatt: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (a Lecke 16 és 17 útmutató csomagolásával), és [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (hogyan validáljuk a jegyzetfüzet példákat éles Microsoft Foundry / Azure OpenAI környezettel).
- **Jegyzetfüzet validáció futtató.** Új [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), amely minden Python jegyzetfüzetet fej nélküli módban futtat `nbconvert`-tel és PASS/FAIL mátrixot nyomtat (plusz `results.json`). Automatikusan érzékeli a repo gyökerét és a Pythont, alapból kizárja a nem tanfolyami jegyzetfüzeteket (`.venv`, `site-packages`, `translations`, képesség sablon assetek) és a `.NET` jegyzetfüzeteket, támogatja a `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` és `-Python` argumentumokat.
- **Tanfolyam navigáció.** Hozzáadott Előző/Következő lecke hivatkozásokat a Leckék 11–15-hoz (korábban hiányoztak), így a teljes tanfolyam láncolva van 00 → 18 irányban mindkét irányban.
- **Új bélyegképek.** Lecke képek a Leckék 16 és 17-hez, plusz megújult repo közösségi kép [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (most már hirdeti a két új leckét és az `aka.ms/ai-agents-beginners` URL-t).
- **Függőségek** ([requirements.txt](../../requirements.txt)): hozzáadva `foundry-local-sdk` és `chromadb` a Lecke 17-hez.

### Megváltozott

- **Fő [README.md](./README.md)** lecke táblázat: a Leckék 16 és 17 most már hivatkoznak a tartalmukra (korábban "Hamarosan"); a repo kép frissítve `repo-thumbnailv3.png`-re.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: hozzáadva a Leckék 16 és 17 a lecke szerinti útmutatóhoz és tanulási utakhoz, valamint egy "Telepített Ágensek Érvényesítése Gyors-Teszttel" szakasz.
- **[AGENTS.md](./AGENTS.md)**: frissítve a lecke szám/leírás (00–18), hozzáadva gyors-teszt validációs rész, hozzáadva Lecke 16/17 példa névadási példák.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Előző Lecke" most a Lecke 17-re mutat (korábban Lecke 15), ezzel lezárva a láncot.
- **Egységesített modell hivatkozások nem elavult modelleken.** Lecserélve minden `gpt-4o` / `gpt-4o-mini` hivatkozást a tanfolyamban (dokumentációk, `.env.example`, Python/.NET jegyzetfüzetek és minták) `gpt-4.1-mini`-re — a `gpt-4o` (minden verzió) 2026-ban megszűnik. A Lecke 16 modell-irányítási példája megtartja a kis/nagy kontrasztot `gpt-4.1-mini` (kis) és `gpt-4.1` (nagy) modellekkel. A Python jegyzetfüzetek mostantól a modellt környezeti változókból (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) választják ki a fix modellnév helyett.

### Megjegyzések és ismert korlátozások

- **Nem futtatva éles Azure ellen.** Az új leckék jegyzetfüzetei oktatási példák; futtassa és validálja őket saját Microsoft Foundry / Foundry Local környezetében. A gyors-teszt workflow megköveteli, hogy telepítse a lecke ügynökét és konfigurálja az Azure OIDC titkokat (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) **Azure AI User** szerepkörrel a Foundry projekt hatókörében.
- **Lecke 17 csak helyi használatú.** Nincs Foundry Válasz végpontja, ezért a gyors-teszt akció nem alkalmazható; validálja a jegyzetfüzet futtatásával a munkaállomásán.

## [Kiadva] — 2026-07-06

Ez a kiadás átállítja a tanfolyamot az **Azure OpenAI Responses API**-ra, egységesíti a terméknévhasználatot a **Microsoft Foundry** és a **Microsoft Agent Framework (MAF)** között, megszünteti a GitHub Modelleket, frissíti az SDK verziókat, és új tartalmat ad hozzá helyi modellekről és más keretrendszerek Foundry-n történő hosztolásáról.

### Hozzáadva

- **Migrációs képesség** — Telepítve az [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Ágensek Képesség (az [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) projektből) a `.agents/skills/` mappába, beleértve a hivatkozásait és pásztázó szkriptet.
- **Foundry Local (modellek futtatása eszközön)** — Új "Alternatív Szolgáltató: Foundry Local" szakasz a [00-course-setup/README.md](./00-course-setup/README.md) fájlban, lefedve a telepítést (`winget` / `brew`), `foundry model run`, a `foundry-local-sdk`-t, és a `FoundryLocalManager` bekötését a Microsoft Agent Framework-be az `OpenAIChatClient`-on keresztül.
- **LangChain / LangGraph ágensek hosztolása Microsoft Foundry-n** — Új szakasz a [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md)-ben plusz futtatható példa [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) a `langchain-azure-ai[hosting]` és a `ResponsesHostServer` (a `/responses` protokoll) használatával, a [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) alapján.
- **Microsoft Project Opal** — Új "Való Világi Példa: Microsoft Project Opal" szakasz a [15-browser-use/README.md](./15-browser-use/README.md) fájlban, amely Opalt vállalati számítógép-használati ügynökként mutatja be és leképezi a tanfolyam koncepciókra (emberi közreműködés, bizalom/biztonság, tervezés, Képességek).
- **Második Lecke 02 Python példa** — Hozzáadva a [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (lásd a "Megváltozott" részt — migrálva a korábbi Semantic Kernel jegyzetfüzetből), és linkelve a lecke README-ben.
- **Modellek és Szolgáltatók** szakasz hozzáadva a [STUDY_GUIDE.md](./STUDY_GUIDE.md) fájlhoz.

### Megváltozott

- **Chat Befejezések → Responses API (Python).** Azok a példák, amelyek közvetlenül hívták a modellt, migrálva lettek a Chat Befejezésekről a Responses API-ra (`client.responses.create(input=..., store=False)`, `resp.output_text`), az `OpenAI` kliens használatával a stabil Azure OpenAI `/openai/v1/` végponton (nincs `api_version`). Érintett példák közé tartoznak:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — a teljes funkcióhívás bemutató (az eszköz séma átalakítva Responses formátumba, eszköz eredmények visszaadva `function_call_output`, `max_output_tokens`, stb.).

- **GitHub Models → Azure OpenAI.** A GitHub Models elavult (2026 júliusában megszűnik) és nem támogatja a Responses API-t. Minden GitHub Models kódvonal át lett alakítva Azure OpenAI / Microsoft Foundry használatára Python és .NET mintákban:
  - Python: 08-as lecke workflow jegyzetfüzetek (`01`–`03`), 14-es lecke (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + mellékelt `.md` dokumentációk, valamint a 08-as lecke dotNET workflow jegyzetfüzetei/`.md` fájljai (`01`–`03`) most `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)`-ot használnak `AzureCliCredential`-lel.
- **Semantic Kernel → Microsoft Agent Framework.** A korábbi `02-semantic-kernel.ipynb` újraírásra került a Microsoft Agent Framework használatához Azure OpenAI-val (Responses API), és át lett nevezve `02-python-agent-framework-azure-openai.ipynb`-re.
- **Standardizálás `FoundryChatClient` + `as_agent` használatára.** A README és jegyzetfüzet kód, amely korábban `AzureAIProjectAgentProvider`-t hivatkozott, egységesen a 01-es lecke és a keretrendszer saját mintái szerint használja a kanonikus mintát: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` az `provider.as_agent(...)`-tal. Frissítve a 02–14-es leckék README-jében és jegyzetfüzeteiben (pl. 13-as lecke memória, minden 14-es lecke jegyzetfüzete, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Termék elnevezések.** Átnevezve az angol tartalomban:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Változatlan: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" és környezeti változó nevek.)
- **Függőségek** ([requirements.txt](../../requirements.txt)):
  - Lekötött `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Lekötött `openai>=1.108.1` (minimum a Responses API-hoz).
  - Eltávolítva `azure-ai-inference` (csak a migrált GitHub Models mintákban használták).
- **Környezeti konfiguráció** ([.env.example](../../.env.example)): eltávolítva GitHub Models változók (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); hozzáadva `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` és opcionális `AZURE_OPENAI_API_KEY`; Microsoft Foundry névhasználatra frissítve.
- **Dokumentációk** — Frissítve a [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) és [STUDY_GUIDE.md](./STUDY_GUIDE.md) a fentiek szerint (környezeti változók beállítása, ellenőrző kód, szolgáltató iránymutatás, névhasználat).

### Eltávolítva

- GitHub Models bevezető lépések és környezeti változók a beállítási dokumentációkból (felváltva Azure OpenAI / Microsoft Foundry által).

### Biztonság / Adatvédelem (nyilvános megosztás takarítás)

- Kitörölve Jupyter jegyzetfüzet futtatási kimenetek, amelyek valódi **Azure előfizetés azonosítót**, erőforrás-csoport / erőforrás neveket és Bing kapcsolat azonosítót, valamint fejlesztői **helyi fájlútvonalakat és felhasználóneveket** szivárogtattak, az alábbiakban:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Ellenőrizve, hogy nem maradtak API kulcsok, tokenek, előfizetés azonosítók vagy személyes útvonalak a nyilvántartott angol tartalomban (a megmaradt `GITHUB_TOKEN` hivatkozások a GitHub Actions tokenjei munkafolyamatokban és a GitHub MCP szerver PAT-je a 11-es lecke beállításában – mind legálisak és nem kapcsolódnak a GitHub Modelsekhez).

### Megjegyzések és ismert korlátozások

- **Nem futtatott/fordított.** Ezek oktatási minták, melyek frissítve lettek az API/névhelyesség érdekében; nem futottak élő Azure erőforrásokon, és a .NET minták sem kerültek fordításra ebben a környezetben. Érvényesítsd saját Microsoft Foundry / Azure OpenAI telepítésedben.
- **A modell telepítésnek támogatnia kell a Responses API-t.** Használj olyan telepítést, mint `gpt-4.1-mini`, `gpt-4.1` vagy egy `gpt-5.x` modell. Régebbi modellek a core Responses funkciókat támogatják, de nem minden szolgáltatást.
- **Agent-framework verzió.** A minták a legújabb MAF-ot célozzák (`>=1.10.0`). A kanonikus ügynök létrehozó hívás a `client.as_agent(...)`; az API-kat ellenőriztük a keretrendszer dokumentációban és egy telepített buildben. Ha más verziót használsz, ellenőrizd a metódusok elérhetőségét (`as_agent` vs `create_agent`).
- **08-as lecke workflow jegyzetfüzet 04** szándékosan megtartja az `AzureAIAgentClient`-et (az `agent-framework-azure-ai`-ból), mert Microsoft Foundry Agent Service által hosztolt eszközöket használ (Bing grounding, kódértelmező); már Responses alapú.
- **.NET alapértelmezett telepítés.** Két 08-as lecke dotNET workflow minta korábban keménykódolt egy meghatározott modellt; most alapértelmezett a `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ha egy minta multimodális / vizuális bemenetet igényel, állítsd be az `AZURE_OPENAI_DEPLOYMENT`-et megfelelő modellre.
- **Foundry Local** nyit egy OpenAI-kompatibilis **Chat Completions** végpontot és helyi fejlesztésre szánt; a teljes Responses API szolgáltatáscsomaghoz használd az Azure OpenAI / Microsoft Foundry-t.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->