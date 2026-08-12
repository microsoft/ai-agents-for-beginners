[![কিভাবে ভাল AI এজেন্ট ডিজাইন করবেন](../../../translated_images/bn/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(এই পাঠের ভিডিও দেখতে উপরের ছবিতে ক্লিক করুন)_

# টুল ব্যবহার ডিজাইন প্যাটার্ন

টুলগুলি আকর্ষণীয় কারণ এগুলো AI এজেন্টদের একটি বিস্তৃত ক্ষমতার পরিসর দেয়। এজেন্টের একটি সীমিত কর্মের সেট থাকার পরিবর্তে, একটি টুল যোগ করার মাধ্যমে, এজেন্ট এখন অনেক ধরণের কর্ম সম্পাদন করতে পারে। এই অধ্যায়ে, আমরা টুল ব্যবহার ডিজাইন প্যাটার্নটি দেখব, যা বর্ণনা করে কিভাবে AI এজেন্টরা নির্দিষ্ট টুলগুলি ব্যবহার করে তাদের লক্ষ্য অর্জন করতে পারে।

## পরিচিতি

এই পাঠে, আমরা নিম্নলিখিত প্রশ্নগুলোর উত্তর খুঁজতে যাচ্ছি:

- টুল ব্যবহার ডিজাইন প্যাটার্ন কী?
- কোন কোন ব্যবহারের ক্ষেত্রে এটি প্রয়োগ করা যেতে পারে?
- ডিজাইন প্যাটার্নটি বাস্তবায়নের জন্য কী উপাদান/নির্মাণ ব্লক প্রয়োজন?
- বিশ্বাসযোগ্য AI এজেন্ট নির্মাণে টুল ব্যবহার ডিজাইন প্যাটার্ন ব্যবহারের বিশেষ বিবেচ্য বিষয়গুলি কী কী?

## শেখার লক্ষ্যসমূহ

এই পাঠ শেষ করার পর আপনি সক্ষম হবেন:

- টুল ব্যবহার ডিজাইন প্যাটার্ন ও এর উদ্দেশ্য সংজ্ঞায়িত করতে।
- যেখানে টুল ব্যবহার ডিজাইন প্যাটার্ন প্রযোজ্য সেসব ব্যবহারের দৃষ্টান্ত চিহ্নিত করতে।
- ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় মূল উপাদানগুলো বুঝতে।
- এই ডিজাইন প্যাটার্ন ব্যবহার করে AI এজেন্টদের বিশ্বাসযোগ্যতা নিশ্চিত করার জন্য বিবেচ্য বিষয়গুলি চিনতে।

## টুল ব্যবহার ডিজাইন প্যাটার্ন কী?

**টুল ব্যবহার ডিজাইন প্যাটার্ন** LLM গুলিকে নির্দিষ্ট লক্ষ্য অর্জনের জন্য বাহ্যিক টুলগুলির সাথে ইন্টারঅ্যাক্ট করার ক্ষমতা দেয়ার ওপর কেন্দ্রীভূত। টুলগুলি কোড যা একটি এজেন্ট দ্বারা কার্য সম্পাদনের জন্য চালানো যেতে পারে। একটি টুল হতে পারে একটি সহজ ফাংশন যেমন ক্যালকুলেটর, অথবা তৃতীয় পক্ষের সেবার API কল যেমন স্টক প্রাইস লুকআপ বা আবহাওয়া পূর্বাভাস। AI এজেন্টের প্রেক্ষাপটে, টুলগুলো এজেন্ট দ্বারা **মডেল-উৎপন্ন ফাংশন কল** এর প্রতিক্রিয়ায় চালনা করার জন্য ডিজাইন করা হয়েছে।

## কোন কোন ব্যবহারের ক্ষেত্রে এটি প্রয়োগ করা যেতে পারে?

AI এজেন্টরা টুল ব্যবহার করে জটিল কাজ সম্পন্ন করতে পারে, তথ্য উদ্ধার করতে পারে, বা সিদ্ধান্ত নিতে পারে। টুল ব্যবহার ডিজাইন প্যাটার্নটি সাধারণত সেইসব পরিস্থিতিতে ব্যবহৃত হয় যেখানে বাহ্যিক সিস্টেম যেমন ডাটাবেস, ওয়েব সার্ভিস বা কোড ইন্টারপ্রেটারের সাথে গতিশীলভাবে ইন্টারঅ্যাক্ট করতে হয়। এই ক্ষমতা বিভিন্ন ব্যবহারের ক্ষেত্রে উপকারী, যেমন:

- **গতিশীল তথ্য উদ্ধার:** এজেন্টরা বাহ্যিক API বা ডাটাবেস থেকে আপ-টু-ডেট ডেটা সংগ্রহ করতে পারে (যেমন, SQLite ডাটাবেস থেকে তথ্য অনুসন্ধান, স্টক প্রাইস বা আবহাওয়া তথ্য প্রাপ্তি)।
- **কোড কার্যকরকরণ ও ব্যাখ্যা:** এজেন্টরা কোড অথবা স্ক্রিপ্ট কার্যকর করে গাণিতিক সমস্যা সমাধান, প্রতিবেদন তৈরি বা সিমুলেশন করতে পারে।
- **কর্মপ্রবাহ স্বয়ংক্রিয়করণ:** টাস্ক শিডিউলার, ইমেল সার্ভিস বা ডেটা পাইপলাইন যুক্ত করে পুনরাবৃত্তি বা বহু-স্তরের কর্মপ্রবাহ স্বয়ংক্রিয় করা।
- **গ্রাহক সাপোর্ট:** এজেন্টরা CRM সিস্টেম, টিকেটিং প্ল্যাটফর্ম, বা তথ্যভান্ডারের সাথে ইন্টারঅ্যাক্ট করে ব্যবহারকারীর প্রশ্নের উত্তর দিতে পারে।
- **কন্টেন্ট তৈরি ও সম্পাদনা:** গ্রামার চেকার, টেক্সট সারাংশকরণ বা কন্টেন্ট নিরাপত্তা মূল্যায়নকারী টুল ব্যবহার করে কন্টেন্ট তৈরিতে সহায়তা।

## টুল ব্যবহার ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় উপাদান/নির্মাণ ব্লকগুলো কী কী?

এই নির্মাণ ব্লকগুলো AI এজেন্টকে বিস্তৃত কাজ করতে সক্ষম করে। চলুন টুল ব্যবহার ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় মূল উপাদানগুলো দেখি:

- **ফাংশন/টুল স্কিমাস**: উপলব্ধ টুলসমূহের বিস্তারিত সংজ্ঞা, যার মধ্যে ফাংশনের নাম, উদ্দেশ্য, প্রয়োজনীয় প্যারামিটার, এবং প্রত্যাশিত আউটপুট রয়েছে। এই স্কিমাসগুলো LLM-কে উপলব্ধ টুলগুলো বুঝতে এবং সঠিক অনুরোধ গঠন করতে সক্ষম করে।

- **ফাংশন কার্যকরকরণ লজিক**: ব্যবহারকারীর উদ্দেশ্য ও কথোপকথনের প্রেক্ষাপটে কবে ও কীভাবে টুলগুলো চালানো হবে তা নিয়ন্ত্রণ করে। এর মধ্যে পরিকল্পনাকারী মডিউল, রাউটিং ব্যবস্থা, অথবা শর্তাধীন প্রবাহ থাকতে পারে যা টুল ব্যবহারের গতি নির্ধারণ করে।

- **মেসেজ হ্যান্ডলিং সিস্টেম**: ব্যবহারকারীর ইনপুট, LLM প্রতিক্রিয়া, টুল কল এবং টুল আউটপুটের মধ্যে কথোপকথনের প্রবাহ পরিচালনা করে এমন উপাদান।

- **টুল ইন্টিগ্রেশন ফ্রেমওয়ার্ক**: এজেন্টকে বিভিন্ন টুলের সাথে সংযুক্ত করে এমন অবকাঠামো, যে টুলগুলো সহজ ফাংশন কিংবা জটিল বাহ্যিক সেবা হতে পারে।

- **ত্রুটি হ্যান্ডলিং ও যাচাই**: টুল কার্যকরকরণে ব্যর্থতা পরিচালনা, প্যারামিটার যাচাই, এবং অপ্রত্যাশিত প্রতিক্রিয়া ব্যবস্থাপনার প্রক্রিয়া।

- **স্টেট ম্যানেজমেন্ট**: কথোপকথনের প্রেক্ষাপট, পূর্ববর্তী টুল সংযোগ এবং স্থায়ী তথ্য ট্র্যাক করে যাতে বহুবার কথোপকথনে ধারাবাহিকতা থাকে।

এবার, চলুন ফাংশন/টুল কলিং-কে বিস্তারিতভাবে দেখি।
 
### ফাংশন/টুল কলিং

ফাংশন কলিং হল বড় ভাষা মডেল (LLM) গুলিকে টুলের সাথে ইন্টারঅ্যাক্ট করার প্রাথমিক পদ্ধতি। আপনি প্রায়ই 'ফাংশন' ও 'টুল' শব্দগুলো বিনিময়যোগ্যভাবে শুনবেন কারণ 'ফাংশন' (পুনরায় ব্যবহারযোগ্য কোড ব্লক) হচ্ছে এজেন্টদের কাজ সম্পাদনের জন্য ব্যবহৃত 'টুল'। একটি ফাংশনের কোড চালানোর জন্য, LLM-কে ব্যবহারকারীর অনুরোধকে ফাংশনের বিবরণের সাথে মিলিয়ে দেখতে হবে। এর জন্য একটি স্কিমা যা সমস্ত উপলব্ধ ফাংশনের বিবরণ রয়েছে, সেটা LLM-কে পাঠানো হয়। এরপর LLM সবচেয়ে উপযুক্ত ফাংশন নির্বাচন করে তার নাম ও আর্গুমেন্ট ফেরত দেয়। নির্বাচিত ফাংশনটি চালু করা হয়, তার প্রতিক্রিয়া LLM-কে পাঠানো হয়, যেটি তথ্য ব্যবহার করে ব্যবহারকারীর অনুরোধের উত্তর প্রদান করে।

ডেভেলপারদের জন্য এজেন্টদের ফাংশন কলিং বাস্তবায়নের জন্য যা প্রয়োজন:

1. ফাংশন কলিং সমর্থনকারী একটি LLM মডেল
2. ফাংশন বিবরণসহ একটি স্কিমা
3. প্রতিটি বর্ণিত ফাংশনের জন্য কোড

একটি শহরের বর্তমান সময় পাওয়ার উদাহরণ দিয়ে আসুন বুঝাই:

1. **ফাংশন কলিং সমর্থনকারী LLM ইনিশিয়ালাইজ করুন:**

    সব মডেলই ফাংশন কলিং সমর্থন করে না, তাই আপনি যে LLM ব্যবহার করছেন তা সমর্থন করে কিনা নিশ্চিত হওয়া জরুরি।     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ফাংশন কলিং সমর্থন করে। আমরা Azure OpenAI **Responses API** (স্থায়ী `/openai/v1/` এন্ডপয়েন্ট — কোন `api_version` দরকার নেই) চালু করে OpenAI ক্লায়েন্ট শুরু করতে পারি।

    ```python
    # Azure OpenAI (Responses API, v1 endpoint) এর জন্য OpenAI ক্লায়েন্ট ইনিশিয়ালাইজ করুন।
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **একটি ফাংশন স্কিমা তৈরি করুন**:

    এরপর আমরা একটি JSON স্কিমা সংজ্ঞায়িত করব, যেটিতে ফাংশনের নাম, ফাংশনের কাজের বর্ণনা, এবং ফাংশনের প্যারামিটারগুলোর নাম ও বর্ণনা থাকবে।
    আমরা এই স্কিমা নিয়ে পূর্বে তৈরি ক্লায়েন্টকে এবং ব্যবহারকারীর সান ফ্রান্সিসকোর সময় খোঁজার অনুরোধ নিয়ে দেব। যা গুরুত্বপূর্ণ তা হল, একটি **টুল কল** ফেরত আসে, প্রশ্নের চূড়ান্ত উত্তর নয়। আগেই বলা হয়েছে, LLM কাজের জন্য নির্বাচিত ফাংশনের নাম এবং তাকে পাঠানোর আর্গুমেন্ট ফেরত দেয়।

    ```python
    # মডেল পড়ার জন্য ফাংশনের বিবরণ (Responses API ফ্ল্যাট টুল ফরম্যাট)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # প্রাথমিক ব্যবহারকারীর বার্তা
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # প্রথম API কল: মডেলকে ফাংশন ব্যবহার করতে বলুন
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API response.output-এ function_call আইটেম হিসাবে টুল কলগুলি ফেরত দেয়।
    # পরবর্তী পর্যায়ে মডেলের সম্পূর্ণ প্রেক্ষাপট থাকে সেজন্য সেগুলি কথোপকথনে যোগ করুন।
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **কাজটি সম্পাদনের জন্য প্রয়োজনীয় ফাংশন কোড:**

    এখন যেহেতু LLM কোন ফাংশন চালাতে হবে তা নির্বাচন করেছে, কাজটি সম্পাদন করার কোড বাস্তবায়ন ও চালানো দরকার।
    আমরা পাইথনে বর্তমান সময় পাওয়ার কোড লিখব। এছাড়াও প্রতিক্রিয়া বার্তা থেকে নাম ও আর্গুমেন্ট বের করার কোডও লিখতে হবে যাতে চূড়ান্ত ফলাফল পাওয়া যায়।

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # ফাংশন কলগুলি পরিচালনা করুন
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # টুলের ফলাফলটি একটি function_call_output আইটেম হিসাবে ফেরত দিন
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # দ্বিতীয় API কল: মডেল থেকে চূড়ান্ত উত্তর পান
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ফাংশন কলিং অধিকাংশ, যদি না সব, এজেন্ট টুল ব্যবহার ডিজাইন প্যাটার্নের মূল, তবে একে স্ক্র্যাচ থেকে বাস্তবায়ন করা কখনও কখনও চ্যালেঞ্জিং হতে পারে।
আমরা শিখেছি [Lesson 2](../../../02-explore-agentic-frameworks) এজেন্টিক ফ্রেমওয়ার্ক আমাদের টুল ব্যবহার বাস্তবায়নের জন্য প্রি-বিল্ট নির্মাণ ব্লক সরবরাহ করে।
 
## Agentic Frameworks দিয়ে টুল ব্যবহার উদাহরণ

বিভিন্ন এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করে কিভাবে টুল ব্যবহার ডিজাইন প্যাটার্ন বাস্তবায়ন করা যায় তার কিছু উদাহরণ এখানে:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> একটি ওপেন-সোর্স AI ফ্রেমওয়ার্ক যা AI এজেন্ট তৈরি করে। এটি ফাংশন কলিং ব্যবহারের প্রক্রিয়াকে সহজ করে, কারণ আপনি `@tool` ডেকোরেটর দিয়ে পাইথন ফাংশন হিসেবে টুল সংজ্ঞায়িত করতে পারেন। ফ্রেমওয়ার্ক মডেল এবং আপনার কোডের মধ্যে বার্তা আদানপ্রদান পরিচালনা করে। এটি `FoundryChatClient` এর মাধ্যমে ফাইল সার্চ ও কোড ইন্টারপ্রেটারের মতো প্রি-বিল্ট টুলগুলোর অ্যাক্সেস দেয়।

নিম্নলিখিত চিত্রটি Microsoft Agent Framework-এ ফাংশন কলিং প্রক্রিয়া প্রদর্শন করে:

![function calling](../../../translated_images/bn/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework-এ, টুলগুলো ডেকোরেটেড ফাংশন হিসেবে সংজ্ঞায়িত। আমরা আগের `get_current_time` ফাংশনটিকে `@tool` ডেকোরেটর ব্যবহার করে একটি টুলে রূপান্তর করতে পারি। ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে ফাংশন ও এর প্যারামিটার সিরিয়ালাইজ করে, LLM-এ পাঠানোর জন্য স্কিমা তৈরি করে।

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ক্লায়েন্ট তৈরি করুন
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# একটি এজেন্ট তৈরি করুন এবং টুলের সাথে চালান
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> একটি আধুনিক এজেন্টিক ফ্রেমওয়ার্ক যা ডেভেলপারদের নিরাপদভাবে উচ্চ-মানের, প্রসারযোগ্য AI এজেন্ট তৈরি, ডিপ্লয় ও স্কেল করতে সাহায্য করে, মূল কম্পিউট ও স্টোরেজ রিসোর্স পরিচালনার দরকার ছাড়াই। এটি বিশেষ করে এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য কার্যকর কারণ এটি সম্পূর্ণভাবে ব্যবস্থাপিত একটি সেবা যা এন্টারপ্রাইজ স্তরের নিরাপত্তা প্রদান করে।

সরাসরি LLM API দিয়ে ডেভেলপমেন্টের তুলনায় Microsoft Foundry Agent Service কিছু সুবিধা দেয়, যেমন:

- স্বয়ংক্রিয় টুল কলিং – টুল কল পার্স করা, টুল চালানো ও প্রতিক্রিয়া পরিচালনার প্রয়োজন নেই; সব এখন সার্ভার-সাইডে হয়
- নিরাপদে পরিচালিত তথ্য – আপনার নিজের কথোপকথন অবস্থা পরিচালনা করার পরিবর্তে, থ্রেডগুলোতে সব তথ্য সংরক্ষণ করা যায়
- তাত্ক্ষণিক টুলস – Bing, Azure AI Search, এবং Azure Functions-এর মতো ডেটা সোর্সের সাথে ইন্টারঅ্যাক্ট করার জন্য যা টুলস পাওয়া যায়

Microsoft Foundry Agent Service-এ উপলব্ধ টুলগুলো দুইটি ভাগে বিভক্ত:

1. জ্ঞান টুলস:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing সার্চ দ্বারা গ্রাউন্ডিং</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ফাইল সার্চ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI সার্চ</a>

2. এ্যাকশন টুলস:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ফাংশন কলিং</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">কোড ইন্টারপ্রেটার</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI দ্বারা সংজ্ঞায়িত টুলস</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

এজেন্ট সার্ভিস আমাদের এই টুলগুলোকে একটি `toolset` হিসাবে ব্যবহার করার সুযোগ দেয়। এটি `threads` ব্যবহার করে যা নির্দিষ্ট কথোপকথনের বার্তাগুলোর ইতিহাস ট্র্যাক করে।

ভাবুন আপনি Contoso নামে একটি কোম্পানির সেলস এজেন্ট। আপনি এমন একটি কথোপকথনমূলক এজেন্ট তৈরি করতে চান যা আপনার বিক্রয় তথ্য নিয়ে প্রশ্নের উত্তর দিতে পারে।

নীচের ছবি Microsoft Foundry Agent Service ব্যবহার করে কিভাবে আপনার বিক্রয় তথ্য বিশ্লেষণ করা যায় তা দেখায়:

![Agentic Service In Action](../../../translated_images/bn/agent-service-in-action.34fb465c9a84659e.webp)

এই টুলস যে কোনওটি ব্যবহার করতে আমরা একটি ক্লায়েন্ট তৈরি করে একটি টুল বা টুলসেট সংজ্ঞায়িত করতে পারি। আমরা নিম্নলিখিত পাইথন কোড ব্যবহার করে এটি বাস্তবায়ন করতে পারি। LLM টুলসেট দেখে ব্যবহারকারী তৈরি ফাংশন `fetch_sales_data_using_sqlite_query` ব্যবহার করবে কিনা বা প্রি-বিল্ট কোড ইন্টারপ্রেটার ব্যবহার করবে কিনা তা সিদ্ধান্ত নেবে, ব্যবহারকারীর অনুরোধের ওপর ভিত্তি করে।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ফাংশন যা fetch_sales_data_functions.py ফাইলে পাওয়া যাবে।
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# টুলসেট আরম্ভ করুন
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ফাংশন সহ ফাংশন কলিং এজেন্ট আরম্ভ করা এবং এটি টুলসেটে যোগ করা
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# কোড ইন্টারপ্রিটার টুল আরম্ভ করুন এবং এটি টুলসেটে যোগ করুন।
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## বিশ্বাসযোগ্য AI এজেন্ট নির্মাণে টুল ব্যবহার ডিজাইন প্যাটার্ন ব্যবহারের বিশেষ বিবেচনাসমূহ কী কী?

LLM দ্বারা গতিশীলভাবে তৈরি SQL-এর নিরাপত্তা নিয়ে সাধারণ উদ্বেগ থাকে, বিশেষ করে SQL ইনজেকশন বা ক্ষতিকর কাজ যেমন ডাটাবেস ড্রপ অথবা তছাড়া করার ঝুঁকি। যদিও এসব উদ্বেগ যথার্থ, সেগুলো ডাটাবেস অ্যাক্সেস পারমিশন সঠিকভাবে কনফিগার করে কার্যকরভাবে প্রতিরোধ করা যায়। বেশিরভাগ ডাটাবেসের ক্ষেত্রে এটি রিড-ওনলি কনফিগার করা জড়িত। PostgreSQL বা Azure SQL-এর মতো ডাটাবেস সেবাগুলোর জন্য, অ্যাপলিকে রিড-ওনলি (SELECT) ভূমিকায় নিয়োগ করা উচিত।

অ্যাপটি নিরাপদ পরিবেশে চালানো আরও সুরক্ষা বাড়ায়। এন্টারপ্রাইজ পরিস্থিতিতে ডেটা সাধারণত অপারেশনাল সিস্টেম থেকে রিড-ওনলি ডাটাবেস বা ডেটা ওয়্যারহাউসে রূপান্তর ও উত্তোলন করা হয়, একটি ব্যবহারকারী-বান্ধব স্কিমা সহ। এই পদ্ধতি নিশ্চিত করে ডেটা নিরাপদ, কর্মক্ষমতা ও প্রবেশযোগ্যতা উন্নত, এবং অ্যাপটি সীমিত, রিড-ওনলি অ্যাক্সেস পায়।

## নমুনা কোড

- পাইথন: [এজেন্ট ফ্রেমওয়ার্ক](./code_samples/04-python-agent-framework.ipynb)
- .NET: [এজেন্ট ফ্রেমওয়ার্ক](./code_samples/04-dotnet-agent-framework.md)

## টুল ব্যবহার ডিজাইন প্যাটার্ন নিয়ে আরও প্রশ্ন আছে?

অন্যান্য শিক্ষার্থীদের সাথে মেলামেশা করতে, অফিস আওয়ারস এ অংশ নিতে এবং AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পেতে [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) এ যোগ দিন।

## অতিরিক্ত সম্পদ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service ওয়ার্কশপ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer মাল্টি-এজেন্ট ওয়ার্কশপ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework ওভারভিউ</a>


## এই এজেন্টের স্মোক-টেস্টিং (ঐচ্ছিক)

[Lesson 16](../16-deploying-scalable-agents/README.md) এ আপনি এজেন্টগুলি কিভাবে স্থাপন করবেন তা শেখার পর, আপনি এই পাঠের `TravelToolAgent`-এর স্মোক-টেস্ট করতে পারেন (এটি এখনও কি এর টুলগুলো কল করে এবং উত্তর দেয়?) [ `tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) দিয়ে। এটি চালানোর জন্য দেখুন [`tests/README.md`](../tests/README.md)।

## পূর্ববর্তী পাঠ

[এজেন্টিক ডিজাইন প্যাটার্নগুলি বোঝা](../03-agentic-design-patterns/README.md)

## পরবর্তী পাঠ

[এজেন্টিক RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->