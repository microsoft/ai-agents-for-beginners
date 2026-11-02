# Registro de cambios

Todos los cambios notables en el curso **Agentes de IA para Principiantes** están documentados en este archivo.

## [Publicado] — 2026-07-14

Esta versión transfiere el curso de dos modelos recién obsoletos, migra los cuadernos restantes de la Lección al API estable de Microsoft Agent Framework, y valida los cuadernos de Python contra un despliegue activo de Microsoft Foundry.

### Cambios

- **Se movió fuera de modelos obsoletos (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Tanto `gpt-4.1` como `gpt-4.1-mini` están ahora obsoletos (fecha de retiro publicada **14 de octubre de 2026**). Se reemplazó cada referencia del curso (documentación, `.env.example`, cuadernos y ejemplos en Python/.NET) con el `gpt-5-mini` no obsoleto. El ejemplo de enrutamiento de modelo de la Lección 16 mantiene un contraste pequeño/grande usando `gpt-5-nano` (pequeño) y `gpt-5-mini` (grande). Los archivos de terceros incluidos ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), el texto histórico de GitHub Models y las notas de capacidad de la habilidad `azure-openai-to-responses` quedaron intencionadamente sin cambios.
- **El cuaderno de entrega de la Lección 14 fue migrado al API estable.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) ahora usa `agent_framework.orchestrations.HandoffBuilder` con `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming basado en `event.type`, y `FoundryChatClient` (reemplazando los símbolos removidos pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **El cuaderno de interacción humana de la Lección 14 fue migrado al API estable.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) ahora pausar vía `ctx.request_info(...)` + `@response_handler` (reemplazando `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), construye con `WorkflowBuilder(start_executor=..., output_executors=[...])`, procesa salida estructurada mediante `default_options={"response_format": ...}`, y usa una respuesta guionizada para que el cuaderno funcione sin supervisión (sin bloquear con `input()`).
- **Configuración del entorno** ([.env.example](../../.env.example)): se cambiaron los nombres de despliegue del modelo a `gpt-5-mini`; se agregaron `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (enrutamiento de la Lección 16) y el previamente ausente `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (uso del navegador en la Lección 15).
- **Dependencias** ([requirements.txt](../../requirements.txt)): se fijaron las versiones de `agent-framework`, `agent-framework-foundry` y `agent-framework-openai` a `~=1.10.0` para un conjunto validado y autoconsistente (la versión 1.11.0 incluye cambios experimentales que rompen las interfaces que usan estas lecciones).

### Notas y limitaciones conocidas

