[![വിശ്വാസയോഗ്യമായ AI ഏജന്റുമാർ](../../../translated_images/ml/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളിൽ ചിത്രം ക്ലിക്ക് ചെയ്യുക)_

# വിശ്വാസയോഗ്യമായ AI ഏജന്റുമാരായ നിർമ്മാണം

## പരിചയം

ഈ പാഠം കവർ ചേരും:

- സുരക്ഷിതവും ഫലപ്രദവുമായ AI ഏജന്റുമാർ എങ്ങനെ നിർമ്മിക്കാനും വിന്യസിക്കാനും
- AI ഏജന്റുമാർ വികസിപ്പിക്കുമ്പോൾ പ്രധാനപ്പെട്ട സുരക്ഷാ പരിഗണനകൾ.
- AI ഏജന്റുമാർ വികസിപ്പിക്കുമ്പോൾ ഡാറ്റയും ഉപയോക്തൃ സ്വകാര്യതയും എങ്ങനെ പരിരക്ഷിക്കാമെന്ന്.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയതിന് ശേഷം, നിങ്ങൾക്ക് അറിയാം:

- AI ഏജന്റുമാർ സൃഷ്ടിക്കുമ്പോൾ അപകടങ്ങൾ തിരിച്ചറിയാനും കുറയ്ക്കാനും.
- ഡാറ്റയും ആക്സസും ശരിയായി നിയന്ത്രിക്കാൻ സുരക്ഷാ മാർഗങ്ങൾ നടപ്പിലാക്കാനും.
- ഡാറ്റ സ്വകാര്യത നിലനിൽക്കുന്ന, ഗുണനിലവാരമുള്ള ഉപയോക്തൃ അനുഭവം നൽകുന്ന AI ഏജന്റുമാരെ സൃഷ്ടിക്കാനും.

## സുരക്ഷ

സുരക്ഷിതമായ ഏജന്റ് അടിസ്ഥാനപ്രയോഗങ്ങൾ നിർമ്മിക്കുന്നതിൽ നിന്നു തുടങ്ങാം. സുരക്ഷ എന്നത് AI ഏജന്റിന്റെ രൂപകൽപ്പന പ്രകാരം പ്രവർത്തിക്കുന്നതിനെയാണ് സൂചിപ്പിക്കുന്നത്. ഏജന്റ് അടിസ്ഥാനപ്രയോഗ നിർമ്മാതാക്കൾ ആയി, സുരക്ഷ പരമാവധി ഉറപ്പാക്കുന്നതിനുള്ള മാർഗങ്ങളും ടൂളുകളും നമ്മുക്ക് ഉണ്ട്:

### ഒരു സിസ്റ്റം മെസേജ് ഫ്രെയിംവർക്കിനെ നിർമ്മിക്കൽ

നിങ്ങൾ ലഭ്യമായിടത്തോളം വലിയ ഭാഷാ മോഡലുകളായ LLMകൾ ഉപയോഗിച്ച് AI ആപ്ലിക്കേഷൻ നിർമ്മിച്ചിരിക്കുകയാണെങ്കിൽ, ശക്തമായ സിസ്റ്റം പ്രോംപ്റ്റ് അല്ലെങ്കിൽ സിസ്റ്റം മെസേജിന്റെ രൂപകൽപ്പനയുടെ പ്രാധാന്യം അറിയാം. ഈ പ്രോംപ്റ്റുകൾ മെടാ നിയമങ്ങൾ, നിർദ്ദേശങ്ങൾ, LLM ഉപയോക്താവിനും ഡാറ്റയുമായി എങ്ങിനെയാണു ഇടപഴകുക എന്നുളള മാർഗനിർദ്ദേശങ്ങൾ നിർണയിക്കുന്നു.

AI ഏജന്റുമാർക്ക്, സിസ്റ്റം പ്രോംപ്റ്റ് കൂടുതൽ പ്രധാനമാണെന്നത് കാരണം, AI ഏജന്റുമാർക്ക് നാം രൂപകൽപ്പന ചെയ്തിട്ടുള്ള കാർയ്യങ്ങൾ പൂർത്തിയാക്കാൻ വളരെ പ്രത്യേകമായ നിർദ്ദേശങ്ങൾ ആവശ്യമാണ്.

വ്യാപകമായ സിസ്റ്റം പ്രോംപ്റ്റുകൾ സൃഷ്ടിക്കാൻ, ഞങ്ങൾ നമ്മളുടെ ആപ്ലിക്കേഷനിൽ ഒരു അല്ലെങ്കിൽ കൂടുതൽ ഏജന്റുമാരെ നിർമ്മിക്കുന്നതിനുള്ള സിസ്റ്റം മെസേജ് ഫ്രെയിംവർക്കുകൾ ഉപയോഗിക്കാം:

![സിസ്റ്റം മെസേജ് ഫ്രെയിംവർക്കിനെ നിർമ്മിക്കൽ](../../../translated_images/ml/system-message-framework.3a97368c92d11d68.webp)

#### ഘട്ടം 1: ഒരു മെടാ സിസ്റ്റം മെസേജ് സൃഷ്ടിക്കുക

മെടാ പ്രോംപ്റ്റ് ഒരു LLM ഉപയോഗിച്ചാണ് ഞങ്ങൾ സൃഷ്ടിക്കുന്ന ഏജന്റുമാർക്കുള്ള സിസ്റ്റം പ്രോംപ്റ്റുകൾ നിർമ്മിക്കാൻ ഉപയോഗിക്കുന്നത്. ഇത് ഒരു ടെംപ്ലേറ്റായി രൂപകൽപ്പന ചെയ്യുന്നു, അതിനാൽ ആവശ്യമുള്ള പക്ഷം നിരവധി ഏജന്റുമാർ എളുപ്പത്തിൽ സൃഷ്ടിക്കാനാകും.

ഇവിടെയാണ് LLM ന് നൽകുന്ന മെടാ സിസ്റ്റം മെസേജിന്റെ ഒരു ഉദാഹരണം:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ഘട്ടം 2: ഒരു അടിസ്ഥാന പ്രോംപ്റ്റ് സൃഷ്ടിക്കുക

അടുത്ത ഘട്ടം AI ഏജന്റിനെ വിവരണം നൽകുന്ന ഒരു അടിസ്ഥാന പ്രോംപ്റ്റ് സൃഷ്ടിക്കുകയാണ്. ഏജന്റിന്റെ പങ്ക്, പൂർത്തിയാക്കേണ്ട കാര്യങ്ങൾ, മറ്റ് ഉത്തരവാദിത്വങ്ങൾ എന്നിവ ഇതിൽ അടങ്ങിയിരിക്കണം.

ഇതാണ് ഒരു ഉദാഹരണം:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ഘട്ടം 3: LLMനെ അടിസ്ഥാന സിസ്റ്റം മെസേജ് നൽകുക

ഇപ്പോൾ നാം ഈ സിസ്റ്റം മെസേജ് മെറ്റാ സിസ്റ്റം മെസേജായി ഉപയോഗിച്ച് നമ്മുടെ അടിസ്ഥാന സിസ്റ്റം മെസേജുമായ സംയോജിപ്പിച്ച് ഈ സിസ്റ്റം മെസേജ് മെച്ചപ്പെടുത്താം.

ഈ സിസ്റ്റം മെസേജ് നഷ്‌ടപ്പെടുത്തിയ AI ഏജന്റുമാരെ മാർഗ്ഗനിർദ്ദേശം നൽകുന്നതിനായി കുറഞ്ഞു രൂപകൽപ്പന ചെയ്തതായിരുന്നു:

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

#### ഘട്ടം 4: ആവർത്തിക്കാനും മെച്ചപ്പെടുത്താനും

ഈ സിസ്റ്റം മെസേജ് ഫ്രെയിംവർക്കിന്റെ മൂല്യം പല ഏജന്റുമാർക്കിന്റെ സിസ്റ്റം മെസേജുകളെ വേഗത്തിൽ സൃഷ്ടിക്കാനും കാലക്രമേണ നിങ്ങളുടെ സിസ്റ്റം മെസേജുകൾ മെച്ചപ്പെടുത്താനും കഴിയും എന്നതാണ്. നിങ്ങളുടെ മുഴുവൻ ഉപയോഗകേസിനും ആദ്യത്തേത് ഒരു സിസ്റ്റം മെസേജ് പ്രവർത്തിക്കുന്ന ഉളള അവസരം അപൂർവ്വമാണ്. ചെറിയ തിരുത്തലുകൾ ചെയ്ത് അടിസ്ഥാന സിസ്റ്റം മെസേജ് മാറ്റാനും അത് സിസ്റ്റത്തിലൂടെ ഓടിച്ച് ഫലങ്ങൾ ഉപയോക്തൃപത്രിക്കാൻ കഴിയും.

## ഭീഷണികളെ മനസിലാക്കൽ

വിശ്വാസയോഗ്യമായ AI ഏജന്റുമാർ നിർമ്മിക്കാൻ, നിങ്ങളുടെ AI ഏജന്റുകളിൽ ഉണ്ടാകാവുന്ന അപകടങ്ങളും ഭീഷണികളും മനസിലാക്കി അവ കുറയ്ക്കുന്നത് പ്രധാനമാണ്. AI ഏജന്റുമാർക്കുള്ള വ്യത്യസ്ത ഭീഷണികളിൽ ചിലതിനെ മാത്രം നോക്കിക്കാണാം, നിങ്ങൾ അവയ്ക്കീ बेहतर പദ്ധതികളും ഒരുക്കലുകളും എങ്ങനെ നടത്താം.

![ഭീഷണികളെ മനസിലാക്കൽ](../../../translated_images/ml/understanding-threats.89edeada8a97fc0f.webp)

### ജോലി നിർദ്ദേശവും നിർദ്ദേശവും

**വിവരണം:** ആക്രമണക്കാർ AI ഏജന്റിന്റെ നിർദ്ദേശങ്ങളെയും ലക്ഷ്യങ്ങളെയും പ്രോംപ്റ്റിംഗ് അല്ലെങ്കിൽ ഇൻപുട്ടുകൾ മാനിപ്പുലേറ്റ് ചെയ്ത് മാറ്റാൻ ശ്രമിക്കുന്നു.

**നിരോധനം**: AI ഏജന്റ് പ്രക്രിയ ചെയ്യുന്നതിനു മുമ്പ് അപകടകരമായ പ്രോംപ്റ്റുകൾ കണ്ടെത്താൻ സാധൂകരിക്കലും ഇൻപുട്ട് ഫിൽട്ടറുകളും നടപ്പിലാക്കൽ. ഈ തരം ആക്രമണങ്ങൾക്ക് ഏജന്റുമായി സ്ഥിരമായി ഇടപഴകേണ്ടതുമായതിനാൽ, സംഭാഷണത്തിലെ തവണകളുടെ എണ്ണം പരിമിതപ്പെടുത്തലും ഈ ആക്രമണങ്ങൾ തടയാൻ സഹായിക്കുന്നു.

### നിർണായക സിസ്റ്റങ്ങളിലേക്കുള്ള ആക്സസ്

**വിവരണം**: സेंसിറ്റിവായ ഡാറ്റ സംഭരിക്കുന്ന സിസ്റ്റങ്ങളിലേക്കും സേവനങ്ങളിലേക്കും AI ഏജന്റ് ആക്‌സസ് ഉണ്ടെങ്കിൽ, ആക്രമണക്കാർ ഏജന്റുവും ആ സേവനങ്ങളുമായുള്ള ആശയവിനിമയം തകരാറിലാക്കാൻ കഴിയും. നേരിട്ട് ആക്രമണങ്ങളോ അല്ലെങ്കിൽ ഈ സിസ്റ്റങ്ങളേക്കുറിച്ചുള്ള വിവരങ്ങൾ നേടാനുള്ളabayaയ ശ്രമങ്ങളോ ആകാം.

**നിരോധനം**: ഈ തരം ആക്രമണങ്ങൾ തടയാൻ, AI ഏജന്റുകൾക്ക് ആവശ്യമായ സാഹചര്യത്തോളം മാത്രമേ ആക്സസ് അനുവദിക്കണം. ഏജന്റും സിസ്റ്റവും തമ്മിലുള്ള ആശയവിനിമയം സുരക്ഷിതമാക്കുക. സാക്ഷ്യീകരണം, ആക്സസ് നിയന്ത്രണം നടപ്പിലാക്കലും ഈ വിവരങ്ങളെ സംരക്ഷിക്കുന്ന മറ്റൊരു മാർഗമാണ്.

### വിഭവങ്ങളും സേവനങ്ങളും കൂടുതലായി ഉപയോഗിക്കൽ

**വിവരണം:** AI ഏജന്റുകൾ വിവിധ ഉപകരണങ്ങളെയും സേവനങ്ങളെയും ഉപയോഗിച്ച് തടവുകൾ പൂർത്തിയാക്കുന്നു. ആക്രമണക്കാർ ഈ കഴിവ് ഉപയോഗിച്ച് AI ഏജന്റിലൂടെ വ്യാപകമായ അഭ്യർത്ഥനകൾ അയച്ച് ഈ സേവനങ്ങളെയൊക്കെ ആക്രമിക്കാം, ഇത് സിസ്റ്റം തകരാറുകൾക്ക് അല്ലെങ്കിൽ ഉയർന്ന ചിലവുകൾക്ക് കാരണമാകാം.

**നിരോധനം:** AI ഏജന്റുകൾ ഒരു സേവനത്തിന് അയയ്ക്കാവുന്ന അഭ്യർത്ഥനകളുടെ എണ്ണം പരിമിതപ്പെടുത്തുന്ന നയങ്ങൾ നടപ്പിലാക്കുക. AI ഏജന്റിനോട് സംഭാഷണത്തിലെ തവണകളും അഭ്യർത്ഥനകളും കുറയ്ക്കുവാനുള്ള നിയന്ത്രണങ്ങളും ഇത്തരം ആക്രമണങ്ങൾ തടയാനാകും.

### അറിവ് അടിസ്ഥാനത്തെ വിഷം കൂട്ടൽ

**വിവരണം:** ഈ തരം ആക്രമണം നേരിട്ട് AI ഏജന്റിനെ ലക്ഷ്യം വെയ്ക്കുന്നില്ല, എന്നാൽ AI ഏജന്റ് ഉപയോഗിക്കുന്ന അറിവ് അടിസ്ഥാനങ്ങളെയും മറ്റ് സേവനങ്ങളെയും ലക്ഷ്യമെങ്കിലും ചെയ്യുന്നു. ഇത് ഡാറ്റ പോലും കേടാക്കുന്നതായിരിക്കാം, ഇത് AI ഏജന്റ് നൽകുന്ന പ്രതികരണങ്ങളിൽ പക്ഷപാതപരമായതോ ഉദ്ധാരിതമല്ലാത്തതോ ഉള്ളതിനു കാരണമാകുന്നു.

**നിരോധനം:** AI ഏജന്റ് തന്റെ പ്രവൃത്തി പ്രവാഹത്തിൽ ഉപയോഗിക്കുന്ന ഡാറ്റയുടെ സ്ഥിരമായി പരിശോധനം നടത്തുക. ഈ ഡാറ്റയിലേക്ക് ആക്സസ് സുരക്ഷിതമാക്കുകയും, വിശ്വസ്ത വ്യക്തികൾ മാത്രം മാറ്റങ്ങൾ വരുത്താൻ അനുവദിക്കുകയും ചെയ്യുക.

### ബന്ധിപ്പിച്ച പിഴവുകൾ

**വിവരണം:** AI ഏജന്റുകൾ വിവിധ ഉപകരണങ്ങളെയും സേവനങ്ങളെയും പ്രവർത്തിപ്പിക്കുന്നു. ആക്രമണക്കാരാൽ സൃഷ്ടിക്കപ്പെട്ട പിഴവുകൾ മറ്റുള്ള സിസ്റ്റങ്ങൾക്കും പരികലനങ്ങൾക്കുമായി സംവിധാനം ദുരിതപ്പെടുന്നതിനും ആക്രമണം വ്യാപിപ്പിക്കുന്നതിനും ഇടയാക്കുന്നു, പരിശോധനയും പരിഹാരവും കൂടുതൽ ക്ലിഷടമാക്കുന്നു.

**നിരോധനം**: AI ഏജന്റ് നിയന്ത്രിതമായ സാഹചര്യത്തിൽ പ്രവർത്തിക്കണമെന്നു ഉറപ്പാക്കുക, ഉദാഹരണത്തിന് ഡോക്കർ കൺറ്റെയ്‌നറിനുള്ളിൽ പ്രവർത്തിക്കുന്നു, നേരിട്ട് സിസ്റ്റം ആക്രമണങ്ങൾ തടയുന്നതിന്. ചില സിസ്റ്റങ്ങൾ പിഴവ് മറുപടി നൽകുമ്പോൾ ഫാൾബാക്ക് മെക്കാനിസങ്ങളും വീണ്ടും ശ്രമിക്കുന്ന സാന്ദ്രതകളും സൃഷ്ടിക്കുക, ഇത് വലിയ സിസ്റ്റം തകരാറുകൾ തടയുന്നതിന് സഹായിക്കും.

## മനുഷ്യൻ-ഇൻ-ലൂപ്പ്

ഒരു വിശ്വാസ്യ AI ഏജന്റ് സിസ്റ്റം നിർമ്മിക്കുന്നതിൽ മറ്റൊരു ഫലപ്രദമായ മാർഗം മനുഷ്യൻ-ഇൻ-ലൂപ്പ് ഉപയോഗിക്കുകയാണ്. ഇത് ഒരിനം പ്രവാഹം സൃഷ്ടിക്കുന്നു, പ്രവർത്തന സമയം ഉപയോക്താക്കൾ ഏജന്റുകളെ ഫീഡ്ബാക്ക് നൽകാവുന്നതാണ്. ഉപയോക്താക്കൾ essentially ഒരു മൾട്ടി-ഏജന്റ് സംവിധാനത്തിലെ ഏജന്റുമാരായി പ്രവർത്തിക്കുകയും പ്രവർത്തനത്തെ അംഗീകരിക്കാവുന്നതും അവസാനിപ്പിക്കാവുന്നതുമായ പ്രകടനവും നൽകുന്നു.

![മനുഷ്യൻ ഇൻ ദ ലൂപ്പ്](../../../translated_images/ml/human-in-the-loop.5f0068a678f62f4f.webp)

ഇതാണ് മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനൊപ്പം ഈ ആശയം നടപ്പാക്കുന്നത് കാണിക്കുന്ന ഒരു കോഡ് സ്നിപ്പെറ്റ്:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# മനുഷ്യൻ ഉൾപ്പെടുന്ന അനുമതിയോടെ പ്രൊവൈഡർ സൃഷ്‌ടിക്കുക
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# മനുഷ്യന് അനുമതി ഘട്ടം ഉള്ള ഏജന്റ് സൃഷ്‌ടിക്കുക
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ഉപയോക്താവ് പ്രതികരണം അവലോകനം ചെയ്ത് അംഗീകരിക്കാം
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## നിക്ഷേപം

വിശ്വാസയോഗ്യമായ AI ഏജന്റുമാർ നിർമ്മിക്കുന്നത് സൂക്ഷ്മമായ രൂപകൽപ്പന, ശക്തമായ സുരക്ഷാ നടപടികൾ, തുടർച്ചയായ 반복ങ്ങൾ എന്നിവ ആവശ്യമാണ്. ഘടനാത്മകമായ മെടാ പ്രോംപ്റ്റിംഗ് സിസ്റ്റങ്ങൾ നടപ്പിലാക്കിയും, സാദ്ധ്യമായ ഭീഷണികളെ മനസിലാക്കിയും, നിയന്ത്രണ തന്ത്രങ്ങൾ പ്രയോഗിച്ചും, ഡെവലപ്പർമാർ സുരക്ഷിതവും ഫലപ്രദവുമായ AI ഏജന്റുമാർ സൃഷ്ടിക്കാനാകും. കൂടാതെ, മനുഷ്യൻ-ഇൻ-ലൂപ്പ് സമീപനം ഉൾപ്പെടുത്തിയാൽ ഉപയോക്തൃ ആവശ്യങ്ങൾക്കോട് AI ഏജന്റുമാർ സുതാര്യമായി ചേർന്നു, അപകടങ്ങൾ കുറച്ചു വളരെ വിശ്വാസ്യതയും ഉറപ്പാക്കും. AI തുടരുമായും വികസിച്ചുവന്നുകൊണ്ടിരിക്കെ, സുരക്ഷ, സ്വകാര്യത, നൈതിക ചിന്തനങ്ങളിൽ സജീവമായ സമീപനം നിലനിർത്തുന്നത് AI-ചാലിത സിസ്റ്റങ്ങളിൽ വിശ്വാസവും വിശ്വാസ്യതയും വളർത്താൻ നിർണ്ണായകമാണ്.

## കോഡ് സാമ്പിളുകൾ

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): മെടാ-പ്രോംപ്റ്റ് സിസ്റ്റം-മെസേജ് ഫ്രെയിംവർക്ക് ഘട്ടം-ഘട്ടം പ്രദർശനം.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): മുൻകൂർ അംഗീകൃതി ഗേറ്റുകൾ, അപകട നിലവാര ക്രമീകരണം, വിശ്വാസ്യമായ ഏജന്റുകളിലേക്ക് ഓഡിറ്റ് ലോഗിംഗ്.

### വിശ്വാസയോഗ്യമായ AI ഏജന്റുമാർ നിർമ്മിക്കലിനെ കുറിച്ച് കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ലെ ചേർന്ന് മറ്റ് പഠനാർത്ഥികളുമായി ചേരുക, ഓഫീസ് ഓവറുകളിൽ പങ്കെടുക്കുക, നിങ്ങളുടെ AI ഏജന്റ് ചോദ്യങ്ങൾക്ക് മറുപടി મેળ്കുക.

## അധിക സ്രോതസ്സുകൾ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ജവാബ് മലയാളത്തിൽ AI അവലോകനം</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">സൃഷ്ടി AI മോഡലുകളും AI ആപ്ലിക്കേഷനും വിലയിരുത്തൽ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">സുരക്ഷാ സിസ്റ്റം മെസേജുകൾ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">അപകടം വിലയിരുത്തൽ ഫോർമാറ്റ്</a>

## കഴിഞ്ഞ പാഠം

[Agentic RAG](../05-agentic-rag/README.md)

## അടുത്ത പാഠം

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->