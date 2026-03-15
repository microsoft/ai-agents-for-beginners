# ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਖੋਜ

![Agent Framework](../../../translated_images/pa/lesson-14-thumbnail.90df0065b9d234ee.webp)

### ਪਰਿਚਯ

ਇਹ ਪਾਠ ਵਿੱਚ ਕਵਰ ਕੀਤਾ ਜਾਵੇਗਾ:

- ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਨੂੰ ਸਮਝਣਾ: ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਮੁੱਲ  
- ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੁੱਖ ਸਿਧਾਂਤਾਂ ਦੀ ਖੋਜ
- ਉन्नਤ MAF ਪੈਟਰਨ: ਵਰਕਫਲੋਜ਼, ਮਿਡਲਵੇਅਰ, ਅਤੇ ਮੈਮੋਰੀ

## ਸਿੱਖਣ ਦੇ ਲੱਖ਼

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਜਾਣੋਗੇ ਕਿ ਕਿਵੇਂ:

- ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਡੱਕਸ਼ਨ ਰੇਡੀ AI ਏਜੰਟ ਬਣਾਉਣੇ  
- ਆਪਣੇ ਏਜੰਟਿਕ ਕੇਸਾਂ ਲਈ ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀਆਂ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਲਾਗੂ ਕਰਨੀਆਂ  
- ਵਰਕਫਲੋਜ਼, ਮਿਡਲਵੇਅਰ ਅਤੇ ਨਿਰੀਖਣ ਸਮੇਤ ਉन्नਤ ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਕਰਨੇ

## ਕੋਡ ਨਮੂਨੇ

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) ਲਈ ਕੋਡ ਨਮੂਨੇ ਇਸ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ `xx-python-agent-framework` ਅਤੇ `xx-dotnet-agent-framework` ਫਾਇਲਾਂ ਦੇ ਹੇਠਾਂ ਮਿਲ ਸਕਦੇ ਹਨ।

## ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਨੂੰ ਸਮਝਣਾ

![Framework Intro](../../../translated_images/pa/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) ਮਾਈਕ੍ਰੋਸਾਫਟ ਦਾ ਇੱਕ ਇਕਸਾਰ ਫਰੇਮਵਰਕ ਹੈ ਜੋ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਹੈ। ਇਹ ਲਚਕੀਲਾਪਨ ਦਿੰਦਾ ਹੈ ਜੋ ਪ੍ਰੋਡਕਸ਼ਨ ਅਤੇ ਰਿਸਰਚ ਮਾਹੌਲਾਂ ਵਿੱਚ ਵੇਖੇ ਜਾਂਦੇ ਵੱਖ-ਵੱਖ ਏਜੰਟਿਕ ਕੇਸਾਂ ਨੂੰ ਸੰਬੋਧਨ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ:

- **ਕ੍ਰਮਬੱਧ ਏਜੰਟ ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ** ਜਿਥੇ ਕਦਮ-ਬਦ-ਕਦਮ ਵਰਕਫਲੋਜ਼ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।  
- **ਸਮਕਾਲੀ ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ** ਜਿਥੇ ਏਜੰਟ ਇੱਕੋ ਸਮੇਂ ਕੰਮ ਪੂਰਾ ਕਰਦੇ ਹਨ।  
- **ਗਰੁੱਪ ਚੈਟ ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ** ਜਿਥੇ ਏਜੰਟ ਇੱਕ ਕੰਮ 'ਤੇ ਮਿਲ ਕੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹਨ।  
- **ਹੈਂਡਆਫ਼ ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ** ਜਿਥੇ ਏਜੰਟਾਂ ਨੇ ਜਦੋਂ ਸਬ-ਟਾਸਕ ਪੂਰੇ ਕਰ ਲਏ ਤਾਂ ਕੰਮ ਇਕ ਦੂਜੇ ਨੂੰ ਸੌਂਪਦੇ ਹਨ।  
- **ਮੈਗਨੀਟਿਕ ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ** ਜਿਥੇ ਪ੍ਰਬੰਧਕ ਏਜੰਟ ਇੱਕ ਕੰਮ ਸੂਚੀ ਬਨਾਉਂਦਾ ਅਤੇ ਸੋਧਦਾ ਹੈ ਅਤੇ ਸਬਏਜੰਟਾਂ ਦੀ ਕੋਆਰਡੀਨੇਸ਼ਨ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਕੰਮ ਪੂਰਾ ਹੋ ਸਕੇ।

