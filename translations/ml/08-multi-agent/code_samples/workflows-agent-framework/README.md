# മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് വർ크ഫ്ലോ ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റ് അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കൽ

ഈ പരിശീലന പരിപാടി മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റ് അപ്ലിക്കേഷനുകൾ മനസ്സിലാക്കുകയും നിർമ്മിക്കുകയുമാണ് നിങ്ങളെ വഴികാട്ടുന്നത്. മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങളുടെ മേധാവി ആശയങ്ങൾ പരിശോധിക്കും, ഫ്രെയിംവർക്കിന്റെ വർക്ക്‌ഫ്ലോ ഘടകത്തിന്റെ ആർക്കിടെക്ചറിലേക്ക് േഴുകി പ്രവേശിക്കും, വ്യത്യസ്ത വർക്ക്‌ഫ്ലോ പാറ്റേണുകൾക്ക് പൈതൺയും .NET എന്നിവയിലുമായി പ്രായോഗിക ഉദാഹരണങ്ങൾ നടത്തുന്നുമുണ്ട്.

## 1\. മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ മനസ്സിലാക്കൽ

ഒരു AI ഏജന്റ് സാധാരണ മര്യാദയിൽ ഒരു വലിയ ഭാഷ മോഡലിന്റെ (LLM) കഴിവുകൾക്കു മുകളിൽ പ്രവർത്തിക്കുന്ന ഒരു സിസ്റ്റമാണ്. ഇത് അതിന്റെ പരിസരങ്ങൾ അനുഭവിക്കുകയും, തീരുമാനങ്ങൾ എടുക്കുകയും, പ്രത്യേക ലക്ഷ്യങ്ങൾ സാദ്ധ്യമാക്കാൻ പ്രവർത്തിക്കുകയും ചെയ്യും. മൾട്ടി-ഏജന്റ് സിസ്റ്റം ഒരേ സമയം നിരവധി ഏജന്റുകൾ ചേർന്നു ഒരു സങ്കീർണ്ണ പ്രശ്നം പരിഹരിക്കുന്നതാണ്, അത് ഒരേ ഏജന്റിന് ഒറ്റയ്ക്ക് ചെയ്യാൻ പ്രയാസമുള്ളതാണ്.

### സാധാരണ ഉപയോഗ സാഹചര്യങ്ങൾ

  * **സങ്കീർണ്ണ പ്രശ്ന പരിഹാരം**: ഒരു വലിയ ജോലി (ഉദാ: ഒരു കമ്പനിയുടെ പൊതുവായ പദ്ധതിയുടെ) ചെറിയ ഉപജോലികളായി വിഭജിച്ച് സവിശേഷ ഏജന്റുകളാൽ കൈകാര്യം ചെയ്യുക (ഉദാ: ബജറ്റ് ഏജന്റ്, ലജിസ്റ്റിക്സ് ഏജന്റ്, മാർക്കറ്റിംഗ് ഏജന്റ്).
  * **വെർച്വൽ അസിസ്റ്റന്റുകൾ**: ഒരു മുഖ്യ അസിസ്റ്റന്റ് ഏജന്റ് ഷെഡ്യൂളിംഗ്, ഗവേഷണം, ബുക്കിംഗ് തുടങ്ങിയ ജോലികൾ മറ്റ് പ്രത്യേക ഏജന്റുകൾക്ക് കൈമാറൽ നടത്തുന്നു.
  * **സ്വയം പ്രവർത്തിക്കുന്ന ഉള്ളടക്ക നിർമ്മാണം**: ഒരാൾ ഉള്ളടക്കം രൂപരേഖപ്പെടുത്തുന്നു, മറ്റൊന്ന് അവ വിലയിരുത്തുന്നു ശരിയാകുകയും ശൈലി പരിശോധിക്കുകയും, മൂന്നാമത്തെയാൾ പ്രസിദ്ധീകരിക്കുന്നു.

### മൾട്ടി-ഏജന്റ് പാറ്റേണുകൾ

മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ വിവിധ പാറ്റേണുകളിൽ ക്രമീകരിക്കാവുന്നതാണ്, അവ എങ്ങനെ സംവദിക്കുന്നു എന്നതിനെ നിർണയിക്കുന്നു:

  * **ക്രമിക (Sequential)**: ഏജന്റുകൾ മുന്നിജ്ഞാനം ക്രമത്തിൽ പ്രവർത്തിക്കുന്നു, അസംബ്ലി ലൈൻ പോലെയാണ്. ഒരാൾ നൽകിയ output അടുത്തയാളുടെ input ആകുന്നു.
  * **സമകാലിക (Concurrent)**: ഏജന്റുകൾ ഒരേ സമയം വ്യത്യസ്ത ഭാഗങ്ങളിൽ പ്രവർത്തിച്ച്, അവരുടെ ഫലം ഒടുവിൽ ഒന്നിച്ച് ചേർക്കുന്നു.
  * **നിബന്ധനാത്മക (Conditional)**: ഒരു ഏജന്റിന്റെ output അടിസ്ഥാനമാക്കി വ്യത്യസ്ത പാതകളിലൂടെ പ്രവണത നടത്തുന്നതു്, if-then-else പ്രസ്താവന പോലെയാണ്.

## 2\. മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് വർക്ക്‌ഫ്ലോ ആർക്കിടെക്ചർ

ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ വർക്ക്‌ഫ്ലോ സിസ്റ്റം സങ്കീർണ്ണമായ വിവിധ ഏജന്റുകൾ തമ്മിലുള്ള സംവാദങ്ങൾ നിയന്ത്രിക്കുന്ന ഒരു പ്രഗത്ഭ ഓർക്കസ്ട്രേഷൻ എൻജിനാണ്. ഇത് ഒരു ഗ്രാഫ് അടിസ്ഥാനമാക്കിയിട്ടുള്ള ആർക്കിടെക്ചറിൽ നിർമ്മിച്ചിരിക്കുന്നു, [പ്രെഗെൽ-ശൈലി എക്സിക്യൂഷൻ മോഡൽ](https://kowshik.github.io/JPregel/pregel_paper.pdf) ഉപയോഗിച്ച് "സൂപ്പർസ്റ്റെപ്പുകൾ" എന്ന同期 നടപടികളിലൂടെ പ്രവർത്തിക്കുന്നു.

### പ്രധാന ഘടകങ്ങൾ

ആർക്കിടെക്ചർ മൂന്നു പ്രധാന ഭാഗങ്ങളാൽ നിര്‍മ്മിച്ചിരിക്കുന്നു:

1.  **എക്സിക്യൂട്ടർമാർ (Executors)**: ഇവ അടിസ്ഥാന പ്രോസസ്സിംഗ് യൂണിറ്റുകളാണ്. ഞങ്ങളുടെ ഉദാഹരണങ്ങളിൽ, `Agent` ഒരു എക്സിക്യൂട്ടർ തരം ആണ്. ഓരോ എക്സിക്യൂട്ടർക്കും സ്വീകരിക്കുന്ന സന്ദേശ തരം അനുസരിച്ച് സ്വയം പ്രവർത്തിക്കുന്ന ഭാരങ്ങൾ ഉണ്ട്.
2.  **എഡ്ജുകൾ (Edges)**: സംവാദങ്ങൾ എക്സിക്യൂട്ടർമാരുടെ ഇടയിൽ പിന്നിൽ എടുക്കുന്ന വഴി നിർവ്വചിക്കുന്നു. എഡ്ജുകൾക്ക് നിബന്ധനകൾ ഉണ്ടാകാം, ഇവ വർക്ക്‌ഫ്ലോ ഗ്രാഫിലൂടെ ഡൈനാമിക് റൂട്ടിംഗ് നടത്തുന്നു.
3.  **വർക്ക്‌ഫ്ലോ (Workflow)**: ഈ ഘടകം മുഴുവൻ പ്രക്രിയയെയും നിയന്ത്രിക്കുന്നു, എക്സിക്യൂട്ടർമാരും എഡ്ജുകളും ആകെ പ്രവർത്തനവും നിയന്ത്രിക്കുന്നു. സന്ദേശം ശരിയായ ക്രമത്തിൽ കൈകാര്യം ചെയ്യുന്നതും ഇവന്റുകൾ സ്റ്റ്രീം ചെയ്ത് നിരീക്ഷണം సുലഭമാക്കുന്നതും ഉറപ്പാക്കുന്നു.

*വർക്ക്‌ഫ്ലോ സിസ്റ്റത്തിന്റെ പ്രധാന ഘടകങ്ങൾ കാണിക്കുന്ന ഒരു രേഖാചിത്രം.*

ഈ ഘടന ശക്തമായ, സ്കെയിലബിൾ അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാൻ അനുമതിയുള്ളതും, ക്രമിക ചൈനുകൾ, പാരലൽ പ്രോസസ്സിംഗിന് ഫാൻ-ഔട്/ഫാൻ-ഇൻ, നിബന്ധനാത്മക പ്രവണതയ്ക്ക് സ്വിച്ച്-കേസ് ലോജിക് പോലുള്ള അടിസ്ഥാന പാറ്റേണുകൾ ഉൾക്കൊള്ളുന്നുമാണ്.

## 3\. പ്രായോഗിക ഉദാഹരണങ്ങളും കോഡ് വിശകലനവും

ഇപ്പോൾ ഫ്രെയിംവർക്കിനു ഉപയോഗിച്ച് വ്യത്യസ്ത വർക്ക്‌ഫ്ലോ പാറ്റേണുകൾ എങ്ങനെ നടപ്പിലാക്കാമെന്ന് പരിശോധിക്കാം. ഓരോ ഉദാഹരണത്തിന്റെയും പൈതൺ, .NET കോഡും നോക്കാം.

### കേസ് 1: അടിസ്ഥാന ക്രമിക വർക്ക്‌ഫ്ലോ

ഇത് ഏറ്റവും ലളിതമായ പാറ്റേണാണ്, ഒരേയൊരു ഏജന്റിന്റെ output നേരിട്ട് അടുത്തയാളുടെ input ആയി നീങ്ങുന്നു. ഹോട്ട്‌വേൽ `FrontDesk` ഏജന്റ് യാത്രാ ശുപാർശകൾ നൽകുന്നു, തുടർന്ന് `Concierge` ഏജന്റ് അവ അവലോകനം ചെയ്യുന്നു.

*അടിസ്ഥാന FrontDesk -> Concierge വർക്ക്‌ഫ്ലോയുടെ രേഖാചിത്രം.*

#### പശ്ചാത്തല ഗതി

ഒരു യാത്രക്കാരന് പാരീസിൽ ശുപാർശ ചോദിക്കുന്നു.

1.  ലഘുത്വത്തിനായി ഡിസൈൻ ചെയ്ത `FrontDesk` ഏജന്റ് ലൂവ്ര് മ്യൂസിയം സന്ദർശിക്കാൻ ശുപാർശ ചെയ്യുന്നു.
2.  യഥാർത്ഥ അനുഭവങ്ങൾക്ക് മുൻഗണന നൽകുന്ന `Concierge` ഏജന്റ് ഈ ശുപാർശ സ്വീകരിച്ച് അവലോകനം നടത്തി കൂടുതൽ പ്രാദേശികവും കുറവ് വിനോദസഞ്ചാരികളും ആയ বিকল্পം നിർദ്ദേശിക്കുന്നു.

#### പൈതൺ നടപ്പാക്കൽ വിശകലനം

പൈതൺ ഉദാഹരണത്തിൽ ആദ്യം രണ്ട് ഏജന്റുകളും അവരുടെ നിർദ്ദേശങ്ങളോടൊപ്പം നിർവചിച്ച് സൃഷ്ടിക്കുന്നു.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# ഏജന്റ് رولുകളും നിർദ്ദേശങ്ങളും നിർവചിക്കുക
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
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

പിന്നീട് `WorkflowBuilder` ഉപയോഗിച്ച് ഗ്രാഫ് നിർമ്മിക്കുന്നു. `front_desk_agent` ആരംഭ ബിന്ദുവായി നിശ്ചയിച്ച് അതിന്റെ output `reviewer_agent` നുമായി കണക്ട് ചെയ്യുന്ന ഒരു എഡ്ജ് ഉണ്ടാക്കുന്നു.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

അവസാനം ആരംഭയൂസർ പ്രോംപ്റ്റോടെ വർക്ക്‌ഫ്ലോ Eliasവാണ്.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run workflow പ്രവര്‍ത്തിപ്പിക്കുന്നു; get_outputs() ഔട്ട്‌പുട് എക്സിക്യൂട്ടറിന്റെ ഫലം തിരിച്ചുകൊടുക്കുന്നു.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) നടപ്പാക്കൽ വിശകലനം

