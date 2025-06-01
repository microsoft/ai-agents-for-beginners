[![ကောင်းမွန်သော AI Agents များကို ဒီဇိုင်းပြုလုပ်နည်း](./images/lesson-4-thumbnail.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)
> *(ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရှုရန် အထက်ပါ ပုံကို နှိပ်ပါ)*

# Tool Use ဒီဇိုင်းပတ်တန်း

Tools များသည် AI agents များအတွက် ပိုမိုကျယ်ပြန့်သော လုပ်ဆောင်နိုင်စွမ်းများရရှိစေသောကြောင့် စိတ်ဝင်စားဖွယ်ရာများဖြစ်သည်။ Agent သည် ကန့်သတ်ထားသော လုပ်ဆောင်ချက်များကိုသာ လုပ်ဆောင်နိုင်မည့်အစား၊ tool တစ်ခုထည့်သွင်းခြင်းအားဖြင့် agent သည် ကျယ်ပြန့်သော လုပ်ဆောင်ချက်များကို လုပ်ဆောင်နိုင်လာမည်။ ဤအခန်းတွင် AI agents များသည် ၎င်းတို့၏ ရည်မှန်းချက်များအောင်မြင်ရန် သီးခြား tools များကို မည်သို့အသုံးပြုကြသည်ကို ဖော်ပြသည့် Tool Use Design Pattern ကို လေ့လာမည်ဖြစ်သည်။

## နိဒါန်း

ဤသင်ခန်းစာတွင် အောက်ပါမေးခွန်းများကို ဖြေရှင်းမည်ဖြစ်သည်-

- Tool use design pattern ဆိုသည်မှာ အဘယ်နည်း။
- မည်သည့်အသုံးပြုမှုများတွင် အသုံးချနိုင်သည်နည်း။
- Design pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော element/building blocks များမှာ အဘယ်နည်း။
- ယုံကြည်ရသော AI agents များတည်ဆောက်ရန် Tool Use Design Pattern ကို အသုံးပြုရာတွင် အထူးထည့်သွင်းစဉ်းစားရမည့်အချက်များမှာ အဘယ်နည်း။

## သင်ယူရမည့်ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးစီးပြီးနောက် သင်သည်-

- Tool Use Design Pattern နှင့် ၎င်း၏ရည်ရွယ်ချက်ကို သတ်မှတ်နိုင်မည်။
- Tool Use Design Pattern ကို အသုံးချနိုင်သော use cases များကို ခွဲခြားသတ်မှတ်နိုင်မည်။
- Design pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အဓိက elements များကို နားလည်မည်။
- ဤ design pattern ကို အသုံးပြု၍ AI agents များတွင် ယုံကြည်စိတ်ချရမှုကို သေချာစေရန် ထည့်သွင်းစဉ်းစားရမည့်အချက်များကို သတ်မှတ်နိုင်မည်။

## Tool Use Design Pattern ဆိုသည်မှာ အဘယ်နည်း။

**Tool Use Design Pattern** သည် LLMs များကို သီးခြား ရည်မှန်းချက်များအောင်မြင်ရန်အတွက် ပြင်ပ tools များနှင့် ပြန်လည်တုံ့ပြန်နိုင်စွမ်းကို ပေးအပ်ရန် အာရုံစိုက်သည်။ Tools များသည် agent တစ်ခုမှ လုပ်ဆောင်ချက်များ လုပ်ဆောင်ရန်အတွက် လုပ်ဆောင်နိုင်သော ကုဒ်များဖြစ်သည်။ Tool တစ်ခုသည် calculator ကဲ့သို့ ရိုးရှင်းသော function တစ်ခု သို့မဟုတ် stock price ကိုရှာခြင်း သို့မဟုတ် ရာသီဥတုခန့်မှန်းချက် စသည့် တတိယပါတီ service တစ်ခုသို့ API call တစ်ခုဖြစ်နိုင်သည်။ AI agents များ၏ နေရာတွင် tools များသည် **model-generated function calls** များအတွက် agents များမှ လုပ်ဆောင်ရန် ဒီဇိုင်းထုတ်ထားပါသည်။

## မည်သည့်အသုံးပြုမှုများတွင် အသုံးချနိုင်သည်နည်း။

AI Agents များသည် ရှုပ်ထွေးသော လုပ်ငန်းများကို ပြီးစီးစေရန်၊ အချက်အလက်များကို ရယူရန် သို့မဟုတ် ဆုံးဖြတ်ချက်များချရန်အတွက် tools များကို အသုံးပြုနိုင်သည်။ Tool use design pattern ကို ဒေတာဘေ့စ်များ၊ web services များ သို့မဟုတ် code interpreters များကဲ့သို့သော ပြင်ပစနစ်များနှင့် ပြောင်းလဲနိုင်သော အပြန်အလှန် လုပ်ဆောင်မှုများ လိုအပ်သော အခြေအနေများတွင် မကြာခဏ အသုံးပြုကြသည်။ ဤစွမ်းရည်သည် အောက်ပါအသုံးပြုမှုများအပါအဝင် အမျိုးမျိုးသော အခြေအနေများတွင် အသုံးဝင်သည်-

- **ပြောင်းလဲနိုင်သော သတင်းအချက်အလက်ရယူခြင်း:** Agents များသည် နောက်ဆုံးရ အချက်အလက်များရယူရန်အတွက် ပြင်ပ APIs သို့မဟုတ် databases များကို မေးမြန်းနိုင်သည် (ဥပမာ- ဒေတာခွဲခြမ်းစိတ်ဖြာမှုအတွက် SQLite database ကို မေးမြန်းခြင်း၊ stock စျေးနှုန်းများ သို့မဟုတ် ရာသီဥတုအချက်အလက်များ ရယူခြင်း)။
- **ကုဒ်လုပ်ဆောင်ခြင်းနှင့် အဓိပ္ပာယ်ပြန်ခွင်းခြင်း:** Agents များသည် သင်္ချာပြဿနာများ ဖြေရှင်းရန်၊ အစီရင်ခံစာများ ထုတ်လုပ်ရန် သို့မဟုတ် simulation များ လုပ်ဆောင်ရန်အတွက် ကုဒ် သို့မဟုတ် scripts များကို လုပ်ဆောင်နိုင်သည်။
- **လုပ်ငန်းဆင်းတန်း အလိုအလျောက်လုပ်ဆောင်ခြင်း:** Task schedulers၊ email services သို့မဟုတ် data pipelines ကဲ့သို့သော tools များကို ပေါင်းစပ်ခြင်းအားဖြင့် ထပ်ခါထပ်ခါ သို့မဟုတ် အဆင့်များစွာပါသော လုပ်ငန်းဆင်းတန်းများကို အလိုအလျောက်လုပ်ဆောင်ခြင်း။
- **ဖောက်သည်ပံ့ပိုးမှု:** Agents များသည် အသုံးပြုသူများ၏ မေးခွန်းများကို ဖြေရှင်းရန်အတွက် CRM စနစ်များ၊ ticketing platforms များ သို့မဟုတ် knowledge bases များနှင့် အပြန်အလှန်လုပ်ဆောင်နိုင်သည်။
- **အကြောင်းအရာထုတ်လုပ်ခြင်းနှင့် တည်းဖြတ်ခြင်း:** Agents များသည် အကြောင်းအရာဖန်တီးရေး လုပ်ငန်းများတွင် အကူအညီပေးရန်အတွက် grammar checkers၊ text summarizers သို့မဟုတ် content safety evaluators ကဲ့သို့သော tools များကို အသုံးပြုနိုင်သည်။

## Tool use design pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော elements/building blocks များမှာ အဘယ်နည်း။

ဤ building blocks များသည် AI agent အား ကျယ်ပြန့်သော လုပ်ငန်းများကို လုပ်ဆောင်ခွင့်ပြုသည်။ Tool Use Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အဓိက elements များကို လေ့လာကြည့်ကြပါစို့-

- **Function/Tool Schemas**: အသုံးပြုနိုင်သော tools များ၏ အသေးစိတ်သတ်မှတ်ချက်များ၊ function အမည်၊ ရည်ရွယ်ချက်၊ လိုအပ်သော parameters များနှင့် မျှော်လင့်ထားသော outputs များအပါအဝင်။ ဤ schemas များသည် LLM အား အသုံးပြုနိုင်သော tools များနှင့် မှန်ကန်သော requests များ တည်ဆောက်နည်းကို နားလည်စေသည်။

- **Function Execution Logic**: အသုံးပြုသူ၏ ရည်ရွယ်ချက်နှင့် စကားပြောဆိုမှု context အပေါ်အခြေခံ၍ tools များကို မည်သို့နှင့် မည်သောအချိန်တွင် invoke လုပ်ရမည်ကို ထိန်းချုပ်သည်။ ၎င်းတွင် planner modules၊ routing mechanisms သို့မဟုတ် tool အသုံးပြုမှုကို ပြောင်းလဲနိုင်စွာ ဆုံးဖြတ်သည့် conditional flows များ ပါဝင်နိုင်သည်။

- **Message Handling System**: အသုံးပြုသူ inputs၊ LLM responses၊ tool calls နှင့် tool outputs များကြား စကားပြောဆိုမှု လုပ်ငန်းစဉ်ကို စီမံခန့်ခွဲသော အစိတ်အပိုင်းများ။

- **Tool Integration Framework**: Agent ကို ရိုးရှင်းသော functions များဖြစ်စေ၊ ရှုပ်ထွေးသော ပြင်ပ services များဖြစ်စေ အမျိုးမျိုးသော tools များနှင့် ချိတ်ဆက်သည့် အခြေခံ အဆောက်အအုံ။

- **Error Handling & Validation**: Tool execution တွင် ပျက်စီးမှုများကို ကိုင်တွယ်ရန်၊ parameters များကို တရားဝင်စစ်ဆေးရန်နှင့် မမျှော်လင့်ထားသော responses များကို စီမံခန့်ခွဲရန် နည်းလမ်းများ။

- **State Management**: Multi-turn interactions များတွင် တသမတ်တည်းဖြစ်စေရန်အတွက် စကားပြောဆိုမှု context၊ ယခင် tool interactions များနှင့် ထာဝရ data များကို ကြေးမုံရေးသေရင်းခြင်း။

နောက်တွင် Function/Tool Calling ကို အသေးစိတ်လေ့လာကြည့်ကြပါစို့။

### Function/Tool Calling

Function calling သည် Large Language Models (LLMs) များကို tools များနှင့် ပြန်လည်တုံ့ပြန်စေရန် ကျွန်ုပ်တို့အသုံးပြုသည့် အဓိက နည်းလမ်းဖြစ်သည်။ 'Function' နှင့် 'Tool' ကို အပြန်အလှန်အသုံးပြုသည်ကို သင်မကြာခဏတွေ့ရမည်ဖြစ်သည်၊ အဘယ်ကြောင့်ဆိုသော် 'functions' (ပြန်လည်အသုံးပြုနိုင်သော code blocks) များသည် agents များမှ လုပ်ငန်းများ လုပ်ဆောင်ရန်အတွက် အသုံးပြုသည့် 'tools' များဖြစ်သောကြောင့်ဖြစ်သည်။ Function ၏ code ကို invoke လုပ်ရန်အတွက် LLM သည် အသုံးပြုသူ၏ တောင်းဆိုမှုကို functions ၏ ဖော်ပြချက်နှင့် နှိုင်းယှဉ်ရမည်။ ၎င်းကို လုပ်ဆောင်ရန်အတွက် အသုံးပြုနိုင်သော functions အားလုံး၏ ဖော်ပြချက်များပါသော schema တစ်ခုကို LLM သို့ ပို့ပေးသည်။ ထို့နောက် LLM သည် လုပ်ငန်းအတွက် အသင့်လျော်ဆုံး function ကို ရွေးချယ်ပြီး ၎င်း၏ အမည်နှင့် arguments များကို ပြန်ပေးသည်။ ရွေးချယ်ထားသော function ကို invoke လုပ်ပြီး ၎င်း၏ response ကို LLM သို့ ပြန်ပို့ပေးသည်၊ ထို့နောက် LLM သည် အသုံးပြုသူ၏ တောင်းဆိုမှုကို ဖြေကြားရန်အတွက် ထိုအချက်အလက်ကို အသုံးပြုသည်။

Developers များသည် agents များအတွက် function calling ကို အကောင်အထည်ဖော်ရန်အတွက် အောက်ပါအရာများ လိုအပ်မည်-

1. Function calling ကို ပံ့ပိုးသော LLM model တစ်ခု
2. Function descriptions များပါသော schema တစ်ခု
3. ဖော်ပြထားသော function တစ်ခုချင်းစီအတွက် code

မြို့တစ်မြို့တွင် လက်ရှိအချိန်ကို ရယူခြင်း၏ ဥပမာကို အသုံးပြုပြီး သရုပ်ဖော်ကြည့်ကြပါစို့-

1. **Function calling ကို ပံ့ပိုးသော LLM တစ်ခုကို စတင်ခြင်း:**

    Model အားလုံးသည် function calling ကို ပံ့ပိုးမှုမရှိသောကြောင့် သင်အသုံးပြုနေသော LLM သည် ပံ့ပိုးမှုရှိမရှိ စစ်ဆေးရန် အရေးကြီးပါသည်။ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> သည် function calling ကို ပံ့ပိုးပါသည်။ ကျွန်ုပ်တို့သည် Azure OpenAI client ကို စတင်ခြင်းအားဖြင့် စတင်နိုင်ပါသည်။

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **Function Schema တစ်ခု ဖန်တီးခြင်း:**

    နောက်ပိုင်းတွင် ကျွန်ုပ်တို့သည် function အမည်၊ function လုပ်ဆောင်သည့်အရာ၏ ဖော်ပြချက်နှင့် function parameters များ၏ အမည်များနှင့် ဖော်ပြချက်များပါသော JSON schema တစ်ခုကို သတ်မှတ်မည်ဖြစ်သည်။
    ထို့နောက် ကျွန်ုပ်တို့သည် ဤ schema ကို ယခင်တွင်ဖန်တီးထားသော client သို့ pass လုပ်ပြီး San Francisco တွင် အချိန်ရှာရန် အသုံးပြုသူ၏ တောင်းဆိုမှုနှင့်အတူ ပေးပို့မည်ဖြစ်သည်။ အရေးကြီးသည်မှာ **tool call** သည် ပြန်ပေးမည့်အရာဖြစ်ပြီး မေးခွန်း၏ နောက်ဆုံးအဖြေ **မဟုတ်**ပါ။ အစောပိုင်းတွင် ဖော်ပြခဲ့သည့်အတိုင်း LLM သည် လုပ်ငန်းအတွက် ရွေးချယ်ထားသော function ၏ အမည်နှင့် ၎င်းသို့ ပေးပို့မည့် arguments များကို ပြန်ပေးသည်။

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

3. **လုပ်ငန်းကို လုပ်ဆောင်ရန် လိုအပ်သော function code:**

    LLM သည် မည်သည့် function ကို run လုပ်ရမည်ကို ရွေးချယ်ပြီးပြီးနောက် လုပ်ငန်းကို လုပ်ဆောင်သော code ကို အကောင်အထည်ဖော်ပြီး လုပ်ဆောင်ရန် လိုအပ်သည်။
    ကျွန်ုပ်တို့သည် Python တွင် လက်ရှိအချိန်ကို ရယူသော code ကို အကောင်အထည်ဖော်နိုင်ပါသည်။ နောက်ဆုံးရလဒ်ကို ရရှိရန်အတွက် response_message မှ အမည်နှင့် arguments များကို ထုတ်ယူသော code ကိုလည်း ရေးရန် လိုအပ်မည်ဖြစ်သည်။

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

Function Calling သည် အများစု၊ သို့မဟုတ် agent tool use design အားလုံး၏ နှလုံးသားဖြစ်သည်၊ သို့သော် ၎င်းကို အစမှ အကောင်အထည်ဖော်ခြင်းသည် တစ်ခါတစ်ရံ စိန်ခေါ်မှုများ ရှိနိုင်သည်။
[Lesson 2](../02-explore-agentic-frameworks/) တွင် သင်ယူခဲ့သည့်အတိုင်း agentic frameworks များသည် tool use ကို အကောင်အထည်ဖော်ရန်အတွက် ကြိုတင်တည်ဆောက်ထားသော building blocks များကို ပေးပါသည်။

## Agentic Frameworks များနှင့် Tool Use ဥပမာများ

Tool Use Design Pattern ကို အမျိုးမျိုးသော agentic frameworks များအသုံးပြု၍ မည်သို့ အကောင်အထည်ဖော်နိုင်သည်ကို ဥပမာအချို့ ဖော်ပြပါမည်-

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> သည် Large Language Models (LLMs) များနှင့် လုပ်ဆောင်နေသော .NET၊ Python နှင့် Java developers များအတွက် open-source AI framework တစ်ခုဖြစ်သည်။ ၎င်းသည် <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a> ဟုခေါ်သော လုပ်ငန်းစဉ်အားဖြင့် သင်၏ functions များနှင့် ၎င်းတို့၏ parameters များကို model သို့ အလိုအလျောက် ဖော်ပြခြင်းအားဖြင့် function calling အသုံးပြုခြင်း လုပ်ငန်းစဉ်ကို ရိုးရှင်းစေသည်။ ၎င်းသည် model နှင့် သင်၏ code ကြား အပြန်အလှန် ဆက်သွယ်မှုကိုလည်း ကိုင်တွယ်သည်။ Semantic Kernel ကဲ့သို့သော agentic framework အသုံးပြုခြင်း၏ နောက်ထပ် အားသာချက်မှာ <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> နှင့် <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a> ကဲ့သို့သော ကြိုတင်တည်ဆောက်ထားသော tools များကို အသုံးပြုနိုင်ခြင်းဖြစ်သည်။

အောက်ပါ diagram သည် Semantic Kernel နှင့် function calling လုပ်ငန်းစဉ်ကို သရုပ်ဖော်ပြသသည်-

![function calling](./images/functioncalling-diagram.png)

Semantic Kernel တွင် functions/tools များကို <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> ဟုခေါ်သည်။ ကျွန်ုပ်တို့သည် အစောပိုင်းတွင် တွေ့ခဲ့သော `get_current_time` function ကို plugin အဖြစ် ပြောင်းလဲနိုင်သည်၊ ၎င်းကို function ပါသော class တစ်ခုအဖြစ် ပြောင်းလဲခြင်းအားဖြင့်ဖြစ်သည်။ ကျွန်ုပ်တို့သည် function ၏ ဖော်ပြချက်ကို ယူသော `kernel_function` decorator ကိုလည်း import လုပ်နိုင်သည်။ သင်သည် GetCurrentTimePlugin နှင့်အတူ kernel တစ်ခုဖန်တီးသောအခါ kernel သည် function နှင့် ၎င်း၏ parameters များကို အလိုအလျောက် serialize လုပ်ပြီး လုပ်ငန်းစဉ်တွင် LLM သို့ပို့ရန် schema ကို ဖန်တီးမည်ဖြစ်သည်။

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> သည် developers များအား အရည်အသွေးမြင့်နှင့် တိုးချဲ့နိုင်သော AI agents များကို လုံခြုံစွာ တည်ဆောက်၊ deploy လုပ်ပြီး တိုးချဲ့ရန် အခြေခံ compute နှင့် storage resources များကို စီမံခန့်ခွဲရန် မလိုအပ်ဘဲ စွမ်းအားပေးရန် ဒီဇိုင်းထုတ်ထားသော ပိုမိုသစ်လွင်သော agentic framework တစ်ခုဖြစ်သည်။ ၎င်းသည် enterprise အဆင့် လုံခြုံရေးရှိသော အပြည့်အ၀ စီမံခန့်ခွဲသော service ဖြစ်သောကြောင့် enterprise applications များအတွက် အထူးအသုံးဝင်သည်။

LLM API နှင့် တိုက်ရိုက် develop လုပ်ခြင်းနှင့် နှိုင်းယှဉ်သောအခါ Azure AI Agent Service သည် အောက်ပါ အားသာချက်များကို ပေးသည်-

- Automatic tool calling – tool call ကို parse လုပ်ခြင်း၊ tool ကို invoke လုပ်ခြင်းနှင့် response ကို ကိုင်တွယ်ခြင်း မလိုအပ်ဘဲ ဤအရာများအားလუံးကို server-side တွင် လုပ်ဆောင်မည်
- Securely managed data – သင်၏ကိုယ်ပိုင် conversation state ကို စီမံခန့်ခွဲမည့်အစား၊ လိုအပ်သော အချက်အလက်အားလုံးကို သိမ်းဆည်းရန်အတွက် threads များကို အသုံးပြုနိုင်မည်
- Out-of-the-box tools – Bing၊ Azure AI Search နှင့် Azure Functions ကဲ့သို့သော သင်၏ data sources များနှင့် ပြန်လည်တုံ့ပြန်ရန်အတွက် အသုံးပြုနိုင်သော Tools များ။

Azure AI Agent Service တွင် အသုံးပြုနိုင်သော tools များကို အမျိုးအစား နှစ်မျိုးခွဲနိုင်သည်-

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service သည် ဤ tools များကို `toolset` အဖြစ် အတူတကွ အသုံးပြုနိုင်ခွင့်ပြုသည်။ ၎င်းသည် သီးခြား စကားပြောဆိုမှုတစ်ခုမှ messages များ၏ သမိုင်းကြောင်းကို ကြေးမုံထားသော `threads` များကိုလည်း အသုံးပြုသည်။

သင်သည် Contoso ဟုခေါ်သော ကုမ္ပဏီတစ်ခုတွင် sales agent တစ်ယောက်ဖြစ်သည်ဟု မြင်ယောင်ကြည့်ပါ။ သင်သည် သင်၏ sales data နှင့်ပတ်သက်သော မေးခွန်းများကို ဖြေကြားနိုင်သော စကားပြောဆိုမှု agent တစ်ခုကို ဖွံ့ဖြိုးတည်ဆောက်လိုပါသည်။

အောက်ပါ ပုံသည် သင်၏ sales data ကို ခွဲခြမ်းစိတ်ဖြာရန်အတွက် Azure AI Agent Service ကို မည်သို့အသုံးပြုနိုင်သည်ကို သရုပ်ဖော်ပြသသည်-

![Agentic Service In Action](./images/agent-service-in-action.jpg)

Service နှင့်အတူ ဤ tools များအားလုံးကို အသုံးပြုရန်အတွက် ကျွန်ုပ်တို့သည် client တစ်ခုဖန်တီးပြီး tool သို့မဟုတ် toolset တစ်ခုကို သတ်မှတ်နိုင်သည်။ ၎င်းကို လက်တွေ့အားဖြင့် အကောင်အထည်ဖော်ရန် အောက်ပါ Python code ကို အသုံးပြုနိုင်သည်။ LLM သည် toolset ကို ကြည့်ပြီး အသုံးပြုသူ၏ တောင်းဆိုမှုပေါ်မူတည်၍ အသုံးပြုသူဖန်တီးထားသော function ဖြစ်သော `fetch_sales_data_using_sqlite_query` ကို အသုံးပြုမည်လား သို့မဟုတ် ကြိုတင်တည်ဆောက်ထားသော Code Interpreter ကို အသုံးပြုမည်လား ဆုံးဖြတ်နိုင်မည်ဖြစ်သည်။

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fecth_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
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

## ယုံကြည်ရသော AI agents များတည်ဆောက်ရန်အတွက် Tool Use Design Pattern ကို အသုံးပြုရာတွင် အထူးထည့်သွင်းစဉ်းစားရမည့်အချက်များမှာ အဘယ်နည်း။

LLMs များမှ ပြောင်းလဲနိုင်စွာ ထုတ်လုပ်သော SQL နှင့်ပတ်သက်သော ယေဘုယျ စိုးရိမ်မှုမှာ လုံခြုံရေးဖြစ်သည်၊ အထူးသဖြင့် SQL injection သို့မဟုတ် database ကို ဖျက်ခြင်း သို့မဟုတ် ပျက်စီးစေခြင်းကဲ့သို့သော အန္တရာယ်ရှိသော လုပ်ဆောင်ချက်များ၏ အန္တရာယ်ဖြစ်သည်။ ဤစိုးရိမ်မှုများသည် ခိုင်လုံပေသာ်လည်း database access permissions များကို ကောင်းမွန်စွာ ချိန်ညှိခြင်းအားဖြင့် ထိရောက်စွာ လျှော့ချနိုင်သည်။ Database အများစုအတွက် ၎င်းတွင် database ကို read-only အဖြစ် ချိန်ညှိခြင်း ပါဝင်သည်။ PostgreSQL သို့မဟုတ် Azure SQL ကဲ့သို့သော database services များအတွက် app ကို read-only (SELECT) role တစ်ခု သတ်မှတ်ပေးရမည်ဖြစ်သည်။

လုံခြုံသော ပတ်ဝန်းကျင်တွင် app ကို run လုပ်ခြင်းသည် အကာအကွယ်ကို ပိုမိုမြှင့်တင်သည်။ Enterprise scenarios များတွင် data ကို ပုံမှန်အားဖြင့် operational systems များမှ ထုတ်ယူပြီး user-friendly schema ရှိသော read-only database သို့မဟုတ် data warehouse တစ်ခုအဖြစ် ပြောင်းလဲထည့်သွင်းကြသည်။ ဤနည်းလမ်းသည် data သည် လုံခြုံပြီး performance နှင့် accessibility အတွက် ကောင်းမွန်စွာ ပြုပြင်ထားကြောင်းနှင့် app သည် ကန့်သတ်ထားသော read-only access ရှိကြောင်း သေချာစေသည်။

## နောက်ထပ် အရင်းအမြစ်များ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## ယခင်သင်ခန်းစာ

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## နောက်သင်ခန်းစာ

[Agentic RAG](../05-agentic-rag/README.md)
