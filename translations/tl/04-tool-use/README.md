<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e056335d729ba6e49571db7a6533825d",
  "translation_date": "2025-09-30T07:34:44+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "tl"
}
-->
[![Paano Magdisenyo ng Magandang AI Agents](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.tl.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(I-click ang imahe sa itaas para mapanood ang video ng araling ito)_

# Tool Use Design Pattern

Ang mga tool ay kawili-wili dahil pinapayagan nila ang mga AI agents na magkaroon ng mas malawak na hanay ng kakayahan. Sa halip na limitado ang mga aksyon na maaaring gawin ng agent, sa pamamagitan ng pagdaragdag ng tool, maaari na nitong gawin ang mas maraming uri ng aksyon. Sa kabanatang ito, tatalakayin natin ang Tool Use Design Pattern, na naglalarawan kung paano maaaring gumamit ng mga partikular na tool ang mga AI agents upang maabot ang kanilang mga layunin.

## Panimula

Sa araling ito, susubukan nating sagutin ang mga sumusunod na tanong:

- Ano ang tool use design pattern?
- Ano ang mga use case na maaaring gamitan nito?
- Ano ang mga elemento o building blocks na kailangan upang maipatupad ang design pattern?
- Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern para makabuo ng mapagkakatiwalaang AI agents?

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, magagawa mo ang sumusunod:

- Tukuyin ang Tool Use Design Pattern at ang layunin nito.
- Kilalanin ang mga use case kung saan naaangkop ang Tool Use Design Pattern.
- Maunawaan ang mga pangunahing elemento na kailangan upang maipatupad ang design pattern.
- Kilalanin ang mga konsiderasyon para matiyak ang tiwala sa AI agents na gumagamit ng design pattern na ito.

## Ano ang Tool Use Design Pattern?

Ang **Tool Use Design Pattern** ay nakatuon sa pagbibigay ng kakayahan sa LLMs na makipag-ugnayan sa mga panlabas na tool upang maabot ang mga partikular na layunin. Ang mga tool ay code na maaaring i-execute ng isang agent upang magsagawa ng mga aksyon. Ang isang tool ay maaaring simpleng function tulad ng calculator, o isang API call sa third-party service tulad ng pagkuha ng presyo ng stock o forecast ng panahon. Sa konteksto ng AI agents, ang mga tool ay idinisenyo upang i-execute ng mga agents bilang tugon sa **model-generated function calls**.

## Ano ang mga use case na maaaring gamitan nito?

Maaaring gamitin ng AI Agents ang mga tool upang makumpleto ang mga kumplikadong gawain, kumuha ng impormasyon, o gumawa ng desisyon. Ang tool use design pattern ay madalas na ginagamit sa mga sitwasyong nangangailangan ng dynamic na interaksyon sa mga panlabas na sistema, tulad ng databases, web services, o code interpreters. Ang kakayahang ito ay kapaki-pakinabang para sa iba't ibang use case kabilang ang:

- **Dynamic Information Retrieval:** Maaaring mag-query ang mga agents sa mga panlabas na API o databases upang makuha ang pinakabagong data (hal., pag-query sa SQLite database para sa data analysis, pagkuha ng presyo ng stock o impormasyon ng panahon).
- **Code Execution and Interpretation:** Maaaring mag-execute ng code o scripts ang mga agents upang lutasin ang mga problemang matematikal, gumawa ng mga ulat, o magsagawa ng mga simulation.
- **Workflow Automation:** Pag-automate ng mga paulit-ulit o multi-step na workflows sa pamamagitan ng pagsasama ng mga tool tulad ng task schedulers, email services, o data pipelines.
- **Customer Support:** Maaaring makipag-ugnayan ang mga agents sa CRM systems, ticketing platforms, o knowledge bases upang masagot ang mga tanong ng user.
- **Content Generation and Editing:** Maaaring gumamit ang mga agents ng mga tool tulad ng grammar checkers, text summarizers, o content safety evaluators upang tumulong sa mga gawain sa paggawa ng nilalaman.

## Ano ang mga elemento o building blocks na kailangan upang maipatupad ang tool use design pattern?

Ang mga building blocks na ito ay nagbibigay-daan sa AI agent na magsagawa ng malawak na hanay ng mga gawain. Tingnan natin ang mga pangunahing elemento na kailangan upang maipatupad ang Tool Use Design Pattern:

- **Function/Tool Schemas**: Detalyadong mga depinisyon ng mga available na tool, kabilang ang pangalan ng function, layunin, kinakailangang mga parameter, at inaasahang outputs. Ang mga schemas na ito ay nagbibigay-daan sa LLM na maunawaan kung anong mga tool ang available at kung paano bumuo ng valid na mga request.

- **Function Execution Logic**: Nagtatakda kung paano at kailan tatawagin ang mga tool batay sa intensyon ng user at konteksto ng usapan. Maaaring kabilang dito ang planner modules, routing mechanisms, o conditional flows na nagtatakda ng paggamit ng tool nang dynamic.

- **Message Handling System**: Mga bahagi na namamahala sa daloy ng usapan sa pagitan ng mga input ng user, mga tugon ng LLM, mga tawag sa tool, at mga output ng tool.

- **Tool Integration Framework**: Imprastraktura na nagkokonekta sa agent sa iba't ibang tool, maging ito ay simpleng functions o kumplikadong panlabas na serbisyo.

- **Error Handling & Validation**: Mga mekanismo upang pamahalaan ang mga pagkabigo sa pag-execute ng tool, i-validate ang mga parameter, at pamahalaan ang mga hindi inaasahang tugon.

- **State Management**: Nagtatala ng konteksto ng usapan, mga nakaraang interaksyon sa tool, at persistent na data upang matiyak ang pagkakapare-pareho sa multi-turn na interaksyon.

Susunod, tingnan natin ang Function/Tool Calling nang mas detalyado.

### Function/Tool Calling

Ang Function Calling ang pangunahing paraan upang bigyang-kakayahan ang Large Language Models (LLMs) na makipag-ugnayan sa mga tool. Madalas mong makikita ang 'Function' at 'Tool' na ginagamit nang palitan dahil ang 'functions' (mga bloke ng reusable code) ang 'tools' na ginagamit ng mga agents upang maisagawa ang mga gawain. Para ma-invoke ang code ng isang function, kailangang ihalintulad ng LLM ang kahilingan ng user sa deskripsyon ng function. Upang magawa ito, isang schema na naglalaman ng mga deskripsyon ng lahat ng available na functions ang ipinapadala sa LLM. Pinipili ng LLM ang pinaka-angkop na function para sa gawain at ibinabalik ang pangalan nito at mga argumento. Ang napiling function ay ini-execute, ang tugon nito ay ibinabalik sa LLM, na ginagamit ang impormasyon upang tumugon sa kahilingan ng user.

Para sa mga developer na magpatupad ng function calling para sa mga agents, kakailanganin mo ang:

1. Isang LLM model na sumusuporta sa function calling
2. Isang schema na naglalaman ng mga deskripsyon ng function
3. Ang code para sa bawat function na inilarawan

Gamitin natin ang halimbawa ng pagkuha ng kasalukuyang oras sa isang lungsod upang ilarawan:

1. **I-initialize ang isang LLM na sumusuporta sa function calling:**

    Hindi lahat ng modelo ay sumusuporta sa function calling, kaya mahalagang tiyakin na ang LLM na ginagamit mo ay sumusuporta dito. Ang <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ay sumusuporta sa function calling. Maaari tayong magsimula sa pamamagitan ng pag-initiate ng Azure OpenAI client.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Gumawa ng Function Schema**:

    Susunod, magde-define tayo ng JSON schema na naglalaman ng pangalan ng function, deskripsyon ng ginagawa ng function, at ang mga pangalan at deskripsyon ng mga parameter ng function. Pagkatapos, dadalhin natin ang schema na ito at ipapasa sa client na ginawa kanina, kasama ang kahilingan ng user na hanapin ang oras sa San Francisco. Ang mahalagang tandaan ay ang **tool call** ang ibinabalik, **hindi** ang panghuling sagot sa tanong. Tulad ng nabanggit kanina, ibinabalik ng LLM ang pangalan ng function na pinili nito para sa gawain, at ang mga argumento na ipapasa dito.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Ang code ng function na kinakailangan upang maisagawa ang gawain:**

    Ngayon na pinili na ng LLM kung aling function ang kailangang patakbuhin, kailangang ipatupad at i-execute ang code na nagsasagawa ng gawain. Maaari nating ipatupad ang code upang makuha ang kasalukuyang oras gamit ang Python. Kakailanganin din nating isulat ang code upang kunin ang pangalan at mga argumento mula sa response_message upang makuha ang panghuling resulta.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

Ang Function Calling ang sentro ng karamihan, kung hindi man lahat, ng disenyo ng paggamit ng tool ng agent, ngunit ang pagpapatupad nito mula sa simula ay maaaring maging hamon. Tulad ng natutunan natin sa [Lesson 2](../../../02-explore-agentic-frameworks), ang mga agentic frameworks ay nagbibigay sa atin ng pre-built na mga building blocks upang maipatupad ang paggamit ng tool.

## Mga Halimbawa ng Paggamit ng Tool sa Agentic Frameworks

Narito ang ilang halimbawa kung paano mo maipapatupad ang Tool Use Design Pattern gamit ang iba't ibang agentic frameworks:

### Semantic Kernel

Ang <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> ay isang open-source na AI framework para sa mga developer ng .NET, Python, at Java na nagtatrabaho gamit ang Large Language Models (LLMs). Pinapadali nito ang proseso ng paggamit ng function calling sa pamamagitan ng awtomatikong pag-describe ng iyong mga function at ang kanilang mga parameter sa modelo sa pamamagitan ng proseso na tinatawag na <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a>. Pinamamahalaan din nito ang komunikasyon sa pagitan ng modelo at ng iyong code. Isa pang bentahe ng paggamit ng agentic framework tulad ng Semantic Kernel ay ang kakayahang ma-access ang mga pre-built na tool tulad ng <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> at <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Ang sumusunod na diagram ay naglalarawan ng proseso ng function calling gamit ang Semantic Kernel:

![function calling](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.tl.png)

Sa Semantic Kernel, ang mga functions/tools ay tinatawag na <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Maaari nating i-convert ang `get_current_time` function na nakita natin kanina sa isang plugin sa pamamagitan ng paggawa nito bilang isang class na may function sa loob. Maaari rin nating i-import ang `kernel_function` decorator, na tumatanggap ng deskripsyon ng function. Kapag gumawa ka ng kernel gamit ang GetCurrentTimePlugin, awtomatikong ise-serialize ng kernel ang function at ang mga parameter nito, na lumilikha ng schema na ipapadala sa LLM sa proseso.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

Ang <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ay isang mas bagong agentic framework na idinisenyo upang bigyang-kakayahan ang mga developer na ligtas na bumuo, mag-deploy, at mag-scale ng mataas na kalidad at extensible na AI agents nang hindi kinakailangang pamahalaan ang underlying compute at storage resources. Ito ay partikular na kapaki-pakinabang para sa mga enterprise applications dahil ito ay isang fully managed service na may enterprise-grade security.

Kung ikukumpara sa pag-develop gamit ang LLM API nang direkta, ang Azure AI Agent Service ay nagbibigay ng ilang bentahe, kabilang ang:

- Awtomatikong tool calling – hindi na kailangang i-parse ang tool call, i-invoke ang tool, at pamahalaan ang tugon; lahat ng ito ay ginagawa na sa server-side
- Ligtas na pamamahala ng data – sa halip na pamahalaan ang iyong sariling conversation state, maaari kang umasa sa threads upang i-store ang lahat ng impormasyong kailangan mo
- Mga pre-built na tool – Mga tool na maaari mong gamitin upang makipag-ugnayan sa iyong mga data sources, tulad ng Bing, Azure AI Search, at Azure Functions.

Ang mga tool na available sa Azure AI Agent Service ay maaaring hatiin sa dalawang kategorya:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Pinapayagan tayo ng Agent Service na magamit ang mga tool na ito nang magkasama bilang isang `toolset`. Ginagamit din nito ang `threads` na nagtatala ng kasaysayan ng mga mensahe mula sa isang partikular na usapan.

Isipin na ikaw ay isang sales agent sa isang kumpanya na tinatawag na Contoso. Nais mong bumuo ng isang conversational agent na maaaring sumagot sa mga tanong tungkol sa iyong sales data.

Ang sumusunod na imahe ay naglalarawan kung paano mo magagamit ang Azure AI Agent Service upang suriin ang iyong sales data:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.tl.jpg)

Upang magamit ang alinman sa mga tool na ito gamit ang serbisyo, maaari tayong gumawa ng client at mag-define ng tool o toolset. Upang maipatupad ito nang praktikal, maaari nating gamitin ang sumusunod na Python code. Ang LLM ay magagawang tingnan ang toolset at magdesisyon kung gagamitin ang user-created function, `fetch_sales_data_using_sqlite_query`, o ang pre-built Code Interpreter depende sa kahilingan ng user.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern upang makabuo ng mapagkakatiwalaang AI agents?

Isang karaniwang alalahanin sa SQL na dynamic na nabuo ng LLMs ay ang seguridad, partikular ang panganib ng SQL injection o malisyosong aksyon, tulad ng pag-drop o pag-tamper sa database. Bagama't valid ang mga alalahaning ito, maaari itong epektibong maibsan sa pamamagitan ng tamang pag-configure ng database access permissions. Para sa karamihan ng mga database, ito ay kinabibilangan ng pag-configure sa database bilang read-only. Para sa mga database services tulad ng PostgreSQL o Azure SQL, ang app ay dapat bigyan ng read-only (SELECT) role.
Ang pagpapatakbo ng app sa isang ligtas na kapaligiran ay higit pang nagpapahusay sa proteksyon. Sa mga senaryo ng enterprise, karaniwang kinukuha at binabago ang data mula sa mga operational system patungo sa isang read-only na database o data warehouse na may user-friendly na schema. Ang ganitong paraan ay nagsisiguro na ang data ay ligtas, na-optimize para sa performance at accessibility, at ang app ay may limitadong, read-only na access.

### May Karagdagang Tanong Tungkol sa Paggamit ng Tool Design Patterns?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipag-ugnayan sa ibang mga nag-aaral, dumalo sa office hours, at makuha ang sagot sa iyong mga tanong tungkol sa AI Agents.

## Karagdagang Mga Mapagkukunan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Nakaraang Aralin

[Pag-unawa sa Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Susunod na Aralin

[Agentic RAG](../05-agentic-rag/README.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.