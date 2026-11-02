[![ਭਰੋਸੇਮੰਦ AI ਏਜੰਟ](../../../translated_images/pa/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ਇਸ ਸਬਕ ਦੀ ਵੀਡੀਓ ਵੇਖਣ ਲਈ ਉਪਰ ਦਿਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿਕ ਕਰੋ)_

# ਭਰੋਸੇਮੰਦ AI ਏਜੰਟ ਬਣਾਉਣਾ

## পরিচয়

ਇਸ ਸਬਕ ਵਿੱਚ ਇਹ ਸਮਝਾਇਆ ਜਾਵੇਗਾ:

- ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ AI ਏਜੰਟ ਕਿਵੇਂ ਬਣਾਏ ਅਤੇ ਤੈਯਾਰ ਕਰੇ ਜਾਣ।
- AI ਏਜੰਟ ਬਣਾਉਂਦੇ ਸਮੇਂ ਮਹੱਤਵਪੂਰਣ ਸੁਰੱਖਿਆ ਸਮੀਖਿਆਵਾਂ।
- ਡਾਟਾ ਅਤੇ ਯੂਜ਼ਰ ਦੀ ਪਰਾਈਵੇਸੀ ਕਿਵੇਂ ਬਣਾਈ ਰੱਖੀ ਜਾਵੇ।

## ਸਿਖਣ ਦੇ ਲਕੜੇ

ਇਸ ਸਬਕ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਦ, ਤੁਸੀਂ ਜਾਣੋਗੇ ਕਿ ਕਿਵੇਂ:

- AI ਏਜੰਟ ਬਣਾਉਂਦੇ ਸਮੇਂ ਖਤਰੇ ਪਛਾਣੇ ਅਤੇ ਘਟਾਏ ਜਾਣ।
- ਸੁਰੱਖਿਆ ਉਪਾਅ ਲਾਗੂ ਕਰਨ ਜੋ ਡਾਟਾ ਅਤੇ ਪਹੁੰਚ ਦੀ ਸਹੀ ਤਰ੍ਹਾਂ ਦੇਖਭਾਲ ਕਰਦੇ ਹਨ।
- ਐਸੇ AI ਏਜੰਟ ਬਣਾਓ ਜੋ ਡਾਟਾ ਪਰਾਈਵੇਸੀ ਰੱਖਣ ਅਤੇ ਵਧੀਆ ਯੂਜ਼ਰ ਅਨੁਭਵ ਦੇਣ।

## ਸੁਰੱਖਿਆ

ਚਲੋ ਪਹਿਲਾਂ ਸੁਰੱਖਿਅਤ ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਬਾਰੇ ਵੇਖੀਏ। ਸੁਰੱਖਿਆ ਦਾ ਮਤਲਬ ਹੈ ਕਿ AI ਏਜੰਟ ਆਪਣੀ ਡਿਜ਼ਾਈਨ ਮੁਤਾਬਕ ਕੰਮ ਕਰਦਾ ਹੈ। ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਵਾਲੇ ਵਜੋਂ ਸਾਡੇ ਕੋਲ ਸੁਰੱਖਿਆ ਵਧਾਉਣ ਲਈ ਤਰੀਕੇ ਅਤੇ ਔਜਾਰ ਹਨ:

### ਸਿਸਟਮ ਮੈਸੇਜ ਫਰੇਮਵਰਕ ਬਣਾਉਣਾ

ਜੇ ਤੁਸੀਂ ਕਦੇ ਵੱਡੇ ਲੈਂਗਵੇਜ ਮਾਡਲਾਂ (LLMs) ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈ ਹੈ ਤਾਂ ਤੁਹਾਨੂੰ ਇਹ ਪਤਾ ਹੈ ਕਿ ਮਜ਼ਬੂਤ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਜਾਂ ਸਿਸਟਮ ਮੈਸੇਜ ਡਿਜ਼ਾਈਨ ਕਰਨਾ ਕਿੰਨਾ ਜ਼ਰੂਰੀ ਹੈ। ਇਹ ਪਰਾਮਰਸ਼ ਮੀਟਾ ਨਿਯਮ, ਹਦਾਇਤਾਂ ਅਤੇ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ ਬਣਾਉਂਦੇ ਹਨ ਕਿ LLM ਯੂਜ਼ਰ ਅਤੇ ਡਾਟਾ ਨਾਲ ਕਿਵੇਂ ਵੱਤਰਵੇ ਕਰੇਗਾ।

AI ਏਜੰਟ ਲਈ, ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਹੋਰ ਵੀ ਜ਼ਰੂਰੀ ਹੁੰਦਾ ਹੈ ਕਿਉਂਕਿ AI ਏਜੰਟਾਂ ਨੂੰ ਉਹਨਾਂ ਦੇ ਕੰਮ ਲਈ ਬਹੁਤ ਵਿਸ਼ੇਸ਼ ਹੁਕਮਾਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

ਸਕੇਲ ਕਰਨ ਯੋਗ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਬਣਾਉਣ ਲਈ, ਅਸੀਂ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਇੱਕ ਜਾਂ ਵੱਧ ਏਜੰਟਾਂ ਲਈ ਸਿਸਟਮ ਮੈਸੇਜ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ:

![ਸਿਸਟਮ ਮੈਸੇਜ ਫਰੇਮਵਰਕ ਬਣਾਉਣਾ](../../../translated_images/pa/system-message-framework.3a97368c92d11d68.webp)

#### ਕਦਮ 1: ਇੱਕ ਮੀਟਾ ਸਿਸਟਮ ਮੈਸੇਜ ਬਣਾਓ

ਇਹ ਮੀਟਾ ਪ੍ਰਾਂਪਟ LLM ਦੁਆਰਾ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਤੇਜ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਵੇਗੀ ਜੋ ਸਾਡੇ ਬਣਾਏ ਵਾਲੇ ਏਜੰਟਾਂ ਲਈ ਹੋਣਗੇ। ਅਸੀਂ ਇਸਨੂੰ ਟੈਮਪਲੇਟ ਵਾਂਗ ਬਣਾਉਂਦੇ ਹਾਂ ਤਾਂ ਜੋ ਜੇ ਜ਼ਰੂਰਤ ਹੋਵੇ ਤਾਂ ਅਸੀਂ ਕਈ ਏਜੰਟਾਂ ਨੂੰ ਅਸਾਨੀ ਨਾਲ ਬਣਾ ਸਕੀਏ।

ਇੱਥੇ ਇੱਕ ਉਦਾਹਰਨ ਹੈ ਜੋ ਅਸੀਂ LLM ਨੂੰ ਮੀਟਾ ਸਿਸਟਮ ਮੈਸੇਜ ਵਜੋਂ ਦੇਵੇਂਗੇ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ਕਦਮ 2: ਇੱਕ ਬੁਨਿਆਦੀ ਪ੍ਰਾਂਪਟ ਬਣਾਓ

ਅਗਲਾ ਕਦਮ ਹੈ AI ਏਜੰਟ ਦਾ ਵੇਰਵਾ ਦੇਣ ਲਈ ਬੁਨਿਆਦੀ ਪ੍ਰਾਂਪਟ ਬਣਾਉਣਾ। ਤੁਹਾਨੂੰ ਏਜੰਟ ਦੀ ਭੂਮਿਕਾ, ਉਹ ਕੰਮ ਜੋ ਏਜੰਟ ਪੂਰੇ ਕਰੇਗਾ, ਅਤੇ ਹੋਰ ਜਿੰਮੇਵਾਰੀਆਂ ਸ਼ਾਮਲ ਕਰਨੀ ਚਾਹੀਦੀਆਂ ਹਨ।

ਇੱਥੇ ਇੱਕ ਉਦਾਹਰਨ ਹੈ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ਕਦਮ 3: ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਮੈਸੇਜ LLM ਨੂੰ ਦਿਓ

ਹੁਣ ਅਸੀਂ ਇਸ ਸਿਸਟਮ ਮੈਸੇਜ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਢਾਲ ਸਕਦੇ ਹਾਂ ਕਿ ਮੀਟਾ ਸਿਸਟਮ ਮੈਸੇਜ ਅਤੇ ਸਾਡਾ ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਮੈਸੇਜ ਦੋਨੋ ਦੇ ਕੇ।

ਇਹ ਇੱਕ ਸਿਸਟਮ ਮੈਸੇਜ ਤਿਆਰ ਕਰੇਗਾ ਜੋ ਸਾਡੇ AI ਏਜੰਟਾਂ ਲਈ ਰਾਹਦਾਰੀ ਕਰਨ ਵਿੱਚ ਬਿਹਤਰ ਹੋਵੇਗਾ:

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

#### ਕਦਮ 4: ਦੁਹਰਾਓ ਅਤੇ ਸੁਧਾਰ ਕਰੋ

ਇਸ ਸਿਸਟਮ ਮੈਸੇਜ ਫਰੇਮਵਰਕ ਦੀ ਕਦਰ ਇਹ ਹੈ ਕਿ ਇਹ ਤੁਹਾਨੂੰ ਕਈ ਏਜੰਟਾਂ ਲਈ ਸਿਸਟਮ ਮੈਸੇਜ ਬਣਾ ਕੇ ਸੌਖਾ ਕਰਨ ਅਤੇ ਸਮੇਂ ਨਾਲ ਆਪਣੇ ਸਿਸਟਮ ਮੈਸੇਜ ਵਧੀਆ ਕਰਦੇ ਜਾਣ ਦੀ ਆਜ਼ਾਦੀ ਦਿੰਦਾ ਹੈ। ਪਹਿਲੀ ਵਾਰ ਤੁਹਾਡੀ ਸਾਰੀ ਜਰੂਰਤਾਂ ਲਈ ਕੋਈ ਸਿਸਟਮ ਮੈਸੇਜ ਬਣਨਾ ਕਮ ਅਕਸਰ ਹੁੰਦਾ ਹੈ। ਛੋਟੇ-ਛੋਟੇ ਬਦਲਾਅ ਅਤੇ ਸੁਧਾਰ ਰਾਹੀਂ ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਮੈਸੇਜ ਬਦਲ ਕੇ ਅਤੇ ਉਸਨੂੰ ਸਿਸਟਮ ਦੁਆਰਾ ਚਲਾਕੇ, ਤੁਸੀਂ ਨਤੀਜੇ ਦੀ ਤੁਲਨਾ ਕਰਕੇ ਮੁਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹੋ।

## ਧਮਕੀਆਂ ਦੀ ਸਮਝ

ਭਰੋਸੇਮੰਦ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਤੁਹਾਨੂੰ ਆਪਣੇ AI ਏਜੰਟ ਉੱਤੇ ਹੋਣ ਵਾਲੇ ਖਤਰੇ ਅਤੇ ਧਮਕੀਆਂ ਨੂੰ ਸਮਝਣਾ ਅਤੇ ਘਟਾਉਣਾ ਬਹੁਤ ਜਰੂਰੀ ਹੈ। ਚਲੋ ਕੁਝ ਵੱਖ-ਵੱਖ ਧਮਕੀਆਂ ਦਾ ਜਾਇਜ਼ਾ ਲਏਂ ਅਤੇ ਦੇਖੀਏ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ ਇਸਨੂੰ ਵਧੀਆ ਤਰੀਕੇ ਨਾਲ ਯੋਜਨਾ ਔਰ ਤਿਅਾਰੀ ਕਰ ਸਕਦੇ ਹੋ।

![ਧਮਕੀਆਂ ਦੀ ਸਮਝ](../../../translated_images/pa/understanding-threats.89edeada8a97fc0f.webp)

### ਟਾਸਕ ਅਤੇ ਹੁਕਮ

**ਵੇਰਵਾ:** ਹਮਲਾਵਰ AI ਏਜੰਟ ਨੂੰ ਪ੍ਰਾਂਪਟਿੰਗ ਜਾਂ ਇਨਪੁੱਟ ਨੂੰ ਠੱਗ ਕੇ ਹਦਾਇਤਾਂ ਜਾਂ ਟਾਸਕ ਦੇ ਲਕੜੇ ਬਦਲਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਨ।

**ਰੋਕਥਾਮ**: ਸੰਭਾਵਿਤ ਖਤਰਨਾਕ ਪ੍ਰਾਂਪਟਾਂ ਦੀ ਪਛਾਣ ਲਈ ਵੈਧਤਾ ਜਾਂਚ ਅਤੇ ਇਨਪੁੱਟ ਫਿਲਟਰ ਲਗਾਓ ਜੋ AI ਏਜੰਟ ਦੁਆਰਾ ਸਾਲਮਿਤ ਤੌਰ 'ਤੇ ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਹੋ। ਕਿਉਂਕਿ ਇਹ ਹਮਲੇ ਅਕਸਰ ਏਜੰਟ ਨਾਲ ਵੱਧ ਮਿਸ਼ਰਤ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਗੱਲਬਾਤ ਦੇ ਮੋੜਾਂ ਦੀ ਗਿਣਤੀ ਘਟਾਓ ਤਾਂ ਕਿ ਇਹ ਤਰ੍ਹਾਂ ਦੇ ਹਮਲੇ ਰੋਕੇ ਜਾ ਸਕਣ।

### ਜ਼ਰੂਰੀ ਸਿਸਟਮਾਂ ਤੱਕ ਪਹੁੰਚ

**ਵੇਰਵਾ:** ਜੇ AI ਏਜੰਟ ਕੋਲ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਸਟੋਰ ਕਰਨ ਵਾਲੇ ਸਿਸਟਮਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਹੈ, ਤਾ ਅਟੈਕਰ ਉਸ ਏਜੰਟ ਅਤੇ ਉਹਨਾਂ ਸੇਵਾਵਾਂ ਵਿਚਕਾਰ ਸੰਚਾਰ ਨੂੰ ਖ਼ਤਰੇ ਵਿੱਚ ਪਾ ਸਕਦੇ ਹਨ। ਇਹ ਸਿੱਧੇ ਹਮਲੇ ਹੋ ਸਕਦੇ ਹਨ ਜਾਂ ਐਜੰਟ ਤੋਂ ਰਾਹੀਂ ਉਨ੍ਹਾਂ ਸਿਸਟਮਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲੈਣ ਦੇ ਅਣਸਿੱਧੇ ਕੋਸ਼ਿਸ਼ਾਂ।

**ਰੋਕਥਾਮ**: AI ਏਜੰਟਾਂ ਨੂੰ ਸਿਸਟਮ ਤੱਕ ਸਿਰਫ਼ ਲੋੜ ਅਨੁਸਾਰ ਪਹੁੰਚ ਮਿਲਣੀ ਚਾਹੀਦੀ ਹੈ ਤਾਂ ਜੋ ਇਹ ਤਰ੍ਹਾਂ ਦੇ ਹਮਲੇ ਰੋਕੇ ਜਾ ਸਕਣ। ਏਜੰਟ ਅਤੇ ਸਿਸਟਮ ਦੇ ਵਿਚਕਾਰ ਸੰਚਾਰ ਵੀ ਸੁਰੱਖਿਅਤ ਹੋਣਾ ਮਨਾਂ ਹੈ। ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰਨਾ ਇੱਕ ਹੋਰ ਤਰੀਕਾ ਹੈ ਜੋ ਇਸ ਜਾਣਕਾਰੀ ਨੂੰ ਬਚਾਉਂਦਾ ਹੈ।

### ਸਰੋਤ ਅਤੇ ਸੇਵਾ ਓਵਰਲੋਡਿੰਗ

**ਵੇਰਵਾ:** AI ਏਜੰਟ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਕਰ ਸਕਦੇ ਹਨ ਆਪਣੀਆਂ ਨਿਯੁਕਤੀਆਂ ਪੂਰੀਆਂ ਕਰਨ ਲਈ। ਹਮਲਾਵਰ ਇਸ ਸਮਰੱਥਾ ਦਾ ਨੁਕਸਾਨ ਉਠਾ ਕੇ AI ਏਜੰਟ ਰਾਹੀਂ ਜ਼ਿਆਦਾ ਬੇਨਤੀ ਭੇਜ ਕੇ ਸੇਵਾਵਾਂ ਉੱਤੇ ਹਮਲਾ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਹੜਾ ਸਿਸਟਮ ਫੇਲ੍ਹ ਜਾਂ ਵੱਧ ਖਰਚੇ ਦਾ ਕਾਰਨ ਬਣ ਸਕਦਾ ਹੈ।

**ਰੋਕਥਾਮ:** ਸੰਸਥਾਵਾਂ ਨੂੰ ਨਿਯਮਾਂ ਨਾਲ ਸੀਮਿਤ ਕਰੋ ਕਿ AI ਏਜੰਟ ਇੱਕ ਸੇਵਾ ਨੂੰ ਕਿੰਨੀ ਵਾਰੀ ਬੇਨਤੀ ਕਰ ਸਕਦਾ ਹੈ। ਗੱਲਬਾਤ ਦੇ ਮੋੜਾਂ ਅਤੇ ਬੇਨਤੀਆਂ ਦੀ ਗਿਣਤੀ ਘਟਾਉਣਾ ਵੀ ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਦਾ ਇੱਕ ਢੰਗ ਹੈ।

### ਗਿਆਨ ਆਧਾਰ ਪ੍ਰਦੂਸ਼ਣ

**ਵੇਰਵਾ:** ਇਹ ਹਮਲਾ ਸਿੱਧਾ AI ਏਜੰਟ ਨੂੰ ਨਿਸ਼ਾਨਾ ਨਹੀਂ ਬਣਾਉਂਦਾ ਪਰ ਉਹ ਗਿਆਨ ਆਧਾਰ ਅਤੇ ਹੋਰ ਸੇਵਾਵਾਂ ਨੂੰ ਨੂਕਸਾਨ ਪਹੁੰਚਾਉਂਦਾ ਹੈ ਜੋ AI ਏਜੰਟ ਵਰਤਦਾ ਹੈ। ਇਸ ਨਾਲ ਡਾਟਾ ਜਾਂ ਜਾਣਕਾਰੀ ਖ਼ਰਾਬ ਹੋ ਸਕਦੀ ਹੈ, ਜਿਹੜਾ AI ਏਜੰਟ ਨੂੰ ਪੱਖਪਾਤੀ ਜਾਂ ਅਣਚਾਹੇ ਜਵਾਬ ਦੇਣ ਵੱਲ ਲੈ ਜਾ ਸਕਦਾ ਹੈ।

**ਰੋਕਥਾਮ:** ਉਹ ਡਾਟਾ ਜੋ AI ਏਜੰਟ ਵਰਤੇਗਾ, ਉਸ ਦੀ ਸਮੇਂ ਸਮੇਂ ਤੇ ਜਾਂਚ ਕਰੋ। ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਸ ਡਾਟਾ ਤੱਕ ਪਹੁੰਚ ਸੁਰੱਖਿਅਤ ਹੈ ਅਤੇ ਇਹ ਸਿਰਫ਼ ਭਰੋਸੇਮੰਦ ਵਿਅਕਤੀਆਂ ਦੁਆਰਾ ਹੀ ਬਦਲੀ ਜਾਵੇ ਤਾਂ ਜੋ ਇਹ ਤਰ੍ਹਾਂ ਦੇ ਹਮਲਿਆਂ ਤੋਂ ਬਚਿਆ ਜਾ ਸਕੇ।

### ਕੈਸਕੇਡਿੰਗ ਗਲਤੀਆਂ

**ਵੇਰਵਾ:** AI ਏਜੰਟ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਕਰਦੇ ਹਨ। ਹਮਲਾਵਰਾਂ ਵੱਲੋਂ ਪੈਦਾ ਕੀਤੀਆਂ ਗਲਤੀਆਂ ਹੋਰ ਸਿਸਟਮਾਂ ਦੀ ਨਾਕਾਮੀ ਦਾ ਕਾਰਣ ਬਣ ਸਕਦੀਆਂ ਹਨ, ਜਿਹੜਾ ਹਮਲੇ ਨੂੰ ਹੋਰ ਵਿਆਪਕ ਅਤੇ ਮੁਸ਼ਕਿਲ ਬਣਾਉਂਦਾ ਹੈ।

**ਰੋਕਥਾਮ**: ਇਕ ਤਰੀਕਾ ਇਹ ਹੈ ਕਿ AI ਏਜੰਟ ਨੂੰ ਸਰਵਰਾਂ ਦੀ ਸੀਮਿਤ ਵਿਵਸਥਾ ਵਿੱਚ ਚਲਾਇਆ ਜਾਵੇ, ਜਿਵੇਂ ਕਿ ਡਾਕਰ ਕੰਟੇਨਰ ਵਿੱਚ ਕੰਮ ਕਰਨਾ, ਤਾਂ ਜੋ ਸਿੱਧੇ ਸਿਸਟਮ ਹਮਲੇ ਰੋਕੇ ਜਾ ਸਕਣ। ਜਦੋਂ ਕੁਝ ਸਿਸਟਮ ਗਲਤੀ ਦਿੰਦੇ ਹਨ ਤਾਂ ਫੈਲਬੈਕ ਮਕੈਨਿਜ਼ਮ ਅਤੇ ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਵਾਲੀ ਲਾਜਿਕ ਬਣਾਉਣਾ ਵੀ ਵੱਡੇ ਸਿਸਟਮ ਫੇਲ੍ਹ ਰੋਕਣ ਦਾ ਢੰਗ ਹੈ।

## ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ

ਭਰੋਸੇਮੰਦ AI ਏਜੰਟ ਸਿਸਟਮ ਬਣਾਉਣ ਦਾ ਇਕ ਹੋਰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਤਰੀਕਾ ਹੈ ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ ਵਰਤਣਾ। ਇਹ ਇੱਕ ਐਸਾ ਪ੍ਰਕਿਰਿਆ ਬਣਾਉਂਦਾ ਹੈ ਜਿੱਥੇ ਯੂਜ਼ਰ ਰਨਿੰਗ ਦੌਰਾਨ ਏਜੰਟਾਂ ਨੂੰ ਫੀਡਬੈਕ ਦੇ ਸਕਦੇ ਹਨ। ਯੂਜ਼ਰ ਅਸਲ ਵਿੱਚ ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਵਿੱਚ ਏਜੰਟ ਵਜੋਂ ਕੰਮ ਕਰਦੇ ਹਨ ਅਤੇ ਚਲ ਰਹੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਮਨਜ਼ੂਰੀ ਜਾਂ ਸਮਾਪਤ ਕਰਦੇ ਹਨ।

![ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ](../../../translated_images/pa/human-in-the-loop.5f0068a678f62f4f.webp)

ਇੱਥੇ Microsoft Agent Framework ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਕੋਡ ਅੰਸ਼ ਹੈ ਜੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਇਹ ਸੰਕਲਪ ਕਿਵੇਂ ਲਾਗੂ ਕੀਤਾ ਗਿਆ ਹੈ:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# ਮਨੁੱਖੀ-ਇਨ-ਦ-ਲੂਪ ਮਨਜ਼ੂਰੀ ਨਾਲ ਪ੍ਰੋਵਾਈਡਰ ਬਣਾਓ
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ ਕਦਮ ਨਾਲ ਏਜੰਟ ਬਣਾਓ
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ਯੂਜ਼ਰ ਜਵਾਬ ਦੀ ਸਮੀਖਿਆ ਕਰ ਸਕਦਾ ਹੈ ਅਤੇ ਮਨਜ਼ੂਰ ਕਰ ਸਕਦਾ ਹੈ
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## ਨਤੀਜਾ

ਭਰੋਸੇਮੰਦ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਧਿਆਨਪੂਰਵਕ ਡਿਜ਼ਾਈਨ, ਮਜ਼ਬੂਤ ਸੁਰੱਖਿਆ ਉਪਾਅ ਅਤੇ ਲਗਾਤਾਰ ਸੁਧਾਰ ਜ਼ਰੂਰੀ ਹਨ। ਸੰਰਚਿਤ ਮੀਟਾ ਪ੍ਰਾਂਪਟਿੰਗ ਸਿਸਟਮ, ਸੰਭਾਵਿਤ ਧਮਕੀਆਂ ਦੀ ਸਮਝ ਅਤੇ ਰੋਕਥਾਮ ਨੀਤੀਆਂ ਨੂੰ ਲਾਗੂ ਕਰਕੇ ਡਿਵੈਲਪਰ ਐਸੇ AI ਏਜੰਟ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹਨ ਜੋ ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਦੋਵਾਂ ਹੁੰਦੇ ਹਨ। ਇਸ ਦੇ ਨਾਲ, ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ ਲਗਾਉਣ ਨਾਲ ਖਤਰੇ ਘਟਾਉਂਦੇ ਹੋਏ AI ਏਜੰਟ ਯੂਜ਼ਰ ਦੀਆਂ ਲੋੜਾਂ ਨਾਲ ਸਹਿਮਤ ਰਹਿੰਦੇ ਹਨ। ਜਿਵੇਂ ਜਿਵੇਂ AI ਵਿਕਸਿਤ ਹੁੰਦਾ ਜਾ ਰਿਹਾ ਹੈ, ਸੁਰੱਖਿਆ, ਪਰਾਈਵੇਸੀ ਅਤੇ ਨੈਤਿਕ ਮਸਲਿਆਂ 'ਤੇ ਸਤਰੰਧੀ ਰੁਖ ਰੱਖਣਾ ਭਰੋਸਾ ਅਤੇ ਭਰੋਸੇਯੋਗਤਾ ਨੂੰ ਬਣਾਈ ਰੱਖਣ ਲਈ ਅਹੰਕਾਰਪੂਰਵਕ ਹੈ।

## ਕੋਡ ਨਮੂਨੇ

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): ਮੀਟਾ-ਪ੍ਰਾਂਪਟ ਸਿਸਟਮ-ਮੈਸੇਜ ਫਰੇਮਵਰਕ ਦਾ ਕਦਮ-ਦਰ-ਕਦਮ ਪ੍ਰਦਰਸ਼ਨ।
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): ਭਰੋਸੇਮੰਦ ਏਜੰਟਾਂ ਲਈ ਪਹਿਲਾਂ ਐਕਸ਼ਨ ਮਨਜ਼ੂਰੀ ਗੇਟ, ਰਿਸਕ ਟੀਅਰਿੰਗ ਅਤੇ ਆਡਿਟ ਲੌਗਿੰਗ।

