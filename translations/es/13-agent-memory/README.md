# Memoria para Agentes de IA 
[![Agent Memory](../../../translated_images/es/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Al hablar de los beneficios únicos de crear Agentes de IA, se discuten principalmente dos cosas: la capacidad de llamar a herramientas para completar tareas y la capacidad de mejorar con el tiempo. La memoria está en la base de la creación de agentes que se mejoran a sí mismos y que pueden crear mejores experiencias para nuestros usuarios.

En esta lección, veremos qué es la memoria para los Agentes de IA y cómo podemos gestionarla y usarla para el beneficio de nuestras aplicaciones.

## Introducción

Esta lección cubrirá:

• **Comprender la Memoria en Agentes de IA**: Qué es la memoria y por qué es esencial para los agentes.

• **Implementar y Almacenar Memoria**: Métodos prácticos para añadir capacidades de memoria a tus agentes de IA, enfocándose en la memoria a corto y largo plazo.

• **Hacer que los Agentes de IA se Mejoren a Sí Mismos**: Cómo la memoria permite que los agentes aprendan de interacciones pasadas y mejoren con el tiempo.

## Implementaciones Disponibles

Esta lección incluye dos tutoriales completos en notebook:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa memoria usando Mem0 y Azure AI Search con Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memoria estructurada usando Cognee, construyendo automáticamente un grafo de conocimiento respaldado por embeddings, visualizando el grafo y recuperación inteligente

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo:

• **Diferenciar entre varios tipos de memoria de agentes de IA**, incluyendo memoria operativa, de corto plazo y de largo plazo, así como formas especializadas como memoria de persona y memoria episódica.

• **Implementar y gestionar memoria a corto y largo plazo para agentes de IA** usando Microsoft Agent Framework, aprovechando herramientas como Mem0, Cognee, memoria en Whiteboard, e integrando con Azure AI Search.

• **Entender los principios detrás de los agentes de IA que se mejoran a sí mismos** y cómo los sistemas robustos de gestión de memoria contribuyen al aprendizaje y adaptación continuos.

## Entendiendo la Memoria de los Agentes de IA

En esencia, **la memoria para agentes de IA se refiere a los mecanismos que les permiten retener y recordar información**. Esta información puede ser detalles específicos sobre una conversación, preferencias del usuario, acciones pasadas o incluso patrones aprendidos.

Sin memoria, las aplicaciones de IA suelen ser sin estado, lo que significa que cada interacción comienza desde cero. Esto lleva a una experiencia de usuario repetitiva y frustrante donde el agente "olvida" el contexto o las preferencias previas.

### ¿Por qué es Importante la Memoria?

La inteligencia de un agente está profundamente ligada a su capacidad para recordar y utilizar información pasada. La memoria permite que los agentes sean:

• **Reflexivos**: Aprender de acciones y resultados pasados.

• **Interactivamente Contextuales**: Mantener el contexto durante una conversación en curso.

• **Proactivos y Reactivos**: Anticipar necesidades o responder apropiadamente basándose en datos históricos.

• **Autónomos**: Operar de manera más independiente apoyándose en conocimientos almacenados.

El objetivo de implementar memoria es hacer a los agentes más **confiables y capaces**.

### Tipos de Memoria

#### Memoria Operativa

Piensa en esto como un papel de borrador que usa un agente durante una tarea o proceso de pensamiento único y en curso. Contiene información inmediata necesaria para calcular el siguiente paso.

Para agentes de IA, la memoria operativa suele capturar la información más relevante de una conversación, incluso si el historial completo del chat es largo o está truncado. Se enfoca en extraer elementos clave como requisitos, propuestas, decisiones y acciones.

**Ejemplo de Memoria Operativa**

En un agente de reservas de viaje, la memoria operativa podría capturar la solicitud actual del usuario, como "Quiero reservar un viaje a París". Este requisito específico se mantiene en el contexto inmediato del agente para guiar la interacción actual.

#### Memoria a Corto Plazo

Este tipo de memoria retiene información durante la duración de una conversación o sesión única. Es el contexto del chat actual, permitiendo que el agente se refiera a turnos previos del diálogo.

**Ejemplo de Memoria a Corto Plazo**

Si un usuario pregunta, "¿Cuánto costaría un vuelo a París?" y luego sigue con "¿Y qué hay del alojamiento allí?", la memoria a corto plazo asegura que el agente sabe que "allí" se refiere a "París" dentro de la misma conversación.

#### Memoria a Largo Plazo

Esta es información que persiste a través de múltiples conversaciones o sesiones. Permite a los agentes recordar preferencias del usuario, interacciones históricas o conocimiento general durante períodos extendidos. Esto es importante para la personalización.

**Ejemplo de Memoria a Largo Plazo**

Una memoria a largo plazo podría almacenar que "Ben disfruta del esquí y actividades al aire libre, le gusta el café con vista a la montaña, y quiere evitar pistas de esquí avanzadas debido a una lesión pasada". Esta información, aprendida en interacciones previas, influye en recomendaciones en futuras sesiones de planificación de viajes, haciéndolas altamente personalizadas.

#### Memoria de Persona

Este tipo de memoria especializada ayuda a un agente a desarrollar una "personalidad" o "persona" consistente. Permite que el agente recuerde detalles sobre sí mismo o su rol intencionado, haciendo que las interacciones sean más fluidas y enfocadas.

**Ejemplo de Memoria de Persona**

Si el agente de viajes está diseñado para ser un "experto en planificación de esquí", la memoria de persona podría reforzar este rol, influyendo en sus respuestas para alinearse con el tono y conocimiento de un experto.

#### Memoria de Flujo de Trabajo / Memoria Episódica

Esta memoria almacena la secuencia de pasos que un agente sigue durante una tarea compleja, incluyendo éxitos y fracasos. Es como recordar "episodios" específicos o experiencias pasadas para aprender de ellas.

**Ejemplo de Memoria Episódica**

Si el agente intentó reservar un vuelo específico pero falló por falta de disponibilidad, la memoria episódica podría registrar este fallo, permitiendo que el agente intente vuelos alternativos o informe al usuario sobre el problema de manera más informada durante un intento posterior.

#### Memoria de Entidad

Esto implica extraer y recordar entidades específicas (como personas, lugares o cosas) y eventos de conversaciones. Permite que el agente construya un entendimiento estructurado de los elementos clave discutidos.

**Ejemplo de Memoria de Entidad**

De una conversación sobre un viaje pasado, el agente podría extraer "París," "Torre Eiffel," y "cena en el restaurante Le Chat Noir" como entidades. En una interacción futura, el agente podría recordar "Le Chat Noir" y ofrecer hacer una nueva reserva allí.

#### RAG Estructurado (Generación Aumentada por Recuperación)

Aunque RAG es una técnica más amplia, "RAG estructurado" se destaca como una tecnología poderosa de memoria. Extrae información densa y estructurada de diversas fuentes (conversaciones, correos electrónicos, imágenes) y la usa para mejorar la precisión, recall y velocidad en las respuestas. A diferencia del RAG clásico que se basa solo en la similitud semántica, el RAG estructurado trabaja con la estructura inherente de la información.

**Ejemplo de RAG Estructurado**

En lugar de solo coincidir palabras clave, el RAG estructurado podría analizar detalles de vuelo (destino, fecha, hora, aerolínea) de un correo electrónico y almacenarlos de forma estructurada. Esto permite consultas precisas como "¿Qué vuelo reservé a París el martes?"

## Implementando y Almacenando Memoria

Implementar memoria para agentes de IA implica un proceso sistemático de **gestión de memoria**, que incluye generar, almacenar, recuperar, integrar, actualizar e incluso "olvidar" (o eliminar) información. La recuperación es un aspecto particularmente crucial.

### Herramientas Especializadas para Memoria

#### Mem0

Una forma de almacenar y gestionar la memoria del agente es usando herramientas especializadas como Mem0. Mem0 funciona como una capa de memoria persistente, permitiendo que los agentes recuerden interacciones relevantes, almacenen preferencias del usuario y contexto factual, y aprendan de éxitos y fracasos con el tiempo. La idea aquí es que agentes sin estado se conviertan en agentes con estado.

Funciona a través de un **pipeline de memoria en dos fases: extracción y actualización**. Primero, los mensajes añadidos al hilo de un agente se envían al servicio Mem0, que usa un modelo de lenguaje grande (LLM) para resumir el historial de la conversación y extraer nuevas memorias. Luego, una fase de actualización impulsada por LLM decide si añadir, modificar o eliminar estas memorias, almacenándolas en un almacén de datos híbrido que puede incluir bases de datos vectoriales, grafo y clave-valor. Este sistema también soporta varios tipos de memoria y puede incorporar memoria de grafo para gestionar relaciones entre entidades.

#### Cognee

Otro enfoque poderoso es usar **Cognee**, una memoria semántica de código abierto para agentes de IA que transforma datos estructurados y no estructurados en grafos de conocimiento consultables respaldados por embeddings. Cognee proporciona una **arquitectura de doble almacenamiento** que combina búsqueda por similitud vectorial con relaciones de grafo, permitiendo a los agentes entender no solo qué información es similar, sino cómo los conceptos se relacionan entre sí.

Destaca en la **recuperación híbrida** que mezcla similitud vectorial, estructura de grafo y razonamiento LLM - desde búsqueda en fragmentos en bruto hasta preguntas conscientes del grafo. El sistema mantiene una **memoria viva** que evoluciona y crece mientras sigue siendo consultable como un grafo conectado, soportando tanto contexto de sesión a corto plazo como memoria persistente a largo plazo.

El tutorial en notebook de Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demuestra la construcción de esta capa unificada de memoria, con ejemplos prácticos de ingestión de diversas fuentes de datos, visualización del grafo de conocimiento y consultas con diferentes estrategias de búsqueda adaptadas a necesidades específicas del agente.

### Almacenamiento de Memoria con RAG

Más allá de herramientas especializadas como Mem0, puedes aprovechar servicios robustos de búsqueda como **Azure AI Search como backend para almacenar y recuperar memorias**, especialmente para RAG estructurado.

Esto te permite fundamentar las respuestas de tu agente con tus propios datos, asegurando respuestas más relevantes y precisas. Azure AI Search puede usarse para almacenar memorias de viajes específicas del usuario, catálogos de productos, o cualquier otro conocimiento específico del dominio.

Azure AI Search soporta capacidades como **RAG Estructurado**, que sobresale en extraer y recuperar información densa y estructurada de grandes conjuntos de datos como historiales de conversación, correos electrónicos o incluso imágenes. Esto proporciona "precisión y recall sobrehumanos" comparado con enfoques tradicionales de fragmentación de texto y embeddings.

## Hacer que los Agentes de IA se Mejoren a Sí Mismos

Un patrón común para agentes que se mejoran a sí mismos implica introducir un **"agente de conocimiento"**. Este agente separado observa la conversación principal entre el usuario y el agente primario. Su rol es:

1. **Identificar información valiosa**: Determinar si alguna parte de la conversación vale la pena guardar como conocimiento general o preferencia específica del usuario.

2. **Extraer y resumir**: Destilar el aprendizaje o preferencia esencial de la conversación.

3. **Almacenar en una base de conocimiento**: Persistir esta información extraída, a menudo en una base de datos vectorial, para que pueda recuperarse luego.

4. **Aumentar consultas futuras**: Cuando el usuario inicia una nueva consulta, el agente de conocimiento recupera información almacenada relevante y la añade al prompt del usuario, proporcionando contexto crucial al agente primario (similar a RAG).

### Optimizaciones para la Memoria

• **Gestión de la Latencia**: Para evitar ralentizar las interacciones del usuario, se puede usar inicialmente un modelo más barato y rápido para revisar si la información vale la pena almacenar o recuperar, invocando solo cuando sea necesario el proceso más complejo de extracción/recuperación.

• **Mantenimiento de la Base de Conocimientos**: Para una base de conocimientos creciente, la información menos usada puede moverse a "almacenamiento en frío" para gestionar costos.

## ¿Tienes Más Preguntas Sobre la Memoria de Agentes?

Únete al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrarte con otros aprendices, asistir a horas de oficina y resolver tus preguntas sobre Agentes de IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->