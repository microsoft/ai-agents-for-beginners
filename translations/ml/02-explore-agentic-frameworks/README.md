[![AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ അന്വേഷിക്കൽ](../../../translated_images/ml/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണുന്നതിനായി മുകളിൽ ചിത്രത്തിൽ ക്ലിക്കുചെയ്യുക)_

# AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ അന്വേഷിക്കുക

AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ, AI ഏജന്റുകൾ സൃഷ്ടിക്കുന്നതും ഉപയോഗപ്പെടുത്തുന്നതിനും മാനേജുചെയ്യുന്നതിനുമായുള്ള പ്രവർത്തനങ്ങൾ ലളിതമാക്കാൻ രൂപകൽപ്പന ചെയ്ത സോഫ്റ്റ്വെയർ പ്ലാറ്റ്ഫോമുകളാണ്. ഈ ഫ്രെയിംവർക്കുകൾ ഡെവലപ്പർമാരെ മുൻകൂട്ടി നിർമ്മിച്ച ഘടകങ്ങൾ, ആബ്സ്ട്രാക്ഷനുകൾ, ടൂൾസുകൾ എന്നിവ നൽകി സങ്കീർണ്ണമായ AI സിസ്റ്റങ്ങൾ വികസിപ്പിക്കുന്നതിനുള്ള പ്രവാഹം സുഗമമാക്കുന്നു.

ഈ ഫ്രെയിംവർക്കുകൾ ഡെവലപ്പർമാരെ അവരുടെ അപ്ലിക്കേഷനുകളുടെ പ്രത്യേക ഭാഗങ്ങളിൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കാൻ സഹായിക്കുകയും AI ഏജന്റ് വികസനത്തിലെ സാധാരണ വെല്ലുവിളികളിൽ ഒരു സ്റ്റാൻഡേർഡൈസ് ചെയ്ത സമീപനം നൽകുകയും ചെയ്യുന്നു. AI സിസ്റ്റങ്ങൾ നിർമ്മിക്കുന്നതിൽ ഇവ സ്കെയിലബിലിറ്റി, ലഭ്യത, കാര്യക്ഷമത എന്നിവ മെച്ചപ്പെടുത്തുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ ചർച്ച ചെയ്യുന്നതുകൾ:

- AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ എന്തെല്ലാം ആണ്, ഡെവലപ്പർമാർക്കു ലഭിക്കുന്ന സാദ്ധ്യതകൾ എന്തൊക്കെയാണ്?
- ടീമുകൾ എങ്ങനെ ഇവ ഉപയോഗിച്ച് എളുപ്പത്തിൽ പ്രോട്ടോട്ടൈപ്പ്, പരിഷ്‌കരണം, ശേഷിപ്പും മെച്ചപ്പെടുത്തലും നടത്തി നടക്കാം?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ഉം <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a> ഉം) നിർമ്മിച്ച ഫ്രെയിംവർക്കുകളും ടൂളുകളും തമ്മിലുള്ള വ്യത്യാസങ്ങൾ എന്തെല്ലാം?
- നിലവിലുള്ള Azure പരിതസ്ഥിതിയിലെ ടൂളുകൾ നേരിട്ട് ഇന്റഗ്രേറ്റ് ചെയ്യാൻ സാധിക്കുമോ, അല്ലെങ്കിൽ സ്റ്റാൻഡലോൺ പരിഹാരങ്ങൾ വേണോ?
- Microsoft Foundry Agent Service എന്താണ്, ഇത് എങ്ങനെ സഹായിക്കുന്നു?

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠത്തിലെ ലക്ഷ്യങ്ങൾ:

- AI ഏജന്റ് ഫ്രെയിംവർക്കുകളുടെ പകർപ്പിൻ്റെ പങ്ക് മനസ്സിലാക്കുക.
- ബുദ്ധിമുട്ടുള്ള AI ഏജന്റുകൾ നിർമ്മിക്കാൻ AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ എങ്ങനെ ഉപയോഗിക്കാമെന്ന് അറിയുക.
- AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ സജ്ജമാക്കുന്ന പ്രധാന കഴിവുകൾ തിരിച്ചറിയുക.
- Microsoft Agent Frameworkനും Microsoft Foundry Agent Serviceനും ഇടയിലുള്ള വ്യത്യാസങ്ങൾ അറിയുക.

## AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ എന്താണു और ഡെവലപ്പർമാർക്ക് എന്ത് സാധ്യമാക്കുന്നു?

പരമ്പരാഗത AI ഫ്രെയിംവർക്കുകൾ നിങ്ങളുടെ ആപ്പുകളിൽ AI സംയോജിപ്പിച്ച് ആപ്പുകൾ മെച്ചപ്പെടുത്തുന്നതിന് സഹായിക്കുന്ന വഴികൾ താഴെപ്പറയുന്നു:

