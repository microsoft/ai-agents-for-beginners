[![कसरी राम्रो AI एजेण्टहरू डिजाइन गर्ने](../../../translated_images/ne/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(यस पाठको भिडियो हेर्न माथिको छविमा क्लिक गर्नुहोस्)_

# उपकरण प्रयोग डिजाइन ढाँचा

उपकरणहरू रोचक छन् किनभने तिनीहरूले AI एजेण्टहरूलाई फराकिलो क्षमताहरूको श्रृंखला दिन्छन्। एजेन्टसँग सीमित कार्यहरू गर्ने क्षमता हुनुको सट्टा, उपकरण थपेर एजेन्ट अब फराकिलो प्रकारका कार्यहरू गर्न सक्छ। यस अध्यायमा, हामी उपकरण प्रयोग डिजाइन ढाँचा हेर्न जाँदैछौं, जसले AI एजेन्टहरूले आफ्नो लक्ष्यहरू पूरा गर्न विशिष्ट उपकरणहरू कसरी प्रयोग गर्न सक्ने बताउँछ।

## परिचय

यस पाठमा, हामी निम्न प्रश्नहरूको उत्तर खोज्दैछौं:

- उपकरण प्रयोग डिजाइन ढाँचा के हो?
- कुन प्रयोग मामिलाहरूमा यो लागू गर्न सकिन्छ?
- डिजाइन ढाँचा लागू गर्न आवश्यक तत्वहरू/निर्माण खण्डहरू के के हुन्?
- विश्वासयोग्य AI एजेण्टहरू बनाउन उपकरण प्रयोग डिजाइन ढाँचाको विशेष विचारहरू के हुन्?

## सिकाइ लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं सक्षम हुनु हुनेछ:

- उपकरण प्रयोग डिजाइन ढाँचा र यसको उद्देश्य परिभाषित गर्न।
- उपकरण प्रयोग डिजाइन ढाँचा लागू गर्न सकिने प्रयोग मामिलाहरू पहिचान गर्न।
- डिजाइन ढाँचा लागू गर्न आवश्यक मुख्य तत्वहरू बुझ्न।
- यो डिजाइन ढाँचा प्रयोग गर्ने AI एजेन्टहरूको विश्वासनीयता सुनिश्चित गर्नका लागि विचारहरू चिन्छ्न।

## उपकरण प्रयोग डिजाइन ढाँचा के हो?

**उपकरण प्रयोग डिजाइन ढाँचा** LLM हरूलाई बाह्य उपकरणहरूसँग अन्तरक्रिया गर्ने क्षमता दिन केन्द्रित हुन्छ ताकि विशिष्ट लक्ष्यहरू प्राप्त गर्न सकियोस्। उपकरणहरू कोड हुन् जुन एजेन्टले क्रियाहरू सञ्चालन गर्न प्रयोग गर्न सक्छ। एउटा उपकरण सरल कार्य जस्तै क्याल्कुलेटर हुन सक्छ, वा स्टक मूल्य हेर्ने वा मौसम पूर्वानुमान जस्ता तृतीय-पक्ष सेवाको API कल हुन सक्छ। AI एजेण्टहरूको सन्दर्भमा, उपकरणहरू एलएलएमद्वारा उत्पादित फंक्शन कलहरूमा प्रतिक्रिया स्वरूप एजेन्टहरूले सञ्चालन गर्न डिजाइन गरिन्छ।

## कुन प्रयोग मामिलाहरूमा यो लागू गर्न सकिन्छ?

AI एजेण्टहरूले जटिल कार्यहरू पूरा गर्न, सूचना प्राप्त गर्न, वा निर्णय लिन उपकरणहरूको उपयोग गर्न सक्छन्। उपकरण प्रयोग डिजाइन ढाँचा प्राय: गतिशील अन्तरक्रिया आवश्यक पर्ने अवस्था जस्तै डाटाबेस, वेब सेवा, वा कोड इन्टरप्रेटरहरूसँग अन्तरक्रिया गर्न प्रयोग गरिन्छ। यसले धेरै विभिन्न प्रयोग मामिलाहरूमा उपयोगी हुन्छ, जस्तै:

- **गतिशील सूचना प्राप्ति:** एजेन्टहरूले बाह्य API वा डाटाबेसहरूलाई सोध्न सक्छन् ताकि हालसालैको डेटा ल्याउन सकियोस् (जस्तै, SQLite डाटाबेसबाट डेटा विश्लेषणका लागि सोधपुछ, स्टक मूल्य वा मौसम जानकारी ल्याउने)।
- **कोड कार्यान्वयन र व्याख्या:** एजेन्टहरूले गणितीय समस्या समाधान गर्न, रिपोर्टहरू उत्पादन गर्न, वा सिमुलेशन गर्न कोड वा स्क्रिप्टहरू कार्यान्वयन गर्न सक्छन्।
- **कार्य प्रवाह स्वचालन:** कार्य सूचीकर्ताहरू, इमेल सेवा, वा डेटा पाइपलाइनहरू जस्ता उपकरणहरू एकीकृत गरेर दोहोरिने वा बहु-चरणका कार्यहरू स्वचालित बनाउने।
- **ग्राहक सहायता:** CRM प्रणालीहरू, टिकटिङ प्लेटफर्महरू, वा ज्ञान आधारहरूसँग अन्तरक्रिया गरेर प्रयोगकर्ता प्रश्नहरू समाधान गर्ने।
- **सामग्री सिर्जना र सम्पादन:** व्याकरण जाँचकर्ता, पाठ सारांशकर्ताहरू, वा सामग्री सुरक्षा मूल्यांकन उपकरणहरू प्रयोग गरेर सामग्री सिर्जनामा सहयोग पुर्‍याउने।

## उपकरण प्रयोग डिजाइन ढाँचा लागू गर्न आवश्यक तत्वहरू/निर्माण खण्डहरू के हुन्?

यी निर्माण खण्डहरूले AI एजेन्टलाई फराकिलो कार्यहरू गर्न सक्षम पार्दछन्। उपकरण प्रयोग डिजाइन ढाँचा लागू गर्न आवश्यक मुख्य तत्वहरू यस्ता छन्:

- **फंक्शन/उपकरण स्कीमा:** उपलब्ध उपकरणहरूको विस्तृत परिभाषा, जसमा फंक्शन नाम, उद्देश्य, आवश्यक प्यारामिटरहरू र अपेक्षित नतिजाहरू समावेश हुन्छन्। यी स्कीमाहरूले LLM लाई कुन उपकरणहरू उपलब्ध छन् र सही अनुरोध कसरी बनाउने बुझ्न मद्दत गर्छ।

- **फंक्शन कार्यान्वयन तर्क:** प्रयोगकर्ताको इरादा र संवाद सन्दर्भको आधारमा उपकरणहरू कहिले र कसरी कल गरिन्छ त्यसको नियमन गर्छ। यसमा योजना बनाउने मोड्युलहरू, राउटिंग मेकानिज्महरू, वा सशर्त प्रवाहहरू हुन सक्छन् जसले गतिशील रूपमा उपकरण प्रयोग निर्धारण गर्छ।

- **सन्देश ह्यान्डलिङ प्रणाली:** प्रयोगकर्ता इनपुट, LLM प्रतिक्रियाहरू, उपकरण कलहरू, र उपकरण नतिजाहरूबीच संवाद प्रक्रियाको व्यवस्थापन गर्ने कम्पोनेन्टहरू।

- **उपकरण एकीकरण फ्रेमवर्क:** एजेन्टलाई विभिन्न उपकरणहरूसँग जडान गर्ने पूर्वाधार, चाहे ती साधारण फंक्शनहरू हुन् वा जटिल बाह्य सेवा।

- **त्रुटि ह्यान्डलिङ र मान्यता:** उपकरण कार्यान्वयनमा असफलता व्यवस्थापन गर्ने, प्यारामिटरहरू मान्य गर्ने र अप्रत्याशित प्रतिक्रियाहरू व्यवस्थापन गर्ने मेकानिज्महरू।

- **स्थिति व्यवस्थापन:** संवाद सन्दर्भ, पहिलेको उपकरण अन्तरक्रियाहरू र दीर्घकालीन डेटा ट्र्याक गर्ने जसले बहु-पटक अन्तरक्रियाहरूमा स्थिरता सुनिश्चित गर्छ।

अब, फंक्शन/उपकरण कलिङलाई विस्तारमा हेरौं।

### फंक्शन/उपकरण कलिङ

फंक्शन कलिङ ठूलो भाषाई मोडेलहरू (LLM) लाई उपकरणहरूसँग अन्तरक्रिया गर्न सक्षम पार्ने मुख्य तरिका हो। प्रायः 'फंक्शन' र 'उपकरण' शब्दहरू वैकल्पिक रूपमा प्रयोग गरिन्छ किनभने 'फंक्शनहरू' (पुन: प्रयोग गर्न मिल्ने कोडका ब्लकहरू) नै एजेन्टहरूले कार्य पूरा गर्न प्रयोग गर्ने 'उपकरण' हुन्। कुनै फंक्शनको कोड चलाउन, LLM ले प्रयोगकर्ताको अनुरोधलाई फंक्शनको विवरणसँग तुलना गर्नुपर्छ। यो गर्नका लागि सबै उपलब्ध फंक्शनहरूको विवरण भएको स्किमा LLM लाई पठाइन्छ। LLM ले त्यसपछि कार्यका लागि सबैभन्दा उपयुक्त फंक्शन चयन गरी त्यसको नाम र तर्कहरू फर्काउँछ। चयनित फंक्शनलाई कल गरिन्छ, यसको प्रतिक्रिया LLM लाई पठाइन्छ, जुन प्रयोगकर्ताको अनुरोधलाई जवाफ दिन प्रयोग गरिन्छ।

डेभलपरहरूलाई एजेन्टहरूको लागि फंक्शन कलिङ लागू गर्न यी कुरा आवश्यक पर्छ:

1. फंक्शन कलिङ समर्थन गर्ने LLM मोडेल
2. फंक्शन विवरण भएको स्किमा
3. प्रत्येक फंक्शनका लागि वर्णन गरिएको कोड

शहरमा हालको समय पत्ता लगाउने उदाहरण प्रयोग गरौं:

1. **फंक्शन कलिङ समर्थन गर्ने LLM आरम्भ गर्नुहोस्:**

    सबै मोडेलहरूले फंक्शन कलिङ समर्थन गर्दैनन्, त्यसैले तपाईं प्रयोग गरिरहनु भएको LLM ले समर्थन गर्छ कि गर्दैन जाँच गर्नु महत्त्वपूर्ण छ। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>ले फंक्शन कलिङ समर्थन गर्छ। हामी Azure OpenAI क्लाइन्ट सुरू गरेर सुरु गर्न सक्छौं।

    ```python
    # Azure OpenAI क्लायन्ट सुरु गर्नुहोस्
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **फंक्शन स्किमा सिर्जना गर्नुहोस्:**

    अब हामी JSON स्किमा परिभाषित गर्नेछौं जसमा फंक्शन नाम, फंक्शन के गर्छ भन्ने विवरण, र फंक्शनका प्यारामिटरहरूको नाम तथा विवरण समावेश हुनेछ।
    त्यसपछि यो स्किमा राखेर पहिले सिर्जना गरिएको क्लाइन्टलाई प्रयोगकर्ताको अनुरोधसहित पठाउनेछौं जसमा सेन फ्रान्सिस्कोको समय पत्ता लगाउने चाहना हुन्छ। ध्यान दिनुस्, फर्कने वस्तु **उपकरण कल** हुन्छ, प्रश्नको अन्तिम जवाफ होइन। पहिले भनिएझैं, LLM ले कार्यका लागि चयन गरेको फंक्शनको नाम र त्यसलाई दिइने तर्कहरू फर्काउँछ।

    ```python
    # मोडेलले पढ्नका लागि कार्य विवरण
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
  
    # पहिलो API कल: मोडेललाई फंक्शन प्रयोग गर्नुस् भनी सोध्नुहोस्
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
  
3. **कार्य सम्पादन गर्न आवश्यक फंक्शन कोड:**

    अब LLM ले कुन फंक्शन चलाउनु पर्ने छ भनेर चयन गरिसकेपछि, कार्य सञ्चालन गर्ने कोड लागू र कार्यान्वयन गर्नुपर्छ।
    हामी Python मा हालको समय पत्ता लगाउने कोड कार्यान्वयन गर्न सक्छौं। साथै, प्रतिक्रिया सन्देशबाट फंक्शन नाम र तर्कहरू निकाल्नुपर्ने कोड पनि लेख्नुपर्छ।

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
     # फङ्क्शन कलहरू व्यवस्थापन गर्नुहोस्
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

फंक्शन कलिङ अधिकांश, यदि सबै एजेण्ट उपकरण प्रयोग डिजाइन कोको भाग नभए पनि, यसको केन्द्रमा हुन्छ, यद्यपि शून्यबाट लागू गर्न कहिलेकाँही चुनौतीपूर्ण हुन सक्छ।
जस्तै हामीले [पाठ २](../../../02-explore-agentic-frameworks) मा सिक्यौं, एजेन्टिक फ्रेमवर्कहरूले उपकरण प्रयोगका लागि पूर्वनिर्मित निर्माण खण्डहरू उपलब्ध गराउँछन्।

## एजेन्टिक फ्रेमवर्कहरू संग उपकरण प्रयोगका उदाहरणहरू

यहाँ विभिन्न एजेन्टिक फ्रेमवर्कहरू प्रयोग गरी उपकरण प्रयोग डिजाइन ढाँचा लागू गर्ने केही उदाहरणहरू छन्:

### सेम्यान्टिक कर्नेल

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">सेम्यान्टिक कर्नेल</a> एक खुल्ला स्रोत AI फ्रेमवर्क हो जुन .NET, Python, र Java विकासकर्ताहरूका लागि हो जसले LLM हरू सँग काम गर्छन्। यसले फंक्शन कलिङ प्रक्रियालाई सजिलो बनाउँछ, तपाईंका फंक्शनहरू र तिनका प्यारामिटरहरूलाई मोडेललाई स्वचालित रूपमा वर्णन गर्न, जसलाई <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">सिरियलाइजिङ</a> भनिन्छ, प्रयोग गर्छ। यसले मोडेल र तपाईंको कोडबीच संवाद व्यवस्थापन पनि गर्छ। सेम्यान्टिक कर्नेल जस्तो एजेन्टिक फ्रेमवर्क प्रयोग गर्ने अर्को फाइदा के छ भने तपाईं पुस्तकालयमा पूर्वनिर्मित उपकरणहरू जस्तै <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">फाइल खोज</a> र <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">कोड इन्टरप्रेटर</a> पनि प्रयोग गर्न पाउनुहुन्छ।

तलको आरेखले सेम्यान्टिक कर्नेलसँग फंक्शन कलिङ प्रक्रियालाई देखाउँछ:

![function calling](../../../translated_images/ne/functioncalling-diagram.a84006fc287f6014.webp)

सेम्यान्टिक कर्नेलमा फंक्शन/उपकरणहरूलाई <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">प्लगइनहरू</a> भनिन्छ। हामी पहिले देखेको `get_current_time` फंक्शनलाई प्लगइनमा परिवर्तन गर्न सक्छौं, जसलाई कक्षामा परिणत गरेर भित्र फंक्शन राखिन्छ। हामी `kernel_function` डेकोरेटर आयात गर्न सक्छौं, जुन फंक्शनको वर्णन लिन्छ। त्यसपछि GetCurrentTimePlugin सँग कर्नेल सिर्जना गर्दा, कर्नेल स्वचालित रूपमा फंक्शन र तिनका प्यारामिटरहरू सिरियलाइज गर्छ, LLM लाई पठाउने स्किमा बनाउँछ।

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

# कर्नेल सिर्जना गर्नुहोस्
kernel = Kernel()

# प्लगइन सिर्जना गर्नुहोस्
get_current_time_plugin = GetCurrentTimePlugin(location)

# प्लगइनलाई कर्नेलमा थप्नुहोस्
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> भर्खरको एजेन्टिक फ्रेमवर्क हो जसले विकासकर्ताहरूलाई सुरक्षित रूपमा उच्च गुणस्तर र विस्तारयोग्य AI एजेन्टहरू बनाउन, तैनाथ गर्न, र मापन गर्न सशक्त बनाउँछ, जबकि आधारभूत कम्प्युट र स्टोरेज स्रोतहरू व्यवस्थापन गर्न आवश्यक पर्दैन। यो विशेष गरी उद्यम अनुप्रयोगहरूको लागि उपयोगी छ किनभने यो पूर्ण रूपमा प्रबन्धित सेवा हो र उद्यम-ग्रेड सुरक्षा प्रदान गर्छ।

LLM API सँग सिधै विकास गर्ने तुलना गर्दा, Azure AI Agent Service ले केही फाइदाहरू दिन्छ, जस्तै:

- स्वचालित उपकरण कलिङ – उपकरण कल पर्स गर्ने, उपकरण कल गर्ने, र प्रतिक्रिया ह्यान्डल गर्ने आवश्यकता छैन; यी सबै अब सर्भर-साइडमा हुन्छ।
- सुरक्षित रूपमा व्यवस्थापन गरिएको डेटा – संवाद अवस्थालाई आफैं व्यवस्थापन गर्ने सट्टा, तपाईं सबै आवश्यक जानकारी 'थ्रेड'मा संग्रह गर्न सक्छौं।
- रेडी-टु-यूज उपकरणहरू – तपाईंका डेटा स्रोतसँग अन्तरक्रिया गर्न प्रयोग गर्न सकिने उपकरणहरू, जस्तै Bing, Azure AI Search, र Azure Functions।

Azure AI Agent Service मा उपलब्ध उपकरणहरू दुई वर्गमा बाँडिएका छन्:

1. ज्ञान उपकरणहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing खोजसँग ग्राउन्डिङ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">फाइल खोज</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI खोज</a>

2. कार्य उपकरणहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">फंक्शन कलिङ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इन्टरप्रेटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित उपकरणहरू</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

एजेण्ट सेवा हामीलाई यी उपकरणहरूलाई `toolset`को रूपमा सँगै प्रयोग गर्न अनुमति दिन्छ। यसले `threads` पनि प्रयोग गर्छ जुन निश्चित संवादको सन्देश इतिहास ट्र्याक गर्छ।

कल्पना गर्नुहोस् तपाईं Contoso नामक कम्पनीमा बिक्री एजेण्ट हुनुहुन्छ। तपाईंले यस्तो संवादात्मक एजेन्ट विकास गर्न चाहनुहुन्छ जसले तपाईंको बिक्री डेटा सम्बन्धी प्रश्नहरूको जवाफ दिन सक्छ।

तलको छविले देखाउँछ कि तपाईं Azure AI Agent Service लाई प्रयोग गरी तपाईंको बिक्री डेटा विश्लेषण कसरी गर्न सक्नुहुन्छ:

![Agentic Service In Action](../../../translated_images/ne/agent-service-in-action.34fb465c9a84659e.webp)

यी उपकरणहरू मध्ये कुनै प्रयोग गर्नका लागि हामी क्लाइन्ट सिर्जना गरी उपकरण वा उपकरण समूह परिभाषित गर्न सक्छौं। व्यवहारमा यसलाई लागू गर्नका लागि तलको Python कोड प्रयोग गर्न सकिन्छ। LLM उपकरण समूह हेरेर प्रयोगकर्ताको अनुरोधअनुसार प्रयोगकर्ताले बनाएको फंक्शन `fetch_sales_data_using_sqlite_query` प्रयोग गर्ने वा पूर्वनिर्मित कोड इन्टरप्रेटर प्रयोग गर्ने निर्णय गर्नेछ।

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

# उपकरण सेट सुरूवात गर्नुहोस्
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query समारोह सहित function calling agent सुरु गर्नुहोस् र यसलाई उपकरण सेटमा थप्नुहोस्
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter उपकरण सुरूवात गर्नुहोस् र यसलाई उपकरण सेटमा थप्नुहोस्।
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## विश्वासयोग्य AI एजेन्टहरू बनाउन उपकरण प्रयोग डिजाइन ढाँचा प्रयोग गर्दा के विशेष विचार गर्नुपर्छ?

LLM द्वारा गतिशील रूपमा उत्पादन गरिने SQL सम्बन्धी सामान्य चिन्ता सुरक्षा हो, विशेष गरी SQL इनजेक्सन वा दुरुपयोग जस्ता जोखिमहरू, जस्तै डाटाबेस ड्रप गर्नु वा नक्कल पुर्न सजिलो हुने कार्यहरू। यी चिन्ताहरू मान्य भए तापनि, तिनीहरूलाई उचित डाटाबेस पहुँच अनुमति सेट गरेर प्रभावकारी रूपमा कम गर्न सकिन्छ। अधिकांश डाटाबेसमा यसका लागि डाटाबेसलाई रिड-ओन्लीमा सेट गरिन्छ। पोस्टग्रेसक्यूएल वा Azure SQL जस्ता डाटाबेस सेवाहरूका लागि एपलाई रिड-ओन्ली (SELECT) भूमिका दिनुपर्छ।
एप्लिकेसनलाई सुरक्षित वातावरणमा चलाउनुले सुरक्षा अझ बढाउँछ। उद्यमिक परिदृश्यहरूमा, डेटा सामान्यतया सञ्चालन प्रणालीहरूबाट निकाली र रूपान्तरण गरी पढ्न मात्र मिल्ने डेटाबेस वा डेटा वेयरहाउसमा राखिन्छ, जसको स्किमा प्रयोगकर्तामैत्री हुन्छ। यस तरिकाले डेटा सुरक्षित, प्रदर्शन र पहुँचका लागि अनुकूलित हुन्छ, र एप्लिकेसनलाई सीमित, पढ्न मात्र मिल्ने पहुँच मिल्छ।

## नमूना कोडहरू

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## उपकरण प्रयोग डिजाइन नमुनाहरू सम्बन्धी थप प्रश्नहरू छन्?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) मा सहभागी हुनुहोस्, अरु सिक्नेहरूलाई भेट्नुहोस्, अफिस अवरमा जानुहोस् र तपाईंका AI Agents सम्बन्धी प्रश्नहरूको जवाफ पाउनुहोस्।

## थप स्रोतहरू

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## अघिल्लो पाठ

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## अर्को पाठ

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यस दस्तावेजलाई एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया बुझ्नुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा असमीक्षताहरू हुन सक्छन्। मूल भाषा मा रहेको दस्तावेजलाई अधिकारिक स्रोतको रूपमा मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->