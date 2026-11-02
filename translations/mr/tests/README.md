# एजेंट स्मोक चाचण्या

या फोल्डरमध्ये आपण कोर्समध्ये तयार करत असलेल्या एजंटसाठी **स्मोक-टेस्ट कॅटलॉग्स** ठेवले आहेत.
स्मोक टेस्ट हा एक स्वस्त, जलद तपासणी आहे की **तैनात केलेला Microsoft Foundry होस्ट केलेला
एजंट** पोहोचण्याजोगा आहे, प्रतिसाद देत आहे, आणि त्याच्या मूलभूत प्रॉम्प्ट
अपेक्षा पाळत आहे की नाही. हा प्रथम गेट आहे — पूर्ण मूल्यमापनासाठी पर्याय नाही
पाईपलाइन जे तुम्ही [Lesson 10](../10-ai-agents-production/README.md) आणि
[Lesson 16](../16-deploying-scalable-agents/README.md) मध्ये शिकता.

कॅटलॉग्स वापरले जातात [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action द्वारे [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
वर्कफ्लो.

## कसे चालवायचे

1. **धड्याचा एजंट** Microsoft Foundry मध्ये होस्टेड एजंट म्हणून तैनात करा (तैनाती वर्कफ्लोसाठी
   Lesson 16 पहा). **एजंट नाव** आणि तुमचा **Foundry प्रोजेक्ट एंडपॉइंट** नोंद करा.
2. या रिपॉझिटरी सीक्रेट्स जोडा (Settings → Secrets and variables → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. फेडरेटेड
   ओळखीसाठी **Foundry प्रोजेक्ट स्कोप** मध्ये **Azure AI User** भूमिका आवश्यक आहे.
3. **Actions** टॅब मध्ये जा, **Smoke-test hosted agents** चालवा व धड्याचा
   `tests_file` निवडा, नंतर त्यानुसार `agent_name` आणि `project_endpoint` पुरवा.

## कॅटलॉग → धडा → एजंट नाव

| कॅटलॉग | धडा | एजंट तैनात करा |

| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro to AI Agents](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Tool Use](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Deploying Scalable Agents](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## कोणते धडे स्मोक चाचण्या आहेत?

स्मोक चाचण्या त्या धड्यांसाठी लागू होतात जिथे तुम्ही **एजंट तैनात करता**

फक्त स्थानिकपणे चालतात, किंवा अनियोजित सर्जनशील आउटपुट तयार करतात ते जाणूनबुजून वगळले आहेत:

- **Lesson 17 (Creating Local AI Agents)** संपूर्णपणे Foundry Local वापरून तुमच्या वर्कस्टेशनवर चालतो आणि

  याची पडताळणी स्थानिकपणे नोटबुक चालवून करा.
- डिझाइन-पॅटर्न आणि सिद्धांताचे धडे (02, 03, 06, 07, 09, 12) स्मोक-टेस्टसाठी एकही
  तैनात एजंट वितरीत करत नाहीत.

## कॅटलॉग स्कीमा (त्वरित संदर्भ)

प्रत्येक कॅटलॉग हा एक JSON दस्तऐवज आहे ज्यात टॉप-लेवल `tests` अ‍ॅरे असतो. प्रत्येक नोंद एक प्रम्प्ट POST करते आणि प्रत्युत्तरावर


| फील्ड | अर्थ |

| `id` | लॉगमध्ये छापले जाणारे युनिक स्टेप आयडेंटिफायर. |
| `description` | मानवीरित्या वाचण्याजोगे उद्दिष्ट. |
| `prompt` | एजंटला पाठवलेले संदेश. |
| `assertions.status` | अपेक्षित HTTP स्टेटस (डिफॉल्ट 200). |
| `assertions.contains_any` | जर प्रत्युत्तरात यापैकी कोणतीही उपस्ट्रिंग्स असतील तर पास. |
| `assertions.contains_all` | जर प्रत्युत्तरात प्रत्येक उपस्ट्रिंग असेल तर पास. |
| `assertions.contains_none` | जर प्रत्युत्तरात यापैकी कोणतीही उपस्ट्रिंग नसतील तर पास. |
| `save_response_id_as` | पुढील मल्टि-टर्न स्टेपसाठी प्रत्युत्तर आयडी साठवा. |
| `use_previous_response_id` | या टर्नमध्ये साठवलेला प्रत्युत्तर आयडी वापरून पाठवा. |

तपासण्या केस-इन्सेन्सिटिव्ह उपस्ट्रिंग तपासण्या आहेत. संपूर्ण स्कीमा, ज्यामध्ये Foundry-व्यवस्थापित संभाषण संसाधने समाविष्ट आहेत, त्यासाठी

अॅसर्शन म्हणजे केस-इन्सेन्सिटिव्ह उपस्ट्रिंग तपासण्या. पहा
[कृतीचे दस्तऐवज](https://github.com/marketplace/actions/ai-smoke-test) साठी
पूर्ण स्कीमा, ज्यामध्ये Foundry-व्यवस्थापित संभाषण संसाधने समाविष्ट आहेत.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->