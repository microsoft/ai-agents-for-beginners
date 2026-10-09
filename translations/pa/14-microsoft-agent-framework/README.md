# ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਖੋਜ

![Agent Framework](../../../translated_images/pa/lesson-14-thumbnail.90df0065b9d234ee.webp)

### ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ ਇਹ ਮੁਕਾਵਲੇ ਕੀਤੇ ਜਾਣਗੇ:

- ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਸਮਝ: ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਮੁੱਲ  
- ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੁੱਖ ਧਾਰਣਾ ਦੀ ਖੋਜ
- ਅਗੇਤੜ੍ਹੇ MAF ਪੈਟਰਨ: ਵਰਕਫਲੋ, ਮਿਡਲਵੇਅਰ ਅਤੇ ਮੈਮੋਰੀ

## ਸਿੱਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਨੂੰ ਸਮਾਪਤ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਜਾਣੋਗੇ ਕਿ ਕਿਵੇਂ:

- ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਡਕਸ਼ਨ ਤਿਆਰ AI ਏਜੰਟ ਬਣਾਉਣੇ
- ਆਪਣੇ ਏਜੰਟਿਕ ਉਪਯੋਗ ਮਾਮਲਿਆਂ ਲਈ ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੂਲ ਫੀਚਰ ਲਾਗੂ ਕਰਨੇ
- ਅਗੇਤੜ੍ਹ ਪੈਟਰਨਾਂ ਜਿਵੇਂ ਕਿ ਵਰਕਫਲੋ, ਮਿਡਲਵੇਅਰ ਅਤੇ ਨਿਗਰਾਨੀ ਦੀ ਵਰਤੋਂ ਕਰਨੀ

## ਕੋਡ ਦੇ ਨਮੂਨੇ 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ਲਈ ਕੋਡ ਦੇ ਨਮੂਨੇ ਇਸ ਰਿਪੋਜਟਰੀ ਵਿੱਚ `xx-python-agent-framework` ਅਤੇ `xx-dotnet-agent-framework` ਫਾਈਲਾਂ ਦੇ ਤਹਿਤ ਮਿਲ ਸਕਦੇ ਹਨ।

## ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਸਮਝ

![Framework Intro](../../../translated_images/pa/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ਮਾਇਕ੍ਰੋਸੋਫਟ ਦਾ ਏਕੱਠਾ ਫਰੇਮਵਰਕ ਹੈ ਜੋ AI ਏਜੰਟ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਉਤਪਾਦਨ ਅਤੇ ਖੋਜ ਵਾਲੇ ਮਾਹੌਲਾਂ ਵਿੱਚ ਵੇਖੇ ਗਏ ਵੱਖ-ਵੱਖ ਰੂਪਾਂ ਵਾਲੇ ਏਜੰਟਿਕ ਉਪਯੋਗ ਮਾਮਲਿਆਂ ਨੂੰ ਸੰਬੋਧਨ ਕਰਨ ਲਈ ਲਚਕੀਲਾਪੁਰਨਤਾ ਦਿੰਦਾ ਹੈ, ਜਿਵੇਂ:

- **ਕ੍ਰਮਬੱਧ ਏਜੰਟ ਅਰਕੈਸਟਰੈਸ਼ਨ** ਜਿੱਥੇ ਕਦਮ-ਦਰ-ਕਦਮ ਵਰਕਫਲੋਜ਼ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।
- **ਸਮਕਾਲੀ ਅਰਕੈਸਟਰੈਸ਼ਨ** ਜਿੱਥੇ ਏਜੰਟ ਇੱਕੋ ਸਮੇਂ ਕੰਮ ਖਤਮ ਕਰਨੇ ਹੁੰਦੇ ਹਨ।
- **ਗਰੁੱਪ ਚੈਟ ਅਰਕੈਸਟਰੈਸ਼ਨ** ਜਿੱਥੇ ਏਜੰਟ ਇੱਕ ਕੰਮ ’ਤੇ ਸਹਿਯੋਗ ਕਰ ਸਕਦੇ ਹਨ।
- **ਹੈਂਡਆਫ਼ਟ ਅਰਕੈਸਟਰੈਸ਼ਨ** ਜਿੱਥੇ ਇੱਕ-ਦੂਜੇ ਨੂੰ ਸਬਟਰਾਸਕ ਸਮਾਪਤ ਹੋਣ ’ਤੇ ਕੰਮ ਸੌਂਪਿਆ ਜਾਂਦਾ ਹੈ।
- **ਮੈਗਨੇਟਿਕ ਅਰਕੈਸਟਰੈਸ਼ਨ** ਜਿੱਥੇ ਮੈਨੇਜਰ ਏਜੰਟ ਇੱਕ ਟਾਸਕ ਸੂਚੀ ਬਣਾਉਂਦਾ ਅਤੇ ਸੋਧਦਾ ਹੈ ਅਤੇ ਸਬਏਜੰਟਾਂ ਦੀ ਸਹਿ-ਸੰਯੋਜਨਾ ਕਰਦਾ ਹੈ ਤਾਯ ਕਿ ਕੰਮ ਪੂਰਾ ਹੋ ਸਕੇ।

ਉਤਪਾਦਨ ਵਿੱਚ AI ਏਜੰਟ ਵੰਡਣ ਲਈ, MAF ਵਿੱਚ ਇਹ ਵੀ ਸ਼ਾਮਿਲ ਹੈ:

- **ਨਿਗਰਾਨੀ** OpenTelemetry ਦੀ ਵਰਤੋਂ ਨਾਲ, ਜਿੱਥੇ AI ਏਜੰਟ ਦੀ ਹਰ ਕਾਰਵਾਈ ਜਿਵੇਂ ਸੰਦ ਬੁਲਾਣਾ, ਅਰਕੈਸਟਰੈਸ਼ਨ ਕਦਮ, ਤਰਕ ਪ੍ਰਵਾਹ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਨਿਗਰਾਨੀ ਦਿਖਾਈ ਜਾਂਦੀ ਹੈ ਮਾਇਕ੍ਰੋਸੋਫਟ ਫਾਉਂਡਰੀ ਡੈਸ਼ਬੋਰਡਾਂ ਰਾਹੀਂ।
- **ਸੁਰੱਖਿਆ** ਮਾਇਕ੍ਰੋਸੋਫਟ ਫਾਉਂਡਰੀ ’ਤੇ ਏਜੰਟਸ ਨੂੰ ਮੂਲ ਤੌਰ ’ਤੇ ਹੋਸਟ ਕਰਕੇ ਜੋ ਕਿ ਰੋਲ-ਅਧਾਰਿਤ ਪਹੁੰਚ, ਨਿੱਜੀ ਡਾਟਾ ਹੈਂਡਲਿੰਗ ਅਤੇ ਬਿਲਟ-ਇਨ ਸਮੱਗਰੀ ਸੁਰੱਖਿਆ ਵਰਗੇ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਰੱਖਦਾ ਹੈ।
- **ਟਿਕਾਊਪਨ** ਕਿਉਂਕਿ ਏਜੰਟ ਥ੍ਰੈਡ ਅਤੇ ਵਰਕਫਲੋਜ਼ ਰੁਕ ਸੱਕਦੇ ਹਨ, ਫਿਰ ਸ਼ੁਰੂ ਹੋ ਸਕਦੇ ਹਨ ਅਤੇ ਗਲਤੀਆਂ ਤੋਂ ਬਚ ਸਕਦੇ ਹਨ ਜੋ ਵੱਡੀ ਸਮੇਂਵਧੀ ਕਾਰਜਕ੍ਰਮ ਸਹਾਇਕ ਹੈ।
- **ਨਿਯੰਤਰਣ** ਜਿਥੇ ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ ਲੋੜੀਂਦੀ ਹੁੰਦੀ ਹੈ, ਮਨੁੱਖ-ਵਿੱਚ-ਲੂਪ ਵਰਕਫਲੋਜ਼ ਦਾ ਸਹਿਯੋਗ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦਾ ਮਨੋਰਥ ਇਹ ਵੀ ਹੈ ਕਿ ਇਹ ਅੰਤਰ-ਚਾਲੂ ਹੋਵੇ:

- **ਕਲਾਉਡ-ਐਗਨੋਸਟੀਕ ਹੋਣਾ** - ਏਜੰਟ ਕੰਟੇਨਰਾਂ ਵਿੱਚ, ਓਨ-ਪ੍ਰੇਮਿਸ ਅਤੇ ਵੱਖ-ਵੱਖ ਕਲਾਉਡਾਂ ’ਚ ਚਲ ਸਕਦੇ ਹਨ।
- **ਪ੍ਰੋਵਾਈਡਰ-ਐਗਨੋਸਟੀਕ ਹੋਣਾ** - ਆਪਣੇ ਮਨਪਸੰਦ SDK ਜਿਵੇਂ Azure OpenAI ਅਤੇ OpenAI ਰਾਹੀਂ ਏਜੰਟ ਬਣਾਉਣਾ।
- **ਖੁੱਲੇ ਮਿਆਰਾਂ ਨੂੰ ਜੋੜਨਾ** - ਏਜੰਟ-ਟੂ-ਏਜੰਟ (A2A) ਅਤੇ ਮਾਡਲ ਸੰਦਰਭ ਪ੍ਰੋਟੋਕਾਲ (MCP) ਵਰਗੇ ਪ੍ਰੋਟੋਕਾਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਰ ਏਜੰਟ ਅਤੇ ਟੂਲ ਖੋਜਣਾ ਅਤੇ ਵਰਤਣਾ।
- **ਪਲੱਗਇਨ ਅਤੇ ਕਨੈਕਟਰ** - ਡਾਟਾ ਅਤੇ ਮੈਮੋਰੀ ਸੇਵਾਵਾਂ ਜਿਵੇਂ ਮਾਇਕ੍ਰੋਸੋਫਟ ਫੈਬਰਿਕ, ਸ਼ੇਅਰਪੌਇੰਟ, ਪਾਈਨਕੋਨ ਅਤੇ ਕਿਊਡ੍ਰੈਂਟ ਨਾਲ ਜੋੜ।

ਚਲੋ ਦੇਖੀਏ ਕਿ ਇਹ ਗੁਣ ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਕੁਝ ਮੂਲ ਧਾਰਣਾਵਾਂ ’ਚ ਕਿਵੇਂ ਲਾਗੂ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

## ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀਆਂ ਮੁੱਖ ਧਾਰਣਾਵਾਂ

### ਏਜੰਟ

![Agent Framework](../../../translated_images/pa/agent-components.410a06daf87b4fef.webp)

**ਏਜੰਟ ਬਣਾਉਣਾ**

ਏਜੰਟ ਬਣਾਉਣਾ ਇੱਕ ਸੇਵਾ (LLM ਪ੍ਰੋਵਾਈਡਰ) ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਕੇ, AI ਏਜੰਟ ਨੂੰ ਹੁਕਮਾਂ ਦਾ ਇੱਕ ਸੈੱਟ ਦੇ ਕੇ ਅਤੇ ਇੱਕ ਨਿਰਧਾਰਤ `name` ਸੁੰਪ ਕੇ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ਉਪਰ ਦਿੱਤਾ ਉਦਾਹਰਨ `Azure OpenAI` ਦੀ ਵਰਤੋਂ ਕਰ ਰਿਹਾ ਹੈ, ਪਰ ਏਜੰਟ ਵੱਖ-ਵੱਖ ਸੇਵਾਵਾਂ ਨਾਲ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ ਜਿਵੇਂ `Microsoft Foundry Agent Service`:

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

ਜਾਂ [MiniMax](https://platform.minimaxi.com/), ਜੋ ਵੱਡੇ ਸੰਦਰਭ ਵਿੰਡੋ (204K ਟੋਕਨ ਤੱਕ) ਦੇ ਨਾਲ OpenAI-ਅਨੁਕੂਲ API ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ਜਾਂ A2A ਪ੍ਰੋਟੋਕਾਲ ਰਾਹੀਂ ਰਿਮੋਟ ਏਜੰਟ:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ਏਜੰਟ ਚਲਾਉਣਾ**

ਏਜੰਟ `.run` ਜਾਂ `.run_stream` ਮੈਥਡਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਘੋੜਿਆ ਜਾਂਦਾ ਹੈ ਜੇਕਰ ਨਾਹ-ਸਟ੍ਰੀਮਿੰਗ ਜਾਂ ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬਾਂ ਲਈ।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ਹਰ ਏਜੰਟ ਚਲਾਉਣ ਸਮੇਂ ਵਿਕਲਪ ਵੀ ਹੋ ਸਕਦੇ ਹਨ ਜਿਵੇਂ ਕਿ `max_tokens` ਜੋ ਏਜੰਟ ਵਰਤਦਾ ਹੈ, `tools` ਜੋ ਏਜੰਟ ਬੁਲਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਉਸ ਏਜੰਟ ਲਈ ਵਰਤੇ ਜਾਣ ਵਾਲੇ `model` ਤੱਕ।

ਇਹ ਉਪਯੋਗੀ ਹੈ ਜਿੱਥੇ ਵੱਖ-ਵੱਖ ਮਾਡਲ ਜਾਂ ਟੂਲ ਇੱਕ ਉਪਭੋਗੀ ਦੇ ਕੰਮ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਲਾਜ਼ਮੀ ਹੁੰਦੇ ਹਨ।

**ਟੂਲ**

ਟੂਲ ਤਿਆਰ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ ਜਦੋਂ ਏਜੰਟ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੋਵੇ:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ਜਦੋਂ ਸੀਧੇ ਤੌਰ 'ਤੇ ਇੱਕ ChatAgent ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੋਵੇ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ਅਤੇ ਜਦੋਂ ਏਜੰਟ ਚਲਾਇਆ ਜਾ ਰਿਹਾ ਹੋਵੇ:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ਇਸ ਦੌੜ ਲਈ ਸਿਰਫ਼ ਉਪਲਬਧ ਟੂਲ )
```

**ਏਜੰਟ ਥ੍ਰੈਡ**

ਏਜੰਟ ਥ੍ਰੈਡ ਬਹੁ-ਮੁੜ ਸੰਵਾਦਾਂ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਥ੍ਰੈਡ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ:

- `get_new_thread()` ਨੂੰ ਵਰਤ ਕੇ ਜੋ ਥ੍ਰੈਡ ਨੂੰ ਸਮੇਂ ਦੇ ਨਾਲ ਸੇਵ ਕਰ ਸਕਦਾ ਹੈ
- ਏਜੰਟ ਚਲਾਉਣ ਸਮੇਂ ਆਪਣੇ ਆਪ ਇੱਕ ਥ੍ਰੈਡ ਬਣਾਉਣਾ ਜੋ ਸਿਰਫ ਮੌਜੂਦਾ ਚਲਾਉਣ ਤੱਕ ਹੀ ਰਹਿੰਦਾ ਹੈ।

ਥ੍ਰੈਡ ਬਣਾਉਣ ਲਈ, ਕੋਡ ਇਸ ਤਰਾ ਹੈ:

```python
# ਨਵੀਂ ਥ੍ਰੇਡ ਬਣਾਓ।
thread = agent.get_new_thread() # ਥ੍ਰੇਡ ਨਾਲ ਏਜੰਟ ਚਲਾਓ।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

ਤੁਸੀਂ ਫਿਰ ਥ੍ਰੈਡ ਨੂੰ ਸੰਰੱਖਿਤ ਕਰਨ ਲਈ ਸੀਰੀਅਲਾਈਜ਼ ਵੀ ਕਰ ਸਕਦੇ ਹੋ:

```python
# ਨਵੀਂ ਥ੍ਰੈੱਡ ਬਣਾਓ।
thread = agent.get_new_thread() 

# ਥ੍ਰੈੱਡ ਨਾਲ ਏਜੰਟ ਚਲਾਓ।

response = await agent.run("Hello, how are you?", thread=thread) 

# ਸਟੋਰੇਜ ਲਈ ਥ੍ਰੈੱਡ ਨੂੰ ਸੀਰੀਅਲਾਈਜ਼ ਕਰੋ।

serialized_thread = await thread.serialize() 

# ਸਟੋਰੇਜ ਤੋਂ ਲੋਡ ਕਰਨ ਤੋਂ ਬਾਅਦ ਥ੍ਰੈੱਡ ਦੀ ਸਥਿਤੀ ਨੂੰ ਡੀਸੀਰੀਅਲਾਈਜ਼ ਕਰੋ।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ਏਜੰਟ ਮਿਡਲਵੇਅਰ**

ਏਜੰਟ ਟੂਲ ਅਤੇ LLMs ਨਾਲ ਦੁਆਰਾ ਉਪਭੋਗੀ ਦੇ ਕੰਮ ਪੂਰੇ ਕਰਦਾ ਹੈ। ਕੁਝ ਸਥਿਤੀਆਂ ਵਿੱਚ, ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ਇਹ ਭੇਦਾਂ ਦੀ ਪਰਤੀ ਜਾਂ ਕਾਰਵਾਈ ਕੀਤੀ ਜਾਵੇ। ਏਜੰਟ ਮਿਡਲਵੇਅਰ ਸਾਡੇ ਲਈ ਇਹ ਕੀਤੇ ਜਾਂਦਾ ਹੈ:

*ਫੰਕਸ਼ਨ ਮਿਡਲਵੇਅਰ*

ਇਹ ਮਿਡਲਵੇਅਰ ਸਾਨੂੰ ਏਜੰਟ ਅਤੇ ਫੰਕਸ਼ਨ/ਟੂਲ ਵਿਚਕਾਰ ਕਾਲ ਵਿੱਚ ਕਾਰਵਾਈ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜਦੋਂ ਤੁਸੀਂ ਫੰਕਸ਼ਨ ਕਾਲ ਦਾ ਲੋਗਿੰਗ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ, `next` ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਅਗਲਾ ਮਿਡਲਵੇਅਰ ਜਾਂ ਅਸਲ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਨਾ ਹੈ।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ਪ੍ਰੀ-ਪ੍ਰੋਸੈਸਿੰਗ: ਫੰਕਸ਼ਨ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਲੌਗ ਕਰੋ
    print(f"[Function] Calling {context.function.name}")

    # ਅਗਲੇ ਮਿਡਲਵੇਅਰ ਜਾਂ ਫੰਕਸ਼ਨ ਚਲਾਣ ਲਈ ਜਾਰੀ ਰੱਖੋ
    await next(context)

    # ਪੋਸਟ-ਪ੍ਰੋਸੈਸਿੰਗ: ਫੰਕਸ਼ਨ ਚਲਾਉਣ ਤੋਂ ਬਾਅਦ ਲੌਗ ਕਰੋ
    print(f"[Function] {context.function.name} completed")
```

*ਚੈਟ ਮਿਡਲਵੇਅਰ*

ਇਹ ਮਿਡਲਵੇਅਰ ਸਾਡੇ ਲਈ ਏਜੰਟ ਅਤੇ LLM ਵਿਚਕਾਰ ਦੀਆਂ ਬੇਨਤੀਆਂ ਵਿੱਚ ਕਾਰਵਾਈ ਜਾਂ ਲੋਗਿੰਗ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

ਇਸ ਵਿੱਚ ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਹੁੰਦੀ ਹੈ ਜਿਵੇਂ `messages` ਜੋ AI ਸੇਵਾ ਨੂੰ ਭੇਜੇ ਜਾ ਰਹੇ ਹਨ।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ਪ੍ਰੀ-ਪ੍ਰੋਸੈਸਿੰਗ: ਏਆਈ ਕਾਲ ਤੋਂ ਪਹਿਲਾਂ ਲਾਗ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ਅਗਲੇ ਮਿਡਲਵੇਅਰ ਜਾਂ ਏਆਈ ਸਰਵਿਸ ਵੱਲ ਜਾਰੀ ਰੱਖੋ
    await next(context)

    # ਪੋਸਟ-ਪ੍ਰੋਸੈਸਿੰਗ: ਏਆਈ ਜਵਾਬ ਦੇ ਬਾਅਦ ਲਾਗ
    print("[Chat] AI response received")

```

**ਏਜੰਟ ਮੈਮੋਰੀ**

`Agentic Memory` ਪਾਠ ਵਿੱਚ ਕਵਰ ਕੀਤੇ ਗਏ ਮੁਤਾਬਕ, ਮੈਮੋਰੀ ਇਕ ਮਹੱਤਵਪੂਰਨ ਤੱਤ ਹੈ ਜੋ ਏਜੰਟ ਨੂੰ ਵੱਖਰੇ ਸੰਦਰਭਾਂ ਉੱਪਰ ਕੰਮ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ। MAF ਵੱਖ-ਵੱਖ ਕਿਸਮ ਦੀ ਮੈਮੋਰੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:

*ਇਨ-ਮੈਮੋਰੀ ਸਟੋਰੇਜ*

ਇਹ ਮੈਮੋਰੀ ਐਪਲੀਕੇਸ਼ਨ ਰਨਟਾਈਮ ਦੌਰਾਨ ਥ੍ਰੈਡਾਂ ਵਿੱਚ ਸਟੋਰ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

```python
# ਇੱਕ ਨਵਾਂ ਥ੍ਰੇਡ ਬਣਾਓ।
thread = agent.get_new_thread() # ਥ੍ਰੇਡ ਨਾਲ ਏਜੰਟ ਨੂੰ ਚਲਾਓ।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*ਪੇਰਸਿਸਟੈਂਟ ਮੈਸੇਜ*

ਇਹ ਮੈਮੋਰੀ ਵੱਖ-ਵੱਖ ਸੈਸ਼ਨਾਂ ਦਰਮਿਆਨ ਗੱਲਬਾਤ ਦੇ ਇਤਿਹਾਸ ਨੂੰ ਸਟੋਰ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ `chat_message_store_factory` ਨਾਲ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੀ ਜਾਂਦੀ ਹੈ:

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

*ਡਾਇਨਾਮਿਕ ਮੈਮੋਰੀ*

ਇਹ ਮੈਮੋਰੀ ਏਜੰਟਾਂ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਸੰਦਰਭ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ ਮੈਮੋਰੀਆਂ ਬਾਹਰੀ ਸੇਵਾਵਾਂ ਜਿਵੇਂ mem0 ਵਿੱਚ ਸਟੋਰ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ:

```python
from agent_framework.mem0 import Mem0Provider

# ਉੱਚ ਪੱਧਰੀ ਮੈਮੋਰੀ ਸਮਰੱਥਾਵਾਂ ਲਈ Mem0 ਦੀ ਵਰਤੋਂ ਕਰਨਾ
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

**ਏਜੰਟ ਨਿਗਰਾਨੀ**

ਨਿਗਰਾਨੀ ਭਰੋਸੇਯੋਗ ਅਤੇ ਰੱਖ-ਰਖਾਵ ਯੋਗ ਏਜੰਟਿਕ ਸਿਸਟਮ ਬਣਾਉਣ ਲਈ ਜਰੂਰੀ ਹੈ। MAF OpenTelemetry ਨਾਲ ਇੰਟਿਗਰੇਟ ਕਰਦਾ ਹੈ ਜੋ ਟ੍ਰੇਸਿੰਗ ਅਤੇ ਮੀਟਰਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਬਿਹਤਰ ਨਿਗਰਾਨੀ ਲਈ।

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

### ਵਰਕਫਲੋਜ਼

MAF ਵਰਕਫਲੋਜ਼ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਕਿਸੇ ਕੰਮ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਪਹਿਲਾਂ ਤੋਂ ਪਰਿਭਾਸ਼ਿਤ ਕਦਮ ਹਨ ਅਤੇ ਜਿਨ੍ਹਾਂ ਵਿੱਚ AI ਏਜੰਟ ਹਿੱਸੇ ਦੇ ਤੌਰ ਤੇ ਸ਼ਾਮਿਲ ਹੁੰਦੇ ਹਨ।

ਵਰਕਫਲੋਜ਼ ਵੱਖਰੇ ਹਿੱਸਿਆਂ ਨਾਲ ਬਣੇ ਹੁੰਦੇ ਹਨ ਜੋ ਬਿਹਤਰ ਨਿਯੰਤਰਣ ਪ੍ਰਵਾਹ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ। ਵਰਕਫਲੋਜ਼ **ਬਹੁ-ਏਜੰਟ ਅਰਕੈਸਟਰੈਸ਼ਨ** ਅਤੇ **ਚੈਕਪਵਾਇੰਟਿੰਗ** ਨੂੰ ਭੀ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ ਜੋ ਵਰਕਫਲੋ ਸਥਿਤੀਆਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਦਾ ਹੈ।

ਇੱਕ ਵਰਕਫਲੋ ਦੇ ਮੁੱਖ ਹਿੱਸੇ ਹਨ:

**ਏਗਜ਼ੈਕਿਊਟਰਸ**

ਏਗਜ਼ੈਕਿਊਟਰਸ ਇਨਪੁਟ ਸੁਨੇਹੇ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਨ, ਆਪਣੇ ਨਿਰਧਾਰਿਤ ਕੰਮ ਕਰਦੇ ਹਨ, ਅਤੇ ਫਿਰ ਐਕ আਉਟਪੁਟ ਸੁਨੇਹਾ ਪੈਦਾ ਕਰਦੇ ਹਨ। ਇਹ ਵਰਕਫਲੋ ਨੂੰ ਵੱਡੇ ਕੰਮ ਵੱਲ ਅੱਗੇ ਵਧਾਉਂਦਾ ਹੈ। ਏਗਜ਼ੈਕਿਊਟਰ ਕਿਸੇ ਵੀ AI ਏਜੰਟ ਜਾਂ ਕਸਟਮ ਲਾਜਿਕ ਹੋ ਸਕਦੇ ਹਨ।

**ਐਜ਼**

ਐਜ਼ ਵਰਕਫਲੋ ਵਿੱਚ ਸੁਨੇਹਿਆਂ ਦੇ ਪ੍ਰਵਾਹ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਇਹ ਹੋ ਸਕਦੇ ਹਨ:

*ਸਿੱਧੇ ਐਜ਼* - ਏਗਜ਼ੈਕਿਊਟਰਾਂ ਦਰਮਿਆਨ ਸਿੱਧੇ ਇਕ-ਤੋਂ-ਇੱਕ ਕਨੈਕਸ਼ਨ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*ਸ਼ਰਤੀ ਐਜ਼* - ਜਦੋਂ ਕੋਈ ਖਾਸ ਸ਼ਰਤ ਪੂਰੀ ਹੁੰਦੀ ਹੈ ਤਦ ਕਾਰਵਾਈ ਹੁੰਦੀ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜਦੋਂ ਹੋਟਲ ਦੇ ਕਮਰੇ ਉਪਲਬਧ ਨਹੀਂ ਹੁੰਦੇ, ਤਾਂ ਏਗਜ਼ੈਕਿਊਟਰ ਹੋਰ ਵਿਕਲਪ ਸੁਝਾ ਸਕਦਾ ਹੈ।

*ਸਵਿੱਚ-ਕੇਸ ਐਜ਼* - ਨਿਰਧਾਰਿਤ ਸ਼ਰਤਾਂ ਅਨੁਸਾਰ ਸੁਨੇਹਿਆਂ ਨੂੰ ਵੱਖਰੇ ਏਗਜ਼ੈਕਿਊਟਰਾਂ ਨੂੰ ਰੂਟ ਕਰਨਾ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਯਾਤਰਾ ਗ੍ਰਾਹਕ ਕੋਲ ਪ੍ਰਾਇਓਰਿਟੀ ਪਹੁੰਚ ਹੈ, ਤਾਂ ਉਸਦੇ ਕੰਮ ਇੱਕ ਹੋਰ ਵਰਕਫਲੋ ਰਾਹੀਂ ਸੰਭਾਲੇ ਜਾਣਗੇ।

*ਫੈਨ-ਆਉਟ ਐਜ਼* - ਇੱਕ ਸੁਨੇਹਾ ਕਈ ਲਕੜੀਾਂ ਜਾਂ ਲਕੜਾਂ ਤੱਕ ਭੇਜਣਾ।

*ਫੈਨ-ਇਨ ਐਜ਼* - ਵੱਖ-ਵੱਖ ਏਗਜ਼ੈਕਿਊਟਰਾਂ ਤੋਂ ਕਈ ਸੁਨੇਹਿਆਂ ਨੂੰ ਇਕੱਠਾ ਕਰਕੇ ਇੱਕ ਲਕੜੀ ਨੂੰ ਭੇਜਣਾ।

**ਘਟਨਾਵਾਂ**

ਵਰਕਫਲੋਜ਼ ਵਿੱਚ ਬਿਹਤਰ ਨਿਗਰਾਨੀ ਦੇ ਲਈ, MAF ਐਗਜ਼ੈਕਿਊਸ਼ਨ ਲਈ ਬਿਲਟ-ਇਨ ਘਟਨਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜਿਹਨਾਂ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹਨ:

- `WorkflowStartedEvent`  - ਵਰਕਫਲੋ ਚਾਲੂ ਹੋਣਾ
- `WorkflowOutputEvent` - ਵਰਕਫਲੋ ਆਉਟਪੁਟ ਪੈਦਾ ਕਰਦਾ ਹੈ
- `WorkflowErrorEvent` - ਵਰਕਫਲੋ ਵਿੱਚ ਗਲਤੀ ਆਉਂਦੀ ਹੈ
- `ExecutorInvokeEvent`  - ਏਗਜ਼ੈਕਿਊਟਰ ਕੰਮ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ
- `ExecutorCompleteEvent`  -  ਏਗਜ਼ੈਕਿਊਟਰ ਕੰਮ ਮੁਕੰਮਲ ਕਰਦਾ ਹੈ
- `RequestInfoEvent` - ਬੇਨਤੀ ਜਾਰੀ ਕੀਤੀ ਜਾਂਦੀ ਹੈ

## ਅਗੇਤੜ੍ਹ ਮਾਫ ਪੈਟਰਨ

ਉਪਰ ਲਿਖੇ ਹਿੱਸਿਆਂ ਵਿੱਚ ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀਆਂ ਮੁੱਖ ਧਾਰਵਾਂ ਨੂੰ ਕਵਰ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਿਵੇਂ ਜਦੋਂ ਤੁਸੀਂ ਹੋਰ ਜਟਿਲ ਏਜੰਟ ਬਣਾਉਂਦੇ ਹੋ, ਇੱਥੇ ਕੁਝ ਅਗੇਤੜ੍ਹ ਪੈਟਰਨ ਹਨ ਜਿਨ੍ਹਾਂ ਬਾਰੇ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ:

- **ਮਿਡਲਵੇਅਰ ਸੰਗਠਨ**: ਕਈ ਮਿਡਲਵੇਅਰ ਹੈਂਡਲਰਾਂ (ਲੋਗਿੰਗ, ਆਥ, ਰੇਟ-ਲਿਮਿਟਿੰਗ) ਨੂੰ ਫੰਕਸ਼ਨ ਅਤੇ ਚੈਟ ਮਿਡਲਵੇਅਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਏਜੰਟ ਦੇ ਵਿਹਾਰ 'ਤੇ ਬारीਕ ਨਿਯੰਤਰਣ ਲਈ ਲੜੀ ਵਿੱਚ ਜੋੜਨਾ।
- **ਵਰਕਫਲੋ ਚੈਕਪੌਇੰਟਿੰਗ**: ਵਰਕਫਲੋ ਘਟਨਾਵਾਂ ਅਤੇ ਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੰਬੀ ਚੱਲ ਰਹੀ ਏਜੰਟ ਪ੍ਰਕਿਰਿਆਵਾਂ ਨੂੰ ਸੇਵ ਅਤੇ ਮੁੜ ਚਾਲੂ ਕਰਨ ਲਈ।
- **ਡਾਇਨਾਮਿਕ ਟੂਲ ਚੋਣ**: MAF ਦੇ ਟੂਲ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਨਾਲ RAG ਨੂੰ ਜੋੜ ਕੇ ਪ੍ਰਤੀਕ੍ਰਮਯੋਗ ਟੂਲ ਹੀ ਦਿਖਾਉਣਾ।
- **ਬਹੁ-ਏਜੰਟ ਹੈਂਡਆਫ਼ਟ**: ਵਰਕਫਲੋ ਐਜ਼ ਅਤੇ ਸ਼ਰਤੀ ਰੁਟਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੁਹਾਰਤ ਵਾਲੇ ਏਜੰਟਾਂ ਦਰਮਿਆਨ ਹੈਂਡਆਫਟ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰਨਾ।

## Microsoft Foundry 'ਤੇ LangChain / LangGraph ਏਜੰਟਸ ਦੀ ਹੋਸਟਿੰਗ

ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ **ਫਰੇਮਵਰਕ-ਅੰਤਰਚਾਲੂ ਹੈ** — ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ **LangChain** ਜਾਂ **LangGraph** ਨਾਲ ਬਣਾਇਆ ਗਿਆ ਏਜੰਟ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਇਸਨੂੰ ਇੱਕ **Microsoft Foundry ਹੋਸਟਿਡ ਏਜੰਟ** ਵਜੋਂ ਚਲਾ ਸਕਦੇ ਹੋ, ਜਿਥੇ Foundry ਰਨਟਾਈਮ, ਸੈਸ਼ਨ, ਸਕੇਲਿੰਗ, ਪਹਚਾਣ ਅਤੇ ਪ੍ਰੋਟੋਕਾਲ ਐਂਡਪੋਇੰਟਾਂ ਦੀ ਸੰਭਾਲ ਕਰਦਾ ਹੈ, ਜਦ ਕਿ ਤੁਹਾਡੀ ਏਜੰਟ ਲਾਜਿਕ LangGraph ਵਿੱਚ ਰਹਿੰਦੀ ਹੈ।

ਇਹ `langchain_azure_ai.agents.hosting` ਪੈਕੇਜ ਨਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜੋ ਉਹਨਾਂ ਹੀ ਪ੍ਰੋਟੋਕਾਲਾਂ ਉੱਪਰ ਇੱਕ ਸੰਕਲਿਤ LangGraph ਗ੍ਰਾਫ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ Foundry ਹੋਸਟਿਡ ਏਜੰਟ ਵਰਤਦੇ ਹਨ।

**1. ਹੋਸਟਿੰਗ ਇਕਸਟਰਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ਇਕਸਟਰਾਂ Foundry ਪ੍ਰੋਟੋਕਾਲ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰਦਾ ਹੈ: `azure-ai-agentserver-responses` (OpenAI-ਅਨੁਕੂਲ `/responses` ਏਂਡਪੋਇੰਟ) ਅਤੇ `azure-ai-agentserver-invocations` (ਜਨਰਲ `/invocations` ਏਂਡਪੋਇੰਟ)।

**2. ਇੱਕ ਹੋਸਟਿੰਗ ਪ੍ਰੋਟੋਕਾਲ ਚੁਣੋ:**

| ਪ੍ਰੋਟੋਕਾਲ | ਹੋਸਟ ਕਲਾਸ | ਏਂਡਪੋਇੰਟ | ਕਦੋਂ ਵਰਤਣਾ |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | ਤੁਸੀਂ OpenAI-ਅਨੁਕੂਲ ਗੱਲਬਾਤ, ਸਟ੍ਰੀਮਿੰਗ, ਜਵਾਬ ਇਤਿਹਾਸ ਅਤੇ ਸੰਵਾਦ ਥ੍ਰੈਡਿੰਗ ਚਾਹੁੰਦੇ ਹੋ — ਗੱਲਬਾਤੀ ਏਜੰਟਾਂ ਲਈ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਡਿਫੌਲਟ। |
| **Invocations** | `InvocationsHostServer` | `/invocations` | ਤੁਹਾਨੂੰ ਇੱਕ ਕਸਟਮ JSON ਆਕਾਰ, ਵੈੱਬਹੁੱਕ-ਸਟਾਈਲ ਏਂਡਪੋਇੰਟ ਜਾਂ ਗੈਰ-ਗੱਲਬਾਤੀ ਪ੍ਰੋਸੈਸਿੰਗ ਚਾਹੀਦੀ ਹੈ। |

ਕਿਉਂਕਿ **Responses API Foundry ਵਿੱਚ ਏਜੰਟ-ਸ਼ੈਲੀ ਵਿਕਾਸ ਲਈ ਪ੍ਰਾਥਮਿਕ API ਹੈ**, ਜ਼ਿਆਦਾਤਰ ਏਜੰਟਾਂ ਲਈ `ResponsesHostServer` ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ।

**3. ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੰਰਚਿਤ ਕਰੋ** (`az login` ਪਹਿਲਾਂ ਕਰੋ ਤਾਂ ਜੋ `DefaultAzureCredential` ਪ੍ਰਮਾਣਿਕਤਾ ਕਰ ਸਕੇ):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ਜਦੋਂ ਏਜੰਟ ਬਾਅਦ ਵਿੱਚ Foundry ਵਿੱਚ ਇੱਕ ਹੋਸਟਿਡ ਏਜੰਟ ਵਜੋਂ ਚਲਦਾ ਹੈ, ਪਲੇਟਫਾਰਮ `FOUNDRY_PROJECT_ENDPOINT` ਨੂੰ ਆਪਣੇ ਆਪ ਇੰਜੈਕਟ ਕਰਦਾ ਹੈ।

**4. Responses ਪ੍ਰੋਟੋਕਾਲ ਉੱਪਰ ਇੱਕ LangGraph ਏਜੰਟ ਪ੍ਰਗਟ ਕਰੋ:**

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

    # ChatOpenAI ਇੱਥੇ Foundry ਪ੍ਰੋਜੈਕਟ ਦੇ OpenAI-ਕਮਪੈਟਿਬਲ (Responses) ਐਂਡਪੋਇੰਟ ਨੂੰ ਲਕੜੀ ਕਰਦਾ ਹੈ।
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

ਇਸਨੂੰ ਲੋਕਲ ਲੈਵਲ ’ਤੇ `python main.py` ਨਾਲ ਚਲਾਓ, ਫਿਰ `http://localhost:8088/responses` ਨੂੰ Responses ਬੇਨਤੀ ਭੇਜੋ।

**ਮੁੱਖ ਵਿਹਾਰ:**

- **ਸੰਵਾਦ**: ਕਲਾਇੰਟ ਇੱਕ ਸੰਵਾਦ ਨੂੰ `previous_response_id` ਜਾਂ `conversation` ID ਭੇਜ ਕੇ ਜਾਰੀ ਰੱਖਦੇ ਹਨ। ਜੇ ਤੁਹਾਡਾ ਗ੍ਰਾਫ LangGraph ਚੈਕਪੌਇੰਟਰ ਨਾਲ ਸੰਕਲਿਤ ਹੈ, ਤਾਂ Foundry ਸੰਵਾਦ ਸਥਿਤੀ ਨੂੰ ਚੈਕਪੌਇੰਟ ਨਾਲ ਜੋੜਦਾ ਹੈ (ਉਤਪਾਦਨ ਵਿੱਚ ਇੱਕ ਟਿਕਾਊ ਚੈਕਪੌਇੰਟਰ ਵਰਤੋਂ; ਸਥਾਨਕ ਟੈਸਟਿੰਗ ਲਈ `MemorySaver` ਠੀਕ ਹੈ)।
- **ਮਨੁੱਖ-ਵਿੱਚ-ਲੂਪ**: ਜੇ ਤੁਹਾਡਾ ਗ੍ਰਾਫ LangGraph `interrupt()` ਵਰਤਦਾ ਹੈ, `ResponsesHostServer` ਇਸ ਰੁਕਾਵਟ ਨੂੰ Responses `function_call` / `mcp_approval_request` ਆਈਟਮ ਵਜੋਂ ਦਰਸਾਉਂਦਾ ਹੈ, ਅਤੇ ਕਲਾਇੰਟ ਮੈਚਿੰਗ `function_call_output` / `mcp_approval_response` ਨਾਲ ਜਾਰੀ ਰੱਖਦੇ ਹਨ।
- **Foundry 'ਤੇ ਡਿਪਲੋਯ ਕਰੋ**: Azure Developer CLI ਨੂੰ ਵਰਤੋਂ — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ਲੋਕਲ, ਡੋਕਰ ਲੋੜੀਂਦਾ ਹੈ), ਫਿਰ `azd provision` ਅਤੇ `azd deploy`। ਹੋਸਟਿਡ ਏਜੰਟ ਡਿਪਲੋਯਮੈਂਟ ਲਈ **Foundry ਪ੍ਰੋਜੈਕਟ ਮੈਨੇਜਰ** ਰੋਲ ਲਾਜ਼ਮੀ ਹੈ।

ਇਸ ਉਦਾਹਰਨ ਦੀ ਚੱਲਣਯੋਗ ਵਰਜਨ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ਵਿੱਚ ਹੈ। ਪੂਰੇ ਵਾਕਥਰੂ ਲਈ (Invocations ਪ੍ਰੋਟੋਕਾਲ, ਕਸਟਮ ਬੇਨਤੀ ਸਕੀਮਾ ਅਤੇ ਸਮੱਸਿਆ ਸਹਿਯੋਗ), ਵੇਖੋ [Foundry ਹੋਸਟਿਡ ਏਜੰਟ ਵਜੋਂ LangGraph ਏਜੰਟ](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)।

## ਕੋਡ ਦੇ ਨਮੂਨੇ 

ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਲਈ ਕੋਡ ਦੇ ਨਮੂਨੇ ਇਸ ਰਿਪੋਜਟਰੀ ਵਿੱਚ `xx-python-agent-framework` ਅਤੇ `xx-dotnet-agent-framework` ਫਾਈਲਾਂ ਦੇ ਤਹਿਤ ਮਿਲਦੇ ਹਨ।

## ਮਾਇਕ੍ਰੋਸੋਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲਣ, ਦਫਤਰੀ ਘੰਟਿਆਂ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਣ ਅਤੇ ਆਪਣੀਆਂ AI ਏਜੰਟ ਸੰਬੰਧੀ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਵੋ।
## ਪਿਛਲਾ ਪਾਠ

[AI ਏਜੰਟ ਲਈ ਮੈਮੋਰੀ](../13-agent-memory/README.md)

## ਅਗਲਾ ਪਾਠ

[ਕੰਪਿਊਟਰ ਉਪਯੋਗ ਏਜੰਟ (CUA) ਬਣਾਉਣਾ](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->