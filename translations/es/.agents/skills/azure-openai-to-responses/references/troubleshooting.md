# Solución de problemas, tabla de riesgos y advertencias

## Solución de problemas 400s

| Error | Solución |
|-------|---------|
| `missing_required_parameter: tools[0].name` | La definición de la herramienta usa el formato anidado antiguo de Chat Completions | Aplanar de `{"type": "function", "function": {"name": ...}}` a `{"type": "function", "name": ..., "parameters": ...}` — nombre, descripción y parámetros van a nivel superior |
| `unknown_parameter: input[N].tool_calls` | Los resultados de herramientas en múltiples turnos usan formato antiguo de Chat Completions | Reemplazar `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` con ítems de `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Herramienta con `strict: true` sin arreglo `required` | Cuando `strict: true`, todas las propiedades deben estar listadas en `required` y debe establecerse `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Herramienta con `strict: true` sin `additionalProperties: false` | Añadir `"additionalProperties": false` al objeto de parámetros |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | El ID de llamada a función few-shot tiene prefijo incorrecto | Los IDs de llamada a función deben comenzar con `fc_` (ej. `fc_example1`), no con `call_` |
| `missing_required_parameter: text.format.name` | Añadir clave `"name"` al diccionario de formato (ej., `"name": "Output"`) |
| `invalid_type: text.format` | Asegurarse de que `text.format` sea un diccionario con llaves `type`, `name`, `strict`, `schema` — no una cadena |
| `invalid input content type` | Usar tipos de contenido `input_text`/`output_text` en lugar de Chat `text` |
| `invalid input content type` (imagen) | El contenido de imagen aún usa `"type": "image_url"` | Cambiar a `"type": "input_image"` |
| `Expected object, got string` en `image_url` | `image_url` sigue como objeto anidado `{"url": "..."}` | Aplanar a cadena simple: `"image_url": "https://..."` o `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` para `max_output_tokens` | El mínimo es **16** en Azure OpenAI. Usar 50+ para pruebas, 1000+ para producción. |
| `429 Too Many Requests` durante streaming | Limitación de tasa. Envolver el streaming en `try/except`, enviar JSON de error al frontend, implementar retroceso/reintento. |
| `KeyError: 'innererror'` en error de filtro de contenido | La estructura del cuerpo de error del filtro de contenido cambió en Responses API | Chat Completions usaba `error.body["innererror"]["content_filter_result"]`; Responses API usa `error.body["content_filters"][0]["content_filter_results"]` (plural, dentro de una matriz). Reescribir todos los accesos a `innererror`. |

---

## Tabla de riesgo de migración

