# Construindo Aplicações Multi-Agente com o Microsoft Agent Framework Workflow

Este tutorial irá guiá-lo pelo entendimento e construção de aplicações multi-agente usando o Microsoft Agent Framework. Exploraremos os conceitos principais de sistemas multi-agente, mergulharemos na arquitetura do componente Workflow do framework e passaremos por exemplos práticos tanto em Python quanto em .NET para diferentes padrões de workflow.

## 1\. Entendendo Sistemas Multi-Agente

Um Agente de IA é um sistema que vai além das capacidades de um Modelo de Linguagem Grande (LLM) padrão. Ele pode perceber seu ambiente, tomar decisões e executar ações para alcançar objetivos específicos. Um sistema multi-agente envolve vários desses agentes colaborando para resolver um problema que seria difícil ou impossível para um único agente resolver sozinho.

### Cenários Comuns de Aplicação

  * **Resolução Complexa de Problemas**: Dividir uma grande tarefa (ex: planejar um evento para toda a empresa) em subtarefas menores, gerenciadas por agentes especializados (ex: um agente de orçamento, um agente de logística, um agente de marketing).
  * **Assistentes Virtuais**: Um agente assistente principal delegando tarefas como agendamento, pesquisa e reservas para outros agentes especializados.
  * **Criação Automática de Conteúdo**: Um fluxo de trabalho onde um agente redige o conteúdo, outro revisa a precisão e o tom, e um terceiro publica.

### Padrões Multi-Agente

Sistemas multi-agente podem ser organizados em vários padrões, que determinam como eles interagem:

  * **Sequencial**: Agentes trabalham em uma ordem pré-definida, como uma linha de montagem. A saída de um agente torna-se a entrada para o próximo.
  * **Concorrente**: Agentes trabalham em paralelo em diferentes partes da tarefa, e seus resultados são agregados no final.
  * **Condicional**: O fluxo de trabalho segue caminhos diferentes com base na saída de um agente, semelhante a uma estrutura if-then-else.

## 2\. A Arquitetura do Workflow do Microsoft Agent Framework

O sistema de workflow do Agent Framework é um motor avançado de orquestração, projetado para gerenciar interações complexas entre múltiplos agentes. Ele é construído sobre uma arquitetura baseada em grafo que utiliza um [modelo de execução estilo Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), onde o processamento ocorre em etapas sincronizadas chamadas "supersteps".

### Componentes Principais

A arquitetura é composta por três partes principais:

1.  **Executores**: São as unidades fundamentais de processamento. Em nossos exemplos, um `Agent` é um tipo de executor. Cada executor pode ter múltiplos manipuladores de mensagens que são invocados automaticamente com base no tipo de mensagem recebida.
2.  **Arestas (Edges)**: Definem o caminho que as mensagens seguem entre os executores. As arestas podem ter condições, permitindo um roteamento dinâmico da informação através do grafo do workflow.
3.  **Workflow**: Este componente orquestra todo o processo, gerenciando os executores, as arestas e o fluxo geral de execução. Ele garante que as mensagens sejam processadas na ordem correta e transmite eventos para observabilidade.

*Um diagrama ilustrando os componentes principais do sistema de workflow.*

Essa estrutura permite construir aplicações robustas e escaláveis usando padrões fundamentais como cadeias sequenciais, fan-out/fan-in para processamento paralelo, e lógica switch-case para fluxos condicionais.

## 3\. Exemplos Práticos e Análise de Código

Agora, vamos explorar como implementar diferentes padrões de workflow usando o framework. Veremos código tanto em Python quanto em .NET para cada exemplo.

### Caso 1: Workflow Sequencial Básico

Este é o padrão mais simples, onde a saída de um agente é passada diretamente para outro. Nosso cenário envolve um agente de hotel `FrontDesk` que faz uma recomendação de viagem, revisada depois por um agente `Concierge`.

