# Desplegando Agentes Escalables con Microsoft Foundry

![Desplegando Agentes Escalables](../../../translated_images/es/lesson-16-thumbnail.d78cace536bc5d50.webp)

Hasta este punto en el curso, has construido agentes que se ejecutan en tu portátil, dentro de un cuaderno, impulsados por `az login` y un puñado de variables de entorno. Esa es exactamente la forma correcta de aprender. No es la forma correcta de ejecutar un agente del que dependan miles de clientes a las 3 a.m.

Esta lección trata sobre la brecha entre "funciona en mi máquina" y "funciona, de forma fiable y asequible, en producción". Cerramos esa brecha usando **Microsoft Foundry** y el **Microsoft Foundry Agent Service**, y lo hacemos construyendo un agente real de soporte al cliente que tiene herramientas, recuperación, memoria, evaluación y monitoreo.

## Introducción

Esta lección cubrirá:

- La diferencia entre un **agente prototipo** y un **agente desplegado**, y por qué la transición se trata principalmente de todo lo que está *alrededor* del modelo.
- **Patrones de despliegue** para agentes: alojado en cliente, alojado en servicio (Hosted Agents) y orquestado por flujo de trabajo.
- El **ciclo de vida del agente** en Microsoft Foundry — crear, versionar, desplegar, evaluar, observar, retirar.
- **Estrategias de escalado**: enrutamiento del modelo, caché, concurrencia y diseño sin estado.
- **Observabilidad** con OpenTelemetry y trazado en Foundry.
- **Optimización de costos** mediante selección de modelo, enrutamiento y puertas de evaluación.
- **Consideraciones empresariales**: gobernanza, aprobación humana, y ejecución segura de servidores MCP en producción.

## Objetivos de Aprendizaje

Tras completar esta lección, sabrás cómo:

- Elegir el patrón de despliegue adecuado para una carga de trabajo determinada del agente.
- Desplegar un agente en el Microsoft Foundry Agent Service para que esté versionado, gobernado y observable.
- Instrumentar un agente para trazado y conectar una canalización de evaluación que se ejecute antes de cada lanzamiento.
- Aplicar enrutamiento y caché de modelo para mantener la latencia y el costo bajo control a escala.
- Añadir una puerta de aprobación humana para acciones de alto riesgo e integrar un servidor MCP de manera segura para producción.

## Prerrequisitos

Esta lección asume que has completado las lecciones anteriores y te sientes cómodo con:

- Construir agentes con el [Microsoft Agent Framework](../14-microsoft-agent-framework/README.md) (Lección 14).
- [Uso de Herramientas](../04-tool-use/README.md) (Lección 4) y [Agentic RAG](../05-agentic-rag/README.md) (Lección 5).
- [Memoria del Agente](../13-agent-memory/README.md) (Lección 13) y [Protocolos Agénticos / MCP](../11-agentic-protocols/README.md) (Lección 11).
- [Observabilidad y Evaluación](../10-ai-agents-production/README.md) (Lección 10) — esta lección se basa directamente en ella.

También necesitarás:

- Una **suscripción de Azure** y un **proyecto Microsoft Foundry** con al menos un modelo de chat desplegado.
- La **CLI de Azure** autenticada (`az login`).
- Python 3.12+ y los paquetes en el repositorio [`requirements.txt`](../../../requirements.txt).

## De Prototipo a Producción: Qué Cambia Realmente

Un agente prototipo y un agente de producción comparten el mismo ciclo básico — razonar, llamar herramientas, responder. Lo que cambia es todo lo que está alrededor de ese ciclo. El modelo es quizás el 20% de un agente de producción; el otro 80% es el esqueleto operativo.

