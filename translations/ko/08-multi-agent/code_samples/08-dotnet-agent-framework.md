# 🤝 엔터프라이즈 다중 에이전트 워크플로우 시스템 (.NET)

## 📋 학습 목표

이 노트북은 Microsoft Agent Framework을 사용하여 .NET과 GitHub 모델로 고급 엔터프라이즈급 다중 에이전트 시스템을 구축하는 방법을 보여줍니다. .NET의 엔터프라이즈 기능을 활용하여 구조화된 워크플로우를 통해 여러 전문화된 에이전트를 협력시키는 방법을 배우고, 프로덕션 준비 솔루션을 구현할 수 있습니다.

**구축할 엔터프라이즈 다중 에이전트 기능:**
- 👥 **에이전트 협업**: 컴파일 타임 유효성 검사를 통한 타입 안전한 에이전트 조정
- 🔄 **워크플로우 오케스트레이션**: .NET의 비동기 패턴을 활용한 선언적 워크플로우 정의
- 🎭 **역할 전문화**: 강력한 타입의 에이전트 성격 및 전문 분야
- 🏢 **엔터프라이즈 통합**: 모니터링 및 오류 처리를 포함한 프로덕션 준비 패턴

## ⚙️ 사전 준비 및 설정

**개발 환경:**
- .NET 9.0 SDK 이상
- Visual Studio 2022 또는 C# 확장이 포함된 VS Code
- Azure 구독 (영구 에이전트용)

**필요한 NuGet 패키지:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## 코드 샘플

이 레슨의 완전한 작동 코드가 동봉된 C# 파일에서 제공됩니다: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

샘플 실행 방법:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

또는 .NET CLI를 사용하여:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## 이 샘플이 보여주는 내용

이 다중 에이전트 워크플로우 시스템은 두 개의 전문화된 에이전트를 사용하는 호텔 여행 추천 서비스를 만듭니다:

1. **FrontDesk Agent**: 활동 및 위치 추천을 제공하는 여행 에이전트
2. **Concierge Agent**: 추천을 검토하여 진정성 있고 비관광적인 경험을 보장

에이전트는 다음과 같은 워크플로우에서 협력합니다:
- FrontDesk 에이전트가 초기 여행 요청을 받음
- Concierge 에이전트가 추천을 검토하고 개선
- 워크플로우가 실시간으로 응답을 스트리밍

## 주요 개념

### 에이전트 조정
Microsoft Agent Framework을 사용하여 컴파일 타임 유효성 검사를 통해 타입 안전한 에이전트 조정을 보여줍니다.

### 워크플로우 오케스트레이션
.NET의 비동기 패턴을 사용하여 여러 에이전트를 파이프라인으로 연결하는 선언적 워크플로우 정의를 구현합니다.

### 스트리밍 응답
비동기 열거형과 이벤트 기반 아키텍처를 사용하여 에이전트 응답을 실시간으로 스트리밍합니다.

### 엔터프라이즈 통합
다음과 같은 프로덕션 준비 패턴을 보여줍니다:
- 환경 변수 구성
- 안전한 자격 증명 관리
- 오류 처리
- 비동기 이벤트 처리

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.
