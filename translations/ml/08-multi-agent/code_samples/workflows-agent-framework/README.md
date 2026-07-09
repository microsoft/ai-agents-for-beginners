# മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് വർക്ഫ്ലോ ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റ് അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കൽ

ഈ പാഠകോശം മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റ് അപ്ലിക്കേഷനുകൾ എങ്ങനെ മനസ്സിലാക്കും, നിർമ്മിക്കും എന്നതിൽ നിങ്ങളെ നയിക്കും. മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ എന്ന മുഖ്യ ആശയങ്ങൾ പരിശോധിച്ച്, ഫ്രെയിംവർക്ക് വർക്ഫ്ലോ ഘടകം ചേർന്ന ആർക്കിടെക്ചർ അന്വഷിച്ച്, വ്യത്യസ്ത വർക്ഫ്ലോ മാതൃകകൾക്കായി Python ഉം .NET ഉം എന്നിവയിൽ പ്രായോഗിക ഉദാഹരണങ്ങൾ വഴി വേണം.

## 1\. മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ മനസ്സിലാക്കുക

ഒരു AI ഏജന്റ് സാധാരണ വലിയ ഭാഷാ മാതൃക (LLM) ന്റെ ശേഷികൾക്ക് മീതെ പോകുന്ന ഒരു സിസ്റ്റമാണ്. അത് തന്റെ പരിസരത്തെ സ്പർശിച്ച്, നിര്യാതം കൊണ്ടു തീരുമാനങ്ങൾ എടുക്കുകയും പ്രത്യേക ലക്ഷ്യങ്ങൾ നേടാൻ പ്രവർത്തിക്കുകയും ചെയ്യുന്നു. ഒരു മൾട്ടി-ഏജന്റ് സിസ്റ്റത്തിൽ പല ഏജന്റുകളും ചേർന്ന് പ്രവർത്തിച്ച് ഒരു ഏജന്റ് ഒരിക്കലും എളുപ്പത്തിൽ കൈകാര്യം ചെയ്യാനാകാത്ത പ്രശ്നം പരിഹരിക്കുന്നു.

### സാധാരണ പ്രയോഗ രംഗങ്ങൾ

  * **സങ്കീർണ്ണ പ്രശ്‌ന പരിഹാരം:** വലിയ ഒരു ജോലിയെ (ഉദാ: ഒരു കമ്പനി വ്യാപകമായ ഇവന്റ് പ്ലാനിംഗ്) ചെറിയ ഉപ ജോലികളായി വിഭജിച്ച് പ്രത്യേക ഏജന്റുകൾ (ഉദാ: ബജറ്റ് ഏജന്റ്, ലജിസ്റ്റിക് ഏജന്റ്, മാർക്കറ്റിംഗ് ഏജന്റ്) കൈകാര്യം ചെയ്യുന്നു.
  * **വർച്വൽ അസിസ്റ്റന്റുകൾ:** ഒരു പ്രാഥമിക അസിസ്റ്റന്റ് ഏജന്റ് ഷെഡ്യൂളിംഗ്, ഗവേഷണം, ബുക്കിംഗ് പോലെയുള്ള ജോലികൾ മറ്റ് പ്രത്യേക ഏജന്റുകൾക്ക് ഏൽപ്പിക്കുന്നു.
  * **സ്വയംമാറ്റിയ ഉള്ളടക്ക സൃഷ്ടി:** ഒരു ഏജന്റ് ഉള്ളടക്കം തയാറാക്കുന്നു, മറ്റൊരു ഏജന്റ് അത് കൃത്യതയും ശൈലിയും പരിശോധിക്കുന്നു, മൂന്നാമൻ ഏജന്റ് അത് പ്രസിദ്ധീകരിക്കുന്നു.

### മൾട്ടി-ഏജന്റ് മാതൃകകൾ

മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ പല മാതൃകകളിൽ ക്രമീകരിക്കാവുന്നതാണ്, അവയുടെ ഇടപെടലുകൾ മറ്റുള്ളവയെ എങ്ങനെ ബാധിക്കുന്നു എന്നത് നിശ്ചയിക്കും:

  * **ക്രമനിര്യം (Sequential):** ഏജന്റുകൾ ഒരു മുൻകൂട്ടി നിശ്ചിത ക്രമത്തിൽ പ്രവർത്തിക്കുന്നു, അസംബ്ലി ലൈൻ പോലെ. ഒരു ഏജന്റിന്റെ ഔട്ട്‌പുട്ട് അടുത്തതിനെ ഇൻപുട്ടായി നൽകുന്നു.
  * **സമകാലികം (Concurrent):** ഏജന്റുകൾ ഒരേ സമയം വിവിധ ഭാഗങ്ങളിൽ ജോലി ചെയ്യുന്നു, അവയുടെ ഫലം ഒടുവിൽ ചേർക്കുന്നു.
  * **ന്യൂനഗതം (Conditional):** ഏജന്റിന്റെ ഔട്ട്‌പുട്ട് അടിസ്ഥാനമാക്കി workflow വ്യത്യസ്ത പാതകൾ പിന്തുടരുന്നു, if-then-else പ്രഖ്യാപനത്തിന് സമാനമായിരിക്കുന്നു.

