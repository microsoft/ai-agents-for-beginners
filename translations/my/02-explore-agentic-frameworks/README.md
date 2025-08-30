<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a9631d0898fc3c6ecbb3a8a0da7aaba3",
  "translation_date": "2025-08-30T09:40:06+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "my"
}
-->
[![AI Agent Frameworks ကို ရှာဖွေခြင်း](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.my.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရန် အထက်ပါ ပုံကို နှိပ်ပါ)_

# AI Agent Frameworks ကို ရှာဖွေခြင်း

AI agent frameworks ဆိုတာ AI agent တွေကို ဖန်တီးခြင်း၊ တင်သွင်းခြင်း၊ စီမံခန့်ခွဲခြင်းကို လွယ်ကူစေဖို့ ရည်ရွယ်ထားတဲ့ ဆော့ဖ်ဝဲပလက်ဖောင်းတွေ ဖြစ်ပါတယ်။ ဒီ framework တွေက developer တွေကို အဆင့်မြင့် AI စနစ်တွေ ဖွံ့ဖြိုးတိုးတက်စေဖို့ အဆင့်မြင့် component တွေ၊ abstraction တွေ၊ tool တွေကို ပေးစွမ်းပါတယ်။

ဒီ framework တွေက AI agent ဖွံ့ဖြိုးတိုးတက်မှုမှာ ရှေ့ဆောင်ပြဿနာတွေကို စံပြနည်းလမ်းတွေဖြင့် ဖြေရှင်းပေးပြီး developer တွေကို သူတို့ application တွေ၏ ထူးခြားတဲ့ အပိုင်းအဆင့်များကို အာရုံစိုက်နိုင်စေပါတယ်။ AI စနစ်တွေကို တိုးတက်မှု၊ လွယ်ကူမှု၊ ထိရောက်မှု ပိုမိုမြှင့်တင်စေပါတယ်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ အောက်ပါအကြောင်းအရာတွေကို လေ့လာပါမယ်-

- AI Agent Frameworks ဆိုတာ ဘာလဲ၊ developer တွေကို ဘာတွေ လုပ်ဆောင်နိုင်စေသလဲ?
- အဖွဲ့တွေက ဒီ framework တွေကို အသုံးပြုပြီး agent ရဲ့ စွမ်းဆောင်ရည်တွေကို prototype လုပ်ခြင်း၊ iteration လုပ်ခြင်း၊ တိုးတက်စေခြင်းကို ဘယ်လို လွယ်ကူစေနိုင်သလဲ?
- Microsoft ဖန်တီးထားတဲ့ framework တွေ၊ tool တွေကြားမှာ ဘာတွေကွာခြားမှုရှိသလဲ?
- Azure ecosystem tool တွေကို တိုက်ရိုက် ပေါင်းစည်းနိုင်မလား၊ ဒါမှမဟုတ် standalone solution တွေလိုအပ်လား?
- Azure AI Agents service ဆိုတာ ဘာလဲ၊ ဒါက ကျွန်တော်တို့ကို ဘယ်လို အကျိုးရှိစေသလဲ?

## သင်ယူရမယ့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာရဲ့ ရည်မှန်းချက်တွေက-

- AI Agent Frameworks ရဲ့ AI ဖွံ့ဖြိုးတိုးတက်မှုမှာ အရေးပါမှုကို နားလည်စေခြင်း။
- AI Agent Frameworks ကို အသုံးပြုပြီး ဉာဏ်ရည်ရှိတဲ့ agent တွေ ဖန်တီးနိုင်စေခြင်း။
- AI Agent Frameworks က ပေးစွမ်းနိုင်တဲ့ အဓိကစွမ်းရည်တွေကို နားလည်စေခြင်း။
- AutoGen, Semantic Kernel, Azure AI Agent Service တို့ကြားက ကွာခြားချက်တွေကို နားလည်စေခြင်း။

## AI Agent Frameworks ဆိုတာ ဘာလဲ၊ developer တွေကို ဘာတွေ လုပ်ဆောင်နိုင်စေသလဲ?

ရိုးရာ AI Frameworks တွေက AI ကို app တွေထဲမှာ ပေါင်းစည်းပြီး အောက်ပါနည်းလမ်းတွေဖြင့် app တွေကို ပိုမိုကောင်းမွန်စေပါတယ်-

- **Personalization**: AI က user ရဲ့ အပြုအမူ၊ အကြိုက်အနှစ်သက်တွေကို ခွဲခြားပြီး အကြံပြုချက်တွေ၊ အကြောင်းအရာတွေ၊ အတွေ့အကြုံတွေကို တိုင်းတာပေးနိုင်ပါတယ်။
ဥပမာ- Netflix က user ရဲ့ ကြည့်ရှုမှုမှတ်တမ်းအပေါ် အခြေခံပြီး ရုပ်ရှင်၊ ရုပ်သံဇာတ်လမ်းတွေကို အကြံပြုပေးတာက user engagement နဲ့ satisfaction ကို မြှင့်တင်ပေးပါတယ်။
- **Automation and Efficiency**: AI က ထပ်တလဲလဲလုပ်ရတဲ့ အလုပ်တွေကို အလိုအလျောက်လုပ်ဆောင်ပေးပြီး workflow တွေကို streamline လုပ်ပေးကာ operational efficiency ကို တိုးတက်စေပါတယ်။
ဥပမာ- Customer service app တွေက AI-powered chatbot တွေကို အသုံးပြုပြီး အများဆုံးမေးခွန်းတွေကို ဖြေရှင်းပေးကာ human agent တွေကို ပိုမိုရှုပ်ထွေးတဲ့ ပြဿနာတွေကို အာရုံစိုက်နိုင်စေပါတယ်။
- **Enhanced User Experience**: AI က voice recognition, natural language processing, predictive text စတဲ့ intelligent feature တွေကို ပေးစွမ်းပြီး user experience ကို တိုးတက်စေပါတယ်။
ဥပမာ- Siri နဲ့ Google Assistant က AI ကို အသုံးပြုပြီး အသံအမိန့်တွေကို နားလည်ပြီး user တွေ device တွေကို ပိုမိုလွယ်ကူစွာ အသုံးပြုနိုင်စေပါတယ်။

### ဒါတွေက အရမ်းကောင်းတယ်လို့ ထင်ရတယ်၊ ဒါပေမယ့် AI Agent Framework ကို ဘာကြောင့် လိုအပ်သလဲ?

AI Agent Frameworks တွေက ရိုးရိုး AI Frameworks တွေထက် ပိုမိုတိုးတက်တဲ့ အရာတွေကို ကိုယ်စားပြုပါတယ်။ User တွေ၊ အခြား agent တွေ၊ ပတ်ဝန်းကျင်နဲ့ အပြန်အလှန်ဆက်သွယ်နိုင်တဲ့ ဉာဏ်ရည်ရှိတဲ့ agent တွေ ဖန်တီးနိုင်စေဖို့ ရည်ရွယ်ထားပါတယ်။ ဒီ agent တွေက autonomous behavior ကို ပြသနိုင်ပြီး ဆုံးဖြတ်ချက်ချနိုင်ကာ အခြေအနေပြောင်းလဲမှုတွေကို လိုက်လျောညီထွေဖြစ်စေပါတယ်။ AI Agent Frameworks က ပေးစွမ်းနိုင်တဲ့ အဓိကစွမ်းရည်တွေကို ကြည့်လိုက်ရအောင်-

- **Agent Collaboration and Coordination**: Agent အများအပြားကို ဖန်တီးပြီး အတူတကွ အလုပ်လုပ်နိုင်စေခြင်း၊ ဆက်သွယ်နိုင်စေခြင်း၊ ပြဿနာရှုပ်ထွေးမှုတွေကို ဖြေရှင်းနိုင်စေခြင်း။
- **Task Automation and Management**: Multi-step workflow တွေကို အလိုအလျောက်လုပ်ဆောင်နိုင်စေခြင်း၊ task delegation နဲ့ dynamic task management ကို agent တွေကြားမှာ စီမံခန့်ခွဲနိုင်စေခြင်း။
- **Contextual Understanding and Adaptation**: Agent တွေကို context ကို နားလည်နိုင်စေခြင်း၊ ပတ်ဝန်းကျင်ပြောင်းလဲမှုတွေကို လိုက်လျောညီထွေဖြစ်စေခြင်း၊ real-time အချက်အလက်အပေါ် အခြေခံပြီး ဆုံးဖြတ်ချက်ချနိုင်စေခြင်း။

အကျဉ်းချုပ်အားဖြင့် agent တွေက automation ကို နောက်တစ်ဆင့်တိုးတက်စေပြီး ပတ်ဝန်းကျင်နဲ့ သင်ယူနိုင်တဲ့ intelligent system တွေကို ဖန်တီးနိုင်စေပါတယ်။

## Agent ရဲ့ စွမ်းဆောင်ရည်တွေကို prototype လုပ်ခြင်း၊ iteration လုပ်ခြင်း၊ တိုးတက်စေခြင်းကို ဘယ်လို လွယ်ကူစေမလဲ?

AI Agent Frameworks အများစုမှာ module component တွေ၊ collaborative tool တွေ၊ real-time learning စတဲ့ အချက်တွေကို အသုံးပြုပြီး prototype လုပ်ခြင်း၊ iteration လုပ်ခြင်းကို လွယ်ကူစေပါတယ်။ အောက်မှာ အကြောင်းအရာတွေကို ဆက်လက်လေ့လာလိုက်ရအောင်-

- **Modular Component တွေကို အသုံးပြုပါ**: AI SDK တွေက AI နဲ့ Memory connector တွေ၊ natural language နဲ့ code plugin တွေကို အသုံးပြုတဲ့ function calling, prompt template တွေကို ပေးစွမ်းပါတယ်။
- **Collaborative Tool တွေကို အသုံးပြုပါ**: Agent တွေကို အခန်းကဏ္ဍနဲ့ task တွေကို သတ်မှတ်ပြီး collaborative workflow တွေကို စမ်းသပ်ပြီး တိုးတက်စေပါ။
- **Real-Time Learning**: Feedback loop တွေကို အကောင်အထည်ဖော်ပြီး agent တွေ interaction တွေကနေ သင်ယူပြီး သူတို့ရဲ့ အပြုအမူကို dynamic အနေဖြင့် ပြောင်းလဲနိုင်စေပါ။

### Modular Component တွေကို အသုံးပြုခြင်း

Microsoft Semantic Kernel နဲ့ LangChain က AI connector, prompt template, memory management စတဲ့ pre-built component တွေကို ပေးစွမ်းပါတယ်။

**အဖွဲ့တွေ ဘယ်လို အသုံးပြုနိုင်သလဲ**: အဖွဲ့တွေက ဒီ component တွေကို အလွယ်တကူ စုပေါင်းပြီး functional prototype တစ်ခုကို အစပြုနိုင်ပါတယ်။ ဒါက rapid experimentation နဲ့ iteration ကို လွယ်ကူစေပါတယ်။

**အကောင်အထည်ဖော်မှုမှာ ဘယ်လို အလုပ်လုပ်သလဲ**: User input ကနေ အချက်အလက်တွေကို extract လုပ်တဲ့ pre-built parser ကို အသုံးပြုနိုင်ပါတယ်။ Memory module က data တွေကို သိမ်းဆည်းပြီး ပြန်လည်ရယူနိုင်စေပါတယ်။ Prompt generator က user တွေနဲ့ အပြန်အလှန်ဆက်သွယ်နိုင်စေပါတယ်။

**ဥပမာ code**: Semantic Kernel Python နဲ့ .Net ကို အသုံးပြုပြီး auto-function calling ကို အသုံးပြုတဲ့ AI Connector ကို ဘယ်လို အသုံးပြုနိုင်သလဲဆိုတာကို ကြည့်လိုက်ရအောင်:

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

ဒီဥပမာမှာ သင်မြင်နိုင်တာက user input ကနေ origin, destination, date စတဲ့ flight booking request အချက်အလက်တွေကို extract လုပ်တဲ့ pre-built parser ကို ဘယ်လို အသုံးပြုနိုင်သလဲဆိုတာပါ။ Modular approach က high-level logic ကို အာရုံစိုက်နိုင်စေပါတယ်။

### Collaborative Tool တွေကို အသုံးပြုခြင်း

CrewAI, Microsoft AutoGen, Semantic Kernel စတဲ့ framework တွေက agent အများအပြားကို ဖန်တီးပြီး အတူတကွ အလုပ်လုပ်နိုင်စေပါတယ်။

**အဖွဲ့တွေ ဘယ်လို အသုံးပြုနိုင်သလဲ**: အဖွဲ့တွေက agent တွေကို အခန်းကဏ္ဍနဲ့ task တွေကို သတ်မှတ်ပြီး collaborative workflow တွေကို စမ်းသပ်ပြီး စနစ်ရဲ့ ထိရောက်မှုကို တိုးတက်စေပါတယ်။

**အကောင်အထည်ဖော်မှုမှာ ဘယ်လို အလုပ်လုပ်သလဲ**: Data retrieval, analysis, decision-making စတဲ့ အခန်းကဏ္ဍတွေကို သတ်မှတ်ထားတဲ့ agent တွေကို ဖန်တီးနိုင်ပါတယ်။ Agent တွေက user query ကို ဖြေရှင်းခြင်း၊ task တစ်ခုကို ပြီးမြောက်စေခြင်း စတဲ့ ရည်မှန်းချက်တစ်ခုကို အတူတကွ အလုပ်လုပ်နိုင်ပါတယ်။

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

ဒီ code မှာ သင်မြင်နိုင်တာက agent အများအပြားကို ဖန်တီးပြီး data ကို analysis လုပ်တဲ့ task တစ်ခုကို ဖန်တီးထားတာပါ။ Agent တစ်ခုချင်းစီက အခန်းကဏ္ဍတစ်ခုစီကို လုပ်ဆောင်ပြီး task ကို coordination လုပ်ကာ ရလဒ်ကို ရရှိစေပါတယ်။ Dedicated agent တွေကို ဖန်တီးခြင်းက task efficiency နဲ့ performance ကို တိုးတက်စေပါတယ်။

### Real-Time Learning

အဆင့်မြင့် framework တွေက real-time context ကို နားလည်ခြင်းနဲ့ adaptation စွမ်းရည်တွေကို ပေးစွမ်းပါတယ်။

**အဖွဲ့တွေ ဘယ်လို အသုံးပြုနိုင်သလဲ**: Feedback loop တွေကို အကောင်အထည်ဖော်ပြီး agent တွေ interaction တွေကနေ သင်ယူပြီး သူတို့ရဲ့ အပြုအမူကို dynamic အနေဖြင့် ပြောင်းလဲနိုင်စေပါတယ်။ ဒါက စွမ်းဆောင်ရည်တွေကို ဆက်လက်တိုးတက်စေပါတယ်။

**အကောင်အထည်ဖော်မှုမှာ ဘယ်လို အလုပ်လုပ်သလဲ**: Agent တွေက user feedback, environmental data, task outcomes တွေကို analysis လုပ်ပြီး knowledge base ကို update လုပ်ကာ decision-making algorithm တွေကို ပြောင်းလဲနိုင်ပါတယ်။ Iterative learning process က agent တွေကို အခြေအနေပြောင်းလဲမှုနဲ့ user preference တွေကို လိုက်လျောညီထွေဖြစ်စေပြီး စနစ်ရဲ့ ထိရောက်မှုကို တိုးတက်စေပါတယ်။

## AutoGen, Semantic Kernel, Azure AI Agent Service Framework တွေကြားက ကွာခြားချက်တွေ ဘာလဲ?

ဒီ framework တွေကို နှိုင်းယှဉ်ဖို့ နည်းလမ်းအများကြီးရှိပေမယ့် design, capability, target use case တွေကို အဓိကထားပြီး ကြည့်လိုက်ရအောင်:

## AutoGen

AutoGen က Microsoft Research ရဲ့ AI Frontiers Lab မှ ဖန်တီးထားတဲ့ open-source framework ဖြစ်ပါတယ်။ Event-driven, distributed *agentic* application တွေကို အဓိကထားပြီး LLMs, SLMs, tool တွေ၊ multi-agent design pattern တွေကို အသုံးပြုနိုင်စေပါတယ်။

AutoGen က agent တွေကို အခြေခံထားပြီး autonomous entity တွေကို ဖန်တီးနိုင်စေပါတယ်။ Agent တွေက environment ကို သိမြင်နိုင်ပြီး ဆုံးဖြတ်ချက်ချကာ ရည်မှန်းချက်တွေကို ပြည့်မှီစေပါတယ်။ Agent တွေက asynchronous message တွေကို အသုံးပြုကာ independent နဲ့ parallel အလုပ်လုပ်နိုင်စေပြီး system scalability နဲ့ responsiveness ကို တိုးတက်စေပါတယ်။
ဒါဆို Semantic Kernel framework ရဲ့ အခြေခံတွေကို နားလည်ပြီးပြီဆိုရင်၊ Agent Framework အကြောင်းကို ဆက်လေ့လာကြည့်ရအောင်။

## Azure AI Agent Service

Azure AI Agent Service ဟာ Microsoft Ignite 2024 မှာ မိတ်ဆက်ခဲ့တဲ့ နောက်ဆုံးပေါ် feature တစ်ခုဖြစ်ပြီး၊ AI agents တွေကို ပိုမိုလွယ်ကူစွာ ဖန်တီးပြီး တည်ဆောက်နိုင်စေပါတယ်။ ဥပမာအားဖြင့် Llama 3, Mistral, Cohere စတဲ့ open-source LLMs တွေကို တိုက်ရိုက်ခေါ်သုံးနိုင်ပါတယ်။

Azure AI Agent Service ဟာ လုံခြုံမှုအဆင့်မြင့်တဲ့ enterprise security mechanism တွေနဲ့ data storage နည်းလမ်းတွေကို ပံ့ပိုးပေးတာကြောင့်၊ စီးပွားရေးလုပ်ငန်းအတွက် အထူးသင့်တော်ပါတယ်။

ဒါ့အပြင် AutoGen နဲ့ Semantic Kernel စတဲ့ multi-agent orchestration frameworks တွေနဲ့ တိုက်ရိုက်အလုပ်လုပ်နိုင်ပါတယ်။

ယခုဝန်ဆောင်မှုဟာ Public Preview အဆင့်မှာရှိပြီး Python နဲ့ C# ကို အသုံးပြုပြီး agent တွေကို ဖန်တီးနိုင်ပါတယ်။

Semantic Kernel Python ကို အသုံးပြုပြီး၊ user-defined plugin နဲ့ Azure AI Agent တစ်ခုကို ဖန်တီးနိုင်ပါတယ်။

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

- **Agent**: Azure AI Agent Service ဟာ Azure AI Foundry နဲ့ ပေါင်းစည်းထားပါတယ်။ AI Foundry အတွင်းမှာ AI Agent ဟာ "smart" microservice တစ်ခုအနေနဲ့ အလုပ်လုပ်ပြီး၊ မေးခွန်းတွေကို ဖြေရှင်းပေးတာ (RAG), လုပ်ဆောင်မှုတွေကို ပြုလုပ်ပေးတာ၊ သို့မဟုတ် workflow တစ်ခုလုံးကို အလိုအလျောက်လုပ်ဆောင်ပေးတာတွေကို လုပ်ဆောင်နိုင်ပါတယ်။ Generative AI models တွေရဲ့ အားကို အသုံးချပြီး၊ tools တွေနဲ့ ပေါင်းစည်းကာ အချက်အလက်ရင်းမြစ်တွေကို ချိတ်ဆက်နိုင်ပါတယ်။ အောက်မှာ agent တစ်ခုရဲ့ ဥပမာကို ကြည့်ပါ-

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ဤဥပမာမှာ `gpt-4o-mini` ဆိုတဲ့ model နဲ့ `my-agent` ဆိုတဲ့ နာမည်နဲ့ agent တစ်ခုကို ဖန်တီးထားပြီး၊ `You are helpful agent` ဆိုတဲ့ ညွှန်ကြားချက်နဲ့ အတူ ဖန်တီးထားပါတယ်။ ဒီ agent ဟာ code interpretation လုပ်ငန်းတွေကို လုပ်ဆောင်နိုင်ဖို့ tools နဲ့ resources တွေကို ထည့်သွင်းပေးထားပါတယ်။

- **Thread နဲ့ messages**: Thread ဟာ agent နဲ့ user အကြား ဆွေးနွေးမှုတစ်ခုကို ကိုယ်စားပြုပါတယ်။ Thread တွေကို conversation ရဲ့ အခြေအနေကို သိမ်းဆည်းထားဖို့၊ context အချက်အလက်တွေကို သိမ်းဆည်းဖို့၊ interaction ရဲ့ အခြေအနေကို စီမံခန့်ခွဲဖို့ အသုံးပြုနိုင်ပါတယ်။ Thread ရဲ့ ဥပမာကို အောက်မှာကြည့်ပါ-

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

    အထက်ပါ code မှာ thread တစ်ခုကို ဖန်တီးထားပြီး၊ ထို့နောက် thread ကို message တစ်ခု ပို့ထားပါတယ်။ `create_and_process_run` ကို ခေါ်သုံးပြီး၊ agent ကို thread ပေါ်မှာ အလုပ်လုပ်ဖို့ မေးမြန်းထားပါတယ်။ messages တွေကို ပြန်လည်ရယူပြီး၊ agent ရဲ့ တုံ့ပြန်မှုကို မှတ်တမ်းတင်ထားပါတယ်။ Messages တွေက user နဲ့ agent အကြား ဆွေးနွေးမှုရဲ့ တိုးတက်မှုကို ပြသပါတယ်။ Messages တွေဟာ text, image, file စတဲ့ အမျိုးအစားအမျိုးမျိုးဖြစ်နိုင်ပြီး၊ agent ရဲ့ အလုပ်ရလဒ်အနေနဲ့ ဥပမာအားဖြင့် ပုံတစ်ပုံ သို့မဟုတ် စာသားတစ်ခုအဖြစ် ရရှိနိုင်ပါတယ်။ Developer အနေနဲ့ ဒီအချက်အလက်တွေကို အသုံးပြုပြီး၊ user ကို ပြသနိုင်ပါတယ်။

- **အခြား AI frameworks တွေနဲ့ ပေါင်းစည်းမှု**: Azure AI Agent Service ဟာ AutoGen နဲ့ Semantic Kernel စတဲ့ frameworks တွေနဲ့ ပေါင်းစည်းနိုင်ပါတယ်။ ဒါကြောင့် app ရဲ့ အချို့ကို ဒီ frameworks တွေထဲမှာ တည်ဆောက်ပြီး၊ Agent service ကို orchestrator အနေနဲ့ သုံးနိုင်ပါတယ်။ သို့မဟုတ် အားလုံးကို Agent service ထဲမှာ တည်ဆောက်နိုင်ပါတယ်။

**အသုံးပြုမှုများ**: Azure AI Agent Service ဟာ လုံခြုံမှု၊ အရွယ်အစားချဲ့ထွင်နိုင်မှု၊ နဲ့ အလွယ်တကူပြုပြင်နိုင်မှုလိုအပ်တဲ့ စီးပွားရေးလုပ်ငန်းအတွက် အထူးသင့်တော်ပါတယ်။

## ဒီ frameworks တွေကြားက ကွာခြားချက်က ဘာလဲ?

ဒီ frameworks တွေဟာ အချို့ overlap ရှိသလို၊ ဒီဇိုင်း၊ စွမ်းဆောင်ရည်နဲ့ ရည်ရွယ်ချက်အရ ကွာခြားချက်တွေ ရှိပါတယ်-

- **AutoGen**: Multi-agent systems တွေကို စမ်းသပ်ဖို့နဲ့ prototype ဖန်တီးဖို့ အကောင်းဆုံးနေရာဖြစ်ပါတယ်။
- **Semantic Kernel**: Enterprise agentic applications တွေကို တည်ဆောက်ဖို့ production-ready library ဖြစ်ပါတယ်။
- **Azure AI Agent Service**: Azure Foundry ထဲမှာ agents တွေကို တည်ဆောက်ပြီး deploy လုပ်ဖို့ platform နဲ့ service ဖြစ်ပါတယ်။

သင့်အတွက် ဘယ်ဟာကို ရွေးချယ်ရမလဲ?

### အသုံးပြုမှုများ

အောက်မှာ သင့်အတွက် အကူအညီပေးနိုင်မယ့် အသုံးပြုမှုအချို့ကို ဖော်ပြထားပါတယ်-

> Q: ကျွန်တော်/ကျွန်မဟာ agent applications တွေကို စမ်းသပ်နေပြီး၊ proof-of-concept တွေကို လျင်မြန်စွာ တည်ဆောက်ချင်တယ်။
>
> A: AutoGen ဟာ ဒီအခြေအနေအတွက် သင့်တော်ပါတယ်။

> Q: AutoGen ဟာ Semantic Kernel နဲ့ Azure AI Agent Service ထက် ဒီအခြေအနေမှာ ပိုကောင်းတာ ဘာလဲ?
>
> A: AutoGen ဟာ event-driven, distributed agentic applications တွေအတွက် အထူးဒီဇိုင်းလုပ်ထားတာကြောင့်၊ code generation နဲ့ data analysis လုပ်ငန်းတွေကို အထူးကောင်းမွန်စွာ လုပ်ဆောင်နိုင်ပါတယ်။

> Q: Azure AI Agent Service ဟာလည်း ဒီအတွက် အသုံးဝင်မယ်ထင်တယ်နော်?
>
> A: ဟုတ်ပါတယ်၊ Azure AI Agent Service ဟာ Azure Foundry Portal မှာ agents တွေကို လွယ်ကူစွာ တည်ဆောက်ပြီး deploy လုပ်နိုင်စေပါတယ်။

> Q: ကျွန်တော်/ကျွန်မ အခုထိ မသေချာသေးဘူး၊ တစ်ခုတည်းကို ရွေးပေးပါ။
>
> A: Semantic Kernel ကို သုံးပြီး application ကို တည်ဆောက်ပြီး၊ Azure AI Agent Service ကို အသုံးပြုကာ agent ကို deploy လုပ်ပါ။

### အဓိကကွာခြားချက်များကို ဇယားဖြင့် ဖော်ပြခြင်း

| Framework | အဓိကရည်ရွယ်ချက် | အဓိကအကြောင်းအရာများ | အသုံးပြုမှုများ |
| --- | --- | --- | --- |
| AutoGen | Event-driven, distributed agentic applications | Agents, Personas, Functions, Data | Code generation, data analysis tasks |
| Semantic Kernel | Human-like text content ကို နားလည်ပြီး ဖန်တီးခြင်း | Agents, Modular Components, Collaboration | Natural language understanding, content generation |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## Azure ecosystem tools တွေကို တိုက်ရိုက်ပေါင်းစည်းနိုင်မလား၊ standalone solutions တွေလိုအပ်မလား?

Azure AI Agent Service ဟာ Azure ecosystem tools တွေနဲ့ တိုက်ရိုက်ပေါင်းစည်းနိုင်ပါတယ်။ Bing, Azure AI Search, Azure Functions စတဲ့ tools တွေကို ပေါင်းစည်းနိုင်သလို၊ Azure AI Foundry နဲ့လည်း နက်ရှိုင်းစွာ ပေါင်းစည်းထားပါတယ်။

AutoGen နဲ့ Semantic Kernel အတွက်လည်း Azure services တွေနဲ့ ပေါင်းစည်းနိုင်ပေမယ့်၊ သင့် code ထဲကနေ service တွေကို ခေါ်သုံးရပါမယ်။

### AI Agent Frameworks အကြောင်း ပိုမိုသိလိုပါသလား?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ကို join လုပ်ပြီး၊ အခြားလေ့လာသူတွေနဲ့ တွေ့ဆုံပါ၊ office hours တွေကို တက်ရောက်ပါ၊ သင့်မေးခွန်းတွေကို ဖြေရှင်းပါ။

## ကိုးကားချက်များ

- 

## ယခင်သင်ခန်းစာ

[AI Agents နဲ့ Agent အသုံးပြုမှုများ အကြောင်း အကျဉ်းချုပ်](../01-intro-to-ai-agents/README.md)

## နောက်သင်ခန်းစာ

[Agentic Design Patterns ကို နားလည်ခြင်း](../03-agentic-design-patterns/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲလွဲအချော်ချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။