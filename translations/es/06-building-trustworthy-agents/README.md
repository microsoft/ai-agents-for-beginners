[![Agentes de IA Confiables](../../../translated_images/es/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Construyendo Agentes de IA Confiables

## Introducción

Esta lección cubrirá:

- Cómo construir y desplegar agentes de IA seguros y efectivos
- Consideraciones importantes de seguridad al desarrollar agentes de IA.
- Cómo mantener la privacidad de los datos y usuarios al desarrollar agentes de IA.

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás cómo:

- Identificar y mitigar riesgos al crear agentes de IA.
- Implementar medidas de seguridad para asegurar que los datos y accesos estén bien gestionados.
- Crear agentes de IA que mantengan la privacidad de los datos y brinden una experiencia de usuario de calidad.

## Seguridad

Primero veamos cómo construir aplicaciones agenticas seguras. Seguridad significa que el agente de IA funciona según lo diseñado. Como constructores de aplicaciones agenticas, contamos con métodos y herramientas para maximizar la seguridad:

### Construyendo un Marco de Mensajes de Sistema

Si alguna vez has construido una aplicación de IA usando modelos de lenguaje grande (LLMs), conoces la importancia de diseñar un prompt o mensaje de sistema robusto. Estos prompts establecen las reglas meta, instrucciones y directrices sobre cómo el LLM interactuará con el usuario y los datos.

Para los agentes de IA, el prompt del sistema es aún más importante ya que los agentes de IA necesitarán instrucciones altamente específicas para completar las tareas que hemos diseñado para ellos.

Para crear prompts de sistema escalables, podemos usar un marco de mensajes de sistema para construir uno o varios agentes en nuestra aplicación:

![Construyendo un Marco de Mensajes de Sistema](../../../translated_images/es/system-message-framework.3a97368c92d11d68.webp)

#### Paso 1: Crear un Mensaje de Sistema Meta

El prompt meta será usado por un LLM para generar los mensajes de sistema para los agentes que creamos. Lo diseñamos como una plantilla para poder crear múltiples agentes de manera eficiente si es necesario.

Aquí hay un ejemplo de un mensaje de sistema meta que le daríamos al LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Paso 2: Crear un prompt básico

El siguiente paso es crear un prompt básico para describir el agente de IA. Debes incluir el rol del agente, las tareas que el agente completará y cualquier otra responsabilidad del agente.

Aquí hay un ejemplo:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Paso 3: Proporcionar el Mensaje Básico de Sistema al LLM

Ahora podemos optimizar este mensaje de sistema proporcionando el mensaje de sistema meta como mensaje de sistema y nuestro mensaje básico de sistema.

Esto producirá un mensaje de sistema mejor diseñado para guiar a nuestros agentes de IA:

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

El valor de este marco de mensajes de sistema es poder escalar la creación de mensajes de sistema de múltiples agentes más fácilmente, así como mejorar tus mensajes de sistema con el tiempo. Es raro que tengas un mensaje de sistema que funcione a la primera para tu caso de uso completo. Poder hacer pequeños ajustes y mejoras cambiando el mensaje básico del sistema y ejecutándolo a través del sistema te permitirá comparar y evaluar resultados.

## Entendiendo las Amenazas

Para construir agentes de IA confiables, es importante entender y mitigar los riesgos y amenazas hacia tu agente de IA. Veamos solo algunas de las diferentes amenazas para agentes de IA y cómo puedes planificar y prepararte mejor para ellas.

![Entendiendo las Amenazas](../../../translated_images/es/understanding-threats.89edeada8a97fc0f.webp)

### Tarea e Instrucción

**Descripción:** Los atacantes intentan cambiar las instrucciones o metas del agente de IA mediante prompting o manipulando las entradas.

**Mitigación**: Ejecuta verificaciones de validación y filtros de entrada para detectar prompts potencialmente peligrosos antes que sean procesados por el agente de IA. Ya que estos ataques suelen requerir interacción frecuente con el agente, limitar el número de turnos en una conversación es otra forma de prevenir estos tipos de ataques.

### Acceso a Sistemas Críticos

**Descripción**: Si un agente de IA tiene acceso a sistemas y servicios que almacenan datos sensibles, los atacantes pueden comprometer la comunicación entre el agente y estos servicios. Estos pueden ser ataques directos o intentos indirectos de obtener información sobre estos sistemas a través del agente.

**Mitigación**: Los agentes de IA deben tener acceso a sistemas solo cuando sea necesario para prevenir estos tipos de ataques. La comunicación entre el agente y el sistema también debe ser segura. Implementar autenticación y control de acceso es otra forma de proteger esta información.

### Sobrecarga de Recursos y Servicios

**Descripción:** Los agentes de IA pueden acceder a diferentes herramientas y servicios para completar tareas. Los atacantes pueden usar esta capacidad para atacar estos servicios enviando un alto volumen de solicitudes a través del agente de IA, lo que puede provocar fallos en el sistema o costos elevados.

**Mitigación:** Implementa políticas para limitar el número de solicitudes que un agente de IA pueda hacer a un servicio. Limitar el número de turnos en la conversación y solicitudes a tu agente de IA es otra forma de prevenir estos tipos de ataques.

### Envenenamiento de Base de Conocimiento

**Descripción:** Este tipo de ataque no se dirige directamente al agente de IA, sino a la base de conocimiento y otros servicios que el agente de IA usará. Esto podría involucrar corromper los datos o información que el agente de IA utilizará para completar una tarea, produciendo respuestas sesgadas o no deseadas para el usuario.

**Mitigación:** Realiza verificaciones regulares de los datos que el agente de IA usará en sus flujos de trabajo. Asegura que el acceso a estos datos sea seguro y solo modificado por personas de confianza para evitar este tipo de ataques.

### Errores en Cascada

**Descripción:** Los agentes de IA acceden a diversas herramientas y servicios para completar tareas. Los errores causados por atacantes pueden llevar a fallos en otros sistemas conectados con el agente de IA, haciendo que el ataque se extienda y sea más difícil de solucionar.

**Mitigación**: Un método para evitar esto es hacer que el agente de IA opere en un ambiente limitado, como realizar tareas en un contenedor Docker, para prevenir ataques directos al sistema. Crear mecanismos de respaldo y lógica de reintentos cuando ciertos sistemas responden con errores es otra forma de prevenir fallos mayores en el sistema.

## Humano en el Bucle

Otra forma efectiva de construir sistemas de agentes de IA confiables es utilizando un Humano en el bucle. Esto crea un flujo donde los usuarios pueden proporcionar retroalimentación a los agentes durante la ejecución. Los usuarios actúan esencialmente como agentes en un sistema multiagente, aprobando o terminando el proceso en ejecución.

![Humano en el Bucle](../../../translated_images/es/human-in-the-loop.5f0068a678f62f4f.webp)

Aquí hay un extracto de código usando el Microsoft Agent Framework para mostrar cómo se implementa este concepto:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Crear el proveedor con aprobación humana activa
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Crear el agente con un paso de aprobación humana
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# El usuario puede revisar y aprobar la respuesta
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusión

Construir agentes de IA confiables requiere un diseño cuidadoso, medidas de seguridad robustas y una iteración continua. Al implementar sistemas estructurados de meta-prompts, entender las amenazas potenciales y aplicar estrategias de mitigación, los desarrolladores pueden crear agentes de IA que sean seguros y efectivos. Además, incorporar un enfoque de humano en el bucle asegura que los agentes de IA permanezcan alineados con las necesidades del usuario mientras se minimizan los riesgos. A medida que la IA continúa evolucionando, mantener una postura proactiva sobre seguridad, privacidad y consideraciones éticas será clave para fomentar la confianza y confiabilidad en sistemas impulsados por IA.

## Ejemplos de Código

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demostración paso a paso del marco de mensajes de sistema meta-prompt.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Puertas de aprobación previa a la acción, categorización de riesgos y registros de auditoría para agentes confiables.

### ¿Tienes más preguntas sobre cómo construir agentes de IA confiables?

Únete al [Discord de Microsoft Foundry](https://discord.com/invite/ATgtXmAS5D) para conocer a otros estudiantes, asistir a horas de oficina y obtener respuestas a tus preguntas sobre agentes de IA.

## Recursos Adicionales

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Resumen de IA Responsable</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluación de modelos de IA generativa y aplicaciones de IA</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mensajes de sistema para seguridad</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Plantilla de Evaluación de Riesgos</a>

## Lección Anterior

[Agentic RAG](../05-agentic-rag/README.md)

## Próxima Lección

[Patrón de Diseño de Planificación](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->