.NET നടപ്പാക്കൽ സമാനമായ തത്വം പിന്തുടരുന്നു. ആദ്യം ഏജന്റുകളുടെ പേര്, നിർദ്ദേശങ്ങൾ സ്ഥിര്യമായ മൂല്യങ്ങൾ ആയി നിർവചിക്കുന്നു.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`AzureOpenAIClient` (Responses API) ഉപയോഗിച്ച് ഏജന്റുകൾ സൃഷ്ടിച്ച്, തുടർന്ന് `WorkflowBuilder` `frontDeskAgent` യിൽ നിന്നുള്ള output `reviewerAgent` ലേക്ക് എഡ്ജ് ചേർക്കുന്നു.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

തുടർന്ന് യൂസർ മെസ്സേജ് ഉപയോഗിച്ച് വർക്ക്‌ഫ്ലോ Eliasവിച്ച് ഫലം സ്റ്റ്രീം ചെയ്തു.

### കേസ് 2: മൾട്ടി-സ്റ്റെപ്പ് ക്രമിക വർക്ക്‌ഫ്ലോ

ഈ പാറ്റേൺ അടിസ്ഥാന ക്രമം കൂടുതൽ ഏജന്റുകളെ ഉൾകൊള്ളിക്കാൻ നീട്ടുന്നു. സങ്കീർണ്ണമായ പുതിയഘട്ടങ്ങളോ പരിവർത്തനങ്ങളോ ആവശ്യമായ പ്രക്രിയകൾക്ക് അനുയോജ്യമാണ്.

