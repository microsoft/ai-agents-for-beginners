<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T10:35:08+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "pa"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.pa.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ਉਪਰੋਕਤ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰਕੇ ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਵੇਖੋ)_

# ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣਾ

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ ਤੁਸੀਂ ਸਿੱਖੋਗੇ:

- ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ AI ਏਜੰਟ ਕਿਵੇਂ ਬਣਾਉਣੇ ਅਤੇ ਤੈਨਾਤ ਕਰਨੇ ਹਨ।
- AI ਏਜੰਟ ਵਿਕਸਿਤ ਕਰਦੇ ਸਮੇਂ ਮਹੱਤਵਪੂਰਨ ਸੁਰੱਖਿਆ ਵਿਚਾਰ।
- ਡਾਟਾ ਅਤੇ ਯੂਜ਼ਰ ਗੋਪਨੀਯਤਾ ਨੂੰ ਕਿਵੇਂ ਕਾਇਮ ਰੱਖਣਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਸਿੱਖ ਲਵੋਗੇ:

- AI ਏਜੰਟ ਬਣਾਉਣ ਸਮੇਂ ਖਤਰੇ ਪਛਾਣਣ ਅਤੇ ਘਟਾਉਣ ਦੇ ਤਰੀਕੇ।
- ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਸੁਰੱਖਿਆ ਉਪਾਅ ਲਾਗੂ ਕਰਨ ਕਿ ਡਾਟਾ ਅਤੇ ਪਹੁੰਚ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਪ੍ਰਬੰਧਿਤ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ।
- ਅਜਿਹੇ AI ਏਜੰਟ ਬਣਾਉਣਾ ਜੋ ਡਾਟਾ ਗੋਪਨੀਯਤਾ ਕਾਇਮ ਰੱਖਣ ਅਤੇ ਉਪਭੋਗਤਾ ਨੂੰ ਗੁਣਵੱਤਾ ਭਰਪੂਰ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਨ।

## ਸੁਰੱਖਿਆ

ਚਲੋ ਪਹਿਲਾਂ ਸੁਰੱਖਿਅਤ ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਬਾਰੇ ਗੱਲ ਕਰੀਏ। ਸੁਰੱਖਿਆ ਦਾ ਮਤਲਬ ਹੈ ਕਿ AI ਏਜੰਟ ਉਸ ਤਰੀਕੇ ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਉਸਨੂੰ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਨਿਰਮਾਤਾ ਵਜੋਂ, ਸਾਡੇ ਕੋਲ ਸੁਰੱਖਿਆ ਵਧਾਉਣ ਲਈ ਤਰੀਕੇ ਅਤੇ ਸਾਧਨ ਹਨ:

### ਸਿਸਟਮ ਸੁਨੇਹਾ ਫਰੇਮਵਰਕ ਬਣਾਉਣਾ

ਜੇ ਤੁਸੀਂ Large Language Models (LLMs) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਦੇ ਵੀ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈ ਹੈ, ਤਾਂ ਤੁਹਾਨੂੰ ਮਜ਼ਬੂਤ ਸਿਸਟਮ ਪ੍ਰੌੰਪਟ ਜਾਂ ਸਿਸਟਮ ਸੁਨੇਹਾ ਡਿਜ਼ਾਈਨ ਕਰਨ ਦੀ ਮਹੱਤਤਾ ਦਾ ਪਤਾ ਹੋਵੇਗਾ। ਇਹ ਪ੍ਰੌੰਪਟ ਇਸ ਗੱਲ ਨੂੰ ਸਥਾਪਿਤ ਕਰਦੇ ਹਨ ਕਿ LLM ਯੂਜ਼ਰ ਅਤੇ ਡਾਟਾ ਨਾਲ ਕਿਵੇਂ ਸੰਚਾਰ ਕਰੇਗਾ।

AI ਏਜੰਟਾਂ ਲਈ, ਸਿਸਟਮ ਪ੍ਰੌੰਪਟ ਹੋਰ ਵੀ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿਉਂਕਿ AI ਏਜੰਟਾਂ ਨੂੰ ਉਹਨਾਂ ਕੰਮਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਬਹੁਤ ਹੀ ਵਿਸ਼ੇਸ਼ ਹਦਾਇਤਾਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ ਜੋ ਅਸੀਂ ਉਨ੍ਹਾਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਹਨ।

