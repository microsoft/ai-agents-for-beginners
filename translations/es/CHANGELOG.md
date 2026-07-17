# Registro de cambios

Todos los cambios notables en el curso **Agentes IA para Principiantes** están documentados en este archivo.

## [Publicado] — 2026-07-13

Esta versión añade dos nuevas lecciones que completan el arco de despliegue — escalando agentes hacia Microsoft Foundry y reduciéndolos a una sola estación de trabajo — además de una canalización de prueba rápida, navegación renovada del curso, nuevas habilidades para aprendices y marca actualizada.

### Añadido

- **Lección 16 — Desplegando Agentes Escalables con Microsoft Foundry.** Nueva lección [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) y cuaderno ejecutable [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) construyendo un agente de soporte al cliente en producción (herramientas, RAG, memoria, enrutamiento de modelos, caché de respuestas, aprobación humana, puerta de evaluación y rastreo OpenTelemetry), con diagramas Mermaid para desarrollo/despliegue/ejecución, un control de conocimiento, una tarea y un desafío.
- **Lección 17 — Creando Agentes IA Locales con Foundry Local y Qwen.** Nueva lección [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) y cuaderno [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) construyendo un asistente de ingeniería completamente en dispositivo (llamadas a funciones Qwen mediante Foundry Local, herramientas de archivos en sandbox, RAG local con Chroma, MCP local opcional), con diagramas solo local / local-RAG / llamada a herramientas, control de conocimiento, tarea y desafío.
- **Canalización de prueba rápida.** Nuevo flujo de trabajo [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) además de catálogos por lección bajo [tests/](./tests/README.md) para los agentes desplegables en las Lecciones 01, 04, 05 y 16, con un README índice que mapea cada catálogo a su lección y nombre del agente alojado. La Lección 16 gana una sección "Validando un Agente Desplegado con Pruebas Rápidas"; y las Lecciones 01/04/05 un apunte opcional a la prueba rápida.
- **Habilidades para aprendices.** Nuevas Habilidades de Agentes bajo `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (que empaquetan la guía de las Lecciones 16 y 17), y [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (cómo validar los ejemplos de los cuadernos con una configuración viva de Microsoft Foundry / Azure OpenAI).
- **Ejecutor de validación de cuadernos.** Nuevo [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) que ejecuta cada cuaderno Python en modo sin cabeza con `nbconvert` y muestra una matriz de PASÓ/NO PASÓ (más `results.json`). Detecta automáticamente la raíz del repositorio y Python, excluye por defecto cuadernos no del curso (`.venv`, `site-packages`, `translations`, activos de plantilla de habilidades) y cuadernos `.NET`, y soporta `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` y `-Python`.
- **Navegación del curso.** Añadidos enlaces de Lección Anterior/Siguiente a las Lecciones 11–15 (que antes faltaban) para que todo el curso enlace de 00 → 18 en ambas direcciones.
- **Miniaturas nuevas.** Miniaturas para las Lecciones 16 y 17, además de una imagen social del repositorio renovada [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (ahora publicitando las dos nuevas lecciones y la URL `aka.ms/ai-agents-beginners`).
- **Dependencias** ([requirements.txt](../../requirements.txt)): añadidos `foundry-local-sdk` y `chromadb` para la Lección 17.

### Cambiado

- **Tabla principal en [README.md](./README.md)** de lecciones: las Lecciones 16 y 17 ahora enlazan a su contenido (antes "Próximamente"); imagen del repositorio actualizada a `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: añadidas las Lecciones 16 y 17 a la guía detallada y rutas de aprendizaje, y sección "Validando Agentes Desplegados con Pruebas Rápidas".
- **[AGENTS.md](./AGENTS.md)**: actualizados el conteo y descripción de lecciones (00–18), añadida sección de validación con prueba rápida, y ejemplos de nomenclatura para las Lecciones 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Lección Anterior" ahora apunta a la Lección 17 (antes era Lección 15), cerrando la cadena.
- **Modelos estándar en referencias no obsoletas.** Reemplazadas todas las referencias `gpt-4o` / `gpt-4o-mini` en el curso (docs, `.env.example`, cuadernos y ejemplos Python/.NET) por `gpt-4.1-mini` — `gpt-4o` (todas las versiones) se retira en 2026. El ejemplo de enrutamiento de modelos de la Lección 16 mantiene un contraste pequeño/grande usando `gpt-4.1-mini` (pequeño) y `gpt-4.1` (grande). Los cuadernos Python ahora seleccionan el modelo desde variables de entorno (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) en lugar de codificar un nombre de modelo.

