<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T10:52:24+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "es"
}
-->
[![Explorando Marcos de Agentes de IA](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.es.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Explorar Marcos de Agentes de IA

Los marcos de agentes de IA son plataformas de software diseñadas para simplificar la creación, implementación y gestión de agentes de IA. Estos marcos proporcionan a los desarrolladores componentes preconstruidos, abstracciones y herramientas que agilizan el desarrollo de sistemas de IA complejos.

Estos marcos ayudan a los desarrolladores a centrarse en los aspectos únicos de sus aplicaciones al proporcionar enfoques estandarizados para los desafíos comunes en el desarrollo de agentes de IA. Mejoran la escalabilidad, accesibilidad y eficiencia en la construcción de sistemas de IA.

## Introducción 

Esta lección cubrirá:

- ¿Qué son los Marcos de Agentes de IA y qué permiten lograr a los desarrolladores?
- ¿Cómo pueden los equipos usarlos para prototipar rápidamente, iterar y mejorar las capacidades de sus agentes?
- ¿Cuáles son las diferencias entre los marcos y herramientas creados por Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> y <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- ¿Puedo integrar directamente mis herramientas existentes del ecosistema de Azure o necesito soluciones independientes?
- ¿Qué es el servicio Azure AI Agents y cómo me está ayudando?

## Objetivos de aprendizaje

Los objetivos de esta lección son ayudarte a entender:

- El papel de los Marcos de Agentes de IA en el desarrollo de IA.
- Cómo aprovechar los Marcos de Agentes de IA para construir agentes inteligentes.
- Capacidades clave habilitadas por los Marcos de Agentes de IA.
- Las diferencias entre AutoGen, Semantic Kernel y Azure AI Agent Service.

## ¿Qué son los Marcos de Agentes de IA y qué permiten hacer a los desarrolladores?

Los marcos tradicionales de IA pueden ayudarte a integrar IA en tus aplicaciones y mejorar estas aplicaciones de las siguientes maneras:

- **Personalización**: La IA puede analizar el comportamiento y las preferencias del usuario para proporcionar recomendaciones, contenido y experiencias personalizadas.  
Ejemplo: Servicios de streaming como Netflix usan IA para sugerir películas y programas basados en el historial de visualización, mejorando el compromiso y la satisfacción del usuario.
- **Automatización y Eficiencia**: La IA puede automatizar tareas repetitivas, optimizar flujos de trabajo y mejorar la eficiencia operativa.  
Ejemplo: Las aplicaciones de servicio al cliente usan chatbots impulsados por IA para manejar consultas comunes, reduciendo los tiempos de respuesta y liberando a los agentes humanos para problemas más complejos.
- **Mejora de la Experiencia del Usuario**: La IA puede mejorar la experiencia general del usuario proporcionando funciones inteligentes como reconocimiento de voz, procesamiento de lenguaje natural y texto predictivo.  
Ejemplo: Asistentes virtuales como Siri y Google Assistant usan IA para entender y responder a comandos de voz, facilitando la interacción de los usuarios con sus dispositivos.

### Todo eso suena genial, ¿verdad? Entonces, ¿por qué necesitamos el Marco de Agentes de IA?

Los marcos de agentes de IA representan algo más que simples marcos de IA. Están diseñados para permitir la creación de agentes inteligentes que puedan interactuar con usuarios, otros agentes y el entorno para lograr objetivos específicos. Estos agentes pueden exhibir comportamientos autónomos, tomar decisiones y adaptarse a condiciones cambiantes. Veamos algunas capacidades clave habilitadas por los Marcos de Agentes de IA:

- **Colaboración y Coordinación entre Agentes**: Permiten la creación de múltiples agentes de IA que pueden trabajar juntos, comunicarse y coordinarse para resolver tareas complejas.
- **Automatización y Gestión de Tareas**: Proporcionan mecanismos para automatizar flujos de trabajo de varios pasos, delegación de tareas y gestión dinámica de tareas entre agentes.
- **Comprensión Contextual y Adaptación**: Equipan a los agentes con la capacidad de entender el contexto, adaptarse a entornos cambiantes y tomar decisiones basadas en información en tiempo real.

En resumen, los agentes te permiten hacer más, llevar la automatización al siguiente nivel y crear sistemas más inteligentes que puedan adaptarse y aprender de su entorno.

## ¿Cómo prototipar rápidamente, iterar y mejorar las capacidades del agente?

Este es un panorama en constante evolución, pero hay algunas cosas comunes en la mayoría de los Marcos de Agentes de IA que pueden ayudarte a prototipar e iterar rápidamente, como componentes modulares, herramientas colaborativas y aprendizaje en tiempo real. Vamos a profundizar en estos:

- **Usar Componentes Modulares**: Los SDK de IA ofrecen componentes preconstruidos como conectores de IA y Memoria, llamadas a funciones usando lenguaje natural o complementos de código, plantillas de prompts y más.
- **Aprovechar Herramientas Colaborativas**: Diseñar agentes con roles y tareas específicas, permitiendo probar y refinar flujos de trabajo colaborativos.
- **Aprender en Tiempo Real**: Implementar bucles de retroalimentación donde los agentes aprendan de las interacciones y ajusten su comportamiento dinámicamente.

### Usar Componentes Modulares

SDKs como Microsoft Semantic Kernel y LangChain ofrecen componentes preconstruidos como conectores de IA, plantillas de prompts y gestión de memoria.

**Cómo los equipos pueden usarlos**: Los equipos pueden ensamblar rápidamente estos componentes para crear un prototipo funcional sin empezar desde cero, permitiendo una experimentación e iteración rápidas.

**Cómo funciona en la práctica**: Puedes usar un analizador preconstruido para extraer información de la entrada del usuario, un módulo de memoria para almacenar y recuperar datos, y un generador de prompts para interactuar con los usuarios, todo sin tener que construir estos componentes desde cero.

**Ejemplo de código**. Veamos ejemplos de cómo puedes usar un Conector de IA preconstruido con Semantic Kernel en Python y .Net que utiliza llamadas automáticas a funciones para que el modelo responda a la entrada del usuario:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```
  
Lo que puedes ver en este ejemplo es cómo puedes aprovechar un analizador preconstruido para extraer información clave de la entrada del usuario, como el origen, destino y fecha de una solicitud de reserva de vuelo. Este enfoque modular te permite centrarte en la lógica de alto nivel.

### Aprovechar Herramientas Colaborativas

Marcos como CrewAI, Microsoft AutoGen y Semantic Kernel facilitan la creación de múltiples agentes que pueden trabajar juntos.

**Cómo los equipos pueden usarlos**: Los equipos pueden diseñar agentes con roles y tareas específicas, permitiendo probar y refinar flujos de trabajo colaborativos y mejorar la eficiencia general del sistema.

**Cómo funciona en la práctica**: Puedes crear un equipo de agentes donde cada agente tenga una función especializada, como recuperación de datos, análisis o toma de decisiones. Estos agentes pueden comunicarse y compartir información para lograr un objetivo común, como responder a una consulta del usuario o completar una tarea.

**Ejemplo de código (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```
  
Lo que ves en el código anterior es cómo puedes crear una tarea que involucra a múltiples agentes trabajando juntos para analizar datos. Cada agente realiza una función específica, y la tarea se ejecuta coordinando a los agentes para lograr el resultado deseado. Al crear agentes dedicados con roles especializados, puedes mejorar la eficiencia y el rendimiento de las tareas.

### Aprender en Tiempo Real

Los marcos avanzados proporcionan capacidades para la comprensión del contexto en tiempo real y la adaptación.

**Cómo los equipos pueden usarlos**: Los equipos pueden implementar bucles de retroalimentación donde los agentes aprendan de las interacciones y ajusten su comportamiento dinámicamente, lo que lleva a una mejora continua y refinamiento de las capacidades.

**Cómo funciona en la práctica**: Los agentes pueden analizar la retroalimentación del usuario, datos del entorno y resultados de tareas para actualizar su base de conocimiento, ajustar algoritmos de toma de decisiones y mejorar el rendimiento con el tiempo. Este proceso de aprendizaje iterativo permite a los agentes adaptarse a condiciones cambiantes y preferencias del usuario, mejorando la efectividad general del sistema.

## ¿Cuáles son las diferencias entre los marcos AutoGen, Semantic Kernel y Azure AI Agent Service?

Existen muchas formas de comparar estos marcos, pero veamos algunas diferencias clave en términos de su diseño, capacidades y casos de uso objetivo:

## AutoGen

AutoGen es un marco de código abierto desarrollado por el Laboratorio de Fronteras de IA de Microsoft Research. Se centra en aplicaciones *agénticas* distribuidas y basadas en eventos, habilitando múltiples LLMs y SLMs, herramientas y patrones avanzados de diseño multiagente.

AutoGen se basa en el concepto central de agentes, que son entidades autónomas que pueden percibir su entorno, tomar decisiones y realizar acciones para lograr objetivos específicos. Los agentes se comunican a través de mensajes asincrónicos, lo que les permite trabajar de forma independiente y en paralelo, mejorando la escalabilidad y capacidad de respuesta del sistema.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Los agentes están basados en el modelo de actor</a>. Según Wikipedia, un actor es _el bloque básico de construcción de la computación concurrente. En respuesta a un mensaje que recibe, un actor puede: tomar decisiones locales, crear más actores, enviar más mensajes y determinar cómo responder al próximo mensaje recibido_.

**Casos de Uso**: Automatización de generación de código, tareas de análisis de datos y construcción de agentes personalizados para funciones de planificación e investigación.

Aquí tienes algunos conceptos clave de AutoGen:

- **Agentes**. Un agente es una entidad de software que:
  - **Se comunica mediante mensajes**, que pueden ser sincrónicos o asincrónicos.
  - **Mantiene su propio estado**, que puede ser modificado por mensajes entrantes.
  - **Realiza acciones** en respuesta a mensajes recibidos o cambios en su estado. Estas acciones pueden modificar el estado del agente y producir efectos externos, como actualizar registros de mensajes, enviar nuevos mensajes, ejecutar código o realizar llamadas a API.
    
  Aquí tienes un fragmento de código breve en el que creas tu propio agente con capacidades de chat:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
  
    En el código anterior, se ha creado `MyAgent` que hereda de `RoutedAgent`. Tiene un manejador de mensajes que imprime el contenido del mensaje y luego envía una respuesta usando el delegado `AssistantAgent`. Nota especialmente cómo asignamos a `self._delegate` una instancia de `AssistantAgent`, que es un agente preconstruido que puede manejar completaciones de chat.

    Informemos a AutoGen sobre este tipo de agente y pongamos en marcha el programa a continuación:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```
  
    En el código anterior, los agentes se registran con el entorno de ejecución y luego se envía un mensaje al agente, lo que da como resultado la siguiente salida:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```
  
- **Multiagentes**. AutoGen admite la creación de múltiples agentes que pueden trabajar juntos para lograr tareas complejas. Los agentes pueden comunicarse, compartir información y coordinar sus acciones para resolver problemas de manera más eficiente. Para crear un sistema multiagente, puedes definir diferentes tipos de agentes con funciones y roles especializados, como recuperación de datos, análisis, toma de decisiones e interacción con el usuario. Veamos cómo se ve una creación de este tipo para hacernos una idea:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```
  
    En el código anterior, tenemos un `GroupChatManager` que está registrado con el entorno de ejecución. Este administrador es responsable de coordinar las interacciones entre diferentes tipos de agentes, como escritores, ilustradores, editores y usuarios.

- **Entorno de Ejecución de Agentes**. El marco proporciona un entorno de ejecución, habilitando la comunicación entre agentes, gestionando sus identidades y ciclos de vida, y aplicando límites de seguridad y privacidad. Esto significa que puedes ejecutar tus agentes en un entorno seguro y controlado, asegurando que puedan interactuar de manera segura y eficiente. Hay dos entornos de ejecución de interés:
  - **Entorno de ejecución independiente**. Es una buena opción para aplicaciones de un solo proceso donde todos los agentes están implementados en el mismo lenguaje de programación y se ejecutan en el mismo proceso. Aquí tienes una ilustración de cómo funciona:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Entorno de ejecución independiente</a>  
Pila de aplicaciones

    *los agentes se comunican mediante mensajes a través del entorno de ejecución, y este gestiona el ciclo de vida de los agentes*

  - **Entorno de ejecución distribuido**, es adecuado para aplicaciones multiproceso donde los agentes pueden estar implementados en diferentes lenguajes de programación y ejecutándose en diferentes máquinas. Aquí tienes una ilustración de cómo funciona:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Entorno de ejecución distribuido</a>

## Semantic Kernel + Marco de Agentes

Semantic Kernel es un SDK de orquestación de IA listo para empresas. Consiste en conectores de IA y memoria, junto con un Marco de Agentes.

Primero cubramos algunos componentes clave:

- **Conectores de IA**: Esta es una interfaz con servicios de IA externos y fuentes de datos para su uso tanto en Python como en C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  
  
    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```
  
    Aquí tienes un ejemplo simple de cómo puedes crear un kernel y agregar un servicio de completado de chat. Semantic Kernel crea una conexión con un servicio de IA externo, en este caso, Azure OpenAI Chat Completion.

- **Plugins**: Estos encapsulan funciones que una aplicación puede usar. Hay tanto plugins listos para usar como personalizados que puedes crear. Un concepto relacionado son las "funciones de prompt". En lugar de proporcionar indicaciones en lenguaje natural para la invocación de funciones, transmites ciertas funciones al modelo. Basado en el contexto actual del chat, el modelo puede elegir llamar a una de estas funciones para completar una solicitud o consulta. Aquí tienes un ejemplo:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```
  
    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```
  
    Aquí, primero tienes un prompt de plantilla `skPrompt` que deja espacio para que el usuario ingrese texto, `$userInput`. Luego creas la función del kernel `SummarizeText` y la importas al kernel con el nombre del plugin `SemanticFunctions`. Nota el nombre de la función que ayuda a Semantic Kernel a entender qué hace la función y cuándo debería ser llamada.

- **Función Nativa**: También hay funciones nativas que el marco puede llamar directamente para llevar a cabo la tarea. Aquí tienes un ejemplo de una función de este tipo que recupera el contenido de un archivo:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```
  
- **Memoria**: Abstrae y simplifica la gestión del contexto para aplicaciones de IA. La idea con la memoria es que esto es algo que el LLM debería conocer. Puedes almacenar esta información en un almacén vectorial que termina siendo una base de datos en memoria o una base de datos vectorial o similar. Aquí tienes un ejemplo de un escenario muy simplificado donde se agregan *hechos* a la memoria:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```
  
Estos hechos se almacenan en la colección de memoria `SummarizedAzureDocs`. Este es un ejemplo muy simplificado, pero puedes ver cómo se puede almacenar información en la memoria para que el LLM la utilice.

Así que esos son los conceptos básicos del marco de Semantic Kernel, ¿qué hay del Marco de Agentes?

## Servicio de Agentes de Azure AI

El Servicio de Agentes de Azure AI es una incorporación más reciente, presentada en Microsoft Ignite 2024. Permite el desarrollo y despliegue de agentes de IA con modelos más flexibles, como la llamada directa a LLMs de código abierto como Llama 3, Mistral y Cohere.

El Servicio de Agentes de Azure AI ofrece mecanismos de seguridad empresarial más sólidos y métodos de almacenamiento de datos, lo que lo hace adecuado para aplicaciones empresariales.

Funciona de manera inmediata con marcos de orquestación de múltiples agentes como AutoGen y Semantic Kernel.

Este servicio está actualmente en Vista Previa Pública y admite Python y C# para la creación de agentes.

Usando Semantic Kernel en Python, podemos crear un Agente de Azure AI con un plugin definido por el usuario:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Conceptos clave

El Servicio de Agentes de Azure AI tiene los siguientes conceptos clave:

- **Agente**. El Servicio de Agentes de Azure AI se integra con Azure AI Foundry. Dentro de AI Foundry, un Agente de IA actúa como un microservicio "inteligente" que puede usarse para responder preguntas (RAG), realizar acciones o automatizar completamente flujos de trabajo. Logra esto combinando el poder de los modelos generativos de IA con herramientas que le permiten acceder e interactuar con fuentes de datos del mundo real. Aquí hay un ejemplo de un agente:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    En este ejemplo, se crea un agente con el modelo `gpt-4o-mini`, un nombre `my-agent` y las instrucciones `You are helpful agent`. El agente está equipado con herramientas y recursos para realizar tareas de interpretación de código.

- **Hilo y mensajes**. El hilo es otro concepto importante. Representa una conversación o interacción entre un agente y un usuario. Los hilos se pueden usar para rastrear el progreso de una conversación, almacenar información de contexto y gestionar el estado de la interacción. Aquí hay un ejemplo de un hilo:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    En el código anterior, se crea un hilo. Posteriormente, se envía un mensaje al hilo. Al llamar a `create_and_process_run`, se le pide al agente que realice un trabajo en el hilo. Finalmente, los mensajes se recuperan y registran para ver la respuesta del agente. Los mensajes indican el progreso de la conversación entre el usuario y el agente. También es importante entender que los mensajes pueden ser de diferentes tipos, como texto, imagen o archivo, es decir, el trabajo del agente ha resultado, por ejemplo, en una imagen o una respuesta de texto. Como desarrollador, puedes usar esta información para procesar aún más la respuesta o presentarla al usuario.

- **Integración con otros marcos de IA**. El Servicio de Agentes de Azure AI puede interactuar con otros marcos como AutoGen y Semantic Kernel, lo que significa que puedes construir parte de tu aplicación en uno de estos marcos y, por ejemplo, usar el Servicio de Agentes como un orquestador o construir todo en el Servicio de Agentes.

**Casos de uso**: El Servicio de Agentes de Azure AI está diseñado para aplicaciones empresariales que requieren un despliegue de agentes de IA seguro, escalable y flexible.

## ¿Cuál es la diferencia entre estos marcos?

Parece que hay mucho solapamiento entre estos marcos, pero hay algunas diferencias clave en términos de su diseño, capacidades y casos de uso objetivo:

- **AutoGen**: Es un marco de experimentación enfocado en la investigación de vanguardia sobre sistemas de múltiples agentes. Es el mejor lugar para experimentar y prototipar sistemas sofisticados de múltiples agentes.
- **Semantic Kernel**: Es una biblioteca de agentes lista para producción para construir aplicaciones empresariales agentivas. Se centra en aplicaciones agentivas distribuidas y basadas en eventos, habilitando múltiples LLMs y SLMs, herramientas y patrones de diseño de agentes individuales/múltiples.
- **Servicio de Agentes de Azure AI**: Es una plataforma y servicio de despliegue en Azure Foundry para agentes. Ofrece conectividad a servicios compatibles con Azure Foundry como Azure OpenAI, Azure AI Search, Bing Search y ejecución de código.

¿Aún no estás seguro de cuál elegir?

### Casos de uso

Veamos si podemos ayudarte revisando algunos casos de uso comunes:

> P: Estoy experimentando, aprendiendo y construyendo aplicaciones de agentes como prueba de concepto, y quiero poder construir y experimentar rápidamente.
>

>R: AutoGen sería una buena opción para este escenario, ya que se centra en aplicaciones agentivas distribuidas y basadas en eventos y admite patrones avanzados de diseño de múltiples agentes.

> P: ¿Qué hace que AutoGen sea una mejor opción que Semantic Kernel y el Servicio de Agentes de Azure AI para este caso de uso?
>
> R: AutoGen está diseñado específicamente para aplicaciones agentivas distribuidas y basadas en eventos, lo que lo hace muy adecuado para automatizar tareas de generación de código y análisis de datos. Proporciona las herramientas y capacidades necesarias para construir sistemas complejos de múltiples agentes de manera eficiente.

>P: Parece que el Servicio de Agentes de Azure AI también podría funcionar aquí, ¿tiene herramientas para la generación de código y más?

>
> R: Sí, el Servicio de Agentes de Azure AI es una plataforma de servicio para agentes y agrega capacidades integradas para múltiples modelos, Azure AI Search, Bing Search y Azure Functions. Facilita la construcción de tus agentes en el Portal Foundry y su despliegue a escala.

> P: Todavía estoy confundido, solo dame una opción.
>
> R: Una gran opción es construir tu aplicación en Semantic Kernel primero y luego usar el Servicio de Agentes de Azure AI para desplegar tu agente. Este enfoque te permite persistir fácilmente tus agentes mientras aprovechas el poder de construir sistemas de múltiples agentes en Semantic Kernel. Además, Semantic Kernel tiene un conector en AutoGen, lo que facilita el uso de ambos marcos juntos.

Resumamos las diferencias clave en una tabla:

| Marco | Enfoque | Conceptos Clave | Casos de Uso |
| --- | --- | --- | --- |
| AutoGen | Aplicaciones agentivas distribuidas y basadas en eventos | Agentes, Personas, Funciones, Datos | Generación de código, tareas de análisis de datos |
| Semantic Kernel | Comprensión y generación de contenido similar al humano | Agentes, Componentes Modulares, Colaboración | Comprensión del lenguaje natural, generación de contenido |
| Servicio de Agentes de Azure AI | Modelos flexibles, seguridad empresarial, Generación de código, Llamadas a herramientas | Modularidad, Colaboración, Orquestación de Procesos | Despliegue de agentes de IA seguro, escalable y flexible |

¿Cuál es el caso de uso ideal para cada uno de estos marcos?

## ¿Puedo integrar directamente mis herramientas existentes del ecosistema de Azure, o necesito soluciones independientes?

La respuesta es sí, puedes integrar tus herramientas existentes del ecosistema de Azure directamente con el Servicio de Agentes de Azure AI, especialmente porque ha sido diseñado para trabajar sin problemas con otros servicios de Azure. Por ejemplo, podrías integrar Bing, Azure AI Search y Azure Functions. También hay una integración profunda con Azure AI Foundry.

Para AutoGen y Semantic Kernel, también puedes integrarte con servicios de Azure, pero puede requerir que llames a los servicios de Azure desde tu código. Otra forma de integrarse es usar los SDKs de Azure para interactuar con los servicios de Azure desde tus agentes. Además, como se mencionó, puedes usar el Servicio de Agentes de Azure AI como un orquestador para tus agentes construidos en AutoGen o Semantic Kernel, lo que facilitaría el acceso al ecosistema de Azure.

## Códigos de Ejemplo

- Python: [Marco de Agentes](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Marco de Agentes](./code_samples/02-dotnet-agent-framework.md)

## ¿Tienes más preguntas sobre los Marcos de Agentes de IA?

Únete al [Discord de Azure AI Foundry](https://aka.ms/ai-agents/discord) para conectarte con otros aprendices, asistir a horas de oficina y resolver tus dudas sobre Agentes de IA.

## Referencias

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Servicio de Agentes de Azure</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel y AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Marco de Agentes de Semantic Kernel en Python</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Marco de Agentes de Semantic Kernel en .Net</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Servicio de Agentes de Azure AI</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Usando el Servicio de Agentes de Azure AI con AutoGen / Semantic Kernel para construir una solución de múltiples agentes</a>

## Lección Anterior

[Introducción a los Agentes de IA y Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima Lección

[Entendiendo los Patrones de Diseño Agentivos](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->