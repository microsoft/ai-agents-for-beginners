[![Cómo diseñar buenos agentes de IA](../../../translated_images/es/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_
# Principios de Diseño de Agentes de IA

## Introducción

Hay muchas maneras de pensar en la construcción de sistemas de agentes de IA. Dado que la ambigüedad es una característica y no un error en el diseño de la IA generativa, a veces resulta difícil para los ingenieros saber por dónde empezar. Hemos creado un conjunto de Principios de Diseño centrados en la experiencia del usuario para que los desarrolladores puedan construir sistemas de agentes centrados en el cliente y satisfacer sus necesidades empresariales. Estos principios de diseño no son una arquitectura prescriptiva, sino más bien un punto de partida para los equipos que están definiendo y construyendo experiencias de agentes.

En general, los agentes deberían:

- Ampliar y escalar las capacidades humanas (lluvia de ideas, resolución de problemas, automatización, etc.)
- Cubrir las lagunas de conocimiento (ponernos al día en dominios de conocimiento, traducción, etc.)
- Facilitar y apoyar la colaboración de la manera en que preferimos trabajar con otros como individuos
- Hacernos mejores versiones de nosotros mismos (por ejemplo, coach de vida/jefe de tareas, ayudándonos a aprender habilidades de regulación emocional y atención plena, construyendo resiliencia, etc.)

## Esta lección cubrirá

- Qué son los Principios de Diseño de Agentes
- Algunas pautas para seguir al implementar estos principios de diseño
- Algunos ejemplos de uso de los principios de diseño

## Objetivos de aprendizaje

Después de completar esta lección, podrás:

1. Explicar qué son los Principios de Diseño de Agentes
2. Explicar las pautas para usar los Principios de Diseño de Agentes
3. Entender cómo construir un agente usando los Principios de Diseño de Agentes

## Los Principios de Diseño de Agentes

![Principios de Diseño de Agentes](../../../translated_images/es/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agente (Espacio)

Este es el entorno en el que opera el agente. Estos principios informan cómo diseñamos agentes para interactuar en mundos físicos y digitales.

- **Conectar, no colapsar** – ayudar a conectar personas con otras personas, eventos y conocimientos accionables para facilitar la colaboración y la conexión.
- Los agentes ayudan a conectar eventos, conocimientos y personas.
- Los agentes acercan a las personas. No están diseñados para reemplazar o menospreciar a las personas.
- **Fácilmente accesible pero ocasionalmente invisible** – el agente opera mayormente en segundo plano y solo nos impulsa cuando es relevante y apropiado.
  - El agente es fácilmente descubrible y accesible para usuarios autorizados en cualquier dispositivo o plataforma.
  - El agente soporta entradas y salidas multimodales (sonido, voz, texto, etc.).
  - El agente puede transitar sin problemas entre primer plano y fondo; entre ser proactivo y reactivo, según su percepción de las necesidades del usuario.
  - El agente puede operar de manera invisible, pero su proceso en segundo plano y colaboración con otros agentes es transparente y controlable por el usuario.

### Agente (Tiempo)

Así es como el agente opera a través del tiempo. Estos principios informan cómo diseñamos agentes que interactúan a través del pasado, presente y futuro.

- **Pasado**: Reflexionando sobre la historia que incluye tanto estado como contexto.
  - El agente proporciona resultados más relevantes basados en el análisis de datos históricos más ricos más allá solo del evento, personas o estados.
  - El agente crea conexiones a partir de eventos pasados y reflexiona activamente en la memoria para relacionarse con situaciones actuales.
- **Ahora**: Impulsar más que solo notificar.
  - El agente incorpora un enfoque comprensivo para interactuar con personas. Cuando ocurre un evento, el agente va más allá de una notificación estática u otra formalidad estática. El agente puede simplificar flujos o generar dinámicamente señales para dirigir la atención del usuario en el momento adecuado.
  - El agente entrega información basada en el entorno contextual, cambios sociales y culturales y adaptada a la intención del usuario.
  - La interacción con el agente puede ser gradual, evolucionando/creciendo en complejidad para empoderar a los usuarios a largo plazo.
- **Futuro**: Adaptando y evolucionando.
  - El agente se adapta a diversos dispositivos, plataformas y modalidades.
  - El agente se adapta al comportamiento del usuario, necesidades de accesibilidad, y es libremente personalizable.
  - El agente se moldea y evoluciona a través de la interacción continua con el usuario.

### Agente (Núcleo)

Estos son los elementos clave en el núcleo del diseño de un agente.

- **Aceptar la incertidumbre pero establecer confianza**.
  - Se espera un cierto nivel de incertidumbre en el agente. La incertidumbre es un elemento clave en el diseño del agente.
  - La confianza y transparencia son capas fundamentales del diseño del agente.
  - Los humanos controlan cuándo el agente está encendido o apagado y el estado del agente es claramente visible en todo momento.

## Las Pautas para Implementar Estos Principios

Cuando uses los principios de diseño anteriores, sigue las siguientes pautas:

1. **Transparencia**: Informar al usuario que se emplea IA, cómo funciona (incluidas acciones pasadas) y cómo dar retroalimentación y modificar el sistema.
2. **Control**: Permitir al usuario personalizar, especificar preferencias y personalizar, y tener control sobre el sistema y sus atributos (incluida la capacidad de olvidar).
3. **Consistencia**: Buscar experiencias consistentes y multimodales en dispositivos y terminales. Usar elementos de UI/UX familiares donde sea posible (p. ej., ícono de micrófono para interacción por voz) y reducir la carga cognitiva del cliente tanto como sea posible (p. ej., respuestas concisas, ayudas visuales y contenido de ‘Aprender más’).

## Cómo Diseñar un Agente de Viajes usando Estos Principios y Pautas

Imagina que estás diseñando un agente de viajes, aquí te mostramos cómo podrías pensar en usar los Principios y Pautas de Diseño:

1. **Transparencia** – Haz saber al usuario que el agente de viajes es un agente habilitado con IA. Proporciona algunas instrucciones básicas para comenzar (p. ej., un mensaje de "Hola", ejemplos de comandos). Documenta esto claramente en la página del producto. Muestra la lista de comandos que el usuario ha preguntado en el pasado. Explica claramente cómo dar retroalimentación (pulgar arriba y abajo, botón de enviar retroalimentación, etc.). Articula claramente si el agente tiene restricciones de uso o de temas.
2. **Control** – Asegúrate de que esté claro cómo el usuario puede modificar el agente después de haber sido creado, con cosas como el Prompt del Sistema. Permite que el usuario elija cuán prolijo es el agente, su estilo de escritura y cualquier advertencia sobre lo que el agente no debe comentar. Permite al usuario ver y eliminar archivos o datos asociados, comandos y conversaciones pasadas.
3. **Consistencia** – Asegúrate de que los íconos para compartir comando, añadir un archivo o foto y etiquetar a alguien o algo sean estándar y reconocibles. Usa el ícono de clip para indicar carga/compartir archivos con el agente, y un ícono de imagen para indicar subida de gráficos.

## Códigos de ejemplo

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## ¿Tienes más preguntas sobre los patrones de diseño de agentes de IA?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros estudiantes, asistir a horas de oficina y obtener respuestas a tus preguntas sobre agentes de IA.

## Recursos adicionales

- <a href="https://openai.com" target="_blank">Prácticas para Gobernar Sistemas de IA Agéntica | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">El Proyecto HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Caja de Herramientas de IA Responsable</a>

## Lección anterior

[Explorando Frameworks Agénticos](../02-explore-agentic-frameworks/README.md)

## Próxima lección

[Patrón de Diseño de Uso de Herramientas](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->