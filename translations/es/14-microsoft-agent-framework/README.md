# Explorando Microsoft Agent Framework

![Agent Framework](../../../translated_images/es/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introducción

Esta lección cubrirá:

- Comprender Microsoft Agent Framework: Características clave y valor  
- Explorar los conceptos clave de Microsoft Agent Framework
- Patrones avanzados de MAF: Flujos de trabajo, middleware y memoria

## Objetivos de aprendizaje

Después de completar esta lección, sabrá cómo:

- Construir agentes de IA listos para producción usando Microsoft Agent Framework
- Aplicar las funciones principales de Microsoft Agent Framework a sus casos de uso agennticos
- Usar patrones avanzados incluyendo flujos de trabajo, middleware y observabilidad

## Ejemplos de Código 

Los ejemplos de código para [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) se encuentran en este repositorio bajo los archivos `xx-python-agent-framework` y `xx-dotnet-agent-framework`.

## Comprendiendo Microsoft Agent Framework

![Framework Intro](../../../translated_images/es/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) es el marco unificado de Microsoft para construir agentes de IA. Ofrece la flexibilidad para abordar la gran variedad de casos de uso agennticos vistos tanto en entornos de producción como en investigación, incluyendo:

- **Orquestación secuencial de agentes** en escenarios donde se requieren flujos de trabajo paso a paso.
- **Orquestación concurrente** en escenarios donde los agentes necesitan completar tareas al mismo tiempo.
- **Orquestación de chat grupal** en escenarios donde los agentes pueden colaborar juntos en una tarea.
- **Orquestación de transferencia** en escenarios donde los agentes pasan la tarea de uno a otro a medida que se completan las subtareas.
- **Orquestación magnética** en escenarios donde un agente gestor crea y modifica una lista de tareas y maneja la coordinación de subagentes para completar la tarea.

Para entregar agentes de IA en producción, MAF también incluye funciones para:

- **Observabilidad** a través del uso de OpenTelemetry donde cada acción del agente de IA, incluyendo la invocación de herramientas, pasos de orquestación, flujos de razonamiento y monitoreo de rendimiento mediante los paneles de Microsoft Foundry.
- **Seguridad** alojando agentes nativamente en Microsoft Foundry que incluye controles de seguridad como acceso basado en roles, manejo de datos privados y seguridad de contenido incorporada.
- **Durabilidad** ya que los hilos y flujos de trabajo del agente pueden pausarse, reanudarse y recuperarse de errores, lo que permite procesos de mayor duración.
- **Control** ya que se soportan flujos de trabajo con persona en el ciclo donde las tareas se marcan como requeridas para aprobación humana.

Microsoft Agent Framework también se centra en ser interoperable mediante:

- **Ser independiente de la nube** - Los agentes pueden ejecutarse en contenedores, localmente y a través de múltiples nubes diferentes.
- **Ser independiente del proveedor** - Los agentes pueden ser creados a través de su SDK preferido incluyendo Azure OpenAI y OpenAI
- **Integrar estándares abiertos** - Los agentes pueden utilizar protocolos como Agent-to-Agent (A2A) y Model Context Protocol (MCP) para descubrir y usar otros agentes y herramientas.
- **Plugins y conectores** - Se pueden establecer conexiones a servicios de datos y memoria tales como Microsoft Fabric, SharePoint, Pinecone y Qdrant.

Veamos cómo estas funciones se aplican a algunos de los conceptos clave de Microsoft Agent Framework.

## Conceptos clave de Microsoft Agent Framework

### Agentes

![Agent Framework](../../../translated_images/es/agent-components.410a06daf87b4fef.webp)

**Creación de agentes**

La creación del agente se realiza definiendo el servicio de inferencia (Proveedor LLM), un
conjunto de instrucciones para que el agente de IA las siga y un `nombre` asignado:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

El ejemplo anterior utiliza `Azure OpenAI` pero los agentes pueden ser creados usando una variedad de servicios incluyendo `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

APIs OpenAI `Responses`, `ChatCompletion`

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

**Ejecución de agentes**

Los agentes se ejecutan usando los métodos `.run` o `.run_stream` para respuestas sin transmisión o con transmisión.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Cada ejecución de agente también puede tener opciones para personalizar parámetros como `max_tokens` usados por el agente, las `tools` que el agente puede llamar e incluso el `modelo` mismo usado para el agente.

Esto es útil en casos donde se requieren modelos o herramientas específicas para completar la tarea de un usuario.

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

Los hilos de agente se usan para manejar conversaciones de múltiples turnos. Los hilos pueden ser creados ya sea por:

- Usar `get_new_thread()` que permite que el hilo se guarde con el tiempo
- Crear un hilo automáticamente al ejecutar un agente y que el hilo dure solo durante la ejecución actual.

Para crear un hilo, el código es el siguiente:

```python
# Crear un nuevo hilo.
thread = agent.get_new_thread() # Ejecutar el agente con el hilo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Luego puede serializar el hilo para almacenarlo para uso posterior:

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

**Middleware del agente**

Los agentes interactúan con herramientas y LLMs para completar las tareas del usuario. En ciertos escenarios, queremos ejecutar o rastrear entre estas interacciones. El middleware del agente nos permite hacer esto mediante:

*Middleware de función*

Este middleware nos permite ejecutar una acción entre el agente y una función/herramienta que está llamando. Un ejemplo de cuándo se usaría esto es cuando desea hacer algún registro en la llamada a la función.

En el código abajo `next` define si se debe llamar al siguiente middleware o a la función real.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-procesamiento: Registro antes de la ejecución de la función
    print(f"[Function] Calling {context.function.name}")

    # Continuar al siguiente middleware o ejecución de la función
    await next(context)

    # Post-procesamiento: Registro después de la ejecución de la función
    print(f"[Function] {context.function.name} completed")
```

*Middleware de chat*

Este middleware nos permite ejecutar o registrar una acción entre el agente y las solicitudes entre el LLM .

Esto contiene información importante como los `messages` que se envían al servicio de IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Preprocesamiento: Registrar antes de la llamada a la IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuar al siguiente middleware o servicio de IA
    await next(context)

    # Postprocesamiento: Registrar después de la respuesta de la IA
    print("[Chat] AI response received")

```

**Memoria del agente**

Como se cubrió en la lección `Agentic Memory`, la memoria es un elemento importante para permitir que el agente opere sobre diferentes contextos. MAF ofrece varios tipos diferentes de memorias:

*Almacenamiento en memoria*

Esta es la memoria almacenada en hilos durante el tiempo de ejecución de la aplicación.

```python
# Crear un nuevo hilo.
thread = agent.get_new_thread() # Ejecutar el agente con el hilo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mensajes persistentes*

Esta memoria se usa cuando se almacena el historial de conversación a través de diferentes sesiones. Se define usando el `chat_message_store_factory` :

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

Esta memoria se agrega al contexto antes de que se ejecuten los agentes. Estas memorias pueden almacenarse en servicios externos como mem0:

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

**Observabilidad del agente**

La observabilidad es importante para construir sistemas agénticos confiables y mantenibles. MAF se integra con OpenTelemetry para proporcionar trazas y métricas para una mejor observabilidad.

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

Los flujos de trabajo están compuestos por diferentes componentes que permiten un mejor control de flujo. Los flujos de trabajo también permiten la **orquestación multi-agente** y la **creación de puntos de control** para guardar estados de flujo.

Los componentes centrales de un flujo de trabajo son:

**Ejecutores**

Los ejecutores reciben mensajes de entrada, realizan las tareas asignadas y luego producen un mensaje de salida. Esto mueve el flujo de trabajo hacia la finalización de la tarea más grande. Los ejecutores pueden ser agentes de IA o lógica personalizada.

**Aristas**

Las aristas se usan para definir el flujo de mensajes en un flujo de trabajo. Estas pueden ser:

*Aristas directas* - Conexiones simples uno a uno entre ejecutores:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Aristas condicionales* - Se activan después de que se cumple cierta condición. Por ejemplo, cuando no hay habitaciones de hotel disponibles, un ejecutor puede sugerir otras opciones.

*Aristas de tipo switch-case* - Dirigen mensajes a diferentes ejecutores basados en condiciones definidas. Por ejemplo, si un cliente de viajes tiene acceso prioritario, sus tareas serán manejadas a través de otro flujo de trabajo.

*Aristas de bifurcación (fan-out)* - Envía un mensaje a múltiples destinos.

*Aristas de convergencia (fan-in)* - Recoge múltiples mensajes de diferentes ejecutores y envía a un destino único.

**Eventos**

Para proporcionar una mejor observabilidad en los flujos de trabajo, MAF ofrece eventos integrados para la ejecución incluyendo:

- `WorkflowStartedEvent`  - Comienza la ejecución del flujo de trabajo
- `WorkflowOutputEvent` - El flujo de trabajo produce una salida
- `WorkflowErrorEvent` - El flujo de trabajo encuentra un error
- `ExecutorInvokeEvent`  - El ejecutor comienza a procesar
- `ExecutorCompleteEvent`  - El ejecutor termina de procesar
- `RequestInfoEvent` - Se realiza una solicitud

## Patrones avanzados de MAF

Las secciones anteriores cubren los conceptos clave de Microsoft Agent Framework. A medida que construya agentes más complejos, aquí hay algunos patrones avanzados a considerar:

- **Composición de middleware**: Encadenar múltiples manejadores de middleware (registro, autenticación, limitación de tasa) usando middleware de función y chat para un control fino sobre el comportamiento del agente.
- **Creación de puntos de control en flujos de trabajo**: Usar eventos de flujo de trabajo y serialización para guardar y reanudar procesos de agente de larga duración.
- **Selección dinámica de herramientas**: Combinar RAG sobre descripciones de herramientas con el registro de herramientas de MAF para presentar solo herramientas relevantes por consulta.
- **Transferencia multi-agente**: Usar aristas de flujo de trabajo y enrutamiento condicional para orquestar transferencias entre agentes especializados.

## Hospedando agentes LangChain / LangGraph en Microsoft Foundry

Microsoft Agent Framework es **interoperable entre frameworks** — no está limitado a agentes escritos con MAF. Si ya tiene un agente construido con **LangChain** o **LangGraph**, puede ejecutarlo como un **agente hospedado en Microsoft Foundry** para que Foundry gestione el tiempo de ejecución, sesiones, escalado, identidad y puntos finales de protocolo para usted, mientras su lógica permanece en LangGraph.

Esto se realiza con el paquete `langchain_azure_ai.agents.hosting`, que expone un grafo compilado de LangGraph sobre los mismos protocolos que usan los agentes hospedados en Foundry.

**1. Instale el extra de hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

El extra `hosting` instala las bibliotecas de protocolo Foundry: `azure-ai-agentserver-responses` (el endpoint OpenAI-compatible `/responses`) y `azure-ai-agentserver-invocations` (el endpoint genérico `/invocations`).

**2. Elija un protocolo de hosting:**

| Protocolo | Clase host | Endpoint | Úselo cuando |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Quiere chat compatible con OpenAI, transmisión, historial de respuestas y agrupamiento de conversación — el predeterminado recomendado para agentes conversacionales. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Necesita una forma JSON personalizada, un endpoint estilo webhook o procesamiento no conversacional. |

Debido a que **la API de Responses es la API principal para desarrollo estilo agente en Foundry**, empiece con `ResponsesHostServer` para la mayoría de agentes.

**3. Configure variables de entorno** (`az login` primero para que `DefaultAzureCredential` pueda autenticarse):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Cuando el agente se ejecute más tarde como agente hospedado en Foundry, la plataforma inyecta `FOUNDRY_PROJECT_ENDPOINT` automáticamente.

**4. Exponga un agente LangGraph sobre el protocolo Responses:**

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI aquí apunta al endpoint compatible con OpenAI (Responses) del proyecto Foundry.
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

Ejecútelo localmente con `python main.py`, luego envíe una solicitud Responses a `http://localhost:8088/responses`.

**Comportamientos clave:**

- **Conversaciones**: Los clientes continúan una conversación pasando `previous_response_id` o un ID de `conversation`. Si su grafo está compilado con un checkpointer de LangGraph, Foundry asigna el estado de la conversación al checkpoint (use un checkpointer duradero en producción; `MemorySaver` está bien para pruebas locales).
- **Humano en el ciclo**: Si su grafo usa LangGraph `interrupt()`, `ResponsesHostServer` muestra la interrupción pendiente como un ítem `function_call` / `mcp_approval_request` de Responses, y los clientes reanudan con un `function_call_output` / `mcp_approval_response` correspondiente.
- **Despliegue en Foundry**: Use Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, requiere Docker), luego `azd provision` y `azd deploy`. El despliegue de agentes hospedados requiere el rol **Foundry Project Manager**.

Una versión ejecutable de este ejemplo está en [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Para la guía completa (protocolo Invocations, esquemas de solicitud personalizados y solución de problemas), vea [Hospedar agentes LangGraph como agentes hospedados en Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ejemplos de Código 

Los ejemplos de código para Microsoft Agent Framework se encuentran en este repositorio bajo los archivos `xx-python-agent-framework` y `xx-dotnet-agent-framework`.

## ¿Tiene más preguntas sobre Microsoft Agent Framework?

Únase al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conocer a otros aprendices, asistir a horas de oficina y obtener respuestas a sus preguntas sobre agentes de IA.
## Lección anterior

[Memoria para agentes de IA](../13-agent-memory/README.md)

## Próxima lección

[Construcción de agentes para uso computacional (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->