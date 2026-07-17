# Agentes de IA para Principiantes - Guía de Estudio

Usa esta guía como un acompañante práctico mientras avanzas en el curso. No está
diseñada para reemplazar las lecciones. Te ayuda a decidir dónde comenzar, qué
buscar en cada lección y cómo conectar las ideas en una pequeña demo de agente
funcional.

Si es tu primera vez aquí, comienza de manera simple:

1. Lee el [Course Setup](./00-course-setup/README.md).
2. Completa las lecciones 01-06 en orden.
3. Mantén una pequeña idea de demo en mente mientras aprendes.
4. Después de cada lección, pregúntate: "¿Qué puede hacer mi agente ahora que antes
   no podía?"

## Una Demo Simple para Recordar

Una buena manera de aprender sobre agentes es seguir una idea de demo a lo largo del curso.

Ejemplo de demo: **un agente ayudante del curso**.

El usuario pregunta:

> "Quiero aprender cómo los agentes usan herramientas. Encuentra las lecciones adecuadas,
> resúmeme qué debería leer primero y dame una tarea corta de práctica."

Un chatbot común puede responder con lo que ya sabe. Un agente puede hacer más:

1. **Leer o buscar archivos del curso** para encontrar las lecciones adecuadas.
2. **Usar herramientas** para obtener enlaces de lecciones, ejemplos o material de apoyo.
3. **Planear** un camino corto de aprendizaje en lugar de dar una respuesta larga.
4. **Usar el contexto** de la conversación actual para enfocarse en la meta del aprendiz.
5. **Recordar preferencias útiles** si la aplicación soporta memoria.
6. **Mostrar rastros, citas o registros** para que el usuario entienda lo que sucedió.
7. **Aplicar barreras de seguridad** antes de tomar acciones riesgosas o usar datos sensibles.


agregaría esta lección?


## Hacia Dónde Estás Construyendo

Al final del curso, deberías poder explicar y construir sistemas de agentes
que combinan estas partes:

| Parte | Significado en lenguaje sencillo | En la demo |
|------|------------------------------|-------------|
| Modelo | El motor de razonamiento que interpreta la solicitud del usuario | Entiende que el aprendiz quiere lecciones sobre el uso de herramientas |
| Herramientas | Funciones, API, archivos, navegadores o servicios que el agente puede usar | Busca en el repositorio o recupera contenido de lecciones |
| Conocimiento | Documentos o datos usados para fundamentar la respuesta | Archivos README del curso y material de las lecciones |
| Contexto | Información incluida en la siguiente llamada al modelo | La meta del usuario y los resultados de las herramientas |
| Memoria | Información guardada para uso posterior | El aprendiz prefiere ejemplos prácticos en Python |
| Planificación | Dividir una meta más grande en pasos más pequeños | Encontrar lecciones, resumirlas, sugerir práctica |
| Orquestación | Dirigir el trabajo entre herramientas, pasos o agentes | Un planificador llama a una herramienta de búsqueda, luego a un resumidor |
| Confianza | Seguridad, evaluación y observabilidad | Registra llamadas a herramientas y pregunta antes de acciones de alto impacto |

## Modelos y Proveedores

Los ejemplos de código del curso usan el **Microsoft Agent Framework (MAF)** y están dirigidos a la **Azure OpenAI Responses API** — la API recomendada de ahora en adelante, que combina chat completions, llamadas a herramientas, entrada multimodal y conversaciones con estado en una sola superficie de API. Puedes conectarte ya sea a través de un proyecto **Microsoft Foundry** (con `FoundryChatClient`) o directamente a Azure OpenAI (con `OpenAIChatClient`).


A medida que avanzas en las lecciones, tienes algunas opciones de proveedor:

- **Microsoft Foundry / Azure OpenAI (API de Respuestas)** — el camino principal usado en las lecciones. Inicia sesión con `az login` para autenticación sin clave vía Entra ID.
- **Foundry Local** — ejecuta modelos completamente en el dispositivo a través de una API compatible con OpenAI (sin nube, sin claves API). Ideal para experimentación sin conexión o sin costo. Ver [Configuración del Curso](./00-course-setup/README.md).
- **MiniMax** — un proveedor compatible con OpenAI con modelos de contexto largo, usable como alternativa directa.

> **Nota:** GitHub Models está en desuso (se retirará en julio 2026) y no soporta la API de Respuestas. Las muestras se han actualizado para usar Azure OpenAI / Microsoft Foundry en su lugar.

## Elige Tu Ruta de Aprendizaje

Puedes tomar el curso completo en orden o saltar a una ruta basada en lo que quieres
construir.

| Si tu objetivo es... | Comienza con | Luego estudia |
|-----------------------|------------|------------|
| Entender qué son los agentes | 01, 02, 03 | 04, 05, 06 |
| Construir un agente que use herramientas | 04 | 05, 07, 14 |
| Construir un agente basado en RAG | 05 | 04, 06, 12 |
| Diseñar flujos de trabajo de múltiples pasos | 07 | 08, 09, 14 |
| Entender sistemas multiagente | 08 | 07, 09, 11 |
| Preparar agentes para producción | 06, 10 | 12, 13, 16, 18 |
| Desplegar y escalar agentes en Foundry | 10, 16 | 06, 13, 18 |
| Construir agentes locales / offline-first | 17 | 04, 05, 11 |
| Explorar protocolos y automatización en navegador | 11, 15 | 10, 18 |

