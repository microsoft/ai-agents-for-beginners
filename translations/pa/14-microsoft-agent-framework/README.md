# ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਖੋਜ

![Agent Framework](../../../translated_images/pa/lesson-14-thumbnail.90df0065b9d234ee.webp)

### ਪਰੇਚਿਆ

ਇਹ ਪਾਠ ਕਵਰ ਕਰੇਗਾ:

- ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਸਮਝ: ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਮੁੱਲ  
- ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੁੱਖ ਸੰਕਲਪਾਂ ਦੀ ਖੋਜ
- ਉੱਨਤ MAF ਪੈਟਰਨ: ਵਰਕਫਲੋ, ਮਿਡਲਵੇਅਰ, ਅਤੇ ਮੈਮੋਰੀ

## ਸਿੱਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਨੂੰ ਮੁਕੰਮਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਜਾਣੋਂਗੇ ਕਿਵੇਂ:

- ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਨਾਲ ਪ੍ਰੋਡਕਸ਼ਨ-ਰੇਡੀ AI ਏਜੰਟ ਬਣਾਏਣੇ
- ਆਪਣੇ ਏਜੰਟਿਕ ਕੇਸਾਂ ਲਈ ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀਆਂ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਲਾਗੂ ਕਰਨਾ
- ਵਰਕਫਲੋ, ਮਿਡਲਵੇਅਰ ਅਤੇ ਓਬਜ਼ਰਵੇਬਿਲਟੀ ਸਮੇਤ ਉੱਨਤ ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਕਰਨਾ

## ਕੋਡ ਨਮੂਨੇ 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ਲਈ ਕੋਡ ਨਮੂਨੇ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ  `xx-python-agent-framework` ਅਤੇ `xx-dotnet-agent-framework` ਫਾਈਲਾਂ ਹੇਠਾਂ ਮਿਲ ਸਕਦੇ ਹਨ।

## ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਨੂੰ ਸਮਝਣਾ

