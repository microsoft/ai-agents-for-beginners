# 🔍 สำรวจ Microsoft Agent Framework - ตัวแทนพื้นฐาน (.NET)

## 📋 วัตถุประสงค์การเรียนรู้

ตัวอย่างนี้สำรวจแนวคิดพื้นฐานของ Microsoft Agent Framework ผ่านการใช้งานตัวแทนพื้นฐานใน .NET คุณจะได้เรียนรู้รูปแบบตัวแทนหลักและเข้าใจการทำงานของตัวแทนอัจฉริยะเบื้องหลังโดยใช้ C# และระบบนิเวศ .NET

### สิ่งที่คุณจะค้นพบ

- 🏗️ **สถาปัตยกรรมตัวแทน**: ความเข้าใจโครงสร้างพื้นฐานของตัวแทน AI ใน .NET
- 🛠️ **การรวมเครื่องมือ**: วิธีที่ตัวแทนใช้ฟังก์ชันภายนอกเพื่อขยายความสามารถ  
- 💬 **การไหลของการสนทนา**: การจัดการการสนทนาแบบหลายรอบและบริบทด้วยการจัดการเธรด
- 🔧 **รูปแบบการตั้งค่า**: แนวทางปฏิบัติที่ดีที่สุดสำหรับการตั้งค่าและจัดการตัวแทนใน .NET

## 🎯 แนวคิดสำคัญที่ครอบคลุม

### หลักการของ Agentic Framework

- **เอกราช**: วิธีที่ตัวแทนตัดสินใจโดยอิสระโดยใช้การนามธรรม AI ใน .NET
- **การตอบสนอง**: การตอบสนองต่อการเปลี่ยนแปลงของสภาพแวดล้อมและป้อนข้อมูลผู้ใช้
- **ความริเริ่ม**: การริเริ่มตามเป้าหมายและบริบท
- **ความสามารถทางสังคม**: การโต้ตอบผ่านภาษาธรรมชาติกับเธรดการสนทนา

### ส่วนประกอบทางเทคนิค

- **AIAgent**: การจัดการการประสานตัวแทนหลักและการสนทนา (.NET)
- **ฟังก์ชันเครื่องมือ**: การขยายความสามารถของตัวแทนด้วยวิธีและแอตทริบิวต์ของ C#
- **การรวม Azure OpenAI**: การใช้โมเดลภาษาโดย API ตอบกลับ Azure OpenAI
- **การตั้งค่าที่ปลอดภัย**: การจัดการจุดสิ้นสุดตามสภาพแวดล้อม

## 🔧 เทคโนโลยีที่ใช้

### เทคโนโลยีหลัก

- Microsoft Agent Framework (.NET)
- การรวม Azure OpenAI (Responses API)
- รูปแบบไคลเอนต์ Azure.AI.OpenAI
- การตั้งค่าตามสภาพแวดล้อมโดยใช้ DotNetEnv

### ความสามารถของตัวแทน

- การเข้าใจและสร้างภาษาธรรมชาติ
- การเรียกฟังก์ชันและใช้งานเครื่องมือด้วยแอตทริบิวต์ C#
- การตอบสนองโดยตระหนักถึงบริบทด้วยเซสชันการสนทนา
- สถาปัตยกรรมที่ขยายได้ด้วยรูปแบบการฉีดพึ่งพา

## 📚 การเปรียบเทียบ Framework

ตัวอย่างนี้สาธิตวิธีการของ Microsoft Agent Framework เทียบกับ Framework อื่นๆ ที่เป็น agentic:

| คุณสมบัติ | Microsoft Agent Framework | Framework อื่น ๆ |
|---------|-------------------------|------------------|
| **การรวมระบบ** | ระบบนิเวศของ Microsoft โดยตรง | ความเข้ากันได้หลากหลาย |
| **ความเรียบง่าย** | API ที่สะอาดและเข้าใจง่าย | ส่วนใหญ่ตั้งค่าซับซ้อน |
| **การขยายตัว** | รวมเครื่องมือได้ง่าย | ขึ้นอยู่กับ Framework |
| **พร้อมสำหรับธุรกิจ** | สร้างสำหรับการผลิต | แตกต่างตาม Framework |

## 🚀 การเริ่มต้นใช้งาน

### สิ่งที่ต้องเตรียม

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) หรือสูงกว่า
- [Azure subscription](https://azure.microsoft.com/free/) ที่มี Azure OpenAI resource และการปรับใช้โมเดล
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — ลงชื่อเข้าใช้ด้วย `az login`

### ตัวแปรสภาพแวดล้อมที่ต้องการ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# จากนั้นลงชื่อเข้าใช้เพื่อให้ AzureCliCredential สามารถรับโทเค็นได้
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# จากนั้นลงชื่อเข้าใช้เพื่อให้ AzureCliCredential สามารถรับโทเค็นได้
az login
```

### ตัวอย่างโค้ด

ในการรันตัวอย่างโค้ด,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

หรือใช้ dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

ดู [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) สำหรับโค้ดสมบูรณ์

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.13.1

using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using Azure.AI.OpenAI;
using Azure.Identity;

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

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

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
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 ประเด็นสำคัญที่ควรรู้

1. **สถาปัตยกรรมตัวแทน**: Microsoft Agent Framework ให้แนวทางที่สะอาดและปลอดภัยแบบ type-safe ในการสร้างตัวแทน AI บน .NET
2. **การรวมเครื่องมือ**: ฟังก์ชันที่มีแอตทริบิวต์ `[Description]` จะกลายเป็นเครื่องมือที่ตัวแทนสามารถใช้งานได้
3. **บริบทการสนทนา**: การจัดการเซสชันช่วยให้สนทนาแบบหลายรอบโดยมีความรับรู้บริบทครบถ้วน
4. **การจัดการการตั้งค่า**: ตัวแปรสภาพแวดล้อมและการจัดการข้อมูลรับรองอย่างปลอดภัยตามแนวทางที่ดีที่สุดของ .NET
5. **Azure OpenAI Responses API**: ตัวแทนใช้ Azure OpenAI Responses API ผ่าน SDK Azure.AI.OpenAI

## 🔗 แหล่งข้อมูลเพิ่มเติม

- [เอกสาร Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI ใน Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->