- **പരസണാത്മകത**: ഉപയോക്തൃ പെരുമാറ്റവും ഇഷ്ടങ്ങളും വിശകലനം ചെയ്ത് വ്യക്തിഗത നിർദ്ദേശങ്ങൾ, ഉള്ളടക്കം, അനുഭവങ്ങൾ നൽകുന്നു.
ഉദാഹരണം: Netflix പോലുള്ള സ്ട്രീമിംഗ് സേവനങ്ങൾ, പ്രേക്ഷണ ചരിത്രം അടിസ്ഥാനമാക്കി സിനിമകളും ഷോകളും നിർദ്ദേശിച്ച് ഉപയോക്തൃ ഏർപ്പെടലും സംതൃപ്തിയും മെച്ചപ്പെടുത്തുന്നു.
- **ഓട്ടോമേഷൻ  പിന്നീടുള്ള കാര്യക്ഷമത**: ആപേക്ഷിക ജോലികൾ ഓട്ടോമേറ്റ് ചെയ്ത് പ്രവൃത്തിയുടെയുമുള്ള പ്രവാഹം ലളിതമാക്കുകയും പ്രവർത്തനക്ഷമത വർദ്ധിപ്പിക്കുകയും ചെയ്യുന്നു.
ഉദാഹരണം: ഉപഭോക്തൃ സേവന ആപ്പുകൾ AI-ഓടുള്ള ചാറ്റ്ബോട്ടുകൾ ഉപയോഗിച്ച് സാധാരണ ചോദിച്ചൽ നേരത്തെ കൈകാര്യം ചെയ്യുന്നു. പ്രതികരണ സമയങ്ങൾ കുറയ്ക്കുകയും ക്ലിഷ്ടമായ കാര്യങ്ങൾക്ക് മനുഷ്യ ഏജന്റുമാരെ വിടുകയും ചെയ്യുന്നു.
- **ഉപയോക്തൃ അനുഭവം മെച്ചപ്പെടുത്തൽ**: വോയിസ് റെക്കോഗ്നിഷൻ, നാചുറൽ ലാംഗ്വേജ് പ്രോസസ്സിംഗ്, പ്രഡിക്ഷൻ ടെക്സ്റ്റ് പോലുള്ള ബുദ്ധിമുട്ടുള്ള സവിശേഷതകൾ ഒരുക്കുന്നു.
ഉദാഹരണം: Siri, Google Assistant പോലുള്ള വെർച്വൽ അസിസ്റ്റന്റുകൾ വോയിസ് കമാൻഡുകൾ മനസ്സിലാക്കി മറുപടി നൽകുന്നു, ഉപയോക്താക്കൾക്ക് ഉപകരണങ്ങളുമായി എളുപ്പത്തിൽ ഇടപഴകാൻ കഴിയും.

### ഇവ എല്ലാം നല്ലതാണ്, എന്നാൽ എന്തിനായി AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ വേണ്ട?

AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ സാധാരണ AI ഫ്രെയിംവർക്കുകളിൽ തോന്നുന്നതിലുപരി വലിയൊരു അവസരം പ്രതിനിധീകരിക്കുന്നു. ഇവ ഉപയോഗിച്ച് ബുദ്ധിമുട്ടുള്ള ലക്ഷ്യങ്ങൾ നേടുന്നതിനായി ഉപയോക്താക്കളുമായും മറ്റ് ഏജന്റുമാരുമായും ചർച്ച ചെയ്ത് ഇടപടിക്കുന്ന ബുദ്ധിശാലിയായ ഏജന്റുകൾ സൃഷ്ടിക്കാൻ കഴിയും. ഇവ സ്വയംതന്നെയാണ് പ്രവർത്തനം നടത്തുന്നത്, തീരുമാനങ്ങൾ എടുക്കുകയും മാറ്റം വരുന്ന സാഹചര്യങ്ങളിൽ ചേരുകയും ചെയ്യുന്നു. AI ഏജന്റ് ഫ്രെയിംവർക്കുകൾ നൽകുന്ന പ്രധാന കഴിവുകൾ:

- **എജന്റ് സഹകരണം, ഏകോപനം**: ബഹുഏജന്റ് പരിസ്ഥിതി നിർമ്മിച്ച് സമുച്ചയമായി പ്രവർത്തിക്കുകയും ആശയവിനിമയം നടത്തി ഉൾക്കാഴ്ചകൾ പങ്കിട്ടു പരിസരപ്രശ്‌ണ്ണങ്ങൾ പരിഹരിക്കാൻ കഴിയും.
- **ജോലി ഓട്ടോമേഷൻ, മാനേജുമെന്റ്**: ബഹുബാധ പ്രവർത്തനങ്ങൾ, ജോലിയിടൽ, ഡൈനാമിക് ജോലി നിയന്ത്രണം എന്നിവയ്ക്കായി മെക്കാനിസങ്ങൾ നൽകുന്നു.
- **സന്ദർഭം മനസ്സിലാക്കൽ, ഒത്തുചേരൽ**: സംപ്രേഷ്യങ്ങൾ, പരിതസ്ഥിതി തിരിച്ചറിയുകയും തികച്ചും സമയത്ത് അധിഷ്ഠിത തീരുമാനങ്ങൾ എടുക്കുകയും ചെയ്യുന്നു.

