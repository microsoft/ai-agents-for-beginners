[![Introducción a los Agentes de IA](../../../translated_images/es/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Introducción a los Agentes de IA y Casos de Uso de Agentes

¡Bienvenido al curso **Agentes de IA para Principiantes**! Este curso te brinda el conocimiento fundamental — y código funcional real — para comenzar a construir Agentes de IA desde cero.

Ven a saludar en la <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidad Discord de Azure AI</a> — está llena de aprendices y creadores de IA que están felices de responder preguntas.

Antes de comenzar a construir, asegurémonos de comprender realmente qué es un Agente de IA y cuándo tiene sentido usar uno.

---

## Introducción

Esta lección cubre:

- Qué son los Agentes de IA y los diferentes tipos que existen
- Para qué tipos de tareas son más adecuados los Agentes de IA
- Los bloques centrales que usarás al diseñar una solución Agentic

## Objetivos de Aprendizaje

Al final de esta lección, deberías ser capaz de:

- Explicar qué es un Agente de IA y cómo se diferencia de una solución de IA normal
- Saber cuándo usar un Agente de IA (y cuándo no)
- Esbozar un diseño básico de solución Agentic para un problema del mundo real

---

## Definición de Agentes de IA y Tipos de Agentes de IA

### ¿Qué son los Agentes de IA?

Aquí hay una manera simple de pensarlo:

> **Los Agentes de IA son sistemas que permiten que los Modelos de Lenguaje Grandes (LLMs) realmente *hagan cosas* — dándoles herramientas y conocimiento para actuar en el mundo, no solo responder a instrucciones.**

Vamos a desglosar eso un poco:

- **Sistema** — Un Agente de IA no es solo una cosa. Es una colección de partes que trabajan juntas. En su núcleo, cada agente tiene tres piezas:
  - **Entorno** — El espacio en el que trabaja el agente. Para un agente de reservas de viajes, este sería la plataforma de reservas misma.
  - **Sensores** — Cómo el agente lee el estado actual de su entorno. Nuestro agente de viajes podría verificar la disponibilidad de hoteles o precios de vuelos.
  - **Actuadores** — Cómo el agente toma acción. El agente de viajes podría reservar una habitación, enviar una confirmación o cancelar una reserva.

![¿Qué son los Agentes de IA?](../../../translated_images/es/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modelos de Lenguaje Grandes** — Los agentes existían antes de los LLMs, pero los LLMs son lo que hace que los agentes modernos sean tan poderosos. Pueden entender lenguaje natural, razonar sobre el contexto y convertir una solicitud vaga del usuario en un plan concreto de acción.

- **Realizar Acciones** — Sin un sistema de agente, un LLM solo genera texto. Dentro de un sistema de agente, el LLM puede realmente *ejecutar* pasos — buscar en una base de datos, llamar a una API, enviar un mensaje.

- **Acceso a Herramientas** — Las herramientas que el agente puede usar dependen de (1) el entorno en el que se ejecuta y (2) lo que el desarrollador eligió darle. Un agente de viajes podría ser capaz de buscar vuelos pero no editar registros de clientes — todo depende de lo que conectes.

- **Memoria + Conocimiento** — Los agentes pueden tener memoria a corto plazo (la conversación actual) y memoria a largo plazo (una base de datos de clientes, interacciones pasadas). El agente de viajes podría "recordar" que prefieres asientos junto a la ventana.

---

### Los Diferentes Tipos de Agentes de IA

No todos los agentes están construidos igual. Aquí tienes un desglose de los tipos principales, usando un agente de reservas de viajes como ejemplo recurrente:

| **Tipo de Agente** | **Qué Hace** | **Ejemplo de Agente de Viajes** |
|---|---|---|
| **Agentes de Reflejo Simple** | Sigue reglas codificadas — sin memoria, ni planificación. | Ve un correo de queja → lo reenvía al servicio al cliente. Eso es todo. |
| **Agentes de Reflejo Basados en Modelo** | Mantiene un modelo interno del mundo y lo actualiza a medida que cambian las cosas. | Rastrea precios históricos de vuelos y señala rutas que de repente son caras. |
| **Agentes Basados en Metas** | Tiene una meta en mente y averigua cómo alcanzarla paso a paso. | Reserva un viaje completo (vuelos, auto, hotel) comenzando desde tu ubicación actual para llevarte a tu destino. |
| **Agentes Basados en Utilidad** | No solo encuentra *una* solución — encuentra la *mejor* sopesando las compensaciones. | Balancea costo versus conveniencia para encontrar el viaje que mejor se adapta a tus preferencias. |
| **Agentes de Aprendizaje** | Mejora con el tiempo aprendiendo de retroalimentación. | Ajusta recomendaciones futuras de reservas según resultados de encuestas post-viaje. |
| **Agentes Jerárquicos** | Un agente de alto nivel divide el trabajo en subtareas y delega a agentes de nivel inferior. | Una solicitud de "cancelar viaje" se divide en: cancelar vuelo, cancelar hotel, cancelar alquiler de auto — cada uno manejado por un sub-agente. |
| **Sistemas Multi-Agente (MAS)** | Múltiples agentes independientes trabajan juntos (o compiten). | Cooperativo: agentes separados manejan hoteles, vuelos y entretenimiento. Competitivo: varios agentes compiten para llenar habitaciones de hotel al mejor precio. |

---

## Cuándo Usar Agentes de IA

Solo porque *puedes* usar un Agente de IA no significa que siempre *debas*. Aquí están las situaciones donde los agentes realmente destacan:

![¿Cuándo usar Agentes de IA?](../../../translated_images/es/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemas Abiertos** — Cuando los pasos para resolver un problema no pueden ser preprogramados. Necesitas que el LLM descubra el camino dinámicamente.
- **Procesos de Múltiples Pasos** — Tareas que requieren usar herramientas a lo largo de varios turnos, no solo una búsqueda o generación única.
- **Mejora con el Tiempo** — Cuando quieres que el sistema se vuelva más inteligente basado en la retroalimentación de usuarios o señales del entorno.

Profundizaremos más en cuándo (y cuándo *no*) usar Agentes de IA en la lección **Construyendo Agentes de IA Confiables** más adelante en el curso.

---

## Fundamentos de Soluciones Agentic

### Desarrollo de Agentes

Lo primero que haces al construir un agente es definir *qué puede hacer* — sus herramientas, acciones y comportamientos.

En este curso, usamos el **Microsoft Foundry Agent Service** como nuestra plataforma principal. Soporta:

- Modelos de proveedores como OpenAI, Mistral y Meta (Llama)
- Datos licenciados de proveedores como Tripadvisor
- Definiciones de herramientas estandarizadas OpenAPI 3.0

### Patrones Agentic

Te comunicas con los LLMs mediante indicaciones. Con agentes, no siempre puedes crear cada indicación manualmente — el agente necesita actuar a través de muchos pasos. Ahí es donde entran los **Patrones Agentic**. Son estrategias reutilizables para inducir y orquestar LLMs de una manera más escalable y confiable.

Este curso está estructurado en torno a los patrones agentic más comunes y útiles.

### Marcos Agentic

Los Marcos Agentic brindan a los desarrolladores plantillas, herramientas e infraestructura listas para construir agentes. Facilitan:

- Conectar herramientas y capacidades
- Observar lo que el agente está haciendo (y depurar cuando algo falla)
- Colaborar entre múltiples agentes

En este curso, nos enfocamos en el **Microsoft Agent Framework (MAF)** para construir agentes listos para producción.

---

## Ejemplos de Código

¿Listo para verlo en acción? Aquí están los ejemplos de código para esta lección:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## ¿Tienes Preguntas?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conectar con otros aprendices, asistir a horas de oficina y obtener respuestas a tus preguntas sobre Agentes de IA por parte de la comunidad.


---

## Pruebas Rápidas a Este Agente (Opcional)

Una vez que aprendas a desplegar agentes en la [Lección 16](../16-deploying-scalable-agents/README.md), puedes agregar una comprobación rápida de salud posterior al despliegue para el `TravelAgent` de esta lección con el catálogo listo [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Consulta [`tests/README.md`](../tests/README.md) para saber cómo ejecutarlo.

---

## Lección Anterior

[Configuración del Curso](../00-course-setup/README.md)

## Siguiente Lección

[Explorando Marcos Agentic](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->