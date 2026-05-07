# סוכני AI למתחילים - קורס

![AI Agents for Beginners](../../translated_images/he/repo-thumbnailv2.06f4a48036fde647.webp)

## קורס המלמד הכל שצריך לדעת כדי להתחיל לבנות סוכני AI

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 תמיכה בריבוי שפות

#### נתמך באמצעות GitHub Action (אוטומטי ותמיד מעודכן)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](./README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **האם אתם מעדיפים לשכפל מקומית?**
>
> מאגר זה כולל תרגומים ב-50+ שפות, מה שמגדיל משמעותית את גודל ההורדה. כדי לשכפל ללא תרגומים, השתמשו ב-sparse checkout:
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
> זה נותן לכם את כל מה שצריך כדי להשלים את הקורס עם הורדה מהירה יותר.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**אם אתם מעוניינים בתמיכה בשפות תרגום נוספות, רשימת השפות הנתמכות נמצאת [כאן](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 התחלה

הקורס כולל שיעורים המכסים את יסודות בניית סוכני AI. כל שיעור עוסק בנושא עצמאי, אז התחילו איפה שאתם רוצים!

יש תמיכה בריבוי שפות עבור הקורס הזה. עברו אל [השפות הזמינות כאן](#-multi-language-support).

אם זו הפעם הראשונה שלכם בבנייה עם מודלי AI גנרטיביים, בדקו את קורס [Generative AI For Beginners](https://aka.ms/genai-beginners), הכולל 21 שיעורים על בנייה עם GenAI.

אל תשכחו [לסמן בכוכב (🌟) את המאגר הזה](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ו-[לעשות פורק למאגר](https://github.com/microsoft/ai-agents-for-beginners/fork) כדי להריץ את הקוד.

### פגשו לומדים אחרים, קבלו מענה לשאלותיכם

אם נתקעתם או יש לכם שאלות לגבי בניית סוכני AI, הצטרפו לערוץ דיסקורד הייעודי שלנו ב-[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord).

### מה אתם צריכים

כל שיעור בקורס כולל דוגמאות קוד, שניתן למצוא בתיקיית code_samples. ניתן [לעשות פורק למאגר](https://github.com/microsoft/ai-agents-for-beginners/fork) כדי ליצור עותק משלכם.

דוגמאות הקוד בתרגילים אלו משתמשות במסגרת Microsoft Agent Framework עם שירות Azure AI Foundry Agent V2:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - דרוש חשבון Azure

קורס זה משתמש במסגרת סוכני AI ושירותים הבאים מ-Microsoft:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

חלק מדוגמאות הקוד תומכות גם בספקים אלטרנטיביים התואמים ל-OpenAI כגון [MiniMax](https://platform.minimaxi.com/), המציע מודלים עם הקשר גדול (עד 204K טוקנים). לפרטים על ההגדרות ראו את [Course Setup](./00-course-setup/README.md).

למידע נוסף על הרצת הקוד לקורס זה, עברו ל-[Course Setup](./00-course-setup/README.md).

## 🙏 רוצים לעזור?

יש לכם הצעות או מצאתם טעויות כתיב או קוד? [פתחו בעיה](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) או [צרו משיכת בקשה](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 כל שיעור כולל

- שיעור כתוב במדריך וידאו קצר
- דוגמאות קוד Python המשתמשות ב-Microsoft Agent Framework עם Azure AI Foundry
- קישורים למשאבים נוספים להמשך הלמידה


## 🗃️ שיעורים

| **שיעור**                                   | **טקסט וקוד**                                    | **וידאו**                                                  | **למידה נוספת**                                                                     |
|----------------------------------------------|----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| מבוא לסוכני AI ומקרי שימוש בסוכנים       | [קישור](./01-intro-to-ai-agents/README.md)          | [וידאו](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [קישור](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| חקר מסגרות סוכנים                        | [קישור](./02-explore-agentic-frameworks/README.md)  | [וידאו](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [קישור](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| הבנת תבניות עיצוב סוכנים                  | [קישור](./03-agentic-design-patterns/README.md)     | [וידאו](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [קישור](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| תבנית עיצוב שימוש בכלים                       | [קישור](./04-tool-use/README.md)                    | [וידאו](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [קישור](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| סוכן RAG                                    | [קישור](./05-agentic-rag/README.md)                 | [וידאו](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [קישור](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| בניית סוכני AI אמינים                       | [קישור](./06-building-trustworthy-agents/README.md) | [וידאו](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [קישור](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| תבנית עיצוב תכנון                            | [קישור](./07-planning-design/README.md)             | [וידאו](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [קישור](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| תבנית עיצוב רב-סוכני                       | [קישור](./08-multi-agent/README.md)                 | [וידאו](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [קישור](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| דפוס עיצוב מתודעתית                 | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| סוכני בינה מלאכותית בפרודקשן                      | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| שימוש בפרוטוקולים סוכניים (MCP, A2A ו-NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| הנדסת הקשר לסוכני בינה מלאכותית            | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| ניהול זיכרון סוכני                      | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| חקירת מסגרת הסוכן של מיקרוסופט                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| בניית סוכנים לשימוש במחשב (CUA)           | [Link](./15-browser-use/README.md)     |                                                            | [Link](https://docs.browser-use.com/examples/templates/playwright-integration)         |
| פריסת סוכנים מדרגים                    | בקרוב                            |                                                            |                                                                                        |
| יצירת סוכני בינה מלאכותית מקומיים                     | בקרוב                               |                                                            |                                                                                        |
| אבטחת סוכני בינה מלאכותית                           | בקרוב                               |                                                            |                                                                                        |

## 🎒 קורסים נוספים

הצוות שלנו מייצר קורסים נוספים! בדקו:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j למתחילים](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js למתחילים](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain למתחילים](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / סוכנים
[![AZD למתחילים](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI למתחילים](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP למתחילים](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![סוכני בינה מלאכותית למתחילים](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### סדרת בינה מלאכותית גנרטיבית
[![בינה מלאכותית גנרטיבית למתחילים](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![בינה מלאכותית גנרטיבית (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![בינה מלאכותית גנרטיבית (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![בינה מלאכותית גנרטיבית (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### למידה עיקרית
[![למידת מכונה למתחילים](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![מדעי הנתונים למתחילים](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![בינה מלאכותית למתחילים](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![אבטחת סייבר למתחילים](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![פיתוח ווב למתחילים](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![מחשוב ענן למתחילים](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![פיתוח XR למתחילים](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### סדרת Copilot
[![Copilot לתכנות זוגי בבינה מלאכותית](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot ל-C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![הרפתקת Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 תודה מהקהילה

תודה ל-[Shivam Goyal](https://www.linkedin.com/in/shivam2003/) על תרומה של דוגמאות קוד חשובות המציגות Agentic RAG. 

## תרומה

פרויקט זה מקבל בברכה תרומות והצעות. רוב התרומות דורשות שתסכימו ל-
הסכם רישיון תורם (CLA) המצהיר שיש לכם את הזכות, ושהאמת היא שאתם מעניקים לנו
את הזכויות להשתמש בתרומתכם. לפרטים, בקרו ב- <https://cla.opensource.microsoft.com>.

כאשר אתם מגישים בקשת משיכה, בוט CLA יבחן באופן אוטומטי אם אתם צריכים לספק
CLA ויקשט את בקשת המשיכה בהתאם (למשל, בדיקת מצב, תגובה). פשוט פעלו לפי ההוראות
של הבוט. תצטרכו לעשות זאת רק פעם אחת בכל הרפוזיטוריות המשתמשות ב-CLA שלנו.

פרויקט זה אימץ את [קוד ההתנהגות של מיקרוסופט בקוד פתוח](https://opensource.microsoft.com/codeofconduct/).
למידע נוסף ראו את [שאלות נפוצות על קוד ההתנהגות](https://opensource.microsoft.com/codeofconduct/faq/) או
צרו קשר ב-[opencode@microsoft.com](mailto:opencode@microsoft.com) עם כל שאלה או הערה נוספת.

## סימני מסחר

ייתכן שפרויקט זה מכיל סימני מסחר או לוגואים של פרויקטים, מוצרים או שירותים. שימוש מורשה
בסימני המסחר או בלוגואים של מיקרוסופט כפוף וצריך לעקוב אחרי
[ההנחיות למסחר ומותגים של מיקרוסופט](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
שימוש בסימני מסחר או לוגואים של מיקרוסופט בגרסאות מותאמות של פרויקט זה לא יגרום לבלבול או יציע חסות מצד מיקרוסופט.
כל שימוש בסימני מסחר או לוגואים של צד שלישי כפוף למדיניות של אותם צדדים שלישיים.

## קבלת עזרה

אם נתקעתם או יש לכם שאלות לגבי בניית אפליקציות בינה מלאכותית, הצטרפו ל:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

אם יש לכם משוב על המוצר או שגיאות בזמן בנייה בקרו ב:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להיעזר בתרגום מקצועי של אדם. אנו לא נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->