![Framework Intro](../../../translated_images/pa/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ਮਾਇਕ੍ਰੋਸੌਫਟ ਦਾ ਏਆਈ ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਇਕ ਸੰਗਠਿਤ ਫਰੇਮਵਰਕ ਹੈ। ਇਹਦੇ ਨਾਲ ਪ੍ਰੋਡਕਸ਼ਨ ਅਤੇ ਰਿਸਰਚ ਮਾਹੌਲ ਵਿੱਚ ਦੇਖੇ ਜਾਣ ਵਾਲੇ ਵੱਖ-ਵੱਖ ਏਜੰਟਿਕ ਕੇਸਾਂ ਲਈ ਲਚੀਲਾਪਨ ਹੈ, ਜਿਵੇਂ ਕਿ:

- **ਕ੍ਰਮਬੱਧ ਏਜੰਟ ਆਰਕੇਸਟਰੈਸ਼ਨ** ਉਹ ਥਾਵਾਂ ਜਿੱਥੇ ਕਦਮ-ਦਰ-ਕਦਮ ਵਰਕਫਲੋ ਦੀ ਲੋੜ ਹੈ।
- **ਸਾਥ-ਸਾਥ ਆਰਕੇਸਟਰੈਸ਼ਨ** ਉਹ ਥਾਵਾਂ ਜਿੱਥੇ ਏਜੰਟ ਇਕੱਠੇ ਕੰਮ ਸੱਪੂਰਣ ਕਰਦੇ ਹਨ।
- **ਗਰੁੱਪ ਚੈਟ ਆਰਕੇਸਟਰੈਸ਼ਨ** ਉਹ ਥਾਵਾਂ ਜਿੱਥੇ ਏਜੰਟ ਇੱਕ ਕੰਮ 'ਤੇ ਮਿਲਕੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹਨ।
- **ਹੈਂਡਾਫ ਆਰਕੇਸਟਰੈਸ਼ਨ** ਉਹ ਥਾਵਾਂ ਜਿੱਥੇ ਏਜੰਟ ਜਦੋਂ ਸਬਟਾਸਕ ਮੁਕੰਮਲ ਕਰ ਲੈਂਦੇ ਹਨ ਤਾਂ ਕੰਮ ਇਕ-दੂਜੇ ਨੂੰ ਸਾਹਮਣੇ ਦਿੰਦੇ ਹਨ।
- **ਮੈਗਨੇਟਿਕ ਆਰਕੇਸਟਰੈਸ਼ਨ** ਉਹ ਥਾਵਾਂ ਜਿੱਥੇ ਇੱਕ ਪਰਬੰਧਕ ਏਜੰਟ ਟਾਸਕ ਲਿਸਟ ਬਣਾਉਂਦਾ ਅਤੇ ਸੋਧਦਾ ਹੈ ਅਤੇ ਸਬਏਜੰਟਾਂ ਦਾ ਮੇਲਜੋਲ ਕਰਕੇ ਟਾਸਕ ਪੂਰਾ ਕਰਵਾਉਂਦਾ ਹੈ।

ਪ੍ਰੋਡਕਸ਼ਨ ਵਿੱਚ ਏਆਈ ਏਜੰਟ ਪਹੁੰਚਾਉਣ ਲਈ, MAF ਵਿੱਚ ਹੇਠ ਲਿਖੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵੀ ਸ਼ਾਮਲ ਹਨ:

- **ਓਬਜ਼ਰਵੇਬਿਲਟੀ** OpenTelemetry ਦੀ ਵਰਤੋਂ ਰਾਹੀਂ, ਜਿੱਥੇ ਏਆਈ ਏਜੰਟ ਦੀ ਹਰ ਕਾਰਵਾਈ ਜਿਵੇਂ ਕਿ ਟੂਲ ਕਾਲ, ਆਰਕੇਸਟਰੈਸ਼ਨ ਕਦਮ, ਤਰਕ ਫਲੋਅ ਅਤੇ ਮਾਇਕ੍ਰੋਸੌਫਟ ਫਾਉਂਡਰੀ ਡੈਸ਼ਬੋਰਡਾਂ ਰਾਹੀਂ ਪ੍ਰਦਰਸ਼ਨ ਨਿਗਰਾਨੀ ਦਿਖਾਈ ਜਾਂਦੀ ਹੈ।
- **ਸੁਰੱਖਿਆ** ਮਾਇਕ੍ਰੋਸੌਫਟ ਫਾਉਂਡਰੀ 'ਤੇ ਨੈਟਿਵ ਤੌਰ 'ਤੇ ਏਜੰਟ ਮਜ਼ਬੂਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਭੂਮਿਕਾ-ਅਧਾਰਿਤ ਪਹੁੰਚ, ਨਿੱਜੀ ਡਾਟਾ ਪ੍ਰਬੰਧਨ ਅਤੇ ਅੰਦਰੂਨੀ ਸਮਗਰੀ ਸੁਰੱਖਿਆ ਸ਼ਾਮਲ ਹਨ।
- **ਟਿਕਾਊपन** ਏਜੰਟ ਥ੍ਰੇਡ ਅਤੇ ਵਰਕਫਲੋਜ਼ ਨੂੰ ਰੋਕਿਆ, ਮੁੜ ਚਾਲੂ ਅਤੇ ਗਲਤੀਆਂ ਤੋਂ ਬਚਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਜੋ ਲੰਮੇ ਸਮੇਂ ਵਾਲੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ।
- **ਕੰਟਰੋਲ** ਮਨੁੱਖ-ਦਰਮਿਆਨ ਵਰਕਫਲੋਜ਼ ਨੂੰ ਸਹਾਇਤਾ ਮਿਲਦੀ ਹੈ ਜਿੱਥੇ ਕੰਮ ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ ਦੀ ਲੋੜ ਦਰਸਾਉਂਦੇ ਹਨ।

ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਅੰਤਰਉਚਿਤ (ਇੰਟਰਓਪਰੇਬਲ) ਹੋਣ 'ਤੇ ਵੀ ਧਿਆਨ ਕੇਂਦਰਤ ਕਰਦਾ ਹੈ:

- **ਕਲਾਉਡ-ਅਗਨੋਸਟਿਕ ਹੋਣਾ** - ਏਜੰਟ ਕੰਟੇਨਰਾਂ ਵਿੱਚ, ਸਥਾਨਕ ਅਤੇ ਕਈ ਵੱਖਰੇ ਕਲਾਉਡਾਂ 'ਤੇ ਚੱਲ ਸਕਦੇ ਹਨ।
- **ਪ੍ਰਦਾਤਾ-ਅਗਨੋਸਟਿਕ ਹੋਣਾ** - ਤੁਹਾਡੇ ਮਨਪਸੰਦ SDK ਦੁਆਰਾ ਜਿਵੇਂ Azure OpenAI ਅਤੇ OpenAI ਨਾਲ ਏਜੰਟ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ।
- **ਖੁੱਲੇ ਮਿਆਰ ਆਪਸੀ ਸੰਪਰਕ** - ਏਜੰਟ-ਤੋਂ-ਏਜੰਟ (A2A) ਅਤੇ ਮਾਡਲ ਸੰਦਰਭ ਪ੍ਰੋਟੋਕੌਲ (MCP) ਵਰਗੇ ਪ੍ਰੋਟੋਕੌਲਾਂ ਨੂੰ ਵਰਤ ਕੇ ਹੋਰ ਏਜੰਟਾਂ ਅਤੇ ਟੂਲਾਂ ਨੂੰ ਖੋਜ ਅਤੇ ਵਰਤ ਸਕਦੇ ਹਨ।
- **ਪਲੱਗਇਨ ਅਤੇ ਕਨੈਕਟਰ** - ਡਾਟਾ ਅਤੇ ਮੈਮੋਰੀ ਸੇਵਾਵਾਂ ਜਿਵੇਂ Microsoft Fabric, SharePoint, Pinecone ਅਤੇ Qdrant ਨਾਲ ਕਨੈਕਸ਼ਨ ਬਣਾਈਏ।

ਆਓ ਵੇਖੀਏ ਕਿ ਇਹ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਕੁਝ ਮੁੱਖ ਸੰਕਲਪਾਂ 'ਤੇ ਕਿਵੇਂ ਲਾਗੂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ।

## ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੁੱਖ ਸੰਕਲਪ

### ਏਜੰਟ

![Agent Framework](../../../translated_images/pa/agent-components.410a06daf87b4fef.webp)

**ਏਜੰਟ ਬਣਾਉਣਾ**

ਏਜੰਟ ਬਣਾਉਣਾ inference ਸਰਵਿਸ (LLM ਪ੍ਰਦਾਤਾ), AI ਏਜੰਟ ਲਈ ਹੁਕਮਾਂ ਦਾ ਸੈੱਟ ਨੇਮ ਕਰਕੇ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ਉਪਰੋਕਤ `Azure OpenAI` ਦੀ ਵਰਤੋਂ ਕਰ ਰਿਹਾ ਹੈ ਪਰ ਏਜੰਟ ਵੱਖ-ਵੱਖ ਸਰਵਿਸਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ ਜਿਵੇਂ `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ਜਾਂ [MiniMax](https://platform.minimaxi.com/), ਜੋ OpenAI-ਸੰਗਤ API ਤੇ ਵੱਡੇ ਸੰਦਰਭ ਵਿੰਡੋ (204K ਟੋਕਨ ਤੱਕ) ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ਜਾਂਦੋਰੇ ਏਜੰਟਾਂ ਲਈ A2A ਪ੍ਰੋਟੋਕਾਲ ਦੀ ਵਰਤੋਂ ਕਰ ਰਿਹਾ ਹੈ:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ਏਜੰਟ ਚਲਾਉਣਾ**

ਏਜੰਟਾਂ ਨੂੰ `.run` ਜਾਂ `.run_stream` ਮੈਥਡਾਂ ਨਾਲ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ ਜੋ ਨਾਨ-ਸਟਰੀਮਿੰਗ ਜਾਂ ਸਟਰੀਮਿੰਗ ਜਵਾਬਾਂ ਲਈ ਹੈ।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ਹਰ ਏਜੰਟ ਦੌੜ ਵਿੱਚ `max_tokens`, `tools` (ਜੋ ਟੂਲ ਏਜੰਟ ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ) ਅਤੇ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਲਈ ਵਿਕਲਪ ਮਿਲਦੇ ਹਨ।

ਇਹ ਸਾਡੇ ਲਈ ਲਾਭਦਾਇਕ ਹੈ ਜਦੋਂ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਮਾਡਲ ਜਾਂ ਟੂਲ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ ਵਰਤੋਂਕਰਤਾ ਦੇ ਕੰਮ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ।

**ਟੂਲ**

ਟੂਲ ਗੱਲਬਾਤ ਦੌਰਾਨ ਜਾਂ ਏਜੰਟ ਬਣਾਉਣ ਸਮੇਂ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ਜਦੋਂ ਸਿੱਧਾ ਇੱਕ ਚੈਟਏਜੰਟ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੋਵੇ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ਅਤੇ ਏਜੰਟ ਚਲਾਉਂਦਿਆਂ:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ਸਿਰਫ਼ ਇਸ ਦੌੜ ਲਈ ਉਪਲਬਧ ਟੂਲ )
```

**ਏਜੰਟ ਥ੍ਰੇਡਸ**

ਏਜੰਟ ਥ੍ਰੇਡਸ ਬਹੁ-ਟਰਨ ਗੱਲਬਾਤਾਂ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਥ੍ਰੇਡ ਬਣਾਈਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ:

- `get_new_thread()` ਵਰਤ ਕੇ ਜੋ ਸਮੇਂ ਸਿਰ ਥ੍ਰੇਡ ਸੰਭਾਲਦਾ ਹੈ
- ਜਦੋਂ ਏਜੰਟ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ ਤਾਂ ਆਪਣੇ ਆਪ ਥ੍ਰੇਡ ਬਣਾਉਣਾ ਜੋ ਸਿਰਫ ਮੌਜੂਦਾ ਦੌੜ ਦੌਰਾਨ ਰਹਿੰਦਾ ਹੈ।

ਥ੍ਰੇਡ ਬਣਾਉਣ ਲਈ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਹੁੰਦਾ ਹੈ:

```python
# ਨਵਾਂ ਥ੍ਰੇਡ ਬਣਾਓ।
thread = agent.get_new_thread() # ਥ੍ਰੇਡ ਨਾਲ ਏਜੰਟ ਨੂੰ ਚਲਾਓ।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

ਫਿਰ ਤੁਸੀਂ ਇਸ ਥ੍ਰੇਡ ਨੂੰ ਭਵਿੱਖ ਲਈ ਸਟੋਰ ਕਰਨ ਲਈ ਸੀਰੀਅਲਾਈਜ਼ ਕਰ ਸਕਦੇ ਹੋ:

```python
# ਇੱਕ ਨਵੀਂ ਥਰੇਡ ਬਣਾਓ।
thread = agent.get_new_thread() 

# ਥਰੇਡ ਦੇ ਨਾਲ agent ਨੂੰ ਚਲਾਓ।

response = await agent.run("Hello, how are you?", thread=thread) 

# ਸਟੋਰੇਜ ਲਈ ਥਰੇਡ ਨੂੰ ਸੀਰੀਅਲਾਈਜ਼ ਕਰੋ।

serialized_thread = await thread.serialize() 

# ਸਟੋਰੇਜ ਤੋਂ ਲੋਡ ਕਰਨ ਤੋਂ ਬਾਅਦ ਥਰੇਡ ਦੀ ਸਥਿਤੀ ਨੂੰ ਡੀਸੀਰੀਅਲਾਈਜ਼ ਕਰੋ।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ਏਜੰਟ ਮਿਡਲਵੇਅਰ**

ਏਜੰਟ ਯੂਜ਼ਰ ਦੇ ਕੰਮ ਪੂਰੇ ਕਰਨ ਲਈ ਟੂਲਾਂ ਅਤੇ LLMs ਨਾਲ ਗੱਲਬਾਤ ਕਰਦੇ ਹਨ। ਕੁਝ ਸਥਿਤੀਆਂ ਵਿੱਚ, ਅਸੀਂ ਇਨ੍ਹਾਂ ਦੇ ਵਿਚਕਾਰ ਕੁਝ ਐਕਸ਼ਨ ਕਰਨ ਜਾਂ ਨਿਗਰਾਨੀ ਕਰਨੇ ਚਾਹੁੰਦੇ ਹਾਂ। ਏਜੰਟ ਮਿਡਲਵੇਅਰ ਸਾਨੂੰ ਇਹ ਕਰਨ ਦੀ ਯੋਗਤਾ ਦਿੰਦਾ ਹੈ:

*ਫੰਕਸ਼ਨ ਮਿਡਲਵੇਅਰ*

ਇਹ ਮਿਡਲਵੇਅਰ ਐਜੰਟ ਅਤੇ ਫੰਕਸ਼ਨ/ਟੂਲ ਜਿਹੜਾ ਇਹ ਕਾਲ ਕਰਨ ਵਾਲਾ ਹੈ, ਦੇ ਵਿੱਚਕਾਰ ਇੱਕ ਐਕਸ਼ਨ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਉਦਾਹਰਣ ਵਜੋਂ, ਤੁਸੀਂ ਫੰਕਸ਼ਨ ਕਾਲ 'ਤੇ ਲਾਇਗਿੰਗ ਕਰ ਸਕਦੇ ਹੋ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ `next` ਇਹ ਸੂਚਿਤ ਕਰਦਾ ਹੈ ਕਿ ਅਗਲਾ ਮਿਡਲਵੇਅਰ ਜਾਂ ਅਸਲੀ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨਾ ਹੈ।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ਪ੍ਰੀ-ਪ੍ਰੋਸੈਸਿੰਗ: ਫੰਕਸ਼ਨ ਇਗਜ਼ੀਕਿਊਸ਼ਨ ਤੋਂ ਪਹਿਲਾਂ ਲੌਗ
    print(f"[Function] Calling {context.function.name}")

    # ਅਗਲੇ ਮਿਡਲਵੇਅਰ ਜਾਂ ਫੰਕਸ਼ਨ ਇਗਜ਼ੀਕਿਊਸ਼ਨ ਵੱਲ ਜਾਰੀ ਰੱਖੋ
    await next(context)

    # ਪੋਸਟ-ਪ੍ਰੋਸੈਸਿੰਗ: ਫੰਕਸ਼ਨ ਇਗਜ਼ੀਕਿਊਸ਼ਨ ਤੋਂ ਬਾਅਦ ਲੌਗ
    print(f"[Function] {context.function.name} completed")
```

*ਚੈਟ ਮਿਡਲਵੇਅਰ*

ਇਹ ਮਿਡਲਵੇਅਰ ਏਜੰਟ ਅਤੇ LLM ਵਿਚਕਾਰ ਦੀਆਂ ਬੇਨਤੀਆਂ 'ਤੇ ਐਕਸ਼ਨ ਜਾਂ ਲਾਈਗਿੰਗ ਕਰਦਾ ਹੈ।

ਇਸ ਵਿੱਚ AI ਸਰਵਿਸ ਨੂੰ ਭੇਜੇ ਜਾ ਰਹੇ `messages` ਵਰਗਾ ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਹੁੰਦੀ ਹੈ।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ਪ੍ਰੀ-ਪ੍ਰੋਸੈਸਿੰਗ: AI ਕਾਲ ਤੋਂ ਪਹਿਲਾਂ ਲੌਗ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ਅਗਲੇ ਮਿਡਲਵੇਅਰ ਜਾਂ AI ਸੇਵਾ ਨੂੰ ਜਾਰੀ ਰੱਖੋ
    await next(context)

    # ਪੋਸਟ-ਪ੍ਰੋਸੈਸਿੰਗ: AI ਜਵਾਬ ਤੋਂ ਬਾਅਦ ਲੌਗ
    print("[Chat] AI response received")

```

**ਏਜੰਟ ਮੈਮੋਰੀ**

ਜਿਵੇਂ ਕਿ `Agentic Memory` ਪਾਠ ਵਿੱਚ ਕਿਹਾ ਗਿਆ, ਮੈਮੋਰੀ ਏਜੰਟ ਨੂੰ ਵੱਖ-ਵੱਖ ਸੰਦਰਭਾਂ ਵਿੱਚ ਕੰਮ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਉਂਦੀ ਹੈ। MAF ਵੱਖਰੇ ਕਿਸਮ ਦੀਆਂ ਮੈਮੋਰੀਆਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:

*ਇਨ-ਮੈਮੋਰੀ ਸਟੋਰੇਜ*

ਇਹ ਐਪਲੀਕੇਸ਼ਨ ਰਨਟਾਈਮ ਦੌਰਾਨ ਥ੍ਰੇਡਸ ਵਿੱਚ ਸਟੋਰ ਕੀਤੀ ਜਾਣ ਵਾਲੀ ਮੈਮੋਰੀ ਹੈ।

```python
# ਇਕ ਨਵੀਂ ਧਾਗਾ ਬਣਾਓ।
thread = agent.get_new_thread() # ਧਾਗੇ ਨਾਲ ਏਜੰਟ ਚਲਾਓ।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*ਪ੍ਰਸਿਸਟੈਂਟ ਮੇਸੇਜ*

ਇਹ ਮੈਮੋਰੀ ਵੱਖ-ਵੱਖ ਸੈਸ਼ਨਾਂ ਵਿੱਚ ਗੱਲਬਾਤ ਇਤਿਹਾਸ ਨੂੰ ਸਟੋਰ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ `chat_message_store_factory` ਵਰਤ ਕੇ ਪਰਿਭਾਸ਼ਿਤ ਹੋਈ ਹੈ:

```python
from agent_framework import ChatMessageStore

# ਇੱਕ ਕਸਟਮ ਸੁਨੇਹਾ ਸਟੋਰ ਬਣਾਓ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ਡਾਇਨੇਮਿਕ ਮੈਮੋਰੀ*

ਇਸ ਮੈਮੋਰੀ ਨੂੰ ਐਜੰਟ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਸੰਦਰਭ ਵਿੱਚ ਜੋੜਿਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਮੈਮੋਰੀ ਬਾਹਰੀ ਸੇਵਾਵਾਂ ਜਿਵੇਂ mem0 ਵਿੱਚ ਸਟੋਰ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ:

```python
from agent_framework.mem0 import Mem0Provider

# ਉन्नਤ ਮੈਮੋਰੀ ਯੋਗਤਾਵਾਂ ਲਈ Mem0 ਦੀ ਵਰਤੋਂ ਕਰਨਾ
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

**ਏਜੰਟ ਓਬਜ਼ਰਵੇਬਿਲਟੀ**

ਓਬਜ਼ਰਵੇਬਿਲਟੀ ਭਰੋਸੇਯੋਗ ਅਤੇ ਰੱਖ-ਰਖਾਅਯੋਗ ਏਜੰਟਿਕ ਪ੍ਰਣਾਲੀਆਂ ਬਣਾਉਣ ਲਈ ਅਹਮ ਹੈ। MAF OpenTelemetry ਨਾਲ ਏਕਤਾ ਕਰਦਾ ਹੈ ਜੋ ਵਧੀਆ ਓਬਜ਼ਰਵੇਬਿਲਟੀ ਲਈ ਟਰੇਸਿੰਗ ਅਤੇ ਮੀਟਰ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ਕੁਝ ਕਰੋ
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### ਵਰਕਫਲੋ

MAF ਅਜਿਹੇ ਵਰਕਫਲੋ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਕਿ ਕਿਸੇ ਟਾਸਕ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਪਹਿਲਾਂ ਤੋਂ ਪਰਿਭਾਸ਼ਿਤ ਕਦਮ ਹੁੰਦੇ ਹਨ ਅਤੇ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਏਆਈ ਏਜੰਟ ਹਿੱਸੇ ਵਜੋਂ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ।

ਵਰਕਫਲੋ ਵੱਖ-ਵੱਖ ਘਟਕਾਂ ਨਾਲ ਬਣੇ ਹੁੰਦੇ ਹਨ ਜੋ ਵਧੀਆ ਕੰਟਰੋਲ ਫਲੋ ਦੇਂਦੇ ਹਨ। ਵਰਕਫਲੋ **ਮਲਟੀ-ਏਜੰਟ ਆਰਕੇਸਟਰੈਸ਼ਨ** ਅਤੇ **ਚੈਕਪੌਇੰਟਿੰਗ** ਦੀ ਵੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ ਤਾਂ ਜੋ ਵਰਕਫਲੋ ਦੇ ਹਾਲਾਤ ਸੰਭਾਲੇ ਜਾ ਸਕਣ।

ਵਰਕਫਲੋ ਦੇ ਮੁੱਖ ਘਟਕ ਹਨ:

**ਐਗਜ਼ਿਕਿਊਟਰ**

ਐਗਜ਼ਿਕਿਊਟਰ ਇਨਪੁੱਟ ਸੰਦੇਸ਼ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਨ, ਆਪਣਾ ਕੰਮ ਕਰਦੇ ਹਨ ਅਤੇ ਫਿਰ ਇੱਕ ਆਉਟਪੁੱਟ ਸੰਦੇਸ਼ ਤਿਆਰ ਕਰਦੇ ਹਨ। ਇਹ ਵਰਕਫਲੋ ਨੂੰ ਵੱਡੇ ਕੰਮ ਵੱਲ ਅੱਗੇ ਵਧਾਉਂਦਾ ਹੈ। ਐਗਜ਼ਿਕਿਊਟਰ AI ਏਜੰਟ ਜਾਂ ਕਸਟਮ ਲਾਜਿਕ ਹੋ ਸਕਦੇ ਹਨ।

**ਏਜ**

ਏਜ ਵਰਕਫਲੋ ਵਿੱਚ ਸੰਦੈਸ਼ਾਂ ਦੇ ਫਲੋ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਨ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਹੋ ਸਕਦੇ ਹਨ:

*ਸਿੱਧੇ ਏਜ* - ਐਗਜ਼ਿਕਿਊਟਰਾਂ ਵਿੱਚ ਇੱਕੋ-ਇੱਕ ਕਨੈਕਸ਼ਨ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*ਸ਼ਰਤੀ ਏਜ* - ਜਦੋਂ ਕੋਈ ਸ਼ਰਤ ਪੂਰੀ ਹੁੰਦੀ ਹੈ ਤਦ ਸ਼ੁਰੂ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਉਦਾਹਰਣ ਵਜੋਂ, ਜਦੋਂ ਹੋਟਲ ਦੇ ਕਮਰੇ ਉਪਲਬਧ ਨਹੀਂ ਹੁੰਦੇ, ਐਗਜ਼ਿਕਿਊਟਰ ਹੋਰ ਵਿਕਲਪ ਸਝਾਓਂਦਾ ਹੈ।

*ਸਵਿੱਚ-ਕੇਸ ਏਜ* - ਵੱਖ-ਵੱਖ ਐਗਜ਼ਿਕਿਊਟਰਾਂ ਨੂੰ ਸੰਦੇਸ਼ ਮੰਗੇ ਗਏ ਸ਼ਰਤਾਂ ਤੇ ਰਾਹ ਦਿੰਦਾ ਹੈ। ਉਦਾਹਰਣ ਲਈ, ਜੇ ਯਾਤਰਾ ਵਾਲੇ ਗਾਹਕ ਨੂੰ ਪ੍ਰਾਥਮਿਕਤਾ ਪ੍ਰਾਪਤ ਹੈ ਤਾਂ ਉਹਨਾਂ ਦੇ ਕੰਮ ਹੋਰ ਵਰਕਫਲੋ ਰਾਹੀਂ ਮੁਕੰਮਲ ਹੁੰਦੇ ਹਨ।

*ਫੈਨ-ਆਊਟ ਏਜ* - ਇੱਕ ਸੰਦੇਸ਼ ਨੂੰ ਕਈ ਟਾਰਗਟਾਂ ਨੂੰ ਭੇਜਣਾ।

*ਫੈਨ-ਇਨ ਏਜ* - ਵੱਖ-ਵੱਖ ਐਗਜ਼ਿਕਿਊਟਰਾਂ ਤੋਂ ਕਈ ਸੰਦੇਸ਼ ਇਕੱਤਰ ਕਰਕੇ ਇੱਕ ਟਾਰਗਟ ਨੂੰ ਭੇਜਨਾ।

**ਇਵੈਂਟ**

ਵਰਕਫਲੋਜ਼ ਵਿੱਚ ਵਧੀਆ ਓਬਜ਼ਰਵੇਬਿਲਟੀ ਲਈ, MAF ਐਗਜ਼ਿਕਿਊਸ਼ਨ ਲਈ ਠੋਸ ਇਵੈਂਟ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜਿਵੇਂ:

- `WorkflowStartedEvent`  - ਵਰਕਫਲੋ ਚਾਲੂ ਹੁੰਦਾ ਹੈ
- `WorkflowOutputEvent` - ਵਰਕਫਲੋ ਇੱਕ ਆਉਟਪੁੱਟ ਬਣਾਉਂਦਾ ਹੈ
- `WorkflowErrorEvent` - ਵਰਕਫਲੋ ਵਿੱਚ ਗਲਤੀ ਆਉਂਦੀ ਹੈ
- `ExecutorInvokeEvent`  - ਐਗਜ਼ਿਕਿਊਟਰ ਕੰਮ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ
- `ExecutorCompleteEvent`  - ਐਗਜ਼ਿਕਿਊਟਰ ਕੰਮ ਮੁਕੰਮਲ ਕਰਦਾ ਹੈ
- `RequestInfoEvent` - ਇੱਕ ਬੇਨਤੀ ਜਾਰੀ ਹੁੰਦੀ ਹੈ

## ਉੱਨਤ MAF ਪੈਟਰਨ

ਉਪਰੋਕਤ ਸੈਕਸ਼ਨਾਂ ਵਿੱਚ ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੁੱਖ ਸੰਕਲਪ ਕਵਰ ਕੀਤੇ ਗਏ ਹਨ। ਜਿਵੇਂ ਤੁਸੀਂ ਹੋਰ ਜਟਿਲ ਏਜੰਟ ਬਣਾਉਂਦੇ ਹੋ, ਇੱਥੇ ਕੁਝ ਉੱਨਤ ਪੈਟਰਨ ਹਨ ਜੋ ਸੋਚਣ ਯੋਗ ਹਨ:

- **ਮਿਡਲਵੇਅਰ ਕਂਪੋਜ਼ੀਸ਼ਨ**: ਕੁਝ ਮਿਡਲਵੇਅਰ ਹેન્ડਲਰਾਂ (ਲਾਗਿੰਗ, ਪ੍ਰਮਾਣਿਕਤਾ, ਰੇਟ-ਲਿਮਿਟਿੰਗ) ਨੂੰ ਚੇਨ ਕਰਦੇ ਹੋਏ ਫੰਕਸ਼ਨ ਅਤੇ ਚੈਟ ਮਿਡਲਵੇਅਰ ਨਾਲ ਏਜੰਟ ਦੇ ਵਰਤਾਵ 'ਤੇ ਸੁਖੜ ਨਿਯੰਤਰਣ ਪ੍ਰਦਾਨ ਕਰੋ।
- **ਵਰਕਫਲੋ ਚੈਕਪੌਇੰਟਿੰਗ**: ਵਰਕਫਲੋ ਇਵੈਂਟ ਅਤੇ ਸੀਰੀਅਲਾਈਜੇਸ਼ਨ ਨਾਲ ਲੰਮੇ ਸਮੇਂ ਚੱਲਦੇ ਐਜੰਟ ਪ੍ਰਕਿਰਿਆਵਾਂ ਨੂੰ ਬਚਾਓ ਅਤੇ ਮੁੜ ਚਾਲੂ ਕਰੋ।
- **ਡਾਇਨੇਮਿਕ ਟੂਲ ਚੋਣ**: ਹਥਿਆਰ ਵਰਣਨਾਂ ਉੱਤੇ RAG ਨੂੰ MAF ਦੇ ਟੂਲ ਰਜਿਸਟਰੇਸ਼ਨ ਨਾਲ ਜੋੜ ਕੇ ਸਿਰਫ ਸੰਬੰਧਿਤ ਟੂਲ ਪ੍ਰਸ਼ਨ-ਪੱਧਰ ਤੇ ਪੇਸ਼ ਕਰੋ।
- **ਮਲਟੀ-ਏਜੰਟ ਹੈਂਡਾਫ**: ਵਰਕਫਲੋ ਏਜ ਅਤੇ ਸ਼ਰਤੀ ਰੂਟਿੰਗ ਲਈ ਵਰਤ ਕੇ ਵਿਸ਼ੇਸ਼ ਏਜੰਟਾਂ ਵਿਚਕਾਰ ਹੈਂਡਾਫ ਆਰਕੇਸਟਰੈਟ ਕਰੋ।

## ਮਾਇਕ੍ਰੋਸੌਫਟ ਫਾਉਂਡਰੀ 'ਤੇ LangChain / LangGraph ਐਜੰਟ ਦੀ ਮੇਜ਼ਬਾਨੀ

ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ **ਫਰੇਮਵਰਕ-ਇੰਟਰਓਪਰੇਬਲ** ਹੈ — ਤੁਸੀਂ ਸਿਰਫ MAF ਨਾਲ ਲਿਖੇ ਐਜੰਟਾਂ ਤੱਕ ਸੀਮਤ ਨਹੀਂ ਹੋ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ **LangChain** ਜਾਂ **LangGraph** ਨਾਲ ਬਣਿਆ ਇੱਕ ਏਜੰਟ ਹੈ, ਤਦ ਤੁਸੀਂ ਇਸਨੂੰ **Microsoft Foundry ਮੇਜ਼ਬਾਨ ਏਜੰਟ** ਵਜੋਂ ਚਲਾ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ Foundry ਰਨਟਾਈਮ, ਸੈਸ਼ਨ, ਸਕੇਲਿੰਗ, ਪਛਾਣ ਅਤੇ ਪ੍ਰੋਟੋਕਾਲ ਐਂਡਪੌਇੰਟ ਤੁਹਾਡੀ ਥਾਂ ਨੂੰ ਸੰਭਾਲੇ ਜਦ ਕਿ ਤੁਹਾਡਾ ਏਜੰਟ ਲਾਜਿਕ LangGraph ਵਿੱਚ ਰਹਿਣ ਦੁਗਾ।

ਇਹ `langchain_azure_ai.agents.hosting` ਪੈਕੇਜ ਨਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜੋ ਇੱਕ ਕੰਪਾਇਲ ਕੀਤੀ ਹੋਈ LangGraph ਗ੍ਰਾਫ ਨੂੰ ਹੇਠ ਲਿਖੇ ਪ੍ਰੋਟੋਕਾਲਾਂ ਉੱਤੇ ਖੁੱਲ੍ਹਾ ਕਰਦਾ ਹੈ ਜੋ Foundry ਦੇ ਮੇਜ਼ਬਾਨ ਏਜੰਟ ਵਰਤਦੇ ਹਨ।

**1. ਹੋਸਟਿੰਗ ਐਕਸਟ੍ਰਾ ਇੰਸਟਾਲ ਕਰੋ:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ਐਕਸਟ੍ਰਾ Foundry ਪ੍ਰੋਟੋਕਾਲ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰਦਾ ਹੈ: `azure-ai-agentserver-responses` (OpenAI-ਸੰਗਤ `/responses` ਐਂਡਪੌਇੰਟ) ਅਤੇ `azure-ai-agentserver-invocations` (ਜਨਰਲ `/invocations` ਐਂਡਪੌਇੰਟ)।

**2. ਇੱਕ ਹੋਸਟਿੰਗ ਪ੍ਰੋਟੋਕਾਲ ਚੁਣੋ:**

| ਪ੍ਰੋਟੋਕਾਲ | ਹੋਸਟ ਕਲਾਸ | ਐਂਡਪੌਇੰਟ | ਕਦੋਂ ਵਰਤਣਾ |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | ਤੁਸੀਂ OpenAI-ਸੰਗਤ ਚੈਟ, ਸਟਰੀਮਿੰਗ, ਜਵਾਬ ਇਤਿਹਾਸ ਅਤੇ ਗੱਲਬਾਤ ਥ੍ਰੇਡਿੰਗ ਚਾਹੁੰਦੇ ਹੋ — ਗੱਲਬਾਤੀ ਏਜੰਟਾਂ ਲਈ ਸਿਫਾਰਸ਼ੀ ਮੁੱਢਲਾ। |
| **Invocations** | `InvocationsHostServer` | `/invocations` | ਤੁਹਾਨੂੰ ਇੱਕ ਕਸਟਮ JSON ਸ਼ੇਪ, ਵੈੱਬਹੁੱਕ-ਸ਼ੈਲੀਲ ਐਂਡਪੌਇੰਟ ਜਾਂ ਗੈਰ-ਗੱਲਬਾਤੀ ਪ੍ਰਕਿਰਿਆ ਚਾਹੀਦੀ ਹੈ। |

ਕਿਉਂਕਿ **Responses API Foundry ਵਿੱਚ ਏਜੰਟ-ਸਟਾਈਲ ਵਿਕਾਸ ਲਈ ਮੁੱਖ API ਹੈ**, ਪ੍ਰਮੁੱਖ ਆਪਣੇ ਬਹੁਤ ਸਾਰੇ ਏਜੰਟਾਂ ਲਈ `ResponsesHostServer` ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ।

**3. ਵਾਤਾਵਰਣ ਚਲਾਓ (ਤੁਹਾਡੀ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ ਪਹਿਲਾਂ `az login` ਕਰੋ):**

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ਜਦੋਂ ਬਾਅਦ ਵਿੱਚ ਏਜੰਟ Foundry ਵਿੱਚ ਮੇਜ਼ਬਾਨ ਏਜੰਟ ਵਜੋਂ ਚਲੇਗਾ, ਤਾਂ ਪਲੇਟਫਾਰਮ `FOUNDRY_PROJECT_ENDPOINT` ਆਪਣੇ ਆਪ ਇੰਜੈਕਟ ਕਰਦਾ ਹੈ।

**4. Responses ਪ੍ਰੋਟੋਕਾਲ ਉੱਤੇ LangGraph ਏਜੰਟ ਖੁੱਲ੍ਹਾ ਕਰੋ:**

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

    # ਇਥੇ ChatOpenAI Foundry ਪ੍ਰੋਜੈਕਟ ਦੇ OpenAI-ਅਨੁਕੂਲ (Responses) ਐਂਡਪੌਇੰਟ ਨੂੰ ਟਾਰਗਟ ਕਰਦਾ ਹੈ।
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

ਇਥੇ `python main.py` ਨਾਲ ਇਸਨੂੰ ਲੋਕਲ ਚਲਾਓ, ਫਿਰ `http://localhost:8088/responses` ਨੂੰ Responses ਬੇਨਤੀ ਭੇਜੋ।

**ਮੁੱਖ ਵਿਹਾਰ:**

- **ਗੱਲਬਾਤਾਂ**: ਕਲਾਇੰਟ ਸੰਵਾਦ ਜਾਰੀ ਰੱਖਦੇ ਹਨ `previous_response_id` ਜਾਂ `conversation` ID ਭੇਜ ਕੇ। ਜੇਕਰ ਤੁਹਾਡਾ ਗ੍ਰਾਫ LangGraph ਚੈਕਪੌਇੰਟਰ ਨਾਲ ਕੰਪਾਇਲ ਕੀਤਾ ਗਿਆ ਹੈ, Foundry ਗੱਲਬਾਤ ਸਥਿਤੀ ਨੂੰ ਚੈਕਪੌਇੰਟ ਨਾਲ ਕੰਝੀਦਾ ਹੈ (ਪ੍ਰੋਡਕਸ਼ਨ ਵਿੱਚ ਡਿਊਰੇਬਲ ਚੈਕਪੌਇੰਟਰ ਵਰਤੋ; ਸਥਾਨਕ ਟੈਸਟਿੰਗ ਲਈ `MemorySaver` ਠੀਕ ਹੈ)।
- **ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ**: ਜੇਕਰ ਤੁਹਾਡਾ ਗ੍ਰਾਫ LangGraph `interrupt()` ਵਰਤਦਾ ਹੈ, `ResponsesHostServer` ਮੌਜੂਦਾ ਇੰਟਰਪਟ ਨੂੰ Responses `function_call` / `mcp_approval_request` ਵਸਤੂ ਵਜੋਂ ਪ੍ਰਗਟ ਕਰਦਾ ਹੈ, ਅਤੇ ਕਲਾਇੰਟ ਮੈਚਿੰਗ `function_call_output` / `mcp_approval_response` ਨਾਲ ਜਾਰੀ ਰੱਖਦੇ ਹਨ।
- **Foundry ਵਿੱਚ ਨਿਯੁਕਤ ਕਰੋ**: Azure Developer CLI ਵਰਤੋਂ ਕਰੋ — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ਸਥਾਨਕ, Docker ਲੋੜੀਂਦਾ ਹੈ), ਫਿਰ `azd provision` ਅਤੇ `azd deploy`। ਮੇਜ਼ਬਾਨ ਏਜੰਟ ਨਿਯੁਕਤੀ ਲਈ **Foundry ਪ੍ਰੋਜੈਕਟ ਮੈਨੇਜਰ** ਦੀ ਭੂਮਿਕਾ ਲਾਜ਼ਮੀ ਹੈ।

