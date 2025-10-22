<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-30T13:08:17+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "es"
}
-->
[![Introducción a los Agentes de IA](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.es.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Introducción a los Agentes de IA y Casos de Uso

¡Bienvenido al curso "Agentes de IA para Principiantes"! Este curso proporciona conocimientos fundamentales y ejemplos prácticos para construir Agentes de IA.

Únete al [Discord de Azure AI Foundry](https://aka.ms/ai-agents/discord) para conocer a otros estudiantes y constructores de Agentes de IA, y para hacer cualquier pregunta que tengas sobre este curso.

Para comenzar este curso, primero obtendremos una mejor comprensión de qué son los Agentes de IA y cómo podemos utilizarlos en las aplicaciones y flujos de trabajo que desarrollamos.

## Introducción

Esta lección cubre:

- ¿Qué son los Agentes de IA y cuáles son los diferentes tipos de agentes?
- ¿Cuáles son los casos de uso ideales para los Agentes de IA y cómo pueden ayudarnos?
- ¿Cuáles son algunos de los bloques básicos al diseñar Soluciones Agénticas?

## Objetivos de Aprendizaje
Al completar esta lección, deberías ser capaz de:

- Comprender los conceptos de los Agentes de IA y cómo se diferencian de otras soluciones de IA.
- Aplicar los Agentes de IA de manera eficiente.
- Diseñar soluciones agénticas de forma productiva tanto para usuarios como para clientes.

## Definiendo los Agentes de IA y Tipos de Agentes de IA

### ¿Qué son los Agentes de IA?

Los Agentes de IA son **sistemas** que permiten que los **Modelos de Lenguaje Extensos (LLMs)** **realicen acciones** al extender sus capacidades, dándoles acceso a **herramientas** y **conocimiento**.

Desglosemos esta definición en partes más pequeñas:

- **Sistema** - Es importante pensar en los agentes no como un único componente, sino como un sistema compuesto por varios componentes. En su nivel más básico, los componentes de un Agente de IA son:
  - **Entorno** - El espacio definido donde opera el Agente de IA. Por ejemplo, si tuviéramos un agente de reservas de viajes, el entorno podría ser el sistema de reservas que el agente utiliza para completar tareas.
  - **Sensores** - Los entornos tienen información y proporcionan retroalimentación. Los Agentes de IA usan sensores para recopilar e interpretar esta información sobre el estado actual del entorno. En el ejemplo del agente de reservas, el sistema de reservas puede proporcionar información como la disponibilidad de hoteles o los precios de vuelos.
  - **Actuadores** - Una vez que el Agente de IA recibe el estado actual del entorno, determina qué acción realizar para cambiar el entorno. En el caso del agente de reservas, podría ser reservar una habitación disponible para el usuario.

![¿Qué son los Agentes de IA?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.es.png)

**Modelos de Lenguaje Extensos** - El concepto de agentes existía antes de la creación de los LLMs. La ventaja de construir Agentes de IA con LLMs es su capacidad para interpretar el lenguaje humano y los datos. Esta habilidad permite a los LLMs interpretar información del entorno y definir un plan para modificarlo.

**Realizar Acciones** - Fuera de los sistemas de Agentes de IA, los LLMs están limitados a generar contenido o información basada en un prompt del usuario. Dentro de los sistemas de Agentes de IA, los LLMs pueden realizar tareas interpretando la solicitud del usuario y utilizando herramientas disponibles en su entorno.

**Acceso a Herramientas** - Las herramientas a las que el LLM tiene acceso están definidas por 1) el entorno en el que opera y 2) el desarrollador del Agente de IA. En nuestro ejemplo del agente de viajes, las herramientas del agente están limitadas por las operaciones disponibles en el sistema de reservas, y/o el desarrollador puede restringir el acceso del agente a vuelos.

**Memoria + Conocimiento** - La memoria puede ser a corto plazo en el contexto de la conversación entre el usuario y el agente. A largo plazo, fuera de la información proporcionada por el entorno, los Agentes de IA también pueden recuperar conocimiento de otros sistemas, servicios, herramientas e incluso otros agentes. En el ejemplo del agente de viajes, este conocimiento podría ser la información sobre las preferencias de viaje del usuario almacenada en una base de datos de clientes.

### Los diferentes tipos de agentes

Ahora que tenemos una definición general de los Agentes de IA, veamos algunos tipos específicos de agentes y cómo se aplicarían a un agente de reservas de viajes.

| **Tipo de Agente**            | **Descripción**                                                                                                                       | **Ejemplo**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agentes de Reflexión Simple** | Realizan acciones inmediatas basadas en reglas predefinidas.                                                                          | El agente de viajes interpreta el contexto de un correo electrónico y reenvía quejas de viaje al servicio al cliente.                                                                                                         |
| **Agentes de Reflexión Basados en Modelos** | Realizan acciones basadas en un modelo del mundo y los cambios en ese modelo.                                                     | El agente de viajes prioriza rutas con cambios significativos en los precios basándose en el acceso a datos históricos de precios.                                                                                           |
| **Agentes Basados en Objetivos** | Crean planes para alcanzar objetivos específicos interpretando el objetivo y determinando las acciones necesarias para lograrlo.       | El agente de viajes organiza un viaje determinando los arreglos necesarios (auto, transporte público, vuelos) desde la ubicación actual hasta el destino.                                                                    |
| **Agentes Basados en Utilidad** | Consideran preferencias y evalúan compromisos numéricamente para determinar cómo alcanzar los objetivos.                              | El agente de viajes maximiza la utilidad al equilibrar conveniencia y costo al reservar un viaje.                                                                                                                             |
| **Agentes de Aprendizaje**     | Mejoran con el tiempo respondiendo a retroalimentación y ajustando sus acciones en consecuencia.                                       | El agente de viajes mejora utilizando comentarios de encuestas post-viaje para realizar ajustes en futuras reservas.                                                                                                          |
| **Agentes Jerárquicos**        | Incluyen múltiples agentes en un sistema escalonado, donde los agentes de nivel superior dividen tareas en subtareas para que los agentes de nivel inferior las completen. | El agente de viajes cancela un viaje dividiendo la tarea en subtareas (por ejemplo, cancelar reservas específicas) y haciendo que los agentes de nivel inferior las completen, informando al agente de nivel superior.                                              |
| **Sistemas Multi-Agente (MAS)** | Los agentes completan tareas de forma independiente, ya sea cooperativa o competitivamente.                                           | Cooperativo: Múltiples agentes reservan servicios específicos de viaje como hoteles, vuelos y entretenimiento. Competitivo: Múltiples agentes gestionan y compiten por un calendario compartido de reservas de hotel para asignar clientes. |

## Cuándo Usar Agentes de IA

En la sección anterior, utilizamos el caso de uso del Agente de Viajes para explicar cómo los diferentes tipos de agentes pueden ser utilizados en distintos escenarios de reservas de viajes. Continuaremos utilizando esta aplicación a lo largo del curso.

Veamos los tipos de casos de uso para los que los Agentes de IA son más adecuados:

![¿Cuándo usar Agentes de IA?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.es.png)

- **Problemas Abiertos** - Permitir que el LLM determine los pasos necesarios para completar una tarea porque no siempre se pueden codificar de forma rígida en un flujo de trabajo.
- **Procesos de Múltiples Pasos** - Tareas que requieren un nivel de complejidad en el que el Agente de IA necesita usar herramientas o información en múltiples interacciones en lugar de una única recuperación.
- **Mejora con el Tiempo** - Tareas donde el agente puede mejorar con el tiempo al recibir retroalimentación de su entorno o de los usuarios para proporcionar una mejor utilidad.

Cubriremos más consideraciones sobre el uso de Agentes de IA en la lección sobre Construcción de Agentes de IA Confiables.

## Fundamentos de las Soluciones Agénticas

### Desarrollo de Agentes

El primer paso para diseñar un sistema de Agente de IA es definir las herramientas, acciones y comportamientos. En este curso, nos enfocamos en usar el **Azure AI Agent Service** para definir nuestros agentes. Ofrece características como:

- Selección de Modelos Abiertos como OpenAI, Mistral y Llama
- Uso de Datos con Licencia a través de proveedores como Tripadvisor
- Uso de herramientas estandarizadas OpenAPI 3.0

### Patrones Agénticos

La comunicación con los LLMs se realiza a través de prompts. Dada la naturaleza semi-autónoma de los Agentes de IA, no siempre es posible o necesario volver a hacer un prompt manualmente después de un cambio en el entorno. Utilizamos **Patrones Agénticos** que nos permiten hacer prompts al LLM en múltiples pasos de una manera más escalable.

Este curso está dividido en algunos de los patrones agénticos más populares actualmente.

### Frameworks Agénticos

Los Frameworks Agénticos permiten a los desarrolladores implementar patrones agénticos a través de código. Estos frameworks ofrecen plantillas, complementos y herramientas para una mejor colaboración entre Agentes de IA. Estas ventajas proporcionan capacidades para una mejor observabilidad y resolución de problemas en los sistemas de Agentes de IA.

En este curso, exploraremos el framework AutoGen, basado en investigación, y el framework Agent de Semantic Kernel, listo para producción.

### ¿Tienes Más Preguntas sobre los Agentes de IA?

Únete al [Discord de Azure AI Foundry](https://aka.ms/ai-agents/discord) para conectarte con otros estudiantes, asistir a horas de oficina y resolver tus dudas sobre los Agentes de IA.

## Lección Anterior

[Configuración del Curso](../00-course-setup/README.md)

## Próxima Lección

[Explorando Frameworks Agénticos](../02-explore-agentic-frameworks/README.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.