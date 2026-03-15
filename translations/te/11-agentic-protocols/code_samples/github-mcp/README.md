# Github MCP Server ఉదాహరణ

## వివరణ

ఇది Microsoft Reactor ద్వారా నిర్వహించిన AI Agents హాకథాన్ కోసం రూపొందించిన ఒక డెమో.

టూల్‌లు వినియోగదారుని Github రీపోస్ ఆధారంగా హాకథాన్ ప్రాజెక్టులను సూచించడానికి ఉపయోగిస్తారు.
ఇది క్రిందివిధంగా చేయబడుతుంది:

1. **Github Agent** - Github MCP Server ఉపయోగించి రీపోస్ మరియు వాటి గురించి సమాచారాన్ని పొందడం.
2. **Hackathon Agent** - Github Agent నుండి డేటాను తీసుకుని ప్రాజెక్టులు, వినియోగదారు ఉపయోగించిన భాషలు మరియు AI Agents హాకథాన్ యొక్క ప్రాజెక్ట్ ట్రాక్స్ ఆధారంగా క్రియేటివ్ హాకథాన్ ప్రాజెక్ట్ ఐడియాలను రూపొందిస్తుంది.
3. **Events Agent** - హాకథాన్ ఏజెంట్ సూచన ఆధారంగా, Events Agent AI Agent Hackathon శ్రేణి నుండి సంబంధిత ఈవెంట్‌లు సూచిస్తుంది.

## కోడ్ నడపడం 

### పరిసర వేరియబుల్స్

ఈ డెమో Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server మరియు Azure AI Search ఉపయోగిస్తుంది.

ఈ టూల్‌లను ఉపయోగించేందుకు మీకు సరైన ఎన్విరన్మెంట్ వేరియబుల్స్ సెట్ చేయబడినట్లు నిర్ధారించుకోండి:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit సర్వర్ నడపడం

MCP సర్వర్‌కు కనెక్ట్ అయ్యేందుకు, ఈ డెమో చాట్ ఇంటర్‌ఫేస్ కోసం Chainlit ఉపయోగిస్తుంది। 

సర్వర్‌ను నడపడానికి, మీ టెర్మినల్‌లో క్రింది కమాండ్‌ను ఉపయోగించండి:

```bash
chainlit run app.py -w
```

ఇది మీ Chainlit సర్వర్‌ను `localhost:8000`లో ప్రారంభిస్తుంది మరియు `event-descriptions.md` కంటెంట్‌తో మీ Azure AI Search ఇండెక్స్‌ను కూడా నింపుతుంది. 

## MCP సర్వర్‌కు కనెక్ట్ అవ్వడం

Github MCP Server‌కు కనెక్ట్ కావడానికి, "మీ సందేశాన్ని ఇక్కడ టైప్ చేయండి.." చాట్ బాక్స్ దిగువ ఉన్న "ప్లగ్" ఐకాన్‌ను ఎంచుకోండి:

![MCP కనెక్ట్](../../../../../translated_images/te/mcp-chainlit-1.7ed66d648e3cfb28.webp)

అక్కడి నుండి మీరు "Connect an MCP" పై క్లిక్ చేసి Github MCP Serverకు కనెక్ట్ అయ్యే కమాండ్‌ను జోడించవచ్చు:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

కనెక్ట్ చేసిన తర్వాత, అది కనెక్ట్ అయిందని నిర్ధారించడానికి మీరు ప్లగ్ ఐకాన్ పక్కన (1) కనిపిస్తుందని చూడగలరు. లేకపోతే, chainlit సర్వర్‌ను `chainlit run app.py -w` కమాండ్‌తో రీస్టార్ట్ చేయండి.

## డెమో ఉపయోగించడం

హాకథాన్ ప్రాజెక్టులను సూచించే ఏజెంట్ వర్క్‌ఫ్లో ప్రారంభించడానికి, మీరు క్రింది విధంగా సందేశాన్ని టైప్ చేయవచ్చు: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent మీ అభ్యర్థనను విశ్లేషించి మీ క్వెరీను నిర్వహించడానికి ఏ ఏజెంట్ల సంకలనం (GitHub, Hackathon, మరియు Events) ఉత్తమంగా అనువైనదో నిర్ణయిస్తుంది. ఏజెంట్లు కలిసి GitHub రిపోజిటరీ విశ్లేషణ, ప్రాజెక్ట్ ఆలోచనలు మరియు సంబంధిత టెక్ ఈవెంట్స్ ఆధారంగా సమగ్ర సిఫార్సులను అందిస్తాయి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటిక్ అనువాదాల్లో తప్పులు లేదా పొరపాట్లు ఉండే అవకాశం ఉందని దయచేసి గమనించండి. మౌలిక పత్రాన్ని దాని స్వదేశీ భాషలో ఉన్న అసలు సంచికను అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం ప్రొఫెషనల్ మానవ అనువాదాన్ని సూచిస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వలన ఏర్పడే ఏవైనా అవగాహనా లోపాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->