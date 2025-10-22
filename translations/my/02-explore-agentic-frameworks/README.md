<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86b9c2b24da3b3e61711182ffa72601c",
  "translation_date": "2025-09-29T23:02:13+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "my"
}
-->
[![AI Agent Frameworks ကိုလေ့လာခြင်း](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.my.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ဤသင်ခန်းစာ၏ဗီဒီယိုကိုကြည့်ရန် အထက်ပါပုံကိုနှိပ်ပါ)_

# AI Agent Frameworks ကိုလေ့လာပါ

AI agent frameworks သည် AI အေးဂျင့်များကို ဖန်တီးခြင်း၊ တင်သွင်းခြင်းနှင့် စီမံခန့်ခွဲခြင်းကို လွယ်ကူစေရန် ရည်ရွယ်ထားသော ဆော့ဖ်ဝဲပလက်ဖောင်းများဖြစ်သည်။ ဤ frameworks များသည် ဖွံ့ဖြိုးတိုးတက်သော AI စနစ်များကို ဖွံ့ဖြိုးတိုးတက်စေရန် အဆင့်မြင့် components များ၊ အကျဉ်းချုပ်များနှင့် tools များကို ပံ့ပိုးပေးသည်။

ဤ frameworks များသည် AI agent ဖွံ့ဖြိုးတိုးတက်မှုတွင် ရှေ့ဆောင်သော စိန်ခေါ်မှုများအတွက် စံပြနည်းလမ်းများကို ပံ့ပိုးပေးခြင်းအားဖြင့် developer များကို သူတို့၏ application များ၏ ထူးခြားသောအပိုင်းများအပေါ် အာရုံစိုက်စေရန် ကူညီပေးသည်။ AI စနစ်များကို ဖွံ့ဖြိုးတိုးတက်စေရန် scalability, accessibility, နှင့် efficiency ကို တိုးတက်စေသည်။

## အကျဉ်းချုပ်

ဤသင်ခန်းစာတွင် အောက်ပါအကြောင်းအရာများကို လေ့လာမည်ဖြစ်သည်-

- AI Agent Frameworks ဆိုတာဘာလဲ၊ developer များအတွက် ဘာတွေကို အကျိုးကျေးဇူးပေးနိုင်မလဲ?
- အဖွဲ့များသည် အေးဂျင့်၏စွမ်းရည်များကို prototype, iterate, နှင့် တိုးတက်စေရန် ဤ frameworks များကို ဘယ်လိုအသုံးပြုနိုင်မလဲ?
- Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, နှင့် <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> တို့၏ frameworks နှင့် tools များအကြားကွာခြားချက်များကဘာလဲ?
- Azure ecosystem tools များကို တိုက်ရိုက်ပေါင်းစည်းနိုင်မလား၊ သို့မဟုတ် standalone solutions များလိုအပ်ပါသလား?
- Azure AI Agents service ဆိုတာဘာလဲ၊ ဒါကဘယ်လိုအကျိုးကျေးဇူးပေးနိုင်မလဲ?

## သင်ယူရမည့်ရည်ရွယ်ချက်များ

ဤသင်ခန်းစာ၏ရည်ရွယ်ချက်များမှာ-

- AI Agent Frameworks ၏ AI ဖွံ့ဖြိုးတိုးတက်မှုတွင် အရေးပါမှုကို နားလည်စေရန်။
- AI Agent Frameworks ကို အသုံးပြု၍ အာဏာရှိသော အေးဂျင့်များကို ဖန်တီးနိုင်ရန်။
- AI Agent Frameworks မှပေးသော အဓိကစွမ်းရည်များကို နားလည်ရန်။
- AutoGen, Semantic Kernel, နှင့် Azure AI Agent Service တို့၏ ကွာခြားချက်များကို နားလည်ရန်။

## AI Agent Frameworks ဆိုတာဘာလဲ၊ developer များအတွက် ဘာတွေကို အကျိုးကျေးဇူးပေးနိုင်မလဲ?

ရိုးရာ AI Frameworks များသည် AI ကို app များတွင် ပေါင်းစည်းရန်နှင့် အောက်ပါနည်းလမ်းများဖြင့် app များကို ပိုမိုကောင်းမွန်စေရန် ကူညီပေးနိုင်သည်-

- **Personalization**: AI သည် အသုံးပြုသူ၏ အပြုအမူနှင့် အကြိုက်အရွေးများကို ခွဲခြားလေ့လာပြီး အကြံပြုချက်များ၊ အကြောင်းအရာများနှင့် အတွေ့အကြုံများကို တိုင်းတာပေးနိုင်သည်။
ဥပမာ- Netflix ကဲ့သို့သော streaming services များသည် AI ကို အသုံးပြု၍ ကြည့်ရှုမှုမှတ်တမ်းအပေါ်အခြေခံပြီး ရုပ်ရှင်နှင့် ရှိုးများကို အကြံပြုပေးသည်။
- **Automation နှင့် Efficiency**: AI သည် ထပ်တလဲလဲလုပ်ရသောအလုပ်များကို အလိုအလျောက်လုပ်ဆောင်ပေးနိုင်ပြီး workflow များကို streamline လုပ်ပေးသည်။
ဥပမာ- Customer service apps များသည် AI-powered chatbots ကို အသုံးပြု၍ ပုံမှန်မေးခွန်းများကို ဖြေဆိုပေးသည်။
- **Enhanced User Experience**: AI သည် အသုံးပြုသူအတွေ့အကြုံကို ပိုမိုကောင်းမွန်စေပြီး voice recognition, natural language processing, နှင့် predictive text ကဲ့သို့သော features များကို ပံ့ပိုးပေးသည်။
ဥပမာ- Siri နှင့် Google Assistant ကဲ့သို့သော virtual assistants များသည် အသုံးပြုသူ၏ voice commands ကို နားလည်ပြီး device များနှင့် interaction ကို လွယ်ကူစေသည်။

### ဒါတွေကောင်းတယ်လို့ထင်ရပေမယ့် AI Agent Framework ကို ဘာကြောင့်လိုအပ်ရတာလဲ?

AI Agent frameworks သည် ရိုးရိုး AI frameworks ထက်ပိုမိုအရေးပါသည်။ ၎င်းတို့သည် အသုံးပြုသူများ၊ အခြားအေးဂျင့်များနှင့် ပတ်ဝန်းကျင်တို့နှင့် အပြန်အလှန်ဆက်သွယ်နိုင်သော အာဏာရှိသော အေးဂျင့်များကို ဖန်တီးရန် ရည်ရွယ်ထားသည်။ ဤအေးဂျင့်များသည် အလိုအလျောက်အပြုအမူများကို ပြသနိုင်ပြီး အခြေအနေများပြောင်းလဲသည့်အခါတွင် အလိုအလျောက်အပြောင်းအလဲလုပ်နိုင်သည်။ AI Agent Frameworks မှပေးသော အဓိကစွမ်းရည်များကို ကြည့်ကြပါစို့-

- **Agent Collaboration နှင့် Coordination**: အေးဂျင့်များအချင်းချင်း ပေါင်းစည်း၍ အလုပ်လုပ်နိုင်ရန်၊ ဆက်သွယ်နိုင်ရန်နှင့် အလုပ်များကို ပိုမိုထိရောက်စွာ ဖြေရှင်းနိုင်ရန်။
- **Task Automation နှင့် Management**: အလုပ်များကို အလိုအလျောက်လုပ်ဆောင်ရန်၊ အလုပ်များကို ခွဲဝေခြင်းနှင့် အလုပ်များကို dynamic task management ဖြင့် စီမံခန့်ခွဲရန်။
- **Contextual Understanding နှင့် Adaptation**: အေးဂျင့်များကို context ကို နားလည်စေရန်၊ ပတ်ဝန်းကျင်ပြောင်းလဲမှုများကို အလိုအလျောက်အပြောင်းအလဲလုပ်နိုင်ရန်။

အကျဉ်းချုပ်အားဖြင့် အေးဂျင့်များသည် automation ကို နောက်တစ်ဆင့်တိုးတက်စေပြီး ပတ်ဝန်းကျင်မှ သင်ယူနိုင်သော ပိုမိုအာဏာရှိသော စနစ်များကို ဖန်တီးနိုင်စေသည်။

## အေးဂျင့်၏စွမ်းရည်များကို prototype, iterate, နှင့် တိုးတက်စေရန် ဘယ်လိုလုပ်ရမလဲ?

AI Agent Frameworks များတွင် module components, collaborative tools, နှင့် real-time learning ကဲ့သို့သော အခြေခံအချက်များကို အသုံးပြု၍ prototype နှင့် iteration ကို လျင်မြန်စွာလုပ်ဆောင်နိုင်သည်။

- **Modular Components ကို အသုံးပြုပါ**: AI SDKs တွင် AI connectors, function calling, prompt templates, နှင့် memory management ကဲ့သို့သော pre-built components များပါဝင်သည်။
- **Collaborative Tools ကို အသုံးပြုပါ**: အေးဂျင့်များကို အထူးလုပ်ငန်းတာဝန်များနှင့် အခန်းကဏ္ဍများဖြင့် ဖန်တီးပါ။
- **Real-Time Learning ကို အသုံးပြုပါ**: Feedback loops များကို အေးဂျင့်များ၏ အပြန်အလှန်ဆက်သွယ်မှုများမှ သင်ယူနိုင်ရန်။

### Modular Components ကို အသုံးပြုခြင်း

Microsoft Semantic Kernel နှင့် LangChain ကဲ့သို့သော SDKs တွင် AI connectors, prompt templates, နှင့် memory management ကဲ့သို့သော pre-built components များပါဝင်သည်။

**အဖွဲ့များသည် ဤအရာများကို ဘယ်လိုအသုံးပြုနိုင်မလဲ**: အဖွဲ့များသည် ဤ components များကို အစမှစ၍ ဖန်တီးရန်မလိုဘဲ functional prototype ကို လျင်မြန်စွာဖန်တီးနိုင်သည်။

**အကောင်အထည်ဖော်နည်း**: User input မှ အချက်အလက်များကို extract လုပ်ရန် pre-built parser ကို အသုံးပြုပါ၊ memory module ကို data ကို သိမ်းဆည်းရန်နှင့် ပြန်လည်ရယူရန် အသုံးပြုပါ။

**ဥပမာ code**: Semantic Kernel Python နှင့် .Net ကို အသုံးပြု၍ pre-built AI Connector ကို အသုံးပြုနည်းကို ကြည့်ပါ:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

ဤဥပမာတွင် user input မှ key information ကို extract လုပ်ရန် pre-built parser ကို အသုံးပြုနည်းကို တွေ့ရသည်။ modular approach သည် high-level logic အပေါ် အာရုံစိုက်ရန် အခွင့်အလမ်းပေးသည်။

### Collaborative Tools ကို အသုံးပြုခြင်း

CrewAI, Microsoft AutoGen, နှင့် Semantic Kernel ကဲ့သို့သော frameworks များသည် အေးဂျင့်များအချင်းချင်း ပေါင်းစည်း၍ အလုပ်လုပ်နိုင်ရန် facilitate လုပ်ပေးသည်။

**အဖွဲ့များသည် ဤအရာများကို ဘယ်လိုအသုံးပြုနိုင်မလဲ**: အဖွဲ့များသည် အထူးလုပ်ငန်းတာဝန်များနှင့် အခန်းကဏ္ဍများဖြင့် အေးဂျင့်များကို ဖန်တီးနိုင်သည်။

**အကောင်အထည်ဖော်နည်း**: Data retrieval, analysis, decision-making ကဲ့သို့သော အထူးလုပ်ငန်းတာဝန်များနှင့် အခန်းကဏ္ဍများပါဝင်သော အေးဂျင့်များကို ဖန်တီးနိုင်သည်။

**ဥပမာ code (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

ဤ code တွင် အေးဂျင့်များသည် data ကို analysis လုပ်ရန် ပေါင်းစည်း၍ အလုပ်လုပ်နည်းကို တွေ့ရသည်။

### Real-Time Learning ကို အသုံးပြုခြင်း

အဆင့်မြင့် frameworks များသည် real-time context ကို နားလည်ခြင်းနှင့် adaptation ကို ပံ့ပိုးပေးသည်။

**အဖွဲ့များသည် ဤအရာများကို ဘယ်လိုအသုံးပြုနိုင်မလဲ**: Feedback loops များကို အေးဂျင့်များ၏ အပြန်အလှန်ဆက်သွယ်မှုများမှ သင်ယူနိုင်ရန် implement လုပ်ပါ။

**အကောင်အထည်ဖော်နည်း**: User feedback, environmental data, နှင့် task outcomes ကို အေးဂျင့်များသည် analysis လုပ်ပြီး performance ကို တိုးတက်စေသည်။

## AutoGen, Semantic Kernel နှင့် Azure AI Agent Service တို့၏ frameworks အကြားကွာခြားချက်များကဘာလဲ?

ဤ frameworks များကို design, capabilities, နှင့် target use cases အရ ကွာခြားချက်များကို ကြည့်နိုင်သည်-

## AutoGen

AutoGen သည် Microsoft Research's AI Frontiers Lab မှ ဖွံ့ဖြိုးတိုးတက်ထားသော open-source framework ဖြစ်သည်။ ၎င်းသည် event-driven, distributed *agentic* applications ကို အထူးအာရုံစိုက်ထားသည်။

AutoGen သည် agents concept အပေါ် အခြေခံထားသည်။ Agents သည် environment ကို သိမြင်နိုင်ပြီး decision-making လုပ်နိုင်သည်။

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agents သည် actor model အပေါ် အခြေခံထားသည်</a>။

**Use Cases**: Code generation, data analysis tasks, နှင့် planning နှင့် research functions များအတွက် custom agents ဖန်တီးခြင်း။

AutoGen ၏ core concepts အချို့မှာ-

- **Agents**: Software entity တစ်ခုဖြစ်ပြီး-
  - **Messages ဖြင့် ဆက်သွယ်ခြင်း**။
  - **State ကို maintain လုပ်ခြင်း**။
  - **Actions ကို ပြုလုပ်ခြင်း**။

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
ဤ code တွင် `MyAgent` သည် `RoutedAgent` ကို အခြေခံထားပြီး message handler ကို အသုံးပြုသည်။

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

AutoGen runtime သို့ agents များကို register လုပ်ပြီး message ကို ပေးပို့သည်။

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

Output တွင် message ကို response ပြန်ပေးနည်းကို တွေ့ရသည်။

- **Multi agents**: AutoGen သည် multi-agent systems ဖန်တီးရန် support ပေးသည်။

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

ဤ code တွင် `GroupChatManager` သည် agents များအကြား coordination လုပ်ပေးသည်။

- **Agent Runtime**: Runtime environment သည် agents များအကြား communication ကို enable လုပ်ပေးသည်။

## Semantic Kernel + Agent Framework

Semantic Kernel သည် enterprise-ready AI Orchestration SDK ဖြစ်သည်။

Core components အချို့မှာ-

- **AI Connectors**: External AI services နှင့် data sources များကို interface လုပ်ပေးသည်။

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

ဤ code တွင် Azure OpenAI Chat Completion ကို kernel တွင် add လုပ်နည်းကို တွေ့ရသည်။

- **Plugins**: Functions များကို encapsulate လုပ်ပေးသည်။

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

ဤ code တွင် prompt function ကို kernel တွင် import လုပ်နည်းကို တွေ့ရသည်။

- **Native function**: Framework သည် native functions ကို call လုပ်နိုင်သည်။

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **Memory**: Context management ကို abstract လုပ်ပေးသည်။

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

ဤ code တွင် memory တွင် facts များကို add လုပ်နည်းကို တွေ့ရသည်။
ဒီအချက်တွေကို `SummarizedAzureDocs` ဆိုတဲ့ memory collection ထဲမှာ သိမ်းဆည်းထားပါတယ်။ ဒီဟာက အလွန်ရိုးရှင်းတဲ့ ဥပမာတစ်ခုဖြစ်ပေမယ့် LLM အတွက် memory ထဲမှာ အချက်အလက်တွေကို သိမ်းဆည်းနိုင်ပုံကို မြင်နိုင်ပါတယ်။

ဒါဆိုရင် Semantic Kernel framework ရဲ့ အခြေခံတွေကို သိပြီးပြီ၊ Agent Framework အကြောင်းလည်း သိလိုက်ရအောင်။

## Azure AI Agent Service

Azure AI Agent Service ဟာ Microsoft Ignite 2024 မှာ မကြာသေးခင်က မိတ်ဆက်ထားတဲ့ နောက်ဆုံးထည့်သွင်းထားတဲ့ feature တစ်ခုဖြစ်ပါတယ်။ ဒါဟာ Llama 3, Mistral, Cohere လို open-source LLMs ကိုတိုက်ရိုက်ခေါ်ယူနိုင်တဲ့ ပိုမိုလွယ်ကူတဲ့ မော်ဒယ်တွေနဲ့ AI agents တွေကို ဖွံ့ဖြိုးပြီး deploy လုပ်နိုင်စေပါတယ်။

Azure AI Agent Service ဟာ လုပ်ငန်းအသုံးအဆောင်အတွက် သင့်လျော်တဲ့ enterprise security mechanism တွေ၊ data storage နည်းလမ်းတွေကို ပိုမိုခိုင်မာစေပါတယ်။

AutoGen နဲ့ Semantic Kernel လို multi-agent orchestration frameworks တွေနဲ့ အလွယ်တကူ အလုပ်လုပ်နိုင်ပါတယ်။

ဒီ service ဟာ Public Preview အဆင့်မှာရှိပြီး Python နဲ့ C# ကို အသုံးပြုပြီး agent တွေကို ဖန်တီးနိုင်ပါတယ်။

Semantic Kernel Python ကို အသုံးပြုပြီး user-defined plugin နဲ့ Azure AI Agent တစ်ခုကို ဖန်တီးနိုင်ပါတယ်။

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### အဓိကအကြောင်းအရာများ

Azure AI Agent Service ရဲ့ အဓိကအကြောင်းအရာတွေကတော့ အောက်ပါအတိုင်းဖြစ်ပါတယ်-

- **Agent**: Azure AI Agent Service ဟာ Azure AI Foundry နဲ့ ပေါင်းစည်းထားပါတယ်။ AI Foundry အတွင်းမှာ AI Agent ဟာ "smart" microservice အနေနဲ့ အသုံးပြုနိုင်ပြီး မေးခွန်းတွေကို ဖြေဆိုပေးခြင်း (RAG), လုပ်ဆောင်မှုတွေကို ပြုလုပ်ပေးခြင်း, သို့မဟုတ် workflow တွေကို အပြည့်အဝ automate လုပ်ပေးခြင်းတို့ကို ပြုလုပ်နိုင်ပါတယ်။ ဒါဟာ generative AI models တွေကို အသုံးပြုပြီး အပြင်လောက data sources တွေနဲ့ ချိတ်ဆက်နိုင်စေတဲ့ tools တွေကို ပေါင်းစပ်ထားတာကြောင့် ဖြစ်ပါတယ်။ Agent တစ်ခုရဲ့ ဥပမာကတော့-

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ဒီဥပမာမှာ `gpt-4o-mini` မော်ဒယ်နဲ့ `my-agent` ဆိုတဲ့ နာမည်နဲ့ agent တစ်ခုကို ဖန်တီးထားပြီး `You are helpful agent` ဆိုတဲ့ အညွှန်းတွေကို ထည့်သွင်းထားပါတယ်။ ဒီ agent ဟာ code interpretation tasks တွေကို လုပ်ဆောင်နိုင်စေတဲ့ tools နဲ့ resources တွေကို ပံ့ပိုးထားပါတယ်။

- **Thread နဲ့ messages**: Thread ဟာ အရေးကြီးတဲ့ အကြောင်းအရာတစ်ခုဖြစ်ပါတယ်။ ဒါဟာ agent နဲ့ user အကြား စကားဝိုင်း သို့မဟုတ် အပြန်အလှန်ဆက်သွယ်မှုကို ကိုယ်စားပြုပါတယ်။ Threads တွေကို စကားဝိုင်းရဲ့ တိုးတက်မှုကို စောင့်ကြည့်ခြင်း၊ context အချက်အလက်တွေကို သိမ်းဆည်းခြင်း၊ interaction ရဲ့ state ကို စီမံခန့်ခွဲခြင်းတို့အတွက် အသုံးပြုနိုင်ပါတယ်။ Thread ရဲ့ ဥပမာကတော့-

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

    အရင် code မှာ thread တစ်ခုကို ဖန်တီးထားပါတယ်။ ထို့နောက် thread ကို message တစ်ခု ပို့ထားပါတယ်။ `create_and_process_run` ကို ခေါ်ပြီး agent ကို thread ပေါ်မှာ အလုပ်လုပ်ဖို့ တောင်းဆိုထားပါတယ်။ messages တွေကို fetch လုပ်ပြီး agent ရဲ့ response ကို log လုပ်ထားပါတယ်။ ဒီ messages တွေက user နဲ့ agent အကြား စကားဝိုင်းရဲ့ တိုးတက်မှုကို ပြသထားပါတယ်။ messages တွေဟာ text, image, file စတဲ့ အမျိုးအစားအမျိုးမျိုးဖြစ်နိုင်ပြီး agent ရဲ့ အလုပ်ရလဒ်အနေနဲ့ ဥပမာအားဖြင့် image တစ်ခု သို့မဟုတ် text response တစ်ခု ဖြစ်နိုင်ပါတယ်။ Developer အနေနဲ့ ဒီအချက်အလက်တွေကို အသုံးပြုပြီး response ကို ထပ်မံ process လုပ်ခြင်း သို့မဟုတ် user ကို ပြသခြင်းတို့ကို ပြုလုပ်နိုင်ပါတယ်။

- **အခြား AI frameworks တွေနဲ့ ပေါင်းစည်းမှု**: Azure AI Agent Service ဟာ AutoGen နဲ့ Semantic Kernel လို frameworks တွေနဲ့ interaction ပြုလုပ်နိုင်ပါတယ်။ ဒါဟာ app ရဲ့ အချို့ကို frameworks တစ်ခုခုမှာ ဖန်တီးပြီး Agent service ကို orchestrator အနေနဲ့ အသုံးပြုခြင်း သို့မဟုတ် app အားလုံးကို Agent service မှာ ဖန်တီးခြင်းတို့ကို ပြုလုပ်နိုင်ပါတယ်။

**အသုံးပြုမှုများ**: Azure AI Agent Service ဟာ secure, scalable, flexible AI agent deployment လိုအပ်တဲ့ လုပ်ငန်းအသုံးအဆောင် application တွေအတွက် ဖန်တီးထားပါတယ်။

## ဒီ frameworks တွေကြားက ကွာခြားချက်တွေက ဘာလဲ?

ဒီ frameworks တွေကြားမှာ အများကြီး တူညီမှုတွေရှိသလို၊ design, capabilities, target use cases အရ ကွာခြားချက်တွေရှိပါတယ်-

- **AutoGen**: Multi-agent systems အပေါ် အဆင့်မြင့် သုတေသနလုပ်ငန်းတွေကို စမ်းသပ်ဖို့အတွက် အကောင်းဆုံးနေရာဖြစ်ပါတယ်။ Sophisticated multi-agent systems တွေကို prototype လုပ်ဖို့အတွက် အကောင်းဆုံးဖြစ်ပါတယ်။
- **Semantic Kernel**: Enterprise agentic applications တွေကို ဖန်တီးဖို့ production-ready agent library ဖြစ်ပါတယ်။ Event-driven, distributed agentic applications တွေကို အဓိကထားပြီး multiple LLMs, SLMs, tools, single/multi-agent design patterns တွေကို enable လုပ်ပါတယ်။
- **Azure AI Agent Service**: Azure Foundry မှာ agents တွေကို ဖန်တီးပြီး deploy လုပ်ဖို့ platform နဲ့ service ဖြစ်ပါတယ်။ Azure OpenAI, Azure AI Search, Bing Search, code execution စတဲ့ services တွေနဲ့ ချိတ်ဆက်မှုကို ပံ့ပိုးပေးပါတယ်။

Framework တစ်ခုကို ရွေးချယ်ဖို့ မသေချာသေးလား?

### အသုံးပြုမှုများ

အများဆုံးအသုံးပြုမှုအခြေအနေတွေကို ကြည့်ပြီး framework ရွေးချယ်ဖို့ ကူညီပေးပါမယ်-

> Q: စမ်းသပ်ခြင်း၊ သင်ယူခြင်း၊ proof-of-concept agent applications တွေကို ဖန်တီးခြင်းလုပ်နေပြီး အလျင်အမြန် ဖန်တီးပြီး စမ်းသပ်ချင်တယ်။
>

>A: AutoGen ဟာ ဒီအခြေအနေအတွက် အကောင်းဆုံးရွေးချယ်မှုဖြစ်ပါတယ်။ ဒါဟာ event-driven, distributed agentic applications တွေကို အဓိကထားပြီး advanced multi-agent design patterns တွေကို ပံ့ပိုးပေးပါတယ်။

> Q: ဒီ use case အတွက် AutoGen ဟာ Semantic Kernel နဲ့ Azure AI Agent Service ထက် ပိုကောင်းတာ ဘာလဲ?
>
> A: AutoGen ဟာ event-driven, distributed agentic applications တွေကို အထူးသင့်လျော်စေတဲ့ design လုပ်ထားပြီး code generation နဲ့ data analysis tasks တွေကို automate လုပ်ဖို့ အကောင်းဆုံးဖြစ်ပါတယ်။ Multi-agent systems တွေကို အလွယ်တကူ ဖန်တီးနိုင်စေတဲ့ tools နဲ့ capabilities တွေကို ပံ့ပိုးပေးပါတယ်။

>Q: Azure AI Agent Service ဟာလည်း ဒီမှာ အလုပ်လုပ်နိုင်မယ်ထင်တယ်၊ code generation tools တွေပါရှိတယ်လို့လား?
>
> A: ဟုတ်ပါတယ်၊ Azure AI Agent Service ဟာ platform service ဖြစ်ပြီး multiple models, Azure AI Search, Bing Search, Azure Functions တွေကို built-in capabilities အနေနဲ့ ပံ့ပိုးပေးပါတယ်။ Foundry Portal မှာ agents တွေကို အလွယ်တကူ ဖန်တီးပြီး အကျယ်အဝ deploy လုပ်နိုင်ပါတယ်။

> Q: မသေချာသေးဘူး၊ တစ်ခုတည်းပဲ ရွေးပေးပါ။
>
> A: Semantic Kernel မှာ application ကို အရင်ဖန်တီးပြီး Azure AI Agent Service ကို အသုံးပြုပြီး agent ကို deploy လုပ်ဖို့ အကောင်းဆုံးရွေးချယ်မှုဖြစ်ပါတယ်။ ဒီနည်းလမ်းက multi-agent systems တွေကို Semantic Kernel မှာ ဖန်တီးနိုင်စေပြီး agents တွေကို အလွယ်တကူ persist လုပ်နိုင်စေပါတယ်။ ထို့အပြင် Semantic Kernel မှာ AutoGen connector ပါရှိတာကြောင့် frameworks နှစ်ခုလုံးကို အလွယ်တကူ ပေါင်းစည်းအသုံးပြုနိုင်ပါတယ်။

အဓိက ကွာခြားချက်တွေကို အောက်ပါဇယားမှာ အကျဉ်းချုပ်ထားပါတယ်-

| Framework | အဓိကထားမှု | အဓိကအကြောင်းအရာများ | အသုံးပြုမှုများ |
| --- | --- | --- | --- |
| AutoGen | Event-driven, distributed agentic applications | Agents, Personas, Functions, Data | Code generation, data analysis tasks |
| Semantic Kernel | လူ့ဘာသာစကားနဲ့ ဆက်နွယ်မှုနဲ့ text content ဖန်တီးခြင်း | Agents, Modular Components, Collaboration | Natural language understanding, content generation |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

Framework တစ်ခုစီရဲ့ အကောင်းဆုံးအသုံးပြုမှုက ဘာလဲ?

## Azure ecosystem tools တွေကို တိုက်ရိုက်ပေါင်းစည်းနိုင်မလား၊ standalone solutions တွေလိုအပ်မလား?

အဖြေက ဟုတ်ပါတယ်၊ Azure AI Agent Service ဟာ Azure ecosystem tools တွေနဲ့ seamless အလုပ်လုပ်ဖို့ ဖန်တီးထားပါတယ်။ Bing, Azure AI Search, Azure Functions တွေကို ပေါင်းစည်းနိုင်ပါတယ်။ Azure AI Foundry နဲ့လည်း အနက်ရှိုင်းတဲ့ integration ရှိပါတယ်။

AutoGen နဲ့ Semantic Kernel အတွက်လည်း Azure services တွေနဲ့ ပေါင်းစည်းနိုင်ပေမယ့် code မှာ Azure services တွေကို ခေါ်ရပါမယ်။ ဒါ့အပြင် Azure SDKs ကို အသုံးပြုပြီး agents တွေကနေ Azure services တွေနဲ့ interaction ပြုလုပ်နိုင်ပါတယ်။ ထို့အပြင် Azure AI Agent Service ကို AutoGen သို့မဟုတ် Semantic Kernel မှာ ဖန်တီးထားတဲ့ agents တွေကို orchestrator အနေနဲ့ အသုံးပြုနိုင်ပြီး Azure ecosystem ကို အလွယ်တကူ access လုပ်နိုင်ပါတယ်။

### AI Agent Frameworks အကြောင်း မေးခွန်းတွေ ရှိသေးလား?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ကို join လုပ်ပြီး အခြားလေ့လာသူတွေနဲ့ တွေ့ဆုံပါ၊ office hours တွေတက်ပါ၊ AI Agents အကြောင်း မေးခွန်းတွေကို ဖြေရှင်းပါ။

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel and AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution</a>

## အရင်စာရင်း

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## နောက်စာရင်း

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။