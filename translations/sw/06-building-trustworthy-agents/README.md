[![Wakala wa AI wa Kuaminika](../../../translated_images/sw/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Bonyeza picha hapo juu kuona video ya somo hili)_

# Kuunda Wakala wa AI wa Kuaminika

## Utangulizi

Somo hili litajumuisha:

- Jinsi ya kuunda na kusambaza Wakala wa AI salama na wenye ufanisi
- Mambo muhimu ya usalama wakati wa kuendeleza Wakala wa AI.
- Jinsi ya kudumisha faragha ya data na mtumiaji wakati wa kuendeleza Wakala wa AI.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utajua jinsi ya:

- Kutambua na kupunguza hatari wakati wa kuunda Wakala wa AI.
- Kutekeleza hatua za usalama kuhakikisha kwamba data na upatikanaji vinadhibitiwa ipasavyo.
- Kuunda Wakala wa AI wanaodumisha faragha ya data na kutoa uzoefu bora kwa mtumiaji.

## Usalama

Kwanza naangalie jinsi ya kuunda programu za wakala salama. Usalama unamaanisha kwamba wakala wa AI anafanya kazi kama ilivyopangwa. Kama wajenzi wa programu za wakala, tuna mbinu na zana za kuongeza usalama:

### Kuunda Mfumo wa Ujumbe wa Mfumo

Ikiwa umewahi kuunda programu ya AI ukitumia Miundo Mikubwa ya Lugha (LLMs), unajua umuhimu wa kubuni mfumo thabiti wa ombi la mfumo au ujumbe wa mfumo. Maombi haya huwekeza sheria kuu, maelekezo, na miongozo ya jinsi LLM itakavyoshirikiana na mtumiaji na data.

Kwa Wakala wa AI, ombi la mfumo ni muhimu zaidi kwani Wakala wa AI watahitaji maelekezo maalum sana kukamilisha kazi tulizozitengeneza zao.

Ili kuunda maombi ya mfumo yanayoweza kupanuka, tunaweza kutumia mfumo wa ujumbe wa mfumo kuunda wakala mmoja au zaidi katika programu yetu:

![Kuunda Mfumo wa Ujumbe wa Mfumo](../../../translated_images/sw/system-message-framework.3a97368c92d11d68.webp)

#### Hatua ya 1: Unda Ujumbe wa Mfumo wa Meta

Ombi la meta litafanya kazi na LLM kuzalisha maombi ya mfumo kwa wakala tunaounda. Tunaunda kama kiolezo ili tuweze kuunda wakala wengi kwa ufanisi ikiwa itahitajika.

Hapa kuna mfano wa ujumbe wa mfumo wa meta tungeupa LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Hatua ya 2: Unda Ombi la Msingi

Hatua inayofuata ni kuunda ombi la msingi kuelezea Wakala wa AI. Unapaswa kujumuisha jukumu la wakala, kazi ambazo wakala atakamilisha, na majukumu mengine yoyote ya wakala.

Hapa kuna mfano:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Hatua ya 3: Toa Ujumbe wa Mfumo wa Msingi kwa LLM

Sasa tunaweza kuboresha ujumbe huu wa mfumo kwa kutoa ujumbe wa mfumo wa meta kama ujumbe wa mfumo pamoja na ujumbe wetu wa msingi wa mfumo.

Hii itatengeneza ujumbe wa mfumo ulio bora zaidi kwa kuongoza wakala wetu wa AI:

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

#### Hatua ya 4: Rudia na Boresha

Thamani ya mfumo huu wa ujumbe wa mfumo ni uwezo wa kupanua kuunda ujumbe wa mfumo kutoka kwa wakala wengi kwa urahisi pamoja na kuboresha ujumbe wako wa mfumo kadri wakati unavyopita. Ni nadra kuwa na ujumbe wa mfumo unaofanya kazi mara ya kwanza kwa matumizi yako kamili. Kuwa na uwezo wa kufanya marekebisho madogo na maboresho kwa kubadilisha ujumbe wa msingi wa mfumo na kuupitia mfumo kutakuwezesha kulinganisha na kutathmini matokeo.

## Kuelewa Vitisho

Ili kuunda wakala wa AI wa kuaminika, ni muhimu kuelewa na kupunguza hatari na vitisho kwa wakala wako wa AI. Tuangalie baadhi tu ya vitisho tofauti kwa wakala wa AI na jinsi unaweza kupanga na kujiandaa vyema kwa ajili yao.

![Kuelewa Vitisho](../../../translated_images/sw/understanding-threats.89edeada8a97fc0f.webp)

### Kazi na Maelekezo

**Maelezo:** Wadukuzi wanajaribu kubadilisha maelekezo au malengo ya wakala wa AI kupitia ombi au kudanganya maingizo.

**Kupunguza**: Fanya ukaguzi wa uthibitisho na vichujio vya maingizo kugundua maombi yenye hatari kabla hayajapokelewa na Wakala wa AI. Kwa kuwa mashambulizi haya kawaida yanahitaji mwingiliano wa mara kwa mara na Wakala, kupunguza idadi ya zamu katika mazungumzo ni njia nyingine ya kuzuia aina hizi za mashambulizi.

### Upatikanaji wa Mifumo Muhimu

**Maelezo**: Ikiwa wakala wa AI ana upatikanaji wa mifumo na huduma zinazohifadhi data nyeti, wadukuzi wanaweza kuhujumu mawasiliano kati ya wakala na huduma hizi. Hii inaweza kuwa mashambulizi ya moja kwa moja au jaribio la kupata habari kuhusu mifumo hii kupitia wakala.

**Kupunguza**: Wakala wa AI wanapaswa kupata upatikanaji wa mifumo kwa msingi wa hitaji tu ili kuzuia aina hizi za mashambulizi. Mawasiliano kati ya wakala na mfumo nayo yanapaswa kuwa salama. Kutekeleza uthibitishaji na udhibiti wa upatikanaji ni njia nyingine ya kulinda taarifa hii.

### Msongamano wa Rasilimali na Huduma

**Maelezo:** Wakala wa AI wanaweza kupata zana na huduma mbalimbali kukamilisha kazi. Wadukuzi wanaweza kutumia uwezo huu kushambulia huduma hizi kwa kutuma ombi nyingi kwa kupitia Wakala wa AI, jambo linaloweza kusababisha mifumo kufeli au gharama kubwa.

**Kupunguza:** Tekeleza sera za kupunguza idadi ya ombi ambalo wakala wa AI anaweza kutuma kwa huduma. Kupunguza idadi ya zamu za mazungumzo na maombi kwa wakala wako wa AI ni njia nyingine ya kuzuia aina hizi za mashambulizi.

### Uchafuzi wa Msingi wa Maarifa

**Maelezo:** Aina hii ya shambulio hairuki moja kwa moja wakala wa AI bali inalenga msingi wa maarifa na huduma nyingine ambazo wakala wa AI atatumia. Hii inaweza kuhusisha kuhujumu data au habari ambazo wakala wa AI atatumia kukamilisha kazi, na kusababisha majibu yenye upendeleo au yasiyokusudiwa kwa mtumiaji.

**Kupunguza:** Fanya uhakiki mara kwa mara wa data ambayo wakala wa AI atatumia katika kazi zake. Hakikisha kwamba upatikanaji wa data hii ni salama na hubadilishwa tu na watu wanaoaminika ili kuepuka aina hii ya shambulio.

### Makosa Yanayoendelea

**Maelezo:** Wakala wa AI hufikia zana na huduma mbalimbali kukamilisha kazi. Makosa yanayosababishwa na wadukuzi yanaweza kusababisha mifumo mingine inayounganishwa na wakala kufeli, na kufanya shambulio kuwa pana zaidi na vigumu kutatua.

**Kupunguza**: Njia moja ya kuepuka hii ni kuhakikisha wakala wa AI anafanya kazi katika mazingira yaliyopunguzwa, kama kufanya kazi katika kontena la Docker, ili kuzuia mashambulizi ya moja kwa moja kwenye mfumo. Kuunda njia za kurejea nyuma na mantiki ya kujaribu tena wakati mifumo fulani inapojibu kwa kosa ni njia nyingine ya kuzuia kushindwa kwa mifumo mikubwa.

## Mtu Katikati ya Mzunguko

Njia nyingine yenye ufanisi ya kuunda mifumo ya Wakala wa AI wa kuaminika ni kutumia Mtu-katikati ya mzunguko. Hii huunda mtiririko ambapo watumiaji wanaweza kutoa maoni kwa Wakala wakati wa utekelezaji. Watumiaji kwa kiasi fulani hufanya kazi kama wakala katika mfumo wa wakala wengi na kwa kutoa idhini au kusitisha mchakato unaoendelea.

![Mtu katika Mzunguko](../../../translated_images/sw/human-in-the-loop.5f0068a678f62f4f.webp)

Hapa kuna sehemu ya msimbo ikitumia Mfumo wa Wakala wa Microsoft kuonyesha jinsi dhana hii inavyotekelezwa:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Unda mtoa huduma pamoja na idhini ya mtu katika mchakato
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Unda wakala pamoja na hatua ya idhini ya mtu
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Mtumiaji anaweza kupitia na kuidhinisha jibu
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Hitimisho

Kuunda wakala wa AI wa kuaminika kunahitaji muundo makini, hatua thabiti za usalama, na kurudia mara kwa mara. Kwa kutekeleza mifumo ya muundo wa ombi la meta, kuelewa vitisho vinavyoweza kutokea, na kutumia mikakati ya kupunguza, watengenezaji wanaweza kuunda wakala wa AI ambao ni salama na wenye ufanisi. Zaidi ya hayo, kuingiza njia ya mtu-katikati ya mzunguko huhakikisha kwamba wakala wa AI wanabaki wanalengwa na mahitaji ya watumiaji huku wakipunguza hatari. Kadiri AI inavyoendelea, kudumisha msimamo wa kuhamasisha kuhusu usalama, faragha, na maadili kutakuwa muhimu katika kukuza imani na kuaminika katika mifumo inayotumia AI.

### Una Maswali Zaidi kuhusu Kuunda Wakala wa AI wa Kuaminika?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ili kutembelea wageni wengine, kuhudhuria saa za ofisi na kupata majibu kwa maswali yako ya Wakala wa AI.

## Rasilimali Zaidi

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Muhtasari wa AI inayowajibika</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Tathmini ya mifano ya AI ya kizazi na programu za AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Ujumbe wa mfumo wa usalama</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Kiolezo cha Tathmini ya Hatari</a>

## Somo lililopita

[Agentic RAG](../05-agentic-rag/README.md)

## Somo lijalo

[Muundo wa Mipango ya Muundo](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifa cha Kuachilia**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya kwanza inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa habari muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutoa fidia kwa maelewano au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->