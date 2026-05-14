[![അനുപമ AI ഏജന്റുമാർ എങ്ങനെ രൂപകൽപ്പന ചെയ്യാം](../../../translated_images/ml/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളിൽ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്യുക)_

# ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ

ടൂളുകൾ രസകരമാണ് കാരണം അവ AI ഏജന്റുമാർക്ക് വിപുലമായ ശേഷികൾ കൈവരിക്കാൻ അനുവദിക്കുന്നു. ഏജന്റ് നിർവ്വഹിക്കാവുന്ന പ്രവർത്തനങ്ങൾ പരിമിതമായ ഒരു സെറ്റ് വരെ മാത്രമല്ല, ഒരു ടൂൾ ചേർത്താൽ ഏജന്റ് ഇപ്പോൾ വിവിധ തരം പ്രവർത്തനങ്ങൾ നിർവ്വഹിക്കാൻ കഴിയും. ഈ അധ്യായത്തിൽ, നാം ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേണിനെ നോക്കുമെന്ന് കാണാം, അത് AI ഏജന്റുമാർ അവരുടെ ലക്ഷ്യങ്ങൾ കൈവരിക്കാൻ പ്രത്യേക ടൂളുകൾ ഉപയോഗിക്കാനുള്ള രീതിയെ വിവരിക്കുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ നാം താഴെ പറയുന്ന ചോദ്യങ്ങൾക്കു മറുപടിയെത്തിക്കാൻ ശ്രമിക്കുന്നു:

- ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ എന്നത് എന്താണ്?
- അത് എവിടെയാണ് പ്രയോഗിക്കാവുന്നതെന്ന്?
- ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാൻ ആവശ്യമായ ഘടകങ്ങൾ/നിർമ്മാണ വിഭാഗങ്ങൾ എന്തെല്ലാമാണ്?
- വിശ്വസനീയമായ AI ഏജന്റുമാർ സൃഷ്ടിക്കുന്നതിന് ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ ഉപയോഗിക്കുമ്പോൾ പ്രത്യേക പരിഗണനകൾ എന്തെല്ലാമാണ്?

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്ക് സാധിക്കും:

- ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേണിന്റെ നിർവചനംയും ലക്ഷ്യവും പറയാനാകും.
- ടൂൾ 사용 디자인 패턴 പ്രയോഗിക്കാവുന്ന ഉപയോഗ പ്രഭാവലേഖനങ്ങളെ തിരിച്ചറിയാനാകും.
- ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാൻ ആവശ്യമുള്ള പ്രധാന ഘടകങ്ങൾ മനസിലാക്കാനാകും.
- ഈ ഡിസൈൻ പാറ്റേൺ ഉപയോഗിച്ച് വിശ്വസനീയത ഉറപ്പാക്കുന്നതിനുള്ള പരിഗണനകൾ അറിയാനാകും.

## ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ എന്താണ്?

**ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ** LLMs താഴ്ന്ന ലക്ഷ്യങ്ങൾ സാധ്യമാക്കാൻ ബാഹ്യ ടൂളുകളുമായി ഇടപെടാൻ അവകാശപ്പെടുന്നതിന്റെ കഴിവിനെയാണ് കേന്ദ്രീകരിക്കുന്നത്. ടൂളുകൾ ഒരു ഏജന്റ് നിർവ്വഹിക്കാൻ കഴിയും പ്രവർത്തനങ്ങൾ ഉള്ളകോർഡ് ആണ്. ഒരു ടൂൾ കാൽക്കുലേറ്റർ പോലുള്ള എളുപ്പമുള്ള ഫങ്ഷൻ ആകാമോ, സ്റ്റോക്ക് വില പരിശോധിക്കൽ അല്ലെങ്കിൽ കാലാവസ്ഥ പ്രവചന പോലുള്ള മൂന്നാം കക്ഷി സേവനത്തിന് API കോൾ ആകാമോ. AI ഏജന്റുമാരുടെ സാഹചര്യത്തിൽ, ടൂളുകൾ **മോഡൽ-ജനിതമായ ഫങ്ഷൻ കോൾസുകൾക്ക്** പ്രതികരിച്ച് ഏജന്റുമാർ പ്രവർത്തിപ്പിക്കാൻ രൂപകൽപ്പന ചെയ്തിരിക്കുന്നു.

## ഇത് പ്രയോഗിക്കാവുന്ന ഉപയോഗങ്ങൾ എന്തെല്ലാമാണ്?

AI ഏജന്റുമാർ ആകാംക്ഷാ ജോലികൾ പൂർത്തിയാക്കാൻ, വിവരങ്ങൾ ലഭ്യമാക്കാൻ, അല്ലെങ്കിൽ തീരുമാനങ്ങൾ എടുക്കാൻ ടൂളുകൾ പ്രയോജനപ്പെടുത്തുന്നു. ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ സാധാരണയായി ഡാറ്റാബേസുകൾ, വെബ് സേവനങ്ങൾ, കോഡ് വിവർത്തകങ്ങൾ പോലുള്ള ബാഹ്യ സംവിധാനങ്ങളുമായി ഡൈനാമിക് ഇടപെടൽ ആവശ്യമുള്ള സാഹചര്യങ്ങളിൽ ഉപയോഗിക്കുന്നു. ഈ കഴിവ് പലിശയുള്ള വിവിധ ഉപയോഗ സാധ്യതകൾക്കായി സഹായിക്കുന്നു, ഉദാഹരണത്തിന്:

- **ഡൈനാമിക് വിവര തിരയൽ:** ഏജന്റുമാർ ബാഹ്യ API കൾക്ക് അല്ലെങ്കിൽ ഡാറ്റാബേസുകൾക്ക് ചോദ്യം ചെയ്‌തു പുതുക്കിയ വിവരങ്ങൾ (ഉദാഹരണത്തിന്, ഡാറ്റാ വിശകലനത്തിന് SQLite ഡാറ്റാബേസ് ചോദിക്കുക, സ്റ്റോക്ക് വിലകളോ കാലാവസ്ഥ വിവരങ്ങളോ അന്വേഷിക്കുക) ശേഖരിക്കുന്നു.
- **കോഡ് നടപ്പാക്കലും വ്യാഖ്യാനവും:** ഏജന്റുമാർ ഗണിത പ്രശ്‌നങ്ങൾ പരിഹരിക്കാൻ, റിപ്പോർട്ടുകൾ സൃഷ്ടിക്കാൻ, അല്ലെങ്കിൽ സിമുലേഷനുകൾ നടത്താൻ കോഡ് അല്ലെങ്കിൽ സ്ക്രിപ്റ്റുകൾ പ്രവർത്തിപ്പിക്കാം.
- **വർക്‌ഫ്ലോ ഓട്ടോമേഷൻ:** ടാസ്‌ക് ഷെഡ്യൂളറുകൾ, ഇമെയിൽ സേവനങ്ങൾ, ഡാറ്റ പൈപ്പലൈൻസ് പോലുള്ള ടൂളുകൾ സംയോജിപ്പിച്ച് ആവർത്തനപരവൃതികളോ ബഹുസ്ഥർ വർക്‌ഫ്ലോകളോ ഓട്ടോമേറ്റ് ചെയ്യുന്നു.
- **കസ്റ്റമർ സഹായം:** ഏജന്റുമാർ CRM സംവിധാനങ്ങളുമായി, ടിക്കറ്റ് പ്ലാറ്റ്ഫോംസുമായി, അല്ലെങ്കിൽ വിജ്ഞാന ബേസുകളുമായി ഇടപെടുകയും ഉപയോക്തൃ ചോദ്യങ്ങൾ പരിഹരിക്കുകയും ചെയ്യുന്നു.
- **ഉള്ളടക്ക സൃഷ്ടിയും എഡിറ്റിംഗും:** ഗ്രാമർ ചെക്കറുകൾ, ടെക്സ്റ്റ് സംഗ്രഹീകരണ ഉപകരണങ്ങൾ, അല്ലെങ്കിൽ ഉള്ളടക്ക സുരക്ഷാ വിലയിരുത്തൽ ഉപകരണങ്ങൾ പോലുള്ള ടൂളുകൾ ഉപയോഗിച്ച് ഉള്ളടക്ക സൃഷ്ടി ജോലികളിലേക്ക് ഏജന്റുമാർ സഹായം നൽകുന്നു.

## ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാൻ ആവശ്യമായ ഘടകങ്ങൾ/നിർമ്മാണ വിഭാഗങ്ങൾ എന്തെല്ലാമാണ്?

അടുത്തിടെ, AI ഏജന്റ് വ്യാപകമായ ജോലികൾ നിർവ്വഹിക്കാൻ സാധിക്കും. ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാൻ ആവശ്യമായ പ്രധാന ഘടകങ്ങൾ കാണാം:

- **ഫങ്ഷൻ/ടൂൾ സ്കീമാസുകൾ**: ലഭ്യമായ ടൂളുകളുടെ വിശദമായ വ്യാഖ്യാനങ്ങൾ, ഫങ്ഷൻ നാമം, പ്രയോജ്‌നം, ആവശ്യമായ പാരാമീറ്ററുകൾ, പ്രതീക്ഷിക്കുന്ന ഔട്ട്‌പുട്ടുകൾ എന്നിവ. ഈ സ്കീമകൾ LLM ന് ലഭ്യമായ ടൂളുകൾ മനസിലാക്കാനും സാധുവായ अनुरോധങ്ങൾ നിർമ്മിക്കാനും സഹായിക്കുന്നു.

- **ഫങ്ഷൻ എക്സിക്യൂഷൻ ലജിക്**: ഉപയോക്താവിന്റെ അഭിലാഷവും സംഭാഷണ സാഹചര്യവും അടിസ്ഥാനപ്പെടുത്തി ടൂളുകൾ എപ്പോഴും എങ്ങനെ വിളിക്കാമെന്നത് നിയന്ത്രിക്കുന്നു. പ്ലാനർാണ്‌ മൾഡ്യൂളുകൾ, റൂട്ടിംഗ് സംവിധാനം, അല്ലെങ്കിൽ സവിശേഷ ഗുണധർമമുള്ള പ്രവാഹങ്ങൾ ഉൾപ്പെടാം.

- **അനുവാദം കൈകാര്യം ചെയ്യുന്ന വ്യവസ്ഥ**: ഉപയോക്തൃ ഇൻപുട്ടുകൾ, LLM പ്രതികരണങ്ങൾ, ടൂൾ കോൾസ്, ടൂൾ ഔട്ട്പുട്ടുകൾ എന്നിവയുടെ സംഭാഷണ ശ്രേണിയ നയിക്കുന്ന ഘടകങ്ങൾ.

- **ടൂൾ ഇന്റഗ്രേഷൻ ഫ്രെയിംവർക്ക്**: ഏജന്റ് വിവിധ വിധത്തിലുള്ള ടൂളുകളുമായി ബന്ധിപ്പിക്കുന്ന അടിസ്ഥാനം, എളുപ്പമുള്ള ഫങ്ഷനുകളും സങ്കീർണ്ണമായ ബാഹ്യ സേവനങ്ങളും ഉള്‍പ്പെടുന്നു.

- **പിശക് കൈകാര്യം നിർവഹണവും സാധുതയും**: ടൂൾ പ്രവർത്തനത്തിലെ പരാജയങ്ങൾ കൈകാര്യം ചെയ്യുന്നതിനുള്ള സംവിധാനങ്ങൾ, പാരാമീറ്ററുകൾ പരിശോധിക്കൽ, പ്രതീക്ഷിക്കുന്നില്ലാത്ത പ്രതികരണങ്ങൾ നിയന്ത്രിക്കൽ.

- **സ്റ്റേറ്റ് മാനേജുമെന്റ്**: സംഭാഷണ സാഹചര്യവും മുന്‍ ടൂൾ ഇടപെടലുകളും സ്ഥിരതയുള്ള ഡാറ്റയും പിന്തുടരുന്നു, കൂടിവായ്പ്പുള്ള സംവാദങ്ങളുടെ തുല്യത ഉറപ്പാക്കുക.

മെറ്റീർ, ഫങ്ഷൻ/ടൂൾ കോൾസ് പറ്റിയും കൂടുതൽ വിശദമായി നോക്കാം.

### ഫങ്ഷൻ/ടൂൾ കോളിംഗ്

ഫംങ്ഷൻ കോളിംഗ് LLMs തൽസമയ ടൂളുകളുമായി ഇടപെടാൻ പ്രാഥമിക മാർഗമാണ്. 'ഫങ്ഷൻ' എന്നും 'ടൂൾ' എന്നും പരസ്പരം ഉപയോഗിക്കാറുണ്ട്; കാരണം '**ഫങ്ഷനുകൾ**' (പുനരുപയോഗം കഴിയുന്ന കോഡുകൾ) ഏജന്റുമാർ നിർവ്വഹിക്കുന്ന 'ടൂളുകൾ' ആണ്. ഒരു ഫങ്ഷന്റെ കോഡ് പ്രവർത്തിപ്പിക്കപ്പെടാൻ വേണ്ടി LLM ഉപയോക്താവിന്റെ അഭിലാഷം ഫങ്ഷന്റെ വിവരണത്തോടും താരതമ്യം ചെയ്യണം. ഇതിനായി എല്ലാ ലഭ്യ ഫങ്ഷനുകളുടെ വിവരണങ്ങളുള്ള ഒരു സ്കീമ LLM ന് അയയ്ക്കപ്പെടുന്നു. LLM പിന്നീട് ഏറ്റവും അനുയോജ്യമായ ഫങ്ഷൻ തെരഞ്ഞെടുത്ത് അതിന്റെ നാമവും argumentുകളും തിരിച്ചയയ്ക്കുന്നു. തിരഞ്ഞെടുക്കപ്പെട്ട ഫങ്ഷൻ പ്രവർത്തിപ്പിക്കപ്പെടുകയും ഫലം LLM ൽ തിരിച്ചയയ്ക്കപ്പെടുകയും പിന്നീട് ഉപയോക്താവിന്റെ അഭ്യർത്ഥനയ്ക്ക് LLM പ്രതികരിക്കുന്നു.

എജന്റുമാർക്ക് ഫങ്ഷൻ കോളിംഗ് നടപ്പിലാക്കാൻ താഴെവണ്ണം വേണം:

1. ഫങ്ഷൻ കോളിംഗ് പിന്തുണയുള്ള ഒരു LLM മോഡൽ
2. ഫങ്ഷൻ വിവരണങ്ങൾ ഉൾകൊള്ളുന്ന ഒരു സ്കീമ
3. ഓരോ ഫങ്ഷനും നിർവ്വഹിക്കുന്ന കോഡ്

ഉദാഹരണമായി ഒരു നഗരത്തിലെ നിലവിലെ സമയം നേടുന്നതിന്:

1. **ഫംങ്ഷൻ കോളിംഗ് പിന്തുണയുള്ള LLM ആരംഭിക്കുക:**

   എല്ലാം മോഡലുകളും ഫംങ്ഷൻ കോളിംഗ് പിന്തുണയ്ക്കുന്നില്ല, അതിനാൽ നിങ്ങൾ ഉപയോഗിക്കുന്ന LLM ഇത് പിന്തുണയ്ക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ഫംങ്ഷൻ കോളിംഗ് പിന്തുണയ്ക്കുന്നു. Azure OpenAI ക്ലയന്റ് ആരംഭിക്കുന്നത് തുടങ്ങാം.

    ```python
    # Azure OpenAI ക്ലയന്റ് ഇൻഷിയലൈസ് ചെയ്യുക
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```
  
1. **ഫംങ്ഷൻ സ്കീമ രൂപപ്പെടുത്തുക**:

   പിന്നീട് ഫംങ്ഷൻ നാമം, ഫംങ്ഷൻ ചെയ്യുന്നത് വിശദീകരണം, ഫംങ്ഷൻ പാരാമീറ്ററുകളുടെ നാമങ്ങൾ-വിവരണങ്ങൾ ഉൾപ്പടെയുള്ള JSON സ്കീമ നിർവ്വചിക്കും.
   പിന്നീട് ഈ സ്കീമ മുൻകൂട്ടി സൃഷ്ടിച്ച ക്ലയന്റ് ഒരുമിച്ച് ഉപയോക്താവിന്റെ San Francisco ന്റെ സമയം കണ്ടെത്താൻ അഭ്യർത്ഥന അയയ്ക്കും. പ്രധാനമായി ശ്രദ്ധിക്കേണ്ടത് **ടൂൾ കോൾ** ആണ് തിരിച്ചുവരുന്നത്, ചോദ്യത്തിനുള്ള അന്തിമ ഉത്തരമല്ല. മുൻപ് പറഞ്ഞതുപോലെ, LLM നിർദ്ദേശിച്ച ഫംങ്ഷന്റെ പേര് மற்றும் അതിനു നൽകിയ argument പുറത്തുനൽകുന്നു.

    ```python
    # മോഡൽ വായിക്കാൻ ഫംഗ്ഷൻ വിവരണം
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
  
    ```python
  
    # പ്രാഥമിക ഉപയോക്തൃ സന്ദേശം
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # ആദ്യ API കോള്ബ്: മോഡലിനെ ഫങ്ഷൻ ഉപയോഗിക്കാൻ ചോദിക്കുക
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # മോഡലിന്റെ പ്രതികരണം പ്രോസസ്സ് ചെയ്യുക
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```
  
    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **ജോലി നിർവ്വഹിക്കാൻ ആവശ്യമായ ഫംങ്ഷൻ കോഡ്:**

   ഇപ്പോൾ LLM തിരഞ്ഞെടുക്കുന്ന ഫംങ്ഷൻ പ്രവർത്തിപ്പിക്കേണ്ടതിനാൽ അതിന്റെ കോഡ് നടപ്പിലാക്കണം.
   Python ഉപയോഗിച്ച് നിലവിലെ സമയം ലഭിക്കുന്ന കോഡ് എഴുതാം. ഫലം കിട്ടാൻ response_message നിന്നും ഫംങ്ഷൻ നാമവും argumentകളും എടുക്കുന്ന കോഡും ആവശ്യമുണ്ട്.

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
     # ഫംഗ്ഷൻ കോൾസ് കൈകാര്യം ചെയ്യുക
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # രണ്ടാം API കോൾ: മോഡലിൽ നിന്നുള്ള അന്തിമ പ്രതികരണം നേടുക
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```
  
     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```
  
ഫംങ്ഷൻ കോളിംഗ് ഏജന്റ് ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേണിന്റെ ഹൃദയമാണ്, എങ്കിലും അത് ആദ്യത്തേത്തുടങ്ങുമ്പോൾ ചിലപ്പോൾ വെല്ലുവിളിയാകാം.  
പാഠം [Lesson 2](../../../02-explore-agentic-frameworks) ൽ നിങ്ങള്‍ പഠിച്ചതുപോലെ, ഏജന്റിക് ഫ്രെയിംവർക്കുകൾ ടൂൾ ഉപയോഗത്തിനുള്ള മുൻനിർമ്മിത ഘടകങ്ങൾ നൽകുന്നു.

## ഏജന്റിക് ഫ്രെയിംവർക്കുകൾ ഉപയോഗിച്ച് ടൂൾ ഉപയോഗ ഉദാഹരണങ്ങൾ

വിവിധ ഏജന്റിക് ഫ്രെയിംവർക്കുകൾ ഉപയോഗിച്ച് ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ എങ്ങനെ നടപ്പിലാക്കാമെന്ന് ഉദാഹരണങ്ങൾ കാണാം:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> AI ഏജന്റുമാർ സൃഷ്ടിക്കാൻ ഒരു ഓപ്പൺസോഴ്സ് ഫ്രെയിംവർക്ക് ആണ്. ഫംങ്ഷൻ കോളിംഗ് ഉപയോഗിക്കുന്നത് ലളിതമാക്കാൻ Python ഫംങ്ഷനുകളെ `@tool` ഡെക്കറേറ്ററും ഉപയോഗിച്ച് ടൂളുകളായി നിർവ്വചിക്കാം. മോഡലും നിങ്ങളുടെ കോഡും തമ്മിലുള്ള എതിരിടപാട് ഫ്രെയിംവർക്ക് കൈകാര്യം ചെയ്യുന്നു. കൂടാതെ `AzureAIProjectAgentProvider` വഴി ഫയൽ സെർച്ച്, കോഡ് ഇന്റർപ്രിറ്റർ പോലുള്ള മുൻസജ്ജമായ ടൂളുകൾ ലഭ്യമാക്കുന്നു.

താഴെ ചിത്രീകരിക്കുന്ന ഡിസഗ്രാമിൽ Microsoft Agent Framework-ചെയ്യുന്ന ഫംങ്ഷൻ കോളിംഗ് പ്രക്രിയ കാണാം:

![function calling](../../../translated_images/ml/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework-ൽ ടൂളുകൾ ഡെക്കറേറ്റഡ് ഫംങ്ഷനുകളായി നിർവ്വചിച്ചിരിക്കുന്നു. മുമ്പ് കണ്ട `get_current_time` ഫംങ്ഷൻ `@tool` ഡെക്കറേറ്റർ ഉപയോഗിച്ച് ടൂളായി മാറ്റാം. ഫ്രെയിംവർക്ക് ദിശാനിർദ്ദേശവും പാരാമീറ്റര്‍ സ്കീമയും സ്വയം സീരിയലൈസ് ചെയ്ത് LLM യ്ക്ക് അയച്ചുതരുന്നു.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ക്ലയന്റ് സൃഷ്ടിക്കുക
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ഒരു ഏജന്റ് സൃഷ്ടിച്ച് ടൂളുമായി പ്രവർത്തിപ്പിക്കുക
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> പുതിയ ഏജന്റിക് ഫ്രെയിംവർക്ക് ആണ്, വികസകരെ സുരക്ഷിതമായി AI ഏജന്റുമാർ നിർമ്മിക്കാൻ, വിനിയോഗിക്കാൻ, സ്‌കെയിൽ ചെയ്യാൻ സഹായിക്കുന്നു, അടിസ്ഥാന ഗണന അധികാരങ്ങളും സംഭരണ കാഴ്ചകളും കൈകാര്യം ചെയ്യാതെ. ഇത് സ്ഥാപനപ്രയോഗങ്ങൾക്ക് ഏറെ ഉപയുക്തമാണ്, കാരണം ഇത് മുഴുവൻ മാനേജുമെന്റ് സർവീസായി കമ്പനി നിലവാരമുള്ള സുരക്ഷ നൽകുന്നു.

LLM API നെ നേരിട്ട് ഉപയോഗിക്കുന്നതുമായി താരതമ്യപ്പെടുത്തുമ്പോൾ, Azure AI Agent Service ചില നേട്ടങ്ങൾ നൽകുന്നു:

- സ്വയം പ്രവർത്തിക്കുന്ന ടൂൾ കോളിംഗ് - ടൂൾ കോൾ ഡികോഡ് ചെയ്ത് പ്രവർത്തിപ്പിക്കുകയും പ്രതികരണം കൈകാര്യം ചെയ്യാനുള്ള ആവശ്യമില്ല, എല്ലാം സെർവർ സൈഡിൽ നടക്കുന്നു
- സുരക്ഷിതമായി മാനേജു ചെയ്ത ഡാറ്റ - സംഭാഷണ സ്റ്റേറ്റ് എടുക്കാനുള്ള ഭാരം നീക്കം ചെയ്ത്, ത്രെഡ്സ് വഴി എല്ലാം സൂക്ഷിക്കുന്നു
- ഔട്ട്-ഓഫ്-ദി ബോക്സ് ടൂളുകൾ - Bing, Azure AI Search, Azure Functions പോലെയുള്ള ഡാറ്റാ സ്രോതസുകളുമായി ഇടപെടാനുള്ള ടൂളുകൾ

Azure AI Agent Service-യിലെ ടൂളുകൾ രണ്ട് വിഭാഗങ്ങളായി വിഭജിക്കാം:

1. വിജ്ഞാന ടൂളുകൾ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ഉപയോഗിച്ച് ഭിന്നീകരണം</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ഫയൽ സെർച്ച്</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. പ്രവർത്തന ടൂളുകൾ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ഫംങ്ഷൻ കോളിംഗ്</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">കോഡ് ഇന്റർപ്രിറ്റർ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI നിർവചിച്ച ടൂളുകൾ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service നമുക്ക് ഈ ടൂളുകൾ `toolset` ആയി ഒരുമിച്ച് ഉപയോഗിക്കാൻ അനുവദിക്കുന്നു. കൂടാതെ പ്രത്യേക സംവാദത്തിൽ നിന്നുള്ള സന്ദേശങ്ങളുടെ ചരിത്രം ട്രാക്ക് ചെയ്യുന്ന `threads`-ഉം ഉപയോഗിക്കുന്നു.

നിങ്ങൾ കോൺററോ എന്ന് പേരുള്ള കമ്പനിയിലെ സെയിൽസ് ഏജന്റാണെന്ന് കരുതൂ. നിങ്ങളുടെ സെയിൽസ് ഡാറ്റ സംബന്ധിച്ച ചോദ്യങ്ങൾക്ക് മറുപടി നൽകുന്ന സംഭാഷണ ഏജണ്ട് വികസിപ്പിക്കാൻ ആഗ്രഹിക്കുന്നു.

താഴെ ചിത്രത്തിൽ Azure AI Agent Service ഉപയോഗിച്ച് നിങ്ങളുടെ സെയിൽസ് ഡാറ്റ വിശകലനം ചെയ്യുന്ന രീതിയ് കാണാം:

![Agentic Service In Action](../../../translated_images/ml/agent-service-in-action.34fb465c9a84659e.webp)

സേവനത്തോടൊപ്പം ഏതെങ്കിലും ടൂളുകൾ ഉപയോഗിക്കാൻ ക്ലയന്റ് സൃഷ്ടിച്ച് ടൂൾ അല്ലെങ്കിൽ ടൂൾസെറ്റ് നിർവ്വചിക്കാം. പ്രായോഗികമായി നടപ്പാക്കാൻ ഈ Python കോഡ് ഉപയോഗിക്കാം. LLM ടൂൾസെറ്റിനെ നോക്കി ഉപയോക്താവ് സൃഷ്ടിച്ച ഫംങ്ഷൻ, `fetch_sales_data_using_sqlite_query`, അല്ലെങ്കിൽ മുൻകൂട്ടി ഉണ്ടാക്കിയ കോഡ് ഇന്റർപ്രിറ്റർ ഉപയോഗിക്കാമെന്ന് തീരുമാനിക്കും.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py ഫയലിൽ കാണുന്ന fetch_sales_data_using_sqlite_query ഫംഗ്ഷൻ.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ടൂൾസെറ്റ് ആരംഭിക്കുക
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ഫംഗ്ഷനുമായി ഫംഗ്ഷൻ കോൾ ചെയ്യുന്ന ഏജന്റ് ആരംഭിച്ച് അത് ടൂൾസെറ്റിലേക്ക് കൂട്ടിച്ചേർക്കുക
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# കോഡ് ഇൻറർപ്രിറ്റർ ടൂൾ ആരംഭിച്ച് ടൂൾസെറ്റിലേക്കു ചേർക്കുക.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```
  
## വിശ്വസനീയമായ AI ഏജന്റുമാർ സൃഷ്‌ടിക്കുന്നതിന് ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേണിൽ പ്രത്യേക പരിഗണനകൾ എന്തെല്ലാമാണ്?

LLM കളാൽ ഡൈനാമിക് ആയി സൃഷ്ടിക്കപ്പെട്ട SQL സുരക്ഷയിൽ പ്രധാന പ്രധാനം ആണ്, പ്രത്യേകിച്ച് SQL ഇൻജക്ഷൻ, അല്ലെങ്കിൽ ഡേറ്റാബേസ് നഷ്ടപ്പെടുത്തൽ പോലുള്ള ദുര്‍വിനിയോഗ സാധ്യതകൾ. ഈ ആശങ്കകൾ ശരിയാണ്, എന്നാൽ ഡാറ്റാബേസ് ആക്‌സസ് അനുമതികൾ ശരിയായി ക്രമീകരിച്ചാൽ അതു മറികടക്കാവുന്നതാണ്. സാധാരണ ഡാറ്റാബേസുകൾക്കായി അത് റീഡ്-ഓൺലി ക്രമീകരണം ആകുന്നു. PostgreSQL അല്ലെങ്കിൽ Azure SQL പോലുള്ള സേവനങ്ങളിൽ ആപ്പ് റീഡ്-ഓൺല (SELECT) റോളിന് അധികൃതമാകണം.

സുരക്ഷിതമായ പരിസരത്തിൽ ആപ്പ് ഓടിക്കുന്നത്arantees കൂടുതൽ സംരക്ഷണം. എന്റർപ്രൈസ് സാഹചര്യങ്ങളിൽ, ഓപ്പറേഷണൽ സിസ്റ്റങ്ങളിലെ ഡാറ്റ വിജയമായി എക്സ്ട്രാക്റ്റ് ചെയ്ത് റീഡ്-ഓൺലി ഡാറ്റാബേസ് അല്ലെങ്കിൽ ഡാറ്റ വെയർഹൗസിലേക്ക് മാറ്റുന്നു, ഉപയോക്തൃ സൗഹൃദ സ്കീമ കൂടെയാണ് നൽകുന്നത്. ഡാറ്റ സുരക്ഷിതവും കാര്യക്ഷമവും ആക്‌സസിബിളുമായിരിക്കുമെന്നും ആപ്പിന് നിരോധിതമായ, റീഡ്-ഓൺലി ആക്‌സസ് മാത്രമേ ഉണ്ടായിരിക്കുകയുള്ളൂ എന്നും ഉറപ്പാക്കുന്നു.

## സാമ്പിൾ കോഡുകൾ

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേണുകൾക്കുറിച്ച് കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ൽ ചേർന്ന് മറ്റു പഠിതാക്കളെ കാണൂ, ഓഫീസ് മണിക്കൂറുകളിൽ പങ്കെടുക്കൂ, നിങ്ങളുടെ AI ഏജന്റുമാർ സംബന്ധിച്ച ചോദ്യങ്ങൾക്ക് മറുപടി ലഭിക്കൂ.

## അധിക რესോഴ്‌സുകൾ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service വര്‍ക്ക്‌ഷോപ്പ്</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer മൾട്ടി ഏജന്റ് വര്‍ക്ക്‌ഷോപ്പ്</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework അവലോകനം</a>

## മുന്‍പത്തെ പാഠം

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## അടുത്ത പാഠം
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->