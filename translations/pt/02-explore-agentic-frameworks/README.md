<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T12:09:43+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "pt"
}
-->
[![Explorar Frameworks de Agentes de IA](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.pt.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Explorar Frameworks de Agentes de IA

Os frameworks de agentes de IA são plataformas de software projetadas para simplificar a criação, implementação e gestão de agentes de IA. Estes frameworks fornecem aos desenvolvedores componentes pré-construídos, abstrações e ferramentas que agilizam o desenvolvimento de sistemas de IA complexos.

Estes frameworks ajudam os desenvolvedores a focar nos aspectos únicos de suas aplicações, oferecendo abordagens padronizadas para desafios comuns no desenvolvimento de agentes de IA. Eles melhoram a escalabilidade, acessibilidade e eficiência na construção de sistemas de IA.

## Introdução 

Esta lição abordará:

- O que são frameworks de agentes de IA e o que permitem que os desenvolvedores alcancem?
- Como as equipas podem utilizá-los para criar protótipos rapidamente, iterar e melhorar as capacidades dos seus agentes?
- Quais são as diferenças entre os frameworks e ferramentas criados pela Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> e <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Posso integrar diretamente as ferramentas existentes do ecossistema Azure ou preciso de soluções independentes?
- O que é o serviço Azure AI Agents e como isso me ajuda?

## Objetivos de aprendizagem

Os objetivos desta lição são ajudá-lo a compreender:

- O papel dos frameworks de agentes de IA no desenvolvimento de IA.
- Como aproveitar os frameworks de agentes de IA para construir agentes inteligentes.
- Capacidades principais habilitadas pelos frameworks de agentes de IA.
- As diferenças entre AutoGen, Semantic Kernel e Azure AI Agent Service.

## O que são frameworks de agentes de IA e o que permitem que os desenvolvedores façam?

Os frameworks tradicionais de IA podem ajudar a integrar IA nas suas aplicações e melhorar estas aplicações das seguintes formas:

- **Personalização**: A IA pode analisar o comportamento e as preferências do utilizador para fornecer recomendações, conteúdos e experiências personalizadas.  
Exemplo: Serviços de streaming como Netflix utilizam IA para sugerir filmes e séries com base no histórico de visualização, aumentando o envolvimento e a satisfação do utilizador.
- **Automação e Eficiência**: A IA pode automatizar tarefas repetitivas, simplificar fluxos de trabalho e melhorar a eficiência operacional.  
Exemplo: Aplicações de atendimento ao cliente utilizam chatbots com IA para lidar com perguntas comuns, reduzindo os tempos de resposta e liberando agentes humanos para questões mais complexas.
- **Melhoria da Experiência do Utilizador**: A IA pode melhorar a experiência geral do utilizador ao fornecer funcionalidades inteligentes, como reconhecimento de voz, processamento de linguagem natural e texto preditivo.  
Exemplo: Assistentes virtuais como Siri e Google Assistant utilizam IA para entender e responder a comandos de voz, facilitando a interação dos utilizadores com os seus dispositivos.

### Isso tudo parece ótimo, certo? Então por que precisamos de frameworks de agentes de IA?

Os frameworks de agentes de IA representam algo mais do que apenas frameworks de IA. Eles são projetados para permitir a criação de agentes inteligentes que podem interagir com utilizadores, outros agentes e o ambiente para alcançar objetivos específicos. Estes agentes podem exibir comportamento autónomo, tomar decisões e adaptar-se a condições em mudança. Vamos analisar algumas capacidades principais habilitadas pelos frameworks de agentes de IA:

- **Colaboração e Coordenação entre Agentes**: Permitem a criação de múltiplos agentes de IA que podem trabalhar juntos, comunicar e coordenar para resolver tarefas complexas.
- **Automação e Gestão de Tarefas**: Fornecem mecanismos para automatizar fluxos de trabalho de múltiplas etapas, delegação de tarefas e gestão dinâmica de tarefas entre agentes.
- **Compreensão Contextual e Adaptação**: Equipam os agentes com a capacidade de entender o contexto, adaptar-se a ambientes em mudança e tomar decisões com base em informações em tempo real.

Resumindo, os agentes permitem fazer mais, levar a automação ao próximo nível e criar sistemas mais inteligentes que podem adaptar-se e aprender com o ambiente.

## Como criar protótipos rapidamente, iterar e melhorar as capacidades do agente?

Este é um cenário em rápida evolução, mas há algumas coisas comuns na maioria dos frameworks de agentes de IA que podem ajudar a criar protótipos e iterar rapidamente, nomeadamente componentes modulares, ferramentas colaborativas e aprendizagem em tempo real. Vamos explorar estes pontos:

- **Utilizar Componentes Modulares**: SDKs de IA oferecem componentes pré-construídos, como conectores de IA e memória, chamadas de função usando linguagem natural ou plugins de código, modelos de prompts e mais.
- **Aproveitar Ferramentas Colaborativas**: Projetar agentes com papéis e tarefas específicas, permitindo testar e refinar fluxos de trabalho colaborativos.
- **Aprender em Tempo Real**: Implementar ciclos de feedback onde os agentes aprendem com interações e ajustam o seu comportamento dinamicamente.

### Utilizar Componentes Modulares

SDKs como Microsoft Semantic Kernel e LangChain oferecem componentes pré-construídos, como conectores de IA, modelos de prompts e gestão de memória.

**Como as equipas podem utilizá-los**: As equipas podem montar rapidamente estes componentes para criar um protótipo funcional sem começar do zero, permitindo experimentação e iteração rápidas.

**Como funciona na prática**: Pode utilizar um parser pré-construído para extrair informações da entrada do utilizador, um módulo de memória para armazenar e recuperar dados, e um gerador de prompts para interagir com os utilizadores, tudo sem precisar construir estes componentes do zero.

**Exemplo de código**. Vamos ver exemplos de como pode usar um conector de IA pré-construído com Semantic Kernel Python e .Net que utiliza chamadas automáticas de função para que o modelo responda à entrada do utilizador:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```
  
O que pode ver neste exemplo é como pode aproveitar um parser pré-construído para extrair informações-chave da entrada do utilizador, como origem, destino e data de um pedido de reserva de voo. Esta abordagem modular permite focar na lógica de alto nível.

### Aproveitar Ferramentas Colaborativas

Frameworks como CrewAI, Microsoft AutoGen e Semantic Kernel facilitam a criação de múltiplos agentes que podem trabalhar juntos.

**Como as equipas podem utilizá-los**: As equipas podem projetar agentes com papéis e tarefas específicas, permitindo testar e refinar fluxos de trabalho colaborativos e melhorar a eficiência geral do sistema.

**Como funciona na prática**: Pode criar uma equipa de agentes onde cada agente tem uma função especializada, como recuperação de dados, análise ou tomada de decisão. Estes agentes podem comunicar e compartilhar informações para alcançar um objetivo comum, como responder a uma consulta do utilizador ou completar uma tarefa.

**Exemplo de código (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```
  
O que vê no código anterior é como pode criar uma tarefa que envolve múltiplos agentes trabalhando juntos para analisar dados. Cada agente desempenha uma função específica, e a tarefa é executada coordenando os agentes para alcançar o resultado desejado. Ao criar agentes dedicados com papéis especializados, pode melhorar a eficiência e o desempenho da tarefa.

### Aprender em Tempo Real

Frameworks avançados fornecem capacidades para compreensão de contexto e adaptação em tempo real.

**Como as equipas podem utilizá-los**: As equipas podem implementar ciclos de feedback onde os agentes aprendem com interações e ajustam o seu comportamento dinamicamente, levando a melhorias contínuas e refinamento de capacidades.

**Como funciona na prática**: Os agentes podem analisar feedback dos utilizadores, dados ambientais e resultados de tarefas para atualizar a sua base de conhecimento, ajustar algoritmos de tomada de decisão e melhorar o desempenho ao longo do tempo. Este processo de aprendizagem iterativa permite que os agentes se adaptem a condições e preferências dos utilizadores em mudança, melhorando a eficácia geral do sistema.

## Quais são as diferenças entre os frameworks AutoGen, Semantic Kernel e Azure AI Agent Service?

Existem várias formas de comparar estes frameworks, mas vamos analisar algumas diferenças principais em termos de design, capacidades e casos de uso alvo:

## AutoGen

AutoGen é um framework de código aberto desenvolvido pelo AI Frontiers Lab da Microsoft Research. Ele foca em aplicações *agentes* distribuídas e orientadas por eventos, permitindo múltiplos LLMs e SLMs, ferramentas e padrões avançados de design multi-agente.

AutoGen é construído em torno do conceito central de agentes, que são entidades autónomas capazes de perceber o seu ambiente, tomar decisões e realizar ações para alcançar objetivos específicos. Os agentes comunicam-se através de mensagens assíncronas, permitindo que trabalhem de forma independente e em paralelo, melhorando a escalabilidade e a capacidade de resposta do sistema.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Os agentes são baseados no modelo de ator</a>. Segundo a Wikipedia, um ator é _o bloco básico de computação concorrente. Em resposta a uma mensagem recebida, um ator pode: tomar decisões locais, criar mais atores, enviar mais mensagens e determinar como responder à próxima mensagem recebida_.

**Casos de Uso**: Automação de geração de código, tarefas de análise de dados e construção de agentes personalizados para funções de planeamento e pesquisa.

Aqui estão alguns conceitos centrais importantes do AutoGen:

- **Agentes**. Um agente é uma entidade de software que:  
  - **Comunica-se via mensagens**, estas mensagens podem ser síncronas ou assíncronas.  
  - **Mantém o seu próprio estado**, que pode ser modificado por mensagens recebidas.  
  - **Realiza ações** em resposta a mensagens recebidas ou mudanças no seu estado. Estas ações podem modificar o estado do agente e produzir efeitos externos, como atualizar registos de mensagens, enviar novas mensagens, executar código ou fazer chamadas de API.  
    
  Aqui tem um pequeno trecho de código no qual cria o seu próprio agente com capacidades de chat:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    No código anterior, `MyAgent` foi criado e herda de `RoutedAgent`. Ele tem um manipulador de mensagens que imprime o conteúdo da mensagem e, em seguida, envia uma resposta usando o delegado `AssistantAgent`. Note especialmente como atribuímos a `self._delegate` uma instância de `AssistantAgent`, que é um agente pré-construído capaz de lidar com conclusões de chat.

    Vamos informar o AutoGen sobre este tipo de agente e iniciar o programa a seguir:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```
  
    No código anterior, os agentes são registados no runtime e, em seguida, uma mensagem é enviada ao agente, resultando na seguinte saída:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```
  
- **Multi-agentes**. O AutoGen suporta a criação de múltiplos agentes que podem trabalhar juntos para alcançar tarefas complexas. Os agentes podem comunicar-se, compartilhar informações e coordenar as suas ações para resolver problemas de forma mais eficiente. Para criar um sistema multi-agente, pode definir diferentes tipos de agentes com funções e papéis especializados, como recuperação de dados, análise, tomada de decisão e interação com o utilizador. Vamos ver como tal criação se parece para termos uma ideia:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```
  
    No código anterior, temos um `GroupChatManager` que é registado no runtime. Este gestor é responsável por coordenar as interações entre diferentes tipos de agentes, como escritores, ilustradores, editores e utilizadores.

- **Runtime de Agentes**. O framework fornece um ambiente de runtime, permitindo a comunicação entre agentes, gerindo as suas identidades e ciclos de vida, e impondo limites de segurança e privacidade. Isso significa que pode executar os seus agentes num ambiente seguro e controlado, garantindo que possam interagir de forma segura e eficiente. Existem dois runtimes de interesse:
  - **Runtime independente**. Esta é uma boa escolha para aplicações de processo único onde todos os agentes são implementados na mesma linguagem de programação e executados no mesmo processo. Aqui está uma ilustração de como funciona:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Runtime independente</a>   
Pilha de aplicação

    *os agentes comunicam-se via mensagens através do runtime, e o runtime gere o ciclo de vida dos agentes*

  - **Runtime distribuído de agentes**, é adequado para aplicações multi-processo onde os agentes podem ser implementados em diferentes linguagens de programação e executados em diferentes máquinas. Aqui está uma ilustração de como funciona:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Runtime distribuído</a>

## Semantic Kernel + Framework de Agentes

Semantic Kernel é um SDK de orquestração de IA pronto para empresas. Ele consiste em conectores de IA e memória, juntamente com um Framework de Agentes.

Vamos primeiro abordar alguns componentes principais:

- **Conectores de IA**: Esta é uma interface com serviços externos de IA e fontes de dados para uso tanto em Python quanto em C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```
  
    Aqui tem um exemplo simples de como pode criar um kernel e adicionar um serviço de conclusão de chat. Semantic Kernel cria uma conexão com um serviço externo de IA, neste caso, Azure OpenAI Chat Completion.

- **Plugins**: Estes encapsulam funções que uma aplicação pode usar. Existem plugins prontos e personalizados que pode criar. Um conceito relacionado é "funções de prompt". Em vez de fornecer pistas em linguagem natural para invocação de função, transmite certas funções ao modelo. Com base no contexto atual do chat, o modelo pode escolher chamar uma destas funções para completar um pedido ou consulta. Aqui está um exemplo:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```
  
    Aqui, primeiro tem um prompt de template `skPrompt` que deixa espaço para o utilizador inserir texto, `$userInput`. Depois cria a função do kernel `SummarizeText` e a importa no kernel com o nome do plugin `SemanticFunctions`. Note o nome da função que ajuda o Semantic Kernel a entender o que a função faz e quando deve ser chamada.

- **Função nativa**: Também há funções nativas que o framework pode chamar diretamente para realizar a tarefa. Aqui está um exemplo de tal função que recupera o conteúdo de um ficheiro:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```
  
- **Memória**: Abstrai e simplifica a gestão de contexto para aplicações de IA. A ideia com memória é que isto é algo que o LLM deve saber. Pode armazenar esta informação numa loja de vetores que acaba sendo uma base de dados em memória ou uma base de dados de vetores ou similar. Aqui está um exemplo de um cenário muito simplificado onde *fatos* são adicionados à memória:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```
  
Esses fatos são então armazenados na coleção de memória `SummarizedAzureDocs`. Este é um exemplo muito simplificado, mas pode ver como é possível armazenar informações na memória para que o LLM as utilize.

Então, esses são os fundamentos do framework Semantic Kernel, e quanto ao Agent Framework?

## Serviço de Agente Azure AI

O Serviço de Agente Azure AI é uma adição mais recente, introduzida no Microsoft Ignite 2024. Ele permite o desenvolvimento e a implementação de agentes de IA com modelos mais flexíveis, como a chamada direta de LLMs de código aberto, como Llama 3, Mistral e Cohere.

O Serviço de Agente Azure AI oferece mecanismos de segurança empresarial mais robustos e métodos de armazenamento de dados, tornando-o adequado para aplicações empresariais.

Funciona de forma integrada com frameworks de orquestração de múltiplos agentes, como AutoGen e Semantic Kernel.

Este serviço está atualmente em Public Preview e suporta Python e C# para a criação de agentes.

Usando o Semantic Kernel em Python, podemos criar um Agente Azure AI com um plugin definido pelo utilizador:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Conceitos principais

O Serviço de Agente Azure AI possui os seguintes conceitos principais:

- **Agente**. O Serviço de Agente Azure AI integra-se com o Azure AI Foundry. Dentro do AI Foundry, um Agente de IA atua como um microserviço "inteligente" que pode ser usado para responder a perguntas (RAG), realizar ações ou automatizar completamente fluxos de trabalho. Ele faz isso combinando o poder dos modelos de IA generativa com ferramentas que permitem acessar e interagir com fontes de dados do mundo real. Aqui está um exemplo de um agente:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Neste exemplo, um agente é criado com o modelo `gpt-4o-mini`, um nome `my-agent` e instruções `You are helpful agent`. O agente está equipado com ferramentas e recursos para realizar tarefas de interpretação de código.

- **Thread e mensagens**. O thread é outro conceito importante. Representa uma conversa ou interação entre um agente e um utilizador. Os threads podem ser usados para acompanhar o progresso de uma conversa, armazenar informações de contexto e gerir o estado da interação. Aqui está um exemplo de um thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    No código anterior, um thread é criado. Depois disso, uma mensagem é enviada ao thread. Ao chamar `create_and_process_run`, o agente é solicitado a realizar trabalho no thread. Finalmente, as mensagens são recuperadas e registadas para ver a resposta do agente. As mensagens indicam o progresso da conversa entre o utilizador e o agente. Também é importante entender que as mensagens podem ser de diferentes tipos, como texto, imagem ou ficheiro, ou seja, o trabalho do agente resultou, por exemplo, numa imagem ou numa resposta em texto. Como desenvolvedor, pode então usar essas informações para processar ainda mais a resposta ou apresentá-la ao utilizador.

- **Integração com outros frameworks de IA**. O Serviço de Agente Azure AI pode interagir com outros frameworks como AutoGen e Semantic Kernel, o que significa que pode construir parte da sua aplicação num desses frameworks e, por exemplo, usar o Serviço de Agente como um orquestrador ou construir tudo no Serviço de Agente.

**Casos de Uso**: O Serviço de Agente Azure AI foi projetado para aplicações empresariais que exigem uma implementação de agentes de IA segura, escalável e flexível.

## Qual é a diferença entre esses frameworks?

Pode parecer que há muita sobreposição entre esses frameworks, mas existem algumas diferenças importantes em termos de design, capacidades e casos de uso alvo:

- **AutoGen**: É um framework de experimentação focado em pesquisa de ponta sobre sistemas de múltiplos agentes. É o melhor lugar para experimentar e prototipar sistemas sofisticados de múltiplos agentes.
- **Semantic Kernel**: É uma biblioteca de agentes pronta para produção para construir aplicações empresariais baseadas em agentes. Foca-se em aplicações baseadas em eventos e distribuídas, permitindo múltiplos LLMs e SLMs, ferramentas e padrões de design de agentes únicos/múltiplos.
- **Serviço de Agente Azure AI**: É uma plataforma e serviço de implementação no Azure Foundry para agentes. Oferece conectividade com serviços suportados pelo Azure, como Azure OpenAI, Azure AI Search, Bing Search e execução de código.

Ainda não sabe qual escolher?

### Casos de Uso

Vamos tentar ajudar ao passar por alguns casos de uso comuns:

> P: Estou a experimentar, aprender e construir aplicações de agentes como prova de conceito, e quero ser capaz de construir e experimentar rapidamente
>

> R: AutoGen seria uma boa escolha para este cenário, pois foca-se em aplicações baseadas em eventos e distribuídas e suporta padrões avançados de design de múltiplos agentes.

> P: O que torna o AutoGen uma escolha melhor do que o Semantic Kernel e o Serviço de Agente Azure AI para este caso de uso?
>
> R: AutoGen foi especificamente projetado para aplicações baseadas em eventos e distribuídas, tornando-o bem adequado para automatizar tarefas de geração de código e análise de dados. Ele fornece as ferramentas e capacidades necessárias para construir sistemas complexos de múltiplos agentes de forma eficiente.

> P: Parece que o Serviço de Agente Azure AI também poderia funcionar aqui, ele tem ferramentas para geração de código e mais?
>
> R: Sim, o Serviço de Agente Azure AI é um serviço de plataforma para agentes e adiciona capacidades integradas para múltiplos modelos, Azure AI Search, Bing Search e Azure Functions. Facilita a construção dos seus agentes no Foundry Portal e a sua implementação em escala.

> P: Ainda estou confuso, apenas me dê uma opção
>
> R: Uma ótima escolha é construir a sua aplicação no Semantic Kernel primeiro e depois usar o Serviço de Agente Azure AI para implementar o seu agente. Esta abordagem permite-lhe persistir facilmente os seus agentes enquanto aproveita o poder de construir sistemas de múltiplos agentes no Semantic Kernel. Além disso, o Semantic Kernel tem um conector no AutoGen, tornando fácil usar ambos os frameworks juntos.

Vamos resumir as principais diferenças numa tabela:

| Framework | Foco | Conceitos Principais | Casos de Uso |
| --- | --- | --- | --- |
| AutoGen | Aplicações baseadas em eventos e distribuídas | Agentes, Personas, Funções, Dados | Geração de código, tarefas de análise de dados |
| Semantic Kernel | Compreensão e geração de conteúdo semelhante ao humano | Agentes, Componentes Modulares, Colaboração | Compreensão de linguagem natural, geração de conteúdo |
| Serviço de Agente Azure AI | Modelos flexíveis, segurança empresarial, Geração de código, Chamadas de ferramentas | Modularidade, Colaboração, Orquestração de Processos | Implementação de agentes de IA segura, escalável e flexível |

Qual é o caso de uso ideal para cada um desses frameworks?

## Posso integrar diretamente as ferramentas existentes do meu ecossistema Azure ou preciso de soluções independentes?

A resposta é sim, pode integrar diretamente as ferramentas existentes do seu ecossistema Azure com o Serviço de Agente Azure AI, especialmente porque foi construído para funcionar perfeitamente com outros serviços Azure. Poderia, por exemplo, integrar Bing, Azure AI Search e Azure Functions. Há também uma integração profunda com o Azure AI Foundry.

Para AutoGen e Semantic Kernel, também pode integrar com serviços Azure, mas pode ser necessário chamar os serviços Azure a partir do seu código. Outra forma de integrar é usar os SDKs Azure para interagir com os serviços Azure a partir dos seus agentes. Além disso, como mencionado, pode usar o Serviço de Agente Azure AI como um orquestrador para os seus agentes construídos no AutoGen ou Semantic Kernel, o que daria fácil acesso ao ecossistema Azure.

## Códigos de Exemplo

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Tem mais perguntas sobre frameworks de agentes de IA?

Junte-se ao [Discord do Azure AI Foundry](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horários de atendimento e obter respostas às suas perguntas sobre agentes de IA.

## Referências

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Serviço de Agente Azure</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel e AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Framework de Agente Semantic Kernel em Python</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Framework de Agente Semantic Kernel em .Net</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Serviço de Agente Azure AI</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Usando o Serviço de Agente Azure AI com AutoGen / Semantic Kernel para construir uma solução de múltiplos agentes</a>

## Aula Anterior

[Introdução a Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima Aula

[Compreendendo Padrões de Design de Agentes](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->