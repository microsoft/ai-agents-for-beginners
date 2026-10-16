# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮುರ್ಕ್ ಅನ್ವೇಷಣೆ

![Agent Framework](../../../translated_images/kn/lesson-14-thumbnail.90df0065b9d234ee.webp)

### ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ನೀವು ತಿಳಿದುಕೊಳ್ಳಲಿರುವುದು:

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮುರ್ಕ್ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು: ಮುಖ್ಯ ವೈಶಿಷ್ಟ್ಯಗಳು ಮತ್ತು ಮೌಲ್ಯ  
- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮುರ್ಕ್‌ನ ಪ್ರಮುಖ ಕಲ್ಪನೆಗಳನ್ನು ಅನ್ವೇಷಣೆ
- ಉನ್ನತ MAF ಮಾದರಿಗಳು: ವರ್ಕ್‌ಫ್ಲೋಗಳು, ಮಿಡ್‌ಲ್‌ವೇರ್ ಮತ್ತು ಮೆಮೊರಿ

## ಅಧ್ಯಯನ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಹೇಗೆ ಎಂಬುದನ್ನು ತಿಳಿದುಕೊಳ್ಳುತ್ತೀರಿ:

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮುರ್ಕ್ ಬಳಸಿ ಉತ್ಪಾದನೆಗಾಗಿ ತಯಾರಾದ AI ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಿಸುವುದು
- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮುರ್ಕ್‌ನ ಮೂಲ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ನಿಮ್ಮ ಏಜೆಂಟಿಕ್ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಗೆ ಅನ್ವಯಿಸುವುದು
- ವರ್ಕ್‌ಫ್ಲೋಗಳು, ಮಿಡ್‌ಲ್‌ವೇರ್ ಮತ್ತು ಪರಿವೀಕ್ಷಣೆಯನ್ನು ಒಳಗೊಂಡ ಉನ್ನತ ಮಾದರಿಗಳನ್ನು ಬಳಸುವುದು

## ಕೋಡ್ ಮಾದರಿಗಳು 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)ನ ಕೋಡ್ ಮಾದರಿಗಳು ಈ ರೆಪೊಸಿಟರಿಯಲ್ಲಿ `xx-python-agent-framework` ಮತ್ತು `xx-dotnet-agent-framework` ಕಡತಗಳ ಹಂತದಲ್ಲಿ ದೊರೆಯಬಹುದು.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮುರ್ಕ್ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು

![Framework Intro](../../../translated_images/kn/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ಮೈಕ್ರೋಸಾಫ್ಟ್‌ನ ಏಐ ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಿಸಲು ಏಕೀಕೃತ ಫ್ರೇಮುರ್ಕ್ ಆಗಿದೆ. ಇದು ಉತ್ಪಾದನೆ ಮತ್ತು ಸಂಶೋಧನೆಯ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಕಾಣುವ ವೈವಿಧ್ಯಮಯ ಏಜೆಂಟಿಕ್ ಬಳಕೆ ಪ್ರಕರಣಗಳನ್ನು ಪೂರೈಸಲು ಲವಚಿಕತೆ ನೀಡುತ್ತದೆ, ಅವುಗಳಲ್ಲಿ:

-  ಕ್ರಮಬದ್ಧ ಏಜೆಂಟ್ ಸಂಕಲನವು ಕ್ರಮಾಗಿ ತನಿಖೆಗಳ ಅಗತ್ಯವಿರುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.
-  ಸಮಕಾಲೀನ ಸಂಕಲನವು ಏಜೆಂಟ್ಸ್ ಜೊತೆಗೆ ಒಂದೇ ಸಮಯದಲ್ಲಿ ಕಾರ್ಯಗಳನ್ನು ಮುಗಿಸಲು ಅಗತ್ಯವಿರುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.
-  ಗುಂಪು ಚಾಟ್ ಸಂಕಲನವು ಏಜೆಂಟ್ಸ್ ಒಂದೇ ಕಾರ್ಯದಲ್ಲಿ ಒಟ್ಟಾಗಿ ಸಹಕರಿಸುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.
-  ಹ್ಯಾಂಡ್‌ಆಫ್ ಸಂಕಲನವು ಸಬ್ಟಾಸ್ಕ್ಗಳ ಮುಗಿದಾಗ ಏಜೆಂಟ್ಸ್ ಕಾರ್ಯವನ್ನು ಪರಸ್ಪರ ಹಸ್ತಾಂತರಿಸುವ ಸಂದರ್ಭಗಳಲ್ಲಿ.
-  ಮಾಗ್ನೆಟಿಕ್ ಸಂಕಲನವು ನಿರ್ವಾಹಕ ಏಜೆಂಟ್ ಕಾರ್ಯಪಟ್ಟಿಯನ್ನು ರಚಿಸುವುದು ಮತ್ತು ಅವು ಸಬ್ಏಜೆಂಟ್ಗಳ ಸಂಯೋಜನೆಗೆ ಸಮನ್ವಯಪಡಿಸುವುದನ್ನು ಕೈಗಾರಿಕೆಗೆ ಕೊಡುತ್ತದೆ.

ಉತ್ಪಾದನೆಯಲ್ಲಿ AI ಏಜೆಂಟ್ಸ್ ನೀಡಲು, MAF ಇವುಗಳ ಜೊತೆಗೆ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಒಳಗೊಂಡಿದೆ:

-  OpenTelemetry ಬಳಸಿ ಪರಿವೀಕ್ಷಣೆ, ಏಐ ಏಜೆಂಟ್ ಪ್ರತಿ ಕ್ರಿಯೆಗಳನ್ನು ಟೂಲ್ಸ್ ಕರೆಯುವುದು, ಸಂಕಲನ ಹಂತಗಳು, ತಾರ್ಕಿಕ ಹರಿವುಗಳು ಮತ್ತು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್‌ಗಳ ಮೂಲಕ ಕಾರ್ಯ ನಿರ್ವಹಣೆ ಮೇಲ್ವಿಚಾರಣೆ.
-  ಭದ್ರತೆ, ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ ನೇಟಿವ್ ಆಗಿ ಏಜೆಂಟ್ಸ್ ಹೊಂದಿಸುವುದು, ಪಾತ್ರ ಆಧಾರಿತ ಪ್ರವೇಶ, ಖಾಸಗಿ ಮಾಹಿತಿ ನಿರ್ವಹಣೆ ಮತ್ತು ನವೀನ ವಿಷಯ ಭದ್ರತೆ ಅಂಗಳಗಳಿಂದ ಸುರಕ್ಷತೆ ನಿಯಂತ್ರಣಗಳು.
-  ಸ್ಥಿರತೆ, ಏಜೆಂಟ್ ಥ್ರೆಡ್‌ಗಳು ಮತ್ತು ವರ್ಕ್‌ಫ್ಲೋಗಳು ನಿಲ್ಲಿಸುವುದು, ಪುನರಾರಂಭ ಮಾಡುವ ಮೂಲಕ ದೋಷಗಳಿಂದ ಪೂರೈಸುತ್ತವೆ, ಇದು ದೀರ್ಘಕಾಲीन ಪ್ರಕ್ರಿಯೆಗಳಿಗೆ ಅನುಕೂಲ.
-  ನಿಯಂತ್ರಣ, ಮಾನವ ಒಳಗಿತ ಪ್ರಕ್ರಿಯೆಗಳು ಬೆಂಬಲಿಸುವುದು, ಕಾರ್ಯಗಳನ್ನು ಮಾನವ ಅನುಮೋದನೆ ಅಗತ್ಯವಿರುತ್ತದೆ ಎಂದು ಗುರುತಿಸುವುದು.

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮುರ್ಕ್ ಹೊಂದಿರುವ ಇನ್ನೊಂದು ವೈಶಿಷ್ಟ್ಯವೆಂದರೆ ಅವುಗಳ ಮಧ್ಯೆ ಪರಸ್ಪರ ಕಾರ್ಯನಿರ್ವಹಣೆ:

-  ಕ್ಲೌಡ್-ನಿರಪೇಕ್ಷವಾಗಿರುವುದು - ಏಜೆಂಟ್ಗಳು ಕಂಟೇನರ್ಸ್, ಆನ್-ಪ್ರೇಮ್ ಹಾಗೂ ವಿವಿಧ ಕ್ಲೌಡ್ಗಳಲ್ಲಿ ಚಲಿಸಲು ಸಾಧ್ಯ.
-  ಪ್ರೊವೈಡರ್-ನಿರಪೇಕ್ಷವಾಗಿರುವುದು - ನಿಮ್ಮ ಇಚ್ಛಿತ SDK ಬಳಸಿ ಏಜೆಂಟ್ಗಳನ್ನು ರಚಿಸಬಹುದು, ಅದರಲ್ಲಿ Azure OpenAI ಮತ್ತು OpenAI ಸೇರಿವೆ.
-  ತೆರೆಯಲಾದ ಮಾದರಿಗಳನ್ನು ಸಂಯೋಜಿಸುವುದು - ಏಜೆಂಟ್ಗಳು Agent-to-Agent(A2A) ಮತ್ತು Model Context Protocol (MCP) ಹೂಡಿಕೆಗಳಿಂದ ಇತರ ಏಜೆಂಟ್ಗಳು ಮತ್ತು ಟೂಲ್ಗಳನ್ನು ಪತ್ತೆಮಾಡಿ ಬಳಕೆ ಮಾಡುವಂತೆ.
-  ಪ್ಲಗಿನ್‌ಗಳು ಮತ್ತು ಕನೆಕ್ಟರ್‌ಗಳು - ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫ್ಯಾಬ್ರಿಕ್, ಶೇರ್‌ಪಾಯಿಂಟ್, ಪೈನ್ಕೋನ್ ಮತ್ತು ಕ್ಯೂಡ್ರಾಂಟ್ ಮುಂತಾದ ಡೇಟಾ ಮತ್ತು ಮೆಮೊರಿ ಸೇವೆಗಳಿಗೆ ಸಂಪರ್ಕಗಳನ್ನು ಮಾಡಬಹುದು.

ಈ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮುರ್ಕ್‌ನ ಕೆಲವು ಮೂಲ ಕಲ್ಪನೆಗಳಿಗೆ ಹೇಗೆ ಅನ್ವಯಿಸಲಾಗುತ್ತದೆ ಎಂಬುದಕ್ಕೆ ನೋಡೋಣ.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮುರ್ಕ್‌ನ ಪ್ರಮುಖ ಕಲ್ಪನೆಗಳು

### ಏಜೆಂಟ್ಗಳು

![Agent Framework](../../../translated_images/kn/agent-components.410a06daf87b4fef.webp)

**ಏಜೆಂಟ್ಗಳ ರಚನೆ**

ಏಜೆಂಟ್ ರಚನೆ ಸ್ನಾಕ್ಷೋಪ ನಿರ್ದೇಶನ ಸೇವೆ (LLM ಪ್ರೊವೈಡರ್), AI ಏಜೆಂಟ್ ಅನುಸರಿಸಬೇಕಾದ ಸೂಚನೆಗಳ ಸರಣಿ, ಮತ್ತು ನಿಯೋಜಿಸಲಾದ `name` ನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವ ಮೂಲಕ ಮಾಡಲಾಗುತ್ತದೆ:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ಮೇಲಿನ ಉದಾಹರಣೆಯಲ್ಲಿ `Azure OpenAI` ಬಳಕೆಯಾಗಿದೆ ಆದರೆ ವಿಭಿನ್ನ ಸೇವೆಗಳೊಂದಿಗೆ ಏಜೆಂಟ್ಗಳನ್ನು ರಚಿಸುವುದು ಸಾಧ್ಯ, ಉದಾಹರಣೆಗೆ `Microsoft Foundry Agent Service`:

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

ಅಥವಾ [MiniMax](https://platform.minimaxi.com/), ಇದು OpenAI-ಅನುರೂಪ API ಅನ್ನು ದೊಡ್ಡ ಸಂದರ್ಬ ವಿಂಡೋಗಳೊಂದಿಗೆ (204K ಟೋಕನ್ಗಳು ವರೆಗೆ) ಒದಗಿಸುತ್ತದೆ:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ಅಥವಾ A2A ಪ್ರೊಟೋಕಾಲ್ ಬಳಸಿ ದೂರಸ್ಥ ಏಜೆಂಟ್ಗಳು:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ಏಜೆಂಟ್ಗಳ ಚಾಲನೆ**

ಏಜೆಂಟ್ಗಳನ್ನು `.run` ಅಥವಾ `.run_stream` ವಿಧಾನಗಳನ್ನು non-streaming ಅಥವಾ streaming ಪ್ರತಿಕ್ರಿಯೆಗಳಿಗೆ ಬಳಸುತ್ತಾರೆ.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ಪ್ರತಿ ಏಜೆಂಟ್ ಚಾಲನೆಯೂ ಆಯ್ಕೆಗಳನ್ನು ಹೊಂದಬಹುದು, ಉದಾ., ಏಜೆಂಟ್ ಬಳಸುವ `max_tokens`, ಏಜೆಂಟ್ ಕರೆ ಮಾಡಲು ಸಾಧ್ಯವಿರುವ `tools`, ಮತ್ತು ನೀವು ಬಳಸುತ್ತಿರುವ `model` ಸಹ ಸಮಾವೇಶ.

ಇದು ಬಳಕೆದಾರನ ಕಾರ್ಯವನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ವಿಶೇಷ ಮಾದರಿಗಳು ಅಥವಾ ಉಪಕರಣಗಳ ಅಗತ್ಯ ಇದ್ದಲ್ಲಿ ಉಪಯುಕ್ತ.

**ಟೂಲ್ಗಳು**

ಟೂಲ್ಗಳನ್ನು ಏಜೆಂಟ್ ವ್ಯಾಖ್ಯಾನಿಸುವಾಗ ಮತ್ತು

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ನೇರವಾಗಿ ಚಾಟ್ ಏಜೆಂಟ್ ಅನ್ನು ರಚಿಸುವಾಗ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ಜೊತೆಗೆ ಏಜೆಂಟ್ ಚಾಲನೆಯಾಗುತ್ತಿರುವಾಗ ಕೂಡ

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ಈ ಕಾರ್ಯಾಚರಣೆಗೆ ಮಾತ್ರ ಒದಗಿಸಲಾದ ಉಪಕರಣ )
```

**ಏಜೆಂಟ್ ಥ್ರೆಡ್‌ಗಳು**

ಏಜೆಂಟ್ ಥ್ರೆಡ್‌ಗಳು ಬಹು-ತಿರುಗು ಸಂವಾದಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಬಳಸಲಾಗುತ್ತವೆ. ಥ್ರೆಡ್‌ಗಳನ್ನು ರಚಿಸುವುದು ಅಥವಾ `get_new_thread()` ಬಳಸಿ ನಿರಂತರವಾಗಿ ಸಂಗ್ರಹಿಸಲಾಗುವಂತೆ ಅಥವಾ ಏಜೆಂಟ್ ಚಾಲನೆಯಾಗುತ್ತಿರುವಾಗ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸೃಷ್ಟಿಯಾಗುವಂತೆ ಮಾಡಬಹುದು ಮತ್ತು ಥ್ರೆಡ್ ಆ ಚಾಲನೆಯ ಸಮಯ ಮಾತ್ರ ಕಾಯುತ್ತದೆ.

- `get_new_thread()` ಬಳಸುವ ಮೂಲಕ ಥ್ರೆಡ್ ಅನ್ನು ನಿಯತ ಸಮಯಕ್ಕೂಮುಂದುವರಿಸಲು ಸಾದ್ಯವಿದೆ
- ಏಜೆಂಟ್ ಚಾಲನೆಯಾಗುತ್ತಿರುವಾಗ ಸ್ವಯಂಚಾಲಿತ ಥ್ರೆಡ್ ರಚನೆ ಮತ್ತು ಅದು ಆ ಚಾಲನೆಯ ಸಮಯಕ್ಕೆ ಮಾತ್ರ ಇರುತ್ತದೆ.

ಥ್ರೆಡ್ ರಚಿಸಲು ಕೋಡ್ ಹೀಗೆ ಕಾಣುತ್ತದೆ:

```python
# ಹೊಸ ಥ್ರೆಡ್ ರಚಿಸಿ.
thread = agent.get_new_thread() # ಥ್ರೆಡಿನೊಂದಿಗೆ ಏಜೆಂಟ್ ಅನ್ನು ಚಲಾಯಿಸಿ.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

ನಂತರ ನೀವು ಥ್ರೆಡ್ ಅನ್ನು ಭವಿಷ್ಯ ಉಪಯೋಗಕ್ಕಾಗಿ ಸರಣಿ ಪ್ರಕ್ರಿಯೆಗೆ ಕಳುಹಿಸಬಹುದು:

```python
# ಹೊಸ ತರಂಗವನ್ನು ಸೃಷ್ಟಿಸಿ.
thread = agent.get_new_thread() 

# ಆಝೆಂಟ್ ಅನ್ನು ತರಂಗದೊಂದಿಗೆ ಚಾಲನೆ ಮಾಡಿ.

response = await agent.run("Hello, how are you?", thread=thread) 

# ಸಂಗ್ರಹಣೆಗೆ ತರಂಗವನ್ನು ಸರಣಿಗೊಳಿ.

serialized_thread = await thread.serialize() 

# ಸಂಗ್ರಹಣೆಯಿಂದ ಲೋಡ್ ಮಾಡಿದ ನಂತರ ತರಂಗ ಸ್ಥಿತಿಯನ್ನು ಅನಿರ್ದೇಶನ ಮಾಡಿ.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ಏಜೆಂಟ್ ಮಿಡ್‌ಲ್‌ವೇರ್**

ಏಜೆಂಟ್ಗಳು ಉಪಕರಣಗಳು ಮತ್ತು LLMs ಜೊತೆ ಬಳಕೆದಾರನ ಕಾರ್ಯಗಳನ್ನು ಮುಗಿಸಲು ಸಂವಹನ ಮಾಡುತ್ತವೆ. ಕೆಲವು ಸಂದರ್ಭಗಳಲ್ಲಿ, ಈ ಸಂವಹನಗಳ ನಡುವೆ ಕಾರ್ಯನಿರ್ವಹಣೆ ಅಥವಾ ಟ್ಯಾಕ್ ಮಾಡಲು ಬಯಸುತ್ತೇವೆ. ಏಜೆಂಟ್ ಮಿಡ್‌ಲ್‌ವೇರ್ ಇದನ್ನು ಈ ಕೆಳಗಿನ ಮೂಲಕ ಅನುಮತಿಸುತ್ತದೆ:

*ಫಂಕ್ಷನ್ ಮಿಡ್‌ಲ್‌ವೇರ್*

ಈ ಮಿಡ್‌ಲ್‌ವೇರ್ ಏಜೆಂಟ್ ಮತ್ತು ಕರೆಮಾಡಲಿರುವ ಫಂಕ್ಷನ್/ಟೂಲ್ಗಳ ನಡುವೆ ಕಾರ್ಯನಿರ್ವಹಿಸಲು ಅನುಮತಿಸುತ್ತದೆ. ಉದಾಹರಣೆಗಾಗಿ, ನೀವು ಫಂಕ್ಷನ್ ಕರೆ ಮಾಡುವಾಗ ಲಾಗಿಂಗ್ ಮಾಡಬಹುದು.

ಕೆಳಗಿನ ಕೋಡಿನಲ್ಲಿ `next` ಲು ಸೂಚಿಸುವುದು ಮುಂದಿನ ಮಿಡ್‌ಲ್‌ವೇರ್ ಅಥವಾ ನಿಜವಾದ ಫಂಕ್ಷನ್ ಕರೆ ಮಾಡಬೇಕೆಂದರೆ ಎಂದು.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ಪೂರ್ವ-ಪ್ರಕ್ರಿಯೆ: ಕಾರ್ಯನಿರ್ವಹಣೆಯ ಮೊದಲು ಲಾಗ್ ಮಾಡಿ
    print(f"[Function] Calling {context.function.name}")

    # ಮುಂದಿನ ಮಧ್ಯವರ್ತಿ ಅಥವಾ ಕಾರ್ಯನಿರ್ವಹಣೆ جاري ಇರಿಸಿ
    await next(context)

    # ನಂತರ-ಪ್ರಕ್ರಿಯೆ: ಕಾರ್ಯನಿರ್ವಹಣೆಯ ನಂತರ ಲಾಗ್ ಮಾಡಿ
    print(f"[Function] {context.function.name} completed")
```

*ಚಾಟ್ ಮಿಡ್‌ಲ್‌ವೇರ್*

ಈ ಮಿಡ್‌ಲ್‌ವೇರ್ ಏಜೆಂಟ್ ಮತ್ತು LLM ನಡುವೆ ವಿನಂತಿಗಳ ನಡುವೆ ಕಾರ್ಯನಿರ್ವಹಣೆ ಅಥವಾ ಲಾಗಿಂಗ್ ಮಾಡಲು ಸಹಾಯಮಾಡುತ್ತದೆ.

ಇದರಲ್ಲಿ `messages` ಎಂಬ ಏಐ ಸೇವೆಗೆ ಕಳುಹಿಸಲ್ಪಡುವ ಮಾಹಿತಿಯಂಥವು ಪ್ರಮುಖ.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ಪೂರ್ವ ಪ್ರಕ್ರಿಯೆ: AI ಕರೆಗೂ ಮೊದಲು ಲಾಗ್ ಮಾಡಿ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ಮುಂದಿನ ಮಿಡ್ಲ್ವೇರ್ ಅಥವಾ AI ಸೇವೆಗೆ ಮುಂದುವರಿಸಿ
    await next(context)

    # ನಂತರದ ಪ್ರಕ್ರಿಯೆ: AI ಪ್ರತಿಕ್ರಿಯೆಯ ನಂತರ ಲಾಗ್ ಮಾಡಿ
    print("[Chat] AI response received")

```

**ಏಜೆಂಟ್ ಮೆಮೊರಿ**

`Agentic Memory` ಪಾಠದಲ್ಲಿ ಚರ್ಚಿಸಲಾದಂತೆ, ಮೆಮೊರಿ ಏಜೆಂಟ್ ವಿಭಿನ್ನ ಸಂತರ್ಬಗಳಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸಲು ಮುಖ್ಯ ಅಂಶವಾಗಿದೆ. MAF ವಿವಿಧ ರೀತಿಯ ಮೆಮೊರಿಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ:

*ಇನ್-ಮೆಮೊರಿ ಸಂಗ್ರಹಣೆ*

ಇದು ಅಪ್ಲಿಕೇಶನ್ ಸಮಯದಲ್ಲಿ ಥ್ರೆಡ್‌ಗಳಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾದ ಮೆಮೊರಿ.

```python
# ಹೊಸ ತಂತಿಯನ್ನು ರಚಿಸಿ.
thread = agent.get_new_thread() # ತಂತಿಯೊಂದಿಗೆ ಏಜೆಂಟ್ ಅನ್ನು ಚಾಲನೆಮಾಡಿ.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*ದೃಢ ಸಂದೇಶಗಳು*

ಇದು ವಿಭಿನ್ನ ಅವಧಿಗಳಲ್ಲಿನ ಸಂವಾದ ಇತಿಹಾಸ ಸಂಗ್ರಹಿಸಲು ಬಳಸುವ ಮೆಮೊರಿ. `chat_message_store_factory` ಬಳಸಿ ವ್ಯಾಖ್ಯಾನ ಮಾಡಲಾಗಿದೆ:

```python
from agent_framework import ChatMessageStore

# ಒಂದು ಕಸ್ಟಮ್ ಸಂದೇಶ ಸಂಗ್ರಹವನ್ನು ರಚಿಸಿ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ಡೈನಾಮಿಕ್ ಮೆಮೊರಿ*


ಸಾರಣಿಗಳನ್ನು ಚಲಾಯಿಸುವ ಮೊದಲು ಈ ಮೆಮೊರಿ ಸಂಧರ್ಭಕ್ಕೆ ಸೇರಿಸಲಾಗುತ್ತದೆ. ಈ ವೃತ್ತಾಂತಗಳನ್ನು mem0ಂತಹ ಹೊರಗಿನ ಸೇವೆಗಳಲ್ಲಿ ಸಂಗ್ರಹಿಸಬಹುದು:

```python
from agent_framework.mem0 import Mem0Provider

# ಸುಧಾರಿತ ಮೆಮೊರಿ ಸಾಮರ್ಥ್ಯಗಳಿಗಾಗಿ Mem0 ಅನ್ನು ಬಳಸುವುದು
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

**ಏಜೆಂಟ್ ಗಮನಾರ್ಹತೆ**

ಯಥಾರ್ಥವೂ ನಿರ್ವಹಣೆಯೂ ಸಾಧ್ಯವಾದ ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಯನ್ನು ನಿರ್ಮಿಸಲು ಗಮನಾರ್ಹತೆ ಮಹತ್ವದ್ದಾಗಿವೆ. ಉತ್ತಮ ಗಮನಾರ್ಹತೆಗಾಗಿ MAF OpenTelemetry ಜೊತೆಗೆ ಸಂಯೋಜಿಸುವ ಮೂಲಕ ಟ್ರೇಸಿಂಗ್ ಮತ್ತು ಮಿತರ್‌ಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ಏನಾದರೂ ಮಾಡುವದು
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### ಕಾರ್ಯಪ್ರವಾಹಗಳು

ಕಾರ್ಯವನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ಪೂರ್ವನಿರ್ಧರಿತ ಹಂತಗಳಾಗಿ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು MAF ನೀಡುತ್ತದೆ ಮತ್ತು ಆ ಹಂತಗಳಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಭಾಗಗಳಾಗಿ ಒಳಗೊಂಡಿರುತ್ತದೆ.

ಕಾರ್ಯಪ್ರವಾಹಗಳು ಕೆಳಗಿನ ವಿವಿಧ ഘಟಕಗಳಿಂದ ಕೂಡಿವೆ, ಇದು ಉತ್ತಮ ನಿಯಂತ್ರಣ ಪ್ರವಾಹಕ್ಕೆ ಅವಕಾಶ ನೀಡುತ್ತದೆ. ಕಾರ್ಯಪ್ರವಾಹಗಳು **ಬಹು ಏಜೆಂಟ್ ಒರ್ಕೆಸ್ಟ್ರೇಶನ್** ಮತ್ತು ಕಾರ್ಯಪ್ರವಾಹ ಸ್ಥಿತಿಗಳನ್ನು ಉಳಿಸುವ **ಚೆಕ್ಪಾಯಿಂಟಿಂಗ್** ಸಹ ಅನುಮತಿಸುತ್ತದೆ.

ಕಾರ್ಯಪ್ರವಾಹದ ಪ್ರಾಥಮಿಕ ಘಟಕಗಳು:

**ಕಾರ್ಯನಿರ್ವಾಹಕಗಳು**

ಕಾರ್ಯನಿರ್ವಾಹಕರು ಇನ್ಪುಟ್ ಸಂದೇಶಗಳನ್ನು ಸ್ವೀಕರಿಸಿ, ಅವರ ನಿಗದිත ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಿ, ನಂತರ ಔಟ್‌ಪುಟ್ ಸಂದೇಶವನ್ನು ಉತ್ಪಾದಿಸುತ್ತಾರೆ. ಇದು ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ದೊಡ್ಡ ಕಾರ್ಯ ಪೂರೈಸುವತ್ತ ಸಾಗಿಸುತ್ತದೆ. ಕಾರ್ಯನಿರ್ವಾಹಕರು AI ಏಜೆಂಟ್ ಅಥವಾ ಕಸ್ಟಮ್ ಲಾಜಿಕಾಗಳಾಗಿರಬಹುದು.

**ಎಡ್ಜ್‌ಗಳು**

ಕಾರ್ಯಪ್ರವಾಹದಲ್ಲಿ ಸಂದೇಶಗಳ ಪ್ರವಾಹವನ್ನು ನಿರ್ಧರಿಸಲು edge ಗಳು ಉಪಯೋಗಿಸುತ್ತವೆ. ಇವುಗಳು:

*ನೇರ ಎಡ್ಜ್‌ಗಳು* - ಕಾರ್ಯನಿರ್ವಾಹಕರ ನಡುವೆ ಸರಳ ಒಂದು-ಮಾತ್ರ ಸಂಪರ್ಕಗಳು:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*ವೈಶಿಷ್ಟಿಕರಿತ ಎಡ್ಜ್‌ಗಳು* - ಕೆಲವು ಶರತ್ತುಗಳನ್ನು ಪೂರೈಸಿದ ಮೇಲೆ ಸಕ್ರಿಯಗೊಳ್ಳುತ್ತಾರೆ. ಉದಾಹರಣೆಗೆ, ಹೋಟೆಲ್ ಕೊಠಡಿಗಳು ಲಭ್ಯವಿಲ್ಲದಿದ್ದಾಗ, ಕಾರ್ಯನಿರ್ವಾಹಕನು ಇನ್ನಷ್ಟು ಆಯ್ಕೆಗಳನ್ನು ಸೂಚಿಸಬಹುದು.

*ಸ್ವಿಚ್-ಕೇಸ್ ಎಡ್ಜ್‌ಗಳು* - ನಿರ್ದಿಷ್ಟ ಶರತ್ತುಗಳ ಆಧಾರದಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ವಿಭಿನ್ನ ಕಾರ್ಯನಿರ್ವಾಹಕರಿಗೆ ಕಳುಹಿಸುತ್ತವೆ. ಉದಾಹರಣೆಗೆ, ಪ್ರಯಾಣದ ಗ್ರಾಹಕರಿಗೆ ಪ್ರಾಥಮಿಕ ಪ್ರವೇಶ ಇದ್ದರೆ ಅವರ ಕಾರ್ಯಗಳನ್ನು ಬೇರೆ ಕಾರ್ಯಪ್ರವಾಹದಿಂದ ನಿಭಾಯಿಸಲಾಗುತ್ತದೆ.

*ಫ್ಯಾನ್-ಆઉಟ್ ಎಡ್ಜ್‌ಗಳು* - ಒಂದೇ ಸಂದೇಶವನ್ನು ಬಹು ಗುರಿಗಳಿಗೆ ಕಳುಹಿಸುವುದು.

*ಫ್ಯಾನ್-ಇನ್ ಎಡ್ಜ್‌ಗಳು* - ವಿಭಿನ್ನ ಕಾರ್ಯನಿರ್ವಾಹಕರಿಂದ ಒಂದು ಗುರಿಗೆ ಬಹು ಸಂದೇಶಗಳನ್ನು ಸಂಗ್ರಹಿಸುವುದು.

**ಈವೆಂಟ್ಸ್**

ಕಾರ್ಯಪ್ರವಾಹ ಗತಿವಿಧಾನಗಳ ಉತ್ತಮ ಗಮನಾರ್ಹತೆಗಾಗಿ, MAF ನಿರ್ವಹಣೆಗೆ ಇತ್ಯರ್ಥ ಇವೆಂಟ್‌ಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ, ಅವುಗಳಲ್ಲಿ:

- `WorkflowStartedEvent` - ಕಾರ್ಯಪ್ರವಾಹ ಕಾರ್ಯಾಚರಣೆ ಪ್ರಾರಂಭ.
- `WorkflowOutputEvent` - ಕಾರ್ಯಪ್ರವಾಹ ಔಟ್‌ಪುಟ್ ಉತ್ಪಾದಿಸುತ್ತದೆ.
- `WorkflowErrorEvent` - ಕಾರ್ಯಪ್ರವಾಹದಲ್ಲು ದೋಷ.
- `ExecutorInvokeEvent` - ಕಾರ್ಯನಿರ್ವಾಹಕ ಪ್ರಕ್ರಿಯೆ ಆರಂಭ.
- `ExecutorCompleteEvent` -  ಕಾರ್ಯನಿರ್ವಾಹಕ ಪ್ರಕ್ರಿಯೆ ಪೂರ್ಣಗೊಳಿಸುವುದು.
- `RequestInfoEvent` - ವಿನಂತಿ ನೀಡಲಾಗಿದೆ.

## ಸುಧಾರಿತ MAF ಮಾದರಿಗಳು

ಮೇಲಿನ ವಿಭಾಗಗಳು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ನ ಪ್ರಮುಖ ಕಲ್ಪನೆಗಳನ್ನು ಒಳಗೊಂಡಿವೆ. ನೀವು ಹೆಚ್ಚು ಕಾಂಪ್ಲೆಕ್ಸಾದ ಏಜೆಂಡ್‌ಗಳನ್ನು ರಚಿಸುವಾಗ, ಇಲ್ಲಿ ಕೆಲವು ಸುಧಾರಿತ ಮಾದರಿಗಳನ್ನು ಪರಿಗಣಿಸಿ:

- **ಮಿಡ್‌ಲ್‌ವೇರ್ ಸಂಯೋಜನೆ**: ಲಾಗಿಂಗ್, ಅನುಮತಿ, ದರ ಮಿತಿಮೀರುವಿಕೆ ಮುಂತಾದ ಮಿಡ್‌ಲ್‌ವೇರ್ ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು ಚೈನ್ ಮಾಡುವುದು, ಕಾರ್ಯಾಚರಣೆ ಮತ್ತು ಚಾಟ್ ಮಿಡ್‌ಲ್‌ವೇರ್ ಬಳಸಿ ಏಜೆಂಟ್ ವರ್ತನೆ ಮೇಲೆ ಸೂಕ್ಷ್ಮ ನಿಯಂತ್ರಣ.
- **ಕಾರ್ಯಪ್ರವಾಹ ಚೆಕ್ಪಾಯಿಂಟಿಂಗ್**: ಕಾರ್ಯಾಚರಣೆ ಈವೆಂಟ್‌ಗಳು ಮತ್ತು ಸರಣೀಕರಣ ಬಳಸಿ ದೀರ್ಘಕಾಲಿಕ ಏಜೆಂಟ್ ಪ್ರಕ್ರಿಯೆಗಳನ್ನು ಉಳಿಸಿ ಪುನರಾರಂಭಿಸಲಾಗುವುದು.
- **ಡೈನಾಮಿಕ್ ಉಪಕರಣ ಆಯ್ಕೆ**: ಉಪಕರಣ ವಿವರಣೆಗಳ ಮೇಲೆ RAG ಯನ್ನು MAF ಉಪಕರಣ ನೋಂದಣಿಯೊಂದಿಗೆ ಸಂಯೋಜಿಸಿ ಪ್ರಶ್ನೆ ಪ್ರಕಾರ ಮಾತ್ರ ಸಂಬಂಧಿತ ಉಪಕರಣಗಳನ್ನು ಪ್ರದರ್ಶಿಸುವುದು.
- **ಬಹು ಏಜೆಂಟ್ ಹ್ಯಾಂಡ್ಓವರ್**: ವಿಶೇಷೀಕೃತ ಏಜೆಂಟ್‌ಗಳ ನಡುವೆ ಹ್ಯಾಂಡ್ಓವರ್‌ಗಳ ಒರ್ಕೆಸ್ಟ್ರೇಶನ್ ಗಾಗಿ ಕಾರ್ಯಪ್ರವಾಹ ಎಡ್ಜ್‌ಗಳು ಮತ್ತು ವೈಶಿಷ್ಟಿಕರಿತ ಮಾರ್ಗವನ್ನು ಉಪಯೋಗಿಸುವುದು.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ LangChain / LangGraph ಏಜೆಂಟ್‌ಗಳನ್ನು ಹೋಸ್ಟ್ ಮಾಡುವುದು

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ **ಫ್ರೇಮ್ವರ್ಕ್-ಅಂತರಚಾಲಕ** ಆಗಿದ್ದು, ನೀವು MAF ಬಳಸಿ ಬರೆದ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಮಾತ್ರ ಸೀಮಿತವಾಗಿಲ್ಲ. ನೀವು ಈಗಾಗಲೇ **LangChain** ಅಥವಾ **LangGraph** ನೊಂದಿಗೆ ಏಜೆಂಟ್ ನಿರ್ಮಿಸಿಕೊಂಡಿದ್ದರೆ, ಅದನ್ನು **Microsoft Foundry ಹೋಸ್ಟ್ ಮಾಡಿದ ಏಜೆಂಟ್** ಆಗಿ ಚಲಾಯಿಸಬಹುದು, ಅಲ್ಲಿ Foundry ರನ್‌ಟೈಮ್‌, ಸೆಷನ್‌ಗಳು, ಸ್ಕೇಲಿಂಗ್, ಪhತೆಯೂ ಮತ್ತು ಪ್ರೋಟೋಕಾಲ್ ಅಂತಿಮ ಬಿಂದುಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಆದರೆ ನಿಮ್ಮ ಏಜೆಂಟ್ ಲಾಜಿಕ್ LangGraph ನಲ್ಲಿ ಉಳಿಯುತ್ತದೆ.

ಇದು `langchain_azure_ai.agents.hosting` ಪ್ಯಾಕೇಜ್ ಮೂಲಕ ಮಾಡಲಾಗುತ್ತದೆ, ಇದು Foundry ಹೋಸ್ಟ್ ಮಾಡಿದ ಏಜೆಂಟ್‌ಗಳು ಬಳಸುವ ಅದೇ ಪ್ರೋಟೋಕಾಲ್‌ಗಳಲ್ಲಿ ಸಂಯೋಜಿತ LangGraph ಗ್ರಾಫ್ ಅನ್ನು ಬಹಿರಂಗ ಮಾಡುತ್ತದೆ.

**1. ಹೋಸ್ಟಿಂಗ್ ಎಕ್ಸ್ಟ್ರಾ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ಎಕ್ಸ್ಟ್ರಾ Foundry ಪ್ರೋಟೋಕಾಲ್ ಲೈಬ್ರರಿಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡುತ್ತದೆ: `azure-ai-agentserver-responses` (OpenAI-ಅನುಕೂಲ /responses ಎಂಡ್‌ಪಾಯಿಂಟ್) ಮತ್ತು `azure-ai-agentserver-invocations` (ಸಾಮಾನ್ಯ /invocations ಎಂಡ್‌ಪಾಯಿಂಟ್).

**2. ಹೋಸ್ಟಿಂಗ್ ಪ್ರೋಟೋಕಾಲ್ ಆಯ್ಕೆಮಾಡಿ:**

| ಪ್ರೋಟೋಕಾಲ್ | ಹೋಸ್ಟ್ ಕ್ಲಾಸ್ | ಎಂಡ್‌ಪಾಯಿಂಟ್ | ಯಾವಾಗ ಉಪಯೋಗಿಸುವುದು |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | ನೀವು OpenAI-ಅನುಕೂಲ ಚಾಟ್, ಸ್ಟ್ರೀಮಿಂಗ್, ಪ್ರತಿಕ್ರಿಯೆಯ ಇತಿಹಾಸ ಮತ್ತು ಸಂಭಾಷಣಾ ಥ್ರೆಡಿಂಗ್ ಬಯಸಿದಾಗ — ಸಂಭಾಷಣಾ ಏಜೆಂಟ್‌ಗಳಿಗಾಗಿ ಶಿಫಾರಸು ಮಾಡಲಾದ ಡೀಫಾಲ್ಟ್. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | ನೀವು ಕಸ್ಟಮ್ JSON ಆಕಾರ, ವೆಬ್‌ಹುಕ್ ಶೈಲಿ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅಥವಾ ಅಸಂಭಾಷಣಾ ಪ್ರಕ್ರಿಯೆಗಳನ್ನು ಬೇಕಾದಾಗ. |

**Responses API Foundry ಯಲ್ಲಿ ಏಜೆಂಟ್ ತರಹದ ಅಭಿವೃದ್ಧಿಗಾಗಿ ಪ್ರಮುಖ API ಆಗಿರುವುದರಿಂದ**, ಬಹು ಪ್ರತಿಕ್ರಿಯೆಗಳಿಗೆ `ResponsesHostServer` ಬಳಕೆ ಮಾಡಿ ಪ್ರಾರಂಭಿಸಿ.

**3. ಪರಿಸರ ಚರಗಳನ್ನು ಸಂರಚಿಸಿ** (`az login` ಮೊದಲು ಮಾಡಿ, ಹೀಗಾಗಿ `DefaultAzureCredential` ಪ್ರಮಾಣೀಕರಿಸುತ್ತದೆ):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ಏಜೆಂಟ್ ನಂತರ Foundry ನಲ್ಲಿ ಹೋಸ್ಟ್ ಆಗುವಾಗ, ವೇದಿಕೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ `FOUNDRY_PROJECT_ENDPOINT` ನ್ನು ಸೇರಿಸುತ್ತದೆ.

**4. Responses ಪ್ರೋಟೋಕಾಲ್ ಮೇಲೆ LangGraph ಏಜೆಂಟ್ ಅನ್ನು ಬಹಿರಂಗಗೊಳಿಸಿ:**

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

    # ChatOpenAI ಇಲ್ಲಿ Foundry ಯೋಜನೆಯ OpenAI-ಸಮ್ಮತ (ಪ್ರತಿಕ್ರಿಯೆಗಳು) ಅಂತಿಮಬಿಂದುವನ್ನು ಗುರಿಯಾಗಿಸಿಕೊಂಡಿದೆ.
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

`python main.py` ಬಳಸಿ ನಿಕಟದಲ್ಲಿ ಚಲಾಯಿಸಿ, ನಂತರ `http://localhost:8088/responses` ಗೆ Responses ವಿನಂತಿಯನ್ನು ಕಳುಹಿಸಿ.

**ಪ್ರಮುಖ ವರ್ತನೆಗಳು:**

- **ಸಂಭಾಷಣೆಗಳು**: ಕ್ಲೈಂಟ್‌ಗಳು `previous_response_id` ಅಥವಾ `conversation` ID ಅನ್ನು ಪಾಸ್ಸಿಂಗ್‌ ಮಾಡಿ ಸಂಭಾಷಣೆಯನ್ನ ಮುಂದುವರಿಸುತ್ತಾರೆ. ನಿಮ್ಮ ಗ್ರಾಫ್ LangGraph ಚೆಕ್ಪಾಯಿಂಟರ್‌ಗಳೊಂದಿಗೆ ಸಂಯೋಜಿತವಾಗಿದ್ದರೆ, Foundry ಸಂಭಾಷಣಾ ಸ್ಥಿತಿಯನ್ನು ಚೆಕ್ಪಾಯಿಂಟ್‌ಗೆ ಕೀ ಮಾಡುತ್ತದೆ (ಉತ್ಪಾದನೆಯಲ್ಲಿ ದೀರ್ಘಕಾಲ टिकುವ ಚೆಕ್ಪಾಯಿಂಟರ್, ಸ್ಥಳೀಯ ಪರೀಕ್ಷೆಗೆ `MemorySaver` ಸಾಕು).
- **ಮಾನವ-ಮಧ್ಯಸ್ಥಿತ್ವದಲ್ಲಿ**: ನಿಮ್ಮ ಗ್ರಾಫ್ LangGraph ನಲ್ಲಿ `interrupt()` ಉಪಯೋಗಿಸಿದರೆ, `ResponsesHostServer` ಬಾಕಿ ಇರುವ ಇಂಟರ್ಪ್ಟ್ ಅನ್ನು Responses `function_call` / `mcp_approval_request` ಐಟಂ ಆಗಿ ತೋರಿಸುತ್ತದೆ, ಮತ್ತು ಕ್ಲೈಂಟ್‌ಗಳು ಹೊಂದಾಣಿಕೆಯಾಗಿರುವ `function_call_output` / `mcp_approval_response` ಮೂಲಕ ಪುನರಾರಂಭಿಸುತ್ತವೆ.
- **Foundry ಗೆ ನಿಯೋಜಿಸಿ**: Azure Developer CLI ಉಪಯೋಗಿಸಿ — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ಸ್ಥಳೀಯ, Docker ಅಗತ್ಯ), ನಂತರ `azd provision` ಮತ್ತು `azd deploy`. ಹೋಸ್ಟ್ ಮಾಡಿದ ಏಜೆಂಟ್ ನಿಯೋಜನೆಗೆ **Foundry Project Manager** ಹುದ್ದೆ ಅಗತ್ಯ.

