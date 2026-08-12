[![Mashine Agents wa Kuaminika wa AI](../../../translated_images/sw/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

# Kujenga Mashine Agents wa Kuaminika wa AI

## Utangulizi

Somo hili litaelezea:

- Jinsi ya kuunda na kupeleka Mashine Agents wa AI salama na yenye ufanisi
- Mambo muhimu ya usalama wakati wa kuendeleza Mashine Agents wa AI.
- Jinsi ya kudumisha usiri wa data na watumiaji wakati wa kuendeleza Mashine Agents wa AI.

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utajua jinsi ya:

- Kutambua na kupunguza hatari wakati wa kuunda Mashine Agents wa AI.
- Kutekeleza hatua za usalama kuhakikisha kwamba data na ufikiaji vinadhibitiwa ipasavyo.
- Kuunda Mashine Agents wa AI wanaodumisha usiri wa data na kutoa uzoefu bora kwa mtumiaji.

## Usalama

Kwanza tuchunguze jinsi ya kujenga programu salama za mawakala. Usalama unamaanisha kuwa wakala wa AI hufanya kazi kama ilivyopangwa. Kama wajenzi wa programu za mawakala, tuna njia na zana za kuongeza usalama:

### Kujenga Mfumo wa Ujumbe wa Mfumo

Ikiwa umewahi kujenga programu ya AI ukitumia Modeli Kubwa za Lugha (LLMs), unajua umuhimu wa kubuni amri imara ya mfumo au ujumbe wa mfumo. Amri hizi huanzisha sheria za meta, maelekezo, na miongozo ya jinsi LLM itakavyoshirikiana na mtumiaji na data.

Kwa Mashine Agents wa AI, amri ya mfumo ni muhimu zaidi kwani Mashine Agents itahitaji maelekezo maalum sana kukamilisha majukumu tuliyoyapanga kwao.

Kuunda amri za mfumo zinazoweza kupanuliwa, tunaweza kutumia mfumo wa ujumbe wa mfumo kujenga wakala mmoja au zaidi katika programu yetu:

![Kujenga Mfumo wa Ujumbe wa Mfumo](../../../translated_images/sw/system-message-framework.3a97368c92d11d68.webp)

#### Hatua ya 1: Unda Ujumbe wa Meta wa Mfumo

Amri ya meta itatumika na LLM kuunda amri za mfumo kwa mawakala tunaowaunda. Tunabuni kama kiolezo ili tuweze kuunda mawakala wengi kwa ufanisi ikiwa inahitajika.

Hapa kuna mfano wa ujumbe wa meta wa mfumo ambao tutampeleka LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Hatua ya 2: Unda Amri ya Msingi

Hatua inayofuata ni kuunda amri ya msingi kuelezea Wakala wa AI. Unapaswa kujumuisha jukumu la wakala, kazi ambazo wakala atakamilisha, na majukumu mengine yoyote ya wakala.

Hapa kuna mfano:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Hatua ya 3: Toa Ujumbe wa Mfumo wa Msingi kwa LLM

Sasa tunaweza kuboresha ujumbe huu wa mfumo kwa kutoa ujumbe wa meta wa mfumo kama ujumbe wa mfumo pamoja na ujumbe wetu wa msingi wa mfumo.

Hii itazalisha ujumbe wa mfumo ulio bora zaidi wa kuongoza mawakala wetu wa AI:

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

Thamani ya mfumo huu wa ujumbe wa mfumo ni kuwawezesha kueneza uundaji wa ujumbe kutoka kwa mawakala wengi kwa urahisi pamoja na kuboresha ujumbe wako wa mfumo kwa muda. Ni nadra kupata ujumbe wa mfumo unaofanya kazi mara ya kwanza kwa matumizi yako kamili. Kuwa na uwezo wa kufanya marekebisho madogo na maboresho kwa kubadilisha ujumbe wa msingi wa mfumo na kuufanya kupitia mfumo kutakuwezesha kulinganisha na kutathmini matokeo.

## Kuelewa Vitisho

Ili kujenga mashine agents wa AI wa kuaminika, ni muhimu kuelewa na kupunguza hatari na vitisho kwa wakala wako wa AI. Hebu tuangalie baadhi tu ya vitisho tofauti kwa mawakala wa AI na jinsi unaweza kupanga na kujiandaa vizuri kwao.

![Kuelewa Vitisho](../../../translated_images/sw/understanding-threats.89edeada8a97fc0f.webp)

### Kazi na Maelekezo

**Maelezo:** Washambuliaji hujaribu kubadilisha maelekezo au malengo ya wakala wa AI kupitia amri au kuendesha pembejeo.

**Kuzuia**: Fanya ukaguzi wa kuthibitisha na vichujio vya pembejeo kugundua amri zinazoweza kuwa hatari kabla ya kushughulikiwa na Wakala wa AI. Kwa kuwa mashambulizi haya kawaida yanahitaji mwingiliano wa mara kwa mara na Wakala, kupunguza idadi ya mzunguko wa mazungumzo ni njia nyingine ya kuzuia aina hizi za mashambulizi.

### Ufikiaji wa Mifumo Muhimu

**Maelezo**: Ikiwa wakala wa AI anaweza kufikia mifumo na huduma zinazohifadhi data nyeti, washambuliaji wanaweza kuingilia mawasiliano kati ya wakala na huduma hizi. Hii inaweza kuwa mashambulizi ya moja kwa moja au majaribio ya moja kwa moja kupata taarifa kuhusu mifumo hii kupitia wakala.

**Kuzuia**: Mawakala wa AI wanapaswa kuwa na ufikiaji wa mifumo kwa misingi ya hitaji tu ili kuzuia aina hizi za mashambulizi. Mawasiliano kati ya wakala na mfumo pia yanapaswa kuwa salama. Kutekeleza uthibitishaji na udhibiti wa ufikiaji ni njia nyingine ya kulinda taarifa hii.

### Kupakia Rasilimali na Huduma

**Maelezo:** Mawakala wa AI wanaweza kufikia zana na huduma mbalimbali kukamilisha kazi. Washambuliaji wanaweza kutumia uwezo huu kushambulia huduma hizi kwa kutuma maombi mengi kupitia Wakala wa AI, jambo ambalo linaweza kusababisha mifumo kutofaulu au gharama kubwa.

**Kuzuia:** Tekeleza sera za kupunguza idadi ya maombi ambayo wakala wa AI anaweza kutuma kwa huduma. Kupunguza mzunguko wa mazungumzo na maombi kwa wakala wako wa AI ni njia nyingine ya kuzuia aina hizi za mashambulizi.

### Kupigia Sumu Misingi ya Maarifa

**Maelezo:** Aina hii ya mashambulizi haisilengi wakala wa AI moja kwa moja lakini inalenga msingi wa maarifa na huduma nyingine ambazo wakala wa AI atatumia. Hii inaweza kuhusisha kuharibu data au taarifa ambayo wakala wa AI atatumia kukamilisha kazi, na kusababisha majibu yenye upendeleo au yasiyokusudiwa kwa mtumiaji.

**Kuzuia:** Fanya uhakiki wa mara kwa mara wa data ambayo wakala wa AI atatumia katika mchakato wake. Hakikisha ufikiaji wa data hii ni salama na unabadilishwa tu na watu wa kuaminika ili kuepuka aina hii ya mashambulizi.

### Makosa Yanayoenea

**Maelezo:** Mawakala wa AI huingia kwenye zana na huduma mbalimbali kukamilisha kazi. Makosa yanayosababishwa na washambuliaji yanaweza kusababisha mifumo mingine ambayo wakala wa AI ameunganishwa nayo kufeli, na kufanya shambulizi hilo kuenea na kuwa gumu kutatua.

**Kuzuia**: Njia moja ya kuepuka hili ni kuwa na Wakala wa AI afanye kazi katika mazingira yaliyopunguzwa, kama kutekeleza kazi katika kontena la Docker, ili kuzuia mashambulizi ya moja kwa moja ya mfumo. Kuunda mbinu za kutegemea na mantiki ya kurudia wakati mifumo fulani inajibu kwa kosa ni njia nyingine ya kuzuia kutofaulu kwa mifumo kubwa.

## Mtu Mshiriki Katika Mzunguko

Njia nyingine yenye ufanisi ya kujenga mifumo ya Mashine Agents wa AI wa kuaminika ni kutumia Mtu katika mzunguko (Human-in-the-loop). Hii huunda mchakato ambapo watumiaji wanaweza kutoa maoni kwa mawakala wakati wa utekelezaji. Watumiaji kwa kweli hufanya kazi kama mawakala katika mfumo wa mawakala wengi kwa kutoa idhini au kusitisha mchakato unaoendelea.

![Mtu Mshiriki Katika Mzunguko](../../../translated_images/sw/human-in-the-loop.5f0068a678f62f4f.webp)

Hapa kuna kipande cha msimbo kinachoonyesha jinsi dhana hii inavyotekelezwa kwa kutumia Microsoft Agent Framework:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Unda mtoaji na idhini ya mtu katika mzunguko
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Unda wakala na hatua ya idhini ya mtu
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

Kujenga mashine agents wa AI wa kuaminika kunahitaji muundo makini, hatua thabiti za usalama, na kurudia mfululizo. Kwa kutekeleza mifumo iliyoandaliwa ya amri za meta ya mfumo, kuelewa vitisho vinavyoweza kuwepo, na kutumia njia za kupunguza hatari, waendelezaji wanaweza kuunda mashine agents wa AI ambao ni salama na wenye ufanisi. Zaidi ya hayo, kuingiza njia ya mtu katika mzunguko hutegemea kuwa mawakala wa AI wanabaki wakiwa sambamba na mahitaji ya watumiaji huku kupunguza hatari. Kadiri AI inavyoendelea kubadilika, kudumisha msimamo wa kuzuia usalama, usiri, na maadili kutakuwa muhimu kukuza imani na kuaminika katika mifumo inayoendeshwa na AI.

## Sampuli za Msimbo

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Maonyesho ya hatua kwa hatua ya mfumo wa amri za meta wa ujumbe wa mfumo.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Milango ya idhini kabla ya vitendo, upangaji wa hatari, na kurekodi ukaguzi kwa mawakala wa kuaminika.

### Una Maswali Zaidi Kuhusu Kujenga Mashine Agents wa Kuaminika wa AI?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanaojifunza wengine, kuhudhuria saa za ofisi, na kupata majibu ya maswali yako kuhusu Mashine Agents wa AI.

## Rasilimali Zaidi

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Muhtasari wa AI Inayowajibika</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Tathmini ya modeli za AI zinazozalisha na programu za AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Ujumbe wa mfumo wa usalama</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Kiolezo cha Tathmini ya Hatari</a>

## Somo la Awali

[Agentic RAG](../05-agentic-rag/README.md)

## Somo Linalofuata

[Mchoro wa Ubunifu wa Mipango](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->