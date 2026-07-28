[![എങ്ങനെ നല്ല AI ഏജൻറുകൾ രൂപകൽപ്പന ചെയ്യാം](../../../translated_images/ml/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളില്‍ ചിത്രം ക്ലിക്കുചെയ്യുക)_

# ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ

ടൂളുകൾ ആകർഷകമാണ് കാരണം അവ AI ഏജൻറുകൾക്ക് വിശാലമായ കഴിവുകൾ നൽകുന്നു. ഏജന്റിന് നിർവ്വഹിക്കാനുള്ള പ്രവൃത്തികളുടെ പരിമിതമായ സമാഹാരം ഉണ്ടാകുന്നതിനുപകരം, ഒരു ടൂൾ ചേർത്താൽ, ഏജന്റ് ഇപ്പോൾ വിശാലമായ പ്രവൃത്തികൾ നിർവ്വഹിക്കാനാകും. ഈ അധ്യായത്തിൽ, നാം ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ നോക്കാം, ഇത് AI ഏജൻറുകൾക്ക് നിർദ്ദിഷ്ട ലക്ഷ്യങ്ങൾ നേടുന്നതിന് പ്രത്യേക ടൂളുകൾ എങ്ങനെ ഉപയോഗിക്കാമെന്ന് വിവരിക്കുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ, നാം താഴെപ്പറയുന്ന ചോദ്യങ്ങളേക്കുറിച്ച് ഉത്തരം കാണാൻ ശ്രമിക്കുന്നു:

- ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ എന്താണ്?
- ഇത് ഏത് ഉപയോഗ मामलों ൽ പാരിഹര്യമാണ്?
- രൂപകൽപ്പന പാറ്റേൺ നടപ്പിലാക്കുന്നത için ആവശ്യമായ ഘടകങ്ങൾ/ബിൽഡിംഗ് ബ്ലോക്കുകൾ എന്തൊക്കെയാണ്?
- വിശ്വസനീയമായ AI ഏജൻറുകൾ നിര്‍മ്മിക്കാൻ ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ ഉപയോഗിക്കുമ്പോൾ പ്രത്യേക പരിഗണനകൾ എന്തൊക്കെയാണ്?

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയതിനു ശേഷം, നിങ്ങൾക്ക് കഴിയും:

- ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ‌യും അതിന്റെ ലക്ഷ്യവുമായി പരിചയപ്പെടുക.
- ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ പ്രയോഗിക്കാവുന്ന ഉപയോഗ കേസുകൾ തിരിച്ചറിയുക.
- രൂപകൽപ്പന പാറ്റേൺ നടപ്പിലാക്കുന്നതിന് ആവശ്യമുള്ള പ്രധാന ഘടകങ്ങൾ മനസ്സിലാക്കുക.
- ഈ രൂപകൽപ്പന പാറ്റേൺ ഉപയോഗിച്ച് AI ഏജൻറുകളിൽ വിശ്വസനീയത ഉറപ്പാക്കുന്നതിനുള്ള പരിഗണനകൾ തിരിച്ചറിയുക.

## ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ എന്താണ്?

**ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ** LLMs-ന് പ്രത്യേകം ലക്ഷ്യങ്ങൾ നേടുന്നതിനായി ബാഹ്യ ടൂളുകളുമായി ഇടപെടാനുള്ള കഴിവ് നൽകുന്നതിൽ കേന്ദ്രീകൃതമാണ്. ടൂളുകൾ ഏജന്റ് പ്രവർത്തനങ്ങൾ നിർവ്വഹിക്കുന്നതിന് പ്രവർത്തിപ്പിക്കാവുന്ന കോഡാണ്. ഒരു ടൂൾ ലളിതമായ ഫങ്ഷൻ (ഉദാ: കാൽക്കുലേറ്റർ) ആയിരിക്കാം, അല്ലെങ്കിൽ സ്റ്റോക്ക് വില പരിശോധിക്കൽ അല്ലെങ്കിൽ കാലാവസ്ഥാ പ്രവചനമൊക്കെ പോലുള്ള മൂന്നാം കക്ഷി സേവനത്തിന് API വിളിയാവാം. AI ഏജന്റുകളുടെ പ്രചാരത്തിൽ, ടൂളുകൾ **മോഡൽ-ഉൽപന്നമായ ഫങ്ഷൻ കോൾസിന്** മറുപടിയായി ഏജന്റുകൾ നിർവഹിക്കുന്നത് ലക്ഷ്യമാക്കിയാണ്.

## ഇത് പ്രയോഗിക്കാവുന്ന ഉപയോഗ കേസുകൾ എന്തൊക്കെയാണ്?

AI ഏജന്റുകൾ ടൂളുകൾ ഉപയോഗിച്ച് സമീകൃതമായ പ്രവർത്തനങ്ങൾ പൂർത്തിയാക്കാൻ, വിവരങ്ങൾ പുനരുദ്ധരിക്കാൻ, അല്ലെങ്കിൽ തീരുമാനം എടുക്കാൻ കഴിയും. ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ ബാഹ്യ സിസ്റ്റങ്ങളുമായി ഡൈനാമിക് ഇന്ററാക്ഷൻ ആവശ്യമുള്ള സാഹചര്യങ്ങളിൽ സാധാരണയായി ഉപയോഗിക്കുന്നു, ഉദാ: ഡാറ്റാബേസുകൾ, വെബ് സർവീസുകൾ, കോഡ് ഇന്റർപ്രറ്ററുകൾ. ഇത് വിവിധ ഉപയോഗ കേസുകൾക്കായി ഉപയോഗപ്രദമാണ്, അതിനുശേഷം:

- **ഡൈനാമിക് വിവര പുനരുദ്ധരിച്ചു:** ഏജന്റുകൾ ബാഹ്യ API കളേക്കോ ഡാറ്റാബേസുകളേക്കോ സമകാലിക ഡാറ്റ നേടുന്നതിനായി ചോദ്യങ്ങൾ നടത്തും (ഉദാ: SQLite ഡാറ്റാബേസിൽ ഡാറ്റാ വിശകലനത്തിനു വേണ്ടി ചോദിക്കൽ, സ്റ്റോക്ക് വിലകൾ അല്ലെങ്കിൽ കാലാവസ്ഥാ വിവരങ്ങൾ നേടൽ).
- **കോഡ് നിർവ്വഹണംും വ്യാഖ്യാനവും:** ഏജന്റുകൾ കോഡ് അല്ലെങ്കിൽ സ്ക്രിപ്റ്റുകൾ നിർവ്വഹിച്ച് ഗണിതപ്രശ്നങ്ങൾ പരിഹരിക്കുക, റിപ്പോർട്ടുകൾ സൃഷ്ടിക്കുക, അല്ലെങ്കിൽ സിമുലേഷനുകൾ നടത്തുക.
- **വർക്ക്‌ഫ്ലോ ഓട്ടോമേഷൻ:** ടാസ്‌ക് ഷെഡ്യൂളറുകൾ, ഇമെയിൽ സേവനങ്ങൾ, ഡാറ്റാ പൈപ്പ്‌ലൈൻസ് പോലുള്ള ടൂളുകൾ ചേർത്ത് ആവർത്തിക്കുന്ന അല്ലെങ്കിൽ മൾട്ടി-സ്റ്റെപ്പ് വർ‍ക്ക്‌ഫ്ലോ ഓട്ടോമേറ്റുചെയ്യുക.
- **കസ്റ്റമർ പിന്തുണ:** ഏജന്റുകൾ CRM സിസ്റ്റങ്ങൾ, ടിക്കറ്റ് പ്ലാറ്റ്ഫോമുകൾ, അല്ലെങ്കിൽ നോളേജ് ബെയ്‌സുകളുമായി ഇടപെടerek ഉപയോക്തൃ സംശയങ്ങൾ പരിഹരിക്കുന്നു.
- **ഉള്ളടക്കം സൃഷ്ടിയും എഡിറ്റിങ്ങും:** ഗ്രാമർ ചാർക്കർത്ത്വം, ടെക്സ്റ്റ് സംസ്കരണങ്ങൾ, അല്ലെങ്കിൽ ഉള്ളടക്കം സുരക്ഷാ പരിശോധകർ പോലുള്ള ടൂളുകൾ ഉപയോഗിച്ച് ഉള്ളടക്കം സൃഷ്ടി സഹായിക്കുന്നു.

## ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ നടപ്പിലാക്കുന്നതിന് ആവശ്യമുള്ള ഘടകങ്ങൾ/ബിൽഡിംഗ് ബ്ലോക്കുകൾ എന്തൊക്കെയാണ്?

ഈ ബിൽഡിംഗ് ബ്ലോക്കുകൾ AI ഏജന്റിന് വിശാലമായ പ്രവർത്തനങ്ങൾ നിർവ്വഹിക്കാൻ അനുവദിക്കുന്നു. ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ നടപ്പിലാകാൻ ആവശ്യമുള്ള പ്രധാന ഘടകങ്ങൾ നോക്കാം:

- **ഫങ്ഷൻ/ടൂൾ സ്കീമകൾ**: ലഭ്യമായ ടൂളുകളുടെ വിശദമായ നിർവചനങ്ങൾ, അതിൽ ഫങ്ഷൻ നാമം, ഉദ്ദേശ്യം, ആവശ്യമായ പാരാമീറ്ററുകൾ, പ്രതീക്ഷിക്കാവുന്ന പുറംഫലങ്ങൾ ഉൾപ്പെടുന്നു. ഈ സ്കീമകൾ LLM-ന് ടൂളുകൾ എന്തൊക്കെ ലഭ്യമാണ് എന്ന് മനസ്സിലാക്കാനും സാധുവായ അഭ്യർത്ഥനകൾ എങ്ങനെ നിർമ്മിക്കാമെന്ന് പഠിക്കാനും സഹായിക്കുന്നു.

- **ഫങ്ഷൻ നിർവഹണ തർജ്ജന**: ഉപയോക്താവിന്റെ ഉദ്ദേശ്യം, സംഭാഷണ പ്രക്രിയ അടിസ്ഥാനമാക്കി ടൂളുകൾ എപ്പോഴും എങ്ങനെ വിളിക്കണമെന്ന നിയന്ത്രിക്കുന്നു. ഇതിൽ പ്ലാനർ മോഡ്യൂളുകൾ, റൂട്ടിംഗ് സംവിധാനം, അല്ലെങ്കിൽ കടപ്പാട് ശക്തമാക്കിയ ചാലനങ്ങൾ ഉൾപ്പെടാം.

- **സന്ദേശ നിർവ്വഹണ സംവിധാനം**: ഉപയോക്തൃ ഇൻപുട്ടുകൾ, LLM പ്രതികരണങ്ങൾ, ടൂൾ കോൾസുകൾ, ടൂൾ ഔട്ട്പുട്ടുകൾ എന്നിവയുടെ ഇടയിൽ സംഭാഷണ പ്രവാഹം നിയന്ത്രിക്കുന്നത്.

- **ടൂൾ സംവേദന ഘടന**: ലളിതമായ ഫങ്ഷനുകൾ ആണോ സങ്കീർണ്ണമായ ബാഹ്യ സേവനങ്ങളാണോ, ഏജന്റ് അവയിലേക്ക് ബന്ധിപ്പിക്കുന്ന അടിസ്ഥാന ഘടന.

- **പിശകു കൈകാര്യം & സാധുത പരിശോധന**: ടൂൾ നിർവഹണത്തിലെ പരാജയങ്ങൾ കൈകാര്യം ചെയ്യുക, പാരാമീറ്ററുകൾ ശരിയെന്ന് ഉറപ്പാക്കുക, പ്രതീക്ഷിക്കാത്ത പ്രതികരണങ്ങൾ നിയന്ത്രിക്കുക.

- **സ്ഥിതിവിവര മാനേജ്‌മെന്റ്**: സംഭാഷണ പരമ്പര, മുൻ ടൂൾ ഇടപെടലുകൾ, സ്ഥിരതയുള്ള ഡാറ്റ എന്നിവ ട്രാക്ക് ചെയ്ത് മൾട്ടി-റ്റേൺ ഇടപെടലുകൾക്ക് സुसന്ദർശനം ഉറപ്പാക്കുന്നു.

അടുത്തതായി, ഫങ്ഷൻ/ടൂൾ കോൾ എന്താണെന്ന് കൂടുതൽ വിശദമായി നോക്കാം.
 
### ഫങ്ഷൻ/ടൂൾ കോൾ

ഫങ്ഷൻ കോൾ LLM കൾ ടൂളുകളുമായി ഇടപെടുവാൻ കഴിയുന്ന പ്രധാന മാർഗമാണ്. 'ഫങ്ഷൻ' എന്നും 'ടൂൾ' എന്നും പദങ്ങൾ പലപ്പോഴും പരസ്പരം ഉപയോഗിക്കുന്നു, കാരണം 'ഫങ്ഷനുകൾ' (പുനരുപയോഗയോഗ്യമായ കോഡിന്റെ ബ്ലോക്കുകൾ) ആണു ഏജന്റുകൾ പ്രവൃത്തികൾ നിർവ്വഹിക്കാൻ ഉപയോഗിക്കുന്ന 'ടൂളുകൾ'. ഫങ്ഷന്റെ കോഡ് പ്രവർത്തിപ്പിക്കാൻ, LLM ഉപയോക്താവിന്റെ അഭ്യർത്ഥന ഫങ്ഷന്റെ വിവരണവുമായി സൂക്ഷ്മമായ താരതമ്യം നടത്തണം. ലഭ്യമായ എല്ലാ ഫങ്ഷനുകളുടെ വിവരണങ്ങൾ അടങ്ങിയൊരു സ്കീമ LLM-ന് അയയ്ക്കപ്പെടുന്നു. LLM ആവശ്യത്തിനു ഏറ്റവും അനുയോജ്യമായ ഫങ്ഷൻ തിരഞ്ഞെടുക്കുന്നു, ആ ഫങ്ഷന്റെ പേര്, പാരാമീറ്ററുകൾ അത് തിരികെ നൽകുന്നു. തിരഞ്ഞെടുത്ത ഫങ്ഷൻ പ്രവർത്തിപ്പിക്കപ്പെടുന്നു, മറുപടി LLM-ന് അയക്കുന്നു, LLM അതിന്റെ അടിസ്ഥാനത്തിൽ ഉപയോക്തൃ അഭ്യർത്ഥനയെ മറുപടി നൽകുന്നു.

ഡെവലപ്പർമാർക്ക് ഏജന്റുകളെ ഫങ്ഷൻ കോൾസിനായി നടപ്പിലാക്കാൻ താഴെപറയുന്നവ ആവശ്യമുള്ളതാണ്:

1. ഫങ്ഷൻ കോൾ പിന്തുണയുള്ള LLM മോഡൽ
2. ഫങ്ഷൻ വിവരണങ്ങൾ അടങ്ങിയ സ്കീമ
3. വിശദീകരിച്ച എല്ലാ ഫങ്ഷനുകളുടെയും കോഡ്

ഒരു നഗരത്തിലെ നിലവിലെ സമയം മനസ്സിലാക്കുന്നതിന്റെ ഉദാഹരണം ഉപയോഗിച്ച് ഇത് വിശദീകരിക്കാം:

1. **ഫങ്ഷൻ കോൾ പിന്തുണയുള്ള LLM ആരംഭിക്കുക:**

    എല്ലാ മോഡലുകളും ഫങ്ഷൻ കോൾ പിന്തുണയ്ക്കാറില്ല, അതിനാൽ നിങ്ങൾ ഉപയോഗിക്കുന്ന LLM ഇത് ചെയ്യുമോ എന്ന് പരിശോധിക്കുക പ്രധാനമാണ്. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ഫങ്ഷൻ കോൾ പിന്തുണയ്ക്കുന്നു. നാം Azure OpenAI **Responses API** (സ്ഥിരമായ `/openai/v1/` എൻഡ്പോയിന്റ് - `api_version` ആവശ്യമില്ല) ഉപയോഗിച്ച് OpenAI ക്ലയന്റ് തുടങ്ങാം.

    ```python
    # Azure OpenAI (Responses API, v1 എण्ड്‌പോയിന്റ്) සඳහා OpenAI ക്ലയന്റിനെ ആരംഭിക്കുക
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **ഫങ്ഷൻ സ്കീമ സൃഷ്ടിക്കുക:**

    ഫങ്ഷൻ നാമം, ഫങ്ഷൻ ചെയ്യുന്നത് എന്ത്, ഫങ്ഷൻ പാരാമീറ്ററുകളുടെ നാമങ്ങളും വിശദവിവരങ്ങളും അടങ്ങിയ JSON സ്കീമ നിർവചിക്കും. പിന്നീട് ഈ സ്കീമ മുൻപ് സൃഷ്ടിച്ച ക്ലയന്റിന് ഉപയോക്താവിന്റെ സാൻ ഫ്രാൻസിസ്കോയിലെ സമയം കണ്ടെത്താനുള്ള അഭ്യർത്ഥനയോടെ അയക്കും. ഒരു **ടൂൾ കോൾ** ആണ് തിരിച്ചറിയപ്പെടുന്നത്, ആശയക്കുഴപ്പമില്ലാതെ, ചോദ്യത്തിനുള്ള അന്തിമ ഉത്തരം അല്ല. LLM ഫങ്ഷൻ സർവ്വേ ചെയ്തത് തിരഞ്ഞെടുത്ത ഫങ്ഷന്റെ പേരും പാരാമീറ്ററുകളുമാണ്.


    ```python
    # മോഡൽ വായിക്കാനുള്ള ഫംഗ്ഷൻ വിവരണം (റസ്പോൺസസ് API ഫ്‌ളാറ്റ് ടൂൾ ഫോർമാറ്റ്)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # പ്രാരംഭ ഉപയോക്തൃ സന്ദേശം
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # ആദ്യത്തെ API വിളി: മോഡലിനോട് ഫങ്ഷൻ ഉപയോഗിക്കാനു അഭ്യർത്ഥിക്കുക
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # റെസ്പോൺസസ് API ഫങ്ഷൻ_കോൾ ഐറ്റംസ് ആയി ടൂൾ കോൾസ് response.output ൽ നൽകുന്നു.
    # ആ കോൾസ് സംഭാഷണത്തിലേക്ക് ചേർക്കുക ώστε മോഡലിന് അടുത്ത തവണ മുഴുവൻ സാഹചര്യവും ഉണ്ടാകൂ.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **പ്രവർത്തി നടത്താൻ ആവശ്യമുള്ള ഫങ്ഷൻ കോഡ്:**

    എപ്പോൾ LLM പ്രവർത്തിപ്പിക്കേണ്ട ഫങ്ഷൻ തിരഞ്ഞെടുത്തു, ആ ടാസ്‌ക് നിർവ്വഹിക്കുന്ന കോഡ് നടപ്പിലാക്കി പ്രവർത്തിക്കുക ആവശ്യമാണ്. പൈതൺ ഉപയോഗിച്ചു നിലവിലെ സമയവും ലഭിക്കാനുള്ള കോഡ് ഞങ്ങൾ നിർമ്മിക്കാം. മറുപടി സന്ദേശത്തിൽ നിന്ന് ഫങ്ഷിന്റെ പേര്, പാരാമീറ്ററുകൾ എടുത്ത് അന്തിമ ഫലമാക്കേണ്ട കോഡും എഴുതണം.


    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # ഫംഗ്ഷൻ കോൾസിനെ കൈകാര്യം ചെയ്യുക
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # ടൂൾ ഫലത്തെ function_call_output ഇനമായി തിരിച്ചുവരുത്തുക
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # രണ്ടാം API കോൾ: മോഡലിൽ നിന്ന് അന്തിമ പ്രതികരണം നേടുക
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ഫങ്ഷൻ കോൾ ഏജന്റ് ടൂൾ ഉപയോഗ രൂപകൽപ്പനയുടെ ഹൃദയഭാഗമാണെങ്കിലും, തുടക്കം മുതൽ നടപ്പാക്കുന്നത് ചിലപ്പോൾ വെല്ലുവിളിയാണ്.
[Lesson 2](../../../02-explore-agentic-frameworks) ൽ പഠിച്ച പോലെ, ഏജന്റിക് ഫ്രെയിംവർക്ക് മുൻകൂർ നിർമ്മിച്ച ഘടകങ്ങൾ ടൂൾ ഉപയോഗം നടപ്പിലാക്കാൻ സഹായിക്കുന്നു.
 
## ഏജന്റിക് ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച ടൂൾ ഉപയോഗ ഉദാഹരണങ്ങൾ

വിവിധ ഏജന്റിക് ഫ്രെയിംവർകുകൾ ഉപയോഗിച്ച് ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ എങ്ങനെ നടപ്പിലാക്കാമെന്ന് ചില ഉദാഹരണങ്ങൾ ഇവിടെ കൊടുക്കുന്നു:

### മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക്

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ഒരു ഓപ്പൺസോഴ്സ് ഫ്രെയിംവർക്ക് ആണ്. ഇത് ഫങ്ഷൻ കോൾ ലളിതമാക്കുന്നു, Python ഫങ്ഷനുകളെ `@tool` ഡെക്കറേറ്റർ ഉപയോഗിച്ച് ടൂളുകളായി നിർവചിക്കാൻ അനുവദിക്കുന്നു. മോഡലിനും നിങ്ങളുടെ കോഡിനും ഇടയിലുള്ള സംവാദം ഫ്രെയിംവർക്ക് കൈകാര്യം ചെയ്യുന്നു. ഇത് `FoundryChatClient` വഴിയുള്ള ഫയൽ തിരയൽ, കോഡ് ഇന്റർപ്രറ്റർ പോലുള്ള മുൻകൂർ നിർമ്മിച്ച ടൂളുകളിലേക്കും ആക്സസ് നൽകുന്നു.

താഴെ നൽകിയുള്ള ആകൃതി Microsoft Agent Framework ഫങ്ഷൻ കോൾ പ്രക്രിയയെ വിശദീകരിക്കുന്നു:

![function calling](../../../translated_images/ml/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework-ല്‍ ടൂളുകൾ അലങ്കരിച്ച ഫങ്ഷനുകളായി നിർവചിക്കപ്പെടുന്നു. മുൻപ് നോക്കിയ `get_current_time` ഫങ്ഷൻ `@tool` ഡെക്കറേറ്റർ ഉപയോഗിച്ച് ടൂളാക്കി മാറ്റാം. ഫങ്ഷന്റെ ഫാക്റ്റുകൾ, പാരാമീറ്ററുകളും സ്വയമേവ സീരിയലൈസ് ചെയ്ത് LLM-ന് അയയ്ക്കാനുള്ള സ്കീമ സൃഷ്ടിക്കും.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ക്ലയന്റ് സൃഷ്ടിക്കുക
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ഒരു ഏജന്റ് സൃഷ്ടിച്ച് ടൂൾ ഉപയോഗിച്ച് പ്രവർത്തിപ്പിക്കുക
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### മൈക്രോസോഫ്റ്റ് ഫൗണ്ട്രി ഏജന്റ് സർവീസ്

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> ഒരു പുതിയ ഏജന്റിക് ഫ്രെയിംവർക്ക് ആണ്, ഡെവലപ്പർമാർക്ക് വലിയ പാർപ്പിടമുള്ള, വ്യാപകമായ, വിപുലീകരിക്കാവുന്ന AI ഏജന്റുകൾ സുരക്ഷിതമായി നിർമ്മിക്കാനും, വിന്യസിക്കാനും, സ്കെയിൽ ചെയ്യാനും കഴിയുന്ന വിധത്തിലാണ് ഇത് രൂപകൽപ്പന ചെയ്തത്. അടിയിലെ കംപ്യൂട്ട്, സ്റ്റോറേജ് വിഭവങ്ങൾ കൈകാര്യം ചെയ്യേണ്ടത് ഒഴിവാക്കുകയും, പ്രത്യേകിച്ച് സംരംഭ ഇടപാടുകൾക്കു കരാറായ സുരക്ഷ ഉറപ്പുവരുത്തുകയും ചെയ്യുന്നു.

LLM API നേരിട്ട് ഉപയോഗിക്കുന്നതിനൊപ്പം താരതമ്യപ്പെടുത്തുമ്പോൾ, Microsoft Foundry Agent Service താഴെപ്പറയുന്ന നേട്ടങ്ങൾ നൽകുന്നു:

- ഓട്ടോമാറ്റിക് ടൂൾ കോൾ - ടൂൾ കോൾ പാഴ്‌സു ചെയ്യാനും, ടൂൾ പ്രവർത്തിപ്പിക്കാനുമുള്ള ആവശ്യം ഇല്ല; ഇത് എല്ലാം സർവർ-പക്ഷത്ത് നടക്കുന്നു
- സുരക്ഷിതമായ ഡാറ്റ മാനേജ്‌മെന്റ് - നിങ്ങളുടെ സംഭാഷണ സ്ഥിതിവിവരം കൈകാര്യം ചെയ്യാതെ, ത്രെഡ്‌സിൽ എല്ലാ വിവരങ്ങളും സൂക്ഷിക്കാൻ കഴിയും
- പുറത്തിറക്കിയ ടൂളുകൾ - Bing, Azure AI Search, Azure Functions തുടങ്ങിയ ഡാറ്റാ സ്രോതസ്സുകളുമായി ഇടപെടാൻ ഉപയോഗിക്കുന്ന ടൂളുകൾ

Microsoft Foundry Agent Service-ൽ ലഭ്യമായ ടൂളുകൾ രണ്ട് വിഭാഗങ്ങളായി വിഭജിക്കാവുന്നതാണ്:

1. നോളജ് ടൂളുകൾ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search- ഉപയോഗിച്ച ഗ്രൗണ്ടിംഗ്</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ഫയൽ തിരയൽ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. ആക്ഷൻ ടൂളുകൾ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ഫങ്ഷൻ കോൾ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">കോഡ് ഇന്റർപ്രറ്റർ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">ഓപ്പൻഎപിഐ നിർവ്വചിച്ച ടൂളുകൾ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ഏജന്റ് സർവീസ് ഈ ടൂളുകൾ ഒന്നിച്ച് `toolset` ആയി ഉപയോഗിക്കാനായി സാധ്യമാക്കുന്നു. അതോടൊപ്പം, ഒരു പ്രത്യേക സംഭാഷണത്തിലെ സന്ദേശ ചരിത്രം ത്രെഡ്സ് ഉപയോഗിച്ച് ട്രാക്ക് ചെയ്യുന്നു.

നിങ്ങൾ Contoso എന്ന കമ്പനിയിലെ ഒരു വിറ്റുൾ സംവിധാന ഏജന്റ് ആണെന്ന് കണക്കു വയ്ക്കൂ. നിങ്ങളുടെ വിൽപ്പന ഡാറ്റയെക്കുറിച്ചു ഉള്ള ചോദ്യങ്ങൾക്ക് മറുപടി നൽകുന്ന ഒരു സംഭാഷണ ഏജന്റ് വികസിപ്പിക്കണം.

താഴെയുള്ള ചിത്രം Microsoft Foundry Agent Service നിങ്ങളുടെ വിൽപ്പന ഡാറ്റ വിശകലനം ചെയ്യുന്നതിന് എങ്ങനെ ഉപയോഗിക്കാം എന്ന് കാണിക്കുന്നു:

![Agentic Service In Action](../../../translated_images/ml/agent-service-in-action.34fb465c9a84659e.webp)

ഈ ടൂളുകൾ സർവീസുമായി ഉപയോഗിക്കാൻ, നമ്മൾ ഒരു ക്ലയന്റ് സൃഷ്ടിക്കുകയും ടൂൾ അല്ലെങ്കിൽ ടൂൾസെറ്റ് നിർവചിക്കുകയും ചെയ്യും. പൈതൺ കോഡ് ഉപയോഗിച്ച് ഇതിനെ പ്രായോഗികമായി നടപ്പിലാക്കാം. ഉപയോക്തൃ അഭ്യർത്ഥന അനുസരിച്ച് LLM ടൂൾസെറ്റ് നോക്കി ഉപയോക്താവിന്റെ സൃഷ്ടിച്ച `fetch_sales_data_using_sqlite_query` ഫങ്ഷൻ അല്ലെങ്കിൽ മുൻകൂർ നിർമ്മിച്ച കോഡ് ഇന്റർപ്രറ്റർ ഉപയോഗിക്കണമെന്ന തീരുമാനമെടുക്കും.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ഫംഗ്ഷൻ, അത് fetch_sales_data_functions.py ഫയലിൽ കാണാം.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ടൂൾസെറ്റ് ആരംഭിക്കുക
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ഫംഗ്ഷനോടുകൂടിയ ഫംഗ്ഷൻ കോളിംഗ് ഏജന്റ് ആരംഭിച്ച് അത് ടൂൾസെറ്റിലേക്കു ചേർക്കുക
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# കോഡ് ഇന്റർപ്രിറ്റർ ടൂൾ ആരംഭിച്ച് അത് ടൂൾസെറ്റിലേക്കു ചേർക്കുക.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## വിശ്വസനീയമായ AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺ ഉപയോഗിക്കുമ്പോൾ പ്രത്യേക പരിഗണനകൾ എന്തൊക്കെയാണ്?

LLM വഴി ഗതാഗതമാർഗ്ഗങ്ങൾ രൂപകൽപ്പന ചെയ്യുന്ന SQL-ന്റെ സുരക്ഷ സംബന്ധിച്ച പൊതുചിന്തനയാണ്, പ്രത്യേകിച്ച് SQL ഇൻജക്ഷൻ അല്ലെങ്കിൽ ദുഷ്പ്രവൃത്തികൾ (ഡാറ്റാബേസ് ഇല്ലാതാക്കൽ, ഭ്രഷ്ടമാക്കൽ തുടങ്ങിയവ) എന്ന ഭയം. ഈ ആശങ്കകൾ ഉള്ളതിനാലും, ഡാറ്റാബേസ് ആക്സസ് അനുമതികൾ ശരിയായി ക്രമീകരിച്ചാൽ നല്ലപോലെ നിയന്ത്രിക്കാം. സാധാരണയായി ഡാറ്റാബേസ് റീഡ്-ഓൺലി ആക്കി ക്രമീകരിക്കുക പ്രധാനമാണ്. PostgreSQL അല്ലെങ്കിൽ Azure SQL പോലുള്ള ഡാറ്റാബേസ് സേവനങ്ങൾക്കായി ആപ്പ് റീഡ്-ഓൺലി (SELECT) റോൾ ഇനവോൾവ് ചെയ്‌തിരിക്കണം.

ആപ്പ് സുരക്ഷിതമായ പരിസ്ഥിതിയിൽ പ്രവർത്തിപ്പിക്കുന്നത് സുരക്ഷ കൂടുതൽ ഉറപ്പാക്കുന്നു. സംരംഭ വ്യാപാരമേഖലയിൽ, ഡാറ്റ സാധാരണയായി പ്രവർത്തന സംവിധാനങ്ങളിൽ നിന്ന് എടുത്ത് റീഡ്-ഓൺലി ഡാറ്റാബേസ് അല്ലെങ്കിൽ ഡാറ്റ ഹൈവെയറിൽ മാറ്റാറുണ്ട്, ഉപയോക്താവിന് സൗഹൃദമായ സ്കീമയോടെ. ഈ രീതിയിൽ ഡാറ്റ സുരക്ഷിതമാണ്, പ്രകടനക്ഷമതയ്ക്കും ആക്‌സസിനും അനുയോജ്യമാണ്, ആപ്പിന് നിയന്ത്രിതമായ റീഡ്-ഓൺലി ആക്സസ് ഉണ്ടാകുന്നു.

## സാമ്പിൾ കോഡുകൾ

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ടൂൾ ഉപയോഗം രൂപകൽപ്പന പാറ്റേൺസ് സംബന്ധിച്ച് കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ലേക്ക് ചേർന്നു മറ്റ് പഠനക്കാരെ 만나, ഓഫീസ് മണിക്കൂറുകളിൽ പങ്കെടുക്കുക, AI ഏജന്റുകളെക്കുറിച്ചുള്ള ചോദ്യങ്ങൾക്ക് മറുപടി നേടുക.

## അധിക സൗകര്യങ്ങൾ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework മലയാളം അവലോകനം</a>


## ഈ ഏജന്റ് സ്മോക്ക്-ടെസ്റ്റ് ചെയ്യൽ (ഐച്ഛികം)

[പാഠം 16](../16-deploying-scalable-agents/README.md) ൽ ഏജന്റുകൾ deploy ചെയ്യുന്നത് പഠിച്ചതിന് ശേഷം, ഈ പാഠത്തിലെ `TravelToolAgent` എന്നത് ഇപ്പോഴും അതിന്റെ ടൂളുകൾ വിളിക്കുന്നോ ഉത്തരം നൽകുന്നോ എന്ന് സ്മോക്ക്-ടെസ്റ്റ് ചെയ്യാൻ നിങ്ങൾക്ക് സാധിക്കും [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) ഉപയോഗിച്ച്. ഇത് എങ്ങനെ നടത്താമെന്ന് അറിയാൻ [`tests/README.md`](../tests/README.md) കാണുക.

## മുൻപത്തെ പാഠം

[Agentic Design Patterns മനസ്സിലാക്കൽ](../03-agentic-design-patterns/README.md)

## അടുത്ത പാഠം

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->