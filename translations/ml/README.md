# ആരംഭക്കാർക്ക് വേണ്ടി AI ഏജന്റുകൾ - ഒരു കോഴ്‌സ്

![AI Agents for Beginners](../../translated_images/ml/repo-thumbnailv2.06f4a48036fde647.webp)

## AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ആരംഭിക്കാൻ നിങ്ങൾക്ക് അറിയേണ്ടതെല്ലാം പഠിപ്പിക്കുന്ന ഒരു കോഴ്‌സ്

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 ബഹുഭാഷ പിന്തുണ

#### GitHub Action വഴി പിന്തുണയുള്ളത് (സ്വയമൂല്യപ്പെടുത്തിയവും എപ്പോഴും പുതുക്കപെടുന്നതുമായത്)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **സ്ഥാനികമായി ക്ലോൺ ചെയ്യാൻ ഇഷ്ടപ്പെടുന്നുണ്ടോ?**
>
> ഈ റീപ്പോസിറ്ററി 50+ ഭാഷാ പരിഭാഷകൾ ഉൾക്കൊള്ളുന്നു, അടക്കം ഡൗൺലോഡ് വലുപ്പം വളരെ കൂടുതലാണ്. പരിഭാഷകളില്ലാതെ ക്ലോൺ ചെയ്യാൻ sparse checkout ഉപയോഗിക്കുക:
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
> ഇത് കോഴ്‌സ് പൂർത്തിയാക്കാന് ആവശ്യമായ എല്ലാം അതിവേഗത്തിൽ ഡൗൺലോഡ് ചെയ്യാൻ സഹായിക്കും.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**കൂടുതൽ പരിഭാഷാ ഭാഷകൾക്ക് പിന്തുണ ലഭിക്കാൻ ഇവിടെ കൊടുത്തിരിക്കുന്നവ കാണുക [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 ആരംഭിക്കുന്നത്

ഈ കോഴ്‌സിൽ AI ഏജന്റുകൾ നിർമ്മിക്കുന്ന അടിസ്ഥാനങ്ങൾ ഉൾപ്പെടുന്ന പാഠങ്ങൾ ഉണ്ട്. ഓരോ പാഠത്തിലും തക്ക വിഷയമാണ്, അതുകൊണ്ട് നിങ്ങൾക്ക് ഇഷ്ടം പോലെ എവിടूनെങ്കിലും തുടങ്ങാം!

ഈ കോഴ്‌സിന് ബഹുഭാഷ പിന്തുണയുണ്ട്. ഞങ്ങളുടെ [ലഭ്യമായ ഭാഷകൾ ഇവിടെയാണ്](#-multi-language-support).

ജനറേറ്റീവ് AI മോഡലുകൾ ഉപയോഗിക്കുന്നത് ആദ്യമായാണെങ്കിൽ, 21 പാഠങ്ങൾ അടങ്ങിയ [Generative AI For Beginners](https://aka.ms/genai-beginners) കോഴ്‌സ് നോക്കുക.

ഈ റീപ്പോയെ [സ്റ്റാർ (🌟) ചെയ്യാനും](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) [ഫോർക്ക് ചെയ്യാനും](https://github.com/microsoft/ai-agents-for-beginners/fork) മറക്കരുത്, കോഡ് പ്രവർത്തിപ്പിക്കാൻ.

### മറ്റു പഠനാർത്ഥികളുമായി കാണുക, നിങ്ങളുടെ ചോദ്യങ്ങൾക്ക് ഉത്തരം നേടുക

AI ഏജന്റുകൾ നിർമ്മിക്കുന്നതിൽ ഉറച്ചുപിടിച്ച് ചോദിക്കാനുള്ള ചോദ്യങ്ങൾ ഉണ്ടെങ്കിൽ, [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) എന്ന നമ്മുടെ പ്രത്യേക Discord ചാനലിൽ ചേരുക.

### നിങ്ങൾക്ക് വേണ്ടത്

ഈ കോഴ്‌സിലെ ഓരോ പാഠത്തിലും കോഡ് ഉദാഹരണങ്ങൾ ഉൾക്കൊള്ളുന്നു, അവ കടുപ്പമായി code_samples ഫോൾഡറിലാണ്. നിങ്ങൾക്ക് [ഈ റീപ്പോ ഫോർക്ക്](https://github.com/microsoft/ai-agents-for-beginners/fork) ചെയ്ത് താങ്കളുടെ തന്നെ കോപ്പി സൃഷ്ടിക്കാം.

ഈ അഭ്യാസങ്ങളിൽ വലിയ പങ്കുവഹിക്കുന്ന കോഡ് ഉദാഹരണങ്ങൾ Microsoft ഏജന്റ് ഫ്രെയിംവർക്ക് സുഖപ്രദമായി Azure AI Foundry Agent Service V2 ഉപയോഗിക്കുന്നു:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure അക്കൗണ്ട് ആവശ്യമാണ്

മൈക്രോസോഫ്റ്റിന്റെ സ്ഥാപിത AI ഏജന്റ് ഫ്രെയിംവർക്കുകളും സേവനങ്ങളുമാണ് ഈ കോഴ്‌സ് ഉപയോഗിക്കുന്നത്:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

ചില കോഡ് ഉദാഹരണങ്ങൾ OpenAI-ഉപയോഗത്തോട് സാരമായ അനുയോജ്യമായ മറ്റ് പ്രദാതാക്കളായ [MiniMax](https://platform.minimaxi.com/) പോലെയുള്ളവയും പിന്തുണച്ചിട്ടുണ്ട്, ഇവ വലിയ-പ്രസംഗം മോഡലുകൾ (204K ടോക്കൺ വരെ) നൽകുന്നു. ക്രമീകരണ വിവരങ്ങൾക്കായി [Course Setup](./00-course-setup/README.md) കാണുക.

കോഴ്‌സ് കോഡ് റൺ ചെയ്‌തെടുക്കുന്നതിന് കൂടുതല് വിവരങ്ങൾക്കായി, [Course Setup](./00-course-setup/README.md) സന്ദർശിക്കൂ.

## 🙏 സഹായിക്കാൻ താൽപര്യമുണ്ടോ?

നിങ്ങൾക്ക് നിർദ്ദേശങ്ങൾ ഉണ്ടോ, അല്ലെങ്കിൽ സ്പെല്ലിംഗ് അല്ലെങ്കിൽ കോഡ് പിശകുകൾ കണ്ടുപിടിച്ചിട്ടുണ്ടോ? [ഒരു ഇഷ്യു ഉയർത്തുക](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) അല്ലെങ്കിൽ [ഒരു പുൾ റിക്വസ്റ്റ് സൃഷ്ടിക്കുക](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ഓരോ പാഠത്തിലും ഉൾപ്പെടുന്നു

- README ലെ എഴുതിയ പാഠവും ചെറിയ വീഡിയോയും
- Python കോഡ് സാമ്പിളുകൾ Microsoft Agent Framework ഉപയോഗിച്ച് Azure AI Foundry
- പഠനം തുടരാനായി അധിക ഉറവിടങ്ങളിലേക്കുള്ള ലിങ്കുകൾ


## 🗃️ പാഠങ്ങൾ

| **പാഠം**                                   | **വാചകം & കോഡ്**                                | **വീഡിയോ**                                               | **അധിക പഠനം**                                                                         |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI ഏജന്റുകളിൽ ആമുഖവും ഏജന്റ് ഉപയോഗ കേസുകളും | [Link](./01-intro-to-ai-agents/README.md)          | [Video](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ഏജന്റിക് ഫ്രെയിംവർക്ക് പര്യവേക്ഷണം           | [Link](./02-explore-agentic-frameworks/README.md)  | [Video](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ഏജന്റിക് ഡിസൈൻ പാറ്റേണുകൾ മനസ്സിലാക്കൽ       | [Link](./03-agentic-design-patterns/README.md)     | [Video](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ                       | [Link](./04-tool-use/README.md)                    | [Video](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ഏജന്റിക് RAG                                  | [Link](./05-agentic-rag/README.md)                 | [Video](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| വിശ്വസനീയമായ AI ഏജന്റുകൾ നിർമ്മിക്കൽ             | [Link](./06-building-trustworthy-agents/README.md) | [Video](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| പദ്ധതിയിടൽ ഡിസൈൻ പാറ്റേൺ                      | [Link](./07-planning-design/README.md)             | [Video](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ബഹുഏജന്റ് ഡിസൈൻ പാറ്റേൺ                        | [Link](./08-multi-agent/README.md)                 | [Video](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| മെറ്റക്കോഗ്നിഷൻ ഡിസൈൻ പാറ്റേൺ                  | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ഉത്പാദനത്തിൽ AI ഏജൻറുകൾ                        | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ഏജന്റിക് പ്രോട്ടോകോളുകൾ ഉപയോഗിക്കൽ (MCP, A2A, NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ഏജൻറുകൾക്ക് കോൺടെക്‌സ്‌റ്റ് എഞ്ചിനീയറിംഗ്     | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ഏജന്റിക് മെമ്മറി മാനേജ്‌മെന്റ്                   | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft ഏജന്റ് ഫ്രെയിംവർക്ക് പരിശോധിക്കൽ         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| കമ്പ്യൂട്ടർ ഉപയോഗ ഏജൻറുകൾ നിർമ്മിക്കൽ (CUA)       | [Link](./15-browser-use/README.md)     |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| സ്കേബിൾ ഏജൻറുകൾ വിന്യസിക്കൽ                    | വരും                                   |                                                            |                                                                                        |
| പ്രാദേശിക AI ഏജൻറുകൾ സൃഷ്ടിക്കൽ                   | വരും                                   |                                                            |                                                                                        |
| AI ഏജൻറുകൾ സുരക്ഷിക്കുക                        | വരും                                   |                                                            |                                                                                        |

## 🎒 മറ്റ് കോഴ്സുകൾ

ഞങ്ങളുടെ ടീം മറ്റ് കോഴ്സുകളും നിർമ്മിക്കുന്നു! പരിശോധിക്കുക:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ജനറേറ്റീവ് AI സീരീസ്
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### കോർ പഠനം
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### കോപി‌ലോട്ട് സീരീസ്
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 കമ്മ്യൂണിറ്റി നന്ദി

ഏജന്റിക് RAG കാണിക്കുന്ന പ്രധാനപ്പെട്ട കോഡ് സാമ്പിളുകൾ സംഭാവന ചെയ്‌തതിന് [ഷിവം ഗോയൽ](https://www.linkedin.com/in/shivam2003/)ക്ക് നന്ദി. 

## സംഭാവന

ഈ പ്രോജക്റ്റിലേക്ക് സംഭാവനകളും നിർദേശങ്ങളും സ്വാഗതം ചെയ്യുന്നു. ഉപയോക്താക്കൾക്കു് അവകാശപ്പെട്ടതും, യഥാർത്ഥത്തിൽ ഞങ്ങൾക്ക് നിങ്ങളുടെ സംഭാവന ഉപയോഗിക്കാൻ അവകാശം നൽകുന്നതായി പ്രഖ്യാപിക്കുന്ന ഒരു
Contributor License Agreement (CLA) അംഗീകരിക്കണം. വിശദാംശങ്ങൾക്കായി, സന്ദർശിക്കുക <https://cla.opensource.microsoft.com>.

നിങ്ങൾ ഒരു പുൾ അഭ്യർത്ഥന സമർപ്പിക്കുമ്പോൾ, CLA ബോട്ട് സ്വതന്ത്രമായി CLA നൽകേണ്ടത് പരിശോധിക്കുകയും PR യഥാർത്ഥമായി അലങ്കരിക്കുകയും (ഉദാ: സ്ഥിതി പരിശോധന, അഭിപ്രായം) ചെയ്യും. ബോട്ടിന്റെ നിർദ്ദേശങ്ങൾ അവലംബിക്കുക. ഞങ്ങളുടെ CLA ഉപയോഗിക്കുന്ന എല്ലാ റീപ്പോസിടറികളിലും ഇത് നിങ്ങൾ ഒരിക്കൽ മാത്രമേ ചെയ്യേണ്ടതുള്ളൂ.

ഈ പ്രോജക്റ്റ് [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) സ്വീകരിച്ചിട്ടുണ്ട്.
കൂടുതൽ വിവരങ്ങൾക്ക് [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) അന്വേഷിക്കുക അല്ലെങ്കിൽ
[opencode@microsoft.com](mailto:opencode@microsoft.com) എന്നവയെ ബന്ധപ്പെടുക.

## ട്രേഡ്‌മാർക്ക്

ഈ പ്രോജക്റ്റിൽ പ്രോജക്റ്റുകൾ, ഉൽപ്പന്നങ്ങൾ അല്ലെങ്കിൽ സേവനങ്ങൾക്കായി ട്രേഡ്‌മാർക്കുകളോ ലോഗോകളോ ഉൾപ്പെട്ടിരിക്കാം. മൈക്രോസോഫ്റ്റിന്റെ
ട്രേഡ്‌മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകളുടെ അംഗീകൃത ഉപയോഗം [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) അനുസരിച്ചിരിക്കണം.
ഈ പ്രോജക്റ്റിന്റെ മാറ്റം വരുത്തിയ പതിപ്പുകളിൽ മൈക്രോസോഫ്റ്റ് ട്രേഡ്‌മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉപയോഗിക്കുന്നത് შესაძლოა സംശയാസ്പദമാക്കരുത് അല്ലെങ്കിൽ മൈക്രോസോഫ്റ്റിന്റെ സ്പോൺസർഷിപ്പ് സൂചിപ്പിക്കരുത്.
മൂന്നാം पक्ष ട്രേഡ്‌മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകളുടെ ഉപയോഗം ആ ടെക്‌സ്റ്റുകൾക്കു ബാധകമായ നയങ്ങളുടെ വിധേയമായിരിക്കും.

## സഹായം കിട്ടാൻ

AI ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുമ്പോൾ ബുദ്ധിമുട്ടുകയോ, ചോദ്യങ്ങളുണ്ടോ എങ്കിൽ:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ഉൽപ്പന്ന പ്രതികരണങ്ങളോ പിഴവുകളോ ഉണ്ടെങ്കിൽ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസ്വീകരണം**:  
ഈ ഡോക്യുമെന്റ് AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്‌തതാണ്. ഞങ്ങൾ കൃത്യത ഉറപ്പാക്കാൻ ശ്രമിച്ചിരിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായവ ഉണ്ടായിരിക്കും എന്ന കാര്യം ഗ്രഹിക്കുക. താത്പര്യമുള്ള ഭാഷയിൽ ഉള്ള ഒറിജിനൽ ഡോക്യുമെന്റ് പ്രമാണ സ്രോതസ്സായി സന്ദർശിക്കണം. നിർണായക വിവരങ്ങൾക്കായി പ്രൊഫഷണൽ മാനവ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ ഉണ്ടായ ഏതെല്ലാ തെറ്റുപ്രതിഭാസങ്ങൾക്കും ഞങ്ങൾ ഉത്തരവാദിത്വം സ്വീകരിക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->