ਪ੍ਰੋਡਕਸ਼ਨ ਵਿੱਚ AI ਏਜੰਟ ਸਪਲੀ ਕਰਨ ਲਈ, MAF ਇਸ ਚੀਜ਼ਾਂ ਦੀ ਵੀ ਪੇਸ਼ਕਸ਼ ਕਰਦਾ ਹੈ:

- **ਨਿਰੀਖਣਯੋਗਤਾ** ਓਪਨਟੈਲੀਮੇਟਰੀ ਦੀ ਵਰਤੋਂ ਰਾਹੀਂ ਜਿਥੇ AI ਏਜੰਟ ਦੀ ਹਰ ਕਾਰਵਾਈ, ਟੂਲ ਕਾਲ, ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ ਕਦਮ, ਤੱਰਕ ਧਾਰਾਵਾਂ ਅਤੇ Microsoft Foundry ਡੈਸ਼ਬੋਰਡਸ ਰਾਹੀਂ ਪ੍ਰਦਰਸ਼ਨ ਦੀ ਮਾਨੀਟਰਿੰਗ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।  
- **ਸੁਰੱਖਿਆ** ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਊਂਡਰੀ 'ਤੇ ਸਰਵਰ ਹੋਸਟ ਕਰਦੇ ਹੋਏ, ਜੋ ਕਿ ਭੂਮਿਕਾ ਅਧਾਰਿਤ ਪਹੁੰਚ, ਨਿੱਜੀ ਡਾਟਾ ਹੈਂਡਲਿੰਗ ਅਤੇ ਬਿਲਟ-ਇਨ ਸਮੱਗਰੀ ਸੁਰੱਖਿਆ ਵਰਗੇ ਸੁਰੱਖਿਆ ਕੰਟਰੋਲ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ।  
- **ਟਿਕਾਊਪਨ** ਕਿਉਂਕਿ ਏਜੰਟ ਦੇ ਥਰੇਡ ਅਤੇ ਵਰਕਫਲੋਜ਼ ਨੂੰ ਰੋਕਿਆ, ਮੁੜ ਚਾਲੂ ਕੀਤਾ ਅਤੇ ਗਲਤੀਆਂ ਤੋਂ ਬਹਾਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਲੰਮੇ ਸਮੇਂ ਦੇ ਪ੍ਰਕਿਰਿਆ ਚੱਲ ਸਕਦੀ ਹੈ।  
- **ਕੰਟਰੋਲ** ਕਿਉਂਕਿ ਮਨੁੱਖੀ ਹਸਤȧੲਗੀ ਵਾਲੇ ਵਰਕਫਲੋਜ਼ ਦਾ ਸਮਰਥਨ ਹੈ, ਜਿਥੇ ਕੰਮਾਂ ਨੂੰ ਮਨੁੱਖੀ ਮੰਜੂਰੀ ਦੀ ਲੋੜ ਵਜੋਂ ਚਿਨ੍ਹਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦਾ ਇੱਕ ਹੋਰ ਧਿਆਨ ਇਨ੍ਹਾਂ ਚੀਜ਼ਾਂ 'ਤੇ ਹੈ:

- **ਕਲਾਉਡ-ਅਗਨੋਸਟਿਕ ਹੋਣਾ** - ਏਜੰਟ ਕੰਟੇਨਰ ਵਿੱਚ, ਓਨ-ਪ੍ਰੈਮ ਅਤੇ ਵੱਖ-ਵੱਖ ਕਲਾਉਡਸ ਵਿੱਚ ਚੱਲ ਸਕਦੇ ਹਨ।  
- **ਪ੍ਰੋਵਾਇਡਰ-ਅਗਨੋਸਟਿਕ ਹੋਣਾ** - ਇਹ ਤੁਹਾਡੇ ਪਸੰਦੀਦਾ SDK ਜਿਵੇਂ ਕਿ ਅਜ਼ੂਰ OpenAI ਅਤੇ OpenAI ਰਾਹੀਂ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ।  
- **ਖੁੱਲੇ ਮਿਆਰ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨਾ** - ਜਿਵੇਂ ਕਿ Agent-to-Agent (A2A) ਅਤੇ Model Context Protocol (MCP) ਵਰਗੇ ਪ੍ਰੋਟੋਕਾਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਰ ਏਜੰਟਾਂ ਅਤੇ ਟੂਲਾਂ ਨੂੰ ਖੋਜਣ ਅਤੇ ਵਰਤਣ ਵਾਲਾ।  
- **ਪਲੱਗਇਨ ਅਤੇ ਕਨੈਕਟਰਜ਼** - ਮਾਈਕ੍ਰੋਸਾਫਟ ਫੈਬਰਿਕ, ਸ਼ੇਅਰਪੋਇੰਟ, ਪਾਈਨਕੋਨ ਅਤੇ ਕ੍ਯੂਡਰਾਂਟ ਵਰਗੇ ਡਾਟਾ ਅਤੇ ਮੈਮੋਰੀ ਸੇਵਾਵਾਂ ਨਾਲ ਕਨੈਕਸ਼ਨ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ।

