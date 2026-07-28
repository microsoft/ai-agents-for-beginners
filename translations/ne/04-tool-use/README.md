[![कसरी राम्रो AI एजेन्टहरू डिजाइन गर्ने](../../../translated_images/ne/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(यो पाठको भिडियो हेर्न माथिको तस्वीरमा क्लिक गर्नुहोस्)_

# टुल प्रयोग डिजाइन ढाँचा

टुलहरू रोचक छन् किनकि तिनीहरूले AI एजेन्टहरूलाई व्यापक क्षमताहरू दिन्छन्। एजेन्टसँग सीमित क्रियाहरूको सट्टा, टुल थप्दा एजेन्टले धेरै प्रकारका क्रियाहरू गर्न सक्छ। यस अध्यायमा, हामी टुल प्रयोग डिजाइन ढाँचालाई हेरौं, जुनले AI एजेन्टहरूले कसरी विशेष टुलहरू प्रयोग गरी आफ्नो लक्ष्यहरू प्राप्त गर्न सक्छन् भनेर वर्णन गर्छ।

## परिचय

यस पाठमा, हामी निम्न प्रश्नहरूको उत्तर दिन खोजिरहेका छौं:

- टुल प्रयोग डिजाइन ढाँचा के हो?
- यसलाई कुन प्रयोग केसहरूमा लागू गर्न सकिन्छ?
- यस डिजाइन ढाँचालाई लागू गर्न आवश्यक तत्वहरू/निर्माण ब्लकहरू के-के छन्?
- विश्वसनीय AI एजेन्ट बनाउन टुल प्रयोग डिजाइन ढाँचा प्रयोग गर्दा के विशेष ध्यान दिनुपर्छ?

## सिकाइ लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं सक्षम हुनुहुनेछ:

- टुल प्रयोग डिजाइन ढाँचाको परिभाषा र यसको उद्देश्य वर्णन गर्न।
- टुल प्रयोग डिजाइन ढाँचा लागू गर्न सकिने प्रयोग केसहरू पहिचान गर्न।
- डिजाइन ढाँचा लागू गर्न आवश्यक मुख्य तत्वहरू बुझ्न।
- यस डिजाइन ढाँचाको प्रयोग गरेर AI एजेन्टहरूको विश्वसनीयता सुनिश्चित गर्न ध्यान दिनुपर्ने कुराहरू पहिचान गर्न।

## टुल प्रयोग डिजाइन ढाँचा के हो?

**टुल प्रयोग डिजाइन ढाँचा** LLM हरुलाई बाह्य टुलहरूसँग अन्तरक्रिया गर्न सक्ने क्षमता दिनमा केन्द्रित छ, जसले विशेष लक्ष्यहरू पूरा गर्न मद्दत गर्छ। टुल भनेको कोड हुन्छ जुन एजेन्टले क्रिया गर्न प्रयोग गर्न सक्छ। टुल साधारण उदाहरणका लागि गणना गर्ने फलन वा तेस्रो पक्षको सेवा जस्तै शेयर मूल्य खोज्ने वा मौसम पूर्वानुमान गर्ने API कल हुन सक्छ। AI एजेन्टहरूको सन्दर्भमा, टुलहरू एजेन्टले **मोडल-जनरेटेड फलन कलहरू** को प्रतिक्रियामा चलाउने गरी डिजाइन गरिन्छ।

## यसलाई कुन प्रयोग केसहरूमा लागू गर्न सकिन्छ?

AI एजेन्टहरूले टुलहरू प्रयोग गरेर जटिल कार्यहरू पूरा गर्न, जानकारी प्राप्त गर्न, वा निर्णय लिन सक्छन्। टुल प्रयोग डिजाइन ढाँचा प्रायः यस्ता परिदृश्यहरूमा प्रयोग गरिन्छ जहाँ बाह्य प्रणालीहरू जस्तै डेटाबेस, वेब सेवा, वा कोड व्याख्याकारहरूसँग गतिशील अन्तरक्रिया आवश्यक हुन्छ। यसले विभिन्न प्रयोग केसहरूमा उपयुक्त हुन्छ जस्तै:

- **गतिशील जानकारी प्राप्ति:** एजेन्टहरूले बाह्य API वा डेटाबेसबाट हालको डाटा सोध्न सक्छन् (जस्तै डेटा विश्लेषणका लागि SQLite डेटाबेस सोध्नु, शेयर मूल्य वा मौसम जानकारी ल्याउनु)।
- **कोड कार्यान्वयन र व्याख्या:** एजेन्टहरूले गणितीय समस्या समाधान गर्न, प्रतिवेदन बनाउन, वा अनुकरणहरू गर्ने कोड वा स्क्रिप्ट चलाउन सक्छन्।
- **कार्यप्रवाह स्वचालन:** कार्य अनुसूचक, इमेल सेवा, वा डेटा पाइपलाइन जस्ता टुलहरू एकीकृत गरेर दोहोरिने वा बहु-चरण कार्यप्रवाहहरू स्वचालित बनाउने।
- **ग्राहक समर्थन:** एजेन्टहरूले CRM प्रणाली, टिकटिङ प्लेटफर्म, वा ज्ञान आधारसँग अन्तरक्रिया गरी प्रयोगकर्ताका प्रश्नहरू समाधान गर्ने।
- **सामग्री सिर्जना र सम्पादन:** एजेन्टहरूले व्याकरण जाँच्ने, पाठ संक्षेप गर्ने, वा सामग्री सुरक्षा मूल्याङ्कन गर्ने टुलहरू प्रयोग गरी सामग्री सिर्जनामा सहयोग गर्ने।

## टुल प्रयोग डिजाइन ढाँचा लागू गर्न आवश्यक तत्वहरू/निर्माण ब्लकहरू के-के हुन्?

यी निर्माण ब्लकहरूले AI एजेन्टलाई फराकिलो कार्यहरू गर्न सक्षम बनाउँछन्। टुल प्रयोग डिजाइन ढाँचा लागू गर्न आवश्यक मुख्य तत्वहरू हेरौं:

- **फलन/टुल स्किमाहरू:** उपलब्ध टुलहरूको विस्तृत परिभाषा जस्तै फलन नाम, उद्देश्य, आवश्यक प्यारामिटरहरू, र अपेक्षित आउटपुटहरू। यी स्किमाहरूले LLM लाई कुन टुल उपलब्ध छ र कसरि मान्य अनुरोध बनाउने बुझ्न मद्दत गर्छ।

- **फलन कार्यान्वयन तर्क:** प्रयोगकर्ताको उद्देश्य र संवाद सन्दर्भमा आधारित भएर टुलहरू कहिले र कसरी बोलाउनु हुन्छ भन्ने निर्धारण गर्ने। यसमा योजना बनाउने मोड्युलहरू, राउटिङ मेकानिजमहरू, वा सर्तीय प्रवाहहरू हुन सक्छन् जुन टुल प्रयोग गतिशील बनाउँछन्।

- **सन्देश व्यवस्थापन प्रणाली:** प्रयोगकर्ता इनपुटहरू, LLM प्रतिक्रिया, टुल कलहरू, र टुल आउटपुटहरू बीच संवाद बहाव व्यवस्थापन गर्ने कम्पोनेन्टहरू।

- **टुल एकीकरण फ्रेमवर्क:** एजेन्टलाई विभिन्न टुलहरूसँग जडान गर्ने पूर्वाधार, चाहे ती साधारण फलन हुन् वा जटिल बाह्य सेवा।

- **त्रुटि व्यवस्थापन र प्रमाणीकरण:** टुल कार्यान्वयनमा असफलता, प्यारामिटर प्रमाणीकरण, र अप्रत्याशित प्रतिक्रियाहरू व्यवस्थापन गर्ने संयन्त्रहरू।

- **स्थिति व्यवस्थापन:** संवाद सन्दर्भ, अघिल्लो टुल अन्तरक्रिया, र दीर्घकालीन डाटालाई ट्र्याक गरेर बहु-पटक संवादहरूमा स्थिरता सुनिश्चित गर्ने।

अब, फलन/टुल कलिङलाई बढी विस्तारमा हेरौं।
 
### फलन/टुल कलिङ

फलन कलिङ मुख्य तरिका हो जसले हामीलाई ठूला भाषिक मोडेलहरू (LLM) लाई टुलहरूसँग अन्तरक्रिया गर्न सक्षम बनाउँछ। तपाईंले प्रायः 'फलन' र 'टुल' लाई समरूप रूपमा देख्नुहुनेछ किनकि 'फलनहरू' (पुन: प्रयोग गर्न मिल्ने कोड ब्लकहरू) नै एजेन्टहरूले कार्यहरू गर्न प्रयोग गर्ने 'टुल' हुन्। एउटा फलनको कोड बोलाउनको लागि, LLM ले प्रयोगकर्ताको अनुरोधलाई फलनको वर्णनसँग तुलना गर्नुपर्छ। यसको लागि, उपलब्ध सबै फलनहरूको वर्णन समावेश गर्ने स्किमा LLM लाई पठाइन्छ। LLM त्यसपछि कार्यका लागि सबैभन्दा उपयुक्त फलन चयन गरी यसको नाम र आर्गुमेन्टहरू फिर्ता गर्छ। चयन गरिएको फलन बोलाइन्छ, यसको प्रतिक्रिया LLM लाई पठाइन्छ, जुन प्रयोगकर्ताको अनुरोधको जवाफ दिन प्रयोग हुन्छ।

विकासकर्ताहरूले एजेन्टहरूको लागि फलन कलिङ कार्यान्वयन गर्नका लागि आवश्यक छ:

1. फलन कलिङ समर्थन गर्ने LLM मोडेल
2. फलन वर्णनहरू सहितको स्किमा
3. प्रत्येक वर्णन गरिएको फलनको कोड

शहरमा हालको समय प्राप्त गर्ने उदाहरण प्रयोग गरौं:

1. **फलन कलिङ समर्थन गर्ने LLM सुरू गर्नुहोस्:**

    सबै मोडेलहरूले फलन कलिङ समर्थन नगर्न सक्छन्, त्यसैले तपाईं प्रयोग गरिरहेको LLM ले गर्छ कि गर्दैन जाँच गर्नु महत्वपूर्ण छ।     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ले फलन कलिङ समर्थन गर्दछ। हामी Azure OpenAI **प्रतिक्रिया API** (स्थिर `/openai/v1/` अन्तबिन्दु — कुनै `api_version` आवश्यक छैन) विरुद्ध OpenAI क्लाइन्ट सुरु गरेर सुरु गर्न सक्छौं। 

    ```python
    # Azure OpenAI (Responses API, v1 endpoint) का लागि OpenAI क्लाइन्ट प्रारम्भ गर्नुहोस्
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **फलन स्किमा सिर्जना गर्नुहोस्**:

    अब हामी JSON स्किमा परिभाषित गर्नेछौं जसमा फलनको नाम, फलनले के गर्छ भन्ने वर्णन, र फलनका प्यारामिटरहरूको नाम र वर्णन हुन्छ। 
    हामी यो स्किमालाई पहिले सिर्जना गरिएको क्लाइन्टलाई र प्रयोगकर्ताको अनुरोध (San Francisco मा समय जान्नको लागि) सँग पठाउनेछौं। महत्वपुर्ण कुरा भनेको **टुल कल** फिर्ता हुन्छ, **प्रश्नको अन्तिम उत्तर होइन**। पहिले उल्लिखित अनुसार, LLM ले कार्यका लागि चयन गरेको फलनको नाम र त्यसलाई पठाइने आर्गुमेन्ट फिर्ता गर्दछ।

    ```python
    # मोडेलले पढ्नको लागि कार्य विवरण (प्रतिसाद API फ्ल्याट उपकरण ढाँचा)
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
  
    # प्रारम्भिक प्रयोगकर्ता सन्देश
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # पहिलो API कल: मोडेललाई फंक्शन प्रयोग गर्न आग्रह गर्नुहोस्
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API ले प्रतिक्रिया.output मा function_call वस्तुहरू रूपमा उपकरण कलहरू फिर्ता गर्दछ।
    # तिनीहरूलाई कुराकानीमा थप्नुहोस् ताकि मोडेलसँग अर्को पालोमा पूर्ण सन्दर्भ होस्।
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **कार्य सम्पन्न गर्न आवश्यक फलन कोड:**

    अब जब LLM ले कुन फलन चलाउनु पर्ने छ चयन गरेको छ, कार्य सम्पन्न गर्ने कोड कार्यान्वयन र चलाउनु पर्छ।
    हामी Python मा वर्तमान समय प्राप्त गर्ने कोड कार्यान्वयन गर्न सक्छौं। साथै, अन्तिम नतिजा प्राप्त गर्न response_message बाट नाम र आर्गुमेन्टहरू निकाल्ने कोड पनि लेख्नुपर्छ।

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
    # फंक्शन कलहरू ह्यान्डल गर्नुहोस्
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # उपकरण परिणामलाई function_call_output वस्तुको रूपमा फर्काउनुहोस्
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # दोस्रो API कल: मोडेलबाट अन्तिम प्रतिक्रिया प्राप्त गर्नुहोस्
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

फन्क्शन कलिंग अधिकांश, यदि सबै होइन भने, एजेन्ट उपकरण प्रयोग डिजाइनको मुटु हो, यद्यपि यसलाई सुरुबाट कार्यान्वयन गर्नु कहिलेकाहीं चुनौतीपूर्ण हुन सक्छ।
जस्तै हामीले [पाठ २](../../../02-explore-agentic-frameworks) मा सिक्यौं, एजेन्टिक फ्रेमवर्कहरूले उपकरण प्रयोग कार्यान्वयन गर्न पूरै तयार ब्लकहरू प्रदान गर्छन्।
 
## एजेन्टिक फ्रेमवर्कहरूसँग उपकरण प्रयोगका उदाहरणहरू

यहाँ विभिन्न एजेन्टिक फ्रेमवर्कहरू प्रयोग गरेर उपकरण प्रयोग डिजाइन ढाँचा कसरी कार्यान्वयन गर्ने केही उदाहरणहरू छन्:

### माइक्रोसफ्ट एजेन्ट फ्रेमवर्क

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">माइक्रोसफ्ट एजेन्ट फ्रेमवर्क</a> AI एजेन्टहरू बनाउनको लागि खुला स्रोत AI फ्रेमवर्क हो। यसले फन्क्शन कलिंग प्रयोग गर्न सजिलो बनाउँछ किनभने तपाईंले उपकरणहरूलाई `@tool` डेकोरेटरसँग पाइथन फन्क्शनका रूपमा परिभाषित गर्न सक्नुहुन्छ। फ्रेमवर्कले मोडल र तपाईंको कोडको बीचमा फर्किने-जान्ने सञ्चार व्यवस्थित गर्छ। यसले `FoundryChatClient` मार्फत फाइल खोज र कोड इन्टरप्रेटर जस्ता तयार उपकरणहरूमा पहुँच पनि प्रदान गर्छ।

तलको चित्रले माइक्रोसफ्ट एजेन्ट फ्रेमवर्कसँग फन्क्शन कलिंग प्रक्रियालाई देखाउँछ:

![function calling](../../../translated_images/ne/functioncalling-diagram.a84006fc287f6014.webp)

माइक्रोसफ्ट एजेन्ट फ्रेमवर्कमा, उपकरणहरू डेकोरेटेड फन्क्शनहरूका रूपमा परिभाषित गरिन्छन्। हामीले पहिले देखेको `get_current_time` फन्क्शनलाई `@tool` डेकोरेटर प्रयोग गरेर टूलमा रूपान्तरण गर्न सक्छौं। फ्रेमवर्कले फन्क्शन र यसको प्यारामिटरहरूलाई स्वचालित रूपमा सिरियलाइज गरेर LLM लाई पठाउनको लागि स्किमालाई बनाउँछ।

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# क्लाइन्ट सिर्जना गर्नुहोस्
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# एजेन्ट सिर्जना गर्नुहोस् र उपकरणसँग चलाउनुहोस्
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### माइक्रोसफ्ट फाउन्ड्री एजेन्ट सेवा

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">माइक्रोसफ्ट फाउन्ड्री एजेन्ट सेवा</a> एक नयाँ एजेन्टिक फ्रेमवर्क हो जसले विकासकर्ताहरूलाई सुरक्षित रूपमा उच्च गुणस्तरको, विस्तारयोग्य AI एजेन्टहरू निर्माण, तैनाथ, र स्केल गर्न सक्षम पार्छ, जुन आधारभूत कम्प्युट र स्टोरेज स्रोत व्यवस्थापन बिना नै सम्भव हुन्छ। यो विशेष गरी उद्यम अनुप्रयोगहरूका लागि उपयोगी छ किनभने यो पूर्ण व्यवस्थापन गरिएको सेवा हो र उद्यम स्तरको सुरक्षा प्रदान गर्छ।

LLM API सँग प्रत्यक्ष विकास गर्ने सन्दर्भमा, माइक्रोसफ्ट फाउन्ड्री एजेन्ट सेवाले केही फाइदाहरू प्रदान गर्दछ, जस्तै:

- स्वचालित उपकरण कलिंग – टूल कल पार्स गर्न, उपकरण आह्वान गर्न, र प्रतिक्रिया व्यवस्थापन गर्न आवश्यक छैन; यी सबै अब सर्भर साइडमाै हुन्छन्
- सुरक्षित रूपमा व्यवस्थापित डेटा – तपाईंले आफ्नो वार्तालाप स्थिति व्यवस्थापन गर्नुपर्ने ठाउँमा, थ्रेडहरूमा सबै जानकारी भण्डारण गर्न सक्नुहुन्छ
- तत्क्षण प्रयोग गर्न सकिने उपकरणहरू – Bing, Azure AI Search, र Azure Functions जस्ता डेटा स्रोतहरूसँग अन्तरक्रिया गर्न प्रयोग गर्न सकिने उपकरणहरू

माइक्रोसफ्ट फाउन्ड्री एजेन्ट सेवामा उपलब्ध उपकरणहरू दुई वर्गमा विभाजन गर्न सकिन्छ:

१. ज्ञान उपकरणहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search द्वारा आधार प्रदान गर्ने</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">फाइल खोज</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI खोज</a>

२. कार्य उपकरणहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">फन्क्शन कलिंग</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इन्टरप्रेटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित उपकरणहरू</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

एजेन्ट सेवालाई यी उपकरणहरूलाई `toolset` का रूपमा प्रयोग गर्न अनुमति दिन्छ। यसले `threads` पनि प्रयोग गर्दछ जसले एक विशेष वार्तालापको संदेशहरूको इतिहास ट्र्याक गर्दछ।

कल्पना गर्नुहोस् तपाईं Contoso नामक कम्पनीमा सेल्स एजेन्ट हुनुहुन्छ। तपाईं एउटा संवादात्मक एजेन्ट विकास गर्न चाहनुहुन्छ जुन तपाईंको बिक्री डाटाबारे प्रश्नहरूको उत्तर दिन सकोस्।

तलको छवि देखाउँछ कसरी माइक्रोसफ्ट फाउन्ड्री एजेन्ट सेवा प्रयोग गरेर तपाईंले आफ्नो बिक्री डाटा विश्लेषण गर्न सक्नुहुन्छ:

![Agentic Service In Action](../../../translated_images/ne/agent-service-in-action.34fb465c9a84659e.webp)

यी कुनै पनि उपकरणहरू सेवा संग प्रयोग गर्न, हामी क्लाइन्ट बनाउन सक्छौँ र उपकरण वा उपकरण सेट निर्दिष्ट गर्न सक्छौँ। व्यवहारमा यसलाई कार्यान्वयन गर्न हामी तलको पाइथन कोड प्रयोग गर्न सक्छौं। LLM ले उपकरण सेट हेरेर प्रयोगकर्ताले बनाएको `fetch_sales_data_using_sqlite_query` फन्क्शन प्रयोग गर्ने वा प्रि-बिल्ट कोड इन्टरप्रेटर प्रयोग गर्ने निर्णय लिन सक्छ।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query फंक्शन जुन fetch_sales_data_functions.py फाइलमा फेला पार्न सकिन्छ।
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# उपकरण सेट सुरु गर्नुहोस्
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query फंक्शनसहित फंक्शन कलिंग एजेन्ट सुरु गर्नुहोस् र यसलाई उपकरण सेटमा थप्नुहोस्
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# कोड इन्टरप्रेटर उपकरण सुरु गर्नुहोस् र यसलाई उपकरण सेटमा थप्नुहोस्।
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## भरोसायोग्य AI एजेन्टहरू निर्माण गर्न उपकरण प्रयोग डिजाइन ढाँचाको के विशेष विचारहरू छन्?

LLM बाट गतिशील रूपमा निर्मित SQL मा सामान्य चिन्ता भनेको सुरक्षा हो, विशेष गरी SQL इन्जेक्शन वा दुष्ट कार्यहरूको जोखिम, जस्तै डेटाबेस ड्रप गर्ने वा छेडछाड गर्ने। यी चिन्ताहरू उचित रूपमा डाटाबेस पहुँच अनुमतिहरू कन्फिगर गरेर प्रभावकारी रूपमा कम गर्न सकिन्छ। अधिकांस डेटाबेसहरूलाई पढ्न मात्र (read-only) कन्फिगर गर्ने कुरा पर्दछ। PostgreSQL वा Azure SQL जस्ता डेटाबेस सेवाहरूमा, एपलाई पढ्न मात्र (SELECT) अधिकार असाइन गर्नुपर्छ।

एपलाई सुरक्षित वातावरणमा चलाउनुले सुरक्षा अझ बढाउँछ। उद्यम परिदृश्यहरूमा, डेटा प्रायः सञ्चालन प्रणालीहरूबाट निकालेर पढ्न मात्र डाटाबेस वा डाटा वेयरहाउसमा रूपान्तरण गरिन्छ जसको एक प्रयोगकर्ता मैत्री स्किमामा उपलब्ध हुन्छ। यसले डेटालाई सुरक्षित, प्रदर्शन र पहुँचका लागि अनुकूलित राख्दछ र एपलाई सीमित, पढ्न मात्र पहुँच दिन्छ।

## नमूना कोडहरू

- पाइथन: [एजेन्ट फ्रेमवर्क](./code_samples/04-python-agent-framework.ipynb)
- .NET: [एजेन्ट फ्रेमवर्क](./code_samples/04-dotnet-agent-framework.md)

## उपकरण प्रयोग डिजाइन ढाँचाबारे थप प्रश्नहरू छन्?

अन्य सिक्नेहरूसँग भेट्न, अफिस आवरहरूमा सहभागी हुन र तपाईंका AI एजेन्ट प्रश्नहरू सोध्न [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मा सहभागी हुनुहोस्।

## थप स्रोतहरू

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service कार्यशाला</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer बहु-एजेन्ट कार्यशाला</a>

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">माइक्रोसफ्ट एजेन्ट फ्रेमवर्क अवलोकन</a>


## यस एजेन्टको स्मोक-टेस्टिंग (वैकल्पिक)

तपाईंले [पाठ १६](../16-deploying-scalable-agents/README.md) मा एजेन्टहरू कसरी तैनाथ गर्ने सिक्नुभयो भने, तपाईंले यस पाठको `TravelToolAgent` (के यो अझै यसको उपकरणहरू कल गर्छ र उत्तर दिन्छ?) लाई [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) सँग स्मोक-टेस्ट गर्न सक्नुहुन्छ। यसलाई कसरी चलाउने भनेर हेर्न [`tests/README.md`](../tests/README.md) हेर्नुहोस्।

## अघिल्लो पाठ

[एजेण्टिक डिजाइन ढाँचा बुझ्दै](../03-agentic-design-patterns/README.md)

## अर्को पाठ

[एजेण्टिक RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->