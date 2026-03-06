# Agentes de IA en Producción: Observabilidad y Evaluación

[![AI Agents in Production](../../../translated_images/es/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

A medida que los agentes de IA pasan de prototipos experimentales a aplicaciones del mundo real, la capacidad para entender su comportamiento, monitorear su rendimiento y evaluar sistemáticamente sus resultados se vuelve importante.

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo/entenderás:
- Conceptos básicos de observabilidad y evaluación de agentes
- Técnicas para mejorar el rendimiento, costos y efectividad de los agentes
- Qué y cómo evaluar sistemáticamente tus agentes de IA
- Cómo controlar costos al desplegar agentes de IA en producción
- Cómo instrumentar agentes construidos con Microsoft Agent Framework

El objetivo es equiparte con el conocimiento para transformar tus agentes "caja negra" en sistemas transparentes, manejables y confiables.

_**Nota:** Es importante desplegar Agentes de IA que sean seguros y confiables. Consulta también la lección [Construyendo Agentes de IA Confiables](./06-building-trustworthy-agents/README.md)._

## Rastros y Spans

Las herramientas de observabilidad como [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) usualmente representan las ejecuciones de agentes como rastros y spans.

- **Rastro** representa una tarea completa del agente de principio a fin (como manejar una consulta de usuario).
- **Spans** son pasos individuales dentro del rastro (como llamar a un modelo de lenguaje o recuperar datos).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sin observabilidad, un agente de IA puede sentirse como una "caja negra": su estado interno y razonamiento son opacos, dificultando diagnosticar problemas u optimizar el rendimiento. Con observabilidad, los agentes se vuelven "cajas de cristal", ofreciendo transparencia vital para generar confianza y asegurar que operen como se espera.

## Por qué la Observabilidad Importa en Entornos de Producción

La transición de agentes de IA a entornos de producción introduce un nuevo conjunto de desafíos y requisitos. La observabilidad ya no es un "lujo", sino una capacidad crítica:

*   **Depuración y Análisis de Causa Raíz**: Cuando un agente falla o produce un resultado inesperado, las herramientas de observabilidad proporcionan los rastros necesarios para localizar la fuente del error. Esto es especialmente importante en agentes complejos que pueden involucrar múltiples llamadas a LLM, interacciones con herramientas y lógica condicional.
*   **Gestión de Latencia y Costos**: Los agentes de IA suelen depender de LLM y otras API externas que se facturan por token o por llamada. La observabilidad permite un seguimiento preciso de estas llamadas, ayudando a identificar operaciones excesivamente lentas o caras. Esto permite a los equipos optimizar prompts, seleccionar modelos más eficientes o rediseñar flujos de trabajo para manejar costos operativos y garantizar una buena experiencia de usuario.
*   **Confianza, Seguridad y Cumplimiento**: En muchas aplicaciones, es importante asegurar que los agentes se comporten de forma segura y ética. La observabilidad proporciona un registro de auditoría de las acciones y decisiones del agente. Esto se puede usar para detectar y mitigar problemas como inyección de prompts, generación de contenido dañino o manejo inadecuado de información personal identificable (PII). Por ejemplo, puedes revisar rastros para entender por qué un agente dio cierta respuesta o utilizó una herramienta específica.
*   **Ciclos de Mejora Continua**: Los datos de observabilidad son la base de un proceso de desarrollo iterativo. Al monitorear cómo se desempeñan los agentes en el mundo real, los equipos pueden identificar áreas de mejora, recopilar datos para ajustar modelos y validar el impacto de cambios. Esto crea un ciclo de retroalimentación donde las perspectivas de producción de la evaluación en línea informan la experimentación y refinamiento fuera de línea, conduciendo a un rendimiento progresivamente mejor.

## Métricas Clave para Rastrear

Para monitorear y entender el comportamiento del agente, se debe rastrear una variedad de métricas y señales. Aunque las métricas específicas pueden variar según el propósito del agente, algunas son universalmente importantes.

Aquí están algunas de las métricas más comunes que las herramientas de observabilidad monitorean:

**Latencia:** ¿Qué tan rápido responde el agente? Los tiempos de espera largos afectan negativamente la experiencia del usuario. Debes medir la latencia para tareas y pasos individuales rastreando ejecuciones del agente. Por ejemplo, un agente que tarda 20 segundos en realizar todas las llamadas a modelos podría acelerarse usando un modelo más rápido o ejecutando llamadas a modelos en paralelo.

**Costos:** ¿Cuál es el costo por ejecución del agente? Los agentes de IA dependen de llamadas a LLM que se facturan por token o a API externas. El uso frecuente de herramientas o múltiples prompts puede incrementar rápidamente los costos. Por ejemplo, si un agente llama a un LLM cinco veces para una mejora marginal en la calidad, debes evaluar si el costo está justificado o si puedes reducir la cantidad de llamadas o usar un modelo más barato. La monitorización en tiempo real también puede ayudar a identificar picos inesperados (por ejemplo, errores que causan bucles excesivos en la API).

**Errores en Solicitudes:** ¿Cuántas solicitudes falló el agente? Esto puede incluir errores de API o llamadas fallidas a herramientas. Para hacer tu agente más robusto frente a estos en producción, puedes entonces configurar mecanismos de respaldo o reintentos. Por ejemplo, si el proveedor LLM A está caído, cambias al proveedor LLM B como respaldo.

**Retroalimentación de Usuarios:** Implementar evaluaciones directas de usuarios proporciona información valiosa. Esto puede incluir calificaciones explícitas (👍pulgar arriba/👎abajo, ⭐1-5 estrellas) o comentarios textuales. Retroalimentación negativa consistente debe alertarte, ya que es señal de que el agente no funciona como se espera.

**Retroalimentación Implícita del Usuario:** Los comportamientos de los usuarios proporcionan retroalimentación indirecta incluso sin calificaciones explícitas. Esto puede incluir reformulación inmediata de preguntas, consultas repetidas o clic en un botón de reintento. Por ejemplo, si ves que los usuarios preguntan repetidamente lo mismo, es señal de que el agente no funciona como se espera.

**Precisión:** ¿Con qué frecuencia el agente produce salidas correctas o deseables? Las definiciones de precisión varían (por ejemplo, corrección de resolución de problemas, precisión en recuperación de información, satisfacción del usuario). El primer paso es definir qué significa éxito para tu agente. Puedes rastrear precisión mediante verificaciones automatizadas, puntuaciones de evaluación o etiquetas de tarea completada. Por ejemplo, marcar rastros como "exitoso" o "fallido".

**Métricas de Evaluación Automatizada:** También puedes configurar evaluaciones automáticas. Por ejemplo, puedes usar un LLM para puntuar la salida del agente, ej. si es útil, precisa o no. También existen varias bibliotecas de código abierto que te ayudan a puntuar diferentes aspectos del agente. Por ejemplo, [RAGAS](https://docs.ragas.io/) para agentes RAG o [LLM Guard](https://llm-guard.com/) para detectar lenguaje dañino o inyección de prompts.

En la práctica, una combinación de estas métricas brinda la mejor cobertura del estado de salud de un agente de IA. En el [notebook de ejemplo](./code_samples/10-expense_claim-demo.ipynb) de este capítulo, te mostraremos cómo se ven estas métricas en ejemplos reales, pero primero aprenderemos cómo luce un flujo típico de evaluación.

## Instrumenta tu Agente

Para recolectar datos de rastreo, necesitarás instrumentar tu código. El objetivo es instrumentar el código del agente para emitir rastros y métricas que puedan ser capturados, procesados y visualizados por una plataforma de observabilidad.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se ha establecido como un estándar industrial para la observabilidad de LLM. Proporciona un conjunto de APIs, SDKs y herramientas para generar, recopilar y exportar datos telemétricos.

Existen muchas bibliotecas de instrumentación que envuelven frameworks de agentes existentes y facilitan exportar spans OpenTelemetry a una herramienta de observabilidad. Microsoft Agent Framework se integra nativamente con OpenTelemetry. A continuación hay un ejemplo de instrumentación de un agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # La ejecución del agente se rastrea automáticamente
    pass
```

El [notebook de ejemplo](./code_samples/10-expense_claim-demo.ipynb) en este capítulo demostrará cómo instrumentar tu agente MAF.

**Creación Manual de Span:** Aunque las bibliotecas de instrumentación proporcionan una buena base, a menudo hay casos donde se necesita información más detallada o personalizada. Puedes crear spans manualmente para añadir lógica de aplicación personalizada. Más importante aún, puedes enriquecer spans creados automática o manualmente con atributos personalizados (también conocidos como etiquetas o metadatos). Estos atributos pueden incluir datos específicos del negocio, cálculos intermedios o cualquier contexto útil para depuración o análisis, como `user_id`, `session_id` o `model_version`.

Ejemplo de creación manual de rastros y spans con el [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluación de Agentes

La observabilidad nos da métricas, pero la evaluación es el proceso de analizar esos datos (y realizar pruebas) para determinar qué tan bien se está desempeñando un agente de IA y cómo puede mejorarse. En otras palabras, una vez que tienes esos rastros y métricas, ¿cómo los usas para juzgar al agente y tomar decisiones?

La evaluación regular es importante porque los agentes de IA a menudo son no deterministas y pueden evolucionar (a través de actualizaciones o cambios en el comportamiento del modelo): sin evaluación, no sabrías si tu "agente inteligente" realmente cumple bien su función o si ha regresado.

Existen dos categorías de evaluaciones para agentes de IA: **evaluación en línea** y **evaluación fuera de línea**. Ambas son valiosas y se complementan. Normalmente comenzamos con evaluación fuera de línea, ya que es el paso mínimo necesario antes de desplegar cualquier agente.

### Evaluación Fuera de Línea

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Esta implica evaluar el agente en un entorno controlado, típicamente usando conjuntos de datos de prueba, no consultas en vivo de usuarios. Usas datasets curados donde sabes cuál es la salida esperada o el comportamiento correcto, y luego ejecutas tu agente sobre estos.

Por ejemplo, si construiste un agente para resolver problemas matemáticos, podrías tener un [dataset de prueba](https://huggingface.co/datasets/gsm8k) de 100 problemas con respuestas conocidas. La evaluación fuera de línea a menudo se realiza durante el desarrollo (y puede ser parte de pipelines CI/CD) para verificar mejoras o proteger contra regresiones. La ventaja es que es **repetible y obtienes métricas claras de precisión porque tienes la verdad de base**. También puedes simular consultas de usuario y medir las respuestas del agente contra respuestas ideales o usar métricas automáticas como se describió arriba.

El reto clave con la evaluación fuera de línea es asegurar que tu dataset de prueba sea completo y se mantenga relevante: el agente podría desempeñarse bien en un conjunto fijo, pero encontrar consultas muy diferentes en producción. Por lo tanto, debes mantener los conjuntos de prueba actualizados con nuevos casos límite y ejemplos que reflejen escenarios reales. Una mezcla de casos pequeños de “prueba rápida” y conjuntos de evaluación más grandes es útil: pequeños para chequeos rápidos y grandes para métricas de rendimiento amplias.

### Evaluación en Línea

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Esto se refiere a evaluar el agente en un entorno real y en vivo, es decir, durante el uso real en producción. La evaluación en línea implica monitorear el desempeño del agente en interacciones reales con usuarios y analizar resultados continuamente.

Por ejemplo, podrías rastrear tasas de éxito, puntuaciones de satisfacción del usuario u otras métricas en tráfico en vivo. La ventaja de la evaluación en línea es que **captura cosas que podrías no anticipar en un laboratorio**: puedes observar deriva del modelo a lo largo del tiempo (si la efectividad del agente decae al cambiar los patrones de entrada) y detectar consultas o situaciones inesperadas que no estaban en tus datos de prueba. Proporciona una imagen verdadera de cómo se comporta el agente en el entorno real.

La evaluación en línea a menudo implica recopilar retroalimentación implícita y explícita de usuarios, como se discutió, y posiblemente ejecutar pruebas sombra o pruebas A/B (donde una nueva versión del agente corre paralelamente para comparar con la antigua). El reto es que puede ser difícil obtener etiquetas o puntuaciones confiables para interacciones en vivo: podrías depender de la retroalimentación del usuario o métricas posteriores (como si el usuario hizo clic en el resultado).

### Combinando Ambos

Las evaluaciones en línea y fuera de línea no se excluyen mutuamente; son altamente complementarias. Las ideas del monitoreo en línea (p. ej., nuevos tipos de consultas donde el agente se desempeña mal) pueden usarse para mejorar y ampliar datasets de prueba fuera de línea. A la inversa, agentes que funcionan bien en pruebas fuera de línea pueden ser desplegados con mayor confianza y monitoreados en línea.

De hecho, muchos equipos adoptan un ciclo:

_evaluar fuera de línea -> desplegar -> monitorear en línea -> recopilar nuevos casos de fallo -> añadir al dataset fuera de línea -> refinar agente -> repetir_.

## Problemas Comunes

Al desplegar agentes de IA en producción, puedes encontrar varios desafíos. Aquí algunos problemas comunes y sus posibles soluciones:

| **Problema**    | **Solución Potencial**   |
| ------------- | ------------------ |
| El Agente de IA no realiza tareas consistentemente | - Refinar el prompt dado al Agente de IA; ser claro en los objetivos.<br>- Identificar dónde dividir las tareas en subtareas y manejarlas por múltiples agentes puede ayudar. |
| El Agente de IA entra en bucles continuos  | - Asegurar que tienes términos y condiciones claros de terminación para que el Agente sepa cuándo parar el proceso.<br>- Para tareas complejas que requieren razonamiento y planificación, usar un modelo más grande especializado en tareas de razonamiento. |
| Las llamadas a herramientas del Agente de IA no funcionan bien   | - Probar y validar la salida de la herramienta fuera del sistema del agente.<br>- Refinar los parámetros definidos, prompts y nombrado de herramientas.  |
| Sistemas Multi-Agente no funcionan consistentemente | - Refinar los prompts dados a cada agente para asegurar que sean específicos y distintos entre ellos.<br>- Construir un sistema jerárquico usando un agente "enrutador" o controlador para determinar cuál agente es el correcto. |

Muchos de estos problemas pueden identificarse más efectivamente con observabilidad en su lugar. Los rastros y métricas que discutimos antes ayudan a localizar exactamente dónde en el flujo de trabajo del agente ocurren los problemas, haciendo la depuración y optimización mucho más eficientes.

## Gestión de Costos
Aquí hay algunas estrategias para gestionar los costos de desplegar agentes de IA en producción:

**Uso de modelos más pequeños:** Los modelos de lenguaje pequeños (SLMs) pueden funcionar bien en ciertos casos de uso agenticos y reducirán significativamente los costos. Como se mencionó anteriormente, construir un sistema de evaluación para determinar y comparar el rendimiento frente a modelos más grandes es la mejor manera de entender qué tan bien funcionará un SLM en su caso de uso. Considere usar SLMs para tareas más simples como clasificación de intenciones o extracción de parámetros, mientras reserva modelos más grandes para razonamientos complejos.

**Uso de un modelo enrutador:** Una estrategia similar es usar una diversidad de modelos y tamaños. Puede usar un LLM/SLM o función serverless para enrutar las solicitudes según la complejidad al modelo que mejor se adapte. Esto también ayudará a reducir costos al mismo tiempo que asegura el rendimiento en las tareas adecuadas. Por ejemplo, enrute consultas simples a modelos más pequeños y rápidos, y solo use modelos grandes y costosos para tareas de razonamiento complejo.

**Almacenamiento en caché de respuestas:** Identificar solicitudes y tareas comunes y proporcionar las respuestas antes de que pasen por su sistema agentico es una buena manera de reducir el volumen de solicitudes similares. Incluso puede implementar un flujo para identificar qué tan similar es una solicitud a sus solicitudes en caché usando modelos de IA más básicos. Esta estrategia puede reducir significativamente los costos para preguntas frecuentes o flujos de trabajo comunes.

## Veamos cómo funciona esto en la práctica

En el [notebook de ejemplo de esta sección](./code_samples/10-expense_claim-demo.ipynb), veremos ejemplos de cómo podemos usar herramientas de observabilidad para monitorear y evaluar nuestro agente.

### ¿Tienes más preguntas sobre agentes de IA en producción?

Únete al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para reunirte con otros aprendices, asistir a horas de oficina y obtener respuestas a tus preguntas sobre agentes de IA.

## Lección anterior

[Patrón de diseño de metacognición](../09-metacognition/README.md)

## Próxima lección

[Protocolos agenticos](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por un humano. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->