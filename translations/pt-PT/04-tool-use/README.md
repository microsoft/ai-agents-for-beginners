[![Como Projetar Bons Agentes de IA](../../../translated_images/pt-PT/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Tool Use Design Pattern

As ferramentas são interessantes porque permitem que agentes de IA tenham um conjunto mais amplo de capacidades. Em vez de o agente ter um conjunto limitado de ações que pode executar, ao adicionar uma ferramenta, o agente pode agora executar uma ampla variedade de ações. Neste capítulo, vamos analisar o Tool Use Design Pattern, que descreve como agentes de IA podem usar ferramentas específicas para atingir os seus objetivos.

## Introduction

Nesta lição, procuramos responder às seguintes perguntas:

- O que é o tool use design pattern?
- Em que casos de uso pode ser aplicado?
- Quais são os elementos/blocos de construção necessários para implementar o padrão de design?
- Quais são as considerações especiais para usar o Tool Use Design Pattern para construir agentes de IA em que se possa confiar?

## Learning Goals

Após completar esta lição, será capaz de:

- Definir o Tool Use Design Pattern e o seu propósito.
- Identificar casos de uso em que o Tool Use Design Pattern é aplicável.
- Compreender os elementos-chave necessários para implementar o padrão de design.
- Reconhecer considerações para garantir a fiabilidade em agentes de IA que usam este padrão de design.

## What is the Tool Use Design Pattern?

O **Tool Use Design Pattern** foca-se em dar aos LLMs a capacidade de interagir com ferramentas externas para atingir objetivos específicos. Ferramentas são código que pode ser executado por um agente para realizar ações. Uma ferramenta pode ser uma função simples, como uma calculadora, ou uma chamada de API para um serviço de terceiros, como consulta de preços de ações ou previsão meteorológica. No contexto de agentes de IA, as ferramentas são concebidas para serem executadas por agentes em resposta a **model-generated function calls**.

## What are the use cases it can be applied to?

Os Agentes de IA podem aproveitar ferramentas para completar tarefas complexas, recuperar informação ou tomar decisões. O tool use design pattern é frequentemente usado em cenários que requerem interação dinâmica com sistemas externos, tais como bases de dados, serviços web ou interpretadores de código. Esta capacidade é útil para vários casos de uso, incluindo:

- **Recuperação Dinâmica de Informação:** Os agentes podem consultar APIs externas ou bases de dados para obter dados atualizados (ex.: consultar uma base de dados SQLite para análise de dados, obter preços de ações ou informações meteorológicas).
- **Execução e Interpretação de Código:** Os agentes podem executar código ou scripts para resolver problemas matemáticos, gerar relatórios ou realizar simulações.
- **Automatização de Fluxos de Trabalho:** Automatizar fluxos de trabalho repetitivos ou multi-etapa integrando ferramentas como agendadores de tarefas, serviços de e-mail ou pipelines de dados.
- **Apoio ao Cliente:** Os agentes podem interagir com sistemas CRM, plataformas de tickets ou bases de conhecimento para resolver dúvidas de utilizadores.
- **Geração e Edição de Conteúdo:** Os agentes podem utilizar ferramentas como verificadores gramaticais, sumarizadores de texto ou avaliadores de segurança de conteúdo para ajudar em tarefas de criação de conteúdo.

## What are the elements/building blocks needed to implement the tool use design pattern?

Estes blocos de construção permitem ao agente de IA realizar uma vasta gama de tarefas. Vamos ver os elementos-chave necessários para implementar o Tool Use Design Pattern:

- **Function/Tool Schemas**: Definições detalhadas das ferramentas disponíveis, incluindo nome da função, finalidade, parâmetros obrigatórios e saídas esperadas. Estes esquemas permitem ao LLM compreender que ferramentas estão disponíveis e como construir pedidos válidos.

- **Function Execution Logic**: Governa como e quando as ferramentas são invocadas com base na intenção do utilizador e no contexto da conversa. Isto pode incluir módulos de planeamento, mecanismos de encaminhamento ou fluxos condicionais que determinam o uso de ferramentas de forma dinâmica.

- **Message Handling System**: Componentes que gerem o fluxo conversacional entre entradas do utilizador, respostas do LLM, chamadas a ferramentas e saídas das ferramentas.

- **Tool Integration Framework**: Infraestrutura que liga o agente a várias ferramentas, quer sejam funções simples ou serviços externos complexos.

- **Error Handling & Validation**: Mecanismos para tratar falhas na execução das ferramentas, validar parâmetros e gerir respostas inesperadas.

- **State Management**: Regista o contexto da conversa, interações anteriores com ferramentas e dados persistentes para garantir consistência em interações multi-turno.

A seguir, vamos analisar a Function/Tool Calling com mais detalhe.
 
### Function/Tool Calling

A chamada de funções é a forma principal pela qual permitimos que os Large Language Models (LLMs) interajam com ferramentas. Verá frequentemente 'Function' e 'Tool' usados de forma intercambiável porque 'functions' (blocos de código reutilizáveis) são as 'tools' que os agentes usam para executar tarefas. Para que o código de uma função seja invocado, um LLM deve comparar o pedido do utilizador com a descrição das funções. Para fazer isto, um esquema contendo as descrições de todas as funções disponíveis é enviado ao LLM. O LLM seleciona então a função mais apropriada para a tarefa e devolve o seu nome e argumentos. A função selecionada é invocada, a sua resposta é enviada de volta ao LLM, que usa a informação para responder ao pedido do utilizador.

Para os desenvolvedores implementarem chamadas de função para agentes, irão precisar de:

1. Um modelo LLM que suporte function calling
2. Um esquema contendo descrições das funções
3. O código para cada função descrita

Vamos usar o exemplo de obter a hora atual numa cidade para ilustrar:

1. **Inicializar um LLM que suporte function calling:**

    Nem todos os modelos suportam function calling, por isso é importante verificar se o LLM que está a utilizar o faz.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suporta function calling. Podemos começar por iniciar o cliente Azure OpenAI. 

    ```python
    # Inicializar o cliente Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Criar um Function Schema**:

    De seguida definiremos um esquema JSON que contém o nome da função, a descrição do que a função faz, e os nomes e descrições dos parâmetros da função.
    Depois iremos mandar este esquema para o cliente criado anteriormente, juntamente com o pedido do utilizador para encontrar a hora em San Francisco. O que é importante notar é que é retornada uma **chamada de ferramenta**, **não** a resposta final à questão. Como mencionado anteriormente, o LLM devolve o nome da função que selecionou para a tarefa, e os argumentos que lhe serão passados.

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
  
    # Primeira chamada de API: Pedir ao modelo que use a função
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

    Agora que o LLM escolheu qual a função que precisa de ser executada, o código que realiza a tarefa precisa de ser implementado e executado.
    Podemos implementar o código para obter a hora atual em Python. Também será necessário escrever o código para extrair o nome e os argumentos da response_message para obter o resultado final.

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

A Function Calling está no centro da maior parte, senão de todo, o design de utilização de ferramentas de agentes, no entanto implementá-la a partir do zero pode por vezes ser um desafio.
Como aprendemos em [Lesson 2](../../../02-explore-agentic-frameworks) os frameworks agentic fornecem-nos blocos de construção pré-construídos para implementar a utilização de ferramentas.
 
## Tool Use Examples with Agentic Frameworks

Aqui estão alguns exemplos de como pode implementar o Tool Use Design Pattern usando diferentes frameworks agentic:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> é um framework de IA open-source para construir agentes de IA. Simplifica o processo de utilização de function calling ao permitir que defina ferramentas como funções Python com o decorador `@tool`. O framework gere a comunicação de ida e volta entre o modelo e o seu código. Também fornece acesso a ferramentas pré-construídas como File Search e Code Interpreter através do `AzureAIProjectAgentProvider`.

O diagrama seguinte ilustra o processo de chamada de função com o Microsoft Agent Framework:

![function calling](../../../translated_images/pt-PT/functioncalling-diagram.a84006fc287f6014.webp)

No Microsoft Agent Framework, as ferramentas são definidas como funções decoradas. Podemos converter a função `get_current_time` que vimos anteriormente numa ferramenta usando o decorador `@tool`. O framework irá serializar automaticamente a função e os seus parâmetros, criando o esquema a enviar ao LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> é um framework agentic mais recente projetado para capacitar os desenvolvedores a construir, implementar e escalar de forma segura agentes de IA de alta qualidade e extensíveis sem necessidade de gerir os recursos subjacentes de computação e armazenamento. É particularmente útil para aplicações empresariais, uma vez que é um serviço totalmente gerido com segurança de nível empresarial.

Comparado com o desenvolvimento direto com a API LLM, o Azure AI Agent Service fornece algumas vantagens, incluindo:

- Chamada automática de ferramentas – não é necessário analisar uma chamada de ferramenta, invocar a ferramenta e tratar a resposta; tudo isto é agora realizado server-side
- Dados geridos de forma segura – em vez de gerir o seu próprio estado de conversa, pode confiar em threads para armazenar toda a informação de que necessita
- Ferramentas prontas a usar – Ferramentas que pode utilizar para interagir com as suas fontes de dados, como Bing, Azure AI Search e Azure Functions.

As ferramentas disponíveis no Azure AI Agent Service podem ser divididas em duas categorias:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

O Agent Service permite-nos usar estas ferramentas em conjunto como um `toolset`. Também utiliza `threads` que mantêm o histórico de mensagens de uma determinada conversa.

Imagine que é um representante de vendas numa empresa chamada Contoso. Pretende desenvolver um agente conversacional que possa responder a perguntas sobre os seus dados de vendas.

A imagem seguinte ilustra como poderia usar o Azure AI Agent Service para analisar os seus dados de vendas:

![Agentic Service In Action](../../../translated_images/pt-PT/agent-service-in-action.34fb465c9a84659e.webp)

Para usar qualquer uma destas ferramentas com o serviço podemos criar um cliente e definir uma ferramenta ou conjunto de ferramentas. Para implementar isto na prática podemos usar o seguinte código Python. O LLM será capaz de olhar para o toolset e decidir se usa a função criada pelo utilizador, `fetch_sales_data_using_sqlite_query`, ou o Code Interpreter pré-construído dependendo do pedido do utilizador.

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

# Inicializar o conjunto de ferramentas
toolset = ToolSet()

# Inicializar um agente de invocação de funções com a função fetch_sales_data_using_sqlite_query e adicioná-lo ao conjunto de ferramentas
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializar a ferramenta Code Interpreter e adicioná-la ao conjunto de ferramentas.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## What are the special considerations for using the Tool Use Design Pattern to build trustworthy AI agents?

Uma preocupação comum com SQL gerado dinamicamente por LLMs é a segurança, particularmente o risco de injeção SQL ou ações maliciosas, como eliminar ou adulterar a base de dados. Embora estas preocupações sejam válidas, podem ser efetivamente mitigadas configurando corretamente as permissões de acesso à base de dados. Para a maioria das bases de dados, isto envolve configurar a base de dados como somente leitura. Para serviços de bases de dados como PostgreSQL ou Azure SQL, a aplicação deve ser atribuída a um papel de somente leitura (SELECT).

Executar a aplicação num ambiente seguro aumenta ainda mais a proteção. Em cenários empresariais, os dados são tipicamente extraídos e transformados a partir de sistemas operacionais para uma base de dados ou data warehouse de somente leitura com um esquema amigável ao utilizador. Esta abordagem garante que os dados estão seguros, otimizados para desempenho e acessibilidade, e que a aplicação tem acesso restrito e somente leitura.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conhecer outros aprendizes, assistir a horas de atendimento e esclarecer as suas dúvidas sobre Agentes de IA.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson
[RAG agentivo](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Isenção de responsabilidade:
Este documento foi traduzido utilizando o serviço de tradução por IA Co-op Translator (https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua original, deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional efetuada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->