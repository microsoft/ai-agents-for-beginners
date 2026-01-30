[![How to Design Good AI Agents](../../../translated_images/bn/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(এই পাঠের ভিডিও দেখতে উপরের ছবিতে ক্লিক করুন)_

# টুল ইউজ ডিজাইন প্যাটার্ন

টুলগুলি আকর্ষণীয় কারণ এগুলো AI এজেন্টদের বিস্তৃত পরিসরের ক্ষমতা প্রদান করে। এজেন্টের যদি সীমিত কর্মসূচি থাকে, তবে একটি টুল যোগ করার মাধ্যমে এজেন্ট এখন বিস্তৃত কার্য সম্পাদন করতে পারে। এই অধ্যায়ে, আমরা টুল ইউজ ডিজাইন প্যাটার্ন সম্পর্কে আলোচনা করব, যা বর্ণনা করে কীভাবে AI এজেন্টরা নির্দিষ্ট টুল ব্যবহার করে তাদের লক্ষ্য অর্জন করতে পারে।

## পরিচিতি

এই পাঠে, আমরা নিম্নলিখিত প্রশ্নগুলোর উত্তর জানার চেষ্টা করব:

- টুল ইউজ ডিজাইন প্যাটার্ন কী?
- এটি কোন কোন ব্যবহারের ক্ষেত্রে প্রযোজ্য?
- ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য কী কী উপাদান/বিল্ডিং ব্লক প্রয়োজন?
- বিশ্বাসযোগ্য AI এজেন্ট তৈরি করার জন্য টুল ইউজ ডিজাইন প্যাটার্ন ব্যবহারের বিশেষ বিবেচ্য বিষয় কী কী?

## শেখার লক্ষ্য

এই পাঠ শেষ করার পর, আপনি সক্ষম হবেন:

- টুল ইউজ ডিজাইন প্যাটার্ন এবং এর উদ্দেশ্য সংজ্ঞায়িত করতে।
- কোন কোন ব্যবহারে টুল ইউজ ডিজাইন প্যাটার্ন প্রযোজ্য তা চিহ্নিত করতে।
- ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় মূল উপাদান বুঝতে।
- এই ডিজাইন প্যাটার্ন ব্যবহার করে AI এজেন্টের বিশ্বাসযোগ্যতা নিশ্চিত করার বিবেচ্য বিষয় চিনতে।

## টুল ইউজ ডিজাইন প্যাটার্ন কী?

**টুল ইউজ ডিজাইন প্যাটার্ন** মূলত LLM-দের বাহ্যিক টুলের সাথে ইন্টারঅ্যাক্ট করার ক্ষমতা দেয় নির্দিষ্ট লক্ষ্য অর্জনের জন্য। টুল হল এমন কোড যা এজেন্ট কোনো কাজ সম্পাদনের জন্য চালাতে পারে। একটি টুল হতে পারে একটি সরল ফাংশন, যেমন ক্যালকুলেটর, অথবা তৃতীয় পক্ষের সেবার API কল, যেমন স্টক দাম বা আবহাওয়ার পূর্বাভাস। AI এজেন্টের প্রেক্ষাপটে, টুলগুলো ডিজাইন করা হয় যাতে এজেন্টরা **মডেল-সৃষ্ট ফাংশন কলের** জবাবে সেগুলো চালাতে পারে।

## এটি কোন কোন ব্যবহারের ক্ষেত্রে প্রয়োগ করা যায়?

AI এজেন্টরা টুল ব্যবহার করে জটিল কাজ সম্পন্ন করতে, তথ্য সংগ্রহ করতে, অথবা সিদ্ধান্ত নিতে পারে। টুল ইউজ ডিজাইন প্যাটার্ন প্রধানত এমন পরিস্থিতিতে ব্যবহৃত হয় যেখানে বাহ্যিক সিস্টেমের সাথে গতিশীল ইন্টারঅ্যাকশনের প্রয়োজন, যেমন ডেটাবেস, ওয়েব সেবা, বা কোড ইন্টারপ্রিটার। এই ক্ষমতা অনেক ব্যবহারের ক্ষেত্রে উপকারী, এদের মধ্যে:

- **গতিশীল তথ্য আহরণ:** এজেন্টরা বাহ্যিক API বা ডেটাবেস থেকে সর্বশেষ তথ্য সংগ্রহ করতে পারে (যেমন, ডেটা বিশ্লেষণের জন্য SQLite ডেটাবেসে প্রশ্ন, স্টক দাম বা আবহাওয়ার তথ্য সংগ্রহ)।
- **কোড কার্যকরকরণ ও ব্যাখ্যা:** এজেন্টরা কোড বা স্ক্রিপ্ট চালিয়ে গণিত সমস্যার সমাধান, রিপোর্ট তৈরী, বা সিমুলেশন করতে পারে।
- **ওয়ার্কফ্লো অটোমেশন:** টুল যেমন টাস্ক শিডিউলার, ইমেইল সেবা, বা ডেটা পাইপলাইন একত্রিত করে পুনরাবৃত্ত বা বহু-ধাপে ওয়ার্কফ্লো অটোমেট করা।
- **গ্রাহক সেবা:** এজেন্টরা CRM সিস্টেম, টিকিটিং প্ল্যাটফর্ম, অথবা তথ্যভাণ্ডারের সাথে ইন্টারঅ্যাক্ট করে ব্যবহারকারীর প্রশ্ন সমাধান করতে পারে।
- **কন্টেন্ট তৈরী ও সম্পাদনা:** গ্রামার চেকার, টেক্সট সামারাইজার, বা কন্টেন্ট সেফটি মূল্যায়নকারী টুল ব্যবহার করে এজেন্টরা কন্টেন্ট তৈরীতে সহায়তা করতে পারে।

## টুল ইউজ ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য কী উপাদান/বিল্ডিং ব্লক প্রয়োজন?

এই বিল্ডিং ব্লকগুলো AI এজেন্টকে বিভিন্ন কাজ সম্পাদন করতে সাহায্য করে। চলুন টুল ইউজ ডিজাইন প্যাটার্ন বাস্তবায়নের মূল উপাদানগুলো দেখি:

- **ফাংশন/টুল স্কিমা**: উপলব্ধ টুলগুলোর বিস্তারিত সংজ্ঞা, যেমন ফাংশনের নাম, উদ্দেশ্য, প্রয়োজনীয় প্যারামিটার, ও প্রত্যাশিত আউটপুট। এই স্কিমাগুলো LLM-কে বোঝায় কী টুল রয়েছে এবং সঠিক অনুরোধ কিভাবে তৈরি করতে হবে।

- **ফাংশন কার্যকরীকরণের লজিক**: ব্যবহারকারীর উদ্দেশ্য ও কথোপকথনের প্রেক্ষাপটে কখন ও কিভাবে টুল ডাকা হবে তা নিয়ন্ত্রণ করে। এতে প্ল্যানার মডিউল, রাউটিং মেকানিজম, বা শর্তাধীন প্রবাহ অন্তর্ভুক্ত থাকতে পারে যা গতিশীলভাবে টুল ব্যবহারের সিদ্ধান্ত নেয়।

- **মেসেজ হ্যান্ডলিং সিস্টেম**: ব্যবহারকারীর ইনপুট, LLM-এর প্রতিক্রিয়া, টুল কল, ও টুল আউটপুটের মধ্যে কথোপকথনের প্রবাহ পরিচালনা করে।

- **টুল ইন্টিগ্রেশন ফ্রেমওয়ার্ক**: এজেন্টকে বিভিন্ন টুলের সাথে সংযোগ করানোর জন্য অবকাঠামো, সেগুলো সরল ফাংশন হোক বা জটিল বাহ্যিক ব্যবস্থা।

- **ত্রুটি হ্যান্ডলিং ও ভ্যালিডেশন**: টুল কার্যকরকরণে ব্যর্থতা মোকাবেলা, প্যারামিটার যাচাই, এবং অপ্রত্যাশিত প্রতিক্রিয়া ব্যবস্থাপনা।

- **স্টেট ম্যানেজমেন্ট**: কথোপকথনের প্রেক্ষাপট, পূর্ববর্তী টুল ইন্টারঅ্যাকশন, ও স্থায়ী ডেটা লিপিবদ্ধ করে যাতে বহুযুগ্ম কথোপকথনে সামঞ্জস্য বজায় থাকে।

এরপর, Function/Tool Calling বিস্তারিতভাবে দেখব।

### Function/Tool Calling

ফাংশন কলিং হল বড় ভাষা মডেল (LLM) কে টুলের সাথে ইন্টারঅ্যাক্ট করার প্রধান মাধ্যম। আপনি প্রায়ই 'ফাংশন' ও 'টুল' পরস্পর বদলে ব্যবহৃত দেখতে পাবেন কারণ 'ফাংশন' (পুনর্ব্যবহারযোগ্য কোড ব্লক) হচ্ছে সেই 'টুল' যা এজেন্টরা কাজ সম্পাদনে ব্যবহার করে। একটি ফাংশনের কোড কল করার জন্য, LLM ব্যবহারকারীর অনুরোধের সঙ্গে ফাংশনের বর্ণনা তুলনা করে। এজন্য একটি স্কিমা তৈরি করা হয় যেখানে সব উপলব্ধ ফাংশনের বর্ণনা থাকে এবং সেটি LLM-এ পাঠানো হয়। তারপর LLM কাজের জন্য সবচেয়ে উপযুক্ত ফাংশন নির্বাচন করে তার নাম ও আর্গুমেন্টস ফেরত দেয়। নির্বাচিত ফাংশন কল হয়, তার প্রতিক্রিয়া LLM-এ ফিরে যায়, এবং LLM তা ব্যবহারকারীর অনুরোধের জবাবে রূপান্তর করে।

এজেন্টের জন্য ফাংশন কলিং বাস্তবায়ন করতে, প্রয়োজন:

1. ফাংশন কলিং সমর্থিত একটি LLM মডেল
2. ফাংশন বর্ণনা সম্বলিত স্কিমা
3. প্রতিটি বর্ণিত ফাংশনের কোড

একটি শহরের বর্তমান সময় জানার উদাহরণ দিয়ে বোঝাচ্ছি:

1. **ফাংশন কলিং সমর্থিত একটি LLM ইনিশিয়ালাইজ করুন:**

    সব মডেল ফাংশন কলিং সমর্থন করে না, তাই নিশ্চিত হতে হবে যে আপনার ব্যবহার করা LLM তা করে। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ফাংশন কলিং সমর্থন করে। আমরা Azure OpenAI ক্লায়েন্ট ইনিশিয়ালাইজ করে শুরু করতে পারি। 

    ```python
    # Azure OpenAI ক্লায়েন্ট শুরু করুন
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **একটি ফাংশন স্কিমা তৈরি করুন**:

    এরপর আমরা একটি JSON স্কিমা সংজ্ঞায়িত করব যেখানে ফাংশনের নাম, ফাংশন কী করে তার বর্ণনা, এবং ফাংশন প্যারামিটারগুলোর নাম ও বর্ণনা থাকবে।
    তারপর এই স্কিমাটি আগের ক্লায়েন্টকে পাঠাবো, ব্যবহারকারীর সান ফ্রান্সিসকো শহরের সময় জানতে চাওয়ার অনুরোধের সাথে। গুরুত্বপূর্ণ বিষয় হল একটি **টুল কল** ফেরত দেয়া হয়, **প্রশ্নের চূড়ান্ত উত্তর নয়**। আগেই উল্লেখ ছিল, LLM কাজের জন্য সবচেয়ে উপযুক্ত ফাংশনের নাম ও আর্গুমেন্ট ফেরত দেয়।

    ```python
    # মডেল পড়ার জন্য ফাংশন বর্ণনা
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
  
    # প্রথম এপিআই কল: মডেলকে ফাংশনটি ব্যবহার করতে বলুন
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # মডেলের প্রতিক্রিয়া প্রক্রিয়াজাত করুন
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **কাজটি করার জন্য প্রয়োজনীয় ফাংশন কোড:**

    এখন LLM ফাংশন নির্বাচন করেছে, কাজটি করার কোড বাস্তবায়ন ও চালানো দরকার।
    আমরা পাইথনে বর্তমান সময় পাওয়ার কোড লিখতে পারি। এছাড়াও response_message থেকে নাম ও আর্গুমেন্ট বার করার কোড থাকতে হবে চূড়ান্ত ফলাফল পাওয়ার জন্য।

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

ফাংশন কলিং বেশিরভাগ এজেন্ট টুল ইউজ ডিজাইনের মূল, যদিও এটি স্ক্র্যাচ থেকে বাস্তবায়ন করা কিছু সময় চ্যালেঞ্জিং হতে পারে।
আমরা শিখেছি [Lesson 2](../../../02-explore-agentic-frameworks) এজেন্টিক ফ্রেমওয়ার্কগুলো আগে থেকেই প্রস্তুত বিল্ডিং ব্লক সরবরাহ করে টুল ইউজ বাস্তবায়নের জন্য।

## এজেন্টিক ফ্রেমওয়ার্ক দিয়ে টুল ইউজ উদাহরণসমূহ

বিভিন্ন এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করে কীভাবে টুল ইউজ ডিজাইন প্যাটার্ন প্রয়োগ করতে হয় তার কিছু উদাহরণ:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> একটি ওপেন-সোর্স AI ফ্রেমওয়ার্ক .NET, পাইথন, ও জাভা ডেভেলপারদের জন্য যারা বড় ভাষা মডেলের সঙ্গে কাজ করেন। এটি ফাংশন কলিং প্রক্রিয়া সহজ করে, স্বয়ংক্রিয়ভাবে আপনার ফাংশন ও তাদের প্যারামিটারগুলি মডেলের কাছে <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">সিরিয়ালাইজিং</a> এর মাধ্যমে বর্ণনা করে। এটি মডেল ও কোডের মধ্যে দ্বিমুখী যোগাযোগও হ্যান্ডেল করে। Semantic Kernel-এর মতো এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করার আরেক উপকারিতা হল, আপনি আগে থেকেই তৈরি টুল যেমন <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> এবং <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a> অ্যাক্সেস করতে পারেন।

নিচের চিত্রটি Semantic Kernel-এর ফাংশন কলিং প্রক্রিয়ার চিত্রায়ন:

![function calling](../../../translated_images/bn/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernel-এ ফাংশন/টুলকে <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">প্লাগইন</a> বলা হয়। আগের দেখানো `get_current_time` ফাংশন প্লাগইনে রূপান্তর করতে পারি, এটি একটি ক্লাসে পরিণত করে যার মধ্যে ফাংশন থাকে। এছাড়াও `kernel_function` ডেকোরেটর ইম্পোর্ট করতে পারি যা ফাংশনের বর্ণনা গ্রহণ করে। এরপর GetCurrentTimePlugin দিয়ে kernel তৈরি করার সময় kernel স্বয়ংক্রিয়ভাবে ফাংশন ও প্যারামিটার সিরিয়ালাইজ করে, স্কিমা তৈরি করে LLM-এ পাঠায়।

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

# কার্নেল তৈরি করুন
kernel = Kernel()

# প্লাগইন তৈরি করুন
get_current_time_plugin = GetCurrentTimePlugin(location)

# কার্নেলে প্লাগইন যোগ করুন
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> একটি নতুন এজেন্টিক ফ্রেমওয়ার্ক যা ডেভেলপারদের নিরাপদে উচ্চমানের, সম্প্রসারযোগ্য AI এজেন্ট তৈরি, ডিপ্লয়, ও স্কেল করতে সহায়তা করে, যেগুলোর বেসিক কম্পিউট ও স্টোরেজ রিসোর্স ম্যানেজ করার দরকার হয় না। এটি বিশেষত এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য উপযোগী কারণ এটি সম্পূর্ণ ম্যানেজড সার্ভিস ও এন্টারপ্রাইজ গ্রেড নিরাপত্তা প্রদান করে।

সরাসরি LLM API’র থেকে উন্নত হিসাবে Azure AI Agent Service কিছু সুবিধা দেয়, যেমন:

- স্বয়ংক্রিয় টুল কলিং – টুল কল পার্স করা, টুল কল করা, ও রেসপন্স পরিচালনার দরকার নেই; সব কিছু সার্ভার সাইডে করা হয়
- নিরাপদভাবে ম্যানেজড ডেটা – নিজস্ব কথোপকথন স্টেট ম্যানেজ না করে থ্রেডের সাহায্যে তথ্য সংরক্ষণ করা যায়
- সরবরাহকৃত টুলস – Bing, Azure AI Search, ও Azure Functions-এর মত ডেটা সোর্সের সঙ্গে ইন্টারঅ্যাক্ট করার জন্য টুলস প্রদান করে।

Azure AI Agent Service-এর টুল দুটি শ্রেণিতে ভাগ করা যায়:

1. জ্ঞান টুলস:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. ক্রিয়াকলাপ টুলস:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

এজেন্ট সার্ভিস আমাদেরকে এই টুলগুলোকে `toolset` হিসেবে ব্যবহার করতে দেয়। এছাড়াও এটি `threads` ব্যবহার করে যা নির্দিষ্ট কথোপকথনের বার্তার ইতিহাস ট্র্যাক করে।

ভাবুন আপনি Contoso নামক কোম্পানিতে একজন বিক্রয় এজেন্ট। আপনি এমন একটি কথোপকথন এজেন্ট ডেভেলপ করতে চান যা আপনার বিক্রয় ডেটা নিয়ে প্রশ্নের উত্তর দিতে পারে।

নিম্নলিখিত চিত্রে দেখা যায় কিভাবে Azure AI Agent Service ব্যবহার করে আপনার বিক্রয় ডেটা বিশ্লেষণ করতে পারেন:

![Agentic Service In Action](../../../translated_images/bn/agent-service-in-action.34fb465c9a84659e.webp)

এই টুলগুলো সার্ভিসের সঙ্গে ব্যবহার করতে ক্লায়েন্ট তৈরি করে টুল বা টুলসেট নির্ধারণ করতে পারেন। বাস্তবায়নের জন্য নিম্নলিখিত পাইথন কোড ব্যবহার করা যেতে পারে। LLM টুলসেট দেখে নির্ধারণ করবে ব্যবহারকারীর অনুরোধ অনুযায়ী নিজস্ব ফাংশন `fetch_sales_data_using_sqlite_query` অথবা প্রি-বিল্ট কোড ইন্টারপ্রিটার ব্যবহার করা উচিত কিনা।

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

# fetch_sales_data_using_sqlite_query ফাংশন সহ ফাংশন কলিং এজেন্ট আরম্ভ করুন এবং এটি টুলসেটে যোগ করুন
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# কোড ইন্টারপ্রেটার টুল আরম্ভ করুন এবং এটি টুলসেটে যোগ করুন।
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## বিশ্বাসযোগ্য AI এজেন্ট তৈরির জন্য টুল ইউজ ডিজাইন প্যাটার্ন ব্যবহারের বিশেষ বিবেচ্য বিষয় কী?

LLM দ্বারা গতিশীলভাবে তৈরি হওয়া SQL-এ নিরাপত্তার উদ্বেগ থাকে, বিশেষ করে SQL ইনজেকশন বা ক্ষতিকারক কাজের ঝুঁকি, যেমন ডাটাবেস ড্রপ করা বা পরিবর্তন করা। যদিও এই উদ্বেগগুলো যুক্তিযুক্ত, সঠিকভাবে ডাটাবেস অ্যাক্সেস পারমিশন কনফিগার করলে এগুলো কার্যকরভাবে প্রতিরোধ করা যায়। অধিকাংশ ডাটাবেসে এটি রিড-ওনলি মোডে কনফিগার করার মাধ্যমে করা হয়। PostgreSQL বা Azure SQL মত ডাটাবেস সেবার ক্ষেত্রে, অ্যাপ্লিকেশনটিকে রিড-ওনলি (SELECT) রোল দেয়া উচিত।
অ্যাপটি একটি সুরক্ষিত পরিবেশে চালানো আরও নিরাপত্তা বৃদ্ধি করে। এন্টারপ্রাইজ পরিস্থিতিতে, সাধারণত ডেটা অপারেশনাল সিস্টেম থেকে নিষ্কাশিত এবং রূপান্তরিত হয়ে পড়াশুনার জন্য একটি পড়ার মাত্র ডাটাবেজ বা ডেটা ওয়্যারহাউসে স্থানান্তরিত হয়, যা একটি ব্যবহারকারী-বান্ধব স্কিমা সহ থাকে। এই পদ্ধতি নিশ্চিত করে যে ডেটা সুরক্ষিত, পারফরম্যান্স এবং অ্যাক্সেসিবিলিটির জন্য অপ্টিমাইজড, এবং অ্যাপটির সীমাবদ্ধ, শুধুমাত্র-পঠিত অ্যাক্সেস রয়েছে।

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**দ্বিপক্ষীয় বিবৃতি**:
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসম্ভব সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে তা দয়া করে মনে রাখবেন। মূল নথিটি তার নিজস্ব ভাষায় প্রামাণিক উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->