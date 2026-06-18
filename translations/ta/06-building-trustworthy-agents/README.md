[![विश्वसनीय AI एजेंट्स](../../../translated_images/ta/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(இந்த பாடத்தின் காணொளியைப் பார்க்க மேலுள்ள படம் கிளிக் செய்யவும்)_

# நம்பகமான AI முகவர்கள் உருவாக்குதல்

## அறிமுகம்

இந்த பாடத்தில் எடுக்கப்படுவது:

- பாதுகாப்பான மற்றும் விளைவு விளைவுடைய AI முகவர்களை உருவாக்கி வெளியிடுவது எப்படி
- AI முகவர்கள் உருவாக்கும் போது முக்கியமான பாதுகாப்பு கவனிப்புகள்
- AI முகவர்கள் உருவாக்கும்போது தரவு மற்றும் பயனர் தனியுரிமையை எப்படி பராமரிப்பது

## கற்றல் நோக்கங்கள்

இந்த பாடத்தை முடித்த பிறகு, நீங்கள் எப்படி அறிந்து கொள்ளுவீர்கள்:

- AI முகவர்கள் உருவாக்கும்போது படுவதை அடையாளம் காண்பது மற்றும் தடுப்பதற்கான வழிகள்.
- தரவு மற்றும் அணுகலைச் சரியாக நிர்வகிப்பதற்கான பாதுகாப்பு நடவடிக்கைகளை செயல்படுத்தல்.
- தரவு தனியுரிமையை பராமரிக்கும் மற்றும் தரமான பயனர் அனுபவத்தை வழங்கும் AI முகவர்கள் உருவாக்கல்.

## பாதுகாப்பு

முதலில் பாதுகாப்பான முகவர் செயலிகள் உருவாக்குவோம். பாதுகாப்பு என்பது AI முகவர் வடிவமைக்கப்பட்டபடி செயல்படுவதை குறிக்கும். முகவர் செயலிகள் உருவாக்குநராக நாம் பாதுகாப்பை அதிகபட்சமாக்குவதற்கான முறைகள் மற்றும் கருவிகள் உள்ளன:

### ஒரு முறை செய்தி அமைப்பு வடிவமைத்தல்

நீங்கள் ஒருபோதும் பெரிய மொழி மாதிரிகளை (LLMs) பயன்படுத்தி AI செயலி உருவாக்கி இருந்தால், ஒரு வலுவான முறை (system) தடையோ அல்லது முறை செய்தியோ (system message) வடிவமைப்பின் முக்கியத்துவத்தை அறிந்திருப்பீர்கள். இந்த தடைகள் LLM பயனர் மற்றும் தரவுடன் எவ்வாறு தொடர்பு கொள்வதை நிர்ணயிக்கும் விதிகள், வழிகாட்டிகள் மற்றும் உத்தரவுகளை அமைக்கின்றன.

AI முகவர்களுக்கு, முறை தடையோ முக்கியத்துவமுடையது ஏனெனில் AI முகவர்கள் நாங்கள் வடிவமைத்துள்ள பணிகளை நிறைவேற்ற மிகத் தெளிவான உத்தரவுகள் தேவை.

பெரிதும் அளவிடக்கூடிய (scalable) முறை தடைகள் உருவாக்க, நாங்கள் செயலி உள்ள ஒரோ அல்லது அதற்கு மேற்பட்ட முகவர்கள் உருவாக்க ஒரு முறை செய்தி அமைப்பை பயன்படுத்தலாம்:

![ஒரு முறை செய்தி அமைப்பை உருவாக்குதல்](../../../translated_images/ta/system-message-framework.3a97368c92d11d68.webp)

#### படி 1: ஒரு மேட்டா முறை செய்தி உருவாக்கவும்

மேட்டா தடையை LLM பயன்படுத்தி உருவாக்கப்படும் முகவர்களுக்கான முறை தடைகளை உருவாக்கும். இது ஒரு வார்ப்புருவாக வடிவமைக்கப்படுகின்றது, இதனால் தேவையான பல முகவர்களை முழுமையாக எளிதாக உருவாக்க முடியும்.

LLM க்குத் தரப்படும் ஒரு மேட்டா முறை செய்தி உதாரணம்:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### படி 2: ஒரு அடிப்படை தடையை உருவாக்கவும்

அடுத்த படி AI முகவரின் விளக்கத்திற்கு ஒரு அடிப்படை தடையை உருவாக்குவது. முகவரின் பங்கு, முகவர் நிறைவேற்றும் பணிகள் மற்றும் முகவரின் வேறு பொறுப்புகளை சேர்க்க வேண்டும்.

உதாரணம்:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### படி 3: அடிப்படை முறை செய்தியை LLM க்கு வழங்குதல்

இப்போது, மேட்டா முறை செய்தியையும் அதே நேரத்தில் அடிப்படை முறை செய்தியையும் வழங்கி இந்த செய்தியை மேம்படுத்தலாம்.

இதனால் நமது AI முகவர்களை வழிநடத்த சிறந்த வடிவமைப்புடைய முறை செய்தி உருவாகும்:

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

#### படி 4: திருத்துதல் மற்றும் மேம்படுத்தல்

இந்த முறை செய்தி அமைப்பின் முக்கியத்துவம் பல முகவர்கள் உருவாக்கும் முறை செய்திகளை எளிதாக அளவிடersoq (scale) செய்வதுடன், உங்கள் முறை செய்திகள் நேரத்திற்குள் மேம்படுதலுக்கு வாய்ப்பளிக்கும். முதல்முறை உங்கள் முழு பயன்பாட்டிற்காக சரியாக செயல்படும் முறை செய்தியை பெறுவது அரிது. அடிப்படை முறை செய்தியில் சிறிய மாற்றங்கள் செய்து, அதை முறை மூலமாக இயக்கி முடிவுகளை ஒப்பிட்டு மதிப்பிடலாம்.

## அச்சுறுத்தல்களை புரிந்துகொள்வது

நம்பகமான AI முகவர்களை உருவாக்க, உங்கள் AI முகவரின் அபாயங்கள் மற்றும் அச்சுறுத்தல்களை புரிந்துகொண்டு தடுப்பது முக்கியம். AI முகவர்களுக்கு மட்டுமே சில அச்சுறுத்தல்களை பார்க்கலாம், அதைச் சரியான முறையில் திட்டமிடலாம் மற்றும் தயாராக இருக்கலாம்.

![அச்சுறுத்தல்களை புரிதல்](../../../translated_images/ta/understanding-threats.89edeada8a97fc0f.webp)

### பணி மற்றும் அறிவுரை

**விளக்கம்:** தாக்குதலாளர்கள் முறைவழிமுறைகள் அல்லது AI முகவரின் குறிக்கோள்களை மாற்ற முயலுகிறார்கள்.

**தடுப்பு**: AI முகவர் இதனை செயல்படுத்தும் முன்னர் சாத்தியமான ஆபத்தான முறைவழிமுறைகளை கண்டறிய சரிபார்ப்பு மற்றும் உள்ளீட்டு வடிகட்டியங்களை நடைமுறைப்படுத்தவும். இந்த சற்றுமுறைகள் பொதுவாக முகவருடன் தொடர்ந்து தொடர்பு கொண்டிருப்பதால், உரையாடல் முறைகளை கட்டுப்படுத்துவது பாதுகாப்புக்கு உதவும்.

### முக்கியமான அமைப்புகளுக்கு அணுகல்

**விளக்கம்**: AI முகவருக்கு முக்கிய தரவு இருக்கும் அமைப்புகள் மற்றும் சேவைகள் அணுகல் இருந்தால், தாக்குதலாளர்கள் இந்த தகவல்களைப் பெற அல்லது தொடர்பை உடைக்க முயன்றால் நேரடி அல்லது மறைமுக தாக்குதல்கள் ஏற்படலாம்.

**தடுப்பு**: AI முகவர்கள் இசையின் அடிப்படையில் மட்டுமே இச்சேவைகள் அணுக வேண்டும். முகவர் மற்றும் அமைப்புகள் இடையேயான தொடர்பும் பாதுகாப்பாக இருக்க வேண்டும். அங்கீகாரம் மற்றும் அணுகல் கட்டுப்பாடு நடைமுறைப்படுத்தப்பட வேண்டும்.

### வளங்கள் மற்றும் சேவைகள் மீறுதல்கள்

**விளக்கம்:** AI முகவர்கள் பணிகளை முடிக்க பிற கருவிகள் மற்றும் சேவைகளை அணுக முடியும். தாக்குதலாளர்கள் இந்த திறனுடன் அதிக கோரிக்கைகளை அனுப்பி சேவைகளை அறையச் செய்யலாம், இதனால் அமைப்புகள் தடுமாறலாம் அல்லது செலவுபெருக்கம் ஏற்படலாம்.

**தடுப்பு:** AI முகவர்கள் சேவைகளுக்கு அனுப்ப இயக்குவதற்கான கோரிக்கை எண்ணிக்கையை கட்டுப்படுத்தும் கொள்கைகளை உருவாக்கவும். உரையாடல் முறைகள் மற்றும் கோரிக்கைகள் எண்ணிக்கையை குறைப்பதுவும் இதற்கு உதவும்.

### அறிவு அறுக்கை மறைதல்

**விளக்கம்:** இந்தத் தாக்குதல் நேரடியாக AI முகவர்களைக் குறிவைக்காது, ஆனால் AI முகவரின் பணிக்கு பயன்படுத்தப்படும் அறிவு மையத்திற்கு மற்றும் பிற சேவைகளுக்குச் சேதம் செய்யும். இது தரவை அழுக்கு செய்தல் அல்லது தவறான பதில்களை உருவாக்கும்.

**தடுப்பு:** AI முகவர் வேலை விசாரணைகளில் பயன்படுத்தும் தரவை நிதானமாக சரிபார்க்க வேண்டும். இந்த தரவுக்கு நம்பகமான நபர்களால் மட்டுமே அணுகலும் மாற்றமும் நடக்க வேண்டும்.

### தொடர்ச்சியான பிழைகள்

**விளக்கம்:** AI முகவர்கள் பிற கருவிகள் மற்றும் சேவைகளை அணுகும் போது, தாக்குதலாளர்களால் ஏற்படும் பிழைகள் மற்ற அமைப்புகளிலும் தோல்வி ஏற்படுத்தும், இது தாக்குதலை விரிவடையச் செய்கிறது மற்றும் சிக்கல்களை அதிகரிக்கின்றது.

**தடுப்பு**: AI முகவர்களை ஒரு கட்டுப்படுத்தப்பட்ட சூழலில் இயக்குதல் (எ.கா., Docker குழாய்) நேரடி தாக்குதல் தவிர்ப்பதற்காக உதவும். தவறு வந்தால் fallback முறைகள் மற்றும் மறுஇயக்கக் கொள்கைகளை உருவாக்குவது கூட உதவும்.

## மனிதர் உள்ளடக்கிய செயல்முறை

நம்பகமான AI முகவர்கள் அமைப்புகளை உருவாக்க மற்றொரு பயனுள்ள செயல்முறை மனிதர் உள்ளடக்கியது. இது பயனர்கள் ஓர் முகவருக்கு பிரதியாக செயல்பட்டு, செயல்பாட்டின்போது கருத்துக்களை வழங்கும் முறை உருவாக்கும். பயனர்கள் ஓர் பல முகவர் அமைப்பில் முகவர்களாக செயல்பட்டு செயலின் அங்கீகார அல்லது நிறுத்தத்தை வழங்குகிறார்கள்.

![மனிதர் உள்ளடக்கிய செயல்முறை](../../../translated_images/ta/human-in-the-loop.5f0068a678f62f4f.webp)

இந்தக் கருத்து எப்படி செயல்படுத்தப்படுகிறது என்று காட்டும் Microsoft முகவர் அமைப்பு குறியீடு துணுக்கை இங்கே காணலாம்:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# மனிதர் இணைந்த ஒப்புதலுடன் வழங்குநரை உருவாக்கவும்
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# மனிதர் ஒப்புதல் படியை கொண்ட முகவரியை உருவாக்கவும்
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# பயனர் பதிலை பரிசீலித்து ஒப்புக் கொள்ளலாம்
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## முடிவு

நம்பகமான AI முகவர்களை உருவாக்குவது கவனமாக வடிவமைப்பது, வலுவான பாதுகாப்பு முறைகள், மற்றும் தொடர்ச்சியான திருத்தம் தேவை. கட்டமைக்கப்பட்ட மேட்டா முறைகள், சாத்தியமான அச்சுறுத்தல்களை நன்கு புரிந்து, தடுப்புக் கொள்கைகளை கவனித்தல் மூலம், பயன்பாட்டாளர்களுக்கு பாதுகாப்பான மற்றும் விளைவு அதிகமான AI முகவர்கள் உருவாக்கலாம். மேலும், மனிதர் உள்ளடக்கிய முறையை அமல்படுத்துவதன் மூலம் AI முகவர்கள் பயனர் தேவைகளுடன் இணங்கும் மற்றும் அபாயங்களை குறைக்கும். AI தொடர்ந்து முன்னேறிப்போகும்போது, பாதுகாப்பு, தனியுரிமை மற்றும் ஒழுங்கு கருத்துகளை முன்னேற்றுவது நம்பிக்கை மற்றும் நம்பகத்தன்மையை ஊக்குவிக்கும்.

## குறியீடு மாதிரிகள்

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): மேட்டா-தடை முறை செய்தி அமைப்பின் படி படியாக உள்ளக்காட்சி.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): முன்னுரிமை அங்கீகார வாயில்கள், அபாய வரிசைப்படுத்தல் மற்றும் நம்பகமான முகவர்களுக்கான ஆய்வு பதிவுகள்.

### நம்பகமான AI முகவர்கள் உருவாக்குவது பற்றி கூடுதல் கேள்விகள் உள்ளதா?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) இல் சேர்ந்துகொண்டு மற்ற கற்றுக்கொள்ளுபவர்களை சந்திக்கவும், அலுவலக நேரங்களில் கலந்துகொண்டு உங்கள் AI முகவர்கள் தொடர்பான கேள்விகளுக்கு பதில்கள் பெறவும்.

## கூடுதல் வளங்கள்

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">பொறுப்பான AI அறிமுகம்</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">உற்பத்திய செயல்திறன் மதிப்பீடு மற்றும் AI பயன்பாடுகள்</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">பாதுகாப்பு முறை செய்திகள்</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ஆபத்து மதிப்பீடு வார்ப்புரு</a>

## முந்தைய பாடம்

[Agentic RAG](../05-agentic-rag/README.md)

## அடுத்த பாடம்

[திட்டமிடும் வடிவமைப்பு மாதிரி](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->