### Notas y limitaciones conocidas

- **No ejecutado contra Azure en vivo.** Los cuadernos de las nuevas lecciones son muestras educativas; ejecútelos y valídelos contra su propia configuración de Microsoft Foundry / Foundry Local. El flujo de trabajo de prueba rápida requiere que despliegue el agente de la lección y configure los secretos OIDC de Azure (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) con el rol **Usuario Azure IA** en el alcance del proyecto Foundry.
- **Lección 17 es solo local.** No tiene punto final Foundry Responses, así que la acción de prueba rápida no aplica; valídelo ejecutando el cuaderno en su estación de trabajo.

## [Publicado] — 2026-07-06

Esta versión migra el curso a la **API Azure OpenAI Responses**, estandariza la nomenclatura de producto en **Microsoft Foundry** y el **Microsoft Agent Framework (MAF)**, retira GitHub Models, actualiza versiones SDK, y añade contenido nuevo sobre modelos locales y hospedaje de otros frameworks en Foundry.

### Añadido

- **Habilidad de migración** — Instaladas la Habilidad de Agente [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (desde [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) bajo `.agents/skills/`, incluyendo sus referencias y el script escáner.
- **Foundry Local (ejecutar modelos en dispositivo)** — Nueva sección "Proveedor Alternativo: Foundry Local" en [00-course-setup/README.md](./00-course-setup/README.md) que cubre la instalación (`winget` / `brew`), `foundry model run`, el `foundry-local-sdk` y conexión del `FoundryLocalManager` con Microsoft Agent Framework vía `OpenAIChatClient`.
- **Hospedaje de agentes LangChain / LangGraph en Microsoft Foundry** — Nueva sección en [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) más un ejemplo ejecutable [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) usando `langchain-azure-ai[hosting]` y `ResponsesHostServer` (protocolo `/responses`), basado en [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nueva sección "Ejemplo Real: Microsoft Project Opal" en [15-browser-use/README.md](./15-browser-use/README.md) presentando Opal como agente empresarial de uso informático y mapeándolo a conceptos del curso (humano en el bucle, confianza/seguridad, planificación, Habilidades).
- **Segundo ejemplo Python en Lección 02** — Añadido [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (ver "Cambiado" — migrado del cuaderno Semantic Kernel anterior) y enlazado en el README de la lección.
- Añadida sección "Modelos y Proveedores" a [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Cambiado

- **Chat Completions → Responses API (Python).** Las muestras que llamaban el modelo directamente se migraron de Chat Completions a Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), usando el cliente `OpenAI` con el endpoint estable de Azure OpenAI `/openai/v1/` (sin `api_version`). Muestras afectadas incluyen:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — la explicación completa de llamadas a funciones (esquema de herramienta aplanado al formato Responses, resultados devueltos como `function_call_output`, `max_output_tokens`, etc.).
- **GitHub Models → Azure OpenAI.** GitHub Models está obsoleto (retiro en **julio 2026**) y no soporta la Responses API. Todas las rutas de código de GitHub Models se convirtieron a Azure OpenAI / Microsoft Foundry en ejemplos Python y .NET:
  - Python: cuadernos de flujo de trabajo Lección 08 (`01`–`03`), Lección 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + docs `.md` complementarios, y cuadernos/`.md` flujo dotNET Lección 08 (`01`–`03`) ahora usan `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` con `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** El cuaderno anterior `02-semantic-kernel.ipynb` fue reescrito para usar Microsoft Agent Framework con Azure OpenAI (Responses API) y renombrado a `02-python-agent-framework-azure-openai.ipynb`.
- **Estandarizado en `FoundryChatClient` + `as_agent`.** El README y código de cuadernos que referenciaban `AzureAIProjectAgentProvider` se estandarizaron al patrón canónico usado por Lección 01 y ejemplos propios del framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` con `provider.as_agent(...)`. Actualizado en los READMEs y cuadernos Lecciones 02–14 (ejemplo: memoria Lección 13, todos los cuadernos Lección 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Nomenclatura de producto.** Renombrados en todo el contenido en inglés:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Sin cambio: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" y nombres de variables de entorno.)
- **Dependencias** ([requirements.txt](../../requirements.txt)):
  - Fijadas `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fijado `openai>=1.108.1` (mínimo para Responses API).
  - Eliminado `azure-ai-inference` (solo usado por muestras migradas de GitHub Models).
- **Configuración de entorno** ([.env.example](../../.env.example)): eliminadas variables de GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); añadidas `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` y opcional `AZURE_OPENAI_API_KEY`; nombres actualizados a Microsoft Foundry.
- **Docs** — Actualizados [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) y [STUDY_GUIDE.md](./STUDY_GUIDE.md) para lo anterior (variables env, fragmento de verificación, guía de proveedor, nomenclatura).

### Eliminado

- Pasos de incorporación y variables de entorno de GitHub Models de la documentación de configuración (reemplazados por Azure OpenAI / Microsoft Foundry).

### Seguridad / Privacidad (limpieza para compartir público)

- Se limpiaron salidas de ejecución de cuadernos Jupyter que filtraban un **ID real de suscripción de Azure**, nombres de grupo de recursos / recurso, ID de conexión Bing, además de **rutas locales y nombres de usuario** del desarrollador, en:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verificado que no quedan claves API, tokens, IDs de suscripción ni rutas personales en el contenido rastreado en inglés (las referencias a `GITHUB_TOKEN` que quedan son el token de GitHub Actions en los flujos de trabajo y el PAT del servidor MCP de GitHub en la configuración de la Lección 11, ambos legítimos y no relacionados con GitHub Models).

### Notas y limitaciones conocidas

- **No ejecutado/compilado.** Estos son ejemplos educativos actualizados para la corrección de API/nombres; no se ejecutaron contra recursos Azure en vivo, y los ejemplos .NET no se compilaron en este entorno. Valide contra su propia implementación de Microsoft Foundry / Azure OpenAI.
- **El despliegue del modelo debe soportar la API de Responses.** Use un despliegue como `gpt-4.1-mini`, `gpt-4.1` o un modelo `gpt-5.x`. Los modelos más antiguos soportan funcionalidades básicas de Responses, pero no todas las características.
- **Versión del agent-framework.** Los ejemplos están orientados a la última versión de MAF (`>=1.10.0`). La llamada canónica para creación de agentes es `client.as_agent(...)`; las APIs se validaron con la documentación publicada del framework y una instalación compilada. Si usa una versión distinta, confirme la disponibilidad del método (`as_agent` vs `create_agent`).
- **Cuaderno de flujo de trabajo de la Lección 08, ejemplo 04** mantiene intencionadamente `AzureAIAgentClient` (de `agent-framework-azure-ai`) porque utiliza herramientas alojadas del Microsoft Foundry Agent Service (fundamento Bing, intérprete de código); ya está basado en Responses.
- **Despliegue predeterminado .NET.** Dos ejemplos de flujos de trabajo dotNET de la Lección 08 codificaban un modelo específico en el código; ahora por defecto usan `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Si un ejemplo requiere entrada multimodal/visión, configure `AZURE_OPENAI_DEPLOYMENT` con un modelo adecuado.
- **Foundry Local** expone un endpoint **Chat Completions** compatible con OpenAI y está destinado para desarrollo local; use Azure OpenAI / Microsoft Foundry para el conjunto completo de características de la API Responses.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->