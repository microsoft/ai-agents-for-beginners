# Github MCP Server ಉದಾಹರಣೆ

## ವಿವರಣೆ

ಈ ಡೆಮೋವನ್ನು Microsoft Reactor ಮೂಲಕ ಆಯೋಜಿಸಲಾದ AI Agents Hackathon ಗಾಗಿ ರಚಿಸಲಾಯಿತು.

ಈ ಟೂಲ್ ಅನ್ನು ಬಳಕೆದಾರನ Github ರೆಪೊಗಳ ಆಧಾರದ ಮೇಲೆ ಹ್ಯಾಕಾಥಾನ್ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳನ್ನು ಶಿಫಾರಸು ಮಾಡಲು ಬಳಸಲಾಗುತ್ತದೆ.
ಇದು ಕೆಳಗಿನಂತೆ ನಡೆಯುತ್ತದೆ:

1. **Github Agent** - Github MCP Server ನನ್ನು ಬಳಸಿ ರೆಪೊಗಳು ಮತ್ತು ಅವುಗಳ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯುವುದು.
2. **Hackathon Agent** - Github Agent ನಿಂದ ಡೇಟಾವನ್ನು ತೆಗೆದು ಬಳಕೆದಾರನ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳು, ಬಳಸದ ಭಾಷೆಗಳು ಮತ್ತು AI Agents ಹ್ಯಾಕಥಾನ್‌ನ ಪ್ರಾಜೆಕ್ಟ್ ಟ್ರ್ಯಾಕ್ಸ್ ಆಧಾರವಾಗಿ ಸೃಜನಶೀಲ ಹ್ಯಾಕಥಾನ್ ಪ್ರಾಜೆಕ್ಟ್ ಐಡಿಯಾಗಳನ್ನು ರಚಿಸುತ್ತದೆ.
3. **Events Agent** - Hackathon Agent ನ ಸಲಹೆಗಳ ಆಧಾರದಲ್ಲಿ, Events Agent AI Agent Hackathon ಸರಣಿಯಿಂದ ಸಂಬಂಧಿತ ಕಾರ್ಯಕ್ರಮಗಳನ್ನು ಶಿಫಾರಸು ಮಾಡುತ್ತದೆ.

## ಕೋಡ್ ಅನ್ನು ಚಲಾಯಿಸುವುದು 

### ಪರಿಸರ ಚರಗಳು

ಈ ಡೆಮೊ Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server ಮತ್ತು Azure AI Search ಅನ್ನು ಬಳಸುತ್ತದೆ.

ಈ ಟೂಲ್ಗಳನ್ನು ಬಳಸಲು ಸರಿಯಾದ ಪರಿಸರ ಚರಗಳನ್ನು ಹೊಂದಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit ಸರ್ವರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡುವುದು

MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸಲು, ಈ ಡೆಮೊ Chainlit ಅನ್ನು ಚಾಟ್ ಇಂಟರ್‌ಫೇಸ್ ಆಗಿ ಬಳಸುತ್ತದೆ. 

ಸರ್ವರ್ ಅನ್ನು ರನ್ ಮಾಡಲು, ನಿಮ್ಮ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು ಬಳಸಿ:

```bash
chainlit run app.py -w
```

ಇದು ನಿಮ್ಮ Chainlit ಸರ್ವರ್ ಅನ್ನು `localhost:8000` ನಲ್ಲಿ ಪ್ರಾರಂಭಿಸಬೇಕು ಮತ್ತು ನಿಮ್ಮ Azure AI Search Index ಅನ್ನು `event-descriptions.md` ವಿಷಯದಿಂದ ಭರ್ತಿ ಮಾಡಬೇಕು. 

## MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸುವುದು

Github MCP Server ಗೆ ಸಂಪರ್ಕಿಸಲು, "Type your message here.." ಚಾಟ್ ಬಾಕ್ಸ್‌ಕೆ ಕೆಳಗಿರುವ "plug" ಐಕಾನ್ ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ:

![MCP ಸಂಪರ್ಕ](../../../../../translated_images/kn/mcp-chainlit-1.7ed66d648e3cfb28.webp)

ಅಲ್ಲಿ ನೀವು "Connect an MCP" ಕ್ಲಿಕ್ ಮಾಡಿ Github MCP Server ಗೆ ಸಂಪರ್ಕಿಸಲು ಆ ಕಮಾಂಡ್ ಅನ್ನು ಸೇರಿಸಬಹುದು:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

ಸಂಪರ್ಕಿಸಿದ ನಂತರ, ಅದರ ಸಂಪರ್ಕವನ್ನು ದೃಢೀಕರಿಸಲು plug ಐಕಾನ್ ಬದಿಯಲ್ಲಿ (1) ಕಾಣಿಸಬೇಕು. ಇಲ್ಲದಿದ್ದರೆ, chainlit ಸರ್ವರ್ ಅನ್ನು `chainlit run app.py -w` ಮೂಲಕ ಮರುಪ್ರಾರಂಭಿಸುವುದನ್ನು ಪ್ರಯತ್ನಿಸಿ.

## ಡೆಮೊ ಬಳಸುವುದು 

ಹ್ಯಾಕಥಾನ್ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳನ್ನು ಶಿಫಾರಸು ಮಾಡುವ ಏಜೆಂಟ್ ವರ್ಕ್‌ಫ್ಲೋವನ್ನು ಪ್ರಾರಂಭಿಸಲು, ನೀವು ಹೀಗೊಂದು ಸಂದೇಶವನ್ನು ಟೈಪ್ ಮಾಡಬಹುದು: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent ನಿಮ್ಮ ವಿನಂತಿಯನ್ನು ವಿಶ್ಲೇಷಿಸಿ, ಯಾವ ಏಜೆಂಟ್‌ಗಳ ಸಂಯೋಜನೆ (GitHub, Hackathon, ಮತ್ತು Events) ನಿಮ್ಮ ಕೇಳಿಕೆಗೆ ಅತ್ಯುತ್ತಮವಾಗಿ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆಎಂದು ನಿರ್ಧರಿಸುತ್ತದೆ. ಏಜೆಂಟ್‌ಗಳು GitHub ರೆಪೊ ವಿಶ್ಲೇಷಣೆ, ಪ್ರಾಜೆಕ್ಟ್ ಆಲೋಚನೆ ಮತ್ತು ಸಂಬಂಧಿತ ತಾಂತ್ರಿಕ ಕಾರ್ಯಕ್ರಮಗಳ ಆಧಾರದಲ್ಲಿ ಸಂಪೂರ್ಣ ಶಿಫಾರಸುಗಳನ್ನು ಒದಗಿಸಲು ಒಟ್ಟಿಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಭಾಷಾಂತರ ಸೇವೆ ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ ಸಹ, ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸೂಕ್ಷ್ಮತೆಗಳು ಇರಬಹುದೆಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿನ ಅಸಲಿ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅಸಮಜ್ಞತೆಗಳು ಅಥವಾ ತಪ್ಪು ಅನುವಾದಗಳಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರಿಯಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->