# ಆರಂಭಿಕರಿಗಾಗಿ AI ಏಜೆಂಟರು - ಒಂದು ಕೋರ್ಸ್

![ಆರಂಬಿಕರಿಗಾಗಿ AI ಏಜೆಂಟರು](../../translated_images/kn/repo-thumbnailv3.917487e234b90100.webp)

## AI ಏಜೆಂಟರನ್ನು ನಿರ್ಮಿಸುವುದನ್ನು ಪ್ರಾರಂಭಿಸಲು ನಿಮಗೆ ತಿಳಿಯಬೇಕಾದ ಎಲ್ಲದನ್ನು ಕಲಿಸುವ ಕೋರ್ಸ್

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 ಬಹುಭಾಷಾ ಬೆಂಬಲ

#### GitHub ಕ್ರಿಯೆಯಿಂದ ಬೆಂಬಲಿಸಲಾಗಿದೆ (ಸ್ವಯಂಚಾಲಿತ ಮತ್ತು ಸದಾ ನವೀಕರಿಸಲಾಗುವದು)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](./README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ಸ್ಥಳೀಯವಾಗಿ ಕ್ಲೋನ್ ಮಾಡಲು ಇಚ್ಛಿಸುವುದೇ?**
>
> ಈ ಸಂಗ್ರಹದಲ್ಲಿ 50 ಕ್ಕೂ ಹೆಚ್ಚು ಭಾಷಾ ಅನುವಾದಗಳು ಸೇರಿವೆ, ಇದು ಡೌನ್ಲೋಡ್ ಗಾತ್ರವನ್ನು ಗಮನಾರ್ಹವಾಗಿ ಹೆಚ್ಚಿಸುತ್ತದೆ. ಅನುವಾದಗಳಿಲ್ಲದೆ ಕ್ಲೋನ್ ಮಾಡಲು sparse checkout ಬಳಸಿ:
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
> ಇದು ನಿಮಗೆ ಕೋರ್ಸ್ ಪೂರ್ಣಗೊಳಿಸಲು ಬೇಕಾದ ಎಲ್ಲವನ್ನೂ ಕಡಿಮೆ ಸಮಯದಲ್ಲಿ ಡೌನ್ಲೋಡ್ ಆಗುವಂತೆ ನೀಡುತ್ತದೆ.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**ನಿಮಗೆ ಹೆಚ್ಚುವರಿ ಅನುವಾದ ಭಾಷೆಗಳ ಬೆಂಬಲ ಬೇಕಾದರೆ, ಅವುಗಳನ್ನು [ಇಲ್ಲಿ](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) ಪಟ್ಟಿ ಮಾಡಲಾಗಿದೆ.**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ATgtXmAS5D)](https://discord.com/invite/ATgtXmAS5D)


## 🌱 ಪ್ರಾರಂಭಿಸುವುದು

ಈ ಕೋರ್ಸ್ AI ಏಜೆಂಟರು ನಿರ್ಮಾಣದ ಮೂಲಭೂತ ವಿಚಾರಗಳನ್ನು ಒಳಗೊಂಡ ಪಾಠಗಳನ್ನು ಹೊಂದಿದೆ. ಪ್ರತಿ ಪಾಠವು ತನ್ನದೇ ವಿಷಯವನ್ನು ಒಳಗೊಂಡಿದ್ದು ನೀವು ತಾನು ಬಯಸಿದ ಸ್ಥಳದಿಂದ ಪ್ರಾರಂಭಿಸಬಹುದು!

ಈ ಕೋರ್ಸ್‌ಗೆ ಬಹುಭಾಷಾ ಬೆಂಬಲ ಇದೆ. ನಮ್ಮ [ಇಲ್ಲಿ ಲಭ್ಯವಿರುವ ಭಾಷೆಗಳು](#-multi-language-support) ಎಂದು ಹೋಗಿ ನೋಡಿ. 

ನೀವು ಜನರೇಟಿವ್ AI ಮಾದರಿಗಳೊಂದಿಗೆ ಮೊದಲ ಬಾರಿಗೆ ನಿರ್ಮಾಣ ಮಾಡುತ್ತಿದ್ದರೆ, ನಮ್ಮ [ಆರಂಬಿಕರಿಗಾಗಿ ಜನರೇಟಿವ್ AI](https://aka.ms/genai-beginners) ಕೋರ್ಸ್ ನೋಡಿ, ಇದರಲ್ಲಿ GenAI తో ನಿರ್ಮಾಣದ 21 ಪಾಠಗಳಿವೆ.

ಈ ಸಂಗ್ರಹವನ್ನು [ನಕ್ಷತ್ರ (🌟) ನೀಡಿ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ಮತ್ತು [ಫೋರ್ಕ್ ಮಾಡಿ](https://github.com/microsoft/ai-agents-for-beginners/fork) ಕೋಡ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಲು ಮರೆಯಬೇಡಿ.

### ಇತರ ಕಲಿತವರನ್ನು ಭೇಟಿ ಮಾಡಿ, ನಿಮ್ಮ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಪಡೆಯಿರಿ

ನೀವು ಇನ್ನೊಂದು ಗೊಂದಲಕ್ಕೆ ಸಿಲುಕಿ ಅಥವಾ AI ಏಜೆಂಟರು ನಿರ್ಮಿಸುವ ಕುರಿತು ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳಿದ್ದರೆ, ನಮ್ಮ ವಿಶೇಷ Discord ಚಾನೆಲ್ [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ಯಲ್ಲಿ ಸೇರಿ.

### ನಿಮಗೆ ಬೇಕಾಗಿರುವುದು 

ಈ ಕೋರ್ಸ್‌ನ ಪ್ರತಿಯೊಂದು ಪಾಠದಲ್ಲೂ ಕೋಡ್‌ನ ಉದಾಹರಣೆಗಳಿವೆ, ಅವುಗಳನ್ನು code_samples ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಕಾಣಬಹುದು. ನೀವು [ಈ ಸಂಗ್ರಹವನ್ನು ಫೋರ್ಕ್](https://github.com/microsoft/ai-agents-for-beginners/fork) ಮಾಡಿ ನಿಮ್ಮದೇ ಪ್ರತಿಯನ್ನು ರಚಿಸಬಹುದು.  

ಈ ವ್ಯಾಯಾಮಗಳಲ್ಲಿ ಕೋಡ್‌ ಉದಾಹರಣೆಗಳು Microsoft Agent Framework ಅನ್ನು Microsoft Foundry Agent Service V2 ಜೊತೆಗೆ ಬಳಸುತ್ತವೆ:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - ಅವಶ್ಯಕ ಅಜೂರ್ ಖಾತೆ

ಈ ಕೋರ್ಸ್ ನಲ್ಲಿ Microsoft ನಿಂದ ಕೆಳಗಿನ AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಮತ್ತು ಸೇವೆಗಳು ಬಳಸಲಾಗುತ್ತವೆ:

- [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/agent-framework/overview/)
- [Microsoft Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

ಕೆಲವು ಕೋಡ್‌ ಉದಾಹರಣೆಗಳು ಇನ್ನಷ್ಟು OpenAI-ಸಹಾಯಕ провೈಡರ್‌ಗಳನ್ನು ಸಹ ಬೆಂಬಲಿಸುತ್ತವೆ, ಉದಾಹರಣೆಗೆ [MiniMax](https://platform.minimaxi.com/), ಇದು ದೊಡ್ಡ ಪ್ರಬಂಧ ಮಾದರಿಗಳನ್ನು (204K tokens ವರೆಗೂ) ನೀಡುತ್ತದೆ. ಸಂರಚನಾ ವಿವರಗಳಿಗಾಗಿ [ಕೋರ್ಸ್ ಸೆಟ್‌ಅಪ್](./00-course-setup/README.md) ನೋಡಿ.

ಈ ಕೋರ್ಸ್‌ಗೆ ಕೋಡ್ ಓಡುವ ಕುರಿತು ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ [ಕೋರ್ಸ್ ಸೆಟ್‌ಅಪ್](./00-course-setup/README.md) ಗೆ ಹೋಗಿ.

## 🙏 ಸಹಾಯ ಮಾಡಲಿಚ್ಚಿಸುತ್ತೀರಾ?

ನಿಮಗೆ ಯಾವುದೇ ಸಲಹೆಗಳು ಇದ್ದರೆ ಅಥವಾ ಮುದ್ರಣ ಅಥವಾ ಕೋಡ್ ದೋಷಗಳನ್ನು ಕಂಡುಹಿಡಿದಿದ್ದರೆ, [ಇಶ್ಯೂ ಮಾಡಿರಿ](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ಅಥವಾ [ಪೂಲ್ ರಿಕ್ವೆಸ್ಟ್ ರಚಿಸಿ](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ಪ್ರತಿಯೊಂದು ಪಾಠದಲ್ಲಿ ಸೇರಿದೆ

- READMEನಲ್ಲಿ ಇರುವ ಬರವಣಿಗೆ ಪಾಠ ಮತ್ತು ಒಂದು ಚಿಕ್ಕ ವೀಡಿಯೊ
- Microsoft Agent Framework ಇನ್ನು Microsoft Foundry ಬಳಸಿ Python ಕೋಡ್ ಉದಾಹರಣೆಗಳು
- ನಿಮ್ಮ ಕಲಿಕೆಯನ್ನು ಮುಂದುವರೆಸಲು ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳಿಗೆ ಲಿಂಕ್‌ಗಳು


## 🗃️ ಪಾಠಗಳು

| **ಪಾಠ**                                   | **ಬರಹ ಮತ್ತು ಕೋಡ್**                                    | **ವೀಡಿಯೋ**                                                  | **ಹೆಚ್ಚುವರಿ ಕಲಿಕೆ**                                                                     |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI ಏಜೆಂಟರ ಪರಿಚಯ ಮತ್ತು ಏಜೆಂಟ್ ಉಪಯೋಗ ಪ್ರಕರಣಗಳು       | [ಲಿಂಕ್](./01-intro-to-ai-agents/README.md)          | [ವೀಡಿಯೋ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [ಲಿಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ಏಜೆಂಟಿಕ್ ಫ್ರೇಮಕ್ವರ್ಕ್‌ಗಳ ಅನ್ವೇಷಣೆ              | [ಲಿಂಕ್](./02-explore-agentic-frameworks/README.md)  | [ವೀಡಿಯೋ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [ಲಿಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ಏಜೆಂಟಿಕ್ ವಿನ್ಯಾಸ ಮಾದರಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ     | [ಲಿಂಕ್](./03-agentic-design-patterns/README.md)     | [ವೀಡಿಯೋ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [ಲಿಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ                      | [ಲಿಂಕ್](./04-tool-use/README.md)                    | [ವೀಡಿಯೋ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [ಲಿಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ಏಜೆಂಟಿಕ್ RAG                                  | [ಲಿಂಕ್](./05-agentic-rag/README.md)                 | [ವೀಡಿಯೋ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [ಲಿಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ನಂಬಕ್ಯ AI ಏಜೆಂಟರು ನಿರ್ಮಾಣ               | [ಲಿಂಕ್](./06-building-trustworthy-agents/README.md) | [ವೀಡಿಯೋ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [ಲಿಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ಯೋಜನೆ ವಿನ್ಯಾಸ ಮಾದರಿ                      | [ಲಿಂಕ್](./07-planning-design/README.md)             | [ವೀಡಿಯೋ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [ಲಿಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ಬಹು ಏಜೆಂಟು ವಿನ್ಯಾಸ ಮಾದರಿ                   | [ಲಿಂಕ್](./08-multi-agent/README.md)                 | [ವೀಡಿಯೋ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [ಲಿಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

| ಮೆಟಾಕಾಗ್ನಿಶನ್ ವಿನ್ಯಾಸ ಮಾದರಿ                 | [ಲೆಂಕ್](./09-metacognition/README.md)               | [ವಿಡಿಯೋ](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [ಲೆಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ಉತ್ಪಾದನೆಯಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳು                      | [ಲೆಂಕ್](./10-ai-agents-production/README.md)        | [ವಿಡಿಯೋ](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [ಲೆಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ಏಜೆಂಟಿಕ್ ಪ್ರೋಟೋಕಾಲ್‌ಗಳ ಬಳಕೆ (MCP, A2A ಮತ್ತು NLWeb) | [ಲೆಂಕ್](./11-agentic-protocols/README.md)           | [ವಿಡಿಯೋ](https://youtu.be/X-Dh9R3Opn8)                                 | [ಲೆಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ಏಜೆಂಟ್‌ಗಳಿಗಾಗಿ ಲುಕಾಯಸ್ಥಿತಿಯ ಇಂಜಿನಿಯರಿಂಗ್            | [ಲೆಂಕ್](./12-context-engineering/README.md)         | [ವಿಡಿಯೋ](https://youtu.be/F5zqRV7gEag)                                 | [ಲೆಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ಏಜೆಂಟಿಕ್ ಮೆಮೊರಿ ನಿರ್ವಹಣೆ                      | [ಲೆಂಕ್](./13-agent-memory/README.md)     |      [ವಿಡಿಯೋ](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಅನ್ವೇಷಣೆ                         | [ಲೆಂಕ್](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| ಕಂಪ್ಯೂಟರ್ ಉಪಯೋಗ ಏಜೆಂಟ್‌ಗಳು (CUA) ನಿರ್ಮಾತ್ಮಕ            | [ಲೆಂಕ್](./15-browser-use/README.md)     |                                                            | [ಲೆಂಕ್](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| ವಿಸ್ತಾರಗೊಳ್ಳುವ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿಯೋಜನೆ                    | [ಲೆಂಕ್](./16-deploying-scalable-agents/README.md) |                                                    | [ಲೆಂಕ್](https://learn.microsoft.com/azure/ai-foundry/agents/overview)                   |
| ಸ್ಥಳೀಯ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸುವುದು                     | [ಲೆಂಕ್](./17-creating-local-ai-agents/README.md)  |                                                    | [ಲೆಂಕ್](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)                    |
| AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಸುರಕ್ಷಿತಗೊಳಿಸುವುದು                           | [ಲೆಂಕ್](./18-securing-ai-agents/README.md)  |                                                            | [ಲೆಂಕ್](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 ಇತರೆ ಕೋರ್ಸ್‌ಗಳು

ನಮ್ಮ ತಂಡ ಇತರೆ ಕೋರ್ಸ್‌ಗಳನ್ನು ಉತ್ಪಾದಿಸುತ್ತದೆ! ಪರಿಶೀಲಿಸಿ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### ಅಝ್ಯುರ್ / ಎಡ್ಜ್ / MCP / ಏಜೆಂಟ್‌ಗಳು
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ಸೃಜನಾತ್ಮಕ AI ಸರಣಿ
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### ಮೂಲ ಅಧ್ಯಯನ
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ಕೋಪೈಲಟ್ ಸರಣಿ
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 ಸಮುದಾಯದ ಧನ್ಯವಾದಗಳು

ಅಜೆಂಟಿಕ್ RAG ಯನ್ನು ತೋರಿಸುವ ಪ್ರಮುಖ ಕೋಡ್ ಮಾದರಿಗಳನ್ನು ಕೊಡುಗೆ ನೀಡಿರುವ [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) ಅವರಿಗೆ ಧನ್ಯವಾದಗಳು. 

## ಕೊಡುಗೆ ನೀಡುವುದು

ಈ ಯೋಜನೆ ಕೊಡುಗೆ ಮತ್ತು ಸಲಹೆಗಳನ್ನು ಸ್ವಾಗತಿಸುತ್ತದೆ. ಬಹುತೇಕ ಕೊಡುಗೆಗಳಿಗೆ ನೀವು ಒಪ್ಪಬೇಕಾಗುತ್ತದೆ
ಕೊಡುಗೆದಾರರ ಲائسನ್ಸ್ ಒಪ್ಪಂದ (CLA) ಅನ್ನು, ನೀವು ತನ್ನ ಹಕ್ಕುಗಳನ್ನು ಹೊಂದಿದಂತೆ ಮತ್ತು ನಿಜವಾಗಿಯೂ
ನಿಮ್ಮ ಕೊಡುಗೆ ಬಳಸುವ ಹಕ್ಕುಗಳನ್ನು ನಮಗೆ ನೀಡುತ್ತೀರಿ ಎಂದು ಘೋಷಿಸುವಂತೆ. ವಿವರಗಳಿಗೆ, ಭೇಟಿ ನೀಡಿ <https://cla.opensource.microsoft.com>.

ನೀವು ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ಸಲ್ಲಿಸಿದಾಗ, CLA ಬಾಟ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನೀವು CLA ಒದಗಿಸಬೇಕೇ ಇಲ್ಲವೇ ಎಂದು ಪತ್ತೆಮಾಡುತ್ತದೆ
ಮತ್ತು PR ಯನ್ನು ಸೂಕ್ತವಾಗಿ ಅಲಂಕರಿಸುತ್ತದೆ (ಉದಾ: ಸ್ಥಿತಿ ಪರಿಶೀಲನೆ, ಕಾಮೆಂಟ್). ಸರಳವಾಗಿ ಬಾಟ್ ನೀಡುವ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ.
ನೀವು ಈ ಎಲ್ಲ ರೆಪೋಗಳಲ್ಲಿಯೂ ಒಂದು ಬಾರಿ ಮಾತ್ರ ಈ ಕಾರ್ಯವನ್ನು ಮಾಡಲು ಬೇಕಾಗುತ್ತದೆ.

ಈ ಯೋಜನೆ [ಮೈಕ್ರೋಸಾಫ್ಟ್ ಓಪನ್ ಸೋರ್ಸ್ ನಡವಳಿ ಕೋಡ್](https://opensource.microsoft.com/codeofconduct/) ಅನ್ನು ಅನುಸರಿಸಿದೆ.
ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗೆ [ನಡವಳಿ ಕೋಡ್ FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ಅನ್ನು ನೋಡಿ ಅಥವಾ
ಯಾವುದೇ ಹೆಚ್ಚುವರಿ ಪ್ರಶ್ನೆಗಳು ಅಥವಾ ಕಾಮೆಂಟ್‌ಗಳಿಗಾಗಿ [opencode@microsoft.com](mailto:opencode@microsoft.com) ಸಂಪರ್ಕಿಸಿ.

## ಟ್ರೇಡ್ಮಾರ್ಕ್‌ಗಳು

ಈ ಯೋಜನೆ ಯೋಜನೆಗಳು, ಉತ್ಪನ್ನಗಳು ಅಥವಾ ಸೇವೆಗಳ ಟ್ರೇಡ್ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೊಗಳನ್ನು ಒಳಗೊಂಡಿರಬಹುದು. ಮೈಕ್ರೋಸಾಫ್ಟ್
ಟ್ರೇಡ್ಮಾರ್ಕ್‌ಗಳ ಅಥವಾ ಲೋಗೊಗಳ ಅಂಗೀಕೃತ ಬಳಕೆ ಅನ್ವಯಿಸುತ್ತದೆ ಮತ್ತು ಅನುಸರಿಸಬೇಕು
[ಮೈಕ್ರೋಸಾಫ್ಟ್ ಟ್ರೇಡ್ಮಾರ್ಕ್ ಮತ್ತು ಬ್ರಾಂಡ್ ಮಾರ್ಗಸೂಚಿ](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
ಮೈಕ್ರೋಸಾಫ್ಟ್ ಟ್ರೇಡ್ಮಾರ್ಕ್‌ಗಳ ಅಥವಾ ಲೋಗೊಗಳ ಈ ಯೋಜನೆಯ ತಿದ್ದುಪಡಿಸಲಾದ ಆವೃತ್ತಿಗಳಲ್ಲಿ ಬಳಕೆ ಗೊಂದಲ ಉಂಟುಮಾಡಬಾರದು ಅಥವಾ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಸ್ಪಾನ್ಸರ್‌ಶಿಪ್ ಅನ್ನು ಸೂಚಿಸಬಾರದು.
ಮೂರನೇ ಪಕ್ಷದ ಟ್ರೇಡ್ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೊಗಳ ಯಾವುದೇ ಬಳಕೆ ಆ ಮೂರನೇ ಪಕ್ಷಗಳ ನಿಯಮಗಳಿಗೆ ಆಧಾರಿತವಾಗಿದೆ.

## ಸಹಾಯ ಪಡೆಯುವುದು


ನೀವು ಸ್ಥಗಿತಗೊಳ್ಳುವುದಾದರೆ ಅಥವಾ AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವ ಕುರಿತು ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳು ಇದ್ದರೆ, ಸೇರಿ:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ಉತ್ಪನ್ನ ಪ್ರತಿಕ್ರಿಯೆ ಅಥವಾ ನಿರ್ಮಾಣದ ಸಮಯದಲ್ಲಿ ದೋಷಗಳಿದ್ದರೆ ಭೇಟಿನೀಡಿ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->