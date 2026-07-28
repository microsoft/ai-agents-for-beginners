---
name: testing-course-samples
---
# पाठ्यक्रम नमुनाहरू परीक्षण गर्दै

सिकियौं कि पाठ नोटबुकहरू र कोड नमूनाहरू लाइभ
Microsoft Foundry / Azure OpenAI सेटअपमा चल्छन् कि छैनन्। रेपोले एक रनर पठाउँछ
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) जुन
हरेक Python नोटबुकलाई हेडलेस रूपमा चलाउँछ र PASS/FAIL म्याट्रिक्स प्रिन्ट गर्छ।

## कहिलेकाहीं प्रयोग गर्ने
- "मेरो Azure सदस्यतामा सबै नोटबुक / नमूनाहरू प्रमाणित गर्न।"
- "प्याकेजहरू अपडेट गरेपछि वा मोडेलहरू परिवर्तन गरेपछि पाठ्यक्रमलाई स्मोक-टेस्ट गर्न।"
- "कुन पाठहरू लाइभमा अझै पास / फेल छन्?"

AI स्मोक टेस्ट GitHub Action (जसले *डिप्लोय* गरिएका
होस्ट एजेन्टहरू प्रमाणित गर्छ — हेर्नुहोस् [`tests/README.md`](../../../tests/README.md)) मा यसलाई प्रयोग नगर्नुहोस्। यो कौशलले
नोटबुकहरू स्थानीय रूपमा चलाउँछ।

## पूर्वापेक्षाहरू (पहिले जाँच्न)
1. **Python 3.12+** संग पाठ्यक्रम निर्भरताहरू: `python -m pip install -r requirements.txt`
   र एक्जीक्युटर: `python -m pip install nbconvert ipykernel`।
2. **रेपो मूलमा `.env` फाइल** (कोपी गर्नुहोस् [`.env.example`](../../../../../.env.example) बाट) कम्तीमा:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry परियोजना अन्त बिंदु
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — गैर-पुरानो गरिएको डिप्लोयमेन्ट (जस्तै `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) र `AZURE_OPENAI_DEPLOYMENT`
     जसले Azure OpenAI प्रत्यक्ष कल गर्ने पाठहरूको लागि (पाठ 06, 02-azure-openai, 14 handoff/human-loop)।
3. **`az login`** पूरा भएको — नमूनाहरू `AzureCliCredential` (Entra ID, बिना कुञ्जी) द्वारा प्रमाणीकरण गर्छन्।
4. मोडेल डिप्लोयमेन्ट अस्तित्वमा छ कि छैन जाँच्नुहोस्:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`।

## प्रमाणिकरण चलाउने
```powershell
# सबै पाइथन नोटबुकहरू (.NET, .venv, साइट-प्याकेजहरू, अनुवादहरू, सीप सम्पत्तिहरू छोडिन्छ)
pwsh scripts/validate-notebooks.ps1

# एकल पाठ, लामो प्रति-सेल टाइमआउट सहित
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# के मात्र चल्नेछ सूचीबद्ध गर्नुहोस् (कुनै कार्यान्वयन छैन)
pwsh scripts/validate-notebooks.ps1 -List

# स्पस्ट व्याख्याता (यदि `python` PATH मा छैन भने, जस्तै Windows Store उपनाम)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
स्क्रिप्टले चलाइएका प्रतिलिपिहरू, प्रति-नोटबुक लगहरू, र `results.json` लाई
`$env:TEMP\aiab-nbval` मा लेख्छ र असफलताहरूको सङ्ख्याबाट बाहिर निस्कन्छ।

अस्थायी असफलताहरू (शेयर गरिएको सदस्यतामा HTTP 429 दर सीमा, कहिलेकाहीं
`AzureCliCredential` टोकनमा समस्या, वा टाइमआउट) स्वतः पुन: प्रयास गरिन्छ
(`-Retries`, डिफ़ल्ट 2, `-RetryDelaySeconds` पछाडि अफ समय, डिफ़ल्ट 20)। यदि
कुनै मोडेल डिप्लोयमेन्ट नियमित रूपमा 429 देखाउँछ भने, सदस्यताको GlobalStandard
TPM कोटा जाँच गर्नुहोस् (`az cognitiveservices usage list -l <region>`) — एक मात्र
डिप्लोयमेन्ट क्षमतामा वृद्धि गर्दा सहयोग हुँदैन जब *सदस्यता* कोटा समाप्त हुन्छ।

## नतिजा व्याख्या गर्दै
- `PASS` — नोटबुकले कुनै कोष्ठक त्रुटि बिना अन्त्यसम्म चल्यो।
- `FAIL` — पहिलो `*Error` / `*Exception` लाइन देखाइन्छ; सम्पूर्ण ट्रेसब्याकका लागि एउटै
  `log_*.txt` फाइल आउटपुट निर्देशिकामा खोल्नुहोस्।
- एकल नोटबुकको असफलता `-Timeout` (प्रति कोष्ठक) द्वारा सीमित हुन्छ, त्यसैले एक अड्केको
  मानवीय इन-द-लूप कोष्ठक `StdinNotImplementedError` देखाउँछ, हटेर अड्केको होइन।

## पाठहरू जसलाई अतिरिक्त स्रोतहरू चाहिन्छ (उनीहरू बिना असफल हुने अपेक्षा)
| पाठ | अतिरिक्त आवश्यकताहरू |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, कुञ्जी) — मेमोरीमा फ्यालब्याक मार्ग छ |
| 11 MCP / GitHub | GitHub MCP सर्भर + PAT |
| 13 memory (cognee) | `cognee` मोडेल प्रदायकको साथ कन्फिगर गरिएको |
| 15 browser-use | Playwright ब्राउजर स्थापना गरिएको (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + डाउनलोड गरिएको Qwen मोडेल (डिभाइसमा, कुनै क्लाउड छैन) |
| `*-dotnet-*` नोटबुकहरू | .NET Interactive कर्नेल (पूर्वनिर्धारित रूपमा बाहिर; प्रयोग गर्नुहोस् `-IncludeDotnet`) |

## प्रतिवेदन फर्काउने
पाठद्वारा समूह गरिएको PASS/FAIL तालिका सारांश गर्नुहोस्। वास्तविक
रिग्रेसनहरू (कोड/कन्फिग गल्तीहरू सुधार्ने) लाई वातावरणका खाली ठाउँहरू (अभावित Search/Foundry Local/PAT) बाट छुट्याउनुहोस्,
र प्रत्येक वास्तविक असफलताका लागि असफल `log_*.txt` लाई उद्धृत गर्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->