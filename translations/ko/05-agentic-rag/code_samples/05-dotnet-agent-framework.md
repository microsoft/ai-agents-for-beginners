<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T08:59:18+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "ko"
}
-->
# 🔍 Azure AI Foundry (.NET)을 활용한 엔터프라이즈 RAG

## 📋 학습 목표

이 노트북은 Microsoft Agent Framework을 사용하여 Azure AI Foundry와 함께 엔터프라이즈급 Retrieval-Augmented Generation (RAG) 시스템을 구축하는 방법을 보여줍니다. 문서를 검색하고 정확하고 상황에 맞는 응답을 제공하며 엔터프라이즈 보안과 확장성을 갖춘 프로덕션 준비 에이전트를 만드는 방법을 배우게 됩니다.

**구축할 엔터프라이즈 RAG 기능:**
- 📚 **문서 인텔리전스**: Azure AI 서비스를 활용한 고급 문서 처리
- 🔍 **시맨틱 검색**: 엔터프라이즈 기능을 갖춘 고성능 벡터 검색
- 🛡️ **보안 통합**: 역할 기반 접근 및 데이터 보호 패턴
- 🏢 **확장 가능한 아키텍처**: 모니터링이 가능한 프로덕션 준비 RAG 시스템

## 🎯 엔터프라이즈 RAG 아키텍처

### 핵심 엔터프라이즈 구성 요소
- **Azure AI Foundry**: 보안 및 규정을 준수하는 관리형 엔터프라이즈 AI 플랫폼
- **Persistent Agents**: 대화 기록 및 컨텍스트 관리를 포함한 상태 유지 에이전트
- **Vector Store Management**: 엔터프라이즈급 문서 인덱싱 및 검색
- **Identity Integration**: Azure AD 인증 및 역할 기반 접근 제어

### .NET 엔터프라이즈 혜택
- **타입 안전성**: RAG 작업 및 데이터 구조에 대한 컴파일 타임 검증
- **비동기 성능**: 비차단 문서 처리 및 검색 작업
- **메모리 관리**: 대규모 문서 컬렉션을 위한 효율적인 리소스 활용
- **통합 패턴**: 종속성 주입을 활용한 네이티브 Azure 서비스 통합

## 🏗️ 기술 아키텍처

### 엔터프라이즈 RAG 파이프라인
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### 핵심 .NET 구성 요소
- **Azure.AI.Agents.Persistent**: 상태 지속성을 갖춘 엔터프라이즈 에이전트 관리
- **Azure.Identity**: 안전한 Azure 서비스 접근을 위한 통합 인증
- **Microsoft.Agents.AI.AzureAI**: Azure 최적화 에이전트 프레임워크 구현
- **System.Linq.Async**: 고성능 비동기 LINQ 작업

## 🔧 엔터프라이즈 기능 및 혜택

### 보안 및 규정 준수
- **Azure AD 통합**: 엔터프라이즈 아이덴티티 관리 및 인증
- **역할 기반 접근**: 문서 접근 및 작업에 대한 세분화된 권한
- **데이터 보호**: 민감한 문서에 대한 저장 및 전송 중 암호화
- **감사 로그**: 규정 준수를 위한 포괄적인 활동 추적

### 성능 및 확장성
- **연결 풀링**: 효율적인 Azure 서비스 연결 관리
- **비동기 처리**: 고처리량 시나리오를 위한 비차단 작업
- **캐싱 전략**: 자주 접근하는 문서에 대한 지능형 캐싱
- **로드 밸런싱**: 대규모 배포를 위한 분산 처리

### 관리 및 모니터링
- **상태 점검**: RAG 시스템 구성 요소에 대한 내장 모니터링
- **성능 지표**: 검색 품질 및 응답 시간에 대한 상세 분석
- **오류 처리**: 재시도 정책을 포함한 포괄적인 예외 관리
- **구성 관리**: 유효성 검사가 포함된 환경별 설정

## ⚙️ 사전 요구 사항 및 설정

**개발 환경:**
- .NET 9.0 SDK 이상
- Visual Studio 2022 또는 C# 확장이 포함된 VS Code
- Azure AI Foundry 액세스가 포함된 Azure 구독

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
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**환경 구성:**
* Azure AI Foundry 구성 (Azure CLI를 통해 자동 처리)
* 올바른 Azure 구독에 인증되었는지 확인

## 📊 엔터프라이즈 RAG 패턴

### 문서 관리 패턴
- **대량 업로드**: 대규모 문서 컬렉션의 효율적인 처리
- **증분 업데이트**: 실시간 문서 추가 및 수정
- **버전 관리**: 문서 버전 관리 및 변경 추적
- **메타데이터 관리**: 풍부한 문서 속성과 분류 체계

