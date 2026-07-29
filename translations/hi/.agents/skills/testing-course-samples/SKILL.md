---
name: testing-course-samples
---
# कोर्स नमूनों का परीक्षण करना

सत्यापित करें कि पाठ नोटबुक और कोड नमूने लाइव Microsoft Foundry / Azure OpenAI सेटअप के खिलाफ चलते हैं।
इस रिपो में एक रनर शामिल है
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) जो
हर एक पायथन नोटबुक को हेडलेस तरीके से चलाता है और PASS/FAIL मैट्रिक्स दिखाता है।

## कब उपयोग करें
- "मेरे Azure सब्सक्रिप्शन के खिलाफ सभी नोटबुक / नमूनों को सत्यापित करें।"
- "पैकेज अपग्रेड या मॉडल बदलने के बाद कोर्स का स्मोक-टेस्ट करें।"
- "कौन से पाठ अभी भी लाइव में पास / फेल हो रहे हैं?"

AI स्मोक टेस्ट GitHub एक्शन के लिए **इसका उपयोग न करें** (जो *डिप्लॉय किए गए*
होस्टेड एजेंट्स को सत्यापित करता है — देखें [`tests/README.md`](../../../tests/README.md))। यह स्किल
नोटबुक को स्थानीय रूप से चलाता है।

## पूर्व आवश्यकताएँ (पहले जांचें)
1. **Python 3.12+** के साथ कोर्स निर्भरताएँ: `python -m pip install -r requirements.txt`
   साथ ही कार्यान्वयन के लिए: `python -m pip install nbconvert ipykernel`।
2. **`.env` रिपो रूट पर** ([`.env.example`](../../../../../.env.example) से कॉपी करें) जिसमें कम से कम:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry प्रोजेक्ट का एंडपॉइंट
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — एक गैर-देप्रिकेटेड डिप्लॉयमेंट (जैसे `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) और `AZURE_OPENAI_DEPLOYMENT`
     उन पाठों के लिए जो सीधे Azure OpenAI को कॉल करते हैं (Lesson 06, 02-azure-openai, 14 handoff/human-loop)।
3. **`az login`** पूरा किया हुआ — नमूने `AzureCliCredential` (Entra ID, बिना कुंजी के) के साथ प्रमाणीकरण करते हैं।
4. जांचें कि मॉडल डिप्लॉयमेंट मौजूद है:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`।

## सत्यापन चलाना
```powershell
# सभी पाइथन नोटबुक (स्किप करता है .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# एक अकेरा पाठ, प्रत्येक सेल के लिए लंबा टाइमआउट के साथ
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# केवल सूची बनाएं कि क्या चलेगा (कोई निष्पादन नहीं)
pwsh scripts/validate-notebooks.ps1 -List

# स्पष्ट समझाने वाला (यदि `python` PATH में नहीं है, जैसे विंडोज स्टोर उपनाम)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
स्क्रिप्ट निष्पादित प्रतियां, प्रति नोटबुक लॉग और `results.json` को
`$env:TEMP\aiab-nbval` में लिखती है और विफलताओं की संख्या के साथ बाहर निकलती है।

अस्थाई विफलताएं (साझा सब्सक्रिप्शन HTTP 429 दर सीमाएं, कभी-कभी
`AzureCliCredential` टोकन में समस्या, या टाइमआउट) स्वचालित रूप से पुनः प्रयास की जाती हैं
(`-Retries`, डिफ़ॉल्ट 2, `-RetryDelaySeconds` बैकऑफ के साथ, डिफ़ॉल्ट 20)। यदि कोई
मॉडल डिप्लॉयमेंट नियमित रूप से 429 प्रदर्शित कर रहा है, तो सब्सक्रिप्शन का GlobalStandard
TPM कोटा जांचें (`az cognitiveservices usage list -l <region>`) — एकल
डिप्लॉयमेंट की क्षमता बढ़ाने से तब मदद नहीं मिलती जब *सब्सक्रिप्शन* कोटा समाप्त हो चुका हो।

## परिणामों की व्याख्या करना
- `PASS` — नोटबुक बिना किसी सेल त्रुटि के अंत से अंत तक चली।
- `FAIL` — पहली `*Error` / `*Exception` लाइन दिखाई जाती है; पूर्ण ट्रेसबैक के लिए आउटपुट डायरेक्टरी में मेल खाता
  `log_*.txt` खोलें।
- एकल नोटबुक की विफलता `-Timeout` (प्रति सेल) द्वारा सीमित होती है, इसलिए अटकी हुई
  human-in-the-loop सेल `StdinNotImplementedError` के रूप में प्रकट होती है बजाय अटके रहने के।

## अतिरिक्त संसाधनों की जरूरत वाले पाठ (बिना इनके विफल होने की उम्मीद)
| पाठ | अतिरिक्त आवश्यकता |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, कुंजी) — मेमोरी में फॉलबैक पथ के साथ |
| 11 MCP / GitHub | GitHub MCP सर्वर + PAT |
| 13 memory (cognee) | `cognee` एक मॉडल प्रदाता के साथ कॉन्फ़िगर किया गया |
| 15 browser-use | Playwright ब्राउज़र इंस्टॉल किए हुए (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local रनटाइम + डाउनलोड किया गया Qwen मॉडल (डिवाइस पर, क्लाउड नहीं) |
| `*-dotnet-*` नोटबुक | .NET Interactive कर्नेल (डिफ़ॉल्ट रूप से अंशित; उपयोग करें `-IncludeDotnet`) |

## रिपोर्टिंग वापस
पाठ द्वारा समूहबद्ध PASS/FAIL तालिका के रूप में सारांश करें। वास्तविक रिग्रेशन
(कोड/कॉन्फ़िग बग जिन्हें ठीक करना है) को वातावरण की कमियों (मिसिंग Search/Foundry Local/PAT) से अलग करें,
और प्रत्येक वास्तविक विफलता के लिए विफल `log_*.txt` का उल्लेख करें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->