ਸਕੇਲਯੋਗ ਸਿਸਟਮ ਪ੍ਰੌੰਪਟ ਬਣਾਉਣ ਲਈ, ਅਸੀਂ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਇੱਕ ਜਾਂ ਇੱਕ ਤੋਂ ਵੱਧ ਏਜੰਟਾਂ ਬਣਾਉਣ ਲਈ ਸਿਸਟਮ ਸੁਨੇਹਾ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ:

![ਸਿਸਟਮ ਸੁਨੇਹਾ ਫਰੇਮਵਰਕ ਬਣਾਉਣਾ](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.pa.png)

#### ਪਹਲਾ ਕਦਮ: ਮੈਟਾ ਸਿਸਟਮ ਸੁਨੇਹਾ ਬਣਾਓ

ਮੈਟਾ ਪ੍ਰੌੰਪਟ ਨੂੰ LLM ਦੁਆਰਾ ਉਹ ਸਿਸਟਮ ਪ੍ਰੌੰਪਟ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ ਜੋ ਅਸੀਂ ਬਣਾਉਂਦੇ ਹਾਂ। ਅਸੀਂ ਇਸਨੂੰ ਇੱਕ ਟੈਂਪਲੇਟ ਵਜੋਂ ਡਿਜ਼ਾਈਨ ਕਰਦੇ ਹਾਂ ਤਾਂ ਜੋ ਜ਼ਰੂਰਤ ਪੈਣ 'ਤੇ ਕਈ ਏਜੰਟਾਂ ਨੂੰ ਕੁਸ਼ਲਤਾਪੂਰਵਕ ਬਣਾਇਆ ਜਾ ਸਕੇ।

ਇਹ ਰਿਹਾ ਮੈਟਾ ਸਿਸਟਮ ਸੁਨੇਹੇ ਦਾ ਉਦਾਹਰਣ ਜੋ ਅਸੀਂ LLM ਨੂੰ ਦੇਵਾਂਗੇ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ਦੂਜਾ ਕਦਮ: ਇੱਕ ਬੁਨਿਆਦੀ ਪ੍ਰੌੰਪਟ ਬਣਾਓ

ਅਗਲਾ ਕਦਮ AI ਏਜੰਟ ਦਾ ਵੇਰਵਾ ਦੇਣ ਲਈ ਇੱਕ ਬੁਨਿਆਦੀ ਪ੍ਰੌੰਪਟ ਬਣਾਉਣਾ ਹੈ। ਤੁਹਾਨੂੰ ਏਜੰਟ ਦੀ ਭੂਮਿਕਾ, ਉਹ ਕੰਮ ਜੋ ਏਜੰਟ ਪੂਰੇ ਕਰੇਗਾ, ਅਤੇ ਏਜੰਟ ਦੀਆਂ ਹੋਰ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਸ਼ਾਮਲ ਕਰਨੀ ਚਾਹੀਦੀਆਂ ਹਨ।

ਇਹ ਰਿਹਾ ਇੱਕ ਉਦਾਹਰਣ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ਤੀਜਾ ਕਦਮ: ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਸੁਨੇਹਾ LLM ਨੂੰ ਦਿਓ

ਹੁਣ ਅਸੀਂ ਮੈਟਾ ਸਿਸਟਮ ਸੁਨੇਹੇ ਨੂੰ ਸਿਸਟਮ ਸੁਨੇਹੇ ਵਜੋਂ ਅਤੇ ਆਪਣੇ ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਸੁਨੇਹੇ ਨੂੰ ਦੇ ਕੇ ਇਸਨੂੰ ਅਪਟਿਮਾਈਜ਼ ਕਰ ਸਕਦੇ ਹਾਂ।

ਇਸ ਨਾਲ ਇੱਕ ਸਿਸਟਮ ਸੁਨੇਹਾ ਤਿਆਰ ਹੋਵੇਗਾ ਜੋ ਸਾਡੇ AI ਏਜੰਟਾਂ ਨੂੰ ਗਾਈਡ ਕਰਨ ਲਈ ਵਧੀਆ ਤਰੀਕੇ ਨਾਲ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੋਵੇਗਾ:

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

