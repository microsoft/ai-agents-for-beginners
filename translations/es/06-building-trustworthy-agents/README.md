<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c069d7ff0feca3027f88819355866ca1",
  "translation_date": "2025-03-28T10:28:22+00:00",
  "source_file": "06-building-trustworthy-agents\\README.md",
  "language_code": "es"
}
-->
[![Agentes de IA Confiables](../../../translated_images/lesson-6-thumbnail.74ea485dbd9a9c3fb4c749f30f2b8130d025072b4d7d911c6f540eac5a78e6b8.es.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Creando Agentes de IA Confiables

## Introducción

Esta lección cubrirá:

- Cómo construir y desplegar agentes de IA seguros y efectivos.
- Consideraciones importantes de seguridad al desarrollar agentes de IA.
- Cómo mantener la privacidad de los datos y de los usuarios al desarrollar agentes de IA.

## Objetivos de Aprendizaje

Al completar esta lección, sabrás cómo:

- Identificar y mitigar riesgos al crear agentes de IA.
- Implementar medidas de seguridad para garantizar que los datos y el acceso estén debidamente gestionados.
- Crear agentes de IA que mantengan la privacidad de los datos y ofrezcan una experiencia de usuario de calidad.

## Seguridad

Primero, veamos cómo construir aplicaciones agenticas seguras. La seguridad significa que el agente de IA funciona según lo diseñado. Como desarrolladores de aplicaciones agenticas, tenemos métodos y herramientas para maximizar la seguridad:

### Construcción de un Marco de Mensajes del Sistema

Si alguna vez has construido una aplicación de IA utilizando Modelos de Lenguaje Extensos (LLMs), sabes la importancia de diseñar un mensaje del sistema robusto. Estos mensajes establecen las reglas, instrucciones y directrices para cómo el LLM interactuará con el usuario y los datos.

Para los agentes de IA, el mensaje del sistema es aún más importante, ya que los agentes necesitan instrucciones altamente específicas para completar las tareas que hemos diseñado para ellos.

Para crear mensajes del sistema escalables, podemos usar un marco de mensajes del sistema para construir uno o más agentes en nuestra aplicación:

![Construcción de un Marco de Mensajes del Sistema](../../../translated_images/system-message-framework.9df67f3d863520cd48878f71a1289740d8cb46e9d63ee065090ccf3b9b6b82a1.es.png)

#### Paso 1: Crear un Meta Mensaje del Sistema

El meta mensaje será utilizado por un LLM para generar los mensajes del sistema para los agentes que creemos. Lo diseñamos como una plantilla para que podamos crear múltiples agentes de manera eficiente si es necesario.

Aquí tienes un ejemplo de un meta mensaje del sistema que le daríamos al LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Paso 2: Crear un mensaje básico

El siguiente paso es crear un mensaje básico para describir al agente de IA. Debes incluir el rol del agente, las tareas que completará y cualquier otra responsabilidad del agente.

Aquí tienes un ejemplo:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Paso 3: Proporcionar el Mensaje Básico al LLM

Ahora podemos optimizar este mensaje del sistema proporcionando el meta mensaje del sistema como el mensaje del sistema y nuestro mensaje básico.

Esto producirá un mensaje del sistema mejor diseñado para guiar a nuestros agentes de IA:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Paso 4: Iterar y Mejorar

El valor de este marco de mensajes del sistema radica en poder escalar la creación de mensajes del sistema para múltiples agentes, así como mejorar tus mensajes del sistema con el tiempo. Es raro que tengas un mensaje del sistema que funcione perfectamente la primera vez para tu caso de uso completo. Poder realizar pequeños ajustes y mejoras cambiando el mensaje básico y ejecutándolo a través del sistema te permitirá comparar y evaluar resultados.

## Comprendiendo las Amenazas

Para construir agentes de IA confiables, es importante entender y mitigar los riesgos y amenazas hacia tu agente de IA. Veamos algunas de las diferentes amenazas a los agentes de IA y cómo puedes planificar y prepararte mejor para ellas.

![Comprendiendo las Amenazas](../../../translated_images/understanding-threats.f8fbe6fe11e025b3085fc91e82d975937ad1d672260a2aeed40458aa41798d0e.es.png)

### Tareas e Instrucciones

**Descripción:** Los atacantes intentan cambiar las instrucciones o metas del agente de IA mediante mensajes o manipulando entradas.

**Mitigación:** Realiza verificaciones de validación y filtros de entrada para detectar mensajes potencialmente peligrosos antes de que sean procesados por el agente de IA. Dado que estos ataques generalmente requieren interacción frecuente con el agente, limitar el número de turnos en una conversación es otra forma de prevenir este tipo de ataques.

### Acceso a Sistemas Críticos

**Descripción:** Si un agente de IA tiene acceso a sistemas y servicios que almacenan datos sensibles, los atacantes pueden comprometer la comunicación entre el agente y estos servicios. Estos pueden ser ataques directos o intentos indirectos de obtener información sobre estos sistemas a través del agente.

**Mitigación:** Los agentes de IA solo deben tener acceso a sistemas cuando sea absolutamente necesario para prevenir este tipo de ataques. La comunicación entre el agente y los sistemas debe ser segura. Implementar autenticación y control de acceso es otra forma de proteger esta información.

### Sobrecarga de Recursos y Servicios

**Descripción:** Los agentes de IA pueden acceder a diferentes herramientas y servicios para completar tareas. Los atacantes pueden usar esta capacidad para atacar estos servicios enviando un gran volumen de solicitudes a través del agente de IA, lo que puede resultar en fallos del sistema o altos costos.

**Mitigación:** Implementa políticas para limitar la cantidad de solicitudes que un agente de IA puede realizar a un servicio. Limitar el número de turnos de conversación y solicitudes a tu agente de IA es otra forma de prevenir este tipo de ataques.

### Envenenamiento de la Base de Conocimientos

**Descripción:** Este tipo de ataque no se dirige directamente al agente de IA, sino a la base de conocimientos y otros servicios que el agente de IA utilizará. Esto podría implicar corromper los datos o la información que el agente de IA utilizará para completar una tarea, lo que lleva a respuestas sesgadas o no intencionadas al usuario.

**Mitigación:** Realiza verificaciones regulares de los datos que el agente de IA utilizará en sus flujos de trabajo. Asegúrate de que el acceso a estos datos sea seguro y solo pueda ser modificado por personas de confianza para evitar este tipo de ataque.

### Errores en Cascada

**Descripción:** Los agentes de IA acceden a varias herramientas y servicios para completar tareas. Los errores causados por atacantes pueden provocar fallos en otros sistemas a los que el agente de IA está conectado, haciendo que el ataque sea más generalizado y difícil de solucionar.

**Mitigación:** Una forma de evitar esto es hacer que el agente de IA opere en un entorno limitado, como realizar tareas en un contenedor Docker, para prevenir ataques directos al sistema. Crear mecanismos de respaldo y lógica de reintento cuando ciertos sistemas respondan con un error es otra forma de evitar fallos más grandes en el sistema.

## Humano-en-el-Bucle

Otra forma efectiva de construir sistemas de agentes de IA confiables es usando un humano-en-el-bucle. Esto crea un flujo donde los usuarios pueden proporcionar retroalimentación a los agentes durante su ejecución. Los usuarios esencialmente actúan como agentes en un sistema multiagente, proporcionando aprobación o terminación del proceso en ejecución.

![Humano en el Bucle](../../../translated_images/human-in-the-loop.e9edbe8f6d42041b4213421410823250aa750fe8bdba5601d69ed46f3ff6489d.es.png)

Aquí tienes un fragmento de código usando AutoGen para mostrar cómo se implementa este concepto:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Conclusión

Construir agentes de IA confiables requiere un diseño cuidadoso, medidas de seguridad robustas y una iteración continua. Al implementar sistemas estructurados de meta mensajes, comprender las amenazas potenciales y aplicar estrategias de mitigación, los desarrolladores pueden crear agentes de IA que sean seguros y efectivos. Además, incorporar un enfoque de humano-en-el-bucle asegura que los agentes de IA se mantengan alineados con las necesidades del usuario mientras se minimizan los riesgos. A medida que la IA sigue evolucionando, mantener una postura proactiva sobre seguridad, privacidad y consideraciones éticas será clave para fomentar la confianza y la fiabilidad en los sistemas impulsados por IA.

## Recursos Adicionales

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Resumen de IA Responsable</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluación de modelos de IA generativa y aplicaciones de IA</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mensajes de sistema de seguridad</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Plantilla de Evaluación de Riesgos</a>

## Lección Anterior

[Agentic RAG](../05-agentic-rag/README.md)

## Próxima Lección

[Patrón de Diseño de Planificación](../07-planning-design/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.