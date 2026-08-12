---
name: jupyter-notebook
description: Usar cuando el usuario solicita crear, estructurar o editar cuadernos
  Jupyter (`.ipynb`) para experimentos, exploraciones o tutoriales; preferir las plantillas
  incluidas y ejecutar el script auxiliar `new_notebook.py` para generar un cuaderno
  inicial limpio.
---
# Habilidad de Jupyter Notebook

Crea notebooks de Jupyter limpios y reproducibles para dos modos principales:

- Experimentos y análisis exploratorio
- Tutoriales y guías orientadas a la enseñanza

Prefiere las plantillas incluidas y el script auxiliar para una estructura coherente y menos errores en JSON.

## Cuándo usar
- Crea un nuevo `.ipynb` notebook desde cero.
- Convierte notas o scripts informales en un notebook estructurado.
- Refactoriza un notebook existente para que sea más reproducible y fácil de revisar.
- Crea experimentos o tutoriales que serán leídos o ejecutados nuevamente por otras personas.

## Árbol de decisiones
- Si la solicitud es exploratoria, analítica o basada en hipótesis, elige `experiment`.
- Si la solicitud es instruccional, paso a paso o dirigida a una audiencia específica, elige `tutorial`.
- Si estás editando un notebook existente, trátalo como una refactorización: conserva la intención y mejora la estructura.

## Ruta de la habilidad (configurar una vez)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Las habilidades a nivel de usuario se instalan en `$CODEX_HOME/skills` (por defecto: `~/.codex/skills`).

## Flujo de trabajo
1. Fija la intención.
Identifica el tipo de notebook: `experiment` o `tutorial`.
Registra el objetivo, la audiencia y qué significa "hecho".

2. Estructura a partir de la plantilla.
Usa el script auxiliar para evitar redactar manualmente el JSON bruto del notebook.

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

3. Rellena el notebook con pasos pequeños y ejecutables.
Mantén cada celda de código enfocada en un solo paso.
Añade celdas markdown cortas que expliquen el propósito y el resultado esperado.
Evita salidas grandes y ruidosas cuando un resumen breve funciona.

4. Aplica el patrón adecuado.
Para experimentos, sigue `references/experiment-patterns.md`.
Para tutoriales, sigue `references/tutorial-patterns.md`.

5. Edita de forma segura cuando trabajes con notebooks existentes.
Preserva la estructura del notebook; evita reordenar las celdas a menos que mejore la narrativa de arriba hacia abajo.
Prefiere ediciones específicas en lugar de reescrituras completas.
Si debes editar el JSON bruto, revisa primero `references/notebook-structure.md`.

6. Valida el resultado.
Ejecuta el notebook de arriba a abajo cuando el entorno lo permita.
Si la ejecución no es posible, indícalo explícitamente y explica cómo validar localmente.
Usa la lista de verificación final en `references/quality-checklist.md`.

## Plantillas y script auxiliar
- Las plantillas se encuentran en `assets/experiment-template.ipynb` y `assets/tutorial-template.ipynb`.
- El script auxiliar carga una plantilla, actualiza la celda de título y escribe un notebook.

Ruta del script:
- `$JUPYTER_NOTEBOOK_CLI` (instalado por defecto: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Convenciones de archivos temporales y de salida
- Usa `tmp/jupyter-notebook/` para archivos intermedios; elimínalos cuando termines.
- Escribe los artefactos finales en `output/jupyter-notebook/` cuando trabajes en este repositorio.
- Usa nombres de archivo estables y descriptivos (por ejemplo, `ablation-temperature.ipynb`).

## Dependencias (instala solo cuando sea necesario)
Prefiere `uv` para la gestión de dependencias.

Paquetes opcionales de Python para la ejecución local del notebook:

```bash
uv pip install jupyterlab ipykernel
```

El script de scaffolding incluido utiliza solo la biblioteca estándar de Python y no requiere dependencias adicionales.

## Entorno
No se requieren variables de entorno.

## Mapa de referencia
- `references/experiment-patterns.md`: estructura del experimento y heurísticas.
- `references/tutorial-patterns.md`: estructura del tutorial y flujo de enseñanza.
- `references/notebook-structure.md`: forma del JSON del notebook y reglas para editar de forma segura.
- `references/quality-checklist.md`: lista de verificación final de validación.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Descargo de responsabilidad:
Este documento ha sido traducido usando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por la exactitud, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por un traductor humano. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->