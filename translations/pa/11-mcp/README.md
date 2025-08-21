<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:16:46+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "pa"
}
-->
# ਪਾਠ 11: ਮਾਡਲ ਕੌਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਇੰਟੀਗ੍ਰੇਸ਼ਨ

## ਮਾਡਲ ਕੌਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਦਾ ਪਰਚੇ

ਮਾਡਲ ਕੌਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਇੱਕ ਅਧੁਨਿਕ ਫਰੇਮਵਰਕ ਹੈ ਜੋ AI ਮਾਡਲਾਂ ਅਤੇ ਕਲਾਇੰਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਵਿਚਕਾਰ ਸੰਚਾਰ ਨੂੰ ਮਿਆਰੀ ਬਣਾਉਣ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ। MCP AI ਮਾਡਲਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਵਰਤਣ ਵਾਲੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਵਿਚਕਾਰ ਇੱਕ ਪੁਲ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ, ਜੋ ਕਿ ਮਾਡਲ ਦੇ ਅਧਾਰਤ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਤੋਂ ਬਿਨਾਂ ਇੱਕ ਸਥਿਰ ਇੰਟਰਫੇਸ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

MCP ਦੇ ਮੁੱਖ ਪੱਖ:

- **ਮਿਆਰੀਕ੍ਰਿਤ ਸੰਚਾਰ**: MCP ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ AI ਮਾਡਲਾਂ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ ਇੱਕ ਸਾਂਝੀ ਭਾਸ਼ਾ ਸਥਾਪਿਤ ਕਰਦਾ ਹੈ  
- **ਉੱਨਤ ਕੌਂਟੈਕਸਟ ਪ੍ਰਬੰਧਨ**: AI ਮਾਡਲਾਂ ਨੂੰ ਸੰਦਰਭ ਜਾਣਕਾਰੀ ਨੂੰ ਕੁਸ਼ਲਤਾਪੂਰਵਕ ਪਾਸ ਕਰਨ ਦੀ ਸਹੂਲਤ ਦਿੰਦਾ ਹੈ  
- **ਕਰਾਸ-ਪਲੇਟਫਾਰਮ ਅਨੁਕੂਲਤਾ**: C#, Java, JavaScript, Python, ਅਤੇ TypeScript ਸਮੇਤ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਕੰਮ ਕਰਦਾ ਹੈ  
- **ਸੁਗਮ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ AI ਮਾਡਲਾਂ ਨੂੰ ਆਪਣੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਆਸਾਨੀ ਨਾਲ ਸ਼ਾਮਲ ਕਰਨ ਦੀ ਸਹੂਲਤ ਦਿੰਦਾ ਹੈ  

MCP ਖਾਸ ਤੌਰ 'ਤੇ AI ਏਜੰਟ ਵਿਕਾਸ ਵਿੱਚ ਕੀਮਤੀ ਹੈ ਕਿਉਂਕਿ ਇਹ ਏਜੰਟਾਂ ਨੂੰ ਇੱਕ統一 ਪ੍ਰੋਟੋਕੋਲ ਰਾਹੀਂ ਵੱਖ-ਵੱਖ ਸਿਸਟਮਾਂ ਅਤੇ ਡਾਟਾ ਸਰੋਤਾਂ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਦੀ ਸਹੂਲਤ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਏਜੰਟ ਹੋਰ ਲਚਕੀਲੇ ਅਤੇ ਸ਼ਕਤੀਸ਼ਾਲੀ ਬਣਦੇ ਹਨ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼
- MCP ਕੀ ਹੈ ਅਤੇ AI ਏਜੰਟ ਵਿਕਾਸ ਵਿੱਚ ਇਸ ਦੀ ਭੂਮਿਕਾ ਨੂੰ ਸਮਝੋ  
- GitHub ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ ਇੱਕ MCP ਸਰਵਰ ਸੈਟਅੱਪ ਅਤੇ ਕਨਫਿਗਰ ਕਰੋ  
- MCP ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਬਣਾਓ  
- Azure Cognitive Search ਨਾਲ RAG (Retrieval Augmented Generation) ਲਾਗੂ ਕਰੋ  

## ਪੂਰਵ ਸ਼ਰਤਾਂ
- Python 3.8+  
- Node.js 14+  
- Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ  
- GitHub ਖਾਤਾ  
- Semantic Kernel ਦੀ ਬੁਨਿਆਦੀ ਸਮਝ  

## ਸੈਟਅੱਪ ਨਿਰਦੇਸ਼

1. **ਮਾਹੌਲ ਸੈਟਅੱਪ**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```  

2. **Azure ਸੇਵਾਵਾਂ ਕਨਫਿਗਰ ਕਰੋ**  
   - ਇੱਕ Azure Cognitive Search ਸਰੋਤ ਬਣਾਓ  
   - Azure OpenAI ਸੇਵਾ ਸੈਟਅੱਪ ਕਰੋ  
   - `.env` ਵਿੱਚ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਕਨਫਿਗਰ ਕਰੋ  

3. **MCP ਸਰਵਰ ਸੈਟਅੱਪ**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```  

