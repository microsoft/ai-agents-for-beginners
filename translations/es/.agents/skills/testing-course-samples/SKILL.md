---
name: testing-course-samples
---
# Pruebas de las muestras del curso

Valide que los notebooks de las lecciones y las muestras de código se ejecuten con una configuración activa de
Microsoft Foundry / Azure OpenAI. El repositorio incluye un ejecutor en
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) que
ejecuta cada notebook de Python sin interfaz y muestra una matriz de APROBADO/FALLADO.

## Cuándo usarlo
- "Validar todos los notebooks / muestras contra mi suscripción de Azure."
- "Prueba rápida del curso después de actualizar paquetes o cambiar modelos."
- "¿Qué lecciones aún aprueban / fallan en entorno real?"

**No** use esto para la GitHub Action de Prueba Rápida de IA (que valida agentes *desplegados* —
consulte [`tests/README.md`](../../../tests/README.md)). Esta habilidad
ejecuta los notebooks localmente.

## Requisitos previos (verifique primero)
1. **Python 3.12+** con dependencias del curso: `python -m pip install -r requirements.txt`
   más el ejecutor: `python -m pip install nbconvert ipykernel`.
2. **`.env` en la raíz del repositorio** (copiar de [`.env.example`](../../../../../.env.example)) con al menos:
   - `AZURE_AI_PROJECT_ENDPOINT` — punto final del proyecto Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — un despliegue no obsoleto (p. ej., `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) y `AZURE_OPENAI_DEPLOYMENT`
     para lecciones que llaman directamente a Azure OpenAI (Lección 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** completado — las muestras se autentican con `AzureCliCredential` (Entra ID, sin claves).
4. Verifique que exista el despliegue del modelo:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Ejecución de la validación
```powershell
# Todos los notebooks de Python (excluye .NET, .venv, site-packages, traducciones, recursos de habilidad)
pwsh scripts/validate-notebooks.ps1

# Una sola lección, con un tiempo de espera por celda más largo
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Sólo listar lo que se ejecutaría (sin ejecución)
pwsh scripts/validate-notebooks.ps1 -List

# Intérprete explícito (si `python` no está en PATH, por ejemplo, alias de la Tienda de Windows)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
El script escribe copias ejecutadas, registros por notebook y `results.json` en
`$env:TEMP\aiab-nbval` y termina con el número de fallos.

## Interpretación de resultados
- `PASS` — el notebook se ejecutó de principio a fin sin error en las celdas.
- `FAIL` — se muestra la primera línea de `*Error` / `*Exception`; abra el `log_*.txt` correspondiente
  en el directorio de salida para ver el rastreo completo.
- La falla de un solo notebook está limitada por `-Timeout` (por celda), así que una celda con intervención humana
  atrapada se muestra como `StdinNotImplementedError` en lugar de quedarse colgada.

## Lecciones que necesitan recursos extra (se espera que fallen sin ellos)
| Lección | Requisito extra |
|--------|----------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, clave) — tiene una ruta de respaldo en memoria |
| 11 MCP / GitHub | Servidor GitHub MCP + PAT |
| 13 memory (cognee) | `cognee` configurado con un proveedor de modelos |
| 15 browser-use | Navegadores Playwright instalados (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Runtime local de Foundry + un modelo Qwen descargado (en el dispositivo, sin nube) |
| Notebooks `*-dotnet-*` | Kernel .NET Interactive (excluido por defecto; use `-IncludeDotnet`) |

## Reportar resultados
Resuma en una tabla de APROBADO/FALLADO agrupada por lección. Separe las regresiones genuinas
(errores de código/configuración por corregir) de las faltas en el entorno (búsqueda/Ffoundry Local/PAT faltantes),
y cite el `log_*.txt` que falla para cada error real.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->