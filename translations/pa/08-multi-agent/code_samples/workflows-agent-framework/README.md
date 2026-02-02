# ਮਲਟੀ-ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ Microsoft Agent Framework Workflow

ਇਹ ਟਿਊਟੋਰਿਅਲ ਤੁਹਾਨੂੰ Microsoft Agent Framework ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਲਟੀ-ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਸਮਝਣ ਅਤੇ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ। ਅਸੀਂ ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਦੇ ਮੁੱਖ ਧਾਰਨਾਵਾਂ ਦੀ ਪੜਚੋਲ ਕਰਾਂਗੇ, ਫਰੇਮਵਰਕ ਦੇ Workflow ਕੰਪੋਨੈਂਟ ਦੀ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਡੁੱਬਾਂਗੇ, ਅਤੇ Python ਅਤੇ .NET ਵਿੱਚ ਵੱਖ-ਵੱਖ ਵਰਕਫਲੋ ਪੈਟਰਨ ਦੇ ਪ੍ਰੈਕਟਿਕਲ ਉਦਾਹਰਣਾਂ ਦੇਖਾਂਗੇ।

## 1\. ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਨੂੰ ਸਮਝਣਾ

AI Agent ਇੱਕ ਸਿਸਟਮ ਹੈ ਜੋ ਇੱਕ ਸਧਾਰਨ Large Language Model (LLM) ਦੀ ਸਮਰੱਥਾ ਤੋਂ ਅੱਗੇ ਜਾਂਦਾ ਹੈ। ਇਹ ਆਪਣੇ ਵਾਤਾਵਰਣ ਨੂੰ ਸਮਝ ਸਕਦਾ ਹੈ, ਫੈਸਲੇ ਲੈ ਸਕਦਾ ਹੈ, ਅਤੇ ਨਿਰਧਾਰਤ ਲਕਸ਼ਾਂ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕਾਰਵਾਈ ਕਰ ਸਕਦਾ ਹੈ। ਇੱਕ ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਵਿੱਚ ਕਈ ਏਜੰਟ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ ਜੋ ਇੱਕ ਅਜਿਹੀ ਸਮੱਸਿਆ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਸਹਿਯੋਗ ਕਰਦੇ ਹਨ ਜੋ ਇੱਕੋ ਏਜੰਟ ਲਈ ਮੁਸ਼ਕਲ ਜਾਂ ਅਸੰਭਵ ਹੋ ਸਕਦੀ ਹੈ।

### ਆਮ ਐਪਲੀਕੇਸ਼ਨ ਸਥਿਤੀਆਂ

  * **ਜਟਿਲ ਸਮੱਸਿਆ ਹੱਲ**: ਇੱਕ ਵੱਡੇ ਕੰਮ (ਜਿਵੇਂ ਕਿ ਕੰਪਨੀ-ਵਿਆਪਕ ਇਵੈਂਟ ਦੀ ਯੋਜਨਾ) ਨੂੰ ਛੋਟੇ ਉਪ-ਕੰਮਾਂ ਵਿੱਚ ਵੰਡਣਾ ਜੋ ਵਿਸ਼ੇਸ਼ ਏਜੰਟਾਂ ਦੁਆਰਾ ਸੰਭਾਲੇ ਜਾਂਦੇ ਹਨ (ਜਿਵੇਂ ਕਿ ਬਜਟ ਏਜੰਟ, ਲਾਜਿਸਟਿਕਸ ਏਜੰਟ, ਮਾਰਕੀਟਿੰਗ ਏਜੰਟ)।
  * **ਵਰਚੁਅਲ ਅਸਿਸਟੈਂਟ**: ਇੱਕ ਪ੍ਰਾਇਮਰੀ ਅਸਿਸਟੈਂਟ ਏਜੰਟ ਜੋ ਸ਼ਡਿਊਲਿੰਗ, ਰਿਸਰਚ, ਅਤੇ ਬੁਕਿੰਗ ਵਰਗੇ ਕੰਮਾਂ ਨੂੰ ਹੋਰ ਵਿਸ਼ੇਸ਼ ਏਜੰਟਾਂ ਨੂੰ ਸੌਂਪਦਾ ਹੈ।
  * **ਆਟੋਮੈਟਿਕ ਸਮੱਗਰੀ ਬਣਾਉਣਾ**: ਇੱਕ ਵਰਕਫਲੋ ਜਿੱਥੇ ਇੱਕ ਏਜੰਟ ਸਮੱਗਰੀ ਦਾ ਮਸੌਦਾ ਤਿਆਰ ਕਰਦਾ ਹੈ, ਦੂਜਾ ਇਸਨੂੰ ਸਹੀਤਾ ਅਤੇ ਟੋਨ ਲਈ ਸਮੀਖਾ ਕਰਦਾ ਹੈ, ਅਤੇ ਤੀਜਾ ਇਸਨੂੰ ਪ੍ਰਕਾਸ਼ਿਤ ਕਰਦਾ ਹੈ।