#### ਚੌਥਾ ਕਦਮ: ਦੁਹਰਾਓ ਅਤੇ ਸੁਧਾਰ ਕਰੋ

ਇਸ ਸਿਸਟਮ ਸੁਨੇਹਾ ਫਰੇਮਵਰਕ ਦੀ ਮੁੱਲਵਾਨੀ ਇਹ ਹੈ ਕਿ ਕਈ ਏਜੰਟਾਂ ਲਈ ਸਿਸਟਮ ਸੁਨੇਹੇ ਬਣਾਉਣ ਨੂੰ ਆਸਾਨ ਬਣਾਉਣਾ ਅਤੇ ਸਮੇਂ ਦੇ ਨਾਲ ਆਪਣੇ ਸਿਸਟਮ ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਸੁਧਾਰ ਕਰਨਾ। ਇਹ ਕਦੇ ਵੀ ਆਮ ਨਹੀਂ ਹੁੰਦਾ ਕਿ ਤੁਹਾਡਾ ਸਿਸਟਮ ਸੁਨੇਹਾ ਪਹਿਲੀ ਵਾਰ ਵਿੱਚ ਹੀ ਤੁਹਾਡੇ ਪੂਰੇ ਯੂਜ਼ ਕੇਸ ਲਈ ਕੰਮ ਕਰੇ। ਬੁਨਿਆਦੀ ਸਿਸਟਮ ਸੁਨੇਹੇ ਵਿੱਚ ਛੋਟੇ-ਛੋਟੇ ਬਦਲਾਅ ਕਰਕੇ ਅਤੇ ਇਸਨੂੰ ਸਿਸਟਮ ਰਾਹੀਂ ਚਲਾਕੇ ਤੁਲਨਾ ਅਤੇ ਮੁਲਾਂਕਣ ਕਰਨ ਦੀ ਯੋਗਤਾ ਤੁਹਾਨੂੰ ਨਤੀਜੇ ਸੁਧਾਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗੀ।

## ਖਤਰੇ ਸਮਝਣਾ

ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ, ਇਹ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਤੁਹਾਡੇ AI ਏਜੰਟ ਨੂੰ ਲੱਗਣ ਵਾਲੇ ਖਤਰੇ ਅਤੇ ਜੋਖਮਾਂ ਨੂੰ ਸਮਝਿਆ ਅਤੇ ਘਟਾਇਆ ਜਾਵੇ। ਚਲੋ ਕੁਝ ਵੱਖ-ਵੱਖ ਖਤਰੇ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਹੱਲਾਂ ਬਾਰੇ ਗੱਲ ਕਰੀਏ।

![ਖਤਰੇ ਸਮਝਣਾ](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.pa.png)

### ਕੰਮ ਅਤੇ ਹਦਾਇਤ

**ਵੇਰਵਾ:** ਹਮਲਾਵਰ ਪ੍ਰੌੰਪਟਿੰਗ ਜਾਂ ਇਨਪੁਟਸ ਨੂੰ ਬਦਲ ਕੇ AI ਏਜੰਟ ਦੀਆਂ ਹਦਾਇਤਾਂ ਜਾਂ ਲਕਸ਼ਾਂ ਨੂੰ ਬਦਲਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਨ।

**ਰੋਕਥਾਮ:** ਖਤਰਨਾਕ ਪ੍ਰੌੰਪਟਾਂ ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ ਵੈਧਤਾ ਜਾਂਚ ਅਤੇ ਇਨਪੁਟ ਫਿਲਟਰ ਲਾਗੂ ਕਰੋ। ਕਿਉਂਕਿ ਇਹ ਹਮਲੇ ਆਮ ਤੌਰ 'ਤੇ ਏਜੰਟ ਨਾਲ ਵਾਰੰ-ਵਾਰ ਸੰਚਾਰ ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ, ਗੱਲਬਾਤ ਵਿੱਚ ਟਰਨ ਦੀ ਗਿਣਤੀ ਘਟਾਉਣਾ ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਦਾ ਹੋਰ ਤਰੀਕਾ ਹੈ।

