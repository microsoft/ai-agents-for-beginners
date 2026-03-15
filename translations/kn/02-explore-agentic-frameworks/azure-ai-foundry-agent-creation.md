# ಅಜೂರ್ AI ಏಜೆಂಟ್ ಸೇವೆ ಅಭಿವೃದ್ಧಿ

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ, ನೀವು [Microsoft Foundry ಪೋರ್ಟಲ್](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ಅಜೂರ್ AI ಏಜೆಂಟ್ ಸೇವೆ ಸಾಧನಗಳನ್ನು ಬಳಸಿಕೊಂಡು ವಿಮಾನ ಬುಕ್ಕಿಂಗ್‌ಗೆ ಏಜೆಂಟ್ ರಚಿಸುವುದು. ಏಜೆಂಟ್ ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಮತ್ತು ವಿಮಾನಗಳ ಕುರಿತು ಮಾಹಿತಿ ನೀಡಲು ಸಾಮರ್ಥ್ಯ ಹೊಂದಿರುತ್ತದೆ.

## ಅಗತ್ಯವಾದವುಗಳು

ಈ ವ್ಯಾಯಾಮವನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು, ನಿಮಗೆ ಕೆಳಗಿನವುಗಳು ಬೇಕಾಗಿವೆ:
1. ಕಾರ್ಯಾಚರಣೆಯಲ್ಲಿ ಇರುವ ಅಜೂರ್ ಖಾತೆ. [ಉಚಿತ ಖಾತೆ ಸೃಜಿಸಿ](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Microsoft Foundry ಹಬ್ ಸೃಜಿಸಲು ಅನುಮತಿಗಳು ಇರುವುದು ಅಥವಾ ನಿಮ್ಮ ಹೆಸರಿನಲ್ಲಿ ಒಂದು ಸೃಜಿಸಲಾಗಿದೆ.
    - ನಿಮ್ಮ ಪಾತ್ರವು Contributor ಅಥವಾ Owner ಆಗಿದ್ದರೆ, ಈ ಓದಿರುವ ಪಾಠದ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಬಹುದು.

## Microsoft Foundry ಹಬ್ ರಚಿಸಿ

> **ಹೆಚ್ಚಿನ ಮಾಹಿತಿ:** Microsoft Foundry ಹಿಂದಿನ ಹೆಸರು ಅಜೂರ್ AI ಸ್ಟುಡಿಯೋ.

1. Microsoft Foundry (https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ಬ್ಲಾಗ್ ಪೋಸ್ಟ್‌ನಿಂದ ಹಬ್ ರಚನೆಗಾಗಿ ಮಾರ್ಗಸೂಚಿಗಳನ್ನು ಅನುಸರಿಸಿ.
2. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಸೃಷ್ಟಿಯಾದ ಮೇಲೆ, ತೋರಿಸಲಾಗಿರುವ ಯಾವುದೇ ಸೂಚನೆಗಳನ್ನು ಮುಚ್ಚಿ ಮತ್ತು Microsoft Foundry ಪೋರ್ಟಲ್ ನಲ್ಲಿ ಪ್ರಾಜೆಕ್ಟ್ ಪೇಜ್ ಪರಿಶೀಲಿಸಿ, ಇದು ಕೆಳಗಿನ chastಚಿತ್ರದಂತೆ ಕಾಣಬೇಕು:

    ![Microsoft Foundry Project](../../../translated_images/kn/azure-ai-foundry.88d0c35298348c2f.webp)

## ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಎಡಗೆ ಇರುವ ಪ್ಯಾನೆಲ್ನಲ್ಲಿ, **My assets** ವಿಭಾಗದಲ್ಲಿ, **Models + endpoints** ಪುಟವನ್ನು ಆಯ್ಕೆಮಾಡಿ.
2. **Models + endpoints** ಪುಟದಲ್ಲಿ, **Model deployments** ಟ್ಯಾಬ್‌ನಲ್ಲಿ, **+ Deploy model** ಮೆನುಯಲ್ಲಿ, **Deploy base model** ಆಯ್ಕೆಮಾಡಿ.
3. ಪಟ್ಟಿ ಇಲ್ಲಿನ `gpt-4o-mini` ಮಾದರಿಯನ್ನು ಹುಡುಕಿ, ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ದೃಢೀಕರಿಸಿ.

    > **ಗಮನಿಸಿ**: TPM ಕಡಿಮೆ ಮಾಡುವುದು ನಿಮ್ಮ ಉಪಯೋಗಿಸುತ್ತಿರುವ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್‌ನ ಉದ್ಯಮವನ್ನು ಹೆಚ್ಚು ಬಳಸುವುದನ್ನು ತಪ್ಪಿಸುತ್ತದೆ.

    ![Model Deployed](../../../translated_images/kn/model-deployment.3749c53fb81e18fd.webp)

## ಏಜೆಂಟ್ ರಚಿಸಿ

ನೀವು ಈಗ ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿದ್ದೀರಿ, ನೀವು ಏಜೆಂಟ್ ರಚಿಸಬಹುದು. ಏಜೆಂಟ್ ಅನ್ನು ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಬಳಸುವ ಸಂವಾದಾತ್ಮಕ AI ಮಾದರಿಯಾಗಿಯೇ ಪರಿಗಣಿಸಲಾಗುತ್ತದೆ.

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಎಡ ತಟದಲ್ಲಿ, **Build & Customize** ವಿಭಾಗದಲ್ಲಿ **Agents** ಪುಟವನ್ನು ಆಯ್ಕೆಮಾಡಿ.
2. **+ Create agent** ಕ್ಲಿಕ್ ಮಾಡಿ ಹೊಸ ಏಜೆಂಟ್ ರಚಿಸಲು. **Agent Setup** ಸಂವಾದ ಪೆಟ್ಟಿಗೆಯಲ್ಲಿ:
    - ಏಜೆಂಟ್ ಗೆ `FlightAgent` ಎಂಬ ಹೆಸರು ನೀಡಿ.
    - ನೀವು ಮೊದಲು ರಚಿಸಿದ `gpt-4o-mini` ಮಾದರಿ ನಿಯೋಜನೆ ಆಯ್ಕೆಮಾಡಿ.
    - ಏಜೆಂಟ್ ಅನುಸರಿಸುವ ಪ್ರಾಂಪ್ಟ್ ಪ್ರಕಾರ **Instructions** ಅನ್ನು ಸೆಟ್ ಮಾಡಿ. ಉದಾಹರಣೆಗೆ:
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
> ವಿವರವಾದ ಪ್ರಾಂಪ್ಟ್ ಗಾಗಿ, ನೀವು [ಈ ರೆಪೊ](https://github.com/ShivamGoyal03/RoamMind) ಕುರಿತು ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ ನೋಡಬಹುದು.

> ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ, ನೀವು **Knowledge Base** ಮತ್ತು **Actions** ಸೇರಿಸಬಹುದು ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯವನ್ನು ಸುಧಾರಿಸಲು ಮತ್ತು ಬಳಕೆದಾರರ ವಿನಂತಿಗಳ ಆಧಾರದ ಮೇಲೆ ಸ್ವಯಂಚಾಲಿತ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು. ಈ ವ್ಯಾಯಾಮಕ್ಕೆ ಈ ಹಂತಗಳನ್ನು ಆಯ್ದುಕೊಳ್ಳಬಹುದು.

![Agent Setup](../../../translated_images/kn/agent-setup.9bbb8755bf5df672.webp)

3. ಹೊಸ ಬಹು-AI ಏಜೆಂಟ್ ಸೃಷ್ಟಿಸಲು, **New Agent** ಕ್ಲಿಕ್ ಮಾಡಿ. ಹೊಸ ಏಜೆಂಟ್ ನಂತರ Agents ಪುಟದಲ್ಲಿ ತೋರಿಸಲಾಗುತ್ತದೆ.

## ಏಜೆಂಟ್ ಪರೀಕ್ಷಿಸಿ

ಏಜೆಂಟ್ ರಚಿಸಿದ ಮೇಲೆ, ನೀವು ಅದನ್ನು Microsoft Foundry ಪೋರ್ಟಲ್ ಪ್ಲೇಗ್ರೌಂಡ್‌ನಲ್ಲಿ ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗಳಿಗೆ ಹೇಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತಿರುವುದನ್ನು ಪರೀಕ್ಷಿಸಬಹುದು.

1. ನಿಮ್ಮ ಏಜೆಂಟ್ ಗೆ **Setup** ಪ್ಯಾನೆಲ್ ಮೇಲೆ, **Try in playground** ಆಯ್ಕೆಮಾಡಿ.
2. **Playground** ಪ್ಯಾನೆಲ್‌ನಲ್ಲಿ, ಚಾಟ್ ವಿಂಡೋದಲ್ಲಿ ಪ್ರಶ್ನೆಗಳನ್ನು ಟೈಪ್ ಮಾಡಿ ಏಜೆಂಟ್ ಜೊತೆ ಸಂವಹನ ಮಾಡಬಹುದು. ಉದಾಹರಣೆಗೆ, ನೀವು ಏಜೆಂಟ್‌ಗೆ ಸಿಯಾಟಲ್ ನಿಂದ ನ್ಯೂಯಾರ್ಕ್ ಗೆ 28 ರಂದು ವಿಮಾನಗಳನ್ನು ಹುಡುಕಲು ಕೇಳಬಹುದು.

    > **ಗಮನಿಸಿ**: ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ ಯಾವುದೇ ನೈಜ ಸಮಯದ ಡೇಟಾ ಬಳಸಲಾಗುತ್ತಿಲ್ಲ ಆದ್ದರಿಂದ ಪ್ರತ್ಯುತ್ತರಗಳು ನಿಖರವಾಗಿರದಿರಬಹುದು. ಈ ಪರೀಕ್ಷೆಯ ಉದ್ದೇಶ ಎಂಜನ್ ಬಳಕೆದಾರನ ಪ್ರಶ್ನೆಗಳನ್ನು ಅರಿತು, ನೀಡಿದ ಸೂಚನೆಗಳ ಮೇಲೆ ಪ್ರತಿಕ್ರಿಯಿಸುವ ಸಾಮರ್ಥ್ಯವನ್ನು ಪರೀಕ್ಷಿಸುವುದಾಗಿದೆ.

    ![Agent Playground](../../../translated_images/kn/agent-playground.dc146586de715010.webp)

3. ಏಜೆಂಟ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿದ ನಂತರ, ನೀವು ಅದನ್ನು ಹೆಚ್ಚು ಉದ್ದೇಶಗಳು, ತರಬೇತಿ ಡೇಟಾ ಮತ್ತು ಕ್ರಿಯೆಗಳೊಂದಿಗೆ ಮತ್ತಷ್ಟು ಕಸ್ಟಮೈಸ್ ಮಾಡಬಹುದು.

## ಸಂಪನ್ಮೂಲಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ

ನೀವು ಏಜೆಂಟ್ ಪರೀಕ್ಷೆಯನ್ನು ಮುಗಿಸಿದಾಗ, ಹೆಚ್ಚುವರಿ ವೆಚ್ಚಗಳು ಬರುವುದನ್ನು ತಪ್ಪಿಸಲು ಅದನ್ನು ಅಳಿಸಬಹುದು.
1. [ಅಜೂರ್ ಪೋರ್ಟಲ್](https://portal.azure.com) ತೆರೆಯಿರಿ ಮತ್ತು ಈ ವ್ಯಾಯಾಮಕ್ಕೆ ಬಳಸಿದ ಹಬ್ ಸಂಪನ್ಮೂಲಗಳಿರುವ resource group ವಿಷಯವನ್ನು ವೀಕ್ಷಿಸಿ.
2. ಟೂಲ್‌ಬಾರ್‌ನಲ್ಲಿ **Delete resource group** ಆಯ್ಕೆಮಾಡಿ.
3. resource group ಹೆಸರನ್ನು ನಮೂದಿಸಿ ಮತ್ತು ಅದನ್ನು ಅಳಿಸಲು ದೃಢೀಕರಿಸಿ.

## ಸಂಪನ್ಮೂಲಗಳು

- [Microsoft Foundry ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry ಪೋರ್ಟಲ್](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Studio ನೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸುವುದು](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [ಅಜೂರ್‌ನಲ್ಲಿ AI ಏಜೆಂಟ್ ಆಧಾರಗಳು](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತ್ಯಾಜ್ಯಕ್ಕಾಗಿ**:  
ಈ ದಸ್ತಾವೇಜು AI ಭಾಷಾಂತರ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಭಾಷಾಂತರಿಸಲಾಗಿದೆ. ನಾವು ಸರಿಯಾಗಿರುವ ಬಗ್ಗೆ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂක්‍රීಯ ಭಾಷಾಂತರಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪಿದ ಮಾಹಿತಿಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ತಿಳಿಯಿರಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಇರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲ ಎಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರಣ ಬಳಕೆಯಿಂದ ಸಂಭವಿಸುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗರ್ಭಿತತೆಗಳು ಅಥವಾ ದುರುಪಯೋಗಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->