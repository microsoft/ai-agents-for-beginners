# தொடக்கத்தினருக்கான AI முகவர்கள் - ஒரு பாடநெறி

![தொடக்கத்தினருக்கான AI முகவர்கள்](../../translated_images/ta/repo-thumbnailv2.06f4a48036fde647.webp)

## AI முகவர்களை உருவாக்கத் தொடங்க தேவையான அனைத்தையும் கற்பிக்கும் ஒரு பாடநெறி

[![GitHub உரிமம்](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub பங்களிப்பாளர்கள்](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub பிழைகள்](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub பூல்மேண்ட் கோரிக்கைகள்](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs வரவேற்கப்படுகின்றன](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 பல மொழி ஆதரவு

#### GitHub செயல்பாட்டின் மூலம் ஆதரிக்கப்படுகிறது (தானியங்கி மற்றும் எப்போதும் புதுப்பிக்கப்பட்ட)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[அரபு](../ar/README.md) | [பெங்காலி](../bn/README.md) | [பல்கேரியன்](../bg/README.md) | [பர்மீஸ் (மியன்மார்)](../my/README.md) | [சீன (எளியமைப்பு)](../zh-CN/README.md) | [சீன (பாரம்பரிய, ஹோங்காங்க்)](../zh-HK/README.md) | [சீன (பாரம்பரிய, மாகாவ்)](../zh-MO/README.md) | [சீன (பாரம்பரிய, தைவான்)](../zh-TW/README.md) | [குரோதியன்](../hr/README.md) | [செக்](../cs/README.md) | [டேனிஷ்](../da/README.md) | [டச்சு](../nl/README.md) | [எஸ்டோனியன்](../et/README.md) | [பினிஷ்](../fi/README.md) | [பிரெஞ்சு](../fr/README.md) | [ஜெர்மன்](../de/README.md) | [கிரீக்கு](../el/README.md) | [ஹீப்ரூ](../he/README.md) | [இந்தி](../hi/README.md) | [ஹங்கேரியன்](../hu/README.md) | [இந்தோனீசியன்](../id/README.md) | [இத்தாலியன்](../it/README.md) | [ஜாப்பனீஸ்](../ja/README.md) | [கன்னடம்](../kn/README.md) | [க்மர்](../km/README.md) | [கொரியன்](../ko/README.md) | [லித்துவேனியன்](../lt/README.md) | [மலே](../ms/README.md) | [மலையாளம்](../ml/README.md) | [மராத்தி](../mr/README.md) | [நேபாளி](../ne/README.md) | [நைஜீரியன் பிஜின்](../pcm/README.md) | [நார்வேஜியன்](../no/README.md) | [பெர்சியன் (பார்சி)](../fa/README.md) | [போலந்து](../pl/README.md) | [பொர்துகீசு (பிரேசில்)](../pt-BR/README.md) | [பொர்துகீசு (போர்ச்சுகல்)](../pt-PT/README.md) | [பஞ்சாபி (குருமுகி)](../pa/README.md) | [ரோமானியன்](../ro/README.md) | [ரஷியன்](../ru/README.md) | [செர்பியன் (செரிலிக்)](../sr/README.md) | [ஸ்லோவாக்](../sk/README.md) | [ஸ்லோவேனியன்](../sl/README.md) | [எஸ்பானியோல்](../es/README.md) | [ஸ்வாஹிலி](../sw/README.md) | [ஸ்வீடிஷ்](../sv/README.md) | [டாகாலாக்க் (பிலிப்பைன்ஸ்)](../tl/README.md) | [தமிழ்](./README.md) | [తెలుగు](../te/README.md) | [தை](../th/README.md) | [துருக்கி](../tr/README.md) | [உக்‌రைனியன்](../uk/README.md) | [உருது](../ur/README.md) | [வியட்நாமீஸ்](../vi/README.md)

> **உங்கள் கணினியில் உள்ளே கிளோன் செய்வது விரும்புகிறீர்களா?**
>
> இந்த ரெப்போசியரி 50+ மொழி மொழி மாற்றங்களை கொண்டுள்ளது, இதனால் டவுன்லோடு அளவு பெரிதாகிறது. மொழி மாற்றங்கள் இல்லாமல் கிளோன் செய்ய sparse checkout பயன்படுத்தவும்:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (விண்டோஸ்):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> இது பாடநெறியை விரைவாக முடிக்க தேவையான அனைத்தையும் தருகின்றது.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**நீங்கள் கூடுதலாக மாற்ற மொழிகளை ஆதரிக்க விரும்பினால், அவை [இங்கு](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) பட்டியலிடப்பட்டுள்ளன.**

[![GitHub பார்வையாளர்கள்](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub கிளோன்கள்](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub நட்சத்திரங்கள்](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 தொடங்குதல்

இந்த பாடநெறி AI முகவர்களை உருவாக்கும் அடிப்படைகளை உள்ளடக்கிய பாடங்களை கொண்டுள்ளது. ஒவ்வொரு பாடமும் தனித்தனியான தலைப்பை உள்ளடக்கியுள்ளது, எனவே நீங்கள் விரும்பிய இடத்தில் தொடங்கலாம்!

இந்தக் கையேட்டிற்கான பல மொழி ஆதரவு உள்ளது. [மொழிகள் இங்கே](#-multi-language-support) பார்க்கவும்.

இதுவுதான் முதலாம் முறை Generative AI மாதிரிகளுடன் பணி செய்வதாக இருந்தால், எங்களுடைய [தொடக்கத்தினருக்கான வடிவமைப்பு AI](https://aka.ms/genai-beginners) பாடநெறியைப் பாருங்கள், இதில் GenAI உடன் உருவாக்க 21 பாடங்கள் உள்ளன.

[இந்த ரெப்போவை நட்சத்திரம் (🌟) பெற](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) மறக்காமல் செய்யவும் மற்றும் குறியீட்டை இயக்க [இந்த ரெப்போவை கிளோன்](https://github.com/microsoft/ai-agents-for-beginners/fork) செய்யவும்.

### பிற கற்றவர்கள் சந்திப்பு, உங்கள் கேள்விகளுக்கு பதில் பெறுதல்

AI முகவர்களை உருவாக்குவதில் ஏதாவது சிக்கல் வந்தால் அல்லது கேள்விகள் இருந்தால், எங்கள் குறிப்பிட்ட Discord சேனல் [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) இல் சேரவும்.

### என்ன வேண்டும்

இந்த பாடநெறியில் உள்ள ஒவ்வொரு பாடத்திலும் குறியீடு எடுத்துக்காட்டுகள் உள்ளன, அவை code_samples என்ற папரில் காணலாம். உங்கள் சொந்த நகலை உருவாக்க [இந்த ரெப்போவை கிளோன்](https://github.com/microsoft/ai-agents-for-beginners/fork) செய்யலாம்.

இந்த பயிற்சிகளின் குறியீடு எடுத்துக்காட்டுகள் Microsoft Agent Framework மற்றும் Azure AI Foundry Agent Service V2 ஐ பயன்படுத்துகின்றன:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure கணக்கு தேவை

இந்தப் பாடநெறி Microsoft இன் பின்வரும் AI முகவர் தொழில்நுட்பங்களையும் சேவைகளையும் பயன்படுத்துகிறது:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

சில குறியீடு எடுத்துக்காட்டுகள் OpenAI-க்கு இணக்கமான மாற்று வழங்குநர்களான [MiniMax](https://platform.minimaxi.com/) போன்றவற்றையும் ஆதரிக்கின்றன, இது பெரிய-context மாதிரிகள் (இருந்து 204K டோக்கன்கள் வரை) வழங்குகிறது. உள்ளமைவு விவரங்களுக்கு [பாடநெறி அமைவு](./00-course-setup/README.md) பார்க்கவும்.

இந்தப் பாடநெறிக்கான குறியீடு இயக்கும் மேலதிக தகவலுக்கு, [பாடநெறி அமைவு](./00-course-setup/README.md) செல்லவும்.

## 🙏 உதவ விரும்புகிறீர்களா?

உங்களுக்கு பரிந்துரைகள் இருந்தால் அல்லது எழுத்துப்பிழைகள் அல்லது குறியீடு பிழைகள் கண்டுபிடித்திருந்தால், [ஒரு பிரச்சினையையும் எழுப்பவும்](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) அல்லது [ஒரு பூல்மேண்ட் கோரிக்கையை உருவாக்கவும்](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ஒவ்வொரு பாடத்திலும் உள்ளவை

- README இல் உள்ள எழுத்து பாடம் மற்றும் ஒரு சுருக்கமான வீடியோ
- Microsoft Agent Framework மற்றும் Azure AI Foundry பயன்படுத்தி Python குறியீடு எடுத்துக்காட்டுகள்
- உங்கள் கற்றலை தொடரும் கூடுதல் வளங்களுக்கான இணைப்புகள்


## 🗃️ பாடங்கள்

| **பாடம்**                                 | **உரை மற்றும் குறியீடு**                          | **வீடியோ**                                                | **கூடுதல் கற்றல்**                                                                        |
|--------------------------------------------|--------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| AI முகவர்களுக்கான அறிமுகம் மற்றும் முகவர் பயன்பாட்டு வழக்குகள் | [இணைப்பு](./01-intro-to-ai-agents/README.md)      | [வீடியோ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)   |
| AI முகவர் கட்டமைப்புகளை ஆய்வு செய்வது     | [இணைப்பு](./02-explore-agentic-frameworks/README.md) | [வீடியோ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)   |
| AI முகவர் வடிவமைப்பு மாதிரிகளைப் புரிந்துகொள் | [இணைப்பு](./03-agentic-design-patterns/README.md)  | [வீடியோ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)   |
| கருவி பயன்பாட்டு வடிவமைப்பு மாதிரி         | [இணைப்பு](./04-tool-use/README.md)                | [வீடியோ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)   |
| முகவர் RAG                                | [இணைப்பு](./05-agentic-rag/README.md)              | [வீடியோ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)   |
| நம்பத்தகுந்த AI முகவர்களை உருவாக்குதல்     | [இணைப்பு](./06-building-trustworthy-agents/README.md) | [வீடியோ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)   |
| திட்டமிடல் வடிவமைப்பு மாதிரி               | [இணைப்பு](./07-planning-design/README.md)         | [வீடியோ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)   |
| பன்முகவர் வடிவமைப்பு மாதிரி                | [இணைப்பு](./08-multi-agent/README.md)              | [வீடியோ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)   |
| மெட்டாகாக்னிசன் வடிவமைப்பு نمு                           | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| உற்பத்தியில் AI முகவர்கள்                                   | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவர் நிரல்ப் செயல்பாடுகள் பயன்படுத்துதல் (MCP, A2A மற்றும் NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவர்களுக்கான சூழல் பொறியியல்                            | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவர் நினைவகத்தை நிர்வகித்தல்                                 | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| மைக்ரோசாஃப்ட் முகவர் வரைபட சோதனை                               | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| கணினி பயனர் முகவர்கள் உருவாக்குதல் (CUA)                           | [Link](./15-browser-use/README.md)     |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| விரிவாக்கக்கூடிய முகவர்களை நிறுவுதல்                          | விரைவில் வருகிறது                                    |                                                            |                                                                                        |
| உள்ளூர் AI முகவர்களை உருவாக்கல்                                | விரைவில் வருகிறது                                    |                                                            |                                                                                        |
| AI முகவர்களை பாதுகாப்பது                                      | [Link](./18-securing-ai-agents/README.md)  |                                                            | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 பிற பாடங்கள்

எங்கள் குழு பிற பாடங்களையும் தயாரிக்கிறது! பாருங்கள்:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
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
 
### மூல கற்றல்
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![தரவு அறிவியல் ஆரம்பக் கட்டங்களுக்கு](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![சைபர் பாதுகாப்பு ஆரம்பம்](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![வலை மேம்பாடு தொடக்கம்](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT ஆரம்பக் கட்டங்களுக்கு](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR மேம்பாடு ஆரம்பம்](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### கோப்பொய்லட் தொடர்
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 சமூகம் நன்றி

Agentic RAG ஐ வெளிப்படுத்தும் முக்கிய குறியீடு உதவியுள்ள [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) அவர்களுக்கு நன்றி.

## பங்களிப்பு

இந்த திட்டம் பங்களிப்புகள் மற்றும் பரிந்துரைகளை வரவேற்கிறது. பெரும்பாலான பங்களிப்புகள் Contributor License Agreement (CLA)-இல் ஒப்புதல் அளிக்க வேண்டும், அதாவது நீங்கள் உங்கள் பங்களிப்பை பயன்படுத்த ஒப்புதல் அளிக்கும் உரிமையை கொண்டுள்ளீர்கள் என்பதை உறுதி செய்யும். 詳細க்கு, <https://cla.opensource.microsoft.com> -ஐ பார்வையிடவும்.

நீங்கள் pull request சமர்ப்பிக்கும் போது, CLA பாட்டி தானாகவே உங்கள் CLA தேவைப்படுகிறதா என்பதையும் PR-ஐ சரியாக அலங்கரிக்கும் (பதிவுப் பரிசோதனை, கருத்து) முடிவினை வழங்கும். பாட்டியின் வழிமுறைகளை பின்பற்றுங்கள். இது அனைத்து கோப்பகங்களில் ஒருமுறை தான் தேவையாகும்.

இந்த திட்டம் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ஐ ஏற்றுக்கொண்டு உள்ளது. மேலதிக தகவலுக்கு [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) பார்வையிடவும் அல்லது [opencode@microsoft.com](mailto:opencode@microsoft.com) மூலம் தொடர்பு கொள்ளவும்.

## வர்த்தக அடையாளங்கள்

இந்த திட்டத்தில் திட்டங்கள், தயாரிப்புகள் அல்லது சேவைகளுக்கான வர்த்தக அடையாளங்கள் அல்லது லோகோக்கள் இருக்கலாம். Microsoft வர்த்தக அடையாளங்கள் அல்லது லோகோக்களை அனுமதிப்புடன் பயன்படுத்துதல் [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ஐ பின்பற்ற வேண்டும். இந்த திட்டத்தின் மாற்றியமைக்கப்பட்ட பதிப்புகளில் Microsoft வர்த்தக அடையாளங்கள் அல்லது லோகோக்களை பயன்படுத்துவது குழப்பம் விளைவிக்கக் கூடாதும் Microsoft ஆதரவு என்பதைக் குறிக்கக்கூடாது. மூன்றாம் தரப்பு வர்த்தக அடையாளங்கள் அல்லது லோகோக்களை பயன்படுத்துவது அந்த மூன்றாம் தரப்பின் கொள்கைகள் அமல்படுத்தப்படும்.

## உதவி பெறுதல்

AI பயன்பாடுகள் உருவாக்கியபோது சிக்கலில் படுகிறீர்கள் அல்லது கேள்விகள் உள்ளதா என்றால், சேருங்கள்:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

உங்கள் தயாரிப்பின் பின்னூட்டங்கள் அல்லது பிழைகள் இருந்தால், பார்வையிடுங்கள்:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->