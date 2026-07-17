[![Trustworthy AI Agents](../../../translated_images/pcm/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik di pich we dey oben fo see video fo dis lesson)_

# How to Build Trustworthy AI Agents

## Introductory

Dis lesson go talk about:

- How to build and deploy safe and effective AI Agents
- Important security considerations when developing AI Agents.
- How to maintain data and user privacy when developing AI Agents.

## Wetin you go learn

After you finish dis lesson, you go sabi how to:

- Identify and reduce wahala wen you dey create AI Agents.
- Put security measures so dat data and access go dey well managed.
- Create AI Agents wey go keep data privacy and make users get beta experience.

## Safety

Make we first check how to build safe agentic applications. Safety mean say the AI agent go do wetin dem design am to do. As people wey dey build agentic applications, we get ways and tools to make sure safety high:

### How to Build System Message Framework

If you don ever build AI app wey use Large Language Models (LLMs), you go know how e important to design robust system prompt or system message. Dis prompts dey set meta rules, instructions, and guidelines on how LLM go dey interact with user and data.

For AI Agents, system prompt get even more importance cos AI Agents go need very specific instructions to do the tasks we don design for dem.

To create system prompts wey fit grow, we fit use system message framework to build one or more agents for our application:

![Building a System Message Framework](../../../translated_images/pcm/system-message-framework.3a97368c92d11d68.webp)

#### Step 1: Make Meta System Message 

The meta prompt na wetin LLM go use generate system prompts for the agents wey we create. We go design am as template so dat e go easy to create plenti agents if e reach time.

Dis na example of meta system message we fit give to LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Step 2: Create Basic Prompt

The next step na to create basic prompt to describe the AI Agent. You go put the role of the agent, the tasks the agent go do, plus any other work the agent get.

Example be dis:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Step 3: Give Basic System Message to LLM

Now, we fit make this system message beta by giving meta system message as system message together with our basic system message.

Dis go create system message wey better for guiding our AI agents:

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

#### Step 4: Try and Make Am Better

The koko for this system message framework na to fit scale how you dey create system messages for multiple agents plus how to dey improve your system messages over time. E rare make your system message work well from first time for your full use case. If you fit small small change and improve your basic system message and run am through system fit help you compare and evaluate how e take work.

## Understand Wahala/Threats

To build trustworthy AI agents, e dey important to understand and reduce the risks and wahala wey fit happen to your AI agent. Make we check small of di different wahala wey fit happen to AI agents and how you fit better plan and prepare for dem.

![Understanding Threats](../../../translated_images/pcm/understanding-threats.89edeada8a97fc0f.webp)

### Task and Instruction

**Description:** Wahala makers dey try change di instructions or goals of AI agent through prompting or by manipulating wetin dem input.

**Mitigation**: Make you run validation checks and input filters to catch any dangerous prompts before AI Agent process am. Since dis kain attacks dey need frequent talks with Agent, one way to prevent am na to limit how many times person fit yan for one conversation.

### Access to Critical Systems

**Description**: If AI agent fit get access to systems and services wey dey keep sensitive data, attackers fit spoil communication between agent and these services. Dis fit be direct attack or indirect way to gather info about these systems through agent.

**Mitigation**: AI agents suppose get access to systems on need-only basis to stop dis kind attack. Communication between agent and system suppose secure. Make authentication and access control dey to protect dis info.

### Resource and Service Overloading

**Description:** AI agents fit take different tools and services do tasks. Attackers fit use dis chance send plenty requests through AI Agent to attack these services, wey fit cause system failure or high cost.

**Mitigation:** Make policies dey limit how many requests AI agent fit send to service. Limiting conversation turns and requests to AI agent na another way to stop dis attack.

### Knowledge Base Poisoning

**Description:** Dis kain attack no target AI agent directly but e target the knowledge base and other services wey AI agent go use. Dem fit spoil the data or info wey AI agent go take do task, cause biased or wrong answer to user.

**Mitigation:** Make you dey check the data wey AI agent go use regular. Make sure only trusted people fit change dat data and access suppose secure to avoid dis kind attack.

### Cascading Errors

**Description:** AI agents dey use tools and services do task. Error wey attackers cause fit make other connected systems fail, cause attack to spread and e go hard to fix.

**Mitigation**: One way to avoid dis na to make AI Agent work for limited environment, like inside Docker container, to stop direct system attacks. Another way na to make fallback ways and retry logic if some systems respond with error, to prevent big system failure.

## Human-in-the-Loop

Another koko way to build trustworthy AI Agent systems na to use Human-in-the-loop. E dey make flow where users fit give feedback to Agents while dem dey work. Users go act as agents for multi-agent system by approving or stopping the running process.

![Human in The Loop](../../../translated_images/pcm/human-in-the-loop.5f0068a678f62f4f.webp)

Dis na code snippet wey use Microsoft Agent Framework to show how dem dey do am:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Make the provider wey need human to approve am before e fit run
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Make the agent wey get one step wey human go approve before e continue
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Di user fit check and approve di answer dem give
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusion

To build trustworthy AI agents, you need careful design, strong security, and continuous improvement. By using structured meta prompting systems, understanding threats, and applying ways to reduce wahala, developers fit create AI agents wey safe and effective. Plus, adding human-in-the-loop make sure AI agents dey align with wetin users want and reduce risk. As AI dey grow, to keep proactive about security, privacy, and ethics na key to build trust and reliability for AI systems.

## Code Samples

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Step-by-step demonstration of the meta-prompt system-message framework.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Pre-action approval gates, risk tiering, and audit logging for trustworthy agents.

### You Get More Questions About How to Build Trustworthy AI Agents?

Join di [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and get your AI Agents questions answered.

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