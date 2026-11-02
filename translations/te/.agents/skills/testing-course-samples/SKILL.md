---
name: testing-course-samples
---
# కోర్సు నమూనాలను పరీక్షించడం  

పాఠం నోట్‌బుక్స్ మరియు కోడ్ నమూనాలు ఒక లైవ్  
Microsoft Foundry / Azure OpenAI సెటప్‌పై నడవడం సరిచూడండి. ఈ రిపోలో  
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) వద్ద ఒక రన్నర్ అందించేందున  
అది ప్రతి Python నోట్‌బుక్‌ను హెడ్లెస్‌ గా అమలు చేసి PASS/FAIL మ్యాట్రిక్స్‌ను ప్రింట్ చేస్తుంది.  

## ఎప్పుడు ఉపయోగించాలి  
- "నా Azure సబ్‌స్క్రిప్షన్‌పై అన్ని నోట్‌బుక్స్ / నమూనాలను సరిచూడండి."  
- "ప్యాకేజీలను అప్‌గ్రేడ్ చేసిన తర్వాత లేదా మోడల్స్ మార్చిన తర్వాత కోర్సును స్మోక్-టెస్ట్ చేయండి."  
- "ఎలాంటి పాఠాలు ఇంకా లైవ్‌లో PASS / FAIL అవుతున్నాయి?"  

AI స్మోక్ టెస్ట్ GitHub ఆక్షన్ (deploy చేసిన వాటిని సరిచూసే) కోసం దీన్ని ఉపయోగించకండి.  
హోస్టెడ్ ఏజెంట్లు — చూడండి [`tests/README.md`](../../../tests/README.md)). ఈ నైపుణ్యం
నోటుబుక్స్‌ను స్థానికంగా నడిపిస్తుంది.

## ముందస్తు అవసరాలు (ముందుగా తనిఖీ చేయండి)
1. **Python 3.12+** కోర్సు డిపెండెన్సీలతో: `python -m pip install -r requirements.txt`
   అదనంగా ఎగ్జిక్యూటర్: `python -m pip install nbconvert ipykernel`.
2. **`.env` రిపో రూట్ వద్ద** (నకలు చేయండి [`.env.example`](../../../../../.env.example)) కనీసం:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry ప్రాజెక్టు ఎండ్పాయింట్
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — ఒక డిప్రిస్కేటెడ్ కాకపోయిన డిప్లాయ్‌మెంట్ (ఉదాహరణకు `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) మరియు `AZURE_OPENAI_DEPLOYMENT`
     ప్రత్యక్షంగా Azure OpenAI ని పిలుస్తున్న పాఠాలు కోసం (పాఠం 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** పూర్తి చేయాలి — నమూనాలు `AzureCliCredential` తో ధృవీకరించబడతాయి (Entra ID, కీ లేకుండా).
4. మోడల్ డిప్లాయ్‌మెంట్ ఉన్నట్లు నిర్ధారించుకోండి:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## ధృవీకరణ నడుపుట
```powershell
# All Python notebooks (skips .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# A single lesson, with a longer per-cell timeout
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Just list what would run (no execution)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit interpreter (if `python` is not on PATH, e.g. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
స్క్రిప్ట్ నడిపించిన ప్రతిలిపులను, ప్రతి-నోటుబుక్ లాగ్‌లను మరియు `results.json` ను
`$env:TEMP\aiab-nbval` లో రాస్తుంది మరియు విఫలాల సంఖ్యతో బయటకు వస్తుంది.

తాత్కాలిక విఫలతలు (షేర్ చేసిన సబ్‌స్క్రిప్షన్ HTTP 429 రేట్ పరిమితులు, ఒక సారి ఒకసారి
`AzureCliCredential` టోకెన్ సమస్య లేదా టైమౌట్) స్వయంచాలకంగా మళ్లీ ప్రయత్నిస్తాయి
(`-Retries`, డిఫాల్ట్ 2, `-RetryDelaySeconds` బ్యాకాఫ్‌తో, డిఫాల్ట్ 20). ఒక
మోడల్ డిప్లాయ్‌మెంట్ తరచూ 429 స్రవిస్తుంటే, సబ్‌స్క్రిప్షన్ యొక్క GlobalStandard
TPM క్వోటాను (`az cognitiveservices usage list -l <region>`) తనిఖీ చేయండి — ఒకే డిప్లాయ్‌మెంట్ సామర్థ్యాన్ని పెంచడము సహాయపడదు جڏهن *సబ్‌స్క్రిప్షన్* క్వోటా పూర్తవుతుంది.


## ఫలితాలను అర్థం చేసుకోవడం
- `PASS` — నోటుబుక్ ఎండ్-టు-ఎండ్ ఎలాంటి సెల్ తప్పు లేకుండా నడిచింది.
- `FAIL` — మొదటి `*Error` / `*Exception` లైన్ చూపబడుతుంది; పూర్తి ట్రేస్‌ బ్యాక్ కోసం సరిపోయే
   `log_*.txt` ని అవుట్‌పుట్ డైరెక్టరీలో తెరవండి.
- ఒకే నోటుబుక్ విఫలతను `-Timeout` (ప్రతి సెల్ నిండుల) తో పరిమితం చేస్తారు, అందువల్ల హంగ్ అయిన
  హ్యూమన్-ఇన్-ది-లూప్ సెల్ `StdinNotImplementedError` గా కనిపిస్తుంది, హంగ్ కాకుండా.

## అదనపు వనరులు అవసరమైన పాఠాలు (వాటిలేని పక్షంలో విఫలమవ్వచ్చు)
| పాఠం | అదనపు అవసరం |
|--------|-------------------|
| 05 Agentic RAG | Azure AI సెర్చ్ (`AZURE_SEARCH_SERVICE_ENDPOINT`, కీ) — ఒక ఇన్-మెమరీ ఫాల్బ్యాక్ మార్గం కలదు |
| 11 MCP / GitHub | GitHub MCP సర్వర్ + PAT |
| 13 memory (cognee) | `cognee` మోడల్ ప్రొవైడర్ తో కాన్ఫిగర్ చేయబడింది |
| 15 browser-use | Playwright బ్రౌజర్‌లు ఇన్‌స్టాల్ చేయబడ్డాయి (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry లోకల్ రన్‌టైం + డౌన్లోడ్ చేసిన Qwen మోడల్ (డివైస్‌పై, క్లౌడ్ లేదు) |
| `*-dotnet-*` నోటుబుక్స్ | .NET ఇంటరాక్టివ్ కర్నెల్ (డిఫాల్ట్‌‌తొ బయట; ఉపయోగించండి `-IncludeDotnet`) |

## ఫిర్యాదు తెలియజేయడం
పాఠం ప్రాతిపదికన PASS/FAIL పట్టిక రూపంలో సారాంశం ఇవ్వండి. నిజమైన పునరావృతాలు
(కోడ్/కాన్ఫిగ్ బగ్స్ పరిష్కారం చేయవలసినవి) వాతావరణ లోపాల నుండి వేరు చేయండి (అన్లభ్యమైన సెర్చ్/Foundry లోకల్/PAT),
మరియు ప్రతి నిజమైన విఫలతకు విఫలమైన `log_*.txt` ను సూచించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->