സംക്ഷേപത്തിൽ, ഏജന്റുകൾ നിങ്ങളെ അധികം ചെയ്യാനാകും, ഓട്ടോമേഷൻ ഉയർന്ന തലത്തിലേക്ക് കൊണ്ടുപോകാനും പരിതസ്ഥിതിയിൽ നിന്ന് പഠിച്ച് ചേരുന്നതും കൂടുതൽ ബുദ്ധിശാലിയായ സിസ്റ്റങ്ങൾ സൃഷ്ടിക്കാനും സഹായിക്കും.

## എങ്ങനെ വേഗത്തിൽ പ്രോട്ടോട്ടൈപ്പ്, ഐറ്ററേറ്റ്, ഏജന്റിന്റെ കഴിവുകൾ മെച്ചപ്പെടുത്താം?

ഈ മേഖലം വേഗത്തിൽ മാറുകയാണ്, എന്നാൽ മിക്ക AI ഏജന്റ് ഫ്രെയിംവർക്കുകളിലും സാധാരണ കാണപ്പെടുന്ന ചില ഘടകങ്ങൾ നിങ്ങൾക്ക് വ്യവസ്ഥാപിതമായ പ്രോട്ടോട്ടൈപ്പിംഗ് ലളിതമാക്കും: മോഡുലാർ ഘടകങ്ങൾ, സഹകരണ ടൂൾസ്, റിയൽ-ടൈം പഠനം. ഇവയെക്കുറിച്ച് നോക്കാം:

- **മോഡുലാർ ഘടകങ്ങൾ ഉപയോഗിച്ചും**: AI SDK കളിൽ AI & മെമ്മറി കണക്ടറുകൾ, ഫംഗ്ഷൻ കോൾ നാചുറൽ ലാംഗ്വേജ് അല്ലെങ്കിൽ കോഡ് പ്ലഗിൻസ് വഴി, പ്രോംപ്‌ട് ടെമ്പ്ലേറ്റുകൾ തുടങ്ങിയ മുൻകൂട്ടി നിർമ്മിച്ച ഘടകങ്ങൾ ലഭ്യമാണ്.
- **സഹകരണ ടൂൾസ് ലാഭിക്കുക**: പ്രത്യേക പ്രവർത്തനങ്ങളുള്ള ഏജന്റുകൾ രൂപകല്പന ചെയ്ത് സഹകരണ പ്രവൃത്തികൾ പരീക്ഷിക്കുകയും തൃതീയപ്പെടുത്തുകയും ചെയ്യുക.
- **റിയൽ-ടൈം പഠനം**: ഏജന്റുകൾ ഇടപഴകലുകൾ വഴി പഠിച്ച് പെരുമാറ്റം ഡൈനാമിക് ആയി ക്രമീകരിക്കുന്നത് നടപ്പിലാക്കുക.

### മോഡുലാർ ഘടകങ്ങൾ ഉപയോഗിക്കുക

Microsoft Agent Framework പോലുള്ള SDKകൾ AI കണക്ടറുകൾ, ടൂൾ നിർവചനങ്ങൾ, ഏജന്റ് മാനേജുമെന്റ് എന്നിവയ്ക്കുള്ള മുൻകൂട്ടി നിർമിത ഘടകങ്ങൾ നൽകുന്നു.

**ടീമുകൾക്ക് ഇത് എങ്ങനെ സഹായിക്കും**: ടീമുകൾ തുടക്കം മുതൽ നിർമ്മിക്കാതെ ഈ ഘടകങ്ങൾ ചേർത്ത് പ്രവർത്തനക്ഷമമായ പ്രോട്ടോട്ടൈപ്പ് ഉടൻ സൃഷ്ടിക്കാം, കൃത്യമായ പരീക്ഷണവും രീതിമാറ്റവും നടത്താൻ കഴിയും.

**പ്രായോഗികമായി ഇത് എങ്ങനെ പ്രവർത്തിക്കും**: ഉപയോക്തൃ ഇൻപുട്ടിൽ നിന്നുള്ള വിവരങ്ങൾ പുറംതള്ളുന്നതിനായി മുൻകൂട്ടി നിർമ്മിച്ച പാർസർ, ഡാറ്റ സംഗ്രഹിക്കാന് മെമ്മറി മോഡ്യൂൾ, ഉപയോക്താക്കളുമായി ചർച്ച ചെയ്യാൻ പ്രോംപ്‌റ് ജനറേറ്റർ എന്നിവ ഒരുമിച്ച് ഉപയോഗിക്കാം, എല്ലാം പൂർണ്ണമായും തുടങ്ങാതെ തന്നെ.

**ഉദാഹരണ കോഡ്**: Microsoft Agent Framework ഉപയോഗിച്ച് `FoundryChatClient` ഉപയോഗിച്ച് ഉപയോക്തൃ ഇൻപുട്ടിന് ടൂൾ കോൾ ഉപയോഗിച്ച് പ്രതികരിക്കുന്ന വിധം കാണുക:

