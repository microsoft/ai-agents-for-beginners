<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T07:58:15+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ko"
}
-->
# 11강: 모델 컨텍스트 프로토콜(MCP) 통합

## 모델 컨텍스트 프로토콜(MCP) 소개

모델 컨텍스트 프로토콜(MCP)은 AI 모델과 클라이언트 애플리케이션 간의 상호작용을 표준화하기 위해 설계된 최첨단 프레임워크입니다. MCP는 AI 모델과 이를 사용하는 애플리케이션 간의 다리 역할을 하며, 기본 모델 구현에 상관없이 일관된 인터페이스를 제공합니다.

MCP의 주요 특징:

- **표준화된 통신**: MCP는 애플리케이션이 AI 모델과 소통할 수 있는 공통 언어를 제공합니다.
- **향상된 컨텍스트 관리**: AI 모델에 컨텍스트 정보를 효율적으로 전달할 수 있습니다.
- **크로스 플랫폼 호환성**: C#, Java, JavaScript, Python, TypeScript 등 다양한 프로그래밍 언어에서 작동합니다.
- **손쉬운 통합**: 개발자가 다양한 AI 모델을 애플리케이션에 쉽게 통합할 수 있도록 지원합니다.

MCP는 특히 AI 에이전트 개발에서 매우 유용합니다. 이 프로토콜을 통해 에이전트는 다양한 시스템 및 데이터 소스와 상호작용할 수 있어 더 유연하고 강력한 에이전트를 만들 수 있습니다.

## 학습 목표
- MCP가 무엇인지, AI 에이전트 개발에서의 역할 이해
- GitHub 통합을 위한 MCP 서버 설정 및 구성
- MCP 도구를 사용한 멀티 에이전트 시스템 구축
- Azure Cognitive Search를 활용한 RAG(Retrieval Augmented Generation) 구현

## 사전 준비 사항
- Python 3.8 이상
- Node.js 14 이상
- Azure 구독
- GitHub 계정
- Semantic Kernel에 대한 기본 이해

## 설정 지침

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
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## 핵심 구성 요소

### 1. 멀티 에이전트 시스템
- GitHub 에이전트: 리포지토리 분석
- 해커톤 에이전트: 프로젝트 추천
- 이벤트 에이전트: 기술 이벤트 제안

### 2. Azure 통합
- 이벤트 색인을 위한 Cognitive Search
- 에이전트 지능을 위한 Azure OpenAI
- RAG 패턴 구현

### 3. MCP 도구
- GitHub 리포지토리 분석
- 코드 검사
- 메타데이터 추출

## 코드 설명

샘플에서는 다음을 시연합니다:
1. MCP 서버 통합
2. 멀티 에이전트 오케스트레이션
3. Azure Cognitive Search 통합
4. RAG 패턴 구현

주요 기능:
- 실시간 GitHub 리포지토리 분석
- 지능형 프로젝트 추천
- Azure Search를 활용한 이벤트 매칭
- Chainlit을 통한 스트리밍 응답

## 샘플 실행

자세한 설정 지침 및 추가 정보는 [Github MCP Server Example README](./code_samples/github-mcp/README.md)를 참조하세요.

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
   - 포트 사용 가능 여부 확인
   - GitHub 토큰 확인

2. Azure Search 문제
   - 연결 문자열 유효성 확인
   - 색인 존재 여부 확인
   - 문서 업로드 확인

## 다음 단계
- 추가 MCP 도구 탐색
- 사용자 정의 에이전트 구현
- RAG 기능 강화
- 더 많은 이벤트 소스 추가
- **고급**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents)에서 에이전트 간 통신 예제를 확인하세요.

## 리소스
- [MCP 초보자 가이드](https://aka.ms/mcp-for-beginners)  
- [MCP 문서](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search 문서](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel 가이드](https://learn.microsoft.com/semantic-kernel/)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.