#### പശ്ചാത്തല ഗതി

ഒരു ഉപയോക്താവ് ലിവിംഗ് റൂമിന്റെ ചിത്രം നൽകുകയും മൂല്യനിർണ്ണയത്തിനായി ഫർണിച്ചർ വിലക്കൂട്ടൽ ചോദിക്കുകയും ചെയ്യുന്നു.

1.  **സെയിൽസ് ഏജന്റ്**: ചിത്രത്തിലുള്ള ഫർണിച്ചർ ഇനങ്ങൾ തിരിച്ചറിയുകയും പട്ടിക സൃഷ്ടിക്കുകയും ചെയ്യുന്നു.
2.  **പ്രൈസ് ഏജന്റ്**: ഇനങ്ങളുടെ വില വിശദീകരിക്കുന്ന ഒരു പട്ടിക നൽകുന്നു, ബജറ്റ്, മിഡ്-റേഞ്ച്, പ്രീമിയം ഓപ്ഷനുകൾ ഉൾപ്പെടെ.
3.  **കോടേഷൻ ഏജന്റ്**: വിലപ്പെടുത്തിയ പട്ടിക സ്വീകരിച്ച് Markdown ഫോംറിൽ ഔദ്യോഗിക കോട്ടേഷൻ ഡോക്യുമെന്റ് രൂപപ്പെടുത്തുന്നു.

*Sales -> Price -> Quote വർക്ക്‌ഫ്ലോയുടെ രേഖാചിത്രം.*

#### പൈതൺ നടപ്പാക്കൽ വിശകലനം

