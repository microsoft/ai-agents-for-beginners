# Azure AI 에이전트 서비스 개발

In this exercise, you use the Azure AI Agent service tools in the [Microsoft Foundry 포털](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) to create a agent for Flight Booking. The agent will be able to interact with users and provide information about flights.

## 사전 요구 사항

To complete this exercise, you need the following:
1. 활성 구독이 있는 Azure 계정. [무료로 계정 만들기](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Microsoft Foundry 허브를 만들 수 있는 권한이 있거나 누군가가 대신 만들어 주어야 합니다.
    - 역할이 Contributor 또는 Owner인 경우 이 자습서의 단계를 따라 할 수 있습니다.

## Microsoft Foundry 허브 만들기

> **참고:** Microsoft Foundry는 이전에 Azure AI Studio로 알려졌습니다.

1. Microsoft Foundry 블로그 게시물의 지침([Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst))을 따라 Microsoft Foundry 허브를 만드세요.
2. 프로젝트가 생성되면 표시되는 팁을 닫고 Microsoft Foundry 포털의 프로젝트 페이지를 검토하세요. 페이지는 다음 이미지와 유사해야 합니다:

    ![Microsoft Foundry 프로젝트](../../../translated_images/ko/azure-ai-foundry.88d0c35298348c2f.webp)

## 모델 배포

1. 프로젝트의 왼쪽 창에서 **My assets** 섹션에서 **Models + endpoints** 페이지를 선택합니다.
2. **Models + endpoints** 페이지에서 **Model deployments** 탭으로 이동한 다음 **+ Deploy model** 메뉴에서 **Deploy base model**을 선택합니다.
3. 목록에서 `gpt-4o-mini` 모델을 검색한 후 선택하고 확인합니다.

    > **참고**: TPM을 줄이면 사용 중인 구독에서 사용 가능한 할당량을 과도하게 사용하는 것을 방지할 수 있습니다.

    ![모델 배포됨](../../../translated_images/ko/model-deployment.3749c53fb81e18fd.webp)

## 에이전트 만들기

모델을 배포했으므로 에이전트를 만들 수 있습니다. 에이전트는 사용자와 상호작용할 수 있는 대화형 AI 모델입니다.

1. 프로젝트의 왼쪽 창에서 **Build & Customize** 섹션의 **Agents** 페이지를 선택합니다.
2. **+ Create agent**를 클릭하여 새 에이전트를 만듭니다. **Agent Setup** 대화 상자에서:
    - 에이전트 이름을 입력합니다(예: `FlightAgent`).
    - 이전에 만든 `gpt-4o-mini` 모델 배포가 선택되어 있는지 확인합니다.
    - 에이전트가 따르도록 할 프롬프트에 따라 **Instructions**를 설정합니다. 예시는 다음과 같습니다:
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
> 자세한 프롬프트는 [이 저장소](https://github.com/ShivamGoyal03/RoamMind)에서 확인할 수 있습니다.
    
> 또한 에이전트의 기능을 확장하기 위해 **지식 베이스**와 **작업**을 추가하여 사용자 요청에 따라 더 많은 정보를 제공하고 자동화된 작업을 수행할 수 있습니다. 이 연습에서는 이 단계를 건너뛸 수 있습니다.
    
![에이전트 설정](../../../translated_images/ko/agent-setup.9bbb8755bf5df672.webp)

3. 새 멀티-AI 에이전트를 만들려면 **New Agent**를 클릭하세요. 생성된 에이전트가 Agents 페이지에 표시됩니다.


## 에이전트 테스트

에이전트를 만든 후 Microsoft Foundry 포털의 플레이그라운드에서 사용자 쿼리에 어떻게 응답하는지 테스트할 수 있습니다.

1. 에이전트의 **Setup** 창 상단에서 **Try in playground**를 선택합니다.
2. **Playground** 창에서 채팅 창에 쿼리를 입력하여 에이전트와 상호작용할 수 있습니다. 예를 들어, 에이전트에게 Seattle에서 뉴욕(New York)으로 가는 28일 항공편을 검색해 달라고 요청할 수 있습니다.

    > **참고**: 이 연습에서는 실시간 데이터가 사용되지 않으므로 에이전트가 정확한 응답을 제공하지 않을 수 있습니다. 목적은 제공된 지침을 기반으로 사용자 쿼리를 이해하고 응답하는 에이전트의 능력을 테스트하는 것입니다.

    ![에이전트 플레이그라운드](../../../translated_images/ko/agent-playground.dc146586de715010.webp)

3. 에이전트를 테스트한 후 더 많은 인텐트, 학습 데이터 및 작업을 추가하여 기능을 향상시킬 수 있습니다.

## 리소스 정리

에이전트 테스트를 마친 후 추가 비용이 발생하지 않도록 에이전트를 삭제할 수 있습니다.
1. [Azure portal](https://portal.azure.com)을 열고 이 연습에서 사용한 허브 리소스를 배포한 리소스 그룹의 내용을 확인합니다.
2. 도구 모음에서 **Delete resource group**을 선택합니다.
3. 리소스 그룹 이름을 입력하고 삭제 여부를 확인합니다.

## 리소스

- [Microsoft Foundry 문서](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 포털](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Studio 시작하기](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure의 AI 에이전트 기초](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
면책사항:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원문이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
