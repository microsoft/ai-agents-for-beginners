# Construcción de Aplicaciones Multi-Agente con Microsoft Agent Framework Workflow

Este tutorial te guiará para entender y construir aplicaciones multi-agente utilizando Microsoft Agent Framework. Exploraremos los conceptos fundamentales de los sistemas multi-agente, profundizaremos en la arquitectura del componente Workflow del framework, y recorreremos ejemplos prácticos en Python y .NET para diferentes patrones de workflow.

## 1\. Entendiendo los Sistemas Multi-Agente

Un Agente de IA es un sistema que va más allá de las capacidades de un modelo de lenguaje grande (LLM) estándar. Puede percibir su entorno, tomar decisiones y realizar acciones para alcanzar objetivos específicos. Un sistema multi-agente involucra varios de estos agentes colaborando para resolver un problema que sería difícil o imposible manejar para un solo agente.

### Escenarios Comunes de Aplicación

  * **Resolución Compleja de Problemas**: Dividir una tarea grande (p. ej., planificar un evento a nivel empresa) en sub-tareas manejadas por agentes especializados (p. ej., agente de presupuesto, agente de logística, agente de marketing).
  * **Asistentes Virtuales**: Un agente asistente principal que delega tareas como programación, investigación y reservas a otros agentes especializados.
  * **Creación Automática de Contenido**: Un flujo de trabajo donde un agente redacta contenido, otro lo revisa para precisión y tono, y un tercero lo publica.

### Patrones Multi-Agente

Los sistemas multi-agente pueden organizarse en varios patrones que determinan cómo interactúan:

  * **Secuencial**: Los agentes trabajan en un orden predefinido, como una línea de ensamblaje. La salida de un agente se convierte en la entrada para el siguiente.
  * **Concurrente**: Los agentes trabajan en paralelo en diferentes partes de una tarea, y sus resultados se agregan al final.
  * **Condicional**: El flujo sigue diferentes caminos basado en la salida de un agente, similar a una declaración if-then-else.

## 2\. La Arquitectura del Workflow de Microsoft Agent Framework

El sistema de workflow del Agent Framework es un motor de orquestación avanzado diseñado para gestionar interacciones complejas entre múltiples agentes. Está construido sobre una arquitectura basada en grafos que usa un [modelo de ejecución estilo Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), donde el procesamiento ocurre en pasos sincronizados llamados "supersteps."

### Componentes Clave

La arquitectura está compuesta por tres partes principales:

1.  **Ejecutores**: Son las unidades fundamentales de procesamiento. En nuestros ejemplos, un `Agent` es un tipo de ejecutor. Cada ejecutor puede tener múltiples manejadores de mensajes que se invocan automáticamente según el tipo de mensaje recibido.
2.  **Aristas**: Definen el camino que toman los mensajes entre ejecutores. Las aristas pueden tener condiciones, permitiendo el enrutamiento dinámico de información a través del grafo del workflow.
3.  **Workflow**: Este componente orquesta todo el proceso, gestionando los ejecutores, aristas y el flujo general de ejecución. Asegura que los mensajes se procesen en el orden correcto y transmite eventos para observabilidad.

*Un diagrama que ilustra los componentes clave del sistema de workflow.*

Esta estructura permite construir aplicaciones robustas y escalables utilizando patrones fundamentales como cadenas secuenciales, fan-out/fan-in para procesamiento paralelo, y lógica switch-case para flujos condicionales.

## 3\. Ejemplos Prácticos y Análisis de Código

Ahora, exploremos cómo implementar diferentes patrones de workflow usando el framework. Veremos código en Python y .NET para cada ejemplo.

### Caso 1: Workflow Secuencial Básico

Este es el patrón más simple, donde la salida de un agente se pasa directamente a otro. Nuestro escenario involucra un agente de hotel `FrontDesk` que hace una recomendación de viaje, que luego es revisada por un agente `Concierge`.

*Diagrama del workflow básico FrontDesk -\> Concierge.*

#### Contexto del Escenario

Un viajero pide una recomendación en París.

1.  El agente `FrontDesk`, diseñado para ser breve, sugiere visitar el Museo del Louvre.
2.  El agente `Concierge`, que prioriza experiencias auténticas, recibe esta sugerencia. Revisa la recomendación y proporciona retroalimentación, sugiriendo una alternativa más local y menos turística.

#### Análisis de Implementación en Python

En el ejemplo Python, primero definimos y creamos los dos agentes, cada uno con instrucciones específicas.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definir roles e instrucciones del agente
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Crear instancias de agentes
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Luego, se usa `WorkflowBuilder` para construir el grafo. El `front_desk_agent` se establece como punto de inicio, y se crea una arista para conectar su salida con el `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Finalmente, se ejecuta el workflow con el prompt inicial del usuario.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run ejecuta el flujo de trabajo; get_outputs() devuelve el resultado del ejecutor de salida.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Análisis de Implementación en .NET (C\#)

La implementación en .NET sigue una lógica muy similar. Primero se definen constantes para los nombres e instrucciones de los agentes.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Los agentes se crean usando un `AzureOpenAIClient` (API de Responses), y luego `WorkflowBuilder` define el flujo secuencial añadiendo una arista desde `frontDeskAgent` hasta `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

El workflow se ejecuta con el mensaje del usuario, y los resultados se transmiten.

### Caso 2: Workflow Secuencial de Múltiples Pasos

Este patrón extiende la secuencia básica para incluir más agentes. Es ideal para procesos que requieren múltiples etapas de refinamiento o transformación.

#### Contexto del Escenario

Un usuario proporciona una imagen de una sala y pide un presupuesto de muebles.

