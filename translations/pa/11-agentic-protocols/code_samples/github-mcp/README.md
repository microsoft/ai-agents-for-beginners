# Github MCP ਸਰਵਰ ਉਦਾਹਰਣ

## ਵਰਣਨ

ਇਹ Microsoft Reactor ਵੱਲੋਂ ਹੋਸਟ ਕੀਤੇ ਗਏ AI Agents ਹੈਕਾਥੌਨ ਲਈ ਬਣਾਈ ਗਈ ਇੱਕ ਡੈਮੋ ਸੀ।

ਇਹ ਟੂਲ ਉਪਭੋਗਤਾ ਦੇ Github ਰਿਪੋਜ਼ ਦੇ ਆਧਾਰ 'ਤੇ ਹੈਕਾਥੌਨ ਪ੍ਰੋਜੈਕਟ ਸਿਫਾਰਸ਼ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।
ਇਹ ਹੇਠ ਲਿਖੇ ਤਰੀਕੇ ਨਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:

1. **Github Agent** - GitHub MCP ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਰਿਪੋਜ਼ ਅਤੇ ਉਨ੍ਹਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨਾ।
2. **Hackathon Agent** - Github Agent ਤੋਂ ਡੇਟਾ ਲੈ ਕੇ ਪ੍ਰੋਜੈਕਟਾਂ, ਉਪਭੋਗਤਾ ਵਲੋਂ ਵਰਤੀ ਗਈਆਂ ਭਾਸ਼ਾਵਾਂ ਅਤੇ AI Agents ਹੈਕਾਥੌਨ ਦੇ ਪ੍ਰੋਜੈਕਟ ਟ੍ਰੈਕਸ ਦੇ ਆਧਾਰ 'ਤੇ ਰਚਨਾਤਮਕ ਹੈਕਾਥੌਨ ਪ੍ਰੋਜੈਕਟ ਵਿਚਾਰ ਤਿਆਰ ਕਰਦਾ ਹੈ।
3. **Events Agent** - Hackathon Agent ਦੀ ਸੁਝਾਵ ਦੇ ਆਧਾਰ 'ਤੇ, Events Agent AI Agent Hackathon ਸਿਰੀਜ਼ ਵਿੱਚੋਂ ਸਬੰਧਤ ਇਵੈਂਟ ਸੁਝਾਅ ਦੇਵੇਗਾ।
## Running the code 

### ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

ਇਸ ਡੈਮੋ ਵਿੱਚ Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server ਅਤੇ Azure AI Search ਵਰਤੇ ਗਏ ਹਨ।

ਇਹਨਾਂ ਟੂਲਾਂ ਨੂੰ ਵਰਤਣ ਲਈ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਸਹੀ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕੀਤੇ ਹੋਏ ਹਨ:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

MCP ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਲਈ, ਇਹ ਡੈਮੋ ਚੈਟ ਇੰਟਰਫੇਸ ਵਜੋਂ Chainlit ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। 

ਸਰਵਰ ਚਲਾਉਣ ਲਈ, ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕਮਾਂਡ ਵਰਤੋਂ:

```bash
chainlit run app.py -w
```

ਇਸ ਨਾਲ ਤੁਹਾਡਾ Chainlit ਸਰਵਰ `localhost:8000` ਉੱਤੇ ਸ਼ੁਰੂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਨਾਲ ਹੀ ਤੁਹਾਡੇ Azure AI Search Index ਨੂੰ `event-descriptions.md` ਸਮੱਗਰੀ ਨਾਲ ਭਰਨਾ ਚਾਹੀਦਾ ਹੈ। 

## MCP ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨਾ

Github MCP Server ਨਾਲ ਜੁੜਨ ਲਈ, "Type your message here.." ਚੈਟ ਬਾਕਸ ਦੇ ਹੇਠਾਂ ਵਾਲੇ "plug" ਆਇਕਨ ਨੂੰ ਚੁਣੋ:

![MCP ਕਨੈਕਟ](../../../../../translated_images/pa/mcp-chainlit-1.7ed66d648e3cfb28.webp)

ਉੱਥੇ ਤੋਂ ਤੁਸੀਂ "Connect an MCP" 'ਤੇ ਕਲਿੱਕ ਕਰ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ Github MCP Server ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਲਈ ਕਮਾਂਡ ਸ਼ਾਮਲ ਕੀਤੀ ਜਾ ਸਕੇ:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

ਕਨੈਕਟ ਕਰਨ ਤੋਂ ਬਾਅਦ, plug ਆਈਕਨ ਦੇ ਕੋਲ (1) ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ ਤਾਂ ਜੋ ਇਹ ਪੱਕਾ ਹੋ ਸਕੇ ਕਿ ਇਹ ਜੁੜਿਆ ਹੋਇਆ ਹੈ। ਜੇ ਨਹੀਂ, ਤਾਂ chainlit ਸਰਵਰ ਨੂੰ `chainlit run app.py -w` ਨਾਲ ਰੀਸਟਾਰਟ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ।

## ਡੈਮੋ ਵਰਤਣਾ 

ਹੈਕਾਥੌਨ ਪ੍ਰੋਜੈਕਟਾਂ ਦੀ ਸੁਿਫਾਰਸ਼ ਕਰਨ ਵਾਲੇ ਏਜੰਟ ਵਰਕਫਲੋ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਸੀਂ ਹੇਠਾਂ ਵਰਗਾ ਸੁਨੇਹਾ ਟਾਈਪ ਕਰ ਸਕਦੇ ਹੋ: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent ਤੁਹਾਡੀ ਬੇਨਤੀ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੇਗਾ ਅਤੇ ਨਿਰਣੇ ਕਰੇਗਾ ਕਿ ਤੁਹਾਡੇ ਸਵਾਲ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਕਿਹੜਾ ਏਜੰਟਾਂ ਦਾ ਸੰਯੋਜਨ (GitHub, Hackathon, ਅਤੇ Events) ਸਭ ਤੋਂ ਉਚਿਤ ਹੈ। ਇਹ ਏਜੰਟ GitHub repository ਵਿਸ਼ਲੇਸ਼ਣ, ਪ੍ਰੋਜੈਕਟ ਵਿਚਾਰਾਂ ਅਤੇ ਸਬੰਧਤ ਟੈਕ ਇਵੈਂਟਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਵਿਸਤ੍ਰਿਤ ਸਿਫਾਰਸ਼ਾਂ ਪ੍ਰਦਾਨ ਕਰਨ ਲਈ ਇਕੱਠੇ ਕੰਮ ਕਰਦੇ ਹਨ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ਅਸਵੀਕਾਰਨਾਮਾ:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ (AI) ਅਨੁਵਾਦ ਸੇਵਾ Co-op Translator (https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸਹੀਅਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਤ੍ਰੁੱਟੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਉਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->