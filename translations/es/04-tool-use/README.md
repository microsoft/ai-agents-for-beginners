[![Cómo diseñar buenos agentes de IA](../../../translated_images/es/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Patrón de Diseño de Uso de Herramientas

Las herramientas son interesantes porque permiten que los agentes de IA tengan un rango más amplio de capacidades. En lugar de que el agente tenga un conjunto limitado de acciones que puede realizar, al agregar una herramienta, el agente ahora puede realizar una amplia gama de acciones. En este capítulo, analizaremos el Patrón de Diseño de Uso de Herramientas, que describe cómo los agentes de IA pueden usar herramientas específicas para lograr sus objetivos.

## Introducción

En esta lección, buscamos responder las siguientes preguntas:

- ¿Qué es el patrón de diseño de uso de herramientas?
- ¿Cuáles son los casos de uso a los que se puede aplicar?
- ¿Cuáles son los elementos/bloques constructores necesarios para implementar el patrón de diseño?
- ¿Cuáles son las consideraciones especiales para usar el Patrón de Diseño de Uso de Herramientas para construir agentes de IA confiables?

## Objetivos de aprendizaje

Después de completar esta lección, podrás:

- Definir el Patrón de Diseño de Uso de Herramientas y su propósito.
- Identificar casos de uso donde el Patrón de Diseño de Uso de Herramientas es aplicable.
- Entender los elementos clave necesarios para implementar el patrón de diseño.
- Reconocer consideraciones para garantizar la confiabilidad en agentes de IA que usan este patrón de diseño.

## ¿Qué es el Patrón de Diseño de Uso de Herramientas?

El **Patrón de Diseño de Uso de Herramientas** se centra en otorgar a los Modelos de Lenguaje Grande (LLMs) la capacidad de interactuar con herramientas externas para lograr objetivos específicos. Las herramientas son códigos que pueden ser ejecutados por un agente para realizar acciones. Una herramienta puede ser una función simple como una calculadora o una llamada a una API de un servicio externo como la consulta de precios de acciones o el pronóstico del clima. En el contexto de agentes de IA, las herramientas están diseñadas para ser ejecutadas por agentes en respuesta a **llamadas de función generadas por el modelo**.

## ¿Cuáles son los casos de uso a los que se puede aplicar?

Los agentes de IA pueden aprovechar herramientas para completar tareas complejas, recuperar información o tomar decisiones. El patrón de diseño de uso de herramientas se usa frecuentemente en escenarios que requieren interacción dinámica con sistemas externos, como bases de datos, servicios web o intérpretes de código. Esta capacidad es útil para varios casos de uso, incluyendo:

- **Recuperación dinámica de información:** Los agentes pueden consultar APIs externas o bases de datos para obtener datos actualizados (p. ej., consultar una base de datos SQLite para análisis de datos, obtener precios de acciones o información meteorológica).
- **Ejecución e interpretación de código:** Los agentes pueden ejecutar código o scripts para resolver problemas matemáticos, generar reportes o realizar simulaciones.
- **Automatización de flujos de trabajo:** Automatizar flujos repetitivos o de varios pasos integrando herramientas como programadores de tareas, servicios de correo electrónico o canalizaciones de datos.
- **Soporte al cliente:** Los agentes pueden interactuar con sistemas CRM, plataformas de tickets o bases de conocimiento para resolver consultas de usuarios.
- **Generación y edición de contenido:** Los agentes pueden utilizar herramientas como correctores gramaticales, resumidores de texto o evaluadores de seguridad de contenido para ayudar con tareas de creación de contenido.

## ¿Cuáles son los elementos/bloques constructores necesarios para implementar el patrón de diseño de uso de herramientas?

Estos bloques constructores permiten que el agente de IA realice una amplia gama de tareas. Observemos los elementos clave necesarios para implementar el Patrón de Diseño de Uso de Herramientas:

- **Esquemas de Función/Herramienta**: Definiciones detalladas de las herramientas disponibles, incluyendo nombre de función, propósito, parámetros requeridos y salidas esperadas. Estos esquemas permiten que el LLM entienda qué herramientas están disponibles y cómo construir solicitudes válidas.

- **Lógica de Ejecución de Funciones**: Regula cómo y cuándo se invocan las herramientas en función de la intención del usuario y el contexto de la conversación. Esto puede incluir módulos planificadores, mecanismos de enrutamiento o flujos condicionales que determinan el uso de herramientas dinámicamente.

- **Sistema de Manejo de Mensajes**: Componentes que gestionan el flujo conversacional entre entradas del usuario, respuestas del LLM, llamadas a herramientas y resultados de herramientas.

- **Marco de Integración de Herramientas**: Infraestructura que conecta al agente con diversas herramientas, ya sean funciones simples o servicios externos complejos.

- **Manejo de Errores y Validación**: Mecanismos para manejar fallos en la ejecución de herramientas, validar parámetros y gestionar respuestas inesperadas.

- **Gestión de Estado**: Rastrea el contexto de la conversación, interacciones previas con herramientas y datos persistentes para asegurar consistencia a lo largo de interacciones múltiples.

A continuación, veamos con más detalle las Llamadas a Funciones/Herramientas.

### Llamadas a Funciones/Herramientas

La llamada a funciones es la forma principal en que permitimos que los Modelos de Lenguaje Grande (LLMs) interactúen con herramientas. A menudo verás que 'Función' y 'Herramienta' se usan indistintamente porque las 'funciones' (bloques de código reutilizable) son las 'herramientas' que los agentes usan para realizar tareas. Para que el código de una función sea invocado, un LLM debe comparar la solicitud del usuario contra la descripción de las funciones. Para esto, se envía al LLM un esquema que contiene las descripciones de todas las funciones disponibles. El LLM entonces selecciona la función más apropiada para la tarea y devuelve su nombre y argumentos. La función seleccionada se invoca, su respuesta se envía de vuelta al LLM, que usa esta información para responder a la solicitud del usuario.

Para que los desarrolladores implementen la llamada a funciones para agentes, necesitarás:

1. Un modelo LLM que soporte llamadas a funciones
2. Un esquema que contenga descripciones de funciones
3. El código para cada función descrita

Usemos el ejemplo de obtener la hora actual en una ciudad para ilustrar:

1. **Inicializar un LLM que soporte llamadas a funciones:**

    No todos los modelos soportan llamadas a funciones, por lo que es importante verificar que el LLM que usas lo haga. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> soporta llamadas a funciones. Podemos comenzar iniciando el cliente de Azure OpenAI.

    ```python
    # Inicializar el cliente de Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Crear un Esquema de Función**:

    Luego definiremos un esquema JSON que contiene el nombre de la función, la descripción de lo que hace la función y los nombres y descripciones de los parámetros de la función.
    Después tomaremos este esquema y se lo pasaremos al cliente creado anteriormente, junto con la solicitud del usuario para encontrar la hora en San Francisco. Es importante notar que lo que se devuelve es una **llamada a herramienta**, **no** la respuesta final a la pregunta. Como se mencionó antes, el LLM devuelve el nombre de la función que seleccionó para la tarea, y los argumentos que se le pasarán.

    ```python
    # Descripción de la función para que el modelo la lea
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
  
    # Mensaje inicial del usuario
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Primera llamada a la API: Pedir al modelo que use la función
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Procesar la respuesta del modelo
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **El código de la función requerido para llevar a cabo la tarea:**

    Ahora que el LLM ha elegido qué función debe ejecutarse, es necesario implementar y ejecutar el código que realiza la tarea.
    Podemos implementar el código para obtener la hora actual en Python. También necesitaremos escribir el código para extraer el nombre y argumentos de la respuesta del mensaje para obtener el resultado final.

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
  
      # Segunda llamada a la API: Obtener la respuesta final del modelo
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

La llamada a funciones está en el corazón de la mayoría, si no todos, los diseños de uso de herramientas de agentes, sin embargo, implementarla desde cero a veces puede ser un desafío.
Como aprendimos en [Lección 2](../../../02-explore-agentic-frameworks) los marcos agenticos nos proporcionan bloques constructores preconstruidos para implementar el uso de herramientas.

## Ejemplos de Uso de Herramientas con Marcos Agenticos

Aquí hay algunos ejemplos de cómo puedes implementar el Patrón de Diseño de Uso de Herramientas usando diferentes marcos agenticos:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> es un framework de IA de código abierto para desarrolladores .NET, Python y Java que trabajan con Modelos de Lenguaje Grande (LLMs). Simplifica el proceso de usar llamadas a funciones describiendo automáticamente tus funciones y sus parámetros al modelo a través de un proceso llamado <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialización</a>. También maneja la comunicación bidireccional entre el modelo y tu código. Otra ventaja de usar un marco agentico como Semantic Kernel es que te permite acceder a herramientas preconstruidas como <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Búsqueda de Archivos</a> y <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Intérprete de Código</a>.

El siguiente diagrama ilustra el proceso de llamadas a funciones con Semantic Kernel:

![function calling](../../../translated_images/es/functioncalling-diagram.a84006fc287f6014.webp)

En Semantic Kernel, las funciones/herramientas se llaman <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Podemos convertir la función `get_current_time` que vimos antes en un plugin convirtiéndola en una clase que contenga la función. También podemos importar el decorador `kernel_function`, que toma la descripción de la función. Cuando creas un kernel con el GetCurrentTimePlugin, el kernel serializa automáticamente la función y sus parámetros, creando el esquema para enviar al LLM en el proceso.

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

# Crear el kernel
kernel = Kernel()

# Crear el plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Añadir el plugin al kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> es un marco agentico más nuevo diseñado para capacitar a los desarrolladores a construir, desplegar y escalar agentes de IA extensibles y de alta calidad de forma segura, sin necesidad de gestionar los recursos subyacentes de cómputo y almacenamiento. Es particularmente útil para aplicaciones empresariales ya que es un servicio completamente gestionado con seguridad de nivel empresarial.

En comparación con desarrollar directamente con la API LLM, Azure AI Agent Service ofrece algunas ventajas, incluyendo:

- Llamada automática a herramientas – no es necesario analizar una llamada a herramienta, invocar la herramienta y manejar la respuesta; todo esto se hace ahora en el servidor
- Datos gestionados de forma segura – en lugar de administrar tu propio estado de conversación, puedes confiar en los hilos para almacenar toda la información que necesitas
- Herramientas listas para usar – Herramientas que puedes usar para interactuar con tus fuentes de datos, como Bing, Azure AI Search y Azure Functions.

Las herramientas disponibles en Azure AI Agent Service pueden dividirse en dos categorías:

1. Herramientas de Conocimiento:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Anclaje con Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Búsqueda de Archivos</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Herramientas de Acción:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Llamada a Funciones</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Intérprete de Código</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Herramientas definidas por OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

El Agent Service nos permite usar estas herramientas juntas como un `conjunto de herramientas`. También utiliza `hilos` que hacen seguimiento del historial de mensajes de una conversación particular.

Imagina que eres un agente de ventas en una empresa llamada Contoso. Quieres desarrollar un agente conversacional que pueda responder preguntas sobre tus datos de ventas.

La siguiente imagen ilustra cómo podrías usar Azure AI Agent Service para analizar tus datos de ventas:

![Agentic Service In Action](../../../translated_images/es/agent-service-in-action.34fb465c9a84659e.webp)

Para usar cualquiera de estas herramientas con el servicio, podemos crear un cliente y definir una herramienta o conjunto de herramientas. Para implementarlo prácticamente, podemos usar el siguiente código Python. El LLM podrá examinar el conjunto de herramientas y decidir si usa la función creada por el usuario, `fetch_sales_data_using_sqlite_query`, o el Intérprete de Código preconstruido dependiendo de la solicitud del usuario.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # función fetch_sales_data_using_sqlite_query que se encuentra en un archivo fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializar el conjunto de herramientas
toolset = ToolSet()

# Inicializar el agente de llamada a función con la función fetch_sales_data_using_sqlite_query y agregarlo al conjunto de herramientas
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializar la herramienta Code Interpreter y agregarla al conjunto de herramientas.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ¿Cuáles son las consideraciones especiales para usar el Patrón de Diseño de Uso de Herramientas para construir agentes de IA confiables?

Una preocupación común con SQL generado dinámicamente por LLMs es la seguridad, particularmente el riesgo de inyección de SQL o acciones maliciosas, como eliminar o manipular la base de datos. Si bien estas preocupaciones son válidas, pueden mitigarse eficazmente configurando apropiadamente los permisos de acceso a la base de datos. Para la mayoría de las bases de datos esto implica configurar la base de datos como solo lectura. Para servicios de base de datos como PostgreSQL o Azure SQL, la aplicación debe tener asignado un rol de solo lectura (SELECT).
Ejecutar la aplicación en un entorno seguro mejora aún más la protección. En escenarios empresariales, normalmente se extraen y transforman los datos de los sistemas operativos a una base de datos o almacén de datos de solo lectura con un esquema amigable para el usuario. Este enfoque garantiza que los datos estén seguros, optimizados para el rendimiento y la accesibilidad, y que la aplicación tenga acceso restringido y de solo lectura.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ¿Tienes más preguntas sobre el uso de patrones de diseño de la herramienta?

Únete al [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) para reunirte con otros estudiantes, asistir a horas de oficina y obtener respuestas a tus preguntas sobre AI Agents.

## Recursos adicionales

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Taller de Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Taller Multi-Agentes Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutorial de llamada a funciones en Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Intérprete de código de Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Herramientas Autogen</a>

## Lección anterior

[Entendiendo los patrones de diseño agéntico](../03-agentic-design-patterns/README.md)

## Próxima lección

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No nos hacemos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->