ਚਲੋ ਵੇਖੀਏ ਕਿ ਇਹ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਕੁਝ ਮੁੱਖ ਸਿਧਾਂਤਾਂ ਵਿੱਚ ਕਿਵੇਂ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ।

## ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੁੱਖ ਸਿਧਾਂਤ

### ਏਜੰਟ

![Agent Framework](../../../translated_images/pa/agent-components.410a06daf87b4fef.webp)

**ਏਜੰਟ ਬਣਾਉਣਾ**

ਏਜੰਟ ਬਣਾਉਣਾ ਇਨਫਰੈਂਸ ਸਰਵਿਸ (LLM ਪ੍ਰਦਾਤਾ) ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਕੇ, AI ਏਜੰਟ ਲਈ ਹਿਦਾਇਤਾਂ ਦੇ ਸੈੱਟ ਨਾਲ, ਅਤੇ ਨਿਰਧਾਰਿਤ `name` ਨਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```
  
ਉੱਪਰ `Azure OpenAI` ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਗਈ ਹੈ ਪਰ ਏਜੰਟ `Microsoft Foundry Agent Service` ਸਮੇਤ ਕਈ ਸਰਵਿਸਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵੀ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```
  
OpenAI ਦੇ `Responses`, `ChatCompletion` ਏਪੀਆਈਜ਼

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```
  
```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```
  
ਜਾਂ A2A ਪ੍ਰੋਟੋਕਾਲ ਵਰਗੇ ਰਿਮੋਟ ਏਜੰਟਾਂ ਦੀ ਵਰਤੋਂ:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```
  
**ਏਜੰਟ ਚਲਾਉਣਾ**

ਏਜੰਟ `.run` ਜਾਂ `.run_stream` ਦੇ ਤਰੀਕੇ ਨਾਲ ਚਲਾਏ ਜਾਂਦੇ ਹਨ, ਜੋ ਕਿ ਗੈਰ-ਸਟ੍ਰੀਮਿੰਗ ਜਾਂ ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬਾਂ ਲਈ ਹੁੰਦੇ ਹਨ।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```
  
```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```
  
ਹਰ ਏਜੰਟ ਚਲਾਣ ਵਿੱਚ ਕੁਝ ਵਿਕਲਪ ਵੀ ਹੋ ਸਕਦੇ ਹਨ ਜਿਵੇਂ ਕਿ `max_tokens` ਜੋ ਏਜੰਟ ਦੁਆਰਾ ਵਰਤੇ ਜਾਂਦੇ ਹਨ, `tools` ਜੋ ਏਜੰਟ ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ, ਅਤੇ ਇੱਥੋਂ ਤੱਕ ਕਿ ਖੁਦ `model` ਜਿਹੜਾ ਏਜੰਟ ਲਈ ਵਰਤਿਆ ਜਾ ਰਿਹਾ ਹੈ।  

ਇਹ ਉਪਯੋਗੀ ਹੁੰਦਾ ਹੈ ਜਦੋਂ ਕਿਸੇ ਯੂਜ਼ਰ ਦੇ ਕੰਮ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਖਾਸ ਮਾਡਲ ਜਾਂ ਟੂਲਾਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

**ਟੂਲ**

ਟੂਲ ਦੋਨੋਂ ਸਮੇਂ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ: ਏਜੰਟ ਬਣਾਉਂਦੇ ਸਮੇਂ:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ਜਦੋਂ ਸਿੱਧਾ ਇੱਕ ChatAgent ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੋਵੇ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```
  
