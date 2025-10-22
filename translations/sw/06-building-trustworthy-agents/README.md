<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T19:55:00+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "sw"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.sw.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

# Kujenga Mawakala wa AI Wenye Kuaminika

## Utangulizi

Somo hili litashughulikia:

- Jinsi ya kujenga na kupeleka Mawakala wa AI salama na wenye ufanisi.
- Masuala muhimu ya usalama wakati wa kuunda Mawakala wa AI.
- Jinsi ya kudumisha faragha ya data na watumiaji wakati wa kuunda Mawakala wa AI.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utajua jinsi ya:

- Kutambua na kupunguza hatari wakati wa kuunda Mawakala wa AI.
- Kutekeleza hatua za usalama ili kuhakikisha data na ufikiaji vinadhibitiwa ipasavyo.
- Kuunda Mawakala wa AI wanaodumisha faragha ya data na kutoa uzoefu bora kwa mtumiaji.

## Usalama

Hebu kwanza tuangalie jinsi ya kujenga programu za mawakala salama. Usalama unamaanisha kwamba wakala wa AI anafanya kazi kama ilivyokusudiwa. Kama watengenezaji wa programu za mawakala, tuna mbinu na zana za kuongeza usalama:

### Kujenga Mfumo wa Ujumbe wa Mfumo

Ikiwa umewahi kuunda programu ya AI kwa kutumia Large Language Models (LLMs), unajua umuhimu wa kubuni mfumo wa ujumbe wa mfumo ulio imara. Ujumbe huu huweka sheria za msingi, maelekezo, na miongozo ya jinsi LLM itakavyoshirikiana na mtumiaji na data.

Kwa Mawakala wa AI, ujumbe wa mfumo ni muhimu zaidi kwani Mawakala wa AI wanahitaji maelekezo maalum sana ili kukamilisha majukumu tuliyowapangia.

Ili kuunda ujumbe wa mfumo unaoweza kupanuka, tunaweza kutumia mfumo wa ujumbe wa mfumo kwa ajili ya kujenga wakala mmoja au zaidi katika programu yetu:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.sw.png)

#### Hatua ya 1: Unda Ujumbe wa Mfumo wa Meta

Ujumbe wa meta utatumika na LLM kuunda ujumbe wa mfumo kwa mawakala tunaowaunda. Tunaunda kama kiolezo ili tuweze kuunda mawakala wengi kwa ufanisi ikiwa inahitajika.

Hapa kuna mfano wa ujumbe wa mfumo wa meta ambao tungepatia LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Hatua ya 2: Unda Ujumbe wa Msingi

Hatua inayofuata ni kuunda ujumbe wa msingi wa kuelezea Wakala wa AI. Unapaswa kujumuisha jukumu la wakala, majukumu ambayo wakala atakamilisha, na majukumu mengine yoyote ya wakala.

Hapa kuna mfano:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Hatua ya 3: Toa Ujumbe wa Msingi kwa LLM

Sasa tunaweza kuboresha ujumbe huu wa mfumo kwa kutoa ujumbe wa mfumo wa meta kama ujumbe wa mfumo na ujumbe wetu wa msingi wa mfumo.

Hii itazalisha ujumbe wa mfumo uliobuniwa vizuri kwa kuongoza Mawakala wetu wa AI:

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

Thamani ya mfumo huu wa ujumbe wa mfumo ni uwezo wa kupanua kuunda ujumbe wa mfumo kwa mawakala wengi kwa urahisi pamoja na kuboresha ujumbe wako wa mfumo kwa muda. Ni nadra kuwa na ujumbe wa mfumo unaofanya kazi mara ya kwanza kwa matumizi yako kamili. Uwezo wa kufanya marekebisho madogo na maboresho kwa kubadilisha ujumbe wa msingi wa mfumo na kuendesha kupitia mfumo utakuwezesha kulinganisha na kutathmini matokeo.

## Kuelewa Vitisho

Ili kujenga Mawakala wa AI wenye kuaminika, ni muhimu kuelewa na kupunguza hatari na vitisho kwa wakala wako wa AI. Hebu tuangalie baadhi tu ya vitisho tofauti kwa Mawakala wa AI na jinsi unavyoweza kupanga na kujiandaa vyema.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.sw.png)

### Majukumu na Maelekezo

**Maelezo:** Washambuliaji wanajaribu kubadilisha maelekezo au malengo ya wakala wa AI kupitia kuandika au kudanganya pembejeo.

**Kupunguza:** Tekeleza ukaguzi wa uthibitisho na vichujio vya pembejeo ili kugundua maelekezo hatari kabla ya kuchakatwa na Wakala wa AI. Kwa kuwa mashambulizi haya kwa kawaida yanahitaji mwingiliano wa mara kwa mara na Wakala, kupunguza idadi ya mizunguko katika mazungumzo ni njia nyingine ya kuzuia mashambulizi ya aina hii.

### Ufikiaji wa Mifumo Muhimu

**Maelezo:** Ikiwa wakala wa AI ana ufikiaji wa mifumo na huduma zinazohifadhi data nyeti, washambuliaji wanaweza kuhatarisha mawasiliano kati ya wakala na huduma hizi. Haya yanaweza kuwa mashambulizi ya moja kwa moja au majaribio ya moja kwa moja ya kupata taarifa kuhusu mifumo hii kupitia wakala.