### ਮਲਟੀ-ਏਜੰਟ ਪੈਟਰਨ

ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਕਈ ਪੈਟਰਨਾਂ ਵਿੱਚ ਆਯੋਜਿਤ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ, ਜੋ ਇਹ ਨਿਰਧਾਰਤ ਕਰਦੇ ਹਨ ਕਿ ਉਹ ਕਿਵੇਂ ਪਰਸਪਰ ਕਿਰਿਆਸ਼ੀਲ ਹਨ:

  * **ਲਗਾਤਾਰ**: ਏਜੰਟ ਇੱਕ ਪੂਰਵ-ਨਿਰਧਾਰਤ ਕ੍ਰਮ ਵਿੱਚ ਕੰਮ ਕਰਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਇੱਕ ਅਸੈਂਬਲੀ ਲਾਈਨ। ਇੱਕ ਏਜੰਟ ਦਾ ਆਉਟਪੁੱਟ ਅਗਲੇ ਏਜੰਟ ਲਈ ਇਨਪੁੱਟ ਬਣ ਜਾਂਦਾ ਹੈ।
  * **ਸਮਕਾਲੀ**: ਏਜੰਟ ਇੱਕ ਕੰਮ ਦੇ ਵੱਖ-ਵੱਖ ਹਿੱਸਿਆਂ 'ਤੇ ਇਕੱਠੇ ਕੰਮ ਕਰਦੇ ਹਨ, ਅਤੇ ਅੰਤ ਵਿੱਚ ਉਨ੍ਹਾਂ ਦੇ ਨਤੀਜੇ ਇਕੱਠੇ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
  * **ਸ਼ਰਤੀ**: ਵਰਕਫਲੋ ਵੱਖ-ਵੱਖ ਰਾਹਾਂ ਦਾ ਪਾਲਣ ਕਰਦਾ ਹੈ ਜੋ ਇੱਕ ਏਜੰਟ ਦੇ ਆਉਟਪੁੱਟ ਦੇ ਅਧਾਰ 'ਤੇ ਹੁੰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਇੱਕ if-then-else ਬਿਆਨ।

## 2\. Microsoft Agent Framework Workflow ਆਰਕੀਟੈਕਚਰ

Agent Framework ਦਾ ਵਰਕਫਲੋ ਸਿਸਟਮ ਇੱਕ ਅਗਰਗਤੀ ਆਰਕੈਸਟ੍ਰੇਸ਼ਨ ਇੰਜਨ ਹੈ ਜੋ ਕਈ ਏਜੰਟਾਂ ਦੇ ਵਿਚਕਾਰ ਜਟਿਲ ਪਰਸਪਰ ਕਿਰਿਆਸ਼ੀਲਤਾ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਹ ਇੱਕ ਗ੍ਰਾਫ-ਅਧਾਰਿਤ ਆਰਕੀਟੈਕਚਰ 'ਤੇ ਬਣਾਇਆ ਗਿਆ ਹੈ ਜੋ [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ, ਜਿੱਥੇ ਪ੍ਰੋਸੈਸਿੰਗ "supersteps" ਕਹੇ ਜਾਣ ਵਾਲੇ ਸਮਰੂਪਿਤ ਕਦਮਾਂ ਵਿੱਚ ਹੁੰਦੀ ਹੈ।

### ਮੁੱਖ ਕੰਪੋਨੈਂਟ

ਆਰਕੀਟੈਕਚਰ ਤਿੰਨ ਮੁੱਖ ਹਿੱਸਿਆਂ 'ਤੇ ਆਧਾਰਿਤ ਹੈ:

