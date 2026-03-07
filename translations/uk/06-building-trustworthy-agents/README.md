[![Надійні агенти ШІ](../../../translated_images/uk/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Побудова надійних агентів ШІ

## Introduction

This lesson will cover:

- How to build and deploy safe and effective AI Agents
- Important security considerations when developing AI Agents.
- How to maintain data and user privacy when developing AI Agents.

## Learning Goals

After completing this lesson, you will know how to:

- Identify and mitigate risks when creating AI Agents.
- Implement security measures to ensure that data and access are properly managed.
- Create AI Agents that maintain data privacy and provide a quality user experience.

## Safety

Let's first look at building safe agentic applications. Safety means that the AI agent performs as designed. As builders of agentic applications, we have methods and tools to maximize safety:

### Building a System Message Framework

If you have ever built an AI application using Large Language Models (LLMs), you know the importance of designing a robust system prompt or system message. These prompts establish the meta rules, instructions, and guidelines for how the LLM will interact with the user and data.

For AI Agents, the system prompt is even more important as the AI Agents will need highly specific instructions to complete the tasks we have designed for them.

To create scalable system prompts, we can use a system message framework for building one or more agents in our application:

![Побудова структури системних повідомлень](../../../translated_images/uk/system-message-framework.3a97368c92d11d68.webp)

#### Step 1: Create a Meta System Message 

The meta prompt will be used by an LLM to generate the system prompts for the agents we create. We design it as a template so that we can efficiently create multiple agents if needed.

Here is an example of a meta system message we would give to the LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Step 2: Create a basic prompt

The next step is to create a basic prompt to describe the AI Agent. You should include the role of the agent, the tasks the agent will complete, and any other responsibilities of the agent.

Here is an example:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Step 3: Provide Basic System Message to LLM

Now we can optimize this system message by providing the meta system message as the system message and our basic system message.

This will produce a system message that is better designed for guiding our AI agents:

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

#### Step 4: Iterate and Improve

The value of this system message framework is to be able to scale creating system messages from multiple agents easier as well as improving your system messages over time. It is rare you will have a system message that works the first time for your complete use case. Being able to make small tweaks and improvements by changing the basic system message and running it through the system will allow you to compare and evaluate results.

## Understanding Threats

To build trustworthy AI agents, it is important to understand and mitigate the risks and threats to your AI agent. Let's look at only some of the different threats to AI agents and how you can better plan and prepare for them.

![Розуміння загроз](../../../translated_images/uk/understanding-threats.89edeada8a97fc0f.webp)

### Task and Instruction

**Опис:** Зловмисники намагаються змінити інструкції або цілі агента ШІ шляхом підказування або маніпулювання вхідними даними.

**Пом'якшення**: Виконуйте перевірки валідації та фільтри вхідних даних, щоб виявляти потенційно небезпечні підкази до їх обробки агентом ШІ. Оскільки ці атаки зазвичай потребують частої взаємодії з агентом, обмеження кількості ходів у розмові — ще один спосіб запобігти таким типам атак.

### Access to Critical Systems

**Опис**: Якщо агент ШІ має доступ до систем і сервісів, які зберігають конфіденційні дані, зловмисники можуть скомпрометувати комунікацію між агентом і цими сервісами. Це можуть бути прямі атаки або непрямі спроби здобути інформацію про ці системи через агента.

**Пом'якшення**: Агентам ШІ слід надавати доступ до систем лише за принципом необхідності, щоб запобігти таким типам атак. Комунікація між агентом і системою також має бути захищеною. Впровадження автентифікації та контролю доступу — ще один спосіб захисту цієї інформації.

### Resource and Service Overloading

**Опис:** Агенти ШІ можуть звертатися до різних інструментів і сервісів для виконання завдань. Зловмисники можуть використати цю здатність для атаки на ці сервіси, надсилаючи велику кількість запитів через агента ШІ, що може призвести до відмов у роботі систем або високих витрат.

**Пом'якшення:** Впровадьте політики для обмеження кількості запитів, які агент ШІ може надсилати до сервісу. Обмеження кількості ходів розмови та запитів до вашого агента ШІ — ще один спосіб запобігти таким типам атак.

### Knowledge Base Poisoning

**Опис:** Цей тип атаки не спрямований безпосередньо на агента ШІ, а на базу знань та інші сервіси, які агент ШІ використовуватиме. Це може включати корупцію даних або інформації, яку агент ШІ використовуватиме для виконання завдання, що призведе до упереджених або небажаних відповідей для користувача.

**Пом'якшення:** Регулярно перевіряйте дані, які агент ШІ використовуватиме у своїх робочих процесах. Забезпечте, щоб доступ до цих даних був захищеним і змінювався лише довіреними особами, щоб уникнути цього типу атаки.

### Cascading Errors

**Опис:** Агенти ШІ звертаються до різних інструментів і сервісів для виконання завдань. Помилки, спричинені зловмисниками, можуть призвести до відмов інших систем, з якими пов'язаний агент ШІ, через що атака стає ширшою і складнішою для усунення.

**Пом'якшення**: Один із методів уникнути цього — запускати агента ШІ в обмеженому середовищі, наприклад, виконувати завдання в контейнері Docker, щоб запобігти прямим атакам на систему. Створення механізмів резервного відновлення та логіки повторних спроб при отриманні помилки від певних систем — ще один спосіб уникнути масштабних збоїв.

## Human-in-the-Loop

Another effective way to build trustworthy AI Agent systems is using a Human-in-the-loop. This creates a flow where users are able to provide feedback to the Agents during the run. Users essentially act as agents in a multi-agent system and by providing approval or termination of the running process.

![Людина в циклі](../../../translated_images/uk/human-in-the-loop.5f0068a678f62f4f.webp)

Here is a code snippet using the Microsoft Agent Framework to show how this concept is implemented:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Створити провайдера з затвердженням за участю людини
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Створити агента з кроком затвердження за участю людини
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Користувач може переглянути й затвердити відповідь
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusion

Building trustworthy AI agents requires careful design, robust security measures, and continuous iteration. By implementing structured meta prompting systems, understanding potential threats, and applying mitigation strategies, developers can create AI agents that are both safe and effective. Additionally, incorporating a human-in-the-loop approach ensures that AI agents remain aligned with user needs while minimizing risks. As AI continues to evolve, maintaining a proactive stance on security, privacy, and ethical considerations will be key to fostering trust and reliability in AI-driven systems.

### Got More Questions about Building Trustworthy AI Agents?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Огляд відповідального ШІ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оцінювання генеративних моделей ШІ та застосунків на основі ШІ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системні повідомлення безпеки</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон оцінки ризиків</a>

## Previous Lesson

[Agentic RAG](../05-agentic-rag/README.md)

## Next Lesson

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Відмова від відповідальності:
Цей документ перекладено за допомогою сервісу машинного перекладу на основі ШІ [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, просимо врахувати, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується скористатися професійним людським перекладом. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->