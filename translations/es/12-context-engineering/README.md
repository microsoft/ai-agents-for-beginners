# Ingeniería de Contexto para Agentes de IA

[![Ingeniería de Contexto](../../../translated_images/es/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

Entender la complejidad de la aplicación para la que estás construyendo un agente de IA es importante para crear uno confiable. Necesitamos construir agentes de IA que gestionen la información de manera efectiva para abordar necesidades complejas más allá de la ingeniería de prompts.

En esta lección, veremos qué es la ingeniería de contexto y su papel en la construcción de agentes de IA.

## Introducción

Esta lección cubrirá:

• **Qué es la Ingeniería de Contexto** y por qué es diferente de la ingeniería de prompts.

• **Estrategias para una Ingeniería de Contexto efectiva**, incluyendo cómo escribir, seleccionar, comprimir y aislar la información.

• **Fallos comunes de contexto** que pueden descarrilar tu agente de IA y cómo solucionarlos.

## Objetivos de Aprendizaje

Al completar esta lección, entenderás cómo:

• **Definir la ingeniería de contexto** y diferenciarla de la ingeniería de prompts.

• **Identificar los componentes clave del contexto** en aplicaciones de Modelos de Lenguaje Grandes (LLM).

• **Aplicar estrategias para escribir, seleccionar, comprimir y aislar contexto** para mejorar el rendimiento del agente.

• **Reconocer fallos comunes de contexto** como envenenamiento, distracción, confusión y choque, e implementar técnicas de mitigación.

## ¿Qué es la Ingeniería de Contexto?

Para los agentes de IA, el contexto es lo que impulsa la planificación de un agente de IA para tomar ciertas acciones. La Ingeniería de Contexto es la práctica de asegurarse de que el agente de IA tenga la información correcta para completar el siguiente paso de la tarea. La ventana de contexto es limitada en tamaño, por lo que como constructores de agentes necesitamos crear sistemas y procesos para gestionar la adición, eliminación y condensación de la información en la ventana de contexto.

### Ingeniería de Prompts vs Ingeniería de Contexto

La ingeniería de prompts se centra en un conjunto único de instrucciones estáticas para guiar eficazmente a los agentes de IA con un conjunto de reglas. La ingeniería de contexto trata de cómo manejar un conjunto dinámico de información, incluyendo el prompt inicial, para asegurar que el agente de IA disponga de lo que necesita a lo largo del tiempo. La idea principal de la ingeniería de contexto es hacer que este proceso sea repetible y confiable.

### Tipos de Contexto

[![Tipos de Contexto](../../../translated_images/es/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Es importante recordar que el contexto no es solo una cosa. La información que el agente de IA necesita puede provenir de una variedad de fuentes y nos corresponde a nosotros asegurar que el agente tenga acceso a estas fuentes:

Los tipos de contexto que un agente de IA podría necesitar gestionar incluyen:

• **Instrucciones:** Son como las "reglas" del agente: prompts, mensajes del sistema, ejemplos few-shot (mostrando a la IA cómo hacer algo) y descripciones de herramientas que puede usar. Aquí es donde se combina el enfoque de la ingeniería de prompts con la ingeniería de contexto.

• **Conocimiento:** Cubre hechos, información recuperada de bases de datos o memorias a largo plazo que el agente ha acumulado. Esto incluye integrar un sistema de Generación Aumentada por Recuperación (RAG) si un agente necesita acceso a diferentes almacenes de conocimiento y bases de datos.

• **Herramientas:** Son las definiciones de funciones externas, APIs y servidores MCP que el agente puede llamar, junto con el feedback (resultados) que recibe al usarlas.

• **Historial de Conversación:** El diálogo en curso con un usuario. Con el tiempo, estas conversaciones se vuelven más largas y complejas, lo que significa que ocupan espacio en la ventana de contexto.

• **Preferencias del Usuario:** Información aprendida sobre los gustos o disgustos del usuario a lo largo del tiempo. Estos podrían ser almacenados y llamados al tomar decisiones clave para ayudar al usuario.

## Estrategias para una Ingeniería de Contexto Efectiva

### Estrategias de Planificación

[![Mejores Prácticas de Ingeniería de Contexto](../../../translated_images/es/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Una buena ingeniería de contexto comienza con una buena planificación. Aquí hay un enfoque que te ayudará a empezar a pensar en cómo aplicar el concepto de ingeniería de contexto:

1. **Definir Resultados Claros** - Los resultados de las tareas que se asignarán a los agentes de IA deben estar claramente definidos. Responde a la pregunta: "¿Cómo se verá el mundo cuando el agente de IA termine su tarea?" En otras palabras, qué cambio, información o respuesta debería tener el usuario después de interactuar con el agente de IA.
2. **Mapear el Contexto** - Una vez que has definido los resultados del agente de IA, necesitas responder a la pregunta "¿Qué información necesita el agente de IA para completar esta tarea?". Así podrás empezar a mapear el contexto de dónde se puede localizar esa información.
3. **Crear Pipelines de Contexto** - Ahora que sabes dónde está la información, necesitas responder a la pregunta "¿Cómo obtendrá esta información el agente?". Esto se puede hacer de varias maneras, incluyendo RAG, uso de servidores MCP y otras herramientas.

### Estrategias Prácticas

La planificación es importante, pero una vez que la información comienza a fluir en la ventana de contexto de nuestro agente, necesitamos tener estrategias prácticas para gestionarla:

#### Gestión del Contexto

Aunque parte de la información se añadirá automáticamente a la ventana de contexto, la ingeniería de contexto trata de tomar un papel más activo con esta información, lo cual se puede hacer con algunas estrategias:

 1. **Bloc de Notas del Agente**
 Esto permite que un agente de IA tome notas de información relevante sobre las tareas actuales y las interacciones con el usuario durante una sola sesión. Esto debería existir fuera de la ventana de contexto en un archivo u objeto en tiempo de ejecución que el agente pueda recuperar posteriormente durante esta sesión si es necesario.

 2. **Memorias**
 Los blocs de notas son buenos para gestionar información fuera de la ventana de contexto de una sola sesión. Las memorias permiten a los agentes almacenar y recuperar información relevante a través de múltiples sesiones. Esto podría incluir resúmenes, preferencias del usuario y retroalimentación para mejoras en el futuro.

 3. **Comprimir Contexto**
  Cuando la ventana de contexto crece y está cerca de su límite, se pueden usar técnicas como resumen y recorte. Esto incluye mantener sólo la información más relevante o eliminar mensajes más antiguos.
  
 4. **Sistemas Multiagente**
  Desarrollar sistemas multiagente es una forma de ingeniería de contexto porque cada agente tiene su propia ventana de contexto. Cómo se comparte y pasa ese contexto a diferentes agentes es otra cosa que planificar cuando se construyen estos sistemas.
  
 5. **Entornos Sandbox**
  Si un agente necesita ejecutar código o procesar grandes cantidades de información en un documento, esto puede requerir un gran número de tokens para procesar los resultados. En lugar de almacenar todo esto en la ventana de contexto, el agente puede usar un entorno sandbox que pueda ejecutar ese código y sólo leer los resultados y otra información relevante.
  
 6. **Objetos de Estado en Tiempo de Ejecución**
   Esto se realiza creando contenedores de información para gestionar situaciones cuando el agente necesita acceder a cierta información. Para una tarea compleja, esto permitiría que un agente almacene los resultados de cada subtarea paso a paso, permitiendo que el contexto permanezca conectado sólo a esa subtarea específica.

#### Inspección del Contexto

Después de aplicar una de estas estrategias, vale la pena revisar qué recibió realmente la siguiente llamada al modelo. Una pregunta útil de depuración es:

> ¿El agente cargó demasiado contexto, el contexto incorrecto o le faltó el contexto que necesitaba?

No necesitas registrar prompts en bruto, resultados de herramientas o contenidos de memoria para responder esa pregunta. En producción, prefiere registros pequeños de inspección de contexto que capturen conteos, IDs, hashes y etiquetas de política:

- **Selección:** Rastrea cuántos fragmentos candidatos, herramientas o memorias se consideraron, cuántos se seleccionaron y qué regla o puntuación causó que los otros fueran filtrados.
- **Compresión:** Registra el rango de origen o ID de traza, el ID del resumen, un conteo estimado de tokens antes y después de la compresión, y si el contenido en bruto fue excluido de la siguiente llamada.
- **Aislamiento:** Nota qué subtarea se ejecutó en un agente, sesión o sandbox separado, qué resumen acotado se devolvió, y si una gran salida de herramienta permaneció fuera del contexto del agente principal.
- **Memoria y RAG:** Almacena IDs de documentos de recuperación, IDs de memoria, puntuaciones, IDs seleccionados y estado de redacción en lugar de texto recuperado completo.
- **Seguridad y privacidad:** Prefiere hashes, IDs, cubos de tokens y etiquetas de política sobre texto sensible del prompt, argumentos de herramientas, resultados de herramientas o cuerpos de memoria del usuario.

El objetivo no es conservar más contexto. Es dejar suficiente evidencia para que un desarrollador pueda identificar qué estrategia de contexto se ejecutó y si cambió la siguiente llamada al modelo de la manera prevista.

### Ejemplo de Ingeniería de Contexto

Supongamos que queremos que un agente de IA **"Me reserve un viaje a París."**

• Un agente simple que use sólo ingeniería de prompts podría simplemente responder: **"De acuerdo, ¿cuándo te gustaría ir a París?**". Solo procesó tu pregunta directa en el momento en que el usuario preguntó.

• Un agente que usa las estrategias de ingeniería de contexto cubiertas haría mucho más. Antes de responder, su sistema podría:

  ◦ **Revisar tu calendario** para fechas disponibles (recuperando datos en tiempo real).

 ◦ **Recordar preferencias de viaje pasadas** (de memoria a largo plazo) como tu aerolínea preferida, presupuesto o si prefieres vuelos directos.

 ◦ **Identificar herramientas disponibles** para reservas de vuelo y hotel.

- Entonces, una respuesta de ejemplo podría ser:  "¡Hola [Tu Nombre]! Veo que estás libre la primera semana de octubre. ¿Busco vuelos directos a París en [Aerolínea Preferida] dentro de tu presupuesto habitual de [Presupuesto]?". Esta respuesta más rica y consciente del contexto demuestra el poder de la ingeniería de contexto.

## Fallos Comunes de Contexto

### Envenenamiento de Contexto

**Qué es:** Cuando una alucinación (información falsa generada por el LLM) o un error entra en el contexto y se referencia repetidamente, haciendo que el agente persiga objetivos imposibles o desarrolle estrategias absurdas.

**Qué hacer:** Implementar **validación de contexto** y **cuarentena**. Validar la información antes de agregarla a la memoria a largo plazo. Si se detecta posible envenenamiento, iniciar hilos de contexto nuevos para evitar que la mala información se propague.

**Ejemplo de Reserva de Viaje:** Tu agente alucina un **vuelo directo desde un pequeño aeropuerto local a una ciudad internacional distante** que en realidad no ofrece vuelos internacionales. Este detalle de vuelo inexistente se guarda en el contexto. Más tarde, cuando le pides al agente que reserve, sigue intentando encontrar boletos para esta ruta imposible, llevando a errores repetidos.

**Solución:** Implementar un paso que **valide la existencia del vuelo y rutas con una API en tiempo real** _antes_ de agregar el detalle del vuelo al contexto de trabajo del agente. Si la validación falla, la información errónea se "cuarentena" y no se usa más.

### Distracción de Contexto

**Qué es:** Cuando el contexto se vuelve tan grande que el modelo se enfoca demasiado en el historial acumulado en lugar de usar lo que aprendió durante el entrenamiento, lo que conduce a acciones repetitivas o poco útiles. Los modelos pueden comenzar a cometer errores incluso antes de que la ventana de contexto esté llena.

**Qué hacer:** Usar **resumen del contexto**. Comprimir periódicamente la información acumulada en resúmenes más cortos, manteniendo detalles importantes mientras se elimina el historial redundante. Esto ayuda a "reiniciar" el enfoque.

**Ejemplo de Reserva de Viaje:** Has estado hablando de varios destinos de viaje soñados durante mucho tiempo, incluyendo un recuento detallado de tu viaje de mochilero de hace dos años. Cuando finalmente pides **"encuéntrame un vuelo barato para el mes que viene"**, el agente se atasca en detalles antiguos e irrelevantes y sigue preguntando sobre tu equipo de mochilero o itinerarios pasados, descuidando tu solicitud actual.

**Solución:** Después de cierto número de turnos o cuando el contexto crece demasiado, el agente debe **resumir las partes más recientes y relevantes de la conversación** – enfocándose en tus fechas de viaje actuales y destino – y usar ese resumen condensado para la siguiente llamada al LLM, descartando el chat histórico menos relevante.

### Confusión de Contexto

**Qué es:** Cuando el contexto innecesario, a menudo en forma de demasiadas herramientas disponibles, hace que el modelo genere respuestas malas o llame a herramientas irrelevantes. Los modelos más pequeños son especialmente propensos a esto.

**Qué hacer:** Implementar **gestión de carga de herramientas** usando técnicas RAG. Almacenar descripciones de herramientas en una base de datos vectorial y seleccionar _solo_ las herramientas más relevantes para cada tarea específica. Las investigaciones muestran limitar las selecciones a menos de 30 herramientas.

**Ejemplo de Reserva de Viaje:** Tu agente tiene acceso a decenas de herramientas: `reservar_vuelo`, `reservar_hotel`, `alquilar_auto`, `encontrar_tours`, `convertidor_moneda`, `pronóstico_meteorológico`, `reservas_restaurantes`, etc. Preguntas, **"¿Cuál es la mejor manera de moverse por París?"** Debido a la gran cantidad de herramientas, el agente se confunde e intenta llamar a `reservar_vuelo` _dentro_ de París, o `alquilar_auto` aunque prefieres transporte público, porque las descripciones de las herramientas podrían superponerse o simplemente no distingue la mejor.

**Solución:** Usar **RAG sobre descripciones de herramientas**. Cuando preguntas sobre moverse por París, el sistema recupera dinámicamente _solo_ las herramientas más relevantes como `alquilar_auto` o `info_transporte_público` basándose en tu consulta, presentando una "carga" enfocada de herramientas al LLM.

### Choque de Contexto

**Qué es:** Cuando existe información contradictoria dentro del contexto, llevando a razonamientos inconsistentes o respuestas finales erróneas. Esto suele ocurrir cuando la información llega en etapas y las suposiciones tempranas e incorrectas permanecen en el contexto.

**Qué hacer:** Usar **poda de contexto** y **descarga**. La poda significa eliminar información desactualizada o contradictoria a medida que llegan nuevos detalles. La descarga proporciona al modelo un espacio de trabajo separado tipo "bloc de notas" para procesar información sin saturar el contexto principal.


**Ejemplo de Reserva de Viaje:** Inicialmente le dices a tu agente, **"Quiero volar en clase económica."** Más tarde en la conversación, cambias de opinión y dices, **"De hecho, para este viaje, vamos en clase business."** Si ambas instrucciones permanecen en el contexto, el agente podría recibir resultados de búsqueda contradictorios o confundirse sobre qué preferencia dar prioridad.

**Solución:** Implementa **poda del contexto**. Cuando una nueva instrucción contradice a una anterior, la instrucción más antigua se elimina o se anula explícitamente en el contexto. Alternativamente, el agente puede usar un **scratchpad** para conciliar preferencias conflictivas antes de decidir, asegurando que solo la instrucción final y consistente guíe sus acciones.

## ¿Tienes más preguntas sobre Ingeniería del Contexto?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros aprendices, asistir a horas de oficina y obtener respuestas a tus preguntas sobre Agentes de IA.
## Lección Anterior

[Protocolos Agénticos](../11-agentic-protocols/README.md)

## Próxima Lección

[Memoria para Agentes de IA](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->