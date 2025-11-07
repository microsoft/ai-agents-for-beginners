<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:55:37+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "ko"
}
-->
# 🎯 GitHub 모델(.NET)을 활용한 계획 및 디자인 패턴

## 📋 학습 목표

이 노트북은 Microsoft Agent Framework을 사용하여 GitHub 모델과 함께 지능형 에이전트를 구축하기 위한 엔터프라이즈급 계획 및 디자인 패턴을 보여줍니다. 복잡한 문제를 분해하고, 다단계 솔루션을 계획하며, .NET의 엔터프라이즈 기능을 활용하여 정교한 워크플로를 실행하는 에이전트를 만드는 방법을 배우게 됩니다.

## ⚙️ 사전 준비 및 설정

**개발 환경:**
- .NET 9.0 SDK 이상
- Visual Studio 2022 또는 C# 확장이 포함된 VS Code
- GitHub Models API 접근 권한

**필요한 종속성:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**환경 설정 (.env 파일):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 코드 실행

이 강의는 .NET 단일 파일 앱 구현을 포함합니다. 실행하려면:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

또는 dotnet run 명령을 사용하세요:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## 코드 구현

전체 구현은 `07-dotnet-agent-framework.cs`에 있으며, 다음을 보여줍니다:

- DotNetEnv를 사용한 환경 설정 로드
- GitHub 모델을 위한 OpenAI 클라이언트 구성
- JSON 직렬화를 사용한 구조화된 데이터 모델(Plan 및 TravelPlan) 정의
- JSON 스키마를 사용하여 구조화된 출력을 생성하는 AI 에이전트 생성
- 타입 안전 응답을 사용한 계획 요청 실행

## 주요 개념

### 타입 안전 모델을 활용한 구조화된 계획

에이전트는 C# 클래스를 사용하여 계획 출력의 구조를 정의합니다:

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
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
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

에이전트는 조정자로서 역할하며, 전문화된 하위 에이전트에게 작업을 위임합니다:

- FlightBooking: 항공편 예약 및 항공편 정보 제공
- HotelBooking: 호텔 예약 및 호텔 정보 제공
- CarRental: 차량 대여 및 차량 대여 정보 제공
- ActivitiesBooking: 활동 예약 및 활동 정보 제공
- DestinationInfo: 목적지 정보 제공
- DefaultAgent: 일반 요청 처리

## 예상 출력

여행 계획 요청으로 에이전트를 실행하면, 요청을 분석하고 TravelPlan 스키마에 맞는 JSON 형식으로 구조화된 계획을 생성하며, 적절한 작업을 전문화된 에이전트에게 할당합니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.