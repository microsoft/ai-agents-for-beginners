[![Paggalugad sa mga AI Agent Framework](../../../translated_images/tl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

# Galugarin ang mga AI Agent Framework

Ang mga AI agent framework ay mga plataporma ng software na dinisenyo upang gawing mas madali ang paggawa, pag-deploy, at pamamahala ng mga AI agent. Nagbibigay ang mga framework na ito sa mga developer ng mga pre-built na bahagi, abstraction, at mga kasangkapan na nagpapadali sa pagbuo ng mga komplikadong AI system.

Tinutulungan ng mga framework na ito ang mga developer na magpokus sa mga natatanging aspeto ng kanilang mga aplikasyon sa pamamagitan ng pagbibigay ng standardized na mga pamamaraan sa mga karaniwang hamon sa AI agent development. Pinapahusay nila ang scalability, accessibility, at kahusayan sa pagbuo ng mga AI system.

## Panimula 

Saklaw ng araling ito:

- Ano ang mga AI Agent Framework at ano ang kaya nilang gawin ng mga developer?
- Paano magagamit ng mga koponan ang mga ito upang mabilis na mag-prototype, mag-iterate, at pahusayin ang kakayahan ng kanilang mga agent?
- Ano ang mga pagkakaiba ng mga framework at kasangkapang ginawa ng Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> at ang <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Maaari ko bang direktang gamitin ang mga kasangkapang Azure na meron na ako, o kailangan ko ba ng mga standalone na solusyon?
- Ano ang Microsoft Foundry Agent Service at paano ako nito natutulungan?

## Mga Layunin sa Pagkatuto

Layunin ng araling ito na tulungan kang maunawaan:

- Ang papel ng AI Agent Frameworks sa pagbuo ng AI.
- Kung paano gamitin ang AI Agent Frameworks para makabuo ng mga matatalinong agent.
- Mga pangunahing kakayahan na posible sa AI Agent Frameworks.
- Ang mga pagkakaiba ng Microsoft Agent Framework at Microsoft Foundry Agent Service.

## Ano ang mga AI Agent Framework at ano ang kaya nitong gawin ng mga developer?

Maaaring makatulong ang mga tradisyunal na AI Framework upang maisama ang AI sa iyong mga app at pagandahin ang mga ito sa mga sumusunod na paraan:

- **Personalization**: Kayang suriin ng AI ang gawi at kagustuhan ng user upang magbigay ng mga personalized na rekomendasyon, nilalaman, at karanasan.
Halimbawa: Ginagamit ng mga streaming service tulad ng Netflix ang AI upang magmungkahi ng mga pelikula at palabas base sa kasaysayan ng panonood, na nagpapahusay ng pakikipag-ugnayan at kasiyahan ng user.
- **Automation at Kahusayan**: Kayang i-automate ng AI ang mga paulit-ulit na gawain, pasimplehin ang mga workflow, at pagbutihin ang operational na kahusayan.
Halimbawa: Gumagamit ang mga customer service app ng AI-powered chatbots upang asikasuhin ang mga karaniwang tanong, nagpapabawas ng oras ng sagot at nagpapalaya ng mga human agent para sa mas kumplikadong isyu.
- **Pinahusay na Karanasan ng User**: Kayang pagbutihin ng AI ang pangkalahatang karanasan ng user sa pamamagitan ng pagbibigay ng matatalinong feature tulad ng voice recognition, natural language processing, at predictive text.
Halimbawa: Gumagamit ang mga virtual assistant tulad ng Siri at Google Assistant ng AI upang maintindihan at tumugon sa mga voice command, na nagpapadali sa pakikipag-ugnayan ng user sa kanilang mga device.

### Maganda ang lahat ng iyon, bakit nga ba kailangan natin ang AI Agent Framework?

Ang mga AI Agent framework ay higit pa sa mga AI framework lamang. Dinisenyo ang mga ito upang magpayagan ng paglikha ng matatalinong agent na maaaring makipag-ugnayan sa mga user, ibang agent, at sa kapaligiran upang makamit ang mga tiyak na layunin. Maaari silang magpakita ng autonomous na pag-uugali, gumawa ng mga desisyon, at mag-adapt sa pagbabago ng kalagayan. Tingnan natin ang ilang pangunahing kakayahan na pinapayagan ng AI Agent Frameworks:

- **Pakikipagtulungan at Koordinasyon ng Agent**: Pinapayagan ang paglikha ng maraming AI agent na maaaring magtulungan, makipagkomunikasyon, at makipag-ugnayan upang lutasin ang mga komplikadong gawain.
- **Automation at Pamamahala ng Gawain**: Nagbibigay ng mga mekanismo para i-automate ang multi-step na workflow, pagtatalaga ng gawain, at dynamic na pamamahala ng gawain sa mga agent.
- **Kontextwal na Pag-unawa at Adaptasyon**: Nilalapatan ang mga agent ng kakayahang maintindihan ang konteksto, mag-adapt sa nagbabagong kapaligiran, at gumawa ng desisyon base sa real-time na impormasyon.

Sa kabuuan, pinapayagan ka ng mga agent na gawin ang higit pa, dalhin ang automation sa mas mataas na antas, at lumikha ng mas matatalinong sistema na kayang mag-adapt at matuto mula sa kanilang kapaligiran.

## Paano mabilis na makapag-prototype, mag-iterate, at pahusayin ang kakayahan ng agent?

Mabilis ang pagbabago sa larangang ito, ngunit may ilang mga bagay na karaniwan sa karamihan ng AI Agent Frameworks na makakatulong sa mabilisang pag-prototype at pag-iterate tulad ng module components, collaborative tools, at real-time learning. Talakayin natin ang mga ito:

- **Gamitin ang Modular na mga Bahagi**: Nag-aalok ang AI SDKs ng mga pre-built na bahagi tulad ng AI at Memory connectors, function calling gamit ang natural na wika o code plugins, prompt templates, at iba pa.
- **Gamitin ang mga Collaborative Tool**: Disenyuhin ang mga agent na may tiyak na papel at mga gawain, upang matest at mapino ang mga collaborative workflows.
- **Matuto nang Real-Time**: Magpatupad ng mga feedback loops kung saan natututo ang mga agent mula sa mga interaksyon at inaayos ang kanilang pag-uugali nang dinamiko.

### Gamitin ang Modular na mga Bahagi

Nag-aalok ang mga SDK tulad ng Microsoft Agent Framework ng mga pre-built na bahagi tulad ng AI connectors, tool definitions, at pamamahala ng agent.

**Paano ito magagamit ng mga koponan**: Maaaring mabilis na pagsamahin ng mga koponan ang mga bahagi upang makabuo ng isang functional prototype nang hindi nagsisimula mula sa wala, na nagpapahintulot sa mabilisang eksperimento at pag-iterate.

**Paano ito gumagana sa praktis**: Maaari kang gumamit ng pre-built parser upang mag-extract ng impormasyon mula sa input ng user, isang memory module upang mag-imbak at kumuha ng data, at isang prompt generator upang makipag-ugnayan sa mga user, lahat nang hindi kinakailangang buuin ang mga bahaging ito mula sa simula.

**Halimbawa ng code**. Tingnan natin ang isang halimbawa kung paano mo magagamit ang Microsoft Agent Framework gamit ang `FoundryChatClient` upang tumugon ang model sa input ng user gamit ang tool calling:

``` python
# Microsoft Agent Framework Halimbawa sa Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Tukuyin ang isang halimbawa ng tool function para mag-book ng biyahe
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Halimbawa ng output: Ang iyong flight papuntang New York sa Enero 1, 2025, ay matagumpay nang na-book. Maligayang paglalakbay! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Makikita mo sa halimbawang ito kung paano mo nagagamit ang pre-built parser upang kunin ang mahahalagang impormasyon mula sa input ng user, tulad ng pinagmulan, destinasyon, at petsa ng flight booking request. Pinapayagan ka ng modular na paraan na ito na magpokus sa high-level na lohika.

### Gamitin ang mga Collaborative Tool

Pinapadali ng mga framework tulad ng Microsoft Agent Framework ang paglikha ng maramihang agent na maaaring magtulungan.

**Paano ito magagamit ng mga koponan**: Maaaring magdisenyo ang mga koponan ng mga agent na may tiyak na papel at mga gawain, na nagbibigay-daan upang matest at mapino ang mga collaborative workflow at mapabuti ang kabuuang kahusayan ng sistema.

**Paano ito gumagana sa praktis**: Maaari kang lumikha ng isang grupo ng mga agent kung saan bawat isa ay may espesyal na tungkulin, tulad ng data retrieval, analysis, o paggawa ng desisyon. Maaaring magkomunikasyon ang mga agent at magbahagi ng impormasyon upang makamit ang isang pangkalahatang layunin, tulad ng pagsagot sa tanong ng user o pagtapos ng isang gawain.

**Halimbawa ng code (Microsoft Agent Framework)**:

```python
# Lumilikha ng maramihang ahente na nagtutulungan gamit ang Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Ahente para sa Pagkuha ng Datos
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Ahente para sa Pagsusuri ng Datos
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Patakbuhin ang mga ahente nang sunod-sunod sa isang gawain
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Makikita mo sa naunang code kung paano gumawa ng isang gawain na humihingi ng pagtutulungan ng maramihang agent upang suriin ang data. Bawat agent ay gumaganap ng isang tiyak na tungkulin, at ang gawain ay isinasagawa sa pamamagitan ng koordinasyon ng mga agent upang makamit ang nais na resulta. Sa paggawa ng dedicated agents na may mga espesyal na papel, mapapabuti mo ang kahusayan at performance ng gawain.

### Matuto nang Real-Time

Nagbibigay ang advanced na mga framework ng mga kakayahan para sa real-time na pag-unawa sa konteksto at adaptasyon.

**Paano ito magagamit ng mga koponan**: Maaaring magpatupad ang mga koponan ng mga feedback loop kung saan natututo ang mga agent mula sa mga interaksyon at inaayos ang kanilang pag-uugali nang dinamiko, na nagreresulta sa tuloy-tuloy na pagpapabuti at pagpino ng kakayahan.

**Paano ito gumagana sa praktis**: Maaaring suriin ng mga agent ang feedback ng user, data ng kapaligiran, at mga kinalabasan ng gawain upang i-update ang kanilang knowledge base, ayusin ang mga decision-making algorithm, at pahusayin ang performance sa paglipas ng panahon. Pinapayagan ng iteratibong prosesong ito sa pagkatuto ang mga agent na mag-adapt sa mga nagbabagong kalagayan at kagustuhan ng user, na nagpapahusay ng kabuuang epektibidad ng sistema.

## Ano ang mga pagkakaiba ng Microsoft Agent Framework at Microsoft Foundry Agent Service?

Maraming paraan upang ihambing ang mga pamamaraang ito, ngunit tingnan natin ang ilang pangunahing pagkakaiba sa kanilang disenyo, kakayahan, at mga target na gamit:

## Microsoft Agent Framework (MAF)

Nagbibigay ang Microsoft Agent Framework ng isang pinasimpleng SDK para sa paggawa ng AI agent gamit ang `FoundryChatClient`. Pinapayagan nito ang mga developer na gumawa ng mga agent na gumagamit ng Azure OpenAI models na may built-in na tool calling, conversation management, at enterprise-grade na seguridad sa pamamagitan ng Azure identity.

**Mga Gamit**: Pagbuo ng mga production-ready AI agent na may tool use, multi-step workflows, at mga senaryo ng enterprise integration.

Narito ang ilang mahahalagang pangunahing konsepto ng Microsoft Agent Framework:

- **Mga Agent**. Ang isang agent ay nilikha gamit ang `FoundryChatClient` at kinokonpigura gamit ang pangalan, mga tagubilin, at mga tool. Ang agent ay maaaring:
  - **Proseso ang mga mensahe ng user** at bumuo ng mga tugon gamit ang Azure OpenAI models.
  - **Tumawag ng mga tool** nang awtomatiko base sa konteksto ng pag-uusap.
  - **Pamahalaan ang estado ng pag-uusap** sa iba't ibang interaksyon.

  Narito ang isang code snippet na nagpapakita kung paano gumawa ng isang agent:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Mga Tool**. Sinusuportahan ng framework ang pagdeklara ng mga tool bilang mga Python function na maaaring tawagin ng agent nang awtomatiko. Nakarehistro ang mga tool kapag nililikha ang agent:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Multi-Agent Coordination**. Maaari kang gumawa ng maraming agent na may iba't ibang espesyalidad at i-coordinate ang kanilang gawain:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integrasyon sa Azure Identity**. Ginagamit ng framework ang `AzureCliCredential` (o `DefaultAzureCredential`) para sa ligtas, keyless na authentication, na inaalis ang pangangailangan na direktang pamahalaan ang API keys.

## Microsoft Foundry Agent Service

Ang Microsoft Foundry Agent Service ay isang mas bagong karagdagan, ipinakilala sa Microsoft Ignite 2024. Pinapayagan nito ang pagbuo at pag-deploy ng AI agent na may mas flexible na mga modelo, tulad ng direktang pagtawag sa open-source na LLMs tulad ng Llama 3, Mistral, at Cohere.

Nagbibigay ang Microsoft Foundry Agent Service ng mas malakas na mekanismo ng enterprise security at mga pamamaraan ng pag-iimbak ng data, kaya angkop ito para sa mga aplikasyon ng enterprise.

Gumagana ito kaagad sa Microsoft Agent Framework para sa pagbuo at pag-deploy ng mga agent.

Nasa Public Preview pa ang serbisyong ito at sumusuporta sa Python at C# para sa paggawa ng mga agent.

Sa paggamit ng Microsoft Foundry Agent Service Python SDK, maaari tayong gumawa ng agent na may user-defined na tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Tukuyin ang mga function ng kasangkapan
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Mga Pangunahing Konsepto

May mga sumusunod na pangunahing konsepto ang Microsoft Foundry Agent Service:

- **Agent**. Nakikipag-integrate ang Microsoft Foundry Agent Service sa Microsoft Foundry. Sa loob ng Microsoft Foundry, ang AI Agent ay gumaganap bilang isang "smart" microservice na maaaring gamitin upang sumagot sa mga tanong (RAG), magsagawa ng mga aksyon, o ganap na mag-automate ng mga workflow. Nakakamit ito sa pamamagitan ng pagsasama ng kapangyarihan ng generative AI models at mga tool na nagpapahintulot dito na ma-access at makipag-ugnayan sa mga totoong pinagkukunan ng data. Narito ang isang halimbawa ng isang agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Sa halimbawang ito, isang agent ang nilikha gamit ang modelong `gpt-5-mini`, pangalang `my-agent`, at mga tagubiling `You are helpful agent`. Nilagyan ang agent ng mga tool at resources para magsagawa ng mga gawain sa code interpretation.

- **Thread at mga mensahe**. Ang thread ay isa pang mahalagang konsepto. Ito ay kumakatawan sa pag-uusap o interaksyon sa pagitan ng agent at ng user. Maaaring gamitin ang mga thread upang subaybayan ang progreso ng pag-uusap, mag-imbak ng impormasyon ng konteksto, at pamahalaan ang estado ng interaksyon. Narito ang isang halimbawa ng thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Hilingin sa ahente na magsagawa ng trabaho sa thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Kunin at i-log lahat ng mga mensahe upang makita ang tugon ng ahente
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Sa naunang code, isang thread ang nilikha. Pagkatapos ay isang mensahe ang ipinadala sa thread. Sa pagtawag ng `create_and_process_run`, hinihiling sa agent na magsagawa ng trabaho sa thread. Sa wakas, kinukuha at nirerecord ang mga mensahe upang makita ang tugon ng agent. Ipinapakita ng mga mensahe ang progreso ng pag-uusap sa pagitan ng user at agent. Mahalaga ring maunawaan na maaaring iba-iba ang uri ng mensahe tulad ng teksto, larawan, o file, halimbawa ang output ng trabaho ng agent ay maaaring isang larawan o tugon na teksto. Bilang developer, maaari mong gamitin ang impormasyong ito para iproseso pa ang tugon o ipakita ito sa user.

- **Nakikipag-integrate sa Microsoft Agent Framework**. Gumagana nang maayos ang Microsoft Foundry Agent Service kasama ang Microsoft Agent Framework, ibig sabihin maaari kang gumawa ng mga agent gamit ang `FoundryChatClient` at i-deploy ang mga ito sa pamamagitan ng Agent Service para sa mga production na senaryo.

**Mga Gamit**: Ang Microsoft Foundry Agent Service ay dinisenyo para sa mga enterprise application na nangangailangan ng secure, scalable, at flexible na pag-deploy ng AI agent.

## Ano ang pagkakaiba ng mga pamamaraang ito?
 
Tunog parang magkakatulad sila, ngunit may ilang mahahalagang pagkakaiba sa kanilang disenyo, kakayahan, at mga target na gamit:
 
- **Microsoft Agent Framework (MAF)**: Isang production-ready SDK para sa paggawa ng AI agent. Nagbibigay ito ng pinasimpleng API para sa paglikha ng mga agent na may tool calling, conversation management, at Azure identity integration.
- **Microsoft Foundry Agent Service**: Isang plataporma at serbisyo sa Microsoft Foundry para sa mga agent. Nag-aalok ito ng built-in na konektibidad sa mga serbisyo tulad ng Azure OpenAI, Azure AI Search, Bing Search, at code execution.
 
Hindi ka pa rin sigurado kung alin ang pipiliin?

### Mga Gamit
 
Tingnan natin kung matutulungan ka namin sa pamamagitan ng pagdaan sa mga karaniwang gamit:
 
> Q: Gumagawa ako ng production AI agent applications at gusto ko agad magsimula
>

>A: Magandang pagpipilian ang Microsoft Agent Framework. Nagbibigay ito ng simple, Pythonic API sa pamamagitan ng `FoundryChatClient` na nagpapahintulot sa iyong magtakda ng mga agent na may mga tool at tagubilin sa loob ng ilang linya ng code lang.

>Q: Kailangan ko ng enterprise-grade na pag-deploy na may mga Azure integration tulad ng Search at code execution
>
> A: Ang Microsoft Foundry Agent Service ang pinakaangkop. Isa itong platform service na may built-in na kakayahan para sa maraming modelo, Azure AI Search, Bing Search, at Azure Functions. Pinapadali nito ang paggawa ng mga agent sa Foundry Portal at pag-deploy sa malaking sukat.
 
> Q: Nalilito pa rin ako, bigyan mo na lang ako ng isang opsyon
>
> A: Magsimula ka sa Microsoft Agent Framework para gumawa ng mga agent, at gamitin ang Microsoft Foundry Agent Service kapag kailangan mong i-deploy at i-scale sa production. Pinapahintulutan ka nitong mabilis na mag-iterate sa iyong agent logic habang may malinaw na landas sa enterprise deployment.
 
Balikan natin ang mga pangunahing pagkakaiba sa isang talahanayan:

| Framework | Pokus | Pangunahing Konsepto | Mga Gamit |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Pinasimpleng agent SDK na may tool calling | Mga Agent, Tool, Azure Identity | Pagbuo ng AI agent, paggamit ng tool, multi-step workflow |
| Microsoft Foundry Agent Service | Flexible na mga modelo, seguridad sa enterprise, code generation, tool calling | Modularity, Pakikipagtulungan, Pag-oorganisa ng Proseso | Secure, scalable, at flexible na pag-deploy ng AI agent |

## Maaari ko bang direktang gamitin ang mga kasangkapang Azure na meron na ako, o kailangan ko ba ng mga standalone na solusyon?


Ang sagot ay oo, maaari mong direktang isama ang iyong umiiral na Azure ecosystem tools sa Microsoft Foundry Agent Service lalo na, dahil ito ay ginawa upang gumana nang maayos kasama ang iba pang mga serbisyo ng Azure. Maaari mong isama ang Bing, Azure AI Search, at Azure Functions bilang halimbawa. Mayroon ding malalim na integrasyon sa Microsoft Foundry.

Ang Microsoft Agent Framework ay nag-iintegrate din sa Azure services sa pamamagitan ng `FoundryChatClient` at Azure identity, na nagpapahintulot sa iyo na tawagan ang mga Azure services nang direkta mula sa iyong mga tool ng ahente.

## Mga Halimbawang Code

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## May Ibang Tanong Tungkol sa AI Agent Frameworks?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para makipagkita sa ibang mga nag-aaral, dumalo sa office hours, at makuha ang mga sagot sa iyong mga tanong tungkol sa AI Agents.

## Mga Sanggunian

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Nakaraang Aralin

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Susunod na Aralin

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->