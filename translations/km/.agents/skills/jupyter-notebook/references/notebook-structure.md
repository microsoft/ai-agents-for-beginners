# រចនាសម្ព័ន្ធកំណត់ត្រា

Jupyter notebooks គឺជា​ឯកសារ JSON ដែលមានរចនាសម្ព័ន្ធកម្រិតខ្លីដូចខាងក្រោម:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (បញ្ជីនៃសែល Markdown និងសែលកូដ)

When editing `.ipynb` files programmatically:

- រក្សា `nbformat` និង `nbformat_minor` ពីគំរូ។
- រក្សា `cells` ជាបញ្ជីដែលមានលំដាប់; កុំប្ដូរតម្រៀប លុះត្រាតែមានគោលបំណង។
- សម្រាប់សែលកូដ កំណត់ `execution_count` ទៅជា `null` នៅពេលមិនបានដឹង។
- សម្រាប់សែលកូដ កំណត់ `outputs` ទៅជា បញ្ជីទទេ នៅពេលរៀបចំបឋម។
- សម្រាប់សែល Markdown, រក្សា `cell_type="markdown"` និង `metadata={}`។

ចូលចិត្តប្រើការរៀបចំបឋមពីគំរូដែលភ្ជាប់មក ឬពី `new_notebook.py` (ឧទាហរណ៍, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) ជំនួសការសរសេរ JSON ដើម្បីរៀបចំ notebook ដោយដៃ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ទោះយើងខិតខំយ៉ាងដើម្បីបានភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែក្នុងប្រព័ន្ធស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកថាជាប្រភពដែលត្រឹមត្រូវ។ សម្រាប់ព័ត៌មានសំខាន់ៗ គោលណែនាំគឺឲ្យប្រើសេវាបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសៗដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->