# ஆரம்பக்கூறுகளுக்கான ஐஐ முகவர்கள் - ஒரு பாடநெறி

![AI Agents for Beginners](../../translated_images/ta/repo-thumbnailv3.917487e234b90100.webp)

## ஐஐ முகவர்களை உருவாக்க தொடங்க தேவைப்படும் அனைத்தையும் கற்பிக்கும் ஒரு பாடநெறி

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 பலமொழி ஆதரவு

#### GitHub செயல் மூலம் ஆதரிப்பு (தானாகவும் எப்பேச்சும் புதுப்பிக்கும்)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](./README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **உள்ளூர் முறையில் க்ரோன் செய்துக்கொள்ள விரும்புகிறீர்களா?**
>
> இந்த களஞ்சியத்தில் 50+ மொழி மொழிபெயர்ப்புகள் உள்ளன, இது பதிவிறக்கும் அளவை மிக அதிகமாக்கும். மொழிபெயர்ப்புகள் இல்லாமல் க்ரோன் செய்ய sparse checkout பயன்படுத்தவும்:
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
> இது பாடநெறியை நிறைவு செய்ய தேவையான அனைத்தையும் மிக விரைவான பதிவிறக்கத்துடன் உங்களுக்குக் கொடுக்கும்.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**மேலும் மொழிபெயர்ப்பு மொழிகள் ஆதரிக்கப்பட வேண்டுமானால், அவை [இங்கு](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) பட்டியலிடப்பட்டுள்ளன.**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ATgtXmAS5D)](https://discord.com/invite/ATgtXmAS5D)


## 🌱 தொடங்குதல்

இந்த பாடநெறியில் AI முகவர்களை உருவாக்குவதற்கான அடிப்படைகள் உள்ள பாடங்களைக் கொண்டுள்ளது. ஒவ்வொரு பாடமும் தன் தலைப்பை உள்ளடக்கியது; எனவே நீங்கள் விரும்பிய இடத்தில் தொடங்கலாம்!

இந்த பாடநெறிக்கு பலமொழி ஆதரவு உள்ளது. எங்கள் [கிடையக மொழிகள் இங்கே](#-multi-language-support) செல்லவும்.

இது உங்கள் முதல் முறையாக ஜெனரேட்டிவ் AI மாதிரிகளுடன் பணிபுரியுமானால், எங்கள் [ஆரம்பக்காரர்களுக்கான ஜெனரேட்டிவ் AI](https://aka.ms/genai-beginners) பாடநெறியை பார்த்து கொள்ளவும், இதில் GenAI உடன் வேலை செய்ய 21 பாடங்கள் உள்ளன.

இந்த களஞ்சியத்தை [தாரகை (🌟) செய்யவும்](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) மற்றும் [ஃபோர்க் செய்யவும்](https://github.com/microsoft/ai-agents-for-beginners/fork) குறியீட்டை இயக்க.

### மற்ற மாணவர்களை சந்திக்கவும், உங்கள் கேள்விகளுக்கு பதில்கள் பெறவும்

நீங்கள் சிக்கலில் சிக்கினால் அல்லது AI முகவர்களை உருவாக்குவது குறித்த கேள்விகள் இருந்தால், எங்கள் பிேிபார்ந்த Discord சேனல் [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) இல் சேரவும்.

### என்ன தேவை

இந்த பாடநெறியில் ஒவ்வொரு பாடத்திலும் குறியீடு எடுத்துக்காட்டுகள் உள்ளன; அவை code_samples கோப்பகத்தில் கிடைக்கும். உங்கள் சொந்த நகலை உருவாக்க [இந்த களஞ்சியத்தை ஃபோர்க் செய்யவும்](https://github.com/microsoft/ai-agents-for-beginners/fork).

இந்த பயிற்சியில் உள்ள குறியீடு எடுத்துக்காட்டுகள் Microsoft Agent Framework ஐ Microsoft Foundry Agent சேவை V2 உடன் பயன்படுத்துகின்றன:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure கணக்கு தேவை

இந்த பாடநெறி Microsoft நிறுவனத்தின் பின்வரும் AI முகவர் கட்டமைப்புகள் மற்றும் சேவைகளை பயன்படுத்துகிறது:

- [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/agent-framework/overview/)
- [Microsoft Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

கொஞ்சம் குறியீடு எடுத்துக்காட்டுகள் துணை OpenAI-ஐப் போன்று செயல்படும் வழங்குநர்களை (உதாரணமாக [MiniMax](https://platform.minimaxi.com/), இது பெரிய உள்ளடக்கம் மாதிரிகள் (204K டோக்கன்கள் வரை) வழங்குகிறது) ஆதரிக்கின்றன. அமைப்புக்கான விவரங்களுக்கு [பாடநெறி அமைப்பு](./00-course-setup/README.md) பெறவும்.

இந்த பாடநெறிக்கான குறியீட்டை இயக்க அதிகமான தகவலுக்கு [பாடநெறி அமைப்பு](./00-course-setup/README.md) என்பதற்கு செல்லவும்.

## 🙏 உதவ விரும்புகிறீர்களா?

உரிமையான சிக்கல்கள் அல்லது எழுத்துப்பிழைகள் இருந்தால் [சிக்கல் எழுப்பவும்](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) அல்லது [புல் கோரிக்கை உருவாக்கவும்](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ஒவ்வொரு பாடத்திலும் சேர்க்கப்பட்டுள்ளது

- README-வில் எழுதப்பட்ட பாடமும், ஒரு குறும்படமும்
- Microsoft Agent Framework உடன் Python குறியீடு எடுத்துக்காட்டுகள் Microsoft Foundry பயன்படுத்தி
- உங்கள் கற்றலை தொடர செல்லும் கூடுதல் வளங்களுக்கான இணைப்புகள்


## 🗃️ பாடங்கள்

| **பாடம்**                                   | **உரை & குறியீடு**                             | **வீடியோ**                                                  | **கூடுதல் கற்றல்**                                                                     |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ஐஐ முகவர்கள் மற்றும் முகவர் பயன்பாடுகளுக்கு அறிமுகம்  | [இணைப்பு](./01-intro-to-ai-agents/README.md)        | [வீடியோ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ஐஐ முகவர் கட்டமைப்புகளை ஆய்வு செய்யுதல்           | [இணைப்பு](./02-explore-agentic-frameworks/README.md)  | [வீடியோ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ஐஐ முகவர் வடிவமைப்பு வடிவமுறைகளைப் புரிந்துகொள்ளுதல்     | [இணைப்பு](./03-agentic-design-patterns/README.md)     | [வீடியோ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| கருவி பயன்பாட்டு வடிவமைப்பு வடிவம்                    | [இணைப்பு](./04-tool-use/README.md)                    | [வீடியோ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| முகவரின் RAG                                      | [இணைப்பு](./05-agentic-rag/README.md)                 | [வீடியோ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| நம்பகமான ஐஐ முகவர்களை உருவாக்குதல்                | [இணைப்பு](./06-building-trustworthy-agents/README.md) | [வீடியோ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| திட்டமிடல் வடிவமைப்பு வடிவம்                          | [இணைப்பு](./07-planning-design/README.md)             | [வீடியோ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| பல முகவர் வடிவமைப்பு வடிவம்                          | [இணைப்பு](./08-multi-agent/README.md)                 | [வீடியோ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [இணைப்பு](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

| மெடாகானிஷன் வடிவமைப்பு முறை               | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| உற்பத்தியில் AI முகவரிகள்                      | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ஏஜென்டிக் நெறிமுறைகளைப் பயன்படுத்துதல் (MCP, A2A மற்றும் NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI முகவரிகளுக்கான சூழல் பொறியியல்            | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ஏஜென்டிக் நினைவைக் கையாளுதல்                      | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| மைக்ரோசாஃப்ட் ஏஜென்ட் சூழல் ஆராய்ச்சி                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| கணினி பயனர் முகவர்களை உருவாக்குதல் (CUA)           | [Link](./15-browser-use/README.md)     |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| பரிமாணக்கூடிய முகவரிகளை மூடுதல்                    | [Link](./16-deploying-scalable-agents/README.md) |                                                    | [Link](https://learn.microsoft.com/azure/ai-foundry/agents/overview)                   |
| உள்ளூர் AI முகவரிகளை உருவாக்குதல்                     | [Link](./17-creating-local-ai-agents/README.md)  |                                                    | [Link](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)                    |
| AI முகவரிகளை பாதுகாப்பது                           | [Link](./18-securing-ai-agents/README.md)  |                                                            | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 பிற பாடங்கள்

எங்கள் குழு பிற பாடங்களையும் உருவாக்குகிறது! இதைப் பார்க்கவும்:

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
 
### மூலக் கற்றல்
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

## 🌟 சமூகம் நன்றி

Agentic RAG-ஐ காட்டும் முக்கிய குறியீட்டு எடுத்துக்காட்டுகளுக்கு [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) அவர்களுக்கு நன்றி .

## பங்களிப்பது

இந்தத் திட்டம் பங்களிப்புகளையும் பரிந்துரைகளையும் வரவேற்கிறது. பெரும்பாலான பங்களிப்புகள் நீங்கள்
பங்களிப்பை பயன்படுத்துவதற்கு உரிமை உங்களிடம் இருப்பதாகவும், உண்மையில் அங்கீகாரம் தருகிறீர்கள் என்று
தெரிவிக்கும் Contributor License Agreement (CLA)-க்கு ஒப்புதல் தெரிவிக்க வேண்டியுள்ளது. விரிவுகளுக்கு, <https://cla.opensource.microsoft.com> பார்க்கவும்.

நீங்கள் ஒரு pull request சமர்ப்பித்தால், CLA பாட்டன் தானாகவே நீங்கள் CLA வழங்க வேண்டுமா என்பதை தீர்மானித்து
PR-ஐ (உதாரணமாக, நிலை சரிபார்ப்பு, கருத்து) முறையாக அழகுபடுத்தும். பாட்டன் வழங்கும் அறிவுறுத்தல்களைப் பின்பற்றவும்.
எங்கள் CLA பயன்படுத்தும் அனைத்து ரெப்போ-களிலும் இது ஒருமுறை மட்டுமே செய்யவேண்டும்.

இந்தத் திட்டம் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)ஐ ஏற்றுக்கொண்டுள்ளது.
கூடுதல் விவரங்களுக்கு [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) பார்க்கவும் அல்லது
எந்தவொரு கூடுதல் கேள்விகள் அல்லது கருத்துகளுக்கு [opencode@microsoft.com](mailto:opencode@microsoft.com) என்பதிலேயே தொடர்பு கொள்ளவும்.

## வர்த்தகக் குறியீடுகள்

இந்தத் திட்டத்தில் திட்டங்கள், தயாரிப்புகள், அல்லது சேவைகளுக்கான வர்த்தகக் குறியீடுகள் அல்லது லோகோக்கள் இருக்கலாம்.
Microsoft வர்த்தகக் குறியீடுகள் அல்லது லோகோக்களை அங்கீகாரம் பெற்ற பயன்முறை மற்றும்
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)ஐ பின்பற்ற வேண்டும்.
மாற்றியமைக்கப்பட்ட இந்தத் திட்டத்தில் Microsoft வர்த்தகக் குறியீடுகள் அல்லது லோகோக்களைப் பயன்படுத்துவது குழப்பத்தை ஏற்படுத்தவோ Microsoft ஆதரவாகக் காட்டவோ கூடாது.
மூன்றாம் பக்கம் வர்த்தகக் குறியீடுகள் அல்லது லோகோக்களின் பயன்பாடு அந்த மூன்றாம் பக்கம் விதிகளுக்கு உட்பட்டது.

## உதவி பெறுவது எப்படி


நீங்கள் சிக்கினால் அல்லது AI செயலிகளை உருவாக்கும் போது கேள்விகள் இருந்தால், சேர்ந்துகொள்ளவும்:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

தயாரிப்பு தொடர்பான கருத்துகள் அல்லது பிழைகள் இருந்தால், இக்கண்காணிப்பு செய்யவும்:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->