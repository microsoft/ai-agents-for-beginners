<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0f72060e745b81a3705ec8b208cb7de2",
  "translation_date": "2026-01-15T18:29:09+00:00",
  "source_file": "README.md",
  "language_code": "ta"
}
-->
# ஆரம்பத்திற்கான AI முகவர்கள் - ஒரு பாடநெறி

![துவக்கத்திற்கான உருவாக்கும் AI](../../../../translated_images/ta/repo-thumbnailv2.06f4a48036fde647.webp)

## AI முகவர்கள் உருவாக்க ஆரம்பிக்கத் தேவையான அனைத்தையும் கற்றுக் கொடுக்கும் பாடநெறி

[![GitHub உரிமம்](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub பங்களிப்பாளர்கள்](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub பிரச்சனைகள்](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub இழுக்குக் கோரிக்கைகள்](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs வரவேற்கப்படுகின்றன](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 பன்மொழி ஆதரவு

#### GitHub செயல்பாடு மூலம் ஆதரிக்கப்படுகிறது (தானாகவும் எப்போதும் புதுப்பிக்கப்படும்)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[அரபு](../ar/README.md) | [பெங்காலி](../bn/README.md) | [பல்கேரியன்](../bg/README.md) | [பர்மீஸ் (மியான்மர்)](../my/README.md) | [சீன (எளிய)](../zh/README.md) | [சீன (முறைபடுத்தப்பட்டம், ஹொங்கொங்)](../hk/README.md) | [சீன (முறைபடுத்தப்பட்டம், மெகாவு)](../mo/README.md) | [சீன (முறைபடுத்தப்பட்டம், தைவான்)](../tw/README.md) | [குரோஷியன்](../hr/README.md) | [செக்](../cs/README.md) | [டேனிஷ்](../da/README.md) | [டச்சு](../nl/README.md) | [எஸ்டோனியன்](../et/README.md) | [பின்னிஷ்](../fi/README.md) | [பிரெஞ்சு](../fr/README.md) | [ஜெர்மன்](../de/README.md) | [கிரேக்கம்](../el/README.md) | [ஹீப்ரு](../he/README.md) | [இந்தி](../hi/README.md) | [ஹங்கேரியன்](../hu/README.md) | [இந்தோனேஷியன்](../id/README.md) | [இத்தாலியன்](../it/README.md) | [ஜப்பானீஸ்](../ja/README.md) | [கன்னடம்](../kn/README.md) | [கொரியன்](../ko/README.md) | [லித்துவேனியன்](../lt/README.md) | [மலாய்](../ms/README.md) | [மலையாளம்](../ml/README.md) | [மராத்தி](../mr/README.md) | [நேபாளி](../ne/README.md) | [நைஜீரியன் புழிகின்](../pcm/README.md) | [நார்வேஜியன்](../no/README.md) | [பேர்ஷியன் (ஃபார்சி)](../fa/README.md) | [போலிஷ்](../pl/README.md) | [போர்த்துகீசியன் (பிரேசில்)](../br/README.md) | [போர்த்துகீசியன் (போர்ச்சுகால்)](../pt/README.md) | [பஞ்சாபி (குர்முகி)](../pa/README.md) | [ரோமானியன்](../ro/README.md) | [ரஷியன்](../ru/README.md) | [செர்பியன் (சிரிலிக்)](../sr/README.md) | [ஸ்லோவாக்](../sk/README.md) | [ஸ்லோவேனியன்](../sl/README.md) | [ஸ்பானிஷ்](../es/README.md) | [சுவாஹிலி](../sw/README.md) | [சுவீடிஷ்](../sv/README.md) | [டகாலோக் (பிலிப்பைனோ)](../tl/README.md) | [தமிழ்](./README.md) | [தெலுங்கு](../te/README.md) | [தை](../th/README.md) | [துருக்கிய](../tr/README.md) | [உக்ரைனியன்](../uk/README.md) | [உருது](../ur/README.md) | [வியட்நாமீஸ்](../vi/README.md)

> **பொது டவுண்லோட் செய்ய விரும்புகிறீர்களா?**

> இந்த களஞ்சியம் 50+ மொழி மொழிபெயர்ப்புகளை கொண்டுள்ளது, இது பதிவிறக்கும் அளவை மிக அதிகரிக்கிறது. மொழிபெயர்ப்புகளை இல்லாமல் கிளோன் செய்ய, sparse checkout பயன்படுத்தவும்:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> இதனால் வேகமாக பதிவிறக்கம் செய்வதற்கு தேவையான அனைத்தும் கிடைக்கும்.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**மேலும் மொழிபெயர்ப்பு மொழிகள் ஆதரிக்கப்பட விரும்பினால், அவை இங்கே பட்டியலிடப்பட்டுள்ளன [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub காக்கும் வாசகர்கள்](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub கிளோன்கள்](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub நட்சத்திரங்கள்](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 தொடங்கி பார்க்க

இந்தப் பாடநெறியில் AI முகவர்கள் உருவாக்குவதற்கான அடிப்படைகள் உள்ள பாடங்கள் உள்ளன. ஒவ்வொரு பாடமும் அதே தலைப்பை பற்றியது, ஆகவே உங்கள் விருப்பப்படி எங்கும் தொடங்குங்கள்!

இந்தப் பாடநெறிக்குப் பன்மொழி ஆதரவு உள்ளது. எங்கள் [கிடைக்கும் மொழிகள் இங்கே](../..) பாருங்கள்.

உங்கள் முதல்முறையாக உருவாக்கும் Generative AI மாதிரிகள் இருந்தால், எங்கள் [துவக்கத்திற்கான உருவாக்கும் AI](https://aka.ms/genai-beginners) பாடநெறியைப் பாருங்கள், இது GenAI உடன் உருவாக்க 21 பாடங்கள் கொண்டுள்ளது.

இந்தக் கோப்பகத்தைக் [நட்சத்திரம் (🌟) இடவும்](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) மற்றும் [இதை கிளோன் செய்யவும்](https://github.com/microsoft/ai-agents-for-beginners/fork) கோட்டை இயக்கு.

### பிற கற்றல் பயனர்களை சந்திக்கவும், உங்கள் கேள்விகளுக்கு பதில் பெறவும்

முக்கியமாக AI முகவர்கள் உருவாக்குவதில் திணறினால் அல்லது கேள்விகள் இருந்தால், எங்கள் Microsoft Foundry Discord இல் உள்ள தனித்துவமான Discord சேனலில் சேரவும் [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord).

### உங்களுக்கு தேவையானவை

இந்தப் பாடநெறியில் ஒவ்வொரு பாடத்திலும் உள்ளடக்க நிரலுக்கான எடுத்துக்காட்டுகள் உள்ளன, அவை code_samples என்ற அடைவில் காணலாம். [இந்தக் கோப்பகத்தை கிளோன் செய்யவும்](https://github.com/microsoft/ai-agents-for-beginners/fork) உங்கள் சொந்த நகலை உருவாக்க.

இந்தப் பயிற்சி எடுத்துக்காட்டுகளில் உள்ள நிரல் Azure AI Foundry மற்றும் GitHub மாதிரி தொகுப்புகளைக் பயன்படுத்தி மொழி மாதிரிகளுடன் உறவு கொள்ளும்:

- [Github மாதிரிகள்](https://aka.ms/ai-agents-beginners/github-models) - இலவசம் / வரம்பு
- [Azure AI Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure கணக்கு தேவை

இந்த பாடநெறி Microsoft வழங்கும் கீழ்காணும் AI முகவர் கட்டமைப்புக்களையும் சேவைகளையும் பயன்படுத்துகிறது:

- [Microsoft Agent Framework (MAF) - புதியது!](https://aka.ms/ai-agents-beginners/agent-framewrok)
- [Azure AI Agent சேவை](https://aka.ms/ai-agents-beginners/ai-agent-service)
- [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel)
- [AutoGen](https://aka.ms/ai-agents/autogen)


இந்தப் பாடநெறிக்கு நிரலை இயக்குவதற்கான மேலதிக தகவலுக்கு [பாடநெறி அமைப்புக்குச் செல்லவும்](./00-course-setup/README.md).

## 🙏 உதவ விரும்புகிறீர்களா?

உங்களுக்கு யோசனைகள் உள்ளதா அல்லது எழுத்து அல்லது கோட் பிழைகளை கண்டுபிடித்திருக்கிறீர்களா? [பிரச்சனை எழுப்பவும்](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) அல்லது [இழுக்குக் கோரிக்கை உருவாக்கவும்](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ஒவ்வொரு பாடத்திலும் அடங்கும்

- README இல் உள்ள எழுத்துப்பாடமும் சிறிய வீடியோவும்
- Azure AI Foundry மற்றும் Github மாதிரிகளை ஆதரிக்கும் Python நிரல் எடுத்துக்காட்டுகள் (இலவசம்)
- உங்கள் கற்றலை தொடர கட்டாய இனிய வளங்களுக்கு இணைப்புகள்


## 🗃️ பாடங்கள்

| **பாடம்**                                   | **எழுத்துமற்றும் நிரல்**                              | **வீடியோ**                                                   | **மேலதிக கற்றல்**                                                                       |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI முகவர்கள் மற்றும் முகவர் பயன்பாடுகளுக்கு அறிமுகம்       | [இணைப்பு](./01-intro-to-ai-agents/README.md)          | [வீடியோ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவர் கட்டமைப்புகளை ஆராய்தல்              | [இணைப்பு](./02-explore-agentic-frameworks/README.md)  | [வீடியோ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவர் வடிவமைப்புக் கட்டமைப்புகளை புரிந்துகொள்ளல்     | [இணைப்பு](./03-agentic-design-patterns/README.md)     | [வீடியோ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| கருவி பயன்பாட்டு வடிவமைப்பு மாதிரி                      | [இணைப்பு](./04-tool-use/README.md)                    | [வீடியோ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவர் RAG                                  | [இணைப்பு](./05-agentic-rag/README.md)                 | [வீடியோ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| நம்பகமான AI முகவர்கள் உருவாக்கல்               | [இணைப்பு](./06-building-trustworthy-agents/README.md) | [வீடியோ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| திட்டமிடல் வடிவமைப்பு மாதிரி                      | [இணைப்பு](./07-planning-design/README.md)             | [வீடியோ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| பன்முகவர் வடிவமைப்பு மாதிரி                   | [இணைப்பு](./08-multi-agent/README.md)                 | [வீடியோ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Metacognition Design Pattern                 | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI Agents in Production                      | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Using Agentic Protocols (MCP, A2A and NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Context Engineering for AI Agents            | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Managing Agentic Memory                      | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Exploring Microsoft Agent Framework                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| Building Computer Use Agents (CUA)           | Coming Soon                            |                                                            |                                                                                        |
| Deploying Scalable Agents                    | Coming Soon                            |                                                            |                                                                                        |
| Creating Local AI Agents                     | Coming Soon                               |                                                            |                                                                                        |
| Securing AI Agents                           | Coming Soon                               |                                                            |                                                                                        |

## 🎒 பிற பாடநெறிகள்

எங்கள் குழு பிற பாடநெறிகளை தயாரிக்கிறது! பார்க்கவும்:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

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
 
### முதன்மை கற்றல்
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot தொடர்
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 சமூக நன்றிகள்

Agentic RAG-ஐ காட்டும் முக்கிய குறியீட்டு மாதிரிகளை வழங்கியதற்கு [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) அவர்களுக்கு நன்றி.

## பங்களிப்பு

இந்த திட்டம் பங்களிப்புகளையும் பரிந்துரைகளையும் வரவேற்கிறது. பெரும்பாலான பங்களிப்புகளுக்கு நீங்கள் பங்களிப்பை பயன்படுத்தும் உரிமையை வழங்குகிறீர்கள் மற்றும் அதை உண்மையாகச் செய்கிறீர்கள் என்று அடையாளப்படுத்தும் Contributor License Agreement (CLA) உடன்பட்டுள்ளீர்கள் என்று ஒப்புக்கொள்ள வேண்டும். விவரங்களுக்கு, <https://cla.opensource.microsoft.com> ஐப் பார்வையிடவும்.

நீங்கள் ஒரு pull request சமர்ப்பிக்கும் போது, CLA பாட்டி தானாகவே நீங்கள் CLA வழங்க வேண்டுமா என்று தீர்மானித்துத் தொகுப்பை (PR) சரியான முறையில் அலங்கரிக்கும் (உதா., நிலை சரிபார்ப்பு, கருத்து). பாட்டி வழங்கும் வழிமுறைகளை பின்பற்றுங்கள். அனைத்து களஞ்சியங்களிலும் CLA பயன்படுத்தி இதை ஒருமுறை மட்டுமே செய்ய வேண்டும்.

இந்த திட்டம் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ஐ ஏற்றுக்கொண்டுள்ளது.
மேலும் விவரங்களுக்கு [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) அல்லது மேலதிக கேள்விகள் அல்லது கருத்துகளுக்கு [opencode@microsoft.com](mailto:opencode@microsoft.com) தொடர்பு கொள்ளவும்.

## வர்த்தக அடையாளங்கள்

இந்த திட்டத்தில் திட்டங்கள், பொருட்கள் அல்லது சேவைகளுக்கான வர்த்தக அடையாளங்கள் அல்லது லோகோக்களைக் கொண்டிருக்கலாம். Microsoft வர்த்தக அடையாளங்களின் அங்கீகாரம் மற்றும் பயன்பாடு
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ஐ பின்பற்றவேண்டும்.
Microsoft வர்த்தக அடையாளங்கள் அல்லது லோகோக்களை மாற்றியமைக்கப்பட்ட பதிப்புகளில் பயன்படுத்துவது குழப்பத்தை உருவாக்கக்கூடாது அல்லது Microsoft ஆதரவாக இருக்கிறது எனத் தெரிவிக்கக்கூடாது.
மூன்றாம் பக்கம் வர்த்தக அடையாளங்கள் அல்லது லோகோக்களின் எந்தவொரு பயன்பாட்டும் அந்த மூன்றாம் பக்கர்களின் கொள்கைகளுக்கு உட்பட்டது ஆகும்.

## உதவி பெறுதல்

நீங்கள் தடுமாறுகிறீர்களானால் அல்லது AI செயலிகள் உருவாக்குதல் தொடர்பான கேள்விகள் உண்டானால், சேர்ந்துகொள்ளவும்:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

உत்பத்தி கருத்துகள் அல்லது பிழைகள் இருந்தால் பார்வையிடவும்:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**வெறியுரை**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற க искусிதமுடைய மொழி மாற்றி சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளமை. நாங்கள் துல்லியத்திற்காக முயலினாலும், இயந்திர மொழிபெயர்ப்பு தவறுகள் அல்லது பிழைகள் கொண்டிருக்க வாய்ப்பு உள்ளது என்பதை நினைவில் கொள்ள வேண்டும். மூல ஆவணம் அதன் உள்ளூர் மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பாளர் சேவையை பரிந்துரைக்கின்றோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டினால் ஏற்படும் உரையாடல் முரண்பாடுகள் அல்லது தவறான புரிதலுக்கு எங்களால் பொறுப்பு ஏற்கப்படாது.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->