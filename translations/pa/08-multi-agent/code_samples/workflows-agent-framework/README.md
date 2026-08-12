# ਮைகਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਵਰਕਫਲੋ ਨਾਲ ਮਲਟੀ-ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

ਇਹ ਟਿਊਟੋਰਿਅਲ ਤੁਹਾਨੂੰ ਮਲਟੀ-ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਸਮਝਣ ਅਤੇ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ Microsoft Agent Framework ਦੀ ਵਰਤੋਂ ਕਰਕੇ। ਅਸੀਂ ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮਾਂ ਦੇ ਮੁੱਖ ਸੰਕਲਪਾਂ ਨੂੰ ਖੰਗਾਲਾਂਗੇ, ਫਰੇਮਵਰਕ ਦੇ ਵਰਕਫਲੋ ਕੰਪੋਨੈਂਟ ਦੀ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਡੁੱਬਾਂਗੇ, ਅਤੇ ਵੱਖ-ਵੱਖ ਵਰਕਫਲੋ ਪੈਟਰਨਾਂ ਲਈ Python ਅਤੇ .NET ਦੋਹਾਂ ਵਿੱਚ ਵਿਹਾਰਕ ਉਦਾਹਰਨਾਂ ਨਾਲ ਚਲਾਂਗੇ।

## 1\. ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਸਮਝਣਾ

ਇੱਕ AI ਏਜੰਟ ਇੱਕ ਸਿਸਟਮ ਹੈ ਜੋ ਇੱਕ ਸਧਾਰਣ ਲਾਰਜ ਲੈਂਗਵੇਜ ਮੌਡਲ (LLM) ਦੀ ਸਮਰੱਥਾ ਤੋਂ ਅੱਗੇ ਵੱਧਦਾ ਹੈ। ਇਹ ਆਪਣੇ ਵਾਤਾਵਰਣ ਨੂੰ ਮਹਿਸੂਸ ਕਰ ਸਕਦਾ ਹੈ, ਫੈਸਲੇ ਲੈ ਸਕਦਾ ਹੈ, ਅਤੇ ਵਿਸ਼ੇਸ਼ ਲਕੜੀਆਂ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕਾਰਵਾਈ ਕਰਦਾ ਹੈ। ਇੱਕ ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਕਈ ਇਨ੍ਹਾਂ ਏਜੰਟਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ ਜੋ ਇੱਕ ਐਸਾ ਸਮੱਸਿਆ ਹੱਲ ਕਰਨ ਲਈ ਮਿਲ ਕੇ ਕੰਮ ਕਰਦੇ ਹਨ ਜੋ ਇੱਕ ਹੀ ਏਜੰਟ ਲਈ ਅਕੇਲਾ ਸੰਭਵ ਜਾਂ ਮੁਸ਼ਕਲ ਹੁੰਦਾ।

### ਆਮ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਦ੍ਰਿਸ਼

  * **ਜਟਿਲ ਸਮੱਸਿਆ ਹੱਲ**: ਵੱਡੇ ਕੰਮ ਨੂੰ (ਜਿਵੇਂ ਕਿ ਕੰਪਨੀ-ਵਿਆਪਕ ਸਮਾਗਮ ਦੀ ਯੋਜਨਾ) ਛੋਟੇ ਉਪ-ਕੰਮਾਂ ਵਿੱਚ ਵੰਡਨਾ ਜੋ ਵਿਸ਼ੇਸ਼ ਐਜੰਟਾਂ ਦੁਆਰਾ ਸੰਭਾਲੇ ਜਾਂਦੇ ਹਨ (ਜਿਵੇਂ ਕਿ ਬਜਟ ਏਜੰਟ, ਲੋਜਿਸਟਿਕਸ ਏਜੰਟ, ਮਾਰਕੀਟਿੰਗ ਏਜੰਟ)।
  * **ਵਰਚੁਅਲ ਅਸਿਸਟੈਂਟ**: ਇੱਕ ਪ੍ਰਮੁੱਖ ਅਸਿਸਟੈਂਟ ਏਜੰਟ ਜੋ ਨਿਯਮਤ ਤੌਰ ‘ਤੇ ਟਾਸਕਾਂ ਨੂੰ ਮੇਲ-ਜੋਲ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਸ਼ਡਿਊਲਿੰਗ, ਖੋਜ, ਅਤੇ ਬੁਕਿੰਗ ਹੋਰ ਵਿਸ਼ੇਸ਼ ਐਜੰਟਾਂ ਨੂੰ ਸौंਂਪਦੇ ਹਨ।
  * **ਆਟੋਮੇਟਿਕ ਸਮੱਗਰੀ ਬਣਾਉਣ**: ਇੱਕ ਵਰਕਫਲੋ ਜਿਸ ਵਿੱਚ ਇੱਕ ਏਜੰਟ ਸਮੱਗਰੀ ਦਾ ਡਰਾਫਟ ਤਿਆਰ ਕਰਦਾ ਹੈ, ਦੂਜਾ ਇਸਦੀ ਸਹੀਤਾ ਅਤੇ ਟੋਨ ਲਈ ਸਮੀਖਿਆ ਕਰਦਾ ਹੈ, ਅਤੇ ਤੀਜਾ ਇਸਨੂੰ ਪ੍ਰਕਾਸ਼ਿਤ ਕਰਦਾ ਹੈ।