1.  **Executors**: ਇਹ ਮੂਲ ਪ੍ਰੋਸੈਸਿੰਗ ਯੂਨਿਟ ਹਨ। ਸਾਡੇ ਉਦਾਹਰਣਾਂ ਵਿੱਚ, `Agent` ਇੱਕ ਕਿਸਮ ਦਾ executor ਹੈ। ਹਰ executor ਵਿੱਚ ਕਈ ਮੈਸੇਜ ਹੈਂਡਲਰ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਪ੍ਰਾਪਤ ਮੈਸੇਜ ਦੀ ਕਿਸਮ ਦੇ ਅਧਾਰ 'ਤੇ ਸਵੈਚਾਲਿਤ ਤੌਰ 'ਤੇ ਚਲਾਏ ਜਾਂਦੇ ਹਨ।
2.  **Edges**: ਇਹ ਉਹ ਰਾਹ ਨਿਰਧਾਰਤ ਕਰਦੇ ਹਨ ਜੋ ਮੈਸੇਜ executors ਦੇ ਵਿਚਕਾਰ ਲੈਂਦੇ ਹਨ। Edges ਵਿੱਚ ਸ਼ਰਤਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ, ਜੋ ਵਰਕਫਲੋ ਗ੍ਰਾਫ ਦੇ ਰਾਹੀਂ ਜਾਣਕਾਰੀ ਦੇ ਗਤੀਮਾਨ ਰੂਟਿੰਗ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ।
3.  **Workflow**: ਇਹ ਕੰਪੋਨੈਂਟ ਪੂਰੇ ਪ੍ਰਕਿਰਿਆ ਦਾ ਆਰਕੈਸਟ੍ਰੇਸ਼ਨ ਕਰਦਾ ਹੈ, executors, edges, ਅਤੇ ਕੁੱਲ execution ਦੇ ਪ੍ਰਵਾਹ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ। ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਮੈਸੇਜ ਸਹੀ ਕ੍ਰਮ ਵਿੱਚ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਅਤੇ observability ਲਈ ਇਵੈਂਟਾਂ ਨੂੰ ਸਟ੍ਰੀਮ ਕਰਦਾ ਹੈ।

*ਵਰਕਫਲੋ ਸਿਸਟਮ ਦੇ ਮੁੱਖ ਕੰਪੋਨੈਂਟਾਂ ਨੂੰ ਦਰਸਾਉਣ ਵਾਲਾ ਇੱਕ ਡਾਇਗ੍ਰਾਮ।*

ਇਹ ਸੰਰਚਨਾ ਲਗਾਤਾਰ ਚੇਨ, ਸਮਕਾਲੀ ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ fan-out/fan-in, ਅਤੇ ਸ਼ਰਤੀ ਪ੍ਰਵਾਹਾਂ ਲਈ switch-case ਲਾਜਿਕ ਵਰਗੇ ਮੁੱਢਲੇ ਪੈਟਰਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਜ਼ਬੂਤ ਅਤੇ ਸਕੇਲਬਲ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ।

## 3\. ਪ੍ਰੈਕਟਿਕਲ ਉਦਾਹਰਣ ਅਤੇ ਕੋਡ ਵਿਸ਼ਲੇਸ਼ਣ

ਹੁਣ, ਆਓ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵੱਖ-ਵੱਖ ਵਰਕਫਲੋ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਦੇ ਤਰੀਕੇ ਦੀ ਪੜਚੋਲ ਕਰੀਏ। ਅਸੀਂ ਹਰ ਉਦਾਹਰਣ ਲਈ Python ਅਤੇ .NET ਕੋਡ ਦੇਖਾਂਗੇ।

### ਕੇਸ 1: ਬੇਸਿਕ ਲਗਾਤਾਰ ਵਰਕਫਲੋ