മൂന്നുദൈനി ഏജന്റുകൾ ഓരോത് പ്രത്യേക പങ്ക് വഹിക്കുന്നു. `add_edge` ഉപയോഗിച്ച് `sales_agent` -> `price_agent` -> `quote_agent` എന്ന ദൃഢചെയിൻ നിർമ്മിക്കുന്നു.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# മൂന്നു പ്രത്യേക ഏജന്റ്മാരെ സൃഷ്ടിക്കുക
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# തുടരുള്ള പ്രവൃത്തി പ്രക്രിയ നിർമ്മിക്കുക
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ഇന്പുട്ട് ഒരു `ChatMessage` ആണെന്ന്, അതിൽ ടെക്സ്റ്റും ചിത്ര URIയും ഉണ്ട്. ഫ്രെയിംവർക്ക് ഏജന്റിന്റെ output അടുത്തയാളിലേക്ക് ഈ ക്രമത്തിൽ കൈമാറി ഒടുവിൽ കോട്ടേഷൻ സൃഷ്ടിക്കുന്നു.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ഉപയോക്തൃ സന്ദേശത്തിൽ എഴുത്തും ഒരു ചിത്രം എന്നിവ ഉണ്ട്
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# പ്രവൃത്തി പ്രവാഹം പ്രവർത്തിക്കുക
events = await workflow.run(message)
```

#### .NET (C\#) നടപ്പാക്കൽ വിശകലനം

.NET ഉദാഹരണം പൈതൺ പതിപ്പിനെ അനുസരിക്കുന്നു. മൂന്ന് ഏജന്റുകൾ `salesagent`, `priceagent`, `quoteagent` സൃഷ്ടിക്കുന്നു. `WorkflowBuilder` അവയെ ക്രമികമായി ബന്ധിപ്പിക്കുന്നു.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

യൂസർ മെസ്സേജ് ചിത്ര ഡാറ്റയും (ബൈറ്റ്സായി) ടെക്സ്റ്റും ഉൾക്കൊള്ളിക്കുന്നു. `InProcessExecution.RunStreamingAsync` ആരംഭിച്ച് അന്തിമ ഫലം സ്ട്രീമിൽ നിന്ന് പിടിക്കുന്നു.

### കേസ് 3: സമകാലിക വർക്ക്‌ഫ്ലോ

ജോലികൾ ഒരേസമയം ചെയ്യാനാകുമ്പോൾ സമയം ലാഭിക്കാനായി ഈ പാറ്റേൺ ഉപയോഗിക്കുന്നു. ഒന്നിൽ നിന്ന് പല ഏജന്റുകളിലേക്ക് "ഫാൻ-ഔട്" ഉം അവസാനം ഫലങ്ങൾ "ഫാൻ-ഇൻ" ആയി ചേരുന്നതും ഉൾപ്പെടുന്നു.

#### പശ്ചാത്തല ഗതി

ഒരു ഉപയോക്താവ് സിയാറ്റിലിലേക്ക് ഒരു യാത്ര ആസൂത്രണം ചെയ്യാൻ പറയുന്നു.

1.  **ഡിസ്പാച്ചർ (Fan-Out)**: ഉപയോക്താവിന്റെ അഭ്യർത്ഥന രണ്ട് ഏജന്റുകൾക്ക് ഒരേസമയം അയക്കുന്നു.
2.  **ഗവേഷണ ഏജന്റ്**: സിയാറ്റിലിന്റെ ആകർഷണങ്ങൾ, കാലാവസ്ഥ, ഡിസംബർ മാസത്തിലെ പ്രധാന കാര്യങ്ങൾ അന്വേഷിക്കുന്നു.
3.  **പ്ലാൻ ഏജന്റ്**: സ്വതന്ത്രമായി പാതി പാതിയായ യാത്രയുടെ വിശദമായ ദിവസംപ്രതി യാത്രാസൂചിക നിർമ്മിക്കുന്നു.
4.  **അഗ്‌ഗ്രിഗേറ്റർ (Fan-In)**: ഗവേഷകന്റെയും പ്ലാനറിന്റെയും output കളെ ശേഖരിച്ച് ഒടുവിൽ ഒന്നാക്കി അവതരിപ്പിക്കുന്നു.

*Concurrent Researcher and Planner വർക്ക്‌ഫ്ലോയുടെ രേഖാചിത്രം.*

#### പൈതൺ നടപ്പാക്കൽ വിശകലനം

`ConcurrentBuilder` ഈ പാറ്റേൺ നിർമ്മിക്കാൻ എളുപ്പമാക്കുന്നു. പങ്കാളി ഏജന്റുകളുടെ പട്ടിക നൽകുക മാത്രമെ ആവശ്യമുള്ളൂ, ബിൽഡർ സ്വയം ഫാൻ-ഔട്/ഫാൻ-ഇൻ അടക്കമുള്ള ലജിക് സൃഷ്ടിക്കും.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ഫാൻ-ഔട്ട്/ഫാൻ-ഇൻ ലജിക്ക് കൈകാര്യം ചെയ്യുന്നു
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# വർക്ക്‌ഫ്ലോ പ്രവർത്തിപ്പിക്കുക
events = await workflow.run("Plan a trip to Seattle in December")
```

