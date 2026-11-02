[![నమ్మదగిన AI ఏజెంట్లు](../../../translated_images/te/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ఈ పాఠం వీడియోను చూడడానికి పై చిత్రాన్ని క్లిక్ చేయండి)_

# నమ్మదగిన AI ఏజెంట్ల నిర్మాణం

## పరిచయం

ఈ పాఠం కింద పేర్కొన్న విషయాలను సమర్థించును:

- ఎలా సురక్షితమైన మరియు సమర్థవంతమైన AI ఏజెంట్లను నిర్మించటం మరియు అమలు చేయటం
- AI ఏజెంట్లు అభివృద్ధి చేయడంలో ముఖ్యమైన భద్రతా చింతనలు
- AI ఏజెంట్లు అభివృద్ధి చేయడంలో డేటా మరియు వినియోగదారు గోప్యతను ఎలా కాపాడుకోవాలి

## అభ్యాస లక్ష్యాలు

ఈ పాఠం పూర్తి చేసిన తరువాత, మీరు ఈ విషయాలను తెలుసుకుంటారు:

- AI ఏజెంట్లు సృష్టించినపుడు ఉన్న ప్రమాదాలను గుర్తించి నియంత్రించటం
- డేటా మరియు యాక్సెస్ సరైన రీతిలో నిర్వహించబడేలా భద్రతా చర్యలను అమలు చేయటం
- డేటా గోప్యతను కాపాడే సమర్ధవంతమైన AI ఏజెంట్లను సృష్టించడం మరియు మంచి వినియోగదారుని అనుభవం అందించడం

## సురక్షితత

ముందుగా, సురక్షిత agentic అనువర్తనాలు ఎలా నిర్మించాలో చూడాలి. సురక్షితత అంటే AI ఏజెంట్ రుజువు చేసిన విధంగా పనిచేయటం. agentic అనువర్తనాల తయారీదారులుగా, సురక్షితతను గరిష్టం చేసేందుకు మనకు పద్ధతులు మరియు టూల్స్ ఉన్నాయి:

### సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ నిర్మాణం

మీరు ఎప్పుడైనా Large Language Models (LLMs) ఉపయోగించి AI అనువర్తనం నిర్మించారా, అప్పుడు మిమ్మల్ని బలమైన సిస్టమ్ ప్రాంప్ట్ లేదా సిస్టమ్ మెసేజ్ డిజైన్ చేసే ప్రాముఖ్యత తెలుసు. ఈ ప్రాంప్టులు LLM వినియోగదారుని మరియు డేటాతో ఎలా పరస్పర చర్య చేస్తుందో నియంత్రించే మెటా నియమాలు, సూచనలు, మార్గదర్శకాలు నిర్వచిస్తాయి.

AI ఏజెంట్ల కొరకు, సిస్టమ్ ప్రాంప్ట్ మరింత ముఖ్యమైనది ఎందుకంటే AI ఏజెంట్లు మనం రూపకం చేసిన పనులు పూర్తి చేయడానికి ఎంతో స్పష్టమైన సూచనలు అవసరం.

కొంతమంది ఏజెంట్లను సృష్టించడానికి స్కేలబుల్ సిస్టమ్ ప్రాంప్ట్‌లను సృష్టించడానికి, మనం సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ ఉపయోగించవచ్చు:

![సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ నిర్మాణం](../../../translated_images/te/system-message-framework.3a97368c92d11d68.webp)

#### దశ 1: మెటా సిస్టమ్ మెసేజ్ సృష్టించండి

మెటా ప్రాంప్ట్ LLM ఉపయోగించి మనం సృష్టించే ఏజెంట్లకు సిస్టమ్ ప్రాంప్ట్‌లను తయారు చేస్తుంది. మనం దీనిని ఒక మ్యాత్రిక సాంద్రతగా డిజైన్ చేస్తాము, అప్పుడు అవసరమైతే ఎన్నో ఏజెంట్లు సులభంగా తయారుచేయవచ్చు.

ఇక్కడ మనం LLM కు ఇస్తున్న ఒక మెటా సిస్టమ్ మెసేజ్ ఉదాహరణ ఉంది:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### దశ 2: ఒక ప్రాథమిక ప్రాంప్ట్ సృష్టించండి

తరువాతి దశ AI ఏజెంట్ ను వివరించే ప్రాథమిక ప్రాంప్ట్ సృష్టించడం. మీరు ఏజెంట్ యొక్క పాత్ర, ఏజెంట్ చేసే పనులు, మరియు ఏజెంట్ యొక్క ఇతర బాధ్యతలను చేర్చాలి.

ఇక్కడ ఒక ఉదాహరణ ఉంది:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### దశ 3: ప్రాథమిక సిస్టమ్ మెసేజ్ ను LLM కు ఇవ్వండి

ఇప్పుడు మనం మెటా సిస్టమ్ మెసేజ్ మరియు మన ప్రాథమిక సిస్టమ్ మెసేజ్ ని సిస్టమ్ మెసేజ్ గా అందిస్తూ ఈ సిస్టమ్ మెసేజ్ ను మెరుగుపరచవచ్చు.

ఇది మన AI ఏజెంట్లను నడిపించడానికి మెరుగైన సిస్టమ్ మెసేజ్ ని తయారు చేస్తుంది:

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

#### దశ 4: పునరావృతం చేసి మెరుగుపరచండి

ఈ సిస్టమ్ మెసేజ్ ఫ్రేమ్‌వర్క్ విలువ ఏంటంటే మీరు ఎన్నో ఏజెంట్లకి సులభంగా సిస్టమ్ మెసేజ్‌లు సృష్టించడంలో సహాయం చేయటం మరియు మీ సిస్టమ్ మెసేజ్‌లను కాలక్రమంలో మెరుగుపరచటం. మీ పూర్తి యూజ్ కేసుకి మొదటిసారి సరిపోయే సిస్టమ్ మెసేజ్ కనిపించడం అరుదు. ప్రాథమిక సిస్టమ్ మెసేజ్ మార్చటం మరియు పునరావృతం చేయడం ద్వారా మీకు మెరుగైన ఫలితాలను సరిపోల్చుకోవచ్చు మరియు మూల్యాంకనం చేయవచ్చు.

## ముప్పులకు అవగాహన

నమ్మదగిన AI ఏజెంట్లు నిర్మించడానికి, మీ AI ఏజెంట్ పై ప్రమాదాలు మరియు ముప్పులను అర్థం చేసుకుని వాటిని తగ్గించడం ముఖ్యం. AI ఏజెంట్లపై ఉన్న కొంతమంది ముప్పులు మరియు మీరు ఎలా మెరుగ్గా ప్లాన్ చేసి సిద్ధం కావచ్చును చూద్దాం.

![ముప్పులకు అవగాహన](../../../translated_images/te/understanding-threats.89edeada8a97fc0f.webp)

### పని మరియు సూచనలు

**వివరణ:** దోపిడీదారులు AI ఏజెంట్ యొక్క సూచనలు లేదా లక్ష్యాలను ప్రాంప్టింగ్ లేదా ఇన్పుట్స్‌ ను మోసపూరితముగా మార్పు చేయడానికి ప్రయత్నిస్తారు.

**తగ్గింపు:** AI ఏజెంట్ ప్రాసెస్ చేసేముందు ప్రమాదకరమైన ప్రాంప్ట్‌లను గుర్తించడానికి నిర్ధారణా తనిఖీలు మరియు ఇన్పుట్ ఫిల్టర్స్ అమలు చేయండి. ఇటువంటి దాడులు ఎక్కువ ఇంటరాక్షన్ అవసరం కాబట్టి, సంభాషణలో మలుపుల సంఖ్యను పరిమితం చేయడం కూడా ఇలా దాడులను నివారించడంలో ఓ మార్గం.

### కీలకమైన వ్యవస్థలకు ప్రాప్తి

**వివరణ:** ఒక AI ఏజెంట్ సున్నితమైన డేటాను నిల్వచేసే వ్యవస్థలు మరియు సేవలకు యాక్సెస్ ఉన్నట్లయితే, దోపిడీదారులు ఏజెంట్ మరియు సేవల మధ్య కమ్యూనికేషన్‌ను దాడి చేయవచ్చు. ఇవి ప్రత్యక్ష దాడులు లేదా ఏజెంట్ ద్వారా ఈ వ్యవస్థల గురించి సమాచారం పొందే అసంక్షిప్త ప్రయత్నాలు కావచ్చు.

**తగ్గింపు:** AI ఏజెంట్లు అవసరమైతేని మాత్రమే వ్యవస్థలకు యాక్సెస్ కలిగి ఉండాలి. ఏజెంట్ మరియు వ్యవస్థ మధ్య కమ్యూనికేషన్ కూడా సురక్షితంగా ఉండాలి. authenticate మరియు access control అమలు చేయడం ద్వారా ఈ సమాచారాన్ని రక్షించవచ్చు.

### వనరు మరియు సేవల అధిక లోడింగ్

**వివరణ:** AI ఏజెంట్లు పనులను పూర్తి చేయడానికి వివిధ టూల్స్ మరియు సేవలను ప్రాప్తి చేయవచ్చు. దోపిడీదారులు AI ఏజెంట్ ద్వారా ఎక్కువ మొత్తంలో అభ్యర్థనలను పంపటం ద్వారా ఈ సేవలపై దాడి చేయవచ్చు, ఇది వ్యవస్థ విఫలమవడం లేదా అధిక ఖర్చులకు దారితీయవచ్చు.

**తగ్గింపు:** AI ఏజెంట్ ఒక సేవకు చేసే అభ్యర్థనల సంఖ్యను పరిమితి చేసే విధానాలు అమలు చేయండి. మీ AI ఏజెంట్ కి సంభాషణ మలుపులు మరియు అభ్యర్థనల పరిమితి ఇది కూడా దాదాపు ఇలాంటి దాడుల నుండి రక్షిస్తుంది.

### జ్ఞానభాండారం విషము

**వివరణ:** ఈ రకం దాడి AI ఏజెంట్ ప్రత్యక్షంగా లక్ష్యంగా చేసుకోదు కానీ AI ఏజెంట్ ఉపయోగించే జ్ఞానభాండారం మరియు ఇతర సేవలను లక్ష్యంగా చేసింది. ఇది దానికి సంబంధించిన డేటాను లేదా సమాచారం వైసైపోవడం వల్ల AI ఏజెంట్ పనులు చేయడంలో పక్షపాతం లేదా ఇష్టేతర ప్రతిస్పందనలకు దారితీయవచ్చు.

**తగ్గింపు:** AI ఏజెంట్ వచించు వర్క్‌ఫ్లో లో ఉపయోగించే డేటాను తరచుగా ధృవీకరించండి. ఈ డేటాకు యాక్సెస్ భద్రంగా ఉండేటట్లు చూస్తూ, నమ్మకమైన వ్యక్తులచే మాత్రమే మార్పులుపడుతుంది అన్నది నిర్ధారించండి.

### శ్రేయసమైన తప్పులు

**వివరణ:** AI ఏజెంట్లు పనులను పూర్తి చేయడానికి వివిధ టూల్లు మరియు సేవలను ఉపయోగిస్తాయి. దోపిడీదారుల కారణంగా తలెత్తిన తప్పులు ఇంకో వ్యవస్థల విజయవంతం లోపం కలిగిస్తాయి, దాని వల్ల దాడి మరింత విస్తరించి, లోతైన సమస్యలు పరిష్కరించటం కష్టం అవుతుంది.

**తగ్గింపు:** దీనిని నివారించడానికి ఒక పద్ధతి ఆ AI ఏజెంట్ పరిమిత వాతావరణంలో పనిచేయటం, ఉదాహరణకు ఒక Docker కంటైనర్ లో పనులు చేయటం, ప్రత్యక్ష వ్యవస్థ దాడులను నివారిస్తుంది. కొన్ని వ్యవస్థలు తప్పు వెనక్కి ఇచ్చేటపుడు fallback వ్యవస్థ మరియు retry లాజిక్ తయారు చేయటం కూడా పెద్ద వ్యవస్థ వైఫల్యాలను నివారిస్తుంది.

## మానవ - ఇన్-ది-లూప్

నమ్మదగిన AI ఏజెంట్ వ్యవస్థలను నిర్మించడానికి మరొక సమర్థవంతమైన మార్గం మానవ-ఇన్-ది-లూప్ ఉపయోగించడం. ఇది యూజర్లకు ఏజెంట్లకు నిర్వహణ సమయంలో అభిప్రాయం ఇవ్వగలిగే ప్రవాహాన్ని సృష్టిస్తుంది. యూజర్లు బహు-ఏజెంట్ వ్యవస్థలో ఏజెంట్లా వ్యవహరిస్తారు, ప్రాసెస్ అభిప్రాయం లేదా నిలిపివేత అందజేస్తారు.

![మానవ ఇన్-ది-లూప్](../../../translated_images/te/human-in-the-loop.5f0068a678f62f4f.webp)

ఈ భావనను ఎలా అమలు చేస్తున్నామో చూపించడానికి Microsoft Agent Framework ఉపయోగించి కోడ్ స్నిపెట్ ఇక్కడ ఉంది:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# మానవ-ఇన్-ది-లూప్ ఆమోదంతో ప్రొవైడర్‌ను సృష్టించండి
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# మానవ ఆమోద దశతో ఏజెంట్‌ను సృష్టించండి
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# వినియోగదారు ప్రతిస్పందనను సమీక్షించి ఆమోదించగలడు
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## ముగింపు

నమ్మదగిన AI ఏజెంట్లు నిర్మించడం జాగ్రత్తగా డిజైన్ చేయటం, బలమైన భద్రతా చర్యలు అమలు చేయటం, మరియు నిరంతర పునరావృతం చేయటం అవసరం. నిర్మితమైన మెటా ప్రాంప్టింగ్ వ్యవస్థలను అమలు చేసి, సంభవించే ప్రమాదాలను అర్థం చేసుకుని తగ్గింపు వ్యూహాలను వర్తింపచేసి, అభివృద్ధి దారులు సురక్షితమైన మరియు సమర్థవంతమైన AI ఏజెంట్లను తయారు చేయగలరు. అదనంగా, మానవ-ఇన్-ది-లూప్ విధానాన్ని చేర్చడం యూజర్ అవసరాలకి AI ఏజెంట్లు సరిపోయేలా చూసుకుంటూ ప్రమాదాలను తగ్గిస్తుంది. AI అభివృద్ధి కొనసాగుతుండగా భద్రత, గోప్యత మరియు నైతిక అంశాలపై ముందుగానే చర్యలు తీసుకోవటం AI ఆధారిత వ్యవస్థల నమ్మకానికి మరియు విశ్వసనీయతకు కీలకం.

## కోడ్ నమూనాలు

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): మెటా ప్రాంప్ట్ సిస్టమ్-మెసేజ్ ఫ్రేమ్‌వర్క్ యొక్క దశల వారీ ప్రదర్శన.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): నమ్మదగిన ఏజెంట్ల కోసం అనుమతి యొక్క ముందస్తు గేట్లు, ప్రమాద స్థాయిలు, మరియు ఆడిట్ లాగింగ్.

### నమ్మదగిన AI ఏజెంట్లను నిర్మించడంపై మరిన్ని ప్రశ్నలు ఉన్నాయా?

ఇతర అభ్యాసకులతో కలుసుకోవడానికి, ఆఫీస్ గంటలకు హాజరయ్యేందుకు, మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానాలు పొందేందుకు [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) లో చేరండి.

## అదనపు వనరులు

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">బాధ్యతాయుతమైన AI అవగాహన</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">సృష్టికర్త AI మోడళ్లు మరియు AI అప్లికేషన్ల మూల్యాంకనం</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">సురక్షిత సిస్టమ్ మెసేజ్లు</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">పనిగలింపు మూల్యాంకన మార్పిడీ పత్రం</a>

## గత పాఠం

[Agentic RAG](../05-agentic-rag/README.md)

## తదుపరి పాఠం

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->