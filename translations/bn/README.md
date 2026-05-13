# AI এজেন্টদের জন্য শুরুর পর্যায় - একটি কোর্স

![AI Agents for Beginners](../../translated_images/bn/repo-thumbnailv2.06f4a48036fde647.webp)

## AI এজেন্ট তৈরি শুরু করার জন্য যা কিছু জানা প্রয়োজন সবকিছু শেখানো একটি কোর্স

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 বহু-ভাষার সমর্থন

#### GitHub Action দ্বারা সমর্থিত (স্বয়ংক্রিয় এবং সর্বদা সর্বশেষ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](./README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **স্থানীয়ভাবে ক্লোন করতে চান?**
>
> এই রেপোজিটরিতে ৫০+ ভাষার অনুবাদ রয়েছে যা ডাউনলোড সাইজ অনেক বৃদ্ধি করে। অনুবাদ ছাড়া ক্লোন করতে sparse checkout ব্যবহার করুন:
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
> এই ভাবে আপনি কোর্স শেষ করার জন্য প্রয়োজনীয় সবকিছু অনেক দ্রুত ডাউনলোড করতে পারেন।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**আপনি যদি অতিরিক্ত অনুবাদের ভাষা চান, সেগুলি [এখানে](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) তালিকাভুক্ত আছে**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 শুরু করা

এই কোর্সটি AI এজেন্ট তৈরির মৌলিক বিষয়গুলি নিয়ে পাঠ দেয়। প্রতিটি পাঠ নিজস্ব বিষয় কভার করে, তাই আপনি যেখানে ইচ্ছা শুরু করতে পারেন!

