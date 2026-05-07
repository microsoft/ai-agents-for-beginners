[![Introducción a los Agentes de IA](../../../translated_images/es/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Introducción a los Agentes de IA y Casos de Uso de Agentes

¡Bienvenido al curso **Agentes de IA para Principiantes**! Este curso te brinda el conocimiento básico — y código funcional real — para comenzar a construir Agentes de IA desde cero.

Ven a saludar en la <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidad de Discord de Azure AI</a>, está llena de estudiantes y creadores de IA que estarán encantados de responder tus preguntas.

Antes de empezar a construir, asegurémonos de que realmente comprendemos qué es un Agente de IA y cuándo tiene sentido usar uno.

---

## Introducción

Esta lección cubre:

- Qué son los Agentes de IA y los diferentes tipos que existen
- Qué tipo de tareas son las más adecuadas para Agentes de IA
- Los componentes básicos que usarás al diseñar una solución agentica

## Objetivos de aprendizaje

Al finalizar esta lección, deberías poder:

- Explicar qué es un Agente de IA y cómo se diferencia de una solución de IA común
- Saber cuándo utilizar un Agente de IA (y cuándo no)
- Esbozar un diseño básico de solución agentica para un problema del mundo real

---

## Definiendo Agentes de IA y Tipos de Agentes de IA

### ¿Qué son los Agentes de IA?

Aquí tienes una forma sencilla de pensarlo:

> **Los Agentes de IA son sistemas que permiten que los Modelos de Lenguaje Grande (LLMs) realmente *hagan cosas* — dándoles herramientas y conocimiento para actuar en el mundo, no solo responder a indicaciones.**

Desglosemos eso un poco:

- **Sistema** — Un Agente de IA no es solo una cosa. Es una colección de partes que trabajan juntas. En esencia, cada agente tiene tres componentes:
  - **Entorno** — El espacio en el que el agente trabaja. Para un agente de reserva de viajes, sería la misma plataforma de reservas.
  - **Sensores** — Cómo el agente lee el estado actual de su entorno. Nuestro agente de viajes podría revisar la disponibilidad de hoteles o los precios de vuelos.
  - **Actuadores** — Cómo el agente toma acción. El agente podría reservar una habitación, enviar una confirmación o cancelar una reserva.

![¿Qué son los Agentes de IA?](../../../translated_images/es/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modelos de Lenguaje Grande** — Los agentes existían antes de los LLMs, pero los LLMs son lo que hace a los agentes modernos tan poderosos. Pueden entender lenguaje natural, razonar sobre el contexto y convertir una solicitud vaga del usuario en un plan de acción concreto.

- **Realizar Acciones** — Sin un sistema agente, un LLM solo genera texto. Dentro de un sistema agente, el LLM puede realmente *ejecutar* pasos — buscar en una base de datos, llamar a una API, enviar un mensaje.

- **Acceso a Herramientas** — Qué herramientas puede usar el agente depende de (1) el entorno en el que está funcionando y (2) lo que el desarrollador eligió darle. Un agente de viajes podría buscar vuelos pero no editar registros de clientes — todo depende de lo que conectes.

- **Memoria + Conocimiento** — Los agentes pueden tener memoria a corto plazo (la conversación actual) y memoria a largo plazo (una base de datos de clientes, interacciones pasadas). El agente de viajes podría "recordar" que prefieres asientos junto a la ventana.

---

### Los Diferentes Tipos de Agentes de IA

No todos los agentes están construidos igual. Aquí tienes un desglose de los principales tipos, usando un agente de reserva de viajes como ejemplo recurrente:

| **Tipo de Agente** | **Qué Hace** | **Ejemplo con Agente de Viajes** |
|---|---|---|
| **Agentes de Reflejo Simple** | Sigue reglas codificadas — sin memoria, sin planificación. | Ve un correo de queja → lo reenvía al servicio al cliente. Eso es todo. |
| **Agentes de Reflejo Basados en Modelo** | Mantiene un modelo interno del mundo y lo actualiza conforme cambian las cosas. | Rastrea precios históricos de vuelos y avisa de rutas que se vuelven caras repentinamente. |
| **Agentes Basados en Objetivos** | Tiene un objetivo en mente y descubre cómo alcanzarlo paso a paso. | Reserva un viaje completo (vuelos, coche, hotel) empezando desde tu ubicación actual para llegar a tu destino. |
| **Agentes Basados en Utilidad** | No solo encuentra *una* solución — encuentra *la mejor* sopesando compensaciones. | Equilibra costo vs conveniencia para encontrar el viaje que más se ajusta a tus preferencias. |
| **Agentes de Aprendizaje** | Mejora con el tiempo aprendiendo de las respuestas. | Ajusta futuras recomendaciones de reserva según resultados de encuestas post-viaje. |
| **Agentes Jerárquicos** | Un agente de alto nivel divide el trabajo en subtareas y delega a agentes de nivel inferior. | Una solicitud de "cancelar viaje" se divide en: cancelar vuelo, cancelar hotel, cancelar alquiler de coche — cada uno manejado por un subagente. |
| **Sistemas Multiagente (MAS)** | Múltiples agentes independientes trabajando juntos (o compitiendo). | Cooperativo: agentes separados manejan hoteles, vuelos y entretenimiento. Competitivo: varios agentes compiten para llenar habitaciones de hotel al mejor precio. |

---

## Cuándo usar Agentes de IA

Solo porque *puedes* usar un Agente de IA no significa que siempre *debas* usarlo. Aquí están las situaciones donde los agentes realmente destacan:

![¿Cuándo usar Agentes de IA?](../../../translated_images/es/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemas Abiertos** — Cuando los pasos para resolver un problema no pueden ser preprogramados. Necesitas que el LLM descubra el camino dinámicamente.
- **Procesos de Múltiples Pasos** — Tareas que requieren usar herramientas en varios turnos, no solo una búsqueda o generación única.
- **Mejora a lo Largo del Tiempo** — Cuando quieres que el sistema se vuelva más inteligente basado en feedback de usuarios o señales del entorno.

Profundizaremos más en cuándo (y cuándo *no*) usar Agentes de IA en la lección **Construyendo Agentes de IA Confiables** más adelante en el curso.

---

## Conceptos básicos de Soluciones Agenticas

### Desarrollo de Agentes

Lo primero que haces al construir un agente es definir *qué puede hacer* — sus herramientas, acciones y comportamientos.

En este curso, usamos el **Azure AI Agent Service** como nuestra plataforma principal. Soporta:

- Modelos abiertos como OpenAI, Mistral y Llama
- Datos con licencia de proveedores como Tripadvisor
- Definiciones de herramientas OpenAPI 3.0 estandarizadas

### Patrones Agenticos

Te comunicas con LLMs mediante indicaciones. Con agentes, no siempre puedes crear cada indicación manualmente — el agente necesita actuar en varios pasos. Ahí es donde entran los **Patrones Agenticos**. Son estrategias reutilizables para indicar y orquestar LLMs de manera más escalable y confiable.

Este curso está estructurado alrededor de los patrones agenticos más comunes y útiles.

### Frameworks Agenticos

Los Frameworks Agenticos ofrecen a los desarrolladores plantillas, herramientas e infraestructura listas para construir agentes. Facilitan:

- Conectar herramientas y capacidades
- Observar lo que hace el agente (y depurar cuando algo falla)
- Colaborar entre múltiples agentes

En este curso, nos enfocamos en el **Microsoft Agent Framework (MAF)** para crear agentes listos para producción.

---

## Ejemplos de Código

¿Listo para verlo en acción? Aquí están los ejemplos de código para esta lección:

- 🐍 Python: [Framework de Agentes](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Framework de Agentes](./code_samples/01-dotnet-agent-framework.md)

---

## ¿Tienes Preguntas?

Únete al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conectar con otros estudiantes, asistir a horas de oficina, y obtener respuestas a tus preguntas sobre Agentes de IA por parte de la comunidad.

---

## Lección Anterior

[Configuración del Curso](../00-course-setup/README.md)

## Próxima Lección

[Explorando Frameworks Agenticos](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->