## ਪ੍ਰੋਜੈਕਟ ਸਟ੍ਰਕਚਰ

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```  

## ਮੁੱਖ ਘਟਕੇ

### 1. ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ  
- GitHub ਏਜੰਟ: ਰਿਪੋਜ਼ਟਰੀ ਵਿਸ਼ਲੇਸ਼ਣ  
- ਹੈਕਾਥਾਨ ਏਜੰਟ: ਪ੍ਰੋਜੈਕਟ ਸਿਫਾਰਸ਼ਾਂ  
- ਇਵੈਂਟਸ ਏਜੰਟ: ਟੈਕਨੋਲੋਜੀ ਇਵੈਂਟ ਸੁਝਾਅ  

### 2. Azure ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
- ਇਵੈਂਟ ਇੰਡੈਕਸਿੰਗ ਲਈ Cognitive Search  
- ਏਜੰਟ ਇੰਟੈਲੀਜੈਂਸ ਲਈ Azure OpenAI  
- RAG ਪੈਟਰਨ ਲਾਗੂ ਕਰਨਾ  

### 3. MCP ਟੂਲਜ਼  
- GitHub ਰਿਪੋਜ਼ਟਰੀ ਵਿਸ਼ਲੇਸ਼ਣ  
- ਕੋਡ ਇੰਸਪੈਕਸ਼ਨ  
- ਮੈਟਾਡਾਟਾ ਐਕਸਟ੍ਰੈਕਸ਼ਨ  

## ਕੋਡ ਵਾਕਥਰੂ

ਸੈਂਪਲ ਵਿੱਚ ਦਰਸਾਇਆ ਗਿਆ ਹੈ:  
1. MCP ਸਰਵਰ ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
2. ਮਲਟੀ-ਏਜੰਟ ਆਰਕੇਸਟਰੈਸ਼ਨ  
3. Azure Cognitive Search ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
4. RAG ਪੈਟਰਨ ਲਾਗੂ ਕਰਨਾ  

ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ:  
- ਰੀਅਲ-ਟਾਈਮ GitHub ਰਿਪੋਜ਼ਟਰੀ ਵਿਸ਼ਲੇਸ਼ਣ  
- ਸਮਰਥ ਪ੍ਰੋਜੈਕਟ ਸਿਫਾਰਸ਼ਾਂ  
- Azure Search ਦੀ ਵਰਤੋਂ ਨਾਲ ਇਵੈਂਟ ਮੈਚਿੰਗ  
- Chainlit ਨਾਲ ਸਟ੍ਰੀਮਿੰਗ ਰਿਸਪਾਂਸਜ਼  

## ਸੈਂਪਲ ਚਲਾਉਣਾ

ਵੇਰਵੇਦਾਰ ਸੈਟਅੱਪ ਨਿਰਦੇਸ਼ਾਂ ਅਤੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, [Github MCP Server Example README](./code_samples/github-mcp/README.md) ਨੂੰ ਵੇਖੋ।  

1. MCP ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  

2. ਐਪਲੀਕੇਸ਼ਨ ਲਾਂਚ ਕਰੋ:  
   ```bash
   chainlit run app.py -w
   ```  

3. ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```  

## ਸਮੱਸਿਆ ਹੱਲ

ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ:  
1. MCP ਕਨੈਕਸ਼ਨ ਸਮੱਸਿਆਵਾਂ  
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ  
   - ਪੋਰਟ ਉਪਲਬਧਤਾ ਦੀ ਜਾਂਚ ਕਰੋ  
   - GitHub ਟੋਕਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ  

2. Azure Search ਸਮੱਸਿਆਵਾਂ  
   - ਕਨੈਕਸ਼ਨ ਸਟ੍ਰਿੰਗਜ਼ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ  
   - ਇੰਡੈਕਸ ਮੌਜੂਦਗੀ ਦੀ ਜਾਂਚ ਕਰੋ  
   - ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ  

## ਅਗਲੇ ਕਦਮ
- ਹੋਰ MCP ਟੂਲਜ਼ ਦੀ ਖੋਜ ਕਰੋ  
- ਕਸਟਮ ਏਜੰਟ ਲਾਗੂ ਕਰੋ  
- RAG ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਵਧਾਓ  
- ਹੋਰ ਇਵੈਂਟ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰੋ  
- **ਅਡਵਾਂਸਡ**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) ਵਿੱਚ ਏਜੰਟ-ਟੂ-ਏਜੰਟ ਕਮਿਊਨਿਕੇਸ਼ਨ ਦੇ ਉਦਾਹਰਣ ਵੇਖੋ  

## ਸਰੋਤ
- [MCP ਲਈ ਸ਼ੁਰੂਆਤੀ ਗਾਈਡ](https://aka.ms/mcp-for-beginners)  
- [MCP ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search ਡੌਕਸ](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel ਗਾਈਡਸ](https://learn.microsoft.com/semantic-kernel/)  

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਭਵਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।