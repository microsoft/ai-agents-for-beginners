<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-30T13:12:35+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "es"
}
-->
[![Agentes de IA Confiables](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.es.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Construcción de Agentes de IA Confiables

## Introducción

Esta lección cubrirá:

- Cómo construir y desplegar agentes de IA seguros y efectivos.
- Consideraciones importantes de seguridad al desarrollar agentes de IA.
- Cómo mantener la privacidad de los datos y los usuarios al desarrollar agentes de IA.

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo:

- Identificar y mitigar riesgos al crear agentes de IA.
- Implementar medidas de seguridad para garantizar que los datos y el acceso estén correctamente gestionados.
- Crear agentes de IA que mantengan la privacidad de los datos y ofrezcan una experiencia de usuario de calidad.

## Seguridad

Primero, veamos cómo construir aplicaciones agentivas seguras. La seguridad significa que el agente de IA funciona según lo diseñado. Como desarrolladores de aplicaciones agentivas, tenemos métodos y herramientas para maximizar la seguridad:

### Construcción de un Marco de Mensajes del Sistema

Si alguna vez has construido una aplicación de IA utilizando Modelos de Lenguaje Extensos (LLMs), sabes la importancia de diseñar un mensaje del sistema robusto. Estos mensajes establecen las reglas meta, instrucciones y pautas sobre cómo el LLM interactuará con el usuario y los datos.

Para los agentes de IA, el mensaje del sistema es aún más importante, ya que los agentes de IA necesitarán instrucciones altamente específicas para completar las tareas que hemos diseñado para ellos.

Para crear mensajes del sistema escalables, podemos usar un marco de mensajes del sistema para construir uno o más agentes en nuestra aplicación:

![Construcción de un Marco de Mensajes del Sistema](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.es.png)

#### Paso 1: Crear un Mensaje Meta del Sistema

El mensaje meta será utilizado por un LLM para generar los mensajes del sistema para los agentes que creemos. Lo diseñamos como una plantilla para que podamos crear múltiples agentes de manera eficiente si es necesario.

Aquí hay un ejemplo de un mensaje meta del sistema que daríamos al LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Paso 2: Crear un mensaje básico

El siguiente paso es crear un mensaje básico para describir al agente de IA. Debes incluir el rol del agente, las tareas que completará y cualquier otra responsabilidad del agente.

Aquí hay un ejemplo:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Paso 3: Proporcionar el Mensaje Básico del Sistema al LLM

Ahora podemos optimizar este mensaje del sistema proporcionando el mensaje meta del sistema como el mensaje del sistema y nuestro mensaje básico del sistema.

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

El valor de este marco de mensajes del sistema es poder escalar la creación de mensajes del sistema para múltiples agentes de manera más fácil, así como mejorar tus mensajes del sistema con el tiempo. Es raro que tengas un mensaje del sistema que funcione perfectamente la primera vez para tu caso de uso completo. Poder hacer pequeños ajustes y mejoras cambiando el mensaje básico del sistema y ejecutándolo a través del sistema te permitirá comparar y evaluar resultados.

## Comprensión de Amenazas

Para construir agentes de IA confiables, es importante comprender y mitigar los riesgos y amenazas para tu agente de IA. Veamos algunas de las diferentes amenazas para los agentes de IA y cómo puedes planificar y prepararte mejor para ellas.

![Comprensión de Amenazas](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.es.png)

### Tarea e Instrucción

**Descripción:** Los atacantes intentan cambiar las instrucciones o metas del agente de IA mediante el uso de prompts o manipulando entradas.

**Mitigación**: Ejecuta verificaciones de validación y filtros de entrada para detectar prompts potencialmente peligrosos antes de que sean procesados por el agente de IA. Dado que estos ataques generalmente requieren interacción frecuente con el agente, limitar el número de turnos en una conversación es otra forma de prevenir este tipo de ataques.

### Acceso a Sistemas Críticos

**Descripción**: Si un agente de IA tiene acceso a sistemas y servicios que almacenan datos sensibles, los atacantes pueden comprometer la comunicación entre el agente y estos servicios. Estos pueden ser ataques directos o intentos indirectos de obtener información sobre estos sistemas a través del agente.

**Mitigación**: Los agentes de IA deben tener acceso a sistemas solo cuando sea necesario para prevenir este tipo de ataques. La comunicación entre el agente y el sistema también debe ser segura. Implementar autenticación y control de acceso es otra forma de proteger esta información.

### Sobrecarga de Recursos y Servicios

**Descripción:** Los agentes de IA pueden acceder a diferentes herramientas y servicios para completar tareas. Los atacantes pueden usar esta capacidad para atacar estos servicios enviando un alto volumen de solicitudes a través del agente de IA, lo que puede resultar en fallos del sistema o altos costos.

**Mitigación:** Implementa políticas para limitar el número de solicitudes que un agente de IA puede hacer a un servicio. Limitar el número de turnos de conversación y solicitudes a tu agente de IA es otra forma de prevenir este tipo de ataques.

### Envenenamiento de la Base de Conocimientos

**Descripción:** Este tipo de ataque no se dirige directamente al agente de IA, sino a la base de conocimientos y otros servicios que el agente de IA utilizará. Esto podría implicar corromper los datos o información que el agente de IA utilizará para completar una tarea, lo que lleva a respuestas sesgadas o no deseadas para el usuario.

**Mitigación:** Realiza verificaciones regulares de los datos que el agente de IA utilizará en sus flujos de trabajo. Asegúrate de que el acceso a estos datos sea seguro y solo modificado por personas de confianza para evitar este tipo de ataque.

### Errores en Cascada

**Descripción:** Los agentes de IA acceden a diversas herramientas y servicios para completar tareas. Los errores causados por atacantes pueden provocar fallos en otros sistemas a los que el agente de IA está conectado, haciendo que el ataque sea más generalizado y difícil de solucionar.

**Mitigación**: Una forma de evitar esto es hacer que el agente de IA opere en un entorno limitado, como realizar tareas en un contenedor Docker, para prevenir ataques directos al sistema. Crear mecanismos de respaldo y lógica de reintento cuando ciertos sistemas respondan con un error es otra forma de prevenir fallos más grandes en el sistema.

## Humano en el Bucle

Otra forma efectiva de construir sistemas de agentes de IA confiables es utilizando un humano en el bucle. Esto crea un flujo donde los usuarios pueden proporcionar retroalimentación a los agentes durante la ejecución. Los usuarios esencialmente actúan como agentes en un sistema multiagente al proporcionar aprobación o terminación del proceso en ejecución.

![Humano en el Bucle](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.es.png)

Aquí hay un fragmento de código usando AutoGen para mostrar cómo se implementa este concepto:

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

Construir agentes de IA confiables requiere un diseño cuidadoso, medidas de seguridad robustas y una iteración continua. Al implementar sistemas estructurados de meta prompts, comprender las amenazas potenciales y aplicar estrategias de mitigación, los desarrolladores pueden crear agentes de IA que sean seguros y efectivos. Además, incorporar un enfoque de humano en el bucle asegura que los agentes de IA permanezcan alineados con las necesidades del usuario mientras se minimizan los riesgos. A medida que la IA continúa evolucionando, mantener una postura proactiva sobre seguridad, privacidad y consideraciones éticas será clave para fomentar la confianza y la fiabilidad en los sistemas impulsados por IA.

### ¿Tienes más preguntas sobre la construcción de agentes de IA confiables?

Únete al [Discord de Azure AI Foundry](https://aka.ms/ai-agents/discord) para conectarte con otros estudiantes, asistir a horas de oficina y resolver tus dudas sobre agentes de IA.

## Recursos Adicionales

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Descripción general de IA responsable</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluación de modelos de IA generativa y aplicaciones de IA</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mensajes del sistema de seguridad</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Plantilla de Evaluación de Riesgos</a>

## Lección Anterior

[Agentic RAG](../05-agentic-rag/README.md)

## Próxima Lección

[Patrón de Diseño de Planificación](../07-planning-design/README.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.