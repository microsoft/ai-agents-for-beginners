# Github MCP سرور کی مثال

## تفصیل

یہ ایک ڈیمو تھا جو Microsoft Reactor کے ذریعے منعقد کردہ AI Agents Hackathon کے لیے تیار کیا گیا تھا۔

یہ ٹولز استعمال کرنے والے کے Github ریپوز کی بنیاد پر ہیکاتھون پروجیکٹس کی سفارش کرنے کے لیے استعمال ہوتے ہیں۔
یہ مندرجہ ذیل طریقے سے کیا جاتا ہے:

1. **Github ایجنٹ** - Github MCP سرور کا استعمال کرتے ہوئے ریپوز اور ان ریپوز کے بارے میں معلومات حاصل کرنا۔
2. **ہیکاتھون ایجنٹ** - Github ایجنٹ سے ڈیٹا لے کر تخلیقی ہیکاتھون پروجیکٹ آئیڈیاز پیش کرتا ہے جو یوزر کے پروجیکٹس، استعمال شدہ زبانوں اور AI Agents ہیکاتھون کے پروجیکٹ ٹریکس پر مبنی ہوتے ہیں۔
3. **ایونٹس ایجنٹ** - ہیکاتھون ایجنٹس کی تجاویز کی بنیاد پر، ایونٹس ایجنٹ AI Agent Hackathon سیریز کے متعلقہ ایونٹس کی سفارش کرے گا۔

## کوڈ چلانا

### ماحول کے متغیرات

یہ ڈیمو Microsoft Agent Framework، Azure OpenAI Service، Github MCP سرور اور Azure AI Search استعمال کرتا ہے۔

یقینی بنائیں کہ آپ نے ان ٹولز کو استعمال کرنے کے لیے مناسب ماحول کے متغیرات سیٹ کیے ہوئے ہیں:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Chainlit سرور چلانا

MCP سرور سے جڑنے کے لیے، یہ ڈیمو بات چیت کے لیے Chainlit استعمال کرتا ہے۔

سرور چلانے کے لیے، اپنے ٹرمینل میں درج ذیل کمانڈ استعمال کریں:

```bash
chainlit run app.py -w
```


اس سے آپ کا Chainlit سرور `localhost:8000` پر شروع ہو جائے گا اور آپ کے Azure AI Search انڈیکس کو `event-descriptions.md` کے مواد سے بھر دے گا۔

## MCP سرور سے کنیکٹ ہونا

Github MCP سرور سے جڑنے کے لیے، "Type your message here.." چیٹ باکس کے نیچے "plug" آئیکن منتخب کریں:

![MCP Connect](../../../../../translated_images/ur/mcp-chainlit-1.7ed66d648e3cfb28.webp)

وہاں سے آپ "Connect an MCP" پر کلک کر کے Github MCP سرور سے کنیکشن کا کمانڈ شامل کر سکتے ہیں:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


"[YOUR PERSONAL ACCESS TOKEN]" کو اپنے اصل Personal Access Token سے بدل دیں۔

کنیکٹ ہونے کے بعد plug آئیکن کے ساتھ (1) نظر آئے گا جو تصدیق کرے گا کہ کنیکشن ہو چکا ہے۔ اگر نہیں، تو `chainlit run app.py -w` کے ساتھ چینلٹ سرور دوبارہ شروع کرنے کی کوشش کریں۔

## ڈیمو استعمال کرنا

ہیکاتھون پروجیکٹس کی سفارش کے لیے ایجنٹ ورک فلو شروع کرنے کے لیے، آپ درج ذیل پیغام لکھ سکتے ہیں:

"Recommend hackathon projects for the Github user koreyspace"

روٹر ایجنٹ آپ کی درخواست کا تجزیہ کرے گا اور طے کرے گا کہ کون سے ایجنٹس (GitHub, Hackathon, اور Events) کا مجموعہ آپ کی درخواست کو بہتر طریقے سے سنبھال سکتا ہے۔ ایجنٹس مل کر Github ریپوزٹری کے تجزیہ، پروجیکٹ آئیڈیاز، اور متعلقہ تکنیکی ایونٹس کی بنیاد پر جامع سفارشات فراہم کرتے ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈسکلیمیر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لئے کوشاں ہیں، براہِ کرم نوٹ کریں کہ خودکار ترجمے میں غلطیاں یا ناکاملیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مقامی زبان میں ہی مستند ذریعہ سمجھی جائے گی۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->