[![How to Design Good AI Agents](../../../translated_images/mr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(या धड्यातील व्हिडिओ पाहण्यासाठी वरच्या प्रतिमेवर क्लिक करा)_

# टूल वापर डिझाइन पॅटर्न

टूल्स मनोरंजक आहेत कारण ते AI एजंटना अधिक विस्तृत क्षमता देतात. ज्यामुळे एजंटकडे एक सीमित क्रियांची यादी असण्याऐवजी, टूल जोडल्याने एजंट आता विविध प्रकारच्या क्रिया करू शकतो. या अध्यायात आपण टूल वापर डिझाइन पॅटर्न पाहणार आहोत, ज्यात AI एजंट कसाही विशिष्ट टूल्स वापरून त्यांचे उद्दिष्ट साध्य करू शकतात याचे वर्णन केले आहे.

## परिचय

या धड्यात आम्ही खालील प्रश्नांची उत्तर शोधणार आहोत:

- टूल वापर डिझाइन पॅटर्न म्हणजे काय?
- कोणत्या वापराच्या बाबतीत हे लागू शकते?
- डिझाइन पॅटर्न अंमलात आणण्यासाठी कोणते घटक/घटक आवश्यक आहेत?
- विश्वासार्ह AI एजंट तयार करण्यासाठी टूल वापर डिझाइन पॅटर्न वापरताना कोणते विशेष विचार करणे आवश्यक आहे?

## शिक्षण उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, तुम्ही खालील गोष्टी करू शकाल:

- टूल वापर डिझाइन पॅटर्न आणि त्याचा उद्देश परिभाषित करा.
- ज्या वापराच्या प्रकरणांमध्ये टूल वापर डिझाइन पॅटर्न लागू होतो ते ओळखा.
- डिझाइन पॅटर्न अंमलात आणण्यासाठी आवश्यक प्रमुख घटक समजून घ्या.
- या डिझाइन पॅटर्नचा वापर करणाऱ्या AI एजंटसाठी विश्वासार्हता सुनिश्चित करण्यासाठी आवश्यक विचार ओळखा.

## टूल वापर डिझाइन पॅटर्न म्हणजे काय?

**टूल वापर डिझाइन पॅटर्न** LLMs ना विशिष्ट उद्दिष्टे साध्य करण्यासाठी बाहेरील टूल्सशी संवाद साधण्याची क्षमता देण्यावर लक्ष केंद्रित करतो. टूल्स म्हणजे असे कोड जे एजंटने क्रिया करण्यासाठी चालवू शकतात. टूल एखादा सोपा फंक्शन जसे की कॅल्क्युलेटर किंवा तृतीय-पक्ष सेवा जसे की स्टॉक प्राइस शोध किंवा हवामान अंदाजासाठी API कॉल असू शकतो. AI एजंटच्या संदर्भात, टूल्स हे **मॉडेल-निर्मित फंक्शन कॉल्स** प्रतिसाद म्हणून एजंटकडून चालविण्यासाठी डिझाइन केल्या जातात.

## यात कोणत्या वापराच्या बाबतीत हे लागू होऊ शकते?

AI एजंट्स गुंतागुंतीची कामे पूर्ण करण्यासाठी, माहिती मिळवण्यासाठी किंवा निर्णय घेण्यासाठी टूल्सचा वापर करू शकतात. टूल वापर डिझाइन पॅटर्न सहसा अशा परिस्थितीत वापरला जातो जिथे बाह्य प्रणालींसोबत डायनॅमिक संवाद आवश्यक असतो, जसे डेटाबेस, वेब सेवा किंवा कोड व्याख्यात्यांसह. ही क्षमता अनेक वेगवेगळ्या वापरांच्या बाबतीत उपयुक्त आहे, जसे की:

- **डायनॅमिक माहिती मिळवणे:** एजंट्स बाह्य API किंवा डेटाबेसमधून अद्ययावत डेटा आणू शकतात (उदा. SQLite डेटाबेसमध्ये डेटा अ‍ॅनालिसिससाठी क्वेरी करणे, स्टॉक किंमती किंवा हवामान माहिती मिळवणे).
- **कोड अंमलबजावणी आणि व्याख्या:** एजंट कोड किंवा स्क्रिप्ट्स चालवून गणितीय समस्या सोडवू शकतात, अहवाल तयार करू शकतात किंवा सिम्युलेशन्स करू शकतात.
- **वर्कफ्लो ऑटोमेशन:** टास्क शेड्यूलर, ईमेल सेवा किंवा डेटा पाईपलाइन्ससारख्या टूल्सचा वापर करून पुनरावृत्ती कामे किंवा बहु-स्टेप वर्कफ्लो ऑटोमेट करा.
- **ग्राहक समर्थन:** एजंट वापरकर्त्याच्या प्रश्नांचे निराकरण करण्यासाठी CRM सिस्टीम्स, तिकीटिंग प्लॅटफॉर्म्स किंवा ज्ञान भांडारांशी संवाद साधू शकतात.
- **सामग्री निर्मिती आणि संपादन:** ग्रामर चेकर्स, मजकूर सारांशक किंवा सामग्री सुरक्षा मूल्यमापकांसारख्या टूल्सचा वापर करून सामग्री निर्मिती कार्यात मदत करू शकतात.

## टूल वापर डिझाइन पॅटर्न अंमलात आणण्यासाठी कोणते घटक/तिकीट आवश्यक आहेत?

हे घटक AI एजंटला विविध प्रकारची कामे करण्यास सक्षम करतात. टूल वापर डिझाइन पॅटर्न अंमलात आणण्यासाठी आवश्यक प्रमुख घटक पाहूया:

- **फंक्शन/टूल स्कीमा**: उपलब्ध टूल्सचे सविस्तर वर्णन जसे की फंक्शनचे नाव, उद्देश, आवश्यक पॅरामीटर्स आणि अपेक्षित आउटपुट. हे स्कीमा LLM ला कळते की कोणती टूल्स उपलब्ध आहेत आणि वैध विनंत्या कशी तयार करायची.
  
- **फंक्शन अंमलबजावणी लॉजिक**: वापरकर्त्याच्या हेतू आणि संवाद संदर्भावर आधारित टूल्स कधी आणि कसे वापरायची याचे नियमन करते. ह्यांत प्लानर मॉड्यूल्स, रूटिंग मेकॅनिझम्स किंवा स्थितीनुसार निर्णय घेणारे प्रवाह असू शकतात.
  
- **मेसेज हँडलिंग सिस्टीम**: वापरकर्ता इनपुट, LLM प्रतिसाद, टूल कॉल्स आणि टूल आउटपुटमधील संभाषण प्रवाह सांभाळणारे घटक.
  
- **टूल इंटिग्रेशन फ्रेमवर्क**: एजंटला विविध टूल्सशी कनेक्ट करणारं यंत्रणा, ज्या टूल्स सोपे फंक्शन्स असोत किंवा जटिल बाह्य सेवां.
  
- **त्रुटी हाताळणी आणि प्रमाणीकरण**: टूल अंमलबजावणीत अपयश हाताळणे, पॅरामीटर्सची पडताळणी करणे आणि अनपेक्षित प्रतिसाद व्यवस्थापनासाठी यंत्रणा.
  
- **स्थिती व्यवस्थापन**: संवाद संदर्भ, आधीच्या टूल वापर, आणि सततचा डेटा ट्रॅक करणे ज्यामुळे बहु-वार संभाषणांमध्ये सुसंगतता राखली जाते.

आता, फंक्शन/टूल कॉलिंगचा अधिक तपशीलवार आढावा घेऊया.

### फंक्शन/टूल कॉलिंग

फंक्शन कॉलिंग हाच मुख्य मार्ग आहे ज्याद्वारे आम्ही मोठ्या भाषा मॉडेल्सना (LLMs) टूल्सशी संवाद साधण्यास सक्षम करतो. तुम्ही 'फंक्शन' आणि 'टूल' हे शब्द अनेकदा एकत्र वेगवेगळ्या संदर्भात वापरले जातात कारण 'फंक्शन' (पुनर्वापर करण्यायोग्य कोडचे ब्लॉक्स) हे 'टूल्स' असतात जे एजंट्स कामे करण्यासाठी वापरतात. एखाद्या फंक्शनचा कोड चालविण्यासाठी, LLM ला वापरकर्त्याच्या विनंतीची तुलना फंक्शनच्या वर्णनाशी करावी लागते. हे करण्यासाठी, सर्व उपलब्ध फंक्शन्सच्या वर्णनांसह स्कीमा LLM कडे पाठविली जाते. नंतर LLM त्या कामासाठी सर्वात योग्य फंक्शन निवडतो आणि त्याचे नाव व आर्ग्युमेंट परत करतो. निवडलेले फंक्शन कॉल केले जाते, त्याचा प्रतिसाद LLM ला परत पाठविला जातो, ज्याचा वापर करून वापरकर्त्याच्या विनंतीला प्रतिसाद दिला जातो.

डेव्हलपर्सना फंक्शन कॉलिंग अंमलात आणण्यासाठी आवश्यक असेल:

1. फंक्शन कॉलिंगला समर्थन करणारे LLM मॉडेल
2. फंक्शन वर्णन करणारे स्कीमा
3. प्रत्येक फंक्शनसाठी कोड

शहरातील वर्तमान वेळ मिळवण्याचा उदाहरण घेऊया:

1. **फंक्शन कॉलिंगला समर्थन करणारे LLM प्रारंभ करा:**

    सर्व मॉडेल फंक्शन कॉलिंगला समर्थन करत नाहीत, त्यामुळे जे LLM तुम्ही वापरत आहात ते तपासणे महत्त्वाचे आहे. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> फंक्शन कॉलिंगला समर्थन देते. आपण Azure OpenAI क्लायंट सुरू करू शकतो.

    ```python
    # Azure OpenAI ग्राहक प्रारंभ करा
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **फंक्शन स्कीमा तयार करा**:

    पुढे, आपण JSON स्कीमा परिभाषित करू जे फंक्शनचे नाव, फंक्शन काय करते याचे वर्णन, तसेच फंक्शन पॅरामीटर्सची नावे आणि वर्णन असते.
    नंतर हा स्कीमा मागील तयार क्लायंटला सोबत वापरकर्त्याची विनंती (उदा. San Francisco मधील वेळ शोधणे) पाठवू. लक्षात ठेवा की **टूल कॉल** परत येतो, **प्रश्नाचे अंतिम उत्तर नाही**. जसा पूर्वी नमूद केले तसे, LLM कामासाठी निवडलेले फंक्शनचे नाव आणि त्याचे आर्ग्युमेंट परत करते.

    ```python
    # वाचनासाठी मॉडेलसाठी फंक्शन वर्णन
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
  
    # प्रारंभिक वापरकर्ता संदेश
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # प्रथम API कॉल: मॉडेलला फंक्शन वापरायचे असं विचारा
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
  
1. **काम करण्यासाठी आवश्यक फंक्शन कोड:**

    LLM ने कोणता फंक्शन चालवायचा हे निवडल्यानंतर, त्या कामासाठी कोड अंमलात आणला पाहिजे.
    Python मध्ये सध्याची वेळ मिळवण्याचा कोड आम्ही लिहू शकतो. प्रतिसादातील नाम व आर्ग्युमेंट काढण्यासाठी कोड देखील तयार करणे आवश्यक आहे.

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
     # फंक्शन कॉल्स हाताळा
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

फंक्शन कॉलिंग हा बहुतांश एजंट टूल वापर डिझाइनचा केंद्रबिंदू आहे, परंतु ते सुरुवातीपासूनच अंमलात आणणे कधी कधी आव्हानात्मक असू शकते.
जसे आपण [धडा 2](../../../02-explore-agentic-frameworks) मध्ये शिकलो आहोत की एजंटिक फ्रेमवर्क्स आम्हाला टूल वापर अंमलात आणण्यासाठी पूर्वनिर्मित घटक देतात.

## एजंटिक फ्रेमवर्क्ससह टूल वापराची उदाहरणे

निम्नलिखित एजंटिक फ्रेमवर्क्सचा वापर करून तुम्ही टूल वापर डिझाइन पॅटर्न कसा अंमलात आणू शकता याची काही उदाहरणे येथे आहेत:

### Microsoft एजंट फ्रेमवर्क

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> हा AI एजंट तयार करण्यासाठी मुक्त स्रोत AI फ्रेमवर्क आहे. तो फंक्शन कॉलिंग वापरण्याची प्रक्रिया सुलभ करतो, ज्याद्वारे तुम्ही Python फंक्शन्स `@tool` डेकोरेटरसह टूल म्हणून परिभाषित करू शकता. फ्रेमवर्क मॉडेल आणि तुमच्या कोडमधील संवाद स्वयंचलितपणे हाताळतो. तसेच, `AzureAIProjectAgentProvider` द्वारे पूर्वनिर्मित टूल्स जसे की फाइल सर्च आणि कोड इंटरप्रेटर वापरण्याची सोय देतो.

खाली दिलेल्या आकृतीत Microsoft Agent Framework मधील फंक्शन कॉलिंग प्रक्रिया दाखवली आहे:

![function calling](../../../translated_images/mr/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework मध्ये, टूल्स डेकोरेट केलेल्या फंक्शन्स म्हणून परिभाषित केले जातात. आपण पूर्वी पाहिलेल्या `get_current_time` फंक्शनला `@tool` डेकोरेटर वापरून टूलमध्ये रूपांतर करू शकतो. फ्रेमवर्क आपोआप फंक्शन आणि त्याचे पॅरामीटर्स सिरीयलाइज करून LLM कडे पाठवण्यासाठी स्कीमा तयार करतो.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# क्लायंट तयार करा
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# एजन्ट तयार करा आणि टूलसह चालवा
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI एजंट सेवा

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> हा एक नवीन एजंटिक फ्रेमवर्क आहे ज्याचे उद्दिष्ट विकसकांना सुरक्षितपणे उच्च दर्जाच्या, विस्तारक्षम AI एजंट तयार करण्यास, तैनात करण्यास आणि स्केल करण्यास सक्षम करणे आहे, ज्यासाठी तुम्हाला अंतर्गत संगणकीय आणि स्टोरेज संसाधनांचे व्यवस्थापन करण्याची गरज नाही. तो खासकरून एंटरप्राइझ अनुप्रयोगांसाठी उपयुक्त आहे कारण हा पूर्णपणे व्यवस्थापित सेवा आहे ज्याला एंटरप्राइझ स्तरीय सुरक्षा आहे.

प्रत्यक्ष LLM API वापरण्याच्या तुलनेत, Azure AI Agent Service काही फायदे देतो, जसे:

- स्वयंचलित टूल कॉलिंग – टूल कॉल पार्स करण्याची, टूल चालवण्याची आणि प्रतिसाद हाताळण्याची गरज नाही; सर्व काही आता सर्व्हर-बंदिस्त done होते
- सुरक्षितपणे व्यवस्थापित डेटा – संवाद स्थिती स्वतः हाताळण्याऐवजी, थ्रेड्समध्ये आवश्यक सर्व माहिती साठवू शकता
- तात्काळ वापरता येणारे टूल्स – Bing, Azure AI Search, आणि Azure Functions सारख्या डेटास्रोतांशी संवाद साधण्यासाठी टूल्स

Azure AI Agent Service मध्ये उपलब्ध टूल्स दोन प्रकारांमध्ये विभागले जाऊ शकतात:

1. ज्ञान टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing सर्चसह ग्राउंडिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">फाइल सर्च</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. क्रिया टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">फंक्शन कॉलिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इंटरप्रेटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI द्वारा परिभाषित टूल्स</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

एजंट सेवा आपल्याला या टूल्सचा एकत्रित `toolset` म्हणून वापर करण्याची परवानगी देते. तसेच, `threads` वापरतो जे विशिष्ट संभाषणाचा मेसेज इतिहास ट्रॅक करतात.

कल्पना करा की तुम्ही Contoso नावाच्या कंपनीतील सेल्स एजंट आहात. तुम्हाला conversational एजंट तयार करायचा आहे जो तुमच्या विक्री डेटाविषयी प्रश्नांना उत्तर देऊ शकेल.

खालील चित्र Azure AI Agent Service वापरून विक्री डेटा कसा विश्लेषित करू शकतो हे दर्शवते:

![Agentic Service In Action](../../../translated_images/mr/agent-service-in-action.34fb465c9a84659e.webp)

सेवेबरोबर कोणतेही टूल वापरण्यासाठी आपण क्लायंट तयार करू आणि टूल किंवा टूलसेट परिभाषित करू शकतो. व्यावहारिक अंमलबजावणीसाठी खालील Python कोड वापरू शकतो. LLM टूलसेट पाहून वापरकर्त्याद्वारे तयार केलेले फंक्शन `fetch_sales_data_using_sqlite_query` वापरायचे की पूर्वनिर्मित कोड इंटरप्रेटर वापरायचा हे ठरवेल.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query फंक्शन जे fetch_sales_data_functions.py फाइलमध्ये सापडू शकते.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# टूलसेट प्रारंभ करा
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query फंक्शनसह फंक्शन कॉलिंग एजंट प्रारंभ करा आणि ते टूलसेटमध्ये जोडा
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# कोड इंटरप्रेटर टूल प्रारंभ करा आणि ते टूलसेटमध्ये जोडा.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## विश्वासार्ह AI एजंट तयार करण्यासाठी टूल वापर डिझाइन पॅटर्न वापरताना कोणते विशेष विचार आवश्यक आहेत?

LLMs कडून डायनॅमिक SQL निर्माण करताना सुरक्षा प्रश्न, विशेषत: SQL इंजेक्शन किंवा धोकादायक क्रिया (जसे डेटाबेस ड्रॉप करणे किंवा छेडछाड) याची भीती असते. हे प्रश्न खरे असले तरी, योग्य प्रकारे डेटाबेस प्रवेश परवानगी संरचीत केल्यास यावर प्रभावीपणे प्रतिबंध करता येतो. बहुतेक डेटाबेससाठी, डेटाबेसला फक्त-वाचन (read-only) मोडमध्ये कॉन्फिगर करणे आवश्यक आहे. PostgreSQL किंवा Azure SQL सारख्या डेटाबेस सेवांसाठी अॅपला फक्त वाचन-परवानगी (SELECT रोल) दिली पाहिजे.

अॅप सुरक्षित वातावरणात चालवल्याने संरक्षण वाढते. एंटरप्राइझ परिस्थितीत, डेटा बहुधा ऑपरेशनल सिस्टम्समधून वाचण्यालायक एक डेटाबेस किंवा डेटा वेअरहाऊसभर पोहोचवला जातो ज्यात वापरकर्ता-अनुकूल स्कीमा असते. यामुळे डेटा सुरक्षित, कार्यक्षम आणि प्रवेशयोग्य राहतो, आणि अॅपला मर्यादित वाचन-परवानगी मिळते.

## नमुना कोड

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## टूल वापर डिझाइन पॅटर्नबद्दल अधिक प्रश्न आहेत?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा, इतर शिकणाऱ्यांशी भेटा, ऑफिस अवर्सला सहभागी व्हा आणि तुमचे AI एजंट्स संबंधी प्रश्न विचार करा.

## अधिक संसाधने

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service कार्यशाळा</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent कार्यशाळा</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework आढावा</a>

## मागील धडा

[एजंटिक डिझाइन पॅटर्न समजून घेणे](../03-agentic-design-patterns/README.md)

## पुढील धडा
[एजेंटिक RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->