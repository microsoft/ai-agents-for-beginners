# 🎯 Azure OpenAI(Responses API)와 함께하는 계획 및 설계 패턴 (.NET)

## 📋 학습 목표

이 노트북은 Azure OpenAI(Responses API)를 사용하는 .NET의 Microsoft Agent Framework를 통해 지능형 에이전트를 구축하기 위한 엔터프라이즈급 계획 및 설계 패턴을 보여줍니다. 복잡한 문제를 분해하고, 다단계 솔루션을 계획하며, .NET의 엔터프라이즈 기능으로 정교한 워크플로를 실행하는 에이전트를 만드는 방법을 배우게 됩니다.

## ⚙️ 전제 조건 및 설정

**개발 환경:**
- .NET 9.0 SDK 이상
- Visual Studio 2022 또는 C# 확장 기능이 포함된 VS Code
- Azure OpenAI 리소스와 모델 배포가 포함된 Azure 구독
- Azure CLI — `az login`으로 로그인

**필수 종속성:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**환경 구성 (.env 파일):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## 코드 실행

이 강의에는 .NET 단일 파일 앱 구현이 포함되어 있습니다. 실행 방법:

```bash
# 파일을 실행 가능하게 만드세요 (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# 애플리케이션을 실행하세요
./07-dotnet-agent-framework.cs
```

또는 dotnet run 명령을 사용하세요:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## 코드 구현

전체 구현은 `07-dotnet-agent-framework.cs`에 있으며, 다음을 보여줍니다:

- DotNetEnv를 사용한 환경 구성 로딩
- Azure OpenAI 클라이언트 구성 및 `GetChatClient().AsAIAgent()`를 사용한 AI 에이전트 생성
- JSON 직렬화가 가능한 구조화된 데이터 모델(Plan 및 TravelPlan) 정의
- JSON 스키마를 사용한 구조화된 출력의 AI 에이전트 생성
- 타입 안전 응답을 가진 계획 요청 실행

## 주요 개념

### 타입 안전 모델을 통한 구조화된 계획

에이전트는 계획 출력의 구조를 정의하기 위해 C# 클래스를 사용합니다:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### 구조화된 출력을 위한 JSON 스키마

에이전트는 TravelPlan 스키마와 일치하는 응답을 반환하도록 구성됩니다:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### 계획 에이전트 지침

에이전트는 코디네이터 역할을 하며, 특화된 서브 에이전트에 작업을 위임합니다:

- FlightBooking: 항공편 예약 및 항공편 정보 제공
- HotelBooking: 호텔 예약 및 호텔 정보 제공
- CarRental: 자동차 예약 및 자동차 렌트 정보 제공
- ActivitiesBooking: 활동 예약 및 활동 정보 제공
- DestinationInfo: 목적지 정보 제공
- DefaultAgent: 일반 요청 처리

## 예상 출력

여행 계획 요청으로 에이전트를 실행하면, 요청을 분석하고 특화된 에이전트에게 적절한 작업 할당과 함께 TravelPlan 스키마에 맞는 JSON 형식의 구조화된 계획을 생성합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->