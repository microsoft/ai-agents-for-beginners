# ایجنٹ سموک ٹیسٹ  

اس فولڈر میں آپ کے کورس میں بنائے گئے ایجنٹس کے لیے **سموک-ٹیسٹ کیٹلاگ** محفوظ کیے گئے ہیں۔  
سموک ٹیسٹ ایک سستا اور تیز چیک ہوتا ہے جو یہ یقینی بناتا ہے کہ **تعینات شدہ Microsoft Foundry میزبان ایجنٹ**  
قابل رسائی ہے، جواب دے رہا ہے، اور اس کے سب سے بنیادی پرامپٹ توقعات کی پابندی کر رہا ہے۔  
یہ ایک ابتدائی قدم ہے — مکمل تشخیص کی جگہ نہیں جو آپ [سبق 10](../10-ai-agents-production/README.md) اور  
[سبق 16](../16-deploying-scalable-agents/README.md) میں سیکھتے ہیں۔  
 

یہ کیٹلاگ [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)  
گٹ ہب ایکشن کے ذریعے [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)  
ورک فلو کے ذریعہ استعمال ہوتے ہیں۔  

## چلانے کا طریقہ  

1. سبق کا ایجنٹ Microsoft Foundry پر بطور میزبان ایجنٹ تعینات کریں (تعیناتی کا ورک فلو دیکھنے کے لیے  
   سبق 16 ملاحظہ کریں)۔ **ایجنٹ کا نام** اور آپ کا **Foundry پروجیکٹ اینڈ پوائنٹ** نوٹ کریں۔  
2. ریپوزیٹری سِیکرٹس (Settings → Secrets and variables → Actions) میں یہ شامل کریں:  
   `AZURE_CLIENT_ID`، `AZURE_TENANT_ID`، `AZURE_SUBSCRIPTION_ID`۔ فریڈیٹڈ شناخت کو **Azure AI User** رول  
   چاہیے ہوتا ہے جو **Foundry پروجیکٹ دائرہ اختیار** میں ہو۔  
3. **Actions** ٹیب سے، **Smoke-test hosted agents** چلائیں اور سبق کے لیے مناسب  
   `tests_file` منتخب کریں، پھر مماثل `agent_name` اور `project_endpoint` فراہم کریں۔  
 
## کیٹلاگ → سبق → ایجنٹ کا نام  

| کیٹلاگ | سبق | بحیثیت ایجنٹ تعینات کریں |  

| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – تعارف برائے AI ایجنٹس](../01-intro-to-ai-agents/README.md) | `TravelAgent` |  
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – ٹول کا استعمال](../04-tool-use/README.md) | `TravelToolAgent` |  
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – ایجنٹک RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |  
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – اسکیل ایبل ایجنٹس کی تعیناتی](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |  
 
## کون سے اسباق میں سموک ٹیسٹ ہوتے ہیں؟  

سموک ٹیسٹ ان اسباق پر لاگو ہوتے ہیں جہاں آپ **ایجنٹ تعینات کرتے ہیں** جس کے متنی جوابات کو معلوم شدہ مواد سے جانچا جا سکتا ہے۔  

 
- **سبق 17 (مقامی AI ایجنٹس کی تخلیق)** مکمل طور پر آپ کے ورک سٹیشن پر  
  Foundry Local کے ساتھ چلتا ہے اور کوئی Foundry Responses اینڈ پوائنٹ مہیا نہیں کرتا، اس لیے یہ  

- ڈیزائن پیٹرن اور نظریاتی اسباق (02، 03، 06، 07، 09، 12) ایک بھی تعیناتی کے قابل ایجنٹ  
  سموک-ٹیسٹ کے لیے فراہم نہیں کرتے۔  
 
## کیٹلاگ اسکیمہ (مختصر حوالہ)  
 

## کیٹلاگ اسکیمہ (تیز حوالہ)

ہر کیٹلاگ ایک JSON دستاویز ہے جس میں ایک ٹاپ لیول `tests` صف ہوتی ہے۔ ہر اندراج ایک پرامپٹ پوسٹ کرتا ہے اور جواب پر دعویٰ کرتا ہے:


| فیلڈ | مطلب |
|-------|---------|
| `id` | منفرد مرحلے کی شناخت جو لاگ میں چھاپی جاتی ہے۔ |
| `description` | انسانی پڑھنے کے قابل مقصد۔ |
| `prompt` | ایجنٹ کو بھیجا گیا پیغام۔ |
| `assertions.status` | متوقع HTTP اسٹیٹس (ڈیفالٹ 200)۔ |
| `assertions.contains_any` | پاس ہو اگر جواب میں ان میں سے کوئی ذیلی سٹرنگ ہو۔ |
| `assertions.contains_all` | پاس ہو اگر جواب میں ہر ذیلی سٹرنگ موجود ہو۔ |
| `assertions.contains_none` | پاس ہو اگر جواب میں ان میں سے کوئی بھی ذیلی سٹرنگ موجود نہ ہو۔ |
| `save_response_id_as` | بعد کے ملٹی ٹرن مرحلے کے لیے جواب کا آئی ڈی محفوظ کریں۔ |
| `use_previous_response_id` | اس ٹرن کو محفوظ شدہ جواب کے آئی ڈی کے ساتھ جوڑ کر بھیجیں۔ |

دعوے (assertions) کیس ان حساس ذیلی سٹرنگ چیکس ہیں۔ مکمل سکیمہ کے لیے،
[action documentation](https://github.com/marketplace/actions/ai-smoke-test) دیکھیں،
جس میں Foundry کے زیر انتظام گفتگو کے وسائل شامل ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->