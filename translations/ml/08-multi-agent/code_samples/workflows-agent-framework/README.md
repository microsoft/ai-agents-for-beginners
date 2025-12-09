<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b39c052ef109db90ad9251183791e2d6",
  "translation_date": "2025-12-03T16:16:24+00:00",
  "source_file": "08-multi-agent/code_samples/workflows-agent-framework/README.md",
  "language_code": "ml"
}
-->
# മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് വർക്ക്ഫ്ലോ ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റ് ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കൽ

ഈ ട്യൂട്ടോറിയൽ മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റ് ആപ്ലിക്കേഷനുകൾ മനസ്സിലാക്കാനും നിർമ്മിക്കാനും നിങ്ങളെ സഹായിക്കും. മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങളുടെ പ്രധാന ആശയങ്ങൾ പരിശോധിക്കുകയും, ഫ്രെയിംവർക്കിന്റെ വർക്ക്ഫ്ലോ ഘടകത്തിന്റെ ആർക്കിടെക്ചറിൽ ആഴത്തിൽ പോകുകയും, Python, .NET എന്നിവയിൽ വ്യത്യസ്ത വർക്ക്ഫ്ലോ പാറ്റേണുകൾക്കുള്ള പ്രായോഗിക ഉദാഹരണങ്ങൾ പരിശോധിക്കുകയും ചെയ്യും.

## 1\. മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ മനസ്സിലാക്കുക

AI ഏജന്റ് ഒരു സാധാരണ ലാർജ് ലാംഗ്വേജ് മോഡലിന്റെ (LLM) കഴിവുകൾക്കപ്പുറം പോകുന്ന ഒരു സിസ്റ്റമാണ്. ഇത് പരിസ്ഥിതി മനസ്സിലാക്കുകയും, തീരുമാനങ്ങൾ എടുക്കുകയും, പ്രത്യേക ലക്ഷ്യങ്ങൾ നേടാൻ പ്രവർത്തനങ്ങൾ നടത്തുകയും ചെയ്യുന്നു. മൾട്ടി-ഏജന്റ് സിസ്റ്റം പല ഏജന്റുമാരും ചേർന്ന് ഒരു ഏജന്റിന് മാത്രം കൈകാര്യം ചെയ്യാൻ പ്രയാസമോ അസാധ്യമായോ ആയ ഒരു പ്രശ്നം പരിഹരിക്കുന്നതിനായി സഹകരിക്കുന്ന ഒരു സംവിധാനമാണ്.

### സാധാരണ ആപ്ലിക്കേഷൻ സീനാരിയോകൾ

  * **സങ്കീർണ്ണമായ പ്രശ്ന പരിഹാരം**: ഒരു വലിയ ടാസ്ക് (ഉദാ: ഒരു കമ്പനി-വ്യാപകമായ ഇവന്റ് പ്ലാൻ ചെയ്യൽ) ചെറിയ ഉപടാസ്കുകളായി വിഭജിച്ച് പ്രത്യേക ഏജന്റുമാർ കൈകാര്യം ചെയ്യുന്നു (ഉദാ: ബജറ്റ് ഏജന്റ്, ലജിസ്റ്റിക്സ് ഏജന്റ്, മാർക്കറ്റിംഗ് ഏജന്റ്).
  * **വിർച്വൽ അസിസ്റ്റന്റുകൾ**: ഒരു പ്രൈമറി അസിസ്റ്റന്റ് ഏജന്റ് ഷെഡ്യൂളിംഗ്, റിസർച്ച്, ബുക്കിംഗ് തുടങ്ങിയ ടാസ്കുകൾ മറ്റ് പ്രത്യേക ഏജന്റുമാർക്ക് ഡെലിഗേറ്റ് ചെയ്യുന്നു.
  * **ഓട്ടോമേറ്റഡ് കണ്ടന്റ് ക്രിയേഷൻ**: ഒരു ഏജന്റ് കണ്ടന്റ് തയ്യാറാക്കുകയും, മറ്റൊന്ന് അത് കൃത്യതയും ടോണും പരിശോധിക്കുകയും, മൂന്നാമത്തേത് അത് പ്രസിദ്ധീകരിക്കുകയും ചെയ്യുന്ന ഒരു വർക്ക്ഫ്ലോ.

