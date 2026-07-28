[![Paano Magdisenyo ng Magandang AI Agents](../../../translated_images/tl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

# Disenyo ng Tool Use Pattern

Kagiliw-giliw ang mga tools dahil pinapayagan nila ang mga AI agents na magkaroon ng mas malawak na hanay ng mga kakayahan. Sa halip na may limitadong set ng mga aksyon na maaaring gawin ang agent, sa pamamagitan ng pagdagdag ng isang tool, maaari na ngayong magsagawa ng malawak na hanay ng mga aksyon ang agent. Sa kabanatang ito, titingnan natin ang Tool Use Design Pattern, na naglalarawan kung paano maaaring gumamit ang mga AI agents ng mga partikular na tool upang makamit ang kanilang mga layunin.

## Panimula

Sa araling ito, nais nating sagutin ang mga sumusunod na tanong:

- Ano ang tool use design pattern?
- Ano ang mga use case na maaaring pag-aplayan nito?
- Ano ang mga elemento/mga pundasyong bahagi na kailangan upang ipatupad ang disenyo ng pattern?
- Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern upang makabuo ng mapagkakatiwalaang AI agents?

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, magagawa mong:

- I-defina ang Tool Use Design Pattern at ang layunin nito.
- Tukuyin ang mga use case kung saan maaaring gamitin ang Tool Use Design Pattern.
- Unawain ang mga pangunahing elemento na kailangan upang ipatupad ang disenyo ng pattern.
- Kilalanin ang mga konsiderasyon para sa pagtiyak ng pagiging mapagkakatiwalaan ng AI agents gamit ang disenyo ng pattern na ito.

## Ano ang Tool Use Design Pattern?

Ang **Tool Use Design Pattern** ay nakatuon sa pagbibigay ng kakayahan sa LLMs na makipag-ugnayan sa mga panlabas na tool upang makamit ang mga partikular na layunin. Ang mga tool ay code na maaaring patakbuhin ng isang agent upang magsagawa ng mga aksyon. Ang isang tool ay maaaring isang simpleng function tulad ng calculator, o isang API call sa isang third-party na serbisyo tulad ng pagtingin ng presyo ng stock o pagtataya ng panahon. Sa konteksto ng AI agents, dinisenyo ang mga tool upang patakbuhin ng mga agent bilang tugon sa **model-generated function calls**.

## Ano ang mga use case na maaaring pag-aplayan nito?

Maaaring gamitin ng mga AI Agents ang mga tool upang tapusin ang mga komplikadong gawain, kumuha ng impormasyon, o gumawa ng mga desisyon. Madalas na ginagamit ang tool use design pattern sa mga sitwasyon na nangangailangan ng dynamic na pakikipag-ugnayan sa mga panlabas na sistema, tulad ng mga database, web services, o mga code interpreter. Ang kakayahang ito ay kapaki-pakinabang para sa iba't ibang mga use case kabilang ang:

- **Dynamic Information Retrieval:** Maaaring mag-query ang mga agent ng mga panlabas na API o database upang kumuha ng up-to-date na data (hal., pag-query sa isang SQLite database para sa data analysis, pagkuha ng presyo ng stock o impormasyon tungkol sa panahon).
- **Code Execution and Interpretation:** Maaaring magpatupad ng code o script ang mga agent upang lutasin ang mga problemang pang-matematika, gumawa ng mga ulat, o magsagawa ng mga simulasyon.
- **Workflow Automation:** Pag-automate ng mga paulit-ulit o multi-step na mga workflow sa pamamagitan ng pag-integrate ng mga tool tulad ng task schedulers, email services, o mga data pipeline.
- **Customer Support:** Maaaring makipag-ugnayan ang mga agent sa mga CRM system, ticketing platform, o knowledge base upang maresolba ang mga tanong ng user.
- **Content Generation and Editing:** Maaaring gamitin ng mga agent ang mga tool tulad ng grammar checkers, text summarizers, o mga content safety evaluator upang tumulong sa mga gawain ng paglikha ng nilalaman.

## Ano ang mga elemento/mga pundasyong bahagi na kailangan upang ipatupad ang tool use design pattern?

Ang mga pundasyong bahagi na ito ay nagbibigay-daan sa AI agent na magsagawa ng malawak na hanay ng mga gawain. Tingnan natin ang mga pangunahing elemento na kailangan upang ipatupad ang Tool Use Design Pattern:

- **Function/Tool Schemas**: Detalyadong mga depinisyon ng mga magagamit na tool, kabilang ang pangalan ng function, layunin, kinakailangang mga parameter, at inaasahang output. Pinapahintulutan ng mga schema na ito ang LLM na maunawaan kung ano ang mga tool na magagamit at paano bumuo ng wastong mga kahilingan.

- **Function Execution Logic**: Namamahala kung paano at kailan tatawagin ang mga tool batay sa layunin ng user at konteksto ng usapan. Maaaring kabilang dito ang mga planner module, mga routing mechanism, o mga conditional flow na tumutukoy sa paggamit ng tool nang dinamiko.

- **Message Handling System**: Mga bahagi na namamahala sa daloy ng pag-uusap sa pagitan ng mga input ng user, mga sagot ng LLM, mga tawag sa tool, at mga output ng tool.

- **Tool Integration Framework**: Inprastraktura na kumokonekta sa agent sa iba't ibang tool, maging ito man ay simpleng mga function o komplikadong panlabas na serbisyo.

- **Error Handling & Validation**: Mga mekanismo para hawakan ang mga pagkabigo sa pagpapatupad ng tool, beripikahin ang mga parameter, at pamahalaan ang mga hindi inaasahang tugon.

- **State Management**: Sumusubaybay sa konteksto ng usapan, mga naunang interaksyon sa tool, at matatag na data upang masiguro ang konsistensi sa maraming pag-uusap.

Susunod, tingnan natin nang mas detalyado ang Function/Tool Calling.
 
### Function/Tool Calling

Ang function calling ang pangunahing paraan upang pahintulutan ang Large Language Models (LLMs) na makipag-ugnayan sa mga tool. Madalas mong makikita ang paggamit ng 'Function' at 'Tool' nang palitan dahil ang 'functions' (mga bloke ng reusable code) ay ang mga 'tool' na ginagamit ng mga agent upang isagawa ang mga gawain. Upang mapatupad ang code ng isang function, kailangang ihambing ng LLM ang kahilingan ng user sa paglalarawan ng mga function. Para dito, isang schema na naglalaman ng mga paglalarawan ng lahat ng magagamit na function ang ipinapadala sa LLM. Pinipili ng LLM ang pinakaangkop na function para sa gawain at ibinabalik ang pangalan nito at mga argumento. Pinapatawag ang piniling function, ang tugon nito ay ipinapadala pabalik sa LLM, na ginagamit ang impormasyon upang tugunan ang kahilingan ng user.

Para sa mga developer na nais magpatupad ng function calling para sa mga agent, kakailanganin mo:

1. Isang LLM model na sumusuporta sa function calling
2. Isang schema na naglalaman ng mga paglalarawan ng function
3. Ang code para sa bawat function na inilalarawan

Gamitin natin ang halimbawa ng pagkuha ng kasalukuyang oras sa isang lungsod upang ipakita:

1. **I-initialize ang LLM na sumusuporta sa function calling:**

    Hindi lahat ng modelo ay sumusuporta sa function calling, kaya mahalagang tiyakin na ang LLM na ginagamit mo ay sumusuporta rito.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Suportado ng Azure OpenAI</a> ang function calling. Maaari tayong magsimula sa pag-initialize ng OpenAI client laban sa Azure OpenAI **Responses API** (ang matatag na endpoint na `/openai/v1/` — hindi kailangan ng `api_version`). 

    ```python
    # I-initialize ang OpenAI client para sa Azure OpenAI (Responses API, v1 endpoint)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Gumawa ng Function Schema**:

    Susunod, magdedefina tayo ng isang JSON schema na naglalaman ng pangalan ng function, paglalarawan ng ginagawa ng function, at mga pangalan at paglalarawan ng mga parameter ng function.
    Ipasa natin ang schema na ito sa client na ginawa kanina, kasabay ng kahilingan ng user upang malaman ang oras sa San Francisco. Ang mahalagang tandaan ay isang **tool call** ang ibinabalik, **hindi** ang huling sagot sa tanong. Tulad ng nabanggit kanina, ibinabalik ng LLM ang pangalan ng function na pinili nito para sa gawain, pati na rin ang mga argumentong ipapasa dito.

    ```python
    # Paglalarawan ng function para basahin ng modelo (Responses API flat tool format)
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
  
    # Paunang mensahe ng gumagamit
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Unang tawag sa API: Hilingin sa modelo na gamitin ang function
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Ibinabalik ng Responses API ang mga tawag sa tool bilang mga function_call item sa response.output.
    # Idagdag ang mga ito sa pag-uusap upang ang modelo ay may buong konteksto sa susunod na palitan.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Ang code ng function na kinakailangan upang isagawa ang gawain:**

    Ngayon na napili na ng LLM kung aling function ang kailangang patakbuhin, kailangang ipatupad at isagawa ang code ng gawain.
    Maaari nating ipatupad ang code upang makuha ang kasalukuyang oras sa Python. Kailangan din nating isulat ang code upang kunin ang pangalan at mga argumento mula sa response_message upang makuha ang panghuling resulta.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Ibalik ang resulta ng tool bilang isang function_call_output na item
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Pangalawang tawag sa API: Kumuha ng panghuling tugon mula sa modelo
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

Ang Function Calling ay nasa puso ng karamihan, kung hindi man lahat, ng disenyo ng tool use para sa mga agent, ngunit minsan ay mahirap itong ipatupad mula sa simula.
Tulad ng natutunan natin sa [Lesson 2](../../../02-explore-agentic-frameworks), nagbibigay ang mga agentic framework ng mga pre-built na pundasyong bahagi upang ipatupad ang tool use.
 
## Mga Halimbawa ng Tool Use gamit ang Agentic Frameworks

Narito ang ilang halimbawa kung paano mo maaaring ipatupad ang Tool Use Design Pattern gamit ang iba't ibang agentic framework:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Ang Microsoft Agent Framework</a> ay isang open-source na AI framework para sa paggawa ng AI agents. Pinapasimple nito ang proseso ng paggamit ng function calling sa pamamagitan ng pagpapahintulot sa iyo na idefine ang mga tool bilang mga Python function gamit ang `@tool` decorator. Pinangangalagaan ng framework ang komunikasyon pabalik-balik sa pagitan ng modelo at ng iyong code. Nagbibigay din ito ng akses sa mga pre-built na tool tulad ng File Search at Code Interpreter sa pamamagitan ng `FoundryChatClient`.

Ipinapakita ng sumusunod na diagram ang proseso ng function calling gamit ang Microsoft Agent Framework:

![function calling](../../../translated_images/tl/functioncalling-diagram.a84006fc287f6014.webp)

Sa Microsoft Agent Framework, ang mga tool ay dinefine bilang mga decorated function. Maaari nating gawing tool ang function na `get_current_time` na nakita kanina gamit ang `@tool` decorator. Awtomatikong isi-serialize ng framework ang function at ang mga parameter nito, ginagawa ang schema upang ipadala sa LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Gumawa ng kliyente
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Gumawa ng ahente at patakbuhin gamit ang tool
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Ang Microsoft Foundry Agent Service</a> ay isang mas bagong agentic framework na dinisenyo upang bigyan ng kapangyarihan ang mga developer na ligtas na makabuo, makapag-deploy, at makapag-scale ng mataas na kalidad at extensible na AI agents nang hindi kinakailangang pamahalaan ang mga underlying compute at storage resources. Partikular itong kapaki-pakinabang para sa mga enterprise application dahil ito ay isang fully managed service na may enterprise grade security.

Kung ihahambing sa direktang pag-develop gamit ang LLM API, nagbibigay ang Microsoft Foundry Agent Service ng ilang mga kalamangan, kabilang ang:

- Awtomatikong pagtawag ng tool – hindi mo na kailangang mag-parse ng tool call, tawagin ang tool, at hawakan ang tugon; lahat ng ito ay ginagawa na sa server-side
- Ligtas na pamamahala ng data – sa halip na pamahalaan ang iyong sariling estado ng pag-uusap, maaari kang umasa sa threads upang itago ang lahat ng impormasyong kailangan mo
- Mga tool na ready gamitin – Mga tool na maaari mong gamitin para makipag-ugnayan sa iyong mga data source, tulad ng Bing, Azure AI Search, at Azure Functions.

Maaaring hatiin ang mga tool na magagamit sa Microsoft Foundry Agent Service sa dalawang kategorya:

1. Mga Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding gamit ang Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Mga Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Mga tool na tinukoy ng OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Pinapayagan tayo ng Agent Service na gamitin ang mga tool na ito nang magkakasama bilang isang `toolset`. Ginagamit din nito ang `threads` na sumusubaybay sa kasaysayan ng mga mensahe mula sa isang partikular na pag-uusap.

Isipin mo na ikaw ay isang sales agent sa kumpanyang tinatawag na Contoso. Nais mong bumuo ng isang conversational agent na maaaring sumagot ng mga tanong tungkol sa iyong sales data.

Ipinapakita ng sumusunod na larawan kung paano mo magagamit ang Microsoft Foundry Agent Service upang suriin ang iyong sales data:

![Agentic Service In Action](../../../translated_images/tl/agent-service-in-action.34fb465c9a84659e.webp)

Upang magamit ang alinman sa mga tool na ito sa serbisyo, maaari tayong gumawa ng client at magdefine ng isang tool o toolset. Para maisagawa ito nang praktikal, maaari nating gamitin ang sumusunod na Python code. Magagawa ng LLM na tingnan ang toolset at magpasya kung gagamitin ang user-created function na `fetch_sales_data_using_sqlite_query` o ang pre-built Code Interpreter depende sa kahilingan ng user.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query na function na makikita sa isang fetch_sales_data_functions.py na file.
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
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Ano ang mga espesyal na konsiderasyon sa paggamit ng Tool Use Design Pattern upang bumuo ng mapagkakatiwalaang AI agents?

Isang karaniwang alalahanin sa dynamically na nilikhang SQL ng LLM ay ang seguridad, partikular ang panganib ng SQL injection o mga malisyosong aksyon, tulad ng pagbura o paninira sa database. Bagamat may katwiran ang mga alalahaning ito, maaaring epektibong mapigilan ang mga ito sa pamamagitan ng tamang pagsasaayos ng mga permiso sa pag-access ng database. Para sa karamihan ng mga database, kabilang dito ang pagsasaayos ng database bilang read-only. Para sa mga serbisyo ng database tulad ng PostgreSQL o Azure SQL, dapat bigyan ang app ng read-only (SELECT) na role.

Ang pagpapatakbo ng app sa isang ligtas na kapaligiran ay higit pang nagpapahusay ng proteksyon. Sa mga senaryo ng enterprise, karaniwang inuutang at binabago ang data mula sa mga operasyon na sistema papunta sa isang read-only na database o data warehouse na may user-friendly na schema. Tinitiyak ng paraan na ito na ang data ay ligtas, optimized para sa performance at accessibility, at may limitadong access lamang ang app bilang read-only.

## Mga Sample Code

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## May Mga Karagdagang Tanong Tungkol sa Tool Use Design Patterns?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa iba pang mga nag-aaral, dumalo sa mga office hours, at sagutin ang iyong mga tanong tungkol sa AI Agents.

## Karagdagang mga Mapagkukunan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pangkalahatang-ideya ng Microsoft Agent Framework</a>


## Pagsusubok ng Agent na Ito (Opsyonal)

Pagkatapos mong matutunan kung paano mag-deploy ng mga agent sa [Lesson 16](../16-deploying-scalable-agents/README.md), maaari mong i-smoke-test ang `TravelToolAgent` ng araling ito (tinitingnan kung tinatawagan pa rin nito ang mga tool at sumasagot) gamit ang [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Tingnan ang [`tests/README.md`](../tests/README.md) para sa kung paano ito patakbuhin.

## Nakaraang Aralin

[Pag-unawa sa Agentic na Mga Disenyo ng Pattern](../03-agentic-design-patterns/README.md)

## Susunod na Aralin

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->