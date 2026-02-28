[![AI ഏജന്റ് ഫ്രെയിംവർക്‌സ് പരീക്ഷണം](../../../translated_images/ml/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ഈ പാഠത്തിന്റെ വീഡിയോകൾ കാണാൻ മേൽ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്യുക)_

# AI ഏജന്റ് ഫ്രെയിംവർക്‌സ് യാത്ര ചെയ്യുക

AI ഏജന്റ് ഫ്രെയിംവർക്‌സ് AI ഏജന്റുകളുടെയൊരു സൃഷ്ടി, വിന്യാസം, വിജയകരമായ നിയന്ത്രണം എളുപ്പമാക്കാൻ രൂപകൽപ്പന ചെയ്ത സോഫ്റ്റ്‌വేర్ പ്ലാറ്റ്‌ഫോമാണ്. ഈ ഫ്രെയിംവർക്‌സ് വികസകർക്ക് മുൻകെട്ടിയ ഘടകങ്ങൾ, സാരാംശങ്ങൾ, ഉപകരണങ്ങൾ നൽകുന്നു, അത് കോംപ്ലെക്സ് AI സിസ്റ്റങ്ങൾ വികസിപ്പിക്കുന്നത് ലാഭകരമാക്കുന്നു.

AI ഏജന്റ് വികസനത്തിൽ സാധാരണ സവാലുകൾക്ക് സാങ്കേതികരീതികൾ നൽകിക്കൊണ്ട്, ഇവ വികസകർക്ക് അവരുടെ അപ്ലിക്കേഷനുകളുടെ വ്യത്യസ്തമായ ഭാഗങ്ങളിൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കാൻ സഹായിക്കുന്നു. ഇവ AI സിസ്റ്റങ്ങളുടെ വ്യാപ്തിവൽക്കരണം, ലഭ്യത, കാര്യക്ഷമത മെച്ചപ്പെടുത്തുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ തരംപറയുന്നത്:

- AI ഏജന്റ് ഫ്രെയിംവർക്‌സ് എന്തെല്ലാം ആണ്, വികസകർക്ക് എന്ത് സാധ്യമാക്കുന്നു?
- ടീങ്ങൾ എങ്ങനെ ഇതുപയോഗിച്ച് തങ്ങൾക്ക് ഏജന്റിന്റെ കഴിവുകൾ പെട്ടെന്ന് മാതൃകാപ്രാപ്‌തമാക്കാനും തിരുത്താനും മെച്ചപ്പെടുത്താനുമാകും?
- മൈക്രോസോഫ്റ്റ് (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> എന്നും <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a> എന്നും) ഉണ്ടാക്കുന്ന ഫ്രെയിംവർക്‌സ്, ഉപകരണങ്ങൾ തമ്മിലുള്ള വ്യത്യാസങ്ങൾ എന്തെല്ലാം?
- എനിക്ക് ഉള്ള Azure അന്താരാഷ്ട്ര ഉപകരണങ്ങൾ നേരിട്ട് ഇന്റഗ്രേറ്റ് ചെയ്യാമോ, അല്ലെങ്കിൽ സ്വതന്ത്ര പരിഹാരങ്ങൾ ആവശ്യമാണോ?
- Azure AI Agents സര്‍വീസ് എന്താണ്, എങ്ങനെ ഇത് എനിക്ക് സഹായിക്കുന്നു?

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠത്തിന്റെ ലക്ഷ്യങ്ങൾ:

- AI ഏജന്റ് ഫ്രെയിംവർക്‌സിന്റെ AI വികസനത്തിലെ പങ്ക് മനസ്സിലാക്കുക.
- ബുദ്ധിമുട്ടുള്ള ഏജന്റ്സ് നിർമ്മിക്കാൻ AI ഏജന്റ് ഫ്രെയിംവർക്‌സ് എങ്ങനെ പ്രയോജനപ്പെടുത്താം.
- AI ഏജന്റ് ഫ്രെയിംവർക്‌സ് സജ്ജമാക്കുന്ന പ്രധാന കഴിവുകൾ.
- Microsoft Agent Framework ഉം Azure AI Agent Service ഉം തമ്മിൽ വ്യത്യാസങ്ങൾ.

## AI ഏജന്റ് ഫ്രെയിംവർക്സ് എന്ത്‌ ആണ്, വികസകർക്ക് എന്ത് സാധ്യമാക്കുന്നു?

പരമ്പരാഗത AI ഫ്രെയിംവർക്സ്, AI നിങ്ങളുടെ ആപ്പുകളിൽ ഉൾപ്പെടുത്താനും, ആപ്പുകൾ മെച്ചപ്പെടുത്താനും താഴെ പറയുന്ന മാർഗങ്ങളിൽ സഹായിക്കുന്നു:

- **വ്യക്തിഗതമാക്കൽ**: ഉപയോക്തൃ പെരുമാറ്റവും ഇഷ്ടങ്ങളും വിശകലനം ചെയ്ത് വ്യക്തിഗത നിർദേശങ്ങൾ, ഉള്ളടക്കം, അനുഭവങ്ങൾ നൽകുന്നു.
ഉദാഹരണം: Netflix പോലുള്ള സ്ട്രീമിംഗ് സേവനങ്ങൾ പാർശ്വം നോണ്ടു മൂവികളും ഷോകളും നിർദ്ദേശിച്ച് ഉപയോക്തൃ ബന്ധം മെച്ചപ്പെടുത്തുന്നു.
- **തൻസമർപ്പണം, കാര്യക്ഷമത**: ആവർത്തിച്ചുള്ള ജോലികൾ ഓട്ടോമേറ്റ് ചെയ്ത് പ്രവര്‍ത്തനപ്രവാഹങ്ങൾ ലളിതമാക്കുകയും കാര്യക്ഷമത ഉയർത്തുകയും ചെയ്യുന്നു.
ഉദാഹരണം: ഉപഭോക്തൃ സേവന ആപ്പുകൾ സാധാരണ ഗതിവിവരങ്ങൾ കൈകാര്യം ചെയ്യാൻ AI-പോവുള്ള ചാറ്റ്ബോട്ടുകൾ ഉപയോഗിച്ച് പ്രതികരണ സമയം കുറച്ചു മനുഷ്യ ഏജന്റുകൾക്ക് സങ്കീർണ്ണകാര്യങ്ങൾ കൈകാര്യം ചെയ്യാനുള്ള സമയം നൽകുന്നു.
- **ഉപയോക്തൃ അനുഭവം മെച്ചപ്പെടുത്തൽ**: വോയ്‌സ് തിരിച്ചറിവ്, സ്വാഭാവിക ഭാഷാ പ്രോസസ്സിംഗ്, പ്രവചനാത്മക വാചകം തുടങ്ങിയ ബുദ്ധിമുട്ടുള്ള പ്രവർത്തനങ്ങൾ നൽകുന്നു.
ഉദാഹരണം: Siri, Google Assistant പോലുള്ള വിർച്ച്വൽ അസിസ്റ്റന്റുകൾ വോയ്‌സ് കമാൻഡുകൾ മനസ്സിലാക്കി പ്രതികരിക്കുന്നതിനായി AI ഉപയോഗിക്കുന്നു, ഉപയോക്താക്കൾക്ക് ഉപകരണങ്ങളുമായി ഇടപഴകാൻ എളുപ്പമാക്കുന്നു.

### എല്ലാം നല്ലതല്ലേ, എന്നാൽ AI ഏജന്റ് ഫ്രെയിംവർക്സ് വേണ്ടതെന്തിന്?

AI ഏജന്റ് ഫ്രെയിംവർക്‌സ് AI ഫ്രെയിംവർക്സ് മാത്രം അല്ല, കൂടുതൽ ഒന്നാണ്. ഉപയോക്താക്കളുമായി, മറ്റ് ഏജന്റുകളുമായി, പരിസ്ഥിതിയുമായി ഇടപഴകാൻ കഴിയുന്ന ബുദ്ധിമുട്ടുള്ള ഏജന്റുകൾ നിർമ്മിക്കാൻ ഇത് രൂപകൽപ്പന ചെയ്തിരിക്കുന്നു. ഈ ഏജന്റുകൾ സ്വയംപ്രത്യക്ഷമായ പെരുമാറ്റം കാഴ്ചവയ്ക്കുകയും തീരുമാനങ്ങൾ എടുക്കുകയും ചുറ്റുപട്ട് മാറിയ സാഹചര്യങ്ങൾക്ക് അനുയോജ്യമായിത്തന്നെ മാറുകയും ചെയ്യും. AI ഏജന്റ് ഫ്രെയിംവർക്സ് സാധ്യമാക്കുന്ന പ്രാഥമിക കഴിവുകൾ:

- **ഏജന്റ് സഹകരണം, സംവരണം**: നിരവധി AI ഏജന്റുകൾ ചേർന്ന് സഹകരിച്ച്, ആശയവിനിമയം നടത്തി, സങ്കീർണ്ണ ജോലികൾ പരിഹരിക്കാൻ.
- **ജോലി ഓട്ടോമേഷൻ, മാനേജ്മെന്റ്**: ബഹു-പടിയുള്ള പ്രവൃത്തികൾ ഓട്ടോമേറ്റുചെയ്യൽ, ജോലി നിയോഗം, ഏജന്റുകൾക്ക് ഇടയിൽ പ്രഗത്ഭതാപൂര്‍വ്വമായ ജോലിപ്രവൃത്തി നിയന്ത്രണം.
- **സന്ദർഭാനുകൂല ബോധ്യവും അനുകൂലവും**: ഏജന്റുകൾക്ക് വിവക്ഷയുടെയെങ്കിലും പശ്ചാത്തലം മനസ്സിലാക്കാനും, സാഹചര്യത്തിന് സരിക്കെത്താനും, യഥാർഥസമയം വിവരങ്ങളുടെ അടിസ്ഥാനത്തിൽ തീരുമാനങ്ങൾ എടുക്കാനുമുള്ള കഴിവ്.

ചുരുക്കത്തിൽ, ഏജന്റുകൾ അധികം കാര്യങ്ങൾ ചെയ്യാനും, ഓട്ടോമേഷൻ അടുത്ത വ്യത്യാസത്തിലേക്ക് കൊണ്ടുപോകാനും, പരിസ്ഥിതിയിൽ നിന്നുള്ള പഠനവും അനുയോജ്യമായ മാറ്റങ്ങളും ചെയ്യാനുമുള്ള ബുദ്ധിമുട്ടുള്ള സംവിധാനങ്ങൾ സൃഷ്ടിക്കാനുമാണ് സഹായിക്കുന്നത്.

## ഏജന്റിന്റെ കഴിവുകൾ എങ്ങനെ പെട്ടെന്ന് മാതൃകാപ്രാപ്‌തമാക്കി, തിരുത്തി മെച്ചപ്പെടുത്താം?

ഈ മേഖലയിലെ പുരോഗതി വേഗത്തിലാണ്, എന്നാൽ പല AI ഏജന്റ് ഫ്രെയിംവർക്‌സിലും സാധാരണ രൂപത്തിൽ ഉള്ള ഘടകങ്ങൾ, സഹകരണ ഉപകരണങ്ങൾ, യഥാർഥസമയം പഠനം എന്നിവ വേഗത്തിൽ മാതൃകാപ്രാപ്‌തമാക്കാനും തിരുത്താനും സഹായിക്കുന്നു. നമുക്ക് ഇവ പരിശോധിക്കാം:

- **മൊഡ്യുലാർ ഘടകങ്ങൾ ഉപയോഗിക്കുക**: AI SDKകൾ മുൻകൂട്ടി നിർമ്മിച്ച ഘടകങ്ങൾ (AI, മെമ്മറി കണക്ടറുകൾ, സ്വാഭാവിക ഭാഷ ഉപയോഗിച്ചോ കോഡ് പ്ലഗിനുകളായോ ഫംഗ്ഷൻ കോളിംഗ്, പ്രംപ്റ്റ് ടെംപ്ലേറ്റുകൾ) എന്നിവ നൽകുന്നു.
- **സഹകരണ ഉപകരണങ്ങൾ പ്രയോജനപ്പെടുത്തുക**: പ്രത്യേക പദവികളും ജോലികളും തിരിച്ചറിയുന്ന പ്രഭാഷികളുള്ള ഏജന്റുകൾ രൂപകൽപ്പന ചെയ്യുക, ഇവയുടെ പ്രവർത്തനങ്ങൾ പരീക്ഷിച്ച് മെച്ചപ്പെടുത്തുക.
- **യഥാർത്ഥസമയം പഠനം**: ഏജന്റുകൾ ഇടപഴകരുന്നതിൽ നിന്നു പഠിച്ച് പെരുമാറ്റം ചാരുതാനുസരമായി ക്രമീകരിക്കുന്ന ഫീഡ്ബാക്ക് ലൂപുകൾ നടപ്പിലാക്കുക.

### മൊഡ്യുലാർ ഘടകങ്ങൾ ഉപയോഗിക്കുക

Microsoft Agent Framework പോലുള്ള SDKകൾ മുൻകൂട്ടി നിർമ്മിച്ച ഘടകങ്ങൾ (AI കണക്ടറുകൾ, ഉപകരണ നിർവ്വചനങ്ങൾ, ഏജന്റ് മാനേജ്‌മെന്റ്) നൽകുന്നു.

**ടിിമുകൾ എങ്ങനെ ഇത് ഉപയോഗിക്കാം**: ടീമുകൾ ഈ ഘടകങ്ങൾ ചുരുങ്ങിയ സമയത്തിൽ ചേർത്ത് പ്രവർത്തനക്ഷമമായ മാതൃക നിർമ്മിക്കാം, തുടർന്ന് വേഗത്തിൽ പരീക്ഷണങ്ങളും തിരുത്തലുകളും നടത്താം.

**പ്രായോഗികമായി ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു**: ഉപയോക്തൃ ഇൻപുട്ടിൽ നിന്ന് വിവരങ്ങൾ മാറ്റി പിടിക്കാൻ മുൻകെട്ടി നിർമ്മിച്ച പാഴ്സർ, ഡേറ്റ സൂക്ഷിക്കാൻ മെമ്മറി മാഡ്യൂൾ, ഉപയോക്താക്കളുമായി ഇടപഴകാനായി പ്രംപ്റ്റ് ജനറേറ്റർ എന്നിവ ഉപയോഗിക്കാം, മുഴുവൻ ഘടകങ്ങളും ആദ്യം മുതൽ നിർമ്മിക്കേണ്ട ആവശ്യമില്ല.

**ഉദാഹരണ കോഡ്**. Microsoft Agent Framework ഉപയോഗിച്ച് `AzureAIProjectAgentProvider` ഉപയോഗിച്ച് ഉപയോക്തൃ ഇൻപുട്ടിന് ടൂൾ കോളിംഗ് സാങ്കേതികവിദ്യ ഉപയോഗിച്ച് പ്രതികരിക്കാനുള്ള ഒരു കോഡ് ഉദാഹരണം പരിഗണിക്കാം:

``` python
# Microsoft Agent Framework Python ഉദാഹരണം

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# യാത്ര ബുക്ക് ചെയ്യാനുള്ള ഒരു സാമ്പിൾ ടൂൾ ഫംഗ്ഷൻ നിർവചിക്കുക
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
    # ഉദാഹരണ ഔട്ട്പുട്ട്: 2025 ജനുവരി 1-ന് ന്യൂയോർക്കിലേക്ക് നിങ്ങളുടെ വിമാനം വിജയകരമായി ബുക്ക് ചെയ്തിരിക്കുന്നു. സുരക്ഷിത യാത്രകൾ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ഈ ഉദാഹരണത്തിൽ കാണുന്നത് ഉപയോക്തൃ ഇൻപുട്ടിൽ നിന്നും ഒരു മുൻകൂട്ടി നിർമിച്ച പാഴ്സറിനെ ഉപയോഗിച്ച് പ്രധാന വിവരങ്ങൾ (ഉദാഹരണത്തിന്, ആഗമന സ്ഥലം, ലക്ഷ്യം, യാത്ര തീയതി) എങ്ങനെ എടുക്കാമെന്ന് ആണ്. ഈ മൊഡ്യുലാർ സമീപനം ഉയർന്ന ലെവൽ ലlogic ്ഗിക്കിൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കാൻ സഹായിക്കുന്നു.

### സഹകരണ ഉപകരണങ്ങൾ പ്രയോജനപ്പെടുത്തുക

Microsoft Agent Framework പോലുള്ള ഫ്രെയിംവർക്സ് ഒന്നിച്ച് പ്രവർത്തിക്കുന്ന നിരവധി ഏജന്റുകളുടെ സൃഷ്ടിയെ സഹായിക്കുന്നു.

**ടിിമുകൾ എങ്ങനെ ഇത് ഉപയോഗിക്കാം**: പ്രത്യേക പദവികളും ജോലികളും സവിശേഷമായി നിർദ്ദേശിച്ച്, ചേർന്ന് പ്രവർത്തിക്കുന്ന പ്രവൃത്തികൾ പരീക്ഷിച്ചു മെച്ചപ്പെടുത്താം, ആകെ സിസ്റ്റം കാര്യക്ഷമത കൂട്ടാം.

**പ്രായോഗികമായി ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു**: ഓരോ ഏജന്റും ഡേറ്റാ ശേഖരണം, വിശകലനം, തീരുമാനമെടുക്കൽ തുടങ്ങിയ പ്രത്യേക ഫംഗ്ഷനുകൾ വഹിക്കുന്ന ഏജന്റുകളുടെ ടീം നിങ്ങൾ സൃഷ്ടിക്കാം. ഇവ പരസ്പരം ആശയവിനിമയം നടത്തുകയും വിവരങ്ങൾ പങ്കുവെച്ചു പൊതുവായ ലക്ഷ്യം നേടുകയും ചെയ്യും, ഉദാഹരണത്തിന് ഉപയോക്തൃ ചോദ്യം മറുപടി നൽകൽ അല്ലെങ്കിൽ കടമ പൂർത്തിയാക്കൽ.

**ഉദാഹരണ കോഡ് (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework ഉപയോഗിച്ച് സഹകരിച്ച് പ്രവർത്തിക്കുന്ന ഒന്നിലധികം ഏജന്റുകൾ സൃഷ്ടിക്കൽ

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ഡേറ്റാ വീണ്ടെടുക്കൽ ഏജന്റ്
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ഡേറ്റാ വിശകലന ഏജന്റ്
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ഒരു ടാസ്ക്കിൽ ഏജന്റുകൾ ക്രമത്തിൽ പ്രവർത്തിപ്പിക്കുക
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

മുൻപുള്ള കോഡിൽ കാണുന്നത് എങ്ങനെ വിവിധ ഫംഗ്ഷനുകൾ നിർവ്വഹിക്കുന്ന ഏജന്റുകൾ ചേർന്ന് ഡേറ്റാ വിശകലനം നടത്തുന്ന ഒരു ജോലി നടത്തുന്നു എന്നതാണ്. പ്രത്യേക പദവികൾ ഉള്ള ഏജന്റുകൾ സൃഷ്ടിക്കുമ്പോൾ ജോലിയുടെ കാര്യക്ഷമതയും പ്രകടനവും മെച്ചപ്പെടുത്താം.

### യഥാർത്ഥസമയം പഠിക്കുക

മോർത്താവുന്ന ഫ്രെയിംവർകുകൾ യഥാർത്ഥസമയം സന്ദർഭം മനസ്സിലാക്കിയും അനുയോജ്യമായി മാറാനും കഴിവ് നൽകുന്നു.

**ട്ടി മുകൾ എങ്ങനെ അത് ഉപയോഗിക്കും**: ഏജന്റുകൾ അവരുമായി ഇടപഴകുന്നതിൽ നിന്നു പഠിച്ചുകൊണ്ട് പെരുമാറ്റം ആവശ്യമനുസരിച്ച് ക്രമീകരിക്കുന്ന ഫീഡ്ബാക്ക് ലൂപ് നടപ്പിലാക്കാം, ഇതുവഴി തുടർച്ചയായ മെച്ചപ്പെടുത്തലും അറിവിന്റെ ശുദ്ധീകരണവും സംഭവിക്കുന്നു.

**പ്രായോഗികമായി ഇത് എങ്ങനെ നടക്കുന്നു**: ഉപയോക്തൃ പ്രതികരണങ്ങൾ, പരിസ്ഥിതി ഡേറ്റ, ജോലിയുടെ ഫലങ്ങൾ എന്നിവ വിശകലനം ചെയ്ത് അറിവ് പുതുക്കി, തീരുമാനെടുപ്പ് ആൽഗോറിതങ്ങൾ ക്രമീകരിച്ച് പ്രവർത്തനം മെച്ചപ്പെടുത്തുന്നു. ഈ പുനരാവൃത പഠന പ്രക്രിയ ഏജന്റുകൾക്ക് മാറുന്ന സാഹചര്യങ്ങൾക്കും ഉപഭോക്തൃ ഇഷ്ടങ്ങൾക്കും പറ്റുന്ന വിധം ക്രമീകരിക്കാന് പാടുപെടുന്നു, സിസ്റ്റം ഫലപ്രാപ്തി വർദ്ധിപ്പിക്കുന്നു.

## Microsoft Agent Framework ഉം Azure AI Agent Service ഉം തമ്മിലുള്ള വ്യത്യാസങ്ങൾ?

ഈ സമീപനങ്ങൾ താരതമ്യം ചെയ്യാനുള്ള നിരവധി മാർഗ്ഗങ്ങൾ ഉണ്ട്, പക്ഷേ രൂപകൽപ്പന, കഴിവുകൾ, ലക്ഷ്യ ഉപയോഗ പ്രത്യയം എന്നിവയുടെ അടിസ്ഥാനത്തിൽ ചില പ്രധാന വ്യത്യാസങ്ങൾ പരിശോധിക്കാം:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework, `AzureAIProjectAgentProvider` ഉപയോഗിച്ച് AI ഏജന്റുകള്‍ നിർമ്മിക്കാൻ ലളിതമായ SDK നൽകുന്നു. Azure OpenAI മോഡലുകൾ ഉപയോഗിച്ച് ടൂൾ കോളിംഗ്, സംഭാഷണ മാനേജ്മെന്റ്, Azure ഐഡന്റിറ്റി മുഖാന്തിരം എന്റർപ്രൈസ് നിലവാരത്തിന്റെ സുരക്ഷ എന്നിവ പിന്തുണയ്‌ക്കുന്നു.

**ഉപയോഗ രംഗങ്ങൾ**: ഉപകരണ ഉപയോഗം, ബഹുപടി പ്രവൃത്തികൾ, എന്റർപ്രൈസ് ഇന്റഗ്രേഷൻ സീനാറിയോവുകൾ എന്നിവയുള്ള പ്രൊഡക്ഷൻ-സജ്ജ AI ഏജന്റുകൾ നിർമിച്ചത്.

Microsoft Agent Framework-ന്റെ പ്രധാന ആശയങ്ങൾ:

- **ഏജന്റുകൾ**. `AzureAIProjectAgentProvider` വഴി ഏജന്റ് സൃഷ്ടിക്കുകയും പേര്, നിർദ്ദേശങ്ങൾ, ഉപകരണങ്ങൾ കോൺഫിഗർ ചെയ്യുകയും ചെയ്യുന്നു. ഏജന്റ്:
  - ഉപയോക്തൃ സന്ദേശങ്ങൾ പ്രോസസ്സ് ചെയ്ത് Azure OpenAI മോഡലുകൾ ഉപയോഗിച്ച് പ്രതികരണങ്ങൾ സൃഷ്ടിക്കുന്നു.
  - സംഭാഷണ സാഹചര്യത്തിന്റെ അടിസ്ഥാനത്തിൽ ഓട്ടോമേറ്റിക് ടൂൾ കോൾ ചെയ്‌തേക്കാം.
  - അനേകം ഇടപഴകലുകൾക്കിടയിൽ സംഭാഷണ അവസ്ഥ നിലനിർത്തുന്നു.

  ഏജന്റ് സൃഷ്ടിക്കുന്ന കോഡ് ഉദാഹരണം:

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

- **ഉപകരണങ്ങൾ**. ഫ്രെയിംവർക്ക്, ഏജന്റ് ഓട്ടോമാറ്റിക്കായി വിളിക്കാവുന്ന പൈതൺ ഫംഗ്ഷനുകളായി ഉപകരണങ്ങൾ നിർവചിച്ച് പിന്തുണയ്ക്കുന്നു. ഉപകരണങ്ങൾ ഏജന്റ് സൃഷ്ടിക്കുമ്പോൾ രജിസ്റ്റർ ചെയ്യപ്പെടുന്നു:

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

- **ബഹുവിധ ഏജന്റ് സംവരണം**. വൈവിധ്യമാർന്ന പ്രത്യേകതകൾ ഉള്ള അനേകം ഏജന്റുകൾ സൃഷ്ടിച്ച് ഇവരുടെ പ്രവർത്തനങ്ങൾ ഏകീകരിക്കാം:

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

- **Azure ഐഡന്റിറ്റി ഇന്റഗ്രേഷൻ**. `AzureCliCredential` (അല്ലെങ്കിൽ `DefaultAzureCredential`) ഉപയോഗിച്ച് സുരക്ഷിതമായ കീ മടങ്ങൽ ഒഴിവാക്കി, സുരക്ഷിതമായ അമിതവ്യാസ നിലവാരം ഉറപ്പാക്കുന്നു.

## Azure AI Agent Service

Microsoft Ignite 2024-ൽ അവതരിപ്പിച്ച Azure AI Agent Service, കൂടുതൽ സൗകര്യമുള്ള മോഡലുകൾ ഉപയോഗിച്ച് AI ഏജന്റുകൾ വികസിപ്പിക്കുകയും വിനിയോഗിക്കുകയും ചെയ്യാനുള്ള സേവനമാണ്. ഉദാഹരണത്തിന് ഓപ്പൺ സോഴ്‌സ് LLMs (Llama 3, Mistral, Cohere) നേരിട്ട് വിളിക്കാനാകും.

Azure AI Agent Service മികച്ച എന്റർപ്രൈസ് സുരക്ഷാ സംവിധാനങ്ങളും ഡാറ്റാ സംഭരണ സംവിധാനങ്ങളും നൽകുന്നു, അതേസമയം എന്റർപ്രൈസ് ആപ്ലിക്കേഷനുകൾക്കായി അനുയോജ്യമാണ്.

Microsoft Agent Framework-നൊപ്പം ചേർന്ന് ഏജന്റുകൾ നിർമ്മിച്ചും വിനിയോഗിച്ചും ചെയ്യാം.

ഇത് ഇപ്പോൾ പബ്ലിക് പ്രിവ്യൂയിൽ ആണ്, Python, C# ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിക്കുന്നതിന് പിന്തുണ നൽകുന്നു.

Azure AI Agent Service Python SDK ഉപയോഗിച്ച്, ഉപയോക്തൃ നിർവചിച്ച ഉപകരണം ഉള്ള ഏജന്റ് സൃഷ്ടിക്കാം:

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


### പ്രാഥമിക ആശയങ്ങൾ

Azure AI Agent Service-ന് താഴെ പറയുന്ന പ്രാഥമിക ആശയങ്ങൾ ഉണ്ട്:

- **ഏജന്റ്**. Azure AI Agent Service Microsoft Foundry-യുമായി സംയോജിപ്പിച്ചിരിക്കുന്നു. AI Foundry-യിൽ, AI ഏജന്റ് ഒരു "സ്മാർട്ട്" മൈക്രോസെർവിസ് ആണ്, ചോദ്യങ്ങളോട് ഉത്തരങ്ങൾ നൽകുക (RAG), പ്രവർത്തനങ്ങൾ നടത്തുക, പ്രവൃത്തികൾ പൂർത്തിയാക്കുക എന്നിവയ്ക്ക് ഉപയോഗിക്കുന്നു. ജനറേറ്റീവ് AI മോഡലുകളുടെ ശക്തിയും യാഥാർത്ഥ്യ ഡേറ്റ സ്രോതസ്സുകളും ചേർത്ത് ഇത് സാധ്യമാകുന്നു. ഒരു ഏജന്റിന്റെ ഉദാഹരണം:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ഈ ഉദാഹരണത്തിൽ, `gpt-4o-mini` മോഡലുമായി, `my-agent` എന്ന പേരോടുകൂടിയ, `You are helpful agent` എന്ന നിർദേശത്തോടെ ഏജന്റ് സൃഷ്ടിച്ചിരിക്കുന്നു. കോഡ് വിവരണം ജോലികൾക്ക് ഉപകരണങ്ങളും വിഭവങ്ങളും ഏജന്റിന് നൽകിയിട്ടുണ്ട്.

- **ത്രീഡ് (Thread) & സന്ദേശങ്ങൾ**. ത്രീഡ് രണ്ടാമത്തെ പ്രധാന ആശയമാണ്. അതൊരു ഏജന്റും ഉപയോക്താവും ഉള്ള സംഭാഷണത്തെയോ ഇടപഴകലിനെയോ പ്രതിനിധീകരിക്കുന്നു. സംഭാഷണ പുരോഗതി ട്രാക്ക് ചെയ്യാനും, സന്ദർഭവിവരങ്ങൾ സൂക്ഷിക്കാനും, ഇടപഴകലിന്റെ അവസ്ഥ കൈകാര്യം ചെയ്യാനുമായി ത്രീഡുകൾ ഉപയോഗിക്കാം. ഒരു ത്രീഡ് ഉദാഹരണം:

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

    മുൻപ് കൊടുത്ത കൊഡിൽ ഒരു ത്രീഡ് സൃഷ്ടിച്ചതായി കാണിക്കുന്നു. തുടർന്ന് ത്രീഡിൽ ഒരു സന്ദേശം അയച്ചിരിക്കുന്നു. `create_and_process_run` വിളിച്ചതോടെ ഏജന്റ് ത്രീഡിൽ ജോലി ചെയ്യാൻ ആവശ്യപ്പെടുന്നു. അവസാനത്തിലും സന്ദേശങ്ങൾ കൈപ്പതക്കി ഏജന്റിന്റെ പ്രതികരണം കാണിക്കുന്നു. ഈ സന്ദേശങ്ങൾ ഉപയോക്താവും ഏജന്റുമിടയിൽ സംഭാഷണത്തിന്റെ പുരോഗതിയാണ് സൂചിപ്പിക്കുന്നത്. സന്ദേശങ്ങളുടെ പ്രകാരം ടെക്സ്റ്റ്, ചിത്രം, ഫയൽ തുടങ്ങിയ വ്യത്യസ്ത തരം ഉള്ളതായിരിക്കും. ഡെവലപ്പർ ഈ വിവരങ്ങൾ കൂടുതൽ പ്രോസസ് ചെയ്തോ ഉപയോക്താവിന് കാഴ്ചവച്ചോ ചെയ്യാം.

- **Microsoft Agent Framework-നൊപ്പം സംയോജിപ്പിക്കുന്നു**. Azure AI Agent Service Microsoft Agent Framework-നൊപ്പം സുഗമമായി പ്രവർത്തിക്കുന്നു. അതായത് `AzureAIProjectAgentProvider` ഉപയോഗിച്ച് ഏജന്റുകൾ വളര്‍ത്തി, അവ പ്രൊഡക്ഷൻ സീനാരിയോക്‌കൾക്കായി Agent Service മുഖേന വിനിയോഗിക്കാവുന്നതാണ്.

**ഉപയോഗ രംഗങ്ങൾ**: സുരക്ഷിതവും വ്യാപനയോഗ്യവുമായ എന്റർപ്രൈസ് AI ഏജന്റ് വിനിയോഗം ആവശ്യമുള്ള അപ്പ്ലിക്കേഷനുകൾക്കായി രൂപകൽപ്പന ചെയ്തിരിക്കുന്നു.

## ഈ സമീപനങ്ങൾ തമ്മിലുള്ള വ്യത്യാസം എന്താണു?

ഒരുപാട് സമാനതകൾ ഉണ്ടെങ്കിലും, രൂപകൽപ്പനം, കഴിവുകൾ, ലക്ഷ്യ ഉപയോഗകേസുകൾ എന്നിവയുടെ അടിസ്ഥാനത്തിൽ ചില പ്രധാന വ്യത്യാസങ്ങൾ ഉണ്ട്:

- **Microsoft Agent Framework (MAF)**: ടൂൾ കോളിംഗ്, സംഭാഷണ മാനേജ്മെന്റ്, Azure ഐഡന്റിറ്റി സംയോജനം എന്നിവയോടുകൂടിയ പ്രൊഡക്ഷൻ-സജ്ജ SDK.
- **Azure AI Agent Service**: Azure Foundry-ൽ ഏജന്റുകൾക്കായുള്ള പ്ലാറ്റ്‌ഫോം, Azure OpenAI, Azure AI Search, Bing Search, കോഡ് എക്സിക്യൂഷൻ തുടങ്ങിയ സേവനങ്ങളുമായി മുൻകൂട്ടി കണക്ഷൻ.

ഇപ്പൊഴും തിരഞ്ഞെടുക്കാനുണ്ടോ?

### ഉപയോഗകേസുകൾ

പോലുള്ള ചില സാധാരണ ഉപയോഗകേസുകൾ പരിശോധിക്കാം:

> ചോദ്യം: ഞാൻ പ്രൊഡക്ഷൻ AI ഏജന്റ് അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുന്നു, വേഗത്തിൽ തുടങ്ങണം
>

>ഉത്തരം: Microsoft Agent Framework ഏറ്റവും യോജിക്കുന്നു. `AzureAIProjectAgentProvider` വഴിയും ഉപകരണങ്ങളും നിർദ്ദേശങ്ങളും ഉൾപ്പെടുത്തി കുറച്ച് കോഡിൽ ഏജന്റുകൾ സൃഷ്ടിക്കാം.

>ചോദ്യം: എന്റർപ്രൈസ് ഗ്രേഡിൽ Azure സംയോജനം (Search, കോഡ് എക്സിക്യൂഷൻ) വേണ്ടിവരും
>
>ഉത്തരം: Azure AI Agent Service ഏറ്റവും അനുയോജ്യം. പല മോഡലുകളും, Azure AI Search, Bing Search, Azure Functions എന്നിവക്ക് മുൻകൂട്ടി കണക്ഷൻ കൊടുക്കുന്ന പ്ലാറ്റ്‌ഫോം സേവനം. Foundry പോര്்டലിൽ അതിവേഗം ഏജന്റുകൾ സൃഷ്ടിച്ച് പിന്നെ വമ്പിച്ച സ്കെയിലിൽ വിനിയോഗിക്കാൻ സഹായിക്കുന്നു.
 
>ചോദ്യം: ഇപ്പോഴും ആശയക്കുഴപ്പത്തിലാണ്, ഒരെണ്ണം മാത്രം പറയൂ
>
>ഉത്തരം: ആദ്യം Microsoft Agent Framework ഉപയോഗിച്ച് ഏജന്റുകൾ നിർമ്മിച്ച്, പിന്നീട് Azure AI Agent Service ഉപയോഗിച്ച് പ്രൊഡക്ഷൻ ലെവലിൽ വിനിയോഗിക്കുക. ഈ സമ്പ്രദായം വേഗത്തിലായി ലളിതമായി ഡിസൈൻ ചെയ്യാനും, എന്റർപ്രൈസ് വിനിയോഗത്തിന് മാർഗ്ഗം ഉറപ്പാക്കാനും സഹായിക്കും.

പ്രധാന വ്യത്യാസങ്ങൾ പട്ടികയിൽ ചുരുക്കാം:

| ഫ്രെയിംവർക് | ശ്രദ്ധ | പ്രധാന ആശയങ്ങൾ | ഉപയോഗകേസുകൾ |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ടൂൾ കോളിംഗ് ഉൾക്കൊള്ളുന്ന ലളിത ഏജന്റ് SDK | ഏജന്റുകൾ, ഉപകരണങ്ങൾ, Azure ഐഡന്റിറ്റി | AI ഏജന്റുകൾ നിർമ്മാണം, ഉപകരണ ഉപയോഗം, ബഹു-പടി പ്രവൃത്തികൾ |
| Azure AI Agent Service | ഫ്ലെക്സിബിൾ മോഡലുകൾ, എന്റർപ്രൈസ് സുരക്ഷ, കോഡ് നിർമ്മാണം, ടൂൾ കോളിംഗ് | മൊഡുലാരിറ്റി, സഹകരണം, പ്രോസസ് ഓർക്കസ്ട്രേഷൻ | സുരക്ഷിതവും വ്യാപനയോഗ്യവുമായ AI ഏജന്റ് വിനിയോഗം |

## എനിക്ക് ഉള്ള Azure പാരിസ്ഥിതിക ഉപകരണങ്ങൾ നേരിട്ട് ഇന്റഗ്രേറ്റ് ചെയ്യാൻ പറ്റുമോ, വേറെ സോള്യൂഷനുകൾ വേണോ?
പതിൽ അതാണ്, നിങ്ങൾക്ക് നിലവിലുള്ള Azure ഇക്കോസിസ്റ്റം ടൂളുകൾ നേരിട്ട് Azure AI Agent Service ലുമായി സംയോജിപ്പിക്കാവുന്നതാണ്, പ്രത്യേകിച്ച് ഇത് മറ്റ് Azure സേവനങ്ങളുമായി സുസ്ഥിരമായി പ്രവർത്തിക്കാൻ നിർമ്മിച്ചതാണ്. ഉദാഹരണത്തിന്, നിങ്ങൾ Bing, Azure AI Search, Azure Functions എന്നിവ സംയോജിപ്പിക്കാം. Microsoft Foundry ക്കുമായുള്ള ആഴത്തിലുള്ള സംയോജനം കൂടിയുണ്ട്.

Microsoft Agent Framework ക്കും AzureAIProjectAgentProvider ഉം Azure ഐഡന്റിറ്റി വഴியாக Azure സേവനങ്ങളുമായി സംയോജിപ്പിക്കൽ ഉണ്ട്, അത് നിങ്ങളുടെ ഏജന്റ് ടൂളുകളിൽ നിന്നാണ് നേരിട്ട് Azure സേവനങ്ങൾ വിളിക്കാൻ അനുവദിക്കുന്നത്.

## സാമ്പിൾ കോഡുകൾ

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ഏജന്റ്.Frameworks സംബന്ധിച്ച കൂടുതൽ ചോദിക്കാനുണ്ടോ?

മറ്റു പഠിക്കാംഗങ്ങളുമായി കൂടികാഴ്ച്ച ചെയ്യാനും, ഓഫീസ് മണിക്കൂറുകളിൽ പങ്കെടുക്കാനും, നിങ്ങളുടെ AI ഏജന്റുകൾക്കുള്ള ചോദ്യങ്ങൾക്ക് ഉത്തരങ്ങൾ തേടാനും [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ൽ ചേർക്കുക.

## റഫറൻസുകൾ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## മുൻപത്തെ പാഠം

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## അടുത്ത പാഠം

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**സ്ഥിരീകരണം**:  
ഈ കോപ്പി [Co-op Translator](https://github.com/Azure/co-op-translator) എന്ന എഐ വിവർത്തന സേവനം ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നമുക്ക് കൂടുതലായി കൃത്യതയ്ക്കായി ശ്രമിക്കുമ്പോളും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ അസാധുവായ വിവരങ്ങൾ ഉണ്ടാകാമെന്ന് ദയവായി മനസ്സിലാക്കുക. ഇതിന്റെ യഥാർത്ഥ രേഖ അതിന്റെ മാതൃഭാഷയിലാണ് authoritative ആക്കി കണക്കാക്കേണ്ടത്. അത്യാവശ്യമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മാനവ വിവർത്തനം നിർദേശിക്കുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗം മൂലം ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കോ വ്യാഖ്യാനങ്ങളുടെ തെറ്റുകൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->