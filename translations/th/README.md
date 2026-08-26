# ตัวแทน AI สำหรับผู้เริ่มต้น - หลักสูตร

![AI Agents for Beginners](../../translated_images/th/repo-thumbnailv3.917487e234b90100.webp)

## หลักสูตรสอนทุกสิ่งที่คุณจำเป็นต้องรู้เพื่อเริ่มต้นสร้างตัวแทน AI

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 รองรับหลายภาษา

#### รองรับผ่าน GitHub Action (อัตโนมัติ & อัปเดตเสมอ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](./README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ต้องการโคลนแบบท้องถิ่น?**
>
> ที่เก็บนี้รวมการแปลมากกว่า 50 ภาษา ซึ่งเพิ่มขนาดการดาวน์โหลดมาก หากต้องการโคลนโดยไม่มีการแปล ให้ใช้ sparse checkout:
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
> นี่จะให้สิ่งที่คุณต้องการทั้งหมดเพื่อทำหลักสูตรให้เสร็จด้วยการดาวน์โหลดที่เร็วขึ้นมาก
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**หากคุณต้องการให้รองรับภาษาการแปลเพิ่มเติม รายการภาษาเหล่านั้นอยู่ที่ [นี่](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ATgtXmAS5D)](https://discord.com/invite/ATgtXmAS5D)


## 🌱 เริ่มต้นใช้งาน

หลักสูตรนี้มีบทเรียนครอบคลุมพื้นฐานการสร้างตัวแทน AI แต่ละบทเรียนจะกล่าวถึงหัวข้อของตัวเอง ดังนั้นเริ่มต้นได้จากตรงไหนก็ได้ตามที่คุณชอบ!

มีการรองรับหลายภาษาสำหรับหลักสูตรนี้ ไปดู [ภาษาที่รองรับที่นี่](#-multi-language-support). 

หากนี่เป็นครั้งแรกของคุณในการสร้างด้วยโมเดล Generative AI ให้ลองดูหลักสูตร [Generative AI For Beginners](https://aka.ms/genai-beginners) ซึ่งมี 21 บทเรียนเกี่ยวกับการสร้างด้วย GenAI

อย่าลืม [ให้ดาว (🌟) ที่เก็บนี้](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) และ [fork ที่เก็บนี้](https://github.com/microsoft/ai-agents-for-beginners/fork) เพื่อรันโค้ด

### พบปะผู้เรียนอื่นๆ และรับคำตอบสำหรับคำถามของคุณ

หากคุณติดขัดหรือต้องการคำถามเกี่ยวกับการสร้างตัวแทน AI เข้าร่วมช่อง Discord เฉพาะของเราใน [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)

### สิ่งที่คุณต้องมี

แต่ละบทเรียนในหลักสูตรนี้มีตัวอย่างโค้ด ซึ่งสามารถพบได้ในโฟลเดอร์ code_samples คุณสามารถ [fork ที่เก็บนี้](https://github.com/microsoft/ai-agents-for-beginners/fork) เพื่อสร้างสำเนาของตัวเองได้  

ตัวอย่างโค้ดในแบบฝึกหัดเหล่านี้ใช้ Microsoft Agent Framework กับ Microsoft Foundry Agent Service V2:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - ต้องมีบัญชี Azure

หลักสูตรนี้ใช้เฟรมเวิร์กและบริการตัวแทน AI ดังต่อไปนี้จาก Microsoft:

- [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/agent-framework/overview/)
- [Microsoft Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

ตัวอย่างโค้ดบางตัวอย่างยังรองรับผู้ให้บริการที่เข้ากันได้กับ OpenAI ทางเลือก เช่น [MiniMax](https://platform.minimaxi.com/) ซึ่งมีโมเดลบริบทขนาดใหญ่ (สูงสุด 204K โทเค็น) ดูรายละเอียดการตั้งค่าได้ที่ [Course Setup](./00-course-setup/README.md)

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการรันโค้ดสำหรับหลักสูตรนี้ ไปที่ [Course Setup](./00-course-setup/README.md)

## 🙏 ต้องการช่วยไหม?

คุณมีคำแนะนำหรือตรวจพบข้อผิดพลาดการสะกดหรือโค้ดไหม? [แจ้งปัญหา](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) หรือ [สร้าง pull request](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 แต่ละบทเรียนประกอบด้วย

- บทเรียนลายลักษณ์อักษรที่อยู่ใน README และวิดีโอสั้นๆ
- ตัวอย่างโค้ด Python ใช้ Microsoft Agent Framework กับ Microsoft Foundry
- ลิงก์ไปยังทรัพยากรเพิ่มเติมเพื่อการเรียนรู้ต่อเนื่อง


## 🗃️ บทเรียน

| **บทเรียน**                                 | **ข้อความ & โค้ด**                                  | **วิดีโอ**                                                  | **การเรียนรู้เพิ่มเติม**                                                             |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| แนะนำตัวแทน AI และกรณีใช้งานตัวแทน          | [ลิงก์](./01-intro-to-ai-agents/README.md)          | [วิดีโอ](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| สำรวจเฟรมเวิร์กตัวแทน AI                     | [ลิงก์](./02-explore-agentic-frameworks/README.md)  | [วิดีโอ](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ทำความเข้าแบบแผนการออกแบบตัวแทน AI          | [ลิงก์](./03-agentic-design-patterns/README.md)     | [วิดีโอ](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| แบบแผนการใช้งานเครื่องมือ                    | [ลิงก์](./04-tool-use/README.md)                    | [วิดีโอ](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Agentic RAG                                  | [ลิงก์](./05-agentic-rag/README.md)                 | [วิดีโอ](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| การสร้างตัวแทน AI ที่น่าเชื่อถือ              | [ลิงก์](./06-building-trustworthy-agents/README.md) | [วิดีโอ](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| แบบแผนการวางแผน                             | [ลิงก์](./07-planning-design/README.md)             | [วิดีโอ](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| แบบแผนการออกแบบตัวแทนหลายตัว                  | [ลิงก์](./08-multi-agent/README.md)                 | [วิดีโอ](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [ลิงก์](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

| รูปแบบการออกแบบเมตาคอกนิชัน                 | [Link](./09-metacognition/README.md)               | [วิดีโอ](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ตัวแทน AI ในการผลิต                      | [Link](./10-ai-agents-production/README.md)        | [วิดีโอ](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| การใช้โปรโตคอล agentic (MCP, A2A และ NLWeb) | [Link](./11-agentic-protocols/README.md)           | [วิดีโอ](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| วิศวกรรมบริบทสำหรับตัวแทน AI            | [Link](./12-context-engineering/README.md)         | [วิดีโอ](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| การจัดการหน่วยความจำ agentic                      | [Link](./13-agent-memory/README.md)     |      [วิดีโอ](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| การสำรวจ Microsoft Agent Framework                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| การสร้างตัวแทนใช้คอมพิวเตอร์ (CUA)           | [Link](./15-browser-use/README.md)     |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| การปรับใช้ตัวแทนที่ปรับขนาดได้                    | [Link](./16-deploying-scalable-agents/README.md) |                                                    | [Link](https://learn.microsoft.com/azure/ai-foundry/agents/overview)                   |
| การสร้างตัวแทน AI บนเครื่อง                     | [Link](./17-creating-local-ai-agents/README.md)  |                                                    | [Link](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)                    |
| การรักษาความปลอดภัยตัวแทน AI                           | [Link](./18-securing-ai-agents/README.md)  |                                                            | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |

## 🎒 คอร์สอื่นๆ

ทีมของเราผลิตคอร์สอื่นๆ! ลองดูได้ที่:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / ตัวแทน
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ชุดความรู้ AI สร้างสรรค์
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### การเรียนรู้หลัก
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ชุด Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 ขอขอบคุณชุมชน

ขอขอบคุณ [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) สำหรับการมีส่วนร่วมโค้ดตัวอย่างสำคัญที่แสดงถึง Agentic RAG.

## การมีส่วนร่วม

โปรเจกต์นี้ยินดีรับการมีส่วนร่วมและคำแนะนำ ส่วนใหญ่การมีส่วนร่วมต้องการให้คุณยอมรับ
ข้อตกลงใบอนุญาตผู้ร่วมพัฒนา (CLA) ที่ระบุว่าคุณมีสิทธิ์และจริง ๆ แล้วให้สิทธิ์เรา
ในการใช้การมีส่วนร่วมของคุณ สำหรับรายละเอียด โปรดเยี่ยมชม <https://cla.opensource.microsoft.com>.

เมื่อคุณส่ง pull request บอท CLA จะตรวจสอบโดยอัตโนมัติว่าคุณต้องจัดเตรียม
CLA หรือไม่ และตกแต่ง PR อย่างเหมาะสม (เช่น การตรวจสอบสถานะ, ความคิดเห็น) เพียงปฏิบัติตามคำแนะนำ
ที่บอทให้ไว้ คุณจะต้องทำแค่ครั้งเดียวในทุก repo ที่ใช้ CLA ของเรา

โปรเจกต์นี้ได้นำ [จรรยาบรรณโค้ดเปิดของ Microsoft](https://opensource.microsoft.com/codeofconduct/) มาใช้
สำหรับข้อมูลเพิ่มเติมดู [คำถามที่พบบ่อยเกี่ยวกับจรรยาบรรณ](https://opensource.microsoft.com/codeofconduct/faq/) หรือ
ติดต่อ [opencode@microsoft.com](mailto:opencode@microsoft.com) หากมีคำถามหรือความคิดเห็นเพิ่มเติม

## เครื่องหมายการค้า

โปรเจกต์นี้อาจประกอบด้วยเครื่องหมายการค้าหรือโลโก้ของโปรเจกต์ ผลิตภัณฑ์ หรือบริการต่าง ๆ การใช้
เครื่องหมายการค้าหรือโลโก้ของ Microsoft ที่ได้รับอนุญาตต้องปฏิบัติตาม
[แนวทางการใช้เครื่องหมายการค้าและแบรนด์ของ Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)
การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft ในเวอร์ชันที่แก้ไขของโปรเจกต์นี้ ต้องไม่สร้างความสับสนหรือบ่งชี้ว่าได้รับการสนับสนุนจาก Microsoft
การใช้เครื่องหมายการค้าหรือโลโก้ของบุคคลที่สามอยู่ภายใต้นโยบายของบุคคลที่สามนั้น ๆ

## การขอความช่วยเหลือ


หากคุณติดขัดหรือมีคำถามเกี่ยวกับการสร้างแอป AI เข้าร่วมได้ที่:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

หากคุณมีข้อเสนอแนะผลิตภัณฑ์หรือพบข้อผิดพลาดระหว่างการสร้างเยี่ยมชม:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->