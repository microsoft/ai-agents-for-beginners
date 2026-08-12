---
name: jupyter-notebook
---
# Habilidade de Jupyter Notebook

Crie notebooks Jupyter limpos e reprodutíveis para dois modos principais:

- Experimentos e análise exploratória
- Tutoriais e guias voltados ao ensino

Prefira os modelos fornecidos e o script auxiliar para estrutura consistente e menos erros no JSON.

## Quando usar
- Crie um novo notebook `.ipynb` do zero.
- Converta anotações ou scripts brutos em um notebook estruturado.
- Refatore um notebook existente para torná-lo mais reprodutível e fácil de ler rapidamente.
- Crie experimentos ou tutoriais que serão lidos ou executados novamente por outras pessoas.

## Árvore de decisão
- Se a solicitação for exploratória, analítica ou orientada por hipótese, escolha `experiment`.
- Se a solicitação for instrucional, passo a passo ou direcionada a um público específico, escolha `tutorial`.
- Ao editar um notebook existente, trate-o como uma refatoração: preserve a intenção e melhore a estrutura.

## Caminho de habilidade (definir uma vez)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

As skills no escopo do usuário são instaladas em `$CODEX_HOME/skills` (padrão: `~/.codex/skills`).

## Fluxo de trabalho
1. Defina a intenção.
Identifique o tipo de notebook: `experiment` ou `tutorial`.
Registre o objetivo, o público e o que significa 'concluído'.

2. Estruture a partir do modelo.
Use o script auxiliar para evitar escrever manualmente o JSON bruto do notebook.

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

3. Preencha o notebook com etapas pequenas e executáveis.
Mantenha cada célula de código focada em um passo.
Adicione células markdown curtas que expliquem o propósito e o resultado esperado.
Evite saídas grandes e ruidosas quando um resumo breve resolve.

4. Aplique o padrão correto.
Para experimentos, siga `references/experiment-patterns.md`.
Para tutoriais, siga `references/tutorial-patterns.md`.

5. Edite com segurança ao trabalhar com notebooks existentes.
Preserve a estrutura do notebook; evite reordenar células, a menos que isso melhore a narrativa de cima para baixo.
Prefira edições direcionadas a reescritas completas.
Se for necessário editar o JSON bruto, revise `references/notebook-structure.md` primeiro.

6. Valide o resultado.
Execute o notebook de cima para baixo quando o ambiente permitir.
Se a execução não for possível, informe isso explicitamente e explique como validar localmente.
Use a lista de verificação da passagem final em `references/quality-checklist.md`.

## Modelos e script auxiliar
- Os modelos ficam em `assets/experiment-template.ipynb` e `assets/tutorial-template.ipynb`.
- O script auxiliar carrega um modelo, atualiza a célula de título e grava um notebook.

Caminho do script:
- `$JUPYTER_NOTEBOOK_CLI` (instalado por padrão: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Convenções de arquivos temporários e de saída
- Use `tmp/jupyter-notebook/` para arquivos intermediários; exclua quando terminar.
- Grave artefatos finais em `output/jupyter-notebook/` ao trabalhar neste repositório.
- Use nomes de arquivo estáveis e descritivos (por exemplo, `ablation-temperature.ipynb`).

## Dependências (instale apenas quando necessário)
Prefira `uv` para gerenciamento de dependências.

Pacotes Python opcionais para execução local de notebooks:

```bash
uv pip install jupyterlab ipykernel
```

O script de scaffold fornecido usa apenas a biblioteca padrão do Python e não requer dependências extras.

## Ambiente
Nenhuma variável de ambiente obrigatória.

## Mapa de referências
- `references/experiment-patterns.md`: estrutura de experimento e heurísticas.
- `references/tutorial-patterns.md`: estrutura de tutorial e fluxo de ensino.
- `references/notebook-structure.md`: formato do JSON do notebook e regras para edição segura.
- `references/quality-checklist.md`: lista de verificação final de validação.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Isenção de responsabilidade:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por tradutores humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->