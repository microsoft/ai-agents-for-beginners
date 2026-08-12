# Microsoft Foundry ഏജന്റ് സർവ്വീസ് വികസനം

ഈ വ്യായാമത്തിൽ, നിങ്ങൾ [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) ൽ Microsoft Foundry ഏജന്റ് സർവ്വീസ് ഉപകരണങ്ങൾ ഉപയോഗിച്ച് Flight Booking-കായി ഒരു ഏജന്റ് സൃഷ്ടിക്കുന്നു. ഏജന്റ് ഉപയോക്താക്കളുമായി സംവദിക്കാനും uçakങ്ങളേക്കുറിച്ചുള്ള വിവരങ്ങൾ നൽകാനും കഴിയും.

## മുന്‍തിരിവുകള്‍

ഈ വ്യായാമം പൂർത്തിയാക്കാൻ, നിങ്ങൾക്കാവശ്യമാണ്:
1. സജീവ സബ്സ്ക്രിപ്ഷനുള്ള ഒരു Azure അക്കൗണ്ട്. [ഉಚಿತമായി ഒരു അക്കൗണ്ട് സൃഷ്ടിക്കുക](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Microsoft Foundry ഹബ് സൃഷ്ടിക്കാൻ അനുവാദമോ, അല്ലെങ്കിൽ നിങ്ങളுக்கായി ഒരു ഹബ് സൃഷ്ടിക്കപ്പെട്ടതോ വേണം.
    - നിങ്ങളുടെ റോൾ Contributor അല്ലെങ്കിൽ Owner ആണെങ്കിൽ, ഈ ട്യൂട്ടോറിയലിലെ ചില പടി പിന്തുടരാം.

## Microsoft Foundry ഹബ് സൃഷ്ടിക്കുക

> **കുറിപ്പ്:** Microsoft Foundry മുമ്പ് Azure AI Studio എന്നറിയപ്പെട്ടിരുന്നു.

1. Microsoft Foundry ഹബ് സൃഷ്ടിക്കുന്നതിനുള്ള ഈ മാർഗ്ഗനിർദ്ദേശങ്ങൾ [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ബ്ലോഗ് പോസ്റ്റിൽ കാണുക.
2. നിങ്ങളുടെ പ്രോജക്ട് സൃഷ്ടിക്കപ്പെട്ടപ്പോൾ, പ്രദർശിപ്പിച്ചിരിക്കുന്ന ടിപ്പുകൾ അടച്ചുവെച്ച് Microsoft Foundry പോർട്ടലിലുള്ള പ്രോജക്ട് പേജ് പരിശോധിക്കുക, ഇത് താഴെ കാണുന്ന ചിത്രത്തോട് സാദൃശ്യമാകും:

    ![Microsoft Foundry Project](../../../translated_images/ml/azure-ai-foundry.88d0c35298348c2f.webp)

## മോഡല്‍ വിന്യസിക്കുക

1. നിങ്ങളുടെ പ്രോജക്ടിന്റെ ഇടത് പാനലിൽ, **My assets** വകുപ്പിൽ, **Models + endpoints** പേജ് തിരഞ്ഞെടുക്കുക.
2. **Models + endpoints** പേജിൽ, **Model deployments** ടാബ് ഇൽ, **+ Deploy model** മെനുയിൽ, **Deploy base model** തിരഞ്ഞെടുക്കുക.
3. ലിസ്റ്റിൽ `gpt-5-mini` മോഡൽ തിരയുക, തുടർന്ന് അത് തിരഞ്ഞെടുക്കുകയും സ്ഥിരീകരിക്കുകയും ചെയ്യുക.

    > **കുറിപ്പ്**: TPM കുറയ്ക്കുന്നത് നിങ്ങൾ ഉപയോഗിക്കുന്ന സബ്സ്ക്രിപ്ഷനിലുള്ള ക്വട്ട ഉപയോഗം ഒഴിവാക്കാൻ സഹായിക്കുന്നു.

    ![Model Deployed](../../../translated_images/ml/model-deployment.3749c53fb81e18fd.webp)

## ഏജന്റ് സൃഷ്ടിക്കുക

ഇപ്പോൾ നിങ്ങൾ ഒരു മോഡൽ വിന്യസിച്ചു, ഒരൊരു ഏജന്റ് സൃഷ്ടിക്കാം. ഏജന്റ് എന്നത് ഉപയോക്താക്കളുമായി സംവദിക്കാൻ ഉപയോഗിക്കുന്ന സംഭാഷണ AI മോഡലാണ്.

1. നിങ്ങളുടെ പ്രോജക്ടിന്റെ ഇടത് പാനലിൽ, **Build & Customize** വകുപ്പിൽ, **Agents** പേജ് തിരഞ്ഞെടുക്കുക.
2. പുതിയ ഏജന്റ് സൃഷ്ടിക്കാൻ **+ Create agent** ക്ലിക്ക് ചെയ്യുക. **Agent Setup** ഡയലോഗ് ബോക്സിൽ:
    - ഏജന്റിന് ഒരു പേര് നൽകുക, ഉദാഹരണത്തിന് `FlightAgent`.
    - മുമ്പ് സൃഷ്ടിച്ച `gpt-5-mini` മോഡൽ വിന്യാസം തിരഞ്ഞെടുക്കാൻ ഉറപ്പ് വരുത്തുക
    - **Instructions** നിങ്ങളുടെ ഏജന്റ് അനുഗമിക്കേണ്ട പ്രോംപ്റ്റ് പ്രകാരം സെറ്റ് ചെയ്യുക. ഉദാഹരണം ഇവിടെ:
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
> കൂടുതൽ വിശദമായ പ്രോംപ്റ്റ് కోసం, കൂടുതൽ വിവരങ്ങൾക്കായി [ഈ റെപ്പോസിറ്ററി](https://github.com/ShivamGoyal03/RoamMind) കാണാം.
    
> കൂടാതെ, ഏജന്റിന്റെ കഴിവുകൾ വർദ്ധിപ്പിക്കാൻ **Knowledge Base** & **Actions** ചേർക്കാം. ഈ വ്യായാമത്തിന് അത് ഒഴിവാക്കാം.
    
![Agent Setup](../../../translated_images/ml/agent-setup.9bbb8755bf5df672.webp)

3. പുതിയ മൾട്ടി-എഐ ഏജന്റ് സൃഷ്ടിക്കാൻ വെറും **New Agent** ക്ലിക്ക് ചെയ്യുക. പുതിയ ഏജന്റ് Agents പേജിൽ കാണിക്കും.


## ഏജന്റ് പരീക്ഷിക്കുക

ഏജന്റ് സൃഷ്ടിച്ചതിനുശേഷം, Microsoft Foundry portal-ന് ഉള്ള playground ൽ ഉപയോക്തൃ ചോദ്യങ്ങൾക്ക് എങ്ങനെ പ്രതികരിക്കുന്നു എന്ന് പരിശോധിക്കാം.

1. നിങ്ങളുടെ ഏജന്റിനുള്ള **Setup** പാനലിന്റെ മുകളിൽ, **Try in playground** തിരഞ്ഞെടുക്കുക.
2. **Playground** പാനലിൽ, ചാറ്റ് വിൻഡോയിൽ ചോദ്യങ്ങൾ ടൈപ്പ് ചെയ്ത് ഏജന്റുമായി സംവദിക്കാം. ഉദാഹരണം, 28-ന് സിയാറ്റിൽ നിന്ന് ന്യൂയോർക്കിലേക്ക് uçak ചേട്ടെടാനായി ഏജന്റിനോട് ചോദിക്കാം.

    > **കുറിപ്പ്**: ഈ വ്യായാമത്തിൽ യഥാർത്ഥ സമയ ഡേറ്റ ഉപയോഗിക്കുന്നില്ല, അതുകൊണ്ട് ഏജന്റ് എല്ലാ ശരിയായ ഉത്തരം നൽകണമെന്ന് кепാപ്യമില്ല. ലക്ഷ്യം നൽകപ്പെട്ട നിർദ്ദേശങ്ങൾ അടിസ്ഥാനമാക്കി ഉപയോക്തൃ ചോദ്യങ്ങൾക്ക് ഏജന്റ് എങ്ങനെ മറുപടി നൽകുന്നു എന്നതുപോകെയാണ്.

    ![Agent Playground](../../../translated_images/ml/agent-playground.dc146586de715010.webp)

3. ഏജന്റ് പരീക്ഷിച്ചതിനു ശേഷം, കൂടുതൽ ഇന്റന്റുകൾ, പരിശീലന ഡാറ്റ, പ്രവർത്തനങ്ങൾ ചേർത്ത് ഏജന്റിന്റെ കഴിവുകൾ മെച്ചപ്പെടുത്താം.

## സ്രോതസ്സുകൾ ശുചിയാക്കുക

ഏജന്റ് പരീക്ഷണം കഴിഞ്ഞാൽ, അധിക ചിലവ് വരുത്താതിരിക്കാൻ അത് ഡിലീറ്റ് ചെയ്യാം.
1. [Azure portal](https://portal.azure.com) തുറന്ന് നിങ്ങൾ ഈ വ്യായാമത്തിൽ ഉപയോഗിച്ച ഹബ് റിസോഴ്‌സ് ഡിപ്ലോയ്മെന്റ് നടന്നിട്ടുള്ള റിസോഴ്‌സ് ഗ്രോപ്പ് ഉള്ളടക്കം കാണുക.
2. ടൂള്ബാറിൽ നിന്നും **Delete resource group** തിരഞ്ഞെടുക്കുക.
3. റിസോഴ്‌സ് ഗ്രൂപ്പ് പേരാണ് നൽകുകയും ഡിലീറ്റ് ചെയ്യാൻ സ്ഥിരീകരിക്കുകയും ചെയ്യുക.

## സ്രോതസ്സുകൾ

- [Microsoft Foundry ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry പോർട്ടൽ](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry ഉപയോഗിച്ച് ആരംഭിക്കുക](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure-യിലെ AI ഏജന്റുകളുടെ അടിസ്ഥാനങ്ങൾ](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->