### 검색 및 검색 패턴
- **하이브리드 검색**: 시맨틱 및 키워드 검색을 결합하여 최적의 결과 제공
- **다면 검색**: 다차원 필터링 및 분류
- **관련성 조정**: 도메인별 요구에 맞춘 사용자 정의 점수 알고리즘
- **결과 순위**: 비즈니스 논리 통합을 통한 고급 순위 지정

### 보안 패턴
- **문서 수준 보안**: 문서별 세분화된 접근 제어
- **데이터 분류**: 자동 민감도 라벨링 및 보호
- **감사 추적**: 모든 RAG 작업에 대한 포괄적인 로깅
- **개인정보 보호**: PII 감지 및 수정 기능

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
- **암호화**: 문서 및 검색 인덱스에 대한 종단 간 암호화
- **접근 제어**: 사용자 및 그룹 권한을 위한 Azure AD 통합
- **데이터 거주지**: 규정을 준수하기 위한 지리적 데이터 위치 제어
- **백업 및 복구**: 자동화된 백업 및 재해 복구 기능

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
- **스트리밍 처리**: 메모리 문제 없이 대규모 문서 처리
- **리소스 풀링**: 고비용 리소스의 효율적인 재사용
- **가비지 컬렉션**: 최적화된 메모리 할당 패턴
- **연결 관리**: 적절한 Azure 서비스 연결 수명 주기

### 캐싱 전략
- **쿼리 캐싱**: 자주 실행되는 검색 캐싱
- **문서 캐싱**: 핫 문서에 대한 메모리 내 캐싱
- **인덱스 캐싱**: 최적화된 벡터 인덱스 캐싱
- **결과 캐싱**: 생성된 응답의 지능형 캐싱

## 📊 엔터프라이즈 사용 사례

### 지식 관리
- **기업 위키**: 회사 지식 기반에 대한 지능형 검색
- **정책 및 절차**: 자동화된 규정 준수 및 절차 안내
- **교육 자료**: 지능형 학습 및 개발 지원
- **연구 데이터베이스**: 학술 및 연구 논문 분석 시스템

### 고객 지원
- **지원 지식 기반**: 자동화된 고객 서비스 응답
- **제품 문서**: 지능형 제품 정보 검색
- **문제 해결 가이드**: 상황에 맞는 문제 해결 지원
- **FAQ 시스템**: 문서 컬렉션에서 동적 FAQ 생성

### 규정 준수
- **법률 문서 분석**: 계약 및 법률 문서 인텔리전스
- **규정 준수 모니터링**: 자동화된 규정 준수 확인
- **위험 평가**: 문서 기반 위험 분석 및 보고
- **감사 지원**: 감사용 지능형 문서 검색

## 🚀 프로덕션 배포

### 모니터링 및 관찰성
- **Application Insights**: 상세한 원격 분석 및 성능 모니터링
- **사용자 정의 지표**: 비즈니스별 KPI 추적 및 경고
- **분산 추적**: 서비스 간 요청의 종단 간 추적
- **상태 대시보드**: 실시간 시스템 상태 및 성능 시각화

### 확장성 및 신뢰성
- **자동 확장**: 부하 및 성능 지표에 따른 자동 확장
- **고가용성**: 장애 조치 기능을 갖춘 다중 지역 배포
- **로드 테스트**: 엔터프라이즈 부하 조건에서 성능 검증
- **재해 복구**: 자동화된 백업 및 복구 절차

민감한 문서를 대규모로 처리할 수 있는 엔터프라이즈급 RAG 시스템을 구축할 준비가 되셨나요? 엔터프라이즈를 위한 지능형 지식 시스템을 설계해 봅시다! 🏢📖✨

## 코드 구현

이 강의의 완전한 작동 코드 샘플은 `05-dotnet-agent-framework.cs`에 있습니다.

예제를 실행하려면:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

또는 `dotnet run`을 직접 사용하세요:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

코드는 다음을 보여줍니다:

1. **패키지 설치**: Azure AI Agents에 필요한 NuGet 패키지 설치
2. **환경 구성**: Azure AI Foundry 엔드포인트 및 모델 설정 로드
3. **문서 업로드**: RAG 처리를 위한 문서 업로드
4. **벡터 스토어 생성**: 시맨틱 검색을 위한 벡터 스토어 생성
5. **에이전트 구성**: 파일 검색 기능을 갖춘 AI 에이전트 설정
6. **쿼리 실행**: 업로드된 문서에 대한 쿼리 실행

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.