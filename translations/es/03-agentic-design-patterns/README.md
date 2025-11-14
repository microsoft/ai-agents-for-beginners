<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c46e4ff9e349c521e2b0b17f51afa64",
  "translation_date": "2025-08-30T13:17:13+00:00",
  "source_file": "03-agentic-design-patterns/README.md",
  "language_code": "es"
}
-->
[![Cómo Diseñar Agentes de IA Eficaces](../../../translated_images/lesson-3-thumbnail.1092dd7a8f1074a5b26e35aa8f810814e05a22fed1765c20c14b2b508c7ae379.es.png)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_
# Principios de Diseño de Agentes de IA

## Introducción

Existen muchas formas de pensar en la construcción de sistemas de agentes de IA. Dado que la ambigüedad es una característica y no un defecto en el diseño de IA generativa, a veces es difícil para los ingenieros saber por dónde empezar. Hemos creado un conjunto de principios de diseño centrados en el usuario para permitir a los desarrolladores construir sistemas de agentes centrados en el cliente que resuelvan sus necesidades empresariales. Estos principios de diseño no son una arquitectura prescriptiva, sino un punto de partida para los equipos que están definiendo y desarrollando experiencias de agentes.

En general, los agentes deberían:

- Ampliar y escalar las capacidades humanas (lluvia de ideas, resolución de problemas, automatización, etc.)
- Rellenar vacíos de conocimiento (ponerse al día en dominios de conocimiento, traducción, etc.)
- Facilitar y apoyar la colaboración de la manera en que preferimos trabajar con otros
- Ayudarnos a ser mejores versiones de nosotros mismos (por ejemplo, entrenador de vida/gestor de tareas, ayudándonos a aprender habilidades de regulación emocional y atención plena, construir resiliencia, etc.)

## Esta Lección Cubrirá

- Qué son los Principios de Diseño de Agentes
- Cuáles son algunas pautas a seguir al implementar estos principios de diseño
- Ejemplos de uso de los principios de diseño

## Objetivos de Aprendizaje

Después de completar esta lección, podrás:

1. Explicar qué son los Principios de Diseño de Agentes
2. Explicar las pautas para usar los Principios de Diseño de Agentes
3. Comprender cómo construir un agente utilizando los Principios de Diseño de Agentes

## Los Principios de Diseño de Agentes

![Principios de Diseño de Agentes](../../../translated_images/agentic-design-principles.1cfdf8b6d3cc73c2b738951ee7b2043e224441d98babcf654be69d866120f93a.es.png)

### Agente (Espacio)

Este es el entorno en el que opera el agente. Estos principios informan cómo diseñamos agentes para interactuar en mundos físicos y digitales.

- **Conectar, no reemplazar** – ayudar a conectar personas con otras personas, eventos y conocimiento accionable para habilitar la colaboración y conexión.
- Los agentes ayudan a conectar eventos, conocimiento y personas.
- Los agentes acercan a las personas. No están diseñados para reemplazar o menospreciar a las personas.
- **Fácilmente accesible pero ocasionalmente invisible** – el agente opera principalmente en segundo plano y solo nos alerta cuando es relevante y apropiado.
  - El agente es fácilmente descubrible y accesible para usuarios autorizados en cualquier dispositivo o plataforma.
  - El agente admite entradas y salidas multimodales (sonido, voz, texto, etc.).
  - El agente puede pasar sin problemas entre primer plano y segundo plano; entre proactivo y reactivo, dependiendo de su percepción de las necesidades del usuario.
  - El agente puede operar de forma invisible, pero su proceso en segundo plano y colaboración con otros agentes son transparentes y controlables por el usuario.

### Agente (Tiempo)

Esto se refiere a cómo opera el agente a lo largo del tiempo. Estos principios informan cómo diseñamos agentes que interactúan en el pasado, presente y futuro.

- **Pasado**: Reflexionar sobre la historia que incluye tanto estado como contexto.
  - El agente proporciona resultados más relevantes basados en el análisis de datos históricos más ricos, más allá del evento, las personas o los estados.
  - El agente crea conexiones a partir de eventos pasados y reflexiona activamente sobre la memoria para interactuar con situaciones actuales.
- **Ahora**: Dar empujones más que notificaciones.
  - El agente adopta un enfoque integral para interactuar con las personas. Cuando ocurre un evento, el agente va más allá de la notificación estática u otra formalidad estática. El agente puede simplificar flujos o generar dinámicamente señales para dirigir la atención del usuario en el momento adecuado.
  - El agente entrega información basada en el entorno contextual, cambios sociales y culturales, y adaptada a la intención del usuario.
  - La interacción del agente puede ser gradual, evolucionando/creciendo en complejidad para empoderar a los usuarios a largo plazo.
- **Futuro**: Adaptarse y evolucionar.
  - El agente se adapta a varios dispositivos, plataformas y modalidades.
  - El agente se adapta al comportamiento del usuario, necesidades de accesibilidad y es completamente personalizable.
  - El agente se forma y evoluciona a través de la interacción continua con el usuario.

### Agente (Núcleo)

Estos son los elementos clave en el núcleo del diseño de un agente.

- **Aceptar la incertidumbre pero establecer confianza**.
  - Se espera un cierto nivel de incertidumbre en el agente. La incertidumbre es un elemento clave del diseño de agentes.
  - La confianza y la transparencia son capas fundamentales del diseño de agentes.
  - Los humanos tienen el control de cuándo el agente está encendido/apagado y el estado del agente es claramente visible en todo momento.

## Las Pautas para Implementar Estos Principios

Cuando utilices los principios de diseño anteriores, sigue las siguientes pautas:

1. **Transparencia**: Informa al usuario que hay IA involucrada, cómo funciona (incluyendo acciones pasadas) y cómo dar retroalimentación y modificar el sistema.
2. **Control**: Permite al usuario personalizar, especificar preferencias y personalizar, y tener control sobre el sistema y sus atributos (incluida la capacidad de olvidar).
3. **Consistencia**: Busca experiencias consistentes y multimodales en dispositivos y puntos de acceso. Usa elementos familiares de UI/UX cuando sea posible (por ejemplo, ícono de micrófono para interacción por voz) y reduce la carga cognitiva del cliente tanto como sea posible (por ejemplo, busca respuestas concisas, ayudas visuales y contenido de "Aprender más").

## Cómo Diseñar un Agente de Viajes Usando Estos Principios y Pautas

Imagina que estás diseñando un Agente de Viajes, aquí tienes cómo podrías pensar en usar los Principios de Diseño y las Pautas:

1. **Transparencia** – Informa al usuario que el Agente de Viajes es un agente habilitado por IA. Proporciona algunas instrucciones básicas sobre cómo empezar (por ejemplo, un mensaje de "Hola", ejemplos de solicitudes). Documenta esto claramente en la página del producto. Muestra la lista de solicitudes que el usuario ha realizado en el pasado. Haz claro cómo dar retroalimentación (pulgar arriba y abajo, botón Enviar Comentarios, etc.). Articula claramente si el agente tiene restricciones de uso o temas.
2. **Control** – Asegúrate de que sea claro cómo el usuario puede modificar el agente después de que haya sido creado con cosas como el System Prompt. Permite al usuario elegir cuán detallado es el agente, su estilo de escritura y cualquier limitación sobre lo que el agente no debería hablar. Permite al usuario ver y eliminar cualquier archivo o dato asociado, solicitudes y conversaciones pasadas.
3. **Consistencia** – Asegúrate de que los íconos para Compartir Solicitud, agregar un archivo o foto y etiquetar a alguien o algo sean estándar y reconocibles. Usa el ícono de clip para indicar carga/compartición de archivos con el agente, y un ícono de imagen para indicar carga de gráficos.

### ¿Tienes Más Preguntas sobre Patrones de Diseño de Agentes de IA?

Únete al [Discord de Azure AI Foundry](https://aka.ms/ai-agents/discord) para conectarte con otros estudiantes, asistir a horas de oficina y resolver tus dudas sobre agentes de IA.

## Recursos Adicionales

## Lección Anterior

[Explorando Marcos de Agentes](../02-explore-agentic-frameworks/README.md)

## Próxima Lección

[Patrón de Diseño de Uso de Herramientas](../04-tool-use/README.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.