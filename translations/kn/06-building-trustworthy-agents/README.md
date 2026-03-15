[![ನಂಬಬಹುದಾದ AI ಏಜೆಂಟ್ಸ್](../../../translated_images/kn/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ಈ ಪಾಠದ ವೀಡಿಯೋವನ್ನು ನೋಡಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# ನಂಬಬಹುದಾದ AI ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಿಸುವುದು

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು ಚರ್ಚಿಸುವುದು:

- ಸುರಕ್ಷಿತ ಮತ್ತು ಪರಿಣಾಮಕಾರಿ AI ಏಜೆಂಟ್ಸ್ ಅನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸುವುದು ಮತ್ತು ನಿಯೋಜಿಸುವುದು
- AI ಏಜೆಂಟ್ಸ್ ಅಭಿವೃದ್ಧಿಪಡಿಸುವಾಗ ಪ್ರಮುಖ ಭದ್ರತಾ ವಿಚಾರಗಳು.
- AI ಏಜೆಂಟ್ಸ್ ಅಭಿವೃದ್ಧಿಪಡಿಸುವಾಗ ಡೇಟಾ ಮತ್ತು ಬಳಕೆದಾರರ ಗೌಪ್ಯತೆ ಹೇಗೆ ಕಾಪಾಡುವುದು.

## ಅಧ್ಯಯನ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ತಿಳಿಯಬಲ್ಲಿರಿ:

- AI ಏಜೆಂಟ್ಸ್ ರಚಿಸುವಾಗ ಅಪಾಯಗಳನ್ನು ಗುರುತಿಸಿ ಇವುಗಳನ್ನು ತಡೆಗಟ್ಟುವುದು.
- ಡೇಟಾ ಮತ್ತು ಪ್ರವೇಶವನ್ನು ಸರಿಯಾಗಿ ನಿರ್ವಹಿಸಲು ಭದ್ರತಾ ಕ್ರಮಗಳನ್ನು ಜಾರಿಗೊಳಿಸುವುದು.
- ಡೇಟಾ ಗೌಪ್ಯತೆ ಕಾಪಾಡುವ ಮತ್ತು ಉತ್ತಮ ಬಳಕೆದಾರ ಅನುಭವ ನೀಡುವ AI ಏಜೆಂಟ್ಸ್ ರಚಿಸುವುದು.

## ಭದ್ರತೆ

ಮನೆಯಲ್ಲಿಯೇ ಸುರಕ್ಷಿತ ಏಜೆಂಟಿಕ್ ಅಪ್ಲಿಕೇಷನ್ಗಳ ನಿರ್ಮಾಣವನ್ನು ನೋಡೋಣ. ಭದ್ರತೆ ಅಂದರೆ AI ಏಜೆಂಟ್ ನಿರ್ದಿಷ್ಟವಾಗಿ ವಿನ್ಯಾಸಗೊಳ್ಳುವಂತೆ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದು. ಏಜೆಂಟಿಕ್ ಅಪ್ಲಿಕೇಷನ್ಸ್ ನಿರ್ಮಾಪಕರಾಗಿ ನಾವು ಭದ್ರತೆಯನ್ನು ಹೆಚ್ಚುಮಾಡಲು ವಿಧಾನಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಹೊಂದಿದ್ದೇವೆ:

### ಸಿಸ್ಟಂ ಸಂದೇಶ ಫ್ರೇಮ್ವರ್ಕ್ ನಿರ್ಮಿಸುವುದು

ನೀವು LLMs ಅನ್ನು ಬಳಸಿಕೊಂಡು AI ಅಪ್ಲಿಕೇಷನ್ ನಿರ್ಮಿಸಿದ್ದರೆ, ಬಲವಾದ ಸಿಸ್ಟಂ ಪ್ರಾಂಪ್ಟ್ ಅಥವಾ ಸಿಸ್ಟಂ ಸಂದೇಶ ವಿನ್ಯಾಸ ಮಾಡುವುದು ಬಹಳ ಮುಖ್ಯವೆಂದು ತಿಳಿದಿರುತ್ತದೆ. ಈ ಪ್ರಾಂಪ್ಟ್‌ಗಳು LLM ಬಳಕೆದಾರರೊಂದಿಗೆ ಮತ್ತು ಡೇಟಾದೊಂದಿಗೆ ಸಂವಾದಿಸುವ ವಿಧಾನಕ್ಕೆ ಮೆಟಾ ನಿಯమಗಳು, ಸೂಚನೆಗಳು ಮತ್ತು ಮಾರ್ಗಸೂಚಿಗಳನ್ನು ಸ್ಥಾಪಿಸುತ್ತವೆ.

AI ಏಜೆಂಟ್ಸ್ ಗಾಗಿ, ಸಿಸ್ಟಂ ಪ್ರಾಂಪ್ಟ್ ಇನ್ನೂ ಹೆಚ್ಚು ಮಹತ್ವದ್ದಾಗಿದೆ ಏಕೆಂದರೆ AI ಏಜೆಂಟ್ಸ್ ಗಾಗಿ ನಾವು ವಿನ್ಯಾಸ ಮಾಡಿರುವ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ಬಹಳ ನಿಖರವಾದ ಸೂಚನೆಗಳು ಅಗತ್ಯವಾಗುತ್ತವೆ.

ಸ್ಕೇಲಬಲ್ ಸಿಸ್ಟಂ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ರಚಿಸಲು, ನಮ್ಮ ಅಪ್ಲಿಕೇಷನಿನಲ್ಲಿ ಒಂದು ಅಥವಾ ಹೆಚ್ಚು ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಿಸಲು ಸಿಸ್ಟಂ ಸಂದೇಶ ಫ್ರೇಮ್ವರ್ಕ್ ಅನ್ನು ಬಳಸಬಹುದು:

![ಸಿಸ್ಟಂ ಸಂದೇಶ ಫ್ರೇಮ್ವರ್ಕ್ ನಿರ್ಮಿಸುವುದು](../../../translated_images/kn/system-message-framework.3a97368c92d11d68.webp)

#### ಹಂತ 1: ಮೆಟಾ ಸಿಸ್ಟಂ ಸಂದೇಶ ರಚಿಸಿ

ಮೆಟಾ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು LLM ಬಳಸಿ ನಾವು ರಚಿಸುವ ಏಜೆಂಟ್ಗಳಿಗೆ ಸಿಸ್ಟಂ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ. ನಾವು ಅದನ್ನು ಟೆಂಪ್ಲೇಟ್ ಆಗಿ ರೂಪಿಸುತ್ತೇವೆ ಆಗ ಬೇಕಾದಷ್ಟು ಏಜೆಂಟ್ಸ್ ಸ ಸೂಕ್ತವಾಗಿ ರಚಿಸಬಹುದು.

ಇದು LLM ಗೆ ನೀಡಬಹುದಾದ ಮೆಟಾ ಸಿಸ್ಟಂ ಸಂದೇಶದ ಉದಾಹರಣೆ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ಹಂತ 2: ಮೂಲ ಪ್ರಾಂಪ್ಟ್ ರಚಿಸಿ

ಮುಂದುವರಿದ ಹಂತದಲ್ಲಿ, AI ಏಜೆಂಟ್ನು ವರ್ಣಿಸುವ ಮೂಲ ಪ್ರಾಂಪ್ಟ್ ರಚಿಸಬೇಕು. ನೀವು ಏಜೆಂಟ್ ಪಾತ್ರ, ಏಜೆಂಟ್ ಪೂರ್ಣ ಮಾಡುವ ಕಾರ್ಯಗಳು ಮತ್ತು ಯಾವುದೇ ಇತರ ಹೊಣೆಗಾರಿಕೆಗಳನ್ನು ಸೇರಿಸಬೇಕು.

ಇದಿಗೆ ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ಹಂತ 3: LLM ಗೆ ಮೂಲ ಸಿಸ್ಟಂ ಸಂದೇಶ ನೀಡಿರಿ

ಈಗ ನಾವು ಈ ಸಿಸ್ಟಂ ಸಂದೇಶವನ್ನು ಮೆಟಾ ಸಿಸ್ಟಂ ಸಂದೇಶ ಮತ್ತು ನಮ್ಮ ಮೂಲ ಸಿಸ್ಟಂ ಸಂದೇಶವನ್ನು ಬಳಸಿ ಉತ್ತಮಗೊಳಿಸಬಹುದು.

ಇದರಿಂದ ನಮ್ಮ AI ಏಜೆಂಟ್ಗಳಿಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡಲು ಉತ್ತಮವಾಗಿ ವಿನ್ಯಾಸಗೊಂಡ ಸಿಸ್ಟಂ ಸಂದೇಶ ಸೃಷ್ಟಿಯಾಗುತ್ತದೆ:

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

#### ಹಂತ 4: ಪುನರಾವೃತ್ತಿ ಮತ್ತು ಸುಧಾರಣೆ

ಈ ಸಿಸ್ಟಂ ಸಂದೇಶ ಫ್ರೇಮ್ವರ್ಕ್ ಮೌಲ್ಯವೆಂದರೆ ಬಹು ಏಜೆಂಟ್ಗಳಿಗಾಗಿ ಸಿಸ್ಟಂ ಸಂದೇಶಗಳನ್ನು ಲಘುವಾಗಿ ತಯಾರಿಸಲು ಮತ್ತು ನಿಮ್ಮ ಸಿಸ್ಟಂ ಸಂದೇಶಗಳನ್ನು ಕಾಲಕಾಲಕ್ಕೆ ಸುಧಾರಣೆ ಮಾಡಲು ಸಾಧ್ಯ. ನಿಮ್ಮ ಸಂಪೂರ್ಣ ಉಪಯೋಗ ಪ್ರಕರಣಕ್ಕೆ ಮೊದಲ ಬಾರಿ ಸರಿ ಸೇರುವ ಸಿಸ್ಟಂ ಸಂದೇಶವನ್ನು ಹೊಂದಿರುವುದು ವಿರಳ. ಮೂಲ ಸಿಸ್ಟಂ ಸಂದೇಶವನ್ನು ಬದಲಾಯಿಸಿ, ಸಿಸ್ಟಂ ಮೂಲಕ ಓಡಿಸಿ ಸಣ್ಣ ಬದಲಾವಣೆಗಳನ್ನು ಮಾಡಿ ಫಲಿತಾಂಶಗಳನ್ನು ಹೋಲಿಸಿ ಮತ್ತು ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ.

## ಬೆದರಿಕೆಗಳನ್ನು ಗುರುತಿಸುವುದು

ನಂಬಬಹುದಾದ AI ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಿಸಲು, ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಗೆ ಅಪಾಯಗಳು ಮತ್ತು ಬೆದರಿಕೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳು ಹೊತ್ತು ಕಡಿಮೆಗೊಳಿಸುವುದು ಪ್ರಮುಖ. ನಾವು ಕೆಲವೇ AI ಏಜೆಂಟ್ ಗಾಗಿ ವಿವಿಧ ಬೆದರಿಕೆಗಳನ್ನು ನೋಡೋಣ ಮತ್ತು ನೀವು ಅದಕ್ಕಾಗಿ ಹೇಗೆ ಉತ್ತಮ ಯೋಜನೆ ಮತ್ತು ಸಿದ್ಧತೆ ಮಾಡಿಕೊಳ್ಳಬಹುದು.

![ಬೆದರಿಕೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](../../../translated_images/kn/understanding-threats.89edeada8a97fc0f.webp)

### ಕಾರ್ಯ ಮತ್ತು ಸೂಚನೆ

**ವಿವರಣೆ:** ದಾಳಿಕಾರರು AI ಏಜೆಂಟ್ ಗೆ ಸೂಚನೆಗಳು ಅಥವಾ ಗುರಿಗಳನ್ನು ಬದಲಾಯಿಸುವ ಪ್ರಯತ್ನ ಮಾಡುತ್ತಾರೆ ಪ್ರಾಂಪ್ಟಿಂಗ್ ಅಥವಾ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಮ್ಯಾನುಪ್ಯುಲേറ്റ് ಮಾಡುವ ಮೂಲಕ.

**ತಡೆಗಟ್ಟು**: AI ಏಜೆಂಟ್ ಪ್ರಕ್ರಿಯೆಗೂ ಮುನ್ನ ಅಪಾಯಕಾರಿ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಮಾನ್ಯತೆ ಪರಿಶೀಲನೆಗಳು ಮತ್ತು ಇನ್‌ಪುಟ್ ಶೋಧಕಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ. ಈ ದಾಳಿಗಳು ಸಾಮಾನ್ಯವಾಗಿ ಏಜೆಂಟ್ ಜೊತೆ ನಿಯಮಿತ ಸಂವಹನ ಬೇಕಾಗುತ್ತದೆ, ಆದ್ದರಿಂದ ಸಂಭಾಷಣೆಯ ತಿರುವಿನ ಸಂಖ್ಯೆಯನ್ನು ಮಿತಿಗೊಳಿಸುವುದು ಇಂತಹ ದಾಳಿಗಳನ್ನು ತಡೆಯುವ ಮತ್ತೊಂದು ಮಾರ್ಗವಾಗಿದೆ.

### ಅತಿ ಪ್ರಮುಖ ವ್ಯವಸ್ಥೆಗಳಿಗೆ ಪ್ರವೇಶ

**ವಿವರಣೆ**: AI ಏಜೆಂಟ್ حساس ಡೇಟಾವನ್ನು ಸಂಗ್ರಹಿಸುವ ವ್ಯವಸ್ಥೆಗಳು ಮತ್ತು ಸೇವೆಗಳಿಗೆ ಪ್ರವೇಶ ಹೊಂದಿದ್ದರೆ, ದಾಳಿಕಾರರು ಏಜೆಂಟ್ ಮತ್ತು ಈ ಸೇವೆಗಳ ನಡುವೆ ಸಂವಹನವನ್ನು ಹಾಳುಮಾಡಬಹುದು. ಇದು ನೇರ ದಾಳಿ ಅಥವಾ ಏಜೆಂಟ್ ಮೂಲಕ ಈ ವ್ಯವಸ್ಥೆಗಳು ಕುರಿತ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಲು ಅಸಹಾಯಕ ಪ್ರಯತ್ನಗಳಾಗಬಹುದು.

**ತಡೆಗಟ್ಟು**: AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ಬೇಕಾದಷ್ಟೇ ಪ್ರವೇಶ ನೀಡಬೇಕು ಇಂತಹ ದಾಳಿಗಳ ತಡೆಗೆ. ಏಜೆಂಟ್ ಮತ್ತು ವ್ಯವಸ್ಥೆಯ ನಡುವೆ ಸಂವಹನವೂ ಭದ್ರವಾಗಿರಬೇಕು. ದೃಢೀಕರಣ ಮತ್ತು ಪ್ರವೇಶ ನಿಯಂತ್ರಣವನ್ನು ಜಾರಿಗೊಳಿಸುವುದು ಇವುಗಳನ್ನು ಸಂರಕ್ಷಿಸಲು ಮತ್ತೊಂದು ವಿಧಾನ.

### ಸಂಪನ್ಮೂಲ ಮತ್ತು ಸೇವೆಭಾರಮಾಡುವಿಕೆ

**ವಿವರಣೆ:** AI ಏಜೆಂಟ್ಗಳು ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ವಿವಿಧ ಸಾಧನಗಳು ಮತ್ತು ಸೇವೆಗಳನ್ನು ಬಳಸಬಹುದು. ದಾಳಿಕಾರರು ಈ ಸಾಮರ್ಥ್ಯವನ್ನು ಬಳಸಿಕೊಂಡು AI ಏಜೆಂಟ್ ಮೂಲಕ ಹೆಚ್ಚಿನ ಸಂಖ್ಯೆಯ ವಿನಂತಿಗಳನ್ನು ಕಳುಹಿಸುವ ಮೂಲಕ ಈ ಸೇವೆಗಳಿಗೆ ದಾಳಿ ಮಾಡಬಹುದು, ಇದರಿಂದ ವ್ಯವಸ್ಥೆ ದೋಷಗಳು ಅಥವಾ ಹೆಚ್ಚಿನ ವೆಚ್ಚಗಳು ಸಂಭವಿಸಬಹುದು.

**ತಡೆಗಟ್ಟು:** AI ಏಜೆಂಟ್ ಒಂದು ಸೇವೆಗೆ ಮಾಡಬಹುದಾದ ವಿನಂತಿಗಳ ಸಂಖ್ಯೆಯನ್ನು ನಿಯಂತ್ರಿಸುವ ನೀತಿ ಜಾರಿಗೊಳಿಸಿ. ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಗೆ ಸಂಭಾಷಣೆಯ ತಿರುವುಗಳ ಮತ್ತು ವಿನಂತಿಗಳ ಸಂಖ್ಯೆಯನ್ನು ಮಿತಿಗೊಳಿಸುವುದು ಇಂತಹ ದಾಳಿಗಳನ್ನು ತಡೆಯುವ ಮತ್ತೊಂದು ವಿಧಾನ.

### ಜ್ಞಾನ ಆಧಾರ ವಿಷಭಕ್ಷಣೆ

**ವಿವರಣೆ:** ಈ ದಾಳಿ ನೇರವಾಗಿ AI ಏಜೆಂಟ್ ಮೇಲೆ ಗುರಿಯಾಗುವುದಿಲ್ಲ ಆದರೆ AI ಏಜೆಂಟ್ ಬಳಸುವ ಜ್ಞಾನ ಆಧಾರ ಮತ್ತು ಇತರ ಸೇವೆಗಳ ಮೇಲೆ ಗುರಿಯಾಗುತ್ತದೆ. ಇದು ಕಾರ್ಯವನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು AI ಏಜೆಂಟ್ ಉಪಯೋಗಿಸುವ ಡೇಟಾ ಅಥವಾ ಮಾಹಿತಿಯನ್ನು ಹಾಳುಮಾಡಬಹುದು, ಇದರಿಂದ ಬಳಕೆದಾರರಿಗೆ ಪಕ್ಷಪಾತದ ಅಥವಾ ಅನನುಕೂಲಿತ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಆಗಬಹುದು.

**ತಡೆಗಟ್ಟು:** AI ಏಜೆಂಟ್ ತನ್ನ ಕಾರ್ಯಪ್ರವಾಹಗಳಲ್ಲಿ ಬಳಸುವ ಡೇಟಾವನ್ನು ನಿಯಮಿತವಾಗಿ ಪರಿಶೀಲಿಸಿ. ಈ ಡೇಟಾಗೆ ಪ್ರವೇಶವು ಭದ್ರವಾಗಿದ್ದು, ವಿಶ್ವಾಸಾರ್ಹ ವ್ಯಕ್ತಿಗಳಿಂದ ಮಾತ್ರ ಬದಲಾಗುವಂತೆ ಮಾಡಿ ಇಂಥ ದಾಳಿಗಳನ್ನು ತಪ್ಪಿಸಬಹುದು.

### ಸರಣಿಬದ್ಧ ದೋಷಗಳು

**ವಿವರಣೆ:** AI ಏಜೆಂಟ್ಗಳು ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ವಿವಿಧ ಸಾಧನಗಳು ಮತ್ತು ಸೇವೆಗಳಿಗೆ ಪ್ರವೇಶ ಹೊಂದಿರುತ್ತವೆ. ದಾಳಿಕಾರರಿಂದ ಉಂಟಾಗುವ ದೋಷಗಳು AI ಏಜೆಂಟ್ ಸಂಪರ್ಕಿಸಿರುವ ಇತರ ವ್ಯವಸ್ಥೆಗಳ ವಿಫಲತೆಯನ್ನುಂಟು ಮಾಡುತ್ತವೆ, ಇದರಿಂದ ದಾಳಿ ಹೆಚ್ಚಾಗಿ ವ್ಯಾಪಕವಾಗುತ್ತದೆ ಮತ್ತು ತೊಂದರೆ ಪರಿಹಾರ ಕಷ್ಟವಾಗುತ್ತದೆ.

**ತಡೆಗಟ್ಟು**: ಇದನ್ನು ತಪ್ಪಿಸಲು ಒಂದು ವಿಧಾನವೆಂದರೆ AI ಏಜೆಂಟ್ ನೇರ ವ್ಯವಸ್ಥೆ ದಾಳಿಗಳನ್ನು ತಡೆಯಲು ಡೋಕರ್ ಕಂಟೈನರ್ ನಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವಂತೆ ಗಡಿಯಲ್ಲಿ ಇರಿಸುವುದು. ಕೆಲ ವ್ಯವಸ್ಥೆಗಳು ದೋಷ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡಿದಾಗ ಬ್ಯಾಕ್ಅಪ್ ಯಂತ್ರಣಗಳನ್ನು ಮತ್ತು ಪುನರಾವೃತ್ತಿ ತಂತ್ರಗಳನ್ನು ರಚಿಸುವುದು ದೊಡ್ಡ ವ್ಯವಸ್ಥೆ ವಿಫಲತೆಗಳನ್ನು ತಡೆಯುವ ಮತ್ತೊಂದು ವಿಧಾನ.

## ಹ್ಯೂಮನ್-ಇನ್-ದಿ-ಲೂಪ್

ನಂಬಬಹುದಾದ AI ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಗಳನ್ನು ನಿರ್ಮಿಸಲು ಮತ್ತೊಂದು ಪರಿಣಾಮಕಾರಿ ವಿಧಾನ ಹ್ಯೂಮನ್-ಇನ್-ದಿ-ಲೂಪ್. ಇದು ಬಳಕೆದಾರರು ಕಾರ್ಯನಿರ್ವಹಣೆಯ ಸಂದರ್ಭದಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುವ ಹರಿವು ಸೃಷ್ಟಿಸುತ್ತದೆ. ಬಳಕೆದಾರರು ಬಹು ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಾರೆ ಮತ್ತು ಪ್ರಕ್ರಿಯೆಯನ್ನು ಅನುಮೋದನೆ ಅಥವಾ ರದ್ದುಮಾಡುವ ಮೂಲಕ ಸಹಾಯ ಮಾಡುತ್ತಾರೆ.

![ಲೂಪ್‌ನಲ್ಲಿರುವ ಮನುಷ್ಯ](../../../translated_images/kn/human-in-the-loop.5f0068a678f62f4f.webp)

ಈ ತತ್ವವನ್ನು ಹೇಗೆ ಜಾರಿಗೆ ತರಲಾಗಿದೆ ಎಂದು ತೋರಿಸಲು Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ ಕೆಳಗಿನ ಕೋಡ್ ಉದಾಹರಣೆ:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# ಮಾನವ-ಇನ್-ದಿ-ಲುಪ್ ಅನುಮೋದನೆಯೊಂದಿಗೆ провೈಡರ್ ಅನ್ನು ರಚಿಸಿ
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# ಮಾನವ ಅನುಮೋದನೆ ಹಂತದೊಂದಿಗೆ ಏಜೆಂಟ್ ರಚಿಸಿ
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ಬಳಕೆದಾರನು ಪ್ರತಿಕ್ರಿಯೆ ಪರಿಶೀಲಿಸಿ ಅನುಮೋದಿಸಬಹುದು
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## ಸಮಾರೋಪ

ನಂಬಬಹುದಾದ AI ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಿಸಲು ಜಾಗರೂಕ ವಿನ್ಯಾಸ, ಬಲವಾದ ಭದ್ರತಾ ಕ್ರಮಗಳು ಮತ್ತು ನಿರಂತರ ಪುನರಾವೃತ್ತಿ ಅಗತ್ಯವಿದೆ. ಸಂರಚಿತ ಮೆಟಾ ಪ್ರಾಂಪ್ಟಿಂಗ್ ವ್ಯವಸ್ಥೆಗಳ ಅನುಷ್ಠಾನ, ಸಾಧ್ಯತೆಯಾದ ಬೆದರಿಕೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು ಮತ್ತು ತಡೆಗಟ್ಟುವ ತಂತ್ರಗಳನ್ನು ಅನ್ವಯಿಸುವ ಮೂಲಕ, ನಿರ್ಮಾಪಕರು ಸುರಕ್ಷಿತ ಮತ್ತು ಪರಿಣಾಮಕಾರಿ AI ಏಜೆಂಟ್ಸ್ ರಚಿಸಬಹುದು. ಜೊತೆಗೆ, ಹ್ಯೂಮನ್ಇನ್ ದಿ ಲೂಪ್ ವಿಧಾನವನ್ನು ಒಳಗೊಂಡರೆ AI ಏಜೆಂಟ್ಸ್ ಬಳಕೆದಾರರ ಅವಶ್ಯಕತೆಗಳಿಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತಾ ಅಪಾಯಗಳನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತವೆ. AI ಮುಂದುವರೆಸುತ್ತಿರುವಂತೆ ಭದ್ರತೆ, ಗೌಪ್ಯತೆ ಮತ್ತು ನೈತಿಕ ವಿಚಾರಗಳ ಮೇಲೆ ಸಕ್ರೀಯ ದೃಷ್ಟಿಕೋನವನ್ನು ಉಳಿಸುವುದು AI ಚಾಲಿತ ವ್ಯವಸ್ಥೆಗಳಲ್ಲಿ ನಂಬಿಕೆ ಮತ್ತು ವಿಶ್ವಾಸಾರ್ಹತೆಯನ್ನು ಹೆಚ್ಚಿಸಲು ಮಿನಚುನಿಕೆ.

### ನಂಬಬಹುದಾದ AI ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಿಸುವ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿವೆಯಾ?

ಇನ್ನಷ್ಟು ಕಲಿಯುವವರಿಗೆ ಭೇಟಿ ನೀಡಲು, ಆಫೀಸ್ ಕಿರುವ ವೇಳಾಪಟ್ಟಿಗೆ ಹಾಜರಾಗಲು, ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ಸ್ ಬಗ್ಗೆ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಪಡೆಯಲು [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ಜಾಯಿಂನ್ ಆಗಿ.

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ಉತ್ತರದಾಯಕ AI ಅವಲೋಕನ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ಜನನ AI ಮಾದರಿಗಳು ಮತ್ತು AI ಅಪ್ಲಿಕೇಷನ್‌ಗಳ ಮೌಲ್ಯಮಾಪನ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ಭದ್ರತಾ ವ್ಯವಸ್ಥೆಯ ಸಂದೇಶಗಳು</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ಅಪಾಯ ಮೌಲ್ಯಮಾಪನ ಟೆಂಪ್ಲೇಟ್</a>

## ಹಿಂದಿನ ಪಾಠ

[ಏಜೆಂಟಿಕ್ RAG](../05-agentic-rag/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಆಯೋಜನೆ ವಿನ್ಯಾಸ ಮಾದರಿ](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತ್ಯಾಜ್ಯ ಘೋಷಣೆ**:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತೇವೆ ಆದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿಡಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿನ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮಾಹಿತಿಯ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೆ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯానಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗಿರಲಾರವು.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->