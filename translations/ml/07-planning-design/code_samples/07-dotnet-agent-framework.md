# 🎯 Azure OpenAI (Responses API) ഉപയോഗിച്ചുള്ള പ്ലാനിംഗ് & ഡിസൈൻ പാറ്റേൺസ് (.NET)

## 📋 പഠനലക്ഷ്യങ്ങൾ

ഈ നോട്ട്ബುക്ക് Microsoft Agent Framework ഉപയോഗിച്ച് .NET-ൽ Azure OpenAI (Responses API) ഉപയോഗിച്ച് ബുദ്ധിമുട്ടുള്ള ഏജന്റുകൾ നിർമ്മിക്കുന്നതിനുള്ള എന്റർപ്രൈസ്-ഗ്രേഡ് പ്ലാനിംഗ്, ഡിസൈൻ പാറ്റേൺസുകൾ പ്രദർശിപ്പിക്കുന്നു. നിങ്ങൾക്ക് സങ്കീർണ്ണപ്രശ്നങ്ങൾ വിഭജിച്ച്, ബഹുവിധ നിലാണ് പരിഹാരങ്ങൾ ആസൂത്രണം ചെയ്ത്, .NET-ന്റെ എന്റർപ്രൈസ് സവിശേഷതകൾ ഉപയോഗിച്ച് സങ്കീർണ്ണ വർക്ഫ്ലോകൾ പ്രവർത്തിപ്പിക്കാൻ കഴിയുന്ന ഏജന്റുകൾ സൃഷ്ടിക്കാനാകും.

## ⚙️ മുൻകൂട്ടി അറിയേണ്ടതും സെറ്റപ്പ്

**ഡെവലപ്പ്‌മെന്റ് പരിതസ്ഥിതി:**
- .NET 9.0 SDK അല്ലെങ്കിൽ അതിൽ മുകളില്‍
- Visual Studio 2022 അല്ലെങ്കിൽ C# എക്സ്റ്റെൻഷൻ ഉള്ള VS Code
- Azure OpenAI റിസോഴ്‌സ് ഉള്ള ഒരു Azure ഉപഭോക്തൃ ഗണന
- Azure CLI — `az login` ഉപയോഗിച്ച് സൈൻ ഇൻ ചെയ്യുക

**ആവശ്യമായ ആശ്രിതങ്ങൾ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**പാരിസ്ഥിതിക ക്രമീകരണം (.env ഫയൽ):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## കോഡ് പ്രവർത്തിപ്പിക്കൽ

ഈ പാഠത്തിൽ .NET Single File App നടപ്പാക്കലുണ്ട്. പ്രവർത്തിപ്പിക്കാൻ:

```bash
# ഫയൽ നിർവ്വഹണയോഗ്യമാക്കുക (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# അപ്ലിക്കേഷൻ പ്രവർത്തിപ്പിക്കുക
./07-dotnet-agent-framework.cs
```

അല്ലെങ്കിൽ dotnet run കമാൻഡ് ഉപയോഗിക്കുക:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## കോഡ് നടപ്പാക്കൽ

പൂര്‍ണ്ണ നടപ്പാക്കൽ `07-dotnet-agent-framework.cs`ൽ ലഭ്യമാണ്, ഇത് പ്രകടിപ്പിക്കുന്നത്:

- DotNetEnv ഉപയോഗിച്ച് പരിസ്ഥിതി ക്രമീകരണം ലോഡ് ചെയ്യൽ
- Azure OpenAI ക്ലയന്റ് Responses API-യ്ക്കായി ക്രമീകരിക്കൽ
- JSON സീരിയലൈസേഷനോടുകൂടിയ സ്ട്രക്ചർ ഡേറ്റ മോഡലുകൾ (Plan, TravelPlan) നിർവ്വചിക്കൽ
- JSON സ്‌കീമ ഉപയോഗിച്ച് സ്ട്രക്ചർഡ് ഔട്ട്‌പുട്ട് ഉള്ള AI ഏജന്റ് സൃഷ്ടിക്കൽ
- ടൈപ്പ്-സേഫ് പ്രതികരണങ്ങളോടുള്ള പ്ലാനിംഗ് അഭ്യർത്ഥനകൾ നിർവ്വഹിക്കൽ

## പ്രധാന ആശയങ്ങൾ

### ടൈപ്പ്-സേഫ് മോഡലുകളോടുള്ള സ്ട്രക്ചർഡ് പ്ലാനിംഗ്

ഏജന്റ് പ്ലാനിംഗ് ഔട്ട്പുട്ടുകളെ നിർവ്വചിക്കാൻ C# ക്ലാസുകൾ ഉപയോഗിക്കുന്നു:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### സ്ട്രക്ചർഡ് ഔട്ട്പുട്ടുകൾക്കുള്ള JSON സ്‌കീമ

ഏജന്റ് TravelPlan സ്‌കീമയോട് പൊരുത്തപ്പെടുന്ന പ്രതികരണങ്ങൾ നൽകാൻ ക്രമീകരിച്ചിരിക്കുന്നു:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### പ്ലാനിംഗ് ഏജന്റ് നിർദേശങ്ങൾ

ഏജന്റ് ഒരു കോർഡിനേറ്ററായി പ്രവർത്തിച്ചുകൊണ്ട് പ്രത്യേക ശാഖ ഏജന്റുകൾക്ക് പ്രവൃത്തികൾ അർപ്പിക്കുന്നു:

- FlightBooking: വിമാന ബുക്കിംഗിനും വിമാന വിവരങ്ങൾ നൽകാനും
- HotelBooking: ഹോട്ടൽ ബുക്കിംഗിനും ഹോട്ടൽ വിവരങ്ങൾ നൽകാനും
- CarRental: കാറുകൾ ബുക്ക് ചെയ്ത് കാർ വാടക വിവരങ്ങൾ നൽകാനും
- ActivitiesBooking: പ്രവർത്തനങ്ങൾ ബുക്ക് ചെയ്ത് പ്രവർത്തന വിവരങ്ങൾ നൽകാനും
- DestinationInfo: ഗമ്യസ്ഥലങ്ങളെക്കുറിച്ചുള്ള വിവരങ്ങൾ നൽകാൻ
- DefaultAgent: പൊതുവായ അഭ്യർത്ഥന കൈകാര്യം ചെയ്യാൻ

## പ്രതീക്ഷിക്കാവുന്ന ഔട്ട്പുട്ട്

യാത്രാ പ്ലാനിംഗ് അഭ്യർത്ഥനയോടുകൂടി ഏജന്റ് പ്രവർത്തിപ്പിക്കുമ്പോൾ, അത് അഭ്യർത്ഥന വിശകലനം ചെയ്ത് TravelPlan സ്‌കീമയ്ക്ക് അനുയോജ്യമായ രൂപത്തിൽ പ്രത്യേക രേഖപ്പെടുത്തിയ ഏജന്റുകളിൽ പണി അനുവദിച്ചുള്ള ഘടനാപരമായ പദ്ധതി JSON ആകാരം സൃഷ്ടിക്കും.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->