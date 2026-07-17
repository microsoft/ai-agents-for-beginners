# Uso de Protocolos Agénticos (MCP, A2A y NLWeb)

[![Protocolos Agénticos](../../../translated_images/es/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Haz clic en la imagen de arriba para ver el vídeo de esta lección)_

A medida que crece el uso de agentes de IA, también crece la necesidad de protocolos que aseguren la estandarización, la seguridad y apoyen la innovación abierta. En esta lección, cubriremos 3 protocolos que buscan satisfacer esta necesidad - Protocolo de Contexto de Modelo (MCP), de Agente a Agente (A2A) y la Web de Lenguaje Natural (NLWeb).

## Introducción

En esta lección, cubriremos:

• Cómo **MCP** permite a los Agentes de IA acceder a herramientas externas y datos para completar las tareas del usuario.

• Cómo **A2A** habilita la comunicación y colaboración entre diferentes agentes de IA.

• Cómo **NLWeb** lleva interfaces de lenguaje natural a cualquier sitio web permitiendo que los Agentes de IA descubran e interactúen con el contenido.

## Objetivos de Aprendizaje

• **Identificar** el propósito central y los beneficios de MCP, A2A y NLWeb en el contexto de agentes de IA.

• **Explicar** cómo cada protocolo facilita la comunicación e interacción entre LLMs, herramientas y otros agentes.

• **Reconocer** los roles distintos que cada protocolo desempeña en la construcción de sistemas agénticos complejos.

## Protocolo de Contexto de Modelo

El **Protocolo de Contexto de Modelo (MCP)** es un estándar abierto que proporciona una forma estandarizada para que las aplicaciones provean contexto y herramientas a los LLMs. Esto habilita un "adaptador universal" para diferentes fuentes de datos y herramientas a las que los Agentes de IA pueden conectarse de manera consistente.

Veamos los componentes del MCP, los beneficios comparados con el uso directo de API, y un ejemplo de cómo los agentes de IA podrían usar un servidor MCP.

### Componentes Principales de MCP

MCP opera bajo una **arquitectura cliente-servidor** y sus componentes principales son:

• **Hosts** son aplicaciones LLM (por ejemplo un editor de código como VSCode) que inician las conexiones hacia un Servidor MCP.

• **Clientes** son componentes dentro de la aplicación host que mantienen conexiones uno a uno con los servidores.

• **Servidores** son programas ligeros que exponen capacidades específicas.

Incluido en el protocolo hay tres primitivas principales que son las capacidades de un Servidor MCP:

• **Herramientas**: Son acciones o funciones discretas que un agente de IA puede llamar para realizar una acción. Por ejemplo, un servicio meteorológico podría exponer la herramienta "obtener clima" o un servidor de comercio electrónico podría exponer la herramienta "comprar producto". Los servidores MCP anuncian el nombre, descripción y esquema de entrada/salida de cada herramienta en su listado de capacidades.

• **Recursos**: Son elementos de datos o documentos de solo lectura que un servidor MCP puede proporcionar, y los clientes pueden recuperarlos bajo demanda. Ejemplos incluyen contenido de archivos, registros de bases de datos o archivos de registro. Los recursos pueden ser texto (como código o JSON) o binarios (como imágenes o PDFs).

• **Prompts**: Son plantillas predefinidas que proveen prompts sugeridos, permitiendo flujos de trabajo más complejos.

### Beneficios de MCP

MCP ofrece ventajas significativas para los Agentes de IA:

• **Descubrimiento Dinámico de Herramientas**: Los agentes pueden recibir dinámicamente una lista de herramientas disponibles de un servidor junto con descripciones de lo que hacen. Esto contrasta con las APIs tradicionales, que a menudo requieren codificación estática para integraciones, lo que implica que cualquier cambio en la API exige actualizaciones de código. MCP ofrece un enfoque de "integrar una vez", llevando a una mayor adaptabilidad.

• **Interoperabilidad entre LLMs**: MCP funciona entre diferentes LLMs, proporcionando flexibilidad para cambiar los modelos principales y evaluar para un mejor rendimiento.

• **Seguridad Estandarizada**: MCP incluye un método estándar de autenticación, mejorando la escalabilidad al agregar acceso a servidores MCP adicionales. Esto es más simple que gestionar diferentes claves y tipos de autenticación para varias APIs tradicionales.

### Ejemplo MCP

![Diagrama MCP](../../../translated_images/es/mcp-diagram.e4ca1cbd551444a1.webp)

Imagina que un usuario quiere reservar un vuelo usando un asistente de IA potenciado por MCP.

1. **Conexión**: El asistente de IA (el cliente MCP) se conecta a un servidor MCP proporcionado por una aerolínea.

2. **Descubrimiento de Herramientas**: El cliente pregunta al servidor MCP de la aerolínea, "¿Qué herramientas tienen disponibles?" El servidor responde con herramientas como "buscar vuelos" y "reservar vuelos".

3. **Invocación de Herramienta**: Luego le pides al asistente de IA, "Por favor busca un vuelo de Portland a Honolulu." El asistente de IA, usando su LLM, identifica que debe llamar a la herramienta "buscar vuelos" y pasa los parámetros relevantes (origen, destino) al servidor MCP.

4. **Ejecución y Respuesta**: El servidor MCP, actuando como envoltorio, hace la llamada real a la API interna de reservas de la aerolínea. Luego recibe la información del vuelo (por ejemplo, datos JSON) y la devuelve al asistente de IA.

5. **Interacción Posterior**: El asistente de IA presenta las opciones de vuelo. Una vez que eliges un vuelo, el asistente podría invocar la herramienta "reservar vuelo" en el mismo servidor MCP, completando la reserva.

## Protocolo de Agente a Agente (A2A)

Mientras MCP se centra en conectar LLMs a herramientas, el **protocolo de Agente a Agente (A2A)** va un paso más allá habilitando la comunicación y colaboración entre diferentes agentes de IA. A2A conecta agentes de IA de distintas organizaciones, entornos y tecnologías para completar una tarea compartida.

Examinaremos los componentes y beneficios de A2A, junto con un ejemplo de cómo podría aplicarse en nuestra aplicación de viajes.

### Componentes Principales de A2A

A2A se enfoca en permitir la comunicación entre agentes y que trabajen juntos para completar una subtarea del usuario. Cada componente del protocolo contribuye a esto:

#### Tarjeta de Agente

Similar a cómo un servidor MCP comparte una lista de herramientas, una Tarjeta de Agente tiene:
- El Nombre del Agente.
- Una **descripción de las tareas generales** que completa.
- Una **lista de habilidades específicas** con descripciones para ayudar a otros agentes (o incluso usuarios humanos) a entender cuándo y por qué querrían llamar a ese agente.
- La **URL actual del Punto de Acceso** del agente.
- La **versión** y **capacidades** del agente como respuestas en streaming y notificaciones push.

#### Ejecutor de Agente

El Ejecutor de Agente es responsable de **pasar el contexto del chat del usuario al agente remoto**, el agente remoto necesita esto para entender la tarea que debe completar. En un servidor A2A, un agente usa su propio Modelo de Lenguaje Grande (LLM) para analizar las solicitudes entrantes y ejecutar tareas usando sus propias herramientas internas.

#### Artefacto

Una vez que un agente remoto ha completado la tarea solicitada, se crea su producto de trabajo como un artefacto. Un artefacto **contiene el resultado del trabajo del agente**, una **descripción de lo que se completó**, y el **contexto textual** que se envía a través del protocolo. Después de enviar el artefacto, la conexión con el agente remoto se cierra hasta que se necesite nuevamente.

#### Cola de Eventos

Este componente se usa para **manejar actualizaciones y pasar mensajes**. Es particularmente importante en producción para sistemas agénticos para evitar que la conexión entre agentes se cierre antes de que una tarea se complete, especialmente cuando los tiempos de finalización de tareas pueden ser largos.

### Beneficios de A2A

• **Colaboración Mejorada**: Permite que agentes de diferentes proveedores y plataformas interactúen, compartan contexto y trabajen juntos, facilitando una automatización fluida entre sistemas tradicionalmente desconectados.

• **Flexibilidad en Selección de Modelo**: Cada agente A2A puede decidir qué LLM usa para atender sus solicitudes, permitiendo modelos optimizados o ajustados fina-mente por agente, a diferencia de una única conexión LLM en algunos escenarios MCP.

• **Autenticación Integrada**: La autenticación está integrada directamente en el protocolo A2A, proporcionando un marco robusto de seguridad para las interacciones entre agentes.

### Ejemplo A2A

![Diagrama A2A](../../../translated_images/es/A2A-Diagram.8666928d648acc26.webp)

Expandiendo nuestro escenario de reserva de viajes, pero esta vez usando A2A.

1. **Solicitud del Usuario a Multi-Agente**: Un usuario interactúa con un cliente/agente A2A "Agente de Viajes", quizás diciendo: "Por favor reserva un viaje completo a Honolulu para la próxima semana, incluyendo vuelos, hotel y coche de alquiler".

2. **Orquestación por el Agente de Viajes**: El Agente de Viajes recibe esta solicitud compleja. Usa su LLM para razonar sobre la tarea y determinar que necesita interactuar con otros agentes especializados.

3. **Comunicación Inter-Agente**: El Agente de Viajes usa entonces el protocolo A2A para conectarse a agentes descendentes, como un "Agente de Aerolínea", un "Agente de Hotel" y un "Agente de Alquiler de Coches" creados por diferentes compañías.

4. **Ejecución Delegada de Tareas**: El Agente de Viajes envía tareas específicas a estos agentes especializados (ejemplo, "Encuentra vuelos a Honolulu", "Reserva un hotel", "Alquila un coche"). Cada uno de estos agentes especializados, ejecutando sus propios LLMs y utilizando sus propias herramientas (que podrían ser servidores MCP ellos mismos), realiza su parte específica de la reserva.

5. **Respuesta Consolidada**: Una vez que todos los agentes descendentes completan sus tareas, el Agente de Viajes compila los resultados (detalles de vuelo, confirmación del hotel, reserva del coche) y envía una respuesta integral, en estilo chat, al usuario.

## Web de Lenguaje Natural (NLWeb)

Los sitios web han sido desde hace mucho la forma principal para que los usuarios accedan a información y datos a través de internet.

Veamos los diferentes componentes de NLWeb, los beneficios de NLWeb y un ejemplo de cómo funciona nuestro NLWeb viendo nuestra aplicación de viajes.

### Componentes de NLWeb

- **Aplicación NLWeb (Código de Servicio Central)**: El sistema que procesa preguntas de lenguaje natural. Conecta las diferentes partes de la plataforma para crear respuestas. Puedes pensar en él como el **motor que impulsa las características de lenguaje natural** de un sitio web.

- **Protocolo NLWeb**: Este es un **conjunto básico de reglas para la interacción de lenguaje natural** con un sitio web. Envía respuestas en formato JSON (a menudo usando Schema.org). Su propósito es crear una base simple para la “Web IA,” de igual forma que HTML hizo posible compartir documentos en línea.

- **Servidor MCP (Punto de Acceso al Protocolo de Contexto de Modelo)**: Cada configuración NLWeb también funciona como un **servidor MCP**. Esto significa que puede **compartir herramientas (como un método “ask”) y datos** con otros sistemas de IA. En la práctica, esto hace que el contenido y las capacidades del sitio web sean utilizables por agentes IA, permitiendo que el sitio se convierte en parte del “ecosistema de agentes” más amplio.

- **Modelos de Embeddings**: Estos modelos se usan para **convertir el contenido del sitio web en representaciones numéricas llamadas vectores** (embeddings). Estos vectores capturan significado de una manera que las computadoras pueden comparar y buscar. Se almacenan en una base de datos especial, y los usuarios pueden elegir qué modelo de embedding desean usar.

- **Base de Datos Vectorial (Mecanismo de Recuperación)**: Esta base de datos **almacena los embeddings del contenido web**. Cuando alguien hace una pregunta, NLWeb revisa la base de datos vectorial para encontrar rápidamente la información más relevante. Proporciona una lista rápida de posibles respuestas, ordenadas por similitud. NLWeb funciona con diferentes sistemas de almacenamiento vectorial como Qdrant, Snowflake, Milvus, Azure AI Search y Elasticsearch.

### NLWeb con un Ejemplo

![NLWeb](../../../translated_images/es/nlweb-diagram.c1e2390b310e5fe4.webp)

Consideremos nuevamente nuestro sitio web de reservas de viajes, pero esta vez, está potenciado por NLWeb.

1. **Ingesta de Datos**: Los catálogos de productos existentes del sitio web de viajes (ej. listados de vuelos, descripciones de hoteles, paquetes turísticos) están formateados usando Schema.org o cargados mediante feeds RSS. Las herramientas de NLWeb ingieren estos datos estructurados, crean embeddings y los almacenan en una base de datos vectorial local o remota.

2. **Consulta en Lenguaje Natural (Humano)**: Un usuario visita el sitio web y, en lugar de navegar menús, escribe en una interfaz de chat: "Encuentra un hotel familiar en Honolulu con piscina para la próxima semana".

3. **Procesamiento NLWeb**: La aplicación NLWeb recibe esta consulta. Envía la consulta a un LLM para su comprensión y simultáneamente busca en su base de datos vectorial listados relevantes de hoteles.

4. **Resultados Precisos**: El LLM ayuda a interpretar los resultados de búsqueda de la base de datos, identifica las mejores coincidencias basadas en los criterios "familiar", "piscina" y "Honolulu", y luego formatea una respuesta en lenguaje natural. Crucialmente, la respuesta se refiere a hoteles reales del catálogo del sitio web, evitando información inventada.

5. **Interacción con Agente IA**: Debido a que NLWeb funciona como un servidor MCP, un agente de viaje IA externo también podría conectarse a esta instancia NLWeb del sitio. El agente IA podría entonces usar el método `ask` de MCP para consultar directamente al sitio web: `ask("¿Hay restaurantes veganos recomendados por el hotel en la zona de Honolulu?")`. La instancia NLWeb procesaría esto, utilizando su base de datos de información de restaurantes (si está cargada), y devolvería una respuesta JSON estructurada.

### ¿Tienes más preguntas sobre MCP/A2A/NLWeb?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros aprendices, asistir a horas de oficina y resolver tus dudas sobre Agentes de IA.

## Recursos

- [MCP para Principiantes](https://aka.ms/mcp-for-beginners)  
- [Documentación MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositorio NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Marco de Agentes Microsoft](https://aka.ms/ai-agents-beginners/agent-framework)

## Lección Anterior

[Agentes de IA en Producción](../10-ai-agents-production/README.md)

## Próxima Lección

[Ingeniería de Contexto para Agentes IA](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->