[![എങ്ങനെ നല്ല AI ഏജന്റുകൾ ഡിസൈൻ ചെയ്യാം](../../../translated_images/ml/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളിലെ ചിത്രത്തെ ക്ലിക്കുക)_

# ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ

ടൂളുകൾ ഇഷ്ടകരമാണു് കാരണം അവ AI ഏജന്റുകൾക്ക് കൂടുതൽ വൈവിധ്യമാർന്ന കഴിവുകൾ നൽകുന്നു. ഏജന്റ് നടത്തുന്ന പ്രവൃത്തികളുടെ പരിധി കുറവായിരിക്കുന്നത് എങ്കിലും, ഒരു ടൂൾ ചേർത്താൽ, ഏജന്റ് വിപുലമായ പ്രവൃത്തികൾ ചെയ്യാൻ കഴിയും. ഈ അധ്യായത്തിൽ, നാം ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ എന്നത് പരിശോധിക്കും, ഇത് എങ്ങനെ AI ഏജന്റുകൾ പ്രത്യേക ടൂളുകൾ ഉപയോഗിച്ച് അവരുടെ ലക്ഷ്യങ്ങൾ നേടാമെന്ന് വിവരിക്കുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ, നമുക്ക് താഴെ ചോദ്യങ്ങൾക്കു മറുപടി കണ്ടെത്തണം:

- ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ എന്നത് എന്താണ്?
- ഇത് ഏത് ഉപയോഗകേസുകളിലായി പ്രയോഗിക്കാം?
- ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാൻ ആവശ്യമായ ഘടകങ്ങൾ/നിർമ്മാണ بلاക്കുകൾ എന്തെല്ലാം?
- വിശ്വസനീയമായ AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ ഉപയോഗിക്കുമ്പോൾ പ്രത്യേക പരിഗണനകൾ എന്തെല്ലാം?

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയായി കഴിഞ്ഞാൽ, നിങ്ങൾക്ക് കഴിയും:

- ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേണിന്റെ നിർവചനം ആയും ലക്ഷ്യവും വിശദീകരിക്കുക.
- ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ പ്രയോഗിക്കാവുന്ന ഉപയോഗകേസുകൾ തിരിച്ചറിയുക.
- ഡിസൈൻ പാറ്റേൺ നടപ്പാക്കാൻ ആവശ്യമായ പ്രധാന ഘടകങ്ങൾ മനസ്സിലാക്കുക.
- ഈ ഡിസൈൻ പാറ്റേൺ ഉപയോഗിക്കുന്ന AI ഏജന്റുകളുടെ വിശ്വസനീയത ഉറപ്പാക്കുന്നതിനുള്ള പരിഗണനകൾ തിരിച്ചറിയുക.

## ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ എന്താണ്?

**ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ** LLMs-ന് (ലാർജ് ലാംഗ്വേജ് മോഡലുകൾ) പ്രത്യേക ലക്ഷ്യങ്ങൾ നേടാൻ بيرിഹിത ടൂളുകളുമായി ഇടപെടാനുള്ള കഴിവ് നൽകുന്നതിന് ഊന്നൽ നൽകുന്നു. ടൂളുകൾ ഏജന്റ് നിർവ്വഹിക്കുന്ന കോഡുകളാണ്. ടൂൾ എന്നത് ഒരു ലളിതമായ ഫังก്ഷൻ ആയിരിക്കാം, ഉദാ: കാൽക്ക്യുലേറ്റർ, അല്ലെങ്കിൽ സ്റ്റോക്ക് വില അന്വേഷിക്കൽ അല്ലെങ്കിൽ കാലവസ്ഥ പ്രവചനത്തിന് ഏറ്റവുംപുറത്തുള്ള സേവനത്തിന്റെ API വിളി ആയിരിക്കാം. AI ഏജന്റുകൾക്കായി, ടൂളുകൾ മോഡൽ നിന്നുള്ള ഫങ്ക്ഷൻ കോളുകൾക്ക് പ്രതികരിച്ച് നടപ്പാക്കുന്നതിന് രൂപകൽപ്പന ചെയ്തതാണ്.

## ഇത് ഏത് ഉപയോഗകേസുകളിൽ പ്രയോഗിക്കാം?

AI ഏജന്റുകൾ ടൂളുകൾ ഉപയോഗിച്ച് സങ്കീർണ്ണ പ്രവർത്തനങ്ങൾ പൂർത്തിയാക്കാൻ, വിവരങ്ങൾ ശേഖരിക്കാൻ, തീരുമാനങ്ങൾ എടുക്കാൻ കഴിയും. ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ സാധാരണയായി ഡേറ്റാബേസുകൾ, വെബ് സേവനങ്ങൾ, കോഡ് വ്യാഖ്യാതാക്കൾ പോലുള്ള بيرിഹിത സിസ്റ്റങ്ങളുമായി സജീവ ഇടപെടലുകൾ ആവശ്യമായ സാഹചര്യങ്ങളിൽ ഉപയോഗിക്കുന്നു. ഇതുവഴി നിരവധി വ്യത്യസ്ത ഉപയോഗകേസുകളിൽ സഹായകരമാണ്, ഉദാ:

- **ഡൈനാമിക് വിവര ശേഖരണ:** ഏജന്റുകൾ بيرിഹിത APIകളോ ഡേറ്റാബേസുകളോ ചോദ്യിക്കുക, പുതിയ വിവരങ്ങൾ ശേഖരിക്കുക (ഉദാ: SQLite ഡേറ്റാബേസ് ചോദ്യിക്കൽ ഡാറ്റാ വിശകലനം ചെയ്യാൻ, സ്റ്റോക്ക് വിലകൾ, കാലാവസ്ഥ വിവരങ്ങൾ ശേഖരിക്കൽ).
- **കോഡ് നിർവഹണവും വ്യാഖ്യാനം:** ഏജന്റുകൾ കണക്കു പ്രശ്നങ്ങൾ പരിഹരിക്കാൻ, റിപ്പോർട്ടുകൾ സൃഷ്ടിക്കാൻ, സിമുലേഷനുകൾ നടത്താൻ കോഡ് അല്ലെങ്കിൽ സ്ക്രിപ്റ്റുകൾ നിർവഹിക്കുന്നു.
- **വർക്ക്‌ഫ്ലോ ഓട്ടോമേഷൻ:** ടാസ്‌ക് ഷെഡ്യൂളറുകൾ, ഇമെയിൽ സേവനങ്ങൾ, ഡാറ്റ പൈപ്പ്ലൈനുകൾ പോലുള്ള ടൂളുകൾ ഉൾപ്പെടുത്തി പുനരാവൃത്തി ചെയ്യാവുന്ന അല്ലെങ്കിൽ ബഹുസ്ഥാപനങ്ങളുള്ള വർക്ക്‌ഫ്ലോകൾ സ്വയം പ്രവർത്തിപ്പിക്കുക.
- **ഉപഭോക്തൃ പിന്തുണ:** ഏജന്റുകൾ CRM സിസ്റ്റങ്ങൾ, ടിക്കറ്റ് പ്ലാറ്റ്‌ഫോമുകൾ, നോളജ് ബേസുകൾ എന്നിവയിൽ ഇടപെടുകയും ഉപയോക്തൃ ചോദ്യങ്ങൾ പരിഹരിക്കുകയും ചെയ്യുന്നു.
- **വിവരം സൃഷ്ടിയും തിരുത്തലും:** ഗ്രാമർ ചെക്കറുകൾ, ടെക്സ്റ്റ് സുമരൈസറുകൾ, ഉള്ളടക്കം സുരക്ഷാ വിലയിരുത്തുവാൻ ടൂളുകൾ ഉപയോഗിച്ച് ഉള്ളടക്കം സൃഷ്ടിയിൽ സഹായിക്കുക.

## ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാൻ ആവശ്യമുള്ള ഘടകങ്ങൾ/ബിൽഡിംഗ് ബ്ലോക്കുകൾ എന്തെല്ലാം?

ഈ ബിൽഡിംഗ് ബ്ലോക്കുകൾ AI ഏജന്റിന് വിപുലമായ പ്രവർത്തനങ്ങൾ നടത്താൻ കഴിയും. ടൂൾ യൂസ് ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാൻ ആവശ്യമായ പ്രധാന ഘടകങ്ങൾ നോക്കാം:

- **ഫംക്ഷൻ/ടൂൾ സ്കീമകൾ**: ലഭ്യമായ ടൂളുകളുടെ വിശദമായ നിർവചനങ്ങൾ, ഫംഗ്ഷന്റെ പേര്, ലക്ഷ്യം, ആവശ്യമായ പാരാമീറ്ററുകൾ, പ്രതീക്ഷിക്കുന്ന output എന്നിവ ഉൾപ്പെടുന്നു. ഈ സ്കീമകൾ LLM-ന് ലഭ്യമായ ടൂളുകൾ എന്തൊക്കെയാണെന്നും എങ്ങനെ സാധുവായ അഭ്യർത്ഥനകൾ നിർമ്മിക്കാമെന്നും മനസ്സിലാക്കാൻ സഹായിക്കുന്നു.

- **ഫംക്ഷൻ നിർവഹണ തന്ത്രം**: ഉപയോക്താവിന്റെ ഉദ്ദേശ്യവും സംഭാഷണ സാഹചര്യവുമടക്കം അടിസ്ഥാനമാക്കി ടൂളുകൾ എപ്പോഴും എങ്ങനെ വിളിക്കണമെന്ന് നിയന്ത്രിക്കുന്നു. പ്ലാനർ മോഡ്യൂളുകൾ, റൂട്ടിംഗ് സാങ്കേതിക വിദ്യകൾ, നിബന്ധനാ പ്രവാഹങ്ങൾ എന്നിവ ഇതിൽ ഉൾപ്പെടാം.

- **സന്ദേശ കൈകാര്യം ചെയ്യുന്ന സംവിധാനം**: ഉപയോക്തൃ ഇൻപുട്ടുകളും LLM പ്രതികരണങ്ങളും ടൂൾ കോളുകളും ടൂൾ output-കളും തമ്മിലുള്ള സംഭാഷണ പ്രവാഹം നിയന്ത്രിക്കുന്ന ഘടകങ്ങൾ.

- **ടൂൾ ഇന്റഗ്രേഷൻ ഫ്രെയിംവർക്ക്**: ഏജന്റിനെ വിവിധ ടൂളുകളുമായി ബന്ധിപ്പിക്കുന്ന അടിസ്ഥാന ഘടന, ലളിതമായ ഫംഗ്ഷനുകളായാലും കാമ്പ്ലക്സ് بیرിഹിത സേവനങ്ങളായാലും.

- **പിശക് കൈകാര്യം ചെയ്യൽ & വിലയിരുത്തൽ**: ടൂൾ നിർവഹണത്തിൽ സംഭവിച്ച പരാജയങ്ങൾ കൈകാര്യം ചെയ്യുന്നതിന്, പാരാമീറ്ററുകൾ ശരിയാണോയെന്ന് പരിശോധിക്കൽ, പ്രതീക്ഷിക്കാത്ത പ്രതികരണങ്ങൾ നിയന്ത്രിക്കൽ എന്നിവ.

- **അവസ്ഥ മാനേജ്മെന്റ്**: സംഭാഷണ സാഹചര്യം, മുൻപ് നടത്തിയ ടൂൾ ഇടപെടലുകൾ, സ്ഥിരതയുള്ള ഡാറ്റ എന്നിവ ട്രാക്ക് ചെയ്യുന്നത്, ബഹുതവണ ഇടപെടലുകൾക്കിടയിൽ സ്ഥിരത ഉറപ്പാക്കുക.

തുടർന്ന്, ഫംഗ്ഷൻ/ടൂൾ കോളിംഗ് വിശദമായി നോക്കാം.
 
### ഫംഗ്ഷൻ/ടൂൾ കോളിംഗ്

ഫംഗ്ഷൻ കോളിംഗ് LLMs-ന് ടൂളുകളുമായി ഇടപെടാനുള്ള പ്രധാന മാർഗമാണ്. 'ഫംഗ്ഷൻ' എന്നും 'ടൂൾ' എന്നും പലസമയം മാറ്റി ഉപയോഗിക്കുന്നു, കാരണം 'ഫംഗ്ഷനുകൾ' (പുനരുപയോഗം ചെയ്യാവുന്ന കോഡ് ബ്ലോക്കുകൾ) ആണ് ഏജന്റുകൾ പ്രവർത്തനങ്ങൾക്കായി ഉപയോഗിക്കുന്ന 'ടൂൾ'കൾ. ഒരു ഫംഗ്ഷന്റെ കോഡ് പ്രവർത്തിപ്പിക്കാൻ, LLM ഉപയോക്തൃ അഭ്യർത്ഥന ഫംഗ്ഷൻ വിവരണത്തോടടങ്ങിയവയുമായെത്താൾ താരതമ്യം ചെയ്യണം. ഇതിനു വേണ്ടി എല്ലാ ലഭ്യമായ ഫംഗ്ഷനുകളുടെ വിവരണങ്ങളുള്ള ഒരു സ്കീമ LLM-ന് അയയ്ക്കുന്നു. LLM ജോലി ചെയ്യാൻ ഏറ്റവും അനുയോജ്യമായ ഫംഗ്ഷൻ തെരഞ്ഞെടുത്ത് അതിന്റെ പേര്, പാരാമീറ്ററുകൾ തിരിച്ചുമറുപടി നൽകുന്നു. തെരഞ്ഞെടുക്കപ്പെട്ട ഫംഗ്ഷൻ വിളിക്കപ്പെടുന്നു, അതിന്റെ പ്രതികരണം LLM-യ്ക്ക് അയയ്ക്കുന്നു, LLM ആ വിവരങ്ങൾ ഉപയോഗിച്ച് ഉപയോക്തൃ അഭ്യർത്ഥനയ്ക്ക് പ്രതികരിക്കുന്നു.

ഏജന്റുകൾക്കായുള്ള ഫംഗ്ഷൻ കോളിംഗ് നടപ്പിലാക്കാൻ ഡെവലപ്പർമാർക്ക് താഴെവുമുള്ളതുണ്ട്:

1. ഫംഗ്ഷൻ കോളിംഗ് പിന്തുണയ്ക്കുന്ന LLM മോഡൽ
2. ഫംഗ്ഷൻ വിവരണങ്ങൾ ഉൾപ്പെട്ട സ്കീമ
3. ഓരോ വിവരണപ്പെടുന്ന ഫംഗ്ഷനും വേണ്ട കോഡ്

ഒരു നഗരം ഇപ്പോഴത്തെ സമയം അറിയാൻ വേണ്ട ഉദാഹരണം ഉപയോഗിച്ച് വിശദീകരിക്കാം:

1. **ഫംഗ്ഷൻ കോളിംഗ് പിന്തുണയ്ക്കുന്ന LLM ആരംഭിക്കുക:**

    എല്ലാ മോഡലുകളും ഫംഗ്ഷൻ കോളിംഗ് പിന്തുണയ്ക്കുന്നില്ല, അതുകൊണ്ട് നിങ്ങൾ ഉപയോഗിക്കുന്ന LLM ഇത് ചെയ്യുമോ എന്നു പരിശോധിക്കുക പ്രധാനമാണ്. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ഫംഗ്ഷൻ കോളിംഗ് പിന്തുണയ്ക്കുന്നു. OpenAI ക്ലയന്റ് തുടക്കം Azure OpenAI **Responses API** യെ പ്രതിസന്ധികരിച്ചാണ് (സ്ഥിരമായ `/openai/v1/` എണ്ട്‌പോയിന്റ് — `api_version` ആവശ്യമില്ല).

    ```python
    # Azure OpenAI (Responses API, v1 എൻഡ്പോയിന്റ്) için OpenAI ക്ലയന്റ് ആർഭത്രണ നിര്‍ദ്ദേശിക്കുക
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **ഫംഗ്ഷൻ സ്കീമ നിർമിക്കുക**:

    അടുത്തതായി, ഫംഗ്ഷന്റെ പേര്, നിർവചനവും ഫംഗ്ഷൻ പാരാമീറ്ററുകളുടെ പേര്, വിശദീകരണം എന്നിവ ഉള്ള ജേസൺ സ്കീമ നിർമിക്കും. 
    ഈ സ്കീം മുമ്പ് സൃഷ്ടിച്ച ക്ലയന്റിന് അയച്ചു, ഉപയോക്താവിന്റെ 'സാൻ ഫ്രാൻസിസ്കോയിൽ സമയം അറിയുക' എന്ന അഭ്യർത്ഥനയ്ക്കൊപ്പം പറയും. ശ്രദ്ധിക്കേണ്ടത്, **ടൂൾ കോളിംഗ്** ആണ് ഫലമായി ലഭിക്കുന്നതും, **ചോദ്യംക്ക് അവസാനം ഉത്തരമല്ല**. മുൻപു പറഞ്ഞതുപോലെ, LLM ഏറ്റവും അനുയോജ്യമായ ഫംഗ്ഷന്റെ പേര്, പാരാമീറ്ററുകൾ തിരിച്ച് നൽകുന്നു.

    ```python
    # മോഡല് വായിക്കാൻ ഫംഗ്ഷൻ വിവരണം (റеспонд്സസ് API ഫ്ലാറ്റ് ടൂൾ ഫോർമാറ്റ്)
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
  
    # പ്രാഥമിക ഉപയോക്തൃ സന്ദേശം
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # ആദ്യ API കോൾ: ഫംഗ്ഷൻ ഉപയോഗിക്കാൻ മോഡലിനോട് ആവശ്യപ്പെടുക
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API ഫംഗ്ഷൻ_കാൾ ഇനങ്ങളായി ടൂൾ കോൾകൾ response.output-ൽ നൽകുന്നു.
    # മോഡലിന് അടുത്ത തിരുത്തലിൽ പൂർണ്ണ സാന്ദർഭ്യം ഉണ്ടാകാൻ അവ ചർച്ചയിൽ ചേർക്കുക.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **നിർവ്വഹിക്കേണ്ട ഫംഗ്ഷൻ കോഡ്:**

    ഇപ്പോൾ LLM തിരഞ്ഞെടുക്കുന്ന ഫംഗ്ഷൻ പ്രവർത്തിപ്പിക്കുന്ന കോഡ് നടപ്പിലാക്കേണ്ടതാണ്. 
    Python ഉപയോഗിച്ച് ഇപ്പോഴത്തെ സമയം നേടാനുള്ള കോഡ് എഴുതി നടപ്പിലാക്കാം. മറുപടി സന്ദേശത്തിൽ നിന്നുള്ള പേര്, പാരാമീറ്ററുകൾ എടുക്കാനുള്ള കോഡും എഴുതണം അവസാന ഫലം നേടാൻ.

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
    # ഫംഗ്ഷൻ കോളുകൾ കൈകാര്യം ചെയ്യുക
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # ഫംഗ്ഷൻ_കോള്ഔട്ട്‌പുട്ട് ഐറ്റംസായി ടൂൾ ഫലം തിരിച്ചു നൽകുക
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # രണ്ടാം API കോളിംഗ്: മോഡലിൽ നിന്നും അന്തിമ പ്രതികരണം നേടുക
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

ഫംഗ്ഷന്‍ കോളിങ് ഏജന്റ് ടൂൾ ഉപയോഗൽ большинθει, അല്ലെങ്കിൽ എല്ലാം അല്ലെങ്കിൽ എല്ലാ ഏജന്റ് ടൂൾ ഉപയോഗൽ ഡിസൈനിൻ്റെ ഹൃദയമാണ്, എന്നാൽ ഇത് സ്രഷ്ടിക്കാൻ തുടങ്ങുന്നതിൽ ചിലപ്പോൾ വെല്ലുവിളികൾ ഉണ്ടാവാം.
[പാഠം 2](../../../02-explore-agentic-frameworks) ൽ നാം പഠിച്ചപോലെ, ഏജന്റിക് ഫ്രെയിംവർക്കുകൾ ടൂൾ ഉപയോഗം നടപ്പാക്കാൻ മുമ്പ് നിർമ്മിച്ച ബിൽഡിങ്ങ് ബ്ലോക്കുകൾ നൽകുന്നു.
 
## ഏജന്റിക് ഫ്രെയിംവർക്കുകളുമായി ടൂൾ ഉപയോഗ ഉദാഹരണങ്ങൾ

വ്യത്യസ്ത ഏജന്റിക് ഫ്രെയിംവർക്കുകൾ ഉപയോഗിച്ച് ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ എങ്ങനെ നടപ്പാക്കാമെന്ന് ചില ഉദാഹരണങ്ങൾ ഇതാ:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ഒരു ഒപ്പൺ സോഴ്‌സ് AI ഫ്രെയിംവർക്കാണ്. ഫംഗ്ഷൻ കോളിങ് പ്രക്രിയ സുലഭമാക്കുന്നു, Python ഫംഗ്ഷനുകളെ `@tool` ഡെക്കറേറ്ററുമായി ടൂളുകളായി നിർവചിക്കാനാകുന്നു. മോഡലും നിങ്ങളുടെ കോഡും തമ്മിലുള്ള ആശയവിനിമയം ഈ ഫ്രെയിംവർക്കാണ് നിയന്ത്രിക്കുക. `FoundryChatClient` വഴി ഫയൽ തിരയൽ, കോഡ് ഇന്റർപ്രിറട്ടർ പോലുള്ള മുമ്പ് നിർമ്മിച്ച ടൂളുകൾ ആക്‌സസ് നൽകുന്നു.

Microsoft Agent Framework ഉപയോഗിച്ച് ഫംഗ്ഷൻ കോളിങ് പ്രക്രിയ താഴെ കാണിക്കുന്നത് പോലെ ആണ്:

![function calling](../../../translated_images/ml/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework-ൽ, ടൂളുകൾ ഡെക്കറേറ്റുചെയ്ത ഫംഗ്ഷനുകളായി നിർവചിച്ചിരിക്കുന്നു. മുമ്പ് കണ്ട `get_current_time` ഫംഗ്ഷൻ `@tool` ഡെക്കറേറ്റർ ഉപയോഗിച്ച് ടൂൾ ആക്മക്കാം. ഫ്രെയിംവർക്കി അത് സ്വയം സീരിയലൈസ് ചെയ്ത്, LLM-ക്ക് അയയ്ക്കാനുള്ള സ്കീമ സൃഷ്ടിക്കും.

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

# ഒരു ഏജന്റ് സൃഷ്ടിച്ച് ടൂൾ ഉപയോഗിച്ച് പ്രവർത്തിക്കുക
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> പുതിയ ഏജന്റിക് ഫ്രെയിംവർക്കായി വികസിപ്പിച്ചത്, ഡെവലപ്പർമാർക്ക് സുരക്ഷിതമായി ഉയർന്ന നിലവാരമുള്ള, വിപുലമാക്കാവുന്നതായ AI ഏജന്റുകൾ സൃഷ്ടിക്കാൻ, വിനിയോഗിക്കാൻ, സ്കെയിൽ ചെയ്യാൻ സഹായിക്കുന്നു, പൈതൃകമായ കമ്പ്യൂട്ട്, സ്റ്റോറേജ് നിവാരണങ്ങൾ കൈകാര്യം ചെയ്യാതെ. ഇത് എന്റർപ്രൈസ് അപ്ലിക്കേഷനുകൾക്കായി വളരെ സഹായകരമാണ്, കാരണം ഇത് ഫുൾ-മാനേജ് ചെയ്ത സേവനമാണ്, ഏന്റർപ്രൈസ്-ഗ്രേഡ് സുരക്ഷയോടുകൂടി.

നേരിട്ട് LLM API- ഉപയോഗിച്ച് വികസിപ്പിക്കൽ തമ്മിൽ താരതമ്യം ചെയ്യുമ്പോൾ, Microsoft Foundry Agent Service-ന് ചില നേട്ടങ്ങൾ ഉണ്ട്, ഉദാഹരണത്തിന്:

- ഓട്ടോമാറ്റിക് ടൂൾ കോളിങ് – ടൂൾ കോൾ പാഴ്സുചെയ്യേണ്ട, ടൂൾ വിളിക്കേണ്ട, പ്രതികരണം കൈകാര്യം ചെയ്യേണ്ട ആവശ്യം ഇല്ല; ഇത് ഇപ്പോൾ സെർവർ-സൈഡിൽ ചെയ്തു.
- സുരക്ഷിതമായി കൈകാര്യം ചെയ്യുന്ന ഡേറ്റ – സംഭാഷണ സ്റ്റേറ്റ് സ്വയം കൈകാര്യം ചെയ്യുന്നതിനുപകരം, ആവശ്യമായ എല്ലാ വിവരങ്ങളും സ്റ്റോർ ചെയ്യാൻ ത്രെഡുകൾ ആശ്രയിക്കാം.
- ഔട്ട്-ഓഫ്-ദി-ബോക്സ് ടൂളുകൾ – Bing, Azure AI Search, Azure Functions പോലുള്ള ഡേറ്റാ സോർസുകളുമായി ഇടപഴകാൻ ഉപയോഗിക്കുന്ന ടൂളുകൾ.

Microsoft Foundry Agent Service-ലുള്ള ടൂളുകൾ രണ്ടു വിഭാഗത്തിലായി വിഭജിക്കാം:

1. അറിവു ടൂളുകൾ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search-ഉടനെയുള്ള ഗ്രൗണ്ടിംഗ്</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ഫയൽ തിരയൽ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. പ്രവർത്തന ടൂളുകൾ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ഫംഗ്ഷൻ കോളിങ്</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">കോഡ് ഇന്റർപ്രിറട്ടർ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI നിർവചിച്ച ടൂളുകൾ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ഏജന്റ് സർവീസ് ഈ ടൂളുകൾ `toolset` ആയി ചേർത്ത് ഉപയോഗിക്കാൻ അനുവദിക്കുന്നു. കൂടാതെ, പ്രത്യേക സംഭാഷണത്തിൽ നിന്ന് സന്ദേശങ്ങളുടെ ചരിത്രം പിടിച്ചെടുക്കുന്ന `threads` ഉപയോഗിക്കുന്നു.

Contoso എന്ന കമ്പനിയിൽ നിങ്ങൾ ഒരു സെയിൽസ് ഏജന്റാണ് എന്നു സ്വപ്നം കാണുക. നിങ്ങളുടെ സെയിൽസ് ഡേറ്റയെക്കുറിച്ച് ചോദ്യങ്ങൾക്ക് മറുപടി പറയുന്ന ഒരു സംഭാഷണ ഏജൻറ് വികസിപ്പിക്കാൻ ആഗ്രഹിക്കുന്നു.

താഴെയുള്ള ചിത്രം Microsoft Foundry Agent Service ഉപയോഗിച്ച് നിങ്ങളുടെ സെയിൽസ് ഡേറ്റ നിർവചിക്കുന്ന വിധം കാണിക്കുന്നു:

![Agentic Service In Action](../../../translated_images/ml/agent-service-in-action.34fb465c9a84659e.webp)

ഈ സർവീസുകൾ ഉപയോഗിച്ച് ടൂളുകൾ ഉപയോഗിക്കാൻ ഒരു ക്ലയന്റ് സൃഷ്ടിച്ച് ടൂൾ അല്ലെങ്കിൽ ടൂൾസെറ്റ് നിർവചിക്കാം. പ്രായോഗികമായി ഇത് നടപ്പിലാക്കാൻ താഴെയുള്ള Python കോഡ് ഉപയോഗിക്കാം. LLM ടൂൾസെറ്റ് നോക്കി ഉപയോക്താവ് രചിച്ച ഫംഗ്ഷൻ `fetch_sales_data_using_sqlite_query` ഉപയോഗിക്കണോ, അല്ലെങ്കിൽ മുൻനിർത്തിയിരിക്കുന്ന കോഡ് ഇന്റർപ്രിറട്ടർ ഉപയോഗിക്കണോ എന്ന് നിർണ്ണയിക്കും.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ഫംഗ്ഷൻ, fetch_sales_data_functions.py ഫയലിൽ കണ്ടെത്താവുന്നതാണ്.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ടൂൾസെറ്റ് ആരംഭിക്കുക
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ഫംഗ്ഷനോടൊപ്പം ഫംഗ്ഷൻ കോൾ ചെയ്യാനുള്ള ഏജന്റ് ആരംഭിച്ച് അതിനെ ടൂൾസെറ്റിലേക്ക് ചേർക്കുക
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# കോഡ് इंटरപ്രേറ്റർ ടൂൾ ആരംഭിച്ച് ടൂൾസെറ്റിലേക്ക് ചേർക്കുക.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## വിശ്വസനീയ AI ഏജന്റുകൾ സൃഷ്ടിക്കാൻ ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ ഉപയോഗിക്കുന്നതിന് പ്രത്യേക പരിഗണനകൾ എന്തൊക്കെയാണ്?

LLMs tərəfindən ഡൈനാമിക് ആയി സൃഷ്ടിച്ച SQL-ന് സുരക്ഷാ പ്രശ്നങ്ങൾ സാധാരണമാണ്, പ്രത്യേകിച്ച് SQL ഇൻജെക്ഷൻ, ദുർവ്യക്ഷങ്ങൾ പോലുള്ള അപകടങ്ങൾ, ഡാറ്റാബേസ് നശിപ്പിക്കൽ അല്ലെങ്കിൽ ചവറ്റി മാറ്റൽ പോലുള്ള പ്രവർത്തനങ്ങൾ. ഈ ആശങ്കകൾ ശരിയാണ്‌, എന്നാൽ ഡാറ്റാബേസ് ആക്സസ് അനുമതികൾ ശരിയായി ക്രമീകരിച്ച് ഇതു ഫലപ്രദമായി നിയന്ത്രിക്കാം. കൂടുതൽ ഡാറ്റാബേസുകൾക്ക് ഇത് വായന മാത്രമുള്ള റെഡ്-ഓൺലി ആയി ക്രമീകരിക്കേണ്ടതാണ്. PostgreSQL അല്ലെങ്കിൽ Azure SQL പോലുള്ള ഡാറ്റാബേസ് സേവനങ്ങൾക്കായി ആപ്പ് റീഡ്-ഓൺലി (SELECT) റോളും നൽകുന്നത് ആവശ്യമാണ്.

ആപ്പ് സുരക്ഷിതമായ പരിസരത്തിൽ ഓടിക്കുന്നത് കൂടുതൽ സംരക്ഷണം വർധിപ്പിക്കും. എന്റർപ്രൈസ് സാഹചര്യങ്ങളിൽ, ഡാറ്റ സാധാരണയായി പ്രവർത്തന സംവിധാനങ്ങളിൽ നിന്ന് എടുക്കുകയും മാറ്റം വരുത്തുകയും ചെയ്ത് വായന മാത്രമുള്ള ഡാറ്റാബേസ് അല്ലെങ്കിൽ ഡാറ്റാ വെയർഹൗസിലേക്ക് മാറ്റാറുണ്ട്, സൗഹൃദ സ്കീമയോടെ. ഇത്തരം സമീപനം ഡാറ്റ സുരക്ഷിതം ആകാൻ, പ്രകടനം മെച്ചപ്പെട്ടതും പ്രാപ്യതകൊണ്ടും ആക്കാനും, ആപ്പിന്റെ ആക്സസ് നിയന്ത്രിക്കപ്പെട്ട വായന മാത്രമുള്ള ആക്സസാണെന്ന് ഉറപ്പാക്കാനും സഹായിക്കുന്നു.

## സാമ്പിൾ കോഡുകൾ

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ പരിശോധിക്കാൻ കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)ൽ ചേർത്ത് മറ്റ് പഠുപ്പുകാരെ കാണാം, ഓഫീസർ ഓവർസുകൾക്ക് ഹാജരാകാം, നിങ്ങളുടെ AI ഏജന്റുകളുമായി ബന്ധപ്പെട്ട ചോദ്യങ്ങൾക്ക് പാൻലിസ്റ്റുകൾക്കൊപ്പം കാഴ്ചവെക്കാം.

## അധിക സ്രോതസ്സുകൾ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service വർക്‌ഷോപ്പ്</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer मल्टि-എജന്റ് വർക്‌ഷോപ്പ്</a>

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft ഏജന്റ് ഫ്രെയിംവർക്ക് അവലോകനം</a>


## ഈ ഏജന്റിനെ സ്മോക്ക്-ടെസ്റ്റ് ചെയ്യുന്നത് (ഐച്ഛികം)

[Lesson 16](../16-deploying-scalable-agents/README.md) ൽ ഏജന്റുകൾ വിന്യസിക്കാൻ പഠിച്ചതിന് ശേഷം, ഈ പാഠത്തിന്റെ `TravelToolAgent` (ഇ nadal ഉം അതിന്റെ ടൂളുകൾ വിളിക്കുന്നുണ്ടോ, മറുപടി നൽകുന്നുണ്ടോ?) [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) ഉപയോഗിച്ച് സ്മോക്ക്-ടെസ്റ്റ് ചെയ്യാം. ഇത് എങ്ങനെ നടത്താമെന്ന് കാണാൻ [`tests/README.md`](../tests/README.md) കാണുക.

## മുമ്പത്തെ പാഠം

[ഏജന്റിക് ഡിസൈൻ പാറ്റേണുകൾ മനസ്സിലാക്കൽ](../03-agentic-design-patterns/README.md)

## അടുത്ത പാഠം

[ഏജന്റിക് RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->