ਅਤੇ ਇਹ ਫਿਰ ਏਜੰਟ ਚਲਾਉਂਦੇ ਸਮੇਂ:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ਸਿਰਫ ਇਸ ਦੌੜ ਲਈ ਉਪਲਬਧ ਸੰਦ )
```
  
**ਏਜੰਟ ਥਰੇਡ**

ਏਜੰਟ ਥਰੇਡ ਬਹੁ-ਚਰਚਾ ਗੱਲਬਾਤ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਥਰੇਡ ਬਣਾਉਣ ਦੇ ਤਰੀਕੇ ਹਨ:

- `get_new_thread()` ਵਰਤ ਕੇ ਜੋ ਥਰੇਡ ਨੂੰ ਸਮੇਂ ਨਾਲ ਸਟੋਰ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ  
- ਇੱਕ ਥਰੇਡ ਆਟੋਮੈਟਿਕ ਬਣਾਉਣਾ ਜਦੋਂ ਏਜੰਟ ਚਲਾਇਆ ਜਾ ਰਿਹਾ ਹੋਵੇ ਅਤੇ ਇਹ ਥਰੇਡ ਸਿਰਫ਼ ਮੌਜੂਦਾ ਧੌੜ ਦੌਰਾਨ ਚਲੇ

ਥਰੇਡ ਬਣਾਉਣ ਲਈ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਦਾ ਹੈ:

```python
# ਇੱਕ ਨਵੀਂ ਥ੍ਰੇਡ ਬਣਾਓ।
thread = agent.get_new_thread() # ਥ੍ਰੇਡ ਨਾਲ ਏਜੰਟ ਨੂੰ ਚਲਾਓ।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```
  
ਫਿਰ ਤੁਸੀਂ ਥਰੇਡ ਨੂੰ ਸਿਰੀਅਲਾਈਜ਼ ਕਰਕੇ ਬਾਅਦ ਵਿੱਚ ਵਰਤਣ ਲਈ ਸਟੋਰ ਕਰ ਸਕਦੇ ਹੋ:

```python
# ਇੱਕ ਨਵੀਂ ਥਰੇਡ ਬਣਾਓ।
thread = agent.get_new_thread() 

# ਥਰੇਡ ਨਾਲ ਏਜੰਟ ਚਲਾਓ।

response = await agent.run("Hello, how are you?", thread=thread) 

# ਸਟੋਰੇਜ ਲਈ ਥਰੇਡ ਨੂੰ ਸੀਰੀਅਲਾਈਜ਼ ਕਰੋ।

serialized_thread = await thread.serialize() 

# ਸਟੋਰੇਜ ਤੋਂ ਲੋਡ ਕਰਨ ਮਗਰੋਂ ਥਰੇਡ ਦੀ ਸਥਿਤੀ ਨੂੰ ਡੀਸੀਰੀਅਲਾਈਜ਼ ਕਰੋ।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```
  
**ਏਜੰਟ ਮਿਡਲਵੇਅਰ**

ਏਜੰਟ ਟੂਲ ਅਤੇ LLMs ਨਾਲ ਮੁਲਾਕਾਤ ਕਰਦੇ ਹਨ ਤਾਂ ਜੋ ਯੂਜ਼ਰ ਦੇ ਕੰਮ ਪੂਰੇ ਹੋ ਸਕਣ। ਕੁਝ ਸਥਿਤੀਆਂ ਵਿੱਚ, ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ਇਹ ਇੰਟਰੈਕਸ਼ਨਾਂ ਵਿਚਕਾਰ ਕੁਝ ਕਾਰਵਾਈ ਜਾਂ ਟ੍ਰੈਕਿੰਗ ਕੀਤੀ ਜਾਵੇ। ਏਜੰਟ ਮਿਡਲਵੇਅਰ ਸਾਨੂੰ ਇਹ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ:

*ਫੰਕਸ਼ਨ ਮਿਡਲਵੇਅਰ*

