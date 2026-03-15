[![വിശ്വാസയോഗ്യമായ AI ഏജന്റുകൾ](../../../translated_images/ml/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(മുകളിൽ കാണുന്ന ചിത്രം ക്ലിക്ക് ചെയ്ത് ഈ പാഠത്തിന്റെ വീഡിയോ കാണുക)_

# വിശ്വാസയോഗ്യമായ AI ഏജന്റുകൾ നിർമ്മിക്കൽ

## പരിചയം

ഈ പാഠത്തിൽ ഉൾപ്പെടുന്നത്:

- സുരക്ഷിതവും ഫലപ്രദവുമായ AI ഏജന്റുകൾ എങ്ങനെ നിർമ്മിച്ച് വിന്യസിക്കാമെന്നത്
- AI ഏജന്റുകൾ വികസിപ്പിക്കുമ്പോൾ പരിഗണിക്കേണ്ട പ്രധാനപ്പെട്ട സുരക്ഷാ കാര്യങ്ങൾ.
- AI ഏജന്റുകൾ വികസിപ്പിക്കുമ്പോൾ ഡാറ്റയും ഉപയോക്തൃ സ്വകാര്യതയും എങ്ങനെ സംരക്ഷിക്കാമെന്ന്.

## പഠനലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയതിനു ശേഷം, നിങ്ങൾക്കറിയാമാകും എങ്ങനെ:

- AI ഏജന്റുകൾ സൃഷ്ടിക്കുമ്പോൾ സംഭവിക്കാവുന്ന അപകടങ്ങൾ തിരിച്ചറിഞ്ഞ് അവയെ കുറക്കാം.
- ഡാറ്റയും ആക്സസ്സും ശരിയായി കൈകാര്യം ചെയ്യുന്നതിന് സുരക്ഷാ നടപടികൾ നടപ്പാക്കാം.
- ഡാറ്റ സ്വകാര്യത നിലനിര്‍ത്തുന്നും ഉപയോക്തൃ അനുഭവം ഗുണമേന്മയുള്ളതാക്കുന്ന AI ഏജന്റുകൾ സൃഷ്ടിക്കാം.

## സുരക്ഷ

ആരംഭത്തിൽ നാം സുരക്ഷിതമായ ഏജന്റിക് (ഏജന്റ് അധിഷ്ഠിത) ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുന്നതിനെ നോക്കാം. സുരക്ഷയുടെ അർത്ഥം AI ഏജന്റ് രൂപകൽപ്പനപ്രകാരം പ്രവർത്തിക്കുക എന്നതാണ്. ഏജന്റ് അധിഷ്ഠിത ആപ്ലിക്കേഷനുകളുടെ നിർമ്മാതാക്കളായ നമുക്ക്, സുരക്ഷ പരമാവധി ഉറപ്പുവരുത്താൻ മാർഗങ്ങളും ഉപകരണങ്ങളും ഉണ്ട്:

### സിസ്റ്റം മെസേജ് ഫ്രെയിംവർക്ക് നിർമ്മാണം

വിപുലമായ ഭാഷാ മോഡലുകൾ (LLMs) ഉപയോഗിച്ച് AI അപ്ലിക്കേഷൻ ഒരിക്കൽ പോലും നിർമ്മിച്ചിട്ടുണ്ടെങ്കിൽ, ഒരു ശക്തമായ സിസ്റ്റം പ്രോംപ്റ്റ് അല്ലെങ്കിൽ സിസ്റ്റം മെസേജിന്റെ രൂപകൽപ്പനയുടെ പ്രാധാന്യം അറിയാം. ഈ പ്രോംപ്റ്റുകൾ LLM ഉപയോക്താവിനുമ interplay ഉയർന്നതും ഡാറ്റയുമായി എങ്ങനെ പ്രവർത്തിക്കുമെന്ന് നിർദ്ദേശിക്കുന്ന മെറ്റാ നിയമങ്ങൾ, നിർദ്ദേശങ്ങൾ, മാർഗ്ഗരേഖകൾ എന്നിവ സ്ഥാപിക്കുന്നു.

AI ഏജന്റുകൾക്കുശേഷം, ഞങ്ങൾ രൂപകല്പന ചെയ്ത ടാസ്കുകൾ പൂർത്തിയാക്കാൻ ഏറ്റവും പ്രത്യേകമായ നിർദ്ദേശങ്ങൾ ആവശ്യമുണ്ട്, അതുകൊണ്ട് സിസ്റ്റം പ്രോംപ്റ്റിന്റെ പ്രാധാന്യം കൂടുതൽ ആണ്.

സ്കേലബിൾ സിസ്റ്റം പ്രോംപ്റ്റുകൾ സൃഷ്ടിക്കാൻ, ഒരു അല്ലെങ്കിൽ അധിക ഏജന്റുകൾ നമ്മുടെ അപ്ലിക്കേഷനിൽ നിർമ്മിക്കുന്നതിന് സിസ്റ്റം മെസേജ് ഫ്രെയിംവർക്ക് ഉപയോഗിക്കാമത്രെ:

![സിസ്റ്റം മെസേജ് ഫ്രെയിംവർക്ക് നിർമ്മാണം](../../../translated_images/ml/system-message-framework.3a97368c92d11d68.webp)

#### ഘടകം 1: ഒരു മെടാ സിസ്റ്റം സന്ദേശം സൃഷ്ടിക്കുക 

മെടാ പ്രോംപ്റ്റ് LLM ഉപയോഗിച്ച് നാം സൃഷ്ടിക്കുന്ന ഏജന്റുകൾക്കുള്ള സിസ്റ്റം പ്രോംപ്റ്റുകൾ ജനനമാക്കാൻ ഉപയോഗിക്കും. ഇത് ഒരു ടെംപ്ലേറ്റായി രൂപകൽപ്പന ചെയ്‌തുകൊണ്ട് ആവശ്യമായപ്പോൾ നിരവധി ഏജന്റുകൾ കാര്യക്ഷമമായി സൃഷ്ടിക്കാൻ സഹായിക്കുന്നു.

ഇതാ LLM-ന് നാം നൽകരുതായിരുന്ന മെടാ സിസ്റ്റം സന്ദേശത്തിന്റെ ഒരു ഉദാഹരണം:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ഘടകം 2: ഒരു അടിസ്ഥാന പ്രോമ്പ്റ്റ് സൃഷ്ടിക്കുക

അടുത്ത ഘടകം AI ഏജന്റിനെ വിവരണം ചെയ്യുന്നതിനുള്ള ഒരു അടിസ്ഥാന പ്രോമ്പ്റ്റ് സൃഷ്ടിക്കുകയാണ്. ഏജന്റിന്റെ റോൾ, ഏജന്റ് പൂർത്തിയാക്കേണ്ട ടാസ്കുകൾ, ഏജന്റിന്റെ മറ്റ് ഉത്തരവാദിത്വങ്ങൾ എന്നിവ ഉൾപ്പെടുത്തുക.

ഇതാ ഒരു ഉദാഹരണം:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ഘടകം 3: മെടാ സിസ്റ്റം സന്ദേശം LLM-ന് അടിസ്ഥാന സിസ്റ്റം സന്ദേശമായി നൽകുക

ഇപ്പോൾ നാം ഈ സിസ്റ്റം സന്ദേശം മെറ്റാ സിസ്റ്റം സന്ദേശമായി നൽകിയും നമ്മുടെ അടിസ്ഥാന സിസ്റ്റം സന്ദേശം നൽകിയും ഇത് മികച്ച രൂപത്തിൽ എഐ ഏജന്റുകൾ നയിക്കുന്നതിനുള്ള സിസ്റ്റം സന്ദേശം ഉണ്ടാക്കാൻ ആകും.

ഇത് കൂടുതൽ നന്നായി രൂപകൽപ്പന ചെയ്ത സിസ്റ്റം സന്ദേശം ഉത്പാദിപ്പിക്കും:

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

#### ഘടകം 4: പുനരാവലോകരിക്കുക மற்றும் മെച്ചപ്പെടുത്തുക

ഈ സിസ്റ്റം മെസേജ് ഫ്രെയിംവർക്കിന്റെ മൂല്യം, ഒരേ സമയം നിരവധി ഏജന്റുകളുടെ സിസ്റ്റം സന്ദേശങ്ങൾ വളരെ എളുപ്പത്തിൽ ഉണ്ടാക്കാൻ കഴിയുക മാത്രമല്ല, സമയംകൊണ്ട് നിങ്ങളുടെ സിസ്റ്റം സന്ദേശങ്ങൾ മെച്ചപ്പെടുത്തുന്നതിലുമാണ്. ഏകദേശം ഒരു സംപൂർണ ഉപയോഗകേസിന് ആദ്യമായിരുന്നുതന്നെ പൂർണ്ണമായി സജ്ജമായ ഒരു സിസ്റ്റം സന്ദേശം ഉണ്ടാകുന്നത് അപൂർവമാണ്. അടിസ്ഥാന സിസ്റ്റം സന്ദേശം ചെറിയ മാറ്റങ്ങൾ വരുത്തുകയും സിസ്റ്റത്തിലൂടെ ഓടിച്ച് ഫലങ്ങൾ താരതമ്യപ്പെടുത്തുകയും വിലയിരുത്തുകയും ചെയ്യാൻ സാധിക്കേണ്ടതാണ്.

## ഭീഷണികളെ മനസിലാക്കൽ

വിശ്വാസയോഗ്യമായ AI ഏജന്റുകൾ നിർമ്മിക്കാൻ, നിങ്ങളുടെ AI ഏജന്റിന് സംഭവിക്കാവുന്ന അപകടങ്ങളും ഭീഷണികളും മനസിലാക്കി അവ കുറയ്ക്കുന്നത് പ്രധാനമാണ്. AI ഏജന്റുകൾക്ക് നേരെയുള്ള ചില ഭീഷണികൾ മാത്രം ഇവിടെ നോക്കാം, അവയെക്കുറിച്ച് നിങ്ങൾക്ക് മെച്ചമായി പദ്ധതി തയ്യാറാക്കാനും തയ്യാറെടുക്കാനും സഹായിക്കും.

![ഭീഷണികളെ മനസിലാക്കൽ](../../../translated_images/ml/understanding-threats.89edeada8a97fc0f.webp)

### ജോലിയും നിർദ്ദേശവും

**വിവരണം:** ആക്രമണക്കാർ പ്രോംപ്റ്റിങ്ങ് yoki ഇൻപുട്ടുകൾ манിപ്പുലേറ്റ് ചെയ്തുകൊണ്ട് AI ഏജന്റിന്റെ നിർദ്ദേശങ്ങളോ ലക്ഷ്യങ്ങളോ മാറ്റാൻ ശ്രമിക്കുന്നു.

**പ്രതിരോധം**: അപകടകരമായ പ്രോംപ്റ്റുകൾ AI ഏജന്റ് പ്രോസസ്സ് ചെയ്യുന്നതിന് മുൻപ് കണ്ടെത്താൻ വാലിഡേഷൻ ചെക്കുകൾയും ഇൻപുട്ട് ഫിൽറ്ററുകളും നടപ്പിലാക്കുക. ഇത്തരം ആക്രമണങ്ങൾക്ക് സാധാരണയായി ഏജന്റുമായുള്ള സ്ഥിരമായ ഇടപെടൽ ആവശ്യമാണ്, അതിനാൽ സംഭാഷണത്തിൽ ഘട്ടങ്ങളുടെ എണ്ണം പരിമിതപ്പെടുത്തുന്നതാണ് മറ്റൊരു പ്രതിരോധી മാതൃക.

### നിർണായക സംവിധാനങ്ങളിലേക്ക് പ്രവേശനം

**വിവരണം**: AI ഏജന്റ് حساس ഡാറ്റ സംഭരിക്കുന്ന സിസ്റ്റങ്ങളിലേക്കും സേവനങ്ങളിലേക്കും ആക്സസ് ഉണ്ടെങ്കിൽ, ആക്രമണക്കാർ ഏജന്റും ഈ സേവനങ്ങളും തമ്മിലുള്ള കമ്മ്യൂണിക്കേഷൻ തകരാറിലാക്കാൻ ശ്രമിക്കാം. ഇത് നേരിട്ടുള്ള ആക്രമാണോ അല്ലെങ്കിൽ ഏജന്റ് വഴി ഈ സിസ്റ്റങ്ങളെക്കുറിച്ചുള്ള വിവരങ്ങൾ നേടിയെടുക്കാൻ ചെയ്‌തുവരുന്ന പരോക്ഷ ശ്രമങ്ങളാണോ ആകാം.

**പ്രതിരോധം**: ഇത്തരത്തിലുള്ള ആക്രമണങ്ങൾ തടയാൻ AI ഏജന്റുകൾക്ക് സിസ്റ്റങ്ങളിലേക്കുള്ള ആക്സസ് ആവശ്യമായത് മാത്രം അനുവദിക്കുക. ഏജന്റ്-സിസ്റ്റം ഇടപെടൽ സുരക്ഷിതമാകണം. ഓഥന്റിക്കേഷൻയും ആക്സസ്‌کنട്രോൾയും നടപ്പിലാക്കുക.

### സ്രോതസ്സുകൾക്കും സേവനങ്ങൾക്കും മേൽഭാരമേറിയ ഉപയോഗം

**വിവരണം:** ടാസ്കുകൾ പൂർത്തിയാക്കാൻ AI ഏജന്റുകൾ വിവിധ ടൂളുകളും സേവനങ്ങളും ഉപയോഗിക്കാം. ആക്രമണക്കാർ ഈ കഴിവ് ഉപയോഗിച്ച് AI ഏജന്റിലൂടെ ഉയർന്ന തോതിലുള്ള അഭ്യർത്ഥനകൾ അയച്ച് ഈ സേവനങ്ങളെ ലക്ഷ്യമാക്കി ആക്രമിക്കാവുന്നതാണ്, ഇതിന്റെ ഫലമായി സിസ്റ്റം തകർച്ചകൾ അല്ലെങ്കിൽ ഉയർന്ന ചെലവുകൾ ഉണ്ടാകാം.

**പ്രതിരോധം:** ഒരു AI ഏജന്റ് ഒരു സേവനത്തിലേക്ക് ചെയ്യാവുന്ന അഭ്യർത്ഥനകളുടെ എണ്ണം പരിമിതപ്പെടുത്തുന്ന നയങ്ങൾ നടപ്പിലാക്കുക. സംഭാഷണ ഘട്ടങ്ങളുടെ എണ്ണം കൂടാതെ നിങ്ങളുടെ AI ഏജന്റിലേയ്ക്ക് വരുന്ന അഭ്യർത്ഥനകൾക്ക് പരിധി നൽകുന്നതും ഇത്തരത്തിലുള്ള ആക്രമണങ്ങൾ തടയാനുള്ള മറ്റൊരു മാർഗമാണ്.

### ജ്ഞാനഭണ്ഡാരത്തിൽ വിഷപ്രവേശനം

**വിവരണം:** ഈ തരത്തിലുള്ള ആക്രമണം AI ഏജന്റിനെ നേരിട്ട് ലക്ഷ്യമിടുന്നില്ല, പക്ഷേ ഏജന്റ് ഉപയോഗിക്കുന്ന നോളജ് ബേസ് പോലുള്ള സേവനങ്ങളെ ലക്ഷ്യമിടുന്നു. ടാസ്കുകൾ പൂർത്തിയാക്കാൻ ഉപയോഗിക്കുന്ന ഡാറ്റ അല്ലെങ്കിൽ വിവരങ്ങൾ ദുഷ്‌പ്രക്ഷേപം ചെയ്യും, ഫലത്തിൽ ഉപയോക്താവിനു ഇഷ്ടമല്ലാത്ത അല്ലെങ്കിൽ പ്രവണതാശാലിയുള്ള പ്രതികരണങ്ങൾ ഉണ്ടാകാം.

**പ്രതിരോധം:** AI ഏജന്റ് താൻ ഉപയോഗിക്കുന്ന പ്രവൃത്തികൾക്കുള്ള ഡാറ്റയുടെ സ്ഥിരമായ പരിശോധന നടത്തുക. ഈ ഡാറ്റയിലേക്കുള്ള ആക്സസ് സുരക്ഷിതമാക്കുകയും വിശ്വാസ്യതയുള്ള വ്യക്തികളുടെ മുഖേന മാത്രമേ മാറ്റങ്ങൾ വരുത്തുകയുള്ളൂ എന്നത് ഉറപ്പാക്കുക.

### കടന്നുപോകുന്ന പിശകുകൾ

**വിവരണം:** AI ഏജന്റുകൾ ടാസ്‌കുകൾ പൂർത്തിയാക്കാൻ വിവിധ ടൂളുകളും സേവനങ്ങളും ആക്സസ് ചെയ്യുന്നു. ആക്രമണക്കാരാൽ ഉണ്ടാകുന്ന പിശകുകൾ മറ്റ് സിസ്റ്റങ്ങളിലേക്കും പരന്നു, ഏജന്റ് കണക്റ്റ ചെയ്തിരിക്കുന്ന മറ്റു സിസ്റ്റങ്ങൾ കൂടി പൊളിഞ്ഞുപോകാൻ നടത്താം, ഇതോടെ ആക്രമണം വൻ വ്യാപകമാകുകയും തകരാറുകൾ കണ്ടെത്തി പരിഹരിക്കാനുള്ളത് ബുദ്ധിമുട്ടായി മാറുകയും ചെയ്യാം.

**പ്രതിരോധം**: ഇതിൽ നിന്ന് രക്ഷപെടാൻ ഒരു മാർഗം ആണ് AI ഏജന്റ് ഒരു പരിമിതമായ പരിസരത്ത് പ്രവർത്തിക്കിക്കുക, ഉദാഹരണത്തിന് Docker കൺടെയ്‌നറിൽ ടാസ്കുകൾ നടത്തുന്നതുപോലെ, നേരിട്ട് സിസ്റ്റം ആക്രമണങ്ങൾ തടയാൻ. ചില സിസ്റ്റുകൾ തെറ്റായ പ്രതികരണം കാണിക്കുമ്പോൾ ഫാല്ബാക്ക് മെക്കാനിസങ്ങളും റിട്രൈ ലജിക്കും സൃഷ്ടിക്കുക, ഇത് വലിയ സിസ്റ്റം തകർച്ചകൾ പ്രതിരോധിക്കാൻ സഹായിക്കും.

## മനുഷ്യൻ-ഇൻ-ദി-ലൂപ്

വിശ്വാസയോഗ്യമായ AI ഏജന്റ് സിസ്റ്റങ്ങൾ നിർമ്മിക്കുന്നതിന് മറ്റൊരു ഫലപ്രദമായ മാർഗമാണ് മനുഷ്യൻ-ഇൻ-ദി-ലൂപ് ഉപയോഗിക്കുക. ഇതിലൂടെ റൺ സമയത്ത് ഉപയോക്താക്കൾ ഏജന്റുകളിൽ ഫീഡ്‌ബാക്ക് നൽകാൻ കഴിയും. ഉപയോക്താക്കൾ സ്വാഭാവികമായി മൾട്ടി-ഏജന്റ് സിസ്റ്റിലുള്ള ഏജന്റുകളായി പ്രവർത്തിച്ച് റണ്ണിങ് പ്രക്രിയയ്ക്കു അംഗീകാരം നൽകുകയോ അവസാനിപ്പിക്കുകയോ ചെയ്യുന്നു.

![ലൂപിൽ മനുഷ്യൻ](../../../translated_images/ml/human-in-the-loop.5f0068a678f62f4f.webp)

ഇത്തരമൊരു ആശയം എങ്ങനെ നടപ്പിലാക്കുന്നുവെന്ന് കാണിക്കാൻ Microsoft Agent Framework ഉപയോഗിച്ച് ഒരു കോഡ് സ്നിപ്പെറ്റ് ഇതാ:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# മാനവ ഇടപെടൽ ഉള്ള അംഗീകാരത്തോടെ പ്രൊവൈഡർ സൃഷ്ടിക്കുക
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# മാനവ അംഗീകാരഘട്ടം ഉള്ള ഏജന്റ് സൃഷ്ടിക്കുക
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

## നിഗമനം

വിശ്വാസയോഗ്യമായ AI ഏജന്റുകൾ നിർമ്മിക്കാൻ സൂക്ഷ്മമായ രൂപകൽപ്പന, ദൃഢമായ സുരക്ഷാ നടപടികൾ, തുടർച്ചയായ പുനരാവലോകരണം എന്നിവ ആവശ്യമാണ്. ഘടനാപരമായ മെറ്റാ പ്രോംപ്റ്റിങ് സിസ്റ്റങ്ങൾ നടപ്പിലാക്കുന്നതിലൂടെ, സാധ്യതാ ഭീഷണികളെ മനസിലാക്കിയും നിവാരണം ആരംഭിക്കുന്നതിലൂടെ ഡെവലപ്പർമാർ സുരക്ഷിതവും ഫലപ്രദവുമായ AI ഏജന്റുകൾ സൃഷ്ടിക്കാം. കൂടാതെ, മനുഷ്യൻ-ഇൻ-ദി-ലൂപ് സമീപനം ഉൾപ്പെടുത്തി എഐ ഏജന്റുകൾ ഉപയോക്തൃ ആവശ്യങ്ങളോടൊപ്പം സുസംയോജിതമായി നിലനിർത്തുകയും അപകടങ്ങൾ കുറയ്ക്കുകയും ചെയ്യുന്നു. AI തുടർന്നും പരിണമിക്കുമ്പോൾ, സുരക്ഷ, സ്വകാര്യത, സദാചാരം എന്നിവയിൽ മുൻകൈ എടുത്തുനിൽക്കുന്നത് AI-ആധാരിത സിസ്റ്റുകളിൽ വിശ്വാസവും വിശ്വാസ്യതയും വളർത്താൻ പ്രധാനമായിരിക്കും.

### വിശ്വാസയോഗ്യമായ AI ഏജന്റുകൾ നിർമ്മിക്കുന്നതിനെക്കുറിച്ച് കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

മറ്റ് പഠിതാക്കളെ കാണാനും, ഓഫീസ് മണിക്കൂർ സെഷനുകളിൽ പങ്കെടുക്കാനും നിങ്ങളുടെ AI ഏജന്റുകൾ സംബന്ധിച്ച ചോദ്യങ്ങൾക്ക് ഉത്തരം ലഭിക്കാനും [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ൽ ചേരുക.

## അധിക വിഭവങ്ങൾ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ഉത്തരവാദിത്വമുള്ള AI അവലോകനം</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ജനനാത്മക AI മോഡലുകളും AI അപ്ലിക്കേഷനുകളുടെയും മൂല്യനിർണ്ണയം</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">സുരക്ഷാ സിസ്റ്റം സന്ദേശങ്ങൾ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">റിസ്ക് അസ്സസ്‌മെന്റ് ടെംപ്ലേറ്റ്</a>

## മുൻപത്തെ പാഠം

[Agentic RAG](../05-agentic-rag/README.md)

## അടുത്ത പാഠം

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:

ഈ ഡോക്യുമെന്റ് AI പരിഭാഷാ സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയിലേക്ക് ശ്രമിച്ചിരുന്നെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിശകുകൾ അല്ലെങ്കിൽ അകമുഖതകൾ ഉണ്ടാകാമെന്നത് ദയവായി ശ്രദ്ധിക്കുക. ഏറെപ്രധാനമായ വിവരങ്ങളുടെ കാര്യത്തിൽ, മാതൃഭാഷയിലെ ആ യഥാർത്ഥ ഡോക്യുമെന്റ് ആണ് അധികാരപരമായ ഉറവിടം എന്ന നിലയിൽ പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ നിർദേശം ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷയുടെ ഉപയോഗത്തിൽ നിന്നുണ്ടാവുന്ന任何误解മോ തെറ്റായ വ്യാഖ്യാനമോ ഇതിലൂടെ ഉണ്ടായാൽ ഞങ്ങൾ അതിലെ οποιαδήποτε ഉത്തരവാദിത്വവും ഏറ്റെടുക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->