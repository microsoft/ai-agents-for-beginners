<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T07:41:06+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ar"
}
-->
# الدرس 11: دمج بروتوكول سياق النموذج (MCP)

## مقدمة إلى بروتوكول سياق النموذج (MCP)

بروتوكول سياق النموذج (MCP) هو إطار عمل متطور مصمم لتوحيد التفاعلات بين نماذج الذكاء الاصطناعي وتطبيقات العملاء. يعمل MCP كجسر بين نماذج الذكاء الاصطناعي والتطبيقات التي تستخدمها، مما يوفر واجهة موحدة بغض النظر عن تنفيذ النموذج الأساسي.

الجوانب الرئيسية لـ MCP:

- **اتصال موحد**: يضع MCP لغة مشتركة للتطبيقات للتواصل مع نماذج الذكاء الاصطناعي  
- **إدارة سياق محسّنة**: يتيح تمرير المعلومات السياقية بكفاءة إلى نماذج الذكاء الاصطناعي  
- **التوافق عبر الأنظمة**: يعمل عبر لغات برمجة متعددة مثل C#، Java، JavaScript، Python، وTypeScript  
- **تكامل سلس**: يمكّن المطورين من دمج نماذج الذكاء الاصطناعي المختلفة بسهولة في تطبيقاتهم  

يعد MCP ذا قيمة خاصة في تطوير وكلاء الذكاء الاصطناعي، حيث يسمح للوكلاء بالتفاعل مع أنظمة ومصادر بيانات متعددة من خلال بروتوكول موحد، مما يجعل الوكلاء أكثر مرونة وقوة.

## أهداف التعلم
- فهم ماهية MCP ودوره في تطوير وكلاء الذكاء الاصطناعي  
- إعداد وتكوين خادم MCP للتكامل مع GitHub  
- بناء نظام متعدد الوكلاء باستخدام أدوات MCP  
- تنفيذ RAG (توليد معزز بالاسترجاع) باستخدام Azure Cognitive Search  

## المتطلبات الأساسية
- Python 3.8+  
- Node.js 14+  
- اشتراك Azure  
- حساب GitHub  
- فهم أساسي لـ Semantic Kernel  

## تعليمات الإعداد

1. **إعداد البيئة**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **تكوين خدمات Azure**  
   - إنشاء مورد Azure Cognitive Search  
   - إعداد خدمة Azure OpenAI  
   - تكوين متغيرات البيئة في `.env`  

3. **إعداد خادم MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## هيكل المشروع

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

## المكونات الأساسية

### 1. نظام متعدد الوكلاء
- وكيل GitHub: تحليل المستودعات  
- وكيل Hackathon: توصيات المشاريع  
- وكيل الأحداث: اقتراحات الفعاليات التقنية  

### 2. تكامل Azure
- البحث الإدراكي لفهرسة الفعاليات  
- Azure OpenAI لذكاء الوكلاء  
- تنفيذ نمط RAG  

### 3. أدوات MCP
- تحليل مستودعات GitHub  
- فحص الكود  
- استخراج البيانات الوصفية  

## استعراض الكود

يوضح المثال:  
1. تكامل خادم MCP  
2. تنسيق متعدد الوكلاء  
3. تكامل Azure Cognitive Search  
4. تنفيذ نمط RAG  

الميزات الرئيسية:  
- تحليل مستودعات GitHub في الوقت الفعلي  
- توصيات ذكية للمشاريع  
- مطابقة الفعاليات باستخدام Azure Search  
- استجابات متدفقة باستخدام Chainlit  

## تشغيل المثال

للحصول على تعليمات إعداد مفصلة ومزيد من المعلومات، راجع [README مثال خادم MCP على GitHub](./code_samples/github-mcp/README.md).

1. تشغيل خادم MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. تشغيل التطبيق:  
   ```bash
   chainlit run app.py -w
   ```

3. اختبار التكامل:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## استكشاف الأخطاء وإصلاحها

المشاكل الشائعة وحلولها:  
1. مشاكل اتصال MCP  
   - تحقق من تشغيل الخادم  
   - تحقق من توفر المنفذ  
   - تأكد من رموز GitHub  

2. مشاكل Azure Search  
   - تحقق من سلاسل الاتصال  
   - تحقق من وجود الفهرس  
   - تأكد من تحميل المستندات  

## الخطوات التالية
- استكشاف أدوات MCP الإضافية  
- تنفيذ وكلاء مخصصة  
- تحسين قدرات RAG  
- إضافة المزيد من مصادر الفعاليات  
- **متقدم**: تحقق من [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) للحصول على أمثلة عن تواصل الوكلاء مع بعضهم البعض  

## الموارد
- [MCP للمبتدئين](https://aka.ms/mcp-for-beginners)  
- [وثائق MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [وثائق Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [أدلة Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.