### ਮਲਟੀ-ਏਜੰਟ ਪੈਟਰਨ

ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਕੁਝ ਪੈਟਰਨਾਂ ਵਿੱਚ ਆਯੋਜਿਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਜੋ ਇਹ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਉਹ ਕਿਵੇਂ ਇੰਟਰਐਕਟ ਕਰਦੇ ਹਨ:

  * **ਕ੍ਰਮਿਕ (Sequential)**: ਏਜੰਟ ਇਕ ਨਿਰਧਾਰਿਤ ਕ੍ਰਮ ਵਿੱਚ ਕੰਮ ਕਰਦੇ ਹਨ, ਜਿਵੇਂ ਇਕ ਅਸੈਂਬਲੀ ਲਾਈਨ। ਇੱਕ ਏਜੰਟ ਦਾ ਨਤੀਜਾ ਦੂਜੇ ਲਈ ਇਨਪੁੱਟ ਬਣਦਾ ਹੈ।
  * **ਸਮਕਾਲੀ (Concurrent)**: ਏਜੰਟ ਇਕੋ ਸਮੇਂ ਵੱਖ-ਵੱਖ ਹਿੱਸਿਆਂ ‘ਤੇ ਕੰਮ ਕਰਦੇ ਹਨ, ਅਤੇ ਉਹਨਾਂ ਦੇ ਨਤੀਜੇ ਆਖਿਰ ਵਿੱਚ ਜੋੜੇ ਜਾਂਦੇ ਹਨ।
  * **ਸ਼ਰਤੀ (Conditional)**: ਵਰਕਫਲੋ ਇੱਕ ਏਜੰਟ ਦੇ ਨਤੀਜੇ ਦੇ ਆਧਾਰ ‘ਤੇ ਵੱਖ-ਵੱਖ ਰਸਤੇ ਫੋਲੋ ਕਰਦਾ ਹੈ, ਇਕ if-then-else ਬਿਆਨ ਵਾਂਗ।

## 2\. ਮਾਇਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਵਰਕਫਲੋ ਆਰਕੀਟੈਕਚਰ