ਇਹ ਮਿਡਲਵੇਅਰ ਸਾਨੂੰ ਏਜੰਟ ਅਤੇ ਫੰਕਸ਼ਨ/ਟੂਲ ਵਿੱਚ ਕਾਲ ਕਰਨ ਵਾਲੀ ਕਾਰਵਾਈ ਦੇ ਵਿਚਕਾਰ ਕੁਝ ਇਕਸ਼ਨ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਜਦੋਂ ਤੁਸੀਂ ਫੰਕਸ਼ਨ ਕਾਲ ਤੇ ਕੁਝ ਲਾਗਿੰਗ ਕਰਨੀ ਹੋਵੇ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ `next` ਇਹ ਤਾਂ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਅੱਗਲਾ ਮਿਡਲਵੇਅਰ ਜਾਂ ਅਸਲ ਫੰਕਸ਼ਨ ਕਾਲ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਜਾਂ ਨਹੀਂ।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ਪ੍ਰੀ-ਪ੍ਰੋਸੈਸਿੰਗ: ਫਂਕਸ਼ਨ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਲੌਗ ਕਰੋ
    print(f"[Function] Calling {context.function.name}")

    # ਅਗਲੇ ਮਿਡਲਵੇਅਰ ਜਾਂ ਫਂਕਸ਼ਨ ਚਲਾਉਣ ਵੱਲ ਜਾਰੀ ਰੱਖੋ
    await next(context)

    # ਪੋਸਟ-ਪ੍ਰੋਸੈਸਿੰਗ: ਫਂਕਸ਼ਨ ਚਲਾਉਣ ਤੋਂ ਬਾਅਦ ਲੌਗ ਕਰੋ
    print(f"[Function] {context.function.name} completed")
```
  
*ਚੈਟ ਮਿਡਲਵੇਅਰ*

ਇਸ ਮਿਡਲਵੇਅਰ ਨਾਲ ਅਸੀਂ ਏਜੰਟ ਅਤੇ LLM ਵਿਚਕਾਰ ਦੀਆਂ ਬੇਨਤੀਆਂ ਵਿੱਚ ਕਾਰਵਾਈ ਜਾਂ ਲਾਗ ਕਰ ਸਕਦੇ ਹਾਂ।

ਇਸ ਵਿੱਚ ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਹੁੰਦੀ ਹੈ ਜਿਵੇਂ ਕਿ AI ਸਰਵਿਸ ਵੱਲ ਭੇਜੇ ਜਾ ਰਿਹਾ `messages`।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ਪ੍ਰੀ-ਪ੍ਰੋਸੈਸਿੰਗ: ਏ.ਆਈ. ਕਾਲ ਤੋਂ ਪਹਿਲਾਂ ਲੌਗ ਕਰੋ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ਅਗਲੇ ਮਿਡਲਵੇਅਰ ਜਾਂ ਏ.ਆਈ. ਸੇਵਾ ਤੇ ਜਾਰੀ ਰੱਖੋ
    await next(context)

    # ਪੋਸਟ-ਪ੍ਰੋਸੈਸਿੰਗ: ਏ.ਆਈ. ਜਵਾਬ ਦੇ ਬਾਅਦ ਲੌਗ ਕਰੋ
    print("[Chat] AI response received")

```
  
**ਏਜੰਟ ਮੈਮੋਰੀ**

`Agentic Memory` ਪਾਠ ਵਿੱਚ ਕਵਰੇਜ ਦੇ ਤੌਰ 'ਤੇ, ਮੈਮੋਰੀ ਇੱਕ ਅਹੰਕਾਰਪੂਰਕ ਅੰਗ ਹੈ ਜੋ ਏਜੰਟ ਨੂੰ ਵੱਖ-ਵੱਖ ਸੰਦਰਭਾਂ ਵਿੱਚ ਕੰਮ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ। MAF ਕਈ ਕਿਸਮਾਂ ਦੀਆਂ ਯਾਦਾਂ ਪੇਸ਼ ਕਰਦਾ ਹੈ:

*ਇਨ-ਮੈਮੋਰੀ ਸਟੋਰੇਜ*

ਇਹ ਮੈਮੋਰੀ ਐਪਲੀਕੇਸ਼ਨ ਰਨਟਾਈਮ ਦੌਰਾਨ ਥਰੇਡਾਂ ਵਿੱਚ ਸਟੋਰੇਜ ਹੁੰਦੀ ਹੈ।

```python
# ਇੱਕ ਨਵੀਂ ਧਾਗਾ ਬਣਾਓ।
thread = agent.get_new_thread() # ਧਾਗੇ ਨਾਲ ਏਜੰਟ ਨੂੰ ਚਲਾਓ।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```
  