ਇਹ ਸਭ ਤੋਂ ਸਧਾਰਨ ਪੈਟਰਨ ਹੈ, ਜਿੱਥੇ ਇੱਕ ਏਜੰਟ ਦਾ ਆਉਟਪੁੱਟ ਸਿੱਧੇ ਦੂਜੇ ਨੂੰ ਪਾਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਸਾਡਾ ਸਥਿਤੀਕਰਣ ਇੱਕ ਹੋਟਲ `FrontDesk` ਏਜੰਟ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ ਜੋ ਯਾਤਰਾ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦਾ ਹੈ, ਜਿਸਨੂੰ ਫਿਰ ਇੱਕ `Concierge` ਏਜੰਟ ਦੁਆਰਾ ਸਮੀਖਿਆ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

*ਬੇਸਿਕ FrontDesk -> Concierge ਵਰਕਫਲੋ ਦਾ ਡਾਇਗ੍ਰਾਮ।*

#### ਸਥਿਤੀ ਪਿਛੋਕੜ

ਇੱਕ ਯਾਤਰੀ ਪੈਰਿਸ ਵਿੱਚ ਸਿਫਾਰਸ਼ ਲਈ ਪੁੱਛਦਾ ਹੈ।

1.  `FrontDesk` ਏਜੰਟ, ਜੋ ਸੰਖੇਪਤਾ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ, ਲੂਵਰ ਮਿਊਜ਼ੀਅਮ ਦਾ ਦੌਰਾ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦਾ ਹੈ।
2.  `Concierge` ਏਜੰਟ, ਜੋ ਪ੍ਰਮਾਣਿਕ ਅਨੁਭਵਾਂ ਨੂੰ ਤਰਜੀਹ ਦਿੰਦਾ ਹੈ, ਇਸ ਸਿਫਾਰਸ਼ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ। ਇਹ ਸਿਫਾਰਸ਼ ਦੀ ਸਮੀਖਿਆ ਕਰਦਾ ਹੈ ਅਤੇ ਇੱਕ ਹੋਰ ਸਥਾਨਕ, ਘੱਟ ਸੈਲਾਨੀ-ਪਸੰਦੀਦਾ ਵਿਕਲਪ ਦੀ ਪੇਸ਼ਕਸ਼ ਕਰਦਾ ਹੈ।

#### Python Implementation Analysis

Python ਉਦਾਹਰਣ ਵਿੱਚ, ਅਸੀਂ ਪਹਿਲਾਂ ਦੋ ਏਜੰਟਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਅਤੇ ਬਣਾਉਂਦੇ ਹਾਂ, ਹਰ ਇੱਕ ਨੂੰ ਵਿਸ਼ੇਸ਼ ਹਦਾਇਤਾਂ ਦੇ ਨਾਲ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

ਅਗਲੇ, `WorkflowBuilder` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਗ੍ਰਾਫ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ। `front_desk_agent` ਨੂੰ ਸ਼ੁਰੂਆਤੀ ਬਿੰਦੂ ਵਜੋਂ ਸੈਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਇਸਦੇ ਆਉਟਪੁੱਟ ਨੂੰ `reviewer_agent` ਨਾਲ ਜੋੜਨ ਲਈ edge ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

ਅੰਤ ਵਿੱਚ, ਵਰਕਫਲੋ ਨੂੰ ਸ਼ੁਰੂਆਤੀ ਯੂਜ਼ਰ ਪ੍ਰੰਪਟ ਨਾਲ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) Implementation Analysis

.NET ਲਾਗੂਕਰਨ ਬਹੁਤ ਹੀ ਸਮਾਨ ਤਰਕ ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ। ਪਹਿਲਾਂ, ਏਜੰਟਾਂ ਦੇ ਨਾਮ ਅਤੇ ਹਦਾਇਤਾਂ ਲਈ constants ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`OpenAIClient` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਏਜੰਟ ਬਣਾਏ ਜਾਂਦੇ ਹਨ, ਅਤੇ ਫਿਰ `WorkflowBuilder` ਲਗਾਤਾਰ ਪ੍ਰਵਾਹ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ, `frontDeskAgent` ਤੋਂ `reviewerAgent` ਤੱਕ edge ਜੋੜਦਾ ਹੈ।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

ਵਰਕਫਲੋ ਫਿਰ ਯੂਜ਼ਰ ਦੇ ਸੁਨੇਹੇ ਨਾਲ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਨਤੀਜੇ ਸਟ੍ਰੀਮ ਵਾਪਸ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

### ਕੇਸ 2: ਮਲਟੀ-ਸਟੈਪ ਲਗਾਤਾਰ ਵਰਕਫਲੋ

