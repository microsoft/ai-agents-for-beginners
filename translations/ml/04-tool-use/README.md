[![എങ്ങനെ നല്ല AI ഏജന്റ്മാർ ഡിസൈൻ ചെയ്യാം](../../../translated_images/ml/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളിൽ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്യുക)_

# ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ

ടൂളുകൾ അത്രയും രസകലമാണ് കാരണം അവ AI ഏജന്റ്മാർക്ക് വൈവിധ്യമാർന്ന കഴിവുകൾ നൽകുന്നു. ഏജന്റിന് നിർബന്ധിതമായ കുറച്ചു പ്രവർത്തനങ്ങൾ മാത്രം ചെയ്യാനാവാങ്ങൾക്കാതെ, ഒരു ടൂൾ ചേർത്തുകൊണ്ട്, ഏജന്റ് ഇപ്പോൾ വിപുലമായ പ്രവർത്തനങ്ങൾ നടത്താൻ കഴിയും. ഈ അധ്യായത്തിൽ, നാം ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ പരിശോധിക്കാം, ഇത് AI ഏജന്റ്മാർ പ്രത്യേകമായ ടൂളുകൾ ഉപയോഗിച്ച് അവരുടെ ലക്ഷ്യങ്ങൾ കൈവരിക്കാൻ എങ്ങനെ കഴിയും എന്ന് വിവരണം നൽകുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ, നമുക്ക് താഴെ പറയുന്ന ചോദ്യങ്ങൾക്ക് മറുപടി തേടുകയാണ്:

- ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ എന്താണ്?
- ഇത് ഏത് ഉപയോഗ കേസുകളിൽ പ്രയോഗിക്കാമെന്ന്?
- ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാൻ ആവശ്യമായ ഘടകങ്ങൾ/നിർമാണഘടകങ്ങൾ എന്തൊക്കെയാണ്?
- വിശ്വസനീയമായ AI ഏജന്റ്മാർ നിർമ്മിക്കാൻ ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ ഉപയോഗിക്കുമ്പോൾ ഉണ്ടാകുന്ന പ്രത്യേക പരിഗണനകൾ എന്തൊക്കെയാണ്?

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയപ്പോൾ, നിങ്ങൾ കഴിയും:

- ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേണിന്റെ വ്യാഖ്യാനം നൽകാനും അതിന്റെ ലക്ഷ്യം തിരിച്ചറിയാനുമാകുക.
- ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ പ്രയോഗിക്കാൻ കഴിയുന്ന ഉപയോഗ കേസുകൾ തിരിച്ചറിയുക.
- ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കുന്നതിനുള്ള പ്രധാന ഘടകങ്ങൾ മനസ്സിലാക്കുക.
- ഈ ഡിസൈൻ പാറ്റേൺ ഉപയോഗിക്കുന്ന AI ഏജന്റ്മാരിൽ വിശ്വസനീയത ഉറപ്പാക്കുന്നതിനുള്ള പരിഗണനകൾ തിരിച്ചറിയുക.

## ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൻ എന്താണ്?

**ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ** LLM-കൾക്ക് (വലുതും ഭാഷാ മോഡലുകൾ) പ്രത്യേക ലക്ഷ്യങ്ങൾ കൈവരിക്കാൻ ബാഹ്യ ടൂളുകളുമായി ഇടപഴകാനുള്ള കഴിവ് നൽകുന്നതിൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കുന്നു. ടൂളുകൾ ഒരു ഏജന്റ് പ്രവർത്തനങ്ങൾ നടത്താൻ ഓടിക്കാൻ കഴിയുന്ന കോഡുകളാണ്. ഒരു ടൂൾ ലളിതമായ ഒരു ഫങ്ഷൻ ആയി കാണുന്നതാകാം – ഉദാഹരണത്തിന്, കലക്ഷൻ രണ്ടു സംഖ്യകൾ കൂട്ടിയത്, അല്ലെങ്കിൽ എപ്പോഴോ സ്റ്റോക്ക് വില നോക്കൽ പോലുള്ള മൂന്നാം പാർട്ടി സേവനങ്ങൾക്ക് API കോൾ ആയിരിക്കാം. AI ഏജന്റുകളുടെ സੰਦਰഭത്തിലാണ് ടൂളുകൾ പ്രധാനമായും **മോഡൽ-ജനിത ഫങ്ഷൻ കോൾസ്** ന്റെ മറുപടിയോടുകൂടി ഏജന്റുകൾക്ക് പ്രവർത്തൻ നടത്താൻ രൂപകൽപ്പന ചെയ്‌തിരിക്കുന്നത്.

## ഏത് ഉപയോഗ കവിതകൾക്ക് ഇത് പ്രയോഗിക്കാമെന്ന്?

AI ഏജന്റ്മാർ ടൂളുകൾ ഉപയോഗിച്ച് സങ്കീർണ്ണമായ പ്രവർത്തനങ്ങൾ പൂർത്തിയാക്കാൻ, വിവരങ്ങൾ പുനരുദ്ധരിക്കാൻ, അല്ലെങ്കിൽ തീരുമാനങ്ങൾ എടുക്കാൻ കഴിയും. ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ ബാഹ്യ സംവിധാനങ്ങളുമായി സാരവുമായ ഇടപെടൽ ആവശ്യമായ സാഹചര്യങ്ങളിൽ പതിവായി ഉപയോഗിക്കുന്നു, ഉദാഹരണത്തിന് ഡേറ്റാബേസുകൾ, വെബ് സേവനങ്ങൾ, അല്ലെങ്കിൽ കോഡ് വ്യാഖ്യാനകർ. ഈ കഴിവ് പല വിധത്തിലുള്ള ഉപയോഗ കേസുകൾക്കാണ് ഉപയോഗയോഗ്യമായിത്തീർക്കുന്നത്, അതിനാൽ:

- **ഡൈനാമിക് വിവര പുനരുദ്ധരണം:** ഏജന്റുകൾ ബാഹ്യ API-കൾ അല്ലെങ്കിൽ ഡാറ്റാബേസുകൾ ചേർന്ന് പുതിയ വിവരങ്ങൾ ശേഖരിക്കാൻ കഴിയും (ഉദാ: SQLite ഡാറ്റാബേസ് ക്വഡറി ചെയ്ത് ഡാറ്റാ വിശകലനം, സ്റ്റോക്ക് വിലകൾ അല്ലെങ്കിൽ കാലാവസ്ഥ വിവരങ്ങൾ ശേഖരണം).
- **കോഡ് പ്രവർത്തനം, വ്യാഖ്യാനം:** ഗണിതപ്രശ്നങ്ങൾ പരിഹരിക്കാൻ, റിപ്പോർട്ടുകൾ ഉണ്ടാക്കാൻ അല്ലെങ്കിൽ സിമുലേഷൻ നടത്താൻ ഏജന്റുകൾ കോഡ് എഴുതാനും ഓടിക്കാനും കഴിയും.
- **പ്രവൃത്തിപ്രവാഹം സ്വയം><![CDATA[ലാമെന്റേഷൻ**: ടാസ്‌ക് ഷെഡ്യൂളർ, ഇമെയിൽ സേവനങ്ങൾ അല്ലെങ്കിൽ ഡാറ്റ പൈപ്പ്ലൈനുകൾ പോലുള്ള ടൂളുകൾ സംയോജിപ്പിച്ച് ആവർത്തന അല്ലെങ്കിൽ ബഹു-പടി പ്രവൃത്തികളെ സ്വയം നിയന്ത്രിക്കൽ.
- **ഗ്രാഹക പിന്തുണ:** ഏജന്റുകൾ CRM സംവിധാനങ്ങൾ, ടിക്കറ്റ് പ്ലാറ്റ്‌ഫോമുകൾ അല്ലെങ്കിൽ വിജ്ഞാനശേഖരങ്ങൾ വഴി ഉപഭോക്തൃ ചോദ്യങ്ങൾ പരിഹരിക്കാം.
- **കോൺടेंटൊഴുക്ക് നിർമ്മാണവും തിരുത്തലും:** വ്യാകരണപരിശോധകങ്ങൾ, ടെക്സ്റ്റ് സംഗ്രഹകരികൾ അല്ലെങ്കിൽ ഉള്ളടക്ക സുരക്ഷാ നിരീക്ഷകങ്ങൾ പോലുള്ള ടൂളുകൾ ഉപയോഗിച്ച് ഉള്ളടക്കം നിർമ്മാണ പ്രവർത്തനങ്ങളിൽ സഹായിക്കുന്നത്.

## ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാൻ ആവശ്യമുള്ള ഘടകങ്ങൾ/നിർമ്മാണഘടകങ്ങൾ

ഈ നിർമാണ ഘടകങ്ങൾ AI ഏജന്റിന് വ്യാപകമായ പ്രവർത്തനങ്ങൾ നടത്താൻ സഹായിക്കുന്നു. ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ നടപ്പിലാക്കാനുള്ള പ്രധാന ഘടകങ്ങൾ നോക്കാം:

- **ഫങ്ഷൻ/ടൂൾ സ്കീമകൾ:** ലഭ്യമായ ടൂളുകളുടെ വിശദമായ നിർവചനങ്ങൾ, ഫങ്ഷൻ പേര്, ലക്ഷ്യം, ആവശ്യമായ പാരാമീറ്ററുകൾ, പ്രതീക്ഷിച്ച ഔട്ട്‌പുട്ട് എന്നിവ ഉൾപ്പെടുന്നു. ഈ സ്കീമകൾ LLM-കൊരു ലഭ്യമായ ടൂളുകൾ മനസ്സിലാക്കാനും സാധുവായ അഭ്യർത്ഥനകൾ നിർമ്മിക്കാനും സഹായിക്കും.

- **ഫങ്ഷൻ നിർവ്വഹണ ലോജിക്ക്:** ഉപയോക്താവിന്റെ إرادہ സംസാര സാന്ദർഭം അനുസരിച്ച് ടൂളുകൾ എപ്പോഴെത്തെ, എങ്ങനെ വിളിക്കണം എന്ന് നിയന്ത്രിക്കുന്നു. പ്ലാനർ മഡ്യൂളുകൾ, റൂട്ടിംഗ് മെക്കാനിസങ്ങൾ, അല്ലെങ്കിൽ ടൂൾ ഉപയോഗം നിർണ്ണയിക്കുന്ന വ്യവസ്ഥാപിത പ്രവാഹങ്ങൾ ഇതിൽ ഉൾപ്പെടാം.

- **സന്ദേശ കൈകാര്യം എടുക്കൽ സിസ്റ്റം:** ഉപയോക്താവിന്റെ ഇൻപുട്ട്, LLM ප්‍රതിക്രിയകൾ, ടൂൾ കോൾസ്, ടൂൾ ഔട്ട്‌പുട്ടുകൾ എന്നിവ തമ്മിലുള്ള സംവാദ പ്രവാഹം നിയന്ത്രിയ്ക്കുന്ന ഘടകങ്ങൾ.

- **ടൂൾ ഇന്റിഗ്രേഷൻ ഫീറംവർക്ക്:** ഏജന്റിനെ വിവിധ ടൂളുകളുമായി ബന്ധിപ്പിക്കുന്നത്, ആ ടൂളുകൾ ലളിതമായ ഫങ്ഷനുകളായിരിക്കാം അല്ലെങ്കിൽ ജടിലമായ വലിയ ബാഹ്യ സേവനങ്ങളായിരിക്കാം.

- **ഭged്: എന്തെങ്കിലും സാമർത്ഥ്യക്ഷമമല്ലാതെ മോച്ചിച്ചുപോകുകയോ ടൂൾ പ്രവർത്തനത്തിലെ പരാജയങ്ങൾ കൈകാര്യം ചെയ്യുക, പാരാമീറ്ററുകൾ പരിശോധിക്കുക, അനിഷ്ട പ്രതികരണങ്ങൾ നിയന്ത്രിക്കുക.

- **സ്റ്റേറ്റ് മാനേജ്മെന്റ്:** സംവാദ സാന്ദർഭം, കഴിഞ്ഞ ടൂൾ ഇടപെടലുകൾ, സ്ഥിരമായ ഡാറ്റ നിയന്ത്രിച്ച് പല ടേൺ സംവാദങ്ങളിലും ഉറച്ച നിലനിർത്തൽ ചെയ്യുന്നു.

ഇനി, ഫങ്ഷൻ/ടൂൾ കോൾ കൂടുതൽ വിശദമായി പരിഗണിക്കാം.

### ഫങ്ഷൻ/ടൂൾ കോൾ

ഫങ്ഷൻ കോൾ കേസുകളാണ് വികസിപ്പിച്ച വലുതും ഭാഷാ മോഡലുകൾ (LLM) ടൂളുമായി ഇടപഴകാൻ സാദ്ധ്യമാക്കുന്ന പ്രധാന മാർഗം. ‘ഫങ്ഷൻ’ എന്നും ‘ടൂൾ’ എന്നും ഉണ്ടായേക്കാം കാരണം 'ഫങ്ഷൻ' (പുനരുപയോഗയോഗ്യമായ കോഡ് ബ്ലോക്കുകൾ) എന്നതാണ് ഏജന്റുകൾക്ക് പ്രവർത്തനങ്ങൾ നടത്താൻ ഉപയോഗിക്കുന്ന 'ടൂൾ'. ഒരു ഫങ്ഷന്റെ കോഡ് പ്രവർത്തിപ്പിക്കാനായി, LLM ഉപയോക്താവിന്റെ അഭ്യർത്ഥനയെ ഫങ്ഷനം വിശദീകരണവുമായി താരതമ്യം ചെയ്യണം. ഇതിനായി എല്ലാ ലഭ്യമായ ഫങ്ഷനുകൾ വിശദീകരിച്ചിരിക്കുന്ന ഒരു സ്കീമ LLM-൯ അയയ്ക്കുന്നു. തുടർന്ന് LLM ഏറ്റവും അനുയോജ്യമായ ഫങ്ഷനെ തിരഞ്ഞെടുക്കുകയും അതിന്റെ പേര്, പാരാമീറ്ററുകൾ തിരിച്ചയയ്ക്കുകയും ചെയ്യുന്നു. തിരഞ്ഞെടുക്കപ്പെട്ട ഫങ്ഷൻ പ്രവർത്തിപ്പിക്കുകയും, അതിന്റെ പ്രതികരണം LLM-നു വേണ്ടി പറക്കുകയും LLM അതു ഉപയോക്തൃ അഭ്യർത്ഥനയ്ക്ക് മറുപടി നൽകാൻ ഉപയോഗിക്കുകയും ചെയ്യുന്നു.

ഫങ്ഷൻ കോൾ ഏജന്റുകൾക്ക് നടപ്പിലാക്കാൻ നിങ്ങള്ക്ക് ആവശ്യമുള്ളത്:

1. ഫങ്ഷൻ കോൾ പിന്തുണയുള്ള LLM മോഡൽ
2. ഫങ്ഷൻ വിശദീകരണങ്ങൾ ഉൾക്കൊള്ളുന്ന ഒരു സ്കീമ
3. ഓരോ ഫങ്ഷനു വേണ്ട കോഡ്

നഗരത്തിലെ നിലവിലെ സമയം അറിയാനുള്ള ഉദാഹരണമായി ഇത് എടുത്തുകൊണ്ട് കാണിക്കാം:

1. **ഫങ്ഷൻ കോൾ പിന്തുണയുള്ള LLM ആരംഭിക്കുക:**

    എല്ലാ മോഡലുകളും ഫങ്ഷൻ കോൾ പിന്തുണയുള്ളതല്ല, അതിനാൽ നിങ്ങൾ ഉപയോഗിക്കുന്ന LLM ഇത് поддерживает എന്ന് പരിശോധിക്കുക. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ഫങ്ഷൻ കോൾ പിന്തുണക്കുന്നു. ആദ്യം Azure OpenAI ക്ലയന്റ് പ്രാരംഭപ്പെടുത്താം.

    ```python
    # അസ്യൂർ ഓപ്പൺഎഐ ക്ലയന്റിനെ ആരംഭിക്കുക
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ഫങ്ഷൻ സ്കീമ സൃഷ്ടിക്കുക:**

    ഫങ്ഷൻ പേര്, ഫങ്ഷൻ ചെയ്യുന്നത് വിശദീകരണം, ഫങ്ഷൻ പാരാമീറ്ററുകളുടെ പേര്, വിവരണം എന്നിവ ഉള്‍പ്പെടുത്തുന്ന JSON സ്കീമ നിർവചിക്കുന്നു.
    പിന്നീട് ഈ സ്കീമ മുമ്പ് സൃഷ്ടിച്ച ക്ലയന്റിനും, ഉപയോക്താവിന്റെ അഭ്യർത്ഥനയെയും (സാൻ ഫ്രാൻസിസ്കോയിൽ സമയം കാണിക്കൽ) അയയ്ക്കും. ശ്രദ്ധിക്കാനുള്ള കാര്യം: **ടൂൾ കോൾ** ആണ് മടക്കമാകുന്നത്, ചോദ്യത്തിന് തുകത്തിലുള്ള മറുപടി അല്ല. മുൻപ് പറഞ്ഞതുപോലെ, LLM ഫങ്ഷൻലെ തുടർവാർത്തയും അതിന്റെ_ARGUMENTസും തിരിച്ചയയ്ക്കുന്നു.

    ```python
    # മോഡൽ വായിക്കാൻ പ്രവർത്തനം വിവരണം
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
  
    # ആദ്യ API کال്: മോഡലോട് ഫംഗ്ഷൻ ഉപയോഗിക്കാൻ ആവശ്യപ്പെടുക
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
  
1. **ഈ ഫങ്ഷൻ പ്രവർത്തിപ്പിക്കുന്ന കോഡ്:**

    LLM സ്ഥിതിമാറ്റിപ്പിച്ചതിനുശേഷം, ഫങ്ഷൻ പ്രവർത്തിപ്പിക്കുന്ന കോഡ് നടപ്പിലാക്കുകയും ഓടിക്കുകയും വേണം.
    നാം Python-ൽ സിറ്റി നിലവിലെ സമയം എടുക്കുന്ന കോഡ് നടപ്പിലാക്കാം. മറുപടി സന്ദേശത്തിൽ നിന്ന് പേര്,_ARGUMENTസ് പിടിച്ച് അവസാന ഫലം ലഭിക്കുന്ന കോഡും എഴുതണം.

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
     # ഫംഗ്ഷന്‍ വിളികളെ കൈകാര്യം ചെയ്യുക
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
  
      # രണ്ടാം API വിളി: മോഡലിൽ നിന്ന് അന്തിമ പ്രതികരണം നേടുക
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

ഫങ്ഷൻ കോൾ ഏജന്റുകളുടെ ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേണിന്റെ മൂള കിണറാണ്, എങ്കിലും ഇത് ഒന്നൊന്നായി ആരാഞ്ഞ് നിർമ്മിക്കുമ്പോൾ ചിലപ്പോൾ വെല്ലുവിളികളുണ്ടാകാം.
[Lesson 2](../../../02-explore-agentic-frameworks) ൽ പഠിച്ച പോലെ, ഏജന്റിക് ഫ്രെയിമ്വർക്കുകൾ നമുക്ക് ടൂൾ ഉപയോഗത്തിൽ ആവശ്യമായ നിർമ്മാണഘടകങ്ങൾ മുൻകൈ അധിഷ്ഠിതമായി നൽകുന്നു.

## ഏജന്റിക് ഫ്രെയിംവർക്കുകളുമായി ടൂൾ ഉപയോഗ ഉദാഹരണങ്ങൾ

വിവിധ ഏജന്റിക് ഫ്രെയിംവർക്കുകൾ ഉപയോഗിച്ച് ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ എങ്ങനെ നടപ്പിലാക്കാമെന്ന് ചില ഉദാഹരണങ്ങൾ:

### സെമാന്റിക് കർണൽ

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">സെമാന്റിക് കർണൽ</a> .NET, Python, Java ഡെവലപ്പർമാർക്കായി LLM എളുപ്പമായ ഫങ്ഷൻ കോൾ ഉപയോഗത്തിന് രൂപകൽപ്പന ചെയ്‌ത ഒരു ഓപ്പൺ സോഴ്‌സ് AI ഫ്രെയിംവർക്ക് ആണ്. ഫങ്ഷനുകൾ, അവയുടെ പാരാമീറ്ററുകൾ മോഡലിലേക്ക് <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">സീരിയലൈസ്</a> എന്ന പ്രക്രിയ വഴി സ്വയം വിവരിക്കുകയും മോഡലും നിങ്ങളുടെ കോഡും തമ്മിലുള്ള ആശയവിനിമയം സ്വകൃതമായി കൈകാര്യം ചെയ്യുകയും ചെയ്യുന്നു. സെമാന്റിക് കർണൽ പോലുള്ള ഏജന്റിക് ഫ്രെയിംവർക്ക് ഉപയോഗിക്കുന്ന മറ്റൊരു ഗുണം, <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">ഫയൽ ശോധന</a>, <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">കോഡ് വ്യാഖ്യാനകർ</a> പോലുള്ള മുൻകൈ ടൂളുകൾ ലഭ്യമാകുന്നു.

താഴെ കൊടുത്ത ചിത്രം സെമാന്റിക് കർണലിൽ ഫങ്ഷൻ കോൾ പ്രക്രിയയെ വിശദീകരിക്കുന്നു:

![function calling](../../../translated_images/ml/functioncalling-diagram.a84006fc287f6014.webp)

സെമാന്റിക് കർണൽ-ൽ ഫങ്ഷനുകൾ/ടൂളുകൾ <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">പ്ലഗിൻ</a>സ് എന്നറിയപ്പെടുന്നു. മുൻപ് കണ്ട `get_current_time` ഫങ്ഷൻ ക്ലാസ്സാക്ഷരമായ പ്ലഗിനായി മാറ്റാം. `kernel_function` ഡെക്കറേറ്ററെയും ഇറക്കുമതി ചെയ്യാം, അത് ഫങ്ഷന്റെ വിവരണം സ്വീകരിക്കുന്നു. GetCurrentTimePlugin ഉപയോഗിച്ച് കർണൽ രൂപപ്പെടുത്തുമ്പോൾ, കർണൽ സ്വയമേവ ഫങ്ഷനും പാരാമീറ്ററുകളും സീരിയലൈസ് ചെയ്ത് LLM-നയയ്ക്കേണ്ട സ്കീമ നിർമ്മിക്കും.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# കർണൽ സൃഷ്ടിക്കുക
kernel = Kernel()

# പ്ലഗിൻ സൃഷ്ടിക്കുക
get_current_time_plugin = GetCurrentTimePlugin(location)

# പ്ലഗിൻ കർണലിൽ ചേർക്കുക
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> പുതിയ ഒരു ഏജന്റിക് ഫ്രെയിംവർക്ക് ആണ്, വികസിപ്പകർക്ക് സുരക്ഷിതമായി ഉയർന്ന നിലവാരമുള്ള, വിപുലീകരണ സാധ്യമായ AI ഏജന്റുകൾ നിർമ്മിക്കുകയും വിനിയോഗിക്കുകയും സ്കെയിൽ ചെയ്യുകയും ചെയ്യാൻ സഹായിക്കുന്നു. അടിസ്ഥാന കമ്പ്യൂട്ട്, സ്റ്റോറേജ് വിഭവങ്ങൾ കൈകാര്യം ചെയ്യേണ്ടതില്ല. ഇത് എന്റർപ്രൈസ് ആപ്ലിക്കേഷനുകൾക്ക് ഏറെ പ്രയോജനകരമാണ്, സ്ഥാപന നിലവാരമുള്ള സുരക്ഷയോട് കൂടിയിരിക്കുന്ന മൊത്തം മാനേജ്ചെയ്ത സേവനമാണ്.

നേരിട്ട് LLM API ഉപയോഗിക്കുന്നതുമായി താരതമ്യപ്പെടുത്തുമ്പോൾ, Azure AI Agent Service ചില നേട്ടങ്ങൾ നൽകുന്നു:

- സ്വയം ടൂൾ കോൾ ചെയ്യൽ – ടൂൾ കോൾ വിശകലനം ചെയ്ത്, ടൂൾ വിളിച്ച്, മറുപടി കൈകാര്യം ചെയ്യുന്നതിനുള്ള പ്രക്രിയകൾ എല്ലാ സെർവർ-ഭാഗത്തായി നടപ്പിലാക്കുന്നു
- സുരക്ഷിതമായി കൈകാര്യം ചെയ്‌ത ഡേറ്റ – നിങ്ങളുടെ സംവാദ നില മാനേജ്ജ് ചെയ്യലിന് പകരം, ട്രെഡ്‌സ് ഉപയോഗിച്ച് എല്ലാ ആവശ്യമായ വിവരങ്ങളും സൂക്ഷിക്കുന്നു
- പുറംണുകളിൽ ടൂളുകൾ – Bing, Azure AI Search, Azure Functions തുടങ്ങിയ ഡാറ്റയുമായി സംവദിക്കാൻ ഉപയോഗിക്കാവുന്ന ടൂളുകൾ

Azure AI Agent Service ഉള്ള ടൂളുകൾ ഈ രണ്ട് വിഭാഗങ്ങളായി വിഭജിക്കാം:

1. അറിവ് ടൂളുകൾ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search-ൽ ഗ്രൗണ്ടിംഗ്</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ഫയൽ ശോധന</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. പ്രവർത്തന ടൂളുകൾ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ഫങ്ഷൻ കോൾ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">കോഡ് വ്യാഖ്യാനകൻ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI നിർവ്വചിച്ച ടൂളുകൾ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ഈ ടൂളുകൾ `toolset` ആയി ഒരുസഹിതമാക്കി ഉപയോഗിക്കാനാകും. നിഗമനമായി, `threads` ഉപയോഗിച്ച് ഒരു പ്രത്യേക സംവാദത്തിലെ സന്ദേശപ്പശ്ചാത്തല ചരിത്രം സൂക്ഷിക്കുകയും ചെയ്യും.

നിങ്ങൾ Contoso എന്ന കമ്പനിയിൽ ഒരു സെയിൽസ് ഏജന്റാണ് എന്നു കരുതുക. നിങ്ങളുടെ സെയിൽസ് ഡാറ്റയെക്കുറിച്ച് ചോദ്യങ്ങൾക്ക് മറുപടി നൽകാൻ കഴിവുള്ള ഒരു സംവാദ ഏജന്റ് വികസിപ്പിക്കാൻ ആഗ്രഹിക്കുന്നു.

താഴെ കാണുന്ന ചിത്രം Azure AI Agent Service ഉപയോഗിച്ച് സെയിൽസ് ഡാറ്റ ആനാലിസിസ് എങ്ങനെ നടത്താമെന്ന് കാണിക്കുന്നു:

![Agentic Service In Action](../../../translated_images/ml/agent-service-in-action.34fb465c9a84659e.webp)

ഈ ടൂളുകൾ ഏത് ഉപയോഗിച്ച് സേവനം ഉപയോഗിക്കാൻ, ക്ലയന്റ് സൃഷ്ടിക്കുകയും ഒരു ടൂൾ അല്ലെങ്കിൽ ടൂൾസെറ്റ് നിർവചിക്കുകയും ചെയ്യാം. പ്രായോഗികമായി നടപ്പിലാക്കാൻ താഴെയുള്ള Python കോഡ് ഉപയോഗിക്കാം. LLM ടൂൾസെറ്റ് പരിശോധിച്ച് ഉപയോക്താവ് സൃഷ്ടിച്ച `fetch_sales_data_using_sqlite_query` ഫങ്ഷൻ ആണോ, മുൻകൈ കോഡ് വ്യാഖ്യാനകരാണോ ഉപയോഗിക്കേണ്ടത് തീരുമാനിക്കും.

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

# ടൂൾസെറ്റ് ആമുഖപ്പെടുത്തുക
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ഫംഗ്ഷനോടൊപ്പം ഫംഗ്ഷൻ കോളിംഗ് ഏജന്റ് ആമുഖപ്പെടുത്തുകയും അത് ടൂൾസെറ്റിൽ ചേർക്കുക.
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# കോഡ് ഇൻറർപ്രീറ്റർ ടൂൾ ആമുഖപ്പെടുത്തുകയും അതിനെ ടൂൾസെറ്റിൽ ചേർക്കുകയും ചെയ്യുക.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## വിശ്വസനീയമായ AI ഏജന്റ്മാർ നിർമ്മിക്കാൻ ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ ഉപയോഗിക്കുമ്പോൾ പ്രത്യേക പരിഗണനകൾ എന്തൊക്കെയാണ്?

LLM-കൾ വഴി ഡൈനാമിക് ആയി ജനറേറ്റ് ചെയ്യുന്ന SQL-ലുള്ള സാധാരണ ആശങ്ക സെകയ്യൂരിറ്റിയാണ്, പ്രത്യേകിച്ച് SQL എൻജക്ഷൻ അല്ലെങ്കിൽ ദുഷ്പ്രഭാവങ്ങൾ (ഡേറ്റാബേസ് ഡ്രോപ്പ് ചെയ്യൽ അല്ലെങ്കിൽ കൃത്രിമം) പോലുള്ള അപകടങ്ങൾ. ഈ ആശങ്കകൾ വാസ്തവമാണ്, എങ്കിലും ശരിയായ ഡേറ്റാബേസ് ആക്‌സസ് അനുവാദങ്ങൾ ക്രമീകരിച്ചാൽ ഫലപ്രദമായി നിയന്ത്രിക്കാവുന്നതാണ്. അധികം ഡേറ്റാബേസുകൾ റീഡ്-ഓൺലി ആകാൻ ക്രമീകരിക്കപ്പെടുന്നുണ്ട്. PostgreSQL അല്ലെങ്കിൽ Azure SQL പോലുള്ള ഡേറ്റാബേസ് സർവീസുകൾക്കായി, ആപ്പ് റീഡ്-ഓൺലി (SELECT) റോളുകൾ നൽകണം.
ആപ്ലിക്കേഷൻ സുരക്ഷിതമായ അന്തരീക്ഷത്തിൽ പ്രവർത്തിപ്പിക്കുന്നത് സംരക്ഷണം കൂടുതൽ മെച്ചപ്പെടുത്തുന്നു. സംരംഭ ഘടകങ്ങളിൽ, ഡാറ്റ സാധാരണയായി ഓപ്പറേഷണൽ സിസ്റ്റങ്ങൾ മുതലായവയിൽ നിന്ന് എടുത്ത് മാറ്റി, വായിക്ക-only ഡാറ്റാബേസ് അല്ലെങ്കിൽ ഡാറ്റാ വെർഹൗസിലോ, ഉപയോക്തൃ സൗഹൃദ സ്കീമയിലോ മാറ്റാവുന്ന രീതിയിൽ പരിവർത്തനം ചെയ്യപ്പെടുന്നു. ഈ സമീപനം ഡാറ്റ സുരക്ഷിതവും പ്രകടനക്ഷമവുമായിരിക്കും എന്നു ഉറപ്പാക്കുക എന്നതോടൊപ്പം ആപ്പിന് പരിധിയിട്ട, വായിക്ക-only ആക്‌സസ് ലഭിക്കും.

## സാമ്പിൾ കോഡുകൾ

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ഉപകരണ ഉപയോഗ ഡിസൈൻ പാറ്റേണുകളെക്കുറിച്ചുള്ള കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

മറ്റുള്ള പഠനാർത്ഥികളോടൊപ്പം കൂടാന്‍, ഓഫീസ് മണിക്കൂറുകളിൽ പങ്കെടുക്കാനും നിങ്ങളുടെ AI ഏജന്റുകളുമായി ബന്ധപ്പെട്ട ചോദ്യങ്ങൾക്ക് മറുപടി അറിയാനും [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ൽ ചേരുക.

## അധിക വിഭവങ്ങൾ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## നാജ പ്രധാന പാഠം

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## അടുത്ത പാഠം

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസാധുവാക്കൽ**:  
ഈ ഡോക്യൂമെന്റ് AI വിവർത്തന സേവനായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യത ലക്ഷ്യമിടുന്നുവെങ്കിലും, സ്വയമേറ്റ വിവർത്തനങ്ങളിൽ പിശകുകളോ അംഗീകരിക്കാത്ത അസ്ഥിരതകളോ ഉണ്ടാകാം എന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൂലഭാഷയിലെ യഥാര്‍ഥ ഡോക്യൂമെന്റേയാണ് അധികാരപരമായി അംഗീകരിക്കേണ്ടതെന്നും ശ്രദ്ധിക്കുക. പ്രധാന വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം നിർദ്ദേശിക്കപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന തെറ്റായ ബോധ്യങ്ങളോ അർത്ഥകല്പനകളോ സംബന്ധിച്ച് ഞങ്ങൾ ഉത്തരവാദിത്വം വഹിക്കുന്നതല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->