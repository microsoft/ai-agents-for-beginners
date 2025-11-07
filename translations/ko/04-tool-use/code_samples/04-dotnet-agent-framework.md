<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:22:36+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "ko"
}
-->
# 🛠️ GitHub 모델을 활용한 고급 도구 사용 (.NET)

## 📋 학습 목표

이 노트북은 Microsoft Agent Framework를 사용하여 GitHub 모델과 함께 엔터프라이즈급 도구 통합 패턴을 보여줍니다. C#의 강력한 타입 지정과 .NET의 엔터프라이즈 기능을 활용하여 여러 전문화된 도구를 갖춘 고급 에이전트를 구축하는 방법을 배우게 됩니다.

**마스터할 고급 도구 기능:**
- 🔧 **다중 도구 아키텍처**: 여러 전문화된 기능을 갖춘 에이전트 구축
- 🎯 **타입 안전 도구 실행**: C#의 컴파일 타임 유효성 검사 활용
- 📊 **엔터프라이즈 도구 패턴**: 프로덕션 준비된 도구 설계 및 오류 처리
- 🔗 **도구 구성**: 복잡한 비즈니스 워크플로우를 위한 도구 결합

## 🎯 .NET 도구 아키텍처의 이점

### 엔터프라이즈 도구 기능
- **컴파일 타임 유효성 검사**: 강력한 타입 지정으로 도구 매개변수의 정확성 보장
- **의존성 주입**: IoC 컨테이너 통합을 통한 도구 관리
- **Async/Await 패턴**: 적절한 리소스 관리를 통한 비차단 도구 실행
- **구조화된 로깅**: 도구 실행 모니터링을 위한 내장 로깅 통합

### 프로덕션 준비된 패턴
- **예외 처리**: 타입 지정된 예외를 통한 포괄적인 오류 관리
- **리소스 관리**: 적절한 폐기 패턴 및 메모리 관리
- **성능 모니터링**: 내장 메트릭 및 성능 카운터
- **구성 관리**: 유효성 검사가 포함된 타입 안전 구성

## 🔧 기술 아키텍처

### 핵심 .NET 도구 구성 요소
- **Microsoft.Extensions.AI**: 통합 도구 추상화 계층
- **Microsoft.Agents.AI**: 엔터프라이즈급 도구 오케스트레이션
- **GitHub 모델 통합**: 연결 풀링이 포함된 고성능 API 클라이언트

### 도구 실행 파이프라인
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ 도구 카테고리 및 패턴

### 1. **데이터 처리 도구**
- **입력 유효성 검사**: 데이터 주석을 활용한 강력한 타입 지정
- **변환 작업**: 타입 안전 데이터 변환 및 포맷팅
- **비즈니스 로직**: 도메인별 계산 및 분석 도구
- **출력 포맷팅**: 구조화된 응답 생성

### 2. **통합 도구**
- **API 커넥터**: HttpClient를 활용한 RESTful 서비스 통합
- **데이터베이스 도구**: 데이터 액세스를 위한 Entity Framework 통합
- **파일 작업**: 유효성 검사가 포함된 안전한 파일 시스템 작업
- **외부 서비스**: 서드파티 서비스 통합 패턴

### 3. **유틸리티 도구**
- **텍스트 처리**: 문자열 조작 및 포맷팅 유틸리티
- **날짜/시간 작업**: 문화권을 고려한 날짜/시간 계산
- **수학적 도구**: 정밀 계산 및 통계 작업
- **유효성 검사 도구**: 비즈니스 규칙 유효성 검사 및 데이터 검증

## ⚙️ 사전 준비 및 설정

**개발 환경:**
- .NET 9.0 SDK 이상
- Visual Studio 2022 또는 C# 확장이 포함된 VS Code
- GitHub 모델 API 액세스

**필요한 NuGet 패키지:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**환경 구성 (.env 파일):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

.NET에서 강력하고 타입 안전한 도구 기능을 갖춘 엔터프라이즈급 에이전트를 구축할 준비가 되셨나요? 전문적인 솔루션을 설계해 봅시다! 🏢⚡

## 💻 코드 구현

전체 C# 구현은 동반 파일 `04-dotnet-agent-framework.cs`에서 확인할 수 있습니다. 이 .NET 단일 파일 앱은 다음을 보여줍니다:

- GitHub 모델 구성을 위한 환경 변수 로드
- 속성을 사용하여 C# 메서드를 활용한 사용자 정의 도구 정의
- 도구 통합을 포함한 AI 에이전트 생성
- 대화 스레드 관리
- 도구 호출을 통한 에이전트 요청 실행

예제를 실행하려면:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

또는 .NET CLI를 사용하여:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.