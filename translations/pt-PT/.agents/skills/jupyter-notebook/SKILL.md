---
name: jupyter-notebook
description: Usado quando o utilizador pede para criar, estruturar ou editar Jupyter
  notebooks (`.ipynb`) para experiências, explorações ou tutoriais; prefira os modelos
  incluídos e execute o script auxiliar `new_notebook.py` para gerar um notebook inicial
  limpo.
---
# Competência Jupyter Notebook

Crie notebooks Jupyter limpos e reprodutíveis para dois modos principais:

- Experimentos e análise exploratória
- Tutoriais e walkthroughs orientados ao ensino

Prefira os modelos incluídos e o script auxiliar para uma estrutura consistente e menos erros no JSON.

## Quando usar
- Crie um novo `.ipynb` notebook a partir do zero.
- Converta notas soltas ou scripts num notebook estruturado.
- Refatore um notebook existente para que seja mais reprodutível e fácil de ler.
- Construa experimentos ou tutoriais que serão lidos ou executados por outras pessoas.

## Árvore de decisão
- Se o pedido for exploratório, analítico ou orientado por hipóteses, escolha `experiment`.
- Se o pedido for instrucional, passo-a-passo ou dirigido a um público específico, escolha `tutorial`.
- Se estiver a editar um notebook existente, trate-o como uma refatoração: preserve a intenção e melhore a estrutura.

## Caminho de competências (definir uma vez)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

As skills a nível de utilizador instalam-se em `$CODEX_HOME/skills` (por omissão: `~/.codex/skills`).

## Workflow
1. Defina a intenção.
Identifique o tipo de notebook: `experiment` ou `tutorial`.
Registe o objetivo, o público e como se percebe que está "concluído".

2. Estruture a partir do modelo.
Use o script auxiliar para evitar criar manualmente o JSON bruto do notebook.

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

3. Preencha o notebook com pequenos passos executáveis.
Mantenha cada célula de código focada num único passo.
Adicione pequenas células markdown que expliquem o propósito e o resultado esperado.
Evite saídas grandes e ruidosas quando um resumo curto for suficiente.

4. Aplique o padrão adequado.
Para experimentos, siga `references/experiment-patterns.md`.
Para tutoriais, siga `references/tutorial-patterns.md`.

5. Edite com segurança ao trabalhar com notebooks existentes.
Preserve a estrutura do notebook; evite reordenar células a menos que isso melhore a narrativa de cima para baixo.
Prefira edições direcionadas em vez de reescritas completas.
Se tiver de editar o JSON bruto, reveja `references/notebook-structure.md` primeiro.

6. Valide o resultado.
Execute o notebook de cima para baixo quando o ambiente permitir.
Se a execução não for possível, declare-o explicitamente e indique como validar localmente.
Use a checklist de passagem final em `references/quality-checklist.md`.

## Modelos e script auxiliar
- Os modelos estão em `assets/experiment-template.ipynb` e `assets/tutorial-template.ipynb`.
- O script auxiliar carrega um modelo, atualiza a célula de título e escreve um notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (instalado por omissão: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Convenções para ficheiros temporários e de saída
- Use `tmp/jupyter-notebook/` para ficheiros intermédios; elimine quando terminar.
- Escreva artefactos finais em `output/jupyter-notebook/` quando trabalhar neste repo.
- Use nomes de ficheiro estáveis e descritivos (por exemplo, `ablation-temperature.ipynb`).

## Dependências (instalar só quando necessário)
Prefira `uv` para gestão de dependências.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

O script de scaffolding incluído usa apenas a biblioteca padrão do Python e não requer dependências extra.

## Ambiente
Não há variáveis de ambiente obrigatórias.

## Mapa de referência
- `references/experiment-patterns.md`: estrutura de experimentos e heurísticas.
- `references/tutorial-patterns.md`: estrutura de tutoriais e fluxo de ensino.
- `references/notebook-structure.md`: forma do JSON do notebook e regras de edição segura.
- `references/quality-checklist.md`: checklist de validação final.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a exatidão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional realizada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->