## 2\. മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് വർക്ഫ്ലോ ആർക്കിടെക്ചർ

ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ വർക്ഫ്ലോ സിസ്റ്റം ഒരുപാട് ഏജന്റുകൾ തമ്മിലുള്ള സങ്കീർണ്ണ ഇടപെടലുകൾ നിയന്ത്രിക്കാൻ രൂപകൽപ്പനചെയ്ത ഒരു മുന്നേറ്റ ഓർക്കസ്ട്രേഷൻ എൻജിനാണ്. ഇത് [പ്രെഗെൽ-സ്റ്റൈൽ എക്‌സ്‌ക്യൂഷൻ മോഡൽ](https://kowshik.github.io/JPregel/pregel_paper.pdf) ഉപയോഗിക്കുന്ന ഗ്രാഫ് അടിസ്ഥാനമായ ഒരു ആർക്കിടെക്ചറിൽ നിർമ്മിച്ചിട്ടുണ്ട്, എവിടെ "സൂപ്പർസ്റ്റെപ്പുകൾ" എന്ന് വിളിക്കുന്ന സംയോജിത ഘട്ടങ്ങളിൽ പ്രോസസ്സിംഗ് നടക്കുന്നു.

### പ്രധാന ഘടകങ്ങൾ

ആർക്കിടെക്ചർ മൂന്ന് പ്രധാന ഭാഗങ്ങളിൽ നിന്നാണ്:

1.  **എക്സിക്യൂട്ടറുകൾ:** ഇവ അടിസ്ഥാന പ്രോസസ്സിങ് യൂണിറ്റുകളാണ്. ഞങ്ങളുടെ ഉദാഹരണങ്ങളിൽ `Agent` എന്നത് എക്സിക്യൂട്ടറിന്റെ ഒരു തരമാണ്. ഓരോ എക്സിക്യൂട്ടറിനും പല മെസ്സേജ് ഹാൻഡ്ലറുകൾ ഉണ്ടാകാം, സ്വീകരിക്കുന്ന മെസ്സജ് തരം അനുസരിച്ച് സ്വയമേവ പ്രവർത്തിക്കുന്നു.
2.  **എഡ്ജുകൾ:** ഈ എക്സിക്യൂട്ടറുകൾക്കിടയിൽ മെസ്സേജുകൾ കടന്നുപോവാനുള്ള മാർഗ്ഗങ്ങൾ നിർവചിക്കുന്നു. എഡ്ജുകൾക്ക് വ്യത്യസ്ത വിജ്ഞാനമാർഗ്ഗങ്ങൾക്കായുള്ള ദിശാബോധം ഉള്ള കുറവുകൾ ഉണ്ടാകാം.
3.  **വർക്ഫ്ലോ:** ഈ ഘടകം മുഴുവൻ പ്രക്രിയ നിയന്ത്രിക്കുന്നു, എക്സിക്യൂട്ടറുകളും എഡ്ജുകളും ആകെ പ്രവാഹവും പാരാമർശിക്കുന്നു. മെസ്സേജുകൾ ശരിയായ ക്രമത്തിൽ പ്രോസസ് ചെയ്യുന്നത് ഉറപ്പാക്കുകയും ഓബ്സർവിബിലിറ്റിക്കായി ഇവന്റ്‌സ് സ്ട്രീം ചെയ്യുകയും ചെയ്യുന്നു.

*വർക്ഫ്ലോ സിസ്റ്റത്തിന്റെ പ്രധാന ഘടകങ്ങൾ കാണിക്കുന്ന ഒരു ചിത്രരൂപം.*

ഈ ഘടന പോരെയുള്ള കോട്ടയിലും സ്കെയിലബിളുമായ അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാൻ അനുമതിസ്ഥാപിക്കുന്നു, ക്രമത്തിൽ നിന്നുള്ള ചെയിനുകൾ, ഫാൻ-ഔട്ട്/ഫാൻ-ഇൻ തന്തു സംയോജനം, ശിച്-കേസ് ലോജിക് പോലുള്ള അടിസ്ഥാന മാതൃകകൾ ഉപയോഗിച്ച്.

## 3\. പ്രായോഗിക ഉദാഹരണങ്ങളും കോഡ് വിശകലനവും

ഫ്രെയിംവർക്കുവഴിലൂടെ വ്യത്യസ്ത വർക്ഫ്ലോ മാതൃകകൾ എങ്ങനെ നടപ്പിലാക്കാമെന്ന് ഇപ്പോൾ പരിശോധിക്കാം. ഓരോ ഉദാഹരണത്തിനും Python ഉം .NET ഉം കോഡുകൾ നോക്കാം.

### കേസ് 1: അടിസ്ഥാന ക്രമനിരം workflow

ഏറ്റവും ലളിതമായ മാതൃകയാണ് ഇത്, ഒരു ഏജന്റിന്റെ ഔട്ട്‌പുട്ട് നേരിട്ട് മറ്റൊന്നിലേക്ക് പാസു ചെയ്യുന്നത്. ഞങ്ങളുടെ ഘടനയിൽ ഹോട്ടൽ `FrontDesk` ഏജന്റ് യാത്രാ ശിപാർശ നൽകുകയും, പിന്നീട് `Concierge` ഏജന്റ് അത് അവലോകനം ചെയ്യുകയും ചെയ്യുന്നു.

*ആസ്ഥിയുടെ അടിസ്ഥാന FrontDesk -> Concierge workflow യുടെ ചിത്രരൂപം.*

#### ഘടന പശ്ചാത്തലം

ഒരു യാത്രക്കാരൻ പാരിസിൽ ശിപാർശ ചോദിക്കുന്നു.

1.  ആത്മശാസ്ത്രം പ്രധാനം ചെയ്യുന്ന `FrontDesk` ഏജന്റ് ലൂവ്ര് മ്യൂസിയം സന്ദർശിക്കാൻ നിർദേശിക്കുന്നു.
2.  യഥാർത്ഥ അനുഭവങ്ങൾ മുൻഗണന നൽകുന്ന `Concierge` ഏജന്റ് ഈ ശിപാർശ സ്വീകരിക്കുകയും അവലോകനം ചെയ്ത്, കൂടുതൽ പ്രാദേശികവും കുറഞ്ഞ ടൂറിസ്റ്റ്-പോലെ ഉള്ള മാറ്റ് നിർദ്ദേശിക്കുകയും ചെയ്യുന്നു.

#### Python നടപ്പിലാക്കൽ വിശകലനം

Python ഉദാഹരണത്തിൽ രണ്ടും ഏജന്റുകളും ആദ്യമേ നിർവചിച്ച് സൃഷ്ടിക്കുന്നു, ഓരോന്നിനും പ്രത്യേക നിർദ്ദേശങ്ങൾ നൽകുന്നു.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# ഏജന്റ് റോൾസും നിർദ്ദേശങ്ങളും നിർവചിക്കുക
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# ഏജന്റ് ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

തുടർന്ന്, `WorkflowBuilder` ഉപയോഗിച്ച് ഗ്രാഫ് നിർമ്മിക്കുന്നു. `front_desk_agent` ആരംഭ ബിന്ദുവായി സജ്ജമാക്കി, അതിന്റെ ഔട്ട്‌പുട്ട് `reviewer_agent`-ന്നു കണക്റ്റ് ചെയ്യാൻ ഒരു എഡ്ജ് സൃഷ്ടിക്കുന്നു.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

അവസാനം, പ്രാഥമിക ഉപയോക്തൃ പ്രോമ്പ്റ്റിനോടൊപ്പം workflow പ്രവർത്തിപ്പിക്കുന്നു.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run പ്രവർത്തനക്രമം നിർവഹിക്കുന്നു; get_outputs() ഔട്ട്‌പുട്ട് എക്സിക്യൂട്ടറിന്റെ ഫലം പ്രദാനം ചെയ്യുന്നു.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C#) നടപ്പിലാക്കൽ വിശകലനം

.NET നടപ്പിലാക്കൽ സമാനമായ തർക്കം പിന്തുടരുന്നു. ആദ്യം ഏജന്റ് പേരുകളും നിർദ്ദേശങ്ങളും കൺസ്റ്റൻറുകളായി നിർവചിക്കുന്നു.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`AzureOpenAIClient`-ഉം (Responses API) ഉപയോഗിച്ച് ഏജന്റുകൾ സൃഷ്ടിക്കുന്നു, തുടർന്ന് `WorkflowBuilder` ക്രമനിരത്തിൽ `frontDeskAgent`-ഇൽ നിന്നു `reviewerAgent`-യിലേക്ക് എഡ്ജ് ചേർക്കുന്നു.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

ഉപയോക്തൃ സന്ദേശത്തോടുകൂടി workflow റൺ ചെയ്യുന്നു, ഫലം സ്ട്രീം വഴി തിരികെ ലഭിക്കുന്നു.

### കേസ് 2: മൾട്ടി-പടി ക്രമനിരം workflow

ഈ മാതൃകം അടിസ്ഥാന ക്രമനിരത്തെ കൂടുതൽ ഏജന്റുകൾ ഉൾപ്പെടുത്താൻ വിപുലീകരിക്കുന്നു. പല ഘട്ടങ്ങളിലായി മെച്ചപ്പെടുത്തലുകൾ അല്ലെങ്കിൽ രൂപാന്തരങ്ങൾ ആവശ്യമായ പ്രക്രിയകൾക്ക് അനുയോജ്യമാണ്.

#### ഘടന പശ്ചാത്തലം

ഒരു ഉപയോക്താവ് ലിവിംഗ് റൂം ചിത്രം നൽകുകയും ഫർണിച്ചർ കോട്ട് ചോദിക്കുകയും ചെയ്യുന്നു.

1.  **Sales-Agent**: ചിത്രത്തിൽ ഫർണിച്ചർ സാധനങ്ങൾ തിരിച്ചറിയുകയും ഒരു ലിസ്റ്റ് സൃഷ്ടിക്കുകയും ചെയ്യുന്നു.
2.  **Price-Agent**: സാധനങ്ങളുടെ ലിസ്റ്റ് സ്വീകരിച്ച് ബജറ്റ്, മിഡ്-റേഞ്ച്, പ്രീമിയം ഓപ്ഷനുകൾ ഉൾപ്പെട്ട വിശദമായ വില വിശദീകരണം നൽകുന്നു.
3.  **Quote-Agent**: വിലപ്പെടുത്തിയ ലിസ്റ്റ് സ്വീകരിച്ച് അത് മൃദുലമായ മാർക്ക്ഡൗൺ ഫോർമാറ്റിലുള്ള ഔദ്യോഗികquote ഡോക്യുമെന്റായി മാറ്റുന്നു.

*Sales -> Price -> Quote workflow യുടെ ചിത്രരൂപം.*

#### Python നടപ്പിലാക്കൽ വിശകലനം

മൂന്ന് ഏജന്റുകൾ കൂടുതലായ ഒരു പ്രത്യേകഭാഗം പ്രവർത്തനം നിർവഹിക്കുന്നു. workflow `add_edge` ഉപയോഗിച്ച് `sales_agent` -> `price_agent` -> `quote_agent` എന്ന ചെയിൻ സൃഷ്ടിക്കുന്നു.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# മൂന്ന് പ്രത്യേക ഏജന്റുകൾ സൃഷ്ടിക്കുക
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# പാരമ്പര്യ പ്രവാഹം നിർമ്മിക്കുക
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ഇൻപുട്ട് `ChatMessage` ആണു, ടെക്സ്റ്റും ചിത്രം URI-യും ഉൾക്കൊള്ളുന്നു. മാറ്റിസ്ഥാപനം ഓരോ ഏജന്റിന്റെ ഔട്ട്‌പുട്ട് അടുത്തതിലേക്ക് പാസ്സടയ്ക്കുന്നതു കൈകാര്യം ചെയ്യുന്നു, അവസാന quote സൃഷ്ടിക്കുന്ന വരെ.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ഉപയോക്തൃ സന്ദേശത്തിൽ ടെക്സ്റ്റും ഒരു ചിത്രം കൂടാതെ ഉണ്ട്
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# പ്രവൃത്തി പ്രവാഹം നടത്തുക
events = await workflow.run(message)
```

#### .NET (C#) നടപ്പിലാക്കൽ വിശകലനം

.NET ഉദാഹരണം Python പതിപ്പിനെ പ്രതിഫലിപ്പിക്കുന്നു. മൂന്ന് ഏജന്റുകളും (`salesagent`, `priceagent`, `quoteagent`) സൃഷ്ടിക്കുന്നു. `WorkflowBuilder` അവരെ ക്രമത്തിൽ ബന്ധിപ്പിക്കുന്നു.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ഉപയോക്തൃ സന്ദേശം ചിത്ര ഡാറ്റ (ബൈറ്റുകളായി) കൂടാതെ ടെക്സ്റ്റ് പ്രോമ്പ്റ്റും ഉൾക്കൊള്ളുന്നു. `InProcessExecution.StreamAsync` മാർഗ്ഗം workflow ആരംഭിപ്പിക്കുന്നു, അന്തിമ ഔട്ട്‌പുട്ട് സ്ട്രീമിൽ നിന്ന് സമാഹരിക്കുന്നു.

### കേസ് 3: സമകാലിക Workflow

ഈ മാതൃക സമയസംരക്ഷണത്തിന് ജോലികൾ ഒരേ സമയം നിർവഹിക്കാവുന്നപ്പോഴാണ് ഉപയോഗിക്കുന്നത്. ഇത് "ഫാൻ-ഔട്ട്" പല ഏജന്റുകളിലേക്ക്, "ഫാൻ-ഇൻ" ഫലങ്ങൾ ഒറ്റപ്പെടുത്തൽ എന്നതു ഉൾക്കൊള്ളുന്നു.

#### ഘടന പശ്ചാത്തലം

ഒരു ഉപയോക്താവ് സിയാട്ടിലിന്റെ യാത്ര പ്ലാൻ ചെയ്യാൻ ചോദ്യമിടുന്നു.

1.  **ഡിസ്‌പാച്ചർ (Fan-Out):** ഉപയോക്താവിന്റെ അഭ്യർത്ഥന രണ്ട് ഏജന്റുകൾക്കു സമകാലികമായി അയയ്ക്കുന്നു.
2.  **റിസർചർ ഏജന്റ്:** സിയാട്ടിൽ ഡിസംബറിൽ കാണേണ്ട ആകർഷണങ്ങളും കാലാവസ്ഥയും പ്രധാന കാര്യങ്ങളും ഗവേഷിക്കുന്നു.
3.  **പ്ലാൻ ഏജന്റ്:** സ്വതന്ത്രമായി ദിവസേന യാത്രാ പദ്ധതി തയ്യാറാക്കുന്നു.
4.  **അഗ്രിഗേറ്റർ (Fan-In):** റിസർചറും പ്ലാനറും നൽകുന്ന ഔട്ട്പുട്ടുകളെ സമാഹരിച്ച് അന്തിമ ഫലം രൂപപ്പെടുത്തുന്നു.

*സമകാലിക Researcher, Planner workflow യുടെ ചിത്രരൂപം.*

#### Python നടപ്പിലാക്കൽ വിശകലനം

`ConcurrentBuilder` ഈ മാതൃക സൃഷ്ടിക്കുന്നതിനെ ലളിതമാക്കുന്നു. പങ്കെടുത്ത ഏജന്റുകൾ ലിസ്റ്റ് ചെയ്യുന്നതിലേയ്ക്ക് മാത്രം, ബിൽഡർ ഫാൻ-ഔട്ട്/ഫാൻ-ഇൻ ലോജിക് ഓട്ടോമാറ്റിച്ച് സൃഷ്ടിക്കുന്നു.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ഫാന്‍-ഔട്ട്/ഫാന്‍-ഇന്‍ ലൊജിക്ക് കൈകാര്യം ചെയ്യുന്നു
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# വര്‍ക്ക്‌ഫ്ലേ തുറക്കുക
events = await workflow.run("Plan a trip to Seattle in December")
```

ഫ്രെയിംവർക്ക് `research_agent` ഉം `plan_agent` ഉം സമകാലികമായി നടത്തുകയും, അവയുടെ അന്തിമ ഔട്ട്പുട്ട് ലിസ്റ്റിൽ ഒത്തുചേർക്കുകയും ചെയ്യുന്നു.

#### .NET (C#) നടപ്പിലാക്കൽ വിശകലനം

.NET-ൽ ഈ മാതൃകം കൂടുതൽ വ്യക്തമായ നിർവചനമോുന്നതാണ് ആവശ്യമായത്. കസ്റ്റം എക്സിക്യുട്ടറുകൾ (`ConcurrentStartExecutor` ഉം `ConcurrentAggregationExecutor` ഉം) ഫാൻ-ഔട്ട്, ഫാൻ-ഇൻ ലോജിക് കൈകാര്യം ചെയ്യാൻ സൃഷ്ടിക്കുന്നു.

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

`WorkflowBuilder` തുടർന്ന് ഈ കസ്റ്റം എക്സിക്യൂട്ടറുകളുമായി ഏജന്റുകളെ ഫാൻ-ഔട്ട്, ഫാൻ-ഇൻ എഡ്ജുകൾ ചേർത്ത് ഗ്രാഫ് നിർമ്മിക്കുന്നു.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### കേസ് 4: ന്യൂനഗതം Workflow

ന്യൂനഗതം workflow-കൾ ബ്രാഞ്ചിംഗ് ലോജിക് പരിചയപ്പെടുത്തി സിസ്റ്റം ഇടക്കാല ഫലങ്ങളുടെ അടിസ്ഥാനത്തിൽ വ്യത്യസ്ത പാതകൾ സ്വീകരിക്കാൻ അനുവദിക്കുന്നു.

#### ഘടന പശ്ചാത്തലം

ഈ workflow സാങ്കേതിക ട്യൂട്ടോറിയൽ സൃഷ്ടിക്കുകയും പ്രസിദ്ധീകരിക്കുകയും ആണ് ഓട്ടോമേറ്റുചെയ്യുന്നത്.

1.  **Evangelist-Agent:** ഒരുoutlineഉം URL-ങ്ങളും അടിസ്ഥാനമാക്കി ട്യൂട്ടോറിയലിന്റെ ഡ്രാഫ്റ്റ് എഴുതുന്നു.
2.  **ContentReviewer-Agent:** ഡ്രാഫ്റ്റ് അവലോകനം ചെയ്യുന്നു. വാചകസംഖ്യ 200-കൂടെ ആണോ എന്ന് പരിശോധിക്കുന്നു.
3.  **ന്യൂനഗതം ബ്രാഞ്ച്:**
      * **അനുമതി (Yes)**: workflow `Publisher-Agent` ചേക്ക് മുന്നോട്ട് പോയും.
      * **നിഷേധം (No)**: workflow നിർത്തുകയും നിഷേധ കാരണം ഔട്ട്പുട്ട് ചെയ്യുകയും ചെയ്യും.
4.  **Publisher-Agent:** ഡ്രാഫ്റ്റ് അനുമതിയുണ്ടെങ്കിൽ, ഈ ഏജന്റ് ഉള്ളടക്കം Markdown ഫയലായി സംരക്ഷിക്കുന്നു.

#### Python നടപ്പിലാക്കൽ വിശകലനം

ഈ ഉദാഹരണത്തിൽ `select_targets` എന്ന ഒരു കസ്റ്റം ഫംഗ്ഷൻ ഉപയോഗിച്ച് ന്യൂനഗതം ലോജിക് നടപ്പിലാക്കുന്നു. ഈ ഫംഗ്ഷൻ `add_multi_selection_edge_group`-ലേക്ക് നൽകുകയും, റിവ്യൂവറുടെ ഔട്ട്‌പുട്ട്-ലെ `review_result` ഫീൽഡിനെ അടിസ്ഥാനമാക്കി workflow-നെ നയിക്കുന്നു.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ഈ ഫംഗ്ഷൻ റിവ്യൂ ഫലത്തിന്റെ അടിസ്ഥാനത്തിൽ അടുത്ത പടി നിർദ്ദേശിക്കുന്നു
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # അംഗീകരിച്ചാൽ, 'save_draft' എക്സിക്യൂട്ടറിലേക്ക് തുടരുക
        return [save_draft_id]
    else:
        # നിരസിച്ചാൽ, പരാജയം റിപ്പോർട്ട് ചെയ്യാൻ 'handle_review' എക്സിക്യൂട്ടറിലേക്ക് തുടരുക
        return [handle_review_id]

# വർക്ക്ഫ്ലോ ബിൽഡർ റൂട്ടിംഗിനായി സെലക്ഷൻ ഫംഗ്ഷൻ ഉപയോഗിക്കുന്നു
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # മൾട്ടി-സെലക്ഷൻ എഡ് കണ്ടീഷണൽ ലജിക്ക് നടപ്പാക്കുന്നു
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` പോലെയുള്ള കസ്റ്റം എക്സിക്യൂട്ടറുകൾ JSON ഔട്ട്പുട്ട് പാഴ്സിംഗ് ചെയ്ത് മજબൂതമായ ടൈപ്പിലുള്ള ഒബ്ജക്ടുകളായി മാറ്റുന്നു, തിരഞ്ഞെടുപ്പ് ഫംഗ്ഷൻ അവ പരിശോധിക്കാൻ കഴിയും.

#### .NET (C#) നടപ്പിലാക്കൽ വിശകലനം

.NET പതിപ്പ് സമാനമായ സമീപനം ഉപയോഗിക്കുന്നു, ഒരു `Func<object?, bool>` നിർവചിച്ച് `ReviewResult` ഒബ്ജക്ടിലെ `Result` പ്രോപ്പർട്ടി പരിശോധിക്കുന്നു.

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

`AddEdge` മാർഗ്ഗത്തിലെ `condition` പാരാമീറ്റർ വഴി `WorkflowBuilder` ബ്രാഞ്ച് പാത സൃഷ്ടിക്കുന്നു. `GetCondition(expectedResult: "Yes")` സത്യമായാൽ നിശ്ചിത എഡ്ജ് `publishExecutor`-യിലേക്കും, അല്ലെങ്കിൽ `sendReviewerExecutor`-യിലേക്കും workflow പിന്തുടരും.

## നിഗമനം

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് വർക്ഫ്ലോ സങ്കീർണ്ണ മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ നിയന്ത്രിക്കുന്നതിന് ശക്തമായ യോജിച്ച അടിത്തറ നൽകുന്നു. ഗ്രാഫ് അടിസ്ഥാനമായ ആർക്കിടെക്ചറും പ്രധാന ഘടകങ്ങളും ഉപയോഗിച്ച് ഡെവലപ്പർമാർക്ക് Python ഉം .NET ഉം ഉപയോഗിച്ച് സങ്കീർണ്ണ workflow കൾ രൂപകൽപ്പന ചെയ്ത് നടപ്പിലാക്കാനാകും. നിങ്ങളുടെ അപ്ലിക്കേഷൻ ലളിതമായ കൃത്യാനുചരണ പ്രോസസ്സിംഗ്, സമകാലിക എക്സിക്യൂഷൻ, ഡൈനാമിക് ന്യൂനഗതം ലോജിക് എന്നിവ ആവശ്യപ്പെടുകയാണെങ്കിൽ, ഈ ഫ്രെയിംവർക്ക് ശക്തമായ, സ്കെയിലബിൾ, ടൈപ്പ് സുരക്ഷിത AI-ആധാരിത പരിഹാരങ്ങൾ നിർമ്മിക്കാൻ ഉപകരണങ്ങൾ വാഗ്ദാനം ചെയ്യുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->