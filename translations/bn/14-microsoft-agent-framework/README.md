# মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্ক অন্বেষণ

![Agent Framework](../../../translated_images/bn/lesson-14-thumbnail.90df0065b9d234ee.webp)

### ভূমিকা

এই পাঠে আলোচনা করা হবে:

- মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্ক বোঝা: মূল বৈশিষ্ট্য এবং মান  
- মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্কের মূল ধারণা অনুসন্ধান
- উন্নত MAF প্যাটার্ন: ওয়ার্কফ্লো, মিডলওয়্যার, এবং মেমোরি

## শেখার লক্ষ্য

এই পাঠ শেষ করার পরে, আপনি জানতে পারবেন:

- মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্ক ব্যবহার করে প্রোডাকশন প্রস্তুত AI এজেন্ট তৈরি করা
- আপনার এজেন্টিক ইউজ কেসে মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্কের মূল বৈশিষ্ট্য প্রয়োগ করা
- উন্নত প্যাটার্ন যেমন ওয়ার্কফ্লো, মিডলওয়্যার, এবং পর্যবেক্ষণ ব্যবহার করা

## কোড স্যাম্পল

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) এর কোড স্যাম্পল এই রিপোজিটরিতে `xx-python-agent-framework` এবং `xx-dotnet-agent-framework` ফাইলগুলির মধ্যে পাওয়া যাবে।

## মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্ক বোঝা

![Framework Intro](../../../translated_images/bn/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) হল মাইক্রোসফ্টের একত্রিত ফ্রেমওয়ার্ক AI এজেন্ট নির্মাণের জন্য। এটি প্রোডাকশন এবং গবেষণা পরিবেশে দেখা বিভিন্ন এজেন্টিক ইউজ কেস সম্পাদনের জন্য নমনীয়তা প্রদান করে, যেখানে অন্তর্ভুক্ত:

- **ক্রমবর্ধক এজেন্ট অর্কেস্ট্রেশন** যেখানে ধাপে ধাপে ওয়ার্কফ্লো প্রয়োজন।
- **সঞ্চালিত অর্কেস্ট্রেশন** যেখানে এজেন্টরা একই সময়ে কাজ সম্পন্ন করতে পারে।
- **গ্রুপ চ্যাট অর্কেস্ট্রেশন** যেখানে এজেন্টরা একসাথে একটি কাজের উপর সহযোগিতা করতে পারে।
- **হ্যান্ডঅফ অর্কেস্ট্রেশন** যেখানে এজেন্টরা উপ-কার্যগুলি শেষ করার সঙ্গে কাজ একে অপরের কাছে হস্তান্তর করে।
- **ম্যাগনেটিক অর্কেস্ট্রেশন** যেখানে একটি ম্যানেজার এজেন্ট একটি কাজের তালিকা তৈরি ও সংশোধন করে এবং উপ-এজেন্টদের সমন্বয় করে কাজ সম্পন্ন করে।

প্রোডাকশনে AI এজেন্ট সরবরাহ করার জন্য MAF তে অন্তর্ভুক্ত বৈশিষ্ট্যসমূহ:

- **পর্যবেক্ষণযোগ্যতা** OpenTelemetry এর মাধ্যমে যেখানে AI এজেন্টের প্রতিটি ক্রিয়া যেমন টুল আহ্বান, অর্কেস্ট্রেশন ধাপ, যুক্তি প্রবাহ এবং কার্যক্ষমতা মনিটরিং Microsoft Foundry ড্যাশবোর্ডের মাধ্যমে ট্র্যাক করা হয়।
- **নিরাপত্তা** Microsoft Foundry তে নেটিভ এজেন্ট হোস্টিং সহ যা রোল-ভিত্তিক অ্যাক্সেস, ব্যক্তিগত ডেটা পরিচালনা এবং বিল্ট-ইন কন্টেন্ট সেফটির মতো নিরাপত্তা নিয়ন্ত্রণ অন্তর্ভুক্ত।
- **স্থায়িত্ব** কারণ এজেন্ট থ্রেড এবং ওয়ার্কফ্লো পজ, রিজুম এবং ত্রুটি পুনরুদ্ধার করতে পারে, যা দীর্ঘ সময়ের প্রসেস চালু রাখতে সক্ষম করে।
- **নিয়ন্ত্রণ** যেখানে মানব ইন-লুপ ওয়ার্কফ্লো সমর্থিত যা কোথায় কাজগুলি মানব অনুমোদন দাবি করে নির্ধারণ করা হয়।

মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্কের লক্ষ্য হল আন্তঃপরিচালনাযোগ্য হওয়া:

