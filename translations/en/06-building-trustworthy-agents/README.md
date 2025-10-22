<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-30T13:03:41+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "en"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.en.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Click the image above to view video of this lesson)_

# Building Trustworthy AI Agents

## Introduction

This lesson will cover:

- How to build and deploy safe and effective AI Agents
- Key security considerations when developing AI Agents
- How to ensure data and user privacy when creating AI Agents

## Learning Goals

After completing this lesson, you will know how to:

- Identify and address risks when developing AI Agents
- Implement security measures to properly manage data and access
- Create AI Agents that prioritize data privacy and deliver a quality user experience

## Safety

Let’s start by exploring how to build safe agentic applications. Safety means ensuring the AI agent performs as intended. As developers of agentic applications, we have tools and methods to maximize safety:

### Building a System Message Framework

If you’ve ever developed an AI application using Large Language Models (LLMs), you understand the importance of crafting a strong system prompt or system message. These prompts define the rules, instructions, and guidelines for how the LLM interacts with users and data.

For AI Agents, the system prompt is even more critical because the agents require highly specific instructions to complete the tasks they are designed for.

To create scalable system prompts, we can use a system message framework to build one or more agents within our application:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.en.png)

#### Step 1: Create a Meta System Message 

The meta prompt is used by an LLM to generate system prompts for the agents we create. It’s designed as a template to efficiently create multiple agents if needed.

Here’s an example of a meta system message we might provide to the LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Step 2: Create a Basic Prompt

The next step is to create a basic prompt that describes the AI Agent. This should include the agent’s role, the tasks it will perform, and any other responsibilities.

Here’s an example:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Step 3: Provide Basic System Message to LLM

We can now optimize this system message by combining the meta system message with the basic system message.

This will generate a system message that is better suited to guide our AI agents:

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

The advantage of this system message framework is that it simplifies the process of creating system messages for multiple agents and allows for continuous improvement. It’s rare for a system message to work perfectly for all use cases on the first attempt. Making small adjustments to the basic system message and running it through the framework enables you to compare and refine results.

## Understanding Threats

To build trustworthy AI agents, it’s essential to understand and mitigate risks and threats. Let’s examine some common threats to AI agents and strategies to address them.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.en.png)

### Task and Instruction

**Description:** Attackers attempt to alter the instructions or goals of the AI agent by manipulating prompts or inputs.

**Mitigation:** Use validation checks and input filters to detect potentially harmful prompts before they are processed by the AI Agent. Since these attacks often require repeated interactions, limiting the number of conversation turns is another effective prevention method.

### Access to Critical Systems

**Description:** If an AI agent has access to systems or services containing sensitive data, attackers may exploit the communication between the agent and these systems. This can involve direct attacks or indirect attempts to extract information through the agent.

**Mitigation:** Restrict the AI agent’s access to systems on a need-only basis. Secure communication between the agent and systems, and implement authentication and access controls to safeguard sensitive information.

### Resource and Service Overloading

**Description:** AI agents can interact with various tools and services to complete tasks. Attackers may exploit this by sending excessive requests through the agent, potentially causing system failures or incurring high costs.

**Mitigation:** Set policies to limit the number of requests an AI agent can make to a service. Restricting the number of conversation turns and requests to the agent can also help prevent such attacks.

### Knowledge Base Poisoning

**Description:** This attack targets the knowledge base or services the AI agent relies on, corrupting the data or information the agent uses to perform tasks. This can lead to biased or unintended responses.

**Mitigation:** Regularly verify the data the AI agent uses in its workflows. Ensure that access to this data is secure and limited to trusted individuals to prevent tampering.

### Cascading Errors

**Description:** AI agents often rely on multiple tools and services to complete tasks. Errors caused by attackers can lead to failures in connected systems, making the attack more widespread and harder to resolve.

**Mitigation:** Operate the AI agent in a controlled environment, such as a Docker container, to minimize direct system attacks. Implement fallback mechanisms and retry logic to handle errors from connected systems and prevent larger failures.

## Human-in-the-Loop

Another effective approach to building trustworthy AI Agent systems is incorporating a Human-in-the-loop. This allows users to provide feedback to the agents during their operation. Users essentially act as agents in a multi-agent system, approving or terminating processes as needed.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.en.png)

Here’s a code snippet using AutoGen to demonstrate this concept:

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

## Conclusion

Creating trustworthy AI agents requires thoughtful design, strong security measures, and ongoing refinement. By using structured meta prompting systems, understanding potential threats, and applying mitigation strategies, developers can build AI agents that are both safe and effective. Additionally, integrating a human-in-the-loop approach ensures that AI agents remain aligned with user needs while minimizing risks. As AI technology advances, prioritizing security, privacy, and ethical considerations will be crucial for fostering trust and reliability in AI-driven systems.

### Got More Questions about Building Trustworthy AI Agents?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI Agent questions answered.

## Additional Resources

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Responsible AI overview</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluation of generative AI models and AI applications</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Safety system messages</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risk Assessment Template</a>

## Previous Lesson

[Agentic RAG](../05-agentic-rag/README.md)

## Next Lesson

[Planning Design Pattern](../07-planning-design/README.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.