[![Como Projetar Bons Agentes de IA](../../../translated_images/pt-BR/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Padrão de Design de Uso de Ferramentas

Ferramentas são interessantes porque permitem que agentes de IA tenham um conjunto mais amplo de capacidades. Em vez de o agente ter um conjunto limitado de ações que pode realizar, ao adicionar uma ferramenta, o agente agora pode executar uma ampla variedade de ações. Neste capítulo, vamos olhar para o Padrão de Design de Uso de Ferramentas, que descreve como agentes de IA podem usar ferramentas específicas para alcançar seus objetivos.

## Introdução

Nesta lição, buscamos responder às seguintes perguntas:

- O que é o padrão de design de uso de ferramentas?
- Quais são os casos de uso aos quais pode ser aplicado?
- Quais são os elementos/blocos de construção necessários para implementar o padrão de design?
- Quais são as considerações especiais para usar o Padrão de Design de Uso de Ferramentas para construir agentes de IA confiáveis?

## Objetivos de Aprendizagem

Após concluir esta lição, você será capaz de:

- Definir o Padrão de Design de Uso de Ferramentas e seu propósito.
- Identificar casos de uso onde o Padrão de Design de Uso de Ferramentas é aplicável.
- Entender os elementos-chave necessários para implementar o padrão de design.
- Reconhecer considerações para garantir confiabilidade em agentes de IA que utilizam este padrão de design.

## O que é o Padrão de Design de Uso de Ferramentas?

O **Padrão de Design de Uso de Ferramentas** foca em dar aos LLMs a capacidade de interagir com ferramentas externas para alcançar objetivos específicos. Ferramentas são códigos que podem ser executados por um agente para realizar ações. Uma ferramenta pode ser uma função simples, como uma calculadora, ou uma chamada de API para um serviço de terceiros, como consulta de preço de ações ou previsão do tempo. No contexto de agentes de IA, ferramentas são projetadas para serem executadas por agentes em resposta a **chamadas de função geradas pelo modelo**.

## Quais são os casos de uso aos quais pode ser aplicado?

Agentes de IA podem usar ferramentas para concluir tarefas complexas, recuperar informações ou tomar decisões. O padrão de design de uso de ferramentas é frequentemente usado em cenários que requerem interação dinâmica com sistemas externos, como bancos de dados, serviços web ou interpretadores de código. Essa habilidade é útil para diversos casos de uso, incluindo:

- **Recuperação Dinâmica de Informações:** Agentes podem consultar APIs externas ou bancos de dados para obter dados atualizados (por exemplo, consultar um banco de dados SQLite para análise de dados, obter preços de ações ou informações meteorológicas).
- **Execução e Interpretação de Código:** Agentes podem executar códigos ou scripts para resolver problemas matemáticos, gerar relatórios ou realizar simulações.
- **Automação de Fluxos de Trabalho:** Automatizar fluxos de trabalho repetitivos ou com múltiplas etapas integrando ferramentas como agendadores de tarefas, serviços de email ou pipelines de dados.
- **Atendimento ao Cliente:** Agentes podem interagir com sistemas CRM, plataformas de atendimento a chamados ou bases de conhecimento para resolver dúvidas de usuários.
- **Geração e Edição de Conteúdo:** Agentes podem utilizar ferramentas como verificadores gramaticais, resumidores de texto ou avaliadores de segurança de conteúdo para auxiliar em tarefas de criação.

## Quais são os elementos/blocos de construção necessários para implementar o padrão de design de uso de ferramentas?

Esses blocos de construção permitem que o agente de IA realize uma gama ampla de tarefas. Vamos analisar os elementos-chave necessários para implementar o Padrão de Design de Uso de Ferramentas:

- **Esquemas de Funções/Ferramentas**: Definições detalhadas das ferramentas disponíveis, incluindo nome da função, propósito, parâmetros requeridos e saídas esperadas. Esses esquemas permitem que o LLM entenda quais ferramentas estão disponíveis e como construir requisições válidas.

- **Lógica de Execução das Funções**: Governa como e quando as ferramentas são invocadas com base na intenção do usuário e no contexto da conversa. Isso pode incluir módulos planejadores, mecanismos de roteamento ou fluxos condicionais que determinam o uso da ferramenta dinamicamente.

- **Sistema de Manipulação de Mensagens**: Componentes que gerenciam o fluxo conversacional entre entradas do usuário, respostas do LLM, chamadas de ferramentas e saídas das ferramentas.

- **Framework de Integração de Ferramentas**: Infraestrutura que conecta o agente às várias ferramentas, sejam funções simples ou serviços externos complexos.

- **Tratamento de Erros & Validação**: Mecanismos para lidar com falhas na execução de ferramentas, validar parâmetros e gerenciar respostas inesperadas.

- **Gerenciamento de Estado**: Acompanha o contexto da conversa, interações anteriores com ferramentas e dados persistentes para garantir consistência em interações multi-turno.

A seguir, vamos olhar em mais detalhes para a Chamada de Função/Ferramenta.
 
### Chamada de Função/Ferramenta

Chamada de função é a forma principal pela qual habilitamos os Modelos de Linguagem de Grande Porte (LLMs) a interagir com ferramentas. Frequentemente, vemos 'Função' e 'Ferramenta' usados de forma intercambiável porque 'funções' (blocos de código reutilizáveis) são as 'ferramentas' que agentes usam para realizar tarefas. Para que o código de uma função seja invocado, um LLM deve comparar a solicitação do usuário com a descrição das funções. Para isso, um esquema contendo as descrições de todas as funções disponíveis é enviado ao LLM. O LLM então seleciona a função mais apropriada para a tarefa e retorna seu nome e argumentos. A função selecionada é invocada, sua resposta é enviada de volta ao LLM, que usa a informação para responder à solicitação do usuário.

Para que desenvolvedores implementem a chamada de função para agentes, você precisará de:

1. Um modelo LLM que suporte chamada de função
2. Um esquema contendo as descrições das funções
3. O código para cada função descrita

Vamos usar o exemplo de obter o horário atual em uma cidade para ilustrar:

1. **Inicializar um LLM que suporte chamada de função:**

    Nem todos os modelos suportam chamada de função, então é importante verificar se o LLM que você está usando oferece esse recurso. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suporta chamada de função. Podemos começar iniciando o cliente Azure OpenAI.

    ```python
    # Inicialize o cliente Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Criar um Esquema de Função**:

    Em seguida, definiremos um esquema JSON que contém o nome da função, a descrição do que a função faz, e os nomes e descrições dos parâmetros da função.
    Depois, passaremos esse esquema para o cliente criado anteriormente, junto com a solicitação do usuário para encontrar o horário em San Francisco. O que é importante notar é que uma **chamada de ferramenta** é o que é retornado, **não** a resposta final à pergunta. Como mencionado antes, o LLM retorna o nome da função que selecionou para a tarefa e os argumentos que serão passados para ela.

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
  
    # Primeira chamada de API: Peça ao modelo para usar a função
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
  
1. **O código da função necessário para executar a tarefa:**

    Agora que o LLM escolheu qual função precisa ser executada, o código que realiza a tarefa precisa ser implementado e executado.
    Podemos implementar o código para obter o horário atual em Python. Também precisaremos escrever o código para extrair o nome e os argumentos da response_message para obter o resultado final.

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

A Chamada de Função está no cerne da maioria, se não de todos, os designs de uso de ferramentas para agentes; no entanto, implementá-la do zero pode às vezes ser desafiador.
Como aprendemos na [Lição 2](../../../02-explore-agentic-frameworks), frameworks agentic nos fornecem blocos de construção pré-construídos para implementar o uso de ferramentas.
 
## Exemplos de Uso de Ferramenta com Frameworks Agentic

Aqui estão alguns exemplos de como você pode implementar o Padrão de Design de Uso de Ferramentas usando diferentes frameworks agentic:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> é um framework de IA open-source para construir agentes de IA. Ele simplifica o processo de uso de chamada de função ao permitir que você defina ferramentas como funções Python com o decorador `@tool`. O framework gerencia a comunicação de ida e volta entre o modelo e seu código. Ele também fornece acesso a ferramentas pré-construídas como Pesquisa de Arquivos e Interpretador de Código através do `AzureAIProjectAgentProvider`.

O diagrama a seguir ilustra o processo de chamada de função com o Microsoft Agent Framework:

![chamada de função](../../../translated_images/pt-BR/functioncalling-diagram.a84006fc287f6014.webp)

No Microsoft Agent Framework, ferramentas são definidas como funções decoradas. Podemos converter a função `get_current_time` que vimos anteriormente em uma ferramenta usando o decorador `@tool`. O framework irá automaticamente serializar a função e seus parâmetros, criando o esquema para enviar ao LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Criar o cliente
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Criar um agente e executar com a ferramenta
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> é um framework agentic mais novo projetado para capacitar desenvolvedores a construir, implantar e escalar agentes de IA extensíveis, seguros e de alta qualidade sem precisar gerenciar recursos de computação e armazenamento subjacentes. É particularmente útil para aplicações empresariais, pois é um serviço totalmente gerenciado com segurança de nível corporativo.

Quando comparado ao desenvolvimento usando a API do LLM diretamente, o Azure AI Agent Service oferece algumas vantagens, incluindo:

- Chamada automática de ferramentas – não é necessário analisar uma chamada de ferramenta, invocar a ferramenta e lidar com a resposta; tudo isso é feito do lado do servidor
- Dados gerenciados com segurança – em vez de gerenciar seu próprio estado de conversa, você pode confiar em threads para armazenar todas as informações necessárias
- Ferramentas prontas para uso – ferramentas que você pode usar para interagir com suas fontes de dados, como Bing, Azure AI Search e Azure Functions.

As ferramentas disponíveis no Azure AI Agent Service podem ser divididas em duas categorias:

1. Ferramentas de Conhecimento:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding com Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pesquisa de Arquivos</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Ferramentas de Ação:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Chamada de Função</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretador de Código</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Ferramentas definidas por OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

O Agent Service nos permite usar essas ferramentas em conjunto como um `conjunto de ferramentas` (`toolset`). Ele também utiliza `threads`, que acompanham o histórico das mensagens de uma conversa específica.

Imagine que você é um agente de vendas em uma empresa chamada Contoso. Você quer desenvolver um agente conversacional que possa responder perguntas sobre seus dados de vendas.

A imagem a seguir ilustra como você poderia usar o Azure AI Agent Service para analisar seus dados de vendas:

![Agentic Service em ação](../../../translated_images/pt-BR/agent-service-in-action.34fb465c9a84659e.webp)

Para usar qualquer uma dessas ferramentas com o serviço, podemos criar um cliente e definir uma ferramenta ou conjunto de ferramentas. Para implementar isso praticamente, podemos usar o seguinte código em Python. O LLM poderá analisar o conjunto de ferramentas e decidir se usa a função criada pelo usuário, `fetch_sales_data_using_sqlite_query`, ou o Interpretador de Código pré-construído, dependendo da solicitação do usuário.

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
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quais são as considerações especiais para usar o Padrão de Design de Uso de Ferramentas para construir agentes de IA confiáveis?

Uma preocupação comum com SQL gerado dinamicamente por LLMs é a segurança, particularmente o risco de injeção de SQL ou ações maliciosas, como apagar ou adulterar o banco de dados. Embora essas preocupações sejam válidas, elas podem ser mitigadas efetivamente configurando corretamente as permissões de acesso ao banco de dados. Para a maioria dos bancos, isso envolve configurar o banco como somente leitura. Para serviços de banco de dados como PostgreSQL ou Azure SQL, o aplicativo deve ser atribuído a um papel somente leitura (SELECT).

Executar o aplicativo em um ambiente seguro melhora ainda mais a proteção. Em cenários empresariais, os dados geralmente são extraídos e transformados de sistemas operacionais para um banco de dados ou data warehouse somente leitura com um esquema amigável. Essa abordagem garante que os dados estejam seguros, otimizados para desempenho e acessibilidade, e que o aplicativo tenha acesso restrito e somente leitura.

## Exemplos de Código

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre o Padrão de Design de Uso de Ferramentas?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horários de atendimento e obter respostas para suas perguntas sobre agentes de IA.

## Recursos Adicionais

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agent Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Visão Geral do Microsoft Agent Framework</a>

## Lição Anterior

[Entendendo Padrões de Design Agentic](../03-agentic-design-patterns/README.md)

## Próxima Lição
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->