| Síntoma | Error probable | Solución |
|---------|---------------|----------|
| `output_text` vacío / respuesta truncada | `max_output_tokens` muy bajo para modelos de razonamiento | Establecer `max_output_tokens=1000` o más — los tokens de razonamiento cuentan contra el límite |
| `400 invalid_type: text.format` | Se pasó cadena `response_format` en lugar del dict `text.format` | Usar `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` en `/openai/v1/responses` | `base_url` incorrecto — falta sufijo `/openai/v1/` | Asegurar `base_url=f"{endpoint}/openai/v1/"` (con barra final) |
| `401 Unauthorized` tras cambiar a `OpenAI()` | `api_key` no configurada o proveedor de token no pasado correctamente | Para EntraID: `api_key=token_provider` (llamable). Para clave API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| El modelo devuelve `deployment not found` | El parámetro `model` no coincide con el nombre de despliegue de Azure | Usar `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — este es el nombre de despliegue, no el nombre del modelo |
| `json.loads(resp.output_text)` lanza `JSONDecodeError` | No se aplicó esquema o el modelo no soporta JSON estricto | Asegurar `"strict": True` en el esquema y verificar soporte del modelo para salida estructurada |
| El streaming no devuelve eventos `delta` | Se está verificando tipo de evento incorrecto | Filtrar por `event.type == "response.output_text.delta"`, no por Chat `chat.completion.chunk` |
| Error 400 en entrada de imagen tras migración | Tipo de contenido de imagen no actualizado | Cambiar `"type": "image_url"` → `"type": "input_image"` y aplanar `"image_url": {"url": "..."}` → `"image_url": "..."` (cadena simple) |
| Las llamadas a herramientas entran en bucle infinito | Falta resultado de herramienta en el `input` de seguimiento | Después de ejecutar una herramienta, añadir un ítem `{"type": "function_call_output", "call_id": ..., "output": ...}` al `input` en la siguiente solicitud |
| Error `temperature` con GPT-5 o serie o | Valor explícito de `temperature` distinto de 1 | Eliminar `temperature` o establecer en `1` para modelos GPT-5 y serie o (o1, o3-mini, o3, o4-mini) |
| Error `top_p` con serie o | `top_p` no soportado | Eliminar `top_p` cuando se usan modelos de serie o |
| `max_completion_tokens` no reconocido | Uso de parámetro específico de Azure | Reemplazar `max_completion_tokens` por `max_output_tokens`. Establecer en 4096+ para serie o (los tokens de razonamiento cuentan contra el límite). |
| Salida vacía/truncada de serie o | `max_output_tokens` muy bajo | Serie o usa tokens de razonamiento internamente. Establecer `max_output_tokens=4096` o más — no 500–1000. |
| `400 integer_below_min_value` para `max_output_tokens` | Valor menor a 16 | Azure OpenAI exige `max_output_tokens >= 16`. Usar 50+ para pruebas ligeras, 1000+ para producción. |
| `429 Too Many Requests` a mitad del streaming | Límite de tasa de Azure OpenAI | El streaming se rompe silenciosamente sin manejo de errores. Siempre envolver el `async for event in await coroutine:` en `try/except` y enviar `{"error": str(e)}` al frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant incorrecto o no ha iniciado sesión | Pasar `tenant_id=os.getenv("AZURE_TENANT_ID")` explícitamente. Ejecutar localmente `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` usando modelos GitHub (`models.github.ai`) | Los modelos GitHub no soportan Responses API | Eliminar completamente el código para modelos GitHub. Usar Azure OpenAI, OpenAI o un endpoint local compatible (ej., Ollama con soporte Responses). |
| MAF `OpenAIChatCompletionClient` aún usa Chat Completions | Uso del cliente MAF antiguo en 1.0.0+ | En MAF 1.0.0+, `OpenAIChatClient` usa Responses API por defecto. Reemplazar `OpenAIChatCompletionClient` por `OpenAIChatClient`. Para versiones anteriores a 1.0.0, actualizar a `agent-framework-openai>=1.0.0`. |
| El agente LangChain devuelve vacío o falla con llamadas a herramientas | `ChatOpenAI` no usa Responses API | Añadir `use_responses_api=True` a `ChatOpenAI(...)`. También cambiar `.content` → `.text` en mensajes de respuesta. |
| `KeyError: 'innererror'` en manejador de error del filtro de contenido | Cambió la estructura del cuerpo de error en Responses API | Reescribir `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. El envoltorio `innererror` desapareció; los detalles del filtro de contenido ahora están en un array superior `content_filters` con `content_filter_results` (plural) dentro de cada entrada. |
| Llamada HTTP cruda a `/openai/deployments/.../chat/completions` devuelve 404 | Endpoint REST antiguo de Chat Completions | Reescribir la URL a `/openai/v1/responses`. Cambiar cuerpo de la solicitud: `messages` → `input`, añadir `max_output_tokens` + `store: false`, eliminar parámetro query `api-version`. Cambiar análisis de respuesta: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` es una propiedad de conveniencia del SDK, no está en el JSON REST crudo). |

---

## Advertencias

1. Si antes usaba Chat Completions para el estado de conversación, maneje su propio estado explícitamente con Responses.
2. Prefiera `max_output_tokens` sobre el legado `max_tokens`.
3. Al migrar a `gpt-5`, asegúrese de que `temperature` no esté especificado o esté establecido en `1`.
4. Reemplace Chat `content[].type: "text"` por Responses `content[].type: "input_text"` para entradas de usuario/sistema.
5. Para `text.format`, proporcione un diccionario apropiado (ej., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), no una cadena simple.
6. El parámetro `seed` no es compatible en Responses; elimínelo de las solicitudes.
7. **Razonamiento**: Incluya `reasoning` solo si el código original ya lo usaba. No añada `reasoning` a llamadas API que no lo tenían — muchos modelos sin razonamiento no lo soportan.
8. **Dimensionamiento de `max_output_tokens`**: Para modelos de razonamiento (GPT-5-mini, GPT-5, serie o), use `max_output_tokens=4096` o más — no 50–1000. El modelo usa tokens de razonamiento internamente antes de generar salida visible; límites demasiado bajos causan respuestas truncadas o vacías.
9. **`max_completion_tokens` para serie o**: Si el código original usaba `max_completion_tokens` (específico de Azure para serie o), reemplácelo por `max_output_tokens`. Responses API no acepta `max_completion_tokens`.
10. **`reasoning_effort` para serie o**: Si el código original usa `reasoning_effort` (bajo/medio/alto), migre a `reasoning={"effort": "<valor>"}` en la llamada a Responses API.
11. **Retraso en streaming de serie o**: Los modelos serie o realizan razonamiento interno antes de generar salida. Al hacer streaming, espere un retraso más largo antes del primer evento `response.output_text.delta`. Esto es normal — el modelo está razonando, no está colgado.
9. **`_azure_ad_token_provider` desapareció**: `AsyncOpenAI` / `OpenAI` no tienen atributo `_azure_ad_token_provider`. Las pruebas o código que accedan a este atributo fallarán con `AttributeError`. El proveedor de token se pasa como `api_key` y no es inspeccionable en el objeto cliente.
10. **Archivos snapshot / golden**: Si la suite de pruebas usa pruebas snapshot, **todos** los archivos snapshot que contengan formas de streaming de Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, etc.) deben actualizarse a la nueva forma de Responses. Esto es fácil de pasar por alto y causa fallos en las aserciones de snapshot.
11. **Ruta de monkeypatch mock**: El destino del monkeypatch cambia de `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (o `Responses.create` para sincronía). Usar la ruta antigua no hace nada silenciosamente — el mock no interceptará y las pruebas usarán la API real o fallarán.
12. **`input` no `messages`**: Las funciones mock deben leer `kwargs.get("input")` no `kwargs.get("messages")`. Responses API usa `input` para el historial de conversación.
13. **Nomenclatura variable de entorno**: Azure Identity SDK usa `AZURE_CLIENT_ID` (no `AZURE_OPENAI_CLIENT_ID`) para `ManagedIdentityCredential(client_id=...)`. Renombre en pruebas, archivos `.env`, configuraciones de app y Bicep/infraestructura.
14. **El mínimo de `max_output_tokens` es 16**: Azure OpenAI rechaza valores menores a 16 con `400 integer_below_min_value`. Use 50 para pruebas ligeras, 1000+ para producción. El antiguo `max_tokens` no tenía mínimo.
15. **`tenant_id` para `AzureDeveloperCliCredential`**: Cuando el recurso Azure OpenAI está en un tenant diferente, **debe** pasar `tenant_id` explícitamente — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Sin esto, la credencial usa silenciosamente el tenant incorrecto y devuelve `401`.
16. **Los límites de tasa se manifiestan diferente en streaming**: Con Chat Completions, un 429 normalmente impedía iniciar el stream. Con Responses API streaming, un 429 puede ocurrir **a mitad del stream** — el iterador asíncrono lanza una excepción. Siempre envolver el bucle de streaming en `try/except` y emitir una línea JSON de error para que el frontend lo maneje con gracia.

