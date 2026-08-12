# 🎯 Azure OpenAI (Responses API) सह नियोजन आणि डिझाइन पॅटर्न (.NET)

## 📋 शिकण्याचे उद्दिष्टे

हा नोटबुक Microsoft Agent Framework सह .NET मध्ये Azure OpenAI (Responses API) वापरून बुद्धिमान एजंट तयार करण्यासाठी एंटरप्राइझ-ग्रेड नियोजन आणि डिझाइन पॅटर्न दाखवतो. तुम्ही जटिल समस्या विघटित करू शकणारे, अनेक टप्प्यांच्या उपाययोजना आखू शकणारे, आणि .NET च्या एंटरप्राइझ वैशिष्ट्यांसह प्रगत कार्यप्रवाह पार पडणारे एजंट कसे तयार करायचे ते शिकाल.

## ⚙️ आवश्यक तयारी आणि सेटअप

**विकास पर्यावरण:**
- .NET 9.0 SDK किंवा त्याहून अधिक
- Visual Studio 2022 किंवा C# विस्तारासह VS Code
- Azure OpenAI स्रोत आणि मॉडेल डिप्लॉयमेंटसह Azure सदस्यता
- Azure CLI — `az login` सह साइन इन करा

**आवश्यक अवलंबित्वे:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**पर्यावरण कॉन्फिगरेशन (.env फाइल):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## कोड चालविणे

या धड्यात .NET सिंगल फाइल अॅप अंमलबजावणी समाविष्ट आहे. ते चालविण्यासाठी:

```bash
# फाइल executable करा (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# ऍप्लिकेशन चालवा
./07-dotnet-agent-framework.cs
```

किंवा dotnet run आदेश वापरा:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## कोड अंमलबजावणी

संपूर्ण अंमलबजावणी `07-dotnet-agent-framework.cs` मध्ये उपलब्ध आहे, जे दाखवते:

- DotNetEnv सह पर्यावरण कॉन्फिगरेशन लोड करणे
- Azure OpenAI क्लायंट कॉन्फिगर करणे आणि `GetChatClient().AsAIAgent()` वापरून AI एजंट तयार करणे
- JSON serialization सह संरचित डेटा मॉडेल्स (Plan आणि TravelPlan) परिभाषित करणे
- JSON स्कीमा वापरून संरचित आउटपुटसह AI एजंट तयार करणे
- प्रकार-सुरक्षित प्रतिसादांसह नियोजन विनंत्या पार पाडणे

## मुख्य संकल्पना

### प्रकार-सुरक्षित मॉडेल्ससह संरचित नियोजन

एजंट नियोजन आउटपुट्सचा स्ट्रक्चर परिभाषित करण्यासाठी C# क्लासेस वापरतो:

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

### संरचित आउटपुटसाठी JSON स्कीमा

एजंट TravelPlan स्कीमाशी सुसंगत उत्तर देण्यासाठी कॉन्फिगर केला गेला आहे:

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

### नियोजन एजंट निर्देश

एजंट एक समन्वयक म्हणून कार्य करतो, खासगी उप-एजंट्सना कार्य सौपतो:

- FlightBooking: फ्लाइट बुकिंगसाठी आणि फ्लाइट माहिती पुरवण्यासाठी
- HotelBooking: हॉटेल बुकिंगसाठी आणि हॉटेल माहिती पुरवण्यासाठी
- CarRental: कार भाड्याने देण्यासाठी आणि कार भाडे माहिती पुरवण्यासाठी
- ActivitiesBooking: क्रियाकलाप बुकिंगसाठी आणि क्रियाकलाप माहिती पुरवण्यासाठी
- DestinationInfo: ठिकाणांची माहिती पुरवण्यासाठी
- DefaultAgent: सर्वसाधारण विनंत्यांना हाताळण्यासाठी

## अपेक्षित आउटपुट

जेव्हा तुम्ही प्रवास नियोजन विनंती सह एजंट चालवाल, तेव्हा तो विनंतीचे विश्लेषण करून योग्य कार्यांची विशेष एजंट्सना नेमणूक करणारा संरचित योजना तयार करेल, जी TravelPlan स्कीमाशी सुसंगत JSON स्वरूपात असेल.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->