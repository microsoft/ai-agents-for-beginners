[![AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ അന്വേഷിക്കുന്നത്](../../../translated_images/ml/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളിൽ ഉള്ള ചിത്രം ക്ലിക് ചെയ്യുക)_

# AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ അന്വേഷിക്കുക

AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ AI ഏജൻറുകളുടെ സൃഷ്ടി, വിന്യാസം, മാനേജ്മെന്റ് ലളിതമാക്കാൻ രൂപകൽപ്പന ചെയ്ത സോഫ്റ്റ്‌വെയർ പ്ലാറ്റ്ഫോമുകളാണ്. ഈ ഫ്രെയിംവർക്കുകൾ ഡെവലപ്പർമാർക്ക് മുൻകൂട്ടി നിർമ്മിച്ച ഘടകങ്ങൾ, സാരാംശങ്ങൾ, ഉപകരണങ്ങൾ എന്നിവകൾ നൽകി സങ്കീർണ്ണമായ AI സിസ്റ്റങ്ങൾ വികസിപ്പിക്കൽ ലളിതമാക്കുന്നു.

AI ഏജന്റ് വികസനത്തിൽ സാധാരണമായ വെല്ലുവിളികൾക്ക് സ്റ്റാൻഡർഡൈസ്ഡ് സമീപനങ്ങൾ നൽകി ഡെവലപ്പർമാർക്ക് അവരുടെ അപേക്ഷകളിലെ പ്രത്യേകതകളിൽ് ശ്രദ്ധ കേന്ദ്രീകരിക്കാൻ സഹായിക്കുന്നു. ഇവ AI സിസ്റ്റം നിർമ്മിക്കുമ്പോൾ സ്‌കെയിലാബിലിറ്റി, ലഭ്യത, കാര്യക്ഷമത വർദ്ധിപ്പിക്കുന്നു.

## പരിചയം 

ഈ പാഠം ഉൾപ്പെടുത്തുന്നത്:

- AI ഏജന്റ് ഫ്രെയിംവർകുകളെന്താണെന്നും ഡെവലപ്പർമാർ എന്ത് കൈവരി നേടാൻ കഴിയുമെന്നുമുള്ളത്?
- ഏജന്റിന്റെ കഴിവുകൾ വേഗം പ്രോട്ടോട്ടൈപ്പ് ചെയ്യാനും ആവർത്തിക്കുകയും മെച്ചപ്പെടുത്താനും ടീമുകൾ എങ്ങനെ ഉപയോഗിക്കാം?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> കൂടാതെ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) നിർമ്മിച്ച ഫ്രെയിംവർകുകളും ഉപകരണങ്ങളും തമ്മിലുള്ള വ്യത്യാസങ്ങൾ എന്തെല്ലാം?
- എന്റെ നിലവിലുള്ള Azure പരിസ്ഥിതി ഉപകരണങ്ങൾ നേരിട്ട് ഇണ unmarried രൂപപ്പെടുത്താൻ കഴിയുമോ, അല്ലെങ്കിൽ സ്റ്റാൻഡ്അലോൺ പരിഹാരങ്ങൾ ആവശ്യമാണോ?
- Microsoft Foundry Agent Service എന്താണ്, ഇത് എങ്ങനെ എനിക്ക് സഹായിക്കുന്നു?

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠത്തിന്റെ ലക്ഷ്യങ്ങൾ നിങ്ങൾ ഉറപ്പാക്കുക:

- AI വികസനത്തിൽ AI ഏജന്റ് ഫ്രെയിംവർക്കുകളുടെ പങ്ക്.
- ബുദ്ധിമാനായ ഏജന്റുകൾ നിർമ്മിക്കാൻ AI ഏജന്റ് ഫ്രെയിംവർകുകൾ എങ്ങനെ ഉപയോഗിക്കാമെന്ന്.
- AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ ചേർത്ത് സാധ്യമാക്കുന്ന പ്രധാന കഴിവുകൾ.
- Microsoft Agent Frameworkമന്മയും Microsoft Foundry Agent Service-നും ഉള്ള വ്യത്യാസങ്ങൾ.

## AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ എന്തും ഡെവലപ്പർമാർക്ക് എന്ത് കഴിയുമെന്നു അറിയുക?

പാരമ്പര്യ AI ഫ്രെയിംവർക്കുകൾ നിങ്ങളുടെ ആപ്പുകളിൽ AI എങ്ങനെ സംയോജിപ്പിക്കാം എന്നും ആ ആപ്പുകൾ മെച്ചപ്പെടുത്താൻ സഹായിക്കുന്നവയാണ്:

