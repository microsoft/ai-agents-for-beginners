---
name: jupyter-notebook
description: ប្រើនៅពេលដែលអ្នកប្រើស្នើឲ្យបង្កើត រៀបចំ (scaffold) ឬកែសម្រួល Jupyter
  notebooks (`.ipynb`) សម្រាប់សាកល្បង ស្វែងរក ឬមេរៀន; អនុសាសន៍ឲ្យប្រើទំរង់គំរូដែលភ្ជាប់មកជាមួយ
  និងរត់ស្គ្រីបជំនួយ `new_notebook.py` ដើម្បីបង្កើតសៀវភៅចាប់ផ្តើមដែលស្អាត។
---
# ជំនាញ Jupyter Notebook

បង្កើតកំណត់ត្រា Jupyter ដែលស្អាត និងអាចសែតឡើងវិញសម្រាប់របៀបធ្វើការចម្បងពីរការ៖

- ការសាកល្បង និងវិភាគស្វែងរក
- មេរៀន និងដំណើរការណែនាំសម្រាប់បង្រៀន

ផ្តល់អាទិភាពដល់ទំរង់ដែលភ្ជាប់មក និងស្គ្រីបជំនួយសម្រាប់រចនាសម្ព័ន្ធមានតុល្យភាព និងកំហុស JSON តិចជាង។

## ពេលណាដែលត្រូវប្រើ
- បង្កើតកំណត់ត្រាថ្មី `.ipynb` ពីចន្លោះសូន្យ។
- បម្លែងកំណត់សម្គាល់មាំមួនឬស្គ្រីបទៅជាកំណត់ត្រាមានរចនាសម្ព័ន្ធ។
- ប្ដូររៀបចំកំណត់ត្រាដែលមានស្រាប់ ដើម្បីឲ្យអាចអង្កកឡើងវិញបាន និងអានបានយ៉ាងស្រួល។
- ស្ថាបនាការសាកល្បងឬមេរៀនដែលនឹងត្រូវបានអាន ឬអនុវត្តឡើងវិញដោយមនុស្សផ្សេងទៀត។

## ដំណើរការសម្រេចចិត្ត
- បើសំណើមានលក្ខណៈស្វែងរក វិភាគ ឬដឹកនាំដោយសន្មត់ យក `experiment`។
- បើសំណើមានលក្ខណៈបណ្តុះបណ្តាល ជាជំហានៗ ឬផ្តោតលើប្រិយមិត្ត យក `tutorial`។
- បើកំពុងកែសម្រួលកំណត់ត្រាដែលមានស្រាប់ សូមប្រព្រឹត្តទៅដូចជា refactor: រក្សាចេតនា និងធ្វើឱ្យរចនាសម្ព័ន្ធប្រសើរឡើង។

## គន្លងជំនាញ (កំណត់ម្តង)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## ដំណើរការ
1. កំណត់គោលបំណង.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. ដាក់ស៊្គេឡេតពីទំរង់.
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

3. បំពេញកំណត់ត្រាទៅដោយជំហានតូចៗដែលអាចរត់បាន.
រក្សាឲ្យប្រអប់កូដមួយនីមួយៗផ្ដោតលើជំហានតែមួយ។
បន្ថែមកោសិកាតំណភាសាខ្លីៗដែលពន្យល់ពីគោលដៅ និងលទ្ធផលរំពឹងទុក។
ជៀសវាងលទ្ធផលធំៗដែលមានសំឡេងពុម្ពពិសេសពេលដែលសេចក្តីសង្ខេបខ្លីគ្រាន់គឺបានជួយ។

4. អនុវត្តលំនាំត្រឹមត្រូវ។
សម្រាប់ការសាកល្បង, អនុយោគទៅ `references/experiment-patterns.md`។
សម្រាប់មេរៀន, អនុយោគទៅ `references/tutorial-patterns.md`។

5. កែសម្រួលយ៉ាងមានសុវត្ថិភាពเมื่อធ្វើការជាមួយកំណត់ត្រាដែលមានស្រាប់។
រក្សាសម្ព័ន្ធកំណត់ត្រា; ជៀសវាងការប្តូរលំដាប់កូសិកុំនៅពេលដែលវាមិនធ្វើឱ្យរឿងរ៉ាវពីលើទៅក្រោមប្រសើរឡើយ។
ផ្ដល់អាទិភាពចំពោះការកែប្រែចំណុចជាក់លាក់ជាងការសរសេរឡើងវិញទាំងមូល។
បើអ្នកចាំបាច់ត្រូវកែ JSON ដើម សូមពិនិត្យ `references/notebook-structure.md` មុន។

6. ផ្ទៀងផ្ទាត់លទ្ធផល។
រត់កំណត់ត្រាពីលើទៅក្រោមនៅពេលដែលបរិស្ថានអនុញ្ញាត។
បើមិនអាចអនុវត្តបាន សូមប្រាប់យ៉ាងច្បាស់ ហើយបង្ហាញវិធីធ្វើផ្ទៀងផ្ទាត់ក្នុងកម្រិតតំបន់។
ប្រើបញ្ជីពិនិត្យលើកចុងក្រោយនៅក្នុង `references/quality-checklist.md`។

## ទម្រង់និងស្គ្រីបជំនួយ
- ទម្រង់រស់នៅក្នុង `assets/experiment-template.ipynb` និង `assets/tutorial-template.ipynb`។
- ស្គ្រីបជំនួយនឹងបង្ហាញទំរង់មួយ អាប់ដេតកោសិកា​ចំណងជើង និងសរសេរកំណត់ត្រាមួយ។

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## ការកំណត់ថតបណ្ដោះអាសន្ន និងលទ្ធផល
- ប្រើ `tmp/jupyter-notebook/` សម្រាប់ឯកសាររវល់; លុបវាយេលប់រួច។
- សរសេររឿងសិល្បៈចុងក្រោយក្រោម `output/jupyter-notebook/` នៅពេលធ្វើការ​នៅក្នុងឃ្លាំងនេះ។
- ប្រើឈ្មោះឯកសារដែលមានស្ថិតិភាព និងពិពណ៌នា (ឧទាហរណ៍, `ablation-temperature.ipynb`)។

## ពឹងផ្អែក (ដំឡើងតែពេលចាំបាច់)
ផ្តល់អាទិភាពចំពោះ `uv` សម្រាប់ការគ្រប់គ្រងការពឹងផ្អែក។

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## បរិយាកាស
គ្មានអថេរបរិយាកាសចាំបាច់។

## ផែនទីយោង
- `references/experiment-patterns.md`: រចនាសម្ព័ន្ធនៃការសាកល្បង និងការណែនាំវិធីសាស្ត្រ។
- `references/tutorial-patterns.md`: រចនាសម្ព័ន្ធមេរៀន និងលំហាត់នៃការបង្រៀន។
- `references/notebook-structure.md`: រូបរាង JSON នៃកំណត់ត្រា និងច្បាប់កែសម្រួលយ៉ាងមានសុវត្ថិភាព។
- `references/quality-checklist.md`: បញ្ជីពិនិត្យផ្ទៀងផ្ទាត់ចុងក្រោយ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធទំនួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំស្វែងរកភាពត្រឹមត្រូវ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិសាច់សោអាចមានកំហុស ឬមិនត្រឹមត្រូវបាន។ ឯកសារដើមក្នុងភាសាម្ចាស់គួរត្រូវបានទទួលស្គាល់ថាជាដើមទុនដែលមានអំណាចដាក់សេចក្តីបញ្ជាក់។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងសូមណែនាំឲ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->