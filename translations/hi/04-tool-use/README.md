[![कैसे डिज़ाइन करें अच्छे AI एजेंट](../../../translated_images/hi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(इस पाठ का वीडियो देखने के लिए ऊपर चित्र पर क्लिक करें)_

# टूल उपयोग डिजाइन पैटर्न

टूल्स दिलचस्प होते हैं क्योंकि वे AI एजेंटों को अधिक व्यापक क्षमताएँ प्रदान करते हैं। एजेंट के पास जो सीमित क्रियाओं का सेट होता है, उसके बजाय, एक टूल जोड़ने से एजेंट अब कई प्रकार की क्रियाएँ कर सकता है। इस अध्याय में, हम टूल उपयोग डिजाइन पैटर्न को देखेंगे, जो बताता है कि AI एजेंट कैसे विशिष्ट टूल्स का उपयोग करके अपने लक्ष्य प्राप्त कर सकते हैं।

## परिचय

इस पाठ में, हम निम्नलिखित प्रश्नों के उत्तर खोजेंगे:

- टूल उपयोग डिजाइन पैटर्न क्या है?
- किन उपयोग मामलों में इसे लागू किया जा सकता है?
- डिजाइन पैटर्न को लागू करने के लिए किन तत्वों/निर्माण ब्लॉकों की आवश्यकता होती है?
- भरोसेमंद AI एजेंट बनाने के लिए टूल उपयोग डिजाइन पैटर्न का उपयोग करते समय क्या विशेष विचार करने होंगे?

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप सक्षम होंगे:

- टूल उपयोग डिजाइन पैटर्न और इसका उद्देश्य परिभाषित करना।
- उन उपयोग मामलों की पहचान करना जहां टूल उपयोग डिजाइन पैटर्न लागू हो सकता है।
- डिजाइन पैटर्न को लागू करने के लिए आवश्यक प्रमुख तत्वों को समझना।
- इस डिजाइन पैटर्न का उपयोग करने वाले AI एजेंटों में विश्वसनीयता सुनिश्चित करने के विचारों को जानना।

## टूल उपयोग डिजाइन पैटर्न क्या है?

**टूल उपयोग डिजाइन पैटर्न** LLMs को बाहरी टूल्स के साथ इंटरैक्ट करने की क्षमता प्रदान करने पर केंद्रित है ताकि विशिष्ट लक्ष्यों को प्राप्त किया जा सके। टूल्स ऐसे कोड होते हैं जिन्हें एजेंट द्वारा क्रियान्वित करके क्रियाएं की जाती हैं। एक टूल एक सरल फ़ंक्शन हो सकता है जैसे कैलकुलेटर, या तृतीय-पक्ष सेवा के लिए API कॉल हो सकता है जैसे स्टॉक प्राइस लुकअप या मौसम पूर्वानुमान। AI एजेंटों के संदर्भ में, टूल्स को मॉडल-जनित फ़ंक्शन कॉल्स के जवाब में एजेंटों द्वारा निष्पादित करने के लिए डिज़ाइन किया गया है।

## किन उपयोग मामलों में इसे लागू किया जा सकता है?

AI एजेंट टूल्स का उपयोग जटिल कार्य पूरे करने, जानकारी पुनःप्राप्त करने या निर्णय लेने के लिए कर सकते हैं। टूल उपयोग डिजाइन पैटर्न अक्सर ऐसे परिदृश्यों में उपयोग किया जाता है जहाँ गतिशील रूप से बाहरी सिस्टम जैसे डेटाबेस, वेब सेवाएं, या कोड इंटरप्रेटर्स के साथ इंटरैक्शन आवश्यक होता है। यह क्षमता कई विभिन्न उपयोग मामलों के लिए उपयोगी है, जिनमें शामिल हैं:

- **गतिशील सूचना पुनःप्राप्ति:** एजेंट बाहरी API या डेटाबेस से नवीनतम डेटा प्राप्त कर सकते हैं (जैसे, डेटा विश्लेषण के लिए SQLite डेटाबेस से क्वेरी करना, स्टॉक मूल्यों या मौसम की जानकारी लेना)।
- **कोड निष्पादन और व्याख्या:** एजेंट गणितीय समस्याओं को हल करने, रिपोर्ट बनाने, या सिमुलेशन करने के लिए कोड या स्क्रिप्ट्स चला सकते हैं।
- **कार्यप्रवाह स्वचालन:** टास्क शेड्यूलर्स, ईमेल सेवाओं, या डेटा पाइपलाइनों जैसे टूल्स को इंटीग्रेट करके दोहराए जाने वाले या बहु-चरण कार्यप्रवाह स्वचालित करना।
- **ग्राहक सहायता:** एजेंट CRM सिस्टम, टिकटिंग प्लेटफॉर्म, या नॉलेज बेस के साथ इंटरैक्ट करके उपयोगकर्ता प्रश्न हल कर सकते हैं।
- **सामग्री निर्माण और संपादन:** एजेंट ग्रामर चेकर, टेक्स्ट समरी, या सामग्री सुरक्षा मूल्यांकन जैसे टूल्स का उपयोग करके सामग्री निर्माण कार्यों में सहायता कर सकते हैं।

## टूल उपयोग डिजाइन पैटर्न को लागू करने के लिए किन तत्वों/निर्माण ब्लॉकों की आवश्यकता होती है?

ये निर्माण ब्लॉक AI एजेंट को व्यापक कार्यों की श्रृंखला को पूरा करने की अनुमति देते हैं। आइए टूल उपयोग डिजाइन पैटर्न को लागू करने के लिए आवश्यक प्रमुख तत्वों को देखें:

- **फ़ंक्शन/टूल स्कीमा**: उपलब्ध टूल्स की विस्तृत परिभाषाएँ, जिनमें फ़ंक्शन का नाम, उद्देश्य, आवश्यक पैरामीटर, और अपेक्षित आउटपुट शामिल हैं। ये स्कीमा LLM को यह समझने में सक्षम बनाते हैं कि कौन से टूल उपलब्ध हैं और मान्य अनुरोध कैसे बनाएँ।

- **फ़ंक्शन निष्पादन तर्क**: उपयोगकर्ता की मंशा और संवाद संदर्भ के आधार पर कब और कैसे टूल्स को कॉल किया जाता है, इसे नियंत्रित करता है। इसमें योजना बनाने वाले मॉड्यूल, रूटिंग तंत्र, या सशर्त प्रवाह शामिल हो सकते हैं जो टूल उपयोग को गतिशील रूप से निर्धारित करते हैं।

- **संदेश प्रबंधन प्रणाली**: उपयोगकर्ता इनपुट, LLM प्रतिक्रियाओं, टूल कॉल्स, और टूल आउटपुट के बीच वार्तालाप प्रवाह का प्रबंधन करने वाले घटक।

- **टूल इंटीग्रेशन फ्रेमवर्क**: एजेंट को विभिन्न टूल्स से जोड़ने वाला बुनियादी ढांचा, चाहे वे सरल फ़ंक्शन हों या जटिल बाहरी सेवाएं।

- **त्रुटि प्रबंधन और मान्यता**: टूल निष्पादन में विफलता को संभालना, पैरामीटर मान्य करना, और अप्रत्याशित प्रतिक्रिया प्रबंधन के लिए तंत्र।

- **स्थिति प्रबंधन**: बहु-टर्न वार्तालापों में संगति सुनिश्चित करने के लिए संवाद संदर्भ, पिछली टूल इंटरैक्शन, और स्थायी डेटा का ट्रैक रखना।

अब, आइए फ़ंक्शन/टूल कॉलिंग को अधिक विस्तार से देखें।
 
### फ़ंक्शन/टूल कॉलिंग

फ़ंक्शन कॉलिंग वह मुख्य तरीका है जिससे हम बड़े भाषा मॉडलों (LLMs) को टूल्स के साथ इंटरैक्ट करने में सक्षम बनाते हैं। आप अक्सर 'फ़ंक्शन' और 'टूल' को एक दूसरे के समान उपयोग करते हुए देखेंगे क्योंकि 'फ़ंक्शन' (पुन: उपयोग योग्य कोड ब्लॉक्स) वे 'टूल्स' हैं जिनका उपयोग एजेंट कार्य करने के लिए करते हैं। एक फ़ंक्शन के कोड को निष्पादित करने के लिए, LLM को उपयोगकर्ता के अनुरोध को फ़ंक्शन के विवरण से तुलना करनी होती है। इसके लिए उपलब्ध सभी फ़ंक्शन्स का विवरण रखने वाला एक स्कीमा LLM को भेजा जाता है। फिर LLM उस कार्य के लिए सबसे उपयुक्त फ़ंक्शन चुनता है और उसका नाम तथा तर्क वापस करता है। चुना गया फ़ंक्शन चलाया जाता है, उसकी प्रतिक्रिया LLM को भेजी जाती है, जो उपयोगकर्ता के अनुरोध का उत्तर तैयार करता है।

डेवलपर्स को एजेंट के लिए फ़ंक्शन कॉलिंग लागू करने के लिए आवश्यक होगा:

1. ऐसा LLM मॉडल जो फ़ंक्शन कॉलिंग का समर्थन करता हो
2. फ़ंक्शन विवरणों वाला स्कीमा
3. प्रत्येक वर्णित फ़ंक्शन के लिए कोड

चलिए वर्तमान समय पाने का उदाहरण लेते हैं:

1. **ऐसा LLM इनिशियलाइज़ करें जो फ़ंक्शन कॉलिंग का समर्थन करता हो:**

    सभी मॉडल फ़ंक्शन कॉलिंग का समर्थन नहीं करते, इसलिए यह जांचना महत्वपूर्ण है कि आप जो LLM उपयोग कर रहे हैं वह करता है या नहीं। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> फ़ंक्शन कॉलिंग का समर्थन करता है। हम Azure OpenAI **Responses API** के खिलाफ OpenAI क्लाइंट को शुरू करके शुरुआत कर सकते हैं (स्थिर `/openai/v1/` एंडपॉइंट — `api_version` की जरूरत नहीं)।

    ```python
    # Azure OpenAI (Responses API, v1 endpoint) के लिए OpenAI क्लाइंट को प्रारंभ करें
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **फ़ंक्शन स्कीमा बनाएँ**:

    इसके बाद हम एक JSON स्कीमा परिभाषित करेंगे जिसमें फ़ंक्शन का नाम, उस फ़ंक्शन का वर्णन कि वह क्या करता है, और फ़ंक्शन के पैरामीटरों के नाम और वर्णन होंगे।
    फिर हम इस स्कीमा को पिछले बनाए गए क्लाइंट को उपयोगकर्ता के समय पूछने वाले अनुरोध के साथ भेजेंगे। ध्यान देने वाली बात यह है कि एक **टूल कॉल** वापस किया जाता है, प्रश्न का अंतिम उत्तर **नहीं**। जैसा कि पहले बताया गया था, LLM उस कार्य के लिए चुने गए फ़ंक्शन का नाम और जो तर्क पास किए जाएंगे उनकी जानकारी देता है।

    ```python
    # मॉडल के पढ़ने के लिए फ़ंक्शन विवरण (Responses API फ्लैट टूल प्रारूप)
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
  
    # प्रारंभिक उपयोगकर्ता संदेश
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # पहला API कॉल: मॉडल से अनुरोध करें कि वह फ़ंक्शन का उपयोग करे
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # रिस्पांस API प्रतिक्रिया.output में टूल कॉल को function_call आइटम के रूप में लौटाती है।
    # उन्हें वार्तालाप में जोड़ें ताकि मॉडल के पास अगले चरण में पूर्ण संदर्भ हो।
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **कार्य पूरा करने के लिए आवश्यक फ़ंक्शन कोड:**

    अब जब LLM ने यह चुना है कि कौन सा फ़ंक्शन चलाना है, तो उस कार्य को पूरा करने वाला कोड लागू करना और निष्पादित करना होगा।
    हम Python में वर्तमान समय प्राप्त करने के लिए कोड लागू कर सकते हैं। हमें response_message से नाम और तर्क निकालने के लिए भी कोड लिखना होगा ताकि अंतिम परिणाम मिल सके।

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
    # फंक्शन कॉल्स को हैंडल करें
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # टूल परिणाम को function_call_output आइटम के रूप में लौटाएं
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # दूसरा API कॉल: मॉडल से अंतिम प्रतिक्रिया प्राप्त करें
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

फ़ंक्शन कॉलिंग अधिकांश, यदि सभी नहीं, एजेंट टूल उपयोग डिज़ाइन का केंद्र होता है, हालांकि इसे शुरुआत से लागू करना कभी-कभी चुनौतीपूर्ण हो सकता है।
जैसा कि हमने [पाठ 2](../../../02-explore-agentic-frameworks) में सीखा, एजेंटिक फ्रेमवर्क हमें टूल उपयोग को लागू करने के लिए प्री-बिल्ट निर्माण ब्लॉक्स प्रदान करते हैं।
 
## एजेंटिक फ्रेमवर्क के साथ टूल उपयोग के उदाहरण

यहाँ कुछ उदाहरण हैं कि आप टूल उपयोग डिजाइन पैटर्न को विभिन्न एजेंटिक फ्रेमवर्क के साथ कैसे लागू कर सकते हैं:

### माइक्रोसॉफ्ट एजेंट फ्रेमवर्क

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">माइक्रोसॉफ्ट एजेंट फ्रेमवर्क</a> AI एजेंट बनाने के लिए एक ओपन-सोर्स AI फ्रेमवर्क है। यह फ़ंक्शन कॉलिंग की प्रक्रिया को सरल बनाता है, जिससे आप टूल्स को Python फ़ंक्शन्स के रूप में `@tool` डेकोरेटर के साथ परिभाषित कर सकते हैं। फ्रेमवर्क मॉडल और आपके कोड के बीच संवाद को संभालता है। यह पहले से बनाए गए टूल्स जैसे File Search और Code Interpreter तक पहुंच भी प्रदान करता है `FoundryChatClient` के माध्यम से।

निम्न आरेख माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के साथ फ़ंक्शन कॉलिंग की प्रक्रिया को दर्शाता है:

![function calling](../../../translated_images/hi/functioncalling-diagram.a84006fc287f6014.webp)

माइक्रोसॉफ्ट एजेंट फ्रेमवर्क में, टूल्स को डेकोरेटेड फ़ंक्शन्स के रूप में परिभाषित किया जाता है। हम पहले देखी गई `get_current_time` फ़ंक्शन को `@tool` डेकोरेटर का उपयोग करके एक टूल में बदल सकते हैं। फ्रेमवर्क स्वचालित रूप से फ़ंक्शन और इसके पैरामीटरों को सीरियलाइज़ करेगा, और LLM को भेजने के लिए स्कीमा बनाएगा।

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# क्लाइंट बनाएं
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# एक एजेंट बनाएं और टूल के साथ चलाएं
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### माइक्रोसॉफ्ट फाउंड्री एजेंट सेवा

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">माइक्रोसॉफ्ट फाउंड्री एजेंट सेवा</a> एक नया एजेंटिक फ्रेमवर्क है जिसे डेवलपर्स को सुरक्षित रूप से उच्च गुणवत्ता, विस्तार योग्य AI एजेंट बनाने, तैनात करने और स्केल करने में सक्षम बनाने के लिए डिज़ाइन किया गया है बिना नीचे के कंप्यूटिंग और स्टोरेज संसाधनों का प्रबंधन किए। यह विशेष रूप से एंटरप्राइज़ अनुप्रयोगों के लिए उपयोगी है क्योंकि यह एक पूरी तरह से प्रबंधित सेवा है जिसमें एंटरप्राइज़ ग्रेड सुरक्षा है।

LLM API के सीधे विकास की तुलना में, माइक्रोसॉफ्ट फाउंड्री एजेंट सेवा कुछ लाभ प्रदान करता है, जिनमें शामिल हैं:

- स्वचालित टूल कॉलिंग – टूल कॉल पार्स करने, टूल को इनवोक करने और प्रतिक्रिया को संभालने की आवश्यकता नहीं; यह सब अब सर्वर-साइड होता है
- सुरक्षित रूप से प्रबंधित डेटा – अपनी स्वयं की वार्तालाप स्थिति प्रबंधित करने के बजाय, आप सभी आवश्यक जानकारी संग्रहीत करने के लिए थ्रेड्स पर निर्भर कर सकते हैं
- बॉक्स के बाहर टूल्स – ऐसे टूल्स जिनका उपयोग आप अपने डेटा स्रोतों के साथ इंटरैक्ट करने के लिए कर सकते हैं, जैसे Bing, Azure AI Search, और Azure Functions।

माइक्रोसॉफ्ट फाउंड्री एजेंट सेवा में उपलब्ध टूल्स को दो श्रेणियों में विभाजित किया जा सकता है:

1. नॉलेज टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search के साथ ग्राउंडिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. एक्शन टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">फ़ंक्शन कॉलिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इंटरप्रेटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित टूल्स</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

एजेंट सेवा हमें इन टूल्स का एक `toolset` के रूप में उपयोग करने की अनुमति देती है। यह `threads` का भी उपयोग करता है जो किसी विशेष वार्तालाप के संदेशों के इतिहास को ट्रैक करते हैं।

कल्पना करें कि आप Contoso नाम की कंपनी में एक बिक्री एजेंट हैं। आप एक वार्तालाप एजेंट विकसित करना चाहते हैं जो आपकी बिक्री डेटा के बारे में प्रश्नों का उत्तर दे सके।

निम्न छवि दर्शाती है कि आप माइक्रोसॉफ्ट फाउंड्री एजेंट सेवा का उपयोग अपनी बिक्री डेटा का विश्लेषण कैसे करने के लिए कर सकते हैं:

![Agentic Service In Action](../../../translated_images/hi/agent-service-in-action.34fb465c9a84659e.webp)

सेवा के साथ इनमे से किसी भी टूल का उपयोग करने के लिए हम एक क्लाइंट बना सकते हैं और एक टूल या टूलसेट परिभाषित कर सकते हैं। इसे व्यवहार में लागू करने के लिए हम निम्न Python कोड का उपयोग कर सकते हैं। LLM टूलसेट को देखकर निर्णय ले सकेगा कि उपयोगकर्ता अनुरोध के आधार पर उपयोगकर्ता द्वारा बनाए गए फ़ंक्शन `fetch_sales_data_using_sqlite_query` का उपयोग करना है या पहले से बना हुआ Code Interpreter।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query फ़ंक्शन जिसे fetch_sales_data_functions.py फ़ाइल में पाया जा सकता है।
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# टूलसेट प्रारंभ करें
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query फ़ंक्शन के साथ फ़ंक्शन कॉलिंग एजेंट प्रारंभ करें और इसे टूलसेट में जोड़ें
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# कोड इंटरप्रेटर टूल प्रारंभ करें और इसे टूलसेट में जोड़ें।
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## भरोसेमंद AI एजेंट बनाने के लिए टूल उपयोग डिजाइन पैटर्न का उपयोग करते समय क्या विशेष विचार हैं?

LLMs द्वारा डायनेमिकली जनरेट किए गए SQL के साथ एक सामान्य चिंता सुरक्षा है, खासकर SQL इंजेक्शन या दुर्भावनापूर्ण कार्य जैसे डेटाबेस को ड्राॅप या छेड़छाड़ करने का खतरा। ये चिंताएँ वाजिब हैं, लेकिन इन्हें डेटाबेस एक्सेस अनुमतियों को सही ढंग से कॉन्फ़िगर करके प्रभावी रूप से कम किया जा सकता है। अधिकांश डेटाबेस के लिए यह डेटाबेस को केवल पढ़ने-के लिए (read-only) कॉन्फ़िगर करना शामिल करता है। PostgreSQL या Azure SQL जैसी डेटाबेस सेवाओं के लिए, ऐप को एक रीड-ओनली (SELECT) भूमिका सौंपनी चाहिए।

ऐप को एक सुरक्षित वातावरण में चलाना सुरक्षा को और बढ़ावा देता है। एंटरप्राइज़ परिदृश्यों में, डेटा को आमतौर पर परिचालन प्रणालियों से निकालकर एक रीड-ओनली डेटाबेस या डेटा वेयरहाउस में परिवर्तित किया जाता है जिसमें उपयोगकर्ता-मित्रवत स्कीमा होता है। यह दृष्टिकोण सुनिश्चित करता है कि डेटा सुरक्षित है, प्रदर्शन और पहुंच के लिए सुधारित है, और ऐप के पास सीमित, केवल पढ़ने-के लिए पहुंच है।

## नमूना कोड

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## टूल उपयोग डिजाइन पैटर्न के बारे में और प्रश्न हैं?

अन्य शिक्षार्थियों से मिलने, ऑफिस ऑवर्स में भाग लेने, और अपने AI एजेंट्स के प्रश्नों के उत्तर पाने के लिए [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) में शामिल हों।

## अतिरिक्त संसाधन

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents सेवा कार्यशाला</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer मल्टी-एजेंट कार्यशाला</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">माइक्रोसॉफ्ट एजेंट फ्रेमवर्क अवलोकन</a>


## इस एजेंट का स्मोक-टेस्ट करना (वैकल्पिक)

[Lesson 16](../16-deploying-scalable-agents/README.md) में एजेंट्स को डिप्लॉय करना सीखने के बाद, आप इस पाठ के `TravelToolAgent` का स्मोक-टेस्ट कर सकते हैं (क्या यह अभी भी अपने टूल्स को कॉल करता है और जवाब देता है?) [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) के साथ। इसे चलाने के तरीके के लिए देखें [`tests/README.md`](../tests/README.md)।

## पिछला पाठ

[एजेंटिक डिजाइन पैटर्न को समझना](../03-agentic-design-patterns/README.md)

## अगला पाठ

[एजेंटिक RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->