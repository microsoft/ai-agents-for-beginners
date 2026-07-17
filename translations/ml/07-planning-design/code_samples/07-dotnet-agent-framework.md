# 🎯 Azure OpenAI (Responses API) (.NET) ഉപയോഗിച്ച് പ്ലാനിംഗ് & ഡിസൈൻ പാറ്റേണുകൾ

## 📋 പഠന ലക്ഷ്യങ്ങൾ

ഈ നോട്ട്ബുക്ക് Microsoft Agent Framework ഉപയോഗിച്ച് .NET ൽ Azure OpenAI (Responses API) ഉപയോഗിച്ച് ബുദ്ധിമുട്ടുള്ള ഏജന്റുകൾ നിർമ്മിക്കുന്നതിനുള്ള എൻറ്റർപ്രൈസ്-ഗ്രേഡ് പ്ലാനിംഗ് & ഡിസൈൻ പാറ്റേണുകൾ കാണിക്കുന്നു. .NET-ന്റെ എൻറ്റർപ്രൈസ് ഫീച്ചറുകൾ ഉപയോഗിച്ച് സങ്കീര്‍ണ്ണമായ പ്രശ്‌നങ്ങൾ ഡീകോംപോസ് ചെയ്യാനും, മൾട്ടി-സ്റ്റെപ് പരിഹാരങ്ങൾ പ്ലാൻ ചെയ്യാനും, സങ്കീർണ്ണമായ വർക്ക്‌ഫ്ലോകൾ നിർവ്വഹിക്കാനും കഴിയുന്ന ഏജന്റുകൾ സൃഷ്ടിക്കാൻ നിങ്ങൾക്ക് പഠിക്കാം.

## ⚙️ പ്രPrerequisites & സെറ്റപ്പ്

**ഡെവലപ്പ്മെന്റ് പരിസ്ഥിതി:**
- .NET 9.0 SDK അല്ലെങ്കിൽ അതിലധികം
- Visual Studio 2022 അല്ലെങ്കിൽ C# വിപുലീകരണത്തോടെ VS Code
- Azure ഓപ്പൺഎയ്ഐ റിസോഴ്സും മോഡൽ ഡിപ്ലോയ്മെന്റും അടങ്ങിയ Azure സബ്‌സ്‌ക്രിപ്ഷൻ
- Azure CLI — `az login` ഉപയോഗിച്ച് സൈൻ ഇൻ ചെയ്യുക

**ആവശ്യമായ ഡിപ്പെൻഡൻസികൾ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**പരിസ്ഥിതി കോൺഫിഗറേഷൻ (.env ഫയൽ):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## കോഡ് റൺ ചെയ്യൽ

ഈ പാഠത്തിൽ .NET സിംഗിൾ ഫയൽ ആപ്പ് വെർക്ക്സാംപിൾ ഉൾപ്പെടുന്നു. ഇത് റൺ ചെയ്യാൻ:

```bash
# ഫയൽ എക്സിക്യൂട്ടബിൾ ആക്കുക (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# ആപ്ലിക്കേഷൻ പ്രവർത്തിപ്പിക്കുക
./07-dotnet-agent-framework.cs
```

അല്ലെങ്കിൽ dotnet run കമാൻഡ് ഉപയോഗിക്കുക:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## കോഡ് അമ്പ്ലിമെന്റേഷൻ

പൂർണ്ണ അമ്പ്ലിമെന്റേഷൻ `07-dotnet-agent-framework.cs` ൽ ലഭ്യമാണ്, ഇത് കാണിക്കുന്നു:

- DotNetEnv ഉപയോഗിച്ച് പരിസ്ഥിതി കോൺഫിഗറേഷൻ ലോഡ് ചെയ്യുക
- Azure OpenAI ക്ലയന്റ് കോൺഫിഗർ ചെയ്ത് `GetChatClient().AsAIAgent()` ഉപയോഗിച്ച് AI ഏജന്റ് സൃഷ്ടിക്കൽ
- JSON സീരിയലൈസേഷൻ ഉപയോഗിച്ച് ഘടനാപരമായ ഡാറ്റ മോഡലുകൾ (Plan & TravelPlan) നിർവചിക്കൽ
- JSON സ്കീമ ഉപയോഗിച്ചുള്ള ഘടനാപരമായ ഔട്ട്‌പുട്ട് ഉള്ള AI ഏജന്റ് സൃഷ്ടിക്കൽ
- ടൈപ്പ്-സേഫ് റസ്പോൺസുകൾ ഉപയോഗിച്ചുള്ള പ്ലാനിംഗ് അഭ്യർത്ഥനകൾ നിർവഹിക്കൽ

## പ്രധാനം ആശയങ്ങൾ

### ടൈപ്പ്-സേഫ് മോഡലുകളുമായി ഘടനാപരമായ പ്ലാനിംഗ്

ഏജന്റ് പ്ലാനിംഗ് ഔട്ട്പുട്ടുകളുടെ ഘടന നിർവചിക്കാൻ C# ക്ലാസുകൾ ഉപയോഗിക്കുന്നു:

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

### ഘടനാപരമായ ഔട്ട്പുട്ടുകൾക്കുള്ള JSON സ്കീമ

ഏജന്റ് TravelPlan സ്കീമയ്ക്ക് സമാനമായ മറുപടികൾ നൽകാൻ കോൺഫിഗർ ചെയ്യപ്പെട്ടിരിക്കുന്നു:

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

ഏജന്റ് കോーデിനേറ്ററെന്ന നിലയിൽ പ്രവർത്തിച്ച് പ്രാവീണ്യമുള്ള സബ്-ഏജന്റുകൾക്ക് ജോലികൾ ഡെലിഗേറ്റ് ചെയ്യുന്നു:

- FlightBooking: വിമാന ടിക്കറ്റ് ബുക്കിംഗ് & വിമാന വിവരങ്ങൾ നൽകുന്നു
- HotelBooking: ഹോട്ടൽ ബുക്കിംഗ് & ഹോട്ടൽ വിവരങ്ങൾ നൽകുന്നു
- CarRental: കാറുകൾ ബുക്ക് ചെയ്യൽ & കാര്‍ വാടക വിവരം നൽകുന്നു
- ActivitiesBooking: പ്രവർത്തികൾ ബുക്കിംഗ് & പ്രവർത്തി വിവരങ്ങൾ നൽകുന്നു
- DestinationInfo: ലക്ഷ്യസ്ഥലത്തെ കുറിച്ചുള്ള വിവരം നൽകുന്നു
- DefaultAgent: പൊതുവായ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യുന്നു

## പ്രതീക്ഷിച്ച ഔട്ട്‌പുട്ട്

യാത്രാപ്രവർത്തന പ്ലാനിംഗ് അഭ്യർത്ഥന നൽകി ഏജന്റ് रन ചെയ്താൽ, അഭ്യർത്ഥന വിശകലനം ചെയ്ത് TravelPlan സ്കീമയ്ക്ക് അനുയോജ്യമായ, പ്രാവീണ്യമുള്ള ഏജന്റുകൾക്ക് ജോലിയനുസൃതമായി ഫോർമാറ്റ് ചെയ്ത ഘടനാപരമായ പ്ലാൻ സൃഷ്ടിക്കും.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->