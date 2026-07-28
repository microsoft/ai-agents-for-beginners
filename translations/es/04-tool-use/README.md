[![Cómo diseñar buenos agentes de IA](../../../translated_images/es/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Patrón de diseño de uso de herramientas

Las herramientas son interesantes porque permiten que los agentes de IA tengan un rango más amplio de capacidades. En lugar de que el agente tenga un conjunto limitado de acciones que puede realizar, al añadir una herramienta, el agente puede ahora ejecutar una amplia variedad de acciones. En este capítulo, veremos el Patrón de Diseño de Uso de Herramientas, que describe cómo los agentes de IA pueden usar herramientas específicas para alcanzar sus objetivos.

## Introducción

En esta lección, buscamos responder las siguientes preguntas:

- ¿Qué es el patrón de diseño de uso de herramientas?
- ¿Cuáles son los casos de uso en los que puede aplicarse?
- ¿Cuáles son los elementos/bloques de construcción necesarios para implementar el patrón de diseño?
- ¿Cuáles son las consideraciones especiales para usar el Patrón de Uso de Herramientas para construir agentes de IA confiables?

## Objetivos de aprendizaje

Después de completar esta lección, podrás:

- Definir el Patrón de Diseño de Uso de Herramientas y su propósito.
- Identificar casos de uso donde el Patrón de Diseño de Uso de Herramientas es aplicable.
- Comprender los elementos clave necesarios para implementar el patrón de diseño.
- Reconocer consideraciones para asegurar la confiabilidad en agentes de IA que usan este patrón de diseño.

## ¿Qué es el Patrón de Diseño de Uso de Herramientas?

El **Patrón de Diseño de Uso de Herramientas** se enfoca en dar a los LLM la capacidad de interactuar con herramientas externas para lograr objetivos específicos. Las herramientas son códigos que pueden ser ejecutados por un agente para realizar acciones. Una herramienta puede ser una función simple como una calculadora, o una llamada API a un servicio externo como consulta de precios de acciones o pronóstico del clima. En el contexto de agentes de IA, las herramientas están diseñadas para ser ejecutadas por agentes en respuesta a **llamadas a funciones generadas por el modelo**.

## ¿Cuáles son los casos de uso en los que puede aplicarse?

Los agentes de IA pueden aprovechar herramientas para completar tareas complejas, recuperar información o tomar decisiones. El patrón de diseño de uso de herramientas se emplea a menudo en escenarios que requieren interacción dinámica con sistemas externos, como bases de datos, servicios web o intérpretes de código. Esta capacidad es útil para varios casos de uso, incluyendo:

- **Recuperación dinámica de información:** Los agentes pueden consultar APIs externas o bases de datos para obtener datos actualizados (por ejemplo, consultar una base de datos SQLite para análisis de datos, obtener precios de acciones o información meteorológica).
- **Ejecución e interpretación de código:** Los agentes pueden ejecutar código o scripts para resolver problemas matemáticos, generar informes o realizar simulaciones.
- **Automatización de flujos de trabajo:** Automatizar flujos de trabajo repetitivos o de múltiples pasos integrando herramientas como planificadores de tareas, servicios de correo electrónico o pipelines de datos.
- **Soporte al cliente:** Los agentes pueden interactuar con sistemas CRM, plataformas de tickets o bases de conocimiento para resolver consultas de usuarios.
- **Generación y edición de contenido:** Los agentes pueden aprovechar herramientas como correctores gramaticales, resumidores de texto o evaluadores de seguridad de contenido para ayudar en tareas de creación de contenido.

## ¿Cuáles son los elementos/bloques de construcción necesarios para implementar el patrón de diseño de uso de herramientas?

Estos bloques de construcción permiten que el agente de IA realice una amplia variedad de tareas. Veamos los elementos clave para implementar el Patrón de Diseño de Uso de Herramientas:

- **Esquemas de Funciones/Herramientas**: Definiciones detalladas de las herramientas disponibles, incluyendo nombre de la función, propósito, parámetros requeridos y salidas esperadas. Estos esquemas permiten que el LLM entienda qué herramientas hay disponibles y cómo construir solicitudes válidas.

- **Lógica de Ejecución de Funciones**: Regula cómo y cuándo se invocan las herramientas basado en la intención del usuario y el contexto de la conversación. Esto puede incluir módulos de planificación, mecanismos de enrutamiento o flujos condicionales que determinan el uso dinámico de herramientas.

- **Sistema de Manejo de Mensajes**: Componentes que gestionan el flujo conversacional entre entradas del usuario, respuestas del LLM, llamadas a herramientas y salidas de las herramientas.

- **Marco de Integración de Herramientas**: Infraestructura que conecta al agente con diversas herramientas, ya sean funciones simples o servicios externos complejos.

- **Manejo de Errores y Validación**: Mecanismos para gestionar fallos en la ejecución de herramientas, validar parámetros y manejar respuestas inesperadas.

- **Gestión de Estado**: Rastrea el contexto de la conversación, interacciones previas con herramientas y datos persistentes para asegurar consistencia en interacciones de múltiples turnos.

A continuación, veamos en más detalle la llamada a Funciones/Herramientas.
 
### Llamada a Funciones/Herramientas

La llamada a funciones es la forma principal en que habilitamos a los Modelos de Lenguaje Extensos (LLMs) a interactuar con herramientas. A menudo verás que 'Función' y 'Herramienta' se utilizan indistintamente porque las 'funciones' (bloques de código reutilizables) son las 'herramientas' que los agentes usan para realizar tareas. Para que se invoque el código de una función, un LLM debe comparar la solicitud del usuario con la descripción de las funciones. Para ello, se envía al LLM un esquema que contiene las descripciones de todas las funciones disponibles. El LLM selecciona entonces la función más apropiada para la tarea y devuelve su nombre y argumentos. La función seleccionada se invoca, su respuesta se envía de vuelta al LLM, que utiliza la información para responder a la solicitud del usuario.

Para que los desarrolladores implementen la llamada a funciones para agentes, necesitarán:

1. Un modelo LLM que soporte llamadas a funciones
2. Un esquema que contenga descripciones de funciones
3. El código para cada función descrita

Usemos el ejemplo de obtener la hora actual en una ciudad para ilustrar:

1. **Inicializar un LLM que soporte llamadas a funciones:**

    No todos los modelos soportan llamada a funciones, por lo que es importante verificar que el LLM que usas lo haga.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> soporta llamadas a funciones. Podemos comenzar iniciando el cliente de OpenAI contra la **API de Respuestas** de Azure OpenAI (el endpoint estable `/openai/v1/` — no se necesita `api_version`). 

    ```python
    # Inicializar el cliente de OpenAI para Azure OpenAI (API de Respuestas, endpoint v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Crear un esquema de función**:

    Luego definiremos un esquema JSON que contiene el nombre de la función, descripción de lo que hace la función, y los nombres y descripciones de los parámetros de la función.
    Después tomaremos este esquema y lo pasaremos al cliente creado previamente, junto con la solicitud del usuario para encontrar la hora en San Francisco. Es importante señalar que se devuelve una **llamada a herramienta**, **no** la respuesta final a la pregunta. Como se mencionó anteriormente, el LLM devuelve el nombre de la función que seleccionó para la tarea, y los argumentos que se le pasarán.

    ```python
    # Descripción de la función para que el modelo la lea (formato de herramienta plana de la API de respuestas)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # Mensaje inicial del usuario
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Primera llamada a la API: Pide al modelo que use la función
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # La API de Respuestas devuelve llamadas a herramientas como elementos function_call en response.output.
    # Agrégalas a la conversación para que el modelo tenga contexto completo en el próximo turno.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **El código de la función necesario para realizar la tarea:**

    Ahora que el LLM ha elegido qué función debe ejecutarse, el código que realiza la tarea debe ser implementado y ejecutado.
    Podemos implementar el código para obtener la hora actual en Python. También necesitaremos escribir el código para extraer el nombre y argumentos del response_message para obtener el resultado final.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # Manejar llamadas a funciones
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Devolver el resultado de la herramienta como un elemento function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Segunda llamada a la API: Obtener la respuesta final del modelo
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

La llamada a funciones está en el corazón de la mayoría, si no de todo el diseño de uso de herramientas en agentes, sin embargo implementarla desde cero a veces puede ser un desafío.
Como aprendimos en [Lección 2](../../../02-explore-agentic-frameworks), los frameworks agenticos nos proporcionan bloques de construcción preconstruidos para implementar el uso de herramientas.
 
## Ejemplos de uso de herramientas con frameworks agenticos

Aquí hay algunos ejemplos de cómo puedes implementar el Patrón de Diseño de Uso de Herramientas utilizando diferentes frameworks agenticos:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> es un framework de IA de código abierto para construir agentes de IA. Simplifica el proceso de usar llamadas a funciones permitiéndote definir herramientas como funciones de Python con el decorador `@tool`. El framework maneja la comunicación de ida y vuelta entre el modelo y tu código. También provee acceso a herramientas preconstruidas como Búsqueda de Archivos e Intérprete de Código a través de `FoundryChatClient`.

El siguiente diagrama ilustra el proceso de llamadas a funciones con Microsoft Agent Framework:

![llamada a funciones](../../../translated_images/es/functioncalling-diagram.a84006fc287f6014.webp)

En Microsoft Agent Framework, las herramientas se definen como funciones decoradas. Podemos convertir la función `get_current_time` que vimos antes en una herramienta usando el decorador `@tool`. El framework automáticamente serializa la función y sus parámetros, creando el esquema para enviar al LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Crear el cliente
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Crear un agente y ejecutarlo con la herramienta
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> es un framework agentico más nuevo diseñado para empoderar a desarrolladores a construir, desplegar y escalar agentes de IA altamente extensibles y de alta calidad de forma segura sin tener que gestionar los recursos subyacentes de computación y almacenamiento. Es especialmente útil para aplicaciones empresariales ya que es un servicio completamente gestionado con seguridad de nivel empresarial.

En comparación con el desarrollo directo con la API de LLM, Microsoft Foundry Agent Service ofrece algunas ventajas, incluyendo:

- Llamada automática a herramientas – no es necesario analizar una llamada a herramienta, invocar la herramienta y manejar la respuesta; todo esto ahora se hace del lado del servidor
- Datos gestionados de forma segura – en lugar de manejar tu propio estado de conversación, puedes confiar en los hilos para almacenar toda la información que necesitas
- Herramientas listas para usar – Herramientas que puedes usar para interactuar con tus fuentes de datos, como Bing, Azure AI Search y Azure Functions.

Las herramientas disponibles en Microsoft Foundry Agent Service pueden dividirse en dos categorías:

1. Herramientas de conocimiento:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Fundamento con Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Búsqueda de archivos</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Herramientas de acción:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Llamada a funciones</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Intérprete de código</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Herramientas definidas por OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

El Agent Service nos permite usar estas herramientas juntas como un `conjunto de herramientas`. También utiliza `hilos` que mantienen el historial de mensajes de una conversación particular.

Imagina que eres un agente de ventas en una compañía llamada Contoso. Quieres desarrollar un agente conversacional que pueda responder preguntas sobre tus datos de ventas.

La siguiente imagen ilustra cómo podrías usar Microsoft Foundry Agent Service para analizar tus datos de ventas:

![Servicio Agentic en acción](../../../translated_images/es/agent-service-in-action.34fb465c9a84659e.webp)

Para usar cualquiera de estas herramientas con el servicio podemos crear un cliente y definir una herramienta o conjunto de herramientas. Para implementarlo prácticamente podemos usar el siguiente código Python. El LLM podrá observar el conjunto de herramientas y decidir si usar la función creada por el usuario, `fetch_sales_data_using_sqlite_query`, o el Intérprete de Código preconstruido dependiendo de la solicitud del usuario.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # función fetch_sales_data_using_sqlite_query que se puede encontrar en un archivo fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializar conjunto de herramientas
toolset = ToolSet()

# Inicializar agente de llamada de función con la función fetch_sales_data_using_sqlite_query y agregarla al conjunto de herramientas
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializar herramienta de Intérprete de Código y agregarla al conjunto de herramientas.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ¿Cuáles son las consideraciones especiales para usar el Patrón de Diseño de Uso de Herramientas para construir agentes de IA confiables?

Una preocupación común con el SQL generado dinámicamente por LLMs es la seguridad, particularmente el riesgo de inyección SQL o acciones maliciosas, como eliminar o alterar la base de datos. Aunque estas preocupaciones son válidas, pueden mitigarse eficazmente configurando adecuadamente los permisos de acceso a la base de datos. Para la mayoría de las bases de datos esto implica configurarla como de solo lectura. Para servicios de base de datos como PostgreSQL o Azure SQL, la aplicación debe tener asignado un rol de solo lectura (SELECT).

Ejecutar la aplicación en un entorno seguro mejora aún más la protección. En escenarios empresariales, normalmente se extraen y transforman los datos de sistemas operativos hacia una base de datos o almacén de datos de solo lectura con un esquema amigable para el usuario. Este enfoque asegura que los datos estén protegidos, optimizados para rendimiento y accesibilidad, y que la aplicación tenga acceso restringido y de solo lectura.

## Códigos de ejemplo

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ¿Tienes más preguntas sobre el Patrón de Diseño de Uso de Herramientas?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros aprendices, asistir a horas de oficina y resolver tus preguntas sobre agentes de IA.

## Recursos adicionales

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Taller de Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Taller Multi-Agente de Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Resumen de Microsoft Agent Framework</a>


## Prueba rápida de este Agente (Opcional)

Después de aprender a desplegar agentes en [Lección 16](../16-deploying-scalable-agents/README.md), puedes hacer una prueba rápida del `TravelToolAgent` de esta lección (¿sigue llamando a sus herramientas y respondiendo?) con [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Consulta [`tests/README.md`](../tests/README.md) para saber cómo ejecutarlo.

## Lección anterior

[Comprendiendo los patrones de diseño agénticos](../03-agentic-design-patterns/README.md)

## Próxima lección

[RAG agéntico](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->