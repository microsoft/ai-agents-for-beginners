# মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক অন্বেষণ  

![Agent Framework](../../../translated_images/bn/lesson-14-thumbnail.90df0065b9d234ee.webp)

### পরিচিতি  

এই পাঠে আলোচনা করা হবে:  

- মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক: মূল বৈশিষ্ট্য ও মূল্য বোঝা  
- মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের প্রধান ধারণা অন্বেষণ  
- উন্নত MAF প্যাটার্নস: ওয়ার্কফ্লো, মিডলওয়্যার, এবং মেমরি  

## শেখার লক্ষ্য  

এই পাঠ শেষ করার পরে, আপনি জানতে পারবেন কীভাবে:  

- মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক ব্যবহার করে প্রোডাকশন রেডি AI এজেন্ট তৈরি করবেন  
- আপনার এজেন্টিক ব্যবহারের ক্ষেত্রে মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের মূল বৈশিষ্ট্য প্রয়োগ করবেন  
- উন্নত প্যাটার্নস ব্যবহার করবেন যেমন ওয়ার্কফ্লো, মিডলওয়্যার, এবং ওবজার্ভেবিলিটি  

## কোড উদাহরণ  

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) এর কোড নমুনা এই রিপোজিটরির `xx-python-agent-framework` এবং `xx-dotnet-agent-framework` ফাইলের মধ্যে পাওয়া যাবে।  

## মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক বোঝা  

![Framework Intro](../../../translated_images/bn/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) হলো AI এজেন্ট নির্মাণের জন্য মাইক্রোসফটের একক ফ্রেমওয়ার্ক। এটি প্রোডাকশন এবং গবেষণা উভয় ক্ষেত্রেই দেখা বিভিন্ন এজেন্টিক ব্যবহারের জন্য নমনীয়তা প্রদান করে, যেমন:  

- **ক্রমাগত এজেন্ট অর্কেস্ট্রেশন** যেখানে ধাপে ধাপে ওয়ার্কফ্লো প্রয়োজন।  
- **সমান্তরাল অর্কেস্ট্রেশন** যেখানে এজেন্টদের একসাথে কাজ সম্পন্ন করতে হয়।  
- **গ্রুপ চ্যাট অর্কেস্ট্রেশন** যেখানে এজেন্টরা একসঙ্গে একটি কাজ নিয়ে সহযোগিতা করে।  
- **হ্যান্ডঅফ অর্কেস্ট্রেশন** যেখানে এজেন্টরা উপ-কাজ শেষ হওয়ার সাথে সাথে কাজ একে অপরকে হস্তান্তর করে।  
- **ম্যাগনেটিক অর্কেস্ট্রেশন** যেখানে একটি ম্যানেজার এজেন্ট কাজের তালিকা তৈরি ও পরিবর্তন করে এবং উপ-এজেন্টদের সমন্বয় করে কাজ সম্পন্ন করে।  

প্রোডাকশনে AI এজেন্ট সরবরাহ করার জন্য, MAF এছাড়াও নিচের বৈশিষ্ট্যগুলো অন্তর্ভুক্ত করেছে:  

- **ওবজার্ভেবিলিটি** OpenTelemetry ব্যবহার করে যেখানে AI এজেন্টের প্রতিটি কাজ যেমন টুল কল, অর্কেস্ট্রেশন ধাপ, যুক্তি প্রবাহ এবং মাইক্রোসফট ফাউন্ড্রি ড্যাশবোর্ডের মাধ্যমে কর্মক্ষমতা পর্যবেক্ষণ করা হয়।  
- **সুরক্ষা** এজেন্টদের মাইক্রোসফট ফাউন্ড্রিতে স্বাভাবিকভাবে হোস্ট করার মাধ্যমে যেখানে ভূমিকা-ভিত্তিক প্রবেশাধিকার, ব্যক্তিগত ডেটা পরিচালনা এবং বিল্ট-ইন কনটেন্ট সেফটি রয়েছে।  
- **টেকসইতা** কারণ এজেন্ট থ্রেড এবং ওয়ার্কফ্লো স্থগিত, পুনরায় চালু এবং ত্রুটি থেকেও পুনরুদ্ধার করতে পারে, যা দীর্ঘ সময় ব্যাপী প্রক্রিয়া সম্ভব করে তোলে।  
- **নিয়ন্ত্রণ** যেখানে মানুষের প্রবেশিকা সাথে সম্পর্কিত ওয়ার্কফ্লো সমর্থিত, এবং কাজগুলো মানব অনুমোদনের জন্য চিহ্নিত থাকে।  

মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক আন্তঃঅপারেবল থেকেও মনোযোগ দেয়, যেমন:  

- **ক্লাউড-নিরপেক্ষ** - এজেন্টরা কনটেইনার, অন-প্রিম বা বিভিন্ন ক্লাউডে চালাতে পারে।  
- **প্রোভাইডার-নিরপেক্ষ** - পছন্দসই SDK (যেমন Azure OpenAI এবং OpenAI) ব্যবহার করে এজেন্ট তৈরি করা যায়।  
- **ওপেন স্ট্যান্ডার্ডস ইন্টিগ্রেশন** - Agent-to-Agent (A2A) এবং Model Context Protocol (MCP) মত প্রোটোকল ব্যবহার করে অন্যান্য এজেন্ট ও টুল আবিষ্কার এবং ব্যবহার করা যেতে পারে।  
- **প্লাগইন এবং কানেক্টরস** - Microsoft Fabric, SharePoint, Pinecone এবং Qdrant এর মতো ডেটা ও মেমরি সেবা সঙ্গে সংযোগ স্থাপন করা যায়।  

চলুন দেখলাম কিভাবে এগুলো মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের কিছু মূল ধারণায় প্রয়োগ করা হয়।  

## মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের মূল ধারণা  

### এজেন্টস  

![Agent Framework](../../../translated_images/bn/agent-components.410a06daf87b4fef.webp)

**এজেন্ট তৈরি করা**  

এজেন্ট তৈরি করা হয় ইনফারেন্স সার্ভিস (LLM প্রোভাইডার), AI এজেন্টের জন্য নির্দেশাবলী সেট এবং একটি বরাদ্দকৃত `name` দিয়ে:  


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

উপরের কোডে `Azure OpenAI` ব্যবহার করা হয়েছে, কিন্তু `Microsoft Foundry Agent Service` সহ বিভিন্ন সেবা দিয়ে এজেন্ট তৈরি করা যায়:  

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI এর `Responses`, `ChatCompletion` API  

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

