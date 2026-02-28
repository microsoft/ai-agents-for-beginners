# Memoria para Agentes de IA 
[![Memoria del Agente](../../../translated_images/es/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Al discutir los beneficios únicos de crear Agentes de IA, se suelen mencionar dos cosas: la capacidad de invocar herramientas para completar tareas y la capacidad de mejorar con el tiempo. La memoria está en la base de crear un agente que se auto-mejora y que puede crear mejores experiencias para nuestros usuarios.

En esta lección, examinaremos qué es la memoria para Agentes de IA y cómo podemos gestionarla y usarla en beneficio de nuestras aplicaciones.

## Introducción

Esta lección cubrirá:

• **Comprender la memoria de los agentes de IA**: Qué es la memoria y por qué es esencial para los agentes.

• **Implementación y almacenamiento de la memoria**: Métodos prácticos para añadir capacidades de memoria a tus agentes de IA, centrándose en la memoria a corto y largo plazo.

• **Hacer que los agentes de IA se auto-mejoren**: Cómo la memoria permite a los agentes aprender de interacciones pasadas y mejorar con el tiempo.

## Implementaciones disponibles

Esta lección incluye dos tutoriales completos en notebook:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implements memory using Mem0 and Azure AI Search with Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implements structured memory using Cognee, automatically building knowledge graph backed by embeddings, visualizing graph, and intelligent retrieval

## Objetivos de aprendizaje

Después de completar esta lección, sabrás cómo:

• **Diferenciar entre varios tipos de memoria de agentes de IA**, incluyendo memoria de trabajo, a corto plazo y a largo plazo, así como formas especializadas como memoria de persona y memoria episódica.

• **Implementar y gestionar la memoria a corto y largo plazo para agentes de IA** usando Microsoft Agent Framework, aprovechando herramientas como Mem0, Cognee, Whiteboard memory e integrando con Azure AI Search.

• **Entender los principios detrás de los agentes de IA que se auto-mejoran** y cómo los sistemas robustos de gestión de memoria contribuyen al aprendizaje y adaptación continuos.

## Comprender la memoria de los agentes de IA

En su núcleo, **la memoria para agentes de IA se refiere a los mecanismos que les permiten retener y recordar información**. Esta información puede ser detalles específicos sobre una conversación, preferencias del usuario, acciones pasadas o incluso patrones aprendidos.

Sin memoria, las aplicaciones de IA suelen ser sin estado, lo que significa que cada interacción comienza desde cero. Esto conduce a una experiencia de usuario repetitiva y frustrante donde el agente "olvida" el contexto o las preferencias previas.

### ¿Por qué es importante la memoria?

La inteligencia de un agente está profundamente ligada a su capacidad de recordar y utilizar información pasada. La memoria permite que los agentes sean:

• **Reflexivos**: Aprender de acciones y resultados pasados.

• **Interactivos**: Mantener el contexto durante una conversación en curso.

• **Proactivos y reactivos**: Anticipar necesidades o responder apropiadamente basándose en datos históricos.

• **Autónomos**: Operar con más independencia recurriendo al conocimiento almacenado.

El objetivo de implementar memoria es hacer que los agentes sean más **confiables y capaces**.

### Tipos de memoria

#### Memoria de trabajo

Piénsalo como un trozo de papel de borrador que un agente usa durante una única tarea en curso o proceso de pensamiento. Contiene la información inmediata necesaria para calcular el siguiente paso.

Para los agentes de IA, la memoria de trabajo suele capturar la información más relevante de una conversación, incluso si el historial completo del chat es largo o está truncado. Se centra en extraer elementos clave como requisitos, propuestas, decisiones y acciones.

**Ejemplo de memoria de trabajo**

En un agente de reservas de viajes, la memoria de trabajo podría capturar la solicitud actual del usuario, como "Quiero reservar un viaje a París". Este requisito específico se mantiene en el contexto inmediato del agente para guiar la interacción actual.

#### Memoria a corto plazo

Este tipo de memoria conserva información durante la duración de una sola conversación o sesión. Es el contexto del chat actual, lo que permite que el agente se refiera a turnos anteriores en el diálogo.

**Ejemplo de memoria a corto plazo**

Si un usuario pregunta, "¿Cuánto costaría un vuelo a París?" y luego añade "¿Y el alojamiento allí?", la memoria a corto plazo asegura que el agente sepa que "allí" se refiere a "París" dentro de la misma conversación.

#### Memoria a largo plazo

Se trata de información que persiste a través de múltiples conversaciones o sesiones. Permite a los agentes recordar preferencias del usuario, interacciones históricas o conocimientos generales durante periodos prolongados. Esto es importante para la personalización.

**Ejemplo de memoria a largo plazo**

Una memoria a largo plazo podría almacenar que "Ben disfruta del esquí y las actividades al aire libre, le gusta el café con vistas a la montaña y quiere evitar pistas avanzadas de esquí debido a una lesión pasada". Esta información, aprendida de interacciones previas, influye en las recomendaciones en futuras sesiones de planificación de viajes, haciéndolas altamente personalizadas.

#### Memoria de persona

Este tipo de memoria especializado ayuda a un agente a desarrollar una "personalidad" o "persona" coherente. Permite que el agente recuerde detalles sobre sí mismo o sobre su rol previsto, haciendo que las interacciones sean más fluidas y enfocadas.

**Ejemplo de memoria de persona**
Si el agente de viajes está diseñado para ser un "planificador experto de esquí", la memoria de persona podría reforzar este rol, influyendo en sus respuestas para alinearlas con el tono y los conocimientos de un experto.

#### Memoria de flujo de trabajo/episódica

Esta memoria almacena la secuencia de pasos que un agente realiza durante una tarea compleja, incluidos éxitos y fracasos. Es como recordar "episodios" específicos o experiencias pasadas para aprender de ellas.

**Ejemplo de memoria episódica**

Si el agente intentó reservar un vuelo específico pero falló debido a falta de disponibilidad, la memoria episódica podría registrar este fallo, permitiendo que el agente pruebe vuelos alternativos o informe al usuario sobre el problema de una manera más informada durante un intento posterior.

#### Memoria de entidades

Esto implica extraer y recordar entidades específicas (como personas, lugares o cosas) y eventos de las conversaciones. Permite al agente construir una comprensión estructurada de los elementos clave discutidos.

**Ejemplo de memoria de entidades**

De una conversación sobre un viaje pasado, el agente podría extraer "París", "Torre Eiffel" y "cena en el restaurante Le Chat Noir" como entidades. En una interacción futura, el agente podría recordar "Le Chat Noir" y ofrecer hacer una nueva reserva allí.

#### RAG Estructurado (Retrieval Augmented Generation)

Aunque RAG es una técnica más amplia, el "RAG estructurado" se destaca como una tecnología de memoria potente. Extrae información densa y estructurada de diversas fuentes (conversaciones, correos electrónicos, imágenes) y la utiliza para mejorar la precisión, la recuperación y la velocidad en las respuestas. A diferencia del RAG clásico que se basa únicamente en la similitud semántica, el RAG estructurado trabaja con la estructura inherente de la información.

**Ejemplo de RAG estructurado**

En lugar de limitarse a coincidir palabras clave, el RAG estructurado podría analizar detalles de un vuelo (destino, fecha, hora, aerolínea) de un correo electrónico y almacenarlos de forma estructurada. Esto permite consultas precisas como "¿Qué vuelo reservé a París el martes?"

## Implementación y almacenamiento de la memoria

Implementar memoria para agentes de IA implica un proceso sistemático de **gestión de memoria**, que incluye generar, almacenar, recuperar, integrar, actualizar e incluso "olvidar" (o eliminar) información. La recuperación es un aspecto particularmente crucial.

### Herramientas de memoria especializadas

#### Mem0

Una forma de almacenar y gestionar la memoria de un agente es utilizando herramientas especializadas como Mem0. Mem0 funciona como una capa de memoria persistente, permitiendo a los agentes recordar interacciones relevantes, almacenar preferencias de usuario y contexto factual, y aprender de éxitos y fracasos con el tiempo. La idea aquí es que los agentes sin estado se conviertan en agentes con estado.

Funciona a través de una **canalización de memoria en dos fases: extracción y actualización**. Primero, los mensajes añadidos al hilo de un agente se envían al servicio Mem0, que utiliza un Large Language Model (LLM) para resumir el historial de la conversación y extraer nuevas memorias. Posteriormente, una fase de actualización impulsada por LLM determina si agregar, modificar o eliminar estas memorias, almacenándolas en un almacén de datos híbrido que puede incluir bases de datos vectoriales, de grafos y de clave-valor. Este sistema también soporta varios tipos de memoria y puede incorporar memoria de grafo para gestionar relaciones entre entidades.

#### Cognee

Otro enfoque potente es usar **Cognee**, una memoria semántica de código abierto para agentes de IA que transforma datos estructurados y no estructurados en grafos de conocimiento consultables respaldados por embeddings. Cognee ofrece una **arquitectura de doble almacenamiento** que combina búsqueda por similitud vectorial con relaciones de grafos, lo que permite a los agentes entender no solo qué información es similar, sino cómo se relacionan los conceptos entre sí.

Sobresale en la **recuperación híbrida** que mezcla similitud vectorial, estructura de grafos y razonamiento LLM — desde la búsqueda de fragmentos sin procesar hasta la respuesta a preguntas con conciencia del grafo. El sistema mantiene una **memoria viva** que evoluciona y crece mientras sigue siendo consultable como un grafo conectado único, apoyando tanto el contexto de sesión a corto plazo como la memoria persistente a largo plazo.

El tutorial en notebook de Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demuestra la construcción de esta capa de memoria unificada, con ejemplos prácticos de ingestión de diversas fuentes de datos, visualización del grafo de conocimiento y consulta con diferentes estrategias de búsqueda adaptadas a las necesidades específicas del agente.

### Almacenamiento de memoria con RAG

Más allá de herramientas de memoria especializadas como Mem0, puedes aprovechar servicios de búsqueda robustos como **Azure AI Search como backend para almacenar y recuperar memorias**, especialmente para RAG estructurado.

Esto te permite fundamentar las respuestas de tu agente con tus propios datos, asegurando respuestas más relevantes y precisas. Azure AI Search puede usarse para almacenar memorias de viaje específicas de usuarios, catálogos de productos o cualquier otro conocimiento específico del dominio.

Azure AI Search soporta capacidades como **RAG Estructurado**, que sobresale en extraer y recuperar información densa y estructurada de grandes conjuntos de datos como historiales de conversación, correos electrónicos o incluso imágenes. Esto proporciona "precisión y recuperación sobrehumanas" en comparación con los enfoques tradicionales de segmentación de texto e incrustaciones.

## Hacer que los agentes de IA se auto-mejoren

Un patrón común para agentes que se auto-mejoran implica introducir un **"agente de conocimiento"**. Este agente separado observa la conversación principal entre el usuario y el agente primario. Su rol es:

1. **Identificar información valiosa**: Determinar si alguna parte de la conversación vale la pena guardar como conocimiento general o como preferencia específica del usuario.

2. **Extraer y resumir**: Destilar el aprendizaje esencial o la preferencia de la conversación.

3. **Almacenar en una base de conocimiento**: Persistir esta información extraída, a menudo en una base de datos vectorial, para que pueda recuperarse más tarde.

4. **Aumentar consultas futuras**: Cuando el usuario inicia una nueva consulta, el agente de conocimiento recupera la información almacenada relevante y la añade al prompt del usuario, proporcionando contexto crucial al agente primario (similar a RAG).

### Optimizaciones para la memoria

• **Gestión de latencia**: Para evitar ralentizar las interacciones del usuario, se puede usar inicialmente un modelo más barato y rápido para comprobar rápidamente si la información vale la pena almacenar o recuperar, invocando el proceso de extracción/recuperación más complejo solo cuando sea necesario.

• **Mantenimiento de la base de conocimiento**: Para una base de conocimiento en crecimiento, la información menos utilizada con frecuencia puede trasladarse a "almacenamiento en frío" para gestionar costos.

## ¿Tienes más preguntas sobre la memoria de los agentes?

Únete al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para reunirte con otros estudiantes, asistir a horas de oficina y resolver tus preguntas sobre Agentes de IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Descargo de responsabilidad:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por un traductor humano. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->