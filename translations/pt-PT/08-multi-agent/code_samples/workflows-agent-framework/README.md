# Construção de Aplicações Multi-Agente com o Microsoft Agent Framework Workflow

Este tutorial irá guiá-lo na compreensão e construção de aplicações multi-agente usando o Microsoft Agent Framework. Vamos explorar os conceitos fundamentais dos sistemas multi-agente, analisar a arquitetura do componente Workflow do framework e percorrer exemplos práticos em Python e .NET para diferentes padrões de fluxo de trabalho.

## 1\. Compreender os Sistemas Multi-Agente

Um Agente de IA é um sistema que ultrapassa as capacidades de um Modelo de Linguagem Grande (LLM) padrão. Pode perceber o seu ambiente, tomar decisões e realizar ações para atingir objetivos específicos. Um sistema multi-agente envolve vários destes agentes a colaborarem para resolver um problema que seria difícil ou impossível para um único agente resolver sozinho.

### Cenários Comuns de Aplicação

  * **Resolução de Problemas Complexos**: Dividir uma tarefa grande (ex., planear um evento para toda a empresa) em sub-tarefas menores tratadas por agentes especializados (ex., agente de orçamento, agente de logística, agente de marketing).
  * **Assistentes Virtuais**: Um agente assistente principal que delega tarefas como agendamento, pesquisa e reservas para outros agentes especializados.
  * **Criação Automática de Conteúdo**: Um fluxo de trabalho onde um agente redige conteúdo, outro o revê para precisão e tom, e um terceiro publica-o.

### Padrões Multi-Agente

Os sistemas multi-agente podem ser organizados em vários padrões, que determinam como interagem:

  * **Sequencial**: Os agentes trabalham numa ordem predefinida, como numa linha de montagem. A saída de um agente torna-se a entrada do seguinte.
  * **Concorrente**: Os agentes trabalham em paralelo em diferentes partes de uma tarefa, e os seus resultados são agregados no final.
  * **Condicional**: O fluxo de trabalho segue diferentes caminhos com base na saída de um agente, semelhante a uma instrução if-then-else.

## 2\. A Arquitetura do Microsoft Agent Framework Workflow

O sistema de fluxo de trabalho do Agent Framework é um motor de orquestração avançado concebido para gerir interações complexas entre múltiplos agentes. Baseia-se numa arquitetura orientada a grafos que usa um [modelo de execução ao estilo Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), onde o processamento ocorre em passos sincronizados chamados "supersteps."

### Componentes Principais

A arquitetura é composta por três partes principais:

1.  **Executores**: São as unidades fundamentais de processamento. Nos nossos exemplos, um `Agent` é um tipo de executor. Cada executor pode ter vários manipuladores de mensagens que são invocados automaticamente com base no tipo de mensagem recebida.
2.  **Arestas**: Definem o caminho que as mensagens seguem entre os executores. As arestas podem ter condições, permitindo o encaminhamento dinâmico da informação através do grafo do fluxo de trabalho.
3.  **Workflow**: Este componente orquestra todo o processo, gerindo os executores, as arestas e o fluxo geral de execução. Garante que as mensagens são processadas na ordem correta e transmite eventos para observabilidade.

*Um diagrama que ilustra os componentes principais do sistema de fluxo de trabalho.*

Esta estrutura permite construir aplicações robustas e escaláveis utilizando padrões fundamentais como cadeias sequenciais, fan-out/fan-in para processamento paralelo, e lógica switch-case para fluxos condicionais.

## 3\. Exemplos Práticos e Análise de Código

Agora, vamos explorar como implementar diferentes padrões de fluxo de trabalho usando o framework. Vamos ver código em Python e .NET para cada exemplo.

### Caso 1: Fluxo de Trabalho Sequencial Básico

Este é o padrão mais simples, onde a saída de um agente é passada diretamente para outro. O nosso cenário envolve um agente `FrontDesk` de hotel que faz uma recomendação de viagem, que é depois revista por um agente `Concierge`.

