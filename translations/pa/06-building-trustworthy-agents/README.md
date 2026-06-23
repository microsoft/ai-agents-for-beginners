[![Trustworthy AI Agents](../../../translated_images/pa/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਦੇਖਣ ਲਈ ਉਪਰ ਦਿਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

# ਭਰੋਸੇਮੰਦ AI ਏਜੈਂਟਸ ਬਣਾਉਣਾ

## ਪਰਿਚਯ

ਇਹ ਪਾਠ ਸਮੇਤਿਆਵੇਗਾ:

- ਕਿਵੇਂ ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ালী AI ਏਜੈਂਟਸ ਬਣਾਏ ਅਤੇ ਤੈਨਾਤ ਕਰੇ
- AI ਏਜੈਂਟ ਬਣਾਉਂਦੇ ਸਮੇਂ ਮਹਤਵਪੂਰਨ ਸੁਰੱਖਿਆ ਵਿਚਾਰ
- AI ਏਜੈਂਟ ਵਿਕਾਸ ਦੌਰਾਨ ਡਾਟਾ ਅਤੇ ਯੂਜ਼ਰ ਦੀ ਪਰਦਰਸ਼ਿਤਾ ਕਿਵੇਂ ਬਣਾਈ ਰੱਖੀ ਜਾ ਸਕਦੀ ਹੈ

## ਸਿੱਖਣ ਦੇ ਲੱਖੇ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਜਾਣੋਗੇ:

- AI ਏਜੈਂਟਸ ਬਣਾਉਣ ਵੇਲੇ ਖਤਰੇ ਪਹਿਚਾਣਨਾ ਅਤੇ ਘਟਾਉਣਾ
- ਵਿਵਸਥਿਤ ਤਰੀਕੇ ਨਾਲ ਡਾਟਾ ਅਤੇ ਐਕਸੈਸ ਦੀ ਸੁਰੱਖਿਆ ਲਈ ਉਪਾਈ ਕਰਨਾ
- ਐਸੇ AI ਏਜੈਂਟਸ ਤਿਆਰ ਕਰਨਾ ਜੋ ਡਾਟਾ ਪਰਦਰਸ਼ਿਤਾ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਣ ਅਤੇ ਗੁਣਵੱਤਾ ਵਾਲਾ ਯੂਜ਼ਰ ਅਨੁਭਵ ਮੁਹੱਈਆ ਕਰਨ

## ਸੁਰੱਖਿਆ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਆਓ ਸੁਰੱਖਿਅਤ ਏਜੈਂਟਿਕ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਬਾਰੇ ਵੇਖੀਏ। ਸੁਰੱਖਿਆ ਦਾ ਮਤਲਬ ਹੈ ਕਿ AI ਏਜੈਂਟ ਆਪਣਾ ਕੰਮ ਢੰਗ ਨਾਲ ਕਰਦਾ ਹੈ। ਏਜੈਂਟਿਕ ਐਪਲੀਕੇਸ਼ਨ੍ਹਾਂ ਦੇ ਨਿਰਮਾਤਾ ਵਜੋਂ ਸਾਨੂੰ ਸੁਰੱਖਿਆ ਵਧਾਉਣ ਲਈ ਤਰੀਕੇ ਅਤੇ ਟੂਲ ਮਿਲਦੇ ਹਨ:

### ਸਿਸਟਮ ਮੇਸੇਜ ਫ੍ਰੇਮਵਰਕ ਬਣਾਉਣਾ

ਜੇ ਤੁਸੀਂ ਕਦੇ ਵੀ ਲਾਰਜ ਲੈਂਗਵੇਜ ਮਾਡਲਜ਼ (LLMs) ਨੂੰ ਵਰਤ ਕੇ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਇਆ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਜਾਣਦੇ ਹੋ ਕਿ ਇੱਕ ਮਜ਼ਬੂਤ ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਜਾਂ ਸਿਸਟਮ ਮੇਸੇਜ ਕਿਵੇਂ ਡਿਜ਼ਾਇਨ ਕਰਨਾ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਇਹ ਪ੍ਰੋੰਪਟ LLM ਨੂੰ ਯੂਜ਼ਰ ਅਤੇ ਡਾਟਾ ਨਾਲ ਕਿਵੇਂ ਸੰਚਾਰ ਕਰਨਾ ਹੈ, ਇਸ ਲਈ ਮੈਟਾ ਨਿਯਮ, ਹੁਕਮ ਅਤੇ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ ਸੈੱਟ ਕਰਦੇ ਹਨ।

AI ਏਜੈਂਟਸ ਲਈ, ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਹੋਰ ਵੀ ਜ਼ਿਆਦਾ ਮਹੱਤਵਪੂਰਨ ਹੁੰਦਾ ਹੈ ਕਿਉਂਕਿ AI ਏਜੈਂਟਸ ਨੂੰ ਉਹ ਟਾਸਕ ਪੂਰੇ ਕਰਨ ਲਈ ਬਹੁਤ ਵਿਸ਼ੇਸ਼ ਹੁਕਮਾਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ ਜੋ ਅਸੀਂ ਉਨ੍ਹਾਂ ਲਈ ਤੈਅ ਕਰਦੇ ਹਾਂ।

ਵੱਧਿਆ ਪ੍ਰਮਾਣ ਵਿੱਚ ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਬਣਾਉਣ ਲਈ, ਅਸੀਂ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਇੱਕ ਜਾਂ ਵੱਧ ਏਜੈਂਟਸ ਬਣਾਉਣ ਲਈ ਸਿਸਟਮ ਮੇਸੇਜ ਫ੍ਰੇਮਵਰਕ ਵਰਤ ਸਕਦੇ ਹਾਂ:

![Building a System Message Framework](../../../translated_images/pa/system-message-framework.3a97368c92d11d68.webp)

#### ਕਦਮ 1: ਮੈਟਾ ਸਿਸਟਮ ਮੇਸੇਜ ਬਣਾਉਣਾ

ਮੈਟਾ ਪ੍ਰੋੰਪਟ ਨੂੰ LLM ਵਰਤ ਕੇ ਉਨ੍ਹਾਂ ਏਜੈਂਟਾਂ ਲਈ ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਤਿਆਰ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ ਜੋ ਅਸੀਂ ਬਣਾਉਂਦੇ ਹਾਂ। ਅਸੀਂ ਇਸਨੂੰ ਐਸਾ ਟੈਮਪਲੇਟ ਬਣਾਉਂਦੇ ਹਾਂ ਤਾਂ ਜੋ ਜਰੂਰਤ ਪੈਣ ਤੇ ਅਸੀਂ ਅਸਾਨੀ ਨਾਲ ਕਈ ਏਜੈਂਟਸ ਬਣਾ ਸਕੀਏ।

ਇੱਥੇ ਇੱਕ ਮਿਸਾਲ ਹੈ ਮੈਟਾ ਸਿਸਟਮ ਮੇਸੇਜ ਦੀ ਜੋ ਅਸੀਂ LLM ਨੂੰ ਦੇਵਾਂਗੇ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ਕਦਮ 2: ਇੱਕ ਬੁਨਿਆਦੀ ਪ੍ਰੋੰਪਟ ਬਣਾਉਣਾ

ਅਗਲਾ ਕਦਮ ਹੈ AI ਏਜੈਂਟ ਦਾ ਵੇਰਵਾ ਦੇਣ ਵਾਲਾ ਇਕ ਸਧਾਰਣ ਪ੍ਰੋੰਪਟ ਬਣਾਉਣਾ। ਤੁਹਾਨੂੰ ਏਜੈਂਟ ਦਾ ਭੂਮਿਕਾ, ਉਸਦੇ ਮੁੱਖ ਕੰਮਾਂ ਅਤੇ ਹੋਰ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਨੂੰ ਸ਼ਾਮਿਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।

ਇਹ ਇੱਕ ਉਦਾਹਰਣ ਹੈ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ਕਦਮ 3: LLM ਨੂੰ ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਮੇਸੇਜ ਦਿਓ

ਹੁਣ ਅਸੀਂ ਇਸ ਸਿਸਟਮ ਮੇਸੇਜ ਨੂੰ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ ਮੈਟਾ ਸਿਸਟਮ ਮੇਸੇਜ ਅਤੇ ਸਾਡਾ ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਮੇਸੇਜ ਸ਼ਾਮਿਲ ਹੋਵੇਗਾ।

ਇਸ ਨਾਲ ਇਕ ਸਿਸਟਮ ਮੇਸੇਜ ਬਣੇਗਾ ਜੋ ਸਾਡੇ AI ਏਜੈਂਟਾਂ ਨੂੰ ਲੀਡ ਕਰਨ ਲਈ ਬਿਹਤਰ ਤਰੀਕੇ ਨਾਲ ਡਿਜ਼ਾਇਨ ਕੀਤਾ ਗਿਆ ਹੈ:

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

ਇਸ ਸਿਸਟਮ ਮੇਸੇਜ ਫ੍ਰੇਮਵਰਕ ਦਾ ਮੁੱਲ ਇਹ ਹੈ ਕਿ ਕਈ ਏਜੈਂਟਾਂ ਲਈ ਸਿਸਟਮ ਮੇਸੇਜ ਬਣਾਉਣਾ ਅਸਾਨ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ ਸਮੇਂ ਦੇ ਨਾਲ ਆਪਣੇ ਸਿਸਟਮ ਮੇਸੇਜ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ ਕਦਰ ਨੈтері ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲੀ ਵਾਰ ਤੁਹਾਡੇ ਪੂਰੇ ਵਰਤੋਂ ਕੇਸ ਲਈ ਸਹੀ ਸਿਸਟਮ ਮੇਸੇਜ ਹੋਵੇ। ਛੋਟੇ-ਛੋਟੇ ਤਬਦੀਲੀ ਅਤੇ ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਮੇਸੇਜ ਨੂੰ ਬਦਲ ਕੇ ਅਤੇ ਦੁਬਾਰਾ ਸਿਸਟਮ ਰਾਹੀਂ ਚਲਾਕੇ ਤੁਸੀਂ ਨਤੀਜੇ ਤੁਲਨਾ ਅਤੇ ਮੱਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹੋ।

## ਖਤਰਨਾਂ ਨੂੰ ਸਮਝਣਾ

ਭਰੋਸੇਮੰਦ AI ਏਜੈਂਟ ਬਣਾਉਣ ਲਈ, ਤੁਹਾਡੇ AI ਏਜੈਂਟ ਲਈ ਖਤਰਿਆਂ ਅਤੇ ਖਤਰਨਾਂ ਨੂੰ ਸਮਝਣਾ ਅਤੇ ਘਟਾਉਣਾ ਬਹੁਤ ਜ਼ਰੂਰੀ ਹੈ। ਆਓ ਕੁਝ ਵੱਖ-ਵੱਖ ਖਤਰਨਾਂ ਤੇ ਨਜ਼ਰ ਮਾਰੀਏ ਜਿਹੜੇ AI ਏਜੈਂਟਸ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਤੁਸੀਂ ਕਿਵੇਂ ਵਧੀਆ ਯੋਜਨਾ ਬਣਾ ਸਕਦੇ ਹੋ ਅਤੇ ਤਿਆਰ ਰਹਿ ਸਕਦੇ ਹੋ।

![Understanding Threats](../../../translated_images/pa/understanding-threats.89edeada8a97fc0f.webp)

### ਟਾਸਕ ਅਤੇ ਹਦੀਏਤਾਂ

**ਵਰਣਨ:** ਹਮਲਾਵਰ AI ਏਜੈਂਟ ਦੀ ਹਦਾਇਤਾਂ ਜਾਂ ਟੀਚਿਆਂ ਨੂੰ ਪ੍ਰੋੰਪਟਿੰਗ ਜਾਂ ਇનਪੁਟਾਂ ਨੂੰ ਠੱਗ ਕੇ ਬਦਲਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਨ।

**ਘਟਾਉਣਾ**: ਜ਼ਰੂਰੀ ਚੈਕ ਅਤੇ ਇਨਪੁਟ ਫਿਲਟਰ ਲਗਾਓ ਤਾਂ ਜੋ ਸੰਭਾਵਿਤ ਖ਼ਤਰਨਾਕ ਪ੍ਰੋੰਪਟ ਨੂੰ AI ਏਜੈਂਟ ਦੁਆਰਾ ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਪਛਾਣਿਆ ਜਾ ਸਕੇ। ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਦੇ ਲਈ ਕਈ ਵਾਰੀ ਗੱਲਬਾਤ ਵਿੱਚ ਤੁਰਾਂ ਦੀ ਗਿਣਤੀ ਸੀਮਿਤ ਕਰਨਾ ਇੱਕ ਹੋਰ ਤਰੀਕਾ ਹੈ।

### ਸੰਵੇਦਨਸ਼ੀਲ ਪ੍ਰਣਾਲੀਆਂ ਤੱਕ ਪਹੁੰਚ

**ਵਰਣਨ**: ਜੇ AI ਏਜੈਂਟ ਕੋਲ ਅਜਿਹੀਆਂ ਪ੍ਰਣਾਲੀਆਂ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਹੈ ਜੋ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਨੂੰ ਸੰਭਾਲਦੀਆਂ ਹਨ, ਤਾਂ ਹਮਲਾਵਰ ਏਜੈਂਟ ਅਤੇ ਇਹ ਸੇਵਾਵਾਂ ਦੇ ਦਰਮਿਆਨ ਦੇ ਸੰਪਰਕ ਨੂੰ ਖ਼ਤਰੇ ਵਿੱਚ ਪਾ ਸਕਦੇ ਹਨ। ਇਹ ਸਿੱਧੇ ਹਮਲੇ ਹੋ ਸਕਦੇ ਹਨ ਜਾਂ ਏਜੈਂਟ ਰਾਹੀਂ ਸਿਸਟਮਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼।

**ਘਟਾਉਣਾ**: AI ਏਜੈਂਟਾਂ ਨੂੰ ਲੋੜ ਅਨੁਸਾਰ ਹੀ ਪ੍ਰਣਾਲੀਆਂ ਨੂੰ ਪਹੁੰਚ ਦਿਓ ਤਾਂ ਜੋ ਇਨ੍ਹਾਂ ਹਮਲਿਆਂ ਤੋਂ ਬਚਾ ਜਾ ਸਕੇ। ਏਜੈਂਟ ਅਤੇ ਪ੍ਰਣਾਲੀ ਵਿਚਕਾਰ ਸੰਪਰਕ ਸੁਰੱਖਿਅਤ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਪ੍ਰਮਾਣਿਕਰਨ ਅਤੇ ਐਕਸੈਸ ਨਿਯੰਤਰਣ ਇਕ ਹੋਰ ਤਰੀਕਾ ਹੈ ਇਸ ਜਾਣਕਾਰੀ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ।

### ਸਰੋਤ ਅਤੇ ਸੇਵਾਵਾਂ ਤੇ ਬਹੁਤ ਜ਼ਿਆਦਾ ਬੋਝ

**ਵਰਣਨ:** AI ਏਜੈਂਟ ਵੱਖ-ਵੱਖ ਟੂਲ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਸਕਦੇ ਹਨ ਕੰਮ ਪੂਰੇ ਕਰਨ ਲਈ। ਹਮਲਾਵਰ ਇਸ ਯੋਗਤਾ ਨੂੰ ਵਰਤ ਕੇ ਉੱਚ ਮਾਤਰਾ ਵਿੱਚ ਬੇਨਤੀਆਂ ਭੇਜ ਕੇ ਇਨ੍ਹਾਂ ਸੇਵਾਵਾਂ ਤੇ ਅਟੈਕ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਕਰਕੇ ਪ੍ਰਣਾਲੀ ਫੇਲਿਆ ਜਾ ਸਕਦਾ ਹੈ ਜਾਂ ਬਹੁਤ ਜ਼ਿਆਦਾ ਖਰਚ ਆ ਸਕਦਾ ਹੈ।

**ਘਟਾਉਣਾ**: ਨੀਤੀ ਲਾਗੂ ਕਰੋ ਜਿਹੜੀ ਇਹ ਸੀਮਤ ਕਰੇ ਕਿ AI ਏਜੈਂਟ ਕਿਸ ਹੱਦ ਤੱਕ ਸੇਵਾ ਨੂੰ ਬੇਨਤੀਆਂ ਭੇਜ ਸਕਦਾ ਹੈ। ਗੱਲਬਾਤ ਦੇ ਦੌਰਾਨ ਮੰਡਲ ਅਤੇ ਬੇਨਤੀਆਂ ਦੀ ਗਿਣਤੀ ਸੀਮਤ ਕਰਨਾ ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਦਾ ਇਕ ਹੋਰ ਤਰੀਕਾ ਹੈ।

### ਗਿਆਨ ਆਧਾਰ ਵਿਸ਼ਫੋਟੀਕਰਨ

**ਵਰਣਨ:** ਇਹ ਹਮਲਾ ਸਿੱਧਾ AI ਏਜੈਂਟ ਨੂੰ ਨਿਸ਼ਾਨਾ ਨਹੀਂ ਲਗਾਉਂਦਾ, ਪਰ ਗਿਆਨ ਆਧਾਰ ਅਤੇ ਹੋਰ ਸੇਵਾਵਾਂ ਨੂੰ ਟਾਰਗੇਟ ਕਰਦਾ ਹੈ ਜੋ AI ਏਜੈਂਟ ਵਰਤੂਗਾ। ਇਹ ਡਾਟਾ ਜਾਂ ਜਾਣਕਾਰੀ ਨੂੰ ਖਰਾਬ ਕਰਨ ਦਾ ਕਾਰਨ ਲੈ ਸਕਦਾ ਹੈ ਜੋ ਏਜੈਂਟ ਕੰਮ ਪੂਰਾ ਕਰਨ ਲਈ ਵਰਤੇਗਾ, ਜਿਸ ਨਾਲ ਜੁਹੋਰੇ ਜਾਂ ਅਣਚਾਹੇ ਜਵਾਬ ਮਿਲ ਸਕਦੇ ਹਨ।

**ਘਟਾਉਣਾ**: AI ਏਜੈਂਟ ਆਪਣੇ ਕੰਮ ਵਿੱਚ ਵਰਤਣ ਵਾਲੇ ਡਾਟੇ ਦੀ ਨਿਯਮਤ ਜਾਂਚ ਕਰੋ। ਇਸ ਡਾਟੇ ਤੱਕ ਪਹੁੰਚ ਸੁਰੱਖਿਅਤ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ ਅਤੇ ਸਿਰਫ਼ ਭਰੋਸੇਮੰਦ ਲੋਕਾਂ ਵੱਲੋਂ ਹੀ ਬਦਲੀ ਜਾਵੇ ਤਾਂ ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਹਮਲੇ ਤੋਂ ਬਚਿਆ ਜਾ ਸਕੇ।

### ਲੜੀਵਾਰ ਗਲਤੀਆਂ

**ਵਰਣਨ:** AI ਏਜੈਂਟ ਵੱਖ-ਵੱਖ ਟੂਲ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚਦੇ ਹਨ ਕੰਮ ਪੂਰੇ ਕਰਨ ਲਈ। ਹਮਲਾਵਰ ਦੁਆਰਾ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਗਲਤੀਆਂ ਦੂਜੀਆਂ ਸਿਸਟਮਾਂ ਦੀਆਂ ਨਾਕਾਮੀਆਂ ਦਾ ਕਾਰਣ ਬਣ ਸਕਦੀਆਂ ਹਨ ਜੋ AI ਏਜੈਂਟ ਨਾਲ ਜੁੜੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਹਮਲਾ ਵੱਧ ਵਿਆਪਕ ਅਤੇ ਮੁਸ਼ਕਲ ਹੋ ਜਾਂਦਾ ਹੈ।

**ਘਟਾਉਣਾ**: ਇੱਕ ਤਰੀਕਾ ਇਹ ਹੈ ਕਿ AI ਏਜੈਂਟ ਨੂੰ ਸਿਮਤ ਵਾਤਾਵਰਣ ਵਿੱਚ ਚਲਾਇਆ ਜਾਵੇ, ਜਿਵੇਂ ਕਿ ਡੋਕਰ ਕੰਟੇਨਰ ਵਿੱਚ ਕੰਮ ਕਰਨਾ, ਤਾਂ ਜੋ ਸਿੱਧੇ ਸਿਸਟਮ ਹਮਲਿਆਂ ਤੋਂ ਬਚਾ ਜਾ ਸਕੇ। ਕੁਝ ਪ੍ਰਣਾਲੀਆਂ ਤੋਂ ਗਲਤੀ ਆਉਣ 'ਤੇ ਫੈਲਬੈਕ ਮਕੈਨੀਜ਼ਮ ਅਤੇ ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਵਾਲੀ ਲਾਜ਼ਮੀਤਾ ਬਣਾਉਣ ਨਾਲ ਵੱਡੀਆਂ ਨਾਕਾਮੀਆਂ ਤੋਂ ਬਚਾ ਜਾ ਸਕਦਾ ਹੈ।

## ਮਨੁੱਖ-ਇਨ-ਦ-ਲੂਪ

ਭਰੋਸੇਮੰਦ AI ਏਜੈਂਟ ਪ੍ਰਣਾਲੀਆਂ ਬਣਾਉਣ ਦਾ ਇੱਕ ਹੋਰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਤਰੀਕਾ ਮਨੁੱਖ-ਇਨ-ਦ-ਲੂਪ ਪधਤਤੀ ਦੀ ਵਰਤੋਂ ਕਰਨੀ ਹੈ। ਇਸ ਨਾਲ ਇੱਕ ਐਸਾ ਪ੍ਰਵਾਹ ਬਣਦਾ ਹੈ ਜਿੱਥੇ ਯੂਜ਼ਰ ਚਲਦੇ ਸਮੇਂ ਏਜੈਂਟਾਂ ਨੂੰ ਫੀਡਬੈਕ ਦੇ ਸਕਦੇ ਹਨ। ਯੂਜ਼ਰ ਅਸਲ ਵਿੱਚ ਇੱਕ ਬਹੁ-ਏਜੈਂਟ ਪ੍ਰਣਾਲੀ ਵਿੱਚ ਏਜੈਂਟ ਵਜੋਂ ਕੰਮ ਕਰਦੇ ਹਨ ਅਤੇ ਚਲਦੇ ਸਮੇਂ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਮੰਨਜ਼ੂਰੀ ਜਾਂ ਸਮਾਪਤੀ ਦੇ ਸਕਦੇ ਹਨ।

![Human in The Loop](../../../translated_images/pa/human-in-the-loop.5f0068a678f62f4f.webp)

ਇੱਥੇ Microsoft Agent Framework ਦੀ ਵਰਤੋਂ ਉੱਤੇ ਇਕ ਕੋਡ ਸ્નਿੱਪੇਟ ਹੈ ਜਿਸ ਨਾਲ ਇਹ ਅਵਧਾਰਣਾ ਲਾਗੂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# ਮਨੁੱਖੀ-ਦਾਖਲ ਅਨুমੋਦੀ ਨਾਲ ਪ੍ਰਦਾਤਾ ਬਣਾਓ
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# ਮਨੁੱਖੀ ਅਨুমੋਦੀ ਕਦਮ ਨਾਲ ਏਜੰਟ ਬਣਾਓ
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ਯੂਜ਼ਰ ਜਵਾਬ ਦੀ ਸਮੀਖਿਆ ਅਤੇ ਮਨਜ਼ੂਰੀ ਕਰ ਸਕਦਾ ਹੈ
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## ਨਤੀਜਾ

ਭਰੋਸੇਮੰਦ AI ਏਜੈਂਟ ਬਣਾਉਣ ਲਈ ਸੰਭਾਲੇ ਹੋਏ ਡਿਜ਼ਾਈਨ, ਮਜ਼ਬੂਤ ਸੁਰੱਖਿਆ ਉਪਾਇ, ਅਤੇ ਲਗਾਤਾਰ ਸੁਧਾਰ ਜ਼ਰੂਰੀ ਹਨ। ਬਣੇ ਬਣੇ ਮੈਟਾ ਪ੍ਰੰਪਟਿੰਗ ਸਿਸਟਮ, ਸੰਭਾਵਿਤ ਖਤਰਿਆਂ ਨੂੰ ਸਮਝਣਾ, ਅਤੇ ਘਟਾਵੇ ਦੇ ਤਰੀਕੇ ਲਾਗੂ ਕਰਕੇ ਵਿਕਾਸਕਾਰ ਐਸੇ AI ਏਜੈਂਟ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹਨ ਜੋ ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ালী ਬਣਦੇ ਹਨ। ਇਸਦੇ ਨਾਲ-ਨਾਲ ਮਨੁੱਖ-ਇਨ-ਦ-ਲੂਪ ਪਹੁੰਚ ਦੇ ਨਾਲ਼ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਕਿ AI ਏਜੈਂਟ ਯੂਜ਼ਰ ਦੀਆਂ ਲੋੜਾਂ ਨਾਲ ਮਿਲਦੇ-ਜੁਲਦੇ ਰਹਿਣ ਅਤੇ ਖਤਰਿਆਂ ਨੂੰ ਘਟਾਓ। ਜਿਵੇਂ-ਜਿਵੇਂ AI ਵਿਕਸਤ ਹੋ ਰਿਹਾ ਹੈ, ਸੁਰੱਖਿਆ, ਪਰਦਰਸ਼ਿਤਾ ਅਤੇ ਨੈਤਿਕ ਵਿਚਾਰਾਂ ਵਿੱਚ ਸਾਵਧਾਨ ਰਹਿਣਾ AI-ਚਲਿਤ ਪ੍ਰਣਾਲੀਆਂ ਵਿੱਚ ਭਰੋਸਾ ਅਤੇ ਵਿਸ਼ਵਾਸ ਬਣਾਉਣ ਲਈ ਅਹੰਕਾਰਮਈ ਭੂਮਿਕਾ ਨਿਭਾਏਗਾ।

## ਕੋਡ ਦੇ ਨਮੂਨੇ

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): ਮੈਟਾ-ਪ੍ਰੰਪਟ ਸਿਸਟਮ-ਮੇਸੇਜ ਫ੍ਰੇਮਵਰਕ ਦੀ ਕਦਮ-ਦਰ-ਕਦਮ ਪ੍ਰਦਰਸ਼ਨੀ।
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): ਭਰੋਸੇਮੰਦ ਏਜੈਂਟਾਂ ਲਈ ਪਹਿਲੇ ਕਾਰਵਾਈ ਮਨਜ਼ੂਰੀ ਗੇਟ, ਖਤਰਾ ਦਰਜਾ, ਅਤੇ ਆਡੀਟ ਲੌਗਿੰਗ।

### ਭਰੋਸੇਮੰਦ AI ਏਜੈਂਟ ਬਨਾਉਣ ਬਾਰੇ ਵਧੇਰੇ ਸਵਾਲ ਹਨ?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਵੋ ਤਾਂ ਜੋ ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲੋ, ਦਫ਼ਤਰ ਘੰਟਿਆਂ ਵਿੱਚ ਹਾਜ਼ਰੀ ਦਿਓ ਅਤੇ ਆਪਣੇ AI ਏਜੈਂਟਾਂ ਦੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲਵੋ।

## ਹੋਰ ਸਰੋਤ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ਜ਼ਿੰਮੇਵਾਰ AI ਦਾ ਜਾਇਜ਼ਾ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਅਤੇ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਮੁੱਲਾਂਕਣ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ਸੁਰੱਖਿਆ ਸਿਸਟਮ ਮੇਸੇਜ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ਖਤਰਾ ਮੁਲਾਂਕਣ ਟੈਮਪਲੇਟ</a>

## ਪਿਛਲਾ ਪਾਠ

[Agentic RAG](../05-agentic-rag/README.md)

## ਅਗਲਾ ਪਾਠ

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->