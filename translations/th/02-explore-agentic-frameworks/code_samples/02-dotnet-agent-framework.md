<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T12:39:58+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "th"
}
-->
# 🔍 สำรวจ Microsoft Agent Framework - Basic Agent (.NET)

## 📋 วัตถุประสงค์การเรียนรู้

ตัวอย่างนี้จะช่วยให้คุณเข้าใจแนวคิดพื้นฐานของ Microsoft Agent Framework ผ่านการสร้างตัวแทน (Agent) แบบง่ายใน .NET คุณจะได้เรียนรู้รูปแบบการทำงานของตัวแทนและเข้าใจวิธีการทำงานของตัวแทนอัจฉริยะในเบื้องหลังโดยใช้ C# และระบบนิเวศ .NET

### สิ่งที่คุณจะได้เรียนรู้

- 🏗️ **สถาปัตยกรรมตัวแทน**: เข้าใจโครงสร้างพื้นฐานของตัวแทน AI ใน .NET  
- 🛠️ **การรวมเครื่องมือ**: วิธีที่ตัวแทนใช้ฟังก์ชันภายนอกเพื่อเพิ่มความสามารถ  
- 💬 **การไหลของการสนทนา**: การจัดการการสนทนาแบบหลายรอบและบริบทด้วยการจัดการเธรด  
- 🔧 **รูปแบบการตั้งค่า**: แนวทางปฏิบัติที่ดีที่สุดสำหรับการตั้งค่าและการจัดการตัวแทนใน .NET  

## 🎯 แนวคิดสำคัญที่ครอบคลุม

### หลักการของ Agentic Framework

- **ความเป็นอิสระ**: วิธีที่ตัวแทนตัดสินใจด้วยตัวเองโดยใช้การสรุป AI ใน .NET  
- **การตอบสนอง**: การตอบสนองต่อการเปลี่ยนแปลงในสิ่งแวดล้อมและการป้อนข้อมูลจากผู้ใช้  
- **การริเริ่ม**: การดำเนินการตามเป้าหมายและบริบท  
- **ความสามารถทางสังคม**: การโต้ตอบผ่านภาษาธรรมชาติด้วยเธรดการสนทนา  

### ส่วนประกอบทางเทคนิค

- **AIAgent**: การจัดการตัวแทนหลักและการสนทนา (.NET)  
- **ฟังก์ชันเครื่องมือ**: เพิ่มความสามารถของตัวแทนด้วยวิธีการและแอตทริบิวต์ใน C#  
- **การรวม OpenAI**: ใช้โมเดลภาษาโดยผ่าน API มาตรฐานของ .NET  
- **การตั้งค่าที่ปลอดภัย**: การจัดการคีย์ API ตามสิ่งแวดล้อม  

## 🔧 เทคโนโลยีที่ใช้

### เทคโนโลยีหลัก

- Microsoft Agent Framework (.NET)  
- การรวม API ของ GitHub Models  
- รูปแบบไคลเอนต์ที่เข้ากันได้กับ OpenAI  
- การตั้งค่าตามสิ่งแวดล้อมด้วย DotNetEnv  

### ความสามารถของตัวแทน

- ความเข้าใจและการสร้างภาษาธรรมชาติ  
- การเรียกฟังก์ชันและการใช้เครื่องมือด้วยแอตทริบิวต์ใน C#  
- การตอบสนองที่คำนึงถึงบริบทด้วยเธรดการสนทนา  
- สถาปัตยกรรมที่ขยายได้ด้วยรูปแบบการฉีดพึ่งพา  

## 📚 การเปรียบเทียบ Framework

ตัวอย่างนี้แสดงให้เห็นถึงวิธีการของ Microsoft Agent Framework เมื่อเปรียบเทียบกับ Framework ตัวแทนอื่น ๆ:

| คุณสมบัติ | Microsoft Agent Framework | Framework อื่น ๆ |
|-----------|---------------------------|------------------|
| **การรวมระบบ** | ระบบนิเวศของ Microsoft โดยตรง | ความเข้ากันได้หลากหลาย |
| **ความเรียบง่าย** | API ที่สะอาดและเข้าใจง่าย | การตั้งค่าที่ซับซ้อนบ่อยครั้ง |
| **การขยายตัว** | การรวมเครื่องมือที่ง่าย | ขึ้นอยู่กับ Framework |
| **พร้อมสำหรับองค์กร** | สร้างเพื่อการใช้งานจริง | แตกต่างกันตาม Framework |

## 🚀 เริ่มต้นใช้งาน

### สิ่งที่ต้องเตรียม

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) หรือเวอร์ชันที่สูงกว่า  
- [GitHub Models API access token](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### ตัวแปรสิ่งแวดล้อมที่จำเป็น

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
  

### ตัวอย่างโค้ด

เพื่อรันตัวอย่างโค้ด,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
หรือใช้ dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
ดู [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) สำหรับโค้ดทั้งหมด  

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
  

## 🎓 สิ่งที่ควรจดจำ

1. **สถาปัตยกรรมตัวแทน**: Microsoft Agent Framework ให้วิธีการที่สะอาดและปลอดภัยในการสร้างตัวแทน AI ใน .NET  
2. **การรวมเครื่องมือ**: ฟังก์ชันที่ตกแต่งด้วยแอตทริบิวต์ `[Description]` จะกลายเป็นเครื่องมือที่ตัวแทนสามารถใช้ได้  
3. **บริบทการสนทนา**: การจัดการเธรดช่วยให้การสนทนาแบบหลายรอบมีการรับรู้บริบทอย่างเต็มที่  
4. **การจัดการการตั้งค่า**: ตัวแปรสิ่งแวดล้อมและการจัดการข้อมูลรับรองที่ปลอดภัยตามแนวทางปฏิบัติที่ดีที่สุดของ .NET  
5. **ความเข้ากันได้กับ OpenAI**: การรวม GitHub Models ทำงานได้อย่างราบรื่นผ่าน API ที่เข้ากันได้กับ OpenAI  

## 🔗 แหล่งข้อมูลเพิ่มเติม

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->