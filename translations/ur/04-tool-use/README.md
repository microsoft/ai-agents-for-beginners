[![اچھے AI ایجنٹس کیسے ڈیزائن کریں](../../../translated_images/ur/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(اس سبق کی ویڈیو دیکھنے کے لیے اوپر تصویر پر کلک کریں)_

# ٹول استعمال کرنے کا ڈیزائن پیٹرن

ٹولز دلچسپ ہیں کیونکہ یہ AI ایجنٹس کو وسیع تر صلاحیتوں کا امتزاج فراہم کرتے ہیں۔ ایجنٹ کے پاس محدود قسم کے اعمال کرنے کی بجائے، ٹول شامل کر کے ایجنٹ اب بہت سے قسم کے اعمال انجام دے سکتا ہے۔ اس باب میں، ہم ٹول استعمال کرنے کے ڈیزائن پیٹرن کو دیکھیں گے، جو وضاحت کرتا ہے کہ AI ایجنٹس مخصوص ٹولز کا استعمال کیسے کر کے اپنے مقاصد حاصل کر سکتے ہیں۔

## تعارف

اس سبق میں، ہم درج ذیل سوالات کے جوابات تلاش کر رہے ہیں:

- ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟
- کن کیسز میں اس کا اطلاق کیا جا سکتا ہے؟
- ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بنیادی اجزاء درکار ہیں؟
- قابل اعتماد AI ایجنٹس بنانے کے لیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کے استعمال میں کیا خاص پہلو ہیں؟

## تعلیمی مقاصد

اس سبق مکمل کرنے کے بعد، آپ کر سکیں گے:

- ٹول استعمال کرنے کے ڈیزائن پیٹرن اور اس کے مقصد کی وضاحت کرنا۔
- ایسے استعمال کے کیسز کی شناخت کرنا جہاں یہ ڈیزائن پیٹرن لاگو ہو۔
- ڈیزائن پیٹرن نافذ کرنے کے لیے ضروری کلیدی عناصر کو سمجھنا۔
- اس ڈیزائن پیٹرن کے استعمال سے AI ایجنٹس کی اعتمادیت کو یقینی بنانے کے لیے غور و فکر کرنا۔

## ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟

**ٹول استعمال کرنے کا ڈیزائن پیٹرن** LLMs کو مخصوص مقاصد حاصل کرنے کے لیے خارجی ٹولز کے ساتھ تعامل کرنے کی صلاحیت دیتا ہے۔ ٹولز کوڈ ہوتے ہیں جنہیں ایجنٹ ایکشن کے لیے چلایا جا سکتا ہے۔ ایک ٹول ایک سادہ فنکشن ہو سکتا ہے، جیسے کیلکولیٹر، یا تیسرے فریق کی سروس کا API کال، جیسے اسٹاک قیمت معلوم کرنا یا موسم کی پیش گوئی۔ AI ایجنٹس کے تناظر میں، ٹولز ایسے بنائے جاتے ہیں کہ ایجنٹ ماڈل کی پیدا کردہ فنکشن کالز کے جواب میں انہیں چلاتے ہیں۔

## یہ کس قسم کے کیسز میں استعمال ہو سکتا ہے؟

AI ایجنٹس ٹولز کا استعمال کر کے پیچیدہ کام مکمل کر سکتے ہیں، معلومات حاصل کر سکتے ہیں، یا فیصلے کر سکتے ہیں۔ یہ ڈیزائن پیٹرن خاص طور پر ایسی صورتوں میں استعمال ہوتا ہے جہاں خارجی نظاموں، جیسے ڈیٹا بیس، ویب سروسز، یا کوڈ انٹرپریٹرز کے ساتھ متحرک تعامل ضروری ہو۔ یہ قابلیت کئی مختلف استعمالات کے لیے مفید ہے، جیسے:

- **متحرک معلومات کی بازیابی:** ایجنٹس خارجی APIs یا ڈیٹا بیس سے تازہ ترین ڈیٹا حاصل کر سکتے ہیں (مثلاً، SQLite ڈیٹا بیس سے ڈیٹا تجزیہ کے لیے استفسار کرنا، اسٹاک قیمت یا موسم کی معلومات حاصل کرنا)۔
- **کوڈ کا نفاذ اور تشریح:** ایجنٹس ریاضیاتی مسائل حل کرنے، رپورٹس بنانے، یا سمیولیشن کرنے کے لیے کوڈ یا اسکرپٹس چلا سکتے ہیں۔
- **ورک فلو کی خودکاری:** ایجنٹس ٹاسک شیڈولرز، ای میل سروسز، یا ڈیٹا پائپ لائنز جیسی ٹولز کو مربوط کر کے دہرانے والے یا کثیر مرحلہ ورک فلو خودکار بنا سکتے ہیں۔
- **کسٹمر سپورٹ:** ایجنٹس CRM نظاموں، ٹکٹنگ پلیٹ فارمز، یا نالج بیسز کے ساتھ تعامل کر کے یوزر کے سوالات کے جوابات دے سکتے ہیں۔
- **مواد کی تخلیق اور ترمیم:** ایجنٹس گرامر چیکرز، متن کے خلاصہ ساز، یا مواد کی حفاظت کے جائزہ لینے والے ٹولز کا استعمال کر کے مواد کی تخلیق میں مدد کر سکتے ہیں۔

## ٹول استعمال کرنے کے ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بنیادی اجزاء درکار ہیں؟

یہ بنیادی اجزاء AI ایجنٹ کو وسیع قسم کے کام کرنے کی اجازت دیتے ہیں۔ آئیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کو نافذ کرنے کے لیے ضروری کلیدی عناصر دیکھتے ہیں:

- **فنکشن/ٹول سکیمہ جات:** دستیاب ٹولز کی تفصیلی تعریفیں، جن میں فنکشن کا نام، مقصد، مطلوبہ پیرا میٹرز، اور متوقع نتائج شامل ہیں۔ یہ سکیمہ جات LLM کو یہ سمجھنے میں مدد دیتے ہیں کہ کون سے ٹولز دستیاب ہیں اور درست درخواستیں کیسے بنائی جائیں۔

- **فنکشن کے نفاذ کا منطق:** یہ اس بات کو کنٹرول کرتا ہے کہ صارف کی مراد اور گفتگو کے سیاق و سباق کی بنیاد پر ٹولز کب اور کیسے کال کیے جائیں۔ اس میں پلانر ماڈیولز، راستہ سازی کے طریقہ کار، یا مشروط بہاؤ شامل ہو سکتے ہیں جو ٹول کے استعمال کا فیصلہ متحرک طریقے سے کرتے ہیں۔

- **پیغام سنبھالنے کا نظام:** وہ اجزاء جو صارف کی ان پٹ، LLM کے جوابات، ٹول کالز، اور ٹول آؤٹ پٹس کے درمیان گفتگو کے بہاؤ کا انتظام کرتے ہیں۔

- **ٹول انٹیگریشن فریم ورک:** ایسا بنیادی ڈھانچہ جو ایجنٹ کو مختلف ٹولز سے منسلک کرتا ہے، چاہے وہ آسان فنکشنز ہوں یا پیچیدہ خارجی سروسز۔

- **خرابی سنبھالنا اور توثیق:** ایسے طریقے جو ٹول کے نفاذ میں ناکامیوں کو سنبھالتے ہیں، پیرا میٹرز کی تصدیق کرتے ہیں، اور غیر متوقع جوابات کا انتظام کرتے ہیں۔

- **حالت کا انتظام:** گفتگو کے سیاق و سباق، ماضی کے ٹول تعاملات، اور مستقل ڈیٹا کو ٹریک کرتا ہے تاکہ کثیر مرحلہ بات چیت میں مطابقت یقینی بنائی جا سکے۔

اب، آئیے فنکشن/ٹول کالنگ کو تفصیل سے دیکھتے ہیں۔

### فنکشن/ٹول کالنگ

فنکشن کالنگ وہ بنیادی طریقہ ہے جس کے ذریعے ہم LLMs کو ٹولز کے ساتھ تعامل کی اجازت دیتے ہیں۔ آپ اکثر 'فنکشن' اور 'ٹول' کو ایک دوسرے کے متبادل استعمال کرتے ہوئے دیکھیں گے کیونکہ 'فنکشنز' (دوبارہ قابل استعمال کوڈ کے بلاکس) وہ 'ٹولز' ہیں جن سے ایجنٹس کام سر انجام دیتے ہیں۔ کسی فنکشن کے کوڈ کو چلانے کے لیے، LLM کو صارف کی درخواست کو فنکشن کے بیان سے مقابلہ کرنا ہوتا ہے۔ اس کے لیے تمام دستیاب فنکشنز کی وضاحت پر مشتمل ایک سکیمہ LLM کو بھیجی جاتی ہے۔ LLM پھر ٹاسک کے لیے سب سے مناسب فنکشن منتخب کرتا ہے اور اس کا نام اور دلائل واپس کرتا ہے۔ منتخب شدہ فنکشن چلایا جاتا ہے، اس کا جواب LLM کو بھیجا جاتا ہے، جو معلومات کو صارف کی درخواست کا جواب دینے کے لیے استعمال کرتا ہے۔

ڈیولپرز کو فنکشن کالنگ نافذ کرنے کے لیے درج ذیل کی ضرورت ہوتی ہے:

1. ایک LLM ماڈل جو فنکشن کالنگ کی حمایت کرتا ہو
2. فنکشن وضاحتوں پر مشتمل سکیمہ
3. ہر فنکشن کا کوڈ جو بیان کیا گیا ہے

مثال کے طور پر کسی شہر میں موجودہ وقت حاصل کرنے کے لیے:

1. **فنکشن کالنگ کی حمایت کرنے والا LLM ماڈل شروع کریں:**

    تمام ماڈلز فنکشن کالنگ کی حمایت نہیں کرتے، اس لیے یہ چیک کرنا ضروری ہے کہ آپ کا LLM ایسا کرتا ہے یا نہیں۔ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> فنکشن کالنگ کی حمایت کرتا ہے۔ ہم Azure OpenAI کلائنٹ کو شروع کر کے شروع کر سکتے ہیں۔

    ```python
    # Azure OpenAI کلائنٹ کو شروع کریں
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **فنکشن سکیمہ بنائیں:**

    اگلا، ہم JSON سکیمہ تعریف کریں گے جس میں فنکشن کا نام، اس کا کیا کام ہے، اور فنکشن کے دلائل کے نام اور وضاحت شامل ہوں گے۔
    پھر ہم اس سکیمہ کو پہلے بنائے گئے کلائنٹ کو بھیجیں گے، ساتھ ہی صارف کی درخواست جو سان فرانسسکو میں وقت معلوم کرنے کے لیے ہوگی۔ اہم بات یہ ہے کہ جو لوٹا ہے وہ **ٹول کال** ہے، **سوال کا آخری جواب نہیں**۔ جیسا کہ پہلے کہا گیا، LLM فنکشن کا نام اور دلائل واپس کرتا ہے جنہیں اسے کال کیا جائے گا۔

    ```python
    # ماڈل کے لیے پڑھنے کے لیے فنکشن کی وضاحت
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
  
    # ابتدائی صارف کا پیغام
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # پہلی API کال: ماڈل سے کہیں کہ فنکشن استعمال کرے
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # ماڈل کے جواب کو پروسیس کریں
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **کام انجام دینے کے لیے ضروری فنکشن کوڈ:**

    اب جب LLM نے منتخب کر لیا ہے کہ کون سا فنکشن چلانا ہے تو کام کو انجام دینے کے لیے کوڈ کو نافذ کرنا اور چلانا ہوگا۔
    ہم Python میں موجودہ وقت حاصل کرنے کا کوڈ لکھ سکتے ہیں۔ ہمیں response_message سے نام اور دلائل نکالنے کا کوڈ بھی لکھنا ہوگا تاکہ حتمی نتیجہ مل سکے۔

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
     # فنکشن کالز کو سنبھالیں
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
  
      # دوسرا API کال: ماڈل سے آخری جواب حاصل کریں
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

فنکشن کالنگ زیادہ تر ایجنٹ ٹول استعمال کے ڈیزائن کا بنیادی حصہ ہے، پھر بھی اسے صفر سے نافذ کرنا کبھی کبھار چیلنجنگ ہو سکتا ہے۔
جیسا کہ ہم نے [سبق 2](../../../02-explore-agentic-frameworks) میں سیکھا، ایجنٹک فریم ورکس یہ بنیادی بلاکس پہلے سے تیار شدہ فراہم کرتے ہیں تاکہ ٹول استعمال کو نافذ کیا جا سکے۔

## ایجنٹک فریم ورکس کے ساتھ ٹول استعمال کی مثالیں

ذیل میں کچھ مثالیں ہیں کہ آپ مختلف ایجنٹک فریم ورکس کے ذریعے ٹول استعمال کے ڈیزائن پیٹرن کو کیسے نافذ کر سکتے ہیں:

### سیمنٹک کرنل

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> ایک اوپن سورس AI فریم ورک ہے جو .NET، Python، اور Java ڈیولپرز کے لیے بنایا گیا ہے جو LLMs کے ساتھ کام کر رہے ہیں۔ یہ فنکشن کالنگ کو آسان بنانے کے لیے خود بخود آپ کے فنکشنز اور ان کے پیرا میٹرز کے بارے میں ماڈل کو بیان کر کے <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">سیریلائز</a> کرتا ہے۔ یہ ماڈل اور آپ کے کوڈ کے درمیان بات چیت کو بھی سنبھالتا ہے۔ Semantic Kernel جیسے ایجنٹک فریم ورک کا ایک اور فائدہ یہ ہے کہ آپ پہلے سے تیار شدہ ٹولز جیسے <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">فائل سرچ</a> اور <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">کوڈ انٹرپریٹر</a> تک رسائی حاصل کر سکتے ہیں۔

ذیل میں Semantic Kernel کے ساتھ فنکشن کالنگ کے عمل کی جھلک دکھائی گئی ہے:

![function calling](../../../translated_images/ur/functioncalling-diagram.a84006fc287f6014.webp)

سیمنٹک کرنل میں فنکشنز/ٹولز کو <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">پلگ انز</a> کہا جاتا ہے۔ ہم نے جو `get_current_time` فنکشن دیکھا تھا اسے پلگ ان میں تبدیل کر سکتے ہیں، یعنی اسے ایک کلاس بنائیں جس میں یہ فنکشن ہو۔ ہم `kernel_function` ڈیکوریٹر بھی امپورٹ کر سکتے ہیں، جو فنکشن کی وضاحت لیتا ہے۔ جب آپ GetCurrentTimePlugin کے ساتھ ایک کرنل بنائیں گے، تو کرنل خود بخود فنکشن اور اس کے پیرا میٹرز کو سیریلائز کرے گا، اور LLM کو بھیجنے کے لیے سکیمہ تیار کرے گا۔

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

# کرنل بنائیں
kernel = Kernel()

# پلگ ان بنائیں
get_current_time_plugin = GetCurrentTimePlugin(location)

# پلگ ان کو کرنل میں شامل کریں
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ایک جدید ایجنٹک فریم ورک ہے جو ڈیولپرز کو اجازت دیتا ہے کہ وہ محفوظ طریقے سے اعلیٰ معیار کے، توسیع پذير AI ایجنٹس بنائیں، تعینات کریں، اور اسکیل کریں بغیر نیچے کے کمپیوٹنگ اور اسٹوریج ریسورسز کا انتظام کیے۔ یہ انٹرپرائز ایپلیکیشنز کے لیے خاص طور پر مفید ہے کیونکہ یہ مکمل طور پر منظم سروس ہے اور انٹرپرائز سکیورٹی کا معیار رکھتی ہے۔

LLM API کے ساتھ براہ راست ترقی کے مقابلے میں، Azure AI Agent Service درج ذیل فوائد فراہم کرتا ہے:

- خودکار ٹول کالنگ – اب سرور سائیڈ پر ٹول کال کو پارس کرنا، ٹول چلانا، اور جواب سنبھالنا کیا جاتا ہے۔
- محفوظ طور پر ڈیٹا کا انتظام – اپنی گفتگو کی حالت کنٹرول کرنے کی بجائے، آپ threads پر اعتماد کر سکتے ہیں جو تمام معلومات محفوظ کرتے ہیں۔
- بکسیا فراہم کیے گئے ٹولز – ٹولز جو آپ کو اپنے ڈیٹا ذرائع، جیسے Bing، Azure AI Search، اور Azure Functions سے بات چیت کرنے دیتے ہیں۔

Azure AI Agent Service میں دستیاب ٹولز کو دو اقسام میں تقسیم کیا جا سکتا ہے:

1. نالج ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search کے ساتھ گراؤنڈنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">فائل سرچ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI سرچ</a>

2. ایکشن ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">فنکشن کالنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">کوڈ انٹرپریٹر</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI سے متعین شدہ ٹولز</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ایجنٹ سروس ہمیں یہ اجازت دیتا ہے کہ ہم ان ٹولز کو ایک `toolset` کے طور پر استعمال کر سکیں۔ یہ `threads` کا بھی استعمال کرتا ہے جو ایک خاص گفتگو کی تاریخ کو ٹریک کرتے ہیں۔

تصور کریں کہ آپ Contoso نامی کمپنی کے سیلز ایجنٹ ہیں۔ آپ ایک بات چیت کرنے والا ایجنٹ بنانا چاہتے ہیں جو آپ کے سیلز ڈیٹا کے بارے میں سوالات کے جواب دے سکے۔

ذیل کی تصویر دکھاتی ہے کہ آپ کس طرح Azure AI Agent Service کو استعمال کر کے اپنے سیلز ڈیٹا کا تجزیہ کر سکتے ہیں:

![Agentic Service In Action](../../../translated_images/ur/agent-service-in-action.34fb465c9a84659e.webp)

کسی بھی ٹول کو سروس کے ساتھ استعمال کرنے کے لیے ہم کلائنٹ بنائیں گے اور ٹول یا ٹول سیٹ کی تعریف کریں گے۔ عملی نفاذ کے لیے نیچے Python کوڈ دیا گیا ہے۔ LLM ٹول سیٹ کو دیکھ کر فیصلہ کرے گا کہ صارف کی درخواست کے مطابق خود سے بنایا گیا فنکشن `fetch_sales_data_using_sqlite_query` استعمال کرے یا پہلے سے بنائے گئے کوڈ انٹرپریٹر کو۔

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # وہ fetch_sales_data_using_sqlite_query فنکشن جو fetch_sales_data_functions.py فائل میں پایا جاتا ہے۔
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ٹول سیٹ کو ابتدائی شکل دینا
toolset = ToolSet()

# function calling ایجنٹ کو fetch_sales_data_using_sqlite_query فنکشن کے ساتھ ابتدائی شکل دینا اور اسے ٹول سیٹ میں شامل کرنا
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter ٹول کو ابتدائی شکل دینا اور اسے ٹول سیٹ میں شامل کرنا۔
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## قابل اعتماد AI ایجنٹس بنانے کے لیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کے استعمال میں کیا خاص پہلو ہیں؟

SQL جو LLMs کے ذریعے متحرک طور پر جنریٹ ہوتا ہے، اس کی سیکیورٹی ایک عام تشویش ہے، خاص طور پر SQL انجیکشن یا بدنیتی پر مبنی کاروائیوں جیسے ڈیٹا بیس کو ڈراپ کرنا یا اس میں مداخلت کرنا۔ اگرچہ یہ خدشات جائز ہیں، انہیں ڈیٹا بیس تک رسائی کی اجازتوں کو درست طریقے سے ترتیب دے کر مؤثر طریقے سے کم کیا جا سکتا ہے۔ زیادہ تر ڈیٹا بیس کے لیے یہ ترتیب پڑھنے کے لیے مخصوص ہوتی ہے (read-only)۔ PostgreSQL یا Azure SQL جیسے ڈیٹا بیس سروسز کے لیے، ایپ کو read-only (SELECT) رول تفویض کیا جانا چاہیے۔
ایپ کو ایک محفوظ ماحول میں چلانا حفاظت کو مزید بڑھاتا ہے۔ کاروباری منظرناموں میں، ڈیٹا عام طور پر آپریشنل سسٹمز سے نکالا اور تبدیل کیا جاتا ہے تاکہ اسے ایک پڑھنے کے قابل ڈیٹا بیس یا ڈیٹا ویئرہاؤس میں ایک صارف دوست اسکیمہ کے ساتھ رکھا جا سکے۔ یہ طریقہ کار اس بات کو یقینی بناتا ہے کہ ڈیٹا محفوظ ہے، کارکردگی اور دسترس کے لیے بہتر ہے، اور ایپ کو محدود، صرف پڑھنے کی اجازت حاصل ہے۔

## نمونہ کوڈز

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ٹول کے استعمال کے بارے میں مزید سوالات ہیں؟

دیگر سیکھنے والوں سے ملاقات کے لیے، آفس آورز میں شرکت کریں اور اپنے AI ایجنٹس کے سوالات کے جوابات حاصل کرنے کے لیے [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں۔

## اضافی وسائل

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## پچھلا سبق

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## اگلا سبق

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخطی دستبرداری**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی مجاز اور مستند ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانِ انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->