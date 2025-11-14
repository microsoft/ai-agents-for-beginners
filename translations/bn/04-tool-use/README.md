<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e056335d729ba6e49571db7a6533825d",
  "translation_date": "2025-09-30T06:41:11+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "bn"
}
-->
[![কিভাবে ভালো AI এজেন্ট ডিজাইন করবেন](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.bn.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(উপরের ছবিতে ক্লিক করে এই পাঠের ভিডিও দেখুন)_

# টুল ব্যবহারের ডিজাইন প্যাটার্ন

টুলগুলো আকর্ষণীয় কারণ এগুলো AI এজেন্টদের আরও বিস্তৃত ক্ষমতা প্রদান করে। এজেন্টের সীমিত সংখ্যক কাজ করার ক্ষমতার পরিবর্তে, একটি টুল যোগ করার মাধ্যমে এজেন্ট এখন অনেক ধরণের কাজ করতে পারে। এই অধ্যায়ে আমরা টুল ব্যবহারের ডিজাইন প্যাটার্ন নিয়ে আলোচনা করব, যা বর্ণনা করে কিভাবে AI এজেন্টরা নির্দিষ্ট টুল ব্যবহার করে তাদের লক্ষ্য অর্জন করতে পারে।

## পরিচিতি

এই পাঠে আমরা নিম্নলিখিত প্রশ্নগুলোর উত্তর খুঁজব:

- টুল ব্যবহারের ডিজাইন প্যাটার্ন কী?
- এটি কোন কোন ক্ষেত্রে প্রয়োগ করা যেতে পারে?
- এই ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় উপাদান/গঠনমূলক অংশগুলো কী কী?
- বিশ্বাসযোগ্য AI এজেন্ট তৈরি করতে টুল ব্যবহারের ডিজাইন প্যাটার্ন ব্যবহার করার ক্ষেত্রে বিশেষ বিবেচনাগুলো কী কী?

## শেখার লক্ষ্য

এই পাঠ শেষ করার পর, আপনি সক্ষম হবেন:

- টুল ব্যবহারের ডিজাইন প্যাটার্ন এবং এর উদ্দেশ্য সংজ্ঞায়িত করতে।
- কোন ক্ষেত্রে টুল ব্যবহারের ডিজাইন প্যাটার্ন প্রযোজ্য তা চিহ্নিত করতে।
- ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় মূল উপাদানগুলো বুঝতে।
- এই ডিজাইন প্যাটার্ন ব্যবহার করে AI এজেন্টের বিশ্বাসযোগ্যতা নিশ্চিত করার জন্য বিবেচনাগুলো চিনতে।

## টুল ব্যবহারের ডিজাইন প্যাটার্ন কী?

**টুল ব্যবহারের ডিজাইন প্যাটার্ন** LLM-কে নির্দিষ্ট লক্ষ্য অর্জনের জন্য বাইরের টুলের সাথে ইন্টারঅ্যাক্ট করার ক্ষমতা প্রদান করার উপর ভিত্তি করে। টুল হলো কোড যা এজেন্ট দ্বারা কার্যকর করা যায় কাজ সম্পাদনের জন্য। একটি টুল একটি সাধারণ ফাংশন হতে পারে যেমন একটি ক্যালকুলেটর, অথবা তৃতীয় পক্ষের সার্ভিসে API কল হতে পারে যেমন স্টক প্রাইস অনুসন্ধান বা আবহাওয়ার পূর্বাভাস। AI এজেন্টের প্রসঙ্গে, টুলগুলো এজেন্টদের দ্বারা **মডেল-উৎপন্ন ফাংশন কল** এর প্রতিক্রিয়ায় কার্যকর করার জন্য ডিজাইন করা হয়।

## এটি কোন কোন ক্ষেত্রে প্রয়োগ করা যেতে পারে?

AI এজেন্টরা টুল ব্যবহার করে জটিল কাজ সম্পন্ন করতে, তথ্য সংগ্রহ করতে, বা সিদ্ধান্ত নিতে পারে। টুল ব্যবহারের ডিজাইন প্যাটার্ন প্রায়ই এমন পরিস্থিতিতে ব্যবহৃত হয় যেখানে বাইরের সিস্টেমের সাথে গতিশীল ইন্টারঅ্যাকশন প্রয়োজন, যেমন ডাটাবেস, ওয়েব সার্ভিস, বা কোড ইন্টারপ্রেটার। এই ক্ষমতা বিভিন্ন ক্ষেত্রে কার্যকর, যেমন:

- **গতিশীল তথ্য সংগ্রহ:** এজেন্টরা বাইরের API বা ডাটাবেস থেকে আপডেটেড তথ্য সংগ্রহ করতে পারে (যেমন SQLite ডাটাবেস থেকে ডেটা বিশ্লেষণ, স্টক প্রাইস বা আবহাওয়ার তথ্য সংগ্রহ)।
- **কোড কার্যকর এবং ব্যাখ্যা:** এজেন্টরা কোড বা স্ক্রিপ্ট কার্যকর করতে পারে গণিত সমস্যার সমাধান, রিপোর্ট তৈরি, বা সিমুলেশন সম্পাদনের জন্য।
- **ওয়ার্কফ্লো অটোমেশন:** টাস্ক শিডিউলার, ইমেইল সার্ভিস, বা ডেটা পাইপলাইনের মতো টুল ইন্টিগ্রেট করে পুনরাবৃত্তিমূলক বা বহু-ধাপের ওয়ার্কফ্লো অটোমেট করা।
- **কাস্টমার সাপোর্ট:** এজেন্টরা CRM সিস্টেম, টিকেটিং প্ল্যাটফর্ম, বা নলেজ বেসের সাথে ইন্টারঅ্যাক্ট করে ব্যবহারকারীর প্রশ্নের সমাধান করতে পারে।
- **কন্টেন্ট তৈরি এবং সম্পাদনা:** এজেন্টরা গ্রামার চেকার, টেক্সট সামারাইজার, বা কন্টেন্ট সেফটি ইভ্যালুয়েটরের মতো টুল ব্যবহার করে কন্টেন্ট তৈরির কাজে সহায়তা করতে পারে।

## টুল ব্যবহারের ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় উপাদান/গঠনমূলক অংশগুলো কী কী?

এই গঠনমূলক অংশগুলো AI এজেন্টকে বিভিন্ন ধরণের কাজ সম্পাদন করতে সক্ষম করে। আসুন টুল ব্যবহারের ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় মূল উপাদানগুলো দেখি:

- **ফাংশন/টুল স্কিমা:** উপলব্ধ টুলগুলোর বিস্তারিত সংজ্ঞা, যার মধ্যে ফাংশনের নাম, উদ্দেশ্য, প্রয়োজনীয় প্যারামিটার, এবং প্রত্যাশিত আউটপুট অন্তর্ভুক্ত। এই স্কিমাগুলো LLM-কে উপলব্ধ টুলগুলো কী এবং কিভাবে বৈধ অনুরোধ তৈরি করতে হয় তা বুঝতে সাহায্য করে।

- **ফাংশন কার্যকর করার লজিক:** ব্যবহারকারীর উদ্দেশ্য এবং কথোপকথনের প্রসঙ্গের উপর ভিত্তি করে টুলগুলো কখন এবং কীভাবে কার্যকর করা হবে তা নিয়ন্ত্রণ করে। এতে প্ল্যানার মডিউল, রাউটিং মেকানিজম, বা শর্তসাপেক্ষ প্রবাহ অন্তর্ভুক্ত থাকতে পারে যা গতিশীলভাবে টুল ব্যবহারের সিদ্ধান্ত নেয়।

- **মেসেজ হ্যান্ডলিং সিস্টেম:** ব্যবহারকারীর ইনপুট, LLM-এর প্রতিক্রিয়া, টুল কল, এবং টুল আউটপুটের মধ্যে কথোপকথনের প্রবাহ পরিচালনা করে।

- **টুল ইন্টিগ্রেশন ফ্রেমওয়ার্ক:** এজেন্টকে বিভিন্ন টুলের সাথে সংযুক্ত করার জন্য অবকাঠামো প্রদান করে, তা সাধারণ ফাংশন হোক বা জটিল বাইরের সার্ভিস।

- **এরর হ্যান্ডলিং এবং ভ্যালিডেশন:** টুল কার্যকর করার ব্যর্থতা পরিচালনা, প্যারামিটার যাচাই, এবং অপ্রত্যাশিত প্রতিক্রিয়া পরিচালনার জন্য প্রক্রিয়া।

- **স্টেট ম্যানেজমেন্ট:** কথোপকথনের প্রসঙ্গ, পূর্ববর্তী টুল ইন্টারঅ্যাকশন, এবং স্থায়ী ডেটা ট্র্যাক করে বহুমুখী কথোপকথনে সামঞ্জস্য নিশ্চিত করে।

এখন আমরা ফাংশন/টুল কলিং সম্পর্কে আরও বিস্তারিতভাবে আলোচনা করব।

### ফাংশন/টুল কলিং

ফাংশন কলিং হলো বড় ভাষার মডেল (LLM) টুলের সাথে ইন্টারঅ্যাক্ট করার প্রধান উপায়। প্রায়ই 'ফাংশন' এবং 'টুল' শব্দগুলো একে অপরের পরিবর্তে ব্যবহৃত হয় কারণ 'ফাংশন' (পুনরায় ব্যবহারযোগ্য কোডের ব্লক) হলো 'টুল' যা এজেন্টরা কাজ সম্পাদনের জন্য ব্যবহার করে। একটি ফাংশনের কোড কার্যকর করার জন্য, LLM-কে ব্যবহারকারীর অনুরোধের সাথে ফাংশনের বিবরণ তুলনা করতে হয়। এটি করার জন্য, উপলব্ধ ফাংশনের বিবরণসহ একটি স্কিমা LLM-কে পাঠানো হয়। এরপর LLM সবচেয়ে উপযুক্ত ফাংশন নির্বাচন করে এবং এর নাম ও আর্গুমেন্টগুলো ফেরত দেয়। নির্বাচিত ফাংশন কার্যকর করা হয়, এর প্রতিক্রিয়া LLM-কে পাঠানো হয়, যা ব্যবহারকারীর অনুরোধের উত্তর দিতে তথ্য ব্যবহার করে।

ডেভেলপারদের এজেন্টের জন্য ফাংশন কলিং বাস্তবায়ন করতে প্রয়োজন হবে:

1. একটি LLM মডেল যা ফাংশন কলিং সমর্থন করে
2. একটি স্কিমা যা ফাংশনের বিবরণ ধারণ করে
3. প্রতিটি ফাংশনের জন্য কোড যা স্কিমায় বর্ণিত

চলুন একটি উদাহরণ ব্যবহার করে দেখি, যেখানে একটি শহরের বর্তমান সময় পাওয়া হচ্ছে:

1. **ফাংশন কলিং সমর্থন করে এমন একটি LLM ইনিশিয়ালাইজ করুন:**

    সব মডেল ফাংশন কলিং সমর্থন করে না, তাই আপনি যে LLM ব্যবহার করছেন তা নিশ্চিত করা গুরুত্বপূর্ণ। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ফাংশন কলিং সমর্থন করে। আমরা Azure OpenAI ক্লায়েন্ট ইনিশিয়ালাইজ করে শুরু করতে পারি।

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **একটি ফাংশন স্কিমা তৈরি করুন:**

    এরপর আমরা একটি JSON স্কিমা সংজ্ঞায়িত করব, যেখানে ফাংশনের নাম, ফাংশন কী করে তার বিবরণ, এবং ফাংশনের প্যারামিটারগুলোর নাম ও বিবরণ থাকবে। 
    আমরা এই স্কিমা এবং ব্যবহারকারীর অনুরোধকে পূর্বে তৈরি করা ক্লায়েন্টে পাঠাব। এখানে গুরুত্বপূর্ণ বিষয় হলো একটি **টুল কল** ফেরত আসে, **প্রশ্নের চূড়ান্ত উত্তর নয়**। পূর্বে উল্লেখ করা হয়েছে, LLM টাস্কের জন্য নির্বাচিত ফাংশনের নাম এবং পাস করা আর্গুমেন্টগুলো ফেরত দেয়।

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **টাস্ক সম্পাদনের জন্য প্রয়োজনীয় ফাংশন কোড:**

    এখন LLM নির্ধারণ করেছে কোন ফাংশন কার্যকর করতে হবে, টাস্ক সম্পাদনের জন্য কোড বাস্তবায়ন এবং কার্যকর করতে হবে। 
    আমরা Python-এ বর্তমান সময় পাওয়ার কোড বাস্তবায়ন করতে পারি। এছাড়াও, response_message থেকে নাম এবং আর্গুমেন্টগুলো বের করার কোড লিখতে হবে চূড়ান্ত ফলাফল পেতে।

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

ফাংশন কলিং হলো বেশিরভাগ, যদি না সব, এজেন্ট টুল ব্যবহারের ডিজাইনের কেন্দ্রবিন্দু। তবে এটি শূন্য থেকে বাস্তবায়ন করা কখনও কখনও চ্যালেঞ্জিং হতে পারে। 
আমরা [Lesson 2](../../../02-explore-agentic-frameworks) এ শিখেছি যে এজেন্টিক ফ্রেমওয়ার্কগুলো আমাদের টুল ব্যবহারের জন্য প্রি-বিল্ট গঠনমূলক অংশ প্রদান করে।

## এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করে টুল ব্যবহারের উদাহরণ

এখানে বিভিন্ন এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করে টুল ব্যবহারের ডিজাইন প্যাটার্ন বাস্তবায়নের কিছু উদাহরণ দেওয়া হলো:

### সেমান্টিক কার্নেল

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">সেমান্টিক কার্নেল</a> হলো .NET, Python, এবং Java ডেভেলপারদের জন্য একটি ওপেন-সোর্স AI ফ্রেমওয়ার্ক যারা বড় ভাষার মডেল (LLM) নিয়ে কাজ করছেন। এটি ফাংশন কলিং ব্যবহারের প্রক্রিয়াকে সহজ করে তোলে কারণ এটি আপনার ফাংশন এবং এর প্যারামিটারগুলোকে মডেলের কাছে স্বয়ংক্রিয়ভাবে বর্ণনা করে একটি প্রক্রিয়ার মাধ্যমে, যাকে <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a> বলা হয়। এটি মডেল এবং আপনার কোডের মধ্যে যোগাযোগ পরিচালনা করে। সেমান্টিক কার্নেলের মতো একটি এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করার আরেকটি সুবিধা হলো এটি আপনাকে <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> এবং <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a> এর মতো প্রি-বিল্ট টুল অ্যাক্সেস করতে দেয়।

নিম্নলিখিত চিত্রটি সেমান্টিক কার্নেল দিয়ে ফাংশন কলিংয়ের প্রক্রিয়া চিত্রিত করে:

![function calling](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.bn.png)

সেমান্টিক কার্নেলে ফাংশন/টুলগুলোকে <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">প্লাগইন</a> বলা হয়। আমরা পূর্বে দেখা `get_current_time` ফাংশনকে একটি ক্লাসে পরিণত করে প্লাগইনে রূপান্তর করতে পারি। আমরা `kernel_function` ডেকোরেটরও ইমপোর্ট করতে পারি, যা ফাংশনের বিবরণ গ্রহণ করে। এরপর আপনি যখন GetCurrentTimePlugin সহ একটি কার্নেল তৈরি করবেন, কার্নেলটি স্বয়ংক্রিয়ভাবে ফাংশন এবং এর প্যারামিটারগুলোকে সিরিয়ালাইজ করবে, প্রক্রিয়ায় LLM-এ পাঠানোর জন্য স্কিমা তৈরি করবে।

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> হলো একটি নতুন এজেন্টিক ফ্রেমওয়ার্ক যা ডেভেলপারদের উচ্চ-মানের এবং সম্প্রসারণযোগ্য AI এজেন্ট তৈরি, ডিপ্লয়, এবং স্কেল করতে সক্ষম করে, এবং এর জন্য আন্ডারলাইন কম্পিউট এবং স্টোরেজ রিসোর্স পরিচালনা করার প্রয়োজন হয় না। এটি বিশেষভাবে এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য কার্যকর কারণ এটি একটি সম্পূর্ণ পরিচালিত সার্ভিস যা এন্টারপ্রাইজ গ্রেড নিরাপত্তা প্রদান করে।

LLM API সরাসরি ব্যবহার করার তুলনায় Azure AI Agent Service কিছু সুবিধা প্রদান করে, যেমন:

- স্বয়ংক্রিয় টুল কলিং – টুল কল পার্স করা, টুল কার্যকর করা, এবং প্রতিক্রিয়া পরিচালনা করার প্রয়োজন নেই; এটি এখন সার্ভার-সাইডে সম্পন্ন হয়।
- নিরাপদভাবে পরিচালিত ডেটা – আপনার নিজস্ব কথোপকথনের স্টেট পরিচালনা করার পরিবর্তে, আপনি থ্রেড ব্যবহার করে প্রয়োজনীয় সমস্ত তথ্য সংরক্ষণ করতে পারেন।
- প্রস্তুত-প্রস্তুত টুল – Bing, Azure AI Search, এবং Azure Functions-এর মতো ডেটা সোর্সের সাথে ইন্টারঅ্যাক্ট করার জন্য টুল।

Azure AI Agent Service-এ উপলব্ধ টুলগুলোকে দুটি বিভাগে ভাগ করা যায়:

1. নলেজ টুল:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search দিয়ে গ্রাউন্ডিং</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. অ্যাকশন টুল:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI নির্ধারিত টুল</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service আমাদের এই টুলগুলোকে একসাথে `toolset` হিসেবে ব্যবহার করার সুযোগ দেয়। এটি `threads` ব্যবহার করে একটি নির্দিষ্ট কথোপকথনের বার্তাগুলোর ইতিহাস ট্র্যাক করে।

ধরা যাক আপনি Contoso নামক একটি কোম্পানির সেলস এজেন্ট। আপনি একটি কথোপকথন এজেন্ট তৈরি করতে চান যা আপনার সেলস ডেটা সম্পর্কে প্রশ্নের উত্তর দিতে পারে।

নিম্নলিখিত চিত্রটি দেখায় কিভাবে আপনি Azure AI Agent Service ব্যবহার করে আপনার সেলস ডেটা বিশ্লেষণ করতে পারেন:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.bn.jpg)

এই সার্ভিসের সাথে কোনো টুল ব্যবহার করতে আমরা একটি ক্লায়েন্ট তৈরি করতে পারি এবং একটি টুল বা টুলসেট সংজ্ঞায়িত করতে পারি। এটি বাস্তবায়নের জন্য আমরা নিম্নলিখিত Python কোড ব্যবহার করতে পারি। LLM টুলসেটটি দেখে ব্যবহারকারীর তৈরি ফাংশন `fetch_sales_data_using_sqlite_query` অথবা প্রি-বিল্ট Code Interpreter ব্যবহার করবে, যা ব্যবহারকারীর অনুরোধের উপর নির্ভর করবে।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## বিশ্বাসযোগ্য AI এজেন্ট তৈরি করতে টুল ব্যবহারের ডিজাইন প্যাটার্ন ব্যবহার করার ক্ষেত্রে বিশেষ বিবেচনাগুলো কী কী?

LLM দ্বারা গতিশীলভাবে তৈরি করা SQL-এর ক্ষেত্রে একটি সাধারণ উদ্বেগ হলো নিরাপত্তা, বিশেষত SQL ইনজেকশন বা ক্ষতিকারক কার্যকলাপের ঝুঁকি, যেমন ডাটাবেস মুছে ফেলা বা পরিবর্তন করা। যদিও এই উদ্বেগগুলো বৈধ, সেগুলো কার্যকরভাবে মোকাবিলা করা যেতে পারে ডাটাবেস অ্যাক্সেস অনুমতিগুলো সঠিকভাবে কনফিগার করে। বেশিরভাগ ডাটাবেসের জন্য এটি ডাটাবেসকে শুধুমাত্র-পড়া (read-only) হিসেবে কনফিগার করার মাধ্যমে সম্পন্ন হয়। PostgreSQL বা Azure SQL-এর মতো ডাটাবেস সার্ভিসের জন্য, অ্যাপটিকে শুধুমাত্র-পড়া (SELECT) ভূম
অ্যাপটি একটি সুরক্ষিত পরিবেশে চালানো সুরক্ষার স্তর আরও উন্নত করে। এন্টারপ্রাইজ পরিস্থিতিতে, ডেটা সাধারণত অপারেশনাল সিস্টেম থেকে বের করে একটি রিড-অনলি ডেটাবেস বা ডেটা ওয়্যারহাউসে রূপান্তরিত করা হয়, যা ব্যবহারকারী-বান্ধব স্কিমা সহ থাকে। এই পদ্ধতি নিশ্চিত করে যে ডেটা সুরক্ষিত, কর্মক্ষমতা এবং অ্যাক্সেসযোগ্যতার জন্য অপ্টিমাইজ করা হয়েছে এবং অ্যাপটির সীমিত, রিড-অনলি অ্যাক্সেস রয়েছে।

### টুল ব্যবহারের ডিজাইন প্যাটার্ন সম্পর্কে আরও প্রশ্ন আছে?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)-এ যোগ দিন, যেখানে আপনি অন্যান্য শিক্ষার্থীদের সাথে দেখা করতে পারেন, অফিস আওয়ার্সে অংশ নিতে পারেন এবং আপনার AI Agents সম্পর্কিত প্রশ্নের উত্তর পেতে পারেন।

## অতিরিক্ত সম্পদ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## পূর্ববর্তী পাঠ

[Agentic Design Patterns বোঝা](../03-agentic-design-patterns/README.md)

## পরবর্তী পাঠ

[Agentic RAG](../05-agentic-rag/README.md)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।