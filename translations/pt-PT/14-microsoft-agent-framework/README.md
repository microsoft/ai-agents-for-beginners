# Explorando o Microsoft Agent Framework

![Framework de Agentes](../../../translated_images/pt-PT/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introdução

Esta lição irá abordar:

- Compreender o Microsoft Agent Framework: Principais Funcionalidades e Valor  
- Explorar os Conceitos Principais do Microsoft Agent Framework
- Padrões Avançados do MAF: Fluxos de Trabalho, Middleware e Memória

## Objetivos de Aprendizagem

Após completar esta lição, saberá como:

- Construir Agentes de IA Prontos para Produção usando o Microsoft Agent Framework
- Aplicar as funcionalidades centrais do Microsoft Agent Framework aos seus casos de uso agentes
- Utilizar padrões avançados incluindo fluxos de trabalho, middleware e observabilidade

## Exemplos de Código 

Os exemplos de código para [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) podem ser encontrados neste repositório nas pastas `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Compreender o Microsoft Agent Framework

![Introdução ao Framework](../../../translated_images/pt-PT/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) é o framework unificado da Microsoft para construir agentes de IA. Oferece a flexibilidade para abordar a grande variedade de casos de uso agenticos observados tanto em produção como em ambientes de investigação, incluindo:

- **Orquestração sequencial de agentes** em cenários onde são necessários fluxos de trabalho passo a passo.
- **Orquestração concorrente** em cenários onde os agentes precisam completar tarefas ao mesmo tempo.
- **Orquestração em chat de grupo** em cenários onde agentes podem colaborar entre si numa única tarefa.
- **Orquestração de passagem de tarefa (Handoff)** em cenários onde os agentes transferem a tarefa entre si à medida que os subtarefas são concluídos.
- **Orquestração magnética** em cenários onde um agente gestor cria e modifica uma lista de tarefas e gere a coordenação de subagentes para completar a tarefa.

Para fornecer Agentes de IA em Produção, o MAF também inclui funcionalidades para:

- **Observabilidade** através do uso do OpenTelemetry, onde cada ação do Agente de IA, incluindo invocação de ferramentas, passos de orquestração, fluxos de raciocínio e monitorização de desempenho, é visível através dos dashboards do Microsoft Foundry.
- **Segurança** ao hospedar agentes nativamente no Microsoft Foundry, que inclui controlos de segurança como acesso baseado em funções, tratamento de dados privados e segurança de conteúdo integrada.
- **Durabilidade** uma vez que os threads de agente e fluxos de trabalho podem pausar, retomar e recuperar de erros, o que permite processos de maior duração.
- **Controlo** pois são suportados fluxos de trabalho com intervenção humana, onde tarefas são marcadas como necessitando aprovação humana.

O Microsoft Agent Framework também se foca em ser interoperável através de:

- **Ser agnóstico quanto à cloud** - Os agentes podem correr em containers, on-prem e através de múltiplas clouds diferentes.
- **Ser agnóstico quanto ao fornecedor** - Os agentes podem ser criados através do seu SDK preferido incluindo Azure OpenAI e OpenAI
- **Integrar padrões abertos** - Os agentes podem utilizar protocolos como Agent-to-Agent(A2A) e Model Context Protocol (MCP) para descobrir e usar outros agentes e ferramentas.
- **Plugins e Conectores** - Podem ser estabelecidas ligações a serviços de dados e memória como Microsoft Fabric, SharePoint, Pinecone e Qdrant.

Vamos ver como estas funcionalidades são aplicadas a alguns dos conceitos centrais do Microsoft Agent Framework.

## Conceitos Principais do Microsoft Agent Framework

### Agentes

![Componentes do Agente](../../../translated_images/pt-PT/agent-components.410a06daf87b4fef.webp)

**Criar Agentes**

A criação de agentes é feita definindo o serviço de inferência (Fornecedor LLM), um conjunto de instruções para o Agente de IA seguir, e um `name` atribuído:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

O acima está a usar `Azure OpenAI` mas os agentes podem ser criados usando uma variedade de serviços incluindo `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

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

**Executar Agentes**

Os agentes são executados utilizando os métodos `.run` ou `.run_stream` para respostas não-streaming ou em streaming, respetivamente.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Cada execução do agente também pode ter opções para personalizar parâmetros tais como `max_tokens` usados pelo agente, `tools` que o agente pode invocar, e  até mesmo o próprio `model` utilizado pelo agente.

Isto é útil em casos onde modelos ou ferramentas específicas são necessárias para completar a tarefa de um utilizador.

**Ferramentas**

As ferramentas podem ser definidas tanto ao definir o agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Ao criar um ChatAgent diretamente

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

como também ao executar o agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Ferramenta fornecida apenas para esta execução )
```

**Threads de Agente**

As threads de agente são usadas para tratar de conversas multi-turno. As threads podem ser criadas por:

- Usar `get_new_thread()` que permite que a thread seja guardada ao longo do tempo
- Criar uma thread automaticamente ao executar um agente e ter a thread apenas durante a execução atual.

Para criar uma thread, o código é o seguinte:

```python
# Criar uma nova thread.
thread = agent.get_new_thread() # Executar o agente com a thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Pode então serializar a thread para ser armazenada para uso posterior:

