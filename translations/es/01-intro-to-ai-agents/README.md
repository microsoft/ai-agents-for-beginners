[![Introducción a los Agentes de IA](../../../translated_images/es/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Haz clic en la imagen arriba para ver el video de esta lección)_


# Introducción a los Agentes de IA y Casos de Uso de Agentes

¡Bienvenido al curso "Agentes de IA para Principiantes"! Este curso proporciona conocimientos fundamentales y ejemplos aplicados para construir Agentes de IA.

Únete a la <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidad de Discord de Azure AI</a> para conocer a otros estudiantes y constructores de Agentes de IA y hacer cualquier pregunta que tengas sobre este curso.

Para comenzar este curso, empezamos entendiendo mejor qué son los Agentes de IA y cómo podemos usarlos en las aplicaciones y flujos de trabajo que construimos.

## Introducción

Esta lección cubre:

- ¿Qué son los Agentes de IA y cuáles son los diferentes tipos de agentes?
- ¿Para qué casos de uso son mejores los Agentes de IA y cómo pueden ayudarnos?
- ¿Cuáles son algunos de los componentes básicos al diseñar Soluciones Agentes?

## Objetivos de Aprendizaje
Después de completar esta lección, deberías ser capaz de:

- Entender los conceptos de Agentes de IA y cómo se diferencian de otras soluciones de IA.
- Aplicar los Agentes de IA de manera más eficiente.
- Diseñar soluciones Agentes productivamente tanto para usuarios como para clientes.

## Definición de Agentes de IA y Tipos de Agentes de IA

### ¿Qué son los Agentes de IA?

Los Agentes de IA son **sistemas** que permiten a los **Modelos de Lenguaje Extensos (LLMs)** **realizar acciones** al extender sus capacidades dando a los LLM **acceso a herramientas** y **conocimiento**.

Desglosemos esta definición en partes más pequeñas:

- **Sistema** - Es importante pensar en los agentes no solo como un componente único, sino como un sistema de muchos componentes. A nivel básico, los componentes de un Agente de IA son:
  - **Entorno** - El espacio definido donde el Agente de IA opera. Por ejemplo, si tuviéramos un agente de IA para reservas de viajes, el entorno podría ser el sistema de reservas de viajes que el Agente de IA usa para completar tareas.
  - **Sensores** - Los entornos tienen información y proporcionan retroalimentación. Los Agentes de IA usan sensores para recopilar e interpretar esta información sobre el estado actual del entorno. En el ejemplo del Agente de Reservas de Viaje, el sistema de reservas puede proporcionar información como disponibilidad de hoteles o precios de vuelos.
  - **Actuadores** - Una vez que el Agente de IA recibe el estado actual del entorno, para la tarea actual el agente determina qué acción realizar para cambiar el entorno. Para el agente de reservas de viaje, podría ser reservar una habitación disponible para el usuario.

![¿Qué son los Agentes de IA?](../../../translated_images/es/what-are-ai-agents.1ec8c4d548af601a.webp)

**Modelos de Lenguaje Extensos** - El concepto de agentes existía antes de la creación de los LLMs. La ventaja de construir Agentes de IA con LLMs es su capacidad para interpretar el lenguaje humano y los datos. Esta habilidad permite a los LLM interpretar información ambiental y definir un plan para cambiar el entorno.

**Realizar Acciones** - Fuera de los sistemas de agentes de IA, los LLM están limitados a situaciones donde la acción es generar contenido o información basada en la solicitud del usuario. Dentro de los sistemas de agentes de IA, los LLM pueden cumplir tareas al interpretar la solicitud del usuario y usar herramientas disponibles en su entorno.

**Acceso a Herramientas** - Las herramientas a las que el LLM tiene acceso están definidas por 1) el entorno en el que opera y 2) el desarrollador del Agente de IA. Para nuestro ejemplo del agente de viajes, las herramientas del agente están limitadas por las operaciones disponibles en el sistema de reservas y/o el desarrollador puede limitar el acceso del agente a las herramientas relacionadas con vuelos.

**Memoria+Conocimiento** - La memoria puede ser a corto plazo en el contexto de la conversación entre el usuario y el agente. A largo plazo, más allá de la información proporcionada por el entorno, los Agentes de IA también pueden recuperar conocimiento de otros sistemas, servicios, herramientas e incluso otros agentes. En el ejemplo del agente de viajes, este conocimiento podría ser la información sobre las preferencias de viaje del usuario ubicada en una base de datos de clientes.

### Los diferentes tipos de agentes

Ahora que tenemos una definición general de Agentes de IA, veamos algunos tipos específicos de agentes y cómo se aplicarían a un agente de IA de reservas de viajes.