- **വ്യക്തിഗത ജിവിതം**: ഉപയോക്തൃ പെരുമാറ്റവും ഇഷ്ടങ്ങളും വിശകലനം ചെയ്ത് വ്യക്തിഗത ശിപാർശകൾ, ഉള്ളടക്കം, അനുഭവങ്ങൾ നൽകുന്നു.
ഉദാഹരണം: Netflix പോലുള്ള സ്റ്റ്രീമിംഗ് സേവനങ്ങൾ മോശസായി കണ്ട മൂവികളും ഷോകളും ശിപാർശ ചെയ്ത് ഉപയോക്തൃ പങ്കാളിത്തവും സംതൃപ്തിയും വർദ്ധിപ്പിക്കുന്നു.
- **ഓട്ടോമേഷൻ, കാര്യക്ഷമത**: ആവർത്തിക്കുന്ന പ്രവർത്തനങ്ങൾ ഓട്ടോമേറ്റ് ചെയ്യുന്നു, പ്രവാഹങ്ങൾ ലളിതമാക്കുന്നു, പ്രവർത്തനക്ഷമത മെച്ചപ്പെടുത്തുന്നു.
ഉദാഹരണം: കസ്റ്റമർ സർവീസ് ആപ്പുകൾ ചാറ്റ്ബോട്ടുകളിലൂടെ സാധാരണ ചോദനകൾ കൈകാര്യം ചെയ്ത് പ്രതികരണ സമയം കുറക്കും, മനുഷ്യ ഏജന്റുകൾക്ക് കൂടുതൽ സങ്കീർണ്ണ പ്രശ്‌നങ്ങൾക്കായി സമയം ഒഴിയാക്കുന്നു.
- **ഉപയോക്തൃ അനുഭവം മെച്ചപ്പെടുത്തൽ**: വോയ്സ് തിരിച്ചറിവ്, സ്വഭാവസഹിത ഭാഷാ പ്രോസസ്സിംഗ്, പ്രവചന വർണം പോലുള്ള ബുദ്ധിമാൻ ഫീച്ചറുകൾ നൽകുന്നു.
ഉദാഹരണം: Siri, Google Assistant പോലുള്ള വിർച്വൽ അസിസ്റ്റന്റുകൾ വോയിസ് കമാൻഡുകൾ മനസിലാക്കി മറുപടി നൽകി ഉപയോക്താക്കളുടെ ഉപകരണങ്ങളുമായി എളുപ്പത്തിൽ ഇടപഴകാൻ സഹായിക്കുന്നു.

### എല്ലാം മികച്ചതാണല്ലോ, എന്നാൽ AI ഏജന്റ് ഫ്രെയിംവർക്ക് എന്തിനാണ്?

AI ഏജന്റ് ഫ്രെയിംവർകുകൾ സാധാരണ AI ഫ്രെയിംവർകുകളിൽനിന്ന് വ്യത്യസ്തമാണ്. അവ ബുദ്ധിമാനായ ഏജന്റുകൾ നിർമ്മിക്കാൻ രൂപകൽപ്പന ചെയ്തിരിക്കുന്നതാണ്, അവ ഉപയോക്താക്കളോടും മറ്റുള്ള ഏജന്റുകളോടും പരിസ്ഥിതിയോട് സംവദിച്ച് നിശ്ചിത ലക്ഷ്യങ്ങൾ നേടുന്നതിന്. സ്വയംഭരണ പെരുമാറ്റം കാണിക്കാനും തീരുമാനങ്ങൾ എടുക്കാനും മാറുന്ന സാഹചര്യം അനുസരിച്ചു അനുകൂലപ്പെടാനും ഇവ കഴിയും. AI ഏജന്റ് ഫ്രെയിംവർകുകൾ സുലഭമാക്കുന്ന പ്രധാന കഴിവുകൾ നോക്കാം:

- **ഏജന്റ് സഹകരണം, ഏകോപനം**: കോമ്പ്ലക്സ് ടാസ്കുകൾ പരിഹരിക്കാൻ ഒന്നിച്ച് പ്രവർത്തിക്കുന്ന, ആശയവിനിമയം നടത്തുന്നതിനും ഏകോപനം കൈകാര്യം ചെയ്യുന്നതിനും കഴിയുന്ന നിരവധി AI ഏജന്റുകൾ സൃഷ്ടിക്കാൻ.
- **ടാസ്‌ക്ക് ഓട്ടോമേഷൻ, മാനേജ്മെന്റ്**: ബഹുസ്ഥാപിത വർക്ക്ഫ്ലോകൾ ഓട്ടോമേറ്റുചെയ്യാനും ടാസ്‌ക് റജിസ്ട്രേഷൻ, പ്രധാനം എന്നിവയ്ക്കുള്ള സംവിധാനങ്ങൾ നൽകാൻ.
- **സന്ദർഭജ്ഞാനം, അനുസരണം**: സാഹചര്യത്തെ മനസിലാക്കി, മാറുന്ന പരിസ്ഥിതി അനുസരിച്ച് അനുകൂലനവും യഥാർത്ഥ സമയ വിവരത്തിനനുസരിച്ചുള്ള നിർണയവും.

സംക്ഷേപത്തിൽ, ഏജന്റുകൾ നിങ്ങൾക്ക് കൂടുതൽ സാധ്യമാക്കുന്നു, ഓട്ടോമേഷൻ അടുത്ത നിലയിലേക്ക് നയിക്കുന്നു, പരിസ്ഥിതിയിൽ നിന്നും പഠിച്ച് അനുസരിച്ച് കൂടുതൽ ബുദ്ധിമാനായ സിസ്റ്റങ്ങൾ സൃഷ്ടിക്കാൻ സഹായിക്കുന്നു.