``` python
# Microsoft Agent Framework പൈതൺ ഉദാഹരണം

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# യാത്ര ബുക്ക് ചെയ്യാൻ ഒരു സാമ്പിൾ ടൂൾ ഫംഗ്ഷൻ నిర్వചിക്കുക
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
    # ഉദാഹരണ ഔട്ട്പുട്ട്: 2025 ജനുവരി 1-നു ഇഞ്ച് ന്യൂയോർക്ക് പറക്കുന്നത് വിജയകരമായി ബുക്ക് ചെയ്‌തിരിക്കുന്നു. സുരക്ഷിത യാത്രകൾ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ഈ ഉദാഹരണത്തിൽ കാണാന് കഴിയുന്നത്, ഉപയോക്തൃ ഇൻപുട്ടിൽ നിന്നായി വിമാനം ബുക്കിങ്ങിന്റെ ഉത്ഭവം, ലക്ഷ്യം, തീയതി എന്നിവ എടുക്കാൻ മുൻകൂട്ടി നിർമ്മിച്ച പാർസർ നിങ്ങൾക്ക് ഉപയോഗിക്കാമെന്നതാണ്. ഈ മോഡുലാർ സമീപനം ഉയർന്ന നിലവാരത്തിലുള്ള ലജിക് വീട്ടിച്ച് അതിൽ കൂടുതൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കാൻ കഴിയും.

### സഹകരണ ടൂൾസ് ലാഭിക്കുക

Microsoft Agent Framework പോലുള്ള ഫ്രെയിംവർക്കുകൾ നാനാതത്വമുള്ള ഏജന്റുകൾ ഒരേ സമയം trabaho ചെയ്യുവാൻ സഹായിക്കുന്നു.

**ടീമുകൾക്ക് ഇത് എങ്ങനെ സഹായിക്കും**: പ്രത്യേക പ്രവർത്തനങ്ങളോടുകൂടെ ഏജന്റുകൾ രൂപകല്പന ചെയ്ത്, സഹകരണ പ്രവൃത്തികൾ പരീക്ഷിച്ച് മെച്ചപ്പെടുത്താം, സിസ്റ്റം കാര്യക്ഷമത വർധിപ്പിക്കാം.

**പ്രായോഗികമായി ഇത് എങ്ങനെ പ്രവർത്തിക്കും**: ഓരോ ഏജന്റിനു പ്രത്യേക പ്രവർത്തനങ്ങൾ (ഡാറ്റ റിട്രീവൽ, വിശകലനം, തീരുമാനം എടുക്കൽ) നിയോഗിച്ച ഒരു സംഘമുണ്ടാക്കാം. ഈ ഏജന്റുകൾ ആശയവിനിമയം നടത്തുകയും വിവരങ്ങൾ പങ്കുവെച്ച് ഒരു ലക്ഷ്യം നേട്ടമാക്കാൻ പ്രവർത്തിക്കും.

**ഉദാഹരണ കോഡ് (Microsoft Agent Framework)**:

```python
# മൈക്രോസോഫ്‌റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് ഒരേ സമയം പ്രവർത്തിക്കുന്ന നിരവധി ഏജന്റുകൾ സൃഷ്ടിക്കുന്നു

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ഡാറ്റ പുനഃപ്രാപ്‌തി ഏജന്റ്
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ഡാറ്റ വിശകലന ഏജന്റ്
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ഒരു പ്രവർത്തനത്തിൽ ഏജന്റുകൾ ക്രമത്തിൽ പ്രവർത്തിപ്പിക്കുക
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

മുകളിൽ നൽകിയ കോഡിൽ ബഹുഏജന്റുകൾ ചേർന്ന് ഡാറ്റ വിശകലനം ചെയ്യുന്ന ടാസ്ക് നിർമ്മിക്കുന്ന രീതി കാണിക്കുന്നു. ഏജന്റുകൾ ഓരോന്നും പ്രത്യേക പ്രവർത്തനം നിർവഹിക്കുകയും, ഇഷ്‌ടപ്പെട്ട ഫലത്തിനായി സംയോജിതമായി പ്രവർത്തിക്കുകയും ചെയ്യുന്നു. പ്രത്യേക പ്രവർത്തനങ്ങളോടുകൂടെ ഏജന്റുകൾ സൃഷ്ടിച്ചതിലൂടെ ടാസ്കിന്റെ കാര്യക്ഷമത മെച്ചപ്പെടുത്താം.

### റിയൽ-ടൈം പഠനം

മുൻനിര ഫ്രെയിംവർക്കുകൾ യഥാർത്ഥ സമയ സന്ദർഭം മനസ്സിലാക്കലും പഠനവും പ്രയോഗമാക്കാൻ കഴിവുകൾ നൽകുന്നു.

**ടീമുകൾക്ക് ഇത് എങ്ങനെ സഹായിക്കും**: ഏജന്റുകൾ ഇടപഴകലുകളിൽ നിന്നും പഠിച്ച് പെരുമാറ്റം ക്രമീകരിക്കുന്ന ഫീഡ്‌ബാക്ക് ലൂപ്പുകൾ നടപ്പിലാക്കുന്നുവെങ്കിൽ, കഴിവുകൾ സ്ഥിരമായി മെച്ചപ്പെടുത്താനും കൂടുതൽ നൈപുണ്യം നേടാനും ഇത് സഹായിക്കും.

