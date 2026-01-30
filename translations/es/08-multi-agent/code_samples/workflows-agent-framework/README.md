# Construcción de Aplicaciones Multi-Agente con el Flujo de Trabajo del Marco de Agentes de Microsoft

Este tutorial te guiará para comprender y construir aplicaciones multi-agente utilizando el Marco de Agentes de Microsoft. Exploraremos los conceptos básicos de los sistemas multi-agente, profundizaremos en la arquitectura del componente Workflow del marco y revisaremos ejemplos prácticos en Python y .NET para diferentes patrones de flujo de trabajo.

## 1\. Comprendiendo los Sistemas Multi-Agente

Un Agente de IA es un sistema que va más allá de las capacidades de un modelo de lenguaje grande estándar (LLM). Puede percibir su entorno, tomar decisiones y realizar acciones para alcanzar objetivos específicos. Un sistema multi-agente implica varios de estos agentes colaborando para resolver un problema que sería difícil o imposible de manejar por un solo agente.

### Escenarios Comunes de Aplicación

  * **Resolución de Problemas Complejos**: Dividir una tarea grande (por ejemplo, planificar un evento para toda la empresa) en sub-tareas más pequeñas manejadas por agentes especializados (por ejemplo, un agente de presupuesto, un agente de logística, un agente de marketing).
  * **Asistentes Virtuales**: Un agente asistente principal delega tareas como programación, investigación y reservas a otros agentes especializados.
  * **Creación Automática de Contenido**: Un flujo de trabajo donde un agente redacta contenido, otro lo revisa para verificar precisión y tono, y un tercero lo publica.

### Patrones Multi-Agente

Los sistemas multi-agente pueden organizarse en varios patrones que determinan cómo interactúan:

  * **Secuencial**: Los agentes trabajan en un orden predefinido, como una línea de ensamblaje. La salida de un agente se convierte en la entrada para el siguiente.
  * **Concurrente**: Los agentes trabajan en paralelo en diferentes partes de una tarea, y sus resultados se agregan al final.
  * **Condicional**: El flujo sigue diferentes caminos según la salida de un agente, similar a una declaración if-then-else.

## 2\. La Arquitectura del Flujo de Trabajo del Marco de Agentes de Microsoft

El sistema de flujo de trabajo del Marco de Agentes es un motor de orquestación avanzado diseñado para gestionar interacciones complejas entre múltiples agentes. Está construido sobre una arquitectura basada en gráficos que utiliza un [modelo de ejecución estilo Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), donde el procesamiento ocurre en pasos sincronizados llamados "supersteps".

### Componentes Principales

La arquitectura se compone de tres partes principales:

1.  **Ejecutores**: Son las unidades fundamentales de procesamiento. En nuestros ejemplos, un `Agent` es un tipo de ejecutor. Cada ejecutor puede tener múltiples manejadores de mensajes que se invocan automáticamente según el tipo de mensaje recibido.
2.  **Edges**: Definen el camino que toman los mensajes entre los ejecutores. Los edges pueden tener condiciones, permitiendo el enrutamiento dinámico de información a través del gráfico de flujo de trabajo.
3.  **Workflow**: Este componente orquesta todo el proceso, gestionando los ejecutores, edges y el flujo general de ejecución. Garantiza que los mensajes se procesen en el orden correcto y transmite eventos para observabilidad.

*Un diagrama que ilustra los componentes principales del sistema de flujo de trabajo.*

Esta estructura permite construir aplicaciones robustas y escalables utilizando patrones fundamentales como cadenas secuenciales, fan-out/fan-in para procesamiento paralelo y lógica switch-case para flujos condicionales.

## 3\. Ejemplos Prácticos y Análisis de Código

Ahora, exploremos cómo implementar diferentes patrones de flujo de trabajo utilizando el marco. Revisaremos código en Python y .NET para cada ejemplo.

### Caso 1: Flujo de Trabajo Secuencial Básico

Este es el patrón más simple, donde la salida de un agente se pasa directamente a otro. Nuestro escenario involucra un agente `FrontDesk` de hotel que hace una recomendación de viaje, la cual es revisada por un agente `Concierge`.

*Diagrama del flujo básico FrontDesk -\> Concierge.*

#### Antecedentes del Escenario

Un viajero solicita una recomendación en París.

1.  El agente `FrontDesk`, diseñado para ser breve, sugiere visitar el Museo del Louvre.
2.  El agente `Concierge`, que prioriza experiencias auténticas, recibe esta sugerencia. Revisa la recomendación y proporciona comentarios, sugiriendo una alternativa más local y menos turística.

#### Análisis de Implementación en Python

En el ejemplo de Python, primero definimos y creamos los dos agentes, cada uno con instrucciones específicas.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Luego, se utiliza el `WorkflowBuilder` para construir el gráfico. El `front_desk_agent` se establece como el punto de inicio, y se crea un edge para conectar su salida al `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Finalmente, se ejecuta el flujo de trabajo con el mensaje inicial del usuario.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Análisis de Implementación en .NET (C\#)

La implementación en .NET sigue una lógica muy similar. Primero, se definen constantes para los nombres e instrucciones de los agentes.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Los agentes se crean utilizando un `OpenAIClient`, y luego el `WorkflowBuilder` define el flujo secuencial agregando un edge desde el `frontDeskAgent` al `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

El flujo de trabajo se ejecuta con el mensaje del usuario, y los resultados se transmiten de vuelta.

### Caso 2: Flujo de Trabajo Secuencial Multi-Paso

