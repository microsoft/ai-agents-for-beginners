<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T16:30:04+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "es"
}
-->
[![Cómo diseñar buenos agentes de IA](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.es.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Patrón de diseño para el uso de herramientas

Las herramientas son interesantes porque permiten que los agentes de IA tengan un rango más amplio de capacidades. En lugar de que el agente tenga un conjunto limitado de acciones que puede realizar, al agregar una herramienta, el agente ahora puede realizar una amplia gama de acciones. En este capítulo, veremos el Patrón de Diseño para el Uso de Herramientas, que describe cómo los agentes de IA pueden usar herramientas específicas para alcanzar sus objetivos.

## Introducción

En esta lección, buscamos responder las siguientes preguntas:

- ¿Qué es el patrón de diseño para el uso de herramientas?
- ¿Cuáles son los casos de uso en los que se puede aplicar?
- ¿Cuáles son los elementos/bloques necesarios para implementar el patrón de diseño?
- ¿Cuáles son las consideraciones especiales para usar el Patrón de Diseño para el Uso de Herramientas para construir agentes de IA confiables?

## Objetivos de aprendizaje

Después de completar esta lección, podrás:

- Definir el Patrón de Diseño para el Uso de Herramientas y su propósito.
- Identificar casos de uso donde el Patrón de Diseño para el Uso de Herramientas es aplicable.
- Comprender los elementos clave necesarios para implementar el patrón de diseño.
- Reconocer consideraciones para garantizar la confiabilidad en agentes de IA que utilizan este patrón de diseño.

## ¿Qué es el Patrón de Diseño para el Uso de Herramientas?

El **Patrón de Diseño para el Uso de Herramientas** se centra en dar a los LLMs la capacidad de interactuar con herramientas externas para alcanzar objetivos específicos. Las herramientas son código que puede ser ejecutado por un agente para realizar acciones. Una herramienta puede ser una función simple como una calculadora, o una llamada API a un servicio externo como la consulta de precios de acciones o el pronóstico del clima. En el contexto de los agentes de IA, las herramientas están diseñadas para ser ejecutadas por agentes en respuesta a **llamadas a funciones generadas por el modelo**.

## ¿Cuáles son los casos de uso en los que se puede aplicar?

Los agentes de IA pueden aprovechar las herramientas para completar tareas complejas, recuperar información o tomar decisiones. El patrón de diseño para el uso de herramientas se utiliza a menudo en escenarios que requieren interacción dinámica con sistemas externos, como bases de datos, servicios web o intérpretes de código. Esta capacidad es útil para varios casos de uso, incluyendo:

- **Recuperación dinámica de información:** Los agentes pueden consultar APIs externas o bases de datos para obtener datos actualizados (por ejemplo, consultar una base de datos SQLite para análisis de datos, obtener precios de acciones o información meteorológica).
- **Ejecución e interpretación de código:** Los agentes pueden ejecutar código o scripts para resolver problemas matemáticos, generar informes o realizar simulaciones.
- **Automatización de flujos de trabajo:** Automatizar flujos de trabajo repetitivos o de múltiples pasos integrando herramientas como programadores de tareas, servicios de correo electrónico o pipelines de datos.
- **Soporte al cliente:** Los agentes pueden interactuar con sistemas CRM, plataformas de tickets o bases de conocimiento para resolver consultas de usuarios.
- **Generación y edición de contenido:** Los agentes pueden utilizar herramientas como correctores gramaticales, resumidores de texto o evaluadores de seguridad de contenido para ayudar en tareas de creación de contenido.

## ¿Cuáles son los elementos/bloques necesarios para implementar el patrón de diseño para el uso de herramientas?

Estos bloques permiten que el agente de IA realice una amplia gama de tareas. Veamos los elementos clave necesarios para implementar el Patrón de Diseño para el Uso de Herramientas:

- **Esquemas de funciones/herramientas:** Definiciones detalladas de las herramientas disponibles, incluyendo el nombre de la función, propósito, parámetros requeridos y resultados esperados. Estos esquemas permiten que el LLM entienda qué herramientas están disponibles y cómo construir solicitudes válidas.

- **Lógica de ejecución de funciones:** Regula cómo y cuándo se invocan las herramientas según la intención del usuario y el contexto de la conversación. Esto puede incluir módulos de planificación, mecanismos de enrutamiento o flujos condicionales que determinan el uso de herramientas de manera dinámica.

- **Sistema de manejo de mensajes:** Componentes que gestionan el flujo conversacional entre las entradas del usuario, las respuestas del LLM, las llamadas a herramientas y los resultados de las herramientas.

- **Marco de integración de herramientas:** Infraestructura que conecta al agente con diversas herramientas, ya sean funciones simples o servicios externos complejos.

- **Gestión de errores y validación:** Mecanismos para manejar fallos en la ejecución de herramientas, validar parámetros y gestionar respuestas inesperadas.

- **Gestión de estado:** Rastrea el contexto de la conversación, interacciones previas con herramientas y datos persistentes para garantizar la consistencia en interacciones de múltiples turnos.

A continuación, veamos en detalle las llamadas a funciones/herramientas.

### Llamadas a funciones/herramientas

Las llamadas a funciones son la forma principal en que habilitamos a los Modelos de Lenguaje Extendido (LLMs) para interactuar con herramientas. A menudo verás que se usan 'Función' y 'Herramienta' de manera intercambiable porque las 'funciones' (bloques de código reutilizable) son las 'herramientas' que los agentes utilizan para llevar a cabo tareas. Para que se invoque el código de una función, un LLM debe comparar la solicitud del usuario con la descripción de la función. Para ello, se envía al LLM un esquema que contiene las descripciones de todas las funciones disponibles. El LLM selecciona la función más adecuada para la tarea y devuelve su nombre y argumentos. La función seleccionada se invoca, su respuesta se envía de vuelta al LLM, que utiliza la información para responder a la solicitud del usuario.

Para que los desarrolladores implementen llamadas a funciones para agentes, necesitarás:

1. Un modelo LLM que soporte llamadas a funciones
2. Un esquema que contenga descripciones de funciones
3. El código para cada función descrita

Usemos el ejemplo de obtener la hora actual en una ciudad para ilustrar:

1. **Inicializar un LLM que soporte llamadas a funciones:**

    No todos los modelos soportan llamadas a funciones, por lo que es importante verificar que el LLM que estás utilizando lo haga. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> soporta llamadas a funciones. Podemos comenzar iniciando el cliente de Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Crear un esquema de funciones:**

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

    Ahora que el LLM ha elegido qué función necesita ejecutarse, el código que lleva a cabo la tarea debe ser implementado y ejecutado. Podemos implementar el código para obtener la hora actual en Python. También necesitaremos escribir el código para extraer el nombre y los argumentos del response_message para obtener el resultado final.

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

Las llamadas a funciones están en el corazón de la mayoría, si no de todos los diseños de uso de herramientas por parte de agentes, sin embargo, implementarlas desde cero puede ser un desafío. Como aprendimos en [Lección 2](../../../02-explore-agentic-frameworks), los marcos agentic nos proporcionan bloques preconstruidos para implementar el uso de herramientas.

## Ejemplos de uso de herramientas con marcos agentic

Aquí hay algunos ejemplos de cómo puedes implementar el Patrón de Diseño para el Uso de Herramientas utilizando diferentes marcos agentic:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> es un marco de IA de código abierto para desarrolladores de .NET, Python y Java que trabajan con Modelos de Lenguaje Extendido (LLMs). Simplifica el proceso de usar llamadas a funciones describiendo automáticamente tus funciones y sus parámetros al modelo mediante un proceso llamado <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialización</a>. También maneja la comunicación de ida y vuelta entre el modelo y tu código. Otra ventaja de usar un marco agentic como Semantic Kernel es que te permite acceder a herramientas preconstruidas como <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Búsqueda de Archivos</a> y <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Intérprete de Código</a>.

El siguiente diagrama ilustra el proceso de llamadas a funciones con Semantic Kernel:

![llamadas a funciones](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.es.png)

En Semantic Kernel las funciones/herramientas se llaman <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Podemos convertir la función `get_current_time` que vimos anteriormente en un plugin convirtiéndola en una clase con la función dentro de ella. También podemos importar el decorador `kernel_function`, que toma la descripción de la función. Cuando luego creas un kernel con el GetCurrentTimePlugin, el kernel automáticamente serializa la función y sus parámetros, creando el esquema para enviar al LLM en el proceso.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> es un marco agentic más reciente diseñado para permitir a los desarrolladores construir, implementar y escalar agentes de IA de alta calidad y extensibles de manera segura, sin necesidad de gestionar los recursos de computación y almacenamiento subyacentes. Es particularmente útil para aplicaciones empresariales, ya que es un servicio completamente gestionado con seguridad de nivel empresarial.

En comparación con el desarrollo directo con la API de LLM, Azure AI Agent Service ofrece algunas ventajas, incluyendo:

- Llamadas a herramientas automáticas: no es necesario analizar una llamada a herramienta, invocar la herramienta y manejar la respuesta; todo esto ahora se realiza en el servidor.
- Gestión segura de datos: en lugar de gestionar tu propio estado de conversación, puedes confiar en los hilos para almacenar toda la información que necesitas.
- Herramientas listas para usar: Herramientas que puedes usar para interactuar con tus fuentes de datos, como Bing, Azure AI Search y Azure Functions.

Las herramientas disponibles en Azure AI Agent Service se dividen en dos categorías:

1. Herramientas de conocimiento:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Fundamentación con Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Búsqueda de Archivos</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Herramientas de acción:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Llamadas a Funciones</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Intérprete de Código</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Herramientas definidas por OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

El Agent Service nos permite usar estas herramientas juntas como un `toolset`. También utiliza `threads` que mantienen un registro del historial de mensajes de una conversación particular.

Imagina que eres un agente de ventas en una empresa llamada Contoso. Quieres desarrollar un agente conversacional que pueda responder preguntas sobre tus datos de ventas.

La siguiente imagen ilustra cómo podrías usar Azure AI Agent Service para analizar tus datos de ventas:

![Servicio Agentic en acción](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.es.jpg)

Para usar cualquiera de estas herramientas con el servicio, podemos crear un cliente y definir una herramienta o conjunto de herramientas. Para implementarlo de manera práctica, podemos usar el siguiente código en Python. El LLM podrá mirar el conjunto de herramientas y decidir si usar la función creada por el usuario, `fetch_sales_data_using_sqlite_query`, o el Intérprete de Código preconstruido dependiendo de la solicitud del usuario.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
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

## ¿Cuáles son las consideraciones especiales para usar el Patrón de Diseño para el Uso de Herramientas para construir agentes de IA confiables?

Una preocupación común con SQL generado dinámicamente por LLMs es la seguridad, particularmente el riesgo de inyección de SQL o acciones maliciosas, como eliminar o alterar la base de datos. Aunque estas preocupaciones son válidas, pueden mitigarse eficazmente configurando adecuadamente los permisos de acceso a la base de datos. Para la mayoría de las bases de datos, esto implica configurarlas como de solo lectura. Para servicios de bases de datos como PostgreSQL o Azure SQL, la aplicación debe ser asignada a un rol de solo lectura (SELECT).
Ejecutar la aplicación en un entorno seguro mejora aún más la protección. En escenarios empresariales, los datos suelen extraerse y transformarse desde sistemas operativos hacia una base de datos de solo lectura o un almacén de datos con un esquema fácil de usar. Este enfoque asegura que los datos sean seguros, optimizados para el rendimiento y la accesibilidad, y que la aplicación tenga acceso restringido y de solo lectura.

## Códigos de Ejemplo

- Python: [Marco de Agentes](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Marco de Agentes](./code_samples/04-dotnet-agent-framework.md)

## ¿Tienes más preguntas sobre los patrones de diseño de uso de herramientas?

Únete al [Discord de Azure AI Foundry](https://aka.ms/ai-agents/discord) para conectarte con otros estudiantes, asistir a horas de oficina y resolver tus dudas sobre Agentes de IA.

## Recursos Adicionales

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Taller de Servicio de Agentes de Azure AI</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Taller Multi-Agente de Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutorial de Llamadas a Funciones en Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Intérprete de Código de Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Herramientas Autogen</a>

## Lección Anterior

[Entendiendo los Patrones de Diseño Agéntico](../03-agentic-design-patterns/README.md)

## Próxima Lección

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->