**പ്രായോഗികമായി ഇത് എങ്ങനെ പ്രവർത്തിക്കും**: ഏജന്റുകൾ ഉപയോക്തൃ പ്രതികരണം, പരിസ്ഥിതി ഡാറ്റ, ടാസ്ക് ഫലങ്ങൾ വിശകലനം ചെയ്ത് അറിവ് പുതുക്കുകയും, തീരുമാനമെടുക്കൽ ആൾഗോരിതങ്ങൾ ക്രമീകരിക്കുകയും, സമയത്തിനൊത്ത് പ്രകടനം മെച്ചപ്പെടുത്തുകയും ചെയ്യുന്നു. ഈ പുനരാവർത്തന പഠന പ്രക്രിയ ഏജന്റുകളെ മാറ്റങ്ങളോട് യോജിപ്പിക്കാൻ സഹായിക്കുന്നു, ആകെയുള്ള സിസ്റ്റം കാര്യക്ഷമത വർധിപ്പിക്കുന്നു.

## Microsoft Agent Frameworkനും Microsoft Foundry Agent Serviceനും തമ്മിലുള്ള വ്യത്യാസങ്ങൾ എന്തെല്ലാം?

ഈ സമീപനങ്ങളെ താരതമ്യം ചെയ്യാൻ നിരവധി മാർഗ്ഗങ്ങൾ ഉണ്ട്, എന്നാൽ രൂപകൽപ്പന, കഴിവുകൾ, ലക്ഷ്യ ഉപയോഗ കേസുകൾ എന്നിവ സംബന്ധിച്ച ചില പ്രധാന വ്യത്യാസങ്ങൾ നോക്കാം:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework, `FoundryChatClient` ഉപയോഗിച്ച് AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ലളിതമായ SDK ആണ്. ഇത് ഡെവലപ്പർമാർക്ക് Azure OpenAI മോഡലുകൾ ഉപയോഗിച്ച് ടൂൾ കോൾ, സംവാദ മാനേജുമെന്റ്, Azure ഐഡന്റിറ്റി പോലുള്ള എന്റർപ്രൈസ്-ഗ്രേഡ് സുരക്ഷ എന്നിവ ഉൾപ്പെടുത്തിയ AI ഏജന്റുകൾ ആസൂത്രണം ചെയ്യാനും സൃഷ്ടിക്കാനും കഴിയും.

**ഉപയോഗ കാര്യങ്ങൾ**: ടൂൾ ഉൾപ്പെടുത്തൽ, ബഹുവിധം പ്രവർത്തന പ്രവാഹങ്ങൾ, എന്റർപ്രൈസ് സംയോജന രംഗങ്ങൾ എന്നിവ ഉപയോഗിച്ച് നിർമാണം പ്രമാദ്ധതയുള്ള AI ഏജന്റുകൾ ഉണ്ടാക്കൽ.

Microsoft Agent Framework-ന്റെ ചില പ്രധാന ആശയങ്ങൾ:

- **ഏജന്റുകൾ**. `FoundryChatClient` വഴിയാണ് ഏജന്റുകൾ സൃഷ്ടിക്കുന്നത്. ഏജന്റിന് പേര്, നിർദ്ദേശങ്ങൾ, ടൂളുകൾ ക്രമീകരിക്കാം. ഏജന്റ് ചെയ്യും:
  - **ഉപയോക്തൃ സന്ദേശങ്ങൾ പ്രോസസ് ചെയ്തു മറുപടി സൃഷ്ടിക്കുന്നു** Azure OpenAI മോഡലുകൾ ഉപയോഗിച്ച്.
  - **സംവാദ സന്ദർഭത്തെ അടിസ്ഥാനമാക്കി ടൂൾസ് ഓട്ടോമാറ്റിക് കോൾ ചെയ്യുന്നു.**
  - **ഒട്ടും സംവാദം നിലനിര്‍ത്തുന്നു** പല ഇടപെടലുകളിലുടനീളം.

  ഏജന്റ് സൃഷ്ടിക്കുന്നതിന് ഈ കോഡ് ഫ്രാഗ്മെന്റ് കാണുക:

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

- **ടൂളുകൾ**. ഫ്രെയിംവർക്ക്, ഏജന്റ് സ്വയം പ്രവർത്തിപ്പിക്കാൻ പൈതൺ ഫംഗ്ഷനുകൾ ടൂൾസായി നിർവചിക്കാനാകും. ടൂളുകൾ ഏജന്റ് സൃഷ്ടിക്കുമ്പോൾ രജിസ്റ്റർ ചെയ്യുന്നു:

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

- **ബഹുഏജന്റ് ഏകോപനം**. വ്യത്യസ്ത സവിശേഷതകളുള്ള ബഹുഏജന്റുകൾ സൃഷ്ടിച്ച് അവരുടെ പ്രവർത്തനം ഏകോപിപ്പിക്കാം:

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

