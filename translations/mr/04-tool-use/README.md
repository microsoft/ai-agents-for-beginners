[![कसे तयार करावे चांगले AI एजंट्स](../../../translated_images/mr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(या धड्याचा व्हिडिओ पाहण्यासाठी वरील प्रतिमेवर क्लिक करा)_

# टूल वापर डिझाईन पॅटर्न

टूल्स मनोरंजक आहेत कारण ते AI एजंट्सना अधिक विस्तृत कार्यक्षमतेची परवानगी देतात. एजंटकडे जे करायची कृतींची मर्यादित सूची आहे त्याऐवजी टूल जोडल्याने, एजंट आता विविध प्रकारच्या क्रिया करू शकतो. या प्रकरणात, आपण टूल वापर डिझाईन पॅटर्न पाहणार आहोत, ज्यामुळे AI एजंट्स विशिष्ट टूल्स वापरून त्यांचे उद्दिष्ट साधू शकतात हे वर्णन होते.

## परिचय

या धड्यात, आपण खालील प्रश्नांची उत्तरे शोधणार आहोत:

- टूल वापर डिझाईन पॅटर्न म्हणजे काय?
- कोणत्या वापरपत्रकांवर हे लागू होऊ शकते?
- या डिझाईन पॅटर्नसाठी कोणकोणते घटक/बिल्डिंग ब्लॉक्स आवश्यक आहेत?
- विश्वसनीय AI एजंट तयार करण्यासाठी टूल वापर डिझाईन पॅटर्न वापरताना कोणती विशेष बाबी लक्षात घ्याव्यात?

## शिक्षणाच्या उद्दिष्टे

हा धडा पूर्ण केल्यावर, आपण पुढील गोष्टी करू शकाल:

- टूल वापर डिझाईन पॅटर्न आणि त्याचा उद्देश परिभाषित करा.
- ज्या वापरपत्रकांवर हा डिझाईन पॅटर्न लागू आहे ते ओळखा.
- डिझाईन पॅटर्न अंमलात आणण्यासाठी आवश्यक मुख्य घटक समजून घ्या.
- या डिझाईन पॅटर्न वापरून AI एजंट्समध्ये विश्वासार्हता सुनिश्चित करण्यासाठीच्या बाबी ओळखा.

## टूल वापर डिझाईन पॅटर्न म्हणजे काय?

**टूल वापर डिझाईन पॅटर्न** LLMs ला विशिष्ट उद्दिष्ट साध्य करण्यासाठी बाह्य टूल्सशी संवाद साधण्याची क्षमता देते. टूल्स म्हणजे कोड जे एजंटद्वारे क्रिया करण्यासाठी चालवता येतात. एक टूल साधी क्रिया असेल जसे की कॅल्क्युलेटर, किंवा तृतीय पक्ष सेवा जसे स्टॉक किंमत शोधणे किंवा हवामानाचा अंदाज, यासाठी API कॉल असू शकतो. AI एजंट्सच्या संदर्भात, टूल एजंटद्वारे **मॉडल-निर्मित फंक्शन कॉल्स** च्या प्रतिसादात चालवले जातात.

## कोणत्या वापरपत्रकांवर हे लागू होऊ शकते?

AI एजंट्स जटिल कामे पूर्ण करण्यासाठी, माहिती मिळवण्यासाठी किंवा निर्णय घेण्यासाठी टूल्सचा लाभ घेऊ शकतात. टूल वापर डिझाईन पॅटर्नचा वापर बहुदा अशा परिस्थितीत केला जातो जिथे बाह्य प्रणालींसह गतिशील संवाद आवश्यक असतो, जसे डेटाबेस, वेब सेवा, किंवा कोड इंटरप्रिटर्स. या क्षमतेचा वापर अनेक विभिन्न वापरपत्रकांसाठी होतो ज्यात समाविष्ट आहे:

- **गतिशील माहिती पुनर्प्राप्ती:** एजंट्स बाह्य API किंवा डेटाबेस चौकशी करू शकतात जसे समसामयिक डेटा मिळविण्यासाठी (उदा. SQLite डेटाबेस डेटा विश्लेषणासाठी, स्टॉक किंमती किंवा हवामान माहिती मिळवणे).
- **कोड अंमलबजावणी आणि व्याख्या:** एजंट्स गणिती समस्यांचे निराकरण, अहवाल तयार करणे किंवा सिम्युलेशन्स करण्यासाठी कोड किंवा स्क्रिप्ट्स चालवू शकतात.
- **वर्कफ्लो ऑटोमेशन:** कार्य वेळापत्रक, ईमेल सेवा किंवा डेटा पाइपलाइनसारख्या टूल्स वापरून पुनरावृत्ती कामे किंवा बहु-टप्प्याचे वर्कफ्लो स्वयंचलित करणे.
- **ग्राहक सेवा:** एजंट्स CRM प्रणाली, तिकीट प्रणाली किंवा ज्ञान भांडारांशी संवाद साधून वापरकर्ता प्रश्न सोडवू शकतात.
- **सामग्री निर्माण आणि संपादन:** एजंट्स व्याकरण तपासक, मजकूर सारांशकार, किंवा सामग्री सुरक्षा मूल्यमापन करणारे टूल्स वापरून सामग्री निर्मितीमध्ये मदत करू शकतात.

## टूल वापर डिझाईन पॅटर्न अंमलात आणण्यासाठी आवश्यक घटक/बिल्डिंग ब्लॉक्स कोणते आहेत?

हे बिल्डिंग ब्लॉक्स AI एजंटला अनेक प्रकारची कामे करण्यास अनुमती देतात. चला टूल वापर डिझाईन पॅटर्न अंमलात आणण्यासाठी आवश्यक मुख्य घटक पाहूया:

- **फंक्शन/टूल स्कीमा:** उपलब्ध टूल्सची तपशीलवार व्याख्या, ज्यात फंक्शन नाव, उद्देश, आवश्यक पॅरामीटर्स आणि अपेक्षित आउटपुट्स यांचा समावेश होतो. हे स्कीमा LLM ला उपलब्ध टूल्स काय आहेत आणि वैध विनंत्या कशा तयार करायच्या हे समजून घेण्यास मदत करतात.

- **फंक्शन अंमलबजावणी लॉजिक:** वापरकर्त्याच्या हेतू आणि संभाषणाच्या संदर्भानुसार टूल्स कधी आणि कसे वापरायचे हे नियंत्रित करते. यात प्लॅनर मॉड्यूल्स, वावटळ व्यवस्था, किंवा निर्देशांक प्रवाह असू शकतात जे टूल वापर गतिशीलपणे ठरवतात.

- **मेसेज हँडलिंग सिस्टम:** वापरकर्ता इनपुट्स, LLM प्रतिसाद, टूल कॉल्स आणि टूल आउटपुट्स यातील संभाषण प्रवाह व्यवस्थापित करणारे घटक.

- **टूल इंटिग्रेशन फ्रेमवर्क:** एजंटला विविध टूल्सशी जोडणारी पायाभूत सुविधा, साधी फंक्शन्स असो किंवा जटिल बाह्य सेवा.

- **त्रुटी हाताळणी आणि प्रमाणीकरण:** टूल अंमलबजावणीत अपयश हाताळणे, पॅरामीटर्सची प्रमाणीकरण करणे, आणि अनपेक्षित प्रतिसाद व्यवस्थापनासाठी यंत्रणा.

- **स्थिती व्यवस्थापन:** संभाषण संदर्भ, आधीच्या टूल संवाद, आणि सातत्य राखण्यासाठी टिकाऊ डेटा ट्रॅक करते.

पुढे, आपण फंक्शन/टूल कॉलिंग याबद्दल अधिक तपशीलवार पाहूया.
 
### फंक्शन/टूल कॉलिंग

फंक्शन कॉलिंग हे LLMs ना टूल्सशी संवाद साधण्यासाठी मुख्य मार्ग आहे. 'फंक्शन' आणि 'टूल' या संज्ञा एकाच अर्थाने वापरल्या जातात कारण 'फंक्शन्स' (पुन्हा वापरता येणाऱ्या कोडचे ब्लॉक्स) हे टूल्स असतात जे एजंट विविध कार्य करायला वापरतात. एखाद्या फंक्शनचे कोड चालवण्यासाठी, LLM ला वापरकर्त्याच्या विनंतीला फंक्शनच्या वर्णनाशी जुळवून पाहावे लागते. यासाठी सर्व उपलब्ध फंक्शन्सची वर्णने असलेले स्कीमा LLM कडे पाठवले जाते. नंतर LLM संबंधित कार्यासाठी साजेसा फंक्शन निवडतो आणि त्याचे नाव व आर्ग्युमेंट्स परत करतो. निवडलेला फंक्शन कॉल केला जातो, त्याचा प्रतिसाद LLM कडे परत पाठवला जातो, जो वापरकर्त्याच्या विनंतीला उत्तर देण्यासाठी वापरला जातो.

डेव्हलपर्सना एजंटसाठी फंक्शन कॉलिंग अंमलात आणण्यासाठी खालील गोष्टी गरजेच्या आहेत:

1. फंक्शन कॉलिंगला समर्थन देणारा LLM मॉडेल
2. फंक्शन वर्णने असलेले स्कीमा
3. प्रत्येक फंक्शनसाठी कोड

शहरातील वर्तमान वेळ मिळवण्याचा उदाहरण वापरून समजून घेऊया:

1. **फंक्शन कॉलिंगला समर्थन देणारा LLM प्रारंभ करा:**

    सर्व मॉडेल्स फंक्शन कॉलिंगला समर्थन देत नाहीत, त्यामुळे वापरत असलेला LLM हा तपासणे महत्त्वाचे आहे. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> फंक्शन कॉलिंगला समर्थन देते. आपण OpenAI क्लायंट सुरू करू शकतो Azure OpenAI **Responses API** वर (स्थिर `/openai/v1/` एंडपॉइंट — `api_version` ची गरज नाही).

    ```python
    # Azure OpenAI साठी OpenAI क्लायंट सुरू करा (Responses API, v1 endpoint)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **फंक्शन स्कीमा तयार करा**:

    पुढे आपण JSON स्कीमा तयार करू ज्यात फंक्शनचे नाव, कार्याचे वर्णन आणि आवश्यक पॅरामीटर्सची नावे व वर्णन असतील.
    नंतर हा स्कीमा क्लायंटला आणि वापरकर्त्याच्या विनंतीला पास करतो, जिथे सॅन फ्रान्सिस्कोचे वेळ माहिती मिळते. लक्षात घ्या की **टूल कॉल** परत मिळतो, **शेवटचे उत्तर नाही**. म्हणून, LLM कार्यासाठी निवडलेले फंक्शनचे नाव आणि त्याचे आर्ग्युमेंट्स परत करतो.

    ```python
    # मॉडेलसाठी फंक्शन वर्णन वाचण्यासाठी (Responses API फ्लॅट टूल स्वरूप)
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
  
    # प्राथमिक वापरकर्ता संदेश
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # प्रथम API कॉल: मॉडेलला फंक्शन वापरण्याचा आग्रह करा
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API प्रतिक्रियेत function_call आयटम्स म्हणून टूल कॉल्स परत करतो response.output मध्ये.
    # त्यांना संभाषणात जोडावे ज्यामुळे मॉडेलला पुढील टप्प्यात पूर्ण संदर्भ मिळेल.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **कार्य पार पाडण्यासाठी आवश्यक फंक्शन कोड:**

    LLM ने फंक्शन निवडल्यानंतर, काम पार पाडणारा कोड तयार करावा व चालवावा लागतो.
    आपण Python मध्ये वर्तमान वेळ मिळवण्यासाठी कोड तयार करू. तसेच response_message मधून नाव आणि आर्ग्युमेंट्स काढण्यासाठी कोड लिहावा लागेल ज्याने अंतिम परिणाम मिळेल.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # टूलचा निकाल function_call_output आयटेम म्हणून परत करा
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # दुसरा API कॉल: मॉडेलकडून अंतिम प्रतिसाद मिळवा
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

फंक्शन कॉलिंग हा जास्तीत जास्त एजंट टूल वापर डिझाईनचा मुख्य भाग आहे, परंतु याला सुरुवातीपासून तयार करणे कधीकधी आव्हानात्मक असू शकते.
आपल्याला [धडा 2](../../../02-explore-agentic-frameworks) मध्ये शिकले तसे एजंटिक फ्रेमवर्क्स आपल्याला टूल वापर अंमलात आणण्यासाठी पूर्वनिर्मित बिल्डिंग ब्लॉक्स पुरवतात.
 
## एजंटिक फ्रेमवर्क्ससह टूल वापर उदाहरणे

येथे विविध एजंटिक फ्रेमवर्क्स वापरून टूल वापर डिझाईन पॅटर्न कसा अंमलात आणता येतो त्याची काही उदाहरणे आहेत:

### Microsoft एजंट फ्रेमवर्क

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft एजंट फ्रेमवर्क</a> हे AI एजंट्स तयार करण्यासाठी ओपन-सोर्स फ्रेमवर्क आहे. हे फंक्शन कॉलिंग वापरणी सोपी करते, ज्यात आपण टूल्सना Python फंक्शन्स म्हणून `@tool` डेकोरेटर वापरुन परिभाषित करू शकतो. हे फ्रेमवर्क मॉडेल आणि तुमच्या कोडमधील संवाद हाताळते. तसेच, File Search आणि Code Interpreter सारखे पूर्वनिर्मित टूल्स `FoundryChatClient` मार्फत उपलब्ध करून देते.

खालील आकृती Microsoft एजंट फ्रेमवर्कसह फंक्शन कॉलिंग प्रक्रियेचं दर्शन घडवते:

![function calling](../../../translated_images/mr/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft एजंट फ्रेमवर्कमध्ये, टूल्स डेकोरेटेड फंक्शन्स म्हणून परिभाषित केल्या जातात. आपण पूर्वी पाहिलेला `get_current_time` फंक्शन `@tool` डेकोरेटर वापरून टूलमध्ये रूपांतरित करू शकतो. फ्रेमवर्क आपोआप फंक्शन व त्याचे पॅरामीटर्स सीरिअलाइज करून LLM कडे पाठवायला स्कीमा तयार करेल.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# क्लायंट तयार करा
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# एक एजंट तयार करा आणि साधनासह चालवा
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry एजंट सेवा

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry एजंट सेवा</a> ही एक नवीन एजंटिक फ्रेमवर्क आहे जी डेव्हलपर्सना सुरक्षितपणे उच्च दर्जाचे आणि विस्तारयोग्य AI एजंट्स तयार, तैनात आणि मापन करण्यास सशक्त करते, ज्यासाठी तुम्हाला अंतर्गत संगणकीय संसाधने आणि संग्रह व्यवस्थापित करण्याची गरज नाही. ती उद्योजकीय अनुप्रयोगांसाठी विशेषतः उपयुक्त आहे कारण ही पूर्णपणे व्यवस्थापित सेवा असून उद्योजकीय दर्जाची सुरक्षा पुरवते.

LLM API सोबत तुलना करता, Microsoft Foundry एजंट सेवा खालील फायदे देते:

- स्वयंचलित टूल कॉलिंग – टूल कॉल पार्स करणे, टूल चालवणे आणि प्रतिसाद हाताळण्याची गरज नाही; हे सर्व आता सर्व्हर बाजूने होते
- सुरक्षितपणे व्यवस्थापित डेटा – संभाषण स्थिती स्वतः व्यवस्थापित करण्याऐवजी तुम्ही थ्रेड्सवर अवलंबून राहू शकता जी आवश्यक सर्व माहिती साठवतात
- रेडी-टू-यूज टूल्स – Bing, Azure AI Search, आणि Azure Functions सारख्या डेटा स्रोतांशी संवाद साधण्यासाठी टूल्स

Microsoft Foundry एजंट सेवेमध्ये उपलब्ध टूल्स दोन श्रेणीत विभागले आहेत:

1. ज्ञान टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing शोधासह ग्राउंडिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">फाइल शोध</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI शोध</a>

2. क्रिया टूल्स:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">फंक्शन कॉलिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इंटरप्रिटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित टूल्स</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure फंक्शन्स</a>

एजंट सेवा आपल्याला या टूल्सना `toolset` म्हणून एकत्र वापरण्याची परवानगी देते. तसेच `threads` चा वापर करते जे विशिष्ट संभाषणातील संदेश इतिहास राखतात.

गृहित धरा की तुम्ही Contoso नावाच्या कंपनीतील विक्री एजंट आहात. तुम्हाला एक संवादात्मक एजंट तयार करायचा आहे जो तुमच्या विक्री डेटाबद्दल प्रश्नांची उत्तरे देऊ शकेल.

खालील प्रतिमा Microsoft Foundry एजंट सेवा वापरून तुमच्या विक्री डेटाचे विश्लेषण कसे करता येईल हे दाखवते:

![Agentic Service In Action](../../../translated_images/mr/agent-service-in-action.34fb465c9a84659e.webp)

या सेवेद्वारे कोणतेही टूल वापरण्यासाठी आपण ग्राहक तयार करू शकतो आणि टूल किंवा टूलसेट परिभाषित करू शकतो. व्यवहारिक रूपात यासाठी पुढील Python कोड वापरू शकतो. LLM टूलसेट पहातो आणि वापरकर्त्याच्या विनंतीनुसार वापरकर्ता तयार केलेला फंक्शन `fetch_sales_data_using_sqlite_query` किंवा पूर्वनिर्मित कोड इंटरप्रिटर वापरण्याचा निर्णय घेतो.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query फंक्शन जे fetch_sales_data_functions.py फाईलमध्ये सापडेल.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# टूलसेट सुरू करा
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query फंक्शनसह फंक्शन कॉलिंग एजंट सुरू करा आणि त्याला टूलसेटमध्ये जोडा
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# कोड इंटरप्रिटर टूल सुरू करा आणि त्याला टूलसेटमध्ये जोडा.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## विश्वासार्ह AI एजंट तयार करण्यासाठी टूल वापर डिझाईन पॅटर्न वापरात विशेष बाबी कोणत्या आहेत?

LLMs द्वारे डायनॅमिकली तयार केलेल्या SQL मध्ये सामान्य चिंता म्हणजे सुरक्षा, विशेषतः SQL इंजेक्शनचा धोका किंवा दुर्भावनायुक्त क्रियाकलाप जसे डेटा बेस ड्रॉप करणे किंवा छेडछाड करणे. या चिंता बरोबर असल्या तरी, योग्य डेटाबेस प्रवेश परवानग्या सेट केल्यास त्यांचा प्रभावीपणे प्रतिबंध करता येतो. बहुतेक डेटाबेससाठी हे डेटाबेसला फक्त वाचन-केवल मोडमध्ये कॉन्फिगर करणे अपेक्षित आहे. PostgreSQL किंवा Azure SQL सारख्या डेटाबेस सेवांसाठी, अॅपला फक्त फक्त वाचन-परवानगी (SELECT) असलेली भूमिका दिली पाहिजे.

अॅपला सुरक्षित वातावरणात चालविल्यास सुरक्षा आणखी वाढते. उद्योजकीय परिस्थितीत डेटाचा वापर सहसा चालू प्रणालींपासून गोळा करून वाचन-केवल डेटाबेस किंवा डेटा वेअरहाऊस मध्ये रूपांतरित केला जातो, ज्यात वापरकर्ता-अनुकूल स्कीमा असतो. या पद्धतीमुळे डेटा सुरक्षित, कार्यक्षमतेसाठी अनुकूल आणि अॅपला मर्यादित वाचन-परवानगी मिळते याची खात्री होते.

## नमुना कोड्स

- Python: [एजंट फ्रेमवर्क](./code_samples/04-python-agent-framework.ipynb)
- .NET: [एजंट फ्रेमवर्क](./code_samples/04-dotnet-agent-framework.md)

## टूल वापर डिझाईन पॅटर्नबाबत अजून प्रश्न आहेत का?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मध्ये सामील व्हा, इतर शिकणाऱ्यांशी भेटा, ऑफिस आवर्समध्ये सहभागी व्हा आणि तुमचे AI एजंट्सबाबत प्रश्नांचे उत्तर मिळवा.

## अतिरिक्त साधने

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI एजंट सेवा कार्यशाळा</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso क्रिएटिव रायटर मल्टि-एजंट कार्यशाळा</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft एजंट फ्रेमवर्क विषद</a>


## या एजंटचे स्मोक-टेस्टिंग (ऐच्छिक)

[Lesson 16](../16-deploying-scalable-agents/README.md) मध्ये एजंट कसे तैनात करायचे ते शिकल्यानंतर, तुम्ही या धड्याचा `TravelToolAgent` (तो अजूनही त्याचे टूल्स कॉल करतो आणि उत्तर देतो का?) [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) वापरून स्मोक-टेस्ट करू शकता. ते कसे चालवायचे ते पाहण्यासाठी [`tests/README.md`](../tests/README.md) पहा.

## मागील धडा

[Agentic Design Patterns समजून घेणे](../03-agentic-design-patterns/README.md)

## पुढील धडा

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->