ਇਹ ਪੈਟਰਨ ਬੇਸਿਕ ਲਗਾਤਾਰ ਕ੍ਰਮ ਨੂੰ ਹੋਰ ਏਜੰਟਾਂ ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਵਧਾਉਂਦਾ ਹੈ। ਇਹ ਪ੍ਰਕਿਰਿਆਵਾਂ ਲਈ ਆਦਰਸ਼ ਹੈ ਜੋ ਕਈ ਪੜਾਅ ਦੇ ਸੁਧਾਰ ਜਾਂ ਰੂਪਾਂਤਰਨ ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ।

#### ਸਥਿਤੀ ਪਿਛੋਕੜ

ਇੱਕ ਯੂਜ਼ਰ ਲਿਵਿੰਗ ਰੂਮ ਦੀ ਇੱਕ ਤਸਵੀਰ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਅਤੇ ਫਰਨੀਚਰ ਕੋਟ ਦੀ ਮੰਗ ਕਰਦਾ ਹੈ।

1.  **Sales-Agent**: ਤਸਵੀਰ ਵਿੱਚ ਫਰਨੀਚਰ ਆਈਟਮਾਂ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ ਅਤੇ ਇੱਕ ਸੂਚੀ ਬਣਾਉਂਦਾ ਹੈ।
2.  **Price-Agent**: ਆਈਟਮਾਂ ਦੀ ਸੂਚੀ ਲੈਂਦਾ ਹੈ ਅਤੇ ਬਜਟ, ਮਿਡ-ਰੇਂਜ, ਅਤੇ ਪ੍ਰੀਮੀਅਮ ਵਿਕਲਪਾਂ ਸਮੇਤ ਵਿਸਤ੍ਰਿਤ ਕੀਮਤ ਵਿਸ਼ਲੇਸ਼ਣ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।
3.  **Quote-Agent**: ਕੀਮਤ ਵਾਲੀ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ ਅਤੇ ਇਸਨੂੰ Markdown ਵਿੱਚ ਇੱਕ ਅਧਿਕਾਰਕ ਕੋਟ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਫਾਰਮੈਟ ਕਰਦਾ ਹੈ।

*Sales -> Price -> Quote ਵਰਕਫਲੋ ਦਾ ਡਾਇਗ੍ਰਾਮ।*

#### Python Implementation Analysis

ਤਿੰਨ ਏਜੰਟ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਹਰ ਇੱਕ ਵਿਸ਼ੇਸ਼ ਭੂਮਿਕਾ ਦੇ ਨਾਲ। ਵਰਕਫਲੋ `add_edge` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਚੇਨ ਬਣਾਉਂਦਾ ਹੈ: `sales_agent` -> `price_agent` -> `quote_agent`।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ਇਨਪੁੱਟ ਇੱਕ `ChatMessage` ਹੈ ਜੋ ਟੈਕਸਟ ਅਤੇ ਤਸਵੀਰ URI ਦੋਨੋ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ। ਫਰੇਮਵਰਕ ਹਰ ਏਜੰਟ ਦੇ ਆਉਟਪੁੱਟ ਨੂੰ ਲਗਾਤਾਰ ਅਗਲੇ ਵਿੱਚ ਪਾਸ ਕਰਦਾ ਹੈ ਜਦੋਂ ਤੱਕ ਅੰਤਮ ਕੋਟ ਤਿਆਰ ਨਹੀਂ ਹੁੰਦਾ।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### .NET (C#) Implementation Analysis

.NET ਉਦਾਹਰਣ Python ਵਰਜਨ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। ਤਿੰਨ ਏਜੰਟ (`salesagent`, `priceagent`, `quoteagent`) ਬਣਾਏ ਜਾਂਦੇ ਹਨ। `WorkflowBuilder` ਉਨ੍ਹਾਂ ਨੂੰ ਲਗਾਤਾਰ ਜੋੜਦਾ ਹੈ।

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ਯੂਜ਼ਰ ਦਾ ਸੁਨੇਹਾ ਤਸਵੀਰ ਡਾਟਾ (bytes ਵਜੋਂ) ਅਤੇ ਟੈਕਸਟ ਪ੍ਰੰਪਟ ਦੋਨੋ ਦੇ ਨਾਲ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ। `InProcessExecution.StreamAsync` ਵਿਧੀ ਵਰਕਫਲੋ ਸ਼ੁਰੂ ਕਰਦੀ ਹੈ, ਅਤੇ ਅੰਤਮ ਆਉਟਪੁੱਟ ਸਟ੍ਰੀਮ ਤੋਂ ਕੈਪਚਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