```python
# Criar um novo fio de execução.
thread = agent.get_new_thread() 

# Executar o agente com o fio de execução.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializar o fio de execução para armazenamento.

serialized_thread = await thread.serialize() 

# Desserializar o estado do fio de execução após o carregamento a partir do armazenamento.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware de Agente**

Os agentes interagem com ferramentas e LLMs para completar as tarefas dos utilizadores. Em certos cenários, queremos executar ou acompanhar ações entre estas interações. O middleware de agente permite-nos fazê-lo através de:

*Middleware de Função*

Este middleware permite-nos executar uma ação entre o agente e uma função/ferramenta que ele irá chamar. Um exemplo de quando isto seria usado é quando se pretende fazer algum registo sobre a chamada da função.

No código abaixo `next` define se o middleware seguinte ou a função real deve ser chamada.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pré-processamento: Registar antes da execução da função
    print(f"[Function] Calling {context.function.name}")

    # Continuar para o próximo middleware ou para a execução da função
    await next(context)

    # Pós-processamento: Registar após a execução da função
    print(f"[Function] {context.function.name} completed")
```

*Middleware de Chat*

Este middleware permite-nos executar ou registar uma ação entre o agente e os pedidos para o LLM .

Isto contém informação importante como as `messages` que estão a ser enviadas para o serviço de IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pré-processamento: Registo antes da chamada à IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuar para o middleware seguinte ou serviço de IA
    await next(context)

    # Pós-processamento: Registo após a resposta da IA
    print("[Chat] AI response received")

```

**Memória do Agente**

Como abordado na lição `Agentic Memory`, a memória é um elemento importante para permitir que o agente opere sobre diferentes contextos. O MAF oferece vários tipos diferentes de memórias:

*Armazenamento em Memória*

Esta é a memória armazenada nas threads durante o tempo de execução da aplicação.

```python
# Criar uma nova thread.
thread = agent.get_new_thread() # Executar o agente com a thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mensagens Persistentes*

Esta memória é usada ao guardar o historial de conversas entre diferentes sessões. É definida usando o `chat_message_store_factory` :

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

Esta memória é adicionada ao contexto antes dos agentes serem executados. Estas memórias podem ser armazenadas em serviços externos como mem0:

```python
from agent_framework.mem0 import Mem0Provider

# A usar o Mem0 para capacidades de memória avançadas
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

A observabilidade é importante para construir sistemas agenticos fiáveis e fáceis de manter. O MAF integra-se com o OpenTelemetry para fornecer traços e métricas para melhor observabilidade.

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

Os fluxos de trabalho são compostos por diferentes componentes que permitem um melhor controlo do fluxo. Os fluxos de trabalho também permitem **orquestração multi-agente** e **gravação de pontos de verificação** para guardar estados do fluxo de trabalho.

Os componentes centrais de um fluxo de trabalho são:

**Executores**

Os executores recebem mensagens de entrada, executam as suas tarefas atribuídas e depois produzem uma mensagem de saída. Isto move o fluxo de trabalho em direção à conclusão da tarefa maior. Os executores podem ser um agente de IA ou lógica personalizada.

**Arestas**

As arestas são usadas para definir o fluxo de mensagens num fluxo de trabalho. Estas podem ser:

*Arestas Diretas* - Conexões simples um-para-um entre executores:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Arestas Condicionais* - Ativadas depois de uma determinada condição ser satisfeita. Por exemplo, quando quartos de hotel não estão disponíveis, um executor pode sugerir outras opções.

*Arestas switch-case* - Roteiam mensagens para diferentes executores com base em condições definidas. Por exemplo, se um cliente de viagens tiver acesso prioritário, as suas tarefas serão tratadas através de outro fluxo de trabalho.

*Arestas Fan-out* - Enviar uma mensagem para múltiplos destinos.

*Arestas Fan-in* - Reunir várias mensagens de diferentes executores e enviar para um único destino.

**Eventos**

Para proporcionar melhor observabilidade nos fluxos de trabalho, o MAF oferece eventos embutidos para a execução, incluindo:

- `WorkflowStartedEvent`  - A execução do fluxo de trabalho começa
- `WorkflowOutputEvent` - O fluxo de trabalho produz uma saída
- `WorkflowErrorEvent` - O fluxo de trabalho encontra um erro
- `ExecutorInvokeEvent`  - O executor começa a processar
- `ExecutorCompleteEvent`  -  O executor termina o processamento
- `RequestInfoEvent` - É emitida uma pedido

## Padrões Avançados do MAF

As secções acima cobrem os conceitos-chave do Microsoft Agent Framework. À medida que constrói agentes mais complexos, aqui estão alguns padrões avançados a considerar:

- **Composição de Middleware**: Encadear múltiplos manipuladores de middleware (registo, autenticação, limitação de taxa) usando middleware de função e de chat para um controlo refinado sobre o comportamento do agente.
- **Pontos de Verificação em Fluxos de Trabalho**: Usar eventos de fluxo de trabalho e serialização para guardar e retomar processos de agente de longa duração.
- **Seleção Dinâmica de Ferramentas**: Combinar RAG sobre descrições de ferramentas com o registo de ferramentas do MAF para apresentar apenas as ferramentas relevantes por consulta.
- **Passagem de Tarefa entre Múltiplos Agentes**: Usar arestas de fluxo de trabalho e encaminhamento condicional para orquestrar a passagem de tarefas entre agentes especializados.

## Exemplos de Código 

Os exemplos de código para Microsoft Agent Framework podem ser encontrados neste repositório nas pastas `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Tem mais perguntas sobre o Microsoft Agent Framework?

Junte-se ao [Discord do Microsoft Foundry](https://aka.ms/ai-agents/discord) para conhecer outros aprendizes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Isenção de responsabilidade**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, tenha em atenção que traduções automatizadas podem conter erros ou imprecisões. O documento original no seu idioma de origem deve ser considerado a fonte autorizada. Para informação crítica, recomenda-se a tradução por um tradutor profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->