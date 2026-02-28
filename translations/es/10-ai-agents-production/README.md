# Agentes de IA en Producción: Observabilidad y Evaluación

[![Agentes de IA en Producción](../../../translated_images/es/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

A medida que los agentes de IA pasan de prototipos experimentales a aplicaciones del mundo real, la capacidad de entender su comportamiento, supervisar su rendimiento y evaluar sistemáticamente sus resultados se vuelve importante.

## Objetivos de aprendizaje

Después de completar esta lección, sabrás/entenderás:
- Conceptos fundamentales de observabilidad y evaluación de agentes
- Técnicas para mejorar el rendimiento, los costos y la eficacia de los agentes
- Qué evaluar y cómo evaluar sistemáticamente tus agentes de IA
- Cómo controlar los costos al desplegar agentes de IA en producción
- Cómo instrumentar agentes construidos con Microsoft Agent Framework

El objetivo es capacitarte con el conocimiento para transformar tus agentes "caja negra" en sistemas transparentes, manejables y fiables.

_**Nota:** Es importante desplegar Agentes de IA que sean seguros y confiables. Consulta también la lección [Construir Agentes de IA Confiables](./06-building-trustworthy-agents/README.md)._

## Trazas y spans

Las herramientas de observabilidad como [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) suelen representar las ejecuciones de agentes como trazas y spans.

- **Traza** representa una tarea completa del agente de principio a fin (como manejar una consulta de usuario).
- **Spans** son pasos individuales dentro de la traza (como llamar a un modelo de lenguaje o recuperar datos).

![Árbol de trazas en Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sin observabilidad, un agente de IA puede sentirse como una "caja negra": su estado interno y razonamiento son opacos, lo que dificulta diagnosticar problemas u optimizar el rendimiento. Con observabilidad, los agentes se convierten en "cajas de cristal", ofreciendo transparencia que es vital para generar confianza y asegurar que operen como se espera. 

## Por qué la observabilidad importa en entornos de producción

La transición de agentes de IA a entornos de producción introduce un nuevo conjunto de desafíos y requisitos. La observabilidad ya no es un "lujo", sino una capacidad crítica:

*   **Depuración y análisis de la causa raíz**: Cuando un agente falla o produce una salida inesperada, las herramientas de observabilidad proporcionan las trazas necesarias para identificar la fuente del error. Esto es especialmente importante en agentes complejos que pueden implicar múltiples llamadas a LLM, interacciones con herramientas y lógica condicional.
*   **Latencia y gestión de costos**: Los agentes de IA a menudo dependen de LLMs y otras APIs externas que se facturan por token o por llamada. La observabilidad permite un seguimiento preciso de estas llamadas, ayudando a identificar operaciones que son excesivamente lentas o caras. Esto permite a los equipos optimizar prompts, seleccionar modelos más eficientes o rediseñar flujos de trabajo para controlar los costos operativos y garantizar una buena experiencia de usuario.
*   **Confianza, seguridad y cumplimiento**: En muchas aplicaciones, es importante asegurar que los agentes se comporten de manera segura y ética. La observabilidad proporciona una pista de auditoría de las acciones y decisiones del agente. Esto puede usarse para detectar y mitigar problemas como la inyección de prompts, la generación de contenido dañino o el manejo indebido de información de identificación personal (PII). Por ejemplo, puedes revisar trazas para entender por qué un agente proporcionó una respuesta determinada o utilizó una herramienta específica.
*   **Bucles de mejora continua**: Los datos de observabilidad son la base de un proceso de desarrollo iterativo. Al monitorear cómo se desempeñan los agentes en el mundo real, los equipos pueden identificar áreas de mejora, recopilar datos para ajustar modelos y validar el impacto de los cambios. Esto crea un bucle de retroalimentación donde los conocimientos de producción obtenidos mediante evaluación en línea informan la experimentación y el refinamiento fuera de línea, conduciendo a un rendimiento de agente progresivamente mejor.

## Métricas clave a rastrear

Para supervisar y entender el comportamiento del agente, se deben rastrear una serie de métricas y señales. Aunque las métricas específicas pueden variar según el propósito del agente, algunas son universalmente importantes.

Aquí están algunas de las métricas más comunes que monitorean las herramientas de observabilidad:

**Latencia:** ¿Qué tan rápido responde el agente? Los tiempos de espera largos impactan negativamente la experiencia del usuario. Debes medir la latencia para tareas y pasos individuales trazando las ejecuciones del agente. Por ejemplo, un agente que tarda 20 segundos en todas las llamadas al modelo podría acelerarse usando un modelo más rápido o ejecutando llamadas al modelo en paralelo.

**Costos:** ¿Cuál es el gasto por ejecución del agente? Los agentes de IA dependen de llamadas a LLM facturadas por token o de APIs externas. El uso frecuente de herramientas o múltiples prompts puede aumentar rápidamente los costos. Por ejemplo, si un agente llama a un LLM cinco veces por una mejora marginal en la calidad, debes evaluar si el costo está justificado o si podrías reducir el número de llamadas o usar un modelo más económico. El monitoreo en tiempo real también puede ayudar a identificar picos inesperados (p. ej., errores que causan bucles excesivos en la API).

**Errores de solicitud:** ¿Cuántas solicitudes falló el agente? Esto puede incluir errores de API o llamadas a herramientas fallidas. Para hacer tu agente más robusto contra estos fallos en producción, puedes configurar mecanismos de recuperación o reintentos. Por ejemplo, si el proveedor de LLM A está caído, cambias al proveedor de LLM B como respaldo.

**Retroalimentación del usuario:** Implementar evaluaciones directas de los usuarios proporciona información valiosa. Esto puede incluir valoraciones explícitas (👍me gusta/👎no me gusta, ⭐1-5 estrellas) o comentarios textuales. La retroalimentación negativa consistente debe alertarte, ya que es una señal de que el agente no está funcionando como se espera. 

**Retroalimentación implícita del usuario:** El comportamiento de los usuarios ofrece retroalimentación indirecta incluso sin valoraciones explícitas. Esto puede incluir reformulación inmediata de preguntas, consultas repetidas o clic en un botón de reintento. Por ejemplo, si ves que los usuarios preguntan repetidamente la misma cosa, es una señal de que el agente no está funcionando como se espera.

**Precisión:** ¿Con qué frecuencia el agente produce salidas correctas o deseables? Las definiciones de precisión varían (p. ej., corrección en la resolución de problemas, precisión en recuperación de información, satisfacción del usuario). El primer paso es definir cómo se ve el éxito para tu agente. Puedes rastrear la precisión mediante verificaciones automatizadas, puntuaciones de evaluación o etiquetas de finalización de tareas. Por ejemplo, marcar trazas como "exitoso" o "fallido". 

**Métricas de evaluación automatizada:** También puedes configurar evaluaciones automáticas. Por ejemplo, puedes usar un LLM para puntuar la salida del agente, p. ej., si es útil, precisa o no. También existen varias bibliotecas de código abierto que te ayudan a puntuar diferentes aspectos del agente. Por ejemplo, [RAGAS](https://docs.ragas.io/) para agentes RAG o [LLM Guard](https://llm-guard.com/) para detectar lenguaje dañino o inyección de prompts. 

En la práctica, una combinación de estas métricas ofrece la mejor cobertura del estado de salud de un agente de IA. En el [cuaderno de ejemplo](./code_samples/10-expense_claim-demo.ipynb) de este capítulo, te mostraremos cómo se ven estas métricas en ejemplos reales, pero primero aprenderemos cómo es un flujo de trabajo de evaluación típico.

## Instrumenta tu agente

Para recopilar datos de trazas, necesitarás instrumentar tu código. El objetivo es instrumentar el código del agente para emitir trazas y métricas que puedan ser capturadas, procesadas y visualizadas por una plataforma de observabilidad.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se ha consolidado como un estándar industrial para la observabilidad de LLM. Proporciona un conjunto de APIs, SDKs y herramientas para generar, recopilar y exportar datos de telemetría. 

Hay muchas bibliotecas de instrumentación que envuelven frameworks de agentes existentes y facilitan la exportación de spans de OpenTelemetry a una herramienta de observabilidad. Microsoft Agent Framework se integra con OpenTelemetry de forma nativa. A continuación hay un ejemplo sobre cómo instrumentar un agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # La ejecución del agente se rastrea automáticamente
    pass
```

El [cuaderno de ejemplo](./code_samples/10-expense_claim-demo.ipynb) en este capítulo demostrará cómo instrumentar tu agente MAF.

**Creación manual de spans:** Si bien las bibliotecas de instrumentación proporcionan una buena base, a menudo hay casos en los que se necesita información más detallada o personalizada. Puedes crear spans manualmente para añadir lógica de aplicación personalizada. Más importante aún, pueden enriquecer spans creados automática o manualmente con atributos personalizados (también conocidos como etiquetas o metadatos). Estos atributos pueden incluir datos específicos del negocio, cómputos intermedios o cualquier contexto que pueda ser útil para depuración o análisis, como `user_id`, `session_id` o `model_version`.

Ejemplo de creación de trazas y spans manualmente con el [SDK de Langfuse para Python](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluación del agente

La observabilidad nos da métricas, pero la evaluación es el proceso de analizar esos datos (y realizar pruebas) para determinar qué tan bien está desempeñándose un agente de IA y cómo se puede mejorar. En otras palabras, una vez que tienes esas trazas y métricas, ¿cómo las usas para juzgar al agente y tomar decisiones?

La evaluación regular es importante porque los agentes de IA suelen ser no deterministas y pueden evolucionar (a través de actualizaciones o deriva del comportamiento del modelo): sin evaluación, no sabrías si tu "agente inteligente" realmente está haciendo bien su trabajo o si ha empeorado.

Hay dos categorías de evaluaciones para agentes de IA: **evaluación en línea** y **evaluación fuera de línea**. Ambas son valiosas y se complementan. Normalmente comenzamos con la evaluación fuera de línea, ya que este es el paso mínimo necesario antes de desplegar cualquier agente.

### Evaluación fuera de línea

![Elementos del conjunto de datos en Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Esto implica evaluar al agente en un entorno controlado, típicamente usando conjuntos de prueba, no consultas de usuarios en vivo. Usas conjuntos de datos curados donde sabes cuál es la salida esperada o el comportamiento correcto, y luego ejecutas tu agente sobre esos datos. 

Por ejemplo, si construiste un agente para resolver problemas matemáticos de texto, podrías tener un [conjunto de prueba](https://huggingface.co/datasets/gsm8k) de 100 problemas con respuestas conocidas. La evaluación fuera de línea suele realizarse durante el desarrollo (y puede ser parte de pipelines de CI/CD) para verificar mejoras o proteger contra regresiones. El beneficio es que es **reproducible y puedes obtener métricas claras de precisión ya que tienes la verdad de referencia**. También podrías simular consultas de usuarios y medir las respuestas del agente frente a respuestas ideales o usar métricas automatizadas como se describió arriba. 

El reto clave con la evaluación fuera de línea es asegurar que tu conjunto de pruebas sea exhaustivo y se mantenga relevante: el agente puede desempeñarse bien en un conjunto de prueba fijo pero encontrar consultas muy diferentes en producción. Por lo tanto, debes mantener los conjuntos de prueba actualizados con nuevos casos límite y ejemplos que reflejen escenarios del mundo real​. Una mezcla de pequeños casos de "smoke test" y conjuntos de evaluación más grandes es útil: conjuntos pequeños para verificaciones rápidas y otros más grandes para métricas de rendimiento más amplias​.

### Evaluación en línea 

![Resumen de métricas de observabilidad](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Esto se refiere a evaluar al agente en un entorno en vivo, del mundo real, es decir, durante el uso real en producción. La evaluación en línea implica supervisar el rendimiento del agente en interacciones reales de usuarios y analizar los resultados de forma continua. 

Por ejemplo, podrías rastrear tasas de éxito, puntuaciones de satisfacción del usuario u otras métricas en tráfico en vivo. La ventaja de la evaluación en línea es que **captura cosas que podrías no anticipar en un laboratorio**: puedes observar la deriva del modelo a lo largo del tiempo (si la efectividad del agente se degrada conforme cambian los patrones de entrada) y detectar consultas o situaciones inesperadas que no estaban en tus datos de prueba​. Ofrece una imagen real de cómo se comporta el agente en el entorno real. 

La evaluación en línea a menudo implica recopilar retroalimentación implícita y explícita de los usuarios, como se comentó, y posiblemente ejecutar pruebas en sombra o pruebas A/B (donde una nueva versión del agente se ejecuta en paralelo para comparar con la anterior). El desafío es que puede ser complicado obtener etiquetas o puntuaciones confiables para interacciones en vivo: podrías depender de la retroalimentación del usuario o de métricas posteriores (como si el usuario hizo clic en el resultado). 

### Combinando ambos

La evaluación en línea y fuera de línea no son mutuamente excluyentes; se complementan mucho. Los conocimientos del monitoreo en línea (p. ej., nuevos tipos de consultas de usuarios donde el agente tiene bajo rendimiento) pueden usarse para aumentar y mejorar los conjuntos de pruebas fuera de línea. A la inversa, los agentes que se desempeñan bien en pruebas fuera de línea pueden desplegarse con más confianza y supervisarse en línea. 

De hecho, muchos equipos adoptan un ciclo:

_evaluar fuera de línea -> desplegar -> monitorizar en línea -> recopilar nuevos casos de fallo -> añadir al conjunto de datos fuera de línea -> refinar agente -> repetir_.

## Problemas comunes

Al desplegar agentes de IA en producción, puedes encontrar varios desafíos. Aquí hay algunos problemas comunes y sus posibles soluciones:

| **Problema**    | **Posible solución**   |
| ------------- | ------------------ |
| Agente de IA que no realiza las tareas consistentemente | - Refinar el prompt dado al Agente de IA; ser claro en los objetivos.<br>- Identificar dónde dividir las tareas en subtareas y manejarlas con varios agentes puede ayudar. |
| Agente de IA entrando en bucles continuos  | - Asegúrate de tener términos y condiciones de terminación claros para que el Agente sepa cuándo detener el proceso.<br>- Para tareas complejas que requieren razonamiento y planificación, usa un modelo más grande que esté especializado en tareas de razonamiento. |
| Las llamadas a herramientas del agente no están funcionando bien   | - Probar y validar la salida de la herramienta fuera del sistema del agente.<br>- Refinar los parámetros definidos, los prompts y la nomenclatura de las herramientas.  |
| Sistema multiagente que no funciona de forma consistente | - Refinar los prompts dados a cada agente para asegurarte de que sean específicos y distintos entre sí.<br>- Construir un sistema jerárquico usando un agente "enrutador" o controlador para determinar cuál agente es el correcto. |

Muchos de estos problemas pueden identificarse de forma más efectiva con observabilidad implementada. Las trazas y métricas que discutimos anteriormente ayudan a localizar exactamente dónde en el flujo de trabajo del agente ocurren los problemas, haciendo que la depuración y la optimización sean mucho más eficientes.

## Gestión de costos
Aquí hay algunas estrategias para gestionar los costos de desplegar agentes de IA en producción:

**Uso de modelos más pequeños:** Los Modelos de Lenguaje Pequeños (SLMs) pueden desempeñarse bien en determinados casos de uso con agentes y reducirán los costos significativamente. Como se mencionó anteriormente, construir un sistema de evaluación para determinar y comparar el rendimiento frente a modelos más grandes es la mejor manera de entender qué tan bien se desempeñará un SLM en tu caso de uso. Considera usar SLMs para tareas más sencillas como clasificación de intención o extracción de parámetros, mientras reservas modelos más grandes para razonamiento complejo.

**Uso de un modelo enrutador:** Una estrategia similar es usar una diversidad de modelos y tamaños. Puedes usar un LLM/SLM o una función sin servidor para enrutar las solicitudes según la complejidad hacia los modelos más adecuados. Esto también ayudará a reducir costos y a garantizar el rendimiento en las tareas correctas. Por ejemplo, dirige consultas simples a modelos más pequeños y rápidos, y utiliza los modelos grandes y costosos solo para tareas de razonamiento complejo.

**Caché de respuestas:** Identificar solicitudes y tareas comunes y proporcionar las respuestas antes de que pasen por tu sistema basado en agentes es una buena manera de reducir el volumen de solicitudes similares. Incluso puedes implementar un flujo para identificar cuán similar es una solicitud a tus solicitudes en caché usando modelos de IA más básicos. Esta estrategia puede reducir significativamente los costos para preguntas frecuentes o flujos de trabajo comunes.

## Veamos cómo funciona esto en la práctica

En el [cuaderno de ejemplo de esta sección](./code_samples/10-expense_claim-demo.ipynb), veremos ejemplos de cómo podemos usar herramientas de observabilidad para supervisar y evaluar a nuestro agente.


### ¿Tienes más preguntas sobre agentes de IA en producción?

Únete al [Discord de Microsoft Foundry](https://aka.ms/ai-agents/discord) para reunirte con otros aprendices, asistir a horas de oficina y obtener respuestas a tus preguntas sobre agentes de IA.

## Lección anterior

[Patrón de diseño de metacognición](../09-metacognition/README.md)

## Siguiente lección

[Protocolos agentivos](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Descargo de responsabilidad:
Este documento ha sido traducido utilizando el servicio de traducción por IA Co-op Translator (https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por traductores humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->