17. **El manejo de errores en streaming es obligatorio para aplicaciones web**: El patrón `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` es fundamental. Sin él, el stream SSE/JSONL muere silenciosamente ante cualquier error en el servidor y el frontend queda colgado.
18. **Las definiciones de herramientas deben usar formato plano**: La API de Responses espera `{"type": "function", "name": ..., "parameters": ...}` — no el formato anidado de Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Este es el error más común al migrar código que llama funciones.
19. **`pydantic_function_tool()` es incompatible**: El helper `openai.pydantic_function_tool()` todavía genera el formato antiguo anidado. No lo uses con `responses.create()`. Define los esquemas de herramientas manualmente o aplana la salida.
20. **Los resultados de herramienta usan `function_call_output`, no `role: tool`**: Después de ejecutar una herramienta, agrega `{"type": "function_call_output", "call_id": ..., "output": ...}` — no `{"role": "tool", "tool_call_id": ..., "content": ...}`. Para la solicitud de herramienta del asistente, usa `messages.extend(response.output)` — no un dict manual `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` requiere `required` + `additionalProperties: false`**: Al usar `strict: true` en una herramienta, cada propiedad debe estar listada en el array `required` y `additionalProperties` debe ser `false`. Faltar cualquiera causa un error 400.
22. **Los IDs de llamada de función tienen prefijos específicos**: Cuando se proveen ítems `function_call` en `input` (few-shot), el campo `id` debe comenzar con `fc_` y el campo `call_id` debe comenzar con `call_` (ejemplo: `"id": "fc_example1", "call_id": "call_example1"`). Usar el prefijo viejo `call_` para `id` en Chat Completions es rechazado.
23. **GitHub Models no soporta la API de Responses**: Si la app tiene una ruta de código para GitHub Models (`base_url` apuntando a `models.github.ai` o `models.inference.ai.azure.com`), elimínala por completo. No existe ruta de migración — cambia a Azure OpenAI, OpenAI o un endpoint local compatible.
24. **La estructura del cuerpo de error del filtro de contenido cambió**: Los errores de Chat Completions usaban `error.body["innererror"]["content_filter_result"]` (singular). Los errores de la API de Responses usan `error.body["content_filters"][0]["content_filter_results"]` (plural, dentro de un arreglo). La clave `innererror` ya no existe. El código que acceda directamente a `innererror` lanzará `KeyError` en tiempo de ejecución — esto es fácil pasar por alto al migrar ya que solo ocurre cuando se activa el filtro de contenido. Siempre busca `innererror` durante la migración.
25. **Las llamadas HTTP en bruto necesitan reescribir URL + cuerpo**: Las apps que llamen directamente el REST de Azure OpenAI (usando `requests`, `httpx`, `aiohttp`) con `/openai/deployments/{name}/chat/completions?api-version=...` deben cambiar a `/openai/v1/responses`. El cuerpo de la petición usa `input` en lugar de `messages`, requiere `max_output_tokens` y `store`, y se elimina el parámetro de consulta `api-version`. El texto en la respuesta está en `output[0].content[0].text` — **no** en `output_text`, que es una propiedad de conveniencia del SDK ausente en el JSON REST crudo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->