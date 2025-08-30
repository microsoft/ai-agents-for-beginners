<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cdfd0acc8592c1af14f8637833450375",
  "translation_date": "2025-08-30T07:09:42+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "es"
}
-->
# Agentes de IA en Producción: Observabilidad y Evaluación

[![Agentes de IA en Producción](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.es.png)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

A medida que los agentes de IA pasan de ser prototipos experimentales a aplicaciones del mundo real, la capacidad de comprender su comportamiento, monitorear su rendimiento y evaluar sistemáticamente sus resultados se vuelve crucial.

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo/entenderás:
- Conceptos fundamentales de observabilidad y evaluación de agentes
- Técnicas para mejorar el rendimiento, los costos y la efectividad de los agentes
- Qué evaluar y cómo hacerlo de manera sistemática en tus agentes de IA
- Cómo controlar los costos al implementar agentes de IA en producción
- Cómo instrumentar agentes construidos con AutoGen

El objetivo es proporcionarte el conocimiento necesario para transformar tus agentes de "caja negra" en sistemas transparentes, manejables y confiables.

_**Nota:** Es importante implementar agentes de IA que sean seguros y confiables. Consulta la lección [Construyendo Agentes de IA Confiables](./06-building-trustworthy-agents/README.md) también._

## Trazas y Spans

Las herramientas de observabilidad como [Langfuse](https://langfuse.com/) o [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) suelen representar las ejecuciones de los agentes como trazas y spans.

- **Traza** representa una tarea completa del agente desde el inicio hasta el final (como manejar una consulta de usuario).
- **Spans** son pasos individuales dentro de la traza (como llamar a un modelo de lenguaje o recuperar datos).

![Árbol de trazas en Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Sin observabilidad, un agente de IA puede sentirse como una "caja negra": su estado interno y razonamiento son opacos, lo que dificulta diagnosticar problemas u optimizar el rendimiento. Con observabilidad, los agentes se convierten en "cajas de cristal", ofreciendo transparencia que es vital para generar confianza y garantizar que operen según lo previsto.

## Por qué la Observabilidad es Importante en Entornos de Producción

La transición de los agentes de IA a entornos de producción introduce un nuevo conjunto de desafíos y requisitos. La observabilidad deja de ser un "lujo" y se convierte en una capacidad crítica:

*   **Depuración y Análisis de Causas Raíz**: Cuando un agente falla o produce un resultado inesperado, las herramientas de observabilidad proporcionan las trazas necesarias para identificar la fuente del error. Esto es especialmente importante en agentes complejos que pueden involucrar múltiples llamadas a LLM, interacciones con herramientas y lógica condicional.
*   **Gestión de Latencia y Costos**: Los agentes de IA suelen depender de LLMs y otras APIs externas que se facturan por token o por llamada. La observabilidad permite un seguimiento preciso de estas llamadas, ayudando a identificar operaciones que son excesivamente lentas o costosas. Esto permite a los equipos optimizar prompts, seleccionar modelos más eficientes o rediseñar flujos de trabajo para gestionar costos operativos y garantizar una buena experiencia de usuario.
*   **Confianza, Seguridad y Cumplimiento**: En muchas aplicaciones, es importante garantizar que los agentes se comporten de manera segura y ética. La observabilidad proporciona un registro de auditoría de las acciones y decisiones del agente. Esto puede usarse para detectar y mitigar problemas como la inyección de prompts, la generación de contenido dañino o el manejo indebido de información personal identificable (PII). Por ejemplo, puedes revisar trazas para entender por qué un agente proporcionó una cierta respuesta o utilizó una herramienta específica.
*   **Bucles de Mejora Continua**: Los datos de observabilidad son la base de un proceso de desarrollo iterativo. Al monitorear cómo los agentes se desempeñan en el mundo real, los equipos pueden identificar áreas de mejora, recopilar datos para ajustar modelos y validar el impacto de los cambios. Esto crea un bucle de retroalimentación donde los conocimientos de producción obtenidos de la evaluación en línea informan la experimentación y refinamiento fuera de línea, llevando a un rendimiento progresivamente mejor de los agentes.

## Métricas Clave para Monitorear

Para monitorear y comprender el comportamiento de los agentes, se deben rastrear una variedad de métricas y señales. Aunque las métricas específicas pueden variar según el propósito del agente, algunas son universalmente importantes.

Aquí están algunas de las métricas más comunes que las herramientas de observabilidad monitorean:

**Latencia:** ¿Qué tan rápido responde el agente? Los tiempos de espera prolongados impactan negativamente la experiencia del usuario. Debes medir la latencia de las tareas y los pasos individuales trazando las ejecuciones del agente. Por ejemplo, un agente que tarda 20 segundos en todas las llamadas al modelo podría acelerarse utilizando un modelo más rápido o ejecutando las llamadas al modelo en paralelo.

**Costos:** ¿Cuál es el costo por ejecución del agente? Los agentes de IA dependen de llamadas a LLM que se facturan por token o APIs externas. El uso frecuente de herramientas o múltiples prompts puede aumentar rápidamente los costos. Por ejemplo, si un agente llama a un LLM cinco veces para una mejora marginal en la calidad, debes evaluar si el costo está justificado o si podrías reducir el número de llamadas o usar un modelo más económico. El monitoreo en tiempo real también puede ayudar a identificar picos inesperados (por ejemplo, errores que causan bucles excesivos de API).

**Errores de Solicitud:** ¿Cuántas solicitudes fallaron en el agente? Esto puede incluir errores de API o llamadas fallidas a herramientas. Para hacer que tu agente sea más robusto en producción, puedes configurar alternativas o reintentos. Por ejemplo, si el proveedor de LLM A está caído, cambias al proveedor de LLM B como respaldo.

**Retroalimentación del Usuario:** Implementar evaluaciones directas de los usuarios proporciona información valiosa. Esto puede incluir calificaciones explícitas (👍pulgar arriba/👎abajo, ⭐1-5 estrellas) o comentarios textuales. La retroalimentación negativa constante debería alertarte, ya que es una señal de que el agente no está funcionando como se espera.

**Retroalimentación Implícita del Usuario:** Los comportamientos de los usuarios proporcionan retroalimentación indirecta incluso sin calificaciones explícitas. Esto puede incluir reformulación inmediata de preguntas, consultas repetidas o hacer clic en un botón de reintento. Por ejemplo, si ves que los usuarios preguntan repetidamente lo mismo, esto es una señal de que el agente no está funcionando como se espera.

**Precisión:** ¿Con qué frecuencia el agente produce resultados correctos o deseables? Las definiciones de precisión varían (por ejemplo, corrección en la resolución de problemas, precisión en la recuperación de información, satisfacción del usuario). El primer paso es definir cómo se ve el éxito para tu agente. Puedes rastrear la precisión mediante verificaciones automatizadas, puntuaciones de evaluación o etiquetas de finalización de tareas. Por ejemplo, marcar trazas como "exitosas" o "fallidas".

**Métricas de Evaluación Automatizada:** También puedes configurar evaluaciones automatizadas. Por ejemplo, puedes usar un LLM para calificar la salida del agente, evaluando si es útil, precisa o no. También hay varias bibliotecas de código abierto que te ayudan a calificar diferentes aspectos del agente. Por ejemplo, [RAGAS](https://docs.ragas.io/) para agentes RAG o [LLM Guard](https://llm-guard.com/) para detectar lenguaje dañino o inyección de prompts.

En la práctica, una combinación de estas métricas ofrece la mejor cobertura de la salud de un agente de IA. En el [notebook de ejemplo](./code_samples/10_autogen_evaluation.ipynb) de este capítulo, te mostraremos cómo se ven estas métricas en ejemplos reales, pero primero aprenderemos cómo se ve un flujo típico de evaluación.

## Instrumenta tu Agente

Para recopilar datos de trazas, necesitarás instrumentar tu código. El objetivo es instrumentar el código del agente para emitir trazas y métricas que puedan ser capturadas, procesadas y visualizadas por una plataforma de observabilidad.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se ha convertido en un estándar de la industria para la observabilidad de LLM. Proporciona un conjunto de APIs, SDKs y herramientas para generar, recopilar y exportar datos de telemetría.

Existen muchas bibliotecas de instrumentación que envuelven los marcos de trabajo de agentes existentes y facilitan la exportación de spans de OpenTelemetry a una herramienta de observabilidad. A continuación, se muestra un ejemplo de cómo instrumentar un agente de AutoGen con la biblioteca de instrumentación [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

El [notebook de ejemplo](./code_samples/10_autogen_evaluation.ipynb) en este capítulo demostrará cómo instrumentar tu agente AutoGen.

**Creación Manual de Spans:** Aunque las bibliotecas de instrumentación proporcionan una buena base, a menudo hay casos donde se necesita información más detallada o personalizada. Puedes crear spans manualmente para agregar lógica personalizada de la aplicación. Más importante aún, pueden enriquecer spans creados automáticamente o manualmente con atributos personalizados (también conocidos como etiquetas o metadatos). Estos atributos pueden incluir datos específicos del negocio, cálculos intermedios o cualquier contexto que pueda ser útil para depuración o análisis, como `user_id`, `session_id` o `model_version`.

Ejemplo de creación de trazas y spans manualmente con el [SDK de Python de Langfuse](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluación de Agentes

La observabilidad nos da métricas, pero la evaluación es el proceso de analizar esos datos (y realizar pruebas) para determinar qué tan bien está funcionando un agente de IA y cómo puede mejorarse. En otras palabras, una vez que tienes esas trazas y métricas, ¿cómo las usas para juzgar al agente y tomar decisiones?

La evaluación regular es importante porque los agentes de IA suelen ser no deterministas y pueden evolucionar (a través de actualizaciones o cambios en el comportamiento del modelo). Sin evaluación, no sabrías si tu "agente inteligente" realmente está haciendo bien su trabajo o si ha retrocedido.

Hay dos categorías de evaluaciones para agentes de IA: **evaluación en línea** y **evaluación fuera de línea**. Ambas son valiosas y se complementan entre sí. Por lo general, comenzamos con la evaluación fuera de línea, ya que este es el paso mínimo necesario antes de implementar cualquier agente.

### Evaluación Fuera de Línea

![Elementos del dataset en Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Esto implica evaluar al agente en un entorno controlado, generalmente utilizando conjuntos de datos de prueba, no consultas de usuarios en vivo. Usas conjuntos de datos curados donde sabes cuál es el resultado esperado o el comportamiento correcto, y luego ejecutas tu agente en ellos.

Por ejemplo, si construiste un agente para resolver problemas matemáticos, podrías tener un [conjunto de datos de prueba](https://huggingface.co/datasets/gsm8k) de 100 problemas con respuestas conocidas. La evaluación fuera de línea se realiza a menudo durante el desarrollo (y puede formar parte de los pipelines de CI/CD) para verificar mejoras o proteger contra regresiones. El beneficio es que es **repetible y puedes obtener métricas claras de precisión, ya que tienes la verdad absoluta**. También podrías simular consultas de usuarios y medir las respuestas del agente frente a respuestas ideales o usar métricas automatizadas como se describió anteriormente.

El desafío clave con la evaluación fuera de línea es garantizar que tu conjunto de datos de prueba sea completo y se mantenga relevante: el agente podría desempeñarse bien en un conjunto de prueba fijo pero enfrentar consultas muy diferentes en producción. Por lo tanto, debes mantener los conjuntos de prueba actualizados con nuevos casos límite y ejemplos que reflejen escenarios del mundo real. Una mezcla de pequeños casos de "prueba de humo" y conjuntos de evaluación más grandes es útil: conjuntos pequeños para verificaciones rápidas y conjuntos más grandes para métricas de rendimiento más amplias.

### Evaluación en Línea

![Resumen de métricas de observabilidad](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Esto se refiere a evaluar al agente en un entorno en vivo, en el mundo real, es decir, durante el uso real en producción. La evaluación en línea implica monitorear el rendimiento del agente en interacciones reales con usuarios y analizar los resultados de manera continua.

Por ejemplo, podrías rastrear tasas de éxito, puntuaciones de satisfacción del usuario u otras métricas en tráfico en vivo. La ventaja de la evaluación en línea es que **captura cosas que podrías no anticipar en un entorno de laboratorio**: puedes observar el cambio del modelo con el tiempo (si la efectividad del agente se degrada a medida que cambian los patrones de entrada) y detectar consultas inesperadas o situaciones que no estaban en tus datos de prueba. Proporciona una imagen real de cómo se comporta el agente en el mundo real.

La evaluación en línea a menudo implica recopilar retroalimentación implícita y explícita de los usuarios, como se discutió, y posiblemente ejecutar pruebas en paralelo o pruebas A/B (donde una nueva versión del agente se ejecuta en paralelo para comparar con la antigua). El desafío es que puede ser complicado obtener etiquetas o puntuaciones confiables para interacciones en vivo: podrías depender de la retroalimentación de los usuarios o métricas posteriores (como si el usuario hizo clic en el resultado).

### Combinando ambas

Las evaluaciones en línea y fuera de línea no son mutuamente excluyentes; se complementan altamente. Los conocimientos obtenidos del monitoreo en línea (por ejemplo, nuevos tipos de consultas de usuarios donde el agente tiene un rendimiento deficiente) pueden usarse para ampliar y mejorar los conjuntos de datos de prueba fuera de línea. Por otro lado, los agentes que se desempeñan bien en pruebas fuera de línea pueden implementarse y monitorearse en línea con mayor confianza.

De hecho, muchos equipos adoptan un bucle:

_evaluar fuera de línea -> implementar -> monitorear en línea -> recopilar nuevos casos de falla -> agregar al conjunto de datos fuera de línea -> refinar agente -> repetir_.

## Problemas Comunes

A medida que implementas agentes de IA en producción, puedes encontrarte con varios desafíos. Aquí hay algunos problemas comunes y sus posibles soluciones:

| **Problema**    | **Solución Potencial**   |
| ------------- | ------------------ |
| El agente de IA no realiza tareas de manera consistente | - Refinar el prompt dado al agente de IA; ser claro en los objetivos.<br>- Identificar dónde dividir las tareas en subtareas y manejarlas con múltiples agentes puede ayudar. |
| El agente de IA entra en bucles continuos  | - Asegúrate de tener términos y condiciones claros de finalización para que el agente sepa cuándo detener el proceso. |

## Evaluación y Optimización

### Identificación de Problemas Comunes

Aquí hay algunos problemas comunes que pueden surgir al trabajar con sistemas de agentes de IA, junto con estrategias para abordarlos:

| **Problema**                                   | **Solución**                                                                                     |
|------------------------------------------------|--------------------------------------------------------------------------------------------------|
| El modelo no responde correctamente            | - Ajusta los datos de entrenamiento para incluir ejemplos más relevantes.<br>- Revisa los prompts para asegurarte de que sean claros y específicos. |
| El modelo tarda demasiado en responder         | - Usa modelos más pequeños para tareas simples.<br>- Optimiza el flujo de trabajo para reducir la latencia. |
| El modelo no maneja tareas complejas           | - Para tareas complejas que requieren razonamiento y planificación, utiliza un modelo más grande especializado en estas tareas. |
| Las herramientas del agente de IA no funcionan bien | - Prueba y valida la salida de las herramientas fuera del sistema del agente.<br>- Refina los parámetros definidos, los prompts y los nombres de las herramientas. |
| El sistema multi-agente no es consistente      | - Ajusta los prompts dados a cada agente para asegurarte de que sean específicos y distintos entre sí.<br>- Construye un sistema jerárquico utilizando un agente "enrutador" o controlador para determinar cuál agente es el adecuado. |

Muchos de estos problemas pueden identificarse de manera más efectiva si se cuenta con herramientas de observabilidad. Las trazas y métricas que discutimos anteriormente ayudan a identificar exactamente dónde ocurren los problemas en el flujo de trabajo del agente, haciendo que la depuración y la optimización sean mucho más eficientes.

## Gestión de Costos

Aquí tienes algunas estrategias para gestionar los costos de implementar agentes de IA en producción:

**Uso de Modelos Más Pequeños:** Los Modelos de Lenguaje Pequeños (SLMs, por sus siglas en inglés) pueden funcionar bien en ciertos casos de uso de agentes y reducir significativamente los costos. Como se mencionó anteriormente, construir un sistema de evaluación para determinar y comparar el rendimiento frente a modelos más grandes es la mejor manera de entender qué tan bien un SLM se ajustará a tu caso de uso. Considera usar SLMs para tareas más simples como clasificación de intenciones o extracción de parámetros, reservando los modelos más grandes para razonamientos complejos.

**Uso de un Modelo Enrutador:** Una estrategia similar es usar una diversidad de modelos y tamaños. Puedes usar un LLM/SLM o una función sin servidor para enrutar solicitudes según su complejidad hacia los modelos más adecuados. Esto también ayudará a reducir costos mientras se asegura el rendimiento en las tareas correctas. Por ejemplo, enruta consultas simples a modelos más pequeños y rápidos, y utiliza modelos grandes y costosos solo para tareas de razonamiento complejo.

**Caché de Respuestas:** Identificar solicitudes y tareas comunes y proporcionar las respuestas antes de que pasen por tu sistema de agentes es una buena manera de reducir el volumen de solicitudes similares. Incluso puedes implementar un flujo para identificar qué tan similar es una solicitud a tus solicitudes en caché utilizando modelos de IA más básicos. Esta estrategia puede reducir significativamente los costos para preguntas frecuentes o flujos de trabajo comunes.

## Veamos cómo funciona esto en la práctica

En el [notebook de ejemplo de esta sección](./code_samples/10_autogen_evaluation.ipynb), veremos ejemplos de cómo podemos usar herramientas de observabilidad para monitorear y evaluar nuestro agente.

### ¿Tienes Más Preguntas sobre Agentes de IA en Producción?

Únete al [Discord de Azure AI Foundry](https://aka.ms/ai-agents/discord) para conectarte con otros estudiantes, asistir a horas de oficina y resolver tus dudas sobre agentes de IA.

## Lección Anterior

[Patrón de Diseño de Metacognición](../09-metacognition/README.md)

## Próxima Lección

[Protocolos Agénticos](../11-agentic-protocols/README.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.