# Agentes de IA para Principiantes - Guía de Estudio

Usa esta guía como un acompañante práctico mientras avanzas en el curso. No está
diseñada para reemplazar las lecciones. Te ayuda a decidir dónde comenzar, qué
buscar en cada lección y cómo conectar las ideas en una pequeña demostración
funcional de un agente.

Si es tu primera vez aquí, comienza simple:

1. Lee la [Configuración del Curso](./00-course-setup/README.md).
2. Completa las Lecciones 01-06 en orden.
3. Mantén una pequeña idea de demostración en mente mientras aprendes.
4. Después de cada lección, pregúntate: "¿Qué puede hacer mi agente ahora que no
   podía hacer antes?"

## Una Demostración Simple para Tener en Mente

Una buena manera de aprender agentes es seguir una idea de demostración durante
todo el curso.

Demostración ejemplo: **un agente ayudante del curso**.

El usuario pregunta:

> "Quiero aprender cómo los agentes usan herramientas. Encuentra las lecciones
> correctas, resume qué debo leer primero y dame una tarea práctica corta."

Un chatbot normal puede responder con lo que ya sabe. Un agente puede hacer más:

1. **Leer o buscar en archivos del curso** para encontrar las lecciones adecuadas.
2. **Usar herramientas** para obtener enlaces de lección, ejemplos o material de apoyo.
3. **Planificar** un camino de aprendizaje corto en lugar de dar una respuesta larga.
4. **Usar el contexto** de la conversación actual para mantenerse enfocado en el
   objetivo del aprendiz.
5. **Recordar preferencias útiles** si la aplicación soporta memoria.
6. **Mostrar rastros, citas o registros** para que el usuario entienda qué pasó.
7. **Aplicar salvaguardas** antes de tomar acciones riesgosas o usar datos sensibles.

Mientras estudias cada lección, vuelve a esta demo y pregúntate: ¿qué nueva
capacidad agregaría esta lección?

## Hacia Qué Estás Construyendo

Al final del curso, deberías poder explicar y construir sistemas de agentes que
combinan estas partes:

| Parte | Significado en lenguaje sencillo | En la demo |
|-------|----------------------------------|------------|
| Modelo | El motor de razonamiento que interpreta la solicitud del usuario | Entiende que el aprendiz quiere lecciones sobre uso de herramientas |
| Herramientas | Funciones, APIs, archivos, navegadores o servicios que el agente puede usar | Busca en el repositorio o recupera contenido de lecciones |
| Conocimiento | Documentos o datos usados para fundamentar la respuesta | Archivos README del curso y material de lecciones |
| Contexto | Información incluida en la siguiente llamada al modelo | El objetivo del usuario y los resultados de las herramientas |
| Memoria | Información guardada para uso posterior | El aprendiz prefiere ejemplos prácticos en Python |
| Planificación | Dividir una meta grande en pasos más pequeños | Buscar lecciones, resumirlas, sugerir práctica |
| Orquestación | Dirigir el trabajo a través de herramientas, pasos o agentes | Un planificador llama a una herramienta de búsqueda, luego a un resumidor |
| Confianza | Seguridad, evaluación, y observabilidad | Registra llamadas a herramientas y pregunta antes de acciones de alto impacto |

## Elige Tu Camino de Aprendizaje

Puedes tomar el curso completo en orden, o saltar a un camino basado en lo que quieres
construir.

| Si tu objetivo es... | Comienza con | Luego estudia |
|---------------------|--------------|--------------|
| Entender qué son los agentes | 01, 02, 03 | 04, 05, 06 |
| Construir un agente que use herramientas | 04 | 05, 07, 14 |
| Construir un agente basado en RAG | 05 | 04, 06, 12 |
| Diseñar flujos de trabajo de múltiples pasos | 07 | 08, 09, 14 |
| Entender sistemas multi-agentes | 08 | 07, 09, 11 |
| Preparar agentes para producción | 06, 10 | 12, 13, 18 |
| Explorar protocolos y automatización de navegadores | 11, 15 | 10, 18 |

