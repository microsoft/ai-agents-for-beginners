[![Explorando Frameworks para Agentes de IA](../../../translated_images/pt-BR/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_

# Explore Frameworks para Agentes de IA

Frameworks para agentes de IA são plataformas de software projetadas para simplificar a criação, implantação e gerenciamento de agentes de IA. Esses frameworks fornecem aos desenvolvedores componentes pré-construídos, abstrações e ferramentas que agilizam o desenvolvimento de sistemas complexos de IA.

Esses frameworks ajudam os desenvolvedores a focar nos aspectos únicos de suas aplicações, oferecendo abordagens padronizadas para desafios comuns no desenvolvimento de agentes de IA. Eles aprimoram a escalabilidade, acessibilidade e eficiência na construção de sistemas de IA.

## Introdução 

Esta aula abordará:

- O que são Frameworks de Agentes de IA e o que eles permitem que os desenvolvedores realizem?
- Como as equipes podem usar esses frameworks para prototipar rapidamente, iterar e melhorar as capacidades dos seus agentes?
- Quais são as diferenças entre os frameworks e ferramentas criados pela Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> e o <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Posso integrar diretamente as minhas ferramentas existentes do ecossistema Azure ou preciso de soluções independentes?
- O que é o Microsoft Foundry Agent Service e como ele me ajuda?

## Objetivos de aprendizagem

Os objetivos desta aula são ajudá-lo a entender:

- O papel dos Frameworks para Agentes de IA no desenvolvimento de IA.
- Como aproveitar Frameworks para Agentes de IA para construir agentes inteligentes.
- Capacidades-chave habilitadas pelos Frameworks para Agentes de IA.
- As diferenças entre o Microsoft Agent Framework e o Microsoft Foundry Agent Service.

## O que são Frameworks para Agentes de IA e o que eles permitem que os desenvolvedores façam?

Frameworks tradicionais de IA podem ajudar você a integrar IA em seus aplicativos e tornar esses aplicativos melhores das seguintes formas:

- **Personalização**: IA pode analisar o comportamento e preferências do usuário para fornecer recomendações, conteúdos e experiências personalizadas.
Exemplo: Serviços de streaming como Netflix usam IA para sugerir filmes e séries baseados no histórico de visualização, aumentando o engajamento e a satisfação do usuário.
- **Automação e Eficiência**: IA pode automatizar tarefas repetitivas, agilizar fluxos de trabalho e melhorar a eficiência operacional.
Exemplo: Aplicativos de atendimento ao cliente usam chatbots com IA para lidar com consultas comuns, reduzindo os tempos de resposta e liberando agentes humanos para questões mais complexas.
- **Melhoria da Experiência do Usuário**: IA pode aprimorar a experiência geral do usuário oferecendo recursos inteligentes como reconhecimento de voz, processamento de linguagem natural e texto preditivo.
Exemplo: Assistentes virtuais como Siri e Google Assistant usam IA para entender e responder a comandos de voz, facilitando a interação dos usuários com seus dispositivos.

### Isso tudo parece ótimo, certo? Então por que precisamos do Framework para Agentes de IA?

Frameworks para Agentes de IA representam algo além de frameworks tradicionais de IA. Eles são projetados para habilitar a criação de agentes inteligentes que podem interagir com usuários, outros agentes e o ambiente para alcançar objetivos específicos. Esses agentes podem apresentar comportamento autônomo, tomar decisões e se adaptar a condições mutáveis. Vamos ver algumas capacidades-chave habilitadas pelos Frameworks para Agentes de IA:

- **Colaboração e Coordenação entre Agentes**: Permite a criação de múltiplos agentes de IA que podem trabalhar juntos, se comunicar e coordenar para resolver tarefas complexas.
- **Automação e Gerenciamento de Tarefas**: Fornece mecanismos para automatizar fluxos de trabalho em múltiplas etapas, delegação de tarefas e gerenciamento dinâmico de tarefas entre agentes.
- **Compreensão Contextual e Adaptação**: Equipa os agentes com a capacidade de entender o contexto, adaptar-se a ambientes em mudança e tomar decisões baseadas em informações em tempo real.

Então, em resumo, agentes permitem que você faça mais, leve a automação para o próximo nível, crie sistemas mais inteligentes que podem se adaptar e aprender com seu ambiente.

## Como prototipar rapidamente, iterar e melhorar as capacidades do agente?

Este é um campo em rápida evolução, mas há algumas coisas comuns à maioria dos Frameworks para Agentes de IA que podem ajudar você a prototipar e iterar rapidamente, principalmente componentes modulares, ferramentas colaborativas e aprendizado em tempo real. Vamos explorar esses pontos:

- **Use Componentes Modulares**: SDKs de IA oferecem componentes pré-construídos como conectores de IA e memória, chamadas de função usando linguagem natural ou plugins de código, templates de prompt e mais.
- **Aproveite Ferramentas Colaborativas**: Projete agentes com papéis e tarefas específicas, permitindo que eles testem e aprimorem fluxos de trabalho colaborativos.
- **Aprenda em Tempo Real**: Implemente ciclos de feedback onde os agentes aprendem com as interações e ajustam seu comportamento dinamicamente.

### Use Componentes Modulares

SDKs como o Microsoft Agent Framework oferecem componentes pré-construídos como conectores de IA, definições de ferramentas e gerenciamento de agentes.

**Como equipes podem usar isso**: Equipes podem montar rapidamente esses componentes para criar um protótipo funcional sem começar do zero, permitindo experimentação rápida e iteração.

**Como funciona na prática**: Você pode usar um parser pré-construído para extrair informações da entrada do usuário, um módulo de memória para armazenar e recuperar dados, e um gerador de prompt para interagir com os usuários, tudo sem precisar construir esses componentes do zero.

**Exemplo de código**. Vamos ver um exemplo de como você pode usar o Microsoft Agent Framework com `FoundryChatClient` para que o modelo responda à entrada do usuário com chamadas de ferramentas:

``` python
# Exemplo de Framework Microsoft Agent em Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Defina uma função de ferramenta de exemplo para reservar viagens
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Saída de exemplo: Seu voo para Nova York em 1º de janeiro de 2025 foi reservado com sucesso. Boa viagem! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

O que você pode observar neste exemplo é como aproveitar um parser pré-construído para extrair informações chave da entrada do usuário, como origem, destino e data de uma solicitação de reserva de voo. Essa abordagem modular permite que você foque na lógica de alto nível.

### Aproveite Ferramentas Colaborativas

Frameworks como o Microsoft Agent Framework facilitam a criação de múltiplos agentes que podem trabalhar juntos.

**Como equipes podem usar isso**: Equipes podem projetar agentes com papéis e tarefas específicas, permitindo que testem e aprimorem fluxos de trabalho colaborativos e melhorem a eficiência geral do sistema.

**Como funciona na prática**: Você pode criar uma equipe de agentes onde cada agente tem uma função especializada, como recuperação de dados, análise ou tomada de decisões. Esses agentes podem se comunicar e compartilhar informações para alcançar um objetivo comum, como responder a uma consulta do usuário ou completar uma tarefa.

**Exemplo de código (Microsoft Agent Framework)**:

```python
# Criando múltiplos agentes que trabalham juntos usando o Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agente de Recuperação de Dados
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agente de Análise de Dados
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Executar agentes em sequência em uma tarefa
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

O que você vê no código anterior é como criar uma tarefa que envolve múltiplos agentes trabalhando juntos para analisar dados. Cada agente realiza uma função específica, e a tarefa é executada por meio da coordenação dos agentes para alcançar o resultado desejado. Ao criar agentes dedicados com papéis especializados, você pode melhorar a eficiência e desempenho da tarefa.

### Aprenda em Tempo Real

Frameworks avançados fornecem capacidades para compreensão de contexto em tempo real e adaptação.

**Como equipes podem usar isso**: Equipes podem implementar ciclos de feedback onde os agentes aprendem a partir das interações e ajustam seu comportamento dinamicamente, levando a melhorias contínuas e refinamento das capacidades.

**Como funciona na prática**: Os agentes podem analisar feedback dos usuários, dados ambientais e resultados de tarefas para atualizar sua base de conhecimento, ajustar algoritmos de tomada de decisão e melhorar o desempenho ao longo do tempo. Esse processo iterativo de aprendizado permite que agentes se adaptem a condições mutáveis e preferências dos usuários, aumentando a eficácia geral do sistema.

## Quais são as diferenças entre o Microsoft Agent Framework e o Microsoft Foundry Agent Service?

Existem muitas formas de comparar essas abordagens, mas vamos analisar algumas diferenças chave em termos de design, capacidades e casos de uso-alvo:

## Microsoft Agent Framework (MAF)

O Microsoft Agent Framework fornece um SDK simplificado para construir agentes de IA usando `FoundryChatClient`. Ele permite que desenvolvedores criem agentes que aproveitam modelos Azure OpenAI com chamadas integradas a ferramentas, gerenciamento de conversas e segurança empresarial por meio da identidade Azure.

**Casos de Uso**: Construção de agentes de IA prontos para produção com uso de ferramentas, fluxos de trabalho multi-etapas e cenários de integração empresarial.

Aqui estão alguns conceitos centrais importantes do Microsoft Agent Framework:

- **Agentes**. Um agente é criado via `FoundryChatClient` e configurado com nome, instruções e ferramentas. O agente pode:
  - **Processar mensagens dos usuários** e gerar respostas usando modelos Azure OpenAI.
  - **Chamar ferramentas** automaticamente baseado no contexto da conversa.
  - **Manter o estado da conversa** através de múltiplas interações.

  Aqui está um trecho de código mostrando como criar um agente:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Ferramentas**. O framework suporta definir ferramentas como funções Python que o agente pode invocar automaticamente. Ferramentas são registradas ao criar o agente:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Coordenação Multi-Agentes**. Você pode criar múltiplos agentes com especializações diferentes e coordenar seu trabalho:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integração de Identidade Azure**. O framework usa `AzureCliCredential` (ou `DefaultAzureCredential`) para autenticação segura e sem necessidade de chaves, eliminando a gestão direta de chaves API.

## Microsoft Foundry Agent Service

O Microsoft Foundry Agent Service é uma adição mais recente, apresentada no Microsoft Ignite 2024. Ele permite o desenvolvimento e implantação de agentes de IA com modelos mais flexíveis, como chamadas diretas a LLMs open-source como Llama 3, Mistral e Cohere.

O Microsoft Foundry Agent Service oferece mecanismos de segurança empresarial mais robustos e métodos de armazenamento de dados, tornando-o adequado para aplicações empresariais.

Ele funciona pronto para uso com o Microsoft Agent Framework para construir e implantar agentes.

Este serviço está atualmente em Prévia Pública e suporta Python e C# para construção de agentes.

Usando o SDK Python do Microsoft Foundry Agent Service, podemos criar um agente com uma ferramenta definida pelo usuário:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Define funções da ferramenta
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Conceitos centrais

O Microsoft Foundry Agent Service tem os seguintes conceitos centrais:

- **Agente**. O Microsoft Foundry Agent Service integra-se ao Microsoft Foundry. No Microsoft Foundry, um Agente de IA atua como um microsserviço "inteligente" que pode ser usado para responder perguntas (RAG), executar ações, ou automatizar fluxos de trabalho completamente. Isso é alcançado combinando o poder de modelos generativos de IA com ferramentas que permitem acessar e interagir com fontes de dados do mundo real. Aqui está um exemplo de um agente:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Neste exemplo, um agente é criado com o modelo `gpt-5-mini`, nome `my-agent` e instruções `Você é um agente prestativo`. O agente está equipado com ferramentas e recursos para realizar tarefas de interpretação de código.

- **Thread e mensagens**. A thread é outro conceito importante. Ela representa uma conversa ou interação entre um agente e um usuário. Threads podem ser usadas para acompanhar o progresso da conversa, armazenar informações de contexto e gerenciar o estado da interação. Aqui está um exemplo de uma thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Peça ao agente para realizar trabalho na thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Buscar e registrar todas as mensagens para ver a resposta do agente
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    No código anterior, uma thread é criada. Em seguida, uma mensagem é enviada para a thread. Ao chamar `create_and_process_run`, o agente é solicitado a trabalhar na thread. Finalmente, as mensagens são recuperadas e registradas para ver a resposta do agente. As mensagens indicam o progresso da conversa entre o usuário e o agente. Também é importante entender que as mensagens podem ser de tipos diferentes como texto, imagem ou arquivo, ou seja, o trabalho do agente pode ter resultado, por exemplo, em uma imagem ou em uma resposta em texto. Como desenvolvedor, você pode então usar essa informação para processar ainda mais a resposta ou apresentá-la ao usuário.

- **Integração com o Microsoft Agent Framework**. O Microsoft Foundry Agent Service funciona perfeitamente com o Microsoft Agent Framework, o que significa que você pode construir agentes usando `FoundryChatClient` e implantá-los através do Agent Service para cenários de produção.

**Casos de Uso**: O Microsoft Foundry Agent Service é projetado para aplicações empresariais que requerem implantação segura, escalável e flexível de agentes de IA.

## Qual é a diferença entre essas abordagens?
 
Parece que há sobreposição, mas há algumas diferenças chave em termos de design, capacidades e casos de uso-alvo:
 
- **Microsoft Agent Framework (MAF)**: É um SDK pronto para produção para construir agentes de IA. Ele fornece uma API simplificada para criar agentes com chamadas de ferramentas, gerenciamento de conversas e integração com identidade Azure.
- **Microsoft Foundry Agent Service**: É uma plataforma e serviço de implantação no Microsoft Foundry para agentes. Ele oferece conectividade integrada a serviços como Azure OpenAI, Azure AI Search, Bing Search e execução de código.
 
Ainda não tem certeza de qual escolher?

### Casos de Uso
 
Vamos ver se podemos ajudar passando por alguns casos de uso comuns:
 
> Q: Estou construindo aplicações de agentes de IA para produção e quero começar rapidamente
>

>R: O Microsoft Agent Framework é uma ótima escolha. Ele fornece uma API simples, em Python, via `FoundryChatClient` que permite definir agentes com ferramentas e instruções em poucas linhas de código.

>Q: Preciso de implantação com padrão empresarial com integrações Azure como Search e execução de código
>
> R: O Microsoft Foundry Agent Service é a melhor opção. É um serviço de plataforma que oferece capacidades integradas para múltiplos modelos, Azure AI Search, Bing Search e Azure Functions. Facilita construir seus agentes no Portal Foundry e implantá-los em escala.
 
> Q: Ainda estou confuso, me dê só uma opção
>
> R: Comece com o Microsoft Agent Framework para construir seus agentes, e depois use o Microsoft Foundry Agent Service quando precisar implantar e escalar em produção. Essa abordagem permite iterar rapidamente na lógica do agente enquanto mantém um caminho claro para implantação empresarial.
 
Vamos resumir as diferenças chave em uma tabela:

| Framework | Foco | Conceitos Centrais | Casos de Uso |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK simplificado para agentes com chamadas a ferramentas | Agentes, Ferramentas, Identidade Azure | Construção de agentes de IA, uso de ferramentas, fluxos multi-etapas |
| Microsoft Foundry Agent Service | Modelos flexíveis, segurança empresarial, geração de código, chamada a ferramentas | Modularidade, Colaboração, Orquestração de Processos | Implantação segura, escalável e flexível de agentes de IA |

## Posso integrar diretamente minhas ferramentas do ecossistema Azure, ou preciso de soluções independentes?


A resposta é sim, você pode integrar suas ferramentas existentes no ecossistema Azure diretamente com o Microsoft Foundry Agent Service especialmente, pois foi construído para funcionar perfeitamente com outros serviços do Azure. Você poderia, por exemplo, integrar o Bing, Azure AI Search e Azure Functions. Há também uma integração profunda com o Microsoft Foundry.

O Microsoft Agent Framework também se integra com os serviços Azure através do `FoundryChatClient` e identidade Azure, permitindo que você chame serviços Azure diretamente de suas ferramentas de agente.

## Códigos de Exemplo

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre Frameworks de Agentes de IA?

Participe do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de sessões de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Referências

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Aula Anterior

[Introdução a Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima Aula

[Compreendendo Padrões de Design Agentic](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->