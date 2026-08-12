---
name: jupyter-notebook
description: प्रयोगकर्ताले प्रयोग, अन्वेषण, वा ट्युटोरियलका लागि Jupyter नोटबुकहरू
  (`.ipynb`) बनाउन, ढाँचा तयार गर्न, वा सम्पादन गर्न अनुरोध गरेमा प्रयोग गर्नुहोस्;
  समावेश गरिएको टेम्प्लेटलाई प्राथमिकता दिनुहोस् र सफा सुरुवाती नोटबुक उत्पन्न गर्न
  सहायक स्क्रिप्ट `new_notebook.py` चलाउनुहोस्।
---
# Jupyter नोटबुक सीप

Create clean, reproducible Jupyter notebooks for two primary modes:

- प्रयोगहरू र अन्वेषणात्मक विश्लेषण
- ट्युटोरियलहरू र शिक्षण-उन्मुख चरण-द्वारा-चरण मार्गदर्शनहरू

Prefer the bundled templates and the helper script for consistent structure and fewer JSON mistakes.

## कहिले प्रयोग गर्ने
- सुरुबाट नयाँ `.ipynb` नोटबुक सिर्जना गर्नुहोस्.
- कच्चा नोटहरू वा स्क्रिप्टहरूलाई संरचित नोटबुकमा रूपान्तरण गर्नुहोस्.
- अवस्थित नोटबुकलाई पुन: संरचना गरी ज्यादा पुनरुत्पादनयोग्य र छिटो स्क्यान गर्न मिल्ने बनाउनुहोस्.
- अरूले पढ्ने वा फेरि चलाउने प्रकारका प्रयोग वा ट्युटोरियलहरू तयार गर्नुहोस्.

## निर्णय वृक्ष
- यदि अनुरोध अन्वेषणात्मक, विश्लेषणात्मक, वा परिकल्पना-प्रेरित छ भने, `experiment` छान्नुहोस्.
- यदि अनुरोध निर्देशात्मक, चरण-दर-चरण, वा लक्षित दर्शक-विशेष छ भने, `tutorial` छान्नुहोस्.
- अवस्थित नोटबुक सम्पादन गर्दा, यसलाई पुनर्रचना (refactor) जस्तै मान्नुहोस्: उद्देश्य संरक्षण गर्नुहोस् र संरचना सुधार गर्नुहोस्.

## सीप पथ (एक पटक सेट गर्नुहोस्)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## कार्यप्रवाह
1. इरादा निश्चित गर्नुहोस्.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. टेम्पलेटबाट संरचना तयार गर्नुहोस्.
Use the helper script to avoid hand-authoring raw notebook JSON.

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

3. नोटबुकलाई साना, चलाउन मिल्ने चरणहरूले भर्नुहोस्.
Keep each code cell focused on one step.
Add short markdown cells that explain the purpose and expected result.
ठूला, अनावश्यक आउटपुटहरूबाट बच्नुहोस् जब छोटो सारांश काम गर्छ।

4. सही ढाँचा प्रयोग गर्नुहोस्.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. अवस्थित नोटबुकहरूमा काम गर्दा सुरक्षित रूपमा सम्पादन गर्नुहोस्.
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Prefer targeted edits over full rewrites.
If you must edit raw JSON, review `references/notebook-structure.md` first.

6. परिणाम प्रमाणित गर्नुहोस्.
Run the notebook top-to-bottom when the environment allows.
If execution is not possible, say so explicitly and call out how to validate locally.
Use the final pass checklist in `references/quality-checklist.md`.

## टेम्पलेटहरू र हेल्पर स्क्रिप्ट
- टेम्पलेटहरू `assets/experiment-template.ipynb` र `assets/tutorial-template.ipynb` मा रहन्छन्.
- हेल्पर स्क्रिप्टले टेम्पलेट लोड गर्छ, शीर्षक सेल अपडेट गर्छ, र नोटबुक लेख्छ।

स्क्रिप्ट पथ:
- `$JUPYTER_NOTEBOOK_CLI` (स्थापित डिफल्ट: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## अस्थायी र आउटपुट कन्वेन्सन
- मध्यवर्ती फाइलहरूको लागि `tmp/jupyter-notebook/` प्रयोग गर्नुहोस्; सकिएपछि मेटाउनुहोस्.
- यस रिपोमा काम गर्दा अन्तिम वस्तुहरू `output/jupyter-notebook/` मा लेख्नुहोस्.
- स्थिर, वर्णनात्मक फाइलनामहरू प्रयोग गर्नुहोस् (उदाहरणका लागि, `ablation-temperature.ipynb`).

## निर्भरता (आवश्यक परे मात्र स्थापना गर्नुहोस्)
`uv` लाई निर्भरता व्यवस्थापनका लागि प्राथमिकता दिनुहोस्.

स्थानीय नोटबुक कार्यान्वयनका लागि वैकल्पिक Python प्याकेजहरू:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## वातावरण
कुनै आवश्यक वातावरणीय चरहरू छैनन्।

## सन्दर्भ नक्शा
- `references/experiment-patterns.md`: प्रयोग संरचना र ह्युरिस्टिकहरू.
- `references/tutorial-patterns.md`: ट्युटोरियल संरचना र शिक्षणको प्रवाह.
- `references/notebook-structure.md`: नोटबुक JSON आकार र सुरक्षित सम्पादन नियमहरू.
- `references/quality-checklist.md`: अन्तिम प्रमाणीकरण जाँचसूची.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यो दस्तावेज AI अनुवाद सेवा Co-op Translator (https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेजलाई यसको मूल भाषामा नै आधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->