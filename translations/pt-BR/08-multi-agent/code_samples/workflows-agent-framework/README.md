# Construindo Aplicações Multi-Agente com o Workflow do Microsoft Agent Framework

Este tutorial irá guiá-lo na compreensão e construção de aplicações multi-agente utilizando o Microsoft Agent Framework. Exploraremos os conceitos principais de sistemas multi-agente, mergulharemos na arquitetura do componente Workflow do framework e analisaremos exemplos práticos em Python e .NET para diferentes padrões de workflow.

## 1\. Compreendendo Sistemas Multi-Agente

Um Agente de IA é um sistema que vai além das capacidades de um modelo de linguagem padrão (LLM). Ele pode perceber seu ambiente, tomar decisões e realizar ações para alcançar objetivos específicos. Um sistema multi-agente envolve vários desses agentes colaborando para resolver um problema que seria difícil ou impossível para um único agente lidar sozinho.

### Cenários Comuns de Aplicação

  * **Resolução de Problemas Complexos**: Dividir uma tarefa grande (por exemplo, planejar um evento corporativo) em sub-tarefas menores tratadas por agentes especializados (por exemplo, um agente de orçamento, um agente de logística, um agente de marketing).
  * **Assistentes Virtuais**: Um agente assistente principal delega tarefas como agendamento, pesquisa e reservas para outros agentes especializados.
  * **Criação Automática de Conteúdo**: Um workflow onde um agente redige o conteúdo, outro revisa para precisão e tom, e um terceiro publica.

### Padrões Multi-Agente

Sistemas multi-agente podem ser organizados em vários padrões, que determinam como eles interagem:

  * **Sequencial**: Os agentes trabalham em uma ordem predefinida, como uma linha de montagem. A saída de um agente se torna a entrada para o próximo.
  * **Concorrente**: Os agentes trabalham em paralelo em diferentes partes de uma tarefa, e seus resultados são agregados no final.
  * **Condicional**: O workflow segue diferentes caminhos com base na saída de um agente, semelhante a uma instrução if-then-else.

## 2\. A Arquitetura do Workflow do Microsoft Agent Framework

O sistema de workflow do Agent Framework é um motor de orquestração avançado projetado para gerenciar interações complexas entre múltiplos agentes. Ele é construído em uma arquitetura baseada em grafos que utiliza um [modelo de execução estilo Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), onde o processamento ocorre em etapas sincronizadas chamadas "supersteps".

### Componentes Principais

A arquitetura é composta por três partes principais:

1.  **Executores**: São as unidades fundamentais de processamento. Em nossos exemplos, um `Agent` é um tipo de executor. Cada executor pode ter vários manipuladores de mensagens que são automaticamente invocados com base no tipo de mensagem recebida.
2.  **Edges**: Definem o caminho que as mensagens percorrem entre os executores. Edges podem ter condições, permitindo o roteamento dinâmico de informações através do grafo de workflow.
3.  **Workflow**: Este componente orquestra todo o processo, gerenciando os executores, edges e o fluxo geral de execução. Ele garante que as mensagens sejam processadas na ordem correta e transmite eventos para observabilidade.

*Um diagrama ilustrando os componentes principais do sistema de workflow.*

Essa estrutura permite construir aplicações robustas e escaláveis utilizando padrões fundamentais como cadeias sequenciais, fan-out/fan-in para processamento paralelo e lógica switch-case para fluxos condicionais.

## 3\. Exemplos Práticos e Análise de Código

Agora, vamos explorar como implementar diferentes padrões de workflow usando o framework. Veremos exemplos de código em Python e .NET para cada caso.

### Caso 1: Workflow Sequencial Básico

Este é o padrão mais simples, onde a saída de um agente é passada diretamente para outro. Nosso cenário envolve um agente `FrontDesk` de hotel que faz uma recomendação de viagem, que é então revisada por um agente `Concierge`.

*Diagrama do workflow básico FrontDesk -\> Concierge.*

#### Contexto do Cenário

Um viajante pede uma recomendação em Paris.

1.  O agente `FrontDesk`, projetado para ser direto, sugere visitar o Museu do Louvre.
2.  O agente `Concierge`, que prioriza experiências autênticas, recebe essa sugestão. Ele revisa a recomendação e fornece um feedback, sugerindo uma alternativa mais local e menos turística.

#### Análise da Implementação em Python

No exemplo em Python, primeiro definimos e criamos os dois agentes, cada um com instruções específicas.

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

