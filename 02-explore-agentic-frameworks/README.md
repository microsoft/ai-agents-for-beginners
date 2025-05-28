# AI Agent Framework များကို စူးစမ်းလေ့လာခြင်း

[![AI Agent Framework များကို စူးစမ်းလေ့လာခြင်း](./images/lesson-2-thumbnail.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရှုရန် အထက်ပါပုံကို နှိပ်ပါ)_

# AI Agent Framework များကို စူးစမ်းလေ့လာခြင်း

AI Agent Framework များသည် AI အေးဂျင့်များ၏ ဖန်တီးမှု၊ အသုံးချမှု နှင့် စီမံခန့်ခွဲမှုတို့ကို ရိုးရှင်းစေရန် ရည်ရွယ်၍ တီထွင်ထားသော ဆော့ဖ်ဝဲလ် ပလပ်ဖောင်းများဖြစ်သည်။ ဤ Framework များသည် developer များအတွက် ရှုပ်ထွေးသော AI စနစ်များ ဖွံ့ဖြိုးတိုးတက်စေရာတွင် လမ်းကြောင်းပြပေးနိုင်သည့် ကြိုတင်တည်ဆောက်ထားသော အစိတ်အပိုင်းများ၊ abstract များနှင့် ကိရိယာများကို ပံ့ပိုးပေးပါသည်။

ဤ Framework များသည် AI Agent ဖွံ့ဖြိုးမှုတွင် တွေ့ကြုံရသော ယေဘုယျ စိန်ခေါ်မှုများအတွက် သတ်မှတ်ထားသော ချဉ်းကပ်နည်းများကို ပံ့ပိုးပေးခြင်းဖြင့် developer များအား ၎င်းတို့၏ အပလီကေးရှင်းများ၏ ထူးခြားသော အင်္ဂါရပ်များအပေါ် အာရုံစိုက်နိုင်စေပါသည်။ ၎င်းတို့သည် AI စနစ်များ တည်ဆောက်ရာတွင် တိုးချဲ့နိုင်မှု၊ အသုံးဝင်နိုင်မှုနှင့် ထိရောက်မှုတို့ကို မြှင့်တင်ပေးပါသည်။

## မိတ်ဆက်

ဤသင်ခန်းစာတွင် အောက်ပါအချက်များကို ခြုံငုံ၍ လေ့လာမည်ဖြစ်သည်-

- AI Agent Framework များဆိုသည်မှာ အဘယ်နည်း နှင့် ၎င်းတို့သည် developer များအား မည်သည့်အရာများ အောင်မြင်စေနိုင်သနည်း?
- အဖွဲ့များသည် ၎င်းတို့၏ agent များ၏ စွမ်းရည်များကို လျင်မြန်စွာ prototype တည်ဆောက်ခြင်း၊ ပြန်လည်ပြင်ဆင်ခြင်း နှင့် မြှင့်တင်ခြင်းအတွက် မည်သို့အသုံးပြုနိုင်မည်နည်း?
- Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>၊ <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> နှင့် <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> တို့မှ ဖန်တီးထားသော framework များနှင့် ကိရိယာများအကြား ကွာခြားချက်များမှာ မည်သည့်အရာများနည်း?
- ကျွန်ုပ်၏ လက်ရှိ Azure ecosystem ကိရိယာများကို တိုက်ရိုက် ပေါင်းစပ်နိုင်သလား၊ သို့မဟုတ် သီးခြား ဖြေရှင်းနည်းများ လိုအပ်သလား?
- Azure AI Agents service ဆိုသည်မှာ အဘယ်နည်း နှင့် ၎င်းသည် ကျွန်ုပ်အား မည်သို့ အကူအညီပေးနေသနည်း?

## သင်ခန်းစာ ရည်မှန်းချက်များ

ဤသင်ခန်းစာ၏ ရည်မှန်းချက်များမှာ သင်အား အောက်ပါအရာများကို နားလည်စေရန်ဖြစ်သည်-

- AI ဖွံ့ဖြိုးမှုတွင် AI Agent Framework များ၏ အခန်းကဏ္ဍ
- ထိုးထွင်းသော agent များ တည်ဆောက်ရန် AI Agent Framework များကို မည်သို့ အသုံးချရမည်နည်း
- AI Agent Framework များမှ လုပ်ဆောင်နိုင်စေသော အဓိက စွမ်းဆောင်ရည်များ
- AutoGen၊ Semantic Kernel နှင့် Azure AI Agent Service တို့အကြား ကွာခြားချက်များ

## AI Agent Framework များသည် အဘယ်နည်း နှင့် developer များအား မည်သည့်အရာများ လုပ်ဆောင်နိုင်စေသနည်း?

ရိုးရာ AI Framework များသည် သင်၏ အပလီကေးရှင်းများတွင် AI ကို ပေါင်းစပ်ရာတွင် အကူအညီပေးနိုင်ပြီး ဤအပလီကေးရှင်းများကို အောက်ပါနည်းလမ်းများဖြင့် ပိုမိုကောင်းမွန်စေနိုင်သည်-

- **စိတ်ကြိုက်ပြင်ဆင်မှု (Personalization)**: AI သည် အသုံးပြုသူ၏ အပြုအမူများနှင့် နှစ်သက်မှုများကို ခွဲခြမ်းစိတ်ဖြာ၍ စိတ်ကြိုက်အကြံပြုချက်များ၊ အကြောင်းအရာများနှင့် အတွေ့အကြုံများကို ပံ့ပိုးပေးနိုင်သည်။
ဥပမာ- Netflix ကဲ့သို့သော streaming service များသည် ကြည့်ရှုမှု သမိုင်းအပေါ် အခြေခံ၍ ရုပ်ရှင်များနှင့် ရှိုးများကို အကြံပြုရန် AI ကို အသုံးပြုကြပြီး အသုံးပြုသူ၏ စိတ်ဝင်စားမှုနှင့် ကျေနပ်မှုကို မြှင့်တင်ပေးသည်။

- **အလိုအလျောက်လုပ်ဆောင်မှုနှင့် ထိရောက်မှု**: AI သည် ထပ်ခါတလဲလဲ လုပ်ရသော အလုပ်များကို အလိုအလျောက်လုပ်ဆောင်ခြင်း၊ လုပ်ငန်းစဉ်များကို ချောမွေ့စေခြင်းနှင့် လုပ်ငန်းဆောင်ရွက်မှု ထိရောက်မှုကို မြှင့်တင်ခြင်းများ လုပ်ဆောင်နိုင်သည်။
ဥပမာ- ဖောက်သည်ဝန်ဆောင်မှု အပလီကေးရှင်းများသည် သာမန် မေးမြန်းမှုများကို ကိုင်တွယ်ရန် AI-စွမ်းအား chatbot များကို အသုံးပြုကြပြီး တုံ့ပြန်ချိန်ကို လျှော့ချကာ ပိုမိုရှုပ်ထွေးသော ပြဿနာများအတွက် လူ့အေးဂျင့်များကို လွတ်မြောက်စေသည်။

- **မြှင့်တင်ထားသော အသုံးပြုသူ အတွေ့အကြုံ**: AI သည် အသံမှတ်သားခြင်း၊ သဘာဝဘာသာစကား လုပ်ဆောင်ခြင်းနှင့် ကြိုတင်ခန့်မှန်းထားသော စာသားများကဲ့သို့သော ထိုးထွင်းသော အင်္ဂါရပ်များကို ပံ့ပိုးပေးခြင်းဖြင့် အသုံးပြုသူ၏ အတွေ့အကြုံကို ပိုမိုကောင်းမွန်စေနိုင်သည်။
ဥပမာ- Siri နှင့် Google Assistant ကဲ့သို့သော virtual assistant များသည် အသံအမိန့်များကို နားလည်ပြီး တုံ့ပြန်ရန် AI ကို အသုံးပြုကြသည်၊ ၎င်းသည် အသုံးပြုသူများအတွက် ၎င်းတို့၏ စက်ပစ္စည်းများနှင့် ပိုမိုလွယ်ကူစွာ အပြန်အလှန်ဆက်သွယ်နိုင်စေသည်။

### ဤအရာများ အားလုံးသည် အလွန်ကောင်းမွန်ကြောင်း ထင်ရသည်၊ ထို့ကြောင့် AI Agent Framework လိုအပ်ရခြင်းမှာ အဘယ်ကြောင့်နည်း?

AI Agent Framework များသည် AI Framework များထက် ပိုမိုအရေးကြီးသော အရာတစ်ခုကို ကိုယ်စားပြုသည်။ ၎င်းတို့သည် သီးခြားရည်မှန်းချက်များ အောင်မြင်ရရှိရန် အသုံးပြုသူများ၊ အခြား agent များနှင့် ပတ်ဝန်းကျင်တို့နှင့် အပြန်အလှန်ဆက်သွယ်နိုင်သော ထိုးထွင်းသော agent များ ဖန်တီးခြင်းကို ဖြစ်နိုင်စေရန် ရည်ရွယ်တီထွင်ထားသည်။ ဤ agent များသည် အလိုအလျောက် အပြုအမူများကို ပြသနိုင်ကြပြီး ဆုံးဖြတ်ချက်များ ချမှတ်နိုင်သလို ပြောင်းလဲနေသော အခြေအနေများနှင့်လည်း လိုက်လျောညီထွေ ဖြစ်နိုင်ကြသည်။ AI Agent Framework များမှ လုပ်ဆောင်နိုင်စေသော အဓိက စွမ်းဆောင်ရည်အချို့ကို လေ့လာကြည့်ကြပါစို့-

- **Agent များ၏ ပူးပေါင်းဆောင်ရွက်မှုနှင့် ညှိနှိုင်းမှု**: ရှုပ်ထွေးသော အလုပ်များကို ဖြေရှင်းရန် ပူးပေါင်းလုပ်ဆောင်နိုင်သော၊ ဆက်သွယ်နိုင်သော နှင့် ညှိနှိုင်းနိုင်သော မျိုးစုံသော AI agent များ ဖန်တီးခြင်းကို ဖြစ်နိုင်စေသည်။

- **အလုပ်လုပ်ငန်း အလိုအလျောက်လုပ်ဆောင်မှုနှင့် စီမံခန့်ခွဲမှု**: agent များအကြား အဆင့်ပေါင်းများစွာရှိသော လုပ်ငန်းစဉ်များကို အလိုအလျောက်လုပ်ဆောင်ခြင်း၊ အလုပ်ခွဲဝေပေးခြင်းနှင့် dynamic အလုပ်စီမံခန့်ခွဲမှုအတွက် ယန္တရားများကို ပံ့ပိုးပေးသည်။

- **အကြောင်းအရာ နားလည်မှုနှင့် လိုက်လျောညီထွေဖြစ်မှု**: agent များအား အကြောင်းအရာကို နားလည်နိုင်စေခြင်း၊ ပြောင်းလဲနေသော ပတ်ဝန်းကျင်များနှင့် လိုက်လျောညီထွေဖြစ်နိုင်စေခြင်းနှင့် အချိန်နှင့်တပြေးညီ အချက်အလက်များအပေါ် အခြေခံ၍ ဆုံးဖြတ်ချက်များ ချမှတ်နိုင်စေခြင်းများဖြင့် တပ်ဆင်ပေးသည်။

ခြုံချုပ်ရလျှင်၊ agent များသည် သင်အား ပိုမိုများပြားသော အရာများ လုပ်ဆောင်နိုင်စေပြီး အလိုအလျောက်လုပ်ဆောင်မှုကို နောက်တစ်အဆင့်သို့ တက်လှမ်းစေကာ ၎င်းတို့၏ ပတ်ဝန်းကျင်မှ လိုက်လျောညီထွေဖြစ်နိုင်ပြီး သင်ယူနိုင်သော ပိုမိုထိုးထွင်းသော စနစ်များ ဖန်တီးနိုင်စေသည်။

## Agent ၏ စွမ်းရည်များကို လျင်မြန်စွာ prototype တည်ဆောက်ခြင်း၊ ပြန်လည်ပြင်ဆင်ခြင်းနှင့် မြှင့်တင်ခြင်းများကို မည်သို့ လုပ်ဆောင်နိုင်မည်နည်း?

ယင်းသည် လျင်မြန်စွာ ရွေ့လျားနေသော ကွင်းပြင်တစ်ခုဖြစ်သော်လည်း AI Agent Framework အများစုတွင် ဘုံရှိသော အရာများ အချို့ရှိပြီး ၎င်းတို့သည် modular components၊ collaborative tools နှင့် real-time learning တို့ဖြစ်သည်။ ဤအချက်များကို နက်ရှိုင်းစွာ လေ့လာကြည့်ကြပါစို့-

- **Modular Components များကို အသုံးပြုခြင်း**: AI SDK များသည် AI နှင့် Memory connector များ၊ သဘာဝဘာသာစကား သို့မဟုတ် code plugin များကို အသုံးပြု၍ function calling၊ prompt template များနှင့် အခြားအရာများကဲ့သို့သော ကြိုတင်တည်ဆောက်ထားသော အစိတ်အပိုင်းများကို ပေးအပ်သည်။

- **Collaborative Tools များကို အသုံးချခြင်း**: သီးခြား အခန်းကဏ္ဍများနှင့် အလုပ်များဖြင့် agent များကို ဒီဇိုင်းပြုလုပ်ခြင်းသည် ပူးပေါင်းဆောင်ရွက်သော လုပ်ငန်းစဉ်များကို စမ်းသပ်ပြီး သန့်စင်နိုင်စေသည်။

- **အချိန်နှင့်တပြေးညီ သင်ယူခြင်း**: agent များသည် အပြန်အလှန်ဆက်သွယ်မှုများမှ သင်ယူပြီး ၎င်းတို့၏ အပြုအမူကို dynamic ပြောင်းလဲနိုင်သော feedback loop များကို အကောင်အထည်ဖော်ခြင်း။

### Modular Components များကို အသုံးပြုခြင်း

Microsoft Semantic Kernel နှင့် LangChain ကဲ့သို့သော SDK များသည် AI connector များ၊ prompt template များနှင့် memory management များကဲ့သို့သော ကြိုတင်တည်ဆောက်ထားသော အစိတ်အပိုင်းများကို ပေးအပ်သည်။

**အဖွဲ့များ မည်သို့ အသုံးပြုနိုင်သနည်း**: အဖွဲ့များသည် ဤအစိတ်အပိုင်းများကို လျင်မြန်စွာ ပေါင်းစပ်၍ အစမှ စတင်ခြင်းမပြုဘဲ လုပ်ဆောင်နိုင်သော prototype တစ်ခု ဖန်တီးနိုင်ကြပြီး လျင်မြန်သော စမ်းသပ်မှုနှင့် ပြန်လည်ပြင်ဆင်မှုကို ခွင့်ပြုပေးသည်။

**လက်တွေ့တွင် မည်သို့ လုပ်ဆောင်သနည်း**: သင်သည် အသုံးပြုသူ၏ input မှ အချက်အလက်ကို ထုတ်ယူရန် ကြိုတင်တည်ဆောက်ထားသော parser တစ်ခု၊ ဒေတာသိမ်းဆည်းခြင်းနှင့် ပြန်လည်ရယူခြင်းအတွက် memory module တစ်ခုနှင့် အသုံးပြုသူများနှင့် အပြန်အလှန်ဆက်သွယ်ရန် prompt generator တစ်ခုတို့ကို အသုံးပြုနိုင်သည်၊ ဤအစိတ်အပိုင်းများကို အစမှ တည်ဆောက်ရန် မလိုအပ်ဘဲပင်ဖြစ်သည်။

**ဥပမာ ကုဒ်များ**။ Model သည် အသုံးပြုသူ၏ input ကို တုံ့ပြန်ရန် auto-function calling ကို အသုံးပြုသော Semantic Kernel Python နှင့် .Net နှင့်အတူ ကြိုတင်တည်ဆောက်ထားသော AI Connector ကို မည်သို့ အသုံးပြုနိုင်သည်ကို ဥပမာများကို လေ့လာကြည့်ကြပါစို့-

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

What you can see from this example is how you can leverage a pre-built parser to extract key information from user input, such as the origin, destination, and date of a flight booking request. This modular approach allows you to focus on the high-level logic.

### Leverage Collaborative Tools

Frameworks like CrewAI, Microsoft AutoGen, and Semantic Kernel facilitate the creation of multiple agents that can work together.

**How teams can use these**: Teams can design agents with specific roles and tasks, enabling them to test and refine collaborative workflows and improve overall system efficiency.

**How it works in practice**: You can create a team of agents where each agent has a specialized function, such as data retrieval, analysis, or decision-making. These agents can communicate and share information to achieve a common goal, such as answering a user query or completing a task.

**Example code (AutoGen)**:

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

What you see in the previous code is how you can create a task that involves multiple agents working together to analyze data. Each agent performs a specific function, and the task is executed by coordinating the agents to achieve the desired outcome. By creating dedicated agents with specialized roles, you can improve task efficiency and performance.

### Learn in Real-Time

Advanced frameworks provide capabilities for real-time context understanding and adaptation.

**How teams can use these**: Teams can implement feedback loops where agents learn from interactions and adjust their behavior dynamically, leading to continuous improvement and refinement of capabilities.

**How it works in practice**: Agents can analyze user feedback, environmental data, and task outcomes to update their knowledge base, adjust decision-making algorithms, and improve performance over time. This iterative learning process enables agents to adapt to changing conditions and user preferences, enhancing overall system effectiveness.

## What are the differences between the frameworks AutoGen, Semantic Kernel and Azure AI Agent Service?

There are many ways to compare these frameworks, but let's look at some key differences in terms of their design, capabilities, and target use cases:

## AutoGen

AutoGen is an open-source framework developed by Microsoft Research's AI Frontiers Lab. It focuses on event-driven, distributed *agentic* applications, enabling multiple LLMs and SLMs, tools, and advanced multi-agent design patterns.

AutoGen is built around the core concept of agents, which are autonomous entities that can perceive their environment, make decisions, and take actions to achieve specific goals. Agents communicate through asynchronous messages, allowing them to work independently and in parallel, enhancing system scalability and responsiveness.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agents are based on the actor model</a>. According to Wikipedia, an actor is _the basic building block of concurrent computation. In response to a message it receives, an actor can: make local decisions, create more actors, send more messages, and determine how to respond to the next message received_.

**Use Cases**: Automating code generation, data analysis tasks, and building custom agents for planning and research functions.

Here are some important core concepts of AutoGen:

- **Agents**. An agent is a software entity that:
  - **Communicates via messages**, these messages can be synchronous or asynchronous.
  - **Maintains its own state**, which can be modified by incoming messages.
  - **Performs actions** in response to received messages or changes in its state. These actions may modify the agent’s state and produce external effects, such as updating message logs, sending new messages, executing code, or making API calls.
    
  Here you have a short code snippet in which you create your own agent with Chat capabilities:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
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
    
    In the previous code, `MyAssistant` has been created and inherits from `RoutedAgent`. It has a message handler that prints the content of the message and then sends a response using the `AssistantAgent` delegate. Especially note how we assign to `self._delegate` an instance of `AssistantAgent` which is a pre-built agent that can handle chat completions.


    Let's let AutoGen know about this agent type and kick off the program next:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    In the previous code the agents are registered with the runtime and then a message is sent to the agent resulting in the following output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agents**. AutoGen supports the creation of multiple agents that can work together to achieve complex tasks. Agents can communicate, share information, and coordinate their actions to solve problems more efficiently. To create a multi-agent system, you can define different types of agents with specialized functions and roles, such as data retrieval, analysis, decision-making, and user interaction. Let's see how such a creation looks like so we get a sense of it:

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

    In the previous code we have a `GroupChatManager` that is registered with the runtime. This manager is responsible for coordinating the interactions between different types of agents, such as writers, illustrators, editors, and users.

- **Agent Runtime**. The framework provides a runtime environment, enabling communication between agents, manages their identities and lifecycles, and enforce security and privacy boundaries. This means that you can run your agents in a secure and controlled environment, ensuring that they can interact safely and efficiently. There are two runtimes of interest:
  - **Stand-alone runtime**. This is a good choice for single-process applications where all agents are implemented in the same programming language and run in the same process. Here's an illustration of how it works:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Stand-alone runtime</a>   
Application stack

    *agents communicate via messages through the runtime, and the runtime manages the lifecycle of agents*

  - **Distributed agent runtime**, is suitable for multi-process applications where agents may be implemented in different programming languages and running on different machines. Here's an illustration of how it works:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Distributed runtime</a>

## Semantic Kernel + Agent Framework

Semantic Kernel is an enterprise-ready AI Orchestration SDK. It consists of AI and memory connectors, along with an Agent Framework.

Let's first cover some core components:

- **AI Connectors**: This is an interface with external AI services and data sources for use in both Python and C#.

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

    Here you have a simple example of how you can create a kernel and add a chat completion service. Semantic Kernel creates a connection to an external AI service, in this case, Azure OpenAI Chat Completion.

- **Plugins**: These encapsulate functions that an application can use. There are both ready-made plugins and custom ones you can create. A related concept is "prompt functions." Instead of providing natural language cues for function invocation, you broadcast certain functions to the model. Based on the current chat context, the model may choose to call one of these functions to complete a request or query. Here's an example:

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

    Here, you first have a template prompt `skPrompt` that leaves room for the user to input text, `$userInput`. Then you create the kernel function `SummarizeText` and then import it into the kernel with the plugin name `SemanticFunctions`. Note the name of the function that helps Semantic Kernel understand what the function does and when it should be called.

- **Native function**: There's also native functions that the framework can call directly to carry out the task. Here's an example of such a function retrieving the content from a file:

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

- **Memory**:  Abstracts and simplifies context management for AI apps. The idea with memory is that this is something the LLM should know about. You can store this information in a vector store which ends up being an in-memory database or a vector database or similar. Here's an example of a very simplified scenario where *facts* are added to the memory:

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

    These facts are then stored in the memory collection `SummarizedAzureDocs`. This is a very simplified example, but you can see how you can store information in the memory for the LLM to use.

So that's the basics of the Semantic Kernel framework, what about the Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service is a more recent addition, introduced at Microsoft Ignite 2024. It allows for the development and deployment of AI agents with more flexible models, such as directly calling open-source LLMs like Llama 3, Mistral, and Cohere.

Azure AI Agent Service provides stronger enterprise security mechanisms and data storage methods, making it suitable for enterprise applications. 

It works out-of-the-box with multi-agent orchestration frameworks like AutoGen and Semantic Kernel.

This service is currently in Public Preview and supports Python and C# for building agents.

Using Semantic Kernel Python, we can create an Azure AI Agent with a user-defined plugin:

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

### Core concepts

Azure AI Agent Service has the following core concepts:

- **Agent**. Azure AI Agent Service integrates with Azure AI Foundry. Within AI Foundry, an AI Agent acts as a "smart" microservice that can be used to answer questions (RAG), perform actions, or completely automate workflows. It achieves this by combining the power of generative AI models with tools that allow it to access and interact with real-world data sources. Here's an example of an agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In this example, an agent is created with the model `gpt-4o-mini`, a name `my-agent`, and instructions `You are helpful agent`. The agent is equipped with tools and resources to perform code interpretation tasks.

- **Thread and messages**. The thread is another important concept. It represents a conversation or interaction between an agent and a user. Threads can be used to track the progress of a conversation, store context information, and manage the state of the interaction. Here's an example of a thread:

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

    In the previous code, a thread is created. Thereafter, a message is sent to the thread. By calling `create_and_process_run`, the agent is asked to perform work on the thread. Finally, the messages are fetched and logged to see the agent's response. The messages indicate the progress of the conversation between the user and the agent. It's also important to understand that the messages can be of different types such as text, image, or file, that is the agents work has resulted in for example an image or a text response for example. As a developer, you can then use this information to further process the response or present it to the user.

- **Integrates with other AI frameworks**. Azure AI Agent service can interact with other frameworks like AutoGen and Semantic Kernel, which means you can build part of your app in one of these frameworks and for example using the Agent service as an orchestrator or you can build everything in the Agent service.

**Use Cases**: Azure AI Agent Service is designed for enterprise applications that require secure, scalable, and flexible AI agent deployment.

## What's the difference between these frameworks?
 
It does sound like there is a lot of overlap between these frameworks, but there are some key differences in terms of their design, capabilities, and target use cases:
 
- **AutoGen**: Is an experimentation framework focused on leading-edge research on multi-agent systems. It is the best place to experiment and prototype sophisticated multi-agent systems.
- **Semantic Kernel**: Is a production-ready agent library for building enterprise agentic applications. Focuses on event-driven, distributed agentic applications, enabling multiple LLMs and SLMs, tools, and single/multi-agent design patterns.
- **Azure AI Agent Service**: Is a platform and deployment service in Azure Foundry for agents. It offers building connectivity to services support by Azure Found like Azure OpenAI, Azure AI Search, Bing Search and code execution.
 
Still not sure which one to choose?

### Use Cases
 
Let's see if we can help you by going through some common use cases:
 
> Q: I'm experimenting, learning and building proof-of-concept agent applications, and I want to be able to build and experiment quickly
>

>A: AutoGen would be a good choice for this scenario, as it focuses on event-driven, distributed agentic applications and supports advanced multi-agent design patterns.

> Q: What makes AutoGen a better choice than Semantic Kernel and Azure AI Agent Service for this use case?
>
> A: AutoGen is specifically designed for event-driven, distributed agentic applications, making it well-suited for automating code generation and data analysis tasks. It provides the necessary tools and capabilities to build complex multi-agent systems efficiently.

>Q: Sounds like Azure AI Agent Service could work here too, it has tools for code generation and more?

>
> A: Yes, Azure AI Agent Service is a platform service for agents and add built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
 
> Q: I'm still confused just give me one option
>
> A: A great choice is to build your application in Semantic Kernel first and then use Azure AI Agent Service to deploy your agent. This approach allows you to easily persist your agents while leveraging the power to build multi-agent systems in Semantic Kernel. Additionally, Semantic Kernel has a connector in AutoGen, making it easy to use both frameworks together.
 
Let's summarize the key differences in a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| AutoGen | Event-driven, distributed agentic applications | Agents, Personas, Functions, Data | Code generation, data analysis tasks |
| Semantic Kernel | Understanding and generating human-like text content | Agents, Modular Components, Collaboration | Natural language understanding, content generation |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

What's the ideal use case for each of these frameworks?

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?

The answer is yes, you can integrate your existing Azure ecosystem tools directly with Azure AI Agent Service especially, this because it has been built to work seamlessly with other Azure services. You could for example integrate Bing, Azure AI Search, and Azure Functions. There's also deep integration with Azure AI Foundry.

For AutoGen and Semantic Kernel, you can also integrate with Azure services, but it may require you to call the Azure services from your code. Another way to integrate is to use the Azure SDKs to interact with Azure services from your agents. Additionally, like was mentioned, you can use Azure AI Agent Service as an orchestrator for your agents built in AutoGen or Semantic Kernel which would give easy access to the Azure ecosystem.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel and AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)
