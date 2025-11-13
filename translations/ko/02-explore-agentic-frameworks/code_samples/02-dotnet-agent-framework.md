<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:36:20+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ko"
}
-->
# 🔍 Microsoft Agent Framework 탐구 - 기본 에이전트 (.NET)

## 📋 학습 목표

이 예제는 .NET에서 기본 에이전트 구현을 통해 Microsoft Agent Framework의 기본 개념을 탐구합니다. C#과 .NET 생태계를 사용하여 지능형 에이전트가 내부적으로 어떻게 작동하는지 이해하고, 핵심 에이전트 패턴을 배울 수 있습니다.

### 학습 내용

- 🏗️ **에이전트 아키텍처**: .NET에서 AI 에이전트의 기본 구조 이해  
- 🛠️ **도구 통합**: 에이전트가 외부 기능을 사용하여 기능을 확장하는 방법  
- 💬 **대화 흐름**: 스레드 관리를 통해 다중 턴 대화와 컨텍스트 관리  
- 🔧 **구성 패턴**: .NET에서 에이전트 설정 및 관리에 대한 모범 사례  

## 🎯 주요 개념

### 에이전트 프레임워크 원칙

- **자율성**: .NET AI 추상화를 사용하여 에이전트가 독립적으로 결정을 내리는 방법  
- **반응성**: 환경 변화와 사용자 입력에 반응하는 능력  
- **능동성**: 목표와 컨텍스트를 기반으로 주도적으로 행동  
- **사회적 능력**: 대화 스레드를 통해 자연어로 상호작용  

### 기술 구성 요소

- **AIAgent**: 핵심 에이전트 오케스트레이션 및 대화 관리 (.NET)  
- **도구 함수**: C# 메서드와 속성을 사용하여 에이전트 기능 확장  
- **OpenAI 통합**: 표준화된 .NET API를 통해 언어 모델 활용  
- **보안 구성**: 환경 기반 API 키 관리  

## 🔧 기술 스택

### 핵심 기술

- Microsoft Agent Framework (.NET)  
- GitHub Models API 통합  
- OpenAI 호환 클라이언트 패턴  
- DotNetEnv를 사용한 환경 기반 구성  

### 에이전트 기능

- 자연어 이해 및 생성  
- C# 속성을 사용한 함수 호출 및 도구 사용  
- 대화 스레드를 통한 컨텍스트 인식 응답  
- 종속성 주입 패턴을 통한 확장 가능한 아키텍처  

## 📚 프레임워크 비교

이 예제는 Microsoft Agent Framework 접근 방식을 다른 에이전트 프레임워크와 비교합니다:

| 기능 | Microsoft Agent Framework | 기타 프레임워크 |
|------|---------------------------|----------------|
| **통합성** | Microsoft 생태계에 최적화 | 호환성 다양 |
| **단순성** | 간결하고 직관적인 API | 종종 복잡한 설정 |
| **확장성** | 도구 통합 용이 | 프레임워크 의존적 |
| **엔터프라이즈 준비** | 프로덕션 환경에 적합 | 프레임워크에 따라 다름 |

## 🚀 시작하기

### 사전 요구 사항

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 이상  
- [GitHub Models API 액세스 토큰](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### 필요한 환경 변수

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
  

### 샘플 코드

코드 예제를 실행하려면,  

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
또는 dotnet CLI를 사용하여:  

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
전체 코드는 [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs)에서 확인할 수 있습니다.  

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
  

## 🎓 주요 요점

1. **에이전트 아키텍처**: Microsoft Agent Framework는 .NET에서 AI 에이전트를 구축하기 위한 간결하고 타입 안전한 접근 방식을 제공합니다.  
2. **도구 통합**: `[Description]` 속성으로 장식된 함수는 에이전트의 사용 가능한 도구가 됩니다.  
3. **대화 컨텍스트**: 스레드 관리를 통해 다중 턴 대화에서 완전한 컨텍스트 인식을 제공합니다.  
4. **구성 관리**: 환경 변수와 보안 자격 증명 처리는 .NET 모범 사례를 따릅니다.  
5. **OpenAI 호환성**: GitHub Models 통합은 OpenAI 호환 API를 통해 원활하게 작동합니다.  

## 🔗 추가 자료

- [Microsoft Agent Framework 문서](https://learn.microsoft.com/agent-framework)  
- [GitHub Models 마켓플레이스](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET 단일 파일 앱](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->