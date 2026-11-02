# 🔍 Microsoft Agent Framework 탐색 - 기본 에이전트 (.NET)

## 📋 학습 목표

이 예제는 .NET에서 기본 에이전트 구현을 통해 Microsoft Agent Framework의 기본 개념을 탐구합니다. 핵심 에이전트 패턴을 배우고 C# 및 .NET 생태계를 이용한 지능형 에이전트가 내부적으로 어떻게 작동하는지 이해하게 됩니다.

### 배울 내용

- 🏗️ **에이전트 아키텍처**: .NET에서 AI 에이전트의 기본 구조 이해
- 🛠️ **도구 통합**: 에이전트가 외부 기능을 사용해 기능을 확장하는 방법  
- 💬 **대화 흐름**: 멀티 턴 대화 및 스레드 관리로 컨텍스트 관리
- 🔧 **구성 패턴**: .NET에서 에이전트 설정 및 관리 모범 사례

## 🎯 다루는 주요 개념

### 에이전틱 프레임워크 원칙

- <strong>자율성</strong>: .NET AI 추상화를 통해 에이전트가 독립적으로 결정하는 방법
- <strong>반응성</strong>: 환경 변화 및 사용자 입력에 대응
- <strong>선제성</strong>: 목표와 상황에 따라 주도적으로 행동
- **사회적 능력**: 대화 스레드를 통해 자연어로 상호작용

### 기술 구성 요소

- **AIAgent**: 핵심 에이전트 오케스트레이션 및 대화 관리 (.NET)
- **도구 함수**: C# 메서드 및 속성으로 에이전트 기능 확장
- **Azure OpenAI 통합**: Azure OpenAI Responses API를 통한 언어 모델 활용
- **보안 구성**: 환경 기반 엔드포인트 관리

## 🔧 기술 스택

### 핵심 기술

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) 통합
- Azure.AI.OpenAI 클라이언트 패턴
- DotNetEnv를 이용한 환경 기반 구성

### 에이전트 기능

- 자연어 이해 및 생성
- C# 속성을 이용한 함수 호출 및 도구 사용
- 대화 세션으로 컨텍스트 인지 응답
- 의존성 주입 패턴으로 확장 가능한 아키텍처

## 📚 프레임워크 비교

이 예제는 Microsoft Agent Framework 접근법을 다른 에이전틱 프레임워크와 비교해 보여줍니다:

| 기능 | Microsoft Agent Framework | 기타 프레임워크 |
|---------|-------------------------|------------------|
| <strong>통합성</strong> | 네이티브 Microsoft 생태계 | 호환성 다양 |
| <strong>단순성</strong> | 깔끔하고 직관적인 API | 종종 복잡한 설정 |
| <strong>확장성</strong> | 쉬운 도구 통합 | 프레임워크 의존적 |
| **기업용 준비도** | 생산 환경용으로 설계됨 | 프레임워크별 다름 |

## 🚀 시작하기

### 사전 준비사항

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 이상
- Azure OpenAI 리소스와 모델 배포가 있는 [Azure 구독](https://azure.microsoft.com/free/)
- `az login`으로 로그인하는 [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

### 필요한 환경 변수

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# 그런 다음 AzureCliCredential이 토큰을 가져올 수 있도록 로그인하세요
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# 그런 다음 AzureCliCredential이 토큰을 가져올 수 있도록 로그인하세요
az login
```

### 샘플 코드

코드를 실행하려면,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

또는 dotnet CLI를 사용하여:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

전체 코드는 [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs)를 참고하세요.

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

## 🎓 주요 요점

1. **에이전트 아키텍처**: Microsoft Agent Framework는 .NET에서 AI 에이전트를 구축하는 깔끔하고 타입 안전한 방식을 제공합니다
2. **도구 통합**: `[Description]` 속성이 붙은 함수는 에이전트의 사용 가능한 도구가 됩니다
3. **대화 컨텍스트**: 세션 관리를 통해 전체 컨텍스트 인지 멀티 턴 대화를 가능하게 합니다
4. **구성 관리**: 환경 변수와 보안 자격 증명 관리는 .NET 모범 사례를 따릅니다
5. **Azure OpenAI Responses API**: 에이전트는 Azure.AI.OpenAI SDK를 통해 Azure OpenAI Responses API를 사용합니다

## 🔗 추가 자료

- [Microsoft Agent Framework 문서](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry의 Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET 단일 파일 앱](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->