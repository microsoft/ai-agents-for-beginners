# ការអភិវឌ្ឍសេវាកម្មភ្នាក់ងារផោនដ្រីរបស់ Microsoft

នៅក្នុងហ្វឹកហាត់នេះ អ្នកប្រើម៉ាស៊ីនមេភ្នាក់ងារផោនដ្រីរបស់ Microsoft នៅក្នុង [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) ដើម្បីបង្កើតភ្នាក់ងារសម្រាប់ការកក់ផ្លូវហោះហើរ។ ភ្នាក់ងារនឹងអាចធ្វើអន្តរកម្មជាមួយអ្នកប្រើហើយផ្តល់ព័ត៌មានអំពីការហោះហើរ។

## លក្ខខណ្ឌមុន

ដើម្បីបញ្ចប់ហ្វឹកហាត់នេះ អ្នកត្រូវការដូចខាងក្រោម៖
1. គណនី Azure ដែលមានការជាវសកម្ម។ [បង្កើតគណនីដោយឥតគិតថ្លៃ](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)។
2. អ្នកត្រូវការអាជ្ញាសិទ្ធិចំពោះការបង្កើតមជ្ឈមណ្ឌល Microsoft Foundry ឬមានមជ្ឈមណ្ឌលត្រូវបានបង្កើតសម្រាប់អ្នក។
    - ប្រសិនបើតួនាទីរបស់អ្នកគឺជា Contributor ឬ Owner អ្នកអាចអនុវត្តជំហានក្នុងមគ្គុទេសក៍នេះបាន។

## បង្កើតមជ្ឈមណ្ឌល Microsoft Foundry

> **ចំណាំ:** Microsoft Foundry គឺជាឈ្មោះថ្មីសម្រាប់ Azure AI Studio។

1. អនុវត្តតាមមគ្គុទេសក៏ពី [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) សម្រាប់ការបង្កើតមជ្ឈមណ្ឌល Microsoft Foundry។
2. នៅពេលដែលគម្រោងរបស់អ្នកត្រូវបានបង្កើត បិទបង្ហាញណែនាំណាមួយហើយពិនិត្យមើលទំព័រគម្រោងនៅក្នុងកំពូល Microsoft Foundry ដែលគួរតែមានរូបរាងដូចរូបខាងក្រោម៖

    ![Microsoft Foundry Project](../../../translated_images/km/azure-ai-foundry.88d0c35298348c2f.webp)

## បញ្ចេញម៉ូដែល

1. នៅផ្នែកឆ្វេងសម្រាប់គម្រោងរបស់អ្នក នៅផ្នែក **My assets** ជ្រើសរើសទំព័រ **Models + endpoints**។
2. នៅក្នុងទំព័រ **Models + endpoints** នៅផ្ទាំង **Model deployments** នៅក្នុងម៉ឺនុយ **+ Deploy model** ជ្រើសរើស **Deploy base model**។
3. ស្វែងរកម៉ូដែល `gpt-5-mini` នៅក្នុងបញ្ជី ហើយបន្ទាប់មកជ្រើសរើស និងបញ្ចាក់វិញ។

    > **ចំណាំ**: ការបន្ថយ TPM ជួយបំបាត់ការប្រើប្រាស់បរិមាណសេវាកម្មលើសពីការជាវដែលអ្នកកំពុងប្រើ។

    ![Model Deployed](../../../translated_images/km/model-deployment.3749c53fb81e18fd.webp)

## បង្កើតភ្នាក់ងារ

ពេលនេះអ្នកបានបញ្ចេញម៉ូដែលហើយ អ្នកអាចបង្កើតភ្នាក់ងារ។ ភ្នាក់ងារជាម៉ូដែល AI ជជែកសន្ទនាដែលអាចប្រើសម្រាប់ធ្វើអន្តរកម្មជាមួយអ្នកប្រើ។

