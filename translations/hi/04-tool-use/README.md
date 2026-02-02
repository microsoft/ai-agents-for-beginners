[![कैसे डिज़ाइन करें अच्छे AI एजेंट](../../../translated_images/hi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(इस पाठ का वीडियो देखने के लिए ऊपर की छवि पर क्लिक करें)_

# टूल उपयोग डिज़ाइन पैटर्न

टूल्स दिलचस्प हैं क्योंकि वे AI एजेंटों को अधिक व्यापक क्षमताओं की अनुमति देते हैं। एजेंट के पास जो क्रियाएँ सीमित होती हैं, उन्हें करने के बजाय, टूल जोड़ने से एजेंट अब कई प्रकार की क्रियाएँ कर सकता है। इस अध्याय में, हम टूल उपयोग डिज़ाइन पैटर्न को देखेंगे, जो वर्णन करता है कि AI एजेंट अपने लक्ष्यों को प्राप्त करने के लिए विशिष्ट टूल्स का उपयोग कैसे कर सकते हैं।

## परिचय

इस पाठ में, हम निम्नलिखित सवालों का उत्तर देने का प्रयास कर रहे हैं:

- टूल उपयोग डिज़ाइन पैटर्न क्या है?
- इसे किन उपयोग मामलों में लागू किया जा सकता है?
- डिज़ाइन पैटर्न को लागू करने के लिए आवश्यक तत्व/निर्माण खंड क्या हैं?
- विश्वसनीय AI एजेंट बनाने के लिए टूल उपयोग डिज़ाइन पैटर्न का उपयोग करते समय विशेष विचार क्या हैं?

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप सक्षम होंगे:

- टूल उपयोग डिज़ाइन पैटर्न और इसका उद्देश्य परिभाषित करना।
- उन उपयोग मामलों की पहचान करना जहाँ टूल उपयोग डिज़ाइन पैटर्न लागू होता है।
- डिज़ाइन पैटर्न को लागू करने के लिए आवश्यक प्रमुख तत्वों को समझना।
- इस डिज़ाइन पैटर्न का उपयोग करने वाले AI एजेंटों में विश्वसनीयता सुनिश्चित करने के लिए विचारों को पहचानना।

## टूल उपयोग डिज़ाइन पैटर्न क्या है?

**टूल उपयोग डिज़ाइन पैटर्न** LLMs को बाहरी टूल्स के साथ अंतःक्रिया करने की क्षमता देने पर केंद्रित है ताकि विशिष्ट लक्ष्यों को प्राप्त किया जा सके। टूल्स वे कोड होते हैं जिन्हें एजेंट द्वारा क्रियान्वित किया जाता है ताकि कार्रवाई की जा सके। एक टूल एक सरल फ़ंक्शन हो सकता है जैसे कैलकुलेटर, या तीसरे पक्ष की सेवा जैसे स्टॉक प्राइस लुकअप या मौसम पूर्वानुमान के लिए API कॉल। AI एजेंटों के संदर्भ में, टूल्स मॉडल-जनित फ़ंक्शन कॉल्स के जवाब में एजेंटों द्वारा निष्पादित किए जाने के लिए डिजाइन किए जाते हैं।

## इसे किन उपयोग मामलों में लागू किया जा सकता है?

AI एजेंट टूल्स का उपयोग जटिल कार्यों को पूरा करने, जानकारी प्राप्त करने या निर्णय लेने के लिए कर सकते हैं। टूल उपयोग डिज़ाइन पैटर्न उन परिस्थितियों में अक्सर उपयोग किया जाता है जहाँ बाहरी सिस्टम जैसे डाटाबेस, वेब सेवाओं या कोड इंटरप्रेटर्स के साथ गतिशील इंटरैक्शन की आवश्यकता होती है। इस क्षमता का उपयोग कई विभिन्न उपयोग मामलों के लिए किया जा सकता है, जिनमें शामिल हैं:

- **गतिशील सूचना पुनःप्राप्ति:** एजेंट बाहरी API या डाटाबेस से नवीनतम डेटा प्राप्त कर सकते हैं (उदा., डेटा विश्लेषण के लिए SQLite डाटाबेस से क्वेरी करना, स्टॉक की कीमतें या मौसम की जानकारी प्राप्त करना)।
- **कोड निष्पादन और व्याख्या:** एजेंट गणितीय समस्याओं को हल करने, रिपोर्ट बनाने, या सिमुलेशन करने के लिए कोड या स्क्रिप्ट्स चला सकते हैं।
- **वर्कफ़्लो स्वचालन:** टूल्स जैसे टास्क शेड्यूलर, ईमेल सेवाएँ, या डेटा पाइपलाइन्स का उपयोग करके दोहराए जाने वाले या बहु-चरण वर्कफ़्लो का ऑटोमेशन करना।
- **ग्राहक सहायता:** एजेंट CRM सिस्टम, टिकटिंग प्लेटफॉर्म, या ज्ञान-बेस के साथ इंटरैक्ट करके उपयोगकर्ता प्रश्नों का समाधान कर सकते हैं।
- **सामग्री निर्माण और संपादन:** एजेंट व्याकरण जांचने वाले, टेक्स्ट सारांशक, या कंटेंट सुरक्षा मूल्यांकन टूल्स का उपयोग करके सामग्री निर्माण कार्यों में मदद कर सकते हैं।

## टूल उपयोग डिज़ाइन पैटर्न को लागू करने के लिए आवश्यक तत्व/निर्माण खंड क्या हैं?

ये निर्माण खंड AI एजेंट को कई प्रकार के कार्यों को करने में सक्षम बनाते हैं। आइए टूल उपयोग डिज़ाइन पैटर्न को लागू करने के लिए आवश्यक प्रमुख तत्वों को देखें:

- **फ़ंक्शन/टूल स्कीमाएँ**: उपलब्ध टूल्स की विस्तृत परिभाषाएँ, जिनमें फ़ंक्शन का नाम, उद्देश्य, आवश्यक पैरामीटर, और अपेक्षित आउटपुट शामिल हैं। ये स्कीमाएँ LLM को यह समझने में मदद करती हैं कि कौन से टूल उपलब्ध हैं और मान्य अनुरोध कैसे बनाएँ।

- **फ़ंक्शन निष्पादन तर्क**: उपयोगकर्ता की मंशा और संवाद संदर्भ के आधार पर टूल्स कब और कैसे कॉल किए जाते हैं, यह नियंत्रित करता है। इसमें योजनाकार मॉड्यूल, रूटिंग तंत्र, या स्थितिजन्य फ्लो शामिल हो सकते हैं जो टूल उपयोग को गतिशील रूप से निर्धारित करते हैं।

- **मैसेज हैंडलिंग सिस्टम**: उपयोगकर्ता इनपुट, LLM प्रतिक्रियाएं, टूल कॉल्स, और टूल आउटपुट के बीच संवाद प्रवाह का प्रबंधन करने वाले घटक।

- **टूल इंटीग्रेशन फ्रेमवर्क**: एजेंट को विभिन्न टूल्स से जोड़ने वाला इंफ्रास्ट्रक्चर, चाहे वे सरल फ़ंक्शन हों या जटिल बाहरी सेवाएं।

- **एरर हैंडलिंग और सत्यापन**: टूल निष्पादन में विफलताओं को संभालने, पैरामीटरों को सत्यापित करने, और अप्रत्याशित प्रतिक्रियाओं को प्रबंधित करने के तंत्र।

- **राज्य प्रबंधन**: संवाद का संदर्भ, पिछले टूल इंटरैक्शंस, और स्थायी डेटा को ट्रैक करता है ताकि मल्टी-टर्न बातचीत में सुसंगतता बनी रहे।

अगला, आइए फ़ंक्शन/टूल कॉलिंग को अधिक विस्तार से देखें।

### फ़ंक्शन/टूल कॉलिंग

फ़ंक्शन कॉलिंग वह प्राथमिक तरीका है जिससे हम LLMs को टूल्स के साथ इंटरैक्ट करने में सक्षम बनाते हैं। अक्सर 'फ़ंक्शन' और 'टूल' शब्दों का पर्यायवाची रूप में उपयोग किया जाता है क्योंकि 'फ़ंक्शन्स' (पुनः उपयोग योग्य कोड ब्लॉक) वे 'टूल्स' होते हैं जिनका एजेंट कार्यों को करने के लिए उपयोग करते हैं। एक फ़ंक्शन के कोड को कॉल करने के लिए, LLM को उपयोगकर्ता के अनुरोध की तुलना फ़ंक्शन्स के विवरण से करनी होती है। इसके लिए, सभी उपलब्ध फ़ंक्शन्स के विवरणों वाला एक स्कीमा LLM को भेजा जाता है। फिर LLM उपयुक्त फ़ंक्शन का चयन करता है और उसके नाम और तर्क लौटाता है। चयनित फ़ंक्शन को कॉल किया जाता है, इसका उत्तर LLM को भेजा जाता है, जो फिर उपयोगकर्ता के अनुरोध का जवाब देने के लिए उस जानकारी का उपयोग करता है।

डेवलपर्स के लिए फ़ंक्शन कॉलिंग को लागू करने के लिए, आपको निम्नलिखित की आवश्यकता होगी:

1. एक LLM मॉडल जो फ़ंक्शन कॉलिंग का समर्थन करता हो
2. फ़ंक्शन विवरणों वाला एक स्कीमा
3. प्रत्येक वर्णित फ़ंक्शन के लिए कोड

चलो शहर में वर्तमान समय प्राप्त करने के उदाहरण का उपयोग करके समझते हैं:

1. **फ़ंक्शन कॉलिंग का समर्थन करने वाले LLM को इनिशियलाइज़ करें:**

    सभी मॉडल फ़ंक्शन कॉलिंग का समर्थन नहीं करते, इसलिए यह जांचना महत्वपूर्ण है कि आप जो LLM उपयोग कर रहे हैं वह यह करता है। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> फ़ंक्शन कॉलिंग का समर्थन करता है। हम Azure OpenAI क्लाइंट प्रारंभ करके शुरुआत कर सकते हैं।

    ```python
    # Azure OpenAI क्लाइंट को प्रारंभ करें
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **एक फ़ंक्शन स्कीमा बनाएँ**:

    अगला, हम JSON स्कीमा परिभाषित करेंगे जिसमें फ़ंक्शन का नाम, फ़ंक्शन क्या करता है इसका वर्णन, और फ़ंक्शन पैरामीटर के नाम व विवरण होंगे। फिर हम इस स्कीमा को पहले से बनाए गए क्लाइंट को उपयोगकर्ता के अनुरोध के साथ पास करेंगे, जिसमें सान फ्रांसिस्को में समय खोजने का अनुरोध होगा। महत्वपूर्ण यह है कि **टूल कॉल** लौटाया जाता है, प्रश्न का अंतिम उत्तर नहीं। जैसा पहले बताया गया, LLM उस फ़ंक्शन का नाम लौटाता है जिसे उसने कार्य के लिए चुना है, और उसे पास किए जाने वाले तर्क।

    ```python
    # मॉडल के पढ़ने के लिए फ़ंक्शन विवरण
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
  
    # पहला एपीआई कॉल: मॉडल से फंक्शन का उपयोग करने को कहें
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
  
1. **कार्य को पूरा करने के लिए आवश्यक फ़ंक्शन कोड:**

    अब जब LLM ने चुना कि कौन सा फ़ंक्शन चलाना है तो उस कार्य को पूरा करने वाला कोड लिखकर निष्पादित किया जाना चाहिए।  
    हम पायथन में वर्तमान समय प्राप्त करने वाला कोड लिख सकते हैं। हमें फ़ाइनल परिणाम पाने के लिए response_message से फ़ंक्शन का नाम और तर्क निकालने वाला कोड भी लिखना होगा।

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

फ़ंक्शन कॉलिंग अधिकांश, यदि सभी नहीं, एजेंट टूल उपयोग डिज़ाइन का मूल है, फिर भी इसे स्क्रैच से लागू करना कभी-कभी चुनौतीपूर्ण हो सकता है। जैसा कि हमने [पाठ 2](../../../02-explore-agentic-frameworks) में सीखा, एजेंटिक फ्रेमवर्क हमें टूल उपयोग को लागू करने के लिए पहले से बने निर्माण खंड प्रदान करते हैं।

## एजेंटिक फ्रेमवर्क्स के साथ टूल उपयोग उदाहरण

यहाँ कुछ उदाहरण हैं कि कैसे आप विभिन्न एजेंटिक फ्रेमवर्क्स का उपयोग करके टूल उपयोग डिज़ाइन पैटर्न को लागू कर सकते हैं:

### सेमैटिक कर्नेल

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">सेमैटिक कर्नेल</a> .NET, Python, और Java डेवलपर्स के लिए एक ओपन-सोर्स AI फ्रेमवर्क है जो LLMs के साथ काम करता है। यह फ़ंक्शन कॉलिंग की प्रक्रिया को सरल बनाता है, अपने फ़ंक्शन्स और उनके पैरामीटरों का मॉडल के लिए कस्टमैटिक वर्णन करके, जिसे <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">सीरियलाइज़िंग</a> कहा जाता है। यह मॉडल और आपके कोड के बीच आने-जाने वाले संवाद को भी संभालता है। सेमैटिक कर्नेल जैसे एजेंटिक फ्रेमवर्क का एक और लाभ यह है कि आप इसके पहले से बने टूल जैसे <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> और <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a> का उपयोग कर सकते हैं।

निम्न आरेख सेमैटिक कर्नेल के साथ फ़ंक्शन कॉलिंग की प्रक्रिया को दर्शाता है:

![function calling](../../../translated_images/hi/functioncalling-diagram.a84006fc287f6014.webp)

सेमैटिक कर्नेल में फ़ंक्शन्स/टूल्स को <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">प्लगइन्स</a> कहा जाता है। हम पहले देखी गई `get_current_time` फ़ंक्शन को एक क्लास में बदलकर एक प्लगइन बना सकते हैं जिसमें वह फ़ंक्शन होता है। हम `kernel_function` डेकोरेटर भी इम्पोर्ट कर सकते हैं, जो फ़ंक्शन के विवरण को लेता है। जब आप GetCurrentTimePlugin के साथ कर्नेल बनाएंगे, तो कर्नेल स्वचालित रूप से फ़ंक्शन और उसके पैरामीटर को सीरियलाइज़ करेगा, जिससे स्कीमा बनेगा जिसे मॉडल को भेजा जाएगा।

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

# कर्नेल बनाएं
kernel = Kernel()

# प्लगइन बनाएं
get_current_time_plugin = GetCurrentTimePlugin(location)

# प्लगइन को कर्नेल में जोड़ें
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> एक नवीन एजेंटिक फ्रेमवर्क है जो डेवलपर्स को सुरक्षित रूप से उच्च गुणवत्ता, और विस्तार योग्य AI एजेंट बनाने, तैनात करने, और स्केल करने के लिए सक्षम बनाता है बिना अंतर्निहित कंप्यूट और स्टोरेज संसाधनों को प्रबंधित किए। यह विशेष रूप से एंटरप्राइज़ अनुप्रयोगों के लिए उपयोगी है क्योंकि यह एक पूरी तरह से प्रबंधित सेवा है जिसमें एंटरप्राइज़ ग्रेड सुरक्षा शामिल है।

सीधा LLM API के साथ विकास के मुकाबले, Azure AI Agent Service कुछ लाभ प्रदान करता है, जिनमें शामिल हैं:

- स्वचालित टूल कॉलिंग – टूल कॉल को पार्स करने, टूल को लॉन्च करने, और प्रतिक्रिया को संभालने की आवश्यकता नहीं; यह सब अब सर्वर साइड पर होता है
- सुरक्षित रूप से प्रबंधित डेटा – अपनी स्वयं की संवाद स्थिति प्रबंधित करने के बजाय, आप थ्रेड्स पर भरोसा कर सकते हैं जो आवश्यक सभी जानकारी संग्रहीत करते हैं
- आउट-ऑफ-द-बॉक्स टूल्स – टूल्स जिनका उपयोग आप अपने डेटा स्रोतों के साथ इंटरैक्ट करने के लिए कर सकते हैं, जैसे Bing, Azure AI Search, और Azure Functions।

Azure AI Agent Service में उपलब्ध टूल्स को दो श्रेणियों में विभाजित किया जा सकता है:

1. ज्ञान टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search के साथ ग्राउंडिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. एक्शन टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित टूल्स</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service हमें इन टूल्स को `toolset` के रूप में एक साथ उपयोग करने की अनुमति देता है। यह `threads` का उपयोग करता है, जो किसी विशिष्ट बातचीत के संदेशों का इतिहास रखता है।

कल्पना करें कि आप Contoso नामक कंपनी में एक सेल्स एजेंट हैं। आप एक संवादात्मक एजेंट विकसित करना चाहते हैं जो आपकी बिक्री डेटा के बारे में प्रश्नों का उत्तर दे सके।

निम्न छवि दिखाती है कि आप Azure AI Agent Service का उपयोग करके अपनी बिक्री डेटा का विश्लेषण कैसे कर सकते हैं:

![Agentic Service In Action](../../../translated_images/hi/agent-service-in-action.34fb465c9a84659e.webp)

सेवा के साथ इनमें से किसी भी टूल का उपयोग करने के लिए हम एक क्लाइंट बना सकते हैं और एक टूल या टूलसेट को परिभाषित कर सकते हैं। इसे व्यावहारिक रूप से लागू करने के लिए हम निम्नलिखित पायथन कोड का उपयोग कर सकते हैं। LLM टूलसेट को देख सकेगा और उपयोगकर्ता अनुरोध के आधार पर या तो उपयोगकर्ता द्वारा बनाई गई फ़ंक्शन `fetch_sales_data_using_sqlite_query` का उपयोग करेगा या पूर्व-निर्मित Code Interpreter का।

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

# फ़ंक्शन कॉलिंग एजेंट को fetch_sales_data_using_sqlite_query फ़ंक्शन के साथ प्रारंभ करें और इसे टूलसेट में जोड़ें
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# कोड इंटरप्रेटर टूल प्रारंभ करें और इसे टूलसेट में जोड़ें।
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## विश्वसनीय AI एजेंट बनाने के लिए टूल उपयोग डिज़ाइन पैटर्न का उपयोग करते समय विशेष विचार क्या हैं?

LLMs द्वारा गतिशील रूप से जेनरेट किए गए SQL के साथ एक सामान्य चिंता सुरक्षा है, विशेष रूप से SQL इंजेक्शन या दुर्भावनापूर्ण क्रियाओं जैसे डेटाबेस को ड्रॉप या छेड़छाड़ करने का जोखिम। जबकि ये चिंताएँ वैध हैं, उन्हें डेटाबेस एक्सेस अनुमतियों को सही तरीके से कॉन्फ़िगर करके प्रभावी रूप से कम किया जा सकता है। अधिकांश डेटाबेस के लिए इसका मतलब है डेटाबेस को केवल पढ़ने (read-only) के रूप में कॉन्फ़िगर करना। PostgreSQL या Azure SQL जैसी डेटाबेस सेवाओं के लिए, ऐप को केवल पढ़ने वाले (SELECT) भूमिका असाइन की जानी चाहिए।
एक सुरक्षित वातावरण में ऐप चलाना सुरक्षा को और भी बढ़ाता है। एंटरप्राइज परिप्रेक्ष्य में, डेटा आमतौर पर परिचालन प्रणालियों से निकाला और रूपांतरित किया जाता है ताकि इसे एक रीड-ओनली डेटाबेस या डेटा वेयरहाउस में स्थानांतरित किया जा सके जिसमें उपयोगकर्ता के अनुकूल स्कीमा होता है। यह दृष्टिकोण सुनिश्चित करता है कि डेटा सुरक्षित है, प्रदर्शन और पहुंच के लिए अनुकूलित है, और ऐप की अनुमति सीमित, रीड-ओनली एक्सेस है।

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
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम शुद्धता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उपजने वाली किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं होंगे।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->