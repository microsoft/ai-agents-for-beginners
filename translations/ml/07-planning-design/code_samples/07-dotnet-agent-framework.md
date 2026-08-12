# 🎯 ആസ്യൂർ ഓപ്പൺഎഐ (レスപോൺസ് API) (.NET) ഉപയോഗിച്ച് പ്ലാനിംഗ് & ഡിസൈൻ പാറ്റേണുകൾ

## 📋 പഠന ലക്ഷ്യങ്ങൾ

ഈ നോട്ട്‌ബുക്ക് മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് .NET ലും ആസ്യൂർ ഓപ്പൺഎഐ (レスപോൺസ് API) ഉപയോഗിച്ച് ബുദ്ധിമുട്ടുള്ള ഏജന്റുകൾ നിർമാണത്തിന് എന്റർപ്രൈസ് ഗ്രേഡ് പ്ലാനിംഗ്, ഡിസൈൻ പാറ്റേണുകൾ പ്രദർശിപ്പിക്കുന്നു. .NET ന്റെ എന്റർപ്രൈസ് ഫീച്ചറുകൾ ഉപയോഗിച്ച് 計算ായ പ്രശ്‌നങ്ങൾ വകവെട്ടി, മൾട്ടി-സ്റ്റെപ്പ് പരിഹാരങ്ങൾ പദ്ധതിയിട്ടു, സങ്കീർണ്ണമായ ವರ್ಕ്‌ഫ്ലോകൾ നടപ്പിലാക്കാൻ ഏജന്റുകൾ സൃഷ്ടിക്കുന്നത് നിങ്ങൾ പഠിക്കും.

## ⚙️ മുൻകൂർ ആവശ്യകതകളും സജ്ജീകരണവും

**വികസന പരിസ്ഥിതി:**
- .NET 9.0 SDK അല്ലെങ്കിൽ അതിനുമുകളിൽ
- Visual Studio 2022 അല്ലെങ്കിൽ C# എക്സ്റ്റെൻഷൻ ഉള്ള VS കോഡ്
- ആസ്യൂർ ഓപ്പൺഎഐ റിസോഴ്‌സും മോഡൽ ഡിപ്പ്ലോയ്മെൻറും ഉള്ള ആസ്യൂർ സബ്സ്ക്രിപ്ഷൻ
- ആസ്യൂർ CLI — `az login` ഉപയോഗിച്ച് സൈൻ ഇൻ ചെയ്യുക

**ആവശ്യപ്പെട്ടിട്ടുള്ള ഡിപ്പൻഡൻസികൾ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**പരിസ്ഥിതി ക്രമീകരണം (.env ഫയൽ):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## കോഡ് പ്രവർത്തിപ്പിക്കൽ

ഈ പാഠത്തിൽ .NET സിംഗിൾ ഫയൽ ആപ്പ് സ്ഥാപനം ഉൾപ്പെടുത്തിയിട്ടുണ്ട്. ഇത് പ്രവർത്തിപ്പിക്കാൻ:

```bash
# ഫയല്‍ എക്സിക്യൂട്ടബിൾ ആക്കുക (ലിനക്സും മാക് ഓഎസും)
chmod +x 07-dotnet-agent-framework.cs

# ആപ്ലിക്കേഷൻ റൺ ചെയ്യുക
./07-dotnet-agent-framework.cs
```

അല്ലെങ്കിൽ dotnet run കമാൻഡ് ഉപയോഗിക്കുക:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## കോഡ് പൂർവ്വംഘടന

പൂർണപരിഭാഷ `07-dotnet-agent-framework.cs` ൽ ലഭ്യമാണ്, ഇത് താഴെ വ്യക്തമാക്കുന്നു:

- DotNetEnv ഉപയോഗിച്ച് പരിസ്ഥിതി ക്രമീകരണം ലോഡ് ചെയ്യുന്നത്
- Azure OpenAI ക്ലയിന്റും `GetChatClient().AsAIAgent()` ഉപയോഗിച്ച് AI ഏജന്റ് നിർമ്മാണം
- JSON സീരിയലൈസേഷൻ ഉപയോഗിച്ച് ഘടനയിട്ട ഡാറ്റ മോഡലുകൾ (Plan, TravelPlan) നിർവചിക്കൽ
- JSON സ്കീമ ഉപയോഗിച്ച് ഘടനയിട്ട ഔട്ട്‌പുട്ട് ഉള്ള AI ഏജന്റ് സൃഷ്ടിക്കൽ
- തരം-സുരക്ഷിതレスപോൺസുകളോടൊപ്പം പ്ലാനിംഗ് അഭ്യർത്ഥനകൾ നടപ്പിലാക്കൽ

## പ്രധാന ആശയങ്ങൾ

### തരം-സുരക്ഷിത മോഡലുകളുള്ള ഘടനാപരമായ പ്ലാനിംഗ്

പ്ലാനിംഗ്_output സ്‌ട്രക്ചർ നിർവചിക്കാൻ ഏജന്റ് C# ക്ലാസുകൾ ഉപയോഗിക്കുന്നു:

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

### ഘടനാപരമായ ഔട്ട്‌പുട്ടുകൾക്കുള്ള JSON സ്കീമ

ഏജന്റ് ആസൂത്രണレスപോൺസുകൾ TravelPlan സ്കീമ തെരെഞ്ഞെടുക്കുന്നതിനായി ക്രമീകരിച്ചിരിക്കുന്നു:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### പ്ലാനിംഗ് ഏജന്റ് നിർദ്ദേശങ്ങൾ

ഏജന്റ് കോഓർഡിനേറ്ററായാണ് പ്രവർത്തിക്കുന്നത്, വിദഗ്ധ ഉപ ഏജന്റുകൾക്ക് പണികൾ നിയോഗിക്കുന്നു:

- FlightBooking: വിമാനബുക്കിങ് ചെയ്യാനും വിമാന വിവരങ്ങൾ നൽകാനും
- HotelBooking: ഹോട്ടൽ ബുക്കിങ് ചെയ്യാനും ഹോട്ടൽ വിവരങ്ങൾ നൽകാനും
- CarRental: കാർ വാടകയ്ക്ക് നൽകാനും കാർ വാടക വിവരങ്ങൾ നൽകാനും
- ActivitiesBooking: പ്രവർത്തനങ്ങൾ ബുക്ക് ചെയ്യാനും പ്രവർത്തന വിവരങ്ങൾ നൽകാനും
- DestinationInfo: ലക്ഷ്യസ്ഥലങ്ങളുടെ വിവരങ്ങൾ നൽകാനായി
- DefaultAgent: പൊതുവായ അഭ്യർത്ഥന കൈകാര്യം ചെയ്യാനായി

## പ്രതീക്ഷിക്കാവുന്ന ഔട്ട്‌പുട്ട്

യാത്രാ പദ്ധതിയിടൽ അഭ്യർത്ഥനയുമായി ഏജന്റ് പ്രവർത്തിപ്പിക്കുമ്പോൾ, ഇത് അഭ്യർത്ഥന വിശകലനം ചെയ്ത് പ്രത്യേക ഏജന്റുകളിലേക്ക് അനുയോജ്യമായ പ്രവൃത്തി നിയോഗങ്ങളോടെ ഘടനാപരമായ പദ്ധതി സൃഷ്ടിക്കും, JSON ആകൃതിയിൽ TravelPlan സ്കീമ അനുസരിച്ച് ഫോർമാറ്റ് ചെയ്യും.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->