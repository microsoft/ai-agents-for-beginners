---
name: jupyter-notebook
description: वापरा जेव्हा वापरकर्ता प्रयोग, अन्वेषण किंवा ट्यूटोरियलसाठी Jupyter नोटबुक्स
  (`.ipynb`) तयार करण्यास, स्कॅफोल्ड करण्यास किंवा संपादित करण्यास विचारतो; बंडल केलेल्या
  टेम्पलेट्सना प्राधान्य द्या आणि स्वच्छ प्रारंभिक नोटबुक तयार करण्यासाठी सहाय्यक
  स्क्रिप्ट `new_notebook.py` चालवा.
---
# Jupyter Notebook कौशल्य

स्वच्छ, पुन्हा निर्माणयोग्य Jupyter नोटबुक दोन प्रमुख मोडसाठी तयार करा:

- प्रयोग आणि अन्वेषणात्मक विश्लेषण
- ट्यूटोरियल आणि शिक्षण-केंद्रित मार्गदर्शने

सुसंगत संरचना आणि कमी JSON चुका यासाठी बंडल केलेल्या टेम्पलेट्स आणि सहाय्यक स्क्रिप्ट पसंत करा.

## कधी वापरावे
- शून्यावरून नवीन `.ipynb` नोटबुक तयार करा.
- अमुक टिपण्या किंवा स्क्रिप्ट संरचित नोटबुकमध्ये बदला.
- विद्यमान नोटबुक रीफॅक्टर करा जेणेकरून ते अधिक पुनरुत्पादनीय आणि स्किम करण्यायोग्य होईल.
- असे प्रयोग किंवा ट्यूटोरियल तयार करा जे इतर लोक वाचतील किंवा पुन्हा चालवतील.

## निर्णय वृक्ष
- विनंती अन्वेषणात्मक, विश्लेषणात्मक, किंवा संकल्पनाधारित असल्यास, `experiment` निवडा.
- विनंती मार्गदर्शक, पायरी-दर-पायरी, किंवा विशिष्ट प्रेक्षकांसाठी असल्यास, `tutorial` निवडा.
- विद्यमान नोटबुक संपादित करत असल्यास, ते रीफॅक्टर म्हणून हाताळा: हेतू जतन करा आणि संरचना सुधारित करा.

## कौशल्य मार्ग (एकदा सेट करा)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## कार्यप्रवाह
1. Lock the intent.
ओळख करा नोटबुक प्रकार: `experiment` किंवा `tutorial`.
उद्दिष्ट, प्रेक्षक, आणि "पूर्ण" कसा दिसतो हे टिपा.

2. Scaffold from the template.
सहाय्यक स्क्रिप्ट वापरा ज्यामुळे कच्चे नोटबुक JSON हातांनी तयार करण्याची गरज पडणार नाही.

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
प्रत्येक कोड सेल एका पावलावर लक्ष केंद्रित करावा.
लघु मार्कडाउन सेल जोडा जे उद्देश आणि अपेक्षित परिणाम स्पष्ट करतात.
जेव्हा लहान सारांश चालतो तेव्हा मोठ्या, गोंधळीत आउटपुट टाळा.

4. Apply the right pattern.
प्रयोगांसाठी, `references/experiment-patterns.md` चा अवलंब करा.
ट्यूटोरियलसाठी, `references/tutorial-patterns.md` चा अवलंब करा.

5. Edit safely when working with existing notebooks.
नोटबुकची रचना जतन करा; वरून खालीपर्यंतच्या कथेनं सुधारणा होत नसेल तर सेल्सचे पुनर्रचना टाळा.
पूर्ण पुनर्लेखनापेक्षा लक्षित संपादनांना प्राधान्य द्या.
जर आपल्याला कच्चे JSON संपादित करावे लागले तर आधी `references/notebook-structure.md` पाहा.

6. Validate the result.
पर्यावरण परवानगी देत असल्यास नोटबुक वरून खाली चालवा.
जर अंमलबजावणी शक्य नसेल तर ते स्पष्टपणे सांगा आणि स्थानिकरित्या कसे पडताळायचे ते नमूद करा.
`references/quality-checklist.md` मधील अंतिम तपासणी यादी वापरा.

## Templates and helper script
- Templates live in `assets/experiment-template.ipynb` and `assets/tutorial-template.ipynb`.
- सहाय्यक स्क्रिप्ट एक टेम्पलेट लोड करते, शीर्षक सेल अद्ययावत करते, आणि नोटबुक लिहिते.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- Use `tmp/jupyter-notebook/` for intermediate files; delete when done.
- Write final artifacts under `output/jupyter-notebook/` when working in this repo.
- स्थिर, वर्णनात्मक फाइलनेम वापरा (उदाहरणार्थ, `ablation-temperature.ipynb`).

## Dependencies (install only when needed)
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

बंडल केलेली scaffold स्क्रिप्ट फक्त Python स्टँडर्ड लायब्ररी वापरते आणि अतिरिक्त अवलंबित्वांची आवश्यकता नाही.

## पर्यावरण
कोणतीही आवश्यक पर्यावरण चल नाहीत.

## संदर्भ नकाशा
- `references/experiment-patterns.md`: प्रयोगांची रचना आणि अनुभवजन्य नियम.
- `references/tutorial-patterns.md`: ट्यूटोरियलची रचना आणि शिक्षण प्रवाह.
- `references/notebook-structure.md`: नोटबुक JSON चे स्वरूप आणि सुरक्षित संपादन नियम.
- `references/quality-checklist.md`: अंतिम पडताळणी तपासणी यादी.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला गेला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी आढळू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत म्हणून मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुतींबद्दल किंवा चुकीच्या अर्थ लावण्याबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->