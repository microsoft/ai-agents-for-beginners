# 🎯 ការធ្វើផែនការ និងគំរូរចនាសម្ព័ន្ធជាមួយ Azure OpenAI (Responses API) (.NET)

## 📋 គោលបំណងការសិក្សា

កំណត់ត្រានេះបង្ហាញពីការធ្វើផែនការ និងគំរូរចនាសម្ព័ន្ធកម្រិតស្ថាប័នសម្រាប់ការបង្កើតភ្នាក់ងារពីរូបិយបច្ចេកទេសប្រាជ្ញា ធ្វើការជាមួយ Microsoft Agent Framework ក្នុង .NET ដោយប្រើ Azure OpenAI (Responses API)។ អ្នកនឹងរៀនរបៀបបង្កើតភ្នាក់ងារដែលអាចបំបែកបញ្ហាស្មុគស្មាញ, រៀបចំដំណោះស្រាយច្រើនជំហាន, និងអនុវត្តស្វ័យប្រវត្តិកម្មស្មុគស្មាញជាមួយមុខងារស្ថាប័នរបស់ .NET។

## ⚙️ តម្រូវការមុន & ការដំឡើង

**បរិយាកាសអភិវឌ្ឍន៍៖**
- .NET 9.0 SDK ឬខ្ពស់ជាង
- Visual Studio 2022 ឬ VS Code ជាមួយជំនួយការ C#
- ការជាវ Azure ដែលមានធនធាន Azure OpenAI និងការចែកចាយម៉ូដែល
- Azure CLI — អ្នកត្រូវចូលប្រើជាមួយ `az login`

**ការទាមទារចាំបាច់៖**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ការកំណត់បរិយាកាស (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## វិធីសាស្ត្ររត់កូដ

មេរៀននេះរួមមានការអនុវត្តកម្មវិធី .NET Single File App។ ដើម្បីរត់វា៖

```bash
# ប្រែឯកសារឱ្យអាចប្រតិបត្តិបាន (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# រត់កម្មវិធី
./07-dotnet-agent-framework.cs
```

រឺប្រើពាក្យបញ្ជា dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## ការអនុវត្តកូដ

ការអនុវត្តពេញលេញមាននៅក្នុង `07-dotnet-agent-framework.cs` ដែលបង្ហាញពី៖

- ការបញ្ចូលការកំណត់បរិយាកាសជាមួយ DotNetEnv
- ការកំណត់អតិថិជន Azure OpenAI សម្រាប់ Responses API
- ការកំណត់ម៉ូដែលទិន្នន័យរចនាសម្ព័ន្ធ (Plan និង TravelPlan) ជាមួយការបម្លែង JSON
- បង្កើតភ្នាក់ងារ AI ជាមួយលទ្ធផលរចនាសម្ព័ន្ធដោយប្រើ JSON schema
- អនុវត្តសំណើរការធ្វើផែនការជាមួយការឆ្លើយតបប្រភេទសុវត្ថិភាព

## គំនិតសំខាន់ៗ

### ការធ្វើផែនការដោយរចនាសម្ព័ន្ធជាមួយម៉ូដែលប្រភេទសុវត្ថិភាព

ភ្នាក់ងារប្រើថ្នាក់ C# ដើម្បីកំណត់រចនាសម្ព័ន្ធលទ្ធផលធ្វើផែនការ៖

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

### JSON Schema សម្រាប់លទ្ធផលរចនាសម្ព័ន្ធ

ភ្នាក់ងារត្រូវបានកំណត់ឲ្យតបស្នងជាមួយនឹង TravelPlan schema៖

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

### សេចក្តីណែនាំភ្នាក់ងារធ្វើផែនការ

ភ្នាក់ងារនេះដើរតួជាអ្នកចោលក្នុងការបែងចែកភារកិច្ចទៅភ្នាក់ងារជំនាញ៖

- FlightBooking៖ សម្រាប់ការកក់សំបុត្រហោះហើរ និងផ្តល់ព័ត៌មានហោះហើរ
- HotelBooking៖ សម្រាប់ការកក់សណ្ឋាគារ និងផ្តល់ព័ត៌មានសណ្ឋាគារ
- CarRental៖ សម្រាប់ការកក់រថយន្ត និងផ្តល់ព័ត៌មានជួលរថយន្ត
- ActivitiesBooking៖ សម្រាប់ការកក់សកម្មភាព និងផ្តល់ព័ត៌មានសកម្មភាព
- DestinationInfo៖ សម្រាប់ផ្តល់ព័ត៌មានអំពីគោលដៅ
- DefaultAgent៖ សម្រាប់រដ្ឋបាលសំណើទូទៅ

## លទ្ធផលដែលរំពឹងទុក

នៅពេលអ្នកដំណើរការភ្នាក់ងារជាមួយសំណើរការធ្វើផែនដំណើរ វានឹងវិភាគសំណើ និងបង្កើតផែនការរចនាសម្ព័ន្ធជាមួយការបែងចែកភារកិច្ចដល់ភ្នាក់ងារជំនាញ ដោយរៀបចំទ្រង់ទ្រាយជា JSON ដែលសម្របសម្រួលទៅនឹង TravelPlan schema។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->