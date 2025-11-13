<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:46:39+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "bn"
}
-->
# 🔍 Microsoft Agent Framework - বেসিক এজেন্ট (.NET) অন্বেষণ

## 📋 শেখার লক্ষ্যসমূহ

এই উদাহরণটি Microsoft Agent Framework-এর মৌলিক ধারণাগুলি .NET-এ একটি বেসিক এজেন্ট বাস্তবায়নের মাধ্যমে অন্বেষণ করে। আপনি এজেন্টিক প্যাটার্নের মূল বিষয়গুলি শিখবেন এবং C# এবং .NET ইকোসিস্টেম ব্যবহার করে বুদ্ধিমান এজেন্ট কীভাবে কাজ করে তা বুঝতে পারবেন।

### আপনি যা আবিষ্কার করবেন

- 🏗️ **এজেন্ট আর্কিটেকচার**: .NET-এ AI এজেন্টের মৌলিক কাঠামো বোঝা  
- 🛠️ **টুল ইন্টিগ্রেশন**: এজেন্ট কীভাবে বহিরাগত ফাংশন ব্যবহার করে সক্ষমতা বাড়ায়  
- 💬 **কথোপকথনের প্রবাহ**: থ্রেড ম্যানেজমেন্টের মাধ্যমে বহু-পর্ব কথোপকথন এবং প্রসঙ্গ পরিচালনা  
- 🔧 **কনফিগারেশন প্যাটার্ন**: .NET-এ এজেন্ট সেটআপ এবং ব্যবস্থাপনার সেরা পদ্ধতি  

## 🎯 মূল ধারণাগুলি

### এজেন্টিক ফ্রেমওয়ার্ক নীতিমালা

- **স্বায়ত্তশাসন**: .NET AI অ্যাবস্ট্রাকশন ব্যবহার করে এজেন্ট কীভাবে স্বাধীন সিদ্ধান্ত নেয়  
- **প্রতিক্রিয়াশীলতা**: পরিবেশগত পরিবর্তন এবং ব্যবহারকারীর ইনপুটের প্রতি সাড়া দেওয়া  
- **প্রোঅ্যাকটিভিটি**: লক্ষ্য এবং প্রসঙ্গের উপর ভিত্তি করে উদ্যোগ নেওয়া  
- **সামাজিক দক্ষতা**: কথোপকথনের থ্রেডের মাধ্যমে প্রাকৃতিক ভাষায় যোগাযোগ করা  

### প্রযুক্তিগত উপাদান

- **AIAgent**: মূল এজেন্ট অর্কেস্ট্রেশন এবং কথোপকথন ব্যবস্থাপনা (.NET)  
- **টুল ফাংশন**: C# মেথড এবং অ্যাট্রিবিউট ব্যবহার করে এজেন্টের সক্ষমতা বাড়ানো  
- **OpenAI ইন্টিগ্রেশন**: স্ট্যান্ডার্ডাইজড .NET API-এর মাধ্যমে ভাষার মডেল ব্যবহার করা  
- **নিরাপদ কনফিগারেশন**: পরিবেশ-ভিত্তিক API কী ব্যবস্থাপনা  

## 🔧 প্রযুক্তিগত স্ট্যাক

### মূল প্রযুক্তি

- Microsoft Agent Framework (.NET)  
- GitHub Models API ইন্টিগ্রেশন  
- OpenAI-সামঞ্জস্যপূর্ণ ক্লায়েন্ট প্যাটার্ন  
- DotNetEnv দিয়ে পরিবেশ-ভিত্তিক কনফিগারেশন  

### এজেন্টের সক্ষমতা

- প্রাকৃতিক ভাষা বোঝা এবং তৈরি করা  
- C# অ্যাট্রিবিউট দিয়ে ফাংশন কলিং এবং টুল ব্যবহার  
- কথোপকথনের থ্রেডের সাথে প্রসঙ্গ-সচেতন প্রতিক্রিয়া  
- ডিপেনডেন্সি ইনজেকশন প্যাটার্ন দিয়ে প্রসারণযোগ্য আর্কিটেকচার  

## 📚 ফ্রেমওয়ার্ক তুলনা

এই উদাহরণটি Microsoft Agent Framework পদ্ধতি অন্যান্য এজেন্টিক ফ্রেমওয়ার্কের সাথে তুলনা করে:

| বৈশিষ্ট্য | Microsoft Agent Framework | অন্যান্য ফ্রেমওয়ার্ক |
|---------|-------------------------|------------------|
| **ইন্টিগ্রেশন** | নেটিভ Microsoft ইকোসিস্টেম | বিভিন্ন সামঞ্জস্যতা |
| **সরলতা** | পরিষ্কার, সহজবোধ্য API | প্রায়ই জটিল সেটআপ |
| **প্রসারণযোগ্যতা** | সহজ টুল ইন্টিগ্রেশন | ফ্রেমওয়ার্ক-নির্ভর |
| **এন্টারপ্রাইজ প্রস্তুত** | প্রোডাকশনের জন্য তৈরি | ফ্রেমওয়ার্ক অনুযায়ী পরিবর্তনশীল |

## 🚀 শুরু করা

### প্রয়োজনীয়তা

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) বা তার বেশি  
- [GitHub Models API অ্যাক্সেস টোকেন](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### প্রয়োজনীয় পরিবেশ ভেরিয়েবল

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### নমুনা কোড

কোড উদাহরণ চালানোর জন্য,  

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
অথবা dotnet CLI ব্যবহার করে:  

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
সম্পূর্ণ কোডের জন্য দেখুন [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs)।  

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

// Tool Function: Random Destination Generator
// This static method will be available to the agent as a callable tool
// The [Description] attribute helps the AI understand when to use this function
// This demonstrates how to create custom tools for AI agents
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // List of popular vacation destinations around the world
    // The agent will randomly select from these options
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };

    // Generate random index and return selected destination
    // Uses System.Random for simple random selection
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```
  

## 🎓 মূল শিক্ষা

1. **এজেন্ট আর্কিটেকচার**: Microsoft Agent Framework .NET-এ AI এজেন্ট তৈরি করার জন্য একটি পরিষ্কার, টাইপ-সেফ পদ্ধতি প্রদান করে  
2. **টুল ইন্টিগ্রেশন**: `[Description]` অ্যাট্রিবিউট দিয়ে সজ্জিত ফাংশনগুলি এজেন্টের জন্য উপলব্ধ টুল হয়ে যায়  
3. **কথোপকথনের প্রসঙ্গ**: থ্রেড ম্যানেজমেন্ট বহু-পর্ব কথোপকথন সম্পূর্ণ প্রসঙ্গ সচেতনতা সহ সক্ষম করে  
4. **কনফিগারেশন ব্যবস্থাপনা**: পরিবেশ ভেরিয়েবল এবং নিরাপদ ক্রেডেনশিয়াল হ্যান্ডলিং .NET-এর সেরা পদ্ধতি অনুসরণ করে  
5. **OpenAI সামঞ্জস্যতা**: GitHub Models ইন্টিগ্রেশন OpenAI-সামঞ্জস্যপূর্ণ API-এর মাধ্যমে নির্বিঘ্নে কাজ করে  

## 🔗 অতিরিক্ত সম্পদ

- [Microsoft Agent Framework ডকুমেন্টেশন](https://learn.microsoft.com/agent-framework)  
- [GitHub Models মার্কেটপ্লেস](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET সিঙ্গেল ফাইল অ্যাপস](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিক অনুবাদের চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় থাকা সংস্করণটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->