- **Validado contra Microsoft Foundry en vivo.** Los cuadernos de Python se ejecutaron sin cabeza con `nbconvert` contra un proyecto Microsoft Foundry usando `gpt-5-mini` (y `gpt-5-nano` para el enrutamiento de la Lección 16). Despliegue modelos equivalentes no obsoletos en su propio proyecto; los cuadernos leen el nombre de despliegue de `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Todavía requiere recursos adicionales para algunas lecciones.** La Lección 05 necesita Azure AI Search; el flujo de trabajo Bing-grounding de la Lección 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) necesita conexión a Bing y herramientas alojadas en Microsoft Foundry Agent Service; las Lecciones 13 (Cognee) y 17 (Foundry Local) necesitan sus propios entornos de ejecución.

## [Publicado] — 2026-07-13

Esta versión añade dos nuevas lecciones que completan el arco de despliegue — escalando agentes a Microsoft Foundry y reduciéndolos a una sola estación de trabajo — además de una canalización de prueba rápida, navegación del curso renovada, nuevas habilidades para los estudiantes y una marca actualizada.

### Añadidos

- **Lección 16 — Desplegando Agentes Escalables con Microsoft Foundry.** Nueva lección [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) y cuaderno ejecutable [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) construyendo un agente de soporte al cliente en producción (herramientas, RAG, memoria, enrutamiento de modelo, cacheo de respuestas, aprobación humana, una puerta de evaluación y trazado con OpenTelemetry), con diagramas Mermaid de desarrollo/despliegue/ejecución, un chequeo de conocimiento, una tarea y un reto.
- **Lección 17 — Creando Agentes Locales de IA con Foundry Local y Qwen.** Nueva lección [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) y cuaderno [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) construyendo un asistente de ingeniería completamente en dispositivo (llamadas a funciones de Qwen vía Foundry Local, herramientas en sandbox para archivos, RAG local con Chroma, MCP local opcional), con diagramas solo-local / local-RAG / llamadas a herramientas, un chequeo de conocimiento, una tarea y un reto.
- **Canalización de prueba rápida.** Nuevo flujo de trabajo [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) más catálogos por lección bajo [tests/](./tests/README.md) para los agentes desplegables de las Lecciones 01, 04, 05 y 16, con un README índice que mapea cada catálogo a su lección y nombre de agente alojado. La Lección 16 gana una sección "Validando un Agente Desplegado con Pruebas Rápidas"; Las Lecciones 01/04/05 ganan un puntero opcional a la prueba rápida.
- **Habilidades para estudiantes.** Nuevas Habilidades de Agente bajo `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (empaquetando la guía de las Lecciones 16 y 17), y [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (cómo validar los ejemplos de cuadernos contra una configuración activa de Microsoft Foundry / Azure OpenAI).
- **Ejecutor de validación de cuadernos.** Nuevo [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) que ejecuta cada cuaderno de Python sin cabeza con `nbconvert` y muestra una matriz PASS/FAIL (más `results.json`). Detecta automáticamente la raíz del repositorio y Python, excluye por defecto cuadernos no del curso (`.venv`, `site-packages`, `translations`, recursos de plantilla de habilidades) y cuadernos `.NET`, y soporta `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, y `-Python`.
- **Navegación del curso.** Se añadieron enlaces de lección anterior/siguiente a las Lecciones 11–15 (antes ausentes) para que todo el curso enlace 00 → 18 en ambas direcciones.
- **Nuevas miniaturas.** Miniaturas para las Lecciones 16 y 17, más una imagen social renovada del repositorio [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (ahora publicitando las dos nuevas lecciones y la URL `aka.ms/ai-agents-beginners`).
- **Dependencias** ([requirements.txt](../../requirements.txt)): añadidos `foundry-local-sdk` y `chromadb` para la Lección 17.

### Cambios

- **Tabla de lecciones principal en [README.md](./README.md)**: las Lecciones 16 y 17 ahora enlazan a su contenido (antes “Próximamente”); imagen del repositorio actualizada a `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: añadidas las Lecciones 16 y 17 a la guía lección por lección y los caminos de aprendizaje, y una sección "Validando Agentes Desplegados con Pruebas Rápidas".
- **[AGENTS.md](./AGENTS.md)**: actualizado el conteo y descripción de lecciones (00–18), añadida una sección de validación con pruebas rápidas, y ejemplos de nombres para las muestras de las Lecciones 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Lección Anterior" ahora apunta a la Lección 17 (antes Lección 15), cerrando la cadena.
- **Referencias estandarizadas a modelos no obsoletos.** Se reemplazaron todas las referencias a `gpt-4o` / `gpt-4o-mini` en el curso (documentación, `.env.example`, cuadernos y ejemplos en Python/.NET) por `gpt-4.1-mini` — `gpt-4o` (todas las versiones) se retira en 2026. El ejemplo de enrutamiento de modelo de la Lección 16 mantiene un contraste pequeño/grande usando `gpt-4.1-mini` (pequeño) y `gpt-4.1` (grande). Los cuadernos de Python ahora seleccionan el modelo desde las variables de entorno (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) en lugar de codificar un nombre de modelo.

### Notas y limitaciones conocidas

- **No ejecutado contra Azure en vivo.** Los cuadernos de las nuevas lecciones son muestras educativas; ejecútelos y valídelos en su propia configuración de Microsoft Foundry / Foundry Local. El flujo de trabajo de prueba rápida requiere que despliegue el agente de la lección y configure secretos Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) con rol de **Usuario Azure AI** en el ámbito del proyecto Foundry.
- **La Lección 17 es solo local.** No tiene punto final de Foundry Responses, por lo que la acción de prueba rápida no se aplica; validela ejecutando el cuaderno en su estación de trabajo.

## [Publicado] — 2026-07-06

Esta versión migra el curso al **Azure OpenAI Responses API**, estandariza la nomenclatura del producto en **Microsoft Foundry** y el **Microsoft Agent Framework (MAF)**, retira GitHub Models, actualiza las versiones del SDK, y agrega nuevo contenido sobre modelos locales y hospedaje de otros frameworks en Foundry.

### Añadidos

