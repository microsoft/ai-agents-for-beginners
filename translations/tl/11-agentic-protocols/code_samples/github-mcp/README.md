<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T10:57:47+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "tl"
}
-->
# Github MCP Server Example

## Deskripsyon

Ito ay isang demo na ginawa para sa AI Agents Hackathon na inorganisa ng Microsoft Reactor.

Ang tool na ito ay ginagamit upang magrekomenda ng mga proyekto para sa hackathon base sa mga Github repos ng isang user. Ginagawa ito sa pamamagitan ng:

1. **Github Agent** - Ginagamit ang Github MCP Server upang kunin ang mga repos at impormasyon tungkol sa mga ito.
2. **Hackathon Agent** - Kinukuha ang data mula sa Github Agent at nagmumungkahi ng mga malikhaing ideya para sa hackathon base sa mga proyekto, mga wika na ginamit ng user, at mga track ng proyekto para sa AI Agents hackathon.
3. **Events Agent** - Base sa mungkahi ng hackathon agent, ang events agent ay magrerekomenda ng mga kaugnay na event mula sa AI Agent Hackathon series.

## Pagpapatakbo ng Code

### Mga Environment Variable

Ang demo na ito ay gumagamit ng Azure Open AI Service, Semantic Kernel, Github MCP Server, at Azure AI Search.

Siguraduhing naitakda mo ang tamang mga environment variable upang magamit ang mga tool na ito:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Pagpapatakbo ng Chainlit Server

Upang kumonekta sa MCP server, ang demo na ito ay gumagamit ng Chainlit bilang chat interface.

Upang patakbuhin ang server, gamitin ang sumusunod na command sa iyong terminal:

```bash
chainlit run app.py -w
```

Dapat nitong simulan ang iyong Chainlit server sa `localhost:8000` pati na rin punan ang iyong Azure AI Search Index gamit ang nilalaman ng `event-descriptions.md`.

## Pagkonekta sa MCP Server

Upang kumonekta sa Github MCP Server, piliin ang icon na "plug" sa ilalim ng chat box na "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.tl.png)

Mula doon, maaari mong i-click ang "Connect an MCP" upang idagdag ang command para kumonekta sa Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Palitan ang "[YOUR PERSONAL ACCESS TOKEN]" ng iyong aktwal na Personal Access Token.

Pagkatapos kumonekta, makikita mo ang (1) sa tabi ng plug icon bilang kumpirmasyon na nakakonekta na ito. Kung hindi, subukang i-restart ang chainlit server gamit ang `chainlit run app.py -w`.

## Paggamit ng Demo

Upang simulan ang workflow ng agent sa pagrerekomenda ng mga proyekto para sa hackathon, maaari kang mag-type ng mensahe tulad ng:

"Magrekomenda ng mga proyekto para sa hackathon para sa Github user koreyspace"

Ang Router Agent ay susuriin ang iyong kahilingan at tutukuyin kung aling kombinasyon ng mga agent (GitHub, Hackathon, at Events) ang pinakaangkop upang tugunan ang iyong query. Ang mga agent ay magtutulungan upang magbigay ng komprehensibong rekomendasyon base sa pagsusuri ng Github repository, pagbuo ng ideya para sa proyekto, at mga kaugnay na tech event.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.