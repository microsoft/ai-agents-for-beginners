---
name: jupyter-notebook
description: Используйте, когда пользователь просит создать, сгенерировать каркас
  или отредактировать Jupyter ноутбуки (`.ipynb`) для экспериментов, исследований
  или учебных материалов; предпочитайте встроенные шаблоны и запустите вспомогательный
  скрипт `new_notebook.py`, чтобы сгенерировать чистый начальный ноутбук.
---
# Навык Jupyter Notebook

Создавайте чистые, воспроизводимые блокноты Jupyter для двух основных режимов:

- Эксперименты и разведочный анализ
- Учебные материалы и обучающие пошаговые руководства

Используйте встроенные шаблоны и вспомогательный скрипт для единообразной структуры и меньшего количества ошибок в JSON.

## Когда использовать
- Создайте новый `.ipynb` блокнот с нуля.
- Преобразуйте грубые заметки или скрипты в структурированный блокнот.
- Рефакторите существующий блокнот, чтобы он был более воспроизводимым и удобным для быстрого просмотра.
- Разрабатывайте эксперименты или руководства, которые будут читаться или повторно запускаться другими людьми.

## Дерево решений
- Если запрос исследовательский, аналитический или ориентирован на гипотезы, выбирайте `experiment`.
- Если запрос носит обучающий характер, пошаговый или ориентирован на конкретную аудиторию, выбирайте `tutorial`.
- При редактировании существующего блокнота рассматривайте это как рефакторинг: сохраняйте исходный замысел и улучшайте структуру.

## Путь навыка (настраивается один раз)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Рабочий процесс
1. Зафиксируйте намерение.
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

3. Заполняйте блокнот небольшими исполняемыми шагами.
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
- `references/experiment-patterns.md`: структура эксперимента и эвристики.
- `references/tutorial-patterns.md`: структура руководства и учебный поток.
- `references/notebook-structure.md`: форма JSON блокнота и правила безопасного редактирования.
- `references/quality-checklist.md`: итоговый чеклист проверки.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведён с помощью сервиса машинного перевода на базе ИИ [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется обратиться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неверные толкования, возникающие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->