Consejo: si eres nuevo en agentes, no saltes las Lecciones 01-06. Te dan el
vocabulario que necesitarás para el resto del curso.

## Guía Lección por Lección

| Lección | Qué aprendes | Prueba esto después de la lección |
|---------|--------------|----------------------------------|
| [01 - Introducción a Agentes de IA](./01-intro-to-ai-agents/README.md) | Qué hace que un agente sea diferente a un chatbot básico. | Explica la idea de tu demo como un agente, no solo una app de chat. |
| [02 - Frameworks Agénticos](./02-explore-agentic-frameworks/README.md) | Cómo los frameworks ayudan con modelos, herramientas, estado y flujos de trabajo. | Identifica qué partes de tu demo manejaría un framework. |
| [03 - Patrones de Diseño Agénticos](./03-agentic-design-patterns/README.md) | Patrones comunes para diseñar comportamiento de agentes. | Bosqueja el viaje del usuario antes de escribir código. |
| [04 - Uso de Herramientas](./04-tool-use/README.md) | Cómo los agentes llaman a herramientas para obtener datos o actuar. | Define una herramienta que tu agente demo necesite. |
| [05 - RAG Agéntico](./05-agentic-rag/README.md) | Cómo la recuperación fundamenta respuestas de agentes en documentos o datos. | Decide qué fuente de conocimiento debería buscar tu demo. |
| [06 - Agentes Confiables](./06-building-trustworthy-agents/README.md) | Cómo agregar salvaguardas, supervisión, y comportamiento más seguro. | Añade una regla sobre cuándo el agente debería preguntar primero. |
| [07 - Diseño de Planificación](./07-planning-design/README.md) | Cómo los agentes dividen metas grandes en pasos pequeños. | Escribe un plan de tres pasos para la solicitud de tu demo. |
| [08 - Diseño Multi-Agente](./08-multi-agent/README.md) | Cuándo dividir el trabajo entre agentes especializados. | Decide si tu demo necesita uno o varios agentes. |
| [09 - Metacognición](./09-metacognition/README.md) | Cómo los agentes pueden revisar y mejorar su propio output. | Añade una auto-verificación antes de que el agente responda. |
| [10 - Agentes de IA en Producción](./10-ai-agents-production/README.md) | Qué cambia cuando un agente pasa de demo a producción. | Lista qué supervisarías: calidad, costo, latencia, fallas. |
| [11 - Protocolos Agénticos](./11-agentic-protocols/README.md) | Cómo los protocolos conectan agentes con herramientas y otros agentes. | Identifica dónde un protocolo estándar podría simplificar integración. |
| [12 - Ingeniería de Contexto](./12-context-engineering/README.md) | Cómo seleccionar, recortar, aislar y gestionar contexto. | Decide qué debe estar en el prompt y qué debe quedar afuera. |
| [13 - Memoria del Agente](./13-agent-memory/README.md) | Cómo los agentes pueden guardar info útil entre interacciones. | Elige una preferencia segura que tu demo podría recordar. |
| [14 - Framework de Agentes Microsoft](./14-microsoft-agent-framework/README.md) | Bloques de construcción específicos para agentes y flujos de trabajo. | Mapea pasos de tu demo a conceptos del framework. |
| [15 - Agentes de Uso de Computadora](./15-browser-use/README.md) | Cómo los agentes pueden interactuar con navegadores o interfaces. | Elige una tarea del navegador que aún requiera confirmación de usuario. |
| [18 - Seguridad para Agentes de IA](./18-securing-ai-agents/README.md) | Cómo hacer acciones de agentes más auditables y a prueba de manipulaciones. | Decide qué acciones en tu demo deben registrarse o dejar recibo. |

Las lecciones 16 y 17 están listadas en el README principal como próximas. Agrégalas
a tu plan de estudio cuando el contenido esté disponible.

## Ideas Clave en Términos para Principiantes

### Herramientas

Una herramienta es algo que el agente puede llamar para hacer trabajo fuera del modelo.
Una buena herramienta tiene un nombre claro, un trabajo específico, entradas tipadas,
salida predecible y una forma segura de fallar.

