<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T14:03:32+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "es"
}
-->
# Usando Protocolos Agénticos (MCP, A2A y NLWeb)

[![Protocolos Agénticos](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.es.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

A medida que crece el uso de agentes de IA, también aumenta la necesidad de protocolos que garanticen estandarización, seguridad y fomenten la innovación abierta. En esta lección, cubriremos tres protocolos diseñados para satisfacer esta necesidad: el Protocolo de Contexto de Modelo (MCP), Agente a Agente (A2A) y Web de Lenguaje Natural (NLWeb).

## Introducción

En esta lección, abordaremos:

• Cómo **MCP** permite a los agentes de IA acceder a herramientas y datos externos para completar tareas de los usuarios.

• Cómo **A2A** facilita la comunicación y colaboración entre diferentes agentes de IA.

• Cómo **NLWeb** lleva interfaces de lenguaje natural a cualquier sitio web, permitiendo que los agentes de IA descubran e interactúen con el contenido.

## Objetivos de Aprendizaje

• **Identificar** el propósito principal y los beneficios de MCP, A2A y NLWeb en el contexto de los agentes de IA.

• **Explicar** cómo cada protocolo facilita la comunicación e interacción entre LLMs, herramientas y otros agentes.

• **Reconocer** los roles específicos que cada protocolo desempeña en la construcción de sistemas agénticos complejos.

## Protocolo de Contexto de Modelo

El **Protocolo de Contexto de Modelo (MCP)** es un estándar abierto que proporciona una forma estandarizada para que las aplicaciones ofrezcan contexto y herramientas a los LLMs. Esto permite un "adaptador universal" para diferentes fuentes de datos y herramientas a las que los agentes de IA pueden conectarse de manera consistente.

Veamos los componentes de MCP, los beneficios en comparación con el uso directo de APIs y un ejemplo de cómo los agentes de IA podrían usar un servidor MCP.

### Componentes Principales de MCP

MCP opera bajo una **arquitectura cliente-servidor** y sus componentes principales son:

• **Hosts**: Son aplicaciones de LLM (por ejemplo, un editor de código como VSCode) que inician las conexiones con un servidor MCP.

• **Clientes**: Son componentes dentro de la aplicación host que mantienen conexiones uno a uno con los servidores.

• **Servidores**: Son programas ligeros que exponen capacidades específicas.

El protocolo incluye tres primitivas principales que representan las capacidades de un servidor MCP:

• **Herramientas**: Son acciones o funciones discretas que un agente de IA puede invocar para realizar una acción. Por ejemplo, un servicio meteorológico podría ofrecer una herramienta "obtener clima", o un servidor de comercio electrónico podría ofrecer una herramienta "comprar producto". Los servidores MCP anuncian el nombre, descripción y esquema de entrada/salida de cada herramienta en su lista de capacidades.

• **Recursos**: Son elementos de datos o documentos de solo lectura que un servidor MCP puede proporcionar y que los clientes pueden recuperar bajo demanda. Ejemplos incluyen contenidos de archivos, registros de bases de datos o archivos de registro. Los recursos pueden ser texto (como código o JSON) o binarios (como imágenes o PDFs).

• **Prompts**: Son plantillas predefinidas que ofrecen sugerencias de prompts, permitiendo flujos de trabajo más complejos.

### Beneficios de MCP

MCP ofrece ventajas significativas para los agentes de IA:

• **Descubrimiento Dinámico de Herramientas**: Los agentes pueden recibir dinámicamente una lista de herramientas disponibles de un servidor junto con descripciones de lo que hacen. Esto contrasta con las APIs tradicionales, que a menudo requieren codificación estática para integraciones, lo que significa que cualquier cambio en la API requiere actualizaciones de código. MCP ofrece un enfoque de "integrar una vez", lo que lleva a una mayor adaptabilidad.

• **Interoperabilidad entre LLMs**: MCP funciona con diferentes LLMs, proporcionando flexibilidad para cambiar modelos principales y evaluar un mejor rendimiento.

• **Seguridad Estandarizada**: MCP incluye un método de autenticación estándar, mejorando la escalabilidad al agregar acceso a servidores MCP adicionales. Esto es más simple que gestionar diferentes claves y tipos de autenticación para varias APIs tradicionales.

### Ejemplo de MCP

![Diagrama MCP](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.es.png)

Imagina que un usuario quiere reservar un vuelo usando un asistente de IA impulsado por MCP.

1. **Conexión**: El asistente de IA (el cliente MCP) se conecta a un servidor MCP proporcionado por una aerolínea.

2. **Descubrimiento de Herramientas**: El cliente pregunta al servidor MCP de la aerolínea: "¿Qué herramientas tienes disponibles?" El servidor responde con herramientas como "buscar vuelos" y "reservar vuelos".

3. **Invocación de Herramientas**: Luego le pides al asistente de IA: "Por favor, busca un vuelo de Portland a Honolulu". El asistente de IA, usando su LLM, identifica que necesita llamar a la herramienta "buscar vuelos" y pasa los parámetros relevantes (origen, destino) al servidor MCP.

4. **Ejecución y Respuesta**: El servidor MCP, actuando como un envoltorio, realiza la llamada real a la API interna de reservas de la aerolínea. Luego recibe la información del vuelo (por ejemplo, datos en JSON) y la envía de vuelta al asistente de IA.

5. **Interacción Adicional**: El asistente de IA presenta las opciones de vuelo. Una vez que seleccionas un vuelo, el asistente podría invocar la herramienta "reservar vuelo" en el mismo servidor MCP, completando la reserva.

## Protocolo Agente a Agente (A2A)

Mientras que MCP se centra en conectar LLMs con herramientas, el **Protocolo Agente a Agente (A2A)** va un paso más allá al permitir la comunicación y colaboración entre diferentes agentes de IA. A2A conecta agentes de IA de diferentes organizaciones, entornos y tecnologías para completar una tarea compartida.

Examinaremos los componentes y beneficios de A2A, junto con un ejemplo de cómo podría aplicarse en nuestra aplicación de viajes.

### Componentes Principales de A2A

A2A se centra en habilitar la comunicación entre agentes y hacer que trabajen juntos para completar una subtarea del usuario. Cada componente del protocolo contribuye a esto:

#### Tarjeta de Agente

Similar a cómo un servidor MCP comparte una lista de herramientas, una Tarjeta de Agente incluye:
- El nombre del agente.
- Una **descripción de las tareas generales** que realiza.
- Una **lista de habilidades específicas** con descripciones para ayudar a otros agentes (o incluso usuarios humanos) a entender cuándo y por qué querrían llamar a ese agente.
- La **URL de endpoint actual** del agente.
- La **versión** y **capacidades** del agente, como respuestas en streaming y notificaciones push.

#### Ejecutor de Agente

El Ejecutor de Agente es responsable de **pasar el contexto del chat del usuario al agente remoto**, ya que el agente remoto necesita esto para entender la tarea que debe completarse. En un servidor A2A, un agente utiliza su propio LLM para analizar solicitudes entrantes y ejecutar tareas usando sus propias herramientas internas.

#### Artefacto

Una vez que un agente remoto ha completado la tarea solicitada, su producto de trabajo se crea como un artefacto. Un artefacto **contiene el resultado del trabajo del agente**, una **descripción de lo que se completó** y el **contexto textual** que se envió a través del protocolo. Después de que se envía el artefacto, la conexión con el agente remoto se cierra hasta que se necesite nuevamente.

#### Cola de Eventos

Este componente se utiliza para **manejar actualizaciones y pasar mensajes**. Es particularmente importante en producción para sistemas agénticos, ya que evita que la conexión entre agentes se cierre antes de que se complete una tarea, especialmente cuando los tiempos de finalización de tareas pueden ser más largos.

### Beneficios de A2A

• **Colaboración Mejorada**: Permite que agentes de diferentes proveedores y plataformas interactúen, compartan contexto y trabajen juntos, facilitando la automatización sin problemas entre sistemas tradicionalmente desconectados.

• **Flexibilidad en la Selección de Modelos**: Cada agente A2A puede decidir qué LLM utiliza para atender sus solicitudes, permitiendo modelos optimizados o ajustados por agente, a diferencia de una conexión única de LLM en algunos escenarios MCP.

• **Autenticación Integrada**: La autenticación está integrada directamente en el protocolo A2A, proporcionando un marco de seguridad robusto para las interacciones entre agentes.

### Ejemplo de A2A

![Diagrama A2A](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.es.png)

Ampliemos nuestro escenario de reserva de viajes, pero esta vez usando A2A.

1. **Solicitud del Usuario a Multi-Agente**: Un usuario interactúa con un "Agente de Viajes" cliente/agente A2A, tal vez diciendo: "Por favor, reserva un viaje completo a Honolulu para la próxima semana, incluyendo vuelos, un hotel y un coche de alquiler".

2. **Orquestación por el Agente de Viajes**: El Agente de Viajes recibe esta solicitud compleja. Utiliza su LLM para razonar sobre la tarea y determinar que necesita interactuar con otros agentes especializados.

3. **Comunicación entre Agentes**: El Agente de Viajes utiliza el protocolo A2A para conectarse con agentes descendentes, como un "Agente de Aerolínea", un "Agente de Hotel" y un "Agente de Alquiler de Coches" creados por diferentes empresas.

4. **Ejecución de Tareas Delegadas**: El Agente de Viajes envía tareas específicas a estos agentes especializados (por ejemplo, "Buscar vuelos a Honolulu", "Reservar un hotel", "Alquilar un coche"). Cada uno de estos agentes especializados, ejecutando sus propios LLMs y utilizando sus propias herramientas (que podrían ser servidores MCP), realiza su parte específica de la reserva.

5. **Respuesta Consolidada**: Una vez que todos los agentes descendentes completan sus tareas, el Agente de Viajes compila los resultados (detalles del vuelo, confirmación del hotel, reserva del coche) y envía una respuesta integral, estilo chat, al usuario.

## Web de Lenguaje Natural (NLWeb)

Los sitios web han sido durante mucho tiempo la forma principal en que los usuarios acceden a información y datos en internet.

Veamos los diferentes componentes de NLWeb, los beneficios de NLWeb y un ejemplo de cómo funciona NLWeb en nuestra aplicación de viajes.

### Componentes de NLWeb

- **Aplicación NLWeb (Código de Servicio Central)**: El sistema que procesa preguntas en lenguaje natural. Conecta las diferentes partes de la plataforma para crear respuestas. Puedes pensar en él como el **motor que impulsa las características de lenguaje natural** de un sitio web.

- **Protocolo NLWeb**: Este es un **conjunto básico de reglas para la interacción en lenguaje natural** con un sitio web. Devuelve respuestas en formato JSON (a menudo usando Schema.org). Su propósito es crear una base simple para la "Web de IA", de la misma manera que HTML hizo posible compartir documentos en línea.

- **Servidor MCP (Punto de Conexión del Protocolo de Contexto de Modelo)**: Cada configuración de NLWeb también funciona como un **servidor MCP**. Esto significa que puede **compartir herramientas (como un método "preguntar") y datos** con otros sistemas de IA. En la práctica, esto hace que el contenido y las capacidades del sitio web sean utilizables por agentes de IA, permitiendo que el sitio se convierta en parte del ecosistema más amplio de agentes.

- **Modelos de Embedding**: Estos modelos se utilizan para **convertir el contenido del sitio web en representaciones numéricas llamadas vectores** (embeddings). Estos vectores capturan el significado de una manera que las computadoras pueden comparar y buscar. Se almacenan en una base de datos especial, y los usuarios pueden elegir qué modelo de embedding quieren usar.

- **Base de Datos de Vectores (Mecanismo de Recuperación)**: Esta base de datos **almacena los embeddings del contenido del sitio web**. Cuando alguien hace una pregunta, NLWeb consulta la base de datos de vectores para encontrar rápidamente la información más relevante. Proporciona una lista rápida de posibles respuestas, clasificadas por similitud. NLWeb funciona con diferentes sistemas de almacenamiento de vectores como Qdrant, Snowflake, Milvus, Azure AI Search y Elasticsearch.

### NLWeb por Ejemplo

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.es.png)

Consideremos nuevamente nuestro sitio web de reservas de viajes, pero esta vez, está impulsado por NLWeb.

1. **Ingesta de Datos**: Los catálogos de productos existentes del sitio web de viajes (por ejemplo, listados de vuelos, descripciones de hoteles, paquetes turísticos) se formatean usando Schema.org o se cargan mediante feeds RSS. Las herramientas de NLWeb ingieren estos datos estructurados, crean embeddings y los almacenan en una base de datos de vectores local o remota.

2. **Consulta en Lenguaje Natural (Humano)**: Un usuario visita el sitio web y, en lugar de navegar por menús, escribe en una interfaz de chat: "Encuéntrame un hotel familiar en Honolulu con piscina para la próxima semana".

3. **Procesamiento de NLWeb**: La aplicación NLWeb recibe esta consulta. Envía la consulta a un LLM para su comprensión y simultáneamente busca en su base de datos de vectores listados de hoteles relevantes.

4. **Resultados Precisos**: El LLM ayuda a interpretar los resultados de búsqueda de la base de datos, identifica las mejores coincidencias basadas en los criterios "familiar", "piscina" y "Honolulu", y luego formatea una respuesta en lenguaje natural. Crucialmente, la respuesta se refiere a hoteles reales del catálogo del sitio web, evitando información inventada.

5. **Interacción con Agentes de IA**: Debido a que NLWeb funciona como un servidor MCP, un agente de viajes externo de IA también podría conectarse a la instancia NLWeb de este sitio web. El agente de IA podría usar el método `ask` de MCP para consultar directamente al sitio web: `ask("¿Hay restaurantes veganos recomendados por el hotel en el área de Honolulu?")`. La instancia NLWeb procesaría esto, aprovechando su base de datos de información de restaurantes (si está cargada), y devolvería una respuesta estructurada en JSON.

### ¿Tienes Más Preguntas sobre MCP/A2A/NLWeb?

Únete al [Discord de Azure AI Foundry](https://aka.ms/ai-agents/discord) para conectarte con otros estudiantes, asistir a horas de oficina y resolver tus dudas sobre agentes de IA.

## Recursos

- [MCP para Principiantes](https://aka.ms/mcp-for-beginners)  
- [Documentación de MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Repositorio de NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Guías de Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.