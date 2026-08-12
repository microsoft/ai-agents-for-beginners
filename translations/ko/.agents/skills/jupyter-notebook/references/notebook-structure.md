# 노트북 구조

Jupyter 노트북은 다음과 같은 고수준 형태의 JSON 문서입니다:

- `nbformat` 및 `nbformat_minor`
- `metadata`
- `cells` (마크다운 및 코드 셀의 목록)

When editing `.ipynb` files programmatically:

- 템플릿의 `nbformat` 및 `nbformat_minor`을 보존하세요.
- `cells`를 순서가 있는 목록으로 유지하세요; 의도적이지 않다면 재정렬하지 마세요.
- 코드 셀의 경우, 알 수 없을 때 `execution_count`를 `null`로 설정하세요.
- 코드 셀의 경우, 스캐폴딩할 때 `outputs`를 빈 목록으로 설정하세요.
- 마크다운 셀의 경우, `cell_type="markdown"` 및 `metadata={}`을 유지하세요.

Prefer scaffolding from the bundled templates or `new_notebook.py` (for example, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) instead of hand-authoring raw notebook JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
면책 조항:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하십시오. 원문(원어) 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->