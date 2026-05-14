[![How to Design Good AI Agents](../../../translated_images/km/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ចុចរូបភាពខាងលើដើម្បីមើលវីដេអូមេរៀននេះ)_

# រចនាប័ទ្មការប្រើឧបករណ៍

ឧបករណ៍គឺគួរឱ្យចាប់អារម្មណ៍ដោយសារវាផ្ដល់ឱ្យភ្នាក់ងារតុល្យភាពធំទូលាយនៃសមត្ថភាព។ មិនត្រឹមតែភ្នាក់ងារមានសកម្មភាពកំណត់ដែលវាអាចអនុវត្តបានទេ ប៉ុន្តែដោយបន្ថែមឧបករណ៍មួយ ភ្នាក់ងារអាចអនុវត្តបានសកម្មភាពជាច្រើនជាងមុន។ ក្នុងជំពូកនេះ យើងនឹងពិនិត្យរចនាប័ទ្មការប្រើឧបករណ៍ ដែលពិពណ៌នាថាភ្នាក់ងារតុល្យភាពធំអាចប្រើឧបករណ៍ជាក់លាក់ដើម្បីសម្រេចគោលបំណងរបស់ពួកគេ។ 

## ការណែនាំ

ក្នុងមេរៀននេះ យើងកំពុងស្វែងរកចម្លើយសម្រាប់សំនួរចម្បងដូចខាងក្រោម៖

- រចនាប័ទ្មការប្រើឧបករណ៍គឺជាអ្វី?
- វាអាចអនុវត្តទៅករណីប្រើប្រាស់ណាខ្លះ?
- ធាតុ/ប្លុកស្នាដៃអ្វីខ្លះដែលត្រូវការ ដើម្បីអនុវត្តរចនាប័ទ្មនេះ?
- ការពិចារណាពិសេសអ្វីខ្លះក្នុងការប្រើរចនាប័ទ្មការប្រើឧបករណ៍ ដើម្បីបង្កើតភ្នាក់ងារតុល្យភាពខ្ពស់?

## គោលបំណងការសិក្សា

បន្ទាប់ពីបញ្ចប់មេរៀននេះ អ្នកនឹងអាច៖

- កំណត់អត្ថន័យរចនាប័ទ្មការប្រើឧបករណ៍ និងគោលបំណងវា។
- សម្គាល់ករណីប្រើប្រាស់ដែលអាចអនុវត្តរចនាប័ទ្មការប្រើឧបករណ៍។
- យល់ដឹងពីធាតុសំខាន់ៗដែលត្រូវការ ដើម្បីអនុវត្តរចនាប័ទ្មនេះ។
- ស្គាល់ការពិចារណាដើម្បីធានាថាភ្នាក់ងារដែលប្រើរចនាប័ទ្មនេះគឺគួរឱ្យទុកចិត្ត។

## រចនាប័ទ្មការប្រើឧបករណ៍គឺជាអ្វី?

**រចនាប័ទ្មការប្រើឧបករណ៍** ផ្តោតលើការផ្ដល់សមត្ថភាពឲ្យ LLMs អាចអន្តរប្រតិកម្មជាមួយឧបករណ៍ខាងក្រៅ ដើម្បីសម្រេចគោលបំណងជាក់លាក់។ ឧបករណ៍គឺជា​កូដ​ដែល​អាចត្រូវបាន​អ្នកភ្នាក់ងារអនុវត្ត​ដើម្បីអនុវត្តសកម្មភាពមួយ។ ឧបករណ៍អាចជាអនុគមន៍ស្រួលដូច​ជា គណនេយ្យករ រឺការហៅ API ទៅសេវាកម្មភាគីទីបី ដូចជាការស្វែងរកតម្លៃភាគហ៊ុនឬព្យាករណ៍អាកាសធាតុ។ ក្នុងបរិបទរបស់ភ្នាក់ងារតុល្យភាពធំ ឧបករណ៍ត្រូវបានរចនាឡើងសម្រាប់អនុវត្តដោយភ្នាក់ងារឆ្លើយតបនឹង **ការហៅអនុគមន៍ដែលបង្កើតដោយម៉ូដែល**។

## ករណីប្រើប្រាស់ណាខ្លះដែលវាអាចអនុវត្តទៅ?

ភ្នាក់ងារតុល្យភាពធំអាចប្រើឧបករណ៍ដើម្បីបញ្ចប់ភារកិច្ចស្មុគស្មាញ យកព័ត៌មាន ឬក៏ទទួលសេចក្ដីសម្រេចចិត្ត។ រចនាប័ទ្មការប្រើឧបករណ៍ត្រូវប្រើជាញឹកញាប់នៅក្នុងសេណារីយ៉ូដែលទាមទារឱ្យមានអន្តរប្រតិកម្មឆាប់រហ័សជាមួយប្រព័ន្ធខាងក្រៅ ដូចជាថតរៀបរងទិន្នន័យ សេវាកម្មបណ្ដាញ ឬអ្នកបកស្រាយកូដ។ សមត្ថភាពនេះមានប្រយោជន៍សម្រាប់ករណីប្រើប្រាស់ផ្សេងៗដូចជា៖

- **ការយកព័ត៌មានស្ម័គ្រចិត្ត:** ភ្នាក់ងារអាចសួរពាក់ព័ន្ធទៅលើ APIs រឺថតរៀបរងទិន្នន័យខាងក្រៅ ដើម្បីទទួលបានទិន្នន័យទាន់សម័យ (ឧ. សួរថតរៀបរង SQLite សម្រាប់វិភាគទិន្នន័យ ឬយកតម្លៃភាគហ៊ុន ឬព័ត៌មានអាកាសធាតុ)។
- **ការអនុវត្តកូដ និងការបកស្រាយ:** ភ្នាក់ងារអាចអនុវត្តកូដ ឬស្គ្រីប ដើម្បីដោះស្រាយបញ្ហាគណិតវិទ្យា បង្កើតរបាយការណ៍ ឬអនុវត្តសមីការស្ម័គ្រចិត្ត។
- **ជំហានស្វ័យប្រវត្តិកម្ម:** ជួយស្វ័យប្រវត្តិកម្មចំពោះរបៀបបញ្ញើច្រើនជំហាន ឬរបៀបដែលមានការធ្វើឡើងឡើងវិញ ដោយបញ្ចូលឧបករណ៍ដូចជា អ្នកកំណត់កាលវិភាគ កម្មវិធីអ៊ីមែល ឬបណ្តារទិន្នន័យ។
- **សេវាកម្មគាំទ្រអតិថិជន:** ភ្នាក់ងារអាចអន្តរប្រតិកម្មជាមួយប្រព័ន្ធ CRM វេទិកាការគ្រប់គ្រងសំបុត្រ ឬមូលដ្ឋានចំណេះដឹង ដើម្បីដោះស្រាយសំណួរអ្នកប្រើប្រាស់។
- **ការចេញផ្សាយ និងកែសម្រួលមាតិកា:** ភ្នាក់ងារអាចប្រើឧបករណ៍ដូចជា កម្មវិធីត្រួតពិនិត្យវេយ្យាករណ៍ ឧបករណ៍សង្ខេបអត្ថបទ ឬកម្មវិធីវាយតម្លៃសុវត្ថិភាពមាតិកា ដើម្បីជួយក្នុងកិច្ចការបង្កើតមាតិការបស់ពួកគេ។

## ធាតុ/ប្លុកស្នាដៃអ្វីខ្លះដែលត្រូវការ ដើម្បីអនុវត្តរចនាប័ទ្មការប្រើឧបករណ៍?

ប្លុកស្នាដៃទាំងនេះអនុញ្ញាតឲ្យភ្នាក់ងារអាចអនុវត្តការងារច្រើនជាងមុន។ មកមើលធាតុសំខាន់ៗដែលត្រូវការ ដើម្បីអនុវត្តរចនាប័ទ្មការប្រើឧបករណ៍៖

- **Function/Tool Schemas**: កំណត់ន័យលម្អិតនៃឧបករណ៍ដែលមាន ស្របតាមឈ្មោះអនុគមន៍ គោលបំណង ប៉ារ៉ាម៉ែត្រត្រូវការ និងលទ្ធផលដែលរំពឹងទុក។ ស្កីម៉ា​ទាំងនេះអនុញ្ញាតឲ្យ LLM យល់ថាអ្វីជាឧបករណ៍ដែលមាន និងរបៀបបង្កើតសំណើត្រឹមត្រូវ។

- **Function Execution Logic**: គ្រប់គ្រងរបៀប និងពេលវេលាដែលឧបករណ៍ត្រូវបានហៅ សំរាប់បាតដ្ឋានលទ្ធផល និងបរិបទការសន្ទនា​របស់អ្នកប្រើ។ វាអាចរួមបញ្ចូលម៉ូឌុលផ្លាស់ប្ដូរ ឬយន្តការបញ្ជូនទៅទិស ដែលកំណត់ការប្រើឧបករណ៍យ៉ាងឆាប់រហ័ស។

- **Message Handling System**: ធាតុដែលគ្រប់គ្រងចរន្តសន្ទនារវាងការបញ្ចូលអ្នកប្រើ ការឆ្លើយតប LLM ការហៅឧបករណ៍ និងលទ្ធផលឧបករណ៍។

- **Tool Integration Framework**: វេទិកាដែលភ្ជាប់ភ្នាក់ងារទៅឧបករណ៍ខុសៗគ្នា ទោះបីជាអនុគមន៍សាមញ្ញ ឬសេវាកម្មខាងក្រៅស្មុគស្មាញក៏ដោយ។

- **Error Handling & Validation**: យន្តការដោះស្រាយបញ្ហាសម្រាប់ការបរាជ័យក្នុងការអនុវត្តឧបករណ៍ ត្រួតពិនិត្យប៉ារ៉ាម៉ែត្រ និងគ្រប់គ្រងការឆ្លើយតបមិនរំពឹងទុក។

- **State Management**: តាមដានបរិបទសន្ទនា ការប្រើឧបករណ៍មុនៗ និងទិន្នន័យដែលមាននៅរយៈពេលបញ្ជាក់ទាំងមូល ដើម្បីធានាសោភ័ណភាពក្នុងការប្រតិបត្តិជាបន្ទាប់ៗ។

បន្ទាប់មក យើងនឹងមើលដល់ការហៅ Function/Tool លម្អិតបន្ថែម។

### ការហៅ Function/Tool

ការហៅអនុគមន៍គឺជាវិធីសំខាន់សម្រាប់អនុញ្ញាតឲ្យ LLMs មានអន្តរប្រតិកម្មជាមួយឧបករណ៍។ អ្នកនឹងជួបប្រទៈឃើញពាក្យ 'Function' និង 'Tool' ត្រូវបានប្រើប្រាស់ជំនួសគ្នា ព្រោះ 'functions' (ប្លុកកូដដែលអាចប្រើឡើងវិញបាន) គឺជាឧបករណ៍ដែលភ្នាក់ងារใช้ដើម្បីអនុវត្តភារកិច្ច។ ដើម្បីអនុញ្ញាតឲ្យកូដអនុគមន៍ត្រូវរត់ LLM ត្រូវប្រៀបធៀបសំណើរ_user ជាមួយនឹងការពិពណ៌នាអនុគមន៍។ ដើម្បីធ្វើនេះ ស្កីម៉ា​មួយដែលមានការពិពណ៌នានៃអនុគមន៍ទាំងអស់ត្រូវត្រូវផ្ញើទៅ LLM។ LLM បន្ទាប់មកជ្រើសរើសអនុគមន៍សមរម្យបំផុតសម្រាប់ភារកិច្ច ហើយបញ្ជូនឈ្មោះ និងអាគុយម៉ង់ទៅវិញ។ អនុគមន៍ជ្រើសរើសត្រូវបានហៅ ហើយលទ្ធផលត្រូវបានផ្ញើទៅ LLM ដែលប្រើព័ត៌មានដើម្បីឆ្លើយតបសំណើរបស់អ្នកប្រើ។ 

សម្រាប់អ្នកអភិវឌ្ឍន៍ដើម្បីអនុវត្តការហៅអនុគមន៍សម្រាប់ភ្នាក់ងារ អ្នកត្រូវការ៖

1. ម៉ូដែល LLM ដែលគាំទ្រការហៅអនុគមន៍
2. ស្កីម៉ាដែលមានការពិពណ៌នាអនុគមន៍
3. កូដសម្រាប់អនុគមន៍នីមួយៗដែលបានពិពណ៌នា

យើងនឹងយកឧទាហរណ៍ការទទួលពេលវេលាបច្ចុប្បន្ននៅក្នុងទីក្រុងមួយ ដើម្បីបង្ហាញ៖

1. **ចាប់ផ្តើម LLM ដែលគាំទ្រការហៅអនុគមន៍៖**

    ម៉ូដែលមិនទាំងអស់គាំទ្រការហៅអនុគមន៍ទេ ដូច្នេះសំខាន់ណាស់ក្នុងការត្រួតពិនិត្យថា LLM ដែលអ្នកប្រើបច្ចុប្បន្នគាំទ្រឬអត់។ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> គាំទ្រការហៅអនុគមន៍។ យើងអាចចាប់ផ្តើមដោយការបង្កើតកឡាយអឺនឡាញ Azure OpenAI។

    ```python
    # ចាប់ផ្តើមអតិថិជន Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **បង្កើតស្កីម៉ាអនុគមន៍៖**

    បន្ទាប់មក យើងនឹងកំណត់ស្កីម៉ា JSON ដែលមានឈ្មោះអនុគមន៍ ការពិពណ៌នាអំពីអ្វីដែលអនុគមន៍ធ្វើ ហើយឈ្មោះ និងការពិពណ៌នាប៉ារ៉ាម៉ែត្រ។ 
    យើងនឹងផ្ញើស្កីម៉ានេះដល់កម客户端ដែលបានបង្កើតមុន ព្រមទាំងសំណើរបស់អ្នកប្រើ ដើម្បីស្វែងរកពេលវេលានៅ San Francisco។ យ៉ាងណាមិញ អ្វីដែលសំខាន់គឺ **ការហៅឧបករណ៍** គឺជាលទ្ធផលដែលត្រូវបានត្រឡប់មក មិនមែនចម្លើយចុងក្រោយជាអ្វីទេ។ ដូចដែលបានលើកឡើង មុននេះនោះ LLM បញ្ចូនឈ្មោះអនុគមន៍ដែលវាជ្រើសសម្រាប់ភារកម្ម និងអាគុយម៉ង់ដែលត្រូវផ្ញើទៅវា។

    ```python
    # ការពិពណ៌នាអំពីមុខងាសម្រាប់គម្លាតអាន
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
  
    # សារ​អ្នកប្រើដំបូង
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # ការហៅ API ដំបូង: សួរអោយម៉ូដែលប្រើមុខងារ
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # ដំណើរការឆ្លើយតបរបស់ម៉ូដែល
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **កូដអនុគមន៍ដែលត្រូវអនុវត្តភារកិច្ច៖**

    ឥឡូវនេះដែល LLM បានជ្រើសអនុគមន៍ យើងត្រូវអនុវត្តន៍កូដសម្រាប់អនុវត្តភារកិច្ច។
    យើងអាចអនុវត្តកូដដើម្បីទទួលពេលវេលាបច្ចុប្បន្នជារឿង Python។ យើងក៏ត្រូវតែសរសេរកូដដើម្បីយកឈ្មោះ និងអាគុយម៉ង់ពី response_message ដើម្បីទទួលបានលទ្ធផលចុងក្រោយ។

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
     # គ្រប់គ្រងការហៅមុខងារ
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
  
      # ការហៅ API ទីពីរ៖ យកប្រតិកម្មចុងក្រោយពីម៉ូឌែល
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

ការហៅអនុគមន៍គឺជាគន្លងចិត្តនៃរចនាប័ទ្មការប្រើឧបករណ៍ភ្នាក់ងារ ភាពស្មុគស្មាញនៃការអនុវត្តវាពីដើមអាចមានភាពលំបាកខ្លះ។
ដូចដែលយើងបានរៀននៅក្នុង [មេរៀន 2](../../../02-explore-agentic-frameworks) គ្រប់មូលដ្ឋាន agentic ផ្ដល់ឧបករណ៍ប្លុកស្នាដៃស្រេចជូនដើម្បីអនុវត្តការប្រើឧបករណ៍។ 

## ឧទាហរណ៍ការប្រើឧបករណ៍ជាមួយគ្រប់មូលដ្ឋាន Agentic

ខាងក្រោមនេះជាឧទាហរណ៍អំពីរបៀបអនុវត្តរចនាប័ទ្មការប្រើឧបករណ៍ដោយប្រើគ្រប់មូលដ្ឋាន agentic ផ្សេងៗគ្នា៖

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> គឺជាគ្រប់មូលដ្ឋាន AI បើកចំហសម្រាប់ការបង្កើតភ្នាក់ងារតុល្យភាពធំ។ វាសម្រួលចំណុចពិបាកនៃការហៅអនុគមន៍ ដោយអនុញ្ញាតឲ្យអ្នកកំណត់ឧបករណ៍ជាអនុគមន៍ Python ជាមួយ @tool decorator។ គ្រប់មូលដ្ឋាននេះគ្រប់គ្រងការអន្តរប្រតិកម្មរវាងម៉ូដែល និងកូដរបស់អ្នក។ វាក៏ផ្ដល់ឧបករណ៍ដែលបានបង្កើតរួចដូចជា File Search និង Code Interpreter តាមរយៈ AzureAIProjectAgentProvider ផងដែរ។

រូបភាពខាងក្រោមបង្ហាញដំណើរការហៅអនុគមន៍ជាមួយ Microsoft Agent Framework៖

![function calling](../../../translated_images/km/functioncalling-diagram.a84006fc287f6014.webp)

នៅក្នុង Microsoft Agent Framework ឧបករណ៍ត្រូវបានកំណត់ជាអនុគមន៍ដែលមានការតុបតែង។ យើងអាចបម្លែងអនុគមន៍ `get_current_time` ដែលយើងបានឃើញពីមុនទៅជាឧបករណ៍ ដោយប្រើ @tool decorator។ គ្រប់មូលដ្ឋាននឹងស្វ័យប្រវត្តិ serialize អនុគមន៍ និងប៉ារ៉ាម៉ែត្រ រួចបង្កើតស្កីម៉ាដើម្បីផ្ញើទៅ LLM។

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# បង្កើតអតិថិជន
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# បង្កើតភ្នាក់ងារមួយ និងរត់ជាមួយឧបករណ៍
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> គឺជាគ្រប់មូលដ្ឋាន agentic ថ្មី ដែលរចនាឡើងសម្រាប់អភិវឌ្ឍន៍ដោយសុវត្ថិភាព អាចដាក់បញ្ចូល ហើយវែងឆ្ងាយ សម្រាប់បង្កើតភ្នាក់ងារតុល្យភាពធំដែលផ្តល់គុណភាពខ្ពស់ និងបន្ថែមបេីកដំណើរការប្រេសសិនិងផ្ទុកទិន្នន័យមិនចាំបាច់បន្ទុកដោយផ្ទាល់។ វាមានប្រយោជន៍បំផុតសម្រាប់កម្មវិធីសហគ្រាស ពីព្រោះវាជាសេវាកម្មគ្រប់គ្រងពេញលេញ និងមានសុវត្ថិភាពថ្នាក់សហគ្រាស។

ប្រៀបធៀបពេលអភិវឌ្ឍជាមួយ LLM API ដោយផ្ទាល់ Azure AI Agent Service ផ្ដល់អត្ថប្រយោជន៍ខ្លះៗ រួមមាន៖

- ការហៅឧបករណ៍អូតូម៉ាទិក - មិនចាំបាច់ចេញពាក្យសុំ ការហៅឧបករណ៍ និងគ្រប់គ្រងចម្លើយទៀតទេ; អ្វីៗទាំងនេះត្រូវបានអនុវត្តនៅខាងម៉ាស៊ីនបម្រើ
- ទិន្នន័យគ្រប់គ្រងដោយសុវត្ថិភាព - មិនចាំបាច់គ្រប់គ្រងស្ថានភាពសន្ទនារបស់អ្នកដោយផ្ទាល់ទេ អ្នកអាចពឹងផ្អែកលើ threads សម្រាប់រក្សាទុកព័ត៌មានទាំងអស់
- ឧបករណ៍ដែលមានក្នុងប្រអប់ - ឧបករណ៍ដែលអាចប្រើសម្រាប់អន្តរប្រតិកម្មជាមួយប្រភពទិន្នន័យរបស់អ្នក ដូចជា Bing, Azure AI Search និង Azure Functions ។

ឧបករណ៍ដែលមានក្នុង Azure AI Agent Service អាចចែកជាប្រភេទពីរៈ

1. ឧបករណ៍ចំណេះដឹង៖
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">ការតភ្ជាប់ជាមួយ Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ស្វែងរកឯកសារ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. ឧបករណ៍សកម្មភាព៖
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ការហៅអនុគមន៍</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">ឧបករណ៍កំណត់រចនាសម្ព័ន្ធ OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

សេវាកម្ម Agent អនុញ្ញាតឲ្យយើងប្រើឧបករណ៍ទាំងនេះជាកម្មវិធី `toolset` មួយ។ វាក៏ប្រើ `threads` ដើម្បីរក្សាទុកប្រវត្តិការផ្ញើសារពីសន្ទនាតែមួយ។

សូមស្រមៃថាអ្នកជាភ្នាក់ងារលក់នៅក្រុមហ៊ុន Contoso។ អ្នកចង់បង្កើតភ្នាក់ងារសន្ទនា អាចឆ្លើយសំណួរអំពីទិន្នន័យលក់របស់អ្នក។

រូបភាពខាងក្រោមបង្ហាញរបៀបដែលអ្នកអាចប្រើ Azure AI Agent Service ដើម្បីវិភាគទិន្នន័យលក់របស់អ្នក៖

![Agentic Service In Action](../../../translated_images/km/agent-service-in-action.34fb465c9a84659e.webp)

ដើម្បីប្រើឧបករណ៍ណាដែលមានជាមួយសេវាកម្មនេះ យើងអាចបង្កើតអតិថិជន និងកំណត់ឧបករណ៍ ឬ toolset។ ដើម្បីអនុវត្តឲ្យមានប្រសិទ្ធភាព យើងអាចប្រើកូដ Python ខាងក្រោម។ LLM នឹងអាចមើល toolset ហើយសម្រេចថាតើត្រូវប្រើអនុគមន៍ដែលអ្នកប្រើបង្កើត `fetch_sales_data_using_sqlite_query` ឬ Code Interpreter ដែលបានបង្កើតរួចជាមធ្យោបាយ ដោយផ្អែកលើសំណើរបស់អ្នកប្រើ។

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # មុខងារ fetch_sales_data_using_sqlite_query ដែលអាចរកឃើញក្នុងឯកសារ fetch_sales_data_functions.py។
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ចាប់ផ្តើមកំណត់ឧបករណ៍
toolset = ToolSet()

# ចាប់ផ្តើមភ្នាក់ងារហៅមុខងារជាមួយមុខងារ fetch_sales_data_using_sqlite_query ហើយបន្ថែមវាទៅឧបករណ៍
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# ចាប់ផ្តើមឧបករណ៍ Interpreter Code ហើយបន្ថែមវាទៅឧបករណ៍។
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ការពិចារណាពិសេសសម្រាប់ការប្រើរចនាប័ទ្មការប្រើឧបករណ៍ ដើម្បីបង្កើតភ្នាក់ងារតុល្យភាពចំពោះតម្លៃទុកចិត្ត?

បញ្ហាទូទៅដែលមានជាមួយ SQL ដែលត្រូវបានបង្កើតឲ្យស្វ័យប្រវត្តិនៅ LLM គឺសុវត្ថិភាព ជាពិសេសគ្រោះថ្នាក់ SQL injection ឬសកម្មភាពមានគ្រោះថ្នាក់ ដូចជា ការលុប ឬបំភាន់ថតរៀបរាងទិន្នន័យ។ បើទោះបីជាបញ្ហាការពារនេះមានសុពលភាព ការបញ្ចៀសដោយត្រឹមត្រូវសិទ្ធិចូលដំណើរការថតរៀបរាងទិន្នន័យអាចទប់ស្កាត់វា។ សម្រាប់ប្រព័ន្ធភាគច្រើន វាគឺជាការកំណត់ថាថតរៀបរាងទិន្នន័យ៤បញ្ចូលគុណតែអាន (read-only)។ សម្រាប់សេវាកម្មថតរៀបរាងទិន្នន័យដូចជា PostgreSQL ឬ Azure SQL អ្នកប្រើប្រាស់ត្រូវបានផ្ដល់សិទ្ធិជាការអានតែប៉ុណ្ណោះ (SELECT role)។

ការប្រតិបត្តិកម្មនៅក្នុងបរិយាកាសមានសុវត្ថិភាពជួយបង្កើនការពារ។ នៅក្នុងសេណារីយ៉ូសហគ្រាស ទិន្នន័យត្រូវបានដកចេញ និងបម្លែងពីប្រព័ន្ធប្រតិបត្តិការ ទៅកាន់ថតរៀបរាងទិន្នន័យ read-only ឬឃ្លាំងទិន្នន័យដែលមានស្ដង់ដាគុណភាព។ វានាំឲ្យទិន្នន័យមានសុវត្ថិភាពប្រសើរឡើង មានល្បឿនប្រសើរនិងចូលប្រើបានងាយស្រួលក្នុងកម្មវិធី និងកម្មវិធីមានកំណត់ថ្មីៗក្នុងការអានប៉ុណ្ណោះ។

## កូដឧទាហរណ៍

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## មានសំនួរបន្ថែមអំពីរចនាប័ទ្មការប្រើឧបករណ៍ទេ?

ចូលរួមក្នុង [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ដើម្បីជួបជាមួយអ្នកសិក្សាផ្សេងទៀត ចូលរួមម៉ោងការិយាល័យ និងសួរសំណួរអំពីភ្នាក់ងារតុល្យភាពធំរបស់អ្នក។

## ប្រភពព័ត៌មានបន្ថែម

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">សិក្ខាសាលាសេវាភ្នាក់ងារ Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">សិក្ខាសាលាភ្នាក់ងារចម្លើយច្នៃប្រឌិត Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">ទិដ្ឋភាពទូទៅ Microsoft Agent Framework</a>

## មេរៀនមុន

[ការយល់ដឹងពីរចនាប័ទ្ម Agentic](../03-agentic-design-patterns/README.md)

## មេរៀនបន្ទាប់
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->