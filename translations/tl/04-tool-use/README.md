[![How to Design Good AI Agents](../../../translated_images/tl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

# Tool Use Design Pattern

Kawili-wili ang mga tools dahil pinapayagan nila ang mga AI agent na magkaroon ng mas malawak na saklaw ng kakayahan. Sa halip na ang agent ay may limitadong set ng mga aksyon na maaari nitong gawin, sa pamamagitan ng pagdaragdag ng isang tool, maaari na ngayong magsagawa ang agent ng malawak na hanay ng mga aksyon. Sa kabanatang ito, titingnan natin ang Tool Use Design Pattern, na naglalarawan kung paano magagamit ng mga AI agent ang mga partikular na tools upang makamit ang kanilang mga layunin.

## Panimula

Sa araling ito, nais nating sagutin ang mga sumusunod na tanong:

- Ano ang tool use design pattern?
- Ano ang mga use case na maaaring ilapat dito?
- Ano ang mga elemento/mga building block na kailangan upang maipatupad ang design pattern?
- Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern upang makabuo ng mga mapagkakatiwalaang AI agent?

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, magagawa mong:

- I-define ang Tool Use Design Pattern at ang layunin nito.
- Kilalanin ang mga use case kung saan ang Tool Use Design Pattern ay angkop.
- Maunawaan ang mga pangunahing elemento na kailangan upang maipatupad ang design pattern.
- Makilala ang mga konsiderasyon para sa pagtitiyak ng mapagkakatiwalaang AI agent gamit ang design pattern na ito.

## Ano ang Tool Use Design Pattern?

Ang **Tool Use Design Pattern** ay nakatuon sa pagbibigay ng kakayahan sa mga LLM na makipag-ugnayan sa mga external na tool upang makamit ang mga partikular na layunin. Ang mga tools ay mga code na maaaring patakbuhin ng isang agent upang magsagawa ng mga aksyon. Ang tool ay maaaring isang simpleng function tulad ng calculator, o isang API call sa isang third-party na serbisyo tulad ng pagtingin sa presyo ng stock o forecast ng panahon. Sa konteksto ng mga AI agent, ang mga tool ay dinisenyo upang maipatupad ng mga agent bilang tugon sa **model-generated function calls**.

## Ano ang mga use case na maaaring ilapat dito?

Maaaring gamitin ng mga AI Agent ang mga tools upang makumpleto ang mga komplikadong gawain, kumuha ng impormasyon, o gumawa ng mga desisyon. Ang tool use design pattern ay madalas gamitin sa mga scenario na nangangailangan ng dynamic na interaksyon sa mga external na sistema, tulad ng databases, web services, o code interpreters. Ang kakayahang ito ay kapaki-pakinabang para sa iba't-ibang use case kabilang ang:

- **Dynamic Information Retrieval:** Maaaring mag-query ang mga agent sa mga external API o databases upang kumuha ng pinaka-sariwang datos (hal., pag-query sa SQLite database para sa data analysis, pagkuha ng presyo ng stock o impormasyon ng panahon).
- **Code Execution and Interpretation:** Maaaring magsagawa ng code o script ang mga agent upang lutasin ang mga matematikal na problema, gumawa ng mga ulat, o magsagawa ng mga simulation.
- **Workflow Automation:** Pag-automate ng mga paulit-ulit o multi-step na mga workflow sa pamamagitan ng integrasyon ng mga tools tulad ng task schedulers, email services, o data pipelines.
- **Customer Support:** Nakikipag-interact ang mga agent sa mga CRM system, ticketing platforms, o knowledge bases upang lutasin ang mga tanong ng user.
- **Content Generation and Editing:** Maaari gamitin ng mga agent ang mga tools tulad ng grammar checkers, text summarizers, o content safety evaluators upang tumulong sa paggawa ng nilalaman.

## Ano ang mga elemento/mga building block na kailangan upang maipatupad ang tool use design pattern?

Ang mga building block na ito ay nagpapahintulot sa AI agent na magsagawa ng malawak na hanay ng mga gawain. Tingnan natin ang mga pangunahing elemento na kailangan upang maipatupad ang Tool Use Design Pattern:

- **Function/Tool Schemas**: Detalyadong mga depinisyon ng mga available na tool, kabilang ang pangalan ng function, layunin, kailangang mga parameter, at inaasahang mga output. Pinapayagan ng mga schema na ito ang LLM na maunawaan kung anong mga tool ang available at kung paano bumuo ng balidong mga kahilingan.

- **Function Execution Logic**: Namamahala kung paano at kailan tinatawag ang mga tool base sa intensyon ng user at konteksto ng pag-uusap. Maaaring kabilang dito ang mga planner module, mekanismo sa pag-route, o mga kondisyonal na daloy na nagde-determine ng paggamit ng tool nang dynamic.

- **Message Handling System**: Mga bahagi na namamahala sa daloy ng pag-uusap sa pagitan ng input ng user, mga tugon ng LLM, mga tawag sa tool, at mga output ng tool.

- **Tool Integration Framework**: Impraestruktura na nag-uugnay sa agent sa iba’t ibang tools, maging ito man ay simpleng mga function o kumplikadong external na serbisyo.

- **Error Handling & Validation**: Mga mekanismo para harapin ang mga pagkabigo sa pagpapatakbo ng tool, i-validate ang mga parameter, at pamahalaan ang hindi inaasahang mga tugon.

- **State Management**: Sinusubaybayan ang konteksto ng pag-uusap, mga nakaraang interaksyon sa tool, at persistent na data upang matiyak ang konsistensi sa maraming turn ng interaksyon.

Susunod, titingnan natin ang Function/Tool Calling nang mas detalyado.

### Function/Tool Calling

Ang function calling ay ang pangunahing paraan kung paano natin pinapayagan ang Large Language Models (LLMs) na makipag-ugnayan sa mga tools. Madalas mong marinig na 'Function' at 'Tool' ay ginagamit na palitan dahil ang 'functions' (mga block ng reusable code) ay ang 'tools' na ginagamit ng mga agent para isagawa ang mga gawain. Para matawag ang code ng isang function, kailangang ikumpara ng LLM ang kahilingan ng user sa deskripsyon ng mga function. Para gawin ito, ipinapadala ang isang schema na naglalaman ng mga deskripsyon ng lahat ng available na function sa LLM. Pinipili ng LLM ang pinaka-angkop na function para sa gawain at ibinabalik ang pangalan at mga argumento nito. Tinatawag ang napiling function, at ang tugon nito ay ibinabalik sa LLM, na gagamitin ang impormasyon upang tugunan ang kahilingan ng user.

Para sa mga developer na gustong mag-implement ng function calling para sa mga agent, kakailanganin mo:

1. Isang LLM model na sumusuporta sa function calling
2. Isang schema na naglalaman ng mga deskripsyon ng function
3. Ang code para sa bawat function na inilalarawan

Gamitin natin ang halimbawa ng pagkuha ng kasalukuyang oras sa isang lungsod upang ipakita:

1. **I-initialize ang isang LLM na sumusuporta sa function calling:**

    Hindi lahat ng modelo ay sumusuporta sa function calling, kaya mahalagang suriin na ang LLM na ginagamit mo ay may ganitong kakayahan. Ang <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ay sumusuporta sa function calling. Maaari nating simulan sa pamamagitan ng pag-initialize ng Azure OpenAI client.

    ```python
    # I-initialize ang Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Gumawa ng Function Schema**:

    Sunod nating ide-define ang isang JSON schema na naglalaman ng pangalan ng function, deskripsyon ng ginagawa ng function, at mga pangalan at deskripsyon ng mga parameter ng function.
    Ipasa natin ang schema na ito sa client na ginawa kanina, kasama ang kahilingan ng user upang malaman ang oras sa San Francisco. Ang mahalagang tandaan ay ang **tool call** ang ibinabalik, **hindi** ang huling sagot sa tanong. Tulad ng nabanggit kanina, ibinabalik ng LLM ang pangalan ng function na pinili nito para sa gawain, at ang mga argumentong ipapasa dito.

    ```python
    # Paglalarawan ng function para mabasa ng modelo
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
  
    # Paunang mensahe ng gumagamit
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Unang tawag sa API: Hilingin sa modelo na gamitin ang function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Proseso ng tugon ng modelo
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Ang code ng function na kailangan upang maisagawa ang gawain:**

    Ngayong napili na ng LLM kung aling function ang kailangang patakbuhin, kailangang ipatupad at patakbuhin ang code na nagsasagawa ng gawain.
    Maaari nating ipatupad ang code upang makuha ang kasalukuyang oras gamit ang Python. Kailangan din natin isulat ang code upang kunin ang pangalan at mga argumento mula sa response_message upang makuha ang huling resulta.

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
     # Pamahalaan ang mga tawag sa function
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
  
      # Pangalawang tawag sa API: Kunin ang huling tugon mula sa modelo
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

Ang Function Calling ay nasa puso ng karamihan, kung hindi man lahat, ng agent tool use design, subalit minsan nakakahirap itong ipatupad mula sa simula.
Tulad ng natutunan natin sa [Lesson 2](../../../02-explore-agentic-frameworks), nagbibigay ang mga agentic framework ng pre-built na mga building block upang maipatupad ang tool use.

## Mga Halimbawa ng Tool Use gamit ang Agentic Frameworks

Narito ang ilang halimbawa kung paano mo maipatutupad ang Tool Use Design Pattern gamit ang iba't ibang agentic frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> ay isang open-source AI framework para sa paggawa ng mga AI agent. Pinapasimple nito ang proseso ng paggamit ng function calling sa pamamagitan ng pagpapahintulot na ideklara ang tools bilang mga Python function gamit ang `@tool` decorator. Pinamamahalaan ng framework ang komunikasyon sa pagitan ng modelo at ng iyong code. Nagbibigay din ito ng access sa mga pre-built na tool tulad ng File Search at Code Interpreter sa pamamagitan ng `AzureAIProjectAgentProvider`.

Ipinapakita ng sumusunod na diagram ang proseso ng function calling gamit ang Microsoft Agent Framework:

![function calling](../../../translated_images/tl/functioncalling-diagram.a84006fc287f6014.webp)

Sa Microsoft Agent Framework, ang mga tool ay dinideklara bilang mga partidong diniseta na function. Maaari nating gawing tool ang `get_current_time` function na nakita natin kanina gamit ang `@tool` decorator. Awtomatikong isinaserialisa ng framework ang function at ang mga parameter nito, na lumilikha ng schema para ipadala sa LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Gumawa ng kliyente
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Gumawa ng ahente at patakbuhin gamit ang kasangkapan
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

Ang <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ay isang mas bagong agentic framework na nilikha upang bigyan ang mga developer ng kapangyarihang magtayo, mag-deploy, at mag-scale ng mga high-quality at extensible na AI agent nang ligtas, nang hindi kinakailangang pamahalaan ang mga underlying compute at storage resources. Lalo na itong kapaki-pakinabang para sa mga enterprise application dahil ito ay isang fully managed service na may enterprise grade na seguridad.

Kung ikukumpara sa direktang pag-develop gamit ang LLM API, nag-aalok ang Azure AI Agent Service ng ilang kalamangan, kabilang ang:

- Awtomatikong tool calling – hindi na kailangang i-parse ang tool call, tawagin ang tool, at pangasiwaan ang tugon; lahat ng ito ay ginagawa server-side
- Ligtas na pinangangasiwaan ang data – sa halip na pamahalaan ang sariling estado ng pag-uusap, maaari kang umasa sa threads para itago ang lahat ng kinakailangang impormasyon
- Mga tool na handang gamitin – Mga tool na maaari mong gamitin upang makipag-ugnayan sa iyong mga data source, tulad ng Bing, Azure AI Search, at Azure Functions.

Ang mga tool na available sa Azure AI Agent Service ay maaaring hatiin sa dalawang kategorya:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding sa Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Mga OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Pinapayagan tayo ng Agent Service na magamit ang mga tool na ito nang sabay bilang isang `toolset`. Ginagamit din nito ang `threads` na nagtatrack ng kasaysayan ng mga mensahe mula sa isang partikular na pag-uusap.

Isipin na ikaw ay isang sales agent sa isang kumpanyang tinatawag na Contoso. Nais mong bumuo ng isang conversational agent na makakasagot ng mga tanong tungkol sa iyong sales data.

Ipinapakita ng sumusunod na larawan kung paano mo magagamit ang Azure AI Agent Service upang suriin ang iyong sales data:

![Agentic Service In Action](../../../translated_images/tl/agent-service-in-action.34fb465c9a84659e.webp)

Upang magamit ang alinmang mga tool na ito sa serbisyo, maaari tayong gumawa ng client at magdeklara ng tool o toolset. Para sa praktikal na implementasyon, maaari nating gamitin ang sumusunod na Python code. Magagawa ng LLM na tumingin sa toolset at magpasya kung gagamitin ang user-created function, `fetch_sales_data_using_sqlite_query`, o ang pre-built Code Interpreter depende sa kahilingan ng user.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query na function na matatagpuan sa isang fetch_sales_data_functions.py na file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# I-initialize ang toolset
toolset = ToolSet()

# I-initialize ang function calling agent gamit ang fetch_sales_data_using_sqlite_query na function at idagdag ito sa toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# I-initialize ang Code Interpreter tool at idagdag ito sa toolset.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern upang makabuo ng mapagkakatiwalaang AI agent?

Isang karaniwang alalahanin tungkol sa dinamikong SQL na ginagawa ng LLMs ay ang seguridad, partikular ang panganib ng SQL injection o malisyosong aksyon, tulad ng pag-drop o pagbabago ng database. Bagamat makatwiran ang mga alalahaning ito, epektibong nae- mitigate ang mga ito sa tamang pag-configure ng access permissions sa database. Para sa karamihan ng mga database, ito ay nangangailangan ng pag-configure ng database bilang read-only. Para sa mga database service tulad ng PostgreSQL o Azure SQL, dapat na italaga sa app ang isang read-only (SELECT) na role.

Ang pagpapatakbo ng app sa isang secure na kapaligiran ay lalo pang nagpapahusay ng proteksyon. Sa mga enterprise scenario, karaniwang kinukuha at binabago ang data mula sa mga operational system papunta sa isang read-only database o data warehouse na may user-friendly na schema. Tinitiyak ng pamamaraang ito na ang data ay ligtas, na-optimize para sa performance at accessibility, at ang app ay may limitadong access lang na read-only.

## Mga Halimbawang Code

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## May Karagdagang Tanong tungkol sa Tool Use Design Patterns?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours, at sagutin ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang mga Mapagkukunan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pangkalahatang-ideya ng Microsoft Agent Framework</a>

## Nakaraang Aralin

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Susunod na Aralin
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang awtomatikong pagsasalin ay maaaring magkaroon ng mga kamalian o pagkukulang. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinakapinagkakatiwalaang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->