এই কোর্সের জন্য বহু-ভাষার সমর্থন আছে। আমাদের [এখানে উপলব্ধ ভাষাগুলো দেখুন](#-multi-language-support)।

আপনি যদি প্রথমবার জেনারেটিভ AI মডেল ব্যবহার করে তৈরি করছেন, তাহলে আমাদের [শুরুয়ার্তাদের জন্য জেনারেটিভ AI](https://aka.ms/genai-beginners) কোর্স দেখুন, যেখানে জেনএআই দিয়ে তৈরি করার ২১টি পাঠ অন্তর্ভুক্ত।

এই রিপোজিটরিটিতে [স্টার (🌟) দিন](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) এবং [ফর্ক করুন](https://github.com/microsoft/ai-agents-for-beginners/fork) কোড চালানোর জন্য।

### অন্যান্য শিক্ষার্থীদের সাথে মিলুন, আপনার প্রশ্নের উত্তর পান

যদি আপনি আটকে যান বা AI এজেন্ট তৈরির বিষয়ে কোনো প্রশ্ন থাকে, তাহলে আমাদের নিবদ্ধ Discord চ্যানেল Microsoft Foundry Discord এ [যোগ দিন](https://aka.ms/ai-agents/discord)।

### আপনার যা দরকার

এই কোর্সের প্রতিটি পাঠে কোড উদাহরণ রয়েছে, যা code_samples ফোল্ডারে পাওয়া যাবে। আপনি [এই রিপোটি ফর্ক করতে পারেন](https://github.com/microsoft/ai-agents-for-beginners/fork) আপনার নিজের কপি তৈরি করার জন্য।  

এই অনুশীলনগুলোর কোড উদাহরণগুলো Microsoft Agent Framework এবং Azure AI Foundry Agent Service V2 ব্যবহার করে:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure একাউন্ট প্রয়োজন

এই কোর্সে Microsoft থেকে নিচের AI এজেন্ট ফ্রেমওয়ার্ক ও সেবাগুলো ব্যবহৃত হয়েছে:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

কিছু কোড নমুনায় বিকল্প OpenAI-সঙ্গত প্রোভাইডার যেমন [MiniMax](https://platform.minimaxi.com/) সাপোর্ট করে, যা বড় কনটেক্সট মডেল (প্রায় ২০৪কে টোকেন পর্যন্ত) প্রদান করে। বিস্তারিত কনফিগারেশনের জন্য [কোর্স সেটআপ](./00-course-setup/README.md) দেখুন।

এই কোর্সের কোড চালানোর বিষয়ে আরো তথ্যের জন্য, [কোর্স সেটআপ](./00-course-setup/README.md) দেখুন।

## 🙏 সাহায্য করতে চান?

আপনার কোন পরামর্শ আছে বা বানান বা কোড ত্রুটি পেয়েছেন? [একটি ইস্যু উত্থাপন করুন](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) অথবা [পুল রিকুয়েস্ট তৈরি করুন](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 প্রতিটি পাঠে অন্তর্ভুক্ত

- একটি লিখিত পাঠ README তে এবং একটি সংক্ষিপ্ত ভিডিও
- Microsoft Agent Framework ও Azure AI Foundry ব্যবহার করে Python কোড নমুনাগুলো
- আপনার শিক্ষাকে চালিয়ে নিতে অতিরিক্ত সম্পদের লিঙ্ক


## 🗃️ পাঠসমূহ

| **পাঠ**                                     | **টেক্সট ও কোড**                                   | **ভিডিও**                                                  | **অতিরিক্ত শেখা**                                                                     |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| AI এজেন্ট এবং এজেন্ট ব্যবহারের পরিচিতি      | [লিঙ্ক](./01-intro-to-ai-agents/README.md)          | [ভিডিও](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI এজেন্টিক ফ্রেমওয়ার্ক অনুসন্ধান             | [লিঙ্ক](./02-explore-agentic-frameworks/README.md)  | [ভিডিও](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI এজেন্টিক ডিজাইন প্যাটার্ন বোঝা             | [লিঙ্ক](./03-agentic-design-patterns/README.md)     | [ভিডিও](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| টুল ব্যবহার ডিজাইন প্যাটার্ন                    | [লিঙ্ক](./04-tool-use/README.md)                    | [ভিডিও](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| এজেন্টিক RAG                               | [লিঙ্ক](./05-agentic-rag/README.md)                 | [ভিডিও](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| বিশ্বাসযোগ্য AI এজেন্ট তৈরি                    | [লিঙ্ক](./06-building-trustworthy-agents/README.md) | [ভিডিও](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| পরিকল্পনা ডিজাইন প্যাটার্ন                      | [লিঙ্ক](./07-planning-design/README.md)             | [ভিডিও](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| বহু-এজেন্ট ডিজাইন প্যাটার্ন                    | [লিঙ্ক](./08-multi-agent/README.md)                 | [ভিডিও](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [লিঙ্ক](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| মেটাকগনিশন ডিজাইন প্যাটার্ন                 | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| উৎপাদনে AI এজেন্টস                      | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| এজেন্টিক প্রোটোকল ব্যবহার (MCP, A2A এবং NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI এজেন্টসের জন্য প্রেক্ষাপট ইঞ্জিনিয়ারিং            | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| এজেন্টিক মেমোরি পরিচালনা                      | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Microsoft এজেন্ট ফ্রেমওয়ার্ক অনুসন্ধান                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| কম্পিউটার ইউজ এজেন্ট নির্মাণ (CUA)           | [Link](./15-browser-use/README.md)     |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| স্কেলযোগ্য এজেন্টস মোতায়েন                    | শীঘ্রই আসছে                            |                                                            |                                                                                        |
| স্থানীয় AI এজেন্ট তৈরি                     | শীঘ্রই আসছে                               |                                                            |                                                                                        |
| AI এজেন্টদের সুরক্ষিত করা                           | [Link](./18-securing-ai-agents/README.md)  |                                                            | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 অন্যান্য কোর্স

আমাদের টিম অন্যান্য কোর্স তৈরি করে! দেখুন:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![শিক্ষার্থীদের জন্য LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![শিক্ষার্থীদের জন্য LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![শিক্ষার্থীদের জন্য LangChain](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / এজেন্টস
[![শিক্ষার্থীদের জন্য AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![শিক্ষার্থীদের জন্য Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![শিক্ষার্থীদের জন্য MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![শিক্ষার্থীদের জন্য AI এজেন্টস](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### জেনারেটিভ AI সিরিজ
[![শিক্ষার্থীদের জন্য জেনারেটিভ AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![জেনারেটিভ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![জেনারেটিভ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![জেনারেটিভ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### কোর লার্নিং
[![শিক্ষার্থীদের জন্য ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![শিক্ষার্থীদের জন্য ডেটা সায়েন্স](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![শিক্ষার্থীদের জন্য AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![শিক্ষার্থীদের জন্য সাইবারসিকিউরিটি](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![শিক্ষার্থীদের জন্য ওয়েব ডেভেলপমেন্ট](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![শিক্ষার্থীদের জন্য IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![শিক্ষার্থীদের জন্য XR ডেভেলপমেন্ট](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### কপাইলট সিরিজ
[![AI পেয়ারড প্রোগ্রামিংয়ের জন্য কপাইলট](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET এর জন্য কপাইলট](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![কপাইলট অ্যাডভেঞ্চার](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 কমিউনিটি ধন্যবাদ

Agentic RAG প্রদর্শনকারী গুরুত্বপূর্ণ কোড স্যাম্পল অবদানের জন্য [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) কে ধন্যবাদ।

## অবদান রাখা

এই প্রকল্প অবদান এবং পরামর্শের জন্য স্বাগত জানায়। বেশিরভাগ অবদানের জন্য আপনাকে একটি
Contributor License Agreement (CLA)-এ সম্মত হতে হবে যা ঘোষণা করে যে আপনার অধিকার রয়েছে এবং প্রকৃতপক্ষে আমাদেরকে
আপনার অবদান ব্যবহারের জন্য অধিকার প্রদান করছেন। বিস্তারিত জানতে <https://cla.opensource.microsoft.com> এ দেখুন।

যখন আপনি একটি পুল রিকুয়েস্ট জমা দেন, একটি CLA বট স্বয়ংক্রিয়ভাবে নির্ধারণ করবে যে আপনি CLA প্রদান করবেন কিনা এবং সহযোগিতা অনুযায়ী পুল রিকুয়েস্টকে (যেমন, স্ট্যাটাস চেক, মন্তব্য) সাজাবে। বটের নির্দেশনা অনুসরণ করুন। আমাদের CLA ব্যবহার করা সমস্ত রিপোজে আপনাকে একবারই এটি করতে হবে।

এই প্রকল্প [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) গ্রহণ করেছে।
আরও তথ্যের জন্য দেখুন [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) অথবা
অতিরিক্ত প্রশ্ন বা মতামতের জন্য [opencode@microsoft.com](mailto:opencode@microsoft.com) যোগাযোগ করুন।

## ট্রেডমার্ক

এই প্রকল্পে প্রকল্প, পণ্য বা সেবার ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft
ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে।
এই প্রকল্পের সংশোধিত সংস্করণে Microsoft ট্রেডমার্ক বা লোগোর ব্যবহার বিভ্রান্তি সৃষ্টি বা Microsoft স্পনসরশিপ নির্দেশ করা থেকে বিরত থাকতে হবে।
তৃতীয় পক্ষের ট্রেডমার্ক বা লোগোর ব্যবহার ঐ তৃতীয় পক্ষের নীতিমালা অনুসারে হতে হবে।

## সাহায্য পাওয়া যায়

যদি আপনি আটকে যান বা AI অ্যাপ তৈরি নিয়ে প্রশ্ন থাকে, যোগ দিন:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

পণ্যের প্রতিক্রিয়া বা নির্মাণকালীন ত্রুটি থাকলে যান:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->