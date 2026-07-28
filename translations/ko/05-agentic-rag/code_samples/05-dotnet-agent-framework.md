# 🔍 Microsoft Foundry (.NET)를 이용한 엔터프라이즈 RAG

## 📋 학습 목표

이 노트북에서는 Microsoft Foundry와 .NET의 Microsoft Agent Framework를 사용하여 엔터프라이즈급 Retrieval-Augmented Generation(RAG) 시스템을 구축하는 방법을 보여줍니다. 문서를 검색하고 엔터프라이즈 보안 및 확장성과 함께 정확하고 컨텍스트에 맞는 응답을 제공하는 생산 준비 완료 에이전트를 만드는 방법을 배우게 됩니다.

**구축할 엔터프라이즈 RAG 기능:**
- 📚 **문서 인텔리전스**: Azure AI 서비스를 활용한 고급 문서 처리
- 🔍 **시맨틱 검색**: 엔터프라이즈 기능을 갖춘 고성능 벡터 검색
- 🛡️ **보안 통합**: 역할 기반 액세스 및 데이터 보호 패턴
- 🏢 **확장 가능한 아키텍처**: 모니터링 기능이 포함된 생산 준비 완료 RAG 시스템

## 🎯 엔터프라이즈 RAG 아키텍처

### 핵심 엔터프라이즈 구성요소
- **Microsoft Foundry**: 보안 및 규정 준수를 갖춘 관리형 엔터프라이즈 AI 플랫폼
- **지속 상태 에이전트**: 대화 기록 및 컨텍스트 관리를 갖춘 상태 저장 에이전트
- **벡터 저장소 관리**: 엔터프라이즈급 문서 색인화 및 검색
- **아이덴티티 통합**: Azure AD 인증 및 역할 기반 액세스 제어

### .NET 엔터프라이즈 이점
- **타입 안전성**: RAG 작업 및 데이터 구조에 대한 컴파일 타임 검증
- **비동기 성능**: 문서 처리 및 검색 작업의 논블로킹 처리
- **메모리 관리**: 대규모 문서 컬렉션에 대한 효율적인 자원 활용
- **통합 패턴**: 종속성 주입과 함께 네이티브 Azure 서비스 통합

## 🏗️ 기술 아키텍처

### 엔터프라이즈 RAG 파이프라인
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### 핵심 .NET 구성요소
- **Azure.AI.Agents.Persistent**: 상태 지속성을 갖춘 엔터프라이즈 에이전트 관리
- **Azure.Identity**: 보안 Azure 서비스 액세스를 위한 통합 인증
- **Microsoft.Agents.AI.AzureAI**: Azure 최적화 에이전트 프레임워크 구현
- **System.Linq.Async**: 고성능 비동기 LINQ 연산

## 🔧 엔터프라이즈 기능 및 이점

### 보안 및 컴플라이언스
- **Azure AD 통합**: 엔터프라이즈 아이덴티티 관리 및 인증
- **역할 기반 액세스**: 문서 액세스 및 작업에 대한 세분화된 권한
- **데이터 보호**: 민감한 문서에 대한 저장 및 전송 중 암호화
- **감사 로깅**: 규정 준수 요구사항을 위한 포괄적 활동 추적

### 성능 및 확장성
- **연결 풀링**: 효율적인 Azure 서비스 연결 관리
- **비동기 처리**: 고처리량 시나리오를 위한 논블로킹 작업
- **캐싱 전략**: 자주 액세스하는 문서에 대한 지능형 캐싱
- **로드 밸런싱**: 대규모 배포를 위한 분산 처리

### 관리 및 모니터링
- **헬스 체크**: RAG 시스템 구성요소에 대한 내장 모니터링
- **성능 지표**: 검색 품질 및 응답 시간에 대한 상세 분석
- **오류 처리**: 재시도 정책이 포함된 포괄적 예외 관리
- **구성 관리**: 환경별 설정 및 검증

## ⚙️ 필수 조건 및 설정

**개발 환경:**
- .NET 9.0 SDK 이상
- Visual Studio 2022 또는 C# 확장 기능이 있는 VS Code
- Microsoft Foundry 액세스가 포함된 Azure 구독

**필요한 NuGet 패키지:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure 인증 설정:**
```bash
# Azure CLI를 설치하고 인증합니다
az login
az account set --subscription "your-subscription-id"
```

**환경 구성:**
* Microsoft Foundry 구성(자동으로 Azure CLI 통해 처리)
* 올바른 Azure 구독에 인증되어 있는지 확인

## 📊 엔터프라이즈 RAG 패턴

### 문서 관리 패턴
- **대량 업로드**: 대규모 문서 컬렉션의 효율적 처리
- **증분 업데이트**: 실시간 문서 추가 및 수정
- **버전 관리**: 문서 버전 및 변경 사항 추적
- **메타데이터 관리**: 풍부한 문서 속성 및 분류 체계

