# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏเจಂಟ್ ಸರ್ವೀಸ್ ಅಭಿವೃದ್ಧಿ

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ, ನೀವು [Microsoft Foundry ಪೋರ್ಟಲ್](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏಜಂಟ್ ಸರ್ವೀಸ್ ಸಾಧನಗಳನ್ನು ಬಳಸಿಕೊಂಡು ವಿಮಾನ ಟಿಕೆಟ್ ಬುಕ್ಕಿಂಗ್ ಗಾಗಿ ಏಜೆಂಟ್ ಸೃಷ್ಟಿಸುತ್ತೀರಿ. ಆ ಏಜೆಂಟ್ ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಾದ ನಡೆಸಿ ವಿಮಾನ ಮಾಹಿತಿಯನ್ನು ಒದಗಿಸಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ.

## ಪೂರ್ವಾಪೇಕ್ಷಿತ ವಸ್ತುಗಳು

ಈ ವ್ಯಾಯಾಮವನ್ನು ಸಂಪೂರ್ಣಗೊಳಿಸಲು ನಿಮಗೆ ಈ ಕೆಳಗಿನವುಗಳು ಬೇಕಾಗಿವೆ:
1. ಸಜೀವ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ಹೊಂದಿರುವ ಏಝುರ್ ಖಾತೆ. [ಉಚಿತವಾಗಿ ಖಾತೆ ಸೃಷ್ಟಿಸಿ](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಹುಬ್ ಸೃಷ್ಟಿಸಲು ಅನುಮತಿಗಳು ಅಥವಾ ನಿಮ್ಮ ಬದಲು ಯಾರಾದರೂ ಸೃಷ್ಟಿಸುವಂತಿರಬೇಕು.
    - ನಿಮ್ಮ ಪಾತ್ರವು ಕೊಡುಗೆದಾರ (Contributor) ಅಥವಾ ಮಾಲೀಕ (Owner) ಆಗಿದ್ದರೆ, ನೀವು ಈ ಟ್ಯೂಟೋರಿಯಲ್‌ನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಬಹುದು.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಹುಬ್ ಸೃಷ್ಟಿಸಿ

> **ಗಮನಿಸಿರಿ:** ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಮೊದಲು ಅಜೂರ್ ಏಐ ಸ್ಟುಡಿಯೋ ಎಂದು ಕರೆಯಲ್ಪಡುತ್ತಿತ್ತು.

1. ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಿಂದ ಈ ಮಾರ್ಗಸೂಚಿಗಳನ್ನು ಅನುಸರಿಸಿ [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ಬ್ಲಾಗ್ ಪೋಸ್ಟ್‌ನಲ್ಲಿ ಹೆಸರಿಸಿರುವಂತೆ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಹುಬ್ ಸೃಷ್ಟಿಸಿ.
2. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಸೃಷ್ಟಿತಾದ ಬಳಿಕ, ತೋರಿಸಲಾಗುವ ಯಾವುದೇ ಟಿಪ್‌ಗಳನ್ನು ಮುಚ್ಚಿ ಮತ್ತು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಪೋರ್ಟಲ್‌ನ ಪ್ರಾಜೆಕ್ಟ್ ಪುಟವನ್ನು ಪರಿಶೀಲಿಸಿ, ಅದು ಕೆಳಗಿನ ಚಿತ್ರಕ್ಕೆ ಹೋಲುತ್ತದೆ:

    ![Microsoft Foundry Project](../../../translated_images/kn/azure-ai-foundry.88d0c35298348c2f.webp)

## ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಎಡಪಟ್ಟಿಯಲ್ಲಿ, **ನನ್ನ ಆಸ್ತಿ (My assets)** ವಿಭಾಗದಲ್ಲಿ, **ಮಾದರಿಗಳು + ತುದಿಗಳನ್ನು (Models + endpoints)** ಆಯ್ಕೆಮಾಡಿ.
2. **ಮಾದರಿಗಳು + ತುದಿಗಳು** ಪುಟದಲ್ಲಿ, **ಮಾದರಿ ನಿಯೋಜನೆಗಳು (Model deployments)** ಟ್ಯಾಬ್‌ನಲ್ಲಿ, **+ ಮಾದರಿ ನಿಯೋಜಿಸಿ** ಮೆನುದಿಂದ **ಮೂಲ ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ (Deploy base model)** ಆಯ್ಕೆಮಾಡಿ.
3. ಪಟ್ಟಿಯಲ್ಲಿ `gpt-5-mini` ಮಾದರಿಯನ್ನು ಶೋಧಿಸಿ, ನಂತರ ಅದನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ದೃಢೀಕರಿಸಿ.

    > **ಗಮನಿಸಿ**: TPM ಕಡಿಮೆಯಾದರೆ ನೀವು ಬಳಸುತ್ತಿರುವ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಕ್ವೋಟಾ ಅತಿ ಬಳಸುವಿಕೆಯನ್ನು ತಪ್ಪಿಸಬಹುದು.

    ![Model Deployed](../../../translated_images/kn/model-deployment.3749c53fb81e18fd.webp)

## ಏಜೆಂಟ್ ಸೃಷ್ಟಿಸಿ

ಈಗ ನೀವು ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿದ್ದೀರಿ, ನೀವು ಏಜೆಂಟ್ ಅನ್ನು ಸೃಷ್ಟಿಸಬಹುದು. ಏಜೆಂಟ್ ಒಂದು ಸಂವಾದಾತ್ಮಕ AI ಮಾದರಿ ಆಗಿದ್ದು, ಬಳಕೆದಾರರ ಜೊತೆಗೆ ಸಂವಾದ ನಡೆಸಲು ಉಪಯೋಗಿಸಲಾಗುತ್ತದೆ.

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಎಡಪಟ್ಟಿಯಲ್ಲಿ, **ನಿರ್ಮಿಸಿ ಮತ್ತು ಕಸ್ಟಮೈಸ್ ಮಾಡಿ (Build & Customize)** ವಿಭಾಗದಲ್ಲಿ, **ಏಜೆಂಟ್ ಗಳು (Agents)** ಪುಟವನ್ನು ಆಯ್ಕೆಮಾಡಿ.
2. ಹೊಸ ಏಜೆಂಟ್ ಸೃಷ್ಟಿಸಲು **+ ಏಜೆಂಟ್ ಸೃಷ್ಟಿಸಿ (+ Create agent)** ಕ್ಲಿಕ್ ಮಾಡಿ. **ಏಜೆಂಟ್ ಸೆಟ್ ಅಪ್ (Agent Setup)** ಡೈಲಾಗ್ ಬಾಕ್ಸ್‌ನಲ್ಲಿ:
    - ಏಜೆಂಟ್‌ಗೆ ಹೆಸರನ್ನಿಟ್ಟು, ಉದಾಹರಣೆಗೆ `FlightAgent` ಎಂದು ನಮೂದಿಸಿ.
    - ನೀವು ಮೊದಲೇ ಸೃಷ್ಟಿಸಿದ `gpt-5-mini` ಮಾದರಿ ನಿಯೋಜನೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.
    - ನೀವು ಏಜೆಂಟ್ ಅನುಸರಿಸಬೇಕಾದ ಸೂಚನೆಗಳನ್ನು **ಸೂಚನೆಗಳು (Instructions)** ವಿಭಾಗದಲ್ಲಿ ಸೆಟ್ ಮಾಡಿ. ಇಲ್ಲಿ ಒಂದು ಉದಾಹರಣೆ ಇದೆ:
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
> ವಿವರವಾದ ಪ್ರಾಂಪ್ಟಿಗಾಗಿ, ನೀವು ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ [ಈ ರೆಪೊ](https://github.com/ShivamGoyal03/RoamMind) ನೋಡಬಹುದು.
    
> ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ ಮತ್ತು ಬಳಕೆದಾರ ವಿನಂತಿಗಳ ಆಧಾರದ ಮೇಲೆ ಸ್ವಯಂಚಾಲಿತ ಕಾರ್ಯಗಳನ್ನು ನೆರವು ಮಾಡಲು ನೀವು **ಜ್ಞಾನಾಧಾರ (Knowledge Base)** ಮತ್ತು **ಕ್ರಿಯೆಗಳು (Actions)** ಸೇರಿಸಬಹುದು. ಈ ವ್ಯಾಯಾಮಕ್ಕೆ, ನೀವು ಈ ಹಂತಗಳನ್ನು ಮೀರಿ ಹೋಗಬಹುದು.
    
![Agent Setup](../../../translated_images/kn/agent-setup.9bbb8755bf5df672.webp)

3. ಹೊಸ ಬಹು-AI ಏಜೆಂಟ್ ಸೃಷ್ಟಿಸಲು ಸರಳವಾಗಿ **ಹೊಸ ಏಜೆಂಟ್ (New Agent)** ಕ್ಲಿಕ್ ಮಾಡಿ. ಹೊಸದಾಗಿ ಸೃಷ್ಟಿಸಿದ ಏಜೆಂಟ್ ನಂತರ ಏಜೆಂಟ್ ಪುಟದಲ್ಲಿ ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ.


## ಏಜೆಂಟ್ ಪರೀಕ್ಷಿಸಿ

ಏಜೆಂಟ್ ಸೃಷ್ಟಿಸಿದ ನಂತರ, ನೀವು ಅದನ್ನು ಪರೀಕ್ಷಿಸಿ ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗಳಿಗೆ ಹೇಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆಯೋ ನೋಡಬಹುದು Microsoft Foundry ಪೋರ್ಟಲ್ ಪ್ಲೇಗ್ರೌಂಡ್‌ನಲ್ಲಿ.

1. ನಿಮ್ಮ ಏಜೆಂಟ್‌ನ **ಸೆಟ್ ಅಪ್ (Setup)** ಪೇನ್‌ನ ಮೇಲ್ಭಾಗದಲ್ಲಿ, **ಪ್ಲೇಗ್ರೌಂಡ್‌ನಲ್ಲಿ ಪ್ರಯತ್ನಿಸಿ (Try in playground)** ಆಯ್ಕೆಮಾಡಿ.
2. **ಪ್ಲೇಗ್ರೌಂಡ್ (Playground)** ಪೇನ್‌ನಲ್ಲಿ, ಚಾಟ್ ವಿಂಡೋದಲ್ಲಿ ಪ್ರಶ್ನೆಗಳನ್ನು ಟೈಪ್ ಮಾಡಿ ಏಜೆಂಟ್ ಜೊತೆ ಸಂವಾದ ನಡೆಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ನೀವು ಏಜೆಂಟ್‌ಗೆ 28ನೇ ತಾರೀಖ್ಯಲ್ಲಿ ಸಿಯಾಟಲ್ ನಿಂದ ನ್ಯೂಯಾರ್ಕ್‌ಗೆ ವಿಮಾನ ಸಚಿವೆಯನ್ನು ಹುಡುಕಲು ಕೇಳಬಹುದು.

    > **ಗಮನಿಸಿ**: ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ ಯಾವುದೇ ಲೈವ್ ಡೇಟಾ ಬಳಸಲಾಗದ ಕಾರಣ ಏಜೆಂಟ್ ನಿಖರ ಉತ್ತರಗಳನ್ನು ನೀಡಿಯಲ್ಲ. ಉದ್ದೇಶವು ಸೂಚನೆಗಳ ಆಧಾರದ ಮೇಲೆ ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯಿಸುವ ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯವನ್ನು ಪರೀಕ್ಷಿಸುವುದು.

    ![Agent Playground](../../../translated_images/kn/agent-playground.dc146586de715010.webp)

3. ಏಜೆಂಟ್ ಪರೀಕ್ಷೆಯ ನಂತರ, ಅದನ್ನು ಇನ್ನೂ ಹೆಚ್ಚು ಉದ್ದೇಶಗಳನ್ನು, ತರಬೆತಿ ಅಂಕಿಗಳನ್ನು ಹಾಗೂ ಕಾರ್ಯಗಳನ್ನು ಸೇರಿಸುವ ಮೂಲಕ ಇನ್ನಷ್ಟು ಕಸ್ಟಮೈಸ್ ಮಾಡಬಹುದು.

## ಸಂಪನ್ಮೂಲಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ

ಏಜೆಂಟ್ ಪರೀಕ್ಷೆ ಮುಗಿಸಿದ ಮೇಲೆ, ಹೆಚ್ಚುವರಿ ವೆಚ್ಚ ಉಂಟಾಗದಂತೆ ಅದನ್ನು ಅಳಿಸಿ.
1. [Azure portal](https://portal.azure.com) ತೆರೆಯಿರಿ ಮತ್ತು ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ ಬಳಸಿದ ಹುಬ್ ಸಂಪನ್ಮೂಲಗಳನ್ನು ನಿಯೋಜಿಸಿದ ರಿಸೋರ್ಸ್ ಗ್ರೂಪ್‌ನ ವಿಷಯವನ್ನು ವೀಕ್ಷಿಸಿ.
2. ಟೂಲ್‌ಬಾರ್‌ನಲ್ಲಿ, **ರಿಸೋರ್ಸ್ ಗ್ರೂಪ್ ಅಳಿಸಿ (Delete resource group)** ಆಯ್ಕೆಮಾಡಿ.
3. ರಿಸೋರ್ಸ್ ಗ್ರೂಪ್ ಹೆಸರನ್ನು ನಮೂದಿಸಿ ಮತ್ತು ಅಳಿಸಲು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

## ಸಂಪನ್ಮೂಲಗಳು

- [Microsoft Foundry ನಿರ್ದೇಶನಾಲಯ](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry ಪೋರ್ಟಲ್](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry ಆರಂಭಿಕ ಮಾಹಿತಿ](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [ಏಝುರ್ ಮೇಲೆ AI ಏಜೆಂಟ್ ಮೂಲಭೂತ ಅಂಶಗಳು](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [ಏಝುರ್ AI ಡಿಸ್ಕೋರ್ಡ್](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->