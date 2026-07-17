# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಂಬರ್‌ಕ್ ಅನ್ವೇಷಣೆ

![Agent Framework](../../../translated_images/kn/lesson-14-thumbnail.90df0065b9d234ee.webp)

### ಪರಿಚಯ

ಈ ಪಾಠವು ಒಳಗೊಂಡಿದೆ:

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಂಬರ್‌ಕ್ ಅನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು: ಮುಖ್ಯ ವೈಶಿಷ್ಟ್ಯಗಳು ಮತ್ತು ಮೌಲ್ಯ  
- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಂಬರ್‌ಕ್ ಪ್ರಮುಖ ತತ್ವಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು
- ಅಧುನಾತನ MAF ಮಾದರಿಗಳು: ವರ್ಕ್‌ಫ್ಲೋಗಳು, ಮೀಡಿಯೇಲ್, ಮತ್ತು ಮೆಮೊರಿ

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ತಿಳಿದುಕೊಳ್ಳುತ್ತೀರಿ:

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಂಬರ್‌ಕ್ ಬಳಸಿಕೊಂಡು ಉತ್ಪಾದನೆಗೆ ಸಿದ್ಧ AI ಏಜೆಂಟ್‌ಗಳು ನಿರ್ಮಿಸುವುದು
- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಂಬರ್‌ಕ್ ಮುಖ್ಯ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ನಿಮ್ಮ ಏಜೆಂಟಿಕ್ ಉಪಯೋಗ ಪ್ರಕರಣಗಳಿಗೆ ಅನ್ವಯಿಸುವುದು
- ವರ್ಕ್‌ಫ್ಲೋಗಳು, ಮೀಡಿಯೇಲ್ ಮತ್ತು ಅವಲೋಕನ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒಳಗೊಂಡು ಉನ್ನತ ಮಟ್ಟದ ಮಾದರಿಗಳನ್ನು ಬಳಸುವುದು

## ಕೋಡ್ ಉದಾಹರಣೆಗಳು 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)ಗಾಗಿ ಕೋಡ್ ಉದಾಹರಣೆಗಳನ್ನು ಈ ಸಂಗ್ರಹದಲ್ಲಿ `xx-python-agent-framework` ಮತ್ತು `xx-dotnet-agent-framework` ಫೈಲ್‌ಗಳಲ್ಲಿ ಕಂಡುಹಿಡಿಯಬಹುದು.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಂಬರ್‌ಕ್ ಅನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು

![Framework Intro](../../../translated_images/kn/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ಎನ್ನುವುದು AI ಏಜೆಂಟ್‌ಗಳು ನಿರ್ಮಿಸಲು ಮೈಕ್ರೋಸಾಫ್ಟ್‌ವರ ಒಕ್ಕೂಟದ ಫ್ರೇಂಬರ್‌ಕ್ ಆಗಿದೆ. ಇದು ಉತ್ಪಾದನೆ ಹಾಗೂ ಸಂಶೋಧನಾ ಪರಿಸರಗಳಲ್ಲಿ ಕಂಡುಬರುವ ವಿವಿಧ ಏಜೆಂಟಿಕ್ ಉಪಯೋಗ ಪ್ರಕರಣಗಳನ್ನು ನಿಬೇಧಿಸಲು ಲವಚೀತೆ ನೀಡುತ್ತದೆ. ಉದಾಹರಣೆಗಳಿಗೆ:

- **ಕ್ರಮವಾಗಿ ಏಜೆಂಟ್ ಸಂಚಾಲನೆ** ಅಂದರೆ ಹಂತ ಹಂತದ ವರ್ಕ್‌ಫ್ಲೋ gerekiರುವ ಪರಿಸರಗಳಲ್ಲಿ.
- **ಸಮಕಾಲೀನ ಸಂಚಾಲನೆ** ಅಂದರೆ ಏಜೆಂಟ್‌ಗಳು ಒಂದೇ ಸಮಯದಲ್ಲಿ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಬೇಕಾಗಿರುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.
- **ಗುಂಪು ಚಾಟ್ ಸಂಚಾಲನೆ** ಅಂದರೆ ಏಜೆಂಟ್‌ಗಳು ಒಂದೇ ಕಾರ್ಯದಲ್ಲಿ ಜೊತೆಯಾಗುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.
- **ಹ್ಯಾಂಡ್ಓಫ್ ಸಂಚಾಲನೆ** ಅಂದರೆ ಉಪಕಾರ್ಯಗಳನ್ನು ಮುಗಿಸಿದಂತೆ ಏಜೆಂಟ್‌ಗಳು ಪರಸ್ಪರ ಕಾರ್ಯವನ್ನು ಹಸ್ತಾಂತರಿಸುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.
- **磁 ನೀವುಕ ಸಂಚಾಲನೆ** ಅಂದರೆ ನಿರ್ವಹಣಾ ಏಜೆಂಟ್ ಕಾರ್ಯಪಟ್ಟಿ ರಚಿಸಿ ತಿದ್ದುಪಡಿ ಮಾಡುತ್ತಾ ಉಪ ಏಜೆಂಟ್‌ಗಳನ್ನು ಸಂಯೋಜಿಸುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.

ಉತ್ಪಾದನೆಯಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಒದಗಿಸಲು MAF ಇವುಗಳನ್ನೂ ಸೇರಿಸಿದೆ:

- **ಅಗತ್ಯವಿರುವ ಅವಲೋಕನ** OpenTelemetry ಬಳಸಿಕೊಂಡು, AI ಏಜೆಂಟ್‌ನ ಪ್ರತಿಯೊಂದು ಕ್ರಿಯೆಯನ್ನೂ, ಉಪಕರಣ ಕರೆ, ಸಂಚಾಲನೆ ಹಂತ, ಯುಕ್ತಿಚಿಂತನೆ ಪ್ರವಾದ, ಮತ್ತು Microsoft's Foundry ಡ್ಯಾಶ್ಬೋರ್ಡ್‌ಗಳ ಮೂಲಕ ಕಾರ್ಯಕ್ಷಮತೆ ದೂರದರ್ಜೆಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡುವುದು.
- **ಸೂಕ್ಷ್ಮತೆ** Microsoft Foundry ನಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ನೇಟೀಕವಾಗಿ ಆತಿಥ್ಯ ನೀಡುವುದು, ಇದರಲ್ಲಿ ಪಾತ್ರ ಆಧಾರಿತ ಪ್ರವೇಶ ನಿಯಂತ್ರಣ, ಖಾಸಗಿ ಡೇಟಾ ಹ್ಯಾಂಡ್ಲಿಂಗ್ ಮತ್ತು ನಿರ್ಮಿತ ವಿಷಯ ಸುರಕ್ಷತೆ ಸೇರಿವೆ.
- **ಸುದೃಢತೆ** ಏಜೆಂಟ್ ಥ್ರೆಡ್‌ಗಳು ಮತ್ತು ವರ್ಕ್‌ಫ್ಲೋಗಳು ಸ್ಥಗಿತಮಾಡಿ, ಮರುಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ದೋಷಗಳಿಂದ ಮರುಪಡೆಯುವ ಅವಶ್ಯಕತೆಗಳಿರುವ, ಹೀಗೆ ದೀರ್ಘ ಅವಧಿಗಾಗುವ ಪ್ರಕ್ರಿಯೆ ನಡೆಸಲು ಅವಕಾಶ.
- **ನಿಯಂತ್ರಣ** ಮಾನವನ ತೊಡಗಣೆಯ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ಬೆಂಬಲಿಸುವುದು, ಕಾರ್ಯಗಳನ್ನು ಮಾನವ ಅನುಮೋದನೆ ಅಗತ್ಯವಿದೆ ಎಂದು ಗುರುತಿಸುವುದು.

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಂಬರ್‌ಕ್ ಸಹ ಇಂಟರ್‌ಒಪರೇಬಲಿಟಿಗೆ ಗಮನ ಹರಿಸಿದೆ:

- **ಮೇಘ-ಸ್ವತಂತ್ರವಾಗಿರುವುದು** - ಏಜೆಂಟ್‌ಗಳು ಕಂಟೇನರ್‌ಗಳಲ್ಲಿ, ಆನ-ಪ್ರೇಮ್ ಮತ್ತು ಹಲವು ಬೇರೆ ಬೇರೆ ಮೇಘಗಳಲ್ಲೂ ನಡೆಯಬಹುದು.
- **ಪ್ರದಾಯಕರ ನಿರಪേക്ഷತೆ** - ನೀವು ಇಚ್ಛಿಸುವ SDK ಮೂಲಕ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಬಹುದು, ಉದಾಹರಣೆಗೆ Azure OpenAI ಮತ್ತು OpenAI
- **ತೆರೆದ ಮಾನಕಗಳ ಸಂಯೋಜನೆ** - ಏಜೆಂಟ್-ಇಂದ-ಏಜೆಂಟ್(Agent-to-Agent, A2A) ಮತ್ತು ಮಾದರಿ ಸಾರಾಂಶ ಪ್ರೋಟೊಕಾಲ್(Model Context Protocol, MCP) ಮುಂತಾದ ಪ್ರೋಟೊಕಾಲ್‌ಗಳನ್ನು ಬಳಸಿ ಇತರ ಏಜೆಂಟ್‌ಗಳು ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ಕಂಡುಹಿಡಿದು ಬಳಸಬಹುದು.
- **ಪ್ಲಗಿನ್‌ಗಳು ಮತ್ತು ಸಂಪರ್ಕಗಳು** - Microsoft Fabric, SharePoint, Pinecone ಮತ್ತು Qdrant ಮುಂತಾದ ಡೇಟಾ ಮತ್ತು ಮೆಮೊರಿ ಸೇವೆಗಳಿಗೆ ಸಂಪರ್ಕ ಸಿಗುತ್ತವೆ.

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಂಬರ್‌ಕ್ ಮುಖ್ಯ ತತ್ವಗಳಿಗೆ ಈ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಹೇಗೆ ಅನ್ವಯಿಸಲಾಗಿದೆ ಎಂದು ನೋಡೋಣ.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಂಬರ್‌ಕ್ ಪ್ರಮುಖ ತತ್ವಗಳು

### ಏಜೆಂಟ್‌ಗಳು

![Agent Framework](../../../translated_images/kn/agent-components.410a06daf87b4fef.webp)

**ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವುದು**

ಏಜೆಂಟ್ ರಚನೆ ಇಂಫರೆನ್ಸ್ ಸೇವೆ (LLM ಪ್ರೊವೈಡರ್), AI ಏಜೆಂಟ್ ಅನುಸರಿಸಬೇಕಾದ ನಿರ್ದೇಶನಗಳ ಸಮೂಹ, ಮತ್ತು ನಿಗದಿಪಡಿಸಿದ `name` ಗೆ ಕ್ರಮಿಸಲಾಗಿದೆ:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ಮೇಲಿನ ಕೋಡ್ `ಆಜ್ಯುರ್ ಓಪನ್ಏಐ` ಬಳಸುತ್ತಿದೆ ಆದರೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿಭಿನ್ನ ಸೇವೆಗಳ ಬಳಕೆ ಮಾಡಬಹುದು, ಉದಾಹರಣೆಗೆ `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIಗಳು

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ಅಥವಾ [MiniMax](https://platform.minimaxi.com/), ಆಗಿದೆ OpenAI-ಸಮಾನ ಎಪಿಐ with ದೊಡ್ಡ ಸನ್ನಿವೇಶ ವಿಂಡೋಗಳು (204K ಟೋಕನ್‌ಗಳವರೆಗೂ):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ಅಥವಾ ದೂರಸ್ಥ ಏಜೆಂಟ್‌ಗಳನ್ನು A2A ಪ್ರೋಟೊಕಾಲ್ ಬಳಸಿ:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ಏಜೆಂಟ್ ಚಲಾಯಿಸುವುದು**

ಏಜೆಂಟ್ ಗಳು `.run` ಅಥವಾ `.run_stream` ವಿಧಾನಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಸಿಬ್ಬಂದಿ ಅಥವಾ ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡಲಾಗುತ್ತದೆ.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ಪ್ರತಿಯೊಂದು ಏಜೆಂಟ್ ರನ್ ನಲ್ಲೂ `max_tokens` (ಏಜೆಂಟ್ ಬಳಸುವ), `tools` (ಏಜೆಂಟ್ ಕರೆಮಾಡಬಹುದಾದ ಉಪಕರಣಗಳು), ಮತ್ತು `model`(ಏಜೆಂಟ್ ಉಪಯೋಗಿಸುವ ಮಾದರಿ)ಗಳಂತಹ ಆಯ್ಕೆಗಳನ್ನು ಹೊಂದಬಹುದು.

ಇದು ಬಳಕೆದಾರನ ಕಾರ್ಯವನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ನಿರ್ದಿಷ್ಟ ಮಾದರಿಗಳು ಅಥವಾ ಉಪಕರಣಗಳು ಅಗತ್ಯವಾಗುವ ಸಂದರ್ಭಗಳಲ್ಲಿ ಉಪಯುಕ್ತ.

**ಉಪಕರಣಗಳು**

ಉಪಕರಣಗಳನ್ನು ಏಜೆಂಟ್ ರಚಿಸುವಾಗ ಅಥವಾ

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ನೇರವಾಗಿ ChatAgent ರಚಿಸುವಾಗ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ಏಜೆಂಟ್ ಚಲಾಯಿಸುವಾಗ ಕೂಡ ನಿರ್ಧರಿಸಬಹುದು:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ಈ ರನ್ ಗೆ ಮಾತ್ರ ಒದಗಿಸಲಾದ ಸಾಧನ )
```

**ಏಜೆಂಟ್ ಥ್ರೆಡ್‌ಗಳು**

ಏಜೆಂಟ್ ಥ್ರೆಡ್‌ಗಳು ಬಹು-ತಿರುವಿನ ಸಂಭಾಷಣೆಯನ್ನು ನಿರ್ವಹಿಸಲು ಬಳಸಲಾಗುತ್ತವೆ. ಥ್ರೆಡ್‌ಗಳು ರಚಿಸುವ ವಿಧಾನಗಳು:

- `get_new_thread()` ಬಳಸಿ ಥ್ರೆಡ್ ಅನ್ನು ಸಮಯದೊಂದಿಗೆ ಉಳಿಸುವುದಕ್ಕೆ ಸಾಧ್ಯತೆ ಇರುತ್ತದೆ
- ಏಜೆಂಟ್ ಓಟದ ಸಮಯದಲ್ಲಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಥ್ರೆಡ್ ರಚಿಸಿ ಮತ್ತು ಆ ಓಟದ ಕಾಲದಲ್ಲಿ ಮಾತ್ರ ಥ್ರೆಡ್ ಉಳಿಯುತ್ತದೆ.

ಥ್ರೆಡ್ ರಚಿಸಲು ಕೋಡ್ ಇವನ್ನು:

```python
# ಹೊಸ ಥ್ರೆಡ್ ಅನ್ನು ರಚಿಸಿ.
thread = agent.get_new_thread() # ಥ್ರೆಡ್‌ನೊಂದಿಗೆ ಏಜೆಂಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

ನಂತರ ನೀವು ಥ್ರೆಡ್ ಅನ್ನು ಶ್ರೇಣೀಕರಿಸಿ ಭವಿಷ್ಯದಲ್ಲಿ ಬಳಕೆಗೆ stೋರ್ ಮಾಡಬಹುದು:

```python
# ಹೊಸ ಥ್ರೆಡ್ ಸೃಷ್ಟಿಸಿ.
thread = agent.get_new_thread() 

# ಥ್ರೆಡ್‌ನೊಂದಿಗೆ ಏಜೆಂಟ್ ಅನ್ನು 실행ಿಸಿ.

response = await agent.run("Hello, how are you?", thread=thread) 

# ಸಂಗ್ರಹಣೆಗೆ ಥ್ರೆಡ್ ಅನ್ನು ಸರಣಿಗೊಳಿಸಿ.

serialized_thread = await thread.serialize() 

# ಸಂಗ್ರಹಣೆಯಿಂದ ಲೋಡ್ ಮಾಡಿದ ನಂತರ ಥ್ರೆಡ್ ಸ್ಥಿತಿಯನ್ನು ಅವಸರಗೊಳಿಸಿ.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ಏಜೆಂಟ್ ಮೀಡಿಯೇಲ್**

ಏಜೆಂಟ್‌ಗಳು ಉಪಕರಣಗಳು ಮತ್ತು LLMಗಳೊಂದಿಗೆ ಬಳಕೆದಾರ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ. ಕೆಲ ಸಂದರ್ಭಗಳಲ್ಲಿ ಈ ಇಂಟರೆಕ್ಷನ್‌ಗಳ ನಡುವೆ ಕಾರ್ಯಾನ್ವಯಿಸುವುದಕ್ಕೆ ಅಥವಾ ಟ್ರ್ಯಾಕ್ ಮಾಡಲು ಬಯಸುತ್ತೇವೆ. ಏಜೆಂಟ್ ಮೀಡಿಯೇಲ್ ಈ ಕಾರ್ಯಾಳಿ ಮಾಡಲು ಸಾದ್ಯಮಾಡುತ್ತದೆ:

*ಫಂಕ್ಷನ್ ಮೀಡಿಯೇಲ್*

ಈ ಮೀಡಿಯೇಲ್ ಏಜೆಂಟ್ ಮತ್ತು ಅದು ಕರೆಮಾಡುವ ಫಂಕ್ಷನ್/ಉಪಕರಣದ ನಡುವೆ ಒಂದು ಕ್ರಿಯೆಯನ್ನು ನಡೆಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ. ಉದಾಹರಣೆಗೆ ಫಂಕ್ಷನ್ ಕರೆ ಮೇಲೆ ಲಾಗಿಂಗ್ ಮಾಡಲು ಬಳಸಬಹುದು.

ಕೆಳಗಿನ ಕೋಡ್‌ನಲ್ಲಿ `next` ಅಂದರೆ ಮುಂದಿನ ಮೀಡಿಯೇಲ್ ಅಥವಾ ನಿಜವಾದ ಫಂಕ್ಷನ್ ಕರೆ ಮಾಡಬೇಕೆಂಬುದನ್ನು ನಿರ್ಧರಿಸುತ್ತದೆ.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ಪ್ರಿ-ಪ್ರೊಸೆಸಿಂಗ್: ಫಂಕ್ಷನ್ ಕಾರ್ಯಾಚರಣೆಯ ಮುಂಚೆ ಲಾಗ್ ಮಾಡು
    print(f"[Function] Calling {context.function.name}")

    # ಮುಂದಿನ ಮಿಡ್ಲ್ವೇರ್ ಅಥವಾ ಫಂಕ್ಷನ್ ಕಾರ್ಯಾಚರಣೆಗೆ ಮುಂದುವರೆಯಿರಿ
    await next(context)

    # ಪೋಸ್ಟ್-ಪ್ರೊಸೆಸಿಂಗ್: ಫಂಕ್ಷನ್ ಕಾರ್ಯಾಚರಣೆಯ ನಂತರ ಲಾಗ್ ಮಾಡು
    print(f"[Function] {context.function.name} completed")
```

*ಚಾಟ್ ಮೀಡಿಯೇಲ್*

ಈ ಮೀಡಿಯೇಲ್ ಏಜೆಂಟ್ ಹಾಗೂ LLMಗಳ ವಿನಂತಿಗಳ ನಡುವೆ ಕ್ರಿಯೆಯನ್ನು ನಡೆಸಲು ಅಥವಾ ಲಾಗ್ ಮಾಡಲು ಅನುಮತಿಸುತ್ತದೆ.

ಇದರಲ್ಲಿ AI ಸೇವೆಗೆ ಕಳುಹಿಸಲಾಗುತ್ತಿರುವ `messages` ಮುಂತಾದ ಪ್ರಮುಖ ಮಾಹಿತಿಗಳು ಇರುತ್ತವೆ.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ಪೂರ್ವಪ್ರಕ್ರಿಯೆ: AI ಕರೆಗೂಮುಗೂ ಮುಂಚೆ ಲಾಗ್ ಮಾಡು
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ಮುಂದಿನ ಮಧ್ಯಂತರ ಸೇವೆಗೆ ಅಥವಾ AI ಸೇವೆಗೆ ಮುಂದುವರಿಯಿರಿ
    await next(context)

    # ನಂತರದ ಪ್ರಕ್ರಿಯೆ: AI ಪ್ರತಿಕ್ರಿಯೆಯಿಂದ ನಂತರ ಲಾಗ್ ಮಾಡು
    print("[Chat] AI response received")

```

**ಏಜೆಂಟ್ ಮೆಮೊರಿ**

`Agentic Memory` ಪಾಠದಲ್ಲಿ ವಿವರಿಸಲಾದಂತೆ, ಮೆಮೊರಿ ವಿವಿಧ ಸನ್ನಿವೇಶಗಳಲ್ಲಿ ಏಜೆಂಟ್ ಕಾರ್ಯನಿರ್ವಹಿಸಲು ಪ್ರಮುಖ ಅಂಶವಾಗಿದೆ. MAF ಹಲವು ವಿಧದ ಮೆಮೊರಿಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ:

*ಇನ್-ಮೆಮೊರಿ ಸಂಗ್ರಹಣೆ*

ಅಪ್ಲಿಕೇಶನ್ ಸಮಯದಲ್ಲಿ ಥ್ರೆಡ್‌ಗಳಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾದ ಮೆಮೊರಿ.

```python
# ಹೊಸ ಥ್ರೆಡ್ ರಚಿಸಿ.
thread = agent.get_new_thread() # ಆ ಥ್ರೆಡ್‌ನೊಂದಿಗೆ ಏಜೆಂಟ್ ಅನ್ನು ರನ್ ಮಾಡಿ.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*ದೃಢವಾದ ಸಂದೇಶಗಳು*

ವಿವಿಧ ಅಧಿವೇಶನಗಳ ನಡುವೆ ಸಂಭಾಷಣಾ ಇತಿಹಾಸವನ್ನು ಸಂಗ್ರಹಿಸುವ ಸಲುವಾಗಿ ಬಳಸುವ ಮೆಮೊರಿ. ಇದನ್ನು `chat_message_store_factory` ಉಪಯೋಗಿಸಿ ವ್ಯಾಖ್ಯಾನಿಸಲಾಗುತ್ತದೆ:

```python
from agent_framework import ChatMessageStore

# ಕಸ್ಟಮ್ ಸಂದೇಶ ಸಂಗ್ರಹಣೆ ರಚಿಸಿ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ಡೈನಾಮಿಕ್ ಮೆಮೊರಿ*

ಏಜೆಂಟ್‌ಗಳನ್ನು ಚಲಾಯಿಸುವ ಮುನ್ನ ಸನ್ನಿವೇಶಕ್ಕೆ ಸೇರಿಸಲಾಗುವ ಮೆಮೊರಿ. ಈ ಮೆಮೊರಿಗಳನ್ನು mem0 ಮುಂತಾದ ಬಾಹ್ಯ ಸೇವೆಗಳಲ್ಲಿ ಸಂಗ್ರಹಿಸಬಹುದು:

```python
from agent_framework.mem0 import Mem0Provider

# ಸುಧಾರಿತ ಮೆಮೊರಿ ಸಾಮರ್ಥ್ಯಗಳಿಗಾಗಿ Mem0 ಅನ್ನು ಬಳಸಲಾಗಿದೆ
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

**ಏಜೆಂಟ್ ಅವಲೋಕನ ಸಾಮರ್ಥ್ಯ**


ನಿಗದಿತ ಮತ್ತು ನಿರ್ವಹಣೆ-ಸಾಧ್ಯ ಏಜೆಂಟಿಕ್ ಸಿಸ್ಟಂಗಳನ್ನು ನಿರ್ಮಿಸುವುದಕ್ಕೆ ನಿರೀಕ್ಷಣೆಯು ಪ್ರಮುಖವಾಗಿದೆ. ಉತ್ತಮ ನಿರೀಕ್ಷಣೆಗೆ ಗಮನಾ ಮತ್ತು ಮೀಟರ್ಗಳಿಗಾಗಿ MAF OpenTelemetry ಜೊತೆಗೆ ಸಂಯೋಜಿಸುತ್ತದೆ.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ಏನಾದರೂ ಮಾಡಿ
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### ಕಾರ್ಯಪ್ರವಾಹಗಳು

MAF ಪೂರ್ವನಿರ್ಧಾರಿತ ಹಂತಗಳಾಗಿ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ನೀಡುತ್ತದೆ, ಅವು ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ಮತ್ತು ಆ ಹಂತಗಳಲ್ಲಿ AI ಏಜೆಂಟ್ಗಳನ್ನು ಘಟಕಗಳಾಗಿ ಒಳಗೊಂಡಿವೆ.

ಕಾರ್ಯಪ್ರವಾಹಗಳು ಉತ್ತಮ ಕಂಟ್ರೋಲ್ ಫ್ಲೋ ಮಾಡಲು ವಿಭಿನ್ನ ಘಟಕಗಳಿಂದ ನಿರ್ಮಿಸಲ್ಪಟಿವೆ. ಕಾರ್ಯಪ್ರವಾಹಗಳು **ಬಹು ಏಜೆಂಟ್ ಸಂಯೋಜನೆ** ಮತ್ತು ಕಾರ್ಯಪ್ರವಾಹ ಸ್ಥಿತಿಗಳನ್ನು ಉಳಿಸುವ **ಚೆಕ್‌ಪಾಯಿಂಟಿಂಗ್** ಅನ್ನು ಸಹ ಸಬಲಿ ಮಾಡುತ್ತದೆ.

ಕಾರ್ಯಪ್ರವಾಹದ ಮುಖ್ಯ ಘಟಕಗಳು:

**ನಿರ್ವಹಕರು**

ನಿರ್ವಹಕರು ಇನ್‌ಪುಟ್ ಸಂದೇಶಗಳನ್ನು ಸ್ವೀಕರಿಸಿ, ನಿಯೋಜಿತ ಕಾರ್ಯಗಳನ್ನು ನೆರವೇರಿಸಿ, ನಂತರ ಒಂದು ಔಟ್ಪುಟ್ ಸಂದೇಶವನ್ನು ಉತ್ಪಾದಿಸುತ್ತಾರೆ. ಇದು ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ದೊಡ್ಡ ಕಾರ್ಯವನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ಮುಂದುವರಿಸುವಂತೆ ಮಾಡುತ್ತದೆ. ನಿರ್ವಹಕರು AI ಏಜೆಂಟಾಗಿರಬಹುದು ಅಥವಾ ಕಸ್ಟಮ್ ಲಾಜಿಕ್ ಆಗಿರಬಹುದು.

**ಎಡ್ಜ್‌ಗಳು**

ಕಾರ್ಯಪ್ರವಾಹದಲ್ಲಿ ಸಂದೇಶಗಳ ಹಾದಿಯನ್ನು ನಿರ್ಧರಿಸಲು ಎಡ್ಜ್‌ಗಳನ್ನು ಬಳಸಲಾಗುತ್ತದೆ. ಇವು:

*ನೇರ ಎಡ್ಜ್‌ಗಳು* - ನಿರ್ವಹಕರ ನಡುವೆ ಸರಳ ಒಬ್ಬರೋಬ್ಬರ ಸಂಪರ್ಕಗಳು:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*ಶರತಿದ್ದ ಎಡ್ಜ್‌ಗಳು* - ನಿರ್ದಿಷ್ಟ ಶರತನ್ನು ಪೂರೈಸಿದ ನಂತರ ಸಕ್ರಿಯಗೊಳ್ಳುತ್ತವೆ. ಉದಾಹರಣೆಗೆ, ಹೋಟೆಲ್ ಕೊಠಡಿಗಳು ಲಭ್ಯವಿಲ್ಲದಿದ್ದಾಗ, ನಿರ್ವಹಕರು ಇತರ ಆಯ್ಕೆಯನ್ನು ಸೂಚಿಸಬಹುದು.

*ಸ್ವಿಚ್-ಕೆಸ್ ಎಡ್ಜ್‌ಗಳು* - ನಿರ್ಧರಿತ ಷರತ್ತುಗಳ ಆಧಾರದಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ವಿಭಿನ್ನ ನಿರ್ವಹಕರಿಗೆ ಹಾದು ಮಾಡುತ್ತದೆ. ಉದಾಹರಣೆಗೆ, ಪ್ರಯಾಣ ಗ್ರಾಹಕರು ಪ್ರಾಮುಖ್ಯತೆಯ ಪ್ರವೇಶ ಹೊಂದಿದ್ದರೆ, ಅವರ ಕಾರ್ಯಗಳನ್ನು ಇನ್ನೊಬ್ಬ ಕಾರ್ಯಪ್ರವಾಹದಲ್ಲಿ ನಿಭಾಯಿಸಲಾಗುತ್ತದೆ.

*ಫ್ಯಾನ್-ಔಟ್ ಎಡ್ಜ್‌ಗಳು* - ಒಂದೇ ಸಂದೇಶವನ್ನು ಬಹು ಗುರಿಗಳಿಗೆ ಕಳುಹಿಸುತ್ತದೆ.

*ಫ್ಯಾನ್-ಇನ್ ಎಡ್ಜ್‌ಗಳು* - ವಿಭಿನ್ನ ನಿರ್ವಹಕರಿಂದ ಬಹು ಸಂದೇಶಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ ಒಂದೇ ಗುರಿಗೆ ಕಳುಹಿಸುತ್ತದೆ.

**ಕೃತಿಗಳು**

ಕಾರ್ಯಪ್ರವಾಹಗಳ ಪರಿಣಾಮಕಾರಿತ್ವವನ್ನು ಉತ್ತಮವಾಗಿ ತೋರಿಸಲು, MAF ಕಾರ್ಯನಿರ್ವಹಣೆಗೆ ಕಟ್ಟಿಕೊಂಡಿರುವ ಕೃತಿಗಳನ್ನು ನೀಡುತ್ತದೆ, ಅವುಗಳಲ್ಲಿ:

- `WorkflowStartedEvent`  - ಕಾರ್ಯಪ್ರವಾಹ ಕಾರ್ಯಾರಂಭ
- `WorkflowOutputEvent` - ಕಾರ್ಯಪ್ರವಾಹ ಔಟ್ಪುಟ್ ನೀಡುತ್ತದೆ
- `WorkflowErrorEvent` - ಕಾರ್ಯಪ್ರವಾಹದಲ್ಲಿ ದೋಷ ಸಂಭವಿಸುತ್ತದೆ
- `ExecutorInvokeEvent`  - ನಿರ್ವಹಕರು ಕಾರ್ಯ ಪ್ರಾರಂಭಿಸುತ್ತಾರೆ
- `ExecutorCompleteEvent`  -  ನಿರ್ವಹಕರು ಕಾರ್ಯ ಮುಗಿಸುತ್ತಾರೆ
- `RequestInfoEvent` - ವಿನಂತಿ ನೀಡಲ್ಪಡುತ್ತದೆ

## ಅಭಿವೃದ್ಧಿಯಾದ MAF ಮಾದರಿಗಳು

ಮೇಲಿನ ವಿಭಾಗಗಳು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ ಮುಖ್ಯ ಕಲ್ಪನೆಗಳನ್ನು ಕೈಗೊಂಡಿವೆ. ನೀವು ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಏಜೆಂಟ್ಗಳನ್ನು ನಿರ್ಮಿಸಿಕೊಂಡಾಗ, ಗಮನಿಸಲು ಕೆಲವು ಉತ್ತಮ ಮಾದರಿಗಳು:

- **ಮಧ್ಯಸ್ಥ ವಾಸ್ತುಶಿಲ್ಪ**: ಲಾಗಿಂಗ್, ಪ್ರಾಧಿಕಾರ, ದರ-ನಿಯಂತ್ರಣವಾದMiddleware ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು ಸರಪಳಿ ಮಾಡಿ ಏಜೆಂಟ್ ಬಿಹೇವಿಯರ್ನಲ್ಲಿ ಸೂಕ್ಷ್ಮ ನಿಯಂತ್ರಣಕ್ಕಾಗಿ ಫಂಕ್ಷನ್ ಮತ್ತು ಚಾಟ್ Middleware ಬಳಸಿ.
- **ಕಾರ್ಯಪ್ರವಾಹ ಚೆಕ್‌ಪಾಯಿಂಟಿಂಗ್**: ಕಾರ್ಯಪ್ರವಾಹ ಕೃತಿಗಳನ್ನು ಮತ್ತು ಸರಣಿಬದ್ಧತೆ ಬಳಸಿ ದೀರ್ಘಕಾಲ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಏಜೆಂಟ್ ಪ್ರಕ್ರಿಯೆಗಳನ್ನು ಉಳಿಸಿ ಮತ್ತು ಪುನರುಸ್ಥಾಪಿಸಿ.
- **ಡೈನಾಮಿಕ್ ಉಪಕರಣ ಆಯ್ಕೆ**: RAG ಉಪಕರಣ ವಿವರಣೆಯ ಮೇಲೆ MAF ಯಾದು ಉಪಕರಣ ನೋಂದಣಿಯನ್ನು ಸಂಯೋಜಿಸಿ ಪ್ರತಿ ಪ್ರಶ್ನೆಗೆ ಮಾತ್ರ ಸಂಬಂಧಿಸಿದ ಉಪಕರಣಗಳನ್ನು ಪ್ರದರ್ಶಿಸಿ.
- **ಬಹು ಏಜೆಂಟ್ ಹ್ಯಾಂಡ್‌ಆಫ್**: ಕಾರ್ಯಪ್ರವಾಹ ಎಡ್ಜ್‌ಗಳು ಮತ್ತು ಶರತಂಜಾಲಿತ ಮಾರ್ಗದರ್ಶನ ಬಳಸಿ ವಿಶೇಷ ಏಜೆಂಟ್‌ಗಳ ನಡುವೆ ಹ್ಯಾಂಡ್‌ಆಫ್ ಅನ್ನು ವ್ಯವಸ್ಥೆ ಮಾಡಿ.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ ಲಾಂಗ್‌ಚೈನ್ / ಲಾಂಗ್‌ಗ್ರಾಫ್ ಏಜೆಂಟ್‌ಗಳನ್ನು ಹೋಸ್ಟ್ ಮಾಡುವುದು

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ **ಫ್ರೇಮ್‌ವರ್ಕ್-ಅಂತರಚಾಲಕ** ಆಗಿದೆ — ನೀವು ಕೇವಲ MAF ಬಳಸಿ ಬರೆದ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸೀಮಿತವಿಲ್ಲ. ನೀವು ಈಗಾಗಲೇ **ಲಾಂಗ್‌ಚೈನ್** ಅಥವಾ **ಲಾಂಗ್‌ಗ್ರಾಫ್** ಬಳಸಿ ಏಜೆಂಟ್ ರಚಿಸಿರುವಿದ್ದರೆ, ಅದನ್ನು **ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಹೋಸ್ಟ್ ಮಾಡಿದ ಏಜೆಂಟ್**ಆಗಿಂಡೆ ಓಡಿಸಬಹುದು. ಇದರಿಂದ ಫೌಂಡ್ರಿ ರಂಟೈಮ್, ಸೆಷನ್‌ಗಳು, ವ್ಯಾಪ್ತಿ, ಐಡೆಂಟಿಟಿ ಮತ್ತು ಪ್ರೋಟೋಕಾಲ್ ಎಂಡ್‌ಪುಂಟ್ಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಏಜೆಂಟ್ ಲಾಜಿಕ್ ಲಾಂಗ್‌ಗ್ರಾಫ್‌ನಲ್ಲಿ ಉಳಿಯುತ್ತದೆ.

ಇದು `langchain_azure_ai.agents.hosting` ಪ್ಯಾಕೇಜ್ ಮೂಲಕ ನೆರವೇರಿಸಲಾಗಿದೆ, ಇದು ಫೌಂಡ್ರಿ ಹೋಸ್ಟ್ ಏಜೆಂಟ್‌ಗಳು ಬಳಸುವ ಅದೇ ಪ್ರೋಟೋಕಾಲ್‌ಗಳ ಮೇಲೆ ಸಂಯೋಜಿತ ಲಾಂಗ್‌ಗ್ರಾಫ್ ಗ್ರಾಫ್ ಅನ್ನು ಹೊರತೆಗೆಯುತ್ತದೆ.

**1. ಹೋಸ್ಟಿಂಗ್ ಎಕ್ಸ್ಟ್ರಾ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ಎಕ್ಸ್ಟ್ರಾ ಫೌಂಡ್ರಿ ಪ್ರೋಟೋಕಾಲ್ ಲೈಸಬ್ರರಿಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡುತ್ತದೆ: `azure-ai-agentserver-responses` (OpenAI-ಅನುಕೂಲ ವಾರ್ತಾ `/responses` ಎಂಡ್‌ಪುಂಟ್) ಮತ್ತು `azure-ai-agentserver-invocations` (ಸಾಮಾನ್ಯ `/invocations` ಎಂಡ್‌ಪುಂಟ್).

**2. ಹೋಸ್ಟಿಂಗ್ ಪ್ರೋಟೋಕಾಲ್ ಆಯ್ಕೆಮಾಡಿ:**

| ಪ್ರೋಟೋಕಾಲ್ | ಹೋಸ್ಟ್ ಕ್ಲಾಸ್ | ಎಂಡ್‌ಪುಂಟ್ | ಯಾವಾಗ ಬಳಸುವುದು |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | ನೀವು OpenAI ಅನುಕೂಲ ಚಾಟ್, ಸ್ಟ್ರೀಮಿಂಗ್, ಪ್ರತಿಕ್ರಿಯೆ ಇತಿಹಾಸ ಮತ್ತು ಸಂಭಾಷಣಾ ಎಂಟ್ರಾಡಿ ಬೇಕಾಗಿರುವಾಗ — ಕಾನ್ಸರ್ವೇಶನಲ್ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಶಿಫಾರಸು ಮಾಡಿದ ಡೀಫಾಲ್ಟ್. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | ನೀವು ಕಸ್ಟಮ್ JSON ಆಕಾರ, webhook ಶೈಲಿ ಎಂಡ್‌ಪುಂಟ್ ಅಥವಾ ಅಕಾನ್ಸರ್ವೇಶನಲ್ ಪ್ರಕ್ರಿಯೆ ಬೇಕಾಗಿರುವಾಗ. |

ಫೌಂಡ್ರಿಯಲ್ಲಿ **ಏಜೆಂಟ್ ಶೈಲಿ ಅಭಿವೃದ್ಧಿಗೆ Responses API ಪ್ರಾಥಮಿಕ API ಆಗಿದೆ**, ಬಹುತೇಕ ಏಜೆಂಟ್‌ಗಳಿಗೆ `ResponsesHostServer` ಯಿಂದ ಪ್ರಾರಂಭಿಸಿ.

**3. ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಸಂರಚಿಸಿ** (`az login` ಮೊದಲು ಮಾಡಿ `DefaultAzureCredential` ನು ದೃಢೀಕರಿಸಬಹುದು):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

ಏಜೆಂಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಆಗಿ ನಂತರ ಕಾರ್ಯನಿರ್ವಹಿಸಿದಾಗ, ವೇದಿಕೆ `FOUNDRY_PROJECT_ENDPOINT` ಅನ್ನು ತಮ್ಮಿಂದ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸೇರಿಸುತ್ತದೆ.

**4. ಲಾಂಗ್‌ಗ್ರಾಫ್ ಏಜೆಂಟ್ ಅನ್ನು Responses ಪ್ರೋಟೋಕಾಲ್ ಮೇಲೆ ಬಹಿರ್ಗತಗೊಳಿಸಿ:**

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI ಇಲ್ಲಿ Foundry ಪ್ರಾಜೆಕ್ಟಿನ OpenAI-ಸಮ್ಮತಿತ (ಪ್ರತ್ಯುತ್ತರಗಳು) ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಗುರಿಯಾಗಿಸಿದೆ.
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

ಅದನ್ನು ಸ್ಥಳೀಯವಾಗಿ `python main.py` ಮೂಲಕ ಓಡಿಸಿ, ನಂತರ `http://localhost:8088/responses` ಗೆ Responses ವಿನಂತಿಯನ್ನು ಕಳುಹಿಸಿ.

**ಮುಖ್ಯ ಆಚಾರಗಳು:**

- **ಸಂಭಾಷಣೆಗಳು**: ಗ್ರಾಹಕರು `previous_response_id` ಅಥವಾ `conversation` ID ನೀಡುವ ಮೂಲಕ ಸಂಭಾಷಣೆಯನ್ನು ಮುಂದುವರಿಸುತ್ತಾರೆ. ನಿಮ್ಮ ಗ್ರಾಫ್ ಲಾಂಗ್‌ಗ್ರಾಫ್ ಚೆಕ್‌ಪಾಯಿಂಟರ್‌ನೊಂದಿಗೆ ಸಂಯೋಜಿತವಾದರೆ, ಫೌಂಡ್ರಿ ಸಂಭಾಷಣ ಸ್ಥಿತಿಯನ್ನು ಚೆಕ್‌ಪಾಯಿಂಟ್ ಗೆ ಕೀ ಮಾಡುತ್ತದೆ ( ಉತ್ಪಾದನೆಯಲ್ಲಿ ದೈರಘ್ಯ ಚೆಕ್‌ಪಾಯಿಂಟರ್ ಬಳಸಿ; ಸ್ಥಳೀಯ ಪರೀಕ್ಷೆಗೆ `MemorySaver` ಸೂಕ್ತ).
- **ಮನುಷ್ಯ ನಿರ್ವಹಣೆಯಲ್ಲಿ**: ನಿಮ್ಮ ಗ್ರಾಫ್ ಲಾಂಗ್‌ಗ್ರಾಫ್ `interrupt()` ಅನ್ನು ಉಪಯೋಗಿಸಿದರೆ, `ResponsesHostServer` ಬಾಕಿ ಇರುವ ಅಂತರವನ್ನು Responses `function_call` / `mcp_approval_request`  ಐಟಂ ಆಗಿ ತೋರಿಸುತ್ತದೆ ಮತ್ತು ಗ್ರಾಹಕರು ಹೊಂದಿಕೊಳ್ಳುವ `function_call_output` / `mcp_approval_response` ಮೂಲಕ ಪುನರೂತ್ಥಾನ ಮಾಡುತ್ತಾರೆ.
- **ಫೌಂಡ್ರಿಗೆ ನಿಯೋಜನೆ**: ಅಜೂರ್ ಡೆವಲಪರ್ CLI ಬಳಸಿ — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ಸ್ಥಳೀಯ, ಡೋಕರ್ ಅಗತ್ಯವಿದೆ), ನಂತರ `azd provision` ಮತ್ತು `azd deploy`. ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ನಿಯೋಜನೆಗೆ **Foundry Project Manager** ಪಾತ್ರ ಅಗತ್ಯ.

