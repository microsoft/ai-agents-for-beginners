---
name: testing-course-samples
---
# သင်တန်းနမူနာများ စမ်းသပ်ခြင်း

သင်ခန်းစာစာအုပ်များနှင့် ကုဒ်နမူနာများကို Microsoft Foundry / Azure OpenAI စနစ်တစ်ခုနှင့် ထိတွေ့ပြေးဆွဲထားသည်ကို အတည်ပြုပါ။ Repo သည်
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) တွင် runner တစ်ခု ပါရှိပြီး
Python notebook အားလုံးကို headless ဖြင့် ပြေးဆွဲကာ PASS/FAIL ဇယားကို ပုံထုတ်ပေးသည်။


## မည့်အချိန်တွင်အသုံးပြုမည်နည်း
- "ငါ့ Azure subscription နှင့် စာအုပ်များ / နမူနာအားလုံးကို အတည်ပြုမည်။"
- "ပက်ကေ့ဂျ်များ အဆင့်မြှင့်တင်ခြင်း သို့မဟုတ် မော်ဒယ်များပြောင်းလဲခြင်းအပြီး သင်တန်းကို smoke-test လုပ်မည်။"
- "မည်သည့်သင်ခန်းစာများသည် ထိုစနစ်နှင့်တကြ PASSED / FAILED ဖြစ်နေသနည်း။"

AI Smoke Test GitHub Action (deployed hosted agents များအတွက် အတည်ပြုချက် — [`tests/README.md`](../../../tests/README.md) တွင် ကြည့်ပါ) အတွက် သုံးရန် မဟုတ်ပါ။
ကိုးကားသည့် skill သည် notebook များအား ဒေသခံတွင် ပြေးဆွဲသည်။


1. **Python 3.12+** နှင့် သင်ခန်းစာ များ လိုအပ်ချက်များ: `python -m pip install -r requirements.txt`
   နှင့် executor: `python -m pip install nbconvert ipykernel`.
2. **repo အခြေခံ .env ဖိုင်** ([`.env.example`](../../../../../.env.example) မှ ကူးယူပါ) အနည်းဆုံး
   ပါဝင်ရန် -
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry project endpoint
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — အတည်ပြုထားသေးသော deployment မဟုတ်သည့် deployment (ဥပမာ `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) နှင့် `AZURE_OPENAI_DEPLOYMENT`
     သင်ခန်းစာများတွင် Azure OpenAI ကို တိုက်ရိုက် ခေါ်သုံးနိုင်ရန် (Lesson 06, 02-azure-openai, 14 handoff/human-loop)။
3. **`az login`** ပြီးဆုံးထားရန် — samples များသည် `AzureCliCredential` ဖြင့် သက်တမ်းတည် ဂရုထည့်ချက်ရသည် (Entra ID, keyless).
4. မော်ဒယ် deployment ရှိမရှိ အတည်ပြုရန်:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## အတည်ပြုချက် ပြေးဆွဲခြင်း
```powershell
# Python နိုတ်ဘွတ်များအားလုံး (.NET, .venv, site-packages, ဘာသာပြန်ချက်များ, ကျွမ်းကျင်မှုဆိုင်ရာပစ္စည်းများကို မထည့်ပါ)
pwsh scripts/validate-notebooks.ps1

# တစ်ခန်းစာတည်း၊ ဆဲလ်တစ်ခုချင်းစီအတွက် ပိုရှည်သော အချိန်ပြည့်သတ်မှတ်ချက်ဖြင့်
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# လည်ပတ်မည့်အရာကိုသာ စာရင်းပြုစုခြင်း (မလည်ပတ်ပါ)
pwsh scripts/validate-notebooks.ps1 -List

# ထူးခြားသတ်မှတ်ထားသော တိကျသော interpreter (PATH တွင် `python` မရှိပါက၊ ဥပမာ Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
 script သည် ဗဟိုစာတမ်းဟောင်းများ၊ notebook လေ့လာထားသော log များနှင့် `results.json` ကို
`$env:TEMP\aiab-nbval` တွင် ရေးထုတ်ပြီး အောင်မြင်မှု မရှိမှုအရေအတွက်နှင့်အတူ ထွက်ခွာသည်။

## ရလဒ်၏ အဓိပ္ပာယ်ဖွင့်ချက်
- `PASS` — notebook သည် အစမှအဆုံး error မရှိဘဲ ပြေးဆွဲနိုင်ခဲ့သည်။
- `FAIL` — ပထမဆုံး `*Error` / `*Exception` အကြောင်းအရာကို ပြသည်; ထည့်သွင်းပါသော
  ယူနစ် `log_*.txt` ကို output လမ်းကြောင်းတွင်ဖွင့်၍ အပြည့်အစုံ traceback ကို ကြည့်ရှုနိုင်သည်။
- တစ်ရက်အတွင်း notebook တစ်ခုချင်း ချို့ယွင်းမှုမှာ `-Timeout` (ယူနစ်အလိုက်) ဖြင့် ကန့်သတ်ထားပြီး
  လူလှည့်ဝင်မည့် ယူနစ်များသည် `StdinNotImplementedError` အဖြစ်ပေါ်လာပြီး ချုပ်သိမ်းခြင်း မဖြစ်ပါ။

## အပိုလိုအပ်ချက်ရှိ သင်ခန်းစာများ (မပါဝင်လျှင် အောင်မြင်မှု မရှိဘူးထင်ရ)
| သင်ခန်းစာ | အပိုလိုအပ်ချက် |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — in-memory fallback လမ်းကြောင်း ပါရှိသည် |
| 11 MCP / GitHub | GitHub MCP ဆက်သွယ်မှု + PAT |
| 13 memory (cognee) | `cognee` ကို မော်ဒယ်ပံ့ပိုးသူနှင့် သတ်မှတ်ထားသည် |
| 15 browser-use | Playwright browsers (install ပြီး) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + Qwen မော်ဒယ် ဒေါင်းလုပ်ပြီး (device ပေါ်တွင်, cloud မလို) |
| `*-dotnet-*` notebooks | .NET Interactive kernel (ပုံမှန်အားဖြင့် ဖယ်ရှားထားသည်; `-IncludeDotnet` အသုံးပြု) |

## ပြန်လည်အစီရင်ခံခြင်း
PASS/FAIL ဇယားအရ သင်ခန်းစာအလိုက် စုစည်း၍ တင်ပြပါ။ အမှန်တကယ် ပြဿနာရှိသော regression များ
(ကုဒ်/configuration အမှားများ) နှင့် ပတ်ဝန်းကျင် အားနည်းချက်များ (Search/Foundry Local/PAT မရှိခြင်း) ကို ခွဲခြားပါ။
ပြဿနာရှိ notebook အပြည့်အစုံကို `log_*.txt` နောက်ခံ ဖိုင်ထံ မှတ်ချက်ပြုပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->