| Aspecto | Prototipo | Producción |
| --- | --- | --- |
| **Alojamiento** | Se ejecuta en tu cuaderno | Se ejecuta como un servicio alojado, versionado y desplegado |
| **Identidad** | Tu token `az login` | Identidad administrada con RBAC con alcance definido |
| **Estado** | En memoria, se pierde al reiniciar | Externalizado (almacén de hilos, servicio de memoria) |
| **Fallas** | Ves el traceback | Reintentos, alternativas, cola de mensajes fallidos, alertas |
| **Costo** | “Son unos pocos centavos” | Rastreado por solicitud, enrutado, almacenado en caché, presupuestado |
| **Calidad** | Revisión visual del resultado | Evaluado automáticamente antes de cada versión |
| **Confianza** | Apruebas cada acción | Política + intervención humana para acciones riesgosas |

Ten presente esta tabla. Cada sección a continuación corresponde a una de estas filas.

## Patrones de Despliegue de Agentes

Hay tres patrones que usarás, a menudo en combinación.

### 1. Agentes alojados en cliente

El objeto agente vive dentro del proceso de *tu* aplicación. Tu código llama directamente al proveedor del modelo; el ciclo de razonamiento se ejecuta en tu servicio. Esto es lo que se ha hecho en todas las lecciones anteriores.

- **Úsalo cuando** necesites control total sobre el ciclo, middleware personalizado o estás insertando el agente dentro de un backend existente.
- **Compromiso**: tú eres responsable del escalado, estado y resiliencia.

### 2. Agentes alojados (Foundry Agent Service)

El agente está *registrado como un recurso* en Microsoft Foundry. Foundry aloja el ciclo de razonamiento, almacena los hilos, aplica la seguridad de contenido y RBAC, y hace visible el agente en el portal de Foundry. Tu aplicación se convierte en un cliente delgado que crea hilos y lee respuestas.

- **Úsalo cuando** quieras durabilidad, observabilidad integrada, gobernanza y menor superficie operativa.
- **Compromiso**: menos control de bajo nivel a cambio de una ejecución gestionada.

### 3. Flujos de trabajo de agentes

Varios agentes (y herramientas) se componen en un grafo con flujo de control explícito — pasos secuenciales, ramificaciones, nodos de aprobación humana y puntos de control duraderos que pueden pausar y reanudar. Esta es la capacidad de **Workflows** del Microsoft Agent Framework aplicada a escala de despliegue.

- **Úsalo cuando** una única tarea abarca varios agentes especializados o requiere un paso de aprobación en medio.
- **Compromiso**: más partes móviles; requiere observabilidad a nivel de orquestación.

```mermaid
flowchart TB
    subgraph P1[Alojado en el Cliente]
        A1[Proceso de tu Aplicación] --> M1[Proveedor del Modelo]
    end
    subgraph P2[Agente Alojado]
        A2[Cliente Ligero] --> F2[Servicio de Agente Foundry]
        F2 --> M2[Modelo + Herramientas + Almacén de Hilos]
    end
    subgraph P3[Flujo de Trabajo del Agente]
        A3[Orquestador] --> S1[Agente de Triaje]
        S1 --> S2[Agente Resolutor]
        S2 --> H[Nodo de Aprobación Humana]
        H --> S3[Agente de Acción]
    end
```

## El Ciclo de Vida del Agente en Microsoft Foundry

Desplegar un agente no es un `push` único. Es un ciclo, y se parece mucho a un ciclo de liberación de software porque eso es exactamente lo que es.

```mermaid
flowchart LR
    Create[Crear / Autor] --> Version[Versión]
    Version --> Evaluate[Evaluar sin conexión]
    Evaluate -->|pasa la puerta| Deploy[Desplegar alojado]
    Evaluate -->|falla la puerta| Create
    Deploy --> Observe[Observar en línea]
    Observe --> Improve[Recopilar fallos]
    Improve --> Create
    Deploy --> Retire[Retirar versión antigua]
```

La idea clave, tomada de la [Lección 10](../10-ai-agents-production/README.md): **la evaluación offline es una puerta, no un pensamiento tardío.** No se lanza una nueva versión del agente a menos que supere los umbrales de evaluación. La observabilidad en línea luego alimenta las fallas del mundo real en tu conjunto de pruebas offline. Ese es todo el ciclo.

