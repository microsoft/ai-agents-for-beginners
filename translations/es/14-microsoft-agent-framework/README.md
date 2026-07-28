# Explorando Microsoft Agent Framework

![Agent Framework](../../../translated_images/es/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introducción

Esta lección cubrirá:

- Comprendiendo Microsoft Agent Framework: Características clave y valor  
- Explorando los conceptos clave de Microsoft Agent Framework
- Patrones avanzados de MAF: Flujos de trabajo, middleware y memoria

## Objetivos de aprendizaje

Después de completar esta lección, sabrás cómo:

- Construir agentes de IA listos para producción usando Microsoft Agent Framework
- Aplicar las características principales de Microsoft Agent Framework a tus casos de uso agente
- Usar patrones avanzados incluyendo flujos de trabajo, middleware y observabilidad

## Ejemplos de código 

Los ejemplos de código para [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) se pueden encontrar en este repositorio bajo los archivos `xx-python-agent-framework` y `xx-dotnet-agent-framework`.

## Comprendiendo Microsoft Agent Framework

![Framework Intro](../../../translated_images/es/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) es el marco unificado de Microsoft para construir agentes de IA. Ofrece la flexibilidad para abordar la gran variedad de casos de uso agente que se ven tanto en entornos de producción como de investigación incluyendo:

- **Orquestación secuencial de agentes** en escenarios donde se necesitan flujos de trabajo paso a paso.
- **Orquestación concurrente** en escenarios donde los agentes necesitan completar tareas al mismo tiempo.
- **Orquestación de chat grupal** en escenarios donde los agentes pueden colaborar juntos en una tarea.
- **Orquestación de transferencia** en escenarios donde los agentes transfieren la tarea entre ellos a medida que se completan las subtareas.
- **Orquestación magnética** en escenarios donde un agente gestor crea y modifica una lista de tareas y maneja la coordinación de subagentes para completar la tarea.

Para entregar agentes de IA en producción, MAF también incluye características para:

- **Observabilidad** mediante el uso de OpenTelemetry donde cada acción del agente de IA incluyendo la invocación de herramientas, pasos de orquestación, flujos de razonamiento y monitoreo de rendimiento a través de los paneles de Microsoft Foundry.
- **Seguridad** alojando agentes de manera nativa en Microsoft Foundry que incluye controles de seguridad como acceso basado en roles, manejo de datos privados y seguridad de contenido integrada.
- **Durabilidad** ya que los hilos y flujos de trabajo de agentes pueden pausarse, reanudarse y recuperarse de errores lo que permite procesos de larga duración.
- **Control** ya que se soportan flujos de trabajo con intervención humana donde las tareas son marcadas como requeridas para su aprobación humana.

Microsoft Agent Framework también se centra en ser interoperable mediante:

- **Ser independiente de la nube** - Los agentes pueden ejecutarse en contenedores, on-premise y en múltiples nubes diferentes.
- **Ser independiente del proveedor** - Los agentes pueden crearse a través de tu SDK preferido incluyendo Azure OpenAI y OpenAI
- **Integrar estándares abiertos** - Los agentes pueden utilizar protocolos como Agent-to-Agent(A2A) y Model Context Protocol (MCP) para descubrir y usar otros agentes y herramientas.
- **Plugins y conectores** - Se pueden establecer conexiones a servicios de datos y memoria como Microsoft Fabric, SharePoint, Pinecone y Qdrant.

Veamos cómo estas características se aplican a algunos de los conceptos clave de Microsoft Agent Framework.

## Conceptos clave de Microsoft Agent Framework

### Agentes

![Agent Framework](../../../translated_images/es/agent-components.410a06daf87b4fef.webp)

**Creando agentes**

La creación de agentes se realiza definiendo el servicio de inferencia (Proveedor LLM), un
conjunto de instrucciones para que el agente de IA siga, y un `nombre` asignado:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Lo anterior usa `Azure OpenAI` pero los agentes pueden crearse usando una variedad de servicios incluyendo `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

API de OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o [MiniMax](https://platform.minimaxi.com/), que provee una API compatible con OpenAI con grandes ventanas de contexto (hasta 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o agentes remotos usando el protocolo A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ejecutando agentes**

Los agentes se ejecutan usando los métodos `.run` o `.run_stream` para respuestas no-transmitidas o transmitidas.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Cada ejecución del agente también puede tener opciones para personalizar parámetros como `max_tokens` usados por el agente, `tools` que el agente puede invocar, e incluso el `model` usado para el agente.

Esto es útil en casos donde modelos o herramientas específicas son requeridas para completar una tarea del usuario.

**Herramientas**

Las herramientas pueden definirse tanto al definir el agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Cuando se crea un ChatAgent directamente

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

y también al ejecutar el agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Herramienta proporcionada solo para esta ejecución )
```

**Hilos de agentes**

Los hilos de agentes se usan para manejar conversaciones de múltiples turnos. Los hilos pueden ser creados ya sea:

- Usando `get_new_thread()` que permite que el hilo sea guardado a lo largo del tiempo
- Creando un hilo automáticamente al ejecutar un agente y solo haciendo que el hilo dure durante la ejecución actual.

Para crear un hilo, el código es así:

```python
# Crear un nuevo hilo.
thread = agent.get_new_thread() # Ejecutar el agente con el hilo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Luego puedes serializar el hilo para almacenarlo para uso posterior:

```python
# Crear un nuevo hilo.
thread = agent.get_new_thread() 

# Ejecutar el agente con el hilo.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializar el hilo para almacenamiento.

serialized_thread = await thread.serialize() 

# Deserializar el estado del hilo después de cargarlo del almacenamiento.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware de agente**

Los agentes interactúan con herramientas y LLM para completar las tareas del usuario. En ciertos escenarios, queremos ejecutar o rastrear las interacciones intermedias. El middleware de agente nos permite hacer esto a través de:

*Middleware de función*

Este middleware nos permite ejecutar una acción entre el agente y una función/herramienta que va a llamar. Un ejemplo de cuando se usaría esto es cuando se quiere registrar la llamada a la función.

En el código abajo `next` define si se debe llamar al siguiente middleware o a la función real.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-procesamiento: Registrar antes de la ejecución de la función
    print(f"[Function] Calling {context.function.name}")

    # Continuar al siguiente middleware o ejecución de la función
    await next(context)

    # Post-procesamiento: Registrar después de la ejecución de la función
    print(f"[Function] {context.function.name} completed")
```

*Middleware de chat*

Este middleware nos permite ejecutar o registrar una acción entre el agente y las solicitudes entre el LLM.

Esto contiene información importante como los `messages` que se envían al servicio de IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-procesamiento: Registrar antes de la llamada a IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuar al siguiente middleware o servicio de IA
    await next(context)

    # Post-procesamiento: Registrar después de la respuesta de IA
    print("[Chat] AI response received")

```

**Memoria de agente**

Como se cubrió en la lección `Agentic Memory`, la memoria es un elemento importante para permitir que el agente opere sobre diferentes contextos. MAF ofrece varios tipos diferentes de memorias:

*Almacenamiento en memoria*

Esta es la memoria almacenada en hilos durante la ejecución de la aplicación.

```python
# Crear un nuevo hilo.
thread = agent.get_new_thread() # Ejecutar el agente con el hilo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mensajes persistentes*

Esta memoria se usa al almacenar el historial de conversaciones a través de diferentes sesiones. Se define usando la `chat_message_store_factory` :

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

Esta memoria se añade al contexto antes de que se ejecuten los agentes. Estas memorias pueden almacenarse en servicios externos como mem0:

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

La observabilidad es importante para construir sistemas agentic confiables y mantenibles. MAF se integra con OpenTelemetry para proporcionar trazas y métricas para una mejor observabilidad.

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

MAF ofrece flujos de trabajo que son pasos predefinidos para completar una tarea e incluyen agentes de IA como componentes en esos pasos.

Los flujos de trabajo están compuestos por distintos componentes que permiten mejor control del flujo. Los flujos de trabajo también habilitan la **orquestación multi-agente** y **checkpointing** para guardar estados del flujo de trabajo.

Los componentes principales de un flujo de trabajo son:

**Ejecutores**

Los ejecutores reciben mensajes de entrada, realizan sus tareas asignadas y luego producen un mensaje de salida. Esto mueve el flujo de trabajo hacia la finalización de la tarea mayor. Los ejecutores pueden ser agentes de IA o lógica personalizada.

**Bordes**

Los bordes se usan para definir el flujo de mensajes en un flujo de trabajo. Estos pueden ser:

*Bordes directos* - Conexiones simples uno a uno entre ejecutores:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Bordes condicionales* - Se activan cuando se cumple cierta condición. Por ejemplo, cuando no hay habitaciones de hotel disponibles, un ejecutor puede sugerir otras opciones.

*Bordes switch-case* - Rutean mensajes a diferentes ejecutores basados en condiciones definidas. Por ejemplo, si un cliente de viaje tiene acceso prioritario y sus tareas serán manejadas a través de otro flujo de trabajo.

*Bordes fan-out* - Enviar un mensaje a múltiples destinos.

*Bordes fan-in* - Recibir múltiples mensajes de diferentes ejecutores y enviarlos a un solo destino.

**Eventos**

Para proveer mejor observabilidad en flujos de trabajo, MAF ofrece eventos integrados para la ejecución incluyendo:

- `WorkflowStartedEvent`  - Comienzo de la ejecución del flujo de trabajo
- `WorkflowOutputEvent` - El flujo de trabajo produce una salida
- `WorkflowErrorEvent` - El flujo de trabajo encuentra un error
- `ExecutorInvokeEvent`  - El ejecutor comienza el procesamiento
- `ExecutorCompleteEvent`  -  El ejecutor finaliza el procesamiento
- `RequestInfoEvent` - Se emite una solicitud

## Patrones Avanzados de MAF

Las secciones anteriores cubren los conceptos clave de Microsoft Agent Framework. A medida que construyas agentes más complejos, aquí tienes algunos patrones avanzados a considerar:

- **Composición de middleware**: Enlaza múltiples manejadores de middleware (registro, autenticación, limitación de tasa) usando middleware de función y chat para control detallado sobre el comportamiento del agente.
- **Checkpointing de flujos de trabajo**: Usa eventos de flujo de trabajo y serialización para guardar y reanudar procesos de agentes de larga duración.
- **Selección dinámica de herramientas**: Combina RAG sobre descripciones de herramientas con el registro de herramientas de MAF para presentar solo las herramientas relevantes por consulta.
- **Entrega multi-agente**: Usa bordes de flujo de trabajo y enrutamiento condicional para orquestar entregas entre agentes especializados.

## Alojar Agentes LangChain / LangGraph en Microsoft Foundry

Microsoft Agent Framework es **interoperable con otros marcos** — no estás limitado a agentes escritos con MAF. Si ya tienes un agente construido con **LangChain** o **LangGraph**, puedes ejecutarlo como un **agente alojado en Microsoft Foundry** para que Foundry administre el tiempo de ejecución, sesiones, escalado, identidad y puntos finales de protocolo por ti, mientras la lógica de tu agente permanece en LangGraph.

Esto se realiza con el paquete `langchain_azure_ai.agents.hosting`, que expone un grafo compilado de LangGraph sobre los mismos protocolos que usan los agentes alojados de Foundry.

**1. Instala el paquete extra de hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

El extra `hosting` instala las bibliotecas del protocolo Foundry: `azure-ai-agentserver-responses` (el endpoint compatible con OpenAI `/responses`) y `azure-ai-agentserver-invocations` (el endpoint genérico `/invocations`).

**2. Elige un protocolo de hosting:**

| Protocolo | Clase de host | Punto final | Úsalo cuando |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Quieres chat compatible con OpenAI, streaming, historial de respuestas y hilo de conversación — la opción recomendada para agentes conversacionales. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Necesitas un JSON personalizado, un endpoint tipo webhook o procesamiento no conversacional. |

Debido a que la **API Responses es la API principal para desarrollo estilo agente en Foundry**, comienza con `ResponsesHostServer` para la mayoría de los agentes.

**3. Configura variables de entorno** (`az login` primero para que `DefaultAzureCredential` pueda autenticarse):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Cuando el agente luego se ejecuta como agente alojado en Foundry, la plataforma inyecta automáticamente `FOUNDRY_PROJECT_ENDPOINT`.

**4. Expone un agente LangGraph sobre el protocolo Responses:**

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

- **Conversaciones**: Los clientes continúan una conversación pasando `previous_response_id` o un ID de `conversation`. Si tu grafo está compilado con un LangGraph checkpointer, Foundry relaciona el estado de la conversación con el checkpoint (usa un checkpointer durable en producción; `MemorySaver` está bien para pruebas locales).
- **Intervención humana**: Si tu grafo usa LangGraph `interrupt()`, `ResponsesHostServer` muestra la interrupción pendiente como un item `function_call` / `mcp_approval_request` de Responses, y los clientes reanudan con un `function_call_output` / `mcp_approval_response` correspondiente.
- **Despliegue en Foundry**: Usa Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, requiere Docker), luego `azd provision` y `azd deploy`. El despliegue de agente alojado requiere el rol **Foundry Project Manager**.

Una versión ejecutable de este ejemplo está en [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Para la guía completa (protocolo Invocations, esquemas de solicitud personalizados y solución de problemas), consulta [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ejemplos de código 

Los ejemplos de código para Microsoft Agent Framework se pueden encontrar en este repositorio bajo los archivos `xx-python-agent-framework` y `xx-dotnet-agent-framework`.

## ¿Tienes más preguntas sobre Microsoft Agent Framework?

Únete al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrarte con otros aprendices, asistir a horas de oficina y obtener respuestas a tus preguntas sobre agentes de IA.
## Lección anterior

[Memoria para agentes de IA](../13-agent-memory/README.md)

## Próxima lección

[Construyendo agentes para uso en computadora (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->