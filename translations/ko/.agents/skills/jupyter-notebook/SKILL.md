---
name: jupyter-notebook
description: 사용자가 실험, 탐색 또는 튜토리얼을 위한 Jupyter 노트북(`.ipynb`)을 생성, 스캐폴딩하거나 편집해 달라고 요청할
  때 사용합니다; 번들로 제공되는 템플릿을 우선 사용하고 깨끗한 시작 노트북을 생성하기 위해 헬퍼 스크립트 `new_notebook.py`를 실행하는
  것을 권장합니다.
---
# Jupyter Notebook 스킬

두 가지 주요 모드에 대해 깔끔하고 재현 가능한 Jupyter 노트북을 만드세요:

- 실험 및 탐색적 분석
- 튜토리얼 및 교육 중심 워크스루

일관된 구조와 JSON 실수 감소를 위해 번들된 템플릿과 도우미 스크립트를 사용하는 것을 권장합니다.

## When to use
- 새로운 `.ipynb` 노트북을 처음부터 생성할 때.
- 초안 노트나 스크립트를 구조화된 노트북으로 변환할 때.
- 기존 노트북을 재현 가능하고 훑어보기 쉬운 형태로 리팩터링할 때.
- 다른 사람들이 읽거나 다시 실행할 실험이나 튜토리얼을 만들 때.

## Decision tree
- 요청이 탐색적이거나 분석적이거나 가설 기반이라면 `experiment`를 선택하세요.
- 요청이 교육적이거나 단계별이거나 특정 대상에 초점을 둔다면 `tutorial`을 선택하세요.
- 기존 노트북을 편집하는 경우에는 리팩터로 간주하세요: 의도를 보존하고 구조를 개선하세요.

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

사용자 범위 스킬은 `$CODEX_HOME/skills`에 설치됩니다 (기본값: `~/.codex/skills`).

## Workflow
1. Lock the intent.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. Scaffold from the template.
템플릿으로부터 골격을 만드세요.
원시 노트북 JSON을 수동으로 작성하지 않도록 도우미 스크립트를 사용하세요.

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
노트북을 작은 실행 가능한 단계들로 채우세요.
각 코드 셀은 한 단계에 집중되도록 하세요.
목적과 예상 결과를 설명하는 짧은 마크다운 셀을 추가하세요.
짧은 요약으로 충분한 경우 큰 소음이 많은 출력은 피하세요.

4. Apply the right pattern.
실험의 경우 `references/experiment-patterns.md`를 따르세요.
튜토리얼의 경우 `references/tutorial-patterns.md`를 따르세요.

5. Edit safely when working with existing notebooks.
기존 노트북 작업 시 안전하게 편집하세요.
노트북 구조를 보존하세요; 위에서 아래로의 흐름을 개선하지 않는 한 셀의 순서를 변경하지 마세요.
전체 재작성보다 목표 지향적인 편집을 선호하세요.
원시 JSON을 편집해야 한다면 먼저 `references/notebook-structure.md`를 검토하세요.

6. Validate the result.
결과를 검증하세요.
환경이 허용하면 노트북을 위에서 아래로 실행하세요.
실행이 불가능하면 이를 명시적으로 알리고 로컬에서 어떻게 검증할지 안내하세요.
마지막 점검 체크리스트는 `references/quality-checklist.md`를 사용하세요.

## Templates and helper script
- 템플릿은 `assets/experiment-template.ipynb` 및 `assets/tutorial-template.ipynb`에 있습니다.
- 도우미 스크립트는 템플릿을 불러와 제목 셀을 업데이트하고 노트북을 작성합니다.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (설치 기본값: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- 중간 파일은 `tmp/jupyter-notebook/`를 사용하고 완료 후 삭제하세요.
- 이 리포지토리에서 작업할 때 최종 산출물은 `output/jupyter-notebook/` 아래에 작성하세요.
- 안정적이고 설명적인 파일 이름을 사용하세요 (예: `ablation-temperature.ipynb`).

## Dependencies (install only when needed)
필요한 경우에만 설치하세요.
종속성 관리는 `uv`를 권장합니다.

로컬 노트북 실행을 위한 선택적 Python 패키지:

```bash
uv pip install jupyterlab ipykernel
```

번들된 스캐폴드 스크립트는 Python 표준 라이브러리만 사용하므로 추가 종속성이 필요하지 않습니다.

## Environment
필수 환경 변수는 없습니다.

## Reference map
- `references/experiment-patterns.md`: 실험 구조 및 휴리스틱.
- `references/tutorial-patterns.md`: 튜토리얼 구조 및 교육 흐름.
- `references/notebook-structure.md`: 노트북 JSON 형태 및 안전한 편집 규칙.
- `references/quality-checklist.md`: 최종 검증 체크리스트.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책사항:**
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원래 언어로 된 원문을 권위 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문 번역가에 의한 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 어떠한 오해나 잘못된 해석에 대해서도 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->