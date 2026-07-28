# 🌍 Microsoft Agent Framework (.NET)을 활용한 AI 여행 에이전트

## 📋 시나리오 개요

이 예제는 .NET용 Microsoft Agent Framework를 사용하여 지능형 여행 계획 에이전트를 구축하는 방법을 보여줍니다. 이 에이전트는 전 세계의 랜덤 목적지에 대해 개인화된 당일 여행 일정을 자동으로 생성할 수 있습니다.

### 주요 기능:

- 🎲 **랜덤 목적지 선택**: 맞춤형 도구를 사용하여 휴가지 선택
- 🗺️ **지능형 여행 계획**: 상세한 일별 여행 일정 생성
- 🔄 **실시간 스트리밍**: 즉시 및 스트리밍 응답 모두 지원
- 🛠️ **커스텀 도구 통합**: 에이전트 기능 확장 방법 시연

## 🔧 기술 아키텍처

### 핵심 기술

- **Microsoft Agent Framework**: AI 에이전트 개발을 위한 최신 .NET 구현체
- **Azure OpenAI (Responses API)**: 모델 추론에 Azure OpenAI Responses API 사용
- **Azure Identity**: `AzureCliCredential`(`az login`)를 통한 안전한 로그인
- **보안 구성**: 환경 기반 엔드포인트 관리

### 주요 구성 요소

1. **AIAgent**: 대화 흐름을 관리하는 주요 에이전트 관리자
2. **커스텀 도구**: 에이전트가 사용할 수 있는 `GetRandomDestination()` 함수
3. **Responses 클라이언트**: Azure OpenAI Responses 기반 대화 인터페이스
4. **스트리밍 지원**: 실시간 응답 생성 기능

### 통합 패턴

```mermaid
graph LR
    A[사용자 요청] --> B[AI 에이전트]
    B --> C[Azure OpenAI (응답 API)]
    B --> D[무작위 목적지 얻기 도구]
    C --> E[여행 일정표]
    D --> E
```

## 🚀 시작하기

### 필요 조건

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 이상
- Azure OpenAI 리소스와 모델 배포가 포함된 [Azure 구독](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login`으로 로그인

### 필수 환경 변수

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# 그런 다음 AzureCliCredential이 토큰을 얻을 수 있도록 로그인하세요
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# 그런 다음 AzureCliCredential가 토큰을 가져올 수 있도록 로그인합니다
az login
```

### 샘플 코드

코드를 실행하려면,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

또는 dotnet CLI를 사용하여:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

전체 코드는 [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs)를 참조하세요.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 주요 시사점

1. **에이전트 아키텍처**: Microsoft Agent Framework는 .NET에서 AI 에이전트를 구축할 수 있는 깔끔하고 타입 안전한 접근법을 제공합니다.
2. **도구 통합**: `[Description]` 특성이 지정된 함수는 에이전트가 사용할 수 있는 도구가 됩니다.
3. **구성 관리**: 환경 변수와 안전한 자격 증명 처리는 .NET 최선 사례를 따릅니다.
4. **Azure OpenAI Responses API**: 에이전트는 Azure.AI.OpenAI SDK를 통해 Azure OpenAI Responses API를 사용합니다.

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