Para la demo del ayudante del curso, una herramienta podría ser:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG y Conocimiento

RAG ayuda al agente a responder desde material fuente en lugar de adivinar. En este
curso, ese material fuente puede ser archivos README de lecciones, ejemplos de código,
o recursos externos enlazados desde las lecciones.

Usa RAG cuando la respuesta debe estar fundamentada en documentos, datos, o archivos
del proyecto actual.

### Planificación

La planificación es útil cuando la solicitud tiene más de un paso. Mantén los planes
cortos y lo suficientemente visibles para que un desarrollador o usuario los inspeccione.

Para la demo, un plan podría ser:

1. Encontrar lecciones relacionadas con el uso de herramientas.
2. Resumir las lecciones más relevantes.
3. Recomendar una tarea práctica.

### Contexto

El contexto es lo que el modelo ve ahora mismo. Muy poco contexto puede hacer que el
agente pierda detalles importantes. Demasiado contexto puede hacer que el agente sea
más lento, más costoso o más fácil de confundir.

Una buena ingeniería de contexto significa elegir la información correcta para la
siguiente llamada al modelo.

### Memoria

La memoria es información guardada para el futuro. No guardes todo. Guarda solo
información que sea útil, segura y fácil de actualizar o borrar.

Por ejemplo, recordar "el aprendiz prefiere ejemplos en Python" puede ser útil.
Recordar datos personales sensibles usualmente no lo es.

### Evaluación y Observabilidad

La evaluación pregunta: ¿hizo el agente lo correcto?

La observabilidad pregunta: ¿podemos ver cómo ocurrió?

Para agentes en producción, lleva registro de llamadas al modelo, llamadas a herramientas,
contexto recuperado, latencia, costo, fallas y retroalimentación del usuario.

### Confianza y Seguridad

Agentes confiables necesitan más que un prompt útil. Usa herramientas con mínimos
privilegios, aprobación humana para acciones de alto impacto, redacción de datos
cuando sea necesario, y registros o recibos para acciones que deben auditarse.

## Rutina de Revisión de 15 Minutos

Usa esta rutina después de cada lección:

1. **Resume la lección en una frase.**
2. **Nombra la nueva capacidad del agente.** Por ejemplo: uso de herramienta,
   recuperación, planificación, memoria, observabilidad o seguridad.
3. **Agrégala a la demo del ayudante del curso.** ¿Qué cambia ahora en la demo?
4. **Encuentra el riesgo.** ¿Qué podría salir mal si se usa mal esta capacidad?
5. **Escribe una pregunta de prueba.** ¿Cómo verificarías que el agente se comporta bien?

## Autoevaluación Rápida

Antes de continuar, intenta responder estas preguntas:

1. ¿Qué puede hacer un agente que un chatbot normal no puede hacer por sí solo?
2. ¿Qué herramienta necesitaría primero tu agente y por qué?
3. ¿Qué fuente de conocimiento debería fundamentar la respuesta del agente?
4. ¿Qué contexto debería incluirse en la siguiente llamada al modelo?
5. ¿Qué debería recordar el agente y qué debería evitar almacenar?
6. ¿Cuándo debería el agente pedir aprobación humana?
7. ¿Qué registros, rastros o recibos te ayudarían a depurar o auditar el agente después?

## Ejercicio Sugerido de Proyecto Final

Al final del curso, construye un pequeño agente que ayude a un aprendiz a navegar este
repositorio.

Versión mínima:

- Acepta un tema del usuario.
- Encuentra las lecciones más relevantes.
- Resume qué leer primero.
- Sugiere una tarea práctica.
- Muestra qué archivos de lección o enlaces se usaron.

Versión extendida:

- Recuerda el lenguaje de programación preferido del aprendiz.
- Usa un plan simple antes de responder.
- Añade un paso de auto-verificación antes de la respuesta final.
- Registra llamadas a herramientas y fuentes recuperadas.
- Pide confirmación antes de abrir tareas de navegador o automatización UI.

Esto te da una forma pequeña pero realista de practicar herramientas, RAG, planificación,
contexto, memoria, observabilidad y confianza en un solo proyecto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->