# 🌍 Microsoft Agent Framework (.NET) के साथ AI ट्रैवल एजेंट

## 📋 परिदृश्य का अवलोकन

यह नोटबुक Microsoft Agent Framework for .NET का उपयोग करके एक बुद्धिमान यात्रा योजना एजेंट बनाने का तरीका दिखाता है। यह एजेंट दुनिया भर के रैंडम डेस्टिनेशन के लिए व्यक्तिगत दिन-यात्रा योजनाएं स्वचालित रूप से तैयार कर सकता है।

**मुख्य क्षमताएं:**
- 🎲 **रैंडम डेस्टिनेशन चयन**: छुट्टी के स्थान चुनने के लिए कस्टम टूल का उपयोग करता है
- 🗺️ **बुद्धिमान यात्रा योजना**: विस्तृत दिन-प्रतिदिन की योजनाएं बनाता है
- 🔄 **रियल-टाइम स्ट्रीमिंग**: तत्काल और स्ट्रीमिंग प्रतिक्रियाओं का समर्थन करता है
- 🛠️ **कस्टम टूल इंटीग्रेशन**: एजेंट की क्षमताओं को बढ़ाने का तरीका दिखाता है

## 🔧 तकनीकी संरचना

### मुख्य तकनीकें
- **Microsoft Agent Framework**: AI एजेंट विकास के लिए नवीनतम .NET कार्यान्वयन
- **GitHub Models Integration**: GitHub के AI मॉडल इनफरेंस सेवा का उपयोग करता है
- **OpenAI API Compatibility**: कस्टम एंडपॉइंट्स के साथ OpenAI क्लाइंट लाइब्रेरी का लाभ उठाता है
- **सुरक्षित कॉन्फ़िगरेशन**: पर्यावरण-आधारित API कुंजी प्रबंधन

### मुख्य घटक
1. **AIAgent**: मुख्य एजेंट ऑर्केस्ट्रेटर जो बातचीत के प्रवाह को संभालता है
2. **कस्टम टूल्स**: `GetRandomDestination()` फ़ंक्शन एजेंट के लिए उपलब्ध है
3. **चैट क्लाइंट**: GitHub Models-समर्थित बातचीत इंटरफ़ेस
4. **स्ट्रीमिंग समर्थन**: रियल-टाइम प्रतिक्रिया उत्पन्न करने की क्षमता

### इंटीग्रेशन पैटर्न
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 आरंभ करना

**पूर्वापेक्षाएँ:**
- .NET 9.0 या उच्चतर
- GitHub Models API एक्सेस टोकन
- `.env` फ़ाइल में कॉन्फ़िगर किए गए पर्यावरण चर

**आवश्यक पर्यावरण चर:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

नीचे दिए गए सेल्स को क्रम में चलाएं और ट्रैवल एजेंट को क्रियान्वित होते हुए देखें!

---

## .NET Single File App: AI Travel Agent Example

See `01-dotnet-agent-framework.cs` for the complete runnable code sample.

नीचे दिए गए कोड नमूने को चलाएं:

```bash
dotnet run 01-dotnet-agent-framework.cs
```

### Sample Code

```csharp
static string GetRandomDestination()
{
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Extract configuration from environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI Client Options
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Create AI Agent with Travel Planning Capabilities
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip (Non-Streaming)
Console.WriteLine(await agent.RunAsync("Plan me a day trip"));

// Execute Agent: Plan a Day Trip (Streaming Response)
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    Console.Write(update);
}
```
