# തുടക്കക്കാർക്കുള്ള AI ഏജന്റുകൾ - ഒരു കോഴ്‌സ്

![തുടക്കക്കാർക്കുള്ള AI ഏജന്റുകൾ](../../translated_images/ml/repo-thumbnailv2.06f4a48036fde647.webp)

## AI ഏജന്റുകൾ നിർമ്മിക്കാൻ നിങ്ങൾ അറിയേണ്ടവയെല്ലാം പഠിപ്പിക്കുന്ന ഒരു കോഴ്‌സ്

[![GitHub ലൈസൻസ്](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub സംഭാവകങ്ങൾ](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub പ്രശ്നങ്ങൾ](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub പുൾ-റിക്വസ്റ്റുകൾ](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs സ്വാഗതം](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 ബഹുസ്വര പിന്തുണ

#### GitHub ആക്ഷൻ മുഖേന പിന്തുണ (സ്വയം പ്രവർത്തിക്കുന്നതും എപ്പോഴും നവീകരിക്കുന്നതുമായത്)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **പ്രാദേശികമായി ക്ലോൺ ചെയ്യാൻ ആഗ്രഹമുണ്ടോ?**
>
> ഈ റീപോസിറ്ററിയിൽ 50-க்கும் മുകളിൽ ഭാഷാ വിവർത്തനങ്ങൾ ഉൾക്കൊള്ളിച്ചിട്ടുള്ളതുകൊണ്ട് ഡൗൺലോഡ് വലുപ്പം വളരെ കൂടുതലാകും. വിവർത്തനങ്ങളില്ലാതെ ക്ലോൺ ചെയ്യാൻ, സ്പാർസ് ചെക്ക്ഔട്ട് ഉപയോഗിക്കുക:
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
> ഈ വഴി കോഴ്‌സ് പൂർത്തിയാക്കാൻ വേണ്ട എല്ലാവരും എളുപ്പത്തിൽ ഡൗൺലോഡ് ചെയ്യാം.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**കൂടുതൽ വിവർത്തന ഭാഷകൾക്ക് പിന്തുണ ആവശ്യപ്പെടുന്നവർക്കായി, അവ ഇവിടെയാണ് പട്ടികയിട്ടിരിക്കുന്നത് [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md).**

[![GitHub വാച്ചേഴ്സ്](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub ഫോർക്ക്സ്](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub സ്റ്റാറുകൾ](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry ഡിസ്‌കോർഡ്](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 തുടക്കം കുറിച്ചുകൊണ്ട്

ഈ കോഴ്‌സിൽ AI ഏജന്റുകൾ നിർമ്മിക്കുന്ന അടിസ്ഥാന കാര്യങ്ങൾക്കുള്ള പാഠങ്ങളുണ്ട്. ഓരോ പാഠവും സ്വതന്ത്ര വിഷയം കൊണ്ടാണ്, അതിനാൽ നിങ്ങൾക്ക് ഇഷ്ടമായിടത്ത് തുടങ്ങാം!

ഈ കോഴ്‌സിന് ബഹുസ്വര പിന്തുണ ലഭ്യമാണ്. [ഇവിടെ ലഭ്യമായ ഭാഷകൾക്ക്](#-multi-language-support) പോകുക.

നിങ്ങൾ ആദ്യമായി സൃഷ്ടിപ്പുകാർ AI മോഡലുകളുമായി പ്രവർത്തിക്കുന്നുവെങ്കിൽ, ഞങ്ങളുടെ [Generative AI For Beginners](https://aka.ms/genai-beginners) കോഴ്‌സ് പരീക്ഷിക്കൂ, അതിൽ GenAI ഉപയോഗിച്ച് നിർമ്മിക്കാനുള്ള 21 ലെസ്സനുകൾ ഉൾക്കൊള്ളിച്ചിരിക്കുന്നു.

ഈ റീപോസിറ്ററി [സ്റ്റാർ (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ചെയ്യാനും [ഫോর্ক്](https://github.com/microsoft/ai-agents-for-beginners/fork) ചെയ്ത് കോഡ് പരീക്ഷിക്കാൻ മറക്കരുത്.

### മറ്റ് പഠിക്കുന്നവരുമായി ബന്ധപ്പെടുക, നിങ്ങളുടെ ചോദ്യങ്ങൾക്ക് മറുപടി നേടുക

നിങ്ങൾക്ക് AI ഏജന്റുകൾ നിർമ്മിക്കുന്നതിലുണ്ടാകുന്ന പ്രശ്നങ്ങളോ ചോദ്യങ്ങളോ എങ്കിൽ, ഞങ്ങളുടെ [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ൽ ഉള്ള സമർപ്പിത ഡിസ്‌കോർഡ് ചാനലിൽ ചേർക്കുക.

### നിങ്ങൾക്ക് വേണ്ടത്

ഈ കോഴ്‌സിലെ ഓരോ പാഠവും കോഡ് ഉദാഹരണങ്ങളോടെയാണ്, അവ കോഡ്_സാമ്പിൾസ് ഫോൾഡറിലുണ്ട്. നിങ്ങളുടെ സ്വന്തം പകർപ്പ് സൃഷ്ടിച്ചെടുക്കാൻ നിങ്ങൾക്ക് ഈ റീപോസിറ്ററി [ഫോർക്കുചെയ്യാൻ](https://github.com/microsoft/ai-agents-for-beginners/fork) കഴിയും.

ഈ ഉദാഹരണ കോഡുകൾ Microsoft Agent Framework-നെ Azure AI Foundry Agent Service V2-നോടൊപ്പം ഉപയോഗിക്കുന്നു:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure അക്കൗണ്ട് ആവശ്യമാണ്

ഈ കോഴ്‌സ് അബദ്ധമാണ് Microsoft-ന്റെ താഴെ പറയുന്ന AI ഏജന്റ് ഫ്രെയിംവർക്കുകളും സേവനങ്ങളും ഉപയോഗിക്കുന്നത്:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

കുറച്ച് കോഡ് സാമ്പിളുകൾ [MiniMax](https://platform.minimaxi.com/) പോലുള്ള മറ്റ് OpenAI-നെ അനുകൂലിക്കുന്ന സേവനദായകരേയും പിന്തുണയ്ക്കുന്നു, കൂടാതെ ഇത് വലിയ സാന്ദ്രതാ മോഡലുകൾ (204K ടോക്കണുകൾ വരെ) ഉണ്ട്. കോൺഫിഗറേഷൻ വിവരങ്ങൾക്ക് [Course Setup](./00-course-setup/README.md) നോക്കുക.

ഈ കോഴ്‌സിന്റെ കോഡ് പ്രവർത്തിപ്പിക്കുന്നതിന് കൂടുതൽ വിവരങ്ങൾക്കായി, [Course Setup](./00-course-setup/README.md) കാണുക.

## 🙏 സഹായം വേണോ?

നിങ്ങൾക്ക് നിർദ്ദേശങ്ങളോ അല്ലെങ്കിൽ പിശകുകളോ കണ്ടുപിടിച്ചിട്ടുണ്ടെങ്കിൽ, [ഇഷ്യു ഉന്നയിക്കുക](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) അല്ലെങ്കിൽ [പുൾ റിക്വസ്റ്റ് സൃഷ്ടിക്കുക](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ഓരോ പാഠത്തിലുമുള്ളത്

- README-യിൽ ഉള്ള എഴുത്ത് പാഠവും ഒരു ചെറിയ വീഡിയോയും
- Microsoft Agent Framework ഉപയോഗിച്ചുള്ള Python കോഡ് സാമ്പിളുകൾ Azure AI Foundry-യോടൊപ്പം
- തുടരുന്നതിന് അധിക പഠനസ്രോതസുകളുടെ ലിങ്കുകൾ


## 🗃️ പാഠങ്ങൾ

| **പാഠം**                                     | **വാചകം & കോഡ്**                                    | **വീഡിയോ**                                                | **അധിക പഠനം**                                                                         |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI ഏജന്റുകളെ പരിചയപ്പെടുക, ഏജന്റ് ഉപയോഗകാര്യങ്ങൾ | [ലിങ്ക്](./01-intro-to-ai-agents/README.md)          | [വീഡിയോ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ഏജന്റിക് ഫ്രെയിംവർക്കുകൾ അന്വേഷിക്കല്‍          | [ലിങ്ക്](./02-explore-agentic-frameworks/README.md)  | [വീഡിയോ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ഏജന്റിക് ഡിസൈൻ പാറ്റേണുകൾ മനസ്സിലാക്കൽ     | [ലിങ്ക്](./03-agentic-design-patterns/README.md)     | [വീഡിയോ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ടൂൾ ഉപയോഗ ഡിസൈൻ പാറ്റേൺ                      | [ലിങ്ക്](./04-tool-use/README.md)                    | [വീഡിയോ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ഏജന്റിക് RAG                                  | [ലിങ്ക്](./05-agentic-rag/README.md)                 | [വീഡിയോ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| വിശ്വസനീയമായ AI ഏജന്റുകൾ നിർമ്മിക്കൽ          | [ലിങ്ക്](./06-building-trustworthy-agents/README.md) | [വീഡിയോ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| പദ്ധതിയിടൽ ഡിസൈൻ പാറ്റേൺ                      | [ലിങ്ക്](./07-planning-design/README.md)             | [വീഡിയോ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ബഹുസംഖ്യ ഏജന്റ് ഡിസൈൻ പാറ്റേൺ                 | [ലിങ്ക്](./08-multi-agent/README.md)                 | [വീഡിയോ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| മെറ്റാകോഗ്നിഷൻ ഡിസൈൻ പാറ്റേൺ                 | [ലിങ്ക്](./09-metacognition/README.md)               | [വീഡിയോ](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| പ്രൊഡക്ഷനിലെ AI ഏജൻറുകൾ                      | [ലിങ്ക്](./10-ai-agents-production/README.md)        | [വീഡിയോ](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ഏജന്റിക് പ്രോട്ടോകോളുകൾ ഉപയോഗിച്ച് (MCP, A2A, NLWeb) | [ലിങ്ക്](./11-agentic-protocols/README.md)           | [വീഡിയോ](https://youtu.be/X-Dh9R3Opn8)                                 | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ഏജൻറുകൾക്കുള്ള കോൺടെക്സ്റ്റ് എഞ്ചിനീയറിംഗ്            | [ലിങ്ക്](./12-context-engineering/README.md)         | [വീഡിയോ](https://youtu.be/F5zqRV7gEag)                                 | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ഏജന്റിക് മെമ്മറി മാനേജ് ചെയ്യൽ                      | [ലിങ്ക്](./13-agent-memory/README.md)     |      [വീഡിയോ](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് പരിശോധിക്കൽ                         | [ലിങ്ക്](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| കമ്പ്യൂട്ടർ ഉപയോക്തൃ ഏജൻറുകൾ നിർമ്മിക്കൽ (CUA)           | [ലിങ്ക്](./15-browser-use/README.md)     |                                                            | [ലിങ്ക്](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| സ്കെയ്ലബിള്‍ ഏജൻറുകൾ വിനയായി ഉപയോഗിക്കൽ                    | ഉടൻ വരുന്നു                            |                                                            |                                                                                        |
| പ്രാദേശിക AI ഏജൻറുകൾ സൃഷ്‌ടിക്കൽ                     | ഉടൻ വരുന്നു                               |                                                            |                                                                                        |
| AI ഏജൻറുകൾ സേഫ്‌ഗാർഡ് ചെയ്യൽ                           | [ലിങ്ക്](./18-securing-ai-agents/README.md)  |                                                            | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 മറ്റുള്ള കോഴ്സുകൾ

ഞങ്ങളുടെ ടീം മറ്റ് കോഴ്സുകളും ഉത്പാദിപ്പിക്കുന്നു! പരിശോധിക്കുക:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### ലാംഗ്‌ചെയിൻ
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### അസ്യൂർ / എഡ്ജ് / MCP / ഏജൻറ്റുകൾ
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ജെനറേറ്റീവ് AI സീരീസ്
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### മുള്ള പഠനം
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![ഡാറ്റ സയൻസ് ഫോർ ബിഗിനേഴ്സ്](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![സൈബർസെക്യൂരിറ്റി ഫോർ ബിഗിനേഴ്സ്](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![വെബ് ഡെവ് ഫോർ ബിഗിനേഴ്സ്](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![ഐഒടി ഫോർ ബിഗിനേഴ്സ്](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR ഡെവലപ്മെന്റ് ഫോർ ബിഗിനേഴ്സ്](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### കോപൈലറ്റ് സീരീസ്
[![AI ചേർത്ത് പ്രോഗ്രാമിംഗിനുള്ള കോപൈലറ്റ്](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET കോപൈലറ്റ്](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![കോപൈലറ്റ് അഡ്വഞ്ചർ](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 കമ്മ്യൂണിറ്റി നന്ദി

ഏജന്റിക് RAG കൈകാര്യം ചെയ്യുന്ന പ്രധാന കോഡ് സാമ്പിളുകൾ സംഭാവന ചെയ്തതിന് [ശിവം ഗോയൽ](https://www.linkedin.com/in/shivam2003/)  ന് നന്ദി. 

## സംഭാവനകൾ

ഈ പ്രോജക്ട് സംഭാവനകളും നിർദ്ദേശങ്ങളും സ്വാഗതം ചെയ്യുന്നു.  
പല സംഭാവനകളും നിങ്ങളെ ഒരു 
Contributor License Agreement (CLA) യുമായി ഒപ്പിടാൻ ആവശ്യപ്പെടും, ഇത് നിങ്ങൾക്ക് അവകാശമുള്ളതും ഉപകാരപ്രദമായതും ആണെന്ന് ഉറപ്പാക്കാൻ. വിശദാംശങ്ങൾക്ക്, സന്ദർശിക്കുക <https://cla.opensource.microsoft.com>.

നിങ്ങൾ ഒരു പുൾ അഭ്യർത്ഥന സമർപ്പിക്കുമ്പോൾ, CLA ബോട്ട് സ്വയം അടയാളപ്പെടുത്തി CLA നൽകേണ്ടതുണ്ടോ എന്ന് നിർണ്ണയിക്കും, PR യെ അനുയോജ്യമായി അലങ്കരിക്കും (ഉദാ: സ്റ്റാറ്റസ് ചെക്ക്, കോമെന്റ്). ബോട്ട് നൽകിയ നിർദ്ദേശങ്ങൾ പിന്തുടരുക. ഞങ്ങളുടെ CLA ഉപയോഗിക്കുന്ന എല്ലാ റിപ്പോസിറ്ററികളിലും നിങ്ങൾ ഒരു തവണ മാത്രം ഇത് ചെയ്യേണ്ടതുണ്ട്.

ഈ പ്രോജക്ട് [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) സ്വീകരിച്ചിട്ടുണ്ട്.
കൂടുതൽ വിവരങ്ങൾക്ക് [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)  കാണുക അല്ലെങ്കിൽ 
അധീകാര്യമായ ചോദ്യംകൾക്കായി [opencode@microsoft.com](mailto:opencode@microsoft.com)  ബന്ധപ്പെടുക.

## ട്രേഡ്മാർക്കുകൾ

ഈ പ്രോജക്ടിൽ പ്രോജക്ടുകൾ, ഉൽപ്പന്നങ്ങൾ, സേവനങ്ങൾ എന്നിവയ്ക്ക് വേണ്ടി ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉണ്ടായിരിക്കാം. Microsoft 
ട്രേഡ്മാർക്കുകളും ലോഗോകളും ഉപയോഗിക്കുന്നതിനുള്ള അവകാശം 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)  അനുസരിച്ചും 
അനുവദിക്കപ്പെടുന്നതുമാണ്.
ഈ പ്രോജക്ടിന്റെ മാറ്റം ചെയ്യപ്പെട്ട പതിപ്പുകളിൽ Microsoft ട്രേഡ്മാർക്കുകളും ലോഗോകളും ഉപയോഗിക്കുന്നത് Microsoft ന്റെ പിന്തുണ അല്ലെങ്കിൽ ആശയം സൃഷ്ടിക്കരുത്.
മൂന്നാം പക്ഷം ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകളുടെ ഉപയോഗം ആ മൂന്നാം പക്ഷത്തിന്റെ നയങ്ങൾ ബാധകമാണ്.

## സഹായം നേടുക


AI ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുമ്പോൾ പ്രശ്നങ്ങൾ ഉണ്ടാകുകയോ ചോദ്യംകളുണ്ടാകുകയോ ചെയ്താൽ, ചേർമാനായിരിക്കുക:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ഉൽപ്പന്ന പ്രതികരണങ്ങൾക്കോ നിർമാണത്തിൽ പാളിപ്പറ്റലുകൾക്കോ സന്ദർശിക്കുക:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->