Consejo: si eres nuevo en agentes, no saltes las lecciones 01-06. Te dan el
vocabulario que necesitarás para el resto del curso.

## Guía Lección por Lección

| Lección | Qué aprendes | Intenta esto después de la lección |
|--------|----------------|---------------------------|
| [01 - Introducción a los Agentes AI](./01-intro-to-ai-agents/README.md) | Qué hace que un agente sea diferente de un chatbot básico. | Explica tu idea de demo como un agente, no sólo como una aplicación de chat. |
| [02 - Frameworks Agénticos](./02-explore-agentic-frameworks/README.md) | Cómo los frameworks ayudan con modelos, herramientas, estado y flujos de trabajo. | Identifica qué partes de tu demo gestionaría un framework. |
| [03 - Patrones de Diseño Agéntico](./03-agentic-design-patterns/README.md) | Patrones comunes para diseñar el comportamiento de agentes. | Esboza el viaje del usuario antes de escribir código. |
| [04 - Uso de Herramientas](./04-tool-use/README.md) | Cómo los agentes llaman herramientas para obtener datos o actuar. | Define una herramienta que tu agente demo necesitaría. |
| [05 - RAG Agéntico](./05-agentic-rag/README.md) | Cómo la recuperación fundamenta las respuestas del agente en documentos o datos. | Decide qué fuente de conocimiento debería buscar tu demo. |

| [06 - Agentes Confiables](./06-building-trustworthy-agents/README.md) | Cómo añadir protecciones, supervisión y comportamientos más seguros. | Añade una regla para cuándo el agente debe preguntar al usuario primero. |
| [07 - Diseño de Planificación](./07-planning-design/README.md) | Cómo los agentes descomponen objetivos grandes en pasos más pequeños. | Escribe un plan de tres pasos para tu solicitud de demo. |
| [08 - Diseño Multi-Agente](./08-multi-agent/README.md) | Cuándo dividir el trabajo entre agentes especializados. | Decide si tu demo necesita un agente o varios. |
| [09 - Metacognición](./09-metacognition/README.md) | Cómo los agentes pueden revisar y mejorar su propia salida. | Añade una auto-verificación final antes de que el agente responda. |
| [10 - Agentes de IA en Producción](./10-ai-agents-production/README.md) | Qué cambia cuando un agente pasa de demo a producción. | Enumera lo que monitorizarías: calidad, coste, latencia, fallos. |
| [11 - Protocolos Agénticos](./11-agentic-protocols/README.md) | Cómo los protocolos conectan agentes con herramientas y otros agentes. | Identifica dónde un protocolo estándar podría simplificar la integración. |
| [12 - Ingeniería de Contexto](./12-context-engineering/README.md) | Cómo seleccionar, recortar, aislar y gestionar el contexto. | Decide qué pertenece al prompt y qué debería quedar fuera. |
| [13 - Memoria de Agentes](./13-agent-memory/README.md) | Cómo los agentes pueden guardar información útil a lo largo de interacciones. | Elige una preferencia segura que tu demo podría recordar. |
| [14 - Marco de Trabajo Microsoft Agent](./14-microsoft-agent-framework/README.md) | Bloques de construcción específicos para agentes y flujos de trabajo, más alojamiento de agentes LangChain/LangGraph en Microsoft Foundry. | Mapea los pasos de tu demo a los conceptos del marco. |
| [15 - Agentes de Uso Informático](./15-browser-use/README.md) | Cómo los agentes pueden interactuar con navegadores o interfaces, incluyendo ejemplos reales como Microsoft Project Opal. | Elige una tarea del navegador que todavía debería requerir confirmación del usuario. |
| [16 - Despliegue de Agentes Escalables](./16-deploying-scalable-agents/README.md) | Cómo pasar un agente de prototipo a un despliegue escalable y observable en producción en Microsoft Foundry (agentes alojados, enrutamiento de modelos, caching, puertas de evaluación, pruebas de humo). | Enumera las preocupaciones de producción que tu demo aún necesita: alojamiento, enrutamiento, coste, evaluación. |
| [17 - Creación de Agentes de IA Locales](./17-creating-local-ai-agents/README.md) | Cómo construir agentes local-first que se ejecutan totalmente en tu máquina con Foundry Local y Qwen (herramientas locales, RAG local, MCP local). | Decide qué partes de tu demo deberían mantenerse privadas y ejecutarse localmente. |
| [18 - Asegurando Agentes de IA](./18-securing-ai-agents/README.md) | Cómo hacer las acciones del agente más auditables y evidentes de manipulación. | Decide qué acciones en tu demo deberían ser registradas o recibidas. |

## Validando Agentes Desplegados con Pruebas de Humo

