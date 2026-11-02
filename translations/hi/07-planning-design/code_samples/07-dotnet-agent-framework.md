# 🎯 Azure OpenAI (Responses API) के साथ योजना & डिज़ाइन पैटर्न (.NET)

## 📋 सीखने के उद्देश्य

यह नोटबुक Microsoft Agent Framework का उपयोग करके .NET में Azure OpenAI (Responses API) के साथ बुद्धिमान एजेंट बनाने के लिए एंटरप्राइज़-ग्रेड योजना और डिज़ाइन पैटर्न प्रदर्शित करता है। आप ऐसे एजेंट बनाने सीखेंगे जो जटिल समस्याओं को विभाजित कर सकें, बहु-चरण समाधान की योजना बना सकें, और .NET के एंटरप्राइज़ फीचर्स के साथ परिष्कृत वर्कफ़्लो निष्पादित कर सकें।

## ⚙️ पूर्वापेक्षाएँ & सेटअप

**विकास पर्यावरण:**
- .NET 9.0 SDK या उससे उच्चतर
- Visual Studio 2022 या VS Code जिसमें C# एक्सटेंशन हो
- Azure OpenAI संसाधन और मॉडल डिप्लॉयमेंट के साथ एक Azure सदस्यता
- Azure CLI — `az login` के साथ लॉगिन करें

**आवश्यक निर्भरताएँ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**पर्यावरण विन्यास (.env फाइल):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## कोड चलाना

इस पाठ में .NET सिंगल फाइल ऐप कार्यान्वयन शामिल है। इसे चलाने के लिए:

```bash
# फ़ाइल को निष्पादन योग्य बनाएं (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# आवेदन चलाएं
./07-dotnet-agent-framework.cs
```

या dotnet run कमांड का उपयोग करें:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## कोड कार्यान्वयन

पूर्ण कार्यान्वयन `07-dotnet-agent-framework.cs` में उपलब्ध है, जो निम्नलिखित प्रदर्शित करता है:

- DotNetEnv के साथ पर्यावरण विन्यास लोड करना
- Azure OpenAI क्लाइंट कॉन्फ़िगर करना और `GetChatClient().AsAIAgent()` का उपयोग कर AI एजेंट बनाना
- JSON सीरियलाइज़ेशन के साथ संरचित डेटा मॉडल (Plan और TravelPlan) परिभाषित करना
- JSON स्कीमा का उपयोग कर संरचित आउटपुट के साथ AI एजेंट बनाना
- टाइप-सेफ प्रतिक्रिया के साथ योजना अनुरोध निष्पादित करना

## मुख्य अवधारणाएँ

### टाइप-सेफ मॉडलों के साथ संरचित योजना

एजेंट योजना आउटपुट की संरचना परिभाषित करने के लिए C# क्लासेस का उपयोग करता है:

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

### संरचित आउटपुट के लिए JSON स्कीमा

एजेंट को TravelPlan स्कीमा से मेल खाने वाले उत्तर वापस करने के लिए कॉन्फ़िगर किया गया है:

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

### योजना एजेंट निर्देश

एजेंट एक समन्वयक के रूप में कार्य करता है, जो विशिष्ट उप-एजेंट्स को कार्य सौंपता है:

- FlightBooking: उड़ान बुकिंग और उड़ान जानकारी प्रदान करने के लिए
- HotelBooking: होटल बुकिंग और होटल जानकारी प्रदान करने के लिए
- CarRental: कार बुकिंग और कार किराए की जानकारी प्रदान करने के लिए
- ActivitiesBooking: गतिविधियों को बुक करने और गतिविधि जानकारी प्रदान करने के लिए
- DestinationInfo: गंतव्य के बारे में जानकारी प्रदान करने के लिए
- DefaultAgent: सामान्य अनुरोधों को संभालने के लिए

## अपेक्षित आउटपुट

जब आप एजेंट को यात्रा योजना अनुरोध के साथ चलाएंगे, तो यह अनुरोध का विश्लेषण करेगा और उपयुक्त कार्य असाइनमेंट के साथ एक संरचित योजना तैयार करेगा, जो TravelPlan स्कीमा के अनुसार JSON में स्वरूपित होगी।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->