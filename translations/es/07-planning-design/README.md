[![Planning Design Pattern](../../../translated_images/es/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Diseño de Planificación

## Introducción

Esta lección cubrirá

* Definir un objetivo general claro y desglosar una tarea compleja en tareas manejables.
* Aprovechar la salida estructurada para obtener respuestas más confiables y legibles por máquina.
* Aplicar un enfoque basado en eventos para manejar tareas dinámicas y entradas inesperadas.

## Objetivos de Aprendizaje

Después de completar esta lección, tendrás comprensión sobre:

* Identificar y establecer un objetivo general para un agente de IA, asegurando que sepa claramente qué debe lograrse.
* Descomponer una tarea compleja en subtareas manejables y organizarlas en una secuencia lógica.
* Dotar a los agentes con las herramientas adecuadas (p. ej., herramientas de búsqueda o análisis de datos), decidir cuándo y cómo se usan, y manejar situaciones inesperadas que surjan.
* Evaluar los resultados de las subtareas, medir el rendimiento e iterar sobre las acciones para mejorar el resultado final.

## Definir el Objetivo General y Desglosar una Tarea

![Defining Goals and Tasks](../../../translated_images/es/defining-goals-tasks.d70439e19e37c47a.webp)

La mayoría de las tareas del mundo real son demasiado complejas como para abordarlas en un solo paso. Un agente de IA necesita un objetivo conciso para guiar su planificación y acciones. Por ejemplo, considera el objetivo:

    "Generar un itinerario de viaje de 3 días."

Aunque es simple de enunciar, aún necesita refinamiento. Cuanto más claro sea el objetivo, mejor podrá el agente (y cualquier colaborador humano) enfocarse en lograr el resultado correcto, como crear un itinerario completo con opciones de vuelos, recomendaciones de hoteles y sugerencias de actividades.

### Descomposición de Tareas

Las tareas grandes o complejas se vuelven más manejables cuando se dividen en subtareas más pequeñas orientadas a objetivos.  
Para el ejemplo del itinerario de viaje, podrías descomponer el objetivo en:

* Reserva de Vuelo
* Reserva de Hotel
* Alquiler de Auto
* Personalización

Cada subtarea puede luego ser abordada por agentes o procesos dedicados. Un agente podría especializarse en buscar las mejores ofertas de vuelo, otro enfocarse en reservas de hotel, y así sucesivamente. Un agente coordinador o "posterior" puede luego compilar estos resultados en un itinerario cohesivo para el usuario final.

Este enfoque modular también permite mejoras incrementales. Por ejemplo, podrías añadir agentes especializados en Recomendaciones de Comida o Sugerencias de Actividades Locales y refinar el itinerario con el tiempo.

### Salida estructurada

Los Modelos de Lenguaje a Gran Escala (LLMs) pueden generar salidas estructuradas (por ejemplo, JSON) que son más fáciles de analizar y procesar para agentes o servicios posteriores. Esto es especialmente útil en un contexto multi-agente, donde podemos ejecutar estas tareas después de recibir la salida de la planificación.

El siguiente fragmento en Python demuestra un agente de planificación simple descomponiendo un objetivo en subtareas y generando un plan estructurado:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Modelo de Subtarea de Viaje
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # queremos asignar la tarea al agente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Definir el mensaje del usuario
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### Agente de Planificación con Orquestación Multi-Agente

En este ejemplo, un Agente Enrutador Semántico recibe una solicitud del usuario (por ejemplo, "Necesito un plan de hotel para mi viaje.").

El planificador luego:

* Recibe el Plan de Hotel: El planificador toma el mensaje del usuario y, basándose en un prompt de sistema (incluyendo detalles de agentes disponibles), genera un plan de viaje estructurado.
* Lista Agentes y Sus Herramientas: El registro de agentes contiene una lista de agentes (por ejemplo, para vuelo, hotel, alquiler de auto y actividades) junto con las funciones o herramientas que ofrecen.
* Enruta el Plan a los Agentes Respectivos: Dependiendo del número de subtareas, el planificador envía el mensaje directamente a un agente dedicado (para escenarios de una sola tarea) o coordina a través de un gestor de chat grupal para colaboración multi-agente.
* Resume el Resultado: Finalmente, el planificador resume el plan generado para mayor claridad.  
El siguiente ejemplo de código en Python ilustra estos pasos:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Modelo de subtarea de viaje

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # queremos asignar la tarea al agente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Crear el cliente

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definir el mensaje del usuario

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# Imprimir el contenido de la respuesta después de cargarlo como JSON

pprint(json.loads(response_content))
```

Lo que sigue es la salida del código anterior y puedes usar esta salida estructurada para enrutar a `assigned_agent` y resumir el plan de viaje para el usuario final.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Un ejemplo de cuaderno con el código anterior está disponible [aquí](07-python-agent-framework.ipynb).

### Planificación Iterativa

Algunas tareas requieren un ir y venir o replanificación, donde el resultado de una subtarea influye en la siguiente. Por ejemplo, si el agente descubre un formato de dato inesperado al reservar vuelos, podría necesitar adaptar su estrategia antes de continuar con las reservas de hotel.

Además, la retroalimentación del usuario (p. ej., una persona que decide que prefiere un vuelo más temprano) puede activar una replanteación parcial. Este enfoque dinámico e iterativo asegura que la solución final se alinee con las restricciones del mundo real y las preferencias cambiantes del usuario.

ejemplo de código

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. igual que el código anterior y pasar el historial del usuario, el plan actual

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. replanificar y enviar las tareas a los agentes respectivos
```

Para una planificación más completa, revisa Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> para resolver tareas complejas.

## Resumen

En este artículo hemos visto un ejemplo de cómo podemos crear un planificador que puede seleccionar dinámicamente los agentes disponibles definidos. La salida del Planificador descompone las tareas y asigna los agentes para que puedan ser ejecutadas. Se asume que los agentes tienen acceso a las funciones/herramientas necesarias para realizar la tarea. Además de los agentes, puedes incluir otros patrones como reflexión, resumidor y chat round robin para personalizar aún más.

## Recursos Adicionales

Magentic One - Un sistema multi-agente generalista para resolver tareas complejas y que ha logrado resultados impresionantes en múltiples benchmarks agenticos desafiantes. Referencia: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. En esta implementación, el orquestador crea planes específicos para tareas y delega estas tareas a los agentes disponibles. Además de planificar, el orquestador emplea un mecanismo de seguimiento para monitorear el progreso de la tarea y replanificar según sea necesario.

### ¿Tienes Más Preguntas sobre el Patrón de Diseño de Planificación?

Únete al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrarte con otros aprendices, asistir a horas de oficina y resolver tus preguntas sobre Agentes de IA.

## Lección Anterior

[Construcción de Agentes de IA Confiables](../06-building-trustworthy-agents/README.md)

## Próxima Lección

[Patrón de Diseño Multi-Agente](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente oficial. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->