### 검색 및 검색 패턴
- **하이브리드 검색**: 최적 결과를 위한 시맨틱 및 키워드 검색 결합
- **다차원 검색**: 다차원 필터링 및 분류
- **관련성 튜닝**: 도메인별 맞춤 점수 알고리즘
- **결과 랭킹**: 비즈니스 로직 통합을 통한 고급 랭킹

### 보안 패턴
- **문서 수준 보안**: 문서별 세분화된 접근 제어
- **데이터 분류**: 자동 민감도 라벨링 및 보호
- **감사 기록**: 모든 RAG 작업에 대한 포괄적 로깅
- **개인정보 보호**: PII 탐지 및 가림 처리 기능

## 🔒 엔터프라이즈 보안 기능

### 인증 및 권한 부여
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### 데이터 보호
- <strong>암호화</strong>: 문서 및 검색 인덱스에 대한 종단 간 암호화
- **액세스 제어**: 사용자 및 그룹 권한을 위한 Azure AD 통합
- **데이터 거주지**: 규정 준수를 위한 지리적 데이터 위치 제어
- **백업 및 복구**: 자동 백업 및 재해 복구 기능

## 📈 성능 최적화

### 비동기 처리 패턴
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### 메모리 관리
- **스트리밍 처리**: 메모리 문제 없이 대용량 문서 처리
- **자원 풀링**: 비용이 많이 드는 자원의 효율적 재사용
- **가비지 컬렉션**: 최적화된 메모리 할당 패턴
- **연결 관리**: 적절한 Azure 서비스 연결 수명 주기

### 캐싱 전략
- **쿼리 캐싱**: 자주 실행되는 검색 캐싱
- **문서 캐싱**: 자주 사용되는 문서에 대한 인메모리 캐싱
- **인덱스 캐싱**: 최적화된 벡터 인덱스 캐싱
- **결과 캐싱**: 생성된 응답의 지능형 캐싱

## 📊 엔터프라이즈 사용 사례

### 지식 관리
- **사내 위키**: 회사 지식 기반에 대한 지능형 검색
- **정책 및 절차**: 자동화된 규정 준수 및 절차 안내
- **교육 자료**: 지능형 학습 및 개발 지원
- **연구 데이터베이스**: 학술 및 연구 논문 분석 시스템

### 고객 지원
- **지원 지식 베이스**: 자동화된 고객 서비스 응답
- **제품 문서**: 지능형 제품 정보 검색
- **문제 해결 가이드**: 컨텍스트 기반 문제 해결 지원
- **FAQ 시스템**: 문서 컬렉션에서 동적 FAQ 생성

### 규제 준수
- **법률 문서 분석**: 계약서 및 법률 문서 인텔리전스
- **컴플라이언스 모니터링**: 자동화된 규제 준수 검사
- **위험 평가**: 문서 기반 위험 분석 및 보고
- **감사 지원**: 감사를 위한 지능형 문서 검색

## 🚀 프로덕션 배포

### 모니터링 및 가시성
- **Application Insights**: 상세한 텔레메트리 및 성능 모니터링
- **사용자 지정 메트릭**: 비즈니스별 KPI 추적 및 경고
- **분산 추적**: 서비스 간 종단 간 요청 추적
- **헬스 대시보드**: 실시간 시스템 상태 및 성능 시각화

### 확장성 및 신뢰성
- **자동 확장**: 부하 및 성능 지표에 따른 자동 확장
- <strong>고가용성</strong>: 페일오버 기능이 포함된 다중 지역 배포
- **부하 테스트**: 엔터프라이즈 부하 조건에서 성능 검증
- **재해 복구**: 자동 백업 및 복구 절차

대규모 민감 문서를 처리할 수 있는 엔터프라이즈급 RAG 시스템 구축할 준비가 되셨나요? 지능형 엔터프라이즈 지식 시스템을 설계해 봅시다! 🏢📖✨

## 코드 구현

이 수업의 전체 동작 코드 샘플은 `05-dotnet-agent-framework.cs`에 있습니다.

예제를 실행하려면:

```bash
# 스크립트를 실행 가능하게 만듭니다 (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# .NET 단일 파일 앱을 실행합니다
./05-dotnet-agent-framework.cs
```

또는 `dotnet run`을 직접 사용:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

이 코드는 다음을 시연합니다:

1. **패키지 설치**: Azure AI Agents에 필요한 NuGet 패키지 설치
2. **환경 구성**: Microsoft Foundry 엔드포인트 및 모델 설정 로드
3. **문서 업로드**: RAG 처리용 문서 업로드
4. **벡터 저장소 생성**: 시맨틱 검색용 벡터 저장소 생성
5. **에이전트 구성**: 파일 검색 기능을 갖춘 AI 에이전트 설정
6. **쿼리 실행**: 업로드된 문서에 대한 쿼리 실행

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->