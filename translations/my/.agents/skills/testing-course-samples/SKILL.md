---
name: testing-course-samples
---
# သင်တန်းနမူနာများကို စမ်းသပ်ခြင်း

သင်ခန်းစာ မှတ်စုစာအုပ်များနှင့် ကုဒ်နမူနာများကို live
Microsoft Foundry / Azure OpenAI စနစ်တစ်ခုအားတည်ဆောက်၍ စမ်းသပ်ခြင်း။ repo တွင်
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) တွင် runner တစ်ခုပါဝင်ပြီး
Python မှတ်စုစာအုပ်အားလုံးကို headlessly အလုပ်လုပ်စေပြီး PASS/FAIL matrix ကို 출력တယ်။

## ဘယ်အချိန်တွင် အသုံးပြုမလဲ
- "ကျွန်ုပ်၏ Azure subscription နှင့်အတူ နိုတ်ဘုတ်များ / ဥပမာများအားလုံးကို စစ်ဆေးခြင်း။"
- "ပက်ကေ့ဂျ်များကို မြှင့်တင်ခြင်း သို့မဟုတ် မော်ဒယ်များကို ပြောင်းလဲခြင်း ပြီးနောက် သင်တန်းကို Smoke-test ဆောင်ရွက်ခြင်း။"
- "ဘယ်သင်ခန်းစာများသည် တိုက်ရိုက်စမ်းသပ်မှုမှ အောင်မြင် / မအောင်မြင်နေလဲ?"

AI Smoke Test GitHub Action (မည်သည့် *deploy လုပ်ထားသော* ကို အတည်ပြုသည့်) အတွက် မသုံးရပေ။ 
hosted agents — ကြည့်ပါ [`tests/README.md`](../../../tests/README.md))။ ဒီကျွမ်းကျင်မှုက
notebook များကို ဒေသတွင်းတွင် ချပြင်ပြီး အလုပ်လုပ်စေသည်။

## မတိုင်မီလိုအပ်ချက်များ (ပထမဦးစွာ စစ်ဆေးပါ)
1. **Python 3.12+** နှင့် course dependencies: `python -m pip install -r requirements.txt`
   နှင့် executor ကိုလည်း: `python -m pip install nbconvert ipykernel`။
2. **`.env` ကို repo root တွင်** (ကူးယူပါ [`.env.example`](../../../../../.env.example)) အနည်းဆုံးပါရှိရမည် -
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry project endpoint
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — deprecated မဟုတ်သော deployment တစ်ခု (ဥပမာ `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) နှင့် `AZURE_OPENAI_DEPLOYMENT`
     Azure OpenAI ကိုတိုက်ရိုက်ခေါ်သုံးသော သင်ခန်းစာများအတွက် (သင်ခန်းစာ 06, 02-azure-openai, 14 handoff/human-loop)။
3. **`az login`** ပြီးစီးပြီးသား — နမူနာများသည် `AzureCliCredential` ဖြင့် Authenticate လုပ်သည် (Entra ID, keyless)။
4. မော်ဒယ် deployment ရှိပါစေကြောင်းအတည်ပြုပါ -
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`။

## အတည်ပြုခြင်းကို ပြုလုပ်ခြင်း
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
 စက္ကန့်ကိုလက်ခံပြီး သေချာပြုလုပ်ထားသော မိတ္တူများ၊ per-notebook logs နှင့် `results.json` ကို
`$env:TEMP\aiab-nbval` သိုလှောင်ပြီး မအောင်မြင်မှု အရေအတွက်နဲ့ ထွက်ခွာသည်။

အရက်ရှားသော အဆို့အတားများ (shared-subscription HTTP 429 rate limits, ကြိမ်တိုင်း
`AzureCliCredential` token hiccup တစ်ခဏအကြိမ်ကြိမ် ဖြစ်ခြင်း သို့မဟုတ် timeout) ကို အလိုအလျောက် ပြန်လည်ကြိုးစားသည်
(`-Retries`, ပုံမှန် 2, `-RetryDelaySeconds` backoff နဲ့, ပုံမှန် 20)။ မော်ဒယ် deployment မှ
စဉ်ဆက်မပြတ် 429 ဖြစ်နေပါက subscription ၏ GlobalStandard
TPM quota (`az cognitiveservices usage list -l <region>`) ကိုစစ်ဆေးပါ — တစ်ခုတည်းသော
deployment ၏ မှတ်တမ်းတိုးမြှင့်ခြင်းသည် *subscription* quota ပြည့်သွားသောအချိန်တွင် အကျိုးမရှိပါ။

## ရလဒ်များကို ဖတ်ရှုခြင်း
- `PASS` — notebook ကို အဆင်ပြေအောင် အဆုံးသတ် cell error မရှိဘဲ run ခြင်း။
- `FAIL` — ပထမဆုံး `*Error` / `*Exception` ကုဒ်တန်းပြသည်။ သင့်တော်သော
  `log_*.txt` ကို output directory မှာဖွင့်ပြီး လုံးဝ traceback ကို ကြည့်ရှုပါ။
- တစ်ခုတည်းသော notebook ၏ မအောင်မြင်မှုကို `-Timeout` (per cell) ဖြင့် ကန့်သတ်ထားပြီး၊ လူ့ loop ၏ cell မှာ ကိုင်တွယ်သေချာမှုမရှိဘဲ
  `StdinNotImplementedError` အဖြစ် ပြသပါသည်။

## အပိုအရင်းအမြစ်များ လိုအပ်သော သင်ခန်းစာများ (မရှိမဖြစ် ပြုတ်မည်ဟုမျှော်လင့်)
| သင်ခန်းစာ | အပို လိုအပ်ချက် |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — in-memory fallback လမ်းကြောင်းပါရှိသည် |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memory (cognee) | `cognee` ကို model provider ဖြင့် ဖြည့်စွက်ထားသည် |
| 15 browser-use | Playwright browsers ထည့်သွင်းထားသည် (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime နှင့် Qwen model ကြိုးပမ်းကုန်ပြီး (on-device, မိုဃ်းမှမဟုတ်) |
| `*-dotnet-*` notebooks | .NET Interactive kernel (default အနေဖြင့် ထားမှပိတ်ထားတယ်; `-IncludeDotnet` ကို အသုံးပြုပါ) |

## ပြန်တင်ပြခြင်း
သင်ခန်းစာ အလိုက် အုပ်စုဖွဲ့ပြီး PASS/FAIL အဇယားအဖြစ် အနှစ်ချုပ်တင်ပြပါ။ အမှန်တကယ် ပြောင်းလဲမှုများ
(ကုဒ်/config အမှားများ ပြင်ဆင်ရန်) နှင့် ပတ်ဝန်းကျင်ဆိုင်ရာ ပြဿနာများ (Search/Foundry Local/PAT မရှိခြင်း) ကို ခွဲခြားပါ။
နှင့် ပျက်ကွက်ခြင်း တစ်ခုချင်းစီအတွက် မအောင်မြင်သော `log_*.txt` ကို ဖော်ပြပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->