---
name: testing-course-samples
description: Gamitin kapag hiniling na i-validate, subukan, smoke-test, o patakbuhin
  ang notebook ng kurso at mga halimbawa ng code laban sa isang live na Microsoft
  Foundry / Azure OpenAI na configuration. Saklaw nito ang pag-setup ng kapaligiran
  (.env, az login, mga package), ang scripts/validate-notebooks.ps1 runner, ang pagpapakahulugan
  ng mga resulta na PASS/FAIL, at kung aling mga aralin ang nangangailangan ng karagdagang
  mga mapagkukunan (Azure AI Search, GitHub MCP, Foundry Local, Playwright).
---
# Pagsusuri ng Mga Halimbawa ng Kurso

Tiyakin na ang mga lesson notebook at mga halimbawa ng code ay tumatakbo laban sa isang aktibong
Microsoft Foundry / Azure OpenAI na setup. Naglalaman ang repo ng isang runner sa
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) na
nagpapatakbo ng bawat Python notebook nang walang interface at nagpapakita ng PASS/FAIL matrix.

## Kailan Gagamitin
- "I-validate lahat ng mga notebook / mga sample laban sa aking Azure subscription."
- "Magsagawa ng smoke-test sa kurso pagkatapos mag-upgrade ng mga package o magpalit ng mga modelo."
- "Aling mga lesson ang pasado pa rin / bagsak nang live?"

Huwag gamitin ito para sa AI Smoke Test GitHub Action (na nagva-validate ng *deployed*
na mga hosted agent — tingnan ang [`tests/README.md`](../../../tests/README.md)). Ang kasanayang ito
ay nagpapatakbo ng mga notebook nang lokal.

## Mga Paunang Kinakailangan (suriin muna)
1. **Python 3.12+** kasama ang mga dependency ng kurso: `python -m pip install -r requirements.txt`
   pati na rin ang executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` sa root ng repo** (kopyahin mula sa [`.env.example`](../../../../../.env.example)) na may mga sumusunod:
   - `AZURE_AI_PROJECT_ENDPOINT` — endpoint ng proyekto sa Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — isang non-deprecated na deployment (hal. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) at `AZURE_OPENAI_DEPLOYMENT`
     para sa mga lesson na tumatawag nang direkta sa Azure OpenAI (Lesson 06, 02-azure-openai, 14 handoff/human-loop).
3. Kumpletuhin ang **`az login`** — ang mga halimbawa ay authenticates gamit ang `AzureCliCredential` (Entra ID, walang key).
4. Suriin kung umiiral ang model deployment:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Pagsasagawa ng Validation
```powershell
# Lahat ng Python notebook (hindi kasama ang .NET, .venv, site-packages, pagsasalin, mga asset ng kasanayan)
pwsh scripts/validate-notebooks.ps1

# Isang aralin, na may mas mahabang timeout bawat cell
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Isa lang ilista kung ano ang tatakbo (hindi mag-e-execute)
pwsh scripts/validate-notebooks.ps1 -List

# Tahasang interpreter (kung ang `python` ay wala sa PATH, halimbawa alias ng Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Ang script ay nagsusulat ng mga kopyang na-execute, mga log per-notebook, at `results.json` sa
`$env:TEMP\aiab-nbval` at lalabas na may bilang ng mga nabigong pagsubok.

Ang mga pansamantalang pagkabigo (limitasyon sa rate ng shared-subscription HTTP 429, isang paminsang
token hiccup ng `AzureCliCredential`, o timeout) ay awtomatikong nire-retry
(`-Retries`, default 2, na may `-RetryDelaySeconds` backoff, default 20). Kung ang
model deployment ay madalas na nagkakaroon ng 429, suriin ang GlobalStandard
TPM quota ng subscription (`az cognitiveservices usage list -l <region>`) — ang pagtaas ng kapasidad ng isang deployment lang ay hindi makakatulong kapag
naubos na ang quota ng *subscription*.

## Pagsasalin ng Mga Resulta
- `PASS` — matagumpay na tumakbo ang notebook mula simula hanggang dulo nang walang error sa cell.
- `FAIL` — ipinapakita ang unang linya ng `*Error` / `*Exception`; buksan ang tumutugmang
  `log_*.txt` sa output directory para sa buong traceback.
- Ang kabiguan ng isang notebook ay nililimitahan ng `-Timeout` (bawat cell), kaya ang isang natigil
  na human-in-the-loop cell ay lalabas bilang `StdinNotImplementedError` sa halip na makahinto.

## Mga Lesson na Nangangailangan ng Karagdagang Mga Kagamitan (inaasahang mabibigo kung wala ang mga ito)
| Lesson | Karagdagang pangangailangan |
|--------|------------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, susi) — may fallback na nasa memorya |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memory (cognee) | `cognee` na naka-configure sa isang model provider |
| 15 browser-use | Mga browser ng Playwright na naka-install (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + isang na-download na modelong Qwen (nasa device, walang cloud) |
| `*-dotnet-*` mga notebook | .NET Interactive kernel (hindi kasali bilang default; gamitin ang `-IncludeDotnet`) |

## Pag-uulat Pabalik
Ibuod bilang isang PASS/FAIL na talahanayan na pinangkat ayon sa lesson. Ihiwalay ang tunay na regression
(bug sa code/config na kailangang ayusin) mula sa mga kakulangan sa kapaligiran (kulang na Search/Foundry Local/PAT),
at ilahad ang mga nabigong `log_*.txt` para sa bawat totoong pagkabigo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->