[![कैसे अच्छे AI एजेंट डिज़ाइन करें](../../../translated_images/hi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(इस पाठ का वीडियो देखने के लिए ऊपर की छवि पर क्लिक करें)_

# टूल उपयोग डिज़ाइन पैटर्न

टूल्स दिलचस्प हैं क्योंकि वे AI एजेंटों को अधिक व्यापक क्षमताओं की अनुमति देते हैं। एजेंट के पास सीमित क्रियाओं का सेट होने के बजाय, एक टूल जोड़ने से एजेंट अब कई प्रकार की क्रियाएं कर सकता है। इस अध्याय में, हम टूल उपयोग डिज़ाइन पैटर्न पर नजर डालेंगे, जो बताता है कि AI एजेंट कैसे अपने लक्ष्यों को प्राप्त करने के लिए विशिष्ट टूल का उपयोग कर सकते हैं।

## परिचय

इस पाठ में, हम निम्नलिखित प्रश्नों के उत्तर खोजने जा रहे हैं:

- टूल उपयोग डिज़ाइन पैटर्न क्या है?
- यह किन उपयोग मामलों पर लागू किया जा सकता है?
- डिज़ाइन पैटर्न को लागू करने के लिए कौन से तत्व/निर्माण खंड आवश्यक हैं?
- भरोसेमंद AI एजेंट बनाने के लिए टूल उपयोग डिज़ाइन पैटर्न का उपयोग करते समय किन विशेष बातों का ध्यान रखना चाहिए?

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप सक्षम होंगे:

- टूल उपयोग डिज़ाइन पैटर्न और उसका उद्देश्य परिभाषित करना।
- उन उपयोग मामलों की पहचान करना जहां यह डिज़ाइन पैटर्न लागू है।
- डिज़ाइन पैटर्न को लागू करने के लिए आवश्यक मुख्य तत्वों को समझना।
- इस डिज़ाइन पैटर्न के उपयोग से AI एजेंटों में विश्वसनीयता सुनिश्चित करने के लिए विचारों को पहचानना।

## टूल उपयोग डिज़ाइन पैटर्न क्या है?

**टूल उपयोग डिज़ाइन पैटर्न** LLMs को बाहरी टूल्स के साथ इंटरैक्ट करने की क्षमता देने पर केंद्रित है, ताकि विशिष्ट लक्ष्य पूरी किए जा सकें। टूल्स ऐसे कोड होते हैं जिन्हें एजेंट द्वारा क्रियान्वित किया जाता है। एक टूल एक साधारण फ़ंक्शन हो सकता है, जैसे एक कैलकुलेटर, या तीसरे पक्ष की सेवा जैसे स्टॉक मूल्य खोज या मौसम पूर्वानुमान के लिए API कॉल। AI एजेंटों के संदर्भ में, टूल्स को इस तरह डिज़ाइन किया जाता है कि एजेंट इन्हें **मॉडल-जनित फ़ंक्शन कॉल्स** पर प्रतिक्रिया स्वरूप चलाते हैं।

## यह किन उपयोग मामलों पर लागू किया जा सकता है?

AI एजेंट टूल्स का उपयोग जटिल कार्य पूरा करने, जानकारी पुनः प्राप्त करने या निर्णय लेने के लिए कर सकते हैं। टूल उपयोग डिज़ाइन पैटर्न आमतौर पर उन परिदृश्यों में उपयोग किया जाता है जिनमें बाहरी सिस्टम के साथ गतिशील सहयोग की आवश्यकता होती है, जैसे डेटाबेस, वेब सेवाएं या कोड इंटरप्रेटर। यह कुछ उपयोग मामलों के लिए लाभकारी है, जैसे:

- **गतिशील जानकारी पुनः प्राप्ति:** एजेंट बाहरी API या डेटाबेस से नवीनतम डेटा प्राप्त कर सकते हैं (जैसे SQLite डेटाबेस से डेटा एनालिसिस के लिए क्वेरी करना, स्टॉक कीमतें या मौसम जानकारी प्राप्त करना)।
- **कोड निष्पादन और व्याख्या:** एजेंट गणितीय समस्याओं को हल करने, रिपोर्ट तैयार करने या सिमुलेशन करने के लिए कोड या स्क्रिप्ट चला सकते हैं।
- **कार्यप्रवाह स्वचालन:** टास्क शेड्यूलर, ईमेल सेवाओं या डाटा पाइपलाइनों जैसे टूल्स के एकीकरण से बार-बार या बहु-चरण वाला कार्यप्रवाह स्वचालित करना।
- **ग्राहक सहायता:** एजेंट CRM सिस्टम, टिकटिंग प्लेटफार्म या ज्ञान भंडार के साथ इंटरैक्ट कर उपयोगकर्ता प्रश्नों को हल कर सकते हैं।
- **सामग्री निर्माण और संपादन:** एजेंट ग्रामर चेकर, टेक्स्ट समरीकारक या सामग्री सुरक्षा मूल्यांकन जैसे टूल का उपयोग करके सामग्री निर्माण कार्यों में सहायता कर सकते हैं।

## टूल उपयोग डिज़ाइन पैटर्न को लागू करने के लिए कौन से तत्व/निर्माण खंड आवश्यक हैं?

ये निर्माण खंड AI एजेंट को विभिन्न कार्यों को करने योग्य बनाते हैं। चलिए, टूल उपयोग डिज़ाइन पैटर्न को लागू करने के लिए आवश्यक मुख्य तत्वों को देखें:

- **फ़ंक्शन/टूल स्कीमास**: उपलब्ध टूल्स की विस्तृत परिभाषाएं, जिनमें फ़ंक्शन का नाम, उद्देश्य, आवश्यक पैरामीटर और अपेक्षित आउटपुट शामिल हैं। ये स्कीमास LLM को समझने में मदद करते हैं कि कौन से टूल उपलब्ध हैं और वैध अनुरोध कैसे बनाएं।

- **फ़ंक्शन निष्पादन तर्क**: उपयोगकर्ता की मंशा और वार्तालाप संदर्भ के आधार पर टूल्स को कब और कैसे बुलाना है, इसे नियंत्रित करता है। इसमें योजना बनाने वाले मॉड्यूल, रूटिंग तंत्र या उन परिस्थितिजन्य प्रवाह शामिल हो सकते हैं जो टूल उपयोग को गतिशील रूप से निर्धारित करते हैं।

- **संदेश हैंडलिंग सिस्टम**: घटक जो उपयोगकर्ता इनपुट, LLM प्रतिक्रिया, टूल कॉल्स और टूल आउटपुट के बीच वार्तालाप प्रवाह को प्रबंधित करते हैं।

- **टूल इंटीग्रेशन फ्रेमवर्क**: एजेंट को विभिन्न टूल्स के साथ जोड़ने वाली अवसंरचना, चाहे वे सरल फ़ंक्शन हों या जटिल बाहरी सेवाएं।

- **त्रुटि हैंडलिंग और सत्यापन**: टूल निष्पादन में विफलताओं को संभालने के तंत्र, पैरामीटर मान्यकरण, और अप्रत्याशित प्रतिक्रियाओं का प्रबंधन।

- **राज्य प्रबंधन**: वार्तालाप संदर्भ, पिछले टूल इंटरैक्शन, और सतत डेटा को ट्रैक करता है ताकि बहु-चरण इंटरैक्शन में स्थिरता बनी रहे।

अब, आइए फ़ंक्शन/टूल कॉलिंग को विस्तार से देखें।

### फ़ंक्शन/टूल कॉलिंग

फ़ंक्शन कॉलिंग वह मुख्य तरीका है जिससे हम LLMs को टूल्स के साथ इंटरैक्ट करने में सक्षम बनाते हैं। आप अक्सर 'फ़ंक्शन' और 'टूल' शब्दों का पर्यायवाची उपयोग देखते हैं क्योंकि 'फ़ंक्शन्स' (पुन: उपयोग किए जाने वाले कोड के ब्लॉक्स) एजेंट द्वारा कार्य करने के लिए उपयोग किए जाने वाले 'टूल्स' ही होते हैं। किसी फ़ंक्शन के कोड को कॉल करने के लिए, LLM को उपयोगकर्ता के अनुरोध की तुलना फ़ंक्शन के विवरण से करनी होती है। इसके लिए, एक स्कीमा जिसमें सभी उपलब्ध फ़ंक्शन्स के विवरण शामिल होते हैं, LLM को भेजा जाता है। फिर LLM उस कार्य के लिए सबसे उपयुक्त फ़ंक्शन चुनता है और उसका नाम व तर्क वापस करता है। चयनित फ़ंक्शन को कॉल किया जाता है, उसका उत्तर LLM को भेजा जाता है, जो उपयोगकर्ता के अनुरोध का जवाब देने के लिए उस जानकारी का प्रयोग करता है।

डेवलपर्स के लिए एजेंट के लिए फ़ंक्शन कॉलिंग लागू करने हेतु आपको चाहिए:

1. ऐसा LLM मॉडल जो फ़ंक्शन कॉलिंग का समर्थन करता हो
2. फ़ंक्शन विवरण वाला स्कीमा
3. वर्णित प्रत्येक फ़ंक्शन का कोड

उदाहरण के लिए, किसी शहर में वर्तमान समय प्राप्त करने को समझाते हैं:

1. **फ़ंक्शन कॉलिंग समर्थित LLM इनिशियलाइज़ करें:**

    सभी मॉडल फ़ंक्शन कॉलिंग का समर्थन नहीं करते, अतः यह जांचना जरूरी है कि आपका LLM ऐसा करता है या नहीं। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> फ़ंक्शन कॉलिंग का समर्थन करता है। हम Azure OpenAI क्लाइंट की स्थापना से शुरू करते हैं। 

    ```python
    # Azure OpenAI क्लाइंट को इनिशियलाइज़ करें
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **एक फ़ंक्शन स्कीमा बनाएं**:

    इसके बाद हम एक JSON स्कीमा परिभाषित करेंगे जिसमें फ़ंक्शन का नाम, फ़ंक्शन क्या करता है इसका विवरण, और फ़ंक्शन पैरामीटर के नाम व विवरण शामिल होंगे।
    इस स्कीमा को हम पूर्व में बनाए क्लाइंट को उपयोगकर्ता के अनुरोध के साथ पास करेंगे ताकि सैन फ्रांसिस्को में समय जानने के लिए उपयोग हो सके। ध्यान देना ज़रूरी है कि **टूल कॉल** ही वापस आता है, **सवाल का अंतिम उत्तर नहीं**। जैसा पहले बताया गया, LLM उस कार्य के लिए चुने गए फ़ंक्शन का नाम और जो तर्क पास होंगे उन्हें लौटाता है।

    ```python
    # मॉडल के लिए फ़ंक्शन विवरण पढ़ने के लिए
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
  
    # प्रारंभिक उपयोगकर्ता संदेश
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # पहली एपीआई कॉल: मॉडल से फ़ंक्शन का उपयोग करने के लिए कहें
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # मॉडल के उत्तर को संसाधित करें
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **कार्य को पूरा करने हेतु आवश्यक फ़ंक्शन कोड:**

    अब जब LLM ने फ़ंक्शन चुन लिया है तो कार्य को पूरा करने वाला कोड लागू और निष्पादित करना आवश्यक है।
    हम पायथन में वर्तमान समय प्राप्त करने का कोड लागू कर सकते हैं। हमें यह भी कोड लिखना होगा जो response_message से नाम और तर्क निकालकर अंतिम परिणाम प्राप्त करे।

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
     # फ़ंक्शन कॉल संभालें
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
  
      # दूसरा API कॉल: मॉडल से अंतिम प्रतिक्रिया प्राप्त करें
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

फ़ंक्शन कॉलिंग अधिकांश, यदि सभी नहीं तो, एजेंट टूल उपयोग डिज़ाइन का मूल है, लेकिन इसे शून्य से लागू करना कभी-कभी चुनौतीपूर्ण हो सकता है।
जैसा कि हमने [Lesson 2](../../../02-explore-agentic-frameworks) में सीखा, एजेंटिक फ्रेमवर्क टूल उपयोग को लागू करने के लिए पूर्व-निर्मित निर्माण खंड प्रदान करते हैं।

## एजेंटिक फ्रेमवर्क के साथ टूल उपयोग उदाहरण

यहाँ कुछ उदाहरण दिए गए हैं कि आप टूल उपयोग डिज़ाइन पैटर्न को विभिन्न एजेंटिक फ्रेमवर्क के साथ कैसे लागू कर सकते हैं:

### माइक्रोसॉफ्ट एजेंट फ्रेमवर्क

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> एक ओपन-सोर्स AI फ्रेमवर्क है जो AI एजेंट बनाने में सहायता करता है। यह फ़ंक्शन कॉलिंग को सरल बनाता है क्योंकि आप टूल्स को Python फ़ंक्शन्स के रूप में `@tool` डेकोरेटर के साथ परिभाषित कर सकते हैं। फ्रेमवर्क मॉडल और आपके कोड के बीच संवाद को संभालता है। यह `AzureAIProjectAgentProvider` के माध्यम से फ़ाइल खोज और कोड इंटरप्रेटर जैसे पूर्व-निर्मित टूल्स तक पहुँच भी प्रदान करता है।

निम्न आरेख Microsoft Agent Framework के साथ फ़ंक्शन कॉलिंग की प्रक्रिया को दर्शाता है:

![function calling](../../../translated_images/hi/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework में, टूल्स को डेकोरेटेड फ़ंक्शन्स के रूप में परिभाषित किया जाता है। हम पहले देखा गया `get_current_time` फ़ंक्शन को `@tool` डेकोरेटर का उपयोग कर एक टूल में परिवर्तित कर सकते हैं। फ्रेमवर्क स्वचालित रूप से फ़ंक्शन और उसके पैरामीटर को सीरियलाइज़ करेगा, LLM को भेजने के लिए स्कीमा बनाएगा।

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# क्लाइंट बनाएँ
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# एक एजेंट बनाएँ और टूल के साथ चलाएँ
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> एक नया एजेंटिक फ्रेमवर्क है जो डेवलपर्स को सुरक्षित रूप से उच्च गुणवत्ता और विस्तारशील AI एजेंट बनाने, तैनात करने और स्केल करने की क्षमता देता है, बिना अंतर्निहित कंप्यूट और स्टोरेज संसाधनों का प्रबंधन किए। यह विशेष रूप से एंटरप्राइज एप्लिकेशन के लिए उपयोगी है क्योंकि यह एक पूरी तरह से प्रबंधित सेवा है जिसमें एंटरप्राइज स्तर की सुरक्षा होती है।

LLM API के सीधे विकास की तुलना में, Azure AI Agent Service कुछ फायदे प्रदान करता है, जैसे:

- स्वचालित टूल कॉलिंग – टूल कॉल को पार्स करने, टूल को कॉल करने और प्रतिक्रिया संभालने की आवश्यकता नहीं; यह सब अब सर्वर-साइड होता है
- सुरक्षित डेटा प्रबंधन – अपनी खुद की कंटेक्स्ट स्टेट मैनेज करने के बजाय, आप थ्रेड्स पर भरोसा कर सकते हैं जो सभी आवश्यक जानकारी संग्रहीत करते हैं
- आउट-ऑफ़-द-बॉक्स टूल्स – ऐसे टूल्स जिनका उपयोग आप अपने डेटा स्रोतों के साथ इंटरैक्ट करने के लिए कर सकते हैं, जैसे Bing, Azure AI Search, और Azure Functions।

Azure AI Agent Service में उपलब्ध टूल्स को दो श्रेणियों में बांटा जा सकता है:

1. ज्ञान टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search के साथ ग्राउंडिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">फाइल खोज</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. कार्य टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">फ़ंक्शन कॉलिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इंटरप्रेटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित टूल्स</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

एजेंट सेवा हमें इन टूल्स का एक `toolset` के रूप में उपयोग करने की अनुमति देती है। यह `threads` का उपयोग भी करता है जो किसी विशिष्ट वार्तालाप से संदेशों के इतिहास को ट्रैक करते हैं।

कल्पना करें कि आप Contoso नामक कंपनी में एक बिक्री एजेंट हैं। आप एक संवादात्मक एजेंट विकसित करना चाहते हैं जो आपकी बिक्री डेटा से संबंधित प्रश्नों के उत्तर दे सकता हो।

निम्न चित्र दर्शाता है कि आप Azure AI Agent Service का उपयोग कर अपनी बिक्री डेटा का विश्लेषण कैसे कर सकते हैं:

![Agentic Service In Action](../../../translated_images/hi/agent-service-in-action.34fb465c9a84659e.webp)

सेवा के साथ इन टूल्स का उपयोग करने के लिए, हम एक क्लाइंट बना सकते हैं और एक टूल या टूलसेट परिभाषित कर सकते हैं। व्यावहारिक रूप से इसे लागू करने के लिए हम निम्न Python कोड का उपयोग कर सकते हैं। LLM टूलसेट को देखकर यह निर्णय ले सकता है कि उपयोगकर्ता के अनुरोध के आधार पर उपयोगकर्ता निर्मित फ़ंक्शन `fetch_sales_data_using_sqlite_query` का उपयोग करना है या पूर्व-निर्मित कोड इंटरप्रेटर।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query फ़ंक्शन जिसे fetch_sales_data_data_functions.py फ़ाइल में पाया जा सकता है।
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# टूलसेट शुरू करें
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query फ़ंक्शन के साथ फ़ंक्शन कॉलिंग एजेंट आरंभ करें और इसे टूलसेट में जोड़ें
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# कोड इंटरप्रेटर टूल आरंभ करें और इसे टूलसेट में जोड़ें।
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## भरोसेमंद AI एजेंट बनाने के लिए टूल उपयोग डिज़ाइन पैटर्न का उपयोग करते समय विशेष विचार क्या हैं?

LLMs द्वारा गतिशील रूप से जेनरेट किए गए SQL के साथ एक आम चिंता सुरक्षा है, विशेष रूप से SQL इंजेक्शन या दुर्भावनापूर्ण क्रियाओं का खतरा, जैसे कि डेटाबेस ड्रॉप करना या उसमें छेड़छाड़ करना। ये चिंताएं वैध हैं, लेकिन उचित डेटाबेस एक्सेस अनुमतियां सेट करके इन्हें प्रभावी रूप से कम किया जा सकता है। अधिकांश डेटाबेस के लिए यह पढ़ने-केवल (read-only) मोड में डेटाबेस को कॉन्फ़िगर करने में शामिल है। PostgreSQL या Azure SQL जैसे डेटाबेस सेवाओं के लिए, ऐप को केवल पढ़ने-केवल (SELECT) भूमिका सौंपनी चाहिए।

ऐप को सुरक्षित वातावरण में चलाना सुरक्षा को और बढ़ाता है। उद्यम परिदृश्यों में, डेटा को आमतौर पर परिचालन सिस्टम से निकालकर एक पढ़ने-केवल डेटाबेस या डेटा वेयरहाउस में ट्रांसफ़ॉर्म किया जाता है जिसमें उपयोगकर्ता के अनुकूल स्कीमा होता है। यह दृष्टिकोण सुनिश्चित करता है कि डेटा सुरक्षित, प्रदर्शन और सुलभता के लिए अनुकूलित है, और ऐप को सीमित, पढ़ने-केवल एक्सेस प्राप्त होता है।

## नमूना कोड

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## टूल उपयोग डिज़ाइन पैटर्न के बारे में और सवाल हैं?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) जॉइन करें, जहाँ आप अन्य शिक्षार्थियों से मिल सकते हैं, ऑफिस आवर्स में भाग ले सकते हैं और अपने AI एजेंट संबंधी प्रश्नों का उत्तर पा सकते हैं।

## अतिरिक्त संसाधन

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service कार्यशाला</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer मल्टी-एजेंट कार्यशाला</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework अवलोकन</a>

## पिछला पाठ

[एजेंटिक डिज़ाइन पैटर्न समझना](../03-agentic-design-patterns/README.md)

## अगला पाठ
[एजेंटिक RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->