*Diagrama do fluxo básico FrontDesk -\> Concierge.*

#### Contexto do Cenário

Um viajante pede uma recomendação em Paris.

1.  O agente `FrontDesk`, concebido para ser sucinto, sugere visitar o Museu do Louvre.
2.  O agente `Concierge`, que prioriza experiências autênticas, recebe esta sugestão. Revê a recomendação e fornece feedback, sugerindo uma alternativa mais local e menos turística.

#### Análise da Implementação em Python

No exemplo em Python, definimos primeiro e criamos os dois agentes, cada um com instruções específicas.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definir papéis de agente e instruções
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

De seguida, usa-se o `WorkflowBuilder` para construir o grafo. O `front_desk_agent` é definido como o ponto de partida, e uma aresta é criada para ligar a sua saída ao `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Finalmente, o fluxo de trabalho é executado com o prompt inicial do utilizador.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run executa o fluxo de trabalho; get_outputs() retorna o resultado do executor de saída.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Análise da Implementação em .NET (C#)

A implementação em .NET segue uma lógica muito semelhante. Primeiro, definem-se constantes para os nomes e instruções dos agentes.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Os agentes são criados usando um `AzureOpenAIClient` (API de respostas), e depois o `WorkflowBuilder` define o fluxo sequencial adicionando uma aresta do `frontDeskAgent` para o `reviewerAgent`.

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

O fluxo de trabalho é depois executado com a mensagem do utilizador, e os resultados são transmitidos em streaming.

### Caso 2: Fluxo de Trabalho Sequencial com Múltiplos Passos

Este padrão estende a sequência básica para incluir mais agentes. É ideal para processos que requerem múltiplas fases de refinamento ou transformação.

#### Contexto do Cenário

Um utilizador fornece uma imagem de uma sala de estar e pede uma cotação para mobiliário.

1.  **Agente de Vendas**: Identifica os itens de mobiliário na imagem e cria uma lista.
2.  **Agente de Preços**: Recebe a lista de itens e fornece uma discriminação detalhada de preços, incluindo opções de orçamento, gama média e premium.
3.  **Agente de Cotação**: Recebe a lista com preços e formata-a num documento formal de cotação em Markdown.

*Diagrama do fluxo Sales -\> Price -\> Quote.*

#### Análise da Implementação em Python

Três agentes são definidos, cada um com um papel especializado. O fluxo de trabalho é construído usando `add_edge` para criar a cadeia: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Criar três agentes especializados
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Construir o fluxo de trabalho sequencial
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

A entrada é uma `ChatMessage` que inclui tanto texto como a URI da imagem. O framework gere a passagem da saída de cada agente para o seguinte na sequência até a cotação final ser gerada.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# A mensagem do utilizador contém texto e uma imagem
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Executar o fluxo de trabalho
events = await workflow.run(message)
```

#### Análise da Implementação em .NET (C#)

O exemplo em .NET espelha a versão em Python. São criados três agentes (`salesagent`, `priceagent`, `quoteagent`). O `WorkflowBuilder` liga-os sequencialmente.

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

A mensagem do utilizador é construída com os dados da imagem (em bytes) e o prompt de texto. O método `InProcessExecution.RunStreamingAsync` inicia o fluxo de trabalho, e a saída final é capturada do stream.

### Caso 3: Fluxo de Trabalho Concorrente

Este padrão é usado quando as tarefas podem ser realizadas simultaneamente para poupar tempo. Envolve um "fan-out" para múltiplos agentes e um "fan-in" para agregar os resultados.

#### Contexto do Cenário

Um utilizador pede para planear uma viagem a Seattle.

1.  **Despachante (Fan-Out)**: O pedido do utilizador é enviado a dois agentes ao mesmo tempo.
2.  **Agente Pesquisador**: Pesquisa atrações, clima e considerações chave para uma viagem a Seattle em dezembro.
3.  **Agente de Planeamento**: Cria independentemente um itinerário detalhado dia a dia.
4.  **Agregador (Fan-In)**: As saídas do pesquisador e do planeador são recolhidas e apresentadas em conjunto como resultado final.

