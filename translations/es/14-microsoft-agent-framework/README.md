# Explorando Microsoft Agent Framework

![Agent Framework](../../../translated_images/es/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introducción

Esta lección cubrirá:

- Comprender Microsoft Agent Framework: características clave y valor  
- Explorando los conceptos clave de Microsoft Agent Framework
- Patrones avanzados de MAF: flujos de trabajo, middleware y memoria

## Objetivos de aprendizaje

Después de completar esta lección, sabrás cómo:

- Construir agentes de inteligencia artificial listos para producción usando Microsoft Agent Framework
- Aplicar las características principales de Microsoft Agent Framework en tus casos de uso agentic
- Usar patrones avanzados incluyendo flujos de trabajo, middleware y observabilidad

## Ejemplos de código 

Los ejemplos de código para [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) pueden encontrarse en este repositorio bajo los archivos `xx-python-agent-framework` y `xx-dotnet-agent-framework`.

## Comprendiendo Microsoft Agent Framework

![Framework Intro](../../../translated_images/es/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) es el marco unificado de Microsoft para construir agentes IA. Ofrece la flexibilidad para abordar la amplia variedad de casos de uso agentic que se ven tanto en ambientes de producción como de investigación incluyendo:

- **Orquestación secuencial de agentes** en escenarios donde se necesitan flujos de trabajo paso a paso.
- **Orquestación concurrente** en escenarios donde los agentes necesitan completar tareas al mismo tiempo.
- **Orquestación de chat en grupo** en escenarios donde los agentes pueden colaborar juntos en una tarea.
- **Orquestación de traspasos** en escenarios donde los agentes pasan la tarea entre sí conforme se completan las subtareas.
- **Orquestación magnética** en escenarios donde un agente gestor crea y modifica una lista de tareas y maneja la coordinación de subagentes para completar la tarea.

Para entregar agentes IA en producción, MAF también incluye características para:

- **Observabilidad** mediante el uso de OpenTelemetry donde cada acción del Agente IA incluyendo la invocación de herramientas, pasos de orquestación, flujos de razonamiento y monitoreo de rendimiento son capturados a través de los paneles de Microsoft Foundry.
- **Seguridad** alojando agentes nativamente en Microsoft Foundry que incluye controles de seguridad como acceso basado en roles, manejo de datos privados y seguridad integrada de contenido.
- **Durabilidad** ya que los hilos y flujos de trabajo del agente pueden pausarse, reanudarse y recuperarse de errores, lo que habilita procesos de larga duración.
- **Control** ya que se soportan flujos de trabajo con intervención humana donde las tareas se marcan como requerimiento de aprobación humana.

Microsoft Agent Framework también se enfoca en ser interoperable mediante:

- **Ser independiente de la nube** - Los agentes pueden ejecutarse en contenedores, localmente y en múltiples nubes diferentes.
- **Ser independiente del proveedor** - Los agentes pueden crearse mediante tu SDK preferido incluyendo Azure OpenAI y OpenAI.
- **Integrar estándares abiertos** - Los agentes pueden utilizar protocolos como Agent-to-Agent (A2A) y Model Context Protocol (MCP) para descubrir y usar otros agentes y herramientas.
- **Plugins y conectores** - Se pueden hacer conexiones a servicios de datos y memoria como Microsoft Fabric, SharePoint, Pinecone y Qdrant.

Veamos cómo estas características se aplican a algunos de los conceptos clave de Microsoft Agent Framework.

## Conceptos clave de Microsoft Agent Framework

### Agentes

![Agent Framework](../../../translated_images/es/agent-components.410a06daf87b4fef.webp)

**Creando agentes**

La creación de agentes se realiza definiendo el servicio de inferencia (proveedor LLM), un
conjunto de instrucciones para que el agente IA siga, y un `nombre` asignado:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Lo anterior usa `Azure OpenAI` pero los agentes pueden crearse usando una variedad de servicios incluyendo `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI APIs `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o [MiniMax](https://platform.minimaxi.com/), que proporciona una API compatible con OpenAI con ventanas de contexto grandes (hasta 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o agentes remotos usando el protocolo A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ejecutando agentes**

Los agentes se ejecutan usando los métodos `.run` o `.run_stream` para respuestas no streaming o streaming respectivamente.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Cada ejecución de agente puede tener opciones para personalizar parámetros como `max_tokens` usado por el agente, `tools` que el agente puede llamar, e incluso el `modelo` mismo usado por el agente.

Esto es útil en casos donde se requieren modelos o herramientas específicos para completar la tarea del usuario.

**Herramientas**

Las herramientas pueden definirse tanto al definir el agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Al crear un ChatAgent directamente

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

y también al ejecutar el agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Herramienta proporcionada solo para esta ejecución )
```

**Hilos de agente**

Los hilos de agente se usan para manejar conversaciones de varios turnos. Los hilos pueden crearse ya sea:

- Usando `get_new_thread()` que permite que el hilo sea guardado a lo largo del tiempo
- Creando un hilo automáticamente al ejecutar un agente y solo durar el hilo durante esa ejecución.

Para crear un hilo, el código es así:

```python
# Crear un nuevo hilo.
thread = agent.get_new_thread() # Ejecutar el agente con el hilo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Luego puedes serializar el hilo para almacenarlo y usarlo más tarde:

```python
# Crear un nuevo hilo.
thread = agent.get_new_thread() 

# Ejecutar el agente con el hilo.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializar el hilo para almacenamiento.

serialized_thread = await thread.serialize() 

# Deserializar el estado del hilo después de cargarlo desde el almacenamiento.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware de agente**

Los agentes interactúan con herramientas y LLMs para completar las tareas de los usuarios. En ciertos escenarios, queremos ejecutar o rastrear acciones entre estas interacciones. El middleware de agente nos permite hacer esto mediante:

*Middleware de función*

Este middleware nos permite ejecutar una acción entre el agente y una función/herramienta que llamará. Un ejemplo de cuando se usaría es para hacer algún registro del llamado de función.

En el código abajo `next` define si se debe llamar al siguiente middleware o a la función actual.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Preprocesamiento: Registrar antes de la ejecución de la función
    print(f"[Function] Calling {context.function.name}")

    # Continuar al siguiente middleware o ejecución de la función
    await next(context)

    # Postprocesamiento: Registrar después de la ejecución de la función
    print(f"[Function] {context.function.name} completed")
```

*Middleware de chat*

Este middleware nos permite ejecutar o registrar una acción entre el agente y las solicitudes al LLM.

Esto contiene información importante como los `messages` que se envían al servicio de IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Preprocesamiento: Registrar antes de la llamada a IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuar al siguiente middleware o servicio de IA
    await next(context)

    # Postprocesamiento: Registrar después de la respuesta de IA
    print("[Chat] AI response received")

```

**Memoria de agente**

Como se cubre en la lección `Agentic Memory`, la memoria es un elemento importante que habilita que el agente opere sobre diferentes contextos. MAF ofrece varios tipos diferentes de memorias:

*Almacenamiento en memoria*

Esta es la memoria almacenada en hilos durante la ejecución de la aplicación.

```python
# Crear un nuevo hilo.
thread = agent.get_new_thread() # Ejecutar el agente con el hilo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mensajes persistentes*

Esta memoria se usa para almacenar el historial de conversación a través de diferentes sesiones. Se define usando `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Crear una tienda de mensajes personalizada
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memoria dinámica*

Esta memoria se añade al contexto antes de ejecutar a los agentes. Estas memorias pueden almacenarse en servicios externos como mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Usando Mem0 para capacidades avanzadas de memoria
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Observabilidad de agente**

La observabilidad es importante para construir sistemas agentic confiables y mantenibles. MAF se integra con OpenTelemetry para proveer trazabilidad y métricas para una mejor observabilidad.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # hacer algo
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Flujos de trabajo

MAF ofrece flujos de trabajo que son pasos predefinidos para completar una tarea e incluyen agentes IA como componentes en esos pasos.

Los flujos de trabajo están compuestos por diferentes componentes que permiten un mejor control del flujo. Los flujos también habilitan la **orquestación multi-agente** y el **checkpointing** para guardar estados del flujo.

Los componentes principales de un flujo de trabajo son:

**Ejecutores**

Los ejecutores reciben mensajes de entrada, realizan sus tareas asignadas y luego producen un mensaje de salida. Esto mueve el flujo de trabajo hacia adelante para completar la tarea mayor. Los ejecutores pueden ser agentes IA o lógica personalizada.

**Aristas**

Las aristas se usan para definir el flujo de mensajes en un flujo de trabajo. Estas pueden ser:

*Aristas directas* - Conexiones simples de uno a uno entre ejecutores:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Aristas condicionales* - Se activan después de que una condición se cumple. Por ejemplo, cuando las habitaciones de hotel no están disponibles, un ejecutor puede sugerir otras opciones.

*Aristas de tipo switch-case* - Dirigen mensajes a diferentes ejecutores basados en condiciones definidas. Por ejemplo, si un cliente de viaje tiene acceso prioritario y sus tareas serán manejadas por otro flujo de trabajo.

*Aristas fan-out* - Envían un mensaje a múltiples destinos.

*Aristas fan-in* - Recogen múltiples mensajes de diferentes ejecutores y los envían a un solo destino.

**Eventos**

Para proveer mejor observabilidad en los flujos de trabajo, MAF ofrece eventos incorporados para la ejecución incluyendo:

- `WorkflowStartedEvent`  - Comienzo de la ejecución del flujo de trabajo
- `WorkflowOutputEvent` - El flujo de trabajo produce una salida
- `WorkflowErrorEvent` - El flujo de trabajo encuentra un error
- `ExecutorInvokeEvent`  - El ejecutor empieza el procesamiento
- `ExecutorCompleteEvent`  -  El ejecutor termina el procesamiento
- `RequestInfoEvent` - Se emite una solicitud

## Patrones avanzados de MAF

Las secciones anteriores cubren los conceptos clave de Microsoft Agent Framework. Al construir agentes más complejos, aquí hay algunos patrones avanzados a considerar:

- **Composición de middleware**: Encadena múltiples manejadores de middleware (registro, autenticación, limitación de tasa) usando middleware de función y chat para control detallado del comportamiento del agente.
- **Checkpointing en flujos de trabajo**: Usa eventos del flujo de trabajo y serialización para guardar y reanudar procesos de agentes de larga duración.
- **Selección dinámica de herramientas**: Combina RAG sobre descripciones de herramientas con el registro de herramientas de MAF para presentar solo herramientas relevantes por consulta.
- **Traspaso multi-agente**: Usa aristas de flujo y enrutamiento condicional para orquestar traspasos entre agentes especializados.

## Alojar agentes LangChain / LangGraph en Microsoft Foundry

Microsoft Agent Framework es **interoperable con otros frameworks** — no estás limitado a agentes escritos con MAF. Si ya tienes un agente construido con **LangChain** o **LangGraph**, puedes ejecutarlo como un **agente alojado en Microsoft Foundry** para que Foundry maneje el tiempo de ejecución, sesiones, escalabilidad, identidad y puntos finales de protocolo para ti, mientras tu lógica de agente permanece en LangGraph.

Esto se realiza con el paquete `langchain_azure_ai.agents.hosting`, que expone un gráfico LangGraph compilado sobre los mismos protocolos que usan los agentes alojados en Foundry.

**1. Instala el extra hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

El extra de `hosting` instala las bibliotecas de protocolo Foundry: `azure-ai-agentserver-responses` (el endpoint `/responses` compatible con OpenAI) y `azure-ai-agentserver-invocations` (el endpoint genérico `/invocations`).

**2. Elige un protocolo de hosting:**

| Protocolo | Clase host | Endpoint | Úsalo cuando |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Quieras chat compatible con OpenAI, streaming, historial de respuestas y hilos de conversación — el recomendado por defecto para agentes conversacionales. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Necesites una forma JSON personalizada, un endpoint estilo webhook o procesamiento no conversacional. |

Como la **API Responses es la API primaria para desarrollo de agentes en Foundry**, comienza con `ResponsesHostServer` para la mayoría de agentes.

**3. Configura las variables de entorno** (`az login` primero para que `DefaultAzureCredential` pueda autenticarse):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Cuando el agente se ejecute más tarde como agente alojado en Foundry, la plataforma inyecta automáticamente `FOUNDRY_PROJECT_ENDPOINT`.

**4. Expón un agente LangGraph sobre el protocolo Responses:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI aquí apunta al endpoint compatible con OpenAI (Respuestas) del proyecto Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Ejecútalo localmente con `python main.py`, luego envía una solicitud Responses a `http://localhost:8088/responses`.

**Comportamientos clave:**

- **Conversaciones**: Los clientes continúan una conversación pasando `previous_response_id` o un ID de `conversation`. Si tu gráfico está compilado con un checkpointer LangGraph, Foundry asocia el estado de la conversación al checkpoint (usa un checkpointer duradero en producción; `MemorySaver` está bien para pruebas locales).
- **Intervención humana**: Si tu gráfico usa LangGraph `interrupt()`, `ResponsesHostServer` presenta la interrupción pendiente como un ítem de `function_call` / `mcp_approval_request` en Responses, y los clientes reanudan con una respuesta correspondiente `function_call_output` / `mcp_approval_response`.
- **Desplegar en Foundry**: Usa Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, requiere Docker), luego `azd provision` y `azd deploy`. El despliegue de agentes alojados requiere el rol **Foundry Project Manager**.

Una versión ejecutable de este ejemplo está en [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Para la guía completa (protocolo Invocations, esquemas de solicitud personalizados y solución de problemas), ve a [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ejemplos de código 

Los ejemplos de código para Microsoft Agent Framework pueden encontrarse en este repositorio bajo los archivos `xx-python-agent-framework` y `xx-dotnet-agent-framework`.

## ¿Tienes más preguntas sobre Microsoft Agent Framework?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros estudiantes, asistir a horas de oficina y obtener respuestas a tus preguntas sobre agentes IA.
## Lección anterior

[Memoria para agentes IA](../13-agent-memory/README.md)

## Próxima lección

[Construyendo agentes de uso de computadoras (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->