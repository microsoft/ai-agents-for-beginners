---
name: testing-course-samples
---
# Probando las muestras del curso

Valide que los cuadernos de lecciones y los ejemplos de código se ejecuten contra una configuración en vivo de
Microsoft Foundry / Azure OpenAI. El repositorio incluye un ejecutor en
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) que
ejecuta cada cuaderno de Python sin cabeza y muestra una matriz de APROBADO/FALLADO.

## Cuándo usarlo
- "Validar todos los cuadernos / muestras con mi suscripción de Azure."
- "Prueba rápida del curso después de actualizar paquetes o cambiar modelos."
- "¿Qué lecciones aún pasan / fallan en vivo?"

No utilice esto para la Acción GitHub de Prueba Rápida de IA (que valida *desplegados*
agentes alojados — vea [`tests/README.md`](../../../tests/README.md)). Esta habilidad
ejecuta los cuadernos localmente.

## Prerrequisitos (verificar primero)
1. **Python 3.12+** con las dependencias del curso: `python -m pip install -r requirements.txt`
   además del ejecutor: `python -m pip install nbconvert ipykernel`.
2. **`.env` en la raíz del repositorio** (copiar desde [`.env.example`](../../../../../.env.example)) con al menos:
   - `AZURE_AI_PROJECT_ENDPOINT` — endpoint del proyecto Foundry
     (`https://<cuenta>.services.ai.azure.com/api/projects/<proyecto>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — un despliegue no obsoleto (por ejemplo `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<cuenta>.openai.azure.com`) y `AZURE_OPENAI_DEPLOYMENT`
     para lecciones que llaman a Azure OpenAI directamente (Lección 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** completado — las muestras se autentican con `AzureCliCredential` (Entra ID, sin claves).
4. Verifique que el despliegue del modelo exista:
   `az cognitiveservices account deployment list -g <rg> -n <cuenta> -o table`.

## Ejecución de la validación
```powershell
# Todos los notebooks de Python (excluye .NET, .venv, site-packages, traducciones, recursos de habilidades)
pwsh scripts/validate-notebooks.ps1

# Una sola lección, con un tiempo de espera más largo por celda
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Solo listar lo que se ejecutaría (sin ejecución)
pwsh scripts/validate-notebooks.ps1 -List

# Intérprete explícito (si `python` no está en PATH, por ejemplo alias de la Tienda de Windows)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
El script escribe copias ejecutadas, registros por cuaderno y `results.json` en
`$env:TEMP\aiab-nbval` y termina con el número de fallos.

Fallos transitorios (límites de tasa HTTP 429 de suscripción compartida, un tropiezo ocasional de
token `AzureCliCredential`, o un tiempo de espera) se reintentan automáticamente
(`-Retries`, 2 por defecto, con retardo `-RetryDelaySeconds`, 20 por defecto). Si un
despliegue de modelo genera 429 regularmente, revise la cuota TPM GlobalStandard
de la suscripción (`az cognitiveservices usage list -l <región>`) — aumentar la capacidad de un solo
despliegue no ayuda cuando la cuota de *suscripción* está agotada.

## Interpretación de resultados
- `PASS` — el cuaderno se ejecutó de principio a fin sin errores en celdas.
- `FAIL` — se muestra la primera línea de `*Error` / `*Exception`; abra el
  `log_*.txt` correspondiente en el directorio de salida para ver el rastro completo.
- El fallo de un único cuaderno está limitado por `-Timeout` (por celda), por lo que una
  celda de interacción humana colgada aparece como `StdinNotImplementedError` en lugar de quedarse colgada.

## Lecciones que necesitan recursos extra (se espera que fallen sin ellos)
| Lección | Requisito extra |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, clave) — tiene una ruta de reserva en memoria |
| 11 MCP / GitHub | Servidor MCP de GitHub + PAT |
| 13 memoria (cognee) | `cognee` configurado con un proveedor de modelo |
| 15 uso de navegador | Navegadores Playwright instalados (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 agente local | Runtime Local de Foundry + modelo Qwen descargado (en dispositivo, sin nube) |
| cuadernos `*-dotnet-*` | Kernel interactivo .NET (excluido por defecto; use `-IncludeDotnet`) |

## Informar resultados
Resuma en una tabla de APROBADO/FALLADO agrupada por lección. Separe las regresiones genuinas
(errores de código/configuración a corregir) de las brechas del entorno (Search/Foundry Local/PAT faltantes),
y cite los `log_*.txt` con fallos para cada fallo real.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->