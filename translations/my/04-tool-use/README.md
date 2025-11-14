<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e056335d729ba6e49571db7a6533825d",
  "translation_date": "2025-09-30T07:58:02+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "my"
}
-->
[![How to Design Good AI Agents](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.my.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရန် အထက်ပါ ပုံကို နှိပ်ပါ)_

# Tool Use Design Pattern

Tools သည် AI အေးဂျင့်များကို ပိုမိုကျယ်ပြန့်သော စွမ်းရည်များပေးနိုင်သောကြောင့် စိတ်ဝင်စားဖွယ်ဖြစ်သည်။ အေးဂျင့်သည် လုပ်ဆောင်နိုင်သော လုပ်ဆောင်ချက်များ အကန့်အသတ်ရှိခြင်းမရှိဘဲ tool တစ်ခု ထည့်သွင်းခြင်းဖြင့် အေးဂျင့်သည် လုပ်ဆောင်ချက်များစွာကို လုပ်ဆောင်နိုင်သည်။ ဤအခန်းတွင် AI အေးဂျင့်များသည် သူတို့ရည်မှန်းချက်များကို ရောက်ရှိရန် သတ်မှတ်ထားသော tools များကို ဘယ်လိုအသုံးပြုနိုင်သည်ကို ဖော်ပြထားသော Tool Use Design Pattern ကို လေ့လာပါမည်။

## အကျဉ်းချုပ်

ဤသင်ခန်းစာတွင် ကျွန်ုပ်တို့သည် အောက်ပါမေးခွန်းများကို ဖြေရှင်းရန် ကြိုးစားပါမည်-

- Tool Use Design Pattern ဆိုတာဘာလဲ?
- ၎င်းကို အသုံးချနိုင်သော use cases များက ဘာတွေလဲ?
- Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အစိတ်အပိုင်းများ/အခြေခံအဆောက်အအုံများက ဘာတွေလဲ?
- ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များကို တည်ဆောက်ရန် Tool Use Design Pattern ကို အသုံးပြုရာတွင် အထူးစဉ်းစားရန်အချက်များက ဘာတွေလဲ?

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာကို ပြီးမြောက်ပြီးနောက် သင်သည်-

- Tool Use Design Pattern နှင့် ၎င်း၏ ရည်ရွယ်ချက်ကို သတ်မှတ်နိုင်မည်။
- Tool Use Design Pattern ကို အသုံးချနိုင်သော use cases များကို ဖော်ထုတ်နိုင်မည်။
- Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အဓိကအစိတ်အပိုင်းများကို နားလည်နိုင်မည်။
- Tool Use Design Pattern ကို အသုံးပြုသော AI အေးဂျင့်များတွင် ယုံကြည်စိတ်ချရမှုကို အာမခံရန် စဉ်းစားရန်အချက်များကို သိရှိနိုင်မည်။

## Tool Use Design Pattern ဆိုတာဘာလဲ?

**Tool Use Design Pattern** သည် LLMs ကို အပြင်ပ tools များနှင့် အပြန်အလှန်ဆက်သွယ်နိုင်စွမ်းပေးခြင်းကို အဓိကထားသည်။ Tools ဆိုသည်မှာ အေးဂျင့်များက လုပ်ဆောင်ချက်များကို လုပ်ဆောင်ရန် အသုံးပြုနိုင်သော code ဖြစ်သည်။ Tool တစ်ခုသည် calculator ကဲ့သို့ ရိုးရှင်းသော function ဖြစ်နိုင်သလို၊ stock price lookup သို့မဟုတ် မိုးလေဝသခန့်မှန်းခြေကဲ့သို့ third-party service သို့ API call တစ်ခုလည်း ဖြစ်နိုင်သည်။ AI အေးဂျင့်များ၏ အနက်တွင် tools များကို **model-generated function calls** အဖြစ် အေးဂျင့်များက လုပ်ဆောင်ရန်အတွက် ဒီဇိုင်းထုတ်ထားသည်။

## ၎င်းကို အသုံးချနိုင်သော use cases များက ဘာတွေလဲ?

AI အေးဂျင့်များသည် tools များကို အသုံးပြု၍ ရှုပ်ထွေးသောအလုပ်များကို ပြီးမြောက်စေခြင်း၊ အချက်အလက်များကို ရှာဖွေခြင်း၊ သို့မဟုတ် ဆုံးဖြတ်ချက်များကို ချမှတ်ခြင်းတို့ကို လုပ်ဆောင်နိုင်သည်။ Tool Use Design Pattern ကို databases, web services, သို့မဟုတ် code interpreters ကဲ့သို့ အပြင်ပစနစ်များနှင့် dynamic interaction လိုအပ်သော အခြေအနေများတွင် မကြာခဏ အသုံးပြုသည်။ ၎င်း၏ စွမ်းရည်သည် အောက်ပါ use cases များအတွက် အသုံးဝင်သည်-

- **Dynamic Information Retrieval:** Agents များသည် SQLite database ကို query လုပ်၍ အချက်အလက်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း၊ stock prices သို့မဟုတ် မိုးလေဝသအချက်အလက်များကို ရှာဖွေခြင်းကဲ့သို့ အပြင်ပ APIs သို့မဟုတ် databases ကို query လုပ်နိုင်သည်။
- **Code Execution and Interpretation:** Agents များသည် code သို့မဟုတ် scripts များကို run လုပ်၍ သင်္ချာပြဿနာများကို ဖြေရှင်းခြင်း၊ အစီရင်ခံစာများကို ဖန်တီးခြင်း၊ သို့မဟုတ် simulation များကို လုပ်ဆောင်နိုင်သည်။
- **Workflow Automation:** Task schedulers, email services, သို့မဟုတ် data pipelines ကဲ့သို့ tools များကို ပေါင်းစပ်၍ အလုပ်များကို အလိုအလျောက်လုပ်ဆောင်ခြင်း။
- **Customer Support:** CRM systems, ticketing platforms, သို့မဟုတ် knowledge bases များနှင့် ဆက်သွယ်၍ အသုံးပြုသူမေးခွန်းများကို ဖြေရှင်းခြင်း။
- **Content Generation and Editing:** Grammar checkers, text summarizers, သို့မဟုတ် content safety evaluators ကဲ့သို့ tools များကို အသုံးပြု၍ content ဖန်တီးမှုအလုပ်များကို ကူညီခြင်း။

## Tool Use Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အစိတ်အပိုင်းများက ဘာတွေလဲ?

AI အေးဂျင့်များကို အလုပ်အမျိုးမျိုးကို လုပ်ဆောင်နိုင်စွမ်းပေးသော အစိတ်အပိုင်းများကို လိုအပ်သည်။ Tool Use Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အဓိကအစိတ်အပိုင်းများကို ကြည့်ကြပါစို့-

- **Function/Tool Schemas**: အသုံးပြုနိုင်သော tools များ၏ အသေးစိတ်ဖော်ပြချက်များ၊ function name, ရည်ရွယ်ချက်, လိုအပ်သော parameters, နှင့် မျှော်မှန်းထားသော outputs အပါအဝင်။ ၎င်းတို့သည် LLM ကို tools များရရှိနိုင်မှုနှင့် valid requests များကို ဖန်တီးပုံကို နားလည်စေသည်။
- **Function Execution Logic**: အသုံးပြုသူ၏ ရည်ရွယ်ချက်နှင့် စကားဝိုင်းအကြောင်းအရာအပေါ် မူတည်၍ tools များကို ဘယ်အချိန်တွင်၊ ဘယ်လို invoke လုပ်မည်ကို စီမံခန့်ခွဲသည်။
- **Message Handling System**: အသုံးပြုသူ input, LLM response, tool calls, နှင့် tool outputs အကြား စကားဝိုင်းလှည့်ပတ်မှုကို စီမံခန့်ခွဲသော components များ။
- **Tool Integration Framework**: ရိုးရှင်းသော functions များမှစ၍ ရှုပ်ထွေးသော အပြင်ပ services များအထိ အေးဂျင့်ကို tools များနှင့် ချိတ်ဆက်ပေးသော အဆောက်အအုံ။
- **Error Handling & Validation**: Tool execution တွင် ဖြစ်ပေါ်သော အဆင်မပြေမှုများကို ကိုင်တွယ်ခြင်း၊ parameters များကို validate လုပ်ခြင်း၊ နှင့် မမျှော်လင့်ထားသော response များကို စီမံခန့်ခွဲခြင်း။
- **State Management**: စကားဝိုင်းအကြောင်းအရာ, ယခင် tool interactions, နှင့် multi-turn interactions အတွင်းတွင် တိကျမှုရှိစေရန် အဆက်အသွယ်ရှိသော data များကို ထိန်းသိမ်းခြင်း။

အခုတော့ Function/Tool Calling ကို ပိုမိုအသေးစိတ်ကြည့်ကြပါစို့။

### Function/Tool Calling

Function calling သည် Large Language Models (LLMs) များကို tools များနှင့် ဆက်သွယ်စေသော အဓိကနည်းလမ်းဖြစ်သည်။ 'Function' နှင့် 'Tool' ကို အပြန်အလှန်အသုံးပြုသောကြောင့် 'functions' (အသုံးပြုနိုင်သော code blocks) သည် အေးဂျင့်များအတွက် tasks များကို လုပ်ဆောင်ရန် အသုံးပြုသော 'tools' ဖြစ်သည်။ Function code ကို invoke လုပ်ရန်အတွက် LLM သည် အသုံးပြုသူ၏ တောင်းဆိုမှုကို function description နှင့် နှိုင်းယှဉ်ရမည်။ Function description များပါရှိသော schema ကို LLM သို့ ပေးပို့ပြီး LLM သည် task အတွက် အကောင်းဆုံး function ကို ရွေးချယ်ပြီး ၎င်း၏ name နှင့် arguments ကို ပြန်ပေးသည်။ ရွေးချယ်ထားသော function ကို invoke လုပ်ပြီး ၎င်း၏ response ကို LLM သို့ ပြန်ပေးပြီး အသုံးပြုသူ၏ တောင်းဆိုမှုကို ဖြေရှင်းရန် အသုံးပြုသည်။

Function calling ကို အေးဂျင့်များအတွက် အကောင်အထည်ဖော်ရန် developer များအတွက် လိုအပ်သည်မှာ-

1. Function calling ကို support လုပ်သော LLM model
2. Function descriptions ပါရှိသော schema
3. ဖော်ပြထားသော function တစ်ခုချင်းစီ၏ code

San Francisco မြို့၏ လက်ရှိအချိန်ကို ရယူရန် ဥပမာကို အသုံးပြုကြည့်ပါစို့-

1. **Function calling ကို support လုပ်သော LLM ကို initialize လုပ်ပါ:**

    Function calling ကို support မလုပ်သော models များလည်း ရှိနိုင်သဖြင့် သင်အသုံးပြုနေသော LLM ကို function calling ကို support လုပ်မလုပ် စစ်ဆေးရန် အရေးကြီးသည်။ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> သည် function calling ကို support လုပ်သည်။ Azure OpenAI client ကို initiate လုပ်ခြင်းဖြင့် စတင်နိုင်သည်။

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Function Schema တစ်ခု ဖန်တီးပါ:**

    နောက်တစ်ဆင့်မှာ function name, function ၏ description, နှင့် function parameters ၏ name နှင့် description များပါရှိသော JSON schema ကို သတ်မှတ်ပါမည်။ ၎င်း schema ကို ယခင် client နှင့် users request (ဥပမာ- San Francisco ၏ အချိန်ကို ရှာဖွေခြင်း) နှင့်အတူ ပေးပို့ပါမည်။ အရေးကြီးသောအချက်မှာ **tool call** သည် ပြန်ပေးသည့်အဖြေဖြစ်ပြီး **မေးခွန်း၏ နောက်ဆုံးအဖြေ** မဟုတ်ပါ။ အထက်တွင် ဖော်ပြခဲ့သည့်အတိုင်း LLM သည် task အတွက် ရွေးချယ်ထားသော function name နှင့် ၎င်းကို pass လုပ်မည့် arguments ကို ပြန်ပေးသည်။

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
  
1. **Task ကို လုပ်ဆောင်ရန် လိုအပ်သော function code:**

    LLM သည် run လုပ်ရန်လိုအပ်သော function ကို ရွေးချယ်ပြီးနောက် task ကို လုပ်ဆောင်ရန် code ကို implement လုပ်ပြီး run လုပ်ရန်လိုအပ်သည်။ Python ကို အသုံးပြု၍ လက်ရှိအချိန်ကို ရယူရန် code ကို implement လုပ်နိုင်သည်။ response_message မှ function name နှင့် arguments ကို extract လုပ်ရန် code ကိုလည်း ရေးသားရန်လိုအပ်သည်။

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

Function Calling သည် အေးဂျင့် tool use design အများစု၏ အဓိကဖြစ်သော်လည်း အခြေခံမှစ၍ ၎င်းကို အကောင်အထည်ဖော်ခြင်းသည် တစ်ခါတစ်ရံ အခက်အခဲဖြစ်နိုင်သည်။
[Lesson 2](../../../02-explore-agentic-frameworks) တွင် သင်ယူခဲ့သည့်အတိုင်း agentic frameworks များသည် tool use ကို အကောင်အထည်ဖော်ရန် pre-built building blocks များကို ပေးသည်။

## Agentic Frameworks များနှင့် Tool Use Examples

Agentic frameworks များကို အသုံးပြု၍ Tool Use Design Pattern ကို အကောင်အထည်ဖော်နိုင်သော ဥပမာများကို ကြည့်ပါစို့-

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> သည် Large Language Models (LLMs) နှင့်အလုပ်လုပ်နေသော .NET, Python, နှင့် Java developer များအတွက် open-source AI framework ဖြစ်သည်။ ၎င်းသည် function calling ကို အသုံးပြုခြင်းလုပ်ငန်းစဉ်ကို function များနှင့် ၎င်းတို့၏ parameters ကို model သို့ အလိုအလျောက် ဖော်ပြပေးခြင်းဖြင့် လွယ်ကူစေသည်။ ၎င်းသည် model နှင့် သင့် code အကြား communication ကို handle လုပ်ပေးသည်။ Semantic Kernel ကဲ့သို့ agentic framework ကို အသုံးပြုခြင်း၏ အခြားတစ်ခု advantage ကတော့ <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> နှင့် <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a> ကဲ့သို့ pre-built tools များကို access လုပ်နိုင်ခြင်းဖြစ်သည်။

အောက်ပါ diagram သည် Semantic Kernel နှင့် function calling လုပ်ငန်းစဉ်ကို ဖော်ပြသည်-

![function calling](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.my.png)

Semantic Kernel တွင် functions/tools များကို <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> ဟုခေါ်သည်။ ယခင် `get_current_time` function ကို class အဖြစ် ပြောင်းလဲပြီး plugin အဖြစ် အသုံးပြုနိုင်သည်။ `kernel_function` decorator ကို import လုပ်ပြီး function ၏ description ကို ထည့်သွင်းနိုင်သည်။ GetCurrentTimePlugin ဖြင့် kernel တစ်ခုကို ဖန်တီးသောအခါ kernel သည် function နှင့် ၎င်း၏ parameters ကို အလိုအလျောက် serialize လုပ်ပြီး schema ကို ဖန်တီးကာ LLM သို့ ပေးပို့သည်။

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
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> သည် developer များကို compute နှင့် storage resources ကို စီမံခန့်ခွဲရန် မလိုအပ်ဘဲ ယုံကြည်စိတ်ချရသော extensible AI agents များကို securely build, deploy, နှင့် scale လုပ်ရန် အခွင့်အလမ်းပေးသော agentic framework အသစ်ဖြစ်သည်။ ၎င်းသည် enterprise grade security ရှိသော fully managed service ဖြစ်သောကြောင့် enterprise applications များအတွက် အထူးအသုံးဝင်သည်။

LLM API ကို တိုက်ရိုက် အသုံးပြုခြင်းနှင့် နှိုင်းယှဉ်ပါက Azure AI Agent Service သည် အချို့သော အားသာချက်များကို ပေးသည်၊ ၎င်းမှာ-

- Automatic tool calling – tool call ကို parse လုပ်ရန်၊ tool ကို invoke လုပ်ရန်၊ response ကို handle လုပ်ရန် မလိုအပ်တော့ဘဲ server-side တွင် အားလုံးကို လုပ်ဆောင်ပေးသည်။
- Securely managed data – conversation state ကို ကိုယ်တိုင် စီမံရန်မလိုအပ်တော့ဘဲ threads ကို အသုံးပြု၍ လိုအပ်သော အချက်အလက်အားလုံးကို သိမ်းဆည်းနိုင်သည်။
- Out-of-the-box tools – Bing, Azure AI Search, နှင့် Azure Functions ကဲ့သို့ data sources များနှင့် interaction လုပ်ရန် အသုံးပြုနိုင်သော tools များ။

Azure AI Agent Service တွင် ရရှိနိုင်သော tools များကို အောက်ပါအတိုင်း အမျိုးအစားနှစ်မျိုးခွဲနိုင်သည်-

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how
အက်ဥ်းချုပ် - အက်ပ်ကို လုံခြုံသောပတ်ဝန်းကျင်တွင် အလုပ်လုပ်စေခြင်းသည် ကာကွယ်မှုကို ပိုမိုတိုးမြှင့်ပေးနိုင်သည်။ စီးပွားရေးလုပ်ငန်းများတွင် အချက်အလက်များကို လုပ်ငန်းစဉ်များမှ ထုတ်ယူပြီး အသုံးပြုရလွယ်ကူသော schema ပါရှိသော ဖတ်ရှုနိုင်သော database သို့မဟုတ် data warehouse သို့ ပြောင်းလဲသိမ်းဆည်းလေ့ရှိသည်။ ဒီနည်းလမ်းက အချက်အလက်များကို လုံခြုံစေပြီး၊ စွမ်းဆောင်ရည်နှင့် အသုံးပြုနိုင်မှုအတွက် အကောင်းဆုံးဖြစ်စေပြီး၊ အက်ပ်ကို ဖတ်ရှုနိုင်မှုသာရှိသော အခွင့်အာဏာပေးထားသည်။

### Tool Use Design Patterns အကြောင်း ပိုမိုသိချင်ပါသလား?

အခြားလေ့လာသူများနှင့် တွေ့ဆုံရန်၊ office hours တွင် ပါဝင်ရန်၊ သင့် AI Agents အကြောင်းမေးခွန်းများကို ဖြေရှင်းရန် [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ကို ဝင်ရောက်ပါ။

## အပိုဆောင်း အရင်းအမြစ်များ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## ယခင် သင်ခန်းစာ

[Agentic Design Patterns ကို နားလည်ခြင်း](../03-agentic-design-patterns/README.md)

## နောက်သင်ခန်းစာ

[Agentic RAG](../05-agentic-rag/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြု၍ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။