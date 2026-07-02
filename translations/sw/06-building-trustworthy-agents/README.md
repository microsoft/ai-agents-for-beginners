[![Wakala wa AI wa Kuaminika](../../../translated_images/sw/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

# Kujenga Wakala wa AI wa Kuaminika

## Utangulizi

Somo hili litajumuisha:

- Jinsi ya kujenga na kutekeleza wakala salama na wenye ufanisi wa AI
- Mambo muhimu ya usalama wakati wa kuendeleza wakala wa AI.
- Jinsi ya kudumisha usiri wa data na mtumiaji wakati wa kuendeleza wakala wa AI.

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utaweza:

- Kutambua na kupunguza hatari wakati wa kuunda wakala wa AI.
- Kutekeleza hatua za usalama ili kuhakikisha data na ufikiaji vinadhibitiwa ipasavyo.
- Kuunda wakala wa AI ambao hudumisha usiri wa data na kutoa uzoefu bora kwa mtumiaji.

## Usalama

Kwanza tuangalie kujenga matumizi salama ya wakala. Usalama ina maana kwamba wakala wa AI hufanya kazi kama ilivyobuniwa. Kama wajenzi wa matumizi ya wakala, tuna mbinu na zana za kuongeza usalama:

### Kujenga Mfumo wa Ujumbe wa Mfumo

Iwapo umewahi kujenga programu ya AI kwa kutumia Modeli Kubwa za Lugha (LLMs), unajua umuhimu wa kubuni prompt thabiti ya mfumo au ujumbe wa mfumo. Hii huweka kanuni za meta, maagizo, na miongozo ya jinsi LLM itakavyoshirikiana na mtumiaji na data.

Kwa Wakala wa AI, prompt ya mfumo ni muhimu zaidi kwani wakala wa AI watahitaji maagizo maalum kabisa kukamilisha kazi ambazo tumebuni kwao.

Ili kuunda prompts za mfumo zinazoweza kupanuka, tunaweza kutumia mfumo wa ujumbe wa mfumo kujenga wakala mmoja au zaidi kwenye programu yetu:

![Kujenga Mfumo wa Ujumbe wa Mfumo](../../../translated_images/sw/system-message-framework.3a97368c92d11d68.webp)

#### Hatua ya 1: Tengeneza Ujumbe wa Meta wa Mfumo

Meta prompt itatumika na LLM kuunda prompts za mfumo kwa wakala tunaowaunda. Tunabuni kama templeti ili tuweze kuunda wakala wengi kwa ufanisi ikiwa inahitajika.

Hapa ni mfano wa ujumbe wa meta wa mfumo tungeupa LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Hatua ya 2: Tengeneza prompt ya msingi

Hatua inayofuata ni kuunda prompt ya msingi kuelezea Wakala wa AI. Unapaswa kujumuisha nafasi ya wakala, kazi ambazo wakala atazimaliza, na majukumu mengine yoyote ya wakala.

Hapa ni mfano:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Hatua ya 3: Toa Ujumbe wa Msingi wa Mfumo kwa LLM

Sasa tunaweza kuboresha ujumbe huu wa mfumo kwa kutoa ujumbe wa meta kama ujumbe wa mfumo pamoja na ujumbe wetu wa msingi wa mfumo.

Hii itazalisha ujumbe wa mfumo ulio bora zaidi kwa kuongoza wakala wetu wa AI:

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

#### Hatua ya 4: Rudia na Boreshaji

Thamani ya mfumo huu wa ujumbe wa mfumo ni kuwawezesha kuunda ujumbe wa mfumo kutoka kwa wakala wengi kwa urahisi pamoja na kuboresha ujumbe wako wa mfumo kwa muda. Ni nadra kupata ujumbe wa mfumo ambao unafanya kazi mara ya kwanza kwa matumizi yako kamili. Kuwa na uwezo wa kufanya marekebisho madogo na maboresho kwa kubadilisha ujumbe wa msingi wa mfumo na kuupitia mfumo kutakuruhusu kulinganisha na kutathmini matokeo.

## Kuelewa Vitisho

Ili kujenga wakala wa AI wa kuaminika, ni muhimu kuelewa na kupunguza hatari na vitisho kwa wakala wako wa AI. Tuchunguze baadhi tu ya vitisho tofauti kwa wakala wa AI na jinsi unaweza kupanga na kujiandaa vizuri kwao.

![Kuelewa Vitisho](../../../translated_images/sw/understanding-threats.89edeada8a97fc0f.webp)

### Kazi na Maagizo

**Maelezo:** Washambuliaji wanajaribu kubadilisha maagizo au malengo ya wakala wa AI kupitia prompt au kudanganya pembejeo.

**Kupunguza**: Fanya ukaguzi wa uthibitisho na vichujio vya pembejeo kugundua prompts zenye hatari kabla hazijashughulikiwa na Wakala wa AI. Kwa kuwa mashambulizi haya kwa kawaida yanahitaji mawasiliano mara kwa mara na Wakala, kupunguza idadi ya mzunguko katika mazungumzo ni njia nyingine ya kuzuia aina hizi za mashambulizi.

### Ufikiaji wa Mifumo Muhimu

**Maelezo**: Ikiwa wakala wa AI anaweza kufikia mifumo na huduma zinazohifadhi data nyeti, washambuliaji wanaweza kuingilia kati mawasiliano kati ya wakala na huduma hizi. Hizi zinaweza kuwa mashambulizi ya moja kwa moja au majaribio yasiyo ya moja kwa moja ya kupata taarifa kuhusu mifumo hii kupitia wakala.

**Kupunguza**: Wakala wa AI wanapaswa kuwa na ufikiaji wa mifumo kwa msingi wa haja tu ili kuzuia aina hizi za mashambulizi. Mawasiliano kati ya wakala na mfumo pia yanapaswa kuwa salama. Kutekeleza uthibitishaji na udhibiti wa ufikiaji ni njia nyingine za kulinda taarifa hii.

### Msongamano wa Rasilimali na Huduma

**Maelezo:** Wakala wa AI wanaweza kupata zana na huduma tofauti kukamilisha kazi. Washambuliaji wanaweza kutumia uwezo huu kushambulia huduma hizi kwa kutuma maombi mengi kupitia Wakala wa AI, jambo ambalo linaweza kusababisha mfumo kushindwa au gharama kubwa.

**Kupunguza:** Tekeleza sera za kupunguza idadi ya maombi ambayo wakala wa AI anaweza kutuma kwa huduma. Kupunguza idadi ya mizunguko ya mazungumzo na maombi kwa wakala wako wa AI ni njia nyingine ya kuzuia mashambulizi haya.

### Uchovu wa Msingi wa Maarifa

**Maelezo:** Aina hii ya shambulio haijumuishi wakala wa AI moja kwa moja lakini inalenga msingi wa maarifa na huduma zingine ambazo wakala wa AI atatumia. Hii inaweza kuhusisha kuharibu data au taarifa ambazo wakala wa AI atatumia kukamilisha kazi, na kusababisha majibu yenye upendeleo au yasiyotakiwa kwa mtumiaji.

**Kupunguza:** Fanya uhakiki wa mara kwa mara wa data ambayo wakala wa AI atatumia katika mifumo yake ya kazi. Hakikisha ufikiaji wa data hii ni salama na hubadilishwa tu na watu wenye imani ili kuepuka aina hii ya shambulio.

### Makosa Yanayofuatana

**Maelezo:** Wakala wa AI wanapata zana na huduma tofauti kukamilisha kazi. Makosa yaliyosababishwa na washambuliaji yanaweza kusababisha kufeli kwa mifumo mingine ambayo wakala wa AI amehusishwa nayo, na kusababisha shambulio kuwa pana zaidi na kuwa ngumu kuitatua.

**Kupunguza**: Njia moja ya kuepuka hili ni kuwa na Wakala wa AI afanye kazi katika mazingira yaliyopunguzwa, kama kufanya kazi katika kontena ya Docker, ili kuzuia mashambulizi ya moja kwa moja kwenye mfumo. Kuunda mbinu za kutembea na mantiki ya kujaribu tena wakati mifumo fulani inajibu na kosa ni njia nyingine ya kuzuia kushindwa kwa mifumo kubwa.

## Binadamu Katika Mzunguko

Njia nyingine yenye ufanisi ya kujenga mifumo ya Wakala wa AI wa kuaminika ni kutumia Binadamu katika mzunguko. Hii huunda mtiririko ambapo watumiaji wanaweza kutoa maoni kwa Wakala wakati wa utekelezaji. Watumiaji kwa msingi ni wakala katika mfumo wa wakala wengi na kwa kutoa idhini au kusitisha mchakato unaoendelea.

![Binadamu Katika Mzunguko](../../../translated_images/sw/human-in-the-loop.5f0068a678f62f4f.webp)

Hapa kuna kipande cha msimbo kinachotumia Microsoft Agent Framework kuonyesha jinsi dhana hii inavyotekelezwa:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Unda muuzaji kwa idhini ya mwanadamu katika mzunguko
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Unda wakala na hatua ya idhini ya mwanadamu
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

Kujenga wakala wa AI wa kuaminika kunahitaji muundo makini, hatua madhubuti za usalama, na kurudia mara kwa mara. Kwa kutekeleza mifumo ya meta prompting iliyopangwa, kuelewa vitisho vinavyowezekana, na kutumia mikakati ya kupunguza, waendelezaji wanaweza kuunda wakala wa AI ambao ni salama na wenye ufanisi. Zaidi ya hayo, kuingiza njia ya binadamu katika mzunguko kuna hakikisha wakala wa AI wanabaki wakiwa sambamba na mahitaji ya mtumiaji huku wakipunguza hatari. AI inapendelea kuendelea kubadilika, kudumisha mtazamo wa kujiandaa kuhusu usalama, usiri, na maadili kutakuwa kiini cha kuendeleza imani na kuaminika katika mifumo inayotegemea AI.

## Mifano ya Msimbo

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Maelezo ya hatua kwa hatua ya mfumo wa meta-prompt na ujumbe wa mfumo.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Mlangoni wa idhini kabla ya kitendo, upangaji wa hatari, na uandikishaji wa ukaguzi kwa wakala wa kuaminika.

### Una Maswali Zaidi Kuhusu Kujenga Wakala wa AI wa Kuaminika?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu Wakala wa AI.

## Rasilimali Zaidi

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Muhtasari wa AI Inayohusika</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Tathmini ya mifano ya AI inayotengeneza na programu za AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Ujumbe wa mfumo wa usalama</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Kiolezo cha Tathmini ya Hatari</a>

## Somo lililopita

[Agentic RAG](../05-agentic-rag/README.md)

## Somo lijalo

[Mpangilio wa Muundo wa Mipango](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->