## Estrategias de Escalado

Escalar un agente es diferente de escalar una API web sin estado, porque cada solicitud puede disparar múltiples llamadas costosas a modelos y herramientas. Cuatro técnicas soportan la mayoría de la carga.

**Manejo de solicitudes sin estado.** No guardes estado por usuario en la memoria de tu proceso. Persiste los hilos de conversación en el almacén de hilos de Foundry o en un servicio de memoria para que cualquier instancia pueda manejar cualquier solicitud. Esto es lo que permite escalar horizontalmente — agregar instancias, sin sesiones pegajosas.

**Enrutamiento de modelos.** No toda solicitud necesita tu modelo más capaz (y más costoso). Enruta solicitudes simples — clasificación de intención, respuestas factuales cortas — a un modelo pequeño y rápido, y reserva el modelo grande para razonamiento verdadero. El **Model Router** de Foundry puede hacerlo por ti, o puedes implementar un clasificador liviano tú mismo. Construirás la versión DIY en el laboratorio.

**Caché de respuestas.** Muchas consultas de soporte son casi duplicados ("¿cómo restablezco mi contraseña?"). Cachea respuestas a preguntas comunes y sírvelas sin llamar al modelo. Incluso una tasa modesta de aciertos en caché reduce significativamente costo y latencia.

**Concurrencia y presión de retroceso.** Los proveedores de modelos tienen límites de tasa. Limita tu concurrencia, usa reintentos con retroceso exponencial y falla con gracia (una respuesta en cola de "estamos trabajando en ello" es mejor que un 500).

```mermaid
flowchart LR
    Q[Consulta del usuario] --> C{¿Cache hit?}
    C -->|sí| R[Devolver respuesta en caché]
    C -->|no| Router{¿Complejidad?}
    Router -->|simple| SLM[Modelo pequeño]
    Router -->|complejo| LLM[Modelo grande]
    SLM --> Out[Respuesta]
    LLM --> Out
    Out --> Store[Caché + rastro]
```

## Observabilidad en Producción

No puedes operar lo que no puedes ver. Como se cubrió en la Lección 10, el Microsoft Agent Framework emite trazas **OpenTelemetry** de forma nativa — cada llamada a modelo, invocación de herramienta y paso de orquestación se convierte en una span. En producción exportas esas spans a Microsoft Foundry (o cualquier backend compatible con OTel) para poder:

- Rastrear una queja de cliente completa de principio a fin a través de cada llamada a modelo y herramienta.
- Ver la latencia p50/p95 y el costo por solicitud a lo largo del tiempo.
- Alertar sobre picos de tasa de error y anomalías de costo antes de que tus usuarios (o tu equipo financiero) lo noten.

```python
from agent_framework.observability import get_tracer

tracer = get_tracer()

with tracer.start_as_current_span("support_request") as span:
    span.set_attribute("customer.tier", "enterprise")
    span.set_attribute("routed.model", "gpt-4.1-mini")
    # la ejecución del agente se rastrea automáticamente dentro de este intervalo
```

Los atributos como `customer.tier` y `routed.model` son los que convierten un muro de trazas en preguntas con respuesta ("¿se está enroutando demasiado el modelo pequeño a los clientes empresariales?").

## Optimización de Costos

El costo en agentes de producción está dominado por los tokens. Tres palancas, en orden de impacto:

1. **Tamaño adecuado del modelo.** Un modelo pequeño que pasa tu puerta de evaluación casi siempre es más barato que uno grande que también pasa. Usa la evaluación para *demostrar* que el modelo pequeño es suficientemente bueno en vez de elegir el más grande por precaución.
2. **Enrutar por complejidad.** Como arriba — paga el precio de modelo grande sólo para solicitudes que necesitan razonamiento de modelo grande.
3. **Cachear agresivamente.** La llamada a modelo más barata es la que nunca haces.