- **Azure ഐഡന്റിറ്റി ഇന്റഗ്രേഷൻ**. API കീകൾ കൈകാര്യം ചെയ്യാതെ സുരക്ഷിത ഇൻതെന്റിഫിക്കേഷൻ കൂടാതെ `AzureCliCredential` അല്ലെങ്കിൽ `DefaultAzureCredential` ഉപയോഗിക്കുന്നു.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service Microsoft Ignite 2024 ൽ അവതരിപ്പിച്ച പുതിയ സേവനമാണ്. Llama 3, Mistral, Cohere പോലുള്ള ഓപ്പൺ സോഴ്‌സ് LLM-കൾ നേരിട്ട് കോൾ ചെയ്യാനാകുന്ന കൂടുതൽ വായനാവേണ്ട മോഡലുകളുള്ള AI ഏജന്റുകൾ വികസിപ്പിക്കാനും വിന്യസിക്കാനും ഇത് സഹായിക്കുന്നു.

Microsoft Foundry Agent Service ശക്തമായ എന്റർപ്രൈസ് സുരക്ഷാ സംവിധാനങ്ങളും ഡാറ്റ സംഭരണ രീതികളും നൽകുന്നു, എന്റർപ്രൈസ് അപേക്ഷകൾക്കു അനുയോജ്യമാണ്.

ഇത് Microsoft Agent Framework-നൊപ്പം ചേർന്ന് ഏജന്റുകൾ നിർമ്മിക്കുകയും വിന്യസിക്കുകയും ചെയ്യാൻ ഔട്ട്ഓഫ് ദി ബോക്സ് പ്രവർത്തിക്കുന്നു.

ഇപ്പോൾസേവനം പബ്ലിക് പ്രവ്യൂവിലുമാണ്, Python, C# എന്നിവയിൽ ഏജന്റുകൾ സൃഷ്ടിക്കാൻ പിന്തുണ നല്‍കുന്നു.

Microsoft Foundry Agent Service Python SDK ഉപയോഗിച്ച് ഉപയോക്തൃ നിർവചിച്ച ടൂൾ ഉപയോഗിച്ചുള്ള ഏജന്റ് എങ്ങനെ സൃഷ്ടിക്കാമെന്ന് കാണുക:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ടൂൾ ഫംഗ്ഷനുകൾ നിർവ്വചിക്കുക
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
        model="gpt-4.1-mini",
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

Microsoft Foundry Agent Service-ന് താഴെപ്പറയുന്ന പ്രധാന ആശയങ്ങളുണ്ട്:

- **ഏജന്റ്**. Microsoft Foundry Agent Service Microsoft Foundry-വുമായ സംയോജനം ആണ്. AI ഏജന്റ് ഒരു "സ്മാർട്ട്" മൈക്രോസർവിസായി പ്രവർത്തിച്ച് ചോദ്യങ്ങൾക്ക് ഉത്തരം നൽകാനും (RAG), പ്രവർത്തനങ്ങൾ നടത്താനും, പ്രവൃത്തിത്തന്ത്രങ്ങൾ മുഴുവൻ ഓട്ടോമേറ്റുചെയ്യാനും കഴിയും. സൃഷ്‌ടിക്കുന്നതിനു വലിയ AI മോഡലുകളും യഥാർത്ഥ ഡാറ്റാകുറ്റുകളും പിന്തുണയോടെയുള്ള ടൂളുകളും ചേർക്കുന്നു. ഒരു ഏജന്റിൻ്റെ ഉദാഹരണം:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ഈ ഉദാഹരണത്തിൽ, `gpt-4.1-mini` മോഡലും `my-agent` പേരും `You are helpful agent` നിർദ്ദേശവും ഉപയോഗിച്ച് ഏജന്റ് സൃഷ്ടിച്ചിരിക്കുന്നു. കോഡ് വ്യാഖ്യാനം പ്രവർത്തനങ്ങൾക്ക് ടൂളുകളും വിഭവങ്ങളും ഏജന്റിന് നൽകിയിട്ടുണ്ട്.