Cuando despliegas un agente (Lección 16), una **prueba de humo** es la primera
comprobación más económica para verificar que el despliegue realmente responde. Este repositorio incluye catálogos listos para ejecutar
bajo [tests/](./tests/README.md) para los agentes desplegables en las Lecciones
01, 04, 05 y 16, conectados con la
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) Acción de GitHub.
Ejecútalas desde la pestaña **Actions** después de desplegar el agente de la lección.
Las pruebas de humo son una primera puerta — las evaluaciones offline y online (Lecciones 10 y 16)
te dicen qué tan *bueno* es el agente.

## Ideas Clave en Términos para Principiantes

### Herramientas

Una herramienta es algo que el agente puede invocar para hacer trabajo fuera del modelo. Una buena herramienta
tiene un nombre claro, una tarea específica, entradas tipadas, salida predecible y una forma segura
de fallar.

Para la demo del asistente del curso, una herramienta podría ser:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG y Conocimiento

RAG ayuda al agente a responder desde material fuente en lugar de adivinar. En este
curso, ese material fuente podrían ser los READMEs de las lecciones, ejemplos de código o recursos externos
enlazados desde las lecciones.

Usa RAG cuando la respuesta debe estar fundamentada en documentos, datos o archivos
actuales de proyectos.

### Planificación

La planificación es útil cuando la solicitud tiene más de un paso. Mantén los planes cortos y
lo suficientemente visibles para que un desarrollador o usuario pueda inspeccionarlos.

Para la demo, un plan podría ser:

1. Encuentra lecciones relacionadas con el uso de herramientas.
2. Resume las lecciones más relevantes.
3. Recomienda una tarea práctica.

### Contexto

El contexto es lo que el modelo ve en este momento. Poca información puede hacer que el agente
pierda detalles importantes. Mucho contexto puede hacer que el agente sea más lento, más costoso,
o más fácil de confundir.

Una buena ingeniería de contexto significa elegir la información correcta para la próxima
llamada al modelo.

### Memoria

La memoria es la información guardada para más adelante. No guardes todo. Guarda la información
solo cuando sea útil, segura y fácil de actualizar o eliminar.

Por ejemplo, recordar "el aprendiz prefiere ejemplos en Python" puede ser útil.
Recordar datos personales sensibles generalmente no lo es.

### Evaluación y Observabilidad

La evaluación pregunta: ¿hizo el agente lo correcto?

La observabilidad pregunta: ¿podemos ver cómo sucedió?

Para agentes en producción, lleva registro de llamadas al modelo, llamadas a herramientas, contexto recuperado,
latencia, costes, fallos y retroalimentación de usuarios.

### Confianza y Seguridad

Los agentes confiables necesitan más que un prompt útil. Usa herramientas con privilegios mínimos,
aprobación humana para acciones de alto impacto, redacción de datos donde sea necesario, y registros o
recibos para acciones que deben auditarse.

## Una Rutina de Revisión de 15 Minutos

Usa esta rutina después de cada lección:

1. **Resume la lección en una oración.**
2. **Nombra la nueva capacidad del agente.** Por ejemplo: uso de herramientas, recuperación,
   planificación, memoria, observabilidad o seguridad.
3. **Agrégala a la demo del asistente del curso.** ¿Qué cambia en la demo ahora?
4. **Encuentra el riesgo.** ¿Qué podría salir mal si esta capacidad es mal usada?
5. **Escribe una pregunta de prueba.** ¿Cómo verificarías que el agente se comporta bien?

## Auto-Check Rápido

Antes de continuar, intenta responder estas preguntas:

1. ¿Qué puede hacer un agente que un chatbot normal no puede hacer por sí solo?
2. ¿Qué herramienta necesitaría tu agente primero, y por qué?
3. ¿Qué fuente de conocimiento debería fundamentar la respuesta del agente?
4. ¿Qué contexto debería incluirse en la próxima llamada al modelo?

5. ¿Qué debería recordar el agente y qué debería evitar almacenar?
6. ¿Cuándo debería el agente pedir aprobación humana?
7. ¿Qué registros, trazas o recibos te ayudarían a depurar o auditar el agente más tarde?


## Ejercicio Propuesto Final

Al final del curso, crea un pequeño agente que ayude a un aprendiz a navegar por este
repositorio.

Versión mínima:

- Aceptar un tema del usuario.
- Encontrar las lecciones más relevantes.
- Resumir qué leer primero.
- Sugerir una tarea práctica.
- Mostrar qué archivos de lecciones o enlaces se usaron.

Versión avanzada:

- Recordar el lenguaje de programación preferido del aprendiz.
- Usar un plan simple antes de responder.
- Añadir un paso de autoverificación antes de la respuesta final.
- Registrar llamadas a herramientas y fuentes consultadas.
- Solicitar confirmación antes de abrir el navegador o tareas de automatización de UI.

Esto te ofrece una forma pequeña pero realista de practicar herramientas, RAG, planificación,
contexto, memoria, observabilidad y confianza en un solo proyecto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->