[![कसरी राम्रो AI एजेन्ट डिजाइन गर्ने](../../../translated_images/ne/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(यो पाठको भिडियो हेर्न माथि रहेको छवि क्लिक गर्नुहोस्)_

# उपकरण प्रयोग डिजाइन ढाँचा

उपकरणहरू रोचक छन् किनभने तिनीहरूले AI एजेन्टहरूलाई व्यापक प्रकारका क्षमताहरू प्रदान गर्छन्। एजेन्टसँग सीमित क्रियाहरूको सेट हुनुपर्ने सट्टा, उपकरण थप्दा एजेन्टले धेरै किसिमका क्रियाहरू गर्न सक्छ। यस अध्यायमा, हामी उपकरण प्रयोग डिजाइन ढाँचा हेरिरहेका छौं, जसले AI एजेन्टहरूले तिनीहरूको लक्ष्य प्राप्त गर्न कसरी विशिष्ट उपकरणहरू प्रयोग गर्न सक्छन् भन्ने वर्णन गर्दछ।

## परिचय

यस पाठमा, हामी तलका प्रश्नहरूको उत्तर खोज्नेछौं:

- उपकरण प्रयोग डिजाइन ढाँचा के हो?
- यसलाई कुन प्रयोग केसहरूमा लागू गर्न सकिन्छ?
- डिजाइन ढाँचा लागू गर्न आवश्यक तत्वहरू/निर्माण खण्डहरू के के हुन्?
- विश्वसनीय AI एजेन्ट बनाउन उपकरण प्रयोग डिजाइन ढाँचाको प्रयोग गर्दा कुन विशेष विचारहरू ध्यानमा राख्नुपर्छ?

## सिकाइ लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं सक्षम हुनुभयो:

- उपकरण प्रयोग डिजाइन ढाँचा र यसको उद्देश्य परिभाषित गर्न।
- उपकरण प्रयोग डिजाइन ढाँचा लागू हुने प्रयोग केसहरू पहिचान गर्न।
- डिजाइन ढाँचा लागू गर्न आवश्यक मुख्य तत्वहरू बुझ्न।
- यस डिजाइन ढाँचाको प्रयोग गर्ने AI एजेन्टहरूमा विश्वसनीयता सुनिश्चित गर्न विचार गर्नुपर्ने कुराहरू चिन्न।

## उपकरण प्रयोग डिजाइन ढाँचा के हो?

**उपकरण प्रयोग डिजाइन ढाँचा** LLM हरूलाई बाह्य उपकरणहरूसँग अन्तरक्रिया गर्न सक्ने क्षमता दिन केन्द्रित छ जसले विशिष्ट लक्ष्यहरू प्राप्त गर्न सहयोग गर्छ। उपकरणहरू एजेन्टले कार्यहरू गर्न सक्छ भनेर कोडहरू हुन्। एउटा उपकरण सामान्य गणक (calculator) जस्तो साधारण फङ्क्शन हुन सक्छ, वा तेस्रो-पाटी सेवाको API जस्तै स्टक मूल्य हेर्न वा मौसम पूर्वानुमान लिनको लागि कल हुन सक्छ। AI एजेन्टहरूको सन्दर्भमा, उपकरणहरू **मोडेल-द्वारा उत्पन्न फङ्क्शन कलहरू** को जवाफमा एजेन्टहरूले चलाउने गरी डिजाइन गरिएका हुन्छन्।

## यसलाई कुन प्रयोग केसहरूमा लागू गर्न सकिन्छ?

AI एजेन्टहरूले जटिल कार्यहरू पूरा गर्न, जानकारी प्राप्त गर्न, वा निर्णय लिन उपकरणहरूको उपयोग गर्न सक्छन्। उपकरण प्रयोग डिजाइन ढाँचा प्रायः डायनामिक अन्तरक्रिया आवश्यक पर्ने परिस्थितिहरूमा प्रयोग गरिन्छ, जस्तै डेटाबेस, वेब सेवा, वा कोड व्याख्याता संग अन्तरक्रिया। यस क्षमताले विभिन्न प्रयोग केसहरूको लागि उपयोगी छ जस्तै:

- **डायनामिक जानकारी प्राप्ति:** एजेन्टहरूले बाह्य API वा डेटाबेसहरूलाई सोध्न सक्छन् र ताजा डेटा ल्याउन सक्छन् (जस्तै SQLite डेटाबेसमा प्रश्न सोधेर डेटा विश्लेषण, स्टक मूल्य वा मौसम जानकारी प्राप्त गर्न)।
- **कोड निष्पादन र व्याख्या:** एजेन्टहरूले गणितीय समस्याहरू समाधान गर्न, रिपोर्ट तयार गर्न, वा सिमुलेशन गर्ने कोड वा स्क्रिप्ट चलाउन सक्छन्।
- **कार्यप्रवाह स्वचालन:** उपकरणहरू जस्तै कार्य तालिका, इमेल सेवा, वा डेटा पाइपलाइनहरूलाई एकीकृत गरेर दोहोरिने वा बहु-चरण कार्यहरू स्वचालित बनाउन।
- **ग्राहक सहायता:** एजेन्टहरूले CRM प्रणालीहरू, टिकटिंग प्लेटफर्महरू वा ज्ञान आधारहरू सँग अन्तरक्रिया गरी प्रयोगकर्ताका प्रश्नहरूको समाधान गर्न सक्छन्।
- **सामग्री सिर्जना र सम्पादन:** एजेन्टहरूले वाक्य-विन्यास जाँचकर्ताहरू, पाठ सारांशकर्ता, वा सामग्री सुरक्षा मूल्यांकन गर्ने उपकरणहरू प्रयोग गरी सामग्री सिर्जाना कार्यमा सहायता पुर्‍याउन सक्छन्।

## उपकरण प्रयोग डिजाइन ढाँचा लागू गर्न चाहिने तत्वहरू/निर्माण खण्डहरू के हुन्?

यी निर्माण खण्डहरूले AI एजेन्टलाई व्यापक कार्यहरू गर्न अनुमति दिन्छ। उपकरण प्रयोग डिजाइन ढाँचा लागू गर्न आवश्यक मुख्य तत्वहरू यसप्रकार छन्:

- **फङ्क्शन/उपकरण स्कीमाहरू**: उपलब्ध उपकरणहरूको विस्तृत परिभाषा, जसमा फङ्क्शन नाम, उद्देश्य, आवश्यक प्यारामीटरहरू र अपेक्षित परिणामहरू समावेश हुन्छन्। यी स्कीमाले LLM लाई उपलब्ध उपकरणहरू र वैध अनुरोध कसरी बनाउने बुझ्न मद्दत गर्छ।

- **फङ्क्शन निष्पादन लॉजिक**: प्रयोगकर्ताको उद्देश्य र कुराकानी सन्दर्भ अनुसार उपकरणहरू कहिले र कसरी बोलाउने भन्ने नियम। यसमा योजना बनाउने मोड्युलहरू, मार्गनिर्देशन तन्त्र वा सशर्त प्रवाहहरू समावेश हुन सक्छ जसले उपकरणहरूको प्रयोग डायनामिक रूपमा निर्धारण गर्छ।

- **सन्देश व्यवस्थापन प्रणाली**: प्रयोगकर्ता इनपुट, LLM जवाफ, उपकरण कल र उपकरण आउटपुटबीचको संवाद प्रवाह व्यवस्थापन गर्ने कम्पोनेन्टहरू।

- **उपकरण एकीकरण फ्रेमवर्क**: एजेन्टलाई विभिन्न उपकरणहरू (साधारण फङ्क्शन वा जटिल बाह्य सेवा) सँग जोड्ने पूर्वाधार।

- **त्रुटि व्यवस्थापन र प्रमाणीकरण**: उपकरण निष्पादनमा असफलता सामना गर्ने, प्यारामीटरहरू प्रमाणीकरण गर्ने र अनपेक्षित प्रतिक्रियाहरू व्यवस्थापन गर्ने यन्त्रहरू।

- **स्थिति व्यवस्थापन**: धेरै चरणको अन्तरक्रियामा निरन्तरता कायम राख्न कुराकानी सन्दर्भ, पहिलेका उपकरण अन्तरक्रिया र दिर्घकालीन डेटा ट्र्याक गर्ने।

अब, फङ्क्शन/उपकरण कललाई विस्तृत रूपमा हेरौं।

### फङ्क्शन/उपकरण कल

फङ्क्शन कल ठूलो भाषा मोडेलहरू (LLMs) लाई उपकरणहरूसँग अन्तरक्रिया गर्न सक्षम पार्ने प्राथमिक विधि हो। धेरै पटक 'फङ्क्शन' र 'उपकरण' शब्दहरू एकै अर्थमा प्रयोग गरिन्छ किनभने 'फङ्क्शन' (पुन: प्रयोग गर्न मिल्ने कोड ब्लक) नै तिन उपकरण हुन् जसले एजेन्टले कार्यहरू सम्पन्न गर्छ। कुनै फङ्क्शनको कोड चलाउनको लागि, LLM ले प्रयोगकर्ताको अनुरोधलाई फङ्क्शनको विवरणसँग तुलना गर्नु पर्छ। यसको लागि उपलब्ध सबै फङ्क्शनहरूको विवरण भएको स्कीमा LLM लाई पठाइन्छ। LLM ले कामका लागि सबैभन्दा उपयुक्त फङ्क्शन छानेर यसको नाम र तर्कहरू फर्काउँछ। चयनित फङ्क्शन चलाइन्छ, यसको प्रतिक्रिया LLM मा पठाइन्छ र त्यो जानकारी प्रयोगकर्ता अनुरोधको जवाफ बनाउन प्रयोग गरिन्छ।

एजेन्टहरूका लागि फङ्क्शन कल लागू गर्नका लागि तपाईंलाई चाहिन्छ:

1. फङ्क्शन कल समर्थन गर्ने LLM मोडेल
2. फङ्क्शन विवरणयुक्त स्कीमा
3. हरेक फङ्क्शनको कोड

सहरको हालको समय प्राप्त गर्ने उदाहरण प्रयोग गरौं:

1. **फङ्क्शन कल समर्थन गर्ने LLM प्रारम्भ गर्नुहोस्:**

    सबै मोडेलहरूले फङ्क्शन कल समर्थन नगर्न सक्छन्, त्यसैले तपाईंकहाँ प्रयोग हुने LLM मा यो सुविधा छ कि छैन जाँच गर्नु जरुरी छ। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> फङ्क्शन कल समर्थन गर्छ। हामी Azure OpenAI क्लायंट सुरु गरेर आरम्भ गर्न सक्छौं। 

    ```python
    # Azure OpenAI क्लाइन्टलाई आरम्भ गर्नुहोस्
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **फङ्क्शन स्कीमा बनाउनुहोस्:**

    पछि हामी JSON स्कीमा परिभाषित गर्नेछौं जसमा फङ्क्शन नाम, यसको कामको विवरण, र प्यारामीटरहरूको नाम तथा विवरण समावेश हुनेछ। त्यसपछि यो स्कीमा र प्रयोगकर्ताको अनुरोधसँग क्लायंटमा पठाइनेछ जसले सान फ्रान्सिस्कोको समय पत्ता लगाउने काम गर्छ। महत्वपूर्ण कुरा हो कि **टूल कल** फर्काइन्छ, प्रश्नको अन्तिम उत्तर होइन। जस्तै पहिले भनिएको थियो, LLM ले कार्यका लागि चयन गरेको फङ्क्शनको नाम र तर्कहरू फर्काउँछ।

    ```python
    # मोडेलले पढ्नको लागि कार्य विवरण
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
  
    # प्रारम्भिक प्रयोगकर्ता सन्देश
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # पहिलो API कल: मोडेललाई फंक्शन प्रयोग गर्न सोध्नुहोस्
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # मोडेलको प्रतिक्रिया प्रक्रिया गर्नुहोस्
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **कार्य सम्पन्न गर्न आवश्यक फङ्क्शन कोड:**

    अहिले LLM ले कुन फङ्क्शन चलाउनु पर्छ चयन गरिसकेको छ, त्यस फङ्क्शनलाई लागू गर्ने कोड लेखेर कार्य सन्चालन गर्नुपर्छ। हामी Python मा हालको समय प्राप्त गर्नको लागि कोड लेख्नेछौं। साथै प्रतिक्रिया सन्देशबाट नाम र तर्कहरू निकाल्ने कोड पनि आवश्यक पर्दछ।

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
     # फङ्सन कलहरूलाई व्यवस्थापन गर्नुहोस्
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
  
      # दोस्रो API कल: मोडेलबाट अन्तिम प्रतिक्रिया प्राप्त गर्नुहोस्
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

फङ्क्शन कल धेरैजसो, यदि सबै होइन भने, एजेन्ट उपकरण प्रयोग डिजाइनको मूल हो, यद्यपि यसलाई सुरुबाट लागू गर्नु कहिलेकाहीं चुनौतीपूर्ण हुन सक्छ।
[पाठ २](../../../02-explore-agentic-frameworks) मा जस्तै, एजेन्टिक फ्रेमवर्कहरूले उपकरण प्रयोग लागू गर्न पूर्वनिर्मित निर्माण खण्डहरू प्रदान गर्छन्।

## एजेन्टिक फ्रेमवर्कहरूको साथ उपकरण प्रयोगका उदाहरणहरू

विभिन्न एजेन्टिक फ्रेमवर्कहरूको प्रयोग गरी उपकरण प्रयोग डिजाइन ढाँचा कसरी लागू गर्ने केही उदाहरणहरू:

### माइक्रोसफ्ट एजेन्ट फ्रेमवर्क

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> AI एजेन्टहरू निर्माण गर्नको लागि खुला स्रोत AI फ्रेमवर्क हो। यसले फङ्क्शन कल प्रयोग सरल बनाउँछ किनभने तपाईं उपकरणहरूलाई Python फङ्क्शनहरू `@tool` डिकोरेटर प्रयोग गरेर परिभाषित गर्न सक्नुहुन्छ। फ्रेमवर्कले मोडेल र तपाईंको कोडको बीचमा दोहोरो संवाद व्यवस्थापन गर्छ। साथै AzureAIProjectAgentProvider मार्फत तयार उपकरणहरू जस्तै File Search र Code Interpreter पहुँच उपलब्ध गराउँछ।

माइक्रोसफ्ट एजेन्ट फ्रेमवर्कमा फङ्क्शन कल प्रक्रिया तलको चित्रले देखाउँछ:

![function calling](../../../translated_images/ne/functioncalling-diagram.a84006fc287f6014.webp)

यस फ्रेमवर्कमा उपकरणहरू डेकोरेट गरिएको फङ्क्शनका रूपमा परिभाषित गरिन्छ। हामीले पहिले देखेको `get_current_time` फङ्क्शनलाई `@tool` डिकोरेटर प्रयोग गरेर उपकरणमा रूपान्तरण गर्न सक्छौं। फ्रेमवर्कले फङ्क्शन र त्यसका प्यारामीटरहरू स्वचालित रूपमा सिरियलाइज गरी LLM लाई पठाउन स्कीमा तयार पार्छ।

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ग्राहक बनाउनुहोस्
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# एजेन्ट बनाउनुहोस् र उपकरणसँग चलाउनुहोस्
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent सेवा

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> नयाँ एजेन्टिक फ्रेमवर्क हो जसले विकासकर्ताहरूलाई सुरक्षित, स्केलेबल र गुणस्तरिय AI एजेन्टहरू निर्माण गर्न सक्षम बनाउँछ, जसले तलका संसाधनहरू व्यवस्थापन गर्नुपर्दैन। यो व्यवसाय अनुप्रयोगहरूका लागि उपयोगी छ किनभने यो पूर्ण रूपमा प्रबन्धित सेवा हो र सुरक्षा स्तर उच्च छ।

प्रत्यक्ष LLM API विकासको सट्टा Azure AI Agent Service प्रयोग गर्दा केहि फाइदाहरू छन्:

- स्वचालित उपकरण कल – उपकरण कल पार्स, उपकरण सन्चालन र प्रतिक्रिया व्यवस्थापन गर्नु पर्दैन; यो सबै सर्भर पक्षमै हुन्छ
- सुरक्षित रूपमा व्यवस्थापन गरिएको डेटा – आफ्नै कुराकानी स्थितिलाई व्यवस्थापन गर्ने सट्टा, थ्रेड्समा सबै आवश्यक जानकारी भण्डारण गर्न सकिन्छ
- तयार उपकरणहरू – Bing, Azure AI Search, Azure Functions जस्ता डेटा स्रोतहरूसँग अन्तरक्रिया गर्न टूलहरू उपलब्ध छन्।

Azure AI Agent Service मा उपलब्ध उपकरणहरू दुई वर्गमा विभाजित छन्:

1. ज्ञान उपकरणहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search संग ग्राउन्डिङ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. कार्य उपकरणहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित उपकरणहरू</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ले यी उपकरणहरूलाई `toolset` को रूपमा संगै प्रयोग गर्न अनुमति दिन्छ। यसले खास कुराकानीबाट सन्देशहरूको इतिहास ट्र्याक गर्न `threads` पनि प्रयोग गर्छ।

कल्पना गर्नुहोस् तपाईं 'Contoso' नामक कम्पनीमा बिक्री एजेन्ट हुनुहुन्छ। तपाईं तपाईँको बिक्री डेटा सम्बन्धी प्रश्नहरूको जवाफ दिन सक्ने संवादात्मक एजेन्ट विकास गर्न चाहनुहुन्छ।

तलको तस्बिरले Azure AI Agent Service को प्रयोग गरी बिक्री डेटा विश्लेषण कसरी गर्ने देखाउँछ:

![Agentic Service In Action](../../../translated_images/ne/agent-service-in-action.34fb465c9a84659e.webp)

यी उपकरणहरू सेवा संग प्रयोग गर्न, हामी क्लायंट सिर्जना गरी उपकरण या उपकरण समूह परिभाषित गर्न सक्छौं। व्यवहारमा लागू गर्न, तलको Python कोड प्रयोग गर्न सकिन्छ। LLM ले उपकरण समूह हेरेर प्रयोगकर्ताको अनुरोध अनुसार प्रयोगकर्ताले बनाएको `fetch_sales_data_using_sqlite_query` फङ्क्शन वा पूर्वनिर्मित Code Interpreter प्रयोग गर्ने निर्णय गर्नेछ।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query समारोह जुन fetch_sales_data_functions.py फाइलमा फेला पार्न सकिन्छ।
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# उपकरण सेट सुरु गर्नुहोस्
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query समारोहसँग function calling agent सुरु गर्नुहोस् र यसलाई उपकरण सेटमा थप्नुहोस्
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter उपकरण सुरु गर्नुहोस् र यसलाई उपकरण सेटमा थप्नुहोस्।
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## विश्वसनीय AI एजेन्ट बनाउन उपकरण प्रयोग डिजाइन ढाँचा प्रयोग गर्दा के विशेष विचारहरू आवश्यक हुन्छ?

LLM द्वारा गतिशील रूपमा सिर्जित SQL सम्बन्धी सामान्य चिन्ता सुरक्षा हो, विशेष गरी SQL injection वा नकरात्मक गतिविधिहरूको जोखिम (जस्तै डेटाबेस ड्रप वा छेउछाउ) । यद्यपि यी चिन्ताहरू उचित रूपमा डेटाबेस पहुँच अनुमतिहरू सेट गरेर प्रभावकारी रूपमा न्यूनीकरण गर्न सकिन्छ। अधिकांश डेटाबेसका लागि यसमा डेटाबेसलाई केवल-पढ्न (read-only) बनाउने समावेश हुन्छ। PostgreSQL वा Azure SQL जस्ता डेटाबेस सेवा प्रयोग गर्दा एपलाई केवल-पढ्न (SELECT) भूमिका प्रदान गर्नुपर्छ।

एपलाई सुरक्षित वातावरणमा चलाउनु थप सुरक्षा प्रदान गर्दछ। व्यावसायिक परिदृश्यमा, डेटा प्राय: सञ्चालन प्रणालीहरूबाट निकालेर पढ्न मात्र मिल्ने डेटाबेस वा डेटा वेयरहाउसमा रूपान्तरण गरिन्छ जसमा प्रयोगकर्तामा मैत्री स्कीमा हुन्छ। यसले सुनिश्चित गर्छ कि डेटा सुरक्षित, प्रदर्शन र पहुँचका लागि अप्टिमाइज गरिएको, र एपलाई सीमित र केवल-पढ्न अनुमति दिइएको छ।

## नमुना कोडहरू

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## उपकरण प्रयोग डिजाइन ढाँचाहरू बारे थप प्रश्नहरू छन्?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा सामेल भएर अन्य सिक्नेहरूसँग भेट गर्नुहोस्, अफिस आवरहरूमा जानुहोस् र तपाईंका AI एजेन्ट सम्बन्धी प्रश्नहरू समाधान पाउनुहोस्।

## थप स्रोतहरू

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service कार्यशाला</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer मल्टि-एजेन्ट कार्यशाला</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework अवलोकन</a>

## अघिल्लो पाठ

[एजेन्टिक डिजाइन ढाँचाहरू बुझ्न](../03-agentic-design-patterns/README.md)

## अर्को पाठ
[एजेन्सिक RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यस दस्तावेजलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं भनेपनि, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा गलत जानकारीहरू हुन सक्दछ। मूल दस्तावेज यसको मातृ भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी दायित्व स्वीकार गर्दैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->