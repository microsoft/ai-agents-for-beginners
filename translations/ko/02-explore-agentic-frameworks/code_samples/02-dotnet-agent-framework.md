<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:33:01+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ko"
}
-->
# 🔍 에이전트 프레임워크 탐구 - 기본 에이전트 (.NET)

## 📋 학습 목표

이 노트북은 .NET에서 기본 에이전트 구현을 통해 Microsoft 에이전트 프레임워크의 기본 개념을 탐구합니다. C#과 .NET 생태계를 사용하여 지능형 에이전트가 내부적으로 작동하는 방식을 이해하고 핵심 에이전트 패턴을 배울 수 있습니다.

**학습 내용:**
- 🏗️ **에이전트 아키텍처**: .NET에서 AI 에이전트의 기본 구조 이해
- 🛠️ **도구 통합**: 에이전트가 외부 기능을 사용하여 능력을 확장하는 방법  
- 💬 **대화 흐름**: 스레드 관리를 통해 다중 턴 대화와 컨텍스트 관리
- 🔧 **구성 패턴**: .NET에서 에이전트 설정 및 관리에 대한 모범 사례

## 🎯 주요 개념

### 에이전트 프레임워크 원칙
- **자율성**: .NET AI 추상화를 사용하여 에이전트가 독립적으로 결정을 내리는 방법
- **반응성**: 환경 변화와 사용자 입력에 대응하는 능력
- **능동성**: 목표와 컨텍스트를 기반으로 주도적으로 행동하는 능력
- **사회적 능력**: 대화 스레드를 통해 자연어로 상호작용

### 기술 구성 요소
- **AIAgent**: 핵심 에이전트 오케스트레이션 및 대화 관리 (.NET)
- **도구 함수**: C# 메서드와 속성을 사용하여 에이전트 기능 확장
- **OpenAI 통합**: 표준화된 .NET API를 통해 언어 모델 활용
- **환경 관리**: DotNetEnv를 사용한 안전한 구성 및 자격 증명 처리

## ⚙️ 사전 준비 및 설정

**필수 종속성:**
- .NET 9.0 SDK 이상
- Visual Studio 2022 또는 C# 확장이 포함된 VS Code

**NuGet 패키지:**
- `Microsoft.Extensions.AI` - 핵심 AI 추상화
- `Microsoft.Extensions.AI.OpenAI` - OpenAI 통합 (미리보기)
- `DotNetEnv` - 환경 변수 관리

**환경 구성 (.env 파일):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 기술 스택

**핵심 기술:**
- Microsoft 에이전트 프레임워크 (.NET)
- GitHub Models API 통합
- OpenAI 호환 클라이언트 패턴
- DotNetEnv를 사용한 환경 기반 구성

**에이전트 기능:**
- 자연어 이해 및 생성
- C# 속성을 사용한 함수 호출 및 도구 사용
- 대화 스레드를 통한 컨텍스트 인식 응답
- 종속성 주입 패턴을 사용한 확장 가능한 아키텍처

## 📚 프레임워크 비교

이 예제는 .NET에서 Microsoft 에이전트 프레임워크 접근 방식을 다른 플랫폼과 비교하여 보여줍니다:

| 기능 | .NET 에이전트 프레임워크 | Python 대안 |
|------|---------------------|-------------|
| **타입 안정성** | C#의 강력한 타입 | 동적 타입 |
| **통합** | 네이티브 .NET 생태계 | 다양한 호환성 |
| **성능** | 컴파일된 코드 성능 | 인터프리터 실행 |
| **엔터프라이즈 준비** | 프로덕션 .NET 앱에 적합 | 프레임워크에 따라 다름 |
| **도구** | Visual Studio 통합 | IDE에 따라 다름 |

## 🚀 시작하기

아래 셀을 따라가며 .NET에서 첫 번째 기본 에이전트를 구축하고 기본적인 에이전트 개념을 이해하세요!

## 📦 설치 및 설정

이 예제는 실행 가능한 .NET 단일 파일 앱으로 제공됩니다. 전체 구현은 동봉된 `02-dotnet-agent-framework.cs` 파일에서 확인할 수 있습니다.

이 예제를 실행하려면:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

또는 dotnet CLI를 사용하여:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 코드 설명

전체 구현은 다음을 포함합니다:

### 1. 패키지 종속성

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. 필수 임포트

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. 환경 구성

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. 도구 함수 정의

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
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
    
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}
```

### 5. 구성 및 클라이언트 설정

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. 에이전트 구성

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. 에이전트 초기화

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. 대화 관리

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 주요 요점

1. **에이전트 아키텍처**: Microsoft 에이전트 프레임워크는 .NET에서 AI 에이전트를 구축하기 위한 깔끔하고 타입 안정적인 접근 방식을 제공합니다.
2. **도구 통합**: `[Description]` 속성으로 장식된 함수는 에이전트가 사용할 수 있는 도구로 변환됩니다.
3. **대화 컨텍스트**: 스레드 관리는 다중 턴 대화를 전체 컨텍스트 인식으로 가능하게 합니다.
4. **구성 관리**: 환경 변수와 안전한 자격 증명 처리는 .NET 모범 사례를 따릅니다.
5. **OpenAI 호환성**: GitHub Models 통합은 OpenAI 호환 API를 통해 원활하게 작동합니다.

## 🔗 추가 자료

- [Microsoft 에이전트 프레임워크 문서](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models 마켓플레이스](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET 단일 파일 앱](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.