### ਕੇਸ 3: ਸਮਕਾਲੀ ਵਰਕਫਲੋ

ਇਹ ਪੈਟਰਨ ਉਸ ਸਮੇਂ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ ਜਦੋਂ ਕੰਮ ਇਕੱਠੇ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਤਾਂ ਕਿ ਸਮਾਂ ਬਚਾਇਆ ਜਾ ਸਕੇ। ਇਹ "fan-out" ਨੂੰ ਕਈ ਏਜੰਟਾਂ ਵੱਲ ਅਤੇ "fan-in" ਨੂੰ ਨਤੀਜਿਆਂ ਨੂੰ ਇਕੱਠਾ ਕਰਨ ਲਈ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ।

#### ਸਥਿਤੀ ਪਿਛੋਕੜ

ਇੱਕ ਯੂਜ਼ਰ ਸਿਆਟਲ ਦੀ ਯਾਤਰਾ ਦੀ ਯੋਜਨਾ ਬਣਾਉਣ ਲਈ ਪੁੱਛਦਾ ਹੈ।

1.  **Dispatcher (Fan-Out)**: ਯੂਜ਼ਰ ਦੀ ਬੇਨਤੀ ਇੱਕ ਸਮੇਂ ਵਿੱਚ ਦੋ ਏਜੰਟਾਂ ਨੂੰ ਭੇਜੀ ਜਾਂਦੀ ਹੈ।
2.  **Researcher-Agent**: ਸਿਆਟਲ ਵਿੱਚ ਦਸੰਬਰ ਵਿੱਚ ਯਾਤਰਾ ਲਈ ਆਕਰਸ਼ਣ, ਮੌਸਮ, ਅਤੇ ਮੁੱਖ ਵਿਚਾਰਾਂ ਦੀ ਖੋਜ ਕਰਦਾ ਹੈ।
3.  **Plan-Agent**: ਸਵਤੰਤਰ ਤੌਰ 'ਤੇ ਇੱਕ ਵਿਸਤ੍ਰਿਤ ਦਿਨ-ਦਰ-ਦਿਨ ਯਾਤਰਾ ਯੋਜਨਾ ਬਣਾਉਂਦਾ ਹੈ।
4.  **Aggregator (Fan-In)**: researcher ਅਤੇ planner ਤੋਂ ਆਉਟਪੁੱਟ ਇਕੱਠਾ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਅੰਤਮ ਨਤੀਜੇ ਵਜੋਂ ਪੇਸ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

*Concurrent Researcher ਅਤੇ Planner ਵਰਕਫਲੋ ਦਾ ਡਾਇਗ੍ਰਾਮ।*

#### Python Implementation Analysis

`ConcurrentBuilder` ਇਸ ਪੈਟਰਨ ਦੀ ਰਚਨਾ ਨੂੰ ਸਧਾਰਨ ਬਣਾਉਂਦਾ ਹੈ। ਤੁਸੀਂ ਸਿਰਫ਼ ਭਾਗੀਦਾਰ ਏਜੰਟਾਂ ਦੀ ਸੂਚੀ ਦਿੰਦੇ ਹੋ, ਅਤੇ builder ਸਵੈਚਾਲਿਤ ਤੌਰ 'ਤੇ ਜ਼ਰੂਰੀ fan-out ਅਤੇ fan-in ਲਾਜਿਕ ਬਣਾਉਂਦਾ ਹੈ।

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

ਫਰੇਮਵਰਕ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ `research_agent` ਅਤੇ `plan_agent` ਸਮਕਾਲੀ ਤੌਰ 'ਤੇ ਚਲਦੇ ਹਨ, ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਅੰਤਮ ਆਉਟਪੁੱਟ ਇੱਕ ਸੂਚੀ ਵਿੱਚ ਇਕੱਠੇ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

#### .NET (C#) Implementation Analysis

