[![நம்பிக்கையுடைந்த AI தயாரிப்பாளர்கள்](../../../translated_images/ta/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(இந்த பாடத்தின் வீடியோவை பார்க்க மேலுள்ள படத்தைச் சொடுக்குக)_

# நம்பிக்கையுடைந்த AI தயாரிப்பாளர்களை உருவாக்குதல்

## அறிமுகம்

இந்த பாடத்தில் கீழ்காணும் விஷயங்கள் உள்ளடக்கமாக இருக்கும்:

- பாதுகாப்பான மற்றும் விளைவான AI தயாரிப்பாளர்களை உருவாக்கி உருவாக்குவதும்
- AI தயாரிப்பாளர்களை உருவாக்கும்போது முக்கியமான பாதுகாப்பு வரையறைகள்.
- AI தயாரிப்பாளர்களை உருவாக்கும்போது தரவு மற்றும் பயனர் தனியுரிமையை பராமரிப்பது எப்படி.

## கற்றல் நோக்குகள்

இந்த பாடத்தை முடித்த பின்பு, நீங்கள் அறிவீர்கள் எப்படி:

- AI தயாரிப்பாளர்களைக் உருவாக்கும்போது உரத்த அபாயங்களைக் கண்டறிந்து குறைக்க.
- தரவு மற்றும் அணுகலை பொருத்தமாக நிர்வகிக்க பாதுகாப்பு நடவடிக்கைகள் அமல்படுத்த.
- தரவு தனியுரிமையை பராமரிக்கும் மற்றும் தரமான பயனர் அனுபவத்தை வழங்கும் AI தயாரிப்பாளர்களை உருவாக்க.

## பாதுகாப்பு

முதலில் பாதுகாப்பான உதவியாளர் பயன்பாடுகளை உருவாக்குதல் பற்றி பார்ப்போம். பாதுகாப்பு என்பது AI உதவியாளர் வடிவமைத்தபடி செயல்படுவதை குறிக்கும். உதவியாளர் பயன்பாடுகளை உருவாக்கி வருகிறது என்ற வகையில், பாதுகாப்பை அதிகபட்சப்படுத்தும் முறைகள் மற்றும் கருவிகள் உள்ளன:

### ஒரு சிஸ்டம் செய்தி கட்டமைப்பை உருவாக்குதல்

நீங்கள் ஏற்கனவே பெரும் மொழி மாதிரிகளைக் (LLMs) கொண்டு AI பயன்பாடுகளை உருவாக்கி இருந்தால், ஒரு வலுவான சிஸ்டம் புரொம்ப்ட் அல்லது சிஸ்டம் செய்தியை வடிவமைப்பது முக்கியத்துவம் என்பதைக் அறிவீர்கள். இந்த புரொம்ப்டுகள் LLM எப்படி பயனர் மற்றும் தரவுடன் தொடர்பு கொள்ளும் என்பது குறித்த மேட்டா விதிகள், வழிமுறைகள் மற்றும் வழிகாட்டுதல்களை உருவாக்குகின்றன.

AI தயாரிப்பாளர்களுக்காக, சிஸ்டம் புரொம்ப்ட் மேலும் முக்கியமானவையாகும், ஏனெனில் AI தயாரிப்பாளர்கள் நாம் அவர்களுக்கு அமைத்த பணிகளை முடிக்க மிகவும் துல்லியமான வழிமுறைகள் தேவைப்படும்.

பெருமளவில் சிஸ்டம் புரொம்ப்டுகளை உருவாக்க, நமது பயன்பாட்டில் ஒரு அல்லது அதற்கு மேற்பட்ட உதவியாளர்களை உருவாக்க ஒரு சிஸ்டம் செய்தி கட்டமைப்பைப் பயன்படுத்தலாம்:

![ஒரு சிஸ்டம் செய்தி கட்டமைப்பை உருவாக்குதல்](../../../translated_images/ta/system-message-framework.3a97368c92d11d68.webp)

#### படி 1: ஒரு மேட்டா சிஸ்டம் செய்தி உருவாக்குதல்

மேட்டா புரொம்ப்ட் எங்களால் உருவாக்கும் உதவியாளர்களுக்கான சிஸ்டம் புரொம்ப்டுகளை உருவாக்க ஒரு LLM கொண்டு பயன்படுத்தப்படும். இது பல உதவியாளர்களை துல்லியமாக உருவாக்க மாதிரி வடிவில் வடிவமைக்கப்படுகிறது.

பின்வருமாறு ஒரு உதாரண மேட்டா சிஸ்டம் செய்தி:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### படி 2: அடிப்படையான புரொம்ப்டை உருவாக்குதல்

அடுத்து AI தயாரிப்பாளரை விவரிக்கும் அடிப்படையான புரொம்ப்டை உருவாக்க வேண்டும். நீங்கள் உதவியாளரின் பங்கு, முடிக்கவேண்டிய பணிகள் மற்றும் பிற பொறுப்புகளை சேர்க்க வேண்டும்.

இங்கே ஒரு உதாரணம்:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### படி 3: அடிப்படை சிஸ்டம் செய்தியை LLMக்கு வழங்குதல்

இப்போது மேட்டா சிஸ்டம் செய்தியை சிஸ்டம் செய்தியாக வழங்கி, நமது அடிப்படை சிஸ்டம் செய்தியுடன் சேர்த்து இந்த செய்தியை மேம்படுத்தலாம்.

இதனால் நமது AI உதவியாளர்களுக்கு வழிகாட்ட சிறந்த வடிவமைப்புடைய சிஸ்டம் செய்தி உருவாகும்:

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

#### படி 4: திருத்தவும் மேம்படுத்தவும்

இந்த சிஸ்டம் செய்தி கட்டமைப்பு மதிப்பு அதன் மூலம் பல உதவியாளர்களுக்கான சிஸ்டம் செய்திகளை சிறிது குணமாகவும், நேரத்தில்தான் உங்கள் செய்திகளை மேம்படுத்தவும் உதவும். உங்கள் முழுமையான பயன்பாட்டுக்கு முதல் முறையைச் சரியாக இயங்கும் சிஸ்டம் செய்தி கிடைக்கும் வாய்ப்பு குறைவு. அடிப்படை சிஸ்டம் செய்தியை மாற்றி அதை சிஸ்டம் மூலமாக இயங்கச் செய்து குணப்படுத்தும் வாயிலாக முடிவுகளைக் நோக்கிச் салыக்கவும் மதிப்பீடு செய்யவும் முடியும்.

## அபாயங்களை புரிந்து கொள்வது

நம்பிக்கையுடைந்த AI தயாரிப்பாளர்களை உருவாக்க, உங்கள் AI உதவியாளருக்கு ஏற்பட்ட அபாயங்கள் மற்றும் அச்சுறுத்தல்களை புரிந்து கொள்ளவும், குறைக்கவும் முக்கியம். AI உதவியாளர்களுக்கு உள்ள சில அபாயங்களையும் அதைத் தடுக்க எப்படி திட்டமிடலாம், தயாராக இருக்கலாம் என்பதையும் பார்ப்போம்.

![அபாயங்களைப் புரிந்து கொள்வது](../../../translated_images/ta/understanding-threats.89edeada8a97fc0f.webp)

### பணி மற்றும் வழிமுறை

**விளக்கம்:** தாக்குதல்காரர்கள் AI உதவியாளரின் குறிக்கோள்களை அல்லது வழிமுறைகளை புரொம்ப்டிங் அல்லது உள்ளீடுகள் மூலம் மாற்ற முயலுவர்.

**தடுக்கல்:** AI உதவியாளரால் செயலாக்கப்படுவதற்கு முன் ஆபத்தான புரொம்ப்ட்களை கண்டறிய சோதனைகள் மற்றும் உள்ளீடு வடிகட்டிகள் இயக்கப்பட வேண்டும். இந்தத் தாக்குதல்கள் பொதுவாக உதவியாளருடன் அடிக்கடி தொடர்பு கொள்ள வேண்டியதால், உரையாடலில் முறைகள் எண்ணிக்கை வரையல் இதனைத் தடுக்கும் ஒரு வழி.

### முக்கியமான அமைப்புகளுக்கு அணுகல்

**விளக்கம்:** AI உதவியாளர் சென்சிட்டிவ் தரவை சேமிக்கும் அமைப்புகள் மற்றும் சேவைகளை அணுகினால், தாக்குதல்காரர்கள் இந்த சேவைகள் மற்றும் உதவியாளருக்கு இடையேயான தொடர்பை மீறக்கூடும். இது நேரடியான அல்லது பிரத்யேகமான முறைகளில் அமையக்கூடும்.

**தடுக்கல்:** AI உதவியாளர்கள் தேவையானவசமாக மட்டுமே அமைப்புகளுக்கு அணுகல்கொள்ள வேண்டும். உதவியாளரும் அமைப்பும் இடையேயான தொடர்பு பாதுகாப்பானதாக இருக்க வேண்டும். அங்கீகாரம் மற்றும் அணுகல் கட்டுப்பாட்டை நடைமுறைப்படுத்தல் பாதுகாப்புக்கு உதவும்.

### வளம் மற்றும் சேவை அதிகப்படிநிறுத்தல்

**விளக்கம்:** AI உதவியாளர்கள் நான்கு கருவிகள் மற்றும் சேவைகளை பயன்படுத்தி பணி முடிக்கும். தாக்குதல்காரர்கள் AI உதவியாளரின் மூலம் அதிக எண்ணிக்கையிலான கோரிக்கைகள் அனுப்பி சேவைகளை தாக்கலாம், இது அமைப்பு தோல்வி அல்லது அதிக செலவுக்கு வழிவகுக்கும்.

**தடுக்கல்:** AI உதவியாளர் ஒரு சேவைக்கு அனுப்பக்கூடிய கோரிக்கைகள் எண்ணிக்கையை வரையறுக்கும் கொள்கைகள் அமல்படுத்த வேண்டும். உரையாடல் முறைகள் மற்றும் கோரிக்கைகள் எண்ணிக்கை வரையல் இதனைத் தடுக்கும் மற்றொரு வழிமுறை.

### அறிவு தளம் மாசுபாடு

**விளக்கம்:** இந்தத் தாக்குதல் நேரடியாக AI உதவியாளரை இலக்காக செய்யாது, ஆனால் அதற்கு பயன்படும் அறிவு தளம் மற்றும் பிற சேவைகளை இலக்காக செய்யும். AI உதவியாளர் பணி செய்ய பயன்படுத்தும் தரவு அல்லது தகவலை மாசுபடுத்துவதன் மூலம் பாகுபாடுடைய அல்லது எதிர்பாராத பதில்களைக் கையாளச் செய்யும்.

**தடுக்கல்:** AI உதவியாளர் பயன்படும் தரவை அடிக்கடி சரிபார்க்கவேண்டும். இந்த தரவை அணுகும் வாய்ப்புகள் பாதுகாப்பாகவும், நம்பகமான நபர்களால் மட்டுமே மாற்றப்படுவதில் உறுதிப்படுத்த வேண்டும்.

### தொடர் பிழைகள்

**விளக்கம்:** AI உதவியாளர் கடைபிடிக்கும் கருவிகள் மற்றும் சேவைகளுக்கு அச்சுறுத்தல்படுத்தும் பிழைகள் காரணமாக மற்ற அமைப்புகளும் தோல்வி அடையலாம், இதனால் தாக்குதல் பரவலாகி எதிர்கொள்ளும் சிக்கல் அதிகமாகும்.

**தடுக்கல்:** AI உதவியாளரை ஒரு குறைந்த பரப்பில் இயக்குவது உதவும், உதாரணமாக டாக்கர் கன்டெய்னரில் பணி செய்கிறதுபோல், நேரடி அமைப்பு தாக்கங்களைத் தடுக்கும். சில அமைப்புகள் பிழையுடன் பதிலளித்தால் மீண்டும் முயற்சிக்கும் மற்றும் ரீதிருப்பு தொழில்நுட்பங்கள் கூட பெரிய அமைப்பு தோல்வியைத் தடுக்கும்.

## மனிதர்-இல்-லூப்

நம்பிக்கையுடைந்த AI உதவியாளர் அமைப்புகளை உருவாக்க மற்றொரு பயனுள்ள வழி மனிதர்-இன்-தி-லூப் பயன்படுத்துதல். இது ஓர் ஓட்டத்தின் போது பயனர்களுக்கு உதவியாளர்களுக்கு கருத்து தெரிவித்தல் வாயிலாக உதவுகிறது. பயனர்கள் பல உதவியாளர் அமைப்பில் உதவியாளர்களின் பங்கு வகித்து இயங்கும் செயல்முறையை நிறுத்த அல்லது ஒப்புக்கும்.

![மனிதர் இந்த் தி லூப்](../../../translated_images/ta/human-in-the-loop.5f0068a678f62f4f.webp)

இந்தக் கருத்து எவ்வாறு செயல்படுத்தப்படுகிறது என்பது காட்டும் Microsoft Agent Framework பயன்படுத்திய ஒரு குறியீட்டு துணுக்கை இங்கே காணவும்:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# மனிதர் இணைந்த ஒப்புதலுடன் வழங்குநரை உருவாக்கவும்
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# மனிதர் ஒப்புதல் கட்டத்தில் செயலாளரை உருவாக்கவும்
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# பயனர் பதிலை பரிசீலித்து ஒப்புக்கொள்ளலாம்
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## முடிவு

நம்பிக்கையுடைந்த AI உதவியாளர்களை உருவாக்க மிகவும் கவனமான வடிவமைப்பு, வலுவான பாதுகாப்பு நடவடிக்கைகள் மற்றும் தொடர்ந்த திருத்தம் தேவை. கட்டமைப்பு மேட்டா புரொம்ப்டிங் அமைப்புகளை நடைமுறைப்படுத்தல், சாத்தியமான அபாயங்களைப் புரிந்து கொள்ளல் மற்றும் தடுக்கும் முறைகளைப் பயன்படுத்தல், மேம்பாட்டாளர்கள் பாதுகாப்புள்ள மற்றும் விளைவான AI உதவியாளர்களை உருவாக்க முடியும். மேலும, மனிதர்-இன்-தி-லூப் முறையை இணைத்தல் AI உதவியாளர்கள் பயனர் தேவைகளுடன் ஒத்துழைத்து அபாயங்களை குறைக்கும். AI வளர்ச்சியில் பாதுகாப்பு, தனியுரிமை மற்றும் நெறிமுறை பரிந்துரைகளை முன்னிலையில் வைத்திருப்பது நம்பிக்கை மற்றும் நம்பிக்கையுடனான AI அமைப்புகளுக்கு முக்கியமாகும்.

### நம்பிக்கையுடைந்த AI தயாரிப்பாளர்கள் உருவாக்குவது பற்றி மேலும் கேள்விகள் உள்ளதா?

பிற கற்றலாளர்களுடன் சந்திக்க, அலுவலக நேரத்தில் கலந்துகொள்ள மற்றும் உங்கள் AI உதவியாளர் கேள்விகளுக்கு பதில் பெற [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) சேரவும்.

## கூடுதல் வளங்கள்

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">பொறுப்பான AI மேற்பார்வை</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">உருவாக்கும் AI மாதிரிகள் மற்றும் AI பயன்பாடுகளின் மதிப்பீடு</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">பாதுகாப்பு சிஸ்டம் செய்திகள்</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ஆபத்து மதிப்பீடு மாதிரி</a>

## முந்தைய பாடம்

[Agentic RAG](../05-agentic-rag/README.md)

## அடுத்த பாடம்

[பதிவு வடிவமைப்பு மாதிரி](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**உறுதிப்புரை**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற செயற்கை நுண்ணறிவு மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்ற போதும், இயந்திர மொழிபெயர்ப்புகளில் தவறுகள் அல்லது பிழைகள் இருக்கலாம் என்பதை நினைவில் கொள்ளுங்கள். இயல்பான மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வமான ஆதாரமாகக் கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, திறமையான மனித மொழிபெயர்ப்பர் மூலம் மொழிபெயர்ப்பு செய்ய பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பை பயன்படுத்துவதிலிருந்து ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பாக இருக்க மாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->