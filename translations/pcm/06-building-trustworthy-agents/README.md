[![Trustworthy AI Agents](../../../translated_images/pcm/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Click di image wey dey above to watch video of dis lesson)_

# Building Trustworthy AI Agents

## Introduction

Dis lesson go cover:

- How to build and deploy safe and effective AI Agents
- Important security things to sabi when you dey develop AI Agents.
- How to maintain data and user privacy when you dey develop AI Agents.

## Learning Goals

After you don finish dis lesson, you go sabi how to:

- Identify and reduce risks when you dey create AI Agents.
- Put security measures for place to make sure say data and access dey properly managed.
- Create AI Agents wey go keep data privacy and give good user experience.

## Safety

Make we first look how to build safe agentic applications. Safety mean say the AI agent dey perform as e suppose do. As people wey dey build agentic applications, we get methods and tools to maximize safety:

### Building a System Message Framework

If you don ever build AI application using Large Language Models (LLMs), you go sabi how important e be to design strong system prompt or system message. Dem prompts na im dey set the meta rules, instructions, and guidelines on how the LLM go take interact with user and data.

For AI Agents, the system prompt matter even more cos AI Agents go need very specific instructions to complete the tasks wey we design for dem.

To create system prompts wey fit grow, we fit use system message framework to build one or more agents for our application:

![Building a System Message Framework](../../../translated_images/pcm/system-message-framework.3a97368c92d11d68.webp)

#### Step 1: Create a Meta System Message 

The meta prompt na im LLM go use generate system prompts for the agents wey we dey create. We design am as template so dat we fit create many agents easily if we need am.

Here na example of meta system message we fit give LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Step 2: Create a basic prompt

Di next step na to create basic prompt to describe di AI Agent. You suppose include di role of di agent, di tasks wey di agent go do, plus any other responsibilities of di agent.

Here na example:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Step 3: Provide Basic System Message to LLM

Now we fit optimize dis system message by providing di meta system message as di system message together with our basic system message.

Dis one go produce better system message wey go fit guide our AI agents well:

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

Di value of dis system message framework na say e go make am easy to scale system messages from many agents plus to improve your system messages over time. E dey rare to get system message wey go work perfect di first time for your whole use case. To fit make small changes and better your messages by changing di basic system message and pass am through di system go allow you compare and check di results.

## Understanding Threats

To build trustworthy AI agents, e important to sabi and reduce di risks and threats wey fit affect your AI agent. Make we look some wia different threats fit affect AI agents and how you fit plan and prepare well for dem.

![Understanding Threats](../../../translated_images/pcm/understanding-threats.89edeada8a97fc0f.webp)

### Task and Instruction

**Description:** Bad people dey try change instructions or goals of AI agent through prompting or manipulating inputs.

**Mitigation**: Make you run validation checks and input filters to catch dangerous prompts before AI Agent process dem. Because dis kind attack dey normally need plenty interaction with Agent, you fit reduce di number of turns for conversation as another way to block dis kind attacks.

### Access to Critical Systems

**Description**: If AI agent get access to systems or services wey store sensitive data, attackers fit spoil communication between agent and those services. Dem fit do direct attack or try gather info about systems through di agent.

**Mitigation**: AI agents suppose get access only wen e really need am to prevent dis kind attacks. Communication between agent and system must also dey secure. Put authentication and access control for place na another way to protect dis info.

### Resource and Service Overloading

**Description:** AI agents fit use different tools and services to do tasks. Bad people fit use this power finish those services by sending plenty requests through AI Agent, wey fit cause system failure or high cost.

**Mitigation:** Setup policies to limit how many requests AI agent fit send to service. To reduce number of conversation turns and requests to AI agent na another way to stop dis attacks.

### Knowledge Base Poisoning

**Description:** Dis kind attack no target AI agent directly but e target knowledge base and other services wey AI agent go use. Dem fit spoil data or info wey AI agent go use do task, wey fit cause biased or wrong answers to user.

**Mitigation:** Make you dey check data wey AI agent dey use regularly. Make sure say access to dis data dey secure and e fit only change by trusted persons to avoid dis attack.

### Cascading Errors

**Description:** AI agents dey use different tools and services to complete tasks. Errors wey attackers cause fit lead to other system failures wey AI agent dey connected to, which fit make attack spread and e go hard to fix.

**Mitigation**: One way to avoid dis na to make AI Agent run only for limited environment, like to perform tasks inside one Docker container to stop direct system attacks. To create fallback system and retry logic if some systems respond with error na another way to prevent bigger system failures.

## Human-in-the-Loop

Another good way to build trustworthy AI Agent systems na to use Human-in-the-loop. Dis one create flow wey make users fit give feedback to Agents during dem dey run. Users go act as agents inside multi-agent system and dem fit approve or stop di running process.

![Human in The Loop](../../../translated_images/pcm/human-in-the-loop.5f0068a678f62f4f.webp)

Here na code snippet using Microsoft Agent Framework to show how dem implement dis idea:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Make di provider wit human-in-the-loop approval
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Make di agent wit human approval step
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Di user fit check and approve di response
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusion

To build trustworthy AI agents require careful design, strong security measures, and constant update. By putting structured meta prompting systems, understanding possible threats, and applying ways to reduce dem, developers fit create AI agents wey both safe and effective. Plus, to add human-in-the-loop approach go make sure say AI agents go dey aligned with users needs while e dey reduce risk. As AI go dey grow, to keep proactive on security, privacy, and ethical considerations go be key to build trust and reliability for AI-driven systems.

## Code Samples

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Step-by-step demonstration of the meta-prompt system-message framework.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Pre-action approval gates, risk tiering, and audit logging for trustworthy agents.

### Got More Questions about Building Trustworthy AI Agents?

Come join [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours and get your AI Agents questions answered.

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

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->