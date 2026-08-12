[![Como Projetar Bons Agentes de IA](../../../translated_images/pt-PT/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Clique na imagem acima para ver o vídeo desta aula)_

# Padrão de Design para Uso de Ferramentas

As ferramentas são interessantes porque permitem que os agentes de IA tenham um leque mais amplo de capacidades. Em vez de o agente ter um conjunto limitado de ações que pode realizar, ao adicionar uma ferramenta, o agente pode agora realizar uma ampla variedade de ações. Neste capítulo, iremos analisar o Padrão de Design para Uso de Ferramentas, que descreve como os agentes de IA podem usar ferramentas específicas para alcançar os seus objetivos.

## Introdução

Nesta aula, procuramos responder às seguintes perguntas:

- O que é o padrão de design para uso de ferramentas?
- Quais são os casos de uso a que pode ser aplicado?
- Quais são os elementos/blocos de construção necessários para implementar o padrão de design?
- Quais são as considerações especiais para usar o Padrão de Design para Uso de Ferramentas para construir agentes de IA confiáveis?

## Objetivos de Aprendizagem

Após completar esta aula, será capaz de:

- Definir o Padrão de Design para Uso de Ferramentas e o seu propósito.
- Identificar casos de uso onde o Padrão de Design para Uso de Ferramentas é aplicável.
- Compreender os elementos-chave necessários para implementar o padrão de design.
- Reconhecer as considerações para garantir a confiabilidade nos agentes de IA que usam este padrão de design.

## O que é o Padrão de Design para Uso de Ferramentas?

O **Padrão de Design para Uso de Ferramentas** concentra-se em dar aos LLMs a capacidade de interagir com ferramentas externas para atingir objetivos específicos. Ferramentas são códigos que podem ser executados por um agente para realizar ações. Uma ferramenta pode ser uma função simples, como uma calculadora, ou uma chamada de API para um serviço de terceiros, como consulta de preços de ações ou previsão do tempo. No contexto dos agentes de IA, as ferramentas são projetadas para serem executadas pelos agentes em resposta a **chamadas de função geradas pelo modelo**.

## A que casos de uso pode ser aplicado?

Os agentes de IA podem aproveitar ferramentas para completar tarefas complexas, recuperar informação ou tomar decisões. O padrão de design para uso de ferramentas é frequentemente usado em cenários que requerem interação dinâmica com sistemas externos, como bases de dados, serviços web ou interpretadores de código. Esta capacidade é útil para vários casos de uso diferentes, incluindo:

- **Recuperação Dinâmica de Informação:** Os agentes podem consultar APIs externas ou bases de dados para obter dados atualizados (por exemplo, consultar uma base de dados SQLite para análise de dados, obter preços de ações ou informação meteorológica).
- **Execução e Interpretação de Código:** Os agentes podem executar código ou scripts para resolver problemas matemáticos, gerar relatórios ou realizar simulações.
- **Automação de Fluxo de Trabalho:** Automatizar fluxos de trabalho repetitivos ou com várias etapas integrando ferramentas como agendadores de tarefas, serviços de email ou pipelines de dados.
- **Suporte ao Cliente:** Os agentes podem interagir com sistemas CRM, plataformas de tickets ou bases de conhecimento para resolver questões dos utilizadores.
- **Geração e Edição de Conteúdo:** Os agentes podem utilizar ferramentas como revisores gramaticais, sumariadores de texto ou avaliadores de segurança de conteúdo para auxiliar nas tarefas de criação de conteúdo.

## Quais são os elementos/blocos de construção necessários para implementar o padrão de design para uso de ferramentas?

Estes blocos de construção permitem ao agente de IA realizar uma ampla gama de tarefas. Vamos analisar os elementos-chave necessários para implementar o Padrão de Design para Uso de Ferramentas:

- **Esquemas de Funções/Ferramentas**: Definições detalhadas das ferramentas disponíveis, incluindo nome da função, propósito, parâmetros necessários e saídas esperadas. Estes esquemas permitem ao LLM compreender quais ferramentas estão disponíveis e como construir pedidos válidos.

- **Lógica de Execução da Função**: Regula como e quando as ferramentas são invocadas com base na intenção do utilizador e no contexto da conversa. Isto pode incluir módulos de planeamento, mecanismos de encaminhamento ou fluxos condicionais que determinam o uso dinâmico da ferramenta.

- **Sistema de Gestão de Mensagens**: Componentes que gerem o fluxo conversacional entre as entradas do utilizador, respostas do LLM, chamadas às ferramentas e resultados das ferramentas.

- **Framework de Integração de Ferramentas**: Infraestrutura que conecta o agente a diversas ferramentas, sejam funções simples ou serviços externos complexos.

- **Gestão de Erros e Validação**: Mecanismos para lidar com falhas na execução da ferramenta, validar parâmetros e gerir respostas inesperadas.

- **Gestão do Estado**: Rastreia o contexto da conversa, interações anteriores com ferramentas e dados persistentes para garantir a consistência em interações de múltiplas etapas.

De seguida, vamos analisar com mais detalhe a Chamada de Função/Ferramenta.
 
### Chamada de Função/Ferramenta

A chamada de função é a forma principal de permitir que os Modelos de Linguagem Grande (LLMs) interajam com ferramentas. Muitas vezes verá 'Função' e 'Ferramenta' usados como sinónimos porque 'funções' (blocos de código reutilizável) são as 'ferramentas' que os agentes usam para realizar tarefas. Para que o código de uma função seja invocado, um LLM deve comparar o pedido do utilizador com a descrição das funções. Para isso, um esquema contendo as descrições de todas as funções disponíveis é enviado ao LLM. O LLM então seleciona a função mais apropriada para a tarefa e devolve o seu nome e argumentos. A função selecionada é invocada, a sua resposta é enviada de volta ao LLM, que usa a informação para responder ao pedido do utilizador.

Para os desenvolvedores implementarem chamada de funções para agentes, será necessário:

1. Um modelo LLM que suporte chamada de funções
2. Um esquema contendo descrições das funções
3. O código para cada função descrita

Vamos usar o exemplo de obter a hora atual numa cidade para ilustrar:

1. **Inicializar um LLM que suporte chamada de funções:**

    Nem todos os modelos suportam chamada de funções, por isso é importante verificar se o LLM que está a usar suporta.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> suporta chamada de funções. Podemos começar por iniciar o cliente OpenAI contra a **API de Respostas** Azure OpenAI (o endpoint estável `/openai/v1/` — não é necessário `api_version`). 

    ```python
    # Inicializar o cliente OpenAI para Azure OpenAI (API Responses, endpoint v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Criar um Esquema de Função**:

    De seguida vamos definir um esquema JSON que contém o nome da função, descrição do que a função faz e os nomes e descrições dos parâmetros da função.
    Depois iremos passar este esquema para o cliente criado anteriormente, juntamente com o pedido do utilizador para encontrar a hora em São Francisco. O importante a notar é que é um **chamado de ferramenta** que é devolvido, **não** a resposta final à pergunta. Como mencionado anteriormente, o LLM devolve o nome da função que selecionou para a tarefa, juntamente com os argumentos que serão passados para ela.

    ```python
    # Descrição da função para o modelo ler (formato plano da ferramenta Responses API)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Mensagem inicial do utilizador
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Primeira chamada de API: Pedir ao modelo para usar a função
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # A API de Respostas devolve chamadas de ferramenta como itens function_call em response.output.
    # Acrescentá-las à conversa para que o modelo tenha o contexto completo na próxima interação.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **O código da função necessário para realizar a tarefa:**

    Agora que o LLM escolheu qual função precisa de ser executada, o código que realiza a tarefa precisa de ser implementado e executado.
    Podemos implementar o código para obter a hora atual em Python. Também precisaremos escrever o código para extrair o nome e os argumentos da resposta para obter o resultado final.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Retornar o resultado da ferramenta como um item function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Segunda chamada da API: Obter a resposta final do modelo
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

A Chamada de Função está no cerne de grande parte, se não de todo, o design para uso de ferramentas em agentes; no entanto, implementá-la do zero pode ser por vezes desafiante.
Como aprendemos na [Aula 2](../../../02-explore-agentic-frameworks), frameworks agenticos fornecem-nos blocos de construção pré-construídos para implementar o uso de ferramentas.
 
## Exemplos de Uso de Ferramentas com Frameworks Agenticos

Aqui estão alguns exemplos de como pode implementar o Padrão de Design para Uso de Ferramentas usando diferentes frameworks agenticos:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> é um framework de IA open-source para construir agentes de IA. Simplifica o processo de usar chamada de funções permitindo definir ferramentas como funções Python com o decorador `@tool`. O framework gere a comunicação entre o modelo e o seu código. Também fornece acesso a ferramentas pré-construídas como Pesquisa de Ficheiros e Interpretador de Código através do `FoundryChatClient`.

O diagrama seguinte ilustra o processo de chamada de função com o Microsoft Agent Framework:

![chamada de função](../../../translated_images/pt-PT/functioncalling-diagram.a84006fc287f6014.webp)

No Microsoft Agent Framework, as ferramentas são definidas como funções decoradas. Podemos converter a função `get_current_time` que vimos anteriormente numa ferramenta utilizando o decorador `@tool`. O framework irá automaticamente serializar a função e os seus parâmetros, criando o esquema a enviar para o LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Criar o cliente
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Criar um agente e executar com a ferramenta
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> é um framework agentico mais recente, projetado para capacitar desenvolvedores a construir, implantar e escalar agentes de IA extensíveis e de alta qualidade de forma segura, sem necessitarem de gerir os recursos subjacentes de computação e armazenamento. É particularmente útil para aplicações empresariais, uma vez que é um serviço totalmente gerido com segurança de nível empresarial.

Quando comparado ao desenvolvimento direto com a API LLM, o Microsoft Foundry Agent Service oferece algumas vantagens, incluindo:

- Chamada automática de ferramentas – não há necessidade de analisar chamadas de ferramentas, invocar a ferramenta e gerir a resposta; tudo isso é agora feito do lado do servidor.
- Dados geridos de forma segura – em vez de gerir o seu próprio estado da conversa, pode confiar em threads para armazenar toda a informação necessária.
- Ferramentas prontas a usar – Ferramentas que pode usar para interagir com as suas fontes de dados, como Bing, Azure AI Search e Azure Functions.

As ferramentas disponíveis no Microsoft Foundry Agent Service podem ser divididas em duas categorias:

1. Ferramentas de Conhecimento:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding com Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pesquisa de Ficheiros</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Ferramentas de Ação:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Chamada de Funções</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretador de Código</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Ferramentas definidas pela OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

O Agent Service permite-nos usar estas ferramentas juntas como um `toolset`. Também utiliza `threads` que mantêm o histórico das mensagens de uma determinada conversa.

Imagine que é um agente comercial numa empresa chamada Contoso. Quer desenvolver um agente conversacional que possa responder a perguntas sobre os seus dados de vendas.

A imagem seguinte ilustra como pode usar o Microsoft Foundry Agent Service para analisar os seus dados de vendas:

![Serviço Agente em Ação](../../../translated_images/pt-PT/agent-service-in-action.34fb465c9a84659e.webp)

Para usar alguma destas ferramentas com o serviço, podemos criar um cliente e definir uma ferramenta ou ferramenta-conjunto. Para implementar isso na prática, podemos usar o seguinte código Python. O LLM poderá analisar o conjunto de ferramentas e decidir se usa a função criada pelo utilizador, `fetch_sales_data_using_sqlite_query`, ou o interpretador de código pré-construído, dependendo do pedido do utilizador.

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
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quais são as considerações especiais para usar o Padrão de Design para Uso de Ferramentas para construir agentes de IA confiáveis?

Uma preocupação comum com SQL gerado dinamicamente por LLMs é a segurança, particularmente o risco de injeção SQL ou ações maliciosas, como apagar ou manipular a base de dados. Embora estas preocupações sejam válidas, podem ser efetivamente mitigadas configurando corretamente as permissões de acesso à base de dados. Para a maioria das bases de dados, isso implica configurar a base de dados como apenas leitura. Para serviços de base de dados como PostgreSQL ou Azure SQL, a aplicação deve ser atribuída a um papel apenas de leitura (SELECT).

Executar a aplicação num ambiente seguro reforça ainda mais a proteção. Em cenários empresariais, os dados são normalmente extraídos e transformados a partir de sistemas operacionais para uma base de dados ou armazém de dados apenas de leitura com um esquema amigável ao utilizador. Esta abordagem assegura que os dados são seguros, otimizados para desempenho e acessibilidade, e que a aplicação tem acesso restrito e apenas de leitura.

## Exemplos de Código

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Tem mais perguntas sobre os Padrões de Design para Uso de Ferramentas?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar em sessões de dúvidas e obter respostas às suas perguntas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop do Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agente Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Visão Geral do Microsoft Agent Framework</a>


## Teste Rápido deste Agente (Opcional)

Depois de aprender a implementar agentes em [Lição 16](../16-deploying-scalable-agents/README.md), pode fazer um teste rápido ao `TravelToolAgent` desta lição (ele ainda chama as suas ferramentas e responde?) com [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Veja [`tests/README.md`](../tests/README.md) para saber como executá-lo.

## Lição Anterior

[Compreendendo Padrões de Design Agênticos](../03-agentic-design-patterns/README.md)

## Próxima Lição

[RAG Agêntico](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->