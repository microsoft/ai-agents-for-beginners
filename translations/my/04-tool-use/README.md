[![How to Design Good AI Agents](../../../translated_images/my/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ဓာတ်ပုံကိုနှိပ်၍ ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရှုပါ)_

# ကိရိယာ အသုံးပြုမှု ဒီဇိုင်းပုံစံ

ကိရိယာများသည် AI အေးဂျင့်များကို ကျယ်ပြန့်သော စွမ်းရည်များ ရရှိစေရန် ခွင့်ပြုကြောင်းကြောင့် စိတ်ဝင်စားဖွယ်ဖြစ်သည်။ အေးဂျင့်သည် ဆောင်ရွက်နိုင်သည့် လုပ်ဆောင်ချက်များကန့်သတ်ထားခြင်းမရှိဖို့မဟုတ်ပဲ၊ ကိရိယာတစ်ခု ထည့်သွင်းခြင်းဖြင့် အေးဂျင့်သည် လုပ်ဆောင်နိုင်သည့် လုပ်ဆောင်ချက်ကျယ်ပြန့်သွားသည်။ ဤအခန်းတွင် ကျွန်ုပ်တို့ သွားကြည့်မည့် ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံမှာ AI အေးဂျင့်များ အသီးသီးသော ကိရိယာများကို ဘယ်လိုအသုံးပြု မည့်လဲဆိုတာ ရည်ရွယ်ချက်များ ပြည့်မှီစေရန် ဖော်ပြထားပါသည်။

## နိဒါန်း

ဤသင်ခန်းစာတွင် ကျွန်ုပ်တို့ ဖြေရှင်းလိုသော မေးခွန်းများမှာ -

- ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံဆိုတာဘာလဲ?
- ဘယ်မည်သည့် အကွာအဝေးများတွင် စွဲဆောင်၍ အသုံးပြုလို့ရမလဲ?
- ဒီဇိုင်းပုံစံကို အကောင်အထည်ဖော်ရန် လိုအပ်သည့် အစိတ်အပိုင်းများ/အခြေခံကွင်းဆက်များက ဘာတွေလဲ?
- ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ ဖန်တီးရာတွင် ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံကို အသုံးပြုသည့်အတွက် အထူးစဉ်းစားရန် ဘာတွေရှိသလဲ?

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာကို ပြီးမြောက်လျှင် -

- ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံနှင့် ၎င်း၏ရည်ရွယ်ချက်ကို ဖော်ထုတ်နိုင်မည်။
- ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံ သင့်တော်ရာ များကို သဘောပေါက်နိုင်မည်။
- ဒီဇိုင်းပုံစံအကောင်အထည်ဖော်ရန် လိုအပ်သည့် အရေးကြီးသော အစိတ်အပိုင်းများကို နားလည်နိုင်မည်။
- ထိုဒီဇိုင်းပုံစံကို အသုံးပြုသော AI အေးဂျင့်များတွင် ယုံကြည်စိတ်ချရမှု အတွက် စဉ်းစားရန် အချက်များကို သိရှိနိုင်မည်။

## ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံ သည်ဘာလဲ?

**ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံ** သည် LLMs ကို ပရောဂျက်တစ်ခုရည်ရွယ်ချက်ကို ပြည့်မီစေဖို့ ပြင်ပ ကိရိယာများနှင့် ဆက်သွယ်သုံးနိုင်စေရန် အာရုံစိုက်ထားသည်။ ကိရိယာဆိုသည်မှာ အေးဂျင့်တစ်ယောက်က စီမံဆောင်ရွက်ရန် အားထုတ်နိုင်သော ကုဒ်တစ်ခုဖြစ်သည်။ ကိရိယာတစ်ခုမှာ တွက်ချက်စက် လို့ဆိုတဲ့ ရိုးရှင်းတဲ့ function တစ်ခု ဖြစ်နိုင်ပြီး၊ ဒါမှမဟုတ် ပစ္စည်းစျေးနှုန်းရှာဖွေရေး သို့မဟုတ် ရာသီဥတု ခန့်မှန်းရေး တို့ကဲ့သို့သော တတိယပါတီ ဝန်ဆောင်မှုများကို API call ဖြင့် ခေါ်ယူခြင်းဖြစ်နိုင်ပါသည်။ AI အေးဂျင့်များ သော အခြေအနေမှာ ရောင့်ရဲအမိန့်အရ function call များကို ပြုလုပ်ဖို့ ဒီကိရိယာများကို အသုံးပြုရန် ရည်ရွယ်ထားသည်။

## ဘယ်မည်သည့် အကွာအဝေးများတွင် အသုံးပြုလို့ရမည်နည်း?

AI အေးဂျင့်များသည် ကိရိယာများကို အသုံးပြု၍ ရှုပ်ထွေးသော လုပ်ဆောင်ချက်များ ပြီးမြောက်စေနိုင်ပါသည်၊ အချက်အလက် ရယူမှု လူမှုဆက်ဆံရေး၊ ဆုံးဖြတ်ချက်ချမှုတို့တွင် အသုံးပြုနိုင်ပါသည်။ ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံကို အောက်ပါနေရာများတွင် များစွာအသုံးပြုကြသည်။

- **သက်တမ်းရှိသော အချက်အလက် ရယူမှု:** အေးဂျင့်များသည် ပြင်ပ API များ သို့မဟုတ် ဒေတာဘေ့စ်များကို စုံစမ်း ရှာဖွေနိုင်ပြီး အဆက်အသွယ်ရှိသောအချက်အလက်များ ရယူနိုင်သည် (ဥပမာ SQLite ဒေတာဘေ့စ်နယ်တွင် ဒေတာခွဲခြမ်းစိတ်ဖြာမှု, စတော့အိတ် စျေးနှုန်းသို့မဟုတ် ရာသီဥတု အချက်အလက်များ)။
- **ကုဒ် သို့မဟုတ် အဓိပ္ပာယ်ဖွင့်ချက် ဆောင်ရွက်မှု:** အေးဂျင့်များသည် ကုဒ်များ သို့မဟုတ် စာတန်းများကို တည်ဆောက်ဆောင်ရွက်ကာ သင်္ချာပြဿနာများ ဖြေရှင်းခြင်း၊ အစီရင်ခံစာများ ပြုလုပ်ခြင်း သို့မဟုတ် စမ်းသပ်မှုများ ပြုလုပ်နိုင်သည်။
- **လုပ်ငန်းစဉ် အလိုအလျောက်ဖြစ်စေရေး:** တိုးတက်ပြောင်းလဲမှုများ သို့မဟုတ် အဆင့်တစ်ခုနှင့်တစ်ခု ပြန်လည် ဆက်စပ်ခြင်းများကို task scheduler များ၊ အီးမေးလ်ဝန်ဆောင်မှုများ သို့မဟုတ် ဒေတာ လမ်းကြောင်းများအား အသုံးပြု၍ အလိုအလျောက်လုပ်ဆောင်ခြင်း။
- **ဖောက်သည် ကူညီပံ့ပိုးမှု:** အေးဂျင့်များသည် CRM စနစ်များ၊ တစ်ကယ်လိုက်နာစီမံရေး စနစ်များ သို့မဟုတ် အသိပညာ အခြေခံများကို ဆက်သွယ်ယူဆောင်ရွက်ကာ အသုံးပြုသူ မေးခွန်းများကို ဖြေရှင်းပေးနိုင်သည်။
- **အကြောင်းအရာ တွဲဖက်ပြောင်းလဲမှုနှင့် တည်းဖြတ်ခြင်း:** စာလုံးပေါင်းစစ်ဆေးရေး၊ စာသားအနှစ်ချုပ်ရေး၊ အကြောင်းအရာ လုံခြုံမှု သုံးသပ်မှုကိရိယာများကို အသုံးပြု၍ အကြောင်းအရာဖန်တီးမှုလုပ်ငန်းများတွင် အကူအညီပေးနိုင်သည်။

## ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံအတွက် လိုအပ်သော အစိတ်အပိုင်းများ/ အခြေခံကွင်းဆက်များကဘာတွေလဲ?

ဤအခြေခံကွင်းဆက်များက AI အေးဂျင့်ကို ကျယ်ပြန့်သည့် လုပ်ငန်းများ ဆောင်ရွက်နိုင်စေပါသည်။ ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံ ကို အကောင်အထည်ဖော်ရန် လိုအပ်သည့် အရေးကြီးသော အစိတ်အပိုင်းများမှာ -

- **Function/Tool Schema များ**: အသုံးပြုနိုင်သော ကိရိယာများ၏ အသေးစိတ်သတ်မှတ်ချက်များဖြစ်ပြီး အလုပ်လုပ်မှုအမည်၊ ရည်ရွယ်ချက်၊ လိုအပ်သော ပါရာမီတာများနှင့် မျှော်မှန်းထားသော ရလဒ်များ ပါဝင်သည်။ အဆိုပါ schema များက LLM ကို အသုံးပြုနိုင်သော ကိရိယာများကို နားလည်စေ၍ တောင်းဆိုမှုများကို မှန်ကန်စွာ ဖန်တီးနိုင်စေသည်။

- **Function ဆောင်ရွက်မှု လုပ်ငန်းစဉ်**: အသုံးပြုသူရည်ရွယ်ချက်နှင့် မက်ဆေ့ချ်အခြေအနေ အပေါ် မူတည်ကာ ကိရိယာများကို ဘယ်လို ဖုန်ညှင်း သုံးပြုမည်ဆိုတာ နိုင်ငံခြားမြေပုံစနစ်၊ လမ်းကြောင်းသတ်မှတ်ခြင်းများ သို့မဟုတ် အခြေအနေလိုက် မျှသာပေါ်ကိရိယာအသုံးပြုမှု ဆုံးဖြတ်ချက်များ ပါဝင်သည်။

- **မက်ဆေ့ချ် ကိုင်တွယ်မှု စနစ်**: အသုံးပြုသူ ဝင်ပေါက်များ၊ LLM တုံ့ပြန်မှုများ၊ ကိရိယာ ခေါ်ဆိုမှုနှင့် ကိရိယာ မှ ထွက်ရှိသည့် အချက်အလက်များ အကြား ဆက်သွယ်မှု လည်ပတ်မှုကို ထိန်းချုပ်သည်။

- **ကိရိယာ ပေါင်းစည်းရေး အခြေခံတွက်စနစ်**: အေးဂျင့် နှင့် ကိရိယာများကို ချိတ်ဆက်ထားသော အခြေခံပတ္တိကိုယ်ပိုင်နယ်မြေ၊ ရိုးရှင်းသည့် function များ သို့မဟုတ် အပြင်ဘက်ဝန်ဆောင်မှုများကို ချိတ်ဆက်ပေးသည်။

- **အမှား ကိုင်တွယ်မှု နှင့် စစ်ဆေးမှု**: ကိရိယာဆောင်ရွက်မှု တွင် မအောင်မြင်မှုများကို ကိုင်တွယ်ခြင်း၊ ပါရာမီတာများကို စစ်ဆေးခြင်း နှင့် မမျှော်လင့်ထားသော တုံ့ပြန်မှုများကို စီမံခန့်ခွဲခြင်း။

- **အခြေအနေ စီမံခန့်ခွဲမှု**: စကားပြောဆိုမှုအခြေအနေ၊ ယခင်ကိရိယာတွင် တုံ့ပြန်မှုများနှင့် တိုက်ရိုက် ဆက်စပ်အသေးသွား သော ဒေတာများကို မှတ်သားထားကာ များစွာ လှည့်လည်သော ဆက်ဆံမှုများ တွင် တစ်ထွေထွေ ထိပ်တန်းဆက်မှု ဖြစ်အောင် စောင့်ကြည့်သည်။

နောက်တစ်ဆင့်မှာ Function/Tool Calling ကို ပိုမိုအသေးစိတ် လေ့လာကြမည်။

### Function/Tool Calling

Function calling သည် LLMs များကို ကိရိယာများနှင့် ဆက်သွယ်နိုင်ရန် အဓိကနည်းလမ်းဖြစ်သည်။ သင်သည် 'Function' နှင့် 'Tool' ကို အတူတကွ အသုံးပြုသည်ကို မကြာခဏတွေ့ရမည်၊ ရှေ့တော်တို၊ 'function' (ပြန်လည်အသုံးပြုနိုင်သော ကုဒ်အပိုင်းများ) များသည် အေးဂျင့်များ၏ လုပ်ဆောင်ချက်များကို ဆောင်ရွက်ရန် အသုံးပြုသော 'ကိရိယာ' အဖြစ် သုံးသည်။ function ရဲ့ ကုဒ်ကို ဖုန်းခေါ်ရန်အတွက် LLM သည် အသုံးပြုသူ တောင်းဆိုချက်အား function ကို ဖော်ပြချက်နှင့် နှိုင်းယှဉ်ရမည်။ ၎င်းအတွက် function များအားလုံး၏ ဖော်ပြချက်လက္ခဏာများ ပါဝင်သော schema တစ်ခုကို LLM ထံ ပေးပို့မည်။ LLM သည် အလုပ်ဆောင်ရန် သင့်တော်သည့် function ကို ရွေးချယ်ပြီး function ၏ အမည်နှင့် အချက်အလက်များကို ပြန်ပေးပို့သည်။ ရွေးချယ်ထားသော function ကို ဖုန်းခေါ်ပြီး ၎င်း၏ တုံ့ပြန်ချက်ကို LLM ထံ ပြန်ပို့၊ LLM သည် ထိုအချက်အလက်အား အသုံးပြုပြီး အသုံးပြုသူ၏ တောင်းဆိုချက်ကို ဖြေပေးသည်။

Developer များအတွက် function calling ကို ဖန်တီးရန်လိုအပ်သောအရာများမှာ -

1. function calling ကို ထောက်ပံ့သည့် LLM မော်ဒယ်
2. function ဖော်ပြချက်များ ပါဝင်သော schema
3. ဖော်ပြထားသည့် function တစ်ခုချင်း၏ ကုဒ်

မြို့တစ်မြို့ရှိ လက်ရှိအချိန် ရယူခြင်း ဥပမာ ဖြင့် ရှင်းပြကြရအောင် -

1. **function calling ကို ထောက်ပံ့သည့် LLM တစ်ခုကို စတင်တည်ဆောက်ပါ။**

    function calling ကို ထောက်ပံ့ခြင်း မရှိသည့် မော်ဒယ် များလည်း ရှိပါသဖြင့် သင် အသုံးပြုလိုသော LLM အမျိုးအစားကို စစ်ဆေးရပါမည်။ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> သည် function calling ကို ထောက်ပံ့ပါသည်။ Azure OpenAI client ကို စတင်ဖန်တီးနိုင်ပါတယ်။

    ```python
    # Azure OpenAI client ကို စတင်ဆောင်ရွက်ပါ။
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Function Schema တစ်ခုဖန်တီးပါ။**

    function အမည်၊ function ၏လုပ်ဆောင်ချက် ဖေါ်ပြချက်နှင့် function ပါရာမီတာများ အမည်နှင့် ဖေါ်ပြချက်များ ပါသည့် JSON schema ကို သတ်မှတ်ပါမည်။ ၎င်း schema ကို client သို့ ပေးပို့ပြီး အသုံးပြုသူ၏ သွားရောက်ရန် ကျွမ်းကျင်ရာ San Francisco မြို့၏ အချိန် ရယူဖို့ တောင်းဆိုချက် နှင့်တွဲ၍ ပို့မည်။ မှတ်ချက်ကတော့ **tool call** သာ ပြန်လာမည်၊ မေးခွန်း၏ နောက်ဆုံးဖြေစကား မဟုတ်ပါ။ LLM သည် တာဝန်ယူချက်အတွက် ရွေးချယ်သော function ၏အမည်နှင့် argument များကို ပြန်ပေးပို့သည်။

    ```python
    # မော်ဒယ်အတွက် ဖတ်ရန် အလုပ်လုပ်ပုံဖော်ပြချက်
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
  
    # အစပိုင်း အသုံးပြုသူ စာတိုက်
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # ပထမဆုံး API ခေါ်ဆိုခြင်း: မော်ဒယ်ကို function ကို အသုံးပြုရန် မေးမြန်းပါ
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # မော်ဒယ်၏ တုံ့ပြန်ချက်ကို ပြန်လည် ဆောင်ရွက်ပါ
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **လုပ်ဆောင်ရန် လိုအပ်သော function ကုဒ်**

    ယခု LLM သည် run ပေးရန် လိုအပ်သည့် function ကို ရွေးချယ်ပြီး ဖြစ်သောကြောင့် လုပ်ဆောင်မှု ကုဒ်ကို ဖန်တီးပြီး run ထားရပါမည်။
    Python ဖြင့် လက်ရှိအချိန်ရယူခြင်းအတွက် ကုဒ်ရေးသားနိုင်ပါသည်။ response_message မှ အမည်နှင့် argument များထုတ်ယူပြီး နောက်ဆုံးရလဒ်ကို ရရှိစေရန် ကုဒ်ရေးရန်လိုအပ်ပါသည်။

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
     # ဖန်ခေါ်မှုများကို ကိုင်တွယ်ပါ
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
  
      # ဒုတိယ API ဖန်ခေါ်မှု: မော်ဒယ်မှ နောက်ဆုံးဖြေကြားချက်ကို ယူပါ
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

Function Calling သည် အများပြည်သူ သို့မဟုတ် အားလုံးသော အေးဂျင့် ကိရိယာ အသုံးပြုမှု ဒီဇိုင်းပုံစံများ၏ မျှအဓိက ဖြစ်ပြီး သို့သော် ကြမ်းတမ်းစွာ ကားမှု ရှိနိုင်သည်။
[Lesson 2](../../../02-explore-agentic-frameworks) တွင် သင်ယူထားသည့်အတိုင်း agentic frameworks များက tool use အတွက် အဆောက်အအုံအခြေခံများ ကို ပေးစွမ်းသည်။

## Agentic Frameworks ဖြင့် Tool Use နမူနာများ

အမျိုးမျိုးသော agentic frameworks များကို အသုံးပြုပြီး ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံကို ဘယ်လို အကောင်အထည်ဖော်ရမည်ကို နမူနာတချို့ဖော်ပြထားသည် -

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> သည် AI အေးဂျင့် သက်တမ်း မြဲစေခြင်းအတွက် open-source framework ဖြစ်သည်။ function calling ကို လွယ်ကူစွာအသုံးပြုနိုင်ရန် `@tool` decorator ဖြင့် Python function အဖြစ် ကိရိယာများ သတ်မှတ်ရန် ခွင့်ပြုသည်။ framework သည် မော်ဒယ်နှင့် သင့်ကုဒ်အကြား ဆက်သွယ်ရေးကို ကိုင်တွယ်ပေးသည်။ ထို့ပြင် File Search နှင့် Code Interpreter ကဲ့သို့ ကြိုတင်ပြင်ဆင်ထားသော ကိရိယာများကို `AzureAIProjectAgentProvider` မှတဆင့် အသုံးပြုနိုင်သည်။

အောက်ဖော်ပြပါ ပုံသည် Microsoft Agent Framework ဖြင့် function calling လုပ်ငန်းစဉ်ကို ဖော်ပြထားသည် -

![function calling](../../../translated_images/my/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework တွင် ကိရိယာများသည် decorated functions အဖြစ် သတ်မှတ်ကြသည်။ ယခင်သင့်ကြည့်ခဲ့သော `get_current_time` function ကို `@tool` decorator ဖြင့် ကိရိယာအဖြစ်ပြောင်းနိုင်သည်။ framework မှ function နှင့် ၎င်း၏ ပါရာမီတာများကို ကွန်ပျူတာသိုလှောင်ရာ schema ကို အလိုအလျောက် ပြုလုပ်၍ LLM ထံ ပို့ပေးမည်။

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Client ကို ဖန်တီးပါ
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agent တစ်ယောက် ဖန်တီးပြီး ကိရိယာနှင့် အတူ ပြေးပါ
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> သည် အကဲဖြတ်သူများကို လုံခြုံစွာ AI အေးဂျင့်များကို ဖန်တီး၊ ထည့်သွင်း၊ တိုးချဲ့နှင့် စီမံခန့်ခွဲနိုင်ရန် ရည်ရွယ်သည့် နောက်ဆုံးပေါ် agentic framework ဖြစ်သည်။ ဤဝန်ဆောင်မှုသည် စီးပွားရေးလုပ်ငန်းတွင် အထူးအသုံးဝင်မည် ဖြစ်ပြီး အထူးအဆင့်မြင့် လုံခြုံရေးနှင့် အပြည့်အဝ စီမံမှု ရရှိသည်။

LLM API ကို တိုက်ရိုက် အသုံးပြုမှုနှင့် နှိုင်းယှဉ်၍ Azure AI Agent Service သည် အောက်ပါတို့ကို ပေးစွမ်းသည် -

- ကိရိယာခေါ်ဆိုမှုကို အလိုအလျောက် ဆောင်ရွက်ခြင်း - ကိရိယာခေါ်ဆိုဗီလျူးကို ဖတ်ရန် အလိုမရှိတော့၊ လက်တင်လုပ်ဆောင်ခြင်းနှင့် တုံ့ပြန်ချက် ထိန်းချုပ်မှုအားလုံးကို server ပေါ်တွင် တာဝန်ယူ
- လုံခြုံစိတ်ချရသော ဒေတာ စီမံခန့်ခွဲမှု - ကိုယ်ပိုင် စကားပြောဆိုမှုအခြေအနေကို စီမံရန်မလိုတော့ပဲ threads အသုံးပြု၍ ဆက်သွယ်မှုသမိုင်းကို သိမ်းဆည်းထားနိုင်သည်
- ထိုနောက်ကျောကိရိယာများ - သင့်ဒေတာအရင်းအမြစ်များနှင့် ဆက်သွယ်ရန် Bing, Azure AI Search, Azure Functions ကဲ့သို့သော ကိရိယာများ

Azure AI Agent Service တွင် ရနိုင်သော ကိရိယာများကို နှစ်သိပ်အုပ်စုခွဲနိုင်သည် -

1. အသိပညာ အကိရိယာများ -
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ဖြင့် Grounding</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. လုပ်ဆောင်ချက် အကိရိယာများ -
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI သတ်မှတ်ထားသော ကိရိယာများ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service သည် ဤကိရိယာများအား `toolset` တစ်ခုအဖြစ် သုံးစွဲနိုင်ရန် ခွင့်ပြုသည်။ ထို့ပြင် `threads` ကို အသုံးပြုခြင်းဖြင့် တစ်စကားနဲ့ပြောသော ဆက်သွယ်မှု သမိုင်းနှင့် မက်ဆေ့ခ်ျများကို မှတ်သားထားသည်။

Contoso ဟုခေါ်သော ကုမ္ပဏီတွင် စျေးကွက်အေးဂျင့်တစ်ယောက် ဖြစ်ကြောင်း စဥ်းစားပါ။ သင်သည် သင့်ရောင်းအားဒေတာကို ဖြေရှင်းနိုင်သော စကားပြောအေးဂျင့် တစ်ခု တည်ဆောက်လိုသည်။

အောက်ဖော်ပြပါပုံသည် Azure AI Agent Service ကို အသုံးပြုပြီး သင့်ရောင်းအားဒေတာကို ခွဲခြမ်းစိတ်ဖြာသော နည်းလမ်းကို ဖော်ပြသည်။

![Agentic Service In Action](../../../translated_images/my/agent-service-in-action.34fb465c9a84659e.webp)

ဝန်ဆောင်မှုနှင့် ဒီကိရိယာများကို အသုံးပြုရန် client တစ်ခု ဖန်တီးပြီး ကိရိယာ သို့မဟုတ် toolset တစ်ခု သတ်မှတ်နိုင်သည်။ လုပ်ဆောင်ရန် Python ကုဒ်က အောက်ပါအတိုင်းဖြစ်မည်။ LLM သည် toolset ကို ကြည့်၍ အသုံးပြုသူ ဖန်တီးထားသော function `fetch_sales_data_using_sqlite_query` ဖြင့် သို့မဟုတ် ကြိုတင်ပြင်ဆင်ထားသော Code Interpreter ကို အသုံးပြုမည်ကို ဆုံးဖြတ်ခြင်းမပြုနိုင်ပါ။

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py ဖိုင်ထဲတွင် တွေ့ရှိနိုင်သော fetch_sales_data_using_sqlite_query ဖန်ကွက်။
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# အရာများစနစ်ကို စတင်ခြင်း
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ဖန်ကွက်နှင့် function calling agent ကို စတင်ပြီး toolset ထဲသို့ ထည့်သွင်းခြင်း
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter tool ကို စတင်ပြီး toolset ထဲသို့ ထည့်သွင်းခြင်း။
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ယုံကြည်စိတ်ချရသော AI အေးဂျင့် ဖန်တီးရန် ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံ အသုံးပြုမှုအတွက် အထူးစဉ်းစားရမည့် အချက်များ

LLM များက များပြားစွာ မီဒီယာထုတ်လုပ်သော SQL ဖြင့် တွေလုပ်ရာတွင် လုံခြုံရေးအခြေအနေ အထူးစိုးရိမ်မှုများ ရှိပါသည်၊ အဓိကအားဖြင့် SQL injection သို့မဟုတ် ဒေတာဘေ့စ်ကို ဖျက်ဆီးခြင်း၊ လုယက်ခြင်းသကဲ့သို့သော ယာယီ လုပ်ဆောင်မှုများ ဖြစ်ပေါ်နိုင်ခြင်း ဖြစ်သည်။ ဤစိုးရိမ်မှုများမှာ ပြစ်မှားသည် ဟုတ်ပေမယ့် ဒေတာဘေ့စ် အသုံးပြုခွင့်များကို သင့်တော်စွာ ဖွဲ့စည်းထားခြင်းဖြင့် ထိရောက်စွာ ကာကွယ်နိုင်ပါသည်။ အများအားဖြင့် ဒေတာဘေ့စ်ကို ဖတ်-only လုပ်ငန်းသုံးထားရန် ဖွဲ့စည်းရမည်။ PostgreSQL သို့မဟုတ် Azure SQL ကဲ့သို့သော ဒေတာဘေ့စ် ဝန်ဆောင်မှုများတွင်လည်း app ကို ဖတ်-only (SELECT) အခန်းကဏ္ဍ ခန့်အပ်ရမည်။

လုံခြုံစိတ်ချရသော ပတ်ဝန်းကျင်တွင် app ကို လည်ပတ်ခြင်းကာ ကာကွယ်မှု မြင့်တက်စေသည်။ စီးပွားရေးလုပ်ငန်းများတွင် ဒေတာများကို လည်ပတ်မှုစနစ်များကနေ ထုတ်ယူ၍ အသုံးပြုရလွယ်ကူသည့် schema နှင့် ဖြည့်သွင်းထားသည့် ဖတ်-only ဒေတာဘေ့စ် သို့မဟုတ် ဒေတာဂိုဒေါင်သို့ ပြောင်းလဲသိမ်းဆည်းထားသည်။ ၎င်းနည်းလမ်းသည် ဒေတာလုံခြုံမှု၊ လုပ်ဆောင်မှု ထိရောက်မှုနှင့် လျှောက်လွှာ လွယ်ကူရယူမှု ဖေါ်ပြချက်တွင် အကောင်းဆုံးဖြစ်စေရန် သေချာစေပြီး app ကို ဖတ်-only အခန်းကဏ္ဍ ဖြင့် ကန့်သတ်ထားသည်။

## နမူနာ ကုဒ်များ

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံများအကြောင်း ပိုမိုမေးမြန်းလိုပါသလား?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) သို့ ဝင်ရောက်ပြီး အခြားလေ့လာသူများနှင့်တွေ့ဆုံ၊ ရုံးချိန်များတက်ရောက်နှင့် သင့် AI အေးဂျင့် မေးခွန်းများဖြေရန် အခွင့်အရေး ရယူပါ။

## ထပ်ဆောင်း အရင်းအမြစ်များ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework အကျဉ်းချုပ်</a>

## ယခင်သင်ခန်းစာ

[Agentic Design Patterns နားလည်ခြင်း](../03-agentic-design-patterns/README.md)

## နောက်သင်ခန်းစာ
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->