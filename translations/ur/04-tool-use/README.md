[![اچھے AI ایجنٹس کیسے ڈیزائن کریں](../../../translated_images/ur/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(اس سبق کی ویڈیو دیکھنے کے لیے اوپر دی گئی تصویر پر کلک کریں)_

# ٹول استعمال کرنے کا ڈیزائن پیٹرن

ٹولز دلچسپ ہیں کیونکہ وہ AI ایجنٹس کو وسیع تر صلاحیتوں کا دائرہ فراہم کرتے ہیں۔ ایجنٹ کے پاس محدود ایکشنز کے سیٹ کے بجائے، ایک ٹول شامل کرنے سے، ایجنٹ اب بہت سے مختلف ایکشنز کر سکتا ہے۔ اس باب میں، ہم ٹول استعمال کرنے کے ڈیزائن پیٹرن کو دیکھیں گے، جو بیان کرتا ہے کہ AI ایجنٹس مخصوص ٹولز کو اپنے اہداف حاصل کرنے کے لیے کیسے استعمال کر سکتے ہیں۔

## تعارف

اس سبق میں، ہم درج ذیل سوالات کے جواب تلاش کرنے والے ہیں:

- ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟
- کن استعمال کے کیسز پر اسے لاگو کیا جا سکتا ہے؟
- اس ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بلڈنگ بلاکس درکار ہیں؟
- قابل اعتماد AI ایجنٹس بنانے کے لیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کے استعمال میں کون سی خاص باتیں مد نظر رکھنی چاہئیں؟

## سیکھنے کے مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ قادر ہوں گے کہ:

- ٹول استعمال کرنے کے ڈیزائن پیٹرن کی تعریف اور اس کا مقصد بیان کریں۔
- ایسے استعمال کے کیسز کی شناخت کریں جہاں ٹول استعمال کرنے کا ڈیزائن پیٹرن نافذ کیا جا سکتا ہے۔
- ڈیزائن پیٹرن کو نافذ کرنے کے لیے ضروری اہم عناصر کو سمجھیں۔
- اس ڈیزائن پیٹرن کا استعمال کرتے ہوئے AI ایجنٹس میں قابل اعتماد ہونے کی شرائط کو پہچانیں۔

## ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟

**ٹول استعمال کرنے کا ڈیزائن پیٹرن** LLMs کو بیرونی ٹولز کے ساتھ انٹرایکٹ کرنے کی صلاحیت دیتا ہے تاکہ مخصوص مقاصد حاصل کیے جا سکیں۔ ٹولز وہ کوڈ ہوتے ہیں جنہیں ایک ایجنٹ عملدرآمد کر کے ایکشنز انجام دیتا ہے۔ ایک ٹول سادہ فنکشن ہو سکتا ہے جیسے کیلکولیٹر، یا کسی تیسری پارٹی کی سروس کا API کال جیسے اسٹاک قیمت معلوم کرنا یا موسم کی پیش گوئی۔ AI ایجنٹس کے تناظر میں، ٹولز کو ماڈل کی طرف سے تخلیق کیے گئے فنکشن کالز کے جواب میں ایجنٹ کے ذریعے چلانے کے لیے ڈیزائن کیا جاتا ہے۔

## کن استعمال کے کیسز پر اسے لاگو کیا جا سکتا ہے؟

AI ایجنٹس ٹولز کا استعمال کر کے پیچیدہ کام مکمل کر سکتے ہیں، معلومات حاصل کر سکتے ہیں، یا فیصلے کر سکتے ہیں۔ ٹول استعمال کرنے کا ڈیزائن پیٹرن اکثر ایسے مناظرات میں استعمال ہوتا ہے جہاں بیرونی نظاموں کے ساتھ متحرک تعامل درکار ہوتا ہے، جیسے ڈیٹا بیسز، ویب سروسز، یا کوڈ انٹرپریٹرز۔ اس صلاحیت کے کئی مختلف استعمالات ہیں جن میں شامل ہیں:

- **متحرک معلومات کی بازیافت:** ایجنٹس بیرونی APIs یا ڈیٹا بیسز سے تازہ ترین ڈیٹا حاصل کر سکتے ہیں (مثلاً SQLite ڈیٹا بیس سے ڈیٹا تجزیہ کے لیے سوال کرنا، اسٹاک کی قیمتیں یا موسم کی معلومات حاصل کرنا)۔
- **کوڈ کی عملدرآمد اور تشریح:** ایجنٹس کوڈ یا اسکرپٹس چلانے کے قابل ہوتے ہیں، ریاضی کے مسائل حل کرنے، رپورٹس بنانے، یا سمولیشن کرنے کے لیے۔
- **ورک فلو خودکاری:** ٹاسک شیڈولرز، ای میل سروسز، یا ڈیٹا پائپ لائنز جیسے ٹولز کو جوڑ کر بار بار یا کثیر مرحلہ ورکس کو خودکار بنانا۔
- **کسٹمر سپورٹ:** ایجنٹس CRM سسٹمز، ٹکٹنگ پلیٹ فارمز، یا نالج بیسز کے ساتھ بات چیت کر کے صارف کے سوالات کا حل فراہم کر سکتے ہیں۔
- **مواد کی تخلیق اور ترمیم:** ایجنٹس گرائمَر چیکرز، ٹیکسٹ سمریزرز، یا مواد کی حفاظت کے تجزیہ کار جیسے ٹولز کا استعمال کر کے مواد کے تخلیقی کاموں میں مدد کر سکتے ہیں۔

## ٹول استعمال کرنے کے ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بلڈنگ بلاکس درکار ہیں؟

یہ بلڈنگ بلاکس AI ایجنٹ کو مختلف کام سرانجام دینے کی اجازت دیتے ہیں۔ آئیے وہ اہم عناصر دیکھتے ہیں جو ٹول استعمال کرنے کے ڈیزائن پیٹرن کو نافذ کرنے کے لیے درکار ہیں:

- **فنکشن/ٹول اسکیمے**: دستیاب ٹولز کی تفصیلی تعریفیں، جن میں فنکشن کا نام، مقصد، ضروری پیرامیٹرز، اور متوقع آؤٹ پٹ شامل ہیں۔ یہ اسکیمے LLM کو بتاتی ہیں کہ کون سے ٹولز دستیاب ہیں اور درست درخواستیں کیسے بنائی جائیں۔

- **فنکشن عملدرآمد کا لاجک**: یوزر کی نیت اور گفتگو کے سیاق و سباق کی بنیاد پر ٹولز کو کب اور کیسے کال کیا جائے، اسے کنٹرول کرتا ہے۔ اس میں پلانر ماڈیولز، روٹنگ میکنزم، یا شرائطی بہاؤ شامل ہو سکتے ہیں جو ٹول کے استعمال کا تعین کرتے ہیں۔

- **پیغام ہینڈلنگ سسٹم**: ایسے اجزاء جو یوزر ان پٹس، LLM جوابات، ٹول کالز، اور ٹول آؤٹ پٹس کے درمیان گفتگو کے بہاؤ کو منظم کرتے ہیں۔

- **ٹول انٹیگریشن فریم ورک**: وہ انفراسٹرکچر جو ایجنٹ کو مختلف ٹولز سے جوڑتا ہے، چاہے وہ سادہ فنکشن ہوں یا پیچیدہ بیرونی خدمات۔

- **غلطیوں کا انتظام اور تصدیق**: وہ طریقے جن سے ٹول عملدرآمد کی ناکامیوں کو سنبھالا جاتا ہے، پیرامیٹرز کی تصدیق کی جاتی ہے، اور غیر متوقع جوابات کا انتظام کیا جاتا ہے۔

- **حالت کا انتظام**: گفتگو کے سیاق و سباق، پچھلے ٹول تعاملات، اور مستقل ڈیٹا کو ٹریک کرتا ہے تاکہ متعدد موڑ کی بات چیت میں تسلسل یقینی بنایا جا سکے۔

اب ہم فنکشن/ٹول کالنگ کو تفصیل سے دیکھتے ہیں۔

### فنکشن/ٹول کالنگ

فنکشن کالنگ وہ بنیادی طریقہ ہے جس سے ہم بڑے زبان کے ماڈلز (LLMs) کو ٹولز کے ساتھ انٹرایکٹ کرنے کے قابل بناتے ہیں۔ آپ اکثر 'فنکشن' اور 'ٹول' کو باری باری استعمال ہوتے ہوئے دیکھیں گے کیونکہ 'فنکشنز' (قابلِ استعمال کوڈ کے بلاکس) وہ 'ٹولز' ہیں جو ایجنٹس کام انجام دینے کے لیے استعمال کرتے ہیں۔ کسی فنکشن کے کوڈ کو چلانے کے لیے، LLM کو صارف کی درخواست کو فنکشن کی تفصیل سے موازنہ کرنا ہوتا ہے۔ اس مقصد کے لیے، ایک اسکیمہ بنایا جاتا ہے جس میں دستیاب تمام فنکشنز کی تفصیلات شامل ہوتی ہیں جو LLM کو بھیجی جاتی ہے۔ LLM پھر سب سے مناسب فنکشن منتخب کرتا ہے اور اس کا نام اور آرگیومنٹس واپس کرتا ہے۔ منتخب کردہ فنکشن چلا کر اس کا جواب LLM کو بھیج دیا جاتا ہے، جو اس معلومات کو استعمال کرتے ہوئے صارف کی درخواست کا جواب دیتا ہے۔

ڈیولپرز کو فنکشن کالنگ نافذ کرنے کے لیے درج ذیل چیزیں درکار ہوں گی:

1. ایسا LLM ماڈل جو فنکشن کالنگ کو سپورٹ کرتا ہو
2. فنکشن کی تفصیل پر مشتمل اسکیمہ
3. ہر بیان کردہ فنکشن کا کوڈ

آئیے ایک مثال لیتے ہیں: کسی شہر کا موجودہ وقت حاصل کرنا۔

1. **فنکشن کالنگ سپورٹ کرنے والا LLM انیشیالائز کریں:**

    تمام ماڈلز فنکشن کالنگ سپورٹ نہیں کرتے، اس لیے یہ چیک کرنا ضروری ہے کہ آپ کا LLM ایسا کرتا ہے یا نہیں۔  
    <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> فنکشن کالنگ کو سپورٹ کرتا ہے۔ ہم Azure OpenAI کلائنٹ کو شروع کر کے شروع کر سکتے ہیں۔

    ```python
    # آزور اوپن اے آئی کلائنٹ کو شروع کریں
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **فنکشن اسکیمہ بنائیں:**

    اگلا مرحلہ JSON اسکیمہ کی تعریف کرنا ہے جس میں فنکشن کا نام، اس کا کیا کام ہے کی تفصیل، اور فنکشن کے پیرامیٹرز کے نام اور وضاحتیں شامل ہوں۔
    پھر ہم اس اسکیمہ کو پچھلے کلائنٹ کو بھیجیں گے، ساتھ ہی صارف کی درخواست بھی تاکہ سان فرانسسکو کا وقت معلوم کیا جا سکے۔ اہم بات یہ ہے کہ واپس آنے والا **جوابة ٹول کال** ہوتا ہے، سوال کا حتمی جواب نہیں۔ جیسا کہ پہلے ذکر کیا گیا، LLM اس فنکشن کا نام اور آرگیومنٹس دیتا ہے جسے اس نے اس کام کے لیے منتخب کیا ہے۔

    ```python
    # ماڈل کے لئے پڑھنے کی فنکشن کی تفصیل
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
  
    # پہلا API کال: ماڈل سے کہیں کہ فنکشن استعمال کرے
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
  
3. **کام سرانجام دینے کے لیے ضروری فنکشن کوڈ:**

    اب چونکہ LLM نے فیصلہ کر لیا ہے کہ کون سا فنکشن چلانا ہے، اس کام کو انجام دینے والا کوڈ لکھ کر چلانا ہوگا۔
    ہم پائتھون میں موجودہ وقت حاصل کرنے کا کوڈ لکھیں گے۔ نیز جواب سے فنکشن کا نام اور آرگیومنٹس نکالنے کے لیے کوڈ بھی لکھنا ہوگا تاکہ حتمی نتیجہ حاصل ہو۔

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

فنکشن کالنگ زیادہ تر، اگر سب نہیں تو، ایجنٹ ٹول استعمال کرنے کے ڈیزائن کا مرکزی حصہ ہے، لیکن اسے شروع سے مکمل کرنا کبھی کبھی مشکل ہو سکتا ہے۔  
جیسا کہ ہم نے [سبق 2](../../../02-explore-agentic-frameworks) میں سیکھا، ایجنٹ فریم ورکس ہمیں ٹول استعمال کرنے کے لیے پہلے سے تیار بلڈنگ بلاکس فراہم کرتے ہیں۔

## ایجنٹک فریم ورکس کے ساتھ ٹول استعمال کی مثالیں

یہاں مختلف ایجنٹک فریم ورکس کا استعمال کرتے ہوئے ٹول استعمال کے ڈیزائن پیٹرن کو نافذ کرنے کی چند مثالیں دی گئی ہیں:

### مائیکروسافٹ ایجنٹ فریم ورک

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">مائیکروسافٹ ایجنٹ فریم ورک</a> ایک اوپن سورس AI فریم ورک ہے جو AI ایجنٹس بنانے کے لیے استعمال ہوتا ہے۔ یہ فنکشن کالنگ کے استعمال کو آسان بناتا ہے آپ کوٹولز کو Python فنکشنز کے طور پر `@tool` ڈیکوریٹر کے ساتھ بیان کرنے کی اجازت دیتا ہے۔ یہ فریم ورک ماڈل اور آپ کے کوڈ کے درمیان پیغام رسانی کو خود بخود سنبھالتا ہے۔ اس کے علاوہ یہ پہلے سے بنے ہوئے ٹولز جیسے فائل سرچ اور کوڈ انٹرپریٹر تک رسائی بھی دیتا ہے جو `AzureAIProjectAgentProvider` کے ذریعے دستیاب ہیں۔

مندرجہ ذیل خاکہ مائیکروسافٹ ایجنٹ فریم ورک میں فنکشن کالنگ کے عمل کو ظاہر کرتا ہے:

![function calling](../../../translated_images/ur/functioncalling-diagram.a84006fc287f6014.webp)

مائیکروسافٹ ایجنٹ فریم ورک میں، ٹولز کو ڈیکوریٹر والے فنکشنز کے طور پر ڈیفائن کیا جاتا ہے۔ ہم نے جو `get_current_time` فنکشن پہلے دیکھا تھا، اسے `@tool` ڈیکوریٹر لگا کر ٹول میں تبدیل کر سکتے ہیں۔ فریم ورک خود بخود فنکشن اور اس کے پیرامیٹرز کو سیریلائز کر کے LLM کو بھیجنے کے لیے اسکیمہ بناتا ہے۔

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# کلائنٹ بنائیں
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ایک ایجنٹ بنائیں اور ٹول کے ساتھ چلائیں
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent سروس

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent سروس</a> ایک تازہ ترین ایجنٹک فریم ورک ہے جو ڈویلپرز کو محفوظ طریقے سے اعلی معیار کے AI ایجنٹس بنانے، ڈیپلائے کرنے، اور اسکیل کرنے کے لیے تیار کیا گیا ہے، بجائے اس کے کہ وہ بنیادی کمپیوٹ اور اسٹوریج کے وسائل کا خود انتظام کریں۔ یہ اینٹرپرائز ایپلیکیشنز کے لیے خاص طور پر مفید ہے کیونکہ یہ ایک مکمل منظم شدہ سروس ہے جس میں انٹرپرائز گریڈ سیکیورٹی دستیاب ہے۔

LLM API کے ساتھ براہ راست ڈویلپمنٹ کے مقابلے میں، Azure AI Agent Service کچھ فوائد فراہم کرتا ہے:

- خودکار ٹول کالنگ – اب ٹول کال کو پارس کرنے، ٹول کو چلانے، اور جواب سنبھالنے کی ضرورت نہیں؛ یہ سب سرور سائڈ پر ہوتا ہے
- محفوظ شدہ ڈیٹا – اپنی گفتگو کی حالت کا انتظام کرنے کی بجائے، آپ تھریڈز پر انحصار کر سکتے ہیں جو تمام معلومات ذخیرہ کرتے ہیں
- تیار شدہ ٹولز – ایسے ٹولز جو آپ کو ڈیٹا ذرائع جیسے Bing، Azure AI Search، اور Azure Functions کے ساتھ تعامل کرنے کی اجازت دیتے ہیں۔

Azure AI Agent Service میں دستیاب ٹولز کو دو اقسام میں تقسیم کیا جا سکتا ہے:

1. نالج ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing سرچ کے ذریعے گراؤنڈنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">فائل سرچ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI سرچ</a>

2. ایکشن ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">فنکشن کالنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">کوڈ انٹرپریٹر</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI ڈیفائن کردہ ٹولز</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure فنکشنز</a>

ایجنٹ سروس ہمیں ان ٹولز کو ایک `toolset` کے طور پر ایک ساتھ استعمال کرنے کی سہولت دیتی ہے۔ یہ `threads` کا بھی استعمال کرتی ہے جو کسی مخصوص گفتگو کے پیغاموں کی تاریخ کو ٹریک کرتے ہیں۔

تصور کریں کہ آپ Contoso نامی کمپنی میں ایک سیلز ایجنٹ ہیں۔ آپ ایک بات چیت کرنے والا ایجنٹ تیار کرنا چاہتے ہیں جو آپ کے سیلز ڈیٹا کے بارے میں سوالات کے جوابات دے سکے۔

مندرجہ ذیل تصویر دکھاتی ہے کہ آپ Azure AI Agent Service کو اپنے سیلز ڈیٹا کا تجزیہ کرنے کے لیے کیسے استعمال کر سکتے ہیں:

![Agentic Service In Action](../../../translated_images/ur/agent-service-in-action.34fb465c9a84659e.webp)

سروس کے ساتھ ان میں سے کوئی بھی ٹول استعمال کرنے کے لیے ہم کلائنٹ بنا کر ٹول یا ٹول سیٹ ڈیفائن کر سکتے ہیں۔ عملی نفاذ کے لیے ہم درج ذیل Python کوڈ استعمال کر سکتے ہیں۔ LLM ٹول سیٹ پر نظر ڈال کر فیصلہ کرے گا کہ آیا صارف کے سوال کے مطابق یوزر کا بنایا ہوا فنکشن `fetch_sales_data_using_sqlite_query` استعمال کیا جائے یا پہلے سے بنے ہوئے کوڈ انٹرپریٹر کو۔

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query فنکشن جو fetch_sales_data_functions.py فائل میں پایا جا سکتا ہے۔
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ٹول سیٹ کو ابتدائی شکل دینا
toolset = ToolSet()

# فنکشن کالنگ ایجنٹ کو fetch_sales_data_using_sqlite_query فنکشن کے ساتھ ابتدائی شکل دینا اور اسے ٹول سیٹ میں شامل کرنا
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# کوڈ انٹر پریٹر ٹول کو ابتدائی شکل دینا اور اسے ٹول سیٹ میں شامل کرنا۔
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## قابل اعتماد AI ایجنٹس بنانے میں ٹول استعمال کرنے کے ڈیزائن پیٹرن کا استعمال کرتے وقت خاص باتیں

LLM کی طرف سے متحرک طور پر پیدا کردہ SQL میں ایک عام فکر سلامتی کی ہوتی ہے، خاص طور پر SQL انجیکشن یا نقصان دہ کاروائیوں کا خطرہ، جیسے ڈیٹا بیس کو حذف کرنا یا اس میں مداخلت کرنا۔ اگرچہ یہ خدشات بجا ہیں، لیکن ڈیٹا بیس کی رسائی کی اجازتوں کو صحیح طریقے سے ترتیب دے کر انہیں مؤثر طریقے سے کم کیا جا سکتا ہے۔ زیادہ تر ڈیٹا بیسز کے لیے یہ مطلب ہوتا ہے کہ ڈیٹا بیس کو صرف پڑھنے کے موڈ پر ترتیب دیا جائے۔ PostgreSQL یا Azure SQL جیسی ڈیٹا بیس سروسز کے لیے، ایپ کو صرف پڑھنے (SELECT) کا کردار دیا جانا چاہیے۔

ایپ کو محفوظ ماحول میں چلانا بھی حفاظت کو بڑھاتا ہے۔ اینٹرپرائز منظرناموں میں، ڈیٹا عام طور پر آپریشنل سسٹمز سے نکال کر ایک پڑھنے کے لیے مخصوص ڈیٹا بیس یا ڈیٹا ویئر ہاؤس میں منتقل کیا جاتا ہے جس کا اسکیمہ صارف دوست ہوتا ہے۔ اس سے یہ یقینی بنتا ہے کہ ڈیٹا محفوظ ہے، کارکردگی اور رسائی کے لیے بہتر ہے، اور ایپ کو محدود، صرف پڑھنے کی اجازت ملتی ہے۔

## نمونہ کوڈز

- Python: [ایجنٹ فریم ورک](./code_samples/04-python-agent-framework.ipynb)
- .NET: [ایجنٹ فریم ورک](./code_samples/04-dotnet-agent-framework.md)

## ٹول استعمال کرنے کے ڈیزائن پیٹرنز کے بارے میں مزید سوالات ہیں؟

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں تاکہ دوسرے سیکھنے والوں سے مل سکیں، دفتر کے اوقات میں شرکت کریں، اور اپنے AI ایجنٹس کے سوالات کے جواب حاصل کریں۔

## اضافی وسائل

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents سروس ورکشاپ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer ملٹی ایجنٹ ورکشاپ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework کا جائزہ</a>

## پچھلا سبق

[ایجنٹک ڈیزائن پیٹرنز کو سمجھنا](../03-agentic-design-patterns/README.md)

## اگلا سبق
[ایجنٹک RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->