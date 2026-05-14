[![Como Projetar Bons Agentes de IA](../../../translated_images/pt-BR/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Padrão de Design de Uso de Ferramentas

Ferramentas são interessantes porque permitem que agentes de IA tenham uma gama maior de capacidades. Em vez de o agente ter um conjunto limitado de ações que pode realizar, ao adicionar uma ferramenta, o agente pode agora executar uma ampla variedade de ações. Neste capítulo, vamos examinar o Padrão de Design de Uso de Ferramentas, que descreve como agentes de IA podem utilizar ferramentas específicas para atingir seus objetivos.

## Introdução

Nesta lição, buscamos responder às seguintes perguntas:

- O que é o padrão de design de uso de ferramentas?
- Quais são os casos de uso aos quais ele pode ser aplicado?
- Quais são os elementos/blocos de construção necessários para implementar o padrão de design?
- Quais são as considerações especiais para usar o Padrão de Design de Uso de Ferramentas para construir agentes de IA confiáveis?

## Objetivos de Aprendizagem

Após concluir esta lição, você será capaz de:

- Definir o Padrão de Design de Uso de Ferramentas e seu propósito.
- Identificar casos de uso onde o Padrão de Design de Uso de Ferramentas é aplicável.
- Compreender os elementos-chave necessários para implementar o padrão de design.
- Reconhecer considerações para garantir a confiabilidade em agentes de IA que utilizam este padrão de design.

## O que é o Padrão de Design de Uso de Ferramentas?

O **Padrão de Design de Uso de Ferramentas** foca em dar aos Modelos de Linguagem de Grande Escala (LLMs) a capacidade de interagir com ferramentas externas para alcançar objetivos específicos. Ferramentas são códigos que podem ser executados por um agente para realizar ações. Uma ferramenta pode ser uma função simples, como uma calculadora, ou uma chamada de API para um serviço de terceiros, como consulta de preço de ações ou previsão do tempo. No contexto de agentes de IA, as ferramentas são projetadas para serem executadas pelos agentes em resposta a **chamadas de função geradas pelo modelo**.

## Quais são os casos de uso aos quais ele pode ser aplicado?

Agentes de IA podem aproveitar ferramentas para completar tarefas complexas, recuperar informações ou tomar decisões. O padrão de design de uso de ferramentas é frequentemente usado em cenários que exigem interação dinâmica com sistemas externos, como bancos de dados, serviços web ou interpretadores de código. Essa capacidade é útil para diversos casos de uso, incluindo:

- **Recuperação Dinâmica de Informação:** Agentes podem consultar APIs externas ou bancos de dados para obter dados atualizados (por exemplo, consultar uma base SQLite para análise de dados, buscar preços de ações ou informações meteorológicas).
- **Execução e Interpretação de Código:** Agentes podem executar códigos ou scripts para resolver problemas matemáticos, gerar relatórios ou realizar simulações.
- **Automação de Fluxo de Trabalho:** Automatização de fluxos de trabalho repetitivos ou de múltiplas etapas, integrando ferramentas como agendadores de tarefas, serviços de e-mail ou pipelines de dados.
- **Suporte ao Cliente:** Agentes podem interagir com sistemas CRM, plataformas de tickets ou bases de conhecimento para resolver dúvidas dos usuários.
- **Geração e Edição de Conteúdo:** Agentes podem usar ferramentas como verificadores gramaticais, resumidores de texto ou avaliadores de segurança de conteúdo para ajudar em tarefas de criação.

## Quais são os elementos/blocos de construção necessários para implementar o padrão de design de uso de ferramentas?

Esses blocos de construção permitem que o agente de IA realize uma ampla variedade de tarefas. Vamos examinar os elementos-chave necessários para implementar o Padrão de Design de Uso de Ferramentas:

- **Esquemas de Função/Ferramenta**: Definições detalhadas das ferramentas disponíveis, incluindo nome da função, propósito, parâmetros necessários e saídas esperadas. Esses esquemas permitem que o LLM entenda quais ferramentas estão disponíveis e como construir solicitações válidas.

- **Lógica de Execução da Função**: Rege como e quando as ferramentas são invocadas com base na intenção do usuário e no contexto da conversa. Isso pode incluir módulos planejadores, mecanismos de roteamento ou fluxos condicionais que determinam dinamicamente o uso da ferramenta.

- **Sistema de Manipulação de Mensagens**: Componentes que gerenciam o fluxo conversacional entre entradas do usuário, respostas do LLM, chamadas de ferramentas e saídas das ferramentas.

- **Estrutura de Integração de Ferramentas**: Infraestrutura que conecta o agente a várias ferramentas, sejam elas funções simples ou serviços externos complexos.

- **Tratamento e Validação de Erros**: Mecanismos para lidar com falhas na execução das ferramentas, validar parâmetros e gerenciar respostas inesperadas.

- **Gerenciamento de Estado**: Acompanha o contexto da conversa, interações anteriores com ferramentas e dados persistentes para garantir consistência em interações de múltiplas etapas.

A seguir, vamos examinar o Chamado de Função/Ferramenta com mais detalhes.
 
### Chamado de Função/Ferramenta

O chamado de função é a principal forma pela qual habilitamos Modelos de Linguagem de Grande Escala (LLMs) a interagir com ferramentas. Frequentemente, você verá “Função” e “Ferramenta” usados de forma intercambiável porque “funções” (blocos de código reutilizáveis) são as “ferramentas” que agentes utilizam para realizar tarefas. Para que o código de uma função seja invocado, o LLM deve comparar a solicitação do usuário com a descrição das funções. Para isso, um esquema contendo as descrições de todas as funções disponíveis é enviado ao LLM. O LLM então seleciona a função mais apropriada para a tarefa e retorna seu nome e argumentos. A função selecionada é invocada, sua resposta é enviada de volta para o LLM, que usa essa informação para responder à solicitação do usuário.

Para que os desenvolvedores possam implementar o chamado de função para agentes, são necessários:

1. Um modelo LLM que suporte chamado de função
2. Um esquema contendo as descrições das funções
3. O código para cada função descrita

Vamos usar o exemplo de obter o horário atual em uma cidade para ilustrar:

1. **Inicializar um LLM que suporta chamado de função:**

    Nem todos os modelos suportam chamado de função, então é importante verificar se o LLM que você está utilizando o faz. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suporta chamado de função. Podemos começar iniciando o cliente Azure OpenAI.

    ```python
    # Inicializar o cliente Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Criar um Esquema de Função**:

    Em seguida, definiremos um esquema JSON que contém o nome da função, a descrição do que ela faz e os nomes e descrições dos parâmetros da função.
    Depois, passaremos esse esquema para o cliente criado anteriormente, junto com a solicitação do usuário para encontrar a hora em São Francisco. O que é importante notar é que uma **chamada de ferramenta** é o que é retornado, **não** a resposta final para a pergunta. Como mencionado anteriormente, o LLM retorna o nome da função que selecionou para a tarefa e os argumentos que serão passados para ela.

    ```python
    # Descrição da função para o modelo ler
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Mensagem inicial do usuário
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Primeira chamada da API: Peça ao modelo para usar a função
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Processar a resposta do modelo
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **O código da função necessário para realizar a tarefa:**

    Agora que o LLM escolheu qual função precisa ser executada, o código que realiza a tarefa precisa ser implementado e executado.
    Podemos implementar o código para obter o horário atual em Python. Também precisaremos escrever o código para extrair o nome e os argumentos da mensagem de resposta para obter o resultado final.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Lidar com chamadas de função
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Segunda chamada da API: Obter a resposta final do modelo
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

O Chamado de Função está no coração da maioria, senão de todo o design de uso de ferramentas para agentes, porém implementá-lo do zero pode às vezes ser desafiador.
Como aprendemos na [Lição 2](../../../02-explore-agentic-frameworks), frameworks agenticos nos fornecem blocos de construção pré-construídos para implementar o uso de ferramentas.
 
## Exemplos de Uso de Ferramentas com Frameworks Agenticos

Aqui estão alguns exemplos de como você pode implementar o Padrão de Design de Uso de Ferramentas usando diferentes frameworks agenticos:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> é um framework de código aberto para construir agentes de IA. Ele simplifica o processo de usar chamado de função permitindo que você defina ferramentas como funções Python com o decorador `@tool`. O framework gerencia a comunicação de ida e volta entre o modelo e seu código. Ele também fornece acesso a ferramentas pré-construídas como Busca de Arquivos e Interpretador de Código através do `AzureAIProjectAgentProvider`.

O diagrama a seguir ilustra o processo de chamado de função com o Microsoft Agent Framework:

![function calling](../../../translated_images/pt-BR/functioncalling-diagram.a84006fc287f6014.webp)

No Microsoft Agent Framework, ferramentas são definidas como funções decoradas. Podemos converter a função `get_current_time` que vimos antes em uma ferramenta usando o decorador `@tool`. O framework serializará automaticamente a função e seus parâmetros, criando o esquema para enviar ao LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Crie o cliente
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Crie um agente e execute com a ferramenta
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> é um framework agentico mais recente, projetado para capacitar desenvolvedores a construir, implantar e escalar agentes de IA de alta qualidade e extensíveis de forma segura, sem precisar gerenciar os recursos computacionais e de armazenamento subjacentes. É particularmente útil para aplicações empresariais, pois é um serviço totalmente gerenciado com segurança em nível empresarial.

Quando comparado ao desenvolvimento diretamente com a API do LLM, o Azure AI Agent Service oferece algumas vantagens, incluindo:

- Chamada automática de ferramentas – não é necessário analisar uma chamada de ferramenta, invocar a ferramenta e tratar a resposta; tudo isso agora é feito no servidor
- Dados gerenciados de forma segura – em vez de gerenciar seu próprio estado de conversa, você pode contar com threads para armazenar todas as informações necessárias
- Ferramentas prontas para uso – ferramentas que você pode usar para interagir com suas fontes de dados, como Bing, Azure AI Search e Azure Functions.

As ferramentas disponíveis no Azure AI Agent Service podem ser divididas em duas categorias:

1. Ferramentas de Conhecimento:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding com Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Busca de Arquivos</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Ferramentas de Ação:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Chamado de Função</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretador de Código</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Ferramentas definidas por OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

O Agent Service nos permite usar essas ferramentas juntas como um `conjunto de ferramentas`. Ele também utiliza `threads`, que acompanham o histórico de mensagens de uma conversa específica.

Imagine que você é um agente de vendas em uma empresa chamada Contoso. Você quer desenvolver um agente conversacional que possa responder a perguntas sobre seus dados de vendas.

A imagem a seguir ilustra como você poderia usar o Azure AI Agent Service para analisar seus dados de vendas:

![Agentic Service In Action](../../../translated_images/pt-BR/agent-service-in-action.34fb465c9a84659e.webp)

Para usar qualquer uma dessas ferramentas com o serviço, podemos criar um cliente e definir uma ferramenta ou um conjunto de ferramentas. Para implementar isso na prática, podemos usar o seguinte código Python. O LLM poderá analisar o conjunto de ferramentas e decidir se usa a função criada pelo usuário, `fetch_sales_data_using_sqlite_query`, ou o Interpretador de Código pré-construído, dependendo da solicitação do usuário.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # função fetch_sales_data_using_sqlite_query que pode ser encontrada no arquivo fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializar conjunto de ferramentas
toolset = ToolSet()

# Inicializar agente de chamada de função com a função fetch_sales_data_using_sqlite_query e adicioná-la ao conjunto de ferramentas
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializar ferramenta Code Interpreter e adicioná-la ao conjunto de ferramentas.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quais são as considerações especiais para usar o Padrão de Design de Uso de Ferramentas para construir agentes de IA confiáveis?

Uma preocupação comum com SQL gerado dinamicamente por LLMs é a segurança, particularmente o risco de injeção de SQL ou ações maliciosas, como excluir ou adulterar o banco de dados. Embora essas preocupações sejam válidas, elas podem ser efetivamente mitigadas configurando corretamente as permissões de acesso ao banco de dados. Para a maioria dos bancos de dados, isso envolve configurá-lo como leitura apenas. Para serviços de banco de dados como PostgreSQL ou Azure SQL, o aplicativo deve receber uma função somente leitura (SELECT).

Executar o aplicativo em um ambiente seguro melhora ainda mais a proteção. Em cenários empresariais, os dados são tipicamente extraídos e transformados de sistemas operacionais para um banco de dados somente leitura ou data warehouse com um esquema amigável ao usuário. Essa abordagem garante que os dados estejam seguros, otimizados para desempenho e acessibilidade, e que o aplicativo tenha acesso restrito e somente leitura.

## Códigos de Exemplo

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre o Padrão de Design de Uso de Ferramentas?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para se conectar com outros aprendizes, participar de horários de atendimento e esclarecer suas dúvidas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Visão Geral do Microsoft Agent Framework</a>

## Lição Anterior

[Entendendo Padrões de Design Agentes](../03-agentic-design-patterns/README.md)

## Próxima Lição
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->