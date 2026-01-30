[![Paano Magdisenyo ng Magandang AI Agents](../../../translated_images/tl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

# Tool Use Design Pattern

Kawili-wili ang mga tools dahil pinapahintulutan nila ang mga AI agent na magkaroon ng mas malawak na hanay ng mga kakayahan. Sa halip na limitado ang mga aksyon na kayang gawin ng agent, sa pamamagitan ng pagdagdag ng tool, maaari na ngayong magsagawa ang agent ng malawak na uri ng mga aksyon. Sa kabanatang ito, tatalakayin natin ang Tool Use Design Pattern, na naglalarawan kung paano maaaring gumamit ang mga AI agent ng mga partikular na tool upang makamit ang kanilang mga layunin.

## Panimula

Sa araling ito, nais nating sagutin ang mga sumusunod na tanong:

- Ano ang tool use design pattern?
- Ano ang mga use case kung saan ito maaaring ilapat?
- Ano ang mga elemento/mga pundasyon na kailangan upang ipatupad ang design pattern?
- Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern upang bumuo ng mga AI agent na mapagkakatiwalaan?

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, magagawa mong:

- Ibigay ang depinisyon ng Tool Use Design Pattern at ang layunin nito.
- Kilalanin ang mga use case kung saan ang Tool Use Design Pattern ay naaangkop.
- Maunawaan ang mga pangunahing elemento na kailangan upang ipatupad ang design pattern.
- Makilala ang mga konsiderasyon para matiyak ang pagiging mapagkakatiwalaan ng mga AI agent na gumagamit ng design pattern na ito.

## Ano ang Tool Use Design Pattern?

Ang **Tool Use Design Pattern** ay nakatuon sa pagbibigay ng kakayahan sa LLM upang makipag-ugnayan sa mga panlabas na tool upang makamit ang mga partikular na layunin. Ang mga tool ay code na maaaring ipatakbo ng agent upang magsagawa ng mga aksyon. Ang isang tool ay maaaring isang simpleng function tulad ng calculator, o isang tawag sa API ng isang third-party na serbisyo tulad ng paghahanap ng presyo ng stock o forecast ng panahon. Sa konteksto ng mga AI agent, ang mga tool ay dinisenyo upang mapatakbo ng mga agent bilang tugon sa **model-generated function calls**.

## Ano ang mga use case kung saan ito maaaring ilapat?

Maaaring gamitin ng mga AI Agent ang mga tool upang tapusin ang mga komplikadong gawain, kumuha ng impormasyon, o gumawa ng mga desisyon. Madalas gamitin ang tool use design pattern sa mga senaryo na nangangailangan ng dinamiko at tuloy-tuloy na interaksyon sa mga panlabas na sistema, tulad ng databases, web services, o code interpreters. Ang kakayahang ito ay kapaki-pakinabang para sa iba't ibang use case kabilang ang:

- **Dinamiko na Pagkuha ng Impormasyon:** Maaaring mag-query ang mga agent sa mga panlabas na API o databases upang kumuha ng pinakabagong datos (hal., pag-query ng SQLite database para sa pagsusuri ng datos, pagkuha ng presyo ng stock o impormasyon tungkol sa panahon).
- **Pagpapatakbo at Pag-interpret ng Code:** Maaaring magpatakbo ng mga code o script ang mga agent upang lutasin ang mga suliraning pang-matematika, gumawa ng mga ulat, o magsagawa ng mga simulation.
- **Automation ng Workflow:** Pag-automate ng paulit-ulit o multi-step na workflows sa pamamagitan ng pagsasama ng mga tool tulad ng task schedulers, mga serbisyo ng email, o pipelines ng datos.
- **Customer Support:** Maaaring makipag-ugnayan ang mga agent sa mga CRM system, ticketing platforms, o knowledge bases upang malutas ang mga tanong ng gumagamit.
- **Pagbuo at Pag-edit ng Nilalaman:** Maaaring gamitin ng mga agent ang mga tool tulad ng grammar checker, text summarizer, o content safety evaluator upang tumulong sa mga gawain sa paggawa ng nilalaman.

## Ano ang mga elemento/mga pundasyon na kailangan upang ipatupad ang tool use design pattern?

Ang mga pundasyong ito ay nagpapahintulot sa AI agent na magsagawa ng malawak na hanay ng mga gawain. Tingnan natin ang mga pangunahing elemento na kailangan upang ipatupad ang Tool Use Design Pattern:

- **Function/Tool Schemas**: Detalyadong mga depinisyon ng mga magagamit na tool, kabilang ang pangalan ng function, layunin, mga kinakailangang parameter, at inaasahang mga output. Pinapahintulutan ng mga schema na ito ang LLM na maunawaan kung anong mga tool ang magagamit at kung paano bumuo ng valid na mga request.

- **Function Execution Logic**: Namamahala kung paano at kailan tinatawag ang mga tool batay sa intensyon ng user at konteksto ng usapan. Maaaring kabilang dito ang mga planner modules, routing mechanisms, o kondisyunal na mga daloy na tumutukoy ng paggamit ng tool nang dinamiko.

- **Message Handling System**: Mga bahagi na namamahala sa daloy ng usapan sa pagitan ng mga input ng user, mga tugon ng LLM, mga tawag sa tool, at mga output ng tool.

- **Tool Integration Framework**: Inprastruktura na nag-uugnay sa agent sa iba't ibang tool, maging ito man ay simpleng mga function o komplikadong panlabas na serbisyo.

- **Error Handling & Validation**: Mga mekanismo upang pamahalaan ang mga pagkabigo sa pagpapatakbo ng tool, i-validate ang mga parameter, at ayusin ang hindi inaasahang mga tugon.

- **State Management**: Nagsubaybay sa konteksto ng usapan, mga nakaraang pakikipag-ugnayan sa tool, at persistent na datos upang matiyak ang pagkakapare-pareho sa maraming turn na interaksyon.

Susunod, tingnan natin ang Function/Tool Calling nang mas detalyado.

### Function/Tool Calling

Ang function calling ang pangunahing paraan para payagan ang Large Language Models (LLMs) na makipag-ugnayan sa mga tool. Madalas mong makita na ginagamit nang palitan ang 'Function' at 'Tool' dahil ang 'functions' (mga bloke ng reusable code) ay ang mga 'tool' na ginagamit ng mga agent upang isakatuparan ang mga gawain. Para mapatakbo ang code ng isang function, kailangan ng LLM na ihambing ang kahilingan ng user sa paglalarawan ng mga function. Upang gawin ito, isang schema na naglalaman ng mga paglalarawan ng lahat ng magagamit na function ang ipinapadala sa LLM. Pinipili ng LLM ang pinaka-angkop na function para sa gawain at ibinabalik ang pangalan at mga argumento nito. Tinatawag ang napiling function, ang tugon nito ay ipinapadala pabalik sa LLM, na ginagamit ang impormasyong ito upang tumugon sa kahilingan ng user.

Para sa mga developer na nais magpatupad ng function calling para sa mga agent, kakailanganin mo:

1. Isang LLM na sumusuporta sa function calling
2. Isang schema na naglalaman ng paglalarawan ng mga function
3. Ang code para sa bawat function na inilalarawan

Gamitin natin ang halimbawa ng pagkuha ng kasalukuyang oras sa isang lungsod upang ilarawan ito:

1. **I-initialize ang LLM na sumusuporta sa function calling:**

    Hindi lahat ng modelo ay sumusuporta sa function calling, kaya mahalagang tiyakin na sumusuporta ang LLM na iyong ginagamit. Ang <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ay sumusuporta sa function calling. Maaari nating simulan sa pamamagitan ng pag-initiate ng Azure OpenAI client.

    ```python
    # I-initialize ang Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Gumawa ng Function Schema**:

    Susunod, magdedeklara tayo ng JSON schema na naglalaman ng pangalan ng function, paglalarawan ng ginagawa nito, at mga pangalan at paglalarawan ng mga parameter ng function.
    Ipasa natin ang schema na ito sa client na nilikha kanina, kasabay ng kahilingan ng user upang hanapin ang oras sa San Francisco. Mahalaga na tandaan na ang **tool call** ang ibinabalik, **hindi** ang final na sagot sa tanong. Tulad ng nabanggit kanina, ibinabalik ng LLM ang pangalan ng function na napili nito para sa gawain, at ang mga argumento na ipapasa dito.

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
  
      # Proseso ang tugon ng modelo
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Ang code ng function na kinakailangan upang isakatuparan ang gawain:**

    Ngayon na napili na ng LLM kung aling function ang kailangang patakbuhin, kailangang ipatupad at isagawa ang code na magsasagawa ng gawain.
    Maaring ipatupad ang code upang makuha ang kasalukuyang oras gamit ang Python. Kailangan din nating isulat ang code upang kunin ang pangalan at mga argumento mula sa response_message para makuha ang huling resulta.

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
     # Pangasiwaan ang mga tawag sa function
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
  
      # Pangalawang tawag sa API: Kunin ang panghuling tugon mula sa modelo
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

Ang Function Calling ay nasa puso ng karamihan, kung hindi lahat, ng tool use design para sa mga agent, subalit minsan ay hamon na ipatupad ito mula sa simula.
Tulad ng natutunan natin sa [Lesson 2](../../../02-explore-agentic-frameworks), nagbibigay ang mga agentic framework ng mga pre-built na pundasyon upang ipatupad ang tool use.

## Mga Halimbawa ng Tool Use gamit ang Agentic Frameworks

Narito ang ilang mga halimbawa kung paano mo maaaring ipatupad ang Tool Use Design Pattern gamit ang iba't ibang agentic frameworks:

### Semantic Kernel

Ang <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> ay isang open-source AI framework para sa .NET, Python, at Java developers na nagtatrabaho gamit ang Large Language Models (LLMs). Pinapasimple nito ang proseso ng paggamit ng function calling sa pamamagitan ng awtomatikong paglalarawan ng iyong mga function at mga parameter sa modelo sa pamamagitan ng prosesong tinatawag na <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a>. Pinangangasiwaan din nito ang komunikasyon pabalik-balik sa pagitan ng modelo at iyong code. Isa pang benepisyo ng paggamit ng agentic framework tulad ng Semantic Kernel ay pinapahintulutan ka nitong ma-access ang mga pre-built na tool tulad ng <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> at <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Ipinapakita ng sumusunod na diagram ang proseso ng function calling gamit ang Semantic Kernel:

![function calling](../../../translated_images/tl/functioncalling-diagram.a84006fc287f6014.webp)

Sa Semantic Kernel, ang mga functions/tools ay tinatawag na <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Maaari nating gawing plugin ang function na `get_current_time` na nakita natin kanina sa pamamagitan ng pag-convert nito sa isang klase na may function sa loob nito. Maaari rin nating i-import ang dekorador na `kernel_function`, na tumatanggap ng paglalarawan ng function. Kapag gumawa ka ng kernel gamit ang GetCurrentTimePlugin, awtomatikong isi-serialize ng kernel ang function at ang mga parameter nito, na lumilikha ng schema na ipapadala sa LLM sa proseso.

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

# Lumikha ng kernel
kernel = Kernel()

# Lumikha ng plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Idagdag ang plugin sa kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

Ang <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ay isang mas bagong agentic framework na idinisenyo upang bigyang kapangyarihan ang mga developer na ligtas na makabuo, mag-deploy, at mag-scale ng mataas na quality at extensible na mga AI agent nang hindi kailangang pamahalaan ang underlying compute at storage resources. Mahalaga ito para sa mga enterprise application dahil ito ay isang fully managed service na may enterprise grade security.

Kung ikukumpara sa pag-develop gamit ang LLM API nang direkta, nag-aalok ang Azure AI Agent Service ng ilang kalamangan, kabilang ang:

- Awtomatikong tool calling – hindi kailangang mag-parse ng tool call, tawagin ang tool, at pamahalaan ang tugon; lahat ng ito ay ginagawa na server-side
- Securely managed data – sa halip na pamahalaan ang sariling estado ng usapan, maaari kang umasa sa mga threads upang itago ang lahat ng impormasyong kailangan mo
- Out-of-the-box na mga tool – Mga tool na magagamit para makipag-ugnayan sa iyong mga pinagkukunan ng datos, tulad ng Bing, Azure AI Search, at Azure Functions.

Ang mga tool na available sa Azure AI Agent Service ay mahahati sa dalawang kategorya:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Pinapahintulutan tayo ng Agent Service na magamit ang mga tool na ito nang magkasama bilang isang `toolset`. Ginagamit din nito ang `threads` na sumusubaybay sa kasaysayan ng mga mensahe mula sa isang partikular na pag-uusap.

Isipin na ikaw ay isang sales agent sa kumpanyang Contoso. Nais mong bumuo ng isang conversational agent na maaaring sumagot sa mga tanong tungkol sa iyong sales data.

Ipinapakita ng sumusunod na larawan kung paano mo magagamit ang Azure AI Agent Service upang suriin ang iyong sales data:

![Agentic Service In Action](../../../translated_images/tl/agent-service-in-action.34fb465c9a84659e.webp)

Para magamit ang alinman sa mga tool na ito sa serbisyo, maaari tayong gumawa ng client at magdeklara ng isang tool o toolset. Para maipatupad ito nang praktikal, maaari nating gamitin ang sumusunod na Python code. Magagawa ng LLM na tingnan ang toolset at magpasya kung gagamitin ang user-created na function na `fetch_sales_data_using_sqlite_query` o ang pre-built Code Interpreter depende sa kahilingan ng user.

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

## Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern upang bumuo ng mapagkakatiwalaang AI agents?

Isang karaniwang alalahanin tungkol sa SQL na dinamiko na nabubuo ng LLMs ay ang seguridad, partikular ang panganib ng SQL injection o masamang aksyon, tulad ng pagbura o pag-tamper sa database. Bagamat makatwiran ang mga alalahaning ito, epektibong mapipigilan ang mga ito sa pamamagitan ng wastong pag-configure ng mga access permissions sa database. Para sa karamihan ng mga database, kinakailangan ang pag-configure nito bilang read-only. Para sa mga database service tulad ng PostgreSQL o Azure SQL, dapat bigyan ng read-only (SELECT) na papel ang app.
Ang pagpapatakbo ng app sa isang ligtas na kapaligiran ay higit pang nagpapahusay ng proteksyon. Sa mga enterprise na senaryo, karaniwang kinukuha at trinatransporma ang data mula sa mga operational na sistema papunta sa isang read-only na database o data warehouse na may user-friendly na schema. Tinitiyak ng paraang ito na ang data ay ligtas, na-optimize para sa pagganap at accessibility, at na may limitadong read-only na access ang app.

## Mga Halimbawang Kodigo

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## May Higit Pang Mga Tanong Tungkol sa Paggamit ng Tool Use Design Patterns?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makilala ang iba pang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang Mga Mapagkukunan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Nakaraang Aralin

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Susunod na Aralin

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI na serbisyo sa pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring bilang pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->