# Agentes de IA en Producción: Observabilidad y Evaluación

[![AI Agents in Production](../../../translated_images/es/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

A medida que los agentes de IA pasan de ser prototipos experimentales a aplicaciones del mundo real, la capacidad para comprender su comportamiento, monitorear su rendimiento y evaluar sistemáticamente sus resultados se vuelve importante.

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás/entenderás:
- Conceptos clave de observabilidad y evaluación de agentes
- Técnicas para mejorar el rendimiento, costos y efectividad de los agentes
- Qué y cómo evaluar sistemáticamente tus agentes de IA
- Cómo controlar los costos al desplegar agentes de IA en producción
- Cómo instrumentar agentes construidos con Microsoft Agent Framework

El objetivo es equiparte con el conocimiento para transformar tus agentes "caja negra" en sistemas transparentes, gestionables y confiables.

_**Nota:** Es importante desplegar agentes de IA que sean seguros y confiables. Consulta también la lección [Construyendo Agentes de IA Confiables](./06-building-trustworthy-agents/README.md)._

## Rastros y Spans

Las herramientas de observabilidad como [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) suelen representar las ejecuciones de agentes como rastros y spans.

- **Rastro (Trace)** representa una tarea completa del agente de inicio a fin (como manejar una consulta de usuario).
- **Spans** son pasos individuales dentro del rastro (como llamar a un modelo de lenguaje o recuperar datos).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sin observabilidad, un agente de IA puede parecer una "caja negra": su estado interno y razonamientos son opacos, lo que dificulta diagnosticar problemas u optimizar el rendimiento. Con la observabilidad, los agentes se convierten en "cajas de cristal", ofreciendo transparencia vital para generar confianza y asegurar que funcionen como se espera.

## Por qué la Observabilidad es Importante en Entornos de Producción

El paso de agentes de IA a entornos de producción introduce un nuevo conjunto de desafíos y requisitos. La observabilidad ya no es "algo deseable" sino una capacidad crítica:

*   **Depuración y análisis de causa raíz**: Cuando un agente falla o produce un resultado inesperado, las herramientas de observabilidad proporcionan los rastros necesarios para localizar el origen del error. Esto es especialmente importante en agentes complejos que pueden involucrar múltiples llamadas a LLM, interacciones con herramientas y lógica condicional.
*   **Gestión de latencia y costos**: Los agentes de IA a menudo dependen de LLM y otras APIs externas que se cobran por token o por llamada. La observabilidad permite un seguimiento preciso de estas llamadas, ayudando a identificar operaciones excesivamente lentas o costosas. Esto permite a los equipos optimizar prompts, seleccionar modelos más eficientes o rediseñar flujos de trabajo para controlar costos operativos y asegurar una buena experiencia al usuario.
*   **Confianza, seguridad y cumplimiento**: En muchas aplicaciones, es importante asegurar que los agentes se comporten de manera segura y ética. La observabilidad brinda una pista de auditoría de las acciones y decisiones del agente. Esto puede usarse para detectar y mitigar problemas como inyección de prompts, generación de contenido dañino o manejo inadecuado de información personal identificable (PII). Por ejemplo, puedes revisar rastros para entender por qué un agente proporcionó cierta respuesta o usó una herramienta específica.
*   **Ciclos continuos de mejora**: Los datos de observabilidad son la base de un proceso iterativo de desarrollo. Al monitorear cómo performan los agentes en el mundo real, los equipos pueden identificar áreas de mejora, recopilar datos para afinar modelos y validar el impacto de cambios. Esto crea un ciclo donde las percepciones de producción obtenidas con evaluaciones en línea informan experimentos y refinamientos fuera de línea, llevando a un rendimiento progresivamente mejor del agente.

## Métricas Clave para Rastrear

Para monitorear y entender el comportamiento del agente, se deben rastrear diversas métricas y señales. Aunque las métricas específicas pueden variar según el propósito del agente, algunas son universalmente importantes.

Aquí algunas de las métricas más comunes que monitorean las herramientas de observabilidad:

**Latencia:** ¿Con qué rapidez responde el agente? Los tiempos de espera largos impactan negativamente la experiencia del usuario. Debes medir la latencia de tareas y pasos individuales mediante rastreo de las ejecuciones del agente. Por ejemplo, un agente que tarda 20 segundos en todas las llamadas al modelo podría acelerarse usando un modelo más rápido o ejecutando llamadas en paralelo.

**Costos:** ¿Cuál es el costo por ejecución del agente? Los agentes de IA dependen de llamadas a LLM que se facturan por token o APIs externas. El uso frecuente de herramientas o múltiples prompts puede aumentar costos rápidamente. Por ejemplo, si un agente llama a un LLM cinco veces para una mejora marginal en calidad, debes evaluar si el costo está justificado o si podrías reducir llamadas o usar un modelo más económico. El monitoreo en tiempo real también ayuda a identificar picos inesperados (p. ej., bugs causando bucles excesivos con APIs).

**Errores en Solicitudes:** ¿Cuántas solicitudes falló el agente? Esto puede incluir errores de API o llamadas a herramientas fallidas. Para hacer tu agente más robusto ante estos problemas en producción, puedes configurar fallbacks o reintentos. Por ejemplo, si el proveedor LLM A está caído, puedes cambiar al proveedor LLM B como respaldo.

**Retroalimentación del Usuario:** Implementar evaluaciones directas de usuarios proporciona valiosos insights. Esto puede incluir valoraciones explícitas (👍 pulgares arriba/👎 abajo,⭐1-5 estrellas) o comentarios textuales. Un feedback negativo consistente debería alertarte ya que es una señal de que el agente no está funcionando como se espera.

**Retroalimentación Implícita del Usuario:** Los comportamientos de usuario proporcionan retroalimentación indirecta sin valoraciones explícitas. Esto puede incluir reformulación inmediata de preguntas, consultas repetidas o pulsar un botón de reintento. Por ejemplo, si ves que los usuarios preguntan repetidamente lo mismo, es una señal de que el agente no está funcionando como se espera.

**Precisión:** ¿Con qué frecuencia produce el agente resultados correctos o deseables? Las definiciones de precisión varían (p. ej., corrección en resolución de problemas, precisión en recuperación de información, satisfacción del usuario). El primer paso es definir qué significa éxito para tu agente. Puedes rastrear precisión mediante verificaciones automáticas, puntuaciones de evaluación o etiquetas de finalización de tarea. Por ejemplo, marcar rastros como "exitosos" o "fallidos".

**Métricas de Evaluación Automáticas:** También puedes configurar evaluaciones automáticas. Por ejemplo, usar un LLM para puntuar la salida del agente: si es útil, precisa o no. Hay varias bibliotecas open source que te ayudan a puntuar diferentes aspectos del agente. Por ejemplo, [RAGAS](https://docs.ragas.io/) para agentes RAG o [LLM Guard](https://llm-guard.com/) para detectar lenguaje dañino o inyección de prompts.

En la práctica, una combinación de estas métricas ofrece la mejor cobertura del estado de salud de un agente de IA. En el [notebook de ejemplo](./code_samples/10-expense_claim-demo.ipynb) de este capítulo, te mostraremos cómo se ven estas métricas en ejemplos reales, pero primero aprenderemos cómo es un flujo típico de evaluación.

## Instrumenta tu Agente

Para recopilar datos de rastreo, necesitarás instrumentar tu código. El objetivo es instrumentar el código del agente para emitir rastros y métricas que puedan ser capturados, procesados y visualizados por una plataforma de observabilidad.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se ha convertido en un estándar de la industria para la observabilidad de LLM. Proporciona un conjunto de APIs, SDKs y herramientas para generar, recopilar y exportar datos de telemetría.

Existen muchas bibliotecas de instrumentación que envuelven frameworks de agentes existentes y facilitan exportar spans de OpenTelemetry a una herramienta de observabilidad. Microsoft Agent Framework se integra con OpenTelemetry de forma nativa. A continuación, un ejemplo para instrumentar un agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # La ejecución del agente se rastrea automáticamente
    pass
```

El [notebook de ejemplo](./code_samples/10-expense_claim-demo.ipynb) de este capítulo demostrará cómo instrumentar tu agente MAF.

**Creación Manual de Spans:** Aunque las bibliotecas de instrumentación brindan una buena base, a menudo hay casos donde se necesita información más detallada o personalizada. Puedes crear spans manualmente para añadir lógica de aplicación personalizada. Lo más importante, pueden enriquecer spans creados automática o manualmente con atributos personalizados (también conocidos como etiquetas o metadata). Estos atributos pueden incluir datos específicos del negocio, cálculos intermedios o cualquier contexto que pueda ser útil para depuración o análisis, como `user_id`, `session_id` o `model_version`.

Ejemplo de creación manual de rastros y spans con el [SDK de Langfuse para Python](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluación del Agente

La observabilidad nos da métricas, pero la evaluación es el proceso de analizar esos datos (y realizar pruebas) para determinar qué tan bien está funcionando un agente de IA y cómo puede mejorarse. En otras palabras, una vez que tienes esos rastros y métricas, ¿cómo los usas para juzgar el agente y tomar decisiones?

La evaluación regular es importante porque los agentes de IA suelen ser no determinísticos y pueden evolucionar (a través de actualizaciones o cambios en el comportamiento del modelo); sin evaluación, no sabrías si tu "agente inteligente" realmente está haciendo bien su trabajo o si ha empeorado.

Existen dos categorías de evaluaciones para agentes de IA: **evaluación en línea** y **evaluación fuera de línea**. Ambas son valiosas y se complementan. Usualmente se comienza con la evaluación fuera de línea, ya que es el paso mínimo necesario antes de desplegar cualquier agente.

### Evaluación Fuera de Línea

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Esto implica evaluar el agente en un entorno controlado, típicamente usando conjuntos de datos de prueba, no consultas reales de usuarios. Usas datasets curados donde sabes cuál es la salida esperada o comportamiento correcto, y luego ejecutas tu agente con esos datos.

Por ejemplo, si construiste un agente para resolver problemas matemáticos, podrías tener un [dataset de prueba](https://huggingface.co/datasets/gsm8k) de 100 problemas con respuestas conocidas. La evaluación fuera de línea suele hacerse durante el desarrollo (y puede ser parte de pipelines CI/CD) para verificar mejoras o evitar regresiones. El beneficio es que es **repetible y puedes obtener métricas claras de precisión porque tienes la verdad de referencia**. También podrías simular consultas de usuario y medir las respuestas del agente contra respuestas ideales o usar métricas automáticas como se describió arriba.

El principal desafío de la evaluación fuera de línea es asegurarte que tu dataset de prueba sea completo y se mantenga relevante: el agente podría funcionar bien en un conjunto fijo pero enfrentar consultas muy diferentes en producción. Por eso debes mantener los conjuntos de prueba actualizados con nuevos casos frontera y ejemplos que reflejen escenarios reales. Una mezcla de pequeños "smoke tests" y conjuntos más grandes es útil: conjuntos pequeños para pruebas rápidas y grandes para métricas de rendimiento más amplias.

### Evaluación en Línea

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Esto se refiere a evaluar al agente en un entorno real y en vivo, es decir, durante el uso real en producción. La evaluación en línea implica monitorear el rendimiento del agente en interacciones reales con usuarios y analizar los resultados de forma continua.

Por ejemplo, podrías rastrear tasas de éxito, puntajes de satisfacción del usuario u otras métricas en tráfico en vivo. La ventaja de la evaluación en línea es que **captura aspectos que podrías no anticipar en un laboratorio**: puedes observar la deriva del modelo a lo largo del tiempo (si la efectividad del agente degrada con cambios en patrones de entrada) y detectar consultas o situaciones inesperadas que no estaban en tus datos de prueba. Proporciona una imagen verdadera de cómo se comporta el agente en el entorno real.

La evaluación en línea a menudo implica recolectar retroalimentación implícita y explícita de usuarios, como se discutió, y posiblemente ejecutar pruebas sombra o pruebas A/B (donde una nueva versión del agente corre en paralelo para comparar con la antigua). El reto es que puede ser difícil obtener etiquetas o puntajes confiables para interacciones en vivo; podrías depender de la retroalimentación del usuario o métricas posteriores (como si el usuario hizo clic en el resultado).

### Combinar Ambas

Las evaluaciones en línea y fuera de línea no son mutuamente excluyentes, sino altamente complementarias. Los insights del monitoreo en línea (p. ej., nuevos tipos de consultas donde el agente falla) pueden usarse para ampliar y mejorar los datasets de prueba fuera de línea. A la inversa, agentes que funcionan bien en pruebas fuera de línea pueden desplegarse luego con mayor confianza y ser monitoreados en línea.

De hecho, muchos equipos adoptan un ciclo:

_evaluar fuera de línea -> desplegar -> monitorear en línea -> recopilar nuevos casos fallidos -> agregar al conjunto fuera de línea -> afinar agente -> repetir_.

## Problemas Comunes

Al desplegar agentes de IA en producción, puedes enfrentar diversos desafíos. Aquí algunos problemas comunes y sus soluciones potenciales:

| **Problema**    | **Solución Potencial**   |
| ------------- | ------------------ |
| El agente de IA no realiza tareas consistentemente | - Refinar el prompt dado al agente; ser claro en los objetivos.<br>- Identificar dónde dividir tareas en subtareas manejadas por múltiples agentes. |
| El agente de IA se queda en bucles continuos | - Asegurar términos y condiciones claras de terminación para que el agente sepa cuándo detener el proceso.<br>- Para tareas complejas que requieren razonamiento y planificación, usar un modelo más grande especializado en razonamiento. |
| Llamadas a herramientas del agente no funcionan bien | - Probar y validar la salida de la herramienta fuera del sistema del agente.<br>- Refinar los parámetros definidos, prompts y nombres de las herramientas. |
| Sistema multiagente que no funciona consistentemente | - Refinar los prompts dados a cada agente para que sean específicos y distintos entre sí.<br>- Construir un sistema jerárquico usando un agente "enrutador" o controlador para determinar cuál agente es el correcto. |

Muchos de estos problemas pueden identificarse más eficazmente con observabilidad activa. Los rastros y métricas que discutimos antes ayudan a localizar exactamente dónde ocurren los problemas en el flujo del agente, haciendo la depuración y optimización mucho más eficiente.

## Gestión de Costos
Aquí hay algunas estrategias para gestionar los costos de desplegar agentes de IA en producción:

**Usar Modelos Más Pequeños:** Los Modelos de Lenguaje Pequeños (SLMs) pueden funcionar bien en ciertos casos de uso agenticos y reducirán significativamente los costos. Como se mencionó anteriormente, construir un sistema de evaluación para determinar y comparar el rendimiento frente a modelos más grandes es la mejor manera de entender qué tan bien funcionará un SLM en tu caso de uso. Considera usar SLMs para tareas más simples como clasificación de intenciones o extracción de parámetros, mientras reservas modelos más grandes para razonamientos complejos.

**Usar un Modelo Router:** Una estrategia similar es usar una diversidad de modelos y tamaños. Puedes usar un LLM/SLM o una función serverless para enrutar las solicitudes según la complejidad a los modelos más adecuados. Esto también ayudará a reducir costos mientras se asegura el rendimiento en las tareas correctas. Por ejemplo, enruta consultas simples a modelos más pequeños y rápidos, y usa solo modelos grandes y costosos para tareas de razonamiento complejo.

**Cachear Respuestas:** Identificar solicitudes y tareas comunes y proporcionar las respuestas antes de que pasen por tu sistema agentico es una buena manera de reducir el volumen de solicitudes similares. Incluso puedes implementar un flujo para identificar cuán similar es una solicitud a las respuestas cacheadas usando modelos de IA más básicos. Esta estrategia puede reducir significativamente los costos para preguntas frecuentes o flujos de trabajo comunes.

## Veamos cómo funciona esto en la práctica

En el [notebook de ejemplo de esta sección](./code_samples/10-expense_claim-demo.ipynb), veremos ejemplos de cómo podemos usar herramientas de observabilidad para monitorear y evaluar nuestro agente.

### ¿Tienes Más Preguntas sobre Agentes de IA en Producción?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros estudiantes, asistir a horas de oficina y obtener respuestas a tus preguntas sobre Agentes de IA.

## Lección Anterior

[Patrón de Diseño de Metacognición](../09-metacognition/README.md)

## Lección Siguiente

[Protocolos Agenticos](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->