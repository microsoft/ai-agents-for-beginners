# Explorando o Microsoft Agent Framework

![Agent Framework](../../../translated_images/pt-BR/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introdução

Esta lição cobrirá:

- Entendendo o Microsoft Agent Framework: Principais Características e Valor  
- Explorando os Conceitos-Chave do Microsoft Agent Framework
- Padrões Avançados do MAF: Workflows, Middleware e Memória

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como:

- Construir Agentes de IA Prontos para Produção usando o Microsoft Agent Framework
- Aplicar as funcionalidades principais do Microsoft Agent Framework para seus Casos de Uso Agentes
- Usar padrões avançados incluindo workflows, middleware e observabilidade

## Exemplos de Código 

Exemplos de código para [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) podem ser encontrados neste repositório, nas pastas `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Entendendo o Microsoft Agent Framework

![Framework Intro](../../../translated_images/pt-BR/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) é o framework unificado da Microsoft para construção de agentes de IA. Ele oferece flexibilidade para atender à ampla variedade de casos de uso agentes observados em ambientes de produção e de pesquisa, incluindo:

- **Orquestração Sequencial de Agentes** em cenários onde workflows passo a passo são necessários.
- **Orquestração Concorrente** em cenários onde agentes precisam completar tarefas ao mesmo tempo.
- **Orquestração de Chat em Grupo** em cenários onde agentes podem colaborar juntos numa tarefa.
- **Orquestração de Transferência (Handoff)** em cenários onde agentes passam a tarefa uns aos outros à medida que as subtarefas são concluídas.
- **Orquestração Magnética** em cenários onde um agente gerenciador cria e modifica uma lista de tarefas e coordena subagentes para completar a tarefa.

Para entregar Agentes de IA em Produção, o MAF também inclui funcionalidades para:

- **Observabilidade** por meio do uso do OpenTelemetry, onde cada ação do agente de IA, incluindo invocação de ferramentas, passos da orquestração, fluxos de raciocínio e monitoramento de desempenho por dashboards do Microsoft Foundry.
- **Segurança** hospedando os agentes nativamente no Microsoft Foundry, que inclui controles de segurança como acesso baseado em funções, manuseio de dados privados e segurança integrada de conteúdo.
- **Durabilidade** pois threads e workflows de agentes podem pausar, retomar e se recuperar de erros, o que possibilita processos de maior duração.
- **Controle** pois workflows humano no loop são suportados, onde tarefas são marcadas como exigindo aprovação humana.

O Microsoft Agent Framework também foca em ser interoperável através de:

- **Ser Cloud-agnóstico** - agentes podem rodar em containers, on-premises e em múltiplas clouds diferentes.
- **Ser Provider-agnóstico** - agentes podem ser criados via seu SDK preferido incluindo Azure OpenAI e OpenAI
- **Integrar Padrões Abertos** - agentes podem usar protocolos como Agent-to-Agent(A2A) e Model Context Protocol (MCP) para descobrir e usar outros agentes e ferramentas.
- **Plugins e Conectores** - Conexões podem ser feitas a serviços de dados e memória como Microsoft Fabric, SharePoint, Pinecone e Qdrant.

Vamos ver como essas funcionalidades são aplicadas a alguns dos conceitos principais do Microsoft Agent Framework.

## Conceitos-Chave do Microsoft Agent Framework

### Agentes

![Agent Framework](../../../translated_images/pt-BR/agent-components.410a06daf87b4fef.webp)

**Criando Agentes**

A criação do agente é feita definindo o serviço de inferência (provedor LLM), um
conjunto de instruções para o agente de IA seguir, e um `nome` atribuído:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

O exemplo acima usa `Azure OpenAI`, mas agentes podem ser criados usando vários serviços incluindo `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

APIs OpenAI de `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou [MiniMax](https://platform.minimaxi.com/), que fornece API compatível com OpenAI e grandes janelas de contexto (até 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou agentes remotos usando protocolo A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Executando Agentes**

Os agentes são executados usando os métodos `.run` ou `.run_stream` para respostas não-streaming ou streaming respectivamente.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Cada execução do agente pode também ter opções para personalizar parâmetros como `max_tokens` usados pelo agente, `tools` que o agente pode chamar, e até o próprio `model` usado para o agente.

Isso é útil em casos onde modelos ou ferramentas específicas são requeridos para completar uma tarefa do usuário.

**Ferramentas**

Ferramentas podem ser definidas tanto ao definir o agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Ao criar um ChatAgent diretamente

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

quanto também ao executar o agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Ferramenta fornecida apenas para esta execução )
```

**Threads de Agentes**

Threads de agentes são usadas para lidar com conversas multi-turno. Threads podem ser criadas por meio de:

- Usar `get_new_thread()` que permite a thread ser salva ao longo do tempo
- Criar uma thread automaticamente ao executar um agente, fazendo a thread durar somente essa execução.

Para criar uma thread, o código é assim:

```python
# Crie uma nova thread.
thread = agent.get_new_thread() # Execute o agente com a thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Você pode então serializar a thread para armazená-la para uso futuro:

```python
# Crie uma nova thread.
thread = agent.get_new_thread() 

# Execute o agente com a thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialize a thread para armazenamento.

serialized_thread = await thread.serialize() 

# Desserialize o estado da thread após carregar do armazenamento.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware do Agente**

Agentes interagem com ferramentas e LLMs para completar as tarefas do usuário. Em certos cenários, queremos executar ou rastrear entre essas interações. Middleware de agente nos permite fazer isso por meio de:

*Middleware de Função*

Esse middleware permite executar uma ação entre o agente e a função/ferramenta que ele irá chamar. Um exemplo de uso é quando se deseja fazer algum registro (logging) na chamada da função.

No código abaixo, `next` define se o próximo middleware ou a função real deve ser chamada.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pré-processamento: Registrar antes da execução da função
    print(f"[Function] Calling {context.function.name}")

    # Continuar para o próximo middleware ou execução da função
    await next(context)

    # Pós-processamento: Registrar depois da execução da função
    print(f"[Function] {context.function.name} completed")
```

*Middleware de Chat*

Esse middleware permite executar ou registrar uma ação entre o agente e as requisições feitas para o LLM.

Isso inclui informações importantes como as `messages` que estão sendo enviadas ao serviço de IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pré-processamento: Registrar antes da chamada de IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuar para o próximo middleware ou serviço de IA
    await next(context)

    # Pós-processamento: Registrar após a resposta da IA
    print("[Chat] AI response received")

```

**Memória do Agente**

Como coberto na lição `Memória Agente`, a memória é um elemento importante para permitir que o agente opere sobre diferentes contextos. O MAF oferece vários tipos diferentes de memórias:

*Memória em Memória RAM*

Esta é a memória armazenada em threads durante o tempo de execução do aplicativo.

```python
# Crie uma nova thread.
thread = agent.get_new_thread() # Execute o agente com a thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mensagens Persistentes*

Essa memória é usada para armazenar o histórico da conversa ao longo de diferentes sessões. Ela é definida usando o `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Criar um armazenamento de mensagens personalizado
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memória Dinâmica*

Essa memória é adicionada ao contexto antes que os agentes sejam executados. Essas memórias podem ser armazenadas em serviços externos como mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Usando Mem0 para recursos avançados de memória
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

**Observabilidade do Agente**

A observabilidade é importante para construir sistemas agentes confiáveis e manuteníveis. O MAF integra com OpenTelemetry para fornecer traces e métricas para melhor observabilidade.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # faça algo
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

O MAF oferece workflows que são passos pré-definidos para completar uma tarefa, incluindo agentes IA como componentes desses passos.

Workflows são compostos por diferentes componentes que permitem maior controle no fluxo. Workflows também permitem **orquestração multi-agentes** e **criação de checkpoints** para salvar estados do workflow.

Os componentes principais de um workflow são:

**Executores**

Os executores recebem mensagens de entrada, realizam as tarefas atribuídas e depois produzem uma mensagem de saída. Isso move o workflow adiante na direção de completar a tarefa maior. Os executores podem ser agentes IA ou lógica customizada.

**Arestas (Edges)**

As arestas são usadas para definir o fluxo de mensagens em um workflow. Estas podem ser:

*Arestas Diretas* - Conexões simples um para um entre executores:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Arestas Condicionais* - Ativadas após o cumprimento de certa condição. Por exemplo, quando quartos de hotel estão indisponíveis, um executor pode sugerir outras opções.

*Arestas switch-case* - Encaminham mensagens para diferentes executores baseados em condições definidas. Por exemplo, se um cliente de viagem tem acesso prioritário, suas tarefas serão tratadas por outro workflow.

*Arestas Fan-out* - Enviam uma mensagem para múltiplos destinatários.

*Arestas Fan-in* - Coletam múltiplas mensagens de diferentes executores e enviam para um destinatário.

**Eventos**

Para oferecer melhor observabilidade em workflows, o MAF oferece eventos embutidos de execução, incluindo:

- `WorkflowStartedEvent`  - Execução do workflow começa
- `WorkflowOutputEvent` - Workflow produz uma saída
- `WorkflowErrorEvent` - Workflow encontra um erro
- `ExecutorInvokeEvent`  - Executor começa processamento
- `ExecutorCompleteEvent`  - Executor finaliza processamento
- `RequestInfoEvent` - Uma requisição é emitida

## Padrões Avançados do MAF

As seções acima cobrem os conceitos chave do Microsoft Agent Framework. À medida que você constrói agentes mais complexos, aqui estão alguns padrões avançados a considerar:

- **Composição Middleware**: encadeie múltiplos handlers de middleware (logging, auth, rate-limiting) usando middleware de função e de chat para controle refinado do comportamento do agente.
- **Checkpointing no Workflow**: use eventos do workflow e serialização para salvar e retomar processos longos do agente.
- **Seleção Dinâmica de Ferramentas**: combine RAG sobre descrições de ferramentas com o registro de ferramentas do MAF para apresentar apenas ferramentas relevantes por consulta.
- **Transferência Multi-Agente**: use arestas de workflow e roteamento condicional para orquestrar transferências entre agentes especializados.

## Hospedando Agentes LangChain / LangGraph no Microsoft Foundry

O Microsoft Agent Framework é **interoperável entre frameworks** — você não está limitado a agentes escritos com MAF. Se já tem um agente construido com **LangChain** ou **LangGraph**, pode executá-lo como um **agente hospedado no Microsoft Foundry** para que Foundry gerencie o runtime, sessões, escalabilidade, identidade e endpoints de protocolo para você, enquanto sua lógica do agente permanece no LangGraph.

Isso é feito com o pacote `langchain_azure_ai.agents.hosting`, que expõe um grafo LangGraph compilado pelos mesmos protocolos usados por agentes hospedados em Foundry.

**1. Instale o extra de hospedagem:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

O extra `hosting` instala as bibliotecas de protocolo Foundry: `azure-ai-agentserver-responses` (o endpoint `/responses` compatível com OpenAI) e `azure-ai-agentserver-invocations` (endpoint genérico `/invocations`).

**2. Escolha um protocolo de hospedagem:**

| Protocolo | Classe Host | Endpoint | Use quando |
|----------|-------------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Você quer chat compatível com OpenAI, streaming, histórico de respostas e threading de conversa — o padrão recomendado para agentes conversacionais. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Você precisa de um formato JSON customizado, um endpoint estilo webhook, ou processamento não conversacional. |

Como **a API Responses é a API principal para desenvolvimento tipo agente em Foundry**, comece com `ResponsesHostServer` para a maioria dos agentes.

**3. Configure variáveis de ambiente** (`az login` primeiro para que `DefaultAzureCredential` possa autenticar):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Quando o agente rodar depois como agente hospedado em Foundry, a plataforma injeta `FOUNDRY_PROJECT_ENDPOINT` automaticamente.

**4. Exponha um agente LangGraph pelo protocolo Responses:**

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

    # ChatOpenAI aqui direciona para o endpoint compatível com OpenAI (Responses) do projeto Foundry.
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

Execute localmente com `python main.py`, depois envie uma requisição Responses para `http://localhost:8088/responses`.

**Comportamentos principais:**

- **Conversas**: Clientes continuam uma conversa ao passar `previous_response_id` ou um ID de `conversation`. Se seu grafo for compilado com LangGraph checkpointer, Foundry associa o estado da conversa ao checkpoint (use um checkpointer durável em produção; `MemorySaver` é adequado para testes locais).
- **Humano no loop**: Se seu grafo usa LangGraph `interrupt()`, `ResponsesHostServer` apresenta a interrupção pendente como um item Responses `function_call` / `mcp_approval_request`, e os clientes retomam com um `function_call_output` / `mcp_approval_response` correspondente.
- **Deploy para Foundry**: Use Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, precisa Docker), depois `azd provision` e `azd deploy`. Deploy como agente hospedado requer a função **Foundry Project Manager**.

Um exemplo executável deste código vive em [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Para o tutorial completo (protocolo Invocations, schemas customizados de requisição e solução de problemas), veja [Hospede agentes LangGraph como agentes hospedados no Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Exemplos de Código 

Exemplos de código para Microsoft Agent Framework podem ser encontrados neste repositório, nas pastas `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Tem Mais Perguntas sobre Microsoft Agent Framework?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de office hours e obter respostas sobre seus Agentes de IA.
## Lição Anterior

[Memória para Agentes de IA](../13-agent-memory/README.md)

## Próxima Lição

[Construindo Agentes de Uso de Computador (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->