Las puertas de evaluación y el control de costos son la misma disciplina vista desde dos ángulos: la evaluación te indica el *piso de calidad*, el enrutamiento y caché mantienen tu *costo* lo más cerca posible de ese piso.

## Consideraciones Empresariales para Despliegue

**Gobernanza.** Los Agentes alojados heredan el RBAC, seguridad de contenido y registro de auditoría de Foundry. Da a cada agente una identidad administrada con el menor privilegio necesario — acceso solo lectura a la base de conocimiento, acceso con alcance a la API de tickets, nada más.

**Intervención humana.** Algunas acciones son demasiado importantes para automatizar totalmente — emitir un reembolso, borrar una cuenta, escalar a un equipo legal. El Microsoft Agent Framework soporta herramientas **que requieren aprobación**: el agente propone la acción, la ejecución se pausa, un humano aprueba o rechaza, y el flujo de trabajo continúa. Viste el primitivo en la [Lección 6](../06-building-trustworthy-agents/README.md); aquí lo despliegas.

**MCP en producción.** [MCP](../11-agentic-protocols/README.md) permite que tu agente consuma herramientas externas a través de una interfaz estándar. En producción, trata cada servidor MCP como un límite no confiable: fija la versión del servidor, ejecútalo con una identidad con alcance definido, valida sus salidas y nunca le expongas secretos. Un servidor MCP es una dependencia, y las dependencias se parchean, auditan y limitan en tasa.

```mermaid
flowchart TB
    subgraph Dev[Arquitectura de Desarrollo]
        D1[Cuaderno] --> D2[Marco de Agentes]
        D2 --> D3[Proveedor de Modelos]
        D2 --> D4[Herramientas locales]
    end
    subgraph Deploy[Arquitectura de Despliegue]
        E1[Pipeline CI] --> E2[Puerta de evaluación]
        E2 -->|aprobar| E3[Servicio de Agente Foundry]
        E3 --> E4[Agente alojado versionado]
    end
    subgraph Run[Arquitectura de Tiempo de Ejecución]
        F1[Aplicación cliente] --> F2[Agente alojado]
        F2 --> F3[Enrutador de Modelos]
        F2 --> F4[Búsqueda AI de Azure RAG]
        F2 --> F5[Servicio de memoria]
        F2 --> F6[Herramientas MCP]
        F2 --> F7[OTel -> Trazado Foundry]
        F2 --> F8[Aprobación humana]
    end
```

Esos tres diagramas — desarrollo, despliegue, tiempo de ejecución — son el mismo agente en tres etapas de su vida. El laboratorio que sigue te guía a construirlo.

## Laboratorio Práctico: Un Agente de Soporte al Cliente Listo para Producción

Abre [`code_samples/16-python-agent-framework.ipynb`](./code_samples/16-python-agent-framework.ipynb) y sigue todo el proceso. Armarás un **agente de soporte al cliente Contoso** con todas las preocupaciones de producción integradas:

1. **Llamada a herramientas** — consulta de estado de pedidos y apertura de tickets de soporte.
2. **RAG** — responde preguntas de políticas desde una base de conocimiento (Azure AI Search, con un respaldo en memoria para que el cuaderno funcione sin un recurso Search).
3. **Memoria** — recuerda al cliente a lo largo de los turnos de la conversación.
4. **Enrutamiento de modelo** — un clasificador de complejidad enruta cada solicitud a un modelo pequeño o grande.
5. **Caché de respuestas** — preguntas repetidas se sirven desde la caché.
6. **Aprobación humana** — reembolsos por encima de un umbral se pausan para autorización humana.
7. **Canalización de evaluación** — un conjunto pequeño de pruebas offline puntúa al agente y actúa como puerta de liberación.
8. **Observabilidad** — trazado OpenTelemetry alrededor de cada solicitud.

