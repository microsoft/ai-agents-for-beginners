# דוגמת שרת MCP של Github

## תיאור

זו הייתה הדגמה שיצרה עבור האקתון סוכני AI שנערך באמצעות Microsoft Reactor.

הכלים משמשים להמליץ על פרויקטים להאקתון בהתבסס על מאגרים של משתמש ב-Github.
זה נעשה על ידי:

1. **סוכן Github** - שימוש בשרת MCP של Github כדי לאחזר מאגרים ומידע על אותם מאגרים.
2. **סוכן האקתון** - מקבל את הנתונים מסוכן ה-Github ומציע רעיונות יצירתיים לפרויקטים להאקתון בהתבסס על הפרויקטים, השפות שבהן משתמש המשתמש ותחומי הפרויקט של האקתון סוכני AI.
3. **סוכן אירועים** - בהתבסס על הצעת סוכן ההאקתון, סוכן האירועים ימליץ על אירועים רלוונטיים מסדרת האקתון סוכני ה-AI.

## הפעלת הקוד

### משתנים סביבתיים

הדגמה זו משתמשת במסגרת סוכנים של Microsoft, שירות Azure OpenAI, שרת MCP של Github ו-Azure AI Search.

ודאו שיש לכם את משתני הסביבה המתאימים להגדרת השימוש בכלים אלו:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## הפעלת שרת Chainlit

כדי להתחבר לשרת MCP, הדגמה זו משתמשת ב-Chainlit כממשק צ'אט.

להפעלת השרת, השתמשו בפקודה הבאה בטרמינל שלכם:

```bash
chainlit run app.py -w
```


זה אמור להפעיל את שרת ה-Chainlit שלכם בכתובת `localhost:8000` וכן למלא את האינדקס של Azure AI Search שלכם עם תוכן `event-descriptions.md`.

## התחברות לשרת MCP

כדי להתחבר לשרת MCP של Github, בחרו באייקון "תקע" שמתחת לתיבת הצ'אט עם הטקסט "Type your message here..":

![MCP Connect](../../../../../translated_images/he/mcp-chainlit-1.7ed66d648e3cfb28.webp)

משם תוכלו ללחוץ על "Connect an MCP" כדי להוסיף את הפקודה להתחברות לשרת MCP של Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


החליפו את "[YOUR PERSONAL ACCESS TOKEN]" ב-Token האישי שלכם.

לאחר ההתחברות, אמור להופיע (1) ליד אייקון התקע לאישור שהחיבור הושלם. אם לא, נסו להפעיל מחדש את שרת ה-chainlit עם `chainlit run app.py -w`.

## שימוש בדגמה

כדי להתחיל את זרימת העבודה של סוכן ההמלצות לפרויקטים להאקתון, אפשר להקליד הודעה כמו:

"Recommend hackathon projects for the Github user koreyspace"

סוכן הכיוון ינתח את בקשתכם ויקבע איזו שילוב של סוכנים (GitHub, האקתון, וארועים) מתאים ביותר לטפל בשאילתה שלכם. הסוכנים עובדים יחד כדי לספק המלצות מקיפות המבוססות על ניתוח מאגרים של GitHub, יצירת רעיונות לפרויקטים, ואירועי טכנולוגיה רלוונטיים.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור:**
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לשים לב כי תרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפה המקורית מהווה את המקור הרשמי והמהימן. למידע קריטי מומלץ לבצע תרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לכל אי-הבנה או פרשנות מוטעית הנובעים משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->