# মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক অন্বেষণ

![Agent Framework](../../../translated_images/bn/lesson-14-thumbnail.90df0065b9d234ee.webp)

### পরিচিতি

এই পাঠে আলোচনা করা হবে:

- মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক বোঝা: মূল বৈশিষ্ট্য এবং মূল্য  
- মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের মূল ধারণাগুলি অন্বেষণ করা
- উন্নত MAF প্যাটার্ন: ওয়ার্কফ্লো, মিডলওয়্যার, এবং মেমোরি

## শেখার লক্ষ্য

এই পাঠটি সম্পন্ন করার পর, আপনি জানতে পারবেন কীভাবে:

- মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক ব্যবহার করে প্রোডাকশন-রেডি এআই এজেন্ট তৈরি করবেন
- মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের মূল বৈশিষ্ট্যগুলি আপনার এজেন্টিক ব্যবহার কেসে প্রয়োগ করবেন
- কর্মপ্রবাহ, মিডলওয়্যার এবং পর্যবেক্ষণসহ উন্নত প্যাটার্ন ব্যবহার করবেন

## কোড নমুনা 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) এর কোড নমুনা এই সংরক্ষণাগারে `xx-python-agent-framework` এবং `xx-dotnet-agent-framework` ফাইলগুলির মধ্যে পাওয়া যাবে।

## মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক বোঝা

![Framework Intro](../../../translated_images/bn/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) হলো মাইক্রোসফটের একীভূত ফ্রেমওয়ার্ক এআই এজেন্ট তৈরি করার জন্য। এটি বিভিন্ন ধরণের এজেন্টিক ইউজ কেস মোকাবেলার জন্য নমনীয়তা প্রদান করে যা প্রোডাকশন এবং গবেষণা পরিবেশে দেখা যায়, যেমন:

- যেখানে ধাপে ধাপে ওয়ার্কফ্লো প্রয়োজন, সেখানে **ক্রমবিন্যাস এজেন্ট সমন্বয়**।
- যেখানে একসঙ্গে কাজ করতে হয়, সেখানে **সমান্তরাল সমন্বয়**।
- যেখানে একক টাস্কে একসঙ্গে কাজ করে, সেখানে **গ্রুপ চ্যাট সমন্বয়**।
- যেখানে সাবটাস্ক সম্পন্ন হলে কাজ একে অপরের মাঝে হস্তান্তর করা হয়, সেখানে **হ্যান্ডঅফ সমন্বয়**।
- যেখানে একজন ম্যানেজার এজেন্ট টাস্ক তালিকা তৈরি ও পরিবর্তন করে এবং সাবএজেন্টদের সমন্বয় করে কাজ সম্পন্ন করে, সেখানে **ম্যাগনেটিক সমন্বয়**।

প্রোডাকশন এআই এজেন্ট সরবরাহ করার জন্য, MAF-এ নিম্নলিখিত বৈশিষ্ট্যও অন্তর্ভুক্ত রয়েছে:

- OpenTelemetry ব্যবহারের মাধ্যমে **পর্যবেক্ষণযোগ্যতা**, যেখানে প্রতিটি এআই এজেন্টের কাজ যেমন টুল ইনভোকেশন, সমন্বয় ধাপ, যুক্তি প্রবাহ এবং পারফরম্যান্স মনিটরিং Microsoft Foundry ড্যাশবোর্ডের মাধ্যমে দেখা যায়।
- Microsoft Foundry-তে এজেন্টগুলো স্থানীয়ভাবে হোস্ট করার মাধ্যমে **নিরাপত্তা**, যেখানে রোল-ভিত্তিক অ্যাক্সেস, ব্যক্তিগত ডেটা পরিচালনা এবং অন্তর্নির্মিত কনটেন্ট সেফটি রয়েছে।
- **স্থিতিশীলতা**, যেখানে এজেন্ট থ্রেড এবং ওয়ার্কফ্লো বিরতি নিতে, পুনরায় চালু করতে এবং ত্রুটি থেকে পুনরুদ্ধার করতে পারে, যা দীর্ঘদিন চলা প্রক্রিয়া সক্ষম করে।
- যেখানে মানব অনুমোদন প্রয়োজন, সেসব ক্ষেত্রে মানব নিয়ন্ত্রণ সমর্থিত **নিয়ন্ত্রণ**।

মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক আন্তঃপরিচালনাযোগ্যতায়ও মনোযোগী:

