# Github MCP Server உதாரணம்

## விளக்கம்

இது Microsoft Reactor மூலம் நடத்தப்பட்ட AI Agents Hackathon க்காக உருவாக்கப்பட்ட ஒரு டெமோ.

இந்த கருவி பயனரின் Github ரெப்போக்களின் அடிப்படையில் ஹேக்கதான் திட்டங்களை பரிந்துரைக்க பயன்படுகிறது.
இது பின்வருமாறு செயப்படும்:

1. **Github Agent** - ரெப்போக்களையும் அவற்றின் தகவல்களையும் பெற Github MCP Server-ஐ பயன்படுத்துகிறது.
2. **Hackathon Agent** - Github Agent-இருந்து தரவை எடுத்துக்கொண்டு, திட்டங்கள், பயனர் பயன்படுத்திய மொழிகள் மற்றும் AI Agents hackathon இன் டிராக்குகள் அடிப்படையில் படைப்பாற்றல் நிறைந்த ஹேக்கதான் திட்ட யோசனைகள் உருவாக்குகிறது.
3. **Events Agent** - Hackathon Agent-ன் பரிந்துரையின் அடிப்படையில், Events Agent AI Agent Hackathon தொடர் சார்ந்த தொடர்புடைய நிகழ்வுகளை பரிந்துரைக்கும்.

## குறியீட்டை இயக்குதல் 

### சூழல் மாறிலிகள்

இந்த டெமோ Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server மற்றும் Azure AI Search ஐப் பயன்படுத்துகிறது.

இந்த கருவிகளை பயன்படுத்த தேவையான சரியான சூழல் மாறிலிகள் அமைக்கப்பட்டுள்ளதா என்பதை உறுதிசெய்க:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Server ஐ இயக்குவது

MCP சர்வருடன் இணைக்க இந்த டெமோ உரையாடல் இடைமுகமாக Chainlit-ஐப் பயன்படுத்துகிறது। 

சர்வரை இயக்க, உங்கள் டெர்மினலில் பின்வரும் கட்டளையை பயன்படுத்துங்கள்:

```bash
chainlit run app.py -w
```

இது உங்கள் Chainlit சர்வரை `localhost:8000` இல் துவக்குவதோடு, `event-descriptions.md` உள்ளடக்கத்துடன் உங்கள் Azure AI Search Index-ஐ நிரப்பும்.

## MCP Server-க்கு இணைவு

Github MCP Server-க்கு இணைக்க, "உங்கள் செய்தியை இங்கே தட்டச்சு செய்யவும்.." உரையாடல் பெட்டியின் கீழ் உள்ள "பிளக்" ஐகானை தேர்ந்தெடுக்கவும்:

![MCP இணைப்பு](../../../../../translated_images/ta/mcp-chainlit-1.7ed66d648e3cfb28.webp)

அதிலிருந்து நீங்கள் "Connect an MCP" என்பதைக் கிளிக் செய்து Github MCP Server-க்கு இணைக்கும் கட்டளையை சேர்க்கலாம்:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

இணைப்புக்கு பிறகு, அது இணைக்கப்பட்டதாக உறுதிசெய்ய plug ஐகானின் பக்கத்தில் (1) என்பதை நீங்கள் காணவேண்டும். காணப்படவில்லை என்றால், `chainlit run app.py -w` மூலம் chainlit சர்வரை மீண்டும் துவக்க முயற்சிக்கவும்.

## டெமோவை பயன்படுத்துதல் 

ஹேக்கதான் திட்டங்களை பரிந்துரைக்கும் முகாமை தொடங்க, நீங்கள் இதுபோன்ற ஒரு செய்தியை தட்டச்சு செய்யலாம்: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent உங்கள் கோரிக்கையை பகுப்பாய்வு செய்து எந்தக் கூட்டு ஏஜென்டுகள் (GitHub, Hackathon, மற்றும் Events) உங்கள் வினாவை கையாள சிறந்தவை என்பதை தீர்மானிக்கும். ஏஜென்டுகள் ஒன்றாக சேர்ந்து GitHub ரெப்போசிடரி பகுப்பாய்வு, திட்ட யோசனை மற்றும் தொடர்புடைய தொழில்நுட்ப நிகழ்வுகளை அடிப்படையாகக் கொண்டு விரிவான பரிந்துரைகளை வழங்குகின்றன.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
மறுப்பு:
இந்த ஆவணம் AI மொழி மொழியாக்க சேவையான Co-op Translator (https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் தவறுகள் அல்லது பிழைகள் இருக்க வாய்ப்புள்ளது என்பதை தயவுசெய்து கருத்தில் கொள்க. முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்தியதனால் ஏற்படும் எந்த தவறான புரிதலுக்கும் அல்லது தவறான விளக்கங்களுக்குமான பொறுப்பையும் நாங்கள் ஏற்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->