### Guía paso a paso

El cuaderno está organizado para que cada preocupación de producción sea una sección autónoma y ejecutable. El corazón es el manejador de solicitudes con enrutamiento y caché:

```python
async def handle_support_request(query: str, customer_id: str) -> str:
    # 1. Servir desde la caché cuando sea posible.
    cached = response_cache.get(normalize(query))
    if cached:
        return cached

    # 2. Enrutar por complejidad para controlar el costo.
    model = "gpt-4.1-mini" if is_simple(query) else "gpt-4.1"

    # 3. Ejecutar el agente dentro de un span de traza para observabilidad.
    with tracer.start_as_current_span("support_request") as span:
        span.set_attribute("routed.model", model)
        span.set_attribute("customer.id", customer_id)
        response = await support_agent.run(query, model=model)

    # 4. Cachear y devolver.
    response_cache.set(normalize(query), response.text)
    return response.text
```

La puerta de evaluación que protege una liberación se ve así:

```python
async def evaluation_gate(agent, test_cases, threshold: float = 0.8) -> bool:
    passed = 0
    for case in test_cases:
        result = await agent.run(case["input"])
        if score_response(result.text, case["expected"]) >= 0.8:
            passed += 1
    pass_rate = passed / len(test_cases)
    print(f"Evaluation pass rate: {pass_rate:.0%} (gate: {threshold:.0%})")
    return pass_rate >= threshold  # desplegar solo si la puerta pasa
```

Lee cada línea — el cuaderno mantiene los primitivos deliberadamente pequeños para que nada esté oculto tras una llamada a framework.

## Validando un Agente Desplegado con Pruebas Básicas

La puerta de evaluación arriba funciona *offline* contra tu objeto agente. Una vez que el agente está desplegado como Agente alojado, necesitas una comprobación adicional, aún más barata: **¿el endpoint desplegado realmente responde?**

Desplegar "con éxito" sólo prueba que el plano de control aceptó la definición — no prueba que el agente responda. Una dependencia perdida, un enrutamiento de modelo erróneo o una conexión expirada pueden dejar un despliegue verde que no retorna nada. Una **prueba básica (smoke test)** detecta eso en segundos, en cada despliegue, sin el costo de una evaluación completa.

Este repositorio incluye una canalización de prueba básica lista para usar basada en la GitHub Action [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test):