- **ത്രീഡ്, സന്ദേശങ്ങൾ**. ത്രീഡ് മറ്റൊരു പ്രധാന ആശയമാണ്. ഉപയോക്താവിനും ഏജന്റിനും ഇടയിലുള്ള സംവാദം അല്ലെങ്കിൽ ഇടപെടൽ പ്രതിനിധീകരിക്കുന്നു. സംവാദത്തിന്റെ പുരോഗതി, സന്ദർഭ വിവരങ്ങൾ സൂക്ഷിക്കൽ, ഇടപെടൽ അവസ്ഥ നിയന്ത്രണം എന്നിവയ്ക്ക് ത്രീഡ് ഉപയോഗിക്കും. ഒരു ത്രീഡ് ഉദാഹരണം:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ഏജന്റിനെ ത്രെഡിൽ ജോലി നിർവഹിക്കാൻ ആവശ്യപ്പെടുക
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ഏജന്റിന്റെ പ്രതികരണം കാണാൻ എല്ലാ സന്ദേശങ്ങളും പരിഗണിച്ച് ലോഗു ചെയ്യുക
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    മുൻകോഡിൽ ഒരു ത്രീഡ് സൃഷ്ടിച്ച് സന്ദേശം അയച്ചിരിക്കുന്നു. `create_and_process_run` വിളിച്ചു ഏജന്റിനെ ത്രീഡിൽ ജോലി ചെയ്യാൻ ആവശ്യപ്പെടുന്നു. അവസാന ഘട്ടത്തിൽ സന്ദേശങ്ങൾ വീണ്ടെടുക്കുകയും ഏജന്റിൻ്റെ മറുപടി ലോഗ് ചെയ്യുകയും ചെയ്യുന്നു. സന്ദേശങ്ങൾ ഉപയോക്താവിനും ഏജന്റിനും തമ്മിലുള്ള സംവാദ പുരോഗതി സൂചിപ്പിക്കുന്നു. സന്ദേശങ്ങളിൽ വാചകം, ചിത്രം, ഫയൽ എന്നിവ അടങ്ങിയിരിക്കും, ഉദാഹരണത്തിന് ഏജന്റിന്‍റെ പ്രവർത്തനം ഡോക്യുമെന്റ് അല്ലെങ്കിൽ ചിത്രം സൃഷ്ടിച്ചിരിക്കാം. ഡെവലപ്പർ ഈ വിവരങ്ങൾ മറുപടി പ്രോസസ്സ് ചെയ്യാൻ അല്ലെങ്കിൽ ഉപയോക്താവിന് കാണിക്കാൻ ഉപയോഗിക്കാം.

- **Microsoft Agent Framework-നൊപ്പം സംയോജനം**. Microsoft Foundry Agent Service Microsoft Agent Framework-നൊപ്പം ചേർന്ന് പ്രവർത്തിക്കുന്നു, അതായത് `FoundryChatClient` ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിച്ച് ഏജന്റ് സേവനം വഴി പ്രൊഡക്ഷൻ സാഹചര്യങ്ങളിൽ വിന്യസിക്കാം.

**ഉപയോഗ വിഷയങ്ങൾ**: Microsoft Foundry Agent Service സുരക്ഷിതം, സ്കെയിലബിൾ, ഫ്ലെക്സിബിൾ AI ഏജന്റ് വിന്യാസം ആവശ്യമായ എന്റർപ്രൈസ് അപേക്ഷകൾക്കാണ് രൂപകൽപ്പന ചെയ്തിരിക്കുന്നത്.

## ഈ സമീപനങ്ങളിൽ എന്ത് വ്യത്യാസമുണ്ട്?
 
മിക്കപ്പേരിലും ഇരു പ്ലാറ്റ്ഫോമുകളും ഒരൊന്നെപ്പോലെയാണ് തോന്നാറുള്ളത്, എന്നാൽ രൂപകൽപ്പന, കഴിവുകൾ, ലക്ഷ്യ ഉപയോഗ മേഖലകൾ എന്നിവയിൽ ചില പ്രധാന വ്യത്യാസങ്ങൾ ഉണ്ട്:
 
- **Microsoft Agent Framework (MAF)**: ടൂൾ കോൾ, സംവാദ മാനേജുമെന്റ്, Azure ഐഡന്റിറ്റി ഇന്റഗ്രേഷൻ എന്നിവയുള്ള പ്രൊഡക്ഷൻ റെഡി SDK ആണ്.
- **Microsoft Foundry Agent Service**: Microsoft Foundry-ൽ ഏജന്റുകൾക്കുള്ള പ്ലാറ്റ്ഫോം, Azure OpenAI, Azure AI Search, Bing Search, കോഡ് എക്സിക്യൂഷൻ തുടങ്ങിയ സേവനങ്ങളുമായുള്ള ഇൻബിൽറ്റ് കണക്ടിവിറ്റി.
 
ഇനിയും തീരുമാനമെടുക്കാൻ ബുദ്ധിമുട്ടാണോ?

### ഉപയോഗ കേസുകൾ
 
ചില സാധാരണ ഉപയോഗ കേസുകൾ വഴി സഹായമാകാമോ നോക്കാം:
 
> Q: ഞാൻ പ്രൊഡക്ഷൻ റെഡി AI ഏജന്റ് അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുകയാണ്, വേഗത്തിൽ തുടങ്ങേണ്ടത് എങ്ങനെ?
>

>A: Microsoft Agent Framework മികച്ച ഓപ്ഷൻ ആണ്. `FoundryChatClient` വഴി ലളിതവും പൈതോണിക് API വഴി ടൂൾസ്, നിർദ്ദേശങ്ങൾ കുറച്ച് വരി കോഡിൽ ഡിഫൈൻ ചെയ്യാം.