*ਪੈਕਾਕਾਈ ਸੰਦੇਸ਼*

ਇਹ ਯਾਦ ਉਸ ਸਮੇਂ ਵਰਤੀ ਜਾਂਦੀ ਹੈ ਜਦੋਂ ਵੱਖ-ਵੱਖ ਸੈਸ਼ਨਾਂ ਵਿੱਚ ਗੱਲਬਾਤ ਦਾ ਇਤਿਹਾਸ ਸੰਭਾਲਣਾ ਹੋਵੇ। ਇਹ ਨੂੰ `chat_message_store_factory` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:

```python
from agent_framework import ChatMessageStore

# ਇਕ ਕਸਟਮ ਸੁਨੇਹਾ ਸਟੋਰ ਬਣਾਓ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```
  
*ਡਾਇਨਾਮਿਕ ਮੈਮੋਰੀ*

ਇਹ ਮੈਮੋਰੀ ਏਜੰਟ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਸੰਦਰਭ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ ਯਾਦਾਂ ਬਾਹਰੀ ਸੇਵਾਵਾਂ ਜਿਵੇਂ mem0 ਵਿੱਚ ਭੀ ਸਟੋਰ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ:

```python
from agent_framework.mem0 import Mem0Provider

# ਉन्नਤ ਮੈਮੋਰੀ ਸਮਰੱਥਾਵਾਂ ਲਈ Mem0 ਦੀ ਵਰਤੋਂ ਕਰਨਾ
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
  
**ਏਜੰਟ ਨਿਰੀਖਣਯੋਗਤਾ**

ਨਿਰੀਖਣਯੋਗਤਾ ਭਰੋਸੇਮੰਦ ਅਤੇ ਬਰਕਰਾਰ ਰੱਖਣਯੋਗ ਏਜੰਟਿਕ ਪ੍ਰਣਾਲੀਆਂ ਬਣਾਉਣ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ। MAF ਨਿਰੀਖਣ ਲਈ OpenTelemetry ਨਾਲ ਇੰਟਿਗ੍ਰੇਟ ਹੋ ਕੇ ਟ੍ਰੇਸਿੰਗ ਅਤੇ ਮੀਟਰ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ।

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

MAF ਐਸੇ ਵਰਕਫਲੋਜ਼ ਪੇਸ਼ ਕਰਦਾ ਹੈ ਜੋ ਪਹਿਲਾਂ ਤੋਂ ਨਿਰਧਾਰਿਤ ਕਦਮ ਹੁੰਦੇ ਹਨ ਕੰਮ ਪੂਰਾ ਕਰਨ ਲਈ ਅਤੇ ਜਿਨ੍ਹਾਂ ਵਿੱਚ AI ਏਜੰਟ ਕਿਊੰਪੋਨੈਂਟ ਵਜੋਂ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ।

ਵਰਕਫਲੋਜ਼ ਵੱਖ-ਵੱਖ ਤੱਤਾਂ ਤੋਂ ਬਣੇ ਹੁੰਦੇ ਹਨ ਜੋ ਚੰਗੀ ਕੰਟਰੋਲ ਫਲੋ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ। ਵਰਕਫਲੋਜ਼ **ਮਲਟੀ-ਏਜੰਟ ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ** ਅਤੇ ਵਰਕਫਲੋ ਸਥਿਤੀ ਸੁਰੱਖਿਆ ਲਈ **ਚੈਕਪੋਇੰਟਿੰਗ** ਵੀ ਸਮਰਥਨ ਕਰਦੇ ਹਨ।

ਵਰਕਫਲੋਜ਼ ਦੇ ਮੁੱਖ ਤੱਤ ਹਨ:

**ਐਕਜ਼ੈਕਿਊਟਰ**

ਐਕਜ਼ੈਕਿਊਟਰ ਇਨਪੁੱਟ ਮੇਸੇਜ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਨ, ਆਪਣੇ ਸੌਂਪੇ ਕੰਮ ਕਰਦੇ ਹਨ, ਅਤੇ ਫਿਰ ਇੱਕ ਔਟਪੁੱਟ ਮੇਸੇਜ ਤੈਯਾਰ ਕਰਦੇ ਹਨ। ਇਹ ਵਰਕਫਲੋ ਨੂੰ ਵੱਡੇ ਕੰਮ ਦੀ ਪੂਰੀ ਕਰਨ ਦੀ ਯਾਤਰਾ 'ਤੇ ਅੱਗੇ ਵਧਾਉਂਦਾ ਹੈ। ਐਕਜ਼ੈਕਿਊਟਰ AI ਏਜੰਟ ਜਾਂ ਕਸਟਮ ਲੌਜਿਕ ਹੋ ਸਕਦਾ ਹੈ।

**ਐਜ**

ਐਜ ਵਰਕਫਲੋ ਵਿੱਚ ਮੇਸੇਜ ਦੇ ਪ੍ਰਵਾਹ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਇਹ ਹੋ ਸਕਦੇ ਹਨ:

*ਸਿੱਧੇ ਐਜ* - ਐਕਜ਼ੈਕਿਊਟਰਜ਼ ਵਿਚਕਾਰ ਸਿੱਧਾ ਇੱਕ-ਦੂਜੇ ਨਾਲ ਜੁੜਾਅ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```
  