- **Habilidad de migración** — Instaló la Habilidad de Agente [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (desde [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) bajo `.agents/skills/`, incluyendo sus referencias y script de escaneo.
- **Foundry Local (ejecutar modelos en dispositivo)** — Nueva sección "Proveedor Alternativo: Foundry Local" en [00-course-setup/README.md](./00-course-setup/README.md) cubriendo instalación (`winget` / `brew`), `foundry model run`, el `foundry-local-sdk`, y la integración de `FoundryLocalManager` con Microsoft Agent Framework a través de `OpenAIChatClient`.
- **Hospedaje de agentes LangChain / LangGraph en Microsoft Foundry** — Nueva sección en [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) más ejemplo ejecutable [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) usando `langchain-azure-ai[hosting]` y `ResponsesHostServer` (el protocolo `/responses`), basado en [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nueva sección "Ejemplo del Mundo Real: Microsoft Project Opal" en [15-browser-use/README.md](./15-browser-use/README.md) presentando a Opal como agente empresarial de uso de computadora y mapeándolo a conceptos del curso (interacción humana, confianza/seguridad, planificación, Habilidades).
- **Segundo ejemplo de Python para la Lección 02** — Añadido [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (ver "Cambios" — migrado desde el cuaderno anterior Semantic Kernel) y enlazado en el README de la lección.
- Sección **Modelos y Proveedores** añadida a [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Cambios

- **Chat Completions → Responses API (Python).** Las muestras que llamaban directamente al modelo fueron migradas de Chat Completions a la Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), usando el cliente `OpenAI` contra el endpoint estable Azure OpenAI `/openai/v1/` (sin `api_version`). Las muestras afectadas incluyen:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04/tool-use/README.md) — el recorrido completo para llamadas a funciones (esquema de herramientas adaptado al formato Responses, resultados de herramientas retornados como `function_call_output`, `max_output_tokens`, etc.).

- **Modelos de GitHub → Azure OpenAI.** Los modelos de GitHub están obsoletos (se retirarán en **julio de 2026**) y no son compatibles con la API de Respuestas. Todas las rutas de código de los modelos de GitHub se convirtieron a Azure OpenAI / Microsoft Foundry en muestras de Python y .NET:
  - Python: cuadernos de flujo de trabajo de la Lección 08 (`01`–`03`), Lección 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + documentos complementarios `.md`, y los cuadernos/`.md` de flujo de trabajo dotNET de la Lección 08 (`01`–`03`) ahora usan `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` con `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** El antiguo `02-semantic-kernel.ipynb` fue reescrito para usar el Microsoft Agent Framework con Azure OpenAI (API de Respuestas) y renombrado a `02-python-agent-framework-azure-openai.ipynb`.
- **Estandarizado en `FoundryChatClient` + `as_agent`.** El README y el código de los cuadernos que referenciaban `AzureAIProjectAgentProvider` se estandarizaron en el patrón canónico usado por la Lección 01 y las propias muestras del framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` con `provider.as_agent(...)`. Actualizado en los READMEs y cuadernos de la Lección 02–14 (por ejemplo, la memoria de la Lección 13, todos los cuadernos de la Lección 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Nombres de productos.** Renombrado en todo el contenido en inglés:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Sin cambios: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", y nombres de variables de entorno.)
- **Dependencias** ([requirements.txt](../../requirements.txt)):
  - Fijado `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fijado `openai>=1.108.1` (mínimo para la API de Respuestas).
  - Eliminado `azure-ai-inference` (solo se usaba en las muestras migradas de los Modelos de GitHub).
- **Configuración del entorno** ([.env.example](../../.env.example)): eliminadas variables de los Modelos de GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); añadidas `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` y opcional `AZURE_OPENAI_API_KEY`; actualizado el nombre a Microsoft Foundry.
- **Documentación** — Actualizados [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) y [STUDY_GUIDE.md](./STUDY_GUIDE.md) para lo anterior (variables de entorno de configuración, fragmento de verificación, guía de proveedor, nombres).

### Eliminado

- Pasos de incorporación de Modelos de GitHub y variables de entorno en la documentación de configuración (reemplazados por Azure OpenAI / Microsoft Foundry).

### Seguridad / Privacidad (limpieza para compartición pública)

- Borrados resultados de ejecución de cuadernos Jupyter que filtraban un real **ID de suscripción de Azure**, nombres de grupos de recursos / recursos, e ID de conexión de Bing, además de rutas locales de archivos y nombres de usuario de desarrolladores, en:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verificado que no permanezcan claves API, tokens, IDs de suscripción o rutas personales en el contenido en inglés rastreado (las referencias a `GITHUB_TOKEN` que quedan son el token de GitHub Actions en flujos de trabajo y el PAT del servidor GitHub MCP en la configuración de la Lección 11 — ambos legítimos y no relacionados con Modelos de GitHub).

### Notas y limitaciones conocidas

- **No ejecutados/compilados.** Son muestras educativas actualizadas para la corrección de API/nombres; no se ejecutaron contra recursos reales de Azure, y las muestras .NET no se compilaron en este entorno. Valide con su propio despliegue de Microsoft Foundry / Azure OpenAI.
- **El despliegue del modelo debe soportar la API de Respuestas.** Use un despliegue como `gpt-4.1-mini`, `gpt-4.1`, o un modelo `gpt-5.x`. Los modelos antiguos soportan la funcionalidad básica de Respuestas pero no todas las características.
- **Versión de agent-framework.** Las muestras apuntan a la versión más reciente de MAF (`>=1.10.0`). La llamada canónica para la creación del agente es `client.as_agent(...)`; las APIs se validaron con la documentación publicada del framework y una compilación instalada. Si fija una versión distinta, confirme la disponibilidad del método (`as_agent` vs `create_agent`).
- **Cuaderno del flujo de trabajo de la Lección 08, número 04** mantiene intencionadamente `AzureAIAgentClient` (de `agent-framework-azure-ai`) porque usa herramientas alojadas del Microsoft Foundry Agent Service (fundamentación Bing, intérprete de código); ya está basado en Respuestas.
- **Despliegue predeterminado en .NET.** Dos muestras de flujo de trabajo dotNET de la Lección 08 tenían antes un modelo específico codificado; ahora usan por defecto `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Si una muestra requiere entrada multimodal/visión, configure `AZURE_OPENAI_DEPLOYMENT` con un modelo adecuado.
- **Foundry Local** expone un punto final compatible con OpenAI para **Chat Completions** y está pensado para desarrollo local; use Azure OpenAI / Microsoft Foundry para el conjunto completo de características de la API de Respuestas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->