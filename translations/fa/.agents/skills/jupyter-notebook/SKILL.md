---
name: jupyter-notebook
description: زمانی استفاده شود که کاربر درخواست ایجاد، ساختاردهی یا ویرایش دفترچه‌های
  Jupyter (`.ipynb`) برای آزمایش‌ها، کاوش‌ها یا آموزش‌ها را دارد؛ از قالب‌های همراه
  ترجیحاً استفاده کنید و اسکریپت کمکی `new_notebook.py` را اجرا کنید تا یک دفترچهٔ
  آغازین تمیز تولید شود.
---
# مهارت Jupyter Notebook

دفترچه‌های Jupyter تمیز و بازتولیدپذیر برای دو حالت اصلی ایجاد کنید:

- آزمایش‌ها و تجزیه و تحلیل اکتشافی
- آموزش‌ها و راهنماهای آموزشی مرحله‌به‌مرحله

قالب‌های بسته‌بندی‌شده و اسکریپت کمکی را برای ساختار یکنواخت و کاهش خطاهای JSON ترجیح دهید.

## When to use
- یک دفترچه جدید `.ipynb` از ابتدا ایجاد کنید.
- یادداشت‌ها یا اسکریپت‌های خام را به یک دفترچه ساختارمند تبدیل کنید.
- یک دفترچه موجود را بازسازی کنید تا قابل بازتولیدتر و قابل مرور سریع‌تر باشد.
- آزمایش‌ها یا آموزش‌هایی بسازید که توسط دیگران خوانده یا دوباره اجرا شوند.

## Decision tree
- اگر درخواست اکتشافی، تحلیلی، یا مبتنی بر فرضیه است، `experiment` را انتخاب کنید.
- اگر درخواست آموزشی، مرحله‌به‌مرحله، یا ویژهٔ مخاطب است، `tutorial` را انتخاب کنید.
- اگر در حال ویرایش یک دفترچه موجود هستید، آن را به‌عنوان یک بازسازی (refactor) در نظر بگیرید: هدف را حفظ کنید و ساختار را بهبود دهید.

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Workflow
1. هدف را تثبیت کنید.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. از قالب پایه‌ای (scaffold) استفاده کنید.
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

3. دفترچه را با گام‌های کوچک و قابل اجرا پر کنید.
Keep each code cell focused on one step.
Add short markdown cells that explain the purpose and expected result.
Avoid large, noisy outputs when a short summary works.

4. الگوی مناسب را اعمال کنید.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. هنگام کار با دفترچه‌های موجود، با احتیاط ویرایش کنید.
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Prefer targeted edits over full rewrites.
If you must edit raw JSON, review `references/notebook-structure.md` first.

6. نتیجه را اعتبارسنجی کنید.
Run the notebook top-to-bottom when the environment allows.
If execution is not possible, say so explicitly and call out how to validate locally.
Use the final pass checklist in `references/quality-checklist.md`.

## Templates and helper script
- قالب‌ها در `assets/experiment-template.ipynb` و `assets/tutorial-template.ipynb` قرار دارند.
- اسکریپت کمکی یک قالب را بارگذاری می‌کند، سلول عنوان را به‌روزرسانی می‌کند، و یک دفترچه می‌نویسد.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (نصب پیش‌فرض: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- از `tmp/jupyter-notebook/` برای فایل‌های میانی استفاده کنید؛ پس از اتمام حذف کنید.
- آثار نهایی را در `output/jupyter-notebook/` بنویسید وقتی در این مخزن کار می‌کنید.
- از نام‌فایل‌های پایدار و توصیفی استفاده کنید (برای مثال، `ablation-temperature.ipynb`).

## Dependencies (install only when needed)
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## Environment
هیچ متغیر محیطی اجباری وجود ندارد.

## Reference map
- `references/experiment-patterns.md`: ساختار آزمایش و قواعد سرانگشتی.
- `references/tutorial-patterns.md`: ساختار آموزش و جریان تدریس.
- `references/notebook-structure.md`: شکل JSON دفترچه و قوانین ویرایش ایمن.
- `references/quality-checklist.md`: چک‌لیست اعتبارسنجی نهایی.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
سلب مسئولیت:
این سند با استفاده از سرویس ترجمهٔ مبتنی بر هوش مصنوعی Co-op Translator (https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. نسخهٔ اصلی سند به زبان مادری‌اش باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمهٔ حرفه‌ای انسانی توصیه می‌شود. ما در قبال هر گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->