- **ক্লাউড-নিরপেক্ষ** - এজেন্টগুলো কন্টেইনারে, অন-প্রিমাইস এবং একাধিক ক্লাউডে চলতে পারে।
- **প্রোভাইডার-নিরপেক্ষ** - Azure OpenAI এবং OpenAI সহ আপনার পছন্দের SDK ব্যবহার করে এজেন্ট তৈরি করা যায়।
- **ওপেন স্ট্যান্ডার্ড ইন্টিগ্রেশন** - Agent-to-Agent (A2A) এবং Model Context Protocol (MCP) প্রোটোকল ব্যবহার করে অন্য এজেন্ট ও টুল আবিষ্কার ও ব্যবহার করা যায়।
- **প্লাগইন এবং কানেক্টর** - Microsoft Fabric, SharePoint, Pinecone এবং Qdrant এর মতো ডেটা ও মেমোরি সেবা সংযোগ করা যায়।

আসুন দেখি কীভাবে এই বৈশিষ্ট্যগুলো মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের মূল ধারণাগুলোর মধ্যে প্রযোজ্য হয়।

## মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের মূল ধারণা

### এজেন্ট

![Agent Framework](../../../translated_images/bn/agent-components.410a06daf87b4fef.webp)

**এজেন্ট তৈরি করা**

এজেন্ট তৈরি করতে inference সার্ভিস (LLM প্রদানকারী), এআই এজেন্ট অনুসরণ করার জন্য নির্দেশাবলী সেট, এবং একটি `name` নির্ধারণ করা হয়:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

উপরের উদাহরণে `Azure OpenAI` ব্যবহার করা হয়েছে, তবে এজেন্ট বিভিন্ন সার্ভিস ব্যবহার করে তৈরি হতে পারে, যেমন `Microsoft Foundry Agent Service`:

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

