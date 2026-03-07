[![कसे चांगले AI एजंट डिझाइन करावे](../../../translated_images/mr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(वरील प्रतिमा क्लिक करून या धड्याचा व्हिडिओ पहा)_

# टूल वापर डिझाइन पॅटर्न

टूल्स मनोरंजक आहेत कारण ते AI एजंट्सना अधिक विस्तृत क्षमतांची अनुमती देतात. एजंटकडे केवळ मर्यादित क्रिया करण्याची करण्याची क्षमता असण्याऐवजी, एका टूलची भर घालून एजंट आता विविध प्रकारच्या क्रिया करू शकतो. या अध्यायात, आपण Tool Use Design Pattern पाहणार आहोत, जे वर्णन करते की AI एजंट्स विशिष्ट टूल्सचा वापर करून त्यांच्या उद्दिष्टांची कशी पूर्तता करू शकतात.

## परिचय

या धड्यात, आपण खालील प्रश्नांची उत्तरे शोधणार आहोत:

- टूल वापर डिझाइन पॅटर्न म्हणजे काय?
- कोणत्या उपयोगप्रकरणांवर हे लागू होते?
- डिझाइन पॅटर्न अमलात आणण्यासाठी कोणते घटक/बिल्डिंग ब्लॉक्स आवश्यक आहेत?
- विश्वासार्ह AI एजंट तयार करण्यासाठी Tool Use Design Pattern वापरताना कोणत्या विशेष बाबींचा विचार करावा?

## शिकण्याचे उद्दिष्ट

हा धडा पूर्ण केल्यानंतर, आपण सक्षम असाल:

- Tool Use Design Pattern आणि त्याचा उद्देश परिभाषित करण्यास.
- कोणत्या उपयोगप्रकरणांमध्ये Tool Use Design Pattern लागू होता हे ओळखण्यास.
- डिझाइन पॅटर्न अमलात आणण्यासाठी आवश्यक प्रमुख घटक समजण्यास.
- हा डिझाइन पॅटर्न वापरणाऱ्या AI एजंट्समध्ये विश्वासार्हता सुनिश्चित करण्यासाठी विचार करण्याच्या बाबी ओळखण्यास.

## टूल वापर डिझाइन पॅटर्न म्हणजे काय?

The **Tool Use Design Pattern** LLMs ला बाह्य टूल्सशी संवाद साधण्याची क्षमता देण्यावर लक्ष केंद्रित करते जेणेकरून विशिष्ट उद्दिष्टे साध्य करता येतील. टूल्स म्हणजे असे कोड जे एजन्टद्वारे क्रिया करण्यासाठी चालवले जाऊ शकतात. टूल हे साधे फंक्शन जसे की कॅलक्युलेटर असू शकते, किंवा तृतीय-पक्ष सेवेकडे API कॉल असू शकते जसे स्टॉक किंमत शोधणे किंवा हवामान अंदाज. AI एजंट्सच्या संदर्भात, टूल्सना **model-generated function calls** च्या प्रतिसादात एजंटद्वारे चालवण्यासाठी डिझाइन केले जाते.

## कोणत्या उपयोगप्रकरणांवर हे लागू होते?

AI एजंट्स जटिल कार्ये पूर्ण करण्यासाठी, माहिती प्राप्त करण्यासाठी किंवा निर्णय घेण्यासाठी टूल्सचा लाभ घेऊ शकतात. टूल वापर डिझाइन पॅटर्न बहुधा असे परिदृश्यात वापरले जाते ज्यांना बाह्य प्रणालींबरोबर डायनॅमिक संवादाची आवश्यकता असते, जसे डेटाबेस, वेब सेवा किंवा कोड इंटरप्रेटर. ही क्षमता अनेक वेगळ्या उपयोगप्रकरणांसाठी उपयुक्त आहे ज्यात समावेश आहे:

- **डायनॅमिक माहिती मिळवणे:** एजंट्स बाह्य APIs किंवा डेटाबेसवर प्रश्न विचारू शकतात अपडेटेड डेटा घेण्यासाठी (उदा., डेटा विश्लेषणासाठी SQLite डेटाबेसमध्ये क्वेरी करणे, स्टॉक किंमती किंवा हवामान माहिती प्राप्त करणे).
- **कोड अंमलबजावणी आणि इंटरप्रिटेशन:** एजंट्स गणितीय समस्या सोडवण्यासाठी, अहवाल तयार करण्यासाठी किंवा सिम्युलेशन्स करण्यासाठी कोड किंवा स्क्रिप्ट चालवू शकतात.
- **कार्यप्रवाह स्वयंचलितीकरण:** टास्क शेड्युलर्स, ईमेल सेवा किंवा डेटा पाइपलाइन्स सारख्या टूल्सचे एकत्रीकरण करून पुनरावृत्ती होणारे किंवा बहु-टप्प्यांचे कार्यप्रवाह स्वयंचलित करणे.
- **कस्टमर समर्थन:** एजंट्स CRM सिस्टम्स, तिकीट प्लॅटफॉर्म्स किंवा ज्ञानाधारांशी संवाद साधून वापरकर्ता प्रश्न सोडवू शकतात.
- **सामग्री तयार करणे आणि संपादन:** एजंट्स व्याकरण तपासक, मजकूर सारांशक किंवा सामग्री सुरक्षा मूल्यांकन करणारे टूल्स वापरून सामग्री निर्मिती कार्यात मदत करू शकतात.

## टूल वापर डिझाइन पॅटर्न अमलात आणण्यासाठी कोणते घटक/बिल्डिंग ब्लॉक्स आवश्यक आहेत?

हे बिल्डिंग ब्लॉक्स AI एजंटला विस्तृत कार्ये करण्यास परवानगी देतात. Tool Use Design Pattern अमलात आणण्यासाठी आवश्यक प्रमुख घटक पाहूया:

- **Function/Tool Schemas**: उपलब्ध टूल्सच्या सविस्तर व्याख्या, ज्यात फंक्शनचे नाव, उद्देश, आवश्यक पॅरामीटर्स आणि अपेक्षित आऊटपुट यांचा समावेश असतो. या स्कीमामुळे LLM ला काय उपलब्ध आहे आणि वैध विनंत्या कशा बांधायच्या हे समजते.

- **Function Execution Logic**: वापरकर्त्याच्या उद्देश आणि संभाषण संदर्भावर आधारित केव्हा आणि कसे टूल्स कॉल करावेत हे नियंत्रित करते. यात प्लॅनर मॉड्यूल, राउटिंग मेकॅनिझम किंवा अट-आधारित प्रवाह असू शकतात जे टूल वापर डायनॅमिकली ठरवतात.

- **Message Handling System**: वापरकर्ता इनपुट्स, LLM प्रतिसाद, टूल कॉल्स आणि टूल आउटपुटमधील संभाषण प्रवाह व्यवस्थापित करणारे घटक.

- **Tool Integration Framework**: एजंटला विविध टूल्सशी कनेक्ट करणारी इन्फ्रास्ट्रक्चर, मग ती साधी फंक्शन्स असोत किंवा जटिल बाह्य सेवा असोत.

- **Error Handling & Validation**: टूल अंमलबजावणीतील अपयश हाताळण्यासाठी, पॅरामीटर्सची पडताळणी करण्यासाठी आणि अनपेक्षित प्रतिसाद व्यवस्थापित करण्यासाठी यंत्रणा.

- **State Management**: संभाषण संदर्भ, मागील टूल परस्परसंवाद आणि सातत्य राखण्यासाठी कायमची डेटा ट्रॅक करते जे बहु-टर्न संवादात सुसंगतता सुनिश्चित करते.

पुढे, Function/Tool Calling ची अधिक तफावत पाहूया.
 
### Function/Tool Calling

Function calling हा मुख्य मार्ग आहे ज्याद्वारे आम्ही Large Language Models (LLMs) ना टूल्सशी संवाद साधण्यासाठी सक्षम करतो. आपण अनेकदा 'Function' आणि 'Tool' या शब्दांचा परस्परवापर होताना पाहू कारण 'functions' (पुन्हा वापरता येण्यायोग्य कोडचे ब्लॉक्स) हेच एजंट्स कार्ये पार पाडण्यासाठी वापरत असलेले 'tools' असतात. एखाद्या फंक्शनचा कोड invoke होण्यासाठी, LLM ला वापरकर्त्याच्या विनंतीची तुलना फंक्शनच्या वर्णनाशी करावी लागते. हे करण्यासाठी उपलब्ध सर्व फंक्शन्सच्या वर्णनांचा समावेश असलेली स्कीमा LLM कडे पाठवली जाते. मग LLM कार्यासाठी सर्वात योग्य फंक्शन निवडते आणि त्याचे नाव आणि आर्ग्युमेंट्स परत करते. निवडलेले फंक्शन invoke केले जाते, त्याचा प्रतिसाद LLM कडे परत पाठवला जातो, आणि LLM त्या माहितीचा वापर करून वापरकर्त्याच्या विनंतीला उत्तर देते.

डेव्हलपर्सना एजंट्ससाठी function calling अमलात आणण्यासाठी, आपल्याला आवश्यक आहे:

1. Function calling ला समर्थन करणारे LLM मॉडेल
2. फंक्शन वर्णन असलेली स्कीमा
3. वर्णन केलेल्या प्रत्येक फंक्शनसाठी कोड

सॅन फ्रान्सिस्कोमधील सध्याचा वेळ मिळवण्याचे उदाहरण घेऊया:

1. **Function calling ला समर्थन करणारे LLM इनिशियलाइझ करा:**

    सर्व मॉडेल्स function calling ला समर्थन करत नाहीत, त्यामुळे आपण वापरत असलेले LLM हे समर्थन करते का ते तपासणे महत्वाचे आहे.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> function calling ला समर्थन करते. आपण Azure OpenAI क्लायंट इनिशिएट करून सुरुवात करू शकतो. 

    ```python
    # Azure OpenAI क्लायंट प्रारंभ करा
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Function Schema तयार करा**:

    पुढे आपण JSON स्कीमा परिभाषित करू ज्यात फंक्शनचे नाव, फंक्शन काय करते याचे वर्णन, आणि फंक्शन पॅरामीटर्सची नावे व वर्णने असतील.
    नंतर ही स्कीमा आपण पूर्वी तयार केलेल्या क्लायंटकडे पास करू आणि वापरकर्ता San Francisco मधील वेळ शोधण्याची विनंती करेल. महत्वाचे लक्षात घ्यायचे म्हणजे **tool call** परत केला जातो, **प्रश्नाचे अंतिम उत्तर नाही**. जसे आधी सांगितले, LLM त्याने कार्यासाठी निवडलेले फंक्शनचे नाव आणि त्याला पास केले जाणारे आर्ग्युमेंट्स परत करते.

    ```python
    # मॉडेलने वाचण्यासाठी फंक्शनचे वर्णन
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
  
    # पहिला API कॉल: मॉडेलला फंक्शन वापरण्यास विचारा
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
  
1. **कार्य पार पाडण्यासाठी आवश्यक फंक्शन कोड:**

    आता LLM ने कोणते फंक्शन चालवायचे ते निवडलं आहे, ते कार्य पार पाडणारा कोड अंमलात आणावा आणि चालवावा लागेल.
    आम्ही सध्याचा वेळ मिळवण्यासाठी Python मध्ये कोड अंमलात आणू शकतो. तसेच response_message मधून नाव आणि आर्ग्युमेंट्स काढून अंतिम निकाल मिळवण्यासाठी कोड लिहावा लागेल.

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

Function Calling हे बहुसंख्य, किंवा सर्व एजंट टूल वापर डिझाइनचा हृदयस्थान आहे, परंतु ते स्क्रॅचपासून अंमलात आणणे कधीकधी आव्हानात्मक असू शकते.
जसे आपण [Lesson 2](../../../02-explore-agentic-frameworks) मध्ये शिकलो, agentic frameworks आम्हाला टूल वापर अंमलबजावणीसाठी पूर्व-निर्मित बिल्डिंग ब्लॉक्स पुरवतात.
 
## Agentic फ्रेमवर्क्ससह टूल वापर उदाहरणे

येथे विविध agentic frameworks वापरून आपण Tool Use Design Pattern कशी अमलात आणू शकतो याची काही उदाहरणे आहेत:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> हा AI एजंट्स तयार करण्यासाठी एक open-source AI फ्रेमवर्क आहे. हे function calling वापरण्याची प्रक्रिया सुलभ करते कारण आपण `@tool` डेकोरेटरसह Python फंक्शन्स म्हणून टूल्स परिभाषित करू शकता. फ्रेमवर्क मॉडेल आणि आपल्या कोडमधील परत-फिरतीचे संवाद हाताळते. तसेच ते `AzureAIProjectAgentProvider` मार्फत File Search आणि Code Interpreter सारखी पूर्व-निर्मित टूल्स वापरण्याची सुविधा देते.

खालील आलेख Microsoft Agent Framework सह function calling प्रक्रिया दर्शवितो:

![function calling](../../../translated_images/mr/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework मध्ये, टूल्स decorated फंक्शन्स म्हणून परिभाषित केले जातात. आपण आधी बघितलेले `get_current_time` फंक्शन `@tool` डेकोरेटर वापरून टूलमध्ये रूपांतर करू शकतो. फ्रेमवर्क आपोआप फंक्शन आणि त्याच्या पॅरामीटर्सची सिरीअलायझेशन करून LLM कडे पाठवण्यासाठी स्कीमा तयार करेल.

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

# एजंट तयार करा आणि साधनासह चालवा
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> हा एक नवीन agentic फ्रेमवर्क आहे जो डेव्हलपर्सना सुरक्षितपणे उच्च-गुणवत्तेचे, वर्धनीय AI एजंट तयार, तैनात आणि स्केल करण्यास सक्षम बनवण्यासाठी डिझाइन केले गेले आहे, ज्यासाठी बेसिक compute आणि storage resources व्यवस्थापित करण्याची गरज नाही. हे एंटरप्राइझ अनुप्रयोगांसाठी विशेषतः उपयुक्त आहे कारण हे पूर्णपणे managed सेवा असून एंटरप्राइझ दर्जाच्या सुरक्षा सुविधांसह येते.

LLM API शी थेट विकसित करण्याच्या तुलनेत, Azure AI Agent Service काही फायदे प्रदान करते, ज्यात समावेश आहे:

- Automatic tool calling – टूल कॉल पार्स करण्याची, टूल invoke करण्याची आणि प्रतिसाद हाताळण्याची आवश्यकता नाही; ही सर्व प्रक्रिया आता server-side केली जाते
- Securely managed data – संभाषण स्थिती स्वतःच व्यवस्थापित करण्याऐवजी, आपण threads वर विसंबू शकता जे सर्व आवश्यक माहिती साठवतात
- Out-of-the-box tools – आपल्या डेटा स्त्रोतांसोबत संवाद साधण्यासाठी वापरता येणारी टूल्स, जसे Bing, Azure AI Search, आणि Azure Functions.

Azure AI Agent Service मधील उपलब्ध टूल्स दोन श्रेण्यांमध्ये विभागले जाऊ शकतात:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service आम्हाला हे टूल्स एकत्र `toolset` म्हणून वापरण्याची परवानगी देते. ते `threads` देखील वापरते जे विशिष्ट संभाषणाच्या संदेश इतिहासाला ट्रॅक करतात.

कल्पना करा आपण Contoso नावाच्या कंपनीतील सेल्स एजंट आहात. आपण असा संभाषणात्मक एजंट विकसित करू इच्छिता जो आपल्या विक्री डेटाबद्दल प्रश्नांची उत्तरे देऊ शकेल.

खालील प्रतिमा दर्शवते की आपण Azure AI Agent Service वापरून आपल्या विक्री डेटाचे विश्लेषण कसे करु शकता:

![Agentic Service In Action](../../../translated_images/mr/agent-service-in-action.34fb465c9a84659e.webp)

या सेवा सोबत कोणतेही टूल वापरण्यासाठी आपण क्लायंट तयार करू आणि टूल किंवा toolset परिभाषित करू शकतो. व्यावहारिकपणे हे अमलात आणण्यासाठी आपण खालील Python कोड वापरू शकतो. LLM टूलसेट बघून निर्णय घेऊ शकेल की वापरकर्ता बनवलेल्या `fetch_sales_data_using_sqlite_query` फंक्शनचा वापर करायचा की पूर्व-निर्मित Code Interpreter वापरायचा, हा वापरकर्त्याच्या विनंतीवर अवलंबून असेल.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py फाईलमध्ये उपलब्ध असलेले fetch_sales_data_using_sqlite_query फंक्शन.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# टूलसेट आरंभ करा
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query फंक्शनसह फंक्शन कॉल करणारा एजंट आरंभ करा आणि तो टूलसेटमध्ये जोडा
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter टूल आरंभ करा आणि ते टूलसेटमध्ये जोडा.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## विश्वासार्ह AI एजंट बनवण्यासाठी Tool Use Design Pattern वापरताना कोणत्या विशेष बाबी विचारात घ्याव्यात?

LLMs द्वारा डायनॅमिकली जनरेट केलेल्या SQL बाबत सामान्य चिंता म्हणजे सुरक्षा, विशेषत: SQL injection किंवा डेटाबेस ड्रॉप/छेडछाड सारख्या दुर्भावनापूर्ण क्रियांचे धोके. जरी या चिंता बरोबर असल्या तरी त्या योग्यरित्या डेटाबेस प्रवेश परवानग्या कॉन्फिगर करून प्रभावीपणे कमी करता येऊ शकतात. बहुतेक डेटाबेससाठी हे डेटाबेसचे read-only म्हणून कॉन्फिगरेशन करणे समाविष्ट करते. PostgreSQL किंवा Azure SQL सारख्या डेटाबेस सेवांसाठी, अॅपला read-only (SELECT) भूमिका दिली गेली पाहिजे.

अॅप सुरक्षित वातावरणात चालविल्यास संरक्षण अधिक वाढते. एंटरप्राइझ परिदृश्यांमध्ये, डेटाला सामान्यपणे ऑपरेशनल सिस्टम्समधून काढून read-only डेटाबेस किंवा डेटा वेअरहाऊसमध्ये रूपांतरित केले जाते ज्याचा स्कीमा वापरकर्ता-अनुकूल असतो. हा दृष्टिकोन सुनिश्चित करतो की डेटा सुरक्षित आहे, कार्यक्षमता व प्रवेशयोग्यता optimized आहे, आणि अॅपला मर्यादित, read-only प्रवेश आहे.

## नमुना कोड्स

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Tool Use Design Patterns बद्दल अजून प्रश्न आहेत का?

इतर शिक्षार्थींशी भेटण्यासाठी, office hours attended करण्यासाठी आणि आपले AI Agents सम्बन्धी प्रश्न विचारण्यासाठी [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा.

## अतिरिक्त संसाधने

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## मागील धडा

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## पुढील धडा
[एजेन्टिक RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
हा दस्तऐवज AI अनुवाद सेवा Co-op Translator (https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, परंतु कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा चुकीची माहिती असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत समजावा. महत्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुतीं किंवा चुकीच्या अर्थलावाबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->