## എങ്ങനെ വേഗത്തിൽ പ്രോട്ടോടൈപ്പ് ചെയ്യാനും ആവർത്തിക്കുകയും ഏജന്റിന്റെ കഴിവുകൾ മെച്ചപ്പെടുത്തുകയും ചെയ്യാം?

ഈ മേഖല വേഗത്തിൽ മുന്നേറുകയാണ്, എന്നാൽ മുപ്പത്താറിൽ കൂടുതൽ AI ഏജന്റ് ഫ്രെയിംവർകുകളിൽ പൊതുവായി കാണപ്പെടുന്ന ഘടകങ്ങൾ ഉണ്ട്, ഉദാഹരണത്തിന് മോഡ്യൂളർ ഘടകങ്ങൾ, സഹകരണ ഉപകരണങ്ങൾ, യഥാർത്ഥ സമയ പഠനം. ഇതിൽ കടന്നു നോക്കാം:

- **മോഡ്യൂളാർ ഘടകങ്ങൾ ഉപയോഗിക്കുക**: AI SDKകൾ മുൻകൂട്ടി നിർമ്മിച്ച AI, മെമ്മറി കണക്ടറുകൾ, ഫങ്ഷൻ കോളിംഗ് (നേച്ച്വറൽ ലാംഗ്വേജ് അല്ലെങ്കിൽ കോഡ് പ്ലഗിനുകൾ വഴി), പ്രോംപ്റ്റ് ടെംപ്ലേറ്റുകൾ മുതലായ കോംപോണന്റുകൾ വാഗ്ദാനം ചെയ്യുന്നു.
- **സഹകരണ ഉപകരണങ്ങൾ ഉപയോഗിക്കുക**: പ്രത്യേക റോളുകൾ, ടാസ്‌കുകൾ ഉള്ള ഏജന്റുകൾ ഡിസൈൻ ചെയ്ത്, സഹകരണ പ്രവാഹങ്ങൾ പരീക്ഷിച്ച് ഉന്നതപ്പെടുത്താൻ കഴിയും.
- **യഥാർത്ഥ സമയത്തിൽ പഠിക്കുക**: ഏജന്റുകൾ ഇടപെടലുകളിൽ നിന്നു പഠിച്ച് പെരുമാറ്റം ഡൈനാമിക് ആയി ക്രമീകരിക്കുന്ന ഫീഡ്ബാക്ക് ലൂപ്പുകൾ നടപ്പിലാക്കുക.

### മോഡ്യൂളാർ ഘടകങ്ങൾ ഉപയോഗിക്കുക

Microsoft Agent Framework പോലുള്ള SDKകൾ മുൻകൂട്ടി നിർമ്മിച്ച AI കണക്ടറുകൾ, ടൂൾ നിർവചനങ്ങൾ, ഏജന്റ് മാനേജ്മെന്റ് എന്നിവ വാഗ്ദാനം ചെയ്യുന്നു.

**ടീമുകൾ ഇതെങ്ങനെയാണ് ഉപയോഗിക്കുന്നത്**: ടീം അംഗങ്ങൾ ഈ ഘടകങ്ങൾ വേഗത്തിൽ ഒത്തുചേര്ക്ക് പ്രവര്‍ത്തന പ്രോട്ടോടൈപ്പ് നിർമ്മിക്കാം, എളുപ്പത്തിൽ പരീക്ഷണവും ആവർത്തനവും നടത്താൻ.

**പ്രായോഗികമായി ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു**: ഉപയോക്തൃ ഇൻപുട്ടിൽ നിന്ന് വിവരങ്ങൾ എടുക്കാൻ മുൻകൂട്ടി നിർമ്മിച്ച പാഴ്സർ, ഡാറ്റ സംഭരിച്ച് പിൻവലിക്കാൻ മെമ്മറി മോഡ്യൂൾ, ഉപയോക്താക്കളുമായി ഇടപഴകാൻ പ്രോംപ്റ്റ് ജനറേറ്റർ തുടങ്ങിയ ഘടകങ്ങൾ ഉപയോഗിക്കാം, നവാഗതമായി നിന്നോടു തുടങ്ങാതെ തന്നെ.

**ഉദാഹരണ കോഡ്**: Microsoft Agent Framework ഉപയോഗിച്ച് `FoundryChatClient` വഴി ഉപയോക്തൃ ഇൻപുട്ടിന് ടൂൾ കോളിംഗ് സജ്ജമാക്കി മാറ്റാനുള്ള ഉദാഹരണം:

