<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:31:48+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "he"
}
-->
# שיעור 11: שילוב פרוטוקול הקשר מודל (MCP)

## מבוא לפרוטוקול הקשר מודל (MCP)

פרוטוקול הקשר מודל (MCP) הוא מסגרת מתקדמת שנועדה לתקנן את האינטראקציות בין מודלים של בינה מלאכותית לבין יישומי לקוח. MCP משמש כגשר בין מודלים של בינה מלאכותית לבין היישומים המשתמשים בהם, ומספק ממשק אחיד ללא תלות במימוש המודל הבסיסי.

היבטים מרכזיים של MCP:

- **תקשורת מתוקננת**: MCP מגדיר שפה משותפת ליישומים לתקשר עם מודלים של בינה מלאכותית  
- **ניהול הקשר משופר**: מאפשר העברת מידע הקשרי בצורה יעילה למודלים של בינה מלאכותית  
- **תאימות בין-פלטפורמות**: פועל על פני שפות תכנות שונות, כולל C#, Java, JavaScript, Python ו-TypeScript  
- **שילוב חלק**: מאפשר למפתחים לשלב בקלות מודלים שונים של בינה מלאכותית ביישומיהם  

MCP הוא בעל ערך במיוחד בפיתוח סוכנים מבוססי בינה מלאכותית, שכן הוא מאפשר לסוכנים לתקשר עם מערכות ומקורות נתונים שונים באמצעות פרוטוקול אחיד, מה שהופך את הסוכנים לגמישים וחזקים יותר.

## מטרות למידה
- להבין מהו MCP ותפקידו בפיתוח סוכנים מבוססי בינה מלאכותית  
- להגדיר ולהגדיר שרת MCP לשילוב עם GitHub  
- לבנות מערכת רב-סוכנים באמצעות כלי MCP  
- ליישם RAG (הפקת מידע מוגברת) עם Azure Cognitive Search  

## דרישות מוקדמות
- Python 3.8+  
- Node.js 14+  
- מנוי Azure  
- חשבון GitHub  
- הבנה בסיסית של Semantic Kernel  

## הוראות התקנה

1. **הגדרת סביבה**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **הגדרת שירותי Azure**  
   - יצירת משאב Azure Cognitive Search  
   - הגדרת שירות Azure OpenAI  
   - הגדרת משתני סביבה בקובץ `.env`  

3. **הגדרת שרת MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## מבנה הפרויקט

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## רכיבים מרכזיים

### 1. מערכת רב-סוכנים
- סוכן GitHub: ניתוח מאגרי קוד  
- סוכן האקתון: המלצות לפרויקטים  
- סוכן אירועים: הצעות לאירועים טכנולוגיים  

### 2. שילוב עם Azure
- חיפוש קוגניטיבי לאינדוקס אירועים  
- Azure OpenAI לאינטליגנציה של סוכנים  
- יישום תבנית RAG  

### 3. כלי MCP
- ניתוח מאגרי GitHub  
- בדיקת קוד  
- חילוץ מטא-נתונים  

## מעבר על הקוד

הדוגמה מדגימה:  
1. שילוב שרת MCP  
2. תזמור רב-סוכנים  
3. שילוב עם Azure Cognitive Search  
4. יישום תבנית RAG  

תכונות עיקריות:  
- ניתוח מאגרי GitHub בזמן אמת  
- המלצות חכמות לפרויקטים  
- התאמת אירועים באמצעות Azure Search  
- תגובות בזמן אמת עם Chainlit  

## הפעלת הדוגמה

להוראות התקנה מפורטות ומידע נוסף, עיינו ב-[Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. הפעלת שרת MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. הפעלת היישום:  
   ```bash
   chainlit run app.py -w
   ```

3. בדיקת השילוב:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## פתרון בעיות

בעיות נפוצות ופתרונות:  
1. בעיות חיבור ל-MCP  
   - ודאו שהשרת פועל  
   - בדקו זמינות פורטים  
   - אשרו אסימוני GitHub  

2. בעיות בחיפוש Azure  
   - אימות מחרוזות חיבור  
   - בדיקת קיום אינדקס  
   - אימות העלאת מסמכים  

## שלבים הבאים
- חקר כלים נוספים של MCP  
- יישום סוכנים מותאמים אישית  
- שיפור יכולות RAG  
- הוספת מקורות אירועים נוספים  
- **מתקדם**: עיינו ב-[mcp-agents/](../../../11-mcp/code_samples/mcp-agents) לדוגמאות של תקשורת בין סוכנים  

## משאבים
- [MCP למתחילים](https://aka.ms/mcp-for-beginners)  
- [תיעוד MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [תיעוד Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [מדריכי Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.