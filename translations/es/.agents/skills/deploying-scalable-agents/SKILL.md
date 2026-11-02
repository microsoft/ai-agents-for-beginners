---
name: deploying-scalable-agents
license: MIT
---
# Desplegando Agentes Escalables con Microsoft Foundry

> Habilidad complementaria para [Lección 16 – Desplegando Agentes Escalables](../../../16-deploying-scalable-agents/README.md).
> Úsala para ayudar a un aprendiz a mover un agente desde el prototipo hasta un despliegue de producción escalable y observable.
> Fundamenta cada recomendación en el contenido de la lección y
> el cuaderno ejecutable; no inventes APIs de Foundry.

## Desencadenantes

Activa esta habilidad cuando un aprendiz quiera:
- Desplegar un agente en Microsoft Foundry como un **agente alojado** y hacerlo versionado/observable.
- Elegir entre los patrones de despliegue **cliente-alojado, agente alojado y flujo de trabajo de agentes**.
- Añadir **enrutamiento de modelo**, **caché de respuestas** o **concurrencia limitada** para controlar la latencia y el coste.
- Añadir una **puerta de evaluación** para que una versión mala del agente no se despliegue.
- Añadir un paso de **aprobación humana en el ciclo** para acciones de alto riesgo.
- Instrumentar un agente con **OpenTelemetry** para trazabilidad y observabilidad en producción.
- **Prueba rápida** (smoke-test) a un agente desplegado como una puerta rápida tras el despliegue.

## Modelo mental central

Un agente en producción es mayormente el esqueleto operativo *alrededor* del modelo (~80%),
no el modelo en sí. Mapear cada recomendación a una de estas preocupaciones:

| Preocupación | Prototipo → Producción |
|------------|------------------------|
| Alojamiento | cuaderno → servicio alojado versionado |
| Identidad | tu `az login` → identidad administrada + RBAC con alcance |
| Estado | en memoria → almacén externo de hilos/memoria |
| Fallos | rastreo de errores → reintentos, respaldos, alertas |
| Coste | "unos pocos centavos" → seguimiento, enrutamiento, caché, presupuesto |
| Calidad | revisión visual → puerta de evaluación automatizada |
| Confianza | aprobación tuya → política + humano en el ciclo |

## Patrones de despliegue (elige uno o combina)

1. **Cliente-alojado** — el ciclo de razonamiento se ejecuta en tu proceso. Control máximo; tú gestionas escalado/estado.
2. **Agente alojado (Foundry Agent Service)** — Foundry aloja el ciclo, almacena hilos, aplica RBAC/seguridad de contenido, muestra el agente en el portal. Menos control, mucho menos superficie operativa.
3. **Flujo de trabajo de agentes** — múltiples agentes/herramientas compuestos en un grafo con ramificaciones, nodos de aprobación y puntos de control duraderos.

## Ciclo de vida (el ciclo que despliega un agente)

`crear → versionar → evaluar (puerta) → desplegar alojado → observar en línea → recopilar fallos → repetir`.
**La evaluación offline es una puerta, no un pensamiento secundario** — una versión no se despliega
salvo que supere el umbral. La observabilidad online retroalimenta
los fallos reales al conjunto de pruebas offline.

## Palancas para escala y coste (en orden de prioridad)

1. **Ajustar el tamaño del modelo** — usar el modelo más pequeño que pase la puerta de evaluación.
2. **Enrutar según complejidad** — modelo pequeño/rápido para peticiones simples, modelo grande para razonamiento real (clasificador DIY o Foundry Model Router).
3. **Caché** — servir peticiones casi idénticas sin llamar al modelo.
4. **Diseño sin estado + concurrencia limitada** — externalizar estado; reintentar con retroceso exponencial.

## Patrones clave para reproducir

Dirige al aprendiz hacia estos desde el cuaderno
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Manejador de solicitudes**: caché → enrutar según complejidad → trazar span → ejecutar → caché.
- **Puerta de evaluación**: puntuar un conjunto de pruebas offline; devolver `pass_rate >= threshold` y solo desplegar si es verdadero.
- **Aprobación humana**: `@tool(approval_mode="always_require")` para acciones como grandes reembolsos.
- **Trazabilidad**: envolver cada solicitud en `tracer.start_as_current_span(...)` y establecer atributos como `routed.model`, `customer.id`.

## Prueba rápida (smoke-test) a un agente desplegado

Tras desplegar, verifica que el endpoint realmente responde (un despliegue exitoso puede aún estar
silencioso). Usa la acción [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
vía [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
con el catálogo en [`tests/`](../../../tests/README.md). El ejecutor envía mediante POST cada
prompt a `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
y comprueba el texto de la respuesta. La identidad necesita el rol de **Azure AI User** en
el ámbito del proyecto Foundry; la audiencia del token debe ser `https://ai.azure.com/`.

Superpone las puertas: **prueba rápida** (accesible/respondiente, en cada despliegue) → **evaluación offline** (lo suficientemente bueno para desplegar, antes de promoción) → **evaluación online** (cómo está funcionando en producción, continuo).



## Controles empresariales

- **RBAC**: asigna a cada agente alojado una identidad administrada con privilegios mínimos.
- **MCP en producción**: trata cada servidor MCP como un límite no confiable — fija la versión, limita su identidad, valida salidas, limita tasa, nunca expongas secretos.

## Barreras para el asistente

- Prefiere el patrón canónico `FoundryChatClient(...)` + `provider.as_agent(...)` usado en todo el curso.
- No prometas resultados en vivo de Azure que no hayas verificado; recomienda el flujo de trabajo de prueba rápida para confirmar un despliegue.
- Mantén la evaluación y el consejo de coste ligados: la evaluación fija el suelo de calidad, el enrutamiento/caché mantiene el coste cerca de ese suelo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->