<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b8ea2abd1a674f736d5fc08982e6ec06",
  "translation_date": "2025-03-28T10:21:42+00:00",
  "source_file": "04-tool-use\\README.md",
  "language_code": "es"
}
-->
[![Cómo Diseñar Agentes de IA de Calidad](../../../translated_images/lesson-4-thumbnail.2c292cd87b951b3e914e9548b46cb4d14a0852f9c8d75e9566d46da839c983d9.es.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Patrón de Diseño de Uso de Herramientas

Las herramientas son interesantes porque permiten que los agentes de IA tengan una gama más amplia de capacidades. En lugar de que el agente tenga un conjunto limitado de acciones que puede realizar, al agregar una herramienta, el agente ahora puede llevar a cabo una variedad de acciones. En este capítulo, exploraremos el Patrón de Diseño de Uso de Herramientas, que describe cómo los agentes de IA pueden usar herramientas específicas para alcanzar sus objetivos.

## Introducción

En esta lección, buscamos responder las siguientes preguntas:

- ¿Qué es el patrón de diseño de uso de herramientas?
- ¿Cuáles son los casos de uso en los que se puede aplicar?
- ¿Cuáles son los elementos necesarios para implementar el patrón de diseño?
- ¿Cuáles son las consideraciones especiales para usar el Patrón de Diseño de Uso de Herramientas para construir agentes de IA confiables?

## Objetivos de Aprendizaje

Después de completar esta lección, serás capaz de:

- Definir el Patrón de Diseño de Uso de Herramientas y su propósito.
- Identificar casos de uso donde el Patrón de Diseño de Uso de Herramientas es aplicable.
- Comprender los elementos clave necesarios para implementar el patrón de diseño.
- Reconocer las consideraciones para garantizar la confiabilidad en agentes de IA que utilizan este patrón de diseño.

## ¿Qué es el Patrón de Diseño de Uso de Herramientas?

El **Patrón de Diseño de Uso de Herramientas** se centra en dar a los LLMs la capacidad de interactuar con herramientas externas para alcanzar objetivos específicos. Las herramientas son código que puede ser ejecutado por un agente para realizar acciones. Una herramienta puede ser una función sencilla como una calculadora, o una llamada a una API de un servicio externo, como consultar el precio de acciones o el pronóstico del clima. En el contexto de los agentes de IA, las herramientas están diseñadas para ser ejecutadas por agentes en respuesta a **llamadas a funciones generadas por el modelo**.

## ¿Cuáles son los casos de uso en los que se puede aplicar?

Los agentes de IA pueden aprovechar las herramientas para completar tareas complejas, recuperar información o tomar decisiones. El patrón de diseño de uso de herramientas se utiliza frecuentemente en escenarios que requieren interacción dinámica con sistemas externos, como bases de datos, servicios web o intérpretes de código. Esta capacidad es útil para diversos casos de uso, incluyendo:

- **Recuperación Dinámica de Información:** Los agentes pueden consultar APIs externas o bases de datos para obtener datos actualizados (por ejemplo, consultar una base de datos SQLite para análisis de datos, obtener precios de acciones o información meteorológica).
- **Ejecución e Interpretación de Código:** Los agentes pueden ejecutar código o scripts para resolver problemas matemáticos, generar informes o realizar simulaciones.
- **Automatización de Flujos de Trabajo:** Automatización de tareas repetitivas o flujos de trabajo de múltiples pasos mediante la integración de herramientas como programadores de tareas, servicios de correo electrónico o pipelines de datos.
- **Soporte al Cliente:** Los agentes pueden interactuar con sistemas CRM, plataformas de tickets o bases de conocimiento para resolver consultas de usuarios.
- **Generación y Edición de Contenido:** Los agentes pueden usar herramientas como verificadores gramaticales, resumidores de texto o evaluadores de seguridad de contenido para asistir en tareas de creación de contenido.

## ¿Cuáles son los elementos necesarios para implementar el patrón de diseño de uso de herramientas?

Estos elementos permiten que el agente de IA realice una amplia gama de tareas. Veamos los elementos clave necesarios para implementar el Patrón de Diseño de Uso de Herramientas:

- **Llamada a Funciones/Herramientas:** Esta es la forma principal de habilitar a los LLMs para interactuar con herramientas. Las funciones o herramientas son bloques de código reutilizable que los agentes utilizan para llevar a cabo tareas. Estas pueden variar desde funciones simples como una calculadora hasta llamadas a APIs de servicios externos como consultas de precios de acciones o pronósticos meteorológicos.

- **Recuperación Dinámica de Información:** Los agentes pueden consultar APIs externas o bases de datos para obtener datos actualizados. Esto es útil para tareas como análisis de datos, obtener precios de acciones o información meteorológica.

- **Ejecución e Interpretación de Código:** Los agentes pueden ejecutar código o scripts para resolver problemas matemáticos, generar informes o realizar simulaciones.

- **Automatización de Flujos de Trabajo:** Esto implica automatizar tareas repetitivas o flujos de trabajo de múltiples pasos mediante la integración de herramientas como programadores de tareas, servicios de correo electrónico o pipelines de datos.

- **Soporte al Cliente:** Los agentes pueden interactuar con sistemas CRM, plataformas de tickets o bases de conocimiento para resolver consultas de usuarios.

- **Generación y Edición de Contenido:** Los agentes pueden usar herramientas como verificadores gramaticales, resumidores de texto o evaluadores de seguridad de contenido para asistir en tareas de creación de contenido.

A continuación, profundicemos en la llamada a funciones/herramientas.

### Llamada a Funciones/Herramientas

La llamada a funciones es la forma principal en que habilitamos a los Modelos de Lenguaje Extenso (LLMs) para interactuar con herramientas. Frecuentemente verás los términos 'Función' y 'Herramienta' usados de manera intercambiable porque las 'funciones' (bloques de código reutilizable) son las 'herramientas' que los agentes utilizan para llevar a cabo tareas. Para que el código de una función sea invocado, un LLM debe comparar la solicitud del usuario con la descripción de la función. Para hacer esto, se envía al LLM un esquema que contiene las descripciones de todas las funciones disponibles. El LLM selecciona la función más adecuada para la tarea y devuelve su nombre y argumentos. La función seleccionada se invoca, su respuesta se envía de vuelta al LLM, que utiliza la información para responder a la solicitud del usuario.

Para que los desarrolladores implementen la llamada a funciones para agentes, necesitarás:

1. Un modelo LLM que admita llamadas a funciones
2. Un esquema que contenga las descripciones de las funciones
3. El código para cada función descrita

Usemos el ejemplo de obtener la hora actual en una ciudad para ilustrar:

1. **Inicializar un LLM que admita llamadas a funciones:**

    No todos los modelos admiten llamadas a funciones, por lo que es importante verificar que el LLM que estás utilizando lo haga. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> admite llamadas a funciones. Podemos comenzar iniciando el cliente de Azure OpenAI. 

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Crear un Esquema de Función:**

    A continuación, definiremos un esquema JSON que contiene el nombre de la función, una descripción de lo que hace la función, y los nombres y descripciones de los parámetros de la función. Luego tomaremos este esquema y lo pasaremos al cliente creado previamente, junto con la solicitud del usuario para encontrar la hora en San Francisco. Es importante notar que lo que se devuelve es una **llamada a herramienta**, **no** la respuesta final a la pregunta. Como se mencionó anteriormente, el LLM devuelve el nombre de la función que seleccionó para la tarea y los argumentos que se le pasarán.

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **El código de la función necesario para llevar a cabo la tarea:**

    Ahora que el LLM ha elegido qué función necesita ejecutarse, el código que realiza la tarea debe ser implementado y ejecutado. Podemos implementar el código para obtener la hora actual en Python. También necesitaremos escribir el código para extraer el nombre y los argumentos del response_message para obtener el resultado final.

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
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

La llamada a funciones está en el núcleo de la mayoría, si no de todos los diseños de uso de herramientas de agentes; sin embargo, implementarla desde cero puede ser desafiante. Como aprendimos en [Lección 2](../../../02-explore-agentic-frameworks), los frameworks agentic nos proporcionan bloques de construcción predefinidos para implementar el uso de herramientas.

## Ejemplos de Uso de Herramientas con Frameworks Agentic

Aquí hay algunos ejemplos de cómo puedes implementar el Patrón de Diseño de Uso de Herramientas utilizando diferentes frameworks agentic:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> es un framework de IA de código abierto para desarrolladores de .NET, Python y Java que trabajan con Modelos de Lenguaje Extenso (LLMs). Simplifica el proceso de usar llamadas a funciones describiendo automáticamente tus funciones y sus parámetros al modelo mediante un proceso llamado <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialización</a>. También maneja la comunicación entre el modelo y tu código. Otra ventaja de usar un framework agentic como Semantic Kernel es que te permite acceder a herramientas predefinidas como <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> y <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

El siguiente diagrama ilustra el proceso de llamada a funciones con Semantic Kernel:

![function calling](../../../translated_images/functioncalling-diagram.b5493ea5154ad8e3e4940d2e36a49101eec1398948e5d1039942203b4f5a4209.es.png)

En Semantic Kernel, las funciones/herramientas se llaman <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Podemos convertir la función `get_current_time` function we saw earlier into a plugin by turning it into a class with the function in it. We can also import the `kernel_function` con el decorador, que toma la descripción de la función. Cuando luego creas un kernel con el GetCurrentTimePlugin, el kernel automáticamente serializa la función y sus parámetros, creando el esquema para enviarlo al LLM en el proceso.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> es un framework agentic más reciente diseñado para permitir a los desarrolladores construir, desplegar y escalar agentes de IA de alta calidad y extensibles de manera segura, sin necesidad de gestionar los recursos subyacentes de cómputo y almacenamiento. Es particularmente útil para aplicaciones empresariales ya que es un servicio completamente administrado con seguridad de nivel empresarial.

Comparado con el desarrollo directo con la API de LLM, Azure AI Agent Service ofrece algunas ventajas, incluyendo:

- Llamada a herramientas automática: no es necesario analizar una llamada a herramienta, invocar la herramienta y manejar la respuesta; todo esto ahora se realiza del lado del servidor.
- Gestión segura de datos: en lugar de gestionar tu propio estado de conversación, puedes confiar en los hilos para almacenar toda la información que necesitas.
- Herramientas listas para usar: Herramientas que puedes usar para interactuar con tus fuentes de datos, como Bing, Azure AI Search y Azure Functions.

Las herramientas disponibles en Azure AI Agent Service se dividen en dos categorías:

1. Herramientas de Conocimiento:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding con Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Herramientas de Acción:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Herramientas definidas por OpenAI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

El Agent Service nos permite usar estas herramientas juntas como un `toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

The following image illustrates how you could use Azure AI Agent Service to analyze your sales data:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.8c2d8aa8e9d91feeb29549b3fde529f8332b243875154d03907616a69198afbc.es.jpg)

To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the following Python code. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query`, o el Code Interpreter predefinido según la solicitud del usuario.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fecth_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ¿Cuáles son las consideraciones especiales para usar el Patrón de Diseño de Uso de Herramientas para construir agentes de IA confiables?

Una preocupación común con SQL generado dinámicamente por LLMs es la seguridad, particularmente el riesgo de inyección de SQL o acciones maliciosas, como eliminar o manipular la base de datos. Aunque estas preocupaciones son válidas, pueden mitigarse eficazmente configurando correctamente los permisos de acceso a la base de datos. Para la mayoría de las bases de datos, esto implica configurarlas como de solo lectura. Para servicios de bases de datos como PostgreSQL o Azure SQL, la aplicación debe ser asignada a un rol de solo lectura (SELECT).

Ejecutar la aplicación en un entorno seguro mejora aún más la protección. En escenarios empresariales, los datos típicamente se extraen y transforman desde sistemas operativos hacia una base de datos de solo lectura o un data warehouse con un esquema amigable para el usuario. Este enfoque asegura que los datos sean seguros, optimizados para rendimiento y accesibilidad, y que la aplicación tenga acceso restringido de solo lectura.

## Recursos Adicionales

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Taller de Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Taller Multi-Agente Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutorial de Llamada a Funciones con Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter de Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Lección Anterior

[Entendiendo los Patrones de Diseño Agentic](../03-agentic-design-patterns/README.md)

## Próxima Lección

[Agentic RAG](../05-agentic-rag/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.