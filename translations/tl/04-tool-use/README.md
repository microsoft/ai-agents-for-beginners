[![How to Design Good AI Agents](../../../translated_images/tl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

# Tool Use Design Pattern

Kawili-wili ang mga tool dahil nagbibigay-daan sila sa mga AI agent na magkaroon ng mas malawak na hanay ng kakayahan. Sa halip na ang agent ay may limitadong set ng mga aksyon na maaaring gawin, sa pamamagitan ng pagdaragdag ng isang tool, maaari na ngayong magsagawa ang agent ng malawak na hanay ng mga aksyon. Sa kabanatang ito, titingnan natin ang Tool Use Design Pattern, na naglalarawan kung paano makakagamit ang mga AI agent ng mga partikular na tool upang maabot ang kanilang mga layunin.

## Panimula

Sa araling ito, layunin nating sagutin ang mga sumusunod na tanong:

- Ano ang tool use design pattern?
- Ano ang mga kaso ng paggamit kung saan ito maaaring ilapat?
- Ano ang mga elemento/bloke ng gusali na kailangan upang maipatupad ang design pattern?
- Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern upang makabuo ng mapagkakatiwalaang AI agents?

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, magagawa mong:

- Tukuyin ang Tool Use Design Pattern at ang layunin nito.
- Kilalanin ang mga kaso ng paggamit kung saan maaari itong ilapat.
- Maunawaan ang mga pangunahing elemento na kailangan upang maipatupad ang design pattern.
- Matukoy ang mga konsiderasyon para matiyak ang mapagkakatiwalaan sa AI agents na gumagamit ng design pattern na ito.

## Ano ang Tool Use Design Pattern?

Ang **Tool Use Design Pattern** ay nakatuon sa pagbibigay sa LLMs ng kakayahang makipag-ugnayan sa mga panlabas na tool upang makamit ang mga partikular na layunin. Ang mga tool ay code na maaaring patakbuhin ng isang agent upang magsagawa ng mga aksyon. Ang isang tool ay maaaring isang simpleng function tulad ng calculator, o isang API call sa isang third-party na serbisyo tulad ng paghahanap ng presyo ng stock o forecast ng panahon. Sa konteksto ng AI agents, ang mga tool ay dinisenyo upang patakbuhin ng mga agent bilang tugon sa **model-generated function calls**.

## Ano ang mga kaso ng paggamit kung saan ito maaaring ilapat?

Maaaring samantalahin ng mga AI Agent ang mga tool upang tapusin ang mga komplikadong gawain, kumuha ng impormasyon, o gumawa ng mga desisyon. Madalas gamitin ang tool use design pattern sa mga sitwasyon na nangangailangan ng dynamic na pakikipag-ugnayan sa mga panlabas na sistema, tulad ng mga database, web services, o code interpreters. Kapaki-pakinabang ito sa maraming kaso ng paggamit kabilang ang:

- **Dynamic Information Retrieval:** Maaaring magtanong ang mga agent sa external APIs o database upang kumuha ng napapanahong data (hal., pagtatanong sa SQLite database para sa data analysis, pagkuha ng presyo ng stock o impormasyon ng panahon).
- **Code Execution and Interpretation:** Maaaring magpatakbo ang mga agent ng code o script upang lutasin ang mga problemang matematika, gumawa ng mga ulat, o magsagawa ng mga simulation.
- **Workflow Automation:** Awtomatikong pagsasagawa ng paulit-ulit o maraming-hakbang na workflow sa pamamagitan ng pagsasama ng mga tool tulad ng task schedulers, email services, o data pipelines.
- **Customer Support:** Maaaring makipag-ugnayan ang mga agent sa mga CRM system, ticketing platform, o knowledge base upang lutasin ang mga katanungan ng user.
- **Content Generation and Editing:** Maaaring gamitin ng mga agent ang mga tool tulad ng grammar checkers, text summarizers, o content safety evaluators upang makatulong sa paglikha ng nilalaman.

## Ano ang mga elemento/bloke ng gusali na kailangan upang maipatupad ang tool use design pattern?

Ang mga bloke ng gusali na ito ay nagpapahintulot sa AI agent na magsagawa ng malawak na hanay ng mga gawain. Tingnan natin ang mga pangunahing elemento na kinakailangan upang maipatupad ang Tool Use Design Pattern:

- **Function/Tool Schemas**: Detalyadong depinisyon ng mga magagamit na tool, kasama ang pangalan ng function, layunin, kailangang mga parameter, at inaasahang output. Pinapahintulutan ng mga schema na ito ang LLM na maunawaan kung ano ang mga magagamit na tool at kung paano bumuo ng wastong mga request.

- **Function Execution Logic**: Namamahala kung paano at kailan tatawagin ang mga tool base sa layunin ng gumagamit at konteksto ng pag-uusap. Maaari itong kabilang ang planner modules, mekanismo ng routing, o mga conditional na daloy na nagpapasya ng paggamit ng tool nang dinamiko.

- **Message Handling System**: Mga bahagi na namamahala sa daloy ng pag-uusap sa pagitan ng input ng user, mga tugon ng LLM, pagtawag sa tool, at output ng tool.

- **Tool Integration Framework**: Inprastruktura na nag-uugnay sa agent sa iba't ibang tool, maging ito man ay mga simpleng function o komplikadong panlabas na serbisyo.

- **Error Handling & Validation**: Mekanismo upang harapin ang mga pagkabigo sa pagpapatupad ng tool, patunayan ang mga parameter, at pamahalaan ang mga hindi inaasahang tugon.

- **State Management**: Nakakasubaybay sa konteksto ng pag-uusap, mga nakaraang interaksyon sa tool, at persistent na data upang matiyak ang pagkakapare-pareho sa mga multi-turn na interaksyon.

Susunod, tingnan natin nang mas detalyado ang Function/Tool Calling.
 
### Function/Tool Calling

Ang function calling ay ang pangunahing paraan kung paano pinapayagan nating makipag-ugnayan ang Large Language Models (LLMs) sa mga tool. Madalas mong marinig na ginagamit nang palitan ang 'Function' at 'Tool' dahil ang mga 'function' (mga bloke ng reusable na code) ay ang mga 'tool' na ginagamit ng mga agent upang isagawa ang mga gawain. Para matawag ang code ng isang function, kailangang ihambing ng LLM ang kahilingan ng gumagamit laban sa paglalarawan ng mga function. Para gawin ito, isinusumite ang isang schema na naglalaman ng mga paglalarawan ng lahat ng magagamit na function sa LLM. Pagkatapos ay pipili ang LLM ng pinaka-angkop na function para sa gawain at ibabalik ang pangalan nito at ang mga argumento. Tatawagin ang napiling function, at ang tugon nito ay ibabalik sa LLM, na gagamitin ang impormasyon upang tumugon sa kahilingan ng gumagamit.

Para sa mga developer upang maipatupad ang function calling para sa mga agent, kakailanganin mo:

1. Isang LLM model na sumusuporta sa function calling
2. Isang schema na naglalaman ng mga paglalarawan ng function
3. Ang code para sa bawat function na inilalarawan

Gamitin natin ang halimbawa ng pagkuha ng kasalukuyang oras sa isang lungsod upang ipakita:

1. **I-initialize ang LLM na sumusuporta sa function calling:**

    Hindi lahat ng modelo ay sumusuporta sa function calling, kaya mahalagang suriin kung sinusuportahan ito ng LLM na iyong ginagamit. Ang <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ay sumusuporta sa function calling. Maaari tayong magsimula sa pamamagitan ng pag-initialize ng Azure OpenAI client. 

    ```python
    # I-initialize ang Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Gumawa ng Function Schema**:

    Susunod, magtatalaga tayo ng JSON schema na naglalaman ng pangalan ng function, paglalarawan kung ano ang ginagawa ng function, at mga pangalan at paglalarawan ng mga parameter ng function.
    Ipasa natin ang schema na ito sa client na nilikha kanina, kasama ang kahilingan ng user upang malaman ang oras sa San Francisco. Ang mahalagang tandaan ay ang **tool call** ang ibinabalik, **hindi** ang panghuling sagot sa tanong. Tulad ng nabanggit, ibinabalik ng LLM ang pangalan ng function na pinili nito para sa gawain, at ang mga argumentong ipapasa dito.

    ```python
    # Paglalarawan ng function para basahin ng modelo
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

    Ngayong napili na ng LLM kung aling function ang kailangan patakbuhin, ang code na nagsasagawa ng gawain ay kailangang ipatupad at patakbuhin.
    Maaari nating ipatupad ang code para makuha ang kasalukuyang oras gamit ang Python. Kailangan din nating isulat ang code upang kunin ang pangalan at argumento mula sa response_message upang makuha ang pangwakas na resulta.

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
  
      # Pangalawang tawag sa API: Kunin ang huling sagot mula sa modelo
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

Ang Function Calling ay nasa puso ng karamihan, kung hindi man lahat, ng agent tool use design, ngunit minsan ay mahirap itong ipatupad mula sa simula.
Tulad ng natutunan natin sa [Lesson 2](../../../02-explore-agentic-frameworks), nagbibigay ang mga agentic framework ng mga pre-built na bloke ng gusali upang ipatupad ang tool use.
 
## Mga Halimbawa ng Tool Use gamit ang Agentic Frameworks

Narito ang ilang mga halimbawa kung paano mo maipapatupad ang Tool Use Design Pattern gamit ang iba't ibang agentic frameworks:

### Microsoft Agent Framework

Ang <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> ay isang open-source na AI framework para sa paggawa ng AI agents. Pinapadali nito ang proseso ng paggamit ng function calling sa pamamagitan ng pagpapahintulot sa'yo na tukuyin ang mga tool bilang Python functions gamit ang `@tool` decorator. Pinamamahalaan ng framework ang komunikasyon sa pagitan ng modelo at ng iyong code. Nagbibigay din ito ng access sa mga pre-built na tool tulad ng File Search at Code Interpreter sa pamamagitan ng `AzureAIProjectAgentProvider`.

Ipinapakita ng sumusunod na diagram ang proseso ng function calling gamit ang Microsoft Agent Framework:

![function calling](../../../translated_images/tl/functioncalling-diagram.a84006fc287f6014.webp)

Sa Microsoft Agent Framework, tinutukoy ang mga tool bilang mga dekoradong function. Maaari nating gawing tool ang `get_current_time` function na nakita kanina gamit ang `@tool` decorator. Awtomatikong ise-serialize ng framework ang function at mga parameter nito, na lumilikha ng schema upang ipadala sa LLM.

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

# Gumawa ng ahente at patakbuhin gamit ang tool
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

Ang <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ay isang mas bagong agentic framework na idinisenyo upang bigyang kapangyarihan ang mga developer na ligtas na makabuo, mag-deploy, at mag-scale ng mataas na kalidad, at extensible na AI agents nang hindi kinakailangang pamahalaan ang mga underlying compute at storage resources. Partikular itong kapaki-pakinabang para sa mga enterprise application dahil ito ay isang fully managed service na may enterprise grade security.

Kung ikukumpara sa direktang pag-develop gamit ang LLM API, nagbibigay ang Azure AI Agent Service ng ilang mga kalamangan, kabilang ang:

- Awtomatikong pagtawag ng tool – hindi na kailangang i-parse ang tool call, tawagin ang tool, at pamahalaan ang tugon; lahat ito ay ginagawa na ngayon sa server-side
- Ligtas na pinamamahalaang data – sa halip na pahalagahan ang iyong sariling estado ng pag-uusap, maaari kang umasa sa mga thread para itago ang lahat ng impormasyong kailangan mo
- Mga tools na handang gamitin – Mga tool na maaari mong gamitin para makipag-ugnayan sa iyong mga data source, tulad ng Bing, Azure AI Search, at Azure Functions.

Maaaring hatiin sa dalawang kategorya ang mga tool na available sa Azure AI Agent Service:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Pinapayagan tayo ng Agent Service na magamit ang mga tool na ito nang magkakasama bilang isang `toolset`. Gumagamit din ito ng `threads` na sumusubaybay sa kasaysayan ng mga mensahe mula sa isang partikular na pag-uusap.

Isipin mo na isang sales agent ka sa isang kumpanya na tinatawag na Contoso. Nais mong bumuo ng isang conversational agent na makakakasagot ng mga tanong tungkol sa iyong sales data.

Ipinapakita ng sumusunod na imahe kung paano mo magagamit ang Azure AI Agent Service upang suriin ang iyong sales data:

![Agentic Service In Action](../../../translated_images/tl/agent-service-in-action.34fb465c9a84659e.webp)

Para magamit ang alinman sa mga tool na ito sa serbisyo, maaari tayong gumawa ng client at tukuyin ang isang tool o toolset. Upang ipatupad ito nang praktikal, maaari nating gamitin ang sumusunod na Python code. Magagawa ng LLM na tingnan ang toolset at magpasya kung gagamitin ang user-created function na `fetch_sales_data_using_sqlite_query`, o ang pre-built Code Interpreter depende sa kahilingan ng user.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query na function na matatagpuan sa fetch_sales_data_functions.py na file.
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

# I-initialize ang Code Interpreter na tool at idagdag ito sa toolset.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern upang bumuo ng mapagkakatiwalaang AI agents?

Isang karaniwang alalahanin sa SQL na dinamiko na nilikha ng LLMs ay seguridad, partikular ang panganib ng SQL injection o malisyosong aksyon, tulad ng pag-drop o pagsira sa database. Bagaman tama ang mga alalahaning ito, maaaring epektibong mapigilan sa pamamagitan ng wastong pagkaka-konpigura ng mga database access permission. Para sa karamihan ng mga database, ito ay nangangahulugan ng pagkaka-konpigura ng database bilang read-only. Para sa mga database service gaya ng PostgreSQL o Azure SQL, dapat italaga ang app ng read-only (SELECT) role.

Ang pagpapatakbo ng app sa isang secure na kapaligiran ay lalo pang nagpapahusay ng proteksyon. Sa mga enterprise scenario, karaniwang iniu-extract at tinatransform ang data mula sa operational systems papunta sa isang read-only na database o data warehouse na may user-friendly na schema. Tinitiyak ng ganitong paraan na ang data ay ligtas, na-optimize para sa performance at accessibility, at may restrict na read-only access ang app.

## Mga Sample Code

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Nais Mo Pang Magtanong Tungkol sa Tool Use Design Patterns?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours, at sagutin ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang Mga Mapagkukunan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Nakaraang Aralin

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Susunod na Aralin
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->