অথবা [MiniMax](https://platform.minimaxi.com/), যা OpenAI-সঙ্গত API সরবরাহ করে বৃহদায়তন প্রসঙ্গ উইন্ডো (২০৪কে টোকেন পর্যন্ত) সহ:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

অথবা A2A প্রোটোকল ব্যবহার করে দূরবর্তী এজেন্ট:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**এজেন্ট চালানো**

.run বা .run_stream পদ্ধতি ব্যবহার করে এজেন্ট চালানো হয়, যা সঠিকভাবে নন-স্ট্রিমিং বা স্ট্রিমিং উত্তর প্রদান করে।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

প্রতিটি এজেন্ট চালানোর সময় প্যারামিটার কাস্টমাইজ করাও সম্ভব যেমন `max_tokens`, agent কল করতে পারার `tools`, এবং এমনকি ব্যবহৃত `model`।

এটি বিশেষ মডেল বা টুল প্রয়োজন হলে ব্যবহারিক।

**টুলস**

টুলস সংজ্ঞায়িত করা যায় এজেন্ট সংজ্ঞায়িত করার সময়:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# যখন সরাসরি একটি ChatAgent তৈরি করা হয়

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

এবং এজেন্ট চালানোর সময়ও:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # শুধুমাত্র এই রান-এর জন্য সরঞ্জাম সরবরাহ করা হয়েছে )
```

**এজেন্ট থ্রেড**

বহু-বার্তালাপ পরিচালনার জন্য এজেন্ট থ্রেড ব্যবহার করা হয়। থ্রেড তৈরি করা যায়:

- `get_new_thread()` ব্যবহার করে যা থ্রেড সময়ের সাথে সংরক্ষণ করতে দেয়
- এজেন্ট চালানোর সময় স্বয়ংক্রিয়ভাবে থ্রেড তৈরি করে যা শুধুমাত্র চলমান সেশনের মধ্যে থাকে

থ্রেড তৈরি করার কোড দেখতে এই রকম:

```python
# একটি নতুন থ্রেড তৈরি করুন।
thread = agent.get_new_thread() # থ্রেডটি দিয়ে এজেন্টটি চালান।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

পরবর্তীতে থ্রেড সঞ্চয়ের জন্য সিরিয়ালাইজ করা যায়:

```python
# একটি নতুন থ্রেড তৈরি করুন।
thread = agent.get_new_thread() 

# থ্রেডটির সাথে এজেন্টটি চালান।

response = await agent.run("Hello, how are you?", thread=thread) 

# সংরক্ষণের জন্য থ্রেড সিরিয়ালাইজ করুন।

serialized_thread = await thread.serialize() 

# সংরক্ষণের পর থ্রেডের অবস্থা ডেসিরিয়ালাইজ করুন।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**এজেন্ট মিডলওয়্যার**

এজেন্ট অপারেশন সম্পন্ন করতে টুল ও LLM এর সাথে ইন্টারঅ্যাক্ট করে। মাঝে মাঝে এই কন্ট্রোল বা ট্র্যাক করার প্রয়োজন হয়। এজেন্ট মিডলওয়্যার অনুমোদন দেয় এই কাজটি করার জন্য:

*ফাংশন মিডলওয়্যার*

এই মিডলওয়্যার এজেন্ট এবং তার কল করা ফাংশন/টুলের মাঝে কাজ সম্পাদন করে। যেমন, ফাংশন কল লগিং করা।

নিচের কোডে `next` নির্দেশ করে পরবর্তী মিডলওয়্যার বা আসল ফাংশন কোনটি কল হবে।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # প্রি-প্রসেসিং: ফাংশন সংবহার পূর্বে লগ করুন
    print(f"[Function] Calling {context.function.name}")

    # পরবর্তী মিডলওয়্যার বা ফাংশন সংবহার চালিয়ে যান
    await next(context)

    # পোস্ট-প্রসেসিং: ফাংশন সংবহার পর লগ করুন
    print(f"[Function] {context.function.name} completed")
```

*চ্যাট মিডলওয়্যার*

এজেন্ট এবং LLM-এর অনুরোধের মাঝে কাজ সম্পাদন বা লগ করার জন্য ব্যবহৃত।

এতে গুরুত্বপূর্ণ তথ্য যেমন AI সার্ভিসে পাঠানো `messages` থাকে।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # প্রি-প্রসেসিং: AI কলের আগে লগ করুন
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # পরবর্তী মিডলওয়্যার বা AI সার্ভিস চালিয়ে যান
    await next(context)

    # পোস্ট-প্রসেসিং: AI রেসপন্সের পরে লগ করুন
    print("[Chat] AI response received")

```

**এজেন্ট মেমোরি**

`Agentic Memory` পাঠে আলোচিত হয়েছে, মেমোরি একটি গুরুত্বপূর্ণ উপাদান যা এজেন্টকে বিভিন্ন প্রসঙ্গে কাজ করতে সাহায্য করে। MAF বিভিন্ন প্রকার মেমোরি অফার করে:

*ইন-মেমোরি স্টোরেজ*

এটি রানটাইম সময় থ্রেডে সংরক্ষিত মেমোরি।

```python
# একটি নতুন থ্রেড তৈরি করুন।
thread = agent.get_new_thread() # থ্রেডের সাথে এজেন্ট চালান।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*পরম্পরাগত বার্তা*

বিভিন্ন সেশনে কথোপকথন ইতিহাস সংরক্ষণে ব্যবহৃত। এটি `chat_message_store_factory` দ্বারা সংজ্ঞায়িত:

```python
from agent_framework import ChatMessageStore

# একটি কাস্টম বার্তা সংরক্ষণাগার তৈরি করুন
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ডায়নামিক মেমোরি*

এজেন্ট চালানোর আগে প্রসঙ্গে যোগ করা হয়। বহিরাগত সেবায় সংরক্ষণযোগ্য যেমন mem0:

```python
from agent_framework.mem0 import Mem0Provider

# উন্নত মেমোরি সক্ষমতার জন্য Mem0 ব্যবহার করা হচ্ছে
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

নির্ভরযোগ্য এবং রক্ষণাবেক্ষণযোগ্য এজেন্টিক সিস্টেম তৈরির জন্য পর্যবেক্ষণযোগ্যতা জরুরি। MAF OpenTelemetry-এর সঙ্গে ইন্টিগ্রেট করে ট্রেসিং এবং মিটার প্রদান করে উন্নত পর্যবেক্ষণযোগ্যতার জন্য।

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

MAF ওয়ার্কফ্লো সরবরাহ করে — পূর্বনির্ধারিত ধাপ যা একটি কাজ সম্পন্ন করে এবং ওই ধাপে এআই এজেন্ট থাকে।

ওয়ার্কফ্লো বিভিন্ন উপাদানে গঠিত যা নিয়ন্ত্রণ প্রবাহ উন্নত করে। এটি **মাল্টি-এজেন্ট সমন্বয়** এবং **চেকপয়েন্টিং** সমর্থন করে ওয়ার্কফ্লো অবস্থা সংরক্ষণের জন্য।

ওয়ার্কফ্লোর মূল উপাদানগুলো হলো:

**এক্সিকিউটর**

ইনপুট মেসেজ গ্রহণ করে, বরাদ্দকৃত কাজ সম্পাদন করে এবং আউটপুট মেসেজ তৈরি করে যা বৃহত্তর কাজের দিকে নিয়ে যায়। এক্সিকিউটর হয় এআই এজেন্ট বা কাস্টম লজিক।

**এজ**

মেসেজ প্রবাহ সংজ্ঞায়িত করতে ব্যবহার হয়। হতে পারে:

*ডিরেক্ট এজ* - এক্সিকিউটরের মধ্যে সরাসরি এক থেকে এক সংযোগ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*শর্তাধীন এজ* - নির্দিষ্ট শর্ত পূরণ হলে সক্রিয় হয়। উদাহরণস্বরূপ, হোটেল রুম না থাকলে অন্য বিকল্প প্রস্তাব।

*সুইচ-কেস এজ* - শর্ত অনুযায়ী মেসেজ ভিন্ন এক্সিকিউটরে পাঠায়। যেমন, একটি ভ্রমণ গ্রাহক প্রাধান্য পেলে তাদের কাজ অন্য ওয়ার্কফ্লোতে হবে।

*ফ্যান-আউট এজ* - একটি মেসেজ একাধিক লক্ষ্যকে পাঠানো।

*ফ্যান-ইন এজ* - বিভিন্ন এক্সিকিউটরের একাধিক মেসেজ একত্র করে এক লক্ষ্যকে পাঠানো।

**ইভেন্ট**

ওয়ার্কফ্লো তদারকি সহজ করতে MAF বিল্ট-ইন ইভেন্ট দেয় যেমন:

- `WorkflowStartedEvent`  - ওয়ার্কফ্লো শুরু হয়
- `WorkflowOutputEvent` - ওয়ার্কফ্লো আউটপুট তৈরি করে
- `WorkflowErrorEvent` - ওয়ার্কফ্লো ত্রুটি পায়
- `ExecutorInvokeEvent`  - এক্সিকিউটর কাজ শুরু করে
- `ExecutorCompleteEvent`  -  এক্সিকিউটর কাজ শেষ করে
- `RequestInfoEvent` - অনুরোধ করা হয়

## উন্নত MAF প্যাটার্ন

উপরের অংশে মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের মূল ধারণা আলোচনা হয়েছে। যখন আপনি জটিল এজেন্ট তৈরি করবেন, সেক্ষেত্রে কিছু উন্নত প্যাটার্ন বিবেচনা করুন:

- **মিডলওয়্যার সংমিশ্রণ**: বিভিন্ন মিডলওয়্যার হ্যান্ডলার (লগিং, অথ, রেট-লিমিটিং) সংযুক্ত করে সূক্ষ্ম নিয়ন্ত্রণ, ফাংশন ও চ্যাট মিডলওয়্যার ব্যবহার করে।
- **ওয়ার্কফ্লো চেকপয়েন্টিং**: ওয়ার্কফ্লো ইভেন্ট ও সিরিয়ালাইজেশন ব্যবহার করে দীর্ঘমেয়াদী এজেন্ট প্রক্রিয়া সংরক্ষণ ও পুনরায় শুরু করা।
- **ডায়নামিক টুল নির্বাচন**: টুল বর্ণনার উপর RAG এবং MAF টুল নিবন্ধন মিলিয়ে, প্রতিটি প্রশ্নের জন্য প্রাসঙ্গিক টুল দেখানো।
- **মাল্টি-এজেন্ট হ্যান্ডঅফ**: ওয়ার্কফ্লো এজ ও শর্তাধীন রাউটিং ব্যবহার করে বিশেষায়িত এজেন্টদের মধ্যে হ্যান্ডঅফ সমন্বয় করা।

## Microsoft Foundry-তে LangChain / LangGraph এজেন্ট হোস্টিং

Microsoft Agent Framework হলো **ফ্রেমওয়ার্ক-ইন্টারঅপারেবল** — শুধুমাত্র MAF দিয়ে লেখা এজেন্টেই সীমাবদ্ধ নয়। আপনি যদি ইতিমধ্যে **LangChain** বা **LangGraph** দিয়ে এজেন্ট তৈরি করে থাকেন, তাহলে এটি **Microsoft Foundry হোস্টেড এজেন্ট** হিসেবে চালাতে পারেন, যেখানে Foundry রানটাইম, সেশন, স্কেলিং, পরিচয় এবং প্রোটোকল এন্ডপয়েন্ট পরিচালনা করলেও আপনার এজেন্ট লজিক LangGraph-এ থাকে।

এটি করা হয় `langchain_azure_ai.agents.hosting` প্যাকেজ দিয়ে, যা একই প্রোটোকলের মাধ্যমে কম্পাইলড LangGraph গ্রাফ প্রকাশ করে যা Foundry হোস্টেড এজেন্ট ব্যবহার করে।

**1. হোস্টিং এক্সট্রা ইন্সটল করুন:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` এক্সট্রা Foundry প্রোটোকল লাইব্রেরি ইনস্টল করে: `azure-ai-agentserver-responses` (OpenAI-সঙ্গত `/responses` এন্ডপয়েন্ট) এবং `azure-ai-agentserver-invocations` (সাধারণ `/invocations` এন্ডপয়েন্ট)।

**2. একটি হোস্টিং প্রোটোকল নির্বাচন করুন:**

| প্রোটোকল | হোস্ট ক্লাস | এন্ডপয়েন্ট | কখন ব্যবহার করবেন |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-সঙ্গত চ্যাট, স্ট্রিমিং, উত্তর ইতিহাস, এবং কথোপকথন থ্রেডিং দরকার হলে — কথোপকথন এজেন্টের জন্য সুপারিশকৃত |
| **Invocations** | `InvocationsHostServer` | `/invocations` | যদি কাস্টম JSON ফরম্যাট, webhook-স্টাইল এন্ডপয়েন্ট বা অ-কথোপকথন প্রক্রিয়াকরণ দরকার হয় |

কারণ **Responses API Foundry-তে এজেন্ট স্টাইল উন্নয়নের প্রধান API**, বেশিরভাগ এজেন্টের জন্য `ResponsesHostServer` দিয়ে শুরু করুন।

**3. পরিবেশ পরিবর্তনশীল কনফিগার করুন** (`az login` আগে করুন যাতে `DefaultAzureCredential` প্রমাণীকৃত হতে পারে):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

যখন এজেন্ট পরে Foundry-তে হোস্টেড এজেন্ট হিসেবে চালানো হবে, প্ল্যাটফর্ম স্বয়ংক্রিয়ভাবে `FOUNDRY_PROJECT_ENDPOINT` ইনজেক্ট করে।

**4. Responses প্রোটোকলের ওপর LangGraph এজেন্ট প্রকাশ করুন:**

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

    # এখানে ChatOpenAI Foundry প্রকল্পের OpenAI-সঙ্গতিপূর্ণ (Responses) এন্ডপয়েন্টকে লক্ষ করে।
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

লোকালভাবে `python main.py` দিয়ে চালান, তারপর `http://localhost:8088/responses` এ Responses অনুরোধ পাঠান।

**মূল আচরণগুলি:**

- **কথোপকথন**: ক্লায়েন্টরা `previous_response_id` বা `conversation` আইডি পাস করে কথোপকথন চালিয়ে যায়। আপনার গ্রাফ LangGraph চেকপয়েন্টার দিয়ে কম্পাইল করা থাকলে, Foundry কথোপকথন অবস্থা সেই চেকপয়েন্টে জমা রাখে (প্রোডাকশনে স্থায়ী চেকপয়েন্টার ব্যবহার করুন; স্থানীয় পরীক্ষার জন্য `MemorySaver` ভালো)।
- **মানব-ইন-দ্য-লুপ**: আপনার গ্রাফ LangGraph `interrupt()` ব্যবহার করলে, `ResponsesHostServer` মুলতুবি ইন্টারাপ্টকে Responses `function_call` / `mcp_approval_request` আইটেম হিসেবে প্রকাশ করে, আর ক্লায়েন্ট মিলে এমন `function_call_output` / `mcp_approval_response` দিয়ে পুনরায় শুরু করে।
- **Foundry-এ ডিপ্লয় করুন**: Azure Developer CLI ব্যবহার করুন — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (লোকাল, Docker দরকার), তারপর `azd provision` এবং `azd deploy`। হোস্টেড-এজেন্ট ডিপ্লয়মেন্টে **Foundry Project Manager** রোল প্রয়োজন।

এই উদাহরণের রানযোগ্য সংস্করণ পাওয়া যাবে [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)। সম্পূর্ণ ওয়াকথ্রু (Invocations প্রোটোকল, কাস্টম রিকোয়েস্ট স্কিমা, এবং সমস্যা সমাধান) এর জন্য দেখুন [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)।

## কোড নমুনা 

মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্কের কোড নমুনা এই সংরক্ষণাগারে `xx-python-agent-framework` এবং `xx-dotnet-agent-framework` ফাইলগুলোর মধ্যে পাওয়া যাবে।

## মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক সম্পর্কে আরও প্রশ্ন আছে?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) এ যোগ দিন, অন্যান্য শিক্ষার্থীদের সঙ্গে মেলামেশা করুন, অফিস আওয়ার এ অংশ নিন এবং আপনার AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পান।
## আগের পাঠ

[AI এজেন্টের জন্য মেমোরি](../13-agent-memory/README.md)

## পরের পাঠ

[কম্পিউটার ব্যবহারকারী এজেন্ট তৈরি (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->