ഫ്രെയിംവർക്ക് `research_agent` ഉം `plan_agent` ഉം പോരഴിക്കുന്നു, അവയുടെ അന്തിമ ഫലങ്ങൾ ഒരു ലിസ്റ്റിലായി ശേഖരിക്കുന്നു.

#### .NET (C\#) നടപ്പാക്കൽ വിശകലനം

.NETൽ ഈ പാറ്റേൺ കൂടുതൽ വ്യക്തമായ നിർവചനത്തെ ആവശ്യമുള്ളതാണ്. കസ്റ്റം എക്സിക്യൂട്ടർമാരായ `ConcurrentStartExecutor`യും `ConcurrentAggregationExecutor`യും ഫാൻ-ഔട്, ഫാൻ-ഇൻ ലജിക് കൈകാര്യം ചെയ്യാൻ സൃഷ്ടിക്കുന്നു.

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

`WorkflowBuilder` പിന്നീട് ഈ കസ്റ്റം എക്സിക്യൂട്ടർമാരുടെയും ഏജന്റുകളുടെയും സഹായത്തോടെ `AddFanOutEdge` ഉം `AddFanInEdge` ഉം ഉപയോഗിച്ച് ഗ്രാഫ് നിർമ്മിക്കുന്നു.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### കേസ് 4: നിബന്ധനാത്മക വർക്ക്‌ഫ്ലോ

നിബന്ധനാത്മക വർക്ക്‌ഫ്ലോകൾ ശാഖപ്പെടുത്തലിലൂടെ പ്രവർത്തിക്കുന്നു, ഇടനിട ഫലങ്ങളുടെ അടിസ്ഥാനമാക്കി വ്യത്യസ്ത പാതകൾ സ്വീകരിക്കാൻ സിസ്റ്റം അനുവദിക്കുന്നു.

#### പശ്ചാത്തല ഗതി

ഒരു സാങ്കേതിക പാഠപുസ്തകം സ്വയം നിർമ്മിച്ച് പ്രസിദ്ധീകരിക്കുന്ന വർക്ക്‌ഫ്ലോ ആണ് ഇത്.

1.  **Evangelist-Agent**: നൽകിയ അവലോകനംയും URL കളും അടിസ്ഥാനമാക്കി പാഠം എഴുതുന്നു.
2.  **ContentReviewer-Agent**: പാഠം പരിശോധിക്കുന്നു. വാക്കിന്റെ എണ്ണം 200 കടക്കുന്നതാണോ എന്ന് പരിശോധിക്കുന്നു.
3.  **നിബന്ധന ശാഖ**:
      * **അംഗീകൃതമായാൽ (`Yes`)**: വർക്ക്‌ഫ്ലോ `Publisher-Agent` എത്തുന്നു.
      * **പ്രതിഷേധിക്കപ്പെട്ടാൽ (`No`)**: വർക്ക്‌ഫ്ലോ توقف ചെയ്ത് കാരണം output ആക്കി നൽകുന്നു.
4.  **Publisher-Agent**: പാഠം അംഗീകാരം ലഭിച്ചാൽ Markdown ഫയലായി സംരക്ഷിക്കുന്നു.

#### പൈതൺ നടപ്പാക്കൽ വിശകലനം

