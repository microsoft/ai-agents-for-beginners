# नोटबुक संरचना

Jupyter नोटबुक हे खालील उच्च-स्तरीय स्वरूपाचे JSON दस्तऐवज असतात:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (a list of markdown and code cells)

When editing `.ipynb` files programmatically:

- टेम्पलेटमधून `nbformat` आणि `nbformat_minor` जपून ठेवा.
- `cells` क्रमबद्ध यादी म्हणून ठेवा; हेतुपुरस्सर नसल्यास त्यांचे क्रम बदलू नका.
- कोड सेल्ससाठी, अज्ञात असल्यास `execution_count` ची किंमत `null` असे सेट करा.
- कोड सेल्ससाठी, स्कॅफोल्डिंग करताना `outputs` रिकामी यादी म्हणून सेट करा.
- Markdown सेल्ससाठी, `cell_type="markdown"` आणि `metadata={}` असे ठेवा.

हाताने कच्चे नोटबुक JSON तयार करण्याऐवजी बंडल केलेल्या टेम्पलेट्समधून किंवा `new_notebook.py` (उदा., `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) मधून स्कॅफोल्डिंग करणे प्राधान्य द्या.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
हे दस्तऐवज AI अनुवाद सेवा Co-op Translator (https://github.com/Azure/co-op-translator) वापरून अनुवादित केले गेले आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत म्हणून मानला जावा. महत्त्वाच्या माहितीच्या बाबतीत व्यावसायिक मानवी अनुवाद शिफारस केला जातो. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थनिर्देशांबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->