*Diagrama do workflow básico FrontDesk -> Concierge.*

#### Contexto do Cenário

Um viajante pede uma recomendação em Paris.

1.  O agente `FrontDesk`, projetado para brevidade, sugere visitar o Museu do Louvre.
2.  O agente `Concierge`, que prioriza experiências autênticas, recebe essa sugestão. Ele revisa a recomendação e fornece feedback, sugerindo uma alternativa mais local e menos turística.

#### Análise da Implementação em Python

No exemplo em Python, primeiro definimos e criamos os dois agentes, cada um com instruções específicas.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definir papéis e instruções do agente
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Criar instâncias de agentes
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Em seguida, o `WorkflowBuilder` é usado para construir o grafo. O `front_desk_agent` é definido como o ponto de partida, e uma aresta é criada para conectar sua saída ao `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Finalmente, o workflow é executado com o prompt inicial do usuário.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run executa o fluxo de trabalho; get_outputs() retorna o resultado do executor de saída.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Análise da Implementação em .NET (C#)

A implementação em .NET segue uma lógica muito similar. Primeiro, constantes são definidas para os nomes e instruções dos agentes.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Os agentes são criados usando um `AzureOpenAIClient` (API de Respostas), e então o `WorkflowBuilder` define o fluxo sequencial adicionando uma aresta do `frontDeskAgent` para o `reviewerAgent`.

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

O workflow é então executado com a mensagem do usuário, e os resultados são transmitidos de volta.

### Caso 2: Workflow Sequencial em Múltiplas Etapas

Este padrão estende a sequência básica para incluir mais agentes. É ideal para processos que exigem múltiplas etapas de refinamento ou transformação.

#### Contexto do Cenário

Um usuário oferece uma imagem de uma sala de estar e pede um orçamento para mobília.

1.  **Agente de Vendas**: Identifica os itens de mobília na imagem e cria uma lista.
2.  **Agente de Preços**: Recebe a lista de itens e fornece uma detalhada discriminação de preços, incluindo opções econômicas, intermediárias e premium.
3.  **Agente de Orçamento**: Recebe a lista precificada e formata-a em um documento formal de orçamento em Markdown.

*Diagrama do workflow Vendas -> Preço -> Orçamento.*

#### Análise da Implementação em Python

Três agentes são definidos, cada um com um papel especializado. O workflow é construído usando `add_edge` para criar uma cadeia: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Crie três agentes especializados
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Construa o fluxo de trabalho sequencial
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

A entrada é uma `ChatMessage` que inclui tanto texto quanto o URI da imagem. O framework cuida de passar a saída de cada agente para o seguinte na sequência até que o orçamento final seja gerado.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# A mensagem do usuário contém texto e uma imagem
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Execute o fluxo de trabalho
events = await workflow.run(message)
```

#### Análise da Implementação em .NET (C#)

O exemplo em .NET espelha a versão em Python. Três agentes (`salesagent`, `priceagent`, `quoteagent`) são criados. O `WorkflowBuilder` os conecta sequencialmente.

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

A mensagem do usuário é construída com os dados da imagem (em bytes) e o prompt de texto. O método `InProcessExecution.RunStreamingAsync` inicia o workflow e a saída final é capturada do stream.

### Caso 3: Workflow Concorrente

Este padrão é usado quando tarefas podem ser realizadas simultaneamente para economizar tempo. Envolve um "fan-out" para múltiplos agentes e um "fan-in" para agregar os resultados.

#### Contexto do Cenário

Um usuário pede para planejar uma viagem a Seattle.

1.  **Despachante (Fan-Out)**: A solicitação do usuário é enviada a dois agentes ao mesmo tempo.
2.  **Agente Pesquisador**: Pesquisa atrações, clima e considerações chave para uma viagem a Seattle em dezembro.
3.  **Agente Planejador**: Cria independentemente um itinerário detalhado dia a dia.
4.  **Agregador (Fan-In)**: As saídas tanto do pesquisador quanto do planejador são coletadas e apresentadas juntas como resultado final.