`select_targets` എന്ന കസ്റ്റം ഫംഗ്ഷൻ ഉപയോഗിച്ച് നിബന്ധനാത്മക ലജിക് നടപ്പാക്കുന്നു. ഇത് `add_multi_selection_edge_group` കു പാസ്സ് ചെയ്ത് `reviewer` output യിലെ `review_result` എന്ന ഫീൽഡിനെ അടിസ്ഥാനമാക്കി വർക്ക്‌ഫ്ലോ ദിശാഗതം നിർണ്ണയിക്കുന്നു.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ഈ ഫംഗ്ഷൻ റിവ്യൂ ഫലത്തിന്റെ അടിസ്ഥാനത്തിൽ അടുത്ത ഘട്ടം നിർണയിക്കുന്നു
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ആട്ടു നൽകിയാൽ, 'save_draft' എക്സിക്യൂട്ടറിലേക്ക് മുന്നോട്ട് പോവുക
        return [save_draft_id]
    else:
        # നിരസിച്ചെങ്കിൽ, പരാജയം റിപ്പോർട്ട് ചെയ്യാൻ 'handle_review' എക്സിക്യൂട്ടറിലേക്ക് മുന്നോട്ട് പോവുക
        return [handle_review_id]

# വർക്ക്‌ഫ്ലോ ബിൽഡർ റൂട്ടിംഗിനായി സെലക്ഷൻ ഫങ്ഷൻ ഉപയോഗിക്കുന്നു
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # മൾട്ടി-സെലക്ഷൻ എഡ്ജ് വ്യഞ്ജനാത്മക ലോഗിക് നടപ്പാക്കുന്നു
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` പോലുള്ള കസ്റ്റം എക്സിക്യൂട്ടറുകൾ ഏജന്റുകളുടെ JSON output നിർവ്വചിച്ച സ്ട്രോങ്-ടൈപ്പ് ഒബ്ജക്റ്റുകളിലേക്ക് മാറ്റാൻ ഉപയോഗിക്കുന്നു, സേവനം തിരഞ്ഞെടുക്കുന്ന ഫംഗ്ഷൻ പരിശോധിക്കാൻ കഴിയും.

#### .NET (C\#) നടപ്പാക്കൽ വിശകലനം

.NET പതിപ്പ് സമാനമായ സമീപനം സ്വീകാര്യമാക്കുന്നു. `Func<object?, bool>` ഒരെണ്ണം നിർവചിച്ച് `ReviewResult` ഓബ്ജക്റ്റിന്റെ `Result` പദം പരിശോധിക്കുന്നു.

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

`AddEdge` സവിശേഷതയിൽ ഉള്ള `condition` പാരാമീറ്റർ ഉപയോഗിച്ച് `WorkflowBuilder` ബ്രാഞ്ചിംഗ് പാത സൃഷ്ടിക്കുന്നു. നിബന്ധന `GetCondition(expectedResult: "Yes")` ശരിയാണെങ്കിൽ മാത്രമേ `publishExecutor` ലേക്ക് കൂടിക്കാഴ്ച നടത്തുകയുള്ളൂ. അല്ലെങ്കിൽ `sendReviewerExecutor` നു പാത തുടരുന്നു.

## സംക്ഷേപം

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് വർക്ക്‌ഫ്ലോ ശക്തമായ, ലളിതവും അനുകൂലവുമായ അടിസ്ഥാനവും പ്രദാനം ചെയ്യുന്നു, സങ്കീർണ്ണ മൾട്ടി-ഏജന്റ് സിസ്റ്റങ്ങൾ നിയന്ത്രിക്കാൻ ഉപയോഗിക്കാം. ഗ്രാഫ് അടിസ്ഥാനമാക്കിയ ആർക്കിടെക്ചറും പ്രധാന ഘടകങ്ങളും വിനിയോഗിച്ച്, ഡെവലപ്പർമാർ പൈതണിലും .NETൽ ഫലപ്രദവും സംഖ്യാത്മകവുമായ വർക്ക്‌ഫ്ലോകൾ ഡിസൈൻ ചെയ്ത് നടപ്പിലാക്കാൻ കഴിയും. ലളിതമായ ക്രമിക പ്രോസസ്സിംഗ് ആഗ്രഹിക്കുന്നുവെങ്കിലും, പാരലൽ ഏകീകരണമോ, ഡൈനാമിക് നിബന്ധനാത്മക ലജിക്കോ ആവശ്യമുള്ളാലും, ഈ ഫ്രെയിംവർക്ക് കരുത്തുള്ള, സ്കെയിലബിൾ, ടൈപ്പ്-സേഫ് AI ഉറച്ച പരിഹാരങ്ങൾ നിർമ്മിക്കാൻ സാദ്ധ്യമാക്കുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->