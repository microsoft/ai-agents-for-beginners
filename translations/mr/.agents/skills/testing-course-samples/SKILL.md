---
name: testing-course-samples
description: जेव्हा Microsoft Foundry / Azure OpenAI च्या लाईव्ह कॉन्फिगरेशन विरुद्ध
  कोर्सचा नोटबुक आणि कोड नमुने व्हॅलिडेट, टेस्ट, स्मोक-टेस्ट, किंवा चालवायचे असे विचारले
  जाते तेव्हा वापरा. यात वातावरण सेटअप (.env, az login, पॅकेजेस), स्क्रिप्ट्स/validate-notebooks.ps1
  रन्नर, PASS/FAIL निकालांचे अर्थ लावणे, आणि कोणत्या धड्यांना अतिरिक्त संसाधने (Azure
  AI Search, GitHub MCP, Foundry Local, Playwright) आवश्यक आहेत याचा समावेश आहे.
---
# कोर्स नमुन्यांची चाचणी करणे

धडा नोटबुक आणि कोड नमुने Microsoft Foundry / Azure OpenAI सेटअपवर प्रत्यक्ष चालतात याची पडताळणी करा.
रेपो [`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) येथे एक रनर प्रदान करतो ज्यामुळे
प्रत्येक Python नोटबुक हेडलेस पद्धतीने चालविला जातो आणि PASS/FAIL मॅट्रिक्स छापला जातो.


- "माझ्या Azure सदस्यत्वाद्वारे सर्व नोटबुक / नमुन्यांची पडताळणी करा."
- "पॅकेजेस अपग्रेड केल्यानंतर किंवा मॉडेल बदलल्यानंतर कोर्सचे स्मोक-टेस्ट करा."
- "कोणते धडे अजूनही प्रत्यक्ष चालतात / फेल होतात?"


कृपया AI Smoke Test GitHub कृतीसाठी (जी *प्रकाशित* असल्याची पडताळणी करते) हे वापरू नका
होस्ट केलेले एजंट्स — पाहा [`tests/README.md`](../../../tests/README.md)). हा कौशल्य
नोटबुक्स स्थानिकपणे चालवतो.

## पूर्वअटी (प्रथम तपासा)
1. **Python 3.12+** कोर्स डेप्ससह: `python -m pip install -r requirements.txt`
   तसेच एक्झिक्युटर: `python -m pip install nbconvert ipykernel`.
2. **`.env` रेपो रूटवर** ([`.env.example`](../../../../../.env.example) कडून कॉपी करा) कमीतकमी:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry प्रोजेक्ट एन्डपॉइंट
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — एक नॉन-डिप्रिकेटेड डिप्लॉयमेंट (उदा. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) आणि `AZURE_OPENAI_DEPLOYMENT`
     ज्यासाठी धडे Azure OpenAI थेट कॉल करतात (Lesson 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** पूर्ण केलेले — नमुने `AzureCliCredential` (Entra ID, कीलेस) सह प्रमाणित करतात.
4. मॉडेल डिप्लॉयमेंट अस्तित्वात आहे हे सत्यापित करा:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## वैधता चालविणे
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
स्क्रिप्ट कार्यान्वित केलेल्या प्रती, प्रति-नोटबुक लॉग्स, आणि `results.json` लिहिते
`$env:TEMP\aiab-nbval` वर आणि अपयशांची संख्या सह बाहेर पडते.

तात्पुरते अपयशे (शेअर-सदस्यता HTTP 429 दर मर्यादा, कधी कधी
`AzureCliCredential` टोकन हिच्काप (hiccup), किंवा टाइमआउट झाल्यास) आपोआप पुनःप्रयत्न केल्या जातात
(`-Retries`, डीफॉल्ट 2, `-RetryDelaySeconds` बॅकऑफसह, डीफॉल्ट 20). जर एखादा
मॉडेल डिप्लॉयमेंट नियमितपणे 429 त्रुटी देत असेल, तर सदस्यत्वाचा GlobalStandard
TPM कोटा (`az cognitiveservices usage list -l <region>`) तपासा — एका
डिप्लॉयमेंटची क्षमता वाढविल्याने उपयोग होत नाही जेव्हा *सदस्यत्वाचा* कोटा संपतो.

## निकालांचे अर्थ लावणे
- `PASS` — नोटबुक कोणतीही सेल त्रुटी न देता अखंड चालला.
- `FAIL` — पहिला `*Error` / `*Exception` ओळ दाखवली जाते; पूर्ण
  ट्रेसबॅकसाठी आउटपुट डायरेक्टरीतील जुळणारी `log_*.txt` उघडा.
- एका नोटबुकची अपयशाची मर्यादा `-Timeout` (प्रति सेल) आहे, त्यामुळे अडकलेल्या
  माणसाच्या हस्तक्षेपाच्या सेलला `StdinNotImplementedError` म्हणून ओळखले जाते, अडकण्याऐवजी.

## अतिरिक्त संसाधने आवश्यक असलेल्या धड्यांसाठी (त्यांशिवाय अपयशी होण्याची शक्यता)
| धडा | अतिरिक्त आवश्यकता |
|--------|-------------------|
| 05 एजेन्टिक RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, की) — एक इन-मेमरी फॉलबॅक मार्ग आहे |
| 11 MCP / GitHub | GitHub MCP सर्व्हर + PAT |
| 13 मेमरी (cognee) | `cognee` मॉडेल पुरवठादारासह कॉन्फिगर केलेले |
| 15 ब्राउझर-उपयोग | Playwright ब्राउझर इंस्टॉल केलेले (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 स्थानिक एजंट | Foundry स्थानिक रनटाइम + डाउनलोड केलेला Qwen मॉडेल (ऑन-डिव्हाइस, क्लाऊड नाही) |
| `*-dotnet-*` नोटबुक्स | .NET इंटरएक्टिव्ह कर्नेल (डीफॉल्टनंतर वगळलेले; वापरा `-IncludeDotnet`) |

## अहवाल परत पाठवणे
धड्यांच्या आधारे PASS/FAIL सारणीएकत्र करा. खरी रिग्रेशन (कोड/कॉन्फिग बग्स दुरुस्त करणे आवश्यक)
पर्यावरणातील गॅप्स (Search/Foundry Local/PAT चा अभाव) यापासून वेगळे करा,
आणि प्रत्येक खरी अपयशासाठी फेल झालेल्या `log_*.txt` ची नोंद करा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->