# AI 에이전트 초보자용 - 강의

![AI Agents for Beginners](../../translated_images/ko/repo-thumbnailv3.917487e234b90100.webp)

## AI 에이전트 개발을 시작하는 데 필요한 모든 것을 가르치는 강의

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 다국어 지원

#### GitHub 액션을 통해 지원 (자동화 및 항상 최신 상태 유지)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](./README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **로컬 클론을 선호하시나요?**
>
> 이 저장소에는 50개 이상의 언어 번역이 포함되어 있어 다운로드 크기가 크게 증가합니다. 번역 없이 클론하려면 스패어스 체크아웃(sparse checkout)을 사용하세요:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 이 방법을 사용하면 강의를 완료하는 데 필요한 모든 것을 훨씬 빠른 다운로드로 받을 수 있습니다.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**추가 번역 언어 지원을 원하시면, [여기](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)에 목록이 있습니다.**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ATgtXmAS5D)](https://discord.com/invite/ATgtXmAS5D)


## 🌱 시작하기

이 강의는 AI 에이전트 개발의 기본을 다루는 수업들로 구성되어 있습니다. 각 수업은 자체 주제를 다루므로 원하는 곳에서 시작하세요!

이 강의는 다국어 지원을 제공합니다. [사용 가능한 언어 목록](#-multi-language-support)을 참조하세요.

생성형 AI 모델로 처음 빌드하시는 분은, 생성형 AI 초보자를 위한 [Generative AI For Beginners](https://aka.ms/genai-beginners) 강의를 확인해 보세요. 21개의 생성형 AI 빌드 레슨이 포함되어 있습니다.

코드를 실행하려면 이 저장소를 [⭐스타 표시](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)하고 [포크](https://github.com/microsoft/ai-agents-for-beginners/fork)하는 것을 잊지 마세요.

### 다른 학습자와 만나고 질문에 답을 얻으세요

AI 에이전트 개발 중 막히거나 질문이 있으면, [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)의 전용 Discord 채널에 참여하세요.

### 준비물

이 강의의 각 수업에는 코드 예제가 포함되어 있으며, code_samples 폴더에서 찾을 수 있습니다. 저장소를 [포크](https://github.com/microsoft/ai-agents-for-beginners/fork)하여 본인만의 복사본을 만들 수 있습니다.

이 연습의 코드 예제는 Microsoft Foundry Agent Service V2와 함께 Microsoft Agent Framework를 이용합니다:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure 계정 필요

이 강의는 Microsoft의 다음 AI 에이전트 프레임워크 및 서비스를 사용합니다:

- [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/agent-framework/overview/)
- [Microsoft Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

일부 코드 샘플은 대규모 컨텍스트 모델(최대 204K 토큰)을 제공하는 [MiniMax](https://platform.minimaxi.com/)와 같은 OpenAI 호환 대체 제공자도 지원합니다. 구성 세부 정보는 [Course Setup](./00-course-setup/README.md)를 확인하세요.

이 강의 코드를 실행하는 자세한 내용은 [Course Setup](./00-course-setup/README.md)을 참조하세요.

## 🙏 도움을 주시겠습니까?

제안사항이나 철자 또는 코드 오류를 찾으셨다면? [이슈를 등록](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)하거나 [풀 리퀘스트를 만드세요](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 각 수업에는 다음이 포함됩니다

- README에 있는 서면 수업과 짧은 비디오
- Microsoft Agent Framework와 Microsoft Foundry를 사용하는 Python 코드 샘플
- 학습을 계속할 수 있는 추가 자료 링크


## 🗃️ 수업

| <strong>수업</strong>                                   | **텍스트 및 코드**                                    | <strong>비디오</strong>                                                  | **추가 학습 자료**                                                                     |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI 에이전트 및 에이전트 사용 사례 소개       | [링크](./01-intro-to-ai-agents/README.md)          | [비디오](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI 에이전트 프레임워크 탐색                   | [링크](./02-explore-agentic-frameworks/README.md)  | [비디오](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI 에이전트 디자인 패턴 이해                   | [링크](./03-agentic-design-patterns/README.md)     | [비디오](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 도구 사용 디자인 패턴                          | [링크](./04-tool-use/README.md)                    | [비디오](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 에이전틱 RAG                                  | [링크](./05-agentic-rag/README.md)                 | [비디오](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 신뢰할 수 있는 AI 에이전트 구축                 | [링크](./06-building-trustworthy-agents/README.md) | [비디오](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 계획 디자인 패턴                               | [링크](./07-planning-design/README.md)             | [비디오](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 다중 에이전트 디자인 패턴                       | [링크](./08-multi-agent/README.md)                 | [비디오](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

| 메타인지 디자인 패턴                 | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 프로덕션의 AI 에이전트                      | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 에이전틱 프로토콜 사용 (MCP, A2A 및 NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI 에이전트용 컨텍스트 엔지니어링            | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 에이전틱 메모리 관리                      | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft Agent Framework 탐색                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| 컴퓨터 사용 에이전트 구축 (CUA)           | [Link](./15-browser-use/README.md)     |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| 확장 가능한 에이전트 배포                    | [Link](./16-deploying-scalable-agents/README.md) |                                                    | [Link](https://learn.microsoft.com/azure/ai-foundry/agents/overview)                   |
| 로컬 AI 에이전트 생성                     | [Link](./17-creating-local-ai-agents/README.md)  |                                                    | [Link](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)                    |
| AI 에이전트 보안                           | [Link](./18-securing-ai-agents/README.md)  |                                                            | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 다른 과정들

저희 팀은 다른 과정들도 제작합니다! 확인해 보세요:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / 에이전트
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 생성형 AI 시리즈
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)

[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 핵심 학습
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 

### 코파일럿 시리즈
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 커뮤니티 감사

Agentic RAG를 시연하는 중요한 코드 샘플을 기여해 주신 [Shivam Goyal](https://www.linkedin.com/in/shivam2003/)님께 감사드립니다.

## 기여하기

이 프로젝트는 기여와 제안을 환영합니다. 대부분의 기여는 여러분이 권리를 가지고 실제로 권리를 부여한다는 것을 선언하는
기여자 라이선스 계약서(CLA)에 동의해야 합니다.
자세한 내용은 <https://cla.opensource.microsoft.com>을 참조하십시오.

풀 리퀘스트를 제출하면 CLA 봇이 자동으로 CLA 제출 필요 여부를 판단하고 적절히 표시합니다(예: 상태 검사, 댓글).
봇의 안내에 따라 진행하면 됩니다. 모든 리포지토리에서 CLA는 한 번만 제출하면 됩니다.


이 프로젝트는 [마이크로소프트 오픈소스 행동 강령](https://opensource.microsoft.com/codeofconduct/)을 채택했습니다.
자세한 내용을 보려면 [행동 강령 FAQ](https://opensource.microsoft.com/codeofconduct/faq/)를 참조하거나,
추가 질문이나 의견이 있는 경우 [opencode@microsoft.com](mailto:opencode@microsoft.com)으로 문의하십시오.

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스와 관련된 상표 또는 로고가 포함될 수 있습니다. 마이크로소프트의
상표 또는 로고의 합법적인 사용은
[마이크로소프트 상표 및 브랜드 지침](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)을 따라야 합니다.
수정된 버전에서 마이크로소프트 상표나 로고를 사용할 때는 혼동을 유발하거나 마이크로소프트의 후원을 암시해서는 안 됩니다.
제3자 상표 또는 로고의 사용은 해당 제3자의 정책에 따릅니다.

## 도움 받기


AI 앱 개발 중 문제가 발생하거나 질문이 있으면 다음에 참여하세요:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

제품 피드백 또는 빌드 중 오류가 있는 경우 방문하십시오:


[![Microsoft Foundry 개발자 포럼](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->