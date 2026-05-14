[![कसरी राम्रो AI एजेन्टहरूले डिजाइन गर्ने](../../../translated_images/ne/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(यस पाठको भिडियो हेर्न माथि रहेको तस्बिरमा क्लिक गर्नुहोस्)_

# उपकरण प्रयोग डिजाइन ढाँचा

उपकरणहरू रोचक छन् किनभने यीले AI एजेन्टहरूलाई व्यापक क्षमताहरू प्रदान गर्छन्। एजेन्टसँग सीमित क्रियाहरूको सेट हुने सट्टा, उपकरण थप्दा एजेन्टले अब फराकिलो दायराका क्रियाहरू गर्न सक्छ। यस अध्यायमा, हामी उपकरण प्रयोग डिजाइन ढाँचालाई हेर्नेछौं, जसले कसरी AI एजेन्टहरूले विशेष उपकरणहरू प्रयोग गरेर आफ्ना लक्ष्यहरू हासिल गर्न सक्छन् भन्ने वर्णन गर्छ।

## परिचय

यस पाठमा, हामी निम्न प्रश्नहरूको उत्तर खोज्दैछौं:

- उपकरण प्रयोग डिजाइन ढाँचा के हो?
- यसलाई कुन-कुन प्रयोग केसहरूमा लागू गर्न सकिन्छ?
- डिजाइन ढाँचा लागू गर्न आवश्यक अङ्ग/निर्माण ब्लकहरू के-के हुन्?
- भरोसायोग्य AI एजेन्टहरू निर्माण गर्न उपकरण प्रयोग डिजाइन ढाँचा प्रयोग गर्दा के-कस्ता विशेष विचारहरू छन्?

## सिकाइ लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं सक्ने हुनुहुनेछ:

- उपकरण प्रयोग डिजाइन ढाँचाको परिभाषा र यसको उद्देश्य बुझ्न।
- उपकरण प्रयोग डिजाइन ढाँचा कुन-कुन प्रयोग केसहरूमा लागू हुन्छ त्यसको पहिचान गर्न।
- डिजाइन ढाँचा लागू गर्नका लागि आवश्यक मुख्य अङ्गहरू बुझ्न।
- यस डिजाइन ढाँचाको प्रयोग गर्ने AI एजेन्टहरूमा भरोसायोग्यता सुनिश्चित गर्नका लागि विचारहरू चिन्हित गर्न।

## उपकरण प्रयोग डिजाइन ढाँचा के हो?

**उपकरण प्रयोग डिजाइन ढाँचा** ले LLMs लाई बाह्य उपकरणहरूसँग अन्तरक्रिया गर्ने क्षमता दिने कुरामा केन्द्रित छ, जसले विशेष लक्ष्यहरू हासिल गर्न मद्दत गर्दछ। उपकरणहरू भनेको त्यस्ता कोड हुन् जुन एजेन्टले कार्यहरू गर्नका लागि सञ्चालन गर्न सक्छ। उपकरण एक सरल कार्य जस्तै क्याल्कुलेटर हुन सक्छ, वा स्टक मूल्य खोज वा मौसम पूर्वानुमानजस्ता तेस्रो-पक्ष सेवामा API कल पनि हुन सक्छ। AI एजेन्टहरूको सन्दर्भमा, उपकरणहरू एजेन्टहरूले **मोडेल-जनरेट गरिएको फंक्शन कलहरू** प्रतिक्रिया स्वरूप सञ्चालन गर्न डिजाइन गरिएका हुन्छन्।

## त्यसलाई कुन-कुन प्रयोग केसहरूमा लागू गर्न सकिन्छ?

AI एजेन्टहरूले जटिल कार्यहरू पूरा गर्न, जानकारी पुनःप्राप्त गर्न, वा निर्णय लिन उपकरणहरूको उपयोग गर्न सक्छन्। उपकरण प्रयोग डिजाइन ढाँचा प्रायः यस्तो अवस्थामा प्रयोग हुन्छ जहाँ बाह्य प्रणालीहरूसँग गतिशील अन्तरक्रिया आवश्यक हुन्छ, जस्तै डाटाबेस, वेब सेवाहरू, वा कोड इन्टरप्रेटरहरू। यस क्षमताले विभिन्न प्रयोग केसहरूमा उपयोगी हुन्छ, जस्तै:

- **गतिशील जानकारी पुनःप्राप्ति:** एजेन्टहरूले बाह्य API वा डाटाबेसहरूलाई सोधेर अद्यावधिक जानकारी प्राप्त गर्न सक्छन् (जस्तै, SQLite डाटाबेसबाट डेटा विश्लेषणका लागि सोध्ने, स्टक मूल्य वा मौसम जानकारी आर्जन गर्ने)।
- **कोड सञ्चालन र व्याख्या:** एजेन्टहरूले गणितीय समस्या समाधान गर्न, रिपोर्ट सिर्जना गर्न, वा सिमुलेशनहरू गर्न कोड वा स्क्रिप्ट सञ्चालन गर्न सक्छन्।
- **कार्यप्रवाह स्वचालन:** कार्य तालिका, ईमेल सेवा, वा डेटा पाइपलाइनहरू जस्ता उपकरणहरू समावेश गरी पुनरावृत्ति वा बहु-चरण कार्यप्रवाह स्वचालित गर्ने।
- **ग्राहक समर्थन:** एजेन्टहरूले CRM प्रणाली, टिकटिङ प्लेटफर्म, वा ज्ञान आधारहरूसँग अन्तरक्रिया गरी प्रयोगकर्ताका प्रश्नहरू समाधान गर्ने।
- **सामग्री सिर्जना र सम्पादन:** व्याकरण जाँच्ने, पाठ संक्षेप गर्ने, वा सामग्री सुरक्षा मूल्याङ्कन गर्ने उपकरणहरू प्रयोग गरेर सामग्री सिर्जनामा सहयोग गर्ने।

## उपकरण प्रयोग डिजाइन ढाँचा लागू गर्न आवश्यक अङ्ग/निर्माण ब्लकहरू के-के हुन्?

यी निर्माण ब्लकहरूले AI एजेन्टलाई फराकिलो कार्यहरू गर्न सक्षम पार्छन्। उपकरण प्रयोग डिजाइन ढाँचा लागू गर्न आवश्यक मुख्य अङ्गहरू हेरौं:

- **फंक्शन/उपकरण स्किमा:** उपलब्ध उपकरणहरूको विस्तृत परिभाषाहरू, जस्तै फंक्शन नाम, उद्देश्य, आवश्यक प्यारामिटरहरू, र अपेक्षित आउटपुटहरू। यी स्किमाले LLM लाई कुन उपकरणहरू उपलब्ध छन् र वैध अनुरोध कसरी बनाउने बुझ्न मद्दत गर्छ।

- **फंक्शन कार्यान्वयन तर्क:** प्रयोगकर्ताको अभिप्राय र संवाद संदर्भअनुसार उपकरणहरू कहिले र कसरी कल गर्ने निर्धारण गर्छ। यसमा योजना बनाउने मोड्युलहरू, राउटिङ मेकानिज्महरू, वा सशर्त प्रवाहहरू हुन सक्छन् जसले उपकरण प्रयोग गतिशील रूपमा निर्धारण गर्दछन्।

- **सन्देश व्यवस्थापन प्रणाली:** प्रयोगकर्ता इनपुट, LLM प्रतिक्रिया, उपकरण कलहरू, र उपकरण आउटपुटहरूबीचको संवाद प्रवाह व्यवस्थापन गर्ने घटकहरू।

- **उपकरण एकीकरण फ्रेमवर्क:** एजेन्टलाई विभिन्न उपकरणहरूसँग जडान गर्ने पूर्वाधार, जे साना फंक्शन हुन् वा जटिल बाह्य सेवाहरू हुन्।

- **त्रुटि व्यवस्थापन र मान्यकरण:** उपकरण सञ्चालनमा समस्या आउँदा सम्हाल्ने, प्यारामिटरहरूको मान्यता गर्ने, र अप्रत्याशित प्रतिक्रियाहरू व्यवस्थापन गर्ने संयन्त्रहरू।

- **राज्य व्यवस्थापन:** संवाद संदर्भ, पहिला गरिएका उपकरण अन्तरक्रियाहरू, र दिर्घकालीन डेटा ट्र्याक गर्ने जसले बहु-चरण अन्तरक्रियाहरूमा निरन्तरता सुनिश्चित गर्दछ।

अब हामी फंक्शन/उपकरण कल गर्ने प्रक्रियालाई विस्तारमा हेरौं।
 
### फंक्शन/उपकरण कल गर्ने

फंक्शन कल गर्ने ठूलो भाषाई मोडेलहरू (LLMs) लाई उपकरणहरूसँग अन्तरक्रिया गराउने प्रमुख माध्यम हो। प्रायः 'फंक्शन' र 'उपकरण' शब्दहरू विनिमयीय रूपमा प्रयोग हुन्छन् किनकि 'फंक्शनहरू' (पुनःप्रयोग गर्न मिल्ने कोड ब्लकहरू) नै ती 'उपकरणहरू' हुन् जुन एजेन्टहरूले कार्यहरू गर्न प्रयोग गर्छन्। फंक्शनको कोड सञ्चालन गर्नको लागि, LLM ले प्रयोगकर्ताको अनुरोधलाई फंक्शन विवरणसँग तुलना गर्नुपर्छ। यसका लागि उपलब्ध सबै फंक्शनहरूको विवरण समेटिएको स्किमा LLM लाई पठाइन्छ। LLM त्यसपछि कार्यका लागि सबैभन्दा उपयुक्त फंक्शन चयन गरी त्यसको नाम र आर्गुमेन्टहरू फर्काउँछ। चयनित फंक्शन सञ्चालन हुन्छ, यसको प्रतिक्रिया LLM लाई पठाइन्छ जसले त्यस सूचना प्रयोग गरी प्रयोगकर्ताको अनुरोधको जवाफ दिन्छ।

एजेन्टहरूको लागि फंक्शन कल कार्यान्वयन गर्न, तपाईंलाई चाहिन्छ:

1. फंक्शन कल समर्थन गर्ने LLM मोडेल
2. फंक्शन विवरण समेटिएको स्किमा
3. प्रत्येक फंक्शनको लागि कोड

सहरको हालको समय पत्ता लगाउने उदाहरण प्रयोग गरौं:

1. **फंक्शन कल समर्थन गर्ने LLM सुरु गर्ने:**

    सबै मोडेलहरूले फंक्शन कल समर्थन गर्दैनन्, त्यसैले प्रयोग गर्ने LLM मा यो सुविधा छ कि छैन जाँच्नु आवश्यक हुन्छ। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ले फंक्शन कल समर्थन गर्छ। हामी Azure OpenAI क्लाइन्ट सुरु गरेर थाल्न सक्छौं।

    ```python
    # Azure OpenAI क्लाइंटलाई प्रारम्भ गर्नुहोस्
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **फंक्शन स्किमा बनाउने:**

    अर्को चरणमा, JSON स्किमा परिभाषित गर्नेछौं जसमा फंक्शनको नाम, के काम गर्छ भन्ने विवरण, र फंक्शनका प्यारामिटरहरूको नाम र वर्णन समावेश हुनेछ। त्यसपछि यो स्किमा पहिले बनाइएको क्लाइन्टलाई प्रयोगकर्ताको अनुरोधसँगै पठाइनेछ, जसले San Francisco मा समय पत्ता लगाउने काम गर्दछ। यहाँ महत्वपूर्ण कुरा के हो भने **उपकरण कल** फर्काइन्छ, प्रश्नको अन्तिम उत्तर होइन। पहिले जस्तै, LLM ले कार्यका लागि छानेको फंक्शनको नाम र त्यसमा पठाइने आर्गुमेन्टहरू फर्काउँछ।

    ```python
    # मोडलले पढ्नको लागि कार्य विवरण
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
  
    # आरम्भिक प्रयोगकर्ता सन्देश
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # पहिलो API कल: मोडेललाई फङ्सन प्रयोग गर्न भन्नुहोस्
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # मोडेलको प्रतिक्रिया प्रशोधन गर्नुहोस्
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **कार्य सम्पन्न गर्न आवश्यक फंक्शन कोड:**

    अब LLM ले कुन फंक्शन चलाउनु पर्ने निर्णय गरी सकेपछि, त्यस कार्य गर्न कोड कार्यान्वयन गर्नुपर्छ। हामी Python मा हालको समय प्राप्त गर्ने कोड लेख्न सक्दछौं। अन्तिम नतिजा प्राप्त गर्न response_message बाट नाम र आर्गुमेन्टहरू निकाल्ने कोड पनि लेख्न जरुरी हुन्छ।

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
  
      # दोस्रो API कल: मोडेलबाट अन्तिम जवाफ प्राप्त गर्नुहोस्
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

फंक्शन कल अधिकांश एजेन्ट उपकरण प्रयोग डिजाइनको मुटु हो, यद्यपि यो सुरूवातदेखि नै कार्यान्वयन गर्न कहिलेकाहीं चुनौतीपूर्ण हुन सक्छ।
जस्तै [पाठ २](../../../02-explore-agentic-frameworks) मा हामीले सिक्यौं, एजेन्ट फ्रेमवर्कहरूले उपकरण प्रयोग कार्यान्वयन गर्न पूर्वनिर्मित ब्लकहरू प्रदान गर्दछन्।
 
## एजेन्टिक फ्रेमवर्कहरूसँग उपकरण प्रयोगका उदाहरणहरू

यहाँ विभिन्न एजेन्टिक फ्रेमवर्कहरू प्रयोग गरी उपकरण प्रयोग डिजाइन ढांचा कसरी कार्यान्वयन गर्ने केही उदाहरणहरू छन्:

### Microsoft एजेन्ट फ्रेमवर्क

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft एजेन्ट फ्रेमवर्क</a> एक खुला स्रोत AI फ्रेमवर्क हो AI एजेन्टहरू निर्माण गर्न। यसले फंक्शन कल प्रयोगलाई सरल बनाउँछ किनभने तपाईंले उपकरणहरूलाई Python फंक्शनहरूलाई `@tool` डेकोरेटरका साथ परिभाषित गर्न सक्नुहुन्छ। फ्रेमवर्कले मोडेल र तपाईंको कोड बीचको संवादको ब्याक-एण्ड सञ्चालन सम्हाल्छ। यसले `AzureAIProjectAgentProvider` मार्फत फाइल सर्च र कोड इन्टरप्रेटर जस्ता पूर्वनिर्मित उपकरणहरूको पहुँच पनि दिन्छ।

माइक्रोसफ्ट एजेन्ट फ्रेमवर्कसँग फंक्शन कल गर्ने प्रक्रिया तल चित्रले देखाएको छ:

![function calling](../../../translated_images/ne/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft एजेन्ट फ्रेमवर्कमा उपकरणहरूसँग सजाइएको फंक्शनको रूपमा परिभाषित गरिन्छ। हामीले अघि देखेको `get_current_time` फंक्शनलाई `@tool` डेकोरेटर प्रयोग गरी एउटा उपकरणमा परिवर्तन गर्न सक्छौं। फ्रेमवर्कले उक्त फंक्शन र यसको प्यारामिटरहरूको स्वचालित रुपमा सिरियलाइजेसन गरेर LLM मा पठाउनको लागि स्किमा तयार पार्छ।

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# क्लाइन्ट सिर्जना गर्नुहोस्
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# एउटा एजेन्ट बनाउनुहोस् र उपकरणसँग चलेर संचालन गर्नुहोस्
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI एजेन्ट सेवा

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI एजेन्ट सेवा</a> नयाँ एजेन्टिक फ्रेमवर्क हो जुन विकासकर्ताहरूलाई सुरक्षापूर्वक उच्च गुणस्तरका र विस्तारयोग्य AI एजेन्टहरू निर्माण, डिप्लोय र स्केल गर्न सक्षम पार्छ, जसले आधारभूत कम्प्युट र स्टोरेज स्रोतहरू व्यवस्थापन गर्नुपर्ने बाध्यता हटाउँछ। यो विशेष गरी उद्यम अनुप्रयोगहरूको लागि उपयोगी छ, किनभने यो पूर्णतया प्रबन्धित सेवा हो र उद्यम स्तरीय सुरक्षा प्रदान गर्छ।

सीधा LLM API प्रयोग गरी विकासभन्दा, Azure AI एजेन्ट सेवाले केही फाइदाहरू दिन्छ, जस्तै:

- स्वचालित उपकरण कल – उपकरण कल पार्स गर्नु, उपकरण सञ्चालन गर्नु, र प्रतिक्रिया सम्हाल्नु पर्दैन; यो सबै सर्भर पक्षमा हुन्छ
- सुरक्षित रूपमा व्यवस्थापित डेटा – संवाद स्थितिलाई तपाईंले आफैं व्यवस्थापन गर्नु पर्दैन, थ्रेडहरूमा सबै जानकारी भण्डारण गर्न सकिन्छ
- तयार उपकरणहरू – Bing, Azure AI Search, र Azure Functions जस्ता डेटा स्रोतहरूसँग अन्तरक्रिया गर्न प्रयोग गर्न सकिने उपकरणहरू।

Azure AI एजेन्ट सेवामा उपलब्ध उपकरणहरू दुई वर्गमा छुट्टाइन्छ:

1. ज्ञान उपकरणहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing खोजसंग ग्राउन्डिङ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">फाइल सर्च</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI खोज</a>

2. कार्य उपकरणहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">फंक्शन कल</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इन्टरप्रेटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित उपकरणहरू</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

एजेन्ट सेवाले यी उपकरणहरूलाई `toolset` रूपमा सँगै प्रयोग गर्न सक्ने सुविधा दिन्छ। यो `थ्रेडहरू` पनि प्रयोग गर्छ जसले विशेष संवादबाट सन्देशहरूको इतिहास राख्छ।

कल्पना गर्नुहोस् तपाईं Contoso नामक कम्पनीमा एक बिक्री एजेन्ट हुनुहुन्छ। तपाईं यस्तो संवादात्मक एजेन्ट विकास गर्न चाहनुहुन्छ जसले तपाईंको बिक्री डेटा सम्बन्धी प्रश्नहरूको जवाफ दिन सक्छ।

तलको चित्रले Azure AI एजेन्ट सेवा प्रयोग गरी बिक्री डेटा कसरी विश्लेषण गर्ने देखाउँछ:

![Agentic Service In Action](../../../translated_images/ne/agent-service-in-action.34fb465c9a84659e.webp)

सेवासँग कुनै उपकरण प्रयोग गर्न हामी क्लाइन्ट बनाएर उपकरण वा उपकरण समूह परिभाषित गर्न सक्दछौं। यथार्थमा कार्यान्वयन गर्न तलको Python कोड प्रयोग गर्न सकिन्छ। LLM ले उपकरण समूह हेरि प्रयोगकर्ताले सिर्जना गरेको फंक्शन `fetch_sales_data_using_sqlite_query` प्रयोग गर्ने वा पूर्वनिर्मित कोड इन्टरप्रेटर प्रयोग गर्ने निर्णय गर्नेछ।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query फंक्शन जुन fetch_sales_data_functions.py फाइलमा पाइन्छ।
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# उपकरण सेट सुरु गर्नुहोस्
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query फंक्शन प्रयोग गरेर फंक्शन कलिङ एजेन्ट सुरु गर्नुहोस् र यसलाई उपकरण सेटमा जोड्नुहोस्
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# कोड इन्टरप्रेटर उपकरण सुरु गर्नुहोस् र यसलाई उपकरण सेटमा जोड्नुहोस्।
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## भरोसायोग्य AI एजेन्टहरू निर्माण गर्न उपकरण प्रयोग डिजाइन ढाँचा प्रयोग गर्दा के विशेष विचारहरू हुन्छन्?

LLMहरूले गतिशील रूपमा सिर्जित SQL सम्बन्धी सामान्य चिन्ता भनेको सुरक्षा हो, विशेष गरी SQL इन्जेक्शन वा दुर्भावनापूर्ण कार्यहरू जस्तै डेटाबेस हटाउने वा छेडछाड गर्ने जोखिम। यी चिन्ताहरू वैध भए तापनि, डेटाबेस पहुँच अनुमति उचित तरिकाले कन्फिगर गरेर प्रभावकारी रूपमा टार्न सकिन्छ। धेरैजसो डेटाबेसका लागि यसले डेटाबेसलाई पढ्न मात्र योग्य (read-only) बनाउने व्यवस्था गर्नुपर्छ। PostgreSQL वा Azure SQL जस्ता डेटाबेस सेवाहरूमा एपलाई पढ्न मात्र (SELECT) अधिकार दिने भूमिका दिनु पर्छ।

एपलाई सुरक्षित वातावरणमा चलाउनु थप सुरक्षा बढाउँछ। उद्यम परिदृश्यहरूमा, डेटा सामान्यतया सञ्चालन प्रणालीहरूबाट निकाली पढ्न मात्र योग्य डेटाबेस वा डेटा वेयरहाउसमा परिवर्तन गरिन्छ जसमा प्रयोगकर्ता-मित्रवत स्किमा हुन्छ। यसले डेटा सुरक्षित, प्रदर्शन र पहुँचयोग्य बनाउँछ र एपलाई सीमित पढ्नु मात्र अनुमति दिन्छ।

## नमूना कोडहरू

- Python: [एजेन्ट फ्रेमवर्क](./code_samples/04-python-agent-framework.ipynb)
- .NET: [एजेन्ट फ्रेमवर्क](./code_samples/04-dotnet-agent-framework.md)

## उपकरण प्रयोग डिजाइन ढाँचाको बारेमा थप प्रश्नहरू छन्?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा सहभागी हुनुहोस् अन्य सिक्नेलाई भेट्न, अफिस आवरहरूमा जान, र तपाईंका AI एजेन्ट प्रश्नहरूको जवाफ पाउन।

## अतिरिक्त स्रोतहरू

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI एजेन्ट सेवा कार्यशाला</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer बहु-एजेन्ट कार्यशाला</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft एजेन्ट फ्रेमवर्क अवलोकन</a>

## अघिल्लो पाठ

[एजेन्टिक डिजाइन ढाँचाहरू बुझ्न](../03-agentic-design-patterns/README.md)

## अर्को पाठ
[एजेन्सी आरएजी](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->