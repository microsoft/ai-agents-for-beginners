# Halimbawa ng Github MCP Server

## Paglalarawan

Ang demo na ito ay ginawa para sa AI Agents Hackathon na in-host ng Microsoft Reactor.

Ang mga tool ay ginagamit upang magrekomenda ng mga proyekto para sa hackathon batay sa mga repo ng isang user sa Github.
Ginagawa ito sa pamamagitan ng:

1. **Github Agent** - Ginagamit ang Github MCP Server para kunin ang mga repo at impormasyon tungkol sa mga repo na iyon.
2. **Hackathon Agent** - Kinukuha ang data mula sa Github Agent at bumubuo ng mga malikhaing ideya para sa mga proyekto ng hackathon batay sa mga proyekto, mga wika na ginamit ng user, at mga track ng proyekto para sa AI Agents hackathon.
3. **Events Agent** - Batay sa mungkahi ng hackathon agent, irerekomenda ng events agent ang mga nauugnay na kaganapan mula sa serye ng AI Agent Hackathon.
## Pagpapatakbo ng code 

### Mga Environment Variables

Gumagamit ang demo na ito ng Microsoft Agent Framework, Azure OpenAI Service, ang Github MCP Server at Azure AI Search.

Tiyaking mayroon kang wastong mga environment variable na nakaset upang magamit ang mga tool na ito:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Pagpapatakbo ng Chainlit Server

Upang kumonekta sa MCP server, gumagamit ang demo na ito ng Chainlit bilang chat interface. 

Upang patakbuhin ang server, gamitin ang sumusunod na utos sa iyong terminal:

```bash
chainlit run app.py -w
```

Dapat nitong simulan ang iyong Chainlit server sa `localhost:8000` pati na rin punuin ang iyong Azure AI Search Index gamit ang nilalaman ng `event-descriptions.md`. 

## Pagkokonekta sa MCP Server

Upang kumonekta sa Github MCP Server, piliin ang icon na "plug" sa ilalim ng chat box na "I-type ang iyong mensahe dito..":

![Kumonekta sa MCP](../../../../../translated_images/tl/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Mula doon maaari mong i-click ang "Connect an MCP" upang idagdag ang utos para kumonekta sa Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Palitan ang "[YOUR PERSONAL ACCESS TOKEN]" ng iyong aktwal na Personal Access Token. 

Pagkatapos kumonekta, dapat mong makita ang (1) sa tabi ng plug icon bilang kumpirmasyon na nakakonekta na ito. Kung hindi, subukang i-restart ang chainlit server gamit ang `chainlit run app.py -w`.

## Paggamit ng Demo 

Upang simulan ang workflow ng agent para magrekomenda ng mga proyekto sa hackathon, maaari kang mag-type ng mensahe tulad ng: 

"Magrekomenda ng mga proyekto sa hackathon para sa Github user koreyspace"

Susuriin ng Router Agent ang iyong kahilingan at tutukuyin kung aling kombinasyon ng mga agent (GitHub, Hackathon, at Events) ang pinakaangkop na hahawak sa iyong query. Nagpagtutulungan ang mga agent upang magbigay ng komprehensibong mga rekomendasyon batay sa pagsusuri ng repositoryo ng GitHub, pagbuo ng ideya para sa proyekto, at mga nauugnay na tech event.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng pagsasalin na pinapagana ng AI na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nilalayon naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinagkukunang may awtoridad. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->