``` python
# മൈക്രോസോഫ്‌റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് പൈതൺ ഉദാഹരണം

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# യാത്ര ബുക്ക് ചെയ്യാൻ ഒരു ഉദാഹരണ ഉപകരണം ഫങ്ഷൻ നിർവ്വചിക്കുക
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # ഉദാഹരണ പുറംവരവ്: 2025 ജനുവരി 1-നുള്ള നിങ്ങളുടെ ന്യൂയോർക്ക് യാത്ര വിജയകരമായി ബുക്ക് ചെയ്‌തിട്ടുണ്ട്. സുരക്ഷിതമായ യാത്രകൾ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ഈ ഉദാഹരണത്തിൽ, ഉപയോക്തൃ ഇൻപുട്ടിൽ നിന്ന് ഉല്പത്തി, ലക്ഷ്യം, വിമാന ബുക്കിംഗ് ആവശ്യത്തിന്റെ തീയതി തുടങ്ങിയ മുഖ്യ വിവരങ്ങൾ പാഴ്സർ ഉപയോഗിച്ച് എങ്ങനെ ലഭ്യമാക്കാമെന്നു കാണുന്നു. ഈ മോഡ്യൂളർ സമീപനം ഹൈ-ലെവൽ ലജിക് കാര്യമായി ശ്രദ്ധിക്കാനായി സഹായിക്കുന്നു.

### സഹകരണ ഉപകരണങ്ങൾ ഉപയോഗിക്കുക

Microsoft Agent Framework പോലുള്ള ഫ്രെയിംവർകുകൾ ഒന്നിച്ച് പ്രവർത്തിക്കുന്ന ബഹു ഏജന്റും സൃഷ്ടിക്കാൻ സഹായിക്കുന്നു.

**ടീമുകൾ എങ്ങനെ ഉപയോഗിക്കും**: പ്രത്യേക റോളുകളും ടാസ്‌കുകളും ഉള്ള ഏജന്റുകൾ ഡിസൈൻ ചെയ്ത്, സഹകരണ പ്രവാഹങ്ങൾ പരീക്ഷിക്കുകയും, സിസ്റ്റം കാര്യക്ഷമത മെച്ചപ്പെടുത്തുകയും ചെയ്യാൻ.

**പ്രായോഗികമായി എങ്ങനെ പ്രവർത്തിക്കുന്നു**: ഡാറ്റാ ശേഖരിക്കൽ, വിശകലനം, തീരുമാനമെടുക്കൽ പോലുള്ള വൈവിധ്യമാർന്ന ഫംഗ്ഷനുകൾ ഉള്ള ഏജന്റുകളുടെ ടീം രൂപപ്പെടുത്താം. ഇവ ആശയവിനിമയം നടത്തുകയും സാധാരണ ലക്ഷ്യം തേടി ചേർന്ന് പ്രവർത്തിക്കുകയും ചെയ്യും, ഉദാഹരണത്തിന് ഉപയോക്തൃ ചോദ്യത്തിന് മറുപടി നൽകുക അല്ലെങ്കിൽ ഒരു ടാസ്‌ക് പൂർത്തിയാക്കുക.

**ഉദാഹരണ കോഡ് (Microsoft Agent Framework)**:

```python
# മൈക്രോസോഫ്‌ട് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ സഹായത്തോടെ ഒന്നിച്ച് പ്രവര്‍ത്തിക്കുന്ന ഒന്നിലധികം ഏജന്റുകള്‍ സൃഷ്ടിക്കുന്നു

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ഡാറ്റ റിട്രീവല്‍ ഏജന്റ്
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ഡാറ്റ അനാലിസിസ് ഏജന്റ്
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ഒരു ടാസ്കില്‍ഏജന്റുമാര്‍ ക്രമത്തില്‍ ഓടിക്കുക
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

മുകളിൽ കാണുന്ന കോഡിൽ, ഒരിക്കൽ ബഹുല AI ഏജന്റുകൾ ചേർത്ത് ഡാറ്റ വിശകലനം ചെയ്യുന്ന ഒരു ടാസ്‌ക് സൃഷ്ടിക്കുന്നത് കാണിക്കുന്നു. ഓരോ ഏജന്റും പ്രത്യേകം പ്രവർത്തനം നിർവഹിക്കുന്നു, അവിഭાજ്യമായി ഏകോപിപ്പിച്ച് ടാസ്‌ക് വിജയകരമായി പൂർത്തിയാക്കുന്നു. പ്രത്യേക റോളുകൾ ഉള്ള ഏജന്റുകൾ സൃഷ്ടിച്ച് ടാസ്‌ക് കാര്യക്ഷമത മെച്ചപ്പെടുത്താം.

### യഥാർത്ഥ സമയത്തിൽ പഠിക്കുക

ആധുനിക ഫ്രെയിംവർകുകൾ യഥാർത്ഥ സമയ സന്ദർഭ മനസ്സിലാക്കലും അനുസരണവും അനുവദിക്കുന്നു.

**ടീമുകൾ എങ്ങനെ ഉപയോഗിക്കും**: ഏജന്റുകൾ ഇടപെടലുകളിൽ നിന്നു ഫീഡ്ബാക്ക് ശേഖരിച്ച് പെരുമാറ്റം ക്രമീകരിച്ച് തുടർച്ചയായ മെച്ചപ്പെടുത്തലും പരിഷ്‌കരണവും നടത്താൻ ഫീഡ്ബാക്ക് ലൂപ്പുകൾ നടപ്പിലാക്കുക.