- **Catálogo** — [`tests/lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) contiene indicaciones y aserciones para el agente de soporte Contoso (respuestas fundamentadas en políticas, consulta de pedidos, mantener el tema y continuidad multi-turno). Catálogos para agentes de otras lecciones están junto a él — ver [`tests/README.md`](../tests/README.md).
- **Flujo de trabajo** — [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml) inicia sesión con OIDC de Azure y envía un POST de cada indicación al endpoint Responses del agente, fallando el trabajo con cualquier fallo de aserción.

```yaml
- name: Smoke-test hosted agent
  uses: JFolberth/ai-smoketest@v1
  with:
    project_endpoint: ${{ inputs.project_endpoint }}
    agent_name: ContosoSupportAgent
    tests_file: tests/lesson-16-smoke-tests.json
```


Ejecútalo desde la pestaña **Actions** una vez que tu agente esté desplegado, proporcionando el endpoint de tu proyecto Foundry y el nombre del agente. La identidad federada necesita el rol **Azure AI User** en el ámbito del proyecto Foundry. Piensa en las capas como una pirámide: las pruebas de humo (¿es accesible y responde?) se ejecutan en cada despliegue, la evaluación offline (¿es lo suficientemente bueno para enviar?) se ejecuta antes de la promoción, y la evaluación online (¿cómo está funcionando en el entorno real?) se ejecuta continuamente.

## Comprobación de conocimientos

Pon a prueba tu comprensión antes de avanzar a la tarea.

**1. Aproximadamente, ¿qué porcentaje de un agente de producción es "el modelo" y qué es el resto?**

<details>
<summary>Respuesta</summary>

El modelo es una minoría del sistema, se cita a menudo como alrededor del 20%. El resto es el esqueleto operacional: alojamiento y versionado, identidad y RBAC, estado externalizado, manejo de fallos, seguimiento de costos, evaluación y controles con intervención humana. Pasar a producción consiste principalmente en construir todo *alrededor* del ciclo de razonamiento.
</details>

**2. ¿Cuándo elegirías un agente alojado sobre uno alojado en el cliente?**

<details>
<summary>Respuesta</summary>

Cuando deseas un entorno de ejecución gestionado con durabilidad incorporada (hilos que persisten y pueden reanudarse), observabilidad, seguridad de contenido y RBAC, y estás dispuesto a sacrificar algo de control de bajo nivel del ciclo de razonamiento para reducir la superficie operacional. El alojamiento en cliente es preferible cuando necesitas control total sobre el ciclo o cuando embebes el agente en un backend existente.
</details>

**3. ¿Por qué un agente escalable debe ser sin estado en la memoria de su propio proceso?**

<details>
<summary>Respuesta</summary>

Para que cualquier instancia pueda manejar cualquier solicitud, lo que permite la escalabilidad horizontal sin sesiones fijas. El estado de la conversación por usuario se externaliza a un almacén de hilos o servicio de memoria. Si el estado residiera en la memoria del proceso, se perdería al reiniciar y no se podría distribuir la carga libremente.
</details>

**4. ¿Qué problema resuelve el enrutamiento de modelos y cómo se relaciona con la evaluación?**

<details>
<summary>Respuesta</summary>

El enrutamiento envía solicitudes simples a un modelo pequeño, barato y rápido, y reserva el modelo grande para razonamientos genuinos, controlando tanto la latencia como el costo. Se relaciona con la evaluación porque esta es lo que *demuestra* que el modelo pequeño es lo suficientemente bueno para una clase de solicitudes; enrutamiento sin evaluación es adivinar.
</details>

**5. ¿Qué es una "puerta de evaluación" y dónde se ubica en el ciclo de vida?**

<details>
<summary>Respuesta</summary>

Una puerta de evaluación ejecuta un conjunto de pruebas offline contra una nueva versión del agente y bloquea el despliegue a menos que la tasa de aprobación supere un umbral. Se sitúa entre "versión" y "despliegue" en el ciclo de vida, haciendo de la calidad una condición previa para el lanzamiento en lugar de algo que se verifica después del envío.
</details>

**6. ¿Por qué un servidor MCP debe tratarse como un límite no confiable en producción?**

<details>
<summary>Respuesta</summary>

Porque es una dependencia externa a la que tu agente llama. Debes fijar su versión, ejecutarlo con una identidad restringida, validar sus salidas, limitar su tasa de uso y nunca exponer secretos a él; la misma disciplina que aplicas a cualquier dependencia de terceros. Sus salidas fluyen hacia el razonamiento de tu agente, por lo que confiar sin validar es un riesgo de seguridad.
</details>

**7. ¿Qué cambio único suele tener el mayor impacto en el costo de un agente en producción, y por qué?**

<details>
<summary>Respuesta</summary>

Ajustar el tamaño del modelo — usar el modelo más pequeño que aún pase la puerta de evaluación. El costo está dominado por los tokens, y un modelo más pequeño que cumpla el nivel de calidad es casi siempre más barato que uno más grande. El almacenamiento en caché y el enrutamiento reducen el costo aún más, pero elegir el modelo base adecuado tiene el mayor efecto de primer orden.
</details>

**8. ¿Qué papel juegan atributos de span como `customer.tier` y `routed.model` en la observabilidad?**

<details>
<summary>Respuesta</summary>

Transforman rastreos en bruto en preguntas de negocio que se pueden responder. Sin atributos tienes una pared de spans; con ellos puedes preguntar "¿A los clientes empresariales se les está enviando demasiado al modelo pequeño?" o "¿Qué modelo maneja nuestras solicitudes más lentas?" Los atributos son cómo segmentas la telemetría por dimensiones que importan para tu operación.
</details>

## Tarea

Toma el agente de soporte al cliente del laboratorio y refuérzalo para un escenario específico: **un agente de soporte de facturación por suscripción para una empresa SaaS.**

Tu entrega debe:

1. **Reemplazar las herramientas** con aquellas relevantes para facturación: `get_subscription_status`, `get_invoice` y `issue_credit` (los créditos superiores a $50 requieren aprobación humana).
2. **Agregar tres documentos RAG** que cubran la política de reembolso, el ciclo de facturación y la política de cancelación de la empresa.
3. **Extender el conjunto de evaluación** a al menos ocho casos, incluyendo al menos dos que *deberían* activar la ruta de aprobación humana, y confirmar que la puerta de evaluación pasa o falla correctamente.
4. **Agregar un reporte de costos**: después de ejecutar diez consultas mixtas a través del agente, imprimir cuántas fueron al modelo pequeño, cuántas al modelo grande y cuántas se sirvieron desde caché.

Escribe un párrafo corto (en una celda markdown) explicando qué regla de enrutamiento de modelo elegiste y cómo la validarías con tráfico real. No hay una única respuesta correcta — se evalúa si las preocupaciones de producción están integradas coherentemente.

## Resumen

En esta lección moviste un agente de prototipo a producción con Microsoft Foundry:

- El salto a producción es principalmente sobre el **esqueleto operacional** alrededor del modelo — alojamiento, identidad, estado, manejo de fallos, costo, calidad y confianza.
- Aprendiste los tres **patrones de despliegue** — cliente alojado, agentes alojados y flujos de trabajo de agentes — y cuándo usar cada uno.
- Recorriendo el **ciclo de vida del agente**, donde la **evaluación offline actúa como una puerta de lanzamiento** y la observabilidad online alimenta fallos de vuelta al conjunto de pruebas.
- Aplicaste **estrategias de escalado** — diseño sin estado, enrutamiento de modelos, caché y concurrencia limitada — y las conectaste a la **optimización de costos**.
- Integramos **controles empresariales**: RBAC, aprobación con intervención humana e integración segura de MCP en producción.
- Construiste un **agente de soporte al cliente listo para producción** que une todas estas preocupaciones en código ejecutable.

La siguiente lección toma el camino opuesto: en lugar de escalar agentes hacia la nube, los llevarás *hacia abajo* a una sola máquina de desarrollador y los ejecutarás completamente local.

## Recursos adicionales

- <a href="https://learn.microsoft.com/azure/ai-foundry/what-is-azure-ai-foundry" target="_blank">Documentación de Microsoft Foundry</a>
- <a href="https://learn.microsoft.com/azure/ai-foundry/agents/overview" target="_blank">Resumen del Servicio de Agentes de Microsoft Foundry</a>
- <a href="https://aka.ms/ai-agents-beginners/agent-framework" target="_blank">Marco de Agentes de Microsoft</a>
- <a href="https://learn.microsoft.com/azure/ai-foundry/concepts/model-router" target="_blank">Enrutador de Modelos en Microsoft Foundry</a>
- <a href="https://learn.microsoft.com/azure/search/search-what-is-azure-search" target="_blank">Azure AI Search</a>
- <a href="https://opentelemetry.io/" target="_blank">OpenTelemetry</a>
- <a href="https://github.com/marketplace/actions/ai-smoke-test" target="_blank">GitHub Action AI Smoke Test</a>
- <a href="https://modelcontextprotocol.io/" target="_blank">Protocolo de Contexto de Modelo (MCP)</a>

## Lección anterior

[Construcción de Agentes de Uso de Computadora (CUA)](../15-browser-use/README.md)

## Próxima lección

[Creación de Agentes de IA Locales](../17-creating-local-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->