<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:42:16+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "he"
}
-->
# מדריך הגדרת Azure AI Search

מדריך זה יסייע לך להגדיר את Azure AI Search באמצעות פורטל Azure. עקוב אחר השלבים הבאים ליצירה ולהגדרת שירות Azure AI Search שלך.

## דרישות מקדימות

לפני שתתחיל, ודא שיש לך את הדברים הבאים:

- מנוי Azure. אם אין לך מנוי Azure, תוכל ליצור חשבון חינמי ב-[חשבון חינמי של Azure](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## שלב 1: יצירת חשבון אחסון Azure

1. עקוב אחר ההוראות ב-[יצירת חשבון אחסון Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) כדי ליצור חשבון אחסון חדש ב-Azure.
   **NOTE**: ודא שסוג חשבון האחסון הוא Standard General Purpose V2.

## שלב 2: יצירת שירות Azure AI Search

1. היכנס ל-[פורטל Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. בלוח הניווט בצד שמאל, לחץ על **Create a resource**.
3. בתיבת החיפוש, הקלד "Azure AI Search" ובחר **Azure AI Search** מרשימת התוצאות.
4. לחץ על כפתור **Create**.
5. בלשונית **Basics**, ספק את המידע הבא:
   - **Subscription**: בחר את מנוי Azure שלך.
   - **Resource group**: צור קבוצת משאבים חדשה או בחר אחת קיימת.
   - **Resource name**: הזן שם ייחודי לשירות החיפוש שלך.
   - **Region**: בחר את האזור הקרוב ביותר למשתמשים שלך.
   - **Pricing tier**: בחר רמת תמחור שמתאימה לצרכים שלך. תוכל להתחיל עם הרמה החינמית לצורך בדיקות.
6. לחץ על **Review + create**.
7. סקור את ההגדרות ולחץ על **Create** כדי ליצור את שירות החיפוש.

## שלב 3: התחלה עם Azure AI Search

1. לאחר שהפריסה הושלמה, נווט לשירות החיפוש שלך בפורטל Azure.
2. בלוח סקירת שירות החיפוש, העתק את כתובת ה-URL. היא אמורה להיראות כמו `https://<service-name>.search.windows.net`.
3. בלוח Settings > Keys, העתק את מפתח השאילתה.
4. עקוב אחר השלבים בדף [מדריך התחלה מהירה](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) כדי ליצור אינדקס, להעלות נתונים ולבצע שאילתת חיפוש.

## שלב 4: שימוש בכלי Azure AI Search

Azure AI Search משתלב עם כלים שונים לשיפור יכולות החיפוש שלך. תוכל להשתמש ב-Azure CLI, Python SDK, .NET SDK וכלים נוספים לצורך הגדרות מתקדמות ותפעול.

### שימוש ב-Azure CLI

1. התקן את Azure CLI על ידי ביצוע ההוראות ב-[התקנת Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. היכנס ל-Azure CLI באמצעות הפקודה:

   ```bash
   az login
   ```

3. שמור את נקודת הקצה ואת מפתח ה-API של שירות Azure AI Search במשתני סביבה.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### שימוש ב-Python SDK

1. התקן את ספריית הלקוח של Azure Cognitive Search עבור Python:

   ```bash
   pip install azure-search-documents
   ```

2. השתמש בקוד Python הבא כדי ליצור אינדקס ולהעלות מסמכים:

    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = "sample-index"

    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(service_endpoint, credential)

    fields = [
        SimpleField(name="id", type=edm.String, key=True),
        SimpleField(name="content", type=edm.String, searchable=True),
    ]

    index = SearchIndex(name=index_name, fields=fields)

    index_client.create_index(index)

    search_client = SearchClient(service_endpoint, index_name, credential)

    documents = [
        {"id": "1", "content": "Hello world"},
        {"id": "2", "content": "Azure Cognitive Search"}
    ]

    search_client.upload_documents(documents)
    ```

### שימוש ב-.NET SDK

1. הרץ את הפקודה הבאה כדי ליצור אינדקס ולהעלות מסמכים:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. הנה קוד ה-.NET של `AzureSearch.cs`:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:property PublishAot=false

    using Azure;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var apiKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!;
    var indexName = "sample-index";

    var credential = new AzureKeyCredential(apiKey);
    var indexClient = new SearchIndexClient(serviceEndpoint, credential);

    var fields = new List<SearchField>()
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    };

    var index = new SearchIndex(name: indexName, fields: fields);

    var response = await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{response.Value.Name}' ready.");

    var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

    var documents = new[]
    {
        new { id = "1", content = "Hello world" },
        new { id = "2", content = "Azure Cognitive Search" }
    };

    var result = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {result.Value.Results.Count} documents to index '{response.Value.Name}'.");
    ```

למידע מפורט יותר, עיין בתיעוד הבא:

- [יצירת שירות Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [התחלה עם Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [כלי Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## סיכום

הגדרת בהצלחה את Azure AI Search באמצעות פורטל Azure ושילוב כלים. כעת תוכל לחקור תכונות מתקדמות ויכולות של Azure AI Search לשיפור פתרונות החיפוש שלך.

לעזרה נוספת, בקר בתיעוד [Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.