[![നല്ല AI ഏജന്റുകള്‍ എങ്ങനെ രൂപകല്‍പ്പന ചെയ്യാം](../../../translated_images/ml/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ഈ പാഠത്തിന്റെ വീഡിയൊ കാണാൻ മുകളിൽ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്യുക)_

# Tool Use Design Pattern

ടൂളുകൾ രസകരമാണ് കാരണം അവ AI ഏജന്റുകൾക്ക് വിപുലമായ കഴിവുകൾ അനുവദിക്കുന്നു. ഏജന്റിന് ചെയ്യാവുന്ന പ്രവർത്തനങ്ങളിലൊരു സീമിത സെറ്റ് ഉണ്ടായിരുന്നതിനുപകരം, ഒരു ടൂൾ ചേർക്കുമ്പോൾ ഏജന്റ് ഏറ്റവും വ്യത്യസ്തമായ പ്രവർത്തനങ്ങൾ ചെയ്യാനാകും. ഈ അധ്യാപനത്തിൽ നാം Tool Use Design Pattern നോക്കാം, ഇത് എങ്ങനെ AI ഏജന്റുകൾക്ക് അവരുടെ ലക്ഷ്യങ്ങൾ പ്രാപ്തമാക്കാൻ പ്രത്യേക ടൂളുകൾ ഉപയോഗിക്കാമെന്ന് വിവരണം ചെയ്യുന്നു.

## Introduction

ഈ പാഠത്തിൽ നാം താഴെപ്പറയുന്ന ചോദ്യങ്ങൾക്ക് ഉത്തരം അന്വേഷിക്കുന്നു:

- ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ എന്നത് എന്താണ്?
- ഇത് ഏതു ഉപയോഗപ്രവൃത്തികളിൽ പ്രയോഗിക്കാവുന്നതാണ്?
- ഡിസൈൻ പാറ്റേൺ നടപ്പാക്കാൻ ആവശ്യമായ ഘടകങ്ങൾ/ബിൽഡിംഗ് ബ്ലോകുകൾ എന്തൊക്കെയാണ്?
- വിശ്വാസയോഗ്യമായ AI ഏജന്റുകൾ നിർമ്മിക്കാൻ Tool Use Design Pattern ഉപയോഗിക്കുമ്പോൾ പ്രത്യേക പരിഗണനകൾ എന്തൊക്കെയാണ്?

## Learning Goals

ഈ പാഠം പൂർത്തീകരിച്ചതിനുശേഷം, നിങ്ങൾക്ക് സാധിക്കും:

- Tool Use Design Pattern നും അതിന്റെ ഉദ്ദേശത്തിന് 五月天യെ നിർവചിക്കുക.
- Tool Use Design Pattern പ്രയോഗിക്കാവുന്ന ഉപയോഗങ്ങള തിരിച്ചറിയുക.
- ഡിസൈൻ പാറ്റേൺ നടപ്പാക്കാനാവശ്യമായ പ്രധാന ഘടകങ്ങൾ മനസ്സിലാക്കുക.
- ഈ ഡിസൈൻ പാറ്റേൺ ഉപയോഗിക്കുന്ന AI ഏജന്റുകളിൽ വിശ്വാസയോഗ്യത ഉറപ്പാക്കാൻ қажет പരിഗണനകൾ തിരിച്ചറിഞ്ഞുക.

## What is the Tool Use Design Pattern?

The **Tool Use Design Pattern** വലുതായ ഭാഷ മോഡലുകൾക്ക് (LLMs) പ്രത്യേക ലക്ഷ്യങ്ങൾ നേടാൻ ബാഹ്യ ടൂളുകളുമായി ഇടപഴകാനുള്ള ശേഷി നൽകുന്നതിൽ കേന്ദ്രീകരിക്കുന്നു. ടൂളുകൾ ഏജന്റ് ഒരു പ്രവർത്തനം നടത്തുന്നതിനായി നിർവഹിക്കാൻ കഴിയുന്ന കോഡാണ്. ഒരു ടൂൾ കാൽക്കുലേറ്ററിന്റെ പോലുള്ള ലളിതമായ ഫംഗ്ഷൻ ആകാമോ, സ്റ്റോക്ക് വില പരിശോധിക്കൽ അല്ലെങ്കിൽ കാലാവസ്ഥ പ്രവചനമായി ഒരു മൂന്നാംപക്ഷ സർവീസിലേക്കുള്ള API കോളായിരിക്കാമോ. AI ഏജന്റുകളുടെ സന്ദർഭത്തിൽ, ടൂളുകൾ ഭാവി **model-generated function calls** നുസരിച്ച് ഏജന്റുകൾ പ്രവർത്തിപ്പിക്കാൻ രൂപകൽപ്പന ചെയ്യപ്പെടുന്നു.

## What are the use cases it can be applied to?

AI ഏജന്റുകൾ സങ്കീർണ്ണമായ ടാസ്കുകൾ പൂർത്തിയാക്കാൻ, വിവരങ്ങൾ നേടാൻ, അല്ലെങ്കിൽ തീരുമാനങ്ങൾ എടുക്കാൻ ടൂളുകൾ ഉപയോഗിക്കാം. ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ സാധാരണയായി ഡാറ്റാബേസുകൾ, വെബ് സർവീസുകൾ, അല്ലെങ്കിൽ കോഡ് інтэрപ്രിറ്ററുകൾ പോലുള്ള ബാഹ്യ സിസ്റ്റങ്ങളുമായി ഡൈനാമിക് ഇന്ററാക്ഷൻ ആവശ്യമായ സാഹചര്യങ്ങളിൽ ഉപയോഗിക്കുന്നു. ഈ കഴിവ് പലവിധ ഉപയോഗങ്ങളിലേക്കും ഉപകാരപ്രദമാണ്, ഉദാഹരണത്തിന്:

- **ഡൈനാമിക് വിവര ശോധനം:** ഏജന്റുകൾ അപ്-ടു-ഡേറ്റ് ഡാറ്റ നേടാൻ ബാഹ്യ APIകൾക്ക് അല്ലെങ്കിൽ ഡാറ്റാബേസുകൾക്ക് ചോദ്യം ചെയ്യാം (ഉദാഹരണം: ഡാറ്റാ അനാലിസിസിന് SQLite ഡാറ്റാബേസില്‍ ചോദ്യമിടൽ, സ്റ്റോക്ക് വിലകൾ അല്ലെങ്കിൽ കാലാവസ്ഥ വിവരങ്ങൾ എടുക്കൽ).
- **കോഡ് നടപ്പാക്കലും വ്യാഖ്യാനവും:** ഗണിത പ്രശ്നങ്ങൾ പരിഹരിക്കാൻ, റിപ്പോർട്ടുകൾ സൃഷ്ടിക്കാൻ, അല്ലെങ്കിൽ സിമുലേഷനുകൾ നടത്താൻ ഏജന്റുകൾ കോഡ് അല്ലെങ്കിൽ സ്ക്രിപ്റ്റുകൾ 실행 ചെയ്യാം.
- **വർക്ക്ഫ്ലോ ഓട്ടോമേഷൻ:** ടാസ്‌ക് ഷെഡ്യൂളറുകൾ, ഇമെയിൽ സർവിസുകൾ, അല്ലെങ്കിൽ ഡാറ്റ പൈപ്പ്ലൈനുകൾ പോലുള്ള ടൂളുകൾ ഇന്റഗ്രേറ്റ് ചെയ്ത് ആവർത്തനപരമായ അല്ലെങ്കിൽ മൾട്ടി-സ്റ്റെപ് വർക്സ്ഫ്ലോകൾ ഓട്ടോമേറ്റ് ചെയ്യൽ.
- **കസ്റ്റമർ സ്‌പോർട്ട്:** CRM സിസ്റ്റങ്ങൾ, ടിക്കറ്റിങ്ങ് പ്ലാറ്റ്‌ഫോംസ്, അല്ലെങ്കിൽ നോളേജ് ബേസ്സുകളുമായി ബന്ധം സ്ഥാപിച്ച് ഉപയോക്തൃ ചോദികള്‍ പരിഹരിക്കൽ.
- **വസ്തുതവൽകരണം සහ ಎഡിറ്റിംഗ്:** ഗ്രാമർ ചെക്കറുകൾ, ടെകസ്റ്റ് സംഗ്രഹകരങ്ങൾ, അല്ലെങ്കിൽ ഉള്ളടക്ക സുരക്ഷാ മൂല്യനിർണയകരങ്ങൾ പോലുള്ള ടൂളുകൾ ഉപയോഗിച്ച് ഉള്ളടക്ക സൃഷ്ടി സഹായിക്കുക.

## What are the elements/building blocks needed to implement the tool use design pattern?

ഈ ബിൽഡിംഗ് ബ്ലോകുകൾ AI ഏജന്റിന് വ്യാപകമായ ടാസ്കുകൾ നിർവഹിക്കാൻ അനുവദിക്കുന്നു. Tool Use Design Pattern നടപ്പിലാക്കാൻ 필요한 പ്രധാന ഘടകങ്ങൾ ചുവടെ കൊടുക്കുന്നു:

- **Function/Tool Schemas**: ഫംഗ്ഷനുകളുടെ പേര്, ഉദ്ദേശ്യം, ആവശ്യമായ പാരാമീറ്ററുകൾ, പ്രതീക്ഷിക്കുന്ന ഔട്ട്പുട്ടുകൾ എന്നിവ ഉൾപ്പെടെയുള്ള ലഭ്യമായ ടൂളുകളുടെ വിശദമായ നിർവചനങ്ങൾ. ഈ സ്‌ക്കീമകൾ LLM-ന് എവിടെ ടൂളുകൾ ലഭ്യമാണ് എന്നതും സാധുവായ അഭ്യർത്ഥനകൾ എങ്ങനെ നിർമ്മിക്കാമെന്നതും മനസിലാക്കാൻ സഹായിക്കുന്നു.

- **Function Execution Logic**: ഉപയോക്തൃന്റെ ഉദ്ദേശ്യവും സംഭാഷണ സാഹചര്യവുമ അടിസ്ഥാനത്തിൽ എങ്ങനെ, 언제 ടൂളുകൾ വിളിക്കപ്പെടണമെന്ന് നിയന്ത്രിക്കുന്നു. ഇത് പ്ലാനർ മോഡ്യൂൾസ്, റൂട്ടിങ്ങ് മെക്കാനിസങ്ങൾ, അല്ലെങ്കിൽ ടൂൾ ഉപയോഗം ഡൈനാമിക്കായി നിർണയിക്കുന്ന സാമ്പത്തിക പ്രവാഹങ്ങൾ ഉൾക്കൊള്ളാം.

- **Message Handling System**: ഉപയോക്തൃ ഇൻപുട്ടുകൾ, LLM പ്രതികരണങ്ങൾ, ടൂൾ കോളുകൾ, ടൂൾ ഔട്ട്പുട്ടുകൾ എന്നിവയിലെ സംഭാഷണ പ്രവാഹം നിയന്ത്രിക്കുന്ന ഘടകങ്ങൾ.

- **Tool Integration Framework**: ലളിതമായ ഫംഗ്ഷനുകളായോ സങ്കീർണ്ണമായ ബാഹ്യ സർവീസുകളായോ ഉള്ള വിവിധ ടൂളുകളുമായി ഏജന്റ് കണക്ട് ചെയ്യാനുള്ള ഇൻഫ്രാസ്ട്രക്ചർ.

- **Error Handling & Validation**: ടൂൾ 실행ത്തിൽ പരാജയങ്ങൾ കൈകാര്യം ചെയ്യുക, പാരാമീറ്ററുകൾ സാധുവായിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക, അനपेേക്ഷിത പ്രതികരണങ്ങൾ മാനേജ് ചെയ്യുക എന്നവറ.

- **State Management**: സംഭാഷണ സാഹചര്യവും, മുൻപ് നടത്തിയ ടൂൾ ഇടപെടലുകൾ, സ്ഥിരതയുള്ള ഡാറ്റ എന്നിവ ട്രാക്ക് ചെയ്ത് മൾട്ടി-ടേൺ ഇന്ററാക്ഷനുകളിൽ സ്ഥിരത ഉറപ്പാക്കുന്നു.

നിന്ന്, Function/Tool Calling ന്റെ കാര്യത്തിൽ കൂടുതൽ വിശദമായി നോക്കാം.
 
### Function/Tool Calling

Function calling ആണ് വലുത് ഭാഷ മോഡലുകൾ (LLMs) ടൂളുകളുമായി ഇന്ററാക്ഷൻ ചെയ്യുന്നതിനുള്ള പ്രധാന മാർഗം. പുനരാവൃത്തിയുള്ള കോഡിന്റെ ബ്ലോക്കുകൾ ആയ 'functions' ആണ് ഏജന്റുകൾ പ്രവർത്തനങ്ങൾ നിർവഹിക്കാൻ ഉപയോഗിക്കുന്ന 'tools' എന്നതിനാൽ 'Function' എന്നും 'Tool' എന്നും പരസ്പരം ഉപയോഗിക്കുന്നതു സാധാരണമാണ്. ഒരു ഫംഗ്ഷന്റെ കോഡ് വിളിക്കുകയും ചെയ്യാൻ LLM-ന് ഉപയോക്താവിന്റെ അഭ്യർത്ഥന ഫംഗ്ഷൻ വിവരണങ്ങളോടു താരതമ്യം ചെയ്യണം. ഇതിന് ഉപയോഗിക്കുന്നതായാണ് ലഭ്യമായ എല്ലാ ഫംഗ്ഷനുകളുടെ വിവരണങ്ങളുള്ള ഒരു സ്‌കീമ LLM-യ്ക്ക് അയയ്ക്കപ്പെടുന്നത്. LLM പിന്നീട് ടാസ്കിന് ഏറ്റവും അനുയോജ്യമായ ഫംഗ്ഷൻ തിരഞ്ഞെടുക്കുകയും അതിന്റെ പേര് കൂടാതെ ആർഗുമെന്റുകൾ തിരികെ നൽകുകയും ചെയ്യും. തിരഞ്ഞെടുക്കപ്പെട്ട ഫംഗ്ഷൻ വിളിക്കപ്പെടുകയും, അതിന്റെ പ്രതികരണം LLM-ക്ക് തിരികെ അയക്കപ്പെടുകയും ചെയ്ത് LLM അതിന്റെ വിവരങ്ങൾ ഉപയോക്തൃ അഭ്യർത്ഥനയ്ക്ക് പ്രതികരിക്കാൻ ഉപയോഗിക്കുന്നു.

ഡെവലപ്പർമാർക്ക് ഏജന്റുകൾക്കായി ഫംഗ്ഷൻ കോളിംഗ് നടപ്പിലാക്കാൻ, നിങ്ങളുടെ কাছে ആവശ്യമായിരിക്കുന്നത്:

1. ഫംഗ്ഷൻ കോളിംഗ് പിന്തുണക്കുന്ന LLM മോഡൽ
2. ഫംഗ്ഷൻ വിവരണങ്ങൾ അടങ്ങിയ ഒരു സ്‌കീമ
3. വിവരണമായ ഓരോ ഫംഗ്ഷനുടെയും കോഡ്

നഗരത്തിലെ ഇപ്പോഴത്തെ സമയമറിയാൻ സ്വീകരിക്കാനുള്ള ഉദാഹരണം ഉപയോഗിക്കാം:

1. **Function calling പിന്തുണക്കുന്ന ഒരു LLM ആരംഭിക്കുക:**

    എല്ലാ മോഡലുകളും ഫംഗ്ഷൻ കോളിംഗ് പിന്തുണയ്ക്കാറില്ല, അതിനാൽ നിങ്ങളുടെ ഉപയോഗിക്കുന്ന LLM ഇത് പിന്തുണയ്ക്കുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക നിർണായകമാണ്.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ഫംഗ്ഷൻ കോളിംഗ് പിന്തുണയ്ക്കുന്നു. നാം ആരംഭിക്കാം Azure OpenAI ക്ലയന്റ് പ്രാരംഭിപ്പിച്ച്.

    ```python
    # Azure OpenAI ക്ലയന്റ് ആരംഭിക്കുക
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Create a Function Schema**:

    അടുത്തതായി നാം ഒരു JSON സ്‌കീമ നിർവചിക്കും, ഇതിൽ ഫംഗ്ഷന്റെ പേര്, ഫംഗ്ഷൻ ചെയ്യുന്നതിന്റെ വിവരണം, ഫംഗ്ഷൻ പാരാമീറ്ററുകളുടെ പേര് și വിവരണങ്ങൾ ഉൾപ്പെടും.
    പിന്നീട് ഈ സ്‌കീമ മുന്‍പ് സൃഷ്ടിച്ച ക്ലയന്റിന്, ഉപയോക്താവിന്റെ സാന്‍ ഫ്രാന്‍സിസ്കോയിലെ സമയം കണ്ടെത്താനുള്ള അഭ്യർത്ഥനയോടൊപ്പം പാസ്സ് ചെയ്യാം. പ്രധാനമായി ശ്രദ്ധിക്കേണ്ടത് ഒരു **tool call** ആണ് തിരികെ നൽകുന്നത്, ചോദ്യത്തിന് അന്തിമ ഉത്തരമല്ല. മുമ്പ് പറഞ്ഞതുപോലെ, LLM ടാസ്കിന് തെരഞ്ഞെടുത്ത ഫംഗ്ഷന്റെ പേര് കൂടാതെ അത് അയക്കാവുന്ന ആർഗുമെന്റുകളും തിരികെ നൽകുന്നു.

    ```python
    # മോഡൽ വായിക്കാൻ ഫംഗ്ഷന്റെ വിവരണം
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
  
    # ആദ്യ ഉപയോക്തൃ സന്ദേശം
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # ആദ്യ API വിളി: മോഡലിനെ ഫംഗ്ഷൻ ഉപയോഗിക്കാൻ അഭ്യർഥിക്കുക
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # മോഡലിന്റെ പ്രതികരണം പ്രക്രിയിക്കുക
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **തസംഭവം നിറവേറ്റാൻ ആവശ്യമായ ഫംഗ്ഷൻ കോഡ്:**

    ഇപ്പോൾ LLM നിർവചിച്ച ഫംഗ്ഷൻ ഏത് എന്ന് തിരഞ്ഞെടുത്തു; ആ ഫംഗ്ഷൻ ഓടിക്കാൻ ആവശ്യമായ കോഡ് നടപ്പിലാക്കുകയും നടത്തുകയും ചെയ്യണം.
    Python ഉപയോഗിച്ച് നഗരത്തിലെ ഇപ്പോഴത്തെ സമയം കണ്ടെത്താൻ കോഡ് നമുക്ക് നടപ്പിലാക്കാം. response_message-ൽ നിന്ന് പേര് आणि ആർഗുമെന്റുകൾ പ്രകാശിപ്പിക്കുന്നതിന് കോഡും നമുക്ക് എഴുതേണ്ടതുണ്ട് ഫൈനൽ ഫലമെടുക്കാൻ.

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
  
      # രണ്ടാം API കോൾ: മോഡൽ നിന്നുള്ള അന്തിമ പ്രതികരണം നേടുക
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

Function Calling ഏജന്റ് ടൂൾ ഉപയോഗ ഡിസൈന്റെ ഹൃദയത്തിലാണ്, പക്ഷേ ഒരു മുതല്‍ പൂരമായുനിന്ന് ഇതിന്റെ നടപ്പാക്കൽ ചിലപ്പോൾ വെല്ലുവിളിയാക്കാം.
നാം [Lesson 2](../../../02-explore-agentic-frameworks) ല്‍ പഠിച്ചതു പോലെ agentic ഫ്രെയിംവർക്കുകൾ ടൂൾ ഉപയോഗം നടപ്പാക്കാൻ മുന്‍കൂട്ടി സജ്ജമാക്കിയ ബിൽഡിംഗ് ബ്ലോകുകൾ നമുക്ക് നൽകുന്നു.
 
## Tool Use Examples with Agentic Frameworks

ഇവയാണ് വിവിധ agentic ഫ്രെയിംവർക്കുകൾ ഉപയോഗിച്ച് Tool Use Design Pattern എങ്ങനെ നടപ്പിലാക്കാമെന്ന് കാണിക്കുന്ന ചില ഉദാഹരണങ്ങൾ:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ഒരു ഓപ്പൺ-സോഴ്‌സ് ഫ്രെയിംവർക്ക് ആണ്. ഇത് `@tool` ഡെക്കോറേറ്റർ ഉപയോഗിച്ച് Python ഫംഗ്ഷനുകളായി ടൂളുകൾ നിർവചിക്കാൻ അനുവദിച്ചുകൊണ്ട് ഫംഗ്ഷൻ കോളിംഗ് ഉപയോഗിക്കുന്നത് ലളിതമാക്കുന്നു. ഫ്രെയിംവർക് മോഡലിനും നിങ്ങളുടെ കോഡിനും തമ്മിലുള്ള മടങ്ങിമറുക ആശയവിനിമയം കൈകാര്യം ചെയ്യുന്നു. കൂടാതെ `AzureAIProjectAgentProvider` മുഖേന File Search, Code Interpreter പോലുള്ള മുൻനിർമ്മിച്ച ടൂൾസുകൾക്കുള്ള ആക്സസ് നൽകുന്നതും ഉള്ളത്.

താഴെയുള്ള ഡ്രോയിംഘ്രാം Microsoft Agent Framework ഉപയോഗിച്ച് ഫംഗ്ഷൻ കോളിംഗ് പ്രക്രിയ ദർശിപ്പിക്കുന്നു:

![ഫംഗ്ഷൻ കോളിംഗ്](../../../translated_images/ml/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework-ൽ ടൂളുകൾ ഡെക്കറേറ്റേഡ് ഫംഗ്ഷനുകളായി നിർവചിക്കപ്പെടുന്നു. നാം മുൻപ് കണ്ട `get_current_time` ഫംഗ്ഷൻ `@tool` ഡെക്കോറേറ്റർ ഉപയോഗിച്ച് ഒരു ടൂളായി മാറ്റാൻ കഴിയും. ഫ്രെയിംവർക്ക് സ്വയം ഫംഗ്ഷൻ അതിന്റെ പാരാമീറ്ററുകൾ എന്നിവ സീരിയലൈസ് ചെയ്ത് LLM-യ്ക്ക് അയക്കാൻ വേണ്ട സ്‌കീമ സൃഷ്ടിക്കും.

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

# ഒരു ഏജന്റ് സൃഷ്ടിച്ച് ടൂൾ ഉപയോഗിച്ച് പ്രവർത്തിപ്പിക്കുക
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> എന്നത് പുതിയൊരു agentic ഫ്രെയിംവർക്കാണ്, ഇത് ഡെവലപ്പർമാർക്ക് അടിസ്ഥാന കംപ്യൂട്ട് ഉം സ്റ്റോറേജ് വിഭവങ്ങൾ നിയന്ത്രിക്കാൻ വേണ്ടാതെ സുരക്ഷിതമായി ഉയർന്ന-ഗുണനിലവാരമുള്ള, വിപുലീകരിക്കാൻ കഴിയുന്ന AI ഏജന്റുകൾ നിർമ്മിക്കാനും ഡിപ്പ്ലോയ് ചെയ്യാനും സ്കേൽ ചെയ്യാനും സഹായിക്കുന്നു. ഇത് പ്രത്യേകിച്ച് എന്റർപ്രൈസ് അപ്ലിക്കേഷനുകൾക്ക് பயനകാരിയാണ് കാരണം ഇത് പൂർണ്ണമായി മാനേജുചെയ്‌ത സർവീസാണ് കൂടാതെ എന്റർപ്രൈസ് ഗ്രേഡ് സുരക്ഷ ലഭ്യമാക്കുന്നു.

LLM API നെ നേരിട്ട് ഉപയോഗിച്ച് വികസിപ്പിക്കുന്നത് when സാന്ദർഭ്യത്തിൽ താരതമ്യിച്ച്, Azure AI Agent Service ചില അനുഭവലാഭങ്ങൾ നൽകുന്നു, അവ:

- സ്വയം ടൂൾ കോളിംഗ് – ഒരു ടൂൾ കോൾ പാഴ്‌സുചെയ്യുന്നതിനും ടൂൾ വിളിച്ച് പ്രതികരണം കൈകാര്യം ചെയ്യുന്നതിനുമുള്ള ആവശ്യം ഇല്ല; ഇവ സർവർ-സൈഡിൽ കൈകാര്യം ചെയ്യപ്പെടും
- സുരക്ഷിതമായി മാനേജുചെയ്യുന്ന ഡാറ്റ – നിങ്ങളുടെ സ്വന്തം സംഭാഷണ സംസ്ഥാനത്തെ മാനേജ് ചെയ്യേണ്ട പകരം, പ്രത്യേക സംഭാഷണത്തിന് വേണ്ട എല്ലാ വിവരങ്ങളും സ്തേർഡ് ചെയ്യാൻ threads ന്മ്മിനെ ആശ്രയിക്കാം
- പ്രത്യക്ഷത്തിലും നേരത്തെ നിർമ്മിച്ച ടൂളുകൾ – Bing, Azure AI Search, Azure Functions പോലുള്ള ഡാറ്റ സ്രോതസുകളുമായി ഇടപഴകാൻ ഉപയോഗിക്കാവുന്ന ടൂളുകൾ

Azure AI Agent Service-ൽ ലഭ്യമായ ടൂളുകൾ രണ്ട് വിഭാഗങ്ങളായി വിഭജിക്കപ്പെടാം:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ഞങ്ങളെ ടെൂൾസെറ്റായി ഈ ടൂളുകൾ ചേർന്ന് ഉപയോഗിക്കാനുള്ള സൗകര്യം അനുവദിക്കുന്നു. കൂടാതെ ഇത് `threads` ഉപയോഗിക്കുന്നു, ഓരോ സംഭാഷണത്തിന്റെയും സന്ദേശ ചരിത്രം ട്രാക്ക് ചെയ്യാൻ സഹായിക്കുന്നു.

നിങ്ങൾ Contoso എന്ന കമ്പനിയിലെ ഒരു സെയിൽസ് ഏജന്റ് ആണ് എന്നു ഉറപ്പിക്കുക. നിങ്ങളുടെ സെയിൽസ് ഡേറ്റയെക്കുറിച്ച് ചോദ്യങ്ങൾക്ക് മറുപടി പറയാൻ കഴിയുന്ന ഒരു സംഭാഷണാത്മക ഏജന്റ് വികസിപ്പിക്കാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നു.

താഴെയുള്ള ചിത്രം Azure AI Agent Service ഉപയോഗിച്ച് നിങ്ങളുടെ സെയിൽസ് ഡാറ്റ വിശകലനം എങ്ങനെ ചെയ്യാമെന്ന് ദർശിപ്പിക്കുന്നു:

![ഏജന്റിക് സർവീസ് പ്രവർത്തനത്തിൽ](../../../translated_images/ml/agent-service-in-action.34fb465c9a84659e.webp)

ഈ സർവീസുമായി ഏതെങ്കിലും ടൂൾ ഉപയോഗിക്കാൻ നാം ഒരു ക്ലയന്റ് സൃഷ്ടിച്ച് ഒരു ടൂൾ അല്ലെങ്കിൽ ടൂൾസെറ്റ് നിർവചിക്കാം. പ്രായോഗികമായി ഇത് നടപ്പിലാക്കാൻ നാം താഴെയുള്ള Python കോഡ് ഉപയോഗിക്കാം. LLM ടൂൾസെറ്റിനെ നോക്കി ഉപയോക്തൃ നിർമ്മിച്ച ഫംഗ്ഷൻ `fetch_sales_data_using_sqlite_query` ഉപയോഗിക്കണോ, അല്ലെങ്കിൽ ഉപയോഗത്തിനനുസരിച്ച് മുൻനിർമ്മിച്ച Code Interpreter ഉപയോഗിക്കണോ എന്ന് തീരുമാനിക്കാൻ കഴിയും.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query എന്ന ഫംഗ്ഷൻ fetch_sales_data_functions.py ഫയലിൽ കാണപ്പെടും.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ടൂൾസെറ്റ് ആരംഭിക്കുക
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ഫംഗ്ഷൻ ഉപയോഗിച്ച് ഫംഗ്ഷൻ കോളിംഗ് ഏജന്റിനെ ആരംഭിച്ച് അത് ടൂൾസെറ്റിൽ ചേർക്കുക
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# കോഡ് ഇന്റർപ്രിറ്റർ ടൂൾ ആരംഭിച്ച് അത് ടൂൾസെറ്റിലേക്ക് ചേർക്കുക.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## What are the special considerations for using the Tool Use Design Pattern to build trustworthy AI agents?

LLM-കൾ സൃഷ്ടിക്കുന്ന ഡൈനാമിക് SQL സംബന്ധിച്ച പൊതുവായ ആശങ്ക бяспекаയുമായി ബന്ധപ്പെട്ടതാണ്, പ്രത്യേകിച്ച് SQL ഇൻജക്ഷൻ അല്ലെങ്കിൽ ദോഷകരമായ പ്രവർത്തനങ്ങൾ, kuten ഡാറ്റാബേസ് ഡ്രോപ്പ് ചെയ്യൽ അല്ലെങ്കിൽ തട്ടുക അടക്കമുള്ള അപകടങ്ങൾ. ഈ ആശങ്കകൾവ്യക്തമാണ്, പക്ഷേ ഡാറ്റാബേസ് ആക്‌സസ് അനുമതികൾ ശരിയായി ക്രമീകരിച്ചാൽ ഇവ ഫലപ്രദമായി ലഘൂകരിക്കാവുന്നതാണ്. പല ഡാറ്റാബേസുകളിലും ഇതിന് സാധാരണയായി ഡാറ്റാബേസ് റീഡ്-ഓൺലി ആയി ക്രമീകരിക്കുകയാണ് ഉൾപ്പെടുന്നത്. PostgreSQL അല്ലെങ്കിൽ Azure SQL പോലുള്ള ഡാറ്റാബേസ് സർവീസുകൾക്കായി ആപ്പ് ഒരു റീഡ്-ഓൺലി (SELECT) റോൾ അനുവദിക്കണമെന്നും.

ആപ്പ് ഒരു സുരക്ഷിത പരിസരത്തിൽ ഓടിച്ചാൽ സുരക്ഷയും വർദ്ധിപ്പിക്കും. എന്റർപ്രൈസ് സാഹചര്യങ്ങളിൽ, സാധാരണയായി പ്രവർത്തന സംവിധാനങ്ങളിൽ നിന്നുള്ള ഡാറ്റ എടുക്കുകയും ട്രാൻസ്ഫോം ചെയ്യുകയും ചെയ്ത് യുസർ-ഫ്രണ്ട്‌ളി സ്‌കീമയുള്ള ഒരു റീഡ്-ഓൺലീ ഡാറ്റാബേസിലേക്കോ ഡാറ്റാത്തോരാഹയില്‍ എത്തിക്കുന്നു. ഈ സമീപനം ഡാറ്റയെ സുരക്ഷിതമാക്കുകയും പ്രകടനക്ഷമതക്കും ആക്സസിബിലിറ്റിക്കും ഒപ്റ്റിമൈസുചെയ്യുകയും ആപ്പിന് പരിമിതമായ, റീഡ്-ഓൺലി ആക്‌സസ് നൽകുകയും ചെയ്യുന്നു.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson
[ഏജന്റിക് RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:
ഈ ഡോക്യുമെന്റ് AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് യന്ത്രപരിഭാഷ ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്രപരിഭാഷകളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവർത്തനങ്ങൾ ഉണ്ടായേക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. മാതൃഭാഷയിലുള്ള മൂല ദസ്താവേയം ആധാരമുള്ളതായാണ് പരിഗണിക്കപ്പെടേണ്ടത്. നിർണ്ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ചതിൽ നിന്നുണ്ടാകുന്ന ഏതൊരു തെറ്റിദ്ധാരണത്തിനും അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനത്തിനും ഞങ്ങൾ ഉത്തരവാദിത്വം വഹിക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->