# அமர்ந்துகொள்ளும் செயற்கை நுண்ணறிவு முகவர்கள் - ஒரு பாடநெறி

![அமர்ந்துகொள்ளும் செயற்கை நுண்ணறிவு முகவர்கள்](../../translated_images/ta/repo-thumbnailv2.06f4a48036fde647.webp)

## செயற்கை நுண்ணறிவு முகவர்கள் கட்டுவதற்கான தேவையான அனைத்தையும் கற்பிக்கும் ஒரு பாடநெறி

[![GitHub உரிமம்](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub பங்களிப்பாளர்கள்](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub பிரச்சனைகள்](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub புல்-ரிக்வஸ்ட்கள்](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs வரவேற்கப்படுகிறது](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 பல மொழி ஆதரவு

#### GitHub செயல்பாட்டின் மூலம் ஆதரவு (தானாகவும் என்றும் புதுப்பிக்கப்படும்)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[அரபி](../ar/README.md) | [பெங்காலி](../bn/README.md) | [பல்காரியன்](../bg/README.md) | [பர்மீஸ் (மையன்மர்)](../my/README.md) | [சீனப் (எளிதாக்கிய)](../zh-CN/README.md) | [சீனப் (பாரம்பரிய, ஹாங் காங்)](../zh-HK/README.md) | [சீனப் (பாரம்பரிய, மாகாவ்)](../zh-MO/README.md) | [சீனப் (பாரம்பரிய, தைவான்)](../zh-TW/README.md) | [குரோசியன்](../hr/README.md) | [செக்](../cs/README.md) | [டேனிஷ்](../da/README.md) | [டச்சு](../nl/README.md) | [எஸ்டோனியன்](../et/README.md) | [பின்லாந்து](../fi/README.md) | [பிரஞ்சு](../fr/README.md) | [ஜெர்மன்](../de/README.md) | [கிரேக்கம்](../el/README.md) | [ஹீப்ரு](../he/README.md) | [இந்தி](../hi/README.md) | [ஹங்கேரியன்](../hu/README.md) | [இந்தோனீசியன்](../id/README.md) | [இத்தாலியன்](../it/README.md) | [ஜப்பானீஸ்](../ja/README.md) | [கன்னடம்](../kn/README.md) | [க்ஹ்மேர்](../km/README.md) | [கொரியன்](../ko/README.md) | [லிதுவேனியன்](../lt/README.md) | [மலாய்](../ms/README.md) | [மலையாளம்](../ml/README.md) | [மராத்தி](../mr/README.md) | [நேபாளி](../ne/README.md) | [நைஜீரியன் பிட்ஜின்](../pcm/README.md) | [நார்வேஜியன்](../no/README.md) | [பெர்ஷியன் (பார்சி)](../fa/README.md) | [போலீஷ்](../pl/README.md) | [போர்த்துகீசியன் (பிரேசில்)](../pt-BR/README.md) | [போர்த்துகீசியன் (போர்ச்சுகல்)](../pt-PT/README.md) | [பஞ்சாபி (குருமுகி)](../pa/README.md) | [ரோமானியன்](../ro/README.md) | [ராக்ஷியன்](../ru/README.md) | [செர்பியன் (சிரில்லிக்)](../sr/README.md) | [ஸ்லோவக்](../sk/README.md) | [ஸ்லோவேனியன்](../sl/README.md) | [எஸ்பானியன்](../es/README.md) | [ஸ்வாஹிலி](../sw/README.md) | [ஸ்வீடியன்](../sv/README.md) | [தாகாலோக் (பிலிப்பீனோ)](../tl/README.md) | [தமிழ்](./README.md) | [தேசுகு](../te/README.md) | [தாய்](../th/README.md) | [ тур்கிஷ்](../tr/README.md) | [உக்ரைனியன்](../uk/README.md) | [உர்டு](../ur/README.md) | [வியட்நாமீஸ்](../vi/README.md)

> **உள்ளூரில் கிளோன் செய்ய விரும்புகிறீர்களா?**
>
> இந்த சேமிப்பகம் 50+ மொழி மொழிபெயர்ப்புக்களைக் கொண்டிருப்பதால், பதிவிறக்கும் அளவு மிக அதிகம் ஆகும். மொழிபெயர்ப்புக்களை தவிர்த்து கிளோன் செய்ய, sparse checkout பயன்படுத்தவும்:
>
> **பாஷ் / macOS / லினக்ஸ்:**
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
> இது மிக வேகமான பதிவிறக்கம் மூலம் பாடநெறியை முடிக்க தேவையான அனைத்தையும் உங்களுக்கு தரும்.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**மேலும் மொழிபெயர்ப்பு மொழிகள் ஆதரவு தேவைப்பட்டால், இங்கேப் பட்டியலிடப்பட்டுள்ளன [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub பாவனையாளர் கண்காணிப்பவர்கள்](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub கிளோன்கள்](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub நட்சத்திரங்கள்](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 தொடக்கம் செய்வது எப்படி

இந்தப் பாடநெறியில் செயற்கை நுண்ணறிவு முகவர்கள் கட்டுவதன் அடிப்படைகள் உள்ள பாடங்கள் உள்ளன. ஒவ்வொரு பாடமும் தனிப்பட்ட பொருளை கற்பிக்கிறது, எனவே உங்களுக்கு பிடித்த இடத்தில் துவங்கலாம்!

இந்தப் பாடநெறிக்குப் பலமொழி ஆதரவு உண்டு. எங்கள் [கிடைக்கும் மொழிகள் இங்கே](#-multi-language-support) செல்லவும்.

இதுவே முதன்முறையாக ஜெனரேட்டிவ் AI மாதிரிகளில் கட்டுவதற்கு இருப்பின், எங்கள் [ஜெனரேட்டிவ் AI ஆரம்பகாலங்களுக்கு](https://aka.ms/genai-beginners) பாடநெறியை பார்க்கவும், இதில் GenAI மூலம் கட்டுவதற்கான 21 பாடங்கள் உள்ளன.

இந்த சேமிப்பகத்தை [நட்சத்திரம் (🌟) தொடர்பவும்](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) மற்றும் [தனது நகலை உருவாக்க இந்த சேமிப்பகத்தை Fork செய்யவும்](https://github.com/microsoft/ai-agents-for-beginners/fork) குறியீட்டை இயக்க.

### பிற பயிலும் நண்பர்களைச் சந்தியுங்கள், உங்கள் கேள்விகளுக்கு பதில் பெறுங்கள்

நீங்கள் சிக்கினால் அல்லது செயற்கை நுண்ணறிவு முகவர்கள் கட்டுவதற்கான கேள்விகள் இருந்தால், எங்கள் Microsoft Foundry Discord இல் உள்ள தனித்துவமான Discord சேனலில் இணையுங்கள் [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord).

### தேவையானவை

இந்தப் பாடநெறியில் உள்ள ஒவ்வொரு பாடத்திலும் குறியீட்டு உதாரணங்கள் உள்ளன, அவை code_samples என்ற கோப்புறையில் காணலாம். நீங்கள் [இந்த சேமிப்பகத்தை fork செய்ய](https://github.com/microsoft/ai-agents-for-beginners/fork) உங்கள் சொந்த நகலை உருவாக்கலாம்.

இந்த பயிற்சிகளில் உள்ள குறியீட்டு உதாரணங்கள் Microsoft Agent Framework மற்றும் Azure AI Foundry Agent Service V2 கட்டமைப்புகளை பயன்படுத்துகின்றன:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure கணக்கு தேவைப்படுகிறது

இந்த பாடநெறி Microsoft வழங்கும் பின்வரும் AI முகவர் கட்டமைப்புகள் மற்றும் சேவைகளை பயன்படுத்துகிறது:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

சில குறியீட் உதாரணங்கள் குறைந்தபட்ச OpenAI சார்ந்த வழங்குநர்களையும் ஆதரிக்கின்றன, அவற்றில் [MiniMax](https://platform.minimaxi.com/) போன்றவை பெரும்பரிமாண உள்ளடக்க மாதிரிகளை (204K டோக்கன்களுக்கும் மேல்) வழங்குகின்றன. கட்டமைப்பு விவரங்களுக்கு [Course Setup](./00-course-setup/README.md) பார்க்கவும்.

இந்தப் பாடநெறிக்கான குறியீட்டை இயக்குவதற்கான கூடுதல் தகவல்களுக்கு, [Course Setup](./00-course-setup/README.md) பார்க்கவும்.

## 🙏 உதவ விரும்புகிறீர்களா?

உங்களிடம் பரிந்துரைகள் உள்ளதா அல்லது எழுத்துப் பிழைகள் அல்லது குறியீடு பிழைகள் இருந்ததா? [பிரச்சனையை எழுப்பவும்](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) அல்லது [ஒரு புல் ரிக்வஸ்டை உருவாக்கவும்](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ஒவ்வொரு பாடத்திலும் உள்ளவை

- README இல் உள்ள எழுதப்பட்ட பாடமும் சிறு வீடியோக்களும்
- Microsoft Agent Framework மற்றும் Azure AI Foundry உடன் Python குறியீடு உதாரணங்கள்
- உங்கள் கற்றலுக்கு தொடரும் கூடுதல் வளங்களுக்கான இணைப்புகள்


## 🗃️ பாடங்கள்

| **பாடம்**                                       | **உரை மற்றும் குறியீடு**                                | **வீடியோ**                                                  | **கூடுதல் கற்றல்**                                                                  |
|----------------------------------------------|--------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------------|
| AI முகவர்களின் அறிமுகம் மற்றும் பயன்பாடுகள்     | [இணைப்பு](./01-intro-to-ai-agents/README.md)           | [வீடியோ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவர் கட்டமைப்புகளை ஆராய்தல்              | [இணைப்பு](./02-explore-agentic-frameworks/README.md)   | [வீடியோ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவர் வடிவமைப்பு மாதிரிகளை புரிந்து கொள்வது | [இணைப்பு](./03-agentic-design-patterns/README.md)       | [வீடியோ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| கருவி பயன்பாட்டு வடிவமைப்பு மாதிரி             | [இணைப்பு](./04-tool-use/README.md)                      | [வீடியோ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவர் RAG                                      | [இணைப்பு](./05-agentic-rag/README.md)                   | [வீடியோ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| நம்பகமான AI முகவர்களை கட்டுவது               | [இணைப்பு](./06-building-trustworthy-agents/README.md)   | [வீடியோ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| திட்டமிடல் வடிவமைப்பு மாதிரி                   | [இணைப்பு](./07-planning-design/README.md)               | [வீடியோ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| பன்முகவரி வடிவமைப்பு மாதிரி                     | [இணைப்பு](./08-multi-agent/README.md)                   | [வீடியோ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| மெட்டகாக்னிஷன் வடிவமைப்பு மாதிரியீடு                 | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| உற்பத்தியில் AI முகவர்கள்                      | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவரிக.protocols (MCP, A2A மற்றும் NLWeb) பயன்படுத்துதல் | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவர்களுக்கு உள்ளடக்க பொறியியல்            | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவர் நினைவகத்தை நிர்வகித்தல்                      | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft முகவர் கட்டமைப்பை ஆராய்தல்                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| கணினி பயன்படுத்தும் முகவர்களை கட்டமைத்தல் (CUA)           | [Link](./15-browser-use/README.md)     |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| பரிமாணமிக்க முகவர்களை பிரியோஜிப்பது                    | விரைவில் வரும்                            |                                                            |                                                                                        |
| உள்ளூர் AI முகவர்களை உருவாக்குதல்                     | விரைவில் வரும்                               |                                                            |                                                                                        |
| AI முகவர்களை பாதுகாப்பது                           | [Link](./18-securing-ai-agents/README.md)  |                                                            | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 பிற பாடநெறிகள்

எங்கள் குழு பிற பாடநெறிகளையும் உருவாக்குகிறது! பார்:

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
 
### மூலை கற்றல்
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### கோபைலட் தொடர்
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 சமூக நன்றிகள்

Agentic RAG காட்டும் முக்கியமான குறியீட்டு மாதிரிகளை கொடுத்த [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) அவர்களுக்கு நன்றி. 

## பங்களிப்பு

இந்த திட்டம் பங்களிப்புகள் மற்றும் பரிந்துரைகளை வரவேற்கிறது. பெரும்பாலான பங்களிப்புகள் Contributor License Agreement (CLA) ஒன்றிற்கு நீங்கள் ஒப்புச் சொல்வதையும், நீங்கள் வழங்கும் பங்களிப்பை பயன்படுத்தும் உரிமைகள் உங்களுக்கு இருப்பதையும் தெரிவிக்க வேண்டும். குறிப்புகளுக்கு <https://cla.opensource.microsoft.com> செல்லவும்.

நீங்கள் ஒரு pull request சமர்ப்பித்தால், CLA bot தானாகவே நீங்கள் CLA வழங்க வேண்டுமா என்று தீர்மானித்து PR ஐ உறுதிப்படுத்து (status check, comment போன்றவை) செய்கிறது. bot வழங்கும் வழிமுறைகளைப் பின்பற்றுங்கள். எங்கள் CLA பயன்படுத்தும் அனைத்து repos க்களிலும் ஒருமுறை இதை செய்வது போதும்.

இந்தத் திட்டம் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ஐ ஏற்றுக்கொண்டுள்ளது. மேலும் தகவலுக்கு [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ஐ பார்க்கவும் அல்லது [opencode@microsoft.com](mailto:opencode@microsoft.com) என்ற முகவரிக்கு தொடர்புகொள்ளவும்.

## வர்த்தகச் சின்னங்கள்

இந்தத் திட்டத்தில் திட்டங்கள், தயாரிப்புகள் அல்லது சேவைகளுக்கான வர்த்தகச் சின்னங்கள் அல்லது லோகோக்கள் இருக்கலாம். Microsoft வர்த்தகச் சின்னங்கள் அல்லது லோகோக்களை அனுமதிப்பதற்கான பயன்படுத்துவது [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) வழிகாட்டுதல்களை பின்பற்ற வேண்டும். இந்தத் திட்டத்தின் மாற்றியமைக்கப்பட்ட பதிப்புகளில் Microsoft வர்த்தகச் சின்னங்கள் அல்லது லோகோக்களை பயன்படுத்துவது குழப்பம் ஏற்படுத்தக்கூடாது மற்றும் Microsoft ஆதரவை குறிக்கக்கூடாது. மூன்றாம் தரப்பு வர்த்தகச் சின்னங்கள் அல்லது லோகோக்கான எந்தவொரு பயன்பாடும் அப்பகுதிகளின் கொள்கைகளுக்கு உட்பட்டது.

## உதவிக்கு அணுகல்

AI பயன்பாடுகளை உருவாக்குவதில் சிக்கல் அல்லது கேள்விகள் இருந்தால், சேரவும்:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

உங்கள் தயாரிப்பு கருத்துகள் அல்லது பிழைகள் இருந்தால்:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->