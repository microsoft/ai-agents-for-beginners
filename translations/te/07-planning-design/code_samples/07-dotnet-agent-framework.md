# 🎯 Azure OpenAI (Responses API) ( .NET) తో యోజన & డిజైన్ నమూనాలు  

## 📋 నేర్చుకునే లక్ష్యాలు  

ఈ నోట్‌బుక్ Microsoft Agent Framework ను .NET లో Azure OpenAI (Responses API) తో ఉపయోగించి తెలివైన ఏజెంట్లను నిర్మించేందుకు ఎంటర్ప్రైజ్-గ్రేడ్ యోజన మరియు డిజైన్ నమూనాలను చూపిస్తుంది. మీరు సాంక్లిష్ట సమస్యలను విభజించే, బహుళ దశల పరిష్కారాలను యోజించే, .NET యొక్క ఎంటర్ప్రైజ్ ఫీచర్లతో అభివృద్ధి చెందిన వర్క్‌ఫ్లోలను నిర్వర్తించే ఏజెంట్లను సృష్టించడం నేర్చుకుంటారు.  

## ⚙️ ముందు అవసరాలు & సెటప్  

**డెవలప్మెంట్ వాతావరణం:**  
- .NET 9.0 SDK లేదా అంతకంటే ఎక్కువ  
- Visual Studio 2022 లేదా C# ఎక్స్‌టెన్షన్‌తో VS Code  
- Azure OpenAI వనరు మరియు మోడల్ డిప్లాయ్మెంట్ ఉన్న Azure సబ్‌స్క్రిప్షన్  
- Azure CLI — `az login` తో సైన్ ఇన్ అవ్వండి  

**అవసరమైన డిపెండెన్సీలు:**  
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```
  
**పరిసరాల కాన్ఫిగరేషన్ (.env ఫైల్):**  
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```
  
## కోడ్ నడిపించడం  

ఈ పాఠం .NET సింగిల్ ఫైల్ యాప్ అమలును కలిగి ఉంది. దీనిని నడిపించేందుకు:  

```bash
# ఫైల్‌ను అమలు చేయదగిన విధంగా చేయండి (లినక్స్/మ్యాక్‌ఓఎస్)
chmod +x 07-dotnet-agent-framework.cs

# అప్లికేషన్‌ను నడపండి
./07-dotnet-agent-framework.cs
```
  
లేకపోతే dotnet run కమాండ్ను ఉపయోగించండి:  

```bash
dotnet run 07-dotnet-agent-framework.cs
```
  
## కోడ్ అమలు  

పూర్తి అమలును `07-dotnet-agent-framework.cs` లో చూడవచ్చు, ఇది చూపిస్తుంది:  

- DotNetEnv తో పరిసరాల కాన్ఫిగరేషన్ లోడ్ చేయడం  
- Azure OpenAI క్లయింట్ సెటప్ చేసి `GetChatClient().AsAIAgent()` ఉపయోగించి AI ఏజెంట్ సృష్టించడం  
- JSON సీరియలైజేషన్‌తో నిర్మిత డేటా నమూనాలు (Plan మరియు TravelPlan) నిర్వచించడం  
- JSON స్కీమాతో నిర్మిత అవుట్పుట్ కలిగిన AI ఏజెంట్ సృష్టించడం  
- టైప్-సురక్షిత స్పందనలతో యోజన అభ్యర్థనలను నిర్వహించడం  

## ముఖ్య ఆలోచనలు  

### టైప్-సురక్షిత నమూనాల‌తో నిర్మిత యోజన  

ఏజెంట్ C# తరగతులను ఉపయోగించి యోజన అవుట్పుట్ల నిర్మాణాన్ని నిర్వచిస్తుంది:  

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
  
### నిర్మిత అవుట్పుట్‌లకు JSON స్కీమా  

ఏజెంట్ TravelPlan స్కీమాను అనుసరించునట్టుగా స్పందనలు తిరిగి ఇవ్వడానికి సెటప్ చేయబడింది:  

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
  
### యోజన ఏజెంట్ సూచనలు  

ఏజెంట్ ఓ కోఆర్డినేటర్ వలె పనిచేసి, ప్రత్యేక సబ్-ఏజెంట్లకు పనులు అప్పగిస్తుంది:  

- FlightBooking: విమాన బుకింగ్ మరియు విమాన సమాచారానికీ  
- HotelBooking: హోటల్ బుకింగ్ మరియు హోటల్ సమాచారానికీ  
- CarRental: కారు బుకింగ్ మరియు కారు రెంటల్ సమాచారానికీ  
- ActivitiesBooking: కార్యకలాపాలు బుకింగ్ మరియు సమాచారానికీ  
- DestinationInfo: గమ్యస్థలాల సమాచారం అందించటానికి  
- DefaultAgent: సాధారణ అభ్యర్థనలను నిర్వహించడానికి  

## ఎదురుచూసే అవుట్పుట్  

మీరు యోజన అభ్యర్థనతో ఏజెంట్ నడిపిస్తే, అది అభ్యర్థనను విశ్లేషించి, ప్రత్యేక ఏజెంట్లకు పనులను కేటాయిస్తూ, TravelPlan స్కీమాకు అనుగుణంగా JSON రూపంలో నిర్మిత యోజనను సృష్టిస్తుంది.  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->