**പ്രായോഗികമായി എങ്ങനെ പ്രവർത്തിക്കുന്നു**: ഉപയോക്തൃ ഫീഡ്ബാക്ക്, പരിസ്ഥിതി ഡാറ്റ, ടാസ്‌ക് ഔട്ട്കം വിശകലനം ചെയ്ത് അറിവ് അപ്ഡേറ്റ് ചെയ്യുക, തീരുമാനം എടുക്കുന്ന ആൽഗോരിത്തങ്ങൾ ശരിയാക്കുക, പ്രകടനം മെച്ചപ്പെടുത്തുക. ഈ ആവർത്തന പഠനം ഏജന്റുകൾക്ക് മാറുന്ന സാഹചര്യത്തിനും ഉപയോക്തൃ ഇഷ്ടങ്ങൾക്കും അനുസരിച്ച് ക്രമീകരിക്കാൻ സഹായിക്കുന്നു, ഇതുവഴി സിസ്റ്റം ഗുണനിലവാരം മെച്ചപ്പെടുന്നു.

## Microsoft Agent Frameworkനും Microsoft Foundry Agent Serviceനും ഉള്ള വ്യത്യാസങ്ങൾ എന്തൊക്കെയാണ്?

ഇവയെ താരതമ്യം ചെയ്യാനുള്ള പല വഴികളുണ്ട്, എന്നാൽ രൂപകൽപ്പന, കഴിവുകൾ, ലക്ഷ്യമിടുന്ന ഉപയോഗക്കേസുകൾ എന്ന പരിപ്രേക്ഷ്യത്തിൽ ചില പ്രധാന വ്യത്യാസങ്ങൾ നോക്കാം:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `FoundryChatClient` ഉപയോഗിച്ച് AI ഏജന്റുകൾ നിർമ്മിക്കാൻ streamlined SDK വാഗ്ദാനം ചെയ്യുന്നു. Azure OpenAI മോഡലുകൾ ഉപയോഗിച്ച് ടൂൾ കോളിംഗ്, സംവാദ മാനേജ്മെന്റ്, Azure തിരിച്ചറിയൽ സുരക്ഷ എന്നിവയ്ക്ക് ഉതകുന്നു.

**ഉപയോഗം**: പ്രൊഡക്ഷൻ റെഡിയായ AI ഏജന്റുകൾ നിർമ്മിക്കാനായി, ടൂൾ ഉപയോഗം, ബഹു ഘട്ട workflowകൾ, എന്റർപ്രൈസ് ഇന്റഗ്രേഷൻ സീനാകാരികൾ.

Microsoft Agent Frameworkന്റെ ചില പ്രധാന ആശയങ്ങൾ:

- **ഏജന്റുകൾ**. `FoundryChatClient` വഴി ഏജന്റ് സൃഷ്ടിക്കുകയും പേരും നിർദ്ദേശങ്ങളും ടൂളുകളും കൊണ്ടു കോൺഫിഗർ ചെയ്യുകയും ചെയ്യാം. ഏജന്റ്:
  - **ഉപയോക്തൃ സന്ദേശങ്ങൾ പ്രോസസ് ചെയ്ത്** Azure OpenAI മോഡലുകളുപയോഗിച്ച് മറുപടികൾ സൃഷ്ടിക്കും.
  - **സംവാദ സാഹചര്യം അനുസരിച്ചു ടൂളുകൾ** ഓട്ടോമാറ്റിക്കായി വിളിക്കും.
  - **ബഹുസ്വര സംവാദം സ്റ്റേറ്റ്** സൂക്ഷിച്ച് കൈകാര്യം ചെയ്ത് തുടർച്ച നിലനിർത്തും.

  ഏജന്റ് സൃഷ്ടിക്കുന്നതിനുള്ള കോഡ് ഒരു സ്നിപ്പെറ്റ് ഇവിടെ കാണാം:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **ടൂൾസ്**. ഫ്രെയിംവർക്ക് Python ഫംഗ്ഷനുകളായി ടൂളുകൾ നിർവ്വചിച്ച് ഏജന്റ് ഓട്ടോമായി വിളിക്കാൻ സഹായിക്കുന്നു. ടൂളുകൾ ഏജന്റ് സൃഷ്ടിക്കുമ്പോൾ രജിസ്റ്റർ ചെയ്യപ്പെടുന്നു:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **ബഹു ഏജന്റ് ഏകോപനം**. വ്യത്യസ്ത സ്പെഷ്യലൈസേഷനുകൾ ഉള്ള നിരവധി ഏജന്റുകൾ സൃഷ്ടിച്ച് ഓരോരുത്തരുടെയും പ്രവർത്തനം ഏകോപിപ്പിക്കാൻ കഴിയും:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure തിരിച്ചറിയൽ സംയോജനം**. `AzureCliCredential` (അല്ലെങ്കിൽ `DefaultAzureCredential`) ഉപയോഗിച്ച് സുരക്ഷിതമായ കീ ഇല്ലാത്ത ഒത്താശ്വാസം ഏജൻറുകൾക്ക് നൽകുന്നു, API കീകൾ നേരിട്ട് കൈകാര്യം ചെയ്യേണ്ടതില്ല.

