<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T14:50:52+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "ko"
}
-->
# Github MCP 서버 예제

## 설명

이 데모는 Microsoft Reactor에서 주최한 AI Agents 해커톤을 위해 제작되었습니다.

이 도구는 사용자의 Github 저장소를 기반으로 해커톤 프로젝트를 추천하는 데 사용됩니다. 이는 다음과 같은 방식으로 이루어집니다:

1. **Github Agent** - Github MCP 서버를 사용하여 저장소와 해당 저장소에 대한 정보를 가져옵니다.
2. **Hackathon Agent** - Github Agent에서 가져온 데이터를 바탕으로 사용자가 진행한 프로젝트, 사용된 언어, AI Agents 해커톤의 프로젝트 트랙을 고려하여 창의적인 해커톤 프로젝트 아이디어를 제안합니다.
3. **Events Agent** - Hackathon Agent의 제안을 기반으로 AI Agent 해커톤 시리즈에서 관련 이벤트를 추천합니다.

## 코드 실행하기

### 환경 변수

이 데모는 Azure Open AI Service, Semantic Kernel, Github MCP Server, 그리고 Azure AI Search를 사용합니다.

이 도구들을 사용하려면 적절한 환경 변수를 설정해야 합니다:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit 서버 실행하기

MCP 서버에 연결하기 위해 이 데모는 Chainlit을 채팅 인터페이스로 사용합니다.

서버를 실행하려면 터미널에서 다음 명령어를 사용하세요:

```bash
chainlit run app.py -w
```

이 명령어를 실행하면 `localhost:8000`에서 Chainlit 서버가 시작되며, `event-descriptions.md` 콘텐츠가 Azure AI Search Index에 채워집니다.

## MCP 서버 연결하기

Github MCP 서버에 연결하려면 "Type your message here.." 채팅 상자 아래에 있는 "플러그" 아이콘을 선택하세요:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.ko.png)

그 후 "Connect an MCP"를 클릭하여 Github MCP 서버에 연결하는 명령어를 추가하세요:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]"을 실제 개인 액세스 토큰으로 대체하세요.

연결이 완료되면 플러그 아이콘 옆에 (1)이 표시되어 연결이 확인됩니다. 표시되지 않는 경우 `chainlit run app.py -w` 명령어로 Chainlit 서버를 다시 시작해 보세요.

## 데모 사용하기

해커톤 프로젝트를 추천하는 에이전트 워크플로를 시작하려면 다음과 같은 메시지를 입력할 수 있습니다:

"Github 사용자 koreyspace를 위한 해커톤 프로젝트를 추천해 주세요."

Router Agent는 요청을 분석하고 Github, Hackathon, Events 에이전트의 조합 중 어떤 것이 가장 적합한지 결정합니다. 에이전트들은 협력하여 Github 저장소 분석, 프로젝트 아이디어 생성, 관련 기술 이벤트를 기반으로 종합적인 추천을 제공합니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.