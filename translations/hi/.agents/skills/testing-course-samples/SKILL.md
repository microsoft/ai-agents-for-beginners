---
name: testing-course-samples
---
# पाठ्यक्रम नमूनों का परीक्षण

सत्यापित करें कि पाठ नोटबुक और कोड नमूने एक लाइव
Microsoft Foundry / Azure OpenAI सेटअप के खिलाफ चल रहे हैं। रिपो एक रनर भेजता है
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) जो
हर पायथन नोटबुक को हेडलेसली निष्पादित करता है और एक PASS/FAIL मैट्रिक्स प्रिंट करता है।

## कब उपयोग करें
- "मेरी Azure सदस्यता के खिलाफ सभी नोटबुक / नमूनों को सत्यापित करें।"
- "पैकेज को अपग्रेड करने या मॉडल बदलने के बाद कोर्स का स्मोक-टेस्ट करें।"
- "कौन से पाठ अभी भी लाइव में पास / फेल होते हैं?"

AI स्मोक टेस्ट GitHub एक्शन (जो *तैनात* होस्टेड एजेंट्स को सत्यापित करता है — देखें [`tests/README.md`](../../../tests/README.md)) के लिए इसका उपयोग **नहीं** करें। यह स्किल नोटबुक को स्थानीय रूप से चलाता है।



## आवश्यकताएँ (पहले जांचें)
1. **Python 3.12+** पाठ्यक्रम डिप्स के साथ: `python -m pip install -r requirements.txt`
   साथ ही कार्यपालक: `python -m pip install nbconvert ipykernel`।
2. **रिपो रूट पर `.env`** ([`.env.example`](../../../../../.env.example) से कॉपी करें) जिसमें कम से कम:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry प्रोजेक्ट एंडपॉइंट
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — एक गैर-डिप्रिकेटेड डिप्लॉयमेंट (जैसे `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) और `AZURE_OPENAI_DEPLOYMENT`
     उन पाठों के लिए जो Azure OpenAI को सीधे कॉल करते हैं (Lesson 06, 02-azure-openai, 14 handoff/human-loop)।
3. **`az login`** पूरा हुआ — नमूने `AzureCliCredential` के साथ प्रमाणीकृत होते हैं (Entra ID, बिना कुंजी के)।
4. सत्यापित करें कि मॉडल डिप्लॉयमेंट मौजूद है:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`।

## सत्यापन चलाना
```powershell
# सभी पाइथन नोटबुक्स (छोड़ें .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# एकल पाठ, प्रत्येक सेल के लिए अधिक समय सीमा के साथ
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# केवल बताएं क्या चलेगा (कोई निष्पादन नहीं)
pwsh scripts/validate-notebooks.ps1 -List

# स्पष्ट इंटरप्रेटर (अगर `python` PATH में नहीं है, जैसे Windows Store उपनाम)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
स्क्रिप्ट निष्पादित प्रतियां, प्रति नोटबुक लॉग, और `results.json` को
`$env:TEMP\aiab-nbval` में लिखती है और विफलताओं की संख्या के साथ निकलती है।

## परिणामों की व्याख्या
- `PASS` — नोटबुक ने बिना सेल त्रुटि के पूरा रन किया।
- `FAIL` — पहली `*Error` / `*Exception` लाइन दिखाई जाती है; आउटपुट डायरेक्टरी में मेल खाने वाला
  `log_*.txt` खोलें पूरे ट्रेसबैक के लिए।
- एक एकल नोटबुक की विफलता `-Timeout` (प्रति सेल) द्वारा सीमित होती है, इसलिए एक रुका हुआ
  मानव-इन-द-लूप सेल `StdinNotImplementedError` के रूप में प्रदर्शित होता है न कि हैंग होता है।

## अतिरिक्त संसाधनों वाले पाठ (उनके बिना विफल होने की उम्मीद)
| पाठ | अतिरिक्त आवश्यकताएं |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — एक इन-मेमोरी बैकअप पाथ के साथ |
| 11 MCP / GitHub | GitHub MCP सर्वर + PAT |
| 13 memory (cognee) | `cognee` एक मॉडल प्रदाता के साथ कॉन्फ़िगरेड |
| 15 browser-use | Playwright ब्राउज़र इंस्टॉल किए हुए (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local रनटाइम + एक डाउनलोड किया हुआ Qwen मॉडल (डिवाइस पर, कोई क्लाउड नहीं) |
| `*-dotnet-*` नोटबुक | .NET इंटरएक्टिव कर्नेल (डिफ़ॉल्ट से बाहर; `-IncludeDotnet` का उपयोग करें) |

## रिपोर्टिंग वापस
एक PASS/FAIL टेबल के रूप में सारांश करें जो पाठ द्वारा समूहित हो। असली रिग्रेशन
(कोड/कॉन्फ़िग बग जिन्हें ठीक करना है) को पर्यावरण अंतरालों (मिसिंग Search/Foundry Local/PAT)
से अलग करें, और प्रत्येक वास्तविक विफलता के लिए विफल `log_*.txt` का उल्लेख करें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->