- **ক্লাউড-অ্যাগনস্টিক** - এজেন্টরা কন্টেইনার, অন-প্রিম এবং একাধিক ক্লাউডে চালানো যায়।
- **প্রোভাইডার-অ্যাগনস্টিক** - আপনার পছন্দের SDK যেমন Azure OpenAI এবং OpenAI ব্যবহার করে এজেন্ট তৈরি করা যায়।
- **খোলামাত্রার মান অন্তর্ভুক্তি** - Agent-to-Agent (A2A) এবং Model Context Protocol (MCP) এর মতো প্রোটোকল ব্যবহার করে অন্য এজেন্ট এবং টুল খুঁজে পাওয়া ও ব্যবহার করা যায়।
- **প্লাগইন এবং কানেক্টর** - Microsoft Fabric, SharePoint, Pinecone এবং Qdrant এর মতো ডাটা ও মেমোরি সার্ভিসের সাথে সংযোগ করা যায়।

এখন দেখা যাক মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্কের কিছু মূল ধারণায় এই বৈশিষ্ট্যগুলো কিভাবে প্রয়োগ করা হয়।

## মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্কের মূল ধারণা

### এজেন্টস

![Agent Framework](../../../translated_images/bn/agent-components.410a06daf87b4fef.webp)

**এজেন্ট তৈরি করা**

এজেন্ট তৈরি করা হয় ইনফারেন্স সার্ভিস (LLM প্রদানকারী) নির্ধারণ করে, AI এজেন্ট যে নির্দেশাবলী অনুসরণ করবে সেটি নির্ধারণ করে, এবং একটি `name` বরাদ্দ করে:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

উপরের উদাহরণে `Azure OpenAI` ব্যবহার করা হয়েছে, কিন্তু এজেন্ট বিভিন্ন সার্ভিস ব্যবহার করে তৈরি করা যায়, যেমন `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

অথবা A2A প্রোটোকল ব্যবহার করে রিমোট এজেন্ট:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**এজেন্ট চালানো**

এজেন্ট `.run` বা `.run_stream` পদ্ধতি ব্যবহার করে চালানো হয়, নন-স্ট্রিমিং বা স্ট্রিমিং প্রতিক্রিয়ার জন্য।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

প্রত্যেক এজেন্ট রান অপশন নিতে পারে যেমন এজেন্ট দ্বারা ব্যবহৃত `max_tokens`, এজেন্ট কল করতে পারে এমন `tools`, এবং এমনকি এজেন্টের জন্য ব্যবহৃত `model`।

এটি বিশেষ মডেল বা টুল প্রয়োজন এমন ক্ষেত্রে কাজে লাগে যেখানে ব্যবহারকারীর কাজ সম্পন্ন করতে নির্দিষ্ট কিছু দরকার।

**টুলস**

টুলস নির্ধারণ করা যায় এজেন্ট তৈরি করার সময়:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# যখন সরাসরি একটি ChatAgent তৈরি করা হয়

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

এবং এজেন্ট চালাবার সময়ও:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # শুধুমাত্র এই রানটির জন্য সরঞ্জাম সরবরাহ করা হয়েছে )
```

**এজেন্ট থ্রেডস**

এজেন্ট থ্রেডগুলো বহু-ট্যার্ন কথোপকথন পরিচালনার জন্য ব্যবহৃত হয়। থ্রেড তৈরি করা যায়:

- `get_new_thread()` ব্যবহার করে যা থ্রেড সংরক্ষণ করতে সক্ষম করে
- এজেন্ট চালানোর সময় স্বয়ংক্রিয়ভাবে থ্রেড তৈরি করা যা কেবল চলমান সময় থাকে।

থ্রেড তৈরি করার জন্য কোড এইরকম দেখতে হয়:

```python
# একটি নতুন থ্রেড তৈরি করুন।
thread = agent.get_new_thread() # থ্রেডের সাথে এজেন্টটি চালান।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

তারপর থ্রেড সিরিয়ালাইজ করে পরে ব্যবহারের জন্য সংরক্ষণ করা যায়:

```python
# একটি নতুন থ্রেড তৈরি করুন।
thread = agent.get_new_thread() 

# থ্রেডের সাথে এজেন্ট চালান।

response = await agent.run("Hello, how are you?", thread=thread) 

# সংরক্ষণের জন্য থ্রেড সিরিয়ালাইজ করুন।

serialized_thread = await thread.serialize() 

# সংরক্ষণ থেকে লোড করার পর থ্রেডের অবস্থা ডিজেরিয়ালাইজ করুন।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**এজেন্ট মিডলওয়্যার**

এজেন্ট ইউজারের কাজ সম্পাদনের জন্য টুল এবং LLM এর সঙ্গে যোগাযোগ করে। কিছু পরিস্থিতিতে এই ইন্টারঅ্যাকশনগুলোর মধ্যে ক্রিয়া চালানো বা ট্র্যাক করা দরকার। এজেন্ট মিডলওয়্যার এটি সক্ষম করে:

