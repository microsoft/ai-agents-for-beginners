[![AI ഏജന്റ് ഫ്രെയിംവർക്സ് പരിശോധിക്കുന്നു](../../../translated_images/ml/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളിൽ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്യുക)_

# AI ഏജന്റ് ഫ്രെയിംവർക്സ് അന്വേഷിക്കുക

AI ഏജന്റ് ഫ്രെയിംവർകുകൾ AI ഏജന്റുകളുടെ സൃഷ്ടി, വിന്യസനം, മാനേജ്മെന്റ് എളുപ്പമാക്കാൻ രൂപകൽപ്പന ചെയ്ത സോഫ്റ്റ്‌വെയർ പ്ലാറ്റ്ഫോമാണ്. സങ്കീർണമായ AI സിസ്റ്റങ്ങൾ വികസിപ്പിക്കാനുള്ള മുൻകൂട്ടി നിർമ്മിച്ച ഘടകങ്ങൾ, സമരൂപീകരണങ്ങൾ, ഉപകരണങ്ങൾ വികസിപ്പകർക്ക് നൽകുന്നു.

AI ഏജന്റ് വികസന中的 സാധാരണ വെല്ലുവിളികൾക്ക് സ്റ്റാൻഡേർഡൈസ്ഡ് സമീപനങ്ങൾ നൽകുന്നതിലൂടെ ഈ ഫ്രെയിംവർകുകൾ ഡെവലപ്പർമാരെ അവരുടെ അപ്ലിക്കേഷനുകളിലെ പ്രത്യേക ഭാഗങ്ങളിൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കാൻ സഹായിക്കുന്നു. ഇവ AI സിസ്റ്റങ്ങൾ നിർമ്മിക്കുന്നതിനുള്ള സ്കെയിലബിലിറ്റി, എത്തിനിടത്തും, കാര്യക്ഷമത ഉയർത്തുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ ഉൾപ്പെടുത്തുന്നത്:

- AI ഏജന്റ് ഫ്രെയിംവർകുകളെന്താണ്, ഡെവലപ്പർമാർക്ക് എന്ത് സാധ്യമാകും?
- ടീമുകൾ എങ്ങനെ ഇവ ഉപയോഗിച്ച് അവരുടെ ഏജന്റിന്റെ കഴിവുകൾ വേഗത്തിൽ പ്രോട്ടോട്ടൈപ്പ് ചെയ്ത് മെച്ചപ്പെടുത്താം?
- <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> എന്നും <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a> എന്ന Microsoft's സൃഷ്ടികളിൽ有什么 വ്യത്യാസങ്ങളുണ്ട്?
- എന്റെ നിലവിലുള്ള Azure ഇക്കോസിസ്റ്റം ഉപകരണങ്ങൾ നേരിട്ട് ഇന്റഗ്രേറ്റ് ചെയ്യാമോ, അല്ലെങ്കിൽ സ്റ്റാൻഡലോൺ സോല്യൂഷനുകൾ വേണമോ?
- Azure AI Agent Service എന്താണ്, ഇത് എനിക്ക് എങ്ങനെ സഹായിക്കുന്നു?

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം നിങ്ങളുടെ മനസിലാക്കുവാനുള്ള സഹായം ചെയ്യും:

- AI വികസനത്തിലെ AI ഏജന്റ് ഫ്രെയിംവർകുകളുടെ പങ്ക്.
- ഐ.ஐ ഏജന്റ് ഫ്രെയിംവർകുകൾ ഉപയോഗിച്ച് ബുദ്ധിമാൻ ഏജന്റുകൾ നിർമ്മിക്കുന്ന വിധം.
- AI ഏജന്റ് ഫ്രെയിംവർകുകൾ വഴി സാധ്യമാകുന്ന പ്രധാന കഴിവുകൾ.
- Microsoft Agent Framework-നും Azure AI Agent Service-നും ഇടയിലെ വ്യത്യാസങ്ങൾ.

## AI ഏജന്റ് ഫ്രെയിംവർകുകൾ എന്ത്? ഡെവലപ്പർമാർക്ക് എന്ത് ചെയ്യാൻ അനുവദിക്കുന്നു?

പരമ്പരാഗത AI ഫ്രെയിംവർകുകൾ നിങ്ങളുടെ ആപ്പുകളിൽ AI ഇന്റഗ്രേറ്റ് ചെയ്യാനും ആ ആപ്പുകൾ മെച്ചപ്പെടുത്താനും സഹായിക്കുന്നു:

- **വ്യക്തിഗതമാക്കൽ**: ഉപയോക്തൃ പെരുമാറ്റവും മുൻഗണനകളും വിശകലനം ചെയ്ത് വ്യക്തിഗത ശുപാർശകൾ, ഉള്ളടക്കം, അനുഭവങ്ങൾ നൽകുന്നു.
ഉദാഹരണം: Netflix പോലുള്ള സ്ട്രീമിംഗ് സേവനങ്ങൾ നോക്കിയFilm ചരിത്രം അടിസ്ഥാനമാക്കി സിനിമകൾ, ഷോകൾ ശുപാർശ ചെയ്ത് ഉപയോക്തൃ പങ്കാളിത്തം വർധിപ്പിക്കുന്നു.
- **സ്വയമേവ പ്രവർത്തനം, കാര്യക്ഷമത**: ആവർത്തിക്കുന്ന ജോലിയാക автоматически ചെയ്തുകൊണ്ട് പ്രവൃത്തി പ്രവാഹങ്ങൾ സുഗമമാക്കുകയും പ്രവർത്തന കാര്യക്ഷമത മെച്ചപ്പെടുത്തുകയും ചെയ്യുന്നു.
ഉദാഹരണം: കസ്റ്റമർ സർവീസ് ആപ്പുകൾ എളുപ്പപ്രശ്‌നങ്ങൾക്ക് AI ചാറ്റ്ബോട്ടുകൾ ഉപയോഗിച്ച് മനുഷ്യ ഏജന്റുകളുടെ സമയവഞ്ചന കുറയ്ക്കുന്നു.
- **ഉപയോക്തൃ അനുഭവം മെച്ചപ്പെടുത്തൽ**: ശബ്ദം തിരിച്ചറിയൽ, പ്രാകൃത ഭാഷാ പ്രോസസിങ്, പ്രവാചക എഴുത്ത് പോലുള്ള ബുദ്ധിമാനായ സവിശേഷതകൾ നൽകുന്നു.
ഉദാഹരണം: Siri, Google Assistant പോലുള്ള വെർച്വൽ അസിസ്റ്റന്റുകൾ ശബ്ദ കമാൻഡുകൾ മനസിലാക്കി പ്രതികരിച്ച് ഉപയോക്താക്കളെ സഹായിക്കുന്നു.

### എല്ലാം നല്ലതാണ്, എങ്കിൽ AI ഏജന്റ് ഫ്രെയിംവർകുകൾക്ക് എന്ത് ആവശ്യമാണ്?

AI Agent ഫ്രെയിംവർകുകൾ സാധാരണ AI ഫ്രെയിംവർകുകൾക്കുമപ്പുറമാണ്. ഉപയോക്താക്കളുമായി, മറ്റ് ഏജന്റുകളുമായി, പരിതസ്ഥിതിയുമായി സംവദിച്ച് പ്രത്യയശാസ്ത്രീയ ലക്ഷ്യങ്ങൾ നേടാൻ കഴിയുന്ന ബുദ്ധിമാനായ ഏജന്റുകളെ സൃഷ്ടിക്കാനുള്ള സഹായമാണ്. ഈ ഏജന്റുകൾ സ്വയം സ്വഭാവം കാണിക്കുകയും, തീരുമാനങ്ങൾ എടുക്കുകയും, പരിസ്ഥിതിയിലെ മാറ്റങ്ങൾ അനുസരിക്കുകയും ചെയ്യും. താഴെ ചില പ്രധാന കഴിവുകൾ:

- **ഏജന്റ് സഹകരണം, കോർഡിനേഷൻ**: ബഹുഏജന്റ് സൃഷ്ടിച്ച് സംവദിക്കുകയും കൂട്ടായ്‌മ ചെയ്ത് സങ്കീർണ ജോലികൾ പരിഹരിക്കാനും സാധിക്കും.
- **ജോലി സ്വയംമാറ്റം, മാനേജ്മെന്റ്**: ബഹു-പടിയോയുള്ള പ്രവൃത്തി ഒഴുക്കുകൾ സ്വയം നിയന്ത്രിക്കുകയും ഏജന്റുകൾ മദ്ധ്യേ ജോലികൾ ചുമത്തിലാക്കുകയും നിയന്ത്രിക്കുകയും ചെയ്യാം.
- **പരിസരാന്തര വ്യാഖ്യാനം, ഒത്തുപോകൽ**: ഏജന്റുകൾക്ക് സാഹചര്യങ്ങൾ മനസിലാക്കാനും, അതിനനുസരിച്ച് പ്രവർത്തിക്കാനും, വാസ്തവ സമയ വിവരങ്ങളുടെ അടിസ്ഥാനത്തിൽ തീരുമാനങ്ങൾ എടുക്കാനും കഴിയും.

സംഗ്രഹത്തോടെ പറഞ്ഞാൽ, ഏജന്റുകൾ കൂടുതൽ സാധ്യമാക്കുന്നു, ഓട്ടോമേഷന്റെ നിലവാരം കൂട്ടുന്നു, പരിസ്ഥിതിയിൽ നിന്നും പഠിച്ചും ഒത്തുപോയും കൂടുതൽ ബുദ്ധിമാനായ സിസ്റ്റങ്ങൾ നിർമ്മിക്കാൻ സഹായിക്കുന്നു.

## ഏജന്റിന്റെ കഴിവുകൾ എങ്ങനെ വേഗത്തിൽ പ്രോട്ടോട്ടൈപ്പ്, പുനഃസംസ്‌ക്കരണം, മെച്ചപ്പെടുത്താം?

ഈ രംഗം വേഗത്തിൽ മാറുകയാണ്, എങ്കിലും ഭൂരിഭാഗം AI ഏജന്റ് ഫ്രെയിംവർകുകളിലും പൊതുവായ ചില ഘടകങ്ങൾ ഉണ്ട്: മോഡ്യുലാർ ഘടകങ്ങൾ, സഹകരണ ഉപകരണങ്ങൾ, യഥാർത്ഥ-സമയം പഠനം. അവയെക്കുറിച്ച്:

- **മോഡ്യുലാർ ഘടകങ്ങൾ ഉപയോഗിക്കുക**: AI SDKകൾ മുൻകൂട്ടി നിർമ്മിച്ച AI, മെമ്മറി കണക്റ്ററുകൾ, Functions നിശ്ചയം സ്വഭാവത്തിലുള്ള Plugins, Prompt ട്യാമ്പ്ൾറ്റുകൾ എന്നിവ വാഗ്ദാനം ചെയ്യുന്നു.
- **സഹകരണ ഉപകരണങ്ങൾ പ്രയോജനപ്പെടുത്തുക**: നിർദ്ദിഷ്ട പദവികളും ജോലികളും ഉള്ള ഏജന്റുകൾ രൂപകൽപ്പന ചെയ്ത് സഹകരണം പരീക്ഷിച്ച് മെച്ചപ്പെടുത്തുക.
- **യഥാർത്ഥ-സമയം പഠനം**: ഏജന്റുകൾ ഇടപെടലുകളിൽ നിന്നും പഠിച്ച് ഒന്നടങ്കം സ്വഭാവം ക്രമീകരിക്കുന്ന ഫീഡ്ബാക്ക് ലൂപ്പുകൾ നടപ്പിലാക്കുക.

### മോഡ്യുലാർ ഘടകങ്ങൾ ഉപയോഗിക്കുക

Microsoft Agent Framework പോലുളള SDKകൾ മുൻകൂട്ടി നിർമ്മിച്ച AI കണക്റ്ററുകൾ, ഉപകരണ നിർവചനങ്ങൾ, ഏജന്റ് മാനേജ്മെന്റ് എന്നിവ നൽകുന്നു.

**ടീമുകൾ എങ്ങനെയാണ് ഉപയോഗിക്കുന്നത്**: ടീമുകൾ പ്രവർത്തനക്ഷമമായ പ്രോട്ടോട്ടൈപ്പ് വേഗത്തിൽ സംയോജിപ്പിച്ച് പരീക്ഷണവും പുനഃസംസ്‌കരണവും നടത്താം.

**പ്രയോഗത്തിൽ എങ്ങനെ പ്രവർത്തിക്കുന്നു**: ഉപയോക്തൃ ഇൻപുട്ടിൽ നിന്ന് വിവരങ്ങൾ എടുക്കാൻ മുൻകൂട്ടി നിർമ്മിച്ച പാഴ്സർ ഉപയോഗിക്കാം, ഡേറ്റ സംഭരണം/പ്രതിച്ച്ഛേദനം നടത്താൻ മെമ്മറി ഘടകം, ഉപയോക്താവുമായി സംവദിക്കാൻ പ്രോമ്പ് ജനറേറ്ററും, എല്ലാം സൃഷ്ടിക്കാതെ ഉപയോഗിക്കാം.

**കോഡ് ഉദാഹരണം**. Microsoft Agent Framework ഉപയോഗിച്ച് `AzureAIProjectAgentProvider` എന്നയാളിൽ ഉപയോക്തൃ ഇൻപുട്ട് ടൂൾ കോൾ ഉപയോഗിച്ച് പ്രതികരിക്കാൻ ഒരു ഉദാഹരണം:

``` python
# Microsoft Agent Framework പൈതൺ ഉദാഹരണം

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# യാത്ര ബുക്ക് ചെയ്യുന്നതിനുള്ള ഒരു സാമ്പിൾ ടൂൾ ഫംഗ്ഷൻ നിർവചിക്കുക
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # ഉദാഹരണ ഔട്ട്‌പുട്ട്: 2025 ജനുവരി 1-ന് ന്യൂയോർക്കിലേക്ക് നിങ്ങളുടെ ഫ്ലൈറ്റ് വിജയകരമായി ബുക്ക് ചെയ്തു. സുരക്ഷിത യാത്രകൾ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ഈ ഉദാഹരണത്തിൽ കാണുന്നത് ഉപയോക്തൃ ഇൻപുട്ടിൽ നിന്നുള്ള പ്രധാന വിവരങ്ങൾ (ആദ്യസ്ഥാനം, ഗമ്യസ്ഥാനം, തീയതി) എടുത്തെടുക്കാൻ മുൻകൂട്ടി നിർമ്മിച്ച പാഴ്സർ ഉപയോഗിക്കുന്ന വിധമാണ്. ഈ മോഡുലാർ സമീപനം ഉയർന്ന തലത്തിലുള്ള ലോജിക് കുറിച്ച് ശ്രദ്ധ കേന്ദ്രീകരിക്കാൻ അനുവദിക്കുന്നു.

### സഹകരണ ഉപകരണങ്ങൾ പ്രയോജനപ്പെടുത്തുക

Microsoft Agent Framework പോലുള്ള ഫ്രെയിംവർകുകൾ ഒരുപാട് ഏജന്റുകളെ കൂട്ടായ്മയിൽ പ്രവർത്തിക്കാൻ സഹായിക്കുന്നു.

**ടീമുകൾ എങ്ങനെ ഉപയോഗിക്കും**: പ്രത്യേക പദവിയും ജോലികളും ഉള്ള ഏജന്റുകൾ രൂപകൽപ്പന ചെയ്ത് സഹകരണ പ്രവൃത്തി പ്രവാഹം പരീക്ഷിച്ചു മെച്ചപ്പെടുത്താം.

**പ്രയോഗത്തിൽ എങ്ങനെ**: ഓരോ ഏജന്റും ഡാറ്റാ ശേഖരണം, വിശകലനം, തീരുമാനമെടുക്കൽ തുടങ്ങിയ പ്രത്യേക ഫംഗ്ഷനുകൾ വഹിക്കുന്നു. ലക്ഷ്യം സംവദിച്ച് ജോലികൾ പൂർത്തിയാക്കാൻ ഇവ ഇടപడి വിവരങ്ങൾ പങ്കുവെക്കുന്നു.

**കോഡ് ഉദാഹരണം (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework ഉപയോഗിച്ച് ചേർന്ന് പ്രവർത്തിക്കുന്ന പല ഏജന്റുകളെ സൃഷ്ടിക്കുന്നത്

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ഡാറ്റ വീണ്ടെടുക്കൽ ഏജന്റ്
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ഡാറ്റ വിശകലന ഏജന്റ്
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ഒരു പ്രവൃത്തിയിൽ ഏജന്റുകൾ ക്രമത്തിൽ പ്രവർത്തിപ്പിക്കുക
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

മുന്‍പത്തെ കോഡിൽ കാണുന്നത് ബഹുഏജന്റുകൾ ചേർന്ന് ഡാറ്റ വിശകലനം ചെയ്യുന്ന ഒരു ജോലിയുടെ സൃഷ്ടിയാണ്. ഓരോ ഏജന്റും പ്രത്യേക ജോലികൾ നിർവഹിക്കുന്നു, ശരിയായ ഫലം ലഭിക്കാൻ കോർഡിനേഷൻ നടത്തുന്നു. പ്രത്യേക പദവികളും പാടവങ്ങളുമുള്ള ഏജന്റുകൾ സൃഷ്ടിച്ച്, ജോലി കാര്യക്ഷമതയും പ്രകടനവും മെച്ചപ്പെടുത്താം.

### യഥാർത്ഥ-സമയം പഠനം

ഉന്നതമായ ഫ്രെയിംവർകുകൾ യഥാർത്ഥ സമയം ഘട്ടത്തിൽ സാഹചര്യ മനസിലാക്കൽ ഒത്തുപോകലുകൾ അനുവദിക്കുന്നു.

**ടീമുകൾ എങ്ങനെ പ്രയോജനപ്പെടുത്തും**: ഏജന്റുകൾ ഇടപെടലുകളിൽ നിന്ന് പഠിച്ച് സ്വഭാവം ക്രമീകരിക്കുന്ന ഫീഡ്ബാക്ക് ലൂപ്പുകൾ നടപ്പിലാക്കുന്നു, കഴിവുകൾ തുടർച്ചയായ മെച്ചപ്പെടുത്തലിന്.

**പ്രയോഗത്തിൽ**: ഉപയോക്തൃ പ്രതികരണങ്ങൾ, പരിസ്ഥിതിവിവരങ്ങൾ, ജോലി ഫലങ്ങൾ വിശകലനം ചെയ്ത് അറിവ് പുതുക്കൽ, തീരുമാനമെടുക്കൽ ആൽഗോരിതങ്ങൾ ക്രമീകരണം, പ്രകടനം മെച്ചപ്പെടുത്തൽ നടത്തുന്നു. ഈ പുനരാവർത്തന ശേഷിയുള്ള പഠനം ഏജന്റുകൾക്ക് ഘടകങ്ങളെ അനുഗ്രമിച്ച് പ്രവർത്തിക്കാൻ സഹായിക്കുന്നു.

## Microsoft Agent Framework ഉം Azure AI Agent Service ഉം തമ്മിലുള്ള വ്യത്യാസങ്ങൾ എന്താണ്?

ഈ സമീപനങ്ങൾ താരതമ്യം ചെയ്യാനായി, ഡിസൈൻ, കഴിവുകൾ, ലക്ഷ്യമിട്ട ഉപയോഗം എന്നീ തലങ്ങളിൽ മുഖ്യ വ്യത്യാസങ്ങൾ നോക്കാം:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `AzureAIProjectAgentProvider` ഉപയോഗിച്ച് AI ഏജന്റുകൾ നിർമ്മിക്കാൻ എളുപ്പം ലഭ്യമാക്കുന്ന SDK ആണ്. ഇത് Azure OpenAI മോഡലുകൾ ഉപയോഗിച്ച് ടൂൾ കോൾ, സംഭാഷണ മേധാവ്, Azure ഐഡന്റിറ്റി വഴി എന്റർപ്രൈസ്-ഗ്രേഡ് സോരക്ഷ എന്നിവ ചേർന്ന് ഏജന്റ് സൃഷ്ടിക്കാൻ അനുവദിക്കുന്നു.

**ഉപയോഗങ്ങൾ**: ടൂൾ ഉപയോഗിച്ച് പ്രൊഡക്ഷൻ റെഡി AI ഏജന്റുകൾ, ബഹു-പടി പ്രവൃത്തി പ്രവാഹങ്ങൾ, എന്റർപ്രൈസ് സംയോജിത സീറ്റുവേഷനുകൾ നിർമ്മിക്കൽ.

Microsoft Agent Framework ന്റെ ചില പ്രധാന ആശയങ്ങൾ:

- **ഏജന്റുകൾ**: `AzureAIProjectAgentProvider` വഴി ഏജന്റ് സൃഷ്ടിച്ചുവെന്നും പേര്, നിർദ്ദേശങ്ങൾ, ഉപകരണങ്ങൾ കൂടി ക്രമീകരിക്കാൻ സാധിക്കും. ഏജന്റ്:
  - **ഉപയോക്തൃ സന്ദേശങ്ങൾ പ്രോസസ് ചെയ്ത് Azure OpenAI മോഡലുകളുമായി പ്രതികരണം സൃഷ്ടിക്കുന്നു.**
  - **സംഭാഷണ പരിസരത്തിന് അനുസരിച്ച് ടൂൾസ് സ്വയം വിളിക്കും.**
  - **പല സംവാദങ്ങളിൽ സംഭാഷണ അവസ്ഥ നിലനിർത്തും.**

  ഒരു ഏജენტის നിർമ്മാണത്തിന് കോഡ് ഉദാഹരണം:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **ടൂൾസ്**: ഫ്രെയിംവർക്ക് ഏജന്റുകൾക്ക് സ്വയം വിളിക്കാനുള്ള Python ഫംഗ്ഷനുകൾ ആയി ടൂൾസ് നിർവചിക്കാൻ സഹായിക്കുന്നു. ടൂൾസ് രജിസ്റ്റർ ചെയ്യുന്നത് ഏജന്റ് സൃഷ്ടിക്കുമ്പോൾ:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **ബഹുഏജന്റ് കോർഡിനേഷൻ**: വ്യത്യസ്ത വിദഗ്ധതയുള്ള എന്ജന്റുകൾ നിർമ്മിച്ച് അവരുടെ വർക്ക് കോർഡിനേറ്റ് ചെയ്യാം:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure ഐഡന്റിറ്റി സംയോജനം**: `AzureCliCredential` അല്ലെങ്കിൽ `DefaultAzureCredential` ഉപയോഗിച്ച് സുരക്ഷിത, കീമില്ലാത്ത ഓതന്റികേഷൻ, API കീകൾ കൈകാര്യം ചെയ്യേണ്ടതില്ല.

## Azure AI Agent Service

Azure AI Agent Service പുതിയ സേവനമാണ്, Microsoft Ignite 2024 ൽ അവതരിപ്പിച്ചത്. കൂടുതൽ ഫ്ലെക്സിബിൾ മോഡലുകൾ ഉപയോഗിച്ച്, ഉദാഹരണത്തിന് Llama 3, Mistral, Cohere പോലുള്ള ഓപ്പൺ-സോഴ്‌സ് LLMs നേരിട്ട് വിളിക്കാൻ അനുവാദം നൽകുന്നു.

Azure AI Agent Service ശക്തിയായ എന്റർപ്രൈസ് സോരക്ഷയും ഡേറ്റ ശേഖരണ രീതികളും നൽകുന്നു, എന്റർപ്രൈസ് ആപ്ലിക്കേഷനുകൾക്കു അനുയോജ്യം.

Microsoft Agent Framework-ഉം Azure AI Agent Service-ഉം സമന്വയപൂർവ്വം പ്രവർത്തിക്കുന്നു ഏജന്റ് നിർമ്മാണത്തിനും വിന്യസിപ്പിക്കുന്നതിനും.

ഇക്കഴിയുടെ പബ്ലിക് പ്രിവ്യൂയിൽ ആണിത്, Python, C# ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിക്കാൻ പിന്തുണ ഉണ്ട്.

Azure AI Agent Service Python SDK ഉപയോഗിച്ച് ഉപയോക്തൃ നിർവ്വചിത ടൂൾ ഉപയോഗിച്ച് ഏജന്റ് സൃഷ്ടിക്കുന്നത്:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ടൂൾ ഫംഗ്ഷനുകൾ നിർവചിക്കുക
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### മുഖ്യ ആശയങ്ങൾ

Azure AI Agent Service ഇങ്ങനെ ആശയങ്ങൾ ഉണ്ട്:

- **ഏജന്റ്**: Azure AI Agent Service Microsoft Foundry-നൊപ്പം ഒരുമകൊണ്ടുവെന്ന് അടയാളപ്പെടുത്താം. AI Foundry-യിൽ AI ഏജന്റ് "സ്മാർട്ട്" മൈക്രോസർവീസായി പ്രവർത്തിക്കുന്നു, RAG (RETRIEVE-ആൻഡ്-ജനറേറ്റ്) ചോദ്യങ്ങൾക്കു ഉത്തരങ്ങൾ നൽകാനും, ക്രിയകൾ പ്രവർത്തിക്കാനും, പ്രവൃത്തി ഒഴുക്കുകൾ ഓട്ടോമേറ്റുചെയ്യാനുമാകും. ജനന AI മോഡലുകൾക്കൊപ്പം ടൂൾസ് ഉപയോഗിച്ച് വാസ്തവ ഡേറ്റ സ്രോതസ്സുകളെ ആക്‌സസ് ചെയ്യാനും ഇത് സാധിക്കും. ഉദാഹരണ ഏജന്റ്:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ഈ ഉദാഹരണത്തിൽ `gpt-4o-mini` മോഡലിൽ ഒരു ഏജന്റ് സൃഷ്ടിക്കുന്നു, പേരു `my-agent`, നിർദ്ദേശങ്ങൾ `You are helpful agent`. കോഡ് വ്യാഖ്യാനം ഓട്ട് ചെയ്യാൻ ടൂൾസ് ഉൾപ്പെടുത്തിയിട്ടുണ്ട്.

- **ത്രീഡ്, സന്ദേശങ്ങൾ**: ത്രീഡ് മറ്റൊരു പ്രധാന ആശയമാണ്. ഇത് ഏജന്റും ഉപയോക്താവും തമ്മിലുള്ള സംഭാഷണം അല്ലെങ്കിൽ ഇടപെടലിന്റെ പ്രതിനിധാനം ആണ്. സംഭാഷണ പുരോഗതി ട്രാക് ചെയ്യാനും, സാഹചര്യ വിവരങ്ങൾ സൂക്ഷിക്കാനും, ഇടപെടൽ നില നിയന്ത്രിക്കാനും ത്രീഡുകൾ ഉപയോഗിക്കും. ഉദാഹരണ ത്രീഡ്:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    മുകളിൽ നൽകിയ കോഡിൽ ഒരു ത്രീഡ് സൃഷ്ടിച്ച ശേഷം സന്ദേശം അയക്കുന്നു. `create_and_process_run` വിളിച്ച് ഏജന്റിനെ ത്രീഡിൽ ജോലി ചെയ്യാൻ ആവശ്യപ്പെടുന്നു. പിന്നീട് സന്ദേശങ്ങൾ ലഭിച്ചു, ഏജന്റിന്റെ പ്രതികരണം ലോഗ് ചെയ്യുന്നു. സന്ദേശങ്ങൾ സംഭാഷണ പുരോഗതി സൂചിപ്പിക്കുന്നു. സന്ദേശങ്ങളുടെ തരംവിവിധമായിരിക്കാം: എഴുത്ത്, ചിത്രം, ഫയൽ; ഉദാഹരണത്തിന് ഏജന്റിന്റെ പ്രവർത്തനം ചിത്രമോ എഴുത്തോ ആയിരിക്കാം. ഡെവലപ്പറായി നിങ്ങൾ ഈ വിവരം തുടര്‍നടപടികൾക്ക് ഉപയോഗിക്കാം.

- **Microsoft Agent Framework-നൊപ്പം സംയോജനം**: Azure AI Agent Service Microsoft Agent Framework-നൊപ്പം സൗകര്യപ്രദമായി പ്രവർത്തിക്കുന്നു, അതായത് `AzureAIProjectAgentProvider` ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിച്ച് എന്റർപ്രൈസ് സീനാറിയോകൾക്കായി ഈ സർവ്വീസ് വഴി വിന്യസിക്കാം.

**ഉപയോഗങ്ങൾ**: സുരക്ഷിതം, സ്കെയിലബിൾ, ഫ്ലെക്സിബിൾ AI ഏജന്റ് വിന്യസനത്തിന് എന്റർപ്രൈസ് ആപ്ലിക്കേഷനുകൾക്ക് അനുയോജ്യം.

## ഈ സമീപനങ്ങളുടെ വ്യത്യാസം?

ഓവർലാപ്പ് ഉള്ളതായി തോന്നാം, പക്ഷേ ഡിസൈൻ, കഴിവ്, ലക്ഷ്യമിട്ട ഉപയോഗം എന്നിവ അടിസ്ഥാനത്തിൽ പ്രധാന വ്യത്യാസങ്ങൾ:

- **Microsoft Agent Framework (MAF)**: ടൂൾ കോൾ, സംഭാഷണ മേധാവ്, Azure ഐഡന്റിറ്റി സംയോജനം പോലുള്ള സൗജന്യ API-ഉം പ്രൊഡക്ഷൻ-സമൃദ്ധ SDK-ഉം ഉള്ള AI ഏജന്റ് നിർമാണത്തിന്.
- **Azure AI Agent Service**: Microsoft Foundry-യിൽ AI ഏജന്റുകൾക്ക് പ്ലാറ്റ്ഫോം, വിന്യസന സേവനം. Azure OpenAI, Azure AI Search, Bing Search, കോഡ് എക്സിക്യൂഷൻ തുടങ്ങിയ സേവനങ്ങളുമായി ബിൽറ്റ്-ഇൻ കണക്റ്റിവിറ്റി ഉണ്ട്.

ഇനി തീരുമാനിക്കാൻ ബുദ്ധിമുട്ടുണ്ടോ?

### ഉപയോഗ വ്യവസ്ഥകൾ

ചാരതമ്യത്തിനു ചില പൊതുവായ ഉപയോഗ വ്യവസ്ഥകൾ:

> ചോദ്യം: ഞാൻ പ്രൊഡക്ഷൻ മികവുള്ള AI ഏജന്റ് ആപ്ലിക്കേഷനുകൾ വേഗത്തിൽ നിർമ്മിക്കാൻ ആഗ്രഹിക്കുന്നു
>

>ഉത്തരം: Microsoft Agent Framework മികച്ച തിരഞ്ഞെടുപ്പാണ്. `AzureAIProjectAgentProvider` വഴി കുറച്ച് കുരുമ്പുകൾ കൊണ്ട് ടൂൾസ്, നിർദ്ദേശങ്ങൾ ഉപയോഗിച്ച് ഏജന്റുകൾ നിർവ്വചിക്കാം.

> ചോദ്യം: എന്റർപ്രൈസ്-ഗ്രേഡ് വിന്യസനം, Azure Search, കോഡ് എക്സിക്യൂഷൻ തുടങ്ങിയ ഇന്റഗ്രേഷനുകൾ വേണം
>
> ഉത്തരം: Azure AI Agent Service ഏറ്റവും അനുയോജ്യം. ഇത് ബഹുമുച്ചുര ഘടകങ്ങൾ, Azure AI Search, Bing Search, Azure Functions എന്നിവയ്ക്ക് ബിൽറ്റ്-ഇൻ പിന്തുണ നൽകുന്നു. Foundry പോർട്ടലിൽ ഏജന്റുകൾ സൃഷ്ടിച്ച് സ്കെയിലിൽ വിന്യസിക്കാം.

> ചോദ്യം: ഇപ്പോഴും ആശയക്കുഴപ്പം, ഒന്നാമത്തെ മാത്രം പറയൂ
>
> ഉത്തരം: ആദ്യം Microsoft Agent Framework-ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിച്ച് തുടക്കം കുറിക്കുക, പിന്നീട് പ്രൊഡക്ഷനിൽ വിന്യസിക്കുന്നതിനും സ്കെയിൽ ചെയ്യുന്നതിനും Azure AI Agent Service ഉപയോഗിക്കുക. ഇതിൽ ഏജന്റ് ലോകിക് വേഗത്തിൽ പുനഃസംസ്‌ക്കരിക്കാനും എന്റർപ്രൈസ് വിന്യസനത്തിലും സഹായകരമാണ്.

പ്രധാന വ്യത്യാസങ്ങൾ ഒരു പട്ടികയിൽ:

| ഫ്രെയിംവർക്ക് | ഫോകസ് | പ്രധാന ആശയങ്ങൾ | ഉപയോഗ സാഹചര്യങ്ങൾ |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ടൂൾ കോൾ സഹിതം സംക്ഷിപ്ത ഏജന്റ് SDK | ഏജന്റുകൾ, ടൂൾസ്, Azure ഐഡന്റിറ്റി | AI ഏജന്റ് നിർമ്മാണം, ടൂൾ ഉപയോഗം, ബഹു-പടി പ്രവൃത്തി പ്രവാഹങ്ങൾ |
| Azure AI Agent Service | ഫ്ലെക്സിബിൾ മോഡലുകൾ, എന്റർപ്രൈസ് സുരക്ഷ, കോഡ് ജെനറേഷൻ, ടൂൾ കോൾ | മോഡുലാർ, സഹകരണം, പ്രോസസ് ഓർക്കസ്ട്രേഷൻ | സുരക്ഷിതവും സ്കെയിലബിൾവും ഫ്ലെക്സിബിളുമായ AI ഏജന്റ് വിന്യസനം |

## നിലവിലുള്ള Azure ഇക്കോസിസ്റ്റം ഉപകരണങ്ങൾ നേരിട്ട് ഇന്റഗ്രേറ്റ് ചെയ്യാമോ, അല്ലെങ്കിൽ സ്റ്റാൻഡലോൺ സൊല്യൂഷനുകൾ ആവണോ?
ഉത്തരം അതെ, നിങ്ങളുടെ നിലവിലുള്ള Azure ഇക്കോസിസ്റ്റം ഉപകരണങ്ങൾ പ്രത്യേകിച്ച് Azure AI ഏജന്റ് സർവീസുമായി നേരിട്ട് സംയോജിപ്പിക്കാനാകും, കാരണം ഇത് മറ്റ് Azure സർവീസുകളുമായി ലംഘനരഹിതമായി പ്രവർത്തിക്കാൻ നിർമ്മിച്ചിരിക്കുന്നു. ഉദാഹരണത്തിന്, നിങ്ങള്ക്ക് ബിംഗ്, Azure AI Search, Azure Functions എന്നിവ സംയോജിപ്പിക്കാം. മൈക്രോസോഫ്റ്റ് ഫൌണ്ട്രിയുമായി സമഗ്രമായ സംയോജനം കൂടി ഉണ്ട്.

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് `AzureAIProjectAgentProvider` വഴിയും Azure ഐഡന്റിറ്റിയും ഉപയോഗിച്ച് Azure സർവീസുകളുമായി സംയോജിപ്പിക്കുന്നു, ഇത് നിങ്ങളുടെ ഏജന്റ് ഉപകരണങ്ങളിൽ നിന്നു നേരിട്ട് Azure സർവീസുകൾ വിളിക്കാൻ അനുവദിക്കുന്നു.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Got More Questions about AI Agent Frameworks?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസാധാരണ**:  
ഈ documento AI പരിഭാഷ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ നിശ്ചിതത്വത്തിനായി ശ്രമിക്കുന്നെങ്കിലും, ഓട്ടോമാറ്റിക് പരിഭാഷകളിൽ പിശകുകളോ കൃത്യതയില്ലാത്തതുണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. നാട്ടുരാജ്യത്തിലെ മൊഴിയിലുള്ള അസൽ documento ഔദ്യോഗിക സ്രോതസ്സ് എന്ന നിലയിൽ കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ചതിൽ നിന്നുണ്ടാകുന്ന തെറ്റിനർത്ഥകമോ തെറ്റുതരമോ ഏതെങ്കിലും അന്ധവിശ്വാസങ്ങൾക്ക് ഞങ്ങൾ ഉത്തരവാദിത്തം വഹിക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->