# Agentes de IA en Producción: Observabilidad y Evaluación

[![Agentes de IA en Producción](../../../translated_images/es/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

A medida que los agentes de IA pasan de prototipos experimentales a aplicaciones del mundo real, la capacidad para entender su comportamiento, monitorear su desempeño y evaluar sistemáticamente sus resultados se vuelve importante.

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo / entenderás:
- Conceptos básicos de observabilidad y evaluación de agentes
- Técnicas para mejorar el rendimiento, los costos y la efectividad de los agentes
- Qué y cómo evaluar sistemáticamente tus agentes de IA
- Cómo controlar los costos al implementar agentes de IA en producción
- Cómo instrumentar agentes construidos con Microsoft Agent Framework

El objetivo es equiparte con el conocimiento para transformar tus agentes "caja negra" en sistemas transparentes, gestionables y confiables.

_**Nota:** Es importante desplegar agentes de IA que sean seguros y confiables. También consulta la lección [Construyendo Agentes de IA Confiables](../06-building-trustworthy-agents/README.md)._

## Rastros y Segmentos

Las herramientas de observabilidad como [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) usualmente representan ejecuciones de agentes como rastros y segmentos.

- **Rastro** representa una tarea completa del agente de inicio a fin (como atender una consulta de usuario).
- **Segmentos** son pasos individuales dentro del rastro (como llamar a un modelo de lenguaje o recuperar datos).

![Árbol de rastros en Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sin observabilidad, un agente de IA puede sentirse como una "caja negra": su estado interno y razonamiento son opacos, dificultando diagnosticar problemas u optimizar el rendimiento. Con observabilidad, los agentes se vuelven "cajas de cristal", ofreciendo transparencia vital para generar confianza y asegurar que operen como se espera.

## Por Qué la Observabilidad es Importante en Entornos de Producción

Pasar los agentes de IA a entornos de producción introduce nuevos desafíos y requisitos. La observabilidad ya no es un "bono", sino una capacidad crítica:

*   **Depuración y Análisis de Causas Raíz**: Cuando un agente falla o produce un resultado inesperado, las herramientas de observabilidad proporcionan los rastros necesarios para localizar la fuente del error. Esto es especialmente importante en agentes complejos que pueden involucrar múltiples llamadas a LLM, interacciones con herramientas y lógica condicional.
*   **Gestión de Latencia y Costos**: Los agentes de IA a menudo dependen de LLM y otras API externas que cobran por token o por llamada. La observabilidad permite un seguimiento preciso de estas llamadas, ayudando a identificar operaciones que son excesivamente lentas o costosas. Esto permite optimizar los prompts, seleccionar modelos más eficientes o rediseñar flujos de trabajo para gestionar costos operativos y asegurar una buena experiencia de usuario.
*   **Confianza, Seguridad y Cumplimiento**: En muchas aplicaciones, es importante asegurar que los agentes se comporten de manera segura y ética. La observabilidad brinda una pista de auditoría de las acciones y decisiones del agente. Esto puede usarse para detectar y mitigar problemas como inyección de prompts, generación de contenido dañino o manejo incorrecto de información personal identificable (PII). Por ejemplo, puedes revisar rastros para entender por qué un agente proporcionó cierta respuesta o usó una herramienta específica.
*   **Ciclos de Mejora Continua**: Los datos de observabilidad son la base de un proceso de desarrollo iterativo. Al monitorear cómo se desempeñan los agentes en el mundo real, los equipos pueden identificar áreas para mejorar, recopilar datos para ajustar modelos y validar el impacto de cambios. Esto crea un ciclo de retroalimentación donde los insights de producción de la evaluación en línea informan la experimentación y refinamiento fuera de línea, llevando a un mejor rendimiento progresivo del agente.

## Métricas Clave para Monitorear

Para monitorear y entender el comportamiento del agente, se debe rastrear una variedad de métricas y señales. Aunque las métricas específicas pueden variar según el propósito del agente, algunas son universalmente importantes.

Aquí están algunas de las métricas más comunes que monitorean las herramientas de observabilidad:

**Latencia:** ¿Qué tan rápido responde el agente? Los tiempos de espera largos impactan negativamente la experiencia del usuario. Debes medir la latencia para tareas y pasos individuales rastreando ejecuciones del agente. Por ejemplo, un agente que tarda 20 segundos en todas las llamadas de modelo podría acelerarse utilizando un modelo más rápido o ejecutando llamadas de modelo en paralelo.

**Costos:** ¿Cuál es el gasto por ejecución del agente? Los agentes de IA dependen de llamadas a LLM facturadas por token o APIs externas. El uso frecuente de herramientas o múltiples prompts puede aumentar rápidamente los costos. Por ejemplo, si un agente llama a un LLM cinco veces para una mejora marginal de calidad, debes evaluar si el costo se justifica o si podrías reducir el número de llamadas o usar un modelo más económico. El monitoreo en tiempo real también ayuda a identificar picos inesperados (por ejemplo, bugs que causan bucles excesivos en la API).

**Errores en las Solicitudes:** ¿Cuántas solicitudes falló el agente? Esto puede incluir errores de API o llamadas a herramientas fallidas. Para hacer tu agente más robusto contra estos en producción, puedes configurar mecanismos de respaldo o reintentos. Por ejemplo, si el proveedor LLM A está caído, cambias al proveedor LLM B como respaldo.

**Retroalimentación del Usuario:** Implementar evaluaciones directas de usuarios proporciona valiosos insights. Esto puede incluir valoraciones explícitas (👍positivo/👎negativo, ⭐1-5 estrellas) o comentarios textuales. Retroalimentación negativa constante debería alertarte, ya que es señal de que el agente no está funcionando como se espera.

**Retroalimentación Implícita del Usuario:** Los comportamientos de los usuarios dan retroalimentación indirecta incluso sin valoraciones explícitas. Esto puede incluir reformulación inmediata de preguntas, consultas repetidas o clicar un botón de reintento. Por ejemplo, si ves que los usuarios preguntan repetidamente la misma cuestión, es señal de que el agente no está funcionando como se espera.

**Precisión:** ¿Con qué frecuencia el agente produce resultados correctos o deseables? Las definiciones de precisión varían (por ejemplo, corrección en resolución de problemas, precisión en recuperación de información, satisfacción del usuario). El primer paso es definir cómo se ve el éxito para tu agente. Puedes medir precisión con chequeos automatizados, puntajes de evaluación o etiquetas de tarea completada. Por ejemplo, marcar rastros como "exitoso" o "fallido".

**Métricas de Evaluación Automatizadas:** También puedes configurar evaluaciones automáticas. Por ejemplo, usar un LLM para puntuar la salida del agente, si es útil, precisa o no. También existen diversas bibliotecas de código abierto que ayudan a puntuar diferentes aspectos del agente, por ejemplo, [RAGAS](https://docs.ragas.io/) para agentes RAG o [LLM Guard](https://llm-guard.com/) para detectar lenguaje dañino o inyección de prompts.

En la práctica, una combinación de estas métricas brinda la mejor cobertura del estado de salud de un agente de IA. En el [notebook de ejemplo](./code_samples/10-expense_claim-demo.ipynb) de este capítulo, te mostraremos cómo se ven estas métricas en ejemplos reales, pero primero aprenderemos cómo es el flujo típico de evaluación.

## Instrumenta tu Agente

Para recopilar datos de rastreo, necesitarás instrumentar tu código. El objetivo es instrumentar el código del agente para emitir rastros y métricas que puedan ser capturados, procesados y visualizados por una plataforma de observabilidad.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se ha convertido en un estándar de la industria para la observabilidad en LLM. Proporciona un conjunto de APIs, SDKs y herramientas para generar, recopilar y exportar datos de telemetría.

Hay muchas bibliotecas de instrumentación que envuelven frameworks existentes de agentes y facilitan exportar segmentos de OpenTelemetry a una herramienta de observabilidad. Microsoft Agent Framework integra OpenTelemetry de forma nativa. Abajo hay un ejemplo de cómo instrumentar un agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # La ejecución del agente se rastrea automáticamente
    pass
```

El [notebook de ejemplo](./code_samples/10-expense_claim-demo.ipynb) en este capítulo demostrará cómo instrumentar tu agente MAF.

**Creación Manual de Segmentos:** Aunque las bibliotecas de instrumentación proveen una buena base, a menudo se necesitan casos donde se requiere información más detallada o personalizada. Puedes crear segmentos manualmente para añadir lógica de aplicación personalizada. Más importante aún, pueden enriquecer segmentos creados automáticamente o manualmente con atributos personalizados (también conocidos como etiquetas o metadatos). Estos atributos pueden incluir datos específicos del negocio, cálculos intermedios o cualquier contexto útil para depuración o análisis, como `user_id`, `session_id` o `model_version`.

Ejemplo de creación manual de rastros y segmentos con el [SDK de Langfuse para Python](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluación del Agente

La observabilidad nos da métricas, pero la evaluación es el proceso de analizar esos datos (y realizar pruebas) para determinar qué tan bien se está desempeñando un agente de IA y cómo puede mejorarse. En otras palabras, una vez que tienes esos rastros y métricas, ¿cómo los usas para juzgar al agente y tomar decisiones?

La evaluación regular es importante porque los agentes de IA a menudo no son determinísticos y pueden evolucionar (a través de actualizaciones o cambios en el comportamiento del modelo) – sin evaluación no sabrías si tu “agente inteligente” realmente está haciendo bien su trabajo o si ha retrocedido.

Hay dos categorías de evaluaciones para agentes de IA: **evaluación en línea (online)** y **evaluación fuera de línea (offline)**. Ambas son valiosas y se complementan. Usualmente comenzamos con la evaluación fuera de línea, ya que es el paso mínimo necesario antes de desplegar cualquier agente.

### Evaluación fuera de línea

![Items del conjunto de datos en Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Esto implica evaluar al agente en un entorno controlado, típicamente usando conjuntos de datos de prueba, no consultas de usuarios en vivo. Usas conjuntos de datos curados donde sabes cuál es el resultado esperado o el comportamiento correcto, y luego ejecutas tu agente sobre ellos.

Por ejemplo, si construiste un agente para problemas matemáticos de palabras, podrías tener un [conjunto de datos de prueba](https://huggingface.co/datasets/gsm8k) de 100 problemas con respuestas conocidas. La evaluación fuera de línea usualmente se realiza durante el desarrollo (y puede ser parte de pipelines CI/CD) para verificar mejoras o prevenir regresiones. La ventaja es que es **repetible y puedes obtener métricas claras de precisión porque tienes la verdad en tierra**. También podrías simular consultas de usuarios y medir las respuestas del agente contra respuestas ideales o usar métricas automatizadas como se describió antes.

El reto clave con la evaluación fuera de línea es asegurar que tu conjunto de datos de prueba sea completo y se mantenga relevante: el agente podría funcionar bien en un conjunto de prueba fijo pero enfrentarse a consultas muy diferentes en producción. Por lo tanto, debes mantener los conjuntos de prueba actualizados con nuevos casos límite y ejemplos que reflejen escenarios reales. Una combinación de conjuntos pequeños de “prueba rápida” y conjuntos de evaluación más grandes es útil: sets pequeños para revisiones rápidas y grandes para métricas más amplias de rendimiento.

### Evaluación en línea

![Resumen de métricas de observabilidad](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Esto se refiere a evaluar al agente en un entorno real y en vivo, es decir, durante el uso real en producción. La evaluación en línea implica monitorizar el desempeño del agente en interacciones reales con usuarios y analizar resultados de forma continua.

Por ejemplo, podrías hacer seguimiento de tasas de éxito, puntajes de satisfacción del usuario u otras métricas sobre tráfico en vivo. La ventaja de la evaluación en línea es que **captura cosas que quizá no anticipas en un entorno de laboratorio** – puedes observar la deriva del modelo con el tiempo (si la efectividad del agente se degrada a medida que cambian los patrones de entrada) y detectar consultas o situaciones inesperadas que no estaban en tus datos de prueba. Proporciona una imagen real de cómo se comporta el agente en condiciones reales.

La evaluación en línea a menudo implica recolectar retroalimentación implícita y explícita del usuario, como se discutió, y posiblemente ejecutar pruebas shadow o tests A/B (donde una nueva versión del agente corre en paralelo para comparar con la antigua). El reto es que puede ser complicado obtener etiquetas o puntajes fiables para interacciones en vivo – podrías depender de la retroalimentación del usuario o de métricas downstream (por ejemplo, si el usuario hizo clic en el resultado).

### Combinando ambos

Las evaluaciones en línea y fuera de línea no son mutuamente exclusivas; son altamente complementarias. Los insights del monitoreo en línea (por ejemplo, nuevos tipos de consultas donde el agente tiene bajo rendimiento) pueden usarse para ampliar y mejorar conjuntos de prueba fuera de línea. A la inversa, agentes que funcionan bien en pruebas fuera de línea pueden desplegarse y monitorearse con más confianza en línea.

De hecho, muchos equipos adoptan un ciclo:

_evaluar fuera de línea -> desplegar -> monitorear en línea -> recopilar nuevos casos de fallos -> agregar al conjunto de datos fuera de línea -> refinar agente -> repetir_.

## Problemas Comunes

Al desplegar agentes de IA en producción, puedes encontrar varios desafíos. Aquí algunos problemas comunes y sus posibles soluciones:

| **Problema**    | **Solución Potencial**   |
| ------------- | ------------------ |
| El Agente de IA no realiza las tareas consistentemente | - Refinar el prompt dado al agente de IA; ser claro en los objetivos.<br>- Identificar cuándo dividir las tareas en subtareas y manejarlas por múltiples agentes puede ayudar. |
| El Agente de IA entra en bucles continuos  | - Asegurarse de contar con términos y condiciones de terminación claros para que el agente sepa cuándo detener el proceso.<br>- Para tareas complejas que requieren razonamiento y planificación, usar un modelo más grande especializado en tareas de razonamiento. |
| Las llamadas a herramientas del agente no funcionan bien   | - Probar y validar la salida de la herramienta fuera del sistema del agente.<br>- Refinar los parámetros definidos, prompts y nombres de las herramientas.  |
| Sistema Multi-Agente no funciona consistentemente | - Refinar los prompts dados a cada agente para asegurar que sean específicos y distintos entre sí.<br>- Construir un sistema jerárquico usando un agente "enrutador" o controlador para determinar cuál agente es el correcto. |

Muchos de estos problemas pueden identificarse más efectivamente con la observabilidad activada. Los rastros y métricas que discutimos antes ayudan a localizar exactamente dónde en el flujo de trabajo del agente ocurren los problemas, haciendo la depuración y optimización mucho más eficiente.

## Gestión de Costos


Aquí hay algunas estrategias para gestionar los costos de desplegar agentes de IA en producción:

**Uso de modelos más pequeños:** Los Modelos de Lenguaje Pequeños (SLMs) pueden funcionar bien en ciertos casos de uso agente y reducirán los costos significativamente. Como se mencionó anteriormente, construir un sistema de evaluación para determinar y comparar el rendimiento frente a modelos más grandes es la mejor manera de entender qué tan bien funcionará un SLM en tu caso de uso. Considera usar SLMs para tareas más simples como clasificación de intenciones o extracción de parámetros, mientras reservas los modelos más grandes para razonamientos complejos.

**Uso de un modelo enrutador:** Una estrategia similar es usar una diversidad de modelos y tamaños. Puedes usar un LLM/SLM o una función serverless para enrutar las solicitudes según la complejidad al modelo más adecuado. Esto también ayudará a reducir costos mientras aseguras rendimiento en las tareas correctas. Por ejemplo, enruta consultas simples a modelos más pequeños y rápidos, y solo usa modelos grandes y costosos para tareas de razonamiento complejas.

**Cacheo de respuestas:** Identificar solicitudes y tareas comunes y proporcionar las respuestas antes de que pasen por tu sistema agente es una buena forma de reducir el volumen de solicitudes similares. Incluso puedes implementar un flujo para identificar qué tan similar es una solicitud a tus solicitudes almacenadas en caché usando modelos de IA más básicos. Esta estrategia puede reducir significativamente los costos para preguntas frecuentes o flujos de trabajo comunes.

## Veamos cómo funciona esto en la práctica

En el [cuaderno de ejemplo de esta sección](./code_samples/10-expense_claim-demo.ipynb), veremos ejemplos de cómo podemos usar herramientas de observabilidad para monitorear y evaluar a nuestro agente.


### ¿Tienes más preguntas sobre agentes de IA en producción?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros aprendices, asistir a horas de oficina y resolver tus preguntas sobre agentes de IA.

## Lección anterior

[Patrón de diseño de metacognición](../09-metacognition/README.md)

## Próxima lección

[Protocolos agenticos](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->