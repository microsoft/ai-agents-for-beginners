[![छान AI एजंट्स कसे डिझाइन करायचे](../../../translated_images/mr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(या धड्याचा व्हिडिओ पाहण्यासाठी वरील प्रतिमा क्लिक करा)_

# टूल युज डिझाइन पॅटर्न

टूल्स रंजक आहेत कारण ते AI एजंट्सना अधिक व्यापक क्षमता देतात. एजंटकडे जर फक्त काही अंमलबजावणी करण्याच्या मर्यादित क्रियांचा संच असेल, तर टूल जोडल्याने ती एजंट आता विस्तृत प्रमाणात क्रियाकलाप करू शकतो. या प्रकरणात आपण टूल युज डिझाइन पॅटर्न पाहणार आहोत, जे सांगते की AI एजंट्स कसे विशिष्ट साधने वापरून त्यांच्या उद्दिष्टांपर्यंत पोहोचू शकतात.

## परिचय

या धड्यात आपण खालील प्रश्नांची उत्तरे शोधणार आहोत:

- टूल युज डिझाइन पॅटर्न म्हणजे काय?
- कोणत्या वापराच्या प्रकरणांमध्ये ते लागू करता येऊ शकते?
- डिझाइन पॅटर्न लागू करण्यासाठी कोणत्या घटक/बिल्डिंग ब्लॉक्सची आवश्यकता आहे?
- विश्वासार्ह AI एजंट तयार करण्यासाठी टूल युज डिझाइन पॅटर्न वापरताना कोणत्या विशेष बाबी लक्षात ठेवाव्यात?

## शिकण्याचे उद्दिष्टे

हा धडा पूर्ण केल्यावर, आपण सक्षम असाल:

- टूल युज डिझाइन पॅटर्न आणि त्याचा हेतू परिभाषित करण्यासाठी.
- ज्या वापराच्या प्रकरणांमध्ये टूल युज डिझाइन पॅटर्न लागू आहे ती ओळखण्यासाठी.
- डिझाइन पॅटर्न अंमलात आणण्यासाठी आवश्यक मुख्य घटक समजण्यासाठी.
- हा डिझाइन पॅटर्न वापरून AI एजंटमध्ये विश्वासार्हता सुनिश्चित करण्यासाठी विचार करण्याच्या बाबी ओळखण्यासाठी.

## टूल युज डिझाइन पॅटर्न म्हणजे काय?

**टूल युज डिझाइन पॅटर्न** LLMs ला विशिष्ट उद्दिष्ट साध्य करण्यासाठी बाह्य साधनांशी संवाद साधण्याची क्षमता देते. टूल म्हणजे कोड जो एजंटद्वारे क्रिया करण्यासाठी चालवता येतो. टूल एक साधा कार्य (फंक्शन) असू शकतो जसे कॅल्क्युलेटर, किंवा तृतीय पक्ष सेवा जसे स्टॉक किंमती तपासणे किंवा हवामानाचा अंदाज घेण्यासाठी API कॉल. AI एजंट्सच्या संदर्भात, टूल्स हे **मॉडेल-जनरेट केलेल्या फंक्शन कॉल्स** च्या प्रतिसादादाखल एजंटद्वारे चालविण्यासाठी डिझाइन केलेले आहेत.

## कोणत्या वापराच्या प्रकरणांमध्ये ते लागू करता येते?

AI एजंट्स बहु-प्रकारच्या कामांसाठी, माहिती घेण्यासाठी, किंवा निर्णय घेण्यासाठी टूल्सचा वापर करू शकतात. टूल युज डिझाइन पॅटर्न विशेषत: अशा परिदृश्यांमध्ये वापरला जातो जेथे बाह्य प्रणालींसह गतिशील संवाद आवश्यक असतो, जसे डेटाबेस, वेब सेवा, किंवा कोड व्याख्याकार. ही क्षमता खालील विविध वापराच्या बाबतीत उपयुक्त आहे:

- **गतिशील माहिती प्राप्ती:** एजंट्स बाह्य API किंवा डेटाबेसमधून सतत अद्ययावत डेटा विचारू शकतात (उदा. SQLite डेटाबेसमधून डेटा विश्लेषणासाठी विचारणा करणे, स्टॉक किंमती किंवा हवामान माहिती घेणे).
- **कोडच्या अंमलबजावणी आणि व्याख्या:** गणितीय समस्या सोडविण्यासाठी, अहवाल तयार करण्यासाठी, किंवा सिम्युलेशन्स करण्यासाठी कोड/स्क्रिप्ट चालवू शकतात.
- **कार्यप्रवाह स्वयंचलन:** कामांचे पुन्हा पुन्हा होणारे किंवा बहु-टप्प्यांचे कार्यप्रवाह ऑटोमेट करण्यासाठी टास्क शेड्युलर, ईमेल सेवा, किंवा डेटा पाईपलाइन्स यासारखी टूल्स समाकलित करणे.
- **ग्राहक समर्थन:** एजंट्स CRM प्रणाली, तिकीट प्रणाली, किंवा ज्ञानाधारांशी संवाद साधून वापरकर्त्यांच्या प्रश्नांची सोडवणूक करू शकतात.
- **सामग्री निर्मिती आणि संपादन:** एजंट्स व्याकरण तपासणी, मजकूर सारांश, किंवा सामग्री सुरक्षितता मूल्यमापन करणाऱ्या टूल्सचा वापर करून सामग्री तयार करण्यास मदत करू शकतात.

## टूल युज डिझाइन पॅटर्न लागू करण्यासाठी कोणते घटक/बिल्डिंग ब्लॉक्स आवश्यक आहेत?

हे बिल्डिंग ब्लॉक्स AI एजंटला विस्तृत काम करण्यास सक्षम करतात. टूल युज डिझाइन पॅटर्न अंमलात आणण्यासाठी आवश्यक मुख्य घटक खालीलप्रमाणे आहेत:

- **फंक्शन/टूल स्कीमा:** उपलब्ध टूल्सची सविस्तर व्याख्या, ज्यात फंक्शनचे नाव, हेतू, आवश्यक पॅरामीटर्स, आणि अपेक्षित आउटपुट्स यांचा समावेश असतो. हे स्कीमा LLM ला टूल्सची उपलब्धता आणि वैध विनंत्या कशा तयार कराव्यात हे समजावून देतात.

- **फंक्शन अंमलबजावणी लॉजिक:** वापरकर्त्याच्या हेतू आणि संभाषणाच्या संदर्भावर आधारित टूल कधी आणि कसे वापरायचे हे नियंत्रित करते. यात नियोजक मॉड्यूल, रूटिंग यंत्रणा, किंवा परिस्थितीनुरूप प्रवाह असू शकतात जे टूलच्या वापरावर गतिशीलपणे निर्णय घेतात.

- **संदेश व्यवस्थापन प्रणाली:** वापरकर्त्याच्या इनपुट्स, LLM प्रतिसाद, टूल कॉल्स, आणि टूल आउटपुट्स यामधील संभाषण प्रवाह व्यवस्थापित करणारे घटक.

- **टूल इंटिग्रेशन फ्रेमवर्क:** एजंटला विविध टूल्सशी जोडणारे पायाभूत सुविधा, ज्या सोपे फंक्शन्स असू शकतात किंवा जटिल बाह्य सेवा असू शकतात.

- **त्रुटी हाताळणी व प्रमाणीकरण:** टूल अंमलबजावणीत अपयश हाताळणे, पॅरामीटर्सची प्रमाणीकरण करणे, आणि अनपेक्षित प्रतिसादांची व्यवस्थापन करण्यासाठी यंत्रणा.

- **स्थिती व्यवस्थापन:** संभाषणाचा संदर्भ, मागील टूल संवाद, आणि सातत्य राखण्यासाठी टिकाऊ डेटा ट्रॅक करण्यासाठी.

आता चला फंक्शन/टूल कॉलिंग अधिक तपशीलवार पाहू.

### फंक्शन/टूल कॉलिंग

फंक्शन कॉलिंग हे मुख्य माध्यम आहे ज्याद्वारे Large Language Models (LLMs) टूल्सशी संवाद साधतात. तुम्हाला 'फंक्शन' आणि 'टूल' हा दोन शब्द बाजूने वापरले जातील कारण 'फंक्शन्स' (पुन्हा वापरता येणाऱ्या कोडचे ब्लॉक्स) हे 'टूल्स' आहेत जे एजंट्स त्यांच्या कामासाठी वापरतात. जेणेकरून फंक्शनचा कोड चालवला जाईल, LLM ला वापरकर्त्याच्या विनंतीचे तुलनात्मक दरम्यान फंक्शनचे वर्णन तपासावे लागते. त्यामुळे उपलब्ध सर्व फंक्शन्सच्या वर्णन असलेले स्कीमा LLM कडे पाठवले जाते. LLM मग त्या कामासाठी सर्वात योग्य फंक्शन निवडतो आणि त्याचे नाव आणि पॅरामीटर्स परत पाठवतो. निवडलेले फंक्शन कॉल केले जाते, त्याचा प्रतिसाद LLM कडे परत पाठवला जातो, जे वापरकर्त्याच्या विनंतीला प्रतिसाद देण्यासाठी तो माहिती वापरते.

डेव्हलपर्सना एजंटसाठी फंक्शन कॉलिंग लागू करायचे असल्यास, खाली लागेल:

1. फंक्शन कॉलिंग समर्थन करणारे LLM मॉडेल
2. फंक्शन वर्णन असलेले स्कीमा
3. प्रत्येक फंक्शनसाठी कोड

चला, एका शहरातील सध्याच्या वेळेचा तपासण्यासाठी उदाहरण म्हणुन पहा:

1. **फंक्शन कॉलिंगसाठी समर्थन करणारे LLM मॉडेल सुरु करा:**

    सर्व मॉडेल्स फंक्शन कॉलिंगसाठी समर्थन करत नाहीत, त्यामुळे वापरत असलेल्या LLM मध्ये ते आहे की नाही हे तपासणे महत्वाचे आहे. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> फंक्शन कॉलिंगसाठी समर्थन देतो. आपण Azure OpenAI क्लायंट सुरू करण्यापासून प्रारंभ करू शकतो.

    ```python
    # Azure OpenAI क्लायंट सुरू करा
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **फंक्शन स्कीमा तयार करा:**

    पुढे आपण JSON स्कीमा तयार करू ज्यात फंक्शनचे नाव, फंक्शन काय करते याचे वर्णन, आणि फंक्शन पॅरामीटर्सची नावे व त्यांचे वर्णन असेल.
    हे स्कीमा आणि वापरकर्त्याची विनंती क्लायंटला दिल्या जातील जे आधी तयार केले होते, उदाहरणार्थ San Francisco मधील वेळ मिळवण्याच्या साठी. महत्वाचं म्हणजे, परत मिळणं म्हणजे **टूल कॉल** आहे, **प्रश्नाचे अंतिम उत्तर नाही**. जसे आधी सांगितले, LLM निवडलेल्या फंक्शनचे नाव आणि त्याला दिले जाणारे अर्ग्युमेंट्स परत पाठवतो.

    ```python
    # मॉडेल वाचण्यासाठी फंक्शनचे वर्णन
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
  
    # प्रारंभिक वापरकर्त्याचा संदेश
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # प्रथम API कॉल: मॉडेलला फंक्शन वापरण्यास विचारा
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # मॉडेलच्या प्रतिसादाची प्रक्रिया करा
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **काम करण्यासाठी आवश्यक असलेला फंक्शन कोड:**

    आता LLM ने कोणता फंक्शन चालवायचा तो निवडल्यावर, तो कार्य करणारा कोड अंमलबजावनीसाठी तयार करणे व चालवणे आवश्यक आहे.
    आपण Python मध्ये वर्तमान वेळ मिळविण्यासाठी कोड लिहू. तसेच, response_message मधून नाव व अर्ग्युमेंट्स काढण्याचा कोड देखील लिहायला हवा.

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
     # फंक्शन कॉल हाताळा
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
  
      # दुसरा API कॉल: मॉडेलकडून अंतिम प्रतिसाद मिळवा
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

फंक्शन कॉलिंग ही बहुतांश, सर्व नाही तरी, एजंट टूल युज डिझाइनचा केंद्रस्थानी असते, पण ते कधी कधी सुरुवातीपासून अंमलबजावणी करणे आव्हानात्मक असू शकते.
जसे आपण [Lesson 2](../../../02-explore-agentic-frameworks) मध्ये जाणले, एजंटिक फ्रेमवर्क्स आम्हाला टूल युजसाठी पूर्वनिर्मित बिल्डिंग ब्लॉक्स उपलब्ध करून देतात.

## एजंटिक फ्रेमवर्क्ससह टूल युज उदाहरणे

टूल युज डिझाइन पॅटर्न कसे विविध एजंटिक फ्रेमवर्क वापरून अंमलात आणता येते याची काही उदाहरणे येथे दिली आहेत:

### सेमॅंटिक कर्नेल

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">सेमॅंटिक कर्नेल</a> हा .NET, Python, आणि Java विकसकांसाठी एक मुक्त स्रोत AI फ्रेमवर्क आहे जे LLMs सह काम करते. तो फंक्शन कॉलिंग वापरणे सुलभ करतो कारण तो आपली फंक्शन्स व त्यांच्या पॅरामीटर्सना मॉडेलकडे वर्णन करणाऱ्या प्रक्रियेला <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">सीरियलायझिंग</a> म्हणतात, तसेच मॉडेल आणि कोडमधील संवाद नियंत्रित करतो. सेमॅंटिक कर्नेलसारखा एजंटिक फ्रेमवर्क वापरण्याचा आणखी फायदा म्हणजे यामध्ये आपल्याला पूर्व-निर्मित टूल्स जसे <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> आणि <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a> वापरता येतात.

खालील आकृती सेमॅंटिक कर्नेलसह फंक्शन कॉलिंग प्रक्रियेला दर्शविते:

![function calling](../../../translated_images/mr/functioncalling-diagram.a84006fc287f6014.webp)

सेमॅंटिक कर्नेलमध्ये फंक्शन/टूल्सना <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">प्लगइन्स</a> म्हणतात. आपण `get_current_time` फंक्शन प्लगइनमध्ये रूपांतर करू शकतो, ज्यामध्ये तो फंक्शन असलेला एक वर्ग (class) बनवू शकतो. `kernel_function` डिकॉरटर देखील आपण आयात करू शकतो, जो फंक्शनचे वर्णन घेते. जेव्हा आपण GetCurrentTimePlugin सह कर्नेल तयार करता, तेव्हा कर्नेल आपोआप फंक्शन आणि त्याचे पॅरामीटर्स सीरियलाइज करून स्कीमा तयार करतो आणि LLM कडे पाठवतो.

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

# कर्नल तयार करा
kernel = Kernel()

# प्लगइन तयार करा
get_current_time_plugin = GetCurrentTimePlugin(location)

# प्लगइन कर्नलमध्ये जोडा
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> हा एक नवा एजंटिक फ्रेमवर्क आहे जो विकासकांना सुरक्षितरीत्या उच्च-गुणवत्तेचे आणि विस्तारक्षम AI एजंट तयार करणे, तैनात करणे, आणि स्केल करण्यास सक्षम करतो, त्याच वेळी खालीलच्या संगणकीय आणि संचयन संसाधनांचे व्यवस्थापन करावे लागत नाही. हा विशेषतः एंटरप्राइझ अनुप्रयोगांसाठी उपयुक्त आहे कारण तो पूर्णपणे व्यवस्थापित सेवा आहे ज्यामध्ये एंटरप्राइझ-स्तरीय सुरक्षा आहे.

LLM API थेट वापरून विकसित करण्याच्या तुलनेत, Azure AI Agent Service काही फायदे देते जसे:

- स्वयंचलित टूल कॉलिंग – टूल कॉल पार्स करण्याची, टूल चालवण्याची, आणि प्रतिसाद हाताळण्याची गरज नाही; हे सर्व आता सर्व्हर साईडवर होते.
- सुरक्षितरीत्या व्यवस्थापित डेटा – आपला स्वतःचा संभाषणाचा स्थिती व्यवस्थापित करण्याऐवजी, आपण थ्रेड्सवर पूर्ण माहिती साठवू शकता.
- रेडीमेड टूल्स – वापरले जाणारे टूल्स ज्याद्वारे तुम्ही तुमच्या डेटा स्त्रोतांशी जसे Bing, Azure AI Search, आणि Azure Functions यांच्यासह संवाद साधू शकता.

Azure AI Agent Service मध्ये उपलब्ध टूल्स दोन श्रेणींमध्ये विभागले आहेत:

1. ज्ञान टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search सह ग्राउंडिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. अ‍ॅक्शन टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित टूल्स</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service आम्हाला हे टूल्स एकत्र `toolset` म्हणून वापरण्याची परवानगी देतो. हे `threads` देखील वापरतो जे एका विशिष्ट संभाषणाबाबत इतिहास ट्रॅक करतात.

कल्पना करा की तुम्ही कॉन्टोसो नावाच्या कंपनीत विक्री एजंट आहात. तुम्हाला असा संभाषण एजंट तयार करायचा आहे जो तुमच्या विक्री डेटाविषयी प्रश्नांची उत्तरे देऊ शकतो.

खालील प्रतिमा Azure AI Agent Service वापरून तुमच्या विक्री डेटाचा कसोटी कशी करता येईल हे दाखवते:

![Agentic Service In Action](../../../translated_images/mr/agent-service-in-action.34fb465c9a84659e.webp)

या सेवेतील कोणतेही टूल वापरण्यासाठी आपण क्लायंट तयार करू शकतो आणि टूल किंवा टूलसेट परिभाषित करू शकतो. प्रत्यक्षात यासाठी खालील Python कोड वापरू शकतो. LLM टूलसेट पाहून वापरकर्त्याने तयार केलेले फंक्शन `fetch_sales_data_using_sqlite_query` वापरायचे की पूर्वनिर्मित Code Interpreter वापरायचा हे वापरकर्त्याच्या विनंतीनुसार ठरवेल.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query फंक्शन जे fetch_sales_data_functions.py फाईलमध्ये सापडू शकते.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# टूलसेट सुरू करा
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query फंक्शनसह फंक्शन कॉलिंग एजंट सुरू करा आणि ते टूलसेटमध्ये जोडा
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# कोड इंटरप्रिटर टूल सुरू करा आणि ते टूलसेटमध्ये जोडा.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## विश्वासार्ह AI एजंट तयार करण्यासाठी टूल युज डिझाइन पॅटर्नच्या वापरासाठी विशेष बाबी कोणत्या?

LLM द्वारे डायनॅमिकली तयार होणाऱ्या SQL बाबत एक सामान्य चिंता म्हणजे सुरक्षा, विशेषतः SQL इंजेक्शनचा धोका किंवा खाल्ल्याच्या डेटाबेसमध्ये हल्ला करणारे कृत्ये जसे डेटाबेस ड्रॉप करणे किंवा त्यात फेरफार करणे. जरी या चिंता योग्य असल्या तरी, त्या योग्य रीतीने डेटाबेस प्रवेश परवानग्या संरचीत करून परिणामकारकपणे टाळता येऊ शकतात. बहुतेक डेटाबेससाठी हे रीड-ओनली मोडमध्ये डेटाबेस संरचीत करण्याचा समावेश आहे. PostgreSQL किंवा Azure SQL सारख्या डेटाबेस सेवांसाठी, अ‍ॅपला रीड-ओनली (SELECT) रोल दिला जावा.
अॅपला सुरक्षित वातावरणात चालवणे संरक्षण आणखी वाढवते. एंटरप्राइझ परिस्थितीत, डेटा बहुतेक वेळा ऑपरेशनल सिस्टम्समधून वाचण्यासाठी फक्त उपलब्ध असलेल्या डेटाबेस किंवा डेटा वेअरहाऊसबद्दल वापरकर्ता-अनुकूल स्कीमासह रूपांतरित केला जातो. हा दृष्टिकोन डेटा सुरक्षित ठेवतो, कामगिरी आणि प्रवेशयोग्यता यासाठी ऑप्टिमाइझ करतो, आणि अॅपला मर्यादित, फक्त वाचण्याच्या प्रवेश परवानगी देतो.

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
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा विसंगती असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्वाच्या माहितीच्या बाबतीत व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थ लावणीबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->