Em seguida, o `WorkflowBuilder` é usado para construir o grafo. O `front_desk_agent` é definido como o ponto de partida, e uma edge é criada para conectar sua saída ao `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Por fim, o workflow é executado com o prompt inicial do usuário.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Análise da Implementação em .NET (C#)

A implementação em .NET segue uma lógica muito semelhante. Primeiro, constantes são definidas para os nomes e instruções dos agentes.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Os agentes são criados usando um `OpenAIClient`, e então o `WorkflowBuilder` define o fluxo sequencial adicionando uma edge do `frontDeskAgent` para o `reviewerAgent`.

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

O workflow é então executado com a mensagem do usuário, e os resultados são transmitidos de volta.

### Caso 2: Workflow Sequencial Multi-Etapas

Este padrão estende a sequência básica para incluir mais agentes. É ideal para processos que requerem múltiplos estágios de refinamento ou transformação.

#### Contexto do Cenário

Um usuário fornece uma imagem de uma sala de estar e pede um orçamento de móveis.

1.  **Sales-Agent**: Identifica os itens de mobiliário na imagem e cria uma lista.
2.  **Price-Agent**: Pega a lista de itens e fornece um detalhamento de preços, incluindo opções econômicas, intermediárias e premium.
3.  **Quote-Agent**: Recebe a lista com preços e a formata em um documento de orçamento formal em Markdown.

*Diagrama do workflow Sales -\> Price -\> Quote.*

#### Análise da Implementação em Python

Três agentes são definidos, cada um com um papel especializado. O workflow é construído usando `add_edge` para criar uma cadeia: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

A entrada é uma `ChatMessage` que inclui texto e o URI da imagem. O framework lida com a passagem da saída de cada agente para o próximo na sequência até que o orçamento final seja gerado.

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

#### Análise da Implementação em .NET (C#)

O exemplo em .NET espelha a versão em Python. Três agentes (`salesagent`, `priceagent`, `quoteagent`) são criados. O `WorkflowBuilder` os conecta sequencialmente.

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

A mensagem do usuário é construída com os dados da imagem (como bytes) e o prompt de texto. O método `InProcessExecution.StreamAsync` inicia o workflow, e a saída final é capturada do stream.

### Caso 3: Workflow Concorrente

Este padrão é usado quando tarefas podem ser realizadas simultaneamente para economizar tempo. Ele envolve um "fan-out" para múltiplos agentes e um "fan-in" para agregar os resultados.

#### Contexto do Cenário

Um usuário pede para planejar uma viagem para Seattle.

1.  **Dispatcher (Fan-Out)**: A solicitação do usuário é enviada para dois agentes ao mesmo tempo.
2.  **Researcher-Agent**: Pesquisa atrações, clima e considerações importantes para uma viagem a Seattle em dezembro.
3.  **Plan-Agent**: Cria independentemente um itinerário detalhado dia a dia.
4.  **Aggregator (Fan-In)**: As saídas do pesquisador e do planejador são coletadas e apresentadas juntas como resultado final.

*Diagrama do workflow concorrente Researcher e Planner.*

#### Análise da Implementação em Python

O `ConcurrentBuilder` simplifica a criação deste padrão. Basta listar os agentes participantes, e o builder cria automaticamente a lógica necessária de fan-out e fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

O framework garante que o `research_agent` e o `plan_agent` sejam executados em paralelo, e suas saídas finais sejam coletadas em uma lista.

#### Análise da Implementação em .NET (C#)

Em .NET, este padrão requer uma definição mais explícita. Executores personalizados (`ConcurrentStartExecutor` e `ConcurrentAggregationExecutor`) são criados para lidar com a lógica de fan-out e fan-in.

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

O `WorkflowBuilder` então usa `AddFanOutEdge` e `AddFanInEdge` para construir o grafo com esses executores personalizados e os agentes.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Caso 4: Workflow Condicional

Workflows condicionais introduzem lógica de ramificação, permitindo que o sistema siga diferentes caminhos com base em resultados intermediários.

#### Contexto do Cenário

Este workflow automatiza a criação e publicação de um tutorial técnico.

1.  **Evangelist-Agent**: Escreve um rascunho do tutorial com base em um esboço e URLs fornecidos.
2.  **ContentReviewer-Agent**: Revisa o rascunho. Verifica se a contagem de palavras é superior a 200.
3.  **Ramificação Condicional**:
      * **Se Aprovado (`Yes`)**: O workflow prossegue para o `Publisher-Agent`.
      * **Se Rejeitado (`No`)**: O workflow para e exibe o motivo da rejeição.
4.  **Publisher-Agent**: Se o rascunho for aprovado, este agente salva o conteúdo em um arquivo Markdown.

#### Análise da Implementação em Python

Este exemplo usa uma função personalizada, `select_targets`, para implementar a lógica condicional. Esta função é passada para `add_multi_selection_edge_group` e direciona o workflow com base no campo `review_result` da saída do revisor.

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

Executores personalizados como `to_reviewer_result` são usados para analisar a saída JSON dos agentes e convertê-la em objetos fortemente tipados que a função de seleção pode inspecionar.

#### Análise da Implementação em .NET (C#)

A versão em .NET usa uma abordagem semelhante com uma função condicional. Um `Func<object?, bool>` é definido para verificar a propriedade `Result` do objeto `ReviewResult`.

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

O parâmetro `condition` do método `AddEdge` permite que o `WorkflowBuilder` crie um caminho de ramificação. O workflow seguirá apenas a edge para `publishExecutor` se a condição `GetCondition(expectedResult: "Yes")` retornar verdadeiro. Caso contrário, seguirá o caminho para `sendReviewerExecutor`.

## Conclusão

O Workflow do Microsoft Agent Framework oferece uma base robusta e flexível para orquestrar sistemas complexos e multi-agente. Ao aproveitar sua arquitetura baseada em grafos e componentes principais, os desenvolvedores podem projetar e implementar workflows sofisticados em Python e .NET. Seja sua aplicação baseada em processamento sequencial simples, execução paralela ou lógica condicional dinâmica, o framework oferece as ferramentas para construir soluções poderosas, escaláveis e com segurança de tipos.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante estar ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.