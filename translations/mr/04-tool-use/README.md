<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:06:37+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "mr"
}
-->
[![चांगले AI एजंट्स कसे डिझाइन करावे](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.mr.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(वरील प्रतिमेवर क्लिक करा आणि या धड्याचा व्हिडिओ पहा)_

# टूल वापर डिझाइन पॅटर्न

टूल्स मनोरंजक आहेत कारण ते AI एजंट्सना अधिक व्यापक क्षमता देतात. एजंट्सकडे मर्यादित क्रिया संच असण्याऐवजी, टूल जोडल्याने एजंट्स आता विविध प्रकारच्या क्रिया करू शकतात. या अध्यायात, आपण टूल वापर डिझाइन पॅटर्न पाहणार आहोत, जो वर्णन करतो की AI एजंट्स विशिष्ट टूल्सचा वापर करून आपले उद्दिष्ट कसे साध्य करू शकतात.

## परिचय

या धड्यात, आम्ही खालील प्रश्नांची उत्तरे शोधण्याचा प्रयत्न करणार आहोत:

- टूल वापर डिझाइन पॅटर्न म्हणजे काय?
- कोणत्या उपयोग प्रकरणांमध्ये याचा वापर केला जाऊ शकतो?
- डिझाइन पॅटर्न अंमलात आणण्यासाठी आवश्यक घटक/बांधकाम ब्लॉक्स कोणते आहेत?
- विश्वासार्ह AI एजंट्स तयार करण्यासाठी टूल वापर डिझाइन पॅटर्न वापरण्याच्या विशेष विचार कोणते आहेत?

## शिकण्याची उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, तुम्ही सक्षम असाल:

- टूल वापर डिझाइन पॅटर्न आणि त्याचा उद्देश परिभाषित करणे.
- टूल वापर डिझाइन पॅटर्न लागू होऊ शकणारे उपयोग प्रकरणे ओळखणे.
- डिझाइन पॅटर्न अंमलात आणण्यासाठी आवश्यक मुख्य घटक समजून घेणे.
- या डिझाइन पॅटर्नचा वापर करून AI एजंट्समध्ये विश्वासार्हता सुनिश्चित करण्यासाठी विचार ओळखणे.

## टूल वापर डिझाइन पॅटर्न म्हणजे काय?

**टूल वापर डिझाइन पॅटर्न** LLMs ला विशिष्ट उद्दिष्टे साध्य करण्यासाठी बाह्य टूल्सशी संवाद साधण्याची क्षमता देण्यावर लक्ष केंद्रित करते. टूल्स म्हणजे एजंट्सद्वारे क्रिया करण्यासाठी चालवले जाणारे कोड. टूल्स साध्या फंक्शनसारखे असू शकतात, जसे की कॅल्क्युलेटर, किंवा तृतीय-पक्ष सेवा, जसे की स्टॉक किंमत शोधणे किंवा हवामान अंदाजासाठी API कॉल. AI एजंट्सच्या संदर्भात, टूल्स **मॉडेल-जनरेटेड फंक्शन कॉल्स**च्या प्रतिसादात एजंट्सद्वारे चालवण्यासाठी डिझाइन केले जातात.

## कोणत्या उपयोग प्रकरणांमध्ये याचा वापर केला जाऊ शकतो?

AI एजंट्स टूल्सचा उपयोग करून जटिल कार्ये पूर्ण करू शकतात, माहिती मिळवू शकतात किंवा निर्णय घेऊ शकतात. टूल वापर डिझाइन पॅटर्न बाह्य प्रणालींसह डायनॅमिक संवाद आवश्यक असलेल्या परिस्थितींमध्ये वापरला जातो, जसे की डेटाबेस, वेब सेवा किंवा कोड इंटरप्रिटर्स. ही क्षमता विविध उपयोग प्रकरणांसाठी उपयुक्त आहे, ज्यामध्ये समाविष्ट आहे:

- **डायनॅमिक माहिती मिळवणे:** एजंट्स बाह्य APIs किंवा डेटाबेस क्वेरी करू शकतात जेणेकरून अद्ययावत डेटा मिळवता येईल (उदा. SQLite डेटाबेस क्वेरी करणे, स्टॉक किंमती किंवा हवामान माहिती मिळवणे).
- **कोड अंमलबजावणी आणि व्याख्या:** एजंट्स गणितीय समस्या सोडवण्यासाठी, अहवाल तयार करण्यासाठी किंवा सिम्युलेशन करण्यासाठी कोड किंवा स्क्रिप्ट चालवू शकतात.
- **वर्कफ्लो ऑटोमेशन:** टास्क शेड्यूलर्स, ईमेल सेवा किंवा डेटा पाइपलाइन्ससारख्या टूल्स एकत्रित करून पुनरावृत्ती किंवा बहु-चरण वर्कफ्लो स्वयंचलित करणे.
- **ग्राहक समर्थन:** एजंट्स CRM प्रणाली, तिकीटिंग प्लॅटफॉर्म किंवा ज्ञान तळाशी संवाद साधून वापरकर्त्याच्या चौकशीचे निराकरण करू शकतात.
- **सामग्री निर्मिती आणि संपादन:** एजंट्स व्याकरण तपासक, मजकूर संक्षेपक किंवा सामग्री सुरक्षा मूल्यांकन करणारे टूल्स वापरून सामग्री निर्मिती कार्यांमध्ये मदत करू शकतात.

## टूल वापर डिझाइन पॅटर्न अंमलात आणण्यासाठी आवश्यक घटक/बांधकाम ब्लॉक्स कोणते आहेत?

हे बांधकाम ब्लॉक्स AI एजंट्सना विविध प्रकारची कार्ये करण्यास सक्षम करतात. टूल वापर डिझाइन पॅटर्न अंमलात आणण्यासाठी आवश्यक मुख्य घटक पाहूया:

- **फंक्शन/टूल स्कीमाज:** उपलब्ध टूल्सची तपशीलवार परिभाषा, ज्यामध्ये फंक्शनचे नाव, उद्देश, आवश्यक पॅरामीटर्स आणि अपेक्षित आउटपुट्स समाविष्ट आहेत. या स्कीमाज LLM ला उपलब्ध टूल्स काय आहेत आणि वैध विनंत्या कशा तयार करायच्या ते समजून घेण्यास सक्षम करतात.

- **फंक्शन अंमलबजावणी लॉजिक:** वापरकर्त्याच्या हेतू आणि संभाषणाच्या संदर्भावर आधारित टूल्स कसे आणि कधी वापरायचे याचे नियमन करते. यात प्लॅनर मॉड्यूल्स, रूटिंग यंत्रणा किंवा टूल वापर डायनॅमिकपणे ठरवणारे अटी प्रवाह समाविष्ट असू शकतात.

- **संदेश हाताळणी प्रणाली:** वापरकर्त्याच्या इनपुट्स, LLM प्रतिसाद, टूल कॉल्स आणि टूल आउटपुट्स यांच्यातील संभाषणाचा प्रवाह व्यवस्थापित करणारे घटक.

- **टूल इंटिग्रेशन फ्रेमवर्क:** एजंट्सना विविध टूल्सशी जोडणारे पायाभूत सुविधा, ते साधे फंक्शन्स असो किंवा जटिल बाह्य सेवा.

- **त्रुटी हाताळणी आणि पडताळणी:** टूल अंमलबजावणीतील अपयश हाताळण्यासाठी, पॅरामीटर्स पडताळण्यासाठी आणि अनपेक्षित प्रतिसाद व्यवस्थापित करण्यासाठी यंत्रणा.

- **स्थिती व्यवस्थापन:** संभाषणाचा संदर्भ, मागील टूल संवाद आणि सातत्य सुनिश्चित करण्यासाठी सतत डेटा ट्रॅक करते.

पुढे, फंक्शन/टूल कॉलिंग अधिक तपशीलवार पाहूया.

### फंक्शन/टूल कॉलिंग

फंक्शन कॉलिंग हे मोठ्या भाषेच्या मॉडेल्स (LLMs) ला टूल्सशी संवाद साधण्यास सक्षम करण्याचा प्राथमिक मार्ग आहे. तुम्ही 'फंक्शन' आणि 'टूल' परस्पर वापरलेले पाहाल कारण 'फंक्शन्स' (पुनर्वापरयोग्य कोडचे ब्लॉक्स) हे 'टूल्स' आहेत जे एजंट्स कार्ये पार पाडण्यासाठी वापरतात. फंक्शनचा कोड चालवण्यासाठी, LLM ला वापरकर्त्याच्या विनंतीची तुलना फंक्शनच्या वर्णनाशी करावी लागते. हे करण्यासाठी सर्व उपलब्ध फंक्शन्सची वर्णने असलेली स्कीमा LLM ला पाठवली जाते. LLM नंतर कार्यासाठी सर्वात योग्य फंक्शन निवडते आणि त्याचे नाव आणि युक्तिवाद परत करते. निवडलेले फंक्शन चालवले जाते, त्याचा प्रतिसाद LLM ला परत पाठवला जातो, जो वापरकर्त्याच्या विनंतीला प्रतिसाद देण्यासाठी माहिती वापरतो.

एजंट्ससाठी फंक्शन कॉलिंग अंमलात आणण्यासाठी, तुम्हाला आवश्यक आहे:

1. फंक्शन कॉलिंगला समर्थन देणारे LLM मॉडेल
2. फंक्शन वर्णनांची स्कीमा
3. प्रत्येक वर्णन केलेल्या फंक्शनसाठी कोड

सॅन फ्रान्सिस्कोमधील वर्तमान वेळ मिळवण्याचे उदाहरण वापरूया:

1. **फंक्शन कॉलिंगला समर्थन देणारे LLM प्रारंभ करा:**

    सर्व मॉडेल्स फंक्शन कॉलिंगला समर्थन देत नाहीत, त्यामुळे तुम्ही वापरत असलेल्या LLM ला समर्थन आहे की नाही हे तपासणे महत्त्वाचे आहे. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> फंक्शन कॉलिंगला समर्थन देते. आम्ही Azure OpenAI क्लायंट सुरू करून सुरुवात करू शकतो.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **फंक्शन स्कीमा तयार करा:**

    पुढे आम्ही JSON स्कीमा परिभाषित करू ज्यामध्ये फंक्शनचे नाव, फंक्शन काय करते याचे वर्णन, आणि फंक्शन पॅरामीटर्सची नावे आणि वर्णने असतील. आम्ही ही स्कीमा पूर्वी तयार केलेल्या क्लायंटला वापरकर्त्याच्या सॅन फ्रान्सिस्कोमधील वेळ शोधण्याच्या विनंतीसह पास करू. महत्त्वाचे म्हणजे टूल कॉल परत केला जातो, प्रश्नाचे अंतिम उत्तर **नाही**. यापूर्वी नमूद केल्याप्रमाणे, LLM कार्यासाठी निवडलेल्या फंक्शनचे नाव आणि त्याला पास होणारे युक्तिवाद परत करते.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
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

    आता LLM ने कोणते फंक्शन चालवायचे ते निवडले आहे, कार्य पार पाडण्यासाठी कोड अंमलात आणणे आणि चालवणे आवश्यक आहे. आम्ही Python मध्ये वर्तमान वेळ मिळवण्यासाठी कोड अंमलात आणू शकतो. आम्हाला अंतिम परिणाम मिळवण्यासाठी response_message मधून नाव आणि युक्तिवाद काढण्यासाठी कोड लिहिण्याची आवश्यकता असेल.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

फंक्शन कॉलिंग हे बहुतेक, जर सर्व नाही तर एजंट टूल वापर डिझाइनचे केंद्र आहे, परंतु ते सुरुवातीपासून अंमलात आणणे कधी कधी आव्हानात्मक असू शकते. 
जसे आपण [धडा 2](../../../02-explore-agentic-frameworks) मध्ये शिकलो, एजंटिक फ्रेमवर्क्स आपल्याला टूल वापर अंमलात आणण्यासाठी पूर्व-निर्मित बांधकाम ब्लॉक्स प्रदान करतात.

## एजंटिक फ्रेमवर्क्ससह टूल वापर उदाहरणे

येथे काही उदाहरणे आहेत की तुम्ही वेगवेगळ्या एजंटिक फ्रेमवर्क्स वापरून टूल वापर डिझाइन पॅटर्न कसा अंमलात आणू शकता:

### सेमॅंटिक कर्नल

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">सेमॅंटिक कर्नल</a> हे .NET, Python आणि Java डेव्हलपर्ससाठी ओपन-सोर्स AI फ्रेमवर्क आहे जे मोठ्या भाषेच्या मॉडेल्स (LLMs) सह कार्य करतात. हे तुमच्या फंक्शन्स आणि त्यांच्या पॅरामीटर्सचे वर्णन मॉडेलला स्वयंचलितपणे करून फंक्शन कॉलिंग वापरण्याची प्रक्रिया सुलभ करते, ज्याला <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">सिरीयलायझिंग</a> म्हणतात. हे मॉडेल आणि तुमच्या कोडमधील संवाद व्यवस्थापित करते. सेमॅंटिक कर्नलसारख्या एजंटिक फ्रेमवर्कचा वापर करण्याचा आणखी एक फायदा म्हणजे तुम्ही <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">फाइल शोध</a> आणि <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">कोड इंटरप्रिटर</a> सारखी पूर्व-निर्मित टूल्स वापरू शकता.

खालील आकृती सेमॅंटिक कर्नलसह फंक्शन कॉलिंगची प्रक्रिया स्पष्ट करते:

![फंक्शन कॉलिंग](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.mr.png)

सेमॅंटिक कर्नलमध्ये फंक्शन्स/टूल्सना <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">प्लगइन्स</a> म्हणतात. आपण पूर्वी पाहिलेल्या `get_current_time` फंक्शनला वर्गात बदलून प्लगइनमध्ये रूपांतरित करू शकतो. आम्ही `kernel_function` डेकोरेटर देखील आयात करू शकतो, जो फंक्शनचे वर्णन घेतो. जेव्हा तुम्ही GetCurrentTimePlugin सह कर्नल तयार करता, तेव्हा कर्नल स्वयंचलितपणे फंक्शन आणि त्याच्या पॅरामीटर्सचे सिरीयलायझेशन करतो, प्रक्रिया करताना LLM ला पाठवण्यासाठी स्कीमा तयार करतो.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> हे एक नवीन एजंटिक फ्रेमवर्क आहे जे डेव्हलपर्सना उच्च-गुणवत्तेचे आणि विस्तारक्षम AI एजंट्स सुरक्षितपणे तयार, तैनात आणि स्केल करण्यासाठी सक्षम करण्यासाठी डिझाइन केले आहे, त्यासाठी अंतर्गत संगणन आणि स्टोरेज संसाधने व्यवस्थापित करण्याची आवश्यकता नाही. हे विशेषतः एंटरप्राइझ अनुप्रयोगांसाठी उपयुक्त आहे कारण ते एंटरप्राइझ ग्रेड सुरक्षा असलेली पूर्णपणे व्यवस्थापित सेवा आहे.

LLM API सह थेट विकसित करण्याच्या तुलनेत, Azure AI Agent Service काही फायदे प्रदान करते, ज्यामध्ये समाविष्ट आहे:

- स्वयंचलित टूल कॉलिंग – टूल कॉल पार्स करण्याची, टूल चालवण्याची आणि प्रतिसाद हाताळण्याची गरज नाही; हे सर्व आता सर्व्हर-साइड केले जाते.
- सुरक्षितपणे व्यवस्थापित डेटा – तुमची स्वतःची संभाषण स्थिती व्यवस्थापित करण्याऐवजी, तुम्ही थ्रेड्सवर विश्वास ठेवू शकता जे तुम्हाला आवश्यक असलेली सर्व माहिती संग्रहित करतात.
- रेडी-टू-यूज टूल्स – Bing, Azure AI Search आणि Azure Functions सारख्या डेटा स्रोतांशी संवाद साधण्यासाठी तुम्ही वापरू शकणारी टूल्स.

Azure AI Agent Service मध्ये उपलब्ध टूल्स दोन श्रेणींमध्ये विभागली जाऊ शकतात:

1. ज्ञान टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search सह ग्राउंडिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">फाइल शोध</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. क्रिया टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">फंक्शन कॉलिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इंटरप्रिटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित टूल्स</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service आम्हाला `toolset` म्हणून ही टूल्स एकत्र वापरण्याची परवानगी देते. हे `threads` देखील वापरते जे विशिष्ट संभाषणातील संदेशांचा इतिहास ट्रॅक करतात.

कल्पना करा की तुम्ही Contoso नावाच्या कंपनीत विक्री एजंट आहात. तुम्हाला तुमच्या विक्री डेटाबद्दल प्रश्नांची उत्तरे देणारा संभाषण एजंट विकसित करायचा आहे.

खालील प्रतिमा स्पष्ट करते की तुम्ही तुमच्या विक्री डेटा विश्लेषणासाठी Azure AI Agent Service कसे वापरू शकता:

![एजंटिक सेवा क्रियेत](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.mr.jpg)

सेवेच्या मदतीने कोणतेही टूल्स वापरण्यासाठी आम्ही क्लायंट तयार करू शकतो आणि टूल किंवा टूलसेट परिभाषित करू शकतो. हे व्यावहारिकपणे अंमलात आणण्यासाठी आम्ही खालील Python कोड वापरू शकतो. LLM टूलसेटकडे पाहून वापरकर्त्याने तयार केलेले फंक्शन, `fetch_sales_data_using_sqlite_query`, किंवा पूर्व-निर्मित कोड इंटरप्रिटर वापरायचे की नाही हे वापरकर्त्याच्या विनंतीनुसार ठरवू शकते.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## विश्वासार्ह AI एजंट्स तयार करण्यासाठी टूल
अ‍ॅप सुरक्षित वातावरणात चालवल्याने संरक्षण अधिक मजबूत होते. एंटरप्राइझ परिस्थितीत, डेटा सामान्यतः ऑपरेशनल सिस्टीममधून काढला जातो आणि वाचण्यापुरत्या परवानगी असलेल्या डेटाबेस किंवा डेटा वेअरहाऊसमध्ये रूपांतरित केला जातो, ज्यामध्ये वापरकर्ता-अनुकूल स्कीमा असते. या दृष्टिकोनामुळे डेटा सुरक्षित राहतो, कार्यक्षमतेसाठी आणि प्रवेशयोग्यतेसाठी अनुकूलित होतो, तसेच अ‍ॅपला मर्यादित, वाचण्यापुरतीच परवानगी मिळते.

## नमुना कोड

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## टूल वापर डिझाईन पॅटर्नबद्दल अधिक प्रश्न आहेत का?

इतर शिकणाऱ्यांशी भेटण्यासाठी, ऑफिस तासांमध्ये सहभागी होण्यासाठी आणि तुमचे AI Agents संबंधित प्रश्न विचारण्यासाठी [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा.

## अतिरिक्त संसाधने

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## मागील धडा

[Agentic Design Patterns समजून घेणे](../03-agentic-design-patterns/README.md)

## पुढील धडा

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपयाआहे की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->