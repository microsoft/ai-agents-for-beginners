# Explorando o Microsoft Agent Framework

![Agent Framework](../../../translated_images/pt-PT/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introdução

Esta lição irá abordar:

- Compreender o Microsoft Agent Framework: Características principais e valor  
- Explorar os Conceitos Chave do Microsoft Agent Framework
- Padrões avançados do MAF: Workflows, Middleware e Memória

## Objetivos de Aprendizagem

Após completar esta lição, saberá como:

- Construir Agentes de IA Prontos para Produção usando o Microsoft Agent Framework
- Aplicar as funcionalidades principais do Microsoft Agent Framework aos seus Casos de Uso Agénticos
- Usar padrões avançados incluindo workflows, middleware e observabilidade

## Exemplos de Código 

Exemplos de código para o [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) podem ser encontrados neste repositório nos ficheiros `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Compreendendo o Microsoft Agent Framework

![Framework Intro](../../../translated_images/pt-PT/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) é a framework unificada da Microsoft para construir agentes de IA. Oferece a flexibilidade para abordar a grande variedade de casos de uso agénticos encontrados tanto em ambientes de produção como de pesquisa, incluindo:

- **Orquestração sequencial de agentes** em cenários onde são necessários workflows passo a passo.
- **Orquestração concorrente** em cenários onde agentes precisam realizar tarefas em simultâneo.
- **Orquestração de chat em grupo** em cenários onde agentes podem colaborar juntos numa tarefa.
- **Orquestração de passagem de tarefa** em cenários onde agentes passam a tarefa uns aos outros à medida que as subtarefas são concluídas.
- **Orquestração magnética** em cenários onde um agente gestor cria e modifica uma lista de tarefas e gere a coordenação dos subagentes para completar a tarefa.

Para entregar Agentes de IA em Produção, o MAF inclui também funcionalidades para:

- **Observabilidade** através do uso de OpenTelemetry onde cada ação do Agente de IA incluindo invocação de ferramentas, passos de orquestração, fluxos de raciocínio e monitorização de desempenho através dos dashboards Microsoft Foundry.
- **Segurança** ao hospedar agentes nativamente na Microsoft Foundry, que inclui controlos de segurança tais como acesso baseado em funções, tratamento de dados privados e segurança de conteúdo embutida.
- **Durabilidade** pois os threads e workflows do agente podem pausar, retomar e recuperar de erros, permitindo processos de longa duração.
- **Controlo** pois são suportados workflows de humano no ciclo onde as tarefas são marcadas como requerendo aprovação humana.

O Microsoft Agent Framework foca-se também na interoperabilidade através de:

- **Ser Cloud-agnóstico** – Agentes podem correr em contentores, on-premises e através de múltiplas clouds diferentes.
- **Ser Provider-agnóstico** – Agentes podem ser criados com o seu SDK preferido incluindo Azure OpenAI e OpenAI
- **Integrar Standards Abertos** – Agentes podem utilizar protocolos como Agent-to-Agent (A2A) e Model Context Protocol (MCP) para descobrir e usar outros agentes e ferramentas.
- **Plugins e Conectores** – Conexões podem ser feitas a serviços de dados e memória como Microsoft Fabric, SharePoint, Pinecone e Qdrant.

Vamos ver como estas funcionalidades são aplicadas a alguns dos conceitos chave do Microsoft Agent Framework.

## Conceitos Chave do Microsoft Agent Framework

### Agentes

![Agent Framework](../../../translated_images/pt-PT/agent-components.410a06daf87b4fef.webp)

**Criar Agentes**

A criação de agentes é feita definindo o serviço de inferência (Fornecedor LLM), um
conjunto de instruções para o Agente de IA seguir, e um `nome` atribuído:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

O exemplo acima usa `Azure OpenAI` mas agentes podem ser criados usando uma variedade de serviços incluindo o `Microsoft Foundry Agent Service`:

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

ou [MiniMax](https://platform.minimaxi.com/), que fornece uma API compatível com OpenAI com janelas de contexto grandes (até 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou agentes remotos usando o protocolo A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Executar Agentes**

Agentes são executados utilizando os métodos `.run` ou `.run_stream` para respostas não-streaming ou streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Cada execução de agente pode também ter opções para personalizar parâmetros tais como `max_tokens` usados pelo agente, `tools` que o agente pode chamar, e até o próprio `model` usado para o agente.

Isto é útil em casos onde modelos ou ferramentas específicas são requeridas para completar a tarefa do utilizador.

**Ferramentas**

Ferramentas podem ser definidas tanto ao definir o agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Quando criar um ChatAgent diretamente

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

e também ao executar o agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Ferramenta fornecida apenas para este uso )
```

**Threads de Agente**

Threads de Agente são usadas para gerir conversas multi-turno. Threads podem ser criadas por:

- Usar `get_new_thread()` que permite que o thread seja guardado ao longo do tempo
- Criar um thread automaticamente quando se executa um agente e o thread existir apenas durante essa execução.

Para criar um thread, o código é:

```python
# Criar um novo thread.
thread = agent.get_new_thread() # Executar o agente com o thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Pode depois serializar o thread para ser armazenado para uso futuro:

```python
# Criar uma nova thread.
thread = agent.get_new_thread() 

# Executar o agente com a thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializar a thread para armazenamento.

serialized_thread = await thread.serialize() 

# Desserializar o estado da thread após carregar do armazenamento.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware do Agente**

Agentes interagem com ferramentas e LLMs para completar as tarefas dos utilizadores. Em certos cenários, queremos executar ou rastrear interações intermédias. Middleware do agente permite fazer isso através de:

*Middleware de Função*

Este middleware permite executar uma ação entre o agente e uma função/ferramenta que irá chamar. Um exemplo de uso é quando se quer registar a chamada da função.

No código abaixo, `next` define se o próximo middleware ou a função real deve ser chamada.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pré-processamento: Registar antes da execução da função
    print(f"[Function] Calling {context.function.name}")

    # Continuar para o próximo middleware ou execução da função
    await next(context)

    # Pós-processamento: Registar após a execução da função
    print(f"[Function] {context.function.name} completed")
```

*Middleware de Chat*

Este middleware permite executar ou registar uma ação entre o agente e os pedidos ao LLM.

Isto contém informação importante como as `messages` que estão a ser enviadas ao serviço de IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pré-processamento: Registar antes da chamada à IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuar para o próximo middleware ou serviço de IA
    await next(context)

    # Pós-processamento: Registar após resposta da IA
    print("[Chat] AI response received")

```

**Memória do Agente**

Conforme abordado na lição `Agentic Memory`, a memória é um elemento importante para permitir ao agente operar em diferentes contextos. O MAF oferece vários tipos de memória:

*Memória In-Memory*

Esta é a memória armazenada em threads durante a execução da aplicação.

```python
# Criar uma nova thread.
thread = agent.get_new_thread() # Execute o agente com a thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mensagens Persistentes*

Esta memória é usada para armazenar histórico de conversas entre diferentes sessões. É definida usando o `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Criar uma loja de mensagens personalizada
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memória Dinâmica*

Esta memória é adicionada ao contexto antes de os agentes serem executados. Estas memórias podem ser armazenadas em serviços externos como mem0:

```python
from agent_framework.mem0 import Mem0Provider

# A usar Mem0 para capacidades avançadas de memória
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

A observabilidade é importante para construir sistemas agénticos fiáveis e fáceis de manter. O MAF integra-se com OpenTelemetry para fornecer tracing e medidores para melhor observabilidade.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # fazer algo
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

O MAF oferece workflows que são passos pré-definidos para completar uma tarefa e incluem agentes de IA como componentes nesses passos.

Workflows são compostos por diferentes componentes que permitem um melhor fluxo de controlo. Workflows habilitam também **orquestração multi-agente** e **checkpointing** para salvar estados do workflow.

Os componentes principais de um workflow são:

**Executores**

Executores recebem mensagens de entrada, realizam as suas tarefas atribuídas e depois produzem uma mensagem de saída. Isto movimenta o workflow na direção da conclusão da tarefa maior. Executores podem ser agentes IA ou lógica personalizada.

**Edges**

Edges são usados para definir o fluxo de mensagens num workflow. Estes podem ser:

*Edges Diretos* - Ligações simples um-a-um entre executores:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Edges Condicionais* - Ativados quando uma condição é cumprida. Por exemplo, quando quartos de hotel não estão disponíveis, um executor pode sugerir outras opções.

*Edges switch-case* - Direcionam mensagens a diferentes executores baseados em condições definidas. Por exemplo, se o cliente de viagens tem acesso prioritário e as suas tarefas serão tratadas com outro workflow.

*Edges fan-out* - Enviam uma mensagem para múltiplos destinos.

*Edges fan-in* - Colecionam múltiplas mensagens de diferentes executores e enviam para um único destino.

**Eventos**

Para providenciar melhor observabilidade nos workflows, o MAF oferece eventos embutidos para execução incluindo:

- `WorkflowStartedEvent`  - Início da execução do workflow
- `WorkflowOutputEvent` - Workflow produz uma saída
- `WorkflowErrorEvent` - Workflow encontra um erro
- `ExecutorInvokeEvent`  - Executor inicia processamento
- `ExecutorCompleteEvent`  -  Executor termina processamento
- `RequestInfoEvent` - Um pedido é efectuado

## Padrões Avançados do MAF

As secções acima cobrem os conceitos chave do Microsoft Agent Framework. Ao construir agentes mais complexos, aqui estão alguns padrões avançados a considerar:

- **Composição de Middleware**: Encadear múltiplos manipuladores de middleware (registo, autenticação, limitação de taxa) usando middleware de função e chat para controlo fino sobre o comportamento do agente.
- **Checkpointing de Workflows**: Usar eventos de workflow e serialização para salvar e retomar processos de agentes de longa duração.
- **Seleção Dinâmica de Ferramentas**: Combinar RAG sobre descrições de ferramentas com o registo de ferramentas do MAF para apresentar apenas as ferramentas relevantes para cada consulta.
- **Passagem Multi-Agente**: Usar edges de workflow e encaminhamento condicional para orquestrar passagens entre agentes especializados.

## Hospedar Agentes LangChain / LangGraph no Microsoft Foundry

O Microsoft Agent Framework é **interoperável a nível de framework** — não está limitado a agentes escritos com o MAF. Se já tiver um agente construído com **LangChain** ou **LangGraph**, pode executá-lo como um **agente hospedado no Microsoft Foundry** para que o Foundry gere o runtime, sessões, escalabilidade, identidade e pontos finais de protocolo para si, enquanto a sua lógica de agente permanece no LangGraph.

Isto é feito com o pacote `langchain_azure_ai.agents.hosting`, que expõe um grafo LangGraph compilado pelos mesmos protocolos que os agentes hospedados pelo Foundry usam.

**1. Instale a extra hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

A extra `hosting` instala as bibliotecas de protocolo Foundry: `azure-ai-agentserver-responses` (o endpoint `/responses` compatível com OpenAI) e `azure-ai-agentserver-invocations` (o endpoint genérico `/invocations`).

**2. Escolha um protocolo de hosting:**

| Protocolo | Classe Host | Endpoint | Usar quando |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Quer um chat compatível com OpenAI, streaming, histórico de respostas e threading de conversação — o recomendado por defeito para agentes conversacionais. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Precisa de uma forma JSON customizada, um endpoint em estilo webhook, ou processamento não conversacional. |

Como a **API Responses é a API principal para desenvolvimento de agentes no Foundry**, comece com `ResponsesHostServer` para a maioria dos agentes.

**3. Configure variáveis de ambiente** (`az login` primeiro para que o `DefaultAzureCredential` possa autenticar):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Quando o agente correr mais tarde como um agente hospedado no Foundry, a plataforma injeta automaticamente `FOUNDRY_PROJECT_ENDPOINT`.

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

    # O ChatOpenAI aqui tem como alvo o endpoint compatível com OpenAI (Respostas) do projeto Foundry.
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

Execute localmente com `python main.py`, depois envie um pedido Responses para `http://localhost:8088/responses`.

**Comportamentos chave:**

- **Conversas**: Clientes continuam uma conversação passando `previous_response_id` ou um ID de `conversation`. Se o seu grafo estiver compilado com checkpoint LangGraph, Foundry associa o estado da conversa ao checkpoint (use checkpoint durável em produção; `MemorySaver` é adequado para testes locais).
- **Humano no ciclo**: Se o seu grafo usar `interrupt()` LangGraph, `ResponsesHostServer` apresenta a interrupção pendente como um item `function_call` / `mcp_approval_request` do Responses, e os clientes retomam com a correspondência `function_call_output` / `mcp_approval_response`.
- **Deploy no Foundry**: Use o Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, requer Docker), depois `azd provision` e `azd deploy`. O deployment de agente hospedado requer o papel **Foundry Project Manager**.

Uma versão executável deste exemplo encontra-se em [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Para o walkthrough completo (protocolo Invocations, esquemas customizados de pedido e resolução de problemas), veja [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Exemplos de Código 

Exemplos de código para Microsoft Agent Framework podem ser encontrados neste repositório nos ficheiros `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Tem Mais Perguntas Sobre o Microsoft Agent Framework?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar em horas de atendimento e esclarecer as suas dúvidas sobre Agentes de IA.
## Lição Anterior

[Memória para Agentes de IA](../13-agent-memory/README.md)

## Próxima Lição

[Construção de Agentes de Uso Informático (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->