# Agentes de IA en Producción: Observabilidad y Evaluación

[![Agentes de IA en Producción](../../../translated_images/es/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

A medida que los agentes de IA pasan de ser prototipos experimentales a aplicaciones del mundo real, se vuelve importante la capacidad de entender su comportamiento, monitorear su desempeño y evaluar sistemáticamente sus resultados.

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo / comprenderás:
- Conceptos básicos de la observabilidad y evaluación de agentes
- Técnicas para mejorar el rendimiento, costos y efectividad de los agentes
- Qué y cómo evaluar sistemáticamente tus agentes de IA
- Cómo controlar costos al desplegar agentes de IA en producción
- Cómo instrumentar agentes construidos con Microsoft Agent Framework

El objetivo es proveerte del conocimiento para transformar tus agentes "caja negra" en sistemas transparentes, manejables y confiables.

_**Nota:** Es importante desplegar agentes de IA que sean seguros y confiables. Revisa también la lección [Construyendo Agentes de IA Confiables](../06-building-trustworthy-agents/README.md)._

## Rastreos y Span

Las herramientas de observabilidad como [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) suelen representar ejecuciones de agentes como rastreos y spans.

- **Rastreo** representa una tarea completa de un agente de principio a fin (como manejar una consulta de usuario).
- **Spans** son pasos individuales dentro del rastreo (como llamar a un modelo de lenguaje o recuperar datos).

![Árbol de rastreo en Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sin observabilidad, un agente de IA puede sentirse como una "caja negra": su estado interno y razonamiento son opacos, dificultando diagnosticar problemas o optimizar el rendimiento. Con observabilidad, los agentes se convierten en "cajas de vidrio", ofreciendo transparencia vital para generar confianza y asegurar que operen como se espera.

## Por qué Importa la Observabilidad en Entornos de Producción

La transición de agentes de IA a entornos de producción introduce un nuevo conjunto de desafíos y requerimientos. La observabilidad deja de ser un "algo deseable" para ser una capacidad crítica:

*   **Depuración y Análisis de la Causa Raíz**: Cuando un agente falla o produce un resultado inesperado, las herramientas de observabilidad proporcionan los rastreos necesarios para localizar la fuente del error. Esto es especialmente importante en agentes complejos que pueden involucrar múltiples llamadas a LLM, interacciones con herramientas y lógica condicional.
*   **Gestión de Latencia y Costos**: Los agentes de IA a menudo dependen de LLMs y otras APIs externas que se facturan por token o llamada. La observabilidad permite un seguimiento preciso de estas llamadas, ayudando a identificar operaciones demasiado lentas o costosas. Esto permite a los equipos optimizar prompts, seleccionar modelos más eficientes o rediseñar flujos de trabajo para administrar costos operativos y asegurar una buena experiencia de usuario.
*   **Confianza, Seguridad y Cumplimiento**: En muchas aplicaciones, es importante garantizar que los agentes se comporten de manera segura y ética. La observabilidad proporciona una pista de auditoría de acciones y decisiones del agente. Esto se puede usar para detectar y mitigar problemas como la inyección de prompts, la generación de contenido dañino o el manejo inadecuado de información personal identificable (PII). Por ejemplo, puedes revisar rastreos para entender por qué un agente proporcionó una respuesta específica o usó una herramienta determinada.
*   **Bucles de Mejora Continua**: Los datos de observabilidad son la base de un proceso iterativo de desarrollo. Al monitorear cómo los agentes se desempeñan en el mundo real, los equipos pueden identificar áreas de mejora, recopilar datos para afinar modelos y validar el impacto de cambios. Esto crea un ciclo de retroalimentación donde las perspectivas de producción desde la evaluación en línea informan la experimentación y refinamiento fuera de línea, conduciendo a un mejor desempeño progresivo del agente.

## Métricas Clave a Rastrear

Para monitorear y entender el comportamiento del agente, se debe rastrear una variedad de métricas y señales. Aunque las métricas específicas pueden variar según el propósito del agente, algunas son universalmente importantes.

Aquí algunas de las métricas más comunes que monitorean las herramientas de observabilidad:

**Latencia:** ¿Qué tan rápido responde el agente? Los tiempos de espera largos afectan negativamente la experiencia del usuario. Debes medir la latencia para tareas y pasos individuales trazando ejecuciones de agentes. Por ejemplo, un agente que toma 20 segundos para todas las llamadas a modelos podría acelerarse usando un modelo más rápido o ejecutando las llamadas en paralelo.

**Costos:** ¿Cuál es el gasto por ejecución del agente? Los agentes de IA dependen de llamadas a LLM facturadas por token o APIs externas. El uso frecuente de herramientas o múltiples prompts puede aumentar los costos rápidamente. Por ejemplo, si un agente llama a un LLM cinco veces para una mejora marginal en calidad, debes evaluar si el costo está justificado o si podrías reducir el número de llamadas o usar un modelo más barato. El monitoreo en tiempo real también puede ayudar a identificar picos inesperados (p. ej., errores que causan bucles excesivos en la API).

**Errores de Solicitud:** ¿Cuántas solicitudes falló el agente? Esto puede incluir errores en APIs o llamadas fallidas a herramientas. Para hacer tu agente más robusto contra esto en producción, puedes entonces establecer planes de contingencia o reintentos. Por ejemplo, si el proveedor de LLM A falla, cambias al proveedor B como respaldo.

**Retroalimentación del Usuario:** Implementar evaluaciones directas de usuarios brinda insights valiosos. Esto puede incluir calificaciones explícitas (👍pulgar arriba/👎abajo, ⭐1-5 estrellas) o comentarios textuales. Retroalimentación negativa consistente debería alertarte ya que es señal de que el agente no funciona como se espera.

**Retroalimentación Implícita del Usuario:** Los comportamientos de los usuarios brindan feedback indirecto incluso sin calificaciones explícitas. Esto puede incluir reformulación inmediata de preguntas, consultas repetidas o hacer clic en un botón de reintento. Por ejemplo, si ves que los usuarios preguntan repetidamente la misma cuestión, es señal de que el agente no funciona como se espera.

**Precisión:** ¿Con qué frecuencia el agente produce resultados correctos o deseables? Las definiciones de precisión varían (p. ej., corrección en resolución de problemas, precisión en recuperación de información, satisfacción del usuario). El primer paso es definir qué significa éxito para tu agente. Puedes rastrear precisión mediante verificaciones automáticas, puntuaciones de evaluación o etiquetas de tarea completada. Por ejemplo, marcando rastreos como "exitosos" o "fallidos".

**Métricas de Evaluación Automatizada:** También puedes configurar evaluaciones automáticas. Por ejemplo, puedes usar un LLM para puntuar la salida del agente, p. ej., si es útil, precisa o no. Hay varias bibliotecas de código abierto que te ayudan a puntuar diferentes aspectos del agente. Por ejemplo [RAGAS](https://docs.ragas.io/) para agentes RAG o [LLM Guard](https://github.com/protectai/llm-guard) para detectar lenguaje dañino o inyección de prompts.

En la práctica, una combinación de estas métricas ofrece la mejor cobertura del estado de un agente de IA. En el [notebook de ejemplo](./code_samples/10-expense_claim-demo.ipynb) de este capítulo, te mostraremos cómo se ven estas métricas en ejemplos reales pero primero, aprenderemos cómo es un flujo típico de evaluación.

## Instrumenta tu Agente

Para recopilar datos de rastreo, necesitarás instrumentar tu código. El objetivo es instrumentar el código del agente para emitir trazas y métricas que puedan ser capturadas, procesadas y visualizadas por una plataforma de observabilidad.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) ha emergido como un estándar de la industria para la observabilidad de LLM. Proporciona un conjunto de APIs, SDKs y herramientas para generar, recopilar y exportar datos de telemetría.

Existen muchas bibliotecas de instrumentación que envuelven marcos de agentes existentes y facilitan la exportación de spans de OpenTelemetry a una herramienta de observabilidad. Microsoft Agent Framework se integra con OpenTelemetry de manera nativa. A continuación se muestra un ejemplo de cómo instrumentar un agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # La ejecución del agente se rastrea automáticamente
    pass
```

El [cuaderno de ejemplo](./code_samples/10-expense_claim-demo.ipynb) en este capítulo demostrará cómo instrumentar tu agente MAF.

**Creación manual de spans:** Aunque las bibliotecas de instrumentación proporcionan una buena base, a menudo hay casos donde se necesita información más detallada o personalizada. Puedes crear spans manualmente para agregar lógica personalizada a la aplicación. Más importante aún, pueden enriquecer los spans creados automática o manualmente con atributos personalizados (también conocidos como etiquetas o metadatos). Estos atributos pueden incluir datos específicos del negocio, cálculos intermedios o cualquier contexto que pueda ser útil para la depuración o el análisis, como `user_id`, `session_id` o `model_version`.

Ejemplo de creación manual de trazas y spans con el [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluación del Agente

La observabilidad nos proporciona métricas, pero la evaluación es el proceso de analizar esos datos (y realizar pruebas) para determinar qué tan bien está desempeñando un agente de IA y cómo se puede mejorar. En otras palabras, una vez que tienes esas trazas y métricas, ¿cómo las usas para juzgar al agente y tomar decisiones?

La evaluación regular es importante porque los agentes de IA a menudo son no deterministas y pueden evolucionar (mediante actualizaciones o cambios en el comportamiento del modelo); sin evaluación, no sabrías si tu “agente inteligente” está haciendo bien su trabajo o si ha regresado.

Hay dos categorías de evaluaciones para agentes de IA: **evaluación en línea** y **evaluación fuera de línea**. Ambas son valiosas y se complementan. Generalmente comenzamos con la evaluación fuera de línea, ya que es el paso mínimo necesario antes de desplegar cualquier agente.

### Evaluación fuera de línea

![Elementos del conjunto de datos en Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Esto implica evaluar al agente en un entorno controlado, típicamente usando conjuntos de datos de prueba, no consultas en vivo de usuarios. Utilizas conjuntos de datos seleccionados donde sabes cuál es la salida esperada o el comportamiento correcto, y luego ejecutas tu agente sobre esos.

Por ejemplo, si construiste un agente para resolver problemas de palabras matemáticos, podrías tener un [conjunto de datos de prueba](https://huggingface.co/datasets/openai/gsm8k) de 100 problemas con respuestas conocidas. La evaluación fuera de línea a menudo se realiza durante el desarrollo (y puede formar parte de pipelines CI/CD) para verificar mejoras o prevenir regresiones. La ventaja es que es **repetible y puedes obtener métricas claras de precisión porque tienes la verdad de terreno**. También puedes simular consultas de usuario y medir las respuestas del agente contra respuestas ideales o usar métricas automatizadas como se describió anteriormente.

El principal desafío con la evaluación fuera de línea es garantizar que tu conjunto de datos de prueba sea completo y se mantenga relevante: el agente podría funcionar bien en un conjunto fijo de prueba pero enfrentarse a consultas muy diferentes en producción. Por lo tanto, debes mantener los conjuntos de prueba actualizados con nuevos casos extremos y ejemplos que reflejen escenarios del mundo real. Una mezcla de pequeños casos de “prueba rápida” y conjuntos de evaluación más grandes es útil: conjuntos pequeños para verificaciones rápidas y otros más amplios para métricas de rendimiento generales.

### Evaluación en línea

![Resumen de métricas de observabilidad](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Esto se refiere a evaluar al agente en un entorno real y en vivo, es decir, durante el uso real en producción. La evaluación en línea implica monitorear el desempeño del agente en interacciones reales con usuarios y analizar resultados continuamente.

Por ejemplo, podrías rastrear tasas de éxito, puntuaciones de satisfacción del usuario u otras métricas sobre tráfico en vivo. La ventaja de la evaluación en línea es que **captura cosas que podrías no anticipar en un entorno de laboratorio**: puedes observar la deriva del modelo con el tiempo (si la efectividad del agente se degrada a medida que cambian los patrones de entrada) y detectar consultas o situaciones inesperadas que no estaban en tus datos de prueba. Proporciona una imagen real de cómo se comporta el agente en el mundo real.

La evaluación en línea a menudo implica recopilar retroalimentación implícita y explícita de usuarios, como se discutió, y posiblemente ejecutar pruebas sombra o pruebas A/B (donde una nueva versión del agente funciona en paralelo para comparar con la anterior). El desafío es que puede ser complicado obtener etiquetas o puntuaciones fiables para interacciones en vivo: podrías depender de retroalimentación de usuarios o métricas descendentes (como si el usuario hizo clic en el resultado).

### Combinando ambas

Las evaluaciones en línea y fuera de línea no son mutuamente excluyentes; son altamente complementarias. Los insights del monitoreo en línea (por ejemplo, nuevos tipos de consultas de usuario donde el agente tiene bajo rendimiento) pueden usarse para incrementar y mejorar los conjuntos de datos de prueba fuera de línea. A la inversa, los agentes que rinden bien en pruebas fuera de línea pueden ser desplegados con más confianza y monitoreados en línea.

De hecho, muchos equipos adoptan un ciclo:

_evaluar fuera de línea -> desplegar -> monitorear en línea -> recolectar nuevos casos de fallo -> agregar al conjunto de datos fuera de línea -> refinar agente -> repetir_.

## Problemas Comunes

Al desplegar agentes de IA en producción, puedes encontrarte con varios desafíos. Aquí hay algunos problemas comunes y sus posibles soluciones:

| **Problema**    | **Solución Potencial**   |
| ------------- | ------------------ |
| El agente de IA no realiza tareas consistentemente | - Refinar el prompt dado al agente de IA; ser claro en los objetivos.<br>- Identificar dónde dividir las tareas en subtareas y manejarlas por múltiples agentes puede ayudar. |
| El agente de IA entra en bucles continuos | - Asegurar que tienes términos y condiciones claros de terminación para que el agente sepa cuándo detener el proceso.<br>- Para tareas complejas que requieren razonamiento y planificación, usar un modelo más grande especializado en tareas de razonamiento. |
| Las llamadas a herramientas del agente de IA no funcionan bien | - Probar y validar la salida de la herramienta fuera del sistema del agente.<br>- Refinar los parámetros definidos, prompts y nombres de las herramientas. |
| El sistema multi-agente no funciona consistentemente | - Refinar prompts dados a cada agente para asegurar que sean específicos y distintos entre sí.<br>- Construir un sistema jerárquico usando un agente "enrutador" o controlador para determinar cuál agente es el correcto. |

Muchos de estos problemas pueden identificarse más eficazmente con observabilidad en marcha. Las trazas y métricas que discutimos anteriormente ayudan a precisar exactamente dónde ocurren los problemas en el flujo de trabajo del agente, haciendo la depuración y optimización mucho más eficientes.

## Gestión de Costos

Aquí hay algunas estrategias para gestionar los costos de desplegar agentes de IA en producción:

**Uso de modelos más pequeños:** Los Modelos de Lenguaje Pequeños (SLMs) pueden funcionar bien en ciertos casos de uso agenticos y reducirán significativamente los costos. Como se mencionó anteriormente, construir un sistema de evaluación para determinar y comparar el rendimiento frente a modelos más grandes es la mejor manera de entender qué tan bien funcionará un SLM en su caso de uso. Considere usar SLMs para tareas más simples como la clasificación de intenciones o la extracción de parámetros, mientras reserva los modelos más grandes para razonamientos complejos.

**Uso de un modelo enrutador:** Una estrategia similar es usar una diversidad de modelos y tamaños. Puede usar un LLM/SLM o una función sin servidor para enrutar solicitudes basadas en la complejidad hacia los modelos que mejor se ajusten. Esto también ayudará a reducir costos mientras se asegura el rendimiento en las tareas adecuadas. Por ejemplo, dirija consultas simples a modelos más pequeños y rápidos, y solo use modelos grandes y costosos para tareas complejas de razonamiento.

**Caché de respuestas:** Identificar solicitudes y tareas comunes y proporcionar las respuestas antes de que pasen por su sistema agentico es una buena manera de reducir el volumen de solicitudes similares. Incluso puede implementar un flujo para identificar qué tan similar es una solicitud a sus solicitudes almacenadas en caché usando modelos de IA más básicos. Esta estrategia puede reducir significativamente los costos para preguntas frecuentes o flujos de trabajo comunes.

## Veamos cómo funciona esto en la práctica

En el [cuaderno de ejemplo de esta sección](./code_samples/10-expense_claim-demo.ipynb), veremos ejemplos de cómo podemos usar herramientas de observabilidad para monitorear y evaluar nuestro agente.


### ¿Tiene más preguntas sobre agentes de IA en producción?

Únase al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para reunirse con otros aprendices, asistir a horas de oficina y obtener respuestas a sus preguntas sobre agentes de IA.

## Lección anterior

[Patrón de diseño metacognitivo](../09-metacognition/README.md)

## Próxima lección

[Protocolos agenticos](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->