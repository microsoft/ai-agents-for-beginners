# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ ಅನ್ವೇಷಣೆ

![Agent Framework](../../../translated_images/kn/lesson-14-thumbnail.90df0065b9d234ee.webp)

### ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ಆವರಿಸಿಕೊಂಡಿರುವುದು:

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು: ಮುಖ್ಯ ಲಕ್ಷಣಗಳು ಮತ್ತು ಮೌಲ್ಯ  
- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ ಪ್ರಮುಖ ಕಾಲ್ಪನಿಕತೆಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು
- ಉನ್ನತ MAF ಮಾದರಿಗಳು: ಕಾರ್ಯಪ್ರವಾಹಗಳು, ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್, ಮತ್ತು ಮೆಮೊರಿ

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ಮೇಲೆ, ನಿಮಗೆ ತಿಳಿಯುವುದು ಹೇಗೆಂದು:

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಬಳಸಿ ಉತ್ಪಾದನೆಗೆ ಸಿದ್ಧವಾದ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು
- ನಿಮ್ಮ ಏಜೆಂಟಿಕ್ ಉಪಯೋಗ ಪ್ರಕರಣಗಳಿಗೆ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ ಮೂಲ ಲಕ್ಷಣಗಳನ್ನು ಅನ್ವಯಿಸುವುದು
- ಕಾರ್ಯಪ್ರವಾಹಗಳು, ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್ ಮತ್ತು ವಿಷ್ಲೇಷಣಾ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒಳಗೊಂಡ ಉನ್ನತ ಮಾದರಿಗಳನ್ನು ಬಳಸು

## ಕೋಡ್ ಮಾದರಿಗಳು 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ಗಾಗಿ ಕೋಡ್ ಮಾದರಿಗಳನ್ನು ಈ ರೆಪೋಸಿಟರಿಯಲ್ಲಿ `xx-python-agent-framework` ಮತ್ತು `xx-dotnet-agent-framework` ಫೈಲ್‌ಗಳಲ್ಲಿ ಕಂಡುಹಿಡಿಯಬಹುದು.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು

