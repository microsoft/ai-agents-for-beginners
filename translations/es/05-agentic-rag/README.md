[![Agentic RAG](../../../translated_images/es/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Agentic RAG

Esta lección ofrece una visión general completa de Agentic Retrieval-Augmented Generation (Agentic RAG), un paradigma emergente en IA donde los grandes modelos de lenguaje (LLMs) planifican autónomamente sus próximos pasos mientras extraen información de fuentes externas. A diferencia de los patrones estáticos de recuperación y luego lectura, Agentic RAG implica llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas. El sistema evalúa los resultados, refina las consultas, invoca herramientas adicionales si es necesario y continúa este ciclo hasta alcanzar una solución satisfactoria.

## Introducción

Esta lección cubrirá

- **Entender Agentic RAG:** Aprende sobre el paradigma emergente en IA donde los grandes modelos de lenguaje (LLMs) planifican autónomamente sus próximos pasos mientras extraen información de fuentes de datos externas.
- **Comprender el estilo Iterativo Maker-Checker:** Comprende el ciclo de llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas, diseñadas para mejorar la corrección y manejar consultas malformadas.
- **Explorar aplicaciones prácticas:** Identifica escenarios donde Agentic RAG destaca, como entornos con prioridad en la corrección, interacciones complejas con bases de datos y flujos de trabajo prolongados.

## Objetivos de aprendizaje

Después de completar esta lección, sabrás cómo/comprenderás:

- **Comprensión de Agentic RAG:** Aprende sobre el paradigma emergente en IA donde los grandes modelos de lenguaje (LLMs) planifican autónomamente sus próximos pasos mientras extraen información de fuentes de datos externas.
- **Estilo Iterativo Maker-Checker:** Comprende el concepto de un ciclo de llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas, diseñadas para mejorar la corrección y manejar consultas malformadas.
- **Ser dueño del proceso de razonamiento:** Comprende la capacidad del sistema para ser dueño de su proceso de razonamiento, tomando decisiones sobre cómo abordar los problemas sin depender de rutas predefinidas.
- **Flujo de trabajo:** Comprende cómo un modelo agente decide de forma independiente recuperar informes de tendencias del mercado, identificar datos de competidores, correlacionar métricas internas de ventas, sintetizar hallazgos y evaluar la estrategia.
- **Ciclos iterativos, integración de herramientas y memoria:** Aprende sobre la dependencia del sistema en un patrón de interacción en bucle, manteniendo estado y memoria a lo largo de los pasos para evitar bucles repetitivos y tomar decisiones informadas.
- **Manejo de modos de fallo y autocorrección:** Explora los sólidos mecanismos de autocorrección del sistema, incluyendo iterar y reconsultar, usar herramientas diagnósticas y recurrir a supervisión humana.
- **Límites de la agencia:** Comprende las limitaciones de Agentic RAG, centrándote en la autonomía específica del dominio, la dependencia de la infraestructura y el respeto por las directrices.
- **Casos de uso prácticos y valor:** Identifica escenarios donde Agentic RAG destaca, como entornos con prioridad en la corrección, interacciones complejas con bases de datos y flujos de trabajo prolongados.
- **Gobernanza, transparencia y confianza:** Aprende la importancia de la gobernanza y la transparencia, incluyendo razonamiento explicable, control de sesgos y supervisión humana.

## ¿Qué es Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) es un paradigma emergente en IA donde los grandes modelos de lenguaje (LLMs) planifican autónomamente sus próximos pasos mientras obtienen información de fuentes externas. A diferencia de los patrones estáticos de recuperación y luego lectura, Agentic RAG implica llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas. El sistema evalúa resultados, refina consultas, invoca herramientas adicionales si se necesita y continúa este ciclo hasta lograr una solución satisfactoria. Este estilo iterativo “maker-checker” mejora la corrección, maneja consultas malformadas y asegura resultados de alta calidad.

El sistema es dueño activo de su proceso de razonamiento, reescribiendo consultas fallidas, eligiendo diferentes métodos de recuperación e integrando múltiples herramientas —como búsqueda vectorial en Azure AI Search, bases de datos SQL o APIs personalizadas— antes de finalizar su respuesta. La cualidad distintiva de un sistema agente es su capacidad para ser dueño de su proceso de razonamiento. Las implementaciones tradicionales de RAG dependen de rutas predefinidas, pero un sistema agente determina autónomamente la secuencia de pasos según la calidad de la información que encuentra.

## Definición de Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) es un paradigma emergente en el desarrollo de IA donde los LLM no solo extraen información de fuentes de datos externas sino que también planifican autónomamente sus siguientes pasos. A diferencia de patrones estáticos de recuperación y luego lectura o secuencias cuidadosamente guionizadas de indicaciones, Agentic RAG implica un ciclo de llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas. En cada etapa, el sistema evalúa los resultados que ha obtenido, decide si refinar sus consultas, invoca herramientas adicionales si es necesario y continúa este ciclo hasta lograr una solución satisfactoria.

Este estilo iterativo “maker-checker” está diseñado para mejorar la corrección, manejar consultas malformadas a bases de datos estructuradas (por ejemplo, NL2SQL) y asegurar resultados equilibrados y de alta calidad. En lugar de depender únicamente de cadenas de indicaciones cuidadosamente diseñadas, el sistema es dueño activo de su proceso de razonamiento. Puede reescribir consultas que fallen, elegir diferentes métodos de recuperación e integrar múltiples herramientas —como búsqueda vectorial en Azure AI Search, bases de datos SQL o APIs personalizadas— antes de finalizar su respuesta. Esto elimina la necesidad de marcos de orquestación demasiado complejos. En su lugar, un ciclo relativamente simple de “llamada a LLM → uso de herramienta → llamada a LLM → …” puede producir salidas sofisticadas y bien fundamentadas.

![Ciclo central de Agentic RAG](../../../translated_images/es/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Ser dueño del proceso de razonamiento

La cualidad distintiva que hace que un sistema sea “agentic” es su capacidad para ser dueño de su proceso de razonamiento. Las implementaciones tradicionales de RAG a menudo dependen de que los humanos predefinan una ruta para el modelo: una cadena de pensamiento que indica qué recuperar y cuándo.
Pero cuando un sistema es verdaderamente agentic, decide internamente cómo abordar el problema. No solo ejecuta un guion; determina autónomamente la secuencia de pasos según la calidad de la información que encuentra.
Por ejemplo, si se le pide crear una estrategia de lanzamiento de producto, no depende únicamente de una indicación que explique todo el flujo de trabajo de investigación y toma de decisiones. En cambio, el modelo agentic decide de forma independiente:

1. Recuperar informes actuales de tendencias del mercado usando Bing Web Grounding
2. Identificar datos relevantes de competidores usando Azure AI Search.
3. Correlacionar métricas históricas internas de ventas usando Azure SQL Database.
4. Sintetizar los hallazgos en una estrategia cohesionada orquestada a través de Azure OpenAI Service.
5. Evaluar la estrategia para detectar brechas o inconsistencias, solicitando otra ronda de recuperación si es necesario.
Todos estos pasos —refinar consultas, elegir fuentes, iterar hasta estar “contento” con la respuesta— son decididos por el modelo, no predefinidos por un humano.

## Ciclos iterativos, integración de herramientas y memoria

![Arquitectura de integración de herramientas](../../../translated_images/es/tool-integration.0f569710b5c17c10.webp)

Un sistema agentic se basa en un patrón de interacción en bucle:

- **Llamada inicial:** El objetivo del usuario (también llamado indicación de usuario) se presenta al LLM.
- **Invocación de herramienta:** Si el modelo identifica información faltante o instrucciones ambiguas, selecciona una herramienta o método de recuperación —como una consulta a una base de datos vectorial (por ejemplo, búsqueda híbrida Azure AI Search sobre datos privados) o una llamada SQL estructurada— para reunir más contexto.
- **Evaluación y refinamiento:** Tras revisar los datos devueltos, el modelo decide si la información es suficiente. Si no, refina la consulta, prueba con otra herramienta o ajusta su enfoque.
- **Repetir hasta estar satisfecho:** Este ciclo continúa hasta que el modelo determina que tiene suficiente claridad y evidencias para entregar una respuesta final y bien razonada.
- **Memoria y estado:** Debido a que el sistema mantiene estado y memoria entre pasos, puede recordar intentos previos y sus resultados, evitando bucles repetitivos y tomando decisiones más informadas conforme avanza.

Con el tiempo, esto crea una sensación de comprensión evolutiva, permitiendo que el modelo navegue tareas complejas de múltiples pasos sin requerir la intervención humana constante o reformulación de la indicación.

## Manejo de modos de fallo y autocorrección

La autonomía de Agentic RAG también incluye mecanismos robustos de autocorrección. Cuando el sistema llega a callejones sin salida —como recuperar documentos irrelevantes o enfrentarse a consultas malformadas— puede:

- **Iterar y reconsultar:** En lugar de devolver respuestas de bajo valor, el modelo intenta nuevas estrategias de búsqueda, reescribe consultas de bases de datos o analiza conjuntos de datos alternativos.
- **Usar herramientas diagnósticas:** El sistema puede invocar funciones adicionales diseñadas para ayudar a depurar sus pasos de razonamiento o confirmar la corrección de los datos recuperados. Herramientas como Azure AI Tracing serán importantes para permitir una observabilidad y monitoreo robustos.
- **Recurrir a la supervisión humana:** Para escenarios de alto riesgo o fallos repetidos, el modelo podría señalar incertidumbre y solicitar orientación humana. Una vez que el humano proporciona retroalimentación correctiva, el modelo puede incorporar esa lección para futuras ocasiones.

Este enfoque iterativo y dinámico permite que el modelo mejore continuamente, asegurando que no sea solo un sistema de un solo intento, sino uno que aprende de sus errores durante una sesión dada.

![Mecanismo de autocorrección](../../../translated_images/es/self-correction.da87f3783b7f174b.webp)

## Límites de la agencia

A pesar de su autonomía dentro de una tarea, Agentic RAG no es análogo a la Inteligencia Artificial General. Sus capacidades “agentic” están confinadas a las herramientas, fuentes de datos y políticas proporcionadas por desarrolladores humanos. No puede inventar sus propias herramientas ni salirse de los límites del dominio establecidos. Más bien, sobresale en la orquestación dinámica de los recursos disponibles.
Las diferencias clave respecto a formas de IA más avanzadas incluyen:

1. **Autonomía específica del dominio:** Los sistemas Agentic RAG se enfocan en alcanzar objetivos definidos por el usuario dentro de un dominio conocido, empleando estrategias como reescritura de consultas o selección de herramientas para mejorar resultados.
2. **Dependencia de infraestructura:** Las capacidades del sistema dependen de las herramientas y datos integrados por los desarrolladores. No puede superar estos límites sin intervención humana.
3. **Respeto por las directrices:** Las pautas éticas, reglas de cumplimiento y políticas empresariales siguen siendo muy importantes. La libertad del agente siempre está restringida por medidas de seguridad y mecanismos de supervisión (¡espero!).

## Casos de uso prácticos y valor

Agentic RAG destaca en escenarios que requieren refinamiento iterativo y precisión:

1. **Entornos con prioridad en la corrección:** En revisiones de cumplimiento, análisis regulatorios o investigaciones legales, el modelo agentic puede verificar repetidamente hechos, consultar múltiples fuentes y reescribir consultas hasta producir una respuesta plenamente validada.
2. **Interacciones complejas con bases de datos:** Al tratar con datos estructurados donde las consultas pueden fallar o necesitar ajustes, el sistema puede refinar autónomamente sus consultas usando Azure SQL o Microsoft Fabric OneLake, asegurando que la recuperación final se alinee con la intención del usuario.
3. **Flujos de trabajo extendidos:** Las sesiones de larga duración pueden evolucionar a medida que surge nueva información. Agentic RAG puede incorporar continuamente nuevos datos, cambiando estrategias conforme aprende más sobre el espacio del problema.

## Gobernanza, transparencia y confianza

A medida que estos sistemas se vuelven más autónomos en su razonamiento, la gobernanza y la transparencia son fundamentales:

- **Razonamiento explicable:** El modelo puede proporcionar una auditoría de las consultas realizadas, las fuentes consultadas y los pasos de razonamiento que siguió para llegar a su conclusión. Herramientas como Azure AI Content Safety y Azure AI Tracing / GenAIOps pueden ayudar a mantener la transparencia y mitigar riesgos.
- **Control de sesgos y recuperación equilibrada:** Los desarrolladores pueden ajustar estrategias de recuperación para garantizar que se consideren fuentes de datos equilibradas y representativas, y auditar regularmente los resultados para detectar sesgos o patrones distorsionados usando modelos personalizados para organizaciones avanzadas de ciencia de datos que usan Azure Machine Learning.
- **Supervisión humana y cumplimiento:** Para tareas sensibles, la revisión humana sigue siendo esencial. Agentic RAG no reemplaza el juicio humano en decisiones de alto impacto—lo complementa ofreciendo opciones más plenamente validadas.

Contar con herramientas que proporcionen un registro claro de las acciones es esencial. Sin ellas, depurar un proceso de múltiples pasos puede ser muy difícil. Ve el siguiente ejemplo de Literal AI (compañía detrás de Chainlit) para una ejecución de agente:

![Ejemplo de ejecución de agente](../../../translated_images/es/AgentRunExample.471a94bc40cbdc0c.webp)

## Conclusión

Agentic RAG representa una evolución natural en cómo los sistemas de IA manejan tareas complejas e intensivas en datos. Al adoptar un patrón de interacción en bucle, seleccionar autónomamente herramientas y refinar consultas hasta alcanzar un resultado de alta calidad, el sistema va más allá de seguir indicaciones estáticas hacia un tomador de decisiones más adaptativo y consciente del contexto. Aunque sigue limitado por infraestructuras definidas por humanos y directrices éticas, estas capacidades agente habilitan interacciones de IA más ricas, dinámicas y finalmente más útiles tanto para empresas como para usuarios finales.

### ¿Tienes más preguntas sobre Agentic RAG?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros estudiantes, asistir a horas de oficina y obtener respuestas a tus preguntas sobre agentes de IA.

## Recursos adicionales

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementar Retrieval Augmented Generation (RAG) con Azure OpenAI Service: Aprende a usar tus propios datos con Azure OpenAI Service. Este módulo de Microsoft Learn ofrece una guía completa para implementar RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluación de aplicaciones de IA generativa con Microsoft Foundry: Este artículo cubre la evaluación y comparación de modelos en conjuntos de datos públicos, incluyendo aplicaciones de IA agentic y arquitecturas RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Qué es Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Una guía completa sobre generación aumentada con recuperación basada en agentes – Noticias de generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: potencia tu RAG con reformulación de consultas y auto-consulta! Recetario de IA de código abierto de Hugging Face</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Añadiendo Capas Agentic a RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">El Futuro de los Asistentes de Conocimiento: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Cómo Construir Sistemas Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Usando Microsoft Foundry Agent Service para escalar tus agentes de IA</a>

### Artículos Académicos

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Refinamiento Iterativo con Auto-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Agentes de Lenguaje con Aprendizaje por Refuerzo Verbal</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Grandes Modelos de Lenguaje Pueden Autocorregirse con Crítica Interactiva con Herramientas</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Generación Aumentada por Recuperación Agentic: Una Encuesta sobre Agentic RAG</a>

## Prueba Rápida de Este Agente (Opcional)

Después de aprender a desplegar agentes en [Lección 16](../16-deploying-scalable-agents/README.md), puedes realizar una prueba rápida del `TravelRAGAgent` de esta lección — verificando que sus respuestas se mantengan basadas en la base de conocimientos — con [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Consulta [`tests/README.md`](../tests/README.md) para saber cómo ejecutarla.

## Lección Anterior

[Patrón de Diseño para Uso de Herramientas](../04-tool-use/README.md)

## Siguiente Lección

[Construyendo Agentes de IA Confiables](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->