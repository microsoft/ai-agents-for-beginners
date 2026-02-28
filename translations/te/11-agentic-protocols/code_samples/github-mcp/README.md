# Github MCP Server ఉదాహరణ

## వివరణ

ఇది Microsoft Reactor ద్వారా నిర్వహించబడిన AI Agents హ్యాకథాన్ కోసం సృష్టించిన డెమో.

ఈ టూల్ ఒక వినియోగదారి యొక్క Github రిపోస్ ఆధారంగా హాకథాన్ ప్రాజెక్టులను సూచించడానికి ఉపయోగించబడుతుంది.
ఇది ఈ విధంగా జరుగుతుంది:

1. **Github Agent** - Github MCP సర్వర్ ఉపయోగించి రిపోజిటరీలు మరియు వాటి గురించి సమాచారం పొందుతుంది.
2. **Hackathon Agent** - Github Agent నుంచి డేటాను తీసుకుని ప్రాజెక్టులు, వినియోగదారు ఉపయోగించిన భాషలు మరియు AI Agents హ్యాకథాన్ ట్రాక్స్ ఆధారంగా సృజనాత్మక హ్యాకథాన్ ప్రాజెక్టు ఐడియాలను తయారుచేస్తుంది.
3. **Events Agent** - Hackathon Agent సూచనల ఆధారంగా, Events Agent AI Agent Hackathon సిరీస్ నుండి సంబంధిత ఈవెంట్లను సూచిస్తుంది.
## కోడ్ నడిపించడం 

### పర్యావరణ వేరియబుల్స్

ఈ డెమో Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server మరియు Azure AI Search ఉపయోగిస్తుంది.

Make sure that you have the proper environment variables set to use these tools:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit సర్వర్ నడపడం

MCP సర్వర్‌కు కనెక్ట్ అయ్యేందుకు, ఈ డెమో చాట్ ఇంటర్‌ఫేస్‌గా Chainlit ఉపయోగిస్తుంది। 

సర్వర్ నడిపడానికి, మీ టెర్మినల్లో క్రింది కమాండ్ ఉపయోగించండి:

```bash
chainlit run app.py -w
```

ఇది మీ Chainlit సర్వర్‌ను `localhost:8000` పై ప్రారంభించి, అలాగే `event-descriptions.md` కంటెంట్‌తో మీ Azure AI Search ఇండెక్స్‌ను పూరిస్తుంది। 

## MCP సర్వర్‌కు కనెక్ట్ కావడం

Github MCP Server‌కు కనెక్ట్ కావడానికి, "ఇక్కడ మీ సందేశం టైప్ చేయండి.." చాట్ బాక్స్ కింద ఉండే "ప్లగ్" ఐకాన్‌ను ఎంచుకోండి:

![MCP కనెక్ట్](../../../../../translated_images/te/mcp-chainlit-1.7ed66d648e3cfb28.webp)

అక్కడి నుంచి మీరు Github MCP Server‌కు కనెక్ట్ చేసే కమాండ్‌ను జోడించడానికి "MCP కనెక్ట్ చేయండి" పైన క్లిక్ చేయవచ్చు:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

కనెక్ట్ అయిన తర్వాత, ప్లగ్ ఐకాన్ పక్కన (1) కనిపించాలి తద్వారా అది కనెక్ట్ అయినది అని నిర్ధారించవచ్చు. కనిపించకపోతే, `chainlit run app.py -w` తో chainlit సర్వర్‌ను రీస్టార్ట్ చేయడం ప్రయత్నించండి.

## డెమో ఉపయోగించడం 

హాకథాన్ ప్రాజెక్టుల సిఫార్సులను చేసేది ఏజెంట్ వర్క్‌ఫ్లో ని ప్రారంభించడానికి, మీరు ఈ విధంగా ఒక సందేశం టైప్ చేయవచ్చు: 

"Github వినియోగదారు koreyspace కోసం హాకథాన్ ప్రాజెక్టులను సూచించండి"

Router Agent మీ అభ్యర్థనను విశ్లేషించి మీ ప్రశ్నను పరిష్కరించడానికి ఏ ఏజెంట్ల కలయిక (GitHub, Hackathon, మరియు Events) అనువైనదో నిర్ణయిస్తుంది. ఏజెంట్‌లు GitHub రిపోజిటరీ విశ్లేషణ, ప్రాజెక్ట్ ఆలోచనలు మరియు సంబంధిత టెక్ ఈవెంట్ల ఆధారంగా సమగ్ర సూచనలు ఇవ్వడానికి కలిసి పనిచేస్తాయి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
స్పష్టీకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి యత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండవచ్చు అని దయచేసి గమనించండి. అసలు పత్రాన్ని దాని స్థానిక భాషలోని అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారం కోసం వృత్తిపరమైన మానవ అనువాదాన్ని సిఫార్సు చేయబడింది. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుడు అర్థాల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->