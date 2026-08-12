# Estructura del cuaderno

Los cuadernos de Jupyter son documentos JSON con esta estructura de alto nivel:

- `nbformat` y `nbformat_minor`
- `metadata`
- `cells` (una lista de celdas Markdown y de código)

Al editar archivos `.ipynb` programáticamente:

- Conserva `nbformat` y `nbformat_minor` de la plantilla.
- Mantén `cells` como una lista ordenada; no reordenes a menos que sea intencional.
- Para las celdas de código, establece `execution_count` a `null` cuando sea desconocido.
- Para las celdas de código, establece `outputs` en una lista vacía al generar la plantilla.
- Para las celdas Markdown, conserva `cell_type="markdown"` y `metadata={}`.

Prefiere generar la plantilla a partir de las plantillas incluidas o `new_notebook.py` (por ejemplo, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) en lugar de escribir manualmente el JSON bruto del cuaderno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Descargo de responsabilidad:
Este documento ha sido traducido mediante el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la exactitud, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por un traductor humano. No nos hacemos responsables de ningún malentendido o interpretación errónea que pueda surgir del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->