*ফাংশন মিডলওয়্যার*

এই মিডলওয়্যার এজেন্ট এবং যে ফাংশন/টুল এটি কল করবে তার মধ্যে একটি ক্রিয়া কার্যকর করতে দেয়। যেমন, ফাংশন কল করার সময় লগিং করতে চাইলে এটি ব্যবহৃত হয়।

নিচের কোডে `next` নির্ধারণ করে পরবর্তী মিডলওয়্যার বা আসল ফাংশন কল হবে কিনা।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # প্রি-প্রসেসিং: ফাংশন এক্সেকিউশনের আগে লগ
    print(f"[Function] Calling {context.function.name}")

    # পরবর্তী মিডলওয়্যার বা ফাংশন এক্সেকিউশনে যান
    await next(context)

    # পোস্ট-প্রসেসিং: ফাংশন এক্সেকিউশনের পরে লগ
    print(f"[Function] {context.function.name} completed")
```

*চ্যাট মিডলওয়্যার*

এই মিডলওয়্যার এজেন্ট এবং LLM এর অনুরোধের মাঝে একটি ক্রিয়া লগ বা কার্যকর করতে দেয়।

এতে গুরুত্বপূর্ণ তথ্য থাকে যেমন `messages` যা AI সার্ভিসে পাঠানো হয়।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # প্রি-প্রসেসিং: AI কলের আগে লগ করুন
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # পরবর্তী মিডলওয়্যার বা AI সার্ভিসে চালিয়ে যান
    await next(context)

    # পোস্ট-প্রসেসিং: AI প্রতিক্রিয়ার পরে লগ করুন
    print("[Chat] AI response received")

```

**এজেন্ট মেমোরি**

`Agentic Memory` পাঠে আলোচনা করা হয়েছে, মেমোরি হল এজেন্টকে বিভিন্ন প্রসঙ্গের ওপর কাজ করার জন্য সক্ষম করার একটি গুরুত্বপূর্ণ উপাদান। MAF এর বিভিন্ন ধরনের মেমোরি রয়েছে:

*ইন-মেমোরি স্টোরেজ*

এটি থ্রেডগুলোর মধ্যে অ্যাপ্লিকেশন রানটাইমে সংরক্ষিত মেমোরি।

```python
# একটি নতুন থ্রেড তৈরি করুন।
thread = agent.get_new_thread() # থ্রেড সহ এজেন্ট চালান।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*স্থায়ী বার্তা*

এই মেমোরি ব্যবহার করা হয় বিভিন্ন সেশনের কথোপকথন ইতিহাস সংরক্ষণের জন্য। এটি `chat_message_store_factory` দিয়ে নির্ধারিত হয়:

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

*ডাইনামিক মেমোরি*

এই মেমোরি এজেন্ট চালানোর আগে প্রসঙ্গে যোগ করা হয়। এটি mem0 এর মত বাহ্যিক সার্ভিসে সংরক্ষিত হতে পারে:

```python
from agent_framework.mem0 import Mem0Provider

# উন্নত মেমোরি ক্ষমতার জন্য Mem0 ব্যবহার করা হচ্ছে
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

**এজেন্ট পর্যবেক্ষণযোগ্যতা**

পর্যবেক্ষণযোগ্যতা নির্ভরযোগ্য ও রক্ষণাবেক্ষণযোগ্য এজেন্টিক সিস্টেম তৈরি করতে গুরুত্বপূর্ণ। MAF OpenTelemetry এর সঙ্গে ইন্টিগ্রেটেড যা ট্রেসিং ও মিটার প্রদান করে উন্নত পর্যবেক্ষণের জন্য।

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

MAF ওয়ার্কফ্লো প্রদান করে যা পূর্বনির্ধারিত ধাপ দিয়ে একটি কাজ সম্পন্ন করে এবং সেই ধাপগুলোতে AI এজেন্ট অংশ নেয়।

ওয়ার্কফ্লো বিভিন্ন উপাদান নিয়ে গঠিত যা ভাল কন্ট্রোল ফ্লো দেয়। ওয়ার্কফ্লো **মাল্টি-এজেন্ট অর্কেস্ট্রেশন** এবং **চেকপয়েন্টিং** সেভ করার সুবিধাও দেয়।

একটি ওয়ার্কফ্লোর মূল উপাদানসমূহ:

**এক্সিকিউটরস**

এক্সিকিউটর ইনপুট বার্তা গ্রহণ করে, নির্ধারিত কাজ সম্পন্ন করে, এবং একটি আউটপুট বার্তা উৎপাদন করে। এটি ওয়ার্কফ্লোকে বড় কাজের দিকে এগিয়ে নিয়ে যায়। এক্সিকিউটর হতে পারে AI এজেন্ট অথবা কাস্টম লজিক।

