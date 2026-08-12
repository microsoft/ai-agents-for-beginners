# 🎯 Azure OpenAI (Responses API) తో ప్లానింగ్ & డిజైన్ ప్యాటర్న్స్ (.NET)

## 📋 నేర్చుకునే లక్ష్యాలు

ఈ నోట్‌బుక్ Microsoft Agent Frameworkను ఉపయోగించి .NET లో Azure OpenAI (Responses API) తో తెలివైన ఏజెంట్లను రూపొందించడానికీ ఎంటర్ప్రైజ్-గ్రేడ్ ప్లానింగ్ మరియు డిజైన్ ప్యాటర్న్లను ప్రదర్శిస్తుంది. మీరు సంక్లిష్ట సమస్యలను విభజించగల, బహుళ దశల పరిష్కారాలు ప్లాన్ చేయగల మరియు .NET యొక్క ఎంటర్ప్రైజ్ ఫీచర్లతో స్మార్ట్ వర్క్‌ఫ్లోలను అమలు చేసే ఏజెంట్లను సృష్టించడం నేర్చుకుంటారు.

## ⚙️ ఆవశ్యకతలు & సెటప్

**డెవలప్‌మెంట్ పరిసరాలు:**
- .NET 9.0 SDK లేదా మించిపోయిన వెర్షన్
- Visual Studio 2022 లేదా VS Code C# ఎక్స్‌టెన్షన్ తో
- Azure OpenAI వనరు మరియు మోడల్ డిప్లాయ్‌మెంట్ తో Azure సబ్‌స్క్రిప్షన్
- Azure CLI — `az login` ద్వారా సైన్ ఇన్ చేయండి

**అవసరమైన డిపెండెన్సీలు:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**వాతావరణ కాన్ఫిగరేషన్ (.env ఫైల్):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## కోడ్ నడిపించడం

ఈ పాఠంలో .NET సింగిల్ ఫైల్ యాప్ అమలు ఉంది. దాన్ని నడపడానికి:

```bash
# ఫైల్ ను అమలు చేయదగినదిగా మార్చండి (లినక్స్/మాక్‌‌ఓఎస్)
chmod +x 07-dotnet-agent-framework.cs

# అప్లికేషన్ నడపండి
./07-dotnet-agent-framework.cs
```

లేదా డాట్‌నెట్ రన్ ఆదేశాన్ని ఉపయోగించండి:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## కోడ్ అమలు

పూర్తి అమలు `07-dotnet-agent-framework.cs` లో అందుబాటులో ఉంది, ఇది చూపిస్తుంది:

- DotNetEnv తో వాతావరణ కాన్ఫిగరేషన్ లోడ్ చేయడం
- Azure OpenAI క్లయింట్‌ను కాన్ఫిగర్ చేసి `GetChatClient().AsAIAgent()` ఉపయోగించి AI ఏజెంట్ సృష్టించడం
- JSON సీరియలైజేషన్ తో నిర్మిత డేటా మోడల్స్ (Plan మరియు TravelPlan) నిర్వచించడం
- JSON స్కీమాతో నిర్మిత అవుట్పుట్ కలిగిన AI ఏజెంట్ సృష్టించడం
- టైపు-సురక్షిత ప్రతిస్పందనలతో ప్లానింగ్ అభ్యర్థనలు అమలు చేయడం

## ముఖ్యమైన కాన్సెప్ట్లు

### టైపు-సురక్షిత మోడల్స్‌తో నిర్మిత ప్లానింగ్

ఏజెంట్ ప్లానింగ్ అవుట్పుట్‌ల నిర్మాణం నిర్వచించడానికి C# క్లాసులు ఉపయోగిస్తుంది:

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

### నిర్మిత అవుట్పుట్ల కోసం JSON స్కీమా

ఏజెంట్ TravelPlan స్కీమాతో సరిపోతున్న ప్రతిస్పందనలను తిరిగి ఇవ్వడానికి కాన్ఫిగర్ చేసినది:

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

### ప్లానింగ్ ఏజెంట్ సూచనలు

ఏజెంట్ సహకారిగా పనిచేస్తుంది, ప్రత్యేక సబ్ఆజెంట్లకు పనులను అప్పగిస్తోంది:

- FlightBooking: విమానాల బుకింగ్ మరియు విమాన సమాచారం అందించడానికి
- HotelBooking: హోటల్స్ బుకింగ్ మరియు హోటల్ సమాచారం అందించడానికి
- CarRental: కార్ల బుకింగ్ మరియు కార్ రెంటల్ సమాచారం అందించడానికి
- ActivitiesBooking: కార్యకలాపాలు బుకింగ్ మరియు సమాచారాన్ని అందించడానికి
- DestinationInfo: గమ్యస్థానాల వివరణ అందించడానికి
- DefaultAgent: సాధారణ అభ్యర్థనల నిర్వహణ కోసం

## అంచనా ఫలితం

మీరు ప్రయాణం ప్లానింగ్ అభ్యర్థనతో ఏజెంట్‌ను నడిపినప్పుడు, అది అభ్యర్థనను విశ్లేషించి, ప్రత్యేక ఏజెంట్లకు పనుల కేటాయింపుతో నిర్మితమైన ప్లాన్‌ను JSONగా TravelPlan స్కీమాను అనుసరించి రూపొందిస్తుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->