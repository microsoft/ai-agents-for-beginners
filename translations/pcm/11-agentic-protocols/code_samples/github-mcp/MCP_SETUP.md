<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-11-11T14:20:59+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "pcm"
}
-->
# MCP Server Integration Guide

## Wetin you go need
- Node.js wey don dey install (version 14 or higher)
- npm package manager
- Python environment wey get all di things wey e need

## How you go set am up

1. **Install MCP Server Package**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Start MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Di server go start and show one connection URL.

3. **Check di Connection**
   - Look for di plug icon (🔌) for your Chainlit interface
   - One number (1) go show near di plug icon wey mean say connection don work well
   - Di console go show: "GitHub plugin setup completed successfully" (plus other status lines)

## How you go solve wahala

### Di wahala wey dey happen well well

1. **Port wahala**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   How you go solve am: Change di port like dis:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Authentication wahala**
   - Make sure say GitHub credentials dey set well
   - Check say di .env file get di tokens wey e need
   - Confirm say GitHub API dey work

3. **Connection no work**
   - Make sure say server dey run for di port wey you expect
   - Check firewall settings
   - Confirm say Python environment get di packages wey e need

## How you go know say connection don work

Your MCP server don connect well if:
1. Console show "GitHub plugin setup completed successfully"
2. Connection logs show "✓ MCP Connection Status: Active"
3. GitHub commands dey work for chat interface

## Environment Variables

Di ones wey you need for your .env file:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## How you go test di Connection

Send dis test message for chat:
```
Show me the repositories for username: [GitHub Username]
```
If e work well, e go show repository information.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even though we dey try make am correct, abeg make you sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->