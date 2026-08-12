---
name: jupyter-notebook
description: Използвайте, когато потребителят иска да създаде, да изгради основна
  структура за или да редактира Jupyter тетрадки (`.ipynb`) за експерименти, изследвания
  или уроци; предпочитайте вградените шаблони и стартирайте помощния скрипт `new_notebook.py`,
  за да генерирате чист начален файл на тетрадка.
---
# Умение за Jupyter Notebook

Създавайте чисти, възпроизводими Jupyter бележници за два основни режима:

- Експерименти и изследователски анализ
- Уроци и ръководства, ориентирани към обучение

Предпочитайте вградените шаблони и помощния скрипт за последователна структура и по-малко грешки в JSON.

## Кога да използвате
- Създайте нов `.ipynb` бележник от нулата.
- Конвертирайте неполни бележки или скриптове в структуриран бележник.
- Рефакторирайте съществуващ бележник, за да бъде по-възпроизводим и лесен за преглед.
- Създавайте експерименти или уроци, които ще бъдат прочетени или преизпълнени от други хора.

## Дърво на решенията
- Ако заявката е изследователска, аналитична или хипотетично-ориентирана, изберете `experiment`.
- Ако заявката е инструктивна, стъпка по стъпка или насочена към конкретна аудитория, изберете `tutorial`.
- Ако редактирате съществуващ бележник, третирайте го като рефакториране: запазете намерението и подобрете структурата.

## Път на умението (за настройка веднъж)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Потребителските умения се инсталират под `$CODEX_HOME/skills` (по подразбиране: `~/.codex/skills`).

## Работен процес
1. Lock the intent.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. Scaffold from the template.
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

3. Fill the notebook with small, runnable steps.
Keep each code cell focused on one step.
Add short markdown cells that explain the purpose and expected result.
Avoid large, noisy outputs when a short summary works.

4. Apply the right pattern.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. Edit safely when working with existing notebooks.
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Prefer targeted edits over full rewrites.
If you must edit raw JSON, review `references/notebook-structure.md` first.

6. Validate the result.
Run the notebook top-to-bottom when the environment allows.
If execution is not possible, say so explicitly and call out how to validate locally.
Use the final pass checklist in `references/quality-checklist.md`.

## Шаблони и помощен скрипт
- Шаблоните се намират в `assets/experiment-template.ipynb` и `assets/tutorial-template.ipynb`.
- Помощният скрипт зарежда шаблон, обновява заглавната клетка и записва бележник.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Конвенции за временни и изходни файлове
- Използвайте `tmp/jupyter-notebook/` за междинни файлове; изтрийте след приключване.
- Записвайте финалните артефакти под `output/jupyter-notebook/`, когато работите в това repo.
- Използвайте стабилни, описателни имена на файлове (например, `ablation-temperature.ipynb`).

## Зависимости (инсталирайте само при необходимост)
Предпочитайте `uv` за управление на зависимости.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## Среда
Не са необходими променливи на средата.

## Справочна карта
- `references/experiment-patterns.md`: структура на експеримента и евристики.
- `references/tutorial-patterns.md`: структура на урока и поток на обучение.
- `references/notebook-structure.md`: формат на notebook JSON и правила за безопасно редактиране.
- `references/quality-checklist.md`: контролен списък за финална проверка.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Отказ от отговорност:

Този документ е преведен с помощта на услуга за превод с изкуствен интелект [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на оригиналния език трябва да се счита за авторитетен източник. За критична информация препоръчваме професионален превод от квалифициран човешки преводач. Не носим отговорност за каквито и да е недоразумения или погрешни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->