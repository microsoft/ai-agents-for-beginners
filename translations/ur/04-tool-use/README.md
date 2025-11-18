<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T16:42:28+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "ur"
}
-->
[![اچھے AI ایجنٹس کو ڈیزائن کرنے کا طریقہ](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.ur.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(اوپر دی گئی تصویر پر کلک کریں تاکہ اس سبق کی ویڈیو دیکھ سکیں)_

# ٹول استعمال کرنے کا ڈیزائن پیٹرن

ٹولز دلچسپ ہیں کیونکہ یہ AI ایجنٹس کو زیادہ وسیع صلاحیتیں فراہم کرتے ہیں۔ ایجنٹ کے محدود اعمال کے بجائے، ٹول شامل کرنے سے ایجنٹ اب مختلف قسم کے اعمال انجام دے سکتا ہے۔ اس باب میں، ہم ٹول استعمال کرنے کے ڈیزائن پیٹرن پر نظر ڈالیں گے، جو بیان کرتا ہے کہ AI ایجنٹس مخصوص ٹولز کو اپنے مقاصد حاصل کرنے کے لیے کیسے استعمال کر سکتے ہیں۔

## تعارف

اس سبق میں، ہم درج ذیل سوالات کے جوابات تلاش کریں گے:

- ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟
- یہ کن استعمال کے معاملات پر لاگو ہو سکتا ہے؟
- اس ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بنیادی اجزاء درکار ہیں؟
- قابل اعتماد AI ایجنٹس بنانے کے لیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کے استعمال کے لیے کون سے خاص پہلوؤں پر غور کرنا چاہیے؟

## سیکھنے کے مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ قابل ہوں گے:

- ٹول استعمال کرنے کے ڈیزائن پیٹرن اور اس کے مقصد کی وضاحت کریں۔
- ان استعمال کے معاملات کی شناخت کریں جہاں ٹول استعمال کرنے کا ڈیزائن پیٹرن قابل اطلاق ہے۔
- ڈیزائن پیٹرن کو نافذ کرنے کے لیے درکار کلیدی عناصر کو سمجھیں۔
- اس ڈیزائن پیٹرن کا استعمال کرتے ہوئے AI ایجنٹس میں اعتماد کو یقینی بنانے کے لیے غور و فکر کو پہچانیں۔

## ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟

**ٹول استعمال کرنے کا ڈیزائن پیٹرن** LLMs کو بیرونی ٹولز کے ساتھ تعامل کرنے کی صلاحیت دینے پر مرکوز ہے تاکہ مخصوص مقاصد حاصل کیے جا سکیں۔ ٹولز وہ کوڈ ہیں جو ایجنٹ کے ذریعے اعمال انجام دینے کے لیے چلائے جا سکتے ہیں۔ ایک ٹول ایک سادہ فنکشن ہو سکتا ہے جیسے کیلکولیٹر، یا کسی تیسرے فریق کی سروس جیسے اسٹاک کی قیمت یا موسم کی پیش گوئی کے لیے API کال۔ AI ایجنٹس کے تناظر میں، ٹولز کو ایجنٹس کے ذریعے **ماڈل سے پیدا شدہ فنکشن کالز** کے جواب میں چلانے کے لیے ڈیزائن کیا گیا ہے۔

## یہ کن استعمال کے معاملات پر لاگو ہو سکتا ہے؟

AI ایجنٹس ٹولز کا فائدہ اٹھا کر پیچیدہ کام مکمل کر سکتے ہیں، معلومات حاصل کر سکتے ہیں، یا فیصلے کر سکتے ہیں۔ ٹول استعمال کرنے کا ڈیزائن پیٹرن اکثر ایسے منظرناموں میں استعمال ہوتا ہے جن میں بیرونی نظاموں جیسے ڈیٹا بیس، ویب سروسز، یا کوڈ انٹرپریٹرز کے ساتھ متحرک تعامل کی ضرورت ہوتی ہے۔ یہ صلاحیت مختلف استعمال کے معاملات کے لیے مفید ہے، جن میں شامل ہیں:

- **متحرک معلومات کی بازیافت:** ایجنٹس بیرونی APIs یا ڈیٹا بیس کو استفسار کر کے تازہ ترین ڈیٹا حاصل کر سکتے ہیں (جیسے SQLite ڈیٹا بیس سے ڈیٹا تجزیہ کے لیے استفسار کرنا، اسٹاک کی قیمتیں یا موسم کی معلومات حاصل کرنا)۔
- **کوڈ کا نفاذ اور تشریح:** ایجنٹس کوڈ یا اسکرپٹس چلا سکتے ہیں تاکہ ریاضی کے مسائل حل کریں، رپورٹس تیار کریں، یا سیمولیشنز انجام دیں۔
- **ورک فلو آٹومیشن:** ٹاسک شیڈولرز، ای میل سروسز، یا ڈیٹا پائپ لائنز جیسے ٹولز کو مربوط کر کے بار بار یا کثیر مرحلہ ورک فلو کو خودکار بنانا۔
- **کسٹمر سپورٹ:** ایجنٹس CRM سسٹمز، ٹکٹنگ پلیٹ فارمز، یا نالج بیسز کے ساتھ تعامل کر کے صارف کے سوالات حل کر سکتے ہیں۔
- **مواد کی تخلیق اور تدوین:** ایجنٹس گرامر چیکرز، ٹیکسٹ سمریزرز، یا مواد کی حفاظت کے جائزہ لینے والے ٹولز کا فائدہ اٹھا کر مواد تخلیق کرنے کے کاموں میں مدد کر سکتے ہیں۔

## ٹول استعمال کرنے کے ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بنیادی اجزاء درکار ہیں؟

یہ بنیادی اجزاء AI ایجنٹ کو مختلف قسم کے کام انجام دینے کی اجازت دیتے ہیں۔ آئیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کو نافذ کرنے کے لیے درکار کلیدی عناصر پر نظر ڈالیں:

- **فنکشن/ٹول اسکیمز:** دستیاب ٹولز کی تفصیلی تعریفیں، جن میں فنکشن کا نام، مقصد، مطلوبہ پیرامیٹرز، اور متوقع آؤٹ پٹس شامل ہیں۔ یہ اسکیمز LLM کو یہ سمجھنے کے قابل بناتی ہیں کہ کون سے ٹولز دستیاب ہیں اور درست درخواستیں کیسے بنائی جائیں۔
- **فنکشن نفاذ منطق:** صارف کے ارادے اور گفتگو کے سیاق و سباق کی بنیاد پر ٹولز کو کب اور کیسے استعمال کیا جائے اس پر حکمرانی کرتا ہے۔ اس میں پلانر ماڈیولز، روٹنگ میکانزم، یا مشروط فلو شامل ہو سکتے ہیں جو متحرک طور پر ٹول کے استعمال کا تعین کرتے ہیں۔
- **پیغام ہینڈلنگ سسٹم:** وہ اجزاء جو صارف کے ان پٹ، LLM کے جوابات، ٹول کالز، اور ٹول آؤٹ پٹس کے درمیان گفتگو کے بہاؤ کو منظم کرتے ہیں۔
- **ٹول انٹیگریشن فریم ورک:** وہ انفراسٹرکچر جو ایجنٹ کو مختلف ٹولز سے جوڑتا ہے، چاہے وہ سادہ فنکشنز ہوں یا پیچیدہ بیرونی خدمات۔
- **غلطی سے نمٹنے اور توثیق:** ٹول کے نفاذ میں ناکامیوں کو سنبھالنے، پیرامیٹرز کی توثیق کرنے، اور غیر متوقع جوابات کا انتظام کرنے کے طریقہ کار۔
- **اسٹیٹ مینجمنٹ:** گفتگو کے سیاق و سباق، پچھلے ٹول تعاملات، اور مستقل ڈیٹا کو ٹریک کرتا ہے تاکہ کثیر موڑ تعاملات میں مستقل مزاجی کو یقینی بنایا جا سکے۔

اب، آئیے فنکشن/ٹول کالنگ کو مزید تفصیل سے دیکھتے ہیں۔

### فنکشن/ٹول کالنگ

فنکشن کالنگ وہ بنیادی طریقہ ہے جس کے ذریعے ہم بڑے زبان کے ماڈلز (LLMs) کو ٹولز کے ساتھ تعامل کرنے کے قابل بناتے ہیں۔ آپ اکثر 'فنکشن' اور 'ٹول' کو ایک دوسرے کے ساتھ استعمال ہوتے دیکھیں گے کیونکہ 'فنکشنز' (دوبارہ استعمال کے قابل کوڈ کے بلاکس) وہ 'ٹولز' ہیں جنہیں ایجنٹس کام انجام دینے کے لیے استعمال کرتے ہیں۔ کسی فنکشن کے کوڈ کو چلانے کے لیے، LLM کو صارف کی درخواست کو فنکشن کی تفصیل کے خلاف موازنہ کرنا ہوگا۔ ایسا کرنے کے لیے، تمام دستیاب فنکشنز کی تفصیلات پر مشتمل ایک اسکیم LLM کو بھیجی جاتی ہے۔ پھر LLM کام کے لیے سب سے مناسب فنکشن کا انتخاب کرتا ہے اور اس کا نام اور دلائل واپس کرتا ہے۔ منتخب کردہ فنکشن کو چلایا جاتا ہے، اس کا جواب LLM کو واپس بھیجا جاتا ہے، جو صارف کی درخواست کا جواب دینے کے لیے معلومات کا استعمال کرتا ہے۔

ایجنٹس کے لیے فنکشن کالنگ کو نافذ کرنے کے لیے، ڈویلپرز کو درج ذیل کی ضرورت ہوگی:

1. ایک LLM ماڈل جو فنکشن کالنگ کو سپورٹ کرتا ہو
2. فنکشن کی تفصیلات پر مشتمل ایک اسکیم
3. ہر بیان کردہ فنکشن کے لیے کوڈ

آئیے ایک مثال کے ذریعے وضاحت کریں کہ کسی شہر میں موجودہ وقت حاصل کرنے کے لیے یہ کیسے کام کرتا ہے:

1. **فنکشن کالنگ کو سپورٹ کرنے والے LLM کو شروع کریں:**

    تمام ماڈلز فنکشن کالنگ کو سپورٹ نہیں کرتے، اس لیے یہ چیک کرنا ضروری ہے کہ آپ جو LLM استعمال کر رہے ہیں وہ کرتا ہے۔ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> فنکشن کالنگ کو سپورٹ کرتا ہے۔ ہم Azure OpenAI کلائنٹ کو شروع کر کے آغاز کر سکتے ہیں۔

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **فنکشن اسکیم بنائیں:**

    اگلا، ہم ایک JSON اسکیم کی وضاحت کریں گے جس میں فنکشن کا نام، فنکشن کیا کرتا ہے اس کی وضاحت، اور فنکشن پیرامیٹرز کے نام اور وضاحتیں شامل ہوں گی۔
    پھر ہم اس اسکیم کو پہلے سے بنائے گئے کلائنٹ کو صارف کی درخواست کے ساتھ پاس کریں گے تاکہ سان فرانسسکو میں وقت معلوم کیا جا سکے۔ اہم بات یہ ہے کہ جو **ٹول کال** واپس آتی ہے، وہ سوال کا حتمی جواب **نہیں** ہوتا۔ جیسا کہ پہلے ذکر کیا گیا ہے، LLM اس فنکشن کا نام واپس کرتا ہے جو اس نے کام کے لیے منتخب کیا ہے، اور وہ دلائل جو اسے پاس کیے جائیں گے۔

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **کام انجام دینے کے لیے مطلوبہ فنکشن کوڈ:**

    اب جب کہ LLM نے منتخب کر لیا ہے کہ کون سا فنکشن چلایا جانا چاہیے، کام انجام دینے کے لیے کوڈ کو نافذ اور چلانے کی ضرورت ہے۔
    ہم Python میں موجودہ وقت حاصل کرنے کے لیے کوڈ نافذ کر سکتے ہیں۔ ہمیں response_message سے نام اور دلائل نکالنے کے لیے کوڈ بھی لکھنا ہوگا تاکہ حتمی نتیجہ حاصل کیا جا سکے۔

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

فنکشن کالنگ زیادہ تر، اگر تمام نہیں، ایجنٹ ٹول استعمال کے ڈیزائن کے مرکز میں ہے، تاہم اسے شروع سے نافذ کرنا بعض اوقات چیلنجنگ ہو سکتا ہے۔
جیسا کہ ہم نے [سبق 2](../../../02-explore-agentic-frameworks) میں سیکھا، ایجنٹک فریم ورک ہمیں ٹول استعمال کو نافذ کرنے کے لیے پہلے سے بنے ہوئے بنیادی اجزاء فراہم کرتے ہیں۔

## ایجنٹک فریم ورک کے ساتھ ٹول استعمال کی مثالیں

یہاں کچھ مثالیں ہیں کہ آپ مختلف ایجنٹک فریم ورک کا استعمال کرتے ہوئے ٹول استعمال کرنے کے ڈیزائن پیٹرن کو کیسے نافذ کر سکتے ہیں:

### سیمینٹک کرنل

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">سیمینٹک کرنل</a> .NET، Python، اور Java ڈویلپرز کے لیے ایک اوپن سورس AI فریم ورک ہے جو بڑے زبان کے ماڈلز (LLMs) کے ساتھ کام کرتے ہیں۔ یہ فنکشن کالنگ کے استعمال کے عمل کو آسان بناتا ہے کیونکہ یہ آپ کے فنکشنز اور ان کے پیرامیٹرز کو ماڈل کے لیے خود بخود بیان کرتا ہے، جسے <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">سیریلائزنگ</a> کہا جاتا ہے۔ یہ ماڈل اور آپ کے کوڈ کے درمیان بات چیت کو بھی سنبھالتا ہے۔ ایجنٹک فریم ورک جیسے سیمینٹک کرنل کا ایک اور فائدہ یہ ہے کہ یہ آپ کو پہلے سے بنے ہوئے ٹولز تک رسائی فراہم کرتا ہے جیسے <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">فائل سرچ</a> اور <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">کوڈ انٹرپریٹر</a>۔

مندرجہ ذیل خاکہ سیمینٹک کرنل کے ساتھ فنکشن کالنگ کے عمل کو ظاہر کرتا ہے:

![فنکشن کالنگ](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.ur.png)

سیمینٹک کرنل میں فنکشنز/ٹولز کو <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">پلگ انز</a> کہا جاتا ہے۔ ہم پہلے دیکھے گئے `get_current_time` فنکشن کو ایک کلاس میں تبدیل کر کے پلگ ان میں تبدیل کر سکتے ہیں جس میں فنکشن موجود ہو۔ ہم `kernel_function` ڈیکوریٹر کو بھی درآمد کر سکتے ہیں، جو فنکشن کی وضاحت لیتا ہے۔ جب آپ پھر GetCurrentTimePlugin کے ساتھ ایک کرنل بناتے ہیں، تو کرنل خود بخود فنکشن اور اس کے پیرامیٹرز کو سیریلائز کر دے گا، اس عمل میں LLM کو بھیجنے کے لیے اسکیم بنائے گا۔

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI ایجنٹ سروس

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI ایجنٹ سروس</a> ایک نیا ایجنٹک فریم ورک ہے جو ڈویلپرز کو اعلیٰ معیار کے، اور قابل توسیع AI ایجنٹس کو محفوظ طریقے سے بنانے، تعینات کرنے، اور پیمانے پر لانے کے لیے ڈیزائن کیا گیا ہے، بغیر بنیادی کمپیوٹ اور اسٹوریج وسائل کا انتظام کرنے کی ضرورت کے۔ یہ خاص طور پر انٹرپرائز ایپلیکیشنز کے لیے مفید ہے کیونکہ یہ ایک مکمل طور پر منظم سروس ہے جس میں انٹرپرائز گریڈ سیکیورٹی ہے۔

LLM API کے ساتھ براہ راست ترقی کرنے کے مقابلے میں، Azure AI ایجنٹ سروس کچھ فوائد فراہم کرتی ہے، جن میں شامل ہیں:

- خودکار ٹول کالنگ – ٹول کال کو پارس کرنے، ٹول کو چلانے، اور جواب کو سنبھالنے کی ضرورت نہیں؛ یہ سب اب سرور سائیڈ پر کیا جاتا ہے۔
- محفوظ طریقے سے منظم ڈیٹا – اپنی گفتگو کی حالت کا انتظام کرنے کے بجائے، آپ تھریڈز پر انحصار کر سکتے ہیں تاکہ آپ کو اپنی ضرورت کی تمام معلومات ذخیرہ کی جا سکیں۔
- پہلے سے بنے ہوئے ٹولز – ایسے ٹولز جنہیں آپ اپنے ڈیٹا سورسز کے ساتھ تعامل کرنے کے لیے استعمال کر سکتے ہیں، جیسے Bing، Azure AI سرچ، اور Azure فنکشنز۔

Azure AI ایجنٹ سروس میں دستیاب ٹولز کو دو اقسام میں تقسیم کیا جا سکتا ہے:

1. نالج ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing سرچ کے ساتھ گراؤنڈنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">فائل سرچ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI سرچ</a>

2. ایکشن ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">فنکشن کالنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">کوڈ انٹرپریٹر</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI سے متعین ٹولز</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure فنکشنز</a>

ایجنٹ سروس ہمیں ان ٹولز کو `toolset` کے طور پر ایک ساتھ استعمال کرنے کی اجازت دیتی ہے۔ یہ `threads` کا بھی استعمال کرتی ہے جو کسی خاص گفتگو سے پیغامات کی تاریخ کو ٹریک کرتے ہیں۔

تصور کریں کہ آپ Contoso نامی کمپنی میں ایک سیلز ایجنٹ ہیں۔ آپ ایک گفتگو ایجنٹ تیار کرنا چاہتے ہیں جو آپ کے سیلز ڈیٹا کے بارے میں سوالات کے جوابات دے سکے۔

مندرجہ ذیل تصویر ظاہر کرتی ہے کہ آپ اپنے سیلز ڈیٹا کا تجزیہ کرنے کے لیے Azure AI ایجنٹ سروس کو کیسے استعمال کر سکتے ہیں:

![ایجنٹک سروس ایکشن میں](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.ur.jpg)

ان ٹولز کو سروس کے ساتھ استعمال کرنے کے لیے ہم ایک کلائنٹ بنا سکتے ہیں اور ایک ٹول یا ٹول سیٹ کی وضاحت کر سکتے ہیں۔ اسے عملی طور پر نافذ کرنے کے لیے ہم درج ذیل Python کوڈ استعمال کر سکتے ہیں۔ LLM ٹول سیٹ کو دیکھ سکے گا اور صارف کے بنائے گئے فنکشن، `fetch_sales_data_using_sqlite_query`، یا پہلے سے بنے ہوئے کوڈ انٹرپریٹر کو صارف کی درخواست کے مطابق استعمال کرنے کا فیصلہ کرے گا۔

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## قابل اعتماد AI ایجنٹس بنانے کے لیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کے استعمال کے لیے کون سے خاص پہلوؤں پر غور کرنا چاہیے؟

LLMs کے ذریعے متحرک طور پر تیار کردہ SQL کے ساتھ ایک عام تشویش سیکیورٹی ہے، خاص طور پر SQL انجیکشن یا نقصان دہ اعمال کا خطرہ، جیسے ڈیٹا بیس کو حذف کرنا یا چھیڑ چھاڑ کرنا۔ اگرچہ
ایپ کو محفوظ ماحول میں چلانا تحفظ کو مزید بہتر بناتا ہے۔ کاروباری منظرناموں میں، ڈیٹا عام طور پر آپریشنل سسٹمز سے نکالا اور تبدیل کیا جاتا ہے تاکہ اسے ایک ریڈ-اونلی ڈیٹا بیس یا ڈیٹا ویئرہاؤس میں منتقل کیا جا سکے، جس میں صارف دوست اسکیمہ ہوتا ہے۔ یہ طریقہ یقینی بناتا ہے کہ ڈیٹا محفوظ ہے، کارکردگی اور رسائی کے لیے بہتر بنایا گیا ہے، اور ایپ کو محدود، ریڈ-اونلی رسائی حاصل ہے۔

## نمونہ کوڈز

- Python: [ایجنٹ فریم ورک](./code_samples/04-python-agent-framework.ipynb)
- .NET: [ایجنٹ فریم ورک](./code_samples/04-dotnet-agent-framework.md)

## ٹول استعمال کے ڈیزائن پیٹرنز کے بارے میں مزید سوالات ہیں؟

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں تاکہ دوسرے سیکھنے والوں سے ملاقات کریں، آفس آورز میں شرکت کریں اور اپنے AI ایجنٹس کے سوالات کے جوابات حاصل کریں۔

## اضافی وسائل

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI ایجنٹس سروس ورکشاپ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer ملٹی ایجنٹ ورکشاپ</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel فنکشن کالنگ ٹیوٹوریل</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel کوڈ انٹرپریٹر</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen ٹولز</a>

## پچھلا سبق

[ایجنٹک ڈیزائن پیٹرنز کو سمجھنا](../03-agentic-design-patterns/README.md)

## اگلا سبق

[ایجنٹک RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلانِ لاتعلقی**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->