[![Exploring AI Agent Frameworks](../../../translated_images/pt-PT/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Explore Frameworks de Agentes de IA

Os frameworks de agentes de IA são plataformas de software projetadas para simplificar a criação, implementação e gestão de agentes de IA. Estes frameworks fornecem aos desenvolvedores componentes pré-construídos, abstrações e ferramentas que agilizam o desenvolvimento de sistemas de IA complexos.

Estes frameworks ajudam os desenvolvedores a concentrar-se nos aspetos únicos das suas aplicações, fornecendo abordagens padronizadas para desafios comuns no desenvolvimento de agentes de IA. Melhoram a escalabilidade, acessibilidade e eficiência na construção de sistemas de IA.

## Introdução 

Esta lição cobrirá:

- O que são Frameworks de Agentes de IA e o que permitem aos desenvolvedores alcançar?
- Como é que as equipas podem usar estes para prototipar rapidamente, iterar e melhorar as capacidades do seu agente?
- Quais as diferenças entre os frameworks e ferramentas criadas pela Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> e o <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Posso integrar diretamente as minhas ferramentas existentes do ecossistema Azure, ou preciso de soluções autónomas?
- O que é o serviço Azure AI Agents e como é que isto me ajuda?

## Objetivos de aprendizagem

Os objetivos desta lição são ajudá-lo a compreender:

- O papel dos Frameworks de Agentes de IA no desenvolvimento de IA.
- Como tirar partido dos Frameworks de Agentes de IA para construir agentes inteligentes.
- As principais capacidades habilitadas pelos Frameworks de Agentes de IA.
- As diferenças entre o Microsoft Agent Framework e o Azure AI Agent Service.

## O que são Frameworks de Agentes de IA e o que permitem aos desenvolvedores fazer?

Os frameworks tradicionais de IA podem ajudá-lo a integrar IA nas suas aplicações e melhorar essas aplicações das seguintes formas:

- **Personalização**: A IA pode analisar o comportamento e as preferências do utilizador para fornecer recomendações, conteúdos e experiências personalizados.
Exemplo: Serviços de streaming como a Netflix usam IA para sugerir filmes e programas com base no histórico de visualização, aumentando o envolvimento e satisfação do utilizador.
- **Automação e Eficiência**: A IA pode automatizar tarefas repetitivas, otimizar fluxos de trabalho e melhorar a eficiência operacional.
Exemplo: Aplicações de serviço ao cliente usam chatbots com IA para tratar questões comuns, reduzindo os tempos de resposta e libertando agentes humanos para problemas mais complexos.
- **Melhoria da Experiência do Utilizador**: A IA pode melhorar a experiência geral do utilizador ao fornecer funcionalidades inteligentes, como reconhecimento de voz, processamento de linguagem natural e texto preditivo.
Exemplo: Assistentes virtuais como Siri e Google Assistant usam IA para compreender e responder a comandos de voz, tornando mais fácil a interação dos utilizadores com os seus dispositivos.

### Isto tudo soa bem, certo? Então, por que precisamos do Framework de Agentes de IA?

Os frameworks de agentes de IA representam algo mais do que apenas frameworks de IA. Eles são desenhados para possibilitar a criação de agentes inteligentes que podem interagir com utilizadores, outros agentes e o ambiente para alcançar objetivos específicos. Estes agentes podem exibir comportamentos autónomos, tomar decisões e adaptar-se às condições em mudança. Vejamos algumas capacidades chave habilitadas pelos Frameworks de Agentes de IA:

- **Colaboração e Coordenação de Agentes**: Permite a criação de múltiplos agentes de IA que podem trabalhar em conjunto, comunicar-se e coordenar para resolver tarefas complexas.
- **Automação e Gestão de Tarefas**: Fornece mecanismos para automatizar fluxos de trabalho com vários passos, delegação de tarefas e gestão dinâmica de tarefas entre agentes.
- **Compreensão Contextual e Adaptação**: Equipa agentes com a capacidade de entender o contexto, adaptar-se a ambientes em mudança e tomar decisões baseadas em informação em tempo real.

Assim, em resumo, os agentes permitem-lhe fazer mais, levar a automação para o próximo nível, criar sistemas mais inteligentes que podem adaptar-se e aprender com o seu ambiente.

## Como prototipar rapidamente, iterar e melhorar as capacidades do agente?

Este é um campo em rápida evolução, mas há alguns elementos comuns na maioria dos Frameworks de Agentes de IA que podem ajudá-lo a prototipar e iterar rapidamente, nomeadamente componentes modulares, ferramentas colaborativas e aprendizagem em tempo real. Vamos explorar estes aspectos:

- **Use Componentes Modulares**: Os SDKs de IA oferecem componentes pré-construídos, tais como conectores de IA e Memória, chamadas de funções usando linguagem natural ou plugins de código, modelos de prompts, e mais.
- **Tire Partido de Ferramentas Colaborativas**: Desenhe agentes com funções e tarefas específicas, permitindo-lhes testar e refinar fluxos de trabalho colaborativos.
- **Aprenda em Tempo Real**: Implemente ciclos de feedback onde os agentes aprendem das interações e ajustam o seu comportamento dinamicamente.

### Use Componentes Modulares

SDKs como o Microsoft Agent Framework oferecem componentes pré-construídos como conectores de IA, definições de ferramentas e gestão de agentes.

**Como as equipas podem usar isto**: As equipas podem rapidamente combinar estes componentes para criar um protótipo funcional sem começar do zero, permitindo experimentação e iteração rápida.

**Como funciona na prática**: Pode usar um parser pré-construído para extrair informação da entrada do utilizador, um módulo de memória para armazenar e recuperar dados, e um gerador de prompts para interagir com utilizadores, tudo sem ter de construir estes componentes do início.

**Exemplo de código**. Vejamos um exemplo de como pode usar o Microsoft Agent Framework com `AzureAIProjectAgentProvider` para fazer o modelo responder à entrada do utilizador com chamadas a ferramentas:

``` python
# Exemplo em Python do Microsoft Agent Framework

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Define uma função de ferramenta de exemplo para reservar viagens
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Exemplo de saída: O seu voo para Nova Iorque no dia 1 de janeiro de 2025 foi reservado com sucesso. Boa viagem! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

O que pode ver neste exemplo é como pode tirar partido de um parser pré-construído para extrair informação chave da entrada do utilizador, como a origem, destino e data de um pedido de reserva de voo. Esta abordagem modular permite-lhe concentrar-se na lógica de alto nível.

### Tire Partido de Ferramentas Colaborativas

Frameworks como o Microsoft Agent Framework facilitam a criação de múltiplos agentes que podem trabalhar em conjunto.

**Como as equipas podem usar isto**: As equipas podem desenhar agentes com funções e tarefas específicas, permitindo-lhes testar e refinar fluxos de trabalho colaborativos e melhorar a eficiência global do sistema.

**Como funciona na prática**: Pode criar uma equipa de agentes onde cada agente tem uma função especializada, como recuperação de dados, análise ou tomada de decisões. Estes agentes podem comunicar-se e partilhar informação para alcançar um objetivo comum, como responder a uma questão do utilizador ou completar uma tarefa.

**Exemplo de código (Microsoft Agent Framework)**:

```python
# Criar vários agentes que trabalham em conjunto usando a Estrutura de Agentes da Microsoft

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agente de Recuperação de Dados
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agente de Análise de Dados
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Executar agentes em sequência numa tarefa
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

O que vê no código anterior é como pode criar uma tarefa que envolve múltiplos agentes a trabalhar juntos para analisar dados. Cada agente realiza uma função específica, e a tarefa é executada através da coordenação dos agentes para alcançar o resultado desejado. Ao criar agentes dedicados com papéis especializados, pode melhorar a eficiência e desempenho da tarefa.

### Aprenda em Tempo Real

Frameworks avançados fornecem capacidades para compreensão de contexto em tempo real e adaptação.

**Como as equipas podem usar isto**: As equipas podem implementar ciclos de feedback onde os agentes aprendem das interações e ajustam o seu comportamento dinamicamente, conduzindo a melhorias contínuas e refinamento das capacidades.

**Como funciona na prática**: Os agentes podem analisar feedback dos utilizadores, dados ambientais e resultados de tarefas para atualizar a sua base de conhecimento, ajustar algoritmos de tomada de decisão e melhorar o desempenho ao longo do tempo. Este processo iterativo de aprendizagem permite que agentes se adaptem a condições em mudança e preferências dos utilizadores, aumentando a eficácia geral do sistema.

## Quais as diferenças entre o Microsoft Agent Framework e o Azure AI Agent Service?

Existem várias formas de comparar estas abordagens, mas vejamos algumas diferenças chave em termos de design, capacidades e casos de uso alvo:

## Microsoft Agent Framework (MAF)

O Microsoft Agent Framework oferece um SDK simplificado para construir agentes de IA usando `AzureAIProjectAgentProvider`. Permite aos desenvolvedores criar agentes que utilizam modelos Azure OpenAI com chamadas de ferramentas integradas, gestão de conversação e segurança empresarial de nível empresarial através da identidade Azure.

**Casos de uso**: Construção de agentes de IA prontos para produção com uso de ferramentas, fluxos de trabalho multi-etapas e cenários de integração empresarial.

Aqui estão alguns conceitos principais do Microsoft Agent Framework:

- **Agentes**. Um agente é criado através de `AzureAIProjectAgentProvider` e configurado com um nome, instruções e ferramentas. O agente pode:
  - **Processar mensagens dos utilizadores** e gerar respostas usando modelos Azure OpenAI.
  - **Chamar ferramentas** automaticamente com base no contexto da conversa.
  - **Manter o estado da conversa** ao longo de múltiplas interações.

  Aqui está um excerto de código que mostra como criar um agente:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Ferramentas**. O framework suporta a definição de ferramentas como funções Python que o agente pode invocar automaticamente. As ferramentas são registadas ao criar o agente:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Coordenação Multi-Agente**. Pode criar múltiplos agentes com diferentes especializações e coordenar o seu trabalho:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integração com Identidade Azure**. O framework usa `AzureCliCredential` (ou `DefaultAzureCredential`) para autenticação segura sem chaves, eliminando a necessidade de gerir diretamente chaves API.

## Azure AI Agent Service

O Azure AI Agent Service é uma adição mais recente, apresentada na Microsoft Ignite 2024. Permite o desenvolvimento e implementação de agentes de IA com modelos mais flexíveis, como chamadas diretas a LLMs open-source como Llama 3, Mistral e Cohere.

O Azure AI Agent Service fornece mecanismos de segurança empresarial mais robustos e métodos de armazenamento de dados, tornando-o adequado para aplicações empresariais.

Funciona fora-da-caixa com o Microsoft Agent Framework para construir e implementar agentes.

Este serviço está atualmente em Public Preview e suporta Python e C# para construção de agentes.

Usando o SDK Python do Azure AI Agent Service, podemos criar um agente com uma ferramenta definida pelo utilizador:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definir funções da ferramenta
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
        model="gpt-4o-mini",
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

### Conceitos principais

O Azure AI Agent Service tem os seguintes conceitos principais:

- **Agente**. O Azure AI Agent Service integra-se com o Microsoft Foundry. Dentro do AI Foundry, um agente de IA age como um microserviço "inteligente" que pode ser usado para responder a perguntas (RAG), realizar ações ou automatizar completamente fluxos de trabalho. Isto alcança-se combinando o poder dos modelos generativos de IA com ferramentas que permitem aceder e interagir com fontes de dados do mundo real. Aqui está um exemplo de um agente:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Neste exemplo, um agente é criado com o modelo `gpt-4o-mini`, um nome `my-agent` e as instruções `You are helpful agent`. O agente está equipado com ferramentas e recursos para realizar tarefas de interpretação de código.

- **Thread e mensagens**. O thread é outro conceito importante. Representa uma conversa ou interação entre um agente e um utilizador. Os threads podem ser usados para acompanhar o progresso de uma conversa, armazenar informação de contexto e gerir o estado da interação. Aqui está um exemplo de um thread:

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

    No código anterior, um thread é criado. Depois, uma mensagem é enviada para o thread. Chamando `create_and_process_run`, o agente é solicitado a realizar trabalho no thread. Finalmente, as mensagens são buscadas e registadas para ver a resposta do agente. As mensagens indicam o progresso da conversa entre o utilizador e o agente. É também importante compreender que as mensagens podem ser de tipos diferentes, como texto, imagem ou ficheiro, ou seja, o trabalho dos agentes pode ter resultado, por exemplo, numa imagem ou resposta em texto. Como desenvolvedor, pode então usar esta informação para processar ainda mais a resposta ou apresentá-la ao utilizador.

- **Integração com o Microsoft Agent Framework**. O Azure AI Agent Service funciona perfeitamente com o Microsoft Agent Framework, o que significa que pode criar agentes usando `AzureAIProjectAgentProvider` e implementá-los através do Agent Service para cenários de produção.

**Casos de uso**: O Azure AI Agent Service é projetado para aplicações empresariais que requerem implementação segura, escalável e flexível de agentes de IA.

## Qual é a diferença entre estas abordagens?
 
Parece que existe sobreposição, mas há algumas diferenças chave em termos de design, capacidades, e casos de uso alvo:
 
- **Microsoft Agent Framework (MAF)**: É um SDK pronto para produção para construir agentes de IA. Fornece uma API simplificada para criar agentes com chamadas de ferramentas, gestão de conversações e integração com identidade Azure.
- **Azure AI Agent Service**: É uma plataforma e serviço de implementação no Azure Foundry para agentes. Oferece conectividade incorporada a serviços como Azure OpenAI, Azure AI Search, Bing Search e execução de código.
 
Ainda não tem certeza de qual escolher?

### Casos de uso
 
Vamos ver se ajudamos percebendo alguns casos de uso comuns:
 
> Q: Estou a construir aplicações de agentes de IA para produção e quero começar rapidamente
>

> A: O Microsoft Agent Framework é uma ótima escolha. Ele fornece uma API simples e Pythonic via `AzureAIProjectAgentProvider` que permite definir agentes com ferramentas e instruções em apenas algumas linhas de código.

> Q: Preciso de implementação de nível empresarial com integrações Azure como Search e execução de código
>
> A: O Azure AI Agent Service é o mais adequado. É um serviço de plataforma que oferece capacidades incorporadas para múltiplos modelos, Azure AI Search, Bing Search e Azure Functions. Facilita a construção dos seus agentes no Foundry Portal e a sua implementação em escala.
 
> Q: Ainda estou confuso, dá-me só uma opção
>
> A: Comece com o Microsoft Agent Framework para construir os seus agentes e depois use o Azure AI Agent Service quando precisar de implementar e escalar em produção. Esta abordagem permite iterar rapidamente na lógica do agente enquanto tem um caminho claro para implementação empresarial.
 
Vamos resumir as diferenças chave numa tabela:

| Framework | Foco | Conceitos Principais | Casos de Uso |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK agilizado para agentes com chamadas a ferramentas | Agentes, Ferramentas, Identidade Azure | Construção de agentes IA, uso de ferramentas, fluxos de trabalho multi-etapas |
| Azure AI Agent Service | Modelos flexíveis, segurança empresarial, geração de código, chamadas a ferramentas | Modularidade, Colaboração, Orquestração de processos | Implementação segura, escalável e flexível de agentes IA |

## Posso integrar diretamente as minhas ferramentas existentes do ecossistema Azure, ou preciso de soluções autónomas?
A resposta é sim, pode integrar as suas ferramentas do ecossistema Azure existentes diretamente com o Azure AI Agent Service especialmente, uma vez que foi concebido para funcionar perfeitamente com outros serviços Azure. Poderia, por exemplo, integrar o Bing, Azure AI Search e Azure Functions. Existe também uma integração profunda com a Microsoft Foundry.

O Microsoft Agent Framework também se integra com os serviços Azure através do `AzureAIProjectAgentProvider` e da identidade Azure, permitindo-lhe chamar serviços Azure diretamente a partir das suas ferramentas de agentes.

## Exemplo de Códigos

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre AI Agent Frameworks?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conhecer outros aprendizes, participar em sessões de atendimento e obter respostas às suas perguntas sobre AI Agents.

## Referências

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Aula Anterior

[Introdução aos AI Agents e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima Aula

[Compreender os Padrões de Design Agentic](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->