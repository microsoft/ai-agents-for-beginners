---
name: azure-openai-to-responses
license: MIT
---
# Migrar aplicaciones Python de Azure OpenAI Chat Completions a Responses API

> **GUIA AUTORIZADA — SEGUIR EXACTAMENTE**
>
> Esta habilidad migra bases de código Python que usan Azure OpenAI Chat Completions
> a la API unificada de Responses. Siga estas instrucciones con precisión.
> No improvise mapeos de parámetros ni invente formas de API.

---

## Desencadenantes

Active esta habilidad cuando el usuario quiera:
- Migrar una aplicación Python de Azure OpenAI Chat Completions a Responses API
- Actualizar el uso del SDK OpenAI en Python a la forma de API más reciente contra Azure OpenAI
- Preparar código Python para modelos GPT-5 o más nuevos que requieren Responses en Azure
- Cambiar de `AzureOpenAI`/`AsyncAzureOpenAI` a cliente estándar `OpenAI`/`AsyncOpenAI` con el endpoint v1
- Corregir advertencias de deprecación relacionadas con constructores `AzureOpenAI` o `api_version`

---

## ⚠️ Compatibilidad del modelo — VERIFICAR PRIMERO

> **Antes de migrar, verifique que su implementación Azure OpenAI soporte la API de Responses.**

### 1. Prueba rápida de implementación (más rápida)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Nota**: `max_output_tokens` tiene un **mínimo de 16** en Azure OpenAI. Valores por debajo de 16 devuelven error 400. Use 50+ para pruebas rápidas.

Si esto devuelve 404, el modelo de la implementación aún no soporta Responses — consulte la referencia a continuación o vuelva a implementar con un modelo compatible.

### 2. Verifique modelos disponibles en su región (recomendado)

Ejecute la herramienta incorporada de compatibilidad de modelos para ver qué está disponible con soporte para Responses API en su región específica:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Esto consulta Azure ARM en tiempo real y muestra una matriz de compatibilidad — qué modelos soportan Responses, salida estructurada, herramientas, etc. Use `--filter gpt-5.1,gpt-5.2` para filtrar resultados o `--json` para scripting.

### 3. Referencia completa de soporte de modelos