ಈ ಉದಾಹರಣೆಯ ಕಾರ್ಯನಿರ್ವಹಿಸಲು ಶೇಕಡಾ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ನಲ್ಲಿ ಲಭ್ಯವಿದೆ. ಸಂಪೂರ್ಣ ಮಾರ್ಗದರ್ಶನಕ್ಕಾಗಿ (Invocations ಪ್ರೋಟೋಕಾಲ್, ಕಸ್ಟಮ್ ವಿನಂತಿ ಶೀಮಾ ಮತ್ತು ಸಮಸ್ಯೆಗಳ ಪರಿಹಾರ), [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ನೋಡಿ.

## ಕೋಡ್ ಉದಾಹರಣೆಗಳು 

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗೆ ಸಂಬಂಧಿಸಿದ ಕೋಡ್ ಉದಾಹರಣೆಗಳನ್ನು ಈ ರೆಪೊಸಿಟರಿಯಲ್ಲಿ `xx-python-agent-framework` ಮತ್ತು `xx-dotnet-agent-framework` ಕಡತಗಳ ಅಡಿಯಲ್ಲಿ ಕಂಡುಹಿಡಿಯಬಹುದು.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿದೆಯೆ?

 ಇತರ ಕಲಿಕೆಯವರನ್ನು ಭೇಟಿಯಾಗಲು, ಕಚೇರಿ ಸಮಯಗಳಲ್ಲಿ ಭಾಗವಹಿಸಲು ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಗಳನ್ನು ಪಡೆಯಲು [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ಗೆ ಸೇರಿರಿ.
## ಮುನ್ನ elaborate

[AI ಏಜೆಂಟ್‌ಗಳ ನೆನಪು](../13-agent-memory/README.md)

## ಮುಂದಿನ elaborate


[ಕಂಪ್ಯೂಟರ್ ಬಳಕೆ ಏಜೆಂಟ್‌ಗಳನ್ನು (CUA) ನಿರ್ಮಿಸುವುದು](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->