### മൾട്ടി-ഏജന്റ് പാറ്റേണുകൾ

മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ പല പാറ്റേണുകളിലായി ക്രമീകരിക്കാം, അവ തമ്മിൽ എങ്ങനെ ഇടപെടുന്നു എന്നതിനെ ആശ്രയിച്ച്:

  * **സീക്വൻഷ്യൽ**: ഏജന്റുമാർ ഒരു നിർവചിച്ച ക്രമത്തിൽ പ്രവർത്തിക്കുന്നു, ഒരു ഏജന്റിന്റെ ഔട്ട്പുട്ട് അടുത്ത ഏജന്റിന്റെ ഇൻപുട്ട് ആകുന്നു.
  * **കോൺകറന്റ്**: ഏജന്റുമാർ ഒരു ടാസ്കിന്റെ വ്യത്യസ്ത ഭാഗങ്ങളിൽ സമാന്തരമായി പ്രവർത്തിക്കുന്നു, അവരുടെ ഫലങ്ങൾ അവസാനം സമാഹരിക്കുന്നു.
  * **കണ്ടീഷണൽ**: വർക്ക്ഫ്ലോ ഒരു ഏജന്റിന്റെ ഔട്ട്പുട്ടിനെ ആശ്രയിച്ച് വ്യത്യസ്ത പാതകൾ പിന്തുടരുന്നു, ഒരു if-then-else സ്റ്റേറ്റ്മെന്റിനെ പോലെ.

