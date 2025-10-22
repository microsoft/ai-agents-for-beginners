<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86b9c2b24da3b3e61711182ffa72601c",
  "translation_date": "2025-09-29T22:10:45+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "bn"
}
-->
[![Exploring AI Agent Frameworks](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.bn.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(উপরের ছবিতে ক্লিক করে এই পাঠের ভিডিও দেখুন)_

# AI এজেন্ট ফ্রেমওয়ার্ক অন্বেষণ করুন

AI এজেন্ট ফ্রেমওয়ার্ক হলো সফটওয়্যার প্ল্যাটফর্ম যা AI এজেন্ট তৈরি, স্থাপন এবং পরিচালনা সহজতর করার জন্য ডিজাইন করা হয়েছে। এই ফ্রেমওয়ার্কগুলো ডেভেলপারদের জন্য পূর্বনির্মিত উপাদান, অ্যাবস্ট্রাকশন এবং টুল সরবরাহ করে যা জটিল AI সিস্টেমের উন্নয়নকে সহজ করে তোলে।

এই ফ্রেমওয়ার্কগুলো ডেভেলপারদের তাদের অ্যাপ্লিকেশনের অনন্য দিকগুলোর উপর মনোযোগ কেন্দ্রীভূত করতে সাহায্য করে, AI এজেন্ট উন্নয়নের সাধারণ চ্যালেঞ্জগুলোর জন্য মানসম্মত পদ্ধতি প্রদান করে। এগুলো AI সিস্টেম তৈরিতে স্কেলযোগ্যতা, অ্যাক্সেসযোগ্যতা এবং দক্ষতা বৃদ্ধি করে।

## পরিচিতি

এই পাঠে আলোচনা করা হবে:

- AI এজেন্ট ফ্রেমওয়ার্ক কী এবং ডেভেলপারদের কী অর্জন করতে সক্ষম করে?
- দলগুলো কীভাবে দ্রুত প্রোটোটাইপ তৈরি, পুনরাবৃত্তি এবং তাদের এজেন্টের সক্ষমতা উন্নত করতে পারে?
- Microsoft-এর তৈরি <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, এবং <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> ফ্রেমওয়ার্ক এবং টুলগুলোর মধ্যে পার্থক্য কী?
- আমি কি আমার বিদ্যমান Azure ইকোসিস্টেম টুলগুলো সরাসরি সংযুক্ত করতে পারি, নাকি আলাদা সমাধান প্রয়োজন?
- Azure AI Agents সার্ভিস কী এবং এটি কীভাবে আমাকে সাহায্য করছে?

## শেখার লক্ষ্য

এই পাঠের লক্ষ্য হলো আপনাকে বুঝতে সাহায্য করা:

- AI এজেন্ট ফ্রেমওয়ার্কের ভূমিকা AI উন্নয়নে।
- বুদ্ধিমান এজেন্ট তৈরি করতে AI এজেন্ট ফ্রেমওয়ার্ক ব্যবহার করা।
- AI এজেন্ট ফ্রেমওয়ার্ক দ্বারা সক্ষম করা মূল বৈশিষ্ট্য।
- AutoGen, Semantic Kernel, এবং Azure AI Agent Service-এর মধ্যে পার্থক্য।

## AI এজেন্ট ফ্রেমওয়ার্ক কী এবং ডেভেলপারদের কী করতে সক্ষম করে?

প্রথাগত AI ফ্রেমওয়ার্কগুলো আপনার অ্যাপ্লিকেশনে AI সংযুক্ত করতে এবং নিম্নলিখিত উপায়ে এই অ্যাপগুলোকে উন্নত করতে সাহায্য করতে পারে:

- **ব্যক্তিগতকরণ**: AI ব্যবহারকারীর আচরণ এবং পছন্দ বিশ্লেষণ করে ব্যক্তিগতকৃত সুপারিশ, কন্টেন্ট এবং অভিজ্ঞতা প্রদান করতে পারে।
উদাহরণ: Netflix-এর মতো স্ট্রিমিং সার্ভিসগুলো AI ব্যবহার করে দেখার ইতিহাসের উপর ভিত্তি করে সিনেমা এবং শো সুপারিশ করে, যা ব্যবহারকারীর সম্পৃক্ততা এবং সন্তুষ্টি বাড়ায়।
- **স্বয়ংক্রিয়তা এবং দক্ষতা**: AI পুনরাবৃত্তিমূলক কাজগুলো স্বয়ংক্রিয় করতে, কর্মপ্রবাহ সহজতর করতে এবং অপারেশনাল দক্ষতা উন্নত করতে পারে।
উদাহরণ: কাস্টমার সার্ভিস অ্যাপগুলো AI-চালিত চ্যাটবট ব্যবহার করে সাধারণ প্রশ্নের উত্তর দেয়, প্রতিক্রিয়া সময় কমায় এবং মানব এজেন্টদের আরও জটিল সমস্যার জন্য মুক্ত করে।
- **উন্নত ব্যবহারকারীর অভিজ্ঞতা**: AI ভয়েস রিকগনিশন, প্রাকৃতিক ভাষা প্রক্রিয়াকরণ এবং প্রেডিক্টিভ টেক্সটের মতো বুদ্ধিমান বৈশিষ্ট্য প্রদান করে সামগ্রিক ব্যবহারকারীর অভিজ্ঞতা উন্নত করতে পারে।
উদাহরণ: Siri এবং Google Assistant-এর মতো ভার্চুয়াল অ্যাসিস্ট্যান্ট AI ব্যবহার করে ভয়েস কমান্ড বুঝতে এবং সাড়া দিতে, ব্যবহারকারীদের তাদের ডিভাইসের সাথে সহজে যোগাযোগ করতে সাহায্য করে।

### সবকিছুই চমৎকার শোনাচ্ছে, তাহলে AI এজেন্ট ফ্রেমওয়ার্ক কেন প্রয়োজন?

AI এজেন্ট ফ্রেমওয়ার্কগুলো AI ফ্রেমওয়ার্কের চেয়ে বেশি কিছু উপস্থাপন করে। এগুলো এমন বুদ্ধিমান এজেন্ট তৈরি করতে ডিজাইন করা হয়েছে যা ব্যবহারকারী, অন্যান্য এজেন্ট এবং পরিবেশের সাথে যোগাযোগ করতে পারে নির্দিষ্ট লক্ষ্য অর্জনের জন্য। এই এজেন্টগুলো স্বায়ত্তশাসিত আচরণ প্রদর্শন করতে পারে, সিদ্ধান্ত নিতে পারে এবং পরিবর্তিত পরিস্থিতির সাথে মানিয়ে নিতে পারে। আসুন AI এজেন্ট ফ্রেমওয়ার্ক দ্বারা সক্ষম করা কিছু মূল বৈশিষ্ট্য দেখি:

- **এজেন্ট সহযোগিতা এবং সমন্বয়**: একাধিক AI এজেন্ট তৈরি করা সম্ভব করে যা একসাথে কাজ করতে পারে, যোগাযোগ করতে পারে এবং জটিল কাজ সমাধানে সমন্বয় করতে পারে।
- **কাজের স্বয়ংক্রিয়তা এবং ব্যবস্থাপনা**: মাল্টি-স্টেপ কর্মপ্রবাহ, কাজের প্রতিনিধিত্ব এবং এজেন্টদের মধ্যে গতিশীল কাজ ব্যবস্থাপনার জন্য প্রক্রিয়া প্রদান করে।
- **প্রাসঙ্গিক বোঝাপড়া এবং অভিযোজন**: এজেন্টদের প্রাসঙ্গিকতা বুঝতে, পরিবর্তিত পরিবেশের সাথে মানিয়ে নিতে এবং রিয়েল-টাইম তথ্যের উপর ভিত্তি করে সিদ্ধান্ত নিতে সক্ষম করে।

সারসংক্ষেপে, এজেন্টগুলো আপনাকে আরও বেশি কিছু করতে, স্বয়ংক্রিয়তাকে পরবর্তী স্তরে নিয়ে যেতে এবং আরও বুদ্ধিমান সিস্টেম তৈরি করতে সক্ষম করে যা তাদের পরিবেশ থেকে শিখতে এবং মানিয়ে নিতে পারে।

## কীভাবে দ্রুত প্রোটোটাইপ তৈরি, পুনরাবৃত্তি এবং এজেন্টের সক্ষমতা উন্নত করবেন?

এটি একটি দ্রুত পরিবর্তনশীল ক্ষেত্র, তবে বেশিরভাগ AI এজেন্ট ফ্রেমওয়ার্কে কিছু সাধারণ বিষয় রয়েছে যা আপনাকে দ্রুত প্রোটোটাইপ এবং পুনরাবৃত্তি করতে সাহায্য করতে পারে, যেমন মডিউল উপাদান, সহযোগী টুল এবং রিয়েল-টাইম লার্নিং। আসুন এগুলো নিয়ে আলোচনা করি:

- **মডুলার উপাদান ব্যবহার করুন**: AI SDK-গুলো পূর্বনির্মিত উপাদান সরবরাহ করে, যেমন AI এবং মেমরি সংযোগকারী, প্রাকৃতিক ভাষা বা কোড প্লাগইন ব্যবহার করে ফাংশন কলিং, প্রম্পট টেমপ্লেট এবং আরও অনেক কিছু।
- **সহযোগী টুল ব্যবহার করুন**: নির্দিষ্ট ভূমিকা এবং কাজের জন্য এজেন্ট ডিজাইন করুন, সহযোগী কর্মপ্রবাহ পরীক্ষা এবং পরিমার্জন সক্ষম করুন।
- **রিয়েল-টাইমে শিখুন**: প্রতিক্রিয়া লুপ বাস্তবায়ন করুন যেখানে এজেন্টগুলো ইন্টারঅ্যাকশন থেকে শিখে এবং তাদের আচরণ গতিশীলভাবে সামঞ্জস্য করে।

### মডুলার উপাদান ব্যবহার করুন

Microsoft Semantic Kernel এবং LangChain-এর মতো SDK-গুলো AI সংযোগকারী, প্রম্পট টেমপ্লেট এবং মেমরি ব্যবস্থাপনার মতো পূর্বনির্মিত উপাদান সরবরাহ করে।

**দলগুলো কীভাবে ব্যবহার করতে পারে**: দলগুলো এই উপাদানগুলো দ্রুত একত্রিত করে একটি কার্যকরী প্রোটোটাইপ তৈরি করতে পারে, যা স্ক্র্যাচ থেকে শুরু না করেই দ্রুত পরীক্ষা এবং পুনরাবৃত্তি করার অনুমতি দেয়।

**এটি বাস্তবে কীভাবে কাজ করে**: আপনি একটি পূর্বনির্মিত পার্সার ব্যবহার করতে পারেন ব্যবহারকারীর ইনপুট থেকে তথ্য বের করতে, একটি মেমরি মডিউল ডেটা সংরক্ষণ এবং পুনরুদ্ধার করতে, এবং একটি প্রম্পট জেনারেটর ব্যবহারকারীদের সাথে যোগাযোগ করতে, সবকিছু স্ক্র্যাচ থেকে তৈরি না করেই।

**উদাহরণ কোড**। আসুন Semantic Kernel Python এবং .Net-এর সাথে একটি পূর্বনির্মিত AI সংযোগকারী ব্যবহার করার উদাহরণ দেখি যা ব্যবহারকারীর ইনপুটের প্রতিক্রিয়া জানাতে মডেলকে স্বয়ংক্রিয়ভাবে ফাংশন কলিং ব্যবহার করে:

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

এই উদাহরণ থেকে আপনি দেখতে পাচ্ছেন কীভাবে আপনি একটি পূর্বনির্মিত পার্সার ব্যবহার করে ব্যবহারকারীর ইনপুট থেকে মূল তথ্য বের করতে পারেন, যেমন একটি ফ্লাইট বুকিং অনুরোধের উৎস, গন্তব্য এবং তারিখ। এই মডুলার পদ্ধতি আপনাকে উচ্চ-স্তরের যুক্তির উপর মনোযোগ কেন্দ্রীভূত করতে দেয়।

### সহযোগী টুল ব্যবহার করুন

CrewAI, Microsoft AutoGen এবং Semantic Kernel-এর মতো ফ্রেমওয়ার্কগুলো একাধিক এজেন্ট তৈরি করার সুবিধা দেয় যা একসাথে কাজ করতে পারে।

**দলগুলো কীভাবে ব্যবহার করতে পারে**: দলগুলো নির্দিষ্ট ভূমিকা এবং কাজের জন্য এজেন্ট ডিজাইন করতে পারে, সহযোগী কর্মপ্রবাহ পরীক্ষা এবং পরিমার্জন করতে পারে এবং সামগ্রিক সিস্টেম দক্ষতা উন্নত করতে পারে।

**এটি বাস্তবে কীভাবে কাজ করে**: আপনি এজেন্টদের একটি দল তৈরি করতে পারেন যেখানে প্রতিটি এজেন্টের একটি বিশেষায়িত ফাংশন রয়েছে, যেমন ডেটা পুনরুদ্ধার, বিশ্লেষণ বা সিদ্ধান্ত গ্রহণ। এই এজেন্টগুলো একটি সাধারণ লক্ষ্য অর্জনের জন্য তথ্য যোগাযোগ এবং শেয়ার করতে পারে, যেমন ব্যবহারকারীর প্রশ্নের উত্তর দেওয়া বা একটি কাজ সম্পন্ন করা।

**উদাহরণ কোড (AutoGen)**:

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

পূর্ববর্তী কোডে আপনি দেখতে পাচ্ছেন কীভাবে আপনি একটি কাজ তৈরি করতে পারেন যা একাধিক এজেন্ট একসাথে ডেটা বিশ্লেষণ করতে কাজ করে। প্রতিটি এজেন্ট একটি নির্দিষ্ট ফাংশন সম্পাদন করে, এবং কাজটি এজেন্টদের সমন্বয় করে কাঙ্ক্ষিত ফলাফল অর্জনের মাধ্যমে সম্পন্ন হয়। বিশেষায়িত ভূমিকা সহ নিবেদিত এজেন্ট তৈরি করে, আপনি কাজের দক্ষতা এবং কর্মক্ষমতা উন্নত করতে পারেন।

### রিয়েল-টাইমে শিখুন

উন্নত ফ্রেমওয়ার্কগুলো রিয়েল-টাইম প্রাসঙ্গিক বোঝাপড়া এবং অভিযোজনের জন্য সক্ষমতা প্রদান করে।

**দলগুলো কীভাবে ব্যবহার করতে পারে**: দলগুলো প্রতিক্রিয়া লুপ বাস্তবায়ন করতে পারে যেখানে এজেন্টগুলো ইন্টারঅ্যাকশন থেকে শিখে এবং তাদের আচরণ গতিশীলভাবে সামঞ্জস্য করে, যা ক্রমাগত উন্নতি এবং সক্ষমতার পরিমার্জন ঘটায়।

**এটি বাস্তবে কীভাবে কাজ করে**: এজেন্টগুলো ব্যবহারকারীর প্রতিক্রিয়া, পরিবেশগত ডেটা এবং কাজের ফলাফল বিশ্লেষণ করতে পারে তাদের জ্ঞানভাণ্ডার আপডেট করতে, সিদ্ধান্ত গ্রহণের অ্যালগরিদম সামঞ্জস্য করতে এবং সময়ের সাথে কর্মক্ষমতা উন্নত করতে। এই পুনরাবৃত্তিমূলক শেখার প্রক্রিয়া এজেন্টগুলোকে পরিবর্তিত পরিস্থিতি এবং ব্যবহারকারীর পছন্দের সাথে মানিয়ে নিতে সক্ষম করে, সামগ্রিক সিস্টেম কার্যকারিতা উন্নত করে।

## AutoGen, Semantic Kernel এবং Azure AI Agent Service-এর মধ্যে পার্থক্য কী?

এই ফ্রেমওয়ার্কগুলো তুলনা করার অনেক উপায় রয়েছে, তবে আসুন তাদের ডিজাইন, সক্ষমতা এবং লক্ষ্য ব্যবহার ক্ষেত্রে কিছু মূল পার্থক্য দেখি:

## AutoGen

AutoGen হলো Microsoft Research-এর AI Frontiers Lab দ্বারা উন্নত একটি ওপেন-সোর্স ফ্রেমওয়ার্ক। এটি ইভেন্ট-চালিত, বিতরণকৃত *agentic* অ্যাপ্লিকেশনগুলোর উপর ফোকাস করে, একাধিক LLMs এবং SLMs, টুল এবং উন্নত মাল্টি-এজেন্ট ডিজাইন প্যাটার্ন সক্ষম করে।

AutoGen এজেন্টের মূল ধারণার উপর ভিত্তি করে তৈরি, যা স্বায়ত্তশাসিত সত্তা যা তাদের পরিবেশ উপলব্ধি করতে পারে, সিদ্ধান্ত নিতে পারে এবং নির্দিষ্ট লক্ষ্য অর্জনের জন্য পদক্ষেপ নিতে পারে। এজেন্টগুলো অ্যাসিঙ্ক্রোনাস মেসেজের মাধ্যমে যোগাযোগ করে, তাদের স্বাধীনভাবে এবং সমান্তরালভাবে কাজ করতে সক্ষম করে, সিস্টেমের স্কেলযোগ্যতা এবং প্রতিক্রিয়াশীলতা উন্নত করে।

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">এজেন্টগুলো অ্যাক্টর মডেলের উপর ভিত্তি করে</a>। Wikipedia অনুযায়ী, একটি অ্যাক্টর হলো _একটি বার্তা প্রাপ্তির প্রতিক্রিয়ায় স্থানীয় সিদ্ধান্ত নিতে পারে, আরও অ্যাক্টর তৈরি করতে পারে, আরও বার্তা পাঠাতে পারে এবং পরবর্তী বার্তা প্রাপ্তির প্রতিক্রিয়া কীভাবে হবে তা নির্ধারণ করতে পারে_।

**ব্যবহার ক্ষেত্র**: কোড জেনারেশন, ডেটা বিশ্লেষণ কাজ স্বয়ংক্রিয় করা এবং পরিকল্পনা ও গবেষণা ফাংশনের জন্য কাস্টম এজেন্ট তৈরি করা।

AutoGen-এর কিছু গুরুত্বপূর্ণ মূল ধারণা এখানে:

- **এজেন্ট**। একটি এজেন্ট হলো একটি সফটওয়্যার সত্তা যা:
  - **বার্তার মাধ্যমে যোগাযোগ করে**, এই বার্তাগুলো সিঙ্ক্রোনাস বা অ্যাসিঙ্ক্রোনাস হতে পারে।
  - **নিজস্ব অবস্থা বজায় রাখে**, যা আগত বার্তাগুলোর মাধ্যমে পরিবর্তিত হতে পারে।
  - **পদক্ষেপ গ্রহণ করে** প্রাপ্ত বার্তা বা তার অবস্থার পরিবর্তনের প্রতিক্রিয়ায়। এই পদক্ষেপগুলো এজেন্টের অবস্থাকে পরিবর্তন করতে পারে এবং বাহ্যিক প্রভাব তৈরি করতে পারে, যেমন বার্তা লগ আপডেট করা, নতুন বার্তা পাঠানো, কোড কার্যকর করা বা API কল করা।

  এখানে একটি সংক্ষিপ্ত কোড স্নিপেট রয়েছে যেখানে আপনি চ্যাট সক্ষমতা সহ আপনার নিজস্ব এজেন্ট তৈরি করেন:

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
    
    পূর্ববর্তী কোডে, `MyAgent` তৈরি করা হয়েছে এবং `RoutedAgent` থেকে উত্তরাধিকারী হয়েছে। এতে একটি বার্তা হ্যান্ডলার রয়েছে যা বার্তার বিষয়বস্তু প্রিন্ট করে এবং তারপর `AssistantAgent` ডেলিগেট ব্যবহার করে একটি প্রতিক্রিয়া পাঠায়। বিশেষভাবে লক্ষ্য করুন কীভাবে আমরা `self._delegate`-এ `AssistantAgent`-এর একটি ইনস্ট্যান্স বরাদ্দ করি, যা একটি পূর্বনির্মিত এজেন্ট যা চ্যাট সম্পন্ন পরিচালনা করতে পারে।

    AutoGen-কে এই এজেন্ট টাইপ সম্পর্কে জানাতে এবং প্রোগ্রাম শুরু করতে দিন:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    পূর্ববর্তী কোডে এজেন্টগুলো রানটাইমে নিবন্ধিত হয় এবং তারপর এজেন্টে একটি বার্তা পাঠানো হয় যার ফলে নিম্নলিখিত আউটপুট তৈরি হয়:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **মাল্টি এজেন্ট**। AutoGen একাধিক এজেন্ট তৈরি করার সুবিধা দেয় যা জটিল কাজ অর্জনের জন্য একসাথে কাজ করতে পারে। এজেন্টগুলো যোগাযোগ করতে পারে, তথ্য শেয়ার করতে পারে এবং সমস্যাগুলো আরও দক্ষতার সাথে সমাধান করতে তাদের পদক্ষেপগুলো সমন্বয় করতে পারে। একটি মাল্টি-এজেন্ট সিস্টেম তৈরি করতে, আপনি বিভিন্ন ধরনের এজেন্ট সংজ্ঞায়িত করতে পারেন যাদের বিশেষায়িত ফাংশন এবং ভূমিকা রয়েছে, যেমন ডেটা পুনরুদ্ধার, বিশ্লেষণ, সিদ্ধান্ত গ্রহণ এবং ব্যবহারকারীর সাথে যোগাযোগ। আসুন এমন একটি সৃষ্টির চেহারা দেখি যাতে আমরা এর একটি ধারণা পাই:

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

    পূর্ববর্তী কোডে আমাদের একটি `GroupChatManager` রয়েছে যা রানটাইমে নিবন্ধিত হয়। এই ম্যানেজার বিভিন্ন ধরনের এজেন্টের মধ্যে ইন্টারঅ্যাকশন সমন্বয় করার জন্য দায়ী, যেমন লেখক, চিত্রশিল্পী, সম্পাদক এবং ব্যবহারকারী।

- **এজেন্ট রানটাইম**। ফ্রেমওয়ার্কটি একটি রানটাইম পরিবেশ প্রদান করে, এজেন্টদের মধ্যে যোগাযোগ সক্ষম করে, তাদের পরিচয় এবং জীবনচক্র পরিচালনা করে এবং নিরাপত্তা এবং গোপনীয়তার সীমানা প্রয়োগ করে। এর মানে হলো আপনি আপনার এজেন্টগুলোকে একটি নিরাপদ এবং নিয়ন্ত্রিত পরিবেশে চালাতে পারেন, নিশ্চিত করে যে তারা নিরাপদে এবং দক্ষতার সাথে যোগাযোগ করতে পারে। এখানে দুটি গুরুত্বপূর্ণ রানটাইম রয়েছে:
  - **স্ট্যান্ড-অ্যালোন রানটাইম**। এটি একক-প্রক্রিয়া অ্যাপ্লিকেশনের জন্য একটি ভাল পছন্দ যেখানে সমস্ত এজেন্ট একই প্রোগ্রামিং ভাষায় বাস্তবায়িত হয় এবং একই প্রক্রিয়ায় চলে। এটি কীভাবে কাজ করে তার একটি চিত্র এখানে রয়েছে:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">স্ট্যান্ড-অ্যালোন রানটাইম</a>   
অ্যাপ্লিকেশন স্ট্যাক

    *এজেন্টগুলো রানটাইমের মাধ্যমে বার্তার মাধ্যমে যোগাযোগ করে, এবং রানটাইম এজেন্টদের জীবনচক্র পরিচালনা করে*

  - **বিতরণকৃত এজেন্ট রানটাইম**, এটি মাল্টি-প্রক্রিয়া অ্যাপ্লিকেশনের জন্য উপযুক্ত যেখানে এজেন্টগুলো বিভিন্ন প্রোগ্রামিং ভাষায় বাস্তবায়িত হতে পারে এবং বিভিন্ন মেশিনে চলতে পারে। এটি কীভাবে কাজ করে তার একটি চিত্র এখানে রয়েছে:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">বিতরণকৃত রানটাইম</a>

## Semantic Kernel + এজেন্ট ফ্রেমওয়ার্ক

Semantic Kernel হলো একটি এন্টারপ্রাইজ-রেডি AI অর্কেস্ট্রেশন SDK। এটি AI এবং মেমরি সংযোগকারী, পাশাপাশি একটি এজেন্ট ফ্রেমওয়ার্ক নিয়ে গঠিত।

প্রথমে কিছু মূল উপাদান কভার করা যাক:

- **AI সংযোগকারী**: এটি বাইরের AI সার্ভিস এবং ডেটা সোর্সের সাথে ইন্টারফেস তৈরি করে Python এবং C# উভয়ের জন্য ব্যবহারের জন্য।


এই তথ্যগুলো তারপর মেমরি সংগ্রহে `SummarizedAzureDocs`-এ সংরক্ষণ করা হয়। এটি একটি খুব সহজ উদাহরণ, তবে আপনি দেখতে পাচ্ছেন কীভাবে তথ্য মেমরিতে সংরক্ষণ করা যায় যাতে LLM এটি ব্যবহার করতে পারে।

এখন পর্যন্ত আমরা Semantic Kernel ফ্রেমওয়ার্কের মৌলিক বিষয়গুলো আলোচনা করেছি, এবার Agent Framework সম্পর্কে কথা বলি।

## Azure AI Agent Service

Azure AI Agent Service Microsoft Ignite 2024-এ চালু হওয়া একটি সাম্প্রতিক সংযোজন। এটি AI এজেন্ট তৈরি এবং মোতায়েনের জন্য আরও নমনীয় মডেল সরবরাহ করে, যেমন Llama 3, Mistral, এবং Cohere-এর মতো ওপেন-সোর্স LLM সরাসরি কল করা।

Azure AI Agent Service শক্তিশালী এন্টারপ্রাইজ নিরাপত্তা ব্যবস্থা এবং ডেটা সংরক্ষণের পদ্ধতি প্রদান করে, যা এটিকে এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য উপযুক্ত করে তোলে।

এটি AutoGen এবং Semantic Kernel-এর মতো মাল্টি-এজেন্ট অর্কেস্ট্রেশন ফ্রেমওয়ার্কের সাথে সরাসরি কাজ করে।

এই পরিষেবা বর্তমানে Public Preview-এ রয়েছে এবং Python এবং C#-এ এজেন্ট তৈরির জন্য সমর্থন প্রদান করে।

Semantic Kernel Python ব্যবহার করে, আমরা একটি ব্যবহারকারী-সংজ্ঞায়িত প্লাগইন সহ একটি Azure AI Agent তৈরি করতে পারি:

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

### মূল ধারণা

Azure AI Agent Service-এর নিম্নলিখিত মূল ধারণাগুলো রয়েছে:

- **Agent**: Azure AI Agent Service Azure AI Foundry-এর সাথে সংযুক্ত। AI Foundry-এর মধ্যে, একটি AI Agent একটি "স্মার্ট" মাইক্রোসার্ভিস হিসেবে কাজ করে যা প্রশ্নের উত্তর দিতে (RAG), কাজ সম্পাদন করতে বা সম্পূর্ণভাবে ওয়ার্কফ্লো স্বয়ংক্রিয় করতে ব্যবহৃত হয়। এটি জেনারেটিভ AI মডেলের শক্তি এবং বাস্তব-জগতের ডেটা সোর্সে অ্যাক্সেস ও ইন্টারঅ্যাক্ট করার জন্য টুলগুলোর সংমিশ্রণ ব্যবহার করে। এখানে একটি এজেন্টের উদাহরণ দেওয়া হলো:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    এই উদাহরণে, `gpt-4o-mini` মডেল, `my-agent` নাম এবং `You are helpful agent` নির্দেশনা সহ একটি এজেন্ট তৈরি করা হয়েছে। এজেন্টটি কোড ইন্টারপ্রিটেশন কাজ সম্পাদনের জন্য টুল এবং রিসোর্স দিয়ে সজ্জিত।

- **Thread এবং Messages**: থ্রেড একটি গুরুত্বপূর্ণ ধারণা। এটি একটি এজেন্ট এবং ব্যবহারকারীর মধ্যে কথোপকথন বা ইন্টারঅ্যাকশনকে উপস্থাপন করে। থ্রেড কথোপকথনের অগ্রগতি ট্র্যাক করতে, প্রসঙ্গ তথ্য সংরক্ষণ করতে এবং ইন্টারঅ্যাকশনের অবস্থা পরিচালনা করতে ব্যবহার করা যেতে পারে। এখানে একটি থ্রেডের উদাহরণ:

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

    পূর্ববর্তী কোডে, একটি থ্রেড তৈরি করা হয়েছে। এরপর, থ্রেডে একটি বার্তা পাঠানো হয়েছে। `create_and_process_run` কল করে, এজেন্টকে থ্রেডে কাজ সম্পাদন করতে বলা হয়েছে। শেষে, বার্তাগুলো সংগ্রহ করা হয়েছে এবং এজেন্টের প্রতিক্রিয়া দেখতে লগ করা হয়েছে। বার্তাগুলো ব্যবহারকারী এবং এজেন্টের মধ্যে কথোপকথনের অগ্রগতি নির্দেশ করে। এটি বোঝা গুরুত্বপূর্ণ যে বার্তাগুলো বিভিন্ন ধরনের হতে পারে যেমন টেক্সট, ইমেজ বা ফাইল, যা এজেন্টের কাজের ফলাফল হতে পারে। একজন ডেভেলপার হিসেবে, আপনি এই তথ্য ব্যবহার করে প্রতিক্রিয়াটি আরও প্রক্রিয়াকরণ করতে বা ব্যবহারকারীর কাছে উপস্থাপন করতে পারেন।

- **অন্যান্য AI ফ্রেমওয়ার্কের সাথে ইন্টিগ্রেশন**: Azure AI Agent Service AutoGen এবং Semantic Kernel-এর মতো অন্যান্য ফ্রেমওয়ার্কের সাথে ইন্টারঅ্যাক্ট করতে পারে, যার অর্থ আপনি আপনার অ্যাপের একটি অংশ এই ফ্রেমওয়ার্কগুলোর মধ্যে একটিতে তৈরি করতে পারেন এবং উদাহরণস্বরূপ Agent Service-কে অর্কেস্ট্রেটর হিসেবে ব্যবহার করতে পারেন অথবা সবকিছু Agent Service-এ তৈরি করতে পারেন।

**ব্যবহার ক্ষেত্র**: Azure AI Agent Service এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য ডিজাইন করা হয়েছে যা নিরাপদ, স্কেলযোগ্য এবং নমনীয় AI এজেন্ট মোতায়েনের প্রয়োজন।

## এই ফ্রেমওয়ার্কগুলোর মধ্যে পার্থক্য কী?

এটি মনে হতে পারে যে এই ফ্রেমওয়ার্কগুলোর মধ্যে অনেকটা মিল রয়েছে, তবে তাদের ডিজাইন, সক্ষমতা এবং লক্ষ্য ব্যবহার ক্ষেত্রের ক্ষেত্রে কিছু গুরুত্বপূর্ণ পার্থক্য রয়েছে:

- **AutoGen**: মাল্টি-এজেন্ট সিস্টেমের উপর অগ্রণী গবেষণার জন্য একটি পরীক্ষামূলক ফ্রেমওয়ার্ক। এটি জটিল মাল্টি-এজেন্ট সিস্টেমের প্রোটোটাইপ তৈরি এবং পরীক্ষা করার জন্য সেরা জায়গা।
- **Semantic Kernel**: এন্টারপ্রাইজ এজেন্টিক অ্যাপ্লিকেশন তৈরির জন্য একটি প্রোডাকশন-রেডি এজেন্ট লাইব্রেরি। এটি ইভেন্ট-চালিত, বিতরণকৃত এজেন্টিক অ্যাপ্লিকেশনগুলোর উপর ফোকাস করে, যা একাধিক LLM এবং SLM, টুল এবং একক/মাল্টি-এজেন্ট ডিজাইন প্যাটার্ন সক্ষম করে।
- **Azure AI Agent Service**: Azure Foundry-তে এজেন্টের জন্য একটি প্ল্যাটফর্ম এবং মোতায়েন পরিষেবা। এটি Azure OpenAI, Azure AI Search, Bing Search এবং কোড এক্সিকিউশনের মতো Azure Found দ্বারা সমর্থিত পরিষেবাগুলোর সাথে সংযোগ তৈরি করার সুবিধা প্রদান করে।

এখনও নিশ্চিত নন কোনটি বেছে নেবেন?

### ব্যবহার ক্ষেত্র

চলুন কিছু সাধারণ ব্যবহার ক্ষেত্রের মাধ্যমে আপনাকে সাহায্য করি:

> প্রশ্ন: আমি পরীক্ষা করছি, শিখছি এবং প্রুফ-অফ-কনসেপ্ট এজেন্ট অ্যাপ্লিকেশন তৈরি করছি, এবং আমি দ্রুত তৈরি ও পরীক্ষা করতে চাই।
>

>উত্তর: AutoGen এই পরিস্থিতির জন্য একটি ভালো পছন্দ হবে, কারণ এটি ইভেন্ট-চালিত, বিতরণকৃত এজেন্টিক অ্যাপ্লিকেশনগুলোর উপর ফোকাস করে এবং উন্নত মাল্টি-এজেন্ট ডিজাইন প্যাটার্ন সমর্থন করে।

> প্রশ্ন: এই ক্ষেত্রে Semantic Kernel এবং Azure AI Agent Service-এর চেয়ে AutoGen কেন ভালো পছন্দ?
>
> উত্তর: AutoGen বিশেষভাবে ইভেন্ট-চালিত, বিতরণকৃত এজেন্টিক অ্যাপ্লিকেশনগুলোর জন্য ডিজাইন করা হয়েছে, যা কোড জেনারেশন এবং ডেটা বিশ্লেষণ কাজগুলো স্বয়ংক্রিয় করার জন্য উপযুক্ত। এটি জটিল মাল্টি-এজেন্ট সিস্টেম দক্ষতার সাথে তৈরি করার জন্য প্রয়োজনীয় টুল এবং সক্ষমতা প্রদান করে।

>প্রশ্ন: মনে হচ্ছে Azure AI Agent Service এখানে কাজ করতে পারে, এতে কোড জেনারেশন এবং আরও অনেক কিছু করার টুল রয়েছে?
>
>উত্তর: হ্যাঁ, Azure AI Agent Service এজেন্টের জন্য একটি প্ল্যাটফর্ম পরিষেবা এবং এতে একাধিক মডেল, Azure AI Search, Bing Search এবং Azure Functions-এর জন্য বিল্ট-ইন সক্ষমতা রয়েছে। এটি Foundry Portal-এ আপনার এজেন্ট তৈরি এবং স্কেলে মোতায়েন করা সহজ করে তোলে।

> প্রশ্ন: আমি এখনও বিভ্রান্ত, আমাকে একটি অপশন দিন।
>
> উত্তর: একটি দুর্দান্ত পছন্দ হলো প্রথমে Semantic Kernel-এ আপনার অ্যাপ্লিকেশন তৈরি করা এবং তারপর Azure AI Agent Service ব্যবহার করে আপনার এজেন্ট মোতায়েন করা। এই পদ্ধতিতে আপনি সহজেই আপনার এজেন্ট সংরক্ষণ করতে পারবেন এবং Semantic Kernel-এ মাল্টি-এজেন্ট সিস্টেম তৈরির ক্ষমতা ব্যবহার করতে পারবেন। এছাড়াও, Semantic Kernel-এর AutoGen-এ একটি সংযোগকারী রয়েছে, যা উভয় ফ্রেমওয়ার্ক একসাথে ব্যবহার করা সহজ করে তোলে।

চলুন একটি টেবিলে মূল পার্থক্যগুলো সংক্ষেপে দেখি:

| ফ্রেমওয়ার্ক | ফোকাস | মূল ধারণা | ব্যবহার ক্ষেত্র |
| --- | --- | --- | --- |
| AutoGen | ইভেন্ট-চালিত, বিতরণকৃত এজেন্টিক অ্যাপ্লিকেশন | এজেন্ট, পারসোনা, ফাংশন, ডেটা | কোড জেনারেশন, ডেটা বিশ্লেষণ কাজ |
| Semantic Kernel | মানবসদৃশ টেক্সট বিষয়বস্তু বোঝা এবং তৈরি করা | এজেন্ট, মডুলার কম্পোনেন্ট, সহযোগিতা | প্রাকৃতিক ভাষা বোঝা, বিষয়বস্তু তৈরি |
| Azure AI Agent Service | নমনীয় মডেল, এন্টারপ্রাইজ নিরাপত্তা, কোড জেনারেশন, টুল কলিং | মডুলারিটি, সহযোগিতা, প্রক্রিয়া অর্কেস্ট্রেশন | নিরাপদ, স্কেলযোগ্য এবং নমনীয় AI এজেন্ট মোতায়েন |

প্রত্যেকটি ফ্রেমওয়ার্কের জন্য আদর্শ ব্যবহার ক্ষেত্র কী?

## আমি কি আমার বিদ্যমান Azure ইকোসিস্টেম টুলগুলো সরাসরি ইন্টিগ্রেট করতে পারি, নাকি আমাকে স্ট্যান্ডঅ্যালোন সমাধান দরকার?

উত্তর হলো হ্যাঁ, আপনি আপনার বিদ্যমান Azure ইকোসিস্টেম টুলগুলো সরাসরি Azure AI Agent Service-এর সাথে ইন্টিগ্রেট করতে পারেন, বিশেষত কারণ এটি অন্যান্য Azure পরিষেবার সাথে নির্বিঘ্নে কাজ করার জন্য তৈরি করা হয়েছে। উদাহরণস্বরূপ, আপনি Bing, Azure AI Search এবং Azure Functions ইন্টিগ্রেট করতে পারেন। এছাড়াও Azure AI Foundry-এর সাথে গভীর ইন্টিগ্রেশন রয়েছে।

AutoGen এবং Semantic Kernel-এর জন্য, আপনি Azure পরিষেবাগুলোর সাথে ইন্টিগ্রেট করতে পারেন, তবে এটি আপনার কোড থেকে Azure পরিষেবাগুলো কল করার প্রয়োজন হতে পারে। আরেকটি উপায় হলো Azure SDK ব্যবহার করে আপনার এজেন্ট থেকে Azure পরিষেবাগুলোর সাথে ইন্টারঅ্যাক্ট করা। এছাড়াও, যেমন উল্লেখ করা হয়েছে, আপনি AutoGen বা Semantic Kernel-এ তৈরি আপনার এজেন্টগুলোর জন্য অর্কেস্ট্রেটর হিসেবে Azure AI Agent Service ব্যবহার করতে পারেন, যা Azure ইকোসিস্টেমে সহজ অ্যাক্সেস প্রদান করবে।

### AI Agent Frameworks সম্পর্কে আরও প্রশ্ন আছে?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)-এ যোগ দিন, যেখানে আপনি অন্যান্য শিক্ষার্থীদের সাথে দেখা করতে পারবেন, অফিস আওয়ার্সে অংশ নিতে পারবেন এবং আপনার AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পেতে পারবেন।

## রেফারেন্স

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel এবং AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">AutoGen / Semantic Kernel ব্যবহার করে Azure AI Agent Service দিয়ে মাল্টি-এজেন্ট সমাধান তৈরি</a>

## পূর্ববর্তী পাঠ

[AI এজেন্ট এবং এজেন্ট ব্যবহার ক্ষেত্রের পরিচিতি](../01-intro-to-ai-agents/README.md)

## পরবর্তী পাঠ

[Agentic Design Patterns বোঝা](../03-agentic-design-patterns/README.md)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।