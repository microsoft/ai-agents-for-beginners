[![విశ్వసనీయ AI ఏజెంట్లు](../../../translated_images/te/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ఈ పాఠం వీడియో చూడడానికి పై చిత్రం పై క్లిక్ చేయండి)_

# విశ్వసనీయ AI ఏజెంట్ల నిర్మాణం

## పరిచయం

ఈ పాఠం కింద ఉన్నాయి:

- సురక్షితమైన మరియు సమర్థవంతమైన AI ఏజెంట్లను ఎలా నిర్మించాలి మరియు మౌలికంగా అమలు చేయాలి
- AI ఏజెంట్లను అభివృద్ధి చేసే సమయంలో ముఖ్యమైన భద్రతా ఆలొచనలు.
- AI ఏజెంట్లను అభివృద్ధి చేసే సమయంలో డేటా మరియు వినియోగదారుల గోప్యతను ఎలా నిర్వహించాలి.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం పూర్తి చేసిన తర్వాత, మీరు తెలుసుకోగలుగుతారు:

- AI ఏజెంట్లను సృష్టించేటప్పుడు ప్రమాదాలను గుర్తించి తగ్గించడం ఎలా.
- డేటా మరియు ప్రాప్తిని సక్రమంగా నిర్వహించేందుకు భద్రతా చర్యలు అమలు చేయడం.
- డేటా గోప్యతను సంరక్షించే మరియు మంచి వినియోగదారుల అనుభవాన్ని అందించేది AI ఏజెంట్లను సృష్టించడం.

## భద్రత

ముందుగా సురక్షిత agentic అప్లికేషన్లను నిర్మించడం చూద్దాం. భద్రత అంటే AI ఏజెంట్ రూపకల్పన ప్రకారం పనిచేయాలి. agentic అప్లికేషన్ల నిర్మాణకారులుగా, మనకు భద్రతను గరిష్టం చేయడానికి పద్ధతులు మరియు సాధనాలున్నాయి:

### సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ రూపొందించడం

మీరు ఎప్పుడైనా LLMs (Large Language Models) ఉపయోగించి AI అప్లికేషన్ నిర్మించినట్లయితే, బలమైన సిస్టమ్ ప్రాంప్ట్ లేదా సిస్టమ్ మెసేజ్ డిజైన్ ప్రాముఖ్యత మీకు తెలుసు. ఈ ప్రాంప్ట్స్ మెటా నియమాలు, సూచనలు మరియు మార్గదర్శకాలను ఏర్పాటు చేస్తాయి, LLM వినియోగదారుడు మరియు డేటాతో ఎలా ఇంటరాక్ట్ అవుతుంది అన్నది నిర్దేశిస్తాయి.

AI ఏజెంట్స్‌కి, సిస్టమ్ ప్రాంప్ట్ మరింత ముఖ్యం అవుతుంది, ఎందుకంటే AI ఏజెంట్లు మనం రూపకల్పన చేసిన పనులను పూర్తి చేయడానికి చాలా నిర్దిష్ట సూచనల్నే అవసరం పడతాయి.

నిర్మాణం కచ్చితమైన సిస్టమ్ ప్రాంప్ట్‌ల కోసం, మనం ఒక లేదా అంతకంటే ఎక్కువ ఏజెంట్లను మన అప్లికేషన్‌లో నిర్మించడానికి సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ ఉపయోగించవచ్చు:

![సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ తయారు చేయడం](../../../translated_images/te/system-message-framework.3a97368c92d11d68.webp)

#### దశ 1: మెటా సిస్టమ్ మెసేజ్ సృష్టించండి

మెటా ప్రాంప్ట్‌ను LLM ఉపయోగించి మనం సృష్టించే ఏజెంట్ల కోసం సిస్టమ్ ప్రాంప్ట్‌లను జనరేట్ చేయడానికి ఉపయోగిస్తారు. దాన్ని మేము టెంప్లేట్ రూపంలో రూపకల్పన చేస్తాము, అవసరమైతే బహుళ ఏజెంట్లను సమర్థవంతంగా సృష్టించుకునేందుకు.

ఇది మన LLM కు ఇచ్చే మెటా సిస్టమ్ మెసేజ్ యొక్క ఉదాహరణ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### దశ 2: ప్రాథమిక ప్రాంప్ట్ సృష్టించండి

తర్వాతి దశ AI ఏజెంట్ వివరించడానికి ప్రాథమిక ప్రాంప్ట్ సృష్టించడం. ఏజెంట్ పాత్ర, ఏజెంట్ పూర్తి చేయబోయే పనుల వివరములు మరియు ఏజెంట్ బాధ్యతలు ఇతర అంశాలు చేర్చాలి.

ఇది ఒక ఉదాహరణ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### దశ 3: ప్రాథమిక సిస్టమ్ మెసేజ్ LLMకు ఇవ్వడం

ఇప్పుడు మనం ఈ సిస్టమ్ మెసేజ్‌ను మెటా సిస్టమ్ మెసేజ్‌ను కూడా ప్రదర్శించి, మన ప్రాథమిక సిస్టమ్ మెసేజ్‌తో మిళితం చేస్తూ మెరుగుపరచవచ్చు.

దీంతో మన AI ఏజెంట్లకు మార్గనిర్దేశకంగా మెరుగైన సిస్టమ్ మెసేజ్ తయారవుతుంది:

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

#### దశ 4: పునరావృతం చేసి మెరుగుపరచడం

ఈ సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ విలువ, బహుళ ఏజెంట్ల నుండి సులభంగా సిస్టమ్ మెసేజ్‌లను సృష్టించగలగడం మరియు మీ సిస్టమ్ మెసేజ్‌లను కాలానుగుణంగా మెరుగుపర్చగలగడం. మీ పూర్తి ఉపయోగ కేసుకు మొదటి ప్రయత్నంలో సరిపోయే సిస్టమ్ మెసేజ్ ఉండటం అరుదు. ప్రాథమిక సిస్టమ్ మెసేజ్ మార్చడం మరియు దాన్ని సిస్టమ్ ద్వారా మరల ఆపరేట్ చేయడం ద్వారా చిన్న మార్పులు, మెరుగుదలలను చేయగలగడం, ఫలితాలను పోల్చడం, అంచనా వేయడానికి వీలు కల్పిస్తుంది.

## ముప్పులను అర్థం చేసుకోవడం

విశ్వసనీయ AI ఏజెంట్లను నిర్మించడానికి, మీ AI ఏజెంట్‌కు ఉన్న ప్రమాదాలు మరియు ముప్పులను అర్థం చేసుకుని తగ్గించడం ముఖ్యం. AI ఏజెంట్లకు ఉన్న వివిధ ముప్పులలో కొన్నిటినే చూస్తూ మీరు ఈ వాటిని ఎలా మెరుగ్గా ప్రణాళిక చేసుకుని సిద్ధమవ్వొచ్చు.

![ముప్పులను అర్థం చేసుకోవడం](../../../translated_images/te/understanding-threats.89edeada8a97fc0f.webp)

### పని మరియు సూచన

**వివరణ:** దోపిడీదారులు AI ఏజెంట్ సూచనలు లేదా లక్ష్యాలను ప్రాంప్టింగ్ లేదా ఇన్‌పుట్‌లను మానిప్యులేషన్ చేయడం ద్వారా మార్చడానికి యత్నిస్తారు.

**తగ్గింపు**: ప్రమాదకర ప్రాంప్ట్‌లను AI ఏజెంట్ ప్రాసెస్‌ చేయక ముందు గుర్తించేందుకు ధృవీకరణ తనిఖీలు మరియు ఇన్‌పుట్ ఫిల్టర్లను అమలు చేయండి. ఈ దాడులు ఎక్కువగా ఏజెంట్‌తో తరచూ సహకరించాల్సినవ కావున, సంభాషణ టర్న్‌ల సంఖ్యను పరిమితం చేయడం ఈ దాడులను నివారించే మరో మార్గం.

### కీలక సిస్టమ్‌లకు ప్రాప్తి

**వివరణ**: AI ఏజెంట్ సున్నితమైన డేటాను నిల్వ చేసే సిస్టమ్స్ మరియు సేవలకు ప్రాప్తి ఉంటే, దోపిడీదారులు ఏజెంట్ మరియు ఈ సేవల మధ్య కమ్యూనికేషన్‌ను దాడి చేయవచ్చు. ఇవి ప్రత్యక్ష దాడులు లేదా ఏజెంట్ ద్వారా ఈ సిస్టమ్స్ గురించి సమాచారం పొందడానికి సూచనలు కావచ్చు.

**తగ్గింపు**: ఈ రకమైన దాడులను నివారించేందుకు AI ఏజెంట్లు అవసరమైన సిస్టమ్స్ మాత్రమే ప్రాప్తి ఉండాలి. ఏజెంట్ మరియు సిస్టమ్ మధ్య కమ్యూనికేషన్ కూడా సురక్షితం కావాలి. గుర్తింపు మరియు ప్రాప్తి నియంత్రణ అమలు చేయడం మరో రక్షణ మార్గం.

### వనరులు మరియు సేవలను అధిక బండిల్‌ చేయడం

**వివరణ:** AI ఏజెంట్లు పలు సాధనాలు మరియు సేవలను పనులు పూర్తి చేసేందుకు ప్రాప్తి కలిగినవి. దోపిడీదారులు AI ఏజెంట్ ద్వారా ఎక్కువ రిక్వెస్టులు పంపించి ఈ సేవలపై దాడి చేయవచ్చు, దీనివల్ల సిస్టమ్ వైఫల్యాలు లేదా అధిక ఖర్చులు అవ్వచ్చు.

**తగ్గింపు:** AI ఏజెంట్ సర్వీసుకు పంపే రిక్వెస్టుల సంఖ్యను పరిమితం చేసే విధానాలు అమలు చేయండి. సంభాషణ టర్న్‌లను మరియు రిక్వెస్టుల సంఖ్యను పరిమితం చేయడం ఇలాంటి దాడులను నిరోధించే మరో మార్గం.

### జ్ఞానాధారపు విషపు సంక్రమణ

**వివరణ:** ఈ రకం దాడి AI ఏజెంట్‌కు ప్రత్యక్ష దాడి చేయదు కానీ AI ఏజెంట్ ఉపయోగించే జ్ఞానాధారం మరియు ఇతర సేవలను లక్ష్యంగా చేసుకుంటుంది. ఇది విధంగా డేటా కర墓త చేయడం లేదా AI ఏజంట్ పనులు పూర్తి చేసేందుకు ఉపయోగించే సమాచారం అవిశ్వసనీయమయ్యేలా చేసి, బైయాస్ లేదా అక్రమ ప్రత్యుత్తరాలు వచ్చేలా చేస్తుంది.

**తగ్గింపు:** AI ఏజెంట్ ఉపయోగించే డేటాను తరచుగా ధృవీకరించి చూడండి. ఈ డేటాకు ప్రాప్తి సురక్షితంగా ఉండాలి మరియు కేవలం నమ్మకమైన వ్యక్తుల ద్వారా మాత్రమే మార్పులు చేయబడాలి.

### పదునైన తప్పిదాలు

**వివరణ:** AI ఏజెంట్లు పనులు పూర్తి చేసేందుకు పలు సాధనాలు మరియు సేవలకు ప్రాప్తి కలిగి ఉంటాయి. దోపిడీదారుల సృష్టించిన తప్పిదాలు AI ఏజెంట్ అనుసంధానమైన ఇతర సిస్టముల వైఫల్యాలకు దారితీస్తాయి, దాని కారణంగా దాడి మరింత విస్తృతమై, నిరోధించడం కష్టం అవుతుంది.

**తగ్గింపు**: ఈ సమస్యను నివారించడానికి ఒక రకమైన పద్ధతి AI ఏజెంట్‌ను పరిమిత వాతావరణంలో నిర్వహించడం, ఉదాహరణకు Docker కంటైనర్‌లో పనులు చేయించడం, ప్రత్యక్ష సిస్టమ్ దాడులను నిరోధిస్తుంది. కొన్ని సిస్టములు తప్పులు సూచిస్తే fallback మెహెకనిజంలు మరియు రీట్రై లాజిక్ సృష్టించడం కూడా పెద్ద సిస్టమ్ వైఫల్యాల నిలిపేందుకు సహాయం చేస్తుంది.

## మానవ-ఇన్-ది-లూప్

ఇంకో సమర్థవంతమైన విధానం విశ్వసనీయ AI ఏజెంట్ సిస్టమ్లను నిర్మించడంలో మానవ-ఇన్-ది-లూప్ ఉపయోగించడం. ఇది ఒక విధంగా వినియోగదారులు ఏజెంట్లకు రన్ సమయంలో అభిప్రాయం ఇచ్చే అవకాశాన్ని కల్పిస్తుంది. వినియోగదారులు బహుళ ఏజెంట్ సిస్టమ్లో ఏజెంట్‌లుగా ప్రతిభావంతంగా వ్యవహరిస్తారు మరియు జరిగుతున్న ప్రక్రియకు ఆమోదం లేదా రద్దు ఇవ్వగలుగుతారు.

![లూప్‌లో మానవుడు](../../../translated_images/te/human-in-the-loop.5f0068a678f62f4f.webp)

ఈ భావనను ఎలా అమలు చేసినారో చూపేందుకు Microsoft Agent Framework ఉపయోగించి ఒక కోడ్ ఉదాహరణ:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# మానవ-ఇన్-ది-లూప్ ఆమోదంతో ప్రొవైడర్ని సృష్టించండి
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# మానవ ఆమోదం దశతో ఏజెంట్‌ను సృష్టించండి
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# వినియోగదారు స్పందనను సమీక్షించి ఆమోదించవచ్చు
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## ముగింపు

విశ్వసనీయ AI ఏజెంట్లను నిర్మించడానికి జాగ్రత్తగా రూపకల్పన, బలమైన భద్రతా చర్యలు, మరియు నిరంతర పునరావృతం అవసరం. నిర్మిత మెటా ప్రాంప్లింగ్ వ్యవస్థలను అమలు చేయడం, సాధ్యమైన ముప్పులను అర్థం చేసుకోవడం, తగ్గింపు వ్యూహాలను అనుసరించడం ద్వారా అభివృద్ధిదారులు సురక్షిత మరియు సమర్థవంతమైన AI ఏజెంట్లను సృష్టించవచ్చు. అదనంగా, మానవ-ఇన్-ది-లూప్ పద్ధతిని చేర్చడం వినియోగదారుల అవసరాలతో ఏజెంట్లను అనుసంధానంగా ఉంచడం, ప్రమాదాలను తగ్గించడం సాధ్యం అవుతుంది. AI అభివృద్ధి కొనసాగుతున్నందున భద్రత, గోప్యత, నైతిక అంశాలపై ముందస్తుగా జాగ్రత్తలు తీసుకోవడం విశ్వసనీయత మరియు నమ్మకం పెంచడంలో కీలకం అవుతుంది.

### విశ్వసనీయ AI ఏజెంట్ల నిర్మాణం గురించి ఇంకా ప్రశ్నలున్నాయా?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) లో చేరండి, ఇతర అభ్యాసకులతో కలవండి, ఆఫీస్ గంటలకు హాజరై మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానం పొందండి.

## అదనపు వనరులు

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ذمه وار AI సమీక్ష</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ఉత్పత్తి AI మోడల్స్ మరియు AI అనువర్తనాల కొలత</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">సురక్షిత సిస్టమ్ మెసేజ్‌లు</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ప్రమాద విలువ వేసే టెంప్లేట్</a>

## గత పాఠం

[Agentic RAG](../05-agentic-rag/README.md)

## తదుపరి పాఠం

[ప్లానింగ్ డిజైన్ ప్యాటర్న్](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత సూచన**:
ఈ డాక్యుమెంట్‌ను AI భాషా అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువాదం చేయబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించడం జరుగుతోందని ದయచేసి గమనించండి, కానీ ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పులు ఉండే అవకాశముంది. ఈ డాక్యుమెంట్ యొక్క అసలు భాషలో ఉండే 원 పత్రాన్ని అధికారిక మూలంగా పరిగణించవలసింది. ముఖ్యమైన సమాచారం కోసం, నిపుణుల చేతి అనువాదాన్ని చేయించుకోవాలని సూచించబడుతుంది. ఈ అనువాదం వాడకంతో కలిగే ఏవైనా అపార్థాలు లేదా తప్పు అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->