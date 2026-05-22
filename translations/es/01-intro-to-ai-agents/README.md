[![Introducción a los Agentes de IA](../../../translated_images/es/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Haz clic en la imagen arriba para ver el video de esta lección)_

# Introducción a los Agentes de IA y Casos de Uso de Agentes

¡Bienvenido al curso **Agentes de IA para Principiantes**! Este curso te brinda el conocimiento fundamental —y código funcional real— para comenzar a construir agentes de IA desde cero.

Ven a saludar a la <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidad de Azure AI en Discord</a> — está llena de estudiantes y creadores de IA que estarán encantados de responder tus preguntas.

Antes de comenzar a construir, asegurémonos de entender realmente qué es un agente de IA y cuándo tiene sentido usar uno.

---

## Introducción

Esta lección cubre:

- Qué son los Agentes de IA y los diferentes tipos que existen
- Para qué tipo de tareas son más adecuados los Agentes de IA
- Los bloques de construcción principales que usarás al diseñar una solución agentica

## Objetivos de Aprendizaje

Al finalizar esta lección, deberías ser capaz de:

- Explicar qué es un Agente de IA y en qué se diferencia de una solución de IA convencional
- Saber cuándo es apropiado usar un Agente de IA (y cuándo no)
- Esbozar un diseño básico de una solución agentica para un problema del mundo real

---

## Definiendo Agentes de IA y Tipos de Agentes de IA

### ¿Qué son los Agentes de IA?

Aquí tienes una forma simple de pensarlo:

> **Los Agentes de IA son sistemas que permiten a los Modelos de Lenguaje Grande (LLMs) realmente *hacer cosas* — dándoles herramientas y conocimiento para actuar sobre el mundo, no solo para responder a solicitudes.**

Desglosemos eso un poco:

- **Sistema** — Un agente de IA no es solo una cosa. Es una colección de partes que trabajan juntas. En su núcleo, cada agente tiene tres componentes:
  - **Entorno** — El espacio en el que el agente trabaja. Para un agente de reservas de viajes, sería la propia plataforma de reservas.
  - **Sensores** — Cómo el agente lee el estado actual de su entorno. Nuestro agente de viajes podría consultar disponibilidad de hoteles o precios de vuelos.
  - **Actuadores** — Cómo el agente toma acciones. El agente de viajes podría reservar una habitación, enviar una confirmación o cancelar una reserva.

![¿Qué Son los Agentes de IA?](../../../translated_images/es/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modelos de Lenguaje Grande** — Los agentes existían antes de los LLM, pero los LLM son los que hacen a los agentes modernos tan poderosos. Ellos pueden entender lenguaje natural, razonar sobre el contexto y convertir una solicitud vaga del usuario en un plan de acción concreto.

- **Realizar Acciones** — Sin un sistema agente, un LLM solo genera texto. Dentro de un sistema agente, el LLM puede realmente *ejecutar* pasos — buscar en una base de datos, llamar a una API, enviar un mensaje.

- **Acceso a Herramientas** — Qué herramientas puede usar el agente depende de (1) el entorno en el que está funcionando y (2) lo que el desarrollador decidió proporcionarle. Un agente de viajes podría poder buscar vuelos pero no editar registros de clientes — todo depende de lo que conectes.

- **Memoria + Conocimiento** — Los agentes pueden tener memoria a corto plazo (la conversación actual) y memoria a largo plazo (una base de datos de clientes, interacciones pasadas). El agente de viajes podría "recordar" que prefieres asientos de ventana.

---

### Los Diferentes Tipos de Agentes de IA

No todos los agentes están construidos igual. Aquí tienes un desglose de los tipos principales, usando un agente de reservas de viajes como ejemplo recurrente:

| **Tipo de Agente** | **Qué Hace** | **Ejemplo de Agente de Viajes** |
|---|---|---|
| **Agentes de Reflejo Simple** | Sigue reglas codificadas — no tiene memoria ni planificación. | Ve un correo de queja → lo reenvía a servicio al cliente. Eso es todo. |
| **Agentes de Reflejo Basados en Modelo** | Mantiene un modelo interno del mundo y lo actualiza a medida que cambian las cosas. | Rastrea precios históricos de vuelos y señala rutas que de repente son caras. |
| **Agentes Basados en Objetivos** | Tiene un objetivo en mente y descubre cómo alcanzarlo paso a paso. | Reserva un viaje completo (vuelos, coche, hotel) desde tu ubicación actual para llevarte a tu destino. |
| **Agentes Basados en Utilidad** | No solo encuentra *una* solución — encuentra la *mejor* evaluando las compensaciones. | Equilibra costo vs. conveniencia para encontrar el viaje que mejor se ajusta a tus preferencias. |
| **Agentes de Aprendizaje** | Mejora con el tiempo aprendiendo de la retroalimentación. | Ajusta recomendaciones de reservas futuras basándose en resultados de encuestas posteriores al viaje. |
| **Agentes Jerárquicos** | Un agente de alto nivel divide el trabajo en subtareas y delega a agentes de nivel inferior. | Una solicitud de “cancelar viaje” se divide en: cancelar vuelo, cancelar hotel, cancelar alquiler de coche — cada uno manejado por un subagente. |
| **Sistemas Multi-Agente (MAS)** | Varios agentes independientes trabajando juntos (o compitiendo). | Cooperativo: agentes separados manejan hoteles, vuelos y entretenimiento. Competitivo: varios agentes compiten para llenar habitaciones de hotel al mejor precio. |

---

## Cuándo Usar Agentes de IA

El hecho de que *puedas* usar un agente de IA no significa que siempre *debas* usarlo. Aquí están las situaciones en las que los agentes realmente destacan:

![¿Cuándo usar Agentes de IA?](../../../translated_images/es/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemas Abiertos** — Cuando no se pueden programar de antemano los pasos para resolver un problema. Necesitas que el LLM descubra el camino de forma dinámica.
- **Procesos de Múltiples Pasos** — Tareas que requieren usar herramientas a lo largo de varios turnos, no solo una consulta o generación única.
- **Mejora con el Tiempo** — Cuando quieres que el sistema se vuelva más inteligente basándose en retroalimentación de usuarios o señales del entorno.

Exploraremos más a fondo cuándo (y cuándo *no*) usar Agentes de IA en la lección **Construyendo Agentes de IA Confiables** más adelante en el curso.

---

## Fundamentos de Soluciones Agenticas

### Desarrollo de Agentes

Lo primero que haces al construir un agente es definir *lo que puede hacer* — sus herramientas, acciones y comportamientos.

En este curso, usamos el **Azure AI Agent Service** como plataforma principal. Soporta:

- Modelos de proveedores como OpenAI, Mistral y Meta (Llama)
- Datos licenciados de proveedores como Tripadvisor
- Definiciones de herramientas estandarizadas OpenAPI 3.0

### Patrones Agenticos

Te comunicas con los LLM mediante prompts. Con los agentes, no siempre puedes crear manualmente cada prompt — el agente necesita actuar a lo largo de muchos pasos. Ahí es donde entran los **Patrones Agenticos**. Son estrategias reutilizables para hacer prompts y orquestar LLMs de forma más escalable y confiable.

Este curso está estructurado alrededor de los patrones agenticos más comunes y útiles.

### Frameworks Agenticos

Los Frameworks Agenticos ofrecen a los desarrolladores plantillas, herramientas e infraestructura listas para crear agentes. Facilitan:

- Conectar herramientas y capacidades
- Observar lo que el agente está haciendo (y depurar cuando algo falla)
- Colaborar entre múltiples agentes

En este curso, nos enfocamos en el **Microsoft Agent Framework (MAF)** para construir agentes listos para producción.

---

## Ejemplos de Código

¿Listo para verlo en acción? Aquí tienes los ejemplos de código para esta lección:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## ¿Tienes Preguntas?

Únete al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conectar con otros estudiantes, asistir a horas de oficina y obtener respuestas a tus preguntas sobre Agentes de IA por parte de la comunidad.

---

## Lección Anterior

[Configuración del Curso](../00-course-setup/README.md)

## Próxima Lección

[Explorando Frameworks Agenticos](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->