1.  **Agente de Ventas**: Identifica los muebles en la imagen y crea una lista.
2.  **Agente de Precios**: Toma la lista de artículos y ofrece un desglose detallado de precios, incluyendo opciones económicas, medias y premium.
3.  **Agente de Cotización**: Recibe la lista con precios y la formatea en un documento formal de cotización en Markdown.

*Diagrama del workflow Ventas -\> Precio -\> Cotización.*

#### Análisis de Implementación en Python

Se definen tres agentes, cada uno con un rol especializado. El workflow se construye usando `add_edge` para crear una cadena: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Crear tres agentes especializados
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Construir el flujo de trabajo secuencial
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

La entrada es un `ChatMessage` que incluye texto y la URI de la imagen. El framework maneja el paso de la salida de cada agente al siguiente en la secuencia hasta generar la cotización final.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# El mensaje del usuario contiene tanto texto como una imagen
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Ejecutar el flujo de trabajo
events = await workflow.run(message)
```

#### Análisis de Implementación en .NET (C\#)

El ejemplo .NET refleja la versión de Python. Se crean tres agentes (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` los enlaza secuencialmente.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

El mensaje del usuario se construye con los datos de la imagen (como bytes) y el texto del prompt. El método `InProcessExecution.RunStreamingAsync` inicia el workflow, y la salida final se captura desde el stream.

### Caso 3: Workflow Concurrente

Este patrón se usa cuando las tareas pueden realizarse simultáneamente para ahorrar tiempo. Implica un "fan-out" a múltiples agentes y un "fan-in" para agregar los resultados.

#### Contexto del Escenario

Un usuario pide planear un viaje a Seattle.

1.  **Despachador (Fan-Out)**: La solicitud del usuario se envía a dos agentes al mismo tiempo.
2.  **Agente Investigador**: Investiga atracciones, clima y consideraciones clave para un viaje a Seattle en diciembre.
3.  **Agente Planificador**: Crea independientemente un itinerario detallado día por día.
4.  **Agregador (Fan-In)**: Se recogen las salidas tanto del investigador como del planificador, y se presentan juntas como resultado final.

*Diagrama del workflow concurrente de Investigador y Planificador.*

#### Análisis de Implementación en Python

El `ConcurrentBuilder` simplifica la creación de este patrón. Simplemente se listan los agentes participantes, y el builder crea automáticamente la lógica necesaria de fan-out y fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder maneja la lógica de fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Ejecutar el flujo de trabajo
events = await workflow.run("Plan a trip to Seattle in December")
```

El framework asegura que `research_agent` y `plan_agent` se ejecuten en paralelo, y que sus salidas finales se colecten en una lista.

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

Luego el `WorkflowBuilder` usa `AddFanOutEdge` y `AddFanInEdge` para construir el grafo con estos ejecutores personalizados y los agentes.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Caso 4: Workflow Condicional

Los workflows condicionales introducen lógica ramificada, permitiendo que el sistema tome diferentes caminos basados en resultados intermedios.

#### Contexto del Escenario

Este workflow automatiza la creación y publicación de un tutorial técnico.

1.  **Agente Evangelista**: Escribe un borrador del tutorial basado en un esquema y URLs dados.
2.  **Agente Revisor de Contenido**: Revisa el borrador. Verifica si el conteo de palabras supera las 200.
3.  **Rama Condicional**:
      * **Si Aprobado (`Yes`)**: El workflow continúa con el `Publisher-Agent`.
      * **Si Rechazado (`No`)**: El workflow se detiene y entrega el motivo del rechazo.
4.  **Agente Editor**: Si el borrador es aprobado, este agente guarda el contenido en un archivo Markdown.

#### Análisis de Implementación en Python

Este ejemplo usa una función personalizada, `select_targets`, para implementar la lógica condicional. Esta función se pasa a `add_multi_selection_edge_group` y dirige el workflow basado en el campo `review_result` de la salida del revisor.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Esta función determina el siguiente paso basado en el resultado de la revisión
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Si se aprueba, proceda al ejecutor 'save_draft'
        return [save_draft_id]
    else:
        # Si se rechaza, proceda al ejecutor 'handle_review' para reportar el fallo
        return [handle_review_id]

# El constructor de flujo de trabajo utiliza la función de selección para la enrutación
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # El borde de selección múltiple implementa la lógica condicional
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Se usan ejecutores personalizados como `to_reviewer_result` para analizar la salida JSON de los agentes y convertirla en objetos fuertemente tipados que la función de selección puede inspeccionar.

#### Análisis de Implementación en .NET (C\#)

La versión .NET usa un enfoque similar con una función de condición. Se define un `Func<object?, bool>` para verificar la propiedad `Result` del objeto `ReviewResult`.

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

El parámetro `condition` del método `AddEdge` permite que `WorkflowBuilder` cree una ruta ramificada. El workflow seguirá la arista hacia `publishExecutor` solo si la condición `GetCondition(expectedResult: "Yes")` retorna verdadero. De lo contrario, seguirá el camino hacia `sendReviewerExecutor`.

## Conclusión

Microsoft Agent Framework Workflow proporciona una base robusta y flexible para orquestar sistemas multi-agente complejos. Aprovechando su arquitectura basada en grafos y componentes clave, los desarrolladores pueden diseñar e implementar workflows sofisticados tanto en Python como en .NET. Ya sea que tu aplicación requiera procesamiento secuencial simple, ejecución paralela, o lógica condicional dinámica, el framework ofrece las herramientas para construir soluciones potentes, escalables y tipo-seguras impulsadas por IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->