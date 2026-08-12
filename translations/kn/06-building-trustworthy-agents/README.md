[![ವಿಶ್ವಾಸಾರ್ಹ AI ಏಜೆಂಟ್ಸ್](../../../translated_images/kn/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ಈ ಪಾಠದ ವಿಡಿಯೋವನ್ನು ನೋಡಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# ವಿಶ್ವಾಸಾರ್ಹ AI ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಾಣ

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ಕವರ್ ಮಾಡುವುದು:

- ಸುರಕ್ಷಿತ ಮತ್ತು ಪರಿಣಾಮಕಾರಿಯಾದ AI ಏಜೆಂಟ್ಸ್ ಅನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸಬೇಕು ಮತ್ತು ನಿಯೋಜಿಸಬೇಕು
- AI ಏಜೆಂಟ್ಸ್ ಅಭಿವೃದ್ಧಿಪಡಿಸುವಾಗ ಮುಖ್ಯ ಭದ್ರತಾ ಪರಿಗಣನೆಗಳು.
- AI ಏಜೆಂಟ್ಗಳನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸುವಾಗ ಡೇಟಾ ಮತ್ತು ಬಳಕೆದಾರ ಗೌಪ್ಯತೆಯನ್ನು ಹೇಗೆ ಉಳಿಸಿಕೊಳ್ಳಬೇಕು.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಹೇಗೆ ತಿಳಿಯಬಹುದು:

- AI ಏಜೆಂಟ್ಸ್ ರಚಿಸುವಾಗ ಅಪಾಯಗಳನ್ನು ಗುರುತುಹಚ್ಚಿ ಮತ್ತು ತಡೆಗಟ್ಟುವಿಕೆ.
- ಡೇಟಾ ಮತ್ತು ಪ್ರವೇಶವು ಸರಿಯಾಗಿ ನಿರ್ವಹಿಸಲ್ಪಡುವಂತೆ ಭದ್ರತಾ ಕ್ರಮಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು.
- ಡೇಟಾ ಗೌಪ್ಯತೆ ಉಳಿಸಿದ ಹಾಗು ಗುಣಮಟ್ಟದ ಬಳಕೆದಾರ ಅನುಭವ ಒದಗಿಸುವ AI ಏಜೆಂಟ್ಸ್ ರಚಿಸುವುದು.

## ಸುರಕ್ಷತೆ

ನಾವು ಮೊದಲು ಸುರಕ್ಷಿತ ಏಜೆಂಟಿಕ್ ಅಪ್ಲಿಕೇಶನ್ಗಳನ್ನು ನಿರ್ಮಿಸುವ ಬಗ್ಗೆ ನೋಡುವೆವು. ಸುರಕ್ಷತೆ ಎಂದರೆ AI ಏಜೆಂಟ್ ವಿನ್ಯಾಸ ಮಾಡಿದ್ದಂತೆ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದು. ಏಜೆಂಟಿಕ್ ಅಪ್ಲಿಕೇಶನ್ಗಳ ನಿರ್ಮಾಪಕರಾಗಿ, ನಾವು ಸುರಕ್ಷತೆಗೆ ಗರಿಷ್ಠ ಆದ್ಯತೆ ನೀಡಲು ವಿಧಾನಗಳು ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ಹೊಂದಿದ್ದೇವೆ:

### ಸಿಸ್ಟಮ್ ಸಂದೇಶ ಫ್ರೇಮ್ವರ್ಕ್ ನಿರ್ಮಾಣ

ನೀವು ಲಾರ್ಜ್ ಲ್ಯಾಂಗ್ವೇಜ್ ಮಾದರಿಗಳನ್ನು (LLMs) ಬಳಸಿಕೊಂಡು AI ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಿದ್ದು ಇದೆಯಾದರೆ, ದೃಢವಾದ ಸಿಸ್ಟಮ್ ಪ್ರಂಪ್ಟ್ ಅಥವಾ ಸಿಸ್ಟಮ್ ಸಂದೇಶ ವಿನ್ಯಾಸ的重要ತೆ ನಿಮಗೆ ತಿಳಿದಿರುತ್ತದೆ. ಈ ಪ್ರಂಪ್ಟ್ಗಳು LLM ಯು ಬಳಕೆದಾರ ಮತ್ತು ಡೇಟಾದೊಂದಿಗೆ ಹೇಗೆ ಸಂವಹನ ನಡೆಸಬೇಕೆಂಬ ಮೆಟಾ ನಿಯಮಗಳು, ಸೂಚನೆಗಳು ಮತ್ತು ಮಾರ್ಗಸೂಚಿಗಳನ್ನು ಸ್ಥಾಪಿಸುತ್ತವೆ.

AI ಏಜೆಂಟ್ಗಾಗಿ, ಸಿಸ್ಟಮ್ ಪ್ರಂಪ್ಟ್ ಇನ್ನಷ್ಟು ಪ್ರಮುಖವಾಗಿದೆ ಏಕೆಂದರೆ AI ಏಜೆಂಟ್ಗಳು ನಾವು ವಿನ್ಯಾಸ ಮಾಡಿರುವ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ಬಹುಶಃ ನಿಯತ ಸೂಚನೆಗಳನ್ನು ಅಗತ್ಯವಿಡುತ್ತವೆ.

ಹೆಚ್ಚು ವ್ಯಾಪಕ ಸಿಸ್ಟಮ್ ಪ್ರಂಪ್ಟ್ ಗಳನ್ನು ರಚಿಸಲು, ನಾವು ನಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಒಬ್ಬ ಅಥವಾ ಹೆಚ್ಚು ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸಿಸ್ಟಮ್ ಸಂದೇಶ ಫ್ರೇಮ್ವರ್ಕ್ ಉಪಯೋಗಿಸಬಹುದು:

![ಸಿಸ್ಟಮ್ ಸಂದೇಶ ಫ್ರೇಮ್ವರ್ಕ್ ನಿರ್ಮಾಣ](../../../translated_images/kn/system-message-framework.3a97368c92d11d68.webp)

#### ಹಂತ 1: ಮೆಟಾ ಸಿಸ್ಟಮ್ ಸಂದೇಶ ರಚಿಸಿ 

ಮೆಟಾ ಪ್ರಂಪ್ಟ್ ಅನ್ನು LLM ಮೂಲಕ ನಾವು ರಚಿಸುವ ಏಜೆಂಟ್ಗಳಿಗೆ ಸಿಸ್ಟಮ್ ಪ್ರಂಪ್ಟ್‌ಗಳನ್ನು ಉತ್ಪಾದಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ. ನಾವು ಇದನ್ನು ಟೆಂಪ್ಲೇಟಾಗಿ ವಿನ್ಯಾಸ ಮಾಡುತ್ತೇವೆ, ಅವಶ್ಯಕತೆಯಾದರೆ ಬಹು ಏಜೆಂಟ್ಗಳನ್ನು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ರಚಿಸಲು.

LLM ಗೆ ನೀಡುವ ಮೆಟಾ ಸಿಸ್ಟಮ್ ಸಂದೇಶ ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ಹಂತ 2: ಮೂಲ ಪ್ರಂಪ್ಟ್ ರಚಿಸಿ

ಮುಂದಿನ ಹಂತವೆಂದರೆ AI ಏಜೆಂಟ್ ಅನ್ನು ವಿವರಿಸುವ ಮೂಲ ಪ್ರಂಪ್ಟ್ ರಚಿಸುವುದು. ನೀವು ಏಜೆಂಟ್‌ನ ಪಾತ್ರ, ಏಜೆಂಟ್ ಪೂರ್ಣಗೊಳಿಸುವ ಕಾರ್ಯಗಳು ಮತ್ತು ಇತರೆ ಹೊಣೆಗಾರಿಕೆಗಳನ್ನು ಸೇರಿಸಬೇಕು.

ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ಹಂತ 3: ಮೂಲ ಸಿಸ್ಟಮ್ ಸಂದೇಶವನ್ನು LLM ಗೆ ನೀಡಿ

ಈಗ ನಾವು ಈ ಸಿಸ್ಟಮ್ ಸಂದೇಶವನ್ನು ಉತ್ತಮಗೊಳಿಸಬಹುದು, ಮೆಟಾ ಸಿಸ್ಟಮ್ ಸಂದೇಶವನ್ನು ಸಿಸ್ಟಮ್ ಸಂದೇಶವಾಗಿ ಮತ್ತು ನಮ್ಮ ಮೂಲ ಸಿಸ್ಟಮ್ ಸಂದೇಶವನ್ನು ನೀಡುವುದರಿಂದ.

ಇದು ನಮ್ಮ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಮಾರ್ಗದರ್ಶನ ಮಾಡಲು ಉತ್ತಮ ವಿನ್ಯಾಸದ ಸಿಸ್ಟಮ್ ಸಂದೇಶವನ್ನು ಉತ್ಪಾದಿಸುತ್ತದೆ:

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

#### ಹಂತ 4: ಪುನರಾವರ್ತಿಸಿ ಮತ್ತು ಸುಧಾರಣೆ ಮಾಡಿ

ಈ ಸಿಸ್ಟಮ್ ಸಂದೇಶ ಫ್ರೇಮ್ವರ್ಕ್‌ನ ಮೌಲ್ಯವೆಂದರೆ ಬಹು ಏಜೆಂಟ್‌ಗಳಿಂದ ಸುಲಭವಾಗಿ ಸಿಸ್ಟಮ್ ಸಂದೇಶಗಳನ್ನು ವಿಸ್ತರಿಸಲು ಹಾಗೂ ನಿಮ್ಮ ಸಿಸ್ಟಮ್ ಸಂದೇಶಗಳನ್ನು ಕಾಲಕಾಲಕ್ಕೆ ಸುಧಾರಿಸಲು ಸಾಧ್ಯವಾಗುವುದು. ನಿಮ್ಮ ಪೂರ್ಣ ಬಳಕೆ ಪ್ರಕರಣಕ್ಕೆ ಪೂರಕವಾಗುವ ಮೊದಲ ಬಾರಿ ಸಿಸ್ಟಮ್ ಸಂದೇಶ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದು ಅಪರೂಪ. ಮೂಲ ಸಿಸ್ಟಮ್ ಸಂದೇಶವನ್ನು ಬದಲಾಯಿಸಿ ಸಿಸ್ಟಮ್ ಮೂಲಕ ರನ್ ಮಾಡುವ ಮೂಲಕ ಸಣ್ಣ ತಿದ್ದುಪಡಿ ಮತ್ತು ಸುಧಾರಣೆಗಳನ್ನು ಮಾಡಬಹುದು. ಇದು ನಿಮ್ಮ ಫಲಿತಾಂಶಗಳನ್ನು ಹೋಲಿಸಿ ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

## ಧಮ್ಕಿಗಳ ಅರಿವು

ವಿಶ್ವಾಸಾರ್ಹ AI ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಿಸಲು, ನಿಮ್ಮ AI ಏಜೆಂಟ್‌ಗೆ ಅಪಾಯಗಳು ಮತ್ತು ಧಮ್ಕಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು ಹಾಗೂ ತಡೆಗಟ್ಟುವುದು ಮುಖ್ಯ. AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ಇರುವ ಕೆಲ ವಿಧದ ಧಮ್ಕಿಗಳನ್ನು ಮತ್ತು ಅವುಗಳಿಗೆ ನೀವು ಹೇಗೆ ಉತ್ತಮವಾಗಿ ಯೋಜನೆ ರೂಪಿಸಿ ತಯಾರಾಗಬಹುದು ಎಂಬುದನ್ನು ನೋಡೋಣ.

![ಧಮ್ಕಿಗಳ ಅರಿವು](../../../translated_images/kn/understanding-threats.89edeada8a97fc0f.webp)

### ಕಾರ್ಯ ಮತ್ತು ಸೂಚನೆ

**ವಿವರಣೆ:** ದ್ರೋಹಿಗಳು AI ಏಜೆಂಟ್‌ನ ಸೂಚನೆಗಳು ಅಥವಾ ಗುರಿಗಳನ್ನು prompting ಅಥವಾ ಇನ್ಪುಟ್‌ಗಳನ್ನು ತ್ರಾಸು ಮಾಡುವುದು ಮೂಲಕ ಬದಲಾಯಿಸಲು ಯತ್ನಿಸುತ್ತಾರೆ.

**ತಡೆಗಟ್ಟುವಿಕೆ**: ಅಪಾಯಕಾರಿ prompting ಅನ್ನು AI ಏಜೆಂಟ್ ಪ್ರಕ್ರಿಯೆಗೆ ಮೊದಲು ಪತ್ತೆಹಚ್ಚಲು ಮಾನ್ಯತೆ ಪರಿಶೀಲನೆಗಳು ಮತ್ತು ಇನ್ಪುಟ್ ಫಿಲ್ಟರ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಿ. ಈ ದಾಳಿಗಳು ಸಾಮಾನ್ಯವಾಗಿ ಏಜೆಂಟ್‌తో ನಿಯತ ಸಂವಹನವನ್ನು ಕೋರಲು ಕಾರಣವಾಗುವುದರಿಂದ, ಸಂವಾದದ ತಿರುವುಗಳ ಸಂಖ್ಯೆಯನ್ನು ಮಿತಿಗೊಳಿಸುವುದು ಇವುಗಳನ್ನು ತಡೆಯುವ ಮತ್ತೊಂದು ವಿಧಾನ.

### ಮಹತ್ವದ ವ್ಯವಸ್ಥೆಗಳ ಪ್ರವೇಶ

**ವಿವರಣೆ**: AI ಏಜೆಂಟ್ ಗಾತ್ರವಾದ ಡೇಟಾವನ್ನು ಸಂಗ್ರಹಿಸುವ ವ್ಯವಸ್ಥೆಗಳು ಮತ್ತು ಸೇವೆಗಳ ಪ್ರವೇಶ ಹೊಂದಿದ್ದರೆ, ದ್ರೋಹಿಗಳು ಏಜೆಂಟ್ ಮತ್ತು ಈ ಸೇವೆಗಳ ನಡುವೆ ಸಂವಹನವನ್ನು ಭೇದಿಸಬಹುದು. ಇವು ನೇರ ದಾಳಿಗಳು ಅಥವಾ ಏಜೆಂಟ್ ಮೂಲಕ ಈ ವ್ಯವಸ್ಥೆಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿಯನ್ನು ಪಡೆದಲು ಅಪ್ರತ್ಯಕ್ಷ ಪ್ರಯತ್ನಗಳಾಗಬಹುದು.

**ತಡೆಗಟ್ಟುವಿಕೆ**: ಈ ರೀತಿಯ ದಾಳಿಗಳನ್ನು ತಡೆಯಲು AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ಕೇವಲ ಅಗತ್ಯದ ಅವಕಾಶ ಮಾತ್ರ ನೀಡಬೇಕು. ಏಜೆಂಟ್ ಮತ್ತು ವ್ಯವಸ್ಥೆಯ ನಡುವೆ ಸಂವಹನವೂ ಸುರಕ್ಷಿತವಾಗಿರಬೇಕು. ಪ್ರಾಮಾಣೀಕರಣ ಮತ್ತು ಪ್ರವೇಶ ನಿಯಂತ್ರಣಗಳನ್ನು ಜಾರಿಗೆ ತರಲು ಇದು ಇನ್ನೊಂದು ರಕ್ಷಣೆ ವಿಧಾನ.

### ಸಂಪನ್ಮೂಲ ಮತ್ತು ಸೇವೆ ಮೇಲೆ ಭಾರವಾದ ಸಾಗಣೆ

**ವಿವರಣೆ:** AI ಏಜೆಂಟ್‌ಗಳು ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ವಿವಿಧ ಸಾಧನಗಳು ಮತ್ತು ಸೇವೆಗಳನ್ನು ಪ್ರವೇಶಿಸಬಹುದು. ದ್ರೋಹಿಗಳು AI ಏಜೆಂಟ್ ಮೂಲಕ ಸೇವೆಗೆ ಹೆಚ್ಚಿನ ಸಂಖ್ಯೆಯ ವಿನಂತಿಗಳನ್ನು ಕಳುಹಿಸುವ ಮೂಲಕ ಈ ಸೇವೆಗಳಿಗೆ ದಾಳಿ ಮಾಡಬಹುದು, ಇದರಿಂದ ವ್ಯವಸ್ಥೆ ವಿಫಲತೆಗಳು ಅಥವಾ ಹೆಚ್ಚಿನ ವೆಚ್ಚಗಳು ಸಂಭವಿಸಬಹುದು.

**ತಡೆಗಟ್ಟುವಿಕೆ:** AI ಏಜೆಂಟ್ ಒಂದು ಸೇವೆಗೆ ಮಾಡುವ ವಿನಂತಿಗಳ ಸಂಖ್ಯೆಯನ್ನು ಮಿತಿಗೊಳಿಸಲು ನೀತಿ ಜಾರಿಗೆ ತರುವುದು. ನಿಮ್ಮ AI ಏಜೆಂಟ್‌ಗೆ ಸಂವಾದದ ತಿರುವುಗಳ ಮತ್ತು ವಿನಂತಿಗಳ ಸಂಖ್ಯೆಯನ್ನು ಮಿತಿಗೊಳಿಸುವುದು ಇವುಗಳನ್ನು ತಡೆಯುವ ಮತ್ತೊಂದು ವಿಧಾನ.

### ಜ್ಞಾನಾಧಾರ ವಿಷ ಪ್ರಾಯೋಗ

**ವಿವರಣೆ:** ಈ ರೀತಿಯ ದಾಳಿ ನೇರವಾಗಿ AI ಏಜೆಂಟ್ ಮೇಲೆ ನಡೆಸುವುದಿಲ್ಲ ಆದರೆ AI ಏಜೆಂಟ್ ಬಳಸುವ ಜ್ಞಾನಾಧಾರ ಮತ್ತು ಇತರ ಸೇವೆಗಳನ್ನು ಗುರಿಯಾಗಿಸಿಕೊಂಡಿರುತ್ತದೆ. ಇದರಲ್ಲಿ AI ಏಜೆಂಟ್ ಕಾರ್ಯ ಪೂರ್ಣಗೊಳಿಸಲು ಬಳಸುವ ಡೇಟಾ ಅಥವಾ ಮಾಹಿತಿಯನ್ನು ದುರ್ನಿಗ್ರಹಣ ಮಾಡುವುದು ಸೇರಿರಬಹುದು, ಇದರಿಂದ ಬಳಕೆದಾರಿಗೆ ಪೂರ್ವಗ್ರಹಿತ ಅಥವಾ ಅಕಾಯಕ ಉತ್ತರಗಳು ಬರುವ ಸಾಧ್ಯತೆ.

**ತಡೆಗಟ್ಟುವಿಕೆ:** AI ಏಜೆಂಟ್ ಅದರ ಕಾರ್ಯಹೊಂದಿಕೆಯಲ್ಲಿಉಪಯೋಗಿಸುವ ಡೇಟಾವನ್ನು ನಿಯಮಿತವಾಗಿ ಪರಿಶೀಲಿಸಿ. ಈ ಡೇಟಾವಿಗೆ ಪ್ರವೇಶವು ಸುರಕ್ಷಿತವಾಗಿದ್ದು ಮತ್ತು ಕೇವಲ ವಿಶ್ವಾಸಾರ್ಹ ವ್ಯಕ್ತಿಗಳಿಂದ ಮಾತ್ರ ಬದಲಾಯಿಸಲಾಗುತ್ತದೆ ಎಂಬುದನ್ನು ಖಾತ್ರಿಪಡಿಸಿ.

### ಸರಣಿ ದೋಷಗಳು

**ವಿವರಣೆ:** AI ಏಜೆಂಟ್ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ವಿವಿಧ ಸಾಧನಗಳು ಮತ್ತು ಸೇವೆಗಳಿಗೆ ಪ್ರವೇಶಿಸುತ್ತದೆ. ದ್ರೋಹಿಗಳು ತಂದ ದೋಷಗಳು ಈ AI ಏಜೆಂಟ್ ಸಂಪರ್ಕದಲ್ಲಿರುವ ಇತರ ವ್ಯವಸ್ಥೆಗಳ ವೈಫಲ್ಯಗಳಿಗೆ ಕಾರಣವಾಗಿ ದಾಳಿ ಹೆಚ್ಚು ವ್ಯಾಪಕವಾಗುತ್ತದೆಯೂ, ಸಮಸ್ಯೆಗಳನ್ನು ಪರಿಹರಿಸುವುದೇ ಕಷ್ಟವಾಗುತ್ತದೆ.

**ತಡೆಗಟ್ಟುವಿಕೆ**: ಇದನ್ನು ತಡೆಯಲು ಒಂದು ವಿಧಾನವೆಂದರೆ AI ಏಜೆಂಟ್ ಅನ್ನು ಸೀಮಿತ ಪರಿಸರದಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವಂತೆ ಮಾಡುವುದು, ಉದಾ: ಡಾಕರ್ ಕಂಟೈನರ್‌ನಲ್ಲಿ ಕಾರ್ಯಗಳನ್ನು ನಡೆಸುವುದು, ನೇರ ವ್ಯವಸ್ಥೆ ದಾಳಿಗಳನ್ನು ತಡೆಯಲು. ಕೆಲ ವ್ಯವಸ್ಥೆಗಳು ದೋಷ ಸೂಚಿಸಿದಾಗ ಬ್ಯಾಕ್ಅಪ್ ಕ್ರಮಗಳು ಮತ್ತು ಮರುಪ್ರಯತ್ನ ತಂತ್ರಗಳನ್ನು ತಯಾರಿಸುವುದು ದೊಡ್ಡ ವ್ಯವಸ್ಥೆ ವೈಫಲ್ಯಗಳನ್ನು ತಡೆಯಲು ಮತ್ತೊಂದು ಸಾಧನ.

## ಮಾನವ-ಇನ್ಫ-ದಿ-ಲುಪ್

ವಿಶ್ವಾಸಾರ್ಹ AI ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಗಳನ್ನು ಇನ್ನೊಂದು ಪರಿಣಾಮಕಾರಿ ವಿಧಾನವೆಂದರೆ ಮಾನವ-ಇನ್ಫ-ದಿ-ಲುಪ್ ಉಪಯೋಗಿಸುವುದು. ಇದು ಬಳಕೆದಾರರು ಸಂಚಲನದ ಸಮಯದಲ್ಲಿ ಏಜೆಂಟ್ ಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುವ ಹರಿವು ರಚಿಸುತ್ತದೆ. ಬಳಕೆದಾರರು ಬಹು ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳಾಗಿದ್ದು ಚಾಲನೆಯಲ್ಲಿರುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಅನುಮೋದಿಸಲು ಅಥವಾ ನಿಲ್ಲಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತಾರೆ.

![ಮಾನವ ಇನ ದ ಲೂಪ್](../../../translated_images/kn/human-in-the-loop.5f0068a678f62f4f.webp)

ಈ ಕಲ್ಪನೆಯನ್ನು ಜಾರಿಗೆ ತರುವುದನ್ನು ತೋರಿಸಲು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ ಕೆಳಗಿನ ಕೋಡ್ ಉಲ್ಲೇಖ ಇಲ್ಲಿದೆ:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# ಮಾನವನ ಅನುಮೋದನೆಯೊಂದಿಗೆ ಪ್ರೊವೈಡರ್ ಅನ್ನು ರಚಿಸಿ
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ಮಾನವ ಅನುಮೋದನೆ ಹಂತದೊಂದಿಗೆ ಏಜೆಂಟ್ ಅನ್ನು ರಚಿಸಿ
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ಬಳಕೆದಾರರು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ ಅನುಮೋದಿಸಬಹುದು
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## ಸಮಾರೋಪ

ವಿಶ್ವಾಸಾರ್ಹ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಜಾಗರೂಕ ವಿನ್ಯಾಸ, ದೃಢ ಭದ್ರತಾ ಕ್ರಮಗಳು ಮತ್ತು ನಿರಂತರ ಪುನರಾವರ್ತನೆ ಅಗತ್ಯ. ಸಂರಚಿತ ಮೆಟಾ ಪ್ರಂಪ್ಟ್ ಸಿಸ್ಟಮ್‌ಗಳನ್ನು ಜಾರಿಗೆ ತಂದರೆ, ಸಾಧ್ಯವಾದ ಧಮ್ಕಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಂಡು ತಡೆಗಟ್ಟುವ ತಂತ್ರಗಳನ್ನು ಅನುಸರಿಸಿದರೆ, ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರು ಸುರಕ್ಷಿತ ಮತ್ತು ಪರಿಣಾಮಕಾರಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಬಹುದು. ಹೆಚ್ಚುವರಿ, ಮಾನವ-ಇನ್ಫ-ದಿ-ಲುಪ್ ವಿಧಾನವನ್ನು ಅಳವಡಿಸಿದರೆ AI ಏಜೆಂಟ್‌ಗಳು ಬಳಕೆದಾರ ಅಗತ್ಯಗಳೊಂದಿಗೆ ಸಮ್ಮಿಲನ ಹೊಂದಿ ಅಪಾಯಗಳನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತವೆ. AI ಮುಂದುವರಿಯುವಂತೆ ಭದ್ರತೆ, ಗೌಪ್ಯತೆ ಮತ್ತು ನೈತಿಕ ಪರಿಗಣನೆಗಳ ಮೇಲೆ ಮುಂಚೂಣಿಯಲ್ಲಿರುವುದು AI ಚಾಲಿತ ವ್ಯವಸ್ಥೆಗಳಲ್ಲಿ ವಿಶ್ವಾಸ ಮತ್ತು ನಂಬಿಕೆಯನ್ನು ಹೆಚ್ಚಿಸುವುದಕ್ಕೆ ಮುಖ್ಯವಾಗಲಿದೆ.

## ಕೋಡ್ ಉದಾಹರಣೆಗಳು

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): ಮೆಟಾ-ಪ್ರಂಪ್ಟ್ ಸಿಸ್ಟಮ್-ಸಂದೇಶ ಫ್ರೇಮ್ವರ್ಕ್ ಹಂತ-ಹಂತದ ಪ್ರದರ್ಶನ.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): ಕಾರ್ಯ ಪೂರ್ವ ಅನುಮೋದನಾ ಗೇಟುಗಳು, ಅಪಾಯ ಹಂತೀಕರಣ ಮತ್ತು ವಿಶ್ವಾಸಾರ್ಹ ಏಜೆಂಟ್‌ಗಳಿಗಾಗಿ ಲಾಗ್ ಪತ್ತೆ.

### ವಿಶ್ವಾಸಾರ್ಹ AI ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಿಸುವ ಕುರಿತು ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿವೆಯಾ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ನಲ್ಲಿ ಸೇರಿ ಇತರ ಕಲಿಯುವವರನ್ನು ಭೇಟಿ ಮಾಡಿ, ಕಚೇರಿ ಸಮಯಗಳಿಗೆ ಹಾಜರಾಗಿರಿ ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ದೊರಕಿಸಿ.

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ಜವಾಬ್ದಾರಿಯಾದ AI ಅವಲೋಕನ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ಜನರೇಟಿವ್ AI ಮಾದರಿಗಳು ಮತ್ತು AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ಮೌಲ್ಯಮಾಪನ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ಸುರಕ್ಷತಾ ಸಿಸ್ಟಮ್ ಸಂದೇಶಗಳು</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ಅಪಾಯ ಮೌಲ್ಯಮಾಪನ ಟೆಂಪ್ಲೇಟು</a>

## ಹಿಂದಿನ ಪಾಠ

[Agentic RAG](../05-agentic-rag/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಯೋಜನೆ ವಿನ್ಯಾಸ ಮಾದರಿ](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->