# အေးဂျင်တစ် RAG (Agentic RAG)

[![အေးဂျင်တစ် RAG](./images/lesson-5-thumbnail.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရှုရန် အထက်ပါ ပုံကို နှိပ်ပါ)_

# အေးဂျင်တစ် RAG (Agentic RAG)

ဤသင်ခန်းစာသည် အေးဂျင်တစ် ရီထရီဗယ်-အောက်မင်တက်ဒ် ဂျင်နရေးရှင်း (Agentic RAG) ၏ ကျယ်ပြန့်သော အခြေခံဗဟုသုတကို ပေးစွမ်းပါသည်။ ၎င်းသည် ကြီးမားသော ဘာသာစကား မော်ဒယ်များ (LLMs) သည် ပြင်ပအချက်အလက်ရင်းမြစ်များမှ အချက်အလက်များကို ရယူနေစဉ် ၎င်းတို့၏နောက်ဆုံးအဆင့်များကို အလိုအလျောက် စီစဉ်သည့် ပေါ်ထွက်လာသော AI နည်းပညာတစ်ခုဖြစ်ပါသည်။ ထုံးစံအတိုင်း ရယူ-ထို့နောက်-ဖတ် ပုံစံများနှင့် မတူဘဲ၊ အေးဂျင်တစ် RAG တွင် LLM သို့ အကြိမ်ကြိမ် ခေါ်ဆိုမှုများ၊ ကိရိယာ သို့မဟုတ် လုပ်ဆောင်ချက်ခေါ်ဆိုမှုများနှင့် ဖွဲ့စည်းတည်ဆောက်ထားသော ရလဒ်များ ပါဝင်ပါသည်။ စနစ်သည် ရလဒ်များကို အကဲဖြတ်ပြီး၊ မေးခွန်းများကို ပြန်လည်ပြင်ဆင်ကာ၊ လိုအပ်လျှင် ထပ်မံကိရိယာများကို အသုံးပြုပြီး၊ ကျေနပ်ဖွယ်ရာ ဖြေရှင်းချက်ရရှိသည်အထိ ဤလုပ်ငန်းစဉ်ကို ဆက်လက်လုပ်ဆောင်ပါသည်။

## မိတ်ဆက်

ဤသင်ခန်းစာတွင် အောက်ပါအကြောင်းအရာများ ပါဝင်ပါသည်-

- **အေးဂျင်တစ် RAG ကို နားလည်ခြင်း:** ကြီးမားသော ဘာသာစကား မော်ဒယ်များ (LLMs) သည် ပြင်ပအချက်အလက်ရင်းမြစ်များမှ အချက်အလက်များကို ရယူနေစဉ် ၎င်းတို့၏နောက်ဆုံးအဆင့်များကို အလိုအလျောက် စီစဉ်သည့် AI တွင် ပေါ်ထွက်လာသော နည်းပညာအကြောင်း လေ့လာပါ။
- **အကြိမ်ကြိမ် မေကာ-ချက်ကာ ပုံစံကို နားလည်ခြင်း:** ကိရိယာ သို့မဟုတ် လုပ်ဆောင်ချက်ခေါ်ဆိုမှုများနှင့် ဖွဲ့စည်းတည်ဆောက်ထားသော ရလဒ်များဖြင့် ရောယှက်ထားသော LLM သို့ အကြိမ်ကြိမ်ခေါ်ဆိုမှုများ၏ လှည့်ပတ်မှုကို နားလည်ပါ၊ ၎င်းသည် တိကျမှန်ကန်မှုကို မြှင့်တင်ရန်နှင့် ပုံစံမမှန်သော မေးခွန်းများကို ကိုင်တွယ်ရန် ဒီဇိုင်းထုတ်ထားပါသည်။
- **လက်တွေ့အသုံးချမှုများကို စူးစမ်းလေ့လာခြင်း:** တိကျမှန်ကန်မှုကို ဦးစားပေးသော ပတ်ဝန်းကျင်များ၊ ရှုပ်ထွေးသော ဒေတာဘေ့စ် အပြန်အလှန်တုံ့ပြန်မှုများနှင့် တိုးချဲ့ထားသော လုပ်ငန်းစဉ်များကဲ့သို့သော အေးဂျင်တစ် RAG ထွန်းကားသော အခြေအနေများကို ခွဲခြားသတ်မှတ်ပါ။

## သင်ယူရန် ရည်မှန်းချက်များ

ဤသင်ခန်းစာကို ပြီးဆုံးပြီးနောက်၊ သင်သည် အောက်ပါအကြောင်းအရာများကို သိရှိ/နားလည်လာမည်ဖြစ်ပါသည်-

- **အေးဂျင်တစ် RAG ကို နားလည်ခြင်း:** ကြီးမားသော ဘာသာစကား မော်ဒယ်များ (LLMs) သည် ပြင်ပအချက်အလက်ရင်းမြစ်များမှ အချက်အလက်များကို ရယူနေစဉ် ၎င်းတို့၏နောက်ဆုံးအဆင့်များကို အလိုအလျောက် စီစဉ်သည့် AI တွင် ပေါ်ထွက်လာသော နည်းပညာအကြောင်း လေ့လာပါ။
- **အကြိမ်ကြိမ် မေကာ-ချက်ကာ ပုံစံ:** တိကျမှန်ကန်မှုကို မြှင့်တင်ရန်နှင့် ပုံစံမမှန်သော မေးခွန်းများကို ကိုင်တွယ်ရန် ဒီဇိုင်းထုတ်ထားသော ကိရိယာ သို့မဟုတ် လုပ်ဆောင်ချက်ခေါ်ဆိုမှုများနှင့် ဖွဲ့စည်းတည်ဆောက်ထားသော ရလဒ်များဖြင့် ရောယှက်ထားသော LLM သို့ အကြိမ်ကြိမ်ခေါ်ဆိုမှုများ၏ လှည့်ပတ်မှု၏ အယူအဆကို နားလည်ခြင်း။
- **ဆင်ခြင်တုံတရား လုပ်ငန်းစဉ်ကို ပိုင်ဆိုင်ခြင်း:** ကြိုတင်သတ်မှတ်ထားသော လမ်းကြောင်းများပေါ် မှီခိုမှုမရှိဘဲ ပြဿနာများကို မည်သို့ချဉ်းကပ်ရမည်ကို ဆုံးဖြတ်ချက်ချသည့် စနစ်၏ ၎င်း၏ဆင်ခြင်တုံတရား လုပ်ငန်းစဉ်ကို ပိုင်ဆိုင်နိုင်သည့် စွမ်းရည်ကို နားလည်ခြင်း။
- **လုပ်ငန်းစဉ်:** စျေးကွက်ခေါင်းပါးမှု အစီရင်ခံစာများကို ရယူရန်၊ ပြိုင်ဘက်အချက်အလက်များကို ခွဲခြားသတ်မှတ်ရန်၊ အတွင်းပိုင်း ရောင်းချရေး မက်ထရစ်များကို ဆက်စပ်ရန်၊ တွေ့ရှိချက်များကို ပေါင်းစပ်ရန်နှင့် မဟာဗျူဟာကို အကဲဖြတ်ရန် အေးဂျင်တစ် မော်ဒယ်တစ်ခုသည် မည်သို့ လွတ်လပ်စွာ ဆုံးဖြတ်သည်ကို နားလည်ခြင်း။
- **အကြိမ်ကြိမ် လှည့်ပတ်မှုများ၊ ကိရိယာ ပေါင်းစပ်မှုနှင့် မှတ်ဉာဏ်:** ထပ်ခါထပ်ခါ လှည့်ပတ်မှုများကို ရှောင်ရှားရန်နှင့် အသိအမြင်ရှိသော ဆုံးဖြတ်ချက်များ ချရန် အဆင့်များအကြား အခြေအနေနှင့် မှတ်ဉာဏ်ကို ထိန်းသိမ်းထားသော လှည့်ပတ်သည့် အပြန်အလှန်တုံ့ပြန်မှု ပုံစံပေါ် စနစ်၏ မှီခိုမှုကို လေ့လာခြင်း။
- **ပျက်ကွက်မှု မော်ဒများနှင့် မိမိကိုယ်ကို ပြင်ဆင်ခြင်းကို ကိုင်တွယ်ခြင်း:** အကြိမ်ကြိမ် ပြန်လည်မေးခွန်းထုတ်ခြင်း၊ ရောဂါရှာဖွေရေး ကိရိယာများကို အသုံးပြုခြင်းနှင့် လူ့ကြီးကြပ်မှုပေါ် နောက်ကျခြင်းများ အပါအဝင် စနစ်၏ ခိုင်မာသော မိမိကိုယ်ကို ပြင်ဆင်ခြင်း ယန္တရားများကို စူးစမ်းလေ့လာခြင်း။
- **အေးဂျင်စီ၏ နယ်နိမိတ်များ:** ဒိုမိန်းအလိုက် လွတ်လပ်မှု၊ အခြေခံအဆောက်အအုံ မှီခိုမှုနှင့် ကန့်သတ်ချက်များကို လေးစားခြင်းကို အာရုံစိုက်ကာ အေးဂျင်တစ် RAG ၏ ကန့်သတ်ချက်များကို နားလည်ခြင်း။
- **လက်တွေ့အသုံးချမှုများနှင့် တန်ဖိုး:** တိကျမှန်ကန်မှုကို ဦးစားပေးသော ပတ်ဝန်းကျင်များ၊ ရှုပ်ထွေးသော ဒေတာဘေ့စ် အပြန်အလှန်တုံ့ပြန်မှုများနှင့် တိုးချဲ့ထားသော လုပ်ငန်းစဉ်များကဲ့သို့သော အေးဂျင်တစ် RAG ထွန်းကားသော အခြေအနေများကို ခွဲခြားသတ်မှတ်ခြင်း။
- **အုပ်ချုပ်မှု၊ ဖေါ်ထုတ်မှုနှင့် ယုံကြည်မှု:** အကြောင်းပြချက်ရှင်းလင်းနိုင်မှု၊ ဘက်လိုက်မှု ထိန်းချုပ်မှုနှင့် လူ့ကြီးကြပ်မှု အပါအဝင် အုပ်ချုပ်မှုနှင့် ဖေါ်ထုတ်မှု၏ အရေးပါမှုကို လေ့လာခြင်း။

## အေးဂျင်တစ် RAG ဆိုသည်မှာ အဘယ်နည်း?

အေးဂျင်တစ် ရီထရီဗယ်-အောက်မင်တက်ဒ် ဂျင်နရေးရှင်း (Agentic RAG) သည် ကြီးမားသော ဘာသာစကား မော်ဒယ်များ (LLMs) သည် ပြင်ပရင်းမြစ်များမှ အချက်အလက်များကို ရယူနေစဉ် ၎င်းတို့၏နောက်ဆုံးအဆင့်များကို အလိုအလျောက် စီစဉ်သည့် ပေါ်ထွက်လာသော AI နည်းပညာတစ်ခုဖြစ်ပါသည်။ ထုံးစံအတိုင်း ရယူ-ထို့နောက်-ဖတ် ပုံစံများနှင့် မတူဘဲ၊ အေးဂျင်တစ် RAG တွင် LLM သို့ အကြိမ်ကြိမ် ခေါ်ဆိုမှုများ၊ ကိရိယာ သို့မဟုတ် လုပ်ဆောင်ချက်ခေါ်ဆိုမှုများနှင့် ဖွဲ့စည်းတည်ဆောက်ထားသော ရလဒ်များ ပါဝင်ပါသည်။ စနစ်သည် ရလဒ်များကို အကဲဖြတ်ပြီး၊ မေးခွန်းများကို ပြန်လည်ပြင်ဆင်ကာ၊ လိုအပ်လျှင် ထပ်မံကိရိယာများကို အသုံးပြုပြီး၊ ကျေနပ်ဖွယ်ရာ ဖြေရှင်းချက်ရရှိသည်အထိ ဤလုပ်ငန်းစဉ်ကို ဆက်လက်လုပ်ဆောင်ပါသည်။ ဤအကြိမ်ကြိမ် "မေကာ-ချက်ကာ" ပုံစံသည် တိကျမှန်ကန်မှုကို မြှင့်တင်ရန်၊ ပုံစံမမှန်သော မေးခွန်းများကို ကိုင်တွယ်ရန်နှင့် အရည်အသွေးမြင့် ရလဒ်များကို သေချာစေရန် ရည်ရွယ်ပါသည်။

စနစ်သည် ၎င်း၏ဆင်ခြင်တုံတရား လုပ်ငန်းစဉ်ကို တက်ကြွစွာ ပိုင်ဆိုင်ကာ၊ ပျက်ကွက်သော မေးခွန်းများကို ပြန်လည်ရေးသားခြင်း၊ မတူကွဲပြားသော ရယူရေး နည်းလမ်းများကို ရွေးချယ်ခြင်းနှင့် Azure AI Search တွင် vector search၊ SQL ဒေတာဘေ့စ်များ သို့မဟုတ် စိတ်ကြိုက် APIs များကဲ့သို့သော ကိရိယာများစွာကို ပေါင်းစပ်ခြင်းတို့ကို ၎င်း၏အဖြေကို အပြီးအစီး မပြုလုပ်မီ လုပ်ဆောင်ပါသည်။ အေးဂျင်တစ် စနစ်တစ်ခု၏ ထူးခြားသော အရည်အသွေးမှာ ၎င်း၏ဆင်ခြင်တုံတရား လုပ်ငန်းစဉ်ကို ပိုင်ဆိုင်နိုင်သည့် စွမ်းရည်ဖြစ်ပါသည်။ ရိုးရာ RAG အကောင်အထည်ဖေါ်မှုများသည် ကြိုတင်သတ်မှတ်ထားသော လမ်းကြောင်းများပေါ် မှီခိုကြသော်လည်း၊ အေးဂျင်တစ် စနစ်သည် ၎င်းရှာဖွေတွေ့ရှိသော အချက်အလက်၏ အရည်အသွေးကို အခြေခံ၍ အဆင့်များ၏ အစီအစဉ်ကို အလိုအလျောက် သတ်မှတ်ပါသည်။

## အေးဂျင်တစ် ရီထရီဗယ်-အောက်မင်တက်ဒ် ဂျင်နရေးရှင်း (အေးဂျင်တစ් RAG) ကို သတ်မှတ်ခြင်း

အေးဂျင်တစ် ရီထရီဗယ်-အောက်မင်တက်ဒ် ဂျင်နရေးရှင်း (အေးဂျင်တစ် RAG) သည် LLMs များသည် ပြင်ပအချက်အလက်ရင်းမြစ်များမှ အချက်အလက်များကို ရယူရုံမက ၎င်းတို့၏နောက်ဆုံးအဆင့်များကိုပါ အလိုအလျောက် စီစဉ်သည့် AI ဖွံ့ဖြိုးတိုးတက်မှုတွင် ပေါ်ထွက်လာသော နည်းပညာတစ်ခုဖြစ်ပါသည်။ တည်ငြိမ်သော ရယူ-ထို့နောက်-ဖတ် ပုံစံများ သို့မဟုတ် ဂရုတစိုက် ရေးသားထားသော ညွှန်ပြချက် အစီအစဉ်များနှင့် မတူဘဲ၊ အေးဂျင်တစ် RAG တွင် ကိရိယာ သို့မဟုတ် လုပ်ဆောင်ချက်ခေါ်ဆိုမှုများနှင့် ဖွဲ့စည်းတည်ဆောက်ထားသော ရလဒ်များဖြင့် ရောယှက်ထားသော LLM သို့ အကြိမ်ကြိမ်ခေါ်ဆိုမှုများ၏ လှည့်ပတ်မှုများ ပါဝင်ပါသည်။ အချိန်တိုင်းတွင်၊ စနစ်သည် ၎င်းရရှိထားသော ရလဒ်များကို အကဲဖြတ်ပြီး၊ ၎င်း၏မေးခွန်းများကို ပြန်လည်ပြင်ဆင်ရန် ဆုံးဖြတ်လျှင်၊ လိုအပ်လျှင် ထပ်မံကိရိယာများကို အသုံးပြုပြီး၊ ကျေနပ်ဖွယ်ရာ ဖြေရှင်းချက်ရရှိသည်အထိ ဤလုပ်ငန်းစဉ်ကို ဆက်လက်လုပ်ဆောင်ပါသည်။

ဤအကြိမ်ကြိမ် "မေကာ-ချက်ကာ" လုပ်ဆောင်မှု ပုံစံသည် တိကျမှန်ကန်မှုကို မြှင့်တင်ရန်၊ ဖွဲ့စည်းတည်ဆောက်ထားသော ဒေတာဘေ့စ်များသို့ ပုံစံမမှန်သော မေးခွန်းများ (ဥပမာ- NL2SQL) ကို ကိုင်တွယ်ရန်နှင့် မျှတကွဲလွဲ၊ အရည်အသွေးမြင့် ရလဒ်များကို သေချာစေရန် ဒီဇိုင်းထုတ်ထားပါသည်။ ဂရုတစိုက် အင်ဂျင်နီယာလုပ်ထားသော ညွှန်ပြချက် ကွင်းဆက်များပေါ်မှာ အချည်းနှီး မှီခိုမှုထက်၊ စနစ်သည် ၎င်း၏ဆင်ခြင်တုံတရား လုပ်ငန်းစဉ်ကို တက်ကြွစွာ ပိုင်ဆိုင်ပါသည်။ ၎င်းသည် ပျက်ကွက်သော မေးခွန်းများကို ပြန်လည်ရေးသားနိုင်၊ မတူကွဲပြားသော ရယူရေး နည်းလမ်းများကို ရွေးချယ်နိုင်ပြီး Azure AI Search တွင် vector search၊ SQL ဒေတာဘေ့စ်များ သို့မဟုတ် စိတ်ကြိုက် APIs များကဲ့သို့သော ကိရိယာများစွာကို ပေါင်းစပ်ကာ ၎င်း၏အဖြေကို အပြီးအစီး မပြုလုပ်မီ လုပ်ဆောင်နိုင်ပါသည်။ ဤသည်က အလွန်ရှုပ်ထွေးသော စီမံခန့်ခွဲမှု framework များ၏ လိုအပ်ချက်ကို ဖယ်ရှားပေးပါသည်။ ၎င်း၏အစား၊ "LLM ခေါ်ဆိုမှု → ကိရိယာအသုံးပြုမှု → LLM ခေါ်ဆိုမှု → …" ဟူသော ရိုးရှင်းသော လှည့်ပတ်မှုသည် ရှုပ်ထွေးပြီး ကောင်းမွန်စွာ အခြေခံထားသော ရလဒ်များကို ထုတ်ပေးနိုင်ပါသည်။

![အေးဂျင်တစ် RAG အဓိက လှည့်ပတ်မှု](./images/agentic-rag-core-loop.png)

## ဆင်ခြင်တုံတရား လုပ်ငန်းစဉ်ကို ပိုင်ဆိုင်ခြင်း

စနစ်တစ်ခုကို "အေးဂျင်တစ်" ဖြစ်စေသည့် ထူးခြားသော အရည်အသွေးမှာ ၎င်း၏ဆင်ခြင်တုံတရား လုပ်ငန်းစဉ်ကို ပိုင်ဆိုင်နိုင်သည့် စွမ်းရည်ဖြစ်ပါသည်။ ရိုးရာ RAG အကောင်အထည်ဖေါ်မှုများသည် မကြာခဏ လူများက မော်ဒယ်အတွက် လမ်းကြောင်းကို ကြိုတင်သတ်မှတ်ပေးခြင်းပေါ် မှီခိုကြပါသည်- မည်သည့်အရာကို ရယူရမည်နှင့် မည်သည့်အချိန်တွင် ရယူရမည်ကို ဖေါ်ပြသည့် ဆင်ခြင်တုံတရား ကွင်းဆက်တစ်ခုဖြစ်ပါသည်။
သို့သော် စနစ်သည် အမှန်တကယ် အေးဂျင်တစ် ဖြစ်သောအခါ၊ ၎င်းသည် ပြဿနာကို မည်သို့ချဉ်းကပ်ရမည်ကို အတွင်းမှ ဆုံးဖြတ်ပါသည်။ ၎င်းသည် script တစ်ခုကိုသာ လုပ်ဆောင်ခြင်းမဟုတ်ဘဲ၊ ၎င်းရှာဖွေတွေ့ရှိသော အချက်အလက်၏ အရည်အသွေးကို အခြေခံ၍ အဆင့်များ၏ အစီအစဉ်ကို အလိုအလျောက် သတ်မှတ်ခြင်းဖြစ်ပါသည်။
ဥပမာအားဖြင့်၊ ၎င်းအား ထုတ်ကုန်မိတ်ဆက်မဟာဗျူဟာ ဖန်တီးရန် တောင်းဆိုလျှင်၊ ၎င်းသည် တစ်ခုလုံးသော သုတေသနနှင့် ဆုံးဖြတ်ချက်ချမှု လုပ်ငန်းစဉ်ကို ဖေါ်ပြသည့် ညွှန်ပြချက်တစ်ခုပေါ်တွင်သာ မှီခိုခြင်းမရှိပါ။ ၎င်း၏အစား၊ အေးဂျင်တစ် မော်ဒယ်သည် လွတ်လပ်စွာ ဆုံးဖြတ်ပါသည်-

1. Bing Web Grounding ကို အသုံးပြု၍ လက်ရှိ စျေးကွက်ခေါင်းပါးမှု အစီရင်ခံစာများကို ရယူခြင်း
2. Azure AI Search ကို အသုံးပြု၍ ဆက်စပ်သော ပြိုင်ဘက်အချက်အလက်များကို ခွဲခြားသတ်မှတ်ခြင်း
3. Azure SQL Database ကို အသုံးပြု၍ သမိုင်း ကြောင်းဆိုင်ရာ အတွင်းပိုင်း ရောင်းချရေး မက်ထရစ်များကို ဆက်စပ်ခြင်း
4. Azure OpenAI Service မှတစ်ဆင့် စီမံခန့်ခွဲ၍ တွေ့ရှိချက်များကို ဖြေရှင်းနိုင်သော မဟာဗျူဟာအဖြစ် ပေါင်းစပ်ခြင်း
5. မဟာဗျူဟာကို ကွာဟချက်များ သို့မဟုတ် ကိုက်ညီမှုမရှိမှုများအတွက် အကဲဖြတ်ကာ၊ လိုအပ်လျှင် နောက်ထပ် ရယူမှုများ လုပ်ဆောင်ရန် တိုက်တွန်းခြင်း

ဤအဆင့်များအားလုံး—မေးခွန်းများကို ပြန်လည်ပြင်ဆင်ခြင်း၊ ရင်းမြစ်များကို ရွေးချယ်ခြင်း၊ အဖြေနှင့်ပတ်သက်၍ "ကျေနပ်သည်" အထိ ပြန်လည်လုပ်ဆောင်ခြင်း—တို့သည် လူတစ်ဦးမှ ကြိုတင်ရေးသားထားသော script မဟုတ်ဘဲ၊ မော်ဒယ်မှ ဆုံးဖြတ်သည့် အရာများဖြစ်ပါသည်။

## အကြိမ်ကြိမ် လှည့်ပတ်မှုများ၊ ကိရိယာ ပေါင်းစပ်မှုနှင့် မှတ်ဉာဏ်

![ကိရိယာ ပေါင်းစပ်မှု ဗိသုကာပညာ](./images/tool-integration.png)

အေးဂျင်တစ် စနစ်သည် လှည့်ပတ်သည့် အပြန်အလှန်တုံ့ပြန်မှု ပုံစံပေါ် မှီခိုပါသည်-

- **ကနဦး ခေါ်ဆိုမှု:** အသုံးပြုသူ၏ ရည်မှန်းချက် (ဆိုလိုသည်မှာ အသုံးပြုသူ ညွှန်ပြချက်) ကို LLM သို့ တင်ပြပါသည်။
- **ကိရိယာ အသုံးပြုမှု:** မော်ဒယ်သည် ပျောက်ဆုံးနေသော အချက်အလက်များ သို့မဟုတ် မရေရာသော ညွှန်ကြားချက်များကို ခွဲခြားသတ်မှတ်လျှင်၊ ၎င်းသည် ကိရိယာ သို့မဟုတ် ရယူရေး နည်းလမ်းတစ်ခုကို ရွေးချယ်ပါသည်—ဥပမာ vector database မေးခွန်းထုတ်မှု (ဥပမာ- သီးသန့်အချက်အလက်များပေါ် Azure AI Search Hybrid search) သို့မဟုတ် ဖွဲ့စည်းတည်ဆောက်ထားသော SQL ခေါ်ဆိုမှု—ကို ပိုမိုအကြောင်းအရာ စုဆောင်းရန် အသုံးပြုပါသည်။
- **အကဲဖြတ်မှုနှင့် ပြန်လည်ပြင်ဆင်မှု:** ပြန်လာသော အချက်အလက်များကို ပြန်လည်သုံးသပ်ပြီးနောက်၊ မော်ဒယ်သည် အချက်အလက်များ လုံလောက်မှုရှိမရှိ ဆုံးဖြတ်ပါသည်။ မလုံလောက်လျှင်၊ ၎င်းသည် မေးခွန်းကို ပြန်လည်ပြင်ဆင်၊ မတူကွဲပြားသော ကိရိယာကို စမ်းသုံး သို့မဟုတ် ၎င်း၏ချဉ်းကပ်မှုကို ပြင်ဆင်ပါသည်။
- **ကျေနပ်သည်အထိ ပြန်လည်လုပ်ဆောင်:** မော်ဒယ်သည် နောက်ဆုံး၊ ကောင်းမွန်စွာ ဆင်ခြင်တုံတရားပြုထားသော တုံ့ပြန်မှုကို ပေးဆောင်ရန် လုံလောက်သော ရှင်းလင်းမှုနှင့် အထောက်အထားများ ရှိသည်ဟု ဆုံးဖြတ်သည်အထိ ဤလုပ်ငန်းစဉ်ကို ဆက်လက်လုပ်ဆောင်ပါသည်။
- **မှတ်ဉာဏ်နှင့် အခြေအနေ:** စနစ်သည် အဆင့်များအကြား အခြေအနေနှင့် မှတ်ဉာဏ်ကို ထိန်းသိမ်းထားသောကြောင့်၊ ၎င်းသည် ယခင်ကြိုးပမ်းမှုများနှင့် ၎င်းတို့၏ ရလဒ်များကို အမှတ်ရနိုင်ပြီး၊ ထပ်ခါထပ်ခါ လှည့်ပတ်မှုများကို ရှောင်ရှားကာ ဆက်လက်လုပ်ဆောင်သည့်အခါ ပိုမို အသိအမြင်ရှိသော ဆုံးဖြတ်ချက်များ ချနိုင်ပါသည်။

အချိန်ကြာလာသည်နှင့်အမျှ၊ ဤသည်က တိုးတက်လာသော နားလည်မှု၏ အသိအမြင်ကို ဖန်တီးပေးပြီး၊ မော်ဒယ်သည် လူတစ်ဦးက အမြဲတမ်း ဝင်ရောက်စွက်ဖက်ရန် သို့မဟုတ် ညွှန်ပြချက်ကို ပြန်လည်ပုံသွင်းရန် မလိုအပ်ဘဲ ရှုပ်ထွေးသော၊ များစွာအဆင့်ရှိသော လုပ်ငန်းများကို လမ်းညွှန်နိုင်စေပါသည်။

## ပျက်ကွက်မှု မော်ဒများနှင့် မိမိကိုယ်ကို ပြင်ဆင်ခြင်းကို ကိုင်တွယ်ခြင်း

အေးဂျင်တစ် RAG ၏ လွတ်လပ်မှုတွင် ခိုင်မာသော မိမိကိုယ်ကို ပြင်ဆင်ခြင်း ယန္တရားများလည်း ပါဝင်ပါသည်။ စနစ်သည် မဆီမဆိုင်သော စာရွက်စာတမ်းများ ရယူမိခြင်း သို့မဟုတ် ပုံစံမမှန်သော မေးခွန်းများ ကြုံတွေ့ခြင်းကဲ့သို့သော အဆုံးသတ်များနှင့် တိုက်ရိုက်မျက်နှာချင်းဆိုင်သောအခါ၊ ၎င်းသည်-

- **ပြန်လည်လုပ်ဆောင်ခြင်းနှင့် ပုနစ်မေးခွန်းထုတ်ခြင်း:** တန်ဖိုးနည်းသော တုံ့ပြန်မှုများကို ပြန်ပေးမည့်အစား၊ မော်ဒယ်သည် ရှာဖွေရေး မဟာဗျူဟာအသစ်များကို ကြိုးပမ်း၊ ဒေတာဘေ့စ် မေးခွန်းများကို ပြန်လည်ရေးသား သို့မဟုတ် အခြားရွေးချယ်စရာ အချက်အလက်အစုများကို ကြည့်ရှုပါသည်။
- **ရောဂါရှာဖွေရေး ကိရိယာများကို အသုံးပြုခြင်း:** စနစ်သည် ၎င်း၏ဆင်ခြင်တုံတရား အဆင့်များကို debug လုပ်ရန် သို့မဟုတ် ရယူထားသော အချက်အလက်၏ တိကျမှန်ကန်မှုကို အတည်ပြုရန် ဒီဇိုင်းထုတ်ထားသော ထပ်မံလုပ်ဆောင်ချက်များကို အသုံးပြုနိုင်ပါသည်။ Azure AI Tracing ကဲ့သို့သော ကိရိယာများသည် ခိုင်မာသော observability နှင့် monitoring ကို ဖွင့်လှစ်ရန် အရေးကြီးမည်ဖြစ်သည်။
- **လူ့ကြီးကြပ်မှုပေါ် နောက်ကျခြင်း:** အဆင့်မြင့်ရင်းစားမှု သို့မဟုတ် ထပ်ခါထပ်ခါ ပျက်ကွက်သော အခြေအနေများအတွက်၊ မော်ဒယ်သည် မသေချာမှုကို အလံပြ၍ လူ့လမ်းညွှန်မှုကို တောင်းဆိုနိုင်ပါသည်။ လူသည် ပြင်ဆင်ရေး တုံ့ပြန်ချက်ကို ပေးအပ်ပြီးနောက်၊ မော်ဒယ်သည် ဤသင်ခန်းစာကို ရှေ့သို့ ထည့်သွင်းနိုင်ပါသည်။

ဤအကြိမ်ကြိမ်နှင့် ပြောင်းလဲနိုင်သော ချဉ်းကပ်မှုသည် မော်ဒယ်ကို စဉ်ဆက်မပြတ် တိုးတက်အောင် ခွင့်ပြုပြီး၊ ၎င်းသည် တစ်ကြိမ်တည်း စနစ်တစ်ခုသာ မဟုတ်ဘဲ သတ်မှတ်ထားသော session တစ်ခုအတွင်း ၎င်း၏မှားယွင်းမှုများမှ သင်ယူသည့် စနစ်တစ်ခုဖြစ်ကြောင်း သေချာစေပါသည်။

![မိမိကိုယ်ကို ပြင်ဆင်ခြင်း ယန္တရား](./images/self-correction.png)

## အေးဂျင်စီ၏ နယ်နိမိတ်များ

လုပ်ငန်းတစ်ခုအတွင်း ၎င်း၏လွတ်လပ်မှုရှိသော်လည်း၊ အေးဂျင်တစ် RAG သည် အင်္ဂါရေး ယေဘူယ အသိဉာဏ်နှင့် တူညီမှုမရှိပါ။ ၎င်း၏ "အေးဂျင်တစ်" စွမ်းရည်များသည် လူ့ဖွံ့ဖြိုးရေးသမားများမှ ပေးအပ်ထားသော ကိရိယာများ၊ အချက်အလက်ရင်းမြစ်များနှင့် မူဝါဒများအတွင်း ကန့်သတ်ထားပါသည်။ ၎င်းသည် ၎င်း၏ကိုယ်ပိုင် ကိရိယာများကို တီထွင်နိုင်ခြင်း သို့မဟုတ် သတ်မှတ်ထားသော ဒိုမိန်း နယ်နိမိတ်များပြင်ပသို့ ထွက်နိုင်ခြင်း မရှိပါ။ ၎င်း၏အစား၊ ၎င်းသည် လက်ရှိရရှိနိုင်သော အရင်းအမြစ်များကို ပြောင်းလဲနိုင်သော စွမ်းရည်ဖြင့် စီမံခန့်ခွဲရာတွင် ထူးခြားပါသည်။
အဆင့်မြင့် AI ပုံစံများနှင့် အဓိက ကွာခြားချက်များမှာ-

1. **ဒိုမိန်းအလိုက် လွတ်လပ်မှု:** အေးဂျင်တစ် RAG စနစ်များသည် ရလဒ်များကို မြှင့်တင်ရန် မေးခွန်းပြန်လည်ရေးသားခြင်း သို့မဟုတ် ကိရိယာရွေးချယ်ခြင်းကဲ့သို့သော နည်းဗျူဟာများကို အသုံးပြု၍ သိရှိထားသော ဒိုမိန်းတစ်ခုအတွင်း အသုံးပြုသူ-သတ်မှတ်ထားသော ရည်မှန်းချက်များကို အောင်မြင်ရန် အာရုံစိုက်ထားပါသည်။
2. **အခြေခံအဆောက်အအုံ-မှီခိုခြင်း:** စနစ်၏ စွမ်းရည်များသည် ဖွံ့ဖြိုးရေးသမားများမှ ပေါင်းစပ်ထားသော ကိရိယာများနှင့် အချက်အလက်များပေါ် မူတည်ပါသည်။ လူ့ဝင်ရောက်စွက်ဖက်မှုမရှိဘဲ ဤနယ်နိမိတ်များကို ကျော်လွန်နိုင်ခြင်း မရှိပါ။
3. **ကန့်သတ်ချက်များကို လေးစားခြင်း:** ကျင့်ဝတ်လမ်းညွှန်ချက်များ၊ လိုက်နာမှု စည်းမျဉ်းများနှင့် စီးပွားရေး မူဝါဒများသည် အလွန်အရေးကြီးပါသည်။ အေးဂျင့်၏ လွတ်လပ်မှုသည် ဘေးကင်းရေး အစီအမံများနှင့် ကြီးကြပ်မှု ယန္တရားများမှ အမြဲတမ်း ကန့်သတ်ထားပါသည် (မျှော်လင့်ပါသည်?)

## လက်တွေ့အသုံးချမှုများနှင့် တန်ဖိုး

အေးဂျင်တစ် RAG သည် အကြိမ်ကြိမ် ပြန်လည်ပြင်ဆင်မှုနှင့် တိကျမှန်ကန်မှုကို လိုအပ်သော အခြေအနေများတွင် ထွန်းကားပါသည်-

1. **တိကျမှန်ကန်မှုကို ဦးစားပေးသော ပတ်ဝန်းကျင်များ:** လိုက်နာမှု စစ်ဆေးမှုများ၊ စည်းမျဉ်းဆိုင်ရာ ခွဲခြမ်းစိတ်ဖြာမှု သို့မဟုတ် ဥပဒေရေးရာ သုတေသနတွင်၊ အေးဂျင်တစ် မော်ဒယ်သည် အချက်အလက်များကို ထပ်ခါထပ်ခါ အတည်ပြု၊ ရင်းမြစ်များစွာကို တိုင်ပင်ပြီး၊ အပြီးအစီး စစ်ဆေးထားသော အဖြေကို ထုတ်ပေးသည်အထိ မေးခွန်းများကို ပြန်လည်ရေးသားနိုင်ပါသည်။
2. **ရှုပ်ထွေးသော ဒေတာဘေ့စ် အပြန်အလှန်တုံ့ပြန်မှုများ:** မေးခွန်းများ မကြာခဏ ပျက်ကွက်နိုင် သို့မဟုတ် ပြင်ဆင်မှု လိုအပ်နိုင်သော ဖွဲ့စည်းတည်ဆောက်ထားသော အချက်အလက်များနှင့် ရင်ဆိုင်သောအခါ၊ စနစ်သည် Azure SQL သို့မဟုတ် Microsoft Fabric OneLake ကို အသုံးပြု၍ ၎င်း၏မေးခွန်းများကို အလိုအလျောက် ပြန်လည်ပြင်ဆင်နိုင်ပြီး၊ နောက်ဆုံး ရယူမှုသည် အသုံးပြုသူ၏ ရည်ရွယ်ချက်နှင့် ကိုက်ညီကြောင်း သေချာစေပါသည်။
3. **တိုးချဲ့ထားသော လုပ်ငန်းစဉ်များ:** ရေရှည် session များသည် အချက်အလက်အသစ်များ ထွက်ပေါ်လာသည်နှင့်အမျှ တိုးတက်နိုင်ပါသည်။ အေးဂျင်တစ် RAG သည် ပြဿနာနယ်ပယ်အကြောင်း ပိုမို သင်ယူလာသည်နှင့်အမျှ နည်းဗျူဟာများကို ပြောင်းလဲကာ အချက်အလက်အသစ်များကို စဉ်ဆက်မပြတ် ထည့်သွင်းနိုင်ပါသည်။

## အုပ်ချုပ်မှု၊ ဖေါ်ထုတ်မှုနှင့် ယုံကြည်မှု

ဤစနစ်များသည် ၎င်းတို့၏ဆင်ခြင်တုံတရားတွင် ပိုမို လွတ်လပ်လာသည်နှင့်အမျှ၊ အုပ်ချုပ်မှုနှင့် ဖေါ်ထုတ်မှုတို့သည် အရေးကြီးပါသည်-

- **အကြောင်းပြချက်ရှင်းလင်းနိုင်မှု:** မော်ဒယ်သည် ၎င်းလုပ်ဆောင်ခဲ့သော မေးခွန်းများ၊ ၎င်းတိုင်ပင်ခဲ့သော ရင်းမြစ်များနှင့် ၎င်း၏နိဂုံးချုပ်သို့ ရောက်ရှိရန် လုပ်ဆောင်ခဲ့သော ဆင်ခြင်တုံတရား အဆင့်များ၏ စာရင်းစစ် လမ်းကြောင်းကို ပေးအပ်နိုင်ပါသည်။ Azure AI Content Safety နှင့် Azure AI Tracing / GenAIOps ကဲ့သို့သော ကိရိယာများသည် ဖေါ်ထုတ်မှုကို ထိန်းသိမ်းကာ အန္တရာယ်များကို လျှော့ချရာတွင် ကူညီနိုင်ပါသည်။
- **ဘက်လိုက်မှု ထိန်းချုပ်မှုနှင့် မျှတသော ရယူမှု:** ဖွံ့ဖြိုးရေးသမားများသည် မျှတပြီး ကိုယ်စားပြုမှုရှိသော အချက်အလက်ရင်းမြစ်များကို စဉ်းစားကြောင်း သေချာစေရန် ရယူရေး နည်းဗျူဟာများကို ချိန်ညှိနိုင်ပြီး၊ Azure Machine Learning ကို အသုံးပြုသော အဆင့်မြင့် ဒေတာသိပ္ပံ အဖွဲ့အစည်းများအတွက် စိတ်ကြိုက်မော်ဒယ်များကို အသုံးပြု၍ ဘက်လိုက်မှု သို့မဟုတ် လှဲနေသော ပုံစံများကို ရှာဖွေရန် ရလဒ်များကို ပုံမှန် စစ်ဆေးနိုင်ပါသည်။
- ** အုပ်ချုပ်မှု၊ ပွင့်လင်းမြင်သာမှုနှင့် ယုံကြည်မှု** ဤစနစ်များသည် ၎င်းတို့၏ ဆင်ခြင်တုံတရားတွင် ပိုမိုကိုယ်ပိုင်လွတ်လပ်လာသည်နှင့်အမျှ၊ အုပ်ချုပ်မှုနှင့် ပွင့်လင်းမြင်သာမှုသည် အလွန်အရေးကြီးပါသည်-

- **ရှင်းလင်းစွာရှင်းပြနိုင်သော ဆင်ခြင်တုံတရား:** မော်ဒယ်သည် ၎င်းပြုလုပ်ခဲ့သော မေးခွန်းများ၊ တိုင်ပင်ခဲ့သော အရင်းအမြစ်များနှင့် ၎င်း၏ နိဂုံးချုပ်သို့ရောက်ရှိရန် လုပ်ဆောင်ခဲ့သော ဆင်ခြင်တုံတရားအဆင့်များ၏ စောင့်ကြည့်စစ်ဆေးမှုလမ်းကြောင်းကို ပံ့ပိုးပေးနိုင်သည်။ Azure AI Content Safety နှင့် Azure AI Tracing / GenAIOps ကဲ့သို့သော ကိရိယာများသည် ပွင့်လင်းမြင်သာမှုကို ထိန်းသိမ်းရန်နှင့် အန်တရာယ်များကို လျှော့ချရန် ကူညီနိုင်သည်။

- **ဘက်လိုက်မှုထိန်းချုပ်မှုနှင့် ဟန်ချက်ညီသော ပြန်လည်ရယူမှု:** ရေးဆွဲသူများသည် ဟန်ချက်ညီပြီး ကိုယ်စားပြုမှုရှိသော အချက်အလက်အရင်းအမြစ်များကို ထည့်သွင်းစဉ်းစားရန် ပြန်လည်ရယူမှုနည်းဗျူဟာများကို ချိန်ညှိနိုင်ပြီး Azure Machine Learning ကိုအသုံးပြုသော အဆင့်မြင့်အချက်အလက်သိပ္ပံအဖွဲ့အစည်းများအတွက် စိတ်ကြိုက်မော်ဒယ်များအသုံးပြု၍ ဘက်လိုက်မှု သို့မဟုတ် ဘက်လိုက်သောပုံစံများကို ရှာဖွေတွေ့ရှိရန် ရလဒ်များကို ပုံမှန်စောင့်ကြည့်စစ်ဆေးနိုင်သည်။

- **လူသား၏ကြီးကြပ်မှုနှင့် လိုက်နာမှု:** အရေးကြီးသောအလုပ်များအတွက်၊ လူသား၏ပြန်လည်သုံးသပ်မှုသည် မရှိမဖြစ်လိုအပ်သေးသည်။ Agentic RAG သည် အရေးကြီးသောဆုံးဖြတ်ချက်များတွင် လူသား၏တရားစီရင်မှုကို အစားထိုးခြင်းမဟုတ်ဘဲ၊ ပိုမိုစေ့စေ့စပ်စပ် စစ်ဆေးထားသော ရွေးချယ်စရာများကို ပေးပို့ခြင်းဖြင့် ၎င်းကို တိုးတက်စေပါသည်။

လုပ်ဆောင်ချက်များ၏ ရှင်းလင်းသောမှတ်တမ်းကို ပံ့ပိုးပေးသော ကိရိယာများရှိခြင်းသည် မရှိမဖြစ်လိုအပ်ပါသည်။ ၎င်းတို့မရှိပါက၊ များစွာသောအဆင့်ပါသော လုပ်ငန်းစဉ်ကို ပြန်လည်ပြင်ဆင်ခြင်းသည် အလွန်ခက်ခဲပါသည်။ Agent run အတွက် Literal AI (Chainlit ကုမ္ပဏီ၏နောက်မှ) မှ အောက်ပါဥပမာကို ကြည့်ပါ-

![AgentRunExample](./images/AgentRunExample.png)

![AgentRunExample2](./images/AgentRunExample2.png)

## နိဂုံးချုပ်

Agentic RAG သည် AI စနစ်များသည် ရှုပ်ထွေးပြီး အချက်အလက်များစွာလိုအပ်သော အလုပ်များကို ကိုင်တွယ်ပုံတွင် သဘာဝကျသော ဆင့်ကဲဖြစ်တိုးတက်မှုကို ကိုယ်စားပြုပါသည်။ လေ့လာဆက်သွယ်မှုပုံစံကို လက်ခံခြင်း၊ ကိရိယာများကို လွတ်လပ်စွာရွေးချယ်ခြင်းနှင့် အရည်အသွေးမြင့်ရလဒ်ရရှိသည်အထိ မေးခွန်းများကို ပြန်လည်ပြင်ဆင်ခြင်းအားဖြင့်၊ စနစ်သည် တည်ငြိမ်သော အမိန့်လိုက်နာခြင်းမှ ပိုမိုလိုက်လျောညီထွေ၊ အကြောင်းအရာအသိရှိသော ဆုံးဖြတ်ချက်ချသူဖြစ်လာသည်။ လူသားမှ သတ်မှတ်ထားသော အခြေခံအဆောက်အအုံများနှင့် ကျင့်ဝတ်လမ်းညွှန်ချက်များဖြင့် ကန့်သတ်ထားသေးသော်လည်း၊ ဤ agentic စွမ်းရည်များသည် စီးပွားရေးအဖွဲ့အစည်းများနှင့် အဆုံးအသုံးပြုသူများအတွက် ပိုမိုကြွယ်ဝ၊ ပိုမိုတက်ကြွပြီး နောက်ဆုံးတွင် ပိုမိုအသုံးဝင်သော AI အပြန်အလှန်အသုံးပြုမှုများကို ဖြစ်ပေါ်စေပါသည်။

## နောက်ထပ်အရင်းအမြစ်များ

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Azure OpenAI Service ဖြင့် Retrieval Augmented Generation (RAG) ကို အကောင်အထည်ဖော်ပါ- Azure OpenAI Service ဖြင့် သင့်ကိုယ်ပိုင်အချက်အလက်များကို အသုံးပြုနည်းကို လေ့လာပါ။ ဤ Microsoft Learn မော်ဂျူးသည် RAG အကောင်အထည်ဖော်ခြင်းအတွက် ကျယ်ကျယ်ပြန့်ပြန့် လမ်းညွှန်ချက်ကို ပံ့ပိုးပေးပါသည်</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Azure AI Foundry ဖြင့် generative AI applications များ၏ အကဲဖြတ်မှု- ဤဆောင်းပါးသည် Agentic AI applications နှင့် RAG architectures အပါအဝင် အများပြည်သူရရှိနိုင်သော datasets များတွင် မော်ဒယ်များ၏ အကဲဖြတ်မှုနှင့် နှိုင်းယှဉ်မှုကို လွှမ်းခြုံထားပါသည်</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Agentic RAG ဆိုတာဘာလဲ | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG- Agent-Based Retrieval Augmented Generation အတွက် ပြီးပြည့်စုံသော လမ်းညွှန် – generation RAG မှ သတင်းများ</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG- query reformulation နှင့် self-query ဖြင့် သင့် RAG ကို အရှိန်မြှင့်ပါ! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">RAG တွင် Agentic Layers များ ထည့်သွင်းခြင်း</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Knowledge Assistants များ၏ အနာဂတ်- Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Agentic RAG Systems များကို ဘယ်လို တည်ဆောက်မလဲ</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">သင့် AI agents များကို စကေးချဲ့ရန် Azure AI Foundry Agent Service ကို အသုံးပြုခြင်း</a>

### ပညာရေးစာတမ်းများ

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine- Self-Feedback ဖြင့် Iterative Refinement</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion- Verbal Reinforcement Learning ဖြင့် Language Agents များ</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC- Tool-Interactive Critiquing ဖြင့် Large Language Models များသည် Self-Correct လုပ်နိုင်သည်</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation- Agentic RAG အတွက် စစ်တမ်းလေ့လာမှု</a>

## ယခင်သင်ခန်းစာ

[Tool Use Design Pattern](../04-tool-use/README.md)

## နောက်သင်ခန်းစာ

[ယုံကြည်ရသော AI Agents များ တည်ဆောက်ခြင်း](../06-building-trustworthy-agents/README.md)

  
[![Agentic RAG](./images/lesson-5-thumbnail.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Click the image above to view video of this lesson)_

# Agentic RAG

This lesson provides a comprehensive overview of Agentic Retrieval-Augmented Generation (Agentic RAG), an emerging AI paradigm where large language models (LLMs) autonomously plan their next steps while pulling information from external sources. Unlike static retrieval-then-read patterns, Agentic RAG involves iterative calls to the LLM, interspersed with tool or function calls and structured outputs. The system evaluates results, refines queries, invokes additional tools if needed, and continues this cycle until a satisfactory solution is achieved.

## Introduction

This lesson will cover

- **Understand Agentic RAG:**  Learn about the emerging paradigm in AI where large language models (LLMs) autonomously plan their next steps while pulling information from external data sources.
- **Grasp Iterative Maker-Checker Style:** Comprehend the loop of iterative calls to the LLM, interspersed with tool or function calls and structured outputs, designed to improve correctness and handle malformed queries.
- **Explore Practical Applications:** Identify scenarios where Agentic RAG shines, such as correctness-first environments, complex database interactions, and extended workflows.

## Learning Goals

After completing this lesson, you will know how to/understand:

- **Understanding Agentic RAG:** Learn about the emerging paradigm in AI where large language models (LLMs) autonomously plan their next steps while pulling information from external data sources.
- **Iterative Maker-Checker Style:** Grasp the concept of a loop of iterative calls to the LLM, interspersed with tool or function calls and structured outputs, designed to improve correctness and handle malformed queries.
- **Owning the Reasoning Process:** Comprehend the system's ability to own its reasoning process, making decisions on how to approach problems without relying on pre-defined paths.
- **Workflow:** Understand how an agentic model independently decides to retrieve market trend reports, identify competitor data, correlate internal sales metrics, synthesize findings, and evaluate the strategy.
- **Iterative Loops, Tool Integration, and Memory:** Learn about the system's reliance on a looped interaction pattern, maintaining state and memory across steps to avoid repetitive loops and make informed decisions.
- **Handling Failure Modes and Self-Correction:** Explore the system's robust self-correction mechanisms, including iterating and re-querying, using diagnostic tools, and falling back on human oversight.
- **Boundaries of Agency:** Understand the limitations of Agentic RAG, focusing on domain-specific autonomy, infrastructure dependence, and respect for guardrails.
- **Practical Use Cases and Value:** Identify scenarios where Agentic RAG shines, such as correctness-first environments, complex database interactions, and extended workflows.
- **Governance, Transparency, and Trust:** Learn about the importance of governance and transparency, including explainable reasoning, bias control, and human oversight.

## What is Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) is an emerging AI paradigm where large language models (LLMs) autonomously plan their next steps while pulling information from external sources. Unlike static retrieval-then-read patterns, Agentic RAG involves iterative calls to the LLM, interspersed with tool or function calls and structured outputs. The system evaluates results, refines queries, invokes additional tools if needed, and continues this cycle until a satisfactory solution is achieved. This iterative “maker-checker” style improves correctness, handles malformed queries, and ensures high-quality results.

The system actively owns its reasoning process, rewriting failed queries, choosing different retrieval methods, and integrating multiple tools—such as vector search in Azure AI Search, SQL databases, or custom APIs—before finalizing its answer. The distinguishing quality of an agentic system is its ability to own its reasoning process. Traditional RAG implementations rely on pre-defined paths, but an agentic system autonomously determines the sequence of steps based on the quality of the information it finds.

## Defining Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) is an emerging paradigm in AI development where LLMs not only pull information from external data sources but also autonomously plan their next steps. Unlike static retrieval-then-read patterns or carefully scripted prompt sequences, Agentic RAG involves a loop of iterative calls to the LLM, interspersed with tool or function calls and structured outputs. At every turn, the system evaluates the results it has obtained, decides whether to refine its queries, invokes additional tools if needed, and continues this cycle until it achieves a satisfactory solution.

This iterative “maker-checker” style of operation is designed to improve correctness, handle malformed queries to structured databases (e.g. NL2SQL), and ensure balanced, high-quality results. Rather than relying solely on carefully engineered prompt chains, the system actively owns its reasoning process. It can rewrite queries that fail, choose different retrieval methods, and integrate multiple tools—such as vector search in Azure AI Search, SQL databases, or custom APIs—before finalizing its answer. This removes the need for overly complex orchestration frameworks. Instead, a relatively simple loop of “LLM call → tool use → LLM call → …” can yield sophisticated and well-grounded outputs.

![Agentic RAG Core Loop](./images/agentic-rag-core-loop.png)

## Owning the Reasoning Process

The distinguishing quality that makes a system “agentic” is its ability to own its reasoning process. Traditional RAG implementations often depend on humans pre-defining a path for the model: a chain-of-thought that outlines what to retrieve and when.
But when a system is truly agentic, it internally decides how to approach the problem. It’s not just executing a script; it’s autonomously determining the sequence of steps based on the quality of the information it finds.
For example, if it’s asked to create a product launch strategy, it doesn’t rely solely on a prompt that spells out the entire research and decision-making workflow. Instead, the agentic model independently decides to:

1. Retrieve current market trend reports using Bing Web Grounding
2. Identify relevant competitor data using Azure AI Search.
3.	Correlate historical internal sales metrics using Azure SQL Database.
4. Synthesize the findings into a cohesive strategy orchestrated via Azure OpenAI Service.
5.	Evaluate the strategy for gaps or inconsistencies, prompting another round of retrieval if necessary.
All of these steps—refining queries, choosing sources, iterating until “happy” with the answer—are decided by the model, not pre-scripted by a human.

## Iterative Loops, Tool Integration, and Memory

![Tool Integration Architecture](./images/tool-integration.png)

An agentic system relies on a looped interaction pattern:

- **Initial Call:** The user’s goal (aka. user prompt) is presented to the LLM.
- **Tool Invocation:** If the model identifies missing information or ambiguous instructions, it selects a tool or retrieval method—like a vector database query (e.g. Azure AI Search Hybrid search over private data) or a structured SQL call—to gather more context.
- **Assessment & Refinement:** After reviewing the returned data, the model decides whether the information suffices. If not, it refines the query, tries a different tool, or adjusts its approach.
- **Repeat Until Satisfied:** This cycle continues until the model determines that it has enough clarity and evidence to deliver a final, well-reasoned response.
- **Memory & State:** Because the system maintains state and memory across steps, it can recall previous attempts and their outcomes, avoiding repetitive loops and making more informed decisions as it proceeds.

Over time, this creates a sense of evolving understanding, enabling the model to navigate complex, multi-step tasks without requiring a human to constantly intervene or reshape the prompt.

## Handling Failure Modes and Self-Correction

Agentic RAG’s autonomy also involves robust self-correction mechanisms. When the system hits dead ends—such as retrieving irrelevant documents or encountering malformed queries—it can:

- **Iterate and Re-Query:** Instead of returning low-value responses, the model attempts new search strategies, rewrites database queries, or looks at alternative data sets.
- **Use Diagnostic Tools:** The system may invoke additional functions designed to help it debug its reasoning steps or confirm the correctness of retrieved data. Tools like Azure AI Tracing will be important to enable robust observability and monitoring.
- **Fallback on Human Oversight:** For high-stakes or repeatedly failing scenarios, the model might flag uncertainty and request human guidance. Once the human provides corrective feedback, the model can incorporate that lesson going forward.

This iterative and dynamic approach allows the model to improve continuously, ensuring that it’s not just a one-shot system but one that learns from its missteps during a given session.

![Self Correction Mechanism](./images/self-correction.png)

## Boundaries of Agency

Despite its autonomy within a task, Agentic RAG is not analogous to Artificial General Intelligence. Its “agentic” capabilities are confined to the tools, data sources, and policies provided by human developers. It can’t invent its own tools or step outside the domain boundaries that have been set. Rather, it excels at dynamically orchestrating the resources at hand.
Key differences from more advanced AI forms include:

1. **Domain-Specific Autonomy:** Agentic RAG systems are focused on achieving user-defined goals within a known domain, employing strategies like query rewriting or tool selection to improve outcomes.
2. **Infrastructure-Dependent:** The system’s capabilities hinge on the tools and data integrated by developers. It can’t surpass these boundaries without human intervention.
3. **Respect for Guardrails:** Ethical guidelines, compliance rules, and business policies remain very important. The agent’s freedom is always constrained by safety measures and oversight mechanisms (hopefully?)

## Practical Use Cases and Value

Agentic RAG shines in scenarios requiring iterative refinement and precision:

1. **Correctness-First Environments:** In compliance checks, regulatory analysis, or legal research, the agentic model can repeatedly verify facts, consult multiple sources, and rewrite queries until it produces a thoroughly vetted answer.
2. **Complex Database Interactions:** When dealing with structured data where queries might often fail or need adjustment, the system can autonomously refine its queries using Azure SQL or Microsoft Fabric OneLake, ensuring the final retrieval aligns with the user’s intent.
3. **Extended Workflows:** Longer-running sessions might evolve as new information surfaces. Agentic RAG can continuously incorporate new data, shifting strategies as it learns more about the problem space.

## Governance, Transparency, and Trust

As these systems become more autonomous in their reasoning, governance and transparency are crucial:

- **Explainable Reasoning:** The model can provide an audit trail of the queries it made, the sources it consulted, and the reasoning steps it took to reach its conclusion. Tools like Azure AI Content Safety and Azure AI Tracing / GenAIOps can help maintain transparency and mitigate risks.
- **Bias Control and Balanced Retrieval:** Developers can tune retrieval strategies to ensure balanced, representative data sources are considered, and regularly audit outputs to detect bias or skewed patterns using custom models for advanced data science organizations using Azure Machine Learning.
- **Human Oversight and Compliance:** For sensitive tasks, human review remains essential. Agentic RAG doesn’t replace human judgment in high-stakes decisions—it augments it by delivering more thoroughly vetted options.

Having tools that provide a clear record of actions is essential. Without them, debugging a multi-step process can be very difficult. See the following example from Literal AI (company behind Chainlit) for an Agent run:

![AgentRunExample](./images/AgentRunExample.png)

![AgentRunExample2](./images/AgentRunExample2.png)

## Conclusion

Agentic RAG represents a natural evolution in how AI systems handle complex, data-intensive tasks. By adopting a looped interaction pattern, autonomously selecting tools, and refining queries until achieving a high-quality result, the system moves beyond static prompt-following into a more adaptive, context-aware decision-maker. While still bounded by human-defined infrastructures and ethical guidelines, these agentic capabilities enable richer, more dynamic, and ultimately more useful AI interactions for both enterprises and end-users.

## Additional Resources

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implement Retrieval Augmented Generation (RAG) with Azure OpenAI Service: Learn how to use your own data with the Azure OpenAI Service. This Microsoft Learn module provides a comprehensive guide on implementing RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluation of generative AI applications with Azure AI Foundry: This article covers the evaluation and comparison of models on publicly available datasets, including Agentic AI applications and RAG architectures</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">What is Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: A Complete Guide to Agent-Based Retrieval Augmented Generation – News from generation RAG</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: turbocharge your RAG with query reformulation and self-query! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Adding Agentic Layers to RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">The Future of Knowledge Assistants: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">How to Build Agentic RAG Systems</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Using Azure AI Foundry Agent Service to scale your AI agents</a>

### Academic Papers

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterative Refinement with Self-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG</a>

## Previous Lesson

[Tool Use Design Pattern](../04-tool-use/README.md)

## Next Lesson

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)
