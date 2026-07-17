[![ភ្នាក់ងារបញ្ញាស مصنوعទុកចិត្តបាន](../../../translated_images/km/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ចុចលើរូបភាពខាងលើដើម្បីមើលវីដេអួរពីមេរៀននេះ)_

# ការបង្កើតភ្នាក់ងារបញ្ញាស مصنوعទុកចិត្តបាន

## ការណែនាំ

មេរៀននេះនឹងបញ្ចេញមាតិកា៖

- របៀបបង្កើត និងចេញដំណើរការភ្នាក់ងារបញ្ញាស مصنوعគ្មានគ្រោះថ្នាក់ និងមានប្រសិទ្ធភាព
- ការពិចារណាស៊ីគុណសន្តិសុខសំខាន់ៗនៅពេលអភិវឌ្ឍភ្នាក់ងារបញ្ញាស مصنوع
- របៀបរក្សាទុកទិន្នន័យ និងភាពឯកជនរបស់អ្នកប្រើនៅពេលអភិវឌ្ឍភ្នាក់ងារបញ្ញាស مصنوع

## គោលបំណងសិក្សា

បន្ទាប់ពីបញ្ចប់មេរៀននេះ អ្នកនឹងដឹងរបៀប៖

- សម្គាល់ និងកាត់បន្ថយហានិភ័យនៅពេលបង្កើតភ្នាក់ងារបញ្ញាស مصنوع
- អនុវត្តវិធានសន្តិសុខដើម្បីធានាថាទិន្នន័យ និងការចូលប្រើត្រូវបានគ្រប់គ្រងយ៉ាងត្រឹមត្រូវ
- បង្កើតភ្នាក់ងារបញ្ញាស مصنوع ដែលរក្សាភាពឯកជនទិន្នន័យ និងផ្ដល់បទពិសោធន៍ប្រើប្រាស់ដែលមានគុណភាព

## សុវត្ថិភាព

ឱ្យយើងមើលការបង្កើតកម្មវិធីភ្នាក់ងារដូច្នេះដែលមានសុវត្ថិភាពជាលើកដំបូង។ សុវត្ថិភាពមានន័យថា ភ្នាក់ងារបញ្ញាស مصنوعធ្វើការតាមការរចនាដែលបានកំណត់។ ជាអ្នកបង្កើតកម្មវិធីភាពភ្នាក់ងារ យើងមានវិធានការ និងឧបករណ៍ដើម្បីបង្កើនសុវត្ថិភាព៖

### ការបង្កើតស៊ុមសារ ប្រព័ន្ធសារយោង

បើអ្នកធ្លាប់បង្កើតកម្មវិធី AI ដោយប្រើម៉ូដែលភាសាធំ (LLMs) អ្នកនឹងដឹងពីសារៈសំខាន់នៃការរចនាសារ ប្រព័ន្ធឬសំណូមពរជា​រាងរឹងមាំ។ សំណូមពរទាំងនេះកំណត់ច្បាប់មេតា សេចក្តីណែនាំ និងវិនិច្ឆ័យផ្សេងៗដែលត្រូវអនុវត្តជាមួយអ្នកប្រើ និងទិន្នន័យ។

សម្រាប់ភ្នាក់ងារបញ្ញាស مصنوع សំណូមព្រប្រព័ន្ធនេះមានសារៈសំខាន់បន្ថែមទៀតព្រោះភ្នាក់ងារបញ្ញាស مصنوعត្រូវការសេចក្តីណែនាំពិសេសខ្ពស់ដើម្បីបញ្ចប់ភារកិច្ចដែលយើងបានរចនា។

ដើម្បីបង្កើតសំណូមព្រង្រប្រព័ន្ធដែលអាចពន្លឿនបាន យើងអាចប្រើស៊ុមសារប្រព័ន្ធសម្រាប់បង្កើតភ្នាក់ងារមួយឬច្រើននៅក្នុងកម្មវិធីរបស់យើង៖

![ការបង្កើតស៊ុមសារប្រព័ន្ធ](../../../translated_images/km/system-message-framework.3a97368c92d11d68.webp)

#### ជំហានទី ១៖ បង្កើតសារប្រព័ន្ធមេតា

សំណូមព្រមេតានឹងត្រូវបានប្រើដោយ LLM ដើម្បីបង្កើតសំណូមព្រប្រព័ន្ធសារសម្រាប់ភ្នាក់ងារដែលយើងបង្កើត។ យើងរចនាវាគឺជាគំរូដើម្បីអោយអាចបង្កើតភ្នាក់ងារជាច្រើនបានយ៉ាងមានប្រសិទ្ធភាពប្រសិនបើត្រូវការ។

នេះគឺជាឧទាហរណ៍នៃសារប្រព័ន្ធមេតាដែលយើងនឹងផ្តល់ឲ្យ LLM៖

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ជំហានទី ២៖ បង្កើតសំណូមព្រមូលដ្ឋាន

ជំហានបន្ទាប់គឺបង្កើតសំណូមព្រមូលដ្ឋានមួយសាមញ្ញដើម្បីពិពណ៌នាអ្នកភ្នាក់ងារ AI។ អ្នកគួរតែរួមបញ្ចូលតួនាទីរបស់ភ្នាក់ងារ ភារកិច្ចដែលភ្នាក់ងារនឹងបញ្ចប់ និងបំណួសទំនួលខុសត្រូវផ្សេងទៀតរបស់ភ្នាក់ងារ។

នេះគឺជាឧទាហរណ៍៖

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ជំហានទី ៣៖ ផ្តល់សារប្រព័ន្ធមូលដ្ឋានទៅ LLM

ឥឡូវនេះយើងអាចបង្កើនសមត្ថភាពសារប្រព័ន្ធនេះដោយផ្តល់សារប្រព័ន្ធមេតាជាសារប្រព័ន្ធ និងសារប្រព័ន្ធមូលដ្ឋានរបស់យើង។

នេះនឹងបង្កើតសារប្រព័ន្ធដែលបានរចនាយ៉ាងល្អប្រសើរជាងមុនសម្រាប់ណែនាំភ្នាក់ងារបញ្ញាស مصنوعរបស់យើង៖

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

#### ជំហានទី ៤៖ បន្តធ្វើតេស្ត និងកែលម្អ

តម្លៃនៃស៊ុមសារប្រព័ន្ធនេះគឺអាចធ្វើឲ្យមានការ​ពន្លឿនបង្កើតសារប្រព័ន្ធពីភ្នាក់ងារច្រើនបានយ៉ាងងាយស្រួល និងកែលម្អសារប្រព័ន្ធរបស់អ្នកជារៀងរាល់ពេល។ វាមានករណីតិចណាស់ដែលអ្នកនឹងមានសារប្រព័ន្ធដែលដំណើរការបានល្អនៅលើដំណើរការដំបូងសម្រាប់ករណីប្រើប្រាស់ពេញលេញ។ អាចធ្វើកែប្រែ​តែមួយថែម​ត្រួតពិនិត្យ និងកែលម្អតាមរយៈការផ្លាស់ប្តូរសារប្រព័ន្ធមូលដ្ឋាន និងរត់វាចូលប្រព័ន្ធនឹងអនុញ្ញាតឲ្យអ្នកប្រៀបធៀប និងវាយតម្លៃលទ្ធផល។

## ការយល់ដឹងពីគ្រោះថ្នាក់

ដើម្បីបង្កើតភ្នាក់ងារបញ្ញាស مصنوعដែលអាចទុកចិត្ត បាន វាជារឿងសំខាន់ក្នុងការយល់ដឹង និងកាត់បន្ថយហានិភ័យ និងគ្រោះថ្នាក់ដែលមានចំពោះភ្នាក់ងារបស់អ្នក។ ឱ្យមើលតែលក្ខខណ្ឌគ្រោះថ្នាក់ខ្លះៗចំពោះភ្នាក់ងារបញ្ញាស مصنوع និងរបៀបដែលអ្នកអាចគ្រោងការល្អប្រសើរនិងត្រៀមខ្លួន។

![ការយល់ដឹងពីគ្រោះថ្នាក់](../../../translated_images/km/understanding-threats.89edeada8a97fc0f.webp)

### ភារកិច្ច និងសេចក្តីណែនាំ

**ការពិពណ៌នា:** អ្នកបាញ់ប្រហារព្យាយាមផ្លាស់ប្តូរសេចក្តីណែនាំឬគោលបំណងរបស់ភ្នាក់ងារបញ្ញាស مصنوعតាមរយៈការបញ្ចូលសំណូមពរ ឬគ្រប់គ្រងការបញ្ចូលទិន្នន័យ។

**ការកាត់បន្ថយ**: ប្រតិបត្តិការត្រួតពិនិត្យ និងជម្រះការបញ្ចូលទិន្នន័យ ដើម្បីរកឃើញសំណូមពរដែលមានហានិភ័យមុនពេលទទួលបានកំណត់ពីភ្នាក់ងារ AI។ ពីព្រោះការវាយប្រហារទាំងនេះភាគច្រើនត្រូវការជំនាញទំនាក់ទំនងជាប់លាប់ជាមួយភ្នាក់ងារ ការបញ្ជាក់តម្លៃការបញ្ចូលជំនួសនៃការប្រាស្រ័យទំនាក់ទំនងគឺជាវិធីមួយទៀតដើម្បីការពារ​ការវាយប្រហារទាំងនេះ។

### ចូលប្រើប្រព័ន្ធសំខាន់ៗ

**ការពិពណ៌នា**: ប្រសិនបើភ្នាក់ងារបញ្ញាស مصنوع មានការចូលប្រើប្រព័ន្ធនិងសេវាកម្មដែលផ្ទុកទិន្នន័យសំខាន់ៗ អ្នកបាញ់ប្រហារអាចបំផ្លាញការទំនាក់ទំនងរវាងភ្នាក់ងារនិងសេវាកម្មទាំងនេះ។ នេះអាចជាការវាយប្រហារផ្ទាល់ ឬក៏ការប្រើប្រាស់ជឿនលឿនដើម្បីទទួលបានព័ត៌មានអំពីប្រព័ន្ធទាំងនេះតាមរយៈភ្នាក់ងារ។

**ការកាត់បន្ថយ**: ភ្នាក់ងារបញ្ញាស مصنوعគួរតែមានសិទ្ធិចូលប្រព័ន្ធតាមតម្រូវការតែប៉ុណ្ណោះ ដើម្បីការពារវាយប្រហារទាំងនេះ។ ការទំនាក់ទំនងរវាងភ្នាក់ងារនិងប្រព័ន្ធគួរត្រូវបានធ្វើឲ្យមានសុវត្ថិភាព។ ការអនុវត្តការផ្ទៀងផ្ទាត់ និងការគ្រប់គ្រងការចូលប្រើគឺជាវិធានការមួយទៀតដើម្បីការពារព័ត៌មាននេះ។

### ការបង្កលើសកំណត់ធនធាន និងសេវាកម្ម

**ការពិពណ៌នា:** ភ្នាក់ងារបញ្ញាស مصنوعអាចចូលប្រើឧបករណ៍ និងសេវាកម្មផ្សេងៗដើម្បីបញ្ចប់ភារកិច្ច។ អ្នកបាញ់ប្រហារអាចប្រើសមត្ថភាពនេះវាយប្រហារសេវាកម្មទាំងនេះដោយផ្ញើសំណើច្រើនតាមរយៈភ្នាក់ងារបញ្ញាស مصنوع ដែលអាចបណ្តាលឲ្យមានបរាជ័យប្រព័ន្ធ ឬការចំណាយខ្ពស់។

**ការកាត់បន្ថយ:** អនុវត្តន៍គោលនយោបាយដើម្បីដាក់កំណត់ចំនួនសំណើដែលភ្នាក់ងារបញ្ញាស مصنوعអាចធ្វើទៅលើសេវាកម្មមួយ។ ការកំណត់ជួរឆលើការសន្ទនា និងចំនួនសំណើទៅភ្នាក់ងាររបស់អ្នកគឺជាវិធីមួយទៀតដើម្បីការពារការវាយប្រហារទាំងនេះ។

### ការបំពុលមូលដ្ឋានចំណេះដឹង

**ការពិពណ៌នា:** ប្រភេទវិជ្ជមាននេះមិនត្រូវគោលដៅទៅលើភ្នាក់ងារបញ្ញាស مصنوعដោយផ្ទាល់ទេ ប៉ុន្តែគោលដៅទៅលើមូលដ្ឋានចំណេះដឹង និងសេវាកម្មផ្សេងទៀតដែលភ្នាក់ងារបញ្ញាស مصنوعនឹងប្រើ។ នេះអាចជាការបំពុលទិន្នន័យ ឬព័ត៌មានដែលភ្នាក់ងារនឹងប្រើក្នុងការបំពេញភារកិច្ច បណ្តាលឲ្យមានចម្លើយលើសសំខាន់ ឬដែលមិនចង់បានចំពោះអ្នកប្រើ។

**ការកាត់បន្ថយ:** ប្រារព្ធការត្រួតពិនិត្យទិន្នន័យជាប្រចាំដែលភ្នាក់ងារនឹងប្រើនៅក្នុងវគ្គធ្វើការ។ វិញ្ញាប់ថាការចូលប្រើទិន្នន័យនេះមានសុវត្ថិភាព និងត្រូវបានផ្លាស់ប្តូរតែដោយមនុស្សដែលទុកចិត្តបាន ដើម្បីជៀសវាងការវាយប្រហារប្រភេទនេះ។

### កំហុសរាត់លើគ្នា

**ការពិពណ៌នា:** ភ្នាក់ងារបញ្ញាស مصنوعចូលប្រើឧបករណ៍ និងសេវាកម្មផ្សេងៗដើម្បីបញ្ចប់ភារកិច្ច។ កំហុសដែលបង្ករដោយអ្នកវាយប្រហារអាចបណ្តាលឲ្យមានបរាជ័យប្រព័ន្ធផ្សេងទៀតដែលភ្នាក់ងារតភ្ជាប់ជាមួយនោះ ធ្វើឲ្យការវាយប្រហារផ្សារភ្ជាប់ទូលំទូលាយ និងពិបាកដោះស្រាយ។

**ការកាត់បន្ថយ**: វិធីមួយដើម្បីជៀសវាងនេះគឺឲ្យភ្នាក់ងារធ្វើការនៅក្នុងបរិយាកាសកំណត់ ដូចជាការបំពេញភារកិច្ចក្នុងកុងតឺន័ Docker ដើម្បីការពារការវាយប្រហារផ្ទាល់ទៅប្រព័ន្ធ។ ការបង្កើតប្រព័ន្ធផ្ទុកជំនួស និងកន្សោមព្យាយាមឡើងវិញនៅពេលប្រព័ន្ធមួយឆ្លើយតបមានកំហុស គឺជាវិធីមួយសម្រាប់ការពារបរាជ័យប្រព័ន្ធធំជាងនេះ។

## មនុស្សក្នុងខ្សែការងារ

វិធីផ្សេងទៀតដែលមានប្រសិទ្ធភាពក្នុងការបង្កើតប្រព័ន្ធភ្នាក់ងារបញ្ញាស مصنوعដែលទុកចិត្តបានគឺការប្រើប្រាស់មនុស្សក្នុងខ្សែការងារ។ វាបង្កើតផ្លូរដែលអ្នកប្រើអាចផ្ដល់មតិយោបល់ទៅភ្នាក់ងារពេលនោះ។ អ្នកប្រើជាភ្នាក់ងារនៅក្នុងប្រព័ន្ធភ្នាក់ងារជាច្រើន ហើយផ្ដល់ការអនុម័ត ឬបញ្ចប់ដំណើរការដំណើរការ។

![មនុស្សក្នុងខ្សែការងារ](../../../translated_images/km/human-in-the-loop.5f0068a678f62f4f.webp)

នេះគឺជាឧទាហរណ៍កូដប្រើប្រាស់ Microsoft Agent Framework ដើម្បីបង្ហាញរបៀបអនុវត្តគំនិតនេះ៖

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# បង្កើតអ្នកផ្គត់ផ្គង់ដែលមានការអនុម័តដោយមនុស្សរួមចំណែក
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# បង្កើតភ្នាក់ងារជាមួយជំហានអនុម័តដោយមនុស្ស
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# អ្នកប្រើអាចពិនិត្យនិងអនុម័តចម្លើយបាន
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 결론

ការបង្កើតភ្នាក់ងារបញ្ញាស مصنوعដែលទុកចិត្តបានត្រូវការរចនាយ៉ាងប្រុងប្រយ័ត្ន ការអនុវត្តវិធានសន្តិសុខរឹងមាំ និងការបន្តធ្វើតេស្តជាបន្តបន្ទាប់។ ដោយប្រើប្រាស់ប្រព័ន្ធមេតាសំណូមព្រដែលមានរចនាសង្ខេប ការយល់ដឹងនៃគ្រោះថ្នាក់ដែលអាចកើតមាន និងអនុវត្តវិធានការកាត់បន្ថយ អ្នកអភិវឌ្ឍអាចបង្កើតភ្នាក់ងារបញ្ញាស مصنوعដែលមានសុវត្ថិភាព និងប្រសិទ្ធភាព។ បន្ថែមពីនេះ ការរួមបញ្ចូលអ្នកមនុស្សក្នុងខ្សែការងារធានាថាភ្នាក់ងារមានការត្រូវគ្នាជាមួយតម្រូវការអ្នកប្រើ ខណៈពេលកាត់បន្ថយហានិភ័យ។ ដូច្នេះ ពេលបញ្ញាស مصنوعបន្តរលូតលាស់ ការរក្សារមុខងារវិភាគមុខ និងប្រយ័ត្នចំពោះសន្តិសុខ ភាពឯកជន និងក្រមសីលធម៌ នឹងធ្វើឲ្យមានការជឿជាក់ និងអាចទុកចិត្តបានក្នុងប្រព័ន្ធដែលបើកចេញដោយបញ្ញាស مصنوع។

## កូដគំរូ

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): ការបង្ហាញជាដំណាក់កាលនៃប្រព័ន្ធសារមេតាសំណូមព្រប្រព័ន្ធ
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): ការអនុម័តមុនសកម្មភាព ខ្នាតហានិភ័យ និងការចុះបញ្ជីតួនាទីសម្រាប់ភ្នាក់ងារដែលអាចទុកចិត្តបាន

### មានសំណួរបន្ថែមអំពីការបង្កើតភ្នាក់ងារបញ្ញាស مصنوعទុកចិត្តបានទៀតទេ?

ចូលរួមជាមួយ [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ដើម្បីជួបជាមួយអ្នករៀនផ្សេងទៀត ចូលរួមម៉ោងការិយាល័យ និងទទួលការឆ្លើយសំណួរអំពីភ្នាក់ងារបញ្ញាស مصنوعរបស់អ្នក។

## ធនធានបន្ថែម

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ទិដ្ឋភាពទូលំទូលាយនៃ AI ទំនួលខុសត្រូវ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ការវាយតម្លៃម៉ូដែល AI ការបង្កើត និងកម្មវិធី AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">សារប្រព័ន្ធសុវត្ថិភាព</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">គំរូការវាយតម្លៃហានិភ័យ</a>

## មេរៀនមុន

[Agentic RAG](../05-agentic-rag/README.md)

## មេរៀនបន្ទាប់

[រចនាបទគំរូផែនការ](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->