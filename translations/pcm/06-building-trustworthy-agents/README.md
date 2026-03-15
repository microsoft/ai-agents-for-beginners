[![Trustworthy AI Agents](../../../translated_images/pcm/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Click di piksha we dey above to watch video of dis lesson)_

# Building Trustworthy AI Agents

## Introduction

Dis lesson go cover:

- How to build and deploy safe and effective AI Agents
- Important security considerations wen you dey develop AI Agents.
- How to maintain data and user privacy wen you dey develop AI Agents.

## Learning Goals

After you don finish dis lesson, you go sabi how to:

- Identify and reduce risks wen you dey create AI Agents.
- Implement security measures to make sure say data and access dem dey properly managed.
- Create AI Agents wey go maintain data privacy and give beta user experience.

## Safety

Make we first look how to build safe agentic applications. Safety mean say di AI agent go perform as dem design am. As people wey dey build agentic applications, we get methods and tools to maximize safety:

### Building a System Message Framework

If you don ever build AI application wey dey use Large Language Models (LLMs), you know how e important to design strong system prompt or system message. Dem prompts na dem wey set di meta rules, instructions, and guidelines on how di LLM go take interact with user and data.

For AI Agents, di system prompt important pass as AI Agents go need very specific instructions to complete di tasks we design for dem.

To create scalable system prompts, we fit use system message framework to build one or more agents for our application:

![Building a System Message Framework](../../../translated_images/pcm/system-message-framework.3a97368c92d11d68.webp)

#### Step 1: Create a Meta System Message 

Di meta prompt go dey used by LLM to generate di system prompts for di agents wey we create. We go design am as template so dat we fit create multiple agents quick quick if we need am.

Dis na example of meta system message we go give LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Step 2: Create a basic prompt

Di next step na to create basic prompt wey go describe di AI Agent. You suppose put for am di role of di agent, di tasks wey di agent go complete, and any other responsibilities of di agent.

Dis na example:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Step 3: Provide Basic System Message to LLM

Now we fit optimize dis system message by giving di meta system message as system message plus our basic system message.

Dis one go produce system message wey go beta for guiding our AI agents:

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

Di value of dis system message framework na say e go fit scale to create system messages for plenty agents easy plus e go help improve your system messages as time dey go. E nko dey common to get system message wey go work perfectly di first time for your complete use case. To fit make small changes and improve by changing di basic system message and run am through di system go allow you to compare and judge results well well.

## Understanding Threats

To build trustworthy AI agents, e important to understand and reduce di risks and threats to your AI agent. Make we look some of di different threats wey dey AI agents and how you fit better plan and prepare for dem.

![Understanding Threats](../../../translated_images/pcm/understanding-threats.89edeada8a97fc0f.webp)

### Task and Instruction

**Description:** Attackers dey try to change instructions or goals of di AI agent through prompt or by manipulating inputs.

**Mitigation**: Make you do validation checks and input filters to detect any dangerous prompts before di AI Agent fit process dem. Because dis kain attacks for the most part require frequent interaction with di Agent, to limit how many turns conversation fit happen na another way to stop dis kind attack.

### Access to Critical Systems

**Description**: If AI agent get access to systems and services wey dey store sensitive data, attackers fit compromise di communication between di agent and dem services. Dis fit be direct attacks or indirect attempts to gather info about di systems through di agent.

**Mitigation**: AI agents no suppose get access to systems unless e really necessary to prevent dis kind attacks. Di communication between di agent and system gats secure too. To put authentication and access control na another way to protect dis information.

### Resource and Service Overloading

**Description:** AI agents fit access different tools and services to complete tasks. Attackers fit use dis ability to attack those services by sending plenty requests dem through di AI Agent, which fit cause system failure or high costs.

**Mitigation:** Make you put rules to limit how many requests AI agent fit make to any service. Limit how many conversation turns and requests you fit send to AI agent na another way to stop dis kind attacks.

### Knowledge Base Poisoning

**Description:** Dis type attack no target AI agent directly but e target di knowledge base and other services wey AI agent go use. Dis one fit involve corrupting di data or info wey AI agent go use to complete task, wey fit lead to biased or wrong responses to user.

**Mitigation:** Make you regularly check di data wey AI agent dey use for im workflows. Make sure say access to dis data dey secure and only trusted people fit change am to avoid dis kind attack.

### Cascading Errors

**Description:** AI agents dey access different tools and services to complete tasks. Errors caused by attackers fit cause other connected systems to fail, causing di attack to spread and e go hard to fix.

**Mitigation**: One way to avoid dis na to make AI Agent work for limited environment, like inside Docker container, to prevent direct system attacks. To create fallback mechanisms and retry logic when some systems respond with error na another way to avoid big system failures.

## Human-in-the-Loop

Another better way to build trustworthy AI Agent systems na to use Human-in-the-loop. Dis one create flow where users fit give feedback to Agents during im run. Users dey act like agents for multi-agent system by approving or stopping di running process.

![Human in The Loop](../../../translated_images/pcm/human-in-the-loop.5f0068a678f62f4f.webp)

Dis na code snippet wey dey use Microsoft Agent Framework to show how dem implement dis idea:

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

To build trustworthy AI agents, you go need carefull design, strong security measures, and continuous iteration. By use structured meta prompting systems, understanding potential threats and using mitigation strategies, developers fit create AI agents wey safe and effective. Plus, to add human-in-the-loop approach go make sure AI agents dey follow user needs well while e dey reduce risks. As AI dey grow, to maintain good security, privacy and ethical considerations go be key to build trust and reliability for AI-driven systems.

### You Get More Questions about Building Trustworthy AI Agents?

Join [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours and get your AI Agents questions answered.

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
Dis document dem translate am wit AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we try make am correct, abeg sabi say automatic translation fit get mistake or no too clear. The original document wey dem write for im own language na im correct one. If na serious matter, make you use professional human translator. We no go answer if pesin misunderstand or take am wrong because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->