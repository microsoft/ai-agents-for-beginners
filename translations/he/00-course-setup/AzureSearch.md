# מדריך להגדרת Azure AI Search

מדריך זה יעזור לך להגדיר את Azure AI Search באמצעות פורטל Azure. עקוב אחר השלבים הבאים כדי ליצור ולהגדיר את שירות Azure AI Search שלך.

## דרישות מוקדמות

לפני שתתחיל, ודא שיש לך את הדברים הבאים:

- מנוי ל-Azure. אם אין לך מנוי ל-Azure, תוכל ליצור חשבון חינמי ב-[Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## שלב 1: צור חשבון אחסון Azure

1. עקוב אחר ההוראה הזו, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), כדי ליצור חשבון אחסון Azure חדש.
   **הערה**: ודא שסוג חשבון האחסון הוא Standard General Purpose V2.

## שלב 2: צור שירות Azure AI Search

1. התחבר ל-[פורטל Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. בתפריט הניווט בצד שמאל, לחץ על **Create a resource**.
3. בתיבת החיפוש, הקלד "Azure AI Search" ובחר **Azure AI Search** מהרשימה.
4. לחץ על כפתור **Create**.
5. בלשונית **Basics**, ספק את המידע הבא:
   - **Subscription**: בחר את המנוי שלך ב-Azure.
   - **Resource group**: צור קבוצת משאבים חדשה או בחר קיימת.
   - **Resource name**: הזן שם ייחודי לשירות החיפוש שלך.
   - **Region**: בחר את האזור הקרוב ביותר למשתמשים שלך.
   - **Pricing tier**: בחר שכבת תמחור המתאימה לדרישותיך. תוכל להתחיל בשכבת Free לצורך בדיקה.
6. לחץ על **Review + create**.
7. סקור את ההגדרות ולחץ על **Create** כדי ליצור את שירות החיפוש.

## שלב 3: התחל עם Azure AI Search

1. לאחר שהפריסה הושלמה, עבור לשירות החיפוש שלך בפורטל Azure.
2. בלוח הסקירה של שירות החיפוש, העתק את הקישור. הוא אמור להיראות כמו `https://<service-name>.search.windows.net`.
3. **(מומלץ)** אפשר גישה ללא מפתח באמצעות Microsoft Entra ID (RBAC) כפי שמראה שלב 4 למטה — ללא צורך במפתח. הדוגמאות במדריך זה יוצרות/מעדכנות אינדקסים ומעלות מסמכים, שדורשים את תפקיד **Search Service Contributor** ו-**Search Index Data Contributor** (או, לאימות מבוסס מפתח, את **מפתח מנהל ראשי** — לא מפתח השאילתה). רק אם אינך יכול להשתמש ב-RBAC, פתח את לוח **Settings > Keys** והעתק את **מפתח המנהל הראשי**.
4. עקוב אחר השלבים בעמוד [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) כדי ליצור אינדקס, להעלות נתונים ולבצע חיפוש.

## שלב 4: השתמש בכלי Azure AI Search

Azure AI Search משתלב עם כלים שונים לשיפור יכולות החיפוש שלך. תוכל להשתמש ב-Azure CLI, Python SDK, .NET SDK וכלים נוספים עבור תצורות ופעולות מתקדמות.

### שימוש ב-Azure CLI

1. התקן את Azure CLI על ידי ביצוע ההוראות ב-[Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. היכנס ל-Azure CLI באמצעות הפקודה:

   ```bash
   az login
   ```
3. **(מומלץ) אפשר גישה ללא מפתח באמצעות Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    עם RBAC מופעל, דוגמאות ה-Python וה-.NET SDK למטה מאמתות באמצעות `DefaultAzureCredential`, שמשתמש במפגש `az login` שלך במהלך הפיתוח המקומי — ללא צורך במפתח מנהל. ראה [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(מילוט) אימות מבוסס מפתח** — רק אם אינך יכול להשתמש ב-RBAC, אחסן גם את מפתח המנהל:

#### אחסן גם את נקודת הקצה וגם את מפתח ה-API עבור מופע Azure AI Search במשתני סביבה.

   * **zsh / bash**
     ```bash
     # az search service show has no "endpoint" field; build the URL from the service name.
     export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
     export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

   * **PowerShell**
     ```powershell
     # az search service show has no "endpoint" field; build the URL from the service name.
     $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
     $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

### שימוש ב-Python SDK

1. התקן את ספריית הלקוח Azure Cognitive Search ואת Azure Identity עבור Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. השתמש בקוד Python הבא כדי ליצור אינדקס ולהעלות מסמכים:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    # Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    credential = DefaultAzureCredential()
    # Fallback (key-based auth):
    # from azure.core.credentials import AzureKeyCredential
    # credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

    דוגמת ה-.NET למטה משתמשת ב-`DefaultAzureCredential`, שיכולה להשתמש בכניסה שלך ל-Azure CLI מ-`az login` במהלך הפיתוח המקומי.

2. הנה קוד ה-.NET של `AzureSearch.cs`:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:package Azure.Identity@1.21.0
    #:property PublishAot=false

    using Azure;
    using Azure.Identity;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var indexName = "sample-index";

    // Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    // Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    var credential = new DefaultAzureCredential();
    // Fallback (key-based auth): the `using Azure;` directive above already imports
    // AzureKeyCredential; replace the credential line above with:
    // var credential = new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!);
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

לפרטים נוספים, עיין בתיעוד הבא:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## סיכום

הגדרת בהצלחה את Azure AI Search באמצעות פורטל Azure וכלים משולבים. כעת תוכל לחקור תכונות ויכולות מתקדמות יותר של Azure AI Search לשיפור פתרונות החיפוש שלך.

לקבלת סיוע נוסף, בקר ב-[Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->