![Framework Intro](../../../translated_images/kn/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ಮೈಕ್ರೋಸಾಫ್ಟ್‌ನ ಏಐ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಒಕ್ಕೂಟಿತ ಫ್ರೇಮ್‌ವರ್ಕ್ ಆಗಿದೆ. ಇದು ಉತ್ಪಾದನೆ ಮತ್ತು ಸಂಶೋಧನಾ ಪರಿಸರಗಳಲ್ಲಿ ಕಂಡುಬರುವ ವಿವಿಧ ರೀತಿಯ ಏಜೆಂಟಿಕ್ ಉಪಯೋಗ ಪ್ರಕರಣಗಳನ್ನು ಪರಿಹರಿಸಲು ಬಲವಾದ ಲವಚಿಕತೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ, ಇದರಲ್ಲಿ:

- **ಕ್ರಮಾನುವಯಾಚಿ ಏಜೆಂಟ್ ಯೋಚನೆ** - ಹಂತ ಹಂತವದ ಕಾರ್ಯಪ್ರವಾಹಗಳ ಅಗತ್ಯವಿರುವ ಹಲವು ಸಂದರ್ಭಗಳಲ್ಲಿ.
- **ಸಮಕಾಲೀನ ಯೋಚನೆ** - ಏಜೆಂಟ್‌ಗಳಿಗೆ ಒಂದೇ ಸಮಯದಲ್ಲಿ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಬೇಕಾದ ಸಂದರ್ಭಗಳಲ್ಲಿ.
- **ಗುಂಪು ಚಾಟ್ ಯೋಚನೆ** - ಏಜೆಂಟ್‌ಗಳು ಒಂದು ಕಾರ್ಯವನ್ನು ಸೇರಿ ಸಹಕರಿಸುತ್ತಿರುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.
- **ಹ್ಯಾಂಡ್ಓಫ್ ಯೋಚನೆ** - ಸಬ್ಟಾಸ್ಕ್‌ಗಳನ್ನು ಪೂರೈಸಿದಂತೆ ಏಜೆಂಟ್‌ಗಳು ಕಾರ್ಯವನ್ನು ಒಬ್ಬರಿಂದ ಒಬ್ಬರಿಗೆ ಹಸ್ತಾಂತರಿಸುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.
- **ಮ್ಯಾಗ್ನೆಟಿಕ್ ಯೋಚನೆ** - ಮ್ಯಾನೇಜರ್ ಏಜೆಂಟ್ ಕೆಲಸ ಪಟ್ಟಿಯನ್ನು ರಚಿಸಿ ಬದಲಾಯಿಸಿ ಉಪ ಏಜೆಂಟ್‌ಗಳ ಸಂಯೋಜನೆಯನ್ನು ನಿರ್ವಹಿಸುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.

ಉತ್ಪಾದನೆಗೆ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನೀಡಲು, MAF ಯೂಟಿಲಿಟಿಗಳಿಗೂ ಹೊಂದಿಕೆಯಾಗಿರುವ ಲಕ್ಷಣಗಳನ್ನು ಒಳಗೊಂಡಿದೆ:

- **ವೀಕ್ಷಣಾ ಸಾಮರ್ಥ್ಯ** OpenTelemetry ಬಳಸಿ, AI ಏಜೆಂಟ್‌ನ ಪ್ರತಿ ಕ್ರಿಯೆಯೂ — ಸಾಧನ ಕರೆ, ಯೋಚನೆ ಹಂತಗಳು, ನೀತಿ ಹಂಚಿಕೆ ಮತ್ತು ಪ್ರದರ್ಶನ ನಿಗಾ ಕೊಡುವ Microsoft Foundry ಡ್ಯಾಶ್‌ಬೋರ್ಡ್‌ಗಳ ಮೂಲಕ — ಗಮನಿಸಿದಂತಾಗುತ್ತದೆ.
- **ಭದ್ರತೆ** Microsoft Foundry ನಲ್ಲಿ ನೇಟಿವ್ ಆಗಿ ಏಜೆಂಟುಗಳನ್ನು ಆತಿಥ್ಯ ನೀಡುವುದು, ಇದು ಪಾತ್ರಾಧಾರಿತ ಪ್ರವೇಶ, ಖಾಸಗಿ ಡೇಟಾ ನಿರ್ವಹಣೆ ಮತ್ತು ನಕ್ಸೇದ ಸಂರಕ್ಷಣೆಗಳನ್ನು ಒಳಗೊಂಡಿದೆ.
- **ದೃಢತೆ** ಏಜೆಂಟ್ ಧಾರೆಗಳು ಮತ್ತು ಕಾರ್ಯಪ್ರವಾಹಗಳು ಸ್ಥಗಿತ, ಪುನರಾರಂಭ ಮತ್ತು ತಪ್ಪುಗಳಿಂದ ಪುನರ್ವಸತಿ ಮಾಡಬಹುದು, ಈದು ದೀರ್ಘಾವಧಿ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಸಾಧ್ಯವಾಗಿಸುತ್ತದೆ.
- **ನಿಯಂತ್ರಣ** ಮಾನವ-ವಲಯದ ಕಾರ್ಯಪ್ರವಾಹಗಳು ಬೆಂಬಲಿತವಾಗಿದ್ದು, ಕಾರ್ಯಗಳನ್ನು ಮಾನವ ಅನುಮೋದನೆ ಅಗತ್ಯವಿದೆ ಎಂದು ಗುರುತಿಸಲಾಗುತ್ತದೆ.

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಸಹ ಅನೇಕವಾಗಿ ಸಂವಹನಾತ್ಮಕವಾಗಿರುವುದಾಗಿ ಗಮನ ಹರಿಸಲಾಗಿದೆ:

- **ಮೇಘ-ಸ್ವಾತಂತ್ರ್ಯ** - ಏಜೆಂಟ್‌ಗಳು ಕಂಟೇನರ್‌ಗಳಲ್ಲಿ, ಆನ್-ಪ್ರೆಮಿ ಮತ್ತು ವಿವಿಧ ಮೇಘಗಳಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸಬಹುದು.
- **ಪೂರೈಕೆದಾರ-ಸ್ವಾತಂತ್ರ್ಯ** - ನೀವು ಆಯ್ಕೆ ಮಾಡಿಕೊಂಡ SDK ಗಳ ಮೂಲಕ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಬಹುದು, ಇದರಲ್ಲಿ Azure OpenAI ಮತ್ತು OpenAI ಸೇರಿವೆ.
- **ಮುಕ್ತ ಪ್ರಮಾಣಗಳು ಸಮೀಕರಿಸುವುದು** - ಏಜೆಂಟ್‌ಗಳು Agent-to-Agent(A2A) ಮತ್ತು Model Context Protocol(MCP) ಇತ್ಯಾದಿ ಪ್ರೋಟೋಕಾಲ್‌ಗಳನ್ನು ಬಳಸಿರುತ್ತವೆ, ಇತರ ಏಜೆಂಟ್‌ಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಮತ್ತು ಬಳಸಲು.
- **ಪ್ಲಗಿನ್‌ಗಳು ಮತ್ತು ಸಂಪರ್ಕಕಗಳು** - Microsoft Fabric, SharePoint, Pinecone ಮತ್ತು Qdrant ಮುಂತಾದ ಡೇಟಾ ಮತ್ತು ಮೆಮೊರಿ ಸೇವೆಗಳಿಗೆ ಸಂಪರ್ಕ ಉಂಟಾಗಬಹುದು.

ಈಗ, ಈ ಲಕ್ಷಣಗಳನ್ನು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ ಕೆಲವು ಪ್ರಮುಖ ತತ್ವಗಳಿಗೆ ಹೇಗೆ ಅನ್ವಯಿಸಲ್ಪಡುವುದೋ ನೋಡೋಣ.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ ಮುಖ್ಯ ತತ್ವಗಳು

### ಏಜೆಂಟ್‌ಗಳು

![Agent Framework](../../../translated_images/kn/agent-components.410a06daf87b4fef.webp)

**ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವುದು**

ಏಜೆಂಟ್ ರಚನೆ ನಿರ್ದಿಷ್ಟ ಪಾತಮಾಹಿತಿ ಸೇವೆ (LLM ಪ್ರೊವೈಡರ್), AI ಏಜೆಂಟ್ ಅನುಸರಿಸಬೇಕಾದ ಸೂಚನೆಗಳ ಒಂದು ಸರಣಿ ಮತ್ತು ನಿಗದಿಪಡಿಸಿದ `name` ಮೂಲಕ ಮಾಡುತ್ತದೆ:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ಮೇಲಿನ ಉದಾಹರಣೆ `Azure OpenAI` ಬಳಸುತ್ತಿದೆ ಆದರೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿವಿಧ ಸೇವೆಗಳ ಬಳಕೆ ಮೂಲಕ ರಚಿಸಬಹುದು, ಅವುಗಳಲ್ಲೊಂದು `Microsoft Foundry Agent Service`:

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

ಅಥವಾ [MiniMax](https://platform.minimaxi.com/), ಇದು ದೊಡ್ಡ ಸನ್ನಿವೇಶ ವಿಂಡೋಗಳೊಂದಿಗೆ (ಅತ್ಯಧಿಕ 204K ಟೋಕನ್‌ಗಳ) OpenAI-ಸಂಗತ API ಒದಗಿಸುತ್ತದೆ:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ಅಥವಾ A2A ಪ್ರೋಟೋಕಾಲ್ ಬಳಸಿ ರಿಮೋಟ್ ಏಜೆಂಟ್‌ಗಳು:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ಏಜೆಂಟ್‌ಗಳನ್ನು ಚಲಿಸುವುದು**

ಏಜೆಂಟ್‌ಗಳು `.run` ಅಥವಾ `.run_stream` ವಿಧಾನಗಳನ್ನು ಬಳಸಿ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ, ಇದು ಸ್ಟ್ರಿಮಿಂಗ್ ಅಥವಾ ನಾನ್-ಸ್ಟ್ರಿಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಗಳಿಗಾಗಿ.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ಪ್ರತಿಯೊಂದು ಏಜೆಂಟ್ ಚಾಲನೆಗೂ `max_tokens`, `tools` ಮತ್ತು `model` ಹೀಗೆ ಆಯ್ಕೆಮಾಡಬಹುದಾದ ಪರಿಮಿತಿಗಳು ಇರುತ್ತವೆ.

ಇದು ಬಳಕೆದಾರರ ಕಾರ್ಯವನ್ನು ಪೂರೈಸಲು ನಿರ್ದಿಷ್ಟ ಮಾದರಿ ಅಥವಾ ಸಾಧನಗಳ ಅಗತ್ಯವಿರುವ ಸಂದರ್ಭಗಳಲ್ಲಿ ಉಪಯೋಗವಾಗುತ್ತದೆ.

**ಸಾಧನಗಳು**

ಸಾಧನಗಳನ್ನು ಏಜೆಂಟ್‌ವನ್ನು ವಿವರಿಸುವಾಗ ಸಮೇತವಾಗಿ ನಿರ್ಧರಿಸಬಹುದು:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ನೇರವಾಗಿ ChatAgent ರಚಿಸುವಾಗ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ಮತ್ತು ಏಜೆಂಟ್‌ಗಳನ್ನು ಚಲಿಸುವಾಗ ಕೂಡ:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ಈ ಓಟಕ್ಕೆ ಮಾತ್ರ ಒದಗಿಸಲಾಗಿರುವ ಸಾಧನ )
```

**ಏಜೆಂಟ್ ಥ್ರೆಡ್ಗಳು**

ಏಜೆಂಟ್ ಥ್ರೆಡ್ಗಳು ಬಹು-ಚರ್ಚೆ ಸಂಭಾಷಣೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ. ಥ್ರೆಡ್‌ಗಳು ಎರಡು ರೀತಿಯಲ್ಲಿ ರಚಿಸಬಹುದು:

- `get_new_thread()` ಬಳಸಿ, ಇದು ಥ್ರೆಡ್ ಅನ್ನು ಕಾಲದ ಮೇಲೆ ಉಳಿಸಲು ಸಮ್ಮತಿಸುತ್ತದೆ
- ಏಜೆಂಟ್ ಚಾಲನೆ ವೇಳೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಥ್ರೆಡ್ ರಚಿಸುವುದು ಮತ್ತು ಆ ಥ್ರೆಡ್ ಚಾಲನೆಯಲ್ಲಿರುವಾಗ ಮಾತ್ರ ಇರುತ್ತದೆ.

ಥ್ರೆಡ್ ರಚಿಸುವುದಕ್ಕೆ ಕೋಡ್ ಹೀಗಿದೆ:

```python
# ಹೊಸ ತಂತಿಯನ್ನು ರಚಿಸಿ.
thread = agent.get_new_thread() # ಅಜೆಂಟ್ ಅನ್ನು ಆ ತಂತಿಯೊಂದಿಗೆ ಚಲಾಯಿಸಿ.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

ನಂತರ ನೀವು ಥ್ರೆಡ್ ಅನ್ನು ಸಂರಕ್ಷಿಸಲು ಸರಣೀಕರಿಸಬಹುದು:

```python
# ಹೊಸ ಥ್ರೆಡ್ ಅನ್ನು ರಚಿಸಿ.
thread = agent.get_new_thread() 

# ಆ ಥ್ರೆಡ್ ಜೊತೆಗೆ ಏಜೆಂಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡು.

response = await agent.run("Hello, how are you?", thread=thread) 

# ಸಂಗ್ರಹಕ್ಕಾಗಿ ಥ್ರೆಡ್ ಅನ್ನು ಸರಣೀಕರಿಸಿ.

serialized_thread = await thread.serialize() 

# ಸಂಗ್ರಹದಿಂದ ಲೋಡ್ ಮಾಡಿದ ನಂತರ ಥ್ರೆಡ್ ಸ್ಥಿತಿಯನ್ನು ಡಿಸೆರಿಯಲೈಜ್ ಮಾಡಿ.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ಏಜೆಂಟ್ ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್**

ಏಜೆಂಟ್‌ಗಳು ಸಾಧನಗಳು ಮತ್ತು LLM ಗಳೊಂದಿಗೆ ಸಹಕರಿಸಿ ಬಳಕೆದಾರರ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸುತ್ತವೆ. ಕೆಲವು ಸಂದರ್ಭಗಳಲ್ಲಿ, ಈ ಪರಸ್ಪರ ಕ್ರಿಯೆ ನಡುವೆ ನಿರ್ವಹಣೆ ಅಥವಾ ಟ್ರ್ಯಾಕಿಂಗ್ ಬೇಕಾಗುತ್ತದೆ. ಏಜೆಂಟ್ ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್ ಇದನ್ನು ಈ ಕೆಳಗಿನ ಮೂಲಕ ಸಾಧ್ಯಮಾಡುತ್ತದೆ:

*ಫಂಕ್ಷನ್ ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್*

ಈ ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್ ಏಜೆಂಟು ಮತ್ತು ಕಾರ್ಯ/ಸಾಧನದ ನಡುವೆ ಕ್ರಿಯೆಯನ್ನು ನಿರ್ವಹಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ. ಉದಾಹರಣೆಗೆ, ಕಾರ್ಯ ಕರೆ ಸಂದರ್ಭದಲ್ಲಿ ಲಾಗಿಂಗ್ ಅನ್ನು ನಡೆಸಬಹುದು.

ಕೆಳಗಿನ ಕೋಡಿನಲ್ಲಿ `next` ಅನ್ನು ಬಳಸಿ ಮುಂದಿನ ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್ ಅಥವಾ ನಿಜವಾದ ಕಾರ್ಯವನ್ನು ಕರೆ ಮಾಡಲು ನಿರ್ಧರಿಸಲಾಗುತ್ತದೆ.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ಪೂರ್ವ ಪ್ರಕ್ರಿಯೆ: ಕಾರ್ಯ ನಡೆಸುವ ಮೊದಲು ಲಾಗ್ ಮಾಡುವುದು
    print(f"[Function] Calling {context.function.name}")

    # ಮುಂದಿನ ಮಧ್ಯಮ ಅಥವಾ ಕಾರ್ಯಾಚರಣೆಗೆ ಮುಂದುವರೆಯಿರಿ
    await next(context)

    # ನಂತರದ ಪ್ರಕ್ರಿಯೆ: ಕಾರ್ಯ ನಡೆಸಿದ ನಂತರ ಲಾಗ್ ಮಾಡುವುದು
    print(f"[Function] {context.function.name} completed")
```

*ಚಾಟ್ ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್*

ಏಜೆಂಟ್ ಮತ್ತು LLM ನಡುವಿನ ವಿನಂತಿಗಳಲ್ಲಿ ಭಾಗವಹಿಸುವ ಅಥವಾ ಲಾಗ್ ಮಾಡಲು ಈ ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್ ಸಹಾಯ ಮಾಡುತ್ತದೆ.

ಇದರಲ್ಲಿ AI ಸೇವೆಗೆ ಕಳುಹಿಸುವ `messages` ಮುಂತಾದ ಮುಖ್ಯ ಮಾಹಿತಿ ಇರುತ್ತದೆ.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ಪೂರ್ವ-ಪ್ರಕ್ರಿಯೆ: AI ಕರೆಗಾಗಿ ಮುಂಚಿತವಾಗಿ ಲಾಗ್ ಮಾಡು
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ಮುಂದಿನ ಮಿಡ್ಲ್ವೇರ್ ಅಥವಾ AI ಸೇವೆಗೆ ಮುಂದುವರೆಯಿರಿ
    await next(context)

    # ನಂತರ-ಪ್ರಕ್ರಿಯೆ: AI ಪ್ರತಿಕ್ರಿಯೆಯ ನಂತರ ಲಾಗ್ ಮಾಡು
    print("[Chat] AI response received")

```

**ಏಜೆಂಟ್ ಮೆಮೊರಿ**

`Agentic Memory` ಪಾಠದಲ್ಲಿ ವಿವರಿಸಿದಂತೆ, ಮೆಮೊರಿ ವಿವಿಧ ಸಂದರ್ಭಗಳಲ್ಲಿ ಏಜೆಂಟ್ ಕಾರ್ಯಾಚರಣೆಗೆ ಮುಖ್ಯಾಂಶವಾಗಿದೆ. MAF ವಿವಿಧ ಪ್ರಕಾರದ ಮೆಮೊರಿಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ:

*ಇನ್-ಮೆಮೊರಿ ಸಂರক্ষণ*

ಇದು ಅಪ್ಲಿಕೇಶನ್ ಚಾಲನೆಯ ಸಮಯದಲ್ಲಿ ಥ್ರೆಡ್ಗಳು ಒಳಗುತ್ತಿರುವ ಮೆಮೊರಿ.

```python
# ಹೊಸ ತಂತಿ ರಚಿಸಿ.
thread = agent.get_new_thread() # ಆ ಎಜೆಂಟ್ ಅನ್ನು ಆ ತಂತಿಯೊಂದಿಗೆ ದೌಡಾಯಿಸು.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*ಸ್ಥಾಯಿಬದ್ಧ ಸಂದೇಶಗಳು*

ವಿಭಿನ್ನ ಸೆಷನ್‌ಗಳ ಕಾಲ ಸಂಭಾಷಣೆ ಇತಿಹಾಸವನ್ನು ಸಂರಕ್ಷಿಸುವುದು. ಇದನ್ನು `chat_message_store_factory` ಬಳಸಿ ನಿರ್ಧರಿಸಲಾಗಿದೆ:

```python
from agent_framework import ChatMessageStore

# ಕಸ್ಟಮ್ ಸಂದೇಶ ಅಂಗಡಿ ರಚಿಸಿ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ಡೈನಾಮಿಕ್ ಮೆಮೊರಿ*

ಏಜೆಂಟ್‌ಗಳು ಚಲಿಸುವ ಮುನ್ನ ಈ ಮೆಮೊರಿಗಳನ್ನು ಸನ್ನಿವೇಶಕ್ಕೆ ಸೇರಿಸಲಾಗುತ್ತದೆ. ಈ ಮೆಮೊರಿಗಳು mem0 ಮುಂತಾದ ಹೊರಗಿನ ಸೇವೆಗಳಲ್ಲಿ ಸಂಗ್ರಹಿಸಬಹುದಾಗಿವೆ:

```python
from agent_framework.mem0 import Mem0Provider

# ಸುಧಾರಿತ ಸ್ಮೃತಿ ಸಾಮರ್ಥ್ಯಗಳಿಗಾಗಿ Mem0 ಬಳಕೆಮಾಡುತ್ತಿದೆ
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

**ಏಜೆಂಟ್ ವೀಕ್ಷಣಾ ಸಾಮರ್ಥ್ಯ**

ವಿಶ್ವಾಸಾರ್ಹ ಮತ್ತು ನಿರ್ವಹಣಾರ್ಹ ಏಜೆಂಟಿಕ್ ವ್ಯವಸ್ಥೆಗಳನ್ನು ನಿರ್ಮಿಸುವಲ್ಲಿ ವೀಕ್ಷಣಾ ಸಾಮರ್ಥ್ಯ ಮಹತ್ವಪೂರ್ಣವಾಗಿದೆ. MAF OpenTelemetry ಅನ್ನು ಸಂಯೋಜಿಸಿ ಉತ್ತಮ ವೀಕ್ಷಣಾ ಸಾಮರ್ಥ್ಯಕ್ಕಾಗಿ ಟ್ರೇಸಿಂಗ್ ಮತ್ತು ಮೀಟರ್ಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ಏನಾದರು ಮಾಡಿ
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### ಕಾರ್ಯಪ್ರವಾಹಗಳು

MAF ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ, ಇವು ಪೂರ್ಣಗೊಳಿಸುವ ಹಂತಗಳ ಪೂರ್ವನಿಗದಿ ಮತ್ತು ಅವುಗಳಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಭಾಗಗಳಾಗಿ ಒಳಗೊಂಡಿರುತ್ತವೆ.

ಕಾರ್ಯಪ್ರವಾಹಗಳು ವಿಭಿನ್ನ ಘಟಕಗಳಿಂದ ಕೂಡಿವೆ, ಇದರಿಂದ ಉತ್ತಮ ನಿಯಂತ್ರಣದ ಹರಿವು ಸಾಧ್ಯ. ಕಾರ್ಯಪ್ರವಾಹಗಳು **ಬಹು-ಏಜೆಂಟ್ ಯೋಚನೆ** ಮತ್ತು **ಚೆಕ್‌ಪಾಯಿಂಟಿಂಗ್** ಕೂಡ ನೆರವಾಗುತ್ತವೆ.

ಕಾರ್ಯಪ್ರವಾಹದ ಮುಖ್ಯ ಘಟಕಗಳು:

**ಕಾರ್ಯನಿರ್ವಹಿಸುವವರು**

ಕಾರ್ಯನಿರ್ವಹಿಸುವವರು ಪ್ರವೇಶ ಸಂದೇಶಗಳನ್ನು ಸ್ವೀಕರಿಸಿ, ನಿಗದಿಪಡಿಸಿದ ಕಾರ್ಯಗಳನ್ನು ನೆರವೇರಿಸಿ, ನಂತರ ಫಲಿತಾಂಶ ಸಂದೇಶವನ್ನು ಉತ್ಪಾದಿಸುವವರು. ಇದು ದೊಡ್ಡ ಕಾರ್ಯಪಟುವಿನ ಕಡೆಗೆ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಮುಂದುವರಿಸುತ್ತದೆ. ಕಾರ್ಯನಿರ್ವಹಿಸುವವರು AI ಏಜೆಂಟ್ ಅಥವಾ ಕಸ್ಟಮ್ ಲಾಜಿಕ್ ಇರಬಹುದು.

**ಎಡ್ಜ್‌ಗಳು**

ಕಾರ್ಯಪ್ರವಾಹದಲ್ಲಿ ಸಂದೇಶ ಹರಿವನ್ನು ನಿರ್ಧರಿಸಲು ಎಡ್ಜ್‌ಗಳು ಬಳಕೆಯಾಗುತ್ತವೆ. ಅವು:

*ನೇರ ಎಡ್ಜ್‌ಗಳು* - ಕಾರ್ಯನಿರ್ವಹಿಸುವವರ ನಡುವಿನ ಸರಳ ಒಬ್ಬ-ಕಳೆದ ಸಂಪರ್ಕಗಳು:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*ಶರತ ಎಡ್ಜ್‌ಗಳು* - ನಿರ್ದಿಷ್ಟ ಶರತ್ತು ಪೂರೈಸಿದ ಮೇಲೆ ಸಕ್ರಿಯವಾಗುವವು. ಉದಾಹರಣೆಗಾಗಿ, ಹೋಟೆಲ್ ಕೊಠಡಿಗಳು ಲಭ್ಯವಿಲ್ಲದಿರುವಾಗ, ಕಾರ್ಯನಿರ್ವಹಿಸುವವರು ಬೇರೆಯ ಆಯ್ಕೆಯನ್ನು ಸೂಚಿಸಬಹುದು.

*ಸ್ವಿಚ್-ಕೇಸ್ ಎಡ್ಜ್‌ಗಳು* - ಶರತ್ತು ಆಧರಿಸಿ ಸಂದೇಶಗಳನ್ನು ವಿಭಿನ್ನ ಕಾರ್ಯನಿರ್ವಹಿಸುವವರಿಗೆ ಮಾರ್ಗದರ್ಶನ ಮಾಡುತ್ತದೆ. ಉದಾಹರಣೆಗೆ, ಪ್ರಾಧಾನ್ಯ ಪ್ರವೇಶವನ್ನು ಹೊಂದಿರುವ ಪ್ರಯಾಣಿಕರಿಗೆ ಬೇರೆಯ ಕಾರ್ಯಪ್ರವಾಹದಿಂದ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು.

*ಫ್ಯಾನ್-ಔಟ್ ಎಡ್ಜ್‌ಗಳು* - ಒಂದೇ ಸಂದೇಶವನ್ನು ಹಲವು ಗುರಿಗಳಿಗೆ ಕಳುಹಿಸುವುದು.

*ಫ್ಯಾನ್-ಇನ್ ಎಡ್ಜ್‌ಗಳು* - ವಿಭಿನ್ನ ಕಾರ್ಯನಿರ್ವಹಿಸುವವರಿಂದ ಬಹಳಷ್ಟು ಸಂದೇಶಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ ಒಂದೇ ಗುರಿಗೆ ಕಳುಹಿಸುವುದು.

**ಈವೆಂಟ್ಸ್**

ಕಾರ್ಯಪ್ರವಾಹಗಳಲ್ಲಿ ಉತ್ತಮ ವೀಕ್ಷಣಾ ಸಾಮರ್ಥ್ಯ ನೀಡಲು, MAF ಕಾರ್ಯಗತಗೊಳಿಸುವ built-in ಈವೆಂಟ್ಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ, ಅವು:

- `WorkflowStartedEvent`  - ಕಾರ್ಯಪ್ರವಾಹ ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ ಆರಂಭ
- `WorkflowOutputEvent` - ಕಾರ್ಯಪ್ರವಾಹವು ಔಟ್‌ಪುಟ್ ಉತ್ಪಾದಿಸುತ್ತದೆ
- `WorkflowErrorEvent` - ಕಾರ್ಯಪ್ರವಾಹದಲ್ಲಿ ತಪ್ಪು ಉಂಟಾಗುತ್ತದೆ
- `ExecutorInvokeEvent`  - ಕಾರ್ಯನಿರ್ವಹಿಸುವವರು ಪ್ರಕ್ರಿಯೆ ಆರಂಭಿಸುತ್ತಾರೆ
- `ExecutorCompleteEvent`  -  ಕಾರ್ಯನಿರ್ವಹಿಸುವವರು ಪ್ರಕ್ರಿಯೆ ಮುಗಿಸುತ್ತಾರೆ
- `RequestInfoEvent` - ವಿನಂತಿ ಸಲ್ಲಿಸಲಾಗಿದೆ

## ಉನ್ನತ MAF ಮಾದರಿಗಳು

ಮೇಲಿನ ವಿಭಾಗಗಳು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ ಪ್ರಮುಖ ತತ್ವಗಳನ್ನು ಒಳಗೊಂಡಿವೆ. ನೀವು ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿದಾಗ, ಕೆಲವು ಉನ್ನತ ಮಾದರಿಗಳನ್ನು ಪರಿಗಣಿಸಬೇಕಾಗಿದೆ:

- **ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್ ಸಂಯೋಜನೆ**: ಹಲವು ಮಧ್ಯಮ ಸಾಫ್ಟ್‌ವೇರ್ ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು (ಲಾಗಿಂಗ್, ಪ್ರಾಧಿಕಾರ, ದರ-ನಿಯಮನ) ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಶ್ರೇಣೀಬದ್ಧ ಮಾಡಿ ಏಜೆಂಟ್ ನಡೆಗಿನ ಕುರಿತು ಸೂಕ್ಷ್ಮ ನಿಯಂತ್ರಣವನ್ನು ಪಡೆಯುವುದು.
- **ಕಾರ್ಯಪ್ರವಾಹ ಚೆಕ್‌ಪಾಯಿಂಟಿಂಗ್**: ಕಾರ್ಯಪ್ರವಾಹ ಈವೆಂಟ್ಗಳು ಮತ್ತು ಸರಣೀಕರಣವನ್ನು ಬಳಸಿ ದೀರ್ಘಾವಧಿ ಏಜೆಂಟ್ ಪ್ರಕ್ರಿಯೆಗಳನ್ನು ಉಳಿಸಬೇಕು ಮತ್ತು ಪುನಃ ಪ್ರಾರಂಭಿಸಬೇಕು.
- **ಡೈನಾಮಿಕ್ ಸಾಧನ ಆಯ್ಕೆ**: ಸಾಧನ ವಿವರಣೆಗಳ ಮೇಲೆ RAG ಅನ್ನು MAF ಸಾಧನ ನೋಂದಣಿಯೊಂದಿಗೆ ಒಂದಾಗಿಸಿ ಪ್ರತಿ ಪ್ರಶ್ನೆಗೆ ಅನ್ವಯಿಸುವ ಸಾಧನಗಳನ್ನು ಮಾತ್ರ ಪ್ರದರ್ಶಿಸುವುದು.
- **ಬಹು-ಏಜೆಂಟ್ ಹ್ಯಾಂಡ್ಓಫ್**: ಕಾರ್ಯಪ್ರವಾಹ ಎಡ್ಜ್‌ಗಳು ಮತ್ತು ಶರತ ಅನುಸಾರ ಮಾರ್ಗದರ್ಶನ ಬಳಸಿ ವಿಶೇಷೀಕೃತ ಏಜೆಂಟ್‌ಗಳ ನಡುವೆ ಹ್ಯಾಂಡ್ಓಫ್‌ಗಳನ್ನು ಸಂಚಾಲನೆ ಮಾಡುವುದು.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ LangChain / LangGraph ಏಜೆಂಟ್‌ಗಳನ್ನು ಆತಿಥ್ಯ ನೀಡುವುದು

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ **ಫ್ರೇಮ್‌ವರ್ಕ್-ಇಂಟರ್‌ಒಪರೇಬಲ್** ಆಗಿದ್ದು, ನೀವು MAF ಮೂಲಕ ಬರೆದೆದಿಲ್ಲದ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸೀಮಿತವಾಗಿಲ್ಲ. ನೀವು ಈಗಾಗಲೇ **LangChain** ಅಥವಾ **LangGraph** ಬಳಸಿ ನಿರ್ಮಿಸಿದ ಏಜೆಂಟ್ ಇದ್ದರೆ, ಅದನ್ನು **Microsoft Foundry ಆತಿಥ್ಯ ಏಜೆಂಟ್** ಆಗಿ ನಡಿಸಲು, ಫೌಂಡ್ರಿಯು ರನ್‌ಟೈಮ್, ಸೆಷನ್‌ಗಳು, ಸ್ಕೇಲಿಂಗ್, ಗುರುತು ಪರಿಶೀಲನೆ ಮತ್ತು ಪ್ರೋಟೋಕಾಲ್ ಎಂಡಿಪಾಯಿಂಟ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಮತ್ತು ನಿಮ್ಮ ಏಜೆಂಟ್ ಲಾಜಿಕ್ LangGraph ನಲ್ಲಿ ಉಳಿಯುತ್ತದೆ.

ಇದು `langchain_azure_ai.agents.hosting` ಪ್ಯಾಕೇಜ್ ಜೊತೆಗೆ ಆಗಿದ್ದು, ಅದು ಫೌಂಡ್ರಿಯು ಆತಿಥ್ಯ ಏಜೆಂಟ್‌ಗಳು ಬಳಸುವ ಪ್ರೋಟೋಕಾಲ್‌ಗಳ ಮೇಲೆ ಸಂಯೋಜಿಸಲಾದ LangGraph ಗ್ರಾಫ್ ಅನ್ನು ಪುರಸ್ಕರಿಸುತ್ತದೆ.

**1. ಹೋಸ್ಟಿಂಗ್ ಹೆಚ್ಚುವರಿ ಸ್ಥಾಪನೆ:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ಹೆಚ್ಚುವರಿ ಫೌಂಡ್ರಿ ಪ್ರೋಟೋಕಾಲ್ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಸ್ಥಾಪಿಸುತ್ತದೆ: `azure-ai-agentserver-responses` (OpenAI-ಸಂಗತ `/responses` ಎಂಡಿಪಾಯಿಂಟ್) ಮತ್ತು `azure-ai-agentserver-invocations` (ಸಾಮಾನ್ಯ `/invocations` ಎಂಡಿಪಾಯಿಂಟ್).

**2. ಹೋಸ್ಟಿಂಗ್ ಪ್ರೋಟೋಕಾಲ್ ಆಯ್ಕೆ ಮಾಡಿಕೊಳ್ಳಿ:**

| ಪ್ರೋಟೋಕಾಲ್ | ಹೋಸ್ಟ್ ತರಗತಿ | ಎಂಡಿಪಾಯಿಂಟ್ | ಯಾವಾಗ ಬಳಸುವುದು |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-ಸಂಗತ ಚಾಟ್, ಸ್ಟ್ರಿಮಿಂಗ್, ಪ್ರತಿಕ್ರಿಯೆ ಇತಿಹಾಸ ಮತ್ತು ಸಂಭಾಷಣೆ ಥ್ರೆಡಿಂಗ್ ಬೇಕಾದಾಗ — ಸಂಭಾಷಣಾತ್ಮಕ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಶಿಫಾರಸಿನ ಡೀಫಾಲ್ಟ್. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | ನೀವು ಕಸ್ಟಮ್ JSON ಶೇಪ್, ವೆಬ್‌ಹುಕ್ ಶೈಲಿ ಎಂಡಿಪಾಯಿಂಟ್ ಅಥವಾ ಅನ್ಸಂಭಾಷಣಾತ್ಮಕ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಅವಶ್ಯಕವಿದ್ದಾಗ. |

ಏಕೆಂದರೆ **Responses API ಫೌಂಡ್ರಿಯಲ್ಲಿನ ಏಜೆಂಟ್ ಶೈಲಿ ಅಭಿವೃದ್ಧಿಗಾಗಿ ಪ್ರಮುಖ API**, ಬಹುತೇಕ ಏಜೆಂಟ್‌ಗಳಿಗೆ `ResponsesHostServer` ಯಿಂದ ಪ್ರಾರಂಭಿಸಿರಿ.

**3. ಪರಿಮ окружённые ಮೌಲ್ಯಗಳನ್ನು ಸಂರಚಿಸಿ** (`az login` ಮೊದಲು ಮಾಡಿ, ಹೀಗಾಗಿ `DefaultAzureCredential` ದೃಢೀಕರಿಸಲು ಸಾಧ್ಯ): 

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ಏಜೆಂಟ್ ನಂತರ ಫೌಂಡ್ರಿಯಲ್ಲಿ ಆತಿಥ್ಯ ಏಜೆಂಟ್ ಆಗಿ ನಡೆದಾಗ, ವೇದಿಕೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ `FOUNDRY_PROJECT_ENDPOINT` ಅನ್ನು ಪೂರೈಸುತ್ತದೆ.

**4. Responses ಪ್ರೋಟೋಕಾಲ್ ಮೂಲಕ LangGraph ಏಜೆಂಟ್ ಅನ್ನು ಅನಾವರಣಗೊಳಿಸಿ:**

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

    # ChatOpenAI ಇಲ್ಲಿ Foundry ಪ್ರಾಜೆಕ್ಟಿನ OpenAI-ಸಮ್ಮತ (ಪ್ರತಿಕ್ರಿಯೆಗಳು) ಎಂಡ್‌ಪಾಯಿಂಟ್ ಗುರಿಯಾಗಿಸಿದೆ.
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

ಇದನ್ನು ಸ್ಥಳೀಯವಾಗಿ `python main.py`기로 ನಡೆಸಿ, ನಂತರ `http://localhost:8088/responses` ಗೆ Responses ವಿನಂತಿಯನ್ನು ಕಳುಹಿಸಿ.

**ಮುಖ್ಯ ನಡೆಗಳು:**

- **ಸಂಭಾಷಣೆಗಳು**: ಗ್ರಾಹಕರು `previous_response_id` ಅಥವಾ `conversation` ID ಒದಗಿಸುತ್ತಾರೆ ಸಂಭಾಷಣೆ ಮುಂದುವರಿಸಲು. ನಿಮ್ಮ ಗ್ರಾಫ್ LangGraph ಚೆಕ್‌ಪಾಯಿಂಟರ್‌ ಜೊತೆಗೆ ಸಂಯೋಜಿತವಾಗಿದ್ದರೆ, ಫೌಂಡ್ರಿ ಸಂಭಾಷಣೆ ಸ್ಥಿತಿಯನ್ನು ಚೆಕ್‌ಪಾಯಿಂಟ್‌ಗೆ ಕೀ ಮಾಡಿ (ಉತ್ಪಾದನೆಯಲ್ಲಿ ದೀರ್ಘಕಾಲಿಕ ಚೆಕ್‌ಪಾಯಿಂಟರ್ ಬಳಸಿ; ಸ್ಥಳೀಯ ಪರೀಕ್ಷೆಗಾಗಿ `MemorySaver` ಸೂಕ್ತವಾಗಿದೆ).
- **ಮಾನವ-ವಲಯದಲ್ಲಿ**: ನಿಮ್ಮ ಗ್ರಾಫ್ LangGraph `interrupt()` ಬಳಸಿದರೆ, `ResponsesHostServer` ಪೆಂಡಿಂಗ್ ಅಂತರವನ್ನು Responses `function_call` / `mcp_approval_request` ಐಟಂ ಆಗಿ ಮೆಲುಕು ಹಾಕುತ್ತದೆ, ಮತ್ತು ಗ್ರಾಹಕರು ಸರಿಯಾದ `function_call_output` / `mcp_approval_response` ಮೂಲಕ ಪುನರಾರಂಭ ಮಾಡುತ್ತಾರೆ.
- **Foundry ಗೆ ನಿಯೋಜಿಸಿ**: Azure Developer CLI ಬಳಸಿ — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ಸ್ಥಳীয়, ಡೋಕರ್ ಅಗತ್ಯವಿದೆ), ಬಳಿಕ `azd provision` ಮತ್ತು `azd deploy`. ಆತಿಥ್ಯ-ಏಜೆಂಟ್ ನಿಯೋಜನೆಗೆ **Foundry Project Manager** ಪಾತ್ರ ಅಗತ್ಯ.

