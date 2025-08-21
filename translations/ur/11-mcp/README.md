<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:03:00+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ur"
}
-->
# سبق 11: ماڈل کانٹیکسٹ پروٹوکول (MCP) انضمام

## ماڈل کانٹیکسٹ پروٹوکول (MCP) کا تعارف

ماڈل کانٹیکسٹ پروٹوکول (MCP) ایک جدید فریم ورک ہے جو AI ماڈلز اور کلائنٹ ایپلیکیشنز کے درمیان تعاملات کو معیاری بنانے کے لیے ڈیزائن کیا گیا ہے۔ MCP AI ماڈلز اور ان ایپلیکیشنز کے درمیان ایک پل کا کام کرتا ہے جو ان ماڈلز کو استعمال کرتی ہیں، اور یہ ایک مستقل انٹرفیس فراہم کرتا ہے، چاہے ماڈل کی بنیادی عمل درآمد کچھ بھی ہو۔

MCP کی اہم خصوصیات:

- **معیاری مواصلات**: MCP ایپلیکیشنز کے لیے ایک مشترکہ زبان قائم کرتا ہے تاکہ وہ AI ماڈلز سے بات چیت کر سکیں  
- **بہتر کانٹیکسٹ مینجمنٹ**: AI ماڈلز کو سیاق و سباق کی معلومات مؤثر طریقے سے منتقل کرنے کی اجازت دیتا ہے  
- **کراس پلیٹ فارم مطابقت**: مختلف پروگرامنگ زبانوں جیسے C#, Java, JavaScript, Python، اور TypeScript کے ساتھ کام کرتا ہے  
- **آسان انضمام**: ڈویلپرز کو مختلف AI ماڈلز کو اپنی ایپلیکیشنز میں آسانی سے شامل کرنے کے قابل بناتا ہے  

MCP خاص طور پر AI ایجنٹ کی ترقی میں قیمتی ہے کیونکہ یہ ایجنٹس کو مختلف سسٹمز اور ڈیٹا ذرائع کے ساتھ ایک متحد پروٹوکول کے ذریعے تعامل کرنے کی اجازت دیتا ہے، جس سے ایجنٹس زیادہ لچکدار اور طاقتور بن جاتے ہیں۔

## سیکھنے کے مقاصد
- MCP کیا ہے اور AI ایجنٹ کی ترقی میں اس کا کردار سمجھنا  
- GitHub انضمام کے لیے MCP سرور کو سیٹ اپ اور کنفیگر کرنا  
- MCP ٹولز کا استعمال کرتے ہوئے ایک ملٹی ایجنٹ سسٹم بنانا  
- Azure Cognitive Search کے ساتھ RAG (Retrieval Augmented Generation) کو نافذ کرنا  

## ضروریات
- Python 3.8+  
- Node.js 14+  
- Azure سبسکرپشن  
- GitHub اکاؤنٹ  
- Semantic Kernel کی بنیادی سمجھ  

## سیٹ اپ ہدایات

1. **ماحول کی ترتیب**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure سروسز کو کنفیگر کریں**
   - Azure Cognitive Search ریسورس بنائیں  
   - Azure OpenAI سروس سیٹ اپ کریں  
   - `.env` میں ماحول کے متغیرات کو کنفیگر کریں  

3. **MCP سرور سیٹ اپ کریں**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## پروجیکٹ کی ساخت

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

## بنیادی اجزاء

### 1. ملٹی ایجنٹ سسٹم
- GitHub ایجنٹ: ریپوزٹری تجزیہ  
- Hackathon ایجنٹ: پروجیکٹ کی تجاویز  
- Events ایجنٹ: ٹیک ایونٹ کی تجاویز  

### 2. Azure انضمام
- ایونٹ انڈیکسنگ کے لیے Cognitive Search  
- ایجنٹ انٹیلیجنس کے لیے Azure OpenAI  
- RAG پیٹرن کا نفاذ  

### 3. MCP ٹولز
- GitHub ریپوزٹری تجزیہ  
- کوڈ انسپیکشن  
- میٹا ڈیٹا نکالنا  

## کوڈ واک تھرو

یہ نمونہ درج ذیل کو ظاہر کرتا ہے:
1. MCP سرور انضمام  
2. ملٹی ایجنٹ آرکیسٹریشن  
3. Azure Cognitive Search انضمام  
4. RAG پیٹرن کا نفاذ  

اہم خصوصیات:
- ریئل ٹائم GitHub ریپوزٹری تجزیہ  
- ذہین پروجیکٹ کی تجاویز  
- Azure Search کا استعمال کرتے ہوئے ایونٹ میچنگ  
- Chainlit کے ساتھ اسٹریمنگ جوابات  

## نمونہ چلانا

تفصیلی سیٹ اپ ہدایات اور مزید معلومات کے لیے، [Github MCP Server Example README](./code_samples/github-mcp/README.md) کا حوالہ دیں۔

1. MCP سرور شروع کریں:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. ایپلیکیشن لانچ کریں:
   ```bash
   chainlit run app.py -w
   ```

3. انضمام کی جانچ کریں:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## مسائل کا حل

عام مسائل اور ان کے حل:
1. MCP کنکشن کے مسائل  
   - تصدیق کریں کہ سرور چل رہا ہے  
   - پورٹ کی دستیابی چیک کریں  
   - GitHub ٹوکنز کی تصدیق کریں  

2. Azure Search کے مسائل  
   - کنکشن اسٹرنگز کی تصدیق کریں  
   - انڈیکس کی موجودگی چیک کریں  
   - دستاویز اپلوڈ کی تصدیق کریں  

## اگلے اقدامات
- اضافی MCP ٹولز کو دریافت کریں  
- کسٹم ایجنٹس کو نافذ کریں  
- RAG صلاحیتوں کو بہتر بنائیں  
- مزید ایونٹ ذرائع شامل کریں  
- **ایڈوانسڈ**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) میں ایجنٹ سے ایجنٹ مواصلات کی مثالیں دیکھیں  

## وسائل
- [MCP کے لیے ابتدائی رہنما](https://aka.ms/mcp-for-beginners)  
- [MCP دستاویزات](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)  

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