অথবা [MiniMax](https://platform.minimaxi.com/), যা বড় কনটেক্সট উইন্ডো (২০৪কে টোকেন পর্যন্ত) সহ OpenAI-সামঞ্জস্যপূর্ণ API প্রদান করে:  

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

অথবা A2A প্রোটোকল ব্যবহার করে রিমোট এজেন্টস:  

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**এজেন্ট চালানো**  

এজেন্ট চালানো হয় `.run` বা `.run_stream` পদ্ধতি ব্যবহার করে, যা নন-স্ট্রিম বা স্ট্রিমিং রেসপন্সের জন্য।  

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

প্রতিটি এজেন্ট রান বিকল্প দিয়ে নির্দিষ্ট প্যারামিটার যেমন `max_tokens` যা এজেন্ট ব্যবহার করবে, `tools` যেগুলো এজেন্ট কল করতে পারবে, এমনকি এজেন্টের জন্য ব্যবহৃত `model` নির্ধারণ করতে দেয়।  

এটি বিশেষ মডেল বা টুলের প্রয়োজন হলে উপকারী।  

**টুলস**  

টুলস সংজ্ঞায়িত করা যেতে পারে এজেন্ট সংজ্ঞায়িত করার সময়:  

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# যখন সরাসরি একটি ChatAgent তৈরি করা হচ্ছে

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

এবং এজেন্ট চালানোর সময়ও:  

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # এই রানটির জন্য সরবরাহকৃত টুল )
```

**এজেন্ট থ্রেডস**  

মাল্টি-টার্ন কথোপকথন পরিচালনা করতে এজেন্ট থ্রেডস ব্যবহার করা হয়। থ্রেড তৈরি করা যেতে পারে:  

- `get_new_thread()` ব্যবহার করে যা সময়ের সঙ্গে থ্রেড সংরক্ষণে সক্ষম করে  
- অথবা এজেন্ট চালানোর সময় স্বয়ংক্রিয়ভাবে থ্রেড তৈরি করে যা শুধুমাত্র চলমান সেশনের জন্য থাকে।  

থ্রেড তৈরি করার কোড দেখতে এরকম:  

```python
# একটি নতুন থ্রেড তৈরি করুন।
thread = agent.get_new_thread() # থ্রেডের সাথে এজেন্ট চালান।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

পরে থ্রেড সিরিয়ালাইজ করে সংরক্ষণ করতে পারেন:  

```python
# একটি নতুন থ্রেড তৈরি করুন।
thread = agent.get_new_thread() 

# থ্রেডের সাথে এজেন্ট চালান।

response = await agent.run("Hello, how are you?", thread=thread) 

# সংরক্ষণের জন্য থ্রেড সিরিয়ালাইজ করুন।

serialized_thread = await thread.serialize() 

# সংরক্ষণ থেকে লোড করার পরে থ্রেডের অবস্থা ডেসিরিয়ালাইজ করুন।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**এজেন্ট মিডলওয়্যার**  

এজেন্টরা টুল ও LLM এর সাথে ইন্টারঅ্যাক্ট করে ব্যবহারকারীর কাজ সম্পন্ন করে। কিছু ক্ষেত্রে আমরা এই ইন্টারঅ্যাকশনের মাঝখানে কিছু চালাতে বা ট্র্যাক করতে চাই। এজেন্ট মিডলওয়্যার আমাদের এটি করতে দেয়:  

*ফাংশন মিডলওয়্যার*  

এই মিডলওয়্যার আমাদের এজেন্ট এবং ফাংশন/টুল কলের মাঝে একটি অ্যাকশন সম্পাদন করতে দেয়। উদাহরণস্বরূপ, ফাংশন কল লগিং।  

নিচের কোডে `next` নির্দেশ করে পরবর্তী মিডলওয়্যার অথবা আসল ফাংশন কল করা হবে কি না।  

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # প্রি-প্রসেসিং: ফাংশন সম্পাদনের আগে লগ করুন
    print(f"[Function] Calling {context.function.name}")

    # পরবর্তী মিডলওয়্যার বা ফাংশন সম্পাদনার জন্য চালিয়ে যান
    await next(context)

    # পোস্ট-প্রসেসিং: ফাংশন সম্পাদনার পরে লগ করুন
    print(f"[Function] {context.function.name} completed")
```

*চ্যাট মিডলওয়্যার*  

এই মিডলওয়্যার এজেন্ট ও LLM এর অনুরোধের মধ্যে অ্যাকশন চালানো বা লগিং করার সুযোগ দেয়।  

এটি AI সার্ভিসে পাঠানো `messages` এর মতো গুরুত্বপূর্ণ তথ্য ধারণ করে।  

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # প্রি-প্রসেসিং: AI কলের আগে লগ করুন
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # পরবর্তী মিডলওয়্যার বা AI সার্ভিসে এগিয়ে যান
    await next(context)

    # পোস্ট-প্রসেসিং: AI উত্তর পাওয়ার পর লগ করুন
    print("[Chat] AI response received")

```

**এজেন্ট মেমরি**  

`Agentic Memory` পাঠে আলোচনা অনুযায়ী, মেমরি এজেন্টকে বিভিন্ন প্রসঙ্গে কাজ করার সুযোগ দেয়। MAF বিভিন্ন ধরনের মেমরি অফার করে:  

*ইন-মেমরি স্টোরেজ*  

এটি অ্যাপ্লিকেশন রানটাইমে থ্রেডে সংরক্ষিত মেমরি।  

```python
# একটি নতুন থ্রেড তৈরি করুন।
thread = agent.get_new_thread() # থ্রেডের সাথে এজেন্ট চালান।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*পারসিস্টেন্ট মেসেজেস*  

বিভিন্ন সেশনের কথোপকথনের ইতিহাস সংরক্ষণে ব্যবহৃত মেমরি, যা `chat_message_store_factory` দিয়ে সংজ্ঞায়িত:  

```python
from agent_framework import ChatMessageStore

# একটি কাস্টম মেসেজ স্টোর তৈরি করুন
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ডায়নামিক মেমরি*  

এজেন্ট চালানোর আগে প্রসঙ্গে যোগ করা হয়। এটি বাহ্যিক সেবায় যেমন mem0 এ সংরক্ষিত হতে পারে:  

```python
from agent_framework.mem0 import Mem0Provider

# উন্নত মেমরি সক্ষমতার জন্য Mem0 ব্যবহার করা হচ্ছে
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**এজেন্ট ওবজার্ভেবিলিটি**  

নির্ভরযোগ্য এবং রক্ষণাবেক্ষণযোগ্য এজেন্টিক সিস্টেম নির্মাণে ওবজার্ভেবিলিটি গুরুত্বপূর্ণ। MAF OpenTelemetry এর সাথে ইন্টিগ্রেট করে ট্রেসিং ও মিটার প্রদান করে।  

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # কিছু করো
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### ওয়ার্কফ্লো  

MAF ওয়ার্কফ্লো অফার করে, যা পূর্ব নির্ধারিত ধাপসমূহের মাধ্যমে কাজ সম্পন্ন করে এবং সেই ধাপে AI এজেন্ট থাকে।  

ওয়ার্কফ্লো বিভিন্ন উপাদানের সমন্বয়ে গঠিত যা উন্নত নিয়ন্ত্রণ প্রবাহ দেয়। ওয়ার্কফ্লো **মাল্টি-এজেন্ট অর্কেস্ট্রেশন** এবং **চেকপয়েন্টিং** সমর্থন করে ওয়ার্কফ্লো অবস্থান সংরক্ষণ করতে।  

একটি ওয়ার্কফ্লোর প্রধান উপাদান হলো:  

**এক্সিকিউটরস**  

ইনপুট মেসেজ গ্রহণ করে, নির্ধারিত কাজ সম্পাদন করে এবং আউটপুট মেসেজ তৈরি করে। এটি ওয়ার্কফ্লোকে বড় কাজের প্রতি এগিয়ে নিয়ে যায়। এক্সিকিউটর AI এজেন্ট অথবা কাস্টম লজিক হতে পারে।  

**এজেস**  

ওয়ার্কফ্লোতে মেসেজের প্রবাহ নির্ধারণ করতে এজেস ব্যবহার হয়। এগুলো হতে পারে:  

*সরাসরি এজেস* - এক্সিকিউটরদের মধ্যে সরল এক থেকে এক সংযোগ:  

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*শর্তাধীন এজেস* - নির্দিষ্ট শর্ত পূরণ হলে সক্রিয় হয়। উদাহরণস্বরূপ, হোটেলের কক্ষ না থাকলে বিকল্প সুপারিশ করে।  

*সুইচ-কেস এজেস* - নির্ধারিত শর্ত অনুযায়ী মেসেজ বিভিন্ন এক্সিকিউটরের দিকে রুট করে। উদাহরণস্বরূপ, যাত্রী যদি অগ্রাধিকার অ্যাক্সেস পায়, তাদের কাজ অন্য ওয়ার্কফ্লোর মাধ্যমে করা হবে।  

*ফ্যান-আউট এজেস* - এক মেসেজ একাধিক লক্ষ্যস্থলের কাছে পাঠায়।  

*ফ্যান-ইন এজেস* - বিভিন্ন এক্সিকিউটর থেকে একাধিক মেসেজ সংগ্রহ করে একটি লক্ষ্যস্থলের কাছে পাঠায়।  

**ইভেন্টস**  

উন্নত ওবজার্ভেবিলিটির জন্য, MAF ওয়ার্কফ্লোর জন্য বিল্ট-ইন ইভেন্ট প্রদান করে, যেমন:  

- `WorkflowStartedEvent` - ওয়ার্কফ্লোর একজিকিউশন শুরু  
- `WorkflowOutputEvent` - ওয়ার্কফ্লো আউটপুট তৈরি করে  
- `WorkflowErrorEvent` - ওয়ার্কফ্লো ত্রুটির সম্মুখীন হয়  
- `ExecutorInvokeEvent` - এক্সিকিউটর প্রক্রিয়াকরণ শুরু করে  
- `ExecutorCompleteEvent` - এক্সিকিউটর প্রক্রিয়াকরণ শেষ করে  
- `RequestInfoEvent` - একটি রিকোয়েস্ট জারি হয়  

## উন্নত MAF প্যাটার্নস  

উপরের অংশে মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের মূল ধারণা আলোচনা হয়েছে। আরও জটিল এজেন্ট তৈরির জন্য কিছু উন্নত প্যাটার্নস:  

- **মিডলওয়্যার কম্পোজিশন**: একাধিক মিডলওয়্যার হ্যান্ডলার (লগিং, অথ, রেট-লিমিটিং) ফাংশন ও চ্যাট মিডলওয়্যারের মাধ্যমে যুক্ত করুন এজেন্ট আচরণের সূক্ষ্ম নিয়ন্ত্রণের জন্য।  
- **ওয়ার্কফ্লো চেকপয়েন্টিং**: ওয়ার্কফ্লো ইভেন্ট এবং সিরিয়ালাইজেশন ব্যবহার করে দীর্ঘমেয়াদী এজেন্ট প্রক্রিয়া সংরক্ষণ ও পুনরায় শুরু করুন।  
- **ডায়নামিক টুল সিলেকশন**: টুল বিবরণীর উপর RAG ও MAF টুল নিবন্ধন একত্রিত করে শুধুমাত্র প্রাসঙ্গিক টুল প্রদর্শন করুন।  
- **মাল্টি-এজেন্ট হ্যান্ডঅফ**: স্পেশালাইজড এজেন্টদের মধ্যে হ্যান্ডঅফ অর্কেস্ট্রেট করতে ওয়ার্কফ্লো এজ এবং শর্তাধীন রাউটিং ব্যবহার করুন।  

## মাইক্রোসফট ফাউন্ড্রিতে LangChain / LangGraph এজেন্ট হোস্টিং  

মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক **ফ্রেমওয়ার্ক-ইন্টারঅপারেবল** — আপনি শুধুমাত্র MAF দিয়ে তৈরি এজেন্টে সীমাবদ্ধ নন। আগেই যদি আপনার কাছে **LangChain** অথবা **LangGraph** এজেন্ট থাকে, আপনি এটিকে **মাইক্রোসফট ফাউন্ড্রি হোস্টেড এজেন্ট** হিসেবে চালাতে পারেন যেখানে ফাউন্ড্রি_runtime, সেশন, স্কেলিং, আইডেন্টিটি এবং প্রোটোকল এন্ডপয়েন্ট ব্যবস্থাপনা করে, আর আপনার এজেন্ট লজিক LangGraph এ থাকে।  

এটি করা হয় `langchain_azure_ai.agents.hosting` প্যাকেজের মাধ্যমে, যা প্রস্তুত LangGraph গ্রাফ একত্রিত করে ফাউন্ড্রি হোস্টেড এজেন্টের মত প্রোটোকল ব্যবহার করে।  

**১. হোস্টিং এক্সট্রা ইনস্টল করুন:**  

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` এক্সট্রা Foundry প্রোটোকল লাইব্রেরি ইনস্টল করে: `azure-ai-agentserver-responses` (OpenAI-সামঞ্জস্যপূর্ণ `/responses` এন্ডপয়েন্ট) এবং `azure-ai-agentserver-invocations` (সাধারণ `/invocations` এন্ডপয়েন্ট)।  

**২. হোস্টিং প্রোটোকল নির্বাচন করুন:**  

| প্রোটোকল | হোস্ট ক্লাস | এন্ডপয়েন্ট | ব্যবহারের সময় |  
|----------|-----------|----------|----------|  
| **Responses** | `ResponsesHostServer` | `/responses` | আপনি OpenAI-সামঞ্জস্যপূর্ণ চ্যাট, স্ট্রিমিং, রেসপন্স ইতিহাস, এবং কথোপকথন থ্রেডিং চান— যা কথোপকথন এজেন্টের জন্য সুপারিশকৃত ডিফল্ট। |  
| **Invocations** | `InvocationsHostServer` | `/invocations` | কাস্টম JSON শেপ, ওয়েবহুক-স্টাইল এন্ডপয়েন্ট, বা অ-কথোপকথন প্রক্রিয়াকরণ দরকার হলে। |  

যেহেতু **Responses API হলো Foundry-তে এজেন্ট-স্টাইল ডেভেলপমেন্টের প্রধান API**, বেশিরভাগ এজেন্টের জন্য `ResponsesHostServer` দিয়ে শুরু করুন।  

**৩. পরিবেশ ভেরিয়েবল কনফিগার করুন** (`az login` আগে করুন যাতে `DefaultAzureCredential` প্রমাণীকরণ করতে পারে):  

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

পরে যখন এজেন্ট ফাউন্ড্রি হোস্টেড এজেন্ট হিসেবে চলবে, প্ল্যাটফর্ম স্বয়ংক্রিয়ভাবে `FOUNDRY_PROJECT_ENDPOINT` ইনজেক্ট করে।  

**৪. Responses প্রোটোকলের ওপর LangGraph এজেন্ট এক্সপোজ করুন:**  

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI এখানে Foundry প্রকল্পের OpenAI-সঙ্গতিপূর্ণ (Responses) এন্ডপয়েন্ট লক্ষ্য করে।
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

লোকালিতে `python main.py` দিয়ে চালান, তারপর `http://localhost:8088/responses` এ Responses রিকুয়েস্ট পাঠান।  

**মূল আচরণ:**  

- **কথোপকথন**: ক্লায়েন্টরা `previous_response_id` অথবা `conversation` আইডি প্রদান করে কথোপকথন অব্যাহত রাখে। গ্রাফ LangGraph চেকপয়েন্টার দিয়ে কম্পাইল হলে, ফাউন্ড্রি কথোপকথন অবস্থা চেকপয়েন্টের সাথে যুক্ত করে (প্রোডাকশনে টেকসই চেকপয়েন্টার ব্যবহার করুন; লোকাল টেস্টিং এর জন্য `MemorySaver` উপযুক্ত)।  
- **মানব-ইন-লুপ**: যদি গ্রাফ LangGraph `interrupt()` ব্যবহার করে, `ResponsesHostServer` পেন্ডিং ইন্টারাপ্টকে Responses এর `function_call` / `mcp_approval_request` আইটেম হিসেবে দেখায়, এবং ক্লায়েন্ট মিলানো `function_call_output` / `mcp_approval_response` দিয়ে পুনরায় শুরু করে।  
- **Foundry এ ডিপ্লয় করুন**: Azure Developer CLI ব্যবহার করুন — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (লোকাল, Docker প্রয়োজন), তারপর `azd provision` এবং `azd deploy`। হোস্টেড এজেন্ট ডিপ্লয়মেন্টের জন্য **Foundry Project Manager** ভূমিকা থাকা বাধ্যতামূলক।  

এই উদাহরণের চালনাযোগ্য সংস্করণ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) এ রয়েছেঃ সম্পূর্ণ ওয়াকথ্রু (Invocations প্রোটোকল, কাস্টম রিকুয়েস্ট স্কিমা, এবং সমস্যা সমাধান) জন্য দেখুন [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)।  

## কোড নমুনা  

মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের কোড নমুনা এই রিপোজিটরির `xx-python-agent-framework` এবং `xx-dotnet-agent-framework` ফাইলের মধ্যে পাওয়া যাবে।  

## মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক সম্পর্কে আরও প্রশ্ন?  

অন্যান্য শিক্ষার্থীদের সাথে মেলামেশা, অফিস আওয়ার অংশগ্রহণ এবং AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পাওয়ার জন্য [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) এ যোগ দিন।  
## পূর্ববর্তী পাঠ  

[AI এজেন্টের জন্য মেমরি](../13-agent-memory/README.md)  

## পরবর্তী পাঠ  

[কম্পিউটার ইউজ এজেন্ট নির্মাণ (CUA)](../15-browser-use/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->