ಈ ಉದಾಹರಣೆ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ನಲ್ಲಿ ಕಾಮಗಾರಿ ರೂಪಿತವಾಗಿದೆ. ಪೂರ್ಣ ನಡೆ (Invocations ಪ್ರೋಟೋಕಾಲ್, ಕಸ್ಟಮ್ ವಿನಂತಿ ಸ್ಥಾವರಗಳು, ಮತ್ತು ತೊಂದರೆ ನಿವಾರಣೆ)ಗಾಗಿ [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ನೋಡಿ.

## ಕೋಡ್ ಮಾದರಿಗಳು 

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಗಾಗಿ ಕೋಡ್ ಮಾದರಿಗಳನ್ನು ಈ ರೆಪೋಸಿಟರಿಯಲ್ಲಿ `xx-python-agent-framework` ಮತ್ತು `xx-dotnet-agent-framework` ಫೈಲ್‌ಗಳಲ್ಲಿ ಕಂಡುಹಿಡಿಯಬಹುದು.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿವೆಯೇ?

ಇತರ ಕಲಿಯುವವರನ್ನೂ ಭೇಟಿ ಮಾಡುವುದು, ಕಾರ್ಯಾಲಯ ಸಮಯದಲ್ಲಿ ಪಾಲ್ಗೊಳ್ಳುವುದು ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಪಡೆಯಲು [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ಗೆ ಸೇರಿ.
## ಹಿಂದಿನ ಪಾಠ

[AI ಏಜೆಂಟ್‌ಗಳ ಮೆಮೊರಿ](../13-agent-memory/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಕಂಪ್ಯೂಟರ್ ಬಳಕೆಯ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->