<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T18:40:31+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "he"
}
-->
# מדריך אינטגרציה לשרת MCP

## דרישות מקדימות
- Node.js מותקן (גרסה 14 או גבוהה יותר)
- מנהל חבילות npm
- סביבת Python עם התלויות הנדרשות

## שלבי התקנה

1. **התקנת חבילת שרת MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **הפעלת שרת MCP**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   השרת אמור להתחיל ולהציג כתובת URL לחיבור.

3. **אימות חיבור**  
   - חפשו את סמל התקע (🔌) בממשק Chainlit  
   - מספר (1) אמור להופיע ליד סמל התקע, מה שמעיד על חיבור מוצלח  
   - הקונסולה אמורה להציג: "GitHub plugin setup completed successfully" (יחד עם שורות סטטוס נוספות)

## פתרון בעיות

### בעיות נפוצות

1. **התנגשות ביציאה**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   פתרון: שינוי היציאה באמצעות:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **בעיות אימות**  
   - ודאו שפרטי ההתחברות ל-GitHub מוגדרים כראוי  
   - בדקו שקובץ .env מכיל את הטוקנים הנדרשים  
   - וודאו שיש גישה ל-API של GitHub  

3. **חיבור נכשל**  
   - ודאו שהשרת פועל ביציאה הצפויה  
   - בדקו את הגדרות חומת האש  
   - וודאו שסביבת Python מכילה את החבילות הנדרשות  

## אימות חיבור

השרת MCP מחובר כראוי כאשר:  
1. הקונסולה מציגה "GitHub plugin setup completed successfully"  
2. לוגי החיבור מציגים "✓ MCP Connection Status: Active"  
3. פקודות GitHub פועלות בממשק הצ'אט  

## משתני סביבה

נדרשים בקובץ .env שלכם:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## בדיקת חיבור

שלחו את הודעת הבדיקה הזו בצ'אט:  
```
Show me the repositories for username: [GitHub Username]
```  
תגובה מוצלחת תציג מידע על מאגרי הנתונים.  

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.