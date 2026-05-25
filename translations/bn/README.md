# AI এজেন্টদের জন্য শুরু প্রবেশিকা - একটি কোর্স

![AI এজেন্টদের জন্য শুরু প্রবেশিকা](../../translated_images/bn/repo-thumbnailv2.06f4a48036fde647.webp)

## একটি কোর্স যা শেখায় শুরু করতে যা কিছু জানা দরকার AI এজেন্ট নির্মাণে

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 বহুভাষিক সমর্থন

#### GitHub Action এর মাধ্যমে সমর্থিত (স্বয়ংক্রিয় ও সর্বদা আপ-টু-ডেট)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](./README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **লোকালি ক্লোন করতে চান?**
>
> এই রেপোজিটোরিতে ৫০+ ভাষার অনুবাদ রয়েছে যা ডাউনলোড আকার অনেক বাড়িয়ে দেয়। অনুবাদ ছাড়া ক্লোন করতে sparse checkout ব্যবহার করুন:
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
> এটি আপনাকে দ্রুত ডাউনলোডের মাধ্যমে কোর্স সম্পন্ন করার জন্য প্রয়োজনীয় সবকিছু দেয়।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**অতিরিক্ত অনুবাদ ভাষা চান? এগুলি এখানে তালিকাভুক্ত করা হয়েছে [এখানে](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)।**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 শুরু করাঃ

এই কোর্সে AI এজেন্ট নির্মাণের মৌলিক বিষয়গুলি শেখানো হয়েছে। প্রতিটি পাঠের নিজস্ব বিষয় রয়েছে, তাই যেখান থেকে চান সেখানে শুরু করুন!

