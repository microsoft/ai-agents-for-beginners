[![Explorando Frameworks de Agentes de IA](../../../translated_images/pt-PT/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Explore Frameworks de Agentes de IA

Frameworks de agentes de IA são plataformas de software concebidas para simplificar a criação, implementação e gestão de agentes de IA. Estes frameworks fornecem aos desenvolvedores componentes pré-construídos, abstrações e ferramentas que agilizam o desenvolvimento de sistemas complexos de IA.

Estes frameworks ajudam os desenvolvedores a focarem-se nos aspetos únicos das suas aplicações, fornecendo abordagens padronizadas para desafios comuns no desenvolvimento de agentes de IA. Eles melhoram a escalabilidade, acessibilidade e eficiência na construção de sistemas de IA.

## Introdução 

Esta lição irá cobrir:

- O que são Frameworks de Agentes de IA e o que permitem alcançar aos desenvolvedores?
- Como é que as equipas podem usar estes para prototipar rapidamente, iterar e melhorar as capacidades do seu agente?
- Quais são as diferenças entre os frameworks e ferramentas criados pela Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> e o <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Posso integrar diretamente as minhas ferramentas existentes do ecossistema Azure, ou preciso de soluções autónomas?
- O que é o Microsoft Foundry Agent Service e como é que isto me ajuda?

## Objetivos de aprendizagem

Os objetivos desta lição são ajudar-te a compreender:

- O papel dos Frameworks de Agentes de IA no desenvolvimento de IA.
- Como tirar partido dos Frameworks de Agentes de IA para construir agentes inteligentes.
- Capacidades chave habilitadas pelos Frameworks de Agentes de IA.
- As diferenças entre o Microsoft Agent Framework e o Microsoft Foundry Agent Service.

## O que são Frameworks de Agentes de IA e o que permitem aos desenvolvedores fazer?

Frameworks tradicionais de IA podem ajudar a integrar IA nas tuas aplicações e melhorar estas aplicações das seguintes formas:

- **Personalização**: A IA pode analisar o comportamento e preferências do utilizador para fornecer recomendações personalizadas, conteúdos e experiências.
Exemplo: Serviços de streaming como a Netflix usam IA para sugerir filmes e programas com base no histórico de visualização, aumentando o envolvimento e a satisfação do utilizador.
- **Automação e Eficiência**: A IA pode automatizar tarefas repetitivas, simplificar fluxos de trabalho e melhorar a eficiência operacional.
Exemplo: Aplicações de serviço ao cliente usam chatbots com IA para tratar perguntas comuns, reduzindo os tempos de resposta e libertando agentes humanos para problemas mais complexos.
- **Experiência do Utilizador Melhorada**: A IA pode melhorar a experiência geral do utilizador ao fornecer funcionalidades inteligentes como reconhecimento de voz, processamento de linguagem natural e texto preditivo.
Exemplo: Assistentes virtuais como a Siri e o Google Assistant usam IA para compreender e responder a comandos de voz, facilitando a interação dos utilizadores com os seus dispositivos.

### Tudo isso parece ótimo, certo? Então por que precisamos do Framework de Agentes de IA?

Frameworks de agentes de IA representam algo mais do que apenas frameworks de IA. Foram concebidos para permitir a criação de agentes inteligentes que podem interagir com utilizadores, outros agentes e o ambiente para alcançar objetivos específicos. Estes agentes podem exibir comportamento autónomo, tomar decisões e adaptar-se a condições em mudança. Vamos ver algumas capacidades chave habilitadas pelos Frameworks de Agentes de IA:

- **Colaboração e Coordenação de Agentes**: Permitem a criação de múltiplos agentes de IA que podem trabalhar juntos, comunicar-se e coordenar-se para resolver tarefas complexas.
- **Automação e Gestão de Tarefas**: Fornecem mecanismos para automatizar fluxos de trabalho em múltiplas etapas, delegação de tarefas e gestão dinâmica de tarefas entre agentes.
- **Compreensão Contextual e Adaptação**: Equipam agentes com a capacidade de entender o contexto, adaptar-se a ambientes em mudança e tomar decisões com base em informação em tempo real.

Resumindo, agentes permitem-te fazer mais, levar a automação ao próximo nível, criar sistemas mais inteligentes que podem adaptar-se e aprender com o seu ambiente.

## Como prototipar rapidamente, iterar e melhorar as capacidades do agente?

Este é um panorama em rápida evolução, mas há algumas coisas comuns na maioria dos Frameworks de Agentes de IA que te podem ajudar a prototipar e iterar rapidamente, nomeadamente componentes modulares, ferramentas colaborativas, e aprendizagem em tempo real. Vamos aprofundar estes pontos:

- **Usa Componentes Modulares**: SDKs de IA oferecem componentes pré-construídos como conectores de IA e de memória, chamada de funções usando linguagem natural ou plugins de código, modelos de prompt e mais.
- **Aproveita Ferramentas Colaborativas**: Desenha agentes com papéis e tarefas específicas, permitindo-lhes testar e refinar fluxos colaborativos.
- **Aprende em Tempo Real**: Implementa ciclos de feedback onde os agentes aprendem das interações e ajustam o seu comportamento dinamicamente.

### Usa Componentes Modulares

SDKs como o Microsoft Agent Framework oferecem componentes pré-construídos tais como conectores de IA, definições de ferramentas e gestão de agentes.

**Como as equipas podem usar isto**: Equipas podem reunir rapidamente estes componentes para criar um protótipo funcional sem começar do zero, permitindo experimentação e iteração rápidas.

**Como funciona na prática**: Podes usar um parser pré-construído para extrair informação da entrada do utilizador, um módulo de memória para armazenar e recuperar dados, e um gerador de prompts para interagir com os utilizadores, tudo sem ter de construir estes componentes do zero.

**Código de exemplo**. Vamos ver um exemplo de como podes usar o Microsoft Agent Framework com `FoundryChatClient` para fazer o modelo responder à entrada do utilizador com chamadas de ferramentas:

``` python
# Exemplo do Microsoft Agent Framework em Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definir uma função de ferramenta de exemplo para reservar viagens
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
    # Exemplo de saída: O seu voo para Nova Iorque no dia 1 de janeiro de 2025 foi reservado com sucesso. Boa viagem! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

O que podes ver neste exemplo é como podes aproveitar um parser pré-construído para extrair informação chave da entrada do utilizador, como origem, destino e data de um pedido de reserva de voo. Esta abordagem modular permite-te focar na lógica de alto nível.

### Aproveita Ferramentas Colaborativas

Frameworks como o Microsoft Agent Framework facilitam a criação de múltiplos agentes que podem trabalhar juntos.

**Como as equipas podem usar isto**: Equipas podem desenhar agentes com papéis e tarefas específicas, permitindo-lhes testar e refinar fluxos de trabalho colaborativos e melhorar a eficiência global do sistema.

**Como funciona na prática**: Podes criar uma equipa de agentes onde cada agente tem uma função especializada, como recuperação de dados, análise ou tomada de decisões. Estes agentes podem comunicar e partilhar informação para alcançar um objetivo comum, como responder a uma questão do utilizador ou completar uma tarefa.

**Código exemplo (Microsoft Agent Framework)**:

```python
# Criar múltiplos agentes que trabalham em conjunto usando o Microsoft Agent Framework

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

# Executar agentes em sequência numa tarefa
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

O que vês no código anterior é como podes criar uma tarefa que envolve múltiplos agentes a trabalhar juntos para analisar dados. Cada agente executa uma função específica, e a tarefa é executada através da coordenação dos agentes para alcançar o resultado desejado. Ao criares agentes dedicados com papéis especializados, podes melhorar a eficiência e desempenho da tarefa.

### Aprende em Tempo Real

Frameworks avançados fornecem capacidades para compreensão contextual e adaptação em tempo real.

**Como as equipas podem usar isto**: Equipas podem implementar ciclos de feedback onde os agentes aprendem das interações e ajustam o seu comportamento dinamicamente, levando a melhoria contínua e refinamento das capacidades.

**Como funciona na prática**: Agentes podem analisar feedback dos utilizadores, dados ambientais e resultados de tarefas para atualizar a sua base de conhecimento, ajustar algoritmos de decisão e melhorar o desempenho ao longo do tempo. Este processo iterativo de aprendizagem permite que os agentes se adaptem a condições em mudança e preferências dos utilizadores, melhorando a eficácia geral do sistema.

## Quais são as diferenças entre o Microsoft Agent Framework e o Microsoft Foundry Agent Service?

Existem muitas formas de comparar estas abordagens, mas vamos ver algumas diferenças chave em termos de design, capacidades e casos de uso alvo:

## Microsoft Agent Framework (MAF)

O Microsoft Agent Framework fornece um SDK simplificado para construir agentes de IA usando `FoundryChatClient`. Permite aos desenvolvedores criar agentes que tiram partido dos modelos Azure OpenAI com chamadas de ferramentas integradas, gestão de conversas e segurança ao nível empresarial através da identidade Azure.

**Casos de Uso**: Construção de agentes de IA prontos para produção com uso de ferramentas, fluxos de trabalho multi-etapas e cenários de integração empresarial.

Aqui estão alguns conceitos básicos importantes do Microsoft Agent Framework:

- **Agentes**. Um agente é criado via `FoundryChatClient` e configurado com um nome, instruções e ferramentas. O agente pode:
  - **Processar mensagens do utilizador** e gerar respostas usando modelos Azure OpenAI.
  - **Chamar ferramentas** automaticamente com base no contexto da conversa.
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

- **Ferramentas**. O framework suporta a definição de ferramentas como funções Python que o agente pode invocar automaticamente. As ferramentas são registadas ao criar o agente:

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

- **Coordenação Multi-Agente**. Podes criar múltiplos agentes com diferentes especializações e coordenar o seu trabalho:

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

- **Integração de Identidade Azure**. O framework usa `AzureCliCredential` (ou `DefaultAzureCredential`) para autenticação segura sem chaves, eliminando a necessidade de gerir diretamente as chaves API.

## Microsoft Foundry Agent Service

O Microsoft Foundry Agent Service é uma adição mais recente, apresentada na Microsoft Ignite 2024. Permite o desenvolvimento e implementação de agentes de IA com modelos mais flexíveis, como chamadas diretas a LLMs open-source como Llama 3, Mistral e Cohere.

O Microsoft Foundry Agent Service oferece mecanismos de segurança empresarial mais robustos e métodos de armazenamento de dados, tornando-o adequado para aplicações empresariais.

Funciona pronto a usar com o Microsoft Agent Framework para construir e implementar agentes.

Este serviço está atualmente em Pré-visualização Pública e suporta Python e C# para construir agentes.

Usando o SDK Python do Microsoft Foundry Agent Service, podemos criar um agente com uma ferramenta definida pelo utilizador:

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

### Conceitos principais

O Microsoft Foundry Agent Service tem os seguintes conceitos principais:

- **Agente**. O Microsoft Foundry Agent Service integra-se com o Microsoft Foundry. Dentro do Microsoft Foundry, um Agente de IA atua como um microserviço "inteligente" que pode ser usado para responder a perguntas (RAG), executar ações ou automatizar fluxos de trabalho completamente. Consegue isto combinando o poder dos modelos generativos de IA com ferramentas que lhe permitem aceder e interagir com fontes de dados do mundo real. Aqui está um exemplo de um agente:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Neste exemplo, um agente é criado com o modelo `gpt-5-mini`, um nome `meu-agente` e instruções `És um agente prestável`. O agente está equipado com ferramentas e recursos para executar tarefas de interpretação de código.

- **Thread e mensagens**. A thread é outro conceito importante. Representa uma conversa ou interação entre um agente e um utilizador. As threads podem ser usadas para rastrear o progresso de uma conversa, armazenar informação de contexto e gerir o estado da interação. Aqui está um exemplo de uma thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Peça ao agente para realizar trabalho na thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Buscar e registar todas as mensagens para ver a resposta do agente
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    No código anterior, uma thread é criada. Posteriormente, uma mensagem é enviada para a thread. Ao chamar `create_and_process_run`, solicita-se ao agente para executar trabalho na thread. Finalmente, as mensagens são buscadas e registadas para se ver a resposta do agente. As mensagens indicam o progresso da conversa entre o utilizador e o agente. Também é importante entender que as mensagens podem ser de diferentes tipos, como texto, imagem ou ficheiro, ou seja, o trabalho dos agentes resultou, por exemplo, numa imagem ou numa resposta de texto. Como programador, podes usar esta informação para processar ainda mais a resposta ou apresentá-la ao utilizador.

- **Integração com o Microsoft Agent Framework**. O Microsoft Foundry Agent Service funciona perfeitamente com o Microsoft Agent Framework, o que significa que podes construir agentes usando `FoundryChatClient` e implementá-los através do Agent Service para cenários de produção.

**Casos de Uso**: O Microsoft Foundry Agent Service é desenhado para aplicações empresariais que requerem uma implementação segura, escalável e flexível de agentes de IA.

## Qual é a diferença entre estas abordagens?
 
Parece que existe alguma sobreposição, mas há algumas diferenças chave em termos de design, capacidades e casos de uso alvo:
 
- **Microsoft Agent Framework (MAF)**: É um SDK pronto para produção para construir agentes de IA. Fornece uma API simplificada para criar agentes com chamada de ferramentas, gestão de conversas e integração com identidade Azure.
- **Microsoft Foundry Agent Service**: É uma plataforma e serviço de implementação no Microsoft Foundry para agentes. Oferece conectividade incorporada a serviços como Azure OpenAI, Azure AI Search, Bing Search e execução de código.
 
Ainda não tens certeza de qual escolher?

### Casos de Uso
 
Vamos ver se te podemos ajudar passando por alguns casos de uso comuns:
 
> P: Estou a construir aplicações de agentes de IA para produção e quero começar rapidamente
>

>R: O Microsoft Agent Framework é uma excelente escolha. Fornece uma API simples e pythonica via `FoundryChatClient` que te permite definir agentes com ferramentas e instruções em apenas algumas linhas de código.

>P: Preciso de implementação ao nível empresarial com integrações Azure como Search e execução de código
>
> R: O Microsoft Foundry Agent Service é a melhor opção. É uma plataforma que fornece capacidades incorporadas para múltiplos modelos, Azure AI Search, Bing Search e Azure Functions. Facilita construir os teus agentes no Portal Foundry e implementá-los em escala.
 
> P: Ainda estou confuso, apenas dá-me uma opção
>
> R: Começa com o Microsoft Agent Framework para construir os teus agentes e depois usa o Microsoft Foundry Agent Service quando precisares de os implementar e escalar em produção. Esta abordagem permite iterar rapidamente na lógica do agente enquanto tens um caminho claro para implementação empresarial.
 
Vamos resumir as diferenças principais numa tabela:

| Framework | Foco | Conceitos Principais | Casos de Uso |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK simplificado para agentes com chamada de ferramentas | Agentes, Ferramentas, Identidade Azure | Construir agentes de IA, uso de ferramentas, fluxos de trabalho multi-etapas |
| Microsoft Foundry Agent Service | Modelos flexíveis, segurança empresarial, geração de código, chamada de ferramentas | Modularidade, Colaboração, Orquestração de Processos | Implementação segura, escalável e flexível de agentes de IA |

## Posso integrar diretamente as minhas ferramentas existentes do ecossistema Azure, ou preciso de soluções autónomas?


A resposta é sim, pode integrar as suas ferramentas existentes do ecossistema Azure diretamente com o Microsoft Foundry Agent Service especialmente, pois foi construído para funcionar perfeitamente com outros serviços Azure. Poderia, por exemplo, integrar o Bing, Azure AI Search e Azure Functions. Há também uma integração profunda com o Microsoft Foundry.

O Microsoft Agent Framework também integra com serviços Azure através de `FoundryChatClient` e identidade Azure, permitindo-lhe chamar serviços Azure diretamente das suas ferramentas de agente.

## Códigos Exemplares

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre Frameworks de Agentes de IA?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar em horas de expediente e fazer as suas perguntas sobre Agentes de IA.

## Referências

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Aula Anterior

[Introdução a Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima Aula

[Compreender Padrões de Design Agénticos](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->