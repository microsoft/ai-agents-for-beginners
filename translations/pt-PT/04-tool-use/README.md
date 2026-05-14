[![Como Desenhar Bons Agentes de IA](../../../translated_images/pt-PT/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Clique na imagem acima para ver o vídeo desta aula)_

# Padrão de Design de Utilização de Ferramentas

As ferramentas são interessantes porque permitem que os agentes de IA tenham uma gama mais ampla de capacidades. Em vez do agente ter um conjunto limitado de ações que pode executar, ao adicionar uma ferramenta, o agente pode agora realizar uma vasta gama de ações. Neste capítulo, vamos analisar o Padrão de Design de Utilização de Ferramentas, que descreve como agentes de IA podem usar ferramentas específicas para atingir os seus objetivos.

## Introdução

Nesta lição, procuramos responder às seguintes perguntas:

- O que é o padrão de design de utilização de ferramentas?
- Quais são os casos de uso a que pode ser aplicado?
- Quais são os elementos/blocos de construção necessários para implementar o padrão de design?
- Quais são as considerações especiais para usar o Padrão de Design de Utilização de Ferramentas para construir agentes de IA confiáveis?

## Objetivos de Aprendizagem

Depois de concluir esta lição, será capaz de:

- Definir o Padrão de Design de Utilização de Ferramentas e o seu propósito.
- Identificar casos de uso onde o Padrão de Design de Utilização de Ferramentas é aplicável.
- Compreender os elementos-chave necessários para implementar o padrão de design.
- Reconhecer considerações para garantir a confiabilidade nos agentes de IA que usam este padrão de design.

## O que é o Padrão de Design de Utilização de Ferramentas?

O **Padrão de Design de Utilização de Ferramentas** foca-se em dar aos LLMs a capacidade de interagir com ferramentas externas para atingir objetivos específicos. Ferramentas são código que pode ser executado por um agente para realizar ações. Uma ferramenta pode ser uma função simples, como uma calculadora, ou uma chamada de API a um serviço externo, como consulta de preços de ações ou previsão do tempo. No contexto dos agentes de IA, as ferramentas são projetadas para serem executadas pelos agentes em resposta a **chamadas de funções geradas pelo modelo**.

## Quais são os casos de uso a que pode ser aplicado?

Os Agentes de IA podem aproveitar ferramentas para completar tarefas complexas, obter informação ou tomar decisões. O padrão de design de utilização de ferramentas é frequentemente usado em cenários que requerem interação dinâmica com sistemas externos, como bases de dados, serviços web ou interpretadores de código. Esta capacidade é útil para vários casos de uso diferentes, incluindo:

- **Recuperação Dinâmica de Informação:** Os agentes podem consultar APIs externas ou bases de dados para obter dados atualizados (por exemplo, consultar uma base de dados SQLite para análise de dados, obter preços de ações ou informações meteorológicas).
- **Execução e Interpretação de Código:** Os agentes podem executar código ou scripts para resolver problemas matemáticos, gerar relatórios ou realizar simulações.
- **Automação de Fluxo de Trabalho:** Automatizar fluxos de trabalho repetitivos ou multi-etapas integrando ferramentas como agendadores de tarefas, serviços de email ou pipelines de dados.
- **Suporte ao Cliente:** Os agentes podem interagir com sistemas CRM, plataformas de emissão de tickets ou bases de conhecimento para resolver questões dos utilizadores.
- **Geração e Edição de Conteúdo:** Os agentes podem utilizar ferramentas como corretores gramaticais, resumidores de texto ou avaliadores de segurança de conteúdo para ajudar nas tarefas de criação de conteúdo.

## Quais são os elementos/blocos de construção necessários para implementar o padrão de design de utilização de ferramentas?

Estes blocos de construção permitem que o agente de IA execute uma ampla gama de tarefas. Vamos ver os elementos chave necessários para implementar o Padrão de Design de Utilização de Ferramentas:

- **Esquemas de Função/Ferramenta**: Definições detalhadas das ferramentas disponíveis, incluindo nome da função, propósito, parâmetros requeridos e saídas esperadas. Estes esquemas permitem que o LLM compreenda que ferramentas estão disponíveis e como construir pedidos válidos.

- **Lógica de Execução de Funções**: Regula como e quando as ferramentas são invocadas com base na intenção do utilizador e no contexto da conversa. Pode incluir módulos de planeamento, mecanismos de roteamento ou fluxos condicionais que determinam a utilização da ferramenta de forma dinâmica.

- **Sistema de Gestão de Mensagens**: Componentes que gerem o fluxo conversacional entre entradas do utilizador, respostas do LLM, chamadas de ferramentas e saídas de ferramentas.

- **Framework de Integração de Ferramentas**: Infraestrutura que liga o agente a várias ferramentas, sejam funções simples ou serviços externos complexos.

- **Gestão de Erros & Validação**: Mecanismos para lidar com falhas na execução da ferramenta, validar parâmetros e gerir respostas inesperadas.

- **Gestão de Estado**: Rastreia o contexto da conversa, interações anteriores com ferramentas e dados persistentes para assegurar consistência ao longo de interações multi-turno.

De seguida, vamos analisar o Chamar Função/Ferramenta com mais detalhe.
 
### Chamar Função/Ferramenta

Chamar funções é a principal forma de permitir que os Modelos de Linguagem de Grande Escala (LLMs) interajam com ferramentas. Muitas vezes verá os termos 'Função' e 'Ferramenta' usados de forma intercambiável porque as 'funções' (blocos de código reutilizável) são as 'ferramentas' que os agentes usam para realizar tarefas. Para que o código de uma função seja invocado, um LLM deve comparar o pedido do utilizador com a descrição das funções. Para isso, é enviado ao LLM um esquema que contém as descrições de todas as funções disponíveis. O LLM seleciona então a função mais apropriada para a tarefa e retorna o seu nome e argumentos. A função selecionada é invocada, a sua resposta é enviada de volta ao LLM, que usa a informação para responder ao pedido do utilizador.

Para os desenvolvedores implementarem chamadas de funções para agentes, será necessário:

1. Um modelo LLM que suporte chamadas de funções
2. Um esquema contendo descrições das funções
3. O código para cada função descrita

Vamos usar o exemplo de obter a hora atual numa cidade para ilustrar:

1. **Inicializar um LLM que suporta chamada de função:**

    Nem todos os modelos suportam chamada de função, por isso é importante verificar se o LLM que está a usar suporta.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suporta chamada de função. Podemos começar por iniciar o cliente Azure OpenAI. 

    ```python
    # Inicializar o cliente Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Criar um Esquema de Função**:

    De seguida definimos um esquema JSON que contém o nome da função, descrição do que a função faz, e os nomes e descrições dos parâmetros da função.
    Depois pegamos neste esquema e passamo-lo para o cliente criado anteriormente, juntamente com o pedido do utilizador para encontrar a hora em São Francisco. O que é importante notar é que o que é retornado é uma **chamada de ferramenta**, **não** a resposta final à pergunta. Como mencionado anteriormente, o LLM retorna o nome da função que selecionou para a tarefa, e os argumentos que lhe serão passados.

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
  
    # Mensagem inicial do utilizador
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Primeira chamada à API: Solicitar ao modelo para usar a função
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

    Agora que o LLM escolheu qual a função que precisa ser executada, o código que realiza a tarefa precisa ser implementado e executado.
    Podemos implementar o código para obter a hora atual em Python. Também precisaremos de escrever o código para extrair o nome e argumentos da response_message para obter o resultado final.

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
     # Tratar chamadas de função
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
  
      # Segunda chamada à API: Obter a resposta final do modelo
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

Chamar funções está no coração da maioria, senão de todos, os projetos de uso de ferramentas em agentes, no entanto implementar isto do zero pode por vezes ser desafiante.
Como aprendemos na [Lição 2](../../../02-explore-agentic-frameworks) os frameworks agents fornecem-nos blocos de construção pré-construídos para implementar o uso de ferramentas.
 
## Exemplos de Utilização de Ferramentas com Frameworks Agentics

Aqui estão alguns exemplos de como pode implementar o Padrão de Design de Utilização de Ferramentas usando diferentes frameworks agents:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> é um framework de IA open-source para construir agentes de IA. Simplifica o processo de uso de chamadas de função ao permitir definir ferramentas como funções Python com o decorador `@tool`. O framework gere a comunicação entre o modelo e o seu código. Também fornece acesso a ferramentas pré-construídas como Pesquisa de Ficheiros e Interpretador de Código através do `AzureAIProjectAgentProvider`.

O diagrama seguinte ilustra o processo de chamada de função com o Microsoft Agent Framework:

![function calling](../../../translated_images/pt-PT/functioncalling-diagram.a84006fc287f6014.webp)

No Microsoft Agent Framework, as ferramentas são definidas como funções decoradas. Podemos converter a função `get_current_time` que vimos anteriormente numa ferramenta usando o decorador `@tool`. O framework vai automaticamente serializar a função e seus parâmetros, criando o esquema para enviar ao LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> é um framework agentic mais recente projetado para capacitar desenvolvedores a construir, implantar e escalar agentes de IA de alta qualidade e extensíveis de forma segura, sem necessitar gerir os recursos subjacentes de computação e armazenamento. É particularmente útil para aplicações empresariais, pois é um serviço totalmente gerido com segurança ao nível empresarial.

Quando comparado com o desenvolvimento direto com a API LLM, o Azure AI Agent Service oferece algumas vantagens, incluindo:

- Chamada automática de ferramentas – não é necessário analisar uma chamada de ferramenta, invocar a ferramenta e gerir a resposta; tudo isto é feito no lado do servidor
- Dados geridos de forma segura – em vez de gerir o estado da conversa, pode confiar nos threads para armazenar toda a informação necessária
- Ferramentas prontas a usar – ferramentas que pode usar para interagir com as suas fontes de dados, como Bing, Azure AI Search e Azure Functions.

As ferramentas disponíveis no Azure AI Agent Service podem ser divididas em duas categorias:

1. Ferramentas de Conhecimento:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Ancoragem com Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pesquisa de Ficheiros</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Ferramentas de Ação:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Chamada de Função</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretador de Código</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Ferramentas definidas por OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

O Agent Service permite utilizar estas ferramentas em conjunto como um `conjunto de ferramentas`. Utiliza também `threads` que rastreiam o histórico de mensagens de uma conversa particular.

Imagine que é um agente de vendas numa empresa chamada Contoso. Quer desenvolver um agente conversacional que possa responder a perguntas sobre os dados de vendas.

A imagem seguinte ilustra como pode usar o Azure AI Agent Service para analisar seus dados de vendas:

![Agentic Service In Action](../../../translated_images/pt-PT/agent-service-in-action.34fb465c9a84659e.webp)

Para usar qualquer destas ferramentas com o serviço podemos criar um cliente e definir uma ferramenta ou conjunto de ferramentas. Para implementar isto na prática, podemos usar o seguinte código Python. O LLM será capaz de analisar o conjunto de ferramentas e decidir se usa a função criada pelo utilizador, `fetch_sales_data_using_sqlite_query`, ou o Interpretador de Código pré-construído, dependendo do pedido do utilizador.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # função fetch_sales_data_using_sqlite_query que pode ser encontrada num ficheiro fetch_sales_data_functions.py.
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

## Quais são as considerações especiais para usar o Padrão de Design de Utilização de Ferramentas para construir agentes de IA confiáveis?

Uma preocupação comum com SQL gerado dinamicamente por LLMs é a segurança, particularmente o risco de injeção de SQL ou ações maliciosas, como eliminar ou manipular a base de dados. Embora estas preocupações sejam válidas, podem ser efetivamente mitigadas configurando corretamente as permissões de acesso à base de dados. Para a maioria das bases de dados, isto envolve configurar a base de dados como somente leitura. Para serviços de base de dados como PostgreSQL ou Azure SQL, a aplicação deve ser atribuída a um papel somente leitura (SELECT).

Executar a aplicação num ambiente seguro reforça ainda mais a proteção. Em cenários empresariais, os dados são tipicamente extraídos e transformados de sistemas operacionais para uma base de dados ou armazém de dados em modo somente leitura com um esquema amigável para o utilizador. Esta abordagem assegura que os dados estão seguros, otimizados para desempenho e acessibilidade, e que a aplicação tem acesso restrito e somente leitura.

## Códigos de Exemplo

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre os Padrões de Design de Utilização de Ferramentas?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar em sessões de assistência e esclarecer as suas dúvidas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop do Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Lição Anterior

[Compreendendo Padrões de Design Agentic](../03-agentic-design-patterns/README.md)

## Próxima Lição
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->