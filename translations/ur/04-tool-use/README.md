[![اچھے AI ایجنٹس ڈیزائن کرنے کا طریقہ](../../../translated_images/ur/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(اس سبق کی ویڈیو دیکھنے کے لیے اوپر تصویر پر کلک کریں)_

# ٹول استعمال کرنے کا ڈیزائن پیٹرن

ٹولز دلچسپ ہیں کیونکہ وہ AI ایجنٹس کو وسیع تر صلاحیتوں کا حامل بناتے ہیں۔ ایجنٹ کے پاس اگر صرف محدود کارروائیاں کرنے کا اختیار ہو، تو ٹول شامل کر کے ایجنٹ اب مختلف اقسام کی کارروائیاں انجام دے سکتا ہے۔ اس باب میں، ہم ٹول استعمال کرنے کے ڈیزائن پیٹرن کا جائزہ لیں گے، جو بیان کرتا ہے کہ AI ایجنٹس مخصوص ٹولز کو اپنے مقاصد کے حصول کے لیے کیسے استعمال کر سکتے ہیں۔

## تعارف

اس سبق میں، ہم درج ذیل سوالات کے جواب تلاش کرنے کی کوشش کریں گے:

- ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟
- اس کو کن کیسز میں استعمال کیا جا سکتا ہے؟
- اس ڈیزائن پیٹرن کو لاگو کرنے کے لیے کن عناصر / بنیادی اجزاء کی ضرورت ہوتی ہے؟
- قابل اعتبار AI ایجنٹس بنانے کے لیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کے استعمال میں خاص احتیاطی باتیں کیا ہیں؟

## سیکھنے کے مقاصد

اس سبق کے مکمل ہونے کے بعد، آپ قابل ہوں گے کہ:

- ٹول استعمال کرنے کا ڈیزائن پیٹرن اور اس کا مقصد بیان کریں۔
- ایسے کیسز کی شناخت کریں جہاں یہ ڈیزائن پیٹرن قابل اطلاق ہو۔
- ڈیزائن پیٹرن کو نافذ کرنے کے لیے بنیادی عناصر کو سمجھیں۔
- اس ڈیزائن پیٹرن کا استعمال کرتے ہوئے AI ایجنٹس کی قابل اعتباریت کو یقینی بنانے کے لیے غور طلب نکات کو پہچانیں۔

## ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟

**ٹول استعمال کرنے کا ڈیزائن پیٹرن** LLMs کو خارجی ٹولز کے ساتھ تعامل کا امکان دیتا ہے تاکہ مخصوص مقاصد حاصل کیے جا سکیں۔ ٹولز کوڈ ہوتے ہیں جنہیں ایجنٹ کسی کارروائی کے لیے چلا سکتا ہے۔ ٹول ایک سادہ فنکشن ہو سکتا ہے جیسے کیلکولیٹر، یا تیسرے فریق کی سروس کا API کال ہو سکتا ہے جیسے اسٹاک کی قیمت معلوم کرنا یا موسمی پیشنگوئی۔ AI ایجنٹس کے سیاق و سباق میں، ٹولز ایسے ڈیزائن کیے جاتے ہیں کہ وہ **ماڈل کی جانب سے پیدائش پانے والے فنکشن کالز** کے جواب میں ایجنٹس کی جانب سے چلائے جائیں۔

## اس کے استعمال کے وہ کیسز کون سے ہیں جہاں لاگو کیا جا سکتا ہے؟

AI ایجنٹس مختلف پیچیدہ کام مکمل کرنے، معلومات حاصل کرنے یا فیصلے کرنے کے لیے ٹولز کا فائدہ اٹھا سکتے ہیں۔ ٹول استعمال کرنے کا ڈیزائن پیٹرن اکثر ایسے مناظرات میں استعمال ہوتا ہے جن میں خارجی سسٹمز جیسے ڈیٹا بیس، ویب سروسز، یا کوڈ انٹرپریٹرز سے متحرک تعامل کی ضرورت ہوتی ہے۔ یہ صلاحیت درج ذیل کئی مختلف استعمالات کے لیے مفید ہے:

- **متحرک معلومات حاصل کرنا:** ایجنٹس خارجی APIs یا ڈیٹا بیس سے تازہ ترین ڈیٹا حاصل کر سکتے ہیں (مثلاً، SQLite ڈیٹا بیس سے ڈیٹا تجزیہ کے لیے سوال کرنا، اسٹاک کی قیمت یا موسم کی معلومات حاصل کرنا)۔
- **کوڈ کا نفاذ اور تشریح:** ایجنٹس ریاضیاتی مسائل کو حل کرنے، رپورٹس تیار کرنے یا سیمولیشنز کرنے کے لیے کوڈ یا اسکرپٹس چلا سکتے ہیں۔
- **ورک فلو آٹومیشن:** بار بار یا کثیر مراحل والے کاموں کو خودکار بنانے کے لئے ٹولز جیسے ٹاسک شیڈیولرز، ای میل سروسز، یا ڈیٹا پائپ لائنز کا انضمام۔
- **کسٹمر سپورٹ:** ایجنٹس CRM سسٹمز، ٹکٹنگ پلیٹ فارمز، یا نالج بیس کے ساتھ تعامل کر کے صارف کے سوالات حل کر سکتے ہیں۔
- **مواد کی تخلیق اور ترمیم:** ایجنٹس گرامر چیکرز، ٹیکسٹ سمریز یا مواد کی حفاظت کے آلہ جات استعمال کر کے مواد تخلیق کے کاموں میں مدد دے سکتے ہیں۔

## ٹول استعمال کرنے کا ڈیزائن پیٹرن نافذ کرنے کے لیے کن اجزاء / بنیادی بلاکس کی ضرورت ہے؟

یہ بنیادی بلاکس AI ایجنٹ کو متنوع کام انجام دینے کی اجازت دیتے ہیں۔ آئیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کو نافذ کرنے کے لیے ضروری کلیدی عناصر دیکھتے ہیں:

- **فنکشن / ٹول اسکیماز:** دستیاب ٹولز کی تفصیلی تعریفیں، جن میں فنکشن کا نام، مقصد، درکار پیرامیٹرز اور متوقع آؤٹ پٹ شامل ہیں۔ یہ اسکیماز LLM کو یہ سمجھنے کے قابل بناتے ہیں کہ کون سے ٹول دستیاب ہیں اور درست درخواستیں کیسے بنائی جائیں۔

- **فنکشن کے نفاذ کا منطقی سلسلہ:** یہ یوزر کی نیت اور گفتگو کے سیاق و سباق کی بنیاد پر ٹولز کو کب اور کیسے استعمال کیا جائے کو کنٹرول کرتا ہے۔ اس میں منصوبہ ساز ماڈیولز، راستہ تعین کرنے کے طریقے، یا مشروط بہاؤ شامل ہوسکتے ہیں جو ٹول کے استعمال کو متحرک انداز میں طے کرتے ہیں۔

- **پیغام ہینڈلنگ سسٹم:** ایسے اجزاء جو صارف کے ان پٹ، LLM کے جواب، ٹول کالز، اور ٹول آؤٹ پٹ کے درمیان گفتگو کے بہاؤ کو منظم کرتے ہیں۔

- **ٹول انٹیگریشن فریم ورک:** وہ بنیادی ڈھانچہ جو ایجنٹ کو مختلف ٹولز سے جوڑتا ہے، چاہے وہ سادہ فنکشنز ہوں یا پیچیدہ خارجی خدمات۔

- **ایرر ہینڈلنگ اور توثیق:** ایسے طریقے جو ٹول کے نفاذ میں ناکامیوں کو سنبھالتے ہیں، پیرامیٹرز کی تصدیق کرتے ہیں، اور غیر متوقع جوابات کا انتظام کرتے ہیں۔

- **اسٹیٹ مینجمنٹ:** گفتگو کے سیاق و سباق، سابقہ ٹول تعاملات، اور مستقل ڈیٹا کو ٹریک کرتا ہے تاکہ کثیر مراتبی تعاملات میں تسلسل برقرار رہے۔

اگلے حصے میں، فنکشن / ٹول کالنگ کو تفصیل سے دیکھتے ہیں۔
 
### فنکشن / ٹول کالنگ

فنکشن کالنگ وہ بنیادی طریقہ ہے جس سے ہم Large Language Models (LLMs) کو ٹولز کے ساتھ تعامل کرنے کے قابل بناتے ہیں۔ آپ اکثر 'فنکشن' اور 'ٹول' کو بیک وقت استعمال ہوتا دیکھیں گے کیونکہ 'فنکشن' (دوبارہ استعمال ہونے والے کوڈ بلاکس) وہ 'ٹولز' ہیں جنہیں ایجنٹس کام سرانجام دینے کے لیے استعمال کرتے ہیں۔ کسی فنکشن کے کوڈ کو چلانے کے لیے، LLM کو صارف کی درخواست کو فنکشن کی وضاحت سے موازنہ کرنا ہوتا ہے۔ اس کے لئے ایک اسکیمہ جو تمام دستیاب فنکشنز کی وضاحتیں رکھتا ہو، LLM کو بھیجا جاتا ہے۔ LLM پھر کام کے لیے سب سے مناسب فنکشن منتخب کرتا ہے اور اس کا نام اور دلائل واپس کرتا ہے۔ منتخب شدہ فنکشن کو چلایا جاتا ہے، اس کا جواب LLM کو بھیجا جاتا ہے، جو اس معلومات کو صارف کی درخواست کا جواب دینے کے لیے استعمال کرتا ہے۔

ڈویلپرز کے لیے ایجنٹس کے لیے فنکشن کالنگ نافذ کرنے کے لیے آپ کو چاہیے:

1. ایسی LLM ماڈل جو فنکشن کالنگ کو سپورٹ کرتا ہو
2. فنکشن کی تفصیلات پر مشتمل اسکیمہ
3. ہر بیان کیے گئے فنکشن کا کوڈ

آئیں شہر میں موجودہ وقت حاصل کرنے کی مثال لیں:

1. **ایسی LLM کو شروع کریں جو فنکشن کالنگ کو سپورٹ کرے:**

    تمام ماڈلز فنکشن کالنگ کو سپورٹ نہیں کرتے، اس لیے یہ چیک کرنا ضروری ہے کہ آپ جو LLM استعمال کر رہے ہیں وہ ایسا کرتا ہو۔    <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> فنکشن کالنگ کو سپورٹ کرتا ہے۔ ہم OpenAI کلائنٹ کو Azure OpenAI **Responses API** کے خلاف چلا کر شروع کر سکتے ہیں (مستحکم `/openai/v1/` اینڈ پوائنٹ — کسی `api_version` کی ضرورت نہیں)۔

    ```python
    # Azure OpenAI (Responses API, v1 endpoint) کے لیے OpenAI کلائنٹ کو شروع کریں
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **فنکشن اسکیمہ بنائیں**:

    اگلے مرحلے میں ہم ایک JSON اسکیمہ متعین کریں گے، جس میں فنکشن کا نام، فنکشن کے کام کی وضاحت، اور فنکشن کے پیرامیٹرز کے نام اور وضاحتیں ہوں گی۔
    اس اسکیمہ کو ہم کلائنٹ کو بھیجیں گے جسے پہلے بنایا گیا تھا، اور صارف کی درخواست جو سان فرانسسکو کا وقت معلوم کرنے کی ہے۔ جو بات اہم ہے کہ ایک **ٹول کال** واپس کیا جاتا ہے، **سوال کا حتمی جواب نہیں**۔ جیسا کہ پہلے بتایا گیا کہ LLM اس فنکشن کا نام واپس کرتا ہے جو اس نے منتخب کیا ہے، اور دلائل جو بھیجے جائیں گے۔

    ```python
    # ماڈل کے لیے فنکشن کی تفصیل پڑھنے کے لیے (Responses API فلیٹ ٹول فارمیٹ)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # ابتدائی صارف کا پیغام
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # پہلا API کال: ماڈل سے کہیں کہ فنکشن استعمال کرے
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API جواب میں function_call اشیاء کے طور پر ٹول کالز واپس کرتا ہے جو response.output میں ہوتی ہیں۔
    # انہیں گفتگو میں شامل کریں تاکہ ماڈل کو اگلے مرحلے کے لیے مکمل سیاق و سباق حاصل ہو۔
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **وہ فنکشن کوڈ جو کام مکمل کرے گا:**

    اب چونکہ LLM نے منتخب کر لیا ہے کہ کون سا فنکشن چلانا ہے، کام مکمل کرنے کا کوڈ لکھنا اور چلانا ضروری ہے۔
    ہم موجودہ وقت حاصل کرنے کا کوڈ Python میں لکھ سکتے ہیں۔ ہمیں response_message سے نام اور دلائل نکالنے کا کوڈ بھی لکھنا ہوگا تاکہ آخری نتیجہ حاصل ہو۔

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # ٹول کے نتیجے کو function_call_output آئٹم کے طور پر واپس کریں
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # دوسرا API کال: ماڈل سے حتمی رد عمل حاصل کریں
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

فنکشن کالنگ زیادہ تر، اگر تمام نہیں، ایجنٹ ٹول استعمال کرنے کے ڈیزائن کی جڑ ہے، تاہم اسے شروع سے نافذ کرنا کبھی کبھار چیلنجنگ ہو سکتا ہے۔
جیسا کہ ہم نے [سبق 2](../../../02-explore-agentic-frameworks) میں سیکھا، ایجنٹک فریم ورکس ہمیں پہلے سے تیار شدہ بنیادی بلاکس فراہم کرتے ہیں تاکہ ٹول استعمال کو نافذ کیا جا سکے۔
 
## ایجنٹک فریم ورکس کے ساتھ ٹول استعمال کی مثالیں

یہاں کچھ مثالیں ہیں کہ آپ مختلف ایجنٹک فریم ورکس کا استعمال کر کے ٹول استعمال کرنے کا ڈیزائن پیٹرن کیسے نافذ کر سکتے ہیں:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> ایک اوپن سورس AI فریم ورک ہے جو AI ایجنٹس بنانے کے لیے استعمال ہوتا ہے۔ یہ فنکشن کالنگ کے عمل کو آسان بناتا ہے، جس میں آپ آسانی سے ٹولز کو Python فنکشنز کے طور پر `@tool` کے زیریں نشان کے ذریعے متعین کر سکتے ہیں۔ فریم ورک ماڈل اور آپ کے کوڈ کے درمیان رابطہ سنبھالتا ہے۔ یہ پہلے سے تیار کردہ ٹولز جیسے File Search اور Code Interpreter تک رسائی بھی فراہم کرتا ہے `FoundryChatClient` کے ذریعے۔

ذیل میں ایک ڈایاگرام دیا گیا ہے جو Microsoft Agent Framework کے ساتھ فنکشن کالنگ کے عمل کو ظاہر کرتا ہے:

![فنکشن کالنگ](../../../translated_images/ur/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework میں، ٹولز کو سجاوٹ شدہ فنکشنز کے طور پر بیان کیا جاتا ہے۔ ہم `get_current_time` فنکشن کو، جو ہم نے پہلے دیکھا، `@tool` سجاوٹ کے ساتھ ایک ٹول میں تبدیل کر سکتے ہیں۔ فریم ورک خود بخود فنکشن اور اس کے پیرامیٹرز کو سیریلائز کرتا ہے، اسکیمہ بناتا ہے اور اسے LLM کو بھیجتا ہے۔

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# کلائنٹ بنائیں
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ایک ایجنٹ بنائیں اور ٹول کے ساتھ چلائیں
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> ایک نیا ایجنٹک فریم ورک ہے جو ڈویلپرز کو محفوظ طریقے سے اعلی معیار کے، توسیعی AI ایجنٹس بنانے، تعینات کرنے اور اسکیل کرنے کی سہولت دیتا ہے بغیر بنیادی کمپیوٹ اور اسٹوریج وسائل کا انتظام کیے۔ یہ خاص طور پر انٹرپرائز ایپلیکیشنز کے لیے مفید ہے کیونکہ یہ مکمل طور پر منظم سروس ہے جس میں انٹرپرائز سیکیورٹی بھی شامل ہے۔

LLM API کے مقابلے میں براہِ راست ترقی کے، Microsoft Foundry Agent Service درج ذیل فوائد فراہم کرتا ہے:

- خودکار ٹول کالنگ – اب ٹول کال کو پارس کرنے، ٹول چلانے اور جواب سنبھالنے کی ضرورت نہیں؛ یہ سب سرور سائیڈ سے ہوتا ہے
- محفوظ طریقے سے مینج کردہ ڈیٹا – اپنی خود کی گفتگو کی حالت سنبھالنے کے بجائے، آپ تھریڈز پر اعتماد کر سکتے ہیں جو تمام معلومات ذخیرہ کرتے ہیں
- پہلے سے تیار کردہ ٹولز – ایسے ٹولز جو آپ کو اپنے ڈیٹا ذرائع کے ساتھ تعامل کرنے دیتے ہیں، جیسا کہ Bing، Azure AI Search، اور Azure Functions

Microsoft Foundry Agent Service میں دستیاب ٹولز کو دو زمروں میں تقسیم کیا جا سکتا ہے:

1. نالج ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing سرچ کے ساتھ گراؤنڈنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">فائل سرچ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI سرچ</a>

2. ایکشن ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">فنکشن کالنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">کوڈ انٹرپریٹر</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI سے متعین کیے گئے ٹولز</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure فنکشنز</a>

ایجنٹ سروس ہمیں یہ اجازت دیتا ہے کہ ہم ان ٹولز کو `toolset` کے طور پر ایک ساتھ استعمال کریں۔ یہ `threads` کا بھی استعمال کرتا ہے جو کسی خاص گفتگو کے پیغامات کی تاریخ کو ٹریک کرتا ہے۔

تصور کریں کہ آپ Contoso نامی کمپنی میں سیلز ایجنٹ ہیں۔ آپ ایک بات چیت کا ایجنٹ تیار کرنا چاہتے ہیں جو آپ کے سیلز ڈیٹا کے بارے میں سوالات کے جواب دے سکے۔

ذیل کی تصویر دکھاتی ہے کہ آپ Microsoft Foundry Agent Service کا استعمال کر کے کس طرح اپنے سیلز ڈیٹا کا تجزیہ کر سکتے ہیں:

![Agentic Service In Action](../../../translated_images/ur/agent-service-in-action.34fb465c9a84659e.webp)

ان ٹولز کو سروس کے ساتھ استعمال کرنے کے لیے، ہم کلائنٹ بنا کر ٹول یا ٹول سیٹ کی تعریف کر سکتے ہیں۔ عملی طور پر یہ ہم ذیل کے Python کوڈ سے کر سکتے ہیں۔ LLM ٹول سیٹ دیکھ کر فیصلہ کرے گا کہ صارف کی درخواست کے مطابق صارف کی جانب سے بنایا گیا فنکشن `fetch_sales_data_using_sqlite_query` استعمال کیا جائے یا پہلے سے تیار شدہ کوڈ انٹرپریٹر۔

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

# ٹول سیٹ کو شروع کریں
toolset = ToolSet()

# فنکشن کالنگ ایجنٹ کو fetch_sales_data_using_sqlite_query فنکشن کے ساتھ شروع کریں اور اسے ٹول سیٹ میں شامل کریں
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# کوڈ انٹرپریٹر ٹول کو شروع کریں اور اسے ٹول سیٹ میں شامل کریں۔
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## قابل اعتماد AI ایجنٹس بنانے کے لیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کے خصوصی نکات کیا ہیں؟

LLMs کی جانب سے ڈائنامک طور پر تیار کردہ SQL کے ساتھ سب سے عام تشویش سیکورٹی ہے، خاص طور پر SQL انجیکشن یا نقصان دہ کارروائیوں جیسے ڈیٹا بیس کا نقصان یا چھیڑ چھاڑ کا خطرہ۔ یہ تشویشیں معقول ہیں، تاہم انہیں مؤثر طریقے سے روکا جا سکتا ہے اگر ڈیٹا بیس کی رسائی کی اجازتوں کو درست طریقے سے ترتیب دیا جائے۔ بیشتر ڈیٹا بیسز کے لیے یہ ترتیب انھیں صرف پڑھنے کے قابل بنایا جانا ہے۔ PostgreSQL یا Azure SQL جیسی خدمات کے لیے، ایپ کو ایک صرف پڑھنے کی (SELECT) پرمیشن دی جانی چاہیے۔

درخواست کو ایک محفوظ ماحول میں چلانا حفاظت کو مزید بڑھاتا ہے۔ انٹرپرائز مناظرات میں عام طور پر ڈیٹا آپریشنل سسٹمز سے نکالا اور تبدیل کیا جاتا ہے تاکہ اسے ایک صرف پڑھنے کے قابل ڈیٹا بیس یا ڈیٹا ویئرہاؤس میں رکھا جائے جس میں صارف دوستانہ اسکیمہ ہوتا ہے۔ یہ طریقہ کار یہ یقینی بناتا ہے کہ ڈیٹا محفوظ، کارکردگی اور رسائی کے لحاظ سے بہتر ہے، اور ایپ کے پاس محدود اور صرف پڑھنے کا حق ہے۔

## نمونہ کوڈز

- Python: [ایجنٹ فریم ورک](./code_samples/04-python-agent-framework.ipynb)
- .NET: [ایجنٹ فریم ورک](./code_samples/04-dotnet-agent-framework.md)

## ٹول استعمال ڈیزائن پیٹرن کے بارے میں مزید سوالات ہیں؟

دیگر سیکھنے والوں سے ملنے، آفس آورز میں شرکت کرنے، اور اپنے AI ایجنٹس کے سوالات کے جواب حاصل کرنے کے لیے [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) میں شامل ہوں۔

## اضافی وسائل

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents سروس ورکشاپ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent ورکشاپ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework کا جائزہ</a>


## اس ایجنٹ کا سموک ٹیسٹنگ (اختیاری)

جب آپ [سبق 16](../16-deploying-scalable-agents/README.md) میں ایجنٹس کو ڈپلائے کرنا سیکھ جاتے ہیں، تو آپ اس سبق کے `TravelToolAgent` کا سموک ٹیسٹ کر سکتے ہیں (کیا یہ اب بھی اپنے ٹولز کو کال کرتا ہے اور جواب دیتا ہے؟) جس کے لیے [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) استعمال کریں۔ اسے چلانے کے طریقے کے لیے [`tests/README.md`](../tests/README.md) دیکھیں۔

## پچھلا سبق

[ایجنٹک ڈیزائن پیٹرنز کو سمجھنا](../03-agentic-design-patterns/README.md)

## اگلا سبق

[ایجنٹک RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->