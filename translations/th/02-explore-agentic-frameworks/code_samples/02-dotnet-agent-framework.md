# 🔍 การสำรวจ Microsoft Agent Framework - ตัวแทนพื้นฐาน (.NET)

## 📋 วัตถุประสงค์การเรียนรู้

ตัวอย่างนี้สำรวจแนวคิดพื้นฐานของ Microsoft Agent Framework ผ่านการใช้งานตัวแทนพื้นฐานใน .NET คุณจะได้เรียนรู้รูปแบบตัวแทนหลักและเข้าใจวิธีที่ตัวแทนอัจฉริยะทำงานภายใต้พื้นผิวโดยใช้ C# และระบบนิเวศ .NET

### สิ่งที่คุณจะค้นพบ

- 🏗️ **สถาปัตยกรรมตัวแทน**: การเข้าใจโครงสร้างพื้นฐานของตัวแทน AI ใน .NET  
- 🛠️ **การผสานเครื่องมือ**: วิธีที่ตัวแทนใช้ฟังก์ชันภายนอกเพื่อขยายความสามารถ  
- 💬 **การไหลของการสนทนา**: การจัดการการสนทนาหลายรอบและบริบทด้วยการจัดการเธรด  
- 🔧 **รูปแบบการกำหนดค่า**: แนวทางปฏิบัติที่ดีที่สุดสำหรับการตั้งค่าและจัดการตัวแทนใน .NET  

## 🎯 แนวคิดหลักที่ครอบคลุม

### หลักการของ Agentic Framework

- **อิสระ**: วิธีที่ตัวแทนตัดสินใจอย่างอิสระโดยใช้การนามธรรม AI ของ .NET  
- **การตอบสนอง**: การตอบสนองต่อการเปลี่ยนแปลงของสภาพแวดล้อมและข้อมูลผู้ใช้  
- **เชิงรุก**: การริเริ่มตามเป้าหมายและบริบท  
- **ความสามารถทางสังคม**: การโต้ตอบผ่านภาษาธรรมชาติกับเธรดการสนทนา  

### ส่วนประกอบทางเทคนิค

- **AIAgent**: การประสานงานหลักของตัวแทนและการจัดการการสนทนา (.NET)  
- **ฟังก์ชันเครื่องมือ**: ขยายความสามารถของตัวแทนด้วยวิธีการและแอตทริบิวต์ C#  
- **การผสาน Azure OpenAI**: ใช้ประโยชน์จากโมเดลภาษาโดยผ่าน Azure OpenAI Responses API  
- **การกำหนดค่าที่ปลอดภัย**: การจัดการจุดสิ้นสุดตามสภาพแวดล้อม  

## 🔧 เทคโนโลยีทางเทคนิค

### เทคโนโลยีหลัก

- Microsoft Agent Framework (.NET)  
- การผสาน Azure OpenAI (Responses API)  
- รูปแบบไคลเอนต์ Azure.AI.OpenAI  
- การกำหนดค่าตามสภาพแวดล้อมด้วย DotNetEnv  

### ความสามารถของตัวแทน

- ความเข้าใจและการสร้างภาษาธรรมชาติ  
- การเรียกใช้ฟังก์ชันและการใช้เครื่องมือด้วยแอตทริบิวต์ C#  
- การตอบสนองที่ตระหนักถึงบริบทด้วยเธรดการสนทนา  
- สถาปัตยกรรมที่สามารถขยายได้ด้วยรูปแบบการฉีดพึ่งพิง  

## 📚 การเปรียบเทียบ Framework

ตัวอย่างนี้แสดงวิธีการของ Microsoft Agent Framework เทียบกับเฟรมเวิร์กตัวแทนอื่น ๆ:

| คุณลักษณะ | Microsoft Agent Framework | เฟรมเวิร์กอื่น ๆ |
|---------|-------------------------|------------------|
| **การผสานรวม** | ระบบนิเวศ Microsoft โดยตรง | ความเข้ากันได้หลากหลาย |
| **ความเรียบง่าย** | API ที่สะอาดและเข้าใจง่าย | การตั้งค่าที่ซับซ้อนบ่อยครั้ง |
| **การขยายตัว** | การผสานเครื่องมือที่ง่าย | ขึ้นอยู่กับเฟรมเวิร์ก |
| **พร้อมสำหรับองค์กร** | สร้างขึ้นสำหรับการผลิต | แตกต่างตามเฟรมเวิร์ก |

## 🚀 เริ่มต้นใช้งาน

### ความต้องการเบื้องต้น

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) หรือสูงกว่า  
- บัญชี [Azure subscription](https://azure.microsoft.com/free/) ที่มีทรัพยากร Azure OpenAI และการปรับใช้โมเดล  
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — ลงชื่อเข้าใช้ด้วย `az login`  

### ตัวแปรสภาพแวดล้อมที่ต้องการ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# จากนั้นลงชื่อเข้าใช้เพื่อให้ AzureCliCredential สามารถรับโทเค็นได้
az login
```
  
```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# จากนั้นลงชื่อเข้าใช้เพื่อให้ AzureCliCredential สามารถรับโทเค็นได้
az login
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
  
ดู [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) สำหรับโค้ดฉบับสมบูรณ์

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

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
    .GetOpenAIResponseClient(deployment)
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
  
## 🎓 ประเด็นสำคัญที่ควรจดจำ

1. **สถาปัตยกรรมตัวแทน**: Microsoft Agent Framework มอบแนวทางที่สะอาดและปลอดภัยในเชิงประเภทสำหรับการสร้างตัวแทน AI ใน .NET  
2. **การผสานเครื่องมือ**: ฟังก์ชันที่ติดแอตทริบิวต์ `[Description]` จะกลายเป็นเครื่องมือที่ตัวแทนใช้ได้  
3. **บริบทการสนทนา**: การจัดการเธรดรองรับการสนทนาหลายรอบพร้อมการรับรู้บริบทเต็มรูปแบบ  
4. **การจัดการการกำหนดค่า**: ตัวแปรสภาพแวดล้อมและการจัดการข้อมูลรับรองอย่างปลอดภัยปฏิบัติตามแนวทางปฏิบัติที่ดีที่สุดของ .NET  
5. **Azure OpenAI Responses API**: ตัวแทนใช้ Azure OpenAI Responses API ผ่าน SDK ของ Azure.AI.OpenAI  

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