### ਮਹੱਤਵਪੂਰਨ ਸਿਸਟਮਾਂ ਤੱਕ ਪਹੁੰਚ

**ਵੇਰਵਾ:** ਜੇਕਰ AI ਏਜੰਟ ਨੂੰ ਉਹਨਾਂ ਸਿਸਟਮਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਹੈ ਜਿੱਥੇ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਸਟੋਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਹਮਲਾਵਰ ਏਜੰਟ ਅਤੇ ਸੇਵਾਵਾਂ ਦੇ ਵਿਚਕਾਰ ਸੰਚਾਰ ਨੂੰ ਖਤਰੇ ਵਿੱਚ ਪਾ ਸਕਦੇ ਹਨ। ਇਹ ਸਿੱਧੇ ਹਮਲੇ ਜਾਂ ਅਪਰੋਕਸ਼ ਤੌਰ 'ਤੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਹੋ ਸਕਦੀ ਹੈ।

**ਰੋਕਥਾਮ:** AI ਏਜੰਟਾਂ ਨੂੰ ਸਿਰਫ਼ ਜ਼ਰੂਰਤ ਦੇ ਅਧਾਰ 'ਤੇ ਸਿਸਟਮਾਂ ਤੱਕ ਪਹੁੰਚ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ। ਏਜੰਟ ਅਤੇ ਸਿਸਟਮ ਦੇ ਵਿਚਕਾਰ ਸੰਚਾਰ ਸੁਰੱਖਿਅਤ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰਨਾ ਇਸ ਜਾਣਕਾਰੀ ਦੀ ਰੱਖਿਆ ਕਰਨ ਦਾ ਹੋਰ ਤਰੀਕਾ ਹੈ।

### ਸਰੋਤ ਅਤੇ ਸੇਵਾ ਓਵਰਲੋਡਿੰਗ

**ਵੇਰਵਾ:** AI ਏਜੰਟ ਵੱਖ-ਵੱਖ ਸੰਦਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਕਰ ਸਕਦੇ ਹਨ। ਹਮਲਾਵਰ ਇਸ ਯੋਗਤਾ ਦਾ ਫਾਇਦਾ ਚੁੱਕ ਕੇ ਸੇਵਾਵਾਂ 'ਤੇ ਬਹੁਤ ਸਾਰੇ ਬੇਨਤੀ ਭੇਜ ਕੇ ਹਮਲਾ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਸਿਸਟਮ ਫੇਲ ਹੋ ਸਕਦੇ ਹਨ ਜਾਂ ਵੱਡੇ ਖਰਚੇ ਹੋ ਸਕਦੇ ਹਨ।

**ਰੋਕਥਾਮ:** ਸੇਵਾਵਾਂ ਨੂੰ ਕੀਤੀਆਂ ਜਾ ਸਕਣ ਵਾਲੀਆਂ ਬੇਨਤੀਆਂ ਦੀ ਗਿਣਤੀ ਸੀਮਿਤ ਕਰਨ ਲਈ ਨੀਤੀਆਂ ਲਾਗੂ ਕਰੋ। ਗੱਲਬਾਤ ਦੇ ਟਰਨਾਂ ਦੀ ਗਿਣਤੀ ਘਟਾਉਣਾ ਅਤੇ AI ਏਜੰਟ ਦੀਆਂ ਬੇਨਤੀਆਂ ਨੂੰ ਸੀਮਿਤ ਕਰਨਾ ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਦਾ ਹੋਰ ਤਰੀਕਾ ਹੈ।

### ਨੋਲੇਜ ਬੇਸ ਪੌਇਜ਼ਨਿੰਗ

