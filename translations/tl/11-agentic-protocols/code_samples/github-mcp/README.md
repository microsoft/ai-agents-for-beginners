# Github MCP Server Halimbawa

## Paglalarawan

Ang demo na ito ay ginawa para sa AI Agents Hackathon na in-host ng Microsoft Reactor.

Ginagamit ang mga tool para magrekomenda ng mga proyekto para sa hackathon batay sa mga repo ng isang gumagamit sa Github.
Ginagawa ito sa pamamagitan ng:

1. **Github Agent** - Gumagamit ng Github MCP Server para kunin ang mga repo at impormasyon tungkol sa mga repo na iyon.
2. **Hackathon Agent** - Kinukuha ang data mula sa Github Agent at bumubuo ng mga malikhaing ideya ng proyekto para sa hackathon batay sa mga proyekto, mga wika na ginamit ng gumagamit, at mga project track para sa AI Agents hackathon.
3. **Events Agent** - Batay sa mungkahi ng hackathon agent, magrerekomenda ang events agent ng mga kaugnay na kaganapan mula sa serye ng AI Agent Hackathon.

## Patakbuhin ang code 

### Mga Variable ng Kapaligiran

Gumagamit ang demo na ito ng Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server at Azure AI Search.

Tiyaking naka-set ang mga wastong variable ng kapaligiran upang magamit ang mga tool na ito:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Pagpapatakbo ng Chainlit Server

Upang kumonekta sa MCP server, ang demo na ito ay gumagamit ng Chainlit bilang isang chat interface. 

Upang patakbuhin ang server, gamitin ang sumusunod na utos sa iyong terminal:

```bash
chainlit run app.py -w
```

Dapat nito simulan ang iyong Chainlit server sa `localhost:8000` pati na rin mapunan ang iyong Azure AI Search Index ng nilalaman ng `event-descriptions.md`. 

## Pagkonekta sa MCP Server

Upang kumonekta sa Github MCP Server, piliin ang icon na "plug" sa ilalim ng chat box na "I-type ang iyong mensahe dito..":

![Kumonekta sa MCP](../../../../../translated_images/tl/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Mula doon maaari mong i-click ang "Kumonekta ng MCP" upang idagdag ang command para kumonekta sa Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Palitan ang "[YOUR PERSONAL ACCESS TOKEN]" ng iyong aktwal na Personal Access Token. 

Pagkatapos kumonekta, dapat mong makita ang (1) sa tabi ng icon na plug bilang pag-confirm na ito ay nakakonekta. Kung hindi, subukang i-restart ang chainlit server gamit ang `chainlit run app.py -w`.

## Paggamit ng Demo 

Upang simulan ang workflow ng agent para sa pagrerekomenda ng mga proyekto para sa hackathon, maaari kang mag-type ng isang mensahe tulad ng: 

"Magrekomenda ng mga proyekto para sa hackathon para sa Github user koreyspace"

Susuriin ng Router Agent ang iyong kahilingan at tutukuyin kung aling kombinasyon ng mga agent (GitHub, Hackathon, at Events) ang pinakaangkop para hawakan ang iyong katanungan. Nagkakatuwang gumagana ang mga agent upang magbigay ng komprehensibong mga rekomendasyon batay sa pagsusuri ng repositoryo sa GitHub, pagbuo ng ideya ng proyekto, at mga kaugnay na tech na kaganapan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Isinalin ang dokumentong ito gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsisikap kami na maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mga kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na magmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->