*Diagrama do fluxo concorrente Researcher e Planner.*

#### Análise da Implementação em Python

O `ConcurrentBuilder` simplifica a criação deste padrão. Basta listar os agentes participantes e o construtor cria automaticamente a lógica necessária de fan-out e fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder gere a lógica de bifurcação/reunião
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Executar o fluxo de trabalho
events = await workflow.run("Plan a trip to Seattle in December")
```

O framework assegura que o `research_agent` e o `plan_agent` executam em paralelo, e as suas saídas finais são recolhidas numa lista.

#### Análise da Implementação em .NET (C#)

Em .NET, este padrão requer uma definição mais explícita. São criados executores personalizados (`ConcurrentStartExecutor` e `ConcurrentAggregationExecutor`) para gerir a lógica de fan-out e fan-in.

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

O `WorkflowBuilder` usa depois `AddFanOutEdge` e `AddFanInEdge` para construir o grafo com estes executores personalizados e os agentes.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Caso 4: Fluxo de Trabalho Condicional

Os fluxos condicionais introduzem lógica de ramificação, permitindo que o sistema siga caminhos diferentes com base nos resultados intermédios.

#### Contexto do Cenário

Este fluxo automatiza a criação e publicação de um tutorial técnico.

1.  **Agente Evangelista**: Escreve um rascunho do tutorial baseado num esboço e URLs fornecidos.
2.  **Agente Revisor de Conteúdo**: Revê o rascunho. Verifica se a contagem de palavras ultrapassa 200 palavras.
3.  **Ramo Condicional**:
      * **Se aprovado (`Sim`)**: O fluxo segue para o agente `Publisher`.
      * **Se rejeitado (`Não`)**: O fluxo para e apresenta o motivo da rejeição.
4.  **Agente Publisher**: Se o rascunho for aprovado, este agente guarda o conteúdo num ficheiro Markdown.

#### Análise da Implementação em Python

Este exemplo utiliza uma função personalizada, `select_targets`, para implementar a lógica condicional. Esta função é passada para `add_multi_selection_edge_group` e direciona o fluxo de trabalho com base no campo `review_result` da saída do revisor.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Esta função determina o próximo passo com base no resultado da revisão
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Se aprovado, prosseguir para o executor 'save_draft'
        return [save_draft_id]
    else:
        # Se rejeitado, prosseguir para o executor 'handle_review' para reportar falha
        return [handle_review_id]

# O construtor de workflow utiliza a função de seleção para o encaminhamento
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

Executores personalizados como `to_reviewer_result` são usados para interpretar a saída JSON dos agentes e convertê-la em objetos fortemente tipados que a função de seleção pode inspeccionar.

#### Análise da Implementação em .NET (C#)

A versão .NET usa uma abordagem semelhante com uma função condicional. Um `Func<object?, bool>` é definido para verificar a propriedade `Result` do objeto `ReviewResult`.

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

O parâmetro `condition` do método `AddEdge` permite ao `WorkflowBuilder` criar um caminho ramificado. O fluxo de trabalho segue a aresta para `publishExecutor` somente se a condição `GetCondition(expectedResult: "Yes")` retornar verdadeiro. Caso contrário, segue o caminho para `sendReviewerExecutor`.

## Conclusão

O Microsoft Agent Framework Workflow oferece uma base robusta e flexível para orquestrar sistemas multi-agente complexos. Aproveitando a sua arquitetura orientada a grafos e os componentes principais, os desenvolvedores podem desenhar e implementar fluxos de trabalho sofisticados em Python e .NET. Quer a sua aplicação necessite de processamento sequencial simples, execução paralela ou lógica condicional dinâmica, o framework oferece as ferramentas para construir soluções poderosas, escaláveis e seguras por tipagem, potenciadas por IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->