**ਵੇਰਵਾ:** ਇਹ ਕਿਸਮ ਦਾ ਹਮਲਾ ਸਿੱਧੇ ਤੌਰ 'ਤੇ AI ਏਜੰਟ ਨੂੰ ਨਿਸ਼ਾਨਾ ਨਹੀਂ ਬਣਾਉਂਦਾ, ਪਰ ਉਸ ਨੋਲੇਜ ਬੇਸ ਅਤੇ ਹੋਰ ਸੇਵਾਵਾਂ ਨੂੰ ਨਿਸ਼ਾਨਾ ਬਣਾਉਂਦਾ ਹੈ ਜੋ AI ਏਜੰਟ ਵਰਤਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਡਾਟਾ ਜਾਂ ਜਾਣਕਾਰੀ ਨੂੰ ਖਰਾਬ ਕਰਨਾ ਸ਼ਾਮਲ ਹੋ ਸਕਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਉਪਭੋਗਤਾ ਨੂੰ ਪੱਖਪਾਤੀ ਜਾਂ ਅਣਚਾਹੇ ਜਵਾਬ ਮਿਲ ਸਕਦੇ ਹਨ।

**ਰੋਕਥਾਮ:** ਉਸ ਡਾਟਾ ਦੀ ਨਿਯਮਿਤ ਤਸਦੀਕ ਕਰੋ ਜੋ AI ਏਜੰਟ ਆਪਣੇ ਕੰਮਾਂ ਵਿੱਚ ਵਰਤਦਾ ਹੈ। ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਸ ਡਾਟਾ ਤੱਕ ਪਹੁੰਚ ਸੁਰੱਖਿਅਤ ਹੈ ਅਤੇ ਸਿਰਫ਼ ਭਰੋਸੇਯੋਗ ਵਿਅਕਤੀਆਂ ਦੁਆਰਾ ਬਦਲੀ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

### ਕੈਸਕੇਡਿੰਗ ਗਲਤੀਆਂ

**ਵੇਰਵਾ:** AI ਏਜੰਟ ਵੱਖ-ਵੱਖ ਸੰਦਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਪਹੁੰਚ ਕਰਦੇ ਹਨ। ਹਮਲਾਵਰਾਂ ਦੁਆਰਾ ਕੀਤੀਆਂ ਗਲਤੀਆਂ ਹੋਰ ਸਿਸਟਮਾਂ ਦੀ ਨਾਕਾਮੀ ਦਾ ਕਾਰਨ ਬਣ ਸਕਦੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਹਮਲਾ ਹੋਰ ਵਿਆਪਕ ਅਤੇ ਸਮੱਸਿਆ ਦਾ ਪਤਾ ਲਗਾਉਣਾ ਮੁਸ਼ਕਲ ਹੋ ਜਾਂਦਾ ਹੈ।

**ਰੋਕਥਾਮ:** ਇੱਕ ਤਰੀਕਾ ਇਹ ਹੈ ਕਿ AI ਏਜੰਟ ਨੂੰ ਸੀਮਿਤ ਵਾਤਾਵਰਣ ਵਿੱਚ ਚਲਾਇਆ ਜਾਵੇ, ਜਿਵੇਂ ਕਿ ਡੌਕਰ ਕੰਟੇਨਰ ਵਿੱਚ ਕੰਮ ਕਰਨਾ, ਤਾਂ ਜੋ ਸਿੱਧੇ ਸਿਸਟਮ ਹਮਲਿਆਂ ਤੋਂ ਬਚਿਆ ਜਾ ਸਕੇ। ਫਾਲਬੈਕ ਮਕੈਨਿਜ਼ਮ ਅਤੇ ਰੀਟ੍ਰਾਈ ਲੌਜਿਕ ਬਣਾਉਣਾ, ਜਦੋਂ ਕੁਝ ਸਿਸਟਮ ਗਲਤੀ ਨਾਲ ਜਵਾਬ ਦਿੰਦੇ ਹਨ, ਹੋਰ ਵੱਡੀਆਂ ਸਿਸਟਮ ਨਾਕਾਮੀਆਂ ਨੂੰ ਰੋਕਣ ਦਾ ਤਰੀਕਾ ਹੈ।

## ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ

ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਸਿਸਟਮ ਬਣਾਉਣ ਦਾ ਹੋਰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਤਰੀਕਾ ਹੈ ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ ਦੀ ਵਰਤੋਂ। ਇਹ ਇੱਕ ਐਸਾ ਪ੍ਰਵਾਹ ਬਣਾਉਂਦਾ ਹੈ ਜਿੱਥੇ ਯੂਜ਼ਰ ਪ੍ਰਕਿਰਿਆ ਦੌਰਾਨ ਏਜੰਟਾਂ ਨੂੰ ਫੀਡਬੈਕ ਦੇ ਸਕਦੇ ਹਨ। ਯੂਜ਼ਰ ਅਸਲ ਵਿੱਚ ਇੱਕ ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਵਿੱਚ ਏਜੰਟਾਂ ਵਜੋਂ ਕੰਮ ਕਰਦੇ ਹਨ ਅਤੇ ਚਲ ਰਹੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਮਨਜ਼ੂਰੀ ਜਾਂ ਰੱਦ ਕਰਦੇ ਹਨ।

![ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.pa.png)

ਇਹ ਰਿਹਾ AutoGen ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਇਸ ਸੰਕਲਪ ਨੂੰ ਲਾਗੂ ਕਰਨ ਦਾ ਕੋਡ ਸਨਿੱਪਟ:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## ਨਤੀਜਾ

ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਧਿਆਨਪੂਰਵਕ ਡਿਜ਼ਾਈਨ, ਮਜ਼ਬੂਤ ਸੁਰੱਖਿਆ ਉਪਾਅ, ਅਤੇ ਲਗਾਤਾਰ ਸੁਧਾਰ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਢਾਂਚਾਗਤ ਮੈਟਾ ਪ੍ਰੌੰਪਟਿੰਗ ਸਿਸਟਮ ਲਾਗੂ ਕਰਕੇ, ਸੰਭਾਵਿਤ ਖਤਰੇ ਸਮਝ ਕੇ, ਅਤੇ ਰੋਕਥਾਮ ਦੀ ਰਣਨੀਤੀਆਂ ਲਾਗੂ ਕਰਕੇ, ਡਿਵੈਲਪਰ ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ AI ਏਜੰਟ ਬਣਾਉਣ ਵਿੱਚ ਸਫਲ ਹੋ ਸਕਦੇ ਹਨ। ਇਸਦੇ ਨਾਲ ਹੀ, ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ ਪਹੁੰਚ ਸ਼ਾਮਲ ਕਰਨਾ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ AI ਏਜੰਟ ਯੂਜ਼ਰ ਦੀਆਂ ਜ਼ਰੂਰਤਾਂ ਨਾਲ ਸੰਗਤ ਰਹਿੰਦੇ ਹਨ ਅਤੇ ਖਤਰੇ ਘਟਦੇ ਹਨ। ਜਿਵੇਂ ਕਿ AI ਵਿਕਸਿਤ ਹੁੰਦਾ ਹੈ, ਸੁਰੱਖਿਆ, ਗੋਪਨੀਯਤਾ, ਅਤੇ ਨੈਤਿਕ ਵਿਚਾਰਾਂ 'ਤੇ ਸਜਗ ਰਹਿਣਾ AI-ਚਲਿਤ ਸਿਸਟਮਾਂ ਵਿੱਚ ਭਰੋਸਾ ਅਤੇ ਭਰੋਸੇਯੋਗਤਾ ਨੂੰ فروغ ਦੇਣ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੋਵੇਗਾ।

### ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ ਤਾਂ ਜੋ ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲ ਸਕੋ, ਦਫ਼ਤਰ ਦੇ ਘੰਟਿਆਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋ ਸਕੋ ਅਤੇ ਆਪਣੇ AI ਏਜੰਟਾਂ ਬਾਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰ ਸਕੋ।

## ਵਾਧੂ ਸਰੋਤ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ਜਿੰਮੇਵਾਰ AI ਦਾ ਝਲਕ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਅਤੇ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਮੁਲਾਂਕਣ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ਸੁਰੱਖਿਆ ਸਿਸਟਮ ਸੁਨੇਹੇ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ਜੋਖਮ ਮੁਲਾਂਕਣ ਟੈਂਪਲੇਟ</a>

## ਪਿਛਲਾ ਪਾਠ

[Agentic RAG](../05-agentic-rag/README.md)

## ਅਗਲਾ ਪਾਠ

[ਪਲੈਨਿੰਗ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ](../07-planning-design/README.md)

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਅਸਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।