1. នៅផ្នែកឆ្វេងសម្រាប់គម្រោងរបស់អ្នក នៅផ្នែក **Build & Customize** ជ្រើសរើសទំព័រ **Agents**។
2. ចុច **+ Create agent** ដើម្បីបង្កើតភ្នាក់ងារថ្មី។ ក្នុងប្រអប់ តំឡើងភ្នាក់ងារ (**Agent Setup**):
    - បញ្ចូលឈ្មោះសម្រាប់ភ្នាក់ងារ ដូចជា `FlightAgent`។
    - បញ្ជាក់ថាម៉ូដែល `gpt-5-mini` ដែលអ្នកបានបញ្ចេញជាមុនគេត្រូវបានជ្រើសរើស
    - កំណត់ **សេចក្តីណែនាំ** តាមការបញ្ជា ដែលអ្នកចង់ឱ្យភ្នាក់ងារប្រតិបត្តិ។ នេះជាគំរូមួយ៖
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> សម្រាប់ការបញ្ជាផ្ទាល់លម្អិត អ្នកអាចពិនិត្យមើល [repository នេះ](https://github.com/ShivamGoyal03/RoamMind) សម្រាប់ព័ត៌មានបន្ថែម។
    
> ក៏ដូចជាអ្នកអាចបន្ថែម **មូលដ្ឋានចំណេះដឹង** និង **សកម្មភាព** ដើម្បីពង្រឹងសមត្ថភាពភ្នាក់ងារដើម្បីផ្តល់ព័ត៌មានបន្ថែម និងអនុវត្តភារកិច្ចអូតូម៉ាទិកផ្អែកលើសំណើររបស់អ្នកប្រើ។ សម្រាប់ហ្វឹកហាត់នេះ អ្នកអាចមិនចាំបាច់អនុវត្តជំហានទាំងនេះ។
    
![Agent Setup](../../../translated_images/km/agent-setup.9bbb8755bf5df672.webp)

3. ដើម្បីបង្កើតភ្នាក់ងារជា AI ដែលច្រើន ប្រើប៉ុស្តិ៍ **New Agent**។ ភ្នាក់ងារថ្មីនឹងត្រូវបង្ហាញនៅលើទំព័រ Agents។


## សាកល្បងភ្នាក់ងារ

បន្ទាប់ពីបង្កើតភ្នាក់ងារ អ្នកអាចសាកល្បងវាដើម្បីមើលថាតើវាឆ្លើយតបសំណួររបស់អ្នកប្រើយ៉ាងដូចម្តេចនៅក្នុង Microsoft Foundry portal playground។

1. នៅខាងលើបន្ទះ **Setup** សម្រាប់ភ្នាក់ងាររបស់អ្នក ជ្រើសរើស **Try in playground**។
2. នៅបន្ទះ **Playground** អ្នកអាចធ្វើអន្តរកម្មជាមួយភ្នាក់ងារដោយវាយសំណួរនៅក្នុងវីនដូចជាសន្ទនាផ្ទាល់។ ឧទាហរណ៍ អ្នកអាចសួរភ្នាក់ងារឲ្យស្វែងរកទំនិញហោះហើរពី Seattle ទៅ New York នៅថ្ងៃទី 28។

    > **ចំណាំ**: ភ្នាក់ងារអាចមិនផ្ដល់ចម្លើយត្រឹមត្រូវពេញលេញ ដោយសារតែទិន្នន័យពិតមិនត្រូវបានប្រើនៅក្នុងហ្វឹកហាត់នេះ។ គោលបំណងគឺសម្រាប់សាកល្បងសមត្ថភាពភ្នាក់ងារនៅក្នុងការយល់និងឆ្លើយតបសំណួររបស់អ្នកប្រើផ្អែកលើសេចក្តីណែនាំដែលបានផ្តល់។

    ![Agent Playground](../../../translated_images/km/agent-playground.dc146586de715010.webp)

3. បន្ទាប់ពីសាកល្បងភ្នាក់ងារ អ្នកអាចបន្ថែមការប្ដូរតាមបំណង ដូចជាការបន្ថែមគំនិត ទិន្នន័យបណ្តុះបណ្តាល និងសកម្មភាព ដើម្បីពង្រឹងសមត្ថភាពរបស់វា។

## ដោះស្រាយធនធាន

នៅពេលដែលអ្នកបានបញ្ចប់ការសាកល្បងភ្នាក់ងារ អ្នកអាចលុបវាដើម្បីជៀសវាងការចំណាយបន្ថែម។
1. បើក [Azure portal](https://portal.azure.com) ហើយមើលខ្លឹមសាររបស់ក្រុមធនធានដែលអ្នកបានបញ្ចេញធនធានមជ្ឈមណ្ឌលសម្រាប់ហ្វឹកហាត់នេះ។
2. នៅលើរបារឧបករណ៍ជ្រើសរើស **Delete resource group**។
3. បញ្ចូលឈ្មោះក្រុមធនធានហើយបញ្ជាក់ថាអ្នកចង់លុបវា។

## ធនធាន

- [ឯកសារពាក់ព័ន្ធ Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [ទំព័រ Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [ការចាប់ផ្តើមជាមួយ Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [មូលដ្ឋានគ្រឹះនៃភ្នាក់ងារ AI នៅលើ Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->