এই কোর্সের জন্য বহুভাষিক সমর্থন রয়েছে। আমাদের [উপলব্ধ ভাষাগুলো এখানে](#-multi-language-support) যান। 

যদি আপনি প্রথমবার জীবন্ত AI মডেল দিয়ে কাজ করছেন, তাহলে আমাদের [Generative AI For Beginners](https://aka.ms/genai-beginners) কোর্সটি দেখুন, যেখানে GenAI দিয়ে নির্মাণের ২১টি পাঠ অন্তর্ভুক্ত।

[তারকা (🌟) দিন এই রেপোতে](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) এবং [ফর্ক করুন এই রেপোটি](https://github.com/microsoft/ai-agents-for-beginners/fork) কোড রান করার জন্য।

### অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হন, আপনার প্রশ্নের উত্তর পান

যদি আটকে যান বা AI এজেন্ট নির্মাণ সংক্রান্ত কোনো প্রশ্ন থাকে, আমাদের [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) এ নিবেদিত Discord চ্যানেলে যোগ দিন।

### যা আপনার প্রয়োজন

এই কোর্সের প্রতিটি পাঠের কোড উদাহরণ রয়েছে, যা code_samples ফোল্ডারে পাওয়া যাবে। আপনি আপনার নিজের কপি তৈরির জন্য [ফর্ক করতে পারেন এই রেপোটি](https://github.com/microsoft/ai-agents-for-beginners/fork)।

এই পরীক্ষা কোড উদাহরণগুলো Microsoft Agent Framework এবং Azure AI Foundry Agent Service V2 ব্যবহার করে:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure Account প্রয়োজন

এই কোর্সটি Microsoft এর নিম্নলিখিত AI Agent ফ্রেমওয়ার্কস এবং সার্ভিস ব্যবহার করে:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

কিছু কোড স্যাম্পল বিকল্প OpenAI-সঙ্গত সেবা প্রদানকারী যেমন [MiniMax](https://platform.minimaxi.com/) সমর্থন করে, যা বড় প্রসঙ্গ মডেল (আদায় ২০৪ কে টোকেন) প্রদান করে। বিস্তারিত কনফিগারেশনের জন্য দেখুন [Course Setup](./00-course-setup/README.md)।

এই কোর্সের কোড চালানোর বিষয়ে আরও তথ্যের জন্য [Course Setup](./00-course-setup/README.md) দেখুন।

## 🙏 সাহায্য করতে চান?

আপনার পরামর্শ আছে বা বানান বা কোড ত্রুটি পেয়েছেন? [একটি issue তুলুন](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) অথবা [একটি pull request তৈরি করুন](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 প্রতিটি পাঠে রয়েছে

- README তে লিখিত পাঠ এবং একটি সংক্ষিপ্ত ভিডিও
- Microsoft Agent Framework এবং Azure AI Foundry ব্যবহার করে Python কোড উদাহরণ
- আপনার শেখা চালিয়ে যাওয়ার জন্য অতিরিক্ত রিসোর্সের লিঙ্ক


## 🗃️ পাঠসমূহ

| **পাঠ**                                    | **লিখিত ও কোডসহ**                                      | **ভিডিও**                                                   | **অতিরিক্ত শেখা**                                                                      |
|--------------------------------------------|----------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| AI এজেন্ট ও এজেন্ট ব্যবহারের পরিচিতি       | [লিঙ্ক](./01-intro-to-ai-agents/README.md)                | [ভিডিও](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)   | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)  |
| AI এজেন্টিক ফ্রেমওয়ার্ক অন্বেষণ             | [লিঙ্ক](./02-explore-agentic-frameworks/README.md)        | [ভিডিও](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)   | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)  |
| AI এজেন্টিক ডিজাইন প্যাটার্ন বোঝা            | [লিঙ্ক](./03-agentic-design-patterns/README.md)           | [ভিডিও](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)   | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)  |
| টুল ব্যবহার ডিজাইন প্যাটার্ন                  | [লিঙ্ক](./04-tool-use/README.md)                          | [ভিডিও](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)   | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)  |
| এজেন্টিক RAG                               | [লিঙ্ক](./05-agentic-rag/README.md)                        | [ভিডিও](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)   | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)  |
| বিশ্বাসযোগ্য AI এজেন্ট নির্মাণ                | [লিঙ্ক](./06-building-trustworthy-agents/README.md)       | [ভিডিও](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK )  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)  |
| পরিকল্পনা ডিজাইন প্যাটার্ন                    | [লিঙ্ক](./07-planning-design/README.md)                   | [ভিডিও](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)   | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)  |
| মাল্টি-এজেন্ট ডিজাইন প্যাটার্ন                | [লিঙ্ক](./08-multi-agent/README.md)                        | [ভিডিও](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)   | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)  |
| মেটাকগনিশন ডিজাইন প্যাটার্ন                 | [লিঙ্ক](./09-metacognition/README.md)               | [ভিডিও](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| উৎপাদনে AI এজেন্ট্স                      | [লিঙ্ক](./10-ai-agents-production/README.md)        | [ভিডিও](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| এজেন্টিক প্রোটোকল ব্যবহার (MCP, A2A এবং NLWeb) | [লিঙ্ক](./11-agentic-protocols/README.md)           | [ভিডিও](https://youtu.be/X-Dh9R3Opn8)                                 | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI এজেন্টসের জন্য প্রাসঙ্গিক ইঞ্জিনিয়ারিং            | [লিঙ্ক](./12-context-engineering/README.md)         | [ভিডিও](https://youtu.be/F5zqRV7gEag)                                 | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| এজেন্টিক মেমোরি পরিচালনা                      | [লিঙ্ক](./13-agent-memory/README.md)     |      [ভিডিও](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক অন্বেষণ                         | [লিঙ্ক](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| কম্পিউটার ইউজ এজেন্টস (CUA) তৈরি করা           | [লিঙ্ক](./15-browser-use/README.md)     |                                                            | [লিঙ্ক](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| স্কেলেবল এজেন্টস ডিপ্লয় করা                    | শীঘ্রই আসছে                            |                                                            |                                                                                        |
| লোকাল AI এজেন্টস তৈরি করা                     | শীঘ্রই আসছে                               |                                                            |                                                                                        |
| AI এজেন্টস সুরক্ষা                           | [লিঙ্ক](./18-securing-ai-agents/README.md)  |                                                            | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 অন্যান্য কোর্সসমূহ

আমাদের দল অন্যান্য কোর্স তৈরি করে! দেখুন:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### ল্যাংচেইন
[![শুরুদের জন্য LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![শুরুদের জন্য LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![শুরুদের জন্য LangChain](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### আজুড় / এজ / MCP / এজেন্টস
[![শুরুদের জন্য AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুদের জন্য এজ এআই](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুদের জন্য MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুদের জন্য AI এজেন্টস](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### জেনেরেটিভ AI সিরিজ
[![শুরুদের জন্য জেনেরেটিভ AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![জেনেরেটিভ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![জেনেরেটিভ AI (জাভা)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![জেনেরেটিভ AI (জাভাস্ক্রিপ্ট)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### ক্রিয়া শিক্ষণ
[![শুরুদের জন্য এমএল](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুদের জন্য ডেটা সায়েন্স](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুদের জন্য AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুদের জন্য সাইবারসিকিউরিটি](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![শুরুদের জন্য ওয়েব ডেভ](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুদের জন্য আইওটি](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুদের জন্য XR ডেভেলপমেন্ট](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### কোপাইলট সিরিজ
[![AI সহিত যুগল প্রোগ্রামিংয়ের জন্য কোপাইলট](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET এর জন্য কোপাইলট](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![কোপাইলট অ্যাডভেঞ্চার](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 সম্প্রদায়ের ধন্যবাদ

এজেন্টিক RAG প্রদর্শন করে গুরুত্বপূর্ণ কোড নমুনার জন্য [শিবম গোহল](https://www.linkedin.com/in/shivam2003/) কে ধন্যবাদ।

## অবদান রাখা

এই প্রকল্পে অবদান এবং পরামর্শ স্বাগত জানানো হয়। বেশিরভাগ অবদানের জন্য আপনাকে একটি
Contributor License Agreement (CLA) এ সম্মত হতে হবে যা বলে আপনি অধিকার রাখেন এবং প্রকৃতপক্ষে
আমাদের আপনার অবদানের ব্যবহার করার অধিকার প্রদান করেন। বিস্তারিত জানতে, দেখুন <https://cla.opensource.microsoft.com>।

আপনি যখন একটি পুল রিকোয়েস্ট জমা দেবেন, CLA বট স্বয়ংক্রিয়ভাবে নির্ধারণ করবে আপনি CLA প্রদান করতে হবে কিনা এবং পিআর-কে উপযুক্তভাবে চিহ্নিত করবে (যেমন স্টেটাস চেক, মন্তব্য)। বট দ্বারা প্রদত্ত নির্দেশগুলি অনুসরণ করুন। আমাদের CLA ব্যবহৃত সমস্ত রিপোজে আপনি একবার মাত্র এটি করবেন।

এই প্রকল্প [মাইক্রোসফট ওপেন সোর্স কোড অব কন্ডাক্ট](https://opensource.microsoft.com/codeofconduct/) গ্রহণ করেছে।
আরও তথ্যের জন্য দেখুন [কোড অব কন্ডাক্ট FAQ](https://opensource.microsoft.com/codeofconduct/faq/) অথবা কোনো অতিরিক্ত প্রশ্ন বা মন্তব্যের জন্য যোগাযোগ করুন [opencode@microsoft.com](mailto:opencode@microsoft.com) এ।

## ট্রেডমার্ক

এই প্রকল্পে প্রকল্প, পণ্য, বা পরিষেবাগুলোর ট্রেডমার্ক বা লোগো থাকতে পারে। মাইক্রোসফটের
ট্রেডমার্ক অথবা লোগোর অনুমোদিত ব্যবহার [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে।
পরিবর্তিত সংস্করণে মাইক্রোসফট ট্রেডমার্ক বা লোগো ব্যবহারে বিভ্রান্তি সৃষ্টি বা মাইক্রোসফট স্পনসরশিপ ইঙ্গিত দেওয়া যাবেনা।
তৃতীয় পক্ষের ট্রেডমার্ক বা লোগো ব্যবহারের ক্ষেত্রে সেই পক্ষের নীতিমালা প্রযোজ্য।

## সহায়তা পাওয়া

যদি আপনি আটকে যান বা AI অ্যাপ নির্মাণ সম্পর্কে কোনো প্রশ্ন থাকে, যোগ দিন:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

যদি পণ্য প্রতিক্রিয়া বা নির্মাণ কালে ত্রুটি হয়, যান:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->