*ਸ਼ਰਤਿਤ ਐਜ* - ਜਦੋਂ ਇੱਕ ਨਸ਼ਚਿਤ ਸ਼ਰਤ ਪੂਰੀ ਹੋ ਜਾਵੇ ਤਾਂ ਐਕਟਿਵ ਹੋਣ ਵਾਲੇ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜਦੋਂ ਹੋਟਲ ਦੇ ਕਮਰੇ ਉਪਲਬਧ ਨਾ ਹੋਣ, ਤਾਂ ਇੱਕ ਐਕਜ਼ੈਕਿਊਟਰ ਹੋਰ ਵਿਕਲਪ ਪੇਸ਼ ਕਰ ਸਕਦਾ ਹੈ।

*ਸਵਿੱਚ-ਕੇਸ ਐਜ* - ਨਿਰਧਾਰਿਤ ਸ਼ਰਤਾਂ ਅਨੁਸਾਰ ਮੇਸੇਜ ਨੂੰ ਵੱਖ-ਵੱਖ ਐਕਜ਼ੈਕਿਊਟਰਜ਼ ਵੱਲ ਭੇਜਣ। ਜਿਵੇਂ ਕਿ ਯਾਤਰਾ ਗਾਹਕ ਨੂੰ ਪਹਿਲਾਂ ਪਹੁੰਚ ਮਿਲਦੀ ਹੈ ਤੇ ਉਹਨਾਂ ਦੇ ਕੰਮ ਹੋਰ ਵਰਕਫਲੋ ਰਾਹੀਂ ਕਿਯੇ ਜਾਣਗੇ।

*ਫੈਨ-ਆਉਟ ਐਜ* - ਇਕ ਮੇਸੇਜ ਕਈ ਟਾਰਗੇਟਾਂ ਨੂੰ ਭੇਜਣਾ।

*ਫੈਨ-ਇਨ ਐਜ* - ਕਈ ਐਕਜ਼ੈਕਿਊਟਰਜ਼ ਦੇ ਵੱਖ-ਵੱਖ ਮੇਸੇਜ ਇਕੱਠੇ ਕਰਕੇ ਇੱਕ ਟਾਰਗੇਟ ਨੂੰ ਭੇਜਣਾ।

**ਈਵੈਂਟ**

ਵਰਕਫਲੋਜ਼ ਵਿੱਚ ਵਧੀਆ ਨਿਰੀਖਣ ਲਈ, MAF ਐਕਜ਼ੈਕਿਊਸ਼ਨ ਲਈ ਬਿਲਟ-ਇਨ ਈਵੈਂਟ ਪੇਸ਼ ਕਰਦਾ ਹੈ ਜਿਵੇਂ:

- `WorkflowStartedEvent` - ਵਰਕਫਲੋ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ  
- `WorkflowOutputEvent` - ਵਰਕਫਲੋ ਇੱਕ ਅਉਟਪੁੱਟ ਪੈਦਾ ਕਰਦਾ ਹੈ  
- `WorkflowErrorEvent` - ਵਰਕਫਲੋ ਵਿੱਚ ਗਲਤੀ ਆਉਂਦੀ ਹੈ  
- `ExecutorInvokeEvent` - ਐਕਜ਼ੈਕਿਊਟਰ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ  
- `ExecutorCompleteEvent` - ਐਕਜ਼ੈਕਿਊਟਰ ਪ੍ਰਕਿਰਿਆ ਸਮਾਪਤ ਕਰਦਾ ਹੈ  
- `RequestInfoEvent` - ਇਕ ਬੇਨਤੀ ਜਾਰੀ ਕੀਤੀ ਜਾਂਦੀ ਹੈ

