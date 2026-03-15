[![ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ](../../../translated_images/pa/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਦੇਖਣ ਲਈ ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

# ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣਾ

## ਤਾਰੂਫ਼

ਇਸ ਪਾਠ ਵਿੱਚ ਵਰਤੋਂ ਕਰਾਂਗੇ:

- ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ੀਲ AI ਏਜੰਟ ਕਿਵੇਂ ਬਣਾਉਣ ਅਤੇ ਤੈਨਾਤ ਕਰਨੇ ਹਨ।
- AI ਏਜੰਟ ਵਿਕਾਸ ਦੌਰਾਨ ਜਰੂਰੀ ਸੁਰੱਖਿਆ ਖਿਆਲ।
- AI ਏਜੰਟ ਵਿਕਾਸ ਦੌਰਾਨ ਡਾਟਾ ਅਤੇ ਉਪਭੋਗਤਾ ਦੀ ਪਰਦੇਦਾਰੀ ਕਿਵੇਂ ਬਰਕਰਾਰ ਰੱਖਣੀ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਹਾਨੂੰ ਇਹ ਪਤਾ ਹੋਵੇਗਾ ਕਿ:

- AI ਏਜੰਟ ਬਣਾਉਂਦੇ ਸਮੇਂ ਖਤਰਿਆਂ ਦੀ ਪਹਚਾਣ ਅਤੇ ਰੋਕਥਾਮ ਕਿਵੇਂ ਕਰਨੀ ਹੈ।
- ਡਾਟਾ ਅਤੇ ਪਹੁੰਚ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲਣ ਲਈ ਸੁਰੱਖਿਆ ਕਦਮ ਕਿਵੇਂ ਲਾਗੂ ਕਰਨੇ ਹਨ।
- ਐਸੇ AI ਏਜੰਟ ਬਣਾਉਣ ਜੋ ਡਾਟਾ ਪਰਦੇਦਾਰੀ ਬਣਾਈ ਰੱਖਣ ਅਤੇ ਉਪਭੋਗਤਾ ਨੂੰ ਕੁਆਲਟੀਤਾ ਭਰਪੂਰ ਤਜਰਬਾ ਦੇਣ।

## ਸੁਰੱਖਿਆ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਆਓ ਸੁਰੱਖਿਅਤ ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਬਾਰੇ ਜਾਣੀਏ। ਸੁਰੱਖਿਆ ਦਾ ਅਰਥ ਹੈ ਕਿ AI ਏਜੰਟ ਆਪਣੇ ਡਿਜ਼ਾਈਨ ਅਨੁਸਾਰ ਕੰਮ ਕਰੇ। ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਨਿਰਮਾਤਾ ਵਜੋਂ ਸਾਡੇ ਕੋਲ ਇਸ ਸੁਰੱਖਿਆ ਨੂੰ ਵਧਾਉਣ ਲਈ ਤਰੀਕੇ ਅਤੇ ਟੂਲ ਹਨ:

### ਸਿਸਟਮ ਸੁਨੇਹਾ ਫ੍ਰੇਮਵਰਕ ਬਣਾਉਣਾ

ਜੇ ਤੁਸੀਂ ਕਦੇ Large Language Models (LLMs) ਵਰਤ ਕੇ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਜਾਣਦੇ ਹੋ ਕਿ ਇੱਕ ਮਜ਼ਬੂਤ ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਜਾਂ ਸਿਸਟਮ ਸੁਨੇਹਾ ਦੀ ਡਿਜ਼ਾਈਨਿੰਗ ਕਿੰਨੀ ਜ਼ਰੂਰੀ ਹੈ। ਇਹ ਪ੍ਰੋੰਪਟ ਮੈਟਾ ਨਿਯਮ, ਹੁਕਮ, ਅਤੇ ਹਦਾਇਤਾਂ ਸਥਾਪਤ ਕਰਦੇ ਹਨ ਕਿ LLM ਉਪਭੋਗਤਾ ਅਤੇ ਡਾਟਾ ਨਾਲ ਕਿਵੇਂ ਗੱਲਬਾਤ ਕਰੇਗਾ।

AI ਏਜੰਟਾਂ ਲਈ ਇਹ ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਹੋਰ ਵੀ ਜ਼ਿਆਦਾ ਮਹੱਤਵਪੂਰਣ ਹੁੰਦਾ ਹੈ ਕਿਉਂਕਿ ਇਹਨਾਂ ਨੂੰ ਬਿਲਕੁਲ ਵਿਸ਼ੇਸ਼ ਹਦਾਇਤਾਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ ਤਾਂ ਜੋ ਉਹ ਸਾਡੇ द्वारा ਡਿਜ਼ਾਇਨ ਕੀਤੇ ਕੰਮ ਪੂਰੇ ਕਰ ਸਕਣ।

ਸਕੈਲਬਲ ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਬਣਾਉਣ ਲਈ, ਅਸੀਂ ਆਪਣੀ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਇੱਕ ਜਾਂ ਵੱਧ ਏਜੰਟਾਂ ਨੂੰ ਬਣਾਉਣ ਦੇ ਲਈ ਸਿਸਟਮ ਸੁਨੇਹਾ ਫ੍ਰੇਮਵਰਕ ਵਰਤ ਸਕਦੇ ਹਾਂ:

![ਸਿਸਟਮ ਸੁਨੇਹਾ ਫ੍ਰੇਮਵਰਕ ਬਣਾਉਣਾ](../../../translated_images/pa/system-message-framework.3a97368c92d11d68.webp)

#### ਕਦਮ 1: ਮੈਟਾ ਸਿਸਟਮ ਸੁਨੇਹਾ ਬਣਾਓ

ਮੈਟਾ ਪ੍ਰੋੰਪਟ ਇੱਕ LLM ਵੱਲੋਂ ਏਜੰਟਾਂ ਲਈ ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ। ਅਸੀਂ ਇਸ ਨੂੰ ਇਕ ਟੈਮਪਲੇਟ ਵਜੋਂ ਡਿਜ਼ਾਇਨ ਕਰਦੇ ਹਾਂ ਤਾਂ ਜੋ ਜਰੂਰਤ ਪੈਣ 'ਤੇ ਪ੍ਰਭਾਵਸ਼ੀਲ ਤਰੀਕੇ ਨਾਲ ਕਈ ਏਜੰਟ ਬਣਾਇਆ ਜਾ ਸਕੇ।

ਇੱਥੇ ਇੱਕ ਮੈਟਾ ਸਿਸਟਮ ਸੁਨੇਹਾ ਦੀ ਉਦਾਹਰਨ ਹੈ ਜੋ ਅਸੀਂ LLM ਨੂੰ ਦੇਣਾ ਚਾਹੁੰਦੇ ਹਾਂ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ਕਦਮ 2: ਬੁਨਿਆਦੀ ਪ੍ਰੋੰਪਟ ਬਣਾਓ

ਅਗਲਾ ਕਦਮ ਇਹ ਹੈ ਕਿ ਇੱਕ ਬੁਨਿਆਦੀ ਪ੍ਰੋੰਪਟ ਬਣਾਇਆ ਜਾਵੇ ਜੋ AI ਏਜੰਟ ਦਾ ਵਰਣਨ ਕਰੇ। ਤੁਹਾਨੂੰ ਏਜੰਟ ਦੀ ਭੂਮਿਕਾ, ਜੋ ਕੰਮ ਏਜੰਟ ਪੂਰੇ ਕਰੇਗਾ, ਅਤੇ ਹੋਰ ਜਿੰਮੇਵਾਰੀਆਂ ਸ਼ਾਮਲ ਕਰਨੀ ਚਾਹੀਦੀਆਂ ਹਨ।

ਇਹਾਂ ਇੱਕ ਉਦਾਹਰਨ ਹੈ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ਕਦਮ 3: LLM ਨੂੰ ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਸੁਨੇਹਾ ਦਿਓ

ਹੁਣ ਅਸੀਂ ਇਸ ਸਿਸਟਮ ਸੁਨੇਹਾ ਨੂੰ ਬਿਹਤਰ ਬਣਾ ਸਕਦੇ ਹਾਂ ਜਦੋਂ ਅਸੀਂ ਮੈਟਾ ਸਿਸਟਮ ਸੁਨੇਹਾ ਅਤੇ ਸਾਡਾ ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਸੁਨੇਹਾ ਦਿੰਦੇ ਹਾਂ।

ਇਸ ਨਾਲ ਇੱਕ ਐਸਾ ਸਿਸਟਮ ਸੁਨੇਹਾ ਤਿਆਰ ਹੋਵੇਗਾ ਜੋ ਸਾਡੇ AI ਏਜੰਟਾਂ ਨੂੰ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਮਾਰਗਦਰਸ਼ਨ ਕਰਨ ਵਿੱਚ ਮਦਦਗਾਰ ਹੋਵੇਗਾ:

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

#### ਕਦਮ 4: ਦੁਹਰਾਉ ਅਤੇ ਸੁਧਾਰ ਕਰੋ

ਇਸ ਸਿਸਟਮ ਸੁਨੇਹਾ ਫ੍ਰੇਮਵਰਕ ਦੀ ਕੀਮਤ ਇਹ ਹੈ ਕਿ ਇਸ ਨਾਲ ਵੱਖ-ਵੱਖ ਏਜੰਟਾਂ ਲਈ ਸਿਸਟਮ ਸੁਨੇਹੇ ਬਣਾਉਣਾ ਤੇਜ਼ ਅਤੇ ਆਸਾਨ ਹੋ ਜਾਂਦਾ ਹੈ ਅਤੇ ਸਮੇਂ ਨਾਲ ਆਪਣੇ ਸਿਸਟਮ ਸੁਨੇਹੇ ਨੂੰ ਸੁਧਾਰਣਾ ਵੀ ਸੰਭਵ ਹੁੰਦਾ ਹੈ। ਪਹਿਲੀ ਵਾਰੀ ਵਧੀਆ ਕੰਮ ਕਰਨ ਵਾਲਾ ਸਿਸਟਮ ਸੁਨੇਹਾ ਲੱਭਣਾ ਸਾਨੂੰ ਕਮ ਹੀ ਮਿਲਦਾ ਹੈ। ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਸੁਨੇਹੇ ਵਿੱਚ ਛੋਟੇ ਟਵਿੱਟ ਕਰਨ ਅਤੇ ਸਿਸਟਮ ਵਿੱਚ ਚਲਾਉਣ ਨਾਲ ਤੁਸੀਂ ਨਤੀਜੇ ਤੁਲਨਾ ਅਤੇ ਮੁਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹੋ।

## ਖਤਰਿਆਂ ਦੀ ਸਮਝ

ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ, ਇਹ ਜਰੂਰੀ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੀ AI ਏਜੰਟ ਨੂੰ ਹੋ ਸਕਣ ਵਾਲੇ ਖਤਰਿਆਂ ਅਤੇ ਧਮਕੀਆਂ ਨੂੰ ਸਮਝੋ ਅਤੇ ਰੋਕਥਾਮ ਕਰੋ। ਆਓ ਕੁਝ ਖਾਸ ਖਤਰਿਆਂ ਨੂੰ ਦੇਖੀਏ ਅਤੇ ਇਹ ਕਿ ਤੁਸੀਂ ਇਨ੍ਹਾਂ ਲਈ ਕਿਵੇਂ ਪੂਰੀ ਤਿਆਰੀ ਕਰ ਸਕਦੇ ਹੋ।

![ਖਤਰਿਆਂ ਦੀ ਸਮਝ](../../../translated_images/pa/understanding-threats.89edeada8a97fc0f.webp)

### ਕੰਮ ਅਤੇ ਹਦਾਇਤ

**ਵੇਰਵਾ:** ਹਮਲਾਵਰ ਪ੍ਰੋੰਪਟਿੰਗ ਜਾਂ ਇਨਪੁਟਸ ਨੂੰ ਮਾਨਿਪੂਲੇਟ ਕਰਕੇ AI ਏਜੰਟ ਦੇ ਹਦਾਇਤਾਂ ਜਾਂ ਨਿਸ਼ਾਨਿਆਂ ਨੂੰ ਬਦਲਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਨ।

**ਰੋਕਥਾਮ**: ਸੰਭਾਵਿਤ ਖਤਰਨਾਕ ਪ੍ਰੋੰਪਟਾਂ ਦੀ ਪਹਚਾਣ ਲਈ ਵੈਰੀਫਿਕੇਸ਼ਨ ਚੈੱਕ ਅਤੇ ਇਨਪੁਟ ਫਿਲਟਰ ਲਗਾਓ। ਕਿਉਂਕਿ ਇਹ ਹਮਲੇ ਆਮ ਤੌਰ 'ਤੇ ਏਜੰਟ ਨਾਲ ਬਾਰੰਬਾਰ ਗੱਲਬਾਤ ਮੰਗਦੇ ਹਨ, ਗੱਲਬਾਤ ਵਿੱਚ ਗਿਣਤੀ ਘਟਾ ਕੇ ਇਨ੍ਹਾਂ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕਦਾ ਹੈ।

### ਸੰਵੇਦਨਸ਼ੀਲ ਸਿਸਟਮਾਂ ਤੱਕ ਪਹੁੰਚ

**ਵੇਰਵਾ**: ਜੇਕਰ AI ਏਜੰਟ ਕੋਲ ਉਹ ਸਿਸਟਮ ਅਤੇ ਸੇਵਾਵਾਂ ਦਾ ਪਹੁੰਚ ਹੈ ਜਿੱਥੇ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਰੱਖਿਆ ਗਿਆ ਹੈ, ਤਾਂ ਹਮਲਾਵਰ ਏਜੰਟ ਅਤੇ ਇਨ੍ਹਾਂ ਸੇਵਾਵਾਂ ਵਿਚਕਾਰ ਸੰਚਾਰ ਨੂੰ ਖ਼ਤਰੇ ਵਿੱਚ ਪਾਵਣਗੇ। ਇਹ ਸਿੱਧੇ ਹਮਲੇ ਜਾਂ ਇੰਡੀਰੈਕਟ ਜ਼ਰੀਏ ਹੰਮਲਿਆਂ ਜਿਵੇਂ ਜਾਣਕਾਰੀ ਇਕੱਠਾ ਕਰਨ ਵਾਲੀਆਂ ਕੋਸ਼ਿਸ਼ਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ।

**ਰੋਕਥਾਮ:** AI ਏਜੰਟਾਂ ਨੂੰ ਸਿਰਫ਼ ਜਰੂਰੀ ਜਗ੍ਹਾ ਤੇ ਪਹੁੰਚ ਦੇਨਾ ਚਾਹੀਦਾ ਹੈ। ਏਜੰਟ ਅਤੇ ਸਿਸਟਮ ਦਾ ਸੰਚਾਰ ਵੀ ਸੁਰੱਖਿਅਤ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਅਥੈਂਟੀਕੇਸ਼ਨ ਅਤੇ ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਲਗਾਉਣਾ ਵੀ ਇਸ ਜਾਣਕਾਰੀ ਦੀ ਸੁਰੱਖਿਆ ਲਈ ਜ਼ਰੂਰੀ ਹੈ।

### ਸਰੋਤ ਅਤੇ ਸੇਵਾ ਓਵਰਲੋਡਿੰਗ

**ਵੇਰਵਾ:** AI ਏਜੰਟ ਵੱਖ-ਵੱਖ ਟੂਲ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਰੱਖਦੇ ਹਨ ਤਾਂ ਜੋ ਕੰਮ ਸਿਰੇ ਚੜ੍ਹਾ ਸਕਣ। ਹਮਲਾਵਰ ਇਸ ਖੁਬੀ ਨੂੰ ਵਰਤ ਕੇ AI ਏਜੰਟ ਰਾਹੀਂ ਬਹੁਤ ਸਾਰੇ ਬੇਨਤੀਆਂ ਭੇਜ ਕੇ ਸੇਵਾਵਾਂ 'ਤੇ ਹਮਲਾ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਕਰਕੇ ਸਿਸਟਮ ਫੇਲ ਹੋ ਸਕਦਾ ਹੈ ਜਾਂ ਖਰਚ ਜ਼ਿਆਦਾ ਹੋ ਸਕਦਾ ਹੈ।

**ਰੋਕਥਾਮ:** ਇਹ ਨੀਤੀ ਬਨਾਓ ਕਿ AI ਏਜੰਟ ਕਿਸੇ ਸੇਵਾ ਨੂੰ ਕਿੰਨੇ ਬੇਨਤੀਆਂ ਭੇਜ ਸਕਦਾ ਹੈ। ਆਪਣੇ AI ਏਜੰਟ ਲਈ ਗੱਲਬਾਤ ਦੇ ਚੱਲਦੇ ਮੋੜਾਂ ਅਤੇ ਬੇਨਤੀਆਂ ਦੀ ਗਿਣਤੀ ਸੀਮਿਤ ਕਰਨ ਦਾ ਹੋਰ ਇੱਕ ਤਰੀਕਾ ਹੈ।

### ਗਿਆਨ ਅਧਾਰ ਵਿਸ਼ਾਕਤਕਰਨ

**ਵੇਰਵਾ:** ਇਹ ਹਮਲਾ ਸਿੱਧਾ AI ਏਜੰਟ ਨੂੰ ਲਕੜਾ ਨਹੀਂ ਹਾਣਦਾ, ਬਲਕਿ ਉਹ ਗਿਆਨ ਅਧਾਰ ਅਤੇ ਹੋਰ ਸੇਵਾਵਾਂ ਨੂੰ ਨਿਸ਼ਾਨਾ ਬਣਾਉਂਦਾ ਹੈ ਜਿਹੜੀਆਂ AI ਏਜੰਟ ਕੰਮ ਮੁਕੰਮਲ ਕਰਨ ਲਈ ਵਰਤੇਗਾ। ਇਹ ਡਾਟੇ ਜਾਂ ਜਾਣਕਾਰੀ ਨੂੰ ਕਰਪਟ ਕਰਕੇ ਉਪਭੋਗਤਾ ਨੂੰ ਪੇਂਟ ਅਥਵਾ ਗਲਤ ਜਵਾਬ ਦੇ ਸਕਦਾ ਹੈ।

**ਰੋਕਥਾਮ:** ਅਕਸਰ ਗਤੀਵਿਧੀ ਦੁਆਰਾ AI ਏਜੰਟ ਵਰਤੇ ਜਾਣ ਵਾਲੇ ਡਾਟੇ ਦੀ ਜਾਂਚ ਕਰੋ। ਇਹ ਸੁਨਿਸ਼ਚਿਤ ਕਰੋ ਕਿ ਇਸ ਡਾਟੇ ਤੱਕ ਪਹੁੰਚ ਸਿਰਫ਼ ਭਰੋਸੇਮੰਦ ਲੋਕਾਂ ਨੂੰ ਹੀ ਹੈ ਤੇ ਡਾਟਾ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖੋ ਤਾਂ ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਦੀ ਹਮਲੇ ਰੋਕ ਸਕੀਏ।

### ਚੇਨ ਉਲਟ ਆਪਣੇ ਆਪ ਨੁਕਸਾਨ ਪਹੁੰਚਾਉਂਦੀਆਂ

**ਵੇਰਵਾ:** AI ਏਜੰਟ ਵੱਖ-ਵੱਖ ਟੂਲ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਰੱਖਦੇ ਹਨ। ਹਮਲਾਵਰ ਵੱਲੋਂ ਪੈਦਾ ਗਈਆਂ ਗਲਤੀਆਂ ਹੋਰ ਸਿਸਟਮਾਂ ਨੂੰ ਵੀ ਪ੍ਰਭਾਵਿਤ ਕਰਦੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਹਮਲਾ ਵਧਦਾ ਹੈ ਤੇ ਸਮੱਸਿਆ ਹੱਲ ਕਰਨਾ ਮੁਸ਼ਕਿਲ ਹੁੰਦਾ ਹੈ।

**ਰੋਕਥਾਮ:** ਇੱਕ ਤਰੀਕਾ ਇਹ ਹੈ ਕਿ AI ਏਜੰਟਨੂੰ ਇੱਕ ਸੀਮਿਤ ਮਾਹੌਲ ਵਿੱਚ ਟਾਸਕ ਕਰਨ ਲਈ ਰੱਖੋ, ਜਿਵੇਂ ਕਿ Docker ਕੰਟੇਨਰ ਵਿੱਚ ਕੰਮ ਕਰਨਾ, ਤਾਂ ਜੋ ਸਿੱਧੇ ਸਿਸਟਮ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਿਆ ਜਾ ਸਕੇ। ਜਦੋਂ ਕੁਝ ਸਿਸਟਮ ਦੋਸ਼ ਦਿੱਂਦੇ ਹਨ ਤਾਂ ਬੈਕਅੱਪ ਮਕੈਨਿਜ਼ਮ ਅਤੇ ਰਿਟ੍ਰਾਈ ਲੌਜਿਕ ਬਣਾਉਣਾ ਵੀ ਵੱਡੇ ਨੁਕਸਾਨ ਤੋਂ ਬਚਾਉਂਦਾ ਹੈ।

## ਮਨੁੱਖ-ਸਮਿਲਿਤ ਲੂਪ

ਭਰੋਸੇਮੰਦ AI ਏਜੰਟ ਸਿਸਟਮ ਬਣਾਉਣ ਦਾ ਇਕ ਹੋਰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਤਰੀਕਾ ਮਨੁੱਖ-ਸਮਿਲਿਤ ਲੂਪ ਵਰਤਣਾ ਹੈ। ਇਹ ਪ੍ਰਕਿਰਿਆ ਬਣਾਉਂਦੀ ਹੈ ਜਿਸ ਵਿੱਚ ਉਪਭੋਗਤਾ ਰੁਜ਼ਾਨਾ ਦੌਰਾਨ ਏਜੰਟਾਂ ਨੂੰ ਫੀਡਬੈਕ ਦੇ ਸਕਦੇ ਹਨ। ਉਪਭੋਗਤਾ ਬਹੁ-ਏਜੰਟ ਸਿਸਟਮ ਵਿੱਚ ਏਜੰਟ ਵਾਂਗੋਂ ਕੰਮ ਕਰਦੇ ਹਨ ਅਤੇ ਚੱਲ ਰਹੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਮਨਜ਼ੂਰੀ ਜਾਂ ਖਤਮ ਕਰ ਸਕਦੇ ਹਨ।

![ਮਨੁੱਖ-ਸਮਿਲਿਤ ਲੂਪ](../../../translated_images/pa/human-in-the-loop.5f0068a678f62f4f.webp)

ਇੱਥੇ Microsoft Agent Framework ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ ਇਸ ਵਿਚਾਰ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਇੱਕ ਕੋਡ ਸ్నਿੱਪੇਟ ਦਿੱਤਾ ਹੈ:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# ਮਨੁੱਖੀ-ਇੰਟਰਵਾਲ ਮਨਜ਼ੂਰੀ ਦੇ ਨਾਲ ਪ੍ਰਦਾਤਾ ਬਣਾਓ
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ ਕਦਮ ਨਾਲ ਏਜੰਟ ਬਣਾਓ
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ਉਪਭੋਗਤਾ ਜਵਾਬ ਨੂੰ ਸਮੀਖਿਆ ਅਤੇ ਮਨਜ਼ੂਰ ਕਰ ਸਕਦਾ ਹੈ
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## ਨਤੀਜਾ

ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਸਾਵਧਾਨ ਡਿਜ਼ਾਈਨ, ਮਜ਼ਬੂਤ ਸੁਰੱਖਿਆ ਕਦਮ ਅਤੇ ਲਗਾਤਾਰ ਸੁਧਾਰ ਜਰੂਰੀ ਹਨ। ਢੰਗ ਨਾਲ ਬਣਾਏ ਗਏ ਮੈਟਾ ਪ੍ਰੋੰਪਟਿੰਗ ਸਿਸਟਮ, ਸੰਭਾਵਿਤ ਖਤਰਿਆਂ ਦੀ ਸਮਝ ਅਤੇ ਉਨਾਂ ਦੀ ਰੋਕਥਾਮ ਲਈ ਯੋਜਨਾਵਾਂ ਲਗਾਉਣ ਨਾਲ ਵਿਕਾਸਕਾਰ ਅਜਿਹੇ AI ਏਜੰਟ ਬਣਾਉਂਦੇ ਹਨ ਜੋ ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ੀਲ ਹੁੰਦੇ ਹਨ। ਇਸਦੇ ਨਾਲ ਮਨੁੱਖ-ਸਮਿਲਿਤ ਲੂਪ ਦੇ ਉਦਯੋਗ ਨੂੰ ਸ਼ਾਮਿਲ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ AI ਏਜੰਟ ਉਪਭੋਗਤਾ ਦੀਆਂ ਲੋੜਾਂ ਦੇ ਅਨੁਕੂਲ ਰਹਿਣ ਅਤੇ ਜੋਖਮ ਘਟਾਵੇ। ਜਿਵੇਂ-ਜਿਵੇਂ AI ਅੱਗੇ ਵੱਧ ਰਿਹਾ ਹੈ, ਸੁਰੱਖਿਆ, ਪਰਦੇਦਾਰੀ, ਅਤੇ ਨੈਤਿਕ ਪੱਖਾਂ 'ਤੇ ਸਕ੍ਰਿਯ ਰਹਿਣਾ ਭਰੋਸਾ ਅਤੇ ਵਿਸ਼ਵਾਸੀਯੋਗਤਾ ਬਣਾਉਣ ਲਈ ਜ਼ਰੂਰੀ ਹੈ।

### ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ ਬਾਰੇ ਹੋਰ ਸਵਾਲ?

ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲਣ ਲਈ, ਦਫ਼ਤਰ ਦੇ ਸਮੇਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਣ ਲਈ ਅਤੇ ਆਪਣੇ AI ਏਜੰਟ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲੈਣ ਲਈ [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ।

## ਵਾਧੂ ਸਾਧਨ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ਜ਼ਿੰਮੇਵਾਰ AI ਦਾ ਸਰਵੇਖਣ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ਜਨਰਲ AI ਮਾਡਲਾਂ ਅਤੇ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਮੁਲਾਂਕਣ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ਸੁਰੱਖਿਆ ਸਿਸਟਮ ਸੁਨੇਹੇ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ਖਤਰੇ ਦੀ ਮੂਲਾਂਕਣ ਟੈਮਪਲੇਟ</a>

## ਪਿਛਲਾ ਪਾਠ

[Agentic RAG](../05-agentic-rag/README.md)

## ਅਗਲਾ ਪਾਠ

[ਯੋਜਨਾ ਬਣਾਉਣ ਦਾ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਅਨੁਵਾਦ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਉਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫ਼ਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->