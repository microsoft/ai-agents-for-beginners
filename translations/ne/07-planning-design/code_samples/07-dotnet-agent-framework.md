# 🎯 Azure OpenAI (Responses API) सँग योजना र डिजाइन ढाँचा (.NET)

## 📋 सिकाइका उद्देश्यहरू

यो नोटबुकले Microsoft Agent Framework को .NET मा Azure OpenAI (Responses API) प्रयोग गरी बौद्धिक एजेन्टहरू निर्माण गर्नका लागि उद्यम-स्तरको योजना र डिजाइन ढाँचाहरू देखाउँछ। तपाईंले जटिल समस्याहरूलाई टुक्र्याउन सक्ने, बहु-चरण समाधान योजना बनाउन सक्ने, र .NET का उद्यम सुविधाहरूको साथ जटिल कार्यप्रवाहहरू कार्यान्वयन गर्ने एजेन्टहरू कसरी सिर्जना गर्ने सिक्नुहुन्छ।

## ⚙️ पूर्वआवश्यकता र सेटअप

** विकास वातावरण:**
- .NET 9.0 SDK वा माथि
- Visual Studio 2022 वा VS Code सँग C# एक्सटेन्सन
- Azure सदस्यता जसमा Azure OpenAI स्रोत र मोडेल डिप्लोइमेन्ट छ
- Azure CLI — `az login` सँग साइन इन गर्नुहोस्

**आवश्यक निर्भरता:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**परिवेश कन्फिगरेसन (.env फाइल):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## कोड चलाउने तरिका

यस पाठले .NET सिङ्गल फाइल एप इम्प्लिमेन्टेसन समावेश गर्दछ। यसलाई चलाउनका लागि:

```bash
# फाइललाई executable बनाउनुहोस् (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# अनुप्रयोग चलाउनुहोस्
./07-dotnet-agent-framework.cs
```

वा dotnet run कमाण्ड प्रयोग गर्नुहोस्:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## कोड इम्प्लिमेन्टेसन

सम्पूर्ण इम्प्लिमेन्टेसन `07-dotnet-agent-framework.cs` मा उपलब्ध छ, जसले देखाउँछ:

- DotNetEnv प्रयोग गरी वातावरण कन्फिगरेसन लोड गर्दै
- Azure OpenAI क्लाइंट कन्फिगर गर्दै र `GetChatClient().AsAIAgent()` प्रयोग गरी AI एजेन्ट सिर्जना गर्दै
- JSON सिरियलाइजेशनसहित संरचित डेटा मोडेलहरू (Plan र TravelPlan) परिभाषित गर्दै
- JSON स्कीमाबाट संरचित आउटपुटसहित AI एजेन्ट सिर्जना गर्दै
- प्रकार-सुरक्षित प्रतिक्रियाहरू सहित योजना अनुरोधहरू कार्यान्वयन गर्दै

## मुख्य अवधारणाहरू

### प्रकार-सुरक्षित मोडेलहरू सहित संरचित योजना

एजेन्टले योजना आउटपुटको संरचना परिभाषित गर्न C# कक्षाहरू प्रयोग गर्छ:

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

### संरचित आउटपुटका लागि JSON स्कीमा

एजेन्टलाई TravelPlan स्कीमासँग मेल खाने प्रतिक्रियाहरू फर्काउने रूपमा कन्फिगर गरिएको छ:

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

### योजना एजेन्ट निर्देशनहरू

एजेन्ट एक समन्वयकर्ता झैं काम गर्छ, जसले विशेषज्ञतापूर्वक उप-एजेन्टहरूलाई कार्यहरू सुम्पन्छ:

- FlightBooking: उडान बुकिंग र उडान जानकारीका लागि
- HotelBooking: होटेल बुकिंग र होटेल जानकारीका लागि
- CarRental: कार बुकिंग र कार भाडा जानकारीका लागि
- ActivitiesBooking: गतिविधि बुकिंग र गतिविधि जानकारीका लागि
- DestinationInfo: गन्तव्यहरू बारे जानकारी प्रदान गर्न
- DefaultAgent: सामान्य अनुरोधहरू ह्यान्डल गर्न

## अपेक्षित परिणाम

जब तपाईंले यात्रा योजना अनुरोधसहित एजेन्ट चलाउनुहुन्छ, यसले अनुरोध विश्लेषण गरेर विशेषज्ञ एजेन्टहरूलाई उपयुक्त कार्य असाइनमेन्टसहित संरचित योजना तयार पार्नेछ, जुन TravelPlan स्कीमासँग मेल खाने JSON स्वरूपमा हुनेछ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->