## Microsoft Foundry Agent Service

Microsoft Ignite 2024-ൽ പരിചയപ്പെടുത്തിയ പുതിയ സേവനം. ഇതുവഴി Llama 3, Mistral, Cohere പോലുള്ള ഓപ്പൺ സോഴ്‌സ് LLMs നേരിട്ട് വിളിക്കാവുന്ന കൂടുതൽ സൗകര്യമുള്ള മോഡലുകൾ വഴി AI ഏജന്റുകൾ വികസിപ്പിക്കാനും വിന്യസിക്കാനും കഴിയും.

Microsoft Foundry Agent Service ഉതകുന്ന എന്റർപ്രൈസ് സുരക്ഷാ സംവിധാനങ്ങളും ഡാറ്റാ സൂക്ഷിപ്പ് രീതികളും ഉപയോക്താക്കൾക്ക് നൽകുന്നു, എന്റർപ്രൈസ് ആപ്പ്ലിക്കേഷനുകൾക്കായി അനുയോജ്യം.

Microsoft Agent Framework-നൊപ്പം കൂടിയായ പ്രവർത്തനം കൂടിയതാണ്, ഏജന്റുകൾ നിർമ്മിച്ച് വിന്യസിക്കാൻ സഹായിക്കുന്നു.

ഇപ്പോൾ പബ്ലിക് പ്രവ്യുവിലാണ്, Python, C# ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിക്കുന്നത് സഹായിക്കുന്നു.

Microsoft Foundry Agent Service Python SDK ഉപയോഗിച്ച് ഉപയോക്തൃ നിർവ്വചിച്ച ഒരു ടൂൾ ഉൾപ്പെടുത്തി ഏജന്റ് സൃഷ്ടിക്കാം:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ഉപകരണ ഫังก്ഷനുകൾ നിർവചിക്കുക
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
        model="gpt-5-mini",
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

### പ്രധാന ആശയങ്ങൾ

Microsoft Foundry Agent Service-ന്റെ പ്രധാന ആശയങ്ങൾ:

- **ഏജന്റ്**. Microsoft Foundry Agent Service Microsoft Foundry-നൊപ്പം സംയോജിപ്പിച്ചിരിക്കുന്നത്. ഇവിടെ AI ഏജന്റ് ഒരു "സ്മാർട്ട്" മൈക്രോസേവീസ് ആയി പ്രവർത്തിക്കുന്നു, RAG (രേഖകൾ ആധാരമാക്കി ഉത്തരം നൽകൽ), പ്രവർത്തനങ്ങൾ നിർവഹിക്കൽ, പ്രക്രിയാപദ്ധതികൾ പൂർണ്ണമായി ഓട്ടോമേറ്റ് ചെയ്യാൻ സാധിക്കും. ജനറേറ്റീവ് AI മോഡലുകളുടെ ശക്തിയോടൊപ്പം ഉപകരണം ഉപയോഗിച്ച് യഥാർത്ഥ ലോക ഡാറ്റാ സ്രോതസ്സുകൾ ആക്സസ് ചെയ്യാനും ഇടപെടാനും.

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ഈ ഉദാഹരണത്തിൽ `gpt-5-mini` മോഡൽ, `my-agent` എന്ന പേര്, `You are helpful agent` എന്ന നിർദ്ദേശങ്ങളോടെയുള്ള ഏജന്റ് സൃഷ്ടിച്ചിരിക്കുന്നു. ഏജന്റ് കോഡ് വ്യാഖ്യാനം ടാസ്‌കുകൾ നിർവ്വഹിക്കാനായി ടൂളുകളും വിഭവങ്ങളും കൊണ്ടിരിക്കുന്നു.