### ਭਰੋਸੇਮੰਦ AI ਏਜੰਟ ਬਣਾਉਣ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ਨਾਲ ਜੁੜੋ ਜਿੱਥੇ ਤੁਸੀਂ ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲ ਸਕਦੇ ਹੋ, ਦਫ਼ਤਰ ਘੰਟਿਆਂ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋ ਸਕਦੇ ਹੋ ਅਤੇ ਆਪਣੇ AI ਏਜੰਟ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲੈ ਸਕਦੇ ਹੋ।

## ਵਾਧੂ ਸਰੋਤ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ਜ਼ਿੰਮੇਵਾਰ AI ਦਾ ਸਿੱਖਿਆ ਬਾਰੇ ਓਵਰਵਿਊ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ਮੂਲਿਕ AI ਮਾਡਲਾਂ ਅਤੇ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਮੂਲਾਂਕਣ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ਸੁਰੱਖਿਆ ਸਿਸਟਮ ਮੈਸੇਜ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ਖਤਰਾ ਮੁਲਾਂਕਣ ਟੈਮਪਲੇਟ</a>

## ਪਿਛਲਾ ਸਬਕ

[Agentic RAG](../05-agentic-rag/README.md)

## ਅਗਲਾ ਸਬਕ

[ਪланਿੰਗ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->