<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:10:01+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "ne"
}
-->
[![कसरी राम्रो एआई एजेन्ट डिजाइन गर्ने](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.ne.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(माथिको तस्बिरमा क्लिक गरेर यस पाठको भिडियो हेर्नुहोस्)_

# टूल प्रयोग डिजाइन ढाँचा

टूलहरू रोचक छन् किनभने तिनीहरूले एआई एजेन्टहरूलाई व्यापक क्षमताहरू प्रदान गर्छन्। एजेन्टले सीमित कार्यहरू मात्र गर्न सक्ने सट्टा, टूल थप्दा एजेन्टले धेरै प्रकारका कार्यहरू गर्न सक्छ। यस अध्यायमा, हामी टूल प्रयोग डिजाइन ढाँचाको अध्ययन गर्नेछौं, जसले एआई एजेन्टहरूले विशिष्ट टूलहरू प्रयोग गरेर आफ्नो लक्ष्य प्राप्त गर्ने तरिका वर्णन गर्दछ।

## परिचय

यस पाठमा, हामी निम्न प्रश्नहरूको उत्तर खोज्दैछौं:

- टूल प्रयोग डिजाइन ढाँचा के हो?
- यसलाई कुन उपयोग केसहरूमा लागू गर्न सकिन्छ?
- डिजाइन ढाँचा कार्यान्वयन गर्न आवश्यक तत्वहरू/निर्माण ब्लकहरू के हुन्?
- विश्वासयोग्य एआई एजेन्ट निर्माण गर्न टूल प्रयोग डिजाइन ढाँचाको प्रयोग गर्दा विशेष विचारहरू के हुन्?

## सिकाइ लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं सक्षम हुनुहुनेछ:

- टूल प्रयोग डिजाइन ढाँचा र यसको उद्देश्य परिभाषित गर्नुहोस्।
- टूल प्रयोग डिजाइन ढाँचा लागू गर्न सकिने उपयोग केसहरू पहिचान गर्नुहोस्।
- डिजाइन ढाँचा कार्यान्वयन गर्न आवश्यक प्रमुख तत्वहरू बुझ्नुहोस्।
- यस डिजाइन ढाँचाको प्रयोग गर्ने एआई एजेन्टहरूको विश्वासयोग्यता सुनिश्चित गर्न विचारहरू पहिचान गर्नुहोस्।

## टूल प्रयोग डिजाइन ढाँचा के हो?

**टूल प्रयोग डिजाइन ढाँचा** LLMs लाई बाह्य टूलहरूसँग अन्तरक्रिया गर्न र विशिष्ट लक्ष्यहरू प्राप्त गर्न सक्षम बनाउनेमा केन्द्रित छ। टूलहरू कोड हुन् जसलाई एजेन्टले कार्यहरू गर्न कार्यान्वयन गर्न सक्छ। टूल एक साधारण कार्य हुन सक्छ जस्तै क्यालकुलेटर, वा तेस्रो-पक्ष सेवामा API कल जस्तै स्टक मूल्य हेर्ने वा मौसम पूर्वानुमान। एआई एजेन्टहरूको सन्दर्भमा, टूलहरू **मोडल-उत्पन्न कार्य कलहरू**को प्रतिक्रिया स्वरूप एजेन्टहरूले कार्यान्वयन गर्न डिजाइन गरिएका छन्।

## यसलाई कुन उपयोग केसहरूमा लागू गर्न सकिन्छ?

एआई एजेन्टहरूले जटिल कार्यहरू पूरा गर्न, जानकारी पुनःप्राप्त गर्न, वा निर्णय लिन टूलहरू प्रयोग गर्न सक्छन्। टूल प्रयोग डिजाइन ढाँचा प्रायः बाह्य प्रणालीहरूसँग गतिशील अन्तरक्रिया आवश्यक पर्ने परिदृश्यहरूमा प्रयोग गरिन्छ, जस्तै डेटाबेस, वेब सेवाहरू, वा कोड इन्टरप्रेटरहरू। यो क्षमता विभिन्न उपयोग केसहरूको लागि उपयोगी छ, जसमा समावेश छन्:

- **गतिशील जानकारी पुनःप्राप्ति:** एजेन्टहरूले बाह्य API वा डेटाबेसहरू सोधपुछ गरेर अद्यावधिक डेटा प्राप्त गर्न सक्छन् (जस्तै, SQLite डेटाबेस सोधपुछ गरेर डेटा विश्लेषण, स्टक मूल्य वा मौसम जानकारी प्राप्त गर्दै)।
- **कोड कार्यान्वयन र व्याख्या:** एजेन्टहरूले गणितीय समस्याहरू समाधान गर्न, रिपोर्टहरू उत्पन्न गर्न, वा सिमुलेशनहरू गर्न कोड वा स्क्रिप्टहरू कार्यान्वयन गर्न सक्छन्।
- **कार्यप्रवाह स्वचालन:** कार्य तालिकाहरू, इमेल सेवाहरू, वा डेटा पाइपलाइनहरू जस्ता टूलहरू एकीकृत गरेर दोहोरिने वा बहु-चरण कार्यप्रवाहहरू स्वचालित गर्दै।
- **ग्राहक समर्थन:** एजेन्टहरूले CRM प्रणालीहरू, टिकटिङ प्लेटफर्महरू, वा ज्ञान आधारहरूसँग अन्तरक्रिया गरेर प्रयोगकर्ता प्रश्नहरूको समाधान गर्न सक्छन्।
- **सामग्री निर्माण र सम्पादन:** एजेन्टहरूले व्याकरण जाँचकर्ता, पाठ संक्षेपकर्ता, वा सामग्री सुरक्षा मूल्यांकनकर्ताजस्ता टूलहरू प्रयोग गरेर सामग्री निर्माण कार्यहरूमा सहयोग गर्न सक्छन्।

## टूल प्रयोग डिजाइन ढाँचा कार्यान्वयन गर्न आवश्यक तत्वहरू/निर्माण ब्लकहरू के हुन्?

यी निर्माण ब्लकहरूले एआई एजेन्टलाई धेरै प्रकारका कार्यहरू गर्न सक्षम बनाउँछन्। टूल प्रयोग डिजाइन ढाँचा कार्यान्वयन गर्न आवश्यक प्रमुख तत्वहरू हेरौं:

- **कार्य/टूल स्कीमाहरू:** उपलब्ध टूलहरूको विस्तृत परिभाषा, जसमा कार्यको नाम, उद्देश्य, आवश्यक प्यारामिटरहरू, र अपेक्षित आउटपुटहरू समावेश छन्। यी स्कीमाहरूले LLM लाई उपलब्ध टूलहरू के हुन् र मान्य अनुरोधहरू कसरी निर्माण गर्ने भनेर बुझ्न सक्षम बनाउँछन्।

- **कार्य कार्यान्वयन तर्क:** प्रयोगकर्ताको उद्देश्य र संवाद सन्दर्भको आधारमा टूलहरू कहिले र कसरी आह्वान गरिन्छ भन्ने शासित गर्दछ। यसमा योजनाकार मोड्युलहरू, राउटिङ मेकानिज्महरू, वा सशर्त प्रवाहहरू समावेश हुन सक्छन् जसले गतिशील रूपमा टूल प्रयोग निर्धारण गर्दछ।

- **सन्देश ह्यान्डलिङ प्रणाली:** प्रयोगकर्ता इनपुटहरू, LLM प्रतिक्रियाहरू, टूल कलहरू, र टूल आउटपुटहरू बीचको संवाद प्रवाह व्यवस्थापन गर्ने घटकहरू।

- **टूल एकीकरण फ्रेमवर्क:** एजेन्टलाई विभिन्न टूलहरूसँग जडान गर्ने पूर्वाधार, चाहे ती साधारण कार्यहरू हुन् वा जटिल बाह्य सेवाहरू।

- **त्रुटि ह्यान्डलिङ र मान्यता:** टूल कार्यान्वयनमा असफलता व्यवस्थापन गर्न, प्यारामिटरहरू मान्य गर्न, र अप्रत्याशित प्रतिक्रियाहरू व्यवस्थापन गर्नका लागि संयन्त्रहरू।

- **राज्य व्यवस्थापन:** संवाद सन्दर्भ, अघिल्लो टूल अन्तरक्रिया, र स्थायी डेटा ट्र्याक गर्दै बहु-टर्न अन्तरक्रियाहरूमा निरन्तरता सुनिश्चित गर्न।

अब, कार्य/टूल कलिङलाई विस्तृत रूपमा हेरौं।

### कार्य/टूल कलिङ

कार्य कलिङ LLMs लाई टूलहरूसँग अन्तरक्रिया गर्न सक्षम बनाउने प्राथमिक तरिका हो। तपाईंले प्रायः 'कार्य' र 'टूल'लाई परस्पर प्रयोग गरिएको देख्नुहुनेछ किनभने 'कार्यहरू' (पुनः प्रयोग गर्न मिल्ने कोडका ब्लकहरू) 'टूलहरू' हुन् जुन एजेन्टहरूले कार्यहरू पूरा गर्न प्रयोग गर्छन्। कार्यको कोड आह्वान गर्नको लागि, LLM ले प्रयोगकर्ताको अनुरोधलाई कार्यको विवरणसँग तुलना गर्नुपर्छ। यसका लागि उपलब्ध कार्यहरूको विवरणहरू समावेश भएको स्कीमा LLM लाई पठाइन्छ। त्यसपछि LLM ले कार्यको नाम र तर्कहरू फिर्ता गर्दै कार्यको लागि सबैभन्दा उपयुक्त कार्य चयन गर्दछ। चयन गरिएको कार्य आह्वान गरिन्छ, यसको प्रतिक्रिया LLM लाई फिर्ता पठाइन्छ, जसले प्रयोगकर्ताको अनुरोधको उत्तर दिन जानकारी प्रयोग गर्दछ।

एजेन्टहरूको लागि कार्य कलिङ कार्यान्वयन गर्न, विकासकर्ताहरूलाई आवश्यक छ:

1. कार्य कलिङ समर्थन गर्ने LLM मोडेल
2. कार्य विवरणहरू समावेश भएको स्कीमा
3. प्रत्येक वर्णन गरिएको कार्यको कोड

सहरमा वर्तमान समय प्राप्त गर्ने उदाहरण प्रयोग गरौं:

1. **कार्य कलिङ समर्थन गर्ने LLM आरम्भ गर्नुहोस्:**

    सबै मोडेलहरूले कार्य कलिङ समर्थन गर्दैनन्, त्यसैले तपाईंले प्रयोग गरिरहेको LLM ले समर्थन गर्छ कि गर्दैन जाँच गर्नु महत्त्वपूर्ण छ। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> कार्य कलिङ समर्थन गर्दछ। हामी Azure OpenAI क्लाइन्ट आरम्भ गरेर सुरु गर्न सक्छौं।

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **कार्य स्कीमा सिर्जना गर्नुहोस्:**

    त्यसपछि हामी JSON स्कीमा परिभाषित गर्नेछौं जसमा कार्यको नाम, कार्यले के गर्छ भन्ने विवरण, र कार्य प्यारामिटरहरूको नाम र विवरण समावेश हुनेछ। हामी यस स्कीमालाई पहिले सिर्जना गरिएको क्लाइन्टमा प्रयोगकर्ताको अनुरोधसँगै पास गर्नेछौं। महत्त्वपूर्ण कुरा के हो भने **टूल कल** फिर्ता हुन्छ, **प्रश्नको अन्तिम उत्तर होइन।** जस्तै पहिले उल्लेख गरिएको थियो, LLM ले कार्यको नाम र तर्कहरू फिर्ता गर्छ जुन कार्यान्वयन गरिनेछ।

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
  
1. **कार्य पूरा गर्न आवश्यक कार्यको कोड:**

    अब LLM ले कुन कार्य चलाउनुपर्नेछ भनेर चयन गरिसकेको छ, कार्य पूरा गर्न आवश्यक कोड कार्यान्वयन र कार्यान्वयन गर्नुपर्छ। 
    हामी Python मा वर्तमान समय प्राप्त गर्न कोड कार्यान्वयन गर्न सक्छौं। हामीले प्रतिक्रिया सन्देशबाट नाम र तर्कहरू निकाल्न कोड पनि लेख्नुपर्छ।

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

कार्य कलिङ अधिकांश, यदि सबै होइन भने, एजेन्ट टूल प्रयोग डिजाइनको केन्द्रमा छ, तर यसलाई सुरुबाट कार्यान्वयन गर्न कहिलेकाहीं चुनौतीपूर्ण हुन सक्छ। 
जसरी हामीले [Lesson 2](../../../02-explore-agentic-frameworks) मा सिक्यौं, एजेन्टिक फ्रेमवर्कहरूले हामीलाई टूल प्रयोग कार्यान्वयन गर्न पूर्वनिर्मित निर्माण ब्लकहरू प्रदान गर्छ।

## एजेन्टिक फ्रेमवर्कहरूसँग टूल प्रयोगका उदाहरणहरू

यहाँ विभिन्न एजेन्टिक फ्रेमवर्कहरू प्रयोग गरेर टूल प्रयोग डिजाइन ढाँचा कार्यान्वयन गर्ने केही उदाहरणहरू छन्:

### सेम्यान्टिक कर्नेल

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">सेम्यान्टिक कर्नेल</a> .NET, Python, र Java विकासकर्ताहरूका लागि खुला-स्रोत एआई फ्रेमवर्क हो जसले LLMs सँग काम गर्छ। यसले कार्य कलिङको प्रयोग प्रक्रिया सरल बनाउँछ जसले तपाईंको कार्यहरू र तिनीहरूको प्यारामिटरहरूलाई मोडेलमा स्वचालित रूपमा वर्णन गर्ने प्रक्रिया <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">सिरियलाइजिङ</a> मार्फत गर्छ। यसले मोडेल र तपाईंको कोड बीचको संवाद पनि व्यवस्थापन गर्छ। सेम्यान्टिक कर्नेल जस्तो एजेन्टिक फ्रेमवर्क प्रयोग गर्ने अर्को फाइदा भनेको यसले तपाईंलाई <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">फाइल खोज</a> र <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">कोड इन्टरप्रेटर</a> जस्ता पूर्वनिर्मित टूलहरू पहुँच गर्न अनुमति दिन्छ।

निम्न चित्रले सेम्यान्टिक कर्नेलसँग कार्य कलिङको प्रक्रिया चित्रण गर्दछ:

![कार्य कलिङ](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.ne.png)

सेम्यान्टिक कर्नेलमा कार्यहरू/टूलहरू <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">प्लगइनहरू</a> भनिन्छ। हामीले पहिले देखेको `get_current_time` कार्यलाई कक्षामा परिणत गरेर प्लगइनमा रूपान्तरण गर्न सक्छौं। हामीले कार्यको विवरण लिने `kernel_function` डेकोरेटर पनि आयात गर्न सक्छौं। जब तपाईं GetCurrentTimePlugin सहित कर्नेल सिर्जना गर्नुहुन्छ, कर्नेलले स्वचालित रूपमा कार्य र यसको प्यारामिटरहरू सिरियलाइज गर्नेछ, प्रक्रिया मा LLM लाई पठाउन स्कीमा सिर्जना गर्नेछ।

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
  
### Azure AI एजेन्ट सेवा

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI एजेन्ट सेवा</a> नयाँ एजेन्टिक फ्रेमवर्क हो जसले विकासकर्ताहरूलाई उच्च-गुणस्तर र विस्तारयोग्य एआई एजेन्टहरू सुरक्षित रूपमा निर्माण, परिनियोजन, र स्केल गर्न सशक्त बनाउँछ। यसले अन्तर्निहित कम्प्युट र भण्डारण स्रोतहरू व्यवस्थापन गर्न आवश्यक पर्दैन। यो विशेष रूपमा उद्यम अनुप्रयोगहरूको लागि उपयोगी छ किनभने यो पूर्ण रूपमा व्यवस्थापित सेवा हो जसमा उद्यम स्तरको सुरक्षा छ।

LLM API सँग प्रत्यक्ष विकासको तुलनामा, Azure AI एजेन्ट सेवाले केही फाइदाहरू प्रदान गर्दछ, जसमा समावेश छन्:

- स्वचालित टूल कलिङ – टूल कल पार्स गर्न, टूल आह्वान गर्न, र प्रतिक्रिया ह्यान्डल गर्न आवश्यक छैन; यो सबै अब सर्भर-साइडमा गरिन्छ।
- सुरक्षित रूपमा व्यवस्थापित डेटा – तपाईंको आफ्नै संवाद अवस्था व्यवस्थापन गर्ने सट्टा, तपाईंले आवश्यक सबै जानकारी भण्डारण गर्न थ्रेडहरूमा भर पर्न सक्नुहुन्छ।
- आउट-ऑफ-द-बक्स टूलहरू – तपाईंको डेटा स्रोतहरूसँग अन्तरक्रिया गर्न प्रयोग गर्न सकिने टूलहरू, जस्तै Bing, Azure AI खोज, र Azure कार्यहरू।

Azure AI एजेन्ट सेवामा उपलब्ध टूलहरू दुई श्रेणीमा विभाजित गर्न सकिन्छ:

1. ज्ञान टूलहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing खोजको साथ ग्राउन्डिङ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">फाइल खोज</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI खोज</a>

2. कार्य टूलहरू:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">कार्य कलिङ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">कोड इन्टरप्रेटर</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI परिभाषित टूलहरू</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure कार्यहरू</a>

एजेन्ट सेवाले हामीलाई यी टूलहरूलाई `toolset` को रूपमा सँगै प्रयोग गर्न अनुमति दिन्छ। यसले `threads` पनि प्रयोग गर्दछ जसले विशेष संवादबाट सन्देशहरूको इतिहास ट्र्याक गर्दछ।

कल्पना गर्नुहोस् कि तपाईं Contoso नामक कम्पनीमा बिक्री एजेन्ट हुनुहुन्छ। तपाईं आफ्नो बिक्री डेटा बारे प्रश्नहरूको उत्तर दिन सक्ने संवादात्मक एजेन्ट विकास गर्न चाहनुहुन्छ।

निम्न चित्रले Azure AI एजेन्ट सेवा प्रयोग गरेर तपाईंको बिक्री डेटा विश्लेषण गर्ने तरिका चित्रण गर्दछ:

![एजेन्टिक सेवा कार्यमा](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.ne.jpg)

सेवाको साथ कुनै पनि टूल प्रयोग गर्न हामी क्लाइन्ट सिर्जना गर्न सक्छौं र टूल वा टूलसेट परिभाषित गर्न सक्छौं। यसलाई व्यावहारिक रूपमा कार्यान्वयन गर्न हामी निम्न Python कोड प्रयोग गर्न सक्छौं। LLM ले टूलसेट हेर्न सक्नेछ र प्रयोगकर्ताको अनुरोधको आधारमा प्रयोगकर्ता द्वारा सिर्जना गरिएको कार्य `fetch_sales_data_using_sqlite_query` वा पूर्वनिर्मित कोड इन्टरप्रेटर प्रयोग गर्ने निर्णय गर्नेछ।

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

## विश्वासयोग्य एआई एजेन्ट निर्माण गर्न टूल प्रयोग डिजाइन ढाँचाको प्रयोग गर्दा विशेष विचारहरू के हुन्?

LLMs द्वारा गतिशील रूपमा उत्पन्न SQL सँग सम्बन्धित सामान्य चिन्ता सुरक्षा हो, विशेष गरी SQL इन्जेक्शन वा हानिकारक कार्यहरूको जोखिम, जस्तै डेटाबेस हटाउने वा छेडछाड गर्ने। यद्यपि यी चिन्ताहरू मान्य छन्, डेटाबेस पहुँच अनुमतिहरू उचित रूपमा कन्फिगर गरेर प्रभावकारी रूपमा कम गर्न सकिन्छ। अधिकांश डेटाबेसहरूको लागि यसमा डेटाबेसलाई केवल-पढ्न सकिने रूपमा कन्फिगर गर्नु समावेश छ। PostgreSQL वा Azure SQL जस्ता डेटाबेस सेवाहरूको लागि, एपलाई केवल-पढ्न सकिने (SELECT) भूमिका असाइन गर्नुपर्छ।
एपलाई सुरक्षित वातावरणमा चलाउँदा सुरक्षा अझै बढ्छ। उद्यम परिदृश्यहरूमा, डाटा प्रायः सञ्चालन प्रणालीहरूबाट निकालिन्छ र रूपान्तरण गरिन्छ, त्यसपछि प्रयोगकर्ता-अनुकूल स्किमासहितको केवल-पढ्न मिल्ने डाटाबेस वा डाटा वेयरहाउसमा राखिन्छ। यस दृष्टिकोणले सुनिश्चित गर्दछ कि डाटा सुरक्षित छ, प्रदर्शन र पहुँचको लागि अनुकूलित छ, र एपलाई सीमित, केवल-पढ्न मिल्ने पहुँच मात्र छ।

## नमूना कोडहरू

- Python: [एजेन्ट फ्रेमवर्क](./code_samples/04-python-agent-framework.ipynb)
- .NET: [एजेन्ट फ्रेमवर्क](./code_samples/04-dotnet-agent-framework.md)

## उपकरण प्रयोग डिजाइन ढाँचाहरूको बारेमा थप प्रश्नहरू छन्?

अन्य सिक्नेहरू भेट्न, कार्यालय समयमा सहभागी हुन, र तपाईंका AI एजेन्टहरूको प्रश्नहरूको उत्तर पाउन [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस्।

## थप स्रोतहरू

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI एजेन्ट सेवा कार्यशाला</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer बहु-एजेन्ट कार्यशाला</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">सेम्यान्टिक कर्नेल फङ्सन कलिङ ट्युटोरियल</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">सेम्यान्टिक कर्नेल कोड इन्टरप्रेटर</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen उपकरणहरू</a>

## अघिल्लो पाठ

[एजेन्टिक डिजाइन ढाँचाहरू बुझ्दै](../03-agentic-design-patterns/README.md)

## अर्को पाठ

[एजेन्टिक RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मूल भाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->