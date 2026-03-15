# Explorando o Microsoft Agent Framework

![Agent Framework](../../../translated_images/pt-BR/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introdução

Esta lição abordará:

- Entendendo o Microsoft Agent Framework: Principais Características e Valor  
- Explorando os Conceitos-Chave do Microsoft Agent Framework
- Padrões Avançados do MAF: Fluxos de Trabalho, Middleware e Memória

## Objetivos de Aprendizagem

Após concluir esta lição, você saberá como:

- Construir Agentes de IA Prontos para Produção usando o Microsoft Agent Framework
- Aplicar os recursos principais do Microsoft Agent Framework aos seus Casos de Uso de Agentes
- Usar padrões avançados incluindo fluxos de trabalho, middleware e observabilidade

## Exemplos de Código

Exemplos de código para [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) podem ser encontrados neste repositório nos arquivos `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Entendendo o Microsoft Agent Framework

![Framework Intro](../../../translated_images/pt-BR/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) é a estrutura unificada da Microsoft para construir agentes de IA. Ele oferece a flexibilidade para atender a uma ampla variedade de casos de uso agenticos vistos em ambientes de produção e pesquisa, incluindo:

- **Orquestração Sequencial de Agentes** em cenários onde fluxos de trabalho passo a passo são necessários.
- **Orquestração Concorrente** em cenários onde agentes precisam completar tarefas ao mesmo tempo.
- **Orquestração de Chat em Grupo** em cenários onde agentes podem colaborar juntos em uma tarefa.
- **Orquestração de Transferência** em cenários onde agentes transferem a tarefa uns para os outros à medida que subtarefas são concluídas.
- **Orquestração Magnética** em cenários onde um agente gerente cria e modifica uma lista de tarefas e gerencia a coordenação dos subagentes para completar a tarefa.

Para entregar Agentes de IA em Produção, o MAF também inclui recursos para:

- **Observabilidade** por meio do uso do OpenTelemetry onde cada ação do Agente de IA, incluindo invocação de ferramentas, etapas de orquestração, fluxos de raciocínio e monitoramento de desempenho através de dashboards Microsoft Foundry.
- **Segurança** hospedando agentes nativamente no Microsoft Foundry que inclui controles de segurança como acesso baseado em papéis, manipulação de dados privados e segurança de conteúdo incorporada.
- **Durabilidade** pois os threads e fluxos de agentes podem pausar, retomar e recuperar de erros, o que permite processos de longa duração.
- **Controle** com suporte a fluxos com intervenção humana onde tarefas são marcadas como exigindo aprovação humana.

O Microsoft Agent Framework também é focado em ser interoperável por:

- **Ser Cloud-agnóstico** - Agentes podem rodar em containers, on-premises e em múltiplas nuvens diferentes.
- **Ser Provider-agnóstico** - Agentes podem ser criados através do seu SDK preferido incluindo Azure OpenAI e OpenAI.
- **Integrar Padrões Abertos** - Agentes podem utilizar protocolos como Agent-to-Agent (A2A) e Model Context Protocol (MCP) para descobrir e usar outros agentes e ferramentas.
- **Plugins e Conectores** - Conexões podem ser feitas para serviços de dados e memória como Microsoft Fabric, SharePoint, Pinecone e Qdrant.

Vamos ver como esses recursos são aplicados a alguns dos conceitos principais do Microsoft Agent Framework.

## Conceitos-Chave do Microsoft Agent Framework

### Agentes

![Agent Framework](../../../translated_images/pt-BR/agent-components.410a06daf87b4fef.webp)

**Criando Agentes**

A criação de agentes é feita definindo o serviço de inferência (Fornecedor de LLM), um conjunto de instruções para o Agente de IA seguir, e um `nome` atribuído:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

O exemplo acima usa `Azure OpenAI`, mas agentes podem ser criados utilizando uma variedade de serviços incluindo `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, APIs `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou agentes remotos usando o protocolo A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Executando Agentes**

Agentes são executados usando os métodos `.run` ou `.run_stream` para respostas não-streaming ou streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Cada execução de agente também pode ter opções para customizar parâmetros como `max_tokens` usados pelo agente, `tools` que o agente pode chamar, e até o próprio `model` usado pelo agente.

Isto é útil em casos onde modelos ou ferramentas específicas são necessários para completar a tarefa do usuário.

**Ferramentas**

Ferramentas podem ser definidas tanto na definição do agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Ao criar um ChatAgent diretamente

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

quanto na execução do agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Ferramenta fornecida apenas para esta execução )
```

**Threads de Agente**

Threads de agente são usados para manejar conversas de múltiplas interações. Threads podem ser criados por:

- Usar `get_new_thread()` que permite que o thread seja salvo ao longo do tempo
- Criar um thread automaticamente ao executar um agente, e o thread durar apenas durante a execução atual.

Para criar um thread, o código é assim:

```python
# Crie uma nova thread.
thread = agent.get_new_thread() # Execute o agente com a thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Você pode então serializar o thread para ser armazenado para uso posterior:

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

**Middleware de Agente**

Agentes interagem com ferramentas e LLMs para completar tarefas dos usuários. Em certos cenários, queremos executar ou rastrear entre essas interações. Middleware de agente nos permite isso através de:

*Middleware de Função*

Este middleware permite executar uma ação entre o agente e uma função/ferramenta que ele irá chamar. Um exemplo de uso seria para fazer logging da chamada da função.

No código abaixo, `next` define se o próximo middleware ou a própria função deve ser chamado.

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

    # Pós-processamento: Registrar após a execução da função
    print(f"[Function] {context.function.name} completed")
```

*Middleware de Chat*

Este middleware permite executar ou registrar uma ação entre o agente e as requisições entre o LLM.

Isto contém informações importantes como as `messages` que estão sendo enviadas ao serviço de IA.

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

**Memória de Agente**

Como abordado na lição `Agentic Memory`, memória é um elemento importante para permitir que o agente opere sobre diferentes contextos. O MAF oferece vários tipos diferentes de memórias:

*Armazenamento em Memória*

Esta é a memória armazenada em threads durante a execução da aplicação.

```python
# Criar uma nova thread.
thread = agent.get_new_thread() # Executar o agente com a thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mensagens Persistentes*

Esta memória é usada ao armazenar o histórico de conversas entre diferentes sessões. É definida usando o `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Criar um armazenamento personalizado de mensagens
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memória Dinâmica*

Esta memória é adicionada ao contexto antes dos agentes serem executados. Estas memórias podem ser armazenadas em serviços externos como mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Usando Mem0 para capacidades avançadas de memória
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

**Observabilidade de Agente**

Observabilidade é importante para construir sistemas agenticos confiáveis e manuteníveis. O MAF integra-se com OpenTelemetry para fornecer rastreamento e métricas para melhor observabilidade.

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

O MAF oferece fluxos de trabalho que são passos pré-definidos para completar uma tarefa e incluem agentes de IA como componentes nesses passos.

Fluxos de trabalho são compostos por diferentes componentes que permitem melhor controle do fluxo. Fluxos de trabalho também permitem **orquestração multi-agente** e **checkpointing** para salvar estados do fluxo.

Os componentes principais de um fluxo de trabalho são:

**Executores**

Executores recebem mensagens de entrada, realizam as tarefas designadas, e então produzem uma mensagem de saída. Isso move o fluxo para a frente na direção de completar a tarefa maior. Executores podem ser tanto agentes de IA quanto lógica customizada.

**Arestas**

Arestas são usadas para definir o fluxo de mensagens em um fluxo de trabalho. Elas podem ser:

*Arestas Diretas* - Conexões simples um para um entre executores:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Arestas Condicionais* - Ativadas após certa condição ser atendida. Por exemplo, quando quartos de hotel estão indisponíveis, um executor pode sugerir outras opções.

*Arestas Switch-case* - Roteiam mensagens para diferentes executores baseados em condições definidas. Por exemplo, se um cliente de viagem tem acesso prioritário e suas tarefas serão tratadas por outro fluxo.

*Arestas Fan-out* - Enviam uma mensagem para múltiplos destinos.

*Arestas Fan-in* - Coletam múltiplas mensagens de diferentes executores e enviam para um destino único.

**Eventos**

Para fornecer melhor observabilidade nos fluxos, o MAF oferece eventos embutidos para execução, incluindo:

- `WorkflowStartedEvent`  - Início da execução do fluxo
- `WorkflowOutputEvent` - Fluxo produz uma saída
- `WorkflowErrorEvent` - Fluxo encontra um erro
- `ExecutorInvokeEvent`  - Executor inicia processamento
- `ExecutorCompleteEvent`  -  Executor finaliza processamento
- `RequestInfoEvent` - Uma requisição foi emitida

## Padrões Avançados do MAF

As seções acima cobrem os conceitos-chave do Microsoft Agent Framework. À medida que você constrói agentes mais complexos, aqui estão alguns padrões avançados para considerar:

- **Composição de Middleware**: Encadeie múltiplos handlers de middleware (logging, autenticação, limitação de taxa) usando middleware de função e chat para controle detalhado sobre o comportamento do agente.
- **Checkpointing de Fluxo de Trabalho**: Use eventos de fluxo de trabalho e serialização para salvar e retomar processos longos de agentes.
- **Seleção Dinâmica de Ferramentas**: Combine RAG sobre descrições de ferramentas com registro de ferramentas do MAF para apresentar apenas ferramentas relevantes por consulta.
- **Transferência Multi-Agente**: Use arestas de fluxo de trabalho e roteamento condicional para orquestrar transferências entre agentes especializados.

## Exemplos de Código

Exemplos de código para o Microsoft Agent Framework podem ser encontrados neste repositório nos arquivos `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Tem Mais Perguntas Sobre Microsoft Agent Framework?

Participe do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conhecer outros aprendizes, participar de horas de atendimento e esclarecer suas dúvidas sobre Agentes de IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->