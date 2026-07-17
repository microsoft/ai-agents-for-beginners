[![വിശ്വസനീയമായ AI ഏജന്റുമാർ](../../../translated_images/ml/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളിൽ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്യുക)_

# വിശ്വസനീയമായ AI ഏജന്റുമാർ നിർമ്മിക്കൽ

## പരിചയം

ഈ പാഠത്തിൽ ഉൾപ്പെടുന്നത്:

- എങ്ങനെ സുരക്ഷിതവും ഫലപ്രദവുമായ AI ഏജന്റുമാർ നിർമ്മിച്ച് വിനിയോഗിക്കാമെന്ന്
- AI ഏജന്റുമാർ ഉണ്ടാക്കുമ്പോൾ ശ്രദ്ധിക്കേണ്ട പ്രധാന സുരക്ഷാമാനങ്ങൾ.
- AI ഏജന്റുമാർ വികസിപ്പിക്കുമ്പോൾ ഡാറ്റയും ഉപയോക്തൃ സ്വകാര്യതയും എങ്ങനെ പരിപാലിക്കാമെന്ന്.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം നമുക്ക് പൂർത്തിയാക്കി കഴിഞ്ഞാൽ നിങ്ങൾക്ക് അറിയാം:

- AI ഏജന്റുമാർ സൃഷ്ടിക്കുമ്പോൾ അപകടസാധ്യതകൾ തിരിച്ചറിയാനും പരിഹരിക്കാനും.
- ഡാറ്റയും ആക്സസും ശരിയായി കൈകാര്യം ചെയ്യാൻ സുരക്ഷാ നടപടികൾ നടപ്പിലാക്കാനും.
- ഡാറ്റ സ്വകാര്യത പാലിക്കുകയും ഗുണമേന്മയുള്ള ഉപഭോക്തൃ അനുഭവം നൽകുകയും ചെയ്യുന്ന AI ഏജന്റുമാർ നിർമ്മിക്കാനും.

## സുരക്ഷ

ആദ്യം സുരക്ഷിതമായ ഏജന്റിക് അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാം. സുരക്ഷ എന്നത് AI ഏജന്റ് രൂപകൽപ്പന പ്രകാരം പ്രവർത്തിക്കുന്നതാണ്. ഏജന്റിക് അപ്ലിക്കേഷനുകളുടെ നിർമ്മാതാക്കളായി, സുരക്ഷ പരമാവധി ഉറപ്പാക്കാൻ നമ്മുടെ കൈമുറകൾക്കും ഉപകരണങ്ങൾക്കും മാർഗ്ഗങ്ങൾ ഉണ്ട്:

### സിസ്റ്റം സന്ദേശം ഘടന ശിൽപ്പം

വലിയ ഭാഷാ മോഡലുകൾ (LLMs) ഉപയോഗിച്ച് AI അപ്ലിക്കേഷൻ നിങ്ങൾ നിർമ്മിച്ചതാണെങ്കിൽ, മികവുറ്റ സിസ്റ്റം പ്രോംപ്‌റ് അല്ലെങ്കിൽ സിസ്റ്റം സന്ദേശം രൂപകൽപ്പനയുടെ അനിവാര്യത നിങ്ങൾക്ക് അറിയാം. ഈ പ്രോംപ്‌റുകൾ LLM ഉപയോക്താവിനും ഡാറ്റയ്ക്കുമായുള്ള ഇടപെടലിൽ സ്വീകരിക്കുന്ന മെറ്റാ നിയമങ്ങളും നിർദ്ദേശങ്ങളും മാർഗനിർദേശങ്ങളും സ്ഥാപിക്കുന്നു.

AI ഏജന്റുകൾക്കായി സിസ്റ്റം പ്രോംപ്‌റ് കൂടുതൽ പ്രധാനമാണ്, കാരണം നിർദ്ദേശിച്ച പ്രവർത്തനങ്ങൾ പൂർത്തിയാക്കാൻ ഏറെ പ്രത്യേകമായ നിർദ്ദേശങ്ങൾ AI ഏജന്റുകൾക്ക് വേണം.

സ്കേലബിള്‍ സിസ്റ്റം പ്രോംപ്‌റുകൾ സൃഷ്ടിക്കാൻ, അപ്ലിക്കേഷനിലെ ഒരു അല്ലെങ്കിൽ കൂടി ഏജന്റുകൾക്കായി സിസ്റ്റം സന്ദേശ ഘടന ഉപയോഗിക്കാം:

![സിസ്റ്റം സന്ദേശ ഘടന നിർമ്മിക്കൽ](../../../translated_images/ml/system-message-framework.3a97368c92d11d68.webp)

#### ഘട്ട് 1: ഒരു മെറ്റാ സിസ്റ്റം സന്ദേശം സൃഷ്ടിക്കുക

മെറ്റാ പ്രോംപ്‌റ് LLM ഉപയോഗിച്ച് ഏജന്റുകൾക്കായുള്ള സിസ്റ്റം പ്രോംപ്‌റുകൾ സൃഷ്ടിക്കാൻ ഉപയോക്തൃ രൂപത്തിലുള്ളതാണ്. ഓരോ ഏജന്റും കാര്യക്ഷമമായി സൃഷ്ടിക്കാനായി ഞങ്ങൾ ഇത് ഒരു ടെംപ്ലേറ്റായി രൂപീകരിക്കുന്നു.

LLM-ന് നാം നൽകുന്ന ഒരു മെറ്റാ സിസ്റ്റം സന്ദേശത്തിനുള്ള ഉദാഹരണം ഇവിടെ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ഘട്ട് 2: ഒരു അടിസ്ഥാന പ്രോംപ്‌ര്‍ സൃഷ്ടിക്കുക

അടുത്ത ഘട്ടം AI ഏജന്റിനെ വിവരിക്കാൻ ഒരു അടിസ്ഥാന പ്രോംപ്‌ർ സൃഷ്ടിക്കുകയാണ്. ഏജന്റിന്റെ പദവി, പൂർത്തിയാക്കേണ്ട ദൗത്യങ്ങൾ, മറ്റ് ഉത്തരവാദിത്വങ്ങൾ ഉൾപ്പെടുത്തണം.

ഒരു ഉദാഹരണം:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ഘട്ട് 3: അടിസ്ഥാന സിസ്റ്റം സന്ദേശം LLM-ന് നൽകുക

ഇനി മെറ്റാ സിസ്റ്റം സന്ദേശവും അടിസ്ഥാന സിസ്റ്റം സന്ദേശവും നൽകിയാണ് ഈ സാങ്കേതിക സന്ദേശം മെച്ചപ്പെടുത്തുന്നത്.

ഇതിലൂടെ നമ്മുടെ AI ഏജന്റുമാരെ നയിക്കുന്നതിനായി മെച്ചപ്പെട്ട സിസ്റ്റം സന്ദേശം ലഭിക്കും:

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

#### ഘട്ട് 4: പുനരാലോചനയും മെച്ചപ്പെടുത്തലും

ഈ സിസ്റ്റം സന്ദേശ ഘടനയുടെ മൂല്യം പല ഏജന്റുമാരുടെ സിസ്റ്റം സന്ദേശങ്ങൾ സകലം സൃഷ്ടിക്കുന്നത് സുഗമമാക്കുകയും, താങ്കളുടെ സന്ദേശങ്ങൾ സമയക്രമത്തിൽ മെച്ചപ്പെടുത്തുകയും ചെയ്യുന്നതിലാണ്. നിങ്ങളുടെ സംപ്രേഷണം ആദ്യത്തവണ മുഴുവനായി ശരിയായതായി പ്രവർത്തിക്കുന്നത് അപൂർവം. അടിസ്ഥാന സന്ദേശം ചെറിയ ഭേദഗതികൾ വരുത്തി പ്രവർത്തനം പരിശോധിച്ച് ഫലങ്ങൾ വിലയിരുത്താനാകും.

## ഭീഷണികൾ മനസിലാക്കൽ

വിശ്വസനീയമായ AI ഏജന്റുമാർ നിർമ്മിക്കാൻ, നിങ്ങളുടെ AI ഏജന്റിന്റെ അപകടങ്ങളും ഭീഷണികളും മനസ്സിലാക്കി നിയന്ത്രിക്കൽ അത്യന്താപേക്ഷിതമാണ്. AI ഏജന്റുമാരെ നേരിടുന്ന ചില ഭീഷണികൾ മാത്രമേ ഇവിടെ കാണിക്കുകയുള്ളുവെങ്കിലും അവയ്ക്ക് എങ്ങനെ ടീംബദ്ധമായി ഒരുക്കപ്പെടാമെന്ന് നോക്കാം.

![ഭീഷണികൾ മനസിലാക്കൽ](../../../translated_images/ml/understanding-threats.89edeada8a97fc0f.webp)

### ദൗത്യംയും നിർദേശവും

**വിവരണം:** ആക്രമകർ പ്രോപംപ്‌റുകൾ ധൂതീകരിച്ച് അല്ലെങ്കിൽ ഇൻപുട്ടുകൾ നിയന്ത്രിച്ച് AI ഏജന്റെ സ്വഭാവം അല്ലെങ്കിൽ ലക്ഷ്യങ്ങൾ മാറ്റാൻ ശ്രമിക്കുന്നു.

**പരിഹാരം**: അപകടകാരിയായ പ്രോംപ്‌റുകൾ AI ഏജന്റ് ഗതാഗതത്തിലേക്ക് എത്തുന്നതിന് മുമ്പായി സജീവമായ പരിശോധനകളും ഇൻപുട്ട് ഫിൽട്ടറുകളും നടപ്പിലാക്കുക. ഈ ആക്രമണങ്ങൾക്ക് സാധാരണയായി ഏജന്റുമായി സ്ഥിരമായ ആശയവിനിമയം വേണം, അതുകൊണ്ട് സംഭാഷണത്തിന്റെ ടേണുകളുടെ എണ്ണം പരിമിതപ്പെടുത്തലും മറ്റൊരു തടസ്സമാണ്.

### നിർണായക സംവിധാനങ്ങൾക്ക് ആക്സസ്

**വിവരണം**: AI ഏജന്റിന് സങ്കീർണ്ണ ഡാറ്റ സംഭരിക്കുന്ന സംവിധാനങ്ങളിലും സേവനങ്ങളിലും ആക്സസ് ഉണ്ടായാൽ, ആക്രമകർ ഏജന്റുമായി ഈ സേവനങ്ങൾ തമ്മിലുള്ള ആശയവിനിമയം മൂടിക്കൊണ്ട് ആക്രമിക്കാം. നേരിട്ട് അല്ലെങ്കിൽ ഏജന്റുടെ വഴി ഈ സമ്പർക്കത്തെക്കുറിച്ച് വിവരങ്ങൾ നേടാൻ ശ്രമിച്ചുകൊണ്ടേയുമാകാം.

**പരിഹാരം**: ആക്സസ്സ് ആവശ്യമായ ഓൺലി അടിസ്ഥാനത്തിൽ AI ഏജന്റുകൾക്ക് നൽകണമെന്നും, ഏജന്റും സംവിധാനവും തമ്മിലുള്ള ആശയവിനിമയം സുരക്ഷിതമാക്കണമെന്നും നിർബന്ധം. അംഗീകാരം, ആക്സസ് നിയന്ത്രണം നടപ്പിലാക്കുന്നതും സുരക്ഷാ സംരക്ഷണം നൽകി സഹായിക്കും.

### സാധനങ്ങളും സേവനങ്ങളും അധികഭാരം

**വിവരണം:** AI ഏജന്റുകൾ ദൗത്യം പൂർത്തിയാക്കാനായി വിവിധ സേവനങ്ങളും ഉപകരണങ്ങളും ആക്സസ് ചെയ്യാൻ കഴിയുന്നു. ആക്രമകർ ഈ കഴിവ് ഉപയോഗിച്ച് AI ഏജന്റിലൂടെ ഉയർന്ന ഹ്രസ്വവാറുള്ള അഭ്യർത്ഥനകൾ അയച്ച് ഈ സേവനങ്ങൾ ആക്രമിച്ചീടാൻ കഴിയും, ഇത് സംവിധാനം തകരുന്നതിലേക്ക് അല്ലെങ്കിൽ വലിയ ചെലവിലേക്ക് നയിക്കാം.

**പരിഹാരം:** ഒരു AI ഏജന്റ് ഒരു സേവനത്തിന് അയയ്‌ക്കാവുന്ന അഭ്യർത്ഥനകളുടെ എണ്ണം നിയന്ത്രിക്കുന്ന നയങ്ങൾ നടപ്പിലാക്കുക. സംഭാഷണ ടേണുകളുടെ എണ്ണവും AI ഏജന്റിനോടുള്ള അഭ്യർത്ഥനകളുടെ എണ്ണം പരിധി വയ്ക്കുന്നു എന്നതും ഈ ആക്രമണങ്ങൾ തടയാനുണ്ടാകാം.

### നോളജ് ബേസ് വിഷപരിഹാരം

**വിവരണം:** ഈ തരത്തിലുള്ള ആക്രമണം നേരിട്ട് AI ഏജന്റിനെ ലക്ഷ്യമിട്ട് അല്ല, പകരം AI ഏജന്റ് ഉപയോഗിക്കുന്ന നോളജ് ബേസ്, മറ്റ് സേവനങ്ങളും ലക്ഷ്യമിടുന്നു. ഡാറ്റ കൃത്യം അല്ലാതെയാക്കൽ, തെറ്റായ/അപ്രതീക്ഷിത പ്രതികരണങ്ങൾ ഉണ്ടാക്കുക എന്നതാണ് ലക്ഷ്യം.

**പരിഹാരം:** AI ഏജന്റ് workflow-കളിൽ ഉപയോഗിക്കുന്ന ഡാറ്റയുടെ സ്ഥിരം സ്ഥിരീകരണം നടത്തണം. ഈ ഡാറ്റ സുരക്ഷിതമായ ആക്‌സസ്സ് മാത്രം അവകാശിക്കുന്നത് ഉറപ്പാക്കേണ്ടത് ഈ തരത്തിലുള്ള ആക്രമണങ്ങൾ തടയാൻ സഹായിക്കും.

### കസ്ക്കേഡിംഗ് എറേഴ്‌സ് (തെറ്റുകളുടെ ഇത് ഒന്ന് വേറെത്തലിൽ പ്രഭാഷണം)

**വിവരണം:** AI ഏജന്റുകൾ പല ഉപകരണങ്ങളും സേവനങ്ങളും ഉപയോഗിച്ച് ദൗത്യം പൂർത്തിയാക്കുന്നു. ആക്രമകർസൃഷ്ടിച്ച പിഴവുകൾ മറ്റ് ബന്ധപ്പെടുന്ന സംവിധാനങ്ങളിലും പരാജയം സൃഷ്ടിക്കുകയും, ആക്രമണം വ്യാപകമാകുകയും, പരിഹരിക്കാൻ ബുദ്ധിമുട്ട് ഉണ്ടാക്കുകയും ചെയ്യും.

**പരിഹാരം**: ഇതു തടയാനുള്ള ഒരു മാർഗം, AI ഏജന്റിനെ ഒരു പരിധിയുള്ള അന്തരീക്ഷത്തിൽ പ്രവർത്തിക്കാനായി Docker കൺറ്റെയിനർ പോലുള്ളവയിൽ പ്രവർത്തിപ്പിക്കുക, നേരിട്ടുള്ള സംവിധാന ആക്രമണങ്ങൾ തടയാൻ. പിഴവുള്ള സേവനങ്ങൾക്ക് പകരം മെക്കാനിസങ്ങളും പുന:ശ്രമ തന്ത്രങ്ങളും സൃഷ്ടിക്കുന്നത് വലിയ പരാജയങ്ങൾ തടയും.

## മനുഷ്യൻ ലൂപ്പിൽ (Human-in-the-Loop)

വിശ്വസനീയമായ AI ഏജന്റ് സംവിധാനങ്ങൾ നിർമ്മിക്കാൻ മറ്റൊരു ഫലപ്രദമായ മാർഗം മനുഷ്യനെയുള്ള ലൂപ്പ് ഉൾപ്പെടുത്തലാണ്. ഇത് ഒരു പ്രവാഹം സൃഷ്ടിക്കുന്നു, ഉപയോഗക്കാർ റൺ സമയത്ത് ഏജന്റുമാരെ ഫീഡ്ബാക്ക് നൽകാൻ കഴിയും. ഉപയോക്താക്കൾ മൾട്ടി-ഏജന്റ് സിസ്റ്റം വഴി ഏജന്റുമാരായി പ്രവർത്തിച്ച് പ്രവർത്തനം അംഗീകരിക്കുകയോ അവസാനിപ്പിക്കുകയോ ചെയ്യുന്നു.

![ലൂപ്പിലെ മനുഷ്യൻ](../../../translated_images/ml/human-in-the-loop.5f0068a678f62f4f.webp)

ഇത് എങ്ങനെ നടപ്പിലാക്കുന്നുവെന്ന് Microsoft Agent Framework ഉപയോഗിച്ച് ഒരു കോഡ് ഉദാഹരണമുണ്ട്:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# മനുഷ്യനു-ഇടപെടലുള്ള അംഗീകാരം ഉപയോഗിച്ച് പ്രൊവൈഡർ സൃഷ്ടിക്കുക
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# മനുഷ്യ അംഗീകരണഘട്ടത്തോടെ ഏജൻറ് സൃഷ്ടിക്കുക
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ഉപയോക്താവ് പ്രതികരണം പരിശോധിച്ച് അംഗീകരിക്കാം
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## സമാപനം

വിശ്വസനീയമായ AI ഏജന്റുമാർ നിർമ്മിക്കാൻ സൂക്ഷ്മമായ രൂപകൽപ്പന, ശക്തമായ സുരക്ഷാ മാർഗ്ഗരേഖകൾ, തുടർച്ചയായ പുനരാലോചന എന്നിവ ആവശ്യമാണ്. ഘടക മെറ്റാ പ്രോംപ്‌റുകൾ നടപ്പിലാക്കുകയും, സാധ്യതയുള്ള ഭീഷണികൾ മനസ്സിലാക്കി പരിഹാര തന്ത്രങ്ങൾ പ്രയോഗിക്കുകയും ചെയ്താൽ, സുരക്ഷിതവും ഫലപ്രദവും ആയ AI ഏജന്റുമാർ നിർമ്മിക്കാം. കൂടാതെ, മനുഷ്യൻ ലൂപ്പിൽ ഉൾപ്പെടുത്തൽ ഉപയോക്തൃ ആവശ്യങ്ങൾക്കനുസരിച്ച് ഏജന്റുമാരെ കൂട്ടിച്ചേർക്കുകയും അപകടങ്ങൾ കുറയ്ക്കുകയും ചെയ്യും. AI വികസിച്ചതിനൊപ്പം സുരക്ഷ, സ്വകാര്യത, നൈതികത എന്നിവയിൽ മുന്നേറ്റം ഉറപ്പുനൽകുന്നത് വിശ്വാസവും വിശ്വസനീയതയും വളർത്തുന്ന ഒരു പ്രധാന ഘടകമായിരിക്കും.

## കോഡ് സാമ്പിളുകൾ

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): മെറ്റാ-പ്രോംപ്‌റ് സിസ്റ്റം-സന്ദേശ ഘടനയുടെ ഘട്ടം ഘട്ടമായ ദൃശ്യീകരണം.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): വിശ്വസനീയ ഏജന്റുമാർക്കുള്ള മുൻ പ്രവർത്തന അംഗീകാരം, അപകട നിരൂപണം, ഓഡിറ്റ് ലോഗിംഗ്.

### വിശ്വസനീയ AI ഏജന്റുമാർ നിർമ്മിക്കുന്നതിനെക്കുറിച്ച് കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

പഠനാർത്ഥികളുമായി ബന്ധപ്പെടുന്നതിന്, ഓഫീസ് മണിക്കൂറുകൾക്ക് ഹാജരാകാനായി, നിങ്ങളുടെ AI ഏജന്റ് ചോദ്യങ്ങൾക്ക് ഉത്തരം ലഭിക്കാനായി [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)-ൽ ചേരുക.

## അധിക რესോഴ്‌സുകൾ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ഉത്തരംവഹിക്കുന്ന AI അവലോകനം</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ജനന AI മോഡലുകളും AI അപ്ലിക്കേഷനുകളും വിലയിരുത്തൽ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">സുരക്ഷാ സിസ്റ്റം സന്ദേശങ്ങൾ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">അപേക്ഷാ അപകടം വിലയിരുത്തൽ Teamplate</a>

## മുൻ പാഠം

[Agentic RAG](../05-agentic-rag/README.md)

## അടുത്ത പാഠം

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->