ಈ ಉದಾಹರಣೆಯ ಚಾಲನೆಯಾದ সংস্কರಣೆ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ನಲ್ಲಿ ಲಭ್ಯವಿದೆ. ಸಂಪೂರ್ಣ ಸಂಚಲನಕ್ಕಾಗಿ (Invocations ಪ್ರೋಟೋಕಾಲ್, ಕಸ್ಟಮ್ ವಿನಂತಿchemaಗಳು, ಮತ್ತು ಸಮಸ್ಯೆ ಪರಿಹಾರ) ನೋಡಿ [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## ಕೋಡ್ ಉದಾಹರಣೆಗಳು

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗೆ ಸಂಬಂಧಿಸಿದ ಕೋಡ್ ಉದಾಹರಣೆಗಳು ಈ ರೆಪೊಸಿಟರಿಗೆಲ್ಲಿದೆ `xx-python-agent-framework` ಮತ್ತು `xx-dotnet-agent-framework` ಕಡತಗಳಡಿಯಲ್ಲಿ.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿದ್ದರೆ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ನಲ್ಲಿ ಸೇರಿಕೊಳ್ಳಿ, ಇತರ ಕಲಿಕೆಯವರನ್ನು ಭೇಟಿ ಮಾಡಿ, ಆಫೀಸ್ ಘಂಟೆಗಳಲ್ಲಿ ಹಾಜರಾಗಿರಿ ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಗಳನ್ನು ಪಡೆಯಿರಿ.
## ಹಿಂದಿನ ಪಾಠ

[AI ಏಜೆಂಟ್‌ಗಳಿಗಾಗಿ ಮೆಮೊರಿ](../13-agent-memory/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಕಂಪ್ಯೂಟರ್ ಬಳಕೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->