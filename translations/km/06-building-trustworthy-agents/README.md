[![គោលដៅ AI Agents ដែលគួរឱ្យទុកចិត្ត](../../../translated_images/km/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ចុចរូបភាពខាងលើដើម្បីមើលវីដេអូរបស់មេរៀននេះ)_

# កសាងគោលដៅ AI Agents ដែលគួរឱ្យទុកចិត្ត

## ការណែនាំ

មេរៀននេះនឹងផ្តោតទៅលើ៖

- របៀបកសាង និងដំឡើង AI Agents អោយមានសុវត្ថិភាព និងមានប្រសិទ្ធភាព
- គោលការណ៍សុវត្ថិភាពសំខាន់ៗនៅពេលបង្កើត AI Agents។
- របៀបថែរក្សาข้อมูล និងភាពឯកជនរបស់អ្នកប្រើ នៅពេលបង្កើត AI Agents។

## គោលបំណងការសិក្សា

បន្ទាប់ពីបញ្ចប់មេរៀននេះ អ្នកនឹងដឹងថា៖

- រកឃើញ និងកាត់បន្ថយហានិភ័យនៅពេលបង្កើត AI Agents។
- អនុវត្តវិធានសុវត្ថិភាពដើម្បីធានាថា​ទិន្នន័យ និងការចូលប្រើ​ត្រូវបាន​គ្រប់គ្រង​យ៉ាងត្រឹមត្រូវ។
- បង្កើត AI Agents ដែលថែរក្សា​ភាពឯកជន​ទិន្នន័យ និង​ផ្តល់បទពិសោធន៍​ប្រើប្រាស់មានគុណភាព។

## សុវត្ថិភាព

មុនដំបូងយើងត្រូវមើលទៅកាន់ការបង្កើតកម្មវិធី​អាជីវកម្ម agentic ដែលមានសុវត្ថិភាព។ សុវត្ថិភាពមានន័យថា AI agent កំពុងអនុវត្តតាមការរចនាដែលបានកំណត់។ ជាអ្នកបង្កើតកម្មវិធី agentic យើងមានវិធីសាស្ត្រ និងឧបករណ៍សម្រាប់បង្កើនសុវត្ថិភាពបំផុត៖

### ការបង្កើតស៊ុមសាររបស់ប្រព័ន្ធ

ប្រសិនបើអ្នកធ្លាប់បានបង្កើតកម្មវិធី AI ដែលប្រើម៉ូដែលភាសាធំ (LLMs) អ្នកនឹងដឹងពីសារៈសំខាន់នៃការរចនាស៊ុមសារប្រព័ន្ធ ឬសារប្រព័ន្ធរឹងមាំ។ សឹទ្ធនិយមទាំងនេះកំណត់ច្បាប់​សម្រាប់ពិធីការ និងអនុស្សារណៈ​របៀបដែល LLM នឹងអន្តរកម្មជាមួយអ្នកប្រើ និងទិន្នន័យ។

សម្រាប់ AI Agents សារប្រព័ន្ធនេះមានសារៈសំខាន់ជាងមុន ព្រោះ AI Agents នឹងត្រូវការណែនាំជាក់លាក់ខ្ពស់ដើម្បីបញ្ចប់ភារកិច្ចដែលយើងបានរចនាឲ្យពួកវា។

ដើម្បីបង្កើតស៊ុមសារប្រព័ន្ធដែលអាចបង្កើត​បានច្រើន យើងអាចប្រើស៊ុមសារប្រព័ន្ធជារាងស៊ីស្តាំមួយសម្រាប់កសាងមួយឬច្រើន​អេហ្សិនក្នុងកម្មវិធីរបស់យើង៖

![Building a System Message Framework](../../../translated_images/km/system-message-framework.3a97368c92d11d68.webp)

#### ជំហានទី 1៖ បង្កើតសារប្រព័ន្ធ Meta

សារប្រព័ន្ធ meta នឹងត្រូវបានប្រើដោយ LLM ដើម្បីបង្កើតសារប្រព័ន្ធសម្រាប់អេហ្សិនដែលយើងបង្កើត។ យើងរចនាវាជាគំរូ ដើម្បីយើងអាចបង្កើតអេហ្សិនជាមួយច្រើនបានយ៉ាងមានប្រសិទ្ធភាពប្រសិនបើត្រូវការ។

នេះគឺជាគំរូនៃសារប្រព័ន្ធ meta ដែលយើងនឹងផ្តល់ដល់ LLM៖

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ជំហានទី 2៖ បង្កើតសារចាប់ផ្តើមមូលដ្ឋាន

ជំហានបន្ទាប់គឺបង្កើតសារចាប់ផ្តើមមូលដ្ឋានដើម្បីពិពណ៌នាអំពី AI Agent។ អ្នកគួរតែបញ្ចូលតួនាទីរបស់អេហ្សិន ភារកិច្ចដែលអេហ្សិននឹងបញ្ចប់ ហើយនឹងមានទំនួលខុសត្រូវផ្សេងៗទៀត។

នេះគឺជាគំរូ៖

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ជំហានទី 3៖ ផ្តល់សារប្រព័ន្ធមូលដ្ឋានទៅ LLM

ឥឡូវនេះយើងអាចបង្កើនសមត្ថភាពសារប្រព័ន្ធនេះដោយផ្តល់សារប្រព័ន្ធ meta ជាសារប្រព័ន្ធ និងសារប្រព័ន្ធមូលដ្ឋានរបស់យើង។

នេះនឹងបង្កើតសារប្រព័ន្ធដែលរចនាឡើងប្រសើរជាងមុនសម្រាប់ណែនាំ AI agents របស់យើង៖

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### ជំហានទី 4៖ ធ្វើមីត និងបង្កើតកែលម្អ

តម្លៃនៃស៊ុមសារប្រព័ន្ធនេះគឺឱ្យអាចបង្កើតសារប្រព័ន្ធពីអេហ្សិនជាច្រើនបានងាយស្រួល និងធ្វើការកែលម្អសារប្រព័ន្ធរបស់អ្នកជាដំណើរពេលវេលា។ វាក្លាយជារឿងក្រឡាប់ចិត្តក្នុងការរកឃើញសារប្រព័ន្ធដែលដំណើរការបានល្អជាលើកដំបូងសម្រាប់ករណីប្រើប្រាស់របស់អ្នក។ អាចធ្វើបម្លែងតិចតួច និងកែលម្អដោយប្ដូរសារប្រព័ន្ធមូលដ្ឋាន ហើយដំណើរការវាជាលក្ខណៈប្រព័ន្ធ អោយអ្នកអាចប្រៀបធៀបនិងវាយតម្លៃលទ្ធផលបាន។

## ការយល់ដឹងពីគំរាមកំហែង

ដើម្បីកសាង AI agents ដែលគួរឱ្យទុកចិត្ត វាសំខាន់ក្នុងការយល់ដឹង និងកាត់បន្ថយហានិភ័យ និងគំរាមកំហែងលើ AI agent របស់អ្នក។ យើងចង់មើលតែខ្លះនៃគំរាមកំហែងផ្សេងៗលើ AI agents និងរបៀបដែលអ្នកអាចរៀបចំ និងត្រៀមខ្លួនបានល្អជាងមុន។

![Understanding Threats](../../../translated_images/km/understanding-threats.89edeada8a97fc0f.webp)

### ភារកិច្ច និងការណែនាំ

**ពិពណ៌នា:** អ្នកបំផ្លាញព្យាយាមបំលែងការណែនាំ ឬគោលដៅរបស់ AI agent តាមរយៈការផ្តល់សារឬបញ្ជូលព័ត៌មានដែលចង់លេងសម្រុក។

**ការកាត់បន្ថយ:** អនុវត្តការត្រួតពិនិត្យសុវត្ថិភាព និងការពិនិត្យ​ជញ្ជាំង​សម្រាប់ការបញ្ចូលទិន្នន័យ ដើម្បីរកសារដែលគួរត្រូវបានចូលរួមនូវការគំរាមកំហែងមុនពេលវាដំណើរការដោយ AI Agent។ ដោយសារការវាយប្រហារនេះជាទូទៅត្រូវការអន្តរកម្មញឹកញាប់ជាមួយអេហ្សិន ការកំណត់ចំនួនជុំក្នុងការសន្ទនាជាគ្រោងវិធានដើម្បីបង្ការការវាយប្រហារថ្មីៗនេះ។

### ការចូលប្រើប្រព័ន្ធសំខាន់ៗ

**ពិពណ៌នា:** ប្រសិនបើ AI agent មានការចូលប្រើប្រព័ន្ធ និងសេវាកម្មដែលផ្ទុកព័ត៌មានដែលមានភាពឯកជន ខូចខាតអាចធ្វើអោយការទំនាក់ទំនងរវាងអេហ្សិន និងសេវាកម្មទាំងនេះខូចខាត។ វាអាចជាការវាយប្រហារផ្ទាល់ ឬជាការព្យាយាមឆ្លងដំណឹងអំពីប្រព័ន្ធទាំងនេះតាមរយៈអេហ្សិន។

**ការកាត់បន្ថយ:** AI agents គួរតែមានការចូលប្រើប្រព័ន្ធតែតាមជាក់ស្តែងដែលចាំបាច់ប៉ុណ្ណោះ ដើម្បីការពារការវាយប្រហារដូចនេះ។ ការទំនាក់ទំនងរវាងអេហ្សិន និងប្រព័ន្ធគួរតែមានសុវត្ថិភាពផងដែរ។ ការអនុវត្តតម្រង់សញ្ញាប័ត្រ និងការគ្រប់គ្រងការចូលប្រើគឺជាវិធីសាស្រ្តមួយទៀតក្នុងការពារព័ត៌មាននេះ។

### បញ្ហាការប្រើប្រាស់ធនធាន និងសេវាកម្ម​ជា​ជួរ

**ពិពណ៌នា:** AI agents អាចចូលប្រើឧបករណ៍ និងសេវាកម្មផ្សេងៗដើម្បីបញ្ចប់ភារកិច្ច។ អ្នកវាយប្រហារអាចប្រើសម្ថតភាពនេះ ដើម្បីផ្ញើសំណើជាច្រើនតាមរយៈ AI Agent ដែលអាចបណ្តាលឲ្យប្រព័ន្ធខូចខាត ឬមានការចំណាយខ្ពស់។

**ការកាត់បន្ថយ:** អនុវត្តគោលនយោបាយដើម្បីកំណត់ចំនួនសំណើដែលAI agent អាចផ្ញើទៅសេវាកម្ម។ ការកំណត់ចំនួនជុំក្នុងសន្ទនា និងសំណើទៅ AI agent ផងដែរជាវិធីបង្ការការវាយប្រហារទាំងនេះ។

### ការបំផ្លាញមូលដ្ឋានចំណេះដឹង

**ពិពណ៌នា:** ការវាយប្រហារប្រភេទនេះមិនរក្សាទុកបញ្ចេញលើ AI agent ដោយផ្ទាល់ឡើយ ប៉ុន្តែវាមានគោលបំណងលើមូលដ្ឋានចំណេះដឹង និងសេវាកម្មផ្សេងទៀតដែល AI agent នឹងប្រើ។ វាអាចជាការបំផ្លាញទិន្នន័យ ឬព័ត៌មានដែល AI agent នឹងប្រើក្នុងការបញ្ចប់ភារកិច្ច ដែលអាចបណ្ដាលឲ្យមានចម្លើយមិនល្អ ឬមានចំនុច​លម្អៀងចេញទៅអ្នកប្រើ។

**ការកាត់បន្ថយ:** អនុវត្តការត្រួតពិនិត្យទិន្នន័យជាប្រចាំដែល AI agent នឹងប្រើក្នុងចរន្តការងាររបស់វា។ ដើម្បីជៀសវាងការវាយប្រហារ ប្រព័ន្ធត្រូវបញ្ចេញការចូលប្រើទិន្នន័យសុវត្ថិ និងត្រូវមានក្រុមមនុស្សដែលទទួលខុសត្រូវទុកចិត្តបំផុត។

### កំហុសស្រទាប់រាយ

**ពិពណ៌នា:** AI agents ចូលប្រើឧបករណ៍ និងសេវាកម្មជាច្រើនដើម្បីបញ្ចប់ភារកិច្ច។ កំហុសដែលបណ្តាលមកពីអ្នកវាយប្រហារ អាចបណ្តាលឲ្យប្រព័ន្ធផ្សេងៗដែល AI agent មានការតភ្ជាប់ខូចខាត ដូច្នេះការវាយប្រហារគឺធំទូលាយ និងពិបាកដោះស្រាយ។

**ការកាត់បន្ថយ:** វិធីមួយក្នុងការជៀសវាងគឺឱ្យ AI Agent ប្រតិបត្តិការ​ក្នុងបរិយាកាសបញ្ចប់ (sandbox-like environment) ដូចជាការបំពេញភារកិច្ចនៅក្នុងកុងតឺន័រ Docker ដើម្បីការពារការវាយប្រហារដោយផ្ទាល់លើប្រព័ន្ធ។ ការបង្កើតយន្តការជំនួស និងលូជាប្រឡងបន្ថែមនៅពេលប្រព័ន្ធខ្លះឆ្លើយតបទៅកំហុសគឺវិធីសាស្រ្តមួយទៀតដែលជួយបង្ការការខូចខាតធំដាច់។

## មនុស្សនៅក្នុងរង្វង់ (Human-in-the-Loop)

វិធីផ្សេងទៀតដូចជាដំណើរការដែលមានមនុស្សនៅក្នុងរង្វង់ជួយបង្កើតប្រព័ន្ធ AI Agent ដែលគួរឱ្យទុកចិត្ត។ វាបង្កើតដំណើរការដែលអ្នកប្រើអាចផ្តល់មតិយោបល់ទៅអេហ្សិននៅពេលវាត្រូវដំណើរការ។ អ្នកប្រើប្រាស់ជា​មូលដ្ឋានដូចជា​អេហ្សិនម្នាក់នៅក្នុងប្រព័ន្ធ​ច្រើន​អេហ្សិន ដោយផ្តល់ការអនុម័ត ឬបញ្ឈប់ដំណើរការនោះ។

![Human in The Loop](../../../translated_images/km/human-in-the-loop.5f0068a678f62f4f.webp)

នៅទីនេះគឺជា snippet កូដប្រើ Microsoft Agent Framework បង្ហាញពីរបៀបអនុវត្តគំនិតនេះ៖

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# បង្កើតអ្នកផ្ដល់សេវាជាមួយការអនុម័តដោយមនុស្សក្នុងច្រក
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# បង្កើតភ្នាក់ងារជាមួយជំហានអនុម័តដោយមនុស្ស
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# អ្នកប្រើអាចពិចារណា និងអនុម័តចម្លើយបាន
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## សេចក្តីសន្និដ្ឋាន

ការកសាង AI agents ដែលគួរឱ្យទុកចិត្តត្រូវការការរចនាដោយប្រុងប្រយ័ត្ន វិធានសុវត្ថិភាពរឹងមាំ និងការធ្វើមីតជាបន្តបន្ទាប់។ តាមរយៈការអនុវត្តប្រព័ន្ធ meta prompting រចនាសម្ព័ន្ធ ការយល់ដឹងពីគំរាមកំហែង និងការអនុវត្តយុទ្ធសាស្រ្តកាត់បន្ថយ អ្នកអwickរេនអាចបង្កើត AI agents ដែលមានសុវត្ថិភាព និងមានប្រសិទ្ធភាព។ ព្រមទាំងបញ្ចូលវិធីសាស្ត្រHuman-in-the-loop ផងដែរ ដើម្បីធានាថា AI agents នៅតែសម្របសម្រួលជាមួយតម្រូវការអ្នកប្រើ ខណៈកាត់បន្ថយហានិភ័យ។ នៅពេល AI កំពុងអភិវឌ្ឍ ការរក្សាទុក្ខធ្វើការផ្គត់ផ្គង់គោលការណ៍លើសុវត្ថិភាព ភាពឯកជន និងកត្តាគ្រប់គ្រងវិជ្ជាជីវៈ នឹងជាកត្តាសំខាន់ក្នុងការបង្កើតទំនុកចិត្ត និងភាពទៀងទាត់នៅក្នុងប្រព័ន្ធដែលគ្រប់គ្រងដោយ AI។

## លំហាត់កូដ

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): ការបង្ហាញជាជំហាននៃប្រព័ន្ធសារប្រព័ន្ធ meta-prompt។
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): ការអនុម័តមុនសកម្មភាព ការតម្រៀបហានិភ័យ និងកំណត់ហេតុ audit សម្រាប់អេហ្សិនដែលគួរឱ្យទុកចិត្ត។

### មានសំណួរបន្ថែមអំពីការកសាង AI Agents ដែលគួរឱ្យទុកចិត្តទេ?

ចូលរួម [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ដើម្បីជួបជាមួយអ្នករៀនផ្សេងទៀត ចូលរួមវគ្គការិយាល័យ និងទទួលបានចម្លើយសំណួរអំពី AI Agents របស់អ្នក។

## ឯកសារបន្ថែម

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">មើលទិដ្ឋភាពទូទៅអំពី AI ទទួលខុសត្រូវ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ការវាយតម្លៃម៉ូដែល AI កំណើត និងកម្មវិធី AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">សារប្រព័ន្ធសុវត្ថិភាព</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ប្លង់វាយតម្លៃហានិភ័យ</a>

## មេរៀនមុន

[Agentic RAG](../05-agentic-rag/README.md)

## មេរៀនបន្ទាប់

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->