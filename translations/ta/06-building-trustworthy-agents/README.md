[![நம்பகமான AI முகவர்கள்](../../../translated_images/ta/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(இந்த பாடத்தின் வீடியோ பார்க்க மேலே உள்ள படம் கிளிக் செய்யவும்)_

# நம்பகமான AI முகவர்களை உருவாக்குதல்

## வரவேற்பு

இந்த பாடத்தில் சேர்க்கப்படும் விஷயங்கள்:

- பாதுகாப்பான மற்றும் விளைவான AI முகவர்களை எப்படி உருவாக்கி பயன்படுத்துவது
- AI முகவர்களை உருவாக்கும் பொழுது முக்கியமான பாதுகாப்பு பரிசீலனைகள்
- AI முகவர்களை உருவாக்கும் பொழுது தரவு மற்றும் பயனர் தனியுரிமையை எப்படி பராமரிப்பது

## கற்றல் இலக்குகள்

இந்த பாடத்தை முடித்த பிறகு, நீங்கள் அறிவீர்கள் எப்படி:

- AI முகவர்களை உருவாக்கும்போது அபாயங்களையும் ஆபத்துகளையும் அடையாளம் காண்ந்து குறைக்கும்.
- தரவு மற்றும் அணுகலை சரியாக நிர்வகிப்பதற்கான பாதுகாப்பு நடவடிக்கைகளை அமல்படுத்துவது.
- தரவு தனியுரிமையை பராமரிக்கும் மற்றும் தரமான பயனர் அனுபவம் வழங்கும் AI முகவர்களை உருவாக்குவது.

## பாதுகாப்பு

முதலில் பாதுகாப்பான முகவரிச் செயலிகளைக் கட்டமைப்போம். பாதுகாப்பு என்பது AI முகவர் திட்டமிட்டபடி செயல்பட வேண்டும் என்பதைக் குறிக்கிறது. முகவரிச் செயலிகளின் கட்டிடர்கள் ஆக நாம் அதிகபட்ச பாதுகாப்புக்கான முறைகள் மற்றும் கருவிகள் உள்ளன:

### ஒரு அமைப்பு செய்தி அமைப்பை உருவாக்குதல்

பெரிய மொழி மாதிரிகள் (LLMs) பயன்படுத்தி AI பயன்பாடுகளை உருவாக்கி இருந்தால், ஒரு வலுவான அமைப்பு தூண்டுகோல் அல்லது அமைப்பு செய்தியின் முக்கியத்துவத்தை நீங்கள் அறிந்திருப்பீர்கள். இந்த தூண்டுகோல்கள் LLM பயனர் மற்றும் தரவுடன் எப்படி பணியாற்ற வேண்டும் என்பதற்கான விதிமுறைகள் மற்றும் வழிகாட்டுதல்களை அமைக்கின்றன.

AI முகவர்களுக்கு, அமைப்பு தூண்டுகோல் மிகவும் முக்கியமானது, ஏனெனில் AI முகவர்கள் நாம் வடிவமைத்த பணிகளை முடிக்க மிகவும் தெளிவான வழிமுறைகள் வேண்டும்.

பரவலாக அமைப்பு தூண்டுகோல்களை உருவாக்க, நாம் ஒரு செயலியில் ஒரு அல்லது பல முகவர்களை கட்டமைக்க அமைப்பு செய்தி அமைப்பைப் பயன்படுத்தலாம்:

![ஒரு அமைப்பு செய்தி அமைப்பை உருவாக்குதல்](../../../translated_images/ta/system-message-framework.3a97368c92d11d68.webp)

#### படி 1: ஒரு மேட்டா அமைப்பு செய்தியை உருவாக்குதல்

மேட்டா தூண்டுகோல் LLM க்கு நமக்கு உருவாக்கும் முகவரிகளுக்கான அமைப்பு தூண்டுகோல்களை உருவாக்க பயன்படுத்தப்படும். தேவையானபட்சம் பல முகவர்களை துரிதமாக உருவாக்க ஒரு முன்மாதிரியாக இதை வடிவமைக்கும்.

இதோ LLM க்கு வழங்குவதற்கான ஒரு மேட்டா அமைப்பு செய்தியின் எடுத்துக்காட்டு:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### படி 2: அடிப்படை தூண்டுகோலை உருவாக்குதல்

அடுத்த படி AI முகவரைக் குறிக்கும் அடிப்படை தூண்டுகோலை உருவாக்குதல். இதில் முகவரின் பங்கு, முகவர் முடிப்பவுள்ள பணிகள் மற்றும் பிற பொறுப்புகளை சேர்க்க வேண்டும்.

இதோ எடுத்துக்காட்டு:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### படி 3: அடிப்படை அமைப்பு செய்தியைக் LLM க்கு வழங்குதல்

இப்போது மேட்டா அமைப்பு செய்தியைச் சொல்லி நாம் இந்த அமைப்பு செய்தியை மேம்படுத்தலாம்.

இது நமது AI முகவர்களை வழிநடத்த சிறந்த வடிவமைக்கப்பட்ட அமைப்பு செய்தியைக் உருவாக்கும்:

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

#### படி 4: மீண்டும் முயற்சி செய்து மேம்படுத்தல்

இந்த அமைப்பு செய்தி அமைப்பின் மதிப்பு பல முகவர்களுக்கான அமைப்பு செய்திகளை எளிதாக உருவாக்கவும், உங்கள் அமைப்பு செய்திகளை காலப்போக்கில் மேம்படுத்தவும் உதவுகிறது. முதன்முறை பயன்படுத்தும் போது உங்கள் முழுமையான பயன்பாட்டிற்கு ஏற்ற அமைப்பு செய்தி அரிதாகவே இருக்கும். சிறிய திருத்தங்களை செய்து, அடிப்படை அமைப்பு செய்தியை மாற்றி, அதை மீண்டும் இயக்கி உங்கள் முடிவுகளை ஒப்பிடவும் மூலமாக மேம்படுத்தலாம்.

## ஆபத்துக்களை புரிதல்

நம்பகத்தன்மை வாய்ந்த AI முகவர்களை கட்டமைப்பதற்கு, உங்கள் AI முகவருக்கு உள்ள அபாயங்கள் மற்றும் ஆபத்துக்களை புரிந்து, குறைக்க வேண்டும். AI முகவர்களுக்கு உள்ள சில ஆபத்துக்கள் மற்றும் அவற்றுக்கு நீங்கள் எவ்வாறு சிறந்த திட்டமிடல் மற்றும் தயாரிப்புகளை செய்யலாம் என்று பார்ப்போம்.

![ஆபத்துக்களை புரிதல்](../../../translated_images/ta/understanding-threats.89edeada8a97fc0f.webp)

### பணிகள் மற்றும் வழிமுறைகள்

**விபரம்:** தாக்குதல்காரர்கள் AI முகவரின் வழிமுறைகள் அல்லது இலக்குகளை தூண்டுதல்களோ அல்லது உள்ளீடுகளை மாற்றுவதோ முயலுகிறார்கள்.

**செயல் திட்டம்:** செயல்முறை சரிபார்ப்பு மற்றும் உள்ளீடு வடிகட்டிகள் மூலம் ஆபத்தான தூண்டுதல்களை AI முகவர் செயலாக்கம்காணும் முன் கண்டறிய வேண்டும். இந்தத் தாக்குதல்களுக்கு அடிக்கடி AI முகவருடன் தொடர்பு வேண்டும் என்பதால் உரையாடல் முறை எண்ணிக்கையைக் குறைப்பதும் மற்றொரு தடுப்பு முறையாகும்.

### முக்கிய அமைப்புகளுக்கு அணுகல்

**விபரம்:** AI முகவர் حساس தரவு சேமிக்கும் அமைப்புகள் மற்றும் சேவைகளுக்கு அணுகல் இருந்தால், தாக்குதல்காரர்கள் முகவர் மற்றும் சேவைகளுக்கு இடையேயான தொடர்பை குறைகடத்தலாம். இவை நேரடி தாக்குதல்கள் அல்லது முகவரின் மூலம் அந்த அமைப்புக்கள் பற்றி தகவல் பெறும் முறைகள் ஆக இருக்கலாம்.

**செயல் திட்டம்:** AI முகவர்களுக்கு தேவையான அளவுக்கு மட்டுமே அமைப்புக்களை அணுக அனுமதிக்க வேண்டும். முகவர் மற்றும் அமைப்புக்கிடையிலான தொடர்பு பாதுகாப்பானதாக இருக்க வேண்டும். அங்கீகரிப்பு மற்றும் அணுகல் கட்டுப்பாட்டை அமல்படுத்துவது இன்னும் ஒரு பாதுகாப்பு உத்தி.

### வளங்கள் மற்றும் சேவைகளை அடிமைப்படுத்தல்

**விபரம்:** AI முகவர்கள் பணிகளை முடிக்க பல கருவிகள் மற்றும் சேவைகளை அணுகலாம். தாக்குதல்காரர்கள் AI முகவரின் மூலம் அதிக ஆதரவு வேண்டுகோள்களை அனுப்பி இந்த சேவைகளை தாக்கலாம். இது அமைப்பு தவறுகள் அல்லது உயர்ந்த செலவுகளுக்கு காரணமாகும்.

**செயல் திட்டம்:** AI முகவர்கள் சேவைகளுக்கு அனுப்பும் கோரிக்கைகளின் எண்ணிக்கையை வரையறுக்கும் விதிமுறைகளை அமல்படுத்தவும். உரையாடல் முறையின் திருப்புகளின் எண்ணிக்கையையும் AI முகவருக்கு அனுப்பும் கோரிக்கைகளையும் கட்டுப்படுத்துவது இதற்கான மற்றொரு முறையாகும்.

### அறிவுக் கூற்றுக்களின் விஷமப்படுத்தல்

**விபரம்:** இந்த தாக்குதல் நேரடியாக AI முகவருக்கே அல்ல, ஆனால் AI முகவர் பயன்படுத்தும் அறிவுக் கூற்றுக்கள் மற்றும் பிற சேவைகள் மீது நோக்கமிடுகிறது. இது தரவு மோசடியாக்கப்படல் அல்லது தவறான பதில்களுக்கான காரணமாக பயன்படும்.

**செயல் திட்டம்:** AI முகவர் வேலையில் பயன்படுத்தும் தரவுகளை தவறற்ற பயனிற்காக அடிக்கடி சரிபார்க்கவும். இந்த தரவுக்கு அணுகல் நம்பகமான நபர்களால் மட்டுமே மாற்றப்பட வேண்டும் என்பதற்கான பாதுகாப்புகள் இருக்க வேண்டும்.

### தொடர் பிழைகள்

**விபரம்:** AI முகவர்கள் பல கருவிகள் மற்றும் சேவைகளை அணுகிப் பணிகளை முடிக்கின்றனர். தாக்குதல்களால் ஏற்படும் பிழைகள் மற்ற அமைப்புகளிலும் தோல்விகளை ஏற்படுத்துகிறது, இதனால் தாக்குதல் பரவலாகி, சிக்கலை அதிகரிக்கிறது.

**செயல் திட்டம்:** இதைத் தவிர்க்க AI முகவரைக் கட்டுப்படுத்தப்பட்ட சூழலில் இயங்கச்செய்தல், உதாரணமாக டாக்கர் கொண்டெய்னர் போன்றது ஒரு வழி. சில அமைப்புகள் பிழை சொன்னால் பின்னணி பாதுகாப்பு முறைகள் மற்றும் மீண்டும் முயற்சி செய்யும் நடைமுறைகளை உருவாக்குதல் பெரிய தோல்விகளை தவிர்க்கிறது.

## மனிதர் பங்கு

நம்பகமான AI முகவர் அமைப்புகளைக் கட்டமைப்பதற்கான இன்னொரு பயனுள்ள வழி மனிதர் பங்கு கொண்டதாக இருக்கிறது. இதனால் பயனர்கள் இயங்கும் போது முகவர்களுக்கு பின்னூட்டம் அளிக்க முடியும். பயனர்கள் பல முகவர் அமைப்பில் முகவர்களாக செயல்பட்டு செயல்முறையை அங்கீகரிப்பது அல்லது நிறுத்துவது ஆகியவற்றை செய்யலாம்.

![மனிதர் பங்கு கொண்டது](../../../translated_images/ta/human-in-the-loop.5f0068a678f62f4f.webp)

இந்த கருத்தை எவ்வாறு அமல்படுத்துகிறோம் என்பதை காட்ட மைக்ரோசாஃப்ட் முகவர் அமைப்பை பயன்படுத்தும் குறியீட்டு பகுதி:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# மனித ஒப்புதலுடன் வழங்குநரை உருவாக்கவும்
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# மனித ஒப்புதல் படியை உடைய முகவரியை உருவாக்கவும்
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# பயனர் பதிலை மதிப்பாய்வு செய்து ஒப்புக்கொள்ள முடியும்
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## முடிவு

நம்பகமான AI முகவர்களை கட்டமைப்பது முறையாக வடிவமைக்கப்படும், வலுவான பாதுகாப்பு நடவடிக்கைகள் கொண்டதும், தொடர்ந்து மேம்படுத்தும் செயல்முறைகளைக் கொண்டதுமானது. கட்டமைக்கப்பட்ட மேட்டா தூண்டுதல் அமைப்புகளைப் பயன்படுத்தி, சாத்தியமான ஆபத்துக்களை புரிந்து, குறைக்க அணுகுமுறைகளை செயல்படுத்துவதன் மூலம், பாதுகாப்பான மற்றும் விளைவான AI முகவர்களை உருவாக்க முடியும். கூடுதலாக, மனிதர் பங்கு கொண்ட முறையை இணைப்பதன் மூலம் AI முகவர்களின் பயனர் தேவைகளுடன் ஒத்திசைவில் இயங்குதலும், அபாயங்கள் குறைவாகவும் இருக்கும். AI தொடர்ந்தே மேம்படும் போது, பாதுகாப்பு, தனியுரிமை மற்றும் நெறிமுறை பரிசீலனைகளை முன்னிட்டு செயல்படுவதும் நம்பகத்தன்மையையும் நம்பகமான AI இயங்குதளத்தையும் வலுப்படுத்தும்.

## குறியீட்டு எடுத்துக்காட்டுகள்

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): மேட்டா தூண்டுதல் அமைப்பு செய்தி அமைப்பின் படிநிலையான காட்சி.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): நம்பகமான முகவர்களுக்கு முன்னாள் நடைமுறை அங்கீகாரம், ஆபத்து நிலை வகை மற்றும் ஆய்வு பதிவுகள்.

### நம்பகமான AI முகவர்களை உருவாக்குவதற்கான மேலும் கேள்விகள் உள்ளதா?

மற்ற கற்பவர்களுடன் சந்திக்க, அலுவலக நேரங்களுக்கு செல்க, மற்றும் உங்கள் AI முகவர்களுக்கு தொடர்பான கேள்விகளுக்கு பதில்கள் பெற [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)இல் சேர்ந்துகொள்ளவும்.

## கூடுதல் ஆதாரங்கள்

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">பொறுப்பான AI கண்ணோட்டம்</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">உருவாக்கும் AI மாதிரிகள் மற்றும் AI பயன்பாடுகளுக்கான மதிப்பீடு</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">பாதுகாப்பு அமைப்பு செய்திகள்</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ஆபத்து மதிப்பீட்டு மாதிரி</a>

## முந்தைய பாடம்

[Agentic RAG](../05-agentic-rag/README.md)

## அடுத்த பாடம்

[திட்டமிடல் வடிவமைப்பு முறை](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->