.NET ਵਿੱਚ, ਇਸ ਪੈਟਰਨ ਲਈ ਹੋਰ explicit ਪਰਿਭਾਸ਼ਾ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। Custom executors (`ConcurrentStartExecutor` ਅਤੇ `ConcurrentAggregationExecutor`) fan-out ਅਤੇ fan-in ਲਾਜਿਕ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਬਣਾਏ ਜਾਂਦੇ ਹਨ।

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

`WorkflowBuilder` ਫਿਰ `AddFanOutEdge` ਅਤੇ `AddFanInEdge` ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਤਾਂ ਕਿ ਇਹ custom executors ਅਤੇ agents ਨਾਲ ਗ੍ਰਾਫ ਬਣਾਇਆ ਜਾ ਸਕੇ।

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### ਕੇਸ 4: ਸ਼ਰਤੀ ਵਰਕਫਲੋ

ਸ਼ਰਤੀ ਵਰਕਫਲੋ ਸ਼ਾਖਾ ਲਾਜਿਕ ਨੂੰ ਪੇਸ਼ ਕਰਦੇ ਹਨ, ਜੋ ਸਿਸਟਮ ਨੂੰ ਮੱਧਵਰਤੀ ਨਤੀਜਿਆਂ ਦੇ ਅਧਾਰ 'ਤੇ ਵੱਖ-ਵੱਖ ਰਾਹਾਂ ਨੂੰ ਲੈਣ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ।

#### ਸਥਿਤੀ ਪਿਛੋਕੜ

ਇਹ ਵਰਕਫਲੋ ਇੱਕ ਤਕਨੀਕੀ ਟਿਊਟੋਰਿਅਲ ਬਣਾਉਣ ਅਤੇ ਪ੍ਰਕਾਸ਼ਿਤ ਕਰਨ ਨੂੰ ਆਟੋਮੈਟ ਕਰਦਾ ਹੈ।

1.  **Evangelist-Agent**: ਦਿੱਤੇ outline ਅਤੇ URLs ਦੇ ਅਧਾਰ 'ਤੇ ਟਿਊਟੋਰਿਅਲ ਦਾ ਮਸੌਦਾ ਲਿਖਦਾ ਹੈ।
2.  **ContentReviewer-Agent**: ਮਸੌਦੇ ਦੀ ਸਮੀਖਿਆ ਕਰਦਾ ਹੈ। ਇਹ ਜਾਂਚਦਾ ਹੈ ਕਿ ਸ਼ਬਦ ਗਿਣਤੀ 200 ਸ਼ਬਦਾਂ ਤੋਂ ਵੱਧ ਹੈ।
3.  **ਸ਼ਰਤੀ ਸ਼ਾਖਾ**:
      * **ਜੇ ਮਨਜ਼ੂਰ ਕੀਤਾ ਗਿਆ (`Yes`)**: ਵਰਕਫਲੋ `Publisher-Agent` ਵੱਲ ਅੱਗੇ ਵਧਦਾ ਹੈ।
      * **ਜੇ ਰੱਦ ਕੀਤਾ ਗਿਆ (`No`)**: ਵਰਕਫਲੋ ਰੁਕ ਜਾਂਦਾ ਹੈ ਅਤੇ ਰੱਦ ਕਰਨ ਦਾ ਕਾਰਨ ਆਉਟਪੁੱਟ ਕਰਦਾ ਹੈ।
4.  **Publisher-Agent**: ਜੇ ਮਸੌਦਾ ਮਨਜ਼ੂਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਇਹ ਏਜੰਟ ਸਮੱਗਰੀ ਨੂੰ Markdown ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕਰਦਾ ਹੈ।

#### Python Implementation Analysis

ਇਸ ਉਦਾਹਰਣ ਵਿੱਚ ਇੱਕ custom function, `select_targets`, ਸ਼ਰਤੀ ਲਾਜਿਕ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਇਹ function `add_multi_selection_edge_group` ਨੂੰ ਪਾਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ `review_result` ਫੀਲਡ ਦੇ ਅਧਾਰ 'ਤੇ ਵਰਕਫਲੋ ਨੂੰ ਨਿਰਦੇਸ਼ਿਤ ਕਰਦਾ ਹੈ।

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Custom executors ਜ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।