>Q: എന്റർപ്രൈസ് ഗ്രേഡ് വിന്യാസം, Azure Search, കോഡ് എക്സിക്യൂഷൻ പോലുള്ള ഇൻറഗ്രേഷനുകൾ വേണം.
>
> A: Microsoft Foundry Agent Service ഏറ്റവും അനുയോജ്യമാണ്. ഇത് പല മോഡലുകൾക്കും Azure AI Search, Bing Search, Azure Functions പോലുള്ള സേവനങ്ങൾക്കും ഇൻബിൽറ്റ് പിന്തുണ നൽകുന്ന പ്ലാറ്റ്ഫോം സേവനം ആണ്. Foundry പോർട്ടലിൽ ഏജന്റുകൾ എളുപ്പത്തിൽ നിർമ്മിച്ച് സ്കെയിലിൽ വിന്യസിക്കാൻ കഴിയും.
 
> Q: ഞാൻ ഇപ്പോഴും നിർണ്ണയിക്കാതെ困惑, ഒരു ഓപ്ഷൻ മാത്രം പറയൂ.
>
> A: ആദ്യം Microsoft Agent Framework ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിക്കുക, പിന്നീട് പ്രൊഡക്ഷൻ വിന്യാസത്തിനായി Microsoft Foundry Agent Service ഉപയോഗിക്കുക. ഇത്തരം സമീപനം ഏജന്റ് ലജിക് വേഗത്തിൽ മുന്നോട്ട് കൊണ്ടുപോകാനും എന്റർപ്രൈസ് വിന്യാസത്തിലേക്ക് വ്യക്തമായ മാർഗ്ഗം നല്കുകയും ചെയ്യും.
 
പ്രധാന വ്യത്യാസങ്ങൾ പട്ടികയിൽ സംക്ഷേപിക്കാം:

| ഫ്രെയിം‌വർക്ക് | കേന്ദ്ര ഫോകസ് | പ്രധാന ആശയങ്ങൾ | ഉപയോഗ കേസുകൾ |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ടൂൾ കോൾ, streamlined ഏജന്റ് SDK | ഏജന്റുകൾ, ടൂളുകൾ, Azure ഐഡന്റിറ്റി | AI ഏജന്റുകൾ നിർമ്മിക്കൽ, ടൂൾ ഉപയോഗം, ബഹു-ഘട്ട പ്രവൃത്തി |
| Microsoft Foundry Agent Service | ഫ്ലെക്സിബിൾ മോഡലുകൾ, എന്റർപ്രൈസ് സുരക്ഷ, കോഡ് ജനറേഷൻ, ടൂൾ കോൾ | മോട്യുലാറിറ്റി, സഹകരണ പ്രവർത്തനം, പ്രോസസ് ഓർക്കസ്ട്രേഷൻ | സുരക്ഷിതം, സ്കെയിലബിൾ, ഫ്ലെക്സിബിൾ AI ഏജന്റ് വിന്യാസം |

## നിലവിലുള്ള Azure പരിതസ്ഥിതിയിലെ ടൂളുകൾ നേരിട്ട് ഇന്റഗ്രേറ്റ് ചെയ്യാമോ, സ്റ്റാൻഡലോൺ പരിഹാരങ്ങളാണ് വേണ്ടത്?


ഉത്തരം അതെ, നിങ്ങൾ നിലവിലുള്ള Azure വാതാവരണം ടൂളുകൾ Microsoft Foundry Agent Service-നോടു നേരിട്ട് സംയോജിപ്പിക്കാൻ കഴിയും, പ്രത്യേകിച്ച് അത് മറ്റു Azure സേവനങ്ങളുമായി സാരവൽകമായി പ്രവർത്തിക്കാൻ രൂപകൽപ്പന ചെയ്‌തതിനാൽ. ഉദാഹരണത്തിന്, ബിംഗ്, Azure AI Search, Azure Functions എന്നിവ സംയോജിപ്പിക്കാം. Microsoft Foundry-യുമായി കൂടുതൽ ലളിതമായ സംയോജനം ഉണ്ട്.

Microsoft Agent Framework `FoundryChatClient`-ഉം Azure ഐഡന്റിറ്റിയും വഴി Azure സേവനങ്ങളുമായി സംയോജിപ്പിക്കുന്നു, അതിലൂടെ നിങ്ങളുടെ ഏജന്റ് ടൂളുകളിൽ നിന്ന് നേരിട്ട് Azure സേവനങ്ങളെ വിളിക്കാം.

## സാമ്പിൾ കോഡുകൾ

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ഏജന്റ് ഫ്രെയിമ്വർക്കുകളെക്കുറിച്ചും കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ലിൽ ചേരൂ, മറ്റ് പഠനക്കാരെ കാണാനും ഓഫീസ് മണിക്കൂറുകളിൽ പങ്കെടുക്കാനും നിങ്ങളുടെ AI ഏജന്റുമാരുടെ ചോദ്യങ്ങൾക്ക് ഉത്തരം ലഭിക്കാനും.

## റഫറൻസുകൾ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## മുമ്പത്തെ പാഠം

[AI ഏജന്റ്മാരുടെയും ഏജന്റ് ഉപയോഗകേസുകളുടെയും പരിചയം](../01-intro-to-ai-agents/README.md)

## അടുത്ത പാഠം

[Agentic ഡിസൈൻ പാറ്റേണുകളെ മനസ്സിലാക്കുക](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->