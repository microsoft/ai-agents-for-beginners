# Github MCP سرور کی مثال

## تفصیل

یہ ایک مظاہرہ تھا جو Microsoft Reactor کے ذریعے منعقدہ AI Agents Hackathon کے لیے تیار کیا گیا تھا۔

یہ اوزار صارف کے Github ریپوز کی بنیاد پر ہیکاتھون پروجیکٹس کی سفارش کرنے کے لیے استعمال ہوتا ہے۔
یہ اس طرح کیا جاتا ہے:

1. **Github Agent** - Github MCP سرور کا استعمال کرتے ہوئے ریپوز اور ان ریپوز کے بارے میں معلومات حاصل کرنا۔
2. **Hackathon Agent** - Github Agent سے حاصل شدہ ڈیٹا لیتا ہے اور صارف کے استعمال کئے گئے پروجیکٹس، زبانوں اور AI Agents ہیکاتھون کے پروجیکٹ ٹریکس کی بنیاد پر تخلیقی ہیکاتھون پروجیکٹ آئیڈیاز تیار کرتا ہے۔
3. **Events Agent** - ہیکاتھون ایجنٹس کی تجاویز کی بنیاد پر، ایونٹس ایجنٹ AI Agent Hackathon سیریز کے متعلقہ واقعات کی سفارش کرے گا۔

## کوڈ چلانا

### ماحول کے متغیرات

یہ مظاہرہ Microsoft Agent Framework، Azure OpenAI Service، Github MCP Server اور Azure AI Search استعمال کرتا ہے۔

ان اوزاروں کو استعمال کرنے کے لیے یقینی بنائیں کہ آپ نے مناسب ماحولیاتی متغیرات سیٹ کر رکھے ہیں:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Chainlit سرور چلانا

MCP سرور سے جڑنے کے لیے، یہ مظاہرہ چیٹ انٹرفیس کے طور پر Chainlit استعمال کرتا ہے۔

سرور چلانے کے لیے، اپنے ٹرمینل میں درج ذیل کمانڈ استعمال کریں:

```bash
chainlit run app.py -w
```


یہ آپ کے Chainlit سرور کو `localhost:8000` پر شروع کرے گا اور آپ کے Azure AI Search انڈیکس کو `event-descriptions.md` مواد سے بھر دے گا۔

## MCP سرور سے رابطہ

Github MCP سرور سے جڑنے کے لیے، "Type your message here.." چیٹ باکس کے نیچے "پلگ" آئیکن منتخب کریں:

![MCP Connect](../../../../../translated_images/ur/mcp-chainlit-1.7ed66d648e3cfb28.webp)

وہاں سے آپ "Connect an MCP" پر کلک کر کے Github MCP سرور سے جڑنے کا کمانڈ شامل کر سکتے ہیں:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


"[YOUR PERSONAL ACCESS TOKEN]" کو اپنے اصل پرسنل ایکسیس ٹوکن سے بدلیں۔

کنیکٹ کرنے کے بعد، آپ کو پلگ آئیکن کے ساتھ (1) دکھائی دے گا تاکہ اس بات کی تصدیق ہو جائے کہ کنیکٹڈ ہے۔ اگر نہیں، تو `chainlit run app.py -w` کے ساتھ chainlit سرور کو دوبارہ شروع کرنے کی کوشش کریں۔

## مظاہرہ استعمال کرنا

ہیکاتھون پروجیکٹس کی سفارش کرنے والے ایجنٹ کے ورک فلو کو شروع کرنے کے لیے، آپ ایک پیغام لکھ سکتے ہیں، مثلاً:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent آپ کی درخواست کا تجزیہ کرے گا اور فیصلہ کرے گا کہ کون سے ایجنٹس (GitHub، Hackathon، اور Events) کے مجموعے آپ کی درخواست سنبھالنے کے لیے بہترین ہیں۔ ایجنٹس مل کر Github ریپوز کے تجزیے، پروجیکٹ آئیڈییشن، اور متعلقہ ٹیک ایونٹس کی بنیاد پر مکمل سفارشات فراہم کرتے ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ خدمات [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم یاد رکھیں کہ خودکار ترجمے میں غلطیاں یا کمیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی قابل اعتبار ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی تجویز دی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا بدفہمی کی ذمہ داری ہم پر عائد نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->