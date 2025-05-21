<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-05-21T09:33:18+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ko"
}
-->
# Lesson 11: Model Context Protocol (MCP) 통합

## Model Context Protocol (MCP) 소개

Model Context Protocol(MCP)은 AI 모델과 클라이언트 애플리케이션 간 상호작용을 표준화하기 위해 고안된 최신 프레임워크입니다. MCP는 AI 모델과 이를 사용하는 애플리케이션 사이의 다리 역할을 하며, 모델 구현 방식에 상관없이 일관된 인터페이스를 제공합니다.

MCP의 주요 특징:

- **표준화된 통신**: 애플리케이션과 AI 모델 간 공통 언어를 구축
- **향상된 컨텍스트 관리**: AI 모델에 컨텍스트 정보를 효율적으로 전달 가능
- **크로스 플랫폼 호환성**: C#, Java, JavaScript, Python, TypeScript 등 다양한 프로그래밍 언어 지원
- **원활한 통합**: 개발자가 다양한 AI 모델을 애플리케이션에 쉽게 통합할 수 있도록 지원

MCP는 AI 에이전트 개발에 특히 유용하며, 통합된 프로토콜을 통해 여러 시스템과 데이터 소스와 상호작용할 수 있게 해 에이전트를 더욱 유연하고 강력하게 만듭니다.

## 학습 목표
- MCP가 무엇이며 AI 에이전트 개발에서 어떤 역할을 하는지 이해하기
- GitHub 통합을 위한 MCP 서버 설정 및 구성
- MCP 도구를 활용한 다중 에이전트 시스템 구축
- Azure Cognitive Search를 활용한 RAG(Retrieval Augmented Generation) 구현

## 사전 준비 사항
- Python 3.8 이상
- Node.js 14 이상
- Azure 구독
- GitHub 계정
- Semantic Kernel에 대한 기본 이해

## 설정 안내

1. **환경 설정**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure 서비스 구성**
   - Azure Cognitive Search 리소스 생성
   - Azure OpenAI 서비스 설정
   - `.env` 파일에 환경 변수 구성

3. **MCP 서버 설정**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## 프로젝트 구조

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## 핵심 구성 요소

### 1. 다중 에이전트 시스템
- GitHub Agent: 저장소 분석
- Hackathon Agent: 프로젝트 추천
- Events Agent: 기술 이벤트 제안

### 2. Azure 통합
- 이벤트 인덱싱을 위한 Cognitive Search
- 에이전트 인텔리전스를 위한 Azure OpenAI
- RAG 패턴 구현

### 3. MCP 도구
- GitHub 저장소 분석
- 코드 검사
- 메타데이터 추출

## 코드 설명

샘플에서는 다음을 보여줍니다:
1. MCP 서버 통합
2. 다중 에이전트 조율
3. Azure Cognitive Search 통합
4. RAG 패턴 구현

주요 기능:
- 실시간 GitHub 저장소 분석
- 지능형 프로젝트 추천
- Azure Search를 활용한 이벤트 매칭
- Chainlit을 통한 스트리밍 응답

## 샘플 실행 방법

자세한 설정 방법과 추가 정보는 [Github MCP Server Example README](./code_samples/github-mcp/README.md)를 참고하세요.

1. MCP 서버 시작:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. 애플리케이션 실행:
   ```bash
   chainlit run app.py -w
   ```

3. 통합 테스트:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## 문제 해결

자주 발생하는 문제와 해결 방법:
1. MCP 연결 문제
   - 서버가 실행 중인지 확인
   - 포트 사용 가능 여부 점검
   - GitHub 토큰 확인

2. Azure Search 문제
   - 연결 문자열 유효성 검사
   - 인덱스 존재 여부 확인
   - 문서 업로드 확인

## 다음 단계
- 추가 MCP 도구 탐색
- 커스텀 에이전트 구현
- RAG 기능 강화
- 이벤트 소스 추가

## 참고 자료
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.