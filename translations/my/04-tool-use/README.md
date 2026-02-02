[![How to Design Good AI Agents](../../../translated_images/my/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရန် အပေါ်ရှိ ပုံကို နှိပ်ပါ)_

# ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံ

ကိရိယာများသည် AI အေးဂျင့်များအား နေရာကျယ်လွန်းသော တတ်နိုင်မှုများ ပိုင်ဆိုင်စေသောကြောင့် စိတ်ဝင်စားစရာကောင်းသော်လည်း AI အေးဂျင့်တွင် ကန့်သတ်ထားသော လုပ်ဆောင်နိုင်မှုများရှိနေခြင်းအစား ကိရိယာတစ်ခု တိုးချဲ့ထည့်သွင်းခြင်းဖြင့် အေးဂျင့်သည် လုပ်ဆောင်နိုင်သော လုပ်ငန်းစဉ်များစွာကို ပြုလုပ်နိုင်သည်။ ယခုအခန်းတွင် AI အေးဂျင့်များသည် ၎င်းတို့၏ ရည်မှန်းချက်များကို တက်နိုင်ရန် ကိရိယာများကို မည်သို့ အသုံးပြုနိုင်ကြောင်း ဖော်ပြသော ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံကို ကြည့်မည်ဖြစ်သည်။

## နိဒါန်း

ဤသင်ခန်းစာတွင် ကျွန်ုပ်တို့အဖြေရှာလိုသော မေးခွန်းများမှာ -

- ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံ란 무엇입니까?
- ၎င်းကို မည်သည့်အသုံးအများဆုံးဖြစ်စေသော သုံးစွဲမှုများအတွက် အသုံးပြုနိုင်ပါသလဲ?
- ဒီဇိုင်းပုံစံအား လက်တွေ့ တည်ဆောက်ရန် လိုအပ်သော အစိတ်အပိုင်းများ/ဖွဲ့စည်းပုံများက ဘာတွေလဲ?
- ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များကို တည်ဆောက်ရာတွင် ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံကို အသုံးပြုရာရှိ အထူးစဉ်းစားရန် ချက်များက ဘာများလဲ?

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးနောက်၊ သင်သည် -

- ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံ၏ အဓိပ္ပါယ်နှင့် ရည်ရွယ်ချက်ကို သတ်မှတ်နိုင်မည်။
- ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံကို အသုံးပြုနိုင်သည့် သုံးစွဲမှုလိုတ်စဉ်များကို မှတ်မိနိုင်မည်။
- ဒီဇိုင်းပုံစံသာ ရေးဆွဲမှုတွင် လိုအပ်သော အဓိကအစိတ်အပိုင်းများကို နားလည်နိုင်မည်။
- ဒီဇိုင်းပုံစံကို အသုံးပြုသည့် AI အေးဂျင့်များတွင် ယုံကြည်စိတ်ချနိုင်မှုအတွက် စဉ်းစားရမည့် ချက်များကို သိမြင်နိုင်မည်။

## ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံ란 무엇입니까?

**ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံ** သည် LLMs များအား နေရာရပြင်ပကိရိယာများနှင့် ဆက်သွယ်နိုင်စွမ်းပေးခြင်းဖြင့် သတ်မှတ်ထားသော ရည်ရွယ်ချက်များကို ရရှိစေခြင်းကို ဦးတည်သည်။ ကိရိယာများဆိုသည်မှာ အေးဂျင့်မှ လုပ်ဆောင်နိုင်သည့် ကုဒ်များဖြစ်ပြီး လုပ်ဆောင်ချက်များပြုလုပ်ရန် သုံးစွဲနိုင်သည်။ ကိရိယာတစ်ခုမှာ ကီလိုကန်ယူလေးတာကဲ့သို့သော ရိုးရိုး function တစ်ခုကို ဖြစ်နိုင်သလို စတော့ရှယ်ယာဈေးနှုန်းရှာဖွေရန် သို့မဟုတ် ရာသီဥတုခန့်မှန်းခြေကဲ့သို့သော တတိယပုဂ္ဂိုလ်ဝန်ဆောင်မှု API ဖုန်းခေါ်မှုတစ်ခုလည်း ဖြစ်နိုင်သည်။ AI အေးဂျင့်များအရ ပုံမှန်အားဖြင့် ကိရိယာများကို **မော်ဒယ်ပြုလုပ်သော function ခေါ်ဆိုမှုများ** အဖြစ် အေးဂျင့်များမှ အကောင်အထည်ပြုနိုင်သည်။

## ၎င်းကို မည်သည့်အသုံးပြုမှုများတွင် အသုံးပြုနိုင်ပါသလဲ?

AI အေးဂျင့်များသည် ကိရိယာများကို အသုံးပြု၍ ခက်ခဲခဲလုပ်ရက်သောလုပ်ငန်းများ ပြီးစီးနိုင်ရန်၊ သတင်းအချက်အလက် ရယူနိုင်ရန် သို့မဟုတ် ဆုံးဖြတ်ချက်များ ချနိုင်ရန် လိုအပ်ပါသည်။ ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံသည် ဒေတာဘေ့စ်များ၊ ဝက်ဘ်ဝန်ဆောင်မှုများ သို့မဟုတ် ကုဒ်ဖော်ပြသူများကဲ့သို့ ပြင်ပစနစ်များနှင့် လှုပ်ရှားမှုတိုးတက်စေသော အခြေအနေများတွင် မကြာခဏအသုံးပြုသည်။ ၎င်းစွမ်းရည်သည် အမျိုးမျိုးသော အသုံးပြုမှုများအတွက် အထောက်အကူဖြစ်ပါသည် -

- **အဆင့်မြင့် သတင်းအချက်အလက် ရယူမှု:** အေးဂျင့်များသည် ပြင်ပ API များ သို့မဟုတ် ဒေတာဘေ့စ်များကို မှေးဖွင့်၍ အချိန်နှင့်တပြေးညီသော အချက်အလက်များ ရယူနိုင်သည် (ဥပမာ - SQLite ဒေတာဘေ့စ်ကို မေးမြန်း၍ ဒေတာစစ်ထုတ်ခြင်း၊ စတော့ဆိုင်ကယ် ဈေးထားများ သို့မဟုတ် ရာသီဥတု သတင်းအချက်အလက်များ ရရှိစေခြင်း)။
- **ကုဒ်စစ်ဆေးခြင်းနှင့် ဖော်ထုတ်ခြင်း:** AI အေးဂျင့်များသည် ကုပြုလုပ်ရန်၊ အစီရင်ခံစာများထုတ်ရန် သို့မဟုတ် အတုအယောင်များ ပြုလုပ်ရန် ကုဒ်များ သို့မဟုတ် စကရစ်တ်များ ကို အကောင်အထည်ဖော်နိုင်သည်။
- **လုပ်ငန်းစဉ် အလိုအလျောက်ပြုလုပ်ခြင်း:** ကိရိယာများကို တစ်ဆင့်စီ လိုက်ဖက်မှုများဖြင့် ပေးပြီး စဉ်ဆက်မပြတ် ပြုလုပ်ရသော လုပ်ငန်းစဉ်များ (ဥပမာ - တာဝန်ရက်ဇယားများ၊ အီးမေးလ် ဝန်ဆောင်မှုများ၊ ဒေတာလမ်းကြောင်းများ) ကို အလိုအလျောက်လုပ်ဆောင်ခြင်း။
- **ဖောက်သည် ပံ့ပိုးမှု:** CRM စနစ်များ၊ တစ်ကတ်စနစ်များ သို့မဟုတ် သိပ္ပံဘက် အချက်အလက် အခြေစိုက် ဒေတာများနှင့် ဆက်သွယ်ကူညီ၍ အသုံးပြုသူ မေးခွန်းများ ရှင်းလင်းပေးခြင်း။
- **အကြောင်းအရာ ဖန်တီးခြင်းနှင့် တည်းဖြတ်ခြင်း:** စာလုံးပေါင်းစစ်ဆေးခြင်း၊ အကျဉ်းချုပ်ရေးခြင်း သို့မဟုတ် အကြောင်းအရာ လုံခြုံရေးမှူချက် ထောက်ပံ့ အကူအညီ ပေးနိုင်သော ကိရိယာများကို အသုံးပြု၍ အကြောင်းအရာ ဖန်တီးမှုလုပ်ငန်းများကို ကူညီခြင်း။

## ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံကို လက်တွေ့ဆောင်ရွက်ရန် လိုအပ်သည့် အစိတ်အပိုင်းများ/ဖွဲ့စည်းပုံများ

ဤဖွဲ့စည်းပုံများသည် AI အေးဂျင့်ကို လုပ်ငန်းစဉ်များ များစွာ ဆောင်ရွက်နိုင်စေသည်။ ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံကို တည်ဆောက်ရန် လိုအပ်သော အဓိက အစိတ်အပိုင်းများအား ကြည့်ကြပါစို့ -

- **Function/Tool Schemas:** ရနိုင်သော ကိရိယာများ၏ အသေးစိတ် ဖော်ပြချက်များဖြစ်ပြီး function နာမည်၊ ရည်ရွယ်ချက်၊ လိုအပ်သော အမည်များနှင့် ထွက်ရှိရမည့် အချက်များကို ပေါင်းစပ်တည်ဆောက်ထားသည်။ ၎င်းများက LLM သို့ ကိရိယာရှိမှုနှင့် မှန်ကန်သော မေ့စ်ကိုတောင်းဆိုရန် နည်းလမ်းကို နားလည်စေသည်။

- **Function Execution Logic:** အသုံးပြုသူ၏ ရည်မှန်းချက်နှင့် စကားပြောဆိုမှုအခြေအနေကို အခြေခံ၍ မည်ကိရိယာကို မည်သည့်အချိန်၌ခေါ်သုံးမည်ကို သတ်မှတ်သော စီမံကိန်းဖြစ်သည်။ ဤတွင် စီမံကိန်းဖန်တီးမှု မော်ဒူးများ၊ လမ်းညွှန်မှုစနစ်များ သို့မဟုတ် ကိရိယာအသုံးပြုမှုကို အလိုအလျောက် ရွေးချယ်သော အခြေအနေများ ပါဝင်နိုင်သည်။

- **Message Handling System:** အသုံးပြုသူအထောက်အထား၊ LLM အဖြေများ၊ ကိရိယာခေါ်ဆိုမှုများနှင့် ကိရိယာထွက်ရှိမှုများကို စီမံခန့်ခွဲသော အစိတ်အပိုင်းများ။

- **Tool Integration Framework:** လွယ်ကူစွာ ဆက်သွယ်သုံးစွဲနိုင်သော တည်ဆောက်ပုံခေါင်းစဉ်ဖြစ်၍ ရိုးရှင်းသော function များ ထဲမှ စတာမှ အတော်လေးရှုပ်တဲ့ နေရာရပြင်ပဝန်ဆောင်မှုများအထိ ချိတ်ဆက်ပေးသည်။

- **Error Handling & Validation:** ကိရိယာဆောင်ရွက်မှု အပြစ်အနာဂတ်များကို ကိုင်တွယ်ရန်၊ အမည်ပိုင်းများကို စစ်ဆေးရန်နှင့် မမှန်ကန်သော တုံ့ပြန်ချက်များ ကို စီမံခန့်ခွဲရန် စနစ်များ။

- **State Management:** စကားပြောဆိုမှုအခြေအနေ၊ ယခင်ကိရိယာဆက်ဆံမှုများနှင့် တာရှည်ထိန်းသိမ်းထားသော ဒေတာတို့ကို ခြေရာခံ၍ မျက်စောင်းအတန်းဆက်ဆံမှုများအတွင်း တည်ငြိမ်မှုရှိစေရန်။

နောက်တစ်ဆင့် Function/Tool Calling ကို ပိုမိုအသေးစိတ် ကြည့်ကြမည်။

### Function/Tool Calling

Function ခေါ်ဆိုခြင်းသည် LLMs များအား ကိရိယာများနှင့် ဆက်သွယ်နိုင်ရန် အဓိကနည်းလမ်းဖြစ်သည်။ 'Function' နှင့် 'Tool' ဆိုသော စကားများကို တူညီစွာ အသုံးပြုကြသည်မှာ 'function' များသည် ပြန်လည်အသုံးပြုနိုင်သော ကုဒ်အပိုင်းများဖြစ်ပြီး AI အေးဂျင့်များလုပ်ငန်းများ ပြုလုပ်ရန် အသုံးပြုသော 'tool' များ ဖြစ်ကြောင်းကြောင့်ဖြစ်သည်။ Function code ကို ခေါ်ဆိုပြီး လုပ်ဆောင်နိုင်ရန်အတွက် LLM သည် အသုံးပြုသူ၏ တောင်းဆိုချက်နှင့် function ဖော်ပြချက်ကို နှိုင်းယှဉ်ဖို့ လိုအပ်သည်။ ၎င်းအတွက် ရနိုင်သော function များအား ဖော်ပြထားသော schema တစ်ခုကို LLM သို့ ပို့သည်။ LLM သည် လက်ရှိလုပ်ငန်းအတွက် သင့်လျော်ဆုံး function ကို ရွေးချယ်ပြီး ၎င်း၏ နာမည်နှင့် ပါရာမီတာများကို ပြန်လည်ပေးပို့သည်။ ရွေးချယ်ထားသော function ကို ခေါ်ဆိုပြီး တုံ့ပြန်ချက်ကို LLM သို့ ပြန်ပို့သည်၊ ထိုအချက်အလက်များဖြင့် အသုံးပြုသူ၏ တောင်းဆိုချက်အား အဖြေပြုသည်။

developer များအတွက် function calling ကို အေးဂျင့်များအတွက် တည်ဆောက်ရန် -

1. function calling ကို ပံ့ပိုးနိုင်သော LLM မော်ဒယ်တစ်ခု
2. function ဖေါ်ပြချက်ပါရှိသည့် schema တစ်ခု
3. ဖော်ပြထားသော function တစ်ခုချင်းစီအတွက် ကုဒ်

မြို့တစ်မြို့ရှိ လက်ရှိအချိန်ရယူမည့် နမူနာကို အသုံးပြု၍ ဖော်ပြကြမည် -

1. **function calling ကို ပံ့ပိုးသော LLM တစ်ခု ဖန်တီးပါ:**

    မော်ဒယ်အားလုံးမှာ function calling ပံ့ပိုးမှု မရှိနိုင်ပါ၊ သင့်အသုံးပြုလိုသော LLM တွင်ရှိသည်ကို စစ်ဆေးရမည်။ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> သည် function calling ကို ပံ့ပိုးထားသည်။ Azure OpenAI client ကို စတင်ဖြင့် သုံးစတင်နိုင်သည်။

    ```python
    # Azure OpenAI client ကို စတင်တည်ဆောက်ခြင်း
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Function Schema တစ်ခု ဖန်တီးပါ:**

    နောက်တစ်ဆင့်မှာ function နာမည်၊ function ၏ လုပ်ဆောင်ချက်ဖော်ပြချက်နှင့် ပါရာမီတာအမည်များနှင့် ဖော်ပြချက်များ ပါဝင်သည့် JSON schema တစ်ခု သတ်မှတ်မည်။ 
    schema ကို ယခင် client သို့၊ အသုံးပြုသူ၏ San Francisco အချိန်ကို ရှာဖွေလိုသော တောင်းဆိုချက်နှင့်အတူ ပေးပို့မည်။ ပြန်လာသည်မှာ **tool call** ဖြစ်ပြီး မေးခွန်းအတွက် နောက်ဆုံးအဖြေ မဟုတ်ပါ။ LLM သည် ရွေးချယ်ထားသော function နာမည်နှင့် သွားမည့် arguments များကို ပြန်ပို့သည်။

    ```python
    # မော်ဒယ်အတွက် ဖတ်ရန် လုပ်ဆောင်ချက် ဖော်ပြချက်
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
  
    # အစပိုင်း အသုံးပြုသူ စာတမ်း
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # ပထမဆုံး API ခေါ်ယူမှု: မော်ဒယ်ကို ဖန်ရွက်မှုကို အသုံးပြုရန် မေးမြန်းပါ
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # မော်ဒယ်၏ တုံ့ပြန်ချက်ကို ပြုလုပ်ပါ
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **လုပ်ငန်းဆောင်ရွက်ရန် လိုအပ်သော function code:**

    LLM မှ function ကို ပြိုင်တင်ပြီးနောက်၊ လုပ်ငန်းဆောင်ရွက်သော ကုဒ် ကို အကောင်အထည်ဖော်ရန်လိုအပ်သည်။
    Python ဖြင့် လက်ရှိအချိန် ရယူရန် ကုဒ်ရေးသားနိုင်ပြီး response_message မှ function နာမည်နှင့် arguments ကို ဆွဲထုတ်ရန်လည်း လိုအပ်မည်။

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
     # ဖန်ရှင်ခေါ်ဆိုမှုများကို ကိုင်တွယ်ပါ
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
  
      # ဒုတိယ API ခေါ်ဆိုမှု: ပုံစံမှ နောက်ဆုံးတုံ့ပြန်ချက်ကို ရယူပါ
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

Function Calling သည် အက်ဂျင့်ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံများ အများစု၊ သို့မဟုတ် အားလုံးတွင် အခြေခံဖြစ်သည်။ သို့သော် စတင်ရေးဆွဲခြင်းမှာ အခက်အခဲရှိနိုင်ပါသည်။
[Lesson 2](../../../02-explore-agentic-frameworks) တွင် သင်ယူခဲ့သလို agentic framework များသည် ကိရိယာအသုံးပြုမှု အကောင်အထည်ဖော်ရန် အဆောက်အအုံများ မျှဝေပြုပေးကြသည်။

## Agentic Framework များဖြင့် ကိရိယာအသုံးပြု နမူနာများ

အောက်ပါ agentic framework များကို အသုံးပြု၍ ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံ ကို မည်သို့လုပ်နိုင်သည်ကို အသုံးပြုပုံ နမူနာများ ဖြစ်ပါသည် -

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> သည် .NET၊ Python နှင့် Java developer များအတွက် ဖွင့်လှစ်အရင်းအမြစ် AI Framework ဖြစ်ပြီး LLM များဖြင့် function calling ကို လွယ်ကူစွာ ပြုလုပ်နိုင်ရန် function များနှင့် ၎င်း၏ ပါရာမီတာများကို <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a> ဖြင့် ကိုယ်စားပြုပေးသည်။ နှင့် model နှင့် ကုဒ်အကြား ပြန်လည်ဆက်သွယ်ဆောင်ရွက်မှုကို လည်း ကိုင်တွယ်ပေးသည်။ Semantic Kernel ကဲ့သို့ အေးဂျင့် framework အသုံးပြုခြင်း၏ အခြားအားသာချက်မှာ <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> နှင့် <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a> ကဲ့သို့ ရှိပြီးသားကိရိယာများကို လွယ်ကူစွာ အသုံးပြုနိုင်ခြင်း ဖြစ်ပါသည်။

Semantic Kernel ဖြင့် function calling နေရာရပြင် ပုံစံကို အောက်ပါပုံက ဖော်ပြပါသည် -

![function calling](../../../translated_images/my/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernel တွင် function/ကိရိယာများကို <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> ဟု ခေါ်သည်။ ယခင်တွင် မြင်ခဲ့သော `get_current_time` function ကို class အဖြစ် ပြောင်းပြီး plugin တစ်ခုအဖြစ် ပြုလုပ်နိုင်သည်။ `kernel_function` decorator ကို မူကြမ်းအနေဖြင့် ထည့်သွင်းနိုင်ပြီး function ရဲ့ ဖော်ပြချက်ကိုလည်း ထည့်သွင်းသည်။ GetCurrentTimePlugin ဖြင့် kernel ကို ဖန်တီးပါက kernel သည် function နှင့် ပါရာမီတာများကို လက်ဖြင့် serializing ပြုလုပ်ပြီး LLM ပို့ရန် schema ဖန်တီးသည်။

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

# ကန့်ကွက်ကို ဖန်တီးပါ
kernel = Kernel()

# ပလပ်ဂ်အင်ကို ဖန်တီးပါ
get_current_time_plugin = GetCurrentTimePlugin(location)

# ပလပ်ဂ်အင်ကို ကန့်ကွက်ထဲ ထည့်ပါ
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> သည် နောက်ဆုံးပေါ် Agentic Framework ဖြစ်ပြီး အောက်ခံ တို့ကို ကိုင်တွယ်စီမံရန်မလိုဘဲ developer များအား လုံခြုံစိတ်ချရသော၊ အသုံးပြုရလွယ်ကူပြီး တိုးချဲ့နိုင်သော AI အေးဂျင့်များ ဖန်တီး၊ ထုတ်လွှင့်နှင့် ချဲ့ထွင်နိုင်ရန် ရည်ရွယ်ထားသည်။ အထူးသဖြင့် လုပ်ငန်းအသုံးပြုမှုများအတွက် အသုံးဝင်ပြီး တစ်လုံးတည်း အစီအစဉ်ဆောင်ရွက်ခြင်းအားဖြင့် လုံခြုံရေးအဆင့်မြင့် Managed service ဖြစ်သည်။

LLM API ကို တိုက်ရိုက် အသုံးပြုခြင်းနှင့် နှိုင်းယှဉ်လျှင် Azure AI Agent Service သည် အောက်ပါ အားသာချက်များပေးသည် -

- ကိရိယာခေါ်ဆိုမှုကို အလိုအလျောက် ပြုလုပ်ခြင်း – ကိရိယာခေါ်ဆိုမှုကို မြင်ညွှန်းစစ်ပြီး tool ကို ခေါ်သုံးပြီး တုံ့ပြန်ချက်ကို ထိန်းညှိရန် မလိုအပ်ပဲ ဆာဗာဘက်တွင် အမှတ်အသားသွားဆောင်ရွက်ပေးသည်။
- ဒေတာများကို လုံခြုံစွာ စီမံခြင်း – ကိုယ်ပိုင် စကားပြောဆိုမှု ပြည်တွင်းသိုလှောင်မှု မလိုပဲ thread များကို အချက်အလက် စုဆောင်းထိန်းသိမ်းရန် အောက်ခံထားနိုင်သည်။
- ရှိပြီးသား ကိရိယာများ – Bing, Azure AI Search, Azure Functions ကဲ့သို့သော ဒေတာရင်းမြစ်များနှင့် ဆက်သွယ်ရန် တိုက်ရိုက်အသုံးပြုနိုင်သော ကိရိယာများ။

Azure AI Agent Service သည် ကိရိယာများကို အောက်ပါ ၂ မျိုးခွဲခြားနိုင်သည် -

1. အသိပညာကိရိယာများ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ဖြင့် စိစစ်ခြင်း</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ဖိုင်ရှာဖွေရေး</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. လုပ်ဆောင်ချက် ကိရိယာများ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI က သတ်မှတ်ထားသော ကိရိယာများ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service သည် ၎င်းကိရိယာများကို `toolset` အဖြစ် အတူသုံးနိုင်ရန် နှင့် သတ်မှတ်ထားသော စကားပြောဆိုမှုမှ အချက်အလက်များကို မှတ်တမ်းတင်ထားသည့် `threads` ကို အသုံးပြုသည်။

Contoso ဟု အမည်ရှိကုမ္ပဏီတစ်ခုတွင် အရောင်းကိုယ်စားလှယ်တစ်ဦး ဖြစ်ကြောင်း စဉ်းစားပါ။ သင်သည် သင်၏ အရောင်းအချက်အလက်အပေါ် မေးခွန်းများ ဖြေဆိုနိုင်သော စကားပြောဆိုမှု အေးဂျင့် တစ်ခု ဖန်တီးလိုသည်။

အောက်ပါပုံသည် Azure AI Agent Service ကို အသုံးပြုပြီး သင်၏ အရောင်းအချက်အလက်များကို ခွဲခြမ်းစိတ်ဖြာသည့် နည်းလမ်းကို ဖော်ပြထားသည် -

![Agentic Service In Action](../../../translated_images/my/agent-service-in-action.34fb465c9a84659e.webp)

ဤကိရိယာများထဲမှ တစ်ခုခုကို service နှင့် အသုံးပြုရန် client တစ်ခု ဖန်တီးပြီး tool လုပ် ဒါမှမဟုတ် toolset သတ်မှတ်နိုင်သည်။ လက်တွေ့တွင် Python ကုဒ်အောက်ပါအတိုင်း အသုံးပြုနိုင်သည်။ LLM သည် toolset ကို ကြည့်၍ အသုံးပြုသူ ဖြင့် ဖန်တီးထားသော `fetch_sales_data_using_sqlite_query` function သို့မဟုတ် ပြင်ပရှိ Code Interpreter ကို အသုံးပြုရန် ဆုံးဖြတ်လိမ့်မည်။

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query အလုပ်အစီအစဉ်ကို fetch_sales_data_functions.py ဖိုင်ထဲတွင်တွေ့နိုင်သည်။
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ကိရိယာစနစ်ကို စတင်တပ်ဆင်သည်
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query အလုပ်အစီအစဉ်နှင့် function calling agent ကို စတင်တပ်ဆင်ပြီး toolset တွင် ထည့်သွင်းသည်
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter ကိရိယာကို စတင်တပ်ဆင်ပြီး toolset တွင် ထည့်သွင်းသည်။
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ ဖန်တီးရာတွင် ကိရိယာအသုံးပြု ဒီဇိုင်းပုံစံကို အသုံးပြုရာရှိ အထူးစဉ်းစားရမည့် ချက်များ

LLM များမှ ဒိုင်နမစ်ပြုလုပ်သော SQL များတွင် လုံခြုံရေးအရေးပါသည်။ အထူးသဖြင့် SQL injection သို့မဟုတ် database ကို ဖျက်ဆီးခြင်း၊ ပျက်စီးအောင် ပြုလုပ်ခြင်းကဲ့သို့ အန္တရာယ်ရှိနိုင်သည်။ ဤစိုးရိမ်ချက်များမှာ တကယ်လက်တွေ့ရှိပြီး database access လိုင်စင်မှန်ကန်စွာ မသတ်မှတ်လျှင် ဖြစ်ပေါ်နိုင်သည်။ များသော ဒေတာဘေ့စ်များတွင် database ကို ဖတ်-only အခြေအနေ ဖြင့် သတ်မှတ်ရုံဖြင့် ဒီအန္တရာယ်များကို လျော့နည်းစေပါသည်။ PostgreSQL သို့မဟုတ် Azure SQL ကဲ့သို့သော database ဝန်ဆောင်မှုများတွင် app ကို ဖတ်-only (SELECT) role ဖြစ်အောင် သတ်မှတ်သင့်သည်။
လုံခြုံသောပတ်ဝန်းကျင်တွင် app ကိုလည်ပတ်ခြင်းသည် လုံခြုံမှုကို ပိုမိုတိုးတက်စေသည်။ စက်မှုလုပ်ငန်းအခြေအနေများတွင်၊ ဒေတာကို ပုံမှန်အားဖြင့် လုပ်ငန်းဆောင်တာစနစ်များမှ ထုတ်ယူပြီး ဖတ်ရန်သာဖြစ်သော ဒေတာဘေ့စ် သို့မဟုတ် ဒေတာဂိုဏ်းတွင် အသုံးပြုရန်အဆင်ပြေသော schema ဖြင့် ပြောင်းလဲထည့်သွင်းသည်။ ဤနည်းလမ်းလည်း ဒေတာများကို လုံခြုံစေရန်၊ စွမ်းဆောင်ရည်နှင့် ဝင်ရောက်နိုင်မှုများအတွက် အကောင်းဆုံးပြုလုပ်ထားရန်နှင့် app သည် ဖတ်ရန်သာ ခွင့်ပြုထားသော ဝင်ရောက်ခွင့်ဖြင့် လည်ပတ်စေရန် အာမခံပေးသည်။

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့်ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည်တိကျမှုအတွက်ကြိုးပမ်းသည်ဖြစ်ပေမယ့် အလိုအလျောက်ဘာသာပြန်ခြင်းမျှသော အမှားများ သို့မဟုတ် အမှားအယွင်းများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန်။ မူလစာတမ်းကို မိမိဘာသာဖြင့်သာ အတည်ပြုရင်းမြစ်အဖြစ်ယူဆရန် သင့်တော်သည်။ အရေးကြီးသောအချက်အလက်များအတွက်တော့ ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်မှုပို၍ ယုံကြည်စိတ်ချစေပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုရာမှ ဖြစ်ပေါ်မည့် နားလည်မှု ချွတ်ယွင်းမှုများအတွက် အမှုခံယူမည်မဟုတ်ပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->