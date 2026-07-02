[![Trustworthy AI Agents](../../../translated_images/te/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ఈ పాఠం వీడియో చూడటానికి పై చిత్రం క్లిక్ చేయండి)_

# నమ్మదగిన AI ఏజెంట్ల నిర్మాణం

## పరిచయము

ఈ పాఠములో చర్చించబడేది:

- సురక్షితమయిన, ఫలప్రదమైన AI ఏజెంట్లను ఎలా నిర్మించాలి మరియు అమలు చేయాలి
- AI ఏజెంట్లు అభివృద్ధి చేసే సమయంలో ముఖ్య సెక్యూరిటీ పరామర్శలు
- AI ఏజెంట్లు అభివృద్ధి సమయంలో డేటా మరియు მომხმარరి గోప్యతను ఎలా నిలుపుకోవాలి

## నేర్చుకోవాల్సిన లక్ష్యాలు

ఈ పాఠం పూర్తి చేసిన తర్వాత, మీరు తెలిసుకోవచ్చు:

- AI ఏజెంట్లు సృష్టించే సమయానికి ప్రమాదాలు గుర్తించటం మరియు వాటిని తగ్గింపు
- డేటా మరియు యాక్సెస్ సక్రమంగా నిర్వహించబడుటకు సెక్యూరిటీ చర్యలు అమలు చేయడం
- డేటా గోప్యతను నిలుపుకునే మరియు ఉత్తమమైన వినియోగదారు అనుభవాన్ని అందించే AI ఏజెంట్లు సృష్టించడం

## సేఫ్టీ

ముందుగా సురक्षित agentic అప్లికేషన్లను నిర్మించడాన్ని చూద్దాం. సేఫ్టీ అంటే AI ఏజెంట్ డిజైన్ ప్రకారం స్పందించటం. agentic అప్లికేషన్ల నిర్మాణకర్తలాగా, మేము సేఫ్టీని గరిష్టం చేసేందుకు పద్ధతులు మరియు పరికరాలు కలిగి ఉంటాము:

### సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ నిర్మాణం

మీరు LLMs ఉపయోగించి AI అప్లికేషన్ ఎప్పుడైనా నిర్మించుంటే, బలమైన సిస్టమ్ ప్రాంప్ట్ లేదా సిస్టమ్ మెసేజ్ డిజైన్ ప్రాముఖ్యత మీకు తెలుసు. ఈ ప్రాంప్ట్‌లు LLM వినియోగదారుని మరియు డేటాను ఎలా పరస్పరం అవుతుందో నియంత్రించే మెటా నియమాలు, సూచనలు, మార్గదర్శకాలను ఏర్పాటు చేస్తాయి.

AI ఏజెంట్ల కోసం, సిస్టమ్ ప్రాంప్ట్ మరింత ముఖ్యమయినది ఎందుకంటే AI ఏజెంట్లు మా డిజైన్ చేసిన పనులను పూర్తిచేయడానికి ఖచ్చితమైన సూచనలు అవసరం.

స్కేలబుల్ సిస్టమ్ ప్రాంప్ట్‌లను సృష్టించేందుకు, మనం ఒక లేదా ఎక్కువ ఏజెంట్లను నిర్మించడానికి సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ ఉపయోగించవచ్చు:

![Building a System Message Framework](../../../translated_images/te/system-message-framework.3a97368c92d11d68.webp)

#### దశ 1: మెటా సిస్టమ్ మెసేజ్ సృష్టించండి

మెటా ప్రాంప్ట్ LLM ద్వారా ఏజెంట్ల కోసం సిస్టమ్ ప్రాంప్ట్‌లను ఉత్పత్తి చేయడానికి ఉపయోగించబడుతుంది. అవసరమైతే చాలా ఏజెంట్లను సురక్షితంగా తయారు చేయడానికి టెంప్లేట్‌గా దీన్ని రూపొందిస్తాము.

ఇక్కడ మేము LLM కు ఇస్తున్న ఒక మెటా సిస్టమ్ మెసేజ్ ఉదాహరణ ఉంది:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### దశ 2: ప్రాథమిక ప్రాంప్ట్ సృష్టించండి

తర్వాత దశ AI ఏజెంట్ గురించి ప్రాథమిక ప్రాంప్ట్ సృష్టించడం. మీరు ఏజెంట్ పాత్ర, ఏజెంట్ చేసే పనులు మరియు ఇతర బాధ్యతలను చేర్చాలి.

ఇది ఒక ఉదాహరణ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### దశ 3: ప్రాథమిక సిస్టమ్ మెసేజ్ LLM కు అందించండి

ఇప్పుడు ఈ సిస్టమ్ మెసేజ్‌ ను మెటా సిస్టమ్ మెసేజ్ మరియు మా ప్రాథమిక సిస్టమ్ మెసేజ్ ఇవ్వడం ద్వారా మెరుగుపరచవచ్చు.

ఇది మా AI ఏజెంట్లకు మార్గనిర్దేశం చేయడానికి మంచిగా రూపుదిద్దిన సిస్టమ్ మెసేజ్ ఉత్పత్తి చేస్తుంది:

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

#### దశ 4: పునర్విచారించి మెరుగుపర్చండి

ఈ సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ విలువ అనేక ఏజెంట్ల నుండి సిస్టమ్ మెసేజ్‌లను సులభంగా సృష్టించగలగడం మరియు మీ సిస్టమ్ మెసేజ్‌లను సమయం తో మెరుగుపరచడం. మొదటి సారి మీ పూర్తి వాడుక కేసు కోసం పని చేసే సిస్టమ్ మెసేజ్ raro ఉంటుంది. ప్రాథమిక సిస్టమ్ మెసేజ్ మార్చి దాన్ని సిస్టమ్ ద్వారా నడిపించి ఫలితాలను సమీక్షించడము మరియు తక్కువ మార్పులు చేయడం మీకు వీలవుతుంది.

## ప్రమాదాలను అర్థం చేసుకోవడం

నమ్మదగిన AI ఏజెంట్లను నిర్మించడానికి, మీ AI ఏజెంట్ పై ప్రమాదాలు మరియు تهديدాలను అర్థం చేసుకోవడం మరియు తగ్గింపు చేయడం ముఖ్యము. AI ఏజెంట్లపై ఉన్న కొన్ని భిన్నమైన ప్రమాదాలు మరియు మీరు వాటి కోసం ఎలా మెరుగుగా ప్రణాళిక మరియు సిద్ధమవ్వవచ్చు అనేది చూద్దాం.

![Understanding Threats](../../../translated_images/te/understanding-threats.89edeada8a97fc0f.webp)

### పని మరియు సూచన

**వివరణ:** దాడి చేసే వారు ప్రాంప్టింగ్ లేదా ఇన్‌పుట్లను చేతలిఫిం చేయడం ద్వారా AI ఏజెంట్ సూచనలు లేదా లక్ష్యాలను మార్చాలని యత్నిస్తారు.

**తగ్గింపు**: AI ఏజెంట్ పని చేసేముందు ప్రమాదకర ప్రాంప్ట్‌లను గమనించేందుకు ధ్రువీకరణ తనిఖీలు మరియు ఇన్‌పుట్ ఫిల్టర్లను అమలు చేయండి. ఈ దాడులు సాధారణంగా తరచూ ఏజెంట్‌తో సంభాషణ అవసరం అవుతూ ఉంటాయి కనుక సంభాషణ టర్న్‌ల సంఖ్యను పరిమితం చేయడం ఈ రకపు దాడులను నివారించగలదు.

### అతి కీలకమైన వ్యవస్థలకు యాక్సెస్

**వివరణ:** AI ఏజెంట్ సంజ్ఞోపరమైన డేటాను గుప్తంగా ఉంచే వ్యవస్థలు మరియు సేవలకు యాక్సెస్ ఉంటే, దాడి చేసే వారు ఏజెంట్ మరియు ఈ సేవల మధ్య కమ్యూనికేషన్‌ను చెలామణి చేయవచ్చు. ఇది నేరుగా దాడులు లేదా ఏజెంట్ ద్వారా ఈ వ్యవస్థల గురించి సమాచారాన్ని సంపాదించడానికి ప్రయత్నాలు కావచ్చు.

**తగ్గింపు:** ఈ రకపు దాడులను నివారించేందుకు AI ఏజెంట్లకు అవసరమైన సందర్భాల్లోనే వ్యవస్థలకు యాక్సెస్ ఉండాలి. ఏజెంట్ మరియు వ్యవస్థ మధ్య కమ్యూనికేషన్ కూడా సురక్షితం కావాలి. ధృవీకరణ మరియు యాక్సెస్ కంట్రోల్ అమలు చేయడం మరొక రక్షణ మార్గం.

### వనరు మరియు సేవలో ఓవర్‌లోడ్

**వివరణ:** AI ఏజెంట్లు పనులు పూర్తిచేయటానికి వివిధ సాధనాలు మరియు సేవలను యాక్సెస్ చేయగలవు. దాడి చేసే వారు AI ఏజెంట్ ద్వారా పెద్ద సంఖ్యలో అభ్యర్థనలు పంపించడం ద్వారా ఈ సేవలు దెబ్బతీయవచ్చు, తద్వారా వ్యవస్థ జాగ్రత్తల వైఫల్యం లేదా అధిక ఖర్చు ఏర్పడవచ్చు.

**తగ్గింపు:** AI ఏజెంట్ సర్వీస్‌కు చేయగల అభ్యర్థనల సంఖ్యలను పరిమితం చేసే విధానాలు అమలు చేయండి. సంభాషణ టర్న్‌లను మరియు AI ఏజెంట్‌కు అభ్యర్థనలు సంఖ్యను పరిమితం చేయడం ఈ రకపు దాడులను నివారించడంలో సహాయపడుతుంది.

### జ్ఞాన కేంద్రం విషము

**వివరణ:** ఈ రకమైన దాడి నేరుగా AI ఏజెంట్‌ను లక్ష్యంగా చేసుకోవడం లేదు కానీ AI ఏజెంట్ ఉపయోగించే జ్ఞాన కేంద్రం మరియు ఇతర సేవలను లక్ష్యం చేస్తుంది. ఇది ఆ డేటాను పాడుచేయడం లేదా AI ఏజెంట్ పనితీరుకు దుష్ప్రభావం కలిగించే సమాచారం నాస్థమవ్వడం ఉండవచ్చు, ఫలితంగా వైఖరులు వక్రీకృతమయ్యే అవకాశం ఉంటుంది.

**తగ్గింపు:** AI ఏజెంట్ పని చేసే డేటా తరచూ తనిఖీలు చేయండి. ఈ డేటాకు యాక్సెస్ సురక్షితంగా ఉండి, నమ్మకమైన వ్యక్తులచే మాత్రమే మార్చబడేలా చూసుకోండి.

### వరస తప్పిదాలు

**వివరణ:** AI ఏజెంట్లు వివిధ సాధనాలు మరియు సేవలను పని పూర్తిచేయటానికి యాక్సెస్ చేస్తాయి. దాడి చేసే వారి కారణంగా వచ్చే తప్పిదాలు ఇతర వ్యవస్థల వైఫల్యాలకు దారి తీస్తాయి, ఇది దాడిని మరింత వ్యాప్తి చేస్తుంది మరియు పరిష్కరించడం కష్టం అవుతుంది.

**తగ్గింపు:** దీనిని నివారించడానికి ఒక మార్గం ఆ ఏజెంట్‌లను పరిమిత వాతావరణంలో నిర్వహించడం, ఉదాహరణకు డోకర్ కంటైనర్‌లో పనులు చేయించడం, తద్వారా ప్రత్యక్ష వ్యవస్థ దాడులను నివారించవచ్చు. తప్పిద ప్రతిస్పందనలు ఇచ్చే కొన్ని వ్యవస్థల కోసం బాకాఫ్ మరియు రీట్రై లాజిక్ సృష్టించడం పెద్ద వైఫల్యాల నివారణలో సహాయపడుతుంది.

## హ్యూమన్-ఇన్-ది-లూప్

నమ్మదగిన AI ఏజెంట్ వ్యవస్థలు సృష్టించడం కోసం మరొక సమర్థవంతమైన మార్గం హ్యూమన్-ఇన్-ది-లూప్ ఉపయోగించడం. ఇది ఓ ప్రవాహం సృష్టిస్తుంది, ఇందులో వినియోగదారులు ఏజెంట్లకు రన్ సమయంలో ఫీడ్‌బ్యాక్ ఇచ్చేందుకు వీలుగా ఉంటారు. వినియోగదారులు బహుళ ఏజెంట్ వ్యవస్థలో ఏజెంట్లుగా పనిచేస్తూ, ప్రస్తుత ప్రక్రియను ఆమోదించటం లేదా నిలిపేయటం ద్వారా పాలుపంచుకుంటారు.

![Human in The Loop](../../../translated_images/te/human-in-the-loop.5f0068a678f62f4f.webp)

ఈ భావనను Microsoft Agent Framework ఉపయోగించి ఎలా అమలు చేస్తారో చూపే కోడ్ స్నిపెట్:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# మానవ-ఇన్-ద-లూప్ ఆమోదంతో ప్రొవైడర్‌ను సృష్టించండి
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# మానవ ఆమోద దశతో ఏజెంట్‌ను సృష్టించండి
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# వినియోగదారు స్పందనను పరిశీలించి ఆమోదించవచ్చు
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## ముగింపు

నమ్మదగిన AI ఏజెంట్లను నిర్మించేటప్పుడు జాగ్రత్తపూర్వక డిజైన్, బలమైన సెక్యూరిటీ చర్యలు, మరియు నిరంతర పునర్విచారాలు అవసరం. నిర్మితమైన మెటా ప్రాంప్ట్ సిస్టమ్‌లు అమలు చేయడం, సాద్యమైన ప్రమాదాలను అర్థం చేసుకోవడం, మరియు తగ్గింపు వ్యూహాలు అన్వయించడం ద్వారా, డెవలపర్లు సురక్షితమయిన మరియు ఫలప్రదమైన AI ఏజెంట్లను సృష్టించగలుగుతారు. అదనంగా, హ్యూమన్-ఇన్-ది-లూప్ విధానాన్ని కలిపితే, AI ఏజెంట్లు వినియోగదారు అవసరాలకు సరిపోయేటట్లు ఉండి, ప్రమాదాలను తగ్గించగలవు. AI అభివృద్ధి కొనసాగుతున్న తరుణంలో, సెక్యూరిటీ, గోప్యత మరియు నైతిక అంశాలపై ముందుండటం నమ్మకానికి మరియు విశ్వసనీయతకు కీలకం.

## కోడ్ నమూనాలు

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): మెటా-ప్రాంప్ట్ సిస్టమ్-మెసేజ్ ఫ్రేమ్‌వర్క్ యొక్క దశలవారీ ప్రదర్శన.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): నమ్మదగిన ఏజెంట్లకు ముందస్తు అనుమతి గేట్లు, ప్రమాద స్థాయిల విభజన, మరియు ఆడిట్ లాగింగ్.

### నమ్మదగిన AI ఏజెంట్ల నిర్మాణం గురించి మరిన్ని ప్రశ్నలు ఉన్నాయా?

ఇతర నేర్చుకునే వారిని కలుసుకోవడానికి, ఆఫీసు గంటలకు హాజరు కావడానికి మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు జవాబులు పొందడానికి [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) చేరండి.

## అదనపు వనరులు

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">బాధ్యతగల AI అవలోకనం</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">సృష్టించే AI మోడల్లు మరియు AI అప్లికేషన్ల మూల్యాంకనం</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">సురక్షిత సిస్టమ్ మెసేజ్‌లు</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ప్రమాద మదింపుల నమూనా</a>

## గత పాఠం

[Agentic RAG](../05-agentic-rag/README.md)

## వచ్చే పాఠం

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->