*Diagrama do workflow concorrente Pesquisador e Planejador.*

#### Análise da Implementação em Python

O `ConcurrentBuilder` simplifica a criação deste padrão. Você simplesmente lista os agentes participantes, e o builder cria automaticamente a lógica necessária de fan-out e fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder lida com a lógica de dispersão/convergência
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Execute o fluxo de trabalho
events = await workflow.run("Plan a trip to Seattle in December")
```

O framework garante que o `research_agent` e o `plan_agent` executem em paralelo, e as saídas finais sejam coletadas numa lista.

#### Análise da Implementação em .NET (C#)

Em .NET, este padrão requer uma definição mais explícita. Executores personalizados (`ConcurrentStartExecutor` e `ConcurrentAggregationExecutor`) são criados para gerenciar a lógica de fan-out e fan-in.

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

O `WorkflowBuilder` então utiliza `AddFanOutEdge` e `AddFanInEdge` para construir o grafo com esses executores personalizados e os agentes.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Caso 4: Workflow Condicional

Workflows condicionais introduzem lógica de ramificação, permitindo que o sistema siga caminhos diferentes baseados em resultados intermediários.

#### Contexto do Cenário

Este workflow automatiza a criação e publicação de um tutorial técnico.

1.  **Agente Evangelista**: Redige um rascunho do tutorial baseado em um esboço e URLs fornecidos.
2.  **Agente Revisor de Conteúdo**: Revisa o rascunho. Verifica se a contagem de palavras é superior a 200.
3.  **Ramificação Condicional**:
      * **Se Aprovado (`Sim`)**: O workflow prossegue para o `Agente Publicador`.
      * **Se Rejeitado (`Não`)**: O workflow para e exibe a razão da rejeição.
4.  **Agente Publicador**: Se o rascunho for aprovado, este agente salva o conteúdo em um arquivo Markdown.

#### Análise da Implementação em Python

Este exemplo utiliza uma função customizada, `select_targets`, para implementar a lógica condicional. Essa função é passada para `add_multi_selection_edge_group` e direciona o workflow com base no campo `review_result` da saída do revisor.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Esta função determina o próximo passo com base no resultado da revisão
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Se aprovado, prossiga para o executor 'save_draft'
        return [save_draft_id]
    else:
        # Se rejeitado, prossiga para o executor 'handle_review' para reportar falha
        return [handle_review_id]

# O construtor de fluxo usa a função de seleção para roteamento
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # A aresta de seleção múltipla implementa a lógica condicional
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executores customizados como `to_reviewer_result` são usados para analisar a saída JSON dos agentes e convertê-la em objetos fortemente tipados que a função de seleção pode inspecionar.

#### Análise da Implementação em .NET (C#)

A versão .NET usa uma abordagem similar com uma função condicional. Um `Func<object?, bool>` é definido para checar a propriedade `Result` do objeto `ReviewResult`.

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

O parâmetro `condition` do método `AddEdge` permite ao `WorkflowBuilder` criar um caminho de ramificação. O workflow seguirá a aresta para `publishExecutor` somente se a condição `GetCondition(expectedResult: "Yes")` retornar true. Caso contrário, seguirá o caminho para `sendReviewerExecutor`.

## Conclusão

O Microsoft Agent Framework Workflow fornece uma base sólida e flexível para orquestrar sistemas complexos multi-agente. Ao aproveitar sua arquitetura baseada em grafo e componentes principais, desenvolvedores podem projetar e implementar workflows sofisticados tanto em Python quanto em .NET. Seja sua aplicação necessitando de processamento sequencial simples, execução paralela ou lógica condicional dinâmica, o framework oferece as ferramentas para construir soluções potentes, escaláveis e fortemente tipadas com IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->