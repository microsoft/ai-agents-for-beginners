---
name: jupyter-notebook
description: အသုံးပြုပါသည်။ အသုံးပြုသူက စမ်းသပ်မှုများ၊ ရှာဖွေမှုများ သို့မဟုတ် သင်ခန်းစာများအတွက်
  Jupyter notebook (`.ipynb`) များကို ဖန်တီးရန်၊ အခြေခံဖွဲ့စည်းရန် သို့မဟုတ် တည်းဖြတ်ရန်
  တောင်းဆိုသောအခါ အသုံးပြုပါ။ ပါထည့်ထားသော ပုံစံများကို ဦးစားပေးအသုံးပြု၍ သန့်ရှင်းစင်ကြယ်သော
  စတင်အသုံးပြုနိုင်သော notebook တစ်ခုဖန်တီးရန် helper script `new_notebook.py` ကို
  လည်ပတ်ပါ။
---
# Jupyter Notebook Skill

သန့်ရှင်းပြီး ပြန်လည်ထုတ်လုပ်နိုင်သော Jupyter notebooks များကို ရိုးရှင်းသိသာစွာ ဖန်တီးပါ — အဓိက အလုပ်ဆောင်ပုံ နှစ်မျိုးအတွက်။

- ဖြေဆိုလေ့လာမှုများနှင့် စူးစမ်းသုံးသပ်မှုပုံစံများ
- လေ့ကျင့်သင်ကြားရေးနှင့် သင်ခန်းစာအဆင့်လိုက် လမ်းညွှန်မှုများ

တူညီသော ဖွဲ့စည်းပုံနှင့် JSON မှားယွင်းမှုနည်းစေရန် အထုပ်ထဲပါရှိသည့် template များနှင့် helper script ကို မျှော်လင့်၍ အသုံးပြုပါ။

## When to use
- Create a new `.ipynb` notebook from scratch.
- Convert rough notes or scripts into a structured notebook.
- Refactor an existing notebook to be more reproducible and skimmable.
- Build experiments or tutorials that will be read or re-run by other people.

## Decision tree
- If the request is exploratory, analytical, or hypothesis-driven, choose `experiment`.
- If the request is instructional, step-by-step, or audience-specific, choose `tutorial`.
- If editing an existing notebook, treat it as a refactor: preserve intent and improve structure.

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Workflow
1. Lock the intent.
အလုပ်ရည်ရွယ်ချက်ကို သတ်မှတ်ပါ — notebook အမျိုးအစားကို `experiment` သို့မဟုတ် `tutorial` အဖြစ် မှတ်ထားပါ။ ရည်ရွယ်ချက်၊ ပရိသတ်နှင့် "ပြီးပြည့်စုံ" ဖြစ်ခြင်း၏အခြေအနေကို ဖမ်းယူပါ။

2. Scaffold from the template.
helper script ကို အသုံးပြုပြီး raw notebook JSON ကို ကိုယ်တိုင်ရေးသားရခြင်းမှ ရှောင်ရှားပါ။

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
တစ်ခုချင်းစီသော code cell ကို စည်းရုံးထားသော တစ်ဆင့်တည်းသော အလုပ်အပိုင်းအဖြစ်ထားပါ။ ရည်ရွယ်ချက်နှင့် မျှော်လင့်ထားသောရလဒ်ကို ရှင်းလင်းဖော်ပြသည့် ဆောင်းပါးကဏ္ဍများကို ထည့်ပါ။ စိတ်မကောင်းစေသော အထွတ်အထိပ် ထွက်ရှိမှုများကို ရှောင်ရှား၍ လိုအပ်လျှင် ကိုယ်စားပြု အကျဉ်းချုပ်ကို အသုံးပြုပါ။

4. Apply the right pattern.
experiments များအတွက် `references/experiment-patterns.md` ကိုလိုက်နာပါ။ tutorials များအတွက် `references/tutorial-patterns.md` ကိုလိုက်နာပါ။

5. Edit safely when working with existing notebooks.
Notebook ဖွဲ့စည်းပုံကို ထိန်းသိမ်းပါ။ အထက်မှ အောက်သို့ စဉ်ဆက်တန်းကို တိုးချဲ့ခြင်းကောင်းမွန်လာမလားဆိုသော် မဟုတ်ရင် cell များကို ပြောင်းရွှေ့ခြင်းမှ ရှောင်ကြဉ်ပါ။ ပြန်လည်ရေးသားခြင်းမပြုမီ သက်သာသော အပြောင်းအလဲများကို ဖော်ဆောင်ပါ။ raw JSON ကို တည်းဖြတ်ရမည့်အခါ `references/notebook-structure.md` ကို အရင်ကြည့်ပါ။

6. Validate the result.
ပတ်ဝန်းကျင်သည် ခွင့်ပြုပါက notebook ကို အစမှ အဆုံးထိ အလုပ်လုပ်ကြည့်ပါ။ အရေးယူ၍ စမ်းသပ်ခြင်း မဖြစ်နိုင်ပါက ထိုအခြေအနေကို သေချာ ဖော်ပြပြီး ဒေသတွင်းတွင် မည်သို့ စစ်ဆေးရမည်ကို ဖော်ပြပါ။ `references/quality-checklist.md` ပါရှိသည့် နောက်ဆုံးစစ်ဆေးစာရင်းကို အသုံးပြုပါ။

## Templates and helper script
- Templates live in `assets/experiment-template.ipynb` and `assets/tutorial-template.ipynb`.
- The helper script loads a template, updates the title cell, and writes a notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- Use `tmp/jupyter-notebook/` for intermediate files; delete when done.
- Write final artifacts under `output/jupyter-notebook/` when working in this repo.
- Use stable, descriptive filenames (for example, `ablation-temperature.ipynb`).

## Dependencies (install only when needed)
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## Environment
No required environment variables.

## Reference map
- `references/experiment-patterns.md`: experiment structure and heuristics.
- `references/tutorial-patterns.md`: tutorial structure and teaching flow.
- `references/notebook-structure.md`: notebook JSON shape and safe editing rules.
- `references/quality-checklist.md`: final validation checklist.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
သတိပေးချက်:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သည့် [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားခြင်း ဖြစ်ပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်စေရန် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါရှိနိုင်ကြောင်း မွတ်သိထားပေးပါ။ မူလစာရွက်စာတမ်းကို မူလဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အရင်းအမြစ်အဖြစ် ဆင်ခြင်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်သူအား အတည်ပြု၍ ဘာသာပြန်စေခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုပြီး ဖြစ်ပေါ်လာသော နားမလည်မှုများ သို့မဟုတ် မှားယွင်းသော အဓိပ္ပာယ်ဖော်ပြချက်များအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->