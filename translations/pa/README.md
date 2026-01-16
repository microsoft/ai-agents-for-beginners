<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0f72060e745b81a3705ec8b208cb7de2",
  "translation_date": "2026-01-16T08:06:31+00:00",
  "source_file": "README.md",
  "language_code": "pa"
}
-->
# ਸ਼ੁਰੂਆਤੀ ਲਈ AI ਏਜੰਟ - ਇੱਕ ਕੋਰਸ

![ਸ਼ੁਰੂਆਤੀ ਲਈ ਜਨਰੇਟਿਵ AI](../../../../translated_images/pa/repo-thumbnailv2.06f4a48036fde647.webp)

## AI ਏਜੰਟ ਬਣਾਉਣਾ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਤੁਹਾਨੂੰ ਜੋ ਕੁਝ ਵੀ ਜਾਣਨਾ ਹੈ ਉਸ ਦਾ ਸਬਕ

[![GitHub ਲਾਇਸੈਂਸ](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub ਯੋਗਦਾਨਕਾਰ](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub ਮੁੱਦੇ](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub ਪੁੱਲ-ਰਿਕਵੇਸਟਾਂ](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs ਸਵਾਗਤ ਹੈ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 ਬਹੁਭਾਸ਼ੀ ਸਮਰਥਨ

#### GitHub ਐਕਸ਼ਨ ਰਾਹੀਂ ਸਮਰਥਿਤ (ਆਟੋਮੇਟਡ ਅਤੇ ਹਮੇਸ਼ਾਂ ਅੱਪ-ਟੂ-ਡੇਟ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ਕੀ ਤੁਸੀਂ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਕਲੋਨ ਕਰਨਾ ਪਸੰਦ ਕਰਦੇ ਹੋ?**

> ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ 50+ ਭਾਸ਼ਾ ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਹਨ ਜੋ ਡਾਊਨਲੋਡ ਸਾਈਜ਼ ਨੂੰ ਕਾਫੀ ਵਧਾ ਦਿੰਦੇ ਹਨ। ਬਿਨਾਂ ਅਨੁਵਾਦਾਂ ਦੇ ਕਲੋਨ ਕਰਨ ਲਈ, ਸਪਾਰਸ ਚੈਕਆਉਟ ਨੂੰ ਵਰਤੋ:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ਇਹ ਤੁਹਾਨੂੰ ਸਬ ਕੁਝ ਦਿੰਦਾ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਕੋਰਸ ਪੂਰਾ ਕਰਨ ਲਈ ਚਾਹੀਦਾ ਹੈ ਬਹੁਤ ਤੇਜ਼ ਡਾਊਨਲੋਡ ਦੇ ਨਾਲ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**ਜੇ ਤੁਹਾਨੂੰ ਵਧੇਰੇ ਅਨੁਵਾਦ ਭਾਸ਼ਾਵਾਂ ਦੀ ਚਾਹਤ ਹੈ ਤਾਂ ਉਨ੍ਹਾਂ ਦੀ ਸੂਚੀ ਇੱਥੇ ਦਿੱਤੀ ਹੈ [ਹੇਠਾਂ](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub ਵਾਚਰਜ਼](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub ਫੋਰਕ](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub ਸਟਾਰਜ਼](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 ਸ਼ੁਰੂਆਤ ਕਰਨਾ

ਇਸ ਕੋਰਸ ਵਿੱਚ AI ਏਜੰਟ ਬਣਾਉਣ ਦੇ ਮੂਲ ਭਾਗਾਂ ਨੂੰ ਸਿੱਖਾਇਆ ਗਿਆ ਹੈ। ਹਰ ਪਾਠ ਆਪਣਾ ਵਿਸ਼ਾ ਕਵਰ ਕਰਦਾ ਹੈ, ਇਸ ਲਈ ਜੋ ਮਜ਼ੇਦਾਰ ਲੱਗੇ ਉੱਥੋਂ ਸ਼ੁਰੂ ਕਰੋ!

ਇਸ ਕੋਰਸ ਲਈ ਬਹੁਭਾਸ਼ੀ ਸਮਰਥਨ ਉਪਲਬਧ ਹੈ। ਸਾਡੇ [ਉਪਲਬਧ ਭਾਸ਼ਾਵਾਂ ਇੱਥੇ](../..) ਚੈੱਕ ਕਰੋ।

ਜੇ ਤੁਸੀਂ ਪਹਿਲੀ ਵਾਰ ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਨਾਲ ਕੰਮ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਸਾਡਾ [ਜਨਰੇਟਿਵ AI ਫ਼ਾਰ ਬਿਗਿਨਰਜ਼](https://aka.ms/genai-beginners) ਕੋਰਸ ਵੇਖੋ, ਜਿਸ ਵਿੱਚ ਜਨ-ਏਆਈ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ 21 ਪਾਠ ਹਨ।

ਇਸ ਰਿਪੋ ਨੂੰ [ਸਟਾਰ (🌟) ਕਰਨਾ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ਨਾ ਭੁੱਲੋ ਅਤੇ ਕੋਡ ਚਲਾਉਣ ਲਈ ਇਸਨੂੰ [Fork ਕਰੋ](https://github.com/microsoft/ai-agents-for-beginners/fork)।

### ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲੋ, ਆਪਣੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲਵੋ

ਜੇ ਤੁਸੀਂ ਅਟਕ ਜਾਂਦੇ ਹੋ ਜਾਂ AI ਏਜੰਟ ਬਣਾਉਣ ਬਾਰੇ ਕੋਈ ਸਵਾਲ ਹੈ, ਤਾਂ ਸਾਡੇ ਨਿਰਧਾਰਿਤ ਡਿਸਕੋਰਡ ਚੈਨਲ ਵਿੱਚ ਜੁੜੋ [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ਵਿੱਚ।

### ਤੁਹਾਨੂੰ ਕੀ ਚਾਹੀਦਾ ਹੈ

ਇਸ ਕੋਰਸ ਦੇ ਹਰ ਪਾਠ ਵਿੱਚ ਕੋਡ ਦੇ ਉਦਾਹਰਨ ਸ਼ਾਮਲ ਹਨ, ਜੋ code_samples ਫੋਲਡਰ ਵਿੱਚ ਮਿਲਦੇ ਹਨ। ਤੁਸੀਂ ਆਪਣੀ ਨਕਲ ਬਣਾਉਣ ਲਈ ਇਸਨੂੰ [Fork](https://github.com/microsoft/ai-agents-for-beginners/fork) ਕਰ ਸਕਦੇ ਹੋ।  

ਇਹਨਾਂ ਅਭਿਆਸਾਂ ਵਿੱਚ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ Azure AI Foundry ਅਤੇ GitHub ਮਾਡਲ ਕੈਟਾਲੋਗਸ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਨਾਲ ਇੰਟਰਐਕਸ਼ਨ ਲਈ:

- [Github ਮਾਡਲ](https://aka.ms/ai-agents-beginners/github-models) - ਮੁਫਤ / ਸੀਮਤ
- [Azure AI Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure ਖਾਤਾ ਲੋੜੀਂਦਾ

ਇਹ ਕੋਰਸ Microsoft ਤੋਂ ਇਹਨਾਂ AI ਏਜੰਟ ਢਾਂਚਿਆਂ ਅਤੇ ਸੇਵਾਵਾਂ ਦੀ ਵੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ:

- [Microsoft ਏਜੰਟ ਫਰੇਮਵਰਕ (MAF) - ਨਵਾਂ!](https://aka.ms/ai-agents-beginners/agent-framewrok)
- [Azure AI ਏਜੰਟ ਸੇਵਾ](https://aka.ms/ai-agents-beginners/ai-agent-service)
- [ਸੈਮੈਂਟਿਕ ਕਰਨਲ](https://aka.ms/ai-agents-beginners/semantic-kernel)
- [AutoGen](https://aka.ms/ai-agents/autogen)


ਇਸ ਕੋਰਸ ਲਈ ਕੋਡ ਚਲਾਉਣ ਬਾਰੇ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਲਈ ਜਾਓ [ਕੋਰਸ ਸੈਟਅਪ](./00-course-setup/README.md)।

## 🙏 ਮਦਦ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?

ਕੀ ਤੁਹਾਡੇ ਕੋਲ ਸੁਝਾਅ ਹਨ ਜਾਂ ਤੁਸੀਂ ਵਿਆਕਰਨ ਜਾਂ ਕੋਡ ਦੀਆਂ ਗਲਤੀਆਂ ਲੱਭੀਆਂ ਹਨ? [ਇਸ਼ੂ ਉਠਾਓ](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ਜਾਂ [ਪੁੱਲ ਰਿਕਵੇਸਟ ਬਣਾਓ](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 ਹਰ ਪਾਠ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ

- README ਵਿੱਚ ਲਿਖਿਆ ਹੋਇਆ ਪਾਠ ਅਤੇ ਇੱਕ ਛੋਟੀ ਵੀਡੀਓ
- Azure AI Foundry ਅਤੇ Github ਮਾਡਲਾਂ (ਮੁਫਤ) ਲਈ ਸਹਾਇਕ Python ਕੋਡ ਸੈਂਪਲ
- ਤੁਹਾਡੇ ਸਿੱਖਣ ਨੂੰ ਜਾਰੀ ਰੱਖਣ ਲਈ ਵਾਧੂ ਸਰੋਤਾਂ ਦੇ ਲਿੰਕ


## 🗃️ ਪਾਠ

| **ਪਾਠ**                                        | **ਲਿਖਤ ਅਤੇ ਕੋਡ**                                  | **ਵੀਡੀਓ**                                                   | **ਵਾਧੂ ਸਿੱਖਿਆ**                                                                       |
|----------------------------------------------|-------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI ਏਜੰਟ ਅਤੇ ਏਜੰਟ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਦਾ ਜਾਣ-ਪਹਚਾਣ  | [ਲਿੰਕ](./01-intro-to-ai-agents/README.md)          | [ਵੀਡੀਓ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [ਲਿੰਕ](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ਏਜੰਟਿਕ ਫਰੇਮਵਰਕਾਂ ਦੀ ਖੋਜ                      | [ਲਿੰਕ](./02-explore-agentic-frameworks/README.md)  | [ਵੀਡੀਓ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [ਲਿੰਕ](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ਏਜੰਟਿਕ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨਸ ਦੀ ਸਮਝ               | [ਲਿੰਕ](./03-agentic-design-patterns/README.md)     | [ਵੀਡੀਓ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [ਲਿੰਕ](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ                        | [ਲਿੰਕ](./04-tool-use/README.md)                    | [ਵੀਡੀਓ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [ਲਿੰਕ](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ਏਜੰਟਿਕ RAG                                     | [ਲਿੰਕ](./05-agentic-rag/README.md)                 | [ਵੀਡੀਓ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [ਲਿੰਕ](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ਭਰੋਸੇਮੰਦ AI ਏਜੰਟ ਬਣਾਉਣਾ                        | [ਲਿੰਕ](./06-building-trustworthy-agents/README.md) | [ਵੀਡੀਓ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [ਲਿੰਕ](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ਯੋਜਨਾ ਬਣਾਉਣ ਦਾ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ                  | [ਲਿੰਕ](./07-planning-design/README.md)             | [ਵੀਡੀਓ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [ਲਿੰਕ](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ਬਹੁ-ਏਜੰਟ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ                         | [ਲਿੰਕ](./08-multi-agent/README.md)                 | [ਵੀਡੀਓ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [ਲਿੰਕ](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
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

## 🎒 ਹੋਰ ਕੋਰਸز

ਸਾਡੀ ਟੀਮ ਹੋਰ ਕੋਰਸਜ਼ ਤਿਆਰ ਕਰਦੀ ਹੈ! ਵੇਖੋ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 ਕਮਿਊਨੀਟੀ ਧੰਨਵਾਦ

Agentic RAG ਦਿਖਾਉਂਦੇ ਅਹਿਮ ਕੋਡ ਨਮੂਨੇ ਪੇਸ਼ ਕਰਨ ਲਈ [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) ਦਾ ਧੰਨਵਾਦ।  

## ਯੋਗਦਾਨ ਪਾਉਣਾ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਯੋਗਦਾਨ ਅਤੇ ਸੁਝਾਵਾਂ ਸਵਾਗਤ ਹਨ। ਜ਼ਿਆਦਾਤਰ ਯੋਗਦਾਨਾਂ ਲਈ ਤੁਹਾਡੇ ਕੋਲ Contributor License Agreement (CLA) ਨੂੰ ਸਵੀਕਾਰ ਕਰਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਤੁਸੀਂ ਇਹ ਦੱਸਦੇ ਹੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਆਪਣੇ ਯੋਗਦਾਨ ਦੇ ਉਪਯੋਗ ਲਈ ਹੱਕ ਹਨ ਅਤੇ ਤੁਸੀਂ ਸਾਨੂੰ ਉਹ ਹੱਕ ਦੇ ਰਹੇ ਹੋ। ਵੇਰਵੇ ਲਈ, <https://cla.opensource.microsoft.com> ’ਤੇ ਜਾਓ।

ਜਦੋਂ ਤੁਸੀਂ ਇੱਕ ਪੁਲ ਰਿਕਵੇਸਟ ਸਬਮਿਟ ਕਰਦੇ ਹੋ, ਤਾਂ ਇੱਕ CLA ਬੋਟ ਸਵੈ-ਚਾਲਿਤ ਤਰੀਕੇ ਨਾਲ ਤੈਅ ਕਰੇਗਾ ਕਿ ਕੀ ਤੁਹਾਨੂੰ CLA ਪ੍ਰਦਾਨ ਕਰਨ ਦੀ ਲੋੜ ਹੈ ਅਤੇ PR ਨੂੰ ਉਚਿਤ ਤੌਰ 'ਤੇ ਸਜਾਵੇਗਾ (ਜਿਵੇਂ ਕਿ ਸਥਿਤੀ ਜਾਂ ਜਾਂਚ, ਟਿੱਪਣੀ)। ਬੋਟ ਵੱਲੋਂ ਦਿੱਤੇ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। ਸਾਡੇ CLA ਵੱਲੋਂ ਸਾਰੇ ਰੇਪੋ ਵਿੱਚ ਇਸਨੂੰ ਸਿਰਫ ਇੱਕ ਵਾਰੀ ਕਰਨਾ ਪਵੇਗਾ।

ਇਸ ਪ੍ਰੋਜੈਕਟ ਨੇ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ਨੂੰ ਅਪਨਾਇਆ ਹੈ। ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਲਈ [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ਵੇਖੋ ਜਾਂ ਵਾਧੂ ਸਵਾਲਾਂ ਜਾਂ ਟਿੱਪਣੀਆਂ ਲਈ [opencode@microsoft.com](mailto:opencode@microsoft.com) ਨਾਲ ਸੰਪਰਕ ਕਰੋ।

## ਟ੍ਰੇਡਮਾਰਕ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਪ੍ਰੋਜੈਕਟਾਂ, ਉਤਪਾਦਾਂ ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਹੋ ਸਕਦੇ ਹਨ। Microsoft ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦਾ ਪ੍ਰਧਾਨ ਕੀਤਾ ਗਿਆ ਉਪਯੋਗ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ਦੇ ਅਧੀਨ ਹੈ ਅਤੇ ਇਸਨੂੰ ਫਾਲੋ ਕਰਨਾ ਜਰੂਰੀ ਹੈ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੇ ਸੋਧੇ ਹੋਏ ਵਰਜਨ ਵਿੱਚ Microsoft ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੇ ਉਪਯੋਗ ਨਾਲ ਭੁਲ-ਭੁੱਲੈਿਆ ਜਾਂ Microsoft ਦੇ ਪ੍ਰਾਯੋਜਨ ਦਾ ਇੰਗਿਤ ਨਹੀਂ ਹੋਣਾ ਚਾਹੀਦਾ। ਕਿਸੇ ਤੀਸਰੇ-ਪੱਖ ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੇ ਉਪਯੋਗ ਨਾਲ ਸੰਬੰਧਿਤ ਨੀਤੀਆਂ ਉਸ ਤੀਸਰੇ-ਪੱਖ ਦੀਆਂ ਹੀ ਹੁੰਦੀਆਂ ਹਨ।

## ਸਹਾਇਤਾ ਲੈਣ ਲਈ

ਜੇ ਤੁਸੀਂ ਫਸ ਜਾਂਦੇ ਹੋ ਜਾਂ AI ਐਪਸ ਬਣਾਉਣ ਬਾਰੇ ਕੋਈ ਸਵਾਲ ਹੈ, ਤਾਂ ਜੁੜੋ:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ਜੇ ਤੁਸੀਂ ਉਤਪਾਦ ਬਾਰੇ ਫੀਡਬੈਕ ਜਾਂ ਗਲਤੀਆਂ ਦਾ ਸਾਹਮਣਾ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਦਰਜ ਕਰੋ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋ ਹਨੇਰਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਜਾਣੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸੂਝੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ਾਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->