**এডজেস**

এডজেস ওয়ার্কফ্লোতে বার্তাগুলোর প্রবাহ সংজ্ঞায়িত করতে ব্যবহৃত হয়। এর প্রকার:

*ডাইরেক্ট এডজেস* - এক্সিকিউটরদের মধ্যে সরল এক থেকে এক সংযোগ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*শর্তাধীন এডজেস* - নির্দিষ্ট শর্ত পূরণের পরে সক্রিয়। উদাহরণস্বরূপ, হোটেল রুম অনুপলব্ধ হলে, এক্সিকিউটর অন্য বিকল্প প্রস্তাব করতে পারে।

*সুইচ-কেস এডজেস* - নির্ধারিত শর্তের উপর ভিত্তি করে বার্তাগুলো বিভিন্ন এক্সিকিউটরের কাছে পাঠায়। যেমন, ভ্রমণ গ্রাহকের অগ্রাধিকার প্রবেশাধিকার থাকলে তাদের কাজ অন্য ওয়ার্কফ্লোর মাধ্যমে পরিচালিত হবে।

*ফ্যান-আউট এডজেস* - একটি বার্তা একাধিক লক্ষ্যে পাঠানো হয়।

*ফ্যান-ইন এডজেস* - বিভিন্ন এক্সিকিউটরের কাছ থেকে একাধিক বার্তা সংগ্রহ করে এক লক্ষ্যে পাঠানো হয়।

**ইভেন্টস**

ওয়ার্কফ্লোতে উন্নত পর্যবেক্ষণের জন্য, MAF এক্সিকিউশনের জন্য বিল্ট-ইন ইভেন্ট প্রদান করে:

- `WorkflowStartedEvent`  - ওয়ার্কফ্লো এক্সিকিউশন শুরু হয়
- `WorkflowOutputEvent` - ওয়ার্কফ্লো আউটপুট উৎপাদন করে
- `WorkflowErrorEvent` - ওয়ার্কফ্লো কোনো ত্রুটি পায়
- `ExecutorInvokeEvent`  - এক্সিকিউটর প্রসেসিং শুরু করে
- `ExecutorCompleteEvent`  - এক্সিকিউটর প্রসেসিং শেষ করে
- `RequestInfoEvent` - একটি অনুরোধ জারি করা হয়

## উন্নত MAF প্যাটার্ন

উপরোক্ত অংশগুলি মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্কের মূল ধারণা কভার করেছে। আরও জটিল এজেন্ট তৈরি করার সময় বিবেচনা করার জন্য কিছু উন্নত প্যাটার্ন:

- **মিডলওয়্যার কম্পোজিশন**: একাধিক মিডলওয়্যার হ্যান্ডলার (লগিং, অথ, রেট-লিমিটিং) সংযুক্ত করা ফাংশন এবং চ্যাট মিডলওয়্যার ব্যবহার করে এজেন্টের আচরণের সূক্ষ্ম নিয়ন্ত্রণের জন্য।
- **ওয়ার্কফ্লো চেকপয়েন্টিং**: ওয়ার্কফ্লো ইভেন্ট এবং সিরিয়ালাইজেশন ব্যবহার করে দীর্ঘ সময় চালানো এজেন্ট প্রসেস সংরক্ষণ এবং পুনরায় চালু করা।
- **ডাইনামিক টুল সিলেকশন**: টুল বর্ণনার উপর RAGের সাথে MAF এর টুল রেজিস্ট্রেশন মিলিয়ে শুধুমাত্র প্রাসঙ্গিক টুলগুলো প্রশ্নের জন্য উপস্থাপন করা।
- **মাল্টি-এজেন্ট হ্যান্ডঅফ**: ওয়ার্কফ্লো এডজেস ও শর্তাধীন রাউটিং ব্যবহার করে বিশেষায়িত এজেন্টদের মধ্যে হ্যান্ডঅফ অর্কেস্ট্রেট করা।

## কোড স্যাম্পল

মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্কের কোড স্যাম্পলগুলো এই রিপোজিটরিতে `xx-python-agent-framework` এবং `xx-dotnet-agent-framework` ফাইলের মধ্যে পাওয়া যাবে।

## মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্ক সম্পর্কে আরও প্রশ্ন?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) এ যোগ দিন অন্য শিক্ষানবিশদের সাথে পরিচিত হতে, অফিস আওয়ার্সে অংশ নিতে এবং AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পেতে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**বিস্তারিত বিবৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ভুল বা ত্রুটি থাকতে পারে। মূল ভাষায় থাকা নথিটিকেই সর্বোচ্চ কর্তৃত্বশীল উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে কোনও ভুল বোঝাবুঝি বা ভুল অর্থগ্রহণের জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->