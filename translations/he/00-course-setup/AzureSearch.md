<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:38:15+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "he"
}
-->
# מדריך הגדרת Azure AI Search

מדריך זה יעזור לך להגדיר את Azure AI Search באמצעות פורטל Azure. עקוב אחר השלבים הבאים כדי ליצור ולהגדיר את שירות Azure AI Search שלך.

## דרישות מוקדמות

לפני שתתחיל, ודא שיש לך את הדברים הבאים:

- מנוי Azure. אם אין לך מנוי Azure, תוכל ליצור חשבון חינמי ב-[Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## שלב 1: יצירת שירות Azure AI Search

1. היכנס ל-[פורטל Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. בפאנל הניווט השמאלי, לחץ על **Create a resource**.
3. בתיבת החיפוש, הקלד "Azure AI Search" ובחר **Azure AI Search** מהרשימה.
4. לחץ על כפתור **Create**.
5. בכרטיסיית **Basics**, ספק את המידע הבא:
   - **Subscription**: בחר את מנוי ה-Azure שלך.
   - **Resource group**: צור קבוצת משאבים חדשה או בחר קיימת.
   - **Resource name**: הזן שם ייחודי לשירות החיפוש שלך.
   - **Region**: בחר את האזור הקרוב ביותר למשתמשים שלך.
   - **Pricing tier**: בחר שכבת תמחור שמתאימה לצרכיך. ניתן להתחיל עם שכבת Free לצורך בדיקות.
6. לחץ על **Review + create**.
7. בדוק את ההגדרות ולחץ על **Create** כדי ליצור את שירות החיפוש.

## שלב 2: התחלת עבודה עם Azure AI Search

1. לאחר שהפריסה הושלמה, עבור לשירות החיפוש שלך בפורטל Azure.
2. בדף הסקירה של שירות החיפוש, לחץ על כפתור **Quickstart**.
3. עקוב אחר השלבים במדריך Quickstart כדי ליצור אינדקס, להעלות נתונים ולבצע שאילתת חיפוש.

### יצירת אינדקס

1. במדריך Quickstart, לחץ על **Create an index**.
2. הגדר את סכמת האינדקס על ידי ציון השדות והתכונות שלהם (למשל, סוג הנתונים, חיפוש, סינון).
3. לחץ על **Create** כדי ליצור את האינדקס.

### העלאת נתונים

1. במדריך Quickstart, לחץ על **Upload data**.
2. בחר מקור נתונים (למשל, Azure Blob Storage, Azure SQL Database) וספק את פרטי החיבור הנדרשים.
3. מיפוי שדות מקור הנתונים לשדות האינדקס.
4. לחץ על **Submit** כדי להעלות את הנתונים לאינדקס.

### ביצוע שאילתת חיפוש

1. במדריך Quickstart, לחץ על **Search explorer**.
2. הזן שאילתת חיפוש בתיבת החיפוש כדי לבדוק את פונקציונליות החיפוש.
3. בדוק את תוצאות החיפוש והתאם את סכמת האינדקס או הנתונים לפי הצורך.

## שלב 3: שימוש בכלי Azure AI Search

Azure AI Search משתלב עם כלים שונים כדי לשפר את יכולות החיפוש שלך. ניתן להשתמש ב-Azure CLI, Python SDK וכלים נוספים להגדרות ופעולות מתקדמות.

### שימוש ב-Azure CLI

1. התקן את Azure CLI על פי ההוראות ב-[Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. היכנס ל-Azure CLI באמצעות הפקודה:
   ```bash
   az login
   ```
3. צור שירות חיפוש חדש באמצעות Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. צור אינדקס באמצעות Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### שימוש ב-Python SDK

1. התקן את ספריית הלקוח של Azure Cognitive Search עבור Python:
   ```bash
   pip install azure-search-documents
   ```
2. השתמש בקוד Python הבא כדי ליצור אינדקס ולהעלות מסמכים:
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

למידע מפורט יותר, עיין בתיעוד הבא:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## סיכום

הגדרת בהצלחה את Azure AI Search באמצעות פורטל Azure והכלים המשולבים. כעת תוכל לחקור תכונות ויכולות מתקדמות יותר של Azure AI Search כדי לשפר את פתרונות החיפוש שלך.

לסיוע נוסף, בקר ב-[Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.