- **ത്രെഡ്, സന്ദേശങ്ങൾ**. ത്രെഡ് മറ്റൊരു പ്രധാന ആശയമാണ്. ഇത് ഉപയോക്താവും ഏജന്റും തമ്മിലുള്ള സംവാദം / ഇടപെടലിന്റെ പ്രതിനിധിത്ത്വം. സംവാദ പുരോഗതിയേയും സാഹചര്യ ഡാറ്റയും സൂക്ഷിക്കാനും സംവാദ നിലയേയും കൈകാര്യം ചെയ്യാനുമുള്ളത്. ത്രെഡിന്റെ ഉദാഹരണം:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ഏജന്റോട് ത്രെഡിൽ ജോലി ചെയ്യാൻ പറയുക
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ഏജന്റിന്റെ പ്രതികരണം കാണാൻ എല്ലാ സന്ദേശങ്ങളും ക്രമീകരിച്ച് രേഖപ്പെടുത്തുക
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    മുകളിൽ കാണുന്ന കോഡിൽ ത്രെഡ് സൃഷ്ടിച്ച് പിന്നീട് ത്രെഡിലേക്ക് സന്ദേശം അയക്കുന്നു. `create_and_process_run` വിളിച്ച് ഏജന്റിനെ ത്രെഡിൽ പ്രവർത്തനങ്ങൾ നിർവഹിക്കാൻ ആവശ്യപ്പെടുന്നു. സന്ദേശങ്ങൾ എടുത്ത് ലോഗ് ചെയ്യുമ്പോൾ ഉപയോക്താവും ഏജന്റും തമ്മിലുള്ള സംവാദ പുരോഗതി വ്യക്തമാകും. സന്ദേശങ്ങൾ വണങ്ങിയതാണ് (ടെസ്റ്റ്, ചിത്രം, ഫയൽ മുതലായവ), ഉദാഹരണത്തിന്, ഏജന്റിന്റെ പ്രവർത്തനം ചിത്രമായി അല്ലെങ്കിൽ ടെക്സ്റ്റായി ഫലം നൽകിയിട്ടുണ്ട്. ഡെവലപ്പറായി നിങ്ങൾക്ക് ഈ വിവരങ്ങൾ ഉപയോഗിച്ച് മറുപടി കൂടുതൽ പ്രോസസ് ചെയ്യുകയോ ഉപയോക്താവിന് അവതരിപ്പിക്കുകയോ ചെയ്യാം.

- **Microsoft Agent Framework-നൊപ്പം സംയോജനം**. Microsoft Foundry Agent Service Microsoft Agent Framework-നൊപ്പം അതിവേഗം പ്രവർത്തിക്കുന്നു, അതിലൂടെ `FoundryChatClient` ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിച്ച് പ്രൊഡക്ഷൻ സീനാരിയോകൾക്കായി ഏജന്റ് സർവീസിലൂടെ വിന്യസിക്കാം.

**ഉപയോഗം**: സുരക്ഷിതം, സ്‌കെയിലബിള്‍, ലളിതമായി എന്റർപ്രൈസ് ലെവലിൽ AI ഏജന്റ് വിന്യാസങ്ങൾക്കായി രൂപകല്പന ചെയ്ത സേവനം.

## ഈ സമീപനങ്ങൾ തമ്മിലുള്ള വ്യത്യാസം എന്താണ്?
 
ഒരേ പോലെ തോന്നാം, എന്നാൽ രൂപകൽപ്പന, കഴിവുകൾ, ലക്ഷ്യമിടുന്ന ഉപയോഗങ്ങൾ എന്ന നിലയിൽ പ്രധാന വ്യത്യാസങ്ങൾ ഉണ്ട്:
 
- **Microsoft Agent Framework (MAF)**: AI ഏജന്റുകൾ നിർമ്മിക്കാൻ പ്രൊഡക്ഷൻ റെഡിയായ SDK. ടൂൾ കോളിംഗ്, സംവാദ മാനേജ്മെന്റ്, Azure തിരിച്ചറിയൽ സംയോജനം എന്നിവക്ക് ലളിതമായ API നൽകുന്നു.
- **Microsoft Foundry Agent Service**: Microsoft Foundry-ൽ ഉള്ള ഒരു പ്ലാറ്റ്ഫോവും വിന്യസിക്കൽ സേവനവും. Azure OpenAI, Azure AI Search, Bing Search, കോഡ് നിർവഹണം തുടങ്ങിയ സേവനങ്ങളുമായി ഇൻബിൽറ്റ് കണക്ഷൻ വാഗ്ദാനം ചെയ്യുന്നു.
 
തിരഞ്ഞെടുക്കാൻ സംശയമുണ്ടോ?

### ഉപയോഗ സമികൾ
 
ചില പൊതുവായ ഉപയോഗങ്ങൾ പരിശോധിച്ച് നിങ്ങളെ സഹായിക്കാമെന്ന് നോക്കൂ:
 
> ചോദ്യമുണ്ട്: തത്സമയം പ്രൊഡക്ഷൻ AI ഏജന്റ് ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാനാണ് ഞാൻ ആഗ്രഹിക്കുന്നത്, എളുപ്പത്തിൽ തുടങ്ങേണ്ടത് എങ്ങനെ?
>

> മറുപടി: Microsoft Agent Framework മികച്ചതാണ്. `FoundryChatClient` വഴി ടൂൾസ്, നിർദ്ദേശങ്ങൾ ഉള്ള ഏജന്റുകൾ കുറച്ച് കോഡ് ലൈൻസിൽ നിർവ്വചിക്കാം.

> ചോദ്യമുണ്ട്: Azure Search, കോഡ് നിർവഹണങ്ങൾ പോലുള്ള എന്റർപ്രൈസ് ലെവൽ ഇന്റഗ്രേഷനുകളോടെ വിന്യാസം വേണം
>
> മറുപടി: Microsoft Foundry Agent Service ഉതകും. ഇതൊരു പ്ലാറ്റ്ഫോം സേവനം, ബഹുഭാഗ മോഡലുകൾ, Azure AI Search, Bing Search, Azure Functions എന്നിവയുടെ ഇൻബിൽറ്റ് സൗകര്യങ്ങൾ നൽകുന്നു. Foundry പോർട്ടലിൽ ഏജന്റുകൾ നിർമ്മിച്ച് സ്‌കെയിലിൽ വിന്യസിക്കാനുള്ള എളുപ്പമുള്ള മാർഗം.
 
