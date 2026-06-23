# Memoria para Agentes de IA 
[![Agent Memory](../../../translated_images/es/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Al hablar de los beneficios únicos de crear Agentes de IA, se discuten principalmente dos cosas: la capacidad de llamar a herramientas para completar tareas y la capacidad de mejorar con el tiempo. La memoria está en la base de la creación de agentes auto-mejorables que pueden crear mejores experiencias para nuestros usuarios.

En esta lección, veremos qué es la memoria para los Agentes de IA y cómo podemos gestionarla y usarla en beneficio de nuestras aplicaciones.

## Introducción

Esta lección cubrirá:

• **Comprender la Memoria de Agentes de IA**: Qué es la memoria y por qué es esencial para los agentes.

• **Implementación y almacenamiento de la Memoria**: Métodos prácticos para agregar capacidades de memoria a sus agentes de IA, centrándose en la memoria a corto y largo plazo.

• **Hacer que los Agentes de IA se Auto-mejoren**: Cómo la memoria permite a los agentes aprender de interacciones pasadas y mejorar con el tiempo.

## Implementaciones Disponibles

Esta lección incluye dos tutoriales completos en notebooks:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa memoria usando Mem0 y Azure AI Search con Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memoria estructurada usando Cognee, construyendo automáticamente un grafo de conocimiento respaldado por embeddings, visualizando el grafo y recuperación inteligente

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo:

• **Diferenciar entre varios tipos de memoria de agentes de IA**, incluyendo memoria operativa, a corto plazo y a largo plazo, así como formas especializadas como la memoria de persona y episódica.

• **Implementar y gestionar memoria a corto y largo plazo para agentes de IA** usando Microsoft Agent Framework, aprovechando herramientas como Mem0, Cognee, memoria Whiteboard e integrando con Azure AI Search.

• **Comprender los principios detrás de los agentes de IA auto-mejorables** y cómo los sistemas robustos de gestión de memoria contribuyen al aprendizaje continuo y a la adaptación.

## Comprendiendo la Memoria de Agentes de IA

En esencia, **la memoria para agentes de IA se refiere a los mecanismos que les permiten retener y recordar información**. Esta información puede ser detalles específicos sobre una conversación, preferencias del usuario, acciones pasadas o incluso patrones aprendidos.

Sin memoria, las aplicaciones de IA suelen ser sin estado, lo que significa que cada interacción comienza desde cero. Esto conduce a una experiencia de usuario repetitiva y frustrante donde el agente "olvida" el contexto o las preferencias previas.

### ¿Por qué es importante la Memoria?

La inteligencia de un agente está profundamente ligada a su capacidad para recordar y utilizar información pasada. La memoria permite que los agentes sean:

• **Reflexivos**: Aprendiendo de acciones y resultados pasados.

• **Interactivos**: Manteniendo el contexto durante una conversación en curso.

• **Proactivos y Reactivos**: Anticipando necesidades o respondiendo adecuadamente basándose en datos históricos.

• **Autónomos**: Operando con mayor independencia al extraer conocimiento almacenado.

El objetivo de implementar la memoria es hacer que los agentes sean más **fiables y capaces**.

### Tipos de Memoria

#### Memoria Operativa

Piense en esto como un papel de borrador que un agente usa durante una única tarea o proceso de pensamiento en curso. Contiene información inmediata necesaria para calcular el siguiente paso.

Para los agentes de IA, la memoria operativa a menudo captura la información más relevante de una conversación, incluso si el historial completo del chat es largo o está truncado. Se enfoca en extraer elementos clave como requisitos, propuestas, decisiones y acciones.

**Ejemplo de Memoria Operativa**

En un agente de reservas de viajes, la memoria operativa podría capturar la solicitud actual del usuario, como "Quiero reservar un viaje a París". Este requisito específico se mantiene en el contexto inmediato del agente para guiar la interacción actual.

#### Memoria a Corto Plazo

Este tipo de memoria retiene información durante la duración de una única conversación o sesión. Es el contexto del chat actual, permitiendo que el agente se refiera a turnos previos en el diálogo.

En las muestras del SDK Python de [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), esto se corresponde con `AgentSession`, creado con `agent.create_session()`. La sesión es la memoria a corto plazo incorporada del framework: mantiene disponible el contexto de la conversación mientras se reutilice esa misma sesión, pero ese contexto no se persiste cuando la sesión termina o la aplicación se reinicia. Use memoria a largo plazo para hechos y preferencias que necesitan sobrevivir a través de sesiones, típicamente a través de una base de datos, índice vectorial u otro almacén persistente.

**Ejemplo de Memoria a Corto Plazo**

Si un usuario pregunta, "¿Cuánto costaría un vuelo a París?" y luego añade "¿Y qué hay del alojamiento allí?", la memoria a corto plazo asegura que el agente sabe que "allí" se refiere a "París" dentro de la misma conversación.

#### Memoria a Largo Plazo

Esta es información que persiste a lo largo de múltiples conversaciones o sesiones. Permite a los agentes recordar preferencias de usuario, interacciones históricas o conocimientos generales por períodos extendidos. Esto es importante para la personalización.

**Ejemplo de Memoria a Largo Plazo**

Una memoria a largo plazo podría almacenar que "Ben disfruta del esquí y actividades al aire libre, le gusta el café con vista a la montaña, y quiere evitar pistas de esquí avanzadas debido a una lesión pasada". Esta información, aprendida en interacciones previas, influye en recomendaciones durante futuras sesiones de planificación de viajes, haciéndolas altamente personalizadas.

#### Memoria de Persona

Este tipo especializado de memoria ayuda a un agente a desarrollar una "personalidad" o "persona" consistente. Permite que el agente recuerde detalles sobre sí mismo o su rol previsto, haciendo las interacciones más fluidas y enfocadas.

**Ejemplo de Memoria de Persona**

Si el agente de viajes está diseñado para ser un "planificador experto de esquí", la memoria de persona podría reforzar este rol, influyendo en sus respuestas para alinearlas con el tono y conocimiento de un experto.

#### Memoria de Flujo de Trabajo/Episódica

Esta memoria almacena la secuencia de pasos que un agente toma durante una tarea compleja, incluyendo éxitos y fallos. Es como recordar "episodios" específicos o experiencias pasadas para aprender de ellas.

**Ejemplo de Memoria Episódica**

Si el agente intentó reservar un vuelo específico pero falló por falta de disponibilidad, la memoria episódica podría registrar este fallo, permitiendo al agente intentar vuelos alternativos o informar al usuario sobre el problema de forma más informada en un intento posterior.

#### Memoria de Entidad

Esto implica extraer y recordar entidades específicas (como personas, lugares o cosas) y eventos de las conversaciones. Permite al agente construir una comprensión estructurada de los elementos clave discutidos.

**Ejemplo de Memoria de Entidad**

De una conversación sobre un viaje pasado, el agente podría extraer "París", "Torre Eiffel" y "cena en el restaurante Le Chat Noir" como entidades. En una interacción futura, el agente podría recordar "Le Chat Noir" y ofrecer hacer una nueva reserva allí.

#### RAG Estructurado (Generación Aumentada por Recuperación)

Aunque RAG es una técnica más amplia, el "RAG Estructurado" se destaca como una tecnología potente de memoria. Extrae información densa y estructurada de varias fuentes (conversaciones, correos electrónicos, imágenes) y la usa para mejorar precisión, recall y velocidad en las respuestas. A diferencia del RAG clásico que se basa solo en similitud semántica, RAG Estructurado trabaja con la estructura inherente de la información.

**Ejemplo de RAG Estructurado**

En lugar de solo coincidir palabras clave, RAG Estructurado podría analizar detalles de vuelo (destino, fecha, hora, aerolínea) de un correo y almacenarlos de forma estructurada. Esto permite consultas precisas como "¿Qué vuelo reservé a París el martes?".

## Implementación y Almacenamiento de la Memoria

Implementar memoria para agentes de IA implica un proceso sistemático de **gestión de memoria**, que incluye generar, almacenar, recuperar, integrar, actualizar e incluso "olvidar" (o borrar) información. La recuperación es un aspecto particularmente crucial.

### Herramientas Especializadas de Memoria

#### Mem0

Una forma de almacenar y gestionar la memoria del agente es usando herramientas especializadas como Mem0. Mem0 funciona como una capa de memoria persistente, permitiendo a los agentes recordar interacciones relevantes, almacenar preferencias de usuario y contexto factual, y aprender de éxitos y fracasos con el tiempo. La idea aquí es que los agentes sin estado se conviertan en agentes con estado.

Funciona mediante un **pipeline de memoria en dos fases: extracción y actualización**. Primero, los mensajes añadidos al hilo de un agente se envían al servicio Mem0, que usa un Modelo de Lenguaje Grande (LLM) para resumir el historial de la conversación y extraer nuevas memorias. Posteriormente, una fase de actualización impulsada por LLM determina si agregar, modificar o eliminar estas memorias, almacenándolas en un almacén de datos híbrido que puede incluir bases de datos vectoriales, de grafos y de clave-valor. Este sistema también soporta varios tipos de memoria y puede incorporar memoria en grafo para gestionar relaciones entre entidades.

#### Cognee

Otro enfoque potente es usar **Cognee**, una memoria semántica de código abierto para agentes de IA que transforma datos estructurados y no estructurados en grafos de conocimiento consultables respaldados por embeddings. Cognee ofrece una **arquitectura de doble almacén** que combina búsqueda por similitud vectorial con relaciones de grafo, permitiendo a los agentes entender no solo qué información es similar, sino cómo los conceptos se relacionan entre sí.

Destaca en la **recuperación híbrida** que mezcla similitud vectorial, estructura de grafo y razonamiento LLM - desde consulta de fragmentos sin procesar hasta respuestas basadas en grafo. El sistema mantiene una **memoria viva** que evoluciona y crece mientras permanece consultable como un grafo conectado, soportando tanto el contexto de sesión a corto plazo como la memoria persistente a largo plazo.

El tutorial en notebook de Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demuestra cómo construir esta capa unificada de memoria, con ejemplos prácticos de ingestión de fuentes de datos diversas, visualización del grafo de conocimiento y consulta con diferentes estrategias de búsqueda adaptadas a necesidades específicas del agente.

### Almacenando Memoria con RAG

Más allá de herramientas especializadas como Mem0, puedes aprovechar servicios robustos de búsqueda como **Azure AI Search como backend para almacenar y recuperar memorias**, especialmente para RAG estructurado.

Esto permite fundamentar las respuestas de tu agente con tus propios datos, asegurando respuestas más relevantes y precisas. Azure AI Search puede usarse para almacenar memorias de viaje específicas del usuario, catálogos de productos o cualquier otro conocimiento específico de dominio.

Azure AI Search soporta capacidades como **RAG Estructurado**, que sobresale en extraer y recuperar información densa y estructurada de grandes conjuntos de datos como historiales de conversación, correos electrónicos o incluso imágenes. Esto proporciona "precisión y recall sobrehumanos" en comparación con enfoques tradicionales de fragmentación de texto y embeddings.

## Haciendo que los Agentes de IA se Auto-mejoren

Un patrón común para agentes auto-mejorables implica introducir un **"agente de conocimiento"**. Este agente separado observa la conversación principal entre el usuario y el agente principal. Su rol es:

1. **Identificar información valiosa**: Determinar si alguna parte de la conversación merece guardarse como conocimiento general o preferencia específica del usuario.

2. **Extraer y resumir**: Destilar el aprendizaje o preferencia esencial de la conversación.

3. **Almacenar en una base de conocimiento**: Persistir esta información extraída, a menudo en una base de datos vectorial, para que pueda recuperarse luego.

4. **Aumentar consultas futuras**: Cuando el usuario inicia una nueva consulta, el agente de conocimiento recupera información relevante almacenada y la añade al prompt del usuario, proporcionando contexto crucial al agente principal (similar a RAG).

### Optimización para la Memoria

• **Gestión de Latencia**: Para evitar ralentizar las interacciones del usuario, se puede usar inicialmente un modelo más barato y rápido para comprobar rápidamente si la información es valiosa para almacenar o recuperar, invocando el proceso más complejo de extracción/recuperación solo cuando sea necesario.

• **Mantenimiento de la Base de Conocimiento**: Para una base de conocimiento en crecimiento, la información menos usada con frecuencia puede trasladarse a "almacenamiento en frío" para gestionar los costos.

## ¿Tienes más preguntas sobre Memoria de Agentes?

Únete al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrarte con otros aprendices, asistir a horas de oficina y resolver tus preguntas sobre Agentes de IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->