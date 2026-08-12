---
name: jupyter-notebook
description: उपयोग तब करें जब उपयोगकर्ता प्रयोगों, खोजों, या ट्यूटोरियल्स के लिए Jupyter
  नोटबुक (`.ipynb`) बनाने, स्कैफोल्ड करने, या संपादित करने के लिए कहे; पैकेज किए गए
  टेम्पलेट्स को प्राथमिकता दें और एक साफ शुरुआत वाला नोटबुक बनाने के लिए सहायक स्क्रिप्ट
  `new_notebook.py` चलाएँ।
---
# Jupyter Notebook Skill

दो मुख्य मोड के लिए साफ़, पुनरुत्पादनीय Jupyter नोटबुक बनाएं:

- प्रयोग और अन्वेषणात्मक विश्लेषण
- ट्यूटोरियल और शिक्षण-उन्मुख विस्तृत मार्गदर्शिकाएँ

सुसंगत संरचना और कम JSON त्रुटियों के लिए बने-बंडल किए गए टेम्पलेट और हेल्पर स्क्रिप्ट का उपयोग करें।

## When to use
- एक नया `.ipynb` नोटबुक शून्य से बनाएं।
- असंरचित नोट्स या स्क्रिप्ट को संरचित नोटबुक में परिवर्तित करें।
- मौजूदा नोटबुक को अधिक पुनरुत्पादनीय और आसानी से स्किम करने योग्य बनाने के लिए रीफैक्टर करें।
- ऐसे प्रयोग या ट्यूटोरियल बनाएं जिन्हें अन्य लोग पढ़ेंगे या फिर से चलाएंगे।

## Decision tree
- यदि अनुरोध अन्वेक्षात्मक, विश्लेषणात्मक, या परिकल्पना-प्रधान है, तो `experiment` चुनें।
- यदि अनुरोध निर्देशात्मक, चरण-दर-चरण, या दर्शक-विशेष है, तो `tutorial` चुनें।
- यदि किसी मौजूदा नोटबुक को संपादित किया जा रहा है, तो इसे रीफैक्टर के रूप में मानें: उद्देश्य बनाए रखें और संरचना में सुधार करें।

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

यूज़र-स्कोप्ड स्किल्स `$CODEX_HOME/skills` के तहत इंस्टॉल होती हैं (डिफ़ॉल्ट: `~/.codex/skills`)।

## Workflow
1. Lock the intent.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. Scaffold from the template.
टेम्पलेट से ढाँचा तैयार करें।
हैंड-ऑथरिंग के बजाय हेल्पर स्क्रिप्ट का उपयोग करें ताकि कच्चे नोटबुक JSON में गलतियाँ न हों।

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. Fill the notebook with small, runnable steps.
नोटबुक को छोटे, चलने योग्य चरणों से भरें।
प्रत्येक कोड सेल को एक चरण पर केंद्रित रखें।
छोटे markdown सेल जोड़ें जो उद्देश्य और अपेक्षित परिणाम बताते हों।
जब संक्षेप पर्याप्त हो तो बड़े, शोर वाले आउटपुट से बचें।

4. Apply the right pattern.
प्रयोगों के लिए, `references/experiment-patterns.md` का पालन करें।
ट्यूटोरियल के लिए, `references/tutorial-patterns.md` का पालन करें।

5. Edit safely when working with existing notebooks.
मौजूदा नोटबुक पर काम करते समय सुरक्षित रूप से संपादित करें।
नोटबुक संरचना बनाए रखें; कोशिकाओं को फिर से क्रमबद्ध करने से बचें जब तक कि यह ऊपर से नीचे की कहानी में सुधार न करे।
पूरी तरह से पुनर्लेखन के बजाय लक्षित संपादनों को प्राथमिकता दें।
यदि आपको कच्चे JSON को संपादित करना अनिवार्य है, तो पहले `references/notebook-structure.md` की समीक्षा करें।

6. Validate the result.
परिणाम को सत्यापित करें।
जब पर्यावरण अनुमति दे तब नोटबुक को ऊपर से नीचे तक चलाएं।
यदि निष्पादन संभव नहीं है, तो इसे स्पष्ट रूप से बताएं और लोकल रूप से सत्यापित करने का तरीका बताएं।
अंतिम जाँच सूची के रूप में `references/quality-checklist.md` का उपयोग करें।

## Templates and helper script
- टेम्पलेट्स `assets/experiment-template.ipynb` और `assets/tutorial-template.ipynb` में स्थित हैं।
- हेल्पर स्क्रिप्ट एक टेम्पलेट लोड करती है, शीर्षक सेल अपडेट करती है, और एक नोटबुक लिखती है।

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (स्थापित डिफ़ॉल्ट: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- मध्यवर्ती फ़ाइलों के लिए `tmp/jupyter-notebook/` का उपयोग करें; काम खत्म होने पर हटाएँ।
- इस रिपॉज़िटरी में काम करते समय अंतिम आर्टिफ़ैक्ट्स `output/jupyter-notebook/` के अंतर्गत लिखें।
- स्थिर, वर्णनात्मक फ़ाइलनामों का उपयोग करें (उदाहरण के लिए, `ablation-temperature.ipynb`)।

## Dependencies (install only when needed)
निर्भरता (आवश्यक होने पर ही इंस्टॉल करें)

Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

बंडल किया गया स्कैफ़ोल्ड स्क्रिप्ट केवल Python मानक लाइब्रेरी का उपयोग करती है और अतिरिक्त निर्भरताओं की आवश्यकता नहीं है।

## Environment
कोई आवश्यक पर्यावरण चर नहीं हैं।

## Reference map
- `references/experiment-patterns.md`: प्रयोग की संरचना और अनुभवजन्य नियम।
- `references/tutorial-patterns.md`: ट्यूटोरियल की संरचना और शिक्षण प्रवाह।
- `references/notebook-structure.md`: नोटबुक JSON संरचना और सुरक्षित संपादन नियम।
- `references/quality-checklist.md`: अंतिम सत्यापन चेकलिस्ट।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यह दस्तावेज़ AI अनुवाद सेवा Co-op Translator (https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। हालाँकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में मौज़ूद मूल दस्तावेज़ को अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->