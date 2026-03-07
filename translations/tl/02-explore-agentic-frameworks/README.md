[![Paggalugad ng mga Framework ng AI Agent](../../../translated_images/tl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

# Galugarin ang mga Framework ng AI Agent

Ang mga AI agent framework ay mga platform ng software na idinisenyo upang pasimplehin ang paglikha, pag-deploy, at pamamahala ng mga AI agent. Ang mga framework na ito ay nagbibigay sa mga developer ng mga pre-built na component, abstraksiyon, at mga tool na nagpapabilis sa pagbuo ng kumplikadong mga sistema ng AI.

Tinutulungan ng mga framework na ito ang mga developer na magpokus sa natatanging aspeto ng kanilang mga aplikasyon sa pamamagitan ng pagbibigay ng mga standardized na paraan sa pangkaraniwang mga hamon sa pag-develop ng AI agent. Pinahusay nila ang scalability, accessibility, at kahusayan sa pagbuo ng mga sistema ng AI.

## Introduction 

Tatalakayin sa araling ito ang:

- Ano ang mga AI Agent Framework at ano ang maaaring makamit ng mga developer gamit ang mga ito?
- Paano magagamit ng mga koponan ang mga ito upang mabilis na mag-prototype, mag-iterate, at pahusayin ang kakayahan ng kanilang agent?
- Ano ang mga pagkakaiba sa pagitan ng mga framework at tool na nilikha ng Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> at ang <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Maaari ko bang direktang i-integrate ang aking umiiral na Azure ecosystem tools, o kailangan ko ng mga standalone na solusyon?
- Ano ang Azure AI Agents service at paano ito nakakatulong sa akin?

## Learning goals

Ang mga layunin ng araling ito ay tulungan kang maunawaan ang:

- Ang papel ng mga AI Agent Framework sa pag-develop ng AI.
- Paano gamitin ang mga AI Agent Framework upang bumuo ng mga intelligent agent.
- Pangunahing kakayahan na pinapagana ng mga AI Agent Framework.
- Ang mga pagkakaiba sa pagitan ng Microsoft Agent Framework at Azure AI Agent Service.

## What are AI Agent Frameworks and what do they enable developers to do?

Makakatulong sa iyo ang mga tradisyunal na AI Framework na i-integrate ang AI sa iyong mga app at gawing mas maganda ang mga ito sa mga sumusunod na paraan:

- **Personalization**: Maaaring suriin ng AI ang pag-uugali at mga kagustuhan ng user upang magbigay ng mga personalized na rekomendasyon, nilalaman, at karanasan.
Example: Ang mga streaming service tulad ng Netflix ay gumagamit ng AI para magmungkahi ng mga pelikula at palabas base sa kasaysayan ng panonood, na nagpapataas ng pakikipag-ugnayan at kasiyahan ng user.
- **Automation and Efficiency**: Maaaring i-automate ng AI ang mga paulit-ulit na gawain, pasimplehin ang workflow, at pagbutihin ang operational efficiency.
Example: Gumagamit ang mga customer service app ng AI-powered na chatbot upang humawak ng mga karaniwang katanungan, na nagpapababa ng oras ng pagtugon at nagbibigay-laya sa mga human agent para sa mas kumplikadong isyu.
- **Enhanced User Experience**: Maaaring pagandahin ng AI ang pangkalahatang karanasan ng user sa pamamagitan ng pagbibigay ng mga intelligent na tampok tulad ng voice recognition, natural language processing, at predictive text.
Example: Gumagamit ang mga virtual assistant tulad ng Siri at Google Assistant ng AI upang maunawaan at tumugon sa mga voice command, na nagpapadali sa pakikipag-ugnayan ng mga user sa kanilang mga device.

### That all sounds great right, so why do we need the AI Agent Framework?

Ang mga AI Agent framework ay kumakatawan sa higit pa kaysa sa mga simpleng AI framework. Idinisenyo ang mga ito upang payagan ang paglikha ng mga intelligent agent na maaaring makipag-ugnayan sa mga user, iba pang agent, at sa kapaligiran upang makamit ang partikular na mga layunin. Ang mga agent na ito ay maaaring magpakita ng autonomous na pag-uugali, gumawa ng mga desisyon, at umangkop sa mga nagbabagong kondisyon. Tingnan natin ang ilang pangunahing kakayahan na pinapagana ng mga AI Agent Framework:

- **Agent Collaboration and Coordination**: Pinapahintulutan ang paglikha ng maraming AI agent na maaaring magtrabaho nang magkakasama, makipagkomunika, at makipag-koordina upang lutasin ang kumplikadong mga gawain.
- **Task Automation and Management**: Nagbibigay ng mga mekanismo para sa pag-automate ng multi-step workflows, delegasyon ng gawain, at dynamic na pamamahala ng gawain sa pagitan ng mga agent.
- **Contextual Understanding and Adaptation**: Nilalagyan ang mga agent ng kakayahang maunawaan ang konteksto, umangkop sa nagbabagong kapaligiran, at gumawa ng mga desisyon batay sa real-time na impormasyon.

Sa buod, pinapayagan ka ng mga agent na gawin ang higit pa, dalhin ang automation sa mas mataas na antas, at lumikha ng mas intelligent na mga sistema na maaaring umangkop at matuto mula sa kanilang kapaligiran.

## How to quickly prototype, iterate, and improve the agent’s capabilities?

Mabilis ang pagbabago sa larangang ito, ngunit may ilang bagay na karaniwan sa karamihan ng mga AI Agent Framework na makakatulong sa iyo na mabilis na mag-prototype at mag-iterate — partikular ang mga module component, collaborative tools, at real-time learning. Talakayin natin ang mga ito:

- **Use Modular Components**: Nag-aalok ang mga AI SDK ng mga pre-built na component tulad ng AI at Memory connectors, function calling gamit ang natural language o code plugins, prompt templates, at higit pa.
- **Leverage Collaborative Tools**: Disenyuhin ang mga agent na may tiyak na mga tungkulin at gawain, na nagpapahintulot sa kanila na subukan at pinuhin ang collaborative workflows.
- **Learn in Real-Time**: Magpatupad ng feedback loops kung saan ang mga agent ay natututo mula sa mga interaksyon at inaayos ang kanilang pag-uugali nang dinamiko.

### Use Modular Components

Nag-aalok ang mga SDK tulad ng Microsoft Agent Framework ng mga pre-built na component tulad ng AI connectors, tool definitions, at agent management.

**How teams can use these**: Maaaring mabilis na buuin ng mga koponan ang mga component na ito upang lumikha ng functional na prototype nang hindi nagsisimula mula sa simula, na nagpapahintulot para sa mabilis na eksperimento at pag-iterate.

**How it works in practice**: Maaari mong gamitin ang pre-built na parser upang kunin ang impormasyon mula sa input ng user, isang memory module upang mag-imbak at kumuha ng data, at isang prompt generator upang makipag-ugnayan sa mga user, lahat nang hindi kailangang buuin ang mga component na ito mula sa simula.

**Example code**. Tingnan natin ang halimbawa kung paano mo magagamit ang Microsoft Agent Framework kasama ang `AzureAIProjectAgentProvider` upang mag-respond ang modelo sa input ng user gamit ang tool calling:

``` python
# Halimbawa ng Microsoft Agent Framework sa Python

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Magtakda ng isang halimbawa ng tool function para mag-book ng biyahe
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
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

Makikita mo mula sa halimbawang ito kung paano mo magagamit ang pre-built parser upang kunin ang mahahalagang impormasyon mula sa input ng user, tulad ng pinagmulan, destinasyon, at petsa ng request para sa booking ng flight. Pinapahintulutan ka ng modular na pamamaraang ito na mag-focus sa high-level na lohika.

### Leverage Collaborative Tools

Pinapadali ng mga framework tulad ng Microsoft Agent Framework ang paglikha ng maraming agent na maaaring magtrabaho nang magkakasama.

**How teams can use these**: Maaaring magdisenyo ang mga koponan ng mga agent na may espesipikong mga tungkulin at gawain, na nagpapahintulot sa kanila na subukan at pinuhin ang collaborative workflows at pagbutihin ang kabuuang kahusayan ng sistema.

**How it works in practice**: Maaari kang lumikha ng isang koponan ng mga agent kung saan ang bawat agent ay may espesyal na tungkulin, tulad ng data retrieval, analysis, o decision-making. Ang mga agent na ito ay maaaring mag-komunika at magbahagi ng impormasyon upang makamit ang isang karaniwang layunin, tulad ng pagsagot sa isang query ng user o pagtapos ng isang gawain.

**Example code (Microsoft Agent Framework)**:

```python
# Lumilikha ng maraming ahente na nagtutulungan gamit ang Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Ahente ng Pagkuha ng Datos
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Ahente ng Pagsusuri ng Datos
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Patakbuhin ang mga ahente nang sunud-sunod sa isang gawain
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Makikita sa naunang code kung paano ka makakalikha ng isang gawain na kinapapalooban ng maraming agent na nagtutulungan upang suriin ang data. Ang bawat agent ay gumaganap ng isang partikular na tungkulin, at ang gawain ay isinasagawa sa pamamagitan ng pag-koordina ng mga agent upang makamit ang inaasahang resulta. Sa pamamagitan ng paglikha ng nakatalagang mga agent na may espesyalisadong mga tungkulin, maaari mong pagbutihin ang kahusayan at pagganap ng gawain.

### Learn in Real-Time

Nagbibigay ang mga advanced na framework ng kakayahan para sa real-time na pag-unawa sa konteksto at pag-aangkop.

**How teams can use these**: Maaaring magpatupad ang mga koponan ng mga feedback loop kung saan ang mga agent ay natututo mula sa mga interaksyon at inaayos ang kanilang pag-uugali nang dinamiko, na nagreresulta sa tuloy-tuloy na pagpapabuti at pagpinuhin ng mga kakayahan.

**How it works in practice**: Maaaring suriin ng mga agent ang feedback ng user, data ng kapaligiran, at mga resulta ng gawain upang i-update ang kanilang knowledge base, ayusin ang mga algorithm ng paggawa ng desisyon, at pagbutihin ang pagganap sa paglipas ng panahon. Pinapahintulutan ng prosesong ito ng paulit-ulit na pagkatuto ang mga agent na umangkop sa nagbabagong kondisyon at mga kagustuhan ng user, pinapahusay ang kabuuang pagiging epektibo ng sistema.

## What are the differences between the Microsoft Agent Framework and Azure AI Agent Service?

Maraming paraan upang ihambing ang mga pamamaraang ito, ngunit tingnan natin ang ilang mahahalagang pagkakaiba sa mga tuntunin ng kanilang disenyo, kakayahan, at target na mga use case:

## Microsoft Agent Framework (MAF)

Nagbibigay ang Microsoft Agent Framework ng isang streamlined na SDK para sa pagbuo ng mga AI agent gamit ang `AzureAIProjectAgentProvider`. Pinahihintulutan nito ang mga developer na lumikha ng mga agent na gumagamit ng Azure OpenAI models na may built-in na tool calling, conversation management, at enterprise-grade security sa pamamagitan ng Azure identity.

**Use Cases**: Pagbuo ng production-ready na mga AI agent na may tool use, multi-step workflows, at mga senaryong enterprise integration.

Narito ang ilang mahahalagang core concepts ng Microsoft Agent Framework:

- **Agents**. Ang isang agent ay nililikha via `AzureAIProjectAgentProvider` at kino-configure na may pangalan, instructions, at mga tool. Ang agent ay maaaring:
  - **Process user messages** at bumuo ng mga tugon gamit ang Azure OpenAI models.
  - **Call tools** nang awtomatiko base sa konteksto ng pag-uusap.
  - **Maintain conversation state** sa maraming interaksyon.

  Narito ang isang code snippet na nagpapakita kung paano lumikha ng isang agent:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Tools**. Sinusuportahan ng framework ang pagde-define ng mga tool bilang mga Python function na maaaring i-invoke ng agent nang awtomatiko. Ang mga tool ay nirerehistro kapag nililikha ang agent:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Multi-Agent Coordination**. Maaari kang lumikha ng maraming agent na may iba't ibang espesyalisasyon at i-koordina ang kanilang trabaho:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identity Integration**. Gumagamit ang framework ng `AzureCliCredential` (o `DefaultAzureCredential`) para sa secure, keyless authentication, na inaalis ang pangangailangan na pamahalaan ang mga API key nang direkta.

## Azure AI Agent Service

Ang Azure AI Agent Service ay isang mas bagong karagdagan, ipinakilala sa Microsoft Ignite 2024. Pinapayagan nito ang pag-develop at pag-deploy ng mga AI agent na may mas flexible na mga modelo, tulad ng direktang pagtawag sa open-source na LLMs gaya ng Llama 3, Mistral, at Cohere.

Nagbibigay ang Azure AI Agent Service ng mas matibay na enterprise security mechanisms at mga paraan ng pag-iimbak ng data, na ginagawa itong angkop para sa mga enterprise application.

Gumagana ito out-of-the-box kasama ang Microsoft Agent Framework para sa pagbuo at pag-deploy ng mga agent.

Kasulukuyan itong nasa Public Preview at sumusuporta sa Python at C# para sa pagbuo ng mga agent.

Gamit ang Azure AI Agent Service Python SDK, maaari tayong lumikha ng agent na may user-defined na tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Tukuyin ang mga function ng tool
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
        model="gpt-4o-mini",
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

### Core concepts

Mayroon ang Azure AI Agent Service ng mga sumusunod na core concepts:

- **Agent**. Nag-iintegrate ang Azure AI Agent Service sa Microsoft Foundry. Sa loob ng AI Foundry, kumikilos ang isang AI Agent bilang isang "smart" microservice na maaaring gamitin upang sumagot ng mga tanong (RAG), magsagawa ng mga aksyon, o ganap na i-automate ang mga workflow. Nakakamit nito ito sa pamamagitan ng pagsasama ng lakas ng generative AI models sa mga tool na nagpapahintulot dito na ma-access at makipag-interact sa totoong mga pinagmumulan ng data. Narito ang isang halimbawa ng isang agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Sa halimbawang ito, nilikha ang isang agent gamit ang model na `gpt-4o-mini`, isang pangalan na `my-agent`, at mga instructions na `You are helpful agent`. Ang agent ay binigyan ng mga tool at resources upang magsagawa ng mga gawain sa pag-interpret ng code.

- **Thread and messages**. Ang thread ay isa pang mahalagang konsepto. Kinakatawan nito ang isang pag-uusap o interaksyon sa pagitan ng isang agent at isang user. Maaaring gamitin ang mga thread upang subaybayan ang progreso ng isang pag-uusap, mag-imbak ng impormasyon ng konteksto, at pamahalaan ang estado ng interaksyon. Narito ang isang halimbawa ng isang thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Sa naunang code, isang thread ang nilikha. Pagkatapos noon, isang mensahe ang ipinadala sa thread. Sa pamamagitan ng pagtawag sa `create_and_process_run`, hiniling ang agent na magsagawa ng trabaho sa thread. Sa wakas, kinukuha at nilalagda ang mga mensahe upang makita ang tugon ng agent. Ipinapakita ng mga mensahe ang progreso ng pag-uusap sa pagitan ng user at ng agent. Mahalagang maunawaan na ang mga mensahe ay maaaring magkakaibang uri tulad ng text, image, o file; ibig sabihin, ang gawa ng mga agent ay maaaring magresulta sa halimbawa sa isang imahe o isang text na tugon. Bilang isang developer, maaari mong gamitin ang impormasyong ito upang karagdagang iproseso ang tugon o ipakita ito sa user.

- **Integrates with the Microsoft Agent Framework**. Gumagana nang walang putol ang Azure AI Agent Service kasama ang Microsoft Agent Framework, na nangangahulugang maaari kang bumuo ng mga agent gamit ang `AzureAIProjectAgentProvider` at i-deploy ang mga ito sa pamamagitan ng Agent Service para sa mga senaryong production.

**Use Cases**: Dinisenyo ang Azure AI Agent Service para sa mga enterprise application na nangangailangan ng secure, scalable, at flexible na pag-deploy ng mga AI agent.

## What's the difference between these approaches?
 
Mukhang may overlap, ngunit may ilang mahahalagang pagkakaiba sa mga tuntunin ng kanilang disenyo, kakayahan, at target na mga use case:
 
- **Microsoft Agent Framework (MAF)**: Isang production-ready SDK para sa pagbuo ng mga AI agent. Nagbibigay ito ng streamlined na API para sa paglikha ng mga agent na may tool calling, conversation management, at Azure identity integration.
- **Azure AI Agent Service**: Isang platform at deployment service sa Azure Foundry para sa mga agent. Nag-aalok ito ng built-in na konektividad sa mga serbisyo katulad ng Azure OpenAI, Azure AI Search, Bing Search at code execution.
 
Hindi pa rin sigurado kung alin ang pipiliin?

### Use Cases
 
Subukan nating tulungan ka sa pamamagitan ng pagdaan sa ilang mga karaniwang use case:
 
> Q: Gumagawa ako ng production AI agent applications at gusto kong magsimula nang mabilis
>

>A: Magandang pagpipilian ang Microsoft Agent Framework. Nagbibigay ito ng isang simple, Pythonic na API via `AzureAIProjectAgentProvider` na nagpapahintulot sa iyo na mag-defina ng mga agent na may mga tool at instructions sa ilang linya ng code.

>Q: Kailangan ko ng enterprise-grade deployment na may Azure integrations tulad ng Search at code execution
>
> A: Mas nababagay ang Azure AI Agent Service. Isa itong platform service na nagbibigay ng built-in na kakayahan para sa maraming modelo, Azure AI Search, Bing Search at Azure Functions. Pinapadali nito ang pagbuo ng iyong mga agent sa Foundry Portal at ang pag-deploy ng mga ito sa malakihang gamit.
 
> Q: Nalilito pa rin ako, bigyan mo na lang ako ng isang opsyon
>
> A: Magsimula sa Microsoft Agent Framework para buuin ang iyong mga agent, at pagkatapos ay gamitin ang Azure AI Agent Service kapag kailangan mong i-deploy at i-scale ang mga ito sa production. Pinahihintulutan ka ng pamamaraang ito na mag-iterate nang mabilis sa iyong agent logic habang may malinaw na landas patungo sa enterprise deployment.
 
Ibuod natin ang mga pangunahing pagkakaiba sa isang talahanayan:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
Ang sagot ay oo, maaari mong i-integrate nang direkta ang iyong kasalukuyang mga tool sa Azure ecosystem sa Azure AI Agent Service, lalo na dahil ito ay binuo upang gumana nang maayos kasama ang iba pang mga serbisyo ng Azure. Halimbawa, maaari mong i-integrate ang Bing, Azure AI Search, at Azure Functions. Mayroon ding malalim na integrasyon sa Microsoft Foundry.

Ang Microsoft Agent Framework ay nag-iintegrate din sa mga serbisyo ng Azure sa pamamagitan ng `AzureAIProjectAgentProvider` at Azure identity, na nagbibigay-daan sa iyo na tawagan ang mga serbisyo ng Azure nang direkta mula sa iyong mga tool ng agent.

## Mga Halimbawang Code

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## May iba ka pa bang mga tanong tungkol sa AI Agent Frameworks?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para makipagkita sa iba pang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Mga Sanggunian

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Nakaraang Aralin

[Panimula sa AI Agents at Mga Kaso ng Paggamit](../01-intro-to-ai-agents/README.md)

## Susunod na Aralin

[Pag-unawa sa Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtanggi ng pananagutan**:
Ang dokumentong ito ay naisalin gamit ang serbisyong pagsasalin na pinapagana ng AI na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinagmumulan ng opisyal na impormasyon. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling ginagawa ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->