**Kupunguza:** Mawakala wa AI wanapaswa kuwa na ufikiaji wa mifumo kwa msingi wa mahitaji tu ili kuzuia mashambulizi ya aina hii. Mawasiliano kati ya wakala na mfumo yanapaswa pia kuwa salama. Kutekeleza uthibitisho na udhibiti wa ufikiaji ni njia nyingine ya kulinda taarifa hii.

### Kuelemea Rasilimali na Huduma

**Maelezo:** Mawakala wa AI wanaweza kufikia zana na huduma tofauti ili kukamilisha majukumu. Washambuliaji wanaweza kutumia uwezo huu kushambulia huduma hizi kwa kutuma idadi kubwa ya maombi kupitia Wakala wa AI, ambayo inaweza kusababisha kushindwa kwa mfumo au gharama kubwa.

**Kupunguza:** Tekeleza sera za kupunguza idadi ya maombi ambayo wakala wa AI anaweza kufanya kwa huduma. Kupunguza idadi ya mizunguko ya mazungumzo na maombi kwa wakala wako wa AI ni njia nyingine ya kuzuia mashambulizi ya aina hii.

### Uchafuzi wa Msingi wa Maarifa

**Maelezo:** Aina hii ya shambulio hailengi wakala wa AI moja kwa moja lakini inalenga msingi wa maarifa na huduma nyingine ambazo wakala wa AI atatumia. Hii inaweza kuhusisha kuharibu data au taarifa ambayo wakala wa AI atatumia kukamilisha jukumu, na kusababisha majibu yenye upendeleo au yasiyotarajiwa kwa mtumiaji.

**Kupunguza:** Fanya uthibitisho wa mara kwa mara wa data ambayo wakala wa AI atatumia katika mtiririko wake wa kazi. Hakikisha kwamba ufikiaji wa data hii ni salama na unabadilishwa tu na watu wanaoaminika ili kuepuka shambulio la aina hii.

### Makosa Yanayozidi

**Maelezo:** Mawakala wa AI wanapata zana na huduma mbalimbali ili kukamilisha majukumu. Makosa yanayosababishwa na washambuliaji yanaweza kusababisha kushindwa kwa mifumo mingine ambayo wakala wa AI umeunganishwa nayo, na kusababisha shambulio kuwa kubwa zaidi na gumu kutatua.

**Kupunguza:** Njia moja ya kuepuka hili ni kuwa na Wakala wa AI akifanya kazi katika mazingira yaliyopunguzwa, kama vile kutekeleza majukumu katika kontena la Docker, ili kuzuia mashambulizi ya moja kwa moja ya mfumo. Kuunda mifumo ya kurudi nyuma na mantiki ya kurudia wakati mifumo fulani inajibu na kosa ni njia nyingine ya kuzuia kushindwa kwa mifumo mikubwa.

## Binadamu Katika Mzunguko

Njia nyingine bora ya kujenga mifumo ya Mawakala wa AI yenye kuaminika ni kutumia Binadamu Katika Mzunguko. Hii huunda mtiririko ambapo watumiaji wanaweza kutoa maoni kwa Mawakala wakati wa mchakato wa utekelezaji. Watumiaji kimsingi hufanya kama mawakala katika mfumo wa mawakala wengi kwa kutoa idhini au kusitisha mchakato unaoendelea.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.sw.png)

Hapa kuna kipande cha msimbo kinachotumia AutoGen kuonyesha jinsi dhana hii inavyotekelezwa:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Hitimisho

Kujenga Mawakala wa AI wenye kuaminika kunahitaji muundo makini, hatua madhubuti za usalama, na mabadiliko ya mara kwa mara. Kwa kutekeleza mifumo ya meta ya ujumbe iliyopangwa, kuelewa vitisho vinavyoweza kutokea, na kutumia mikakati ya kupunguza, watengenezaji wanaweza kuunda Mawakala wa AI ambao ni salama na wenye ufanisi. Zaidi ya hayo, kuingiza mbinu ya binadamu katika mzunguko huhakikisha kwamba Mawakala wa AI wanabaki sambamba na mahitaji ya watumiaji huku wakipunguza hatari. Kadri AI inavyoendelea kubadilika, kudumisha msimamo wa kuzuia kuhusu usalama, faragha, na masuala ya kimaadili kutakuwa muhimu katika kukuza uaminifu na kutegemewa katika mifumo inayoendeshwa na AI.

### Una Maswali Zaidi Kuhusu Kujenga Mawakala wa AI Wenye Kuaminika?

Jiunge na [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ili kukutana na wanafunzi wengine, kuhudhuria masaa ya ofisi, na kupata majibu ya maswali yako kuhusu Mawakala wa AI.

## Rasilimali za Ziada

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Muhtasari wa AI yenye Uwajibikaji</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Tathmini ya mifano ya AI ya kizazi na programu za AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Ujumbe wa mfumo wa usalama</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Kiolezo cha Tathmini ya Hatari</a>

## Somo la Awali

[Agentic RAG](../05-agentic-rag/README.md)

## Somo Linalofuata

[Planning Design Pattern](../07-planning-design/README.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.