> ചോദ്യമുണ്ട്: എനിക്ക് ഇപ്പോഴും സംശയം, ഒരു ഓപ്ഷൻ മാത്രം തരൂ
>
> മറുപടി: ആദ്യം Microsoft Agent Framework ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിക്കുകയും പിന്നീട് എന്റർപ്രൈസ് വിന്യാസത്തിനായി Microsoft Foundry Agent Service ഉപയോഗിക്കുകയും ചെയ്യുക. ഇതു വഴി ഏജന്റ് ലജിക്കിൽ വേഗത്തിൽ ആവർത്തനം നടത്താനും എന്റർപ്രൈസ് വിന്യാസത്തിലേക്ക് ക്രമികരിക്കാനും സാധിക്കും.
 
പ്രധാന വ്യത്യാസങ്ങൾ പട്ടികയിൽ സംക്ഷേപിക്കുക:

| ഫ്രെയിംവർക്ക് | ശ്രദ്ധ | പ്രധാന ആശയങ്ങൾ | ഉപയോഗങ്ങൾ |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ടൂൾ കോളിംഗിന്റെ streamlined ഏജന്റ് SDK | ഏജന്റുകൾ, ടൂളുകൾ, Azure തിരിച്ചറിയൽ | AI ഏജന്റുകൾ നിർമ്മിക്കൽ, ടൂൾ ഉപയോഗം, ബഹു ഘട്ട workflow |
| Microsoft Foundry Agent Service | ഫ്ലെക്‌സിബിൾ മോഡലുകൾ, എന്റർപ്രൈസ് സുരക്ഷ, കോഡ് സൃഷ്ടി, ടൂൾ കോളിംഗ് | മോഡുലാരിറ്റി, സഹകരണ, പ്രോസസ് ഓർക്കുംസ്ട്രേഷൻ | സുരക്ഷിതം, സ്‌കെയിലബിള്‍, ലളിതമായ AI ഏജന്റ് വിന്യാസം |

## എന്റെ നിലവിലുള്ള Azure പരിസ്ഥിതി ഉപകരണങ്ങൾ നേരിട്ട് ഇണ unmarried ചെയ്യാമോ, അല്ലെങ്കിൽ സ്റ്റാൻഡ്അലോൺ പരിഹാരങ്ങൾ വേണമോ?


ഉത്തരം അതെ, നിങ്ങൾ നിലവിലുള്ള Azure പരിതസ്ഥിതി ഉപകരണങ്ങളെ നേരിട്ട് Microsoft Foundry Agent Service-നൊപ്പം സംയോജിപ്പിക്കാം, പ്രത്യേകിച്ച് ഇത് മറ്റ് Azure സേവനങ്ങളുമായി ചേർന്ന് പ്രവർത്തിക്കാൻ രൂപകല്‍പ്പന ചെയ്തിട്ടുള്ളതാണ്. ഉദാഹരണത്തിന്, നിങ്ങൾ Bing, Azure AI Search, Azure Functions എന്നിവ സംയോജിപ്പിക്കാം. Microsoft Foundry-യുമായി ആഴത്തിലുള്ള സംയോജനവും υπάρχει.

Microsoft Agent Framework-യും Azure സേവനങ്ങളുമായ സംയോജനം `FoundryChatClient`-നും Azure ഐഡന്റിറ്റിയുടെയും മാർഗം സാധ്യമാക്കുന്നു, ഇത് നിങ്ങളുടെ ഏജന്റ് ഉപകരണങ്ങളിൽ നിന്ന് നേരിട്ട് Azure സേവനങ്ങളെ വിളിക്കാൻ കഴിയും.

## സാമ്പിൾ കോഡുകൾ

- പൈത്തൺ: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- പൈത്തൺ: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ഏജന്റ് ഫ്രെയിംവർക്കുകളെക്കുറിച്ച് കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)-ൽ ചേർന്നു മറ്റു പഠനാർഥികൾക്ക് ഒപ്പം കാണുകയും, ഓഫീസ് മണിക്കൂറുകളിൽ പങ്കെടുക്കുകയും, നിങ്ങളുടെ AI ഏജന്റുകളുമായി ബന്ധപ്പെട്ട ചോദ്യങ്ങൾക്ക് ഉത്തരങ്ങൾ നേടുകയും ചെയ്യുക.

## റഫറൻസുകൾ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## മുൻ പാഠം

[AI ഏജന്റുകളുടെയും ഏജന്റ് ഉപയോഗ കേസുകൾക്കും പരിചയം](../01-intro-to-ai-agents/README.md)

## അടുത്ത പാഠം

[Agentic ഡിസൈൻ പാറ്റേണുകൾ മനസിലാക്കൽ](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->