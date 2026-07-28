# مائیکروسافٹ فانڈری ایجنٹ سروس کی ترقی

اس مشق میں، آپ مائیکروسافٹ فانڈری ایجنٹ سروس کے آلات استعمال کرتے ہوئے [مائیکروسافٹ فانڈری پورٹل](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) میں فلائٹ بکنگ کے لیے ایک ایجنٹ بنائیں گے۔ یہ ایجنٹ صارفین سے بات چیت کر سکے گا اور پروازوں کے متعلق معلومات فراہم کرے گا۔

## ضروریات

اس مشق کو مکمل کرنے کے لیے آپ کو درج ذیل چیزوں کی ضرورت ہے:
1. ایک Azure اکاؤنٹ جس میں ایک فعال سبسکرپشن ہو۔ [مفت اکاؤنٹ بنائیں](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)۔
2. آپ کو مائیکروسافٹ فانڈری ہب بنانے کی اجازت ہونی چاہیے یا کوئی ہب آپ کے لیے بنایا گیا ہو۔
    - اگر آپ کا کردار Contributor یا Owner ہے تو، آپ اس ٹیوٹوریل میں دی گئی ہدایات پر عمل کر سکتے ہیں۔

## مائیکروسافٹ فانڈری ہب بنائیں

> **نوٹ:** مائیکروسافٹ فانڈری پہلے Azure AI اسٹوڈیو کے نام سے جانا جاتا تھا۔

1. مائیکروسافٹ فانڈری بلاگ پوسٹ میں موجود [ہدایات](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) کے مطابق مائیکروسافٹ فانڈری ہب بنائیں۔
2. جب آپ کا پروجیکٹ بن جائے، تو جو بھی ٹپس ظاہر ہوں انہیں بند کریں اور مائیکروسافٹ فانڈری پورٹل میں پروجیکٹ صفحہ کا جائزہ لیں، جو مندرجہ ذیل تصویر کے مشابہ ہونا چاہیے:

    ![Microsoft Foundry Project](../../../translated_images/ur/azure-ai-foundry.88d0c35298348c2f.webp)

## ماڈل تعینات کریں

1. اپنے پروجیکٹ کے لیے بائیں جانب پین میں، **My assets** سیکشن میں، **Models + endpoints** صفحہ منتخب کریں۔
2. **Models + endpoints** صفحہ میں، **Model deployments** ٹیب میں، **+ Deploy model** مینو کے تحت، **Deploy base model** منتخب کریں۔
3. فہرست میں `gpt-5-mini` ماڈل تلاش کریں، پھر اسے منتخب کریں اور تصدیق کریں۔

    > **نوٹ**: TPM کو کم کرنا آپ کے سبسکرپشن میں دستیاب کوٹہ کے زیادہ استعمال سے بچاتا ہے۔

    ![Model Deployed](../../../translated_images/ur/model-deployment.3749c53fb81e18fd.webp)

## ایجنٹ بنائیں

اب جب کہ آپ نے ماڈل تعینات کر لیا ہے، آپ ایک ایجنٹ بنا سکتے ہیں۔ ایجنٹ ایک مکالماتی AI ماڈل ہے جو صارفین سے بات چیت کے لیے استعمال کیا جا سکتا ہے۔

1. اپنے پروجیکٹ کے لیے بائیں جانب پین میں، **Build & Customize** سیکشن میں، **Agents** صفحہ منتخب کریں۔
2. **+ Create agent** پر کلک کریں تاکہ ایک نیا ایجنٹ بنایا جا سکے۔ **Agent Setup** ڈائیلاگ باکس میں:
    - ایجنٹ کے لیے کوئی نام درج کریں، جیسے `FlightAgent`۔
    - یقینی بنائیں کہ پہلے سے بنایا گیا `gpt-5-mini` ماڈل ڈیپلائمنٹ منتخب ہے۔
    - **Instructions** کو اس پرامپٹ کے مطابق سیٹ کریں جو آپ چاہتے ہیں کہ ایجنٹ پر عمل کرے۔ مثال کے طور پر:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> ایک تفصیلی پرامپٹ کے لیے، آپ [اس ریپوزیٹری](https://github.com/ShivamGoyal03/RoamMind) کو مزید معلومات کے لیے دیکھ سکتے ہیں۔
    
> مزید برآں، آپ ایجنٹ کی صلاحیتوں کو بڑھانے کے لیے **Knowledge Base** اور **Actions** بھی شامل کر سکتے ہیں تاکہ یہ زیادہ معلومات فراہم کرے اور صارف کی درخواستوں کی بنیاد پر خودکار کام کر سکے۔ اس مشق کے لیے، آپ یہ مراحل چھوڑ سکتے ہیں۔
    
![Agent Setup](../../../translated_images/ur/agent-setup.9bbb8755bf5df672.webp)

3. نیا ملٹی-AI ایجنٹ بنانے کے لیے، بس **New Agent** پر کلک کریں۔ تازہ بنایا گیا ایجنٹ پھر Agents صفحہ پر ظاہر ہوگا۔


## ایجنٹ کا امتحان کریں

ایجنٹ بنانے کے بعد، آپ اس کا امتحان کر سکتے ہیں کہ یہ Microsoft Foundry پورٹل کے پلے گراؤنڈ میں صارف کی سوالات پر کیسے ردعمل دیتا ہے۔

1. اپنے ایجنٹ کے لیے **Setup** پین کے اوپر، **Try in playground** منتخب کریں۔
2. **Playground** پین میں، آپ چیٹ ونڈو میں سوالات ٹائپ کرکے ایجنٹ سے بات چیت کر سکتے ہیں۔ مثال کے طور پر، آپ ایجنٹ سے پوچھ سکتے ہیں کہ وہ 28 تاریخ کو سیئٹل سے نیو یارک کے لیے پروازیں تلاش کرے۔

    > **نوٹ**: ایجنٹ درست جوابات فراہم نہ کر سکے کیونکہ اس مشق میں کوئی حقیقی وقت کا ڈیٹا استعمال نہیں کیا جا رہا ہے۔ مقصد یہ ہے کہ ایجنٹ کی صلاحیت کو جانچا جائے کہ وہ فراہم کردہ ہدایات کی بنیاد پر صارف کے سوالات کو سمجھ اور جواب دے سکے۔

    ![Agent Playground](../../../translated_images/ur/agent-playground.dc146586de715010.webp)

3. ایجنٹ کا امتحان کرنے کے بعد، آپ اسے مزید اہداف، تربیتی ڈیٹا، اور ایکشنز شامل کرکے اس کی صلاحیتوں کو بڑھا سکتے ہیں۔

## وسائل کی صفائی کریں

جب آپ نے ایجنٹ کا امتحان مکمل کر لیا ہو تو اضافی لاگت سے بچنے کے لیے اسے حذف کر سکتے ہیں۔
1. [Azure پورٹل](https://portal.azure.com) کھولیں اور اس ریسورس گروپ کا مواد دیکھیں جہاں آپ نے اس مشق میں استعمال ہونے والے ہب کے وسائل تعینات کیے تھے۔
2. ٹول بار پر، **Delete resource group** منتخب کریں۔
3. ریسورس گروپ کا نام درج کریں اور حذف کرنے کی تصدیق کریں۔

## وسائل

- [مائیکروسافٹ فانڈری دستاویزیات](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [مائیکروسافٹ فانڈری پورٹل](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [مائیکروسافٹ فانڈری کے ساتھ آغاز](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure پر AI ایجنٹس کی بنیادی باتیں](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->