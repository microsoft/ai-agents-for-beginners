# Github MCP ਸਰਵਰ ਉਦਾਹਰਨ

## ਵਰਣਨ

ਇਹ Microsoft Reactor ਰਾਹੀਂ ਹੋਸਟ ਕੀਤੇ AI Agents Hackathon ਲਈ ਬਣਾਈ ਗਈ ਇੱਕ ਡੈਮੋ ਸੀ।

ਇਹ ਟੂਲ ਇੱਕ ਯੂਜ਼ਰ ਦੇ Github ਰੇਪੋਜ਼ ਦੇ ਆਧਾਰ 'ਤੇ ਹੈਕਥੋਂ ਪ੍ਰੋਜੈਕਟ ਸਿਫਾਰਸ਼ਾਂ ਦੇਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।
ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:

1. **Github Agent** - Github MCP ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਰੇਪੋਜ਼ ਅਤੇ ਉਹਨਾਂ ਰੇਪੋਜ਼ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨੀ।
2. **Hackathon Agent** - Github Agent ਤੋਂ ਡਾਟਾ ਲੈਂਦਾ ਹੈ ਅਤੇ ਯੂਜ਼ਰ ਦੁਆਰਾ ਵਰਤੇ ਗਏ ਪ੍ਰੋਜੈਕਟਾਂ, ਭਾਸ਼ਾਵਾਂ ਅਤੇ AI Agents ਹੈਕਥੋਂ ਲਈ ਪ੍ਰੋਜੈਕਟ ਟ੍ਰੈਕਸ ਦੇ ਆਧਾਰ 'ਤੇ ਰਚਨਾਤਮਕ ਹੈਕਥੋਂ ਪ੍ਰੋਜੈਕਟ ਵਿਚਾਰ ਸੋਚਦਾ ਹੈ।
3. **Events Agent** - ਹੈਕਥੋਂ ਏਜੰਟ ਦੀ ਸਿਫਾਰਸ਼ ਦੇ ਆਧਾਰ 'ਤੇ, Events Agent AI Agent Hackathon ਸੀਰੀਜ਼ ਤੋਂ ਸੰਬੰਧਤ ਇਵੈਂਟ ਸੁਝਾਅ ਦੇਵੇਗਾ।
## ਕੋਡ ਨੂੰ ਚਲਾਉਣਾ 

### ਪਰੀਵਰਤਨ ਵੈਰੀਏਬਲ (Environment Variables)

ਇਸ ਡੈਮੋ ਵਿੱਚ Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server ਅਤੇ Azure AI Search ਵਰਤੇ ਗਏ ਹਨ।

ਇਨ੍ਹਾਂ ਟੂਲਜ਼ ਨੂੰ ਵਰਤਣ ਲਈ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਠੀਕ Environment Variables ਸੈਟ ਕੀਤੇ ਹੋਏ ਹਨ:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit ਸਰਵਰ ਚਲਾਉਣਾ

MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ, ਇਸ ਡੈਮੋ ਵਿੱਚ Chainlit ਨੂੰ ਇੱਕ ਚੈਟ ਇੰਟਰਫੇਸ ਵਜੋਂ ਵਰਤਿਆ ਗਿਆ ਹੈ। 

ਸਰਵਰ ਚਲਾਉਣ ਲਈ, ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕਮਾਂਡ ਵਰਤੋ:

```bash
chainlit run app.py -w
```

ਇਸ ਨਾਲ ਤੁਹਾਡਾ Chainlit ਸਰਵਰ `localhost:8000` ਤੇ ਸ਼ੁਰੂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਨਾਲ ਹੀ `event-descriptions.md` ਸਮੱਗਰੀ ਨਾਲ ਤੁਹਾਡੀ Azure AI Search Index ਭਰ ਜਾਵੇਗੀ। 

## MCP ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨਾ

Github MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ, "Type your message here.." ਚੈਟ ਬਾਕਸ ਹੇਠਾਂ ਦਿੱਤੇ "ਪਲੱਗ" ਆਈਕਨ ਨੂੰ ਚੁਣੋ:

![MCP ਨਾਲ ਜੁੜੋ](../../../../../translated_images/pa/mcp-chainlit-1.7ed66d648e3cfb28.webp)

ਉਥੋਂ ਤुਸੀਂ "Connect an MCP" 'ਤੇ ਕਲਿੱਕ ਕਰਕੇ Github MCP ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਦਾ ਕਮਾਂਡ ਜੋੜ ਸਕਦੇ ਹੋ:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

ਕਨੈਕਟ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਪੁਸ਼ਟੀ ਲਈ ਪਲੱਗ ਆਈਕਨ ਦੇ ਨਜ਼ਦੀਕ ਇੱਕ (1) ਵੇਖਣ ਨੂੰ ਮਿਲਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਇਹ ਕਨੈਕਟ ਹੋ ਗਿਆ ਹੈ। ਜੇ ਨਹੀਂ, ਤਾਂ `chainlit run app.py -w` ਨਾਲ chainlit ਸਰਵਰ ਨੂੰ ਮੁੜ ਸ਼ੁਰੂ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ।

## ਡੈਮੋ ਦੀ ਵਰਤੋਂ

ਹੈਕਥੋਂ ਪ੍ਰੋਜੈਕਟਾਂ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਨ ਵਾਲੀ ਏਜੰਟ ਵਰਕਫਲੋ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਸੀਂ ਇਹਨਾਂ ਵਰਗਾ ਸੁਨੇਹਾ ਲਿਖ ਸਕਦੇ ਹੋ: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent ਤੁਹਾਡੀ ਬੇਨਤੀ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੇਗਾ ਅਤੇ ਨਿਰਧਾਰਤ کرےਗਾ ਕਿ ਕਿਹੜਾ ਏਜੰਟਸ (GitHub, Hackathon, ਅਤੇ Events) ਦਾ ਕੌਨ-सा ਮਿੱਕਸ ਤੁਹਾਡੇ ਪ੍ਰਸ਼ਨ ਨੂੰ ਸਾਂਭਣ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਹੈ। ਏਜੰਟ ਇਕੱਠੇ ਕੰਮ ਕਰਦੇ ਹਨ ਤਾਂ ਜੋ GitHub ਰੇਪੋਜ਼ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ, ਪ੍ਰੋਜੈਕਟ ਆਈਡੀਏਸ਼ਨ ਅਤੇ ਸੰਬੰਧਤ ਟੈਕ ਇਵੈਂਟਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਵਿਸਤ੍ਰਿਤ ਸਿਫਾਰਸ਼ਾਂ ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਜਾ ਸਕਣ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ਅਸਵੀਕਾਰ:
ਇਹ ਦਸਤਾਵੇਜ਼ ਏ.ਆਈ. ਅਨੁਵਾਦ ਸੇਵਾ Co-op Translator (https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਗੰਭੀਰ ਜਾਂ ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->