ਏਜੰਟ ਫਰੇਮਵਰਕ ਦਾ ਵਰਕਫਲੋ ਸਿਸਟਮ ਇਕ ਉਤਕ੍ਰਿਸ਼ਟ ਓਰਕੈਸਟਰੈਸ਼ਨ ਇੰਜਣ ਹੈ ਜੋ ਕਈ ਏਜੰਟਾਂ ਦਰਮਿਆਨ ਜਟਿਲ ਇੰਟਰੇਕਸ਼ਨਾਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ। ਇਹ ਇੱਕ ਗ੍ਰਾਫ-ਆਧਾਰਤ ਆਰਕੀਟੈਕਚਰ ‘ਤੇ ਅਧਾਰਤ ਹੈ ਜੋ ਇੱਕ [Pregel-ਸ਼ੈਲੀ ਕਾਰਜਨ ਢਾਂਚਾ](https://kowshik.github.io/JPregel/pregel_paper.pdf) ਵਰਤਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਪ੍ਰੋਸੈਸਿੰਗ "ਸੁਪਰਸਟੇਪ" ਕਿਹਾ ਜਾਂਦਾ ਸਮਾਂਨੁਕੂਲ ਕਦਮਾਂ ਵਿੱਚ ਹੁੰਦੀ ਹੈ।

### ਮੁੱਖ ਭਾਗ

ਆਰਕੀਟੈਕਚਰ ਤਿੰਨ ਮੁੱਖ ਹਿੱਸਿਆਂ ਦਾ ਬਣਿਆ ਹੈ:

1.  **ਐਕਜ਼ਿਕਿਊਟਰ**: ਇਹ ਮੂਲ ਪ੍ਰੋਸੈਸਿੰਗ ਯੂਨਿਟ ਹੁੰਦੇ ਹਨ। ਸਾਡੇ ਉਦਾਹਰਣ ਵਿੱਚ, ਇੱਕ `Agent` ਇੱਕ ਰੂਪ ਦਾ ਐਕਜ਼ਿਕਿਊਟਰ ਹੁੰਦਾ ਹੈ। ਹਰ ਐਕਜ਼ਿਕਿਊਟਰ ਕੋਲ ਕਈ ਮੈਸੇਜ ਹੈਂਡਲਰ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਪ੍ਰਾਪਤ ਮੈਸੇਜ ਦੀ ਕਿਸਮ ਅਨੁਸਾਰ ਆਪਮੈਤ ਤੌਰ ‘ਤੇ ਕੰਮ ਕਰਦੇ ਹਨ।
2.  **ਏਜ**: ਇਹ ਪਰਿਵਹਨ ਰਸਤੇ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਨ ਜੋ ਐਕਜ਼ਿਕਿਊਟਰਾਂ ਦੇ ਵਿਚਕਾਰ ਸੰਦੇਸ਼ ਲੈਂਦੇ ਹਨ। ਏਜਾਂ ਕੋਲ ਸ਼ਰਤਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ, ਜੋ ਵਰਕਫਲੋ ਗ੍ਰਾਫ ਵਿੱਚ ਜਾਣਕਾਰੀ ਦੇ ਗਤੀਵਿਧੀ ਲੋੜਾਂ ਮੁਤਾਬਕ ਆਵਾਜਾਈ ਕਰਦੀਆਂ ਹਨ।
3.  **ਵਰਕਫਲੋ**: ਇਹ ਪੂਰੇ ਪ੍ਰਕਿਰਿਆ ਦੀ ਓਰਕੈਸਟਰਿੰਗ ਕਰਦਾ ਹੈ, ਐਕਜ਼ਿਕਿਊਟਰਾਂ, ਏਜਾਂ, ਅਤੇ ਸਮੂਹ ਵਰਤੋਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ। ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਮੈਸੇਜ ਸਹੀ ਕ੍ਰਮ ਵਿੱਚ ਪ੍ਰਕਿਰਿਆ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਅਤੇ ਮੌਨੀਟਰਿੰਗ ਲਈ ਇਹ ਵਾਰਦਾਤਾਂ ਨੂੰ ਸਟ੍ਰੀਮ ਕਰਦਾ ਹੈ।

*ਵਰਕਫਲੋ ਸਿਸਟਮ ਦੇ ਮੁੱਖ ਭਾਗਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਇੱਕ ਡਾਇਗ੍ਰਾਮ।*

ਇਹ ਢਾਂਚਾ ਮੂਲ ਪੈਟਰਨਾਂ ਵਰਗੇ ਕਿ੍ਰਮਿਕ ਚੇਨ, ਫੈਨ-ਆਉਟ/ਫੈਨ-ਇਨ ਪੈਰੈਲਲ ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ, ਅਤੇ ਸ਼ਰਤੀ ਫਲੋਜ਼ ਲਈ ਸੁਵਿੱਚ-ਕੇਸ ਲਾਜਿਕ ਵਰਗੇ ਮਜ਼ਬੂਤ ਅਤੇ ਸਕੇਲਬਲ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

## 3\. ਵਿਹਾਰਕ ਉਦਾਹਰਨ ਅਤੇ ਕੋਡ ਵਿਸ਼ਲੇਸ਼ਣ

ਹੁਣ ਅਸੀਂ ਵੇਖਾਂਗੇ ਕਿਵੇਂ ਵੱਖ-ਵੱਖ ਵਰਕਫਲੋ ਪੈਟਰਨਾਂ ਨੂੰ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲਾਗੂ ਕੀਤਾ ਜਾਵੇ। ਅਸੀਂ ਹਰ ਉਦਾਹਰਨ ਲਈ Python ਅਤੇ .NET ਕੋਡ ਨੂੰ ਵੇਖਾਂਗੇ।

### ਮਾਮਲਾ 1: ਬੁਨਿਆਦੀ ਕ੍ਰਮਿਕ ਵਰਕਫਲੋ

ਇਹ ਸਭ ਤੋਂ ਸਧਾਰਣ ਪੈਟਰਨ ਹੈ, ਜਿੱਥੇ ਇੱਕ ਏਜੰਟ ਦਾ ਨਤੀਜਾ ਸਿੱਧਾ ਦੂਜੇ ਵਲ ਪਾਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਸਾਡਾ ਪਰਿਦ੍ਰਿਸ਼ਟ ਇੱਕ ਹੋਟਲ `FrontDesk` ਏਜੰਟ ਹੈ ਜੋ ਯਾਤਰਾ ਸਿਫਾਰਸ਼ ਕਰਦਾ ਹੈ, ਜਿਸ ਨੂੰ ਬਾਅਦ ਵਿੱਚ `Concierge` ਏਜੰਟ ਦੁਆਰਾ ਸਮੀਖਿਆ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

*ਮੂਲ FrontDesk -> Concierge ਵਰਕਫਲੋ ਦਾ ਡਾਇਗ੍ਰਾਮ।*

#### ਪਿਛੋਕੜ

ਇੱਕ ਯਾਤਰੀ ਪੈਰਿਸ ਵਿੱਚ ਸਿਫਾਰਸ਼ ਮੰਗਦਾ ਹੈ।

1.  `FrontDesk` ਏਜੰਟ, ਜੋ ਸੰਖੇਪ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ, ਲੂਵਰ ਮਿਊਜੀਅਮ ਵਿਚ ਜਾਉਣ ਦੀ ਸਿਫਾਰਸ਼ ਦਿੰਦਾ ਹੈ।
2.  `Concierge` ਏਜੰਟ, ਜੋ ਅਸਲੀ ਅਨੁਭਵਾਂ ਨੂੰ ਤਰਜੀਹ ਦਿੰਦਾ ਹੈ, ਇਸ ਸਿਫਾਰਸ਼ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ। ਇਹ ਸਿਫਾਰਸ਼ ਦੀ ਸਮੀਖਿਆ ਕਰਦਾ ਹੈ ਅਤੇ ਫੀਡਬੈਕ ਦਿੰਦਾ ਹੈ, ਜੋ ਇੱਕ ਹੋਰ ਸਥਾਨਕ, ਕਮ ਘੂਮਣ-ਫਿਰਣ ਵਾਲਾ ਵਿਕਲਪ ਸੁਝਾਉਂਦਾ ਹੈ।

#### Python ਲਾਗੂ ਕਰਨ ਦੀ ਸਮੀਖਿਆ

Python ਉਦਾਹਰਨ ਵਿੱਚ ਅਸੀਂ ਪਹਿਲਾਂ ਦੋ ਏਜੰਟ ਪਰਿਭਾਸ਼ਿਤ ਅਤੇ ਬਣਾਉਂਦੇ ਹਾਂ, ਹਰ ਇੱਕ ਖ਼ਾਸ ਹੁਕਮਾਂ ਨਾਲ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# ਏਜੰਟ ਦੇ ਭੂਮਿਕਾਵਾਂ ਅਤੇ ਹਦਾਇਤਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# ਏਜੰਟ ਉਦਾਹਰਨਾਂ ਬਣਾਓ
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

ਅਗਲਾ, `WorkflowBuilder` ਨਾਲ ਗ੍ਰਾਫ ਬਣਾਈਏ। `front_desk_agent` ਸ਼ੁਰੂਆਤੀ ਬਿੰਦੂ ਵਜੋਂ ਸੈੱਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਇੱਕ ਏਜ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ ਜੋ ਇਸ ਦਾ ਨਤੀਜਾ `reviewer_agent` ਨੂੰ ਜੋੜਦਾ ਹੈ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

ਅੰਤ 'ਚ ਵਰਕਫਲੋ ਮੂਲ ਯੂਜ਼ਰ ਪ੍ਰੰਪਟ ਨਾਲ ਚਲਾਈ ਜਾਂਦੀ ਹੈ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run ਵਰਕਫਲੋ ਚਲਾਉਂਦਾ ਹੈ; get_outputs() ਆਉਟਪੁੱਟ ਐਕਸਿਕਿਊਟਰ ਦਾ ਨਤੀਜਾ ਵਾਪਸ ਕਰਦਾ ਹੈ।
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C#) ਲਾਗੂ ਕਰਨ ਦੀ ਸਮੀਖਿਆ

.NET ਲਾਗੂ ਕਰਨ ਵੱਡੇ ਪੱਧਰ ‘ਤੇ ਸਮਾਨ ਤਰਤੀਬ ਨਾਲ ਹੁੰਦਾ ਹੈ। ਪਹਿਲਾਂ ਏਜੰਟਾਂ ਦੇ ਨਾਮ ਅਤੇ ਹੁਕਮਾਂ ਲਈ ਕਾਂਸਟੈਂਟ ਡਿਫਾਈਨ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ਏਜੰਟ `AzureOpenAIClient` (Responses API) ਦੀ ਵਰਤੋਂ ਨਾਲ ਬਣਾਏ ਜਾਂਦੇ ਹਨ, ਅਤੇ ਫਿਰ `WorkflowBuilder` ਕ੍ਰਮਿਕ ਅਨੁਕ੍ਰਮ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ `frontDeskAgent` ਤੋਂ `reviewerAgent` ਲਈ ਏਜ ਜੋੜੀ ਜਾਂਦੀ ਹੈ।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

ਵਰਕਫਲੋ ਨੂੰ ਯੂਜ਼ਰ ਦੀ ਸੁਨੇਹਾ ਨਾਲ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਨਤੀਜੇ ਵਾਪਸ ਸਟ੍ਰੀਮ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

### ਮਾਮਲਾ 2: ਬਹੁ-ਕਦਮੀ ਕ੍ਰਮਿਕ ਵਰਕਫਲੋ

ਇਹ ਪੈਟਰਨ ਬੁਨਿਆਦੀ ਕ੍ਰਮ ਨੂੰ ਵੱਧ ਏਜੰਟਾਂ ਨਾਲ ਵਧਾਉਂਦਾ ਹੈ। ਇਹ ਉਹਨਾਂ ਪ੍ਰਕਿਰਿਆਵਾਂ ਲਈ ਸੁਧਾਰਤ ਹੈ ਜਿੱਥੇ ਕਈ ਪੜਾਵਾਂ ਦੀ ਬਦਲਾਵ ਜਾਂ ਰੂਪਾਂਤਰਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

#### ਪਿਛੋਕੜ

ਇੱਕ ਯੂਜ਼ਰ ਇੱਕ ਲਿਵਿੰਗ ਰੂਮ ਦੀ ਤਸਵੀਰ ਦਿੰਦਾ ਹੈ ਅਤੇ ਫਰਨੀਚਰ ਦਾ ਕੋਟ ਮੰਗਦਾ ਹੈ।

1.  **Sales-Agent**: ਤਸਵੀਰ ਵਿੱਚ ਫਰਨੀਚਰ ਦੀਆਂ ਚੀਜ਼ਾਂ ਪਛਾਣਦਾ ਹੈ ਅਤੇ ਇੱਕ ਸੂਚੀ ਬਣਾਉਂਦਾ ਹੈ।
2.  **Price-Agent**: ਚੀਜ਼ਾਂ ਦੀ ਸੂਚੀ ਲੈਂਦਾ ਹੈ ਅਤੇ ਬਜਟ, ਮਿੱਡ-ਰੇਂਜ, ਅਤੇ ਪ੍ਰੀਮੀਅਮ ਵਿਕਲਪਾਂ ਸਮੇਤ ਵਿਸਥਾਰਿਤ ਕੀਮਤ ਵੰਡ ਦਿੰਦਾ ਹੈ।
3.  **Quote-Agent**: ਕੀਮਤ ਵਾਲੀ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ ਅਤੇ ਇਸਨੂੰ ਮਾਰਕਡਾਊਨ ਵਿੱਚ ਆਧਿਕਾਰਿਕ ਕੋਟ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਫਾਰਮੈਟ ਕਰਦਾ ਹੈ।

*Sales -> Price -> Quote ਵਰਕਫਲੋ ਦਾ ਡਾਇਗ੍ਰਾਮ।*

#### Python ਲਾਗੂ ਕਰਨ ਦੀ ਸਮੀਖਿਆ

ਤਿੰਨ ਏਜੰਟ ਪਰਿਭਾਸ਼ਿਤ ਹਨ, ਹਰ ਇੱਕ ਖ਼ਾਸ ਭੂਮਿਕਾ ਨਾਲ। ਵਰਕਫਲੋ ਨੂੰ `add_edge` ਵਰਤ ਕੇ ਚੇਨ ਬਣਾਈ ਗਈ ਹੈ: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ਤਿੰਨ ਵਿਸ਼ੇਸ਼ ਏਜੰਟ ਬਣਾਓ
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# ਕ੍ਰਮਵਾਰ ਵਰਕਫ਼ਲੋ ਬਣਾਓ
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ਇਨਪੁੱਟ ਇੱਕ `ChatMessage` ਹੈ ਜੋ ਟੈਕਸਟ ਅਤੇ ਤਸਵੀਰ URI ਦੋਹਾਂ ਸ਼ਾਮਲ ਹੈ। ਫਰੇਮਵਰਕ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਹਰ ਏਜੰਟ ਦੇ ਨਤੀਜੇ ਅਗਲੇ ਨੂੰ ਕ੍ਰਮ ਵਿੱਚ ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ ਜਦ ਤੱਕ ਆਖਰੀ ਕੋਟ ਤਿਆਰ ਨਹੀਂ ਹੁੰਦੀ।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ਉਪਭੋਗਤਾ ਸੁਨੇਹਾ ਵਿਚ ਦੋਹਾਂ ਲਿਖਤ ਅਤੇ ਇੱਕ ਚਿੱਤਰ ਸ਼ਾਮਲ ਹੈ
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# ਵਰਕਫਲੋ ਚਲਾਓ
events = await workflow.run(message)
```

#### .NET (C#) ਲਾਗੂ ਕਰਨ ਦੀ ਸਮੀਖਿਆ

.NET ਉਦਾਹਰਨ Python ਵਰਜਨ ਦੇ ਸਮਾਨ ਹੈ। ਤਿੰਨ ਏਜੰਟ (`salesagent`, `priceagent`, `quoteagent`) ਬਣਾਏ ਜਾਂਦੇ ਹਨ। `WorkflowBuilder` ਉਨ੍ਹਾਂ ਨੂੰ ਕ੍ਰਮਿਕ ਤੌਰ ‘ਤੇ ਜੋੜਦਾ ਹੈ।

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ਯੂਜ਼ਰ ਦਾ ਸੁਨੇਹਾ ਤਸਵੀਰ ਦੇ ਡੇਟਾ (ਬਾਈਟਸ ਵਜੋਂ) ਅਤੇ ਟੈਕਸਟ ਪ੍ਰੰਪਟ ਦੋਹਾਂ ਦੇ ਨਾਲ ਤਿਆਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। `InProcessExecution.RunStreamingAsync` ਵਰਕਫਲੋ ਨੂੰ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ, ਅਤੇ ਆਖਰੀ ਨਤੀਜਾ ਸਟ੍ਰੀਮ ਤੋਂ ਕੈਪਚਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

### ਮਾਮਲਾ 3: ਸਮਕਾਲੀ ਵਰਕਫਲੋ

ਇਹ ਪੈਟਰਨ ਉਸ ਵੇਲੇ ਵਰਤੀ ਜਾਂਦੀ ਹੈ ਜਦ ਟਾਸਕ ਇਕੱਠੇ ਕੀਤੇ ਜਾਂ ਸਕਦੇ ਹਨ ਤਾਂ ਜੋ ਸਮਾਂ ਬਚਾਇਆ ਜਾ ਸਕੇ। ਇਹ "ਫੈਨ-ਆਉਟ" ਪਹੁੰਚ ਨੂੰ ਕਈ ਏਜੰਟਾਂ ਵੱਲ ਜਾਂਦਾ ਹੈ ਅਤੇ "ਫੈਨ-ਇਨ" ਨਾਲ ਨਤੀਜੇ ਇਕੱਠੇ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

#### ਪਿਛੋਕੜ

ਇੱਕ ਯੂਜ਼ਰ ਸਿਏਟਲ ਯਾਤਰਾ ਦੀ ਯੋਜਨਾ ਬਨਾਉਣ ਲਈ ਕਹਿੰਦਾ ਹੈ।

1.  **Dispatcher (Fan-Out)**: ਯੂਜ਼ਰ ਦੀ ਅਰਜ਼ੀ ਇੱਕੋ ਸਮੇਂ ਦੋ ਏਜੰਟਾਂ ਨੂੰ ਭੇਜੀ ਜਾਂਦੀ ਹੈ।
2.  **Researcher-Agent**: ਸਿਏਟਲ ਵਿੱਚ ਦਸੰਬਰ ਦੀ ਯਾਤਰਾ ਲਈ ਆਕਰਸ਼ਣ, ਮੌਸਮ, ਅਤੇ ਮੁੱਖ ਗੱਲਾਂ ਦੀ ਖੋਜ ਕਰਦਾ ਹੈ।
3.  **Plan-Agent**: ਸੁਤੰਤਰ ਤੌਰ ‘ਤੇ ਦਿਨ ਦਰ ਦਿਨ ਯਾਤਰਾ ਯੋਜਨਾ ਤਿਆਰ ਕਰਦਾ ਹੈ।
4.  **Aggregator (Fan-In)**: ਦੋਹਾਂ ਰਿਸਰਚਰ ਅਤੇ ਯੋਜਨਾਕਾਰ ਦੇ ਨਤੀਜੇ ਇਕੱਠੇ ਕਰਕੇ ਅੰਤਿਮ ਨਤੀਜਾ ਤਿਆਰ ਕਰਦਾ ਹੈ।

*Concurrent Researcher ਅਤੇ Planner ਵਰਕਫਲੋ ਦਾ ਡਾਇਗ੍ਰਾਮ।*

#### Python ਲਾਗੂ ਕਰਨ ਦੀ ਸਮੀਖਿਆ

`ConcurrentBuilder` ਇਸ ਪੈਟਰਨ ਨੂੰ ਬਣਾਉਣ ਨੂੰ ਆਸਾਨ ਕਰਦਾ ਹੈ। ਤੁਸੀਂ ਸਿਰਫ਼ ਸਹਿਭਾਗੀ ਏਜੰਟਾਂ ਨੂੰ ਸੂਚੀਬੱਧ ਕਰਦੇ ਹੋ, ਅਤੇ ਬਿਲਡਰ ਆਪਣੇ ਆਪ ਫੈਨ-ਆਉਟ ਅਤੇ ਫੈਨ-ਇਨ ਲਾਜਿਕ ਬਣਾਉਂਦਾ ਹੈ।

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ਫੈਨ-ਆਉਟ/ਫੈਨ-ਇਨ ਲੋਜਿਕ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# workflow ਚਲਾਓ
events = await workflow.run("Plan a trip to Seattle in December")
```

ਫਰੇਮਵਰਕ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ `research_agent` ਅਤੇ `plan_agent` ਇਕੱਠੇ ਚੱਲਦੇ ਹਨ, ਅਤੇ ਉਹਨਾਂ ਦੇ ਅੰਤਿਮ ਨਤੀਜੇ ਇੱਕ ਲਿਸਟ ਵਿੱਚ ਇਕੱਠੇ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

#### .NET (C#) ਲਾਗੂ ਕਰਨ ਦੀ ਸਮੀਖਿਆ

.NET ਵਿੱਚ ਇਹ ਪੈਟਰਨ ਥੋੜ੍ਹੀ ਵੱਧ ਸਪਸ਼ਟ ਪਰਿਭਾਸ਼ਾ ਮੰਗਦਾ ਹੈ। ਫੈਨ-ਆਉਟ ਅਤੇ ਫੈਨ-ਇਨ ਲਾਜਿਕ ਸੰਭਾਲਣ ਲਈ ਕਸਟਮ ਐਕਜ਼ਿਕਿਊਟਰ ਬਣਾਏ ਜਾਂਦੇ ਹਨ (`ConcurrentStartExecutor` ਅਤੇ `ConcurrentAggregationExecutor`)।

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

ਫਿਰ `WorkflowBuilder` `AddFanOutEdge` ਅਤੇ `AddFanInEdge` ਵਰਤ ਕੇ ਇਸ ਗ੍ਰਾਫ ਨੂੰ ਕਸਟਮ ਐਕਜ਼ਿਕਿਊਟਰਾਂ ਅਤੇ ਏਜੰਟਾਂ ਨਾਲ ਬਣਾਉਂਦਾ ਹੈ।

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### ਮਾਮਲਾ 4: ਸ਼ਰਤੀ ਵਰਕਫਲੋ

ਸ਼ਰਤੀ ਵਰਕਫਲੋ ਵਿੱਚ ਬ੍ਰਾਂਚਿੰਗ ਲਾਜਿਕ ਸ਼ਾਮਲ ਹੁੰਦੀ ਹੈ, ਜੋ ਸਿਸਟਮ ਨੂੰ ਅੰਤਰਿਮ ਨਤੀਜਿਆਂ ਦੇ ਆਧਾਰ ‘ਤੇ ਵੱਖ-ਵੱਖ ਰਾਹ ਲੈਣ ਦੇ ਯੋਗ ਬਣਾਉਂਦੀ ਹੈ।

#### ਪਿਛੋਕੜ

ਇਹ ਵਰਕਫਲੋ ਇਕ ਟੈਕਨੀਕਲ ਟਿਊਟੋਰਿਅਲ ਦੇ ਬਣਾਉਣ ਅਤੇ ਪ੍ਰਕਾਸ਼ਨ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ।

1.  **Evangelist-Agent**: ਇੱਕ ਦਿੱਤੇ ਗਏ ਆਊਟਲਾਈਨ ਅਤੇ URLs ਦੇ ਆਧਾਰ ‘ਤੇ ਟਿਊਟੋਰਿਅਲ ਦਾ ਡਰਾਫਟ ਲਿਖਦਾ ਹੈ।
2.  **ContentReviewer-Agent**: ਡਰਾਫਟ ਦੀ ਸਮੀਖਿਆ ਕਰਦਾ ਹੈ। ਜाँचਦਾ ਹੈ ਕਿ ਸ਼ਬਦਾਂ ਦੀ ਗਿਣਤੀ 200 ਤੋਂ ਵੱਧ ਹੈ ਜਾਂ ਨਹੀਂ।
3.  **ਸ਼ਰਤੀਕ ਬ੍ਰਾਂਚ**:
      * **ਜੇ ਮਨਜ਼ੂਰ (`Yes`)**: ਵਰਕਫ਼ਲੋ `Publisher-Agent` ਵੱਲ ਵਧਦਾ ਹੈ।
      * **ਜੇ ਨਾ-ਮਨਜ਼ੂਰ (`No`)**: ਵਰਕਫਲੋ ਰੁਕ ਜਾਂਦਾ ਹੈ ਅਤੇ ਇਨਕਾਰ ਦੇ ਕਾਰਨ ਨੂੰ ਆਉਟਪੁੱਟ ਕਰਦਾ ਹੈ।
4.  **Publisher-Agent**: ਜੇ ਡਰਾਫਟ ਮਨਜ਼ੂਰ ਹੈ, ਇਹ ਏਜੰਟ ਸਮੱਗਰੀ ਨੂੰ ਮਾਰਕਡਾਊਨ ਫਾਇਲ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਕਰਦਾ ਹੈ।

#### Python ਲਾਗੂ ਕਰਨ ਦੀ ਸਮੀਖਿਆ

ਇਸ ਉਦਾਹਰਣ ਵਿੱਚ ਇੱਕ ਕਸਟਮ ਫੰਕਸ਼ਨ `select_targets` ਵਰਤਿਆ ਗਿਆ ਹੈ ਜੋ ਸ਼ਰਤੀ ਲਾਜਿਕ ਨੂੰ ਲਾਗੂ ਕਰਦਾ ਹੈ। ਇਹ ਫੰਕਸ਼ਨ `add_multi_selection_edge_group` ਨੂੰ ਦਿੱਤਾ ਗਿਆ ਹੈ ਅਤੇ ਸਮੀਖਿਆਕਾਰ ਦੇ ਆਊਟਪੁੱਟ ਦੇ `review_result` ਖੇਤਰ `ਦੇ ਆਧਾਰ ‘ਤੇ ਵਰਕਫਲੋ ਨੂੰ ਦਿਸ਼ਾ ਦਿੰਦਾ ਹੈ।

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ਇਹ ਫੰਕਸ਼ਨ ਸਮੀਖਿਆ ਨਤੀਜੇ ਦੇ ਆਧਾਰ 'ਤੇ ਅਗਲਾ ਕਦਮ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ਜੇ ਮਨਜ਼ੂਰ ਹੋਵੇ, ਤਾਂ 'save_draft' ਐਗਜ਼ੀਕਿੂਟਰ ਵੱਲ ਵਧੋ
        return [save_draft_id]
    else:
        # ਜੇ ਰੱਦ ਕੀਤਾ ਗਿਆ, ਤਾਂ ਫੇਲ੍ਹ ਦੀ ਰਿਪੋਰਟ ਕਰਨ ਲਈ 'handle_review' ਐਗਜ਼ੀਕਿੂਟਰ ਵੱਲ ਵਧੋ
        return [handle_review_id]

# ਵਰਕਫਲੋ ਬਿਲਡਰ ਰੂਟਿੰਗ ਲਈ ਚੋਣ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # ਮਲਟੀ-ਚੋਣ ਐਜ ਸਾਵਿਕਲ ਤਰਕ ਦੀ ਕਾਰਜਾਨਵੇਂਸ਼ ਕਰਦਾ ਹੈ
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

ਜਿਵੇਂ ਕਿ `to_reviewer_result` ਵਰਗੇ ਕਸਟਮ ਐਕਜ਼ਿਕਿਊਟਰ JSON ਆਊਟਪੁੱਟ ਨੂੰ ਮਜ਼ਬੂਤ ਟਾਈਪ ਵਾਲੇ ਵਸਤੂਆਂ ਵਿਚ ਪਰਿਵਰਤਿਤ ਕਰਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਚੋਣ ਫੰਕਸ਼ਨ ਜਾਂਚ ਸਕਦਾ ਹੈ।

#### .NET (C#) ਲਾਗੂ ਕਰਨ ਦੀ ਸਮੀਖਿਆ

.NET ਵਰਜ਼ਨ ਸਮਾਨ ਤਰੀਕੇ ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ। ਇੱਕ `Func<object?, bool>` ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜੋ `ReviewResult` ਵਸਤੂ ਦੇ `Result` ਗੁਣ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ।

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

`AddEdge` ਤਰੀਕੇ ਦਾ `condition` ਪੈਰਾਮੀਟਰ `WorkflowBuilder` ਨੂੰ ਇੱਕ ਸ਼ਖਸੀ ਰਾਹ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਵਰਕਫਲੋ ਕੇਵਲ ਉਸ ਵੇਲੇ `publishExecutor` ਨੂੰ ਜਾਵੇਗਾ ਜਦਿਓਂ `GetCondition(expectedResult: "Yes")` ਸੱਚਾ ਫਿਰਦਾ ਹੈ। ਨਹੀਂ ਤਾਂ, ਇਹ ਰਾਹ `sendReviewerExecutor` ਵੱਲ ਜਾਂਦਾ ਹੈ।

## ਨਤੀਜਾ

ਮਾਇਕਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਵਰਕਫਲੋ ਜਟਿਲ, ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮਾਂ ਦੇ ਓਰਕੈਸਟਰ ਕਰਨ ਲਈ ਮਜ਼ਬੂਤ ਅਤੇ ਲਚਕੀਲਾ ਬੁਨਿਆਦ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਸ ਦੇ ਗ੍ਰਾਫ ਪਰ ਆਧਾਰਿਤ ਆਰਕੀਟੈਕਚਰ ਅਤੇ ਮੁੱਖ ਭਾਗਾਂ ਨੂੰ ਵਰਤ ਕੇ ਵਿਕਾਸਕਾਰ ਸੋਫਟਵੇਅਰ ਦੀ ਡਿਜ਼ਾਈਨ ਅਤੇ ਲਾਗੂ ਕਰਨ ਲਈ ਉਚਿਤ ਵਰਕਫਲੋਜ਼ Python ਅਤੇ .NET ਦੋਹਾਂ ਵਿੱਚ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹਨ। ਚਾਹੇ ਤੁਹਾਡੀ ਐਪਲੀਕੇਸ਼ਨ ਸਧਾਰਣ ਕ੍ਰਮਿਕ ਪ੍ਰਕਿਰਿਆ, ਸਮਕਾਲੀ ਕਾਰਜਨਿ, ਜਾਂ ਗਤੀਸ਼ੀਲ ਸ਼ਰਤੀ ਲਾਜ਼ਿਕ ਦੀ ਲੋੜ ਰੱਖਦੀ ਹੋਵੇ, ਫਰੇਮਵਰਕ ਤਾਕਤਵਰ, ਸਕੇਲਬਲ, ਅਤੇ ਪ੍ਰਕਾਰ-ਸੁਰੱਖਿਅਤ AI-ਸ਼ਕਤਿਸ਼ালী ਹੱਲ ਪੈਦਾ ਕਰਨ ਦੇ ਸੰਦ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->