ਇਸ ਉਦਾਹਰਣ ਦਾ ਚਲਣ ਵਾਲਾ ਸੰસ્કਰਣ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ਵਿੱਚ ਹੈ। ਪੂਰੀ ਵੇਰਵਾ ਲਈ (Invocations ਪ੍ਰੋਟੋਕਾਲ, ਕਸਟਮ ਬੇਨਤੀ ਸਕੀਮਾ, ਅਤੇ ਸਮੱਸਿਆ ਨਿਵਾਰਨ), ਵੇਖੋ [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)।

## ਕੋਡ ਨਮੂਨੇ 

ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਲਈ ਕੋਡ ਨਮੂਨੇ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ `xx-python-agent-framework` ਅਤੇ `xx-dotnet-agent-framework` ਫਾਈਲਾਂ ਹੇਠਾਂ ਮਿਲ ਸਕਦੇ ਹਨ।

## ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲਣ, ਦਫਤਰ ਘੰਟੇ ਹਾਜ਼ਰ ਕਰਨ ਅਤੇ ਆਪਣੇ AI ਏਜੰਟ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲਈ [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਵੋ।
## ਪਿਛਲਾ ਪਾਠ

[Memory for AI Agents](../13-agent-memory/README.md)

## ਅਗਲਾ ਪਾਠ

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->