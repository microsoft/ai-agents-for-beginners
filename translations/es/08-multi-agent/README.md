[![Multi-agente Diseño](../../../translated_images/es/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Haz clic en la imagen arriba para ver el video de esta lección)_

# Patrones de diseño multi-agente

Tan pronto como comiences a trabajar en un proyecto que involucra múltiples agentes, necesitarás considerar el patrón de diseño multi-agente. Sin embargo, podría no estar inmediatamente claro cuándo cambiar a multi-agentes y cuáles son las ventajas.

## Introducción

En esta lección, buscamos responder las siguientes preguntas:

- ¿Cuáles son los escenarios donde los multi-agentes son aplicables?
- ¿Cuáles son las ventajas de usar multi-agentes en lugar de un único agente que realiza múltiples tareas?
- ¿Cuáles son los bloques de construcción para implementar el patrón de diseño multi-agente?
- ¿Cómo tenemos visibilidad sobre cómo los múltiples agentes interactúan entre sí?

## Objetivos de aprendizaje

Después de esta lección, deberías ser capaz de:

- Identificar escenarios donde los multi-agentes son aplicables
- Reconocer las ventajas de usar multi-agentes sobre un agente singular.
- Comprender los bloques de construcción para implementar el patrón de diseño multi-agente.

¿Cuál es la imagen más amplia?

*Los multi-agentes son un patrón de diseño que permite que múltiples agentes trabajen juntos para lograr un objetivo común*.

Este patrón se usa ampliamente en varios campos, incluyendo robótica, sistemas autónomos y computación distribuida.

## Escenarios donde los multi-agentes son aplicables

Entonces, ¿qué escenarios son un buen caso de uso para emplear multi-agentes? La respuesta es que hay muchos escenarios donde emplear múltiples agentes es beneficioso, especialmente en los siguientes casos:

- **Grandes cargas de trabajo**: Las grandes cargas de trabajo pueden dividirse en tareas más pequeñas y asignarse a diferentes agentes, permitiendo el procesamiento en paralelo y una finalización más rápida. Un ejemplo de esto es en el caso de una tarea de procesamiento de datos grande.
- **Tareas complejas**: Las tareas complejas, como las grandes cargas de trabajo, pueden dividirse en subtareas más pequeñas y asignarse a diferentes agentes, cada uno especializado en un aspecto específico de la tarea. Un buen ejemplo de esto es en vehículos autónomos donde diferentes agentes manejan navegación, detección de obstáculos y comunicación con otros vehículos.
- **Diversidad de experiencia**: Diferentes agentes pueden tener diversa experiencia, permitiéndoles manejar distintos aspectos de una tarea de manera más efectiva que un solo agente. Para este caso, un buen ejemplo es en el sector salud donde los agentes pueden gestionar diagnósticos, planes de tratamiento y monitoreo del paciente.

## Ventajas de usar multi-agentes sobre un agente singular

Un sistema con un solo agente podría funcionar bien para tareas simples, pero para tareas más complejas, usar múltiples agentes puede proporcionar varias ventajas:

- **Especialización**: Cada agente puede estar especializado en una tarea específica. La falta de especialización en un agente único significa que tienes un agente que puede hacer todo pero que podría confundirse sobre qué hacer cuando enfrenta una tarea compleja. Podría, por ejemplo, terminar haciendo una tarea para la que no está mejor capacitado.
- **Escalabilidad**: Es más fácil escalar sistemas agregando más agentes en lugar de sobrecargar un único agente.
- **Tolerancia a fallos**: Si un agente falla, los demás pueden continuar funcionando, asegurando la fiabilidad del sistema.

Tomemos un ejemplo, reservemos un viaje para un usuario. Un sistema con un solo agente tendría que manejar todos los aspectos del proceso de reserva del viaje, desde encontrar vuelos, hasta reservar hoteles y autos de alquiler. Para lograr esto con un solo agente, el agente necesitaría tener herramientas para manejar todas estas tareas. Esto podría llevar a un sistema complejo y monolítico que es difícil de mantener y escalar. Un sistema multi-agente, por otro lado, podría tener diferentes agentes especializados en encontrar vuelos, reservar hoteles y autos de alquiler. Esto haría que el sistema sea más modular, más fácil de mantener y escalable.

Compáralo con una agencia de viajes administrada como una tienda familiar versus una agencia de viajes operada como una franquicia. La tienda familiar tendría un solo agente manejando todos los aspectos del proceso de reserva del viaje, mientras que la franquicia tendría diferentes agentes manejando diferentes aspectos del proceso.

## Bloques de construcción para implementar el patrón de diseño multi-agente

Antes de que puedas implementar el patrón de diseño multi-agente, necesitas entender los bloques de construcción que conforman el patrón.

Hagamos esto más concreto volviendo al ejemplo de reservar un viaje para un usuario. En este caso, los bloques de construcción incluirían:

- **Comunicación entre agentes**: Los agentes para encontrar vuelos, reservar hoteles y autos de alquiler necesitan comunicarse y compartir información sobre las preferencias y restricciones del usuario. Necesitas decidir los protocolos y métodos para esta comunicación. Lo que significa concretamente que el agente que encuentra vuelos necesita comunicarse con el agente que reserva hoteles para asegurar que el hotel sea reservado para las mismas fechas que el vuelo. Eso significa que los agentes necesitan compartir información sobre las fechas de viaje del usuario, lo que implica que necesitas decidir *qué agentes están compartiendo información y cómo la están compartiendo*.
- **Mecanismos de coordinación**: Los agentes necesitan coordinar sus acciones para asegurar que se cumplan las preferencias y restricciones del usuario. Una preferencia del usuario podría ser que quiere un hotel cerca del aeropuerto mientras que una restricción podría ser que los autos de alquiler solo están disponibles en el aeropuerto. Esto significa que el agente que reserva hoteles necesita coordinarse con el agente que reserva autos para asegurar que se cumplan las preferencias y restricciones del usuario. Esto significa que necesitas decidir *cómo los agentes están coordinando sus acciones*.
- **Arquitectura del agente**: Los agentes necesitan tener la estructura interna para tomar decisiones y aprender de sus interacciones con el usuario. Esto significa que el agente que encuentra vuelos necesita tener la estructura interna para decidir qué vuelos recomendar al usuario. Esto significa que necesitas decidir *cómo los agentes están tomando decisiones y aprendiendo de sus interacciones con el usuario*. Ejemplos de cómo un agente aprende y mejora podrían ser que el agente que encuentra vuelos podría usar un modelo de aprendizaje automático para recomendar vuelos al usuario basado en sus preferencias anteriores.
- **Visibilidad en las interacciones multi-agente**: Necesitas tener visibilidad sobre cómo los múltiples agentes están interactuando entre sí. Esto significa que necesitas herramientas y técnicas para rastrear las actividades e interacciones de los agentes. Esto podría ser en forma de herramientas de registro y monitoreo, herramientas de visualización y métricas de rendimiento.
- **Patrones multi-agente**: Hay diferentes patrones para implementar sistemas multi-agente, como arquitecturas centralizadas, descentralizadas e híbridas. Necesitas decidir el patrón que mejor se ajuste a tu caso de uso.
- **Humano en el bucle**: En la mayoría de los casos, habrá un humano en el bucle y necesitas instruir a los agentes cuándo solicitar intervención humana. Esto podría ser en forma de un usuario pidiendo un hotel o vuelo específico que los agentes no han recomendado o pidiendo confirmación antes de reservar un vuelo o un hotel.

## Visibilidad en las interacciones multi-agente

Es importante que tengas visibilidad sobre cómo los múltiples agentes interactúan entre sí. Esta visibilidad es esencial para depurar, optimizar y asegurar la efectividad general del sistema. Para lograr esto, necesitas herramientas y técnicas para rastrear las actividades e interacciones de los agentes. Esto podría ser en forma de herramientas de registro y monitoreo, herramientas de visualización y métricas de rendimiento.

Por ejemplo, en el caso de reservar un viaje para un usuario, podrías tener un tablero que muestre el estado de cada agente, las preferencias y restricciones del usuario, y las interacciones entre los agentes. Este tablero podría mostrar las fechas de viaje del usuario, los vuelos recomendados por el agente de vuelos, los hoteles recomendados por el agente de hoteles y los autos de alquiler recomendados por el agente de autos. Esto te daría una vista clara de cómo los agentes están interactuando entre sí y si se están cumpliendo las preferencias y restricciones del usuario.

Veamos cada uno de estos aspectos con más detalle.

- **Herramientas de registro y monitoreo**: Quieres que se registre cada acción tomada por un agente. Una entrada de registro podría almacenar información sobre el agente que tomó la acción, la acción que se tomó, la hora en que se tomó y el resultado. Esta información puede usarse para depurar, optimizar y más.

- **Herramientas de visualización**: Las herramientas de visualización pueden ayudarte a ver las interacciones entre agentes de manera más intuitiva. Por ejemplo, podrías tener un gráfico que muestre el flujo de información entre agentes. Esto podría ayudarte a identificar cuellos de botella, ineficiencias y otros problemas en el sistema.

- **Métricas de rendimiento**: Las métricas de rendimiento pueden ayudarte a rastrear la efectividad del sistema multi-agente. Por ejemplo, podrías medir el tiempo que toma completar una tarea, el número de tareas completadas por unidad de tiempo y la precisión de las recomendaciones hechas por los agentes. Esta información puede ayudarte a identificar áreas de mejora y optimizar el sistema.

## Patrones multi-agente

Vamos a profundizar en algunos patrones concretos que podemos usar para crear aplicaciones multi-agente. Aquí hay algunos patrones interesantes que vale la pena considerar:

### Chat grupal

Este patrón es útil cuando quieres crear una aplicación de chat grupal donde múltiples agentes puedan comunicarse entre sí. Los casos de uso típicos para este patrón incluyen la colaboración en equipo, soporte al cliente y redes sociales.

En este patrón, cada agente representa a un usuario en el chat grupal, y los mensajes se intercambian entre agentes usando un protocolo de mensajería. Los agentes pueden enviar mensajes al chat grupal, recibir mensajes del chat grupal y responder a mensajes de otros agentes.

Este patrón puede implementarse usando una arquitectura centralizada donde todos los mensajes se enrutan a través de un servidor central, o una arquitectura descentralizada donde los mensajes se intercambian directamente.

![Chat grupal](../../../translated_images/es/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transferencia

Este patrón es útil cuando quieres crear una aplicación donde múltiples agentes puedan transferir tareas entre sí.

Los casos de uso típicos para este patrón incluyen soporte al cliente, gestión de tareas y automatización de flujos de trabajo.

En este patrón, cada agente representa una tarea o un paso en un flujo de trabajo, y los agentes pueden transferir tareas a otros agentes basándose en reglas predefinidas.

![Transferencia](../../../translated_images/es/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtrado colaborativo

Este patrón es útil cuando quieres crear una aplicación donde múltiples agentes puedan colaborar para hacer recomendaciones a los usuarios.

La razón para querer que múltiples agentes colaboren es que cada agente puede tener diferentes áreas de especialización y puede contribuir al proceso de recomendación de formas diversas.

Tomemos un ejemplo donde un usuario quiere una recomendación sobre la mejor acción para comprar en el mercado bursátil.

- **Experto en la industria**: Un agente podría ser un experto en una industria específica.
- **Análisis técnico**: Otro agente podría ser un experto en análisis técnico.
- **Análisis fundamental**: Y otro agente podría ser un experto en análisis fundamental. Al colaborar, estos agentes pueden proporcionar una recomendación más integral al usuario.

![Recomendación](../../../translated_images/es/multi-agent-filtering.d959cb129dc9f608.webp)

## Escenario: proceso de reembolso

Considera un escenario donde un cliente intenta obtener un reembolso por un producto, puede haber varios agentes involucrados en este proceso, pero dividámoslos entre agentes específicos para este proceso y agentes generales que pueden ser usados en otros procesos.

**Agentes específicos para el proceso de reembolso**:

Los siguientes son algunos agentes que podrían estar involucrados en el proceso de reembolso:

- **Agente del cliente**: Este agente representa al cliente y es responsable de iniciar el proceso de reembolso.
- **Agente del vendedor**: Este agente representa al vendedor y es responsable de procesar el reembolso.
- **Agente de pago**: Este agente representa el proceso de pago y es responsable de reembolsar el pago del cliente.
- **Agente de resolución**: Este agente representa el proceso de resolución y es responsable de resolver cualquier problema que surja durante el proceso de reembolso.
- **Agente de cumplimiento**: Este agente representa el proceso de cumplimiento y es responsable de asegurar que el proceso de reembolso cumpla con regulaciones y políticas.

**Agentes generales**:

Estos agentes pueden ser usados por otras partes de tu negocio.

- **Agente de envíos**: Este agente representa el proceso de envío y es responsable de enviar el producto de vuelta al vendedor. Este agente puede usarse tanto para el proceso de reembolso como para envíos generales de un producto, por ejemplo, por una compra.
- **Agente de retroalimentación**: Este agente representa el proceso de retroalimentación y es responsable de recopilar comentarios del cliente. La retroalimentación podría recibirse en cualquier momento, no solo durante el proceso de reembolso.
- **Agente de escalamiento**: Este agente representa el proceso de escalamiento y es responsable de escalar problemas a un nivel superior de soporte. Puedes usar este tipo de agente para cualquier proceso donde necesites escalar un problema.
- **Agente de notificaciones**: Este agente representa el proceso de notificación y es responsable de enviar notificaciones al cliente en varias etapas del proceso de reembolso.
- **Agente de análisis**: Este agente representa el proceso de análisis y es responsable de analizar datos relacionados con el proceso de reembolso.
- **Agente de auditoría**: Este agente representa el proceso de auditoría y es responsable de auditar el proceso de reembolso para asegurar que se esté llevando a cabo correctamente.
- **Agente de reportes**: Este agente representa el proceso de reportes y es responsable de generar informes sobre el proceso de reembolso.
- **Agente de conocimiento**: Este agente representa el proceso de conocimiento y es responsable de mantener una base de conocimientos relacionada con el proceso de reembolso. Este agente podría tener conocimiento tanto sobre reembolsos como sobre otras partes de tu negocio.
- **Agente de seguridad**: Este agente representa el proceso de seguridad y es responsable de asegurar la seguridad del proceso de reembolso.
- **Agente de calidad**: Este agente representa el proceso de calidad y es responsable de asegurar la calidad del proceso de reembolso.

Hay bastantes agentes listados anteriormente, tanto para el proceso específico de reembolso como para los agentes generales que pueden usarse en otras partes de tu negocio. Esperamos que esto te dé una idea de cómo puedes decidir qué agentes usar en tu sistema multi-agente.

## Tarea

Diseña un sistema multi-agente para un proceso de atención al cliente. Identifica los agentes involucrados en el proceso, sus roles y responsabilidades, y cómo interactúan entre sí. Considera tanto agentes específicos para el proceso de atención al cliente como agentes generales que pueden usarse en otras partes de tu negocio.
> Piensa un momento antes de leer la siguiente solución, es posible que necesites más agentes de los que crees.

> TIP: Piensa en las diferentes etapas del proceso de soporte al cliente y también considera los agentes necesarios para cualquier sistema.

## Solución

[Solution](./solution/solution.md)

## Evaluaciones de conocimiento

Pregunta: ¿Cuándo deberías considerar usar múltiples agentes?

- [ ] A1: Cuando tienes una pequeña carga de trabajo y una tarea simple.
- [ ] A2: Cuando tienes una carga de trabajo grande.
- [ ] A3: Cuando tienes una tarea simple.

[Solution quiz](./solution/solution-quiz.md)

## Resumen

En esta lección, hemos analizado el patrón de diseño multi-agente, incluyendo los escenarios donde son aplicables los multi-agentes, las ventajas de usar múltiples agentes en lugar de un agente singular, los elementos fundamentales para implementar el patrón de diseño multi-agente y cómo tener visibilidad sobre cómo interactúan entre sí los múltiples agentes.

### ¿Tienes más preguntas sobre el patrón de diseño multi-agente?

Únete al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conocer a otros aprendices, asistir a horas de oficina y resolver tus dudas sobre Agentes de IA.

## Recursos adicionales

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentación del Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Patrones de diseño agentico</a>

## Lección anterior

[Planning Design](../07-planning-design/README.md)

## Próxima lección

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->