# Explorando o Microsoft Agent Framework

![Agent Framework](../../../translated_images/pt-PT/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introdução

Esta lição irá abordar:

- Compreender o Microsoft Agent Framework: Características principais e valor  
- Explorar os conceitos chave do Microsoft Agent Framework
- Padrões avançados do MAF: Fluxos de trabalho, Middleware e Memória

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como:

- Construir Agentes de IA prontos para produção usando o Microsoft Agent Framework
- Aplicar as funcionalidades principais do Microsoft Agent Framework aos seus casos de uso agenticos
- Usar padrões avançados incluindo fluxos de trabalho, middleware e observabilidade

## Exemplos de Código 

Exemplos de código para [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) podem ser encontrados neste repositório nos ficheiros `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Compreender o Microsoft Agent Framework

![Framework Intro](../../../translated_images/pt-PT/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) é o framework unificado da Microsoft para construir agentes de IA. Oferece a flexibilidade para abordar a grande variedade de casos de uso agenticos vistos tanto em produção como em ambientes de investigação, incluindo:

- **Orquestração sequencial de agentes** em cenários onde são necessários fluxos de trabalho passo a passo.
- **Orquestração concorrente** em cenários onde os agentes precisam completar tarefas ao mesmo tempo.
- **Orquestração de chat de grupo** em cenários onde agentes podem colaborar juntos numa tarefa.
- **Orquestração de transmissão** em cenários onde agentes passam a tarefa uns aos outros à medida que as subtarefas são concluídas.
- **Orquestração magnética** em cenários onde um agente gestor cria e modifica uma lista de tarefas e gere a coordenação dos subagentes para completar a tarefa.

Para entregar Agentes de IA em Produção, o MAF também inclui funcionalidades para:

- **Observabilidade** através do uso do OpenTelemetry onde cada ação do Agente de IA incluindo invocação de ferramentas, passos de orquestração, fluxos de raciocínio e monitorização de performance são acompanhados através de dashboards Microsoft Foundry.
- **Segurança** por hospedar agentes nativamente no Microsoft Foundry que inclui controlos de segurança como acesso baseado em funções, manuseamento de dados privados e segurança incorporada de conteúdo.
- **Durabilidade** pois os threads e fluxos de trabalho do agente podem pausar, retomar e recuperar de erros, o que permite processos de duração mais longa.
- **Controlo** pois os fluxos humanos no loop são suportados onde as tarefas podem ser marcadas como a exigir aprovação humana.

O Microsoft Agent Framework também foca-se em ser interoperável por:

- **Ser agnóstico em relação à Cloud** - Os agentes podem correr em contentores, no local e em múltiplas clouds diferentes.
- **Ser agnóstico em relação a fornecedores** - Agentes podem ser criados com o seu SDK preferido incluindo Azure OpenAI e OpenAI
- **Integrar padrões abertos** - Agentes podem utilizar protocolos como Agent-to-Agent (A2A) e Model Context Protocol (MCP) para descobrir e usar outros agentes e ferramentas.
- **Plugins e Conectores** - Podem ser feitas ligações a serviços de dados e memória tais como Microsoft Fabric, SharePoint, Pinecone e Qdrant.

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

O acima está a utilizar `Azure OpenAI` mas agentes podem ser criados usando uma variedade de serviços incluindo `Microsoft Foundry Agent Service`:

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

ou [MiniMax](https://platform.minimaxi.com/), que oferece uma API compatível com OpenAI com grandes janelas de contexto (até 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou agentes remotos usando o protocolo A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Executar Agentes**

Os agentes são executados usando os métodos `.run` ou `.run_stream` para respostas não-streaming ou streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Cada execução de agente pode também ter opções para personalizar parâmetros como `max_tokens` usado pelo agente, `tools` que o agente consegue chamar, e até o próprio `model` usado para o agente.

Isto é útil em casos onde modelos ou ferramentas específicas são necessárias para completar a tarefa do utilizador.

**Ferramentas**

As ferramentas podem ser definidas tanto quando se define o agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Ao criar um ChatAgent diretamente

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

e também ao executar o agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Ferramenta fornecida apenas para esta execução )
```

**Threads do Agente**

Threads do Agente são usados para gerir conversas multi-turno. Threads podem ser criados por:

- Usar `get_new_thread()` que permite que o thread seja guardado ao longo do tempo
- Criar um thread automaticamente quando se executa um agente e só mantendo o thread durante a execução atual.

Para criar um thread, o código é este:

```python
# Criar uma nova thread.
thread = agent.get_new_thread() # Executar o agente com a thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Pode depois serializar o thread para ser armazenado para uso posterior:

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

Agentes interagem com ferramentas e LLMs para completar as tarefas dos utilizadores. Em certos cenários, queremos executar ou registar entre essas interações. Middleware de agente permite fazer isto através de:

*Middleware de Função*

Este middleware permite executar uma ação entre o agente e uma função/ferramenta que ele vai chamar. Um exemplo de quando isto seria usado é se quiser fazer algum registo na chamada da função.

No código abaixo `next` define se o próximo middleware ou a função real deve ser chamado.

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

Este middleware permite executar ou registar uma ação entre o agente e os pedidos entre o LLM.

Este contém informação importante como as `messages` que estão a ser enviadas para o serviço de IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pré-processamento: Registar antes da chamada à IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuar para o middleware seguinte ou serviço de IA
    await next(context)

    # Pós-processamento: Registar após a resposta da IA
    print("[Chat] AI response received")

```

**Memória do Agente**

Como foi abordado na lição `Memória Agentica`, a memória é um elemento importante para permitir que o agente opere sobre diferentes contextos. O MAF oferece vários tipos diferentes de memórias:

*Armazenamento em Memória*

Esta é a memória armazenada em threads durante o tempo de execução da aplicação.

```python
# Criar uma nova thread.
thread = agent.get_new_thread() # Executar o agente com a thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mensagens Persistentes*

Esta memória é usada ao armazenar histórico de conversação em diferentes sessões. É definida usando a `chat_message_store_factory` :

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

Esta memória é adicionada ao contexto antes dos agentes serem executados. Estas memórias podem ser armazenadas em serviços externos como o mem0:

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

A observabilidade é importante para construir sistemas agenticos confiáveis e fáceis de manter. O MAF integra-se com o OpenTelemetry para fornecer tracing e medidores para melhor observabilidade.

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

### Fluxos de Trabalho

O MAF oferece fluxos de trabalho que são passos pré-definidos para completar uma tarefa e incluem agentes de IA como componentes desses passos.

Os fluxos de trabalho são compostos por diferentes componentes que permitem melhor controlo do fluxo. Fluxos de trabalho também permitem **orquestração multi-agente** e **checkpointing** para salvar os estados do fluxo de trabalho.

Os componentes principais de um fluxo de trabalho são:

**Executores**

Os executores recebem mensagens de entrada, realizam as suas tarefas atribuídas e depois produzem uma mensagem de saída. Isto move o fluxo de trabalho em direção ao cumprimento da tarefa maior. Os executores podem ser um agente de IA ou lógica personalizada.

**Arestas**

As arestas são usadas para definir o fluxo de mensagens num fluxo de trabalho. Estas podem ser:

*Arestas Diretas* - Ligações simples um-para-um entre executores:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Arestas Condicionais* - Ativadas após certa condição ser satisfeita. Por exemplo, quando quartos de hotel estão indisponíveis, um executor pode sugerir outras opções.

*Arestas Switch-case* - Roteia mensagens para diferentes executores baseando-se em condições definidas. Por exemplo, se um cliente de viagens tem acesso prioritário e as suas tarefas serão tratadas através de outro fluxo de trabalho.

*Arestas Fan-out* - Envia uma mensagem para múltiplos destinos.

*Arestas Fan-in* - Recolhe múltiplas mensagens de diferentes executores e envia para um único destino.

**Eventos**

Para proporcionar melhor observabilidade dos fluxos de trabalho, o MAF oferece eventos incorporados para a execução incluindo:

- `WorkflowStartedEvent`  - A execução do fluxo de trabalho começa
- `WorkflowOutputEvent` - O fluxo de trabalho produz uma saída
- `WorkflowErrorEvent` - O fluxo de trabalho encontra um erro
- `ExecutorInvokeEvent`  - Executor inicia o processamento
- `ExecutorCompleteEvent`  -  Executor termina o processamento
- `RequestInfoEvent` - Um pedido é emitido

## Padrões Avançados do MAF

As secções acima cobrem os conceitos chave do Microsoft Agent Framework. À medida que constrói agentes mais complexos, aqui estão alguns padrões avançados a considerar:

- **Composição de Middleware**: Encadear múltiplos manipuladores middleware (registos, autenticação, limitação de taxa) usando middleware de função e chat para controlo fino do comportamento do agente.
- **Checkpointing de Fluxos de Trabalho**: Usar eventos de fluxo de trabalho e serialização para salvar e retomar processos longos de agentes.
- **Seleção Dinâmica de Ferramentas**: Combinar RAG sobre descrições de ferramentas com o registo de ferramentas do MAF para apresentar apenas as ferramentas relevantes por consulta.
- **Transmissão Multi-Agente**: Usar arestas de fluxo de trabalho e roteamento condicional para orquestrar transmissões entre agentes especializados.

## Hospedagem de Agentes LangChain / LangGraph no Microsoft Foundry

O Microsoft Agent Framework é **interoperável entre frameworks** — não está limitado a agentes escritos com MAF. Se já tem um agente construído com **LangChain** ou **LangGraph**, pode executá-lo como um **agente hospedado no Microsoft Foundry**, para que o Foundry gere o ambiente de execução, sessões, escalamento, identidade e endpoints de protocolo para si, enquanto a sua lógica de agente permanece no LangGraph.

Isto é feito com o pacote `langchain_azure_ai.agents.hosting`, que expõe um grafo LangGraph compilado sobre os mesmos protocolos usados pelos agentes hospedados no Foundry.

**1. Instale a extensão hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

A extensão `hosting` instala as bibliotecas de protocolo Foundry: `azure-ai-agentserver-responses` (o endpoint compatível OpenAI `/responses`) e `azure-ai-agentserver-invocations` (o endpoint genérico `/invocations`).

**2. Escolha um protocolo de hospedagem:**

| Protocolo | Classe Host | Endpoint | Use quando |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Quer chat compatível OpenAI, streaming, histórico de respostas, e threading de conversação — o recomendado para agentes conversacionais. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Precisa de uma forma JSON customizada, um endpoint estilo webhook, ou processamento não-conversacional. |

Porque **a API Responses é a API principal para desenvolvimento de agentes no Foundry**, comece com `ResponsesHostServer` para a maioria dos agentes.

**3. Configure variáveis de ambiente** (`az login` primeiro para que `DefaultAzureCredential` possa autenticar):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Quando o agente correr mais tarde como agente hospedado no Foundry, a plataforma injeta `FOUNDRY_PROJECT_ENDPOINT` automaticamente.

**4. Exponha um agente LangGraph sobre o protocolo Responses:**

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

    # O ChatOpenAI aqui destina-se ao endpoint compatível com OpenAI (Responses) do projeto Foundry.
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

- **Conversas**: Clientes dão continuidade a uma conversa passando `previous_response_id` ou um ID de `conversation`. Se o seu grafo for compilado com um verificador LangGraph, o Foundry associa o estado da conversação ao checkpoint (use um checkpoint durável em produção; `MemorySaver` é adequado para testes locais).
- **Humano no loop**: Se o seu grafo usa `interrupt()` do LangGraph, `ResponsesHostServer` exponencia o interrompimento pendente como um item Responses `function_call` / `mcp_approval_request`, e os clientes retomam com um `function_call_output` / `mcp_approval_response` correspondente.
- **Desploy no Foundry**: Use a Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, requer Docker), depois `azd provision` e `azd deploy`. O deployment de agente hospedado requer o papel **Foundry Project Manager**.

Uma versão executável deste exemplo encontra-se em [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Para o walkthrough completo (protocolo Invocations, esquemas de pedido customizados, e resolução de problemas), consulte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Exemplos de Código 

Exemplos de código para Microsoft Agent Framework podem ser encontrados neste repositório nos ficheiros `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Tem Mais Perguntas Sobre o Microsoft Agent Framework?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conhecer outros aprendizes, participar das horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.
## Lição Anterior

[Memória para Agentes de IA](../13-agent-memory/README.md)

## Próxima Lição

[Construindo Agentes de Uso de Computador (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->