# AI ഏജന്റുകൾ ആരംഭക്കാർക്ക് - ഒരു കോഴ്സ്

![ജനറേറ്റീവ് AI ആരംഭക്കാർക്കായി](../../translated_images/ml/repo-thumbnailv2.06f4a48036fde647.webp)

## AI ഏജന്റുകൾ നിർമ്മിക്കാൻ തുടങ്ങാൻ നിങ്ങൾക്ക് അറിയേണ്ടതെല്ലാം പഠിപ്പിക്കുന്ന ഒരു കോഴ്സ്

[![GitHub ലൈസൻസ്](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub സംഭാവകർ](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub ഇഷ്യൂകൾ](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub പുൾ-റിക്വസ്റ്റ്‌സ്](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs സ്വാഗതം](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 ബഹുഭാഷാ പിന്തുണ

#### GitHub Action മുഖേന പിന്തുണ (ഓട്ടോമേറ്റഡ് & എപ്പോഴും അപ്-ടു-ഡേറ്റ്)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **പ്രാദേശികമായി ക്ലോൺ ചെയ്യാൻ ഇഷ്ടമാണോ?**
>
> ഈ റിപോസിറ്ററിയിൽ 50+ ഭാഷ പരിഭാഷകൾ ഉൾക്കൊള്ളുന്നു, അതിനാൽ ഡൗൺലോഡ് സൈസ് ഗണ്യമായി ഉയരുമുണ്ട്. പരിഭാഷകൾ ഇല്ലാതെ ക്ലോൺ ചെയ്യാൻ sparse checkout ഉപയോഗിക്കുക:
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
> ഇത് കോഴ്സ് പൂർത്തിയാക്കാനുള്ള എല്ലാ കാര്യങ്ങളും നൽകും, എന്നാൽ ഡൗൺലോഡ് гораздо വേഗത്തിലാകും.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**കൂടുതൽ പരിഭാഷാ ഭാഷകൾ പിന്തുണയ്ക്കണമെന്ന് ആഗ്രഹിക്കുന്നുവെങ്കിൽ ഇവ [വ്യവസ്ഥകൾ](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) എന്നിടത്ത് ലിസ്റ്റുചെയ്യപ്പെട്ടിരിക്കുന്നു**

[![GitHub വാച്ചേഴ്സ്](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub ഫോർക്ക്‌സ്](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub സ്റ്റാർസ്](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 തുടങ്ങാം

ഈ കോഴ്സിൽ AI ഏജന്റുകൾ നിർമ്മിക്കുന്നതിലെ അടിസ്ഥാനങ്ങൾ ഉൾപ്പെടുന്ന പാഠങ്ങൾ ഉണ്ട്. ഓരോ പാഠവും തന്റേതായ വിഷയം ഉൾക്കൊള്ളുന്നവയാണ്, അതിനാൽ നിങ്ങൾക്ക് ഇഷ്ടമുള്ളതു തുടങ്ങി തുടങ്ങാം!

ഈ കോഴ്സിന് ബഹുഭാഷാ പിന്തുണ ഉണ്ട്. ലഭ്യമായ ഭാഷകൾക്കായി ഞങ്ങളുടെ [ഇവിടെ ലഭ്യമായ ഭാഷകൾ](../..) സെക്ഷൻ കാണുക. 

Generative AI മോഡലുകളുമായി ആദ്യമായി നിർമ്മിക്കുന്നത് ആണെങ്കിൽ, 21 പാഠങ്ങൾ അടങ്ങിയ ഞങ്ങളുടെ [Generative AI For Beginners](https://aka.ms/genai-beginners) കോഴ്സ് പരിശോധിക്കുക.

ഈ റിപൊസിറ്ററിയെ [സ്റ്റാർ (🌟) ചെയ്യാനും](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) കോഡ് চালിക്കാൻ നിങ്ങളുടെ copy ഉണ്ടാക്കാൻ [ഈ റിപോ ഫോർക് ചെയ്യാൻ](https://github.com/microsoft/ai-agents-for-beginners/fork) മറക്കേണ്ടല്ലേ.

### മറ്റ് പഠിതാക്കളെ കാണാൻ, നിങ്ങളുടെ ചോദ്യങ്ങൾക്കുള്ള മറുപടി നേടുക

എഐ ഏജൻറുകൾ നിർമ്മിക്കുമ്പോൾ നിങ്ങള്‍ കുടുങ്ങിയാൽ അല്ലെങ്കിൽ ഏതെങ്കിലും ചോദ്യങ്ങൾ ഉണ്ടെങ്കിൽ, ഞങ്ങളുടെ സമർപ്പിത Discord ചാനലിൽ ചേരുക: [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord).

### നിങ്ങൾക്ക് വേറെ എന്തെല്ലാം വേണം

ഈ കോഴ്സിലെ ഓരോ പാഠത്തിലും code_samples ഫോൾഡറിൽ ലഭ്യമായ കോഡ് ഉദാഹരണങ്ങൾ ഉണ്ട്. നിങ്ങളുടെ സ്വന്തം കോപ്പി സൃഷ്ടിക്കാൻ നിങ്ങൾക്ക് [ഈ റിപോ ഫോർക് ചെയ്യാം](https://github.com/microsoft/ai-agents-for-beginners/fork).  

ഈ പരിശീലനപരിപാടിയിലെ കോഡ് ഉദാഹരണങ്ങൾ Microsoft Agent Framework നെ Azure AI Foundry Agent Service V2 ഉപയോഗിച്ച് പ്രയോജനം ചെയ്യുന്നു:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure അക്കൗണ്ട് ആവശ്യമാണ്

ഈ കോഴ്സ് മൈക്രോസോഫ്റ്റിന്റെ താഴെയുള്ള AI ഏജന്റ് ഫ്രെയിംവർക്ക്‌സ് மற்றும் സേവനങ്ങൾ ഉപയോഗിക്കുന്നു:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)


ഈ കോഴ്സിന്റെ കോഡ് റൺ ചെയ്യുന്നതിനുള്ള കൂടുതൽ വിവരങ്ങൾക്ക്, [Course Setup](./00-course-setup/README.md) കാണുക.

## 🙏 സഹായിക്കണമെന്നുണ്ടോ?

എന്തെങ്കിലും നിര്‍ദ്ദേശങ്ങളുണ്ടോ അല്ലെങ്കിൽ ഷെല്ലിംഗിൽ അല്ലെങ്കിൽ കോഡിൽ പിഴവുകൾ കണ്ടെത്തിയോ? [ഒരു Issue ഉയർത്തുക](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) അല്ലെങ്കിൽ [ഒരു Pull Request സൃഷ്ടിക്കുക](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ഓരോ പാഠവുമായി ഉണ്ടാകുന്നത്

- README-യിൽ നിലകൊള്ളുന്ന എഴുത്ത് പാഠവും ഒരു ചെറിയ വീഡിയോയുമുണ്ട്
- Microsoft Agent Framework ഉപയോഗിക്കുന്ന Python കോഡ് ഉദാഹരണങ്ങൾ Azure AI Foundry-യുമായി
- നിങ്ങളുടെ പഠനം തുടരാൻ അധിക വിഭവങ്ങളിലേക്കുള്ള ലിങ്കുകൾ


## 🗃️ പാഠങ്ങൾ

| **പാഠം**                                    | **വാചകവും കോഡും**                                 | **വീഡിയോ**                                               | **കൂടുതൽ പഠനം**                                                                      |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI ഏജന്റുകൾക്കും ഏജന്റ് ഉപയോഗ കേസുകൾക്കും പരിചയം       | [Link](./01-intro-to-ai-agents/README.md)          | [Video](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ഏജന്റിക് ഫ്രെയിംവർക്കുകൾ അന്വേഷിക്കൽ              | [Link](./02-explore-agentic-frameworks/README.md)  | [Video](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ഏജന്റിക് ഡിസൈൻ മാതൃകകൾ മനസ്സിലാക്കൽ     | [Link](./03-agentic-design-patterns/README.md)     | [Video](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ടൂൾ ഉപയോഗിക്കുന്ന ഡിസൈൻ മാതൃക                      | [Link](./04-tool-use/README.md)                    | [Video](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ഏജന്റിക് RAG                                  | [Link](./05-agentic-rag/README.md)                 | [Video](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| വിശ്വാസയോഗ്യമായ AI ഏജന്റുകൾ നിർമ്മിക്കൽ               | [Link](./06-building-trustworthy-agents/README.md) | [Video](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| പദ്ധതി രൂപകൽപ്പന ഡിസൈൻ മാതൃക                      | [Link](./07-planning-design/README.md)             | [Video](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| മൾട്ടി-ഏജന്റ് ഡിസൈൻ മാതൃക                   | [Link](./08-multi-agent/README.md)                 | [Video](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| മെറ്റക്കോഗ്നിഷൻ ഡിസൈൻ മാതൃക                 | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| പ്രൊഡക്ഷനിലുള്ള AI ഏജന്റുകൾ                      | [ലിങ്ക്](./10-ai-agents-production/README.md)        | [വീഡിയോ](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| എജന്റിക് പ്രോട്ടോകോളുകൾ ഉപയോഗിക്കുന്നത് (MCP, A2A and NLWeb) | [ലിങ്ക്](./11-agentic-protocols/README.md)           | [വീഡിയോ](https://youtu.be/X-Dh9R3Opn8)                                 | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ഏജന്റുകൾക്കുള്ള കോൺടെക്‌സ്‌റ്റ് എഞ്ചിനീയറിംഗ്            | [ലിങ്ക്](./12-context-engineering/README.md)         | [വീഡിയോ](https://youtu.be/F5zqRV7gEag)                                 | [ലിങ്ക്](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| എജന്റിക് മെമ്മറി മാനേജ് ചെയ്യൽ                      | [ലിങ്ക്](./13-agent-memory/README.md)     |      [വീഡിയോ](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft Agent Framework അന്വേഷിക്കൽ                         | [ലിങ്ക്](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| കമ്പ്യൂട്ടർ ഉപയോഗ ഏജന്റുകൾ (CUA)           | ഉടൻ വരുന്നു                            |                                                            |                                                                                        |
| സ്കேലബിൾ ഏജന്റുകൾ വിന്യസിക്കൽ                    | ഉടൻ വരുന്നു                            |                                                            |                                                                                        |
| പ്രാദേശിക AI ഏജന്റുകൾ സൃഷ്ടിക്കൽ                     | ഉടൻ വരുന്നു                               |                                                            |                                                                                        |
| AI ഏജന്റുകളെ സുരക്ഷിപ്പിക്കല്‍                           | ഉടൻ വരുന്നു                               |                                                            |                                                                                        |

## 🎒 മറ്റ് കോഴ്സുകൾ

ഞങ്ങളുടെ ടീം മറ്റ് കോഴ്സുകളും നിർമ്മിക്കുന്നു! ഇവ നോക്കുക:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j ആരംഭക്കാർക്കായി](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js ആരംഭക്കാർക്കായി](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain ആരംഭക്കാർക്കായി](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / ഏജന്റുകൾ
[![AZD ആരംഭക്കാർക്കായി](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI ആരംഭക്കാർക്കായി](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP ആരംഭക്കാർക്കായി](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ഏജന്റുകൾ ആരംഭക്കാർക്കായി](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ജനറേറ്റീവ് AI പരമ്പര
[![ജനറേറ്റീവ് AI ആരംഭക്കാർക്കായി](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ജനറേറ്റീവ് AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![ജനറേറ്റീവ് AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![ജനറേറ്റീവ് AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### കോർ ലേണിംഗ്
[![ML ആരംഭക്കാർക്കായി](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![ഡാറ്റാ സയൻസ് ആരംഭക്കാർക്കായി](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ആരംഭക്കാർക്കായി](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![സൈബർസെക്യൂരിറ്റി ആരംഭക്കാർക്കായി](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![വെബ് ഡെവ് ആരംഭക്കാർക്കായി](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT ആരംഭക്കാർക്കായി](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR ഡെവലപ്‌മെന്റ് ആരംഭക്കാർക്കായി](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot പരമ്പര
[![AI Paired Programming-നുള്ള Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET-നുള്ള Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot സാഹസിക യാത്ര](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 സമൂഹത്തിന് നന്ദി

Agentic RAG പ്രദർശിപ്പിക്കുന്ന പ്രധാന കോഡ് സാമ്പിളുകൾ സംഭാവന നൽകിയതിന് [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) നെ നന്ദി. 

## സംഭാവന

ഈ പ്രോജക്‌ട് സംഭാവനകളും നിർദ്ദേശങ്ങളും സ്വാഗതം ചെയ്യുന്നു. പല സംഭാവനകളും നിങ്ങൾക്കു Contributor License Agreement (CLA) നോട് එකമാകണമെന്ന് ആവശ്യപ്പെടും, നിങ്ങളുടെ സംഭാവന ഉപയോഗിക്കാൻ നിങ്ങള്‍ക്കുള്ള അവകാശങ്ങൾ നിങ്ങൾക്കുണ്ടെന്ന് പ്രസ്താവിക്കുന്ന ഒരു കരാർ. വിശദാംശങ്ങൾക്കായി കാണുക <https://cla.opensource.microsoft.com>.

നിങ്ങൾ ഒരു പുൾ റിക്വസ്റ്റ് സമർപ്പിക്കുമ്പോൾ, CLA ബോട്ട് സ്വയം നിർണ്ണയിക്കും നിങ്ങൾക്ക് CLA നൽകേണ്ടതുണ്ടോ എന്ന്, പിന്നീട് PR അനുയോജ്യമായി അലങ്കരിക്കും (ഉദാഹരണത്തിന്, സ്റ്റാറ്റസ് ചെക്ക്, കമന്റ്). ബോട്ടിന്റെ നിർദ്ദേശങ്ങൾ അനുസരിക്കുക. ഇതു നിങ്ങൾ എല്ലാവിധ repos-ലിലും ഒരിക്കൽ മാത്രം ചെയ്യേണ്ടിവരും.

ഈ പ്രോജക്‌ട് [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) സ്വീകരിച്ചിട്ടുണ്ട്.
കൂടുതൽ വിവരങ്ങൾക്ക് [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) കാണുക അല്ലെങ്കിൽ അധിക ചോദ്യങ്ങൾക്കും അഭിപ്രായങ്ങൾക്കും [opencode@microsoft.com](mailto:opencode@microsoft.com) ബന്ധപ്പെടുക.

## ട്രേഡ്മാർക്കുകൾ

ഈ പ്രോജക്ടിൽ പ്രോജക്ടുകൾ, ഉൽപ്പന്നങ്ങൾ, സേവനങ്ങൾക്ക് ബന്ധപ്പെട്ട ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ അടങ്ങിയിരിക്കാം. Microsoft ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകളുടെ അംഗീകൃത ഉപയോഗം [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) അണുബന്ധിച്ച് പാലിക്കണം.
ഈ പ്രോജക്റ്റിന്റെ മാറ്റിയ പതിപ്പുകളിൽ Microsoft ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉപയോഗിക്കുന്നത് Confusion ഉണ്ടാക്കാതിരിക്കണം അല്ലെങ്കിൽ Microsoft ന്റെ സ്പോൺസർഷിപ്പ് സൂചിപ്പിക്കരുത്.
മൂന്നു-पാർട്ടി ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകളുടെ_any_ ഉപയോഗം ആ ട്രഡ്മാർക്കുകളുടേത് നയങ്ങൾക്കനുസരിച്ചാവും.

## 도움 നേടുക


AI ആപ്ലിക്കേഷനുകൾ നിർമിക്കുമ്പോൾ തടസ്സമുണ്ടായെങ്കിൽ അല്ലെങ്കിൽ ഏതെങ്കിലും ചോദ്യം ഉണ്ടെങ്കിൽ ചേരുക:

[![Microsoft Foundry ഡിസ്കോർഡ്](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

നിർമാണത്തിനിടെ ഉൽപ്പന്ന പ്രതികരണം അല്ലെങ്കിൽ പിശകുകൾ ഉണ്ടെങ്കിൽ സന്ദർശിക്കുക:

[![Microsoft Foundry ഡെവലപ്പർ ഫോറം](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അസ്വീകരണം:
ഈ ഡൊക്ക്യുമെന്റ് AI വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നെങ്കിലും, യന്ത്രബാധിതമായ വിവർത്തനങ്ങളിൽ പിഴവുകളും അസാധുതകളും ഉണ്ടാകാമെന്നതെക്കുറിച്ച് ദയവായി ശ്രദ്ധിക്കുക. മൂലഭാഷയിലുണ്ടായിരുന്ന അസൽ രേഖയെയാണ് ഔദ്യോഗികവും വിശ്വസനീയവുമായ സ്രോതസ്സായി പരിഗണിക്കുക. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യവിവർത്തനം ശിപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽനിന്ന് ഉളവാകുന്ന quaisquer തെറ്റിദ്ധാരണകൾക്കും അപവ്യാഖ്യാനങ്ങൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->