## ਉਦਕ੍ਰਮਿਕ MAF ਪੈਟਰਨ

ਉਪਰੋਕਤ ਸੈਕਸ਼ਨ ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੁੱਖ ਸਿਧਾਂਤਾਂ ਨੂੰ ਕਵਰ ਕਰਦੇ ਹਨ। ਜਦੋਂ ਤੁਸੀਂ ਹੋਰ ਜਟਿਲ ਏਜੰਟਾਂ ਬਣਾਉਂਦੇ ਹੋ, ਤਾਂ ਇੱਥੇ ਕੁਝ ਉੱਨਤ ਪੈਟਰਨ ਹਨ ਜੋ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣ ਯੋਗ ਹਨ:

- **ਮਿਡਲਵੇਅਰ ਕੰਪੋਜ਼ੀਸ਼ਨ**: ਬਹੁ ਮਿਡਲਵੇਅਰ ਹੈਂਡਲਰਜ਼ (ਲਾਗਿੰਗ, ਆਥ, ਰੇਟ-ਲਿਮਿਟਿੰਗ) ਨੂੰ ਫੰਕਸ਼ਨ ਅਤੇ ਚੈਟ ਮਿਡਲਵੇਅਰ ਰਾਹੀਂ ਜੁੜੇ ਜਾ ਸਕਦੇ ਹਨ, ਜੋ ਏਜੰਟ ਦੇ ਵਿਹਾਰ 'ਤੇ ਤਿੱਨਤਲੀ ਕੰਟਰੋਲ ਦਿੰਦੇ ਹਨ।  
- **ਵਰਕਫਲੋ ਚੈਕਪੋਇੰਟਿੰਗ**: ਵਰਕਫਲੋ ਈਵੈਂਟਸ ਅਤੇ ਸਿਰੀਅਲਾਈਜ਼ੇਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੰਬੇ ਸਮੇਂ ਚੱਲ ਰਹੇ ਏਜੰਟ ਪ੍ਰਕਿਰਿਆਵਾਂ ਨੂੰ ਸੇਵ ਅਤੇ ਮੁੜ ਚਾਲੂ ਕਰੋ।  
- **ਡਾਇਨਾਮਿਕ ਟੂਲ ਸਿਲੈਕਸ਼ਨ**: RAG ਨੂੰ ਟੂਲ ਵੇਰਵੇਂ ਨਾਲ ਜੋੜ ਕੇ MAF ਦੇ ਟੂਲ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਦੇ ਨਾਲ ਕੇਵਲ ਲੋੜੀਂਦੇ ਟੂਲ ਨੂੰ ਹੀ ਪ੍ਰਸਤੁਤ ਕਰੋ।  
- **ਮਲਟੀ-ਏਜੰਟ ਹੈਂਡਆਫ਼**: ਵਰਕਫਲੋ ਐਜ ਅਤੇ ਸ਼ਰਤਾਂ ਵੱਲੋਂ ਰੂਟਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਿਸ਼ੇਸ਼ ਏਜੰਟਾਂ ਵਿਚਕਾਰ ਹੈਂਡਆਫ਼ ਦਾ ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ ਕਰੋ।

## ਕੋਡ ਨਮੂਨੇ

ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਲਈ ਕੋਡ ਨਮੂਨੇ ਇਸ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ `xx-python-agent-framework` ਅਤੇ `xx-dotnet-agent-framework` ਫਾਇਲਾਂ ਦੇ ਹੇਠਾਂ ਮਿਲ ਸਕਦੇ ਹਨ।

## ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲਣ, ਆਫ਼ਿਸ ਘੰਟੇ ਵਿੱਚ ਹਾਜ਼ਰੀ ਲੱਗਾਉਣ ਅਤੇ ਆਪਣੇ AI ਏਜੰਟ ਸਬੰਧੀ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲੈਣ ਲਈ [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ਨਾਲ ਜੁੜੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਡਿਸਕਲੇਮਰ**:  
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [ਕੋ-ਆਪ ਟ੍ਰਾਂਸਲੇਟਰ](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਸਮਝਾਵਟ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->