- **Consulta en vivo**: `python migrate.py models` (ver arriba — específica por región, siempre actualizada)
- **Navegar disponibilidad**: [Tabla resumen de modelos y disponibilidad por región](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Inicio rápido y guía**: **https://aka.ms/openai/start**

### ⚠️ Limitaciones de modelos más antiguos

> **ADVERTENCIA**: Los modelos antiguos (anteriores a `gpt-4.1`) pueden no soportar completamente todas las características de Responses API.
>
> Limitaciones conocidas con modelos antiguos:
> - **Parámetro `reasoning`**: No soportado en muchos modelos sin razonamiento. Migre `reasoning` solo si ya estaba presente en el código original.
> - **Parámetro `seed`**: No soportado en Responses API en absoluto — elimínelo de todas las solicitudes.
> - **Salida estructurada vía `text.format`**: Modelos antiguos pueden no aplicar esquemas JSON `strict: true` confiablemente.
> - **Orquestación de herramientas**: GPT-5+ orquesta llamadas a herramientas como parte del razonamiento interno. Modelos antiguos en Responses funcionan pero carecen de esta integración profunda.
> - **Restricciones de temperatura**: Al migrar a `gpt-5`, la temperatura debe omitirse o ponerse en `1`. Modelos antiguos no tienen esta restricción.

### Modelos de razonamiento serie O (o1, o3-mini, o3, o4-mini)

Los modelos serie O tienen restricciones únicas en parámetros. Al migrar aplicaciones que apuntan a modelos serie O:

- **`temperature`**: Debe ser `1` (o omitido). Modelos serie O no aceptan otros valores.
- **`max_completion_tokens` → `max_output_tokens`**: Aplicaciones que usan el específico de Azure `max_completion_tokens` deben cambiar a `max_output_tokens`. Use valores altos (4096+) porque los tokens de razonamiento cuentan para el límite.
- **`reasoning_effort`**: Si la app usa `reasoning_effort` (bajo/medio/alto), manténgalo — la Responses API soporta este parámetro para modelos serie O.
- **Comportamiento de streaming**: Modelos serie O pueden acumular salida hasta completar razonamiento antes de emitir eventos delta de texto. El streaming sigue funcionando, pero el primer `response.output_text.delta` puede llegar tras un retraso mayor que con modelos GPT.
- **`top_p`**: No soportado en serie O — elimínelo si está presente.
- **Uso de herramientas**: Modelos serie O soportan herramientas vía Responses API igual que modelos GPT, pero la calidad de la orquestación varía según el modelo.

**Acción — asesoría proactiva de modelo**: Durante la fase de escaneo, verifique qué modelo usa la app (nombres de implementaciones, variables de entorno, configuración). Si el modelo es anterior a `gpt-4.1` (no gpt-4.1+), informe proactivamente al usuario:
- La migración funcionará para texto básico, chat, streaming y herramientas en su modelo actual.
- Modelos más nuevos (`gpt-5.1`, `gpt-5.2`) ofrecen mejor orquestación de herramientas, aplicación estricta de salida estructurada, razonamiento y disponibilidad regional cruzada.
- Deben considerar actualizar su implementación cuando estén listos — no bloquea la migración.

No bloquee ni rechace la migración basada en la versión del modelo. La asesoría es solo informativa.

### GitHub Models NO soporta Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) no soporta Responses API.**

Si la base de código tiene una ruta para GitHub Models (busque `base_url` apuntando a `models.github.ai` o `models.inference.ai.azure.com`), **elimínela completamente** durante la migración. La Responses API requiere Azure OpenAI, OpenAI o un endpoint local compatible (p. ej., Ollama con soporte Responses).

Acción durante el escaneo:
- Señale cualquier ruta de código GitHub Models para eliminación.

---

## Migración de frameworks

Muchas apps usan frameworks de alto nivel sobre OpenAI. Al migrar estas, cambian las API propias del framework — no solo las llamadas internas a OpenAI.

### Microsoft Agent Framework (MAF)

**Verifique su versión de MAF primero** — la migración depende de si está en MAF 1.0.0+ o en beta/rc pre-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ya usa Responses API** — no necesita migración. Si la base usa el legado `OpenAIChatCompletionClient` (que usa `chat.completions.create`), reemplácelo por `OpenAIChatClient`.

| Antes | Después |
|--------|--------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Para revisar su versión: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (versiones beta/rc)

En MAF pre-1.0.0, `OpenAIChatClient` usaba Chat Completions. Actualice a `agent-framework-openai>=1.0.0` donde `OpenAIChatClient` usa por defecto Responses API.

No se necesitan otros cambios — las APIs `Agent` y de herramientas permanecen igual.

### LangChain (`langchain-openai`)

Añada `use_responses_api=True` a `ChatOpenAI()`. También actualice acceso a respuesta de `.content` a `.text`.

| Antes | Después |
|--------|--------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Para ejemplos completos antes y después, vea [cheat-sheet.md](./references/cheat-sheet.md).

---

## Guía de migración frontend

> **La Responses API es un asunto del lado servidor.** Migre su backend Python; el contrato HTTP del frontend debería mantenerse sin cambios a menos que su backend sea un paso delgado — en tal caso, considere adoptar la forma Requests de Responses para eliminar una capa de traducción. Si el frontend llama directamente a OpenAI con una clave del cliente, mueva esas llamadas primero al backend.

### Deprecated `@microsoft/ai-chat-protocol`

El paquete npm `@microsoft/ai-chat-protocol` está deprecado y debe reemplazarse por [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Si lo encuentra en un frontend:

1. Reemplace la etiqueta de script CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Elimine la instancia `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Reemplace `client.getStreamedCompletion(messages)` con llamada directa `fetch()` al endpoint streaming backend.
4. Reemplace `for await (const response of result)` con `for await (const chunk of readNDJSONStream(response.body))`.
5. Actualice acceso a propiedades de `response.delta.content` / `response.error` a `chunk.delta.content` / `chunk.error`.

---

## Objetivos

- Enumerar todos los lugares de llamada Python que usan Chat Completions o Completions legados contra Azure OpenAI.
- Proponer un plan de migración y secuencia para la base de código Python.
- Aplicar ediciones seguras y mínimas para cambiar a Responses API.
- Actualizar llamadas para consumir el esquema de salida Responses; sin envoltorios de compatibilidad.
- Ejecutar tests/lint; corregir fallas triviales introducidas por la migración.
- Preparar conjuntos de cambios pequeños y revisables y proveer resumen final con diffs (no hacer commit).

---

## Reglas de seguridad

- Modifique solo archivos dentro del espacio de trabajo git. Nunca escriba fuera.
- No preserve adaptadores de compatibilidad hacia atrás; migre código a la nueva forma de API.
- No deje comentarios de transición ni archivos respaldo.
- Preservar semántica de streaming si se usaba previamente; si no, usar no streaming.
- Solicite aprobación antes de ejecutar comandos o llamadas de red si está en modo de aprobación.
- No ejecute `git add`/`git commit`/`git push`; producir solo ediciones en el árbol de trabajo.

---

## Paso 0: Migración del cliente Azure OpenAI (Prerrequisito)

Si la base usa constructores `AzureOpenAI` o `AsyncAzureOpenAI`, migre primero a constructores estándar `OpenAI` / `AsyncOpenAI`. Los constructores específicos de Azure están deprecados en `openai>=1.108.1`.

### ¿Por qué el path API v1?

El nuevo endpoint `/openai/v1` usa el cliente estándar `OpenAI()` en lugar de `AzureOpenAI()`, no requiere parámetro `api_version` y funciona idéntico en OpenAI y Azure OpenAI. El mismo código cliente es a prueba de futuro — sin necesidad de gestión de versiones.

### Cambios clave

| Antes | Después |
|-------|---------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Eliminar completamente |

### Lista de limpieza

- Eliminar argumento `api_version` de la construcción del cliente.
- Eliminar variables de entorno `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` de `.env`, configuraciones de app, y archivos Bicep/infra.
- Renombrar `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` en `.env`, configuraciones de app, Bicep/infra, y fixtures de tests (convención estándar Azure Identity SDK).
- Asegurarse que `openai>=1.108.1` esté en `requirements.txt` o `pyproject.toml`.

### Migración de variables de entorno

| Variable antigua | Acción | Notas |
|---------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Eliminar** | No se necesita `api_version` con endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Eliminar** | Igual que arriba |
| `AZURE_OPENAI_CLIENT_ID` | **Renombrar** → `AZURE_CLIENT_ID` | Convención estándar Azure Identity SDK para `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Mantener** | Todavía usado para construir `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Mantener** | Usado como parámetro `model` en `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Mantener** | Usado como `api_key` para autenticación por clave |

Para ejemplos de código de setup cliente (sync, async, EntraID, clave API, multi-inquilino), vea [cheat-sheet.md](./references/cheat-sheet.md).

---

## Paso 1: Detectar lugares de llamada legados

Ejecute el script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) para encontrar todos los lugares de llamada que requieren migración:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

O ejecute estas búsquedas manualmente — cada coincidencia es un objetivo de migración:

```bash
# Llamadas a la API heredada (deben reescribirse)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Constructores de clientes de Azure obsoletos (deben reemplazarse)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Patrones de acceso a la forma de respuesta (deben actualizarse)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definiciones de herramientas en formato antiguo anidado (deben aplanarse)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Resultados de herramientas en formato antiguo (deben convertirse a function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Parámetros obsoletos (deben eliminarse o renombrarse)
rg "response_format"
rg "max_tokens\b"        # renombrar a max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Variables de entorno obsoletas (limpiar)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # debería ser AZURE_CLIENT_ID

# Endpoints de modelos de GitHub (deben eliminarse — API de respuestas no soportada)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Patrones heredados a nivel de framework (deben actualizarse)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: reemplazar con OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: necesita use_responses_api=True

# Infraestructura de pruebas (debe actualizarse)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Acceso al cuerpo de error del filtro de contenido (debe actualizarse — estructura cambiada)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # forma singular antigua — ahora content_filter_results (plural) dentro del arreglo content_filters

# Llamadas HTTP en bruto al endpoint de Chat Completions (debe actualizarse la URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heurísticas (detectar y reescribir)

- **Cliente Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Constructores del cliente Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Herramientas**: convertir definiciones de herramientas para llamadas a funciones de formato anidado (`{"type": "function", "function": {"name": ...}}`) a formato plano de Responses (`{"type": "function", "name": ...}`); usar `tool_choice`; devolver resultados de herramientas como ítems `{"type": "function_call_output", "call_id": ..., "output": ...}` (no `{"role": "tool", ...}`).
- **Recorridos de herramientas**: cuando el modelo devuelve llamadas a funciones, agregar ítems `response.output` a la conversación (no un dict manual `{"role": "assistant", "tool_calls": [...]}`), luego agregar ítems `function_call_output` para cada resultado.
- **Ejemplos de herramientas con pocos disparos**: si la conversación incluye ejemplos codificados de llamadas a herramientas, convertirlos a ítems `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Los IDs deben comenzar con `fc_`.
- **`pydantic_function_tool()`**: este asistente aún genera el formato anidado antiguo y **no es compatible** con `responses.create()`. Reemplazar con definiciones manuales de herramientas o un envoltorio para aplanar.
- **Multi-turn**: mantener el historial de la conversación en la app; pasar los turnos previos a través de ítems `input`.
- **Formato**: reemplazar el `response_format` de nivel superior de Chat con `text.format` en Responses. Forma canónica: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Ítems de contenido**: reemplazar `content[].type: "text"` de Chat con `content[].type: "input_text"` en Responses para turnos de usuario/sistema.
- **Ítems de contenido de imagen**: reemplazar `content[].type: "image_url"` de Chat con `content[].type: "input_image"` en Responses. El campo `image_url` cambia de un objeto anidado `{"url": "..."}` a una cadena plana. Ver la hoja de referencia para ejemplos antes/después.
- **Esfuerzo de razonamiento**: **solo migrar `reasoning` si ya existe en el código original**.
- **Manejo de errores del filtro de contenido**: la estructura del cuerpo de error cambió. Chat Completions usaba `error.body["innererror"]["content_filter_result"]` (singular); Responses API usa `error.body["content_filters"][0]["content_filter_results"]` (plural, dentro de un arreglo). El código que acceda a `innererror` lanzará `KeyError`. Reescribir para usar la nueva ruta.
- **Llamadas HTTP sin procesar**: si la app realiza llamadas directas REST al Azure OpenAI API (mediante `requests`, `httpx`, etc.) usando `/openai/deployments/{name}/chat/completions?api-version=...`, reescribir a `/openai/v1/responses`. El cuerpo de la petición cambia: `messages` → `input`, agregar `max_output_tokens` y `store: false`, eliminar el parámetro de consulta `api-version`. El cuerpo de la respuesta cambia: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` es una propiedad de conveniencia del SDK que no está presente en JSON REST sin procesar).

---

## Paso 2: Aplicar la migración

### Notas de migración (Chat Completions → Responses)

- **Por qué migrar**: Responses es la API unificada para texto, herramientas y streaming; Chat Completions es legado. Con GPT-5, Responses es requerido para el mejor desempeño.
- **HTTP**: el endpoint de Azure cambia de `/openai/deployments/{name}/chat/completions` a `/openai/v1/responses`.
- **Campos**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` permanece igual.
- **Formato**: `response_format` → `text.format` con un objeto apropiado.
- **Ítems de contenido**: Reemplazar `content[].type: "text"` de Chat con `content[].type: "input_text"` de Responses para turnos de sistema/usuario.
- **Ítems de contenido de imagen**: Reemplazar `content[].type: "image_url"` de Chat con `content[].type: "input_image"` de Responses. Aplanar el campo `image_url` de `{"image_url": {"url": "..."}}` a `{"image_url": "..."}` (una cadena simple, ya sea una URL HTTPS o un URI de datos `data:image/...;base64,...`).

### Referencia de mapeo de parámetros

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (arreglo de ítems) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objeto) |
| `temperature` | `temperature` (sin cambios) |
| `stop` | `stop` (sin cambios) |
| `frequency_penalty` | `frequency_penalty` (sin cambios) |
| `presence_penalty` | `presence_penalty` (sin cambios) |
| `tools` / llamadas a funciones | `tools` (sin cambios) |
| `seed` | **Eliminar** (no soportado) |
| `store` | `store` (fijar en `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (cadena plana) |

Para ejemplos completos de código antes y después, ver [cheat-sheet.md](./references/cheat-sheet.md).

Para la migración de infraestructura de pruebas (mocks, snapshots, asersiones), ver [test-migration.md](./references/test-migration.md).

Para solución de problemas y puntos críticos, ver [troubleshooting.md](./references/troubleshooting.md).

---

## Retención de datos y estado

- Fijar `store: false` en todas las peticiones a Responses.
- No confiar en IDs de mensajes previos ni en contexto almacenado en servidor; mantener estado gestionado por el cliente y minimizar metadatos.

---

## Criterios de aceptación

### Reglas a nivel de código (todas deben pasar)

- [ ] Cero coincidencias con `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` en archivos migrados.
- [ ] Cero coincidencias con `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — todos los constructores usan `OpenAI`/`AsyncOpenAI` con el endpoint v1.
- [ ] Cero coincidencias con `rg "models\.github\.ai|models\.inference\.ai\.azure"` — rutas de código de modelos GitHub eliminadas.
- [ ] Cero coincidencias con `rg "OpenAIChatCompletionClient"` — código MAF 1.0.0+ usa `OpenAIChatClient` (que usa Responses API). En pre-1.0.0, actualizar a `agent-framework-openai>=1.0.0`.
- [ ] Todas las llamadas a `ChatOpenAI(...)` incluyen `use_responses_api=True`.
- [ ] Cero coincidencias con `rg "choices\[0\]"` — todo acceso a respuesta usa `resp.output_text` o el esquema de salida de Responses.
- [ ] No hay `response_format` en el nivel superior; toda salida estructurada usa `text={"format": {...}}`.
- [ ] `openai>=1.108.1` y `azure-identity` en `requirements.txt` o `pyproject.toml`; dependencias reinstaladas.
- [ ] `store=False` establecido en cada llamada a `responses.create`.
- [ ] No hay `api_version` en la construcción del cliente; `AZURE_OPENAI_API_VERSION` eliminado de archivos de entorno e infra.

### Reglas para infraestructura de pruebas (todas deben pasar)

- [ ] Cero coincidencias con `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Cero coincidencias con `rg "_azure_ad_token_provider" tests/` — asersiones actualizadas para verificar `isinstance(client, AsyncOpenAI)` o `base_url`.
- [ ] Cero coincidencias con `rg "prompt_filter_results|content_filter_results" tests/` — mocks específicos de filtro Azure eliminados.
- [ ] Fixtures de mocks usan `kwargs.get("input")` no `kwargs.get("messages")`.
- [ ] Archivos snapshot / golden actualizados al formato de streaming de Responses (sin `choices[0]`, `function_call`, `logprobs`, etc.).
- [ ] `pytest` pasa con cero fallos tras todas las actualizaciones de pruebas.

### Reglas comportamentales (verificar manualmente o mediante test harness)

- [ ] **Completado básico**: `responses.create` sin streaming devuelve `output_text` no vacío.
- [ ] **Paridad en streaming**: si el código original usaba streaming, el código migrado transmite y produce eventos `response.output_text.delta` con deltas no vacíos.
- [ ] **Salida estructurada**: si se usa `text.format` con `json_schema`, `json.loads(resp.output_text)` tiene éxito y coincide con el esquema.
- [ ] **Bucle de llamadas a herramientas**: si se usan herramientas, el modelo realiza llamadas a ellas, la app las ejecuta y la petición de seguimiento devuelve un `output_text` final (sin bucle infinito).
- [ ] **Paridad async**: si se usaba `AsyncAzureOpenAI`, el equivalente `AsyncOpenAI` funciona con `await`.
- [ ] **Tasa de errores**: no hay nuevos errores 400/401/404 comparado con la línea base antes de la migración.

### Entregables

- El resumen incluye archivos editados, conteo antes/después de sitios de llamadas legacy y siguientes pasos.
- Los cambios son solo en el árbol de trabajo (sin commits).

---

## Requisitos de versión del SDK

| Paquete | Versión mínima |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Última (para autenticación EntraID) |

---

## Referencias

- [Hoja de referencia — todos los fragmentos de código](./references/cheat-sheet.md)
- [Migración de pruebas — mocks, snapshots, asersiones](./references/test-migration.md)
- [Solución de problemas — errores, tabla de riesgos, puntos críticos](./references/troubleshooting.md)
- [detect_legacy.py — escáner automatizado](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Kit de inicio de Azure OpenAI](https://aka.ms/openai/start)
- [Documentación API Responses de Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Ciclo de vida de la versión de API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referencia API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->