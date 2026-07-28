# 🤝 기업용 다중 에이전트 워크플로우 시스템 (.NET)

## 📋 학습 목표

이 노트북에서는 Azure OpenAI(Responses API)를 이용해 .NET의 Microsoft Agent Framework를 사용하여 정교한 기업용 다중 에이전트 시스템을 구축하는 방법을 보여줍니다. 여러 전문화된 에이전트들이 구조화된 워크플로우를 통해 함께 작동하도록 조율하며, .NET의 기업용 기능을 활용해 프로덕션 준비가 된 솔루션을 만드는 법을 배우게 됩니다.

**구축할 기업용 다중 에이전트 기능:**
- 👥 **에이전트 협업**: 컴파일 시 검증이 포함된 타입 안전 에이전트 조율
- 🔄 **워크플로우 오케스트레이션**: .NET의 비동기 패턴으로 선언형 워크플로우 정의
- 🎭 **역할 전문화**: 강력하게 타입화된 에이전트 성격 및 전문 영역
- 🏢 **기업 통합**: 모니터링 및 오류 처리 포함 프로덕션 준비 패턴

## ⚙️ 전제 조건 및 설정

**개발 환경:**
- .NET 9.0 SDK 이상
- Visual Studio 2022 또는 C# 확장 설치된 VS Code
- Azure 구독 (지속형 에이전트용)

**필요한 NuGet 패키지:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## 코드 샘플

이 수업의 전체 작동 코드는 함께 제공되는 C# 파일 [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)에서 확인할 수 있습니다.

샘플을 실행하려면:

```bash
# 파일을 실행 가능하게 만듭니다 (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# 샘플을 실행합니다
./08-dotnet-agent-framework.cs
```

또는 .NET CLI를 사용하여:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## 이 샘플의 시연 내용

이 다중 에이전트 워크플로우 시스템은 두 개의 전문화된 에이전트와 함께 호텔 여행 추천 서비스를 만듭니다:

1. **FrontDesk Agent**: 활동 및 위치 추천을 제공하는 여행 에이전트
2. **Concierge Agent**: 추천사항을 검토하여 진짜 같고 관광객용이 아닌 경험을 보장

에이전트들은 다음과 같이 함께 작동하는 워크플로우에 참여합니다:
- FrontDesk 에이전트가 초기 여행 요청을 받음
- Concierge 에이전트가 추천을 검토하고 다듬음
- 워크플로우가 실시간으로 응답을 스트리밍

## 주요 개념

### 에이전트 조율
이 샘플은 Microsoft Agent Framework를 사용하여 컴파일 타임 검증과 함께 타입 안전 에이전트 조율을 보여줍니다.

### 워크플로우 오케스트레이션
.NET의 비동기 패턴으로 선언형 워크플로우 정의를 사용하여 여러 에이전트를 파이프라인으로 연결합니다.

### 스트리밍 응답
비동기 열거자와 이벤트 중심 아키텍처를 사용하여 에이전트 응답의 실시간 스트리밍을 구현합니다.

### 기업 통합
다음을 포함한 프로덕션 준비 패턴을 보여줍니다:
- 환경 변수 구성
- 보안 자격 증명 관리
- 오류 처리
- 비동기 이벤트 처리

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->