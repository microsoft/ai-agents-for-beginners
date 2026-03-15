[![How to Design Good AI Agents](../../../translated_images/my/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(အပေါ်ရှိ ပုံကို နှိပ်၍ ဤသင်ခန်းစာ၏ ဗွီဒီယိုကို ကြည့်ရှုနိုင်သည်)_

# ကိရိယာအသုံးပြုမှု ဒီဇင်ပုံစံ

ကိရိယာများမှာ စိတ်ဝင်စားစရာကောင်းသည်၊ အကြောင်းမှာ AI အေးဂျင့်များအတွက် ပိုမိုကျယ်ပြန့်သော စွမ်းဆောင်ရည်များကို ခွင့်ပြုနိုင်သည်ဆိုသောအတွက်ဖြစ်သည်။ အေးဂျင့်တွင် လုပ်ဆောင်နိုင်သည့် အမှုအရာအများကြီးမရှိဘဲ ကန့်သတ်ထားခြင်းမဟုတ်ပဲ၊ ကိရိယာတစ်ခုထည့်သွင်းခြင်းဖြင့် အေးဂျင့်က အမျိုးမျိုးသော လုပ်ဆောင်ချက်များကို ပြုလုပ်နိုင်သည်။ ဤအခန်းတွင် ကျွန်ုပ်တို့သည် Tool Use Design Pattern ကို သုံးသပ်မည်ဖြစ်ပြီး၊ AI အေးဂျင့်များသည် ၎င်းတို့ရဲ့ရည်မှန်းချက်များကို ပြည့်မီစေရန် သတ်မှတ်ထားသော ကိရိယာများကို မည်သို့ အသုံးပြုနိုင်သည့်နည်းကို ဖော်ပြသည်။

## မိတ်ဆက်

ဤသင်ခန်းစာတွင် မေးခွန်းများကို ဖြေကြားရန် ကြိုးပမ်းနေပါသည်-

- ကိရိယာအသုံးပြုမှု ဒီဇိုင်န်ပုံစံ란 무엇인가요?
- ၎င်းကို အသုံးပြုနိုင်သည့် ကိစ္စရပ်များကဘာများ인가요?
- ဒီဇိုင်နာပုံစံကို အလုပ်လုပ်အောင် တည်ဆောက်ရန်လိုအပ်သည့် အစိတ်အပိုင်းများ/တည်ဆောက်ပစ္စည်းများကဘာများ인가요?
- ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ ဆောက်လုပ်ရာတွင် ကိရိယာအသုံးပြုမှု ဒီဇင်ပုံစံကို အသုံးပြုရာတွင် သတိပြုရန် အထူးစဉ်းစားချက်များကဘာများ인가요?

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးစီးပြီးနောက် သင်သည် -

- ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံ၏ အဓိပ္ပါယ်နှင့် ရည်ရွယ်ချက်ကို သတ်မှတ်နိုင်မည်။
- ကိရိယာအသုံးပြုမှု ဒီဇိုင်နာပုံစံအသုံးပြုလို့ရသည့် ကိစ္စရပ်များကို ဖော်ထုတ်နိုင်မည်။
- ဒီဇိုင်နာပုံစံအသုံးပြုရာတွင် လိုအပ်သည့် အဓိက အစိတ်အပိုင်းများကို နားလည်နိုင်မည်။
- ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ တည်ဆောက်ရာတွင် ဒီဒီဇိုင်နာပုံစံကို အသုံးပြုရာ တွင် သတိပြုရန် လိုအပ်သည့်အချက်များကို မွတ်မိနိုင်မည်။

## ကိရိယာအသုံးပြုမှု ဒီဇိုင်နာပုံစံ란 무엇인가요?

**ကိရိယာအသုံးပြုမှု ဒီဇိုင်နာပုံစံ** သည် LLM များအား သတ်မှတ်ထားသော ရည်မှန်းချက်များကို ပြည့်မီစေရန် ပြင်ပကိရိယာများနှင့် ဆက်သွယ်ဆောင်ရွက်နိုင်စေရန် လုပ်ဆောင်ချက်ပေးခြင်းကို အလယ်အလတ်ထားသည်။ ကိရိယာများမှာ အေးဂျင့်တစ်ယောက်က လုပ်ဆောင်ရန် ဖြစ်နိုင်သော ကုဒ်တစ်ရပ်ဖြစ်သည်။ ကိရိယာတစ်ခုသည် ကိန်းဂဏန်းတွက်ခြင်းကဲ့သို့ ရိုးရှင်းသော ဖင်ရှင်တစ်ခု ဖြစ်နိုင်ပြီး၊ စတော့ရှယ်ယာဈေးနှုန်း တိုင်းတာခြင်း သို့မဟုတ် ရာသီဥတုပိုင်းစိစစ်ခြင်းကဲ့သို့ တတိယပါတီ ဝန်ဆောင်မှုထံ API ခေါ်ဆိုမှုတစ်ခုဖြစ်နိုင်သည်။ AI အေးဂျင့်အပေါ်တွင် ကိရိယာများကို ထိုသူများ သုံးစွဲရာတွင် **မော်ဒယ်ထုတ်လုပ်သော ဖင်ရှင်ခေါ်ဆိုမှုများ** ဖြင့် တုံ့ပြန်ထားပြီး အေးဂျင့်များဖြင့် ဆောင်ရွက်ရမည့်အတိုင်းဒီဇိုင်နာဖန်တီးသည်။

## ၎င်းကို အသုံးပြုနိုင်သည့် ကိစ္စရပ်များကဘာများ인가요?

AI အေးဂျင့်များသည် ကိရိယာများကို အသုံးပြု၍ ပြဿနာရှုပ်ထွေးသော အလုပ်များကို ပြီးမြောက်စေနိုင်ပြီး၊ သတင်းအချက်အလက် ရယူခြင်း သို့မဟုတ် ဆုံးဖြတ်ချက်များ ချမှုများကို လုပ်ဆောင်နိုင်သည်။ ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံကို database များ၊ ဝဘ်ဆာဗစ်များ သို့မဟုတ် ကုဒ်ဗျူဟာများနှင့် အပြန်အလှန်ဆက်သွယ်နိုင်မှုလိုအပ်သော စီးရီးအခြေအနေများတွင် မကြာခဏ အသုံးပြုသည်။ ဤစွမ်းဆောင်ရည်သည် အမျိုးမျိုးသော ကိစ္စများတွင် အထောက်အကူဖြစ်ပြီး အောက်ပါသဘောအတိုင်း ဖြစ်သည်-

- **သတင်းအချက်အလက် ထပ်မံအသစ်ရယူခြင်း** - အေးဂျင့်များသည် ပြင်ပ API များ သို့မဟုတ် ဒေတာဘေ့စ်များကို မေးမြန်း၍ နောက်ဆုံးရ သတင်းအချက်အလက်များကို ရယူနိုင်သည် (ဥပမာ- SQLite database တစ်ခုကို မေးမြန်းပြီး ဒေတာ विश्लेषण ပြုလုပ်ခြင်း၊ စတော့ဈေးနှုန်း သို့မဟုတ် ရာသီဥတုပြင်ပ း ၆် ပေးခြင်း)။
- **ကုဒ် ပြုလုပ်ခြင်းနှင့် ဘာသာပြန်ခြင်း** - အေးဂျင့်များသည် သင်္ချာပြဿနာများ ဖြေရှင်းရန် ဖိုင်ရှင်များ ရေးရန် သို့မဟုတ် အစီရင်ခံစာများ ဖန်တီးရန် ကုဒ်များ ချဲ့ထွင်နိုင်သည်။
- **အလုပ်စဉ် အလိုအလျောက် ပြုလုပ်ခြင်း** - အလုပ်များကို အလိုအလျောက် ပြုလုပ်ရန် ကိရိယာ များဖြင့် အလုပ်စဉ်များ၊ အီးမေးလ် ဝန်ဆောင်မှုများ သို့မဟုတ် ဒေတာလိုင်းများ အထိ ထည့်သွင်း စနစ်တကျ ဆက်သွယ်ခြင်း။
- **ဖောက်သည် ပံ့ပိုးမှု** - အေးဂျင့်များသည် CRM စနစ်များ၊ တစ်ကတ် စနစ်များ သို့မဟုတ် အသိပညာအခြေပြု ဗဟုသုတများနှင့် ဆက်သွယ်ပြီး အသုံးပြုသူ မေးခွန်းများ ဖြေရှင်းသည်။
- **အကြောင်းအရာ ဖန်တီးခြင်းနှင့် တည်းဖြတ်ခြင်း** - စာလုံးပေါင်းစစ်သူများ၊ အနှစ်ချုပ်ရေးသူများ သို့မဟုတ် အကြောင်းအရာ လုံခြုံမှု ကိုးကားသူများကဲ့သို့ ကိရိယာများဖြင့် အကြောင်းအရာ ဖန်တီးမှု အလုပ်များကို အထောက်အကူပြုနိုင်သည်။

## ကိရိယာအသုံးပြုမှု ဒီဇိုင်နာပုံစံ အလုပ်လုပ်အောင် တည်ဆောက်ရန် လိုအပ်သည့် အစိတ်အပိုင်းများ/တည်ဆောက်ပစ္စည်းများကဘာများ인가요?

ဤတည်ဆောက်ပစ္စည်းများက AI အေးဂျင့်အား အမျိုးမျိုးသော လုပ်ငန်းများ ပြုလုပ်နိုင်စေရန် ခွင့်ပြုသည်။ Tool Use Design Pattern ကို တည်ဆောက်ရာတွင် လိုအပ်သော အဓိက အစိတ်အပိုင်းများမှာ-

- **ဖင်ရှင်/ကိရိယာ Schema များ** - အသုံးပြုနိုင်သည့် ကိရိယာများ၏ အသေးစိတ် ဖော်ပြချက်များ၊ ဖင်ရှင်နာမည်၊ ရည်ရွယ်ချက်၊ လိုအပ်သည့် ပါရာမီတာများနှင့် မျှော်မှန်းရသော ထုတ်လွှင့်ချက်များပါဝင်သည်။ ဤ schema များက LLM ကို ကိရိယာများ ရှိသည့် နေရာနှင့် မှန်ကန်သော မေးမြန်းမှုများ တည်ဆောက်နည်းကို နားလည်အောင် သက်သေပြသည်။

- **ဖင်ရှင် လုပ်ဆောင်မှု မှန်ကန်မှု** - အသုံးပြုသူ ရည်ရွယ်ချက်နှင့် ဆွေးနွေးမှု အခြေအနေအပေါ်မူတည်၍ ကိရိယာများကို မည်သည့်အချိန် ရည်ရွယ်ပြီး မည်သည့်နည်းဖြင့် ဖိတ်ခေါ်မည်ကို ထိန်းချုပ်သည်။ ဤတွင် အစီအစဉ်ရေးသူ မော်ဂျူးများ၊ လမ်းကြောင်းသတ်မှတ်မှုများ သို့မဟုတ် ကိရိယာအသုံးပြုမှုကို သတ်မှတ်သော အခြေအနေဆိုင်ရာ လမ်းကြောင်းအချိန်များ ပါဝင်နိုင်သည်။

- **သတင်းစကားများ ကိုင်တွယ်မှု စနစ်** - အသုံးပြုသူ၏ အမှာစကားများ၊ LLM ဖြေကြားချက်များ၊ ကိရိယာခေါ်ဆိုမှုများနှင့် ကိရိယာထုတ်လွှင့်ချက်များအကြား ဆက်သွယ်မှုလှုပ်ရှားမှုများကို စီမံခန့်ခွဲသည်။

- **ကိရိယာ ပေါင်းစည်းမှု ဖွဲ့စည်းမှုပုံစံ** - အေးဂျင့်အား ရိုးရှင်းသော ဖင်ရှင်များ ဖြစ်ဖြစ်၊ စိန်ခေါ်မှုများရှိသော ပြင်ပဝန်ဆောင်မှုများ ဖြစ်ဖြစ် ဆက်သွယ်ပေးနိုင်ရန် အခြေခံအင်အားပေးခြင်း။

- **အမှားများ ကိုင်တွယ်မှုနှင့် မှန်ကန်မှု စစ်ဆေးခြင်း** - ကိရိယာများ ရိုက်ခတ်မှုအတွင်း ဖြစ်ပေါ်နိုင်သည့် အဆင်မပြေမှုများကို ကိုင်တွယ်ခြင်း၊ ပါရာမီတာများ အမှန်ပြုခြင်း နှင့် မထင်မှတ်ထားသော တုံ့ပြန်ချက်များ စီမံခန့်ခွဲခြင်း။

- **အခြေအနေစီမံခန့်ခွဲမှု** - ဆွေးနွေးမှု အခြေအနေ၊ ယခင်ကိရိယာအသုံးပြုမှုများနှင့် ပျော်တမ်းမြဲသော ဒေတာများကို စုဆောင်းကာ ပိုမိုအပြတ်အထန် ဆက်လက်ဆောင်ရွက်နိုင်စေရန် ထိန်းသိမ်းသည်။

နောက်ပိုင်းတွင် Function/Tool ခေါ်ဆိုခြင်းအား အသေးစိတ်လေ့လာမည်။

### Function/Tool ခေါ်ဆိုခြင်း

Function ခေါ်ဆိုခြင်းသည် LLM များအား ကိရိယာများနှင့် ဆက်သွယ်နိုင်စေရန် အဓိကနည်းလမ်းဖြစ်သည်။ Function နှင့် Tool ဆိုသော အကြောင်းအရာများကို အတူတူ အသုံးပြုကြသည့်အတွက် Function များ (ပြန်၍ အသုံးချနိုင်သော ကုဒ်ကွက်များ) သည် AI အေးဂျင့်များ လုပ်ငန်းများ ပြုလုပ်ရန် အသုံးပြုသော ကိရိယာများ ဖြစ်ပါသည်။ Function ကို ခေါ်ဆိုနိုင်ရန် LLM သည် အသုံးပြုသူ ပြဿနာတင်ပြချက်ကို ဖင်ရှင် ဖော်ပြချက်နှင့် နှိုင်းယှဥ်ရမည်။ ၎င်းဆောင်ရွက်မှုအတွက် ဖင်ရှင်များ၏ ဖော်ပြချက်များ ပါဝင်သည့် schema ကို LLM သို့ ပို့သည်။ ထို့နောက် LLM သည် အလုပ်အတွက် အသင့်တော်ဆုံး ဖင်ရှင်ကို ရွေးချယ်ပြီး ၎င်း၏နာမည်နှင့် အကြောင်းအရာများကို ပြန်ပေးပို့သည်။ ရွေးချယ်ထားသော ဖင်ရှင်ကို ခေါ်ဆိုပြီး ထုတ်ပြန်ချက်ကို LLM သို့ ပြန်ပို့သည်။ LLM သည် ထိုအချက်အလက်အား အသုံးပြု၍ အသုံးပြုသူ၏ တောင်းဆိုချက်ကို ဖြေကြားသည်။

ဖင်ရှင်ခေါ်ဆိုခြင်းအား အေးဂျင့်ချက်များအနေဖြင့် လက်တွေ့ အသုံးပြုရန်-

1. ဖင်ရှင်ခေါ်ဆိုရန် ပံ့ပိုးသော LLM မော်ဒယ်တစ်ခု
2. ဖင်ရှင်ဖော်ပြချက်များ ပါဝင်သည့် schema တစ်ခု
3. ဖော်ပြထားသည့် ဖင်ရှင်တစ်ခုချင်းစီအတွက် ကုဒ်

မြို့တစ်မြို့ရှိ လက်ရှိအချိန်ရယူနည်းကို ကိုယ့်အချိန်လက္ခဏာအရ ဖေါ်ပြကြမယ်-

1. **ဖင်ရှင်ခေါ်ဆိုမှု ပံ့ပိုးသည့် LLM ကို စတင်အသုံးပြုရန်**

    မော်ဒယ်အားလုံးမှာ ဤလုပ်ဆောင်မှုကို ပံ့ပိုးမှုမရှိသောကြောင့် သုံးနေသည့် LLM သည် function calling ပါဝင်မှုရှိကြောင်း စစ်ဆေးရန် အရေးကြီးသည်။ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> တွင် function calling ပါဝင်သည်။ ကျွန်ုပ်တို့သည် Azure OpenAI client ကို စတင်အသုံးပြုဖြင့် စတင်နိုင်သည်။

    ```python
    # Azure OpenAI client ကို စတင်တပ်ဆင်ပါ။
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Function Schema တစ်ခု ဖန်တီးရန်**:

    နောက်တစ်ဆင့်တွင် function နာမည်၊ ဖင်ရှင်လုပ်ဆောင်ချက်၏ ဖော်ပြချက်၊ ပါရာမီတာများ၏ နာမည်နှင့် ဖော်ပြချက်များပါဝင်သည့် JSON schema တစ်ခုကို သတ်မှတ်ပါမည်။
    ထို schema ကို ယခင်တွင်ဖန်တီးထားသော client အတွက် ဖြန့်ပေးပြီး သုံးစွဲသူ၏ စုံစမ်းမေးမြန်းမှု (San Francisco ၏ အချိန်ကို ရှာဖွေ) နှင့် ပေါင်းထည့်ပေးသည်။ အရေးကြီးစွာ သတိပြုရန်မှာ **ကိရိယာခေါ်ဆိုမှု** ျဖစ္သည့်အတွက် မေးခွန်း၏ နောက်ဆုံးဖြေသည် မဟုတ်ပါ။ LLM သည် အလုပ်အတွက် ရွေးချယ်ထားသော ဖင်ရှင်နာမည်နှင့် ဥပမာအနေနှင့် ထည့်သွင်းရမည့် အချက်အလက်များကို ပြန်လည်ပေးပို့သည်။

    ```python
    # မော်ဒယ်ဖတ်ရန်လုပ်ဆောင်ချက်ဖော်ပြချက်
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
  
    # စတင်အသုံးပြုသူမက်ဆေ့ခ်ျ
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # ပထမဆုံး API ခေါ်ဆိုခြင်း: မော်ဒယ်ကို function ကိုအသုံးပြုရန် တောင်းဆိုပါ
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # မော်ဒယ်၏တုံ့ပြန်ချက်ကို ပြန်လည်ဆန်းစစ်ပါ
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **လုပ်ငန်းကို ဆောင်ရွက်ရန် လိုအပ်သော function ကုဒ်**:

    LLM သည် ဖင်ရှင် ဘယ်ဟာ ရွေးဖို့လိုသည်ဆိုတာ ရွေးပြီး ဖြစ်သည်ဆိုသော်လည်း ယင်းဖင်ရှင်ကို အကောင်အထည် ဖော်ဆောင်ရန် ကုဒ်ရေးသားရန် လိုအပ်သည်။
    Python မှာ လက်ရှိ အချိန် ရယူရန် ကုဒ်အတွက် ဖန်တီးနိုင်သည်။ ရလဒ်နောက်ဆုံးထွက်ရန် response_message မှ ဖင်ရှင် နာမည်နှင့် ပါရာမီတာများကို ရယူရန်လည်း ကုဒ်ကို ရေးသားရမည်ဖြစ်သည်။

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
     # function ခေါ်ယူချက်များကို ကိုင်တွယ်သည်
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
  
      # ဒုတိယ API ခေါ်ယူချက်: မော်ဒယ်မှ နောက်ဆုံးဖြေကြားချက်ကို ရယူသည်
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

Function calling သည် အများစု (သို့) အားလုံးအတွက် ကိရိယာအသုံးပြုမှု ဒီဇိုင်နာတွင် အခြေခံ အစိတ်အပိုင်းဖြစ်သော်လည်း စတင်ဆောင်ရွက်ရာတွင် ခက်ခဲနိုင်ပါသည်။ [Lesson 2](../../../02-explore-agentic-frameworks) တွင် သင်ကြားသည့်အတိုင်း agentic framework များသည် ကိရိယာအသုံးပြုမှုဆောင်ရွက်ရာ အတွက် ဖန်တီးထားသည့် အဆောက်အအုံများ ပေးသည်။

## Agentic Framework များနှင့် ကိရိယာအသုံးပြုမှု လုပ်ငန်းများ နမူနာများ

အောက်ပါအတိုင်း အမျိုးမျိုးသော agentic framework များ အသုံးပြု၍ Tool Use Design Pattern ကို မည်သို့ ဆောင်ရွက်နိုင်သည်ကို ကြည့်မည်-

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> သည် AI အေးဂျင့်များ ဖန်တီးရန် အဆင့်မြှင့် လွယ်ကူသည့် ဖွင့်လှစ်သော AI framework တစ်ခု ဖြစ်သည်။ function calling အသုံးပြုစနစ်ကို ပိုမိုလွယ်ကူစေရန် @tool decorator ဖြင့် Python function များကို ကိရိယာအဖြစ် သတ်မှတ်ခွင့်ပေးသည်။ framework သည် မော်ဒယ်နှင့် ကုဒ်အကြား ဆက်သွယ်မှုများကို ကိုင်တွယ်ပေးသည်။ File Search နှင့် Code Interpreter ကဲ့သို့ ရေးသားပြီးသား ကိရိယာများကို `AzureAIProjectAgentProvider` မှတဆင့် အသုံးပြုခွင့်ရှိသည်။

အောက်ပါပုံသည် Microsoft Agent Framework ဖြင့် function calling လုပ်ငန်းစဉ်ကို ဖော်ပြသည်-

![function calling](../../../translated_images/my/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework တွင် ကိရိယာများကို decorator function အဖြစ် သတ်မှတ်ပေးသည်။ ယခင်တွင် ကြည့်ရှုခဲ့သော `get_current_time` ဖင်ရှင်ကို `@tool` decorator သုံးပြီး ကိရိယာတစ်ခုကဲ့သို့ ပြောင်းလဲပြုလုပ်နိုင်သည်။ framework သည် function နှင့် ၎င်း၏ ပါရာမီတာများကို ကိုယ်တိုင် serialize လုပ်ပြီး LLM သို့ ပို့ရန် schema ဖန်တီးပေးသည်။

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# client ကိုဖန်တီးပါ
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# agent တစ်ခုဖန်တီးပြီး တူးလ်နှင့်အသုံးပြုပါ
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> သည် နောက်ဆုံးသော agentic framework ဖြစ်ပြီး၊ underlying compute နှင့် storage အရင်းအမြစ်များကို မောင်းနှင်စီမံရန် မလိုအပ်ဘဲ အဆင်ပြေသော AI အေးဂျင့်များ ဖန်တီး၊ တပ်ဆင် နှင့် အတိုင်းအတာချိန်ညှိမှုကို အလွယ်တကူ ပြုလုပ်ရမည့် Developer များအတွက် ထူးခြားသော အင်ကြင်းရှင်တယောက်ဖြစ်သည်။ လုပ်ငန်းအသုံးပြုမှုများတွင် အထူးအသုံးဝင်ပြီး management လုပ်ဆောင်ချက်မြင့်မားသော အနုပညာစနစ်ကို ပေးစွမ်းနိုင်သည်။

LLM API ဖြင့် တိုက်ရိုက် ဖွံ့ဖြိုးနေစဉ်နှိုင်းယှဉ်ပါက၊ Azure AI Agent Service သည် နောက်ကျောစံချိန်များ ပါဝင်သည်-

- ကိရိယာခေါ်ဆိုမှုအလိုအလျောက် ဆောင်ရွက်ခြင်း – tool call ကို ဖြေဖျောက်ခြင်း၊ tool ကို ဖိတ်ခေါ်ခြင်း နှင့် တုံ့ပြန်ချက် ကို server-အနေဖြင့်စီမံခန့်ခွဲခြင်း။
- ဒေတာကို ဘေးကင်းစွာ စီမံခြင်း – တိုက်ဆိုင်စကားပြောမှု အခြေအနေ ကိုသူသုံးသူနှစ်ဦးကြား နားလည်မှုများစာရင်း `threads` တွင် သိမ်းဆည်းခြင်း။
- အခြေခံကိရိယာများ – Bing, Azure AI Search နှင့် Azure Functions ကဲ့သို့ ဒေတာပြင်များနှင့် ဆက်သွယ်ရန် ကိရိယာများ။

Azure AI Agent Service တွင် ရရှိနိုင်သော ကိရိယာများကို နှစ်မျိုးခွဲနိုင်သည်-

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ဖြင့် အခြေခံခြင်း</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI သတ်မှတ်ထားသော ကိရိယာများ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service သည် ဤကိရိယာများအား `toolset` အဖြစ် အတူတကွ အသုံးပြုနိုင်ရန် ခွင့်ပြုသည်။ ထို့ဖြင့် `threads` ကိုတစ်ပြိုင်နက် အကြောင်းအရာ သမိုင်းကြောင်း အဖြစ် ထိန်းသိမ်းနိုင်သည်။

သင်သည် Contoso ဟူသော ကုမ္ပဏီတွင် ရောင်းအား အေးဂျင့်တစ်ဦးဖြစ်ကြောင်း စဥ်းစားပါ။ သင်သည် ဝယ်လိုသူ ရောင်းအားဒေတာများနှင့် ပတ်သက်၍ မေးခွန်းများကို ဖြေရှင်းနိုင်သော ဆွေးနွေးမှု AI အေးဂျင့် တည်ဆောက်လိုသည်။

အောက်ပါ ပုံသည် Azure AI Agent Service ကို အသုံးပြု၍ သင်၏ ရောင်းအား ဒေတာများကို စိစစ်ခြင်းနည်းလမ်းကို ဖော်ပြသည်-

![Agentic Service In Action](../../../translated_images/my/agent-service-in-action.34fb465c9a84659e.webp)

ဤကိရိယာတစ်ခုချင်းအား service နှင့် အသုံးပြုရန် client တစ်ခု ဖန်တီးကာ tool သို့မဟုတ် toolset တစ်ခု သတ်မှတ်ရမည်။ လက်တွေ့ရန်အတွက် Python ကုဒ်ကို အသုံးပြုနိုင်သည်။ LLM သည် toolset ကို ကြည့်ပြီး အသုံးပြုသူဖန်တီးထားသော function `fetch_sales_data_using_sqlite_query` သို့မဟုတ် ရေးသားပြီးသား Code Interpreter ကို အသုံးပြုရန်ဆုံးဖြတ်ရန် လွယ်ကူသည်။

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function ကို fetch_sales_data_functions.py ဖိုင်ထဲမှာတွေ့နိုင်ပါတယ်။
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ကိရိယာစနစ်ကို စတင်ချိန်တင်ပါ။
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query function နှင့် function calling agent ကို စတင်ချိန်တင်ပြီး toolset ထဲထည့်ပါ။
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter ကိရိယာကို စတင်ချိန်တင်ပြီး toolset ထဲထည့်ပါ။
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ယုံကြည်စိတ်ချရသော AI အေးဂျင့် ဖန်တီးရာတွင် ကိရိယာအသုံးပြုမှု ဒီဇိုင်နာပုံစံကို အသုံးပြုသည့်အခါ အထူးသတိပြုရန် အချက်များကဘာများ인가요?

LLM များမှ dynamic အနေဖြင့် ဖန်တီးသည့် SQL query များအား ထိန်းချုပ်ရာတွင် ဘေးကင်းရေးကိစ္စများသည် အရေးကြီးသည်၊ အထူးသဖြင့် SQL injection သို့မဟုတ် မကောင်းမွန်သော လုပ်ဆောင်ချက်များဖြစ်သည့် database ကို ဖျက်ဆီးခြင်း သို့မဟုတ် ပြင်ဆင်ခြင်းတို့ ဖြစ်နိုင်ခြေရှိသည်။ ဤသတိပေးချက်များမှာ တကယ်တင်းကျပ်သည်မဟုတ်ပေမယ့်၊ database access permissions များကို သင့်တော်စွာ ဖန်တီးထိန်းသိမ်းခြင်းဖြင့် ထိရောက်စွာ ကာကွယ်နိုင်သည်။ database များအများစုအနေဖြင့် read-only အဖြစ် သတ်မှတ်နိုင်သည်။ PostgreSQL သို့ Azure SQL ကဲ့သို့ database ဝန်ဆောင်မှုများအတွက် app ကို read-only (SELECT) role ပေးသင့်သည်။

application ကို ဘေးကင်းသော ပတ်ဝန်းကျင်တွင် ပြေးဆွဲခြင်းကာကွယ်မှုအား ပိုမိုတိုးတက်စေသည်။ လုပ်ငန်းအသုံးပြုမှုများတွင်၊ ဒေတာများကို operational system များမှ ဖျော်ဖြေထုတ်ယူကာ အသုံးပြုရလွယ်ကူသော schema တစ်ခုပါရှိသော read-only database သို့ data warehouse ‌သို့ပြောင်းလဲသည်။ ဤနည်းလမ်းသည် ဒေတာ အားလုံးကို ကာကွယ်မှုရှိစေကာ ဆောင်ရွက်မှုနှင့်လွယ်ကူရေးကို တိုးတတ်စေပြီး application သည် ရှေ့ပြေးပြသော read-only access ကို ခံစားသည်။

## နမူနာကုဒ်များ

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံများနောက်ထပ် မေးခွန်းများ ရှိပါသလား?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) တွင် တက်ရောက်လိုက်ပါ၊ အခြားအာရုံစူးစိုက်သူများနှင့် တွေ့ဆုံကာ ရုံးချိန်တွေတက်ရောက်၍ သင်၏ AI အေးဂျင့် မေးခွန်းများကို ဖြေကြားနိုင်ပါသည်။

## ထပ်ဆင့် အရင်းအမြစ်များ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service လေ့ကျင့်ရေး</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent လေ့ကျင့်ရေး</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework အကျဉ်းချုပ်</a>

## ယခင်သင်ခန်းစာ

[Agentic Design Patterns ကို နားလည်ခြင်း](../03-agentic-design-patterns/README.md)

## နောက်တစ်ခန်းစာ
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**သတိပေးချက်**  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်မှုပေးမည့် [Co-op Translator](https://github.com/Azure/co-op-translator) ဝန်ဆောင်မှုမှ အသုံးပြုပြီး ဘာသာပြန်ထားပါသည်။ ကျွန်တော်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသောကြောင့် ဖြစ်ပေမယ့် အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါရှိနိုင်ကြောင်း သတိထားကြပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာရွက်စာတမ်းသည် မိမိဘာသာစကားဖြင့် ရေးသားထားသည့် အရာဖြစ်၍ အာဏာပိုင်အချက်အလက်အနေဖြင့် ယူဆရမည်ဖြစ်သည်။ အရေးပါသော အချက်အလက်များအတွက် တက္ကသိုလ်ရှင် သို့မဟုတ် ပညာရှင်လူမှုအဖွဲ့ကတိပြုထားသော ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကိုအသုံးပြုမှုမှဆင်းရဲမှုများ သို့မဟုတ် ဖြစ်ပေါ်လာနိုင်သော စကားချိုးမှုများ အတွက် ကျွန်တော်တို့မှာ တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->