[![اچھے AI ایجنٹس کیسے ڈیزائن کریں](../../../translated_images/ur/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(سبق کی ویڈیو دیکھنے کے لیے اوپر موجود تصویر پر کلک کریں)_

# Tool Use Design Pattern

ٹولز دلچسپ ہیں کیونکہ وہ AI ایجنٹس کو وسیع تر صلاحیتوں کا حامل بناتے ہیں۔ محدود کارروائیوں کے بجائے جو ایجنٹ انجام دے سکتا ہے، کسی ٹول کے اضافے سے ایجنٹ اب وسیع تر اعمال انجام دے سکتا ہے۔ اس باب میں، ہم Tool Use Design Pattern کا جائزہ لیں گے، جو بتاتا ہے کہ AI ایجنٹس مخصوص ٹولز کو اپنے مقاصد حاصل کرنے کے لیے کیسے استعمال کر سکتے ہیں۔

## Introduction

اس سبق میں ہم درج ذیل سوالات کے جواب تلاش کریں گے:

- ٹول یوز ڈیزائن پیٹرن کیا ہے؟
- کن استعمال کے کیسز میں اسے لاگو کیا جا سکتا ہے؟
- ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بلڈنگ بلاکس درکار ہیں؟
- قابل اعتماد AI ایجنٹس تعمیر کرنے کے لیے Tool Use Design Pattern استعمال کرتے وقت خصوصی غور و فکر کیا ہیں؟

## Learning Goals

اس سبق کو مکمل کرنے کے بعد، آپ قابل ہو جائیں گے:

- Tool Use Design Pattern اور اس کے مقصد کی تعریف کرنا۔
- ان استعمال کے کیسز کی شناخت کرنا جہاں Tool Use Design Pattern لاگو ہونے کے قابل ہو۔
- ڈیزائن پیٹرن کو نافذ کرنے کے لیے درکار اہم عناصر کو سمجھنا۔
- اس ڈیزائن پیٹرن کو استعمال کرنے والے AI ایجنٹس میں اعتماد کو یقینی بنانے کے لئے غور و فکر کو پہچاننا۔

## What is the Tool Use Design Pattern?

**Tool Use Design Pattern** کا محور یہ ہے کہ LLMs کو بیرونی ٹولز کے ساتھ تعامل کرنے کی صلاحیت دی جائے تاکہ مخصوص مقاصد حاصل کیے جا سکیں۔ ٹولز ایسے کوڈ ہوتے ہیں جنہیں ایجنٹ کسی کارروائی کو انجام دینے کے لیے چلائے سکتا ہے۔ ایک ٹول سادہ فنکشن ہو سکتا ہے جیسے کیلکولیٹر، یا تیسرے فریق کی سروس کے لیے API کال جیسے اسٹاک کی قیمت معلوم کرنا یا موسم کی پیش گوئی۔ AI ایجنٹس کے سیاق و سباق میں، ٹولز اس طریقے کے لیے ڈیزائن کیے جاتے ہیں کہ انہیں **model-generated function calls** کے جواب میں ایجنٹس چلائیں۔

## What are the use cases it can be applied to?

AI Agents پیچیدہ کام مکمل کرنے، معلومات بازیافت کرنے، یا فیصلے کرنے کے لیے ٹولز کا فائدہ اٹھا سکتے ہیں۔ ٹول یوز ڈیزائن پیٹرن اکثر ایسے منظرناموں میں استعمال ہوتا ہے جہاں بیرونی نظاموں کے ساتھ متحرک تعامل کی ضرورت ہوتی ہے، جیسے کہ ڈیٹا بیس، ویب سروسز، یا کوڈ انٹرپریٹرز۔ یہ صلاحیت کئی مختلف استعمال کے کیسز کے لیے مفید ہے جن میں شامل ہیں:

- **Dynamic Information Retrieval:** ایجنٹس بیرونی APIs یا ڈیٹا بیسز سے تازہ ترین ڈیٹا حاصل کر سکتے ہیں (مثلاً، تجزیہ کے لیے SQLite ڈیٹا بیس سے کوئری کرنا، اسٹاک کی قیمتیں یا موسم کی معلومات حاصل کرنا)۔
- **Code Execution and Interpretation:** ایجنٹس ریاضیاتی مسائل حل کرنے، رپورٹس تیار کرنے، یا سیمولیشنز انجام دینے کے لیے کوڈ یا اسکرپٹس چلا سکتے ہیں۔
- **Workflow Automation:** ٹاسک شیڈولرز، ای میل سروسز، یا ڈیٹا پائپ لائنز جیسے ٹولز کو مربوط کر کے دہرائی جانے والی یا کثیر مرحلوں والی ورک فلو کو خود کار بنانا۔
- **Customer Support:** ایجنٹس CRM سسٹمز، ٹکٹنگ پلیٹ فارمز، یا نالج بیسس کے ساتھ تعامل کر کے صارف کے سوالات حل کر سکتے ہیں۔
- **Content Generation and Editing:** ایجنٹس گرامر چیکرز، متن کا خلاصہ نکالنے والے، یا مواد کی حفاظت کے جائزہ کار جیسے ٹولز کا استعمال کر کے مواد بنانے کے کام میں مدد دے سکتے ہیں۔

## What are the elements/building blocks needed to implement the tool use design pattern?

یہ بلڈنگ بلاکس AI ایجنٹ کو بہت سی اقسام کے کام انجام دینے کے قابل بناتے ہیں۔ آئیے Tool Use Design Pattern کو نافذ کرنے کے لیے درکار کلیدی عناصر دیکھتے ہیں:

- **Function/Tool Schemas**: دستیاب ٹولز کی تفصیلی تعریفیں، جن میں فنکشن کا نام، مقصد، درکار پیرامیٹرز، اور متوقع آؤٹ پٹس شامل ہوں۔ یہ اسکیموں سے LLM یہ سمجھ پاتا ہے کہ کون سے ٹولز دستیاب ہیں اور درست درخواستیں کیسے بنائی جائیں۔

- **Function Execution Logic**: اس بات کا تعین کرتی ہے کہ صارف کے ارادے اور گفتگو کے سیاق و سباق کی بنیاد پر ٹولز کو کب اور کیسے بلایا جائے۔ اس میں پلانر ماڈیولز، روٹنگ میکانزم، یا شرطی فلو شامل ہو سکتے ہیں جو متحرک طور پر ٹول کے استعمال کا فیصلہ کرتے ہیں۔

- **Message Handling System**: وہ اجزاء جو صارف کے ان پٹس، LLM جوابات، ٹول کالز، اور ٹول آؤٹ پٹس کے درمیان گفتگونی بہاؤ کو منظم کرتے ہیں۔

- **Tool Integration Framework**: وہ انفراسٹرکچر جو ایجنٹ کو مختلف ٹولز کے ساتھ جوڑتا ہے، چاہے وہ سادہ فنکشنز ہوں یا پیچیدہ بیرونی سروسز۔

- **Error Handling & Validation**: وہ میکانزم جو ٹول کے اجرا میں ناکامیوں کو ہینڈل کرتے ہیں، پیرامیٹرز کی توثیق کرتے ہیں، اور غیر متوقع جوابات کو منظم کرتے ہیں۔

- **State Management**: بات چیت کے سیاق و سباق، پچھلی ٹول انٹریکشنز، اور مستقل ڈیٹا کو ٹریک کرتا ہے تاکہ کثیر موڑ بات چیت میں ہم آہنگی برقرار رہے۔

اب، آئیے Function/Tool Calling کو مزید تفصیل سے دیکھتے ہیں۔
 
### Function/Tool Calling

Function calling وہ بنیادی طریقہ ہے جس کے ذریعے ہم Large Language Models (LLMs) کو ٹولز کے ساتھ تعامل کرنے کے قابل بناتے ہیں۔ آپ اکثر 'Function' اور 'Tool' کو ایک دوسرے کے متبادل کے طور پر دیکھیں گے کیونکہ 'functions' (دوبارہ استعمال کے قابل کوڈ بلاکس) وہ 'tools' ہیں جن کا ایجنٹس استعمال کرتے ہیں۔ کسی فنکشن کے کوڈ کو چلانے کے لیے، ایک LLM کو صارف کی درخواست کو فنکشن کی تفصیل کے ساتھ موازنہ کرنا ہوتا ہے۔ اس کے لیے تمام دستیاب فنکشنز کی تفصیلات پر مشتمل ایک اسکیمہ LLM کو بھیجی جاتی ہے۔ پھر LLM سب سے مناسب فنکشن کا انتخاب کرتا ہے اور اس کا نام اور دلائل واپس کرتا ہے۔ منتخب شدہ فنکشن کو چلایا جاتا ہے، اس کا جواب LLM کو بھیجا جاتا ہے، جو اس معلومات کا استعمال کر کے صارف کی درخواست کا جواب تیار کرتا ہے۔

ڈیولپرز کے لیے ایجنٹس کے لیے فنکشن کالنگ نافذ کرنے کے لیے آپ کو درکار ہوگا:

1. An LLM model that supports function calling
2. A schema containing function descriptions
3. The code for each function described

آئیے شہر میں موجودہ وقت معلوم کرنے کی مثال استعمال کرتے ہیں تاکہ بات واضح ہو:

1. **Initialize an LLM that supports function calling:**

    Not all models support function calling, so it's important to check that the LLM you are using does.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> supports function calling. We can start by initiating the Azure OpenAI client. 

    ```python
    # Azure OpenAI کلائنٹ کو ابتدائی طور پر ترتیب دیں
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Create a Function Schema**:

    Next we will define a JSON schema that contains the function name, description of what the function does, and the names and descriptions of the function parameters.
    We will then take this schema and pass it to the client created previously, along with the users request to find the time in San Francisco. What's important to note is that a **tool call** is what is returned, **not** the final answer to the question. As mentioned earlier, the LLM returns the name of the function it selected for the task, and the arguments that will be passed to it.

    ```python
    # ماڈل کے پڑھنے کے لیے فنکشن کی وضاحت
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
  
    # پہلا API کال: ماڈل سے کہیں کہ اس فنکشن کو استعمال کرے
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
  
1. **The function code required to carry out the task:**

    Now that the LLM has chosen which function needs to be run the code that carries out the task needs to be implemented and executed.
    We can implement the code to get the current time in Python. We will also need to write the code to extract the name and arguments from the response_message to get the final result.

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
  
      # دوسری اے پی آئی کال: ماڈل سے حتمی جواب حاصل کریں
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

Function Calling is at the heart of most, if not all agent tool use design, however implementing it from scratch can sometimes be challenging.
As we learned in [Lesson 2](../../../02-explore-agentic-frameworks) agentic frameworks provide us with pre-built building blocks to implement tool use.
 
## Tool Use Examples with Agentic Frameworks

درج ذیل کچھ مثالیں ہیں کہ آپ مختلف agentic frameworks استعمال کرتے ہوئے Tool Use Design Pattern کو کیسے نافذ کر سکتے ہیں:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> ایک اوپن سورس AI فریم ورک ہے AI ایجنٹس بنانے کے لیے۔ یہ function calling کے استعمال کو آسان بناتا ہے کیونکہ آپ ٹولز کو Python فنکشنز کے طور پر `@tool` ڈی کوریٹر کے ساتھ تعریف کر سکتے ہیں۔ یہ فریم ورک ماڈل اور آپ کے کوڈ کے درمیان بات چیت کو سنبھالتا ہے۔ یہ `AzureAIProjectAgentProvider` کے ذریعے File Search اور Code Interpreter جیسے پیش ساختہ ٹولز تک رسائی بھی فراہم کرتا ہے۔

درج ذیل خاکہ Microsoft Agent Framework کے ساتھ function calling کے عمل کی وضاحت کرتا ہے:

![فنکشن کالنگ](../../../translated_images/ur/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework میں، ٹولز کو سجایا ہوا فنکشنز کے طور پر تعریف کیا جاتا ہے۔ ہم پہلے دیکھے گئے `get_current_time` فنکشن کو `@tool` ڈی کوریٹر استعمال کر کے ایک ٹول میں تبدیل کر سکتے ہیں۔ فریم ورک خود بخود فنکشن اور اس کے پیرامیٹرز کو سیریلائز کر کے LLM کو بھیجنے کے لیے اسکیمہ تیار کر دے گا۔

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

# ایک ایجنٹ بنائیں اور اسے ٹول کے ساتھ چلائیں
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ایک جدید agentic framework ہے جو ڈویلپرز کو محفوظ طریقے سے اعلیٰ معیار کے، قابل توسیع AI ایجنٹس بنانے، ڈیپلائے کرنے، اور اسکیل کرنے کے قابل بناتا ہے بغیر بنیادی کمپیوٹ اور اسٹوریج وسائل کو خود مینیج کیے۔ یہ خاص طور پر انٹرپرائز ایپلیکیشنز کے لیے مفید ہے کیونکہ یہ ایک مکمل مینیجڈ سروس ہے جس میں انٹرپرائز گریڈ سیکیورٹی موجود ہے۔

براہِ راست LLM API کے ساتھ ڈویلپ کرنے کے مقابلے میں، Azure AI Agent Service کچھ فوائد فراہم کرتا ہے، جن میں شامل ہیں:

- Automatic tool calling – اب سرور سائیڈ پر ٹول کال پارس کرنے، ٹول چلانے، اور جواب ہینڈل کرنے کی ضرورت نہیں رہتی۔
- Securely managed data – اپنے بات چیت کی حالت کو خود مینیج کرنے کی بجائے آپ threads پر انحصار کر سکتے ہیں تاکہ تمام مطلوبہ معلومات محفوظ ہوں۔
- Out-of-the-box tools – ایسے ٹولز جو آپ کو آپ کے ڈیٹا سورسز کے ساتھ تعامل کرنے میں مدد دیتے ہیں، جیسے Bing، Azure AI Search، اور Azure Functions۔

Azure AI Agent Service میں دستیاب ٹولز کو دو زمروں میں تقسیم کیا جا سکتا ہے:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ہمیں ان ٹولز کو ایک `toolset` کے طور پر ایک ساتھ استعمال کرنے کی اجازت دیتا ہے۔ یہ `threads` کا استعمال بھی کرتا ہے جو کسی مخصوص گفتگو کی پیغام رسانی کی تاریخ کا ریکارڈ رکھتے ہیں۔

تصور کریں آپ Contoso کمپنی میں ایک سیلز ایجنٹ ہیں۔ آپ ایک conversational agent تیار کرنا چاہتے ہیں جو آپ کے سیلز ڈیٹا کے بارے میں سوالات کے جوابات دے سکے۔

درج ذیل تصویر دکھاتی ہے کہ آپ Azure AI Agent Service کا استعمال کرتے ہوئے اپنے سیلز ڈیٹا کا تجزیہ کیسے کر سکتے ہیں:

![Agentic Service In Action](../../../translated_images/ur/agent-service-in-action.34fb465c9a84659e.webp)

ان ٹولز میں سے کسی کو سروس کے ساتھ استعمال کرنے کے لیے ہم ایک کلائنٹ بنا کر ایک ٹول یا toolset کی تعریف کر سکتے ہیں۔ عملی نفاذ کے لیے ہم درج ذیل Python کوڈ استعمال کر سکتے ہیں۔ LLM toolset کو دیکھ کر فیصلہ کرے گا کہ صارف کی درخواست کے مطابق user created function `fetch_sales_data_using_sqlite_query` استعمال کرے یا پیش ساختہ Code Interpreter۔

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py فائل میں پایا جانے والا fetch_sales_data_using_sqlite_query فنکشن۔
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ٹول سیٹ کو ابتدائی کریں۔
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query فنکشن کے ساتھ فنکشن کال کرنے والا ایجنٹ مرتب کریں اور اسے ٹول سیٹ میں شامل کریں۔
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter ٹول کو مرتب کریں اور اسے ٹول سیٹ میں شامل کریں۔
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## What are the special considerations for using the Tool Use Design Pattern to build trustworthy AI agents?

LLMs کی طرف سے ڈائنامکلی جنریٹ کیے گئے SQL کے حوالے سے ایک عام تشویش سیکیورٹی ہے، خاص طور پر SQL injection یا نقصان دہ اعمال کا خطرہ، جیسے کہ ڈیٹا بیس کو ڈراپ کرنا یا اس میں چھیڑچھاڑ کرنا۔ اگرچہ یہ خدشات جائز ہیں، لیکن انہیں مناسب طریقے سے ڈیٹا بیس ایکسیس پرمشنز ترتیب دے کر مؤثر طریقے سے کم کیا جا سکتا ہے۔ زیادہ تر ڈیٹا بیسز کے لیے یہ عام طور پر ڈیٹا بیس کو read-only کنفیگر کرنے میں شامل ہوتا ہے۔ PostgreSQL یا Azure SQL جیسے ڈیٹا بیس سروسز کے لیے، ایپ کو read-only (SELECT) رول تفویض کیا جانا چاہیے۔

ایپ کو ایک محفوظ ماحول میں چلانے سے حفاظت مزید بہتر ہوتی ہے۔ انٹرپرائز منظرناموں میں، ڈیٹا عام طور پر آپریشنل سسٹمز سے نکالا اور تبدیل کر کے ایک read-only ڈیٹا بیس یا ڈیٹا ویئر ہاؤس میں رکھا جاتا ہے جس کا اسکیمہ صارف دوست ہوتا ہے۔ یہ طریقہ اس بات کو یقینی بناتا ہے کہ ڈیٹا محفوظ ہے، کارکردگی اور قابل رسائی کے لیے بہتر کیا گیا ہے، اور ایپ کو محدود، صرف پڑھنے کی رسائی حاصل ہے۔

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson
[ایجنٹک RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
دستبرداری:
اس دستاویز کا ترجمہ AI ترجمہ سروس Co‑op Translator (https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہِ کرم ذہن میں رکھیں کہ خودکار ترجموں میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مادری زبان میں معتبر ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->