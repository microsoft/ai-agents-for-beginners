# नोटबुक संरचना

Jupyter नोटबुक इस उच्च-स्तरीय रूपरेखा वाले JSON दस्तावेज़ होते हैं:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (a list of markdown and code cells)

When editing `.ipynb` files programmatically:

- टेम्पलेट से `nbformat` और `nbformat_minor` को संरक्षित रखें।
- `cells` को एक क्रमबद्ध सूची के रूप में रखें; जब तक इरादा न हो, पुनःक्रमित न करें।
- कोड सेल्स के लिए, अज्ञात होने पर `execution_count` को `null` पर सेट करें।
- कोड सेल्स के लिए, स्कैफ़ोल्डिंग करते समय `outputs` को एक खाली सूची पर सेट करें।
- मार्कडाउन सेल्स के लिए, `cell_type="markdown"` और `metadata={}` रखें।

Prefer scaffolding from the bundled templates or `new_notebook.py` (for example, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) instead of hand-authoring raw notebook JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल भाषा में उपलब्ध दस्तावेज़ को अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->