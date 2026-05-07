# ตัวแทน AI สำหรับผู้เริ่มต้น - หลักสูตร

![AI Agents for Beginners](../../translated_images/th/repo-thumbnailv2.06f4a48036fde647.webp)

## หลักสูตรสอนทุกอย่างที่คุณต้องรู้เพื่อเริ่มสร้างตัวแทน AI

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 การสนับสนุนหลายภาษา

#### สนับสนุนผ่าน GitHub Action (อัตโนมัติ & อัปเดตเสมอ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](./README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ต้องการโคลนแบบท้องถิ่น?**
>
> ที่เก็บนี้มีการแปลมากกว่า 50 ภาษา ซึ่งเพิ่มขนาดการดาวน์โหลดอย่างมาก หากต้องการโคลนโดยไม่รวมการแปล ให้ใช้ sparse checkout:
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
> วิธีนี้จะให้ทุกอย่างที่คุณต้องการเพื่อทำหลักสูตรนี้ให้เสร็จอย่างรวดเร็วขึ้นมาก
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**หากคุณต้องการให้สนับสนุนภาษาแปลเพิ่มเติม มีรายชื่อไว้ที่ [นี่](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 การเริ่มต้น

หลักสูตรนี้มีบทเรียนที่ครอบคลุมพื้นฐานการสร้างตัวแทน AI แต่ละบทเรียนจะครอบคลุมหัวข้อของมันเอง ดังนั้นคุณสามารถเริ่มจากที่ใดก็ได้ที่คุณชอบ!

มีการสนับสนุนหลายภาษาสำหรับหลักสูตรนี้ ไปที่ [ภาษาที่มีให้ที่นี่](#-multi-language-support) 

หากนี่เป็นครั้งแรกที่คุณสร้างกับโมเดล Generative AI ลองดูหลักสูตร [Generative AI For Beginners](https://aka.ms/genai-beginners) ของเรา ซึ่งรวมบทเรียน 21 บทเกี่ยวกับการสร้างด้วย GenAI

อย่าลืม [กดดาว(🌟) ให้ repo นี้](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) และ [fork repo นี้](https://github.com/microsoft/ai-agents-for-beginners/fork) เพื่อรันโค้ดด้วย

### พบกับผู้เรียนคนอื่น ๆ และรับคำตอบคำถามของคุณ

หากคุณติดขัดหรือมีคำถามใด ๆ เกี่ยวกับการสร้างตัวแทน AI เข้าร่วมช่อง Discord เฉพาะของเราใน [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)

### สิ่งที่คุณต้องมี

แต่ละบทเรียนในหลักสูตรนี้มีตัวอย่างโค้ด ซึ่งคุณสามารถหาได้ในโฟลเดอร์ code_samples คุณสามารถ [fork repo นี้](https://github.com/microsoft/ai-agents-for-beginners/fork) เพื่อสร้างสำเนาของคุณเอง  

ตัวอย่างโค้ดในแบบฝึกหัดเหล่านี้ใช้ Microsoft Agent Framework ร่วมกับ Azure AI Foundry Agent Service V2:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - ต้องมีบัญชี Azure

หลักสูตรนี้ใช้เฟรมเวิร์กและบริการ AI Agent ต่อไปนี้จาก Microsoft:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

ตัวอย่างโค้ดบางส่วนยังรองรับผู้ให้บริการที่เข้ากันได้กับ OpenAI ทางเลือกเช่น [MiniMax](https://platform.minimaxi.com/) ซึ่งมีโมเดลบริบทขนาดใหญ่ (สูงสุด 204K tokens) ดู [การตั้งค่าหลักสูตร](./00-course-setup/README.md) เพื่อดูรายละเอียดการกำหนดค่า

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการรันโค้ดสำหรับหลักสูตรนี้ ไปที่ [การตั้งค่าหลักสูตร](./00-course-setup/README.md)

## 🙏 ต้องการช่วยไหม?

คุณมีคำแนะนำหรือพบการสะกดผิดหรือข้อผิดพลาดของโค้ดหรือไม่? [แจ้งปัญหา](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) หรือ [สร้าง pull request](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 แต่ละบทเรียนประกอบด้วย

- บทเรียนเขียนที่อยู่ใน README และวิดีโอสั้น
- ตัวอย่างโค้ด Python ที่ใช้ Microsoft Agent Framework ร่วมกับ Azure AI Foundry
- ลิงก์ไปยังแหล่งข้อมูลเพิ่มเติมสำหรับการเรียนรู้ต่อเนื่อง


## 🗃️ บทเรียน

| **บทเรียน**                                 | **ข้อความ & โค้ด**                                  | **วิดีโอ**                                                | **การเรียนรู้เพิ่มเติม**                                                               |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| แนะนำตัวแทน AI และกรณีการใช้งานตัวแทน      | [ลิงก์](./01-intro-to-ai-agents/README.md)           | [วิดีโอ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)   | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| สำรวจเฟรมเวิร์กตัวแทน AI                    | [ลิงก์](./02-explore-agentic-frameworks/README.md)   | [วิดีโอ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)   | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| เข้าใจแบบแผนการออกแบบตัวแทน AI               | [ลิงก์](./03-agentic-design-patterns/README.md)      | [วิดีโอ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)   | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| แบบแผนการใช้เครื่องมือ                       | [ลิงก์](./04-tool-use/README.md)                     | [วิดีโอ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)   | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agentic RAG                                  | [ลิงก์](./05-agentic-rag/README.md)                 | [วิดีโอ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)   | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| การสร้างตัวแทน AI ที่น่าเชื่อถือ            | [ลิงก์](./06-building-trustworthy-agents/README.md) | [วิดีโอ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK )  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| แบบแผนการออกแบบการวางแผน                     | [ลิงก์](./07-planning-design/README.md)              | [วิดีโอ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)   | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| แบบแผนการออกแบบตัวแทนหลายตัว                 | [ลิงก์](./08-multi-agent/README.md)                 | [วิดีโอ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)   | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| รูปแบบการออกแบบการรู้จักคิด (Metacognition Design Pattern) | [ลิงก์](./09-metacognition/README.md)               | [วิดีโอ](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ตัวแทนปัญญาประดิษฐ์ในการผลิต                    | [ลิงก์](./10-ai-agents-production/README.md)        | [วิดีโอ](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| การใช้โพรโทคอล Agentic (MCP, A2A และ NLWeb)       | [ลิงก์](./11-agentic-protocols/README.md)           | [วิดีโอ](https://youtu.be/X-Dh9R3Opn8)                                 | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| วิศวกรรมบริบทสำหรับตัวแทน AI                      | [ลิงก์](./12-context-engineering/README.md)         | [วิดีโอ](https://youtu.be/F5zqRV7gEag)                                 | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| การจัดการความทรงจำ Agentic                          | [ลิงก์](./13-agent-memory/README.md)     |      [วิดีโอ](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| การสำรวจกรอบงาน Microsoft Agent                   | [ลิงก์](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| การสร้างตัวแทนใช้งานคอมพิวเตอร์ (CUA)             | [ลิงก์](./15-browser-use/README.md)     |                                                            | [ลิงก์](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| การปรับใช้ตัวแทนแบบขยายได้                         | เร็วๆ นี้                            |                                                            |                                                                                        |
| การสร้างตัวแทน AI ท้องถิ่น                         | เร็วๆ นี้                               |                                                            |                                                                                        |
| การรักษาความปลอดภัยตัวแทน AI                      | เร็วๆ นี้                               |                                                            |                                                                                        |

## 🎒 คอร์สอื่นๆ

ทีมของเราผลิตคอร์สอื่นๆ ด้วย! ลองดู:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j สำหรับผู้เริ่มต้น](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js สำหรับผู้เริ่มต้น](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain สำหรับผู้เริ่มต้น](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / ตัวแทน
[![AZD สำหรับผู้เริ่มต้น](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI สำหรับผู้เริ่มต้น](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP สำหรับผู้เริ่มต้น](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents สำหรับผู้เริ่มต้น](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ซีรีส์ Generative AI
[![Generative AI สำหรับผู้เริ่มต้น](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### การเรียนรู้พื้นฐาน
[![ML สำหรับผู้เริ่มต้น](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![วิทยาศาสตร์ข้อมูลสำหรับผู้เริ่มต้น](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI สำหรับผู้เริ่มต้น](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![ความมั่นคงปลอดภัยไซเบอร์สำหรับผู้เริ่มต้น](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![เว็บพัฒนา สำหรับผู้เริ่มต้น](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT สำหรับผู้เริ่มต้น](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![การพัฒนา XR สำหรับผู้เริ่มต้น](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ซีรีส์ Copilot
[![Copilot สำหรับการเขียนโปรแกรมร่วมกับ AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot สำหรับ C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 ขอบคุณชุมชน

ขอบคุณ [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) สำหรับการมีส่วนร่วมตัวอย่างโค้ดสำคัญที่แสดงตัวอย่าง Agentic RAG

## การมีส่วนร่วม

โครงการนี้ต้อนรับการมีส่วนร่วมและข้อเสนอแนะ ส่วนใหญ่ของการมีส่วนร่วมจะต้องให้คุณตกลงใน
Contributor License Agreement (CLA) ที่ประกาศว่าคุณมีสิทธิ์และได้ให้สิทธิ์แก่เราในการใช้
ผลงานของคุณ สำหรับรายละเอียด โปรดเยี่ยมชม <https://cla.opensource.microsoft.com>.

เมื่อคุณส่งคำขอดึงโค้ด CLA bot จะตรวจสอบโดยอัตโนมัติว่าคุณต้องจัดเตรียม
CLA หรือไม่ และประดับคำขอดึงโค้ดอย่างเหมาะสม (เช่น ตรวจสอบสถานะ, แสดงความคิดเห็น) เพียงทำตามคำแนะนำที่
bot ให้ไว้ คุณจะต้องทำเพียงครั้งเดียวสำหรับรีโปทั้งหมดที่ใช้ CLA ของเรา

โครงการนี้ได้ยอมรับ [แนวทางปฏิบัติรหัสเปิดของ Microsoft](https://opensource.microsoft.com/codeofconduct/).
สำหรับข้อมูลเพิ่มเติม ดูที่ [คำถามที่พบบ่อยเกี่ยวกับแนวทางปฏิบัติรหัส](https://opensource.microsoft.com/codeofconduct/faq/) หรือ
ติดต่อ [opencode@microsoft.com](mailto:opencode@microsoft.com) หากมีคำถามหรือข้อคิดเห็นเพิ่มเติม

## เครื่องหมายการค้า

โครงการนี้อาจมีเครื่องหมายการค้าหรือโลโก้ของโครงการ ผลิตภัณฑ์ หรือบริการ การใช้เครื่องหมายการค้า
หรือโลโก้ของ Microsoft อย่างถูกต้องนั้นจะต้องเป็นไปตามและปฏิบัติตาม
[แนวทางการใช้เครื่องหมายการค้าและแบรนด์ของ Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft ในเวอร์ชันที่ดัดแปลงของโครงการนี้ต้องไม่ก่อให้เกิดความสับสนหรือนำไปสู่การสปอนเซอร์โดย Microsoft
การใช้เครื่องหมายการค้าหรือโลโก้ของบุคคลที่สามใดๆ ต้องเป็นไปตามนโยบายของบุคคลที่สามเหล่านั้น

## การขอความช่วยเหลือ

หากคุณติดขัดหรือต้องการสอบถามเกี่ยวกับการสร้างแอป AI เข้าร่วมได้ที่:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

หากคุณมีข้อเสนอแนะเกี่ยวกับผลิตภัณฑ์หรือพบข้อผิดพลาดระหว่างการสร้าง โปรดเยี่ยมชม:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญแนะนำให้ใช้บริการแปลโดยมืออาชีพ เรายังไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่คลาดเคลื่อนที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->