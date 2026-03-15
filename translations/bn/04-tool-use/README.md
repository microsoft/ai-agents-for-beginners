[![কিভাবে ভালো AI এজেন্ট ডিজাইন করবেন](../../../translated_images/bn/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(এই পাঠের ভিডিও দেখার জন্য উপরের ছবিতে ক্লিক করুন)_

# টুল ব্যবহার ডিজাইন প্যাটার্ন

টুলগুলো আকর্ষণীয় কারণ এগুলো AI এজেন্টদের একটি বৃহত্তর দক্ষতার পরিধি দেয়। এজেন্টের কাছে সীমিত সংখ্যক কার্যকলাপ করার ক্ষমতা থাকার পরিবর্তে, একটি টুল যুক্ত করার মাধ্যমে এজেন্ট এখন বিস্তৃত রকমের কাজ করতে পারে। এই অধ্যায়ে, আমরা টুল ব্যবহার ডিজাইন প্যাটার্ন নিয়ে আলোচনা করব, যা বর্ণনা করে কিভাবে AI এজেন্ট নির্দিষ্ট টুল ব্যবহার করে তাদের লক্ষ্যমাত্রা অর্জন করতে পারে।

## পরিচিতি

এই পাঠে, আমরা নিম্নলিখিত প্রশ্নগুলোর উত্তর দিতে চাই:

- টুল ব্যবহার ডিজাইন প্যাটার্ন কী?
- কোন ব্যবহারের ক্ষেত্রে এটি প্রয়োগ করা যায়?
- ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য দরকারী উপাদান/নির্মাণ ব্লক কী কী?
- বিশ্বাসযোগ্য AI এজেন্ট তৈরি করতে টুল ব্যবহার ডিজাইন প্যাটার্ন ব্যবহার করার বিশেষ বিবেচ্য বিষয় কী কী?

## শেখার লক্ষ্য

এই পাঠ সম্পন্ন করার পর, আপনি সক্ষম হবেন:

- টুল ব্যবহার ডিজাইন প্যাটার্ন এবং এর উদ্দেশ্য সংজ্ঞায়িত করতে।
- কোন ব্যবহারের ক্ষেত্রে টুল ব্যবহার ডিজাইন প্যাটার্ন প্রযোজ্য তা চিনতে।
- ডিজাইন প্যাটার্ন বাস্তবায়নে প্রয়োজনীয় মূল উপাদান বুঝতে।
- এই ডিজাইন প্যাটার্ন ব্যবহার করে AI এজেন্টদের বিশ্বাসযোগ্যতা নিশ্চিত করার বিবেচনা চিনতে।

## টুল ব্যবহার ডিজাইন প্যাটার্ন কী?

**টুল ব্যবহার ডিজাইন প্যাটার্ন** LLM গুলোকে নির্দিষ্ট লক্ষ্য অর্জনের জন্য বাইরের টুলগুলোর সাথে ইন্টারঅ্যাক্ট করার ক্ষমতা দেয়ার ওপর গুরুত্ব দেয়। টুল হলো এমন কোড যা কোনো এজেন্ট দ্বারা কার্যকর করা যেতে পারে কোনো কাজ সম্পন্ন করার জন্য। একটি টুল হতে পারে সহজ ফাংশন যেমন ক্যালকুলেটর, অথবা তৃতীয় পক্ষের সেবার API কল যেমন শেয়ার বাজারের মূল্য অনুসন্ধান বা আবহাওয়ার পূর্বাভাস। AI এজেন্টদের প্রেক্ষিতে, টুলগুলো মডেল-জেনারেটেড ফাংশন কল এর প্রতিক্রিয়ায় এজেন্ট দ্বারা কার্যকর করার জন্য ডিজাইন করা হয়।

## কোন ব্যবহারের ক্ষেত্রে এটি প্রয়োগ করা যায়?

AI এজেন্ট টুল ব্যবহার করে জটিল কাজ সম্পন্ন করতে, তথ্য অনুসন্ধান করতে, বা সিদ্ধান্ত নিতে পারে। টুল ব্যবহার ডিজাইন প্যাটার্ন সাধারণত এমন পরিস্থিতিতে ব্যবহৃত হয় যেখানে বাইরের সিস্টেম যেমন ডাটাবেস, ওয়েব সার্ভিস, বা কোড ইন্টারপ্রেটারের সাথে গতিশীল ইন্টারঅ্যাকশন প্রয়োজন। এর কিছু গুরুত্বপূর্ণ ব্যবহারের ক্ষেত্রে হল:

- **গতিশীল তথ্য অনুসন্ধান:** এজেন্টরা বাইরের API বা ডাটাবেস থেকে আপ-টু-ডেট তথ্য অনুসন্ধান করতে পারে (যেমন, SQLite ডাটাবেসে ডেটা বিশ্লেষণের জন্য প্রশ্ন করা, শেয়ার বাজারের দাম বা আবহাওয়া তথ্য আনা)।
- **কোড কার্যকর ও ব্যাখ্যা:** এজেন্টরা কোড বা স্ক্রিপ্ট চালিয়ে গাণিতিক সমস্যা সমাধান, প্রতিবেদন তৈরি, বা সিমুলেশন করতে পারে।
- **ওয়ার্কফ্লো স্বয়ংক্রিয়করণ:** পুনরাবৃত্তিমূলক বা বহু-ধাপের কাজ স্বয়ংক্রিয় করতে টুল যেমন টাস্ক স্কেজুলার, ইমেইল সার্ভিস, বা ডেটা পাইপলাইন ব্যবহার করা।
- **গ্রাহক সহায়তা:** এজেন্টরা CRM সিস্টেম, টিকিটিং প্ল্যাটফর্ম, বা জ্ঞানভাণ্ডারের সাথে ইন্টারঅ্যাক্ট করেও ব্যবহারকারীর প্রশ্নের সমাধান দিতে পারে।
- **বিষয়বস্তু সৃষ্টি ও সম্পাদনা:** গ্রামার চেকার, টেক্সট সারাংশকারী, বা বিষয়বস্তু সুরক্ষা মূল্যায়নকারী টুল ব্যবহার করে বিষয়বস্তু তৈরিতে সহায়তা।

## টুল ব্যবহার ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য কী উপাদান/নির্মাণ ব্লক দরকার?

এই নির্মাণ ব্লকগুলো AI এজেন্টকে বিস্তৃত কাজ করতে সহায়তা করে। আসুন টুল ব্যবহার ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রধান উপাদানগুলো দেখি:

- **ফাংশন/টুল স্কিমা:** উপলব্ধ টুলের বিস্তারিত সংজ্ঞা, যেমন ফাংশনের নাম, উদ্দেশ্য, প্রয়োজনীয় প্যারামিটার এবং প্রত্যাশিত আউটপুট। এই স্কিমাগুলো LLM কে উপলব্ধ টুলগুলো বুঝতে এবং সঠিক অনুরোধ গঠন করতে সাহায্য করে।

- **ফাংশন কার্যকরকরণের লজিক:** ব্যবহারকারীর উদ্দেশ্য ও কথোপকথনের প্রসঙ্গ অনুসারে কখন ও কিভাবে টুল ব্যবহার হবে নির্ধারণ করে। এতে পরিকল্পক মডিউল, রাউটিং ব্যবস্থাপনা, বা শর্তাধীন প্রবাহ থাকতে পারে যা গতিশীলভাবে টুল ব্যবহারের সিদ্ধান্ত নেয়।

- **বার্তা হ্যান্ডলিং সিস্টেম:** ব্যবহারকারী ইনপুট, LLM-এর প্রতিক্রিয়া, টুল কল ও টুল আউটপুটের মধ্যে কথোপকথনের প্রবাহ পরিচালনা করে।

- **টুল ইন্টিগ্রেশন ফ্রেমওয়ার্ক:** এজেন্টকে বিভিন্ন টুলের সঙ্গে সংযোগ করানোর অবকাঠামো, হোক তা সহজ ফাংশন কিংবা জটিল বাইরের সার্ভিস।

- **ত্রুটি পরিচালনা ও যাচাই:** টুল কার্যকরকরণের ব্যর্থতা পরিচালনা, প্যারামিটার যাচাই এবং অপ্রত্যাশিত প্রতিক্রিয়া পরিচালনার ব্যবস্থা।

- **স্টেট ব্যবস্থাপনা:** কথোপকথনের প্রসঙ্গ, পূর্বের টুল সহযোগিতা এবং ধ্রুপদী ডেটা ট্র্যাক করে একাধিক ধাপে ধারাবাহিকতা নিশ্চিত করে।

এরপর, আসুন ফাংশন/টুল কলিং সম্পর্কে বিস্তারিত জানি।

### ফাংশন/টুল কলিং

ফাংশন কলিং হলো LLM গুলোকে টুলের সাথে ইন্টারঅ্যাক্ট করার প্রধান উপায়। 'ফাংশন' এবং 'টুল' এই দুটি শব্দ প্রায়শই বিনিময়যোগ্য হিসেবে ব্যবহৃত হয় কারণ 'ফাংশন' (পুনঃব্যবহারযোগ্য কোড ব্লক) হলো সেই 'টুল' যেগুলো এজেন্ট কাজ সম্পন্নে ব্যবহার করে। একটি ফাংশনের কোড কল করার জন্য LLM কে ব্যবহারকারীর অনুরোধের সঙ্গে ফাংশনের বর্ণনা তুলনা করতে হয়। এজন্য একটি স্কিমা যা সব উপলব্ধ ফাংশনের বর্ণনা থাকে, তা LLM-কে পাঠানো হয়। LLM তারপর সবচেয়ে উপযুক্ত ফাংশন নির্বাচন করে তার নাম ও আর্গুমেন্ট ফেরত দেয়। নির্বাচিত ফাংশন কল করা হয়, প্রতিক্রিয়া LLM-কে পাঠানো হয়, যা ব্যবহারকারীর অনুরোধের উত্তর দিতে তথ্য হিসেবে ব্যবহার করে।

ডেভেলপারদের জন্য এজেন্টদের ফাংশন কলিং বাস্তবায়নের জন্য লাগবে:

1. ফাংশন কলিং সমর্থন করে এমন একটি LLM মডেল
2. ফাংশন বর্ণনা সম্বলিত স্কিমা
3. প্রতিটি বর্ণিত ফাংশনের কোড

চলুন একটি উদাহরণ দেখাই—কোন শহরের বর্তমান সময় নেওয়া:

1. **ফাংশন কলিং সমর্থন করে এমন একটি LLM ইনিশিয়ালাইজ করা:**

    সব মডেল ফাংশন কলিং সমর্থন করে না, তাই ব্যবহৃত LLM এ এটি আছে কিনা তা যাচাই করা জরুরি। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ফাংশন কলিং সমর্থন করে। আমরা Azure OpenAI ক্লায়েন্ট শুরু করতে পারি।

    ```python
    # Azure OpenAI ক্লায়েন্ট শুরু করুন
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **একটি ফাংশন স্কিমা তৈরি করুন:**

    এরপর একটি JSON স্কিমা সংজ্ঞায়িত করব যা ফাংশনের নাম, ফাংশন কী কাজ করে তার বর্ণনা, এবং প্যারামিটার নাম ও বর্ণনা থাকবে। 
    তারপর এই স্কিমাটি পূর্বে তৈরি ক্লায়েন্টকে এবং ব্যবহারকারীর অনুরোধ 'San Francisco তে সময় জানতে' পাঠানো হবে। গুরুত্বপূর্ণ হলো, ফলাফল সরাসরি নয় বরং একটি **টুল কল** ফেরত দেয়া হয়। যেমন পূর্বে বলা হয়েছে, LLM কাজের জন্য নির্বাচিত ফাংশনের নাম এবং আর্গুমেন্ট দেয়।

    ```python
    # মডেল পড়ার জন্য ফাংশনের বর্ণনা
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # প্রাথমিক ব্যবহারকারী বার্তা
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # প্রথম API কল: মডেলকে ফাংশন ব্যবহার করতে বলুন
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # মডেলের প্রতিক্রিয়া প্রক্রিয়াকরণ করুন
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
3. **কাজটি সম্পন্ন করার জন্য ফাংশনের কোড:**

    এখন যখন LLM কোন ফাংশন চালানো দরকার নির্বাচিত করেছে, কাজটি সম্পন্ন করার কোড বাস্তবায়ন ও চালাতে হবে। 
    আমরা পাইথনে বর্তমান সময় পাওয়ার কোড লিখব। পাশাপাশি response_message থেকে নাম ও আর্গুমেন্ট বের করার কোডও লিখতে হবে।

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
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # দ্বিতীয় API কল: মডেল থেকে চূড়ান্ত প্রতিক্রিয়া পান
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ফাংশন কলিং প্রায় সবাই—যদি না সব— এজেন্ট টুল ব্যবহার ডিজাইন প্যাটার্নের হৃদয়স্থল হলেও, সেটি শুরু থেকে তৈরি করা কিছু সময় জটিল হতে পারে। 
যেমনটি শিখেছি [Lesson 2](../../../02-explore-agentic-frameworks) এজেন্টিক ফ্রেমওয়ার্ক আগে থেকেই তৈরি নির্মাণ ব্লক সরবরাহ করে টুল ব্যবহার সহজ করতে।

## Agentic Frameworks দিয়ে টুল ব্যবহারের উদাহরণ

নিম্নলিখিত কিছু agentic ফ্রেমওয়ার্ক ব্যবহার করে টুল ব্যবহার ডিজাইন প্যাটার্ন কিভাবে বাস্তবায়ন করা যায় তার উদাহরণ:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> হলো AI এজেন্ট তৈরি করার জন্য একটি ওপেন-সোর্স ফ্রেমওয়ার্ক। এটি ফাংশন কলিং ব্যবহারের প্রক্রিয়া সরল করে, যেখানে আপনি `@tool` ডেকোরেটর ব্যবহার করে টুলগুলোকে পাইথন ফাংশন হিসেবে সংজ্ঞায়িত করতে পারেন। ফ্রেমওয়ার্ক মডেল ও কোডের মধ্যে বার্তা বিনিময় পরিচালনা করে। এটি আগেই তৈরি ফাইল সার্চ ও কোড ইন্টারপ্রেটার টুলেও অ্যাক্সেস দেয় `AzureAIProjectAgentProvider` এর মাধ্যমে।

নীচের ডায়াগ্রামটি Microsoft Agent Framework এ ফাংশন কলিংয়ের প্রক্রিয়া তুলে ধরে:

![function calling](../../../translated_images/bn/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework এ, টুলগুলোকে ডেকোরেটেড ফাংশন হিসেবে সংজ্ঞায়িত করা হয়। আগের 'get_current_time' ফাংশনটিকে `@tool` ডেকোরেটর দিয়ে টুলে রূপান্তর করা যায়। ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে ফাংশন ও তার প্যারামিটার সিরিয়ালাইজ করে, যা LLM কে পাঠানো স্কিমা তৈরি করে।

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ক্লায়েন্ট তৈরি করুন
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# একটি এজেন্ট তৈরি করুন এবং টুলের সাথে চালান
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> হলো একটি নতুন এজেন্টিক ফ্রেমওয়ার্ক যা ডেভেলপারদেরকে নিরাপদে, সহজে, এবং স্কেলযোগ্য উচ্চমানের AI এজেন্ট তৈরি, ডিপ্লয় ও পরিচালনার সুযোগ দেয়, নীচের কম্পিউট ও স্টোরেজ রিসোর্স ব্যবস্থাপনা ছাড়াই। বিশেষত এন্টারপ্রাইজ ব্যবহারের জন্য এটি গুরুত্বপূর্ণ কারণ এটি পূর্ণ জনপ্রিয় সার্ভিস যা এন্টারপ্রাইজ গ্রেড সিকিউরিটি প্রদান করে।

LLM API এর সঙ্গেও সরাসরি ডেভেলপমেন্টের তুলনায় Azure AI Agent Service কিছু সুবিধা দেয়, যেমন:

- স্বয়ংক্রিয় টুল কলিং – টুল কল পার্স করার, চালানোর ও প্রতিক্রিয়া ব্যবস্থাপনা করার প্রয়োজন নেই; সব কিছু এখন সার্ভার-সাইডে হয়
- নিরাপদভাবে পরিচালিত ডেটা – আপনার কথোপকথনের সকল তথ্য সংরক্ষণে থ্রেডের উপর নির্ভর করা যায়
- প্রস্তুত টুল – Bing, Azure AI Search, ও Azure Functions-এর মতো উৎসের সাথে ইন্টারঅ্যাকট করতে টুল

Azure AI Agent Service এ উপলব্ধ টুল দুই ভাগে বিভক্ত:

1. জ্ঞানভিত্তিক টুল:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search দিয়ে Grounding</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. কর্মসাধনের টুল:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI নির্ধারিত টুল</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service এইসব টুলকে একটি `toolset` হিসেবে ব্যবহারের সুযোগ দেয়। এছাড়াও এটি `threads` ব্যবহার করে নির্দিষ্ট কথোপকথনের বার্তা ইতিহাস ট্র্যাক করে।

ভাবুন আপনি একটি কোম্পানি Contoso-তে সেলস এজেন্ট। আপনি একটি কথোপকথন ভিত্তিক এজেন্ট তৈরি করতে চান যা সেলস ডেটা সম্পর্কিত প্রশ্নের উত্তর দিতে পারবে।

নিম্নলিখিত ছবি দেখায় কীভাবে Azure AI Agent Service ব্যবহার করে আপনার সেলস ডেটা বিশ্লেষণ করতে পারেন:

![Agentic Service In Action](../../../translated_images/bn/agent-service-in-action.34fb465c9a84659e.webp)

সার্ভিসের সঙ্গে কোনো টুল ব্যবহার করতে আমরা ক্লায়েন্ট তৈরি করে একটি টুল বা টুলসেট সংজ্ঞায়িত করতে পারি। ব্যবহারকারীর অনুরোধের ওপর ভিত্তি করে LLM টুলসেট দেখে নির্বাচন করবে—ব্যবহারকারী তৈরি 'fetch_sales_data_using_sqlite_query' ফাংশন ব্যবহার করবে নাকি পূর্বনির্মিত কোড ইন্টারপ্রেটার।

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

# টুলসেট ইনিশিয়ালাইজ করুন
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ফাংশন সহ ফাংশন কলিং এজেন্ট ইনিশিয়ালাইজ করুন এবং এটি টুলসেটে যোগ করুন
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# কোড ইন্টারপ্রিটার টুল ইনিশিয়ালাইজ করুন এবং এটি টুলসেটে যোগ করুন।
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## বিশ্বাসযোগ্য AI এজেন্ট তৈরিতে টুল ব্যবহার ডিজাইন প্যাটার্ন ব্যবহারের বিশেষ বিবেচনা কী?

LLM দ্বারা গতিশীলভাবে তৈরি SQL নিয়ে নিরাপত্তার উদ্বেগ সাধারণ, বিশেষত SQL ইনজেকশন বা ক্ষতিকারক কাজের ঝুঁকি যেমন ডাটাবেস ড্রপ বা টেম্পারিং। এই উদ্বেগগুলি হলেও সঠিকভাবে ডাটাবেস এক্সেস পারমিশন কনফিগার করে কার্যকরভাবে নিয়ন্ত্রণ করা যেতে পারে। অধিকাংশ ডাটাবেসের জন্য এটি রিড-অনলি কনফিগারেশন অন্তর্ভুক্ত। PostgreSQL অথবা Azure SQL মত সার্ভিসের জন্য অ্যাপকে রিড-অনলি (SELECT) রোল প্রদান করা উচিত।

নিরাপদ পরিবেশে অ্যাপ চালানো সুরক্ষা বৃদ্ধি করে। এন্টারপ্রাইজ ক্ষেত্রে, তথ্য অপারেশনাল সিস্টেম থেকে বের করে রিড-অনলি ডাটাবেস অথবা ডেটা ওয়্যারহাউসে রূপান্তরিত করা হয় যেখানে ব্যবহারকারী-বান্ধব স্কিমা থাকে। এতে ডেটা সুরক্ষিত, কর্মক্ষমতা ও অ্যাক্সেসযোগ্যতা উন্নত হয় এবং অ্যাপের অ্যাক্সেস সীমিত ও রিড-অনলি হয়।

## নমুনা কোড

- পাইথন: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## টুল ব্যবহার ডিজাইন প্যাটার্ন সম্পর্কিত আরো প্রশ্ন?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) এ যোগ দিন অন্য শিক্ষার্থীদের সাথে দেখা করতে, অফিস আওয়ারে অংশ নিতে এবং আপনার AI এজেন্ট প্রশ্নের উত্তর পেতে।

## অতিরিক্ত সম্পদ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service ওয়ার্কশপ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent ওয়ার্কশপ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework ওভারভিউ</a>

## আগের পাঠ

[Agentic Design Patterns সম্পর্কে ধারণা](../03-agentic-design-patterns/README.md)

## পরবর্তী পাঠ
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**দায়ভারবিহীন ঘোষণা**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ভুল বা অসম্পূর্ণতা থাকতে পারে বলে অনুগ্রহ করে সচেতন থাকুন। মূল নথি তার আদিম ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানুষের দ্বারা অনুবাদ করানো উচিৎ। এই অনুবাদের ব্যবহারে সৃষ্ট কোনও ভুল বোঝাবুঝি বা তাৎপর্যেমিশ্রণের জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->