[![Como Desenhar Bons Agentes de IA](../../../translated_images/pt-PT/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Padrão de Design para Utilização de Ferramentas

As ferramentas são interessantes porque permitem que os agentes de IA tenham um leque mais amplo de capacidades. Em vez de o agente ter um conjunto limitado de ações que pode executar, ao adicionar uma ferramenta, o agente pode agora realizar uma vasta gama de ações. Neste capítulo, vamos observar o Padrão de Design para Utilização de Ferramentas, que descreve como os agentes de IA podem usar ferramentas específicas para alcançar os seus objetivos.

## Introdução

Nesta lição, pretendemos responder às seguintes perguntas:

- O que é o padrão de design para utilização de ferramentas?
- Em que casos de uso pode ser aplicado?
- Quais os elementos/blocos de construção necessários para implementar o padrão de design?
- Quais as considerações especiais para usar o Padrão de Design para Utilização de Ferramentas para construir agentes de IA confiáveis?

## Objetivos de Aprendizagem

Após completar esta lição, será capaz de:

- Definir o Padrão de Design para Utilização de Ferramentas e o seu propósito.
- Identificar casos de uso em que o padrão é aplicável.
- Compreender os elementos-chave necessários para implementar o padrão de design.
- Reconhecer considerações para garantir a confiança em agentes de IA que utilizam este padrão.

## O que é o Padrão de Design para Utilização de Ferramentas?

O **Padrão de Design para Utilização de Ferramentas** foca-se em dar aos LLMs a capacidade de interagir com ferramentas externas para alcançar objetivos específicos. Ferramentas são código que pode ser executado por um agente para realizar ações. Uma ferramenta pode ser uma função simples como uma calculadora ou uma chamada de API para um serviço externo, como consulta de preço de ações ou previsão do tempo. No contexto de agentes de IA, as ferramentas são desenhadas para serem executadas por agentes em resposta a **chamadas de função geradas pelo modelo**.

## Em que casos de uso pode ser aplicado?

Os agentes de IA podem utilizar ferramentas para completar tarefas complexas, recuperar informação ou tomar decisões. O padrão de design para utilização de ferramentas é frequentemente usado em cenários que requerem interação dinâmica com sistemas externos, como bases de dados, serviços web ou interpretadores de código. Esta capacidade é útil para vários casos de uso, incluindo:

- **Recuperação Dinâmica de Informação:** Os agentes podem interrogar APIs externas ou bases de dados para obter dados atualizados (ex: consultar uma base de dados SQLite para análise de dados, obter preços das ações ou informações meteorológicas).
- **Execução e Interpretação de Código:** Os agentes podem executar código ou scripts para resolver problemas matemáticos, gerar relatórios ou realizar simulações.
- **Automação de Fluxos de Trabalho:** Automatizar fluxos de trabalho repetitivos ou multi-etapas integrando ferramentas como agendadores de tarefas, serviços de email ou pipelines de dados.
- **Suporte ao Cliente:** Os agentes podem interagir com sistemas CRM, plataformas de tickets ou bases de conhecimento para responder a perguntas dos utilizadores.
- **Geração e Edição de Conteúdo:** Os agentes podem usar ferramentas como corretor gramatical, resumidores de texto ou avaliadores de segurança de conteúdo para ajudar em tarefas de criação.

## Quais os elementos/blocos de construção necessários para implementar o padrão de design para utilização de ferramentas?

Estes blocos de construção permitem que o agente de IA realize uma ampla gama de tarefas. Vamos observar os principais elementos para implementar o Padrão de Design para Utilização de Ferramentas:

- **Esquemas de Funções/Ferramentas**: Definições detalhadas das ferramentas disponíveis, incluindo nome da função, propósito, parâmetros necessários e saídas esperadas. Estes esquemas permitem que o LLM compreenda que ferramentas estão disponíveis e como construir pedidos válidos.

- **Lógica de Execução das Funções**: Regula como e quando as ferramentas são invocadas, baseado na intenção do utilizador e no contexto da conversação. Isto pode incluir módulos de planeamento, mecanismos de roteamento ou fluxos condicionais que determinam o uso das ferramentas dinamicamente.

- **Sistema de Gestão de Mensagens**: Componentes que gerem o fluxo da conversação entre as entradas do utilizador, respostas do LLM, chamadas às ferramentas e as respostas das ferramentas.

- **Framework de Integração de Ferramentas**: Infraestrutura que conecta o agente a várias ferramentas, sejam elas funções simples ou serviços externos complexos.

- **Gestão de Erros e Validação**: Mecanismos para lidar com falhas na execução das ferramentas, validar parâmetros e gerir respostas inesperadas.

- **Gestão de Estado**: Rastreia o contexto da conversação, interações anteriores com ferramentas e dados persistentes para garantir consistência em interações multi-turno.

De seguida, vamos analisar em mais detalhe a Chamada de Funções/Ferramentas.
 
### Chamada de Função/Ferramenta

A chamada de função é a principal forma de permitir que os Modelos de Linguagem Grandes (LLMs) interajam com ferramentas. Frequentemente verá 'Função' e 'Ferramenta' usados como sinónimos porque 'funções' (blocos de código reutilizáveis) são as 'ferramentas' que os agentes usam para executar tarefas. Para que o código de uma função seja invocado, o LLM deve comparar o pedido do utilizador com a descrição das funções. Para tal, é enviado ao LLM um esquema que contém as descrições de todas as funções disponíveis. O LLM seleciona então a função mais apropriada para a tarefa e retorna o seu nome e argumentos. A função selecionada é invocada, a sua resposta é enviada de volta ao LLM, que usa essa informação para responder ao pedido do utilizador.

Para os desenvolvedores implementarem chamada de funções para agentes, será necessário:

1. Um modelo LLM que suporte chamada de funções.
2. Um esquema contendo descrições das funções.
3. O código para cada função descrita.

Vamos usar o exemplo de obter a hora atual numa cidade para ilustrar:

1. **Inicializar um LLM que suporte chamada de funções:**

    Nem todos os modelos suportam chamada de funções, por isso é importante verificar se o LLM que está a usar o faz. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suporta chamada de funções. Podemos começar por inicializar o cliente do Azure OpenAI.

    ```python
    # Inicializar o cliente Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Criar um Esquema de Função**:

    De seguida definiremos um esquema JSON que contém o nome da função, descrição do que a função faz, e os nomes e descrições dos parâmetros da função.
    Depois passamos este esquema para o cliente criado anteriormente, juntamente com o pedido do utilizador para obter a hora em São Francisco. O que é importante notar é que o que é retornado é uma **chamada a uma ferramenta**, **não** a resposta final à pergunta. Como mencionado anteriormente, o LLM retorna o nome da função que selecionou para a tarefa, e os argumentos que serão passados.

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
  
    # Primeira chamada à API: Peça ao modelo para usar a função
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
    Podemos implementar o código para obter a hora atual em Python. Também precisaremos de escrever o código para extrair o nome e os argumentos da response_message para obter o resultado final.

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
  
      # Segunda chamada de API: Obter a resposta final do modelo
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

A Chamada de Função é o centro de quase todo, se não todo, o design de uso de ferramentas em agentes, no entanto implementá-la do zero pode ser por vezes desafiante.
Como aprendemos na [Lição 2](../../../02-explore-agentic-frameworks), frameworks agenticos fornecem blocos de construção pré-construídos para implementar a utilização de ferramentas.
 
## Exemplos de Utilização de Ferramentas com Frameworks Agentes

Aqui estão alguns exemplos de como pode implementar o Padrão de Design para Utilização de Ferramentas usando diferentes frameworks agenticos:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> é um framework de IA open-source para desenvolvedores .NET, Python e Java que trabalham com Modelos de Linguagem Grandes (LLMs). Simplifica o processo de utilização da chamada de função ao descrever automaticamente as suas funções e os seus parâmetros para o modelo através de um processo chamado <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialização</a>. Também gere a comunicação bidirecional entre o modelo e o seu código. Outra vantagem de usar um framework agentico como o Semantic Kernel é que permite aceder a ferramentas pré-construídas como <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Pesquisa de Ficheiros</a> e <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpretador de Código</a>.

O seguinte diagrama ilustra o processo de chamada de funções com Semantic Kernel:

![function calling](../../../translated_images/pt-PT/functioncalling-diagram.a84006fc287f6014.webp)

No Semantic Kernel, funções/ferramentas são chamadas <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Podemos converter a função `get_current_time` que vimos anteriormente num plugin, transformando-a numa classe com a função dentro dela. Podemos também importar o decorator `kernel_function`, que recebe a descrição da função. Quando criar um kernel com o GetCurrentTimePlugin, o kernel irá automaticamente serializar a função e seus parâmetros, criando o esquema para enviar ao LLM no processo.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Criar o kernel
kernel = Kernel()

# Criar o plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Adicionar o plugin ao kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> é um framework agentico mais recente, concebido para capacitar os desenvolvedores a construir, implantar e escalar agentes de IA de alta qualidade e extensíveis de forma segura, sem necessidade de gerirem os recursos de computação e armazenamento subjacentes. É particularmente útil para aplicações empresariais, pois é um serviço totalmente gerido com segurança de nível empresarial.

Em comparação com o desenvolvimento direto com a API do LLM, o Azure AI Agent Service oferece algumas vantagens, incluindo:

- Chamada automática de ferramentas – não é necessário analisar uma chamada de ferramenta, invocar a ferramenta e gerir a resposta; tudo isso é feito no lado do servidor
- Dados geridos de forma segura – em vez de gerir o seu próprio estado da conversação, pode confiar nos threads para armazenar toda a informação necessária
- Ferramentas prontas a usar – ferramentas que pode utilizar para interagir com as suas fontes de dados, como Bing, Azure AI Search e Azure Functions.

As ferramentas disponíveis no Azure AI Agent Service podem ser divididas em duas categorias:

1. Ferramentas de Conhecimento:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Integração com Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pesquisa de Ficheiros</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Ferramentas de Ação:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Chamada de Funções</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretador de Código</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Ferramentas definidas por OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

O Agent Service permite-nos usar essas ferramentas em conjunto como um `conjunto de ferramentas` (`toolset`). Também utiliza `threads` que mantêm o histórico de mensagens de uma determinada conversação.

Imagine que é um agente de vendas numa empresa chamada Contoso. Quer desenvolver um agente conversacional que possa responder a perguntas sobre os seus dados de vendas.

A imagem a seguir ilustra como poderia usar o Azure AI Agent Service para analisar os seus dados de vendas:

![Agentic Service In Action](../../../translated_images/pt-PT/agent-service-in-action.34fb465c9a84659e.webp)

Para usar qualquer destas ferramentas com o serviço, podemos criar um cliente e definir uma ferramenta ou conjunto de ferramentas. Para implementar isto na prática, podemos usar o seguinte código Python. O LLM poderá olhar para o conjunto de ferramentas e decidir se usa a função criada pelo utilizador, `fetch_sales_data_using_sqlite_query`, ou o Interpretador de Código pré-construído dependendo do pedido do utilizador.

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

# Inicializar a ferramenta Code Interpreter e adicioná-la ao conjunto de ferramentas.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quais as considerações especiais para usar o Padrão de Design para Utilização de Ferramentas para construir agentes de IA confiáveis?

Uma preocupação comum com SQL dinamicamente gerado por LLMs é a segurança, particularmente o risco de injeção de SQL ou ações maliciosas, como eliminar ou alterar a base de dados. Embora estas preocupações sejam válidas, podem ser eficazmente mitigadas configurando corretamente as permissões de acesso à base de dados. Para a maioria das bases de dados, isso implica configurar a base de dados como de leitura apenas. Para serviços de base de dados como PostgreSQL ou Azure SQL, a aplicação deve ser atribuída a um papel de leitura apenas (SELECT).
Executar a aplicação num ambiente seguro reforça ainda mais a proteção. Em cenários empresariais, os dados são tipicamente extraídos e transformados a partir dos sistemas operacionais para uma base de dados ou armazém de dados somente leitura com um esquema amigável ao utilizador. Esta abordagem garante que os dados estão seguros, otimizados para desempenho e acessibilidade, e que a aplicação tem acesso restrito e somente leitura.

## Códigos de Exemplo

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre o Uso de Padrões de Design na Ferramenta?

Junte-se ao [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar em horas de expediente e obter respostas às suas perguntas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop do Serviço Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agente Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutorial de Chamada de Funções no Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpretador de Código Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Ferramentas Autogen</a>

## Lição Anterior

[Compreender os Padrões de Design Agentic](../03-agentic-design-patterns/README.md)

## Próxima Lição

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por inteligência artificial [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->