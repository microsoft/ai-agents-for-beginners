# Microsoft Foundry 에이전트 서비스 개발

이번 연습에서는 [Microsoft Foundry 포털](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)의 Microsoft Foundry 에이전트 서비스 도구를 사용하여 항공권 예약을 위한 에이전트를 만듭니다. 이 에이전트는 사용자와 상호작용하고 항공편 정보를 제공할 수 있습니다.

## 사전 조건

이 연습을 완료하려면 다음이 필요합니다.
1. 활성 구독이 있는 Azure 계정. [무료로 계정 만들기](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Microsoft Foundry 허브를 생성할 수 있는 권한이 있거나 대신 생성된 허브가 있어야 합니다.
    - 역할이 Contributor 또는 Owner인 경우 이 튜토리얼의 단계를 따라 진행할 수 있습니다.

## Microsoft Foundry 허브 만들기

> **참고:** Microsoft Foundry는 이전에 Azure AI Studio로 알려져 있었습니다.

1. Microsoft Foundry 허브를 만드는 방법에 대해서는 [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) 블로그 게시물의 지침을 따릅니다.
2. 프로젝트가 생성되면 표시되는 팁을 닫고 Microsoft Foundry 포털의 프로젝트 페이지를 검토합니다. 다음 이미지와 유사해야 합니다:

    ![Microsoft Foundry Project](../../../translated_images/ko/azure-ai-foundry.88d0c35298348c2f.webp)

## 모델 배포

1. 프로젝트 왼쪽 창에서 **내 자산** 섹션의 **모델 + 엔드포인트** 페이지를 선택합니다.
2. **모델 + 엔드포인트** 페이지의 **모델 배포** 탭에서 **+ 모델 배포** 메뉴를 클릭하고 <strong>기본 모델 배포</strong>를 선택합니다.
3. 목록에서 `gpt-5-mini` 모델을 검색한 다음 선택하고 확인합니다.

    > <strong>참고</strong>: TPM을 줄이면 사용 중인 구독에 할당된 쿼터를 과다 사용하지 않도록 할 수 있습니다.

    ![Model Deployed](../../../translated_images/ko/model-deployment.3749c53fb81e18fd.webp)

## 에이전트 생성

모델을 배포했으므로 이제 에이전트를 만들 수 있습니다. 에이전트는 사용자와 상호작용할 수 있는 대화형 AI 모델입니다.

1. 프로젝트 왼쪽 창의 **빌드 및 사용자 지정** 섹션에서 <strong>에이전트</strong> 페이지를 선택합니다.
2. <strong>+ 에이전트 생성</strong>을 클릭하여 새 에이전트를 만듭니다. **에이전트 설정** 대화 상자에서:
    - 에이전트 이름으로 `FlightAgent` 같은 이름을 입력합니다.
    - 이전에 만든 `gpt-5-mini` 모델 배포가 선택되어 있는지 확인합니다.
    - 에이전트가 따를 프롬프트에 따라 <strong>지침</strong>을 설정합니다. 예시는 다음과 같습니다:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> 자세한 프롬프트는 [이 저장소](https://github.com/ShivamGoyal03/RoamMind)를 참고하세요.
    
> 또한, <strong>지식 베이스</strong>와 <strong>작업</strong>을 추가하여 에이전트가 사용자 요청에 따라 더 많은 정보 제공과 자동화 작업을 할 수 있게 할 수 있습니다. 이번 연습에서는 이 단계를 건너뛸 수 있습니다.
    
![Agent Setup](../../../translated_images/ko/agent-setup.9bbb8755bf5df672.webp)

3. 새 다중 AI 에이전트를 만들려면 단순히 <strong>새 에이전트</strong>를 클릭하면 됩니다. 새로 생성된 에이전트가 에이전트 페이지에 표시됩니다.


## 에이전트 테스트

에이전트를 만든 후 Microsoft Foundry 포털의 플레이그라운드에서 사용자 쿼리에 어떻게 응답하는지 테스트할 수 있습니다.

1. 에이전트의 <strong>설정</strong> 창 상단에서 <strong>플레이그라운드에서 시도</strong>를 선택합니다.
2. <strong>플레이그라운드</strong> 창에서 채팅창에 쿼리를 입력하여 에이전트와 상호작용할 수 있습니다. 예를 들어, 28일에 시애틀에서 뉴욕으로 가는 항공편을 검색하도록 요청할 수 있습니다.

    > <strong>참고</strong>: 이 연습에서는 실시간 데이터가 사용되지 않아 에이전트가 정확한 답변을 제공하지 않을 수 있습니다. 이 연습은 주어진 지침에 따라 사용자의 쿼리를 이해하고 응답하는 능력을 테스트하는 목적입니다.

    ![Agent Playground](../../../translated_images/ko/agent-playground.dc146586de715010.webp)

3. 에이전트를 테스트한 후에는 더 많은 인텐트, 학습 데이터, 작업을 추가하여 기능을 향상시킬 수 있습니다.

## 리소스 정리

에이전트 테스트를 마친 후 추가 비용 발생을 막기 위해 에이전트를 삭제할 수 있습니다.
1. [Azure 포털](https://portal.azure.com)을 열고 이 연습에서 사용한 허브 리소스가 배포된 리소스 그룹 내용을 봅니다.
2. 도구 모음에서 <strong>리소스 그룹 삭제</strong>를 선택합니다.
3. 리소스 그룹 이름을 입력하고 삭제를 확인합니다.

## 리소스

- [Microsoft Foundry 문서](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 포털](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 시작하기](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure의 AI 에이전트 기초](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->