| **Tipo de Agente**                | **Descripción**                                                                                                                       | **Ejemplo**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agentes Reflexivos Simples**      | Realizan acciones inmediatas basadas en reglas predefinidas.                                                                                  | El agente de viajes interpreta el contexto del correo electrónico y reenvía quejas de viaje al servicio al cliente.                                                                                                                          |
| **Agentes Reflexivos Basados en Modelo** | Realizan acciones basadas en un modelo del mundo y cambios a ese modelo.                                                              | El agente de viajes prioriza rutas con cambios significativos de precio basándose en acceso a datos históricos de precios.                                                                                                             |
| **Agentes Basados en Objetivos**         | Crean planes para lograr metas específicas interpretando la meta y determinando acciones para alcanzarla.                                  | El agente de viajes reserva un viaje determinando los arreglos necesarios (coche, transporte público, vuelos) desde la ubicación actual hasta el destino.                                                                                |
| **Agentes Basados en Utilidad**      | Consideran preferencias y ponderan compensaciones numéricas para determinar cómo alcanzar metas.                                               | El agente de viajes maximiza la utilidad sopesando conveniencia versus costo al reservar viajes.                                                                                                                                          |
| **Agentes de Aprendizaje**           | Mejoran con el tiempo respondiendo a retroalimentación y ajustando acciones en consecuencia.                                                        | El agente de viajes mejora usando la retroalimentación de clientes de encuestas posteriores al viaje para hacer ajustes en futuras reservas.                                                                                                               |
| **Agentes Jerárquicos**       | Presentan múltiples agentes en un sistema por niveles, con agentes de nivel superior que dividen tareas en subtareas para que agentes de nivel inferior las completen. | El agente de viajes cancela un viaje dividiendo la tarea en subtareas (por ejemplo, cancelar reservas específicas) y haciendo que agentes de nivel inferior las completen, reportando al agente de nivel superior.                                     |
| **Sistemas Multiagente (MAS)** | Los agentes completan tareas independientemente, ya sea cooperativa o competitivamente.                                                           | Cooperativo: Múltiples agentes reservan servicios de viaje específicos como hoteles, vuelos y entretenimiento. Competitivo: Múltiples agentes gestionan y compiten por un calendario compartido de reservas hoteleras para alojar clientes en el hotel. |

## Cuándo usar Agentes de IA

En la sección anterior, usamos el caso de uso del Agente de Viajes para explicar cómo diferentes tipos de agentes pueden usarse en distintos escenarios de reserva de viajes. Continuaremos usando esta aplicación durante todo el curso.

Veamos los tipos de casos de uso para los que los Agentes de IA son mejor usados:

![¿Cuándo usar Agentes de IA?](../../../translated_images/es/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Problemas Abiertos** - permitiendo que el LLM determine los pasos necesarios para completar una tarea porque no siempre puede codificarse rígidamente en un flujo de trabajo.
- **Procesos de Múltiples Pasos** - tareas que requieren un nivel de complejidad donde el Agente de IA necesita usar herramientas o información a lo largo de múltiples turnos en lugar de una sola recuperación.  
- **Mejora con el Tiempo** - tareas donde el agente puede mejorar con el tiempo recibiendo retroalimentación ya sea de su entorno o de los usuarios para proporcionar mejor utilidad.

Cubrimos más consideraciones sobre el uso de Agentes de IA en la lección de Construcción de Agentes de IA Confiables.

## Conceptos Básicos de Soluciones Agentes

### Desarrollo de Agentes

El primer paso para diseñar un sistema de Agente de IA es definir las herramientas, acciones y comportamientos. En este curso, nos enfocamos en usar el **Servicio de Agentes Azure AI** para definir nuestros Agentes. Ofrece características como:

- Selección de Modelos Abiertos como OpenAI, Mistral y Llama
- Uso de Datos Licenciados a través de proveedores como Tripadvisor
- Uso de herramientas estandarizadas OpenAPI 3.0

### Patrones Agentes

La comunicación con los LLM se realiza mediante prompts. Dada la naturaleza semi-autónoma de los Agentes de IA, no siempre es posible o necesario volver a activar el prompt del LLM después de un cambio en el entorno. Usamos **Patrones Agentes** que nos permiten solicitar al LLM en múltiples pasos de forma más escalable.

Este curso está dividido en algunos de los patrones agentes populares actuales.

### Marcos Agentes

Los Marcos Agentes permiten a los desarrolladores implementar patrones agentes mediante código. Estos marcos ofrecen plantillas, plugins y herramientas para una mejor colaboración entre Agentes de IA. Estos beneficios proporcionan capacidades para una mejor observabilidad y solución de problemas en sistemas de Agentes de IA.

En este curso, exploraremos el Microsoft Agent Framework (MAF) para construir agentes de IA listos para producción.

## Códigos de Ejemplo

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## ¿Tienes Más Preguntas sobre Agentes de IA?

Únete al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conocer a otros estudiantes, asistir a horas de oficina y obtener respuestas a tus preguntas sobre Agentes de IA.

## Lección Anterior

[Configuración del Curso](../00-course-setup/README.md)

## Próxima Lección

[Explorando Marcos Agentes](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->