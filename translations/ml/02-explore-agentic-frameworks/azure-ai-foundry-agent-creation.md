# Azure AI ഏജന്റ് സർവീസ് വികസനം

ഈ അഭ്യാസത്തിൽ, നിങ്ങളെത്തുന്നത് [Microsoft Foundry പോർട്ടൽ](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) ലെ Azure AI ഏജന്റ് സേവന ഉപകരണങ്ങൾ ഉപയോഗിച്ച് ഫ്ലൈറ്റ് ബുക്കിംഗിന് വേണ്ടി ഒരു ഏജന്റ് സൃഷ്ടിക്കുകയാണ്. ഏജന്റ് ഉപയോക്താക്കളുമായി സംവദിക്കുകയും വിമാനയാത്രകളേക്കുറിച്ചുള്ള വിവരങ്ങൾ നൽകുകയും ചെയ്യാൻ കഴിയും.

## ആവശ്യങ്ങൾ

ഈ അഭ്യാസം പൂർത്തിയാക്കാൻ നിങ്ങൾക്ക് ആവശ്യമാണ്:
1. ഒരു സജീവ സബ്സ്ക്രിപ്ഷൻ ഉള്ള Azure അക്കൗണ്ട്. [സ്വതന്ത്രമായി ഒരു അക്കൗണ്ട് സൃഷ്‌ടിക്കുക](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. ഒരു Microsoft Foundry ഹബ് സൃഷ്ടിക്കാൻ അനുവാദമുള്ളതോ അല്ലെങ്കിൽ നിങ്ങൾക്കായി ഒന്നൊരുക്കപ്പെട്ടതോ വേണം.
    - നിങ്ങളുടെ റോളാണ് Contributor അല്ലെങ്കിൽ Owner ആണെങ്കിൽ, ഈ ട്യൂട്ടോറിയലിലെ ചവിട്ടുകൾ പിന്തുടരാം.

## Create an Microsoft Foundry hub

> **കുറിപ്പ്:** Microsoft Foundry മുന്‍പ് Azure AI Studio എന്ന പേരിലായിരുന്നു.

1. Microsoft Foundry ഹബ് സൃഷ്ടിക്കുന്നതിനെക്കുറിച്ച് [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ബ്ലോഗ് പോസ്റ്റിലെ ഈ മാർഗനിർദ്ദേശങ്ങൾ അനുഗമിക്കുക.
2. നിങ്ങളുടെ പ്രോജക്ട് സൃഷ്ടിക്കപ്പെട്ടതിനു ശേഷം, പ്രദർശിപ്പിക്കുന്ന ടിപ്പ്‌കളെ അടച്ചു Microsoft Foundry പോർട്ടൽയിലെ പ്രോജക്ട് പേജ് അവലോകനം ചെയ്യുക, അത് താഴെ കാണുന്ന ചിത്രത്തെപ്പോലെ ആണ് സംശയിക്കാവുന്നത്:

    ![Microsoft Foundry Project](../../../translated_images/ml/azure-ai-foundry.88d0c35298348c2f.webp)

## Deploy a model

1. നിങ്ങളുടെ പ്രോജക്ടിനുള്ള ഇടത് പാനലിൽ, **എന്റെ ആസ്തികൾ** വിഭാഗത്തിൽ **Models + endpoints** പേജ് തിരഞ്ഞെടുക്കുക.
2. **Models + endpoints** പേജിൽ, **Model deployments** ടാബിൽ, **+ Deploy model** മെനുവിൽ **Deploy base model** തിരഞ്ഞെടുക്കുക.
3. പട്ടികയിൽ നിന്ന് `gpt-4o-mini` മോഡൽ അന്വേഷിച്ച് തിരഞ്ഞെടുക്കുകയും സ്ഥിരീകരിക്കുകയും ചെയ്യുക.

    > **കുറിപ്പ്**: TPM കുറയ്ക്കുന്നത് നിങ്ങൾ ഉപയോഗിക്കുന്ന സബ്സ്ക്രിപ്ഷനിലെ ലഭ്യമായ കോട്ട് കൂടുതലായി ഉപയോഗിക്കാതിരിക്കാനാണ് സഹായിക്കുന്നത്.

    ![Model Deployed](../../../translated_images/ml/model-deployment.3749c53fb81e18fd.webp)

## Create an agent

ഇപ്പോൾ നിങ്ങൾ ഒരു മോഡൽ വിന്യസിച്ചതിനാൽ, ഒരു ഏജന്റ് സൃഷ്ടിക്കാവുന്നതാണ്. ഏജന്റ് ഉപയോക്താക്കളുമായി പ്രാവ്‌സംഗിച്ചുകൊണ്ട് ഇടപെടാൻ ഉപയോഗിക്കാൻ കഴിയുന്ന ഒരു സംഭാഷണാത്മക AI മോഡലാണ്.

1. നിങ്ങളുടെ പ്രോജക്ടിന്റെ ഇടത് പാനലിൽ, **Build & Customize** വിഭാഗത്തിൽ **Agents** പേജ് തിരഞ്ഞെടുക്കുക.
2. പുതിയ ഏജന്റ് സൃഷ്ടിക്കാൻ **+ Create agent** ക്ലിക്കു ചെയ്യുക. **Agent Setup** ഡയലോഗിൽ:
    - ഏജന്റിന് ഒരു പേര് നൽകുക, ഉദാഹരണത്തിന് `FlightAgent`.
    - മുൻപ് നിങ്ങൾ സൃഷ്ടിച്ച `gpt-4o-mini` മോഡൽ വിന്യസിക്കൽ തിരഞ്ഞെടുക്കപ്പെട്ടിരിക്കുന്നതായിരിക്കണം
    - ഏജന്റ് പിന്തുടരാൻ ആഗ്രഹിക്കുന്ന പ്രോംപ്റ്റ് പ്രകാരമുള്ള **Instructions** സജ്ജമാക്കുക. ഉദാഹരണമായി ഇവിടെ ഒരു ഉദാഹരണം കൊടുക്കുന്നു:
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
> For a detailed prompt, you can check out [ഈ റിപ്പോസിറ്ററി](https://github.com/ShivamGoyal03/RoamMind) for more information.
    
> Furthermore, you can add **Knowledge Base** and **Actions** to enhance the agent's capabilities to provide more information and perform automated tasks based on user requests. For this exercise, you can skip these steps.
    
![Agent Setup](../../../translated_images/ml/agent-setup.9bbb8755bf5df672.webp)

3. ഒരു പുതിയ മൾട്ടി-AI ഏജന്റ് സൃഷ്ടിക്കാൻ, सरलമായി **New Agent** ക്ലിക്കുചെയ്യുക. പുതിയതായി സൃഷ്ടിച്ച ഏജന്റ് Agents പേജിൽ പ്രദർശിപ്പിക്കും.


## Test the agent

എജന്റ് സൃഷ്ടിച്ചതിന് ശേഷം, Microsoft Foundry പോർട്ടൽ പ്ലേഗ്രൗണ്ടിൽ ഉപയോക്തൃ ചോദ്യംപ്രശ്നങ്ങൾക്ക് എത് പോലെ പ്രതികരിക്കുന്നു എന്ന് പരിശോധിക്കാൻ നിങ്ങൾക്ക് കഴിയും.

1. നിങ്ങളുടെ ഏജന്റിന്റെ **Setup** പാനലിന്റെ മുകളിൽ **Try in playground** തിരഞ്ഞെടുക്കുക.
2. **Playground** പാനലിൽ, ചാറ്റ് വിൻഡോയിലേക്ക് ചോദ്യങ്ങൾ ടൈപ്പ് ചെയ്ത് ഏജന്റുമായി സംവദിക്കാവുന്നതാണ്. ഉദാഹരണത്തിന്, നിങ്ങൾ ഏജന്റോട് 28-ാം തീയതിയിലുള്ള സീയാറ്റിൽ നിന്ന് ന്യൂയോർക്കിലേക്ക് കടക്കാവുന്ന വിമാനങ്ങൾ അന്വേഷിക്കണമെന്നായി ചോദിക്കാം.

    > **കുറിപ്പ്**: ഈ അഭ്യാസത്തിൽ യാഥാർത്ഥ്യ-സമയ ഡേറ്റ ഉപയോഗിച്ചിട്ടില്ലാത്തതിനാൽ ഏജന്റ് ശരിയായ മറുപടി നൽകാതിരിക്കാം. നൽകിയ നിർദ്ദേശങ്ങളുടെ അടിസ്ഥാനത്തിൽ ഉപയോക്തൃ ചോദ്യങ്ങൾ മനസിലാക്കി പ്രതികരിക്കുന്നതിൽ ഏജന്റിന്റെ ശേഷി പരിശോധിക്കുന്നതാണ് ഉദ്ദേശ്യം.

    ![Agent Playground](../../../translated_images/ml/agent-playground.dc146586de715010.webp)

3. ഏജന്റ് പരീക്ഷിച്ച ശേഷം, അതിന്റെ ശേഷി മെച്ചപ്പെടുത്താൻ കൂടുതൽ ഇന്റന്റുകൾ, പരിശീലന ഡേറ്റ, ആക്ഷനുകൾ എന്നിവ ചേർക്കി കൂടുതൽ ഇഷ്ടാനുസരണം ക്രമീകരിക്കാൻ കഴിയും.

## Clean up resources

എജന്റ് പരീക്ഷണം പൂർത്തിയായാൽ, അധികച്ചെലവ് ഒഴിവാക്കാൻ അത് ഡിലീറ്റ് ചെയ്യാം.
1. [Azure portal](https://portal.azure.com) തുറന്ന് ഈ അഭ്യാസത്തിൽ ഉപയോഗിച്ച ഹബ് റിസോഴ്‌സുകൾ വിന്യസിച്ചിരുന്ന റിസോഴ്‍സ് ഗ്രൂപ്പിന്റെ ഉള്ളടക്കങ്ങൾ കാണുക.
2. ടൂൾബാറിൽ **റിസോഴ്‌സ് ഗ്രൂപ്പ് നീക്കം ചെയ്യുക** തിരഞ്ഞെടുക്കുക.
3. റിസോഴ്‌സ് ഗ്രൂപ്പ് നാമം നൽകുകയും നീക്കം ചെയ്യാൻ നിങ്ങൾക്ക് ആഗ്രഹമുണ്ടെന്ന് സ്ഥിരീകരിക്കുകയും ചെയ്യുക.

## Resources

- [Microsoft Foundry ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry പോർട്ടൽ](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Getting Started with Azure AI Studio](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fundamentals of AI agents on Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:

ഈ രേഖ AI അടിസ്ഥാനത്തിലുള്ള വിവർത്തന സേവനം Co‑op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിരുന്നുവെങ്കിലും, യാന്ത്രിക വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടായേക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. ഈ രേഖയുടെ മാസംഭാഷയിലെ (മൂല) പതിപ്പാണ് അധികാരമുള്ള ഉറവിടമായി കാണപ്പെടേണ്ടത്. നിർണ്ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നും ഉളവാകുന്ന ഏതൊരു തെറ്റിദ്ധാരണത്തിനോ തെറ്റായ വ്യാഖ്യാനത്തിനോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->