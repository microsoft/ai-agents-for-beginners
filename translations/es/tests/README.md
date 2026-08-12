# Pruebas de humo para agentes

Esta carpeta contiene **catálogos de pruebas de humo** para los agentes que construyes en el curso.
Una prueba de humo es una verificación rápida y económica de que un **agente alojado desplegado en Microsoft Foundry**
es accesible, responde y sigue sus expectativas básicas de solicitud.
Es un primer filtro, no un reemplazo para la evaluación completa
que aprendes en [Lección 10](../10-ai-agents-production/README.md) y
[Lección 16](../16-deploying-scalable-agents/README.md).

Los catálogos son consumidos por la GitHub Action [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
a través del flujo de trabajo [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Cómo ejecutar

1. **Despliega el agente de la lección** como un agente alojado en Microsoft Foundry (consulta
   la Lección 16 para el flujo de trabajo de despliegue). Anota el **nombre del agente** y el
   **endpoint del proyecto Foundry**.
2. Añade estos secretos al repositorio (Configuración → Secretos y variables → Acciones):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. La identidad federada
   necesita el rol de **Usuario de Azure AI** a nivel de **ámbito del proyecto Foundry**.
3. Desde la pestaña **Acciones**, ejecuta **Pruebas de humo para agentes alojados** y selecciona el
   `tests_file` correspondiente a la lección, luego proporciona el `agent_name` y
   `project_endpoint` correspondientes.

## Catálogo → lección → nombre del agente

| Catálogo | Lección | Desplegar agente como |
|---------|--------|----------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Introducción a Agentes AI](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Uso de herramientas](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – RAG agente](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Desplegando agentes escalables](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## ¿Qué lecciones tienen pruebas de humo?

Las pruebas de humo aplican a lecciones donde **despliegas un agente** cuyas respuestas de texto
pueden ser validadas contra contenido conocido. Las lecciones que son conceptuales, se ejecutan solo localmente
o producen resultados creativos no deterministas están intencionadamente excluidas:

- La **Lección 17 (Creando agentes AI locales)** se ejecuta completamente en tu estación de trabajo con
  Foundry Local y **no** expone un endpoint de respuestas de Foundry, por lo que esta
  acción no aplica. Valídala ejecutando el cuaderno localmente.
- Las lecciones de patrón de diseño y teoría (02, 03, 06, 07, 09, 12) no incluyen un solo
  agente desplegable para realizar pruebas de humo.

## Esquema del catálogo (referencia rápida)

Cada catálogo es un documento JSON con un arreglo `tests` en el nivel superior. Cada entrada envía
un prompt y verifica la respuesta:

| Campo | Significado |
|-------|------------|
| `id` | Identificador único del paso mostrado en el registro. |
| `description` | Propósito legible para humanos. |
| `prompt` | Mensaje enviado al agente. |
| `assertions.status` | Estado HTTP esperado (por defecto 200). |
| `assertions.contains_any` | Pasa si la respuesta contiene alguna de estas subcadenas. |
| `assertions.contains_all` | Pasa si la respuesta contiene todas las subcadenas. |
| `assertions.contains_none` | Pasa si la respuesta no contiene ninguna de estas subcadenas. |
| `save_response_id_as` | Guarda el id de respuesta para un paso multi-turno posterior. |
| `use_previous_response_id` | Envía este turno encadenado a un id de respuesta guardado. |

Las afirmaciones son verificaciones de subcadenas que no distinguen mayúsculas de minúsculas. Consulta la
[documentación de la acción](https://github.com/marketplace/actions/ai-smoke-test) para
el esquema completo, incluyendo recursos de conversación gestionados por Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->