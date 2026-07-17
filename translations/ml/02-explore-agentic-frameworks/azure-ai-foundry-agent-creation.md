# Microsoft Foundry ഏജന്റ് സേവന വികസനം

ഈ അഭ്യാസത്തിൽ, നിങ്ങൾ [Microsoft Foundry പോർട്ടൽ](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) ൽ Microsoft Foundry ഏജന്റ് സേവന ഉപകരണങ്ങൾ ഉപയോഗിച്ച് ഫ്ലൈറ്റ് ബുക്കിംഗിനായി ഒരു ഏജന്റ് സൃഷ്ടിക്കുന്നു. ഉപയോക്താക്കളുമായി ആശയവിനിമയം നടത്താനും യാത്രാവിവരങ്ങൾ നൽകാനും ഈ ഏജന്റ് കഴിയും.

## മുൻകൂർ ആവശ്യങ്ങൾ

ഈ അഭ്യാസം പൂർത്തിയാക്കാൻ നിങ്ങൾക്കാവശ്യമായവ:
1. സജീവ സബ്സ്ക്രിപ്ഷനുള്ള ഒരു Azure അക്കൗണ്ട്. [ഫ്രീ ആയി അക്കൗണ്ട് സൃഷ്ടിക്കുക](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Microsoft Foundry ഹബ് സൃഷ്ടിക്കാൻ അനുമതികൾ ഉണ്ടാകണം അല്ലെങ്കിൽ നിങ്ങൾക്കായി ഒരു ഹബ് സൃഷ്ടിക്കപ്പെടണം.
    - നിങ്ങളുടെ റോളും Contributor അല്ലെങ്കിൽ Owner ആണെങ്കിൽ, ഈ ട്യൂട്ടോറിയലിലെ ഘടകങ്ങൾ പിന്തുടരാം.

## Microsoft Foundry ഹബ് സൃഷ്ടിക്കുക

> **ഗమనിക്കുക:** Microsoft Foundryക്ക് മുമ്പ് Azure AI Studio എന്നു പേരുണ്ടായിരുന്നു.

1. Microsoft Foundry ബ്ലോഗ്‌ പോസ്റ്റിലെ [കൈപിടികൾ](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) അനുസരിച്ച് Microsoft Foundry ഹബ് സൃഷ്ടിക്കുക.
2. നിങ്ങളുടെ പ്രോജക്റ്റ് സൃഷ്ടിച്ച ശേഷം, കാണുന്ന ടിപ്പുകൾ അടച്ചിട്ട് Microsoft Foundry പോർട്ടൽ പ്രോജക്റ്റ് പേജ് പരിശോധിക്കുക, താഴെ ചിത്രത്തിൽ കാണുന്നത് പോലെ.

    ![Microsoft Foundry Project](../../../translated_images/ml/azure-ai-foundry.88d0c35298348c2f.webp)

## ഒരു മോഡൽ വിന്യസിക്കുക

1. നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ ഇടത്തുവശത്തെ പാനിൽ, **My assets** വിഭാഗത്തിൽ, **Models + endpoints** പേജ് തിരഞ്ഞെടുക്കുക.
2. **Models + endpoints** പേജിൽ, **Model deployments** ടാബിൽ, **+ Deploy model** മെനുവിൽ **Deploy base model** തിരഞ്ഞെടുക്കുക.
3. മോഡലുകളുടെ പട്ടികയിൽ `gpt-4.1-mini` മോഡൽ തെരഞ്ഞെടുത്ത് സ്ഥിരീകരിക്കുക.

    > **കുറിപ്പ്:** TPM കുറയ്ക്കുന്നത് നിങ്ങൾ ഉപയോഗിക്കുന്ന സബ്സ്ക്രിപ്ഷനിലെ ക്വോട്ട നൽകിയ പരിധി അധികം ഉപയോഗിക്കുന്നത് ഒഴിവാക്കാൻ സഹായിക്കും.

    ![Model Deployed](../../../translated_images/ml/model-deployment.3749c53fb81e18fd.webp)

## ഒരു ഏജന്റ് സൃഷ്ടിക്കുക

മോഡൽ വിന്യസിച്ച ശേഷം, നിങ്ങൾ ഒരു ഏജന്റ് സൃഷ്ടിക്കാം. ഏജന്റ് എന്നു പറയുന്നത് ഉപയോക്താക്കളുമായി ബന്ധപ്പെടാൻ ഉപയോഗിക്കുന്ന ഒരു സംഭാഷണ എഐ മോഡലാണ്.

1. നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ ഇടതുവശ പാനেলে, **Build & Customize** വിഭാഗത്തിൽ, **Agents** പേജ് തിരഞ്ഞെടുക്കുക.
2. **+ Create agent** ക്ലിക്കുചെയ്യുക പുതിയ ഏജന്റ് സൃഷ്ടിക്കാൻ. **Agent Setup** ഡയലോഗ് ബോക്സിൽ:
    - ഏജന്റിന് ഒരു പേര് നൽകുക, ഉദാഹരണത്തിന് `FlightAgent`.
    - നിങ്ങൾ മുമ്പ് സൃഷ്ടിച്ച `gpt-4.1-mini` മോഡൽ വിന്യാസം തിരഞ്ഞെടുക്കപ്പെട്ടിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക.
    - ഏജന്റ് പിന്തുടരാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്ന പ്രോപ്‌റ്റിന്റെ അടിസ്ഥാനത്തിൽ **Instructions** സജ്ജമാക്കുക. ഇതാ ഒരു ഉദാഹരണം:
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
> വിശദമായ പ്രോപ്റ്റിനായി [ഈ റിപോസിറ്ററി](https://github.com/ShivamGoyal03/RoamMind) പരിശോധിക്കാം.
    
> കൂടാതെ, ഉപയോക്തൃ അഭ്യർത്ഥനകൾ അനുസരിച്ച് അധിക വിവരങ്ങൾ നൽകാനും സ്വയം പ്രവർത്തനങ്ങൾ നടത്താനും **Knowledge Base** ഉം **Actions** ഉം ചേർക്കാം. ഈ അഭ്യാസത്തിനായി ഈ ഘടകങ്ങൾ ഒഴിവാക്കാം.
    
![Agent Setup](../../../translated_images/ml/agent-setup.9bbb8755bf5df672.webp)

3. ഒരു പുതിയ മൾട്ടി-എഐ ഏജന്റ് സൃഷ്ടിക്കാൻ, **New Agent** ക്ലിക്കുചെയ്യുക. പുതിയ സൃഷ്ടിച്ച ഏജന്റ് Agents പേജിൽ പ്രദർശിപ്പിക്കപ്പെടും.


## ഏജന്റിനെ പരീക്ഷിക്കുക

ഏജന്റ് സൃഷ്ടിച്ചതിന് പിന്നാലെ, Microsoft Foundry പോർട്ടലിലെ പ്ലേഗ്രൗണ്ടിൽ ഉപയോക്തൃ ചോദ്യങ്ങൾക്ക് എങ്ങനെ പ്രതികരിക്കുന്നു എന്ന് പരിശോധിക്കാം.

1. ഏജന്റിന്റെ **Setup** പാനിൽ മുകളിൽ നിന്ന് **Try in playground** തിരഞ്ഞെടുക്കുക.
2. **Playground** പാനിൽ ചാറ്റ് വിൻഡോയിൽ ചോദ്യങ്ങൾ ടൈപ്പ് ചെയ്ത് ഏജന്റിനൊപ്പം ആശയവിനിമയം നടത്താം. ഉദാഹരണത്തിന്, സെയറ്റിൽ നിന്ന് ന്യൂയോർക്കിലേക്ക് 28-നു വിമാനങ്ങൾ അന്വേഷിക്കാൻ ഏജന്റിനോട് അപേക്ഷിക്കുക.

    > **കുറിപ്പ്:** ഈ അഭ്യാസത്തിൽ യഥാർത്ഥ സമയ ഡാറ്റ ഉപയോഗിക്കുന്നതല്ലാത്തതിനാൽ ഏജന്റ് നൽകുന്ന മറുപടികൾ ശരിയായതായിരിക്കില്ല. ഏജന്റിന്റെ ഉപയോക്തൃ ചോദ്യങ്ങൾ മനസിലാക്കി പ്രതികരിക്കുന്ന ശേഷി പരിശോധിക്കുകയാണ് ഉദ്ദേശം.

    ![Agent Playground](../../../translated_images/ml/agent-playground.dc146586de715010.webp)

3. പരീക്ഷിച്ച ശേഷം, ഏജന്റിന്റെ ശേഷി മെച്ചപ്പെടുത്തുന്നതിന് കൂടുതൽ ഉദ്ദേശ്യങ്ങൾ, പരിശീലന ഡാറ്റ, പ്രവർത്തനങ്ങൾ എന്നിവ ചേർക്കാം.

## വിഭവങ്ങൾ കഴുകുക

ഏജന്റ് പരീക്ഷണം കഴിഞ്ഞാൽ, അധികച്ചെലവ് ഒഴിവാക്കാൻ അത് മായ്ക്കാം.
1. [Azure പോർട്ടൽ](https://portal.azure.com) തുറന്ന് ഈ അഭ്യാസത്തിൽ ഉപയോഗിച്ച ഹബ് വിഭവങ്ങൾ വിന്യസിച്ച റിസോഴ്‌സ് ഗ്രൂപ്പ് ഉള്ളടക്കം കാണുക.
2. ടൂള്ബാറിൽ നിന്നു **Delete resource group** തിരഞ്ഞെടുക്കുക.
3. റിസോഴ്‌സ് ഗ്രൂപ്പ് പേര് നൽകുകയും അത് മായ്ക്കാനാണ് നിങ്ങൾ ആഗ്രഹിക്കുന്നത് എന്നാണ് സ്ഥിരീകരിക്കുകയും ചെയ്യുക.

## വിഭവങ്ങൾ

- [Microsoft Foundry പ്രമാണം](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry പോർട്ടൽ](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry ആരംഭിക്കുന്ന വഴി](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure-യിൽ AI ഏജന്റുകളുടെ അടിസ്ഥാനങ്ങൾ](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->