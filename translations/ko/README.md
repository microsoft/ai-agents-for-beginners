# 초보자를 위한 AI 에이전트 - 강좌

![초보자를 위한 생성형 AI](../../translated_images/ko/repo-thumbnailv2.06f4a48036fde647.webp)

## AI 에이전트 구축을 시작하는 데 필요한 모든 것을 가르치는 과정

[![GitHub 라이선스](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub 기여자](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub 이슈](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub 풀 리퀘스트](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PR 환영](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 다국어 지원

#### GitHub Action을 통해 지원 (자동화 및 항상 최신 상태)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[아랍어](../ar/README.md) | [벵골어](../bn/README.md) | [불가리아어](../bg/README.md) | [버마어 (미얀마)](../my/README.md) | [중국어(간체)](../zh-CN/README.md) | [중국어(번체, 홍콩)](../zh-HK/README.md) | [중국어(번체, 마카오)](../zh-MO/README.md) | [중국어(번체, 대만)](../zh-TW/README.md) | [크로아티아어](../hr/README.md) | [체코어](../cs/README.md) | [덴마크어](../da/README.md) | [네덜란드어](../nl/README.md) | [에스토니아어](../et/README.md) | [핀란드어](../fi/README.md) | [프랑스어](../fr/README.md) | [독일어](../de/README.md) | [그리스어](../el/README.md) | [히브리어](../he/README.md) | [힌디어](../hi/README.md) | [헝가리어](../hu/README.md) | [인도네시아어](../id/README.md) | [이탈리아어](../it/README.md) | [일본어](../ja/README.md) | [칸나다어](../kn/README.md) | [한국어](./README.md) | [리투아니아어](../lt/README.md) | [말레이어](../ms/README.md) | [말라얄람어](../ml/README.md) | [마라티어](../mr/README.md) | [네팔어](../ne/README.md) | [나이지리아 피진어](../pcm/README.md) | [노르웨이어](../no/README.md) | [페르시아어 (Farsi)](../fa/README.md) | [폴란드어](../pl/README.md) | [포르투갈어 (브라질)](../pt-BR/README.md) | [포르투갈어 (포르투갈)](../pt-PT/README.md) | [펀자브어 (구르무키)](../pa/README.md) | [루마니아어](../ro/README.md) | [러시아어](../ru/README.md) | [세르비아어 (키릴)](../sr/README.md) | [슬로바키아어](../sk/README.md) | [슬로베니아어](../sl/README.md) | [스페인어](../es/README.md) | [스와힐리어](../sw/README.md) | [스웨덴어](../sv/README.md) | [타갈로그어 (필리핀)](../tl/README.md) | [타밀어](../ta/README.md) | [텔루구어](../te/README.md) | [태국어](../th/README.md) | [터키어](../tr/README.md) | [우크라이나어](../uk/README.md) | [우르두어](../ur/README.md) | [베트남어](../vi/README.md)

> **로컬로 클론하시겠습니까?**
>
> 이 리포지토리는 50개 이상의 언어 번역을 포함하고 있어 다운로드 크기가 크게 증가합니다. 번역을 제외하고 클론하려면 sparse checkout을 사용하세요:
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
> 이렇게 하면 코스를 완료하는 데 필요한 모든 것을 훨씬 빠른 다운로드로 얻을 수 있습니다.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**추가 번역을 원하시면 지원되는 언어 목록은 [여기](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)에 나와 있습니다**

[![GitHub 관찰자](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub 포크](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub 스타](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry 디스코드](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 시작하기

이 과정은 AI 에이전트 구축의 기본을 다루는 수업들로 구성되어 있습니다. 각 수업은 자체 주제를 다루므로 원하는 곳에서 시작하세요!

이 과정은 다국어를 지원합니다. [지원 가능한 언어](../..)를 확인하세요. 

생성형 AI 모델로 처음 빌드하신다면 21개의 GenAI 빌드 수업을 포함한 [Generative AI For Beginners](https://aka.ms/genai-beginners) 과정을 확인해 보세요.

이 저장소에 [별(🌟)을 눌러주세요](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) 그리고 코드를 실행하려면 이 리포지토리를 [포크](https://github.com/microsoft/ai-agents-for-beginners/fork)하세요.

### 다른 학습자들과 만나 질문을 해결하세요

만약 빌드하는 중에 막히거나 AI 에이전트 구축에 관한 질문이 있다면, [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)의 전용 Discord 채널에 참여하세요.

### 필요 사항

이 과정의 각 수업에는 코드 예제가 포함되어 있으며, 해당 예제는 code_samples 폴더에서 찾을 수 있습니다. 자신의 복사본을 만들려면 이 리포지토리를 [포크](https://github.com/microsoft/ai-agents-for-beginners/fork)하세요.  

이 연습의 코드 예제는 Microsoft Agent Framework와 Azure AI Foundry Agent Service V2를 사용합니다:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure 계정 필요

이 과정은 Microsoft의 다음 AI 에이전트 프레임워크 및 서비스를 사용합니다:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)


코드를 실행하는 방법에 대한 자세한 내용은 [Course Setup](./00-course-setup/README.md)를 참조하세요.

## 🙏 도와주시겠어요?

제안 사항이 있거나 철자나 코드 오류를 발견하셨나요? [이슈 등록](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)하거나 [풀 리퀘스트 생성](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)하세요



## 📂 각 수업에는 다음이 포함됩니다

- README에 있는 서면 수업과 짧은 동영상
- Microsoft Agent Framework 및 Azure AI Foundry를 사용하는 Python 코드 샘플
- 학습을 계속할 수 있는 추가 자료 링크


## 🗃️ 수업

| **수업**                                   | **텍스트 및 코드**                                    | **동영상**                                                  | **추가 학습 자료**                                                                     |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI 에이전트 소개 및 에이전트 사용 사례       | [링크](./01-intro-to-ai-agents/README.md)          | [동영상](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI 에이전트 프레임워크 탐색                  | [링크](./02-explore-agentic-frameworks/README.md)  | [동영상](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI 에이전트 설계 패턴 이해                   | [링크](./03-agentic-design-patterns/README.md)     | [동영상](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 도구 사용 설계 패턴                           | [링크](./04-tool-use/README.md)                    | [동영상](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 에이전트 기반 RAG                             | [링크](./05-agentic-rag/README.md)                 | [동영상](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 신뢰할 수 있는 AI 에이전트 구축               | [링크](./06-building-trustworthy-agents/README.md) | [동영상](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 계획 수립 설계 패턴                           | [링크](./07-planning-design/README.md)             | [동영상](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 다중 에이전트 설계 패턴                       | [링크](./08-multi-agent/README.md)                 | [동영상](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 메타인지 설계 패턴                            | [링크](./09-metacognition/README.md)               | [동영상](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 프로덕션의 AI 에이전트                      | [링크](./10-ai-agents-production/README.md)        | [동영상](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 에이전틱 프로토콜 사용 (MCP, A2A 및 NLWeb) | [링크](./11-agentic-protocols/README.md)           | [동영상](https://youtu.be/X-Dh9R3Opn8)                                 | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI 에이전트를 위한 컨텍스트 엔지니어링            | [링크](./12-context-engineering/README.md)         | [동영상](https://youtu.be/F5zqRV7gEag)                                 | [링크](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| 에이전틱 메모리 관리                      | [링크](./13-agent-memory/README.md)     |      [동영상](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft 에이전트 프레임워크 탐색                         | [링크](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| 컴퓨터 사용 에이전트(CUA)           | 곧 공개 예정                            |                                                            |                                                                                        |
| 확장 가능한 에이전트 배포                    | 곧 공개 예정                            |                                                            |                                                                                        |
| 로컬 AI 에이전트 생성                     | 곧 공개 예정                               |                                                            |                                                                                        |
| AI 에이전트 보안                           | 곧 공개 예정                               |                                                            |                                                                                        |

## 🎒 기타 코스

저희 팀은 다른 코스도 제작합니다! 확인해보세요:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![초보자를 위한 LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![초보자를 위한 LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![초보자를 위한 LangChain](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![초보자를 위한 AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI 에이전트](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 생성형 AI 시리즈
[![초보자를 위한 생성형 AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 핵심 학습
[![초보자를 위한 머신러닝](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 데이터 과학](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 사이버보안](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![초보자를 위한 웹 개발](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 XR 개발](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 코파일럿 시리즈
[![AI 페어 프로그래밍용 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET용 Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot 어드벤처](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 커뮤니티에 감사

Agentic RAG를 보여주는 중요한 코드 샘플을 기여해 주신 [Shivam Goyal](https://www.linkedin.com/in/shivam2003/)에게 감사드립니다. 

## 기여

이 프로젝트는 기여와 제안을 환영합니다. 대부분의 기여는 귀하가 귀하의 기여물을 사용할 권리가 있으며 실제로 그 권리를 당사에 부여한다는 것을 선언하는 기여자 사용권 계약(CLA)에 동의해야 합니다. 자세한 내용은 <https://cla.opensource.microsoft.com>을(를) 참조하세요.

풀 리퀘스트를 제출하면 CLA 봇이 자동으로 CLA 제공 필요 여부를 판단하고 PR에 적절한 표시(예: 상태 검사, 코멘트)를 합니다. 봇이 제공하는 지침을 따르면 됩니다. 이 작업은 당사의 CLA를 사용하는 모든 저장소에서 단 한 번만 수행하면 됩니다.

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/)를 채택했습니다.
자세한 내용은 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)를 참조하거나
추가 질문이나 의견이 있으면 [opencode@microsoft.com](mailto:opencode@microsoft.com)으로 문의하세요.

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표나 로고가 포함될 수 있습니다. Microsoft 상표나 로고의 승인된 사용은 [Microsoft의 상표 및 브랜드 가이드라인](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)를 따라야 하며 이를 준수해야 합니다. 이 프로젝트의 수정된 버전에서 Microsoft 상표나 로고를 사용할 경우 혼란을 야기하거나 Microsoft의 후원을 암시해서는 안 됩니다. 타사 상표나 로고의 사용은 해당 타사의 정책을 따릅니다.

## 도움 받기


AI 앱 구축 중 막히거나 질문이 있으면 가입하세요:

[![Microsoft Foundry 디스코드](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

제품 피드백이나 빌드 중 오류가 있을 경우 방문하세요:

[![Microsoft Foundry 개발자 포럼](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
면책사항:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원문(원어) 문서를 권위 있는 원본으로 간주해야 합니다. 중요한 정보의 경우 전문 번역가에 의한 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해 또는 잘못된 해석에 대해서는 당사가 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->