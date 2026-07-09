# 🎯 Azure OpenAI (Responses API)తో ప్లానింగ్ & డిజైన్ ప్యాటర్న్లు (.NET)

## 📋 నేర్చుకునే లక్ష్యాలు

ఈ నోట్బుక్ మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్‌ను .NET తో Azure OpenAI (Responses API) ఉపయోగించి ఇంటెలిజెంట్ ఏజెంట్లను నిర్మించేందుకు సంస్థ స్థాయి ప్లానింగ్ మరియు డిజైన్ ప్యాటర్న్లను చూపిస్తుంది. మీరు సంక్లిష్ట సమస్యలను విభజించి, బహుళమైన దశల పరిష్కారాలను ప్లాన్ చేసి, .NET యొక్క సంస్థ లక్షణాలతో సంక్లిష్ట వర్క్‌ఫ్లోలను అమలు చేసే ఏజెంట్లను సృష్టించడం నేర్చుకుంటారు.

## ⚙️ ముందస్తు అవసరాలు & సెటప్

**డెవలప్మెంట్ పరిసరాలు:**
- .NET 9.0 SDK లేదా అంతకన్నా ఎక్కువ
- Visual Studio 2022 లేదా C# విస్తరణతో VS Code
- Azure OpenAI రిసోర్స్ తో Azure సబ్‌స్క్రిప్షన్ మరియు మోడల్ డిప్లాయ్‌మెంట్
- Azure CLI — `az login` తో సైన్ ఇన్ కావడం

**అవసరమైన డిపెండెన్సీలు:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**పరిసర నిర్మాణం (.env ఫైల్):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## కోడ్ నడిపించటం

ఈ పాఠం ఒక .NET సింగిల్ ఫైల్ యాప్ అమలు కలిగి ఉంది. దాన్ని నడపడానికి:

```bash
# ఫైల్ ను అమలు చేయగలిగేలా మార్చండి (లినక్స్/మ్యాక్‌ఒఎస్)
chmod +x 07-dotnet-agent-framework.cs

# అప్లికేషన్‌ను 실행ించండి
./07-dotnet-agent-framework.cs
```

లేకుండా dotnet run క‌మాండ్ వాడండి:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## కోడ్ అమలు

సంపూర్ణ అమలు `07-dotnet-agent-framework.cs`లో అందుబాటులో ఉంటుంది, ఇది ఈ క్రింద చూపిస్తుంది:

- DotNetEnv తో పరిసర నిర్మాణం లోడ్ చేయడం
- Responses API కోసం Azure OpenAI క్లయింట్‌ను కాన్ఫిగర్ చేయడం
- JSON సీరియలైజేషన్‌తో గঠిత డేటా మోడల్స్ (Plan మరియు TravelPlan) నిర్వచించడం
- JSON స్కీమాతో గঠిత అవుట్‌పుట్ కలిగిన AI ఏజెంట్‌ను సృష్టించడం
- టైప్-సేఫ్ ప్రతిస్పందనలతో ప్లానింగ్ అభ్యర్థనలను అమలు చేయడం

## ముఖ్యమైన భావనలు

### టైప్-సేఫ్ మోడల్స్‌తో గঠిత ప్లానింగ్

ఈ ఏజెంట్ ప్లానింగ్ ఔట్‌పుట్‌ల నిర్మాణాన్ని నిర్వచించడానికి C# తరగతులను ఉపయోగిస్తుంది:

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

### గథిత అవుట్‌పుట్‌ల కోసం JSON స్కీਮਾ

ఏజెంట్ TravelPlan స్కీమాతో సరిపోయే ప్రతిస్పందనలను ఇవ్వటానికి కాన్ఫిగర్ చేయబడింది:

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

### ప్లానింగ్ ఏజెంట్ సూచనలు

ఏజెంట్ ఒక సమన్వయకర్తగా పనిచేస్తుంది, ప్రత్యేక కారణ ఏజెంట్లకు పనులను పంపిస్తుంది:

- FlightBooking: విమాన టికెట్లు బుక్ చేయడం మరియు విమాన సమాచారం ఇవ్వడం
- HotelBooking: హోటల్ బుకింగ్ మరియు హోటల్ సమాచారం అందించడం
- CarRental: కార్లు బుక్ చేయడం మరియు కార్ రెంటల్ సమాచారం అందించడం
- ActivitiesBooking: కార్యకలాపాలు బుక్ చేయడం మరియు సమాచారం ఇవ్వడం
- DestinationInfo: గమ్యస్థానాల గురించి సమాచారం అందించడం
- DefaultAgent: సాధారణ అభ్యర్థనల నిర్వహణ

## మరలించిన ఫలితం

ట్రావెల్ ప్లానింగ్ అభ్యర్థనతో ఏజెంట్ నడిపించినప్పుడు, అది అభ్యర్థనను విశ్లేషించి, TravelPlan స్కీమాకు అనుగుణంగా స్పెషలైజ్డ్ ఏజెంట్లకు సరైన పనుల కేటాయింపులతో కూడిన గధిత ప్లాన్‌ను రూపొందిస్తుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->