## 2\. മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് വർക്ക്ഫ്ലോ ആർക്കിടെക്ചർ

ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ വർക്ക്ഫ്ലോ സിസ്റ്റം മൾട്ടി-ഏജന്റുകളുടെ സങ്കീർണ്ണമായ ഇടപെടലുകൾ കൈകാര്യം ചെയ്യാൻ രൂപകൽപ്പന ചെയ്ത ഒരു പുരോഗമന ഓർക്കസ്ട്രേഷൻ എഞ്ചിനാണ്. ഇത് [Pregel-സ്റ്റൈൽ എക്സിക്യൂഷൻ മോഡൽ](https://kowshik.github.io/JPregel/pregel_paper.pdf) ഉപയോഗിക്കുന്ന ഒരു ഗ്രാഫ്-ബേസ്ഡ് ആർക്കിടെക്ചറിലാണ് നിർമ്മിച്ചിരിക്കുന്നത്, ഇവിടെ പ്രോസസ്സിംഗ് "സൂപ്പർസ്റ്റെപ്പുകൾ" എന്ന സിങ്ക്രണൈസ്ഡ് ഘട്ടങ്ങളിൽ നടക്കുന്നു.

### പ്രധാന ഘടകങ്ങൾ

ആർക്കിടെക്ചർ മൂന്ന് പ്രധാന ഭാഗങ്ങളായി വിഭജിച്ചിരിക്കുന്നു:

1.  **എക്സിക്യൂട്ടേഴ്സ്**: ഇവ അടിസ്ഥാന പ്രോസസ്സിംഗ് യൂണിറ്റുകളാണ്. നമ്മുടെ ഉദാഹരണങ്ങളിൽ, `Agent` ഒരു എക്സിക്യൂട്ടറിന്റെ ഒരു തരം ആണ്. ഓരോ എക്സിക്യൂട്ടർക്കും ലഭിക്കുന്ന സന്ദേശത്തിന്റെ തരം അനുസരിച്ച് സ്വയം പ്രവർത്തിക്കുന്ന നിരവധി മെസേജ് ഹാൻഡ്ലറുകൾ ഉണ്ടാകാം.
2.  **എഡ്ജുകൾ**: ഇവ എക്സിക്യൂട്ടേഴ്സിനിടയിൽ സന്ദേശങ്ങൾ എടുക്കുന്ന പാത നിർവചിക്കുന്നു. എഡ്ജുകൾക്ക് കണ്ടീഷനുകൾ ഉണ്ടാകാം, വർക്ക്ഫ്ലോ ഗ്രാഫിലൂടെ ഡൈനാമിക് റൂട്ടിംഗ് അനുവദിക്കുന്നു.
3.  **വർക്ക്ഫ്ലോ**: ഇത് മുഴുവൻ പ്രക്രിയയും ഓർക്കസ്ട്രേറ്റ് ചെയ്യുന്നു, എക്സിക്യൂട്ടേഴ്സ്, എഡ്ജുകൾ, ആകെ എക്സിക്യൂഷൻ ഫ്ലോ എന്നിവ കൈകാര്യം ചെയ്യുന്നു. ഇത് സന്ദേശങ്ങൾ ശരിയായ ക്രമത്തിൽ പ്രോസസ് ചെയ്യുന്നത് ഉറപ്പാക്കുകയും, ഒബ്സർവബിലിറ്റിക്കായി ഇവന്റുകൾ സ്ട്രീം ചെയ്യുകയും ചെയ്യുന്നു.

*വർക്ക്ഫ്ലോ സിസ്റ്റത്തിന്റെ പ്രധാന ഘടകങ്ങൾ ചിത്രീകരിക്കുന്ന ഒരു ഡയഗ്രാം.*

ഈ ഘടന സീക്വൻഷ്യൽ ചെയിൻസ്, ഫാൻ-ഔട്ട്/ഫാൻ-ഇൻ സമാന്തര പ്രോസസ്സിംഗിനായി, സ്വിച്ച്-കേസ് ലജിക് കണ്ടീഷണൽ ഫ്ലോകൾക്കായി തുടങ്ങിയ അടിസ്ഥാന പാറ്റേണുകൾ ഉപയോഗിച്ച് ശക്തമായ സ്കെയിലബിൾ ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാൻ അനുവദിക്കുന്നു.

## 3\. പ്രായോഗിക ഉദാഹരണങ്ങളും കോഡ് വിശകലനവും

ഇപ്പോൾ, ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് വ്യത്യസ്ത വർക്ക്ഫ്ലോ പാറ്റേണുകൾ എങ്ങനെ നടപ്പിലാക്കാമെന്ന് പരിശോധിക്കാം. ഓരോ ഉദാഹരണത്തിനും Python, .NET കോഡുകൾ പരിശോധിക്കും.

### കേസ് 1: അടിസ്ഥാന സീക്വൻഷ്യൽ വർക്ക്ഫ്ലോ

ഇത് ഏറ്റവും ലളിതമായ പാറ്റേൺ ആണ്, ഒരു ഏജന്റിന്റെ ഔട്ട്പുട്ട് നേരിട്ട് മറ്റൊന്നിലേക്ക് പാസ്സ് ചെയ്യുന്നു. നമ്മുടെ സീനാരിയോയിൽ, ഒരു ഹോട്ടൽ `FrontDesk` ഏജന്റ് ഒരു ട്രാവൽ ശുപാർശ നൽകുകയും, അത് `Concierge` ഏജന്റ് റിവ്യൂ ചെയ്യുകയും ചെയ്യുന്നു.

*ബേസിക് FrontDesk -> Concierge വർക്ക്ഫ്ലോയുടെ ഡയഗ്രാം.*

#### സീനാരിയോ പശ്ചാത്തലം

ഒരു യാത്രക്കാരൻ പാരിസിൽ ഒരു ശുപാർശ ചോദിക്കുന്നു.

1.  `FrontDesk` ഏജന്റ്, ലളിതമായ ശുപാർശ നൽകുന്നു: ലൂവ്ര് മ്യൂസിയം സന്ദർശിക്കുക.
2.  `Concierge` ഏജന്റ്, പ്രാമാണിക അനുഭവങ്ങൾക്ക് മുൻഗണന നൽകുന്നു, ഈ ശുപാർശ റിവ്യൂ ചെയ്യുന്നു, ഒരു പ്രാദേശിക, കുറച്ച് ടൂറിസ്റ്റ് അനുഭവം ശുപാർശ ചെയ്യുന്നു.

#### Python നടപ്പിലാക്കൽ വിശകലനം

Python ഉദാഹരണത്തിൽ, ആദ്യം രണ്ട് ഏജന്റുമാരെ നിർവചിക്കുകയും, ഓരോന്നിനും പ്രത്യേക നിർദ്ദേശങ്ങൾ നൽകുകയും ചെയ്യുന്നു.

```python
# 01.python-ഏജന്റ്-ഫ്രെയിംവർക്ക്-വർക്ഫ്ലോ-ഘ്മോഡൽ-ബേസിക്.ipynb

# ഏജന്റ് റോളുകളും നിർദ്ദേശങ്ങളും നിർവചിക്കുക
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# ഏജന്റ് ഉദാഹരണങ്ങൾ സൃഷ്ടിക്കുക
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

അടുത്തതായി, `WorkflowBuilder` ഉപയോഗിച്ച് ഗ്രാഫ് നിർമ്മിക്കുന്നു. `front_desk_agent` സ്റ്റാർട്ടിംഗ് പോയിന്റായി സജ്ജീകരിക്കുകയും, അതിന്റെ ഔട്ട്പുട്ട് `reviewer_agent`-ലേക്ക് കണക്റ്റ് ചെയ്യുന്ന ഒരു എഡ്ജ് സൃഷ്ടിക്കുകയും ചെയ്യുന്നു.

```python
# 01.python-ഏജന്റ്-ഫ്രെയിംവർക്ക്-വർക്ഫ്ലോ-ഘ്മോഡൽ-ബേസിക്.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

അവസാനമായി, വർക്ക്ഫ്ലോ പ്രാരംഭ ഉപയോക്തൃ പ്രോംപ്റ്റ് ഉപയോഗിച്ച് എക്സിക്യൂട്ട് ചെയ്യുന്നു.

```python
# 01.python-ഏജന്റ്-ഫ്രെയിംവർക്ക്-വർക്ഫ്ലോ-ഘ്മോഡൽ-ബേസിക്.ipynb

result =''
# run_stream രീതി വർക്ഫ്ലോ നടപ്പിലാക്കുകയും ഇവന്റുകൾ സ്ട്രീം ചെയ്യുകയും ചെയ്യുന്നു.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) നടപ്പിലാക്കൽ വിശകലനം

.NET നടപ്പിലാക്കൽ വളരെ സമാനമായ ലജിക് പിന്തുടരുന്നു. ആദ്യം, ഏജന്റുകളുടെ പേരുകൾക്കും നിർദ്ദേശങ്ങൾക്കും വേണ്ടി കോൺസ്റ്റന്റുകൾ നിർവചിക്കുന്നു.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`OpenAIClient` ഉപയോഗിച്ച് ഏജന്റുമാരെ സൃഷ്ടിക്കുകയും, `WorkflowBuilder` ഉപയോഗിച്ച് സീക്വൻഷ്യൽ ഫ്ലോ നിർവചിക്കുകയും ചെയ്യുന്നു, `frontDeskAgent`-ൽ നിന്ന് `reviewerAgent`-ലേക്ക് ഒരു എഡ്ജ് ചേർക്കുന്നു.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

വർക്ക്ഫ്ലോ ഉപയോക്താവിന്റെ സന്ദേശത്തോടെ പ്രവർത്തിപ്പിക്കുകയും, ഫലങ്ങൾ സ്ട്രീം ചെയ്യുകയും ചെയ്യുന്നു.

### കേസ് 2: മൾട്ടി-സ്റ്റെപ്പ് സീക്വൻഷ്യൽ വർക്ക്ഫ്ലോ

ഈ പാറ്റേൺ അടിസ്ഥാന സീക്വൻസിനെ കൂടുതൽ ഏജന്റുമാരെ ഉൾപ്പെടുത്തുന്നതിന് വിപുലീകരിക്കുന്നു. ഇത് പല ഘട്ടങ്ങളിലായി പരിഷ്കരണം അല്ലെങ്കിൽ ട്രാൻസ്ഫർമേഷൻ ആവശ്യമായ പ്രക്രിയകൾക്ക് അനുയോജ്യമാണ്.

#### സീനാരിയോ പശ്ചാത്തലം

ഒരു ഉപയോക്താവ് ഒരു ലിവിംഗ് റൂമിന്റെ ചിത്രം നൽകുകയും, ഫർണിച്ചർ ക്വോട്ട് ചോദിക്കുകയും ചെയ്യുന്നു.

1.  **Sales-Agent**: ചിത്രത്തിൽ ഫർണിച്ചർ ഇനങ്ങളെ തിരിച്ചറിയുകയും, ഒരു ലിസ്റ്റ് സൃഷ്ടിക്കുകയും ചെയ്യുന്നു.
2.  **Price-Agent**: ഇനങ്ങളുടെ ലിസ്റ്റ് എടുക്കുകയും, ബജറ്റ്, മിഡ്-റേഞ്ച്, പ്രീമിയം ഓപ്ഷനുകൾ ഉൾപ്പെടുന്ന വില വിശദീകരണം നൽകുകയും ചെയ്യുന്നു.
3.  **Quote-Agent**: വിലപ്പെടുത്തിയ ലിസ്റ്റ് സ്വീകരിക്കുകയും, Markdown ഫോർമാറ്റിൽ ഒരു ഔദ്യോഗിക ക്വോട്ട് ഡോക്യുമെന്റ് രൂപപ്പെടുത്തുകയും ചെയ്യുന്നു.

*Sales -> Price -> Quote വർക്ക്ഫ്ലോയുടെ ഡയഗ്രാം.*

#### Python നടപ്പിലാക്കൽ വിശകലനം

മൂന്ന് പ്രത്യേക ഏജന്റുമാരെ നിർവചിക്കുകയും, ഓരോന്നിനും പ്രത്യേക റോളുകൾ നൽകുകയും ചെയ്യുന്നു. `add_edge` ഉപയോഗിച്ച് വർക്ക്ഫ്ലോ നിർമ്മിക്കുന്നു: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-ഏജന്റ്-ഫ്രെയിംവർക്ക്-വർക്ഫ്ലോ-ഘ്മോഡൽ-സീക്വൻഷ്യൽ.ipynb

# മൂന്ന് പ്രത്യേക ഏജന്റുമാരെ സൃഷ്ടിക്കുക
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# സീക്വൻഷ്യൽ വർക്ഫ്ലോ നിർമ്മിക്കുക
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ഇൻപുട്ട് ഒരു `ChatMessage` ആണ്, ഇതിൽ ടെക്സ്റ്റും ഇമേജ് URIയും ഉൾപ്പെടുന്നു. ഫ്രെയിംവർക്ക് ഓരോ ഏജന്റിന്റെ ഔട്ട്പുട്ട് അടുത്ത ഏജന്റിലേക്ക് പാസ്സ് ചെയ്യുന്നത് കൈകാര്യം ചെയ്യുന്നു, അവസാന ക്വോട്ട് സൃഷ്ടിക്കുന്നതുവരെ.

```python
# 02.python-ഏജന്റ്-ഫ്രെയിംവർക്ക്-വർക്ഫ്ലോ-ഘ്മോഡൽ-സീക്വൻഷ്യൽ.ipynb

# ഉപയോക്തൃ സന്ദേശത്തിൽ ടെക്സ്റ്റും ഒരു ചിത്രവും അടങ്ങിയിരിക്കുന്നു
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# വർക്ഫ്ലോ പ്രവർത്തിപ്പിക്കുക
async for event in workflow.run_stream(message):
    ...
```

#### .NET (C#) നടപ്പിലാക്കൽ വിശകലനം

.NET ഉദാഹരണം Python പതിപ്പിനെ അനുസരിക്കുന്നു. മൂന്ന് ഏജന്റുമാർ (`salesagent`, `priceagent`, `quoteagent`) സൃഷ്ടിക്കുന്നു. `WorkflowBuilder` അവരെ സീക്വൻഷ്യൽ ആയി ബന്ധിപ്പിക്കുന്നു.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ഉപയോക്താവിന്റെ സന്ദേശം ഇമേജ് ഡാറ്റ (bytes ആയി) കൂടാതെ ടെക്സ്റ്റ് പ്രോംപ്റ്റ് ഉപയോഗിച്ച് നിർമ്മിക്കുന്നു. `InProcessExecution.StreamAsync` മെത്തഡ് വർക്ക്ഫ്ലോ ആരംഭിക്കുകയും, ഫൈനൽ ഔട്ട്പുട്ട് സ്ട്രീമിൽ നിന്ന് പിടിക്കുകയും ചെയ്യുന്നു.

### കേസ് 3: കോൺകറന്റ് വർക്ക്ഫ്ലോ

ഈ പാറ്റേൺ ടാസ്കുകൾ ഒരേസമയം നടത്താൻ കഴിയുന്നപ്പോൾ സമയം ലാഭിക്കാൻ ഉപയോഗിക്കുന്നു. ഇത് "ഫാൻ-ഔട്ട്" പല ഏജന്റുമാർക്കും, "ഫാൻ-ഇൻ" ഫലങ്ങൾ സമാഹരിക്കാൻ ഉൾപ്പെടുന്നു.

#### സീനാരിയോ പശ്ചാത്തലം

ഒരു ഉപയോക്താവ് സിയാറ്റിലിലേക്ക് ഒരു യാത്ര പ്ലാൻ ചെയ്യാൻ ചോദിക്കുന്നു.

1.  **Dispatcher (Fan-Out)**: ഉപയോക്താവിന്റെ അഭ്യർത്ഥന ഒരേസമയം രണ്ട് ഏജന്റുമാർക്ക് അയക്കുന്നു.
2.  **Researcher-Agent**: സിയാറ്റിലിലെ ആകർഷണങ്ങൾ, കാലാവസ്ഥ, പ്രധാന പരിഗണനകൾ എന്നിവ റിസർച്ച് ചെയ്യുന്നു.
3.  **Plan-Agent**: സ്വതന്ത്രമായി ഒരു വിശദമായ ദിനം-പ്രതി യാത്രാ ഷെഡ്യൂൾ സൃഷ്ടിക്കുന്നു.
4.  **Aggregator (Fan-In)**: റിസർച്ചറും പ്ലാനറും നൽകുന്ന ഔട്ട്പുട്ടുകൾ സമാഹരിച്ച് ഫൈനൽ ഫലമായി അവതരിപ്പിക്കുന്നു.

*കോൺകറന്റ് Researcher and Planner വർക്ക്ഫ്ലോയുടെ ഡയഗ്രാം.*

#### Python നടപ്പിലാക്കൽ വിശകലനം

`ConcurrentBuilder` ഈ പാറ്റേൺ സൃഷ്ടിക്കുന്നത് ലളിതമാക്കുന്നു. നിങ്ങൾ പങ്കെടുക്കുന്ന ഏജന്റുമാരുടെ ലിസ്റ്റ് നൽകുക, ബിൽഡർ സ്വയമേവ ഫാൻ-ഔട്ട്, ഫാൻ-ഇൻ ലജിക് സൃഷ്ടിക്കുന്നു.

```python
# 03.python-ഏജന്റ്-ഫ്രെയിംവർക്ക്-വർക്ക്ഫ്ലോ-ഘ്മോഡൽ-സമകാലികം.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ഫാൻ-ഔട്ട്/ഫാൻ-ഇൻ ലജിക് കൈകാര്യം ചെയ്യുന്നു
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# വർക്ക്ഫ്ലോ പ്രവർത്തിപ്പിക്കുക
events = await workflow.run("Plan a trip to Seattle in December")
```

ഫ്രെയിംവർക്ക് `research_agent`-നും `plan_agent`-നും സമാന്തരമായി പ്രവർത്തിക്കാൻ അനുവദിക്കുകയും, അവരുടെ ഫൈനൽ ഔട്ട്പുട്ടുകൾ ഒരു ലിസ്റ്റിലേക്ക് സമാഹരിക്കുകയും ചെയ്യുന്നു.

#### .NET (C#) നടപ്പിലാക്കൽ വിശകലനം

.NET-ൽ, ഈ പാറ്റേൺ കൂടുതൽ വ്യക്തമായ നിർവചനം ആവശ്യമാണ്. ഫാൻ-ഔട്ടിനും ഫാൻ-ഇനിനും ലജിക് കൈകാര്യം ചെയ്യാൻ കസ്റ്റം എക്സിക്യൂട്ടേഴ്സ് (`ConcurrentStartExecutor` and `ConcurrentAggregationExecutor`) സൃഷ്ടിക്കുന്നു.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

`WorkflowBuilder` പിന്നീട് ഈ കസ്റ്റം എക്സിക്യൂട്ടേഴ്സും ഏജന്റുമാരും ഉപയോഗിച്ച് ഗ്രാഫ് നിർമ്മിക്കാൻ `AddFanOutEdge` and `AddFanInEdge` ഉപയോഗിക്കുന്നു.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### കേസ് 4: കണ്ടീഷണൽ വർക്ക്ഫ്ലോ

കണ്ടീഷണൽ വർക്ക്ഫ്ലോകൾ ബ്രാഞ്ചിംഗ് ലജിക് അവതരിപ്പിക്കുന്നു, ഇടക്കാല ഫലങ്ങളെ അടിസ്ഥാനമാക്കി വ്യത്യസ്ത പാതകൾ സ്വീകരിക്കാൻ സിസ്റ്റത്തിന് അനുവദിക്കുന്നു.

#### സീനാരിയോ പശ്ചാത്തലം

ഈ വർക്ക്ഫ്ലോ ഒരു ടെക്നിക്കൽ ട്യൂട്ടോറിയൽ സൃഷ്ടിക്കുകയും പ്രസിദ്ധീകരിക്കുകയും ഓട്ടോമേറ്റ് ചെയ്യുന്നു.

1.  **Evangelist-Agent**: നൽകിയ ഔട്ട്‌ലൈൻ, URLs എന്നിവയെ അടിസ്ഥാനമാക്കി ട്യൂട്ടോറിയലിന്റെ ഒരു ഡ്രാഫ്റ്റ് എഴുതുന്നു.
2.  **ContentReviewer-Agent**: ഡ്രാഫ്റ്റ് റിവ്യൂ ചെയ്യുന്നു. വാക്കുകളുടെ എണ്ണം 200-ൽ കൂടുതലാണോ എന്ന് പരിശോധിക്കുന്നു.
3.  **കണ്ടീഷണൽ ബ്രാഞ്ച്**:
      * **അംഗീകരിച്ചാൽ (`Yes`)**: വർക്ക്ഫ്ലോ `Publisher-Agent`-ലേക്ക് മുന്നോട്ട് പോകുന്നു.
      * **നിരസിച്ചാൽ (`No`)**: വർക്ക്ഫ്ലോ നിർത്തുകയും, നിരസിക്കാനുള്ള കാരണം ഔട്ട്പുട്ട് ചെയ്യുകയും ചെയ്യുന്നു.
4.  **Publisher-Agent**: ഡ്രാഫ്റ്റ് അംഗീകരിച്ചാൽ, ഈ ഏജന്റ് കണ്ടന്റ് ഒരു Markdown ഫയലിലേക്ക് സംരക്ഷിക്കുന്നു.

#### Python നടപ്പിലാക്കൽ വിശകലനം

ഈ ഉദാഹരണം കണ്ടീഷണൽ ലജിക് നടപ്പിലാക്കാൻ ഒരു കസ്റ്റം ഫംഗ്ഷൻ, `select_targets`, ഉപയോഗിക്കുന്നു. ഈ ഫംഗ്ഷൻ `add_multi_selection_edge_group`-ലേക്ക് പാസ്സ് ചെയ്യുകയും, റിവ്യൂവറിന്റെ ഔട്ട്പുട്ടിൽ നിന്ന് `review_result` ഫീൽഡിനെ അടിസ്ഥാനമാക്കി വർക്ക്ഫ്ലോ നയിക്കുകയും ചെയ്യുന്നു.

```python
# 04.python-ഏജന്റ്-ഫ്രെയിംവർക്ക്-വർക്ഫ്ലോ-എഐഫൗണ്ട്രി-കണ്ടീഷൻ.ipynb

# ഈ ഫംഗ്ഷൻ അവലോകന ഫലത്തിന്റെ അടിസ്ഥാനത്തിൽ അടുത്ത ഘട്ടം നിർണ്ണയിക്കുന്നു
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # അംഗീകരിച്ചാൽ, 'save_draft' എക്സിക്യൂട്ടറിലേക്ക് മുന്നോട്ട് പോകുക
        return [save_draft_id]
    else:
        # നിരസിച്ചാൽ, പരാജയം റിപ്പോർട്ട് ചെയ്യാൻ 'handle_review' എക്സിക്യൂട്ടറിലേക്ക് മുന്നോട്ട് പോകുക
        return [handle_review_id]

# വർക്ഫ്ലോ ബിൽഡർ റൂട്ടിംഗിനായി സെലക്ഷൻ ഫംഗ്ഷൻ ഉപയോഗിക്കുന്നു
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # മൾട്ടി-സെലക്ഷൻ എഡ്ജ് കണ്ടീഷണൽ ലജിക് നടപ്പിലാക്കുന്നു
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` പോലുള്ള കസ്റ്റം എക്സിക്യൂട്ടേഴ്സ് ഏജന്റുകളുടെ JSON ഔട്ട്പുട്ട് പാഴ്സുചെയ്ത്, സെലക്ഷൻ ഫംഗ്ഷൻ പരിശോധിക്കാൻ കഴിയുന്ന ശക്തമായ ടൈപ്പ് ചെയ്ത ഒബ്ജക്റ്റുകളാക്കി മാറ്റുന്നു.

#### .NET (C#) നടപ്പിലാക്കൽ വിശകലനം

.NET പതിപ്പ് സമാനമായ സമീപനം ഉപയോഗിക്കുന്നു, ഒരു കണ്ടീഷൻ ഫംഗ്ഷൻ ഉപയോഗിച്ച്. `ReviewResult` ഒബ്ജക്റ്റിന്റെ `Result` പ്രോപ്പർട്ടി പരിശോധിക്കാൻ ഒരു `Func<object?, bool>` നിർവചിക്കുന്നു.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

`AddEdge` മെത്തഡിന്റെ `condition` പാരാമീറ്റർ `WorkflowBuilder`-നെ ഒരു ബ്രാഞ്ചിംഗ് പാത സൃഷ്ടിക്കാൻ അനുവദിക്കുന്നു. `GetCondition(expectedResult: "Yes")` സത്യമായാൽ മാത്രമേ വർക്ക്ഫ്ലോ `publishExecutor`-ലേക്ക് പോകൂ. അല്ലെങ്കിൽ, അത് `sendReviewerExecutor`-ലേക്ക് പോകും.

## നിഗമനം

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് വർക്ക്ഫ്ലോ സങ്കീർണ്ണമായ, മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ ഓർക്കസ്ട്രേറ്റ് ചെയ്യാൻ ശക്തമായ, ഫ്ലെക്സിബിൾ അടിസ്ഥാനം നൽകുന്നു. അതിന്റെ ഗ്രാഫ്-ബേസ്ഡ് ആർക്കിടെക്ചറും പ്രധാന ഘടകങ്ങളും ഉപയോഗിച്ച്, ഡെവലപ്പർമാർ Python, .NET എന്നിവയിൽ സങ്കീർണ്ണമായ വർക്ക്ഫ്ലോകൾ രൂപകൽപ്പന ചെയ്യുകയും നടപ്പിലാക്കുകയും ചെയ്യാം. നിങ്ങളുടെ ആപ്ലിക്കേഷൻ ലളിതമായ സീക്വൻഷ്യൽ പ്രോസസ്സിംഗ്, സമാന്തര എക്സിക്യൂഷൻ, ഡൈനാമിക് കണ്ടീഷണൽ ലജിക് എന്നിവ ആവശ്യപ്പെടുന്നുവോ എന്നതിനെ ആശ്രയിച്ച്, ഈ ഫ്രെയിംവർക്ക് ശക്തമായ, സ്കെയിലബിൾ, ടൈപ്പ്-സേഫ് AI-പവർഡ് സൊല്യൂഷനുകൾ നിർമ്മിക്കാൻ ആവശ്യമായ ഉപകരണങ്ങൾ നൽകുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസത്യവാദം**:  
ഈ രേഖ AI വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. കൃത്യതയ്ക്കായി ഞങ്ങൾ ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള മൗലിക രേഖ പ്രാമാണികമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->