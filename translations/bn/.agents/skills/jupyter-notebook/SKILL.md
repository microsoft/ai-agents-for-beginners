---
name: jupyter-notebook
description: ব্যবহার করুন যখন ব্যবহারকারী পরীক্ষার, অনুসন্ধানের, বা টিউটোরিয়ালের
  জন্য Jupyter নোটবুকগুলি (`.ipynb`) তৈরি, স্ক্যাফোল্ড, বা সম্পাদনার অনুরোধ করে; বান্ডিলকৃত
  টেমপ্লেটগুলিকে অগ্রাধিকার দিন এবং একটি পরিষ্কার সূচনা নোটবুক তৈরি করার জন্য সহায়ক
  স্ক্রিপ্ট `new_notebook.py` চালান।
---
# Jupyter Notebook দক্ষতা

Create clean, reproducible Jupyter notebooks for two primary modes:

- পরীক্ষণ এবং অন্বেষণাত্মক বিশ্লেষণ
- টিউটোরিয়াল এবং শিক্ষামূলক ধাপে-ধাপে নির্দেশিকা

Prefer the bundled templates and the helper script for consistent structure and fewer JSON mistakes.

## When to use
- নতুন `.ipynb` নোটবুক শূন্য থেকে তৈরি করুন।
- খসড়া নোট বা স্ক্রিপ্টকে একটি সংগঠিত নোটবুক-এ রূপান্তর করুন।
- একটি বিদ্যমান নোটবুককে আরো পুনরুত্পাদনযোগ্য এবং সহজে স্কিম করা যায় এমনভাবে রিফ্যাক্টর করুন।
- অন্যান্য মানুষ পড়বে বা পুনরায় চালাবে এমন পরীক্ষাগুলো বা টিউটোরিয়াল তৈরি করুন।

## Decision tree
- If the request is exploratory, analytical, or hypothesis-driven, choose `experiment`.
- If the request is instructional, step-by-step, or audience-specific, choose `tutorial`.
- If editing an existing notebook, treat it as a refactor: preserve intent and improve structure.

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

ব্যবহারকারী-স্কোপড স্কিলস `$CODEX_HOME/skills`-এর নিচে ইনস্টল হয় (ডিফল্ট: `~/.codex/skills`)।

## Workflow
1. উদ্দেশ্য নিশ্চিত করুন।
Identify the notebook kind: `experiment` or `tutorial`.
উদ্দেশ্য, শ্রোতা, এবং কীভাবে "done" দেখতে হবে তা নির্ধারণ করুন।

2. টেমপ্লেট থেকে স্ক্যাফোল্ড তৈরি করুন।
রো নোটবুক JSON হাতে লিখে ত্রুটি এড়াতে সহায়ক স্ক্রিপ্ট ব্যবহার করুন।

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

3. নোটবুকটি ছোট, চালনাযোগ্য ধাপ দিয়ে পূরণ করুন।
প্রতিটি কোড সেলকে একটি ধাপে কেন্দ্রিত রাখুন।
উদ্দেশ্য এবং প্রত্যাশিত ফলাফল ব্যাখ্যা করে সংক্ষিপ্ত Markdown সেল যোগ করুন।
সংক্ষিপ্ত সারাংশ কাজ করলে বড়, গোলমালপূর্ণ আউটপুট এড়িয়ে চলুন।

4. সঠিক প্যাটার্ন প্রয়োগ করুন।
পরীক্ষার জন্য, `references/experiment-patterns.md` অনুসরণ করুন।
টিউটোরিয়ালগুলোর জন্য, `references/tutorial-patterns.md` অনুসরণ করুন।

5. বিদ্যমান নোটবুকের সাথে কাজ করার সময় নিরাপদে সম্পাদনা করুন।
নোটবুকের কাঠামো বজায় রাখুন; সেলগুলোর পুনরায় ক্রমবিন্যাস এড়িয়ে চলুন যদি না এটি উপরে-থেকে-নিচে কাহিনী উন্নত করে।
পূর্ণ রিরাইটের চেয়ে লক্ষ্যিত সম্পাদনাগুলিকে অগ্রাধিকার দিন।
যদি আপনাকে কাঁচা JSON সম্পাদনা করতে হয়, আগে `references/notebook-structure.md` দেখুন।

6. ফলাফল যাচাই করুন।
পরিবেশ অনুমতি দিলে নোটবুকটি উপরের থেকে নিচ পর্যন্ত চালান।
যদি এক্সিকিউশন সম্ভব না হয়, স্পষ্টভাবে বলুন এবং স্থানীয়ভাবে কীভাবে যাচাই করবেন তা উল্লেখ করুন।
চূড়ান্ত পাস চেকলিস্ট `references/quality-checklist.md` ব্যবহার করুন।

## Templates and helper script
- টেমপ্লেটগুলো রয়েছে `assets/experiment-template.ipynb` এবং `assets/tutorial-template.ipynb` এ।
- সহায়ক স্ক্রিপ্ট একটি টেমপ্লেট লোড করে, টাইটেল সেল আপডেট করে, এবং একটি নোটবুক লেখে।

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (ইনস্টল করা ডিফল্ট: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- মধ্যবর্তী ফাইলগুলোর জন্য `tmp/jupyter-notebook/` ব্যবহার করুন; কাজ শেষে মুছে ফেলুন।
- এই রিপোতে কাজ করার সময় চূড়ান্ত আর্টিফ্যাক্টগুলো `output/jupyter-notebook/`-এর অধীনে লিখুন।
- স্থিতিশীল, বর্ণনামূলক ফাইলনেম ব্যবহার করুন (উদাহরণস্বরূপ, `ablation-temperature.ipynb`)।

## Dependencies (install only when needed)
নির্ভরশীলতা পরিচালনার জন্য `uv`-কে অগ্রাধিকার দিন।

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## Environment
No required environment variables.

## Reference map
- `references/experiment-patterns.md`: পরীক্ষার কাঠামো এবং হিউরিস্টিকস।
- `references/tutorial-patterns.md`: টিউটোরিয়ালের কাঠামো এবং শিক্ষাদানের প্রবাহ।
- `references/notebook-structure.md`: নোটবুকের JSON আকৃতি এবং নিরাপদ সম্পাদনার নিয়ম।
- `references/quality-checklist.md`: চূড়ান্ত যাচাই চেকলিস্ট।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
অস্বীকৃতি:
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতার চেষ্টা করি, তবু স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজ ভাষায়ই কর্তৃপক্ষভিত্তিক উৎস হিসেবে বিবেচিত হওয়া উচিত। অত্যন্ত গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে উদ্ভূত কোনো ভুলবোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->