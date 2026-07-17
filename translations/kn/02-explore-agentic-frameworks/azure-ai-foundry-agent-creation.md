# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏಜೆಂಟ್ ಸರ್ವೀಸ್ ಅಭಿವೃದ್ಧಿ

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ, ನೀವು [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏಜೆಂಟ್ ಸರ್ವೀಸ್ ಸಾಧನಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಫ್ಲೈಟ್ ಬುಕ್ಕಿಂಗ್‌ಗೆ ಏಜೆಂಟ್ ಅನ್ನು ರಚಿಸುತ್ತೀರಿ.ಈ ಏಜೆಂಟ್ ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಹನ ನಡೆಸಿ, ಪ್ರಯಾಣಗಳ ಕುರಿತು ಮಾಹಿತಿಯನ್ನು ನೀಡಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ.

## ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

ಈ ವ್ಯಾಯಾಮವನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು, ನಿಮಗೆ ಕೆಳಗಿನವುಗಳು ಅಗತ್ಯ:
1. ಸಕ್ರೀಯ ಚಂದಾದಾರಿಕೆಯೊಂದಿಗೆ Azure ಖಾತೆ. [ಉಚಿತ ಖಾತೆಯನ್ನು ರಚಿಸಿ](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಹಬ್ ರಚಿಸಲು ಅನುಮತಿಗಳು ಇಲ್ಲವೇ ನಿಮಗಾಗಿ ನಿರ್ಮಿಸಲಾಗಿದೆ.
    - ನಿಮ್ಮ ಪಾತ್ರ Contributor ಅಥವಾ Owner ಆಗಿದ್ದರೆ, ನೀವು ಈ ಪಾಠತಾಳಿಕೆನಡಗಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಬಹುದು.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಹಬ್ ರಚಿಸಿ

> **ಸೂಚನೆ:** ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಅನ್ನು ಮೊದಲು Azure AI Studio ಎಂದು ಕರೆಯಲಾಗುತ್ತಿತ್ತು.

1. ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಹಬ್ ರಚನೆಗಾಗಿ [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ಬ್ಲಾಗ್ ಪೋಸ್ಟ್‌ನ ಈ ಮಾರ್ಗಸೂಚಿಗಳನ್ನು ಅನುಸರಿಸಿ.
2. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸುವಾಗ, ತೋರುವ ಯಾವುದೇ ಸಲಹೆಗಳನ್ನು ಮುಚ್ಚಿ ಮತ್ತು Microsoft Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಪ್ರಾಜೆಕ್ಟ್ ಪುಟವನ್ನು ಪರಿಶೀಲಿಸಿ, ಇದು ಹೀಗಿರಬಹುದು:

    ![Microsoft Foundry Project](../../../translated_images/kn/azure-ai-foundry.88d0c35298348c2f.webp)

## ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಎಡಗೆ ಇರುವ ಪ್ಯಾನಲ್ಲಿ, **My assets** ವಿಭಾಗದಲ್ಲಿ **Models + endpoints** ಪುಟವನ್ನು ಆರಿಸಿ.
2. **Models + endpoints** ಪುಟದಲ್ಲಿ, **Model deployments** ಟ್ಯಾಬ್ನಲ್ಲಿ, **+ Deploy model** ಮೆನುನಲ್ಲಿ **Deploy base model** ಆಯ್ಕೆಮಾಡಿ.
3. ಪಟ್ಟಿಯಲ್ಲಿ `gpt-4.1-mini` ಮಾದರಿಯನ್ನು ಹುಡುಕಿ, ಆಯ್ಕೆಮಾಡಿ ಮತ್ತು ದೃಢೀಕರಿಸಿ.

    > **ಸೂಚನೆ**: TPM ಕಡಿಮೆಮಾಡುವುದು ನಿಮ್ಮ ಚಂದಾದಾರ ಈ ಕ್ವೋಟಾದ ಹೆಚ್ಚುವರಿ ಬಳಕೆಯನ್ನು ತಪ್ಪಿಸಲು ಸಹಾಯಕ.

    ![Model Deployed](../../../translated_images/kn/model-deployment.3749c53fb81e18fd.webp)

## ಏಜೆಂಟ್ ರಚಿಸಿ

ನೀವು ಈಗ ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿದ್ದೀರಿ, ಆದ್ದರಿಂದ ನೀವು ಏಜೆಂಟ್ ರಚಿಸಬಹುದು. ಏಜೆಂಟ್ ಎಂದರೆ ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಾದ ನಡೆಸಲು ಬಳಸಬಹುದಾದ ಸಂವಾದಾತ್ಮಕ AI ಮಾದರಿ.

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಎಡ ಪ್ಯಾನ್ನಲ್ಲಿ **Build & Customize** ವಿಭಾಗದಲ್ಲಿ **Agents** ಪುಟವನ್ನು ಆರಿಸಿ.
2. ಹೊಸ ಏಜೆಂಟ್ ರಚಿಸಲು **+ Create agent** ಕ್ಲಿಕ್ ಮಾಡಿ. **Agent Setup** ಡೈಯಲಾಗ್ ಬಾಕ್ಗೆ:
    - ಏಜೆಂಟ್‌ಗೆ ಹೆಸರು ನೀಡಿ, ಉದಾಹರಣೆಗೆ `FlightAgent`.
    - ನೀವು ಮೊದಲು ರಚಿಸಿದ `gpt-4.1-mini` ಮಾದರಿ ನಿಯೋಜನೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಲಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.
    - ನೀವು ಏಜೆಂಟ್ ಅನುಸರಿಸಬೇಕಾದ ಸೂಚನೆಗಳನ್ನು **Instructions** ನಲ್ಲಿ ಹೊಂದಿಸಿ. ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ:
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
> ವಿವರವಾದ ಪ್ರಾಂಪ್ಟ್ ಎದುರಾಗಿಸಲು ನೀವು [ಈ ರೆಪೊಸಿಟರಿ](https://github.com/ShivamGoyal03/RoamMind) ಪರಿಶೀಲಿಸಬಹುದು.
    
> ಜೊತೆಗೆ, ನೀವು **Knowledge Base** ಮತ್ತು **Actions** ಸೇರಿಸಿ ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಹೆಚ್ಚಿಸಿ, ಹೆಚ್ಚು ಮಾಹಿತಿ ನೀಡಲು ಮತ್ತು ಬಳಕೆದಾರ ವಿನಂತಿಗಳ ಈಡೇರಿಕೆಗಾಗಿ ಸ್ವಯಂಚಾಲಿತ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಸಾಧ್ಯ. ಈ ವ್ಯಾಯಾಮಕ್ಕಾಗಿ ನೀವು ಈ ಹಂತಗಳನ್ನು ಬಿಟ್ಟುಹೋಗಬಹುದು.
    
![Agent Setup](../../../translated_images/kn/agent-setup.9bbb8755bf5df672.webp)

3. ಹೊಸ ಬಹು-AI ಏಜೆಂಟ್ ರಚಿಸಲು, ಕೇವಲ **New Agent** ಕ್ಲಿಕ್ ಮಾಡಿ. ಹೊಸವಾಗಿ ರಚಿಸಿದ ಏಜೆಂಟ್ ನಂತರ Agents ಪುಟದಲ್ಲಿ ತೋರಿಸಲಾಗುತ್ತದೆ.


## ಏಜೆಂಟ್ ಪರೀಕ್ಷೆ ಮಾಡಿ

ಏಜೆಂಟ್ ರಚಿಸಿದ ನಂತರ, ಅದನ್ನು Microsoft Foundry ಪೋರ್ಟಲ್ ಪ್ಲೇಗ್ರೌಂಡ್‌ನಲ್ಲಿ ಬಳಕೆದಾರರು ಕೇಳುವ ಪ್ರಶ್ನೆಗಳಿಗೆ ಹೇಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುವುದನ್ನು ಪರೀಕ್ಷಿಸಬಹುದು.

1. ನಿಮ್ಮ ಏಜೆಂಟ್‌ಗೆ **Setup** ಪ್ಯಾನಿನ ಮೇಲ್ಭಾಗದಲ್ಲಿ **Try in playground** ಆಯ್ಕೆಮಾಡಿ.
2. **Playground** ಪ್ಯಾನಲ್ಲಿ ಚಾಟ್ ವಿಂಡೋದಲ್ಲಿ ಪ್ರಶ್ನೆಗಳನ್ನು ಬರೆದು ಏಜೆಂಟ್ ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲು ಸಾಧ್ಯ. ಉದಾಹರಣೆಗೆ, ನೀವು ಏಜೆಂಟ್‌ಗೆ 28ನೇ ತಾರೀಖಿನ ಸಿಯಟಲ್‌ನಿಂದ ನ್ಯೂಯಾರ್ಕ್ಗೆ ವಿಮಾನಗಳಿಗಾಗಿ ಹುಡುಕಲು ಕೇಳಬಹುದು.

    > **ಸೂಚನೆ**: ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ ಯಾವುದೇ ನೈಜ-ಕಾಲದ ಡೇಟಾ ಬಳಸಲಾಗದ ಕಾರಣ, ಏಜೆಂಟ್ ಸರಿಯಾದ ಉತ್ತರಗಳನ್ನು ನೀಡకೊಡಬಹುದು. ಉದ್ದೇಶ ಏಜೆಂಟ್ ಕೊಡುವ ಸೂಚನೆಗಳಿಗೆ ಆಧರಿಸಿ ಬಳಕೆದಾರ ಪ್ರಶ್ನೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯಿಸುವ ಸಾಮರ್ಥ್ಯವನ್ನು ಪರೀಕ್ಷಿಸುವುದು.

    ![Agent Playground](../../../translated_images/kn/agent-playground.dc146586de715010.webp)

3. ಆಯ್ಕೆಮಾಡಿ ಪರೀಕ್ಷಿಸಿದ ನಂತರ, ಹೆಚ್ಚುವರಿ ಉದ್ದೇಶಗಳು, ತರಬೇತಿ ಡೇಟಾ ಮತ್ತು ಕ್ರಿಯೆಗಳನ್ನೂ ಸೇರಿಸಿ ನೀವು ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಇನ್ನಷ್ಟು ಕಸ್ಟಮೈಜ್ ಮಾಡಬಹುದು.

## ಸಂಪನ್ಮೂಲಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ

ಏಜೆಂಟ್ ಪರೀಕ್ಷೆ ಮುಗಿಸಿದ ನಂತರ, ಹೆಚ್ಚು ವೆಚ್ಚವನ್ನು ತಪ್ಪಿಸಲು ಅದನ್ನು ಅಳಿಸಬಹುದು.
1. [Azure portal](https://portal.azure.com) ಅನ್ನು ತೆರೆಯಿರಿ ಮತ್ತು ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ ಬಳಸಿದ ಹಬ್ ಸಂಪನ್ಮೂಲಗಳು ನಿಯೋಜಿಸಲಾದ Resource Group ವಿಷಯವನ್ನು ವೀಕ್ಷಿಸಿ.
2. ಟೂಲ್‌ಬಾರ್‌ನಲ್ಲಿ **Delete resource group** ಆಯ್ಕೆಮಾಡಿ.
3. Resource Group ಹೆಸರನ್ನು ನಮೂದಿಸಿ ಮತ್ತು ನೀವು ಇದನ್ನು ಅಳಿಸಲು ಇಚ್ಛಿಸುವುದಾಗಿ ದೃಢೀಕರಿಸಿ.

## ಸಂಪನ್ಮೂಲಗಳು

- [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Getting Started with Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fundamentals of AI agents on Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->