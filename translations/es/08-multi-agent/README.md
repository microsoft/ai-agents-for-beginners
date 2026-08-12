[![Diseño Multi-Agente](../../../translated_images/es/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Patrones de diseño multi-agente

Tan pronto como comiences a trabajar en un proyecto que involucre múltiples agentes, necesitarás considerar el patrón de diseño multi-agente. Sin embargo, puede que no quede claro inmediatamente cuándo cambiar a multi-agentes y cuáles son las ventajas.

## Introducción

En esta lección, buscamos responder las siguientes preguntas:

- ¿Cuáles son los escenarios en los que los multi-agentes son aplicables?
- ¿Cuáles son las ventajas de usar multi-agentes en lugar de un solo agente que realiza múltiples tareas?
- ¿Cuáles son los bloques de construcción para implementar el patrón de diseño multi-agente?
- ¿Cómo tenemos visibilidad de cómo interactúan los múltiples agentes entre sí?

## Objetivos de aprendizaje

Después de esta lección, deberías ser capaz de:

- Identificar escenarios donde los multi-agentes son aplicables
- Reconocer las ventajas de usar multi-agentes sobre un solo agente.
- Comprender los bloques de construcción para implementar el patrón de diseño multi-agente.

¿Cuál es el panorama general?

*Los multi-agentes son un patrón de diseño que permite que múltiples agentes trabajen juntos para lograr un objetivo común*.

Este patrón se usa ampliamente en diversos campos, incluyendo robótica, sistemas autónomos y computación distribuida.

## Escenarios donde los multi-agentes son aplicables

Entonces, ¿qué escenarios son un buen caso para usar multi-agentes? La respuesta es que hay muchos escenarios en los que emplear múltiples agentes es beneficioso, especialmente en los siguientes casos:

- **Grandes cargas de trabajo**: Las grandes cargas de trabajo pueden dividirse en tareas más pequeñas y asignarse a diferentes agentes, permitiendo procesamiento paralelo y finalización más rápida. Un ejemplo de esto es en el caso de una gran tarea de procesamiento de datos.
- **Tareas complejas**: Las tareas complejas, como las grandes cargas, pueden dividirse en subtareas más pequeñas y asignarse a diferentes agentes, cada uno especializado en un aspecto específico de la tarea. Un buen ejemplo es en vehículos autónomos donde diferentes agentes gestionan navegación, detección de obstáculos y comunicación con otros vehículos.
- **Experiencia diversa**: Diferentes agentes pueden tener experiencia diversa, permitiéndoles manejar distintos aspectos de una tarea de manera más efectiva que un solo agente. Para este caso, un buen ejemplo es en el sector salud donde los agentes pueden gestionar diagnósticos, planes de tratamiento y monitoreo del paciente.

## Ventajas de usar multi-agentes sobre un agente singular

Un sistema de un solo agente podría funcionar bien para tareas simples, pero para tareas más complejas, usar múltiples agentes puede ofrecer varias ventajas:

- **Especialización**: Cada agente puede estar especializado en una tarea específica. La falta de especialización en un solo agente significa tener un agente que puede hacer de todo pero que podría confundirse sobre qué hacer cuando se enfrenta a una tarea compleja. Podría, por ejemplo, terminar haciendo una tarea para la que no está mejor preparado.
- **Escalabilidad**: Es más fácil escalar sistemas añadiendo más agentes en lugar de sobrecargar a un solo agente.
- **Tolerancia a fallos**: Si un agente falla, otros pueden continuar funcionando, asegurando la confiabilidad del sistema.

Tomemos un ejemplo, reservemos un viaje para un usuario. Un sistema de un solo agente tendría que manejar todos los aspectos del proceso de reserva, desde encontrar vuelos hasta reservar hoteles y autos de alquiler. Para lograr esto con un solo agente, el agente necesitaría tener herramientas para manejar todas estas tareas. Esto podría llevar a un sistema complejo y monolítico que es difícil de mantener y escalar. Un sistema multi-agente, en cambio, podría tener diferentes agentes especializados en encontrar vuelos, reservar hoteles y autos de alquiler. Esto haría que el sistema sea más modular, más fácil de mantener y escalable.

Compara esto con una agencia de viajes manejada como una tienda familiar versus una agencia de viajes manejada como una franquicia. La tienda familiar tendría un solo agente manejando todos los aspectos del proceso de reserva, mientras que la franquicia tendría diferentes agentes manejando distintos aspectos del proceso de reserva.

## Bloques de construcción para implementar el patrón de diseño multi-agente

Antes de que puedas implementar el patrón de diseño multi-agente, necesitas entender los bloques de construcción que conforman el patrón.

Hagamos esto más concreto mirando nuevamente el ejemplo de reservar un viaje para un usuario. En este caso, los bloques de construcción incluirían:

- **Comunicación entre agentes**: Los agentes para encontrar vuelos, reservar hoteles y autos de alquiler necesitan comunicarse y compartir información sobre las preferencias y restricciones del usuario. Necesitas decidir los protocolos y métodos para esta comunicación. Lo que esto significa concretamente es que el agente para encontrar vuelos necesita comunicarse con el agente para reservar hoteles para asegurar que el hotel esté reservado para las mismas fechas que el vuelo. Esto significa que los agentes necesitan compartir información sobre las fechas de viaje del usuario, por lo que necesitas decidir *qué agentes comparten información y cómo la comparten*.
- **Mecanismos de coordinación**: Los agentes necesitan coordinar sus acciones para asegurar que se cumplan las preferencias y restricciones del usuario. Una preferencia del usuario podría ser que quiere un hotel cerca del aeropuerto, mientras que una restricción podría ser que los autos de alquiler solo están disponibles en el aeropuerto. Esto significa que el agente para reservar hoteles necesita coordinar con el agente para reservar autos de alquiler para cumplir con las preferencias y restricciones del usuario. Esto significa que necesitas decidir *cómo los agentes coordinan sus acciones*.
- **Arquitectura de agentes**: Los agentes necesitan tener la estructura interna para tomar decisiones y aprender de sus interacciones con el usuario. Esto significa que el agente para encontrar vuelos necesita tener la estructura interna para decidir qué vuelos recomendar al usuario. Esto significa que necesitas decidir *cómo los agentes toman decisiones y aprenden de sus interacciones con el usuario*. Ejemplos de cómo un agente aprende y mejora podrían ser que el agente para encontrar vuelos podría usar un modelo de aprendizaje automático para recomendar vuelos al usuario basado en sus preferencias anteriores.
- **Visibilidad en interacciones multi-agente**: Necesitas tener visibilidad sobre cómo interactúan los múltiples agentes entre sí. Esto significa que necesitas herramientas y técnicas para rastrear las actividades e interacciones de los agentes. Esto podría ser en forma de herramientas de registro y monitoreo, herramientas de visualización y métricas de desempeño.
- **Patrones multi-agente**: Existen diferentes patrones para implementar sistemas multi-agente, como arquitecturas centralizadas, descentralizadas y híbridas. Necesitas decidir el patrón que mejor se adapta a tu caso de uso.
- **Humano en el ciclo**: En la mayoría de los casos, tendrás un humano en el ciclo y necesitas instruir a los agentes cuándo pedir intervención humana. Esto podría ser en forma de un usuario solicitando un hotel o vuelo específico que los agentes no han recomendado o pidiendo confirmación antes de reservar un vuelo o hotel.

## Visibilidad en las interacciones multi-agente

Es importante que tengas visibilidad sobre cómo interactúan los múltiples agentes entre sí. Esta visibilidad es esencial para depurar, optimizar y asegurar la efectividad general del sistema. Para lograr esto, necesitas herramientas y técnicas para rastrear las actividades e interacciones de los agentes. Esto podría ser en forma de herramientas de registro y monitoreo, herramientas de visualización y métricas de desempeño.

Por ejemplo, en el caso de reservar un viaje para un usuario, podrías tener un panel de control que muestre el estado de cada agente, las preferencias y restricciones del usuario y las interacciones entre agentes. Este panel podría mostrar las fechas de viaje del usuario, los vuelos recomendados por el agente de vuelos, los hoteles recomendados por el agente de hoteles y los autos de alquiler recomendados por el agente de autos de alquiler. Esto te daría una vista clara de cómo interactúan los agentes entre sí y si se están cumpliendo las preferencias y restricciones del usuario.

Veamos cada uno de estos aspectos con más detalle.

- **Herramientas de registro y monitoreo**: Quieres que se registre cada acción realizada por un agente. Una entrada de registro podría almacenar información sobre el agente que realizó la acción, la acción realizada, la hora en que se realizó y el resultado de la acción. Esta información puede usarse para depurar, optimizar y más.

- **Herramientas de visualización**: Las herramientas de visualización pueden ayudarte a ver las interacciones entre agentes de una manera más intuitiva. Por ejemplo, podrías tener un gráfico que muestre el flujo de información entre agentes. Esto podría ayudarte a identificar cuellos de botella, ineficiencias y otros problemas en el sistema.

- **Métricas de desempeño**: Las métricas de desempeño pueden ayudarte a rastrear la efectividad del sistema multi-agente. Por ejemplo, podrías medir el tiempo que tarda en completarse una tarea, la cantidad de tareas completadas por unidad de tiempo y la precisión de las recomendaciones hechas por los agentes. Esta información puede ayudarte a identificar áreas para mejorar y optimizar el sistema.

## Patrones de Multi-Agente

Vamos a profundizar en algunos patrones concretos que podemos usar para crear aplicaciones multi-agente. Aquí hay algunos patrones interesantes que vale la pena considerar:

### Chat grupal

Este patrón es útil cuando quieres crear una aplicación de chat grupal donde múltiples agentes puedan comunicarse entre sí. Casos de uso típicos para este patrón incluyen colaboración en equipo, soporte al cliente y redes sociales.

En este patrón, cada agente representa un usuario en el chat grupal, y los mensajes se intercambian entre agentes usando un protocolo de mensajería. Los agentes pueden enviar mensajes al chat grupal, recibir mensajes del chat grupal y responder a mensajes de otros agentes.

Este patrón puede implementarse usando una arquitectura centralizada donde todos los mensajes se enrutan a través de un servidor central, o una arquitectura descentralizada donde los mensajes se intercambian directamente.

![Chat grupal](../../../translated_images/es/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transferencia de tareas

Este patrón es útil cuando quieres crear una aplicación donde múltiples agentes puedan transferirse tareas entre sí.

Casos de uso típicos para este patrón incluyen soporte al cliente, gestión de tareas y automatización de flujos de trabajo.

En este patrón, cada agente representa una tarea o un paso en un flujo de trabajo, y los agentes pueden transferirse tareas a otros agentes según reglas predefinidas.

![Transferencia de tareas](../../../translated_images/es/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtrado colaborativo

Este patrón es útil cuando quieres crear una aplicación donde múltiples agentes puedan colaborar para hacer recomendaciones a los usuarios.

La razón para querer que múltiples agentes colaboren es que cada agente puede tener experiencia diferente y contribuir al proceso de recomendación de distintas maneras.

Tomemos un ejemplo donde un usuario quiere una recomendación sobre la mejor acción para comprar en el mercado de valores.

- **Experto en la industria**: Un agente podría ser un experto en una industria específica.
- **Análisis técnico**: Otro agente podría ser un experto en análisis técnico.
- **Análisis fundamental**: y otro agente podría ser un experto en análisis fundamental. Colaborando, estos agentes pueden proporcionar una recomendación más completa al usuario.

![Recomendación](../../../translated_images/es/multi-agent-filtering.d959cb129dc9f608.webp)

## Escenario: proceso de reembolso

Considera un escenario donde un cliente está tratando de obtener un reembolso por un producto, pueden involucrarse bastantes agentes en este proceso, pero dividámoslo entre agentes específicos para este proceso y agentes generales que pueden usarse en otros procesos.

**Agentes específicos para el proceso de reembolso**:

A continuación algunos agentes que podrían estar involucrados en el proceso de reembolso:

- **Agente del cliente**: Este agente representa al cliente y es responsable de iniciar el proceso de reembolso.
- **Agente del vendedor**: Este agente representa al vendedor y es responsable de procesar el reembolso.
- **Agente de pago**: Este agente representa el proceso de pago y es responsable de reembolsar el pago al cliente.
- **Agente de resolución**: Este agente representa el proceso de resolución y es responsable de resolver cualquier problema que surja durante el proceso de reembolso.
- **Agente de cumplimiento**: Este agente representa el proceso de cumplimiento y es responsable de asegurar que el proceso de reembolso cumpla con regulaciones y políticas.

**Agentes generales**:

Estos agentes pueden ser usados por otras partes de tu negocio.

- **Agente de envío**: Este agente representa el proceso de envío y es responsable de enviar el producto de vuelta al vendedor. Este agente puede usarse tanto para el proceso de reembolso como para el envío general de un producto vía una compra, por ejemplo.
- **Agente de retroalimentación**: Este agente representa el proceso de retroalimentación y es responsable de recopilar comentarios del cliente. La retroalimentación podría darse en cualquier momento y no solo durante el proceso de reembolso.
- **Agente de escalación**: Este agente representa el proceso de escalación y es responsable de escalar problemas a un nivel más alto de soporte. Puedes usar este tipo de agente para cualquier proceso donde necesites escalar un problema.
- **Agente de notificaciones**: Este agente representa el proceso de notificaciones y es responsable de enviar notificaciones al cliente en varias etapas del proceso de reembolso.
- **Agente de análisis**: Este agente representa el proceso de análisis y es responsable de analizar datos relacionados con el proceso de reembolso.
- **Agente de auditoría**: Este agente representa el proceso de auditoría y es responsable de auditar el proceso de reembolso para asegurar que se lleve a cabo correctamente.
- **Agente de reportes**: Este agente representa el proceso de reportes y es responsable de generar informes sobre el proceso de reembolso.
- **Agente de conocimiento**: Este agente representa el proceso de conocimiento y es responsable de mantener una base de conocimientos con información relacionada con el proceso de reembolso. Este agente podría tener conocimiento tanto de reembolsos como de otras partes de tu negocio.
- **Agente de seguridad**: Este agente representa el proceso de seguridad y es responsable de asegurar la seguridad del proceso de reembolso.
- **Agente de calidad**: Este agente representa el proceso de calidad y es responsable de asegurar la calidad del proceso de reembolso.

Hay bastantes agentes listados anteriormente, tanto para el proceso específico de reembolso como para los agentes generales que pueden usarse en otras partes de tu negocio. Esperamos que esto te dé una idea de cómo puedes decidir qué agentes usar en tu sistema multi-agente.

## Tarea

Diseña un sistema multi-agente para un proceso de soporte al cliente. Identifica los agentes involucrados en el proceso, sus roles y responsabilidades, y cómo interactúan entre sí. Considera tanto agentes específicos para el proceso de soporte al cliente como agentes generales que pueden ser usados en otras partes de tu negocio.


> Piensa un momento antes de leer la siguiente solución, puede que necesites más agentes de los que crees.

> CONSEJO: Piensa en las diferentes etapas del proceso de soporte al cliente y también considera los agentes necesarios para cualquier sistema.

## Solución

[Solución](./solution/solution.md)

## Comprobaciones de conocimiento

### Pregunta 1

¿Cuál escenario es el más adecuado para un sistema multiagente?

- [ ] A1: Un bot de soporte responde preguntas comunes usando una base de conocimiento y un pequeño conjunto de herramientas.
- [ ] A2: Un flujo de trabajo de reembolso necesita roles separados para fraude, pagos y cumplimiento, cada uno con sus propias herramientas, y sus resultados deben ser coordinados.
- [ ] A3: La misma solicitud simple de clasificación llega miles de veces por hora.

### Pregunta 2

¿Cuándo suele ser mejor opción un solo agente?

- [ ] A1: La tarea puede manejarse con un conjunto de instrucciones y herramientas, sin transferencias a especialistas.
- [ ] A2: El agente tiene acceso a más de una herramienta.
- [ ] A3: El flujo de trabajo requiere roles separados con diferentes permisos y auditorías independientes.

[Solución del cuestionario](./solution/solution-quiz.md)

## Resumen

En esta lección, hemos explorado el patrón de diseño multiagente, incluyendo los escenarios donde los multiagentes son aplicables, las ventajas de usar multiagentes sobre un agente singular, los componentes clave para implementar el patrón de diseño multiagente, y cómo tener visibilidad sobre cómo los múltiples agentes interactúan entre sí.

### ¿Tienes más preguntas sobre el patrón de diseño multiagente?

Únete a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros estudiantes, asistir a horas de oficina y resolver tus preguntas sobre agentes de IA.

## Recursos adicionales

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentación del Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Patrones de diseño agenticos</a>


## Lección anterior

[Diseño de planificación](../07-planning-design/README.md)

## Próxima lección

[Metacognición en agentes de IA](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->