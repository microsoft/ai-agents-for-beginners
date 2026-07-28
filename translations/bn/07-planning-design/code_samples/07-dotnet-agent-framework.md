# 🎯 Azure OpenAI (Responses API) (.NET) ব্যবহার করে পরিকল্পনা এবং ডিজাইন প্যাটার্ন

## 📋 শেখার উদ্দেশ্য

এই নোটবুকটি প্রদর্শন করে কিভাবে .NET-এর Microsoft Agent Framework ব্যবহার করে Azure OpenAI (Responses API)-এর সাথে বুদ্ধিমান এজেন্ট তৈরি করার জন্য এন্টারপ্রাইজ-স্তরের পরিকল্পনা এবং ডিজাইন প্যাটার্নগুলি ব্যবহার করা যায়। আপনি শিখবেন কিভাবে জটিল সমস্যাগুলি ভাঙতে পারে এমন এজেন্ট তৈরি করতে হয়, বহু-ধাপ সমাধান পরিকল্পনা করতে হয়, এবং .NET-এর এন্টারপ্রাইজ বৈশিষ্ট্য সহ উন্নত ওয়ার্কফ্লো সম্পাদন করতে হয়।

## ⚙️ প্রয়োজনীয়তা এবং সেটআপ

**ডেভেলপমেন্ট পরিবেশ:**
- .NET 9.0 SDK বা ততোধিক
- Visual Studio 2022 অথবা C# এক্সটেনশন সহ VS Code
- Azure সাবস্ক্রিপশন সহ Azure OpenAI রিসোর্স এবং একটি মডেল ডিপ্লয়মেন্ট
- Azure CLI — `az login` দিয়ে সাইন ইন করুন

**প্রয়োজনীয় নির্ভরশীলতা:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**পরিবেশ কনফিগারেশন (.env ফাইল):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## কোড চালানো

এই পাঠে .NET সিঙ্গেল ফাইল অ্যাপ্লিকেশন বাস্তবায়ন অন্তর্ভুক্ত। এটি চালানোর জন্য:

```bash
# ফাইলটি executable করুন (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# অ্যাপ্লিকেশন রান করুন
./07-dotnet-agent-framework.cs
```

অথবা dotnet run কমান্ড ব্যবহার করুন:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## কোড বাস্তবায়ন

সম্পূর্ণ বাস্তবায়ন `07-dotnet-agent-framework.cs` ফাইলে উপলব্ধ, যা প্রদর্শন করে:

- DotNetEnv দিয়ে পরিবেশ কনফিগারেশন লোড করা
- Azure OpenAI ক্লায়েন্ট কনফিগারেশন এবং `GetChatClient().AsAIAgent()` ব্যবহার করে এআই এজেন্ট তৈরি
- JSON সিরিয়ালাইজেশনসহ কাঠামোবদ্ধ ডেটা মডেল (Plan এবং TravelPlan) সংজ্ঞায়িত করা
- JSON স্কিমা ব্যবহার করে কাঠামোবদ্ধ আউটপুট সহ একটি AI এজেন্ট তৈরি
- টাইপ-সেফ রেসপন্স সহ পরিকল্পনা অনুরোধ কার্যকর করা

## মূল ধারণাসমূহ

### টাইপ-সেফ মডেলের মাধ্যমে কাঠামোবদ্ধ পরিকল্পনা

এজেন্ট পরিকল্পনার আউটপুটের কাঠামো সংজ্ঞায়িত করতে C# ক্লাস ব্যবহার করে:

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

### কাঠামোবদ্ধ আউটপুটের জন্য JSON স্কিমা

এজেন্টটি TravelPlan স্কিমার সাথে মেলানো রেসপন্স প্রদান করার জন্য কনফিগার করা হয়েছে:

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

### পরিকল্পনা এজেন্টের ইনস্ট্রাকশন

এজেন্টটি একটি সমন্বয়কারী হিসেবে কাজ করে, বিশেষায়িত সাব-এজেন্টদের কাজ ভাগ করে দেয়:

- FlightBooking: বিমান বুকিং এবং বিমান সম্পর্কিত তথ্য প্রদান
- HotelBooking: হোটেল বুকিং এবং হোটেল সম্পর্কিত তথ্য প্রদান
- CarRental: গাড়ি বুকিং এবং গাড়ি ভাড়া তথ্য প্রদান
- ActivitiesBooking: কার্যক্রম বুকিং এবং কার্যক্রম তথ্য প্রদান
- DestinationInfo: গন্তব্য সম্পর্কে তথ্য প্রদান
- DefaultAgent: সাধারণ অনুরোধ পরিচালনা করা

## প্রত্যাশিত আউটপুট

যখন আপনি একটি ট্রাভেল প্ল্যানিং অনুরোধ দিয়ে এজেন্ট চালাবেন, এটি অনুরোধ বিশ্লেষণ করবে এবং TravelPlan স্কিমার সাথে সামঞ্জস্যপূর্ণ JSON ফরম্যাটে বিশেষায়িত এজেন্টদের জন্য উপযুক্ত টাস্ক অ্যাসাইনমেন্ট সহ একটি কাঠামোবদ্ধ পরিকল্পনা তৈরি করবে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->