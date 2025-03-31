<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d3ceafa2939ede602b96d6bd412c5cbf",
  "translation_date": "2025-03-28T11:44:14+00:00",
  "source_file": "02-explore-agentic-frameworks\\README.md",
  "language_code": "pt"
}
-->
[![Explorando Frameworks de Agentes de IA](../../../translated_images/lesson-2-thumbnail.807a3a4fc57057096d10678bf84638d17d50c50239014e75a7708731a33bb802.pt.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Explore Frameworks de Agentes de IA

Os frameworks de agentes de IA são plataformas de software projetadas para simplificar a criação, implantação e gerenciamento de agentes de IA. Esses frameworks oferecem aos desenvolvedores componentes pré-construídos, abstrações e ferramentas que facilitam o desenvolvimento de sistemas de IA complexos.

Eles ajudam os desenvolvedores a focar nos aspectos únicos de suas aplicações, fornecendo abordagens padronizadas para desafios comuns no desenvolvimento de agentes de IA. Além disso, aumentam a escalabilidade, acessibilidade e eficiência na construção de sistemas de IA.

## Introdução 

Nesta lição, abordaremos:

- O que são frameworks de agentes de IA e o que eles permitem que os desenvolvedores realizem?
- Como as equipes podem utilizá-los para prototipar, iterar e melhorar rapidamente as capacidades de seus agentes?
- Quais são as diferenças entre os frameworks e ferramentas criados pela Microsoft, e como eles se comparam?

## Objetivos de aprendizagem

Os objetivos desta lição são ajudá-lo a entender:

- O papel dos frameworks de agentes de IA no desenvolvimento de IA.
- Como aproveitar os frameworks de agentes de IA para construir agentes inteligentes.
- Capacidades principais habilitadas por frameworks de agentes de IA.
- As diferenças entre AutoGen, Semantic Kernel e Azure AI Agent Service.

## O que são frameworks de agentes de IA e o que eles permitem que os desenvolvedores façam?

Frameworks de IA tradicionais podem ajudar você a integrar IA em seus aplicativos e melhorá-los das seguintes formas:

- **Personalização**: A IA pode analisar o comportamento e as preferências do usuário para fornecer recomendações, conteúdo e experiências personalizadas.  
Exemplo: Serviços de streaming como Netflix utilizam IA para sugerir filmes e séries com base no histórico de visualização, aumentando o engajamento e a satisfação do usuário.

- **Automação e eficiência**: A IA pode automatizar tarefas repetitivas, otimizar fluxos de trabalho e melhorar a eficiência operacional.  
Exemplo: Aplicativos de atendimento ao cliente utilizam chatbots baseados em IA para lidar com dúvidas comuns, reduzindo o tempo de resposta e liberando agentes humanos para questões mais complexas.

- **Experiência aprimorada do usuário**: A IA pode melhorar a experiência geral do usuário ao oferecer recursos inteligentes, como reconhecimento de voz, processamento de linguagem natural e texto preditivo.  
Exemplo: Assistentes virtuais como Siri e Google Assistant utilizam IA para entender e responder a comandos de voz, facilitando a interação dos usuários com seus dispositivos.

### Isso parece ótimo, certo? Então, por que precisamos de frameworks de agentes de IA?

Frameworks de agentes de IA representam algo além dos frameworks de IA tradicionais. Eles são projetados para possibilitar a criação de agentes inteligentes que podem interagir com usuários, outros agentes e o ambiente para alcançar objetivos específicos. Esses agentes podem exibir comportamento autônomo, tomar decisões e se adaptar a condições mutáveis. Vamos explorar algumas capacidades principais habilitadas por frameworks de agentes de IA:

- **Colaboração e coordenação entre agentes**: Permitem a criação de múltiplos agentes de IA que podem trabalhar juntos, se comunicar e coordenar para resolver tarefas complexas.
- **Automação e gerenciamento de tarefas**: Oferecem mecanismos para automatizar fluxos de trabalho em várias etapas, delegação de tarefas e gerenciamento dinâmico de tarefas entre agentes.
- **Compreensão e adaptação contextual**: Equipam os agentes com a capacidade de entender o contexto, se adaptar a ambientes em mudança e tomar decisões com base em informações em tempo real.

Em resumo, os agentes permitem fazer mais, levando a automação para o próximo nível e criando sistemas mais inteligentes que podem aprender e se adaptar ao seu ambiente.

## Como prototipar, iterar e melhorar rapidamente as capacidades de um agente?

Este é um campo em constante evolução, mas há elementos comuns na maioria dos frameworks de agentes de IA que ajudam a prototipar e iterar rapidamente, como componentes modulares, ferramentas colaborativas e aprendizado em tempo real. Vamos explorar cada um deles:

- **Use componentes modulares**: SDKs de IA oferecem componentes pré-construídos, como conectores de IA e memória, chamadas de função usando linguagem natural ou plugins de código, templates de prompt e mais.
- **Aproveite ferramentas colaborativas**: Projete agentes com papéis e tarefas específicas, permitindo testar e refinar fluxos de trabalho colaborativos.
- **Aprenda em tempo real**: Implemente loops de feedback onde os agentes aprendem com interações e ajustam seu comportamento dinamicamente.

### Use componentes modulares

SDKs como Microsoft Semantic Kernel e LangChain oferecem componentes pré-construídos, como conectores de IA, templates de prompt e gerenciamento de memória.

**Como as equipes podem utilizá-los**: Equipes podem montar rapidamente esses componentes para criar um protótipo funcional sem começar do zero, permitindo experimentação e iteração rápidas.

**Como funciona na prática**: Você pode usar um parser pré-construído para extrair informações da entrada do usuário, um módulo de memória para armazenar e recuperar dados e um gerador de prompts para interagir com os usuários, tudo sem precisar criar esses componentes do zero.

**Exemplo de código**: Vamos ver exemplos de como usar um conector de IA pré-construído com Semantic Kernel Python e .Net que utiliza chamadas automáticas de função para o modelo responder à entrada do usuário:

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

Neste exemplo, você pode ver como aproveitar um parser pré-construído para extrair informações-chave da entrada do usuário, como origem, destino e data de uma solicitação de reserva de voo. Essa abordagem modular permite focar na lógica de alto nível.

### Aproveite ferramentas colaborativas

Frameworks como CrewAI, Microsoft AutoGen e Semantic Kernel facilitam a criação de múltiplos agentes que podem trabalhar juntos.

**Como as equipes podem utilizá-los**: Equipes podem projetar agentes com papéis e tarefas específicas, permitindo testar e refinar fluxos de trabalho colaborativos e melhorar a eficiência geral do sistema.

**Como funciona na prática**: Você pode criar uma equipe de agentes onde cada um tem uma função especializada, como recuperação de dados, análise ou tomada de decisão. Esses agentes podem se comunicar e compartilhar informações para alcançar um objetivo comum, como responder a uma consulta do usuário ou concluir uma tarefa.

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

No código anterior, você vê como criar uma tarefa que envolve múltiplos agentes trabalhando juntos para analisar dados. Cada agente realiza uma função específica, e a tarefa é executada coordenando os agentes para alcançar o resultado desejado. Ao criar agentes dedicados com papéis especializados, você pode melhorar a eficiência e o desempenho da tarefa.

### Aprenda em tempo real

Frameworks avançados oferecem capacidades para compreensão de contexto em tempo real e adaptação.

**Como as equipes podem utilizá-los**: Equipes podem implementar loops de feedback onde os agentes aprendem com interações e ajustam seu comportamento dinamicamente, levando a melhorias contínuas e refinamento de capacidades.

**Como funciona na prática**: Agentes podem analisar feedback do usuário, dados ambientais e resultados de tarefas para atualizar sua base de conhecimento, ajustar algoritmos de tomada de decisão e melhorar o desempenho ao longo do tempo. Esse processo de aprendizado iterativo permite que os agentes se adaptem a condições e preferências do usuário em constante mudança, aumentando a eficácia geral do sistema.

## Quais são as diferenças entre os frameworks AutoGen, Semantic Kernel e Azure AI Agent Service?

Há várias maneiras de comparar esses frameworks, mas vamos examinar algumas diferenças principais em termos de design, capacidades e casos de uso:

## AutoGen

AutoGen é um framework de código aberto desenvolvido pelo AI Frontiers Lab da Microsoft Research. Ele se concentra em aplicativos *agentes* distribuídos e orientados por eventos, permitindo múltiplos LLMs e SLMs, ferramentas e padrões avançados de design de múltiplos agentes.

AutoGen é construído em torno do conceito central de agentes, que são entidades autônomas capazes de perceber seu ambiente, tomar decisões e executar ações para alcançar objetivos específicos. Os agentes se comunicam por meio de mensagens assíncronas, permitindo que trabalhem de forma independente e paralela, aumentando a escalabilidade e a capacidade de resposta do sistema.
Modularidade, Colaboração, Orquestração de Processos | Implantação segura, escalável e flexível de agentes de IA | Qual é o caso de uso ideal para cada um desses frameworks? 

## Posso integrar diretamente minhas ferramentas existentes do ecossistema Azure ou preciso de soluções independentes?

A resposta é sim, você pode integrar diretamente suas ferramentas existentes do ecossistema Azure com o Azure AI Agent Service, especialmente porque ele foi desenvolvido para funcionar de forma integrada com outros serviços Azure. Por exemplo, você pode integrar Bing, Azure AI Search e Azure Functions. Há também uma integração profunda com o Azure AI Foundry.

Para AutoGen e Semantic Kernel, também é possível integrar com os serviços Azure, mas pode ser necessário chamar esses serviços a partir do seu código. Outra forma de integração é usar os SDKs do Azure para interagir com os serviços Azure a partir de seus agentes. Além disso, como mencionado, você pode usar o Azure AI Agent Service como um orquestrador para seus agentes criados no AutoGen ou Semantic Kernel, o que facilitaria o acesso ao ecossistema Azure.

## Referências

## Aula Anterior

[Introdução aos Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima Aula

[Entendendo Padrões de Design Agentes](../03-agentic-design-patterns/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.