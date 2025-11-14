<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T11:05:31+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "tl"
}
-->
# Gabay sa Integrasyon ng MCP Server

## Mga Kinakailangan
- Nakainstall na Node.js (bersyon 14 o mas mataas)
- npm package manager
- Python environment na may mga kinakailangang dependencies

## Mga Hakbang sa Setup

1. **I-install ang MCP Server Package**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Simulan ang MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Dapat magsimula ang server at magpakita ng connection URL.

3. **I-verify ang Koneksyon**
   - Hanapin ang icon ng plug (🔌) sa iyong Chainlit interface  
   - Dapat lumitaw ang numero (1) sa tabi ng plug icon na nagpapahiwatig ng matagumpay na koneksyon  
   - Ang console ay dapat magpakita ng: "GitHub plugin setup completed successfully" (kasama ang iba pang status lines)

## Pag-aayos ng Problema

### Karaniwang Isyu

1. **Port Conflict**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Solusyon: Palitan ang port gamit ang:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Mga Isyu sa Authentication**
   - Siguraduhing maayos ang pagkaka-configure ng GitHub credentials  
   - Suriin kung ang .env file ay naglalaman ng mga kinakailangang token  
   - I-verify ang access sa GitHub API

3. **Nabigong Koneksyon**
   - Siguraduhing tumatakbo ang server sa inaasahang port  
   - Suriin ang mga setting ng firewall  
   - I-verify kung ang Python environment ay may mga kinakailangang package

## Pag-verify ng Koneksyon

Ang iyong MCP server ay maayos na nakakonekta kapag:  
1. Ang console ay nagpapakita ng "GitHub plugin setup completed successfully"  
2. Ang connection logs ay nagpapakita ng "✓ MCP Connection Status: Active"  
3. Gumagana ang mga utos ng GitHub sa chat interface

## Mga Environment Variable

Kinakailangan sa iyong .env file:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Pagsubok ng Koneksyon

Magpadala ng test message sa chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Ang matagumpay na tugon ay magpapakita ng impormasyon ng repository.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.