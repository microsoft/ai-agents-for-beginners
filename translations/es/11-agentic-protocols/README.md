# Uso de Protocolos Agénticos (MCP, A2A y NLWeb)

[![Protocolos Agénticos](../../../translated_images/es/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

A medida que crece el uso de agentes de IA, también lo hace la necesidad de protocolos que aseguren estandarización, seguridad y apoyen la innovación abierta. En esta lección, cubriremos 3 protocolos que buscan satisfacer esta necesidad: Model Context Protocol (MCP), Agent to Agent (A2A) y Natural Language Web (NLWeb).

## Introducción

En esta lección, cubriremos:

• Cómo **MCP** permite a los Agentes de IA acceder a herramientas y datos externos para completar tareas de usuario.

• Cómo **A2A** habilita la comunicación y colaboración entre diferentes agentes de IA.

• Cómo **NLWeb** lleva interfaces de lenguaje natural a cualquier sitio web, permitiendo que los Agentes de IA descubran e interactúen con el contenido.

## Objetivos de Aprendizaje

• **Identificar** el propósito central y los beneficios de MCP, A2A y NLWeb en el contexto de agentes de IA.

• **Explicar** cómo cada protocolo facilita la comunicación e interacción entre LLMs, herramientas y otros agentes.

• **Reconocer** los roles distintos que cada protocolo juega en la construcción de sistemas agénticos complejos.

## Model Context Protocol

El **Model Context Protocol (MCP)** es un estándar abierto que proporciona una manera estandarizada para que las aplicaciones ofrezcan contexto y herramientas a los LLMs. Esto permite un "adaptador universal" a diferentes fuentes de datos y herramientas a las que los Agentes de IA pueden conectarse de manera consistente.

Veamos los componentes de MCP, los beneficios en comparación con el uso directo de APIs, y un ejemplo de cómo los agentes de IA podrían usar un servidor MCP.

### Componentes Principales de MCP

MCP opera con una **arquitectura cliente-servidor** y los componentes principales son:

• **Hosts** son aplicaciones LLM (por ejemplo, un editor de código como VSCode) que inician las conexiones a un servidor MCP.

• **Clientes** son componentes dentro de la aplicación host que mantienen conexiones uno a uno con servidores.

• **Servidores** son programas livianos que exponen capacidades específicas.

Incluidos en el protocolo están tres primitivas centrales que son las capacidades de un servidor MCP:

• **Herramientas**: Son acciones o funciones discretas que un agente de IA puede invocar para realizar una acción. Por ejemplo, un servicio meteorológico podría exponer una herramienta "obtener clima", o un servidor de comercio electrónico podría exponer una herramienta "comprar producto". Los servidores MCP anuncian el nombre, descripción y esquema de entrada/salida de cada herramienta en su listado de capacidades.

• **Recursos**: Son datos o documentos de solo lectura que un servidor MCP puede proporcionar y que los clientes pueden obtener bajo demanda. Ejemplos incluyen contenidos de archivos, registros de bases de datos o archivos de bitácora. Los recursos pueden ser texto (como código o JSON) o binarios (como imágenes o PDFs).

• **Prompts**: Son plantillas predefinidas que ofrecen prompts sugeridos, permitiendo flujos de trabajo más complejos.

### Beneficios de MCP

MCP ofrece ventajas significativas para los Agentes de IA:

• **Descubrimiento Dinámico de Herramientas**: Los agentes pueden recibir dinámicamente una lista de herramientas disponibles de un servidor junto con descripciones de lo que hacen. Esto contrasta con las APIs tradicionales, que a menudo requieren codificación estática para integraciones, lo que significa que cualquier cambio en la API requiere actualizar código. MCP ofrece un enfoque de "integrar una vez", llevando a una mayor adaptabilidad.

• **Interoperabilidad entre LLMs**: MCP funciona con diferentes LLMs, brindando flexibilidad para cambiar modelos centrales y evaluar mejor desempeño.

• **Seguridad Estandarizada**: MCP incluye un método estándar de autenticación, mejorando la escalabilidad al agregar acceso a servidores MCP adicionales. Esto es más simple que gestionar diferentes claves y tipos de autenticación para varias APIs tradicionales.

### Ejemplo de MCP

![Diagrama MCP](../../../translated_images/es/mcp-diagram.e4ca1cbd551444a1.webp)

Imagina que un usuario quiere reservar un vuelo usando un asistente de IA impulsado por MCP.

1. **Conexión**: El asistente de IA (el cliente MCP) se conecta a un servidor MCP proporcionado por una aerolínea.

2. **Descubrimiento de Herramientas**: El cliente pregunta al servidor MCP de la aerolínea: "¿Qué herramientas tienes disponibles?" El servidor responde con herramientas como "buscar vuelos" y "reservar vuelos".

3. **Invocación de la Herramienta**: Luego le pides al asistente de IA: "Por favor busca un vuelo de Portland a Honolulu." El asistente de IA, usando su LLM, identifica que debe llamar a la herramienta "buscar vuelos" y pasa los parámetros relevantes (origen, destino) al servidor MCP.

4. **Ejecución y Respuesta**: El servidor MCP, actuando como un envoltorio, realiza la llamada real a la API interna de reservas de la aerolínea. Luego recibe la información del vuelo (por ejemplo, datos JSON) y la envía de regreso al asistente IA.

5. **Interacción Adicional**: El asistente de IA presenta las opciones de vuelo. Una vez que seleccionas un vuelo, el asistente podría invocar la herramienta "reservar vuelo" en el mismo servidor MCP, completando la reserva.

## Protocolo de Agente a Agente (A2A)

Mientras MCP se enfoca en conectar LLMs a herramientas, el **protocolo Agent-to-Agent (A2A)** da un paso más al habilitar la comunicación y colaboración entre diferentes agentes de IA. A2A conecta agentes de IA a través de diferentes organizaciones, entornos y pilas tecnológicas para completar una tarea compartida.

Examinaremos los componentes y beneficios de A2A, junto con un ejemplo de cómo podría aplicarse en nuestra aplicación de viaje.

### Componentes Principales de A2A

A2A se enfoca en habilitar comunicación entre agentes y que trabajen juntos para completar una subtarea del usuario. Cada componente del protocolo contribuye a esto:

#### Tarjeta de Agente

Similar a cómo un servidor MCP comparte una lista de herramientas, una Tarjeta de Agente tiene:
- El Nombre del Agente.
- Una **descripción de las tareas generales** que completa.
- Una **lista de habilidades específicas** con descripciones para ayudar a otros agentes (o incluso usuarios humanos) a entender cuándo y por qué querrían llamar a ese agente.
- La **URL del Endpoint actual** del agente.
- La **versión** y **capacidades** del agente, tales como respuestas en streaming y notificaciones push.

#### Ejecutor de Agente

El Ejecutor de Agente es responsable de **pasar el contexto del chat del usuario al agente remoto**, el agente remoto necesita esto para entender la tarea a completar. En un servidor A2A, un agente usa su propio Modelo de Lenguaje Extenso (LLM) para analizar las solicitudes entrantes y ejecutar tareas usando sus propias herramientas internas.

#### Artefacto

Una vez que un agente remoto ha completado la tarea solicitada, su producto de trabajo se crea como un artefacto. Un artefacto **contiene el resultado del trabajo del agente**, una **descripción de lo que se completó** y el **contexto textual** que se envía a través del protocolo. Después de que el artefacto es enviado, la conexión con el agente remoto se cierra hasta que se necesite nuevamente.

#### Cola de Eventos

Este componente se usa para **manejar actualizaciones y pasar mensajes**. Es particularmente importante en producción para sistemas agénticos para evitar que la conexión entre agentes se cierre antes de que una tarea se complete, especialmente cuando los tiempos de finalización pueden ser más largos.

### Beneficios de A2A

• **Colaboración Mejorada**: Permite que agentes de diferentes proveedores y plataformas interactúen, compartan contexto y trabajen juntos, facilitando la automatización sin fisuras entre sistemas tradicionalmente desconectados.

• **Flexibilidad en la Selección de Modelos**: Cada agente A2A puede decidir qué LLM utiliza para atender sus solicitudes, permitiendo modelos optimizados o afinados por agente, a diferencia de una sola conexión LLM en algunos escenarios MCP.

• **Autenticación Integrada**: La autenticación está integrada directamente en el protocolo A2A, proporcionando un marco robusto de seguridad para las interacciones de agentes.

### Ejemplo de A2A

![Diagrama A2A](../../../translated_images/es/A2A-Diagram.8666928d648acc26.webp)

Expandamos nuestro escenario de reserva de viajes, pero esta vez usando A2A.

1. **Solicitud de Usuario a Multi-Agente**: Un usuario interactúa con un A2A cliente/agente "Agente de Viajes", quizás diciendo: "Por favor reserva un viaje completo a Honolulu para la próxima semana, incluyendo vuelos, hotel y coche de alquiler".

2. **Orquestación por el Agente de Viajes**: El Agente de Viajes recibe esta solicitud compleja. Usa su LLM para razonar sobre la tarea y determinar que necesita interactuar con otros agentes especializados.

3. **Comunicación Inter-Agentes**: El Agente de Viajes usa el protocolo A2A para conectarse con agentes descendentes, como un "Agente de Aerolínea", un "Agente de Hotel" y un "Agente de Alquiler de Autos" que son creados por distintas compañías.

4. **Ejecución Delegada de Tareas**: El Agente de Viajes envía tareas específicas a estos agentes especializados (por ejemplo, "Encuentra vuelos a Honolulu", "Reserva un hotel", "Alquila un coche"). Cada uno de estos agentes especializados, ejecutando sus propios LLMs y utilizando sus propias herramientas (que podrían ser servidores MCP ellos mismos), realiza su parte específica de la reserva.

5. **Respuesta Consolidada**: Una vez que todos los agentes descendentes completan sus tareas, el Agente de Viajes compila los resultados (detalles de vuelo, confirmación de hotel, reserva de coche) y envía una respuesta completa estilo chat al usuario.

## Natural Language Web (NLWeb)

Los sitios web han sido durante mucho tiempo la forma principal para que los usuarios accedan a información y datos a través de Internet.

Veamos los diferentes componentes de NLWeb, los beneficios de NLWeb y un ejemplo de cómo funciona nuestro NLWeb al observar nuestra aplicación de viajes.

### Componentes de NLWeb

- **Aplicación NLWeb (Código del Servicio Principal)**: El sistema que procesa preguntas en lenguaje natural. Conecta las diferentes partes de la plataforma para crear respuestas. Puedes pensar en ello como el **motor que impulsa las funcionalidades de lenguaje natural** de un sitio web.

- **Protocolo NLWeb**: Es un **conjunto básico de reglas para la interacción en lenguaje natural** con un sitio web. Envía respuestas en formato JSON (a menudo usando Schema.org). Su propósito es crear una base simple para la “Web de IA”, de la misma forma que HTML hizo posible compartir documentos en línea.

- **Servidor MCP (Endpoint del Model Context Protocol)**: Cada configuración NLWeb también funciona como un **servidor MCP**. Esto significa que puede **compartir herramientas (como un método “ask”) y datos** con otros sistemas de IA. En la práctica, esto hace que el contenido y las capacidades del sitio web sean utilizables por agentes de IA, permitiendo que el sitio forme parte del “ecosistema de agentes” más amplio.

- **Modelos de Embedding**: Estos modelos se usan para **convertir el contenido del sitio web en representaciones numéricas llamadas vectores** (embeddings). Estos vectores capturan significado de una manera que las computadoras pueden comparar y buscar. Se almacenan en una base de datos especial, y los usuarios pueden elegir qué modelo de embedding desean usar.

- **Base de Datos Vectorial (Mecanismo de Recuperación)**: Esta base de datos **almacena los embeddings del contenido del sitio web**. Cuando alguien hace una pregunta, NLWeb consulta la base de datos vectorial para encontrar rápidamente la información más relevante. Proporciona una lista rápida de posibles respuestas, clasificadas por similitud. NLWeb funciona con diferentes sistemas de almacenamiento vectorial como Qdrant, Snowflake, Milvus, Azure AI Search y Elasticsearch.

### NLWeb por Ejemplo

![NLWeb](../../../translated_images/es/nlweb-diagram.c1e2390b310e5fe4.webp)

Considera nuevamente nuestro sitio web de reservas de viajes, pero esta vez está impulsado por NLWeb.

1. **Ingesta de Datos**: Los catálogos de productos existentes del sitio de viajes (por ejemplo, listados de vuelos, descripciones de hoteles, paquetes turísticos) se formatean usando Schema.org o se cargan vía feeds RSS. Las herramientas de NLWeb ingieren estos datos estructurados, crean embeddings y los almacenan en una base de datos vectorial local o remota.

2. **Consulta en Lenguaje Natural (Humano)**: Un usuario visita el sitio y, en lugar de navegar por menús, escribe en una interfaz de chat: "Encuéntrame un hotel para familias en Honolulu con piscina para la próxima semana".

3. **Procesamiento NLWeb**: La aplicación NLWeb recibe esta consulta. Envía la consulta a un LLM para comprensión y simultáneamente busca en su base de datos vectorial listados de hoteles relevantes.

4. **Resultados Precisos**: El LLM ayuda a interpretar los resultados de búsqueda de la base de datos, identifica las mejores coincidencias basadas en los criterios "para familias", "piscina" y "Honolulu", y luego formatea una respuesta en lenguaje natural. Crucialmente, la respuesta hace referencia a hoteles reales del catálogo del sitio web, evitando información inventada.

5. **Interacción con Agentes de IA**: Como NLWeb funciona como un servidor MCP, un agente de viaje externo de IA también podría conectarse a esta instancia NLWeb del sitio. El agente IA podría usar entonces el método `ask` de MCP para consultar directamente el sitio web: `ask("¿Hay restaurantes veganos en la zona de Honolulu recomendados por el hotel?")`. La instancia NLWeb procesaría esto, usando su base de datos de información sobre restaurantes (si está cargada), y devolvería una respuesta JSON estructurada.

### ¿Tienes Más Preguntas sobre MCP/A2A/NLWeb?

Únete al [Discord de Microsoft Foundry](https://discord.com/invite/ATgtXmAS5D) para encontrarte con otros aprendices, asistir a horas de oficina y resolver tus preguntas sobre Agentes de IA.

## Recursos

- [MCP para Principiantes](https://aka.ms/mcp-for-beginners)  
- [Documentación MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositorio NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->