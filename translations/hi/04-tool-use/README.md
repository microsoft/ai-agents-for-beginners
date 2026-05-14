[![कैसे डिज़ाइन करें अच्छे AI एजेंट्स](../../../translated_images/hi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(वीडियो देखने के लिए ऊपर दी गई छवि पर क्लिक करें)_

# टूल उपयोग डिज़ाइन पैटर्न

टूल्स दिलचस्प होते हैं क्योंकि वे AI एजेंट्स को अधिक व्यापक क्षमताओं की अनुमति देते हैं। एजेंट के पास केवल सीमित क्रियाओं का सेट होने के बजाय, टूल जोड़कर एजेंट अब कई प्रकार की क्रियाएं कर सकता है। इस अध्याय में, हम टूल उपयोग डिज़ाइन पैटर्न को देखेंगे, जो यह बताता है कि AI एजेंट्स अपने लक्ष्यों को प्राप्त करने के लिए विशिष्ट टूल्स का उपयोग कैसे कर सकते हैं।

## परिचय

इस पाठ में, हम निम्नलिखित प्रश्नों के उत्तर खोज रहे हैं:

- टूल उपयोग डिज़ाइन पैटर्न क्या है?
- किन-किन उपयोग मामलों में इसे लागू किया जा सकता है?
- डिज़ाइन पैटर्न को लागू करने के लिए कौन से तत्व/बिल्डिंग ब्लॉक्स आवश्यक हैं?
- विश्वसनीय AI एजेंट्स बनाने के लिए टूल उपयोग डिज़ाइन पैटर्न का उपयोग करते समय किन विशेष विचारों का ध्यान रखना चाहिए?

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप सक्षम होंगे:

- टूल उपयोग डिज़ाइन पैटर्न और इसका उद्देश्य परिभाषित करना।
- उन उपयोग मामलों की पहचान करना जहां टूल उपयोग डिज़ाइन पैटर्न लागू होता है।
- डिज़ाइन पैटर्न लागू करने के लिए आवश्यक मुख्य तत्वों को समझना।
- इस डिज़ाइन पैटर्न का उपयोग करने वाले AI एजेंट्स में विश्वसनीयता सुनिश्चित करने के लिए विचारों को पहचानना।

## टूल उपयोग डिज़ाइन पैटर्न क्या है?

**टूल उपयोग डिज़ाइन पैटर्न** का मुख्य फोकस LLMs को बाहरी टूल्स के साथ इंटरैक्ट करने की क्षमता देना है ताकि वे विशिष्ट लक्ष्यों को प्राप्त कर सकें। टूल्स ऐसे कोड होते हैं जिन्हें एजेंट द्वारा क्रियान्वित किया जाता है ताकि वे कार्य कर सकें। एक टूल एक सरल फ़ंक्शन हो सकता है जैसे कैलकुलेटर, या कोई तृतीय-पक्ष सेवा जैसे स्टॉक की कीमत देखना या मौसम का पूर्वानुमान। AI एजेंट्स के संदर्भ में, टूल्स को मॉडल-जनित फ़ंक्शन कॉल के जवाब में एजेंट द्वारा क्रियान्वित करने के लिए डिज़ाइन किया गया है।

## किन उपयोग मामलों में इसे लागू किया जा सकता है?

AI एजेंट्स टूल्स का उपयोग जटिल कार्यों को पूरा करने, जानकारी प्राप्त करने या निर्णय लेने के लिए कर सकते हैं। टूल उपयोग डिज़ाइन पैटर्न आमतौर पर उन परिदृश्यों में इस्तेमाल किया जाता है जहां बाहरी प्रणालियों से गतिशील इंटरैक्शन आवश्यक होता है, जैसे डेटाबेस, वेब सेवाओं या कोड इंटरप्रेटरों के साथ। यह क्षमता विभिन्न उपयोग मामलों के लिए उपयोगी है, जिनमें शामिल हैं:

- **गतिशील सूचना पुनःप्राप्ति:** एजेंट बाहरी API या डेटाबेस से अद्यतन डेटा प्राप्त कर सकते हैं (जैसे, डेटा विश्लेषण के लिए SQLite डेटाबेस क्वेरी करना, स्टॉक कीमतें या मौसम की जानकारी प्राप्त करना)।
- **कोड निष्पादन और व्याख्या:** एजेंट गणितीय समस्याओं को हल करने, रिपोर्ट बनाने, या सिमुलेशन करने के लिए कोड या स्क्रिप्ट्स को निष्पादित कर सकते हैं।
- **वर्कफ़्लो स्वचालन:** टूल्स जैसे टास्क शेड्यूलर, ईमेल सेवाएँ, या डेटा पाइपलाइंस के एकीकरण से पुनरावृत्ति या मल्टी-स्टेप वर्कफ़्लो को स्वचालित करना।
- **ग्राहक सहायता:** एजेंट CRM सिस्टम, टिकेटिंग प्लेटफ़ॉर्म, या ज्ञान आधार के साथ इंटरैक्ट कर उपयोगकर्ता प्रश्नों का समाधान कर सकते हैं।
- **सामग्री निर्माण और संपादन:** एजेंट व्याकरण जांच, टेक्स्ट सारांश, या सामग्री सुरक्षा मूल्यांकन जैसे टूल्स का उपयोग सामग्री निर्माण कार्यों में सहायता के लिए कर सकते हैं।

## टूल उपयोग डिज़ाइन पैटर्न लागू करने के लिए आवश्यक तत्व/बिल्डिंग ब्लॉक्स कौन से हैं?

ये बिल्डिंग ब्लॉक्स AI एजेंट को विविध कार्य करने में सक्षम बनाते हैं। टूल उपयोग डिज़ाइन पैटर्न लागू करने के लिए आवश्यक मुख्य तत्व हैं:

- **फ़ंक्शन/टूल स्कीमा** : उपलब्ध टूल्स की विस्तृत परिभाषाएं, जिनमें फ़ंक्शन का नाम, उद्देश्य, आवश्यक पैरामीटर और अपेक्षित आउटपुट शामिल हैं। ये स्कीमा LLM को यह समझने में सक्षम बनाते हैं कि कौन से टूल उपलब्ध हैं और वैध अनुरोध कैसे बनाए जाएं।

- **फ़ंक्शन निष्पादन लॉजिक** : उपयोगकर्ता की मंशा और बातचीत के संदर्भ के आधार पर टूल्स के कब और कैसे बुलाए जाएं इसका निर्धारण करता है। इसमें योजनाकार मॉड्यूल, राउटिंग तंत्र, या शर्तीय प्रवाह शामिल हो सकते हैं जो गतिशील रूप से टूल उपयोग निर्धारित करते हैं।

- **संदेश प्रबंधन प्रणाली** : उपयोगकर्ता इनपुट, LLM प्रतिक्रियाओं, टूल कॉल्स, और टूल आउटपुट के बीच संवाद प्रवाह को प्रबंधित करती है।

- **टूल एकीकरण फ्रेमवर्क** : एजेंट को विभिन्न टूल्स से जोड़ने के लिए अवसंरचना, चाहे वे सरल फंक्शन हों या जटिल बाहरी सेवाएं।

- **त्रुटि प्रबंधन और मान्यता** : टूल निष्पादन में असफलताओं को संभालने, पैरामीटरों को मान्य करने, और अप्रत्याशित प्रतिक्रियाओं का प्रबंधन करने के तंत्र।

- **स्थिति प्रबंधन** : बातचीत का संदर्भ, पिछले टूल इंटरैक्शन, और स्थायी डेटा को ट्रैक करता है ताकि बहु-चरण बातचीत में स्थिरता बनी रहे।

अब, फ़ंक्शन/टूल कॉलिंग को विस्तार से देखते हैं।

### फ़ंक्शन/टूल कॉलिंग

फ़ंक्शन कॉलिंग वह मुख्य तरीका है जिससे हम बड़े भाषा मॉडल (LLMs) को टूल्स के साथ इंटरैक्ट करने योग्य बनाते हैं। अक्सर 'फ़ंक्शन' और 'टूल' शब्दों का समानार्थक उपयोग होता है क्योंकि 'फ़ंक्शन' (कोड के पुन: उपयोगी ब्लॉक) वे 'टूल्स' हैं जिन्हें एजेंट कार्य करने के लिए उपयोग करते हैं। किसी फ़ंक्शन का कोड कॉल होने के लिए, LLM को उपयोगकर्ता के अनुरोध की तुलना फ़ंक्शन के विवरण से करनी होती है। इसके लिए, सभी उपलब्ध फ़ंक्शनों के विवरण वाला एक स्कीमा LLM को भेजा जाता है। LLM विशिष्ट कार्य के लिए सबसे उपयुक्त फ़ंक्शन चुनता है और उसका नाम व तर्क लौटाता है। चुना हुआ फ़ंक्शन क्रियान्वित होता है, उसकी प्रतिक्रिया LLM को वापस भेजी जाती है, जो उस जानकारी का उपयोग उपयोगकर्ता के अनुरोध का जवाब देने के लिए करता है।

डेवलपर्स के लिए फ़ंक्शन कॉलिंग लागू करने के लिए आपके पास होना चाहिए:

1. एक ऐसा LLM मॉडल जो फ़ंक्शन कॉलिंग समर्थित हो।
2. फ़ंक्शन विवरणों वाला स्कीमा।
3. प्रत्येक वर्णित फ़ंक्शन के लिए कोड।

एक उदाहरण के रूप में, किसी शहर का वर्तमान समय प्राप्त करने के लिए चलिए समझते हैं:

1. **ऐसा LLM इनिशियलाइज़ करें जो फ़ंक्शन कॉलिंग का समर्थन करता हो:**

    सभी मॉडलों में फ़ंक्शन कॉलिंग का समर्थन नहीं होता, इसलिए यह जांचना आवश्यक है कि आप जिस LLM का उपयोग कर रहे हैं उसमें यह फीचर मौजूद है। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> फ़ंक्शन कॉलिंग का समर्थन करता है। हम Azure OpenAI क्लाइंट को इनिशियलाइज़ करके शुरू कर सकते हैं।

    ```python
    # Azure OpenAI क्लाइंट को प्रारंभ करें
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **फ़ंक्शन स्कीमा बनाएं:**

    अगला कदम है JSON स्कीमा परिभाषित करना जिसमें फ़ंक्शन का नाम, क्या करता है इस बात का विवरण, और फ़ंक्शन पैरामीटर के नाम व विवरण शामिल हों। फिर इस स्कीमा को पिछले चरण में बनाए गए क्लाइंट को, साथ ही उपयोगकर्ता के अनुरोध के साथ पास किया जाएगा ताकि सैन फ्रांसिस्को में समय पता चल सके। ध्यान देने वाली बात यह है कि यहाँ जो परिणाम आता है वह **टूल कॉल** होता है, प्रश्न का अंतिम जवाब नहीं। जैसा कि पहले बताया गया, LLM कार्य के लिए चुने गए फ़ंक्शन का नाम और उसे दिए जाने वाले तर्क लौटाता है।

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
  
    # पहला एपीआई कॉल: मॉडल से फ़ंक्शन का उपयोग करने के लिए कहें
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # मॉडल की प्रतिक्रिया को संसाधित करें
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
3. **कार्य को पूरा करने वाला फ़ंक्शन कोड:**

    अब जब LLM ने निर्धारित कर लिया है कि कौन सा फ़ंक्शन चलाना है, तो उस कार्य को करने वाला कोड लिखा और क्रियान्वित किया जाना चाहिए। हम पायथन में वर्तमान समय प्राप्त करने का कोड लिख सकते हैं। हमें response_message से नाम और तर्क निकालने का कोड भी लिखना होगा ताकि अंतिम परिणाम मिल सके।

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


फ़ंक्शन कॉलिंग अधिकांश, यदि सभी नहीं, एजेंट टूल उपयोग डिज़ाइन का मूल बिंदु है, लेकिन इसे शुरुआती से ठीक तरह से लागू करना कभी-कभी चुनौतीपूर्ण हो सकता है। जैसा हमने [पाठ 2](../../../02-explore-agentic-frameworks) में सीखा, एजेंटिक फ्रेमवर्क हमें टूल उपयोग लागू करने के लिए पूर्व-निर्मित बिल्डिंग ब्लॉक्स प्रदान करते हैं।

## एजेंटिक फ्रेमवर्क के साथ टूल उपयोग उदाहरण

यहां कुछ उदाहरण हैं कि आप विभिन्न एजेंटिक फ्रेमवर्क का उपयोग करके टूल उपयोग डिज़ाइन पैटर्न कैसे लागू कर सकते हैं:

### माइक्रोसॉफ्ट एजेंट फ्रेमवर्क

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">माइक्रोसॉफ्ट एजेंट फ्रेमवर्क</a> AI एजेंट बनाने के लिए एक ओपन-सोर्स AI फ्रेमवर्क है। यह फ़ंक्शन कॉलिंग की प्रक्रिया को सरल बनाता है, जिससे आप टूल्स को `@tool` डेकोरेटर के साथ पायथन फ़ंक्शनों के रूप में परिभाषित कर सकते हैं। यह फ्रेमवर्क मॉडल और आपके कोड के बीच दो-तरफा संवाद को संभालता है। यह `AzureAIProjectAgentProvider` के माध्यम से जैसे फ़ाइल खोज और कोड इंटरप्रेटर जैसे पूर्व-निर्मित टूल्स तक भी पहुँच प्रदान करता है।

निम्नलिखित चित्र माइक्रोसॉफ्ट एजेंट फ्रेमवर्क में फ़ंक्शन कॉलिंग की प्रक्रिया को दर्शाता है:

![function calling](../../../translated_images/hi/functioncalling-diagram.a84006fc287f6014.webp)

माइक्रोसॉफ्ट एजेंट फ्रेमवर्क में, टूल्स को डेकोरेटेड फ़ंक्शनों के रूप में परिभाषित किया जाता है। हम पहले देखे गए `get_current_time` फ़ंक्शन को `@tool` डेकोरेटर का उपयोग करके टूल में परिवर्तित कर सकते हैं। फ्रेमवर्क स्वतः फ़ंक्शन और उसके पैरामीटरों को सीरियलाइज़ करता है, स्कीमा बनाता है और इसे LLM को भेजता है।

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# क्लाइंट बनाएं
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# एक एजेंट बनाएं और टूल के साथ चलाएं
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> एक नवीन एजेंटिक फ्रेमवर्क है जिसे डेवलपर्स को सुरक्षित रूप से उच्च गुणवत्ता वाले और विस्तारणीय AI एजेंट्स बनाने, तैनात करने और स्केलेबल बनाने के लिए डिज़ाइन किया गया है, बिना अंतर्निहित कंप्यूट और स्टोरेज संसाधनों का प्रबंधन किए। यह खासकर एंटरप्राइज़ अनुप्रयोगों के लिए उपयोगी है क्योंकि यह पूर्ण प्रबंधित सेवा है जिसमें एंटरप्राइज़ स्तरीय सुरक्षा है।

LLM API के सीधे विकास से तुलना करने पर, Azure AI Agent Service कुछ फायदे प्रदान करता है, जिनमें शामिल हैं:

- स्वचालित टूल कॉलिंग – टूल कॉल पार्स करने, टूल को invoke करने और प्रतिक्रिया को हैंडल करने की आवश्यकता नहीं; ये सभी अब सर्वर-साइड होते हैं
- सुरक्षित रूप से प्रबंधित डेटा – अपनी बातचीत की स्थिति के प्रबंधन के बजाय, आप थ्रेड्स पर भरोसा कर सकते हैं जो आपको आवश्यक सभी जानकारी संग्रहीत करते हैं
- आउट-ऑफ-द-बॉक्स टूल्स – ऐसे टूल्स जो आपके डेटा स्रोतों के साथ इंटरैक्ट करने के लिए उपलब्ध हैं, जैसे Bing, Azure AI Search, और Azure Functions।

Azure AI Agent Service में उपलब्ध टूल्स को दो श्रेणियों में विभाजित किया जा सकता है:

1. नॉलेज टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search के साथ ग्राउंडिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">फ़ाइल खोज</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. कार्य टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">फ़ंक्शन कॉलिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इंटरप्रेटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित टूल्स</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

एजेंट सेवा हमें इन टूल्स को `toolset` के रूप में एक साथ उपयोग करने की अनुमति देता है। यह `threads` भी उपयोग करता है जो किसी विशेष वार्तालाप का संदेश इतिहास ट्रैक करते हैं।

कल्पना करें कि आप Contoso नामक कंपनी में एक बिक्री एजेंट हैं। आप एक संवादात्मक एजेंट विकसित करना चाहते हैं जो आपकी बिक्री डेटा से संबंधित प्रश्नों का उत्तर दे सके।

निम्न चित्र दर्शाता है कि आप अपने बिक्री डेटा का विश्लेषण करने के लिए Azure AI Agent Service का उपयोग कैसे कर सकते हैं:

![Agentic Service In Action](../../../translated_images/hi/agent-service-in-action.34fb465c9a84659e.webp)

सेवा के साथ इन टूल्स में से किसी का उपयोग करने के लिए हम एक क्लाइंट बना सकते हैं और एक टूल या टूलसेट परिभाषित कर सकते हैं। व्यावहारिक रूप से इसे लागू करने के लिए हम निम्न पायथन कोड का उपयोग कर सकते हैं। LLM टूलसेट को देखकर निर्णय ले सकता है कि उपयोगकर्ता बनाए फ़ंक्शन `fetch_sales_data_using_sqlite_query` का उपयोग करना है या प्री-बिल्ट कोड इंटरप्रेटर का, यह उपयोगकर्ता के अनुरोध पर निर्भर करेगा।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query फ़ंक्शन जो fetch_sales_data_functions.py फ़ाइल में पाया जा सकता है।
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
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## विश्वसनीय AI एजेंट्स बनाने के लिए टूल उपयोग डिज़ाइन पैटर्न का उपयोग करते समय विशेष विचार क्या हैं?

LLMs द्वारा डायनेमिक रूप से जेनरेट किए गए SQL के साथ एक सामान्य चिंता सुरक्षा की होती है, खासकर SQL इंजेक्शन या दुर्भावनापूर्ण कार्यों का जोखिम, जैसे डेटाबेस को ड्रॉप करना या उसमें छेड़छाड़ करना। ये चिंताएं सही हैं, लेकिन डेटाबेस एक्सेस अनुमतियों को ठीक ढंग से कॉन्फ़िगर करके इन्हें प्रभावी ढंग से कम किया जा सकता है। अधिकांश डेटाबेस के लिए इसे रीड-ओनली के रूप में कॉन्फ़िगर करना शामिल होता है। PostgreSQL या Azure SQL जैसी डेटाबेस सेवाओं के लिए, ऐप को एक रीड-ओनली (SELECT) भूमिका आवंटित की जानी चाहिए।

एप्लिकेशन को सुरक्षित वातावरण में चलाने से सुरक्षा और मजबूत होती है। एंटरप्राइज़ परिदृश्यों में, डेटा को आमतौर पर परिचालन प्रणालियों से निकालकर एक रीड-ओनली डेटाबेस या data warehouse में बदला जाता है जिसमें एक उपयोगकर्ता-अनुकूल स्कीमा होता है। यह तरीका सुनिश्चित करता है कि डेटा सुरक्षित हो, प्रदर्शन और उपलब्धता के लिए अनुकूलित हो, और ऐप के पास सीमित, केवल-पढ़ने की पहुंच हो।

## नमूना कोड्स

- पायथन: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## टूल उपयोग डिज़ाइन पैटर्न के बारे में और प्रश्न हैं?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) से जुड़ें ताकि अन्य शिक्षार्थियों से मिल सकें, ऑफिस ऑवर्स में भाग ले सकें और अपने AI एजेंट्स के सवालों के जवाब पा सकें।

## अतिरिक्त संसाधन

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service कार्यशाला</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer मल्टी-एजेंट कार्यशाला</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework अवलोकन</a>

## पिछला पाठ

[एजेंटिक डिज़ाइन पैटर्न्स को समझना](../03-agentic-design-patterns/README.md)

## अगला पाठ
[एजेंटिक RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->