Este patrón extiende la secuencia básica para incluir más agentes. Es ideal para procesos que requieren múltiples etapas de refinamiento o transformación.

#### Antecedentes del Escenario

Un usuario proporciona una imagen de una sala de estar y solicita una cotización de muebles.

1.  **Sales-Agent**: Identifica los muebles en la imagen y crea una lista.
2.  **Price-Agent**: Toma la lista de artículos y proporciona un desglose detallado de precios, incluyendo opciones económicas, de gama media y premium.
3.  **Quote-Agent**: Recibe la lista con precios y la formatea en un documento de cotización formal en Markdown.

*Diagrama del flujo Sales -\> Price -\> Quote.*

#### Análisis de Implementación en Python

Se definen tres agentes, cada uno con un rol especializado. El flujo de trabajo se construye utilizando `add_edge` para crear una cadena: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

La entrada es un `ChatMessage` que incluye tanto texto como la URI de la imagen. El marco maneja el paso de la salida de cada agente al siguiente en la secuencia hasta que se genera la cotización final.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### Análisis de Implementación en .NET (C\#)

El ejemplo en .NET refleja la versión en Python. Se crean tres agentes (`salesagent`, `priceagent`, `quoteagent`). El `WorkflowBuilder` los vincula de manera secuencial.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

El mensaje del usuario se construye con los datos de la imagen (como bytes) y el mensaje de texto. El método `InProcessExecution.StreamAsync` inicia el flujo de trabajo, y la salida final se captura desde el stream.

### Caso 3: Flujo de Trabajo Concurrente

Este patrón se utiliza cuando las tareas pueden realizarse simultáneamente para ahorrar tiempo. Implica un "fan-out" hacia múltiples agentes y un "fan-in" para agregar los resultados.

#### Antecedentes del Escenario

Un usuario solicita planificar un viaje a Seattle.

1.  **Dispatcher (Fan-Out)**: La solicitud del usuario se envía a dos agentes al mismo tiempo.
2.  **Researcher-Agent**: Investiga atracciones, clima y consideraciones clave para un viaje a Seattle en diciembre.
3.  **Plan-Agent**: Crea de manera independiente un itinerario detallado día a día.
4.  **Aggregator (Fan-In)**: Los resultados del investigador y del planificador se recopilan y presentan juntos como resultado final.

*Diagrama del flujo concurrente Researcher y Planner.*

#### Análisis de Implementación en Python

El `ConcurrentBuilder` simplifica la creación de este patrón. Simplemente se enumeran los agentes participantes, y el constructor crea automáticamente la lógica necesaria de fan-out y fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

El marco garantiza que el `research_agent` y el `plan_agent` se ejecuten en paralelo, y sus salidas finales se recopilan en una lista.

#### Análisis de Implementación en .NET (C\#)

En .NET, este patrón requiere una definición más explícita. Se crean ejecutores personalizados (`ConcurrentStartExecutor` y `ConcurrentAggregationExecutor`) para manejar la lógica de fan-out y fan-in.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

El `WorkflowBuilder` utiliza `AddFanOutEdge` y `AddFanInEdge` para construir el gráfico con estos ejecutores personalizados y los agentes.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Caso 4: Flujo de Trabajo Condicional

Los flujos de trabajo condicionales introducen lógica de ramificación, permitiendo que el sistema tome diferentes caminos según los resultados intermedios.

#### Antecedentes del Escenario

Este flujo automatiza la creación y publicación de un tutorial técnico.

1.  **Evangelist-Agent**: Escribe un borrador del tutorial basado en un esquema y URLs proporcionados.
2.  **ContentReviewer-Agent**: Revisa el borrador. Verifica si el conteo de palabras supera las 200.
3.  **Rama Condicional**:
      * **Si Aprobado (`Yes`)**: El flujo continúa hacia el `Publisher-Agent`.
      * **Si Rechazado (`No`)**: El flujo se detiene y se muestra la razón del rechazo.
4.  **Publisher-Agent**: Si el borrador es aprobado, este agente guarda el contenido en un archivo Markdown.

#### Análisis de Implementación en Python

Este ejemplo utiliza una función personalizada, `select_targets`, para implementar la lógica condicional. Esta función se pasa a `add_multi_selection_edge_group` y dirige el flujo según el campo `review_result` de la salida del revisor.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Se utilizan ejecutores personalizados como `to_reviewer_result` para analizar la salida JSON de los agentes y convertirla en objetos fuertemente tipados que la función de selección puede inspeccionar.

#### Análisis de Implementación en .NET (C\#)

La versión en .NET utiliza un enfoque similar con una función condicional. Se define un `Func<object?, bool>` para verificar la propiedad `Result` del objeto `ReviewResult`.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

El parámetro `condition` del método `AddEdge` permite que el `WorkflowBuilder` cree un camino de ramificación. El flujo solo seguirá el edge hacia `publishExecutor` si la condición `GetCondition(expectedResult: "Yes")` devuelve verdadero. De lo contrario, sigue el camino hacia `sendReviewerExecutor`.

## Conclusión

El Flujo de Trabajo del Marco de Agentes de Microsoft proporciona una base robusta y flexible para orquestar sistemas complejos multi-agente. Al aprovechar su arquitectura basada en gráficos y componentes principales, los desarrolladores pueden diseñar e implementar flujos de trabajo sofisticados en Python y .NET. Ya sea que tu aplicación requiera procesamiento secuencial simple, ejecución paralela o lógica condicional dinámica, el marco ofrece las herramientas para construir soluciones potentes, escalables y seguras impulsadas por IA.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.