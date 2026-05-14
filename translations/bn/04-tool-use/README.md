[![How to Design Good AI Agents](../../../translated_images/bn/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(এই পাঠের ভিডিও দেখতে উপরের ছবিতে ক্লিক করুন)_

# টুল ইউজ ডিজাইন প্যাটার্ন

টুলগুলি আকর্ষণীয় কারণ সেগুলি AI এজেন্টদের বৃহত্তর ক্ষমতার পরিসর দিতে পারে। এজেন্টের সীমিত কর্মের পরিবর্তে, একটি টুল যোগ করার মাধ্যমে এজেন্ট এখন ব্যাপক কর্ম সম্পাদন করতে পারে। এই অধ্যায়ে, আমরা টুল ইউজ ডিজাইন প্যাটার্ন সম্পর্কে আলোচনা করব, যা বর্ণনা করে কিভাবে AI এজেন্ট নির্দিষ্ট টুল ব্যবহার করে তাদের লক্ষ্য অর্জন করতে পারে।

## পরিচিতি

এই পাঠে, আমরা নিম্নলিখিত প্রশ্নগুলোর উত্তর খুঁজব:

- টুল ইউজ ডিজাইন প্যাটার্ন কী?
- এটি কোন ব্যবহার ক্ষেত্রে প্রয়োগ করা যেতে পারে?
- ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য কী উপাদান/বিল্ডিং ব্লক প্রয়োজন?
- বিশ্বাসযোগ্য AI এজেন্ট তৈরি করতে টুল ইউজ ডিজাইন প্যাটার্ন ব্যবহারে বিশেষ বিবেচ্য বিষয় কী কী?

## শেখার লক্ষ্য

এই পাঠ সম্পন্ন করার পর আপনি সক্ষম হবেন:

- টুল ইউজ ডিজাইন প্যাটার্ন এবং এর উদ্দেশ্য সংজ্ঞায়িত করতে।
- টুল ইউজ ডিজাইন প্যাটার্ন প্রযোজ্য এমন ব্যবহার ক্ষেত্র চিহ্নিত করতে।
- ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় মূল উপাদানগুলি বুঝতে।
- এই ডিজাইন প্যাটার্ন ব্যবহার করে AI এজেন্টের বিশ্বাসযোগ্যতা নিশ্চিতকরণের বিবেচনা চেনতে।

## টুল ইউজ ডিজাইন প্যাটার্ন কী?

**টুল ইউজ ডিজাইন প্যাটার্ন** LLM-গুদের বহিরাগত টুলের সাথে ইন্টারঅ্যাক্ট করার ক্ষমতা প্রদান করে নির্দিষ্ট লক্ষ্য অর্জনের জন্য। টুল হলো এমন কোড যা এজেন্ট দ্বারা চালিত হয়ে কাজ সম্পাদন করে। একটি টুল হতে পারে একটি সরল ফাংশন যেমন ক্যালকুলেটর, বা তৃতীয় পক্ষের সেবার API কল, যেমন শেয়ারের দাম বা আবহাওয়ার পূর্বাভাস। AI এজেন্টের প্রসঙ্গে, টুলগুলি নির্দিষ্ট **মডেল-জেনারেটেড ফাংশন কলের** প্রতিক্রিয়ায় এজেন্ট দ্বারা চালিত হয়।

## এটি কোন কোন ক্ষেত্রে প্রয়োগ করা যেতে পারে?

AI এজেন্টরা টুল ব্যবহার করে জটিল কাজ সম্পন্ন করতে, তথ্য সংগ্রহ করতে, বা সিদ্ধান্ত নিতে পারে। টুল ইউজ ডিজাইন প্যাটার্ন সাধারনত বহিরাগত সিস্টেম যেমন ডাটাবেস, ওয়েব সার্ভিস, বা কোড ইন্টারপ্রেটারের সাথে গতিশীল যোগাযোগের প্রয়োজনীয় ক্ষেত্রে ব্যবহৃত হয়। এর উপযোগিতা বিভিন্ন ক্ষেত্রে যেমন:

- **গতিশীল তথ্য আহরণ:** এজেন্টরা বহিরাগত API বা ডাটাবেস থেকে আপ-টু-ডেট তথ্য সংগ্রহ করতে পারে (যেমন, তথ্য বিশ্লেষণের জন্য SQLite ডাটাবেস থেকে তথ্য আহরণ, শেয়ার দর বা আবহাওয়া তথ্য সংগ্রহ)।
- **কোড নির্বাহ ও ব্যাখ্যা:** এজেন্টরা গণিত সমস্যার সমাধান, রিপোর্ট তৈরি, বা সিমুলেশন চালানোর জন্য কোড বা স্ক্রিপ্ট নির্বাহী করতে পারে।
- **ওয়ার্কফ্লো অটোমেশন:** টাস্ক শিডিউলার, ইমেইল সার্ভিস, বা ডাটা পাইপলাইন ইন্টিগ্রেট করে পুনরাবৃত্তিমূলক বা বহু-ধাপের কার্যপ্রবাহ স্বয়ংক্রিয় করা।
- **গ্রাহক সহায়তা:** এজেন্টরা CRM সিস্টেম, টিকিটিং প্ল্যাটফর্ম, বা জ্ঞানভিত্তিক ডাটাবেসের সাথে ইন্টারঅ্যাক্ট করে ব্যবহারকারীর প্রশ্ন সমাধান করতে পারে।
- **কন্টেন্ট তৈরি ও সম্পাদনা:** ব্যাকরণ পরীক্ষক, টেক্সট সারাংশকারী, বা বিষয়বস্তু নিরাপত্তা মূল্যায়কের মত টুল ব্যবহার করে বিষয়বস্তু তৈরিতে সহায়তা।

## টুল ইউজ ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য কী উপাদান/বিল্ডিং ব্লক প্রয়োজন?

এই বিল্ডিং ব্লকগুলো AI এজেন্টকে বিস্তৃত কাজ সম্পাদনে সক্ষম করে। আসুন টুল ইউজ ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় মূল উপাদানগুলো দেখি:

- **ফাংশন/টুল স্কিমাস**: উপলব্ধ টুলের বিস্তারিত সংজ্ঞা, যার মধ্যে ফাংশনের নাম, উদ্দেশ্য, প্রয়োজনীয় প্যারামিটার, এবং প্রত্যাশিত আউটপুট। এই স্কিমাগুলো LLM-কে উপলব্ধ টুলগুলো বুঝতে এবং সঠিক অনুরোধ গঠন করতে সহায়তা করে।

- **ফাংশন নির্বাহ লজিক**: ব্যবহারকারীর উদ্দেশ্য ও কথোপকথনের প্রেক্ষাপট অনুযায়ী টুল কখন ও কিভাবে ডাকা হবে তা নিয়ন্ত্রণ করে। এর মধ্যে পরিকল্পক মডিউল, রাউটিং মেকানিজম, বা শর্তাধীন ফ্লো থাকতে পারে যা টুল ব্যবহারের গতিশীল নির্ধারণ করে।

- **মেসেজ হ্যান্ডলিং সিস্টেম**: ব্যবহারকারী ইনপুট, LLM উত্তর, টুল কল, এবং টুল আউটপুটের মধ্যে কথোপকথন প্রবাহ নিয়ন্ত্রণ করে।

- **টুল ইন্টিগ্রেশন ফ্রেমওয়ার্ক**: এজেন্টকে বিভিন্ন টুলের সাথে সংযুক্ত করে, তা সরল ফাংশন হোক বা জটিল বহিরাগত সেবা।

- **এরর হ্যান্ডলিং ও ভ্যালিডেশন**: টুল চালনার ব্যর্থতা, প্যারামিটার যাচাই এবং অপ্রত্যাশিত প্রতিক্রিয়া পরিচালনা।

- **স্টেট ম্যানেজমেন্ট**: কথোপকথনের প্রেক্ষাপট, পূর্বের টুল ইন্টারঅ্যাকশন এবং স্থায়ী তথ্য ট্র্যাক করে বহু-চক্র কথোপকথনের সামঞ্জস্য নিশ্চিত।

এবার আসুন ফাংশন/টুল কলিং আরও বিস্তারিত দেখি।

### ফাংশন/টুল কলিং

ফাংশন কলিং হলো মূল উপায় যার মাধ্যমে LLM-কে টুলের সাথে ইন্টারঅ্যাক্ট করার সুযোগ দেয়া হয়। 'ফাংশন' এবং 'টুল' প্রায়শই একে অপরের পরিবর্তে ব্যবহৃত হয় কারণ 'ফাংশন' (পুনঃব্যবহারযোগ্য কোড ব্লক) হলো এজেন্টদের কার্যের উপকরণ। ফাংশনের কোড চালানোর জন্য, LLM-কে ব্যবহারকারীর অনুরোধের সাথে ফাংশনের বর্ণনা তুলনা করতে হয়। এটি করতে উপলব্ধ সকল ফাংশনের বর্ণনা থাকা একটি স্কিমা LLM-কে পাঠানো হয়। LLM যথোপযুক্ত ফাংশন নির্বাচন করে তার নাম ও আর্গুমেন্ট return করে। নির্বাচিত ফাংশন চালানো হয়, তার প্রতিক্রিয়া LLM-কে পাঠানো হয় যা ব্যবহারকারীর অনুরোধের উত্তর দিতে ব্যবহার করা হয়।

ডেভেলপারদের জন্য ফাংশন কলিং বাস্তবায়নের জন্য প্রয়োজন:

1. ফাংশন কলিং সমর্থনকারী LLM মডেল
2. ফাংশন বর্ণনা সহ একটি স্কিমা
3. প্রতিটি বর্ণিত ফাংশনের কোড

চলুন উদাহরণ স্বরূপ একটি শহরের বর্তমান সময় জানা দেখি:

1. **ফাংশন কলিং সমর্থনকারী একটি LLM শুরু করুন:**

    সব মডেল ফাংশন কলিং সমর্থন করে না, তাই যাচাই করা জরুরি যে আপনি যে LLM ব্যবহার করছেন তা করে কিনা।     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ফাংশন কলিং সমর্থন করে। আমরা Azure OpenAI ক্লায়েন্ট শুরু করতে পারি। 

    ```python
    # Azure OpenAI ক্লায়েন্ট ইনিশিয়ালাইজ করুন
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **একটি ফাংশন স্কিমা তৈরি করুন**:

    এরপর আমরা একটি JSON স্কিমা সংজ্ঞায়িত করব যাতে ফাংশনের নাম, এর কার্যবিবরণ, এবং ফাংশন প্যারামিটারগুলোর নাম ও বর্ণনা থাকবে। আমরা এই স্কিমা পূর্বে তৈরি ক্লায়েন্টকে পাঠাব, ব্যবহারকারীর অনুরোধের সাথে, যাতে সান ফ্রান্সিসকোর সময় খুঁজে পাওয়া যায়। উল্লেখযোগ্য হলো, **টুল কল** ফেরত আসে, প্রশ্নের চূড়ান্ত উত্তর নয়। পূর্বে যেমন বলা হয়েছে, LLM ফাংশনের নাম ও আর্গুমেন্ট রিটার্ন করে যা কাজের জন্য প্রেরিত হবে।

    ```python
    # মডেলটি পড়ার জন্য ফাংশনের বর্ণনা
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
  
    # প্রাথমিক ব্যবহারকারীর বার্তা
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # প্রথম API কল: মডেলকে ফাংশন ব্যবহার করার জন্য জিজ্ঞাসা করুন
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # মডেলের প্রতিক্রিয়া প্রক্রিয়া করুন
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **কাজটি সম্পাদনের জন্য প্রয়োজনীয় ফাংশন কোড:**

    এখন LLM সিদ্ধান্ত নিয়েছে কোন ফাংশন চালাতে হবে, সে ফাংশনটি বাস্তবায়ন ও চালানো দরকার। আমরা পাইথনে বর্তমান সময় পাওয়ার কোড লিখব। এছাড়াও response_message থেকে নাম ও আর্গুমেন্ট বের করার কোডও লিখতে হবে যাতে চূড়ান্ত ফলাফল পাওয়া যায়।

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

ফাংশন কলিং অধিকাংশ, সম্ভবত সব, এজেন্ট টুল ইউজ ডিজাইনে কেন্দ্রীয় ভূমিকা পালন করে, তবে এটাকে শুরু থেকে তৈরি করা মাঝে মাঝে চ্যালেঞ্জিং হতে পারে। আমরা [Lesson 2](../../../02-explore-agentic-frameworks) এ শিখেছি যে এজেন্টিক ফ্রেমওয়ার্কগুলি প্রাক-নির্মিত বিল্ডিং ব্লক সরবরাহ করে টুল ইউজ বাস্তবায়নের জন্য।

## Agentic Frameworks সহ টুল ইউজ উদাহরণ

নিম্নে বিভিন্ন এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করে টুল ইউজ ডিজাইন প্যাটার্ন বাস্তবায়নের কিছু উদাহরণ দেয়া হলো:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> হলো একটি ওপেন-সোর্স AI ফ্রেমওয়ার্ক AI এজেন্ট তৈরি করার জন্য। এটি ফাংশন কলিং ব্যবহারের প্রক্রিয়া সরল করে, যেখানে আপনি টুলগুলোকে পাইথন ফাংশন হিসেবে `@tool` ডেকোরেটর ব্যবহার করে সংজ্ঞায়িত করতে পারেন। ফ্রেমওয়ার্ক মডেল ও আপনার কোডের মধ্যে কথা-বলার সমন্বয় করে। এটি File Search এবং Code Interpreter মতো প্রাক-নির্মিত টুলগুলোতেও অ্যাক্সেস দেয় `AzureAIProjectAgentProvider` এর মাধ্যমে।

নিম্নলিখিত চিত্রটি Microsoft Agent Framework-এ ফাংশন কলিং প্রক্রিয়া দেখায়:

![function calling](../../../translated_images/bn/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework-এ টুলগুলোকে সাজানো ফাংশন হিসেবে সংজ্ঞায়িত করা হয়। আমরা পূর্বে দেখানো `get_current_time` ফাংশনটিকে `@tool` ডেকোরেটর ব্যবহার করে টুলে রূপান্তর করতে পারি। ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে ফাংশন ও এর প্যারামিটার সিরিয়ালাইজ করে, স্কিমা তৈরি করে LLM-কে পাঠায়।

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> একটি নতুন এজেন্টিক ফ্রেমওয়ার্ক যা ডেভেলপারদের নিরাপদে উচ্চমানের এবং প্রসারযোগ্য AI এজেন্ট তৈরি, মোতায়েন ও স্কেল করতে সাহায্য করে, কম্পিউট ও স্টোরেজ সম্পদ পরিচালনার প্রয়োজন ছাড়া। এটি বিশেষত এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য কার্যকর কারণ এটি সম্পূর্ণ ম্যানেজড সেবা এবং এন্টারপ্রাইজ স্তরের নিরাপত্তা প্রদান করে।

LLM API থেকে সরাসরি উন্নয়নের তুলনায় Azure AI Agent Service কিছু সুবিধা দেয়, যেমন:

- স্বয়ংক্রিয় টুল কলিং – টুল কল পার্স, টুল চালনা এবং প্রতিক্রিয়া পরিচালনা করার দরকার নেই; সবই এখন সার্ভার সাইডে সম্পন্ন হয়
- নিরাপদভাবে পরিচালিত ডেটা – নিজস্ব কথোপকথন স্টেট পরিচালনার পরিবর্তে থ্রেডের মাধ্যমে সমস্ত তথ্য সঞ্চয় করতে পারেন
- প্রস্তুত টুল – Bing, Azure AI Search, Azure Functions এর মতো ডেটা সোর্সের সাথে ইন্টারঅ্যাকশনের টুল।

Azure AI Agent Service-এর টুলগুলো দুটো ভাগে বিভক্ত:

1. জ্ঞানাত্মক টুলসমূহ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search দিয়ে গ্রাউন্ডিং</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. অ্যাকশন টুলসমূহ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI নির্ধারিত টুল</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service আমাদের এগুলোকে একটি `toolset` হিসেবে ব্যবহার করার সুযোগ দেয়। এটি `threads` ব্যবহার করে যা নির্দিষ্ট কথোপকথনের বার্তাগুলোর ইতিহাস ধরে রাখে।

ধরুন আপনি একটি কোম্পানি Contoso তে একজন সেলস এজেন্ট। আপনি এমন একটি কথোপকথন এজেন্ট তৈরি করতে চান যা আপনার সেলস ডেটা নিয়ে প্রশ্নের উত্তর দিতে পারে।

নিম্নলিখিত চিত্রটি দেখায় কিভাবে Azure AI Agent Service ব্যবহার করে আপনার সেলস ডেটা বিশ্লেষণ করা যেতে পারে:

![Agentic Service In Action](../../../translated_images/bn/agent-service-in-action.34fb465c9a84659e.webp)

সার্ভিসের সাথে এই টুলগুলো ব্যবহার করতে আমরা একটি ক্লায়েন্ট তৈরি করে টুল বা টুলসেট সংজ্ঞায়িত করতে পারি। বাস্তবায়নের জন্য নিম্নলিখিত পাইথন কোড ব্যবহার করা যেতে পারে। LLM টুলসেট দেখে ব্যবহারকারীর অনুরোধ অনুযায়ী ইউজার-তৈরি ফাংশন `fetch_sales_data_using_sqlite_query` বা প্রাক-নির্মিত Code Interpreter ব্যবহার করার সিদ্ধান্ত নেবে।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ফাংশন যা fetch_sales_data_functions.py ফাইলে পাওয়া যায়।
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# টুলসেট আরম্ভ করুন
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ফাংশন দিয়ে ফাংশন কলিং এজেন্ট আরম্ভ করুন এবং সেটিকে টুলসেটে যোগ করুন
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# কোড ইন্টারপ্রেটার টুল আরম্ভ করুন এবং সেটিকে টুলসেটে যোগ করুন।
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## বিশ্বাসযোগ্য AI এজেন্ট নির্মাণে টুল ইউজ ডিজাইন প্যাটার্ন ব্যবহারের বিশেষ বিবেচ্য বিষয় কী কী?

LLM দ্বারা গড়া ডায়নামিক SQL এর নিরাপত্তা একটি সাধারণ উদ্বেগ, বিশেষ করে SQL ইনজেকশন বা ক্ষতিকারক কাজ যেমন ডাটাবেস ড্রপ করা বা ফাঁকফোকর করার ঝুঁকি। এই উদ্বেগ গুলো সঠিকভাবে ডাটাবেস অ্যাক্সেস অনুমতি কনফিগার করে কার্যকরভাবে প্রতিরোধ করা যেতে পারে। অধিকাংশ ডাটাবেসে এটি শুধুমাত্র রিড-অনলি করা হয়। PostgreSQL বা Azure SQL এর মতো ডাটাবেস সার্ভিসে অ্যাপকে রিড-অনলি (SELECT) ভূমিকা দেওয়া হয়।

সুরক্ষিত পরিবেশে অ্যাপ চালানো সুরক্ষা বাড়ায়। এন্টারপ্রাইজ পরিস্থিতিতে ডেটা সাধারণত অপারেশনাল সিস্টেম থেকে রিড-অনলি ডাটাবেস বা ডাটা ওয়ারহাউসে রূপান্তরিত হয় ব্যবহারকারী-বান্ধব স্কিমা সহ। এটি ডেটা সুরক্ষিত, কর্মক্ষমতা ও প্রবেশযোগ্যতার জন্য অপ্টিমাইজড এবং অ্যাপের সীমিত রিড-অনলি অ্যাক্সেস নিশ্চিত করে।

## নমুনা কোড

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## টুল ইউজ ডিজাইন প্যাটার্ন সম্পর্কে আরও প্রশ্ন আছে?

অন্যান্য শিক্ষার্থীদের সঙ্গে দেখা করতে, অফিস আওয়ার অংশগ্রহণ করতে এবং AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পেতে [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) এ যোগ দিন।

## অতিরিক্ত সম্পদ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service কর্মশালা</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent কর্মশালা</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework ওভারভিউ</a>

## পূর্ববর্তী পাঠ

[Agentic Design Patterns বুঝা](../03-agentic-design-patterns/README.md)

## পরবর্তী পাঠ
[এজেন্টিক আরএজি](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->