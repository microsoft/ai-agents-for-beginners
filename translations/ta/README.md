# புதியவர்களுக்கு AI முகவர்கள் - ஒரு பாடநெறி

![புதியவர்களுக்கு AI முகவர்கள்](../../translated_images/ta/repo-thumbnailv2.06f4a48036fde647.webp)

## AI முகவர்களை உருவாக்கத் தொடங்கி கற்றுக்கொள்ள நீங்கள் அறிய வேண்டும் அனைத்தையும் கற்பிக்கும் ஒரு பாடநெறி

[![GitHub உரிமை](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub பங்களிப்பாளர்கள்](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub பிரச்சினைகள்](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub இழுக்க வேண்டுமென்ற கோரிக்கைகள்](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![இழுக்க வேண்டுகோள்களுக்கு வரவேற்கிறோம்](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 பல மொழி ஆதாரம்

#### GitHub செயல் மூலம் ஆதரவு (தானாகவும் எப்போதும் புதுப்பிக்கப்படும்)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[அரபு](../ar/README.md) | [பெங்காலி](../bn/README.md) | [பல்கேரியன்](../bg/README.md) | [பெர்மீஸ் (மியாமார்)](../my/README.md) | [சீன (சாதாரண)](../zh-CN/README.md) | [சீன (பாரம்பரிய, ஹாங்காங்)](../zh-HK/README.md) | [சீன (பாரம்பரிய, மகாவ்)](../zh-MO/README.md) | [சீன (பாரம்பரிய, தைவான்)](../zh-TW/README.md) | [குரோசியன்](../hr/README.md) | [செக்](../cs/README.md) | [டேனிஷ்](../da/README.md) | [டச்சு](../nl/README.md) | [எஸ்டோனியன்](../et/README.md) | [பின்னிஷ்](../fi/README.md) | [பிரஞ்சு](../fr/README.md) | [ஜெர்மன்](../de/README.md) | [கிரேக்கம்](../el/README.md) | [ஹீப்ரூ](../he/README.md) | [ஹிந்தி](../hi/README.md) | [ஹங்கேரியன்](../hu/README.md) | [இந்தோனேஷியன்](../id/README.md) | [இத்தாலியன்](../it/README.md) | [ஜப்பானியன்](../ja/README.md) | [கன்னடம்](../kn/README.md) | [க்மர்](../km/README.md) | [கொரியன்](../ko/README.md) | [லிதுவேனியன்](../lt/README.md) | [மலாய்](../ms/README.md) | [மலையாளம்](../ml/README.md) | [மறாத்தி](../mr/README.md) | [நேபாளி](../ne/README.md) | [நைஜீரியன் பிஜின்](../pcm/README.md) | [நார்வேஜியன்](../no/README.md) | [பெர்ஷியன் (ஃபார்ஸி)](../fa/README.md) | [போலிஷ்](../pl/README.md) | [போர்ச்சுகீஸ் (பிரசில்)](../pt-BR/README.md) | [போர்ச்சுகீஸ் (போர்ச்சுகல்)](../pt-PT/README.md) | [பஞ்சாபி (குருமுகி)](../pa/README.md) | [ரோமானியன்](../ro/README.md) | [ரஷ்யன்](../ru/README.md) | [செர்பியன் (சிரிலிக்)](../sr/README.md) | [ஸ்லோவக்](../sk/README.md) | [ஸ்லோவேனியன்](../sl/README.md) | [ஸ்பானிஷ்](../es/README.md) | [ஸ்வாஹிலி](../sw/README.md) | [ஸ்வீடிஷ்](../sv/README.md) | [டாகாலோக் (பிலிப்பினோ)](../tl/README.md) | [தமிழ்](./README.md) | [தெலுங்கு](../te/README.md) | [தை](../th/README.md) | [துருக்கி](../tr/README.md) | [உக்ரைனி](../uk/README.md) | [உருது](../ur/README.md) | [வியட்நாமீஸ்](../vi/README.md)

> **உள்ளூரில் கிளோன் செய்ய விரும்புமா?**
>
> இந்த சாதனை 50+ மொழி மொழிபெயர்ப்புகளை கொண்டு தருகிறது, இது பதிவிறக்கம் அளவை கணிசமாக அதிகரிக்கிறது. மொழிபெயர்ப்புகளின்றி கிளோன் செய்ய sparse checkout பயன்படுத்தவும்:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> இது நீங்கள் பாடநெறியை நிறைவேற்ற உங்கள் தேவையான அனைத்தையும் Much faster பதிவிறக்கம் உடன் தரும்.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**மேலும் மொழிபெயர்ப்பு ஆதரவு விரும்பினால் [இங்கே](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) பட்டியலிடப்பட்டுள்ளது**

[![GitHub பார்வையாளர்கள்](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub கிளோன்கள்](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub நட்சத்திரங்கள்](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 துவக்குவது எப்படி

இந்த பாடநெறியில் AI முகவர்களை உருவாக்கும் அடிப்படைகள் கற்றுக்கொடுக்கப்படுகின்றன. ஒவ்வொரு பாடமும் தனித்தனியாக உள்ளத，所以 நீங்கள் எந்த பாடத்திலிருந்து தொடங்கலாம்!

இந்த பாடநெறிக்கு பல மொழி ஆதாரம் உள்ளது. எங்கள் [கிடைக்கும் மொழிகளை இங்கே பார்க்கவும்](#-multi-language-support).

நீங்கள் இது முதன்முறையாக Generative AI மாதிரிகளுடன் பணியாற்றினால், எங்கள் [புதியவர்களுக்கு Generative AI](https://aka.ms/genai-beginners) பாடநெறியை பார்த்து கொள்ளவும், இது GenAI கொண்டு உருவாக்க 21 பாடங்களை கொண்டுள்ளது.

இந்த சேமிப்பகத்தை [நட்சத்திரமிடவும் (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) மற்றும் [கிளோன் செய்யவும்](https://github.com/microsoft/ai-agents-for-beginners/fork) கோவை இயக்க இந்த கோடுகளை பயன்படுத்தவும் மறக்க வேண்டாம்.

### பிற கற்றுப்போகும் நண்பர்களை சந்திக்கவும், உங்கள் கேள்விகளுக்கு பதில் பெறவும்

நீங்கள் சிக்கலாகி அல்லது AI முகவர்கள் உருவாக்கம் குறித்த கேள்விகள் இருந்தால், எங்கள் தனிச்சட்ட போதுரில் உள்ள [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) சேனலுக்கு சேர்ந்துகொள்ளுங்கள்.

### உங்களுக்கு என்ன தேவைகள்

இந்த பாடநெறியின் ஒவ்வொரு பாடமும் குறியீடு உதாரணங்களைக் கொண்டுள்ளது, அவை code_samples ன் கோப்புறையில் உள்ளன. நீங்கள் [இந்த சேமிப்பகத்தை கிளோன் செய்யவும்](https://github.com/microsoft/ai-agents-for-beginners/fork) உங்கள் தனிப்பட்ட பிரதியை உருவாக்கலாம்.

இந்த பயிற்சிகளில் உள்ள குறியீடு உதாரணங்கள் Microsoft Agent Framework ஐ Azure AI Foundry Agent Service V2 உடன் பயன்படுத்துகின்றன:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure கணக்கு தேவை

இந்த பாடநெறி Microsoft நிறுவனத்தின் பின்வரும் AI முகவர் கட்டமைப்புகள் மற்றும் சேவைகளைப் பயன்படுத்துகிறது:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

சில குறியீடு உதாரணங்கள் [MiniMax](https://platform.minimaxi.com/) போன்ற OpenAI ஒத்துழைப்பு பெற்ற மாற்று வினியோகத்தினை ஆதரிக்கின்றன, இது மிகப்பெரிய பார்வை மாதிரிகளை (அதிகபட்சம் 204K டோக்கன்கள்) வழங்குகிறது. அமைப்புக்களின் விரிவான விளக்கங்களுக்கு [பாடநெறி அமைப்பை](./00-course-setup/README.md) காண்க.

இந்த பாடநெறி குறியீடு இயக்கும் முறைகள் பற்றி மேலதிக தகவலுக்கு [பாடநெறி அமைப்பை](./00-course-setup/README.md) பாருங்கள்.

## 🙏 உதவ விரும்புகிறீர்களா?

எதைப் பரிந்துரைகள் உள்ளதா அல்லது எழுத்து பிழைகள் அல்லது குறியீடு பிழைகள் கண்டுபிடிக்கப்பட்டதா? [பிரச்சினை எழுப்பவும்](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) அல்லது [இழுக்க வேண்டுகோள் உருவாக்கவும்](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ஒவ்வொரு பாடத்திலும் உள்ளவை

- README இல் எழுத்துத் பாடமும் ஒரு குறுங்காணொளியும்
- Python குறியீடு உதாரணங்கள் Microsoft Agent Framework உடன் Azure AI Foundry பயன்படுத்தி
- உங்கள் கற்றலை தொடர மேலும் வளவளங்கள் இணைப்புகள்


## 🗃️ பாடங்கள்

| **பாடம்**                                   | **எழுத்தும் குறியீடும்**                                    | **காணொளி**                                                  | **கூடுதல் கற்றல்**                                                                     |
|----------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI முகவர்கள் மற்றும் முகவர் பயன்பாடு அறிமுகம்       | [இணைப்பு](./01-intro-to-ai-agents/README.md)              | [காணொளி](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)   | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவர் கட்டமைப்புகளை ஆராய்தல்              | [இணைப்பு](./02-explore-agentic-frameworks/README.md)      | [காணொளி](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)   | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவர் வடிவமைப்பு வரைவுகளை புரிதல்           | [இணைப்பு](./03-agentic-design-patterns/README.md)         | [காணொளி](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)   | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| கருவி பயன்பாடு வடிவமைப்பு அடுக்கு                | [இணைப்பு](./04-tool-use/README.md)                        | [காணொளி](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)   | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவர் RAG                                    | [இணைப்பு](./05-agentic-rag/README.md)                     | [காணொளி](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)   | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| நம்பகமான AI முகவர்கள் உருவாக்குதல்                 | [இணைப்பு](./06-building-trustworthy-agents/README.md)     | [காணொளி](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK )  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| திட்டமிடல் வடிவமைப்பு அடுக்கு                    | [இணைப்பு](./07-planning-design/README.md)                 | [காணொளி](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)   | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| பன்முகவர் வடிவமைப்பு அடுக்கு                      | [இணைப்பு](./08-multi-agent/README.md)                     | [காணொளி](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)   | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| மேட்டாகக்னிஷன் வடிவமைப்பு மாதிரி                 | [கணக்கு](./09-metacognition/README.md)               | [வீடியோ](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [கணக்கு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| தயாரிப்பில் AI முகவர்கள்                      | [கணக்கு](./10-ai-agents-production/README.md)        | [வீடியோ](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [கணக்கு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவரிச் நெறிமுறைகளை பயன்படுத்துதல் (MCP, A2A மற்றும் NLWeb) | [கணக்கு](./11-agentic-protocols/README.md)           | [வீடியோ](https://youtu.be/X-Dh9R3Opn8)                                 | [கணக்கு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவர்களுக்கான சூழல் பொறியியல்            | [கணக்கு](./12-context-engineering/README.md)         | [வீடியோ](https://youtu.be/F5zqRV7gEag)                                 | [கணக்கு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவரிச் நினைவகத்தை நிர்வகித்தல்                      | [கணக்கு](./13-agent-memory/README.md)     |      [வீடியோ](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| மைக்ரோசாஃப்ட் முகவர் கட்டமைப்பை ஆராய்தல்                         | [கணக்கு](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| கணினி உபயோக முகவர்களை உருவாக்குதல் (CUA)           | [கணக்கு](./15-browser-use/README.md)     |                                                            | [கணக்கு](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| அளவிடக்கூடிய முகவர்களை வெளியிடுதல்                    | விரைவில் வருகிறது                            |                                                            |                                                                                        |
| உள்ளூர் AI முகவர்களை உருவாக்குதல்                     | விரைவில் வருகிறது                               |                                                            |                                                                                        |
| AI முகவர்களை பாதுகாப்பது                           | விரைவில் வருகிறது                               |                                                            |                                                                                        |

## 🎒 பிற பாடநெறிகள்

எங்கள் குழு பிற பாடநெறிகளையும் உருவாக்குகிறது! கீழே பாருங்கள்:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### லாங்செயின்
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / முகவர்கள்
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### உருவாக்கும் AI தொடர்
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### கோர் கற்றல்
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### கோப்பைடு தொடர்
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 சமூக நன்றி

Agentic RAG-ஐ காட்டும் முக்கிய குறியீட்டு எடுத்துக்காட்டுகளை வழங்கிய [ஷிவம் கோயல்](https://www.linkedin.com/in/shivam2003/) அவருக்கு நன்றி.

## பங்களிப்பு

இந்த திட்டம் பங்களிப்புகளையும் பரிந்துரைகளையும் வரவேற்கின்றது. பெரும்பாலும் பங்களிப்புகள் நீங்கள் பங்களிப்பை பயன்படுத்த உரிமை உடையது மற்றும் உண்மையில் கொடுக்கின்றீர்கள் என்ற பணியாளர் உரிமத்திருத்த உடன்பாட்டை (CLA) ஏற்கவேண்டும். விவரங்களுக்கு <https://cla.opensource.microsoft.com> பார்க்கவும்.

நீங்கள் ஒரு புல் கோரிக்கையை சமர்ப்பிக்கும் போது, CLA பாட்டு தானாகவே நீங்கள் CLA வழங்கவேண்டுமா என்பதை நிர்ணயிப்பதுடன் சரியான முகவரியை (எ.கா., நிலை சரிபார்ப்பு, கருத்து) சேர்க்கும். பாட்டின் அறிவுறுத்துகளைப் பின்பற்றவும். எங்கள் CLA பயன்படுத்தும் அனைத்து தொகுதிகளிலும் இதை ஒருமுறை மட்டுமே செய்ய வேண்டியிருக்கும்.

இந்த திட்டம் [Microsoft திறந்த மூல குறியீட்டு நடத்தை கோட்பாடு](https://opensource.microsoft.com/codeofconduct/)ஐ ஏற்றுள்ளதன் கீழ் உள்ளது.
மேலும் விவரங்களுக்கு [நடத்தை கோட்பாடு FAQ](https://opensource.microsoft.com/codeofconduct/faq/) பார்க்கவும் அல்லது மேலதிக கேள்விகள் அல்லது கருத்துக்களுக்கு [opencode@microsoft.com](mailto:opencode@microsoft.com) என்ற முகவரிக்கு தொடர்புகொள்ளவும்.

## வர்த்தகசின்னங்கள்

இந்த திட்டம் திட்டங்கள், தயாரிப்புகள் அல்லது சேவைகளுக்கான வர்த்தகசின்னங்கள் அல்லது லோகோக்கள் உள்ளடக்கியிருக்கலாம். Microsoft வர்த்தகசின்னங்கள் அல்லது லோகோக்கள் பயன்படுத்தும் அனுமதி Microsoft  
[வர்த்தகசின்னம் மற்றும் பிராண்ட் வழிகாட்டிகள்](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) கட்டுப்பாடுகளுக்கு உட்பட்டது மற்றும் அதை பின்பற்ற வேண்டும்.  
இந்த திட்டத்தின் மாற்றிய பதிப்புகளில் Microsoft வர்த்தகசின்னங்கள் அல்லது லோகோக்கள் பயன்படுத்துதல் குழப்பத்தை ஏற்படுத்த கூடாது அல்லது Microsoft பங்காளித்துவத்தைக் குறிக்க கூடாது.  
மூன்றாம் தரப்பு வர்த்தகசின்னங்கள் அல்லது லோகோக்கள் பயன்படுத்துதல் அந்த மூன்றாம் தரப்பு கொள்கைகளுக்கு உட்பட்டது.

## உதவி பெறுதல்

AI செயலிகளை உருவாக்குவதில் சிக்கல் ஏற்பட்டால் அல்லது கேள்விகள் இருந்தால், சேரவும்:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

உற்பத்தி கருத்துக்கள் அல்லது பிழைகள் இருந்தால், பார்வையிடவும்:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**அறிக்கை**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) எனும் AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டது. நாங்கள் துல்லியம் பெற முயல்கிறோம் என்பதாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதையும் தயவுடன் கவனிக்கவும். தொன்மையான ஆவணம் அதன் நேரடி மொழியில் அதிபத்திய ஆதாரமாக கருதப்பட வேண்டியது முக்கியம். முக்கியமான தகவல்களுக்காக, மனித மொழிபெயர்ப்பாளரின் சேவையைப் பயன்படுத்த பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்படும் எந்தவொரு தவறான புரிதல்களுக்கும் நாங்கள் பொறுப்பில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->